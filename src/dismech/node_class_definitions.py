"""Logical definitions for pathograph node classes.

A class in ``kb/node_classes/pathograph_node_classes.txt`` may carry one
``= <expression>`` line: a *sufficient condition* over the ontology-bound slots
a pathophysiology node already carries. A node satisfying the expression is an
instance of the class. The expression is not a schema slot and nothing in
``kb/`` names a class yet; it is what lets the tree be *checked* against its
own worked examples rather than only read.

Grammar (whitespace-separated tokens; a label is single-quoted)::

    expression := conjunction ("or" conjunction)*
    conjunction := atom ("and" atom)*
    atom := ["not"] SLOT "some" TERM ["'label'"] ["modifier" VALUE("|" VALUE)*]
    TERM := CURIE (GO:0008219) | PREFIX (UBERON, ECTO, CHEBI ...)

``SLOT some CURIE`` holds when a descriptor in that slot is bound to the term or
to one of its ``is_a`` descendants (see :func:`evaluate`); ``SLOT some PREFIX``
holds when any descriptor there is bound to a term of that prefix. A trailing
``modifier`` restricts the *same* descriptor to one of the listed
``ModifierEnum`` values, which is how a polar leaf is told apart from its
opposite (``signal transduction modifier INCREASED`` vs ``DECREASED``).
``and`` binds tighter than ``or``; there are no parentheses.

Precision is deliberately not part of the grammar. Two classes may both be
satisfied by one node -- that is the debundle signal the tree already looks
for, not an error in either definition.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

#: Pathophysiology slots that hold ontology-bound descriptors.
DESCRIPTOR_SLOTS = frozenset({
    "biological_processes", "molecular_functions", "cellular_components",
    "cell_types", "locations", "chemical_entities", "gene_products",
    "protein_complexes", "genes", "triggers", "pathways", "assays",
})

#: ``ModifierEnum`` permissible values (``src/dismech/schema/dismech.yaml``).
MODIFIER_VALUES = frozenset({
    "INCREASED", "DECREASED", "ABNORMAL", "DYSREGULATED", "ABSENT",
})

CURIE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*:[A-Za-z0-9._-]+$")
PREFIX_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*$")
TOKEN_RE = re.compile(r"'[^']*'|\S+")


class DefinitionError(ValueError):
    """A ``=`` expression could not be parsed."""


@dataclass(frozen=True)
class Atom:
    slot: str
    term: str
    label: str | None = None
    negated: bool = False
    modifiers: tuple[str, ...] = ()

    @property
    def is_prefix(self) -> bool:
        return ":" not in self.term

    def render(self) -> str:
        parts = ["not"] if self.negated else []
        parts += [self.slot, "some", self.term]
        if self.label is not None:
            parts.append(f"'{self.label}'")
        if self.modifiers:
            parts += ["modifier", "|".join(self.modifiers)]
        return " ".join(parts)


@dataclass(frozen=True)
class Definition:
    raw: str
    disjuncts: tuple[tuple[Atom, ...], ...] = field(default_factory=tuple)

    def atoms(self) -> Iterator[Atom]:
        for conj in self.disjuncts:
            yield from conj

    def render(self) -> str:
        return " or ".join(" and ".join(a.render() for a in conj) for conj in self.disjuncts)


def parse_definition(text: str) -> Definition:
    """Parse one ``=`` expression. Raises :class:`DefinitionError`."""
    tokens = TOKEN_RE.findall(text.strip())
    if not tokens:
        raise DefinitionError("empty definition")
    disjuncts: list[tuple[Atom, ...]] = []
    conj: list[Atom] = []
    i = 0

    def take() -> str:
        nonlocal i
        if i >= len(tokens):
            raise DefinitionError(f"unexpected end of definition: {text!r}")
        tok = tokens[i]
        i += 1
        return tok

    while True:
        negated = False
        tok = take()
        if tok == "not":
            negated = True
            tok = take()
        slot = tok
        if slot not in DESCRIPTOR_SLOTS:
            raise DefinitionError(f"unknown slot {slot!r}")
        if take() != "some":
            raise DefinitionError(f"expected 'some' after slot {slot!r}")
        term = take()
        if not (CURIE_RE.match(term) or PREFIX_RE.match(term)):
            raise DefinitionError(f"bad term {term!r}: expected a CURIE or a prefix")
        label = None
        modifiers: tuple[str, ...] = ()
        if i < len(tokens) and tokens[i].startswith("'"):
            label = take()[1:-1]
            if ":" not in term:
                raise DefinitionError(f"a prefix atom ({term}) takes no label")
        if i < len(tokens) and tokens[i] == "modifier":
            take()
            modifiers = tuple(take().split("|"))
            bad = [m for m in modifiers if m not in MODIFIER_VALUES]
            if bad:
                raise DefinitionError(f"unknown modifier value(s) {bad}")
        conj.append(Atom(slot, term, label, negated, modifiers))
        if i >= len(tokens):
            disjuncts.append(tuple(conj))
            break
        op = take()
        if op == "and":
            continue
        if op == "or":
            disjuncts.append(tuple(conj))
            conj = []
            continue
        raise DefinitionError(f"expected 'and' or 'or', got {op!r}")
    return Definition(raw=text.strip(), disjuncts=tuple(disjuncts))


# --- evaluation -----------------------------------------------------------------

AncestorFn = Callable[[str], set[str]]


def _descriptors(node: dict[str, Any], slot: str) -> Iterator[tuple[str, str | None]]:
    """``(term id, modifier)`` for each bound descriptor in ``slot``."""
    for item in node.get(slot) or []:
        if not isinstance(item, dict):
            continue
        term = (item.get("term") or {}).get("id")
        if term:
            yield str(term), item.get("modifier")


def atom_holds(atom: Atom, node: dict[str, Any], ancestors: AncestorFn) -> bool:
    """Whether one atom (ignoring negation) is satisfied by ``node``."""
    for term, modifier in _descriptors(node, atom.slot):
        if atom.is_prefix:
            if not term.upper().startswith(atom.term.upper() + ":"):
                continue
        elif term != atom.term and atom.term not in ancestors(term):
            continue
        if atom.modifiers and modifier not in atom.modifiers:
            continue
        return True
    return False


def evaluate(defn: Definition, node: dict[str, Any], ancestors: AncestorFn) -> bool:
    """Whether ``node`` satisfies ``defn``.

    ``ancestors(curie)`` returns the ``is_a`` ancestors of a term (the term
    itself need not be included). Pass ``lambda _: set()`` for exact matching
    only, which is what an offline check can do.
    """
    for conj in defn.disjuncts:
        if all(atom_holds(a, node, ancestors) != a.negated for a in conj):
            return True
    return False


def no_closure(_: str) -> set[str]:
    """An ``ancestors`` function for exact-match evaluation."""
    return set()


# --- label checking ---------------------------------------------------------------


def curie_labels(definitions: Iterable[Definition]) -> dict[str, str | None]:
    """Every CURIE mentioned, with the label the definition claims for it."""
    out: dict[str, str | None] = {}
    for defn in definitions:
        for atom in defn.atoms():
            if not atom.is_prefix:
                out.setdefault(atom.term, atom.label)
    return out


def check_labels(
    claimed: dict[str, str | None], lookup: Callable[[str], str | None]
) -> list[str]:
    """Compare claimed labels against ``lookup``; returns problem strings.

    A CURIE ``lookup`` cannot resolve is reported as *unresolved* rather than
    wrong, so an offline run against the term caches stays honest about what
    it did not check.
    """
    problems = []
    for curie, label in sorted(claimed.items()):
        actual = lookup(curie)
        if actual is None:
            problems.append(f"{curie}: unresolved (not in cache)")
        elif label is not None and actual != label:
            problems.append(f"{curie}: label {label!r} but ontology says {actual!r}")
    return problems


# --- checking the committed tree ---------------------------------------------------


def cache_label_lookup(cache_dir: str | Path = "cache") -> Callable[[str], str | None]:
    """Label lookup over the committed ``cache/<prefix>/terms.csv`` files (offline)."""
    import csv

    root = Path(cache_dir)
    loaded: dict[str, dict[str, str]] = {}

    def lookup(curie: str) -> str | None:
        prefix = curie.split(":", 1)[0].lower()
        if prefix not in loaded:
            table: dict[str, str] = {}
            path = root / prefix / "terms.csv"
            if path.is_file():
                with path.open(encoding="utf-8") as fh:
                    for row in csv.DictReader(fh):
                        table[row["curie"]] = row["label"]
            loaded[prefix] = table
        return loaded[prefix].get(curie)

    return lookup


def ontology_label_lookup() -> Callable[[str], str | None]:
    """Label lookup that asks the ontology (OAK ``ols:`` adapters; network)."""
    from oaklib import get_adapter

    adapters: dict[str, Any] = {}

    def lookup(curie: str) -> str | None:
        prefix = curie.split(":", 1)[0].lower()
        if prefix not in adapters:
            try:
                adapters[prefix] = get_adapter(f"ols:{prefix}")
            except Exception:  # noqa: BLE001 - an unknown prefix is "unresolved"
                adapters[prefix] = None
        adapter = adapters[prefix]
        if adapter is None:
            return None
        try:
            return adapter.label(curie)
        except Exception:  # noqa: BLE001
            return None

    return lookup


def go_ancestors() -> AncestorFn:
    """``is_a`` closure over GO from the local OAK sqlite build (memoised).

    Only GO is closed; a CURIE from any other prefix returns an empty set, so a
    ``CL:`` or ``CHEBI:`` atom matches exactly. That is documented behaviour,
    not a gap to paper over silently: the GO build is ~300 MB and the others
    are larger still.
    """
    from oaklib import get_adapter

    adapter = get_adapter("sqlite:obo:go")
    memo: dict[str, set[str]] = {}

    def ancestors(curie: str) -> set[str]:
        if not curie.startswith("GO:"):
            return set()
        if curie not in memo:
            memo[curie] = set(adapter.ancestors(curie, predicates=["rdfs:subClassOf"]))
        return memo[curie]

    return ancestors


@dataclass
class ClassEvaluation:
    """How one defined class fares against the KB."""

    path: tuple[str, ...]
    definition: str
    examples: int
    examples_matched: int
    kb_matched: int
    #: examples of *other* classes the definition also captures, by class path
    cross_hits: dict[tuple[str, ...], int] = field(default_factory=dict)

    @property
    def recall(self) -> float:
        return self.examples_matched / self.examples if self.examples else 0.0


def evaluate_tree(roots: list[Any], kb_dirs: Iterable[Any], ancestors: AncestorFn) -> list[ClassEvaluation]:
    """Evaluate every defined class against its examples and the whole KB.

    Recall over a class's own worked examples says whether the definition
    captures what the curator meant; ``kb_matched`` says how many nodes it
    would classify; ``cross_hits`` says which other classes' examples it also
    captures, which is where a definition is either too broad or the tree's
    own boundary is soft.
    """
    from dismech.node_classes import iter_classes
    from dismech.yaml_io import safe_load

    kb: dict[tuple[str, str], dict[str, Any]] = {}
    for kb_dir in kb_dirs:
        for path in sorted(Path(kb_dir).glob("*.yaml")):
            try:
                data = safe_load(path.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001 - not this tool's business
                continue
            for node in (data or {}).get("pathophysiology") or []:
                if isinstance(node, dict) and node.get("name"):
                    kb[(str(node["name"]), path.stem)] = node

    example_owner: dict[tuple[str, str], tuple[str, ...]] = {}
    for trail, cls in iter_classes(roots):
        for ex in cls.examples:
            example_owner.setdefault((ex.node, ex.disease), trail)

    reports = []
    for trail, cls in iter_classes(roots):
        if not cls.definition:
            continue
        defn = parse_definition(cls.definition)
        own = [(ex.node, ex.disease) for ex in cls.examples]
        matched_own = sum(1 for key in own if key in kb and evaluate(defn, kb[key], ancestors))
        kb_matched = 0
        cross: dict[tuple[str, ...], int] = {}
        for key, node in kb.items():
            if not evaluate(defn, node, ancestors):
                continue
            kb_matched += 1
            owner = example_owner.get(key)
            if owner is not None and owner != trail and not owner[: len(trail)] == trail:
                cross[owner] = cross.get(owner, 0) + 1
        reports.append(ClassEvaluation(trail, cls.definition, len(own), matched_own, kb_matched, cross))
    return reports
