"""
Build the bulk files attached to each GitHub release, beyond the KGX export.

``.github/workflows/release-assets.yaml`` runs these subcommands on every
published release; ``kgx-release.yaml`` uses ``kgx-tsv`` and
``kgx-metadata``. Each archive is built from the checked-out tag, so a
release's files describe exactly the content of that tag.

Subcommands
-----------
kb-zip        ``kb.zip``: every ``kb/**/*.yaml`` entry, the curated gene
              summaries (``kb/genes/curated/*.md``) and the pathograph
              node-class vocabulary. Left out: ``kb/genes/ingest/`` (copies of
              HGNC, ClinGen and ai-gene-review data, published by those
              sources) and the non-YAML provider artifacts under
              ``kb/hypotheses/`` (reports, PDFs, figures).
pathographs   ``pathographs.zip``: the per-disease pathograph JSON the site
              renders, as written by ``dismech.export.pathograph_export``.
cx2           ``pathographs_cx2.zip``: one NDEx CX2 network per disorder with
              at least one pathograph edge. Runs in one process, unlike
              ``just export-cx2-all``, which starts a process per file.
omex          ``dismech_models_omex.zip``: one COMBINE ``.omex`` archive per
              runnable model, from ``dismech.perturb.sedml_export``.
kgx-tsv       KGX TSV copies of a JSON Lines node/edge pair, with every
              property kept. koza's own TSV writer is not used: it keeps only
              six edge columns and does not deduplicate nodes. List values
              are joined with ``|``, as KGX TSV expects; a ``|`` inside a
              value (quoted Orphanet and ClinGen table rows) is written as
              ``¦`` so it does not split the value, and tabs and newlines
              become spaces. The JSON Lines files stay the authoritative form.
kgx-metadata  A JSON summary of a KGX node/edge pair: counts by category and
              predicate, and with ``--biolink`` the installed Biolink Model
              version the export was built against.
manifest      ``release_manifest.json``: entry counts per ``kb/`` section
              (hypotheses counted as assessed hypothesis directories, not
              files), and the name, size and sha256 of every file in a
              directory.

Zip members carry a fixed timestamp, so rebuilding an unchanged tag gives
byte-identical archives.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import tempfile
import zipfile
from collections import Counter
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from dismech import kb_cache

# 1980-01-01, the earliest timestamp a zip entry can hold.
ZIP_EPOCH = (1980, 1, 1, 0, 0, 0)

# kb/ sections counted in the manifest: section -> glob relative to it.
KB_SECTIONS = {
    "disorders": "*.yaml",
    "modules": "*.yaml",
    "module_collections": "*.yaml",
    "groupings": "*.yaml",
    "comorbidities": "*.yaml",
    "gene_classifications": "*.yaml",
    "surrogate_endpoints": "*.yaml",
    "genes/curated": "*.md",
}

# Non-YAML kb/ files that are curated content and belong in kb.zip.
KB_EXTRA_GLOBS = ("genes/curated/*.md", "node_classes/*")


def write_zip(zip_path: Path, members: Iterable[tuple[Path, str]]) -> int:
    """Write ``(source file, archive name)`` pairs to a deterministic zip.

    Members are sorted by archive name and stamped with ``ZIP_EPOCH``. Returns
    the number of members written.
    """
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for source, name in sorted(members, key=lambda pair: pair[1]):
            info = zipfile.ZipInfo(name, date_time=ZIP_EPOCH)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, source.read_bytes())
            count += 1
    return count


def zip_directory(directory: Path, zip_path: Path, prefix: str) -> int:
    """Zip every file under ``directory`` with names rooted at ``prefix/``."""
    members = [
        (path, f"{prefix}/{path.relative_to(directory).as_posix()}")
        for path in directory.rglob("*")
        if path.is_file()
    ]
    return write_zip(zip_path, members)


def kb_files(kb_dir: Path) -> list[Path]:
    """The files that make up ``kb.zip``."""
    files = {path for path in kb_dir.rglob("*.yaml") if path.is_file()}
    for pattern in KB_EXTRA_GLOBS:
        files.update(path for path in kb_dir.glob(pattern) if path.is_file())
    return sorted(files)


def build_kb_zip(kb_dir: Path, zip_path: Path) -> int:
    members = [
        (path, f"kb/{path.relative_to(kb_dir).as_posix()}") for path in kb_files(kb_dir)
    ]
    return write_zip(zip_path, members)


def disorder_files(disorders_dir: Path) -> list[Path]:
    return [
        path
        for path in sorted(disorders_dir.glob("*.yaml"))
        if not path.name.endswith(".history.yaml")
    ]


def build_pathographs_zip(disorders_dir: Path, zip_path: Path) -> dict[str, int]:
    from dismech.export.pathograph_export import PathographExporter

    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp) / "pathographs"
        stats = PathographExporter().export(disorder_files(disorders_dir), out_dir)
        stats["files"] = zip_directory(out_dir, zip_path, "pathographs")
    return stats


def build_cx2_zip(
    disorders_dir: Path,
    zip_path: Path,
    *,
    release_version: str | None = None,
    source_revision: str | None = None,
) -> dict[str, int]:
    from dismech.export.cx2_export import dump_cx2

    stats = Counter()
    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp) / "pathographs_cx2"
        out_dir.mkdir()
        for path in disorder_files(disorders_dir):
            try:
                dump_cx2(
                    path,
                    output_path=out_dir / f"{path.stem}.cx2.json",
                    release_metadata={"version": release_version},
                    source_revision=source_revision,
                )
            except ValueError as error:
                # Same condition `dismech-cx2 --skip-empty` tolerates.
                if "does not contain any pathograph edges" not in str(error):
                    raise
                stats["skipped_no_edges"] += 1
                continue
            stats["networks"] += 1
        zip_directory(out_dir, zip_path, "pathographs_cx2")
    return dict(stats)


def build_omex_zip(zip_path: Path) -> dict[str, int]:
    from dismech.perturb.sedml_export import export_all

    with tempfile.TemporaryDirectory() as tmp:
        results = export_all(output_root=Path(tmp), write_archive=True)
        archives = [r.omex_path for r in results if r.omex_path is not None]
        write_zip(zip_path, [(path, path.name) for path in archives])
    return {
        "models": len(archives),
        "skipped": sum(1 for r in results if r.skipped_reason),
    }


def _iter_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                yield json.loads(line)


# KGX TSV column order: these first, then every other property, sorted.
KGX_LEADING_COLUMNS = {
    "nodes": ("id", "category", "name"),
    "edges": ("id", "subject", "predicate", "object", "category"),
}


def _tsv_cell(value: Any) -> str:
    items = value if isinstance(value, list) else [value]
    cleaned = []
    for item in items:
        text = item if isinstance(item, str) else json.dumps(item, ensure_ascii=False)
        cleaned.append(" ".join(text.replace("|", "¦").split()))
    return "|".join(cleaned)


def jsonl_to_kgx_tsv(jsonl_path: Path, tsv_path: Path, kind: str) -> int:
    """Write a KGX JSON Lines file as KGX TSV, keeping every property."""
    keys: set[str] = set()
    for record in _iter_jsonl(jsonl_path):
        keys.update(record)
    leading = [key for key in KGX_LEADING_COLUMNS[kind] if key in keys]
    columns = leading + sorted(keys - set(leading))
    rows = 0
    tsv_path.parent.mkdir(parents=True, exist_ok=True)
    # Written by hand rather than with the csv module: cells hold no tab or
    # newline after _tsv_cell, and KGX TSV readers do not expect CSV quoting.
    with tsv_path.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write("\t".join(columns) + "\n")
        for record in _iter_jsonl(jsonl_path):
            cells = [_tsv_cell(record[c]) if c in record else "" for c in columns]
            fh.write("\t".join(cells) + "\n")
            rows += 1
    return rows


def kgx_metadata(
    nodes_path: Path, edges_path: Path, *, biolink: bool, experimental: bool
) -> dict[str, Any]:
    """Count a KGX JSON Lines node/edge pair by category and predicate."""
    categories: Counter[str] = Counter()
    node_count = 0
    for node in _iter_jsonl(nodes_path):
        node_count += 1
        category = node.get("category") or ["(none)"]
        for value in category if isinstance(category, list) else [category]:
            categories[value] += 1
    predicates: Counter[str] = Counter()
    edge_count = 0
    for edge in _iter_jsonl(edges_path):
        edge_count += 1
        predicates[edge.get("predicate") or "(none)"] += 1

    metadata: dict[str, Any] = {
        "nodes_file": nodes_path.name,
        "edges_file": edges_path.name,
        "node_count": node_count,
        "edge_count": edge_count,
        "experimental": experimental,
    }
    if biolink:
        metadata["biolink_model_version"] = importlib.metadata.version("biolink-model")
    # A node with several categories is counted once under each.
    metadata["nodes_by_category"] = dict(sorted(categories.items()))
    metadata["edges_by_predicate"] = dict(sorted(predicates.items()))
    return metadata


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def kb_counts(kb_dir: Path) -> dict[str, int]:
    counts = {
        section: sum(1 for path in (kb_dir / section).glob(pattern) if path.is_file())
        for section, pattern in KB_SECTIONS.items()
    }
    # A hypothesis is a kb/hypotheses/<Disease>/<hypothesis_id>/ directory
    # holding several files, so count directories, and only assessed ones.
    hypotheses_dir = kb_dir / "hypotheses"
    counts["hypotheses_assessed"] = len(
        {
            path.relative_to(hypotheses_dir).parts[:2]
            for pattern in ("*assessment*.yaml", "reconciliation*.yaml")
            for path in hypotheses_dir.rglob(pattern)
        }
    )
    return counts


def build_manifest(
    kb_dir: Path,
    assets_dir: Path,
    *,
    tag: str | None = None,
    commit: str | None = None,
) -> dict[str, Any]:
    assets = [
        {"name": path.name, "size_bytes": path.stat().st_size, "sha256": sha256(path)}
        for path in sorted(assets_dir.iterdir())
        if path.is_file() and path.name != "release_manifest.json"
    ]
    return {
        "release_tag": tag,
        "source_commit": commit,
        "kb_entry_counts": kb_counts(kb_dir),
        "assets": assets,
    }


def _write_json(data: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def main(argv: list[str] | None = None) -> None:
    # Each subcommand walks the corpus at most once.
    kb_cache.default_off()
    parser = argparse.ArgumentParser(description="Build release assets.")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("kb-zip", help="Zip the curated kb/ content.")
    p.add_argument("--kb-dir", type=Path, default=Path("kb"))
    p.add_argument("-o", "--output", type=Path, default=Path("dist/kb.zip"))

    p = sub.add_parser("pathographs", help="Zip the pathograph JSON.")
    p.add_argument("--disorders-dir", type=Path, default=Path("kb/disorders"))
    p.add_argument("-o", "--output", type=Path, default=Path("dist/pathographs.zip"))

    p = sub.add_parser("cx2", help="Zip one CX2 network per disorder.")
    p.add_argument("--disorders-dir", type=Path, default=Path("kb/disorders"))
    p.add_argument(
        "-o", "--output", type=Path, default=Path("dist/pathographs_cx2.zip")
    )
    p.add_argument("--release-version", help="Version recorded on each network.")
    p.add_argument("--source-revision", help="Git commit recorded on each network.")

    p = sub.add_parser("omex", help="Zip the COMBINE archives of the runnable models.")
    p.add_argument(
        "-o", "--output", type=Path, default=Path("dist/dismech_models_omex.zip")
    )

    p = sub.add_parser("kgx-tsv", help="Write KGX TSV from KGX JSON Lines.")
    p.add_argument("--nodes", type=Path, required=True)
    p.add_argument("--edges", type=Path, required=True)
    p.add_argument("--nodes-out", type=Path, required=True)
    p.add_argument("--edges-out", type=Path, required=True)

    p = sub.add_parser("kgx-metadata", help="Summarize a KGX node/edge pair.")
    p.add_argument("--nodes", type=Path, required=True)
    p.add_argument("--edges", type=Path, required=True)
    p.add_argument("-o", "--output", type=Path, required=True)
    p.add_argument(
        "--biolink", action="store_true", help="Record the Biolink Model version."
    )
    p.add_argument("--experimental", action="store_true")

    p = sub.add_parser(
        "manifest", help="Write release_manifest.json for a directory of assets."
    )
    p.add_argument("--kb-dir", type=Path, default=Path("kb"))
    p.add_argument("--assets-dir", type=Path, default=Path("dist"))
    p.add_argument(
        "-o", "--output", type=Path, default=Path("dist/release_manifest.json")
    )
    p.add_argument("--tag")
    p.add_argument("--commit")

    args = parser.parse_args(argv)
    if args.command == "kb-zip":
        print(f"Wrote {build_kb_zip(args.kb_dir, args.output)} files to {args.output}")
    elif args.command == "pathographs":
        print(
            f"{build_pathographs_zip(args.disorders_dir, args.output)} -> {args.output}"
        )
    elif args.command == "cx2":
        stats = build_cx2_zip(
            args.disorders_dir,
            args.output,
            release_version=args.release_version,
            source_revision=args.source_revision,
        )
        print(f"{stats} -> {args.output}")
    elif args.command == "omex":
        print(f"{build_omex_zip(args.output)} -> {args.output}")
    elif args.command == "kgx-tsv":
        for kind, src, dst in (
            ("nodes", args.nodes, args.nodes_out),
            ("edges", args.edges, args.edges_out),
        ):
            print(f"{jsonl_to_kgx_tsv(src, dst, kind)} {kind} -> {dst}")
    elif args.command == "kgx-metadata":
        metadata = kgx_metadata(
            args.nodes, args.edges, biolink=args.biolink, experimental=args.experimental
        )
        _write_json(metadata, args.output)
        print(
            f"{metadata['node_count']} nodes, {metadata['edge_count']} edges -> {args.output}"
        )
    elif args.command == "manifest":
        manifest = build_manifest(
            args.kb_dir, args.assets_dir, tag=args.tag, commit=args.commit
        )
        _write_json(manifest, args.output)
        print(f"{len(manifest['assets'])} assets -> {args.output}")


if __name__ == "__main__":
    main()
