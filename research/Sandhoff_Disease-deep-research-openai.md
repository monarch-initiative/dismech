---
provider: openai
model: codex-local-synthesis
cached: true
start_time: '2026-04-14T23:30:00Z'
end_time: '2026-04-14T23:40:00Z'
duration_seconds: 600.0
template_file: codex_supplement_local
template_variables:
  disease_name: Sandhoff Disease
  category: Mendelian
citation_count: 10
source_providers:
- pubmed
- clingen
- mondo
---

## Question

Cross-check note for Sandhoff disease against MONDO / Monarch structure, ClinGen
gene validity framing, and exact-PMID evidence coverage.

## Output

### MONDO / Monarch checks
- MONDO:0010006 label matches Sandhoff disease.
- MONDO:0010006 is a child of GM2 gangliosidosis (MONDO:0017720).
- MONDO:0010100 Tay-Sachs disease remains a separate sibling branch.
- MONDO child terms exist for Sandhoff disease, infantile / juvenile / adult forms.

### ClinGen checks
- ClinGen validity row maps HEXB to Sandhoff disease (MONDO:0010006).
- ClinGen mode of inheritance is autosomal recessive.
- ClinGen classification is Definitive.

### Evidence coverage checks
- Human Sandhoff abstracts used for inheritance, HEXB framing, and phenotype anchors.
- Model-organism abstracts used for lysosomal dysfunction, gliosis, ER stress, and therapy nodes.
- GM2-branch reviews / natural history were kept only where the abstract language applied to Sandhoff explicitly or stated no Tay Sachs versus Sandhoff difference.

### Citation inventory
- PMID:22025593
- PMID:28553389
- PMID:28575132
- PMID:29325092
- PMID:29618308
- PMID:31140649
- PMID:31357902
- PMID:31919734
- PMID:39530163
- PMID:40266357
