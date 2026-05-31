# History Records

Dismech history records are append-only YAML files for curation, review, and
audit sessions. They replace the old pattern of colocating
`*.history.yaml` files beside KB entries and avoid putting provenance inside the
KB object itself.

Store new history files outside `kb/`:

```text
history/disorders/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/modules/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/comorbidities/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/schema/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

Use UTC timestamps in filenames, for example
`2026-05-31T174412Z-codex-a3f9c2.yaml`. The short suffix prevents same-second
collisions when multiple sessions touch the same target.

Legacy `kb/disorders/*.history.yaml` files were compacted into this layout as
`GENERAL` entry-history summaries. They summarize old `edit_history` activity
by action, date range, model, agent tool, and agent version instead of
preserving every old edit event verbatim.

## Format

Each file records one session for one target. The session may include multiple
events, and `actors` is always a list so human and AI participants can be
recorded together.

```yaml
history_version: 1

target:
  kind: disorder
  slug: Asthma
  path: kb/disorders/Asthma.yaml

session:
  id: 2026-05-31T174412Z-codex-a3f9c2
  timestamp: "2026-05-31T17:44:12Z"
  actors:
    - type: ai_agent
      name: codex
      model: gpt-5
      agent_tool: codex
      agent_version: 1.0
    - type: human
      name: cjm

links:
  issues:
    - https://github.com/monarch-initiative/dismech/issues/2892
  prs:
    - https://github.com/monarch-initiative/dismech/pull/3151
  urls: []

events:
  - type: REVIEW
    outcome: no_change
    sections:
      - phenotypes
      - evidence
    summary: Reviewed evidence quality and found no immediate edits needed.
    details: |
      Rich free-text notes go here.

      This can include reviewer reasoning, caveats, what was checked, why no
      edit was made, future follow-up suggestions, or links in prose.
```

## Event Types

Use the smallest useful vocabulary:

- `GENERAL`: general or legacy curation activity that is not more specifically classified.
- `CREATE`: initial creation of a target.
- `EDIT`: content or metadata edit.
- `REVIEW`: review that may or may not produce edits.
- `AUDIT`: structured inspection, compliance check, or triage.

Use one of these outcomes:

- `changed`
- `no_change`
- `needs_followup`
- `blocked`

Keep `summary` short enough for listings and dashboards. Put curator reasoning,
review notes, caveats, and follow-up detail in the required `details` field.

## Validation

Validate one history record:

```bash
just validate-history history/disorders/Asthma/2026-05-31T174412Z-codex-a3f9c2.yaml
```

Validate all committed history records:

```bash
just validate-history-all
```

The schema lives at `src/dismech/schema/history.yaml`.
