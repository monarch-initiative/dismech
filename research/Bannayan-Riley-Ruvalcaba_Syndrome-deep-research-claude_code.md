---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-03T20:06:06.013349'
end_time: '2026-08-03T20:22:44.443204'
duration_seconds: 998.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bannayan-Riley-Ruvalcaba Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 27
  num_turns: 53
  total_cost_usd: 4.525166499999999
  session_id: aab5de24-e43c-4d30-a6cd-74613ed1c693
  stop_reason: end_turn
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bannayan-Riley-Ruvalcaba Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bannayan-Riley-Ruvalcaba Syndrome** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Bannayan–Riley–Ruvalcaba Syndrome (BRRS) — Comprehensive Research Report

**Prepared:** 2026-08-03 · **Target:** `kb/disorders/Bannayan-Riley-Ruvalcaba_Syndrome.yaml` · **Category:** Mendelian (autosomal dominant, tumor-predisposition / overgrowth)

---

## ⚠️ Curator preflight — read this before you copy anything into YAML

Three things will bite you on this entry, so let's get them out of the way first.

**1. Named Entity Confusion risk here is HIGH.** BRRS is a triple eponym collision that got merged in the early 1990s — Bannayan–Zonana syndrome, Riley–Smith syndrome, and Ruvalcaba–Myhre–Smith syndrome were three separately-named conditions that turned out to be one thing. Several databases (NORD included) still file it under `ruvalcaba-syndrome`. Adjacent traps: **Riley–Day syndrome** (familial dysautonomia, `IKBKAP`/`ELP1` — completely unrelated), **Ruvalcaba syndrome** (a distinct skeletal-dysplasia eponym), and **Cowden syndrome** (`MONDO:0016063`, `OMIM:158350`), which is the same gene and arguably the same disease but a *different KB entity*. A deep-research report on "Bannayan syndrome" that talks mostly about breast/thyroid cancer surveillance in adults has probably drifted into Cowden. Run `just preflight-dr <report> MONDO:0007924` and expect the canonical gene to be **PTEN**.

**2. Every ontology ID below is a *candidate*.** My local OAK install in this worktree is broken (the Python 3.14 `pyhornedowl` failure), so I could not verify a single HP/GO/CL/UBERON/CHEBI/NCIT identifier against the authority. Treat the term tables as leads and run `just validate-terms` before committing. I've flagged the ones I'm least sure about.

**3. Quotes marked "verbatim" came from the Europe PMC `abstractText` field**, which is the real abstract — but the reference validator is the arbiter, not me. Run `just fetch-reference PMID:xxxxx` then `just validate-references` for each one. Two abstracts I could *not* retrieve (Marsh 1997 Nat Genet is a letter with **no abstract at all**; Parisi 2001 has no `abstractText` in Europe PMC) — do not invent snippets for those.

---

## 1. Disease Information

### Overview

Bannayan–Riley–Ruvalcaba syndrome is a rare congenital overgrowth and hamartoma disorder, present from birth, defined by the combination of **macrocephaly**, **hamartomatous intestinal polyposis**, **lipomas**, **vascular malformations**, and **pigmented macules of the glans penis** (genital lentiginosis), frequently with developmental delay and/or autism spectrum disorder. It is one of the historical clinical presentations now unified under the molecular umbrella of **PTEN hamartoma tumor syndrome (PHTS)**.

The single most consequential fact for a knowledge base: **BRRS and Cowden syndrome are, mechanistically, the same disease**. Marsh et al. established this in 1999 and Lachlan et al. confirmed it clinically in 2007; GeneReviews now states flatly that the historical phenotypes "represent a unified disease spectrum under the PHTS designation" and that PHTS has no clinical diagnostic criteria of its own — molecular confirmation of a germline *PTEN* variant is the diagnosis.

> **Verbatim (PMID:10400993, Marsh et al. 1999, *Hum Mol Genet* 8:1461–72):** "Thus, PTEN mutation-positive CS and BRR may be different presentations of a single syndrome and, hence, both should receive equal attention with respect to cancer surveillance."

BRRS is best understood as the **pediatric-onset end** of the PHTS spectrum (overgrowth, lipomas, polyps, neurodevelopment) and Cowden syndrome as the **adult-onset end** (mucocutaneous lesions, breast/thyroid/endometrial cancer), with the same gene and age-related penetrance connecting them.

### Identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0007924` | Verified against EBI OLS4; label "Bannayan-Riley-Ruvalcaba syndrome"; not obsolete |
| **OMIM** | `153480` | Formerly "Bannayan-Zonana syndrome" / "Ruvalcaba-Myhre-Smith syndrome" |
| **Orphanet** | `ORPHA:109` | |
| **UMLS** | `C0265326` | |
| **MedGen** | `78554` | |
| **DOID** | `DOID:0050657` | |
| **NCIT** | `NCIT:C3939` | |
| **SNOMED CT** | `21984008` | |
| **ICD-9** | `759.6` | |
| **ICD-10-CM** | MONDO xref says `E71.440` — ⚠️ **suspicious**; most clinical sources use `Q85.8` (other phakomatoses, NEC). Verify before curating. |
| **ICD-11** | MONDO carries foundation ID `357383447`; the practical stem code is in the LD2x hamartoma-syndrome block. Verify. |
| **Gene (HGNC)** | `hgnc:9588` (PTEN); OMIM `*601728`; UniProt `P60484` |

### Synonyms and alternative names

From the MONDO record: **BRRS**, Bannayan syndrome, **Bannayan–Zonana syndrome (BZS)**, Riley–Smith syndrome, **Myhre–Riley–Smith syndrome**, **Ruvalcaba–Myhre–Smith syndrome (RMSS)**, "macrocephaly with multiple lipomas and hemangiomas." Also encountered: *macrocephaly–multiple lipomas–hemangiomata syndrome*, *Bannayan–Ruvalcaba–Riley syndrome*.

### Nature of the evidence base

Overwhelmingly **aggregated disease-level and case-level literature**, not EHR-derived. The definitive BRRS-specific evidence is a 2024 systematic review of **83 published pediatric cases from 33 articles** (PMID:39256443) — all case reports and small series, which the authors explicitly flag as high risk of bias. The large quantitative datasets (cancer risk, GI phenotype) all come from **Cowden-ascertained PHTS cohorts** (Cleveland Clinic, Dutch/European registries) and must be attributed as PHTS-wide rather than BRRS-specific. A very recent unbiased population signal exists (All of Us / UK Biobank) but is still a **preprint** as of December 2025.

---

## 2. Etiology

### Primary cause

Heterozygous **germline loss-of-function variants in *PTEN*** (phosphatase and tensin homolog), at 10q23.31. *PTEN* is a haploinsufficient tumor suppressor; loss of its lipid-phosphatase activity releases the brake on PI3K–AKT–mTOR signaling.

**Detection rate in BRRS specifically:** ~60% in the classic ascertained series.

> **Verbatim (PMID:10400993):** "In this study, constitutive DNA samples from 43 BRR individuals comprising 16 sporadic and 27 familial cases, 11 of which were families with both CS and BRR, were screened for PTEN mutations. Mutations were identified in 26 of 43 (60%) BRR cases."

The 2024 pediatric systematic review reports a much higher rate — **75/83 (90%)** — but that reflects modern ascertainment (patients are increasingly *defined* by having the variant). The earlier Marsh 1998 series found 4/7 (57%) in Bannayan–Zonana families.

> **Verbatim (PMID:9467011, Marsh et al. 1998, *Hum Mol Genet* 7:507–15):** "Germline PTEN mutations were identified in four of seven (57%) BZS families studied. Interestingly, none of these mutations was observed in the PTPase core motif."

That last clause is a real, curatable genotype–phenotype observation: BRRS-associated variants were *not* found in the phosphatase core motif, whereas Cowden variants clustered there (43% of CD mutations in exon 5).

### Genetic risk factors beyond PTEN

**`TTN` (titin) — candidate second gene for PTEN-wildtype BRRS.** This is the most important non-PTEN finding and is BRRS-specific rather than Cowden-derived.

> **Verbatim (PMID:29263846, Yehia, Ni & Eng 2017, *npj Genom Med* 2:37):** "We exome-sequenced 35 unrelated *PTEN-*wildtype patients with classic presentation of BRRS and identified *TTN* germline missense variants in 12/35 (34%) patients... Rare *TTN* variants (MAF ≤ 0.0001) are enriched in classic BRRS patients compared to BRRS-like (OR = 2.7, 95% CI 1.21-5.94, *p* = 1.6 × 10⁻²) and multiple population controls (OR = 2.2, 95% CI 1.01-4.20, *p* = 4.7 × 10⁻²)."

Functional support: CRISPR-edited cells carrying the I-band variant p.Cys5096Arg showed "increased growth and lack of contact inhibition... associated with increased levels of or phosphorylation of focal adhesion kinase (FAK)." The authors propose BRRS may "join the growing list of Titinopathies." **Curation note:** this is a *candidate* gene — use `relationship_type: SUSCEPTIBILITY` or `MODIFIER`, not causal, and tag `evidence_source: IN_VITRO` for the FAK/CRISPR arm.

