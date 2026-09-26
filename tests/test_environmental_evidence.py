"""Guard test: no NEW evidence-free `environmental:` exposures in kb/disorders/.

An `Environmental` entry with no `evidence:` block is an uncited causation
claim that every current validator (`just validate`, `validate-terms`,
`count-verified-snippets`) is structurally blind to, since `evidence` is
optional on the class. The backlog is zero, so this is a hard gate: an
exposure that cannot be cited carries a `review_notes` waiver instead.

See scripts/check_environmental_evidence.py and dismech issue #8296.
"""

from pathlib import Path

from dismech.yaml_io import safe_load
from scripts import check_environmental_evidence as cee
from scripts.check_environmental_evidence import (
    MIN_WAIVER_WORDS,
    WAIVER_SENTINEL,
    find_thin_waivers,
    find_violations,
    find_waivers,
    is_waived,
    scan_repo,
    waiver_detail,
)

ROOT = Path(__file__).resolve().parents[1]


def _entry(name: str | None = "Smoking", evidence=None, **extra) -> dict:
    entry = {}
    if name is not None:
        entry["name"] = name
    if evidence is not None:
        entry["evidence"] = evidence
    entry.update({k: v for k, v in extra.items() if v is not None})
    return entry


def test_no_evidence_free_environmental_exposures():
    # Hard gate: the dismech#8296 backlog was worked to zero and the baseline
    # ratchet removed, so any finding here is a new one. An exposure that
    # genuinely cannot be cited is recorded with a `review_notes` waiver
    # instead (see the waiver tests below), which is why this can be absolute.
    found = [
        f"{rel}:{location}: {name!r}" for rel, location, name in scan_repo()
    ]
    assert not found, (
        "Evidence-free `environmental:` exposure(s) detected. Every "
        "environmental entry is an uncited causation claim until it carries "
        "an `evidence:` block. Add a citable PMID/DOI with a verified "
        "snippet, or -- if you searched and found nothing quotable -- record "
        "that in `review_notes:` beginning 'Left deliberately uncited.':\n  "
        + "\n  ".join(found)
    )


def test_flags_an_entry_with_no_evidence_key():
    findings = list(find_violations({"environmental": [_entry("Smoking")]}))
    assert findings == [("environmental[0]", "Smoking")]


def test_flags_an_entry_with_empty_evidence_list():
    findings = list(
        find_violations({"environmental": [_entry("Smoking", evidence=[])]})
    )
    assert findings == [("environmental[0]", "Smoking")]


def test_flags_an_entry_with_null_evidence():
    findings = list(
        find_violations({"environmental": [_entry("Smoking", evidence=None)]})
    )
    assert findings == [("environmental[0]", "Smoking")]


def test_accepts_an_entry_with_evidence():
    entry = _entry(
        "Smoking",
        evidence=[{"reference": "PMID:1", "snippet": "Smoking is a risk factor."}],
    )
    assert not list(find_violations({"environmental": [entry]}))


def test_flags_an_entry_whose_only_evidence_item_has_an_empty_snippet():
    # dismech#8550: `if entry.get("evidence")` only checked block presence, so
    # an evidence item that cites a real PMID but quotes nothing (snippet: '')
    # was silently treated as "cited". A block whose items are all
    # empty-snippet must still count as evidence-free.
    entry = _entry(
        "Smoking",
        evidence=[{"reference": "PMID:1", "supports": "SUPPORT", "snippet": ""}],
    )
    findings = list(find_violations({"environmental": [entry]}))
    assert findings == [("environmental[0]", "Smoking")]


def test_accepts_an_entry_with_one_quoted_item_among_empty_ones():
    entry = _entry(
        "Smoking",
        evidence=[
            {"reference": "PMID:1", "supports": "NO_EVIDENCE", "snippet": ""},
            {"reference": "PMID:2", "supports": "SUPPORT", "snippet": "Real quote."},
        ],
    )
    assert not list(find_violations({"environmental": [entry]}))


