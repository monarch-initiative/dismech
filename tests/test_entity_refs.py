"""Unit tests for the entity-reference resolver (issue #9193).

`tests/test_data.py::test_entity_ref_foreign_keys` exercises this against real
content; these cover the resolution rules themselves — in particular the three
sections that are *not* keyed on `name`, and the two ways a reference is
skipped rather than failed.
"""

import json
import pathlib
import re

import pytest
import yaml

from dismech import render
from dismech.entity_refs import (
    DISEASE_KIND,
    SECTION_KEYS,
    SINGLETON_SECTIONS,
    EntityRef,
    canonical_kind,
    entity_ref_errors,
    entity_ref_index,
    iter_entity_refs,
    parse_entity_ref,
    resolve_entity_ref,
    section_items,
)

ENTRY = {
    "name": "Test Disease",
    "pathophysiology": [{"name": "Node A"}, {"name": "Node B"}],
    "phenotypes": [{"name": "Pheno A"}],
    "treatments": [{"name": "Drug A"}],
    "genetic": [{"name": "GENE1", "variants": [{"name": "Nested Variant"}]}],
    "variants": [{"name": "Top Variant"}],
    "mechanistic_hypotheses": [
        {"hypothesis_group_id": "canonical_model", "hypothesis_label": "Canonical"}
    ],
    "prevalence": [{"population": "Worldwide"}],
    "progression": [{"phase": "Chronic phase"}],
    "datasets": [{"accession": "geo:GSE1", "title": "A dataset"}],
    "animal_models": [{"species": "Mus musculus", "genotype": "Foo-/-"}],
    "discussions": [{"discussion_id": "gap_one"}],
    "clinical_burden": {"burden_level": "SEVERE"},
}


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("pathophysiology#Node A", EntityRef(None, "pathophysiology", "Node A")),
        (
            "Liver_Cirrhosis:pathophysiology#Hepatic Stellate Cell Activation",
            EntityRef(
                "Liver_Cirrhosis",
                "pathophysiology",
                "Hepatic Stellate Cell Activation",
            ),
        ),
        # A name may itself contain a '#'; only the first splits.
        ("phenotype#Grade #2", EntityRef(None, "phenotype", "Grade #2")),
    ],
)
def test_parse_entity_ref(raw, expected):
    assert parse_entity_ref(raw) == expected


@pytest.mark.parametrize("raw", ["Node A", "", None, 42, "#orphan"])
def test_parse_rejects_non_references(raw):
    """A `target:` carrying a plain node name is not an entity reference."""
    assert parse_entity_ref(raw) is None


@pytest.mark.parametrize(
    "ref",
    [
        "pathophysiology#Node A",
        "phenotype#Pheno A",
        "phenotypes#Pheno A",  # both spellings resolve
        "treatment#Drug A",
        "treatments#Drug A",
        "genetic#GENE1",
        "disease#Test Disease",  # virtual whole-entry anchor
        "mechanistic_hypothesis#canonical_model",  # keyed on hypothesis_group_id
        "mechanistic_hypothesis#Canonical",  # ...and on the human-readable label
        "prevalence#Worldwide",  # keyed on population
        "progression#Chronic phase",  # keyed on phase
        "dataset#geo:GSE1",  # keyed on accession
        "dataset#A dataset",  # ...or title
        "animal_models#Mus musculus",  # unnamed model, keyed on species
        "animal_models#Foo-/-",
        "discussion#gap_one",
        "variant#Top Variant",
        "variant#Nested Variant",  # nested under genetic[].variants
    ],
)
def test_resolves(ref):
    assert resolve_entity_ref(ENTRY, ref) is True


@pytest.mark.parametrize(
    "ref",
    [
        "pathophysiology#Node C",
        "phenotypes#Nope",
        "disease#Other Disease",
        "mechanistic_hypothesis#other_model",
        "prevalence#Elsewhere",
        # A section absent from the entry dangles rather than being skipped.
        "biochemical#Anything",
    ],
)
def test_dangles(ref):
    assert resolve_entity_ref(ENTRY, ref) is False