**Other PTEN-wildtype routes (established in Cowden-like, extrapolate cautiously to BRRS):**
- ***KLLN*/KILLIN germline promoter hypermethylation** — 37% of 123 PTEN-mutation-negative Cowden/Cowden-like patients; downregulates KILLIN ~250-fold with normal PTEN transcription (Bennett, Mester & Eng 2010, *JAMA* 304:2724–31, PMID:21177507). Associated with ~3-fold higher breast cancer and >2-fold higher renal cancer prevalence than germline *PTEN* variants. Assigned OMIM `#615107` (Cowden syndrome 4).
- ***SDHB*/*SDHD*** germline variants — 3 *SDHB* and 7 *SDHD* among 74 PTEN-negative Cowden-like individuals with elevated MnSOD (Ni et al. 2008, *Am J Hum Genet* 83:261–8, PMID:18678321).
- Additional unexpected cancer-predisposition gene variants in PTEN-wildtype CS/BRRS (Yehia et al. 2018, *PLoS Genet*).

### Environmental risk factors

**None established.** BRRS is a monogenic Mendelian disorder with no documented environmental cause, no infectious trigger, and no lifestyle risk factor for *the syndrome itself*. This is a legitimate "not applicable" for the KB — do not fabricate.

Downstream cancer risk in carriers plausibly interacts with generic exposures (UV for the ~6% melanoma risk; diagnostic radiation given the tumor predisposition), but I found no BRRS/PHTS-specific gene–environment interaction study. **Age is the dominant non-genetic modifier of expression** — penetrance is strongly age-related, which is the reason BRRS and Cowden look like different diseases at different life stages.

### Protective factors

No genetic protective variants or modifier alleles are documented. No dietary or lifestyle protective factor has been demonstrated. The only genuinely "protective" intervention is **surveillance-based early detection**, which is secondary prevention, not risk reduction.

### Gene–environment interactions

Not characterized for BRRS. **Report this as a knowledge gap** — a `discussions` entry with `kind: KNOWLEDGE_GAP` is the honest treatment.

---

## 3. Phenotypes

### BRRS-specific frequencies (best available source)

From the 2024 systematic review of 83 pediatric BRRS patients (PMID:39256443, Kapačinskaitė et al., *Sci Rep* 14, doi:10.1038/s41598-024-71991-2). **These are frequencies among published pediatric case reports — publication bias is severe, so use qualitative `FrequencyEnum` bands rather than curating the exact percentages as population frequencies.** Per `docs/frequency-evidence-guidelines.md`, the mapping below is my suggestion; when a number is soft, omit `frequency:` entirely.

| Phenotype | Reported frequency | Suggested `FrequencyEnum` | Candidate HP term (⚠️ verify) |
|---|---|---|---|
| Macrocephaly | **77%** (also 94% in PHTS overall per GeneReviews; often >5 SD above mean) | `VERY_FREQUENT` | `HP:0000256` Macrocephaly |
| Developmental disorders (DD/ASD) | **63%** | `FREQUENT` | `HP:0001263` Global developmental delay; `HP:0000717` Autism |
| Pigmented genital macules (males) | **75%** (21/28 males) | `VERY_FREQUENT` (males) | ⚠️ no confident HP term — search "penile freckling"/"lentigines"; fallback `HP:0007565` |
| Skin manifestations (any) | **64%** | `FREQUENT` | `HP:0000951` Abnormality of the skin |
| Lipomas | **>50%** (18/33) | `FREQUENT` | `HP:0012032` Lipoma |
| Gastrointestinal polyps | **48%** | `FREQUENT` | ⚠️ hamartomatous polyposis — verify `HP:0004390` vs `HP:0200008` |
| Thyroid changes | **36%** | `OCCASIONAL`–`FREQUENT` | `HP:0000820` Abnormal thyroid morphology |
| Hemangiomas | **24%** | `OCCASIONAL` | `HP:0001028` Hemangioma |
| Arteriovenous malformations | **18%** | `OCCASIONAL` | `HP:0100026` Arteriovenous malformation |

> **Verbatim (PMID:39256443):** "A total of 83 pediatric patients with BRRS were identified. The most common clinical findings were macrocephaly (77%) and developmental disorders (63%)."

**Demographics from the same review:** male predominance **60/83 (72%)** — almost certainly an ascertainment artifact, since genital lentiginosis is a male-only diagnostic clue; median age **8 years**; de novo variants in **up to 48%**.

### Additional features (established in the older literature, frequencies less firm)

Neonatal macrosomia / large birth weight; accelerated linear growth in early childhood; **muscular hypotonia and proximal myopathy** (a genuinely BRRS-flavored feature, sometimes with lipid storage on muscle biopsy); joint hyperextensibility; pectus excavatum; scoliosis; café-au-lait macules; frontal bossing and dolichocephaly; downslanting palpebral fissures; **Hashimoto thyroiditis** (Gorlin et al. 1992, *Am J Med Genet* 44:307–14, PMID:1336932 — expanded the BRRS phenotype to include Hashimoto thyroiditis, present in 7 of their cases); high-arched palate; enlarged perivascular Virchow–Robin spaces on brain MRI.

### Phenotype characteristics

- **Onset:** congenital / neonatal for macrocephaly and macrosomia; infancy–early childhood for lipomas, vascular anomalies, and developmental concerns; **peripubertal/adolescent (age ~10+)** for genital lentiginosis; **adult** for the epithelial cancers.
- **Severity:** highly variable, even within a single family carrying the identical variant. Lachlan et al. (2007, *J Med Genet* 44:579–85) concluded BRRS and CS are "one condition with variable expression and age-related penetrance" and argued it is "not helpful to split PTEN-related disorders into separate clinical syndromes."
- **Progression:** the overgrowth features are largely **stable/static** after early childhood (macrocephaly does not progress; some lipomas enlarge). The **tumor-predisposition component is progressive with age** — new lesions and malignancies accrue lifelong. Vascular anomalies (PTEN hamartoma of soft tissue) are typically **progressive and symptomatic**, presenting with pain and swelling.
- **Quality-of-life impact:** driven mostly by (a) neurodevelopment — intellectual disability, ASD, attention and processing-speed deficits; (b) pain and functional impairment from intramuscular vascular/soft-tissue hamartomas (one case in the Kurek series required **amputation**); (c) the psychological burden of lifelong cancer surveillance. I found **no BRRS-specific EQ-5D/SF-36/PROMIS data** — this is a real gap; the sirolimus vascular-anomaly experience reports "significant improvement in patient quality of life" without a validated instrument. Do not curate a QoL number.

### Neurodevelopmental detail

*PTEN* is now recognized as one of the commonest **monogenic causes of ASD with macrocephaly** (~10% of ASD-plus-macrocephaly cases). GeneReviews: neurodevelopmental disorders in ~**35%** of children with PHTS; **epilepsy 6–17%** vs ~1% general population. Frazier et al. 2015 (*Mol Psychiatry*, PMID:25288137) found PTEN-ASD specifically associated with prominent **white-matter abnormalities** and "strong reductions in processing speed and working memory," with white-matter abnormality mediating the relationship between PTEN protein level and full-scale IQ. A 2024 systematic review of PHTS neurology (Dhawan, Baitamouni, Liu & Eng, *Neurology* 103(7):e209844, **PMID:39250745**) screened 1,996 articles and included 90 — but 54% were case reports, so the neurological evidence base is thin.

---

## 4. Genetic / Molecular Information

### Causal gene

***PTEN***, 10q23.31, 9 exons, encoding a 403-amino-acid dual-specificity protein/lipid phosphatase. HGNC `hgnc:9588` (note this repo's lowercase-prefix convention). OMIM `*601728`. UniProt `P60484`. A processed pseudogene, ***PTENP1*** on chromosome 9, cross-amplifies during PCR and must be designed around — a practical testing caveat worth capturing.

### Variant spectrum

- **Types:** missense, nonsense, frameshift, splice-site, small indels, and whole-exon to whole-gene deletions. All classes are represented.
- **Exon 5 hotspot:** "Nearly 40%" of PHTS variants fall in exon 5, which encodes the **phosphatase (PTPase) core motif** (HCXXGXXR, residues ~123–130). Marsh 1998 found 13/30 (43%) of Cowden variants in exon 5, with 7/30 (23%) inside the core motif itself — and notably **none** of the Bannayan–Zonana variants in the core motif.
- **Recurrent variants:** `c.388C>T (p.Arg130Ter)`, `c.697C>T (p.Arg233Ter)`, `c.1003C>T (p.Arg335Ter)`. R233X was seen in two unrelated Cowden families *and* one BZS family in the Marsh 1998 series — direct evidence for allelism.
- **Detection method yield (GeneReviews):** coding-region sequencing ≤80%; deletion/duplication analysis 3–11%; **promoter-region sequencing ~10%** (do not skip the promoter).
- **Origin:** **germline** for the syndrome; **de novo in up to 48%** of BRRS cases per the 2024 review — so a negative family history is common and does not argue against the diagnosis. Somatic *PTEN* loss is separately one of the most frequent events in sporadic cancer (glioblastoma, endometrial, prostate) — mechanistically informative but **not** part of the BRRS entry.
- **Population frequency:** *PTEN* loss-of-function variants are extremely rare in gnomAD; the gene is strongly LoF-constrained. Recent unbiased biobank data suggest carriers are far commoner than the clinic-based estimate: an All of Us analysis found **55 P/LP carriers among 414,830 participants (~1 in 7,500)**, ~26-fold above historical estimates, with 43.5% having a cancer diagnosis (median age at first cancer 48 y). ⚠️ **This is a medRxiv preprint (PMID:41480035, Dec 2025) — cite as preliminary, `evidence_source: HUMAN_CLINICAL` but flag preprint status.** GeneReviews gives ~1 in 9,000 (All of Us) to 1 in 13,000 (UK Biobank).
- **Functional consequence:** **loss of function / haploinsufficiency** is the dominant mechanism. Some missense alleles act as **dominant negatives** (the PTEN dimer means a catalytically dead monomer can poison the wild-type partner) — mechanistically important and worth a distinct pathophysiology node. Missense variants generally associate with **milder** phenotypes than truncating variants.

### Genotype–phenotype correlations

From Marsh 1999 (BRRS-specific):
> **Verbatim (PMID:10400993):** "Genotype-phenotype analyses within the BRR group suggested a number of correlations, including the association of PTEN mutation and cancer or breast fibroadenoma in any given CS, BRR or BRR/CS overlap family (P = 0.014), and, in particular, truncating mutations were associated with the presence of cancer and breast fibroadenoma in a given family (P = 0.024). Additionally, the presence of lipomas was correlated with the presence of PTEN mutation in BRR patients (P = 0.028)."

From Tan 2012 and GeneReviews (PHTS-wide): promoter variants → breast cancer; nonsense variants → colorectal cancer; frameshift variants overrepresented in thyroid cancer; missense variants overrepresented in ASD. **Caveat for curation:** these are cohort-level associations from ascertained series and should be curated with the association language, not as deterministic rules.

> **Verbatim (PMID:22252256):** "Promoter mutations were associated with breast cancer, whereas colorectal cancer was associated with nonsense mutations."

### Modifier genes

Not formally established. *TTN* (above) is a candidate contributing/modifying locus in PTEN-wildtype disease. Second somatic hits in *PTEN* and downstream PI3K-pathway lesions modulate lesion-level behavior but are not germline modifiers.

### Epigenetics

- **Germline *KLLN* promoter hypermethylation** (see §2) — a *bona fide* germline epigenetic etiology within the PHTS/Cowden-like spectrum, and one of the more elegant examples in human genetics: *PTEN* and *KLLN* share a bidirectional promoter, and the methylation silences KILLIN without touching PTEN transcription.
- **Somatic *PTEN* promoter methylation** in tumors is a common second-hit mechanism.

### Chromosomal abnormalities

Whole-gene and multi-exon *PTEN* deletions account for 3–11% of cases and are missed by sequencing alone — **MLPA or CMA is required** to complete the workup. Larger **10q23 contiguous-gene deletions spanning *PTEN* and *BMPR1A*** produce a severe juvenile-polyposis-plus-BRRS phenotype in infancy and are worth curating as a distinct, more severe presentation.

---

## 5. Environmental Information

**Not applicable as an etiology.** No environmental factor, toxin, radiation exposure, occupational exposure, dietary factor, or infectious agent has been implicated in causing BRRS. There is no NCBI Taxon organism to associate.

The only defensible environmental content is downstream and generic: UV exposure as a modifiable contributor to the melanoma component (lifetime risk up to 6%, earliest reported age 3 years), which is why "sun protection" appears in the parent-education recommendations of the 2024 systematic review. Curate that as **prevention guidance**, not as an etiologic environmental factor.

---

## 6. Mechanism / Pathophysiology

### The causal chain, upstream → downstream

**Node 1 — Germline PTEN haploinsufficiency (MOLECULAR).**
One *PTEN* allele is inactivated in every cell from conception. Because *PTEN* is dose-sensitive, even 50% protein reduction perturbs signaling; tissue-specific second hits (somatic mutation, LOH, promoter methylation) deepen the loss focally and explain the patchy, hamartomatous distribution of lesions.

**Node 2 — Loss of PIP₃ 3-phosphatase activity (MOLECULAR).**
PTEN's canonical function is dephosphorylating the 3-position of the inositol ring of **phosphatidylinositol 3,4,5-trisphosphate (PIP₃)**, converting it back to PIP₂ — it is the direct antagonist of class I PI3K. Established by Maehama & Dixon 1998 (*J Biol Chem* 273:13375–8, **PMID:9593664**), who showed PTEN overexpression reduced insulin-induced PtdIns(3,4,5)P₃ in 293 cells and that purified recombinant PTEN dephosphorylates PIP₃ specifically at the 3-position. Marsh 1999 frames it in disease terms: *"PTEN maps to 10q23 and encodes a dual specificity phosphatase, a substrate of which is phosphatidylinositol 3,4,5-triphosphate, a phospholipid in the phosphatidylinositol 3-kinase pathway."*

**Node 3 — Constitutive PI3K–AKT–mTORC1 pathway activation (CELLULAR).**
PIP₃ accumulates at the plasma membrane → PH-domain recruitment of AKT and PDK1 → AKT phosphorylation (Thr308/Ser473) → inhibition of TSC1/TSC2 → RHEB-GTP → **mTORC1 activation** → S6K1/4E-BP1 phosphorylation → increased cap-dependent translation, ribosome biogenesis, and cell mass. In parallel AKT phosphorylates and inactivates FOXO transcription factors, GSK3β, and BAD.

**Node 4a — Increased cell growth, proliferation, and survival (CELLULAR).**
Net effect: increased cell size (not just number), increased proliferation, suppressed apoptosis, suppressed autophagy, loss of contact inhibition.

**Node 4b — Cell-size / soma-size enlargement (CELLULAR).**
This is the specific mechanism behind macrocephaly and neuronal hypertrophy, and it's mTORC1-driven — which is why it is pharmacologically addressable.

**Node 5 — Tissue-level hamartomatous overgrowth (TISSUE).**
Disorganized overgrowth of mature mesenchymal and epithelial elements — the definition of a hamartoma. Produces lipomas, GI polyps, PTEN hamartoma of soft tissue, and cerebellar dysplastic gangliocytoma.

**Node 6 — Organism-level manifestations (ORGANISM).**
Macrocephaly, macrosomia, accelerated linear growth, ASD/DD, and lifelong tumor predisposition.

### Parallel / non-canonical arms worth separate nodes

- **Protein-phosphatase and phosphatase-independent functions.** PTEN also dephosphorylates protein substrates (e.g. FAK) and has scaffolding functions. The BRRS *TTN* work lands here: the p.Cys5096Arg variant produced "increased growth and lack of contact inhibition phenotype associated with increased levels of or phosphorylation of focal adhesion kinase (FAK)" — a PI3K-independent route to the same overgrowth output. Good candidate for an `ALTERNATIVE` or `EMERGING` `mechanistic_hypotheses` group.
- **Nuclear PTEN.** PTEN shuttles to the nucleus, where it maintains chromosomal integrity and promotes RAD51-dependent DNA repair, independent of lipid phosphatase activity. Variants disrupting nuclear localization signals segregate with the **ASD-predominant** phenotype rather than the cancer phenotype (the basis of the `Pten^m3m4^` mouse; §15). This is arguably the single most interesting mechanistic split in PHTS: **where PTEN is, not just how much there is, determines whether you get autism or cancer.** Curate as competing/complementary hypothesis groups.
- **Neurodevelopmental arm.** PTEN loss in neurons → mTORC1 → increased soma size, exuberant dendritic arborization, aberrant synaptic connectivity, and (per the m3m4 mouse work) **microglial activation with excessive synaptic pruning**. Downstream: macrocephaly, white-matter abnormality, ASD, epilepsy.
- **Vascular arm.** PI3K–AKT is a core endothelial/angiogenic pathway; PTEN loss produces the fast-flow vascular anomalies and intramuscular AVM-like lesions. Tan et al. 2007 (*J Med Genet* 44:594–602) found vascular anomalies in 14/26 (54%) of PTEN carriers, 57% multiple, 85% intramuscular on cross-sectional imaging, and **86% fast-flow**.

### Cellular processes, cell types, and compartments

| Element | Candidate term (⚠️ verify all) |
|---|---|
| PIP₃ 3-phosphatase activity | `GO:0016314` phosphatidylinositol-3,4,5-trisphosphate 3-phosphatase activity |
| PI3K signaling | `GO:0014065` phosphatidylinositol 3-kinase signaling |
| PI3K/AKT signal transduction | `GO:0043491` phosphatidylinositol 3-kinase/protein kinase B signal transduction |
| TOR signaling | `GO:0031929` TOR signaling; `GO:0038202` TORC1 signaling |
| Proliferation | `GO:0008284` positive regulation of cell population proliferation |
| Apoptosis suppression | `GO:0043066` negative regulation of apoptotic process |
| Autophagy | `GO:0006914` autophagy |
| Neuron projection development | `GO:0010975` regulation of neuron projection development |
| Organism growth | `GO:0035264` multicellular organism growth |
| Angiogenesis | `GO:0001525` angiogenesis |
| DNA repair (nuclear PTEN) | `GO:0006281` DNA repair |
| Adipocyte | `CL:0000136` |
| Fibroblast | `CL:0000057` |
| Endothelial cell | `CL:0000115` |
| Neuron | `CL:0000540` |
| Microglial cell | `CL:0000129` |
| Purkinje cell / cerebellar granule cell | `CL:0000121` / `CL:0000120` |
| Thyroid follicular cell | `CL:0002258` |
| Intestinal epithelial cell | `CL:0002563` |
| Keratinocyte | `CL:0000312` |
| Cytosol / plasma membrane / nucleus | `GO:0005829` / `GO:0005886` / `GO:0005634` |
| PIP₃ | `CHEBI:16618` (1-phosphatidyl-1D-myo-inositol 3,4,5-trisphosphate) ⚠️ |

### Metabolic, immune, and tissue-damage dimensions

- **Metabolic:** AKT–mTORC1 activation shifts cells toward anabolic metabolism (glucose uptake, glycolysis, lipogenesis, protein synthesis). *PTEN*-carrier humans and Pten⁺/⁻ mice show **enhanced insulin sensitivity** — a notable, counterintuitive metabolic phenotype of the syndrome.
- **Immune:** no autoimmunity is intrinsic to the mechanism, **except** that Hashimoto thyroiditis is overrepresented (Gorlin 1992: 7 cases) — mechanism unresolved, a legitimate knowledge gap. Microglial (innate CNS immune) activation is a key finding in the m3m4 mouse.
- **Tissue damage:** BRRS is a disease of **disorganized overgrowth**, not of degeneration. There is no oxidative-stress/ischemia/fibrosis/necrosis core mechanism. The exceptions are secondary: mass effect and compression from lipomas and soft-tissue hamartomas, GI bleeding and intussusception from polyps, and high-output/steal physiology from fast-flow vascular lesions.

### Molecular profiling

BRRS-specific omics are essentially absent. What exists is from PHTS/model systems: transcriptome and (phospho)proteome characterization of the cytoplasmic-predominant `Pten^m3m4^` brain (*npj Genom Med* 2021), alternative-splicing landscape of the same model (*Transl Psychiatry* 2020), and a neural transcriptome study linking constitutional Pten dysfunction to idiopathic human ASD (PMID:25754085). Cortical transcriptomics in m3m4 showed upregulation of **myeloid cell activation, myeloid cell migration, and phagocytosis** pathways. No BRRS metabolomics, lipidomics, spatial transcriptomics, or single-cell atlas exists that I could find. **Curate as gaps.**

---

## 7. Anatomical Structures Affected

### Organ level

**Primary (directly affected by the germline lesion):**
- **Brain** (`UBERON:0000955`) — megalencephaly, enlarged perivascular spaces, white-matter abnormality, cortical malformations; **cerebellum** (`UBERON:0002037`) for dysplastic gangliocytoma / Lhermitte–Duclos disease
- **Skin and subcutis** (`UBERON:0002097`) — lipomas, hemangiomas, café-au-lait macules, acral keratoses
- **Penis / external genitalia** (`UBERON:0000989`) — pigmented macules of the glans, the BRRS-defining sign
- **Gastrointestinal tract** — colon (`UBERON:0001155`), also ileum, duodenum, stomach, esophagus. Heald 2010 documented polyps throughout: *"There were one to innumerable polyps in the colorectum, ileum, duodenum, stomach, and/or esophagus, with 24 subjects having both upper and lower GI polyps."*
- **Skeletal muscle** (`UBERON:0001134`) — intramuscular PTEN hamartoma of soft tissue; proximal myopathy
- **Adipose tissue** (`UBERON:0001013`) — lipomatous overgrowth
- **Thyroid gland** (`UBERON:0002046`) — goiter, nodules, Hashimoto thyroiditis, differentiated carcinoma
- **Blood vessels** (`UBERON:0001981`) — fast-flow malformations, AVMs

**Secondary / later-emerging (the PHTS cancer spectrum):** breast (`UBERON:0000310`), endometrium (`UBERON:0001295`), kidney (`UBERON:0002113`), skin (melanoma), colon (carcinoma).

**Body systems:** nervous, integumentary, digestive, endocrine, musculoskeletal, cardiovascular (vascular malformations), reproductive.

### Tissue, cell, and subcellular level

Fundamentally a disease of **mesenchymal + epithelial tissues in combination**. Kurek's definition of PTEN hamartoma of soft tissue is the clearest tissue-level statement available:

> **Verbatim (PMID:22446940, Kurek et al. 2012, *Am J Surg Pathol* 36:671–87):** "We designate this disorganized overgrowth of essentially mesenchymal elements as PTEN hamartoma of soft tissue."

Its components, per the same abstract: "(1) a variable admixture of mature adipocytic and dense and/or myxoid fibrous tissues (50% to 90% of surface area); (2) a vascular component (10% to 50% of surface area)... (3) lymphoid follicles (50%); (4) foci of bone (20%); and (5) hypertrophic nerves with 'onion bulb' proliferation of periaxonal spindled cells (9%)."

**Subcellular:** plasma membrane (PIP₃ pool, PTEN's site of action), cytosol, and nucleus — with the nuclear/cytoplasmic partition being mechanistically load-bearing (§6).

**Lateralization:** lesions are **multifocal and asymmetric**, not systematically lateralized. Kurek: lesions "most often located in the lower extremity," 20% multifocal, occasionally involving contiguous muscles. Macrocephaly is symmetric.

---

## 8. Temporal Development

- **Onset:** **congenital**. Macrocephaly is present at birth or emerges in the first two years — "nearly all children by age 2" per the German pediatric guideline. Neonatal macrosomia is common. Onset pattern is **insidious/chronic**, not acute.
- **Lesion timing:** Kurek — soft-tissue hamartomas "manifested by 15 years of age, normally with pain and swelling." Genital lentiginosis typically appears around/after puberty, which is why it is a poor sign in toddlers. GI polyps present in ~25–30% of pediatric cases (GeneReviews) but 93% of endoscoped adult carriers.
- **Stages:** there is no formal staging system. A useful three-phase framing for the KB: **(i) congenital/infantile overgrowth phase** (macrocephaly, macrosomia, hypotonia, early lipomas/vascular lesions); **(ii) childhood neurodevelopmental phase** (DD, ASD, epilepsy) with emerging polyps and thyroid nodules; **(iii) adult neoplastic phase** (breast, thyroid, endometrial, renal, colorectal cancer, melanoma).
- **Progression rate:** slow and variable. The overgrowth features are largely static; the neoplastic risk is cumulative and age-dependent.
- **Course:** **chronic, lifelong, progressive** with respect to tumor risk. Not relapsing-remitting, not episodic. No spontaneous remission of the syndrome. Individual lesions may regress with mTOR-inhibitor therapy (see §12).
- **Critical periods:** early childhood for neurodevelopmental intervention; **age 10–12** for the start of thyroid surveillance (thyroid cancer reported as young as **age 4–7**); **age ~30** for breast surveillance; **age 35** for colonoscopy. Genetic diagnosis at any age is the intervention that unlocks all the rest.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence: unknown/not documented.** Orphanet does not assign a prevalence class to ORPHA:109. A widely circulated figure of **~1 per 200,000** appears in secondary sources without a strong primary citation — **do not curate it as a sourced prevalence; use `prevalence_class: NOT_YET_DOCUMENTED` or `ULTRA_RARE` with `measure_type: UNKNOWN`.**
- **The molecularly-defined denominator is far larger than the clinically-defined one.** GeneReviews cites ~**1 in 9,000** (All of Us) to **1 in 13,000** (UK Biobank) for germline *PTEN* P/LP carriers; the 2025 All of Us preprint reports **1 in 7,500** (55/414,830), ~26-fold above historical estimates. These are **PHTS-wide, not BRRS**, and describe *carriers*, not diagnosed patients. If you curate them, do it on a PHTS/Cowden entry or with an explicit note; `measure_type: CARRIER_FREQUENCY` is arguably the honest classification.
- **Incidence:** no reliable estimate exists.

### Inheritance

- **Pattern:** **autosomal dominant** (`HP:0000006`). *PTEN* is `MONDO:0007924`'s canonical causal gene.
- **De novo rate:** **up to 48%** of BRRS cases (2024 systematic review) — high, consistent with a severe pediatric-onset presentation.
- **Penetrance:** essentially complete for *some* feature (macrocephaly is near-obligate) but **strongly age-related and organ-specific** for the tumor phenotypes. Unbiased biobank data suggest penetrance is considerably **lower** than clinic-ascertained estimates — a live and important controversy. Curate the clinic-based lifetime risks with an explicit ascertainment caveat.
- **Expressivity:** **markedly variable**, including within families sharing an identical variant. This is the central clinical-genetics message of Lachlan 2007.
- **Anticipation:** **not a feature** (no repeat expansion mechanism).
- **Germline mosaicism:** reported in *PTEN* and relevant to recurrence counseling in apparently-de-novo families, but rare and not well quantified. **Somatic mosaicism** is a recognized cause of segmental/atypical presentations and of negative blood-based testing in a clinically convincing patient — this matters for diagnostics.
- **Founder effects / consanguinity / carrier frequency:** none — irrelevant for a dominant de-novo-prone condition. No population-specific founder variant is described.

### Population demographics

- **Ethnic/geographic:** no population is over-represented; cases are reported worldwide with no endemic distribution.
- **Sex ratio:** published pediatric BRRS cases run **~72% male (60/83)**, but this is very likely ascertainment bias from the male-specific genital-lentiginosis sign. The underlying autosomal-dominant inheritance predicts **1:1**. Curate the 1:1 expectation and note the reporting skew.
- **Age distribution:** BRRS as a *label* is applied predominantly in childhood (median age 8 in the review); the same genotype in adults is usually labeled Cowden syndrome.

---

## 10. Diagnostics

### Clinical evaluation

- **Occipitofrontal circumference** — the highest-yield single measurement; macrocephaly is often >5 SD above mean.
- **Genital examination in males** for pigmented macules of the glans penis (75% of male cases) — pathognomonic-adjacent and free.
- **Dermatologic exam** for lipomas, hemangiomas, café-au-lait macules, trichilemmomas/acral keratoses (the latter more Cowden-flavored).
- **Developmental/neurobehavioral assessment**, including formal ASD evaluation.

### Imaging and functional testing

- **Brain MRI** — megalencephaly, enlarged Virchow–Robin spaces, white-matter changes; the cerebellar "tiger-striped" appearance of Lhermitte–Duclos disease. A dedicated BRRS MRI series exists (Bhargava et al., *AJNR* 35:402, **PMID:23907246**).
- **MRI for soft-tissue/vascular lesions** — Kurek: "an infiltrative soft tissue lesion involving the muscle, fascia, and subcutis with frequently enlarged, serpiginous vessels, small arteriovenous fistulae with disproportionately dilated draining veins, and a prominent adipocytic component." Distinguishing PHOST from a true AVM matters because it changes management.
- **Thyroid ultrasound** — the pediatric surveillance workhorse.
- **Esophagogastroduodenoscopy + colonoscopy** — mixed polyposis, upper *and* lower.
- **EEG** where seizures are suspected (epilepsy 6–17%).

### Biopsy and pathology

- **GI polyps in PHTS are a *mixed* polyposis** — this is a frequent diagnostic pitfall, because people expect pure hamartomas. Heald 2010: *"Of the 64, half had hyperplastic polyps"* and the conclusion — *"PTEN-associated CS should be considered a mixed polyp syndrome, with hyperplastic polyps most prevalent, with a risk of early onset colorectal cancer."* Hamartomatous, ganglioneuromatous, juvenile, inflammatory, hyperplastic, and adenomatous polyps all occur.
- **PTEN hamartoma of soft tissue** has the distinctive histology quoted in §7, and per Kurek "its identification should prompt a thorough investigation for PHTS" — i.e. the pathologist can make the syndromic diagnosis.
- **Immunohistochemistry for PTEN loss** in lesional tissue is supportive.

### Genetic testing (the definitive test)

Since PHTS has **no clinical diagnostic criteria**, molecular confirmation is the diagnosis. Recommended approach:

1. **Single-gene *PTEN* testing** — full coding sequence **plus the promoter region** (~10% of variants are promoter). Design around the *PTENP1* pseudogene.
2. **Deletion/duplication analysis (MLPA)** — mandatory adjunct; 3–11% of variants.
3. **Multigene hamartomatous-polyposis / hereditary-cancer panel** where the phenotype is ambiguous (differentiating from *STK11*, *SMAD4*, *BMPR1A*, *AKT1*, *PIK3CA*).
4. **Chromosomal microarray** — detects the 10q23 contiguous-gene deletions involving *PTEN* + *BMPR1A*, and is often the first test in a child presenting with DD/macrocephaly.
5. **WES/WGS** — reasonable in the undiagnosed-DD pathway; also the route by which *TTN* was implicated in PTEN-wildtype BRRS.
6. **Not applicable:** karyotype (too coarse), FISH (superseded by MLPA/CMA), mtDNA testing, repeat-expansion testing.
7. **If PTEN-negative but clinically classic:** consider *KLLN* germline methylation testing, *SDHB/SDHD*, and mosaicism (test lesional tissue, not just blood).

### Omics-based diagnostics

**Not established for BRRS.** No validated RNA-seq, proteomic, metabolomic, epigenomic (other than the *KLLN* methylation assay), or liquid-biopsy diagnostic exists. A methylated KILLIN/PTEN plasma assay has been explored for thyroid/breast cancer detection but is **not** a clinical diagnostic for BRRS.

### Clinical criteria and differential diagnosis

The **International Cowden Consortium** operational criteria (and the Cleveland Clinic *PTEN* risk calculator, Tan et al. 2011) select who to *test*; they do not diagnose PHTS. Historical BRRS clinical criteria required macrocephaly plus two of: hamartomatous polyps, lipomas, genital lentiginosis.

**Differential diagnosis:**

| Condition | Distinguishing features |
|---|---|
| Cowden syndrome (`MONDO:0016063`) | Same gene, same disease — adult mucocutaneous/cancer presentation. Distinguish by *age and presentation*, not biology |
| Peutz–Jeghers (*STK11*) | Perioral/buccal mucocutaneous pigmentation (not genital-only); polyps show characteristic **smooth-muscle arborization** |
| Juvenile polyposis (*SMAD4*, *BMPR1A*) | Juvenile polyps; HHT overlap if *SMAD4*; no macrocephaly/lipomas |
| Proteus syndrome (*AKT1* mosaic) | Progressive, asymmetric, distorting overgrowth; cerebriform connective tissue nevus |
| PIK3CA-related overgrowth (PROS/CLOVES) | Mosaic, segmental; same pathway, different node |
| Neurofibromatosis type 1 | Café-au-lait + neurofibromas + Lisch nodules; macrocephaly overlaps — a genuine clinical trap |
| Simpson–Golabi–Behmel, Sotos, Weaver | Other overgrowth syndromes; distinguish by facies, skeletal findings, and gene |
| Isolated benign macrocephaly | The commonest real-world alternative in a well child |

### Screening of asymptomatic individuals

**Cascade testing of at-risk first-degree relatives** is the key intervention, and given up-to-48% de novo rates, parental testing is essential for recurrence counseling. There is **no newborn screening and no population carrier screening** for *PTEN*. Prenatal/preimplantation testing is technically available once a familial variant is known.

---

## 11. Outcome / Prognosis

- **Life expectancy:** not formally quantified for BRRS. With surveillance, life expectancy is thought to approach normal; the drivers of mortality are the malignancies, not the overgrowth. **Do not curate a survival number** — I found none that is BRRS-specific and defensible.
- **Cancer risk (PHTS-wide, from clinic-ascertained cohorts):**

> **Verbatim (PMID:22252256, Tan et al. 2012, *Clin Cancer Res* 18:400–7):** "Elevated SIRs were found for carcinomas of the breast [25.4, 95% confidence interval (CI), 19.8-32.0], thyroid (51.1, 38.1-67.1), endometrium (42.9, 28.1-62.8), colorectum (10.3, 5.6-17.4), kidney (30.6, 17.8-49.4), and melanoma (8.5, 4.1-15.6). Estimated lifetime risks were, respectively, 85.2% (95% CI, 71.4%-99.1%), 35.2% (19.7%-50.7%), 28.2% (17.1%-39.3%), 9.0% (3.8%-14.1%), 33.6% (10.4%-56.9%), and 6% (1.6%-9.4%)."

  GeneReviews gives comparable ranges (breast 85–91%, thyroid 33–35%, endometrial 28–48%, renal 30–35%, colorectal 17%, melanoma up to 6%) plus soft-tissue sarcoma SIR **10.7 (95% CI 3.9–23.7)**, median age 46. Later European work (Hendricks et al., *Clin Genet* 2021; *JNCI* 2023) gives **lower** estimates — breast 54–76%, endometrial 6–22%, thyroid 9–21% — reflecting less-biased ascertainment. **Curate the range with both anchors and an explicit ascertainment caveat; a single point estimate here would be misleading.**
- **Colorectal cancer, early onset:** Heald 2010 — *"Nine (13%) subjects had colorectal cancer, all younger than the age of 50. The adjusted standardized incidence ratio was 224.1 (95% confidence interval, 109.3-411.3; P < .0001)."*
- **Morbidity and disability:** dominated by **neurodevelopmental outcome** (intellectual disability, ASD, epilepsy) and by **pain/functional loss from soft-tissue and vascular lesions** — Kurek reported resected specimens 1.2–25 cm, with amputation required in one patient. GI morbidity from bleeding, anemia, intussusception, and repeated polypectomy.
- **Complications:** early-onset colorectal carcinoma; differentiated thyroid carcinoma (reported as young as 4–7 years); Lhermitte–Duclos disease with mass effect/hydrocephalus; hemorrhage and high-output physiology from fast-flow vascular lesions; recurrent surgical morbidity.
- **Recovery potential:** the germline lesion is not reversible. Individual lesions respond to surgery and, partially, to mTOR inhibition. Developmental gains occur with early intervention. **Surveillance is the single largest determinant of outcome.**
- **Prognostic factors:** variant type (truncating → higher cancer risk per Marsh 1999; promoter → breast; nonsense → colorectal); age; adherence to surveillance; presence and extent of vascular/soft-tissue hamartomas; severity of neurodevelopmental impairment. **No validated prognostic biomarker exists.**

---

## 12. Treatment

**There is no disease-modifying or curative therapy.** Management is surveillance + symptom-directed intervention + genetic counseling. The 2024 systematic review is blunt about it: *"As targeted treatment is still lacking, symptom relief and long-term surveillance remain the main management strategies."*

### Surgical / interventional (the mainstay)

Per the 2024 review, **surgery was the treatment of choice, described in 19 of 33 articles**:
- **Lipoma excision** — for pain, disfigurement, compression. `treatment_term`: `NCIT:C15329` Surgical Procedure ⚠️
- **Endoscopic polypectomy** — for bleeding, obstruction, dysplasia. ⚠️ verify NCIT term for polypectomy
- **Thyroidectomy** — 4 pediatric cases in the review; prophylactic thyroidectomy is debated in PHTS and is **not** standard, unlike in MEN2. `NCIT:C15289`-adjacent ⚠️
- **Vascular anomaly management** — embolization, sclerotherapy, or resection. Because PHOST is not a true AVM, embolization outcomes are less predictable than for classic AVM.
- **Resection of Lhermitte–Duclos lesions** where symptomatic.

### Pharmacotherapy — mTOR inhibitors

Mechanistically the obvious move: *PTEN* loss → mTORC1 hyperactivation → inhibit mTOR. Results so far are **mixed, and this nuance must survive into the KB.**

**Sirolimus (rapamycin)** — `CHEBI:9168` ⚠️; `therapeutic_modality: SMALL_MOLECULE`; `treatment_term: NCIT:C15986` Pharmacotherapy.
- Komiya et al. 2019 (*The Oncologist* 24:1510, doi:10.1634/theoncologist.2019-0514): first human interventional study in Cowden/PTEN patients; 18 patients, 16 families; 56-day course. Well tolerated; **regression of skin and GI lesions by dermoscopy/endoscopy, improved cerebellar function score at 1 month, and suppressed mTOR signaling in surrogate tissue.** Pilot-scale — no efficacy claim.
- Open-label sirolimus 2 mg daily × 1 year for colon polyposis in PHTS (**NCT04094675**, Nov 2018 – Jun 2024) — published in *Clin Transl Gastroenterol*.
- Case-level use in pediatric BRRS for AVM: the 2024 review notes **one** pediatric case, with AVM size reduction and symptom relief within 6 months.
- Sirolimus for PHTS vascular anomalies: well tolerated, patient-reported QoL improvement (n=6).

**Everolimus** — `CHEBI:68478` ⚠️. The one properly controlled trial is **negative** for its primary endpoint:
- Srivastava et al. 2022 (*Hum Mol Genet* 31:3393–404, **PMID:35594551**): 6-month phase II, randomized, double-blind, placebo-controlled, everolimus 4.5 mg/m², ages 5–45, n=46 (24 everolimus / 22 placebo). Primary neurocognitive composite: **no group difference (Cohen's d = −0.10, p = 0.518)**; GI adverse events significantly more common on everolimus (p < 0.001).
- **Curate this honestly.** An entry that lists "mTOR inhibitors" as treatment for PHTS neurocognitive symptoms without the negative RCT would be misleading. It is a good candidate for an evidence item with `supports: REFUTE` or `PARTIAL`.

### Targeted / advanced therapeutics

**None approved.** No gene therapy, gene editing, cell therapy, RNA-based therapy, or immunotherapy exists for BRRS. PI3K/AKT inhibitors are conceptually attractive and used in *PIK3CA*-related overgrowth (alpelisib) but are **not** established in PHTS. Do not extrapolate.

### Pharmacogenomics

No PHTS-specific pharmacogenomic guidance. Standard CPIC guidance applies to any drugs used for the cancers that arise.

### Supportive, rehabilitative, and counseling

- **Early intervention, physical therapy** (`NCIT:C15302`), **occupational therapy**, **speech therapy** — for hypotonia, motor delay, and language delay. `therapeutic_modality: BEHAVIORAL`.
- **ASD-specific behavioral intervention** and educational support.
- **Antiseizure medication** where epilepsy is present.
- **Genetic counseling** (`NCIT:C15240`) — recurrence risk 50% per offspring; parental testing given the high de novo rate; discussion of prenatal/PGT options; cascade testing of relatives.
- **Multidisciplinary care** is the explicit recommendation of the 2024 review: *"periodic multidisciplinary care that should be individualized to fit every patient's needs."*

### Treatment strategy

Individualized, lesion-directed, and surveillance-anchored. No treatment algorithm or decision tree is standardized. No combination-therapy regimen exists (so `regimen_term` is **not applicable** here).

---

## 13. Prevention

- **Primary prevention: not possible.** The disorder is germline and congenital. No vaccination, no modifiable exposure, no risk-factor modification prevents BRRS. The only true primary prevention available is **reproductive** — preimplantation genetic testing or prenatal diagnosis once a familial variant is identified, which is a family-planning decision requiring genetic counseling, not a public-health intervention.
- **Secondary prevention: this is where essentially all the benefit lives.** Surveillance recommendations (synthesizing GeneReviews, the 2020 European guideline (Tischkowitz et al., *Eur J Hum Genet* 28:1387–93, PMC7608293), the 2025 pediatric update (*Clin Cancer Res* 31(2):234), and the German pediatric guideline):

  | Target | Recommendation |
  |---|---|
  | **Thyroid** | Annual clinical exam + **thyroid ultrasound from age 12** (some centers from age 10; every 2–3 y under age 7 if no nodules). Cancer reported as young as 4–7 y |
  | **Breast** | Monthly self-exam from 18; clinical exam q6–12 mo from 25; **annual mammogram + breast MRI from 30** |
  | **Endometrium** | Assessment q1–2 y from age 30–35; educate about abnormal bleeding |
  | **Colon** | **Colonoscopy from age 35**, q5 y (sooner/more often if polyp burden is high — and note the early-onset CRC signal) |
  | **Kidney** | Renal imaging q1–2 y from age 40 |
  | **Skin** | Annual comprehensive dermatologic exam; sun protection education |
  | **Brain** | MRI as clinically indicated; q3–12 mo if Lhermitte–Duclos present |
  | **Pediatric extras** | Annual dermatologic exam; annual abdominal ultrasound; testicular ultrasound from ~age 10; ongoing psychomotor/neurodevelopmental assessment (German guideline) |

  Yield data exist and are modest but real: thyroid ultrasound surveillance detected DTC in **2/43 (4.65%)** of PHTS patients before age 18 in one expertise centre.

- **Tertiary prevention:** management of polyp burden to prevent CRC; management of vascular lesions to prevent hemorrhage; neurodevelopmental support to maximize function.
- **Risk stratification:** the Cleveland Clinic *PTEN* score (Tan et al. 2011) identifies who should be tested; variant type provides coarse organ-risk stratification.
- **Immunization, public-health, and environmental interventions:** **not applicable.**

---

## 14. Other Species / Natural Disease

- **Naturally occurring BRRS in other species: none reported.** I found no OMIA entry for a spontaneous *PTEN* hamartoma syndrome in companion animals or wildlife, and no veterinary breed predisposition. There is no VBO breed to assign.
- **Zoonotic potential / cross-species transmission: not applicable** — it's a germline genetic disorder.
- ***PTEN* orthologs** are deeply conserved, which is what makes the modeling work: mouse *Pten* (NCBI Gene 19211, `NCBITaxon:10090`), rat *Pten*, zebrafish has two paralogs *ptena*/*ptenb* (`NCBITaxon:7955`), *Drosophila* **Pten** (`NCBITaxon:7227`), *C. elegans* **daf-18** (`NCBITaxon:6239`). The *daf-18* connection is a nice piece of comparative biology: the insulin/IGF-1–PI3K–DAF-16/FOXO axis controlling dauer formation and lifespan in worms is the same pathway that, dysregulated in humans, produces hamartomas. Conserved mechanism, wildly different phenotypic readout.
- **Comparative pathology:** somatic *PTEN* loss is a recurrent event in spontaneous canine and feline tumors (canine osteosarcoma, melanoma, glioma), making dogs an incidental comparative-oncology resource — but that is somatic tumor biology, not the germline syndrome.

