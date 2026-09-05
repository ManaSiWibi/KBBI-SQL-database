#!/usr/bin/env python3
"""Import the Indonesian slice of a droher/etymology-db CSV.GZ release."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS = (
    "term_id",
    "lang",
    "term",
    "reltype",
    "related_term_id",
    "related_lang",
    "related_term",
    "position",
    "group_tag",
    "parent_tag",
    "parent_position",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def optional_text(value: str) -> str | None:
    value = value.strip()
    return value or None


def optional_int(value: str) -> int | None:
    value = value.strip()
    return int(value) if value else None


def import_rows(source: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows: list[dict[str, object]] = []
    relation_types: Counter[str] = Counter()
    related_languages: Counter[str] = Counter()
    source_languages: set[str] = set()
    terms: set[str] = set()
    linked_terms: set[str] = set()
    total_rows = 0
    with gzip.open(source, "rt", encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise ValueError(f"unexpected source fields: {reader.fieldnames!r}")
        for raw in reader:
            total_rows += 1
            source_languages.add(raw["lang"])
            if raw["lang"].casefold() != "indonesian":
                continue
            row = {
                "term_id": raw["term_id"],
                "lang": raw["lang"],
                "term": raw["term"],
                "reltype": raw["reltype"],
                "related_term_id": optional_text(raw["related_term_id"]),
                "related_lang": optional_text(raw["related_lang"]),
                "related_term": optional_text(raw["related_term"]),
                "position": optional_int(raw["position"]),
                "group_tag": optional_text(raw["group_tag"]),
                "parent_tag": optional_text(raw["parent_tag"]),
                "parent_position": optional_int(raw["parent_position"]),
            }
            rows.append(row)
            terms.add(raw["term"].casefold())
            relation_types[raw["reltype"]] += 1
            if row["related_lang"] and row["related_term"]:
                linked_terms.add(raw["term"].casefold())
                related_languages[str(row["related_lang"])] += 1

    if not rows:
        raise ValueError("source contains no Indonesian rows")
    metadata = {
        "source_rows": total_rows,
        "source_languages": len(source_languages),
        "indonesian_rows": len(rows),
        "indonesian_terms_casefolded": len(terms),
        "indonesian_terms_with_linked_related_term": len(linked_terms),
        "relation_types": dict(sorted(relation_types.items())),
        "related_languages": dict(related_languages.most_common()),
    }
    return rows, metadata


def write_json(path: Path, root_key: str, value: object) -> None:
    path.write_text(
        json.dumps({root_key: value}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="etymology.csv.gz release asset")
    parser.add_argument("--output", default="etymology-db", help="repository-relative output directory")
    parser.add_argument("--generated-at", required=True)
    parser.add_argument("--release", default="2023-12")
    parser.add_argument("--release-commit", default="35bf42b")
    parser.add_argument(
        "--source-url",
        default="https://github.com/droher/etymology-db",
    )
    parser.add_argument(
        "--download-url",
        default="https://github.com/droher/etymology-db/releases/download/2023-12/etymology.csv.gz",
    )
    args = parser.parse_args()

    rows, scope = import_rows(args.input)
    output = ROOT / args.output
    output.mkdir(parents=True, exist_ok=True)
    metadata = {
        "source": "droher/etymology-db",
        "release": args.release,
        "release_commit": args.release_commit,
        "source_url": args.source_url,
        "download_url": args.download_url,
        "generated_at": args.generated_at,
        "asset_bytes": args.input.stat().st_size,
        "asset_sha256": sha256(args.input),
        "selection": "rows where lang casefolds to Indonesian",
        "ordering": "source CSV order",
        "license": "CC ShareAlike 3.0 according to the source README; underlying Wiktionary terms and attribution requirements apply",
        "validation_note": "source author reports semi-structured Wiktionary parsing and no systematic validation of individual results",
        "scope": scope,
    }
    write_json(output / "etymology_db_indonesian__JSON.json", "etymology_db_indonesian", rows)
    write_json(output / "etymology_metadata__JSON.json", "etymology_db_metadata", metadata)
    print(json.dumps({"scope": scope, "asset_sha256": metadata["asset_sha256"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
