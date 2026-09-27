"""Remind inactive PR assignees, then release an unanswered assignment.

Runs independently of author allowlists, draft status, reviews, and CI. A
trusted bot comment records each reminder; assignee activity or reassignment
invalidates it. No PR checkout or dependency installation is required.
"""

import argparse
import json
import os
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path

REMINDER_DAYS = 7
RELEASE_DAYS = 14
BOT_LOGIN = "ai4c-agent[bot]"
MARKER = "dismech-assignment-inactivity:v1"


class ActivityUnavailable(ValueError):
    """A known, safe-to-report reason not to infer inactivity."""


def error_detail(exc):
    """Report the failure type and exit code without command arguments or bodies."""
    detail = type(exc).__name__
    if isinstance(exc, subprocess.CalledProcessError):
        detail += f", exit code {exc.returncode}"
    return detail


def timestamp(value):
    result = datetime.fromisoformat(value)
    if result.tzinfo is None:
        raise ValueError("activity timestamp has no timezone")
    return result.astimezone(UTC)


def gh(*args, write=False, payload=None):
    env = os.environ.copy()
    writer = env.pop("GH_ASSIGNMENT_TOKEN", None)
    if write:
        if not writer:
            raise ValueError("assignment writes require GH_ASSIGNMENT_TOKEN")
        env["GH_TOKEN"] = writer
    command = ["gh", *args]
    if payload is not None:
        command += ["--input", "-"]
    return subprocess.run(
        command,
        input=json.dumps(payload) if payload is not None else None,
        env=env,
        text=True,
        capture_output=True,
        check=True,
        timeout=120,
    ).stdout


def api(path):
    return json.loads(gh("api", path))


def pages(path):
    rows = []
    for page in range(1, 1001):
        batch = api(f"{path}{'&' if '?' in path else '?'}per_page=100&page={page}")
        if not isinstance(batch, list):
            raise ValueError("expected a paginated list")
        rows.extend(batch)
        if len(batch) < 100:
            return rows
    raise ActivityUnavailable("activity pagination is incomplete")


def owners(pr):
    return tuple(sorted((int(u["id"]), u["login"]) for u in pr["assignees"]))


def fingerprint(pr):
    return pr["state"], pr["head"]["sha"], owners(pr), pr["updated_at"]


def reminder_data(comment):
    user = comment.get("user") or {}
    if user.get("login", "").casefold() != BOT_LOGIN or user.get("type") != "Bot":
        return None
    match = re.search(
        r"<!-- " + re.escape(MARKER) + r" (.+) -->\s*\Z", comment.get("body") or ""
    )
    if not match:
        return None
    try:
        data = json.loads(match[1])
        return data if isinstance(data, dict) else None
    except ValueError:
        return None


def read_snapshot(repo, number):
    pull_path = f"repos/{repo}/pulls/{number}"
    pr = api(pull_path)
    if pr["state"] != "open" or not pr["assignees"]:
        return {"pr": pr}
    # GitHub's pull/commits endpoint stops at 250 even with pagination. Never
    # infer inactivity from a truncated commit history.
    if pr["commits"] > 250:
        raise ActivityUnavailable("PR exceeds the 250-commit activity lookup limit")
    endpoints = {
        "events": f"repos/{repo}/issues/{number}/events",
        "comments": f"repos/{repo}/issues/{number}/comments",
        "review_comments": f"{pull_path}/comments",
        "reviews": f"{pull_path}/reviews",
        "commits": f"{pull_path}/commits",
    }
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = dict(zip(endpoints, pool.map(pages, endpoints.values()), strict=True))
    if len(rows["commits"]) != pr["commits"]:
        raise ActivityUnavailable("commit activity history is incomplete or changed")
    if fingerprint(api(pull_path)) != fingerprint(pr):
        raise ActivityUnavailable("PR changed while reading activity; retry next sweep")
    return {"pr": pr, **rows}


