---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-30T18:42:51.840263'
end_time: '2026-07-30T18:48:35.618914'
duration_seconds: 343.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypothalamic Hamartoma with Gelastic Seizures
  mondo_id: MONDO:0019484
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
  - claude-sonnet-5
  web_search_requests: 21
  num_turns: 20
  total_cost_usd: 1.9145216999999999
  session_id: 5dd887df-f66e-565b-8209-dadd5bf74d40
  stop_reason: end_turn
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypothalamic Hamartoma with Gelastic Seizures
- **MONDO ID:** MONDO:0019484 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypothalamic Hamartoma with Gelastic Seizures** covering all of the
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

# Hypothalamic Hamartoma with Gelastic Seizures — Comprehensive Research Report

**MONDO:0019484** | **Orphanet: ORPHA86906** ("Gelastic seizures with hypothalamic hamartoma") | **OMIM (syndromic form): #146510** (Pallister-Hall syndrome) | **MedGen: C4707883**

---

## 1. Disease Information

**Overview.** Hypothalamic hamartoma with gelastic seizures (also called gelastic epilepsy–hypothalamic hamartoma syndrome, or HH syndrome) is a rare cerebral malformation-with-epilepsy syndrome caused by a congenital, non-neoplastic heterotopic mass of neurons and glia attached to or within the tuber cinereum/mammillary bodies of the hypothalamus. The lesion is present from fetal life, is histologically benign and non-growing in most cases, but is intrinsically epileptogenic, producing a distinctive early-onset seizure type — **gelastic seizures** (ictal, mirthless laughter) and/or **dacrystic seizures** (ictal crying) — that typically begins in infancy and, if left untreated, evolves into a progressive encephalopathy with multiple seizure types, cognitive decline, and severe behavioral/psychiatric disturbance. A subset of patients additionally present with **central (GnRH-dependent) precocious puberty**. Because the classic clinical picture (gelastic seizures + precocious puberty + developmental delay/cognitive-behavioral decline) is essentially unique to this lesion, this triad is itself diagnostic once hypothalamic hamartoma is confirmed by MRI (MedLink Neurology; GARD).

**Key identifiers:**
- **MONDO:** 0019484
- **Orphanet:** ORPHA86906 (isolated/non-syndromic gelastic-seizure form); ORPHA672 (Pallister-Hall syndrome, the principal syndromic association)
- **OMIM:** No dedicated OMIM number exists for isolated/sporadic hypothalamic hamartoma (it is a somatic/developmental malformation, not classically "Mendelian" in most cases); the syndromic form is captured under **OMIM #146510** (Pallister-Hall syndrome) and **OMIM #277170** (Oral-facial-digital syndrome VI / OFD6, an alternate syndromic association)
- **ICD-11:** Falls under structural focal epilepsy codes (8A62 focal epileptic seizures) combined with congenital malformation of the hypothalamus (LA9Y/LA00 category, structural brain malformations); no unique ICD code exists for HH itself
- **MeSH:** Hamartoma [D006223]; Hypothalamic Diseases [D007027]; Laughter (ictal) is captured under "gelastic epilepsy" in free text/PubMed indexing rather than a discrete MeSH heading
- **MedGen:** C4707883

**Synonyms/alternative names:** Gelastic epilepsy; hypothalamic hamartoma syndrome; tuber cinereum hamartoma; gelastic seizures–hypothalamic hamartoma syndrome; HH with precocious puberty; (when part of the polydactyly/hypopituitarism syndrome) Pallister-Hall syndrome.

**Evidence base composition.** The literature is a mix of: (1) large single- and multi-center **surgical case series** (individual-patient/aggregated clinical data from epilepsy surgery centers — e.g., cohorts of tens to hundreds of patients pooled from endoscopic, open, radiosurgical, and laser-ablation series); (2) **molecular/genetic case-control studies** pairing resected hamartoma tissue with paired leukocyte DNA to find somatic mutations; (3) **single-neuron electrophysiology** studies of intraoperatively resected human HH tissue; and (4) case reports/small case series for the syndromic (Pallister-Hall, OFD6) forms. There is no large population-based disease registry; most epidemiologic estimates are derived from tertiary epilepsy-center catchment calculations (Kerrigan, *Epilepsia* 2017, PMID:28591479 general review context; MedLink Neurology).

---

## 2. Etiology

**Disease causal factors — genetic/mechanistic, not environmental.** Hypothalamic hamartoma is fundamentally a disorder of the **Sonic Hedgehog (SHH) signaling pathway** during hypothalamic morphogenesis. It arises via two overlapping etiologic routes:

