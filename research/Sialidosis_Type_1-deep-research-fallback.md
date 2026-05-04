# Sialidosis type 1 Deep Research Fallback

## Provider Attempts

- Falcon: `just research-disorder falcon Sialidosis_Type_1` initially failed before YAML creation because the disorder file did not exist. After the YAML was created, Falcon started and produced no output beyond startup for several minutes; the provider process was terminated to avoid a long silent deep-research wait.
- OpenAI: `just research-disorder openai Sialidosis_Type_1` was attempted after Falcon and produced no output during bounded wait intervals; the provider process was terminated.

## Evidence Scope

The YAML curation integrates deterministic Orphanet structured data and fetched PubMed abstracts:

- ORPHA:812 provides the direct MONDO:0019346 mapping, OMIM cross-reference, definition, autosomal recessive inheritance, epidemiology, NEU1 disease-causing gene row, natural-history onset, and complete HPO phenotype table.
- PMID:41665440 provides the current 2026 multicenter clinical review of Sialidosis type I myoclonic seizures, treatment-response evidence for antiseizure medications, and the literature window through September 2025.
- PMID:38600684 supports the type I genotype-structure-phenotype model in which type I has at least one catalytically active mild NEU1 variant.
- PMID:32143456 supports the lysosomal NEU1 deficiency mechanism, sialylated metabolite accumulation, patient-fibroblast therapeutic testing, and preclinical betaine findings.
- PMID:28138907, PMID:33121223, PMID:10686466, and PMID:23291686 support human clinical manifestations including ataxia, myoclonus, cherry-red spots, neuraminidase deficiency, and progressive neuroimaging changes.
- PMID:10944856 supports residual enzyme activity and abnormal trafficking of type I NEU1 variants in molecular studies.
- PMID:35242566 supports the single reported hematopoietic cell transplantation experience in Sialidosis type I.
- PMID:38321198 supports investigational AAV-mediated NEU1/CTSA gene therapy in a Neu1 knockout mouse model.

## Integration Notes

The curated YAML represents the disease as NEU1-related lysosomal neuraminidase deficiency leading to impaired sialylated glycoconjugate degradation, sialylated metabolite storage, and progressive neuro-ophthalmologic manifestations. All 42 ORPHA:812 phenotype rows are included with exact Orphanet snippets and frequency bands. Treatment sections are limited to evidence-backed symptomatic antiseizure pharmacotherapy, supportive care, investigational betaine/PPCA and AAV approaches, hematopoietic cell transplantation with partial evidence, and genetic counseling.
