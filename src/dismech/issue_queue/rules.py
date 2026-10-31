"""Pure selection rules: classify, exclude, rank, and read PR histories.

Nothing here touches the network or git, so the "same snapshot, same
arguments, same list" claim is checked by `tests/test_issue_queue.py`.

Reason codes, in the order they are applied (first hit is recorded):

  DISPOSITIONED     duplicate / duplicate-pending / closing-soon / wontfix / invalid / policy-reject
  NUMBER_RANGE      issue number not above --above / not below --below
  AUTHOR            --author given and the issue was opened by someone else
  ASSIGNED_OTHER    an assignee who is not the current user (their hold, never ours)
  NOT_MINE          --mine given and the issue is not assigned to the current user
  NON_ACTIONABLE    lane DISCUSSION: a conversation, not a session to launch
  LANE_EXCLUDED     lane not in --lane
  MULTI_EFFORT      more than one effort label (the curation-scanner skips these too)
  EFFORT_EXCLUDED   effort tier not in --effort
  TEXT_NO_MATCH     --grep given and the text is not in the title or body (nor, with
                    --grep-comments, in any comment; settled after the offline pass)

Then, live and only for survivors, in rank order:

  PR_ACTIVE         --prs active (default): an OPEN PR will close it or is linked to it
  PR_OPEN           --prs any-open: any OPEN PR, including one that only mentions it;
                    also --prs finished's code for an issue with an open PR
  ANY_PR            --prs none: any PR in any state or relation
  NO_PR             --prs finished: no PR at all
  KB_COVERED        NEW_ENTRY only: the coverage index `tidy-stubs` uses says a kb/
                    entry already curates the MONDO ID or carries the label
  OPEN_PR           NEW_ENTRY only: an open PR names the MONDO ID or label
  TARGET_MISSING    scan lanes only: the kb/disorders file the body names is not on origin/main
  BEYOND_N          survived everything, ranked below the Nth pick
"""

from __future__ import annotations

import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass

from dismech.stubs.claims import double_claims, parse_claims, unkeyed_claims

REPO = "monarch-initiative/dismech"
MAX_N = 8

DISPOSITIONED = {
    "duplicate",
    "duplicate-pending",
    "closing-soon",
    "wontfix",
    "invalid",
    "policy-reject",
}
EFFORT_LABELS = {
    "low_effort": "low",
    "medium_effort": "medium",
    "high_effort": "high",
    "very-hard": "very-hard",
}
EFFORT_TIERS = ("low", "medium", "high", "very-hard", "unlabelled")
PRIORITY_RANK = {"high-priority": 0, "low-priority": 2}
PR_MODES = ("active", "any-open", "none", "ignore", "finished")

#: The claim title CLAUDE.md prescribes: `Curate <label> (MONDO:NNNNNNN)`.
MONDO_TITLE = re.compile(r"^Curate (?P<label>.+?) \((?P<mondo>MONDO:\d{7})\)\s*$")
KB_FILE = re.compile(r"kb/disorders/[^\s`'\"\\]+\.yaml")

#: Title prefixes the scheduled workflows write. They change when a workflow
#: does, so they live in this one table rather than inside the rules.
TITLE_PREFIXES = {
    "LIT_SCAN": "[lit-scan]",
    "KGAP_SCAN": "[kgap-scan]",
    "PREPRINT_SCAN": "[preprint-scan]",
    "GENETICS_PASS": "Genetics pass",
}

#: Label sets, one per lane. A label that appears in none of these does not
#: place an issue anywhere; `just check-issue-lanes` lists those labels.
LANE_LABELS = {
    "EVIDENCE_REVIEW": {"evidence-claim-mismatch", "jev-recuration"},
    "NEW_ENTRY": {"claim"},
    "GENETICS_PASS": {"genetics-gap"},
    "DISCUSSION": {
        "discussion",
        "question",
        "decision",
        "governance",
        "lump-split decision",
    },
    "CURATION": {"curation", "knowledge_gaps", "evidence", "reference-verification"},
    "SCHEMA": {"schema"},
    "TOOLING": {
        "technical-debt",
        "tooling",
        "infra",
        "infrastructure",
        "test",
        "testing",
        "cache",
        "export",
        "github_actions",
        "dependencies",
    },
    "BUG": {"bug"},
    "DOCS": {"documentation"},
}
DISCUSSION_TITLES = ("Proposal:", "Decide ")


