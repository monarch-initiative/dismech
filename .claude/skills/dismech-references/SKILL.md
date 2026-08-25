---
name: dismech-references
description: >
  Add, validate, repair, or review evidence references and exact-quote snippets
  in dismech KB YAML and deep-research reports. Use for PMID, DOI, NCT, ICTRP,
  or structured-source evidence; reference-cache generation; snippet failures;
  title snippets; bracket normalization; deep-research citation validation;
  Named Entity Confusion preflight; evidence_source classification; and final
  evidence checks before a PR.
---

# Curate Evidence and References

Use this workflow whenever evidence or its cited source changes.

## Non-negotiable rules

- Quote an exact substring of the cited source. Do not paraphrase or fabricate a
  `snippet`.
- Confirm that the quote substantively supports the precise claim. A matching
  string from the wrong paper, or an unrelated sentence from the right paper,
  is not evidence.
- Prefer a result sentence from the abstract or authoritative source record.
  A paper title usually establishes only that a topic was studied.
- Never create or hand-edit `references_cache/*.md`. Generate or regenerate a
  cache entry with `just fetch-reference <ID>`.
- Never use fuzzy auto-repair to rewrite snippets. Read the source and copy the
  exact passage, choose another source, or remove the evidence.
- Treat deep-research output as leads, not ground truth.

## Evidence shape

```yaml
evidence:
  - reference: PMID:12345678
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "Exact text copied from the cited source."
    explanation: "How this passage supports the specific KB claim."
```

Use `supports: SUPPORT`, `REFUTE`, or the value allowed by the schema. Make the
`explanation` connect the quote to the claim without adding conclusions the
quote does not establish.

Classify `evidence_source` by the cited study, not by the curator or the claim:

- `HUMAN_CLINICAL`: patients, cohorts, clinical observations, or trials
- `MODEL_ORGANISM`: in vivo non-human animal or organism work
- `IN_VITRO`: cells, organoids, explants, or biochemical assays
- `COMPUTATIONAL`: modeling, simulation, or in-silico analysis
- `OTHER`: evidence that does not fit the categories above

Inspect the schema and nearby current entries if a field or enum is uncertain.

## Workflow

### 1. Screen deep-research sources

If evidence came from `research/`, first read the report's
`reference_validation`, `unresolved_references`, `needs_review`, and
`off_topic_references` results. Do not curate an unresolved identifier. An
off-topic flag is a reason to inspect the paper, not an automatic rejection.

For an older report without validation output, run:

```bash
just validate-research-reference research/My_Disease-deep-research-falcon.md
```

Before using any report content, check that the report describes the intended
disease:

```bash
just preflight-dr research/My_Disease-deep-research-falcon.md MONDO:XXXXXXX
```

Interpret the result as follows:

- `PASS`: proceed to normal source, snippet, and term verification.
- `WARN`: resolve the reported conflict or degraded lookup, then manually check
  the causal gene, OMIM xref, and synonyms.
- `FAIL`: discard the report. Do not cherry-pick from it.
- `SKIP`: the automated check cannot discriminate; manually check disease
  identity before proceeding.

For a `WARN` or `SKIP`, inspect the intended MONDO record directly:

```bash
uv run runoak -i sqlite:obo:mondo info MONDO:XXXXXXX -O obo
```

Compare its causal-gene relationship (`RO:0004003`), OMIM xref, and synonyms
with the report. Look specifically for synonym aliasing, eponymic collision,
abbreviation ambiguity, or conflation with a closely related disease. On any
identity mismatch, discard the report rather than cherry-picking from it.

See `docs/deep-research-reference-validation.md` and
`research/nec_risk_disease_classes.md` for uncommon cases.

### 2. Fetch each new reference

```bash
just fetch-reference PMID:12345678
```

Use the actual identifier for other supported reference types. Read the fetched
record and confirm its identity, topic, and quoted passage. A successful fetch
does not prove that the source supports the claim.

### 3. Run the fast edit loop

After each disorder-file edit, run:

```bash
just validate kb/disorders/MyDisease.yaml
just count-verified-snippets kb/disorders/MyDisease.yaml
just validate-terms kb/disorders/MyDisease.yaml
```

All three commands accept the files supported by their recipes; batch files
where practical. `count-verified-snippets` is fast and offline, but advisory.
It reports missing cache entries and skipped prefixes rather than resolving
them.

### 4. Run the authoritative pre-PR sweep

Once, after the tranche is complete, name every changed disorder file:

```bash
just validate-disorders \
  kb/disorders/FirstDisease.yaml \
  kb/disorders/SecondDisease.yaml
```

This batched command mirrors CI's schema, term, and reference checks and uses
`--no-full-text`. It is the authoritative evidence gate for disorder files.
Use `just validate-references <file>` only when a non-disorder target or a
full-text-permitting diagnostic requires it.

Never report a validation command as passing unless it finished and you read
its output.

## Resolve failures

When a snippet is not found:

1. Read the fetched source record.
2. Confirm the identifier belongs to the intended paper or record.
3. Copy an exact, substantively relevant passage.
4. If no such passage exists, cite a better source or remove the evidence.

If the claim is useful but no quotable evidence is available, move it to a
`notes` field where appropriate, keep an unevidenced description only where the
schema and curation policy permit it, or remove the claim. Never manufacture a
quote to preserve an evidence block.

`Total checks: 0` in reference-validator output means zero issues were counted;
it does not mean no evidence was examined. Use the wrapper's affirmative
`Snippets checked: N/N verified` summary to describe cache-backed coverage.

Reference prefixes in `skip_prefixes` within
`conf/reference_validator_config.yaml`, including `DOI:`, are not
snippet-checked. Treat a skipped reference as unverified by these commands.

## Titles and brackets

Run `just check-title-snippets` when adding or repairing evidence. Quote a title
only in the rare case that the title itself states a result; explain why it is
probative. If the cached record has no abstract, cite the underlying study or a
different source instead of treating a topic-shaped title as a finding. Do not
manually regenerate `tests/title_snippet_baseline.txt` when fixing an existing
title snippet.

Snippet matching applies `literal_bracket_patterns` from
`conf/reference_validator_config.yaml`:

- all-caps abbreviations and spans containing a percent sign remain literal and
  must be quoted exactly;
- numeric citation markers and curator glosses are stripped before matching.

If a verbatim quote fails near brackets, read the reason printed by
`count-verified-snippets`. Do not change the global patterns to accommodate one
snippet without replaying validation across the KB.

## Frequency claims

A phenotype `frequency:` value is a separate quantitative claim from the
disease-phenotype association. Give it evidence that supports the frequency
band or omit it. Follow `docs/frequency-evidence-guidelines.md` for acceptable
quantitative, derived, qualitative, and clinical-estimate evidence.

## Reference-cache integrity

Check the derived cache structure with:

```bash
just check-reference-cache-frontmatter
```

If an entry is malformed or incorrect, regenerate it with
`just fetch-reference <ID>`; never patch its filename, frontmatter, or content.
