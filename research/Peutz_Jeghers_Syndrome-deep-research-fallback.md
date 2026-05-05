---
provider: manual-fallback
source_providers_attempted:
- falcon
- openai
status: provider_timeout_fallback
created_at: '2026-05-04T01:04:44Z'
disease_name: Peutz-Jeghers syndrome
orpha_id: ORPHA:2869
mondo_id: MONDO:0008280
cited_references:
- ORPHA:2869
- PMID:19916169
- PMID:20301443
- PMID:37054692
- PMID:38660671
- PMID:19541609
- PMID:18311138
- PMID:12650805
- PMID:20051941
- PMID:36970589
- clinicaltrials:NCT06722534
---

# Peutz-Jeghers Syndrome Research Fallback

Deep-research provider attempts were made after the ORPHA:2869 direct
Orphanet/MONDO target was selected:

- `timeout 120 just research-disorder falcon Peutz_Jeghers_Syndrome`
- `timeout 120 just research-disorder openai Peutz_Jeghers_Syndrome`

Both commands printed the initial provider line, then stalled without producing
a research output file and were terminated by the timeout. The curation
therefore used the structured Orphanet cache plus already-fetched PubMed,
GeneReviews, and ClinicalTrials.gov cache records as the auditable evidence
base.

## Literature Scope Checked

- `references_cache/ORPHA_2869.md`: direct Orphanet leaf record for
  Peutz-Jeghers syndrome, including definition, autosomal dominant inheritance,
  exact MONDO and OMIM mappings, STK11 gene assertion, prevalence, age of
  onset, and HPO phenotype rows.
- `references_cache/PMID_19916169.md`: clinical review supporting autosomal
  dominant inheritance and prevalence range.
- `references_cache/PMID_20301443.md`: GeneReviews record supporting childhood
  mucocutaneous pigmentation, GI polyp complications, malignancy spectrum, and
  endoscopic surveillance with polypectomy.
- `references_cache/PMID_37054692.md`: clinical guideline supporting germline
  STK11 pathogenic variants and autosomal dominant inheritance.
- `references_cache/PMID_38660671.md`: human PJS polyp evidence for impaired
  LKB1/AMPK signaling.
- `references_cache/PMID_19541609.md`: human PJS and LKB1 mouse-model evidence
  for mTORC1 hyperactivation and preclinical rapamycin response.
- `references_cache/PMID_18311138.md`: mesenchymal LKB1/TGF-beta mechanism,
  with both mouse-model and human-polyp evidence.
- `references_cache/PMID_12650805.md`: human PJS hamartoma evidence for COX-2
  overexpression.
- `references_cache/PMID_20051941.md`: systematic review of high PJS cancer
  risk.
- `references_cache/PMID_36970589.md`: 566-case human cohort quantifying
  cumulative intussusception risk.
- `references_cache/clinicaltrials_NCT06722534.md`: trial rationale for
  investigational celecoxib chemoprevention.

## Curation Conclusions

- Disease identity is the syndrome-level disorder `ORPHA:2869`, exact to
  `MONDO:0008280` and `OMIM:175200`.
- The core disease mechanism is germline STK11/LKB1 tumor-suppressor loss with
  downstream AMPK impairment, mTORC1 activation, stromal TGF-beta signaling
  defects, COX-2/prostaglandin upregulation, and somatic second-hit-driven
  malignancy risk.
- Orphanet directly supports the syndrome phenotype profile, including oral
  mucosal pigmentation, multiple lentigines, GI hemorrhage, anemia, intestinal
  obstruction, abdominal pain, GI carcinoma, breast carcinoma, and pancreatic
  adenocarcinoma.
- Evidence-backed management includes endoscopic surveillance with
  polypectomy, genetic counseling/cascade testing, and investigational
  mechanism-directed pharmacotherapy with COX-2 or mTOR inhibition.
