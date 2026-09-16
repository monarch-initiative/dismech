"""A phenotype nothing points at is invisible to every existing check.

``scripts/check_causal_targets.py`` asks which declared edges name a target that
resolves to nothing. This is the complement: which phenotype nodes no causal
edge reaches. An entry can pass that check perfectly and still render its
phenotypes as a disconnected island (issue #11935).

What these tests pin is mostly the *boundary*, because the boundary is where the
report is arguable. Three kinds of edge touch a phenotype without explaining it
-- a treatment addressing it, an observational ``reports_on`` readout, and a
non-committal environmental link -- and the report counts none of them as
connected while still reporting that they exist, so a curator can tell "nothing
knows this node is here" from "something points at it, but not a mechanism".

The connectivity verdict itself is not reimplemented here: it comes from
``dismech.qc_plugins.causal_inlink_coverage``, the metric behind the
``phenotypes[].causal_inlink`` compliance score, which has its own tests in
``tests/test_qc_plugins.py``. These tests pin the triage layer on top of it and
the guarantee that the two cannot disagree.
"""

import subprocess
import sys
from pathlib import Path

import pytest

# Inline the path rather than assigning ROOT first: ruff's E402 allows an
# import preceded by a `sys.path` preamble, but an intervening assignment
# breaks that allowance (see tests/test_causal_targets.py). That allowance is
# also why the import below carries no E402 suppression: ruff reports an unused
# directive (RUF100) for one, as CI caught. Do not add it back.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_disconnected_phenotypes import (
    ATTACH_NONCAUSAL,
    ATTACH_READOUT,
    ATTACH_SEQUELA_SOURCE,
    ATTACH_TREATED,
    FINDING_PARTIAL,
    FINDING_ZERO,
    EntryReport,
    PhenotypeRow,
    assess,
    main,
)

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_disconnected_phenotypes.py"


def _write(tmp_path, name, body):
    path = tmp_path / name
    path.write_text(body)
    return path


CONNECTED_AND_FLOATING = """
name: Test Disorder
pathophysiology:
- name: Mechanism A
  downstream:
  - target: Explained Phenotype
phenotypes:
- name: Explained Phenotype
  category: Neurologic
- name: Floating Phenotype
  category: Laboratory
"""


def test_reports_the_phenotype_no_edge_explains(tmp_path):
    report = assess(_write(tmp_path, "Test.yaml", CONNECTED_AND_FLOATING))
    assert report is not None
    assert (report.connected, report.total) == (1, 2)
    assert [row.name for row in report.disconnected] == ["Floating Phenotype"]
    assert report.findings == [FINDING_PARTIAL]


def test_an_entry_with_every_phenotype_connected_carries_no_finding(tmp_path):
    body = """
name: Wired
pathophysiology:
- name: Mechanism A
  downstream:
  - target: Only Phenotype
phenotypes:
- name: Only Phenotype
"""
    report = assess(_write(tmp_path, "Wired.yaml", body))
    assert report is not None
    assert report.findings == []
    assert report.disconnected == []


def test_an_entry_with_no_phenotypes_is_not_assessed(tmp_path):
    body = """
name: No Phenotypes
pathophysiology:
- name: Mechanism A
"""
    assert assess(_write(tmp_path, "None.yaml", body)) is None


def test_zero_connected_is_a_distinct_finding_from_partial(tmp_path):
    body = """
name: Island
pathophysiology:
- name: Mechanism A
  downstream:
  - target: Mechanism B
- name: Mechanism B
phenotypes:
- name: Phenotype One
- name: Phenotype Two
"""
    report = assess(_write(tmp_path, "Island.yaml", body))
    assert report is not None
    assert report.findings == [FINDING_ZERO]
    assert report.connected == 0
    assert report.isolated_count == 2


# --- the boundary: edges that touch a phenotype without explaining it --------


def test_a_treatment_edge_does_not_connect_but_is_reported(tmp_path):
    """`target_phenotypes` says an intervention addresses it, not what causes it."""
    body = """
name: Treated
phenotypes:
- name: Pain
treatments:
- name: Analgesic
  target_phenotypes:
  - preferred_term: Pain
"""
    report = assess(_write(tmp_path, "Treated.yaml", body))
    assert report is not None
    assert report.connected == 0
    assert report.disconnected[0].attachment == [ATTACH_TREATED]
    # Reported, but not counted as isolated: something points at it.
    assert report.isolated_count == 0


