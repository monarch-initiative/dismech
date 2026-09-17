"""A coarse HPO binding must say why, and the reason must be checkable.

`HP:0000478` "Abnormality of the eye" is a facet bucket, not a finding, and a
phenotype bound to it passes every other gate in the repo. Three legitimate
reasons for such a binding exist and the KB already records all three as prose
nothing can read; the guard turns them into `coarse_binding_basis` so that the
*unexplained* binding is the only thing that fails.

These tests pin three things the design depends on and that a later refactor
could quietly lose:

* the coarse set is the schema's `PhenotypeCategoryEnum` meanings, not a depth
  or information-content computation — so `HP:0001627` "Abnormal heart
  morphology" (which carries "Congenital heart defect" as an EXACT synonym) is
  *not* coarse, however shallow it looks;
* two of the four values take no companion at all. The guard asks a curator to
  state a reason, not to do extra work to prove it;
* where a companion *is* required it is never grandfathered, because a declared
  basis can only come from content written after the slot existed.

A `spectrum_terms` slot for listing a variable spectrum's constituents inside
the binding was built and removed. It inverted the value's meaning — requiring
enumeration in the one case where enumeration is impossible — and where the
findings *are* known and evidenced they are ordinary `phenotypes` entries, which
the phenotype table, the facets and the exports can all see. The last test here
keeps it from coming back.
"""

import subprocess
import sys
from pathlib import Path

# Inline the path rather than assigning ROOT first: ruff's E402 allows an
# import preceded by a `sys.path` preamble, but an intervening assignment
# breaks that allowance (see tests/test_causal_targets.py).
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_coarse_phenotypes import find_in, load_coarse_terms

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_coarse_phenotypes.py"
BASELINE = ROOT / "tests" / "coarse_phenotype_baseline.txt"

COARSE = load_coarse_terms()


def _pheno(term_id, label, **descriptor):
    """One phenotypes[] entry, with descriptor keys split from entry keys."""
    entry_keys = {"name", "frequency", "sequelae", "evidence", "description"}
    entry = {"name": descriptor.pop("name", "A phenotype")}
    for key in list(descriptor):
        if key in entry_keys:
            entry[key] = descriptor.pop(key)
    entry["phenotype_term"] = {"term": {"id": term_id, "label": label}, **descriptor}
    return {"phenotypes": [entry]}


def _kinds(data):
    return [(f.kind, f.detail) for f in find_in(data, "x.yaml", COARSE)]


def test_the_coarse_set_contains_the_facet_vocabulary():
    """Tier 0 is the enum that also drives the UI facets.

    If these drift apart the guard starts flagging terms the browser does not
    treat as organ systems, and the "it is just the facet list" justification
    for tier 0 stops being true. Tier 1 is curated separately, so the facet set
    is a subset now rather than the whole thing.
    """
    from dismech.export.browser_export import HPO_TOP_LEVEL_CATEGORIES

    assert set(HPO_TOP_LEVEL_CATEGORIES) <= set(COARSE)
    assert "HP:0000478" in COARSE


def test_tier_one_is_curated_and_disjoint_from_tier_zero():
    """A term in both lists would double-count in the census and means one
    drifted: tier 1 is defined as what sits BELOW the organ-system roots."""
    import sys as _sys

    from check_coarse_phenotypes import (
        CATEGORY_ENUM_PATH,
        COARSE_TERM_ENUM_PATH,
        _meanings,
    )

    assert _sys  # keep the import block readable for ruff
    tier0 = _meanings(CATEGORY_ENUM_PATH, "PhenotypeCategoryEnum")
    tier1 = _meanings(COARSE_TERM_ENUM_PATH, "CoarsePhenotypeTermEnum")
    assert not (tier0.keys() & tier1.keys())
    assert set(COARSE) == tier0.keys() | tier1.keys()
    # The kidney case the maintainer named, and the skeletal bucket beside it.
    assert "HP:0000077" in tier1
    assert "HP:0000924" in tier1


def test_shallow_but_clinically_real_terms_are_not_coarse():
    """The anti-IC test.

    `HP:0001627` sits one tier below a facet root and is the correct binding for
    a paper that says only "congenital heart defect" — it carries that as an
    EXACT synonym. `HP:0004322` Short stature is the most-used HP term in the
    KB. Any depth or information-content rule would flag both, and pressure
    curators into asserting a lesion their source never named.

    The tier-1 pass is what makes this concrete rather than theoretical: it put
    `HP:0000077` Abnormality of the kidney in the coarse list while leaving
    `HP:0001627` and `HP:0001999` out, and both decisions sit one step below the
    same roots. No rule over depth or over the term's name separates them.
    """
    for curie, label in [
        ("HP:0001627", "Abnormal heart morphology"),
        ("HP:0004322", "Short stature"),
        ("HP:0001999", "Abnormal facial shape"),
        ("HP:0012443", "Abnormal brain morphology"),
        ("HP:0012332", "Abnormal autonomic nervous system physiology"),
    ]:
        assert curie not in COARSE, f"{curie} {label} is a finding, not a bucket"
        assert _kinds(_pheno(curie, label)) == []


