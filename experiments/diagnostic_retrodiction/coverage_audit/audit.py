"""Coverage audit: does a disease's pathograph carry a discriminating, accessible node?

For each disease in negatives.tsv, and each frame.tsv entry with no flagged
(accessible, non-germline) row, ask whether its pathograph holds at least one
node that (a) is measurable in an accessible specimen and (b) appears in none
of its differential diagnoses' pathographs.

Definitions (all fixed here, none tuned per disease):

KB version
    kb/disorders/ as of PINNED_COMMIT, the tree frame.tsv was built from,
    extracted with ``git archive`` into tmp/coverage_audit_kb/. The working
    tree's kb/ is never read.

Pathograph nodes
    dismech.graph.iter_graph_node_rows. Only node types that describe the
    patient are candidates: pathophysiology, phenotype, biochemical, genetic.
    Treatments, exposures and model nodes are not states one can measure.

Measurable in an accessible specimen
    census.classify() -- the same rule that set flag_nongenetic_specimen in the
    frame -- applied to the node's *identity text*: its name plus the labels of
    its identity terms (IDENTITY_KEYS: phenotype_term, biomarker_term,
    loinc_term, gene_term, chemical_entities). Description prose and context
    terms (cell_types, biological_processes, locations, genes) are not read:
    against those, every immune node with a leukocyte cell type and every
    node mentioning a blood vessel resolved to BLOOD. Phrases in which "blood"
    names no specimen (NOT_A_SPECIMEN_RE: blood pressure, blood vessel, blood
    flow, urinary tract, ...) are masked first. A node passes when classify()
    returns flag_nongenetic_specimen TRUE (an accessible specimen resolved and
    not a germline genetic test). The analyte-class IMPLICIT rule may supply
    the specimen only for phenotype and biochemical nodes; a pathophysiology
    or genetic node must name its specimen, because census's enzyme-activity
    pattern otherwise turns "CDK4/6 kinase activity" into a blood test.

Differential pathographs
    Each differential_diagnoses[] item is resolved to a kb entry by its
    disease_term MONDO id, else by exact (case-folded) entry name. Unresolved
    differentials are counted but cannot be compared.

Appears in a differential
    STRICT (primary): some node of a resolved differential has the same
    normalised name, or shares any identity-term CURIE with the candidate node.
    NAME_ONLY (reported alongside): same normalised name only.

Status per disease
    HAS_UNIQUE_NODE       >=1 measurable node absent from every resolved differential
    NO_UNIQUE_NODE        measurable nodes exist, all shared with a differential
    NO_MEASURABLE_NODE    no measurable node at all
    NO_DIFFERENTIALS      measurable nodes exist but no differential is listed
    NO_RESOLVED_DIFFERENTIALS  differentials listed, none resolves to a kb entry
    NOT_IN_KB             the entry file is absent at PINNED_COMMIT

Usage:
    uv run python experiments/diagnostic_retrodiction/coverage_audit/audit.py
"""
from __future__ import annotations

import csv
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
REPO = EXP.parents[1]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(EXP))

from dismech.graph import iter_graph_node_rows  # noqa: E402
import census  # noqa: E402

MEASURABLE_TYPES = {"pathophysiology", "phenotype", "biochemical", "genetic"}
SECTION_OF = {"pathophysiology": "pathophysiology", "phenotype": "phenotypes",
              "biochemical": "biochemical", "genetic": "genetic"}
IDENTITY_KEYS = ("phenotype_term", "biomarker_term", "loinc_term", "gene_term", "chemical_entities")
NOT_A_SPECIMEN_RE = re.compile(
    r"\bblood[- ](pressure|vessel\w*|flow|supply|loss|brain barrier|stream|volume)\b|"
    r"\b(high|low) blood\b|\bbloody\b|"
    r"\burinary (tract|bladder|incontinence|retention|system|urgency|frequency|symptom\w*)\b|"
    r"\bblood[- ]\w+ barrier\b|\bnormal blood\b|\bplasma[- ](membrane|cell\w*)\b|"
    r"\b(csf|cerebrospinal fluid) (outflow|pathway\w*|flow|circulation|space\w*)\b|"
    r"\b(leukocyte|lymphocyte|platelet|erythrocyte)\w* (infiltrat\w*|recruitment)\b|"
    r"\binfiltrat\w*\b.*", re.I)
