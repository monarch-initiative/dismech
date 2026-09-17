#!/usr/bin/env python3
"""Report infectious-disease entries against the granularity ladder (issue #10115).

Design decisions §3e fixes how finely an infectious disease is split: the
default entry is the named clinical entity, organism strata below it are
``has_subtypes`` only when documented to differ, a stratum is promoted to its
own entry only on two differentiating axes, and a phase is never an entry.
Several of those rules are mechanically checkable and several are not. This
script draws that line rather than blurring it:

Deterministic classes (``--strict`` gates on them)
    A finding here is a defect under the ladder with no judgement involved --
    an entry with no ``infectious_agent`` block, an agent with no NCBITaxon
    binding, no ``transmission`` block, an entry anchored to ``MONDO:0005550``
    *infectious disease* itself, a subtype naming a disease that already has
    its own entry without saying so, two entries sharing a ``disease_term``
    with no ``skos:narrowMatch`` between them, two agents in one entry bound
    to the same taxon, a ``curated_in`` pointer at a file that does not exist.

Advisory classes (never gate)
    A finding here is a *question* the ladder asks a curator, not an answer. An
    entry holding three organisms with no subtypes is the ladder's default
    state (rule R9: lump until the literature distinguishes them), so
    ``TAXON_LUMP`` means "nobody has recorded a decision", and it clears when
    the entry's ``review_notes`` records one (see ``LUMP_WAIVER_SENTINEL``).
    An unbound subtype may have no honest term to bind. A missing
    ``progression`` block matters only where the disease has phases.
    ``MISSING_LIFECYCLE`` is the one heuristic: it fires when the transmission
    text names a vector or non-human reservoir and no ``agent_life_cycle``
    block exists.

Informational classes
    Not findings at all, reported so the mechanism is visible: a subtype that
    carries ``curated_in`` is a *pointer* to the entry where the stratum is
    curated in full, which is what the ladder prescribes for a promoted
    stratum (§3a L4, §3e rung 4) and what ``Spotted_Fever_Rickettsiosis`` was
    wrongly reported as violating. A recorded deliberate lump is the other.

What is deliberately not here
    Over-broad anchoring (``Travelers_Diarrhea`` on *diarrheal disease*) needs
    a MONDO descendant count, which needs the 588 MB MONDO build; that stays a
    manual audit. Grouping-shaped entries and phase-as-entry are judgement
    calls the ladder makes in prose.

Scope
    The ladder governs *microbial disease* entries, and the entries the KB
    marks with a pathogen are a wider set than that. An infection-attributed
    neoplasm follows the cancer ladder and its pathogen is an annotation (rule
    R23); a Mendelian susceptibility disorder follows the plain §3 rules; a
    post-infectious immune sequela is its own entry because its mechanism is
    host-immune (R22); a mycotoxicosis is not an infection. Those are excluded
    by :func:`scope_of`, which reports its reason, and the summary prints how
    many entries each exclusion removed so a changed rule is visible as a
    changed count. The neoplasm test is the one ``check_cancer_origin.py``
    uses, imported rather than duplicated.

    The pointer checks run on every entry, because ``curated_in`` is a KB-wide
    slot. The two other cross-entry classes (``DOUBLE_MODELLED``,
    ``DUPLICATE_ANCHOR``) are the mechanical half of #10113 and #10116 as much
    as of this ladder; ``--scope all`` runs them over the whole corpus, where
    the umbrella-entry pattern (``Epilepsy`` listing ``Juvenile Myoclonic
    Epilepsy``, which has its own entry) makes them a backlog in the hundreds.

The cross-entry index needs the whole corpus, so the script always walks
``kb/disorders`` once; naming files on the command line narrows what is
*reported*, not what is *read*.

    just check-granularity                       # census + worklist
    just check-granularity --format tsv          # one row per entry
    just check-granularity --format list         # one line per finding
    just check-granularity --strict              # exit 1 on deterministic findings
    just check-granularity --scope all           # cross-entry classes KB-wide
    just check-granularity kb/disorders/Cholera.yaml

Exit 0 on any number of findings unless ``--strict`` or ``--fail-on`` says
otherwise; 2 on a usage error (an unreadable path, a directory with no entries).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from check_cancer_origin import NEOPLASM_RE, NOT_NEOPLASM_RE  # noqa: E402
from dismech import kb_cache  # noqa: E402
from dismech.kb_cache import load_document  # noqa: E402

DEFAULT_KB_DIR = "kb/disorders"

# Rung 0 of the ladder: MONDO classes too abstract to carry a mechanism. An
# entry anchored here is a grouping wearing a Disease entry's clothes at best.
# Labels are copied from cache/mondo/terms.csv, not written from memory.
ROOT_TERMS: dict[str, str] = {
    "MONDO:0005550": "infectious disease",
    "MONDO:0005108": "viral infectious disease",
    "MONDO:0005113": "bacterial infectious disease",
    "MONDO:0002041": "fungal infectious disease",
    "MONDO:0005135": "parasitic infectious disease",
}

# Rule R9: the default is to lump, and a deliberate lump is recorded. Mirrors
# the `Left deliberately uncited.` waiver `check-environmental-evidence` reads,
# with the same floor on the reasoning that has to follow the sentinel. The
# sentinel must open a paragraph of the entry-level `review_notes`: `notes` is
# disease content and cannot waive, and prose merely mentioning the phrase
# does not trigger it.
LUMP_WAIVER_SENTINEL = "Deliberately lumped."
LUMP_WAIVER_MIN_WORDS = 20

# --- scope -------------------------------------------------------------------

SCOPE_INFECTIOUS = "INFECTIOUS"
SCOPE_NEOPLASM = "NEOPLASM"
SCOPE_MENDELIAN = "MENDELIAN"
SCOPE_SEQUELA = "SEQUELA"
SCOPE_TOXICOLOGIC = "TOXICOLOGIC"
SCOPE_OTHER = "OTHER"
EXCLUSION_SCOPES: tuple[str, ...] = (
    SCOPE_NEOPLASM,
    SCOPE_MENDELIAN,
    SCOPE_SEQUELA,
    SCOPE_TOXICOLOGIC,
)

INFECTIOUS_CATEGORY_RE = re.compile(r"infect", re.IGNORECASE)
INFECTIOUS_CATEGORIES = frozenset({"Viral Disease"})
INFECTIOUS_PARENT_RE = re.compile(
    r"infect|viral|bacteri|helminth|protozo|fung|parasit|rickett|tick[- ]borne"
    r"|arbovir|zoono|mycos|spirochet",
    re.IGNORECASE,
)
# Post-infectious immune sequelae, matched on name and parents. Rule R22 gives
# them their own entry on a host-immune mechanism, so the microbial-entry
# requirements (R25) do not apply to them.
SEQUELA_RE = re.compile(
    r"post-?(infectious|viral|streptococcal|polio)|sequela", re.IGNORECASE
)
MENDELIAN_CATEGORY_RE = re.compile(r"mendelian", re.IGNORECASE)
TOXICOLOGIC_CATEGORY_RE = re.compile(r"toxicolog", re.IGNORECASE)

# The one heuristic: transmission prose naming a vector or a non-human
# reservoir. Advisory, and only ever a prompt to look at rule R26.
VECTOR_OR_RESERVOIR_RE = re.compile(
    r"\bvectors?\b|\bticks?\b|mosquito|\bfleas?\b|\blouse\b|\blice\b|\bmites?\b|sandfl"
    r"|triatom|zoono|rodent|\bbats?\b|\banimals?\b|livestock|cattle|swine|\bpigs?\b"
    r"|poultry|\bbirds?\b|\bdogs?\b|\bsnails?\b|\bcopepods?\b",
    re.IGNORECASE,
)

TAXON_LUMP_MIN_AGENTS = 3

# --- finding classes ---------------------------------------------------------
# Deterministic ones gate under --strict; advisory ones never do; informational
# ones are not findings and are excluded from every count that decides an exit
# code.
MISSING_AGENT = "MISSING_AGENT"
UNBOUND_AGENT = "UNBOUND_AGENT"
MISSING_TRANSMISSION = "MISSING_TRANSMISSION"
ROOT_AS_ENTRY = "ROOT_AS_ENTRY"
DOUBLE_MODELLED = "DOUBLE_MODELLED"
DUPLICATE_ANCHOR = "DUPLICATE_ANCHOR"
PATHOTYPE_COLLAPSE = "PATHOTYPE_COLLAPSE"
DANGLING_POINTER = "DANGLING_POINTER"

TAXON_LUMP = "TAXON_LUMP"
UNBOUND_SUBTYPE = "UNBOUND_SUBTYPE"
UNBOUND_AGENT_STRATUM = "UNBOUND_AGENT_STRATUM"
NO_PROGRESSION = "NO_PROGRESSION"
MISSING_LIFECYCLE = "MISSING_LIFECYCLE"
POINTER_TERM_MISMATCH = "POINTER_TERM_MISMATCH"

POINTER = "POINTER"
LUMP_RECORDED = "LUMP_RECORDED"

DETERMINISTIC_CLASSES: tuple[str, ...] = (
    MISSING_AGENT,
    UNBOUND_AGENT,
    MISSING_TRANSMISSION,
    ROOT_AS_ENTRY,
    DOUBLE_MODELLED,
    DUPLICATE_ANCHOR,
    PATHOTYPE_COLLAPSE,
    DANGLING_POINTER,
)
ADVISORY_CLASSES: tuple[str, ...] = (
    TAXON_LUMP,
    UNBOUND_SUBTYPE,
    UNBOUND_AGENT_STRATUM,
    NO_PROGRESSION,
    MISSING_LIFECYCLE,
    POINTER_TERM_MISMATCH,
)
INFORMATIONAL_CLASSES: tuple[str, ...] = (POINTER, LUMP_RECORDED)
ALL_CLASSES: tuple[str, ...] = (
    DETERMINISTIC_CLASSES + ADVISORY_CLASSES + INFORMATIONAL_CLASSES
)

# Classes computed against the corpus index rather than the entry alone. These
# are what --scope all extends to every entry.
CROSS_ENTRY_CLASSES: frozenset[str] = frozenset({DOUBLE_MODELLED, DUPLICATE_ANCHOR})

# Rule the class enforces, for the summary and the docs.
RULE_FOR_CLASS: dict[str, str] = {
    MISSING_AGENT: "R25",
    UNBOUND_AGENT: "R25/R27",
    MISSING_TRANSMISSION: "R25",
    ROOT_AS_ENTRY: "R2",
    DOUBLE_MODELLED: "R20",
    DUPLICATE_ANCHOR: "R18/R28",
    PATHOTYPE_COLLAPSE: "R15",
    DANGLING_POINTER: "R20",
    TAXON_LUMP: "R7-R9",
    UNBOUND_SUBTYPE: "R12",
    UNBOUND_AGENT_STRATUM: "R12",
    NO_PROGRESSION: "R21",
    MISSING_LIFECYCLE: "R26",
    POINTER_TERM_MISMATCH: "R20",
    POINTER: "R20",
    LUMP_RECORDED: "R9",
}


@dataclass(frozen=True)
class Finding:
    """One (entry, class) case, with the detail a curator needs to act on it."""

    entry: str
    cls: str
    detail: str

    @property
    def deterministic(self) -> bool:
        return self.cls in DETERMINISTIC_CLASSES

    @property
    def informational(self) -> bool:
        return self.cls in INFORMATIONAL_CLASSES


@dataclass
class EntryReport:
    """The computed columns for one entry, plus its findings."""

    entry: str
    path: str
    name: str
    scope: str
    mondo_id: str | None
    signal: bool = False
    n_agents: int = 0
    n_agents_bound: int = 0
    n_subtypes: int = 0
    n_subtypes_bound: int = 0
    n_pointers: int = 0
    n_agent_strata: int = 0
    n_agent_strata_bound: int = 0
    has_transmission: bool = False
    has_agent_life_cycle: bool = False
    has_progression: bool = False
    n_phases: int = 0
    lump_recorded: bool = False
    file_lines: int = 0
    findings: list[Finding] = field(default_factory=list)

    @property
    def infectious(self) -> bool:
        return self.scope == SCOPE_INFECTIOUS

    def classes(self, *, include_informational: bool = False) -> list[str]:
        seen: list[str] = []
        for f in self.findings:
            if f.informational and not include_informational:
                continue
            if f.cls not in seen:
                seen.append(f.cls)
        return seen

    @property
    def deterministic_count(self) -> int:
        return sum(1 for f in self.findings if f.deterministic)

    @property
    def advisory_count(self) -> int:
        return sum(
            1 for f in self.findings if not f.deterministic and not f.informational
        )


# --------------------------------------------------------------------------
# Reading the YAML
# --------------------------------------------------------------------------


def _term_id(descriptor: object) -> str | None:
    """The CURIE inside a ``{preferred_term, term: {id, label}}`` descriptor."""
    if not isinstance(descriptor, dict):
        return None
    term = descriptor.get("term")
    if not isinstance(term, dict):
        return None
    value = term.get("id")
    return value if isinstance(value, str) and value else None


def _term_label(descriptor: object) -> str:
    if not isinstance(descriptor, dict):
        return ""
    term = descriptor.get("term")
    if not isinstance(term, dict):
        return ""
    label = term.get("label")
    return label if isinstance(label, str) else ""


def _as_list(value: object) -> list:
    return value if isinstance(value, list) else []


def _as_dicts(value: object) -> list[dict]:
    return [item for item in _as_list(value) if isinstance(item, dict)]


def _strings(value: object) -> list[str]:
    return [item for item in _as_list(value) if isinstance(item, str)]


def normalise_name(name: object) -> str:
    """Case- and punctuation-insensitive key for matching a subtype name to an entry name."""
    if not isinstance(name, str):
        return ""
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def scope_of(doc: dict) -> str:
    """Which ladder governs this entry. Only :data:`SCOPE_INFECTIOUS` is assessed.

    Order matters and follows the ladder's own exclusions: a neoplasm is a
    neoplasm whatever pathogen it names (R23); a Mendelian susceptibility
    disorder or a mycotoxicosis is not an infection whatever its ``parents``
    say; a sequela keeps its own entry on a host-immune mechanism (R22). Only
    then does an infectious ``category``, a pathogen block, or an infectious
    ``parents`` value put the entry in scope.
    """
    name = doc.get("name") if isinstance(doc.get("name"), str) else ""
    category = doc.get("category") if isinstance(doc.get("category"), str) else ""
    parents = _strings(doc.get("parents"))
    categories = _strings(doc.get("categories"))
    classifications = doc.get("classifications")
    has_icdo = isinstance(classifications, dict) and bool(
        classifications.get("icdo_morphology")
    )
    haystack = " | ".join(
        [name, *categories, *parents, _term_label(doc.get("disease_term"))]
    )
    if (NEOPLASM_RE.search(haystack) or has_icdo) and not NOT_NEOPLASM_RE.search(
        haystack
    ):
        return SCOPE_NEOPLASM
    if MENDELIAN_CATEGORY_RE.search(category):
        return SCOPE_MENDELIAN
    if TOXICOLOGIC_CATEGORY_RE.search(category):
        return SCOPE_TOXICOLOGIC
    if SEQUELA_RE.search(name) or any(SEQUELA_RE.search(p) for p in parents):
        return SCOPE_SEQUELA
    if category in INFECTIOUS_CATEGORIES or INFECTIOUS_CATEGORY_RE.search(category):
        return SCOPE_INFECTIOUS
    if _as_dicts(doc.get("infectious_agent")):
        return SCOPE_INFECTIOUS
    if any(INFECTIOUS_PARENT_RE.search(p) for p in parents):
        return SCOPE_INFECTIOUS
    return SCOPE_OTHER


def has_infectious_signal(doc: dict) -> bool:
    """Whether anything on the entry would put it in scope before the exclusions."""
    category = doc.get("category") if isinstance(doc.get("category"), str) else ""
    if category in INFECTIOUS_CATEGORIES or INFECTIOUS_CATEGORY_RE.search(category):
        return True
    if _as_dicts(doc.get("infectious_agent")):
        return True
    return any(INFECTIOUS_PARENT_RE.search(p) for p in _strings(doc.get("parents")))


def is_infectious(doc: dict) -> bool:
    return scope_of(doc) == SCOPE_INFECTIOUS


def lump_waiver_recorded(review_notes: object) -> bool:
    """Whether ``review_notes`` records a deliberate lump the way rule R9 asks.

    A paragraph must *begin* with :data:`LUMP_WAIVER_SENTINEL` and carry at
    least :data:`LUMP_WAIVER_MIN_WORDS` words of reasoning after it -- which
    strata were kept together, what was searched, and why it came up empty.
    The sentinel alone does not waive.
    """
    if not isinstance(review_notes, str):
        return False
    for paragraph in re.split(r"\n\s*\n", review_notes):
        stripped = paragraph.strip()
        if not stripped.startswith(LUMP_WAIVER_SENTINEL):
            continue
        rest = stripped[len(LUMP_WAIVER_SENTINEL) :]
        if len(rest.split()) >= LUMP_WAIVER_MIN_WORDS:
            return True
    return False


def _narrow_match_targets(doc: dict) -> set[str]:
    """MONDO CURIEs this entry maps to with ``skos:narrowMatch`` (the §3a anchor)."""
    mappings = doc.get("mappings")
    if not isinstance(mappings, dict):
        return set()
    out: set[str] = set()
    for m in _as_dicts(mappings.get("mondo_mappings")):
        if m.get("mapping_predicate") == "skos:narrowMatch":
            term_id = _term_id(m)
            if term_id:
                out.add(term_id)
    return out


# --------------------------------------------------------------------------
# The corpus index
# --------------------------------------------------------------------------


@dataclass
class CorpusIndex:
    """What one entry needs to know about every other entry."""

    slugs: set[str] = field(default_factory=set)
    by_term: dict[str, list[str]] = field(default_factory=dict)
    by_name: dict[str, list[str]] = field(default_factory=dict)
    term_of: dict[str, str | None] = field(default_factory=dict)

    def add(self, slug: str, doc: dict) -> None:
        self.slugs.add(slug)
        term_id = _term_id(doc.get("disease_term"))
        self.term_of[slug] = term_id
        if term_id:
            self.by_term.setdefault(term_id, []).append(slug)
        key = normalise_name(doc.get("name"))
        if key:
            self.by_name.setdefault(key, []).append(slug)


def _entries_in(directory: Path) -> Iterator[Path]:
    yield from (
        path
        for path in sorted(directory.glob("*.yaml"))
        if not path.name.endswith(".history.yaml")
    )


def load_corpus(kb_dir: Path) -> tuple[dict[Path, dict], CorpusIndex]:
    """Parse every entry once and build the cross-entry index from the same parse."""
    docs: dict[Path, dict] = {}
    index = CorpusIndex()
    for path in _entries_in(kb_dir):
        doc = load_document(path)
        if not isinstance(doc, dict):
            continue
        docs[path.resolve()] = doc
        index.add(path.stem, doc)
    return docs, index


# --------------------------------------------------------------------------
# Assessment
# --------------------------------------------------------------------------


def _display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def _count_lines(path: Path) -> int:
    with path.open("rb") as handle:
        return sum(1 for _ in handle)


def _subtype_name(st: dict) -> str:
    return st.get("name") if isinstance(st.get("name"), str) else "?"


def _pointer_target(st: dict) -> str | None:
    target = st.get("curated_in")
    return target if isinstance(target, str) and target else None


def _assess_pointers(
    slug: str, subtypes: list[dict], index: CorpusIndex, report: EntryReport
) -> None:
    """``curated_in`` resolution, on every entry: the slot is KB-wide."""
    for st in subtypes:
        target = _pointer_target(st)
        if target is None:
            continue
        report.n_pointers += 1
        st_name = _subtype_name(st)
        if target not in index.slugs:
            report.findings.append(
                Finding(
                    slug,
                    DANGLING_POINTER,
                    f"subtype {st_name!r} curated_in {target!r}: no kb/disorders/{target}.yaml",
                )
            )
            continue
        report.findings.append(
            Finding(slug, POINTER, f"subtype {st_name!r} -> {target}")
        )
        st_term = _term_id(st.get("subtype_term"))
        target_term = index.term_of.get(target)
        if st_term and target_term and st_term != target_term:
            report.findings.append(
                Finding(
                    slug,
                    POINTER_TERM_MISMATCH,
                    f"subtype {st_name!r} binds {st_term} but {target} is anchored to {target_term}",
                )
            )


def _assess_cross_entry(
    slug: str, doc: dict, subtypes: list[dict], index: CorpusIndex, report: EntryReport
) -> None:
    """Shared anchors and double modelling: the rules §3a and §3e hold in common."""
    mondo_id = report.mondo_id
    if mondo_id:
        others = [s for s in index.by_term.get(mondo_id, []) if s != slug]
        if others and mondo_id not in _narrow_match_targets(doc):
            report.findings.append(
                Finding(
                    slug,
                    DUPLICATE_ANCHOR,
                    f"{mondo_id} is also the disease_term of {', '.join(sorted(others))}; no skos:narrowMatch recorded here",
                )
            )

    for st in subtypes:
        if _pointer_target(st):
            continue
        st_name = _subtype_name(st)
        st_term = _term_id(st.get("subtype_term"))
        hit: str | None = None
        if st_term:
            for other in index.by_term.get(st_term, []):
                if other != slug:
                    hit = f"{other} (same MONDO {st_term})"
                    break
        if hit is None:
            for candidate in (st.get("name"), st.get("display_name")):
                key = normalise_name(candidate)
                others = (
                    [o for o in index.by_name.get(key, []) if o != slug] if key else []
                )
                if others:
                    hit = f"{', '.join(others)} (same name)"
                    break
        if hit:
            report.findings.append(
                Finding(
                    slug,
                    DOUBLE_MODELLED,
                    f"subtype {st_name!r} is also entry {hit}; add curated_in or drop the row",
                )
            )


def assess(
    path: Path, doc: dict, index: CorpusIndex, *, cross_entry_everywhere: bool = False
) -> EntryReport:
    """Compute the columns and findings for one entry against the corpus index."""
    slug = path.stem
    name = doc.get("name") if isinstance(doc.get("name"), str) else slug
    report = EntryReport(
        entry=slug,
        path=_display_path(path),
        name=name,
        scope=scope_of(doc),
        mondo_id=_term_id(doc.get("disease_term")),
        signal=has_infectious_signal(doc),
        file_lines=_count_lines(path) if path.exists() else 0,
    )
    findings = report.findings

    subtypes = _as_dicts(doc.get("has_subtypes"))
    report.n_subtypes = len(subtypes)
    report.n_subtypes_bound = sum(
        1 for st in subtypes if _term_id(st.get("subtype_term"))
    )
    _assess_pointers(slug, subtypes, index, report)

    if report.infectious or cross_entry_everywhere:
        _assess_cross_entry(slug, doc, subtypes, index, report)

    if not report.infectious:
        return report

    # --- deterministic ---------------------------------------------------
    agents = _as_dicts(doc.get("infectious_agent"))
    report.n_agents = len(agents)
    if not agents:
        findings.append(Finding(slug, MISSING_AGENT, "no infectious_agent block"))
    agent_ids: list[str] = []
    for agent in agents:
        agent_name = agent.get("name") if isinstance(agent.get("name"), str) else "?"
        agent_id = _term_id(agent.get("infectious_agent_term"))
        if agent_id:
            report.n_agents_bound += 1
            agent_ids.append(agent_id)
        else:
            findings.append(
                Finding(
                    slug,
                    UNBOUND_AGENT,
                    f"agent {agent_name!r} has no infectious_agent_term",
                )
            )
        strata = _as_dicts(agent.get("has_subtypes"))
        report.n_agent_strata += len(strata)
        for stratum in strata:
            if _term_id(stratum.get("subtype_term")):
                report.n_agent_strata_bound += 1
            else:
                findings.append(
                    Finding(
                        slug,
                        UNBOUND_AGENT_STRATUM,
                        f"agent {agent_name!r} stratum {_subtype_name(stratum)!r} has no subtype_term",
                    )
                )
    seen_ids: dict[str, int] = {}
    for agent_id in agent_ids:
        seen_ids[agent_id] = seen_ids.get(agent_id, 0) + 1
    for agent_id, count in seen_ids.items():
        if count > 1:
            findings.append(
                Finding(
                    slug,
                    PATHOTYPE_COLLAPSE,
                    f"{count} agents bound to {agent_id}; strata below species are structural, not a shared CURIE",
                )
            )

    transmission = _as_dicts(doc.get("transmission"))
    report.has_transmission = bool(transmission)
    if not transmission:
        findings.append(Finding(slug, MISSING_TRANSMISSION, "no transmission block"))

    if report.mondo_id in ROOT_TERMS:
        findings.append(
            Finding(
                slug,
                ROOT_AS_ENTRY,
                f"anchored to {report.mondo_id} '{ROOT_TERMS[report.mondo_id]}' (rung 0)",
            )
        )

    # --- advisory --------------------------------------------------------
    report.lump_recorded = lump_waiver_recorded(doc.get("review_notes"))
    if len(agents) >= TAXON_LUMP_MIN_AGENTS and not subtypes:
        if report.lump_recorded:
            findings.append(
                Finding(
                    slug,
                    LUMP_RECORDED,
                    f"{len(agents)} agents, no subtypes, deliberate lump recorded in review_notes",
                )
            )
        else:
            findings.append(
                Finding(
                    slug,
                    TAXON_LUMP,
                    f"{len(agents)} agents, no subtypes, no decision recorded "
                    "(subtype on one documented axis, or record the lump)",
                )
            )

    for st in subtypes:
        if not _term_id(st.get("subtype_term")):
            findings.append(
                Finding(
                    slug,
                    UNBOUND_SUBTYPE,
                    f"subtype {_subtype_name(st)!r} has no subtype_term",
                )
            )

    progression = _as_dicts(doc.get("progression"))
    report.has_progression = bool(progression)
    report.n_phases = sum(1 for p in progression if p.get("phase"))
    if not progression:
        findings.append(
            Finding(
                slug,
                NO_PROGRESSION,
                "no progression block; list the phases if the disease has them",
            )
        )

    life_cycle = doc.get("agent_life_cycle")
    report.has_agent_life_cycle = isinstance(life_cycle, dict) and bool(life_cycle)
    if not report.has_agent_life_cycle:
        prose = " ".join(
            str(t.get(key))
            for t in transmission
            for key in ("name", "description")
            if isinstance(t.get(key), str)
        )
        match = VECTOR_OR_RESERVOIR_RE.search(prose)
        if match:
            findings.append(
                Finding(
                    slug,
                    MISSING_LIFECYCLE,
                    f"transmission text mentions {match.group(0)!r} but no agent_life_cycle block (heuristic)",
                )
            )

    return report


# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------


def resolve_report_paths(files: list[str]) -> tuple[list[Path] | None, list[str]]:
    """Which entries to *report* on. ``None`` means every entry in the corpus.

    A directory argument expands to its entries; a missing path or an empty
    directory is a usage error, returned as a message rather than raised.
    """
    if not files:
        return None, []
    paths: list[Path] = []
    errors: list[str] = []
    for raw in files:
        path = Path(raw)
        if path.is_dir():
            found = list(_entries_in(path))
            if not found:
                errors.append(f"{raw}: directory holds no entries")
            paths.extend(found)
        elif path.is_file():
            paths.append(path)
        else:
            errors.append(f"{raw}: no such file")
    return paths, errors


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------


def _class_counts(reports: Iterable[EntryReport]) -> dict[str, int]:
    counts = dict.fromkeys(ALL_CLASSES, 0)
    for report in reports:
        for f in report.findings:
            counts[f.cls] += 1
    return counts


def render_summary(
    reports: list[EntryReport], *, limit: int, corpus_size: int, scope_all: bool
) -> None:
    infectious = [r for r in reports if r.infectious]
    counts = _class_counts(reports)
    excluded = {
        scope: sum(1 for r in reports if r.signal and r.scope == scope)
        for scope in EXCLUSION_SCOPES
    }
    print(
        f"Entries walked: {corpus_size}; reported on: {len(reports)}; infectious set: {len(infectious)}"
    )
    print(
        "  in scope: category naming infection, or an infectious_agent block, or a parents value"
        " matching the infectious pattern, minus the exclusions the ladder itself makes"
    )
    print(
        "  pathogen-marked entries excluded: "
        + ", ".join(f"{scope} {n}" for scope, n in excluded.items())
        + (
            "  (cross-entry classes still run on every entry: --scope all)"
            if scope_all
            else ""
        )
    )
    print()
    print("Deterministic (gate under --strict):")
    for cls in DETERMINISTIC_CLASSES:
        print(f"  {cls:<22} {counts[cls]:>5}   {RULE_FOR_CLASS[cls]}")
    print("Advisory (report-only):")
    for cls in ADVISORY_CLASSES:
        print(f"  {cls:<22} {counts[cls]:>5}   {RULE_FOR_CLASS[cls]}")
    print("Informational:")
    for cls in INFORMATIONAL_CLASSES:
        print(f"  {cls:<22} {counts[cls]:>5}   {RULE_FOR_CLASS[cls]}")

    worklist = sorted(
        (r for r in reports if r.deterministic_count),
        key=lambda r: (-r.deterministic_count, r.entry),
    )
    if worklist:
        print()
        print(
            f"Worklist: {len(worklist)} entries with deterministic findings (showing up to {limit})"
        )
        for report in worklist[:limit]:
            classes = ", ".join(
                c for c in report.classes() if c in DETERMINISTIC_CLASSES
            )
            print(f"  {report.entry:<50} {report.deterministic_count:>2}  {classes}")
        if len(worklist) > limit:
            print(
                f"  ... {len(worklist) - limit} more; --format list for every finding"
            )

    lumps = sorted(
        (r for r in infectious if any(f.cls == TAXON_LUMP for f in r.findings)),
        key=lambda r: (-r.n_agents, r.entry),
    )
    if lumps:
        print()
        print(
            f"Undecided lumps ({len(lumps)}): apply the rung-3 gate to each, one at a time"
        )
        for report in lumps[:limit]:
            print(f"  {report.entry:<50} {report.n_agents:>2} agents")


def render_list(reports: list[EntryReport]) -> None:
    for report in sorted(reports, key=lambda r: r.entry):
        for f in report.findings:
            print(f"{report.path}\t{f.cls}\t{f.detail}")


TSV_COLUMNS = (
    "entry",
    "scope",
    "mondo_id",
    "n_agents",
    "n_agents_bound",
    "n_subtypes",
    "n_subtypes_bound",
    "n_pointers",
    "n_agent_strata",
    "n_agent_strata_bound",
    "has_transmission",
    "has_agent_life_cycle",
    "has_progression",
    "n_phases",
    "lump_recorded",
    "file_lines",
    "deterministic",
    "advisory",
)


def _row(report: EntryReport) -> list[str]:
    return [
        report.entry,
        report.scope,
        report.mondo_id or "",
        str(report.n_agents),
        str(report.n_agents_bound),
        str(report.n_subtypes),
        str(report.n_subtypes_bound),
        str(report.n_pointers),
        str(report.n_agent_strata),
        str(report.n_agent_strata_bound),
        str(report.has_transmission).lower(),
        str(report.has_agent_life_cycle).lower(),
        str(report.has_progression).lower(),
        str(report.n_phases),
        str(report.lump_recorded).lower(),
        str(report.file_lines),
        ";".join(c for c in report.classes() if c in DETERMINISTIC_CLASSES),
        ";".join(c for c in report.classes() if c in ADVISORY_CLASSES),
    ]


def _rows_worth_printing(reports: list[EntryReport]) -> list[EntryReport]:
    return [
        r for r in sorted(reports, key=lambda r: r.entry) if r.infectious or r.findings
    ]


def render_tsv(reports: list[EntryReport]) -> None:
    print("\t".join(TSV_COLUMNS))
    for report in _rows_worth_printing(reports):
        print("\t".join(_row(report)))


def render_json(reports: list[EntryReport]) -> None:
    payload = []
    for report in _rows_worth_printing(reports):
        record = dict(zip(TSV_COLUMNS, _row(report), strict=True))
        record["findings"] = [
            {"class": f.cls, "detail": f.detail} for f in report.findings
        ]
        payload.append(record)
    print(json.dumps(payload, indent=2))


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    kb_cache.default_off()

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "files",
        nargs="*",
        help="entries to report on (default: every entry in --kb-dir)",
    )
    parser.add_argument(
        "--kb-dir",
        default=DEFAULT_KB_DIR,
        help="corpus to index (default: %(default)s)",
    )
    parser.add_argument(
        "--format", choices=("summary", "list", "tsv", "json"), default="summary"
    )
    parser.add_argument(
        "--scope",
        choices=("infectious", "all"),
        default="infectious",
        help="run the cross-entry classes (DOUBLE_MODELLED, DUPLICATE_ANCHOR) on infectious entries only, "
        "or on every entry (default: %(default)s)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=40,
        help="rows in the summary worklists (default: %(default)s)",
    )
    parser.add_argument(
        "--strict", action="store_true", help="exit 1 on any deterministic finding"
    )
    parser.add_argument(
        "--fail-on",
        action="append",
        default=[],
        metavar="CLASS",
        help="exit 1 if this class has any finding (repeatable; any class, including advisory)",
    )
    args = parser.parse_args(argv)

    unknown = [c for c in args.fail_on if c not in ALL_CLASSES]
    if unknown:
        parser.error(
            f"unknown class for --fail-on: {', '.join(unknown)} (choose from {', '.join(ALL_CLASSES)})"
        )

    kb_dir = Path(args.kb_dir)
    if not kb_dir.is_dir():
        print(f"error: {kb_dir} is not a directory", file=sys.stderr)
        return 2
    docs, index = load_corpus(kb_dir)
    if not docs:
        print(f"error: {kb_dir} holds no entries", file=sys.stderr)
        return 2

    report_paths, errors = resolve_report_paths(args.files)
    if errors:
        for message in errors:
            print(f"error: {message}", file=sys.stderr)
        return 2

    everywhere = args.scope == "all"
    reports: list[EntryReport] = []
    if report_paths is None:
        for path, doc in docs.items():
            reports.append(assess(path, doc, index, cross_entry_everywhere=everywhere))
    else:
        for path in report_paths:
            doc = docs.get(path.resolve())
            if doc is None:
                # A file outside --kb-dir: parse it on its own, and index it so
                # its own name and term do not read as collisions with itself.
                doc = load_document(path)
                if not isinstance(doc, dict):
                    print(f"error: {path}: not a mapping", file=sys.stderr)
                    return 2
                if path.stem not in index.slugs:
                    index.add(path.stem, doc)
            reports.append(assess(path, doc, index, cross_entry_everywhere=everywhere))

    if args.format == "summary":
        render_summary(
            reports, limit=args.limit, corpus_size=len(docs), scope_all=everywhere
        )
    elif args.format == "list":
        render_list(reports)
    elif args.format == "tsv":
        render_tsv(reports)
    else:
        render_json(reports)

    failed = False
    if args.strict and any(r.deterministic_count for r in reports):
        failed = True
    if args.fail_on:
        wanted = set(args.fail_on)
        if any(f.cls in wanted for r in reports for f in r.findings):
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