@pytest.mark.parametrize(
    "ref",
    [
        "Liver_Cirrhosis:pathophysiology#Hepatic Stellate Cell Activation",
        "gene#LRRK2",  # prefix absent from SECTION_KEYS
        "biological_process#tRNA processing",
        "Node A",  # not a reference at all
    ],
)
def test_skipped_never_fails(ref):
    """An unmapped prefix is a gap in the map, not a defect in the content."""
    assert resolve_entity_ref(ENTRY, ref) is None


def test_section_items_merges_nested_variants():
    names = {v["name"] for v in section_items(ENTRY, "variants")}
    assert names == {"Top Variant", "Nested Variant"}
    assert [n["name"] for n in section_items(ENTRY, "pathophysiology")] == [
        "Node A",
        "Node B",
    ]
    assert section_items(ENTRY, "clinical_trials") == []


def test_entity_ref_index_covers_every_resolvable_ref():
    index = entity_ref_index(ENTRY)
    assert index["disease#Test Disease"] == [ENTRY]
    assert index["pathophysiology#Node A"] == [ENTRY["pathophysiology"][0]]
    # Every key the index emits must also resolve, and vice versa.
    for key in index:
        assert resolve_entity_ref(ENTRY, key) is True


def test_iter_entity_refs_reports_paths():
    doc = {
        "discussions": [
            {
                "attaches_to": ["pathophysiology#Node A", "phenotype#Pheno A"],
                "proposed_experiments": [
                    {
                        "would_support": ["pathophysiology#Node B"],
                        "would_refute": ["pathophysiology#Node C"],
                        "perturbations": [{"target": "genetic#GENE1"}],
                        "readouts": [{"target": "Plain node name"}],
                    }
                ],
            }
        ],
        # `target` on a model link carries a plain name, not a reference.
        "animal_models": [{"modeled_mechanisms": [{"target": "Node A"}]}],
    }
    found = {site.path: site.ref for site in iter_entity_refs(doc)}
    assert found["discussions[0].attaches_to[0]"] == "pathophysiology#Node A"
    assert found["discussions[0].attaches_to[1]"] == "phenotype#Pheno A"
    assert (
        found["discussions[0].proposed_experiments[0].would_refute[0]"]
        == "pathophysiology#Node C"
    )
    assert (
        found["discussions[0].proposed_experiments[0].perturbations[0].target"]
        == "genetic#GENE1"
    )
    # Plain-name targets are yielded but parse to None, so they never fail.
    assert (
        parse_entity_ref(found["animal_models[0].modeled_mechanisms[0].target"]) is None
    )


def test_section_keys_point_at_real_disease_slots():
    """Every mapped section must name a slot the Disease class actually has.

    Covers `SINGLETON_SECTIONS` too: a typo there resolves to `None` and is
    silently skipped rather than failing, so nothing else would catch it.
    """
    schema = yaml.safe_load(open("src/dismech/schema/dismech.yaml"))
    disease_slots = set(schema["classes"]["Disease"]["slots"])
    for kind, (slot, key_slots) in SECTION_KEYS.items():
        assert slot in disease_slots, f"{kind} -> unknown slot {slot}"
        assert key_slots, kind
    for slot in SINGLETON_SECTIONS:
        assert slot in disease_slots, f"SINGLETON_SECTIONS: unknown slot {slot}"
        # A singleton is a single inlined object, not a list -- that is the
        # whole reason it needs the empty-anchor form.
        assert not schema["slots"][slot].get("multivalued"), slot


@pytest.mark.parametrize(
    "ref",
    [
        "prevalence#",  # the section as a whole, not one population
        "treatments#",
        "clinical_burden#",  # a singleton object with no name to anchor to
        "disease#",  # the entry as a whole
    ],
)
def test_whole_section_anchor_resolves(ref):
    """An empty anchor names the section itself (#9394)."""
    assert resolve_entity_ref(ENTRY, ref) is True


def test_whole_section_anchor_resolves_on_the_name_not_the_contents():
    """A section with no content still satisfies `<section>#`.

    The motivating case is a KNOWLEDGE_GAP attached to a section precisely
    because it is empty — `Spondyloepimetaphyseal_Dysplasia_Bieganski_Type`
    records that no disease-specific management is established and curates no
    `treatments:` at all. Requiring content would make that gap unattachable.
    """
    empty = {"name": "Bare Disease"}
    assert resolve_entity_ref(empty, "treatments#") is True
    assert resolve_entity_ref(empty, "clinical_burden#") is True
    # A misspelled or invented section is still caught — that is what the
    # check is for once contents are not required.
    assert resolve_entity_ref(empty, "treatmnets#") is None


