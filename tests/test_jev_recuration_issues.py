"""Issue intake must survive reruns and stale evaluations without duplicate work."""

import json
from copy import deepcopy
from types import SimpleNamespace

import click
import httpx
import pytest
import yaml
from click.testing import CliRunner

from scripts import jev_recuration_issues as intake


def packet(name):
    return {
        "schema_version": 1,
        "task": "review_claim_evidence_match",
        "queue": "overall",
        "file": f"kb/disorders/{name}.yaml",
        "metrics": {"mismatch_assertions": 2, "partial_assertions": 3},
        "findings_total": 12,
        "findings": [
            {
                "evidence_path": "/phenotypes/0/evidence/0",
                "reference": "PMID:123",
                "claim": {
                    "about": {"disease": {"name": name}},
                    "assertion": {
                        "name": "Recurrent fever",
                        "frequency": "FREQUENT",
                    },
                    "selected_evidence": {
                        "snippet": "Fever was reported in one patient.",
                        "supports": "SUPPORT",
                    },
                },
                "answers": {"/about/disease": {"label": "MISMATCH"}},
            }
        ],
        "provenance": {"source_revision": "old", "complete": False},
    }


@pytest.fixture
def service(monkeypatch, tmp_path):
    rows = [packet(name) for name in ("A", "B", "C", "D")]
    issues, calls, labels = [], [], []
    for row in rows:
        path = tmp_path / row["file"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("name: current content differs from evaluated snapshot\n")
    monkeypatch.setattr(intake, "ROOT", tmp_path)

    def get(url, **kwargs):
        assert url == intake.QUEUE_URL and "/main/" in url
        return httpx.Response(
            200,
            request=httpx.Request("GET", url),
            text="\n".join(json.dumps(row) for row in rows),
        )

    def gh(*args, payload=None):
        calls.append((args, payload))
        if "issues?state=all&labels=" in args[0]:
            assert args[1:] == ("--paginate", "--slurp")
            label = args[0].split("labels=")[1].split("&")[0]
            matching = [
                issue
                for issue in issues
                if label
                in {
                    item["name"]
                    for item in issue.get("labels", [{"name": intake.LEGACY_LABEL}])
                }
            ]
            return [deepcopy(matching[:1]), deepcopy(matching[1:])]
        if args[0].endswith("labels?per_page=100"):
            return [deepcopy(labels)]
        if "/issues/" in args[0]:
            number = int(args[0].split("/issues/")[1].split("/")[0])
            issue = next(i for i in issues if i["number"] == number)
            if payload:
                issue["labels"] += [{"name": label} for label in payload["labels"]]
            else:
                assert args[1:] == ("--method", "DELETE")
                issue["labels"] = [
                    label
                    for label in issue["labels"]
                    if label["name"] != intake.LEGACY_LABEL
                ]
            return deepcopy(issue["labels"])
        if args[0].endswith("labels"):
            labels.append(payload)
            return payload
        assert args[0] == f"repos/{intake.REPO}/issues" and payload
        issue = {
            **payload,
            "labels": [{"name": label} for label in payload["labels"]],
            "number": len(issues) + 1,
            "html_url": f"https://example.test/issues/{len(issues) + 1}",
        }
        issues.append(issue)
        return issue

    monkeypatch.setattr(intake.httpx, "get", get)
    monkeypatch.setattr(intake, "gh", gh)
    return SimpleNamespace(
        rows=rows, issues=issues, calls=calls, labels=labels, root=tmp_path
    )


def test_preview_excludes_open_closed_renamed_duplicates_and_missing_entries(service):
    service.issues.extend(
        [
            {
                "number": 1,
                "title": "Jev evidence review: A.yaml",
                "state": "open",
            },
            {
                "number": 2,
                "title": "Retitled after review",
                "state": "closed",
                "body": intake.marker(service.rows[1]["file"]),
                "labels": [{"name": intake.LABEL}],
            },
        ]
    )
    service.rows.insert(0, packet("Deleted"))
    service.rows.append(deepcopy(service.rows[-1]))
    result = CliRunner().invoke(intake.main, ["--limit", "2"])
    assert result.exit_code == 0, result.output
    assert "Would create 2 issue(s)" in result.output
    assert intake.title(packet("C")["file"]) in result.output
    assert intake.title(packet("D")["file"]) in result.output
    assert intake.title(packet("A")["file"]) not in result.output
    assert "Skip missing current entry" in result.output
    assert all(payload is None for _, payload in service.calls)


def test_apply_reuses_issues_after_closure_and_continues_down_queue(service):
    runner = CliRunner()
    result = runner.invoke(intake.main, ["--apply", "--limit", "2"])
    assert result.exit_code == 0, result.output
    assert len(service.issues) == 2 and len(service.labels) == 1
    for issue in service.issues:
        assert [label["name"] for label in issue["labels"]] == [
            "curation",
            "evidence-claim-mismatch",
        ]
        assert "assignees" not in issue
        assert "current entry" in issue["body"]
        assert "not confirmed errors" in issue["body"]
        assert "/about/disease" in issue["body"]
        assert "blob/main/" in issue["body"]
        issue["state"] = "closed"
    result = runner.invoke(intake.main, ["--apply", "--limit", "2"])
    assert result.exit_code == 0, result.output
    assert [issue["title"] for issue in service.issues] == [
        intake.title(packet(name)["file"]) for name in ("A", "B", "C", "D")
    ]
    result = runner.invoke(intake.main, ["--apply"])
    assert result.exit_code == 0 and "Created 0 issue(s)" in result.output
    assert len(service.issues) == 4 and len(service.labels) == 1


def test_dual_label_issue_is_listed_once_and_prs_are_excluded(service):
    service.issues.extend(
        [
            {
                "number": 1,
                "title": "Renamed",
                "body": intake.marker(packet("A")["file"]),
                "labels": [{"name": intake.LABEL}, {"name": intake.LEGACY_LABEL}],
            },
            {"number": 2, "title": "A PR", "pull_request": {}},
        ]
    )
    assert [issue["number"] for issue in intake.existing_issues()] == [1]


def test_apply_migrates_legacy_issue_labels_even_with_no_new_candidates(service):
    row = service.rows[0]
    service.rows[:] = [row]
    issue = {
        "number": 1,
        "title": "Retitled",
        "state": "closed",
        "body": intake.marker(row["file"]),
        "labels": [{"name": intake.LEGACY_LABEL}, {"name": "curation"}],
    }
    service.issues.append(issue)
    result = CliRunner().invoke(intake.main, ["--apply"])
    assert result.exit_code == 0, result.output
    assert "Created 0 issue(s)" in result.output
    assert issue["state"] == "closed" and issue["title"] == "Retitled"
    assert {label["name"] for label in issue["labels"]} == {"curation", intake.LABEL}
    writes = [call for call in service.calls if call[1] or "DELETE" in call[0]]
    result = CliRunner().invoke(intake.main, ["--apply"])
    assert result.exit_code == 0, result.output
    assert [call for call in service.calls if call[1] or "DELETE" in call[0]] == writes


def test_examples_preserve_evaluated_values_not_current_content(service):
    row = service.rows[0]
    row["findings"][0]["answers"]["/assertion/name"] = {"label": "MATCH"}
    original = deepcopy(row)
    body = intake.issue_body(row)
    rendered = yaml.safe_load(body.split("```yaml\n")[1].split("```\n")[0])
    assert rendered["claim"] == row["findings"][0]["claim"]
    assert rendered["reference"] == "PMID:123"
    assert rendered["flagged_aspects"] == {"/about/disease": "MISMATCH"}
    assert "current content differs" not in body
    assert row == original
    assert intake.issue_body(row) == body


def test_markdown_in_snippet_stays_inside_yaml_block():
    finding = packet("A")["findings"][0]
    finding["claim"]["selected_evidence"]["snippet"] = (
        "Literal backticks ``` and [context] ...\nUnicode: α — 'quoted'."
    )
    block = intake.finding_yaml(finding)
    assert block.startswith("````yaml\n") and block.endswith("````\n")
    rendered = yaml.safe_load(block.removeprefix("````yaml\n").removesuffix("````\n"))
    assert rendered["claim"] == finding["claim"]


def test_oversize_examples_are_omitted_whole_and_later_examples_still_render():
    row = packet("A")
    huge = deepcopy(row["findings"][0])
    huge["claim"]["selected_evidence"]["snippet"] = "LONGQUOTATION" * 10000
    row["findings"].insert(0, huge)
    body = intake.issue_body(row)
    assert len(body) < intake.MAX_BODY_LENGTH
    assert "LONGQUOTATION" not in body
    assert "Fever was reported in one patient." in body
    assert "Examples shown: 1." in body


def test_older_queue_without_claim_still_links_to_assessments():
    row = packet("A")
    del row["findings"][0]["claim"]
    body = intake.issue_body(row)
    assert "Not included in this queue" in body
    assert "All saved assessments" in body


def test_uncertain_create_is_not_retried_and_next_run_observes_issue(
    service, monkeypatch
):
    original = intake.gh

    def uncertain(*args, payload=None):
        value = original(*args, payload=payload)
        if payload and args[0].endswith("issues"):
            raise click.ClickException("Response lost after server created issue")
        return value

    monkeypatch.setattr(intake, "gh", uncertain)
    result = CliRunner().invoke(intake.main, ["--apply", "--limit", "2"])
    assert result.exit_code == 1 and len(service.issues) == 1
    monkeypatch.setattr(intake, "gh", original)
    result = CliRunner().invoke(intake.main, ["--apply", "--limit", "1"])
    assert result.exit_code == 0
    assert len(service.issues) == 2
    assert service.issues[1]["title"].endswith("B.yaml")


@pytest.mark.parametrize(
    "file", ["../outside.yaml", "kb/disorders/../outside.yaml", "kb/modules/A.yaml"]
)
def test_invalid_packet_is_rejected_before_any_write(service, file):
    service.rows[-1]["file"] = file
    result = CliRunner().invoke(intake.main, ["--apply"])
    assert result.exit_code == 1
    assert not service.calls


@pytest.mark.parametrize("limit", ["0", "26", "bogus"])
def test_invalid_limit_never_fetches_or_writes(service, limit):
    result = CliRunner().invoke(intake.main, ["--apply", "--limit", limit])
    assert result.exit_code == 2 and not service.calls


def test_unavailable_queue_does_not_create_issues(service, monkeypatch):
    def unavailable(*args, **kwargs):
        raise httpx.ConnectError("offline")

    monkeypatch.setattr(intake.httpx, "get", unavailable)
    result = CliRunner().invoke(intake.main, ["--apply"])
    assert result.exit_code == 1 and not service.calls


def test_github_posts_use_json_stdin_and_do_not_interpret_shell(monkeypatch):
    body = "Literal `text` and $(nothing)\nsecond line"

    def run(args, **kwargs):
        assert args == ["gh", "api", "repos/example/issues", "--input", "-"]
        assert json.loads(kwargs["input"]) == {"body": body}
        assert not kwargs.get("shell")
        return SimpleNamespace(returncode=0, stdout='{"number": 1}', stderr="")

    monkeypatch.setattr(intake.subprocess, "run", run)
    assert intake.gh("repos/example/issues", payload={"body": body}) == {"number": 1}
