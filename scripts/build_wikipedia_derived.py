#!/usr/bin/env python3
"""Build a bounded, Leipzig-compatible corpus from an Indonesian Wikipedia dump prefix."""

from __future__ import annotations

import argparse
import bz2
import hashlib
import html
import itertools
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path


TOKEN_RE = re.compile(r"[^\W\d_]+(?:['’\-][^\W\d_]+)*|\d+(?:[.,]\d+)?", re.UNICODE)
ROOT = Path(__file__).resolve().parents[1]


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def clean_wikitext(text: str) -> str:
    """Remove markup conservatively; this is not a full MediaWiki parser."""
    text = html.unescape(text)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(
        r"<(?:ref|math|gallery|timeline|source|syntaxhighlight|nowiki)\b[^>]*>.*?</(?:ref|math|gallery|timeline|source|syntaxhighlight|nowiki)\s*>",
        " ",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(r"<(?:ref|math|gallery|timeline|source|syntaxhighlight|nowiki)\b[^>]*/>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"\{\|.*?\|\}", " ", text, flags=re.DOTALL)
    # ponytail: bounded innermost-template removal; use a MediaWiki parser if markup fidelity matters.
    for _ in range(12):
        replaced = re.sub(r"\{\{[^{}]*\}\}", " ", text)
        if replaced == text:
            break
        text = replaced
    text = re.sub(r"\[\[(?:File|Berkas|Category|Kategori):[^\]]*\]\]", " ", text, flags=re.IGNORECASE)
    for _ in range(3):
        replaced = re.sub(r"\[\[([^\[\]|]+)\|([^\[\]]+)\]\]", r"\2", text)
        replaced = re.sub(r"\[\[([^\[\]]+)\]\]", r"\1", replaced)
        if replaced == text:
            break
        text = replaced
    text = re.sub(r"\[[^\s\]]+\s+([^\]]+)\]", r"\1", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^\s*=+\s*(.*?)\s*=+\s*$", r"\1", text, flags=re.MULTILINE)
    text = re.sub(r"'{2,5}", "", text)
    text = re.sub(r"^\s*[*#:;]+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"[\[\]{}|]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def sentence_candidates(text: str, minimum: int, maximum: int) -> list[str]:
    cleaned = clean_wikitext(text)
    candidates = re.split(r"(?<=[.!?。！？])\s+|\n+", cleaned)
    return [
        sentence.strip()
        for sentence in candidates
        if minimum <= len(sentence.strip()) <= maximum
        and re.search(r"[^\W\d_]", sentence, re.UNICODE)
    ]


def read_sample(path: Path, target: int, minimum: int, maximum: int) -> tuple[list[str], dict[str, int]]:
    sentences: list[str] = []
    pages = article_pages = candidates = 0
    parser = ET.XMLPullParser(events=("end",))
    decompressor = bz2.BZ2Decompressor()

    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            try:
                decompressed = decompressor.decompress(chunk)
            except OSError:
                break
            if not decompressed:
                continue
            parser.feed(decompressed)
            for _, element in parser.read_events():
                if local_name(element.tag) != "page":
                    continue
                pages += 1
                namespace = next(
                    (child.text or "" for child in element.iter() if local_name(child.tag) == "ns"),
                    "",
                )
                redirect = any(local_name(child.tag) == "redirect" for child in element)
                texts = [child.text or "" for child in element.iter() if local_name(child.tag) == "text"]
                if namespace != "0" or redirect or not texts:
                    element.clear()
                    continue
                article_pages += 1
                page_sentences = sentence_candidates(texts[-1], minimum, maximum)
                candidates += len(page_sentences)
                for sentence in page_sentences:
                    sentences.append(sentence)
                    if len(sentences) >= target:
                        return sentences, {
                            "pages_seen": pages,
                            "article_pages_seen": article_pages,
                            "candidate_sentences_seen": candidates,
                            "compressed_prefix_complete": int(decompressor.eof),
                        }
                element.clear()

    return sentences, {
        "pages_seen": pages,
        "article_pages_seen": article_pages,
        "candidate_sentences_seen": candidates,
        "compressed_prefix_complete": int(decompressor.eof),
    }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def dice_score(frequency: int, first_frequency: int, second_frequency: int) -> float:
    denominator = first_frequency + second_frequency
    return round(200.0 * frequency / denominator, 2) if denominator else 0.0


def write_json(path: Path, root_key: str, value: object) -> None:
    path.write_text(
        json.dumps({root_key: value}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def build(args: argparse.Namespace) -> dict[str, object]:
    source = Path(args.input)
    output = ROOT / args.output
    output.mkdir(parents=True, exist_ok=True)
    sentences, parse_stats = read_sample(
        source,
        args.sample_sentences,
        args.minimum_sentence_chars,
        args.maximum_sentence_chars,
    )
    if len(sentences) < args.sample_sentences:
        raise ValueError(f"prefix yielded {len(sentences)} sentences; expected {args.sample_sentences}")

    tokenized = [tuple(match.group(0).casefold() for match in TOKEN_RE.finditer(sentence)) for sentence in sentences]
    tokenized = [(sentence, tokens) for sentence, tokens in zip(sentences, tokenized) if tokens]
    if len(tokenized) != len(sentences):
        raise ValueError("some retained sentences have no tokens")

    word_frequency: Counter[str] = Counter()
    sentence_occurrence: Counter[str] = Counter()
    word_sentence_ids: defaultdict[str, list[int]] = defaultdict(list)
    neighbour_frequency: Counter[tuple[str, str]] = Counter()
    neighbour_outgoing: Counter[str] = Counter()
    neighbour_incoming: Counter[str] = Counter()
    sentence_frequency: Counter[tuple[str, str]] = Counter()
    capped_sentences = 0
    total_neighbour_events = 0

    for sentence_id, (_, tokens) in enumerate(tokenized, start=1):
        word_frequency.update(tokens)
        unique_tokens = set(tokens)
        for word in unique_tokens:
            sentence_occurrence[word] += 1
            word_sentence_ids[word].append(sentence_id)
        for first, second in itertools.pairwise(tokens):
            if first != second:
                neighbour_frequency[(first, second)] += 1
                neighbour_outgoing[first] += 1
                neighbour_incoming[second] += 1
                total_neighbour_events += 1
        pair_tokens = sorted(unique_tokens)
        if len(pair_tokens) > args.maximum_unique_tokens_per_sentence:
            # ponytail: cap O(n²) pair expansion; raise this only with a memory budget.
            pair_tokens = pair_tokens[: args.maximum_unique_tokens_per_sentence]
            capped_sentences += 1
        sentence_frequency.update(itertools.combinations(pair_tokens, 2))

    words = sorted(word_frequency)
    word_ids = {word: index for index, word in enumerate(words, start=1)}
    word_rows = [
        {"id": word_ids[word], "word": word, "frequency": word_frequency[word]}
        for word in words
    ]
    sentence_rows = [
        {"id": sentence_id, "text": sentence}
        for sentence_id, (sentence, _) in enumerate(tokenized, start=1)
    ]
    index_rows = [
        {"word_id": word_ids[word], "sentence_ids": sentence_ids}
        for word, sentence_ids in sorted(word_sentence_ids.items())
    ]
    neighbour_rows = [
        {
            "word1_id": word_ids[first],
            "word2_id": word_ids[second],
            "frequency": frequency,
            "significance": dice_score(frequency, neighbour_outgoing[first], neighbour_incoming[second]),
        }
        for (first, second), frequency in sorted(neighbour_frequency.items())
        if frequency >= args.minimum_neighbour_frequency
    ]
    sentence_rows_cooccurrence = [
        {
            "word1_id": word_ids[first],
            "word2_id": word_ids[second],
            "frequency": frequency,
            "significance": dice_score(frequency, sentence_occurrence[first], sentence_occurrence[second]),
        }
        for (first, second), frequency in sorted(sentence_frequency.items())
        if frequency >= args.minimum_sentence_frequency
    ]

    metadata = {
        "corpus_id": args.corpus_id,
        "source": "Indonesian Wikipedia (Wikimedia dump)",
        "genre": "Wikipedia",
        "year": 2026,
        "dump_id": args.dump_id,
        "source_url": args.source_url,
        "source_stream_url": args.source_stream_url,
        "source_sha1": args.source_sha1,
        "source_bytes": args.source_bytes,
        "source_part_sha1": args.source_part_sha1,
        "source_part_bytes": args.source_part_bytes,
        "prefix": {
            "bytes": source.stat().st_size,
            "sha256": sha256(source),
            "sampling": "first accepted sentences from the deterministic compressed byte prefix",
            "full_dump_included": False,
        },
        "sample": {
            "sentences": len(sentence_rows),
            "pages_seen": parse_stats["pages_seen"],
            "article_pages_seen": parse_stats["article_pages_seen"],
            "candidate_sentences_seen": parse_stats["candidate_sentences_seen"],
            "compressed_prefix_complete": bool(parse_stats["compressed_prefix_complete"]),
        },
        "normalization": {
            "wikitext": "conservative regex cleanup; templates, references, tables, links, HTML, and formatting markup removed",
            "casefold": True,
            "tokenizer": "Unicode letters with optional internal apostrophe/hyphen, plus numeric tokens",
            "sentence_filter": {
                "minimum_characters": args.minimum_sentence_chars,
                "maximum_characters": args.maximum_sentence_chars,
            },
        },
        "cooccurrence": {
            "neighbour": "directed adjacent token bigrams; identical-token edges omitted",
            "sentence": "unique unordered token pairs per sentence",
            "maximum_unique_tokens_per_sentence": args.maximum_unique_tokens_per_sentence,
            "capped_sentences": capped_sentences,
            "minimum_neighbour_frequency": args.minimum_neighbour_frequency,
            "minimum_sentence_frequency": args.minimum_sentence_frequency,
            "association_score": "Dice coefficient multiplied by 100, stored as significance for Leipzig-compatible schema",
        },
        "retained": {
            "words": len(word_rows),
            "sentences": len(sentence_rows),
            "word_sentence_index": len(index_rows),
            "word_sentence_occurrences": sum(len(row["sentence_ids"]) for row in index_rows),
            "neighbour_events": total_neighbour_events,
            "neighbour_cooccurrences_before_frequency_filter": len(neighbour_frequency),
            "neighbour_cooccurrences": len(neighbour_rows),
            "sentence_cooccurrences_before_frequency_filter": len(sentence_frequency),
            "sentence_cooccurrences": len(sentence_rows_cooccurrence),
        },
        "license_note": "Wikimedia and Wikipedia licensing terms apply, including CC BY-SA/GFDL and possible third-party exceptions; review the linked Terms of Use before redistribution.",
        "derived_not_official_leipzig": True,
        "similar_context": {
            "source_file_present": False,
            "derivation": "the repository similarity script consumes the same six-file relation shape; it does not reproduce Leipzig portal sim_w_co",
            "input_files": [
                "leipzig_neighbour_cooccurrences__JSON.json",
                "leipzig_sentence_cooccurrences__JSON.json",
            ],
        },
    }

    write_json(output / "leipzig_metadata__JSON.json", "leipzig_wikipedia_2026_metadata", metadata)
    write_json(output / "leipzig_words__JSON.json", "leipzig_words", word_rows)
    write_json(output / "leipzig_sentences__JSON.json", "leipzig_sentences", sentence_rows)
    write_json(output / "leipzig_word_sentence_index__JSON.json", "leipzig_word_sentence_index", index_rows)
    write_json(output / "leipzig_neighbour_cooccurrences__JSON.json", "leipzig_neighbour_cooccurrences", neighbour_rows)
    write_json(output / "leipzig_sentence_cooccurrences__JSON.json", "leipzig_sentence_cooccurrences", sentence_rows_cooccurrence)
    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="compressed bzip2 dump prefix")
    parser.add_argument("--output", required=True, help="repository-relative output directory")
    parser.add_argument("--sample-sentences", type=int, default=100_000)
    parser.add_argument("--minimum-sentence-chars", type=int, default=20)
    parser.add_argument("--maximum-sentence-chars", type=int, default=5_000)
    parser.add_argument("--maximum-unique-tokens-per-sentence", type=int, default=100)
    parser.add_argument("--minimum-neighbour-frequency", type=int, default=3)
    parser.add_argument("--minimum-sentence-frequency", type=int, default=6)
    parser.add_argument("--corpus-id", required=True)
    parser.add_argument("--dump-id", required=True)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--source-stream-url", required=True)
    parser.add_argument("--source-sha1", required=True)
    parser.add_argument("--source-bytes", type=int, required=True)
    parser.add_argument("--source-part-sha1", required=True)
    parser.add_argument("--source-part-bytes", type=int, required=True)
    args = parser.parse_args()
    if (
        args.sample_sentences < 1
        or args.maximum_unique_tokens_per_sentence < 2
        or args.minimum_neighbour_frequency < 1
        or args.minimum_sentence_frequency < 1
    ):
        parser.error("sample and pair limits must be positive")

    metadata = build(args)
    print(json.dumps({"retained": metadata["retained"], "prefix": metadata["prefix"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