def test_singleton_section_rejects_a_named_anchor():
    """`clinical_burden` has no `name`, so only the whole-section form works."""
    assert resolve_entity_ref(ENTRY, "clinical_burden#Anything") is False


def test_iter_entity_refs_walks_objects_inside_a_ref_slot():
    """A ref slot holding objects, or a mix, loses neither half (#9385 review).

    Every ref slot holds a string or a list of strings today, so this is
    forward-looking — but the two ways of getting it wrong are both silent.
    Stopping at the slot drops references nested underneath it; recursing past
    the whole list drops the plain strings beside them.
    """
    doc = {
        "discussions": [
            {
                "attaches_to": [
                    "pathophysiology#Node A",
                    {"target": "phenotype#Pheno A"},
                    "genetic#GENE1",
                ]
            }
        ],
        "experiments": [{"target": {"nested": {"target": "treatments#Drug A"}}}],
    }
    found = {site.path: site.ref for site in iter_entity_refs(doc)}

    # The strings beside the object survive...
    assert found["discussions[0].attaches_to[0]"] == "pathophysiology#Node A"
    assert found["discussions[0].attaches_to[2]"] == "genetic#GENE1"
    # ...and so does the reference inside it.
    assert found["discussions[0].attaches_to[1].target"] == "phenotype#Pheno A"
    # An object directly under a ref slot is walked rather than stopped at.
    assert found["experiments[0].target.nested.target"] == "treatments#Drug A"


def test_whole_section_link_requires_a_card_to_jump_to():
    """Resolution and linking answer different questions (#9394 review).

    `treatments#` *resolves* in an entry curating no treatments — that is the
    point, since the motivating case is a gap attached to an empty section. But
    the treatments card is only rendered when there is content, so linking there
    would emit an href to an anchor that does not exist on the page. The index
    must therefore be stricter than the resolver.
    """
    with_content = {"name": "D", "treatments": [{"name": "Drug A"}]}
    without = {"name": "D"}

    assert resolve_entity_ref(without, "treatments#") is True  # resolves...
    assert "treatments#" not in render._build_semantic_ref_index(without)  # ...but no link
    assert render._build_semantic_ref_index(with_content)["treatments#"] == "#treatments"


def test_semantic_ref_index_covers_every_annotated_section(tmp_path):
    """Guard the renderer's ordering dependency (#9193 review, suggestion 5).

    `_build_semantic_ref_index` relies on the `_annotate_*` passes having run,
    and silently emits no link for an item without an `_anchor_id` — a quietly
    missing link rather than an error. This runs the same passes
    `render_disorder` does, in the same order, over the two entries the issue
    named as exercising the awkward prefixes, and checks two things: every href
    the index emits is an id the rendered page actually carries — which catches
    breakage from *any* of the passes on these fixtures — and that the seven ref
    kinds listed below are actually exercised rather than silently absent.
    Dropping or reordering a pass fails here rather than quietly losing links.

    The kind list is not one-per-pass: `_annotate_variant_anchors`,
    `_annotate_external_assertion_anchors` and `_annotate_model_links` are
    covered only by the href-resolves assertion, because these two fixtures
    carry no `variant#`, `external_assertions#` or model references to name.
    """
    # HPAH carries inheritance/clinical_trials/genetic; Gorlin carries the
    # hypotheses. Neither has all of them, which is the point of using both.
    sources = [
        "kb/disorders/Heritable_Pulmonary_Arterial_Hypertension.yaml",
        "kb/disorders/Gorlin_Syndrome.yaml",
    ]
    seen_kinds: set[str] = set()

    for name in sources:
        src = pathlib.Path(name)
        disorder = render.load_disorder(src)

        render._annotate_model_links(disorder)
        render._annotate_card_anchors(disorder)
        render._annotate_variant_anchors(disorder)
        render._annotate_external_assertion_anchors(disorder)
        render._annotate_ref_target_anchors(disorder)
        render._annotate_hypothesis_group_links(disorder)
        index = render._build_semantic_ref_index(disorder)

        out = tmp_path / f"{src.stem}.html"
        render.render_disorder(src, out)
        ids = set(re.findall(r'\sid="([^"]+)"', out.read_text()))

        for ref, href in index.items():
            assert href.lstrip("#") in ids, f"{src.stem}: {ref} -> {href} not on page"
            seen_kinds.add(ref.split("#", 1)[0])

    # Kinds these two fixtures do carry, spanning the card-anchor and
    # ref-target passes, the hypothesis pass, and the two the index
    # resolves inline.
    for kind in (
        "pathophysiology",  # inline fallback in the index
        "disease",  # virtual whole-entry anchor, also inline
        "genetic",  # _annotate_card_anchors
        "treatments",  # _annotate_card_anchors
        "inheritance",  # _annotate_ref_target_anchors
        "clinical_trials",  # _annotate_ref_target_anchors
        "mechanistic_hypotheses",  # _annotate_hypothesis_group_links
        # Sections that gained cards in #9505. Both fixtures carry all three,
        # and `diagnosis` alone accounted for 42 of the 69 dead chips.
        "diagnosis",
        "progression",
        "prevalence",
    ):
        assert kind in seen_kinds, f"no semantic-ref index entries for {kind}#"


