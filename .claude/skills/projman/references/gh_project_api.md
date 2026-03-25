# GitHub Projects CLI Reference

Quick reference for `gh project` commands. Load this when doing project sync operations.

## Authentication

```bash
# Check current scopes
gh auth status

# Add project scope if missing
gh auth refresh -s project
```

## Project Operations

```bash
# List projects
gh project list --owner @me
gh project list --owner monarch-initiative

# View project
gh project view NUMBER --owner OWNER

# Create project
gh project create --owner @me --title "Project Name"

# Close/reopen
gh project close NUMBER --owner OWNER
gh project edit NUMBER --owner OWNER --visibility public
```

## Item Operations

```bash
# List items (JSON for parsing)
gh project item-list NUMBER --owner OWNER --format json --limit 500

# Create draft item
gh project item-create NUMBER --owner OWNER \
  --title "Item Title" \
  --body "Description"

# Add issue/PR to project
gh project item-add NUMBER --owner OWNER --url "https://github.com/..."

# Delete item
gh project item-delete NUMBER --owner OWNER --id ITEM_ID

# Archive item (hides but keeps)
gh project item-archive NUMBER --owner OWNER --id ITEM_ID
```

## Field Operations

```bash
# List fields (get IDs for updates)
gh project field-list NUMBER --owner OWNER --format json

# Create custom field
gh project field-create NUMBER --owner OWNER \
  --name "Tier" \
  --data-type "SINGLE_SELECT"

# Delete field
gh project field-delete NUMBER --owner OWNER --id FIELD_ID
```

## Updating Item Fields

This is the complex part - you need IDs from field-list:

```bash
# Get field info
gh project field-list NUMBER --owner OWNER --format json | \
  jq '.fields[] | select(.name=="Status")'

# Update status (single-select field)
gh project item-edit \
  --id ITEM_ID \
  --field-id STATUS_FIELD_ID \
  --single-select-option-id DONE_OPTION_ID \
  --project-id PROJECT_ID

# Update text field
gh project item-edit \
  --id ITEM_ID \
  --field-id TEXT_FIELD_ID \
  --text "New value" \
  --project-id PROJECT_ID

# Update number field
gh project item-edit \
  --id ITEM_ID \
  --field-id NUMBER_FIELD_ID \
  --number 42 \
  --project-id PROJECT_ID

# Update date field
gh project item-edit \
  --id ITEM_ID \
  --field-id DATE_FIELD_ID \
  --date "2026-01-30" \
  --project-id PROJECT_ID
```

## JSON Parsing Patterns

```bash
# Get all item titles
gh project item-list NUMBER --owner OWNER --format json | \
  jq -r '.items[].title'

# Get item IDs and titles
gh project item-list NUMBER --owner OWNER --format json | \
  jq -r '.items[] | "\(.id)\t\(.title)"'

# Find specific item ID
gh project item-list NUMBER --owner OWNER --format json | \
  jq -r '.items[] | select(.title=="Item Name") | .id'

# Get Status field options
gh project field-list NUMBER --owner OWNER --format json | \
  jq '.fields[] | select(.name=="Status") | .options'

# Get project ID (needed for item-edit)
gh project view NUMBER --owner OWNER --format json | jq -r '.id'
```

## Common Field Types

| Type | Update Flag | Example |
|------|-------------|---------|
| SingleSelect | `--single-select-option-id` | Status field |
| Text | `--text` | Notes |
| Number | `--number` | Priority |
| Date | `--date` | Due date |
| Iteration | `--iteration-id` | Sprint |

## Default Status Options

Most projects have these status options (IDs vary):
- Todo
- In Progress
- Done

Get actual IDs:
```bash
gh project field-list NUMBER --owner OWNER --format json | \
  jq '.fields[] | select(.name=="Status") | .options[] | {name, id}'
```
