"""Checks and worklists for criteria inside ``definitions[]``.

A ``Definition`` holds criteria in two places: directly
(``definitions[].inclusion_criteria`` and its siblings) and inside named
``criteria_sets``. Two things about those criteria were not machine-readable
until the schema grew a slot for each:

* **How the sets combine.** ``CriteriaSet.minimum_required`` says how many of
  one set's criteria are needed, but nothing said whether a case must meet
  every set (DSM-5 criteria A to E), any one of them (the seropositive and
  seronegative NMOSD pathways), is graded by which one it meets (the
  Mississippi HELLP classes), or is scored across them (PARACELSUS).
  ``Definition.criteria_set_logic`` records that.
* **Which phenotype a criterion is.** A ``CriteriaItem`` is a ``Descriptor``
  with no ontology binding, so ``linkml-term-validator`` never checks its
  ``term`` label, and the only link from a criterion to the phenotype it tests
  for was a shared CURIE. ``CriteriaItem.attaches_to`` now names that
  phenotype with the ``<kind>#<name>`` entity-reference grammar, which
  ``dismech.entity_refs`` already resolves as a foreign key.

:func:`criteria_errors` holds the deterministic rules both slots carry, so the
ungated ``scripts/check_entity_refs.py`` sweep and the pytest suite apply the
same ones. :func:`attaches_to_candidates` is the backfill worklist behind
``scripts/criteria_item_refs.py``.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any, NamedTuple

from dismech.entity_refs import parse_entity_ref

__all__ = [
    "CRITERIA_ITEM_SLOTS",
    "AttachCandidate",
    "CriteriaItemSite",
    "attaches_to_candidates",
    "criteria_errors",
    "iter_criteria_items",
]

#: The ``CriteriaItem``-valued slots, in the order the schema lists them. They
#: occur on both ``Definition`` and ``CriteriaSet``.
CRITERIA_ITEM_SLOTS: tuple[str, ...] = (
    "core_clinical_characteristics",
    "inclusion_criteria",
    "exclusion_criteria",
    "imaging_requirements",
    "laboratory_requirements",
    "additional_requirements",
)


class CriteriaItemSite(NamedTuple):
    """One criterion: its dotted ``path``, the slot holding it, and the item."""

    path: str
    slot: str
    item: dict


class AttachCandidate(NamedTuple):
    """A criterion with no ``attaches_to``, and what the backfill can say about it.

    ``status`` is one of:

    ``EXACT``
        The criterion's ``term`` is the ``phenotype_term`` of exactly one
        phenotype in the entry, and the criterion's ``preferred_term`` is that
        phenotype's ``name`` or ``preferred_term`` (ignoring case). ``ref`` is
        the reference to write.
    ``TERM_ONLY``
        One phenotype carries the term, but under different wording. ``ref``
        is the candidate, and a person decides: a shared CURIE does not show
        the two say the same thing. In NMOSD the criterion "Acute myelitis"
        and the phenotype "Longitudinally Extensive Transverse Myelitis" are
        both bound to ``HP:0012486`` Myelitis, and the phenotype is the
        narrower of the two.
    ``AMBIGUOUS``
        Several phenotypes carry that term (typically rows stratified by
        subtype). A person picks; ``ref`` is empty.
    ``NO_MATCH``
        The criterion has a term no phenotype in the entry carries.
    ``NO_TERM``
        The criterion has no term, so there is nothing to match on.
    """

    site: CriteriaItemSite
    status: str
    ref: str
    matches: tuple[str, ...]


def _as_list(value: Any) -> list:
    return value if isinstance(value, list) else []


def iter_criteria_items(data: dict) -> Iterator[CriteriaItemSite]:
    """Every ``CriteriaItem`` in an entry's ``definitions``, with its location."""
    for i, defn in enumerate(_as_list(data.get("definitions"))):
        if not isinstance(defn, dict):
            continue
        containers = [(f"definitions[{i}]", defn)]
        for j, cset in enumerate(_as_list(defn.get("criteria_sets"))):
            if isinstance(cset, dict):
                containers.append((f"definitions[{i}].criteria_sets[{j}]", cset))
        for prefix, container in containers:
            for slot in CRITERIA_ITEM_SLOTS:
                for k, item in enumerate(_as_list(container.get(slot))):
                    if isinstance(item, dict):
                        yield CriteriaItemSite(f"{prefix}.{slot}[{k}]", slot, item)


def _term_of(descriptor: Any) -> tuple[str | None, str | None]:
    if not isinstance(descriptor, dict):
        return None, None
    term = descriptor.get("term")
    if not isinstance(term, dict):
        return None, None
    return term.get("id"), term.get("label")