def last_activity(snapshot):
    pr = snapshot["pr"]
    owner_ids = {uid for uid, _ in owners(pr)}
    assigned = {}
    activity = [timestamp(pr["created_at"])]
    for event in snapshot["events"]:
        if event.get("event") not in {"assigned", "unassigned"}:
            continue
        when = timestamp(event["created_at"])
        # Any assignment change starts a new ownership period, including
        # removing one co-assignee while leaving another assigned.
        activity.append(when)
        uid = (event.get("assignee") or {}).get("id")
        if event["event"] == "assigned":
            assigned[uid] = max(assigned.get(uid, when), when)
    if not owner_ids <= assigned.keys():
        raise ActivityUnavailable("assignment start is missing from the event history")

    for row in snapshot["comments"] + snapshot["review_comments"]:
        if reminder_data(row) is not None:
            continue  # A shepherd reminder must never reset its own timer.
        if (row.get("user") or {}).get("id") in owner_ids:
            activity.append(timestamp(row["created_at"]))
            activity.append(timestamp(row.get("updated_at") or row["created_at"]))
    for row in snapshot["reviews"]:
        if (row.get("user") or {}).get("id") in owner_ids and row.get("submitted_at"):
            activity.append(timestamp(row["submitted_at"]))
    for row in snapshot["commits"]:
        # GitHub-linked identities, not names/emails in user-controlled text.
        # A bot rebasing an old assignee-authored commit must not count the
        # bot's new committer date as fresh activity by the assignee.
        for role in ("author", "committer"):
            if (row.get(role) or {}).get("id") in owner_ids:
                activity.append(timestamp(row["commit"][role]["date"]))
    return max(activity)


def reminder_payload(pr, activity):
    return {
        "assignee_ids": [uid for uid, _ in owners(pr)],
        "activity": activity.isoformat(),
    }


def latest_reminder(snapshot, activity, now):
    expected = reminder_payload(snapshot["pr"], activity)
    candidates = []
    for comment in snapshot["comments"]:
        payload = reminder_data(comment)
        when = timestamp(comment["created_at"])
        if (
            payload == expected
            and activity + timedelta(days=REMINDER_DAYS) <= when <= now
        ):
            candidates.append(comment)
    return max(candidates, key=lambda c: timestamp(c["created_at"]), default=None)


@dataclass(frozen=True)
class Plan:
    action: str
    reason: str
    activity: datetime | None = None
    reminder_id: int | None = None


def decide(snapshot, now):
    pr = snapshot["pr"]
    if pr["state"] != "open" or not pr["assignees"]:
        return Plan("skip", "closed or unassigned")
    activity = last_activity(snapshot)
    if now - activity < timedelta(days=REMINDER_DAYS):
        return Plan("skip", "assignee activity or assignment within the last week")
    reminder = latest_reminder(snapshot, activity, now)
    if reminder is None:
        return Plan(
            "remind", f"no assignee activity since {activity.isoformat()}", activity
        )
    deadline = activity + timedelta(days=RELEASE_DAYS)
    if now < deadline:
        return Plan("skip", f"waiting for a response until {deadline.isoformat()}")
    return Plan(
        "unassign",
        f"no assignee activity for {RELEASE_DAYS} days; reminder #{reminder['id']} "
        f"from {timestamp(reminder['created_at']).isoformat()} unanswered",
        activity,
        reminder["id"],
    )


def reminder_body(pr, activity):
    # Tag the author as requested, and the current assignees who can reset the
    # timer. Deduplicate when the author is also assigned.
    logins = dict.fromkeys([pr["user"]["login"], *(login for _, login in owners(pr))])
    mentions = " ".join(f"@{login}" for login in logins)
    marker = json.dumps(reminder_payload(pr, activity), sort_keys=True)
    return (
        f"{mentions} — this PR has had no comments or commits from its assignees "
        f"since {activity.date().isoformat()}. Is someone still working on it?\n\n"
        "Any current assignee can comment on this PR or commit to its branch to "
        "reset the inactivity clock. "
        f"The shepherd removes inactive assignments after {RELEASE_DAYS} days "
        "since the last assignee activity. If that threshold has already passed, "
        "the next sweep may remove the assignment unless an assignee responds "
        "(currently scheduled hourly).\n\n"
        f"<!-- {MARKER} {marker} -->"
    )


