"""Tests for scripts/dr_reference_validation_census.py (dismech #8841)."""

from __future__ import annotations

import importlib.util
import json
import sys
from io import StringIO
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "dr_reference_validation_census.py"
SPEC = importlib.util.spec_from_file_location("dr_reference_validation_census", SCRIPT_PATH)
assert SPEC and SPEC.loader
census = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = census  # dataclasses under `from __future__ import annotations`
SPEC.loader.exec_module(census)


def _write(path: Path, frontmatter: str | None, body: str) -> None:
    text = f"---\n{frontmatter}\n---\n{body}" if frontmatter is not None else body
    path.write_text(text, encoding="utf-8")


def _populate(research_dir: Path) -> None:
    _write(
        research_dir / "Foo-deep-research-falcon.md",
        "title: Foo\nreference_validation:\n  total_references: 10\n  verified: 8\n  not_found: 2\n"
        "  quotes_checked: 4\n  quotes_valid: 3\n  quotes_unsupported: 1\n  relevance_assessed: 10\n"
        "  on_topic: 7\n  off_topic: 1\n  needs_review: true\n  validator_version: 0.2.10\n",
        "# Foo\n\n## Reference Validation\n\n| Checked | 10 |\n",
    )
    # Keys upstream omits when there is nothing to report count as zero.
    # Frontmatter `provider:` wins over the filename suffix; a malformed counter
    # counts as zero and is reported as a coercion failure.
    _write(
        research_dir / "Bar-deep-research-openscientist-2026-07-30.md",
        "provider: openscientist\nreference_validation:\n  total_references: 5\n  verified: 5\n  not_found: n/a\n",
        "# Bar\n",
    )
    # Retro-fitted: body section, no frontmatter block.
    _write(
        research_dir / "Baz-deep-research-falcon.md",
        "title: Baz\n",
        "# Baz\n\n## Reference Validation\n\n| Checked | 3 |\n",
    )
    # Never validated, and no frontmatter at all.
    _write(research_dir / "Qux-deep-research-claude_code.md", None, "# Qux\n")
    # `just research-module` / `research-surrogacy` write into subdirectories;
    # the walk must be recursive. A non-integral float counter is a failure.
    (research_dir / "modules").mkdir()
    _write(
        research_dir / "modules" / "fibrotic_response-deep-research-falcon.md",
        "provider: falcon\nreference_validation:\n  total_references: 2\n  verified: 1\n  not_found: 1.5\n",
        "# module\n",
    )
    # Artifact folders hold no *-deep-research-*.md reports and are skipped.
    (research_dir / "Foo-deep-research-falcon_artifacts").mkdir()
    _write(research_dir / "Foo-deep-research-falcon_artifacts" / "artifact-00.md", None, "PMID:2\n")
    # Sidecar and non-report files are ignored.
    _write(research_dir / "Foo-deep-research-falcon.md.citations.md", None, "PMID:1\n")
    _write(research_dir / "notes.md", "reference_validation:\n  total_references: 99\n", "ignored\n")


