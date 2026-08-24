"""Resolution of dismech entity references (the ``[<file>:]<kind>#<name>`` grammar).

Several slots point at another object *inside the same entry* using a
hash-anchor grammar the schema documents on ``Discussion.attaches_to``::

    [<file>:]<kind>#<name>

    pathophysiology#Amyloid Plaque Formation
    phenotype#Memory Loss
    Liver_Cirrhosis:pathophysiology#Hepatic Stellate Cell Activation

The same grammar is reused by ``Experiment.would_support`` /
``would_refute`` and by ``ExperimentalPerturbation.target`` /
``ExperimentalReadout.target`` (see ``dismech.yaml``, which says so in as many
words). These are foreign keys, and this module is the single place that knows
how to follow one — so the test suite, the HTML renderer, and any exporter
resolve a reference the same way rather than each growing its own half of the
rules (issue #9193).

Three rules a naive "look the section up by name" resolver gets wrong, all of
which occur in committed content:

* ``disease#`` is not a section at all — it is a virtual anchor for the whole
  entry, matched against the top-level ``name``.
* ``mechanistic_hypothesis#`` resolves against ``hypothesis_group_id``, not
  ``name`` (``MechanisticHypothesis`` has no ``name`` slot).
* ``prevalence#`` resolves against ``population``, likewise.

Curated content also drifts between singular and plural prefixes
(``treatment#`` 53 vs ``treatments#`` 122; ``phenotype#`` 79 vs
``phenotypes#`` 82). Both forms are accepted; content is not churned to
normalise them.

An unknown prefix, or a cross-file reference, yields ``None`` — "no opinion" —
rather than a failure, so a gap in :data:`SECTION_KEYS` can never be mistaken
for a broken reference in the knowledge base.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any, NamedTuple

__all__ = [
    "DISEASE_KIND",
    "REF_SLOTS",
    "SECTION_KEYS",
    "EntityRef",
    "entity_ref_index",
    "iter_entity_refs",
    "parse_entity_ref",
    "resolve_entity_ref",
    "section_items",
]


class EntityRef(NamedTuple):
    """A parsed entity reference.

    ``file`` is ``None`` for a local reference (the common case); a non-``None``
    ``file`` names another entry and is not resolvable against a single loaded
    document.
    """

    file: str | None
    kind: str
    name: str


#: Virtual ``kind`` naming the entry itself rather than one of its sections.
DISEASE_KIND = "disease"

#: Reference prefix -> (top-level slot, key slots to match ``name`` against).
#:
#: Key slots are tried in order and a match on any one resolves the reference.
#: Most sections key on ``name``; the exceptions are called out in the module
#: docstring. Singular aliases are listed alongside the plural section they
#: point into, because both forms occur in committed content.
SECTION_KEYS: dict[str, tuple[str, tuple[str, ...]]] = {
    # --- pathograph and clinical sections, keyed on `name` -----------------
    "pathophysiology": ("pathophysiology", ("name",)),
    "phenotype": ("phenotypes", ("name",)),
    "phenotypes": ("phenotypes", ("name",)),
    "treatment": ("treatments", ("name",)),
    "treatments": ("treatments", ("name",)),
    "genetic": ("genetic", ("name",)),
    "diagnosis": ("diagnosis", ("name",)),
    "biochemical": ("biochemical", ("name",)),
    "environmental": ("environmental", ("name",)),
    "subtype": ("has_subtypes", ("name",)),
    "has_subtypes": ("has_subtypes", ("name",)),
    "definitions": ("definitions", ("name",)),
    "differential_diagnoses": ("differential_diagnoses", ("name",)),
    "imaging_findings": ("imaging_findings", ("name",)),
    "histopathology": ("histopathology", ("name",)),
    "external_assertions": ("external_assertions", ("name",)),
    "epidemiology": ("epidemiology", ("name",)),
    "transmission": ("transmission", ("name",)),
    "infectious_agent": ("infectious_agent", ("name",)),
    "inheritance": ("inheritance", ("name",)),
    "clinical_trials": ("clinical_trials", ("name",)),
    "variant": ("variants", ("name",)),
    "variants": ("variants", ("name",)),
    "stage": ("stages", ("name",)),
    "stages": ("stages", ("name",)),
    # --- models ------------------------------------------------------------
    # `name` is an attribute rather than a slot on AnimalModel, and is optional
    # there, so a model curated without one is named by its species or genotype
    # the way the renderer's fallback label is. Committed content references
    # unnamed models by species (`animal_models#Mus musculus`), so `species` is
    # a real key here, not a courtesy fallback.
    "animal_model": ("animal_models", ("name", "species", "genotype")),
    "animal_models": ("animal_models", ("name", "species", "genotype")),
    "experimental_model": ("experimental_models", ("name",)),
    "experimental_models": ("experimental_models", ("name",)),
    "computational_model": ("computational_models", ("name",)),
    "computational_models": ("computational_models", ("name",)),
    # --- sections with no `name` slot at all -------------------------------
    # MechanisticHypothesis is keyed on its stable id; `hypothesis_label` is
    # accepted too because it is the human-readable form a curator sees.
    "mechanistic_hypothesis": (
        "mechanistic_hypotheses",
        ("hypothesis_group_id", "hypothesis_label"),
    ),
    "mechanistic_hypotheses": (
        "mechanistic_hypotheses",
        ("hypothesis_group_id", "hypothesis_label"),
    ),
    # Prevalence records the cohort, not a name.
    "prevalence": ("prevalence", ("population",)),
    # ProgressionInfo has no name either; `phase` is what a record is called.
    "progression": ("progression", ("phase",)),
    # Dataset is keyed on its accession, with the title as a fallback.
    "dataset": ("datasets", ("accession", "title")),
    "datasets": ("datasets", ("accession", "title")),
    # Discussion is keyed on its stable cross-reference id.
    "discussion": ("discussions", ("discussion_id",)),
    "discussions": ("discussions", ("discussion_id",)),
}

#: Slots whose values carry the hash-anchor grammar. ``target`` is multivalued
#: in neither of its two homes but *is* also used by ``ModelMechanismLink`` and
#: ``target_mechanisms`` for plain node names, so a ``target`` without a ``#``
#: is simply not an entity reference and is skipped by the parser.
REF_SLOTS: frozenset[str] = frozenset(
    {"attaches_to", "would_support", "would_refute", "target"}
)


def parse_entity_ref(ref: Any) -> EntityRef | None:
    """Parse ``[<file>:]<kind>#<name>``; return ``None`` if it is not one.

    A value without a ``#`` is not an entity reference (``target`` in
    particular carries plain node names elsewhere), and neither is a non-string.
    """
    if not isinstance(ref, str):
        return None
    if "#" not in ref:
        return None
    left, name = ref.split("#", 1)
    file: str | None = None
    if ":" in left:
        file, left = left.split(":", 1)
    kind = left.strip()
    if not kind:
        return None
    return EntityRef(file=file or None, kind=kind, name=name)


def section_items(data: dict, slot: str) -> list[Any]:
    """Return the items a section reference resolves against.

    Almost always just ``data[slot]``. ``variants`` is the exception: a variant
    may be curated disease-level or nested under the gene it belongs to
    (``genetic[].variants``), and both are the same kind of object, so a
    ``variant#`` reference must see both.
    """
    items = data.get(slot)
    items = list(items) if isinstance(items, list) else []
    if slot == "variants":
        for gene in data.get("genetic") or []:
            if isinstance(gene, dict) and isinstance(gene.get("variants"), list):
                items.extend(gene["variants"])
    return items


def _key_values(item: Any, key_slots: tuple[str, ...]) -> Iterator[str]:
    if not isinstance(item, dict):
        return
    for key in key_slots:
        value = item.get(key)
        if isinstance(value, str) and value:
            yield value


def resolve_entity_ref(data: dict, ref: Any) -> bool | None:
    """Resolve a *local* entity reference against one loaded entry.

    Returns ``True`` when the reference resolves, ``False`` when it dangles,
    and ``None`` when this module has no opinion — the value is not an entity
    reference, names another file, or uses a prefix absent from
    :data:`SECTION_KEYS`. Callers must treat ``None`` as "skip", never as a
    failure: an unmapped prefix is a gap here, not a defect in the content.
    """
    parsed = parse_entity_ref(ref)
    if parsed is None or parsed.file is not None:
        return None
    if parsed.kind == DISEASE_KIND:
        return parsed.name == data.get("name")
    mapping = SECTION_KEYS.get(parsed.kind)
    if mapping is None:
        return None
    slot, key_slots = mapping
    return any(
        parsed.name in set(_key_values(item, key_slots))
        for item in section_items(data, slot)
    )


def entity_ref_index(data: dict) -> dict[str, list[Any]]:
    """Map every resolvable ``<kind>#<name>`` reference to the item(s) it names.

    Both the singular and plural spelling of a section are emitted, so a
    consumer can look up whichever form the content used without normalising.
    The disease-level ``disease#<name>`` anchor is included when the entry has
    a name.
    """
    index: dict[str, list[Any]] = {}
    for kind, (slot, key_slots) in SECTION_KEYS.items():
        for item in section_items(data, slot):
            for value in _key_values(item, key_slots):
                index.setdefault(f"{kind}#{value}", []).append(item)
    name = data.get("name")
    if isinstance(name, str) and name:
        index.setdefault(f"{DISEASE_KIND}#{name}", []).append(data)
    return index


def iter_entity_refs(node: Any, path: str = "") -> Iterator[tuple[str, str]]:
    """Walk a loaded entry, yielding ``(path, ref)`` for every reference slot.

    ``path`` is a dotted/indexed location such as
    ``discussions[2].attaches_to[0]``, for error messages that point straight
    at the offending line's neighbourhood.
    """
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}" if path else str(key)
            if key in REF_SLOTS:
                if isinstance(value, str):
                    yield child, value
                    continue
                if isinstance(value, list) and all(
                    isinstance(item, str) for item in value
                ):
                    for i, item in enumerate(value):
                        yield f"{child}[{i}]", item
                    continue
                # Every ref slot holds a string or a list of strings today.
                # If one ever nests objects -- `target` is the likeliest, being
                # shared with ModelMechanismLink and target_mechanisms -- keep
                # walking rather than silently stopping, so references
                # underneath it are still found.
            yield from iter_entity_refs(value, child)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from iter_entity_refs(item, f"{path}[{i}]")
