# Drug Indication Priority Analysis

Generated: 2026-04-21 20:49 UTC

## Summary Stats

- Total diseases in source YAML: **3079**
- Diseases with at least one drug-indication block: **34**
- Already curated in `kb/disorders/` by exact MONDO ID: **20**
- Missing from dismech by exact MONDO ID: **14**
- Missing-candidate specificity/actions: `CURATE_ROOT`: 11, `REVIEW_SERIES_FOR_PARENT_ROOT`: 2, `CURATE_ROOT_WITH_SUBTYPES`: 1

## Top 50 Prioritized Candidates

| Rank | MONDO ID | Disease | Drug rows | Medium/high evidence rows | ClinGen D/S (desc) | Action | Priority rationale |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| 1 | MONDO:0007534 | Beckwith-Wiedemann syndrome | 17 | 44 | 0/0 | CURATE_ROOT_WITH_SUBTYPES | Broad syndromic disorder, but still worth prioritizing because the imprinting/growth-pathway biology is tractable and the treatment literature is deep. |
| 2 | MONDO:0010382 | fragile X-associated tremor/ataxia syndrome | 8 | 21 | 0/0 | CURATE_ROOT | Good mechanistic repeat-expansion disease target with enough therapeutic literature to support a focused dismech entry. |
| 3 | MONDO:0008564 | DiGeorge syndrome | 11 | 17 | 0/0 | CURATE_ROOT | Deletion syndrome with pleiotropic biology, but immune/endocrine treatment signals and a recognizable disease entity still make it a solid medium-high target. |
| 4 | MONDO:0008678 | Williams syndrome | 13 | 20 | 0/0 | CURATE_ROOT | Reasonable syndromic target with clear copy-number biology and enough cardiovascular/neurodevelopmental therapeutic literature to justify curation. |
| 5 | MONDO:0007452 | maturity-onset diabetes of the young type 1 | 10 | 16 | 0/0 | REVIEW_SERIES_FOR_PARENT_ROOT | Mechanistically strong, treatment-responsive monogenic diabetes subtype, but better handled with an explicit MODY root/series strategy than as a lone subtype. |
| 6 | MONDO:0007453 | maturity-onset diabetes of the young type 2 | 7 | 10 | 0/0 | REVIEW_SERIES_FOR_PARENT_ROOT | Mechanistically strong monogenic diabetes subtype with clear pharmacogenomic implications, though it should probably be curated under a MODY family plan. |
| 7 | MONDO:0011929 | chromosome 1p36 deletion syndrome | 27 | 55 | 0/0 | CURATE_ROOT | Drug-rich but heterogeneous contiguous-gene deletion syndrome; many signals are symptom-targeted rather than a clean disease-mechanism curation target. |
| 8 | MONDO:0029141 | Usher syndrome, type 4 | 17 | 28 | 0/0 | CURATE_ROOT | Disease entity is valid, but the term is subtype-level and much of the current therapy discussion is inherited-retinal/Usher extrapolation rather than USH4-specific. |
| 9 | MONDO:0010775 | retinitis pigmentosa-deafness syndrome | 12 | 8 | 0/0 | CURATE_ROOT | Potentially useful sensory-disease entry, but much of the drug signal is shared retinal-disease pipeline work rather than syndrome-specific intervention evidence. |
| 10 | MONDO:0007810 | autosomal dominant ichthyosis vulgaris | 10 | 26 | 0/0 | CURATE_ROOT | Reasonable disease entity, but most current signals are topical/systemic retinoid management or broader ichthyosis extrapolation rather than a standout mechanistic target. |
| 11 | MONDO:0008698 | achalasia | 12 | 20 | 0/0 | CURATE_ROOT | Clear clinical entity, but mechanism is heterogeneous and much of the treatment signal is symptomatic or procedure-adjunctive rather than disease-mechanistic. |
| 12 | MONDO:0007523 | Ehlers-Danlos syndrome, hypermobility type | 9 | 6 | 0/0 | CURATE_ROOT | Important disorder, but weak molecular anchoring makes mechanism curation harder than for the stronger monogenic candidates above it. |
| 13 | MONDO:0007184 | alopecia, androgenetic, 1 | 28 | 41 | 0/0 | CURATE_ROOT | High raw drug count, but awkward subtype granularity and mostly common alopecia treatment literature make this a weak dismech target. |
| 14 | MONDO:0012454 | alcohol sensitivity, acute | 9 | 15 | 0/0 | CURATE_ROOT | Lowest-fit candidate: the term behaves more like a susceptibility/physiologic response bucket, and its drug list mixes causes, triggers, and related-condition therapy. |

## Methodology Notes

- Parsed the downloaded Monarch YAML at `/tmp/prioritised-rare-disease-list.yml` and used the top-level `diseases` list.
- Treated a disease as having drug-indication data when it contained at least one non-empty `research[].drug_label` block.
- Counted `Drug rows` as the number of such `drug_label` blocks; counted `Medium/high evidence rows` from nested evidence objects where `confidence_drug` was `MEDIUM` or `HIGH`.
- Considered a disease already covered only when an existing `kb/disorders/*.yaml` file had the same `disease_term.term.id` MONDO CURIE.
- Reused the repo's `dismech.compare.mondo_priority` heuristics to label each missing disease as `CURATE_ROOT`, `CURATE_ROOT_WITH_SUBTYPES`, or a lower-fit series/review case based on MONDO hierarchy metadata from the local sqlite DB.
- Loaded ClinGen support from cached `cache/clingen/gene_validity.csv` and counted Definitive/Strong assertions on the candidate MONDO term or its descendants, which reduces false negatives for broad disease roots.
- Final rank = quantitative score (specificity + drug-signal density + treatment rank + descendant-aware ClinGen support) plus a transparent curator-fit adjustment. Those manual adjustments mainly downgraded broad, heterogeneous, or awkwardly granular terms whose drug lists were dominated by symptomatic/general therapy rather than a clear disease-mechanism target.
- Only **14** missing diseases met the inclusion rule, so the requested Top 50 table contains all available uncurated candidates.
