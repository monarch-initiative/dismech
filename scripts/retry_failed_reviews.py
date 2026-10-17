"""Retry failed review and issue-workflow Actions independently of model and merge eligibility.

Only reruns existing failed jobs; never dispatches a new workflow, edits a PR
or issue, or changes reviews. Uses Actions attempts for persistent backoff.
"""

import argparse
import json
import os
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime, timedelta
from pathlib import Path
from urllib.parse import urlencode

WORKFLOW = "claude-code-review.yml"
RETRYABLE = {"failure", "timed_out"}
REVIEWERS = {"ai4c-reviewer[bot]", "github-actions[bot]"}
RERUN_WINDOW_DAYS = 30
# Issue-opened workflows, keyed to the run-name prefix each one sets. The
# `issues` event cannot fire again for an open issue, so a run that failed
# (typically a shared-account usage limit) is otherwise lost for good (#13150).
ISSUE_WORKFLOWS = {
    "claude-issue-triage.yml": "Triage issue",
    "claude-issue-summarize.yml": "Summarize issue",
    "claude-dedupe-issues.yml": "Dedupe issue",
}


def timestamp(value):
    return datetime.fromisoformat(value)


def gh(*args, write=False):
    env = os.environ.copy()
    writer = env.pop("GH_RETRY_TOKEN", None)
    if write and writer:
        env["GH_TOKEN"] = writer
    result = subprocess.run(
        ["gh", *args],
        env=env,
        text=True,
        capture_output=True,
        check=True,
        timeout=120,
    )
    return result.stdout


def api(path):
    return json.loads(gh("api", path))


def pages(path, key=None):
    result = []
    for page in range(1, 1001):
        data = api(f"{path}{'&' if '?' in path else '?'}per_page=100&page={page}")
        rows = data[key] if key else data
        result.extend(rows)
        if len(rows) < 100:
            return result
    raise RuntimeError("API pagination exceeded 1000 pages")


def workflow_runs(repo, since, until, status=None, event=None):
    """Split search windows to avoid Actions' 1000-result filtered-query cap."""
    if status is None:
        # Avoid thousands of skipped comments and successful PR runs. Success
        # on a PR branch is checked just before retry; manual successes must be
        # indexed here because their Actions branch is main, not the PR branch.
        return [
            run
            for state in (
                "failure",
                "timed_out",
                "queued",
                "in_progress",
                "waiting",
                "pending",
                "requested",
                "cancelled",
                "action_required",
            )
            for run in workflow_runs(repo, since, until, state)
        ] + [
            run
            for trigger in ("workflow_dispatch", "issue_comment")
            for run in workflow_runs(repo, since, until, "success", trigger)
        ]
    return query_runs(repo, WORKFLOW, since, until, status, event)


