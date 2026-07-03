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


_CTX_DISEASE_RE = re.compile(r"^\|\s*disease\s*\|\s*(MONDO:\d+)\s*\|")


def disease_context_mondo(cache_path: Path) -> Optional[str]:
    """Return the disease-context MONDO id from a MYGENESET cache file, if any."""
    in_ctx = False
    for line in cache_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_ctx = line.strip() == "## Context"
            continue
        if in_ctx:
            m = _CTX_DISEASE_RE.match(line)
            if m:
                return m.group(1)
    return None


def build_mondo_index(kb_dir: Path) -> dict[str, str]:
    """Map a disorder's primary disease MONDO id -> its slug (filename stem).

    Approximate: one disorder is kept per MONDO (first by sorted filename), so
    a MONDO shared by several subtype entries resolves to one. Advisory only.
    """
    from ruamel.yaml import YAML

    yaml = YAML(typ="safe")
    index: dict[str, str] = {}
    for path in sorted(kb_dir.glob("*.yaml")):
        try:
            data = yaml.load(path)
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        mondo = _primary_mondo(data)
        if mondo and mondo not in index:
            index[mondo] = path.stem
    return index


def _primary_mondo(data: dict) -> Optional[str]:
    for key in ("disease_term", "mappings", "mondo", "meaning"):
        val = data.get(key)
        candidates = val if isinstance(val, list) else [val]
        for cand in candidates:
            if isinstance(cand, dict):
                term = cand.get("term", cand)
                if isinstance(term, dict) and str(term.get("id", "")).startswith("MONDO:"):
                    return str(term["id"])
    return None


# Descriptor lists whose GO terms count as pathograph terms for alignment.
# Includes cellular_components / protein_complexes so a set's GO CC term
# (e.g. MHC class II protein complex) can match when the disorder models it.
_TERM_BEARING_KEYS = frozenset(
    {
        "biological_processes",
        "cellular_components",
        "protein_complexes",
        "molecular_functions",
    }
)


def extract_pathograph_bps(disease_path: Path) -> dict[str, str]:
    """Collect every GO id -> label under any term-bearing descriptor list."""
    from ruamel.yaml import YAML

    yaml = YAML(typ="safe")
    data = yaml.load(disease_path)
    found: dict[str, str] = {}

    def walk(node: object) -> None:
        if isinstance(node, dict):
            for key, val in node.items():
                if key in _TERM_BEARING_KEYS and isinstance(val, list):
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


@dataclass
class SweepEntry:
    set_id: str  # local id, e.g. KEGG_ASTHMA
    mondo: Optional[str]
    disorder: Optional[str]  # slug, or None if no dismech entry
    result: Optional[AlignmentResult] = None
    source: str = ""  # "declared" (precise gene_sets link) or "mondo" (guess)


def collect_declared_gene_sets(kb_dir: Path) -> dict[str, list[str]]:
    """Map a set's local id -> the disorder slugs that explicitly declare it.

    Reads each disorder's ``gene_sets[].gene_set`` slot, so the disease<->set
    link is curated (precise), not guessed from a shared MONDO id.
    """
    from ruamel.yaml import YAML

    yaml = YAML(typ="safe")
    declared: dict[str, list[str]] = {}
    for path in sorted(kb_dir.glob("*.yaml")):
        try:
            data = yaml.load(path)
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        for assoc in data.get("gene_sets", []) or []:
            ref = str((assoc or {}).get("gene_set", ""))
            if not ref:
                continue
            local_id = ref.split(":", 1)[1] if ref.upper().startswith("MYGENESET:") else ref
            declared.setdefault(local_id, []).append(path.stem)
    return declared


def sweep(cache_dir: Path, kb_dir: Path, adapter: object = None) -> list[SweepEntry]:
    """Align disease-context sets to disorders.

    Precise first: a set explicitly declared by a disorder's ``gene_sets`` slot
    aligns against that disorder. Sets with no declaration fall back to a
    MONDO-based guess (one disorder per disease-context MONDO), flagged as such.
    """
    declared = collect_declared_gene_sets(kb_dir)
    mondo_index = build_mondo_index(kb_dir)
    entries: list[SweepEntry] = []

    def _align(local_id: str, slug: str, mondo: Optional[str], source: str) -> SweepEntry:
        result = None
        if slug and (kb_dir / f"{slug}.yaml").exists():
            set_bps = read_set_bps(cache_dir / f"MYGENESET_{local_id}.md")
            pathograph = extract_pathograph_bps(kb_dir / f"{slug}.yaml")
            result = align(f"MYGENESET:{local_id}", slug, set_bps, pathograph, adapter)
        return SweepEntry(local_id, mondo, slug, result, source)

    for cache in sorted(cache_dir.glob("MYGENESET_*.md")):
        local_id = cache.stem.removeprefix("MYGENESET_")
        if local_id in declared:
            for slug in declared[local_id]:
                entries.append(_align(local_id, slug, disease_context_mondo(cache), "declared"))
            continue
        mondo = disease_context_mondo(cache)
        if not mondo:
            continue  # not a disease-context set and not explicitly declared
        entries.append(_align(local_id, mondo_index.get(mondo), mondo, "mondo"))
    return entries


def format_sweep(entries: list[SweepEntry]) -> str:
    n_declared = sum(1 for e in entries if e.source == "declared")
    out = [
        f"{len(entries)} alignments "
        f"({sum(1 for e in entries if e.result)} mapped to a dismech disorder; "
        f"{n_declared} via explicit gene_sets link, rest MONDO-guess)",
        "",
        "| Gene set | dismech disorder | Map | Corroboration | Core-BP gaps |",
        "|---|---|---|---|---|",
    ]
    for e in entries:
        mark = "declared" if e.source == "declared" else "mondo?"
        if e.result is None:
            out.append(f"| {e.set_id} | — (no entry for {e.mondo}) | {mark} |  |  |")
            continue
        r = e.result
        corr = f"{r.core_covered}/{r.core_total}"
        if r.corroboration is not None:
            corr += f" ({round(100 * r.corroboration)}%)"
        gaps = "; ".join(g.bp.label for g in r.gaps) or "—"
        out.append(f"| {e.set_id} | {e.disorder} | {mark} | {corr} | {gaps} |")
    return "\n".join(out)


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