def _prefix(lane: str) -> Callable[[str, set[str]], bool]:
    return lambda t, l: t.startswith(TITLE_PREFIXES[lane])


def _labels(lane: str) -> Callable[[str, set[str]], bool]:
    return lambda t, l: bool(l & LANE_LABELS[lane])


#: First rule that matches wins. A claim (title or label) comes before the
#: scan prefixes; discussions come before curation so a question is never
#: offered as work; GENERAL catches everything else, so an issue labelled only
#: `enhancement`, or nothing, is still offered instead of silently dropped.
LANE_RULES: list[tuple[str, Callable[[str, set[str]], bool]]] = [
    ("EVIDENCE_REVIEW", _labels("EVIDENCE_REVIEW")),
    ("NEW_ENTRY", lambda t, l: bool(MONDO_TITLE.match(t)) or "claim" in l),
    ("LIT_SCAN", _prefix("LIT_SCAN")),
    ("KGAP_SCAN", _prefix("KGAP_SCAN")),
    ("PREPRINT_SCAN", _prefix("PREPRINT_SCAN")),
    (
        "GENETICS_PASS",
        lambda t, l: _labels("GENETICS_PASS")(t, l) or _prefix("GENETICS_PASS")(t, l),
    ),
    (
        "DISCUSSION",
        lambda t, l: _labels("DISCUSSION")(t, l) or t.startswith(DISCUSSION_TITLES),
    ),
    ("ENTRY_REVIEW", lambda t, l: t.startswith("Review ")),
    ("CURATION", _labels("CURATION")),
    ("SCHEMA", _labels("SCHEMA")),
    ("TOOLING", _labels("TOOLING")),
    ("BUG", _labels("BUG")),
    ("DOCS", _labels("DOCS")),
    ("GENERAL", lambda t, l: True),
]
NON_ACTIONABLE = {"DISCUSSION"}
DISPATCHABLE = [name for name, _ in LANE_RULES if name not in NON_ACTIONABLE]
SCAN_LANES = {"LIT_SCAN", "KGAP_SCAN", "PREPRINT_SCAN"}
LANE_ARG = {name.lower().replace("_", "-"): name for name in DISPATCHABLE}
LIVE_VETOES = (
    "PR_ACTIVE",
    "PR_OPEN",
    "ANY_PR",
    "NO_PR",
    "KB_COVERED",
    "OPEN_PR",
    "TARGET_MISSING",
)
REASON_ORDER = (
    "DISPOSITIONED",
    "NUMBER_RANGE",
    "AUTHOR",
    "ASSIGNED_OTHER",
    "NOT_MINE",
    "NON_ACTIONABLE",
    "LANE_EXCLUDED",
    "MULTI_EFFORT",
    "EFFORT_EXCLUDED",
    "TEXT_NO_MATCH",
    *LIVE_VETOES,
    "BEYOND_N",
)


def label_names(issue: dict) -> set[str]:
    return {
        lab["name"] if isinstance(lab, dict) else str(lab)
        for lab in issue.get("labels") or []
    }


def classify(issue: dict) -> str:
    labels = label_names(issue)
    for name, rule in LANE_RULES:
        if rule(issue["title"], labels):
            return name
    raise AssertionError("GENERAL matches everything")


def effort_of(labels: set[str]) -> str:
    tiers = sorted(EFFORT_LABELS[lab] for lab in labels if lab in EFFORT_LABELS)
    if not tiers:
        return "unlabelled"
    return "MULTI" if len(tiers) > 1 else tiers[0]


def unrouted_labels(repo_labels: Iterable[str]) -> list[str]:
    """Repository labels no lane rule reads, so they never place an issue.

    Not a defect list: `enhancement` or `good first issue` say nothing about
    the kind of work. It is how a new workflow label that *should* route an
    issue is noticed before its issues pile up in GENERAL.
    """
    read = set().union(
        *LANE_LABELS.values(), DISPOSITIONED, EFFORT_LABELS, PRIORITY_RANK
    )
    return sorted(set(repo_labels) - read)