def _phenotype_terms(data: dict) -> dict[str, tuple[str | None, str | None]]:
    """Phenotype ``name`` -> its ``phenotype_term`` (id, label)."""
    out: dict[str, tuple[str | None, str | None]] = {}
    for phenotype in _as_list(data.get("phenotypes")):
        if isinstance(phenotype, dict) and isinstance(phenotype.get("name"), str):
            out.setdefault(phenotype["name"], _term_of(phenotype.get("phenotype_term")))
    return out


def _local_phenotype_targets(refs: list) -> list[str]:
    """Names of the same-entry phenotypes a list of references points at."""
    names = []
    for ref in refs:
        parsed = parse_entity_ref(ref) if isinstance(ref, str) else None
        if parsed is None or parsed.file is not None:
            continue
        if parsed.kind in ("phenotypes", "phenotype") and parsed.name.strip():
            names.append(parsed.name.strip())
    return names


def criteria_errors(data: dict) -> list[str]:
    """Deterministic rule violations for criteria in one loaded entry.

    Two rules:

    * ``criteria_set_logic`` says how criteria sets combine, so it is only
      meaningful on a definition with at least two of them.
    * A criterion that both ``attaches_to`` a phenotype and carries its own
      ``term`` must carry that phenotype's binding, id and label alike. The
      phenotype's binding is the one ``linkml-term-validator`` checks; the
      criterion's is not checked by anything else, so this is what keeps the
      two from drifting apart.

    Whether a reference resolves at all is ``entity_ref_errors``' job and is
    not repeated here: an unresolved phenotype is simply skipped.
    """
    if not isinstance(data, dict):
        return []
    errors: list[str] = []
    for i, defn in enumerate(_as_list(data.get("definitions"))):
        if not isinstance(defn, dict) or not defn.get("criteria_set_logic"):
            continue
        n_sets = len(_as_list(defn.get("criteria_sets")))
        if n_sets < 2:
            errors.append(
                f"definitions[{i}] ({defn.get('name')!r}) sets "
                f"criteria_set_logic: {defn['criteria_set_logic']} but has "
                f"{n_sets} criteria set(s); the slot says how two or more "
                f"sets combine, so remove it"
            )

    phenotypes = _phenotype_terms(data)
    for site in iter_criteria_items(data):
        targets = [
            name
            for name in _local_phenotype_targets(_as_list(site.item.get("attaches_to")))
            if name in phenotypes
        ]
        item_id, item_label = _term_of(site.item)
        if not targets or item_id is None:
            continue
        bound = {phenotypes[name] for name in targets}
        if (item_id, item_label) in bound:
            continue
        expected = "; ".join(
            f"{name}: {pid} {plabel!r}"
            for name in targets
            for pid, plabel in [phenotypes[name]]
        )
        errors.append(
            f"{site.path} carries term {item_id} {item_label!r} but attaches_to "
            f"a phenotype bound differently ({expected}); copy the "
            f"phenotype's term or drop the criterion's own"
        )
    return errors


def _fold(text: str) -> str:
    return " ".join(text.split()).casefold()


def attaches_to_candidates(data: dict) -> list[AttachCandidate]:
    """Every criterion without ``attaches_to``, classified for the backfill."""
    if not isinstance(data, dict):
        return []
    by_term: dict[str, list[str]] = {}
    wording: dict[str, set[str]] = {}
    for phenotype in _as_list(data.get("phenotypes")):
        if not isinstance(phenotype, dict) or not isinstance(
            phenotype.get("name"), str
        ):
            continue
        name = phenotype["name"]
        pid, _label = _term_of(phenotype.get("phenotype_term"))
        if pid and name not in by_term.get(pid, []):
            by_term.setdefault(pid, []).append(name)
        descriptor = phenotype.get("phenotype_term")
        preferred = (
            descriptor.get("preferred_term") if isinstance(descriptor, dict) else None
        )
        wording.setdefault(name, set()).update(
            _fold(w) for w in (name, preferred) if isinstance(w, str)
        )

    out: list[AttachCandidate] = []
    for site in iter_criteria_items(data):
        if site.item.get("attaches_to"):
            continue
        item_id, _ = _term_of(site.item)
        if item_id is None:
            out.append(AttachCandidate(site, "NO_TERM", "", ()))
            continue
        names = tuple(by_term.get(item_id, ()))
        if len(names) == 1:
            preferred = site.item.get("preferred_term")
            same = isinstance(preferred, str) and _fold(preferred) in wording[names[0]]
            status = "EXACT" if same else "TERM_ONLY"
            out.append(AttachCandidate(site, status, f"phenotypes#{names[0]}", names))
        elif names:
            out.append(AttachCandidate(site, "AMBIGUOUS", "", names))
        else:
            out.append(AttachCandidate(site, "NO_MATCH", "", ()))
    return out