# --- review_notes waiver (dismech#8296) ---------------------------------
#
# Some exposures cannot be cited and never will be: a curator searched, found
# no abstract stating the claim, and recorded that. Before the waiver such an
# entry was indistinguishable from one nobody had looked at, so the backlog
# could never reach zero. The sentinel is deliberately narrow -- see the
# negative cases below, which are the whole point of it.

# Long enough to clear MIN_WAIVER_WORDS, because a waiver that records no
# search is no longer a waiver -- see test_a_bare_sentinel_does_not_waive.
WAIVER = (
    "Left deliberately uncited. Targeted PubMed searches for fluid intake and "
    "recurrent attacks, and for hydration status and serum urate, returned no "
    "study whose abstract states this claim directly."
)


def test_waived_entry_is_not_a_violation():
    entry = _entry("Dehydration", review_notes=WAIVER)
    assert not list(find_violations({"environmental": [entry]}))


def test_waived_entry_is_reported_as_a_waiver():
    entry = _entry("Dehydration", review_notes=WAIVER)
    assert list(find_waivers({"environmental": [entry]})) == [
        ("environmental[0]", "Dehydration")
    ]


def test_waiver_matching_is_case_insensitive_and_ignores_leading_space():
    assert is_waived({"review_notes": "  left DELIBERATELY uncited. " + WAIVER_DETAIL})


def test_notes_cannot_waive_only_review_notes_can():
    # `notes` is disease content and is written by anyone; a waiver any prose
    # can trigger is not a waiver. Same sentence, wrong slot -> still a
    # violation.
    entry = _entry("Dehydration", notes=WAIVER)
    assert not is_waived(entry)
    assert list(find_violations({"environmental": [entry]})) == [
        ("environmental[0]", "Dehydration")
    ]


def test_sentinel_must_be_a_prefix_not_a_mention():
    # Prose that merely refers to the convention must not waive.
    entry = _entry(
        "Dehydration",
        review_notes="Considered whether this should be left deliberately uncited.",
    )
    assert not is_waived(entry)
    assert list(find_violations({"environmental": [entry]})) == [
        ("environmental[0]", "Dehydration")
    ]


def test_empty_or_non_string_review_notes_does_not_waive():
    assert not is_waived({"review_notes": ""})
    assert not is_waived({"review_notes": None})
    assert not is_waived({"review_notes": ["Left deliberately uncited."]})
    assert not is_waived({})


def test_a_waived_entry_that_also_has_evidence_is_not_reported_as_a_waiver():
    # Evidence supersedes the waiver: reporting it under --waivers would
    # suggest the claim is still unsourced.
    entry = _entry(
        "Dehydration",
        review_notes=WAIVER,
        evidence=[{"reference": "PMID:1", "snippet": "Real quote."}],
    )
    assert not list(find_violations({"environmental": [entry]}))
    assert not list(find_waivers({"environmental": [entry]}))


def test_waiver_sentinel_constant_is_lowercase_for_prefix_matching():
    # is_waived() lowercases the review_notes before comparing, so a sentinel
    # carrying capitals would never match.
    assert WAIVER_SENTINEL == WAIVER_SENTINEL.lower()
    assert WAIVER.lower().startswith(WAIVER_SENTINEL)


WAIVER_DETAIL = WAIVER[len(WAIVER_SENTINEL) :].strip()


def test_a_bare_sentinel_records_no_search():
    # The sentinel alone is a *claim* that a search happened, with nothing
    # behind it. "" is distinct from None: claimed-and-recorded-nothing needs
    # a different message from did-not-claim.
    assert waiver_detail({"review_notes": "Left deliberately uncited."}) == ""
    assert waiver_detail({"review_notes": "Ordinary note."}) is None


def test_a_bare_sentinel_does_not_waive():
    # The substance floor lives in the script, not only here. The tests are
    # path-filtered and do not run on a kb-only curation PR -- the exact shape
    # of PR that adds a waiver -- so a floor enforced only in pytest would
    # never run on the changes it exists to police.
    entry = _entry("Dehydration", review_notes="Left deliberately uncited.")
    assert not is_waived(entry)
    assert list(find_violations({"environmental": [entry]})) == [
        ("environmental[0]", "Dehydration")
    ]
    assert not list(find_waivers({"environmental": [entry]}))


