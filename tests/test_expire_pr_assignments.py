"""Assignment ownership must survive activity, retries, and concurrent updates."""

import copy
import importlib.util
import json
import subprocess
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "expire_assignments", ROOT / "scripts/expire_pr_assignments.py"
)
expiry = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = expiry
SPEC.loader.exec_module(expiry)
NOW = datetime(2026, 9, 21, 12, tzinfo=UTC)
OWNER = {"id": 1, "login": "owner", "type": "User"}
AUTHOR = {"id": 2, "login": "author", "type": "User"}
BOT = {"id": 3, "login": expiry.BOT_LOGIN, "type": "Bot"}


def ago(days):
    return (NOW - timedelta(days=days)).isoformat()


def comment(user=OWNER, days=1, **updates):
    return {
        "id": 42,
        "user": user,
        "body": "Still working on this.",
        "created_at": ago(days),
        "updated_at": ago(days),
        **updates,
    }


def snapshot():
    return {
        "pr": {
            "number": 7,
            "state": "open",
            "draft": True,
            "user": AUTHOR,
            "assignees": [OWNER],
            "head": {"sha": "head"},
            "commits": 0,
            "created_at": ago(60),
            "updated_at": ago(30),
        },
        "events": [{"event": "assigned", "assignee": OWNER, "created_at": ago(30)}],
        "comments": [],
        "review_comments": [],
        "reviews": [],
        "commits": [],
    }


def warned(days=14):
    s = snapshot()
    body = expiry.reminder_body(s["pr"], expiry.last_activity(s))
    s["comments"].append(comment(BOT, days, body=body))
    return s


def decision(s=None):
    return expiry.decide(s or snapshot(), NOW)


@pytest.mark.parametrize(
    "days,action", [(6.99, "skip"), (7, "remind"), (100, "remind")]
)
def test_first_reminder_requires_one_week_and_old_prs_get_notice_first(days, action):
    s = snapshot()
    s["events"][0]["created_at"] = ago(days)
    assert decision(s).action == action


@pytest.mark.parametrize(
    "inactive_days,reminder_days,action",
    [
        (7, 0, "skip"),
        (13.99, 6.99, "skip"),
        (14, 7, "unassign"),
        (14, 0, "unassign"),
        (30, 0, "unassign"),
    ],
)
def test_release_is_two_weeks_since_activity_not_since_the_reminder(
    inactive_days, reminder_days, action
):
    s = snapshot()
    s["events"][0]["created_at"] = ago(inactive_days)
    body = expiry.reminder_body(s["pr"], expiry.last_activity(s))
    s["comments"] = [comment(BOT, reminder_days, body=body)]
    assert decision(s).action == action


@pytest.mark.parametrize(
    "kind", ["comments", "review_comments", "reviews", "author", "committer"]
)
def test_every_supported_assignee_response_resets_the_clock(kind):
    s = warned()
    if kind == "reviews":
        s[kind] = [{"user": OWNER, "submitted_at": ago(1)}]
    elif kind in {"author", "committer"}:
        s["commits"] = [
            {
                kind: OWNER,
                "commit": {"author": {"date": ago(2)}, "committer": {"date": ago(1)}},
            }
        ]
    else:
        s[kind] = [*s[kind], comment()]
    assert decision(s).action == "skip"


def test_edited_comment_is_activity_and_later_inactivity_gets_a_new_reminder():
    s = warned()
    s["comments"].append(comment(days=40, updated_at=ago(1)))
    assert decision(s).action == "skip"
    s["comments"][-1]["updated_at"] = ago(8)
    assert decision(s).action == "remind"


@pytest.mark.parametrize(
    "user", [AUTHOR, BOT, {"id": 99, "login": "reviewer", "type": "User"}]
)
def test_other_people_and_automation_do_not_keep_an_assignment_alive(user):
    s = warned()
    s["comments"].append(comment(user))
    assert decision(s).action == "unassign"


def test_reminder_does_not_keep_a_bot_assignee_alive():
    s = snapshot()
    s["pr"]["assignees"] = [BOT]
    s["events"][0]["assignee"] = BOT
    body = expiry.reminder_body(s["pr"], expiry.last_activity(s))
    s["comments"] = [comment(BOT, 14, body=body)]
    assert decision(s).action == "unassign"


def test_a_bot_rebasing_an_owners_old_commit_is_not_owner_activity():
    s = warned()
    s["commits"] = [
        {
            "author": OWNER,
            "committer": BOT,
            "commit": {"author": {"date": ago(40)}, "committer": {"date": ago(1)}},
        }
    ]
    assert decision(s).action == "unassign"


