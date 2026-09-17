"""The mechanically checkable half of the infectious-disease granularity ladder.

Design decisions §3e (issue #10115) says how finely an infectious disease is
split. Some of its rules are judgement (is this stratum *documented* to differ
on one axis?) and some are not (does this entry name a pathogen at all?). The
script under test draws that line, and what these tests pin is mostly the
line itself: which classes are deterministic and gate under ``--strict``,
which are advisory and never do, and which entries are *out of scope* because
another decision governs them -- an HPV-driven carcinoma is a cancer whose
pathogen is an annotation (rule R23), a post-streptococcal sequela keeps its
own entry on a host-immune mechanism (R22).

The other thing pinned here is the pointer mechanism. A promoted stratum is
supposed to stay in its parent's ``has_subtypes`` as a pointer to the split
file (§3a L4, §3e rung 4), which until ``curated_in`` existed was a sentence
inside a ``description`` that nothing could read -- which is how
``Spotted_Fever_Rickettsiosis`` came to be reported as a defect for doing the
prescribed thing. With the slot, a pointer is informational and an unmarked
duplicate is a finding, and those tests run against the real entry.
"""

from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

# Inline the path rather than assigning ROOT first: ruff's E402 allows an
# import preceded by a `sys.path` preamble, but an intervening assignment
# breaks that allowance (see tests/test_causal_targets.py).
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_granularity import (
    ADVISORY_CLASSES,
    DANGLING_POINTER,
    DETERMINISTIC_CLASSES,
    DOUBLE_MODELLED,
    DUPLICATE_ANCHOR,
    INFORMATIONAL_CLASSES,
    LUMP_RECORDED,
    LUMP_WAIVER_SENTINEL,
    MISSING_AGENT,
    MISSING_LIFECYCLE,
    MISSING_TRANSMISSION,
    NO_PROGRESSION,
    PATHOTYPE_COLLAPSE,
    POINTER,
    POINTER_TERM_MISMATCH,
    ROOT_AS_ENTRY,
    ROOT_TERMS,
    RULE_FOR_CLASS,
    SCOPE_INFECTIOUS,
    SCOPE_MENDELIAN,
    SCOPE_NEOPLASM,
    SCOPE_OTHER,
    SCOPE_SEQUELA,
    SCOPE_TOXICOLOGIC,
    TAXON_LUMP,
    UNBOUND_AGENT,
    UNBOUND_AGENT_STRATUM,
    UNBOUND_SUBTYPE,
    lump_waiver_recorded,
    main,
    scope_of,
)

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_granularity.py"
KB_DIR = ROOT / "kb" / "disorders"


@pytest.fixture(autouse=True)
def _restore_kb_cache_env():
    """Keep ``main()``'s ``kb_cache.default_off()`` inside this test.

    ``default_off()`` belongs in ``main()`` (CLAUDE.md), but it sets a
    process-wide environment variable; without this the parsed-KB cache stays
    disabled for every test that runs after this module in the same process.
    Copied from ``tests/test_disconnected_phenotypes.py``.
    """
    sentinel = object()
    before = os.environ.get("DISMECH_KB_CACHE", sentinel)
    try:
        yield
    finally:
        if before is sentinel:
            os.environ.pop("DISMECH_KB_CACHE", None)
        else:
            os.environ["DISMECH_KB_CACHE"] = before


# --------------------------------------------------------------------------
# A synthetic corpus, one entry per pattern
# --------------------------------------------------------------------------


def _term(curie: str, label: str = "x") -> dict:
    return {"preferred_term": label, "term": {"id": curie, "label": label}}


def _agent(name: str, curie: str | None, strata: list[dict] | None = None) -> dict:
    agent: dict = {"name": name}
    if curie:
        agent["infectious_agent_term"] = _term(curie, name)
    if strata:
        agent["has_subtypes"] = strata
    return agent


WAIVER_LONG = LUMP_WAIVER_SENTINEL + " " + " ".join(f"word{i}" for i in range(20))
WAIVER_SHORT = LUMP_WAIVER_SENTINEL + " " + " ".join(f"word{i}" for i in range(19))

COMPLETE = {
    "transmission": [{"name": "Fecal-oral"}],
    "progression": [{"phase": "Acute infection"}],
    "agent_life_cycle": {"description": "direct"},
}

