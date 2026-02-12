---
name: projman
description: >
  Project management skill for markdown-based projects with GitHub Project sync.
  Use when: (1) viewing/managing projects in projects/ folder, (2) syncing project
  checkboxes to GitHub Projects, (3) picking up next work item from a project,
  (4) updating project status after completing work, (5) generating project dashboards.
  Replaces the older /pm command with enhanced GitHub integration.
---

# Project Management (projman)

## Overview

Manage markdown-based project files in `projects/` with optional sync to GitHub Projects.
Markdown files are the source of truth; GitHub Projects provides visibility/collaboration.

## Project File Structure

Projects live in `projects/` as either:
- `PROJECT_NAME.md` - single file project
- `PROJECT_NAME/` - folder with multiple materials

### Standard Sections

```markdown
# Project Title

## Overview
[Project description, goals, selection criteria]

## Items to Process
| Item | Field1 | Field2 | Status |
|------|--------|--------|--------|
| Item A | value | value | [ ] |
| Item B | value | value | [x] |

---
# STATUS
## Tier/Category 1 (N/M) ✓
- [x] Completed item - Date, notes
- [ ] Pending item

## Tier/Category 2 (N/M)
- [ ] Item

# NOTES
## YYYY-MM-DD
[Session notes - add new entries at top]
```

## Core Workflows

### 1. View Project Status

```bash
# List all projects
ls projects/

# Quick status - count checkboxes
grep -c "^\- \[x\]" projects/CANCER.md    # completed
grep -c "^\- \[ \]" projects/CANCER.md    # pending
```

### 2. Pick Up Next Item

Read project file → find first unchecked item in priority order → work on it.

```python
# Parse checkboxes from markdown
import re
with open("projects/CANCER.md") as f:
    content = f.read()
# Find unchecked items: - [ ] Item name
pending = re.findall(r'- \[ \] (.+)', content)
next_item = pending[0] if pending else None
```

### 3. Update Status After Work

After completing an item:
1. Change `- [ ]` to `- [x]`
2. Add date/compliance info: `- [x] Item Name - Created 2026-01-30, 55% compliance`
3. Add session notes under `# NOTES` with today's date

### 4. Add Session Notes

Always add notes incrementally:
```markdown
# NOTES

## 2026-01-30
[Today's work - add at TOP]
- Completed X, Y, Z
- Key findings: ...

## 2026-01-29
[Previous session - don't edit unless continuing]
```

Get today's date: `date +%Y-%m-%d`

## GitHub Project Sync

### Setup (One-Time)

```bash
# Check auth has project scope
gh auth status  # should show 'project' in scopes

# If missing:
gh auth refresh -s project

# Create a new GitHub Project for a markdown project
gh project create --owner @me --title "dismech: CANCER Curation"
# Note the project number returned (e.g., 4)
```

### Sync Checkboxes → GitHub Project Items

Parse markdown checkboxes and create/update GitHub Project items:

```bash
# List existing items in project
gh project item-list PROJECT_NUMBER --owner @me --format json

# Create a draft item (not linked to issue)
gh project item-create PROJECT_NUMBER --owner @me \
  --title "Chronic Myeloid Leukemia" \
  --body "Tier 1: BCR-ABL1 paradigmatic cancer"

# Update item status (need field ID and option ID)
# First, get field info:
gh project field-list PROJECT_NUMBER --owner @me --format json

# Then update:
gh project item-edit --id ITEM_ID \
  --field-id STATUS_FIELD_ID \
  --single-select-option-id DONE_OPTION_ID \
  --project-id PROJECT_ID
```

### Useful gh project commands

```bash
# List your projects
gh project list --owner @me

# View project details
gh project view NUMBER --owner @me

# Get items as JSON for parsing
gh project item-list NUMBER --owner @me --format json | jq '.items[]'

# Get field definitions (needed for updates)
gh project field-list NUMBER --owner @me --format json

# Delete an item
gh project item-delete NUMBER --owner @me --id ITEM_ID

# Archive an item (keeps it but hides from view)
gh project item-archive NUMBER --owner @me --id ITEM_ID
```

### Field IDs Quick Reference

Status field typically has these option IDs (varies per project):
- Todo: find in `gh project field-list` output
- In Progress: find in output
- Done: find in output

Example parsing:
```bash
gh project field-list 4 --owner @me --format json | \
  jq '.fields[] | select(.name=="Status") | .options'
```

## Integration with dismech Workflow

When working on dismech projects:

1. **Pick item from project** → consult `initiate-new-disorder-creation` skill
2. **After creating disorder file** → run `just compliance kb/disorders/NewFile.yaml`
3. **Update project checkbox** → add compliance score
4. **Sync to GitHub Project** → if project has linked GH Project

### Example Session

```
1. Read projects/CANCER.md
2. Find next pending: "- [ ] Chronic Myeloid Leukemia"
3. Use initiate-new-disorder-creation skill
4. Run validation: just qc
5. Update markdown:
   "- [x] Chronic Myeloid Leukemia - Created 2026-01-30, 60% compliance"
6. Add session notes
7. (Optional) Sync to GitHub Project
```

## Deprecation Note

This skill replaces the older `/pm` command. Key differences:
- GitHub Project sync capability (new)
- More structured checkbox parsing (improved)
- Clearer session notes format (improved)

The `/pm` command remains available but should be considered deprecated.