@pytest.mark.parametrize(
    "source",
    [
        "kb/disorders/Heritable_Pulmonary_Arterial_Hypertension.yaml",
        "kb/disorders/Chagas_Disease.yaml",
        "kb/disorders/Acute_Flaccid_Myelitis.yaml",
    ],
)
def test_no_reference_renders_as_a_dead_chip(tmp_path, source):
    """Every resolvable reference must become a link, not a dead chip (#9505).

    `test_semantic_ref_index_covers_every_annotated_section` checks the
    converse — that each href the index emits exists on the page. It passes
    happily when a whole section is missing from the index, which is exactly
    what happened: the disorder template rendered no card for `diagnosis`,
    `prevalence`, `progression`, `imaging_findings`, `epidemiology`,
    `infectious_agent`, `transmission`, `clinical_burden` or `stages`, so 69
    references across `kb/` resolved as foreign keys and still drew as inert
    grey text.

    These three fixtures between them carry all nine sections.

    The one accepted exception is a *whole-section* reference to a section the
    entry does not have — a KNOWLEDGE_GAP attached to `treatments#` precisely
    *because* nothing is curated there. That resolves (the section is real) but
    has no card to jump to, which `entity_refs` documents as the deliberate
    difference between "is this a real section" and "is there somewhere to go".
    """
    src = pathlib.Path(source)
    disorder = render.load_disorder(src)

    render._annotate_model_links(disorder)
    render._annotate_card_anchors(disorder)
    render._annotate_variant_anchors(disorder)
    render._annotate_external_assertion_anchors(disorder)
    render._annotate_ref_target_anchors(disorder)
    render._annotate_hypothesis_group_links(disorder)
    index = render._build_semantic_ref_index(disorder)

    dead = []
    for site in iter_entity_refs(disorder):
        parsed = parse_entity_ref(site.ref)
        if parsed is None or parsed.file:
            continue
        known = (
            parsed.kind == DISEASE_KIND
            or parsed.kind in SECTION_KEYS
            or parsed.kind in SINGLETON_SECTIONS
        )
        if not known or index.get(site.ref):
            continue
        slot = SECTION_KEYS.get(parsed.kind, (parsed.kind,))[0]
        if not parsed.name and not disorder.get(slot):
            continue  # the documented empty-section case
        dead.append(f"{site.path}={site.ref!r}")

    assert not dead, f"{src.stem}: references with no link target: {dead}"