ENTRIES: dict[str, dict] = {
    # R25 on an entry with nothing: agent, transmission, and progression missing.
    "Alpha_Fever": {
        "name": "Alpha fever",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000101"),
    },
    # Three bound agents, no subtypes, no decision recorded -> the R9 question.
    "Beta_Lump": {
        "name": "Beta lump",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000102"),
        "infectious_agent": [
            _agent("A", "NCBITaxon:11"),
            _agent("B", "NCBITaxon:12"),
            _agent("C", "NCBITaxon:13"),
        ],
        **COMPLETE,
    },
    # Same shape with the lump recorded the way R9 asks.
    "Beta_Lump_Recorded": {
        "name": "Beta lump recorded",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000103"),
        "infectious_agent": [
            _agent("A", "NCBITaxon:11"),
            _agent("B", "NCBITaxon:12"),
            _agent("C", "NCBITaxon:13"),
        ],
        "review_notes": "Some earlier note.\n\n" + WAIVER_LONG,
        **COMPLETE,
    },
    # The sentinel with too little reasoning behind it does not waive.
    "Beta_Lump_Short": {
        "name": "Beta lump short",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000104"),
        "infectious_agent": [
            _agent("A", "NCBITaxon:11"),
            _agent("B", "NCBITaxon:12"),
            _agent("C", "NCBITaxon:13"),
        ],
        "review_notes": WAIVER_SHORT,
        **COMPLETE,
    },
    # The pointer mechanism, all four outcomes on one parent.
    "Gamma_Group": {
        "name": "Gamma group",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000110"),
        "infectious_agent": [_agent("G", "NCBITaxon:20")],
        "has_subtypes": [
            {"name": "GF-A", "subtype_term": _term("MONDO:0000111")},
            {
                "name": "GF-B",
                "subtype_term": _term("MONDO:0000112"),
                "curated_in": "Gamma_Fever_B",
            },
            {"name": "GF-C", "curated_in": "Nonexistent_Entry"},
            {
                "name": "GF-D",
                "subtype_term": _term("MONDO:0000199"),
                "curated_in": "Gamma_Fever_A",
            },
            {"name": "GF-E"},
        ],
        **COMPLETE,
    },
    "Gamma_Fever_A": {
        "name": "Gamma fever A",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000111"),
        "infectious_agent": [_agent("G", "NCBITaxon:20")],
        **COMPLETE,
    },
    "Gamma_Fever_B": {
        "name": "Gamma fever B",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000112"),
        "infectious_agent": [_agent("G", "NCBITaxon:20")],
        **COMPLETE,
    },
    # A subtype that names another entry by name rather than by term.
    "Gamma_Named": {
        "name": "Gamma named",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000113"),
        "infectious_agent": [_agent("G", "NCBITaxon:20")],
        "has_subtypes": [{"name": "Gamma Fever A"}],
        **COMPLETE,
    },
    # Two agents on the same CURIE: pathotypes collapsed onto the species (R15).
    "Delta_Collapse": {
        "name": "Delta collapse",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000120"),
        "infectious_agent": [
            _agent("ETEC", "NCBITaxon:562"),
            _agent("EPEC", "NCBITaxon:562"),
        ],
        **COMPLETE,
    },
    # Anchored to the rung-0 root, with an unbound agent and an unbound stratum.
    "Root_Entry": {
        "name": "Root entry",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0005550", "infectious disease"),
        "infectious_agent": [_agent("Something", None, strata=[{"name": "serovar X"}])],
        **COMPLETE,
    },
    # Two entries on one MONDO term; only the one without a narrowMatch is flagged.
    "Shared_One": {
        "name": "Shared one",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000130"),
        "infectious_agent": [_agent("S", "NCBITaxon:30")],
        **COMPLETE,
    },
    "Shared_Two": {
        "name": "Shared two",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000130"),
        "infectious_agent": [_agent("S", "NCBITaxon:30")],
        "mappings": {
            "mondo_mappings": [
                {
                    "term": {"id": "MONDO:0000130", "label": "x"},
                    "mapping_predicate": "skos:narrowMatch",
                }
            ]
        },
        **COMPLETE,
    },
    # Out of scope by R23: a carcinoma with a viral agent and no transmission.
    "Epsilon_Carcinoma": {
        "name": "Epsilon carcinoma",
        "disease_term": _term("MONDO:0000140"),
        "infectious_agent": [_agent("HPV", "NCBITaxon:40")],
        "has_subtypes": [{"name": "Shared One"}],
    },
    # Out of scope by R22: a post-infectious sequela.
    "Zeta_Sequela": {
        "name": "Zeta valve disease",
        "category": "Complex",
        "parents": ["post-infectious autoimmune disease"],
        "disease_term": _term("MONDO:0000150"),
    },
    # Out of scope: a Mendelian susceptibility disorder with a pathogen block.
    "Eta_Susceptibility": {
        "name": "Eta susceptibility",
        "category": "Mendelian",
        "disease_term": _term("MONDO:0000160"),
        "infectious_agent": [_agent("M", "NCBITaxon:60")],
    },
    # Out of scope: a mycotoxicosis.
    "Theta_Toxicosis": {
        "name": "Theta toxicosis",
        "category": "Toxicologic",
        "disease_term": _term("MONDO:0000170"),
        "infectious_agent": [_agent("Aspergillus", "NCBITaxon:70")],
    },
    # Lifecycle heuristic: a vector word fires, a word containing one does not.
    "Iota_Vector": {
        "name": "Iota vector",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000180"),
        "infectious_agent": [_agent("I", "NCBITaxon:80")],
        "transmission": [{"name": "Tick bite"}],
        "progression": [{"phase": "Acute"}],
    },
    "Kappa_Stick": {
        "name": "Kappa stick",
        "category": "Infectious Disease",
        "disease_term": _term("MONDO:0000181"),
        "infectious_agent": [_agent("K", "NCBITaxon:81")],
        "transmission": [{"description": "Needlestick injury and fomite spread"}],
        "progression": [{"phase": "Acute"}],
    },
    # Not infectious by any signal.
    "Lambda_Plain": {
        "name": "Lambda plain",
        "category": "Complex",
        "disease_term": _term("MONDO:0000190"),
    },
}


