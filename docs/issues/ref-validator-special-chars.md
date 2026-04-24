# Bug Report: YAML Frontmatter Not Properly Quoted in Cached Markdown Files

## Summary

The `linkml-reference-validator` fails to parse cached reference files when the YAML frontmatter contains unquoted values with special characters (colons, square brackets, etc.).

## Affected Component

`linkml_reference_validator/etl/reference_fetcher.py` - specifically `_save_to_disk()` and `_load_markdown_format()` methods.

## Description

When `ReferenceFetcher._save_to_disk()` writes reference metadata to a markdown file with YAML frontmatter, it does not quote values that contain YAML special characters. When the same file is later read by `_load_from_disk()` -> `_load_markdown_format()`, the YAML parser fails.

### Root Cause

In `_save_to_disk()` (lines 337-383), values are written directly without quoting:

```python
lines.append(f"title: {reference.title}")
```

If `reference.title` contains a colon (e.g., `"Exercise-induced asthma: an overview"`) or starts with a bracket (e.g., `"[Differentiation of dyspnea in patients...]"`), the resulting YAML is invalid.

### Failing YAML Examples

**Colon in value:**
```yaml
---
reference_id: PMID:11678516
title: Exercise-induced asthma: an overview.
---
```
The second colon in the title is interpreted as a YAML mapping separator.

**Square bracket at start:**
```yaml
---
reference_id: PMID:29601558
title: [Differentiation of dyspnea in patients with asthma and lung sarcoidosis].
---
```
The `[...]` is interpreted as a YAML list.

## Reproduction Steps

1. Install linkml-reference-validator
2. Create a test schema with reference validation enabled:

```yaml
# test_schema.yaml
id: https://example.org/test
name: test
prefixes:
  linkml: https://w3id.org/linkml/
  PMID: https://pubmed.ncbi.nlm.nih.gov/

imports:
  - linkml:types

classes:
  TestClass:
    attributes:
      reference:
        range: string
        implements:
          - linkml:authoritative_reference
      snippet:
        range: string
        implements:
          - linkml:excerpt
```

3. Create test data referencing a paper with special characters in title:

```yaml
# test_data.yaml
reference: "PMID:11678516"
snippet: "Asthmatic attack in exercise-induced asthma is brought about by hyperventilation"
```

4. Run validation twice:

```bash
# First run - fetches and caches (succeeds)
linkml-reference-validator validate data test_data.yaml --schema test_schema.yaml --target-class TestClass

# Second run - reads from cache (FAILS)
linkml-reference-validator validate data test_data.yaml --schema test_schema.yaml --target-class TestClass
```

## Error Message

```
ScannerError: mapping values are not allowed in this context
  in "<unicode string>", line 3, column 31
```

or

```
ParserError: while parsing a block mapping
  in "<unicode string>", line 2, column 1
did not find expected key
  in "<unicode string>", line 3, column 81
```

## Test Cases

### Test Case 1: Title with colon

**PMID:** 11678516
**Title:** "Exercise-induced asthma: an overview."

**Current (broken) cache format:**
```yaml
---
reference_id: PMID:11678516
title: Exercise-induced asthma: an overview.
---
```

**Expected (fixed) cache format:**
```yaml
---
reference_id: "PMID:11678516"
title: "Exercise-induced asthma: an overview."
---
```

### Test Case 2: Title with square brackets

**PMID:** 29601558
**Title:** "[Differentiation of dyspnea in patients with asthma and lung sarcoidosis]."

**Current (broken) cache format:**
```yaml
---
reference_id: PMID:29601558
title: [Differentiation of dyspnea in patients with asthma and lung sarcoidosis].
---
```

**Expected (fixed) cache format:**
```yaml
---
reference_id: "PMID:29601558"
title: "[Differentiation of dyspnea in patients with asthma and lung sarcoidosis]."
---
```

### Test Case 3: DOI with special characters

**PMID:** 11678516
**DOI:** 10.1097/00000441-200110000-00009

**Current format (may be problematic):**
```yaml
doi: 10.1097/00000441-200110000-00009
```

**Safer format:**
```yaml
doi: "10.1097/00000441-200110000-00009"
```

## Suggested Fix

**Use a proper YAML library to serialize the frontmatter instead of manual string concatenation.**