@pytest.mark.parametrize(
    ("kind", "expected"),
    [
        # The eight aliases the KB actually carried before #9394 normalised it.
        ("phenotype", "phenotypes"),
        ("mechanistic_hypothesis", "mechanistic_hypotheses"),
        ("treatment", "treatments"),
        ("subtype", "has_subtypes"),  # the one that is not a pluralisation
        ("animal_model", "animal_models"),
        ("experimental_model", "experimental_models"),
        ("discussion", "discussions"),
        ("dataset", "datasets"),
        # ...and the three that were accepted but unused.
        ("variant", "variants"),
        ("stage", "stages"),
        ("computational_model", "computational_models"),
        # Already canonical.
        ("phenotypes", "phenotypes"),
        ("pathophysiology", "pathophysiology"),
        # Not ours to rename: the virtual whole-entry anchor, and any prefix
        # missing from SECTION_KEYS (a gap in the map, not a defect).
        ("disease", "disease"),
        ("not_a_section", "not_a_section"),
    ],
)
def test_canonical_kind(kind, expected):
    assert canonical_kind(kind) == expected


def test_canonical_kind_is_idempotent_over_every_mapped_prefix():
    """Canonicalising twice must not move — otherwise the gate that uses this
    could demand a spelling it would then reject on the next run."""
    for kind in SECTION_KEYS:
        once = canonical_kind(kind)
        assert canonical_kind(once) == once
        assert once in SECTION_KEYS, f"{kind} canonicalises to an unresolvable prefix"


def test_aliases_still_resolve_after_normalisation():
    """The KB was normalised, but the aliases are kept resolvable on purpose.

    Nothing outside `kb/` is bound by the canonical spelling, and an entry
    written before #9394 is not a defect. If this ever fails, the back-compat
    half of that decision has been dropped.
    """
    data = {
        "name": "D",
        "phenotypes": [{"name": "Pheno A"}],
        "treatments": [{"name": "Drug A"}],
        "has_subtypes": [{"name": "Type 1"}],
        "mechanistic_hypotheses": [{"hypothesis_group_id": "canonical_model"}],
    }
    for ref in (
        "phenotype#Pheno A",
        "treatment#Drug A",
        "subtype#Type 1",
        "mechanistic_hypothesis#canonical_model",
    ):
        assert resolve_entity_ref(data, ref) is True, ref


def test_jump_to_card_canonicalises_both_sides_of_the_section_comparison(tmp_path):
    """The pathograph's jump-to-card must survive the #9394 normalisation.

    A card advertises its section in the singular (`data-dismech-type=
    "phenotype"`), but a normalised reference carries the schema slot
    (`phenotypes#Name`). Comparing them raw makes the section-preference step
    dead code for every normalised ref: `findCardForNode` falls through to its
    name-only fallback, which returns whichever card matching that name comes
    first in the DOM. That is wrong precisely when the preference matters —
    when one name appears in two sections.

    No live reference hits this today (all 17 refs pointing at a name that
    occurs in two card sections are `pathophysiology#`/`environmental#`, whose
    card type already equals the schema slot, so none was renamed), which is
    exactly why it needs a test rather than a bug report: the first
    `phenotypes#X` written against a name that is also a pathophysiology node
    would jump to the wrong card, silently.
    """
    for src, renderer in (
        ("kb/disorders/Gorlin_Syndrome.yaml", render.render_disorder),
        ("kb/modules/fibrotic_response.yaml", render.render_module),
    ):
        out = tmp_path / (pathlib.Path(src).stem + ".html")
        renderer(pathlib.Path(src), out)
        html = out.read_text()

        match = re.search(r"var KIND_ALIASES = (\{.*?\});", html, re.DOTALL)
        assert match, f"{src}: alias map not rendered"
        aliases = json.loads(match.group(1))
        # Rendered from SECTION_KEYS, so it cannot drift from the resolver.
        assert aliases == {
            kind: canonical_kind(kind)
            for kind in SECTION_KEYS
            if canonical_kind(kind) != kind
        }
        # The section comparison must run both sides through it.
        assert (
            'canonicalKind(el.getAttribute("data-dismech-type"))'
            " === canonicalKind(nodeType)" in html
        ), f"{src}: section comparison is not canonicalised"

        # A card's advertised type must canonicalise onto a real schema slot,
        # or the comparison silently never matches for that section.
        for card_type in set(re.findall(r'data-dismech-type="([^"]+)"', html)):
            assert canonical_kind(card_type) in SECTION_KEYS, card_type


