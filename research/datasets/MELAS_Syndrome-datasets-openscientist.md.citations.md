# Citations for Research Query

**Query:** # Public Dataset Discovery Research Template

## Target Disease

- **Disease:** MELAS Syndrome
- **MONDO:** MONDO:0010789
- **Category:** Mendelian

## Research Objective

Identify **publicly available datasets** that are directly relevant to the
pathophysiology of **MELAS Syndrome**. The output will be reconciled against a
disease-mechanism knowledge base whose `datasets` records carry a repository
accession, a data type, the organism, the sample count, and the linked
publication.

This is a **retrieval task, not a synthesis task**. Report only datasets you can
point to by accession in a real public repository. A short, accurate list is far
more valuable than a long, uncertain one.

---

## Absolute requirements

1. **Every dataset MUST have a real repository accession.** Give it in the exact
   form the repository uses: `GSE67472`, `E-MTAB-2770`, `PXD000001`,
   `phs000424`, `MTBLS123`, `PRJNA290729`, `SRP123456`, `EGAS00001000123`,
   `OSD-737`, `MSV000078618`, `MGYS00005566`.
2. **Never invent or guess an accession.** Every accession in this report will be
   resolved against the repository's API (NCBI E-utilities, EBI BioStudies,
   PRIDE, MetaboLights, EGA, NASA OSDR). Anything that does not resolve is
   discarded and counts against the report.
3. **Do not extrapolate an accession from a pattern.** If you recall that a paper
   deposited data but cannot recall the accession, say so in prose instead of
   producing a plausible-looking number. `GSE` followed by digits you are not
   certain about is the single most damaging thing this report can contain.
4. **Reproduce the repository's own title verbatim** where you can. Do not
   paraphrase a dataset title into something tidier.
5. **Do not substitute a sibling disease.** MELAS Syndrome may share most of its
   name with a *different* disease that is far better represented in public
   data — acquired vs hereditary angioedema, acquired vs familial partial
   lipodystrophy, juvenile vs adult forms, primary vs secondary forms. A
   dataset about the sibling is not a dataset about this disease, however
   close the wording. If the only data you can find is for the sibling, say
   that in prose and give no accession for it.
6. **If you find nothing, say so.** "No public omics dataset specific to this
   disease was found" is a correct and useful answer for a rare disease. An
   empty result is strongly preferred over a fabricated one.

## Scope

Prefer, in this order:

1. Datasets generated **from patients with MELAS Syndrome** (primary tissue,
   blood, biopsy, post-mortem, patient-derived cells).
2. Datasets from **disease-relevant model systems** — patient-derived iPSC lines,
   organoids, knock-in/knockout animal models of the causal gene, and cell-line
   perturbations of the causal gene.
3. Large **reference / consortium resources** that contain a usable
   MELAS Syndrome stratum (GTEx, TCGA, ENCODE, UK Biobank, GWAS Catalog,
   All of Us, dbGaP, cellxgene, HCA, MorPhiC), only when the disease-relevant
   subset is clearly identifiable.

Exclude: datasets about a different disease that merely mention this one;
review articles; datasets with no accession; supplementary tables that were never
deposited in a repository.

## Repositories to search

- **NCBI GEO** (`GSE…`) — transcriptomics, microarray, methylation, ChIP-seq, ATAC-seq
- **NCBI SRA / BioProject** (`SRP…`, `PRJNA…`) — raw sequencing, metagenomics
- **dbGaP** (`phs…`) — controlled-access human genomic + phenotype data
- **EBI ArrayExpress / BioStudies** (`E-MTAB-…`) — expression, imaging
- **EBI PRIDE** (`PXD…`) — proteomics
- **EBI MetaboLights** (`MTBLS…`) — metabolomics
- **EGA** (`EGAS…`, `EGAD…`) — controlled-access European genomic data
- **MassIVE** (`MSV…`) — proteomics
- **MGnify** (`MGYS…`) — metagenomics
- **NASA OSDR** (`OSD-…`) — spaceflight/microgravity omics
- **cellxgene / Human Cell Atlas** — single-cell
- **GWAS Catalog** (`GCST…`) — GWAS summary statistics

---

## Required output format

For **each** dataset, emit exactly this block. Omit a field only if the
information genuinely is not available; do not fill it with a guess.

```
### <ACCESSION>

- **Repository:** <GEO | SRA | BioProject | dbGaP | ArrayExpress | PRIDE | MetaboLights | EGA | MassIVE | MGnify | OSDR | cellxgene | GWAS Catalog>
- **Title:** <the repository's own title, verbatim>
- **Data type:** <MICROARRAY | BULK_RNA_SEQ | SINGLE_CELL_RNA_SEQ | SPATIAL_TRANSCRIPTOMICS | METHYLATION | CHIP_SEQ | ATAC_SEQ | PROTEOMICS | METABOLOMICS | GWAS | WGS | WES | MULTI_OMICS | PHENOPACKETS | VARIANT_DATABASE>
- **Organism:** <e.g. Homo sapiens, Mus musculus>
- **Sample count:** <integer, or "unknown">
- **Sample types:** <tissue and/or cell type profiled>
- **Conditions:** <the disease/control groups or experimental arms>
- **Publication:** <PMID:######## of the paper reporting the dataset, if any>
- **Mechanistic relevance:** <2-3 sentences: which specific pathophysiological
  step of MELAS Syndrome this dataset speaks to, and what was found. Tie it to
  mechanism, not just to the disease name.>
- **Confidence in accession:** <HIGH: I am certain this accession is correct |
  MEDIUM: the dataset exists but verify the accession | LOW: do not use without
  checking>
```

## Then, a short closing section

### Coverage assessment

- Which aspects of MELAS Syndrome pathophysiology **are** well covered by public
  data, and which are **not** (name the gap explicitly).
- If the disease is rare and has little or no deposited data, state that plainly
  and note the closest available proxy (e.g. data on the causal gene in another
  context, or on a mechanistically related disorder).

### Datasets you believe exist but could not pin down

List these **in prose, without accessions**. This section exists so you never
have to invent an accession to avoid an empty answer.

**Provider:** openscientist
**Generated:** 2026-08-26T03:34:46.440533

1. PMID:15728662
2. PMID:21708074
3. PMID:23894440
4. PMID:37289546
5. PMID:26176921
6. PMID:31641105
7. PMID:34329596
8. PMID:30962477
9. PMID:35884972
10. PMID:28139706
11. PMID:34982085