def query_runs(repo, workflow, since, until, status=None, event=None):
    """One workflow's runs created in a window; no status filter when None."""
    params = {"created": f"{since.isoformat()}..{until.isoformat()}"}
    if status:
        params["status"] = status
    if event:
        params["event"] = event
    query = urlencode(params)
    path = f"repos/{repo}/actions/workflows/{workflow}/runs?{query}"
    first = api(path + "&per_page=100&page=1")
    if first["total_count"] > 1000:
        if (until - since).total_seconds() <= 1:
            raise RuntimeError(f"Too many {workflow} runs in a one-second window")
        middle = since + (until - since) / 2
        return query_runs(repo, workflow, since, middle, status, event) + query_runs(
            repo, workflow, middle, until, status, event
        )
    rows = first["workflow_runs"]
    for page in range(2, (first["total_count"] + 99) // 100 + 1):
        rows.extend(api(path + f"&per_page=100&page={page}")["workflow_runs"])
    return rows


def run_pr(run, repo):
    """Use API association or our run-name; recover legacy dispatches from logs.

    Never match PR titles. Legacy manual runs have no PR association in the
    Actions API, but their trusted guard prints the numeric dispatch input.
    """
    prs = run.get("pull_requests", [])
    if len(prs) == 1:
        return prs[0]["number"]
    match = re.fullmatch(r"Review PR #(\d+)", run.get("display_title") or "")
    if match:
        return int(match[1])
    if run["event"] == "pull_request":
        # Actions can return an empty association even for PR-triggered runs
        # (observed after merges). Resolve by commit/ref, never by title.
        linked = pages(f"repos/{repo}/commits/{run['head_sha']}/pulls")
        numbers = {
            p["number"] for p in linked if p["head"]["ref"] == run["head_branch"]
        }
        return numbers.pop() if len(numbers) == 1 else None
    if run["event"] not in {"workflow_dispatch", "issue_comment"}:
        return None
    jobs = pages(f"repos/{repo}/actions/runs/{run['id']}/jobs", "jobs")
    for job in jobs:
        if job["status"] != "completed":
            continue
        if job["name"] not in {"dispatch-guard", "claude-review"}:
            continue
        log = gh("api", f"repos/{repo}/actions/jobs/{job['id']}/logs")
        # Match the workflow's env/guard output, not arbitrary agent prose.
        found = re.findall(r"(?:Dispatched PR #|\bPR_NUMBER: )([0-9]+)", log)
        numbers = {int(number) for number in found}
        if len(numbers) == 1:
            return numbers.pop()
    return None


def delay_hours(attempt, minimum):
    if minimum == 0:
        return 0
    return max(minimum, (1, 6, 24)[min(max(attempt - 1, 0), 2)])


def resolve_run(run, repo):
    """Bounded, read-only metadata lookup; retain deterministic report order."""
    try:
        return run, run_pr(run, repo), None
    except (subprocess.SubprocessError, ValueError, KeyError, RuntimeError) as exc:
        return run, None, type(exc).__name__


def current_review_runs(repo, specific_pr=None):
    """Cross-check discovery against review checks attached to open PR heads.

    A missing run in the status-filtered Actions census must not make a red
    review check invisible. Resolve its Actions URL back to trusted workflow
    metadata; a check's name alone is not sufficient to authorize a retry.
    """
    pulls = (
        [api(f"repos/{repo}/pulls/{specific_pr}")]
        if specific_pr is not None
        else pages(f"repos/{repo}/pulls?state=open")
    )

    def inspect(pr):
        if pr["state"] != "open":
            return [], None
        try:
            checks = pages(
                f"repos/{repo}/commits/{pr['head']['sha']}/check-runs?filter=latest",
                "check_runs",
            )
            ids = set()
            for check in checks:
                if check["name"] != "claude-review":
                    continue
                match = re.fullmatch(
                    rf"https://github\.com/{re.escape(repo)}/actions/runs/(\d+)(?:/job/\d+)?",
                    check.get("details_url") or "",
                )
                if match:
                    ids.add(int(match[1]))
            runs = []
            for run_id in sorted(ids):
                run = api(f"repos/{repo}/actions/runs/{run_id}")
                if (
                    run.get("path") == f".github/workflows/{WORKFLOW}"
                    and run["event"] == "pull_request"
                    and run["head_sha"] == pr["head"]["sha"]
                    and run_pr(run, repo) == pr["number"]
                ):
                    runs.append(run)
            return runs, None
        except (subprocess.SubprocessError, ValueError, KeyError, RuntimeError) as exc:
            return (
                [],
                f"PR #{pr['number']}: error ({type(exc).__name__}) checking current review checks.",
            )

    runs, errors = [], []
    with ThreadPoolExecutor(max_workers=4) as pool:
        for found, error in pool.map(inspect, pulls):
            runs.extend(found)
            if error:
                errors.append(error)
    return runs, errors


def skip_reason(run, pr, peers, reviews, now, minimum):
    if run["status"] != "completed" or run["conclusion"] not in RETRYABLE:
        return "latest attempt is not a failed or timed-out run"
    if now - timestamp(run["created_at"]) >= timedelta(days=RERUN_WINDOW_DAYS):
        return "outside GitHub's 30-day rerun window"
    if run.get("run_attempt", 1) >= 50:
        return "GitHub's 50-attempt limit reached"
    if pr["state"] != "open":
        return "PR is closed"
    if run["event"] == "pull_request" and run["head_sha"] != pr["head"]["sha"]:
        return "superseded by a new PR commit"
    # A failed pull_request run on the current head is the PR's own
    # `claude-review` check. Manual and comment-triggered reviews run on main,
    # attach no check to the PR head, and so cannot turn that check green; a
    # verdict they post leaves it red too. For such a run, only a newer
    # pull_request run on the same head supersedes it. Without this, the
    # merge controller waits on the red check while this sweep waits on the
    # verdict, and the PR is stuck for good.
    head_check = run["event"] == "pull_request"
    for peer in peers:
        if peer["id"] == run["id"] or peer.get("conclusion") == "skipped":
            continue
        if peer["status"] != "completed":
            return "another review is queued or running"
        if peer["event"] == "pull_request" and peer["head_sha"] != pr["head"]["sha"]:
            continue
        if head_check and peer["event"] != "pull_request":
            continue
        if timestamp(peer["created_at"]) > timestamp(run["created_at"]):
            return "a newer review run exists"
        if peer.get("conclusion") == "success" and timestamp(
            peer["updated_at"]
        ) > timestamp(run["updated_at"]):
            return "another review succeeded after this failure"
    latest = {}
    for review in sorted(reviews, key=lambda row: row["id"]):
        login = (review.get("user") or {}).get("login")
        if login in REVIEWERS and review["state"] != "COMMENTED":
            latest[login] = review
    if not head_check and any(
        r["commit_id"] == pr["head"]["sha"]
        and r["state"] in {"APPROVED", "CHANGES_REQUESTED"}
        for r in latest.values()
    ):
        return "reviewer already submitted a verdict for the current commit"
    wait = delay_hours(run.get("run_attempt", 1), minimum)
    if now - timestamp(run["updated_at"]) < timedelta(hours=wait):
        return f"waiting {wait:g} hours after latest failure"
    return None


def sweep(
    repo,
    now,
    minimum=1,
    limit=5,
    lookback=RERUN_WINDOW_DAYS,
    dry_run=False,
    specific_pr=None,
):
    if limit == 0:
        return ["Review retries disabled (budget 0)."], 0
    runs = {
        r["id"]: r for r in workflow_runs(repo, now - timedelta(days=lookback), now)
    }
    rows = [f"Actions discovery returned {len(runs)} distinct review runs."]
    current, lookup_errors = current_review_runs(repo, specific_pr)
    rows.extend(lookup_errors)
    for run in current:
        if run["id"] not in runs and run.get("conclusion") in RETRYABLE:
            rows.append(
                f"Run {run['id']}: recovered from an open PR's current review check; "
                "missing from Actions discovery."
            )
        runs[run["id"]] = run
    runs = [r for r in runs.values() if r.get("conclusion") != "skipped"]
    errors, indexed, unknown_active = len(lookup_errors), {}, False
    # Historic manual runs require separate jobs/log requests. Bound lookup
    # concurrency so the 30-day census fits the job lifetime. Writes stay serial.
    with ThreadPoolExecutor(max_workers=4) as pool:
        resolved = list(pool.map(lambda run: resolve_run(run, repo), runs))
    for run, number, error in resolved:
        if error:
            rows.append(f"Run {run['id']}: cannot resolve PR ({error}).")
        if number:
            indexed.setdefault(number, []).append(run)
        elif run["status"] != "completed":
            unknown_active = True
        elif run.get("conclusion") in RETRYABLE:
            rows.append(f"Run {run['id']}: deferred; PR association unavailable.")
    if unknown_active:
        return [
            *rows,
            "Retries deferred: an active legacy review cannot yet be associated with a PR.",
        ], errors

    def latest_runs(group):
        # The newest run overall, plus the newest pull_request run: a later
        # manual review that never touches the PR head must not hide a failed
        # head check from the sweep. skip_reason decides between them.
        newest = max(group, key=lambda item: item["created_at"])
        heads = [item for item in group if item["event"] == "pull_request"]
        newest_head = max(heads, key=lambda item: item["created_at"], default=None)
        if newest_head is None or newest_head["id"] == newest["id"]:
            return [newest]
        return [newest, newest_head]

    candidates = sorted(
        [
            (r, n)
            for n, group in indexed.items()
            for r in latest_runs(group)
            if r.get("conclusion") in RETRYABLE
            and timestamp(r["created_at"]) >= now - timedelta(days=lookback)
            and (specific_pr is None or n == specific_pr)
        ],
        key=lambda pair: pair[0]["updated_at"],
    )
    if not candidates:
        rows.append("No failed review runs need recovery.")
    retried = set()
    for run, number in candidates:
        if number in retried:
            continue
        prefix = f"PR #{number}, run {run['id']}"
        try:
            # Refresh the exact attempt and PR before any write. A manual rerun
            # may already have changed this run to queued since discovery.
            current = api(f"repos/{repo}/actions/runs/{run['id']}")
            pr = api(f"repos/{repo}/pulls/{number}")
            reviews = pages(f"repos/{repo}/pulls/{number}/reviews")
            reason = skip_reason(current, pr, indexed[number], reviews, now, minimum)
            if reason:
                rows.append(f"{prefix}: skipped; {reason}.")
                continue
            if len(retried) >= limit:
                rows.append(f"{prefix}: deferred; retry budget reached.")
                continue
            # Recheck branch-triggered runs for pushes/reviews arriving during
            # this sweep, plus manual runs created since discovery began.
            query = urlencode({"branch": pr["head"]["ref"], "per_page": 100})
            fresh = api(f"repos/{repo}/actions/workflows/{WORKFLOW}/runs?{query}")
            recent = workflow_runs(repo, now, datetime.now(UTC))
            # An old manual run can be rerun during discovery without changing
            # created_at. Include active attempts across the full rerun window.
            for state in ("queued", "in_progress", "waiting", "pending", "requested"):
                recent += workflow_runs(
                    repo,
                    now - timedelta(days=RERUN_WINDOW_DAYS),
                    datetime.now(UTC),
                    state,
                )
            peers = list(fresh["workflow_runs"])
            for peer in recent:
                if peer.get("conclusion") == "skipped":
                    continue
                peer_number = run_pr(peer, repo)
                if peer_number == number:
                    peers.append(peer)
                elif peer_number is None and peer["status"] != "completed":
                    raise RuntimeError(
                        "Cannot identify an active review started during discovery"
                    )
            current = api(f"repos/{repo}/actions/runs/{run['id']}")
            pr = api(f"repos/{repo}/pulls/{number}")
            reviews = pages(f"repos/{repo}/pulls/{number}/reviews")
            reason = skip_reason(current, pr, peers, reviews, now, minimum)
            if reason:
                rows.append(f"{prefix}: skipped; {reason}.")
                continue
            if not dry_run:
                gh(
                    "run",
                    "rerun",
                    str(run["id"]),
                    "--failed",
                    "--repo",
                    repo,
                    write=True,
                )
            retried.add(number)
            rows.append(
                f"{prefix}: {'would retry' if dry_run else 'retried'} failed jobs "
                f"(attempt {current.get('run_attempt', 1) + 1})."
            )
        except (subprocess.SubprocessError, ValueError, KeyError, RuntimeError) as exc:
            errors += 1
            rows.append(
                f"{prefix}: error ({type(exc).__name__}); no further action on this PR."
            )
    return rows or ["No failed review runs need recovery."], errors


def run_issue(run, workflow):
    """The issue number from our run-name; never from an issue title.

    Runs from before the run-name was added show the issue title instead and
    stay unresolved. Restricting to the two events the workflows accept keeps
    a title that happens to look like a run-name from keying anything else.
    """
    if run.get("event") not in {"issues", "workflow_dispatch"}:
        return None
    match = re.fullmatch(
        rf"{re.escape(ISSUE_WORKFLOWS[workflow])} #(\d+)",
        run.get("display_title") or "",
    )
    return int(match[1]) if match else None


def issue_skip_reason(run, issue, peers, now, minimum):
    if run["status"] != "completed" or run["conclusion"] not in RETRYABLE:
        return "latest attempt is not a failed or timed-out run"
    if now - timestamp(run["created_at"]) >= timedelta(days=RERUN_WINDOW_DAYS):
        return "outside GitHub's 30-day rerun window"
    if run.get("run_attempt", 1) >= 50:
        return "GitHub's 50-attempt limit reached"
    if "pull_request" in issue:
        return "number belongs to a pull request"
    if issue["state"] != "open":
        return "issue is closed"
    for peer in peers:
        if peer["id"] == run["id"] or peer.get("conclusion") == "skipped":
            continue
        if peer["status"] != "completed":
            return "another run is queued or running"
        if timestamp(peer["created_at"]) > timestamp(run["created_at"]):
            return "a newer run exists"
        if peer.get("conclusion") == "success" and timestamp(
            peer["updated_at"]
        ) > timestamp(run["updated_at"]):
            return "another run succeeded after this failure"
    wait = delay_hours(run.get("run_attempt", 1), minimum)
    if now - timestamp(run["updated_at"]) < timedelta(hours=wait):
        return f"waiting {wait:g} hours after latest failure"
    return None


def sweep_issues(
    repo, now, minimum=1, limit=5, lookback=RERUN_WINDOW_DAYS, dry_run=False
):
    """Rerun the latest failed run of each issue-opened workflow, per issue.

    Same backoff, budget and newer-run guard as the review pass. The budget
    counts runs, not issues: each workflow is its own piece of missing work.
    """
    if limit == 0:
        return ["Issue-workflow retries disabled (budget 0)."], 0
    since = now - timedelta(days=lookback)
    rows, groups, errors = [], {}, 0
    for workflow in ISSUE_WORKFLOWS:
        runs = [
            r
            for r in query_runs(repo, workflow, since, now)
            if r.get("conclusion") != "skipped"
        ]
        rows.append(f"Actions discovery returned {len(runs)} {workflow} runs.")
        legacy = 0
        for run in runs:
            number = run_issue(run, workflow)
            if number:
                groups.setdefault((workflow, number), []).append(run)
            elif run.get("conclusion") in RETRYABLE:
                legacy += 1
        # One line, not one per run: these recur on every sweep until they age
        # out of the rerun window, and none of them can be acted on.
        if legacy:
            rows.append(
                f"{workflow}: {legacy} failed runs predate the issue-number run "
                "name and are not retried."
            )
    candidates = sorted(
        (
            (max(group, key=lambda r: r["created_at"]), key)
            for key, group in groups.items()
        ),
        key=lambda pair: pair[0]["updated_at"],
    )
    candidates = [(r, key) for r, key in candidates if r.get("conclusion") in RETRYABLE]
    if not candidates:
        rows.append("No failed issue-workflow runs need recovery.")
    retried = 0
    for run, (workflow, number) in candidates:
        prefix = f"Issue #{number}, run {run['id']} ({workflow})"
        try:
            current = api(f"repos/{repo}/actions/runs/{run['id']}")
            issue = api(f"repos/{repo}/issues/{number}")
            peers = groups[(workflow, number)]
            reason = issue_skip_reason(current, issue, peers, now, minimum)
            if reason:
                rows.append(f"{prefix}: skipped; {reason}.")
                continue
            if retried >= limit:
                rows.append(f"{prefix}: deferred; retry budget reached.")
                continue
            # A manual dispatch for this issue may have started since discovery.
            for peer in query_runs(repo, workflow, now, datetime.now(UTC)):
                if run_issue(peer, workflow) == number:
                    peers.append(peer)
            current = api(f"repos/{repo}/actions/runs/{run['id']}")
            reason = issue_skip_reason(current, issue, peers, now, minimum)
            if reason:
                rows.append(f"{prefix}: skipped; {reason}.")
                continue
            if not dry_run:
                gh(
                    "run",
                    "rerun",
                    str(run["id"]),
                    "--failed",
                    "--repo",
                    repo,
                    write=True,
                )
            retried += 1
            rows.append(
                f"{prefix}: {'would retry' if dry_run else 'retried'} failed jobs "
                f"(attempt {current.get('run_attempt', 1) + 1})."
            )
        except (subprocess.SubprocessError, ValueError, KeyError, RuntimeError) as exc:
            errors += 1
            rows.append(
                f"{prefix}: error ({type(exc).__name__}); no further action on this run."
            )
    return rows, errors


def nonnegative(value):
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be nonnegative")
    return number


def render_summary(
    repo,
    rows,
    dry_run,
    limit,
    heading="Review retry sweep",
    subject="reviews",
    item="PRs",
    diagnostics="PR lookup diagnostics",
):
    """Make actions prominent without changing sweep decisions."""
    restarted_title = f"Restarted {subject}"
    groups = {
        restarted_title: [],
        "Would restart (dry run)": [],
        "Deferred at retry limit": [],
        "Errors": [],
        "Notices": [],
        "Recovered from PR checks": [],
        "Skipped": [],
        diagnostics: [],
    }
    for row in rows:
        if ": retried failed jobs" in row:
            group = restarted_title
        elif ": would retry failed jobs" in row:
            group = "Would restart (dry run)"
        elif ": deferred; retry budget reached" in row:
            group = "Deferred at retry limit"
        elif ": recovered from an open PR's current review check" in row:
            group = "Recovered from PR checks"
        elif row.startswith("Run "):
            group = diagnostics
        elif ": skipped;" in row:
            group = "Skipped"
        elif ": error (" in row or row.startswith("Discovery failed"):
            group = "Errors"
        else:
            group = "Notices"
        linked = re.sub(
            r"\bPR #(\d+)",
            lambda m: f"[{m[0]}](https://github.com/{repo}/pull/{m[1]})",
            row,
        )
        linked = re.sub(
            r"\bIssue #(\d+)",
            lambda m: f"[{m[0]}](https://github.com/{repo}/issues/{m[1]})",
            linked,
        )
        linked = re.sub(
            r"\b([Rr]un) (\d+)",
            lambda m: f"[{m[0]}](https://github.com/{repo}/actions/runs/{m[2]})",
            linked,
        )
        groups[group].append(linked)
    restarted = len(groups[restarted_title])
    preview = len(groups["Would restart (dry run)"])
    if dry_run:
        lead = f"Dry run: no rerun requests issued; {preview} would restart (limit: {limit})."
    else:
        lead = f"Live run: {restarted} rerun requests accepted (limit: {limit})."
    parts = [
        f"## {heading}",
        lead,
        (
            "Accepted requests restart failed jobs on existing workflow runs; they do not "
            "mean the runs have completed or passed."
        ),
        (
            f"{len(groups['Deferred at retry limit'])} {item} deferred at the retry limit. "
            "They are reconsidered on the next sweep, subject to fresh eligibility checks; "
            "they have not been queued by this sweep."
        ),
    ]
    for title, items in groups.items():
        if not items:
            continue
        listing = "\n".join(f"- {item}" for item in items)
        if title == diagnostics:
            # One unresolved run can produce both an error and a deferral row.
            listing = (
                f"Messages, not unique {item} or runs; no retry issued for these entries.\n\n"
                + listing
            )
        if title in {"Skipped", diagnostics}:
            parts.append(
                f"<details>\n<summary>{title} ({len(items)} messages)</summary>\n\n"
                f"{listing}\n\n</details>"
            )
        else:
            parts.append(f"### {title} ({len(items)})\n\n{listing}")
    return "\n\n".join(parts) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--min-delay-hours", type=nonnegative, default=1)
    parser.add_argument("--max-retries", type=nonnegative, default=5)
    parser.add_argument(
        "--max-issue-retries",
        type=nonnegative,
        help="Budget for failed issue-workflow runs (default: --max-retries)",
    )
    parser.add_argument(
        "--lookback-days",
        type=int,
        choices=range(1, RERUN_WINDOW_DAYS + 1),
        default=RERUN_WINDOW_DAYS,
    )
    parser.add_argument("--specific-pr", type=int)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        rows, errors = sweep(
            args.repo,
            datetime.now(UTC),
            args.min_delay_hours,
            args.max_retries,
            args.lookback_days,
            args.dry_run,
            args.specific_pr,
        )
    except (subprocess.SubprocessError, ValueError, KeyError, RuntimeError) as exc:
        rows, errors = (
            [f"Discovery failed ({type(exc).__name__}); no retries issued."],
            1,
        )
    summary = render_summary(args.repo, rows, args.dry_run, args.max_retries)
    # A specific-PR request is about that PR; leave issue workflows alone.
    if args.specific_pr is None:
        issue_limit = (
            args.max_retries
            if args.max_issue_retries is None
            else args.max_issue_retries
        )
        try:
            issue_rows, issue_errors = sweep_issues(
                args.repo,
                datetime.now(UTC),
                args.min_delay_hours,
                issue_limit,
                args.lookback_days,
                args.dry_run,
            )
        except (subprocess.SubprocessError, ValueError, KeyError, RuntimeError) as exc:
            issue_rows, issue_errors = (
                [f"Discovery failed ({type(exc).__name__}); no retries issued."],
                1,
            )
        errors += issue_errors
        summary += "\n" + render_summary(
            args.repo,
            issue_rows,
            args.dry_run,
            issue_limit,
            heading="Issue-workflow retry sweep",
            subject="issue workflows",
            item="issues",
            diagnostics="Issue lookup diagnostics",
        )
    print(summary)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with Path(os.environ["GITHUB_STEP_SUMMARY"]).open("a") as stream:
            stream.write(summary)
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
