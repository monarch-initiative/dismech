"""A coarse HPO binding must say why, and the reason must be checkable.

`HP:0000478` "Abnormality of the eye" is a facet bucket, not a finding, and a
phenotype bound to it passes every other gate in the repo. Three legitimate
reasons for such a binding exist and the KB already records all three as prose
nothing can read; the guard turns them into `coarse_binding_basis` so that the
*unexplained* binding is the only thing that fails.

These tests pin two things the design depends on and that a later refactor could
quietly lose:

* the coarse set is the schema's `PhenotypeCategoryEnum` meanings, not a depth
  or information-content computation — so `HP:0001627` "Abnormal heart
  morphology" (which carries "Congenital heart defect" as an EXACT synonym) is
  *not* coarse, however shallow it looks;
* each basis has a companion requirement, and those are never grandfathered,
  because a declared basis can only come from content written after the slot
  existed.
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


def test_the_coarse_set_is_the_facet_vocabulary():
    """One source of truth: the enum that also drives the UI facets.

    If these drift apart, the guard starts flagging terms the browser does not
    treat as organ systems, and the "it is just the facet list" justification
    for the whole design stops being true.
    """
    from dismech.export.browser_export import HPO_TOP_LEVEL_CATEGORIES

    assert set(COARSE) == set(HPO_TOP_LEVEL_CATEGORIES)
    assert "HP:0000478" in COARSE


def test_shallow_but_clinically_real_terms_are_not_coarse():
    """The anti-IC test.

    `HP:0001627` sits one tier below a facet root and is the correct binding for
    a paper that says only "congenital heart defect" — it carries that as an
    EXACT synonym. `HP:0004322` Short stature is the most-used HP term in the
    KB. Any depth or information-content rule would flag both, and pressure
    curators into asserting a lesion their source never named.
    """
    assert "HP:0001627" not in COARSE
    assert "HP:0004322" not in COARSE
    assert _kinds(_pheno("HP:0001627", "Abnormal heart morphology")) == []


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


def test_spectrum_summary_needs_at_least_two_bound_terms():
    """One finding is not a spectrum — bind that finding instead."""
    data = _pheno(
        "HP:0000478",
        "Abnormality of the eye",
        coarse_binding_basis="SPECTRUM_SUMMARY",
        spectrum_terms=[{"term": {"id": "HP:0000486", "label": "Strabismus"}}],
    )
    kinds = _kinds(data)
    assert [k for k, _ in kinds] == ["companion"]
    assert "found 1" in kinds[0][1]


def test_spectrum_summary_with_real_constituents_passes():
    data = _pheno(
        "HP:0000478",
        "Abnormality of the eye",
        coarse_binding_basis="SPECTRUM_SUMMARY",
        spectrum_terms=[
            {"term": {"id": "HP:0000486", "label": "Strabismus"}},
            {"term": {"id": "HP:0000545", "label": "Myopia"}},
        ],
    )
    assert _kinds(data) == []


def test_a_spectrum_of_coarse_terms_defeats_the_purpose():
    data = _pheno(
        "HP:0000478",
        "Abnormality of the eye",
        coarse_binding_basis="SPECTRUM_SUMMARY",
        spectrum_terms=[
            {"term": {"id": "HP:0000707", "label": "Abnormality of the nervous system"}},
            {"term": {"id": "HP:0000486", "label": "Strabismus"}},
            {"term": {"id": "HP:0000545", "label": "Myopia"}},
        ],
    )
    assert any("itself a top-level term" in d for _, d in _kinds(data))


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


def test_a_hub_with_a_frequency_is_a_spectrum_summary():
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


def test_hub_constituents_use_spectrum_terms_not_causal_edges():
    """The correction that matters: hub -> finding is subsumption, not causation.

    `sequelae` is a CausalEdge. A coloboma is not *caused by* an eye
    abnormality, it *is* one — so requiring outgoing edges would have had
    curators drawing an is-a hierarchy as a causal chain to satisfy a guard.
    A hub may name its constituents, and `spectrum_terms` asserts no causation.
    """
    data = _with_mechanism(
        _pheno(
            "HP:0000478",
            "Abnormality of the eye",
            name="Ocular abnormalities",
            coarse_binding_basis="PATHOGRAPH_HUB",
            spectrum_terms=[
                {"term": {"id": "HP:0000589", "label": "Coloboma"}},
                {"term": {"id": "HP:0000568", "label": "Microphthalmia"}},
            ],
        ),
        "Ocular abnormalities",
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
    stray_spectrum = _pheno(
        "HP:0000589",
        "Coloboma",
        coarse_binding_basis="SOURCE_UNSPECIFIED",
        spectrum_terms=[{"term": {"id": "HP:0000486", "label": "Strabismus"}}],
    )
    assert any("spectrum_terms names the specific" in d for _, d in _kinds(stray_spectrum))

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
        coarse_binding_basis="SPECTRUM_SUMMARY",
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
    """
    rows = [
        line
        for line in BASELINE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]
    assert len(rows) <= 164, (
        f"{len(rows)} grandfathered coarse bindings — the baseline may only shrink. "
        "If a new coarse binding is genuinely right, give it a coarse_binding_basis "
        "rather than adding a row here."
    )