@pytest.fixture
def corpus(tmp_path: Path) -> Path:
    import yaml

    kb = tmp_path / "kb" / "disorders"
    kb.mkdir(parents=True)
    for slug, body in ENTRIES.items():
        (kb / f"{slug}.yaml").write_text(yaml.safe_dump(body, sort_keys=False))
    return kb


def _run(corpus: Path, capsys, *extra: str) -> tuple[int, str]:
    code = main(["--kb-dir", str(corpus), *extra])
    return code, capsys.readouterr().out


def _records(corpus: Path, capsys, *extra: str) -> dict[str, dict]:
    code, out = _run(corpus, capsys, "--format", "json", *extra)
    assert code == 0, out
    return {r["entry"]: r for r in json.loads(out)}


def _classes(record: dict) -> set[str]:
    return {f["class"] for f in record["findings"]}


# --------------------------------------------------------------------------
# The line between deterministic, advisory and informational
# --------------------------------------------------------------------------


def test_class_lists_partition_and_every_class_names_a_rule():
    all_classes = DETERMINISTIC_CLASSES + ADVISORY_CLASSES + INFORMATIONAL_CLASSES
    assert len(set(all_classes)) == len(all_classes)
    assert set(RULE_FOR_CLASS) == set(all_classes)


def test_root_terms_agree_with_the_committed_mondo_cache():
    """The rung-0 CURIEs are written from the cache, not from memory."""
    with (ROOT / "cache" / "mondo" / "terms.csv").open(newline="") as handle:
        labels = {row["curie"]: row["label"] for row in csv.DictReader(handle)}
    for curie, label in ROOT_TERMS.items():
        assert labels.get(curie) == label, (curie, label, labels.get(curie))


def test_missing_everything_is_three_findings(corpus, capsys):
    rec = _records(corpus, capsys)["Alpha_Fever"]
    assert rec["scope"] == SCOPE_INFECTIOUS
    assert _classes(rec) == {MISSING_AGENT, MISSING_TRANSMISSION, NO_PROGRESSION}
    assert rec["deterministic"] == f"{MISSING_AGENT};{MISSING_TRANSMISSION}"
    assert rec["advisory"] == NO_PROGRESSION


def test_undecided_lump_is_advisory_and_a_recorded_one_is_informational(corpus, capsys):
    recs = _records(corpus, capsys)
    assert _classes(recs["Beta_Lump"]) == {TAXON_LUMP}
    assert recs["Beta_Lump"]["lump_recorded"] == "false"
    assert _classes(recs["Beta_Lump_Recorded"]) == {LUMP_RECORDED}
    assert recs["Beta_Lump_Recorded"]["lump_recorded"] == "true"
    assert _classes(recs["Beta_Lump_Short"]) == {TAXON_LUMP}


@pytest.mark.parametrize(
    ("notes", "expected"),
    [
        (None, False),
        ("", False),
        (WAIVER_LONG, True),
        (WAIVER_SHORT, False),
        ("Prose that merely mentions " + WAIVER_LONG, False),
        ("First paragraph.\n\n" + WAIVER_LONG, True),
        ("First paragraph.\n" + WAIVER_LONG, False),
    ],
)
def test_lump_waiver_needs_the_sentinel_at_a_paragraph_start_and_reasoning_after_it(
    notes, expected
):
    assert lump_waiver_recorded(notes) is expected


