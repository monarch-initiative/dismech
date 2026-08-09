---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T13:58:09.973756'
end_time: '2026-08-01T14:23:35.776807'
duration_seconds: 1525.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PPP2R3C-Related Gonadal Dysgenesis Syndrome
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
  web_search_requests: 6
  num_turns: 71
  total_cost_usd: 4.979807000000001
  session_id: bd35c618-8070-4639-ad87-ae18a1a02540
  stop_reason: end_turn
citation_count: 14
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PPP2R3C-Related Gonadal Dysgenesis Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PPP2R3C-Related Gonadal Dysgenesis Syndrome** covering all of the
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

# PPP2R3C-Related Gonadal Dysgenesis Syndrome — Comprehensive Research Report

**Prepared:** 2026-08-01 · **Target:** dismech knowledge-base entry
**Primary ontology anchor:** `MONDO:0032738` — *gonadal dysgenesis, dysmorphic facies, retinal dystrophy, and myopathy*
**Causal gene:** *PPP2R3C* (`hgnc:17485`), 14q13.2

> **Evidence-quality note up front.** This is an ultra-rare disorder with **~19 published affected individuals from ~12 families** (2019–2026). Nearly all clinical claims rest on five primary reports plus one literature-review case report. Frequency figures are small-denominator counts (n = 4 or n = 16), not population estimates, and two of the source cohorts actively disagree about whether ocular and muscular involvement are core features. Every percentage below is annotated with its denominator. Sections 5, 13 and 14 are largely "not applicable / no data" and are marked as such rather than padded.

---

## 1. Disease Information

### Overview

PPP2R3C-related gonadal dysgenesis syndrome is a rare autosomal recessive syndromic disorder of sex development (DSD) caused by biallelic germline variants in *PPP2R3C*, which encodes the B″γ (B-double-prime gamma) regulatory subunit of protein phosphatase 2A (PP2A). The core presentation is **gonadal dysgenesis with hypergonadotropic hypogonadism** — complete or partial in 46,XY individuals, and ovarian dysgenesis/primary gonadal insufficiency in 46,XX individuals — combined with a **recognizable facial gestalt** and a variable multisystem set of extragonadal anomalies (low birth weight, delayed bone age, neurodevelopmental delay, myopathy, retinal dystrophy, sensorineural hearing loss, renal agenesis, ventral-wall and anorectal malformations, ectodermal changes).

The gene was established as a human disease gene in 2019 by Guran et al., who described it as "a novel 46, XY complete gonadal dysgenesis syndrome caused by homozygous variants in PPP2R3C gene" and noted that "*PPP2R3C* gene is most abundantly expressed in testis in humans, while its function was hitherto unknown" (PMID:30893644).

Two distinct OMIM phenotypes are allelic at this locus:

| Allelic state | Phenotype | OMIM | Inheritance |
|---|---|---|---|
| **Biallelic** (homozygous / compound heterozygous) | Myoectodermal gonadal dysgenesis syndrome (MEGD) / GDRM | **#618419** | Autosomal recessive |
| **Heterozygous** (male carriers) | Spermatogenic failure 36 (SPGF36) — teratozoospermia, reduced fertility | **#618420** | Autosomal dominant, sex-limited |

Altunoglu et al. state this dual architecture explicitly: "Homozygous variants in PPP2R3C have been reported to cause a syndromic 46,XY complete gonadal dysgenesis phenotype with extragonadal manifestations (GDRM, MIM# 618419) in patients from four unrelated families, whereas heterozygous variants have been linked to reduced fertility with teratozoospermia (SPGF36, MIM# 618420) in male carriers" (PMID:34750818).

### Key identifiers

| Resource | Identifier |
|---|---|
| **MONDO** | `MONDO:0032738` — gonadal dysgenesis, dysmorphic facies, retinal dystrophy, and myopathy |
| **OMIM (phenotype, biallelic)** | `OMIM:618419` — MYOECTODERMAL GONADAL DYSGENESIS SYNDROME; MEGD |
| **OMIM (legacy, merged)** | `OMIM:600908` — 46,XY agonadism with intellectual disability, short stature, retarded bone age, and multiple extragenital malformations |
| **OMIM (allelic, heterozygous)** | `OMIM:618420` — SPERMATOGENIC FAILURE 36; SPGF36 |
| **OMIM (gene)** | `OMIM:615902` — PPP2R3C |
| **MedGen** | UID 1679397; Concept ID C5193085 |
| **UMLS** | C5193085 |
| **HGNC** | `hgnc:17485` (PPP2R3C) |
| **NCBI Gene** | 55012 |
| **Ensembl** | ENSG00000092020 |
| **UniProt** | Q969Q6 |
| **Orphanet** | **No dedicated ORPHA code identified.** MONDO:0032738 carries no ORPHA xref (mappings are MEDGEN:1679397, OMIM:600908, OMIM:618419, UMLS:C5193085). Orphanet was not reachable during this research; treat as "not found," not "confirmed absent." |
| **ICD-10** | **No dedicated code.** Closest: Q99.1 (46,XX true hermaphrodite / pure gonadal dysgenesis grouping), Q56.4 (indeterminate sex), Q50.0 (congenital absence of ovary). Code assignment is jurisdiction-dependent. |
| **ICD-11** | **No dedicated code.** Closest: LD2A.0Y / "46,XY disorder of sex development, other specified." |
| **MeSH** | No specific descriptor. Indexed under *Gonadal Dysgenesis, 46,XY* (D023961), *Protein Phosphatase 2*, *Disorders of Sex Development* |

### Synonyms and alternative names

Per MedGen/MONDO:
- Gonadal dysgenesis, dysmorphic facies, retinal dystrophy, and myopathy (**GDRM**)
- Myoectodermal gonadal dysgenesis syndrome (**MEGD**); also written "Myo-Ectodermo-Gonadal Dysgenesis"
- **Kennerknecht syndrome**
- Brosnan-Kennerknecht-Guran-Koc syndrome (**BKGK**)
- 46,XY agonadism with intellectual disability (historically "mental retardation"), short stature, retarded bone age, and multiple extragenital malformations
- PPP2R3C-related syndromic gonadal dysgenesis

**Curation note on naming:** The MONDO label ("…retinal dystrophy, and myopathy") encodes two features that Altunoglu et al. explicitly rejected as major criteria: "Our findings supported neither ocular nor muscular involvement as major criteria of the syndrome" (PMID:34750818). The gene-anchored name (*PPP2R3C-related gonadal dysgenesis syndrome*) is therefore the more defensible entry name, with the MONDO label retained as `disease_term` + synonym.

### Information provenance

All information is derived from **aggregated disease-level resources and individual published case reports** — OMIM, MONDO, MedGen, HPO annotations, and six primary publications. There is **no registry, no EHR-derived cohort, no natural-history study, and no biobank series** for this disorder. HPO annotations for `OMIM:618419` are derived from the four original Guran 2019 patients only (frequencies expressed as n/4).

---

## 2. Etiology

### Disease causal factors

**Monogenic, fully genetic.** The disorder is caused by biallelic germline variants in *PPP2R3C*. There is no evidence for environmental, infectious, or somatic-mosaic contribution.

### Genetic risk factors

**Causal variants (biallelic — required for the syndrome).** Six distinct variants across all published families; note that **every reported disease allele is missense or in-frame** — no biallelic truncating/null genotype has been reported in a living human:

| Variant (cDNA) | Protein | Type | Families / reports | Ancestry |
|---|---|---|---|---|
| c.578T>C | p.(Leu193Ser) | Missense | Most frequent allele; Guran 2019 (P1), Cicek 2021 (4 patients/3 families), Altunoglu 2022 (multiple) | Turkish — **founder** |
| c.1049T>C | p.(Phe350Ser) | Missense | Guran 2019 (P2, P4); Yavuzyilmaz Simsek 2026 (2 siblings) | Turkish |
| c.308T>C | p.(Leu103Pro) | Missense | Guran 2019 (P3); Altunoglu 2022 (p12) | Turkish |
| c.639_647dupTTTCTACTC | p.(Ser216_Tyr218dup) | In-frame duplication (novel) | Altunoglu 2022 (2 patients) | Indian |
| c.684_686delTTC | p.(Phe229del) | In-frame deletion | Zhang 2022 — *in trans* with p.G417E | Chinese |
| c.1250G>A | p.(Gly417Glu) | Missense | Zhang 2022 — *in trans* with p.F229del | Chinese |

Guran et al.: "We have identified three different homozygous PPP2R3C variants, c.308T>C (p.L103P), c.578T>C (p.L193S) and c.1049T>C (p.F350S), in four girls with 46, XY complete gonadal dysgenesis" (PMID:30893644).

Altunoglu et al. added the in-frame duplication: "eight patients from four unrelated families of Turkish and Indian descent with three different germline homozygous PPP2R3C variants including a novel in-frame duplication (c.639_647dupTTTCTACTC, p.Ser216_Tyr218dup)" (PMID:34750818).

**Founder effect.** Cicek et al. concluded from three unrelated Turkish families sharing p.L193S with differing geographic origins that this "suggests a founder effect of p.L193S in *PPP2R3C* in the Turkish population" (PMID:34714774, full text).

**Consanguinity** is a major contextual risk factor — most reported families are consanguineous (Turkish and Indian), and *Consanguinity* is a MeSH index term on Guran 2019.

**Heterozygous carrier risk (SPGF36).** Male heterozygotes have been reported with teratozoospermia and reduced fertility: "Heterozygous males presented with abnormal sperm morphology and impaired fertility" (PMID:30893644). **This is contested** — Altunoglu et al.: "We also did not encounter infertility problems in the carriers" (PMID:34750818). Treat carrier subfertility as a variant- or family-dependent, incompletely penetrant trait, not an established universal.

**Modifier genes.** None identified. *MAP3K1* is a mechanistically plausible modifier candidate given the demonstrated antagonism (Section 6, PMID:39317195), but **no human modifier data exist**.

### Environmental risk factors

**None identified.** No toxin, drug, endocrine-disruptor, radiation, or occupational association has been reported. Consanguinity (a population-structure variable, not an exposure) is the only non-allelic factor influencing occurrence. Parental age has not been examined.

### Protective factors

**None identified,** genetic or environmental. Notably, **heterozygosity is not fully protective in males** (SPGF36). No protective/hypomorphic modifier alleles are described.

### Gene–environment interactions

**No data.** Not searched in CTD/PheGenI-type resources because no environmental axis exists for a fully penetrant recessive Mendelian disorder of embryonic development. This is a legitimate "not applicable" rather than a gap.

---

## 3. Phenotypes

### 3a. Frequency across all published patients (Zhang 2022 systematic tabulation, n = 16 evaluable)

Zhang et al. tabulated every previously published patient plus their own case. Denominators are 16 (their case included where data available):

| Feature | Frequency | HPO suggestion |
|---|---|---|
| **Facial deformity / dysmorphism** | **16/16 (100%)** | `HP:0001999` Abnormal facial shape |
| **Retardation of bone age** | **15/16 (93.7%)** | `HP:0002750` Delayed skeletal maturation |
| **Delayed nervous system development** | **14/16 (87.5%)** | `HP:0012758` Neurodevelopmental delay |
| **Impaired vision** | **10/16 (62.5%)** | `HP:0000505` Visual impairment |
| **Low birth weight** | **9/16 (56.2%)** | `HP:0001518` Small for gestational age |
| **Myopathy** | **8/16 (50%)** | `HP:0003198` Myopathy |
| **Renal agenesis** | **6/16 (37.5%)** | `HP:0000122` Unilateral renal agenesis |
| **Gastrointestinal dysfunction** | **6/16 (37.5%)** | `HP:0011024` Abnormality of the gastrointestinal tract |
| **Sensorineural hearing loss** | **4/16 (25%)** | `HP:0000407` Sensorineural hearing impairment |
| **Cardiac defect** | **3/16 (18.7%)** | `HP:0001627` Abnormal heart morphology |
| **Gonadal dysgenesis** | **17/17 (100%)** — defining | `HP:0000133` Gonadal dysgenesis |

Verbatim: "facial deformity (16 of 16, 100%), retardation of bone age (15 of 16, 93.7%), and delayed development of the nervous system (14 of 16, 87.5%)" … "impaired vision (10 of 16, 62.5%), low birth weight (9 of 16, 56.2%), and myopathy (8 of 16, 50%)" … "renal agenesis (6 of 16, 37.5%), gastrointestinal dysfunction (6 of 16, 37.5%), sensorineural hearing loss (4 of 16, 25%), and cardiac defect (3 of 16, 18.7%)" (PMID:35812758).

> **Frequency-evidence caution (per dismech `docs/frequency-evidence-guidelines.md`).** These are literature-aggregate counts across 16 individuals, heavily weighted to a single founder allele and two Turkish centers. Mapping them to `FrequencyEnum` bands is defensible for the ≥80% features (VERY_FREQUENT/OBLIGATE) and the ~20–40% features (OCCASIONAL), but the *ocular* and *muscular* frequencies are **actively disputed** (Altunoglu 2022) and are the ones most likely to be ascertainment-inflated. Recommend omitting `frequency:` on retinal dystrophy and myopathy, or annotating them with an explicit `discussions` entry.

### 3b. Full HPO annotation set for `OMIM:618419`

The following is the curated HPO annotation set (frequencies are n/4, from the four Guran 2019 patients):

**Genitourinary / reproductive**
| HP ID | Term | Freq |
|---|---|---|
| `HP:0000133` | Gonadal dysgenesis | 4/4 |
| `HP:0000013` | Hypoplasia of the uterus | 4/4 |
| `HP:0000059` | Hypoplastic labia majora | 4/4 |
| `HP:0000060` | Clitoral hypoplasia | 4/4 |
| `HP:0000122` | Unilateral renal agenesis | 2/4 |

**Endocrine (laboratory)**
| `HP:0008232` | Elevated circulating follicle stimulating hormone level | — |
| `HP:0011969` | Elevated circulating luteinizing hormone level | — |

**Craniofacial — the diagnostic gestalt**
| `HP:0012368` | Flat face | 4/4 |
| `HP:0000341` | Narrow forehead | 2/4 |
| `HP:0002236` | Frontal upsweep of hair | 4/4 |
| `HP:0002553` | Highly arched eyebrow | 4/4 |
| `HP:0045075` | Sparse eyebrow | 4/4 |
| `HP:0000286` | Epicanthus | 4/4 |
| `HP:0007892` | Hypoplasia of the lacrimal punctum | 4/4 |
| `HP:0000444` | Convex nasal ridge | 4/4 |
| `HP:0000430` | Underdeveloped nasal alae | 4/4 |
| `HP:0000319` | Smooth philtrum | 4/4 |
| `HP:0000343` | Long philtrum | 4/4 |
| `HP:0000233` | Thin vermilion border | 4/4 |
| `HP:0000668` | Hypodontia | 4/4 |

**Ear**
| `HP:0000369` | Low-set ears | 4/4 |
| `HP:0000358` | Posteriorly rotated ears | 4/4 |
| `HP:0000396` | Overfolded helix | 4/4 |
| `HP:0000407` | Sensorineural hearing impairment | 2/3 |