---

## 15. Model Organisms

### Mouse (`NCBITaxon:10090`) — the workhorse

| Model | Design | Phenotype | Citation |
|---|---|---|---|
| **Pten⁺/⁻ (constitutive het)** | Germline heterozygous null — the direct genocopy of human PHTS | Multi-organ hyperplasia and neoplasia (thyroid, endometrium, GI, lymphoid); increased insulin sensitivity. Homozygous null is **embryonic lethal**, establishing the dominant/haploinsufficient mechanism | Di Cristofano et al. 1998 *Nat Genet*; Podsypanina et al. 1999 *PNAS* |
| **Nse-Cre / GFAP-Cre conditional brain Pten KO** | Neuron- or glia-restricted deletion | **"Deletion of Pten in mouse brain causes seizures, ataxia and defects in soma size resembling Lhermitte-Duclos disease"** — a near-exact recapitulation of the human cerebellar phenotype | Backman et al. 2001 *Nat Genet* 29:396–403, **PMID:11726927**; Kwon et al. 2001, PMID:11726928 |
| **Nse-Cre Pten KO (cortex/hippocampus)** | Deletion in limited differentiated neuronal populations | **Abnormal social interaction, exaggerated response to sensory stimuli, macrocephaly, increased dendritic arborization** — the founding PTEN autism model | Kwon et al. 2006 *Neuron* 50:377–88, **PMID:16675393** |
| **Pten^m3m4^ (knock-in)** | Disrupts 2 of 4 putative nuclear localization signals → **cytoplasm-predominant PTEN with nuclear depletion**; normal total protein | Macrocephaly from megencephaly, neuronal soma hypertrophy, gliosis, autism-like behavior; **microglial activation with enhanced synaptic pruning**; cortical upregulation of myeloid activation/migration/phagocytosis pathways | Sarn et al. 2020 *Mol Psychiatry*, doi:10.1038/s41380-020-0681-0 |
| **Nuclear-predominant Pten model** | Complementary partition mutant | Impaired social and perseverative behavior, microglial activation, increased oxytocinergic activity | *Mol Autism* 2021, doi:10.1186/s13229-021-00448-4 |
| **Pten^m3m4^ multi-omics** | — | Transcriptome/(phospho)proteome and alternative-splicing characterization of the autism-like brain | *npj Genom Med* 2021; *Transl Psychiatry* 2020 |

