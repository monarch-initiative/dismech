---
provider: cyberian-codex
model: codex-local-synthesis
cached: true
start_time: '2026-05-03T11:03:39Z'
end_time: '2026-05-03T11:03:39Z'
duration_seconds: 0.0
template_file: codex_supplement_local
template_variables:
  disease_name: 5-Oxoprolinase Deficiency
  mondo_id: MONDO:0009825
  category: Mendelian
citation_count: 7
source_providers:
- codex-local-literature
provider_attempts:
- falcon: attempted; no artifact produced before cancellation after prolonged stall
- openai: attempted; no artifact produced before cancellation after prolonged stall
- cyberian-codex: attempted; no artifact produced before termination after prolonged stall
---

## Question

Pathophysiology and clinical mechanisms of 5-oxoprolinase deficiency, emphasizing
direct Orphanet/MONDO mapping, OPLAH genetics, gamma-glutamyl-cycle biochemistry,
clinical penetrance, and treatment-relevant mechanisms.

## Output

### Evidence Basis

This local Codex synthesis uses the cached Orphanet record for ORPHA:33572 and
the PubMed references integrated into the YAML. The Asta retrieval attempt for
this disease returned off-topic literature and was not used.

### Core Disease Mechanism

- 5-oxoprolinase deficiency maps directly to MONDO:0009825 and ORPHA:33572.
- Orphanet lists OPLAH as the disease-causing gene and records autosomal
  recessive inheritance.
- OPLAH encodes ATP-dependent 5-oxoprolinase, a gamma-glutamyl-cycle enzyme.
  Biallelic OPLAH variants reduce 5-oxoprolinase activity and impair clearance
  of 5-oxo-L-proline, also called pyroglutamic acid.
- The most consistent disease feature is persistent urinary 5-oxoproline
  elevation, represented in HPO as increased urinary L-pyroglutamic acid.

### Clinical Interpretation

- Published molecular reports support a rare biochemical disorder with
  variable clinical expression. Earlier series described benign or uncertain
  clinical impact in some families, while later case reports and Orphanet
  phenotypes include developmental delay, delayed speech, seizures, metabolic
  acidosis, and brain imaging abnormalities.
- The YAML therefore treats neurologic and metabolic manifestations cautiously:
  the biochemical phenotype is high-confidence, while clinical penetrance and
  causality are supported at variable or case-level strength.

### YAML Integration Notes

- The primary pathophysiology chain is OPLAH molecular-function deficiency to
  gamma-glutamyl-cycle block to 5-oxoproline accumulation.
- Genetic evidence uses biallelic OPLAH mutation series and first molecular
  report evidence.
- Phenotypes are anchored to Orphanet frequency statements and reinforced only
  where PubMed evidence supports the same clinical or biochemical feature.

### Citation Inventory

- PMID:17397529
- PMID:21651516
- PMID:25129617
- PMID:25851806
- PMID:27477828
- PMID:39129838
- ORPHA:33572