def claim_notes(issues: list[dict]) -> dict[int, str]:
    """What `just check-claims` would say about each claim-shaped issue.

    Reported beside the issue, never used to exclude it: a claim problem is for
    the person who filed it to fix, and hiding the issue would hide the
    problem. The claim semantics come from `dismech.stubs.claims`, so the two
    tools cannot disagree about what a claim is.
    """
    labelled = [i for i in issues if "claim" in label_names(i)]
    claims = parse_claims(labelled)
    notes: dict[int, str] = {}
    for claim in unkeyed_claims(claims):
        notes[claim.number] = (
            "UNKEYED_CLAIM: no MONDO ID in the title, so it locks nothing"
        )
    for mondo, dupes in double_claims(claims).items():
        for claim in dupes:
            others = ", ".join(
                f"#{c.number}" for c in dupes if c.number != claim.number
            )
            notes[claim.number] = f"DOUBLE_CLAIM: {mondo} is also claimed by {others}"
    for issue in issues:
        if MONDO_TITLE.match(issue["title"]) and "claim" not in label_names(issue):
            notes.setdefault(
                issue["number"],
                "UNLABELLED_CLAIM: no `claim` label, so it locks nothing",
            )
    return notes


@dataclass
class Options:
    me: str
    author: str | None = None
    mine: bool = False
    above: int | None = None
    below: int | None = None
    lanes: set[str] | None = None
    efforts: set[str] | None = None
    prs: str = "active"
    grep: str | None = None
    grep_comments: bool = False

    def lane_set(self) -> set[str]:
        lanes = set(self.lanes) if self.lanes else set(DISPATCHABLE)
        if self.prs == "finished" and not self.lanes:
            lanes |= NON_ACTIONABLE
        return lanes


def build_rows(issues: list[dict], opt: Options) -> list[dict]:
    """One row per issue, with the first offline exclusion that applies."""
    needle = opt.grep.casefold() if opt.grep else None
    lanes = opt.lane_set()
    notes = claim_notes(issues)
    rows = []
    for issue in issues:
        labels = label_names(issue)
        assignees = [
            u["login"] if isinstance(u, dict) else str(u)
            for u in issue.get("assignees") or []
        ]
        m = MONDO_TITLE.match(issue["title"])
        lane = classify(issue)
        body = issue.get("body") or ""
        # The scan lanes name the entry they augment in the body; elsewhere a
        # kb/ path in the body is incidental and is not a target.
        target = KB_FILE.search(body) if lane in SCAN_LANES else None
        author = issue.get("author") or {}
        row = {
            "number": issue["number"],
            "title": issue["title"],
            "author": author.get("login", "")
            if isinstance(author, dict)
            else str(author),
            "assignees": assignees,
            "lane": lane,
            "effort": effort_of(labels),
            "priority": next((lab for lab in PRIORITY_RANK if lab in labels), ""),
            "mondo": m.group("mondo") if m else "",
            "label": m.group("label") if m else "",
            "target": target.group(0) if target else "",
            "claim_note": notes.get(issue["number"], ""),
            "match": "",
            "exclude": "",
            "detail": "",
        }
        if needle:
            if needle in issue["title"].casefold():
                row["match"] = "title"
            elif needle in body.casefold():
                row["match"] = "body"
        others = [u for u in assignees if u != opt.me]
        if labels & DISPOSITIONED:
            row["exclude"], row["detail"] = (
                "DISPOSITIONED",
                ",".join(sorted(labels & DISPOSITIONED)),
            )
        elif (opt.above is not None and row["number"] <= opt.above) or (
            opt.below is not None and row["number"] >= opt.below
        ):
            row["exclude"] = "NUMBER_RANGE"
        elif opt.author and row["author"] != opt.author:
            row["exclude"], row["detail"] = "AUTHOR", row["author"]
        elif others:
            row["exclude"], row["detail"] = "ASSIGNED_OTHER", ",".join(others)
        elif opt.mine and opt.me not in assignees:
            row["exclude"] = "NOT_MINE"
        elif lane in NON_ACTIONABLE and opt.prs != "finished":
            row["exclude"] = "NON_ACTIONABLE"
        elif lane not in lanes:
            row["exclude"] = "LANE_EXCLUDED"
        elif row["effort"] == "MULTI":
            row["exclude"] = "MULTI_EFFORT"
        elif opt.efforts is not None and row["effort"] not in opt.efforts:
            row["exclude"] = "EFFORT_EXCLUDED"
        elif needle and not row["match"]:
            row["exclude"] = "TEXT_NO_MATCH"
        rows.append(row)
    return rows


