"""Structural linting and membership evaluation for disease groupings.

A grouping (``kb/groupings/*.yaml``, validating against the ``Grouping`` class)
carries one or more ``membership_criteria`` blocks. Each block holds an optional
nested boolean ``logic`` expression built from ``LogicalCriterion`` nodes, plus a
``criteria_semantics`` marker recording the OWL-style direction relating the
criteria to membership:

- ``NECESSARY``   (member => criteria): audit listed members for violations.
- ``SUFFICIENT``  (criteria => member): classify non-members as candidates.
- ``NECESSARY_AND_SUFFICIENT`` (member <=> criteria): both.

This module provides two tiers of tooling:

1. **Structural lint** (:func:`lint_criterion`) — classifies every node as a
   BRANCH or LEAF and checks well-formedness (operator<->operands,
   predicate<->payload, ``NOT`` arity). This is cheap, deterministic, and is
   enforced as a hard check in the test suite.

2. **Membership evaluation** (:func:`evaluate_grouping`) — three-valued
   evaluation of a criteria expression against a member's parsed disease entry,
   returning SATISFIED / NOT_SATISFIED / UNKNOWN per leaf and per branch.
   Term-valued leaves (HP, GO) are evaluated over the ontology's subsumption
   closure, so a member annotated with a descendant of the criterion term
   satisfies it (see :func:`term_closure`). This is advisory: criteria are often
   aspirational (a member may not yet declare a ``conforms_to`` edge the
   criteria require), so the CLI reports rather than gates.

   A NOT_SATISFIED result for a listed member under NECESSARY criteria is
   reported as such, without interpretation. It is a contradiction between two
   curated assertions — "D is a member of G" and "members of G satisfy C" — and
   resolving it may mean annotating the entry, loosening the criteria, or
   dropping the member. The tooling surfaces it; the curator decides which.

3. **Overlap reporting** (:func:`compute_grouping_overlaps`) — all-vs-all
   comparison of grouping disease-member sets, expanding nested ``GROUPING``
   members to concrete disease entries.

4. **Nesting reporting** (:func:`compute_nesting_report`) — the declared
   grouping-of-grouping forest (``member_type: GROUPING`` members) next to the
   *undeclared* containments: pairs where every expanded disease member of one
   grouping is also a member of another that does not list it as nested. A
   containment is a lead, not a ruling — two groupings can deliberately cut the
   same diseases along different axes (a shared organelle versus a shared
   malformation), and the report says so rather than gating.
"""

from __future__ import annotations

import argparse
import glob
from collections.abc import Iterable
from dataclasses import dataclass, field
from enum import Enum
from functools import cache
from pathlib import Path
from typing import Any

from dismech.yaml_io import safe_load

ROOT_DIR = Path(__file__).resolve().parents[2]
DISORDERS_DIR = ROOT_DIR / "kb" / "disorders"
MODULES_DIR = ROOT_DIR / "kb" / "modules"
GROUPINGS_DIR = ROOT_DIR / "kb" / "groupings"

BRANCH_OPERATORS = {"AND", "OR", "NOT"}

# Free-text nosology slots folded into a disease's classification tags,
# alongside the structured `classifications:` block. Shared so the advisory in
# lint_criterion_advisories() names exactly the slots _classification_tags()
# reads, and the two cannot drift apart.
FREE_TEXT_TAG_SLOTS = ("parents", "categories")

# Map each leaf predicate to the payload slot(s) it requires. ``None`` means the
# constraint is carried in free text (``description``) and has no structured
# payload to evaluate.
#
# HAS_INHERITANCE is listed as ``None`` because its payload is OPTIONAL, not
# absent: a leaf carrying an ``inheritance_term`` is evaluated against the
# member's curated inheritance blocks, while a leaf carrying only a
# ``description`` (e.g. "hereditary, i.e. germline rather than acquired", which
# no single HPO term names) stays free text and evaluates to UNKNOWN. Requiring
# the payload here would invalidate the latter, which is a legitimate use.
PREDICATE_PAYLOAD = {
    "HAS_PHENOTYPE": "phenotype_term",
    "HAS_GENE": "gene",
    "CONFORMS_TO_MODULE": "module",
    "HAS_BIOLOGICAL_PROCESS": "biological_processes",
    "HAS_CLASSIFICATION": "classification",
    "HAS_INHERITANCE": None,
    "HAS_MAPPING": None,
    "OTHER": None,
}

# Frequency bands, strongest first. Used for ``min_frequency`` (">=") checks.
FREQUENCY_ORDER = [
    "OBLIGATE",
    "VERY_FREQUENT",
    "FREQUENT",
    "OCCASIONAL",
    "VERY_RARE",
]
FREQUENCY_RANK = {name: i for i, name in enumerate(FREQUENCY_ORDER)}


class NodeKind(str, Enum):
    BRANCH = "BRANCH"
    LEAF = "LEAF"
    INVALID = "INVALID"


class Satisfaction(str, Enum):
    SATISFIED = "SATISFIED"
    NOT_SATISFIED = "NOT_SATISFIED"
    UNKNOWN = "UNKNOWN"

    def negate(self) -> Satisfaction:
        if self is Satisfaction.SATISFIED:
            return Satisfaction.NOT_SATISFIED
        if self is Satisfaction.NOT_SATISFIED:
            return Satisfaction.SATISFIED
        return Satisfaction.UNKNOWN


# --------------------------------------------------------------------------- #
# Node classification + structural lint (Tier 1)
# --------------------------------------------------------------------------- #


def classify_node(node: Any) -> NodeKind:
    """Classify a LogicalCriterion node as a BRANCH, LEAF, or INVALID.

    A BRANCH sets ``operator``; a LEAF sets ``criterion_predicate``. A node that
    sets both, or neither, is INVALID.
    """
    if not isinstance(node, dict):
        return NodeKind.INVALID
    has_operator = node.get("operator") is not None
    has_predicate = node.get("criterion_predicate") is not None
    if has_operator and not has_predicate:
        return NodeKind.BRANCH
    if has_predicate and not has_operator:
        return NodeKind.LEAF
    return NodeKind.INVALID


