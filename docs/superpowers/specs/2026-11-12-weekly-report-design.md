# Weekly activity report: design note

**Date:** 2026-11-12 · **Status:** design approved, not yet implemented

## The ask

A scheduled job that summarises a week of activity in the repository, posted as
a single GitHub issue that replaces the previous week's, and able to file
separate issues for things that need follow-up.

A typical week (30 Oct to 6 Nov 2026) had about 145 new `kb/disorders/` files,
about 250 new issues, and around 30 `evidence-claim-mismatch` issues closed. At
that volume a report that lists everything is unreadable, so the job has to
summarise and rank.

## Decisions

| Question | Decision |
|---|---|
| Who reads it | Two audiences in layers: a short plain-language top for collaborators, collapsible operational detail for maintainers |
| What may open a separate issue | Agent judgement only, no fixed threshold rules. Capped at 3 per week, and only after searching open issues for an existing one |
| How it is built | Agent-first. One agent step gathers and writes everything. Thin deterministic shell steps handle only the previous-report lookup and publishing |
| How it gets more deterministic | Each report logs the commands it ran. After several weeks, commands the agent repeats every week move into a deterministic collector step |

A fully deterministic collector feeding a writing agent was considered and
deferred. Until we know which queries the agent actually needs, writing that
collector would mean guessing.

## Report content

Eight sections, each kept short:

1. **Domain coverage.** New and substantially revised entries grouped by
   therapeutic area or classification, new modules and groupings, and notable
   biology.
2. **Pipeline health.** Evidence-claim-mismatch (opened, closed, closed without
   a content change, median age), jev-recuration, the literature, preprint and
   knowledge-gap scans, and curation-scanner. For each, what it produced this
   week and how much of that was merged versus abandoned.
3. **Schema changes.** Classes, slots and enums added, narrowed or deprecated
   in `src/dismech/schema/`, each with a one-line meaning for curators.
4. **Contentious PRs.** PRs with more than 10 comments, with the agent's
   reading of why: a review loop, a scope dispute, a tooling failure.
5. **Quality ratchets.** Causal-inlink and gene-outlink coverage
   (`just compliance-connectivity`) and the `tests/*_baseline.txt` counts,
   compared with last week.
6. **Automation health.** Scheduled runs that failed or produced nothing,
   merge-queue ejections, ejection-held PRs, review retries.
7. **Queue and claims.** Stub burn-down, new claims, stale claims
   (`just check-claims`), long-open PRs.
8. **Human signal.** Issues opened by people, especially those labelled
   `human-expert-feedback` or `expert_feedback`, so they are not lost among the
   bot-filed issues.

Agent cost from Langfuse and a split of work between humans and agent lanes
were also proposed. Both are deferred.

## Architecture

One workflow, `.github/workflows/weekly-report.yml`, scheduled through
`.github/cron-profiles.yaml` for Monday 14:00 UTC in every enabled profile and
removed in `off`, like the other weekly jobs. It can also be dispatched by hand
with three inputs: `since` (default seven days ago), `dry_run`, and `model`. The
model comes from `.github/agent-config.yaml`, and writes use the ai4c-agent App
token. Setup steps (uv, just, setup-claude-code, Langfuse tracing) copy
`weekly-compliance.yaml`.

Steps:

1. **Previous-report lookup (shell).** Find the open issue labelled
   `weekly-report` and pass its number and body to the agent, so the
   week-over-week figures come from last week's report rather than from a
   committed state file. If there is none, the report says "first report, no
   comparison".
2. **Agent step.** The prompt names the eight sections and suggests starting
   queries for each (`gh pr list --search "merged:>=<since>"`,
   `git log --since=<since> -- src/dismech/schema`, the
   `evidence-claim-mismatch` label, `just compliance-connectivity`,
   `gh run list`, `just check-claims`), and leaves the agent free to go further.
   It writes the issue body to `weekly-report.md` and records any lead issues it
   filed in `filed.json`. It does not create, edit or close the summary issue.
3. **Publish (shell).** Create the new issue, titled
   `Weekly report: <start> to <end>` and labelled `weekly-report`. Then comment
   "Superseded by #N" on the previous one and close it. Pin the new issue.

Keeping step 3 out of the agent's hands makes the guarantee that one report
replaces the last a mechanical one.

## Report layout

Always visible:

- **Highlights.** Three to five plain-language sentences for collaborators.
- **Leads filed this week.** Links to the lead issues, or "none".
- **Needs a human.** A short list of items only a maintainer can act on.

Collapsed, one `<details>` block per section 1–8. Each block has a few figures
with links and one sentence of interpretation. Where last week's report carries
the same figure, the block shows the change. A section the agent could not
collect says `not collected: <reason>` rather than disappearing.

Collapsed at the end: **How this was produced**, the commands run for each
section. This is what tells us, after a few weeks, which queries to make
deterministic. The Langfuse trace for the run is the backup record.

## Lead issues

A lead must be:

- **actionable:** someone could open a PR or make a decision from it;
- **evidenced:** it links at least two concrete instances (PRs, runs, files);
- **new:** a search of open issues finds nothing covering it. If something
  does, the agent comments on that issue instead of filing.

Leads about the content of one disease entry are out of scope, since the
curation scanners already cover that. Lead issues are labelled
`weekly-report-lead`, say they came from the weekly report, and link back to
the summary issue. At most three per run.

## Failure handling

- If the agent step fails, or finishes without writing `weekly-report.md`, the
  publish step does not run. Last week's issue stays open and the run shows as
  failed.
- With `dry_run`, the markdown is uploaded as a workflow artifact and written
  to the job summary, and no issue is created, closed, or commented on. The
  first runs should be dry runs.

## Testing

There is no new Python code, by design, so there is nothing to unit-test yet.
Registering the workflow in `cron-profiles.yaml` and `agent-config.yaml` puts
it under the existing tests that check every managed workflow (profile
completeness, no hardcoded `--model`). The working test is the dry-run output.

## Files

- `.github/workflows/weekly-report.yml` (new)
- `.github/cron-profiles.yaml`: a `weekly-report` entry in every profile
- `.github/agent-config.yaml`: a `weekly-report` model entry
- Labels `weekly-report` and `weekly-report-lead`
- `docs/agent-config.md` and `docs/cron-profiles.md`: list the new workflow
