# DisMech History Records

This directory stores append-only curation session history outside the KB files.
New files should follow:

```text
history/disorders/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/modules/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/comorbidities/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/schema/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

Do not hand-write the filename or session id — scaffold a schema-valid record
with `just new-history` (run `just new-history --help` for options):

```bash
just new-history --kind disorder --slug Asthma --event CREATE --outcome changed \
  --summary "Create: Asthma" --agent-tool claude-code --details "..."
```

See `docs/history.md` and `src/dismech/schema/history.yaml` for the record
format. Validate records with `just validate-history <path>` or
`just validate-history-all`. PRs that change a KB entry should add a matching
record; CI emits an advisory warning when one is missing.

Legacy `kb/disorders/*.history.yaml` files have been compacted into
`history/disorders/<SLUG>/` as `GENERAL` entry-history summaries.
