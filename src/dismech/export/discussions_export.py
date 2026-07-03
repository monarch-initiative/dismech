"""
Discussions browser data exporter for dismech.

Flattens the ``discussions`` blocks of disorder and module YAML files into one
searchable record per discussion, for the faceted discussions browser
(``app/discussions/``). All discussion kinds are exported — open questions,
controversies, curation TODOs, emerging hypotheses, interpretations, and the
two knowledge-gap kinds (``KNOWLEDGE_GAP`` and ``HUMAN_MODEL_MISMATCH``) — and
the ``kind`` facet lets users narrow to a particular kind.

Each record links back to the disorder/module page that owns the discussion,
anchored on the discussion's ``discussion_id``.
"""

import json
from pathlib import Path
from typing import Any

import yaml

# Discussion kinds that count as "knowledge gaps" (used for the Gap? facet).
GAP_KINDS = {"KNOWLEDGE_GAP", "HUMAN_MODEL_MISMATCH"}


def slugify(name: str) -> str:
    """Convert a disorder name to a filename-safe slug (matches render.slugify)."""
    return name.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")


def _node_label(ref: str) -> str:
    """Extract the human-readable node name from an attaches_to reference.

    References use the grammar ``[<file>:]<kind>#<name>`` (e.g.
    ``pathophysiology#Amyloid Plaque Formation``). The portion after ``#`` is
    the node name; everything before it is the entity kind / file scope.
    """
    if "#" in ref:
        return ref.split("#", 1)[1].strip()
    return ref.strip()


def _collect_reference_ids(evidence: Any) -> list[str]:
    refs: list[str] = []
    for item in evidence or []:
        if isinstance(item, dict):
            ref = item.get("reference")
            if isinstance(ref, str) and ref.strip():
                refs.append(ref.strip())
    return refs


