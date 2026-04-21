---
provider: cyberian-codex
model: codex-local-synthesis
cached: true
start_time: '2026-04-14T23:20:00Z'
end_time: '2026-04-14T23:30:00Z'
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

Codex local deep-research synthesis for demo-ready Sandhoff disease curation.

## Output

### Disease framing
- Anchor Sandhoff disease to MONDO:0010006.
- Make the parent relationship to GM2 gangliosidosis (MONDO:0017720) explicit.
- Keep Tay-Sachs disease (MONDO:0010100) as a sibling differential, not a synonym.
- Keep the gene-disease frame ClinGen-consistent: HEXB, autosomal recessive, definitive.

### Causal graph requirements
- Start from pathogenic HEXB variants and loss of Hex A / Hex B activity.
- Pass through lysosomal GM2 and GA2 storage and explicit lysosomal dysfunction.
- Keep neural-cell and glial pathology explicit before the terminal neurodegeneration node.
- Use only exact PMID-backed snippets in YAML evidence.

### Key mechanistic nodes selected
- Pathogenic HEXB variants
- Hexosaminidase A and B deficiency
- Lysosomal GM2 and GA2 accumulation in neural cells
- Lysosomal dysfunction in neurons and glia
- Neuroinflammation and reactive gliosis
- ER stress and spinal motor neuron apoptosis
- Neurodegeneration and circuit dysfunction

### Clinical and treatment emphasis
- Preserve Sandhoff-specific phenotype anchors such as coarse facies and infantile Sandhoff wording where available.
- Use infantile GM2 natural-history data only where the abstract explicitly states Tay Sachs and Sandhoff variants did not differ.
- Keep supportive care as current standard, with gene therapy and 4-PBA labeled preclinical / investigational.

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
