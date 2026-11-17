# Research Plan — Marfan syndrome (MONDO:0007947; FBN1; OMIM:154700)

## Interpretation

The request is a knowledge-base style disease characterisation of **Marfan syndrome (MFS)**, the
autosomal dominant connective tissue disorder caused by heterozygous pathogenic variants in
**FBN1** (fibrillin-1, chromosome 15q21). The identifiers (MONDO:0007947, OMIM:154700, FBN1) are
followed strictly; related but distinct entities (Loeys–Dietz syndrome / TGFBR1/2, MASS phenotype,
isolated ectopia lentis, Weill–Marchesani, "Marfan syndrome type 2" historically mapped to TGFBR2,
neonatal MFS as a severe FBN1 sub-form) are mentioned only as differentials or allelic disorders.
The report follows the 15 requested sections of the template (rather than a free-form review),
with the Mechanism section opening as a numbered causal chain, ontology CURIEs only where looked
up by a retriever and recorded in an evidence file, and ending with `## Open Questions` and
`## References`. Where a template item does not apply (e.g., infectious agents, vaccines, repeat
expansion testing), this is stated explicitly.

## Sub-questions and likely sources

1. **Disease definition, identifiers, synonyms, epidemiology** — overview, OMIM/Orphanet/ICD-10
   (Q87.4)/ICD-11/MeSH/MONDO IDs; prevalence, incidence, sex ratio, geography, de novo fraction.
   *Sources:* OMIM, Orphanet, GeneReviews (NBK1335), MedlinePlus Genetics, population registry
   studies (Danish, Taiwanese, UK), PubMed.
2. **FBN1 genetics and variant spectrum** — gene/protein facts (HGNC, location, cbEGF domains),
   variant types (missense cysteine, truncating, splice, deletions), ACMG/ClinGen FBN1 rules,
   genotype–phenotype (dominant-negative vs haploinsufficiency), penetrance, expressivity,
   de novo/mosaicism, modifiers, founder effects, allelic disorders, epigenetics.
   *Sources:* ClinVar, ClinGen VCEP, UMD-FBN1, genotype–phenotype cohorts, PubMed.
3. **Pathophysiology/mechanism** — microfibril biology, TGF-β sequestration and signalling
   (canonical SMAD2/3 and non-canonical ERK), angiotensin II/AT1R, SMC mechanosensing, NO/eNOS,
   inflammation, MMPs, transcriptomics/single-cell/proteomics.
   *Sources:* landmark mouse papers (Neptune 2003, Habashi 2006/2011, Holm 2011), single-cell
   aortic studies, reviews.
4. **Cardiovascular phenotype and natural history** — aortic root dilatation, dissection,
   mitral valve prolapse, arrhythmia, cardiomyopathy; neonatal MFS; growth rates; age at events.
   *Sources:* cohort studies, GenTAC/registries, PubMed.
5. **Ocular, skeletal, pulmonary, skin, dural and other phenotypes; frequencies; QoL** —
   ectopia lentis, myopia, retinal detachment, pectus, scoliosis, arachnodactyly, dural ectasia,
   pneumothorax, striae; frequencies; quality of life studies.
   *Sources:* clinical series, HPO/OMIM annotations, SF-36 studies.
6. **Diagnosis** — revised Ghent nosology (Loeys 2010), systemic score, genetic testing
   approach (panels/WES), imaging (echo, CT/MRI), differential diagnosis, prenatal/PGT.
   *Sources:* Loeys 2010 (PMID 20591885), GeneReviews, guidelines (ACC/AHA 2022, ESC 2024).
7. **Medical therapy** — beta-blockers, losartan/irbesartan trials (Pediatric Heart Network,
   COMPARE, AIMS, Ghent), meta-analyses (MFS Trialists 2022), NCT IDs, adverse effects,
   pharmacogenomics.
   *Sources:* RCTs, Cochrane/meta-analyses, ClinicalTrials.gov.
8. **Surgery, pregnancy, lifestyle, prevention, counseling** — prophylactic aortic root
   replacement thresholds, valve-sparing vs composite grafts, pregnancy risk, exercise/sport
   guidance, fluoroquinolone/stimulant avoidance, genetic counseling, cascade screening, PGT.
   *Sources:* guidelines, surgical cohorts, pregnancy series.
9. **Prognosis, mortality, life expectancy, morbidity** — historic (Murdoch 1972) vs modern
   survival, causes of death, registry mortality, prognostic factors.
   *Sources:* Murdoch 1972, Silverman 1995, Danish/national registry studies.
10. **Animal models and other species** — mouse models (mgΔ, mgR, C1039G/+, GT-8, mgΔloxPneo),
    pig, rabbit, zebrafish, C. elegans/Drosophila absence; iPSC/organoid models; naturally
    occurring MFS-like disease in cattle (Limousin/Japanese Black), dogs, OMIA.
    *Sources:* MGI, OMIA, PubMed.
11. **Ontology term lookup (HPO)** — HP IDs and exact labels for all major phenotypes.
    *Sources:* HPO (hpo.jax.org), OLS/EBI.
12. **Ontology term lookup (MONDO, HGNC, GO, CL, UBERON, CHEBI, NCIT, NCBITaxon)** — exact IDs
    and labels for disease, gene, processes, cell types, anatomy, drugs, interventions, species.
    *Sources:* OLS/EBI, HGNC, NCBI Taxonomy, NCIt browser.

## Process

Retrieve: one workflow run, one retriever per sub-question, evidence saved to
`/mnt/session/outputs/citations/`. Failed retrievers are listed as not covered. A second, smaller
run will fill gaps. Write: `REPORT.md` built only from evidence files, quotes checked with `grep -F`.

## Status

- Round 1 (12 retrievers): all sub-questions covered; 185 evidence files.
- Round 2 (5 retrievers, gap-filling): guideline thresholds (2022 ACC/AHA, 2024 ESC, 2025 ESC pregnancy, 2020 ESC sports), mechanism gaps (epigenetics, inflammation, oxidative stress, LTBP/BMP binding, circulating TGF-β, human SMC transcriptomics), population/sex/exercise data, differentials and ocular/skeletal cohorts, and additional ontology lookups. No retriever failed.
- Remaining gaps (stated in REPORT.md): FBN1 gnomAD constraint values, founder variants, paternal-age effect, MFS-specific metabolomics, human aortic methylome.