class DiscussionsExporter:
    """Export discussion threads to browser-friendly JSON/JS records."""

    def load_entry(self, file_path: Path) -> dict[str, Any]:
        with open(file_path) as f:
            return yaml.safe_load(f) or {}

    def extract_discussions(
        self,
        entry: dict[str, Any],
        *,
        source_type: str,
        source_file: str,
        page_url: str,
    ) -> list[dict[str, Any]]:
        """Extract one record per discussion in ``entry``."""
        records: list[dict[str, Any]] = []
        source_name = entry.get("name", "Unknown")
        creation_date = entry.get("creation_date")

        # Disease class facet only meaningful for disorder entries.
        parents = entry.get("parents", []) if source_type == "Disorder" else []
        category = entry.get("category", "") if source_type == "Disorder" else ""

        disease_id = None
        disease_term = entry.get("disease_term") or {}
        if isinstance(disease_term, dict) and disease_term.get("term"):
            disease_id = disease_term["term"].get("id")

        for idx, discussion in enumerate(entry.get("discussions") or []):
            if not isinstance(discussion, dict):
                continue
            kind = discussion.get("kind")

            discussion_id = (
                discussion.get("discussion_id")
                or f"{slugify(source_name)}-discussion-{idx}"
            )
            attaches_to = [
                str(ref) for ref in (discussion.get("attaches_to") or []) if ref
            ]
            attached_nodes = sorted({_node_label(ref) for ref in attaches_to})
            experiments = discussion.get("proposed_experiments") or []
            experiment_names = [
                e.get("name", "")
                for e in experiments
                if isinstance(e, dict) and e.get("name")
            ]
            evidence_refs = _collect_reference_ids(discussion.get("evidence"))

            records.append(
                {
                    "discussion_id": discussion_id,
                    # ``name`` drives MiniSearch boosting and the card title.
                    "name": discussion.get("prompt", source_name),
                    "prompt": discussion.get("prompt", ""),
                    "kind": (kind or "").replace("_", " "),
                    "is_gap": "Knowledge gap" if kind in GAP_KINDS else "Other discussion",
                    "status": (discussion.get("status") or "").replace("_", " "),
                    "source_type": source_type,
                    "source_name": source_name,
                    "disease_id": disease_id,
                    "category": category,
                    "parents": parents,
                    "attaches_to": attaches_to,
                    "attached_nodes": attached_nodes,
                    "rationale": discussion.get("rationale", ""),
                    "experiment_names": experiment_names,
                    "num_experiments": len(experiments),
                    "num_evidence": len(evidence_refs),
                    "evidence_refs": evidence_refs,
                    "has_experiments": (
                        "With proposed experiments"
                        if experiments
                        else "No proposed experiments"
                    ),
                    "posed_by": discussion.get("posed_by", ""),
                    "creation_date": creation_date,
                    "page_url": f"{page_url}#{discussion_id}",
                    "source_file": source_file,
                }
            )
        return records

    def collect_records(
        self,
        disorders_dir: Path = Path("kb/disorders"),
        modules_dir: Path = Path("kb/modules"),
    ) -> list[dict[str, Any]]:
        records: list[dict[str, Any]] = []

        if disorders_dir.exists():
            for file_path in sorted(disorders_dir.glob("*.yaml")):
                if file_path.name.endswith(".history.yaml"):
                    continue
                entry = self.load_entry(file_path)
                slug = slugify(entry.get("name", file_path.stem))
                records.extend(
                    self.extract_discussions(
                        entry,
                        source_type="Disorder",
                        source_file=f"kb/disorders/{file_path.name}",
                        page_url=f"../../pages/disorders/{slug}.html",
                    )
                )

        if modules_dir.exists():
            for file_path in sorted(modules_dir.glob("*.yaml")):
                if file_path.name.endswith(".history.yaml"):
                    continue
                entry = self.load_entry(file_path)
                records.extend(
                    self.extract_discussions(
                        entry,
                        source_type="Module",
                        source_file=f"kb/modules/{file_path.name}",
                        page_url=f"../../pages/modules/{file_path.stem}.html",
                    )
                )

        # Stable ordering: by source name, then prompt.
        records.sort(
            key=lambda r: (str(r.get("source_name") or "").casefold(), str(r.get("name") or "").casefold())
        )
        return records

    @staticmethod
    def build_summary_metrics(records: list[dict[str, Any]]) -> dict[str, int]:
        sources = {r["source_name"] for r in records}
        with_experiments = sum(1 for r in records if r["num_experiments"] > 0)
        kinds = {r["kind"] for r in records}
        gaps = sum(1 for r in records if r["is_gap"] == "Knowledge gap")
        return {
            "total_discussions": len(records),
            "total_knowledge_gaps": gaps,
            "total_source_entries": len(sources),
            "total_with_experiments": with_experiments,
            "total_discussion_kinds": len(kinds),
        }

    def export_to_js(
        self,
        output_path: Path,
        disorders_dir: Path = Path("kb/disorders"),
        modules_dir: Path = Path("kb/modules"),
    ) -> None:
        records = self.collect_records(disorders_dir, modules_dir)
        metrics = self.build_summary_metrics(records)

        js_content = f"window.searchData = {json.dumps(records, indent=2)};\n"
        js_content += f"window.searchMetrics = {json.dumps(metrics, indent=2)};\n"
        js_content += "window.dispatchEvent(new Event('searchDataReady'));\n"

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(js_content)

        print(f"Exported {len(records)} discussions to {output_path}")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Export discussion data for browser")
    parser.add_argument("--disorders-dir", default="kb/disorders", help="Disorder YAML directory")
    parser.add_argument("--modules-dir", default="kb/modules", help="Module YAML directory")
    parser.add_argument("--output", "-o", default="app/discussions/data.js", help="Output file path")

    args = parser.parse_args()

    DiscussionsExporter().export_to_js(
        Path(args.output),
        disorders_dir=Path(args.disorders_dir),
        modules_dir=Path(args.modules_dir),
    )


if __name__ == "__main__":
    main()