The current code manually constructs YAML with f-strings, which is fragile and doesn't handle escaping. Since `ruamel.yaml` is already a dependency (used in `_load_markdown_format()`), it should also be used for writing:

```python
from ruamel.yaml import YAML
from io import StringIO

def _save_to_disk(self, reference: ReferenceContent) -> None:
    """Save reference content to disk cache as markdown with YAML frontmatter."""
    cache_path = self._get_cache_path(reference.reference_id)

    # Build frontmatter dict
    frontmatter = {
        "reference_id": reference.reference_id,
    }
    if reference.title:
        frontmatter["title"] = reference.title
    if reference.authors:
        frontmatter["authors"] = reference.authors
    if reference.journal:
        frontmatter["journal"] = reference.journal
    if reference.year:
        frontmatter["year"] = reference.year
    if reference.doi:
        frontmatter["doi"] = reference.doi
    frontmatter["content_type"] = reference.content_type

    # Serialize frontmatter with ruamel.yaml
    yaml = YAML()
    yaml.default_flow_style = False
    stream = StringIO()
    yaml.dump(frontmatter, stream)
    frontmatter_str = stream.getvalue()

    # Build markdown body
    body_lines = []
    if reference.title:
        body_lines.append(f"# {reference.title}")
        if reference.authors:
            body_lines.append(f"**Authors:** {', '.join(reference.authors)}")
        if reference.journal:
            journal_info = reference.journal
            if reference.year:
                journal_info += f" ({reference.year})"
            body_lines.append(f"**Journal:** {journal_info}")
        if reference.doi:
            body_lines.append(f"**DOI:** [{reference.doi}](https://doi.org/{reference.doi})")
        body_lines.append("")
        body_lines.append("## Content")
        body_lines.append("")

    if reference.content:
        body_lines.append(reference.content)

    # Combine into final document
    content = f"---\n{frontmatter_str}---\n\n" + "\n".join(body_lines)
    cache_path.write_text(content, encoding="utf-8")
    logger.info(f"Cached {reference.reference_id} to {cache_path}")
```

This approach:
1. Uses the same YAML library for reading and writing (symmetry)
2. Automatically handles all quoting/escaping edge cases
3. Is more maintainable than manual string construction
4. Follows the principle of using proper serialization libraries for structured data

## Workaround

Until fixed, users can run this script to fix cached files:

```python
#!/usr/bin/env python3
"""Fix YAML quoting in linkml-reference-validator cache files."""
import re
from pathlib import Path

def fix_cache_files(cache_dir: Path = Path("references_cache")):
    if not cache_dir.exists():
        return

    for md_file in cache_dir.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        if not content.startswith("---"):
            continue

        parts = content.split("---", 2)
        if len(parts) < 3:
            continue

        frontmatter, body = parts[1], parts[2]
        lines = frontmatter.split("\n")
        new_lines = []
        modified = False

        for line in lines:
            if not line.strip() or line.strip().startswith("-"):
                new_lines.append(line)
                continue

            match = re.match(r'^(\s*)([a-z_]+):\s+(.+)$', line, re.IGNORECASE)
            if match:
                indent, key, value = match.groups()
                needs_quoting = (
                    ':' in value or
                    value.startswith('[') or
                    value.startswith('{') or
                    value.startswith('*') or
                    value.startswith('&')
                )
                is_quoted = value.startswith('"') or value.startswith("'")

                if needs_quoting and not is_quoted:
                    escaped = value.replace('"', '\\"')
                    new_lines.append(f'{indent}{key}: "{escaped}"')
                    modified = True
                    continue

            new_lines.append(line)

        if modified:
            new_content = f"---{chr(10).join(new_lines)}---{body}"
            md_file.write_text(new_content, encoding="utf-8")
            print(f"Fixed: {md_file.name}")

if __name__ == "__main__":
    fix_cache_files()
```

## Environment

- Python: 3.10+
- linkml-reference-validator: (installed from git main branch)
- ruamel.yaml: (dependency of linkml-reference-validator)

## Impact

This bug prevents validation from working on any dataset that references papers with special characters in their titles - which is extremely common in scientific literature (e.g., "X: a study of Y", "[Article in French]", etc.).

In testing with a real knowledge base of 55 disorders, 99 out of ~150 cached reference files had this issue.
