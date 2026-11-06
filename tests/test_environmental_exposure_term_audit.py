"""Tests for the environmental ``exposure_term`` coverage audit (issue #8430)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "environmental_exposure_term_audit.py"
SPEC = importlib.util.spec_from_file_location(
    "environmental_exposure_term_audit", SCRIPT_PATH
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


def _write(kb_dir: Path, slug: str, environmental: str) -> None:
    kb_dir.mkdir(parents=True, exist_ok=True)
    (kb_dir / f"{slug}.yaml").write_text(
        f"name: {slug.replace('_', ' ')}\nenvironmental:\n{environmental}",
        encoding="utf-8",
    )


BOUND_BLOCK = """- name: Cigarette Smoking
  influences_mechanisms:
  - target: Some Node
  exposure_term:
    preferred_term: exposure to cigarette smoking
    term:
      id: ECTO:0100003
      label: exposure to cigarette smoking
"""

PARTIAL_BLOCK = """- name: Emotional Stress
  influences_mechanisms:
  - target: Some Node
  exposure_term:
    preferred_term: emotional stress
"""

UNBOUND_LINKED_BLOCK = """- name: Cigarette smoking
  influences_mechanisms:
  - target: Other Node
"""

UNBOUND_UNLINKED_BLOCK = """- name: Microgravity Exposure
  description: No ECTO term exists.