def test_a_reports_on_readout_does_not_connect_but_is_reported(tmp_path):
    """`reports_on` is an observational link, carrying the `readout` predicate."""
    body = """
name: Observed
pathophysiology:
- name: Retinal Degeneration
phenotypes:
- name: Abnormal Electroretinogram
  reports_on:
  - target: Retinal Degeneration
"""
    report = assess(_write(tmp_path, "Observed.yaml", body))
    assert report is not None
    assert report.connected == 0
    assert report.disconnected[0].attachment == [ATTACH_READOUT]


def test_a_non_committal_environmental_link_does_not_connect_but_is_reported(tmp_path):
    """PREDISPOSES raises susceptibility without explaining the phenotype."""
    body = """
name: Exposed
phenotypes:
- name: Wheezing
environmental:
- name: Air pollution
  influences_mechanisms:
  - target: Wheezing
    environmental_effect: PREDISPOSES
"""
    report = assess(_write(tmp_path, "Exposed.yaml", body))
    assert report is not None
    assert report.connected == 0
    assert report.disconnected[0].attachment == [ATTACH_NONCAUSAL]


def test_a_causal_environmental_link_does_connect(tmp_path):
    """TRIGGERS and EXACERBATES are genuine causal claims, so they count."""
    body = """
name: Exposed
phenotypes:
- name: Wheezing
environmental:
- name: Cold air
  influences_mechanisms:
  - target: Wheezing
    environmental_effect: EXACERBATES
"""
    report = assess(_write(tmp_path, "Exposed.yaml", body))
    assert report is not None
    assert (report.connected, report.total) == (1, 1)


def test_a_phenotype_that_explains_something_else_is_still_unexplained(tmp_path):
    """Outbound `sequelae` do not substitute for an upstream mechanism."""
    body = """
name: Sequela
phenotypes:
- name: Hypertension
  sequelae:
  - target: Stroke
- name: Stroke
"""
    report = assess(_write(tmp_path, "Sequela.yaml", body))
    assert report is not None
    # Stroke is explained by the sequela edge; Hypertension explains it but
    # nothing explains Hypertension.
    assert (report.connected, report.total) == (1, 1 + 1)
    row = next(r for r in report.disconnected if r.name == "Hypertension")
    assert row.attachment == [ATTACH_SEQUELA_SOURCE]


def test_subtype_scoping_does_not_connect_a_phenotype(tmp_path):
    """A subtype-restricted phenotype still needs an edge from what produces it."""
    body = """
name: Subtyped
has_subtypes:
- name: Type 1
phenotypes:
- name: Seizure
  subtype: Type 1
"""
    report = assess(_write(tmp_path, "Subtyped.yaml", body))
    assert report is not None
    assert report.connected == 0
    assert report.disconnected[0].subtype == "Type 1"


# --- the triage layer --------------------------------------------------------


def test_percentage_and_attachment_string_default_to_the_strict_reading():
    row = PhenotypeRow(name="X", subtype=None, category=None)
    assert row.attachment_str == "ISOLATED"
    report = EntryReport(path="p", name="n", connected=1, total=4, disconnected=[row])
    assert report.percentage == 25.0
    assert report.findings == [FINDING_PARTIAL]


def test_tsv_emits_one_row_per_disconnected_phenotype(tmp_path, capsys):
    path = _write(tmp_path, "Test.yaml", CONNECTED_AND_FLOATING)
    assert main([str(path), "--format", "tsv"]) == 0
    lines = capsys.readouterr().out.strip().splitlines()
    assert lines[0].split("\t")[:3] == ["path", "entry", "phenotype"]
    assert len(lines) == 2
    fields = lines[1].split("\t")
    assert fields[2] == "Floating Phenotype"
    assert fields[5] == "Laboratory"
    assert fields[-1] == FINDING_PARTIAL


