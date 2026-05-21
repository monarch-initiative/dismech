# Wilson Disease — Review Scorecard

Branch: `claude/wilson-disease-review-9TB43`
Reviewer: collaborative (human + Claude), hybrid workflow
Scope: evidence integrity, scientific/clinical accuracy, completeness (schema/term validation out of scope)

## Evidence integrity

- Method: whitespace-normalized substring check vs `references_cache/` (bundled
  `linkml-reference-validator` is a no-op in the web sandbox — reports
  "Total checks: 0" for every file).
- Result: **157 / 157 snippet-bearing evidence items verified**, 0 mismatches,
  0 missing cache files. DOI-only `references:` entries carry no snippets.
- Status: PASS.

## Section verdicts

| Section | Items | Verdict | Notes |
|---|---|---|---|
| description / notes | — | accept | accurate, Leipzig score named |
| inheritance / prevalence / progression | 1 / 3 / 1 | accept | genetic vs clinical prevalence discrepancy handled well |
| mechanistic_hypotheses | 5 | accept | CANONICAL/EMERGING split correct |
| pathophysiology | 11 | accept | causal graph correct; fibrosis module conformance valid |
| phenotypes | 55 | accept w/ flags | see open items (cardiac frequency) |
| biochemical / genetic / environmental | 4 / 1 / 1 | accept | ClinGen + Orphanet corroboration good |
| treatments | 6 | accept | chelators, zinc, TTM, transplant all evidenced |
| differential_diagnoses | 2 | accept | could expand (see open items) |

## Open items (decisions pending)

1. Cardiac Arrhythmia (OCCASIONAL) / Heart Failure frequency rest on an
   HR-only claims study (PMID:28947309) — HR != absolute-frequency band.
2. Completeness candidates: nephrolithiasis, aminoaciduria/Fanconi
   specificity, recurrent spontaneous abortion/infertility, azure lunulae.
3. Subtype structure (hepatic / neurologic / presymptomatic) — none modeled;
   architecturally significant (phenotype.subtype foreign keys).
4. Minor: `evidence_source` inconsistent for review-article citations
   (sometimes OTHER, sometimes absent).

## Decisions log

(to be filled as we converge)