**Eye**
| `HP:0000510` | Rod-cone dystrophy | 4/4 |

**Limb / skeletal**
| `HP:0004279` | Short palm | 4/4 |
| `HP:0001169` | Broad palm | — |
| `HP:0000954` | Single transverse palmar crease | 4/4 |
| `HP:0010554` | Cutaneous finger syndactyly | 4/4 |
| `HP:0001377` | Limited elbow extension | 4/4 |
| `HP:0009611` | Bifid distal phalanx of the thumb | 1/4 |
| `HP:0001853` | Bifid distal phalanx of toe | 1/4 |
| `HP:0001385` | Hip dysplasia | 1/4 |
| `HP:0002650` | Scoliosis | 1/4 |
| `HP:0002750` | Delayed skeletal maturation | 4/4 |

**Skin / hair (ectodermal)**
| `HP:0000958` | Dry skin | 4/4 |
| `HP:0040189` | Scaling skin | 4/4 |
| `HP:0002221` | Absent axillary hair | 1/4 |
| `HP:0002225` | Sparse pubic hair | 1/4 |

**Ventral wall / gastrointestinal**
| `HP:0001539` | Omphalocele | 2/4 |
| `HP:0001540` | Diastasis recti | 1/4 |
| `HP:0002023` | Anal atresia | 1/4 |
| `HP:0002021` | Pyloric stenosis | 1/4 |

**Nervous system**
| `HP:0001274` | Agenesis of corpus callosum | 1/4 |

**Growth**
| `HP:0001518` | Small for gestational age | 2/4 |
| `HP:0004322` | Short stature | 1/4 |

**Other**
| `HP:0001747` | Accessory spleen | 1/4 |

**Clinical course / inheritance**
| `HP:0003577` | Congenital onset | 4/4 |
| `HP:0000007` | Autosomal recessive inheritance | — |

**Additional terms supported by later reports but not in the OMIM:618419 annotation set** (candidates to add with their own evidence):
- `HP:0000786` Primary amenorrhea (Altunoglu 2022; Zhang 2022)
- `HP:0000826` Abnormality of the endocrine system / `HP:0000815` Hypergonadotropic hypogonadism (Altunoglu 2022)
- `HP:0008191` Decreased circulating anti-Müllerian hormone (Cicek 2021 — AMH 0.00–0.01)
- `HP:0001324` Muscle weakness / `HP:0003236` Elevated circulating creatine kinase concentration (Cicek 2021 — elevated CK)
- `HP:0001250` Seizure (Cicek 2021 — epilepsy in patient 1)
- `HP:0000045` Micropenis / `HP:0000047` Hypospadias (`HP:0000051` penoscrotal hypospadias) / `HP:0000028` Cryptorchidism (Cicek 2021 patient 3, partial GD)
- `HP:0000778` Hypoplasia of the thymus — no; instead: `HP:0010976` B lymphocytopenia and `HP:0011840` Abnormal T cell count (Zhang 2022 — novel immunological phenotype, see below)
- `HP:0001249` Intellectual disability (Yavuzyilmaz Simsek 2026)
- `HP:0000155` / `HP:0000175` — not reported
- `HP:0002937` Cubitus valgus, `HP:0000465` Webbed neck, `HP:0001005` (pigmented nevus → `HP:0000998` Hyperpigmentation of the skin) — Zhang 2022, Turner-like features
- `HP:0001155`-adjacent: `HP:0001167` Abnormality of finger; `HP:0009882` Short distal phalanx of finger — Zhang 2022 "short fifth phalanx"
- `HP:0011623` Bicuspid aortic valve, `HP:0001631` Atrial septal defect, `HP:0001642` Pulmonic stenosis, `HP:0005301` (LPSVC → `HP:0005301` persistent left superior vena cava) — Guran 2019 / Altunoglu 2022 cardiac spectrum
- `HP:0002251` Aganglionic megacolon — no; instead `HP:0002566` Intestinal malrotation (Altunoglu p13) and `HP:0004397` (anterior ectopic anus → `HP:0004397` Anteriorly placed anus)
- `HP:0000568` Microphthalmia — no; `HP:0000545` Myopia, `HP:0000646` Amblyopia, `HP:0000540` Hypermetropia (Cicek 2021; Altunoglu 2022)

### 3c. Novel immunological phenotype (n = 1, hypothesis-generating)

Zhang et al. reported the first immune abnormality: "decreased number of CD19+ B cells (1.6%, normal range: 8.5%–14.5%) and CD4+ T cells (21.5%, normal range: 30.0–46.0%)" with increased NK cells, and proposed that "PPP2R3C plays a role in the survival of multiple lymphocytes," establishing immunodeficiency as "a new phenotype in syndromic 46, XY gonadal dysgenesis" (PMID:35812758). This is biologically coherent with two decades of G5PR mouse immunology (Section 6) but rests on **a single patient with no infection history reported** — curate as a `KNOWLEDGE_GAP` discussion, not an established phenotype.

### 3d. Phenotype characteristics

| Dimension | Assessment |
|---|---|
| **Age of onset** | **Congenital** (`HP:0003577`, 4/4). Structural anomalies (omphalocele, anal atresia, renal agenesis, facial gestalt, IUGR) are present at birth. Gonadal dysgenesis is prenatally determined but usually **clinically recognized in childhood or at pubertal age** (probands ascertained at 6–24 years). |
| **Severity** | **Severe and variable.** Gonadal phenotype ranges from complete GD with unambiguous female external genitalia through partial GD with ambiguous genitalia/undervirilization to 46,XX primary gonadal insufficiency. Altunoglu: "46,XY affected individuals displayed a spectrum of external genital phenotypes from ambiguous genitalia to complete female" (PMID:34750818). |
| **Progression** | **Static/non-progressive for malformations**; **progressive for the sensory features** (rod-cone dystrophy is progressive by nature; hearing loss may progress). Gonadal failure is fixed and permanent — the gonad is dysgenetic/absent, not degenerating. Delayed bone age is a fixed maturational delay with delayed epiphyseal closure (Zhang 2022: closure delayed "until after age 20"). |
| **Course pattern** | **Chronic lifelong**, requiring indefinite hormone replacement. Epilepsy (1 patient) would be episodic. |

### 3e. Quality-of-life impact (per domain)

**No disease-specific QoL instrument data exist** (no EQ-5D, SF-36, PROMIS, or DSD-specific PROM published for this disorder). Domain-level inference from the phenotype set, flagged as inference:

| Domain | Expected impact |
|---|---|
| Sexual/reproductive | **Severe** — universal infertility; requires lifelong sex-steroid replacement; psychosocial burden of DSD diagnosis, gender assignment, and disclosure |
| Vision (where present) | **Moderate–severe** — progressive rod-cone dystrophy → night blindness, field loss; amblyopia/refractive error |
| Hearing (where present) | **Moderate** — sensorineural loss affecting language and schooling |
| Neurocognitive | **Moderate–severe** — neuromotor delay in ~87%; intellectual disability reported |
| Musculoskeletal | **Moderate** — myopathy, short stature, joint contracture (limited elbow extension), scoliosis, hip dysplasia |
| Renal | **Mild–moderate** — unilateral agenesis usually compensated; requires monitoring of the solitary kidney |
| Appearance | **Moderate** — distinctive facial gestalt with associated social burden |

---

## 4. Genetic / Molecular Information

### Causal gene

**PPP2R3C** — "protein phosphatase 2 regulatory subunit B''gamma"
- HGNC:17485 · Entrez 55012 · Ensembl ENSG00000092020 · UniProt Q969Q6 · OMIM *615902
- **Location:** 14q13.2
- **Previous symbol:** C14orf10. **Aliases:** **G5PR**, G4-1, FLJ20644; "rhabdomyosarcoma antigen MU-RMS-40.6A/6C"
- **Structure:** 13 exons; encodes a **453-amino-acid**, ~53.3 kDa protein (Zhang 2022 / UniProt Q969Q6)
- **Protein domains:** two **EF-hand** calcium-binding domains (residues 273–308 and 341–376), with five annotated Ca²⁺-binding sites at residues 286, 288, 290, 292, 297 (UniProt Q969Q6). The B″ family of PP2A regulatory subunits is the calcium-responsive family — relevant to mechanism.
- **Role:** the **B″γ regulatory/targeting subunit** of the PP2A heterotrimeric holoenzyme (catalytic C subunit PPP2CA + scaffold A subunit PPP2R1A + variable B subunit). The B subunit dictates substrate selection and subcellular targeting, so loss of B″γ is a **substrate-specific**, not global, phosphatase lesion.

Guran et al.: "This gene encodes B″gamma regulatory subunit of the protein phosphatase 2A (PP2A), which is a serine/threonine phosphatase involved in the phospho-regulation processes of most mammalian cell types" (PMID:30893644).

### Pathogenic variants

**Variant classification.** ClinVar contains **118 records** for *PPP2R3C* (NCBI eSearch, 2026-08-01), the large majority VUS or benign; the six disease alleles above are the curated pathogenic/likely-pathogenic set. A targeted ClinVar pathogenicity query failed (backend error) so per-variant ClinVar assertions should be re-verified before curation.

**Variant type distribution — the striking pattern.** All six disease alleles are **missense (4) or in-frame indels (2)**. **No biallelic nonsense, frameshift, or splice-null genotype has ever been reported in a living patient.** This is not coincidence: the mouse null is early-embryonic lethal (Section 6/15), which predicts that complete human loss of function is also **prenatally lethal** and that all viable human genotypes are necessarily **hypomorphic**. This is a key mechanistic constraint for the pathophysiology model.

**Allele frequencies (population databases).**

| Variant | Frequency | Source |
|---|---|---|
| c.578T>C p.(L193S) | **Absent** from gnomAD, ExAC, 1000 Genomes; also absent from 200 ethnically matched in-house Turkish exomes — "was found neither in 200 ethnically matched in-house Turkish exomes … nor in … GnomAD, ExAC, 1000 Genomes" | PMID:34714774 (full text) |
| c.1250G>A p.(G417E) | **Absent** — "The variant p.Gly417Glu was not found in gnomAD, ExAC, or 1000 Genomes databases" | PMID:35812758 |
| c.684_686delTTC p.(F229del) | ExAC **0.0000753**; gnomAD **0.000194452** | PMID:35812758 |
| c.308T>C, c.1049T>C, c.639_647dup | Not reported in gnomAD in source publications | PMID:30893644, PMID:34750818 |

**Gene-level constraint (pLI / LOEUF):** **not retrieved** — gnomAD's browser is a JavaScript application not fetchable by the tools available, and DECIPHER/GeneCards returned no data. This should be looked up manually before curation. Mechanistically, embryonic lethality of the mouse null plus the complete absence of biallelic nulls in humans both argue for meaningful LoF constraint, but I am explicitly **not** asserting a numeric pLI I could not verify.

**Somatic vs germline:** All disease variants are **germline**. No somatic *PPP2R3C* driver role is established; the gene appears in cancer contexts only as a modifier of multidrug resistance (Section 6) and in bioinformatic prognostic signatures (e.g., lung adenocarcinoma immune-homeostasis signature, PMID:38757752) — these are correlative, not causal.

**Functional consequences — the unresolved question.** Two incompatible framings coexist in the literature:

1. **Loss of function (LoF) of the B″γ subunit.** Supported by Ganga et al.'s functional work: the p.L193S protein showed "strongly diminished localization to centrioles" and "diminished binding to FOP for PPP2R3C-L193S compared to wildtype PPP2R3C" (PMID:39317195); the paper refers throughout to "inactivating PPP2R3C mutations."
2. **Gain of PP2A catalytic activity toward SOX9.** Cicek et al. hypothesized the variant may "upregulate the catalytic function of PP2A and increase the dephosphorylation of active SOX9-phosphoprotein, which impairs SOX9" (PMID:34714774) — invoked to explain the *decreased* SOX9-phospho staining Guran et al. observed.

These are not trivially reconcilable: (1) predicts less PP2A activity at PPP2R3C-targeted substrates, (2) predicts more dephosphorylation of SOX9. A partial reconciliation is that loss of B″γ **mis-targets** rather than inactivates the PP2A core, redistributing catalytic activity onto substrates (including SOX9) that B″γ normally sequesters away from the holoenzyme — but this is unproven. **Curate as competing `mechanistic_hypotheses` with an explicit `KNOWLEDGE_GAP`, not as a settled LoF entry.**

### Modifier genes

None established. *MAP3K1* is the leading candidate on mechanistic grounds (PMID:39317195) — see Section 6.

### Epigenetic information

**No data.** No methylation, histone-modification, chromatin, or episignature study of PPP2R3C-related disease exists. No entry in DiseaseMeth/MethBase. (Note: an episignature study would be worthwhile — many chromatin/phosphatase-related syndromic DSDs have been episignature-profiled.)

### Chromosomal abnormalities

No CNV, translocation, or structural mechanism is reported at this locus for this phenotype. **Important adjacent finding to avoid confusing:** deletions of 14q13.2–q21.1 encompassing *NKX2-1* cause **Brain-Lung-Thyroid syndrome** (PMID:29477862), a mechanistically unrelated disorder that shares the cytoband. A 14q13.2 CNV report should not be mistaken for this disease.

---

## 5. Environmental Information

**Not applicable.** This is a fully penetrant biallelic Mendelian disorder of embryonic development.

- **Environmental factors:** none reported. No CTD/TOXNET association.
- **Lifestyle factors:** none reported; no modifiable behavioral contributor to occurrence. (Lifestyle is relevant only to *management* — bone health, vision safety, cardiovascular risk on hormone replacement.)
- **Infectious agents:** not applicable — no infectious etiology or trigger.

---

## 6. Mechanism / Pathophysiology

### The PP2A holoenzyme substrate-targeting layer (upstream, molecular)

PP2A is an obligate heterotrimer: catalytic subunit C (PPP2CA), scaffold subunit A (PPP2R1A), plus one of ~15 variable **B subunits** that confer substrate specificity and subcellular targeting. PPP2R3C is the **B″γ** subunit. UniProt lists its interaction with "phosphatase 2A core enzyme (PPP2CA and PPP2R1A)," plus MCM3AP/GANP, PPP5C (PP5), ABCB1, and TFPI2.

**Suggested GO terms:**
- `GO:0000159` protein phosphatase type 2A complex (cellular component)
- `GO:0019888` protein phosphatase regulator activity
- `GO:0008601` protein phosphatase type 2A regulator activity
- `GO:0006470` protein dephosphorylation
- `GO:0005509` calcium ion binding (the EF-hand domains)

**Causal chain, node 1 (MOLECULAR):** Biallelic hypomorphic *PPP2R3C* variant → loss/mis-targeting of the PP2A B″γ regulatory subunit → **substrate-specific dysregulation of PP2A-mediated dephosphorylation**.

### Arm A — SOX9 phospho-regulation and the testis-determination switch (the original mechanism)

Guran et al. demonstrated the key human tissue finding: "We have shown a decreased SOX9-Phospho protein expression in the dysgenetic gonads of the patients with homozygous PPP2R3C variants suggesting impaired SOX9 signaling in the pathogenesis of gonadal dysgenesis" (PMID:30893644).

