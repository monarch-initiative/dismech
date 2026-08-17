"""Tests for the affirmative reference/snippet audit (issue #7252).

``linkml-reference-validator`` reports ``Total checks: 0`` on a clean run because
the counter it echoes holds *issues found*, not checks performed. These tests
cover the downstream mitigation: a read-only, offline count of the
reference/snippet pairs actually verified against ``references_cache/``.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from dismech.reference_snippet_audit import (
    DEFAULT_SCHEMA,
    CachedReferenceIndex,
    PairOutcome,
    SnippetPair,
    audit_files,
    check_pair,
    discover_field_names,
    load_cache_dir,
    load_skip_prefixes,
    main,
)

ROOT = Path(__file__).parent.parent

ABSTRACT = (
    "Vici syndrome is caused by recessive mutations in EPG5. "
    "Affected individuals show agenesis of the corpus callosum and cataracts."
)


def _write_cache(
    cache_dir: Path,
    filename: str,
    content: str,
    content_type: str = "full_text_html",
) -> Path:
    """Write one cache file.

    ``content_type`` defaults to a full-text cache, so a snippet that is absent
    reads as a genuine mismatch. Pass ``abstract_only`` to exercise the
    incomplete-cache path added in #7450.
    """
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / filename
    path.write_text(
        "---\n"
        f'reference_id: "{filename[:-3].replace("_", ":", 1)}"\n'
        'title: "A real paper"\n'
        "authors:\n"
        "- Doe J\n"
        "journal: Example Journal\n"
        f"content_type: {content_type}\n"
        "---\n\n"
        f"{content}\n",
        encoding="utf-8",
    )
    return path


def _write_entry(path: Path, snippets: list[tuple[str, str]]) -> Path:
    lines = ["name: Test Disease", "evidence:"]
    for reference, snippet in snippets:
        lines.append(f"- reference: {reference}")
        lines.append("  supports: SUPPORT")
        lines.append(f"  snippet: {snippet!r}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _audit(tmp_path: Path, snippets: list[tuple[str, str]], **kwargs):
    entry = _write_entry(tmp_path / "entry.yaml", snippets)
    return audit_files([entry], cache_dir=tmp_path / "references_cache", **kwargs)


def test_counts_every_verified_pair(tmp_path: Path) -> None:
    _write_cache(tmp_path / "references_cache", "PMID_123.md", ABSTRACT)

    report = _audit(
        tmp_path,
        [
            ("PMID:123", "recessive mutations in EPG5"),
            ("PMID:123", "agenesis of the corpus callosum"),
        ],
    )

    assert (report.total, report.verified) == (2, 2)
    assert report.mismatched == []
    # The whole point of #7252: a clean run must not read as "0".
    assert "2/2 verified" in report.summary_line()


def test_reports_snippet_absent_from_cached_text(tmp_path: Path) -> None:
    _write_cache(tmp_path / "references_cache", "PMID_123.md", ABSTRACT)

    report = _audit(
        tmp_path,
        [
            ("PMID:123", "recessive mutations in EPG5"),
            ("PMID:123", "The moon is made of green cheese."),
        ],
    )

    assert (report.total, report.verified) == (2, 1)
    assert len(report.mismatched) == 1
    unverified = report.mismatched[0]
    assert unverified.pair.location == "evidence[1].snippet"
    assert "green cheese" in unverified.reason
    assert "1 not found in cached text" in report.summary_line()


def test_matching_mirrors_validator_normalization(tmp_path: Path) -> None:
    """Case, punctuation, whitespace, Greek letters, ``...`` and ``[...]``."""
    _write_cache(
        tmp_path / "references_cache",
        "PMID_123.md",
        "TGF-β signalling drives fibrosis;\nmyofibroblasts then deposit collagen.",
    )

    report = _audit(
        tmp_path,
        [
            ("PMID:123", "tgf beta signalling"),
            ("PMID:123", "drives fibrosis ... deposit collagen"),
            ("PMID:123", "myofibroblasts [i.e. activated fibroblasts] then deposit"),
        ],
    )

    assert (report.total, report.verified) == (3, 3)


def test_skips_configured_prefixes_without_counting_them_as_verified(
    tmp_path: Path,
) -> None:
    config = tmp_path / "config.yaml"
    config.write_text("skip_prefixes:\n  - MONDO\n", encoding="utf-8")
    _write_cache(tmp_path / "references_cache", "PMID_123.md", ABSTRACT)

    report = _audit(
        tmp_path,
        [
            ("PMID:123", "recessive mutations in EPG5"),
            ("MONDO:0012345", "not a literature reference"),
        ],
        config_path=config,
    )

    assert (report.total, report.verified, report.skipped_prefix) == (2, 1, 1)
    assert report.mismatched == []
    assert "skipped by prefix" in report.summary_line()


def test_uncached_reference_is_reported_separately_from_a_mismatch(
    tmp_path: Path,
) -> None:
    (tmp_path / "references_cache").mkdir()

    report = _audit(tmp_path, [("PMID:999", "anything at all")])

    assert (report.total, report.verified, report.not_cached) == (1, 0, 1)
    assert report.mismatched == []
    assert "not cached locally" in report.summary_line()


def test_resolves_cache_files_written_under_a_source_prefix(tmp_path: Path) -> None:
    """A bare ``NCT…`` id is cached as ``clinicaltrials_NCT….md`` (see #7252)."""
    _write_cache(
        tmp_path / "references_cache",
        "clinicaltrials_NCT06087757.md",
        "This study evaluates a novel therapy in Williams syndrome.",
    )

    report = _audit(tmp_path, [("NCT06087757", "a novel therapy in Williams syndrome")])

    assert (report.total, report.verified, report.not_cached) == (1, 1, 0)


def test_ambiguous_bare_identifier_is_not_resolved(tmp_path: Path) -> None:
    cache_dir = tmp_path / "references_cache"
    _write_cache(cache_dir, "foo_ABC1.md", "first source body")
    _write_cache(cache_dir, "bar_ABC1.md", "second source body")

    index = CachedReferenceIndex(cache_dir)

    assert index.resolve_cache_path("ABC1") is None


def test_unreadable_file_is_recorded_without_crashing(tmp_path: Path) -> None:
    broken = tmp_path / "broken.yaml"
    broken.write_text("name: [unclosed\n", encoding="utf-8")

    report = audit_files([broken], cache_dir=tmp_path / "references_cache")

    assert report.files == 0
    assert report.unreadable and "broken.yaml" in report.unreadable[0]


def test_empty_input_summary_does_not_claim_verification(tmp_path: Path) -> None:
    report = _audit(tmp_path, [])

    assert report.total == 0
    assert "no reference/snippet pairs" in report.summary_line()


def test_fields_are_discovered_from_schema_implements_annotations() -> None:
    excerpts, references = discover_field_names(ROOT / DEFAULT_SCHEMA)

    assert "snippet" in excerpts
    assert "reference" in references


def test_config_loaders_read_the_repository_config() -> None:
    config = ROOT / "conf" / "reference_validator_config.yaml"

    assert "MONDO" in load_skip_prefixes(config)
    assert load_cache_dir(config) == Path("references_cache")


def test_cli_is_advisory_by_default_and_gated_by_strict(tmp_path: Path, capsys) -> None:
    _write_cache(tmp_path / "references_cache", "PMID_123.md", ABSTRACT)
    entry = _write_entry(
        tmp_path / "entry.yaml", [("PMID:123", "The moon is made of green cheese.")]
    )
    args = [
        str(entry),
        "--cache-dir",
        str(tmp_path / "references_cache"),
        "--config",
        str(tmp_path / "missing-config.yaml"),
    ]

    assert main(args) == 0
    assert "0/1 verified" in capsys.readouterr().out
    assert main([*args, "--strict"]) == 1


def test_wrapper_appends_the_audit_line_to_validator_output(tmp_path: Path) -> None:
    """The wrapper prints the affirmative count without touching the exit code."""
    entry = _write_entry(tmp_path / "entry.yaml", [("PMID:123", "mutations in EPG5")])
    _write_cache(tmp_path / "references_cache", "PMID_123.md", ABSTRACT)

    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    fake_uv = bin_dir / "uv"
    # Stand in for the validator itself; the audit invocation (``uv run python -m
    # dismech.reference_snippet_audit ...``) is delegated to the real interpreter.
    fake_uv.write_text(
        "#!/usr/bin/env bash\n"
        'if [[ "$*" == *reference_snippet_audit* ]]; then\n'
        "  shift 2\n"
        f'  exec "{sys.executable}" "$@"\n'
        "fi\n"
        "printf '%s\\n' '  Total checks: 0'\n"
        "printf '%s\\n' '  All validations passed!'\n",
        encoding="utf-8",
    )
    fake_uv.chmod(0o755)

    env = {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}"}
    result = subprocess.run(
        [
            "bash",
            str(ROOT / "scripts" / "run_reference_validator.sh"),
            "validate",
            "data",
            str(entry),
            "--schema",
            str(ROOT / DEFAULT_SCHEMA),
            "--target-class",
            "Disease",
        ],
        capture_output=True,
        check=False,
        # Run from tmp_path so the audit's default references_cache/ is the
        # fixture cache, not the repository's.
        cwd=tmp_path,
        env=env,
        text=True,
    )

    assert result.returncode == 0
    assert "Total checks: 0" in result.stdout
    assert "Snippets checked: 1/1 verified" in result.stdout


def test_wrapper_audit_can_be_disabled(tmp_path: Path) -> None:
    fake_uv = tmp_path / "uv"
    fake_uv.write_text(
        "#!/usr/bin/env bash\nprintf '%s\\n' '  All validations passed!'\n",
        encoding="utf-8",
    )
    fake_uv.chmod(0o755)

    env = {
        **os.environ,
        "PATH": f"{tmp_path}{os.pathsep}{os.environ['PATH']}",
        "DISMECH_SKIP_SNIPPET_AUDIT": "1",
    }
    result = subprocess.run(
        [
            "bash",
            str(ROOT / "scripts" / "run_reference_validator.sh"),
            "validate",
            "data",
            "dummy.yaml",
        ],
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=env,
        text=True,
    )

    assert result.returncode == 0
    assert "Snippets checked" not in result.stdout


def test_literal_bracket_patterns_are_honoured_like_the_validator(
    tmp_path: Path,
) -> None:
    """Configured literal brackets are source text, not editorial notes.

    Upstream ``_split_query`` preserves bracketed content matching
    ``literal_bracket_patterns``; the audit must do the same or it would strip
    brackets the validator keeps and invent mismatches.
    """
    _write_cache(
        tmp_path / "references_cache",
        "PMID_123.md",
        "The [2Fe-2S] cluster is required for enzyme activity.",
    )
    config = tmp_path / "config.yaml"
    config.write_text('literal_bracket_patterns:\n  - "\\\\d"\n', encoding="utf-8")

    snippets = [("PMID:123", "The [2Fe-2S] cluster is required")]

    with_patterns = _audit(tmp_path, snippets, config_path=config)
    assert (with_patterns.total, with_patterns.verified) == (1, 1)

    # Without the patterns the bracket is stripped as an editorial note, the
    # remaining fragments no longer line up, and the pair reads as a mismatch --
    # the exact false positive that config parity prevents.
    without_patterns = _audit(
        tmp_path, snippets, config_path=tmp_path / "missing-config.yaml"
    )
    assert without_patterns.verified == 0


def test_mismatch_detail_is_capped_but_the_count_is_not(tmp_path: Path) -> None:
    _write_cache(tmp_path / "references_cache", "PMID_123.md", ABSTRACT)

    report = _audit(
        tmp_path, [("PMID:123", f"fabricated quote number {i}") for i in range(25)]
    )

    assert len(report.mismatched) == 25
    assert "0/25 verified" in report.summary_line()
    rendered = report.format(max_mismatches=20)
    assert rendered.count("Text part not found as substring") == 20
    assert "... and 5 more" in rendered


def test_body_cache_eviction_does_not_change_results(tmp_path: Path) -> None:
    """A bounded memo caps peak memory without affecting verification."""
    cache_dir = tmp_path / "references_cache"
    _write_cache(cache_dir, "PMID_1.md", "first body mentions alpha synuclein")
    _write_cache(cache_dir, "PMID_2.md", "second body mentions beta amyloid")

    index = CachedReferenceIndex(cache_dir, cache_size=1)
    pairs = [
        ("PMID:1", "alpha synuclein"),
        ("PMID:2", "beta amyloid"),
        ("PMID:1", "first body mentions"),
    ]
    for reference, snippet in pairs:
        pair = SnippetPair(
            path=tmp_path / "entry.yaml",
            location="evidence[0].snippet",
            reference_id=reference,
            snippet=snippet,
        )
        assert check_pair(index, pair) is PairOutcome.VERIFIED

    assert len(index._normalized) == 1


def test_wrapper_stays_quiet_when_the_validator_crashes(tmp_path: Path) -> None:
    """A traceback means the run never happened; don't print a reassuring count."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    fake_uv = bin_dir / "uv"
    fake_uv.write_text(
        "#!/usr/bin/env bash\n"
        "printf '%s\\n' 'Traceback (most recent call last):'\n"
        "printf '%s\\n' 'RuntimeError: boom'\n"
        "exit 1\n",
        encoding="utf-8",
    )
    fake_uv.chmod(0o755)

    env = {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}"}
    result = subprocess.run(
        [
            "bash",
            str(ROOT / "scripts" / "run_reference_validator.sh"),
            "validate",
            "data",
            "dummy.yaml",
        ],
        capture_output=True,
        check=False,
        cwd=tmp_path,
        env=env,
        text=True,
    )

    assert result.returncode == 1
    assert "Snippets checked" not in result.stdout
    assert "snippet audit skipped" in result.stderr


def test_wrapper_reports_an_arg_order_it_cannot_parse(tmp_path: Path) -> None:
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    fake_uv = bin_dir / "uv"
    fake_uv.write_text(
        "#!/usr/bin/env bash\nprintf '%s\\n' '  All validations passed!'\n",
        encoding="utf-8",
    )
    fake_uv.chmod(0o755)

    env = {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}"}
    result = subprocess.run(
        [
            "bash",
            str(ROOT / "scripts" / "run_reference_validator.sh"),
            "validate",
            "data",
            "--schema",
            str(ROOT / DEFAULT_SCHEMA),
            "entry.yaml",
        ],
        capture_output=True,
        check=False,
        cwd=tmp_path,
        env=env,
        text=True,
    )

    assert result.returncode == 0
    assert "no data files found before the first option" in result.stderr


def test_per_file_validation_loops_surface_the_snippet_count() -> None:
    """The three ``ref_output``-capturing loops must not swallow the audit line."""
    justfile = (ROOT / "project.justfile").read_text()

    assert justfile.count("grep -o 'Snippets checked:.*'") == 3
    assert justfile.count('echo "  ✓ OK${snippet_line:+ ($snippet_line)}"') == 3


# --- Cache-defect tolerance and the abstract-only state (issue #7450) --------
#
# NOTE: these use DOI references, which the repository config lists in
# ``skip_prefixes`` -- the very gap #7450 is about. They therefore audit against
# a config that skips nothing, or they would silently test nothing at all.


def _audit_all_prefixes(tmp_path: Path, snippets: list[tuple[str, str]], **kwargs):
    """Audit with prefix skipping disabled, so DOI pairs are really checked."""
    config = tmp_path / "no_skips.yaml"
    config.write_text("skip_prefixes: []\n", encoding="utf-8")
    return _audit(tmp_path, snippets, config_path=config, **kwargs)


#
# ~6% of KB snippets cite a DOI, which `skip_prefixes` currently hides from the
# validator entirely. Un-skipping it surfaced 86 mismatches, but most were
# defects in the *cache* rather than in the curation. These cover the two
# mechanical classes and the incomplete-cache state.


def test_folds_pdf_ligatures_in_the_cached_text(tmp_path: Path) -> None:
    """A PDF extractor emits 'ﬁ' (U+FB01); the curator typed 'fi'."""
    _write_cache(
        tmp_path / "references_cache",
        "DOI_10.1000_x.md",
        "Congo red staining revealed amyloid ﬁbrils in the biopsy.",
        content_type="full_text_pdf",
    )

    report = _audit_all_prefixes(
        tmp_path, [("DOI:10.1000/x", "amyloid fibrils in the biopsy")]
    )

    assert (report.verified, report.verified_relaxed) == (0, 1)
    assert report.mismatched == []
    assert "1/1 verified" in report.summary_line()
    assert "1 only after cache-defect normalization" in report.summary_line()


def test_tolerates_words_joined_by_stripped_inline_markup(tmp_path: Path) -> None:
    """HTML extraction drops <i> without a space: 'the *ANAPC7* locus'."""
    _write_cache(
        tmp_path / "references_cache",
        "DOI_10.1000_y.md",
        "We found a deletion within theANAPC7locus in all probands.",
        content_type="full_text_html",
    )

    report = _audit_all_prefixes(
        tmp_path, [("DOI:10.1000/y", "a deletion within the ANAPC7 locus")]
    )

    assert (report.verified, report.verified_relaxed) == (0, 1)
    assert report.mismatched == []


def test_relaxed_pass_does_not_rescue_a_genuinely_absent_quote(tmp_path: Path) -> None:
    """Ignoring word gaps must not admit text that simply is not there."""
    _write_cache(tmp_path / "references_cache", "DOI_10.1000_z.md", ABSTRACT)

    report = _audit_all_prefixes(
        tmp_path, [("DOI:10.1000/z", "The moon is made of green cheese.")]
    )

    assert (report.verified, report.verified_relaxed) == (0, 0)
    assert len(report.mismatched) == 1


def test_relaxed_pass_does_not_reorder_words(tmp_path: Path) -> None:
    """Characters must still appear contiguously and in order."""
    _write_cache(tmp_path / "references_cache", "DOI_10.1000_o.md", "alpha beta gamma")

    report = _audit_all_prefixes(tmp_path, [("DOI:10.1000/o", "gamma beta alpha")])

    assert report.verified_relaxed == 0
    assert len(report.mismatched) == 1


def test_a_strictly_matching_snippet_never_reaches_the_relaxed_pass(
    tmp_path: Path,
) -> None:
    _write_cache(tmp_path / "references_cache", "PMID_123.md", ABSTRACT)

    report = _audit(tmp_path, [("PMID:123", "recessive mutations in EPG5")])

    assert (report.verified, report.verified_relaxed) == (1, 0)


def test_abstract_only_cache_is_its_own_state_not_a_mismatch(tmp_path: Path) -> None:
    _write_cache(
        tmp_path / "references_cache",
        "DOI_10.1000_a.md",
        ABSTRACT,
        content_type="abstract_only",
    )

    report = _audit_all_prefixes(
        tmp_path, [("DOI:10.1000/a", "a sentence from the full text")]
    )

    assert report.mismatched == []
    assert report.abstract_only == 1
    assert "quoted beyond an abstract-only cache" in report.summary_line()
    assert "full text may contain the excerpt" in report.format()
    # Not verified either: nothing was established in either direction.
    assert report.verified == 0


def test_a_full_text_cache_still_yields_a_hard_mismatch(tmp_path: Path) -> None:
    """The abstract-only carve-out must not leak to full-text caches."""
    _write_cache(
        tmp_path / "references_cache",
        "DOI_10.1000_b.md",
        ABSTRACT,
        content_type="full_text_pdf",
    )

    report = _audit_all_prefixes(
        tmp_path, [("DOI:10.1000/b", "a sentence from the full text")]
    )

    assert report.abstract_only == 0
    assert len(report.mismatched) == 1


def test_strict_still_fails_on_an_abstract_only_pair_by_default(
    tmp_path: Path,
) -> None:
    """An abstract-only pair is unverified, so --strict must not wave it through."""
    _write_cache(
        tmp_path / "references_cache",
        "DOI_10.1000_c.md",
        ABSTRACT,
        content_type="abstract_only",
    )
    entry = _write_entry(
        tmp_path / "entry.yaml", [("DOI:10.1000/c", "text from the full text")]
    )
    argv = [
        str(entry),
        "--cache-dir",
        str(tmp_path / "references_cache"),
        "--config",
        str(tmp_path / "missing_config.yaml"),
        "--strict",
    ]

    assert main(argv) == 1
    assert main([*argv, "--allow-abstract-only"]) == 0


def test_unskip_prefix_audits_a_configured_skip(tmp_path: Path) -> None:
    """Measure the coverage skip_prefixes hides, without changing the config."""
    config = tmp_path / "config.yaml"
    config.write_text("skip_prefixes:\n  - DOI\n", encoding="utf-8")
    _write_cache(tmp_path / "references_cache", "DOI_10.1000_d.md", ABSTRACT)
    pairs = [("DOI:10.1000/d", "recessive mutations in EPG5")]

    skipped = _audit(tmp_path, pairs, config_path=config)
    assert (skipped.skipped_prefix, skipped.verified) == (1, 0)

    audited = _audit(tmp_path, pairs, config_path=config, unskip_prefixes=["doi"])
    assert (audited.skipped_prefix, audited.verified) == (0, 1)


def test_content_type_is_read_from_the_cache_frontmatter(tmp_path: Path) -> None:
    cache_dir = tmp_path / "references_cache"
    _write_cache(cache_dir, "DOI_10.1000_e.md", ABSTRACT, content_type="abstract_only")
    index = CachedReferenceIndex(cache_dir)

    assert index.content_type("DOI:10.1000/e") == "abstract_only"
    assert index.is_abstract_only("DOI:10.1000/e")
    assert index.content_type("DOI:10.1000/nope") is None
    assert not index.is_abstract_only("DOI:10.1000/nope")


def test_ligature_folding_is_symmetric() -> None:
    fold = CachedReferenceIndex.fold_ligatures
    assert fold("amyloid ﬁbrils") == "amyloid fibrils"
    assert fold("aﬂatoxin") == "aflatoxin"
    assert fold("amyloid fibrils") == "amyloid fibrils"


# --- Bracketed abbreviations in the shipped config (issue #8597) -------------
#
# The fix for #8597 is a data change -- two `literal_bracket_patterns` entries in
# conf/reference_validator_config.yaml -- so the tests that matter exercise the
# committed config rather than a synthetic one. That config is read by the real
# `linkml-reference-validator` behind `just validate-disorders` as well as by
# this audit, so what these assert holds for the gating check too.

REPO_CONFIG = ROOT / "conf" / "reference_validator_config.yaml"


def _repo_index(cache_dir: Path) -> CachedReferenceIndex:
    from dismech.reference_snippet_audit import load_literal_bracket_patterns

    return CachedReferenceIndex(
        cache_dir, literal_bracket_patterns=load_literal_bracket_patterns(REPO_CONFIG)
    )


def test_inline_abbreviation_definitions_survive_normalization(
    tmp_path: Path,
) -> None:
    """A verbatim quote spanning `[APTT]` verifies -- the #8597 regression.

    Structured abstracts define abbreviations in square brackets on first use,
    and that is exactly where the substantive clause tends to sit. Stripping the
    bracket from the query but not from the cached text left `time -adjusted`,
    which failed as "not found as substring" and read as a paraphrase.
    """
    _write_cache(
        tmp_path / "references_cache",
        "PMID_37959386.md",
        "aHIT patients are at risk for treatment failure with (activated "
        "partial thromboplastin time [APTT]-adjusted) direct thrombin "
        "inhibitor (DTI) therapy.",
    )

    report = _audit(
        tmp_path,
        [
            (
                "PMID:37959386",
                (
                    "at risk for treatment failure with (activated partial "
                    "thromboplastin time [APTT]-adjusted) direct thrombin "
                    "inhibitor (DTI) therapy"
                ),
            )
        ],
        config_path=REPO_CONFIG,
    )

    assert (report.total, report.verified) == (1, 1)


def test_bracketed_percentages_survive_normalization(tmp_path: Path) -> None:
    """`[28, 62%]` is a reported figure, not a citation marker."""
    _write_cache(
        tmp_path / "references_cache",
        "PMID_7490992.md",
        "followed by neurological complications (cerebellar ataxia, myoclonus "
        "[28, 62%]) in the fourth decade.",
    )

    report = _audit(
        tmp_path,
        [
            (
                "PMID:7490992",
                (
                    "neurological complications (cerebellar ataxia, myoclonus "
                    "[28, 62%]) in the fourth decade"
                ),
            )
        ],
        config_path=REPO_CONFIG,
    )

    assert (report.total, report.verified) == (1, 1)


def test_citation_markers_and_editorial_glosses_are_still_stripped(
    tmp_path: Path,
) -> None:
    """The narrowing must not cost the feature bracket stripping exists for.

    Inline numeric citation markers and curator glosses are absent from the
    source text by definition, so both have to keep being dropped. The gloss
    examples are the ones actually curated in kb/ today.
    """
    index = _repo_index(tmp_path / "references_cache")
    for citation_marker in ("12", "3,4", "111 - 113", "9-11"):
        assert not index.is_literal_bracket(citation_marker)
    for gloss in ("IL-6", "sic, correct designation is R501X", "of dimethyltryptamine"):
        assert not index.is_literal_bracket(gloss)
    for source_text in ("APTT", "GERD", "RR", "CI", "DTI", "28, 62%", "95% CI 1.2-2.3"):
        assert index.is_literal_bracket(source_text)

    _write_cache(
        tmp_path / "references_cache",
        "PMID_123.md",
        "Filaggrin variants predispose to atopic dermatitis.",
    )
    report = _audit(
        tmp_path,
        [("PMID:123", "Filaggrin variants [FLG, previously reported] predispose")],
        config_path=REPO_CONFIG,
    )

    assert (report.total, report.verified) == (1, 1)


def test_a_stripped_bracket_names_itself_as_the_cause_of_a_mismatch(
    tmp_path: Path,
) -> None:
    """Do not report "not found as substring" when stripping is the reason.

    That message means "the curator paraphrased", which is the one diagnosis
    this failure is not. When the quote matches the cache with its brackets
    kept, say which span was dropped and where the knob lives.
    """
    cache_dir = tmp_path / "references_cache"
    _write_cache(
        cache_dir, "PMID_123.md", "the recurrence rate (relative risk [xRRx], 2.80)"
    )
    index = CachedReferenceIndex(cache_dir)  # no literal patterns configured
    pair = SnippetPair(
        path=tmp_path / "entry.yaml",
        location="evidence[0].snippet",
        reference_id="PMID:123",
        snippet="the recurrence rate (relative risk [xRRx], 2.80)",
    )

    outcome = check_pair(index, pair)

    assert outcome.outcome is not PairOutcome.ABSTRACT_ONLY
    assert "[xRRx]" in outcome.reason
    assert "literal_bracket_patterns" in outcome.reason


def test_a_genuine_misquote_is_not_blamed_on_brackets(tmp_path: Path) -> None:
    """The hint fires only when keeping the brackets would actually match."""
    cache_dir = tmp_path / "references_cache"
    _write_cache(cache_dir, "PMID_123.md", ABSTRACT)
    index = CachedReferenceIndex(cache_dir)
    pair = SnippetPair(
        path=tmp_path / "entry.yaml",
        location="evidence[0].snippet",
        reference_id="PMID:123",
        snippet="Vici syndrome is caused by [dominant] mutations in EPG5",
    )

    outcome = check_pair(index, pair)

    assert "literal_bracket_patterns" not in outcome.reason


def test_the_hint_names_the_culprit_when_a_gloss_shares_the_snippet(
    tmp_path: Path,
) -> None:
    """A gloss and a source-text bracket can sit in one snippet.

    Requiring every stripped span to be restorable would go silent here, which
    is the case a curator most needs named: one bracket is correctly stripped
    (the curator wrote it) and the other is source text the config does not yet
    keep. Only the second is the culprit, and only it should be reported.
    """
    cache_dir = tmp_path / "references_cache"
    _write_cache(
        cache_dir,
        "PMID_123.md",
        "The recurrence rate (relative risk [xRRx], 2.80) was higher.",
    )
    index = CachedReferenceIndex(cache_dir)  # no literal patterns configured
    pair = SnippetPair(
        path=tmp_path / "entry.yaml",
        location="evidence[0].snippet",
        reference_id="PMID:123",
        snippet=(
            "The recurrence rate [after curettage] (relative risk [xRRx], 2.80) "
            "was higher."
        ),
    )

    outcome = check_pair(index, pair)

    assert "[xRRx]" in outcome.reason
    assert "[after curettage]" not in outcome.reason


def test_the_hint_reads_as_a_sentence_with_two_culprits(tmp_path: Path) -> None:
    """Two dropped spans should read '[A] and [B] are kept', not '[A], [B] is'."""
    cache_dir = tmp_path / "references_cache"
    _write_cache(cache_dir, "PMID_123.md", "the rate [xAx] rose and [xBx] fell.")
    index = CachedReferenceIndex(cache_dir)  # no literal patterns configured
    pair = SnippetPair(
        path=tmp_path / "entry.yaml",
        location="evidence[0].snippet",
        reference_id="PMID:123",
        snippet="the rate [xAx] rose and [xBx] fell.",
    )

    outcome = check_pair(index, pair)

    assert "[xAx] and [xBx] are kept" in outcome.reason
