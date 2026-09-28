"""Feed the existing curation scanner from the latest Jev recuration queue."""

import json
import re
import subprocess
from pathlib import Path
from urllib.parse import quote

import click
import httpx
import yaml

REPO = "monarch-initiative/dismech"
EVALS = "monarch-initiative/dismech-evals"
LABEL = "evidence-claim-mismatch"
LEGACY_LABEL = "jev-recuration"
TITLE_PREFIX = "Review evidence–claim mismatches: "
LEGACY_TITLE_PREFIX = "Jev evidence review: "
MAX_BODY_LENGTH = 60000
QUEUE_URL = (
    f"https://raw.githubusercontent.com/{EVALS}/main/"
    "reports/latest/recuration/top.jsonl"
)
ROOT = Path(__file__).resolve().parents[1]
FILE_PATTERN = re.compile(r"kb/disorders/[^/\\\n\r]+\.yaml")


def gh(*args, payload=None):
    """Use gh authentication without putting credentials or prose in shell text."""
    result = subprocess.run(
        ["gh", "api", *args, *(["--input", "-"] if payload is not None else [])],
        input=json.dumps(payload) if payload is not None else None,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        raise click.ClickException(result.stderr.strip() or "GitHub API request failed")
    return json.loads(result.stdout)


def existing_issues():
    """List all labelled issues, including closed ones, without search-index lag."""
    issues = {}
    for label in (LABEL, LEGACY_LABEL):
        pages = gh(
            f"repos/{REPO}/issues?state=all&labels={label}&per_page=100",
            "--paginate",
            "--slurp",
        )
        for page in pages:
            for issue in page:
                if "pull_request" not in issue:
                    issues[issue["number"]] = issue
    return list(issues.values())


def marker(file):
    # This hidden identity is permanent; changing the display label must not
    # make a previously reviewed disease eligible for duplicate intake.
    return f"<!-- {LEGACY_LABEL}:{file} -->"


def title(file):
    return TITLE_PREFIX + Path(file).name


def already_queued(file, issues):
    return any(
        issue["title"] in {title(file), LEGACY_TITLE_PREFIX + Path(file).name}
        or marker(file) in (issue.get("body") or "")
        for issue in issues
    )


def read_queue():
    response = httpx.get(QUEUE_URL, timeout=60)
    response.raise_for_status()
    rows = [json.loads(line) for line in response.text.splitlines() if line.strip()]
    # Check the whole packet before creating any issues. An old, valid packet
    # is usable; there is no age cutoff or revision-matching requirement.
    for row in rows:
        if (
            row.get("schema_version") != 1
            or row.get("task") != "review_claim_evidence_match"
            or row.get("queue") != "overall"
            or not FILE_PATTERN.fullmatch(row.get("file", ""))
            or not isinstance(row.get("metrics"), dict)
            or not isinstance(row.get("findings"), list)
        ):
            raise click.ClickException("Unexpected Jev recuration queue record")
    return rows


def finding_yaml(finding):
    """Render the evaluated values, never attach old verdicts to today's YAML."""
    data = {
        "evidence_path": finding.get("evidence_path"),
        "reference": finding.get("reference"),
        "claim": finding.get("claim"),
        "flagged_aspects": {
            path: answer["label"]
            for path, answer in finding.get("answers", {}).items()
            if answer.get("label") in {"MISMATCH", "PARTIAL"}
        },
    }
    if data["claim"] is None:
        data["claim"] = "Not included in this queue; see the saved assessments."
    content = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=88)
    # A snippet can itself contain Markdown. Keep it inside the code block.
    fence = "`" * max(
        3, 1 + max((len(m) for m in re.findall(r"`+", content)), default=0)
    )
    return f"{fence}yaml\n{content}{fence}\n"


