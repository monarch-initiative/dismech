"""The issue queue's selection rules, against a fixture snapshot.

The point of the selector is that the same snapshot and arguments give the
same list, and that every issue left out carries a reason. These tests pin the
rule order, the ranking, and the live-veto order with fake lookups, so none of
them touches GitHub.
"""

from __future__ import annotations

import random

import pytest

from dismech.issue_queue.launch import LANE_HINT, branch_name, build_prompt
from dismech.issue_queue.rules import (
    DISPATCHABLE,
    LANE_ARG,
    TITLE_PREFIXES,
    Options,
    apply_comment_matches,
    apply_live,
    build_rows,
    claim_notes,
    classify,
    cleanup_tag,
    comment_check_candidates,
    effort_of,
    pr_blocks,
    survivors,
    unrouted_labels,
)

ME = "curator"


def issue(number, title, labels=(), author=ME, assignees=(), body=""):
    return {
        "number": number,
        "title": title,
        "labels": [{"name": name} for name in labels],
        "author": {"login": author},
        "assignees": [{"login": login} for login in assignees],
        "body": body,
        "createdAt": "2026-10-01T00:00:00Z",
    }


SNAPSHOT = [
    issue(101, "Curate rickets (MONDO:0005520)", ["claim", "curation", "enhancement"]),
    issue(
        102, "[lit-scan] New papers for Asthma", body="Target: kb/disorders/Asthma.yaml"
    ),
    issue(103, "Proposal: rename the slot", ["enhancement"]),
    issue(104, "Module pages render no evidence", []),
    issue(105, "Pay down the cache layout", ["technical-debt"]),
    issue(106, "Fix the renderer crash", ["bug", "high-priority"]),
    issue(107, "Old duplicate", ["duplicate", "bug"]),
    issue(108, "Someone else's tooling", ["tooling"], assignees=["other"]),
    issue(109, "Docs for stubs", ["documentation", "low_effort", "high_effort"]),
    issue(110, "Docs for claims", ["documentation", "low_effort", "low-priority"]),
    issue(111, "Curate peripartum cardiomyopathy", ["claim"]),
    issue(112, "Curate rickets (MONDO:0005520)", ["claim"], author="other"),
    issue(113, "Curate gout (MONDO:0005393)", ["curation"]),
    issue(114, "Review the Asthma entry", []),
]


def lanes_of(issues):
    return {i["number"]: classify(i) for i in issues}


def test_lane_rules_place_each_kind_of_issue():
    assert lanes_of(SNAPSHOT) == {
        101: "NEW_ENTRY",
        102: "LIT_SCAN",
        103: "DISCUSSION",
        104: "GENERAL",
        105: "TOOLING",
        106: "BUG",
        107: "BUG",
        108: "TOOLING",
        109: "DOCS",
        110: "DOCS",
        111: "NEW_ENTRY",  # claim label without a MONDO title is still a claim
        112: "NEW_ENTRY",
        113: "NEW_ENTRY",  # claim-shaped title without the label
        114: "ENTRY_REVIEW",
    }


def test_title_prefixes_are_read_from_the_table():
    for lane, prefix in TITLE_PREFIXES.items():
        assert classify(issue(1, f"{prefix} something")) == lane


def test_every_dispatchable_lane_has_a_flag_and_a_launch_hint():
    assert set(LANE_ARG.values()) == set(DISPATCHABLE)
    assert set(LANE_HINT) == set(DISPATCHABLE)


def test_effort_tiers():
    assert effort_of(set()) == "unlabelled"
    assert effort_of({"low_effort"}) == "low"
    assert effort_of({"low_effort", "high_effort"}) == "MULTI"


def exclusions(rows):
    return {r["number"]: r["exclude"] for r in rows}


def test_offline_exclusions_apply_in_order_and_record_the_first_hit():
    rows = build_rows(SNAPSHOT, Options(me=ME))
    got = exclusions(rows)
    assert got[107] == "DISPOSITIONED"
    assert got[108] == "ASSIGNED_OTHER"
    assert got[103] == "NON_ACTIONABLE"
    assert got[109] == "MULTI_EFFORT"
    assert got[104] == ""

    # DISPOSITIONED wins over AUTHOR even though both apply.
    rows = build_rows(
        [issue(1, "x", ["wontfix"], author="other")], Options(me=ME, author=ME)
    )
    assert exclusions(rows) == {1: "DISPOSITIONED"}


def test_author_lane_effort_and_range_filters():
    rows = build_rows(
        SNAPSHOT,
        Options(
            me=ME, author=ME, lanes={"DOCS"}, efforts={"low"}, above=100, below=113
        ),
    )
    kept = [r["number"] for r in survivors(rows)]
    assert kept == [110]
    got = exclusions(rows)
    assert got[112] == "AUTHOR"
    assert got[106] == "LANE_EXCLUDED"
    assert got[113] == "NUMBER_RANGE"


def test_ranking_is_priority_then_age_and_ignores_input_order():
    expected = [r["number"] for r in survivors(build_rows(SNAPSHOT, Options(me=ME)))]
    assert expected[0] == 106  # high-priority first
    assert expected[-1] == 110  # low-priority last
    shuffled = SNAPSHOT[:]
    random.Random(7).shuffle(shuffled)
    assert [
        r["number"] for r in survivors(build_rows(shuffled, Options(me=ME)))
    ] == expected