def lint_criterion(node: Any, path: str = "logic") -> list[str]:
    """Return a list of structural errors for a (possibly nested) expression.

    An empty list means the expression is well-formed.
    """
    errors: list[str] = []
    if node is None:
        return errors  # logic is optional
    if not isinstance(node, dict):
        return [f"{path}: node is not a mapping ({type(node).__name__})"]

    kind = classify_node(node)
    if kind is NodeKind.INVALID:
        if node.get("operator") and node.get("criterion_predicate"):
            errors.append(f"{path}: node sets both operator and criterion_predicate")
        else:
            errors.append(f"{path}: node sets neither operator nor criterion_predicate")
        return errors

    if kind is NodeKind.BRANCH:
        operator = node["operator"]
        if operator not in BRANCH_OPERATORS:
            errors.append(f"{path}: unknown operator {operator!r}")
        operands = node.get("operands") or []
        if not operands:
            errors.append(f"{path}: branch node {operator!r} has no operands")
        if node.get("operands") is not None and not isinstance(node["operands"], list):
            errors.append(f"{path}: operands must be a list")
            operands = []
        for i, child in enumerate(operands):
            errors.extend(lint_criterion(child, f"{path}.operands[{i}]"))
    else:  # LEAF
        predicate = node["criterion_predicate"]
        if predicate not in PREDICATE_PAYLOAD:
            errors.append(f"{path}: unknown criterion_predicate {predicate!r}")
        else:
            required = PREDICATE_PAYLOAD[predicate]
            if required and node.get(required) is None:
                errors.append(f"{path}: predicate {predicate} requires '{required}'")
        if node.get("operands"):
            errors.append(f"{path}: leaf node must not have operands")
    return errors


def lint_criterion_advisories(
    node: Any, path: str = "logic", negated_context: bool = False
) -> list[str]:
    """Return non-gating style advisories for a criteria expression.

    Distinct from :func:`lint_criterion`, whose findings are structural errors
    and gate CI. These are conventions worth steering toward but which existing
    curated groupings legitimately do not follow, so flagging them as errors
    would turn correct files red.

    Currently one advisory: a positive ``HAS_CLASSIFICATION`` leaf whose value
    carries no ``<slot>:`` prefix. ``_classification_tags()`` also emits
    bare-value tags and folds in the free-text ``parents:``/``categories:``
    slots, so a bare value matches a tag in *any* slot -- fine when the tag is
    unique KB-wide (as for ``RASopathy``), but a latent false positive when two
    nosology schemes share a string. The keyed form pins the slot.

    Negated leaves are deliberately exempt. For an exclusion the slot-agnostic
    reading is the *stronger* one -- "not classified there, whichever slot says
    so" -- and keying it would narrow the exclusion, admitting a member tagged
    under a different slot. Advising the keyed form there would be backwards.

    The schema offers two ways to negate, and the exemption covers both: a leaf
    marked ``negated: true``, and a leaf sitting under an ``operator: NOT``
    branch. ``negated_context`` carries the second down the recursion, flipping
    at each NOT so a doubly-negated leaf is treated as positive again. No KB
    grouping uses the NOT-operator form today, so this closes a latent
    inconsistency rather than a live false positive.
    """
    advisories: list[str] = []
    if not isinstance(node, dict):
        return advisories
    excluded = bool(node.get("negated")) ^ negated_context
    if (
        classify_node(node) is NodeKind.LEAF
        and node.get("criterion_predicate") == "HAS_CLASSIFICATION"
        and not excluded
    ):
        value = node.get("classification")
        if isinstance(value, str) and ":" not in value:
            # Name the slots the extractor actually reads, so the advice is
            # actionable without the curator going to look them up. The
            # structured `classifications:` keys vary per entry, so those are
            # described rather than enumerated.
            slots = " or ".join(f"'{slot}:{value}'" for slot in FREE_TEXT_TAG_SLOTS)
            advisories.append(
                f"{path}: HAS_CLASSIFICATION {value!r} is unkeyed, so it matches "
                f"that tag in any slot; prefer {slots}, or "
                f"'<classifications-key>:{value}' (e.g. "
                f"'iuis_category:{value}'), to pin which slot it reads"
            )
    child_context = negated_context ^ (node.get("operator") == "NOT")
    for i, child in enumerate(node.get("operands", []) or []):
        advisories.extend(
            lint_criterion_advisories(child, f"{path}.operands[{i}]", child_context)
        )
    return advisories


def iter_nodes(node: Any) -> Iterable[dict]:
    """Yield every node in a (possibly nested) criteria expression."""
    if not isinstance(node, dict):
        return
    yield node
    for child in node.get("operands", []) or []:
        yield from iter_nodes(child)


# --------------------------------------------------------------------------- #
# Ontology closure
# --------------------------------------------------------------------------- #
#
# A criteria leaf asserting "has P" is satisfied by a member annotated with any
# is_a/part_of DESCENDANT of P, not only by P itself. Without this a grouping
# whose criteria cite high-level anatomical terms reads as violated by every
# member that curated a more specific child term.
#
# The closure is computed over the criteria terms (a small, bounded set: ~90
# distinct terms across all of kb/groupings/) rather than over the far larger
# set of curated disease terms, and is cached per term.

# Prefixes whose subsumption hierarchy is meaningful for membership criteria.
# HGNC is deliberately excluded: its "hierarchy" is gene-group membership, not
# subsumption, so a gene criterion stays an exact match.
CLOSURE_PREFIXES = {"HP", "GO"}

OAK_CONFIG_PATH = ROOT_DIR / "conf" / "oak_config.yaml"

# Fallback adapters if conf/oak_config.yaml is unreadable.
_DEFAULT_ADAPTERS = {"HP": "sqlite:obo:hp", "GO": "ols:go"}

_closure_enabled = True


