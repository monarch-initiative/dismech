# Research plan: Chronic Traumatic Encephalopathy (MONDO:0043512)

## Interpretation
The target is chronic traumatic encephalopathy (CTE), the acquired neurodegenerative tauopathy associated with
repetitive head impacts (RHI). The template lists no causal gene and no OMIM entry; CTE is not a Mendelian disease,
so the "causal gene" is recorded as *none* — the cause is environmental (repetitive head impact exposure), with
genetic *modifiers/susceptibility* (e.g., APOE, TMEM106B) and the central protein being MAPT-encoded tau
(hyperphosphorylated, aggregated; not mutated). Template sections on Mendelian genetics (penetrance, anticipation,
carrier frequency, etc.) will be answered as "not applicable" with explanation. The report follows the 15 template
sections, plus Open Questions and References. Ontology CURIEs only where looked up (via an ontology-lookup retriever
and spot checks).

## Sub-questions and likely sources
1. **Definition, nomenclature, identifiers, history** — what CTE is, synonyms (dementia pugilistica, punch-drunk
   syndrome, traumatic encephalopathy syndrome as clinical counterpart), MONDO/MeSH/ICD codes, NINDS/NIBIB consensus
   neuropathological criteria (2016, 2021). Sources: MONDO/OLS, MeSH, ICD-10/11 browsers, consensus papers (PubMed).
2. **Etiology and environmental risk factors** — RHI as necessary exposure, dose–response (years of play, cumulative
   head impact index), sport/position, age at first exposure, military blast, IPV, single TBI question, causality
   (Bradford Hill) debate. Sources: cohort/brain-bank studies (Mez 2017/2020, Nowinski 2022), reviews.
3. **Genetic risk/modifiers and epigenetics** — APOE ε4, TMEM106B rs3173615, MAPT H1, GRN, GWAS, polygenic, DNA
   methylation/epigenetic aging. Sources: PubMed association studies, GWAS Catalog.
4. **Neuropathology, staging and anatomy** — pathognomonic lesion (perivascular p-tau in neurons ± astrocytes at sulcal
   depths), McKee stages I–IV, TDP-43, Aβ, α-synuclein co-pathology, white matter, CSP, regions affected, cell types.
   Sources: McKee 2013 Brain, consensus papers, Bieniek, neuropathology reviews.
5. **Molecular/cellular mechanisms and omics** — tau isoforms (3R/4R), cryo-EM CTE tau fold, neuroinflammation
   (microglia, CD68, CCL11), vascular/BBB injury, axonal injury, transcriptomics, proteomics, single-nucleus RNA-seq,
   somatic mutation/DNA damage studies. Sources: Nature/Acta Neuropathol primary papers.
6. **Clinical phenotype and natural history** — TES 2021 criteria, symptom domains and frequencies, mood/behavior vs
   cognitive presentation, parkinsonism, suicidality, age of onset, progression, dementia. Sources: Stern 2013, Mez 2017
   JAMA, Katz 2021, UNITE cohort studies.
7. **Diagnosis and biomarkers** — in-vivo diagnosis impossible definitively; tau PET (flortaucipir, PI-2620),
   MRI (CSP, atrophy, white matter), CSF/plasma p-tau/NfL/GFAP, EEG, DIAGNOSE CTE project, differential diagnosis (AD,
   FTD, PSP, PART, ARTAG). Sources: PubMed primary studies.
8. **Epidemiology and demographics** — prevalence in brain banks (convenience vs community series), general population
   estimates, female cases, sex ratio, age distribution, geographic/sport distribution. Sources: Bieniek 2015/2020,
   Mez 2017, Suter, Australian Sports Brain Bank, population studies.
9. **Prognosis, mortality, quality of life** — survival, age at death, cause of death (suicide, neurodegenerative),
   disability, QoL in former athletes. Sources: cohort studies, NFL mortality studies.
10. **Treatment and prevention** — no disease-modifying treatment; symptomatic management; trials (NCT IDs);
    prevention via exposure reduction (rule changes, heading restrictions, tackle football age), policy statements
    (CDC/NIH causal acknowledgement). Sources: ClinicalTrials.gov, reviews, policy statements.
11. **Animal models and other species** — rodent rmTBI, CHIMERA, blast, closed-head impact in mice/rats, Drosophila,
    pigs, iPSC/organoid models; recapitulation and limits; naturally occurring head impact animals (bighorn sheep,
    woodpeckers). Sources: PubMed model papers and reviews.
12. **Ontology terms** — look up MONDO, HP, GO, CL, UBERON, CHEBI, NCIT, NCBITaxon, HGNC IDs for concepts in the report
    via EBI OLS / HGNC; save as an evidence file.

## Execution notes
- Round 1: 12 retrievers (one per sub-question above), all completed.
- Round 2 (gap-filling): ontology supplement lookups; full-text clinical frequencies (Mez 2017 Table 3, Stern 2013, McKee 2013/2023, Montenigro 2014); symptomatic-treatment, tau-antibody trial and female-case evidence.
- Identifier finding: MONDO:0043512 = "traumatic encephalopathy" (generic); CTE = MONDO:0019976. The report covers CTE and flags this.
- Citation checks: `tools/check.py` (strict substring match of every quote against the cited evidence file; every cited identifier present in an evidence file's identifiers).