def test_any_current_assignee_keeps_a_joint_assignment_alive():
    s = warned()
    s["pr"]["assignees"].append(AUTHOR)
    s["events"].append({"event": "assigned", "assignee": AUTHOR, "created_at": ago(30)})
    s["comments"].append(comment(AUTHOR))
    assert decision(s).action == "skip"


def test_assignment_change_invalidates_an_old_reminder_even_for_the_same_owner():
    s = warned()
    s["events"] += [
        {"event": "unassigned", "assignee": OWNER, "created_at": ago(3)},
        {"event": "assigned", "assignee": OWNER, "created_at": ago(2)},
    ]
    assert decision(s).action == "skip"
    s["events"][1]["created_at"] = ago(9)
    s["events"][2]["created_at"] = ago(8)
    assert decision(s).action == "remind"


@pytest.mark.parametrize(
    "user", [OWNER, BOT | {"type": "User"}, BOT | {"login": "different[bot]"}]
)
def test_copied_markers_cannot_authorize_unassignment(user):
    s = warned()
    s["comments"][0]["user"] = user
    assert decision(s).action == "remind"


def test_malformed_marker_and_missing_assignment_history_never_release():
    s = warned()
    s["comments"][0]["body"] = f"<!-- {expiry.MARKER} not-json -->"
    assert decision(s).action == "remind"
    s["events"] = []
    with pytest.raises(ValueError, match="assignment start"):
        decision(s)


def test_closed_or_unassigned_prs_need_no_activity_history():
    assert decision({"pr": snapshot()["pr"] | {"state": "closed"}}).action == "skip"
    assert decision({"pr": snapshot()["pr"] | {"assignees": []}}).action == "skip"


def test_reminder_tags_author_and_assignees_and_explains_the_deadline():
    s = snapshot()
    body = expiry.reminder_body(s["pr"], expiry.last_activity(s))
    assert "@author @owner" in body
    assert "14 days since the last assignee activity" in body
    assert "comment on this PR or commit" in body
    s["pr"]["user"] = OWNER
    assert expiry.reminder_body(s["pr"], expiry.last_activity(s)).count("@owner") == 1


def harness(monkeypatch, initial=None, fresh=None):
    s = initial or snapshot()
    reads = iter([copy.deepcopy(s), copy.deepcopy(fresh or s)])
    writes = []
    monkeypatch.setattr(expiry, "pages", lambda path: [copy.deepcopy(s["pr"])])
    monkeypatch.setattr(expiry, "api", lambda path: copy.deepcopy(s["pr"]))
    monkeypatch.setattr(expiry, "read_snapshot", lambda *args: next(reads))
    monkeypatch.setattr(
        expiry, "gh", lambda *args, **kwargs: writes.append((args, kwargs))
    )
    return writes


def test_reminder_and_release_use_only_the_intended_endpoints(monkeypatch):
    writes = harness(monkeypatch)
    lines, errors = expiry.sweep("owner/repo", NOW)
    assert errors == 0 and len(writes) == 1
    assert writes[0][0] == (
        "api",
        "repos/owner/repo/issues/7/comments",
        "--method",
        "POST",
    )
    assert writes[0][1]["write"] is True
    assert "@author @owner" in writes[0][1]["payload"]["body"]
    writes = harness(monkeypatch, warned())
    _, errors = expiry.sweep("owner/repo", NOW)
    assert errors == 0
    assert writes == [
        (
            ("api", "repos/owner/repo/issues/7/assignees", "--method", "DELETE"),
            {"write": True, "payload": {"assignees": ["owner"]}},
        )
    ]


@pytest.mark.parametrize(
    "change", ["comment", "commit", "assignment", "closed", "head"]
)
def test_activity_or_state_changes_before_publication_prevent_writes(
    monkeypatch, change
):
    old = warned()
    fresh = copy.deepcopy(old)
    if change == "comment":
        fresh["comments"].append(comment())
    elif change == "commit":
        fresh["commits"].append(
            {
                "author": OWNER,
                "commit": {"author": {"date": ago(1)}, "committer": {"date": ago(1)}},
            }
        )
    elif change == "assignment":
        fresh["pr"]["assignees"] = []
    elif change == "closed":
        fresh["pr"]["state"] = "closed"
    else:
        fresh["pr"]["head"]["sha"] = "new-head"
    writes = harness(monkeypatch, old, fresh)
    lines, errors = expiry.sweep("owner/repo", NOW)
    assert not writes and errors == 0
    assert any("changed before action" in line for line in lines)


@pytest.mark.parametrize("options", [{"dry_run": True}, {"limit": 0}])
def test_dry_run_and_disabled_job_never_write(monkeypatch, options):
    writes = harness(monkeypatch, warned())
    expiry.sweep("owner/repo", NOW, **options)
    assert not writes


