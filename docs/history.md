# History Records

DisMech history records are append-only YAML files for curation, review, and
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

## Creating a record

Do not hand-write the path, timestamp, or session id. Scaffold a schema-valid
skeleton with the helper, then edit the emitted `details`:

```bash
just new-history --kind disorder --slug Asthma \
  --event CREATE --outcome changed \
  --summary "Create: Asthma" \
  --agent-tool claude-code --model claude-opus-4-8 \
  --sections phenotypes,pathophysiology,evidence \
  --pr 5123 --issue 2892 \
  --details "One-paragraph summary of what was curated and how it was validated."
```

`--kind` is `disorder`, `module`, `comorbidity`, `schema`, or `other`
(`schema`/`other` require an explicit `--path`). `--event` is one of
`CREATE`/`EDIT`/`REVIEW`/`AUDIT`/`GENERAL`; `--outcome` is
`changed`/`no_change`/`needs_followup`/`blocked`. `--issue`/`--pr`/`--url` accept
bare numbers (expanded to repo URLs) or full URLs and repeat. Run
`just new-history --help` for the full option list. The command prints the path
it created; validate it with `just validate-history <path>` and `git add history/`.

Any PR that creates or edits a KB entry (`kb/disorders/`, `kb/modules/`,
`kb/comorbidities/`) should include a matching record — CI posts an advisory
(non-blocking) warning when one is missing.

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

## Renamed or retargeted targets

History records are **append-only**: once written, a record's `target.slug` and
`target.path` describe the object as it stood during that session and are not
rewritten later. When an entry is renamed, retargeted, or merged — for example a
disorder curated under one name that curation then shows is not an independent
entity — the earlier records keep pointing at the pre-rename path, which no
longer exists on disk.

Record the move with `target.superseded_by` instead of editing the original
fields:

```yaml
target:
  kind: disorder
  slug: Fanconi-Ichthyosis-Dysmorphism_Syndrome
  path: kb/disorders/Fanconi-Ichthyosis-Dysmorphism_Syndrome.yaml
  superseded_by:
    slug: Arthrogryposis-Renal_Dysfunction-Cholestasis_Syndrome
    path: kb/disorders/Arthrogryposis-Renal_Dysfunction-Cholestasis_Syndrome.yaml
    reason: >-
      The 2001 ARC series (PMID:11668108) subsumes FID, so the entry was
      retargeted by the next session in the same PR.
```

`slug`, `path`, and `reason` are all required inside the block — the block turns
a hard layout failure into a pass, so the justification has to be visible in
review. The record files themselves move into the successor's directory
(`history/disorders/<successor-slug>/`) so all sessions for one entry stay
together.

**`superseded_by` may be updated in place; `target.slug`/`target.path` may not.**
The two describe different things, and that is what keeps `superseded_by`
consistent with append-only. `target.slug`/`target.path` record what the session
did and are frozen. `superseded_by` records *where the entry lives now*, so if
the successor is itself renamed later, repoint the existing `superseded_by` at
the new entry (and move the record files again) rather than chaining a second
block.

`tests/test_history_schema.py::test_committed_history_records_follow_layout`
enforces this: a record whose `target.path` is missing passes **only** if
`target.superseded_by.path` resolves to an existing file, so an ordinary bad
slug still fails loudly. `just new-history` also warns at authoring time when
the target path does not exist yet.

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
