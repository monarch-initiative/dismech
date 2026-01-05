---
description: Manage and drive forward an ongoing project, tracked in projects/ dir
argument-hint: [PROJECT_NAME]
---

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

## Making PRs

ONLY make PRs when asked.

The general procedure is:

1. ensure everything validates `just validate-all`
2. make a branch
3. commit diseases related to project, plus all references
4. `gh pr create`

if the user asks, build the static site and stats (`gen-dashboard`, `just
deploy-browser `). Note it can be hard to disentangle derived
files, but you should be OK if there are no other local updates
besides the one for this project. But in general to be safe, we'll make derived files PR separately.
