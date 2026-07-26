---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-26T13:22:13.752276'
end_time: '2026-07-26T13:27:36.263368'
duration_seconds: 322.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lupus Nephritis
  mondo_id: MONDO:0005556
  category: Complex
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
  - claude-sonnet-5
  web_search_requests: 21
  num_turns: 21
  total_cost_usd: 1.6809834
  session_id: f9a4f8a6-559e-5875-b202-2cc5a4e70210
  stop_reason: end_turn
citation_count: 126
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lupus Nephritis
- **MONDO ID:** MONDO:0005556 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Lupus Nephritis** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Lupus Nephritis (LN) — Comprehensive Research Report for Knowledge Base Curation

## 1. Disease Information

**Overview:** Lupus nephritis (LN) is immune complex–mediated glomerulonephritis occurring as an organ-specific manifestation of systemic lupus erythematosus (SLE), affecting an estimated 30–60% of adult SLE patients and up to 70–80% of childhood-onset SLE patients over the disease course. It results from deposition of autoantibody–autoantigen immune complexes (chiefly anti-dsDNA/chromatin-containing complexes) in the glomerular mesangium, subendothelial and/or subepithelial space, triggering complement activation, leukocyte recruitment, and progressive glomerular, tubulointerstitial, and vascular injury. Renal involvement is one of the strongest predictors of morbidity and mortality in SLE and is the only organ-specific finding (biopsy-proven class III/IV LN) sufficient on its own, together with a positive ANA, to classify a patient as having SLE under the 2019 EULAR/ACR criteria (renal biopsy with class III or IV LN plus ANA ≥1:80 meets the ≥10-point classification threshold) [Rheumatology Advisor](https://www.rheumatologyadvisor.com/news/2019-eular-acr-recommendations-for-sle-classification-criteria/).

**Key identifiers:**
- **MONDO:** MONDO:0005556 [Wikidata](https://www.wikidata.org/wiki/Q1621830)
- **Parent disease (SLE) OMIM:** #152700 — Systemic Lupus Erythematosus [OMIM](https://omim.org/entry/152700) (no LN-specific OMIM entry exists; LN is coded as an SLE manifestation)
- **ICD-10-CM:** M32.14 (Glomerular disease in systemic lupus erythematosus); M32.15 (Tubulo-interstitial nephropathy in SLE); N08.5 (glomerular disorders in other systemic connective tissue disorders, when secondary coding is used) [ICD10Data](https://www.icd10data.com/ICD10CM/Codes/M00-M99/M30-M36/M32-/M32.14)
- **Orphanet:** No LN-specific ORPHA code exists; Orphanet aggregates all SLE organ manifestations under ORPHA:536 (Systemic lupus erythematosus); pediatric-onset SLE is separately coded ORPHA:93552 [Orphanet](https://www.orpha.net/en/disease/detail/536)
- **MeSH:** D008181 (Lupus Nephritis)
- **GARD/NIH Rare Disease entry:** GARD 10747 [GARD](https://rarediseases.info.nih.gov/diseases/10747/lupus-nephritis)

Notably, a 2026 *NDT* commentary argues that **active/refractory lupus nephritis functionally behaves as an orphan disease** given its rarity in clinical trials and limited approved-therapy landscape, despite lacking formal orphan designation [NDT](https://academic.oup.com/ndt/article/41/6/988/8514263).

**Synonyms:** SLE nephritis, lupus glomerulonephritis, LGN. Data underlying this report derive from aggregated disease-level resources (case series, registries, RCTs, GWAS meta-analyses) rather than individual EHR records, except where explicitly noted (e.g., single-institution biomarker cohorts).

---

## 2. Etiology

### Causal/risk factors — genetic

LN susceptibility is **polygenic**, shaped by common variants shared with SLE plus a smaller set of loci with LN-specific effect enrichment, and rare high-penetrance monogenic causes account for a minority of cases.

- **HLA region (chr 6p21):** Class II HLA alleles (e.g., HLA-DR2, DR3) are the strongest common SLE/LN susceptibility signals; GWAS of 2,000 unrelated European-ancestry women with SLE (588 with LN vs 1,412 without) identified nephritis-enriched MHC and non-MHC signals [PMC3135416](https://pmc.ncbi.nlm.nih.gov/articles/PMC3135416/).
- **STAT4:** SNP rs7582694 and linked variants show genome-wide-significant association with LN specifically (OR ~2.0–2.2, p as low as 3.76×10⁻²⁹ in case-control analysis) and with **severe renal insufficiency** in case-only analyses (OR 2.22, p=1.6×10⁻³) [PMC3873995](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3873995/), [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0084450).
- **IRF5:** Two near-perfectly linked SNPs (rs2070197, rs10488631; r²≈1.0) show strong LN association (p<1×10⁻⁴) [PMC8123735](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8123735/).
- **ITGAM/ITGAX (CD11b/CD11c, chr16):** Confirmed SLE/LN susceptibility locus from the landmark NEJM 2008 GWAS alongside BLK–C8orf13 [NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa0707865).
- **PXK, BLK, TNIP1, CARD11, IRAK1, PMS2:** Additional SNPs implicated in LN risk across case series; PXK is also a shared IgA nephropathy/SLE susceptibility gene (p=3.62×10⁻²⁴), suggesting convergent glomerular-injury pathways [PMC5090199](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5090199/).
- **Multi-ancestry GWAS meta-analysis (2023):** Cross-population SLE risk-score models now inform clinical risk prediction, relevant to LN given the strong genetic overlap [Nature Communications](https://www.nature.com/articles/s41467-023-36306-5).

**Rare, high-penetrance monogenic causes** (~1–2% of SLE/LN cases collectively):
- **Complete C1q deficiency:** >90% of individuals develop SLE or lupus-like disease; C1q-deficient patients present predominantly with **cutaneous and renal** involvement, and C1q gene SNPs specifically associate with LN in African American and Hispanic populations [PMC5186770](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5186770/), [PMC3467517](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3467517/).
- **C2, C4A, C4B complete deficiency:** Classical-pathway deficiencies impair immune-complex clearance, promoting SLE/LN.
- **C1s deficiency:** Documented case report of SLE with renal involvement in a male patient [PMC10925646](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10925646/).
- **TREX1 mutations:** ~0.5–3% of SLE patients carry TREX1 mutations (3′ repair exonuclease 1; loss of function causes accumulation of endogenous nucleic acids triggering cGAS-STING/type I interferon activation, linking TREX1-related SLE to the Aicardi-Goutières spectrum) [PMC3135416](https://pmc.ncbi.nlm.nih.gov/articles/PMC3135416/).

### Environmental risk factors
- **Sex:** Female predominance (SLE overall ~9:1 F:M), though male sex is a poor-prognosis marker specifically within LN cohorts (below).
- **Ancestry/race:** Non-European ancestry (Black, Hispanic, Asian, Indigenous) is the single strongest non-genetic-mechanistic risk modifier for LN development and severity (Section 9).
- **UV/photosensitivity:** Established SLE trigger; experimental models show UV-induced NETosis driving skin-and-kidney inflammatory flares.
- **Infections, smoking, silica exposure, certain drugs (hydralazine, procainamide — drug-induced lupus, generally without nephritis):** Established broader SLE environmental risk factors.

### Protective factors
Well-powered genetic/environmental *protective*-factor data specific to LN (as opposed to SLE broadly) are limited in the literature surveyed; no robust LN-specific protective allele or lifestyle factor emerged in this search. This is a **notable knowledge gap** worth flagging as `KNOWLEDGE_GAP` in the KB entry.

### Gene-environment interactions
UV exposure interacting with IFN-pathway risk alleles, and infection/complement-deficiency interactions impairing apoptotic-debris clearance, are the best-characterized GxE mechanisms, though LN-specific quantitative GxE studies were not identified in this literature pass beyond the general SLE literature.

---

## 3. Phenotypes

Suggested HPO terms and characteristics (renal-focused; broader SLE phenotypes such as malar rash, arthritis are typically modeled on the parent SLE entry rather than duplicated here):

| Phenotype | HPO term | Notes |
|---|---|---|
| Proteinuria | HP:0000093 | Hallmark presenting sign; nephrotic-range proteinuria in membranous (Class V) and diffuse proliferative (Class IV) disease |
| Nephrotic syndrome | HP:0000100 | Occurs especially in Class V and mixed III/IV+V |
| Hematuria | HP:0000790 | Microscopic common; gross hematuria less common |
| Glomerulonephritis | HP:0000099 | Umbrella histopathologic finding |
| Hypertension | HP:0000822 | Common at diagnosis and with CKD progression |
| Renal insufficiency / Stage 5 chronic kidney disease | HP:0003774 / HP:0003774-adjacent (CKD) | Progressive in undertreated/refractory disease |
| Elevated circulating antinuclear antibody level | HP:0033195 | Serologic biomarker |
| Reduced circulating complement C3/C4 | HP:0045081 (hypocomplementemia)/ related | Classic activity marker, though imperfect (Section 6/10) |
| Edema | HP:0000969 | Secondary to nephrotic syndrome |
| Acute kidney injury | HP:0001919 | In rapidly progressive/crescentic presentations |

**Onset/characteristics:** LN most commonly manifests within the first 1–3 years after SLE diagnosis (childhood-onset SLE has a markedly higher cumulative LN incidence — up to 70–80% — than adult-onset, ~30–60%). Severity and course are variable: Class III/IV (proliferative) disease is typically acute-to-subacute with active urinary sediment and rapid GFR decline if untreated; Class V (membranous) is more indolent, dominated by nephrotic-range proteinuria; mixed III/IV+V combines both patterns. Course can be **relapsing-remitting** (flares interspersed with remission) or **progressive** to CKD/ESRD despite therapy in 10–30% of severe cases within 15 years [PMC12565261](https://pmc.ncbi.nlm.nih.gov/articles/PMC12565261/).

**QoL impact:** Nephrotic syndrome, CKD progression, dialysis dependence, and the cumulative toxicity of long-term immunosuppression (infection risk, glucocorticoid morbidity, infertility risk with cyclophosphamide) substantially affect quality of life; pediatric-onset disease carries additional psychosocial and growth/development burden.

---

## 4. Genetic/Molecular Information

Covered largely under Etiology (Section 2). Summary for KB gene annotation purposes:

| Gene | HGNC | Role | Variant type |
|---|---|---|---|
| STAT4 | hgnc:11365 | Th1 differentiation, IFN-γ signaling | Common intronic risk SNPs (rs7582694 and linked) |
| IRF5 | hgnc:6119 | Type I IFN pathway transcription factor | Common risk SNPs (rs2070197, rs10488631) |
| ITGAM (CD11b) | hgnc:6149 | Complement receptor 3 subunit; leukocyte adhesion/phagocytosis | Common coding/regulatory risk variants |
| BLK | hgnc:1057 | B-cell receptor signaling (B lymphoid kinase) | C8orf13-BLK locus risk variants |
| PXK | hgnc:24500 | Endocytic trafficking | Risk SNP shared with IgA nephropathy |
| C1QA/B/C | hgnc:1241/1242/1243 | Classical complement pathway initiation | Complete deficiency (rare, high penetrance) |
| C2 | hgnc:1248 | Classical complement pathway | Complete deficiency |
| C4A/C4B | hgnc:1234/1235 | Classical complement pathway, immune complex clearance | Complete deficiency; copy-number variation |
| TREX1 | hgnc:12269 | 3′→5′ DNA exonuclease; suppresses cGAS-STING activation | Loss-of-function mutations |

**Functional consequences:** Complement-pathway loss-of-function → impaired clearance of apoptotic debris/immune complexes → chronic autoantigen exposure. TREX1 loss-of-function → cytosolic ssDNA/dsDNA accumulation → cGAS-STING-driven type I interferon production. STAT4/IRF5 gain-of-risk-allele effects amplify Th1/IFN signaling, intensifying renal inflammatory infiltration.

**Somatic vs germline:** LN genetic risk is essentially entirely **germline**; no somatic mosaicism/clonal mechanism is established.

**Epigenetics:** DNA hypomethylation of IFN-response genes in T cells is a well-described SLE epigenetic signature (broader SLE literature); LN-specific epigenetic/DiseaseMeth data were not surfaced in this pass and represent a further gap to verify with a dedicated search of ENCODE/DiseaseMeth if curating an epigenetics subsection.

---

## 5. Environmental Information

- **UV radiation:** Established trigger for cutaneous and systemic flares, mechanistically linked to keratinocyte apoptosis, autoantigen exposure, and NETosis-driven flares affecting both skin and kidney in murine models [bioRxiv preprint noted above].
- **Infections:** Viral (EBV) and bacterial triggers implicated in broader SLE pathogenesis via molecular mimicry and bystander immune activation; no LN-specific infectious trigger was identified as distinct from general SLE literature in this search pass.
- **Smoking, silica, and occupational/toxin exposures:** Established general SLE risk factors; specific LN-stratified toxicological data were not located in this pass (a CTD/TOXNET-focused follow-up search would be needed for LN-specific quantification).
- **Socioeconomic/structural factors:** Poverty, healthcare access disparities, and discrimination are explicitly implicated as contributors — independent of genetics — to worse LN outcomes in non-White populations [Duke Scholars](https://scholars.duke.edu/publication/1159060), [ScienceDirect Disparities](https://www.sciencedirect.com/science/article/pii/S1521694223000803).

---

## 6. Mechanism / Pathophysiology

### Causal chain (upstream → downstream)

1. **Loss of immune tolerance / autoantibody generation** (upstream, systemic): Genetic susceptibility (HLA, STAT4, IRF5, complement/TREX1 lesions) plus environmental triggers (UV, infection) drive loss of B-cell tolerance to nuclear antigens. Autoreactive B cells differentiate into long-lived plasma cells producing sustained anti-dsDNA and anti-nucleosome antibodies; CD4+ Th1/Th17 cells provide help and amplify inflammatory cytokine production [BMC Nephrology](https://bmcnephrol.biomedcentral.com/articles/10.1186/s12882-025-04434-3).
2. **Immune complex formation and glomerular deposition** (organ-entry point): Circulating and in situ–formed immune complexes (anti-dsDNA/chromatin bound to glomerular basement membrane components) deposit in mesangial, subendothelial, and/or subepithelial compartments, determining the ISN/RPS histologic class.
3. **Complement activation** (amplification): Immune complexes engage C1q, activating the **classical pathway**; the **alternative pathway amplification loop** further boosts complement deposition. Terminal complement components (**C5a, C5b-9/MAC**) trigger acute cellular inflammatory responses via cytokine/interleukin signaling cascades. Emerging work also describes **noncanonical intracellular complement functions** regulating immune-cell metabolism [ScienceDirect Complement Review 2025](https://www.sciencedirect.com/science/article/pii/S0952791525001311).
4. **Type I interferon (IFN-I) pathway activation**: IFN-I transcripts are overexpressed in renal biopsy tissue from proliferative LN, with elevated neutrophil-derived defensin-α3 transcripts implicating **neutrophil extracellular traps (NETs)** as a local IFN-I driver within the kidney [Rheumatology (Oxford) PMID:36355567](https://pubmed.ncbi.nlm.nih.gov/36355567/). NETs also promote further complement activation and autoantigen exposure, creating a self-amplifying inflammatory loop.
5. **Cellular infiltration and injury**: CD4+ T cells (Th1/Th17), infiltrating B cells (including an age-associated B-cell subset identified by scRNA-seq), monocyte/macrophage populations at progressive differentiation stages, and neutrophils accumulate in the kidney interstitium and glomeruli, producing pro-inflammatory cytokines, ROS, and proteolytic enzymes [Nature Immunology PMID (AMP consortium)](https://www.nature.com/articles/s41590-019-0398-x).
6. **Podocyte and tubular epithelial injury**: Podocyte foot-process effacement and podocyte loss (nephrin loss demonstrated in NZM2410 mice) drive proteinuria; sustained proteinuria and ischemia further injure podocytes and tubular epithelium, and podocyte–tubular epithelial–immune cell crosstalk sustains chronicity [Frontiers in Immunology 2025](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1682075/full).
7. **Chronic tissue remodeling / fibrosis** (downstream, irreversible endpoint): Interstitial fibrosis and tubular atrophy (captured by the ISN/RPS chronicity index) mark irreversible nephron loss, culminating in progressive CKD/ESRD in a subset of patients.

### Cell types (CL terms)
- Glomerular podocyte — CL:1000452 (or CL:0000653 podocyte)
- Mesangial cell — CL:0000650
- Glomerular endothelial cell — CL:1000450
- Plasma cell — CL:0000786
- Age-associated B cell subset (ABC) — CL:0000236 (B cell, more specific subset term not formally in CL)
- Th1/Th17 CD4+ T cell — CL:0000545 / CL:0000899
- Neutrophil — CL:0000775
- Monocyte/macrophage (kidney-infiltrating) — CL:0000576/CL:0000235
- Renal tubular epithelial cell — CL:1001285 or CL:0002518

### Biological processes (GO terms)
- Complement activation, classical pathway — GO:0006958
- Complement activation, alternative pathway — GO:0006957
- Type I interferon signaling pathway — GO:0060337
- Neutrophil extracellular trap formation — GO:0140448 (NETosis)
- Immune complex clearance/response — GO:0002455 (Fc-receptor mediated immune complex signaling context)
- Podocyte apoptotic process — GO:1990009 (renal podocyte process)
- Renal fibrosis / response to injury — GO:0072028 (renal tubule morphogenesis) or fibrosis-related GO terms

### Molecular profiling
- **Transcriptomics:** The 2019 AMP (Accelerating Medicines Partnership) SLE Network scRNA-seq studies produced the first comprehensive human LN kidney immune-cell atlas (21 leukocyte subsets) [Nature Immunology](https://www.nature.com/articles/s41590-019-0398-x); murine transcriptomic comparisons across MRL/lpr, NZB/W, and BXSB/Yaa reveal both unique and shared regulatory networks [PLOS ONE PMC3805607](https://pmc.ncbi.nlm.nih.gov/articles/PMC3805607/).
- **Spatial transcriptomics:** Childhood-onset LN spatial profiling reveals complex kidney stroma–immune cell interactions, addressing the spatial-information loss inherent to dissociative scRNA-seq [PMC10680641](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10680641/); murine imiquimod-induced LN spatial transcriptomics elucidates renal fibrosis mechanisms [ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S2405580825001748).
- **mTOR pathway:** Cross-species mapping shows shared mTOR pathway perturbations between mouse LN models and human LN [PMC2656226](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2656226/).

### Immune system involvement
LN is fundamentally an autoimmune/immune-complex disease combining humoral autoimmunity (autoantibody/immune complex formation), complement-mediated tissue injury, and cell-mediated (T cell, NET-driven) inflammation — a multi-arm immunopathology rather than a single-pathway process.

---

## 7. Anatomical Structures Affected

- **Primary organ:** Kidney (UBERON:0002113), specifically the renal glomerulus (UBERON:0000074), renal cortex, and tubulointerstitium (UBERON:0001225/renal tubule).
- **Secondary/systemic involvement:** As an SLE manifestation, LN co-occurs with skin (malar rash, discoid lesions), joints (arthritis), serosa (pleuritis, pericarditis), CNS (neuropsychiatric lupus), and hematologic (cytopenias) involvement — modeled on the parent SLE entry.
- **Cell/tissue level:** Glomerular basement membrane (immune complex deposition site), mesangium, glomerular capillary endothelium, podocytes (visceral epithelial cells), tubular epithelium, peritubular capillaries, and renal vasculature (lupus vasculopathy/vasculitis in some cases).
- **Subcellular:** Glomerular basement membrane (extracellular matrix compartment); podocyte foot processes/slit diaphragm (GO Cellular Component: GO:0097610 filtration slit); mitochondria and cytosol relevant to TREX1/cGAS-STING nucleic-acid-sensing pathway.
- **Localization/laterality:** Bilateral, diffuse (typically both kidneys symmetrically involved; focal vs diffuse relates to the proportion of glomeruli affected per the ISN/RPS classification, not laterality between kidneys).

---

## 8. Temporal Development

- **Onset:** Can occur at any SLE disease stage but most often within the first few years after SLE diagnosis; can rarely be the presenting SLE manifestation. Onset pattern ranges from insidious (Class V/membranous) to acute/rapidly progressive (crescentic Class IV).
- **Staging (histologic, ISN/RPS 2018):** Class I (minimal mesangial), Class II (mesangial proliferative), Class III (focal, <50% glomeruli), Class IV (diffuse, ≥50% glomeruli; segmental IV-S or global IV-G), Class V (membranous), Class VI (advanced sclerosing, ≥90% globally sclerosed glomeruli). The 2018 revision replaced subclasses A/C/A+C with NIH-derived **activity index (AI)** and **chronicity index (CI)** semiquantitative scores, emphasizing tubulointerstitial lesions; interstitial inflammation within this framework independently predicts renal outcome [PMC10085727](https://pmc.ncbi.nlm.nih.gov/articles/PMC10085727/), [PubMed 33682052](https://pubmed.ncbi.nlm.nih.gov/33682052/).
- **Progression rate/course:** Variable — relapsing-remitting is common; 10–30% of severe LN progresses to ESRD within 15 years despite aggressive immunosuppression [PMC12565261](https://pmc.ncbi.nlm.nih.gov/articles/PMC12565261/). In pediatric-onset severe LN, patients who progress to ESRD reach CKD stage 3 at a median of 3.2 years post-diagnosis, versus 8 years for the overall severe-LN cohort [PMC11985274](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985274/).
- **Remission patterns:** Complete/partial renal response is the standard trial endpoint (proteinuria reduction, stable/improved eGFR); remission can be treatment-induced (rarely spontaneous) and is a key predictor of long-term renal survival — failure to achieve remission by 12 months predicts advanced CKD in pediatric cohorts.
- **Critical periods:** Early, aggressive induction therapy within the first weeks-to-months of active proliferative disease is considered the critical intervention window to prevent irreversible glomerulosclerosis/fibrosis.

---

## 9. Inheritance and Population

### Epidemiology
- LN prevalence among people with SLE is markedly race/ethnicity-stratified: **53.2% in Asian**, **50.7% in Black**, **49.4% in Hispanic**, vs **25.4% in White** SLE patients [MyLupusTeam summary of literature](https://www.mylupusteam.com/resources/4-ways-race-impacts-sle-treatment-and-severity).
- Population-level LN prevalence per 100,000: **African American 59.69**, **Asian 56.56**, **Hispanic 29.84**, **White 15.83** [ScienceDirect African American disparities](https://www.sciencedirect.com/science/article/abs/pii/S0027968422000864).
- Hazard ratios for developing LN after SLE diagnosis (vs. White): **African American HR 2.3**, **Asian HR 4.3**, **Hispanic HR 2.4**.
- Progression to kidney failure is **~9-fold greater in African American** vs White patients with LN.

### Inheritance pattern
LN/SLE is **multifactorial/polygenic** for the vast majority of patients (not classic Mendelian), with rare **autosomal recessive monogenic forms** (complete complement component deficiencies — C1q, C2, C4 — and TREX1-related interferonopathy) that can behave in a near-Mendelian, highly penetrant fashion (>90% penetrance for complete C1q deficiency). No AD, X-linked, or mitochondrial inheritance pattern is established for LN specifically. Genetic anticipation, founder effects specific to LN (as distinct from SLE broadly), and consanguinity data were not surfaced in this literature pass — appropriate to flag as a further gap if precise quantification is needed for the KB `Inheritance` block.

### Demographics
- **Sex ratio:** Female predominant, consistent with SLE overall (~9:1).
- **Age distribution:** Peaks in women of reproductive age (child-bearing years); childhood-onset (pediatric) LN carries a worse prognosis than adult-onset, and disease onset in advanced age also shows distinct (generally milder but comorbidity-complicated) outcomes per pediatric-vs-adult-vs-advanced-age-onset comparative studies [PMC11966454](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11966454/).
- **Geographic distribution:** Global; highest burden aligns with populations of African, Asian, and Hispanic/Indigenous ancestry regardless of geography, consistent with genetic-ancestry-linked risk rather than a purely geographic/endemic pattern.

---

## 10. Diagnostics

### Clinical tests
- **Urinalysis/urine sediment:** Active sediment (dysmorphic RBCs, RBC casts, cellular casts) signals proliferative disease activity.
- **Proteinuria quantification:** Urine protein:creatinine ratio (UPCR) is the standard quantitative/trial endpoint measure.
- **Serologic biomarkers:** Anti-dsDNA antibody titer and complement C3/C4 are the conventional activity markers with the strongest clinical evidence base, though only **moderate** discriminative performance for predicting LN, flares, and treatment response [PMC12565261](https://pmc.ncbi.nlm.nih.gov/articles/PMC12565261/).
- **Novel urinary biomarkers (outperforming conventional markers in several cohorts):**
  - **ALCAM (activated leukocyte cell adhesion molecule):** AUC 0.75–0.83 for renal/SLE disease activity, best cSLE discriminator in Bayesian network analysis [PMC7251704](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7251704/), [PMC9204340](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9204340/).
  - **VCAM-1:** AUC 0.77–0.88.
  - **MCP-1 (CCL2):** AUC 0.79 [PMC12088007](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12088007/).
  - **PF4, hemopexin, sCD163, CXCL10, NGAL, TWEAK, uric acid:** Additional candidates with good LN-vs-non-renal-SLE discriminative ability.
  - **Neuropilin-1 (urinary):** Predictive of renal outcome [PMC6769814](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6769814/).
- **Complement fixed/functional assays and non-canonical complement markers:** anti-C1q, anti-ficolin, anti-C1s antibodies, and tissue-based renal **C4d** and **C5b-9** deposits are discussed as improved activity/prognosis markers beyond CH50/C3/C4 [ScienceDirect Complement 2025](https://www.sciencedirect.com/science/article/pii/S0952791525001311).
- **Renal biopsy (definitive diagnostic test):** Required for ISN/RPS histologic classification, activity/chronicity index scoring, and to distinguish LN from other glomerulopathies. Full-house immunofluorescence staining (IgG, IgA, IgM, C3, C1q, kappa, lambda all positive) with strong C1q staining is characteristic of LN and helps distinguish it from other glomerulonephritides [PMC11640231](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11640231/).

### Genetic testing
Not routinely used for diagnosis of typical polygenic LN; targeted **complement pathway (C1q, C2, C4) and TREX1 testing** may be considered in atypical presentations (very early onset, family history, disproportionate cutaneous/renal phenotype) suggestive of monogenic lupus/interferonopathy.

### Clinical/classification criteria
- **2019 EULAR/ACR SLE classification criteria:** Entry criterion = ANA ≥1:80; renal biopsy showing Class III/IV LN contributes 10 points (Class II/V contributes 8 points), sufficient alone (with positive ANA) to classify SLE. High sensitivity for LN-containing SLE cohorts; the criteria's renal-domain weighting reaffirms the centrality of biopsy [Rheumatology Advisor](https://www.rheumatologyadvisor.com/news/2019-eular-acr-recommendations-for-sle-classification-criteria/); the 2019 score also predicts subsequent renal flare risk [Renal and Urology News](https://www.renalandurologynews.com/news/2019-eular-acr-criteria-lupus-nephritis-diagnosis-flare-risk/).
- **ISN/RPS 2018 histopathologic classification** (Section 8) is the diagnostic/prognostic gold standard once biopsy is obtained.

### Screening
No population-level newborn or carrier screening applies (LN is not classically Mendelian); however, **all SLE patients are recommended for periodic urinalysis/proteinuria screening** to detect subclinical renal involvement early, and biopsy is recommended for any SLE patient with new proteinuria (typically UPCR threshold ≥0.5 g/g) or active urinary sediment per KDIGO guidance.

---

## 11. Outcome/Prognosis

- **ESRD risk:** 10–30% of severe LN patients progress to ESRD within 15 years despite modern immunosuppressive therapy [PMC12565261](https://pmc.ncbi.nlm.nih.gov/articles/PMC12565261/).
- **Pediatric-specific:** In one severe-LN cohort, 28/95 (≈29%) progressed to ESRD; those progressing reached CKD stage 3 at a median 3.2 years post-diagnosis vs 8 years for the overall cohort; 14.8% developed advanced CKD at last follow-up [PMC11985274](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985274/). Childhood-onset LN carries a **worse renal prognosis than adult-onset** disease, though outcomes have improved substantially over three decades of evolving therapy [Springer/CJASN PMID 21799148](https://pubmed.ncbi.nlm.nih.gov/21799148/).
- **Prognostic risk factors:** Rapidly progressive glomerulonephritis, non-response to induction treatment, severe kidney flare, male sex, failure to achieve remission by 12 months, hypertension, neurologic involvement, treatment non-compliance, and lower eGFR at diagnosis all predict adverse kidney outcomes in pediatric cohorts [PMC11985274](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985274/); serositis is a broader marker of poor pediatric SLE prognosis [PMC11959889](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11959889/).
- **Renal vascular lesions** (a distinct pathologic feature beyond the standard ISN/RPS glomerular classes) are recognized as an independent contributor to poor outcomes in childhood-onset LN [PMC11584461](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11584461/).
- **Race disparities in mortality:** Black patients with SLE/LN are more likely to die of the disease, and the average age of SLE-related death is significantly younger in Black patients than White patients [PMC11815449](https://pmc.ncbi.nlm.nih.gov/articles/PMC11815449/).
- **Pregnancy-related outcome data:** Preeclampsia occurs in **25.7%** of LN pregnancies vs 2.9% of non-renal-lupus pregnancies; preterm birth (<37 weeks) in 25.7% vs 7.5%; preeclampsia occurred in 66.7% of preterm LN deliveries [PMC8120629](https://pmc.ncbi.nlm.nih.gov/articles/PMC8120629/). History of renal flare, hypertension, and longer disease duration predict preeclampsia/HELLP; adverse maternal outcomes are often reversible with prompt diagnosis/treatment [Kidney Medicine](https://www.kidneymedicinejournal.org/article/S2590-0595(23)00142-5/fulltext).

---

## 12. Treatment

### Pharmacotherapy — approved agents (with MAXO/therapeutic-agent mapping guidance)
Three drugs are now FDA-approved specifically for lupus nephritis (in addition to background mycophenolate/cyclophosphamide + glucocorticoid standard-of-care), reflecting rapid label expansion 2020–2025:

1. **Belimumab (2020 approval)** — anti-BAFF/BLyS monoclonal antibody (`therapeutic_modality: MONOCLONAL_ANTIBODY`; NCIT drug-class term available). **BLISS-LN trial** (NEJM 2020;383(12):1117-1128, PMID available via DOI 10.1056/NEJMoa2001180): phase 3, 104-week, RCT of belimumab 10 mg/kg + standard therapy vs standard therapy alone in 448 patients across 107 sites/21 countries; belimumab arm had significantly higher primary efficacy renal response rate [NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa2001180). Post-hoc analyses show belimumab most effective in proliferative LN with baseline UPCR <3 g/g, reducing risk of renal events/death and LN flare [Kidney International](https://www.kidney-international.org/article/S0085-2538(21)00862-0/fulltext).
2. **Voclosporin (LUPKYNIS, 2021 approval)** — calcineurin inhibitor (CNI) (`therapeutic_modality: SMALL_MOLECULE`). **AURORA 1 trial** (Lancet 2021;397(10289):2070-2080, **PMID:33971155**): phase 3, 142 sites/27 countries, patients with biopsy-proven Class III/IV (±V) LN; voclosporin + MMF + low-dose steroids achieved a clinically/statistically superior complete renal response vs MMF + low-dose steroids alone, comparable safety, most common AEs infections (pneumonia most serious) [ScienceDirect/Lancet](https://www.sciencedirect.com/science/article/abs/pii/S014067362100578X).
3. **Obinutuzumab (2025 approval — third-ever LN-specific drug)** — type II anti-CD20 monoclonal antibody (`therapeutic_modality: MONOCLONAL_ANTIBODY`). **REGENCY trial**: complete renal response at 76 weeks in 46.4% (obinutuzumab, n=135) vs 33.1% (placebo, n=136), all patients on background MMF + oral prednisone (target 5 mg/d by week 24) [Medscape](https://www.medscape.com/viewarticle/fda-approves-third-ever-drug-lupus-nephritis-2025a1000sh4); post hoc analysis in *Arthritis & Rheumatology* 2024 confirms preserved kidney function/outcomes [Wiley A&R](https://acrjournals.onlinelibrary.wiley.com/doi/10.1002/art.42734).

### Investigational / emerging
- **Anifrolumab (anti-type I IFN receptor mAb, SAPHNELO):** Phase 2 **TULIP-LN** trial (147 randomized) tested an intensified regimen (900 mg IV ×3 then 300 mg) vs basic regimen vs placebo; intensified regimen showed higher complete renal response through Year 2 extension (PMID:37607780) [PubMed](https://pubmed.ncbi.nlm.nih.gov/37607780/). An optimized, longer intensified dosing regimen (6× 900 mg Q4W then 300 mg) was selected for the ongoing **Phase 3 IRIS trial** (NCT05138133), estimated primary completion 2027 [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT05138133); dose-selection rationale published 2026 in *Clinical Pharmacology & Therapeutics* [Wiley CPT](https://ascpt.onlinelibrary.wiley.com/doi/10.1002/cpt.70307?af=R).
- **Complement inhibitors:** Ravulizumab (anti-C5) and ALXN2050 (alternative-pathway factor D inhibitor) are in trials for proliferative LN/IgA nephropathy [ClinicalTrials.gov NCT04564339](https://cdn.clinicaltrials.gov/large-docs/39/NCT04564339/Prot_000.pdf), [NCT05097989](https://cdn.clinicaltrials.gov/large-docs/89/NCT05097989/Prot_000.pdf).
- **CAR-T cell therapy (rapidly emerging, 2024–2025):** Autologous and allogeneic **anti-CD19 CAR-T** therapy achieves deep peripheral and renal B-cell depletion and durable clinical remission in refractory SLE/LN case series — e.g., a Cleveland Clinic LN patient in drug-free remission >1 year post-infusion [Cleveland Clinic](https://consultqd.clevelandclinic.org/case-car-t-cell-therapy-for-lupus-patient-with-kidney-involvement); allogeneic CD19 CAR-T achieved durable remission with no GvHD/CRS/ICANS in a small cohort (PMID:40446794) [PubMed](https://pubmed.ncbi.nlm.nih.gov/40446794/); **CTA313** (dual CD19/BCMA-targeting, depleting both autoreactive B cells and long-lived plasma cells) showed early efficacy signals in a 7-patient trial [Frontiers 2024](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1476859/full). Dedicated CD19/BCMA CAR-T trials for refractory/relapsed LN are recruiting (NCT06785519, NCT06681337) [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06785519).
- **Combination/triple therapy trial:** **PRESERVE** trial (NCT07611214) testing voclosporin + belimumab, obinutuzumab, or anifrolumab combinations for rapid renal response [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT07611214).

### Guideline-based treatment strategy
**KDIGO 2024 Clinical Practice Guideline** (focused update of KDIGO 2021 glomerular diseases guideline, published *Kidney International* supplements, January 2024) [KDIGO PDF](https://kdigo.org/wp-content/uploads/2024/01/KDIGO-2024-Lupus-Nephritis-Guideline.pdf):
- Active Class III/IV LN (±membranous component) should be treated initially with glucocorticoids **plus** one of: MMF, MMF+belimumab, MMF+CNI (including voclosporin), or cyclophosphamide.
- **Triple immunosuppressive regimens** (MMF + belimumab or CNI, added to standard therapy) are recommended particularly for patients with poor prognostic factors and severe proteinuria, given the rapid proteinuria reduction seen with CNIs; patients responding to triple induction can continue triple regimens into maintenance.
- EULAR guidance has incorporated **MMF + obinutuzumab** as an additional initial-treatment option following REGENCY data [Renal & Urology summary of recent advances](https://doi.org/10.1080/25785826.2025.2610582).

### MAXO term suggestions
- `MAXO:0000647` chemotherapy (cyclophosphamide induction)
- `NCIT:C15986` Pharmacotherapy (paired with `therapeutic_agent` for belimumab, voclosporin, obinutuzumab, anifrolumab, mycophenolate, glucocorticoids)
- `MAXO:0010039` organ transplantation (kidney transplant for ESRD)
- `MAXO:0000950` supportive care (RAAS blockade/antihypertensives for proteinuria/hypertension management, hydroxychloroquine as background SLE therapy)

---

## 13. Prevention

- **Primary prevention:** No disease-specific primary prevention exists for LN itself; general SLE risk-reduction advice (UV protection/sun avoidance, smoking cessation) is the closest analog, extrapolated from broader SLE literature.
- **Secondary prevention (early detection):** Routine urinalysis/proteinuria screening in all SLE patients to catch subclinical renal involvement before irreversible damage; low threshold for renal biopsy with new proteinuria or active sediment.
- **Tertiary prevention:** Hydroxychloroquine background therapy (reduces flare frequency/renal flare risk across SLE), RAAS blockade (ACEi/ARB) for proteinuria reduction and nephroprotection, aggressive blood pressure control, and vaccination/infection-prophylaxis given long-term immunosuppression burden.
- **Pregnancy planning/counseling:** Given the markedly elevated preeclampsia/preterm-birth risk in LN pregnancies, preconception counseling emphasizing disease quiescence (≥6 months remission recommended before conception in general SLE/LN practice) and close obstetric-rheumatology co-management is a key preventive strategy [Kidney Medicine](https://www.kidneymedicinejournal.org/article/S2590-0595(23)00142-5/fulltext).
- **Genetic counseling:** Relevant primarily in rare monogenic complement-deficiency or TREX1-related interferonopathy presentations, where family screening may be considered.

---

## 14. Other Species / Natural Disease

Spontaneous natural LN-like disease in domestic animals is not well-characterized as a distinct veterinary entity in the literature surveyed (unlike, e.g., canine SLE-like syndromes reported anecdotally in veterinary case series); this represents a gap relative to OMIA/veterinary-database cross-referencing that was not resolved in this search pass. The primary cross-species relevance of LN is via **engineered/spontaneous murine models** (below), not naturally occurring disease in companion or wild species.

---

## 15. Model Organisms

Murine models are the dominant and best-validated model system for LN mechanistic and preclinical therapeutic research:

- **NZB/W F1 (New Zealand Black × New Zealand White)** and derivative substrains **NZM2410, NZM 2328**: Classic spontaneous lupus nephritis models with high circulating type I IFN, autoantibody production, and lupus nephritis; NZM2410 mice show **podocyte nephrin loss**, directly recapitulating human podocyte injury [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0077489).
- **MRL/lpr (Fas-signaling-deficient)**: Spontaneous, accelerated lupus-like disease with lymphoproliferation and nephritis; IFN-inducible gene upregulation correlates with disease progression, though the causal role of IFN-α in this strain remains **controversial/unresolved** (a candidate `HUMAN_MODEL_MISMATCH` consideration for KB curation) [Nature Scientific Reports](https://www.nature.com/articles/srep20373).
- **BXSB/Yaa**: Y-chromosome-linked autoimmune acceleration (duplicated TLR7 locus) driving male-predominant severe lupus nephritis (notably reversing the usual female-predominant sex bias, a distinctive model feature).
- **IFN-α-accelerated NZB/W model**: Exogenous IFN-α administration synchronizes onset and accelerates progression, useful for shortened preclinical study timelines; blood transcriptome analysis of this accelerated model shows interferon, plasma cell, neutrophil, T-cell, and protein-synthesis signatures mirroring human disease [PMC5070861 context / general model literature].
- **Pristane-induced (SWR×NZB) F1 model**: Produces prominent **tubulointerstitial inflammation and fibrosis** closely resembling human LN-like fibrotic patterns, useful specifically for studying the chronic/fibrotic endpoint of LN [PMC5070861](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5070861/).
- **Imiquimod-induced (TLR7 agonist) model**: Inducible model recently profiled by single-cell spatial transcriptomics to dissect renal fibrosis mechanisms [ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S2405580825001748).
- **AAV (adeno-associated virus)-induced LN models**: Newer inducible/engineered approach for generating lupus nephritis phenotypes in mice with more controlled onset kinetics [Inotiv](https://www.inotiv.com/solutions/aav-induced-lupus-nephritis-in-mice).
- **Cross-model transcriptomic comparison**: Comparative profiling across three murine LN models reveals both shared (core inflammatory/IFN) and model-specific regulatory networks, informing which findings are likely to generalize to human disease vs. being strain-idiosyncratic [PLOS ONE / PMC3805607](https://pmc.ncbi.nlm.nih.gov/articles/PMC3805607/); shared **mTOR pathway perturbations** between mouse models and human LN have also been mapped directly [PMC2656226](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2656226/).

**Model limitations:** No single murine model fully recapitulates the human ISN/RPS histologic spectrum, the race/ethnicity-linked severity disparities, or human-specific complement/HLA haplotype effects — a translational caveat worth flagging (`HUMAN_MODEL_MISMATCH`) especially for IFN-α's causal-vs-correlative role in MRL/lpr disease and for any claim extrapolating murine podocyte/fibrosis mechanisms directly to human treatment response without confirmatory human kidney biopsy/spatial-transcriptomic data.

---

## Summary Table: Suggested Evidence Anchors for KB Curation

| Claim | PMID/Reference | Evidence type |
|---|---|---|
| BLISS-LN belimumab efficacy | NEJM 2020;383(12):1117-1128 (DOI 10.1056/NEJMoa2001180) | HUMAN_CLINICAL |
| AURORA 1 voclosporin efficacy | PMID:33971155 (Lancet 2021;397:2070-2080) | HUMAN_CLINICAL |
| REGENCY obinutuzumab efficacy | Arthritis & Rheumatology 2024, DOI 10.1002/art.42734 | HUMAN_CLINICAL |
| TULIP-LN anifrolumab Year 2 extension | PMID:37607780 | HUMAN_CLINICAL |
| STAT4 renal insufficiency association | PMC3873995 / PLOS ONE PMID (rs7582694) | HUMAN_CLINICAL (genetic) |
| C1q deficiency SLE/LN penetrance | PMC5186770 | HUMAN_CLINICAL (genetic) |
| ITGAM/BLK GWAS | NEJM 2008 (PMID:18768667, NEJMoa0707865) | HUMAN_CLINICAL (genetic) |
| Type I IFN/neutrophil transcripts in LN biopsy | PMID:36355567 (Rheumatology 2023;62:2534) | HUMAN_CLINICAL |
| AMP kidney immune-cell landscape scRNA-seq | Nature Immunology 2019 (PMID:31209404-adjacent) | HUMAN_CLINICAL / molecular |
| LN race/ethnicity prevalence disparities | ScienceDirect S0027968422000864; PMC11815449 | HUMAN_CLINICAL (epidemiology) |
| Preeclampsia risk in LN pregnancy | PMC8120629 | HUMAN_CLINICAL |
| ISN/RPS 2018 classification revision | PMID:33682052 | HUMAN_CLINICAL |
| Pediatric LN ESRD progression timeline | PMC11985274 | HUMAN_CLINICAL |
| NZM2410 podocyte nephrin loss | PLOS ONE PMC3805607 | MODEL_ORGANISM |
| CAR-T CD19 durable remission in LN | PMID:40446794 | HUMAN_CLINICAL |

---

### Notes on Gaps for Curators
1. **Protective genetic/environmental factors** specific to LN (vs. general SLE) were not well-represented in available literature — flag as `KNOWLEDGE_GAP`.
2. **Veterinary/naturally-occurring LN in other species** is sparse; no OMIA-indexed entry surfaced.
3. **cGAS-STING pathway** mechanistic detail specific to LN kidney tissue (vs. TREX1-driven SLE broadly) merits a dedicated follow-up search before finalizing pathway-level pathophysiology nodes.
4. **IFN-α's causal role in MRL/lpr** is explicitly described in the literature as controversial — a strong candidate for a `HUMAN_MODEL_MISMATCH` discussion node rather than treating murine IFN data as directly confirmatory of human mechanism.

---

### Sources
- [New Insights on Childhood Lupus Nephritis (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11740589/)
- [Complement in SLE across time and space (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0952791525001311)
- [Harnessing T-cell therapy for lupus nephritis (SAGE 2025)](https://journals.sagepub.com/doi/10.1177/09636897251371114)
- [Disease modification in lupus nephritis (Nat Rev Nephrol)](https://www.nature.com/articles/s41581-026-01103-y)
- [Taming renal inflammation (BMC Nephrology)](https://bmcnephrol.biomedcentral.com/articles/10.1186/s12882-025-04434-3)
- [A pathophysiology-based approach (Kidney International)](https://www.kidney-international.org/article/S0085-2538(16)30208-3/fulltext)
- [Genetic susceptibility to SLE in the genomic era (PMC3135416)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3135416/)
- [C1q Deficiency and Neuropsychiatric SLE (PMC5186770)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5186770/)
- [Complement C1s deficiency case report (PMC10925646)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10925646/)
- [Complement deficiencies and SLE susceptibility revisited (PMC3467517)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3467517/)
- [Novel RGS1/RASGRP1 associations, IgAN (PMC5090199)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5090199/)
- [Histologic evaluation of activity/chronicity (PMC10085727)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10085727/)
- [ISN/RPS 2018 vs 2003 classification comparison (PMC7640657)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7640657/)
- [Revised ISN/RPS 2018 predicts remission (PubMed 33682052)](https://pubmed.ncbi.nlm.nih.gov/33682052/)
- [ISN/RPS 2016 classification predicts prognosis (PMC7810677)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7810677/)
- [FDA Approves Third Drug for Lupus Nephritis (Medscape)](https://www.medscape.com/viewarticle/fda-approves-third-ever-drug-lupus-nephritis-2025a1000sh4)
- [PRESERVE combination trial NCT07611214](https://clinicaltrials.gov/study/NCT07611214)
- [NOBILITY post hoc obinutuzumab analysis (Wiley A&R)](https://acrjournals.onlinelibrary.wiley.com/doi/10.1002/art.42734)
- [KDIGO 2024 Executive Summary](https://kdigo.org/wp-content/uploads/2024/01/KDIGO-2024-Lupus-Nephritis-Guideline_Executive-Summary.pdf)
- [KDIGO 2024 Full Guideline](https://kdigo.org/wp-content/uploads/2024/01/KDIGO-2024-Lupus-Nephritis-Guideline.pdf)
- [Efficacy/safety obinutuzumab (PMC12214873)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12214873/)
- [Recent advances immunosuppressive therapy LN (2025)](https://doi.org/10.1080/25785826.2025.2610582)
- [Lupus statistics by race (MyLupusTeam)](https://www.mylupusteam.com/resources/4-ways-race-impacts-sle-treatment-and-severity)
- [Reframing health disparities in SLE (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1521694223000803)
- [Race/ethnicity and mortality meta-analysis (PMC11815449)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11815449/)
- [Lupus nephritis disparities affecting African Americans (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0027968422000864)
- [Urine ALCAM/PF4/VCAM-1 childhood LN (PMC9204340)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9204340/)
- [Biomarkers in Lupus Nephritis review (PMC12565261)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12565261/)
- [Urinary ALCAM as biomarker (PMC7251704)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7251704/)
- [Urinary Neuropilin-1 (PMC6769814)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6769814/)
- [Urinary MCP-1/VCAM-1 biomarkers (PMC12088007)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12088007/)
- [Comparative transcriptional profiling murine SLE models (PMC3805607)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3805607/)
- [Pristane-accelerated (SWR×NZB)F1 fibrosis model (PMC5070861)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5070861/)
- [Fli-1 IL-17A MRL/lpr model (PMC7140643)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7140643/)
- [pDC alterations in lupus-prone mice (Sci Reports)](https://www.nature.com/articles/srep20373)
- [mTOR pathway mapping mouse/human LN (PMC2656226)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2656226/)
- [STAT4/IRF5/renal biopsy Vietnam cohort (PMC8123735)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8123735/)
- [STAT4 severe renal insufficiency (PMC3873995)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3873995/)
- [ITGAM/ITGAX BLK NEJM GWAS](https://www.nejm.org/doi/full/10.1056/NEJMoa0707865)
- [STAT4 polymorphism PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0084450)
- [Multi-ancestry SLE GWAS meta-analysis (Nat Commun)](https://www.nature.com/articles/s41467-023-36306-5)
- [Allogeneic CD19 CAR-T durable remission (Med/Cell Press)](https://www.cell.com/med/abstract/S2666-6340(25)00176-X)
- [IM19 CAR-T pilot study (Annals Rheum Dis)](https://ard.eular.org/article/S0003-4967(25)04608-4/abstract)
- [Cleveland Clinic CAR-T LN case](https://consultqd.clevelandclinic.org/case-car-t-cell-therapy-for-lupus-patient-with-kidney-involvement)
- [Allogeneic CD19 CAR-T PubMed](https://pubmed.ncbi.nlm.nih.gov/40446794/)
- [Universal CAR-T LN trial NCT06681337](https://clinicaltrials.gov/study/NCT06681337)
- [CD19/BCMA CAR-T LN trial NCT06785519](https://clinicaltrials.gov/study/NCT06785519)
- [Autologous CD19 CAR-T refractory LN case (PMC12636897)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12636897/)
- [CAR T-cell therapy for SLE review (Frontiers Immunology 2024)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1476859/full)
- [ACR 2025 dual-target CAR-T (EMJ)](https://www.emjreviews.com/rheumatology/news/acr-2025-car-t-therapies-show-promise-in-autoimmune-disease/)
- [2019 EULAR/ACR recommendations (Rheumatology Advisor)](https://www.rheumatologyadvisor.com/news/2019-eular-acr-recommendations-for-sle-classification-criteria/)
- [2019 EULAR/ACR predicts LN/flare risk (Renal and Urology News)](https://www.renalandurologynews.com/news/2019-eular-acr-criteria-lupus-nephritis-diagnosis-flare-risk/)
- [Histopathological sensitivity/specificity analysis (PMC11640231)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11640231/)
- [2019 EULAR/ACR criteria full text (eScholarship)](https://escholarship.org/content/qt8xx2q1vs/qt8xx2q1vs.pdf)
- [2019 criteria in childhood-onset SLE (PubMed 36990435)](https://pubmed.ncbi.nlm.nih.gov/36990435/)
- [Prognostic value 2019 criteria pediatric LN (ACR Open Rheum)](https://acrjournals.onlinelibrary.wiley.com/doi/full/10.1002/acr2.11674)
- [Lupus nephritis Wikidata Q1621830](https://www.wikidata.org/wiki/Q1621830)
- [MalaCards Lupus Nephritis](https://www.malacards.org/card/lupus_nephritis)
- [NORD MONDO disease page](https://rarediseases.org/mondo-disease/lupus-nephritis/)
- [StatPearls Lupus Nephritis](https://www.ncbi.nlm.nih.gov/books/NBK499817/)
- [GARD Lupus Nephritis](https://rarediseases.info.nih.gov/diseases/10747/lupus-nephritis)
- [NIDDK Lupus & Kidney Disease](https://www.niddk.nih.gov/health-information/kidney-disease/lupus-nephritis)
- [MedlinePlus Lupus Nephritis](https://medlineplus.gov/ency/article/000481.htm)
- [Active LN as orphan disease commentary (NDT 2026)](https://academic.oup.com/ndt/article/41/6/988/8514263)
- [IUPHAR/BPS Lupus Nephritis disease page](https://www.guidetopharmacology.org/GRAC/DiseaseDisplayForward?diseaseId=1055)
- [Orphanet SLE (ORPHA:536)](https://www.orpha.net/en/disease/detail/536)
- [OMIM #152700 SLE](https://omim.org/entry/152700)
- [IKZF2 biomarker LN (PMC9187727)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9187727/)
- [Orphanet Pediatric SLE (ORPHA:93552)](https://www.orpha.net/en/disease/detail/93552)
- [ICD10Data M32.14](https://www.icd10data.com/ICD10CM/Codes/M00-M99/M30-M36/M32-/M32.14)
- [ICD10Data M32.15](https://www.icd10data.com/ICD10CM/Codes/M00-M99/M30-M36/M32-/M32.15)
- [Preeclampsia risk in LN pregnancy (PMC8120629)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8120629/)
- [Maternal outcomes prospective multicenter study (PubMed 27373903)](https://pubmed.ncbi.nlm.nih.gov/27373903/)
- [Adverse pregnancy outcomes LN (Renal and Urology News)](https://www.renalandurologynews.com/news/lupus-nephritis-ups-risk-preeclampsia-prematurity-c-section-pregnant-women/)
- [sFlt-1/PlGF ratio flare vs preeclampsia (PMC12143737)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12143737/)
- [Approach to pregnancy in LN (Kidney Medicine)](https://www.kidneymedicinejournal.org/article/S2590-0595(23)00142-5/fulltext)
- [Managing pregnancy in lupus patients (PMC4515284)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4515284/)
- [Single cell spatial transcriptomics childhood LN (bioRxiv)](https://www.biorxiv.org/content/10.1101/2023.11.09.566503.full.pdf)
- [Advances of scRNA-seq in kidney immunology (PMC8548579)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8548579/)
- [Single cell spatial transcriptomics childhood LN (PMC10680641)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10680641/)
- [Design/application scRNA-seq kidney immune cells LN (PubMed 31853010)](https://pubmed.ncbi.nlm.nih.gov/31853010/)
- [Immune cell landscape kidneys LN (Nature Immunology)](https://www.nature.com/articles/s41590-019-0398-x)
- [AMP Phase 1 Single Cell Portal](https://portals.broadinstitute.org/single_cell/study/amp-phase-1)
- [Broad Institute AMP publication](https://www.broadinstitute.org/publications/broad613206)
- [Single-cell spatial transcriptomics imiquimod LN fibrosis (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2405580825001748)
- [Belimumab in LN new trial results (AJKD)](https://www.ajkd.org/article/S0272-6386(20)31124-0/fulltext)
- [BLISS-LN secondary analysis kidney outcomes (Kidney International)](https://www.kidney-international.org/article/S0085-2538(21)00862-0/fulltext)
- [BLISS-LN NEJM full text](https://www.nejm.org/doi/full/10.1056/NEJMoa2001180)
- [BLISS-LN subgroup post hoc (PubMed 37463054)](https://pubmed.ncbi.nlm.nih.gov/37463054/)
- [BLISS-LN NephJC summary](http://www.nephjc.com/news/bliss-ln)
- [AURORA 1 study NCT03021499](https://clinicaltrials.gov/study/NCT03021499)
- [AURORA 1 Lancet abstract (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S014067362100578X)
- [AURORA 1 NephJC summary](http://www.nephjc.com/news/2021/6/21/aurora1)
- [LUPKYNIS efficacy page](https://www.lupkynispro.com/efficacy/)
- [Anifrolumab dose regimen selection phase 3 (Wiley CPT)](https://ascpt.onlinelibrary.wiley.com/doi/10.1002/cpt.70307?af=R)
- [Anifrolumab LN second-year extension (ResearchGate)](https://www.researchgate.net/publication/373316075_Anifrolumab_in_lupus_nephritis_results_from_second-year_extension_of_a_randomised_phase_II_trial)
- [Phase 3 IRIS trial NCT05138133](https://clinicaltrials.gov/study/NCT05138133)
- [First patients dosed IRIS phase 3 (AstraZeneca)](https://www.astrazeneca.com/content/az-us/media/press-releases/2022/first-patients-dosed-in-iris-phase-iii-trial-evaluating-anifrolumab-in-lupus-nephritis.html)
- [Anifrolumab LN second-year extension PubMed 37607780](https://pubmed.ncbi.nlm.nih.gov/37607780/)
- [SAPHNELO TULIP-SC phase 3 interim (AstraZeneca)](https://www.astrazeneca-us.com/media/press-releases/2025/SAPHNELO-self-administration-TULIP-SC-Phase-III-trial-meets-primary-endpoint-in-patients-with-systemic-lupus-erythematosus-based-on-an-interim-analysis.html)
- [Anifrolumab safe option for active LN (Lupus Foundation)](https://www.lupus.org/news/anifrolumab-saphnelo-added-to-standard-therapy-may-be-safe-option-for-active-lupus-nephritis)
- [Update on cellular/molecular aspects of LN (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1521661620301285)
- [AKI-induced lupus exacerbation via NETs (PMC8269073)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8269073/)
- [NETs drive acute lupus flares UV-triggered (bioRxiv)](https://www.biorxiv.org/content/10.1101/2023.12.23.572573.full.pdf)
- [Frontiers AKI/NETs Fcgr2b lupus model](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2021.669162/full)
- [Type I IFN and neutrophil transcripts renal biopsies (Rheumatology)](https://academic.oup.com/rheumatology/article/62/7/2534/6820951)
- [Type I IFN and neutrophil transcripts PubMed 36355567](https://pubmed.ncbi.nlm.nih.gov/36355567/)
- [Podocyte/tubular epithelial-immune interplay (Frontiers Immunology 2025)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1682075/full)
- [Childhood-onset LN long-term outcomes/predictors (Pediatric Nephrology 2025)](https://link.springer.com/article/10.1007/s00467-025-06718-0)
- [Three decades progress childhood LN (CJASN, PubMed 21799148)](https://pubmed.ncbi.nlm.nih.gov/21799148/)
- [Long-term outcomes prognostic risk factors childhood LN (PMC11985274)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985274/)
- [Renal vascular lesions childhood-onset LN (PMC11584461)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11584461/)
- [Clinical manifestations/prognosis/treat-to-target pediatric LN (Pediatric Nephrology)](https://link.springer.com/article/10.1007/s00467-021-05164-y)
- [Long-term prognosis pediatric/adult/advanced-age onset LN (PMC11966454)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11966454/)
- [Serositis poor prognosis marker pediatric SLE (PMC11959889)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11959889/)
- [Childhood-onset LN unique aspects/challenges (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0085253825006453)
- [Health disparities in lupus (Lupus Foundation of America)](https://www.lupus.org/health-disparities)
- [Health disparities pediatric SLE outcomes (PMC9614219)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9614219/)
- [State of lupus clinical trials minority participation (PMC6722692)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6722692/)
- [Lupus epidemiology sex/race/ethnicity (WebMD)](https://www.webmd.com/lupus/lupus-epidemiology-sex-race-ethnicity)
- [Duke Scholars disparities publication](https://scholars.duke.edu/publication/1159060)
- [Minority health disparities IgAN/glomerulonephritis context (PMC10476677)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10476677)