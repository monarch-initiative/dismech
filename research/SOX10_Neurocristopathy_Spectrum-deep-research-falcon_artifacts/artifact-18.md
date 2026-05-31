```markdown
## Evidence-Limited Session Report: SOX10 Neurocristopathy Spectrum

### Outcome
No citable literature contexts were retrieved in this session, so the requested comprehensive, well-cited research report could not be produced from the available tool outputs.

### What was attempted
- `paper_search`: multiple disease-, gene-, and phenotype-based queries were run, including:
  - `SOX10 neurocristopathy spectrum`
  - `SOX10 Waardenburg Hirschsprung`
  - `SOX10 PCWH syndrome`
  - `SOX10 leukodystrophy neuropathy`
  - `SOX10 Waardenburg syndrome type 4`
- `open_targets_search`: attempted for `SOX10` and related disease terms, but failed after retries.
- `clinical_trials_search`: attempted for `SOX10`, `Waardenburg`, and related terms; no relevant trials were returned.
- `patent_search`: attempted as a fallback translational evidence route; no relevant results were returned.

### Why the report could not be completed
- All literature searches returned zero retrievable papers in this session.
- No usable context IDs were produced.
- Without citable contexts, the system cannot support PMID-backed claims, source URLs tied to retrieved evidence, publication dates, abstract quotes, or evidence-grounded disease synthesis.
- Because no papers were retrieved, figure/table review via `view_images` was also not possible.

### What is available instead
The following session artifacts were prepared to support a rerun:
- **Retrieval log**: documents the failed searches and zero-result pattern.
- **Section-by-section checklist**: maps each disease-template section to the evidence sources needed.
- **Full report template**: a structured placeholder for disease information, phenotypes, genetics, mechanisms, diagnostics, treatment, prognosis, prevention, and models.
- **Minimum evidence table**: identifies the minimum authoritative sources needed to complete the report.
- **Source directory**: lists the main databases and generic URL patterns to use next.

### Prioritized authoritative resources to use next
1. **OMIM** — disease definitions, allelic variants, inheritance, phenotype series
   URL pattern: `https://www.omim.org/search?search=SOX10`
2. **Orphanet** — rare disease classification, epidemiology, synonyms, inheritance
   URL pattern: `https://www.orpha.net/en/disease/search?query=SOX10`
3. **PubMed** — primary case reports, cohort studies, reviews, mechanistic papers
   URL pattern: `https://pubmed.ncbi.nlm.nih.gov/?term=SOX10+Waardenburg+Hirschsprung`
4. **GeneReviews** — diagnosis, management, surveillance, genetic counseling
   URL pattern: `https://www.ncbi.nlm.nih.gov/books/?term=SOX10+GeneReviews`
5. **ClinVar** — variant classifications and condition-linked assertions
   URL pattern: `https://www.ncbi.nlm.nih.gov/clinvar/?term=SOX10%5Bgene%5D`
6. **ClinGen** — gene–disease validity and dosage/curation resources
   URL pattern: `https://search.clinicalgenome.org/kb/genes/HGNC:11190`
7. **gnomAD** — allele frequencies and constraint data
   URL pattern: `https://gnomad.broadinstitute.org/`
8. **DECIPHER** — CNVs and phenotype-linked structural variant data
   URL pattern: `https://www.deciphergenomics.org/search?q=SOX10`
9. **HPO** — phenotype ontology mapping
   URL pattern: `https://hpo.jax.org/app/search/term?query=SOX10`
10. **ClinicalTrials.gov** — any disease-specific or supportive-management studies
    URL pattern: `https://clinicaltrials.gov/search?term=SOX10`
11. **MGI / ZFIN** — mouse and zebrafish model evidence
    URL patterns: `https://www.informatics.jax.org/searchtool/Search.do?query=Sox10` and `https://zfin.org/search?category=gene&q=sox10`

### Minimal rerun plan
1. Re-run literature retrieval in a fresh session.
2. Start with broad queries, then narrow:
   - `SOX10 Waardenburg Hirschsprung`
   - `SOX10 PCWH syndrome`
   - `SOX10 genotype phenotype`
   - `SOX10 neural crest functional study`
3. Retrieve at least:
   - one recent review,
   - two foundational primary case-series papers,
   - variant curation sources,
   - one management/guideline source.
4. Populate the disease report template section by section.
5. Only after citable contexts are available, generate the final comprehensive report with PMIDs, URLs, publication dates, abstract quotes, and ontology mappings.

### Practical note
Until citable contexts are retrievable, any disease summary would fall short of the requested evidence standard and should be treated as incomplete.
```


*Code_block: This artifact provides a concise user-facing report explaining that no citable literature contexts were retrieved for SOX10 Neurocristopathy Spectrum in this session. It also summarizes the failed retrieval attempts, lists fallback deliverables, and gives a prioritized rerun plan with authoritative resource URLs.*
