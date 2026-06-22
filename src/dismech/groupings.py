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
   returning SATISFIED / NOT_SATISFIED / UNKNOWN per leaf and per branch. This
   is advisory: criteria are often aspirational (a member may not yet declare a
   ``conforms_to`` edge the criteria require), so the CLI reports rather than
   gates.

3. **Overlap reporting** (:func:`compute_grouping_overlaps`) — all-vs-all
   comparison of grouping disease-member sets, expanding nested ``GROUPING``
   members to concrete disease entries.
"""

from __future__ import annotations

import argparse
import glob
from dataclasses import dataclass, field
from enum import Enum
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Optional

import yaml

ROOT_DIR = Path(__file__).resolve().parents[2]
DISORDERS_DIR = ROOT_DIR / "kb" / "disorders"
MODULES_DIR = ROOT_DIR / "kb" / "modules"
GROUPINGS_DIR = ROOT_DIR / "kb" / "groupings"

BRANCH_OPERATORS = {"AND", "OR", "NOT"}

# Map each leaf predicate to the payload slot(s) it requires. ``None`` means the
# constraint is carried in free text (``description``) and has no structured
# payload to evaluate.
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

    def negate(self) -> "Satisfaction":
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


def iter_nodes(node: Any) -> Iterable[dict]:
    """Yield every node in a (possibly nested) criteria expression."""
    if not isinstance(node, dict):
        return
    yield node
    for child in node.get("operands", []) or []:
        yield from iter_nodes(child)


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
    # HP id -> best (strongest) known frequency band, if any.
    phenotype_freq: dict[str, Optional[str]] = field(default_factory=dict)


def _walk(obj: Any) -> Iterable[Any]:
    """Recursively yield every mapping and list element in a nested structure."""
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from _walk(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _walk(v)


def extract_disease_facts(name: str, data: dict) -> DiseaseFacts:
    """Extract genes, GO terms, module conformance, and phenotype frequencies."""
    facts = DiseaseFacts(name=name)

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


def _stronger_freq(a: Optional[str], b: Optional[str]) -> Optional[str]:
    """Return the stronger (higher-frequency) of two frequency bands."""
    ranks = [f for f in (a, b) if f in FREQUENCY_RANK]
    if not ranks:
        return a or b
    return min(ranks, key=lambda f: FREQUENCY_RANK[f])


@lru_cache(maxsize=None)
def load_disease_index(
    disorders_dir: Path = DISORDERS_DIR,
) -> dict[str, DiseaseFacts]:
    """Build a name -> DiseaseFacts index over kb/disorders/ (cached)."""
    index: dict[str, DiseaseFacts] = {}
    for fp in glob.glob(str(disorders_dir / "*.yaml")):
        if fp.endswith(".history.yaml"):
            continue
        with open(fp) as f:
            data = yaml.safe_load(f)
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
            result = (
                Satisfaction.SATISFIED
                if ids & facts.go_ids
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
    elif predicate == "HAS_PHENOTYPE":
        hp = _term_id(node.get("phenotype_term"))
        if hp:
            if hp not in facts.phenotype_freq:
                result = Satisfaction.NOT_SATISFIED
            else:
                min_freq = node.get("min_frequency")
                have = facts.phenotype_freq[hp]
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
    # HAS_CLASSIFICATION / HAS_INHERITANCE / HAS_MAPPING / OTHER -> UNKNOWN.

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


def _term_id(descriptor: Any) -> Optional[str]:
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
    semantics: Optional[str]
    result: Satisfaction
    leaves: list[tuple[str, Satisfaction]]  # (leaf description, result)


def evaluate_grouping(
    grouping: dict, index: dict[str, DiseaseFacts]
) -> list[MemberEvaluation]:
    """Evaluate each NECESSARY / N&S criteria block against each member.

    Returns one MemberEvaluation per (member, criteria block). SUFFICIENT-only
    blocks are skipped here (they constrain non-members, not members).
    """
    evaluations: list[MemberEvaluation] = []
    criteria_blocks = grouping.get("membership_criteria", []) or []
    for ci, criteria in enumerate(criteria_blocks):
        semantics = criteria.get("criteria_semantics")
        if semantics == "SUFFICIENT":
            continue  # audits members only for necessary conditions
        logic = criteria.get("logic")
        if logic is None:
            continue
        for member in grouping.get("members", []) or []:
            mtype = member.get("member_type", "DISEASE")
            ref = member.get("member")
            if mtype not in ("DISEASE", "SUBTYPE") or ref not in index:
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
                )
            )
    return evaluations


def find_candidate_members(
    grouping: dict,
    index: dict[str, DiseaseFacts],
    groupings_by_name: Optional[dict[str, dict]] = None,
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
            data = yaml.safe_load(f)
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
    selected_names: Optional[Iterable[str]] = None,
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
    exit_code = 0
    for path in paths:
        with open(path) as f:
            grouping = yaml.safe_load(f)
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

        # Tier 2: advisory membership audit.
        for ev in evaluate_grouping(grouping, index):
            print(
                f"  [criteria {ev.criteria_index} {ev.semantics or '-'}] "
                f"{ev.member}: {ev.result.value}"
            )
            for desc, res in ev.leaves:
                if res is not Satisfaction.SATISFIED:
                    print(f"      - {res.value}: {desc}")
            if strict and ev.result is Satisfaction.NOT_SATISFIED:
                exit_code = 1

        candidates = find_candidate_members(grouping, index)
        if candidates:
            print("  candidate members (satisfy sufficient criteria, not listed):")
            for c in candidates:
                print(f"    + {c}")
    return exit_code


def main(argv: Optional[list[str]] = None) -> int:
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
    args = parser.parse_args(argv)
    if args.overlaps:
        return _report_overlaps(args.paths, args.show_zero_overlaps)

    paths = args.paths or sorted(glob.glob(str(GROUPINGS_DIR / "*.yaml")))
    if not paths:
        print("No grouping files found.")
        return 0
    return _report(paths, args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