SOX9 is the central effector of the SRY→SOX9→FGF9/AMH testis-determination cascade; SOX9 activity requires phosphorylation-dependent regulation. Loss of appropriate PP2A-B″γ control of the SOX9 phospho-cycle collapses the SOX9 activator state during the narrow window of gonadal sex determination (human ~6–7 weeks gestation; mouse 11.5 dpc). In 46,XY embryos this yields failure to establish/maintain testis fate → dysgenetic streak gonad → no Sertoli-cell AMH (Müllerian structures persist) and no Leydig-cell testosterone (external genitalia remain female or under-virilized).

For **46,XX** disease, Cicek et al. proposed the mirror lesion: the variant may "suppress WNT/β-catenin signalling, which subsequently impairs ovarian development resulting in XX-GD" (PMID:34714774). Altunoglu et al. drew the same inference from the sex-agnostic phenotype: "Since both XX and XY individuals were affected, we hypothesize that PPP2R3C is essential in the early signaling cascades controlling sex determination in humans" (PMID:34750818).

**Causal chain, node 2 (CELLULAR/TISSUE):** dysregulated SOX9 phospho-signaling (XY) / impaired WNT-β-catenin ovarian program (XX) → **failure of supporting-cell lineage specification in the bipotential gonad** → gonadal dysgenesis (streak/dysgenetic gonad, or non-visualized gonad).

**Causal chain, node 3 (ORGANISM):** absent gonadal steroid and AMH output → hypergonadotropic hypogonadism (FSH/LH ↑, AMH ↓↓, testosterone ↓), persistent Müllerian derivatives with hypoplastic uterus, absent puberty, primary amenorrhea, infertility.

**Suggested GO/pathway terms:** `GO:0008584` male gonad development · `GO:0008585` female gonad development · `GO:0030238` male sex determination · `GO:0060008` (Sertoli cell differentiation `GO:0060008`) · `GO:0008406` gonad development · `GO:0016055` Wnt signaling pathway · `GO:0060070` canonical Wnt signaling pathway

### Arm B — the PPP2R3C–MAP3K1 centrosomal phospho-regulatory module (2024, the mechanistic breakthrough)

This is the single most important recent advance and it **unifies two previously separate DSD genes**. Ganga et al. used DepMap co-essentiality across ">1000 human cell lines" and found that "Among 16,708 genes analyzed, growth phenotypes for *FOP* and *CEP350* were most highly correlated to those of *PPP2R3C*" (PMID:39317195).

Findings, verbatim where quoted:
- **Centriolar localization:** "PPP2R3C, a poorly characterized PP2A phosphatase subunit, is a distal centriole protein and functional partner of centriolar proteins CEP350 and FOP." Ultrastructure expansion microscopy showed "a cylindrical distribution of PPP2R3C at the distal region of centrioles with a diameter of 239 ± 44 nm."
- **Recruitment hierarchy:** "FOP localizes to centrioles independently of PPP2R3C but is needed to recruit PPP2R3C to centrioles."
- **The kinase counterpart:** "a key function of PPP2R3C is to counteract the kinase activity of MAP3K1."
- **Genetic epistasis:** "MAP3K1 knockout suppresses growth defects caused by PPP2R3C inactivation, and MAP3K1 and PPP2R3C have opposing effects on basal and microtubule stress-induced JNK signaling." "phosphorylated Jun (P-Jun) levels were strongly increased in *PPP2R3C* KO cells."
- **Dosage sensitivity:** "acute overexpression of MAP3K1 severely inhibits centrosome function and triggers rapid centriole disintegration."
- **The disease-gene convergence:** "inactivating PPP2R3C mutations and activating MAP3K1 mutations both cause congenital syndromes characterized by gonadal dysgenesis."
- **Patient-variant functional test:** the L193S protein showed "strongly diminished localization to centrioles" and "diminished binding to FOP."
- **Model:** "we propose that imbalanced activity of this centrosomal kinase-phosphatase pair is the shared cause of these disorders."

This matters because *MAP3K1* gain-of-function is one of the commonest causes of 46,XY gonadal dysgenesis (~15–20% of cases), acting by shifting the SOX9/FGF9-vs-WNT4/β-catenin balance: MAP3K1 GoF increases phosphorylation of MAPK targets → increased CTNNB1, WNT4 and FOXL2, decreased SRY and SOX9 (reviewed PMID:35290982). **PPP2R3C LoF and MAP3K1 GoF are therefore two entry points into the same phospho-balance node** — a strong candidate for a shared dismech mechanism module (`sox9_map3k1_sex_determination_phosphobalance`), with `Loss of PPP2R3C Restraint on MAP3K1` as a specialized trigger node.

**Suggested GO/CL/anatomy terms for this arm:** `GO:0005814` centriole · `GO:0005813` centrosome · `GO:0007099` centriole replication · `GO:0051301` cell division · `GO:0007256` activation of JNKK activity / `GO:0007254` JNK cascade · `GO:0046330` positive regulation of JNK cascade · `GO:0060271` cilium assembly · `GO:0072372` primary cilium (HPA reports PPP2R3C protein in the primary cilium)

### Arm C — Hedgehog/GLI signaling (2024)

Baran et al. established PPP2R3C as a Hedgehog-pathway component: "PPP2R3C interacts with Gli proteins, and its disruption reduces Hedgehog pathway activity as measured by reduced expression of Gli1/2 and Hh target genes upon Hh signaling activation, and reduced growth of a Hh signaling-dependent medulloblastoma cell line. Moreover, we establish an antagonistic connection between PPP2R3C and MEKK1 kinase in Gli protein phosphorylation" (PMID:39173855). Note **MEKK1 = MAP3K1** — this is the *same* antagonistic pair as Arm B, now acting on GLI phosphorylation, and the centrosome/primary cilium is precisely where Hh transduction occurs. Arms B and C are almost certainly one mechanism.

Hh/GLI dependence gives a clean, parsimonious explanation for the **extragonadal** phenotype that SOX9 alone does not: Hedgehog signaling governs limb/digit patterning (syndactyly, bifid distal phalanges), craniofacial morphogenesis (the facial gestalt, underdeveloped alae nasi), ventral body wall closure (omphalocele, diastasis recti), anorectal development (anal atresia, anteriorly placed anus), renal development (renal agenesis), skeletal maturation (delayed bone age), and neural development (corpus callosum agenesis) — i.e., essentially the full extragonadal list. Combined with `GO:0060271` cilium assembly, this makes PPP2R3C-related disease **mechanistically adjacent to the ciliopathies**, and `ciliopathy_dysfunction#Impaired Hedgehog Signal Transduction` is a plausible (if not yet formally demonstrated) conformance target.

**Suggested GO terms:** `GO:0007224` smoothened signaling pathway · `GO:0045880` positive regulation of smoothened signaling pathway · `GO:0008589` regulation of smoothened signaling pathway

### Arm D — JNK-mediated apoptosis and lymphocyte survival (the G5PR literature, 2005–2026)

Twenty years of work on this protein under the name **G5PR** independently established it as a **JNK-pathway brake controlling activation-induced cell death (AICD)** — the same JNK axis Ganga et al. rediscovered at the centrosome.

- **B cells (Xing 2005, PMID:16129705):** "a loss of the protein phosphatase component G5PR increased the activation-induced cell death (AICD) and thus impaired B cell survival." CD19-Cre conditional KO mice "had a decreased number of splenic B cells (60% of the controls)"; "G5pr(-/-) B cells were sensitive to AICD caused by BCR cross-linking. This was associated with an increased depolarization of the mitochondrial membrane and the enhanced activation of c-Jun NH(2)-terminal protein kinase and Bim."
- **T cells (Xing 2008, PMID:18022237):** "T-cell-specific G5PR knockout (G5pr(-/-)) mice displayed thymic atrophy, significant reduction in thymocyte numbers, particularly a 10-fold decrease in the number of CD4 and CD8 double-positive (DP) thymocytes"; the defect was "hyper-activation of JNK and Caspase-3 with augmented Fas ligand (FasL) expression … G5PR is essential for the survival of DP cells during thymocyte development."
- **Transcriptional induction (2006, PMID:16343422):** "BCR-crosslinking-induced G5pr transcription in AICD-resistant mature splenic IgM(lo)IgD(hi) B-cells but not in AICD susceptible immature IgM(hi)IgD(lo) B-cells."
- **Overexpression (2012, PMID:22753944):** G5PR "suppresses JNK phosphorylation"; transgenic overexpression "impaired the affinity-maturation of Ag-specific B cells" and aged female Tg mice "showed an increase in the numbers of peritoneal B-1a cells and the generation of autoantibodies."
- **Autoimmunity (2015, PMID:25601926):** "an abnormal increase of protein phosphatase 2A subunit G5PR that regulates BCR-mediated JNK signaling as a cause of autoimmunity."
- **Human SLE (Fang 2026, PMID:42298912):** PPP2R3C is "a critical and selective negative regulator of T cell receptor (TCR) signaling, which was downregulated in CD4+ T cells from SLE patients"; it "restrains the PLCγ1-JNK axis to limit T cell hyperactivation"; gene therapy restoring PPP2R3C "potently suppressed T cell activation and autoantibody production."

**This arm directly predicts and explains Zhang 2022's patient.** Zhang et al. made exactly this connection: "PPP2R3C is essential for the maintenance of B cells through the regulation status of the JNK-mediated apoptosis signal," citing that "Gene knockout (PPP2R3C-/-) mice by conditional targeting in CD19+ B cells showed a deficit in B-cell survival and a reduced number of mature B cells" (PMID:35812758). The convergence of an independently-derived mouse immunophenotype with a single human patient's B/T lymphopenia is the strongest available argument that the immune phenotype is real rather than incidental — but it remains **n = 1 in humans**.

**Suggested terms:** `GO:0007254` JNK cascade · `GO:0043066` negative regulation of apoptotic process · `GO:0050853` B cell receptor signaling pathway · `GO:0050852` T cell receptor signaling pathway · CL: `CL:0000236` B cell, `CL:0000624` CD4-positive, alpha-beta T cell, `CL:0000809` double-positive, alpha-beta immature T cell

### Arm E — Multidrug transporter regulation (context, not disease mechanism)

Katayama et al.: "PP5/PPP2R3C dephosphorylated protein kinase A/protein kinase C-phosphorylation of P-gp" and "knockdown of PP5 and/or PPP2R3C increased P-gp expression and lowered the sensitivity to vincristine and doxorubicin" (PMID:24333728). Relevant as a documented PPP2R3C substrate relationship (and a pharmacological caveat), **not** as a mechanism of gonadal dysgenesis.

### Protein dysfunction

Structural inferences from the reported alleles (from Zhang 2022 modeling and UniProt domain annotation):
- **p.L193S, p.L103P, p.F350S** — buried hydrophobic residues replaced by polar/proline. p.F350S falls **within EF-hand 2 (341–376)**, predicting disrupted calcium-dependent regulation. L193S is functionally validated as disrupting centriolar targeting and FOP binding (PMID:39317195).
- **p.S216_Y218dup** and **p.F229del** — in-frame indels in the region between the N-terminus and the EF-hands. For p.F229del, Zhang et al.: the deletion "will cause an incomplete alpha helix structure and change the condition of four repeated phenylalanines."
- **p.G417E** — C-terminal; "does not affect a significant protein domain, but the number of hydrogen bonds and contacts formed within residues is changed" (PMID:35812758). This is the weakest structural rationale of the set; it is a compound-heterozygous partner allele, consistent with a mild hypomorph.
- Both Zhang 2022 variants "demonstrated high conservation across species."

There is **no experimental structure** of PPP2R3C (no PDB entry located); AlphaFold model AF-Q969Q6 would be the modeling substrate.

### Metabolic changes

**None reported.** No metabolomic, lipidomic, or intermediary-metabolism abnormality is described. Elevated **creatine kinase** (Cicek 2021) is a marker of muscle-fiber injury, not a metabolic defect per se.

### Immune system involvement

See Arm D. Human evidence: n = 1 (B and CD4 T lymphopenia, increased NK). Mouse evidence: robust and conditional-tissue-specific. Additional human genetic association context — *PPP2R3C* appears in transcriptome-wide association studies for rheumatoid arthritis (PMID:33482886, PMID:32599322), inflammatory bowel disease Immunochip meta-analysis (PMID:29584801), psoriatic arthritis/ankylosing spondylitis overlap (PMID:38907550), and schizophrenia TWAS (PMID:29632383). **These are common-variant/statistical associations at an unrelated allelic architecture and must not be curated as mechanisms of the Mendelian syndrome** — at most as `SUSCEPTIBILITY`-typed context for the gene.

### Tissue damage mechanisms

Rather than a degenerative injury mechanism, the primary lesion is **developmental**: failure of lineage specification and morphogenesis during embryogenesis. The exceptions with a genuine progressive-degeneration component are:
- **Retina** — rod-cone dystrophy: progressive photoreceptor loss. Candidate module conformance: `photoreceptor_degeneration#Rod Photoreceptor Apoptosis`.
- **Cochlea** — sensorineural hearing loss. Candidate: `sensorineural_hair_cell_loss#Hair Cell Mechanotransduction Failure and Death`.
- **Skeletal muscle** — myopathy with elevated CK.
- **Lymphocytes** — JNK/caspase-3-driven activation-induced cell death (Arm D).

### Molecular profiling

| Modality | Status |
|---|---|
| **Transcriptomics** | Mouse gonadal scRNA-seq only (Cicek 2021, see below). **No patient transcriptome.** No GEO/ArrayExpress dataset for this disorder. |
| **Proteomics** | No disease proteome. PPP2R3C interactome data available via BioGRID/IntAct and the Baran 2024 (Derua/Janssens) mass-spec work on the PP2A interactome. |
| **Metabolomics / lipidomics** | None. |
| **Epigenomics** | None (no episignature). |
| **Genomic structural features** | No CNV mechanism. |

**Mouse gonadal single-cell expression (Cicek 2021, PMID:34714774 full text) — the most informative expression data available:** "*Ppp2r3c* expression in the majority of gonadal cell lineages, including *Tcf21*+ gonadal progenitors at 11.5 dpc and *Sox9*+ and *Fst*+ supporting cells in XY and XX gonads, respectively," with the critical negative result: **"no evidence of any sexual dimorphism in levels of expression."** The absence of dimorphic expression is exactly what a gene required for *both* XY and XX gonadal development should show, and it independently supports Altunoglu's "early signaling cascades controlling sex determination" hypothesis over a testis-specific one — despite the human bulk-expression testis enrichment.

**Human tissue expression:** Guran et al. state PPP2R3C "is most abundantly expressed in testis in humans." Human Protein Atlas is more measured: **low tissue specificity (Tau 0.30), "Detected in all"** tissues, assigned to "cluster 39: Testis - Nuclear processes," with "General cytoplasmic expression," nucleoplasm plus nuclear bodies, Golgi, cytosol, actin filaments, and **primary cilium**. The honest formulation for curation is *testis-enriched but broadly expressed* — which is what the multisystem phenotype demands.

**Advanced technologies.** The **functional genomics screen** evidence is the strongest single mechanistic dataset for this gene: DepMap genome-wide CRISPR KO across >1000 cell lines drove the entire Ganga 2024 discovery (co-essentiality of *PPP2R3C* with *FOP* and *CEP350*; MAP3K1 KO suppression). No single-cell, spatial-transcriptomic, or multi-omics patient study exists.