**Why the m3m4 model matters for this entry:** it demonstrates that *subcellular mislocalization* of PTEN — with normal expression level — is sufficient to produce the neurodevelopmental arm of PHTS. That's a genuine mechanistic dissociation between the ASD phenotype and the cancer phenotype, and it maps directly onto the human genotype–phenotype observation that missense variants are overrepresented in ASD. It is the strongest argument for curating the neurodevelopmental and neoplastic arms as **separate pathophysiology branches**.

### Other systems

- **Zebrafish** (`NCBITaxon:7955`): *ptena/ptenb* double mutants are embryonic lethal with hyperbranched vasculature; single mutants are viable and tumor-prone — a useful vascular/angiogenesis model given the BRRS vascular phenotype.
- ***Drosophila*** (`NCBITaxon:7227`): *Pten* mutants show classic cell-size and organ-size overgrowth; the system where the PI3K–TOR growth-control logic was largely worked out.
- ***C. elegans*** (`NCBITaxon:6239`): *daf-18*, the insulin/IGF-1–DAF-16 axis.
- **Cell and in vitro:** patient-derived fibroblasts and LCLs; **patient iPSC-derived neurons and cortical organoids** show increased soma size, altered proliferation, and synaptic phenotypes, and are the most translationally relevant human system currently available; CRISPR-edited isogenic lines (the route used for the *TTN* p.Cys5096Arg functional work). MorPhiC has not, to my knowledge, targeted *PTEN* — worth checking morphic.bio before asserting either way.