def sweep(repo, now, *, dry_run=False, specific_pr=None, limit=10):
    if limit == 0:
        return ["Assignment inactivity checks disabled (budget 0)."], 0
    prs = (
        [api(f"repos/{repo}/pulls/{specific_pr}")]
        if specific_pr
        else pages(f"repos/{repo}/pulls?state=open&sort=created&direction=asc")
    )
    candidates = [p for p in prs if p["state"] == "open" and p["assignees"]]
    lines = [f"Open assigned PRs found: {len(candidates)}."]
    actions = errors = deferred = inspected = 0
    for pr in candidates:
        if actions >= limit:
            lines.append(
                "Action budget reached; remaining assignments will be checked next sweep."
            )
            break
        number = pr["number"]
        inspected += 1
        try:
            snapshot = read_snapshot(repo, number)
            plan = decide(snapshot, now)
            if plan.action == "skip":
                lines.append(f"PR #{number}: {plan.reason}.")
                continue
            if dry_run:
                lines.append(
                    f"PR #{number}: WOULD {plan.action.upper()} — {plan.reason}."
                )
                actions += 1
                continue
            # Re-read comments, commits, assignment, and open state immediately
            # before either write. A changed head or metadata also defers it.
            fresh = read_snapshot(repo, number)
            if (
                fingerprint(fresh["pr"]) != fingerprint(snapshot["pr"])
                or decide(fresh, now) != plan
            ):
                deferred += 1
                lines.append(
                    f"PR #{number}: changed before action; reconsider next sweep."
                )
                continue
            path = f"repos/{repo}/issues/{number}"
            if plan.action == "remind":
                gh(
                    "api",
                    path + "/comments",
                    "--method",
                    "POST",
                    write=True,
                    payload={"body": reminder_body(fresh["pr"], plan.activity)},
                )
            else:
                gh(
                    "api",
                    path + "/assignees",
                    "--method",
                    "DELETE",
                    write=True,
                    payload={"assignees": [login for _, login in owners(fresh["pr"])]},
                )
            actions += 1
            lines.append(f"PR #{number}: {plan.action.upper()} — {plan.reason}.")
        except ActivityUnavailable as exc:
            deferred += 1
            lines.append(f"PR #{number}: DEFERRED: {exc}; no action confirmed.")
        except (
            subprocess.SubprocessError,
            OSError,
            ValueError,
            KeyError,
            TypeError,
        ) as exc:
            # Never print subprocess arguments/environment or untrusted bodies.
            errors += 1
            lines.append(
                f"PR #{number}: ERROR ({error_detail(exc)}); no action confirmed."
            )
    lines.append(
        f"Inspected {inspected}; {'planned' if dry_run else 'completed'} actions {actions}; "
        f"deferred {deferred}; errors {errors}."
    )
    return lines, errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--specific-pr", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-actions", type=int, default=10)
    args = parser.parse_args(argv)
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repo):
        parser.error("expected owner/repository")
    if args.max_actions < 0 or (args.specific_pr is not None and args.specific_pr < 1):
        parser.error("invalid action limit or PR number")
    if (
        not args.dry_run
        and args.max_actions
        and not os.environ.get("GH_ASSIGNMENT_TOKEN")
    ):
        parser.error("execution requires GH_ASSIGNMENT_TOKEN")
    try:
        lines, errors = sweep(
            args.repo,
            datetime.now(UTC),
            dry_run=args.dry_run,
            specific_pr=args.specific_pr,
            limit=args.max_actions,
        )
    except (
        subprocess.SubprocessError,
        OSError,
        ValueError,
        KeyError,
        TypeError,
    ) as exc:
        lines = [f"ERROR ({error_detail(exc)}); assignment sweep could not finish."]
        errors = 1
    summary = "PR assignment inactivity\n\n" + "\n".join(lines) + "\n"
    print(summary)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with Path(os.environ["GITHUB_STEP_SUMMARY"]).open("a") as handle:
            handle.write(summary)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