"""


# --------------------------------------------------------------------------- #
# classification
# --------------------------------------------------------------------------- #


def test_classify_distinguishes_bound_partial_and_unbound(tmp_path: Path) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "disorders", "B", PARTIAL_BLOCK)
    _write(tmp_path / "kb" / "disorders", "C", UNBOUND_UNLINKED_BLOCK)

    by_name = {e.name: e for e in audit.collect(tmp_path)}

    assert by_name["Cigarette Smoking"].state == "BOUND"
    assert by_name["Cigarette Smoking"].curie == "ECTO:0100003"
    # A preferred_term with no term: is NOT bound — it only looks grounded.
    assert by_name["Emotional Stress"].state == "PARTIAL"
    assert by_name["Emotional Stress"].curie == ""
    assert by_name["Microgravity Exposure"].state == "UNBOUND"


def test_pathograph_link_is_read_from_influences_mechanisms(tmp_path: Path) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "disorders", "C", UNBOUND_UNLINKED_BLOCK)

    by_name = {e.name: e for e in audit.collect(tmp_path)}

    assert by_name["Cigarette Smoking"].linked is True
    assert by_name["Microgravity Exposure"].linked is False


def test_priority_is_linked_and_not_bound(tmp_path: Path) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "disorders", "B", PARTIAL_BLOCK)
    _write(tmp_path / "kb" / "disorders", "C", UNBOUND_UNLINKED_BLOCK)
    _write(tmp_path / "kb" / "disorders", "D", UNBOUND_LINKED_BLOCK)

    priority = {e.name for e in audit.collect(tmp_path) if e.priority}

    # PARTIAL counts as a gap; an unlinked entry never does, however unbound.
    assert priority == {"Emotional Stress", "Cigarette smoking"}


def test_modules_and_comorbidities_are_walked_too(tmp_path: Path) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "modules", "M", UNBOUND_LINKED_BLOCK)
    _write(tmp_path / "kb" / "comorbidities", "X", UNBOUND_UNLINKED_BLOCK)

    paths = {e.path for e in audit.collect(tmp_path)}

    assert paths == {
        "kb/disorders/A.yaml",
        "kb/modules/M.yaml",
        "kb/comorbidities/X.yaml",
    }


def test_unparseable_file_is_reported_and_skipped(tmp_path: Path, capsys) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    _write(kb_dir, "Good", BOUND_BLOCK)
    (kb_dir / "Bad.yaml").write_text("name: [unclosed\n", encoding="utf-8")

    exposures = audit.collect(tmp_path)

    assert [e.name for e in exposures] == ["Cigarette Smoking"]
    assert "Bad.yaml" in capsys.readouterr().err


# --------------------------------------------------------------------------- #
# normalization and reuse
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize(
    ("left", "right"),
    [
        ("Cigarette Smoking", "cigarette smoking"),
        ("Tobacco Smoking", "Smoking, tobacco"),
        ("Ultraviolet Radiation Exposure", "ultraviolet radiation"),
        ("Cold exposure", "Exposure to cold"),
    ],
)
def test_normalize_collapses_case_order_and_framing_words(
    left: str, right: str
) -> None:
    assert audit._normalize(left) == audit._normalize(right)


def test_normalize_keeps_distinguishing_tokens() -> None:
    # The whole point of the conservative stopword list: these are different
    # exposures and must not collapse onto one another.
    assert audit._normalize("Ionizing Radiation") != audit._normalize(
        "Ultraviolet Radiation"
    )
    assert audit._normalize("Catabolic stress") != audit._normalize("Emotional Stress")


def test_reuse_index_suggests_a_curie_already_used_for_the_same_concept(
    tmp_path: Path,
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "disorders", "D", UNBOUND_LINKED_BLOCK)

    exposures = audit.collect(tmp_path)
    reuse = audit.build_reuse_index(exposures)

    unbound = next(e for e in exposures if e.state == "UNBOUND")
    assert reuse[audit._normalize(unbound.name)][0] == "ECTO:0100003"


def test_reuse_index_ignores_unbound_entries(tmp_path: Path) -> None:
    _write(tmp_path / "kb" / "disorders", "D", UNBOUND_LINKED_BLOCK)

    assert audit.build_reuse_index(audit.collect(tmp_path)) == {}


def test_reuse_index_prefers_the_majority_curie_on_disagreement(tmp_path: Path) -> None:
    majority = BOUND_BLOCK
    minority = BOUND_BLOCK.replace("ECTO:0100003", "ECTO:6000029").replace(
        "exposure to cigarette smoking", "exposure to tobacco smoking"
    )
    _write(tmp_path / "kb" / "disorders", "A", majority)
    _write(tmp_path / "kb" / "disorders", "B", majority)
    _write(tmp_path / "kb" / "disorders", "C", minority)

    reuse = audit.build_reuse_index(audit.collect(tmp_path))

    assert reuse[audit._normalize("Cigarette Smoking")][0] == "ECTO:0100003"


def test_conflicting_bindings_are_surfaced_not_silently_resolved(
    tmp_path: Path,
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(
        tmp_path / "kb" / "disorders",
        "B",
        BOUND_BLOCK.replace("ECTO:0100003", "ECTO:6000029"),
    )

    conflicts = audit.find_conflicts(audit.collect(tmp_path))

    assert set(conflicts) == {audit._normalize("Cigarette Smoking")}
    assert set(conflicts[audit._normalize("Cigarette Smoking")]) == {
        "ECTO:0100003",
        "ECTO:6000029",
    }


def test_no_conflict_when_every_binding_agrees(tmp_path: Path) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "disorders", "B", BOUND_BLOCK)

    assert audit.find_conflicts(audit.collect(tmp_path)) == {}


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def test_strict_exits_nonzero_when_a_linked_entry_is_unbound(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    _write(tmp_path / "kb" / "disorders", "D", UNBOUND_LINKED_BLOCK)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main(["--strict"]) == 1
    assert "1 pathograph-linked" in capsys.readouterr().err


def test_strict_exits_zero_when_every_linked_entry_is_bound(
    tmp_path: Path, monkeypatch
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "disorders", "C", UNBOUND_UNLINKED_BLOCK)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    # The unlinked-and-unbound entry must not trip --strict.
    assert audit.main(["--strict"]) == 0


def test_summary_reports_the_full_census_even_under_a_filter(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "disorders", "C", UNBOUND_UNLINKED_BLOCK)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main(["--linked-only", "--format", "summary"]) == 0

    # 2, not the 1 entry the filter selects: a census narrowed by a filter would
    # report a coverage percentage of its own selection.
    assert "kb/{disorders, modules, comorbidities}: 2" in capsys.readouterr().out


def test_tsv_carries_the_reuse_suggestion_for_unbound_rows(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "disorders", "D", UNBOUND_LINKED_BLOCK)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main(["--format", "tsv"]) == 0

    rows = [line.split("\t") for line in capsys.readouterr().out.strip().splitlines()]
    header, body = rows[0], rows[1:]
    reuse_col = header.index("reuse_curie")
    by_state = {r[header.index("state")]: r for r in body}

    assert by_state["UNBOUND"][reuse_col] == "ECTO:0100003"
    # A bound row does not suggest a reuse of itself.
    assert by_state["BOUND"][reuse_col] == ""


def test_out_writes_to_a_file(tmp_path: Path, monkeypatch) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)
    out = tmp_path / "audit.tsv"

    assert audit.main(["--format", "tsv", "--out", str(out)]) == 0
    assert "ECTO:0100003" in out.read_text(encoding="utf-8")


# --------------------------------------------------------------------------- #
# enum-membership check on reuse candidates (issue #10738)
# --------------------------------------------------------------------------- #


def _write_enum_cache(repo_root: Path, *curies: str) -> None:
    enums = repo_root / "cache" / "enums"
    enums.mkdir(parents=True, exist_ok=True)
    (enums / "exposureterm_000000000000.csv").write_text(
        "curie\n" + "".join(f"{c}\n" for c in curies), encoding="utf-8"
    )


def test_load_enum_members_reads_the_exposureterm_cache(tmp_path: Path) -> None:
    _write_enum_cache(tmp_path, "ECTO:0100003", "XCO:0000000")

    assert audit.load_enum_members(tmp_path) == {"ECTO:0100003", "XCO:0000000"}


def test_load_enum_members_is_none_without_a_cache(tmp_path: Path) -> None:
    assert audit.load_enum_members(tmp_path) is None


def test_non_member_candidate_is_not_recommended_for_reuse(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    # The bound CURIE is in the KB but absent from the enum cache: an
    # unvalidated binding the audit must not hand back as "reuse".
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "disorders", "D", UNBOUND_LINKED_BLOCK)
    _write_enum_cache(tmp_path, "ECTO:9999999")
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main(["--format", "list"]) == 0
    out = capsys.readouterr().out
    unbound_line = next(line for line in out.splitlines() if "[UNBOUND" in line)

    assert "-> reuse" not in unbound_line
    assert "not in enum cache: ECTO:0100003" in unbound_line


def test_member_candidate_is_still_recommended_for_reuse(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "disorders", "D", UNBOUND_LINKED_BLOCK)
    _write_enum_cache(tmp_path, "ECTO:0100003")
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main(["--format", "list"]) == 0
    out = capsys.readouterr().out
    unbound_line = next(line for line in out.splitlines() if "[UNBOUND" in line)

    assert "-> reuse ECTO:0100003" in unbound_line


def test_tsv_and_summary_report_enum_membership(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "disorders", "D", UNBOUND_LINKED_BLOCK)
    _write_enum_cache(tmp_path, "ECTO:9999999")
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main(["--format", "tsv"]) == 0
    rows = [line.split("\t") for line in capsys.readouterr().out.strip().splitlines()]
    header, body = rows[0], rows[1:]
    unbound = next(r for r in body if r[header.index("state")] == "UNBOUND")
    assert unbound[header.index("reuse_in_enum_cache")] == "no"

    assert audit.main(["--format", "summary"]) == 0
    summary = capsys.readouterr().out
    assert "normalized name: 0 " in summary
    assert "not in the ExposureTerm enum cache (check with validate-terms" in summary
    assert "?ECTO:0100003" in summary


def test_member_curie_is_preferred_over_a_non_member_majority(
    tmp_path: Path,
) -> None:
    non_member = BOUND_BLOCK.replace("ECTO:0100003", "ECTO:6000029")
    _write(tmp_path / "kb" / "disorders", "A", non_member)
    _write(tmp_path / "kb" / "disorders", "B", non_member)
    _write(tmp_path / "kb" / "disorders", "C", BOUND_BLOCK)

    reuse = audit.build_reuse_index(
        audit.collect(tmp_path), frozenset({"ECTO:0100003"})
    )

    curie, _label, _count, in_enum = reuse[audit._normalize("Cigarette Smoking")]
    assert (curie, in_enum) == ("ECTO:0100003", True)


def test_bound_rows_carry_no_reuse_suffix_in_list_format(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BOUND_BLOCK)
    _write(tmp_path / "kb" / "disorders", "B", BOUND_BLOCK)
    _write_enum_cache(tmp_path, "ECTO:0100003")
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main(["--format", "list"]) == 0
    lines = capsys.readouterr().out.strip().splitlines()

    assert len(lines) == 2
    # A bound row does not suggest a reuse of itself, matching --format tsv.
    assert all("[BOUND" in line and "->" not in line for line in lines)