### Recapitulation and limitations

**Recapitulates well:** macrocephaly/megalencephaly, neuronal soma enlargement, Lhermitte–Duclos-like cerebellar pathology, ASD-like social deficits, seizures, multi-organ tumor predisposition, enhanced insulin sensitivity.

**Does NOT recapitulate:** genital lentiginosis (no analog), the human GI mixed-polyp spectrum in its full form, the specific human cancer-organ distribution (mouse tumor spectrum skews differently — thyroid/endometrial/lymphoid rather than breast-dominant), PTEN hamartoma of soft tissue as a defined entity, and the human developmental/cognitive profile in any fine-grained way. Mouse background strain strongly modifies tumor spectrum. **Any curated evidence item drawn from these should carry `evidence_source: MODEL_ORGANISM` and must not be the sole support for a human phenotype** — and given the m3m4 findings are load-bearing for the ASD mechanism but unconfirmed in human tissue, a `discussions` entry with `kind: HUMAN_MODEL_MISMATCH` is warranted rather than a plain `KNOWLEDGE_GAP`.

### Model databases

MGI (mouse), Alliance of Genome Resources, IMPC/KOMP, IMSR/JAX for strain availability, ZFIN, FlyBase, WormBase, Cellosaurus for lines.

---

## Appendix A — Suggested `mechanistic_hypotheses` and `discussions`

