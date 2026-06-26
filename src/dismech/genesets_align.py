"""Align a gene set's curated biological processes to a disease pathograph.

The alignment unit is the **biological process** (GO BP/CC term), not the gene.
A `MYGENESET:` cache file carries a small, role-tagged list of curated GO terms
(``## Curated GO interpretation``); a disorder's pathograph independently curates
GO terms on its ``pathophysiology[].biological_processes``. This module matches
the two — **hierarchy-aware** (exact / ancestor / descendant over GO via OAK) and
**role-weighted** (the score is computed over the set's *core* terms; terms the
interpretation tagged ``nonspecific``/``false_association`` are expected to be
absent and only generate a lint warning if present).

It reads the set BPs from the committed ``references_cache/MYGENESET_*.md`` file
(no refresh needed) and the pathograph BPs from the disorder YAML.

See ``projects/GENESETS.md`` ("Scoring: align the curated BPs, not the genes").
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Optional

# Role buckets (AssociationCategoryEnum upstream).
CORE = frozenset({"core_process", "core_component"})
SUPPORTING = frozenset({"supporting_process", "marker_driven_plausible"})
NOISE = frozenset({"nonspecific", "false_association"})

# Match statuses, best → worst.
EXACT = "EXACT"
DESCENDANT = "DESCENDANT"  # pathograph term is more specific than the set term
ANCESTOR = "ANCESTOR"  # pathograph term is more general than the set term
NONE = "NONE"


@dataclass
class SetBP:
    go_id: str
    label: str
    aspect: str
    category: str
    confidence: str


@dataclass
class AlignmentRow:
    bp: SetBP
    status: str = NONE
    matched_id: str = ""
    matched_label: str = ""

    @property
    def represented(self) -> bool:
        # Only an exact term or a MORE SPECIFIC pathograph term (descendant)
        # counts as representing the curated BP. An ANCESTOR match means the
        # pathograph has only a *more general* term (e.g. set "oxidative
        # phosphorylation" vs pathograph "metabolic process") — that does not
        # mean the specific process is modeled, so it does not count.
        return self.status in (EXACT, DESCENDANT)


@dataclass
class AlignmentResult:
    set_id: str
    disease: str
    n_pathograph_bps: int
    rows: list[AlignmentRow] = field(default_factory=list)

    @property
    def core_rows(self) -> list[AlignmentRow]:
        return [r for r in self.rows if r.bp.category in CORE]

    @property
    def core_total(self) -> int:
        return len(self.core_rows)

    @property
    def core_covered(self) -> int:
        return sum(1 for r in self.core_rows if r.represented)

    @property
    def corroboration(self) -> Optional[float]:
        return self.core_covered / self.core_total if self.core_total else None

    @property
    def gaps(self) -> list[AlignmentRow]:
        """Core set BPs with no pathograph representation — the curation to-do."""
        return [r for r in self.core_rows if not r.represented]

    @property
    def lint(self) -> list[AlignmentRow]:
        """Noise-tagged BPs that ARE in the pathograph (modeled something flagged noise)."""
        return [r for r in self.rows if r.bp.category in NOISE and r.represented]


# ----- inputs -----

_GO_ROW_RE = re.compile(
    r"^\|\s*(GO:\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$"
)


def read_set_bps(cache_path: Path) -> list[SetBP]:
    """Parse the ``## Curated GO interpretation`` table from a MYGENESET cache file."""
    bps: list[SetBP] = []
    in_section = False
    for line in cache_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_section = line.strip() == "## Curated GO interpretation"
            continue
        if not in_section:
            continue
        m = _GO_ROW_RE.match(line)
        if m:
            go_id, label, aspect, category, confidence = (g.strip() for g in m.groups())
            bps.append(SetBP(go_id, label, aspect, category, confidence))
    return bps


