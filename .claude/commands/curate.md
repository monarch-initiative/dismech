---
description: Curate a given disorder, either de-novo, or augment an existing one. A list of deep research providers may be specified.
argument-hint: [DISORDER_NAME] ( using [DEEP_RESEARCH_PROVIDER] )
---

Curate the disorder specified in $ARGUMENTS. 

IMPORTANT: you MUST consult the initiate-new-disorder-creation skill for detailed instructions.

If the user specifies a deep research provider(s), make sure to perform deep research using at
least this provider(s), otherwise default to falcon.

After the KB entry is written and validated, record an append-only history entry
for the session before committing:

```bash
just new-history --kind disorder --slug <DISORDER> \
  --event CREATE --outcome changed \
  --summary "Create: <DISORDER>" \
  --agent-tool claude-code --model <model-id> \
  --details "What was curated, which deep-research provider(s) were used, and how it was validated."
```

Use `--event EDIT` when augmenting an existing entry. Then validate
(`just validate-history <path>`) and `git add history/`. See `docs/history.md`.
