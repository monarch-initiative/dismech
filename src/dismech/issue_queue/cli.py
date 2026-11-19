"""Command line for the issue queue.

    just select-issues 3                                  # the next three issues to pick up
    just select-issues --list --author me --lane tooling  # every match, in rank order
    just select-issues --list --grep references_cache --grep-comments
    just select-issues --list --author me --prs finished  # cleanup: every PR merged or closed
    just issue-prs 13150 14506                            # PRs attached to these issues
    just check-issue-lanes                                # labels no lane rule reads

`select` writes one snapshot of the open issues to tmp/issues.json and every
later step reads it; `--from tmp/issues.json` re-sorts the same snapshot. Each
issue goes into one lane by a fixed rule order, exclusions apply in a fixed
order with a reason code, and survivors are ranked by priority label and then
issue number. The same snapshot and arguments give the same list. Read-only:
nothing here assigns, labels or comments. Exit 0; 2 on a usage error.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from dismech.issue_queue import github as gh
from dismech.issue_queue.rules import (
    EFFORT_TIERS,
    LANE_ARG,
    LIVE_VETOES,
    MAX_N,
    PR_MODES,
    REASON_ORDER,
    Options,
    apply_comment_matches,
    apply_live,
    build_rows,
    comment_check_candidates,
    pr_label,
    rank_key,
    survivors,
    unrouted_labels,
)


def _select_parser(p: argparse.ArgumentParser) -> None:
    p.add_argument(
        "n",
        type=int,
        nargs="?",
        help=f"how many issues to pick, 1-{MAX_N} (omit with --list)",
    )
    p.add_argument(
        "--list", action="store_true", help="list every survivor instead of picking N"
    )
    p.add_argument("--above", type=int, help="only issues numbered above this")
    p.add_argument("--below", type=int, help="only issues numbered below this")
    p.add_argument(
        "--author", help="'me' or a GitHub login; only issues opened by them"
    )
    p.add_argument(
        "--mine",
        action="store_true",
        help="only issues assigned to the current user and nobody else (what curate-next works from)",
    )
    p.add_argument(
        "--lane", help="comma list of " + ",".join(LANE_ARG) + " (default: all of them)"
    )
    p.add_argument(
        "--effort", help="comma list of " + ",".join(EFFORT_TIERS) + " (default: all)"
    )
    p.add_argument(
        "--grep",
        help="only issues whose title or body contains this text (case-insensitive, plain substring)",
    )
    p.add_argument(
        "--grep-comments",
        action="store_true",
        help="with --grep, also accept a match in the issue's comments (read live, in batches)",
    )
    p.add_argument(
        "--prs",
        choices=PR_MODES,
        default="active",
        help="active: hide issues an open PR will close or is linked to (default); any-open: hide any "
        "open PR; none: hide any PR at all; ignore: never hide; finished: keep only issues whose "
        "every PR is merged or closed (cleanup)",
    )
    p.add_argument("--no-prs", action="store_true", help="same as --prs none")
    p.add_argument(
        "--from",
        dest="snapshot",
        help="read this snapshot instead of fetching a new one",
    )
    p.add_argument(
        "--no-fetch", action="store_true", help="skip `git fetch origin main`"
    )
    p.add_argument("--json", action="store_true", help="machine-readable output")


def _validate(p: argparse.ArgumentParser, a: argparse.Namespace) -> None:
    if a.list and a.n is not None:
        p.error("give either N or --list, not both")
    if not a.list and (a.n is None or not 1 <= a.n <= MAX_N):
        p.error(f"give N between 1 and {MAX_N}, or --list")
    if a.grep_comments and not a.grep:
        p.error("--grep-comments needs --grep")
    if a.grep is not None and not a.grep.strip():
        p.error("--grep needs non-empty text")
    if a.lane and (bad := [x for x in a.lane.split(",") if x not in LANE_ARG]):
        p.error(f"unknown lane(s) {bad}; choose from {','.join(LANE_ARG)}")
    if a.effort and (bad := [x for x in a.effort.split(",") if x not in EFFORT_TIERS]):
        p.error(f"unknown effort tier(s) {bad}")
    if a.no_prs:
        a.prs = "none"


def _row_line(r: dict) -> str:
    return (
        f"  #{r['number']:<6} {r['lane']:<15} {r['effort']:<10} {r['priority'] or '-':<13} "
        f"{','.join(r['assignees']) or '-':<12} {r['title'][:70]}"
    )


def cmd_select(a: argparse.Namespace) -> None:
    gh.require_gh()
    me = gh.current_user()
    opt = Options(
        me=me,
        author=me if a.author == "me" else a.author,
        mine=a.mine,
        above=a.above,
        below=a.below,
        lanes={LANE_ARG[x] for x in a.lane.split(",")} if a.lane else None,
        efforts=set(a.effort.split(",")) if a.effort else None,
        prs=a.prs,
        grep=a.grep,
        grep_comments=a.grep_comments,
    )
    if not a.no_fetch:
        gh.sh("git", "fetch", "-q", "origin", "main")

    snapshot = Path(a.snapshot) if a.snapshot else gh.SNAPSHOT
    issues = json.loads(snapshot.read_text()) if a.snapshot else gh.fetch_snapshot()
    rows = build_rows(issues, opt)
    if opt.grep and opt.grep_comments:
        # Only issues that passed every other offline filter, so the cost scales
        # with the filtered set rather than with the repository.
        pending = comment_check_candidates(rows)
        apply_comment_matches(
            rows,
            gh.comments_matching([r["number"] for r in pending], opt.grep.casefold()),
        )

    ranked = survivors(rows)
    # Network checks only on survivors, in rank order.
    links = gh.linked_prs([r["number"] for r in ranked])
    picks = apply_live(
        ranked,
        n=None if a.list else a.n,
        prs_mode=opt.prs,
        links=links,
        kb_covered=gh.kb_covered,
        open_prs_naming=gh.open_prs_naming,
        on_main=gh.on_main,
    )

    if a.json:
        print(
            json.dumps(
                {"user": me, "snapshot": str(snapshot), "picks": picks, "all": rows},
                indent=1,
            )
        )
        return

    lanes = opt.lane_set()
    span = (
        f"; numbers {a.above + 1 if a.above is not None else ''}..{a.below - 1 if a.below is not None else ''}"
        if a.above is not None or a.below is not None
        else ""
    )
    text = (
        f"; text {a.grep!r} in title/body{'/comments' if a.grep_comments else ''}"
        if a.grep
        else ""
    )
    print(
        f"user {me}; snapshot {snapshot} ({len(rows)} open issues); lanes {','.join(sorted(lanes))}; "
        f"effort {a.effort or 'any'}; author {opt.author or 'any'}{'; assigned to me only' if a.mine else ''}{span}; prs {opt.prs}{text}"
    )
    if a.snapshot:
        age_h = (time.time() - snapshot.stat().st_mtime) / 3600
        print(
            f"NOTE: re-read snapshot is {age_h:.1f} h old; issues opened, closed or reassigned since are not "
            f"reflected (PRs and comments are read live)."
        )
    lag = gh.checkout_lag() if any(r["lane"] == "NEW_ENTRY" for r in ranked) else 0
    if lag:
        print(
            f"NOTE: this checkout is {lag} commit(s) behind origin/main, and KB_COVERED reads the local kb/; "
            f"`git pull` on main for a current answer."
        )

    if opt.prs == "finished":
        print(
            f"\nCLEANUP CANDIDATES ({len(picks)}, every PR merged or closed; in rank order):"
        )
    elif a.list:
        print(f"\nLAUNCHABLE ({len(picks)}, in rank order):")
    else:
        print(f"\nPICKS ({len(picks)} of {a.n} requested):")
    for r in picks:
        print(_row_line(r))
        where = r["mondo"] or r["target"] or ""
        if r["match"]:
            where = f"{where} [text in {r['match']}]".strip()
        if where or r["detail"]:
            print(f"          {where} {r['detail']}".rstrip())
        if r["claim_note"]:
            print(f"          {r['claim_note']}")
        if r.get("prs"):
            tag = f"[{r['cleanup']}] " if r.get("cleanup") else ""
            print(f"          {tag}PRs: {', '.join(pr_label(p) for p in r['prs'])}")
    if not a.list and len(picks) < a.n:
        print(
            f"  SHORTFALL: {a.n - len(picks)} fewer than requested; nothing was padded."
        )

    counts: dict[str, int] = {}
    for r in rows:
        if r["exclude"]:
            counts[r["exclude"]] = counts.get(r["exclude"], 0) + 1
    print("\nEXCLUDED, by reason code (in application order):")
    for code in REASON_ORDER:
        if counts.get(code):
            print(f"  {code:<16} {counts[code]}")
    vetoed = sorted(
        (r for r in rows if r["exclude"] in LIVE_VETOES and r["exclude"] != "NO_PR"),
        key=rank_key,
    )
    if vetoed:
        print("\nRANKED ABOVE A PICK BUT VETOED BY A LIVE CHECK:")
        for r in vetoed:
            print(
                f"  #{r['number']:<6} {r['exclude']:<15} {r['lane']:<15} {r['title'][:60]}  {r['detail']}".rstrip()
            )
    if (
        a.list and not a.lane
    ):  # discussions belong to no --lane, so a lane filter leaves them out
        parked = [
            r
            for r in rows
            if r["exclude"] == "NON_ACTIONABLE" and (r["match"] or not opt.grep)
        ]
        if parked:
            print(
                f"\nNOT LAUNCHABLE, matched the filters ({len(parked)}; discussions):"
            )
            for r in sorted(parked, key=lambda r: r["number"]):
                hit = f"  [text in {r['match']}]" if r["match"] else ""
                print(
                    f"  #{r['number']:<6} {r['lane']:<15} {r['effort']:<10} {r['title'][:70]}{hit}"
                )
    beyond = [r for r in ranked if r["exclude"] == "BEYOND_N"]
    if beyond:
        print(
            f"\nNEXT IN LINE ({len(beyond)} survivors ranked below the picks; first 15 shown):"
        )
        for r in beyond[:15]:
            print(
                f"  #{r['number']:<6} {r['lane']:<15} {r['effort']:<10} {r['title'][:60]}"
            )
    general = sum(1 for r in rows if r["lane"] == "GENERAL")
    print(
        f"\nGENERAL lane: {general} of {len(rows)} open issues carry no label a lane rule reads "
        f"(`just check-issue-lanes` lists those labels)."
    )


def cmd_prs(a: argparse.Namespace) -> None:
    """PRs attached to each issue, one line each; the check `curate-next` runs before dispatch."""
    gh.require_gh()
    links = gh.linked_prs(a.issues)
    if a.json:
        print(json.dumps({str(n): links.get(n, []) for n in a.issues}, indent=1))
        return
    for n in a.issues:
        prs = links.get(n) or []
        print(f"#{n}: {', '.join(pr_label(p) for p in prs) if prs else 'no PRs'}")


def cmd_lanes(a: argparse.Namespace) -> None:
    gh.require_gh()
    labels = unrouted_labels(gh.repo_labels())
    print("Labels no lane rule reads (an issue carrying only these lands in GENERAL):")
    for name in labels:
        print(f"  {name}")
    print(
        "\nIf one of these should route issues to a lane, add it to LANE_LABELS in "
        "src/dismech/issue_queue/rules.py."
    )


def main(argv: list[str] | None = None) -> None:
    argv = list(sys.argv[1:] if argv is None else argv)
    p = argparse.ArgumentParser(
        prog="dismech-issues",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = p.add_subparsers(dest="command", required=True)
    sel = sub.add_parser("select", help="shortlist open issues")
    _select_parser(sel)
    prs = sub.add_parser("prs", help="PRs attached to issues")
    prs.add_argument("issues", type=int, nargs="+")
    prs.add_argument("--json", action="store_true")
    sub.add_parser("lanes", help="labels no lane rule reads")
    a = p.parse_args(argv)
    if a.command == "select":
        _validate(sel, a)
        cmd_select(a)
    elif a.command == "prs":
        cmd_prs(a)
    else:
        cmd_lanes(a)


if __name__ == "__main__":
    main()
