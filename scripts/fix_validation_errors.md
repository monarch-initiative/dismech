# Reference Validation Error Fixing Guide

## Summary of Work Done

### Files Fixed
1. **Nephronophthisis.yaml** - Fixed 7 errors:
   - 5 minor text corrections (typos, formatting)
   - 2 hallucinated snippets replaced with actual paper text

2. **Asthma.yaml** - Fixed 19 of 20 errors:
   - Removed hallucinated snippets (PMID:38641129)
   - Fixed truncated sentences
   - Corrected formatting (β2 vs beta2, µg vs microg, etc.)
   - Removed "None." and "Title only:" placeholder snippets
   - 1 remaining error is due to a validator caching bug (documented)

## Types of Errors Encountered

### 1. Minor Text Differences (Easy to Fix)
- Spelling differences in source papers (e.g., "nephronophtisis" vs "nephronophthisis")
- Formatting differences (e.g., "PM10" vs "PM(10)", "β2" vs "beta2")
- Missing prefixes like "RESULTS:", "BACKGROUND:", "CONCLUSIONS:"
- "progress" vs "progresses" (grammar errors in source papers)

**Fix**: Use the suggested text from the validator output.

### 2. Truncated Sentences
- Snippets that combine text from different parts of a paper
- Extra sentences that aren't in the abstract

**Fix**: Use only the text that matches the source, or use a shorter quote.

### 3. Hallucinated Content
- Fabricated quotes not in the cited paper
- Statistics that don't exist (e.g., "10%" when paper says "95%")
- Completely made-up sentences

**Fix**: Either replace with actual text from the paper, or remove the evidence item if it's NO_EVIDENCE or doesn't add value.

### 4. Placeholder Content
- Snippets like "None.", "Abstract not provided.", "Title only: ..."

**Fix**: Remove these evidence items entirely.

## Running Validation

```bash
# Validate a single file
just validate-references kb/disorders/FILENAME.yaml

# Or directly:
uv run linkml-reference-validator validate data kb/disorders/FILENAME.yaml \
  --schema src/dismech/schema/dismech.yaml --target-class Disease
```

## Checking Cached Paper Content

Papers are cached in `references_cache/PMID_XXXXX.md`. You can check what text is actually in a paper:

```bash
cat references_cache/PMID_XXXXX.md | grep -i "search term"
```

## Known Issues

### Validator Caching Bug
The validator may cache old YAML content and show errors for already-fixed snippets. See `bug_reports/validator_caching_issue.md`.

### Fuzzy Matching False Positives
The fuzzy matcher can report high similarity scores (90%+) for completely unrelated text. See `bug_reports/fuzzy_matching_false_positive.md`.

## Quick Fix Script

For each error, the general approach is:

1. Check the suggestion in the error output
2. If it's a close match (>90%), use the suggested text
3. If no suggestion or low match:
   - Check the cached paper: `cat references_cache/PMID_XXXXX.md`
   - If text is hallucinated, either replace with actual text or remove the evidence
4. If the evidence is marked NO_EVIDENCE with a placeholder snippet, remove it
