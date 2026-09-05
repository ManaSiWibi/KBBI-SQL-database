#!/usr/bin/env python3
"""Derive request-time similar-context words from the Leipzig cooccurrence data.

The downloaded 100K archive does not contain the portal's ``sim_w_co`` table.
This script therefore computes a documented approximation: binary, symmetric
profiles over source-selected neighbour and same-sentence edges, compared with
cosine similarity.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(directory: Path, name: str) -> object:
    path = directory / name
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or len(data) != 1:
        raise ValueError(f"{path}: expected one-key JSON envelope")
    return next(iter(data.values()))


def build_profiles(directory: Path, min_significance: float) -> tuple[dict[int, dict[str, object]], dict[int, set[tuple[str, int]]], dict[tuple[str, int], set[int]]]:
    words = {row["id"]: row for row in load(directory, "leipzig_words__JSON.json")}
    profiles: defaultdict[int, set[tuple[str, int]]] = defaultdict(set)
    inverted: defaultdict[tuple[str, int], set[int]] = defaultdict(set)
    for filename, relation_type in (
        ("leipzig_neighbour_cooccurrences__JSON.json", "neighbour"),
        ("leipzig_sentence_cooccurrences__JSON.json", "sentence"),
    ):
        for row in load(directory, filename):
            if row["significance"] < min_significance:
                continue
            word1, word2 = row["word1_id"], row["word2_id"]
            for source, target in ((word1, word2), (word2, word1)):
                feature = (relation_type, target)
                profiles[source].add(feature)
                inverted[feature].add(source)
    return words, profiles, inverted


def find_similar(
    query_id: int,
    words: dict[int, dict[str, object]],
    profiles: dict[int, set[tuple[str, int]]],
    inverted: dict[tuple[str, int], set[int]],
    top_k: int,
    min_shared: int,
) -> list[dict[str, object]]:
    query_profile = profiles.get(query_id, set())
    if not query_profile:
        return []

    shared: Counter[int] = Counter()
    # ponytail: query mode only; all-word similarity belongs in a batch index.
    for feature in query_profile:
        for candidate in inverted.get(feature, ()):
            if candidate != query_id:
                shared[candidate] += 1

    query_size = len(query_profile)
    results = []
    for candidate, common in shared.items():
        if common < min_shared:
            continue
        candidate_size = len(profiles[candidate])
        score = common / math.sqrt(query_size * candidate_size)
        results.append(
            {
                "similar_word_id": candidate,
                "similar_word": words[candidate]["word"],
                "similarity": round(score, 12),
                "common_contexts": common,
            }
        )
    results.sort(key=lambda row: (-row["similarity"], -row["common_contexts"], row["similar_word"], row["similar_word_id"]))
    return results[:top_k]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--word", help="exact word to query")
    target.add_argument("--word-id", type=int, help="Leipzig numeric word ID to query")
    parser.add_argument("--top-k", type=int, default=20)
    parser.add_argument("--min-shared", type=int, default=2)
    parser.add_argument("--min-significance", type=float, default=0.0)
    parser.add_argument("--dataset-dir", default="leipzig", help="Leipzig dataset directory (default: leipzig)")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.top_k < 1 or args.min_shared < 1:
        parser.error("--top-k and --min-shared must be positive")

    directory = ROOT / args.dataset_dir
    if not directory.is_dir():
        parser.error(f"unknown dataset directory: {args.dataset_dir}")
    words, profiles, inverted = build_profiles(directory, args.min_significance)
    if args.word_id is not None:
        query_id = args.word_id
        if query_id not in words:
            parser.error(f"unknown Leipzig word ID: {query_id}")
    else:
        matches = [word_id for word_id, row in words.items() if row["word"] == args.word]
        if not matches:
            parser.error(f"unknown Leipzig word: {args.word!r}")
        if len(matches) > 1:
            parser.error(f"word is ambiguous; use --word-id: {matches}")
        query_id = matches[0]

    payload = {
        "leipzig_context_similarity": {
            "query": {"word_id": query_id, "word": words[query_id]["word"]},
            "dataset_dir": args.dataset_dir,
            "algorithm": "binary cosine over symmetric co_n/co_s profiles",
            "parameters": {
                "top_k": args.top_k,
                "min_shared": args.min_shared,
                "min_significance": args.min_significance,
                "profile_features": ["neighbour", "sentence"],
                "portal_sim_w_co_reproduced": False,
            },
            "results": find_similar(
                query_id,
                words,
                profiles,
                inverted,
                args.top_k,
                args.min_shared,
            ),
        }
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