def test_unexplained_coarse_binding_is_reported():
    findings = _kinds(_pheno("HP:0000478", "Abnormality of the eye"))
    assert [k for k, _ in findings] == ["missing_basis"]


def test_any_declared_basis_clears_the_missing_finding():
    data = _pheno(
        "HP:0000478",
        "Abnormality of the eye",
        coarse_binding_basis="SOURCE_UNSPECIFIED",
    )
    assert _kinds(data) == []


def test_variable_spectrum_is_a_bare_declaration():
    """The value the maintainer actually asked for.

    A spectrum is the case where the findings are "a little bit random and not
    all over the place" — so requiring a list of them, as the first
    implementation did, asks for exactly what is unavailable. Stating the reason
    is the whole obligation.
    """
    data = _pheno(
        "HP:0000478",
        "Abnormality of the eye",
        coarse_binding_basis="VARIABLE_SPECTRUM",
    )
    assert _kinds(data) == []


def test_no_hpo_term_must_actually_claim_something_narrower():
    """A preferred_term echoing the label claims nothing the binding lost."""
    data = _pheno(
        "HP:0000478",
        "Abnormality of the eye",
        preferred_term="Abnormality of the eye",
        coarse_binding_basis="NO_HPO_TERM",
    )
    assert any("echoes the bound label" in d for _, d in _kinds(data))

    narrower = _pheno(
        "HP:0000478",
        "Abnormality of the eye",
        preferred_term="peripapillary retinal pigment mottling",
        coarse_binding_basis="NO_HPO_TERM",
    )
    assert _kinds(narrower) == []


def _with_mechanism(data, target):
    """Give an entry a pathophysiology node whose edge lands on `target`."""
    data["pathophysiology"] = [
        {"name": "Disrupted neural crest migration", "downstream": [{"target": target}]}
    ]
    return data


def test_pathograph_hub_is_defined_by_incoming_edges():
    """A hub is a convergence point, so something must lead to it.

    Every coarse binding in the KB today is a terminal node — the graph ends at
    "eye". A hub is the opposite end of that: a node a mechanism reaches, which
    is what makes it internal to the pathograph rather than a lazy leaf.
    """
    unreached = _pheno(
        "HP:0000478",
        "Abnormality of the eye",
        name="Ocular abnormalities",
        coarse_binding_basis="PATHOGRAPH_HUB",
    )
    assert any("no causal edge in this entry targets" in d for _, d in _kinds(unreached))

    hub = _with_mechanism(
        _pheno(
            "HP:0000478",
            "Abnormality of the eye",
            name="Ocular abnormalities",
            coarse_binding_basis="PATHOGRAPH_HUB",
        ),
        "Ocular abnormalities",
    )
    assert _kinds(hub) == []


def test_a_hub_with_a_frequency_is_a_variable_spectrum():
    """Frequency is a claim about patients; a hub makes none."""
    data = _with_mechanism(
        _pheno(
            "HP:0000478",
            "Abnormality of the eye",
            name="Ocular abnormalities",
            coarse_binding_basis="PATHOGRAPH_HUB",
            frequency="FREQUENT",
        ),
        "Ocular abnormalities",
    )
    assert any("no clinical claim of its own" in d for _, d in _kinds(data))


def test_a_node_pointing_at_itself_does_not_make_it_a_hub():
    data = _pheno(
        "HP:0000478",
        "Abnormality of the eye",
        name="Ocular abnormalities",
        coarse_binding_basis="PATHOGRAPH_HUB",
        sequelae=[{"target": "Ocular abnormalities"}],
    )
    assert any("no causal edge in this entry targets" in d for _, d in _kinds(data))


def test_a_hub_is_not_required_to_point_at_its_constituents():
    """The correction that matters: hub -> finding is subsumption, not causation.

    `sequelae` is a CausalEdge. A coloboma is not *caused by* an eye
    abnormality, it *is* one — so requiring outgoing edges would have had
    curators drawing an is-a hierarchy as a causal chain to satisfy a guard.
    A hub reached by a mechanism is complete on its own; its constituents, where
    they are known, are ordinary phenotype entries beside it.
    """
    data = _with_mechanism(
        _pheno(
            "HP:0000478",
            "Abnormality of the eye",
            name="Ocular abnormalities",
            coarse_binding_basis="PATHOGRAPH_HUB",
        ),
        "Ocular abnormalities",
    )
    data["phenotypes"].append(
        {
            "name": "Coloboma",
            "phenotype_term": {"term": {"id": "HP:0000589", "label": "Coloboma"}},
        }
    )
    assert _kinds(data) == []