def issue_body(row):
    file = row["file"]
    slug = Path(file).stem
    source = f"https://github.com/{REPO}/blob/main/{quote(file, safe='/')}"
    history = (
        f"https://github.com/{EVALS}/blob/main/analysis/classification/jev/"
        f"{quote(slug, safe='')}/evidence_claim_match.yaml"
    )
    dashboard = (
        "https://monarch-initiative.github.io/dismech-evals/entry.html?file="
        + quote(file, safe="")
    )
    metrics = row["metrics"]
    lines = [
        marker(file),
        (
            f"Find and fix evidence–claim mismatches in [{Path(file).name}]({source}). "
            "Expand the literature search to include more papers if necessary."
        ),
        "",
        (
            f"The available evaluation reports {metrics.get('mismatch_assertions', 0)} "
            "distinct assertions with MISMATCH and "
            f"{metrics.get('partial_assertions', 0)} with PARTIAL. Counts can overlap. "
            "These are Jev review signals, not confirmed errors."
        ),
        "",
        (
            f"[Dashboard]({dashboard}) · [All saved assessments]({history}) · "
            f"[Curation skill](https://github.com/{REPO}/blob/main/"
            ".claude/skills/evidence-claim-mismatch/SKILL.md)"
        ),
        "",
        "### Examples to check",
        "",
        (
            "The YAML below contains the evaluated claims and selected snippets. "
            "It is a saved snapshot; check the current entry before editing. "
            "`flagged_aspects` identifies the fields to review, with `/` meaning the whole claim."
        ),
        "",
    ]
    shown = 0
    for finding in row["findings"][:5]:
        block = finding_yaml(finding)
        # Omit whole examples rather than cutting off a claim or quotation.
        # Leave room for the footer under GitHub's issue-body size limit.
        if len("\n".join(lines)) + len(block) > MAX_BODY_LENGTH - 1000:
            continue
        lines += [block]
        shown += 1
    lines += [
        "",
        (
            f"Examples shown: {shown}. The saved assessments contain the full review list. "
            "Generated deterministically from the evaluation queue."
        ),
    ]
    return "\n".join(lines) + "\n"


def ensure_label():
    pages = gh(f"repos/{REPO}/labels?per_page=100", "--paginate", "--slurp")
    if not any(label["name"] == LABEL for page in pages for label in page):
        gh(
            f"repos/{REPO}/labels",
            payload={
                "name": LABEL,
                "color": "1D7666",
                "description": "Find and fix mismatches between disease claims and their evidence",
            },
        )


def migrate_issue_labels(issues):
    """Retire the legacy label once this version of the intake is deployed."""
    for issue in issues:
        labels = {label["name"] for label in issue.get("labels", [])}
        if LEGACY_LABEL not in labels:
            continue
        endpoint = f"repos/{REPO}/issues/{issue['number']}/labels"
        # Separate label operations preserve concurrent assignments of other
        # labels. Add the new identity before dropping the old one.
        if LABEL not in labels:
            gh(endpoint, payload={"labels": [LABEL]})
        gh(f"{endpoint}/{LEGACY_LABEL}", "--method", "DELETE")


@click.command()
@click.option("--limit", type=click.IntRange(1, 25), default=5, show_default=True)
@click.option(
    "--apply",
    is_flag=True,
    help="Create issues and migrate legacy labels; default is a read-only preview.",
)
def main(limit, apply):
    """Queue up to LIMIT previously unqueued diseases from the latest Jev results."""
    try:
        rows = read_queue()
        issues = existing_issues()
        selected = []
        seen = set()
        for row in rows:
            file = row["file"]
            if file in seen or already_queued(file, issues):
                continue
            seen.add(file)
            if not (ROOT / file).is_file():
                click.echo(f"Skip missing current entry: {file}")
                continue
            selected.append((title(file), issue_body(row)))
            if len(selected) == limit:
                break
        if apply and (selected or issues):
            ensure_label()
            migrate_issue_labels(issues)
        for issue_title, body in selected:
            if apply:
                # Do not retry a failed POST: its outcome may be uncertain.
                # The next run lists issues again before doing any writes.
                issue = gh(
                    f"repos/{REPO}/issues",
                    payload={
                        "title": issue_title,
                        "body": body,
                        "labels": ["curation", LABEL],
                    },
                )
                click.echo(f"Created {issue['html_url']}")
            else:
                click.echo(f"\n{issue_title}\n\n{body}")
        click.echo(
            f"{'Created' if apply else 'Would create'} {len(selected)} issue(s)."
        )
    except (httpx.HTTPError, ValueError, KeyError, TypeError) as exc:
        raise click.ClickException(f"Cannot read Jev intake data: {exc}") from exc


if __name__ == "__main__":
    main()
