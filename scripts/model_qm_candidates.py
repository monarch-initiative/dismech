#!/usr/bin/env python3
"""Filter dismech's computational models for quantitative medicine candidates.

FDA defines quantitative medicine (QM) as mathematical and computational models
integrated with biological, clinical and statistical data "to inform drug
development, regulatory, and clinical decisions" (Federal Register 2026-15887).
A model counts only when it has all three parts: a model, data, a decision.

dismech does not rank models -- `docs/explanation/model-credibility.md` says a
model-to-mechanism link is "not a quality score" -- so this does not either. It
turns each part of the definition into a filter over fields dismech already
has, applies them in order to every `computational_models` record, and reports
how many models survive each step and which ones are left:

1. **Mechanistic** (model): `model_type` is one of `MECHANISTIC_TYPES`.
2. **Rerunnable** (model): the model's `model_id` names a folder in `models/`,
   or the record carries `model_format` plus a `model_id` or `repository_url`.
3. **Tied to patient measurements** (data): at least one `variables[]`
   mapping binds a LOINC test or an HPO phenotype.
4. **Tied to a decision** (decision): a node the model's `modeled_mechanisms`
   names is also a `treatments[].target_mechanisms` target in the same entry,
   or is read out by a biomarker that carries `regulatory_endpoint_refs` (a
   row of the FDA Surrogate Endpoint Table).
5. **Credible for that use**: drops nothing. The survivors' decision links are
   listed with `relationship`, `fidelity` and typed `divergences`, ordered so a
   reader meets the links with the fewest recorded problems first.

**A filter step is a reading of what is recorded, not a judgement of the
model.** A model fails step 3 when nobody has mapped its outputs, which says
nothing about whether it could be. And step 5 orders by recorded fields only;
an absent `fidelity` sorts after every recorded value, because it is unknown,
not because it is bad.

Only top-level `computational_models` are read. Animal and in vitro models
are a different question, and a model system inside a proposed experiment has
not been run.

Usage:
    model_qm_candidates.py
    model_qm_candidates.py --format tsv --out qm_candidates.tsv
    model_qm_candidates.py --format json

Report-only; exits 0. Needs PyYAML; run it with uv from the repo root.
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit(
        "error: PyYAML not importable. Run it with uv, e.g.\n"
        "  uv run python scripts/model_qm_candidates.py"
    )

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from model_inventory import repo_commit

from dismech import kb_cache
from dismech.model_registry import iter_model_dirs

REPO_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_GLOBS = (
    "kb/disorders/*.yaml",
    "kb/modules/*.yaml",
    "kb/comorbidities/*.yaml",
)

#: `ComputationalModelTypeEnum` values that describe a mechanism quantitatively,
#: the kind of model quantitative medicine usually means. Statistical and
#: machine-learning models can be QM too, but the enum does not separate a
#: population-PK model from an image classifier, so neither is admitted here.
MECHANISTIC_TYPES = frozenset(
    {"KINETIC", "PHYSIOLOGICAL", "DIGITAL_TWIN", "AGENT_BASED"}
)

#: A variable mapped to one of these is tied to something measured in patients:
#: a laboratory test, or a clinical phenotype.
PATIENT_MEASUREMENT_PREFIXES = ("LOINC:", "HP:")

STEPS = (
    ("mechanistic", "Mechanistic", "model"),
    ("rerunnable", "Rerunnable", "model"),
    ("patient_measurements", "Tied to patient measurements", "data"),
    ("decision", "Tied to a decision", "decision"),
)

#: Read order for step 5. Lower sorts first. Absent sorts after every value.
FIDELITY_ORDER = {"HIGH": 0, "MODERATE": 1, "LOW": 2, "UNKNOWN": 3}


def _list(value) -> list:
    return value if isinstance(value, list) else []


def decision_targets(doc: dict) -> dict[str, list[str]]:
    """Node name -> the decision routes that reach it in this entry."""
    routes: dict[str, list[str]] = {}
    for treatment in _list(doc.get("treatments")):
        if not isinstance(treatment, dict):
            continue
        for tm in _list(treatment.get("target_mechanisms")):
            if isinstance(tm, dict) and tm.get("target"):
                routes.setdefault(tm["target"], [])
                if "treatment target" not in routes[tm["target"]]:
                    routes[tm["target"]].append("treatment target")
    for marker in _list(doc.get("biochemical")):
        if not isinstance(marker, dict):
            continue
        for readout in _list(marker.get("readouts")):
            if (
                isinstance(readout, dict)
                and readout.get("target")
                and readout.get("regulatory_endpoint_refs")
            ):
                routes.setdefault(readout["target"], [])
                if "FDA surrogate endpoint" not in routes[readout["target"]]:
                    routes[readout["target"]].append("FDA surrogate endpoint")
    return routes


def patient_mappings(model: dict) -> list[str]:
    """CURIEs of the LOINC or HPO terms the model's variables map to."""
    found = []
    for variable in _list(model.get("variables")):
        if not isinstance(variable, dict):
            continue
        for mapping in _list(variable.get("mappings_list")):
            term = mapping.get("term") if isinstance(mapping, dict) else None
            curie = term.get("id") if isinstance(term, dict) else None
            if isinstance(curie, str) and curie.startswith(
                PATIENT_MEASUREMENT_PREFIXES
            ):
                found.append(curie)
    return found


