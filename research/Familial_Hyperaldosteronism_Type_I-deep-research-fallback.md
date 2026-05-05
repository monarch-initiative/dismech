---
provider: manual-fallback
source_providers_attempted:
- falcon
- openai
status: provider_timeout_fallback
created_at: '2026-05-04T00:25:32Z'
disease_name: Familial hyperaldosteronism type I
orpha_id: ORPHA:403
mondo_id: MONDO:0007080
cited_references:
- ORPHA:403
- PMID:1731223
- PMID:35012455
- PMID:35778363
- PMID:10618671
- PMID:21451421
---

# Familial Hyperaldosteronism Type I Research Fallback

Deep-research provider attempts were made after the ORPHA:403 leaf disorder was selected:

- `timeout 240 just research-disorder falcon Familial_Hyperaldosteronism_Type_I`
- `timeout 180 just research-disorder openai Familial_Hyperaldosteronism_Type_I`

Both commands stalled without producing a research output file and were terminated. The curation therefore used the structured Orphanet cache plus fetched PubMed abstracts as the auditable evidence base.

## Literature Scope Checked

- `references_cache/ORPHA_403.md`: direct Orphanet leaf record for familial hyperaldosteronism type I, including definition, autosomal dominant inheritance, exact MONDO and OMIM mappings, CYP11B1/CYP11B2 fusion-gene assertions, and HPO phenotype rows.
- `references_cache/PMID_1731223.md`: seminal human study identifying unequal crossover producing a chimeric CYP11B1/CYP11B2 gene under ACTH control.
- `references_cache/PMID_35778363.md`: clinical review summarizing familial primary hyperaldosteronism forms and confirming that type I results from CYP11B2/CYP11B1 fusion with ACTH-regulated aldosterone synthesis.
- `references_cache/PMID_35012455.md`: human diagnostic sequencing paper supporting molecular testing for the CYP11B1/CYP11B2 chimeric form.
- `references_cache/PMID_10618671.md`: genetically proven GRA case in which spironolactone replaced dexamethasone after corticosteroid side effects and controlled blood pressure.
- `references_cache/PMID_21451421.md`: randomized primary-aldosteronism trial comparing spironolactone and eplerenone, supporting the mineralocorticoid receptor antagonist treatment class.

## Curation Conclusions

- Disease identity is the leaf disorder `ORPHA:403`, exact to `MONDO:0007080` and `OMIM:103900`. The broader familial hyperaldosteronism group `ORPHA:235936` was checked but is not emitted by the repository's structured Orphanet source.
- The primary mechanism is a CYP11B1/CYP11B2 chimeric gene from unequal crossover, causing ACTH-regulated aldosterone synthase expression, aldosterone and hybrid steroid excess, suppressed renin, variable hypokalemia, and hypertension.
- Orphanet directly supports the added phenotype profile, including hypertension, dexamethasone-suppressible primary hyperaldosteronism, low renin, hypokalemia, adrenal hyperplasia, secretory adrenocortical adenoma, preeclampsia, epistaxis, caesarean section, intracranial hemorrhage, headache, muscle weakness, and polydipsia.
- Mechanism-directed treatment includes low-dose glucocorticoid suppression and mineralocorticoid receptor antagonist therapy when corticosteroid side effects or additional blood pressure control make receptor blockade clinically relevant.