def test_pointer_outcomes(corpus, capsys):
    rec = _records(corpus, capsys)["Gamma_Group"]
    by_class: dict[str, list[str]] = {}
    for f in rec["findings"]:
        by_class.setdefault(f["class"], []).append(f["detail"])
    # GF-A: same MONDO as Gamma_Fever_A, no pointer -> double modelled.
    assert any(
        "'GF-A'" in d and "Gamma_Fever_A" in d for d in by_class[DOUBLE_MODELLED]
    )
    # GF-B: pointer resolves and terms agree -> informational only.
    assert any("'GF-B' -> Gamma_Fever_B" in d for d in by_class[POINTER])
    # GF-C: pointer at nothing -> deterministic.
    assert any(
        "'GF-C'" in d and "Nonexistent_Entry" in d for d in by_class[DANGLING_POINTER]
    )
    # GF-D: pointer resolves, but the terms disagree -> advisory.
    assert any(
        "'GF-D'" in d and "MONDO:0000199" in d and "MONDO:0000111" in d
        for d in by_class[POINTER_TERM_MISMATCH]
    )
    # GF-E: unbound, and nothing else to say.
    assert any("'GF-E'" in d for d in by_class[UNBOUND_SUBTYPE])
    assert rec["n_pointers"] == "3"
    assert rec["n_subtypes_bound"] == "3"
    # A pointer is never also double-modelled, whatever its term.
    assert not any("'GF-B'" in d or "'GF-D'" in d for d in by_class[DOUBLE_MODELLED])


def test_double_modelled_by_name_as_well_as_by_term(corpus, capsys):
    rec = _records(corpus, capsys)["Gamma_Named"]
    details = [f["detail"] for f in rec["findings"] if f["class"] == DOUBLE_MODELLED]
    assert details and "Gamma_Fever_A (same name)" in details[0]


def test_pathotype_collapse_root_anchor_and_unbound_strata(corpus, capsys):
    recs = _records(corpus, capsys)
    assert _classes(recs["Delta_Collapse"]) == {PATHOTYPE_COLLAPSE}
    assert _classes(recs["Root_Entry"]) == {
        ROOT_AS_ENTRY,
        UNBOUND_AGENT,
        UNBOUND_AGENT_STRATUM,
    }
    assert recs["Root_Entry"]["n_agent_strata"] == "1"
    assert recs["Root_Entry"]["n_agent_strata_bound"] == "0"


def test_shared_anchor_is_flagged_only_where_no_narrow_match_is_recorded(
    corpus, capsys
):
    recs = _records(corpus, capsys)
    assert _classes(recs["Shared_One"]) == {DUPLICATE_ANCHOR}
    assert _classes(recs["Shared_Two"]) == set()


def test_lifecycle_heuristic_matches_whole_words_only(corpus, capsys):
    recs = _records(corpus, capsys)
    assert _classes(recs["Iota_Vector"]) == {MISSING_LIFECYCLE}
    assert MISSING_LIFECYCLE not in _classes(recs["Kappa_Stick"])


# --------------------------------------------------------------------------
# Scope: which ladder governs the entry
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("slug", "expected"),
    [
        ("Alpha_Fever", SCOPE_INFECTIOUS),
        ("Epsilon_Carcinoma", SCOPE_NEOPLASM),
        ("Zeta_Sequela", SCOPE_SEQUELA),
        ("Eta_Susceptibility", SCOPE_MENDELIAN),
        ("Theta_Toxicosis", SCOPE_TOXICOLOGIC),
        ("Lambda_Plain", SCOPE_OTHER),
    ],
)
def test_scope_of(slug, expected):
    assert scope_of(ENTRIES[slug]) == expected


def test_neoplasm_wins_over_an_infectious_category():
    doc = {**ENTRIES["Epsilon_Carcinoma"], "category": "Infectious Disease"}
    assert scope_of(doc) == SCOPE_NEOPLASM


def test_out_of_scope_entries_get_no_infectious_findings(corpus, capsys):
    recs = _records(corpus, capsys)
    for slug in (
        "Epsilon_Carcinoma",
        "Zeta_Sequela",
        "Eta_Susceptibility",
        "Theta_Toxicosis",
    ):
        assert slug not in recs or _classes(recs[slug]) == set(), slug
    assert "Lambda_Plain" not in recs