def extract_pathograph_bps(disease_path: Path) -> dict[str, str]:
    """Collect every GO id -> label under any ``biological_processes`` list."""
    from ruamel.yaml import YAML

    yaml = YAML(typ="safe")
    data = yaml.load(disease_path)
    found: dict[str, str] = {}

    def walk(node: object) -> None:
        if isinstance(node, dict):
            for key, val in node.items():
                if key == "biological_processes" and isinstance(val, list):
                    for item in val:
                        term = (item or {}).get("term") if isinstance(item, dict) else None
                        if isinstance(term, dict) and term.get("id"):
                            found[str(term["id"])] = str(term.get("label", ""))
                else:
                    walk(val)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(data)
    return found


# ----- matching -----


def _hierarchical_match(
    go_id: str, pathograph_ids: set[str], adapter: object
) -> tuple[str, str]:
    """Return (status, matched_id) using GO subsumption; ('NONE','') if no match."""
    if go_id in pathograph_ids:
        return EXACT, go_id
    if adapter is None:
        return NONE, ""
    try:
        from oaklib.datamodels.vocabulary import IS_A, PART_OF

        preds = [IS_A, PART_OF]
        descendants = set(adapter.descendants(go_id, predicates=preds))
        hit = pathograph_ids & descendants
        if hit:
            return DESCENDANT, sorted(hit)[0]
        ancestors = set(adapter.ancestors(go_id, predicates=preds))
        hit = pathograph_ids & ancestors
        if hit:
            return ANCESTOR, sorted(hit)[0]
    except Exception:  # pragma: no cover - adapter/network hiccup → exact-only
        return NONE, ""
    return NONE, ""


def align(
    set_id: str,
    disease: str,
    set_bps: Iterable[SetBP],
    pathograph_bps: dict[str, str],
    adapter: object = None,
) -> AlignmentResult:
    """Align a set's curated BPs to a pathograph's BPs (hierarchy-aware)."""
    pathograph_ids = set(pathograph_bps)
    result = AlignmentResult(
        set_id=set_id, disease=disease, n_pathograph_bps=len(pathograph_ids)
    )
    for bp in set_bps:
        status, matched = _hierarchical_match(bp.go_id, pathograph_ids, adapter)
        result.rows.append(
            AlignmentRow(
                bp=bp,
                status=status,
                matched_id=matched,
                matched_label=pathograph_bps.get(matched, ""),
            )
        )
    return result


# ----- reporting -----


def format_report(result: AlignmentResult) -> str:
    out: list[str] = []
    out.append(f"Alignment: {result.set_id}  ↔  {result.disease}")
    out.append(f"Pathograph BPs: {result.n_pathograph_bps}")
    out.append("")
    out.append(f"Curated set BPs ({len(result.rows)}):")
    for r in result.rows:
        tag = f"[{r.bp.category}]"
        if r.represented:
            detail = f"{r.status} ({r.matched_id}"
            if r.matched_id != r.bp.go_id and r.matched_label:
                detail += f" {r.matched_label}"
            detail += ")"
        elif r.status == ANCESTOR:
            detail = f"broader only ({r.matched_id} {r.matched_label}) — not counted"
        else:
            detail = "absent (expected)" if r.bp.category in NOISE else "absent"
        out.append(f"  {tag:<13} {r.bp.go_id} {r.bp.label}  — {detail}")
    out.append("")
    if result.corroboration is None:
        out.append("Corroboration: n/a (set declares no core BPs)")
    else:
        pct = round(100 * result.corroboration)
        out.append(
            f"Corroboration (core BPs represented): "
            f"{result.core_covered}/{result.core_total} = {pct}%"
        )
    if result.gaps:
        out.append("Core-BP gaps (to curate):")
        for r in result.gaps:
            aspect = f" [{r.bp.aspect}]" if r.bp.aspect else ""
            broader = (
                f" (pathograph has only broader {r.matched_id})"
                if r.status == ANCESTOR
                else ""
            )
            out.append(f"  - {r.bp.go_id} {r.bp.label}{aspect}{broader}")
    else:
        out.append("Core-BP gaps (to curate): none")
    if result.lint:
        out.append("Lint (noise-tagged BPs present in pathograph — review):")
        for r in result.lint:
            out.append(f"  - {r.bp.go_id} {r.bp.label} [{r.bp.category}]")
    return "\n".join(out)
