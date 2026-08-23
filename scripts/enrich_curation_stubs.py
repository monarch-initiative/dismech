#!/usr/bin/env python3
"""Add MONDO context to curation stubs: parents, descendants, and causal genes.

The stub queue deliberately carries no score and no computed verdict — deciding
whether a concept is a disease, a grouping, or a subtype is a curator's job
(issue #8969). But that decision needs facts, and the facts live in MONDO. This
script copies them into the stub so they are visible in the file and in a pull
request diff, rather than requiring an ontology query mid-task.

What it adds, and why each one is the fact a curator actually asks for:

- ``mondo_parents`` — is this a subtype of something we have already curated?
  That question comes up constantly (`Wilms tumor 1` under a curated
  `Wilms_Tumor`), and the parent term is the direct answer.
- ``mondo_descendants`` (+ ``mondo_descendant_count``) — a long list is the
  strongest cheap signal that a term is a grouping. Reported, never scored: the
  old dashboard scored child count and got the sign backwards.
- ``genes`` — which gene MONDO holds responsible, as lowercase ``hgnc:`` per
  repository convention. Distinguishes sibling numbered subtypes from each other.

Idempotent, and it only ever adds these three blocks — everything a person wrote
in the stub is preserved.

    uv run python scripts/enrich_curation_stubs.py            # all stubs
    uv run python scripts/enrich_curation_stubs.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.stubs.seed import yaml_scalar
from dismech.yaml_io import safe_load

DEFAULT_MONDO_DB = Path.home() / ".data" / "oaklib" / "mondo.db"
HGNC_CACHE = ROOT / "cache" / "hgnc" / "terms.csv"
#: Records which MONDO release the committed enrichment came from, so diff churn
#: in `mondo_descendant_count` across machines is attributable. Mirrors
#: `data/orphadata/MANIFEST.yaml` and `data/icees-kg/MANIFEST.yaml`.
MANIFEST = ROOT / "data" / "mondo" / "MANIFEST.yaml"

SUBCLASS_OF = "rdfs:subClassOf"
#: MONDO's "disease has basis in dysfunction of" / causal-gene relation.
CAUSAL_GENE = "RO:0004003"

#: Descendant lists are capped so a grouping term like `rickets` (868
#: descendants) does not bury the rest of the stub. The true total is kept in
#: `mondo_descendant_count`, so truncation is never silent. 25 of the 1,867
#: stubs are actually truncated at this cap.
DESCENDANT_CAP = 25


def mondo_version(conn: sqlite3.Connection) -> str | None:
    """MONDO release date from the ontology's own versionIRI.

    `obo:mondo/releases/2026-05-05/mondo.owl` -> `2026-05-05`.
    """
    row = conn.execute(
        "select object from statements where subject=? and predicate=?",
        ("obo:mondo.owl", "owl:versionIRI"),
    ).fetchone()
    if not row or not row[0]:
        return None
    match = re.search(r"/releases/([0-9]{4}-[0-9]{2}-[0-9]{2})/", str(row[0]))
    return match.group(1) if match else str(row[0])


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_manifest(version: str | None, stubs_processed: int, mondo_db: Path) -> None:
    """Pin the MONDO release the committed enrichment came from.

    A release date alone does not catch a locally rebuilt `mondo.db` drifting at
    the same release, so the database's sha256 is recorded too — the same thing
    `data/orphadata/MANIFEST.yaml` pins for its bulk XML. OAK serves a prebuilt
    `mondo.db.gz`, so the digest is reproducible for anyone who downloaded the
    same artifact.
    """
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(
        "# Which MONDO release the committed stub enrichment was generated from.\n"
        "# Written by scripts/enrich_curation_stubs.py; do not hand-edit.\n"
        "source: mondo\n"
        f"version: {version or 'unknown'}\n"
        f"sha256: {file_sha256(mondo_db)}\n"
        "# Stubs the enrichment pass read, not the number that received a block:\n"
        "# a MONDO leaf with no causal gene is processed and gets nothing.\n"
        f"stubs_processed: {stubs_processed}\n",
        encoding="utf-8",
    )


def load_labels(conn: sqlite3.Connection) -> dict[str, str]:
    return {
        subject: value
        for subject, value in conn.execute(
            "select subject, value from rdfs_label_statement where value is not null"
        )
    }


def load_hgnc_labels() -> dict[str, str]:
    """Gene symbols from the committed term cache — offline and repo-canonical."""
    labels: dict[str, str] = {}
    if not HGNC_CACHE.exists():
        return labels
    with HGNC_CACHE.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            curie, label = row.get("curie"), row.get("label")
            if curie and label:
                labels[curie.lower()] = label
    return labels


def term_block(curie: str, label: str | None, indent: str = "") -> list[str]:
    lines = [f"{indent}- id: {curie}"]
    if label:
        lines.append(f"{indent}  label: {yaml_scalar(label)}")
    return lines


def render(parents, descendants, total, genes) -> list[str]:
    lines: list[str] = []
    if parents:
        lines.append("mondo_parents:")
        for curie, label in parents:
            lines += term_block(curie, label)
    if descendants:
        lines.append("mondo_descendants:")
        for curie, label in descendants:
            lines += term_block(curie, label)
        lines.append(f"mondo_descendant_count: {total}")
    if genes:
        lines.append("genes:")
        for curie, label in genes:
            lines += term_block(curie, label)
    return lines


def strip_existing(text: str) -> str:
    """Remove blocks this script owns, so a re-run replaces rather than appends."""
    owned = (
        "mondo_parents:",
        "mondo_descendants:",
        "mondo_descendant_count:",
        "genes:",
    )
    out, skipping = [], False
    for line in text.splitlines():
        if line.startswith(owned):
            skipping = True
            continue
        if skipping and (line.startswith(("  ", "- ")) or not line.strip()):
            continue
        skipping = False
        out.append(line)
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stub-dir", type=Path, default=ROOT / "stubs")
    parser.add_argument("--mondo-db", type=Path, default=DEFAULT_MONDO_DB)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.mondo_db.exists():
        parser.error(
            f"MONDO database not found at {args.mondo_db}. "
            "Fetch it with `just fetch-ontology-dbs mondo`."
        )

    paths = sorted(args.stub_dir.glob("*.yaml"))
    stub_ids = {}
    for path in paths:
        data = safe_load(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and data.get("mondo_id"):
            stub_ids[path] = str(data["mondo_id"])

    conn = sqlite3.connect(f"file:{args.mondo_db}?mode=ro", uri=True)
    labels = load_labels(conn)
    gene_labels = load_hgnc_labels()
    ids = sorted(set(stub_ids.values()))
    placeholders = ",".join("?" * len(ids))

    parents: dict[str, list[str]] = {}
    for subject, obj in conn.execute(
        f"select subject, object from edge where predicate=? and subject in ({placeholders})",
        [SUBCLASS_OF, *ids],
    ):
        if str(obj).startswith("MONDO:"):
            parents.setdefault(subject, []).append(obj)

    descendants: dict[str, list[str]] = {}
    for subject, obj in conn.execute(
        f"select subject, object from entailed_edge "
        f"where predicate=? and object in ({placeholders})",
        [SUBCLASS_OF, *ids],
    ):
        if subject != obj and str(subject).startswith("MONDO:"):
            descendants.setdefault(obj, []).append(subject)

    genes: dict[str, list[str]] = {}
    for subject, obj in conn.execute(
        f"select subject, object from edge where predicate=? and subject in ({placeholders})",
        [CAUSAL_GENE, *ids],
    ):
        genes.setdefault(subject, []).append(str(obj))

    changed = 0
    for path, mondo_id in stub_ids.items():
        kids = sorted(descendants.get(mondo_id, []))
        block = render(
            [(p, labels.get(p)) for p in sorted(parents.get(mondo_id, []))],
            [(k, labels.get(k)) for k in kids[:DESCENDANT_CAP]],
            len(kids),
            [
                (g.lower(), gene_labels.get(g.lower()) or labels.get(g))
                for g in sorted(genes.get(mondo_id, []))
            ],
        )
        original = path.read_text(encoding="utf-8")
        # Strip unconditionally, including when `block` is empty. Short-circuiting
        # on an empty block would leave a stale block in place forever if a MONDO
        # term later lost every parent, descendant, and gene -- the one case where
        # a refresh most needs to remove something.
        base = strip_existing(original)
        updated = base + ("\n".join(block) + "\n" if block else "")
        if updated != original:
            changed += 1
            if not args.dry_run:
                path.write_text(updated, encoding="utf-8")

    version = mondo_version(conn)
    # Only pin when enriching the committed queue. Running against a subset
    # (`--stub-dir /tmp/...`) must not rewrite the repository's manifest with a
    # count for a directory that is not `stubs/`.
    is_canonical_run = args.stub_dir.resolve() == (ROOT / "stubs").resolve()
    if not args.dry_run and is_canonical_run:
        write_manifest(version, len(stub_ids), args.mondo_db)

    print(
        f"mondo: {version or 'unknown'}  "
        f"stubs: {len(stub_ids)}  with parents: {len(parents)}  "
        f"with descendants: {len(descendants)}  with genes: {len(genes)}  "
        f"{'would change' if args.dry_run else 'changed'}: {changed}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
