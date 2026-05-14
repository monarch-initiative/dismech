# Fibrous Dysplasia Research Fallback

Deep-research provider attempts were bounded and did not produce usable output:

- `just research-disorder falcon Fibrous_Dysplasia` was terminated by the 120-second wrapper after provider silence.
- `just research-disorder openai Fibrous_Dysplasia` was terminated by the 60-second wrapper after provider silence.

Local curation proceeded from generated Orphanet and PubMed caches:

- ORPHA:249: structured record for fibrous dysplasia of bone, including definition, non-applicable inheritance, onset categories, unknown worldwide prevalence, exact MONDO mapping, and phenotype frequency rows.
- PMID:31037426: bench-to-bedside review covering GNAS mosaicism, bone/marrow replacement, FGF23 phosphate wasting, imaging diagnosis, supportive management, surgery, bisphosphonates, and denosumab research limitations.
- PMID:27492469: clinical/translational review covering somatic GNAS activation, histology, clinical manifestations, management, bisphosphonate limitations, and denosumab safety concerns.
- PMID:25033066: randomized placebo-controlled alendronate trial in polyostotic fibrous dysplasia.
- PMID:18489744: McCune-Albright syndrome review, already present in the repository cache and used as background reference provenance.

Scope note: no provider-generated synthesis was used. YAML claims are limited to cached Orphanet/PubMed snippets available locally.
