# Last-pass report: which entries are due for a re-pass

`just last-pass-report` answers a question git cannot: **when was this entry last
given a real curation pass, by whom, and with which model?** It reads `history/`,
excludes bulk sweeps, and prints the result stalest-first so the output is a
worklist rather than a statistic.

```bash
just last-pass-report                       # summary + stalest 25
just last-pass-report --status PASSED       # oldest genuine passes
just last-pass-report --status NO_HISTORY   # entries with no history record at all
just last-pass-report --model sonnet-4      # everything last passed by an old model
just last-pass-report --list-bulk           # audit the sweep classification
just last-pass-report --format tsv --limit 0 > /tmp/passes.tsv
```

## Why not git, and why not `updated_date`

`git log -- kb/disorders/Foo.yaml` reports every touch. A whole-KB slot migration, a
dataset-accession backfill, and somebody sitting down to re-read the pathograph all
look identical in it. That is the objection in
[#5334](https://github.com/monarch-initiative/dismech/issues/5334).

Re-introducing `updated_date` does not fix it. The field was deprecated
([#2892](https://github.com/monarch-initiative/dismech/issues/2892),
[#3151](https://github.com/monarch-initiative/dismech/issues/3151)) because a
mutable line inside every entry conflicts between any two concurrent curation PRs,
and because a bare timestamp carries no actor, model, or scope — so it could not
distinguish a Haiku touch-up from a Fable pass either. Bumping it during a mass
migration is exactly as easy as not bumping it, so it would inherit the same blind
spot on day one.

`history/` already records what is needed — actor, model, agent tool, event type,
outcome, sections, and free-text rationale — and does so **append-only, one file per
session**, which is why it does not reintroduce the conflicts. See
[history.md](history.md).

## The part `history/` does not solve on its own

A bulk sweep writes a history record too. On the corpus at the time of writing, one
identical `Backfill therapeutic_modality` record sits on 700 entries and
`Add public dataset records from GEO` on 320. Reading only the newest record reports
those entries as freshly curated.

So the report separates two things:

| | Meaning |
|---|---|
| **last touch** | the newest history record of any kind |
| **last substantive pass** | the newest record that is not part of a detected bulk sweep and that actually changed the entry (`outcome: changed`) |

A **bulk sweep** is detected structurally rather than from a hand-maintained list: an
event whose summary recurs verbatim across at least `--bulk-threshold` distinct
targets (default 15) was a campaign over many entries, not a pass over this one.

The recurrence gradient is continuous — there is no crisp natural cut between 16
entries and 13 — so the threshold is a dial, and the classification is printed rather
than hidden. Use `--list-bulk` to see exactly what was excluded, and
`--bulk-threshold` to move the line.

One documented exemption: `GENERAL` events whose summary starts with
`Legacy curation summary` are the roll-ups that imported pre-`history/` activity.
Several coincidentally share a summary (same event count, same date range) without
being a campaign, so they are never classified as bulk.

### The known false positive

`Review: 50 least-recently edited Mendelian entries` is classified as a sweep, and it
was not one — it was a real per-entry review campaign, so those 50 entries are
reported staler than they are. (It is also direct evidence that staleness-driven
re-passing is already being done by hand, which is the workflow this report exists to
support.)

A refinement was tried and rejected: *"a sweep touches the same narrow section on
every entry; a real pass varies"*. It inverts on this corpus. The Mendelian review
recorded one identical eight-section list across all 50 records, while the genuinely
mechanical `Reference-title backfill` produced 42 distinct section sets. Section
variance would have promoted the backfill and demoted the review — the opposite of
the intent — so summary recurrence stands as the only signal, with the threshold
exposed as a dial rather than a hidden constant.

## Statuses

| Status | Meaning |
|---|---|
| `PASSED` | a substantive pass is recorded; the row shows its date, event type and model |
| `BULK_ONLY` | history records exist, but all of them are sweeps or `no_change` events |
| `NO_HISTORY` | no history record at all |

`BULK_ONLY` and `NO_HISTORY` entries sort to the top of the worklist, ordered by how
long it has been since anything touched them. A `*` on a `PASSED` row means that
entry's **newest** record is a sweep — i.e. it looks recently updated in git and in
the raw history tree, but has not actually been re-curated since the date shown.

## The limitation to keep in mind

**The report is only as complete as the history ledger.** An entry genuinely
re-curated in a PR that forgot its history record reads as stale here.

`Down_syndrome` is the worked example. Its last recorded substantive pass is
2025-12-15, but PR #5877 (2026-07-09) really did augment it with a tPBM trial and
left no history record, so the report overstates its staleness by seven months. Every
other commit touching that file since December *was* a sweep, which is the finding
the report exists to surface — but the July pass is a false negative.

The fix is ledger discipline, not a different mechanism: CI already posts an advisory
warning when a KB entry changes without a matching history record, and `just
new-history` scaffolds one. Treat a surprising row as a prompt to check
`git log -- <path>` before concluding an entry was neglected.

## Output

`--format summary` (default) prints corpus counts plus the stalest `--limit` rows.
`--format tsv` and `--format json` emit one row per entry with `status`, `last_pass`,
`age_days`, `event_type`, `model`, `agent_tool`, `actor_type`, `last_touch`,
`touch_is_bulk`, `records` and `bulk_events` — enough to drive a scheduled re-pass
campaign or a dashboard.

Ages are measured against now (UTC) unless `--as-of <ISO date>` is given, which makes
output reproducible in tests and reports.

Implementation: `src/dismech/last_pass.py`, tests in `tests/test_last_pass.py`.