Things I'd flag as genuinely unsettled, worth curating as structured discussion rather than prose:

1. **`nuclear_vs_cytoplasmic_pten` (competing hypothesis groups).** Whether the ASD/neurodevelopmental arm is driven by loss of *nuclear* PTEN function (DNA repair, m3m4 evidence) versus by cytoplasmic PIP₃/mTORC1 excess. `status: EMERGING`. Attaches to the neurodevelopmental branch.
2. **`ttn_as_brrs_gene` — `KNOWLEDGE_GAP` / `EMERGING`.** *TTN* enrichment in PTEN-wildtype BRRS is statistically modest (OR 2.2–2.7, p ≈ 0.02–0.05, single lab, no replication cohort published that I found). Do not curate *TTN* as causal.
3. **`phts_penetrance_ascertainment` — `KNOWLEDGE_GAP`.** Clinic-ascertained lifetime cancer risks (breast 85%) versus biobank-derived risks (54–76%, and much lower overall penetrance in All of Us/UK Biobank) differ enough to change clinical advice. Unresolved.
4. **`mtor_inhibition_efficacy` — `KNOWLEDGE_GAP`.** Sirolimus pilots are positive on biomarkers and lesions; the only randomized everolimus trial missed its neurocognitive primary endpoint. Whether mTOR inhibition helps *any* PHTS outcome durably is open.
5. **`hashimoto_thyroiditis_mechanism` — `KNOWLEDGE_GAP`.** Autoimmune thyroiditis is overrepresented since Gorlin 1992; no mechanism connects PTEN loss to thyroid autoimmunity.
6. **`brrs_cowden_entity_boundary`.** Worth an explicit note: this KB models BRRS and Cowden as separate entries while the literature treats them as one disease. Consider a `Grouping` over the PHTS entries with `grouping_basis: [SHARED_MECHANISM, CLINICAL_CONVENTION]` and a `grouping_rationale` that records exactly this lump/split tension — a `NECESSARY` `HAS_GENE` criterion on PTEN would make the boundary auditable.

