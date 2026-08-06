"""
Computational-models browser data exporter for dismech.

Flattens the ``computational_models`` blocks of disorder and module YAML files
into one searchable record per model, for the faceted models browser
(``app/models/``). Every ``ComputationalModelTypeEnum`` kind is exported —
genome-scale metabolic reconstructions, FBA models, ODE/kinetic models, Boolean
networks, agent-based simulations, PBPK/physiological models, digital twins, and
ML/foundation models — and the ``model_type`` facet lets users narrow to one.

Each record links back to the disorder/module page that owns the model, anchored
on the same ``computational-model-<slug>`` anchor that ``render.py`` emits, and
records whether the model is *runnable in-repo* (a ``models/<model_id>.config.yaml``
perturbation config exists) or a literature reference only.
"""

import json
import re
from pathlib import Path
from typing import Any

from dismech.export.utils import slugify
from dismech.yaml_io import safe_load

#: Repository hosts we recognise, so "where does this model live?" is a facet
#: rather than something a reader has to infer from a raw URL.
REPOSITORY_HOSTS: list[tuple[str, str]] = [
    ("ebi.ac.uk/biomodels", "BioModels"),
    ("biomodels.net", "BioModels"),
    ("vmh.life", "Virtual Metabolic Human"),
    ("bigg.ucsd.edu", "BiGG"),
    ("github.com", "GitHub"),
    ("gitlab.com", "GitLab"),
    ("zenodo.org", "Zenodo"),
    ("physiomeproject.org", "Physiome / CellML"),
    ("models.cellml.org", "Physiome / CellML"),
    ("cziscience.com", "CZI Virtual Cells"),
    ("synapse.org", "Synapse"),
]


def make_anchor_id(value: str) -> str:
    """Rebuild the in-page anchor ``render._make_anchor_id`` emits for a model."""
    slug = re.sub(r"[^a-z0-9]+", "-", str(value).casefold()).strip("-")
    return f"computational-model-{slug or 'item'}"


def humanize_enum(value: Any) -> str:
    """Render an enum permissible value as facet-friendly text."""
    if not isinstance(value, str) or not value.strip():
        return ""
    return value.strip().replace("_", " ").title()


def repository_host(url: Any) -> str:
    """Classify a repository URL into a coarse, facetable host name."""
    if not isinstance(url, str) or not url.strip():
        return "No repository link"
    lowered = url.casefold()
    for needle, label in REPOSITORY_HOSTS:
        if needle in lowered:
            return label
    return "Other"


def _descriptor_labels(items: Any) -> list[str]:
    """Pull display labels out of a list of Descriptor-shaped dicts."""
    labels: list[str] = []
    for item in items or []:
        if not isinstance(item, dict):
            continue
        term = item.get("term") if isinstance(item.get("term"), dict) else {}
        label = item.get("preferred_term") or term.get("label") or term.get("id")
        if label:
            labels.append(str(label))
    return labels


def _descriptor_ids(items: Any) -> list[str]:
    ids: list[str] = []
    for item in items or []:
        if not isinstance(item, dict):
            continue
        term = item.get("term") if isinstance(item.get("term"), dict) else {}
        if term.get("id"):
            ids.append(str(term["id"]))
    return ids


def _collect_reference_ids(evidence: Any) -> list[str]:
    refs: list[str] = []
    for item in evidence or []:
        if isinstance(item, dict):
            ref = item.get("reference")
            if isinstance(ref, str) and ref.strip():
                refs.append(ref.strip())
    return refs