def test_scope_all_extends_the_cross_entry_classes_to_every_entry(corpus, capsys):
    recs = _records(corpus, capsys, "--scope", "all")
    assert _classes(recs["Epsilon_Carcinoma"]) == {DOUBLE_MODELLED}
    assert (
        "Shared_One (same name)" in recs["Epsilon_Carcinoma"]["findings"][0]["detail"]
    )


def test_summary_counts_exclusions_among_pathogen_marked_entries_only(corpus, capsys):
    code, out = _run(corpus, capsys)
    assert code == 0
    assert "infectious set: 14" in out
    assert (
        "pathogen-marked entries excluded: NEOPLASM 1, MENDELIAN 1, SEQUELA 1, TOXICOLOGIC 1"
        in out
    )
    assert "Undecided lumps (2)" in out


# --------------------------------------------------------------------------
# Exit codes and reporting scope
# --------------------------------------------------------------------------


def test_report_only_by_default_strict_and_fail_on_gate(corpus, capsys):
    assert _run(corpus, capsys)[0] == 0
    assert _run(corpus, capsys, "--strict")[0] == 1
    assert _run(corpus, capsys, "--fail-on", TAXON_LUMP)[0] == 1
    assert (
        _run(
            corpus, capsys, "--fail-on", LUMP_RECORDED, str(corpus / "Beta_Lump.yaml")
        )[0]
        == 0
    )
    with pytest.raises(SystemExit) as excinfo:
        main(["--kb-dir", str(corpus), "--fail-on", "BOGUS"])
    assert excinfo.value.code == 2


def test_naming_a_file_narrows_the_report_but_not_the_index(corpus, capsys):
    recs = _records(corpus, capsys, str(corpus / "Gamma_Group.yaml"))
    assert set(recs) == {"Gamma_Group"}
    assert DOUBLE_MODELLED in _classes(recs["Gamma_Group"])


def test_usage_errors_exit_2(corpus, capsys, tmp_path):
    assert main(["--kb-dir", str(corpus), str(corpus / "Missing.yaml")]) == 2
    empty = tmp_path / "empty"
    empty.mkdir()
    assert main(["--kb-dir", str(empty)]) == 2
    assert main(["--kb-dir", str(corpus), str(empty)]) == 2


def test_tsv_has_one_row_per_in_scope_or_flagged_entry(corpus, capsys):
    code, out = _run(corpus, capsys, "--format", "tsv")
    assert code == 0
    rows = list(csv.DictReader(out.splitlines(), delimiter="\t"))
    entries = {r["entry"] for r in rows}
    assert "Lambda_Plain" not in entries
    assert "Epsilon_Carcinoma" not in entries
    assert {"Alpha_Fever", "Gamma_Group", "Shared_Two"} <= entries
    beta = next(r for r in rows if r["entry"] == "Beta_Lump")
    assert (
        beta["n_agents"] == "3"
        and beta["n_agents_bound"] == "3"
        and beta["has_transmission"] == "true"
    )


def test_cli_runs_as_a_script(corpus):
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--kb-dir", str(corpus), "--format", "list"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert f"\t{ROOT_AS_ENTRY}\t" in result.stdout


# --------------------------------------------------------------------------
# The real KB
# --------------------------------------------------------------------------


def test_schema_puts_curated_in_on_subtype():
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(str(ROOT / "src" / "dismech" / "schema" / "dismech.yaml"))
    assert "curated_in" in view.class_slots("Subtype")
    assert view.get_slot("curated_in").range == "string"


@pytest.mark.kb_data
def test_spotted_fever_rickettsiosis_pointers_are_pointers_not_defects(capsys):
    """The worked instance of §3a L4 / §3e rung 4, mis-reported as double modelling in #10115."""
    recs = _records(KB_DIR, capsys, str(KB_DIR / "Spotted_Fever_Rickettsiosis.yaml"))
    rec = recs["Spotted_Fever_Rickettsiosis"]
    pointers = {f["detail"] for f in rec["findings"] if f["class"] == POINTER}
    assert "subtype 'RMSF' -> Rocky_Mountain_Spotted_Fever" in pointers
    assert "subtype 'MSF' -> Boutonneuse_Fever" in pointers
    assert DOUBLE_MODELLED not in _classes(rec)
    assert POINTER_TERM_MISMATCH not in _classes(rec)


@pytest.mark.kb_data
def test_no_dangling_pointers_in_the_kb(capsys):
    """``curated_in`` is a foreign key; a target that does not exist is a defect anywhere."""
    code, out = _run(KB_DIR, capsys, "--fail-on", DANGLING_POINTER, "--format", "list")
    assert code == 0, [line for line in out.splitlines() if DANGLING_POINTER in line]