def test_grep_matches_title_then_body_and_records_where():
    rows = build_rows(SNAPSHOT, Options(me=ME, grep="ASTHMA"))
    got = {
        r["number"]: (r["match"], r["exclude"])
        for r in rows
        if r["number"] in (102, 114, 104)
    }
    assert got == {102: ("title", ""), 114: ("title", ""), 104: ("", "TEXT_NO_MATCH")}
    rows = build_rows(SNAPSHOT, Options(me=ME, grep="kb/disorders/asthma"))
    assert {r["number"]: r["match"] for r in rows if r["match"]} == {102: "body"}


def test_comment_matches_restore_only_text_misses():
    rows = build_rows(SNAPSHOT, Options(me=ME, grep="zebrafish", grep_comments=True))
    pending = {r["number"] for r in comment_check_candidates(rows)}
    assert 103 in pending  # discussions are checked for their own listing
    assert 107 not in pending  # excluded for another reason first
    apply_comment_matches(rows, {104: True, 103: True})
    got = {
        r["number"]: (r["match"], r["exclude"])
        for r in rows
        if r["number"] in (103, 104)
    }
    assert got == {103: ("comments", "NON_ACTIONABLE"), 104: ("comments", "")}


def test_claim_notes_agree_with_check_claims():
    notes = claim_notes(SNAPSHOT)
    assert notes[101].startswith("DOUBLE_CLAIM") and "#112" in notes[101]
    assert notes[112].startswith("DOUBLE_CLAIM") and "#101" in notes[112]
    assert notes[111].startswith("UNKEYED_CLAIM")
    assert notes[113].startswith("UNLABELLED_CLAIM")
    assert 104 not in notes


PRS = [
    {"number": 1, "state": "OPEN", "relation": "mentions"},
    {"number": 2, "state": "MERGED", "relation": "closes"},
]


@pytest.mark.parametrize(
    ("prs", "mode", "code"),
    [
        ([], "active", ""),
        ([], "finished", "NO_PR"),
        (PRS[:1], "active", ""),
        (PRS[:1], "any-open", "PR_OPEN"),
        (PRS[:1], "finished", "PR_OPEN"),
        (PRS[1:], "none", "ANY_PR"),
        (PRS[1:], "finished", ""),
        (PRS, "ignore", ""),
        ([{"number": 3, "state": "OPEN", "relation": "linked"}], "active", "PR_ACTIVE"),
    ],
)
def test_pr_modes(prs, mode, code):
    assert pr_blocks(prs, mode) == code


def test_cleanup_tags():
    assert cleanup_tag(PRS[1:]) == "MERGED_CLOSES"
    assert (
        cleanup_tag([{"number": 4, "state": "MERGED", "relation": "mentions"}])
        == "MERGED_MENTIONS"
    )
    assert (
        cleanup_tag([{"number": 5, "state": "CLOSED", "relation": "closes"}])
        == "ABANDONED"
    )


def test_live_vetoes_run_in_rank_order_and_never_pad():
    rows = build_rows(SNAPSHOT, Options(me=ME, lanes={"NEW_ENTRY", "LIT_SCAN", "BUG"}))
    ranked = survivors(rows)
    asked = []

    def kb_covered(mondo, label):
        asked.append(mondo)
        return ["disorders/Rickets.yaml"] if mondo == "MONDO:0005520" else []

    picks = apply_live(
        ranked,
        n=1,
        prs_mode="active",
        links={106: [{"number": 9, "state": "OPEN", "relation": "closes"}]},
        kb_covered=kb_covered,
        open_prs_naming=lambda mondo, label: [],
        on_main=lambda path: False,
    )
    got = exclusions(rows)
    assert got[106] == "PR_ACTIVE"
    assert got[101] == "KB_COVERED"
    assert got[102] == "TARGET_MISSING"
    assert [r["number"] for r in picks] == [
        111
    ]  # no MONDO ID in the title, so no KB check
    assert got[112] == got[113] == "BEYOND_N"
    assert asked == ["MONDO:0005520"]  # nothing is checked once N picks are found


def test_unrouted_labels_lists_only_labels_no_rule_reads():
    assert unrouted_labels(
        ["bug", "enhancement", "high_effort", "codex", "duplicate"]
    ) == ["codex", "enhancement"]


def test_launch_prompt_and_branch():
    branch = branch_name(101, "Curate rickets (MONDO:0005520)")
    assert branch == "issue-101-rickets"
    prompt = build_prompt(
        104,
        "Module pages render no evidence",
        "GENERAL",
        "issue-104-x",
        note="  check the schema ",
    )
    assert "Closes #104" in prompt
    assert prompt.endswith("where they conflict: check the schema")
    assert "precedence" not in build_prompt(104, "t", "GENERAL", "b")


def test_mine_keeps_only_issues_assigned_solely_to_the_current_user():
    issues = [
        issue(1, "Curate a (MONDO:0000001)", ["claim"], assignees=[ME]),
        issue(2, "Curate b (MONDO:0000002)", ["claim"], assignees=[ME, "other"]),
        issue(3, "Curate c (MONDO:0000003)", ["claim"]),
    ]
    rows = build_rows(issues, Options(me=ME, mine=True))
    assert exclusions(rows) == {1: "", 2: "ASSIGNED_OTHER", 3: "NOT_MINE"}