def assess(model: dict, doc: dict, repo_model_ids: set[str]) -> dict:
    """Each step's verdict for one model, plus what step 5 reads."""
    model_type = model.get("model_type") or ""
    model_id = model.get("model_id") or ""
    in_repo = bool(model_id) and model_id in repo_model_ids
    mappings = patient_mappings(model)
    routes = decision_targets(doc)

    decision_links = []
    for link in _list(model.get("modeled_mechanisms")):
        if not isinstance(link, dict) or link.get("target") not in routes:
            continue
        decision_links.append(
            {
                "target": link["target"],
                "routes": routes[link["target"]],
                "relationship": link.get("relationship") or "",
                "fidelity": link.get("fidelity") or "",
                "divergences": [
                    {
                        "type": d.get("divergence_type") or "",
                        "materiality": d.get("materiality") or "",
                    }
                    for d in _list(link.get("divergences"))
                    if isinstance(d, dict)
                ],
            }
        )

    passed = {
        "mechanistic": model_type in MECHANISTIC_TYPES,
        "rerunnable": in_repo
        or bool(model.get("model_format"))
        and bool(model_id or model.get("repository_url")),
        "patient_measurements": bool(mappings),
        "decision": bool(decision_links),
    }
    first_failed = next((key for key, _, _ in STEPS if not passed[key]), "")
    return {
        "name": model.get("name") or "(unnamed)",
        "model_type": model_type,
        "model_id": model_id,
        "in_models_dir": in_repo,
        "patient_mappings": mappings,
        "passed": passed,
        "first_failed": first_failed,
        "decision_links": decision_links,
    }


def read_order(link: dict) -> tuple:
    """Step 5's ordering: fewest recorded problems first. Not a score."""
    invalidating = any(d["materiality"] == "INVALIDATING" for d in link["divergences"])
    return (
        invalidating,
        link["relationship"] == "FAILS_TO_RECAPITULATE",
        FIDELITY_ORDER.get(link["fidelity"], len(FIDELITY_ORDER)),
    )


def collect(repo: Path, globs: list[str]) -> dict:
    repo_model_ids = {p.name for p in iter_model_dirs(repo / "models")}
    models: list[dict] = []
    errors: list[dict] = []
    files: list[Path] = []
    for pattern in globs:
        files += sorted(repo.glob(pattern))

    for path in files:
        rel = str(path.relative_to(repo))
        try:
            doc = kb_cache.load_document(path)
        except (yaml.YAMLError, OSError) as exc:
            errors.append({"file": rel, "error": str(exc)[:200]})
            continue
        if not isinstance(doc, dict):
            continue
        for index, model in enumerate(_list(doc.get("computational_models"))):
            if not isinstance(model, dict):
                continue
            row = assess(model, doc, repo_model_ids)
            row["entry"] = doc.get("name") or rel
            row["file"] = rel
            row["path"] = f"computational_models[{index}]"
            models.append(row)

    funnel = [("all", "All records", "", len(models))]
    remaining = models
    for key, label, part in STEPS:
        remaining = [m for m in remaining if m["passed"][key]]
        funnel.append((key, label, part, len(remaining)))

    return {
        "repo": str(repo),
        "commit": repo_commit(repo),
        "generated": datetime.datetime.now(datetime.UTC).date().isoformat(),
        "globs": globs,
        "files_parsed": len(files) - len(errors),
        "parse_errors": errors,
        "mapped_to_patient_measurements": sum(
            1 for m in models if m["passed"]["patient_measurements"]
        ),
        "funnel": [
            {"step": k, "label": label, "part": part, "kept": n}
            for k, label, part, n in funnel
        ],
        "candidates": [m for m in remaining],
        "models": models,
    }