def test_hub_is_rejected_where_sequelae_cannot_exist():
    """`target_phenotypes` has no edges to carry, so a hub there is a mistake."""
    data = {
        "clinical_trials": [
            {
                "name": "NCT00000000",
                "target_phenotypes": [
                    {
                        "term": {"id": "HP:0000478", "label": "Abnormality of the eye"},
                        "coarse_binding_basis": "PATHOGRAPH_HUB",
                    }
                ],
            }
        ]
    }
    assert any("belongs on a phenotypes[] entry" in d for _, d in _kinds(data))


def test_companion_slots_without_their_basis_are_findings():
    stray_gap = _pheno(
        "HP:0000589",
        "Coloboma",
        coarse_binding_basis="SOURCE_UNSPECIFIED",
        term_gap="https://example.invalid/issues/1",
    )
    assert any("term_gap records" in d for _, d in _kinds(stray_gap))


def test_companion_rules_apply_outside_the_coarse_subset():
    """So a curator can declare a basis on a second-tier term without it going
    unchecked, before anyone decides whether to widen the subset."""
    data = _pheno(
        "HP:0000924",
        "Abnormality of the skeletal system",
        preferred_term="Abnormality of the skeletal system",
        coarse_binding_basis="NO_HPO_TERM",
    )
    assert [k for k, _ in _kinds(data)] == ["companion"]


def test_nested_descriptors_are_reached():
    """Coarse bindings hide in subtypes and trial targets, not just phenotypes[]."""
    data = {
        "has_subtypes": [
            {
                "name": "Type 1",
                "phenotypes": [
                    {
                        "name": "Eye findings",
                        "phenotype_term": {
                            "term": {"id": "HP:0000478", "label": "Abnormality of the eye"}
                        },
                    }
                ],
            }
        ]
    }
    assert [k for k, _ in _kinds(data)] == ["missing_basis"]


def test_update_baseline_refuses_to_be_scoped_to_paths():
    """`write_baseline` records only what was scanned, so a scoped rewrite would
    truncate the committed backlog to that subset."""
    before = BASELINE.read_bytes()
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--update-baseline", "kb/disorders/Asthma.yaml"],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode != 0
    assert "cannot be scoped" in result.stderr
    assert BASELINE.read_bytes() == before


def test_committed_kb_has_no_new_unexplained_bindings():
    """The gate itself, over the real KB."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_baseline_only_shrinks():
    """The backlog is a ratchet.

    Nothing enforces this mechanically — a PR can always regenerate the file —
    so the guard is that the committed size is asserted here, and raising it
    means editing this number in the same diff, in front of a reviewer.

    It has been raised twice, both times for a reason that is not a curation
    PR admitting its own defect:

    - 164 -> 341 when the coarse set itself was widened with tier 1, in one
      reviewed pass over all 360 distinct `Abnormal*` terms bound in the KB.
    - 331 -> 386 when this branch was rebased onto a main that had moved 826
      commits. The baseline is a snapshot of the pre-existing backlog taken at
      the moment the guard lands, so refreshing the branch retakes the
      snapshot: 35 disorder entries curated in the meantime, and 10 existing
      entries, carry 58 bindings that predate the guard, against 3 that main's
      curators rebound to narrower terms. None came from this branch. The rate
      is the argument for landing the guard rather than for widening it again.
    """
    rows = [
        line
        for line in BASELINE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]
    assert len(rows) <= 386, (
        f"{len(rows)} grandfathered coarse bindings — the baseline may only shrink. "
        "The two exceptions on record are a deliberate widening of the coarse set "
        "and a refresh onto a moved main; both are argued in this test's docstring. "
        "If a new coarse binding is genuinely right, give it a coarse_binding_basis "
        "rather than adding a row here."
    )


def test_the_schema_has_no_slot_for_listing_a_spectrum():
    """Removed deliberately; do not reintroduce it.

    A slot holding the constituent findings inside a coarse binding produces
    second-class annotations: not in the phenotype table, not in the browser
    facets, not in the exports, and not reachable by a `phenotypes#` entity
    reference. Every finding worth recording is worth an ordinary `phenotypes`
    entry with its own term and its own evidence — and if it has neither, it was
    not evidenced in the first place.
    """
    import yaml

    schema = yaml.safe_load(
        (ROOT / "src" / "dismech" / "schema" / "dismech.yaml").read_text(encoding="utf-8")
    )
    assert "spectrum_terms" not in schema["slots"]
    assert schema["classes"]["PhenotypeDescriptor"]["slots"] == [
        "coarse_binding_basis",
        "term_gap",
    ]
