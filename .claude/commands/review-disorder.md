---
description: Interactively review and Q&A a disorder YAML file. Present structured review, drill into evidence, request changes, re-validate.
argument-hint: [FILE_PATH or DISORDER_NAME]
---

Review the disorder file specified in $ARGUMENTS.

IMPORTANT: you MUST consult the review-disorder skill for detailed instructions.

If the user provides a disorder name instead of a file path, resolve it to
kb/disorders/<DISORDER_NAME>.yaml (replacing spaces with underscores, removing apostrophes).
