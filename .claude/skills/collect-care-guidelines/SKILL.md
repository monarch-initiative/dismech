---
name: collect-care-guidelines
description: >
  Skill for collecting recent clinical Practice Guideline citations from PubMed
  for dismech disorder entries. Use this skill when building or refreshing a
  care-guideline citation set — searching PubMed by disorder for Publication
  Type "Practice Guideline" within a recent time window, prioritizing disorders
  by guideline availability, and exporting a tab-delimited citation table for
  downstream phenotype/content gap mining (as was done for Fanconi anemia).
---

# Collect Clinical Care Guidelines Skill

## Overview

This skill finds the clinical care guidelines that describe the management of a
dismech disorder, so their phenotype and treatment content can be mined against
the existing knowledge-base entry (the workflow first used for the Fanconi
anemia gap analysis, issue #4878).

A "clinical care description" here is operationalized as a PubMed citation whose
**Publication Type is `Practice Guideline`**, published within the last **10
years** (configurable). PubMed's `Practice Guideline` publication type is a
curated NLM tag applied to society/consensus management guidelines, which makes
it a high-precision filter for care descriptions — far better than free-text
searching for the word "guideline".

The output is a tab-delimited citation table (one row per disorder × PMID) plus
a JSONL discovery record that doubles as a prioritization ranking.

## When to use

- Building an initial care-guideline citation set for a batch of disorders.
- Refreshing an existing set with newly published guidelines.
- Prioritizing which disorders have the richest recent guideline evidence to
  mine for phenotype/treatment gaps.

## The workflow (two steps)

The helper script `scripts/collect_guidelines.py` uses NCBI E-utilities
(`esearch` + `esummary`) with only the standard library plus PyYAML. Run it from
the repo root.

### Step 1 — search

For each disorder, it builds a clean search term (the top-level MONDO mapping
label when present, else the `name` field with underscores as spaces) and runs:

```
esearch  db=pubmed
         term=("<disease name>"[MeSH Terms] OR "<disease name>"[Title/Abstract])
               AND "Practice Guideline"[Publication Type]
         datetype=pdat  reldate=3650   # last 10 years
```

The disease phrase **must be field-tagged** (`[MeSH Terms]` / `[Title/Abstract]`).
A bare quoted phrase lets PubMed's Automatic Term Mapping shatter an unmatched
name into individual all-fields words — e.g. "Alsahan-Harris syndrome" collapses
to `Harris` + `syndrome` and falsely returns dozens of unrelated guidelines.
Field-tagging makes an unmatched disorder correctly return zero.

```bash
# All disorders (≈1,560; ~9 min without an API key at 3 req/s)
python .claude/skills/collect-care-guidelines/scripts/collect_guidelines.py \
    search --out hits.jsonl

# Or a named subset
python .claude/skills/collect-care-guidelines/scripts/collect_guidelines.py \
    search --slugs Asthma,Marfan_Syndrome,Fanconi_Anemia --out hits.jsonl
```

Each JSONL line is `{"slug", "search_name", "count", "pmids"}`. Sorting by
`count` descending is the prioritization ranking — disorders with the most
recent practice guidelines float to the top.

### Step 2 — fetch citation metadata → TSV

```bash
# Keep disorders with ≥1 guideline; take the top 40 by guideline count
python .claude/skills/collect-care-guidelines/scripts/collect_guidelines.py \
    fetch --hits hits.jsonl --out citations.tsv --min-count 1 --top 40
```

The TSV columns are:

| column | meaning |
|--------|---------|
| `disorder_slug` | `kb/disorders/<slug>.yaml` stem |
| `search_name` | the disease term sent to PubMed |
| `pmid` | guideline citation PMID |
| `title` | article title |
| `journal` | journal abbreviation |
| `pub_year` | publication year |
| `pubdate` | full PubMed pubdate string |
| `doi` | DOI when present |
| `publication_types` | all NLM publication types (should include `Practice Guideline`) |
| `guideline_count_for_disorder` | how many guidelines that disorder returned |

## Tuning knobs

- `--reldate <days>` — lookback window (default `3650` = 10 years).
- `--retmax <n>` — max PMIDs captured per disorder (default `30`).
- `--top <n>` / `--min-count <n>` — how many disorders to keep in the TSV.
- `NCBI_API_KEY` env var — raises the rate limit from 3 to 10 req/s.

## Precision notes and caveats

- The bare `"<name>"` term relies on PubMed **Automatic Term Mapping**, which
  expands to the MeSH disease + all-fields text. This favors recall; a returned
  guideline is *about* the disease in the vast majority of cases, but the set is
  a **candidate list for human curation**, not final evidence.
- The `Practice Guideline` publication type is narrower than `Guideline`. Switch
  the `PUBTYPE` constant in the script if you want to widen to `Guideline`.
- Disorders whose `name`/MONDO label is a broad parent (e.g. "Glioblastoma,
  IDH-Wildtype") may under- or over-match; spot-check the top hits.
- This is a **discovery** step. Any citation ultimately used as dismech evidence
  must still pass the normal snippet-verification workflow
  (`just fetch-reference`, `just validate-references`) — the `.hpoa`/guideline
  provenance alone does not satisfy the dismech PMID + verified-snippet policy.

## Relationship to the Fanconi anemia precedent

The FA gap analysis (`projects/FANCONI_ANEMIA_GAP_ANALYSIS.md`) mined a single
disorder's care guideline into a custom HPO profile and diffed it against the
dismech entry. This skill generalizes the *discovery* half of that work across
all disorders so the same mining can be prioritized and repeated at scale. See
`projects/CLINICAL_CARE_GUIDELINES/` for the tracked citation set.