def comment_check_candidates(rows: list[dict]) -> list[dict]:
    """Rows whose only miss is the text, plus discussions for their own listing."""
    return [
        r
        for r in rows
        if not r["match"] and r["exclude"] in {"TEXT_NO_MATCH", "NON_ACTIONABLE"}
    ]


def apply_comment_matches(rows: list[dict], hits: dict[int, bool]) -> None:
    for r in comment_check_candidates(rows):
        if hits.get(r["number"]):
            r["match"] = "comments"
            if r["exclude"] == "TEXT_NO_MATCH":
                r["exclude"] = ""


def rank_key(row: dict) -> tuple[int, int]:
    """Total order: high-priority first, low-priority last, then oldest issue first."""
    return (PRIORITY_RANK.get(row["priority"], 1), row["number"])


def survivors(rows: list[dict]) -> list[dict]:
    return sorted((r for r in rows if not r["exclude"]), key=rank_key)


def pr_blocks(prs: list[dict], mode: str) -> str:
    """The reason code that hides this issue under --prs <mode>, or ''."""
    if mode == "finished" and not prs:
        return "NO_PR"
    if mode == "ignore" or not prs:
        return ""
    if mode == "none":
        return "ANY_PR"
    if mode in ("any-open", "finished"):
        return "PR_OPEN" if any(pr["state"] == "OPEN" for pr in prs) else ""
    return (
        "PR_ACTIVE"
        if any(pr["state"] == "OPEN" and pr["relation"] != "mentions" for pr in prs)
        else ""
    )


def cleanup_tag(prs: list[dict]) -> str:
    """For --prs finished, strongest signal first."""
    if any(pr["state"] == "MERGED" and pr["relation"] != "mentions" for pr in prs):
        return "MERGED_CLOSES"
    if any(pr["state"] == "MERGED" for pr in prs):
        return "MERGED_MENTIONS"
    return "ABANDONED"


def pr_label(pr: dict) -> str:
    prefix = "" if pr.get("repo", REPO) == REPO else pr["repo"]
    return f"{prefix}#{pr['number']} {pr['state'].lower()}/{pr['relation']}"


def apply_live(
    ranked: list[dict],
    *,
    n: int | None,
    prs_mode: str,
    links: dict[int, list[dict]],
    kb_covered: Callable[[str, str], list[str]],
    open_prs_naming: Callable[[str, str], list[str]],
    on_main: Callable[[str], bool],
) -> list[dict]:
    """The live vetoes, in rank order; returns the picks (all of them when n is None).

    The lookups are passed in so the order of checks is testable without GitHub.
    """
    picks = []
    for r in ranked:
        if n is not None and len(picks) == n:
            r["exclude"] = "BEYOND_N"
            continue
        prs = links.get(r["number"]) or []
        r["prs"] = prs
        code = pr_blocks(prs, prs_mode)
        if code:
            r["exclude"], r["detail"] = code, ", ".join(pr_label(p) for p in prs)
            continue
        if prs_mode == "finished":
            r["cleanup"] = cleanup_tag(prs)
        if r["lane"] == "NEW_ENTRY" and r["mondo"]:
            hits = kb_covered(r["mondo"], r["label"])
            if hits:
                r["exclude"], r["detail"] = "KB_COVERED", ",".join(hits)
                continue
            named = open_prs_naming(r["mondo"], r["label"])
            if named:
                r["exclude"], r["detail"] = "OPEN_PR", "; ".join(named)
                continue
        if r["lane"] in SCAN_LANES and r["target"] and not on_main(r["target"]):
            r["exclude"], r["detail"] = "TARGET_MISSING", r["target"]
            continue
        picks.append(r)
    return picks