def test_specific_pr_and_action_budget_bound_the_sweep(monkeypatch):
    writes = harness(monkeypatch)
    expiry.sweep("owner/repo", NOW, specific_pr=7)
    assert len(writes) == 1
    writes.clear()
    s = snapshot()
    monkeypatch.setattr(
        expiry, "pages", lambda path: [s["pr"], s["pr"] | {"number": 8}]
    )
    monkeypatch.setattr(expiry, "read_snapshot", lambda *args: copy.deepcopy(s))
    lines, errors = expiry.sweep("owner/repo", NOW, limit=1)
    assert errors == 0 and len(writes) == 1
    assert "Open assigned PRs found: 2." in lines
    assert any("Inspected 1;" in line for line in lines)


def test_failed_activity_lookup_never_releases_an_assignment(monkeypatch):
    writes = harness(monkeypatch, warned())

    def fail(*args):
        raise subprocess.CalledProcessError(1, ["gh", "secret"])

    monkeypatch.setattr(expiry, "read_snapshot", fail)
    lines, errors = expiry.sweep("owner/repo", NOW)
    assert errors == 1 and not writes
    assert "secret" not in "\n".join(lines)


def test_all_pages_are_read_including_a_response_after_the_first_page(monkeypatch):
    paths = []

    def read(path):
        paths.append(path)
        return [comment(AUTHOR)] * 100 if path.endswith("&page=1") else [comment()]

    monkeypatch.setattr(expiry, "api", read)
    s = warned()
    s["comments"] += expiry.pages("repos/o/r/issues/7/comments")
    assert len(paths) == 2 and decision(s).action == "skip"


@pytest.mark.parametrize("count,returned", [(251, 250), (2, 1)])
def test_truncated_commit_history_is_not_treated_as_inactivity(
    monkeypatch, count, returned
):
    p = snapshot()["pr"] | {"commits": count}
    monkeypatch.setattr(expiry, "api", lambda path: p)
    monkeypatch.setattr(
        expiry,
        "pages",
        lambda path: [{}] * returned if path.endswith("/commits") else [],
    )
    with pytest.raises(ValueError, match="250-commit|incomplete"):
        expiry.read_snapshot("owner/repo", 7)


def test_snapshot_rejects_a_pr_that_changes_during_discovery(monkeypatch):
    p = snapshot()["pr"]
    reads = iter([p, p | {"head": {"sha": "changed"}}])
    monkeypatch.setattr(expiry, "api", lambda path: next(reads))
    monkeypatch.setattr(expiry, "pages", lambda path: [])
    with pytest.raises(ValueError, match="changed while reading"):
        expiry.read_snapshot("owner/repo", 7)


def test_writer_token_is_used_only_for_writes_and_payload_is_stdin(monkeypatch):
    calls = []
    monkeypatch.setenv("GH_TOKEN", "reader")
    monkeypatch.setenv("GH_ASSIGNMENT_TOKEN", "writer")

    def run(command, **kwargs):
        calls.append((command, kwargs))
        return subprocess.CompletedProcess(command, 0, stdout="{}")

    monkeypatch.setattr(expiry.subprocess, "run", run)
    expiry.gh("api", "repos/o/r/pulls/7")
    expiry.gh(
        "api",
        "repos/o/r/issues/7/comments",
        write=True,
        payload={"body": "literal `text`\nnext line"},
    )
    assert calls[0][1]["env"]["GH_TOKEN"] == "reader"
    assert calls[1][1]["env"]["GH_TOKEN"] == "writer"
    assert all("GH_ASSIGNMENT_TOKEN" not in kwargs["env"] for _, kwargs in calls)
    assert calls[1][0][-2:] == ["--input", "-"]
    assert json.loads(calls[1][1]["input"])["body"] == "literal `text`\nnext line"
    monkeypatch.delenv("GH_ASSIGNMENT_TOKEN")
    with pytest.raises(ValueError, match="require"):
        expiry.gh("api", "repos/o/r/issues/7/assignees", write=True)


def test_live_mode_requires_a_writer_and_invalid_arguments_fail(monkeypatch):
    monkeypatch.delenv("GH_ASSIGNMENT_TOKEN", raising=False)
    with pytest.raises(SystemExit):
        expiry.main(["--repo", "owner/repo"])
    with pytest.raises(SystemExit):
        expiry.main(["--repo", "invalid", "--dry-run"])
    with pytest.raises(SystemExit):
        expiry.main(["--repo", "owner/repo", "--dry-run", "--max-actions", "-1"])
