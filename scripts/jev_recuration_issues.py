"""Feed the existing curation scanner from the latest Jev recuration queue."""

import json
import re
import subprocess
from pathlib import Path
from urllib.parse import quote

import click
import httpx

REPO = "monarch-initiative/dismech"
EVALS = "monarch-initiative/dismech-evals"
LABEL = "jev-recuration"
TITLE_PREFIX = "Jev evidence review: "
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
    pages = gh(
        f"repos/{REPO}/issues?state=all&labels={LABEL}&per_page=100",
        "--paginate",
        "--slurp",
    )
    return [issue for page in pages for issue in page if "pull_request" not in issue]


def marker(file):
    return f"<!-- {LABEL}:{file} -->"


def title(file):
    return TITLE_PREFIX + Path(file).name


def already_queued(file, issues):
    return any(
        issue["title"] == title(file) or marker(file) in (issue.get("body") or "")
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
            "Review the claim–snippet relationships flagged by Jev in "
            f"[{Path(file).name}]({source}). Improve the evidence or assertion where "
            "the finding holds up against the current entry."
        ),
        "",
        (
            f"The available evaluation reports {metrics.get('mismatch_assertions', 0)} "
            "distinct assertions with MISMATCH and "
            f"{metrics.get('partial_assertions', 0)} with PARTIAL. Counts can overlap. "
            "These are model review signals; PARTIAL is not a confirmed error."
        ),
        "",
        (
            f"[Dashboard]({dashboard}) · [Assessment history]({history}) · "
            f"[Latest queue](https://github.com/{EVALS}/blob/main/"
            "reports/latest/recuration/top.jsonl)"
        ),
        "",
        "### Review instructions",
        "",
        (
            "- Check the current disease YAML first. The evaluation may lag behind "
            "recent edits; skip findings that have already been resolved or no longer apply."
        ),
        (
            "- Evaluate whether the selected snippet supports the whole assertion "
            "and the flagged aspects, including disease/subtype context, support/refutation "
            "and directness. Consult the cited reference and other evidence on the assertion."
        ),
        (
            "- Extend or replace snippets, or revise assertions, only where justified. "
            "Do not change correct content merely to agree with Jev. Record a short "
            "explanation when a flagged claim should stay as it is."
        ),
        (
            "- Follow CLAUDE.md, validate changes, and link the resulting PR to this issue. "
            "If no change is needed, explain why and close the issue. This is review of "
            "an existing entry, not a request to create a new disease."
        ),
        "",
        "### Example findings",
        "",
    ]
    # A short handoff; the complete saved judgments remain in dismech-evals.
    for finding in row["findings"][:5]:
        flagged = [
            f"`{path}`: **{answer['label']}**"
            for path, answer in finding.get("answers", {}).items()
            if answer.get("label") in {"MISMATCH", "PARTIAL"}
        ]
        lines += [
            f"- Evidence at `{finding.get('evidence_path')}` "
            f"({finding.get('reference') or 'reference not recorded'}): "
            + "; ".join(flagged[:8]),
        ]
    lines += [
        "",
        (
            "These examples are a subset of the available findings. Follow the "
            "assessment-history link for the saved claims, snippets and remaining aspects."
        ),
        "",
        (
            "Automatically queued by the deterministic Jev recuration intake. "
            "An existing open or closed issue suppresses repeat intake for this disease; "
            "reopen this issue if another review is wanted."
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
                "description": "Review existing disease evidence flagged by Jev",
            },
        )


@click.command()
@click.option("--limit", type=click.IntRange(1, 25), default=5, show_default=True)
@click.option(
    "--apply", is_flag=True, help="Create issues; default is a read-only preview."
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
        if apply and selected:
            ensure_label()
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