1. **Germline heterozygous truncating mutations in *GLI3*** (7p14.1) — causal for the syndromic form, **Pallister-Hall syndrome** (autosomal dominant; OMIM #146510). Kang et al. (Nat Genet, 1997, PMID:9054938) first showed frameshift *GLI3* mutations clustered in the middle third of the gene cause PHS, producing a truncated repressor form of GLI3 that constitutively antagonizes SHH-target gene transcription. Related ciliopathic overlap occurs with **oral-facial-digital syndrome type VI (OFD6, OMIM #277170)**, associated with mutations affecting SHH-pathway cilium components (e.g., *OFD1*).
2. **Somatic (post-zygotic, tissue-limited) mutations** in *GLI3* and other SHH-pathway/ciliary genes, confined to the hamartoma tissue itself and absent (or present at very low allele fraction) in blood. Boudreau et al. (*Neurology*, 2007; doi:10.1212/01.wnl.0000284607.12906.c5) first demonstrated somatic *GLI3* mutations in resected hamartoma tissue from patients without Pallister-Hall syndrome, establishing that **isolated ("non-syndromic") gelastic-seizure HH is itself a genetic (mosaic) disease**, not simply an idiopathic malformation. Saitsu et al. (2016, PMID:27453577, *Ann Clin Transl Neurol*) extended this, finding somatic truncating variants in ***GLI3* and *OFD1***, both regulators of SHH ciliary signaling, in resected HH tissue. A 2022 study (*Hum Mol Genet*, Oxford Academic) framed sporadic HH as **"a ciliopathy with somatic and bi-allelic contributions,"** and a 2024 review (Neurology Genetics, PMID:39246740, "Genetic Insights Into Hypothalamic Hamartoma: Unraveling Somatic Variants") estimates that **somatic variants in SHH-pathway genes (GLI3) and ciliary genes (OFD1) collectively account for roughly ~50% of HH cases** when tumor tissue (not just blood) is sequenced.
3. A minority of cases show **mosaic *GLI3* variants detectable even in peripheral blood** — extending the clinicogenetic spectrum beyond the classic "germline PHS vs. purely somatic sporadic HH" dichotomy (Genetics in Medicine Open, 2023).

**Molecular mechanism of SHH pathway involvement:** In canonical signaling, SHH ligand binding to the receptor **PTCH1** releases inhibition of **SMO**, which localizes to the primary cilium and allows **GLI3** to be processed into its transcriptional-activator form rather than its default repressor form. **OFD1** is a basal-body/ciliary protein required for ciliogenesis and correct GLI3 processing. Loss-of-function or truncating mutations disrupt this processing balance, producing dysregulated SHH-target gene expression during early hypothalamic patterning — disrupting the normal separation of neuroepithelial precursors and yielding an ectopic nodule of hypothalamic-type neurons and glia (heterotopia) rather than a true neoplasm.

**Risk factors:**
- **Genetic:** Family history of Pallister-Hall syndrome (autosomal dominant, ~50% transmission risk per affected parent, though ~25% of PHS cases are de novo); somatic/mosaic *GLI3*/*OFD1* variants (not inherited, not predictable by family history — sporadic).
- **Environmental/demographic:** No established toxin, infectious, or lifestyle risk factor. **Male sex is a consistent, replicated risk factor**, with most series reporting a male:female ratio of roughly 1.3:1 for HH with epilepsy (Kerrigan 2017 review; multiple epidemiologic sources). No parental age, teratogen, or perinatal-exposure risk factor has been robustly established, consistent with the lesion's origin in very early (first-trimester) hypothalamic neurodevelopment.
- Over 90–95% of cases are **sporadic**, unassociated with any identifiable syndrome (search results consistently cite this figure across GARD/NORD and MedGen sources).

**Protective factors:** None specifically established in the literature; no genetic variant is documented to reduce hamartoma occurrence, and no dietary/lifestyle protective factor has been studied given the prenatal/developmental origin of the lesion.

**Gene-environment interactions:** Because pathogenesis is driven by early embryonic (first-trimester) SHH-pathway disruption, gene-environment interaction data are essentially absent from the literature; this is a purely genetic/developmental (not multifactorial-acquired) disease model.

---

## 3. Phenotypes

### Core seizure phenotype
- **Gelastic seizures** (ictal, unprovoked, mirthless laughter without an accompanying subjective sense of mirth) — the hallmark and usually the presenting seizure type, typically starting in **infancy, often within the first months to first year of life**. Seizures are brief (2–30 seconds), stereotyped, and frequently occur many times per day, sometimes clustering. Consciousness is characteristically preserved or only mildly altered during the gelastic event itself. Accompanying **autonomic features** are common: tachycardia, facial flushing, altered respiration, pupil dilation. HPO: **HP:0100716 (Gelastic seizures)**.
- **Dacrystic seizures** (ictal crying) — common in infants/young children, sometimes preceding or alternating with laughing spells. HPO: consider under **HP:0002123 (Seizure)** more broadly; a dedicated "dacrystic seizure" HPO term is not standard, so map to HP:0100716 sibling terms/generic seizure terms as appropriate, noting the phenotype in free text.
- **Secondary generalization/other seizure types**: as the disease progresses (often over years), most patients develop additional focal seizures (with impaired awareness), tonic, atonic, or generalized tonic-clonic seizures, reflecting "secondary epileptogenesis" in extra-hypothalamic networks. HPO: **HP:0007359 (Focal-onset seizure)**, **HP:0002069 (Bilateral tonic-clonic seizure)**, **HP:0011153 (Focal aware seizure)**.
- **Drug-resistant epilepsy**: gelastic seizures in particular are notoriously refractory to antiseizure medications — probably <5% of patients achieve seizure freedom with medical therapy alone (Cross et al., *Epilepsia* 2017, PMID:28591485). HPO: **HP:0025191 (Drug-resistant seizures)**.
- **EEG**: Interictal/ictal scalp EEG is frequently unrevealing or non-lateralizing for gelastic events — in one series, **56% of patients with gelastic seizures and 75% of individual gelastic events showed no discernible ictal scalp EEG change**, reflecting the deep, subcortical origin of the ictal generator (search results, MedLink/Barrow Neurological Institute reviews).

### Endocrine phenotype
- **Central (GnRH-dependent) precocious puberty** — occurs in a large minority to majority of patients (co-occurring in an estimated ~63% of patients in some series; "hypothalamic hamartomas are the most frequent CNS cause of precocious puberty in very young children"). Onset can be as early as infancy. HPO: **HP:0000826 (Precocious puberty)**.
- **Hypopituitarism/growth hormone deficiency** — chiefly seen in the Pallister-Hall syndromic form, where hormone abnormalities (including cortisol deficiency) can be life-threatening in the neonatal period. HPO: **HP:0000864 (Hypopituitarism)**, **HP:0000824 (Growth hormone deficiency)**.

### Cognitive/behavioral phenotype
- **Developmental delay / intellectual disability**: cognitive impairment reported in **>80% of patients** in some series; profile ranges from normal cognition (particularly patients presenting primarily with precocious puberty and infrequent seizures) to severe intellectual disability, and can be **progressive** over the disease course. HPO: **HP:0001263 (Global developmental delay)**, **HP:0001249 (Intellectual disability)**.
- **Behavioral/psychiatric disturbance — "rage attacks"**: **50–80%** of children with HH show severe rage/aggression; ~43% show significant aggression and ~20% exhibit classic "rage attacks" — sudden, explosive, often unprovoked anger outbursts, described as affective (not predatory) aggression tied to poor frustration tolerance. Many patients meet criteria for **ADHD, oppositional defiant disorder, and conduct disorder**. HPO: **HP:0000718 (Aggressive behavior)**; consider **HP:0000752 (Hyperactivity)**, **HP:0000737 (Irritability)**.
- **Factors predicting worse cognitive/behavioral outcome**: larger hamartoma volume, earlier seizure onset, higher seizure frequency, and polytherapy with multiple antiseizure medications (systematic review data, Corbet Burcher et al., *Dev Med Child Neurol* 2019).
- Natural history is notably **progressive**: behavioral disruption and intellectual impairment can *predate* clinically overt epilepsy, and — left untreated — the syndrome tends toward worsening seizures, cognitive decline, and behavioral deterioration over childhood, whereas patients who present later in life (adult-onset recognition) tend to have a milder overall phenotype.

### Quality-of-life impact
Direct disease-specific EQ-5D/SF-36 data are sparse in the literature searched; qualitative data consistently emphasize major impact on schooling, family functioning, and social integration driven by uncontrolled seizures plus rage attacks; psychiatric outcomes (aggression, ADHD-spectrum symptoms) have been shown to **improve after successful surgical treatment** in multiple series, underscoring that much of the morbidity is seizure/network-driven rather than fixed structural damage.

---

## 4. Genetic/Molecular Information

**Causal genes:**
| Gene | HGNC | Role | Context |
|---|---|---|---|
| *GLI3* | hgnc:4319 | SHH-pathway zinc-finger transcription factor (activator/repressor) | Germline heterozygous truncating variants → Pallister-Hall syndrome (OMIM #146510); somatic truncating/frameshift variants in resected hamartoma tissue → isolated/sporadic HH |
| *OFD1* | hgnc:2317 | Ciliary basal-body protein required for ciliogenesis/GLI processing | Somatic truncating variants in hamartoma tissue (Saitsu et al. 2016, PMID:27453577); germline variants → OFD syndrome type VI (OMIM #277170), X-linked |
| *PTCH1* | hgnc:9585 | SHH receptor | Implicated as part of the broader "SHH pathway" candidate-gene set in HH tissue sequencing (search results reference PTCH1's canonical mechanistic role; direct HH-causal somatic variants are less consistently reported than for GLI3/OFD1) |

**Variant classification and type:** In Pallister-Hall syndrome, causal *GLI3* variants are **predominantly frameshift or nonsense (truncating) mutations clustering in the middle third of the gene** (exons 14–15 region), producing a constitutively repressive GLI3 fragment — a distinctive genotype-phenotype pattern relative to the N-terminal missense variants that cause Greig cephalopolysyndactyly syndrome (allelic disorder). ACMG/AMP classification of reported variants is typically Pathogenic/Likely Pathogenic given the recurrent truncating mechanism and segregation/de novo occurrence data (ClinVar/GeneReviews).

**Somatic vs. germline origin:** This is the central genetic feature distinguishing isolated HH from the syndromic form:
- **Germline** heterozygous *GLI3* truncating variant → Pallister-Hall syndrome (systemic phenotype: HH + polydactyly + bifid epiglottis + hypopituitarism, etc.)
- **Somatic/mosaic**, tissue-limited to the hamartoma (undetectable or only trace-level in blood) → isolated HH with gelastic seizures, no extra-CNS features. A minority of "somatic" cases have since been shown to have **low-level mosaic variants detectable in blood** with sensitive sequencing (Genetics in Medicine Open, 2023), blurring what was once a strict dichotomy.
- Detection requires **paired tumor-tissue/leukocyte high-depth exome sequencing**, since standard peripheral blood-only clinical genetic testing will **miss purely somatic HH-restricted variants**.

**Functional consequence:** Loss-of-function/truncating mechanism predominates — producing a dominant-negative or haploinsufficient GLI3 repressor isoform that disrupts SHH-pathway transcriptional output during hypothalamic patterning, rather than a classic oncogenic gain-of-function mechanism (distinguishing HH mechanistically from a true neoplasm).

**Allele frequency:** Because these are private (family-specific germline) or somatic/mosaic (not represented in blood-derived population reference panels) variants, gnomAD/1000 Genomes population allele frequencies are essentially zero/not applicable — consistent with these being rare, highly penetrant, individually private disease-causing variants rather than common susceptibility alleles.

**Modifier genes:** No specific modifier-gene literature identified in this search; hamartoma volume/location (Delalande type) is the dominant driver of phenotypic severity (see Sections 6–7) rather than a documented second-locus genetic modifier.

**Epigenetic information:** Not established in the literature reviewed; no DNA methylation/histone-modification studies specific to HH tissue were surfaced.

**Chromosomal abnormalities:** Boudreau et al. (*Am J Hum Genet*, ScienceDirect/PMC2427231) identified **somatic chromosomal abnormalities at the GLI3 locus (7p14)** in hypothalamic hamartoma tissue via chromosomal microarray, reinforcing that somatic copy-number/structural changes at the GLI3 locus (not only point mutations) contribute to sporadic HH pathogenesis.

---

## 5. Environmental Information

No specific environmental toxin, occupational exposure, radiation, or infectious trigger has been established as causal for hypothalamic hamartoma — consistent with its origin as an early embryonic (first-trimester) SHH-pathway developmental malformation rather than an acquired or exposure-driven disease. No lifestyle risk factor (smoking, diet, alcohol) has documented association. No infectious agent is implicated. This section is essentially **not applicable** for this disease, distinguishing it from acquired epilepsies (e.g., post-infectious or post-traumatic).

---

## 6. Mechanism / Pathophysiology

**Causal chain — from developmental lesion to seizure network:**

1. **Trigger (prenatal):** Germline or somatic *GLI3*/*OFD1* loss-of-function/truncating mutation disrupts SHH-pathway ciliary signal transduction during early hypothalamic neuroepithelial patterning (first trimester).
2. **Structural consequence:** Ectopic heterotopic nodule of hypothalamic-type gray matter (mixed neurons + glia) forms, attached to or within the tuber cinereum/floor of the third ventricle, adjacent to mammillary bodies — the hypothalamic hamartoma. This is a **static, congenital malformation**, not a proliferative neoplasm (it does not enlarge via cell division in the way a tumor would, though relative growth can occur with age/brain growth).
3. **Cellular/molecular basis of intrinsic epileptogenicity:** Within the hamartoma, **~80–90% of neurons are small, GABAergic, interneuron-like cells** expressing glutamic acid decarboxylase (GAD) with an intrinsic, pacemaker-like capacity to fire spontaneously even in the absence of synaptic input (Wu et al., *Epilepsia* 2015, PMID:25495642, "Mechanisms of Intrinsic Epileptogenesis in Human Gelastic Seizures with Hypothalamic Hamartoma"). A minority population of **large HH neurons** exhibits an immature, depolarizing response to GABA (rather than the normal hyperpolarizing adult response), consistent with a **reversed transmembrane chloride gradient** (elevated intracellular Cl⁻, likely via persistent NKCC1/reduced KCC2 expression, an immature-neuron signature). **GABA_A receptors on the small neurons show marked functional "rundown"** with repetitive GABA exposure, and **gap junctions electrically couple the small GABAergic neuron population**, synchronizing their spontaneous firing into a coherent oscillatory network capable of generating clinical seizures (Kerrigan, *Epilepsia* 2017, PMID:28591479 context article "Hypothalamic hamartoma: Neuropathology and epileptogenesis"). This yields a **"GABA-mediated paradoxical excitation" model** of intrinsic epileptogenesis — GABA, normally inhibitory in the mature CNS, instead drives network synchronization and seizure generation within the hamartoma.
4. **Network propagation ("secondary epileptogenesis"):** Ictal discharges originating within the hamartoma propagate via hypothalamic connections (mammillothalamic tract, hypothalamo-hypophyseal and limbic connections) to cortical and subcortical networks, explaining why scalp EEG often fails to capture the deep intrinsic discharge directly, and why chronic HH activity can "kindle" extrahypothalamic (often mesial temporal/frontal) secondary epileptogenic foci over time — the presumed substrate for the observed **progressive emergence of additional (non-gelastic) seizure types and cognitive/behavioral decline** with disease duration.
5. **Endocrine mechanism (precocious puberty):** Two mechanistic hypotheses are supported by tissue studies: (a) some hamartomas contain **ectopic GnRH-secreting neurons** acting as an autonomous, hypothalamic-feedback-independent pulse generator; (b) alternatively/additionally, hamartoma astroglial cells express **transforming growth factor-alpha (TGFα)**, which via glia-to-neuron signaling activates the endogenous hypothalamic GnRH pulse generator prematurely (Jung et al., PMID:20389100, found puberty onset correlated with **anatomic contact/size** of the lesion with the tuber cinereum/infundibulum rather than strictly with GnRH/TGFα/KISS1 expression level, suggesting a mechanical/contact-mediated activation component alongside the molecular signaling routes).

**Molecular pathway:** Sonic Hedgehog (SHH) signaling — PTCH1 (receptor) → SMO (derepressed upon SHH binding) → primary cilium-localized processing of GLI3 into activator vs. repressor isoforms → GLI-target gene transcription controlling hypothalamic progenitor patterning. GO term: **GO:0007224 (smoothened signaling pathway)**; **GO:0060831 (Hedgehog signaling pathway involved in dorsal/ventral neural tube patterning)**.

**Cellular processes:** aberrant neuronal migration/heterotopia formation during hypothalamic morphogenesis; abnormal GABAergic interneuron chloride homeostasis (immature Cl⁻ gradient); gap-junction-mediated electrical synchronization; ciliogenesis defects (via OFD1).

**Protein dysfunction:** GLI3 — loss-of-function truncation yielding an aberrant obligate-repressor fragment (dominant-negative/haploinsufficient mechanism) rather than a misfolding/aggregation disease.

**Tissue damage mechanism:** Not a degenerative/necrotic process; pathology is a static developmental malformation whose damage to the host is **functional (seizure-network-mediated and endocrine-mediated)** rather than progressive tissue destruction, though secondary cortical network changes from chronic seizures may occur.

**Molecular profiling:** Whole-exome sequencing and chromosomal microarray of resected hamartoma tissue paired with leukocyte DNA is the primary "omics" modality used clinically/in research (rather than transcriptomics/proteomics/metabolomics, which are not well represented in the literature for this lesion). Immunohistochemistry shows GFAP, S-100, vimentin, synaptophysin (SYN) positivity, and partial EGFR staining, confirming mixed glioneuronal composition without malignant features (Coons et al., "Histopathology of Hypothalamic Hamartomas: Study of 57 Cases," PMID:17278998).

**Suggested ontology terms:**
- GO: GO:0007224 (smoothened signaling pathway), GO:0021884 (forebrain neuron development), GO:0034765 (regulation of ion transmembrane transport — chloride homeostasis)
- CL: CL:0000099 (interneuron), CL:0000125 (glial cell), CL:0002608 (GABAergic neuron)
- UBERON: UBERON:0001891 (hypothalamus), UBERON:0002435 (tuber cinereum), UBERON:0002264 (mammillary body)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Hypothalamus — specifically the tuber cinereum, floor of the third ventricle, and mammillary body region. UBERON: **UBERON:0001891 (hypothalamus)**; **UBERON:0002435 (tuber cinereum)**.
- **Secondary/system involvement:** Nervous system (epilepsy network — limbic/temporal/frontal secondary foci), endocrine system (hypothalamic-pituitary-gonadal axis dysregulation causing precocious puberty; hypothalamic-pituitary-adrenal/growth axis in Pallister-Hall syndrome), and — in Pallister-Hall syndrome specifically — skeletal system (polydactyly), laryngeal (bifid epiglottis), gastrointestinal (imperforate anus), and renal systems.

**Tissue/cell level:** Mixed glioneuronal tissue — small GABAergic interneuron-like cells (~80–90% of neuronal population) plus a minority of large "ganglion cell"-like neurons, interspersed with fibrillary astrocytes and oligodendrocytes; architecture classically described as nodular "grape-like" clusters (Coons et al., PMID:17278998). CL: **CL:0000099 (interneuron)**; **CL:0000127 (astrocyte)**.

**Subcellular level:** Primary cilium (site of GLI3 processing; disrupted by OFD1 dysfunction) — GO Cellular Component: **GO:0005929 (cilium)**, **GO:0097546 (ciliary base)**. Neuronal plasma membrane chloride transporters (NKCC1/KCC2 balance) underlying the immature GABA response.

**Localization:** Intrahypothalamic, at or adjacent to the third ventricle floor; can be **pedunculated** (attached by a stalk, more often associated with precocious puberty/endocrine presentation) or **sessile** (broadly attached along the hypothalamic floor, more often associated with the epileptic/gelastic-seizure phenotype and cognitive-behavioral disease) — this pedunculated-vs-sessile and Delalande anatomic classification (see Section 8) is central to both clinical phenotype prediction and surgical planning. Lesions are typically **midline or slightly lateralized**; bilateral or large "giant" (Delalande type III/IV) lesions carry the worst seizure and neuroendocrine prognosis.

---

## 8. Temporal Development

**Onset:**
- The malformation is **congenital** (present from fetal development), but clinical **seizure onset is typically in infancy** — often within the first year of life, sometimes the first weeks to months, making early-onset gelastic seizures one of the most specific "red-flag" seizure semiologies in infantile epilepsy.
- **Precocious puberty**, when present, likewise typically manifests in **infancy/very early childhood**, sometimes as the presenting sign preceding recognized seizures.
- **Onset pattern:** typically insidious with brief, easily-missed gelastic events initially, which can be misattributed to normal infant giggling/crying before being recognized as seizures.

**Progression:**
- **Disease course is classically progressive** in children: gelastic/dacrystic seizures → emergence of additional focal and generalized seizure types → progressive cognitive decline and worsening behavioral/psychiatric disturbance (rage attacks, ADHD-spectrum symptoms), attributed to "secondary epileptogenesis" (kindling of extrahypothalamic networks).
- **Progression rate is variable**: some patients have a rapidly deteriorating course in early childhood, while others (particularly those identified in adulthood, often via incidental imaging or isolated precocious puberty) show a comparatively **benign, non-progressive course** with normal cognition and infrequent seizures (Sciencedirect, "The benign spectrum of hypothalamic hamartomas: Infrequent epilepsy and normal cognition in patients presenting with central precocious puberty").
- **Disease duration:** chronic/lifelong unless treated; the hamartoma itself does not resolve spontaneously, though seizure frequency/severity and cognitive trajectory can be substantially altered by intervention.

**Patterns:**
- **Remission:** essentially only achieved via surgical/ablative treatment (endoscopic disconnection, LITT, radiofrequency ablation, stereotactic radiosurgery, open resection); spontaneous remission of gelastic seizures is rare and antiseizure-medication-induced remission is uncommon (<5% of patients optimally controlled on medication alone).
- **Critical periods:** Early childhood is considered a critical window for intervention — earlier treatment (before extensive secondary epileptogenesis and before prolonged rage/cognitive decline become entrenched) is associated with better long-term cognitive/behavioral outcomes, motivating current practice trends toward earlier surgical referral rather than prolonged medical-therapy trials.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence estimates vary across sources** from **1 in 50,000 to 1 in 1,000,000**, with commonly cited figures of **1–2 per 100,000** population and, specifically for HH presenting with epilepsy, **~1 per 200,000 children/adolescents**. The condition is estimated to account for only **~0.1% of all epilepsies**.
- **Sex ratio:** Male predominance, with a ratio of roughly **1.3:1 (male:female)** reported for HH with epilepsy across multiple series.
- Co-occurrence figures from one referenced series: precocious puberty in **63%**, epileptic seizures in **61%**, and both together in **25%** of patients (search-derived figures; exact denominators/cohort vary by study — treat as indicative rather than a single definitive population statistic).

**Inheritance pattern:**
- **Isolated/sporadic HH (>90–95% of cases):** not inherited — arises from **somatic (post-zygotic) mosaic mutation**, confined largely or entirely to hamartoma tissue; recurrence risk to siblings/offspring is not elevated above general population baseline.
- **Pallister-Hall syndrome (OMIM #146510):** **autosomal dominant**, due to germline heterozygous *GLI3* mutation; **~25% of PHS cases are de novo**, the remainder inherited from an affected (sometimes mildly/incompletely penetrant) parent.
- **Oral-facial-digital syndrome VI (OMIM #277170):** X-linked pattern in classic OFD subtypes, though the specific inheritance of OFD6 is less uniformly characterized in the literature reviewed.

**Penetrance/expressivity:** Within Pallister-Hall syndrome, **variable expressivity** is well documented — some *GLI3*-mutation carriers present with minimal findings (e.g., isolated polydactyly, incidentally discovered HH) while others have the full life-threatening neonatal phenotype (panhypopituitarism, imperforate anus, respiratory compromise from bifid epiglottis); the search results specifically note asymptomatic/incidental HH discovery even in adults with confirmed PHS mutations, consistent with incomplete/variable clinical penetrance of the hypothalamic component itself.

**Genetic anticipation, germline mosaicism, founder effects, consanguinity, carrier frequency:** No robust evidence for genetic anticipation in PHS (not a repeat-expansion disorder). Germline/gonadal mosaicism is plausible given autosomal dominant transmission with de novo cases but is not extensively quantified in the literature surfaced. No founder-population effect or consanguinity association identified — consistent with the private, per-family/per-patient nature of both germline PHS mutations and (especially) somatic sporadic-HH mutations. Carrier-frequency/gnomAD data are not meaningfully applicable given the private/de novo/somatic mutational spectrum.

**Population demographics:** No specific ethnic or geographic predilection has been established in the sources reviewed; case reports span diverse populations (including the cited first Colombian PHS case, PMC12508622), consistent with a pan-ethnic, sporadic mutational mechanism rather than a population-specific founder variant. Age distribution of clinical presentation skews strongly to **infancy/early childhood** for the epileptic phenotype, with a recognized smaller subset of **adult-onset-recognized** (often incidentally discovered or late-diagnosed) cases that tend to have a milder overall course.

---

## 10. Diagnostics

**Imaging (primary diagnostic modality):**
- **MRI** is the diagnostic gold standard: the lesion appears as a **non-enhancing, isointense-to-hypointense-on-T1, hyperintense-on-T2** mass contiguous with (attached to or within) the hypothalamus/tuber cinereum, without contrast enhancement, edema, or mass effect progression typical of a true neoplasm. A **dedicated 3T epilepsy-protocol MRI** (thin-slice coronal/sagittal sequences through the hypothalamus) is considered essential, since small lesions are easily missed on routine brain MRI.
- **Delalande & Fohlen anatomic classification (2003, PMID:12627881)** — the key clinical/surgical staging system:
  - **Type I:** horizontal plane of attachment entirely below the floor of the third ventricle (extraventricular)
  - **Type II:** vertical plane of attachment to the third-ventricle walls, entirely above the floor (intraventricular)
  - **Type III:** combined vertical + horizontal attachment (both above and below the floor)
  - **Type IV:** "giant" hamartomas, without a clearly defined boundary from type III
  - This classification correlates directly with surgical approach selection and with **prognosis**: Type II lesions have the best surgical seizure outcome (up to ~68.7% Engel class I), while Type IV lesions are the most difficult to treat and often require staged/multiple ablation procedures.

**EEG:** limited sensitivity for gelastic seizures specifically (56–75% of gelastic events show no discernible scalp ictal change), though useful for characterizing secondary/generalized seizure types and interictal epileptiform activity as the disease progresses. Stereo-EEG (SEEG) can be used pre-surgically in complex cases (e.g., to guide stereo-array radiofrequency thermocoagulation of giant HH).

**Genetic testing:**
- **Recommended approach:** Because most isolated HH is driven by **somatic, tissue-restricted** mutation, standard blood-only genetic testing (single-gene *GLI3* sequencing, gene panels, or even blood WES) will frequently be **negative** in sporadic cases; **paired resected-tumor-tissue plus leukocyte high-depth exome sequencing** (or targeted deep resequencing of *GLI3*/*OFD1*/SHH-pathway candidate genes) is the correct diagnostic strategy for research/mechanistic confirmation.
- **Blood-based germline *GLI3* single-gene sequencing** is appropriate and indicated when the clinical picture suggests **Pallister-Hall syndrome** (HH + polydactyly ± bifid epiglottis ± hypopituitarism ± imperforate anus) — a heterozygous truncating *GLI3* variant is diagnostic.
- **Chromosomal microarray (CMA)** of hamartoma tissue has identified somatic copy-number/structural abnormalities at the GLI3 locus (7p14) in some sporadic cases.
- **Whole genome/exome sequencing (WGS/WES)** of tumor-normal pairs is the most sensitive current research approach for detecting low-allele-fraction somatic mosaicism; blood-only mosaic-variant detection (via deep/error-corrected sequencing) has more recently been shown to detect a subset of cases (Genetics in Medicine Open, 2023).
- Karyotyping/FISH, mitochondrial DNA testing, and repeat-expansion testing are **not routinely indicated** for this disease (no evidence implicating these mechanisms).

**Endocrine/laboratory testing:** GnRH-stimulation test and basal LH/FSH for suspected central precocious puberty; standard pituitary hormone panel (GH, cortisol, thyroid axis) especially when Pallister-Hall syndrome is suspected, given risk of life-threatening panhypopituitarism/adrenal insufficiency in infancy.

**Histopathology (when tissue obtained via resection):** Confirms mixed glioneuronal composition (small GABAergic interneuron-like cells + occasional large ganglion-type neurons + glia), GFAP/S-100/vimentin/synaptophysin immunopositivity, absence of mitotic activity or malignant features — distinguishing HH from a low-grade glioneuronal neoplasm (Coons et al., PMID:17278998).

**Clinical diagnostic criteria (gelastic seizures):** recurrent, stereotyped fits of laughter; absence of an external precipitating/context-appropriate trigger; laughter incongruous with mood/context; laughter occurring together with other epileptic clinical manifestations; ictal/interictal epileptiform EEG changes when present (criteria synthesized from PMC7595796/ruralneuropractice review).

**Differential diagnosis:** Pathological/pseudobulbar laughing (post-stroke, ALS), gelastic cataplexy (narcolepsy), frontal/temporal lobe epilepsy with gelastic component from other structural lesions, and — for the syndromic form — other acrocallosal/polydactyly syndromes (Greig cephalopolysyndactyly, Bardet-Biedl) must be distinguished from Pallister-Hall syndrome.

**Screening:** No population newborn-screening program exists (this is a structural, not metabolic, disease); however, early recognition of gelastic seizures in infancy functions as an informal "clinical screening" trigger prompting urgent hypothalamic-protocol MRI, and genetic counseling/*GLI3* testing is appropriate when polydactyly or other PHS features co-occur.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Hypothalamic hamartoma itself is not directly lethal as a static malformation, but drug-resistant epilepsy from HH carries a recognized **risk of sudden unexpected death in epilepsy (SUDEP)**, reported to occur at **a rate comparable to other surgically-treated epilepsy populations**; drug-resistant epilepsy in general carries a SUDEP risk that "can exceed 5% per decade," and this risk is a specific driver of the rationale for early surgical referral rather than prolonged medical-therapy trials. In Pallister-Hall syndrome specifically, **neonatal panhypopituitarism/adrenal insufficiency can be acutely life-threatening** if unrecognized, representing the syndrome's main mortality risk in infancy (rather than the hamartoma/epilepsy per se).

**Morbidity/function:**
- Untreated, the natural history trends toward progressive **cognitive decline, worsening seizure burden (multiple additional seizure types), and severe behavioral/psychiatric morbidity** (rage attacks, ADHD/ODD/conduct-disorder-spectrum presentations) — reported in the majority of pediatric patients.
- **Endocrine morbidity**: precocious puberty causes early growth-plate closure/compromised adult height and psychosocial impact if untreated; hypopituitarism (in PHS) causes growth failure and other hormone-deficiency morbidity.

**Disease course/complications:** Secondary generalized epilepsy, cognitive decline, psychiatric comorbidity (aggression, mood/anxiety disorders), and school/social dysfunction are the principal complications. **Surgical/ablative treatment complications** include hypothalamic injury (reported in ~7% of patients across a large pooled surgical series) and broader hypothalamic/endocrine complications in ~10.4% of patients (diabetes insipidus, further hormonal disturbance, weight gain/hyperphagia risk) — an important counterbalancing consideration against the benefits of intervention.

**Recovery potential:** Substantial and well-documented **improvement in seizure control, cognition, and behavior following successful surgical/ablative disconnection or removal** of the hamartoma — psychiatric/behavioral outcomes specifically have been shown to improve postoperatively in multiple series, and earlier intervention is associated with better long-term cognitive trajectory, supporting a "window of opportunity" model of prognosis.

**Prognostic factors:**
- **Delalande anatomic type** is the single most consistently reported prognostic factor for surgical seizure freedom (best for Type II, worst for Type IV).
- **Hamartoma volume** (larger = worse prognosis, more likely to require staged/multiple ablations).
- **Ablation completeness** (rate of hamartoma-body ablation achieved) correlates with seizure outcome for LITT/radiofrequency approaches.
- Earlier seizure onset, higher seizure frequency, and antiseizure-medication polytherapy predict worse cognitive outcome.

---

## 12. Treatment

**Pharmacotherapy:** Antiseizure medications are **largely ineffective specifically against gelastic seizures**, though they may reduce frequency of the secondary (non-gelastic) seizure types that emerge with disease progression; **no particular antiseizure drug has demonstrated superiority** over others for HH-related epilepsy (Cross et al., *Epilepsia* 2017, PMID:28591485, "Medical management and antiepileptic drugs in hypothalamic hamartoma"). Probably fewer than 5% of patients achieve adequate seizure control on medication alone. MAXO: **MAXO:0000XXX pharmacotherapy generically maps to NCIT:C15986** (no HH-specific drug class exists; standard broad-spectrum antiseizure medications such as levetiracetam, valproate, oxcarbazepine are used empirically).

**Surgical and interventional approaches (mainstay of definitive treatment):**
- **Endoscopic disconnection**: aims to disconnect (rather than fully resect) the intrinsically epileptogenic hamartoma from surrounding hypothalamic/thalamic networks, based on the Delalande/Fohlen hypothesis that disconnection alone can achieve seizure control. Across a large pooled cohort, **77.6% achieved a favorable outcome (Engel I+II)**, with **57.1% fully seizure-free (Engel I)**; a separate very large multi-procedure series reported **47.0% (243/517) seizure freedom** after the index procedure across all approaches. MAXO: **MAXO:0000004 (surgical procedure)**.
- **Open microsurgical resection** (transcallosal, transventricular, subfrontal, or pterional approaches depending on lesion anatomy).
- **Magnetic Resonance-guided Laser Interstitial Thermal Therapy (MRgLITT)**: increasingly regarded as a **first-line, minimally invasive** treatment; one series of 47 patients reported **72.3% gelastic-seizure-free** and an overall **68.1% Engel class I** rate; another series reported **81% completely gelastic-seizure-free** at last follow-up; hospital stay as short as **2.6 days** reflects low morbidity. **Robot-assisted** and **staged (multi-session)** LITT protocols exist for larger/giant lesions. MAXO term mapping: closest fit is **MAXO:0000004 (surgical procedure)** combined with a device/ablation qualifier — dismech `therapeutic_modality` would map this to **DEVICE**/**SURGERY**-adjacent ablation.
- **Stereotactic radiofrequency thermocoagulation** (including SEEG-guided, high-density focal stereo-array approaches) — an option particularly described for giant pediatric HH, with long-term single-center outcome data reported.
- **Stereotactic radiosurgery (Gamma Knife)**: an alternative especially for lesions not amenable to direct surgical access; overall seizure-freedom rates are **inferior to LITT and comparable open/endoscopic series**, though it remains a valid option in select cases (e.g., adults, deep/inaccessible lesions).
- **Comparative summary**: LITT seizure-freedom outcomes are reported as **superior to stereotactic radiosurgery, craniotomy, or neuroendoscopy, and comparable to radiofrequency ablation** — driving the shift toward LITT as an emerging first-line modality, particularly for Delalande Type I–III lesions; **Type IV ("giant") lesions remain the most difficult to cure with any single-modality approach** and often require staged/combination treatment.

**Adjunctive/supportive neuromodulation and dietary therapy:** **Vagus nerve stimulation (VNS)** and the **ketogenic diet** have both been tried as adjuncts but are **largely ineffective for HH-specific gelastic seizures**, though they retain a role in managing the secondary (non-gelastic) seizure burden in some patients, analogous to their use in other refractory epilepsies (e.g., combined VNS + ketogenic diet "rational polytherapy" data from Lennox-Gastaut literature, PMID:17241211, extrapolated cautiously to HH).

**Endocrine treatment:** GnRH-agonist therapy (e.g., leuprolide) for central precocious puberty is standard and effective at halting/reversing pubertal progression, independent of whether the seizure component is surgically treated. Hormone replacement (growth hormone, cortisol, thyroid hormone, desmopressin for diabetes insipidus) is required for hypopituitary features, especially in Pallister-Hall syndrome.

**Rehabilitative/supportive care:** Neuropsychological support, behavioral therapy (targeting rage attacks/ADHD-spectrum symptoms), and educational support are important components of comprehensive management, particularly given the high burden of cognitive/behavioral morbidity independent of seizure control.

**Experimental/advanced therapeutics:** No gene therapy, RNA-based therapy, targeted molecular therapy, or immunotherapy is in clinical use or trial specifically for hypothalamic hamartoma at this time (consistent with its nature as a static, resectable/ablatable structural lesion rather than a progressive molecular disease amenable to systemic targeted therapy); ablative/surgical technology (LITT, robot-assisted ablation, SEEG-guided thermocoagulation) represents the active area of therapeutic innovation instead.

**Treatment strategy/algorithm:** Given poor medical response, current practice trends favor **early referral to epilepsy surgery evaluation** rather than prolonged antiseizure-medication trials, with modality selection (endoscopic disconnection vs. LITT vs. radiosurgery vs. open resection vs. stereotactic thermocoagulation) guided principally by **Delalande anatomic type and hamartoma volume**.

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense — because HH arises from early embryonic somatic/germline mutation, there is no known modifiable environmental/behavioral risk factor to target for primary prevention. The only "primary prevention" analog is **genetic counseling and reproductive planning** for families with a confirmed germline *GLI3* pathogenic variant (Pallister-Hall syndrome), including discussion of **prenatal diagnosis / preimplantation genetic testing** where the familial variant is known.

**Secondary prevention (early detection/intervention):** The most actionable "prevention" strategy in this disease is **early clinical recognition of gelastic seizures in infancy** (a highly specific red-flag semiology) to trigger prompt hypothalamic-protocol MRI and early referral to surgical evaluation — since earlier intervention is associated with better cognitive/behavioral prognosis and reduced risk of secondary epileptogenesis. Similarly, early recognition and treatment of central precocious puberty (with GnRH agonists) prevents adverse growth/psychosocial sequelae.

**Tertiary prevention:** Comprehensive multidisciplinary management (epilepsy surgery, endocrine hormone replacement, neuropsychiatric/behavioral therapy, educational support) aims to prevent/limit complications (SUDEP risk from ongoing drug-resistant epilepsy, panhypopituitary crisis in PHS, progressive cognitive/behavioral decline).

**Genetic counseling:** Recommended for families with confirmed Pallister-Hall syndrome (autosomal dominant, up to 50% recurrence risk per pregnancy from an affected parent, though ~25% of cases are de novo) — including surveillance recommendations for at-risk relatives (screening for polydactyly, imaging for asymptomatic HH, endocrine screening).

**Immunization/public health/prophylaxis:** Not applicable — no infectious, vaccine-preventable, or public-health-modifiable component to this disease.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary/companion-animal disease directly analogous to hypothalamic hamartoma with gelastic seizures was identified in this search (no OMIA entry or veterinary case-series literature surfaced). This is consistent with the disease being a rare, human-specific clinical entity defined largely by human neurodevelopmental/hypothalamic anatomy and the specific human semiology of "gelastic" (laughing) seizures, which has no established veterinary correlate. NCBI Taxon: **NCBITaxon:9606 (Homo sapiens)** only for this specific clinical phenotype; broader SHH-pathway gene conservation (Gli3 orthologs) is extensive across vertebrates (see Model Organisms, below) but manifests as limb-patterning/craniofacial phenotypes rather than a hamartoma-with-gelastic-seizure phenotype in other species.

---

## 15. Model Organisms

**Primary model: mouse (*Mus musculus*), *Gli3* mutants**
- The classical **"extra-toes" (Gli3^Xt^) mouse** is the principal *Gli3*-pathway model, but it primarily recapitulates **Greig cephalopolysyndactyly syndrome (GCPS)** — the allelic disorder caused by different (typically N-terminal missense/haploinsufficient) *GLI3* variants — rather than Pallister-Hall syndrome specifically. Heterozygous Gli3^Xt-J^ mice show variable preaxial polydactyly; homozygotes die in utero with multiple malformations (JAX strain 000026).
- **Forebrain phenotype:** Homozygous Xt/Xt mutant mouse embryos fail to develop an olfactory bulb or lateral-ventricle choroid plexus and lack normal cerebral cortical lamination by E16.5, demonstrating *Gli3*'s essential, dosage-sensitive role in forebrain/diencephalic (hypothalamic-adjacent) patterning — mechanistically relevant background even though this specific model is not a direct HH/gelastic-seizure phenocopy.
- **Truncating (repressor-form) *Gli3* mouse alleles**, which more closely mimic the Pallister-Hall-type truncating mutation mechanism (as opposed to the simple loss-of-function Xt alleles), have been used in the broader Gli3 mouse-genetics literature to model PHS-like polydactyly and hypothalamic/pituitary patterning defects, though the search did not surface a dedicated, well-characterized "hypothalamic hamartoma" histological phenocopy in mouse — this remains a **partial model-limitation/translational gap**: existing Gli3 mouse alleles recapitulate the limb (polydactyly) and broad forebrain patterning phenotypes of GLI3 dysfunction well, but a mouse model directly reproducing the discrete hypothalamic heterotopic nodule + spontaneous GABAergic hyperexcitability phenotype seen in human HH tissue has not been clearly established in the literature retrieved.
- **Applications:** Gli3 mouse models remain the standard tool for studying SHH-pathway dosage effects on limb and forebrain patterning, and for genotype-phenotype correlation work relevant to the broader GLI3-disease spectrum (GCPS, PHS, isolated postaxial polydactyly), even though direct modeling of the human HH lesion and its electrophysiological (spontaneous GABAergic pacemaker) phenotype currently relies on **ex vivo human hamartoma tissue electrophysiology** (single-neuron recordings from surgically resected specimens) rather than an in vivo rodent hamartoma model.
- **Resources:** MGI (Gli3 gene page); IMSR/JAX (strain 000026, extra-toes-J); no dedicated ZFIN/FlyBase/WormBase model was identified as relevant to this specific hypothalamic phenotype, reflecting that HH pathophysiology is best studied to date in human resected tissue rather than invertebrate/non-mammalian systems.

---

## Summary Table: Suggested Ontology Term Bindings

| Concept | Suggested term | ID |
|---|---|---|
| Disease | Hypothalamic hamartoma with gelastic seizures | MONDO:0019484 |
| Gelastic seizures | Gelastic seizures | HP:0100716 |
| Precocious puberty | Precocious puberty | HP:0000826 |
| Global developmental delay | — | HP:0001263 |
| Intellectual disability | — | HP:0001249 |
| Aggressive/rage behavior | Aggressive behavior | HP:0000718 |
| Drug-resistant seizures | — | HP:0025191 |
| Hypopituitarism | — | HP:0000864 |
| Growth hormone deficiency | — | HP:0000824 |
| Causal gene (isolated/somatic + PHS germline) | GLI3 | hgnc:4319 |
| Causal gene (SHH-pathway ciliary, somatic) | OFD1 | hgnc:2317 |
| SHH receptor (pathway context) | PTCH1 | hgnc:9585 |
| Molecular pathway | Smoothened signaling pathway | GO:0007224 |
| Cell type — small GABAergic HH neuron | GABAergic neuron | CL:0002608 |
| Cell type — glia | Glial cell | CL:0000125 |
| Anatomical site | Hypothalamus | UBERON:0001891 |
| Anatomical site | Tuber cinereum | UBERON:0002435 |
| Anatomical site | Mammillary body | UBERON:0002264 |
| Subcellular structure (ciliopathy mechanism) | Cilium | GO:0005929 |
| Syndromic association | Pallister-Hall syndrome | OMIM:146510 |
| Syndromic association | Oral-facial-digital syndrome VI | OMIM:277170 |
| Treatment — surgical/ablative | Surgical procedure | MAXO:0000004 |

---

Sources:
- [Orphanet: Gelastic seizures with hypothalamic hamartoma (ORPHA86906)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=86906)
- [Hypothalamic hamartomas with gelastic seizures – GARD (NIH)](https://rarediseases.info.nih.gov/diseases/19084/hypothalamic-hamartomas-with-gelastic-seizures)
- [Hypothalamic hamartomas with gelastic seizures – NORD](https://rarediseases.org/mondo-disease/hypothalamic-hamartomas-with-gelastic-seizures/)
- [Hypothalamic hamartomas with gelastic seizures – MedGen C4707883](https://www.ncbi.nlm.nih.gov/medgen/1642420)
- [Gelastic seizures with hypothalamic hamartoma – MedLink Neurology](https://www.medlink.com/articles/gelastic-seizures-with-hypothalamic-hamartoma)
- [Hypothalamic Hamartoma – StatPearls (NCBI Bookshelf)](https://www.ncbi.nlm.nih.gov/books/NBK560663/)
- [GLI3 frameshift mutations cause autosomal dominant Pallister-Hall syndrome – Nature Genetics](https://www.nature.com/articles/ng0397-266)
- [OMIM #146510 – Pallister-Hall Syndrome](https://omim.org/entry/146510)
- [Orphanet: Pallister-Hall syndrome](https://www.orpha.net/en/disease/detail/672)
- [Case Report: Whole-Exome Sequencing of Hypothalamic Hamartoma From an Infant With Pallister-Hall Syndrome (PMC8493334)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8493334/)
- [Sporadic hypothalamic hamartoma is a ciliopathy with somatic and bi-allelic contributions – Human Molecular Genetics](https://academic.oup.com/hmg/article-abstract/31/14/2307/6524341)
- [Genetic Insights Into Hypothalamic Hamartoma: Unraveling Somatic Variants – Neurology Genetics (PMID:39246740)](https://pubmed.ncbi.nlm.nih.gov/39246740/)
- [Mutations of the Sonic Hedgehog Pathway Underlie Hypothalamic Hamartoma with Gelastic Epilepsy (PMID:27453577)](https://pubmed.ncbi.nlm.nih.gov/27453577/)
- [Mosaic variants detectable in blood extend the clinicogenetic spectrum of GLI3-related hypothalamic hamartoma – Genetics in Medicine Open](https://www.gimopen.org/article/S2949-7744(23)00819-1/fulltext)
- [Identification of Somatic Chromosomal Abnormalities in Hypothalamic Hamartoma Tissue at the GLI3 Locus – ScienceDirect/AJHG](https://www.sciencedirect.com/science/article/pii/S0002929708000815)
- [Mechanisms of Intrinsic Epileptogenesis in Human Gelastic Seizures with Hypothalamic Hamartoma – PMC4303488 (PMID:25495642)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4303488/)
- [Hypothalamic hamartoma: Neuropathology and epileptogenesis – Epilepsia](https://onlinelibrary.wiley.com/doi/full/10.1111/epi.13752)
- [Firing Behavior and Network Activity of Single Neurons in Human Epileptic Hypothalamic Hamartoma – PMC3873534](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3873534/)
- [The histopathology of hypothalamic hamartomas: study of 57 cases – PubMed (PMID:17278998)](https://pubmed.ncbi.nlm.nih.gov/17278998/)
- [Magnetic Resonance-Guided Laser Interstitial Thermal Therapy for Hypothalamic Hamartoma: Surgical Approach and Treatment Outcomes – PMC9658093](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9658093/)
- [Laser interstitial thermal therapy: A first line treatment for seizures due to hypothalamic hamartoma? – Epilepsia (PMID:28591480)](https://pubmed.ncbi.nlm.nih.gov/28591480/)
- [Robot-assisted laser interstitial thermal therapy for drug-resistant epilepsy in hypothalamic hamartoma – PMC11216431](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11216431/)
- [One-Stage High-Density Focal Stereo-Array SEEG-Guided Radiofrequency Thermocoagulation for Pediatric Giant Hypothalamic Hamartomas – PMC7493627](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7493627/)
- [Disconnecting surgical treatment of hypothalamic hamartoma in children and adults with refractory epilepsy and proposal of a new classification – PubMed (PMID:12627881)](https://pubmed.ncbi.nlm.nih.gov/12627881/)
- [Outcome of Surgery for Hypothalamic Hamartoma-Related Epilepsy – Neurology](https://www.neurology.org/doi/10.1212/WNL.0000000000210060)
- [Seizure outcome and complications following hypothalamic hamartoma treatment in adults: endoscopic, open, and Gamma Knife procedures – PubMed (PMID:22680243)](https://pubmed.ncbi.nlm.nih.gov/22680243/)
- [Medical management and antiepileptic drugs in hypothalamic hamartoma – Epilepsia (PMID:28591485)](https://onlinelibrary.wiley.com/doi/10.1111/epi.13758)
- [Central precocious puberty due to hypothalamic hamartomas correlates with anatomic features but not with expression of GnRH, TGFalpha, or KISS1 – PubMed (PMID:20389100)](https://pubmed.ncbi.nlm.nih.gov/20389100/)
- [The benign spectrum of hypothalamic hamartomas: Infrequent epilepsy and normal cognition in patients presenting with central precocious puberty – ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1059131112002555)
- [Some Hypothalamic Hamartomas Contain Transforming Growth Factor-α But Not LHRH Neurons – JCEM](https://academic.oup.com/jcem/article/84/12/4695/2864786)
- [Aggression in Hypothalamic Hamartoma – StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK545233/)
- [Neuropsychiatric profile of paediatric hypothalamic hamartoma: systematic review and case series – Developmental Medicine & Child Neurology](https://onlinelinelibrary.wiley.com/doi/10.1111/dmcn.14241)
- [Psychiatric comorbidity with hypothalamic hamartoma: Systematic review for predictive clinical features – ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1525505017302603)
- [Gelastic seizures associated with hypothalamic hamartomas: update in clinical presentation, diagnosis and treatment – Taylor & Francis](https://www.tandfonline.com/doi/full/10.2147/ndt.s2173)
- [Clinical features and evolution of the gelastic seizures–hypothalamic hamartoma syndrome – Epilepsia](https://onlinelibrary.wiley.com/doi/full/10.1111/epi.13753)
- [A mouse model of Greig cephalo-polysyndactyly syndrome: the extra-toesJ mutation contains an intragenic deletion of the Gli3 gene – Nature Genetics](https://www.nature.com/articles/ng0393-241)
- [Extra-toes (Xt) homozygous mutant mice demonstrate a role for the Gli-3 gene in forebrain development – PubMed](https://pubmed.ncbi.nlm.nih.gov/7976186/)
- [JAX Strain 000026 – extra toes](https://www.jax.org/strain/000026)
- [Pallister-Hall Syndrome: Clinical and MR Features – AJNR](https://www.ajnr.org/content/20/10/1839)
- [New Pathogenic Variant in the GLI3 Gene in the First Colombian Patient Associated With Pallister-Hall Syndrome – PMC12508622](https://pmc.ncbi.nlm.nih.gov/articles/PMC12508622/)