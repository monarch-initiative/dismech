---
name: dismech-references
description: >
  Skill for validating and repairing evidence references in the dismech knowledge base.
  Use this skill when working with evidence items in disorder YAML files, validating
  that snippet text matches PubMed abstracts, and repairing misquoted or fabricated
  evidence. Critical for ensuring scientific accuracy and preventing AI hallucinations.
---

# Dismech Reference Validation Skill

## Overview

Validate and repair evidence references in the dismech disorder knowledge base. This ensures
that quoted snippets actually appear in the cited PubMed abstracts, preventing fabricated
or misquoted evidence from entering the knowledge base.

## When to Use

- Validating evidence items after adding new disorder content
- Checking that snippets match their cited PMID abstracts
- Repairing evidence items with minor text mismatches
- Removing fabricated evidence (AI hallucinations)
- QC checks before committing changes

## Evidence Item Structure

All evidence items follow this YAML structure:

```yaml
evidence:
  - reference: PMID:12345678
    supports: SUPPORT  # SUPPORT, REFUTE, PARTIAL, NO_EVIDENCE, WRONG_STATEMENT
    snippet: "Exact quoted text from the abstract"
    explanation: "Why this evidence supports/refutes the claim"
```

### Support Classifications

| Value | Meaning |
|-------|---------|
| SUPPORT | Evidence directly supports the statement |
| REFUTE | Evidence contradicts the statement |
| PARTIAL | Evidence partially supports with caveats |
| NO_EVIDENCE | Citation exists but doesn't address the claim |
| WRONG_STATEMENT | The statement itself is incorrect |

## Validation Commands

### Validate a Single File
```bash
uv run linkml-reference-validator validate data kb/disorders/Asthma.yaml \
  --schema src/dismech/schema/dismech.yaml \
  --target-class Disease
```

### Validate All Disorder Files
```bash
just validate-all
```

Or manually:
```bash
for f in kb/disorders/*.yaml; do
  echo "=== $f ==="
  uv run linkml-reference-validator validate data "$f" \
    --schema src/dismech/schema/dismech.yaml \
    --target-class Disease
done
```

### Using the Just Target
```bash
just qc  # Runs all QC including reference validation
```

## Repair Commands

### Dry Run (Preview Changes)
```bash
uv run linkml-reference-validator repair data kb/disorders/Cholera.yaml \
  --schema src/dismech/schema/dismech.yaml \
  --target-class Disease
```

### Auto-Repair with Threshold
```bash
uv run linkml-reference-validator repair data kb/disorders/Cholera.yaml \
  --schema src/dismech/schema/dismech.yaml \
  --target-class Disease \
  --no-dry-run \
  --fix-threshold 0.80
```

The `--fix-threshold 0.80` means snippets with 80%+ similarity to the actual abstract
text will be automatically corrected.

## Common Error Patterns

### 1. Snippet Not Found in Abstract
```
ERROR: Snippet not found in reference PMID:12345678
  Snippet: "The patient showed symptoms..."
  Abstract: [actual abstract text]
```

**Solutions:**
- Check if snippet is from full text (not abstract) - may need to remove
- Check for minor typos - use repair with threshold
- If fabricated, remove the evidence item entirely

### 2. Reference Cannot Be Fetched
```
ERROR: Could not fetch reference PMID:99999999
```

**Solutions:**
- Verify PMID exists on PubMed
- Check for typos in PMID
- If PMID is invalid, remove the evidence item

### 3. Fabricated Evidence Patterns

Watch for these red flags indicating AI-generated fake evidence:
- Snippet says "N/A" or "No abstract available"
- Snippet is suspiciously perfect match to the claim
- PMID doesn't exist or is for unrelated topic
- Generic statements without specific data

**Solution:** Remove the entire evidence item.

## Cache Management

Reference validator caches PubMed abstracts in `.refval_cache/`. If you encounter
stale cache issues:

```bash
rm -rf .refval_cache/
```

### Cache File Format Issues

If you see YAML parsing errors in cache files, check for unquoted colons in titles:
```yaml
# Bad - will cause parse error
title: COVID-19: A New Challenge

# Good - properly quoted
title: "COVID-19: A New Challenge"
```

## Batch Processing Workflow

### 1. Get Error Count
```bash
uv run linkml-reference-validator validate data kb/disorders/*.yaml \
  --schema src/dismech/schema/dismech.yaml \
  --target-class Disease 2>&1 | grep -c "ERROR"
```

### 2. Process Files with Errors
```bash
for f in kb/disorders/*.yaml; do
  errors=$(uv run linkml-reference-validator validate data "$f" \
    --schema src/dismech/schema/dismech.yaml \
    --target-class Disease 2>&1 | grep -c "ERROR" || echo 0)
  if [ "$errors" -gt 0 ]; then
    echo "=== $f has $errors errors ==="
  fi
done
```

### 3. Auto-Repair All
```bash
for f in kb/disorders/*.yaml; do
  uv run linkml-reference-validator repair data "$f" \
    --schema src/dismech/schema/dismech.yaml \
    --target-class Disease \
    --no-dry-run \
    --fix-threshold 0.80
done
```

## Best Practices

### Adding New Evidence

1. **Use real PMIDs**: Always verify the PMID exists on PubMed
2. **Quote exactly**: Copy snippet text directly from the abstract
3. **Keep snippets short**: 1-2 sentences that directly support the claim
4. **Validate immediately**: Run validation after adding evidence

### Reviewing AI-Generated Content

When reviewing disorder files that may contain AI-generated evidence:

1. Run validation first to catch obvious fabrications
2. Spot-check PMIDs on PubMed
3. Look for suspiciously perfect or generic snippets
4. Remove any evidence that cannot be verified

### Handling Unfetchable References

If a reference cannot be fetched:
1. Manually check PubMed for the PMID
2. If it exists but is restricted, note in explanation
3. If it doesn't exist, remove the evidence item
4. Consider replacing with a valid alternative reference

## Integration with Schema

The evidence structure is defined in `src/dismech/schema/dismech.yaml`:

```yaml
EvidenceItem:
  attributes:
    reference:
      description: PMID or DOI reference
      pattern: "^PMID:\\d+$|^DOI:.*$"
    supports:
      range: SupportType
    snippet:
      description: Quoted text from the reference
    explanation:
      description: Why this evidence supports/refutes the claim
```