### Consolidated causal chain for `pathophysiology` curation

```
[MOLECULAR] Biallelic hypomorphic PPP2R3C variant
  → Loss/mis-targeting of the PP2A B''γ regulatory subunit
      ↓
[MOLECULAR] Loss of PPP2R3C restraint on MAP3K1 kinase activity
  (validated: L193S loses centriolar localization + FOP binding; ↑P-Jun in KO)
      ↓ (branches)
      ├─[CELLULAR]  Centrosome/distal-centriole dysfunction + de-repressed JNK signaling
      ├─[CELLULAR]  Reduced Hedgehog/GLI transcriptional output
      ├─[MOLECULAR] Dysregulated SOX9 phospho-cycle (↓SOX9-phospho in dysgenetic gonad)
      │             ± de-repressed WNT4/β-catenin/FOXL2
      └─[CELLULAR]  Excess JNK/caspase-3-driven activation-induced cell death in lymphocytes
      ↓
[TISSUE]  Failure of supporting-cell lineage specification in the bipotential gonad
          (Sertoli in XY / granulosa in XX)  →  dysgenetic or streak gonad
      +   Hh-dependent morphogenetic failure: craniofacial, limb/digit,
          ventral wall, anorectal, renal, skeletal-maturation, CNS
      +   Progressive photoreceptor and cochlear hair-cell loss; myopathy
      ↓
[ORGANISM] Hypergonadotropic hypogonadism (FSH/LH↑, AMH↓↓, T↓),
           absent puberty, primary amenorrhea, infertility
      +    Recognizable facial gestalt + multisystem congenital anomalies
      +    Delayed bone age / short stature
      ± [ORGANISM] B and CD4 T lymphopenia (n=1)
```

---

## 7. Anatomical Structures Affected

### Organ level

**Primary (direct developmental target):**
| Structure | UBERON |
|---|---|
| Gonad (bipotential/indifferent gonad) | `UBERON:0000991` gonad; `UBERON:0005564` indifferent gonad |
| Testis | `UBERON:0000473` testis |
| Ovary | `UBERON:0000992` ovary |

**Secondary / co-affected (multisystem, largely Hh-morphogenetic):**
| Structure | UBERON |
|---|---|
| Uterus (hypoplastic; Müllerian derivatives retained in 46,XY) | `UBERON:0000995` uterus |
| Fallopian tube / oviduct-like structures | `UBERON:0003889` fallopian tube |
| External genitalia (clitoris, labia majora) | `UBERON:0004176` clitoris; `UBERON:0005048` labium majus |
| Kidney (unilateral agenesis) | `UBERON:0002113` kidney |
| Retina | `UBERON:0000966` retina |
| Inner ear / cochlea | `UBERON:0001846` internal ear; `UBERON:0001844` cochlea |
| External ear (low-set, posteriorly rotated, overfolded helix) | `UBERON:0001456` face; `UBERON:0001691` external ear |
| Skeletal muscle | `UBERON:0001134` skeletal muscle tissue |
| Skeleton / epiphysis (delayed maturation) | `UBERON:0001474` bone element; `UBERON:0000980` epiphysis |
| Corpus callosum | `UBERON:0002336` corpus callosum |
| Anal canal / rectum (atresia, ectopia) | `UBERON:0000159` anal canal |
| Stomach — pylorus (stenosis) | `UBERON:0001165` pylorus |
| Anterior abdominal wall (omphalocele, diastasis recti) | `UBERON:0001414` abdominal wall |
| Heart (ASD, bicuspid aortic valve, pulmonic stenosis) | `UBERON:0000948` heart |
| Skin (dry, scaling) | `UBERON:0002097` skin of body |
| Tooth (hypodontia) | `UBERON:0001091` calcareous tooth |
| Lacrimal punctum | `UBERON:0002493` lacrimal punctum |
| Spleen (accessory) | `UBERON:0002106` spleen |
| Thymus (mouse model; human n=1 lymphopenia) | `UBERON:0002370` thymus |

**Body systems involved:** reproductive/endocrine (primary), integumentary, skeletal, muscular, nervous (central + special senses), renal/urinary, gastrointestinal, cardiovascular, immune/hematopoietic. This is a genuine **multisystem** disorder.

### Tissue and cell level

| Cell type | CL | Rationale |
|---|---|---|
| Sertoli cell | `CL:0000216` | SOX9-dependent XY supporting cell; fails to differentiate → no AMH |
| Leydig cell | `CL:0000178` | Absent androgen output |
| Granulosa cell | `CL:0000501` | XX supporting-cell counterpart (*Fst*+ lineage) |
| Gonadal (somatic) progenitor / *Tcf21*+ coelomic-epithelium-derived progenitor | `CL:0000006`-adjacent; nearest specific: `CL:0000630` supporting cell | Cicek 2021 scRNA-seq: *Ppp2r3c*+ at 11.5 dpc |
| Germ cell / primordial germ cell | `CL:0000586` germ cell; `CL:0000670` primordial germ cell | Depleted in the dysgenetic gonad; relevant to tumor risk |
| Male germ cell / spermatid | `CL:0000018` spermatid | Teratozoospermia in heterozygotes (head, acrosome, nucleus anomalies) |
| Rod photoreceptor | `CL:0000604` | Rod-cone dystrophy |
| Cone photoreceptor | `CL:0000573` | Rod-cone dystrophy |
| Cochlear inner/outer hair cell | `CL:0000589` / `CL:0000601` | SNHL |
| Skeletal muscle fiber | `CL:0008002` skeletal muscle myoblast; `CL:0000188` cell of skeletal muscle | Myopathy, ↑CK |
| Chondrocyte | `CL:0000138` | SOX9 is master chondrogenic TF; Zhang 2022 attribute facial/nasal/ear cartilage findings to "dysplasia of cartilage in ears and nose in the early chondrogenesis" |
| Cranial neural crest cell | `CL:0011012` neural crest cell | Facial gestalt (inferred, not demonstrated) |
| B cell | `CL:0000236` | G5PR mouse KO; human n=1 |
| CD4+ αβ T cell | `CL:0000624` | Human n=1 |
| Double-positive immature αβ T cell | `CL:0000809` | Mouse T-cell-specific KO: 10-fold DP reduction |
| Natural killer cell | `CL:0000623` | Increased in the n=1 patient |

Tissue classes affected: **epithelial** (gonadal supporting-cell lineages, tubular epithelium), **connective/cartilage** (facial and auricular cartilage), **muscle** (skeletal), **nervous** (CNS, retina), **lymphoid**.

### Subcellular level

| Compartment | GO CC | Evidence |
|---|---|---|
| **Distal centriole** | `GO:0005814` centriole | Ganga 2024 — cylindrical distribution, 239 ± 44 nm diameter |
| Centrosome | `GO:0005813` centrosome | Ganga 2024 |
| Primary cilium | `GO:0072372` primary cilium | HPA protein localization; Hh transduction site |
| PP2A holoenzyme complex | `GO:0000159` protein phosphatase type 2A complex | UniProt |
| Nucleoplasm / nuclear body | `GO:0005654`, `GO:0016604` | HPA; UniProt (nucleus, excluded from nucleoli) |
| Cytosol | `GO:0005829` | UniProt: cytoplasmic accumulation during cytokinesis |
| Golgi apparatus | `GO:0005794` | HPA |
| Actin filament | `GO:0005884` | HPA |
| Mitochondrion (indirect) | `GO:0005739` | Xing 2005: "increased depolarization of the mitochondrial membrane" in G5pr⁻/⁻ B cells |

### Localization and lateralization

- **Gonadal involvement is bilateral and symmetric** — bilateral streak/dysgenetic gonads, or bilaterally non-visualized gonads.
- **Renal agenesis is unilateral** (`HP:0000122`, 2/4) — an asymmetric feature within an otherwise symmetric syndrome.
- Craniofacial features are bilateral and symmetric. Cicek 2021 patient 3 showed **left** cryptorchidism and **right** ductus deferens agenesis — asymmetric internal genital-duct involvement in partial GD.

---

## 8. Temporal Development

### Onset

