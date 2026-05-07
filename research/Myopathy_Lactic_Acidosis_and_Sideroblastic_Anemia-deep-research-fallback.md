# Myopathy, Lactic Acidosis, and Sideroblastic Anemia Deep Research Fallback

## Provider Attempts

- 2026-05-07: `timeout 90s just research-disorder falcon Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia`
  timed out with exit code 124 after the provider command was terminated by
  `timeout`.
- 2026-05-07: `timeout 90s just research-disorder openai Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia`
  timed out with exit code 124 after the provider command was terminated by
  `timeout`.

No provider-generated deep-research artifact was available to integrate.
Curation therefore proceeded from generated structured Orphanet evidence and
fetched PubMed caches, without hand-editing any `references_cache/*.md` files.

## Evidence Scope Used For Curation

- ORPHA:2598 structured record for disease definition, MONDO and OMIM cross
  references, autosomal recessive inheritance, point prevalence, PUS1 and YARS2
  gene associations, and HPO phenotype rows.
- PMID:15108122 for the original PUS1-associated MLASA families and the
  framing of MLASA as an autosomal recessive oxidative phosphorylation disorder
  affecting skeletal muscle and bone marrow.
- PMID:15772074 for absent or reduced PUS1-dependent mitochondrial tRNA
  pseudouridylation as a molecular pathogenesis mechanism.
- PMID:17056637 for PUS1 loss-of-function evidence, reduced mitochondrial
  translation, and combined respiratory-chain defects.
- PMID:20598274 for YARS2 as a cause of MLASA and the mechanism linking reduced
  mitochondrial tRNA aminoacylation to impaired mitochondrial protein synthesis
  and respiratory-chain dysfunction.
- PMID:23918765 for YARS2/PUS1 sequencing as a diagnostic strategy, severe
  myopathy with respiratory failure requiring ventilatory support, and
  supportive clinical management.
- PMID:25037980 for MT-ATP6-associated MLASA plus syndrome, including complex V
  dysfunction and impaired oligomycin-sensitive respiration.
- PMID:28395030 for the broader YARS2 clinical cohort, elevated lactate,
  generalized myopathy, sideroblastic anemia, COX deficiency, and surveillance
  recommendations.
- PMID:30026338 for the YARS2 phenotypic spectrum, YARS2 enzymatic function,
  ringed sideroblast pathology, ragged-red fiber myopathy, and pyridoxine
  treatment nonresponse.

## Curation Conclusions

The curated graph models MLASA as genetically heterogeneous mitochondrial
disease involving PUS1, YARS2, and MT-ATP6. PUS1 deficiency disrupts
mitochondrial tRNA pseudouridylation, YARS2 deficiency disrupts mitochondrial
tyrosyl-tRNA aminoacylation, and MT-ATP6 variation impairs ATP synthase complex
V. These upstream defects converge on impaired mitochondrial translation and
respiratory-chain dysfunction, supporting the clinical triad of mitochondrial
myopathy, lactic acidosis, and sideroblastic anemia. The entry also records
ORPHA-supported dysmorphic, skeletal, neurologic, endocrine, ocular,
cardiorespiratory, biochemical, diagnostic, histopathologic, and supportive
management features where exact cached snippets support them.
