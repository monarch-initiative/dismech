"""Guard test: no empty (non-NO_EVIDENCE) evidence snippets in kb/.

An `EvidenceItem` with `snippet: ""` passes `linkml-reference-validator`,
`count-verified-snippets`, and `scripts/check_environmental_evidence.py`
vacuously -- see scripts/check_empty_snippets.py and dismech issue #8550.

Unlike the sibling snippet guards (title-quoting, too-short), this one ships
with no baseline: a repo-wide scan found zero non-NO_EVIDENCE empty snippets,
so it is a hard gate rather than a ratchet.
"""

from pathlib import Path

from scripts.check_empty_snippets import find_violations, scan_repo

ROOT = Path(__file__).resolve().parents[1]

EXCERPT_FIELDS = frozenset({"snippet"})
REFERENCE_FIELDS = frozenset({"reference"})


def test_no_empty_non_no_evidence_snippets_in_kb():
    findings = scan_repo()
    formatted = [
        f"{rel}:{location}  {reference_id}  supports={supports}"
        for rel, location, reference_id, supports in findings
    ]
    assert not formatted, (
        "Empty (non-NO_EVIDENCE) evidence snippet(s) detected. An evidence "
        "item that SUPPORTs/PARTIALly supports/REFUTEs a claim must quote "
        "real text -- quote the real sentence, change `supports` to "
        "NO_EVIDENCE if that is genuinely what happened, or drop the item if "
        "the reference has no quotable text:\n  " + "\n  ".join(formatted)
    )


def test_flags_an_empty_support_snippet():
    data = {
        "phenotypes": [
            {
                "evidence": [
                    {"reference": "PMID:1", "supports": "SUPPORT", "snippet": ""}
                ]
            }
        ]
    }
    findings = list(find_violations(data, EXCERPT_FIELDS, REFERENCE_FIELDS))
    assert findings == [
        ("phenotypes[0].evidence[0].snippet", "PMID:1", "SUPPORT")
    ]


def test_flags_a_whitespace_only_snippet():
    data = {"evidence": [{"reference": "PMID:1", "supports": "REFUTE", "snippet": "   "}]}
    findings = list(find_violations(data, EXCERPT_FIELDS, REFERENCE_FIELDS))
    assert len(findings) == 1


def test_flags_an_empty_snippet_with_no_supports_field():
    # A missing `supports` is not the NO_EVIDENCE exemption.
    data = {"evidence": [{"reference": "PMID:1", "snippet": ""}]}
    findings = list(find_violations(data, EXCERPT_FIELDS, REFERENCE_FIELDS))
    assert findings == [("evidence[0].snippet", "PMID:1", None)]


def test_no_evidence_items_are_exempt_by_default():
    data = {"evidence": [{"reference": "PMID:1", "supports": "NO_EVIDENCE", "snippet": ""}]}
    assert not list(find_violations(data, EXCERPT_FIELDS, REFERENCE_FIELDS))


def test_include_exempt_surfaces_no_evidence_items_too():
    data = {"evidence": [{"reference": "PMID:1", "supports": "NO_EVIDENCE", "snippet": ""}]}
    findings = list(
        find_violations(data, EXCERPT_FIELDS, REFERENCE_FIELDS, include_exempt=True)
    )
    assert findings == [("evidence[0].snippet", "PMID:1", "NO_EVIDENCE")]


def test_non_empty_snippet_is_never_flagged():
    data = {"evidence": [{"reference": "PMID:1", "supports": "SUPPORT", "snippet": "real text"}]}
    assert not list(find_violations(data, EXCERPT_FIELDS, REFERENCE_FIELDS))


def test_snippet_without_a_sibling_reference_is_ignored():
    data = {"snippet": ""}
    assert not list(find_violations(data, EXCERPT_FIELDS, REFERENCE_FIELDS))


def test_scan_dir_is_the_kb_root_not_just_disorders():
    import scripts.check_empty_snippets as ces

    assert ces.SCAN_DIR == ROOT / "kb"


def test_scan_repo_finds_a_synthetic_violation(tmp_path):
    disorders = tmp_path / "kb" / "disorders"
    disorders.mkdir(parents=True)
    (disorders / "X.yaml").write_text(
        "name: T\n"
        "phenotypes:\n"
        "- name: Foo\n"
        "  evidence:\n"
        "  - reference: PMID:1\n"
        "    supports: SUPPORT\n"
        "    snippet: ''\n",
        encoding="utf-8",
    )
    findings = scan_repo(scan_dir=tmp_path / "kb", rel_to=tmp_path)
    assert findings == [
        (
            "kb/disorders/X.yaml",
            "phenotypes[0].evidence[0].snippet",
            "PMID:1",
            "SUPPORT",
        )
    ]


def test_scan_repo_skips_unparseable_yaml(tmp_path, capsys):
    disorders = tmp_path / "kb" / "disorders"
    disorders.mkdir(parents=True)
    (disorders / "bad.yaml").write_text("not: [valid: yaml", encoding="utf-8")
    findings = scan_repo(scan_dir=tmp_path / "kb", rel_to=tmp_path)
    assert findings == []
    assert "skipping unparseable" in capsys.readouterr().err
