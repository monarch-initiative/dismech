"""Add reviewed ICD mapping hypotheses to existing Mendelian Boomer inputs.

Preserve all existing facts and probabilities. Keep old solutions byte-for-byte,
mark their index rows STALE_INPUT, and retain before/after hashes in updates.json.
This is an additive migration; a source refresh that removes or changes mappings
requires full input regeneration, not another additive migration.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
from pathlib import Path

import yaml

from build_analyses import External, INDEX_FIELDNAMES, REPO
from dismech import kb_cache
from icd10_enrichment import CONFIG, FIELDS, ICD10Mappings


def digest(content):
    return hashlib.sha256(content).hexdigest()


def tsv(rows, fields, newline="\n"):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream, fieldnames=fields, delimiter="\t", lineterminator=newline
    )
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode()


def migrate(base, disease_dir, importer, validate, sources=None):
    """Preflight and validate every change before writing any input or report."""
    index_path = base / "index.tsv"
    with index_path.open() as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if reader.fieldnames != list(INDEX_FIELDNAMES):
            raise ValueError("Unexpected Boomer index columns")
        index = list(reader)
    if len({r["slug"] for r in index}) != len(index):
        raise ValueError("Duplicate Boomer index slugs")
    out = base / "icd10"
    manifest_path = out / "updates.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    sources_path = out / "import-sources.json"
    if (
        sources is not None
        and sources_path.exists()
        and json.loads(sources_path.read_text()) != sources
    ):
        raise ValueError(
            "ICD sources changed since migration; regenerate inputs instead of appending"
        )
    decisions, writes = [], {}
    changed = stale = 0
    for row in index:
        slug = row["slug"]
        disease = kb_cache.load_document(disease_dir / f"{slug}.yaml")
        if disease.get("category") != "Mendelian":
            continue
        folder = base / "disorders" / slug
        path = folder / "kb.yaml"
        before = path.read_bytes()
        kb = yaml.safe_load(before)
        original = json.dumps(kb, sort_keys=True)
        if slug in manifest and digest(before) != manifest[slug]["after_input_sha256"]:
            raise ValueError(
                f"{slug}: input changed since ICD migration; reconcile updates.json first"
            )
        decisions.extend(
            importer.enrich(
                kb, slug, (disease.get("mappings") or {}).get("icd10cm_mappings") or []
            )
        )
        validate(kb)
        if json.dumps(kb, sort_keys=True) == original:
            continue
        if slug in manifest:
            raise ValueError(
                f"{slug}: ICD assertions changed; use full regeneration instead of additive migration"
            )
        after = yaml.safe_dump(kb, sort_keys=False).encode()
        solved = row["status"] != "NOT_RUN"
        previous = dict(row)
        solution_hashes = {}
        if solved:
            for name in ("solution.yaml", "solution.md"):
                solution_hashes[name] = digest((folder / name).read_bytes())
            readme = folder / "README.md"
            banner = (
                "> **STALE INPUT:** ICD mapping hypotheses were added after the saved solve.\n"
                "> The report and solution files below describe the previous input only.\n"
                "> No result is asserted for the current `kb.yaml`; rerun the solver.\n"
                "> [Input hashes and previous index values](../../icd10/updates.json)\n\n"
            )
            writes[readme] = banner.encode() + readme.read_bytes()
            row["status"] = "STALE_INPUT"
            stale += 1
        elif any((folder / name).exists() for name in ("solution.yaml", "solution.md")):
            raise ValueError(f"{slug}: NOT_RUN input unexpectedly has solution files")
        row["n_pfacts"] = str(len(kb["pfacts"]))
        row["n_retracted"] = "NA"
        manifest[slug] = {
            "before_input_sha256": digest(before),
            "after_input_sha256": digest(after),
            "previous_index": previous,
            "preserved_solution_sha256": solution_hashes,
        }
        writes[path] = after
        changed += 1
    out.mkdir(parents=True, exist_ok=True)
    writes[out / "import-decisions.tsv"] = tsv(decisions, FIELDS)
    writes[manifest_path] = (
        json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    ).encode()
    if sources is not None:
        writes[sources_path] = (
            json.dumps(sources, indent=2, sort_keys=True) + "\n"
        ).encode()
    # Preserve the existing index's line endings, so unaffected rows stay identical.
    ending = "\r\n" if b"\r\n" in index_path.read_bytes() else "\n"
    writes[index_path] = tsv(index, INDEX_FIELDNAMES, ending)
    for path, content in writes.items():
        if not path.exists() or path.read_bytes() != content:
            path.write_bytes(content)
    print(f"Enriched {changed} inputs; {stale} saved results marked STALE_INPUT")
    return decisions


def main():
    kb_cache.default_off()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, default=REPO / "analyses/boomer")
    parser.add_argument("--kb-dir", type=Path, default=REPO / "kb/disorders")
    parser.add_argument("--oak-dir", type=Path, default=Path.home() / ".data/oaklib")
    parser.add_argument("--config", type=Path, default=CONFIG)
    parser.add_argument(
        "--boomer-src", type=Path, default=Path.home() / "repos/boomer-py/src"
    )
    args = parser.parse_args()
    sys.path.insert(0, str(args.boomer_src.expanduser()))
    from boomer.model import KB

    external = External(args.oak_dir)
    importer = ICD10Mappings(external, args.oak_dir, args.config)
    migrate(args.base, args.kb_dir, importer, KB.model_validate, importer.provenance())


if __name__ == "__main__":
    main()