## Appendix B — Suggested `conforms_to` module targets

Check these against `kb/modules/` before asserting:
- The **PI3K–AKT–mTOR overgrowth** logic here has no dedicated module yet — BRRS/PHTS would be a strong flagship if one is created (candidate: `pi3k_akt_mtor_overgrowth`).
- `genome_instability_mutation` — the nuclear-PTEN/RAD51 arm plausibly conforms.
- `sustaining_proliferative_signaling` — constitutive PI3K–AKT mitogenic signaling is exactly this hallmark node.
- `evading_growth_suppressors` — *PTEN* is a canonical tumor suppressor; the two-hit/haploinsufficiency logic fits.
- `tumor_angiogenesis` — for the vascular malformation arm, though the fit is imperfect (these are malformations, not tumor neovasculature).

---

## References (with PMIDs)

**Verbatim abstract text retrieved and usable as evidence snippets (still run `just fetch-reference` + `just validate-references`):**

- **PMID:10400993** — Marsh DJ, Kum JB, Lunetta KL, et al. PTEN mutation spectrum and genotype-phenotype correlations in Bannayan-Riley-Ruvalcaba syndrome suggest a single entity with Cowden syndrome. *Hum Mol Genet.* 1999;8(8):1461-72. doi:10.1093/hmg/8.8.1461
- **PMID:9467011** — Marsh DJ, Coulon V, Lunetta KL, et al. Mutation spectrum and genotype-phenotype analyses in Cowden disease and Bannayan-Zonana syndrome. *Hum Mol Genet.* 1998;7(3):507-15. doi:10.1093/hmg/7.3.507
- **PMID:22252256** — Tan MH, Mester JL, Ngeow J, Rybicki LA, Orloff MS, Eng C. Lifetime cancer risks in individuals with germline PTEN mutations. *Clin Cancer Res.* 2012;18(2):400-7.
- **PMID:20600018** — Heald B, Mester J, Rybicki L, Orloff MS, Burke CA, Eng C. Frequent gastrointestinal polyps and colorectal adenocarcinomas in a prospective series of PTEN mutation carriers. *Gastroenterology.* 2010;139(6):1927-33.
- **PMID:22446940** — Kurek KC, Howard E, Tennant LB, et al. PTEN hamartoma of soft tissue: a distinctive lesion in PTEN syndromes. *Am J Surg Pathol.* 2012;36(5):671-87.
- **PMID:29263846** — Yehia L, Ni Y, Eng C. Germline TTN variants are enriched in PTEN-wildtype Bannayan-Riley-Ruvalcaba syndrome. *npj Genom Med.* 2017;2:37. doi:10.1038/s41525-017-0039-y
- **PMID:31609537** — Macken WL, Tischkowitz M, Lachlan KL. PTEN hamartoma tumor syndrome in childhood: A review of the clinical literature. *Am J Med Genet C.* 2019.
- **PMID:39256443** — Kapačinskaitė M, Stratica N, Adomaitienė I, Rascon J, Vaišnytė B. A systematic review of Bannayan-Riley-Ruvalcaba syndrome. *Sci Rep.* 2024;14. doi:10.1038/s41598-024-71991-2