def set_closure_enabled(enabled: bool) -> None:
    """Enable/disable ontology closure in leaf evaluation (for offline runs).

    Clears the closure cache so a toggle cannot return results computed under
    the previous setting.
    """
    global _closure_enabled
    if enabled != _closure_enabled:
        term_closure.cache_clear()
    _closure_enabled = enabled


@cache
def _adapter_for_prefix(prefix: str) -> str | None:
    """Resolve an ontology prefix to an OAK adapter string via oak_config.yaml."""
    adapters = dict(_DEFAULT_ADAPTERS)
    try:
        with open(OAK_CONFIG_PATH) as f:
            conf = safe_load(f) or {}
        configured = conf.get("ontology_adapters") or {}
        if isinstance(configured, dict):
            adapters.update(
                {k: v for k, v in configured.items() if isinstance(v, str) and v}
            )
    except Exception:
        pass
    return adapters.get(prefix)


@cache
def _get_oak_adapter(adapter_str: str):
    try:
        from oaklib import get_adapter
    except Exception:
        return None
    try:
        return get_adapter(adapter_str)
    except Exception:
        return None


@cache
def term_closure(term_id: str) -> frozenset[str]:
    """Return ``term_id`` plus its is_a/part_of descendants.

    Degrades to ``{term_id}`` (exact-match semantics) when closure is disabled,
    the prefix has no meaningful subsumption hierarchy, or the ontology is
    unreachable — so an offline run under-reports satisfaction rather than
    failing.
    """
    if not isinstance(term_id, str) or ":" not in term_id:
        return frozenset()
    prefix = term_id.split(":", 1)[0]
    if not _closure_enabled or prefix not in CLOSURE_PREFIXES:
        return frozenset({term_id})
    adapter_str = _adapter_for_prefix(prefix)
    if not adapter_str:
        return frozenset({term_id})
    adapter = _get_oak_adapter(adapter_str)
    if adapter is None:
        return frozenset({term_id})
    try:
        from oaklib.datamodels.vocabulary import IS_A, PART_OF

        descendants = {
            d
            for d in adapter.descendants([term_id], predicates=[IS_A, PART_OF])
            if isinstance(d, str) and d.startswith(f"{prefix}:")
        }
    except Exception:
        return frozenset({term_id})
    return frozenset(descendants | {term_id})


# --------------------------------------------------------------------------- #
# Disease entry indexing (for Tier 2 evaluation)
# --------------------------------------------------------------------------- #


@dataclass
class DiseaseFacts:
    """Flattened, queryable facts extracted from one disease entry."""

    name: str
    gene_ids: set[str] = field(default_factory=set)
    go_ids: set[str] = field(default_factory=set)
    module_stems: set[str] = field(default_factory=set)
    # HP mode-of-inheritance ids from curated `inheritance_term` blocks. Kept
    # separate from `phenotype_freq` because an inheritance term is a statement
    # about the entry's genetic architecture, not a phenotype it manifests.
    inheritance_ids: set[str] = field(default_factory=set)
    # HP id -> best (strongest) known frequency band, if any.
    phenotype_freq: dict[str, str | None] = field(default_factory=dict)
    # Normalized nosology/classification tags this disease carries. Holds both
    # the bare value ("combined immunodeficiency") and the keyed form
    # ("iuis_category:combined immunodeficiency") so a criterion may cite
    # either. See _classification_tags().
    classification_tags: set[str] = field(default_factory=set)


