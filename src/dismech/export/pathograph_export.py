"""
Pathograph data exporter for dismech.

Emits a Mondo-keyed pathograph artifact for runtime embedding on external sites
(e.g. Monarch disease/gene pages), without requiring KG ingest.

Writes, into an output directory:

  - ``MONDO_<id>.json`` — one per disorder that has a Mondo id and a non-empty
    causal graph; the ``{nodes, edges, orphan_targets}`` produced by
    ``graph_to_json``.
  - ``index.json`` — disease lookup, ``{"MONDO:0018923": [{file, name, slug}], …}``.
    List-valued so a Mondo id mapping to more than one disorder file isn't
    silently dropped.
  - ``by_gene.json`` — gene reverse index, ``{"hgnc:2228": ["MONDO:0018923", …], …}``,
    built from every node's ``meta.gene_terms`` (including genetic_context).

The per-disorder JSON is produced by the same ``build_causal_graph`` +
``graph_to_json`` the HTML renderer uses, so the emitted data can never drift
from the rendered site.
"""

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterator

import yaml

from dismech.graph import build_causal_graph, graph_to_json


def slugify(name: str) -> str:
    """Convert a disorder name to a filename-safe slug (matches browser_export)."""
    return name.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")


def _disorder_term_id(disorder: dict[str, Any]) -> str | None:
    """Return the disorder's Mondo CURIE (uppercased), or None."""
    term = (disorder.get("disease_term") or {}).get("term") or {}
    term_id = term.get("id")
    if not term_id:
        return None
    return str(term_id).upper()


_EVIDENCE_KEYS = ("reference", "reference_title", "snippet", "supports")


def _trim_evidence(ev_list: list) -> list[dict[str, str]]:
    """Keep the displayable evidence fields (reference + title + snippet)."""
    out: list[dict[str, str]] = []
    for ev in ev_list:
        if isinstance(ev, dict) and ev.get("reference"):
            out.append({k: ev[k] for k in _EVIDENCE_KEYS if ev.get(k)})
    return out


def _evidence_by_name(
    value: Any, acc: dict[str, list[dict[str, str]]]
) -> dict[str, list[dict[str, str]]]:
    """Map every named item's ``name`` → its trimmed evidence list.

    Walks the disorder recursively so items in any section (and nested
    variants) are captured. Node ids in the graph JSON are item names, so this
    lets the exporter re-attach the references that ``graph_to_json`` reduces
    to a bare ``evidence_count``.
    """
    if isinstance(value, dict):
        name = value.get("name")
        ev = value.get("evidence")
        if isinstance(name, str) and isinstance(ev, list) and name not in acc:
            trimmed = _trim_evidence(ev)
            if trimmed:
                acc[name] = trimmed
        for nested in value.values():
            _evidence_by_name(nested, acc)
    elif isinstance(value, list):
        for item in value:
            _evidence_by_name(item, acc)
    return acc


def _iter_gene_ids(value: Any) -> Iterator[str]:
    """Yield every gene CURIE found under any ``gene_terms`` list in a node.

    Walks recursively so both ``meta.gene_terms`` and nested
    ``genetic_context`` gene terms are captured.
    """
    if isinstance(value, dict):
        for key, nested in value.items():
            if key == "gene_terms" and isinstance(nested, list):
                for entry in nested:
                    if isinstance(entry, dict) and entry.get("id"):
                        yield str(entry["id"])
            else:
                yield from _iter_gene_ids(nested)
    elif isinstance(value, list):
        for item in value:
            yield from _iter_gene_ids(item)


class PathographExporter:
    """Export per-disorder pathograph JSON plus Mondo and gene indexes."""

    def load_disorder(self, file_path: Path) -> dict[str, Any]:
        with open(file_path) as f:
            return yaml.safe_load(f)

    def export(self, disorder_files: list[Path], output_dir: Path) -> dict[str, int]:
        output_dir.mkdir(parents=True, exist_ok=True)

        index: dict[str, list[dict[str, str]]] = defaultdict(list)
        by_gene: dict[str, set[str]] = defaultdict(set)
        used_files: set[str] = set()
        written = 0
        skipped_no_mondo = 0
        skipped_no_graph = 0

        for file_path in disorder_files:
            disorder = self.load_disorder(file_path) or {}
            mondo_id = _disorder_term_id(disorder)
            if not mondo_id:
                skipped_no_mondo += 1
                continue

            data_str = graph_to_json(build_causal_graph(disorder), disorder)
            if not data_str:
                # No edges → no pathograph to show.
                skipped_no_graph += 1
                continue
            data = json.loads(data_str)

            # Re-attach the actual evidence references that graph_to_json
            # reduces to meta.evidence_count, so consumers can show the papers.
            evidence_by_name = _evidence_by_name(disorder, {})
            for node in data.get("nodes", []):
                node_evidence = evidence_by_name.get(node.get("id"))
                if node_evidence:
                    node.setdefault("meta", {})["evidence"] = node_evidence

            name = disorder.get("name") or file_path.stem
            # Normally MONDO_<id>.json. When several distinct disorders map to
            # the same Mondo id, disambiguate by slug so neither is clobbered;
            # index.json lists every file for the id.
            base = mondo_id.replace(":", "_")
            filename = f"{base}.json"
            if filename in used_files:
                filename = f"{base}__{slugify(str(name))}.json"
            used_files.add(filename)
            with open(output_dir / filename, "w") as f:
                json.dump(data, f, indent=2, sort_keys=True)
            written += 1

            index[mondo_id].append(
                {"file": filename, "name": str(name), "slug": slugify(str(name))}
            )
            for node in data.get("nodes", []):
                for gene_id in _iter_gene_ids(node):
                    by_gene[gene_id].add(mondo_id)

        with open(output_dir / "index.json", "w") as f:
            json.dump(
                {k: v for k, v in sorted(index.items())}, f, indent=2, sort_keys=True
            )
        with open(output_dir / "by_gene.json", "w") as f:
            json.dump(
                {gene: sorted(mondos) for gene, mondos in sorted(by_gene.items())},
                f,
                indent=2,
                sort_keys=True,
            )

        return {
            "pathographs": written,
            "diseases_indexed": len(index),
            "genes_indexed": len(by_gene),
            "skipped_no_mondo": skipped_no_mondo,
            "skipped_no_graph": skipped_no_graph,
        }


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Export Mondo-keyed pathograph JSON")
    parser.add_argument(
        "--input-dir",
        "-i",
        default="kb/disorders",
        help="Input directory with YAML files",
    )
    parser.add_argument(
        "--output-dir", "-o", default="pathographs", help="Output directory for JSON"
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    disorder_files = [
        path
        for path in sorted(input_dir.glob("*.yaml"))
        if not path.name.endswith(".history.yaml")
    ]

    stats = PathographExporter().export(disorder_files, Path(args.output_dir))
    print(
        f"Wrote {stats['pathographs']} pathographs "
        f"({stats['diseases_indexed']} diseases, {stats['genes_indexed']} genes) "
        f"to {args.output_dir}/ — skipped {stats['skipped_no_mondo']} (no Mondo), "
        f"{stats['skipped_no_graph']} (no edges)"
    )


if __name__ == "__main__":
    main()
