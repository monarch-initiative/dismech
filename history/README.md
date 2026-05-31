# Dismech History Records

This directory stores append-only curation session history outside the KB files.
New files should follow:

```text
history/disorders/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/modules/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/comorbidities/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/schema/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

See `docs/history.md` and `src/dismech/schema/history.yaml` for the record
format. Validate records with `just validate-history-all`.

Legacy `kb/disorders/*.history.yaml` files have been migrated into
`history/disorders/<SLUG>/` as `MIGRATION` records.