def test_a_thin_waiver_is_reported_as_thin_not_merely_uncited():
    entry = _entry("Dehydration", review_notes="Left deliberately uncited. Looked.")
    assert list(find_thin_waivers({"environmental": [entry]})) == [
        ("environmental[0]", "Dehydration", 1)
    ]


def test_a_substantive_waiver_is_not_reported_as_thin():
    detail = " ".join(["word"] * MIN_WAIVER_WORDS)
    entry = _entry("Dehydration", review_notes=f"Left deliberately uncited. {detail}")
    assert is_waived(entry)
    assert not list(find_thin_waivers({"environmental": [entry]}))


def test_committed_kb_waivers_say_what_was_searched():
    """Every waiver in kb/ must record the search, not just claim one.

    This is the check that makes the mechanism honest. `is_waived()` only
    asks whether the sentinel is present, so `review_notes: "Left
    deliberately uncited."` with nothing after it would satisfy the checker
    while recording no work at all -- which is precisely the failure mode the
    docstring and CLAUDE.md promise the waiver is not.

    Deliberately reads the YAML rather than using `scan_waivers()`, which
    returns only (path, location, name) and by construction yields entries
    whose review_notes already starts with the sentinel; asserting anything
    about *that* set's paths or prefixes is a tautology.
    """
    thin = []
    for path in sorted((ROOT / "kb").rglob("*.yaml")):
        try:
            with path.open(encoding="utf-8") as handle:
                data = safe_load(handle)
        except Exception:  # malformed YAML is another check's job
            continue
        if not isinstance(data, dict):
            continue
        for idx, entry in enumerate(data.get("environmental") or []):
            if not isinstance(entry, dict) or not is_waived(entry):
                continue
            detail = waiver_detail(entry) or ""
            if len(detail.split()) < MIN_WAIVER_WORDS:
                rel = path.relative_to(ROOT).as_posix()
                thin.append(
                    f"{rel}:environmental[{idx}]: {entry.get('name')!r} "
                    f"({len(detail.split())} words after the sentinel)"
                )
    assert not thin, (
        "A `Left deliberately uncited.` waiver must say which searches were "
        "run and why they failed -- it records a negative result, it is not a "
        "way to skip the search. These carry the sentinel but little or "
        "nothing after it:\n  " + "\n  ".join(thin)
    )


def test_missing_environmental_key_yields_no_findings():
    assert not list(find_violations({}))


def test_unnamed_entry_gets_a_placeholder_name():
    findings = list(find_violations({"environmental": [{"notes": "no name"}]}))
    assert findings == [("environmental[0]", "<unnamed>")]


def test_non_dict_entries_are_skipped():
    # Malformed YAML (not this check's job to gate) should not crash the scan.
    assert not list(find_violations({"environmental": ["not-a-dict"]}))


def test_scan_dir_is_the_kb_root_not_just_disorders():
    # Pins the module-level constant. The behavioural test below passes
    # scan_dir= explicitly, so on its own it would stay green if SCAN_DIR were
    # narrowed back to kb/disorders -- this is the assertion that actually
    # fails in that case.
    assert cee.SCAN_DIR == cee.ROOT / "kb"


def test_scan_covers_kb_beyond_disorders(tmp_path):
    # SCAN_DIR is kb/, not kb/disorders/. kb/modules/ and kb/comorbidities/
    # validate against the same `Disease` class, so an evidence-free
    # `environmental:` entry there is the same uncited causation claim and must
    # be found. This is a no-op on current content (nothing outside
    # kb/disorders/ carries `environmental:` today), so without this test
    # narrowing SCAN_DIR back would leave all other tests green and silently
    # restore the blind spot.
    for sub in ("modules", "comorbidities"):
        target = tmp_path / "kb" / sub
        target.mkdir(parents=True)
        (target / "X.yaml").write_text(
            "environmental:\n- name: Smoking\n  notes: uncited\n", encoding="utf-8"
        )
    findings = scan_repo(scan_dir=tmp_path / "kb", rel_to=tmp_path)
    assert sorted(rel for rel, _, _ in findings) == [
        "kb/comorbidities/X.yaml",
        "kb/modules/X.yaml",
    ]