def test_classification_and_sums(tmp_path: Path) -> None:
    _populate(tmp_path)
    rows = census.collect(tmp_path)
    by_name = {row.path: row for row in rows}
    assert set(by_name) == {
        "Foo-deep-research-falcon.md",
        "Bar-deep-research-openscientist-2026-07-30.md",
        "Baz-deep-research-falcon.md",
        "Qux-deep-research-claude_code.md",
        "modules/fibrotic_response-deep-research-falcon.md",
    }
    module = by_name["modules/fibrotic_response-deep-research-falcon.md"]
    assert module.status == census.STATUS_FRONTMATTER
    assert module.counters["not_found"] == 0
    assert module.coercion_failures == 1
    bar = by_name["Bar-deep-research-openscientist-2026-07-30.md"]
    assert bar.provider == "openscientist"
    assert bar.coercion_failures == 1
    assert by_name["Foo-deep-research-falcon.md"].status == census.STATUS_FRONTMATTER
    assert by_name["Foo-deep-research-falcon.md"].needs_review is True
    assert bar.status == census.STATUS_FRONTMATTER
    assert bar.counters["not_found"] == 0
    assert bar.counters["unverifiable"] == 0
    assert by_name["Baz-deep-research-falcon.md"].status == census.STATUS_BODY_ONLY
    assert by_name["Qux-deep-research-claude_code.md"].status == census.STATUS_UNVALIDATED

    overall, by_provider = census.summarize(rows)
    assert (overall.reports, overall.frontmatter, overall.body_only, overall.unvalidated) == (5, 3, 1, 1)
    assert overall.needs_review == 1
    assert overall.coercion_failures == 2
    assert overall.counters["total_references"] == 17
    assert overall.counters["not_found"] == 2
    assert overall.rate("not_found", "total_references") == 2 / 17
    assert overall.relevance_undecided == 2  # 10 assessed - 7 on - 1 off
    assert overall.rate("quotes_unsupported", "quotes_checked") == 1 / 4
    assert overall.rate("off_topic", "nonexistent") is None
    assert set(by_provider) == {"falcon", "openscientist", "claude_code"}
    assert by_provider["falcon"].reports == 3
    assert by_provider["falcon"].frontmatter == 2
    assert by_provider["falcon"].body_only == 1


def test_summary_output_mentions_each_bucket(tmp_path: Path) -> None:
    _populate(tmp_path)
    overall, by_provider = census.summarize(census.collect(tmp_path))
    out = StringIO()
    census.write_summary(out, overall, by_provider)
    text = out.getvalue()
    assert "validated (frontmatter block):  3" in text
    assert "retro-fitted (body section only): 1" in text
    assert "unvalidated:                    1" in text
    assert "not found:          2  (11.8%)" in text
    assert "undecided:          2  (assessed, neither on nor off topic)" in text
    assert "unsupported:        1  (25.0%)" in text
    assert "openscientist" in text and "falcon" in text
    # claude_code has reports but none validated: omitted unless asked for.
    assert "claude_code" not in text
    assert "1 provider(s) with no validated reports omitted" in text
    assert "WARNING: 2 counter value(s)" in text
    out = StringIO()
    census.write_summary(out, overall, by_provider, all_providers=True)
    assert "claude_code" in out.getvalue()


def test_tsv_json_and_needs_review_via_main(tmp_path: Path, capsys) -> None:
    _populate(tmp_path)

    assert census.main(["--research-dir", str(tmp_path), "--format", "tsv", "--validated-only"]) == 0
    lines = capsys.readouterr().out.splitlines()
    assert lines[0].split("\t")[:4] == ["path", "disorder", "provider", "status"]
    assert len(lines) == 5  # header + Foo + Bar + Baz + module (Qux dropped by --validated-only)

    out_file = tmp_path / "census.json"
    assert census.main(["--research-dir", str(tmp_path), "--format", "json", "--out", str(out_file)]) == 0
    payload = json.loads(out_file.read_text())
    assert payload["totals"]["frontmatter"] == 3
    assert payload["totals"]["relevance_undecided"] == 2
    assert payload["totals"]["rates"]["not_found_rate"] == 2 / 17
    assert payload["by_provider"]["openscientist"]["counters"]["verified"] == 5
    assert len(payload["reports"]) == 5

    assert census.main(["--research-dir", str(tmp_path), "--needs-review"]) == 0
    text = capsys.readouterr().out
    assert "1 report(s) flagged needs_review" in text
    assert "Foo-deep-research-falcon.md" in text
    assert "Bar-deep-research" not in text
    assert census.main(["--research-dir", str(tmp_path), "--all-providers"]) == 0
    assert "claude_code" in capsys.readouterr().out


def test_missing_research_dir_is_an_error(tmp_path: Path) -> None:
    assert census.main(["--research-dir", str(tmp_path / "nope")]) == 2