#: Node types for which the analyte-class (IMPLICIT) rule may supply the
#: specimen. A pathophysiology node named "... kinase activity" is a molecular
#: state, not an assay, so it must state its specimen.
IMPLICIT_OK_TYPES = {"phenotype", "biochemical"}
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

FIELDS = ["disease", "kb_file", "mondo_id", "source", "frame_flagged_rows", "n_nodes",
          "n_measurable", "n_differentials", "n_resolved_differentials", "unresolved_differentials",
          "n_unique_strict", "n_unique_name_only", "status", "status_name_only",
          "unique_nodes_strict", "measurable_nodes"]


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def walk_terms(obj: Any, ids: set[str], labels: list[str]) -> None:
    """Collect every term.id / term.label nested in ``obj``."""
    if isinstance(obj, dict):
        term = obj.get("term")
        if isinstance(term, dict):
            if term.get("id"):
                ids.add(str(term["id"]))
            if term.get("label"):
                labels.append(str(term["label"]))
        for k, v in obj.items():
            if k in ("evidence", "downstream", "sequelae", "reports_on", "notes", "description"):
                continue  # edges and prose belong to other nodes or to no identity
            walk_terms(v, ids, labels)
    elif isinstance(obj, list):
        for v in obj:
            walk_terms(v, ids, labels)


def node_table(doc: dict) -> list[dict]:
    """One record per pathograph node with its CURIEs and identity text."""
    items: dict[tuple[str, str], dict] = {}
    for section in ("pathophysiology", "phenotypes", "biochemical", "genetic"):
        for it in doc.get(section) or []:
            if isinstance(it, dict) and it.get("name"):
                items[(section, it["name"])] = it
    out = []
    for row in iter_graph_node_rows(doc):
        ids: set[str] = set()
        labels: list[str] = []
        raw = items.get((SECTION_OF.get(row.node_type, ""), row.name))
        if raw is not None:
            for key in IDENTITY_KEYS:
                if key in raw:
                    walk_terms(raw[key], ids, labels)
        out.append({"name": row.name, "type": row.node_type, "ids": ids,
                    "identity": " ".join([row.name, *labels])})
    return out


def is_measurable(node: dict, disease_context: str) -> bool:
    if node["type"] not in MEASURABLE_TYPES:
        return False
    text = NOT_A_SPECIMEN_RE.sub(" ", node["identity"])
    c = census.classify(text, text, [], disease_context, {})
    if c["specimen_basis"] == "IMPLICIT" and node["type"] not in IMPLICIT_OK_TYPES:
        return False
    return c["flag_nongenetic_specimen"] == "TRUE"


def extract_kb(commit: str) -> Path:
    dest = REPO / "tmp" / "coverage_audit_kb" / commit[:11]
    if not (dest / "kb" / "disorders").is_dir():
        dest.mkdir(parents=True, exist_ok=True)
        archive = subprocess.run(["git", "archive", commit, "kb/disorders"], cwd=REPO,
                                 capture_output=True, check=True).stdout
        subprocess.run(["tar", "-x", "-C", str(dest)], input=archive, check=True)
    return dest / "kb" / "disorders"


