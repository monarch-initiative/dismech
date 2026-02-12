---
description: Curate a given disorder, either de-novo, or augment an existing one. A list of deep research providers may be specified.
argument-hint: [DISORDER_NAME] ( using [DEEP_RESEARCH_PROVIDER] )
---

Curate the disorder specified in $ARGUMENTS.

IMPORTANT: you MUST consult the curate skill for detailed instructions. The curate skill
orchestrates a multi-phase subagent pipeline for scaffold creation, deep research extraction,
evidence building, term resolution, and validation.

If the user specifies a deep research provider(s), make sure to perform deep research using at
least this provider(s), otherwise default to falcon.