def _walk(obj: Any) -> Iterable[Any]:
    """Recursively yield every mapping and list element in a nested structure."""
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from _walk(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _walk(v)


def _norm_tag(value: str) -> str:
    """Normalize a classification tag for comparison (case/whitespace-insensitive)."""
    return " ".join(value.lower().split())


def _classification_tags(data: dict) -> set[str]:
    """Collect the nosology tags a disease entry carries.

    DisMech has no single canonical nosology slot, so three slots count:

    * the structured ``classifications:`` block — every
      ``<key>.classification_value``, contributed both bare and as
      ``<key>:<value>`` so a criterion can disambiguate when the same string
      appears under two schemes;
    * the free-text ``parents:`` and ``categories:`` lists, which is where
      tags such as ``RASopathy`` live.

    Plural/singular is not normalized away: a criterion citing ``RASopathy``
    does not match an entry tagged ``RASopathies``. Keeping the match literal
    means a normalization drift shows up as UNKNOWN/NOT_SATISFIED in the audit
    rather than being silently papered over.
    """
    tags: set[str] = set()

    classifications = data.get("classifications")
    if isinstance(classifications, dict):
        for key, assignment in classifications.items():
            items = assignment if isinstance(assignment, list) else [assignment]
            for item in items:
                if not isinstance(item, dict):
                    continue
                value = item.get("classification_value")
                if isinstance(value, str) and value.strip():
                    tags.add(_norm_tag(value))
                    tags.add(f"{_norm_tag(str(key))}:{_norm_tag(value)}")

    for slot in FREE_TEXT_TAG_SLOTS:
        values = data.get(slot)
        if isinstance(values, str):
            values = [values]
        if isinstance(values, list):
            for value in values:
                if isinstance(value, str) and value.strip():
                    tags.add(_norm_tag(value))
                    tags.add(f"{_norm_tag(slot)}:{_norm_tag(value)}")

    return tags


def extract_disease_facts(name: str, data: dict) -> DiseaseFacts:
    """Extract genes, GO terms, module conformance, phenotypes, classifications."""
    facts = DiseaseFacts(name=name)
    facts.classification_tags = _classification_tags(data)

    for node in _walk(data):
        if not isinstance(node, dict):
            continue

        # conforms_to lives on pathophysiology nodes; collect the module stems.
        conforms = node.get("conforms_to")
        if isinstance(conforms, str) and conforms:
            facts.module_stems.add(conforms.split("#", 1)[0].strip())

        # Any term with an id contributes to the appropriate id set.
        term = node.get("term")
        if isinstance(term, dict) and isinstance(term.get("id"), str):
            tid = term["id"]
            if tid.lower().startswith("hgnc:"):
                facts.gene_ids.add(tid.lower())
            elif tid.startswith("GO:"):
                facts.go_ids.add(tid)

        # Inheritance: capture the HPO mode-of-inheritance id. The walk reaches
        # every `inheritance` block in the entry - disease level, has_subtypes,
        # and the per-gene blocks under `genetic` - which is what the criteria
        # mean: a disorder qualifies if ANY curated branch of it does. The
        # gene-level path is deliberate and pinned by a test; no entry uses it
        # for a multi-locus term today, but a per-gene digenic assertion is a
        # reasonable place to make one and must not be silently ignored.
        it = node.get("inheritance_term")
        if isinstance(it, dict):
            iterm = it.get("term") or {}
            ihp = iterm.get("id") if isinstance(iterm, dict) else None
            if isinstance(ihp, str) and ihp.startswith("HP:"):
                facts.inheritance_ids.add(ihp)

        # Phenotypes: capture HP id + (strongest) frequency band.
        pt = node.get("phenotype_term")
        if isinstance(pt, dict):
            pterm = pt.get("term") or {}
            hp = pterm.get("id") if isinstance(pterm, dict) else None
            if isinstance(hp, str) and hp.startswith("HP:"):
                facts.phenotype_freq[hp] = _stronger_freq(
                    facts.phenotype_freq.get(hp), node.get("frequency")
                )
    return facts


def _stronger_freq(a: str | None, b: str | None) -> str | None:
    """Return the stronger (higher-frequency) of two frequency bands."""
    ranks = [f for f in (a, b) if f in FREQUENCY_RANK]
    if not ranks:
        return a or b
    return min(ranks, key=lambda f: FREQUENCY_RANK[f])


@cache
def load_disease_index(
    disorders_dir: Path = DISORDERS_DIR,
) -> dict[str, DiseaseFacts]:
    """Build a name -> DiseaseFacts index over kb/disorders/ (cached)."""
    index: dict[str, DiseaseFacts] = {}
    for fp in glob.glob(str(disorders_dir / "*.yaml")):
        if fp.endswith(".history.yaml"):
            continue
        with open(fp) as f:
            data = safe_load(f)
        if isinstance(data, dict) and data.get("name"):
            index[data["name"]] = extract_disease_facts(data["name"], data)
    return index


# --------------------------------------------------------------------------- #
# Membership evaluation (Tier 2)
# --------------------------------------------------------------------------- #


def _eval_leaf(node: dict, facts: DiseaseFacts) -> Satisfaction:
    predicate = node.get("criterion_predicate")
    result = Satisfaction.UNKNOWN

    if predicate == "HAS_GENE":
        gid = _term_id(node.get("gene"))
        if gid:
            result = (
                Satisfaction.SATISFIED
                if gid.lower() in facts.gene_ids
                else Satisfaction.NOT_SATISFIED
            )
    elif predicate == "HAS_BIOLOGICAL_PROCESS":
        ids = _term_ids(node.get("biological_processes"))
        if ids:
            closure: set[str] = set()
            for gid in ids:
                closure |= term_closure(gid)
            result = (
                Satisfaction.SATISFIED
                if closure & facts.go_ids
                else Satisfaction.NOT_SATISFIED
            )
    elif predicate == "CONFORMS_TO_MODULE":
        ref = node.get("module")
        if ref:
            stem = ref.split("#", 1)[0].strip()
            result = (
                Satisfaction.SATISFIED
                if stem in facts.module_stems
                else Satisfaction.NOT_SATISFIED
            )
    elif predicate == "HAS_INHERITANCE":
        # Optional payload: only a leaf that names a term can be checked.
        hp = _term_id(node.get("inheritance_term"))
        if hp:
            # Closure, as for HAS_PHENOTYPE: a member curating a descendant of
            # the criterion term satisfies it. Note the three non-Mendelian
            # modes are HPO SIBLINGS under HP:0001426, so digenic does not
            # subsume oligogenic (or vice versa) - a grouping that means either
            # must say so with an OR, as Digenic_and_Oligogenic_Disorders does.
            result = (
                Satisfaction.SATISFIED
                if term_closure(hp) & facts.inheritance_ids
                else Satisfaction.NOT_SATISFIED
            )
    elif predicate == "HAS_PHENOTYPE":
        hp = _term_id(node.get("phenotype_term"))
        if hp:
            # A member annotated with any descendant of the criterion term
            # satisfies the criterion (e.g. HP:0007354 amyotrophic lateral
            # sclerosis satisfies HP:0007373 motor neuron atrophy).
            matched = term_closure(hp) & set(facts.phenotype_freq)
            if not matched:
                result = Satisfaction.NOT_SATISFIED
            else:
                min_freq = node.get("min_frequency")
                # Judge against the strongest frequency across matching terms.
                have: str | None = None
                for term_id in matched:
                    have = _stronger_freq(have, facts.phenotype_freq[term_id])
                if not min_freq:
                    result = Satisfaction.SATISFIED
                elif have is None or have not in FREQUENCY_RANK:
                    # Phenotype present but frequency unrecorded -> can't compare.
                    result = Satisfaction.UNKNOWN
                else:
                    result = (
                        Satisfaction.SATISFIED
                        if FREQUENCY_RANK[have] <= FREQUENCY_RANK[min_freq]
                        else Satisfaction.NOT_SATISFIED
                    )
    elif predicate == "HAS_CLASSIFICATION":
        wanted = node.get("classification")
        if isinstance(wanted, str) and wanted.strip():
            result = (
                Satisfaction.SATISFIED
                if _norm_tag(wanted) in facts.classification_tags
                else Satisfaction.NOT_SATISFIED
            )
    # HAS_MAPPING / OTHER, and any payload-less HAS_INHERITANCE leaf -> UNKNOWN.

    if node.get("negated"):
        result = result.negate()
    return result


def _eval_node(node: dict, facts: DiseaseFacts) -> Satisfaction:
    kind = classify_node(node)
    if kind is NodeKind.LEAF:
        return _eval_leaf(node, facts)
    if kind is NodeKind.INVALID:
        return Satisfaction.UNKNOWN

    operator = node["operator"]
    child_results = [_eval_node(c, facts) for c in node.get("operands", []) or []]

    if operator == "NOT":
        # NOT over the conjunction of its operands.
        inner = _combine_and(child_results)
        return inner.negate()
    if operator == "AND":
        return _combine_and(child_results)
    if operator == "OR":
        return _combine_or(child_results)
    return Satisfaction.UNKNOWN


def _combine_and(results: list[Satisfaction]) -> Satisfaction:
    if not results:
        return Satisfaction.UNKNOWN
    if any(r is Satisfaction.NOT_SATISFIED for r in results):
        return Satisfaction.NOT_SATISFIED
    if any(r is Satisfaction.UNKNOWN for r in results):
        return Satisfaction.UNKNOWN
    return Satisfaction.SATISFIED


def _combine_or(results: list[Satisfaction]) -> Satisfaction:
    if not results:
        return Satisfaction.UNKNOWN
    if any(r is Satisfaction.SATISFIED for r in results):
        return Satisfaction.SATISFIED
    if any(r is Satisfaction.UNKNOWN for r in results):
        return Satisfaction.UNKNOWN
    return Satisfaction.NOT_SATISFIED


def _term_id(descriptor: Any) -> str | None:
    if isinstance(descriptor, dict):
        term = descriptor.get("term")
        if isinstance(term, dict):
            return term.get("id")
    return None


def _term_ids(descriptors: Any) -> set[str]:
    ids: set[str] = set()
    for d in descriptors or []:
        tid = _term_id(d)
        if tid:
            ids.add(tid)
    return ids


@dataclass
class MemberEvaluation:
    member: str
    member_type: str
    criteria_index: int
    semantics: str | None
    result: Satisfaction
    leaves: list[tuple[str, Satisfaction]]  # (leaf description, result)
    #: Name of the nested ``member_type: GROUPING`` member through which this
    #: disease belongs to the grouping; ``None`` for a directly listed member.
    via: str | None = None


def _default_groupings_by_name() -> dict[str, dict]:
    return load_groupings_by_name(sorted(glob.glob(str(GROUPINGS_DIR / "*.yaml"))))


def iter_disease_targets(
    grouping: dict,
    groupings_by_name: dict[str, dict] | None = None,
    *,
    _stack: tuple[str, ...] = (),
) -> Iterable[tuple[str, str, str | None]]:
    """Yield ``(disease_name, member_type, via)`` for every disease a grouping
    holds, directly or through nested ``GROUPING`` members.

    ``via`` names the *immediate* nested grouping the disease is reached
    through (``None`` for a direct member), so a parent page can say "member
    via Mucopolysaccharidoses" rather than "not listed". A disease reachable
    more than once is yielded once, direct membership winning. Nesting cycles
    are cut rather than raised: the tree renderer flags them.
    """
    name = str(grouping.get("name") or "<anonymous>")
    members = grouping.get("members", []) or []
    nested_refs = [
        str(m.get("member"))
        for m in members
        if m.get("member") and m.get("member_type") == "GROUPING"
    ]
    if nested_refs and groupings_by_name is None:
        groupings_by_name = _default_groupings_by_name()

    seen: set[str] = set()
    for member in members:
        ref = member.get("member")
        mtype = member.get("member_type", "DISEASE")
        if ref and mtype in ("DISEASE", "SUBTYPE") and ref not in seen:
            seen.add(ref)
            yield ref, mtype, None
    for ref in nested_refs:
        nested = (groupings_by_name or {}).get(ref)
        if nested is None or ref in _stack or ref == name:
            continue
        for disease, mtype, _via in iter_disease_targets(
            nested, groupings_by_name, _stack=(*_stack, name)
        ):
            if disease not in seen:
                seen.add(disease)
                yield disease, mtype, ref


def nested_disease_members(
    grouping: dict, groupings_by_name: dict[str, dict] | None = None
) -> dict[str, str]:
    """Map each disease reached only through a nested grouping to that
    grouping's name (the ``via`` of :func:`iter_disease_targets`)."""
    return {
        disease: via
        for disease, _mtype, via in iter_disease_targets(grouping, groupings_by_name)
        if via is not None
    }


def evaluate_grouping(
    grouping: dict,
    index: dict[str, DiseaseFacts],
    groupings_by_name: dict[str, dict] | None = None,
) -> list[MemberEvaluation]:
    """Evaluate each NECESSARY / N&S criteria block against each member.

    Returns one MemberEvaluation per (member, criteria block). SUFFICIENT-only
    blocks are skipped here (they constrain non-members, not members). A
    disease held through a nested ``GROUPING`` member is a member too — "every
    member of G satisfies C" binds it just as much — so it is evaluated with
    ``via`` set to the nested grouping it arrived through.
    """
    evaluations: list[MemberEvaluation] = []
    criteria_blocks = grouping.get("membership_criteria", []) or []
    targets = list(iter_disease_targets(grouping, groupings_by_name))
    for ci, criteria in enumerate(criteria_blocks):
        semantics = criteria.get("criteria_semantics")
        if semantics == "SUFFICIENT":
            continue  # audits members only for necessary conditions
        logic = criteria.get("logic")
        if logic is None:
            continue
        for ref, mtype, via in targets:
            if ref not in index:
                continue
            facts = index[ref]
            leaves = [
                (
                    leaf.get("description") or leaf.get("criterion_predicate", "?"),
                    _eval_leaf(leaf, facts),
                )
                for leaf in iter_nodes(logic)
                if classify_node(leaf) is NodeKind.LEAF
            ]
            evaluations.append(
                MemberEvaluation(
                    member=ref,
                    member_type=mtype,
                    criteria_index=ci,
                    semantics=semantics,
                    result=_eval_node(logic, facts),
                    leaves=leaves,
                    via=via,
                )
            )
    return evaluations


def find_candidate_members(
    grouping: dict,
    index: dict[str, DiseaseFacts],
    groupings_by_name: dict[str, dict] | None = None,
) -> list[str]:
    """For SUFFICIENT / N&S criteria, find disorders satisfying them that are
    not already listed as direct or nested members (candidate additions)."""
    if groupings_by_name is None:
        groupings_by_name = load_groupings_by_name(
            sorted(glob.glob(str(GROUPINGS_DIR / "*.yaml")))
        )
        if grouping.get("name"):
            groupings_by_name[str(grouping["name"])] = grouping
    listed = grouping_disease_members(grouping, groupings_by_name)
    candidates: set[str] = set()
    for criteria in grouping.get("membership_criteria", []) or []:
        if criteria.get("criteria_semantics") not in (
            "SUFFICIENT",
            "NECESSARY_AND_SUFFICIENT",
        ):
            continue
        logic = criteria.get("logic")
        if logic is None:
            continue
        for name, facts in index.items():
            if name in listed:
                continue
            if _eval_node(logic, facts) is Satisfaction.SATISFIED:
                candidates.add(name)
    return sorted(candidates)


# --------------------------------------------------------------------------- #
# Grouping-overlap reporting
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class GroupingOverlap:
    """Pairwise overlap between two grouping disease-member sets."""

    grouping_a: str
    grouping_b: str
    member_count_a: int
    member_count_b: int
    shared_members: tuple[str, ...]

    @property
    def overlap_count(self) -> int:
        return len(self.shared_members)

    @property
    def relation(self) -> str:
        if self.overlap_count == 0:
            return "DISJOINT"
        if (
            self.overlap_count == self.member_count_a
            and self.overlap_count == self.member_count_b
        ):
            return "EQUAL"
        if self.overlap_count == self.member_count_a:
            return "A_SUBSET_B"
        if self.overlap_count == self.member_count_b:
            return "A_SUPERSET_B"
        return "PARTIAL_OVERLAP"


def load_groupings_by_name(paths: Iterable[str | Path]) -> dict[str, dict]:
    """Load grouping YAML files keyed by their `name`."""
    groupings: dict[str, dict] = {}
    for path in paths:
        with open(path) as f:
            data = safe_load(f)
        if isinstance(data, dict) and data.get("name"):
            groupings[str(data["name"])] = data
    return groupings


def grouping_disease_members(
    grouping: str | dict,
    groupings_by_name: dict[str, dict],
    *,
    expand_nested: bool = True,
    _stack: tuple[str, ...] = (),
) -> set[str]:
    """Return DISEASE/SUBTYPE members for a grouping.

    Nested `member_type: GROUPING` references are expanded by default so the
    result is the set of concrete DisMech disease entries represented by the
    grouping. `MODULE` members are not disease entries and are omitted.
    """
    if isinstance(grouping, str):
        name = grouping
        if name not in groupings_by_name:
            raise KeyError(f"Unknown grouping {name!r}")
        data = groupings_by_name[name]
    else:
        data = grouping
        name = str(data.get("name") or "<anonymous>")

    if name in _stack:
        cycle = " -> ".join((*_stack, name))
        raise ValueError(f"Grouping nesting cycle detected: {cycle}")

    members: set[str] = set()
    for member in data.get("members", []) or []:
        ref = member.get("member")
        if not ref:
            continue
        mtype = member.get("member_type", "DISEASE")
        if mtype in ("DISEASE", "SUBTYPE"):
            members.add(ref)
        elif expand_nested and mtype == "GROUPING":
            members.update(
                grouping_disease_members(
                    ref,
                    groupings_by_name,
                    expand_nested=expand_nested,
                    _stack=(*_stack, name),
                )
            )
    return members


def compute_grouping_overlaps(
    groupings_by_name: dict[str, dict],
    *,
    selected_names: Iterable[str] | None = None,
    include_zero: bool = False,
    expand_nested: bool = True,
) -> list[GroupingOverlap]:
    """Compute all pairwise overlaps among grouping disease-member sets."""
    names = sorted(selected_names if selected_names is not None else groupings_by_name)
    member_sets = {
        name: grouping_disease_members(
            name, groupings_by_name, expand_nested=expand_nested
        )
        for name in names
    }

    overlaps: list[GroupingOverlap] = []
    for i, grouping_a in enumerate(names):
        members_a = member_sets[grouping_a]
        for grouping_b in names[i + 1 :]:
            members_b = member_sets[grouping_b]
            shared = tuple(sorted(members_a & members_b))
            if shared or include_zero:
                overlaps.append(
                    GroupingOverlap(
                        grouping_a=grouping_a,
                        grouping_b=grouping_b,
                        member_count_a=len(members_a),
                        member_count_b=len(members_b),
                        shared_members=shared,
                    )
                )
    return overlaps


# --------------------------------------------------------------------------- #
# Grouping nesting (grouping-of-grouping) reporting
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class NestingCandidate:
    """A ``child`` grouping whose expanded disease members (mostly) sit inside
    ``parent``'s, without ``parent`` listing ``child`` as a nested grouping."""

    parent: str
    child: str
    parent_count: int
    child_count: int
    shared_members: tuple[str, ...]
    missing_members: tuple[str, ...]  # child members the parent does not hold
    equal_sets: bool = False

    @property
    def fraction(self) -> float:
        return len(self.shared_members) / self.child_count if self.child_count else 0.0

    @property
    def is_containment(self) -> bool:
        return not self.missing_members


@dataclass(frozen=True)
class NestingReport:
    """Declared nesting forest plus undeclared containment candidates."""

    children_by_parent: dict[str, tuple[str, ...]]
    parents_by_child: dict[str, tuple[str, ...]]
    containments: tuple[NestingCandidate, ...]
    near_containments: tuple[NestingCandidate, ...]
    standalone: tuple[str, ...]
    unresolved: tuple[tuple[str, str], ...]  # (parent, dangling GROUPING ref)

    @property
    def edge_count(self) -> int:
        return sum(len(c) for c in self.children_by_parent.values())


def expanded_disease_members(name: str, groupings_by_name: dict[str, dict]) -> set[str]:
    """Disease members of a grouping expanded through nesting, cycle-tolerant.

    :func:`grouping_disease_members` raises on a nesting cycle; a report that
    exists to show curators the nesting must survive one and let the tree flag
    it, so this walks :func:`iter_disease_targets`, which cuts cycles instead.
    """
    return {
        disease
        for disease, _mtype, _via in iter_disease_targets(
            groupings_by_name[name], groupings_by_name
        )
    }


def declared_nestings(
    groupings_by_name: dict[str, dict],
) -> tuple[dict[str, tuple[str, ...]], tuple[tuple[str, str], ...]]:
    """Return ``{parent: (child, ...)}`` for every ``member_type: GROUPING``
    member that resolves, plus the ``(parent, ref)`` pairs that do not."""
    children: dict[str, tuple[str, ...]] = {}
    unresolved: list[tuple[str, str]] = []
    for parent in sorted(groupings_by_name, key=str.casefold):
        refs: list[str] = []
        for member in groupings_by_name[parent].get("members", []) or []:
            if member.get("member_type") != "GROUPING" or not member.get("member"):
                continue
            ref = str(member["member"])
            if ref in groupings_by_name:
                refs.append(ref)
            else:
                unresolved.append((parent, ref))
        if refs:
            children[parent] = tuple(sorted(refs, key=str.casefold))
    return children, tuple(unresolved)


def compute_nesting_report(
    groupings_by_name: dict[str, dict],
    *,
    threshold: float = 0.5,
) -> NestingReport:
    """Compare every grouping's expanded disease-member set with every other.

    A pair ``(parent, child)`` is a **containment** when every disease the
    child holds is also held by the parent and the parent does not already
    declare the child as a nested grouping; a **near-containment** when at
    least ``threshold`` of them are. Two groupings with identical member sets
    are reported once, as ``equal_sets``, in name order — neither is obviously
    the parent. Member sets are expanded through declared nesting, so a
    grouping already reached via a nested member is not re-reported against
    its grandparent unless the grandparent lists it directly.
    """
    children_by_parent, unresolved = declared_nestings(groupings_by_name)
    declared = {
        (parent, child) for parent, kids in children_by_parent.items() for child in kids
    }
    parents_by_child: dict[str, list[str]] = {}
    for parent, kids in children_by_parent.items():
        for child in kids:
            parents_by_child.setdefault(child, []).append(parent)

    names = sorted(groupings_by_name, key=str.casefold)
    member_sets = {
        name: expanded_disease_members(name, groupings_by_name) for name in names
    }

    containments: list[NestingCandidate] = []
    near: list[NestingCandidate] = []
    for parent in names:
        parent_set = member_sets[parent]
        for child in names:
            if child == parent or (parent, child) in declared:
                continue
            child_set = member_sets[child]
            if not child_set or not parent_set:
                continue
            shared = child_set & parent_set
            if not shared:
                continue
            equal = child_set == parent_set
            if equal and child.casefold() < parent.casefold():
                continue  # reported once, from the other direction
            if len(parent_set) < len(child_set):
                continue  # the smaller set cannot be the parent
            candidate = NestingCandidate(
                parent=parent,
                child=child,
                parent_count=len(parent_set),
                child_count=len(child_set),
                shared_members=tuple(sorted(shared)),
                missing_members=tuple(sorted(child_set - parent_set)),
                equal_sets=equal,
            )
            if candidate.is_containment:
                containments.append(candidate)
            elif candidate.fraction >= threshold:
                near.append(candidate)

    connected = set(children_by_parent) | set(parents_by_child)
    return NestingReport(
        children_by_parent=children_by_parent,
        parents_by_child={
            child: tuple(sorted(parents, key=str.casefold))
            for child, parents in sorted(parents_by_child.items())
        },
        containments=tuple(containments),
        near_containments=tuple(
            sorted(
                near,
                key=lambda c: (-c.fraction, c.parent.casefold(), c.child.casefold()),
            )
        ),
        standalone=tuple(name for name in names if name not in connected),
        unresolved=unresolved,
    )


def _report_nesting(paths: list[str], threshold: float) -> int:
    groupings_by_name, selected_names = _load_groupings_for_report(paths)
    report = compute_nesting_report(groupings_by_name, threshold=threshold)
    selected = set(selected_names)

    def wanted(*names: str) -> bool:
        return not paths or any(n in selected for n in names)

    print(
        f"Declared nesting: {len(report.children_by_parent)} parent grouping(s), "
        f"{report.edge_count} nested relation(s), "
        f"{len(report.parents_by_child)} nested grouping(s)"
    )
    for parent, kids in report.children_by_parent.items():
        if not wanted(parent, *kids):
            continue
        print(f"  {parent}")
        for child in kids:
            size = len(expanded_disease_members(child, groupings_by_name))
            print(f"    - {child} ({size})")
    for parent, ref in report.unresolved:
        if wanted(parent):
            print(f"  ! {parent}: GROUPING member {ref!r} does not resolve")

    shown = [c for c in report.containments if wanted(c.parent, c.child)]
    print(
        f"\nUndeclared containment ({len(shown)}): every expanded disease member of "
        "the first grouping is also a member of the second, which does not list "
        "it as a nested grouping. A lead, not a ruling — read both rationales."
    )
    for c in shown:
        rel = "=" if c.equal_sets else "⊆"
        print(f"  {c.child} ({c.child_count}) {rel} {c.parent} ({c.parent_count})")

    shown = [c for c in report.near_containments if wanted(c.parent, c.child)]
    print(f"\nNear-containment (>= {threshold:.0%} of the smaller set): {len(shown)}")
    for c in shown:
        missing = ", ".join(c.missing_members)
        print(
            f"  {c.fraction:.0%} {c.child} ({c.child_count}) in {c.parent} "
            f"({c.parent_count}); not in parent: {missing}"
        )

    standalone = [n for n in report.standalone if wanted(n)]
    print(f"\nStandalone (neither a parent nor nested): {len(standalone)}")
    for name in standalone:
        print(f"  {name}")
    return 0


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def _load_groupings_for_report(paths: list[str]) -> tuple[dict[str, dict], list[str]]:
    """Load all groupings for nested expansion and select report targets."""
    all_paths = sorted(glob.glob(str(GROUPINGS_DIR / "*.yaml")))
    if not paths:
        groupings = load_groupings_by_name(all_paths)
        return groupings, sorted(groupings)

    groupings = load_groupings_by_name([*all_paths, *paths])
    selected = sorted(load_groupings_by_name(paths))
    return groupings, selected


def _report_overlaps(paths: list[str], show_zero_overlaps: bool) -> int:
    groupings_by_name, selected_names = _load_groupings_for_report(paths)
    if len(selected_names) < 2:
        print("Need at least two grouping files to compute overlaps.")
        return 0

    all_overlaps = compute_grouping_overlaps(
        groupings_by_name, selected_names=selected_names, include_zero=True
    )
    nonzero = [o for o in all_overlaps if o.overlap_count]
    rows = all_overlaps if show_zero_overlaps else nonzero

    print("\n=== Grouping disease-member overlaps ===")
    print(
        f"  groupings: {len(selected_names)}; pairs checked: {len(all_overlaps)}; "
        f"non-zero overlaps: {len(nonzero)}"
    )

    if not rows:
        print("  no disease-member overlaps")
        return 0

    print(
        "  overlap_count\trelation\tgrouping_a\tmember_count_a\t"
        "grouping_b\tmember_count_b\tshared_members"
    )
    for overlap in sorted(
        rows,
        key=lambda o: (
            -o.overlap_count,
            o.relation,
            o.grouping_a.casefold(),
            o.grouping_b.casefold(),
        ),
    ):
        shared = "; ".join(overlap.shared_members) if overlap.shared_members else "-"
        print(
            f"  {overlap.overlap_count}\t{overlap.relation}\t"
            f"{overlap.grouping_a}\t{overlap.member_count_a}\t"
            f"{overlap.grouping_b}\t{overlap.member_count_b}\t{shared}"
        )
    return 0


def _report(paths: list[str], strict: bool) -> int:
    index = load_disease_index()
    groupings_by_name, _selected = _load_groupings_for_report(paths)
    exit_code = 0
    for path in paths:
        with open(path) as f:
            grouping = safe_load(f)
        name = grouping.get("name", Path(path).stem)
        print(f"\n=== {name} ({Path(path).name}) ===")

        # Tier 1: structural lint (always gating under --strict).
        lint_errors: list[str] = []
        for ci, criteria in enumerate(grouping.get("membership_criteria", []) or []):
            lint_errors.extend(
                lint_criterion(
                    criteria.get("logic"), f"membership_criteria[{ci}].logic"
                )
            )
        if lint_errors:
            exit_code = 1
            print("  STRUCTURAL ERRORS:")
            for e in lint_errors:
                print(f"    - {e}")
        else:
            print("  structure: OK")

        advisories: list[str] = []
        for ci, criteria in enumerate(grouping.get("membership_criteria", []) or []):
            advisories.extend(
                lint_criterion_advisories(
                    criteria.get("logic"), f"membership_criteria[{ci}].logic"
                )
            )
        if advisories:
            # Never gating, including under --strict: these are conventions,
            # not errors, and existing groupings legitimately do not follow them.
            print("  advisories:")
            for a in advisories:
                print(f"    ~ {a}")

        # Tier 2: advisory membership audit.
        for ev in evaluate_grouping(grouping, index, groupings_by_name):
            via = f" (via {ev.via})" if ev.via else ""
            print(
                f"  [criteria {ev.criteria_index} {ev.semantics or '-'}] "
                f"{ev.member}{via}: {ev.result.value}"
            )
            for desc, res in ev.leaves:
                if res is not Satisfaction.SATISFIED:
                    print(f"      - {res.value}: {desc}")
            if strict and ev.result is Satisfaction.NOT_SATISFIED:
                exit_code = 1

        candidates = find_candidate_members(grouping, index, groupings_by_name)
        if candidates:
            print("  candidate members (satisfy sufficient criteria, not listed):")
            for c in candidates:
                print(f"    + {c}")
    return exit_code


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Lint and audit disease grouping membership criteria."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Grouping YAML files (default: all of kb/groupings/).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero on structural errors or NOT_SATISFIED members.",
    )
    parser.add_argument(
        "--overlaps",
        action="store_true",
        help=(
            "Compute all pairwise overlaps between grouping disease-member sets. "
            "Nested GROUPING members are expanded."
        ),
    )
    parser.add_argument(
        "--show-zero-overlaps",
        action="store_true",
        help="With --overlaps, include disjoint pairs in the report.",
    )
    parser.add_argument(
        "--nesting",
        action="store_true",
        help=(
            "Report the declared grouping-of-grouping forest and the undeclared "
            "containments between grouping disease-member sets (advisory)."
        ),
    )
    parser.add_argument(
        "--nesting-threshold",
        type=float,
        default=0.5,
        help=(
            "With --nesting, also list pairs where at least this fraction of the "
            "smaller grouping's members sit inside the larger one (default 0.5)."
        ),
    )
    parser.add_argument(
        "--no-closure",
        action="store_true",
        help=(
            "Evaluate term-valued criteria as exact matches instead of over the "
            "ontology subsumption closure (offline / deterministic runs)."
        ),
    )
    args = parser.parse_args(argv)
    set_closure_enabled(not args.no_closure)
    if args.overlaps:
        return _report_overlaps(args.paths, args.show_zero_overlaps)
    if args.nesting:
        return _report_nesting(args.paths, args.nesting_threshold)

    paths = args.paths or sorted(glob.glob(str(GROUPINGS_DIR / "*.yaml")))
    if not paths:
        print("No grouping files found.")
        return 0
    return _report(paths, args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