def main() -> None:
    commit = (EXP / "PINNED_COMMIT").read_text().strip()
    kb_dir = extract_kb(commit)

    docs: dict[str, dict] = {}
    for p in sorted(kb_dir.glob("*.yaml")):
        try:
            d = yaml.load(p.read_text(encoding="utf-8"), Loader=LOADER)
        except yaml.YAMLError:
            continue
        if isinstance(d, dict) and d.get("name"):
            docs[p.stem] = d
    by_mondo: dict[str, str] = {}
    by_name: dict[str, str] = {}
    for stem, d in docs.items():
        mid = ((d.get("disease_term") or {}).get("term") or {}).get("id")
        if mid:
            by_mondo.setdefault(mid, stem)
        by_name.setdefault(d["name"].casefold(), stem)
    node_cache: dict[str, list[dict]] = {}

    def nodes(stem: str) -> list[dict]:
        if stem not in node_cache:
            node_cache[stem] = node_table(docs[stem])
        return node_cache[stem]

    frame = list(csv.DictReader(open(EXP / "frame.tsv", newline="", encoding="utf-8"), delimiter="\t"))
    flagged = Counter(r["disease_name"] for r in frame if r["flag_nongenetic_specimen"] == "TRUE")
    entries = list(dict.fromkeys(r["disease_name"] for r in frame))

    targets: list[tuple[str, str]] = []  # (stem or "", source)
    seen: set[str] = set()
    for r in csv.DictReader(open(EXP / "negatives.tsv", newline="", encoding="utf-8"), delimiter="\t"):
        stem = Path(r["kb_file"]).stem
        targets.append((stem, "NEGATIVE"))
        seen.add(stem)
    for name in entries:
        if flagged[name]:
            continue
        stem = by_name.get(name.casefold(), "")
        if stem and stem in seen:
            continue
        seen.add(stem or name)
        targets.append((stem or f"?{name}", "FRAME_NO_ACCESSIBLE_TEST"))

    rows = []
    for stem, source in targets:
        if stem.startswith("?") or stem not in docs:
            rows.append({**{f: "" for f in FIELDS}, "disease": stem.lstrip("?"), "source": source,
                         "status": "NOT_IN_KB", "status_name_only": "NOT_IN_KB"})
            continue
        d = docs[stem]
        context = " ".join([d["name"], *(str(c) for c in d.get("categories") or [])])
        own = nodes(stem)
        meas = [n for n in own if is_measurable(n, context)]

        diffs = [x for x in d.get("differential_diagnoses") or [] if isinstance(x, dict)]
        resolved, unresolved = [], []
        for x in diffs:
            mid = ((x.get("disease_term") or {}).get("term") or {}).get("id")
            target = by_mondo.get(mid) if mid else None
            target = target or by_name.get(str(x.get("name", "")).casefold())
            if target and target != stem:
                resolved.append(target)
            else:
                unresolved.append(str(x.get("name", "?")))
        resolved = list(dict.fromkeys(resolved))
        diff_names, diff_ids = set(), set()
        for t in resolved:
            for n in nodes(t):
                diff_names.add(norm(n["name"]))
                diff_ids |= n["ids"]

        uniq_name = [n for n in meas if norm(n["name"]) not in diff_names]
        uniq_strict = [n for n in uniq_name if not (n["ids"] & diff_ids)]

        def status(uniq: list) -> str:
            if not meas:
                return "NO_MEASURABLE_NODE"
            if not diffs:
                return "NO_DIFFERENTIALS"
            if not resolved:
                return "NO_RESOLVED_DIFFERENTIALS"
            return "HAS_UNIQUE_NODE" if uniq else "NO_UNIQUE_NODE"

        rows.append({
            "disease": d["name"], "kb_file": f"kb/disorders/{stem}.yaml",
            "mondo_id": ((d.get("disease_term") or {}).get("term") or {}).get("id", ""),
            "source": source, "frame_flagged_rows": str(flagged.get(d["name"], 0)),
            "n_nodes": str(len(own)), "n_measurable": str(len(meas)),
            "n_differentials": str(len(diffs)), "n_resolved_differentials": str(len(resolved)),
            "unresolved_differentials": "; ".join(unresolved),
            "n_unique_strict": str(len(uniq_strict)), "n_unique_name_only": str(len(uniq_name)),
            "status": status(uniq_strict), "status_name_only": status(uniq_name),
            "unique_nodes_strict": "; ".join(n["name"] for n in uniq_strict),
            "measurable_nodes": "; ".join(n["name"] for n in meas),
        })

    with open(EXP / "coverage.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    for source in ("NEGATIVE", "FRAME_NO_ACCESSIBLE_TEST"):
        sub = [r for r in rows if r["source"] == source]
        print(source, len(sub), dict(Counter(r["status"] for r in sub)),
              "name_only:", dict(Counter(r["status_name_only"] for r in sub)), file=sys.stderr)


if __name__ == "__main__":
    main()