class ModelsExporter:
    """Export computational models to browser-friendly JSON/JS records."""

    def __init__(self, models_dir: Path = Path("models")):
        #: Model ids with a runnable dismech-perturb config checked into ``models/``.
        self.runnable_model_ids: set[str] = set()
        if models_dir.exists():
            for config in models_dir.glob("*.config.yaml"):
                self.runnable_model_ids.add(config.name[: -len(".config.yaml")])

    def load_entry(self, file_path: Path) -> dict[str, Any]:
        with open(file_path) as f:
            return safe_load(f) or {}

    def extract_models(
        self,
        entry: dict[str, Any],
        *,
        source_type: str,
        source_file: str,
        page_url: str,
    ) -> list[dict[str, Any]]:
        """Extract one record per computational model in ``entry``."""
        records: list[dict[str, Any]] = []
        source_name = entry.get("name", "Unknown")
        creation_date = entry.get("creation_date")

        # Disease-class facets are only meaningful for disorder entries.
        parents = entry.get("parents", []) if source_type == "Disorder" else []
        category = entry.get("category", "") if source_type == "Disorder" else ""

        disease_id = None
        disease_term = entry.get("disease_term") or {}
        if isinstance(disease_term, dict) and isinstance(disease_term.get("term"), dict):
            disease_id = disease_term["term"].get("id")

        for idx, model in enumerate(entry.get("computational_models") or []):
            if not isinstance(model, dict):
                continue
            name = model.get("name")
            if not name:
                continue

            anchor = make_anchor_id(str(name))
            model_id = model.get("model_id") or ""
            variables = [
                v for v in (model.get("variables") or []) if isinstance(v, dict)
            ]
            variable_names = [str(v["name"]) for v in variables if v.get("name")]
            variable_ids = [
                str(v["dataset_identifier"])
                for v in variables
                if v.get("dataset_identifier")
            ]
            variable_terms: list[str] = []
            for var in variables:
                variable_terms.extend(_descriptor_labels(var.get("mappings_list")))

            mechanisms = [
                str(link["target"])
                for link in (model.get("modeled_mechanisms") or [])
                if isinstance(link, dict) and link.get("target")
            ]
            findings = [
                str(f["statement"])
                for f in (model.get("findings") or [])
                if isinstance(f, dict) and f.get("statement")
            ]
            evidence_refs = _collect_reference_ids(model.get("evidence"))
            for finding in model.get("findings") or []:
                if isinstance(finding, dict):
                    evidence_refs.extend(_collect_reference_ids(finding.get("evidence")))

            publication = model.get("publication")
            if isinstance(publication, str) and publication.strip():
                publication = publication.strip()
            else:
                publication = ""

            records.append(
                {
                    # Composite id: model names repeat across disorders (e.g. the
                    # AGORA2 microbiome models), so the owning entry is part of it.
                    "model_key": f"{slugify(str(source_name))}--{anchor}--{idx}",
                    "name": str(name),
                    "description": model.get("description", "") or "",
                    "model_type": humanize_enum(model.get("model_type"))
                    or "Unclassified",
                    "model_type_raw": model.get("model_type") or "",
                    "model_format": (model.get("model_format") or "").strip()
                    or "Format not recorded",
                    "model_software": (model.get("model_software") or "").strip()
                    or "Software not recorded",
                    "base_model": model.get("base_model", "") or "",
                    "model_id": str(model_id),
                    "repository_url": model.get("repository_url", "") or "",
                    "repository_host": repository_host(model.get("repository_url")),
                    "publication": publication,
                    "runnable": (
                        "Runnable in-repo"
                        if model_id and str(model_id) in self.runnable_model_ids
                        else "Reference only"
                    ),
                    "source_type": source_type,
                    "source_name": str(source_name),
                    "disease_id": disease_id,
                    "category": category,
                    "parents": parents,
                    "variables": variable_names,
                    "variable_ids": variable_ids,
                    "variable_terms": sorted(set(variable_terms)),
                    "num_variables": len(variables),
                    "perturbations": _descriptor_labels(model.get("perturbations")),
                    "perturbation_ids": _descriptor_ids(model.get("perturbations")),
                    "modeled_mechanisms": mechanisms,
                    "num_mechanisms": len(mechanisms),
                    "findings": findings,
                    "num_findings": len(findings),
                    "evidence_refs": sorted(set(evidence_refs)),
                    "num_evidence": len(set(evidence_refs)),
                    "notes": model.get("notes", "") or "",
                    "creation_date": creation_date,
                    "page_url": f"{page_url}#{anchor}",
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
                    self.extract_models(
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
                    self.extract_models(
                        entry,
                        source_type="Module",
                        source_file=f"kb/modules/{file_path.name}",
                        page_url=f"../../pages/modules/{file_path.stem}.html",
                    )
                )

        # Stable ordering: by model name, then owning entry.
        records.sort(
            key=lambda r: (
                str(r.get("name") or "").casefold(),
                str(r.get("source_name") or "").casefold(),
            )
        )
        return records

    @staticmethod
    def build_summary_metrics(records: list[dict[str, Any]]) -> dict[str, int]:
        return {
            "total_models": len(records),
            "total_source_entries": len({r["source_name"] for r in records}),
            "total_model_types": len(
                {r["model_type"] for r in records if r["model_type"] != "Unclassified"}
            ),
            "total_runnable": sum(1 for r in records if r["runnable"] == "Runnable in-repo"),
            "total_with_repository": sum(1 for r in records if r["repository_url"]),
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

        print(f"Exported {len(records)} computational models to {output_path}")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Export computational model data for the models browser"
    )
    parser.add_argument(
        "--disorders-dir", default="kb/disorders", help="Disorder YAML directory"
    )
    parser.add_argument(
        "--modules-dir", default="kb/modules", help="Module YAML directory"
    )
    parser.add_argument(
        "--models-dir",
        default="models",
        help="Directory of runnable dismech-perturb model configs",
    )
    parser.add_argument(
        "--output", "-o", default="app/models/data.js", help="Output file path"
    )

    args = parser.parse_args()

    ModelsExporter(models_dir=Path(args.models_dir)).export_to_js(
        Path(args.output),
        disorders_dir=Path(args.disorders_dir),
        modules_dir=Path(args.modules_dir),
    )


if __name__ == "__main__":
    main()
