"""Resolution of dismech entity references (the ``[<file>:]<kind>#<name>`` grammar).

Several slots point at another object *inside the same entry* using a
hash-anchor grammar the schema documents on ``Discussion.attaches_to``::

    [<file>:]<kind>#<name>

    pathophysiology#Amyloid Plaque Formation
    phenotypes#Memory Loss
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
* ``mechanistic_hypotheses#`` resolves against ``hypothesis_group_id``, not
  ``name`` (``MechanisticHypothesis`` has no ``name`` slot).
* ``prevalence#`` resolves against ``population``, likewise.

``<kind>`` is the schema slot name of the section referred to. Curated content
used to drift between singular and plural spellings of the same section; it was
normalised to the slot-name form in issue #9394, so that a reference's prefix is
derivable from the schema rather than from this map, and so that grepping for
``phenotypes#`` finds every phenotype reference. The singular aliases are kept
here and still resolve — an entry written before the normalisation, or by hand
today, is not a defect.

A reference may also name a **whole section** by leaving the anchor empty::

    clinical_burden#          # the ClinicalBurden object, not a node within it

This exists because not every referenceable thing has a name to anchor to.
``clinical_burden`` is a singleton inlined object with no ``name`` slot, so
there is nothing to put on the right of the ``#`` — and writing the bare word
``clinical_burden`` instead would be indistinguishable from a node that happens
to be called that. The empty anchor keeps every reference matching
``<kind>#<name>``, which is what lets the grammar be checked at all.

**A whole-section reference resolves on the section name, not its contents.**
``treatments#`` is satisfied by ``treatments`` being a real section, even in an
entry that curates none — because the case that motivates it is a
``KNOWLEDGE_GAP`` attached to a section precisely *because* it is empty
(``Spondyloepimetaphyseal_Dysplasia_Bieganski_Type`` records that no
disease-specific management is established, and has no ``treatments:`` block at
all). Requiring content would make the gap impossible to attach exactly when it
matters most. The check that remains is still worth having: it catches a
misspelled or invented section name.

An unknown prefix, or a cross-file reference, yields ``None`` — "no opinion" —
rather than a failure, so a gap in :data:`SECTION_KEYS` can never be mistaken
for a broken reference in the knowledge base.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any, NamedTuple

__all__ = [
    "DISEASE_KIND",
    "KNOWN_KIND_SLOTS",
    "REFERENCE_ONLY_SLOTS",
    "REF_SLOTS",
    "SECTION_KEYS",
    "SINGLETON_SECTIONS",
    "EntityRef",
    "EntityRefSite",
    "canonical_kind",
    "entity_ref_errors",
    "entity_ref_index",
    "iter_entity_refs",
    "parse_entity_ref",
    "resolve_entity_ref",
    "section_items",
]


class EntityRefSite(NamedTuple):
    """Where a reference was found: its dotted ``path``, the ``slot`` holding
    it, and the raw ``ref`` value.

    ``slot`` is carried explicitly so callers can key on it without parsing it
    back out of ``path`` — a gate that recovers the slot by string surgery
    stops firing silently the day the path format changes.
    """

    path: str
    slot: str
    ref: str


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

#: Slots that are a single inlined object rather than a list, so a reference to
#: one can only ever be the whole-section form ``<slot>#``. They carry no
#: ``name``, which is why the empty anchor exists.
SINGLETON_SECTIONS: frozenset[str] = frozenset({"clinical_burden"})

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
    # --- Grouping sections -------------------------------------------------
    # Groupings carry `discussions` like Disease entries do, so a discussion in
    # a grouping needs somewhere to attach. `members` is the only section a
    # membership argument can point at, and GroupingMember names its target in
    # `member` rather than `name`.
    "member": ("members", ("member",)),
    "members": ("members", ("member",)),
}

#: Slots whose values carry the hash-anchor grammar. ``target`` is multivalued
#: in neither of its two homes but *is* also used by ``ModelMechanismLink`` and
#: ``target_mechanisms`` for plain node names, so a ``target`` without a ``#``
#: is simply not an entity reference and is skipped by the parser.
REF_SLOTS: frozenset[str] = frozenset(
    {"attaches_to", "would_support", "would_refute", "target"}
)

#: Ref-bearing slot -> the slot a prose *outcome* belongs in instead (#9224).
#:
#: ``Experiment.would_support`` / ``would_refute`` name *what a result bears
#: on*; ``supporting_outcome`` / ``refuting_outcome`` state *what would be
#: observed*. Both pairs are multivalued strings, so nothing in the schema
#: stops a sentence being written into the reference slot, and ~51 were before
#: the two prose slots existed. The distinction is not stylistic: an anchor
#: names a referent and resolves to a card on the page, while a sentence like
#: "No enrichment of these lesions in tissue would indicate that ..." is a
#: conditional inference with no referent to resolve, and rendered as a
#: reference chip it becomes a monospace block.
#:
#: ``attaches_to`` is absent because it has no prose sibling -- a bare name
#: there is a mis-written reference, not a misfiled outcome.
REFERENCE_ONLY_SLOTS: dict[str, str] = {
    "would_support": "supporting_outcome",
    "would_refute": "refuting_outcome",
}

#: Slots where an unrecognised ``<kind>`` is an error rather than a gap in
#: `SECTION_KEYS`. The resolver skips an unmapped prefix by design -- right for
#: a section this repo genuinely has not mapped, but it also let a typo like
#: `pathophys#Node A` through every check. `target` stays out: it carries plain
#: node names in `ModelMechanismLink` and `target_mechanisms`, and its 8
#: unknown-kind values in `kb/` (`gene#`, `biological_process#`) look like real
#: missing `SECTION_KEYS` entries rather than typos.
KNOWN_KIND_SLOTS = frozenset(REFERENCE_ONLY_SLOTS) | {"attaches_to"}


def canonical_kind(kind: str) -> str:
    """The schema-slot spelling of ``kind``, or ``kind`` unchanged.

    ``SECTION_KEYS`` accepts a singular alias beside most section slots
    (``phenotype#`` beside ``phenotypes#``), because curated content grew both.
    The canonical spelling is the schema slot itself: it makes a reference's
    prefix derivable from the schema rather than from this map, and it makes
    ``phenotypes#`` a grep that actually finds every phenotype reference. The KB
    was normalised to it in issue #9394; the aliases still resolve.

    ``disease#`` is a virtual anchor for the whole entry rather than a section,
    and an unmapped prefix is not ours to rename, so both are returned as-is.
    """
    slot = SECTION_KEYS.get(kind, (kind,))[0]
    return slot if slot in SECTION_KEYS else kind


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
        # `disease#` with an empty anchor means the entry as a whole, same as
        # naming it; `disease#<name>` must match that name.
        return not parsed.name or parsed.name == data.get("name")
    if parsed.kind in SINGLETON_SECTIONS:
        # No name to anchor to, so only the whole-section form is meaningful.
        return not parsed.name
    mapping = SECTION_KEYS.get(parsed.kind)
    if mapping is None:
        return None
    slot, key_slots = mapping
    if not parsed.name:
        # Whole-section reference: resolves on the section *name*. See the
        # module docstring -- an empty section is the motivating case, so
        # requiring content here would defeat the purpose.
        return True
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


def iter_entity_refs(node: Any, path: str = "") -> Iterator[EntityRefSite]:
    """Walk a loaded entry, yielding an :class:`EntityRefSite` per reference slot.

    ``path`` is a dotted/indexed location such as
    ``discussions[2].attaches_to[0]``, for error messages that point straight
    at the offending line's neighbourhood; ``slot`` is the ref-bearing slot
    name, carried separately so callers never have to parse it back out.
    """
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}" if path else str(key)
            if key in REF_SLOTS:
                if isinstance(value, str):
                    yield EntityRefSite(child, key, value)
                    continue
                if isinstance(value, list):
                    # Yield the strings *and* walk anything else, in one pass:
                    # a mixed list must not lose either half.
                    for i, item in enumerate(value):
                        if isinstance(item, str):
                            yield EntityRefSite(f"{child}[{i}]", key, item)
                        else:
                            yield from iter_entity_refs(item, f"{child}[{i}]")
                    continue
                # A ref slot holding an object. None does today, but `target`
                # is the likeliest to start -- it is shared with
                # ModelMechanismLink and target_mechanisms -- so keep walking
                # rather than silently stopping, and references underneath it
                # are still found.
            yield from iter_entity_refs(value, child)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from iter_entity_refs(item, f"{path}[{i}]")


def _abbrev(value: str, limit: int = 60) -> str:
    """Shorten a value for an error message, so a 40-word sentence stays one line."""
    text = " ".join(str(value).split())
    return text if len(text) <= limit else text[: limit - 1] + "\u2026"


def _is_known_kind(kind: str) -> bool:
    """Whether `<kind>` names something this repo can resolve a reference against.

    `SECTION_KEYS` holds the singular aliases as keys in their own right, so
    there is nothing to normalise here -- `canonical_kind` is what
    `test_entity_ref_prefixes_are_schema_slot_names` uses to insist on the
    canonical *spelling*, which is a different question from whether the
    section is one we know at all.
    """
    return kind == DISEASE_KIND or kind in SECTION_KEYS or kind in SINGLETON_SECTIONS


def entity_ref_errors(data: dict) -> list[str]:
    """Every entity-reference problem in one loaded entry.

    The single implementation of the rules, so the pytest sweep
    (``test_entity_ref_foreign_keys``) and the ungated CI check
    (``scripts/check_entity_refs.py``) cannot drift apart -- two copies of a
    rule eventually disagree, which is the argument this module was created
    on (#9193).

    Messages name the dotted path within the document rather than a file, so a
    caller can prefix whatever locator it has. Returns an empty list for an
    entry with no problems; a non-dict is not an entry and yields nothing.
    """
    if not isinstance(data, dict):
        return []
    errors: list[str] = []
    item_names = {ref.split("#", 1)[1] for ref in entity_ref_index(data)}
    for site in iter_entity_refs(data):
        parsed = parse_entity_ref(site.ref)
        if parsed is None:
            if site.slot not in KNOWN_KIND_SLOTS:
                # `target` carries plain node names in its other homes, so a
                # value without a `#` there is simply not a reference.
                continue
            if site.slot == "attaches_to" or site.ref in item_names:
                # A value naming a real item is a reference missing its
                # prefix, not a misfiled outcome -- telling a curator to move
                # it into the prose slot would undo a working pointer.
                errors.append(
                    f"{site.path}={_abbrev(site.ref)!r} is a bare name, not a "
                    f"<kind>#<name> entity reference"
                )
            else:
                errors.append(
                    f"{site.path}={_abbrev(site.ref)!r} is prose, not a "
                    f"<kind>#<name> entity reference; a statement of what "
                    f"would be observed belongs in "
                    f"`{REFERENCE_ONLY_SLOTS[site.slot]}`"
                )
            continue
        if site.slot in KNOWN_KIND_SLOTS and not _is_known_kind(parsed.kind):
            fix = (
                f", or put a prose outcome in `{REFERENCE_ONLY_SLOTS[site.slot]}`"
                if site.slot in REFERENCE_ONLY_SLOTS
                else ""
            )
            errors.append(
                f"{site.path}={_abbrev(site.ref)!r} uses the unknown section "
                f"{parsed.kind + '#'!r}; use a section in `SECTION_KEYS`{fix}"
            )
            continue
        if resolve_entity_ref(data, site.ref) is False:
            errors.append(
                f"{site.path}={site.ref!r} does not resolve to a {parsed.kind}"
            )
    return errors
