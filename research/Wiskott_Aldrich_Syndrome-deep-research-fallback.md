---
provider: manual-fallback
source_providers_attempted:
- falcon
- openai
status: provider_timeout_fallback
created_at: '2026-05-04T03:42:30Z'
disease_name: Wiskott-Aldrich syndrome
orpha_id: ORPHA:906
mondo_id: MONDO:0010518
cited_references:
- ORPHA:906
- PMID:7579347
- PMID:10523789
- PMID:19628299
- PMID:28805251
- PMID:26159751
- PMID:21659547
---

# Wiskott-Aldrich Syndrome Research Fallback

Deep-research provider attempts were made after selecting the direct
Orphanet/MONDO target `ORPHA:906` / `MONDO:0010518`:

- `timeout 180 just research-disorder falcon Wiskott_Aldrich_Syndrome`
- `timeout 180 just research-disorder openai Wiskott_Aldrich_Syndrome`

Both commands printed the initial provider line, then stalled without
producing a research output file and were terminated by the timeout. The
curation therefore used the structured Orphanet cache plus fetched PubMed
cache records as the auditable evidence base.

## Literature Scope Checked

- `references_cache/ORPHA_906.md`: direct Orphanet disease record for
  Wiskott-Aldrich syndrome, including definition, X-linked recessive
  inheritance, exact MONDO and OMIM mappings, prevalence, age of onset, WAS
  disease-gene assertion, and HPO phenotype rows.
- `references_cache/PMID_7579347.md`: human molecular study showing that
  Wiskott-Aldrich syndrome and X-linked congenital thrombocytopenia are caused
  by mutations of the same WAS gene, with classic WAS linked to complex
  mutations such as termination codons and frameshifts.
- `references_cache/PMID_10523789.md`: review supporting WAS as a disorder of
  hematopoietic actin-cytoskeleton regulation, including membrane-to-actin
  signal transduction and defects in cell polarization and motility.
- `references_cache/PMID_19628299.md`: review supporting defective immune-cell
  migration, antigen uptake, activation, and host defense due to WASp
  deficiency.
- `references_cache/PMID_28805251.md`: review supporting WASp roles in innate
  and adaptive immunity, including immune synapse formation, cell signaling,
  migration, cytokine release, regulatory T and B cell defects, and B-cell
  selection abnormalities.
- `references_cache/PMID_26159751.md`: clinical treatment review supporting
  life-threatening disease burden, bleeding tendency, eczema, autoimmunity,
  malignancy risk, hematopoietic stem cell transplantation, gene therapy, and
  management of pre- and post-transplant complications.
- `references_cache/PMID_21659547.md`: retrospective collaborative human HCT
  cohort of 194 patients supporting survival outcomes, chimerism, and
  persistent thrombocytopenia risk when myeloid donor chimerism is low.

## Curation Conclusions

- Disease identity is the syndrome-level disorder `ORPHA:906`, exact to
  `MONDO:0010518` and `OMIM:301000`.
- The primary mechanism is WAS pathogenic variation causing deficient or
  dysfunctional WASp in hematopoietic cells.
- WASp dysfunction disrupts actin cytoskeleton organization and membrane-to-
  actin signaling, producing impaired immune-cell migration, antigen uptake,
  activation, immune synapse function, signaling, cytokine release, and host
  defense.
- Platelet involvement is represented as microthrombocytopenia with abnormal
  platelet morphology, prolonged bleeding time, bruising, hematomas, and
  internal hemorrhage.
- Orphanet directly supports the curated very-frequent phenotypes:
  immunodeficiency, recurrent respiratory infections, sinusitis, otitis media,
  chronic otitis media, thrombocytopenia, abnormal platelet morphology,
  prolonged bleeding time, bruising susceptibility, spontaneous hematomas,
  internal hemorrhage, decreased total lymphocyte count, fever, chronic
  diarrhea, and chronic pulmonary obstruction.
- Additional evidence-backed features include eczematoid dermatitis,
  autoimmunity, hemolytic anemia, large-intestine inflammation, and lymphoma.
- Evidence-backed treatments are hematopoietic stem cell transplantation,
  emerging gene therapy, and supportive management of infections, bleeding,
  eczema, autoimmunity, and transplant-related complications.
