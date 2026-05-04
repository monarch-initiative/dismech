---
provider: fallback
model: none
cached: false
start_time: "2026-05-04T18:28:00Z"
end_time: "2026-05-04T19:12:00Z"
duration_seconds: 2640
template_file: provider_failure_fallback
template_variables:
  disease_name: Sialidosis type 1
  mondo_id: MONDO:0019346
  category: Mendelian
citation_count: 12
provider_attempts:
- provider: falcon
  status: terminated_no_output
- provider: openai
  status: terminated_no_output
---

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
- PMID:32453490 supports the Type 1/Type 2 clinical distinction, Type 1 neuro-ophthalmic phenotype selection, retinal ganglion-cell/RNFL storage pathology, and the decision not to retain unsupported dysmorphic or skeletal Type 2 features.
- PMID:28138907, PMID:33121223, PMID:10686466, and PMID:23291686 support human clinical manifestations including ataxia, myoclonus, cherry-red spots, neuraminidase deficiency, and progressive neuroimaging changes.
- PMID:10944856 supports residual enzyme activity and abnormal trafficking of type I NEU1 variants in molecular studies.
- PMID:35242566 supports the single reported hematopoietic cell transplantation experience in Sialidosis type I.
- PMID:38321198 supports investigational AAV-mediated NEU1/CTSA gene therapy in a Neu1 knockout mouse model.

## Integration Notes

The curated YAML represents the disease as NEU1-related lysosomal neuraminidase deficiency leading to impaired sialylated glycoconjugate degradation, sialylated metabolite storage, and separate neurologic and retinal Type 1 mechanisms. ORPHA:812 phenotype rows were reconciled against primary Type 1 literature; dysmorphic, skeletal, visceral, and cutaneous rows consistent with Type 2 contamination were not retained without direct Type 1 support. Treatment sections include evidence-backed symptomatic antiseizure pharmacotherapy, refractory-case sodium oxybate and deep-brain stimulation considerations from the 2026 review, supportive care, investigational betaine/PPCA and AAV approaches, hematopoietic cell transplantation with partial evidence, and genetic counseling.