# --- entity_ref_errors: the rules the CI gate and the pytest sweep share ------
#
# These moved here from `tests/test_data.py` with `entity_ref_errors` itself
# (#9473): the function is no longer test-local, since
# `scripts/check_entity_refs.py` is a second caller. They exercise the rules
# against a hand-built entry rather than against whatever `kb/` happens to
# contain -- a gate whose backlog is zero passes just as happily once it has
# stopped firing.

def _experiment_entry(**experiment) -> dict:
    """A minimal entry carrying one proposed experiment, for the checks below."""
    return {
        "name": "Test Disease",
        "pathophysiology": [{"name": "Node A"}],
        "discussions": [
            {
                "discussion_id": "gap_1",
                "kind": "KNOWLEDGE_GAP",
                "attaches_to": ["pathophysiology#Node A"],
                "proposed_experiments": [{"experiment_id": "exp_1", **experiment}],
            }
        ],
    }


def test_would_support_accepts_an_anchor():
    """The intended form: a reference naming the node the result bears on."""
    data = _experiment_entry(
        would_support=["pathophysiology#Node A"],
        would_refute=["disease#Test Disease"],
        supporting_outcome=["Increased apoptosis in patient organoids."],
    )
    assert entity_ref_errors(data) == []


def test_would_support_rejects_prose():
    """A sentence in the reference slot names its prose sibling (#9224).

    This is the ~51-value pattern the two prose slots were added for: a
    conditional inference with no referent, which resolves to nothing and
    renders as a monospace block.
    """
    data = _experiment_entry(
        would_refute=[
            (
                "No enrichment of these lesions in tissue would indicate that the "
                "dominant clinical resistance mechanism lies outside the bypass "
                "lesions currently modeled at this node."
            )
        ]
    )
    errors = entity_ref_errors(data)
    assert len(errors) == 1
    assert "is prose" in errors[0]
    assert "`refuting_outcome`" in errors[0]
    # The quoted value is abbreviated, so one finding stays one line.
    assert "bypass" not in errors[0]


def test_would_support_rejects_a_bare_name_as_a_bare_name():
    """A real node name without its prefix is a mis-written pointer, not prose.

    Reported in review of #9500: sending this to the prose message would have
    a curator move a working pointer into `supporting_outcome`, which is the
    migration this gate exists to prevent, run backwards.
    """
    errors = entity_ref_errors(_experiment_entry(would_support=["Node A"]))
    assert len(errors) == 1
    assert "is a bare name" in errors[0]
    assert "supporting_outcome" not in errors[0]


def test_attaches_to_rejects_an_unknown_section():
    """The same unknown-section hole was open in `attaches_to` (#9500 review)."""
    data = _experiment_entry(would_support=["pathophysiology#Node A"])
    data["discussions"][0]["attaches_to"] = ["pathophys#Node A"]
    errors = entity_ref_errors(data)
    assert len(errors) == 1
    assert "unknown section" in errors[0]
    # `attaches_to` has no prose sibling, so none is suggested.
    assert "prose outcome" not in errors[0]


def test_plain_node_name_in_target_is_not_a_bare_name():
    """`target` carries plain node names by design, in every one of its homes.

    Regression guard: the bare-name rule above matches values that name a real
    item, and every `ModelMechanismLink` / readout `target` in `kb/` does
    exactly that. Applying it there flagged 2,329 files.
    """
    data = _experiment_entry(would_support=["pathophysiology#Node A"])
    data["animal_models"] = [
        {
            "name": "Test mouse",
            "species": "Mus musculus",
            "modeled_mechanisms": [
                {
                    "target": "Node A",
                    "relationship": "RECAPITULATES",
                    "readouts": [{"name": "A readout", "target": "Node A"}],
                }
            ],
        }
    ]
    assert entity_ref_errors(data) == []


def test_would_support_rejects_an_unknown_section():
    """A typo'd or invented prefix is skipped by the resolver, so gate it here."""
    errors = entity_ref_errors(_experiment_entry(would_support=["pathophys#Node A"]))
    assert len(errors) == 1
    assert "unknown section" in errors[0]


def test_would_support_still_gates_a_dangling_anchor():
    """A well-formed reference to a node that does not exist is still a defect."""
    errors = entity_ref_errors(
        _experiment_entry(would_support=["pathophysiology#Node Z"])
    )
    assert len(errors) == 1
    assert "does not resolve" in errors[0]
