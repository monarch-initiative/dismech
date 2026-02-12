---
description: "[DEPRECATED - use projman skill] Manage projects in projects/ dir"
argument-hint: [PROJECT_NAME]
---

> **Note**: This command is deprecated. Use the `projman` skill instead, which adds GitHub Project sync capability. The skill will be triggered automatically when you work with projects.

You should find either a file or a folder:

./PROJECT_NAME.md
./PROJECT_NAME/
   <multiple materials>

A project doc typically will contain a list of diseases, potentially prioritized. This should be in the form of a checkbox you can check off.

Review the diseases in the priority order.

IMPORTANT: you MUST consult the initiate-new-disorder-creation skill for detailed instructions.

If the project docs specifies a deep research provider(s), make sure to perform deep research using at
least this provider(s), otherwise default to falcon.

You can edit the project doc, but try and make this incremental. After the main description have something like:

---
# STATUS

<checkboxes etc here; keep this up to date>
<get the date from `date`>

# NOTES

## YYYY-MM-DD

<todays notes, add here>

## YYYY-MM-DD

<previous session notes, generally don't edit unless this is a direct continuation>
---
