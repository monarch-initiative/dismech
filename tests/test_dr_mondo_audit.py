"""Tests for scripts/dr_mondo_audit.py (dismech #9949)."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "dr_mondo_audit.py"
SPEC = importlib.util.spec_from_file_location("dr_mondo_audit", SCRIPT_PATH)
assert SPEC and SPEC.loader
audit_mod = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = (
    audit_mod  # dataclasses under `from __future__ import annotations`
)
SPEC.loader.exec_module(audit_mod)

LABELS = {
    "MONDO:0011013": "autosomal dominant hypocalcemia 1",
    "MONDO:0008833": "renal-hepatic-pancreatic dysplasia 1",
    "MONDO:0015229": "Bardet-Biedl syndrome",
    "MONDO:0008854": "Bardet-Biedl syndrome 1",
    "MONDO:0007037": "achondroplasia",
}


def _tree(tmp_path: Path) -> Path:
    (tmp_path / "research").mkdir()
    (tmp_path / "kb" / "disorders").mkdir(parents=True)
    (tmp_path / "stubs").mkdir()
    (tmp_path / "cache" / "mondo").mkdir(parents=True)
    rows = ["curie,label,retrieved_at"] + [
        f'{curie},"{label}",2026-10-21T00:00:00' for curie, label in LABELS.items()
    ]
    (tmp_path / "cache" / "mondo" / "terms.csv").write_text(
        "\n".join(rows) + "\n", encoding="utf-8"
    )
    return tmp_path


def _entry(root: Path, slug: str, curie: str) -> None:
    (root / "kb" / "disorders" / f"{slug}.yaml").write_text(
        f"name: {slug}\ndisease_term:\n  preferred_term: x\n  term:\n    id: {curie}\n    label: x\n",
        encoding="utf-8",
    )


def _report(root: Path, slug: str, body: str, provider: str = "openscientist") -> Path:
    path = root / "research" / f"{slug}-deep-research-{provider}.md"
    path.write_text(body, encoding="utf-8")
    return path


def _run(root: Path, *reports: Path) -> list:
    return audit_mod.audit(
        list(reports) or audit_mod.iter_reports(root / "research"),
        kb_dir=root / "kb" / "disorders",
        stubs_dir=root / "stubs",
        cache_path=root / "cache" / "mondo" / "terms.csv",
        display_root=root,
    )


def test_adh1_shape_wrong_disease_curie_in_identifier_list_is_a_mismatch(tmp_path):
    root = _tree(tmp_path)
    _entry(root, "Autosomal_Dominant_Hypocalcemia_1", "MONDO:0011013")
    report = _report(
        root,
        "Autosomal_Dominant_Hypocalcemia_1",
        "# ADH1\n\nADH1 identifiers: **OMIM #601198**; ORPHA:428; **MONDO:0008833**; MeSH\n",
    )
    [result] = _run(root, report)
    assert result.status == "MISMATCH"
    assert result.expected_id == "MONDO:0011013"
    assert [term.curie for term in result.mismatches] == ["MONDO:0008833"]
    assert result.mismatches[0].label == "renal-hepatic-pancreatic dysplasia 1"
    assert result.mismatches[0].lines == [3]


def test_shared_digit_alone_does_not_count_as_related():
    # "1" is the only token the two ADH1-shape labels share.
    assert not audit_mod.content_tokens(
        "autosomal dominant hypocalcemia 1"
    ) & audit_mod.content_tokens("renal-hepatic-pancreatic dysplasia 1")


def test_subtype_curie_is_not_a_mismatch(tmp_path):
    root = _tree(tmp_path)
    _entry(root, "Bardet-Biedl_Syndrome", "MONDO:0015229")
    report = _report(
        root,
        "Bardet-Biedl_Syndrome",
        "Group: MONDO:0015229. Subtype BBS1: MONDO:0008854.\n",
    )
    [result] = _run(root, report)
    assert result.status == "OK"
    verdicts = {term.curie: term.verdict for term in result.cited}
    assert verdicts == {"MONDO:0015229": "EXPECTED", "MONDO:0008854": "RELATED"}


def test_expected_term_falls_back_to_the_stub(tmp_path):
    root = _tree(tmp_path)
    (root / "stubs" / "Achondroplasia.yaml").write_text(
        "mondo_id: MONDO:0007037\nlabel: achondroplasia\n", encoding="utf-8"
    )
    report = _report(root, "Achondroplasia", "MONDO:0007037\n", provider="falcon")
    [result] = _run(root, report)
    assert result.status == "OK"
    assert result.expected_source == "stubs/Achondroplasia.yaml"


def test_uncached_curie_is_reported_not_compared(tmp_path):
    root = _tree(tmp_path)
    _entry(root, "Achondroplasia", "MONDO:0007037")
    report = _report(root, "Achondroplasia", "See MONDO:0099999.\n")
    [result] = _run(root, report)
    assert result.status == "UNCACHED"
    assert result.cited[0].verdict == "UNCACHED"


def test_unresolvable_slug_and_curie_free_report_are_skipped(tmp_path):
    root = _tree(tmp_path)
    _entry(root, "Achondroplasia", "MONDO:0007037")
    orphan = _report(root, "No_Such_Entry", "MONDO:0007037\n")
    bare = _report(
        root, "Achondroplasia", "No identifiers at all.\n", provider="falcon"
    )
    results = {
        result.slug + result.report: result for result in _run(root, orphan, bare)
    }
    assert all(result.status == "SKIPPED" for result in results.values())
    reasons = sorted(result.reason for result in results.values())
    assert reasons[0].startswith("no kb/disorders or stubs/")
    assert reasons[1] == "the report names no MONDO CURIE"


def test_walk_ignores_citation_sidecars(tmp_path):
    root = _tree(tmp_path)
    _report(root, "Achondroplasia", "MONDO:0007037\n")
    (
        root / "research" / "Achondroplasia-deep-research-openscientist.md.citations.md"
    ).write_text("MONDO:0008833\n", encoding="utf-8")
    names = [path.name for path in audit_mod.iter_reports(root / "research")]
    assert names == ["Achondroplasia-deep-research-openscientist.md"]


def test_cli_formats_exit_zero_and_write_nothing_to_research(tmp_path, capsys):
    root = _tree(tmp_path)
    _entry(root, "Autosomal_Dominant_Hypocalcemia_1", "MONDO:0011013")
    _report(root, "Autosomal_Dominant_Hypocalcemia_1", "MONDO:0008833\n")
    before = sorted(p.name for p in (root / "research").iterdir())

    assert audit_mod.main(["--root", str(root)]) == 0
    text = capsys.readouterr().out
    assert "MISMATCH  1" in text
    assert "MONDO:0008833 'renal-hepatic-pancreatic dysplasia 1'" in text

    assert audit_mod.main(["--root", str(root), "--format", "json"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["summary"]["MISMATCH"] == 1
    assert payload["reports"][0]["cited"][0]["curie"] == "MONDO:0008833"

    assert audit_mod.main(["--root", str(root), "--format", "tsv"]) == 0
    lines = capsys.readouterr().out.splitlines()
    assert lines[0].split("\t")[:3] == ["report", "slug", "status"]
    assert lines[1].split("\t")[2] == "MISMATCH"

    assert sorted(p.name for p in (root / "research").iterdir()) == before