def test_zero_only_and_min_phenotypes_narrow_the_worklist(tmp_path, capsys):
    partial = _write(tmp_path, "Partial.yaml", CONNECTED_AND_FLOATING)
    zero = _write(
        tmp_path,
        "Zero.yaml",
        """
name: Zero
pathophysiology:
- name: Mechanism A
phenotypes:
- name: One
- name: Two
- name: Three
""",
    )
    assert main([str(partial), str(zero), "--zero-only", "--format", "tsv"]) == 0
    out = capsys.readouterr().out
    assert "Zero.yaml" in out
    assert "Partial.yaml" not in out

    assert (
        main([str(partial), str(zero), "--min-phenotypes", "3", "--format", "tsv"]) == 0
    )
    out = capsys.readouterr().out
    assert "Zero.yaml" in out
    assert "Partial.yaml" not in out


def test_report_only_by_default_and_gating_is_opt_in(tmp_path):
    path = _write(tmp_path, "Test.yaml", CONNECTED_AND_FLOATING)
    assert main([str(path)]) == 0
    assert main([str(path), "--strict"]) == 1
    assert main([str(path), "--fail-under", "40"]) == 0
    assert main([str(path), "--fail-under", "60"]) == 1


def test_a_path_that_does_not_exist_never_reads_as_a_passing_gate(tmp_path, capsys):
    """Exit 2, not 0 -- otherwise a typo would look like a clean --strict run."""
    missing = tmp_path / "Nope.yaml"
    assert main([str(missing)]) == 2
    assert main([str(missing), "--strict"]) == 2
    assert main([str(missing), "--fail-under", "90"]) == 2
    assert "Nope.yaml" in capsys.readouterr().err

    # A real file beside a missing one is still reported, and still exits 2.
    real = _write(tmp_path, "Test.yaml", CONNECTED_AND_FLOATING)
    assert main([str(real), str(missing), "--format", "tsv"]) == 2
    assert "Floating Phenotype" in capsys.readouterr().out


def test_a_directory_argument_is_expanded_into_its_entries(tmp_path, capsys):
    """`kb/disorders` is this recipe's own default root, so it is typed first."""
    _write(tmp_path, "Test.yaml", CONNECTED_AND_FLOATING)
    _write(
        tmp_path,
        "Second.yaml",
        """
name: Second
pathophysiology:
- name: Mechanism A
phenotypes:
- name: Stranded
""",
    )
    # A history record beside the entries is not an entry.
    _write(tmp_path, "Test.history.yaml", "name: not an entry\n")

    assert main([str(tmp_path), "--format", "tsv"]) == 0
    rows = capsys.readouterr().out.strip().splitlines()[1:]
    assert {row.split("\t")[2] for row in rows} == {"Floating Phenotype", "Stranded"}
    assert not any("history" in row for row in rows)


def test_an_unreadable_path_reports_rather_than_tracebacks(tmp_path, capsys):
    """Any OSError on a named path is a usage error -- reported, never swallowed.

    Exercised with a *directory* named ``*.yaml``, which the directory expansion
    above hands on as an entry and which then fails to read. That is the one
    place ``IsADirectoryError`` still arises once a directory argument is
    expanded, and unlike a permission bit it reproduces for any user, including
    root in CI.
    """
    (tmp_path / "NotAFile.yaml").mkdir()
    _write(tmp_path, "Test.yaml", CONNECTED_AND_FLOATING)

    assert main([str(tmp_path)]) == 2
    captured = capsys.readouterr()
    assert "Is a directory" in captured.err
    assert "NotAFile.yaml" in captured.err
    # The readable entry beside it is still assessed and reported before the
    # exit, rather than the whole run being abandoned.
    assert "Entries with phenotype nodes:        1" in captured.out
    assert "causally connected:                1 (50.0%)" in captured.out


def test_the_script_runs_over_the_real_kb_entry_that_prompted_the_issue():
    """End-to-end through the CLI, on the instance named in issue #11935."""
    entry = ROOT / "kb/disorders/SLC35A1-Congenital_Disorder_of_Glycosylation.yaml"
    if not entry.exists():  # pragma: no cover - entry renamed or retargeted
        pytest.skip(f"{entry.name} is no longer in kb/disorders")
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(entry), "--format", "json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert '"percentage": 0.0' in result.stdout
    assert FINDING_ZERO in result.stdout