def _divergence_text(link: dict) -> str:
    if not link["divergences"]:
        return "none recorded"
    return "; ".join(
        f"{d['type'] or '(untyped)'} ({(d['materiality'] or 'materiality not recorded').lower()})"
        for d in link["divergences"]
    )


def render_md(res: dict) -> str:
    total = res["funnel"][0]["kept"]
    out = [
        "# Quantitative medicine candidates among dismech's computational models",
        "",
        f"- Repo: `{res['repo']}`",
        f"- Commit: `{res['commit']}`",
        f"- Run on: {res['generated']}",
        f"- Files parsed: {res['files_parsed']} from "
        + ", ".join("`" + g + "`" for g in res["globs"]),
        (
            f"- Models whose variables map to a LOINC test or HPO phenotype: "
            f"{res['mapped_to_patient_measurements']} of {total}"
        ),
        "",
        (
            "Each step reads fields dismech already records. A model that fails "
            "a step has not had that field filled in; that is not a judgement "
            "of the model."
        ),
        "",
        "## Models left after each step",
        "",
        "| Step | Keep models that are | Part of the definition | Kept |",
        "|---|---|---|---|",
    ]
    previous = total
    for i, step in enumerate(res["funnel"]):
        if i == 0:
            out.append(f"| 0 | {step['label']} | -- | {step['kept']} |")
            continue
        out.append(
            f"| {i} | {step['label']} | {step['part']} | {step['kept']} of {previous} |"
        )
        previous = step["kept"]
    out.append("| 5 | Credible for that use | -- | orders, drops nothing |")
    out.append("")

    out += ["## Candidates and step 5", ""]
    if not res["candidates"]:
        out += ["No model passes steps 1-4.", ""]
    for model in res["candidates"]:
        out += [
            f"### {model['name']}",
            "",
            f"- Entry: {model['entry']} (`{model['file']}`, `{model['path']}`)",
            f"- Type: `{model['model_type']}`"
            + (
                f"; runs in `models/{model['model_id']}/`"
                if model["in_models_dir"]
                else ""
            ),
            f"- Patient measurements: {', '.join(sorted(set(model['patient_mappings'])))}",
            "",
            "| Decision link | Route | Relationship | Fidelity | Divergences |",
            "|---|---|---|---|---|",
        ]
        for link in sorted(model["decision_links"], key=read_order):
            out.append(
                f"| {link['target']} | {', '.join(link['routes'])} "
                f"| {link['relationship'] or '(not recorded)'} "
                f"| {link['fidelity'] or '(not recorded)'} "
                f"| {_divergence_text(link)} |"
            )
        out.append("")

    if res["parse_errors"]:
        out += ["## Files that would not parse", ""]
        out += [f"- `{e['file']}`: {e['error']}" for e in res["parse_errors"]]
        out.append("")
    return "\n".join(out)


def render_tsv(res: dict) -> str:
    cols = [
        "entry",
        "model",
        "model_type",
        "model_id",
        *[key for key, _, _ in STEPS],
        "first_failed",
        "decision_targets",
        "path",
        "file",
    ]
    rows = ["\t".join(cols)]
    for model in res["models"]:
        rows.append(
            "\t".join(
                [
                    model["entry"],
                    model["name"],
                    model["model_type"],
                    model["model_id"],
                    *[str(model["passed"][key]) for key, _, _ in STEPS],
                    model["first_failed"],
                    "; ".join(link["target"] for link in model["decision_links"]),
                    model["path"],
                    model["file"],
                ]
            )
        )
    return "\n".join(rows) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--repo", default=REPO_ROOT, type=Path)
    ap.add_argument(
        "--glob",
        action="append",
        dest="globs",
        help="KB glob, repeatable (default: disorders, modules, comorbidities)",
    )
    ap.add_argument("--format", choices=("md", "tsv", "json"), default="md")
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    if not args.repo.is_dir():
        print(f"error: no such repo: {args.repo}", file=sys.stderr)
        return 1

    # One walk over the corpus, so the parsed-KB cache would only cost memory.
    kb_cache.default_off()
    res = collect(args.repo, args.globs or list(DEFAULT_GLOBS))

    if args.format == "md":
        text = render_md(res)
    elif args.format == "tsv":
        text = render_tsv(res)
    else:
        text = json.dumps(res, indent=2)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
