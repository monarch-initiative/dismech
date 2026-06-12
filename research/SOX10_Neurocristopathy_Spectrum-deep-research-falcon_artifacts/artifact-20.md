```markdown
A comprehensive PMID-cited report on **SOX10 Neurocristopathy Spectrum** could not be produced in this session because no citable literature contexts were retrieved.

Session outcome:
- `paper_search`: 0 results across repeated SOX10/Waardenburg/Hirschsprung/PCWH queries
- `open_targets_search`: failed after retries
- `clinical_trials_search`: no relevant trials retrieved
- Result: no usable context IDs, so PMID-backed claims, abstract quotes, source-linked dates, and evidence-grounded synthesis were not possible

Artifacts prepared for rerun:
- **Retrieval log**: documents failed searches and zero-result pattern
- **Source directory**: lists authoritative databases/resources and what to extract from each
- **Report template**: full placeholder structure for all requested disease-characteristics sections
- **Rerun plan**: minimal workflow for rebuilding the report once retrieval is restored

Generic source URL patterns to use next:
- OMIM: `https://www.omim.org/search?search=SOX10`
- Orphanet: `https://www.orpha.net/en/disease/search?query=SOX10`
- PubMed: `https://pubmed.ncbi.nlm.nih.gov/?term=SOX10+Waardenburg+Hirschsprung`
- ClinVar: `https://www.ncbi.nlm.nih.gov/clinvar/?term=SOX10%5Bgene%5D`
- ClinGen: `https://search.clinicalgenome.org/kb/genes/HGNC:11190`
- gnomAD: `https://gnomad.broadinstitute.org/`
- GeneReviews: `https://www.ncbi.nlm.nih.gov/books/?term=SOX10+GeneReviews`
- DECIPHER: `https://www.deciphergenomics.org/search?q=SOX10`
- HPO: `https://hpo.jax.org/app/search/term?query=SOX10`
- ClinicalTrials.gov: `https://clinicaltrials.gov/search?term=SOX10`
- MGI: `https://www.informatics.jax.org/searchtool/Search.do?query=Sox10`
- ZFIN: `https://zfin.org/search?category=gene&q=sox10`

Minimal rerun workflow:
1. Re-run literature retrieval in a fresh session.
2. Start with broad queries: `SOX10 Waardenburg Hirschsprung`, `SOX10 PCWH syndrome`, `SOX10 genotype phenotype`, `SOX10 neural crest functional study`.
3. Retrieve at minimum: one recent review, foundational primary case-series papers, variant curation sources, and one diagnostic/management source.
4. Populate the disease report template section by section.
5. Generate the final report only after PMID-linked contexts are available.
```


*Code_block: This code block provides a concise user-facing explanation that no citable contexts were retrieved in the session, preventing a PMID-cited report. It also lists the fallback artifacts, authoritative source URL patterns, and a minimal rerun workflow.*
