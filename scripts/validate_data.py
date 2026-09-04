#!/usr/bin/env python3
"""Validate canonical JSON envelopes, provenance, joins, and cross-references."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "dataset_manifest__JSON.json"


class ValidationError(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def envelope(path: Path) -> tuple[str, object]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        fail(f"{path.relative_to(ROOT)}: cannot parse UTF-8 JSON: {error}")
    if not isinstance(data, dict) or len(data) != 1:
        fail(f"{path.relative_to(ROOT)}: expected exactly one root key")
    return next(iter(data)), next(iter(data.values()))


def assert_manifest(files: list[Path]) -> None:
    manifest_key, manifest_value = envelope(MANIFEST_PATH)
    if manifest_key != "dataset_manifest" or not isinstance(manifest_value, dict):
        fail("dataset_manifest__JSON.json: invalid manifest envelope")
    if manifest_value.get("schema_version") != 1:
        fail("dataset manifest: unsupported schema_version")
    if manifest_value.get("canonical_format") != "JSON":
        fail("dataset manifest: canonical_format must be JSON")

    expected = {path.relative_to(ROOT).as_posix(): path for path in files}
    manifest_files: dict[str, dict[str, object]] = {}
    directories = manifest_value.get("datasets")
    if not isinstance(directories, list):
        fail("dataset manifest: datasets must be an array")
    for dataset in directories:
        if not isinstance(dataset, dict):
            fail("dataset manifest: dataset entry must be an object")
        directory = dataset.get("directory")
        source_urls = dataset.get("source_urls")
        if not isinstance(directory, str):
            fail("dataset manifest: missing directory")
        if not isinstance(source_urls, list) or not source_urls:
            fail(f"{directory}: missing source_urls")
        if not dataset.get("license_status") or not dataset.get("provenance_status"):
            fail(f"{directory}: missing license/provenance status")
        for record in dataset.get("files", []):
            if not isinstance(record, dict) or not isinstance(record.get("path"), str):
                fail(f"{directory}: invalid file record")
            path = record["path"]
            if path in manifest_files:
                fail(f"dataset manifest: duplicate path {path}")
            manifest_files[path] = record

    if set(manifest_files) != set(expected):
        fail(
            "dataset manifest file set mismatch: "
            f"missing={sorted(set(expected) - set(manifest_files))}, "
            f"extra={sorted(set(manifest_files) - set(expected))}"
        )
    for path_string, path in expected.items():
        root_key, value = envelope(path)
        record = manifest_files[path_string]
        value_type = "array" if isinstance(value, list) else type(value).__name__
        record_count = len(value) if isinstance(value, list) else None
        checks = {
            "root_key": root_key,
            "value_type": value_type,
            "record_count": record_count,
            "sha256": sha256(path),
        }
        for field, actual in checks.items():
            if record.get(field) != actual:
                fail(f"{path_string}: manifest {field}={record.get(field)!r}, expected {actual!r}")


def assert_readmes(files: list[Path]) -> None:
    for path in files:
        readme = path.parent / "README.md"
        if not readme.exists():
            fail(f"{path.parent.relative_to(ROOT)}: missing README.md")
        text = readme.read_text(encoding="utf-8")
        if "http://" not in text and "https://" not in text:
            fail(f"{readme.relative_to(ROOT)}: missing source URL")


def assert_kbbi_v5() -> None:
    _, rows = envelope(ROOT / "kbbi-v5/kbbi_v5__JSON.json")
    if not isinstance(rows, list):
        fail("kbbi-v5: value must be an array")
    fingerprints = [json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")) for row in rows]
    if len(fingerprints) != len(set(fingerprints)):
        fail("kbbi-v5: exact duplicate rows remain")
    etimology_rows = [row for row in rows if row.get("etimologi") is not None]
    if any(not isinstance(row.get("etimologi"), str) for row in etimology_rows):
        fail("kbbi-v5: non-null etimologi must remain raw strings")
    if any(not isinstance(row.get("etimologi_parsed"), dict) for row in etimology_rows):
        fail("kbbi-v5: every non-null etimologi needs etimologi_parsed")
    if any("etimologi_parsed" in row and row.get("etimologi") is None for row in rows):
        fail("kbbi-v5: parsed etimology exists without raw etimologi")


def assert_wordnet() -> None:
    _, memberships = envelope(ROOT / "wordnet-bahasa/wordnet_indonesian__JSON.json")
    _, enrichment = envelope(ROOT / "wordnet-bahasa/wordnet_indonesian_enrichment__JSON.json")
    if not isinstance(memberships, list) or not isinstance(enrichment, list):
        fail("WordNet: membership and enrichment values must be arrays")
    if len(memberships) != len(enrichment):
        fail("WordNet: enrichment must preserve one row per membership")
    for membership, enriched in zip(memberships, enrichment):
        for field in ("synset", "lang", "goodness", "lemma"):
            if enriched.get(field) != membership.get(field):
                fail(f"WordNet: enrichment mismatch in {field}")
        if not isinstance(enriched.get("definitions"), list):
            fail("WordNet: definitions must always be an array")
        if enriched.get("has_definition") != bool(enriched["definitions"]):
            fail("WordNet: has_definition disagrees with definitions")


def assert_leipzig() -> None:
    _, words = envelope(ROOT / "leipzig/leipzig_words__JSON.json")
    _, sentences = envelope(ROOT / "leipzig/leipzig_sentences__JSON.json")
    _, index = envelope(ROOT / "leipzig/leipzig_word_sentence_index__JSON.json")
    if not all(isinstance(value, list) for value in (words, sentences, index)):
        fail("Leipzig: words, sentences, and index must be arrays")
    word_ids = {row.get("id") for row in words}
    sentence_ids = {row.get("id") for row in sentences}
    if len(word_ids) != len(words) or len(sentence_ids) != len(sentences):
        fail("Leipzig: word and sentence IDs must be unique")
    for row in index:
        if row.get("word_id") not in word_ids:
            fail(f"Leipzig: index references unknown word {row.get('word_id')}")
        if not isinstance(row.get("sentence_ids"), list):
            fail(f"Leipzig: sentence_ids must be an array for word {row.get('word_id')}")
        if not set(row["sentence_ids"]) <= sentence_ids:
            fail(f"Leipzig: index references unknown sentence for word {row.get('word_id')}")
    for filename in (
        "leipzig/leipzig_neighbour_cooccurrences__JSON.json",
        "leipzig/leipzig_sentence_cooccurrences__JSON.json",
    ):
        _, relations = envelope(ROOT / filename)
        if not isinstance(relations, list):
            fail(f"{filename}: value must be an array")
        for row in relations:
            if row.get("word1_id") not in word_ids or row.get("word2_id") not in word_ids:
                fail(f"{filename}: relation references unknown word")


def main() -> None:
    try:
        files = sorted(
            path
            for path in ROOT.rglob("*__JSON.json")
            if path != MANIFEST_PATH
        )
        if not files:
            fail("no canonical JSON files found")
        assert_readmes(files)
        assert_manifest(files)
        assert_kbbi_v5()
        assert_wordnet()
        assert_leipzig()
    except ValidationError as error:
        print(f"ERROR: {error}")
        raise SystemExit(1)
    print(f"OK: validated {len(files)} canonical JSON files")


if __name__ == "__main__":
    main()