- **Congenital** — `HP:0003577` Congenital onset, 4/4 in the HPO annotation set.
- **Onset pattern: chronic/insidious with a prenatal origin.** The determining lesion occurs during the narrow window of gonadal sex determination (human ~6–7 weeks gestation) and organogenesis. There is no acute phase.
- **Prenatal manifestation:** intrauterine growth restriction (`HP:0001518`, 2/4 in Guran's series; low birth weight 9/16 = 56.2% across all patients; recorded birth weights range **1000 g** (Zhang 2022) to 3700 g). Omphalocele and cardiac defects are prenatally detectable on ultrasound.
- **Typical age at clinical/molecular diagnosis** varies by presenting route:
  - **Neonatal/infantile** — when ambiguous genitalia, omphalocele, or anal atresia forces early evaluation
  - **Childhood** — Guran/Cicek probands assessed at 6–10.5 years, often via dysmorphology or the extragonadal anomalies
  - **Adolescence/adulthood** — absent puberty and primary amenorrhea (Altunoglu's two 46,XX patients; Zhang's patient diagnosed at 24)

### Progression

**No formal staging system exists** for this disorder. A pragmatic natural-history framing:

| Stage | Timing | Features |
|---|---|---|
| Prenatal | 6 wk gestation – birth | Gonadal determination failure; IUGR; structural malformations |
| Neonatal/infantile | 0–2 y | Surgical malformations (omphalocele, anal atresia, pyloric stenosis, cardiac); feeding; hearing screen |
| Childhood | 2–10 y | Neuromotor delay, delayed bone age, myopathy, onset of retinal dystrophy, short stature |
| Pubertal | 10–16 y | Absent spontaneous puberty; rising FSH/LH; primary amenorrhea; diagnosis often crystallizes here; **gonadectomy decision point** |
| Adult | >16 y | Lifelong hormone replacement; infertility; delayed epiphyseal closure (Zhang: closure "until after age 20"); bone-health and progressive sensory surveillance |

- **Progression rate:** **Malformations are static.** The gonadal deficit is fixed and non-progressive (there is no gonad to lose). **Rod-cone dystrophy and sensorineural hearing loss are the progressive components.** Overall course: **slow, with a static structural core plus two progressive sensory tracks.**
- **Course pattern: chronic, lifelong, non-relapsing.**
- **Duration:** lifelong.

### Patterns

- **Remission:** none — spontaneous remission is not possible for a fixed developmental lesion. Hormone replacement induces and maintains secondary sexual characteristics ("treatment-induced" phenotypic improvement, not remission of the disorder).
- **Critical periods:**
  1. **~6–7 weeks gestation (human) / 11.5 dpc (mouse)** — the sex-determination window. Once passed, the gonadal outcome is irreversible; **no postnatal intervention can restore gonadal function.** This is the fundamental therapeutic constraint on the disorder.
  2. **Neonatal period** — surgical correction of omphalocele/anal atresia; sex-assignment discussion in an MDT setting.
  3. **Age 10–13 years** — the window for timely pubertal induction; delay compromises bone mass accrual, growth, and psychosocial outcomes.
  4. **Adolescence** — germ-cell-tumor risk management in 46,XY GD with intra-abdominal dysgenetic gonads.
  5. **Prior to epiphyseal closure (late, ~>20 y here)** — the extended window for growth-directed intervention, unusually long in this disorder because of the marked bone-age delay.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence: no estimate exists.** No ORPHA epidemiology class, no registry, no population study.
- **Cumulative reported cases: ~19 affected individuals from ~12 families**, aggregated as:

| Report | PMID | Patients | Karyotypes |
|---|---|---|---|
| Guran 2019 (Turkey) | 30893644 | 4 (4 unrelated families) | 4 × 46,XY CGD |
| Cicek 2021 (Turkey) | 34714774 | 4 (3 unrelated families) | 1 × 46,XX, 2 × 46,XY CGD, 1 × 46,XY PGD |
| Altunoglu 2022 (Turkey + India) | 34750818 | 8 (4 unrelated families) | 2 × 46,XX; remainder 46,XY (CGD and PGD) |
| Zhang 2022 (China) | 35812758 | 1 | 46,XY CGD (compound het) |
| Yavuzyilmaz Simsek 2026 (Turkey) | 42445464 | 2 (siblings) | 1 × 46,XY CGD, 1 × 46,XX ovarian dysgenesis |

Zhang 2022's own tabulation cross-checks that Guran/Cicek/Altunoglu patients are non-overlapping (their table labels them p1–p4, p5–p8, p9–p16). **Caveat:** the single PPP2R3C patient in Zhang 2024's Chinese 46,XY DSD cohort (PMID:37147882) is almost certainly the same individual as the Zhang 2022 case report (same senior authors, same institution — Peking Union Medical College Hospital) and should **not** be counted twice.

- **Denominator context — how rare within DSD:** In an unselected series of 70 Chinese 46,XY DSD patients, "Seven patients were found harboring RVs of the 46, XY DSD pathogenic genes identified in recent years, namely DHX37 in four patients, MYRF in two patients, and PPP2R3C in one patient" (PMID:37147882). **PPP2R3C therefore accounted for 1/70 ≈ 1.4% of 46,XY DSD** in that cohort, versus ~60% attributable to *AR*, *SRD5A2* and *NR5A1* combined. This is the only quantitative yield estimate available and is a useful figure for the entry.

- **Incidence:** unknown.

### For genetic etiology

| Parameter | Assessment |
|---|---|
| **Inheritance pattern** | **Autosomal recessive** (`HP:0000007`) for the syndrome. The allelic carrier phenotype SPGF36 is **autosomal dominant, sex-limited** (`HP:0000006`) — heterozygous males only. |
| **Penetrance** | **Biallelic: appears complete** for gonadal dysgenesis (17/17 reported biallelic patients have GD) — though ascertainment is entirely through the gonadal phenotype, so this is circular and cannot be treated as an unbiased penetrance estimate. **Heterozygous (SPGF36): incomplete and contested** — Guran reported "abnormal sperm morphology and impaired fertility" in carrier males (PMID:30893644), whereas Altunoglu "did not encounter infertility problems in the carriers" (PMID:34750818). |
| **Expressivity** | **Highly variable**, both between and within families. External genital phenotype spans "ambiguous genitalia to complete female" (PMID:34750818). Extragonadal features vary markedly: 100% facial dysmorphism vs 18.7% cardiac defects. Crucially, **ocular and muscular involvement differ systematically between cohorts** — Guran found rod-cone dystrophy in 4/4 and myopathy in 4/4, while Altunoglu concluded these were not major criteria. Whether this reflects allelic differences, ascertainment/assessment differences, or genetic background is unresolved and is a good candidate `KNOWLEDGE_GAP`. |
| **Genetic anticipation** | **Not applicable** — no repeat expansion mechanism. |
| **Germline mosaicism** | Not reported. |
| **Founder effects** | **Yes — p.L193S in the Turkish population.** Cicek et al.: identification of the same variant in unrelated families of differing geographic origin "suggests a founder effect of p.L193S in *PPP2R3C* in the Turkish population" (PMID:34714774). |
| **Consanguinity** | **Major contributor.** Most reported families are consanguineous; *Consanguinity* is a MeSH index term on Guran 2019. Homozygosity in the Turkish and Indian families is consanguinity-mediated. |
| **Carrier frequency** | **Not established.** p.L193S is absent from gnomAD, ExAC, 1000 Genomes, **and** from 200 in-house Turkish exomes (PMID:34714774) — so even in the founder population the carrier rate is below the detection floor of a 200-exome panel. p.F229del is present in gnomAD at 0.000194452 (PMID:35812758). No systematic carrier-screening study exists. |

### Population demographics

- **Affected populations:** reported in individuals of **Turkish** (majority — 4 of 5 reports), **Indian** (Altunoglu 2022), and **Chinese** (Zhang 2022) ancestry. The Turkish predominance reflects both the p.L193S founder allele and ascertainment at Turkish referral centers (Marmara, Koç, Istanbul University); it should not be read as biological restriction — the Chinese compound-heterozygous case demonstrates independent allelic origins.
- **Geographic distribution:** Turkey, India, China. **Variant-specific:** p.L193S — Turkey (founder); p.S216_Y218dup — India; p.F229del + p.G417E — China; p.L103P and p.F350S — Turkey.
- **Sex ratio:** The disorder affects **both 46,XY and 46,XX** individuals. Of ~19 reported patients, roughly **15 are 46,XY and 4 are 46,XX**. However, **almost all probands are phenotypically female regardless of karyotype**, which makes "sex ratio" a category error here: the correct statement is that **chromosomal-sex ratio is roughly 4:1 XY:XX**, and this excess is very likely **ascertainment bias** — 46,XY GD presents dramatically as sex-discordance in infancy or childhood, whereas 46,XX ovarian dysgenesis presents only as absent puberty/primary amenorrhea and is easy to attribute to other causes. Altunoglu's and Yavuzyilmaz Simsek's identification of 46,XX cases came specifically from recognizing the *facial gestalt*, supporting under-ascertainment of the XX form.
- **Age distribution:** reported patients span 6 to 24 years at assessment; adult data beyond the third decade are essentially absent, so **there is no information on middle-age or long-term outcome.**

---

## 10. Diagnostics

### Clinical / laboratory tests

**Endocrine panel — the core biochemical signature (hypergonadotropic hypogonadism):**

| Analyte | Finding | Illustrative values | LOINC |
|---|---|---|---|
| **FSH** | Markedly elevated | 70.88 IU/L (ref 1.2–19.2) [Zhang 2022]; 41.1, 43.1, 44.59 [Cicek 2021] | `LOINC:15067-2` |
| **LH** | Elevated | 23.22 IU/L (ref 1.2–8.6) [Zhang 2022]; 9.07, 1.81 [Cicek 2021] | `LOINC:10501-5` |
| **Testosterone** | Low/undetectable in CGD | 0.34 ng/mL (ref 1.75–7.81) [Zhang 2022]; <0.07 [Cicek 2021]; 1.3 in PGD | `LOINC:2986-8` |
| **Anti-Müllerian hormone (AMH)** | **Undetectable/very low in CGD; measurable in PGD** | 0.00–0.01 in CGD; **18.8 in the partial-GD patient** [Cicek 2021] | `LOINC:38476-0` |
| **Estradiol** | Low | 11 pg/mL [Zhang 2022] | `LOINC:2243-4` |
| **DHEAS** | Low | 26, 49 [Cicek 2021] | `LOINC:2191-5` |
| **Creatine kinase** | Elevated where myopathy present | [Cicek 2021] | `LOINC:2157-6` |
| **TSH/free T4** | **Normal** — useful negative | [Zhang 2022] | `LOINC:3016-3` |

**Diagnostic pearl:** AMH discriminates complete from partial gonadal dysgenesis (0.00 vs 18.8) better than testosterone alone and should be measured in every case.

**Immunophenotyping (emerging, optional):** lymphocyte subsets — the single reported patient had CD19+ B cells 1.6% (ref 8.5–14.5%) and CD4+ T cells 21.5% (ref 30.0–46.0%) with increased NK cells (PMID:35812758). Reasonable to include as an exploratory assay; not yet standard of care.

**Biomarkers:** There is **no specific circulating biomarker.** Diagnosis is genotype- plus gestalt-driven. The nearest thing to a tissue biomarker is **reduced SOX9-phospho immunostaining in gonadal tissue** (PMID:30893644) — a research-grade IHC finding, not a validated clinical assay.

**Imaging:**
| Study | Purpose | Typical finding |
|---|---|---|
| Pelvic/abdominal ultrasound; **pelvic MRI** | Internal genital anatomy | Hypoplastic/prepubertal uterus; **non-visualized gonads**; oviduct-like structures |
| **Bone-age radiograph (left hand/wrist)** | Skeletal maturation | Markedly delayed — the highest-yield non-gonadal test (93.7%); e.g., bone age 6 y 10 m at chronological 9 y 4 m [Cicek 2021]; ~2-year delay at age 10 [Zhang 2022] |
| Renal ultrasound | Renal agenesis (37.5%) | Unilateral absent kidney |
| **Echocardiography** | Cardiac defects (18.7%) | ASD, bicuspid aortic valve ± aortic stenosis, pulmonic stenosis, persistent left SVC |
| Brain MRI | CNS malformation | Agenesis of the corpus callosum (1/4) |
| Spine radiographs / hip imaging | Scoliosis, hip dysplasia | — |

**Functional and electrophysiological tests:**
- **Electroretinography (ERG)** + full ophthalmological exam with refraction — essential for rod-cone dystrophy, which is often clinically silent early. Also detects myopia, hypermetropia, amblyopia.
- **Audiometry / ABR** — sensorineural hearing loss (25%).
- **EEG** — if seizures (epilepsy in 1 patient).
- **EMG / nerve conduction** — myopathy characterization.
- Developmental/neuropsychological assessment.

**Biopsy and pathology:**
- **Gonadal biopsy with histopathology** — the definitive gonadal assessment. Findings: dysgenetic/streak gonad in CGD; "Histopathologic examination of biopsy of left gonad revealed immature testis" in the partial-GD patient (PMID:34714774). Also indicated for germ-cell-tumor (gonadoblastoma/dysgerminoma) surveillance.
- **Diagnostic laparoscopy** — Zhang 2022 confirmed "hypoplastic uterus, bilateral oviduct-like structures … via laparoscopy."
- **Muscle biopsy** — if myopathy requires characterization.
- **Research IHC:** SOX9 and phospho-SOX9 on gonadal tissue.

### Genetic testing

**Recommended approach (ordered):**

1. **Karyotype** — mandatory first step in any DSD; establishes 46,XY vs 46,XX and SRY status. All reported 46,XY patients were **SRY-positive**, which is itself informative: it excludes SRY deletion as the cause and points to a downstream lesion.
2. **Whole exome sequencing (WES)** — the primary diagnostic modality; all reported cases were found by WES or targeted Sanger. **With an explicit reanalysis caveat**: Yavuzyilmaz Simsek et al. report a homozygous variant "which was initially missed on routine WES but identified upon targeted reanalysis guided by their clinical features," concluding that findings "underscore the diagnostic importance of combining detailed phenotyping - including appreciation of distinctive facial gestalt - with systematic WES reanalysis. This approach is particularly valuable in unresolved syndromic DSD, where variable expressivity may obscure recognition of the underlying genetic defect" (PMID:42445464). **A negative WES does not exclude the diagnosis; phenotype-driven reanalysis is indicated.**
3. **Whole genome sequencing (WGS)** — reasonable when WES/reanalysis is negative; no published PPP2R3C case required WGS, and no non-coding/deep-intronic mechanism is described.
4. **DSD gene panels** — *PPP2R3C* is included on contemporary comprehensive DSD/46,XY DSD panels. In the Zhang 2024 cohort, *PPP2R3C* was one of nine genes yielding P/LP variants. A panel should also cover *SRY, NR5A1, MAP3K1, DHX37, MYRF, WT1, SOX9, DHH, CBX2, ZFPM2, GATA4, AR, SRD5A2, HSD17B3, NR0B1, WNT4, FOXL2*.
5. **Single-gene *PPP2R3C* sequencing** — appropriate when the facial gestalt is recognized, and specifically for **targeted testing of p.L193S in Turkish patients** (founder allele) and for cascade testing of at-risk relatives.
6. **Chromosomal microarray (CMA)** — appropriate in the general syndromic-DSD workup to exclude CNVs; **not diagnostic for this disorder** (no CNV mechanism described). Useful negative.
7. **FISH** — for SRY/Y-material assessment when karyotype is equivocal.
8. **Mitochondrial DNA testing** — **not indicated.** No mitochondrial mechanism.
9. **Repeat expansion testing** — **not indicated.** No repeat mechanism.

**GTR:** the condition is registered as *Gonadal dysgenesis, dysmorphic facies, retinal dystrophy, and myopathy* (C5193085), with *PPP2R3C* (Gene ID 55012) listed as testable.

### Omics-based diagnostics

- **RNA sequencing:** no established diagnostic role. Could in principle be informative for in-frame indel consequences, but no published use.
- **Proteomics / metabolomics / epigenomics / liquid biopsy:** no established or investigational role. An **episignature** study is a reasonable future avenue but does not currently exist.

### Clinical criteria

**No formal published diagnostic criteria or society guideline exists.** Diagnosis in practice rests on a triad:

1. **Gonadal dysgenesis with hypergonadotropic hypogonadism** (46,XY complete/partial, or 46,XX)
2. **The recognizable facial gestalt** — repeatedly emphasized as the entry point: "All patients exhibit recognizable facial dysmorphisms allowing gestalt diagnosis" (PMID:34750818). Components: abnormal hair patterning with frontal upsweep and additional whorls; broad/arched/sparse eyebrows; flat face; epicanthus; convex nasal ridge with underdeveloped alae nasi ("beaked nose"); long smooth philtrum; thin vermilion; low-set posteriorly rotated ears with overfolded helices; hypodontia; hypoplastic lacrimal puncta.
3. **≥1 extragonadal system involved** — delayed bone age (93.7%), neurodevelopmental delay (87.5%), low birth weight, retinal dystrophy, SNHL, renal agenesis, ventral-wall/anorectal anomaly, myopathy.
4. **Confirmed by biallelic *PPP2R3C* variants.**

**Differential diagnosis:**

| Condition | Gene(s) | Distinguishing features |
|---|---|---|
| **MAP3K1-related 46,XY GD** | *MAP3K1* | AD sex-limited; **isolated/non-syndromic** GD without the facial gestalt or multisystem anomalies; mechanistically the closest relative (same phospho-module) |
| *NR5A1*/SF1-related DSD | *NR5A1* | Adrenal involvement possible; variable, often non-syndromic |
| *DHX37*-related 46,XY GD/testicular regression | *DHX37* | 4/70 in the Chinese cohort; typically non-syndromic |
| *MYRF*-related syndromic DSD | *MYRF* | Cardiac-urogenital syndrome; congenital diaphragmatic hernia; 2/70 in the same cohort |
| *WT1* (Denys-Drash, Frasier) | *WT1* | **Nephrotic syndrome/glomerulopathy and Wilms tumor** — renal *dysfunction* vs PPP2R3C's renal *agenesis* |
| Campomelic dysplasia | *SOX9* | AD; bowed long bones, laryngotracheomalacia; SOX9 lesion is direct rather than phospho-regulatory |
| *SOX9*/`SOX9`-region regulatory 46,XY DSD | *SOX9* enhancers | Isolated GD |
| **Turner syndrome / 45,X mosaicism** | — | **Overlaps clinically** — Zhang 2022's patient had webbed neck, cubitus valgus, short 5th phalanx, short stature: Turner-like. **Karyotype is the discriminator.** |
| Complete androgen insensitivity | *AR* | Testes present, **normal/high** testosterone, absent Müllerian structures, **normal AMH** |
| 17β-HSD3 / 5α-reductase deficiency | *HSD17B3*, *SRD5A2* | Steroid-profile abnormality with **present testes** |
| Swyer syndrome (idiopathic 46,XY CGD) | — | Non-syndromic by definition |
| **Ciliopathies with GD-like features** (e.g., Bardet-Biedl) | *BBS*, etc. | Overlap on retinal dystrophy + renal + digit anomalies + hypogonadism; obesity/polydactyly pattern differs; mechanistically adjacent via Hh (Section 6, Arm C) |
| Alkuraya-Kučinskas / other Hh-pathway syndromes | — | Hh-pathway overlap |
| **Brain-Lung-Thyroid syndrome** | *NKX2-1* (14q13.2 del) | **Same cytoband, unrelated disease** — do not conflate a 14q13.2 deletion with this disorder (PMID:29477862) |

### Screening

- **Newborn screening:** **not included** in any program; no biochemical marker suitable for NBS.
- **Carrier screening:** **not offered as population screening.** Feasible and appropriate as **targeted/founder screening** — p.L193S in Turkish consanguineous populations. No published program.
- **Cascade screening:** **indicated.** Test parents (obligate carriers) and at-risk siblings. Because heterozygous males may have teratozoospermia (SPGF36), male carrier identification has independent reproductive-counselling value.
- **Prenatal / preimplantation:** available for known familial variants (see Section 13).

---

## 11. Outcome / Prognosis

> **Overall caveat:** there is **no natural-history study, no survival analysis, and no cohort followed beyond ~24 years of age.** Everything below is either directly attributable to a cited report or explicitly flagged as inference from analogous DSD/syndromic populations.

### Survival and mortality

- **Survival rate (5-/10-year/overall): no data.** No deaths are reported in any of the ~19 published patients.
- **Life expectancy:** **no data.** Inference: not obviously shortened by the gonadal phenotype itself. The determinants of early mortality would be the **neonatal surgical malformations** (omphalocele, anal atresia, pyloric stenosis) and **cardiac defects**, all of which are surgically manageable. **Important contrast:** complete loss of function is **embryonic-lethal in mice** ("results in embryonic death from 7.5 dpc or earlier," PMID:34714774) — all viable human patients carry hypomorphic alleles, so the reported cohort is, by construction, the survivable end of the allelic spectrum. There may be an unascertained burden of early pregnancy loss in carrier couples; this has never been studied and is a genuine knowledge gap.
- **Mortality rate / disease-specific mortality:** no data.

### Morbidity and function

- **Morbidity is high and multisystem** but non-lethal: universal infertility, absent spontaneous puberty requiring lifelong hormone replacement, neurodevelopmental delay (87.5%), progressive visual impairment (62.5%), myopathy (50%), hearing loss (25%), solitary kidney (37.5%).
- **Disability outcomes:** combined **sensory (vision + hearing) and cognitive** impairment is the principal driver of long-term functional limitation. Myopathy and short stature add motor/physical limitation. ICF domains most affected: seeing, hearing, mobility, learning/applying knowledge, and intimate relationships.
- **Quality-of-life measures:** **no instrument data.** No EQ-5D, SF-36, PROMIS, or DSD-specific PROM has been applied. This is a clear-cut evidence gap.

### Disease course and complications

| Complication | Basis |
|---|---|
| **Infertility** — universal in biallelic patients | All reports |
| **Hypogonadism-related osteopenia/osteoporosis** if pubertal induction is delayed or replacement is inadequate | Inference from hypogonadism generally; candidate conformance to `osteoporosis_bone_resorption` |
| **Germ cell tumour (gonadoblastoma / dysgerminoma)** in 46,XY GD with retained intra-abdominal dysgenetic gonads | **Inference from the general 46,XY GD literature, not from PPP2R3C data** — no tumour has been reported in any PPP2R3C patient. Flag as `KNOWLEDGE_GAP`. |
| **Progressive visual loss** from rod-cone dystrophy | Guran 2019 (4/4) |
| **Progressive hearing loss** | 25% |
| **Renal complications** of a solitary kidney (hypertension, hyperfiltration, CKD risk) | Inference from unilateral renal agenesis generally |
| Cardiac sequelae (ASD, bicuspid aortic valve → later valvulopathy) | Guran 2019; Altunoglu 2022 |
| Scoliosis progression; hip dysplasia | 1/4 each |
| Seizures | 1 patient |
| **Recurrent infection / immune dysfunction** | Speculative — n=1 lymphopenia with no reported infection history |
| Short stature | 1/4 in Guran's series; 148 cm (−3 SD) at 18 y in Zhang's patient |

- **Recovery potential:** **none for the gonadal or structural lesions** — these are fixed developmental outcomes and no intervention after the sex-determination window can restore gonadal function. Hormone replacement achieves excellent phenotypic outcomes (secondary sexual development, bone health) but is substitutive, not curative. Surgical correction of the malformations is generally definitive. Rehabilitative gains are achievable for developmental delay and myopathy.

### Prediction

**Prognostic factors (all inferred; none validated):**
- **Complete vs partial gonadal dysgenesis**, best indexed by **AMH** (0.00 in CGD vs 18.8 in PGD, PMID:34714774) — the single most useful available prognostic discriminator, predicting residual testicular tissue and the possibility of spontaneous virilization.
- **Genotype:** possibly informative — the ocular/muscular discordance between the Guran/Cicek (Turkish, L193S/F350S/L103P) and Altunoglu (mixed, including S216_Y218dup) cohorts hints at allele-dependent severity, but with 19 patients this is **not established**.
- **Presence of renal agenesis, cardiac defect, or corpus callosum agenesis** — predicts higher overall morbidity.
- **Timeliness of pubertal induction** — predicts bone mass and psychosocial outcome.
- **Baseline neurodevelopmental status.**

**Prognostic biomarkers:** **none validated.** AMH is the closest functional surrogate. No molecular prognostic marker exists.

---

## 12. Treatment

> **There is no disease-modifying or targeted therapy.** Management is entirely supportive, substitutive, surgical, and rehabilitative, delivered by a multidisciplinary DSD team. No treatment trial, no drug, and no clinical trial specific to PPP2R3C-related disease exists.

### Pharmacotherapy

| Treatment | Purpose / notes | NCIT / suggested annotation |
|---|---|---|
| **Estrogen replacement** (pubertal induction then maintenance) for female-raised individuals | Induces secondary sexual characteristics, uterine growth, bone mineral accrual. Start ~11–13 y with low-dose escalating estradiol. | `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` `CHEBI:16469` 17β-estradiol; modality `SMALL_MOLECULE`. Alternative action term: `NCIT:C15455` Hormone Therapy |
| **Progestin** added after breakthrough bleeding/adequate estrogenization, when a uterus is present | Endometrial protection | `NCIT:C15986` + `CHEBI:8730` progesterone |
| **Testosterone replacement** for male-raised individuals with partial GD | Virilization, pubertal induction | `NCIT:C15986` + `CHEBI:17347` testosterone |
| **Growth hormone** | **Not established for this disorder.** Would be considered only within the general short-stature/DSD framework; the marked bone-age delay and late epiphyseal closure extend the theoretical growth window. Flag as unproven. | `NCIT:C15238`? No — `NCIT:C15986` + `NCIT:C578` Recombinant Human Growth Hormone |
| **Calcium + vitamin D** | Bone health adjunct in hypogonadism | `NCIT:C15433` Nutritional Support + `CHEBI:27300` vitamin D |
| Antiseizure medication | If epilepsy present | `NCIT:C15986` |

**Pharmacogenomics:** No PharmGKB/CPIC guidance relates to *PPP2R3C*. **One theoretically relevant consideration:** PPP2R3C (with PP5) dephosphorylates P-glycoprotein/ABCB1, and "knockdown of PP5 and/or PPP2R3C increased P-gp expression and lowered the sensitivity to vincristine and doxorubicin" (PMID:24333728). This raises a purely speculative possibility that PPP2R3C-deficient patients could show altered handling of P-gp substrate drugs. **No clinical data support this; do not present it as actionable.**

### Advanced therapeutics

- **Gene therapy:** none. **Not a viable strategy for the gonadal phenotype** — the therapeutic window (embryonic sex determination) closes before diagnosis is possible. Of note, Fang et al. showed that gene therapy restoring PPP2R3C "potently suppressed T cell activation and autoantibody production" in a lupus model (PMID:42298912) — a *different* indication entirely, but proof that PPP2R3C restoration is technically achievable in somatic tissue.
- **Cell therapy, RNA-based therapy (ASO/siRNA/mRNA), targeted therapy, immunotherapy:** none; none in development.
- **Speculative future direction (research only):** because the disorder may reflect *imbalance* rather than pure loss — "imbalanced activity of this centrosomal kinase-phosphatase pair is the shared cause of these disorders" (PMID:39317195) — **MAP3K1/JNK inhibition** is a mechanistically rational rebalancing target, supported by the observation that "MAP3K1 knockout suppresses growth defects caused by PPP2R3C inactivation." This is a cell-biological rescue in immortalized lines with **no in vivo, no gonadal, and no therapeutic evidence**, and the window problem applies. Curate as a `mechanistic_hypotheses` entry, not a treatment.

### Surgical and interventional

| Intervention | Indication | NCIT |
|---|---|---|
| **Gonadectomy** | Germ-cell-tumour risk reduction in 46,XY GD with dysgenetic intra-abdominal gonads. **Timing and necessity are genuinely contested in DSD care** and must be an MDT + shared decision, not a reflex. No PPP2R3C-specific tumour data exist. | `NCIT:C15329` Surgical Procedure; more specifically `NCIT:C51642` Gonadectomy if verified |
| Diagnostic laparoscopy ± gonadal biopsy | Internal anatomy; histology; surveillance | `NCIT:C15329` |
| Omphalocele repair | Neonatal | `NCIT:C15329` |
| Anorectal reconstruction (anal atresia, anteriorly placed anus) | Neonatal/infant | `NCIT:C15329` |
| Pyloromyotomy | Pyloric stenosis | `NCIT:C15329` |
| Cardiac surgery / catheter intervention | ASD, pulmonic stenosis, aortic valve disease | `NCIT:C15329` |
| Hypospadias repair, orchidopexy | Partial GD, male-raised | `NCIT:C15329` |
| Genital/vaginal surgery | **Deferred where possible**; individualized, consent-centred | `NCIT:C15329` |
| Scoliosis and hip dysplasia management | Orthopedic | `NCIT:C16186` Orthopedic Surgical Procedure |
| Cochlear implant / hearing aids | Severe SNHL | Device — `DEVICE` modality; no reliable NCIT clinical-action term |

### Supportive and rehabilitative

| Intervention | NCIT | Modality |
|---|---|---|
| **Multidisciplinary DSD team care** (paediatric endocrinology, genetics, urology, gynaecology, psychology, ethics) | `NCIT:C15747` Supportive Care | — |
| **Genetic counselling** | `NCIT:C15240` Genetic Counseling | — |
| **Psychological / psychosexual support** — essential in DSD; addresses gender identity, disclosure, body image, fertility loss | `NCIT:C181743` Behavioral Counseling | `BEHAVIORAL` |
| **Physical therapy** — myopathy, motor delay, contractures | `NCIT:C15302` Physical Therapy | `BEHAVIORAL` |
| Occupational therapy | `NCIT:C121351` Occupational Therapy | `BEHAVIORAL` |
| Speech and language therapy | `NCIT:C159273` Speech Therapy | `BEHAVIORAL` |
| Low-vision rehabilitation | `NCIT:C15315` Rehabilitation | `BEHAVIORAL` |
| Educational support / early intervention | `NCIT:C15315` | `BEHAVIORAL` |
| Fertility counselling (donor gametes, adoption; **no fertility preservation option** — there is no gamete-producing tissue) | `NCIT:C15240` | — |
| Renal surveillance for the solitary kidney (BP, proteinuria, eGFR) | `NCIT:C15747` | — |
| Bone-density monitoring (DXA) | `NCIT:C15747` | — |

### Experimental treatments

**No clinical trials specific to PPP2R3C-related gonadal dysgenesis or MEGD/GDRM were identified on ClinicalTrials.gov.** No NCT identifiers to report. The disorder has never been the subject of an interventional study.

### Treatment outcomes

- **Response rates:** no trial data. Clinical experience with hormone replacement in hypergonadotropic hypogonadism generally shows reliable induction of secondary sexual characteristics and preservation of bone mass when initiated at an appropriate age; this is extrapolated, not measured in this disorder.
- **Side effects / adverse events:** the expected profile of sex-steroid replacement (thromboembolic risk with estrogen, hepatic and lipid effects, breakthrough bleeding; erythrocytosis, acne, mood effects with testosterone) and of the relevant surgeries. **The irreversibility and consent implications of gonadectomy and genital surgery are the most important "adverse event" considerations in DSD care** and warrant explicit documentation. No FAERS signal is specific to this disorder.

### Treatment strategy

**Pragmatic algorithm (synthesized — no published guideline exists for this disorder):**

1. **Establish the diagnosis** — karyotype + endocrine panel (FSH, LH, testosterone, **AMH**, estradiol, DHEAS) + pelvic imaging + WES (with reanalysis if negative).
2. **Systematic multisystem baseline** — renal US, echocardiogram, bone age, ERG + ophthalmology, audiometry, CK, developmental assessment, brain MRI if indicated, ± lymphocyte subsets.
3. **MDT sex-assignment and management discussion** with the family (and the patient, as capacity develops); defer irreversible genital surgery where feasible.
4. **Correct life-limiting malformations** in the neonatal period.
5. **Induce puberty on time** (~11–13 y) with sex steroids matched to assigned/affirmed gender; escalate to adult replacement.
6. **Manage the gonad** — MDT decision on gonadectomy vs surveillance based on karyotype, gonadal location, and histology.
7. **Sensory and developmental habilitation** — hearing aids/implants, low-vision services, PT/OT/speech, educational support.
8. **Lifelong surveillance** — bone density, solitary-kidney function, cardiac follow-up, vision and hearing progression, psychological wellbeing.
9. **Cascade genetic testing and reproductive counselling** for the family, including SPGF36 counselling for male carriers.

- **Combination therapies:** estrogen + progestin is the only true pharmacological combination.
- **Personalized medicine:** the only genotype/phenotype-guided decision currently supportable is **AMH-guided distinction of complete vs partial GD**, which determines whether virilizing or feminizing replacement is physiologically feasible. No genotype-directed drug choice exists.

---

## 13. Prevention

### Prevention levels

- **Primary prevention (preventing occurrence):** **Not possible for an affected fetus.** Prevention operates entirely at the **reproductive-decision** level:
  - **Genetic counselling** for consanguineous couples and for families with a known variant (25% recurrence risk per pregnancy for carrier × carrier)
  - **Preimplantation genetic testing for monogenic disease (PGT-M)** — available for a known familial variant
  - **Prenatal diagnosis** (CVS/amniocentesis) for a known familial variant
  - **Population-level:** counselling about consanguinity risk in high-prevalence communities; targeted founder-variant (p.L193S) carrier screening in Turkish populations would be technically straightforward but **has never been implemented or evaluated**
- **Secondary prevention (early detection/intervention):** the realistic and highest-yield arm —
  - **Cascade testing** of siblings of an affected child, enabling pre-symptomatic diagnosis and timely intervention (critically important for the **46,XX siblings**, who are systematically under-recognized — Yavuzyilmaz Simsek's 46,XX sibling was identified exactly this way)
  - **Facial-gestalt recognition** in unexplained syndromic DSD and unexplained primary amenorrhea, prompting targeted testing
  - **Phenotype-driven WES reanalysis** in previously undiagnosed syndromic DSD (PMID:42445464)
- **Tertiary prevention (preventing complications in affected individuals):**
  - **Timely pubertal induction** → prevents osteoporosis and psychosocial harm
  - **Adequate lifelong sex-steroid replacement** → bone and cardiovascular health
  - **Gonadal surveillance/gonadectomy** → germ-cell tumour prevention (46,XY GD)
  - **Solitary-kidney nephroprotection** — BP control, avoid nephrotoxins, monitor proteinuria/eGFR
  - **Early hearing and vision intervention** → prevents secondary developmental/educational impairment
  - **Scoliosis and hip surveillance**
  - **Cardiac follow-up** for bicuspid aortic valve/valvulopathy

### Immunization

**No disease-specific vaccine strategy.** Routine schedule applies. **One caveat worth documenting:** given the single reported patient with B and CD4 T lymphopenia (PMID:35812758) and the mouse data on lymphocyte survival, it is prudent to (a) verify vaccine responses if immune abnormality is found, and (b) exercise the standard caution regarding live vaccines in a documented lymphopenia. This is a reasonable clinical inference, **not** a published recommendation.

### Screening and early detection

- **Population screening programs:** none, and none warranted at this rarity.
- **Newborn screening:** not applicable.
- **Genetic screening:** carrier screening (targeted/cascade only), PGT-M, prenatal diagnosis — all for known familial variants.
- **Risk stratification:** the only meaningful stratifier is **family history + consanguinity + ancestry** (Turkish p.L193S founder). No polygenic or clinical risk model exists or is appropriate.

### Behavioral interventions

No lifestyle modification affects occurrence. Post-diagnosis: adherence to hormone replacement, weight-bearing exercise and adequate calcium/vitamin D for bone health, and avoidance of nephrotoxic exposures with a solitary kidney.

### Counselling

**Genetic counselling is the central preventive intervention.** Content should include: autosomal recessive inheritance with 25% recurrence; carrier testing for parents and siblings; **the sex-limited SPGF36 phenotype in heterozygous males** (teratozoospermia/reduced fertility — with honest disclosure that this is reported in one cohort and not confirmed in another); the fact that **both 46,XX and 46,XY siblings can be affected**, so karyotype does not exclude risk; reproductive options (PGT-M, prenatal diagnosis, donor gametes, adoption); and psychosocial support around DSD diagnosis and disclosure.

### Public health and environmental interventions

**Not applicable** — no environmental or communicable dimension. The only population-level lever is consanguinity education/genetic services in high-consanguinity populations.

### Prophylaxis

No prophylactic medication. Gonadectomy functions as **surgical prophylaxis** against germ-cell malignancy in 46,XY GD; calcium/vitamin D and sex steroids function as prophylaxis against hypogonadal bone loss.

---

## 14. Other Species / Natural Disease

### Taxonomy

| Species | NCBI Taxon | Relevance |
|---|---|---|
| *Homo sapiens* | `NCBITaxon:9606` | The only species with reported natural disease |
| *Mus musculus* | `NCBITaxon:10090` | Engineered models only (Section 15) |

### Breed

**Not applicable.** No breed-associated (VBO) condition; no domestic-animal disorder is attributed to *PPP2R3C*.

### Gene — orthologues

| Species | Gene | Identifier |
|---|---|---|
| Human | *PPP2R3C* | NCBI Gene 55012 · ENSG00000092020 |
| Mouse | *Ppp2r3c* | **ENSMUSG00000021022** — Ensembl reports a **one-to-one orthologue** (Eutheria), protein ENSMUSP00000021410. **MGI accession ID was not verified** (MGI's site returned only its search interface to the available tools); look this up manually before curating an MGI cross-reference. |

The gene is broadly conserved across vertebrates; Zhang et al. noted both of their variant positions "demonstrated high conservation across species" (PMID:35812758). PPP2R3C-family members appear well outside vertebrates — the gene has been picked up in non-mammalian genetic studies including sea cucumber papilla-number mapping (PMID:37073167) and Nguni cattle coat-colour genetics (PMID:35747604), though these are incidental locus-level associations with no bearing on the human disease.

### Natural disease in other species

**None known.** No entry in OMIA (Online Mendelian Inheritance in Animals) for a *PPP2R3C* disorder; no companion-animal or wildlife syndrome has been attributed to this gene. Naturally occurring gonadal dysgenesis/DSD is well documented in dogs, horses, pigs, and goats, but the molecular causes identified to date (e.g., *SRY*-negative XX DSD, polled intersex syndrome) do not involve *PPP2R3C*. **Veterinary relevance: none currently.**

### Comparative biology

- **Comparative pathology:** the human and mouse phenotypes are **strikingly discordant in severity**, which is the most important comparative observation in this disorder. The mouse constitutive null dies before gastrulation ("embryonic death from 7.5 dpc or earlier"), so **no mouse recapitulates the human syndrome.** Human patients, all carrying hypomorphic missense/in-frame alleles, are viable with a multisystem but survivable phenotype. Human heterozygotes may have teratozoospermia; heterozygous mice "appeared overtly normal and fertile" (PMID:34714774).
- **Evolutionary conservation of mechanism:** strongly conserved. PP2A holoenzyme architecture, the JNK/MAP3K1 (MEKK1) axis, Hedgehog/GLI transduction, and centriole biology are all deeply conserved, and the mouse gonadal expression pattern (*Tcf21*+ progenitors, *Sox9*+/*Fst*+ supporting cells, with **no sexual dimorphism**) mirrors the human sex-agnostic disease. Conversely, the **SRY→SOX9 initiating switch is mammal-specific**, so non-mammalian models cannot test the sex-determination arm directly.

### Transmission

**Not applicable** — no zoonotic potential, no cross-species susceptibility, no transmissibility. This is a germline Mendelian disorder.

---

## 15. Model Organisms

### Model types

| Model | Type | Source | Key result |
|---|---|---|---|
| **Mouse constitutive *Ppp2r3c* knockout (C57BL/6N, CRISPR/Cas9)** | Mammalian, germline null | **Cicek et al. 2021, PMID:34714774** | **Embryonic lethal.** Heterozygotes "appeared overtly normal and fertile." No homozygous embryos at 14.5 dpc (0/27 embryos; 10 WT, 17 het, P<0.001); at 9.5 dpc "No live homozygous embryos … dead and dying material was identified"; at 8.5 dpc "empty Reichert's membranes were identified … embryo remnants." Conclusion: "loss of function of *Ppp2r3c* is not compatible with viability in mice and results in embryonic death from 7.5 dpc or earlier." |
| **Mouse conditional *G5pr* KO — CD19-Cre (B-cell-specific)** | Mammalian, conditional | Xing et al. 2005, PMID:16129705 | Splenic B cells reduced to 60% of control; B cells hypersensitive to BCR-induced AICD with "increased depolarization of the mitochondrial membrane and the enhanced activation of c-Jun NH(2)-terminal protein kinase and Bim" |
| **Mouse conditional *G5pr* KO — T-cell-specific** | Mammalian, conditional | Xing et al. 2008, PMID:18022237 | "thymic atrophy, significant reduction in thymocyte numbers, particularly a 10-fold decrease in the number of CD4 and CD8 double-positive (DP) thymocytes"; "hyper-activation of JNK and Caspase-3 with augmented Fas ligand (FasL) expression" |
| **G5PR transgenic (overexpression) mouse** | Mammalian, transgenic | PMID:22753944; PMID:25601926 | Impaired affinity maturation; increased peritoneal B-1a cells; **autoantibodies in aged females** — i.e., the gain-of-dosage arm |
| **DepMap genome-wide CRISPR KO across >1000 human cell lines** | Cellular / functional genomics | **Ganga et al. 2024, PMID:39317195** | Co-essentiality: "Among 16,708 genes analyzed, growth phenotypes for *FOP* and *CEP350* were most highly correlated to those of *PPP2R3C*" — the discovery engine for the centrosomal mechanism |
| **RPE1, HeLa, HEK293T, SKNBE2 cell lines** (KO + variant rescue) | In vitro | Ganga et al. 2024, PMID:39317195 | Distal-centriole localization (239 ± 44 nm cylinder); FOP-dependent recruitment; ↑P-Jun in KO; MAP3K1 KO suppression; **L193S patient variant** showed "strongly diminished localization to centrioles" and "diminished binding to FOP" |
| **Hh-dependent medulloblastoma cell line + GLI reporter systems** | In vitro | Baran et al. 2024, PMID:39173855 | PPP2R3C disruption "reduces Hedgehog pathway activity … and reduced growth of a Hh signaling-dependent medulloblastoma cell line"; antagonism with MEKK1 on GLI phosphorylation |
| **Mouse embryonic gonad single-cell RNA-seq (re-analysis)** | Computational / transcriptomic | Cicek et al. 2021, PMID:34714774 | *Ppp2r3c* in "*Tcf21*+ gonadal progenitors at 11.5 dpc and *Sox9*+ and *Fst*+ supporting cells in XY and XX gonads"; "no evidence of any sexual dimorphism in levels of expression" |
| **Human patient gonadal tissue IHC** | Ex vivo human | Guran et al. 2019, PMID:30893644 | "decreased SOX9-Phospho protein expression in the dysgenetic gonads" |
| **Lupus-model gene therapy (T-cell PPP2R3C restoration)** | Mammalian, in vivo | Fang et al. 2026, PMID:42298912 | Restoring PPP2R3C "potently suppressed T cell activation and autoantibody production" — different indication, but demonstrates in vivo restorability |

### Genetic models available

- **Constitutive knockout (mouse):** yes — Cicek 2021 CRISPR/Cas9 line, C57BL/6N. Homozygous-lethal, so maintained as heterozygotes.
- **Conditional knockout (mouse):** yes — a floxed *G5pr* allele exists and has been used with CD19-Cre and a T-cell-specific driver. **This is the key existing resource:** the floxed allele could be crossed to a gonadal driver (e.g., *Sf1*-Cre/*Nr5a1*-Cre, *Wt1*-CreERT2, *Amh*-Cre) to build the gonad-specific model the field lacks.
- **Knock-in (patient-variant humanized) models:** **none exist.** A p.L193S or p.F350S knock-in mouse is the single most valuable missing reagent — hypomorphic knock-ins should survive gastrulation and could be the first model of the actual human syndrome.
- **Transgenic (overexpression):** yes — G5PR Tg mouse.
- **Humanized models:** none.
- **Other species:** **no zebrafish, Drosophila, C. elegans, or Xenopus model** of *PPP2R3C* disease was identified. No iPSC line, organoid, or gonadal-differentiation system from a patient has been reported.
- **Induced (non-genetic) models:** none; not applicable to a developmental genetic disorder.

### Model characteristics

**Phenotype recapitulation — poor, and this is the central limitation of the field.**

| Human feature | Recapitulated? |
|---|---|
| Gonadal dysgenesis (XY and XX) | **No** — constitutive null mice die at/before 7.5 dpc, **well before gonadal differentiation** (~10.5–11.5 dpc). The null cannot express a gonadal phenotype. |
| Facial gestalt, limb, ventral wall, renal, anorectal anomalies | **No** — lethality precedes organogenesis |
| Retinal dystrophy, hearing loss, myopathy | **No** |
| Carrier teratozoospermia (SPGF36) | **No** — heterozygous mice "appeared overtly normal and fertile," directly contradicting the reported human carrier phenotype |
| Lymphocyte survival defect / lymphopenia | **Yes** — conditional B- and T-cell KO reproduce reduced B-cell numbers and DP-thymocyte loss, matching the n=1 human B/CD4 lymphopenia |
| Centrosomal/JNK/Hh molecular lesions | **Yes, in cells** — human cell lines faithfully report the molecular defect and validate the L193S patient allele |
| Gonadal expression at the right time in the right cells | **Yes** — mouse gonadal scRNA-seq places *Ppp2r3c* in exactly the lineages the human disease implicates |

**Model limitations (curate as `HUMAN_MODEL_MISMATCH`, not `KNOWLEDGE_GAP`):**

1. **Severity mismatch / dead-before-the-phenotype.** Evidence *exists* in mouse, but its translational validity is the open question: the null is lethal at ≤7.5 dpc and therefore cannot model a disorder whose defining lesion occurs at 11.5 dpc. All human alleles are hypomorphic missense/in-frame; the mouse null is not the human genotype. Resolution requires a **patient-variant knock-in** or **conditional gonadal deletion**.
2. **Carrier-phenotype mismatch.** Human heterozygous males are reported with teratozoospermia and reduced fertility (PMID:30893644), whereas heterozygous mice are "overtly normal and fertile" (PMID:34714774). Note this discrepancy is *also* present human-to-human — Altunoglu "did not encounter infertility problems in the carriers" (PMID:34750818) — so the mismatch may reflect uncertainty on the human side rather than a species difference. Resolution requires systematic semen analysis across carriers from multiple cohorts.
3. **Cell-line vs gonad.** The centrosomal/JNK mechanism is established in RPE1/HeLa/HEK293T/neuroblastoma cells — **none of which is a gonadal supporting cell**. Whether the same kinase-phosphatase imbalance operates in the differentiating Sertoli/granulosa lineage is inferred, not shown.
4. **Species-restricted sex-determination logic.** The SRY→SOX9 switch is mammal-specific, closing off cheap non-mammalian models for the gonadal arm (though zebrafish or *Drosophila* could still model the Hh/centrosome arms).
5. **No patient-derived cellular system** (fibroblasts, iPSC, gonadal organoid) has been reported.

### Research applications

- **Established:** PP2A B″-subunit substrate targeting; centriole/centrosome regulation and the CEP350–FOP–PPP2R3C axis; JNK-pathway regulation of activation-induced cell death; Hedgehog/GLI phospho-regulation; lymphocyte selection and autoimmunity; multidrug-resistance transporter regulation.
- **Achievable next with existing reagents:** conditional gonadal deletion (floxed allele × *Nr5a1*-Cre) to test the sex-determination hypothesis directly; patient-variant knock-in for the syndromic phenotype; testing MAP3K1/JNK inhibition as a rebalancing intervention in PPP2R3C-deficient cells and gonadal explants; gonadal-lineage differentiation from patient iPSC.
- **Open questions the models should address:** LoF vs gain-of-PP2A-activity (Section 4); whether the extragonadal phenotype is Hh/cilium-mediated; whether the immune phenotype is consistent across patients.

### Resources / databases

- **MGI** (informatics.jax.org) — mouse *Ppp2r3c*; **MGI accession ID unverified in this research, must be looked up manually**
- **Ensembl** — mouse orthologue ENSMUSG00000021022
- **IMPC / KOMP** — *Ppp2r3c* IMPC record was not confirmed; given the demonstrated homozygous lethality, an IMPC "lethal" viability call is expected. Verify manually.
- **DepMap** — the primary functional-genomics resource for this gene (drove PMID:39317195)
- **Alliance of Genome Resources** — orthology and phenotype aggregation
- **Cellosaurus / ATCC** — RPE1, HeLa, HEK293T, SKNBE2
- **IMSR / EMMA / MMRRC** — no publicly deposited *Ppp2r3c* line was located; the Cicek 2021 CRISPR line and the *G5pr*-floxed allele would need to be requested from the originating laboratories (Greenfield/MRC Harwell; Sakaguchi/Kumamoto respectively).

---

## Curation Notes for the dismech Entry

### Named Entity Confusion (NEC) preflight — PASSED

Per `CLAUDE.md` §2b, the mandatory NEC check was performed. This disorder falls into **two** high-NEC-risk classes (shared eponym: "Kennerknecht syndrome"; merged/reclassified synonyms: OMIM 600908 → 618419), so the check matters here.

| Anchor | Expected | Found in sources |
|---|---|---|
| **Causal gene** | *PPP2R3C* | *PPP2R3C* is the dominant gene in every source; no competing gene appears at higher frequency ✅ |
| **OMIM xref** | MONDO:0032738 → OMIM:618419 + OMIM:600908 | Altunoglu 2022 states "GDRM, MIM# 618419" verbatim; MedGen 1679397 → OMIM:618419 ✅ |
| **Synonym check** | "Kennerknecht syndrome", MEGD, GDRM, BKGK | All present in the MONDO/MedGen synonym set; note *Ingo Kennerknecht* is a co-author on Altunoglu 2022, confirming the eponym traces to this entity ✅ |
| **Adjacent-entity trap** | 14q13.2 also hosts *NKX2-1* (Brain-Lung-Thyroid syndrome, PMID:29477862) | Distinct gene, distinct mechanism, CNV-mediated — flagged in Section 4 so it is not conflated ✅ |

### Reference cache status

Cache files already exist in this worktree for the key PMIDs: `PMID_30893644`, `PMID_34714774`, `PMID_34750818`, `PMID_35812758`, `PMID_39317195`, `PMID_37147882`, `PMID_42445464`. Abstracts in `PMID_30893644.md` and `PMID_34750818.md` were read directly and **match the quotations used in this report verbatim**. The following PMIDs cited here are **not yet cached** and require `just fetch-reference` before their snippets are used in YAML: `PMID:39173855`, `PMID:42298912`, `PMID:16129705`, `PMID:18022237`, `PMID:22753944`, `PMID:25601926`, `PMID:16343422`, `PMID:24333728`, `PMID:35290982`, `PMID:29477862`.

### Facts that must be verified manually before curation

1. **gnomAD gene-level constraint** (pLI, LOEUF, missense Z) — the gnomAD browser is a JS app and could not be fetched. **No numeric constraint value is asserted anywhere in this report.**
2. **MGI accession ID for mouse *Ppp2r3c*** — MGI returned only its search interface. Only the Ensembl orthologue ID (ENSMUSG00000021022) is asserted.
3. **Orphanet ORPHA code** — Orphanet was unreachable (bot challenge). MONDO carries no ORPHA xref; recorded as "not found," not "confirmed absent."
4. **OMIM clinical synopses** for 618419 and 618420 — omim.org returned HTTP 403. All OMIM-derived content here is sourced from MedGen, MONDO, HPO annotations, or the primary literature instead.
5. **Per-variant ClinVar assertions** — the gene-level count (118 records) is verified; the pathogenicity-filtered query failed with a backend error.
6. **Guran 2019 sperm-morphology percentages** — the OMIM-derived figure ("96–99% teratozoospermic") came from a web-search summary of the OMIM entry, **not from a verified primary source**. Do not use as an evidence snippet until confirmed against the paper's full text (the EJE and Oxford Academic full texts were both inaccessible: HTTP 525 / abstract-only).

### Recommended module conformance targets

| Module | Node | Confidence |
|---|---|---|
| `photoreceptor_degeneration` | `#Rod Photoreceptor Apoptosis` | Moderate — phenotype fits (rod-cone dystrophy 4/4 in Guran); the specific apoptotic mechanism is not demonstrated in this disorder |
| `sensorineural_hair_cell_loss` | `#Hair Cell Mechanotransduction Failure and Death` | Low–moderate — SNHL present in 25%; mechanism entirely inferred |
| `ciliopathy_dysfunction` | `#Impaired Hedgehog Signal Transduction` | **Moderate–good** — PPP2R3C is a validated positive Hh/GLI regulator (PMID:39173855) and HPA localizes the protein to the primary cilium; the multisystem phenotype (limb, craniofacial, renal agenesis, CNS) is classically Hh/ciliary. Worth curating with an explicit note that formal ciliary-transduction assays in patient tissue are absent. |
| `osteoporosis_bone_resorption` | `#Increased Osteoclastic Bone Resorption` | Low — hypogonadal bone loss is expected but not reported in this cohort; curate only if a patient report supports it |

### Suggested new module (strong candidate)

**`sox9_map3k1_sex_determination_phosphobalance`** — a conserved phospho-balance module for the gonadal supporting-cell fate switch. Trigger nodes would be substitutable: *PPP2R3C* loss-of-restraint (this disorder) or *MAP3K1* gain-of-function (~15–20% of 46,XY GD), converging on the same node — dysregulated SOX9/β-catenin phospho-balance → failure of supporting-cell specification → gonadal dysgenesis. This is unusually well-supported for a proposed module because a single 2024 paper demonstrates the convergence experimentally: "inactivating PPP2R3C mutations and activating MAP3K1 mutations both cause congenital syndromes characterized by gonadal dysgenesis … we propose that imbalanced activity of this centrosomal kinase-phosphatase pair is the shared cause of these disorders" (PMID:39317195). It would also give the KB a natural home for *MAP3K1*-related 46,XY DSD.

### Recommended `discussions` entries

| Kind | Topic |
|---|---|
| `KNOWLEDGE_GAP` | **LoF vs gain-of-PP2A-activity** — Ganga 2024's "inactivating mutations" framing vs Cicek 2021's "upregulate the catalytic function of PP2A" hypothesis are not reconciled (Section 4). Proposed experiments: phosphatase-activity assays on reconstituted holoenzymes carrying each patient allele; phospho-SOX9 quantification in isogenic gonadal-lineage cells. |
| `KNOWLEDGE_GAP` | **Are ocular and muscular involvement core features?** Guran/Cicek (4/4 rod-cone dystrophy, 4/4 myopathy) vs Altunoglu ("supported neither ocular nor muscular involvement as major criteria"). Proposed: prospective ERG + CK + muscle imaging in every genotyped patient, stratified by allele. |
| `KNOWLEDGE_GAP` | **Is immunodeficiency a real phenotype?** n=1 human (B/CD4 lymphopenia) with strong independent mouse support. Proposed: systematic lymphocyte subsets, immunoglobulins, and vaccine-response testing in all known patients. |
| `KNOWLEDGE_GAP` | **Germ-cell tumour risk is entirely unmeasured** in PPP2R3C-related 46,XY GD; gonadectomy recommendations are extrapolated from generic 46,XY GD data. |
| `KNOWLEDGE_GAP` | **Carrier reproductive phenotype (SPGF36)** — conflicting reports; unknown penetrance. |
| `HUMAN_MODEL_MISMATCH` | **Mouse null dies at ≤7.5 dpc, before gonadal differentiation at 11.5 dpc**, so no existing mouse models the human gonadal phenotype; all human alleles are hypomorphic while the mouse allele is a null. Evidence exists in the model but its fidelity to human disease is the open question. Proposed: patient-variant knock-in (p.L193S/p.F350S); conditional deletion with *Nr5a1*-Cre. |
| `HUMAN_MODEL_MISMATCH` | **Heterozygous mice are "overtly normal and fertile"** whereas human male heterozygotes are reported with teratozoospermia/reduced fertility. |

### Prevalence record recommendation

```yaml
prevalence:
- population: Worldwide
  measure_type: CASES_IN_LITERATURE
  prevalence_class: UNKNOWN
  notes: >-
    No prevalence estimate exists. Approximately 19 affected individuals from
    ~12 families reported 2019-2026 (Guran 2019 n=4; Cicek 2021 n=4;
    Altunoglu 2022 n=8; Zhang 2022 n=1; Yavuzyilmaz Simsek 2026 n=2).
    Predominantly Turkish, with Indian and Chinese families.
- population: Chinese 46,XY DSD referral cohort (Peking Union Medical College Hospital)
  measure_type: OTHER
  prevalence_class: UNKNOWN
  notes: >-
    Diagnostic yield rather than population prevalence: PPP2R3C accounted for
    1 of 70 patients (~1.4%) in an unselected 46,XY DSD WES series, versus ~60%
    attributable to AR, SRD5A2 or NR5A1 combined. Possible overlap with the
    Zhang 2022 case report (same institution and authors).
```

---

## Primary Literature — Consolidated Citation List

### Disease-defining reports (all six; the complete clinical literature)

1. **Guran T, Yesil G, Turan S, Atay Z, Bozkurtlar E, Aghayev A, Gul S, Tinay I, Aru B, Arslan S, Koroglu MK, Ercan F, Demirel GY, Eren FS, Karademir B, Bereket A.** PPP2R3C gene variants cause syndromic 46,XY gonadal dysgenesis and impaired spermatogenesis in humans. *Eur J Endocrinol.* 2019 May 1;180(5):291-309. **PMID:30893644** · DOI:10.1530/EJE-19-0067 — *disease-gene discovery; 4 patients; SOX9-phospho IHC; carrier teratozoospermia*
2. **Cicek D, Warr N, Yesil G, Kirkgoz T, Turan S, Kaygusuz SB, Bozkurtlar E, Bereket A, Greenfield A, Guran T.** Broad-spectrum XX and XY gonadal dysgenesis in patients with a homozygous L193S variant in PPP2R3C. *Eur J Endocrinol.* 2021 Dec 1;186(1):65-72. **PMID:34714774** · DOI:10.1530/EJE-21-0910 · PMC8679844 — *extension to 46,XX; mouse CRISPR KO embryonic lethality; gonadal scRNA-seq; Turkish founder effect*
3. **Altunoglu U, Börklü E, Shukla A, Escande-Beillard N, Ledig S, Azaklı H, Nayak SS, Eraslan S, Girisha KM, Kennerknecht I, Kayserili H.** Expanding the spectrum of syndromic PPP2R3C-related XY gonadal dysgenesis to XX gonadal dysgenesis. *Clin Genet.* 2022 Feb;101(2):221-232. **PMID:34750818** · DOI:10.1111/cge.14086 — *largest cohort (8 patients/4 families); novel in-frame duplication; gestalt diagnosis; disputes ocular/muscular criteria*
4. **Zhang W, Mao J, Wang X, Zhao Z, Zhang X, Sun B, Cao Y, Nie M, Wu X.** Case Report: Novel Compound Heterozygotic Variants in PPP2R3C Gene Causing Syndromic 46,XY Gonadal Dysgenesis and Literature Review. *Front Genet.* 2022 Jun 23;13:871328. **PMID:35812758** · DOI:10.3389/fgene.2022.871328 · PMC9259967 — *first non-consanguineous compound het; first Chinese patient; the definitive 17-patient tabulation with frequencies; novel immunological phenotype*
5. **Yavuzyilmaz Simsek F, Arslanoglu İ.** Phenotype-Driven Whole-Exome Sequencing Reanalysis Identifies a Homozygous PPP2R3C Variant in Syndromic 46,XY and 46,XX Gonadal Dysgenesis: Case Report and Review of the Literature. *Mol Syndromol.* 2026 May 29. **PMID:42445464** · DOI:10.1159/000552785 — *most recent report; 46,XY + 46,XX sibling pair; diagnostic value of WES reanalysis*
6. **Zhang W, Mao J, Wang X, Zhao Z, Zhang X, Sun B, Cao Y, Nie M, Wu X.** The genetic spectrum of a Chinese series of patients with 46,XY disorders of the sex development. *Andrology.* 2024 Jan;12(1):98-108. **PMID:37147882** · DOI:10.1111/andr.13446 — *cohort denominator: PPP2R3C in 1/70 (~1.4%) of 46,XY DSD; likely the same patient as ref 4*

### Mechanistic studies

7. **Ganga AK, Sweeney LK, Rubio Ramos A, Wrinn CM, Bishop CS, Hamel V, Guichard P, Breslow DK.** A disease-associated PPP2R3C-MAP3K1 phospho-regulatory module controls centrosome function. *Curr Biol.* 2024 Oct 21;34(20):4824-4834.e6. **PMID:39317195** · DOI:10.1016/j.cub.2024.08.058 · PMC11496028 — *the key mechanistic advance; DepMap co-essentiality; distal-centriole localization; L193S functional validation; PPP2R3C/MAP3K1 unification.* (bioRxiv preprint: **PMID:38617270**)
8. **Baran B, Derua R, Janssens V, Niewiadomski P.** PP2A phosphatase regulatory subunit PPP2R3C is a new positive regulator of the hedgehog signaling pathway. *Cell Signal.* 2024 Nov;123:111352. **PMID:39173855** · DOI:10.1016/j.cellsig.2024.111352 — *GLI interaction; MEKK1(MAP3K1) antagonism; explains the extragonadal phenotype*
9. **Xing Y, Igarashi H, Wang X, Sakaguchi N.** Protein phosphatase subunit G5PR is needed for inhibition of B cell receptor-induced apoptosis. *J Exp Med.* 2005;202(5):707-719. **PMID:16129705**
10. **Xing Y, Wang X, Igarashi H, Kawamoto H, Sakaguchi N.** Protein phosphatase subunit G5PR that regulates the JNK-mediated apoptosis signal is essential for the survival of CD4 and CD8 double-positive thymocytes. *Mol Immunol.* 2008;45(7):2028-2037. **PMID:18022237**
11. **Kitabatake M, et al.** Transgenic overexpression of G5PR that is normally augmented in centrocytes impairs the enrichment of high-affinity antigen-specific B cells, increases peritoneal B-1a cells, and induces autoimmunity in aged female mice. *J Immunol.* 2012. **PMID:22753944**
12. **Kotani T, et al.** JNK regulatory molecule G5PR induces IgG autoantibody-producing plasmablasts from peritoneal B1a cells. *J Immunol.* 2015. **PMID:25601926**
13. **Xing Y, et al.** BCR-crosslinking induces a transcription of protein phosphatase component G5PR that is required for mature B-cell survival. *Biochem Biophys Res Commun.* 2006. **PMID:16343422**
14. **Fang X, Qin Y, Tao J, Zhou Z, Cai M, Zhang H, Li X, Li X, Chen Z.** PPP2R3C serves as a negative regulator associated with reduced T cell hyperactivation and renal protection in lupus. *Clin Transl Med.* 2026 Jun;16(6):e70716. **PMID:42298912** · DOI:10.1002/ctm2.70716
15. **Katayama K, Yamaguchi M, Noguchi K, Sugimoto Y.** Protein phosphatase complex PP5/PPP2R3C dephosphorylates P-glycoprotein/ABCB1 and down-regulates the expression and function. *Cancer Lett.* 2014 Apr 1;345(1):124-31. **PMID:24333728** · DOI:10.1016/j.canlet.2013.12.007

### Context / differential diagnosis

16. **Pathogenic Variants in MAP3K1 Cause 46,XY Gonadal Dysgenesis: A Review.** *Sex Dev.* 2022;16(2-3):92. **PMID:35290982** — *the mechanistically paired disorder*
17. **Villafuerte B, et al.** The Brain-Lung-Thyroid syndrome (BLTS): A novel deletion in chromosome 14q13.2-q21.1. *Eur J Med Genet.* 2018 Jul. **PMID:29477862** — *same cytoband, unrelated disease; NEC guard*

### Database resources consulted

- MONDO — `MONDO:0032738` (via Monarch Initiative API, 2026-08-01)
- MedGen — UID 1679397 / CUI C5193085 (NCBI)
- HPO — curated annotations for `OMIM:618419` and `OMIM:618420` (ontology.jax.org API, 2026-08-01)
- HGNC — `hgnc:17485` (rest.genenames.org)
- UniProt — Q969Q6
- Ensembl — ENSG00000092020; mouse orthologue ENSMUSG00000021022 (rest.ensembl.org)
- Human Protein Atlas — ENSG00000092020-PPP2R3C
- ClinVar — 118 records for *PPP2R3C* (NCBI eSearch, 2026-08-01)
- NIH Genetic Testing Registry — condition C5193085; gene 55012
- DepMap — via PMID:39317195

**Sources (web):**
- [PPP2R3C gene variants cause syndromic 46,XY gonadal dysgenesis (PubMed)](https://pubmed.ncbi.nlm.nih.gov/30893644/)
- [Broad-spectrum XX and XY gonadal dysgenesis with homozygous L193S (PMC8679844)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8679844/)
- [Expanding the spectrum to XX gonadal dysgenesis (PubMed)](https://pubmed.ncbi.nlm.nih.gov/34750818/)
- [Novel compound heterozygotic PPP2R3C variants + literature review (PMC9259967)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9259967/)
- [A disease-associated PPP2R3C-MAP3K1 phospho-regulatory module (PMC11496028)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11496028/)
- [MedGen: Gonadal dysgenesis, dysmorphic facies, retinal dystrophy, and myopathy](https://www.ncbi.nlm.nih.gov/medgen/1679397)
- [Monarch Initiative: MONDO:0032738](https://monarchinitiative.org/MONDO:0032738)
- [NIH GTR: condition C5193085](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5193085/)
- [NIH GTR: PPP2R3C (gene 55012)](https://www.ncbi.nlm.nih.gov/gtr/genes/55012/)
- [Human Protein Atlas: PPP2R3C](https://www.proteinatlas.org/ENSG00000092020-PPP2R3C/tissue)
- [Pathogenic Variants in MAP3K1 Cause 46,XY Gonadal Dysgenesis: A Review](https://pubmed.ncbi.nlm.nih.gov/35290982/)
- [OMIM #618419 MEGD](https://omim.org/entry/618419) · [OMIM #618420 SPGF36](https://omim.org/entry/618420) · [OMIM *615902 PPP2R3C](https://omim.org/entry/615902) *(accessed via search summaries; omim.org returned HTTP 403 to direct fetch)*