**Cited but abstract not independently retrieved verbatim — verify before quoting:**

- PMID:9241266 — Marsh DJ, et al. Germline mutations in PTEN are present in Bannayan-Zonana syndrome. *Nat Genet.* 1997;16(4):333-4. ⚠️ **Letter — no abstract exists.** Cannot supply a snippet.
- PMID:11332402 — Parisi MA, et al. The spectrum and evolution of phenotypic findings in PTEN mutation positive cases of Bannayan-Riley-Ruvalcaba syndrome. *J Med Genet.* 2001;38(1):52-8. ⚠️ No `abstractText` in Europe PMC; use PMC1734718 full text.
- PMID:1336932 — Gorlin RJ, et al. Bannayan-Riley-Ruvalcaba syndrome. *Am J Med Genet.* 1992;44(3):307-14.
- PMID:9593664 — Maehama T, Dixon JE. The tumor suppressor, PTEN/MMAC1, dephosphorylates the lipid second messenger, phosphatidylinositol 3,4,5-trisphosphate. *J Biol Chem.* 1998;273(22):13375-8.
- PMID:12938083 — Eng C. PTEN: one gene, many syndromes. *Hum Mutat.* 2003.
- PMID:11726927 / PMID:11726928 — Backman SA et al.; Kwon CH et al. *Nat Genet.* 2001.
- PMID:16675393 — Kwon CH, Luikart BW, Powell CM, et al. Pten regulates neuronal arborization and social interaction in mice. *Neuron.* 2006;50(3):377-88.
- PMID:18678321 — Ni Y, Zbuk KM, Sadler T, et al. Germline mutations and variants in the succinate dehydrogenase genes in Cowden and Cowden-like syndromes. *Am J Hum Genet.* 2008;83(2):261-8.
- PMID:21177507 — Bennett KL, Mester J, Eng C. Germline epigenetic regulation of KILLIN in Cowden and Cowden-like syndrome. *JAMA.* 2010;304(24):2724-31.
- PMID:25288137 — Frazier TW, et al. Molecular and phenotypic abnormalities in individuals with germline heterozygous PTEN mutations and autism. *Mol Psychiatry.* 2015.
- PMID:25754085 — Neural transcriptome of constitutional Pten dysfunction in mice and its relevance to human idiopathic ASD.
- PMID:23907246 — Bhargava R, et al. Bannayan-Riley-Ruvalcaba syndrome: MRI neuroimaging features in a series of 7 patients. *AJNR.* 2014;35(2):402.
- PMID:35594551 — Srivastava S, et al. A randomized controlled trial of everolimus for neurocognitive symptoms in PTEN hamartoma tumor syndrome. *Hum Mol Genet.* 2022;31(20):3393-404.
- PMID:39250745 — Dhawan A, Baitamouni S, Liu D, Eng C. Clinical Neurologic Features and Evaluation of PTEN Hamartoma Tumor Syndrome: A Systematic Review. *Neurology.* 2024;103(7):e209844.
- PMID:31433955 — Yehia L, Keel E, Eng C. The Clinical Spectrum of PTEN Mutations. *Annu Rev Med.* 2020.
- Tischkowitz M, Colas C, Pouwels S, et al. Cancer Surveillance Guideline for individuals with PTEN hamartoma tumour syndrome. *Eur J Hum Genet.* 2020;28:1387-93. (PMC7608293)
- Komiya T, Blumenthal GM, DeChowdhury R, et al. A Pilot Study of Sirolimus in Subjects with Cowden Syndrome or Other Syndromes Characterized by Germline Mutations in PTEN. *The Oncologist.* 2019;24(12):1510. (PMC6975943)
- Hendricks LAJ, et al. A review on age-related cancer risks in PTEN hamartoma tumor syndrome. *Clin Genet.* 2021. (PMC7839546) · Cancer risks by sex and variant type in PHTS. *JNCI.* 2023.
- Update on Pediatric Surveillance Recommendations for PTEN Hamartoma Tumor Syndrome, DICER1-Related Tumor Predisposition, and Tuberous Sclerosis Complex. *Clin Cancer Res.* 2025;31(2):234.
- PMID:41480035 — Population-based Characterization of PTEN Hamartoma Tumor Syndrome. **medRxiv preprint, Dec 2025** — cite as preliminary.
- Sarn N, et al. Cytoplasmic-predominant Pten increases microglial activation and synaptic pruning in a murine model with autism-like phenotype. *Mol Psychiatry.* 2021. (PMC8159731)
- GeneReviews: PTEN Hamartoma Tumor Syndrome. NCBI Bookshelf NBK1488. (PMID:20301661)

---

**Sources:**

- [PTEN Hamartoma Tumor Syndrome — GeneReviews (NBK1488)](https://www.ncbi.nlm.nih.gov/books/NBK1488/)
- [MONDO:0007924 — EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0007924)
- [A systematic review of Bannayan–Riley–Ruvalcaba syndrome (PMC11387762)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11387762/)
- [Marsh 1999, PTEN mutation spectrum in BRRS (PMID:10400993)](https://pubmed.ncbi.nlm.nih.gov/10400993/)
- [Germline TTN variants in PTEN-wildtype BRRS (PMID:29263846)](https://pubmed.ncbi.nlm.nih.gov/29263846/)
- [Tan 2012, Lifetime cancer risks in germline PTEN mutations (PMID:22252256)](https://pubmed.ncbi.nlm.nih.gov/22252256/)
- [Heald 2010, GI polyps in PTEN mutation carriers (PMID:20600018)](https://pubmed.ncbi.nlm.nih.gov/20600018/)
- [Kurek 2012, PTEN hamartoma of soft tissue (PMID:22446940)](https://pubmed.ncbi.nlm.nih.gov/22446940/)
- [Macken 2019, PHTS in childhood (PMID:31609537)](https://pubmed.ncbi.nlm.nih.gov/31609537/)
- [Cancer Surveillance Guideline for PHTS (PMC7608293)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7608293/)
- [Update on Pediatric Surveillance Recommendations, Clin Cancer Res 2025](https://aacrjournals.org/clincancerres/article/31/2/234/751094/Update-on-Pediatric-Surveillance-Recommendations)
- [Everolimus RCT for neurocognitive symptoms in PHTS (PMID:35594551)](https://pubmed.ncbi.nlm.nih.gov/35594551/)
- [Sirolimus pilot in Cowden syndrome (PMC6975943)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6975943/)
- [German pediatric PHTS guideline (PMC8859017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8859017/)
- [Population-based Characterization of PHTS — preprint (PMC12755263)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12755263/)
- [Clinical Neurologic Features of PHTS, Neurology 2024](https://www.neurology.org/doi/10.1212/WNL.0000000000209844)
- [Cytoplasmic-predominant Pten / microglial pruning (PMC8159731)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8159731/)
- [Maehama & Dixon 1998, PTEN dephosphorylates PIP3 (PMID:9593664)](https://pubmed.ncbi.nlm.nih.gov/9593664/)
- [Kwon 2006, Pten regulates neuronal arborization and social interaction (PMID:16675393)](https://pubmed.ncbi.nlm.nih.gov/16675393/)
- [Ni 2008, SDH variants in Cowden/Cowden-like (PMID:18678321)](https://pubmed.ncbi.nlm.nih.gov/18678321/)
- [Germline epigenetic regulation of KILLIN (PMID:21177507)](https://pubmed.ncbi.nlm.nih.gov/21177507/)
- [Orphanet: Bannayan-Riley-Ruvalcaba syndrome (ORPHA:109)](https://www.orpha.net/en/disease/detail/109)
- [NORD: Bannayan-Riley-Ruvalcaba Syndrome](https://rarediseases.org/rare-diseases/ruvalcaba-syndrome/)
- [MedGen C0265326](https://www.ncbi.nlm.nih.gov/medgen/78554)