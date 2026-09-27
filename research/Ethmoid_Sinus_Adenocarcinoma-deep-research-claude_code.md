---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-28T13:13:28.132469'
end_time: '2026-08-28T13:26:58.389310'
duration_seconds: 810.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ethmoid Sinus Adenocarcinoma
  mondo_id: ''
  category: ''
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 13
  num_turns: 43
  total_cost_usd: 4.672205999999999
  session_id: bb911651-0fb3-44b7-8a20-485c3a465cb4
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 1
citation_count: 38
reference_validation:
  total_references: 45
  verified: 45
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 37
  quotes_valid: 24
  quotes_unsupported: 13
  unsupported_quote_references:
  - PMID:19950227
  - PMID:8685214
  - PMID:31047725
  - PMID:16041693
  - PMID:18702897
  - PMID:38791973
  - PMID:32353928
  - PMID:41303732
  - PMID:10534159
  - PMID:34622832
  - PMID:11177030
  - PMC:PMC3195981
  relevance_assessed: 45
  on_topic: 36
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ethmoid Sinus Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Ethmoid Sinus Adenocarcinoma** covering all of the
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

# Ethmoid Sinus Adenocarcinoma — Comprehensive Research Report

**Prepared:** 2026-08-28 · **Target concept:** Ethmoid sinus adenocarcinoma (MONDO:0002418) · **Category:** Head and neck cancer / rare cancer / occupational cancer

---

## Scope note, read first

**The literature is almost entirely sinonasal-level, not ethmoid-subsite-level.** Nearly every molecular, occupational, and outcome study cited below is reported for *sinonasal adenocarcinoma* or, more narrowly, *sinonasal intestinal-type adenocarcinoma (ITAC)* pooled across sinus subsites. The ethmoid is the subsite ITAC most characteristically occupies — roughly 40% of ITAC by subsite in one recent review, and ~85% when the ethmoid and adjacent upper nasal cavity are counted together — which is why MONDO:0002418 is a workable anchor. But there is no MONDO class for sinonasal ITAC, and the mapping is imperfect: some ethmoid adenocarcinomas are non-ITAC, and some ITACs arise in the maxillary sinus or nasal cavity. **Where a claim below is sinonasal-level rather than ethmoid-specific, it is marked.** A future MONDO ITAC class would be the better anchor for most of this content.

---

## 1. Disease Information

### Overview

Adenocarcinoma of the ethmoid sinus is the glandular (non-squamous, non-salivary) malignancy of the sinonasal tract, and the ethmoid labyrinth is the sinus subsite it most characteristically occupies. Two biologically distinct entities sit under the heading:

- **Intestinal-type adenocarcinoma (ITAC)** — a tumour that reproduces the morphology *and* immunophenotype of colorectal epithelium (CDX2, CK20, MUC2, SATB2, villin) in a sinus containing no intestinal tissue of origin. This is the classic occupational cancer of the head and neck.
- **Non-intestinal-type adenocarcinoma (non-ITAC)** — a rarer, non-salivary, non-enteric group split into low-grade and high-grade forms; the low-grade form is increasingly understood as seromucinous-gland-derived (PMID:35322195).

ITAC's defining clinical behaviour is **local aggression without much metastatic drive**: "These tumors are locally aggressive with frequent local recurrences in up to 50% of cases. Metastasis to regional lymph nodes and distant metastasis are less frequent (10%). **Invasion of the duramater and local recurrence are frequent and the major cause of death**" (Llorente et al., *Eur Arch Otorhinolaryngol* 2009; PMID:18560862).

### Identifiers

| System | Value | Notes |
|---|---|---|
| **MONDO** | `MONDO:0002418` — *ethmoid sinus adenocarcinoma* | Verified via OLS. No MONDO class exists for sinonasal ITAC. |
| **NCIT (subsite)** | `NCIT:C6237` — *Ethmoid Sinus Adenocarcinoma* | Verified via OLS. |
| **NCIT (histology)** | `NCIT:C116316` — *Sinonasal Adenocarcinoma, Intestinal-Type*; `NCIT:C160977` — *Sinonasal Adenocarcinoma, Non-Intestinal-Type* | NCIT also codes the Barnes patterns individually: papillary `NCIT:C160984`, colonic `NCIT:C160986`, solid `NCIT:C160987`, mucinous `NCIT:C160995`. **NCIT is substantially better resolved for this disease than MONDO.** |
| **ICD-10** | C31.1 (malignant neoplasm of ethmoidal sinus) | |
| **ICD-O-3 morphology** | 8144/3 (adenocarcinoma, intestinal type); 8140/3 (adenocarcinoma, NOS) for non-ITAC | |
| **ICD-11** | 2C20 block (malignant neoplasms of accessory sinuses) | Exact leaf code not verified in this search. |
| **OMIM** | Not applicable — no Mendelian entry; this is a somatic, exposure-driven cancer. | |
| **Orphanet** | No dedicated ITAC ORPHA code confirmed in this search. | |

### Synonyms

Sinonasal intestinal-type adenocarcinoma; ITAC; adenocarcinoma of the ethmoid sinus; ethmoidal adenocarcinoma; "woodworker's nasal cancer" (historical/colloquial); papillary-tubular cylinder cell adenocarcinoma of the inner nose (Kleinsasser terminology).

### Data provenance

All content below is derived from **aggregated disease-level resources** — published case series, registry analyses (SEER), systematic reviews, and molecular cohort studies. No individual-patient EHR-derived content is used.

---

## 2. Etiology

### 2.1 Primary causal factor: occupational hardwood and leather dust

This is the strongest exposure–histology association in head and neck oncology, and it is **specific to the adenocarcinoma histology** rather than to sinonasal cancer generally.

**Binazzi et al., *BMC Cancer* 2015 (PMID:25885319)** — 28 studies (11 cohort, 17 case-control) meta-analysed:

> "Exposure to wood dust results associated with SNC (RRpooled = 5.91, 95% CI: 4.31-8.11 for the case-control studies and 1.61, 95% CI: 1.10-2.37 for the cohort studies), as well as to leather dust (11.89, 95% CI: 7.69-18.36). **The strongest associations are with adenocarcinomas (29.43, 95% CI: 16.46-52.61 and 35.26, 95% CI: 20.62-60.28 respectively)**."

The same paper reports **an exposure–response relationship for wood dust (p = 0.001)** — a Bradford Hill criterion that matters for causal inference.

Note the magnitude comparison this enables: pooled RR ≈ 29 (wood) and ≈ 35 (leather) for adenocarcinoma, versus RR ≈ 5.9 / 11.9 for sinonasal cancer of all histologies. The adenocarcinoma-specific effect is roughly an order of magnitude above the all-histology effect.

**Other occupational exposures** from the same meta-analysis (sinonasal cancer, all histologies): nickel and chromium compounds RR 18.0 (95% CI 14.55–22.27); textile industry RR 2.03 (1.47–2.80); formaldehyde RR 1.68 (1.37–2.06, case-control) and 1.09 (0.66–1.79, cohort); construction RR 1.62 (1.11–2.36).

**Formaldehyde is a specific caution.** It is a confounder of wood-dust exposure (co-exposure in woodworking is near-universal), and its independent contribution to *adenocarcinoma* is weak. Holmila et al. found that "adjustment for formaldehyde affected the ORs only slightly" (PMID:19950227). A 2025 review states that established carcinogens including formaldehyde and asbestos have **not** been confirmed for adenocarcinoma development specifically (Sciacca et al., *Medicina* 2025; PMID:41303732).

**IARC classification.** Wood dust is IARC Group 1 (carcinogenic to humans), with the 1995 Monograph (Vol. 62) finding a clear association specifically between adenocarcinoma of the nasal cavity/paranasal sinuses and hardwood dust. **Latency is very long — mean ~40 years from first exposure (range 7–70 years)**, which is the single most operationally important etiologic fact for both compensation and surveillance.

**Attributable fraction.** A 2025 review reports "88% of ITAC cases attributed to occupational exposure," with wood dust the primary factor followed by textile products; the remaining ~12% are sporadic, occur disproportionately in women, and carry a worse prognosis (PMID:41303732). Odds ratio for the wood-dust→adenocarcinoma-histology association specifically: **OR 12.6 (95% CI 5.0–31.6)** (PMID:19950227).

**Other reported exposures.** Cork dust has been proposed as an additional risk exposure in a retrospective cohort (PMC7531325); the evidence base is much thinner than for wood/leather.

### 2.2 Genetic risk factors

**There is no established Mendelian or common-variant susceptibility for this tumour.** It is not a hereditary cancer syndrome, and no GWAS has been performed at usable scale (the disease is far too rare).

One finding deserves flagging as **new and unreplicated**: Riobello et al. sequenced 50 ITACs with 29 matched germline samples and reported "**the first report on hereditary germline mutations in ITAC**" — 11 germline mutations in 8 of 29 matched cases, concentrated in DNA-damage-response genes (ATM, BRCA1, BRCA2) (*Cancers* 2021; PMID:34638506). The companion paper makes the methodological point that this cuts both ways: "Matched tumor/germline comparison in 27 cases revealed that **57% were in fact germline variants**" — i.e. tumour-only sequencing of ITAC massively over-calls somatic drivers (PMID:33500480). Whether these germline DDR variants represent genuine predisposition or incidental population variation is unresolved.

### 2.3 Environmental / demographic risk factors

- **Occupation** (dominant): woodworking, furniture and cabinet making, sawmilling, joinery, carpentry; leather tanning and shoemaking; textile work.
- **Sex**: overwhelmingly male — 94.7% male in a 1,126-case ethmoid/sphenoid ITAC meta-analysis (PMID:34622832). This is almost certainly occupational-cohort composition rather than a biological sex effect; note that sporadic (non-occupational) ITAC is enriched in women.
- **Age**: mean 64.7 years in the ethmoid/sphenoid meta-analysis; ITAC predominantly affects males aged 50–64 (PMID:41303732). A Pakistani series reported a notably younger mean of 44 years (range 22–79), suggesting geographic/occupational-pattern variation (PMID:39924774).
- **Tobacco smoking**: **not an established risk factor for ITAC.** Holmila et al.: "Smoking did not influence the occurrence of TP53 mutation; however, it was associated with multiple mutations (p = 0.03)." The mutational-signature work confirms tobacco signatures appear only in smokers and are not the ITAC-defining signal (PMID:38711096).

### 2.4 Protective factors

**No genetic protective variants are known.** Environmental protection is entirely engineering/administrative: dust extraction at source, respiratory protection, and enforced occupational exposure limits. Under EU Directive 2017/2398 (amending the Carcinogens and Mutagens Directive), the binding OEL for inhalable hardwood dust was set at 3 mg/m³ for a transitional five years and then **lowered to 2 mg/m³** (effective 17 January 2023; Germany adopted 2 mg/m³ in March 2021). This threshold is directly informed by the dose–response data: Holmila et al. found TP53-mutation risk significantly elevated at average exposure **>2 mg/m³ (OR 3.6, 95% CI 1.2–10.8)** and cumulative exposure ≥30 mg/m³·years (OR 3.5, 1.2–10.7).

### 2.5 Gene–environment interaction

The best-characterised gene–environment interaction in this disease is **wood dust × TP53**, and it is a dose-dependent one:

> "Risk of TP53 mutation was significantly increased in association with duration (≥24 years, OR 5.1, 95% CI, 1.5-17.1), average level (>2 mg/m³; OR 3.6, 95% CI, 1.2-10.8) and cumulative level (≥30 mg/m³ × years; OR 3.5, 95% CI, 1.2-10.7) of wood-dust exposure" (PMID:19950227).

Whole-genome sequencing gives the mechanistic complement: "Mutation burden was higher in samples of wood dust-exposed patients (p = 0.016). **Reactive oxygen species (ROS) damage-related mutational signatures were almost exclusively identified in ITAC subtype samples (p = 0.00055)**" (Sipilä et al., *Genes Environ* 2024; PMID:38711096). The signatures involved are COSMIC SBS18/SBS36 — oxidative-damage signatures, not direct-adduct signatures. This is the molecular evidence for the "inflammation-mediated, not directly genotoxic" model of wood-dust carcinogenesis.

---

## 3. Phenotypes

### 3.1 Presenting clinical features

Symptoms are **unilateral, non-specific, and easily mistaken for chronic rhinosinusitis**, which is the principal driver of late-stage presentation. Barnes' original 17-case series recorded "Unilateral nasal obstruction and epistaxis, **averaging 6.8 months in duration**, were the most common symptoms" (PMID:3953940).

| Phenotype | Type | HPO suggestion | Frequency / notes |
|---|---|---|---|
| Unilateral nasal obstruction | Symptom | `HP:0001742` Nasal obstruction | Most common presenting symptom; unilaterality is the red flag |
| Epistaxis | Sign | `HP:0000421` Epistaxis | Co-dominant presenting symptom |
| Rhinorrhoea | Symptom | `HP:0031417` Rhinorrhea | Common; often blood-tinged |
| Hyposmia / anosmia | Symptom | `HP:0004409` Hyposmia; `HP:0000458` Anosmia | Reflects olfactory cleft / cribriform involvement |
| Facial or periorbital pain, headache | Symptom | `HP:0002315` Headache | Later; suggests bony/perineural extension |
| Proptosis | Sign | `HP:0000520` Proptosis | Lamina papyracea breach → orbital invasion |
| Diplopia | Symptom | `HP:0000651` Diplopia | Orbital/extraocular muscle involvement |
| Epiphora | Sign | `HP:0009926` Epiphora | Nasolacrimal duct obstruction |
| Sinonasal mass / paranasal sinus neoplasm | Sign | `HP:0030072` Paranasal sinus neoplasm | The anchoring structural phenotype |
| Secondary sinusitis | Sign | `HP:0000246` Sinusitis | Obstruction-driven; a common misdiagnosis |
| Cranial neuropathy | Sign | `HP:0006824` Cranial nerve paralysis | Advanced skull-base disease |

A 48-patient series confirms the pattern: "Most patients were presented with nasal blockage and difficulty in breathing" (PMID:39924774).

### 3.2 Phenotype characteristics

- **Age of onset**: adult, typically 6th–7th decade (mean 64.7 y in the ethmoid/sphenoid meta-analysis). Effectively determined by the ~40-year exposure latency. Never congenital or paediatric.
- **Onset pattern**: insidious. Median symptom duration before diagnosis ~6.8 months (PMID:3953940).
- **Severity**: variable at presentation, but **stage is advanced in most cases** — Franchi et al. found "92.6% of patients had T3 or T4 carcinomas" (PMID:10534159).
- **Progression**: progressive, locally destructive, without spontaneous remission.
- **Laterality**: characteristically **unilateral** at presentation; bilateral extension occurs late via the perpendicular plate/septum.

### 3.3 Quality-of-life impact

No ITAC-specific EQ-5D / SF-36 / PROMIS data were identified in this search — this is a genuine gap. Qualitatively, the QoL burden is driven by (a) permanent anosmia/hyposmia after resection of the olfactory cleft, (b) orbital exenteration when the orbit is invaded, (c) chronic crusting and nasal dryness after extensive endoscopic resection, and (d) xerostomia/visual toxicity from adjuvant radiotherapy to a field abutting the optic apparatus. **Flag as a knowledge gap.**

---

## 4. Genetic / Molecular Information

### 4.1 The headline result: no characterising driver

This is the most important single molecular statement about ITAC, and it is unusual for a carcinoma with such a stereotyped morphology:

> "The wide spectrum of gene mutations suggests that **ITAC is a genetically heterogeneous without specific characterizing gene mutations**" — Riobello et al., *Cancers* 2021 (PMID:34638506).

The same group found "**72% of tumors affected by gene defects in Wnt, DNA-damage response, MAPK and/or PI3K pathways**" — but "**not in a mutually exclusive manner**," and "None of the alterations were related to histological ITAC subtype, tumor stage or survival" (PMID:33500480).

### 4.2 TP53 — the one recurrent, exposure-linked alteration

TP53 (`hgnc:11998`) is the closest thing ITAC has to a defining gene, and it is the gene through which the occupational exposure acts.

- **Frequency, sinonasal cancer overall:** 77% (all histologies, n=358), with adenocarcinoma the histology most likely to be mutation-positive (OR 2.0, 95% CI 1.1–3.7 vs. SCC) (PMID:19950227).
- **Frequency, ITAC specifically:** highly variable across series — 18% in an early small genotyping study (2/11; PMID:8685214), 40–50% in most modern series, 50% (4/8) in the WGS cohort (PMID:38711096); reviews quote a range of 18–86%. The variability is largely assay-driven (IHC vs. exon 5–8 sequencing vs. full-gene sequencing).
- **Mutation spectrum tracks wood dust, not tobacco:** G→A transitions predominate (~50%, 9/18) and occur almost exclusively in nonsmokers, while G→T transversions (~27%, 5/18) are found only in smokers.
- **Historical caution:** Wu et al. 1996 reported "58% of ITAC demonstrated scattered positive p53 immunohistochemical nuclear staining, but **no mutations were identified in exon-5 through exon-8 by genotyping**" (PMID:8685214) — p53 IHC is not a reliable surrogate for TP53 mutation in this tumour.

### 4.3 Pathway-level mutation landscape (Riobello et al., 50 ITACs, 120-gene panel; PMID:34638506)

| Pathway | Combined mutation rate | Individual genes | Protein-level correlate |
|---|---|---|---|
| **DNA damage response** | 32% (16/50) | ATM 16%, BRCA1 14%, BRCA2 4% | PARP1 high expression 60% |
| **Wnt/β-catenin** | 20% (10/50) | APC 16% (all truncating), CTNNB1 6% | Nuclear β-catenin 52%; **all 10 mutated cases nuclear-positive vs 40% of non-mutated** |
| **PI3K-AKT-mTOR** | 22–24% | PIK3CA 10%, TSC2 8%, MTOR 4%, AKT1 2%, PIK3R2 2% | p-mTOR staining **88%** |
| **MAPK** | 22% (11/50) | KRAS 12% (codons 12/13), NF1 8%, BRAF 2%, MAP2K1 2% | p-ERK1/2 **76%** |
| **Receptor tyrosine kinases** | 44% (mutation and/or copy gain) | ERBB3 6%, EPHA2 6%, ERBB2/ERBB4/NTRK1 4% each, FGFR1 gain 10% | **No EGFR mutations** |
| Other | — | AR 20% (highest single gene), LRP1B 14%, NOTCH 6% | — |

Note the striking disconnect between mutation and pathway activity: p-mTOR is positive in 88% of tumours but PI3K-pathway mutations occur in only ~22%, and p-ERK1/2 in 76% versus 22% MAPK mutations. "Expression of key pathway proteins showed no correlation to mutations in these pathways, **except for nuclear β-catenin and APC/CTNNB1 mutation**." Pathway activation in ITAC is therefore mostly *not* explained by mutation — a genuinely open mechanistic question.

### 4.4 KRAS — a discordant literature worth stating explicitly

Reported KRAS frequencies span **0% → 12–16% → 43–50%** across series. Wu et al. 1996: "In contrast to colorectal adenocarcinoma, which demonstrates K-ras-2 mutation in about 50% of cases, **ITAC showed no evidence of K-ras-2 mutation**" (PMID:8685214). Modern panel sequencing gives 12% (PMID:34638506). The high figures come from small older series. Any KB entry should record the range, not a point estimate.

### 4.5 HER2/ERBB2 — a negative result that closed a therapeutic hypothesis

Maffeis et al. tested 43 ITACs by IHC **and** CISH: "83.7% (36/43) of ITAC were scored 0, 14% (6/43) 1+, and 2.3% (1/43) 2+. **No HER2 amplification was detected by CISH** … our findings seem to rule out any oncogenetic role of HER2 in ITAC pathogenesis" (PMID:31047725). This supersedes earlier positive c-erbB-2 IHC reports (e.g. PMID:9570628).

### 4.6 Chromosomal abnormalities / copy number

ITAC is **chromosomally unstable**, with a recurrent pattern. Korinth et al. applied CGH to 42 wood-dust-related sinonasal adenocarcinomas: "Copy number changes were detected in **41 tumours (97.6%)**."

- **Gains:** 12p (83%), 7q (74%), 8q (71%), 20q (71%), 11q (61%), 22 (59%), 1q (52%); high-level amplification most often at 8q (36%).
- **Losses:** 5q (81%), 18q (76%), chromosome 4 (74%), 8p (61%), 9p (60%), 6q and 17p (52% each), 3p/13q/21 (50% each).
- **Grade correlation:** "a quantitative as well as a qualitative increase of alterations from PTCC-G1 to PTCC-G2 and finally PTCC-G3 … PTCC-G3 showed significantly more gains of 7q, 8q, and 12p, and losses of 8p and 17p" (PMID:16041693). Note the 5q and 18q losses and 8q/20q gains mirror the colorectal pattern — the morphologic mimicry extends to the karyotype.

WGS adds recurrent gains in COSMIC Cancer Gene Census genes **TERT, SDHA, RAC1, ETV1, PCM1, and MYC**, plus a **tetraploidy copy-number signature enriched in ITAC (p = 0.042)** (PMID:38711096).

### 4.7 Mismatch repair / microsatellite instability

**ITAC appears to be MMR-proficient**, unlike a subset of colorectal cancer. Puccio et al. examined 32 ITACs: "no alterations regarding MMR proteins were identified" (PMID:38791973). This is a clinically consequential negative — it argues against MSI-high as a route to checkpoint-inhibitor eligibility in ITAC.

### 4.8 Non-ITAC molecular landscape — completely different

Low-grade non-intestinal-type SNAC is defined by **kinase fusions and hotspot mutations**, not by TP53/CIN. Rooper et al., 18 cases (PMID:35322195):

> "likely oncogenic molecular alterations were identified in 76% of cases, most notably including **CTNNB1 p.S33F** mutations in 2 cases, concomitant **BRAF p.V600E and AKT1 p.E17K** mutations in 2 cases, and **ETV6::NTRK3, PRKAR1A::MET, FN1::NRG1, and DNAJB1::PRKACA** fusions in 1 case each."

Genotype–phenotype correlations exist: CTNNB1-mutant cases showed intermixed squamoid morules; BRAF/AKT1 cases showed a myoepithelial population and papillary/micropapillary architecture. **ETV6::NTRK3 is directly actionable** (larotrectinib/entrectinib) — the single most important reason to genotype a low-grade non-ITAC.

### 4.9 Epigenetics

Not systematically characterised. No comprehensive methylation-profiling study of ITAC was identified in this search. **Flag as a knowledge gap.**

### 4.10 Gene symbols for annotation

`TP53` (`hgnc:11998`), `APC` (`hgnc:583`), `CTNNB1` (`hgnc:2514`), `KRAS` (`hgnc:6407`), `PIK3CA` (`hgnc:8975`), `ATM` (`hgnc:795`), `BRCA1` (`hgnc:1100`), `BRAF` (`hgnc:1097`), `NF1` (`hgnc:7765`), `CDX2` (`hgnc:1806`), `MUC2` (`hgnc:7512`), `ERBB2` (`hgnc:3430`), `ETV6` (`hgnc:3495`), `NTRK3` (`hgnc:8033`), `MYC` (`hgnc:7553`), `TERT` (`hgnc:11730`). *(HGNC numeric IDs should be re-verified against the HGNC cache before use; the symbols are the reliable part.)*

---

## 5. Environmental Information

Covered in §2. Summary for annotation:

| Factor | ECTO / ENVO suggestion | Effect | Evidence |
|---|---|---|---|
| Hardwood dust inhalation (occupational) | `ECTO:7000135` exposure to wood dust | **TRIGGERS** | RR 29.4 for adenocarcinoma (PMID:25885319) |
| Leather dust inhalation (occupational) | `ECTO:7000001` exposure to dust (no leather-dust-specific ECTO term exists — verified) | **TRIGGERS** | RR 35.3 for adenocarcinoma (PMID:25885319) |
| Formaldehyde | `ECTO:0000439` exposure to formaldehyde | Weak / confounded; not confirmed for adenocarcinoma | PMID:25885319, PMID:41303732 |
| Textile dust | `ECTO:7000001` (nearest) | Secondary occupational factor | PMID:41303732 |
| Nickel / chromium compounds | — | Associated with sinonasal cancer generally, chiefly SCC | PMID:25885319 |
| Tobacco smoking | — | **Not established** for ITAC | PMID:19950227 |

**Infectious agents: none.** Unlike sinonasal squamous cell carcinoma (HPV-associated in a subset) and nasopharyngeal carcinoma (EBV), no viral etiology is established for ITAC. No HPV-prevalence study in ITAC surfaced in this search.

**Note the absent ECTO term.** There is no `exposure to leather dust` class in ECTO — this is a real ontology gap for the second-strongest exposure in the disease, and worth a term request rather than a forced binding to generic dust exposure.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain, upstream → downstream

**Step 1 — Deposition (`ORGANISM` scale).** Inhaled hardwood/leather dust particles impact on the anterior ethmoid and middle turbinate. This is airflow physics, and it is why the ethmoid is the characteristic site: the region is the principal impaction zone for inhaled particulate in the nasal airway.
*Exposure node:* `ECTO:7000135`. *Anatomy:* `UBERON:0002453` ethmoid sinus, `UBERON:0005385` nasal cavity respiratory epithelium.

**Step 2 — Impaired mucociliary clearance and prolonged residence time (`TISSUE`).** Dust burden slows clearance, extending contact time between particulate and epithelium.

**Step 3 — Chronic inflammation and oxidative/nitrosative stress (`TISSUE`/`MOLECULAR`).** The critical mechanistic claim, and the one that distinguishes this from a classic adduct-forming carcinogen: **wood dust is not thought to be directly mutagenic.** Prolonged irritation drives inflammatory cell turnover, and the resulting reactive oxygen/nitrogen species do the mutagenesis. The WGS evidence is the strongest support: ROS-damage signatures (SBS18/SBS36) were "almost exclusively identified in ITAC subtype samples (p = 0.00055)" and mutation burden was elevated in exposed patients (p = 0.016) (PMID:38711096).
*GO:* `GO:0002544` chronic inflammatory response, `GO:0006954` inflammatory response, `GO:0006979` response to oxidative stress. *CHEBI:* `CHEBI:26523` reactive oxygen species, `CHEBI:62764` reactive nitrogen species.

**Step 4 — Reactive epithelial change: goblet cell hyperplasia (`CELLULAR`).** Palomba et al. biopsied middle-turbinate mucosa in 139 leatherworkers (10–48 years employed, median 29): squamous metaplasia in 64.7%, with mild-moderate dysplasia in 41.1%, and **goblet cell hyperplasia in 21.6%**. "Positivity for MUC-2 was detected in goblet cells of 20 of the 30 samples with goblet cell hyperplasia (66.6%), whereas **no immunostaining was observed for cytokeratin 20 and CDX-2**. Presence of goblet cell hyperplasia was significantly associated with longer occupational exposure … (p = 0.03)" (PMID:18702897). The MUC2-positive/CDX2-negative profile places this **before** full intestinal commitment.
*CL:* `CL:0000160` goblet cell, `CL:0002370` respiratory tract goblet cell.

**Step 5 — Intestinal metaplasia: the putative precursor lesion (`TISSUE`).** Franchi et al. examined mucosa adjacent to 29 ITACs: foci of intestinal metaplasia in 8 cases (27.5%), "all positive for CK20 and CDX2, while MUC2 was detected in six cases (75%)"; 75% showed dysplasia. Decisively, "**TP53 gene sequencing … revealed the same mutation in both IM and ITAC in two cases (c.832C > T and c.215G > C)**," supporting "a possible clonal relationship between areas of sinonasal IM and ITAC, indicating that IM may represent a precursor lesion of ITAC" (PMID:25431194). One case showed a mutation in the ITAC absent from the adjacent IM — i.e. the relationship is clonal but the lesions are not identical, consistent with IM as an early field with subsequent divergent progression.

**Step 6 — TP53 mutation (`MOLECULAR`).** Dose-dependent on cumulative wood-dust exposure (§2.5). G→A transition spectrum in nonsmokers.
*GO:* `GO:0072331` signal transduction by p53 class mediator (modifier: `LOSS_OF_FUNCTION`); `GO:0006974` cellular response to DNA damage stimulus.

**Step 7 — Chromosomal instability and aneuploidy (`MOLECULAR`/`CELLULAR`).** 97.6% of tumours carry copy-number change; alteration load increases monotonically with histologic grade G1→G2→G3 (PMID:16041693). Tetraploidy signature enrichment in ITAC (PMID:38711096).

**Step 8 — Heterogeneous pathway activation (`CELLULAR`).** Wnt (nuclear β-catenin 52%), MAPK (p-ERK1/2 76%), PI3K-mTOR (p-mTOR 88%), DDR defects (32%), RTK gains (44%) — largely non-mutually-exclusive and largely uncorrelated with mutation status except for Wnt.
*GO:* `GO:0016055` Wnt signaling pathway, `GO:0000165` MAPK cascade, `GO:0008283` cell population proliferation.

**Step 9 — Local invasion (`TISSUE`/`ORGANISM`), the lethal step.** Extension through the lamina papyracea into the orbit (`UBERON:0001697` orbit of skull) and through the cribriform plate (`UBERON:0004546` cribriform plate) into the anterior cranial fossa and dura (`UBERON:0002363` dura mater). "Invasion of the duramater and local recurrence are frequent and the major cause of death" (PMID:18560862).

**Step 10 — Tumour budding at the invasive front (`CELLULAR`).** Puccio et al. established this as an independent prognostic mechanism, borrowed from colorectal pathology: "Patients with high TB (>4) have an increased risk of recurrence and death compared to those with low TB, with a **median survival of 13 and 54 months**, respectively. On multivariate analysis … **TB emerged as an independent prognostic factor net of the stage of disease or type of therapy received**" (PMID:38791973).

### 6.2 Immune microenvironment

ITAC is **poorly immunogenic**, which sets the ceiling on checkpoint-inhibitor expectations. García-Marín et al., 133 ITACs: "The presence of intratumoural CD8+ TILs was low in 57% of cases and high in 8% of cases. Tumoural PD-L1 positivity was observed in 26% of cases … **The modest percentage of CD8high/PD-L1pos cases indicates that ITAC is a lowly immunogenic tumour type.** Nevertheless, a proportion of ITAC, especially the papillary and colonic subtypes, could benefit from therapy with immune checkpoint inhibitors" (PMID:32353928). Comparative figures: PD-L1 >5% tumour cells in 34% of sinonasal SCC vs 17% of ITAC; >50% in 26% of SCC vs 3% of ITAC (PMID:41303732; original data PMID:29356178).
*GO:* `GO:0002456` T cell mediated immunity. *CL:* `CL:0000625` CD8-positive, alpha-beta T cell.

### 6.3 Molecular profiling status

| Layer | Status |
|---|---|
| Genomics (WES/WGS/panel) | Well covered — PMID:33500480, PMID:34638506, PMID:38711096 |
| Transcriptomics | Sparse; no reference GEO/ArrayExpress ITAC series identified |
| Proteomics | Essentially limited to IHC panels; no shotgun proteomics identified |
| Metabolomics / lipidomics | **None identified** |
| Single-cell / spatial | **None identified** |
| CRISPR / functional genomics screens | **None identified** — no ITAC cell line in DepMap |

The genomics/everything-else asymmetry is stark and is the clearest research gap in the disease.

---

## 7. Anatomical Structures Affected

**Primary site.** Ethmoid labyrinth (`UBERON:0002453` ethmoid sinus) and adjacent superior/middle nasal cavity (`UBERON:0001707` nasal cavity). Subsite distribution for ITAC in one recent review: **ethmoid sinus 40%, nasal cavity 25%, maxillary antrum 20%** (PMID:41303732); pooling ethmoid + upper nasal cavity gives ~85%. Contrast with sporadic ITAC in Barnes' original series, where the maxillary sinus predominated (8/17 maxillary, 7/17 nasal cavity, 2/17 ethmoid) — "In contrast, ITAC in woodworkers occurs primarily in men, **originates almost exclusively in the nasal cavity or ethmoid sinus**, and has a better prognosis" (PMID:3953940). **Subsite is therefore an etiologic marker, not just a location.**

**Secondary involvement by contiguity.** Orbit via lamina papyracea (`UBERON:0001697`); anterior skull base via cribriform plate (`UBERON:0004546`); dura and frontal lobe (`UBERON:0002363` dura mater); sphenoid sinus; nasolacrimal apparatus; pterygopalatine fossa. Systems: respiratory (upper), nervous (via skull base), visual/orbital.

**Tissue level.** Sinonasal respiratory (pseudostratified ciliated columnar) epithelium (`UBERON:0005385`) and its seromucinous submucosal glands — the latter being the presumed origin of low-grade non-ITAC.

**Cell types.** `CL:0000066` epithelial cell (the malignant compartment); `CL:0000160` goblet cell / `CL:0002370` respiratory tract goblet cell (hyperplasia and metaplasia precursor); `CL:0000151` secretory cell (seromucinous glands, non-ITAC origin); `CL:0000625` CD8+ T cell and macrophages (microenvironment).

**Subcellular.** Nucleus (`GO:0005634`) — nuclear β-catenin accumulation, p53 accumulation, CDX2/SATB2 nuclear staining are all read out here. No mitochondrial, lysosomal, or ER compartment mechanism is established.

**Laterality.** Characteristically **unilateral** at presentation; a unilateral sinonasal mass in a woodworker is the classic clinical trigger for biopsy.

---

## 8. Temporal Development

- **Onset:** adult/geriatric; mean 64.7 y (ethmoid/sphenoid ITAC meta-analysis, PMID:34622832); median 64 y for sinonasal adenocarcinoma in SEER; SEER SNAC incidence peaks in 60–69-year-olds (PMID:39753118).
- **Latency:** ~40 years mean from first wood-dust exposure (range 7–70), per IARC. **This is the defining temporal fact** — it means incidence today reflects exposure conditions of the 1970s–80s, and that OEL improvements will not show up in incidence data for decades.
- **Onset pattern:** insidious; median ~6.8 months of symptoms before diagnosis (PMID:3953940).
- **Staging:** AJCC 8th edition, with the nasal-cavity/ethmoid-sinus scheme (distinct from the maxillary-sinus scheme). Most patients present T3–T4 (92.6% in Franchi's series, PMID:10534159).
- **Course:** progressive, locally destructive. Recurrence is the dominant event, not metastasis:
  - Local recurrence **32.2%** (244/757), regional **2.2%** (22/1,022), distant **10.3%** (89/861) (PMID:34622832).
  - Barnes' 213-case pooled historical figure was harsher: 53% local recurrence, 8% nodal, 13% distant, 60% dead of disease, "**Of those dying, 80% did so within 3 years of diagnosis**" (PMID:3953940).
  - Nodal metastasis <10% at presentation; distant metastasis (lung, bone) <5% at diagnosis (PMID:41303732).
- **Late recurrence is real.** Recurrences beyond five years are documented, and lifelong follow-up is recommended (PMID:41303732).
- **Remission:** treatment-induced only. Pathological complete remission after induction chemotherapy is achievable and durable in the right molecular subgroup (§12.3). No spontaneous remission.
- **Critical intervention window:** the interval between symptom onset and skull-base/dural breach. Once dura is invaded, R0 resection becomes difficult and this is the principal determinant of death.

---

## 9. Inheritance and Population

### Epidemiology

| Metric | Value | Source |
|---|---|---|
| Sinonasal malignancy, all types | 0.5–1.0 per 100,000/yr; <5% of head & neck neoplasms | PMID:35916666 |
| Sinonasal cancer, SEER 1973–2006 | 0.556 per 100,000/yr; M:F 1.8:1; adenocarcinoma = **12.6%** of histologies | PMID:22127982 |
| Sinonasal adenocarcinoma, SEER 1973–2013 | **0.44 per million** (≈0.044/100,000) | via PMID:35916666 |
| Ethmoid/sphenoid ITAC | "**less than 1 case/100,000/yr**" | PMID:34622832 |
| Sinonasal adenocarcinoma as % of sinonasal malignancy | 10–20% (review); ~27% in some international registries | PMID:41303732 |
| ITAC as % of sinonasal adenocarcinoma | Variable by country; **higher where hardwood exposure predominates**, lower (relatively more non-ITAC) where softwood predominates | PMID:38711096 |

Trend data conflict and should be reported as such: Turner & Reh found "The incidence of sinonasal cancer remained relatively stable during the study period" (1973–2006, PMID:22127982), whereas the 2000–2020 SEER analysis of 488 SNAC patients "indicated a **rising incidence**" (PMID:39753118).

**For `prevalence` slot annotation:** use `measure_type: ANNUAL_INCIDENCE`, `prevalence_class: BELOW_1_IN_1000000`, `rate_per_100000: 0.044` for sinonasal adenocarcinoma (SEER), with `population: United States (SEER, 1973–2013)`.

### Inheritance

**Not a heritable disease.** No Mendelian inheritance pattern, no penetrance/expressivity/anticipation/mosaicism/founder-effect/consanguinity/carrier-frequency concepts apply. The only germline signal is the unreplicated DDR finding in §2.2. If an `Inheritance` block is curated at all, it should be `SOMATIC`/not-applicable rather than any HPO mode-of-inheritance term.

### Demographics

- **Sex ratio:** 94.7% male in the ethmoid/sphenoid ITAC meta-analysis (M:F ≈ 18:1) — occupational, not biological. Male predominance also in SEER SNAC (58.2% male across all sinonasal adenocarcinoma, i.e. much less skewed than ITAC specifically, reflecting non-occupational cases).
- **Sporadic cases:** ~12%, "typically occur in women with worse prognosis" (PMID:41303732).
- **Ethnicity:** highest occurrence in White populations in SEER (PMID:39753118) — again likely occupational-cohort composition.
- **Geography:** ITAC clusters where furniture/leather industries concentrate — northern Italy (Brianza), France, Belgium, the Netherlands, Spain (Asturias), Germany. Countries with predominantly **softwood** exposure have both lower sinonasal adenocarcinoma incidence and a higher non-ITAC:ITAC ratio (PMID:38711096) — a natural experiment supporting hardwood specificity.

---

## 10. Diagnostics

### Histopathology — the diagnostic core

**Barnes' five morphologic patterns** (PMID:3953940): **papillary, colonic, solid, mucinous, and mixed**. Barnes' own data: "Histologically, five variants of ITAC were recognized: papillary, colonic, solid, mucinous, and mixed."

**Kleinsasser & Schroeder's alternative scheme**: papillary-tubular cylinder cell (PTCC, graded I–III), alveolar-goblet cell (AGC), signet-ring cell (SRC), transitional (TR). Both schemes are reproducible: interrater agreement 92.6% (κ = 0.89, P < .001) in Franchi's series (PMID:10534159); unanimous agreement in 73% of cases across three independent pathologists in Franquemont's (PMID:2006716).

**Both schemes are prognostic**, and the mucinous/poorly-differentiated axis is what carries the signal:

> "patients with **mucinous and poorly differentiated adenocarcinomas had a significantly shorter disease-free interval and survival rate** than patients with well and moderately differentiated adenocarcinomas (P = .02 and P < .001) … Therefore, the separation into alveolar-goblet, signet-ring, and transitional forms has no prognostic impact" (PMID:10534159).

Median survivals by Kleinsasser type: PTCC-I 9 years, PTCC-II 3 years, AGC 7 years (PMID:2006716).

**Immunohistochemistry**

| Marker | ITAC | non-ITAC | Notes |
|---|---|---|---|
| CDX2 | Positive — **80%** diffuse nuclear | **Negative (0/14)** | PMID:15175880 |
| CK20 | Positive — **84%**, "including all cases negative for CDX-2" | Negative | PMID:15175880 |
| CK7 | Positive 88% | Positive 100% | Not discriminating |
| MUC2 | Positive | Negative | |
| SATB2 | Positive in most | Negative | PMID:39924774 |
| Villin | Positive | — | |
| S100 / SOX10 / DOG1 | Negative | **86% express ≥1** in low-grade non-ITAC | Seromucinous markers; PMID:35322195 |
| Chromogranin A | Reported in up to 75% | — | PMID:41303732 |

Note "Normal sinonasal epithelia expressed cytokeratin 7, but not CDX-2 and cytokeratin 20" (PMID:15175880) — CDX2/CK20 positivity in sinonasal mucosa is by itself abnormal.

**The single most important differential is metastatic colorectal adenocarcinoma**, which is immunophenotypically indistinguishable. This must be excluded clinically/radiologically, not by IHC: "it is important for pathologists to remember the association of these tumors with occupational exposure to wood dusts and **to exclude metastases of intestinal adenocarcinomas** when confronted by these tumors in the sinonasal tract" (PMID:39924774). Other differentials: sinonasal salivary-type adenocarcinoma, low-grade non-ITAC, sinonasal undifferentiated carcinoma, IDH2-mutant sinonasal carcinoma (which can be glandular/poorly-differentiated-adenocarcinoma-like), and olfactory neuroblastoma.

### Imaging

CT (bone detail: lamina papyracea, cribriform plate, skull base erosion) plus **contrast-enhanced MRI** (soft-tissue extent, dural and orbital invasion, distinguishing tumour from obstructed secretions). MRI is essential — the tumour/retained-secretion distinction cannot be made on CT. PET-CT for staging in high-grade/advanced disease.

### Biopsy and workup

Endoscopic biopsy is the diagnostic act. Standard workup adds an **occupational history** — which is diagnostically, prognostically, and medicolegally load-bearing, since ITAC is a compensable occupational disease across the EU.

### Molecular testing

- **TP53 status / p53 functionality** is the one assay with proven treatment-selection value (§12.3). Note it must be **sequencing plus functional interpretation**, not IHC — see PMID:8685214.
- **NGS panel** is worthwhile in advanced disease for actionable alterations: "Potentially actionable somatic mutations were found in 20 of 27 cases, **8 of which being biomarkers of FDA-approved targeted therapies**" (PMID:33500480). Critically: "thorough interpretation of somatic mutations requires sequencing analysis of the corresponding germline DNA" — **paired tumour/normal is not optional in ITAC** (57% of variants were germline).
- **For non-ITAC low-grade tumours: fusion testing (RNA-based) for ETV6::NTRK3 and other kinase fusions.** Directly actionable.
- **MMR/MSI:** low yield — no MMR alterations found in 32 ITACs (PMID:38791973).
- **HER2:** low yield — no amplification in 43 ITACs (PMID:31047725).
- **Tumour budding** should be reported (>4 buds = high) as an independent prognostic variable (PMID:38791973).

### Screening

No population screening. **Targeted endoscopic surveillance of exposed workers** is the rational approach given the long latency and the identifiable precursor (goblet cell hyperplasia → intestinal metaplasia with shared TP53 mutations). The biology supports it — Franchi et al. explicitly frame it as such: "Improving the knowledge on the morphological and molecular features of IM is a key step to identify reliable biomarkers to determine the risk of sinonasal ITAC development" (PMID:25431194). But **no validated screening protocol or biomarker exists**, and this search found no completed screening trial. Programmes exist in some European occupational-health systems on a national/regional basis.

---

## 11. Outcome / Prognosis

### Survival (ethmoid/sphenoid ITAC, 1,126 pooled cases; PMID:34622832)

| Endpoint | Rate |
|---|---|
| 3-year overall survival | **72.8%** (404/555) |
| 5-year overall survival | **66.2%** (401/606) |
| 10-year overall survival | **49%** (140/286) |

Reported 5-year OS across the wider ITAC literature spans **35–80%** depending on stage and histology (PMID:32353928).

**Outcomes are improving.** "local-recurrence rate was decreasing along the years (r = −0.529, P = .043)" and "5-year overall survival rate was increasing along the years (r = 0.814, P = .011)," attributed to "a shifting trend of treating ethmoid ITACs from an external approach to endoscopic resection" (PMID:34622832). This contrasts with sinonasal cancer overall, where "No significant changes in overall relative survival were noted" over three decades (PMID:22127982) — ITAC is one of the few sinonasal histologies where the outcome curve has actually moved.

### Recurrence and mortality pattern

Local recurrence 32.2%, regional 2.2%, distant 10.3% (PMID:34622832). Death is from local/intracranial progression, not systemic disease. Historical Barnes data: 60% dead of disease, 80% of those within 3 years (PMID:3953940).

A cautionary counterpoint from a non-Western series: in 24 patients with follow-up, "Metastases occurred in 19 out of 24 patients. **Brain metastases were very common.** All patients with metastases died of their disease" (PMID:39924774) — this cohort was 73% high-grade, illustrating how grade distribution drives cohort-level outcomes.

### Prognostic factors

| Factor | Direction | Source |
|---|---|---|
| **Tumour budding >4** | Adverse; **independent of stage and therapy**; median OS 13 vs 54 months | PMID:38791973 |
| Mucinous or poorly differentiated histology | Adverse (DFS and OS) | PMID:10534159 |
| Kleinsasser PTCC grade (I→III) | Adverse with increasing grade; tracks CNA burden | PMID:2006716, PMID:16041693 |
| Age ≥70 | Adverse | PMID:39753118 |
| Male sex | Adverse (SEER SNAC multivariable) | PMID:39753118 |
| T4a/T4b stage; tumour ≥5 cm; distant metastasis | Adverse | PMID:39753118 |
| **Absence of surgery** | Adverse | PMID:39753118 |
| Positive margins (R1/R2) | Adverse | PMID:41303732 |
| **High CD8+ TILs** | Favourable OS | PMID:32353928 |
| Sporadic (non-occupational) tumours | Adverse | PMID:41303732 |
| Functional p53 | Favourable **only if induction chemotherapy given** | PMID:23369851 |
| PD-L1 expression (tumour or macrophage) | **No prognostic value** | PMID:32353928 |
| p53 IHC status | **No prognostic value** as a standalone marker | PMID:38791973 |
| Clinical stage (in one series) | No prognostic relevance — but 92.6% were T3/T4, i.e. no contrast | PMID:10534159 |
| Specific gene mutation / mutated pathway / pathway activity | **None correlated with survival** | PMID:34638506 |

### Morbidity, disability, quality of life

Function is lost to the treatment as much as to the disease: permanent anosmia after olfactory-cleft resection; orbital exenteration in orbit-invading disease; visual and lacrimal toxicity from radiotherapy to a field abutting the optic nerve and chiasm; chronic crusting, nasal dryness, and CSF-leak risk after extended endoscopic skull-base resection. Knegt's series documents the complication profile of the conservative approach: temporary periorbital swelling 40%, temporary CSF leak 8%, meningitis 1.6%, **no perioperative deaths** (PMID:11177030). **No validated PRO/QoL instrument data for ITAC were identified — a genuine gap.**

---

## 12. Treatment

### 12.1 Surgery — the backbone

The primary goal is "complete en bloc resection with negative histological margins (R0)" (PMID:41303732), by endoscopic, open (craniofacial), or combined approach depending on extent, with vascularised-flap skull-base reconstruction.

The field has shifted decisively from craniofacial resection to **endoscopic endonasal resection**, and this shift is temporally associated with the falling local-recurrence rate and rising 5-year OS documented in PMID:34622832.

*NCIT suggestions:* `NCIT:C15329` Surgical Procedure; `NCIT:C157836` Endoscopic Sinus Surgery; `NCIT:C180345` Craniofacial Resection; `NCIT:C157984` Skull Base Surgery; `NCIT:C154430` Definitive Surgical Resection. `therapeutic_modality: SURGERY`.

### 12.2 The Rotterdam / Knegt protocol — surgical debulking plus topical 5-FU

A distinctive, ethmoid-specific, organ-preserving alternative to craniofacial resection, with the longest-running outcome data in the disease. Knegt et al., 70 consecutive patients over 23 years (1976–1997), 62 eligible for primary treatment: "Surgical debulking via an extended anterior maxillary antrostomy followed by a combination of repeated topical chemotherapy (fluorouracil) and necrotomy."

> "There were no perioperative deaths … **Adjusted disease-free survival at 2, 5, and 10 years is 96%, 87%, and 74%**, respectively" (PMID:11177030).

These are among the best long-term figures reported for ethmoid adenocarcinoma. Interpret with the usual single-centre-series caveats (selection, era, adjusted-DFS endpoint), but the approach has been independently replicated as "an alternative treatment to craniofacial resection for the management of primary intestinal-type sinonasal adenocarcinoma" (PMC3195981). Typical schedule: topical 5-FU once or twice weekly for 4–6 weeks post-debulking, with interval necrotomy.

*Annotation:* `treatment_term` `NCIT:C15632` Chemotherapy; `therapeutic_agent` `CHEBI:46345` 5-fluorouracil; `therapeutic_modality: SMALL_MOLECULE`. Worth a `notes` line that the route is **topical/intracavitary**, not systemic — the distinguishing feature.

### 12.3 Induction chemotherapy and the TP53 biomarker — the disease's one precision-oncology story

This is the most striking clinical-molecular result in ITAC, and it is a genuine predictive (not merely prognostic) biomarker.

**Licitra et al., *J Clin Oncol* 2004 (PMID:15611505)** — 30 ethmoidal ITAC patients, phase II, cisplatin/5-FU/leucovorin (PFL) then surgery and radiation:

> "Twelve patients achieved a pCR; 18 patients did not (overall response rate, 40%). **In patients with wild-type (wt) TP53 or functional p53 protein, the pCRs were 83% and 80%, respectively; in patients with mutated TP53 or impaired p53 protein, pCRs were 11% and 0%, respectively (P ≤ .0001).** At a median 55-month follow-up, all pCR patients were disease-free; 44% of nonresponding patients experienced relapse (P = .0061)."

Note the subtlety in their conclusion: "PFL seems to be highly effective … in the presence of a wt or a **still-efficient p53 protein, even when encoded by a mutated TP53 gene** (eg, early-stop codon mutation), but ineffective in ITACs carrying a disabled p53 protein." **Functional status, not mutation status, is the discriminator** — a mutated-but-functional p53 still predicts response.

**Bossi et al., *Oral Oncol* 2013 (PMID:23369851)** — 100 consecutive ITAC patients, 74 evaluable for TP53:

> "Five-year OS in Group A [craniofacial resection + RT] was 42%, while in Group B [PFL induction + standard treatment] it was 70% (p = 0.041); 5-year DFS in Group A was 40%, while in Group B it was 66% (p = 0.009) … **only for Group B patients (who received preoperative chemotherapy) both OS and DFS were in favor of functional p53** (p = 0.023 and p = 0.010). **No impact of p53 functional status as a biomarker was observed in Group A.**"

That last clause is what makes p53 *predictive* rather than prognostic: it stratifies outcome only in the arm that received the drug.

*Annotation:* `NCIT:C15632` Chemotherapy; agents `CHEBI:27899` cisplatin, `CHEBI:46345` 5-fluorouracil, `CHEBI:15640` 5-formyltetrahydrofolic acid (leucovorin). No NCIT regimen term for "PLF/PFL" was located — leave `regimen_term` absent rather than force a mismatched code.

### 12.4 Radiotherapy

Adjuvant RT is standard for advanced-stage, high-grade, or margin-positive disease. Typical ITAC dose **60 Gy in 30 × 2 Gy fractions, boostable to 66 Gy**; non-ITAC is escalated to **66–70 Gy** on the basis of perceived radioresistance (PMID:41303732).

**Particle therapy** is an active area given the proximity of the optic apparatus and brainstem. Carbon-ion RT in 22 patients with locally advanced sinonasal adenocarcinoma gave **3-year local control 76.9% and locoregional control 61.3%** (PMID:25287484). Proton therapy for sinonasal cancers broadly: 5-year local control 80%, DFS 62%, cause-specific survival 64%, OS 59% (PMC8270098). The ESMO-EURACAN guideline gives RT advances "a special focus on particle therapy" (PMID:39986703).

*NCIT:* `NCIT:C15313` Radiation Therapy. `therapeutic_modality: RADIOTHERAPY`.

### 12.5 Systemic therapy for recurrent/metastatic disease

Largely extrapolated from colorectal regimens given the shared morphology and immunophenotype: **5-FU with oxaliplatin and/or irinotecan** has been reported for advanced ITAC (*Bull Cancer* 2023). Evidence level is case-series.

### 12.6 Targeted and immunotherapy — status

- **HER2-targeted therapy: ruled out.** No amplification in 43 tumours (PMID:31047725).
- **EGFR-targeted therapy: no rationale.** "No EGFR mutations" in 50 ITACs (PMID:34638506).
- **Checkpoint inhibitors: limited, subtype-restricted rationale.** ITAC is lowly immunogenic; papillary and colonic subtypes with high CD8+ TILs are the plausible candidate group (PMID:32353928).
- **PARP inhibition: an untested hypothesis with a real basis.** DDR mutations in 32% of tumours, high PARP1 expression in 60%, and HRD mutational signatures on WGS — "The presence of homologous recombination deficiency signatures implies a **novel opportunity for treatment, but further studies are needed**" (PMID:38711096). No ITAC PARP-inhibitor trial exists.
- **NTRK inhibition:** relevant to **low-grade non-ITAC** with ETV6::NTRK3, not to ITAC (PMID:35322195).
- **IDH2 inhibition:** relevant to IDH2-mutant sinonasal carcinoma, which can present as poorly differentiated sinonasal adenocarcinoma — see NCT06176989 below.

### 12.7 Active clinical trials (ClinicalTrials.gov, queried 2026-08-28)

| NCT | Title | Phase | Status | Relevance |
|---|---|---|---|---|
| **NCT06176989** | Enasidenib in IDH2-Mutated Malignant Sinonasal and Skull Base Tumors | PHASE2 | Recruiting | Explicitly includes **poorly differentiated sinonasal adenocarcinoma** with IDH2 mutation |
| NCT05925491 | Neoadjuvant Pembrolizumab Plus Chemotherapy in Locally Advanced Sinonasal Carcinoma | — | — | SNUC-focused; adjacent, not ITAC |

No ITAC-specific interventional trial was identified. This is characteristic of the disease — the SINTART 1 and SINTART 2 phase II trials (induction chemotherapy with photon/proton/carbon-ion integration in resectable and unresectable sinonasal tumours) are the main platform studies that enrol these patients, as histology-mixed sinonasal cohorts rather than ITAC trials.

### 12.8 Pharmacogenomics

No ITAC-specific pharmacogenomic data. Standard **DPYD** genotyping applies before 5-FU exposure per CPIC/EMA guidance — relevant given how central 5-FU is to both the Knegt protocol and PFL induction, though note the topical route substantially reduces systemic exposure.

### 12.9 Follow-up

"Clinical examination with endoscopy every 3-4 months (years 1-2)"; contrast-enhanced MRI/CT every 6–12 months for the first 5 years; **lifelong follow-up** because of "late recurrences … more than five years" post-treatment (PMID:41303732).

*NCIT:* `NCIT:C15747` Supportive Care for symptom management.

---

## 13. Prevention

**Primary prevention is where nearly all of the achievable benefit lies**, because the exposure is known, workplace-confined, and regulable.

- **Engineering controls:** local exhaust ventilation at source, enclosed cutting/sanding, wet methods, HEPA filtration. **Not compressed-air cleaning**, which aerosolises settled dust.
- **Exposure limits:** EU binding OEL for inhalable hardwood dust **2 mg/m³** (down from 3 mg/m³, effective 17 January 2023, under Directive 2017/2398). Germany adopted 2 mg/m³ in March 2021. The threshold is empirically supported: TP53-mutation risk was elevated above 2 mg/m³ average exposure (OR 3.6) (PMID:19950227).
- **PPE:** appropriately fit-tested respiratory protection as a secondary control.
- **Substitution:** softwood for hardwood where feasible — supported by the observation that softwood-exposure countries have lower sinonasal adenocarcinoma incidence and relatively more non-ITAC (PMID:38711096).

**Secondary prevention:** targeted endoscopic surveillance of exposed workers, with biopsy of suspicious mucosa. The precursor-lesion biology (goblet cell hyperplasia → intestinal metaplasia sharing TP53 mutations with the eventual carcinoma) makes this biologically coherent, but **no validated protocol, interval, or biomarker exists**, and none of the surveillance programmes has been evaluated in a controlled study. A key practical obstacle is the ~40-year latency: surveillance must continue long after the worker has left the industry, which few occupational-health systems handle well.

**Tertiary prevention:** margin-negative resection, appropriate adjuvant RT, and lifelong endoscopic/imaging surveillance for late local recurrence.

**Not applicable:** immunisation; genetic screening; carrier screening; PGD/prenatal testing; genetic counselling.

**Public health / medicolegal:** ITAC is a recognised compensable occupational disease across the EU. Occupational-history documentation at diagnosis is therefore part of standard care, not an optional extra. Sipilä et al. raise an interesting forward-looking application: "**Mutational signature analysis may eventually become useful for documentation of occupation-related cancer**" (PMID:38711096) — i.e. an ROS-signature-positive ITAC as molecular corroboration of an occupational-exposure claim.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens*, `NCBITaxon:9606`.
- **Naturally occurring homologue:** **Enzootic nasal adenocarcinoma (ENA)** of sheep and goats is the closest natural analogue — a nasal-gland adenocarcinoma caused by *enzootic nasal tumour virus* (ENTV-1/ENTV-2), a betaretrovirus. It is a genuinely useful comparison **because it is mechanistically different**: ENA is retrovirally driven, occurs in young animals, and has no dust-exposure component. It illustrates that nasal glandular epithelium can be transformed by more than one route, but it is **not** a model for wood-dust-associated ITAC.
- Nasal adenocarcinoma occurs sporadically in dogs and cats as part of the canine/feline nasal tumour spectrum; no occupational or wood-dust analogue exists.
- **Zoonotic potential:** none. ITAC is non-transmissible.
- **Comparative pathology and evolutionary conservation:** the interesting comparative axis is not cross-species but cross-organ — ITAC versus colorectal adenocarcinoma. They converge on morphology, immunophenotype (CDX2/CK20/MUC2/SATB2), and even karyotype (5q/18q loss, 8q/20q gain), yet diverge on the drivers: "**on the level of molecular pathologic mechanisms these tumors have their own specific features different from gastrointestinal tumors**" (Leivo, PMID:28321774), with no classical APC-initiated adenoma–carcinoma sequence and markedly lower KRAS mutation rates.
- **OMIA:** no entry corresponding to this disease.

---

## 15. Model Organisms

**This is the largest gap in the entire disease.** No established preclinical model of sinonasal ITAC was identified in this search — no widely used cell line, no PDX, no organoid, no genetically engineered mouse, and no DepMap entry.

- **Genetically engineered models:** none reported. The heterogeneous, no-single-driver genetics (§4.1) is precisely what makes a GEMM hard to design — there is no consensus initiating lesion to knock in.
- **Chemical/inhalation carcinogenesis models:** rodent nasal carcinogenesis models exist for formaldehyde (which produces **squamous cell carcinoma**, not adenocarcinoma, in rat nasal epithelium) and for other inhaled irritants. **No rodent model reproduces wood-dust-induced nasal adenocarcinoma.** This is itself a mechanistically informative negative — consistent with the ~40-year human latency and an inflammation/ROS-mediated rather than direct-genotoxic mechanism, neither of which compresses into a rodent lifespan.
- **In vitro:** work is done on primary/FFPE patient tissue rather than in cultured models; the cited molecular studies are all human tumour-tissue studies (PMID:33500480, PMID:34638506, PMID:38711096).
- **Explanted human tissue:** the closest thing to a "model" in this field is **exposed-worker nasal mucosa biopsy** — Palomba's 139 leatherworkers (PMID:18702897) and Franchi's peri-tumoural intestinal metaplasia (PMID:25431194). These are human observational studies, and they are where the precursor-lesion biology actually comes from.

**Implication for a KB entry:** an `animal_models:` or `experimental_models:` section for this disease should be **empty with an explicit `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion attached**, rather than populated with a loosely related model. Specifically: evidence for the ROS/inflammation mechanism is entirely correlative human mutational-signature data (PMID:38711096), with no experimental system in which wood dust has been shown to *cause* sinonasal intestinal metaplasia or adenocarcinoma. That is a `KNOWLEDGE_GAP` (evidence absent), not a `HUMAN_MODEL_MISMATCH` (evidence exists but translational validity uncertain).

---

## Consolidated ontology-term suggestions

All CURIEs below were verified against OLS during this research on 2026-08-28.

**Disease:** `MONDO:0002418` ethmoid sinus adenocarcinoma · `NCIT:C6237` Ethmoid Sinus Adenocarcinoma · `NCIT:C116316` Sinonasal Adenocarcinoma, Intestinal-Type · `NCIT:C160977` Sinonasal Adenocarcinoma, Non-Intestinal-Type · pattern-level: `NCIT:C160984` papillary, `NCIT:C160986` colonic, `NCIT:C160987` solid, `NCIT:C160995` mucinous

**Phenotypes (HP):** `HP:0001742` Nasal obstruction · `HP:0000421` Epistaxis · `HP:0031417` Rhinorrhea · `HP:0004409` Hyposmia · `HP:0000458` Anosmia · `HP:0000520` Proptosis · `HP:0000651` Diplopia · `HP:0009926` Epiphora · `HP:0002315` Headache · `HP:0030072` Paranasal sinus neoplasm · `HP:0000246` Sinusitis · `HP:0006824` Cranial nerve paralysis

**Anatomy (UBERON):** `UBERON:0002453` ethmoid sinus · `UBERON:0001707` nasal cavity · `UBERON:0005385` nasal cavity respiratory epithelium · `UBERON:0001825` paranasal sinus · `UBERON:0004546` cribriform plate · `UBERON:0002363` dura mater · `UBERON:0001697` orbit of skull

**Cell types (CL):** `CL:0000066` epithelial cell · `CL:0000160` goblet cell · `CL:0002370` respiratory tract goblet cell · `CL:0000151` secretory cell · `CL:0000625` CD8-positive, alpha-beta T cell

**Processes (GO):** `GO:0002544` chronic inflammatory response · `GO:0006954` inflammatory response · `GO:0006979` response to oxidative stress · `GO:0072331` signal transduction by p53 class mediator · `GO:0006974` cellular response to DNA damage stimulus · `GO:0016055` Wnt signaling pathway · `GO:0000165` MAPK cascade · `GO:0008283` cell population proliferation

**Chemicals (CHEBI):** `CHEBI:26523` reactive oxygen species · `CHEBI:62764` reactive nitrogen species · `CHEBI:46345` 5-fluorouracil · `CHEBI:27899` cisplatin · `CHEBI:15640` 5-formyltetrahydrofolic acid

**Exposures (ECTO):** `ECTO:7000135` exposure to wood dust · `ECTO:7000001` exposure to dust · `ECTO:0000439` exposure to formaldehyde · *(gap: no `exposure to leather dust` class exists)*

**Treatments (NCIT):** `NCIT:C15329` Surgical Procedure · `NCIT:C157836` Endoscopic Sinus Surgery · `NCIT:C180345` Craniofacial Resection · `NCIT:C157984` Skull Base Surgery · `NCIT:C154430` Definitive Surgical Resection · `NCIT:C15313` Radiation Therapy · `NCIT:C15632` Chemotherapy · `NCIT:C15986` Pharmacotherapy · `NCIT:C93352` Targeted Therapy · `NCIT:C15747` Supportive Care · `NCIT:C106432` Pembrolizumab

---

## Ranked evidence base

| PMID | Citation | Use |
|---|---|---|
| 25885319 | Binazzi A, et al. *BMC Cancer.* 2015;15:49. | The occupational RR figures (29.4 wood / 35.3 leather for adenocarcinoma) |
| 19950227 | Holmila R, et al. *Int J Cancer.* 2010;127(3):578-88. | TP53 mutation frequency, dose-response, mutation spectrum; n=358 |
| 34638506 | Riobello C, et al. *Cancers.* 2021;13(19):5022. | Pathway-level mutation landscape; "genetically heterogeneous without characterizing mutations" |
| 33500480 | Sánchez-Fernández P, et al. *Sci Rep.* 2021;11(1):2247. | Actionable mutations; the 57%-germline methodological finding |
| 38711096 | Sipilä LJ, et al. *Genes Environ.* 2024;46(1):12. | WGS; ROS signatures; mutation burden; HRD |
| 34622832 | Huang EI, et al. *Medicine (Baltimore).* 2021;100(40):e27341. | The 1,126-case ethmoid/sphenoid survival and recurrence meta-analysis |
| 15611505 | Licitra L, et al. *J Clin Oncol.* 2004;22(24):4901-6. | TP53 status predicts pCR to PFL |
| 23369851 | Bossi P, et al. *Oral Oncol.* 2013;49(5):413-9. | 5-y OS 70% vs 42%; p53 predictive only in the chemo arm |
| 11177030 | Knegt PP, et al. *Arch Otolaryngol Head Neck Surg.* 2001;127(2):141-6. | Debulking + topical 5-FU; DFS 96/87/74% at 2/5/10 y |
| 39986703 | Resteghini C, et al. *ESMO Open.* 2025;10(2):104121. | ESMO-EURACAN clinical practice guideline |
| 3953940 | Barnes L. *Am J Surg Pathol.* 1986;10(3):192-202. | The five morphologic patterns; original clinical description |
| 2006716 | Franquemont DW, et al. *Am J Surg Pathol.* 1991;15(4):368-75. | Kleinsasser classification validation |
| 10534159 | Franchi A, et al. *Hum Pathol.* 1999;30(10):1140-5. | Histologic typing is reproducible and prognostic |
| 15175880 | Franchi A, et al. *Virchows Arch.* 2004;445(1):63-7. | CDX2/CK7/CK20 diagnostic panel with percentages |
| 25431194 | Franchi A, et al. *Virchows Arch.* 2015;466(2):161-8. | Intestinal metaplasia as clonal precursor (shared TP53 mutations) |
| 18702897 | Palomba A, et al. *Am J Rhinol.* 2008;22(4):356-60. | Goblet cell hyperplasia in 139 leatherworkers |
| 16041693 | Korinth D, et al. *J Pathol.* 2005;207(2):207-15. | CGH copy-number landscape; grade correlation |
| 38791973 | Puccio S, et al. *Cancers.* 2024;16(10):1895. | Tumour budding as independent prognostic factor; MMR-proficient |
| 32353928 | García-Marín R, et al. *Vaccines.* 2020;8(2):202. | CD8+ TILs / PD-L1 in 133 ITACs; low immunogenicity |
| 31047725 | Maffeis V, et al. *Pathol Res Pract.* 2019;215(6):152432. | HER2 negative by IHC + CISH in 43 cases |
| 35322195 | Rooper LM, et al. *Mod Pathol.* 2022;35(9):1160-7. | Low-grade non-ITAC: fusions, CTNNB1, BRAF/AKT1 |
| 41303732 | Sciacca M, et al. *Medicina (Kaunas).* 2025;61(11):1895. | Current comprehensive review; subsite %, RT doses, staging |
| 39753118 | Yang L, et al. *Cancer Control.* 2025;32:10732748241303423. | SEER 2000-2020, 488 SNAC; prognostic nomogram |
| 22127982 | Turner JH, Reh DD. *Head Neck.* 2012;34(6):877-85. | SEER incidence 0.556/100,000; adenocarcinoma 12.6% |
| 35916666 | Thawani R, et al. *CA Cancer J Clin.* 2023;73(1):72-112. | Contemporary sinonasal management overview |
| 28321774 | Leivo I. *Head Neck Pathol.* 2017;11(3):295-300. | ITAC classification/immunophenotype review |
| 18560862 | Llorente JL, et al. *Eur Arch Otorhinolaryngol.* 2009;266(1):1-7. | The "dural invasion is the major cause of death" framing |
| 8685214 | Wu TT, et al. *Mod Pathol.* 1996;9(3):199-204. | Historical KRAS-negative / p53 IHC-vs-genotype discordance |
| 39924774 | Ud Din N, et al. *Int J Surg Pathol.* 2025;33(6):1321-33. | 48-patient series; SATB2; younger mean age; brain metastases |
| 25287484 | *(Carbon-ion RT for locally advanced sinonasal adenocarcinoma)* | 3-y LC 76.9% |

---

## Summary of gaps for KB curation

1. **No MONDO class for sinonasal ITAC** — MONDO:0002418 is a subsite proxy. NCIT:C116316 is the semantically correct concept and has no MONDO equivalent.
2. **No ECTO term for leather dust exposure** — the second-strongest exposure in the disease is unbindable.
3. **No preclinical model of any kind.** No cell line, PDX, organoid, or GEMM.
4. **No transcriptomic, proteomic, metabolomic, single-cell, or spatial data.** The disease is genomics-only.
5. **No methylation/epigenomic profiling.**
6. **No QoL / PRO instrument data.**
7. **No validated surveillance protocol** for exposed workers despite a well-characterised precursor lesion.
8. **No ITAC-specific interventional trial** currently recruiting; patients enrol via histology-mixed sinonasal platform studies.
9. **KRAS frequency is genuinely unresolved** (0–50% across series) and should be curated as a range with the discordance noted.
10. **The pathway-activation/mutation disconnect** (p-mTOR 88% vs PI3K mutations 22%; p-ERK 76% vs MAPK mutations 22%) is an open mechanistic question worth a `KNOWLEDGE_GAP` discussion.

---

## Sources

- [Occupational exposure and sinonasal cancer: a systematic review and meta-analysis (PMID:25885319)](https://pubmed.ncbi.nlm.nih.gov/25885319/)
- [Mutations in TP53 tumor suppressor gene in wood dust-related sinonasal cancer (PMID:19950227)](https://pubmed.ncbi.nlm.nih.gov/19950227/)
- [Aberrant Signaling Pathways in Sinonasal Intestinal-Type Adenocarcinoma (PMID:34638506)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8507674/)
- [Next-generation sequencing for identification of actionable gene mutations in ITAC (PMID:33500480)](https://www.nature.com/articles/s41598-020-80242-z)
- [Genome-wide somatic mutation analysis of sinonasal adenocarcinoma with and without wood dust exposure (PMID:38711096)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11071320/)
- [Decreasing recurrence and increasing survival rates in ethmoid or sphenoid ITAC: meta-analysis with 1126 cases (PMID:34622832)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8500565/)
- [ITAC and Non-ITAC Sinonasal Adenocarcinoma: Classification, Etiopathogenesis, Diagnosis and Therapy (PMID:41303732)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12654441/)
- [Epidemiological Features of Sinonasal Adenocarcinoma and Prognostic Nomogram: SEER (PMID:39753118)](https://pubmed.ncbi.nlm.nih.gov/39753118/)
- [Prediction of TP53 status for primary PFL chemotherapy in ethmoid sinus ITAC (PMID:15611505)](https://ascopubs.org/doi/10.1200/JCO.2004.05.071)
- [Tp53 status as guide for the management of ethmoid sinus ITAC (PMID:23369851)](https://pubmed.ncbi.nlm.nih.gov/23369851/)
- [Sinonasal malignancy: ESMO-EURACAN Clinical Practice Guideline (PMID:39986703)](https://www.esmoopen.com/article/S2059-7029(24)01892-1/fulltext)
- [Adenocarcinoma of the ethmoidal sinus complex: surgical debulking and topical fluorouracil (PMID:11177030)](https://pubmed.ncbi.nlm.nih.gov/11177030/)
- [Low-grade non-intestinal-type sinonasal adenocarcinoma: molecularly heterogeneous entity (PMID:35322195)](https://www.nature.com/articles/s41379-022-01068-w)
- [Intestinal-type adenocarcinoma of the nasal cavity and paranasal sinuses — Barnes (PMID:3953940)](https://pubmed.ncbi.nlm.nih.gov/3953940/)
- [The contemporary management of cancers of the sinonasal tract in adults (PMID:35916666)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9840681/)
- [Incidence and survival in patients with sinonasal cancer: SEER historical analysis (PMID:22127982)](https://onlinelibrary.wiley.com/doi/10.1002/hed.21830)
- [Intestinal-Type Adenocarcinoma: Classification, Immunophenotype, Molecular Features — Leivo (PMID:28321774)](https://pubmed.ncbi.nlm.nih.gov/28321774/)
- [Genetic and clinical aspects of wood dust related ITAC: a review (PMID:18560862)](https://link.springer.com/article/10.1007/s00405-008-0749-y)
- [Chromosomal imbalances in wood dust-related adenocarcinomas of the inner nose (PMID:16041693)](https://pubmed.ncbi.nlm.nih.gov/16041693/)
- [Intestinal metaplasia of the sinonasal mucosa adjacent to ITAC (PMID:25431194)](https://pubmed.ncbi.nlm.nih.gov/25431194/)
- [CDX-2, CK7 and CK20 in the differential diagnosis of primary sinonasal adenocarcinomas (PMID:15175880)](https://pubmed.ncbi.nlm.nih.gov/15175880/)
- [A morphologic and immunohistochemical study of nasal mucosa in leatherworkers (PMID:18702897)](https://pubmed.ncbi.nlm.nih.gov/18702897/)
- [Tumor Budding, p53, and DNA Mismatch Repair Markers in Sinonasal ITAC (PMID:38791973)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11120584/)
- [CD8+ TILs and Tumour Microenvironment Immune Types in Sinonasal ITAC (PMID:32353928)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7349388/)
- [HER2 status in sinonasal intestinal-type adenocarcinoma (PMID:31047725)](https://pubmed.ncbi.nlm.nih.gov/31047725/)
- [Intestinal Type Sinonasal Adenocarcinoma: Clinicopathological Study of 48 Patients (PMID:39924774)](https://pubmed.ncbi.nlm.nih.gov/39924774/)
- [K-ras-2 and p53 genotyping of ITAC of the nasal cavity and paranasal sinuses (PMID:8685214)](https://pubmed.ncbi.nlm.nih.gov/8685214/)
- [Clinical relevance of the histological classification of sinonasal ITAC (PMID:10534159)](https://pubmed.ncbi.nlm.nih.gov/10534159/)
- [Histologic classification of sinonasal intestinal-type adenocarcinoma (PMID:2006716)](https://pubmed.ncbi.nlm.nih.gov/2006716/)
- [Feasibility of carbon ion radiotherapy for locally advanced sinonasal adenocarcinoma (PMID:25287484)](https://pubmed.ncbi.nlm.nih.gov/25287484/)
- [Long-term Outcomes from Proton Therapy for Sinonasal Cancers](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8270098/)
- [Endoscopic Resection and Topical 5-FU as an Alternative to Craniofacial Resection for ITAC](https://ncbi.nlm.nih.gov/pmc/articles/PMC3195981)
- [Wood Dust — IARC Summary & Evaluation, Volume 62 (1995)](https://www.inchem.org/documents/iarc/vol62/wood.html)
- [Wood Dust — 15th Report on Carcinogens, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK590780/)
- [EU hardwood dust exposure limit value: 3 mg/m³ for 5 years, thereafter 2 mg/m³](https://eos-oes.eu/2017/07/12/hardwood-dust-exposure-limit-value-of-3-mg-m3-for-5-years-thereafter-a-limit-of-2-mg-m3/)
- [Protecting workers: stricter limits on cancer-causing substances — European Parliament](https://www.europarl.europa.eu/news/en/press-room/20170829IPR82604/protecting-workers-stricter-limits-on-cancer-causing-substances)
- [Pathology Outlines — Sinonasal adenocarcinoma, intestinal type](https://www.pathologyoutlines.com/topic/nasalintestinaladeno.html)
- [ClinicalTrials.gov NCT06176989 — Enasidenib in IDH2-Mutated Sinonasal and Skull Base Tumors](https://clinicaltrials.gov/study/NCT06176989)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 45 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 37 |
| Quoted claims found in source | 24 |
| Quoted claims **not** found in source | 13 |
| References weighed for topical relevance | 45 |
| On topic | 36 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:19950227` *(abstract only)*: "Risk of TP53 mutation was significantly increased in association with duration (≥24 years, OR 5.1, 95% CI, 1.5-17.1), average level (>2 mg/m³; OR 3.6, 95% CI, 1.2-10.8) and cumulative level (≥30 mg/m³ × years; OR 3.5, 95% CI, 1.2-10.7) of wood-dust exposure"
  - closest text in source: "Risk of TP53 mutation was significantly increased in association with duration (> or =24 years, OR 5.1, 95% CI, 1.5-17.1), average level (>2 mg/m(3); OR 3.6, 95% CI, 1.2-10.8) and cumulative level (> or =30 mg/m(3) x years; OR 3.5, 95% CI, 1.2-10.7) of wood-dust exposure; adjustment for formaldehyde affected the ORs only slightly"
- `PMID:8685214` *(abstract only)*: "58% of ITAC demonstrated scattered positive p53 immunohistochemical nuclear staining, but **no mutations were identified in exon-5 through exon-8 by genotyping**"
  - closest text in source: "Fifty-eight percent of ITAC demonstrated scattered positive p53 immunohistochemical nuclear staining, but no mutations were identified in exon-5 through exon-8 by genotyping"
- `PMID:31047725` *(abstract only)*: "83.7% (36/43) of ITAC were scored 0, 14% (6/43) 1+, and 2.3% (1/43) 2+. **No HER2 amplification was detected by CISH** … our findings seem to rule out any oncogenetic role of HER2 in ITAC pathogenesis"
  - closest text in source: "Contrary to previous studies, our findings seem to rule out any oncogenetic role of HER2 in ITAC pathogenesis."
- `PMID:16041693` *(abstract only)*: "a quantitative as well as a qualitative increase of alterations from PTCC-G1 to PTCC-G2 and finally PTCC-G3 … PTCC-G3 showed significantly more gains of 7q, 8q, and 12p, and losses of 8p and 17p"
  - closest text in source: "There was a quantitative as well as a qualitative increase of alterations from PTCC-G1 to PTCC-G2 and finally PTCC-G3, confirming the usefulness of histopathological grading"
- `PMID:18702897` *(abstract only)*: "Positivity for MUC-2 was detected in goblet cells of 20 of the 30 samples with goblet cell hyperplasia (66.6%), whereas **no immunostaining was observed for cytokeratin 20 and CDX-2**. Presence of goblet cell hyperplasia was significantly associated with longer occupational exposure … (p = 0.03)"
  - closest text in source: "Positivity for MUC-2 was detected in goblet cells of 20 of the 30 samples with goblet cell hyperplasia (66.6%), whereas no immunostaining was observed for cytokeratin 20 and CDX-2"
- `PMID:38791973` *(abstract only)*: "Patients with high TB (>4) have an increased risk of recurrence and death compared to those with low TB, with a **median survival of 13 and 54 months**, respectively. On multivariate analysis … **TB emerged as an independent prognostic factor net of the stage of disease or type of therapy received**"
  - closest text in source: "Patients with high TB (>4) have an increased risk of recurrence and death compared to those with low TB, with a median survival of 13 and 54 months, respectively"
- `PMID:32353928` *(abstract only)*: "The presence of intratumoural CD8+ TILs was low in 57% of cases and high in 8% of cases. Tumoural PD-L1 positivity was observed in 26% of cases … **The modest percentage of CD8high/PD-L1pos cases indicates that ITAC is a lowly immunogenic tumour type.** Nevertheless, a proportion of ITAC, especially the papillary and colonic subtypes, could benefit from therapy with immune checkpoint inhibitors"
  - closest text in source: "Nevertheless, a proportion of ITAC, especially the papillary and colonic subtypes, could benefit from therapy with immune checkpoint inhibitors."
- `PMID:41303732` *(abstract only)*: "typically occur in women with worse prognosis"
  - Text part not found as substring: 'typically occur in women with worse prognosis' (note: only abstract available for PMID:41303732, full text may contain this excerpt)
- `PMID:10534159` *(abstract only)*: "patients with **mucinous and poorly differentiated adenocarcinomas had a significantly shorter disease-free interval and survival rate** than patients with well and moderately differentiated adenocarcinomas (P = .02 and P < .001) … Therefore, the separation into alveolar-goblet, signet-ring, and transitional forms has no prognostic impact"
  - closest text in source: "Kaplan-Meier analysis of cases stratified according to WHO classification showed that patients with mucinous and poorly differentiated adenocarcinomas had a significantly shorter disease-free interval and survival rate than patients with well and moderately differentiated adenocarcinomas (P = .02 and P < .001, respectively; log-rank test)"
- `PMID:34622832` *(abstract only)*: "a shifting trend of treating ethmoid ITACs from an external approach to endoscopic resection"
  - closest text in source: "There was a shifting trend of treating ethmoid ITACs from external approach to endoscopic resection"
- `PMID:41303732` *(abstract only)*: "complete en bloc resection with negative histological margins (R0)"
  - closest text in source: "Treatment usually involves surgical resection, often followed by radiotherapy, while the role of chemotherapy remains limited"
- `PMID:11177030` *(abstract only)*: "There were no perioperative deaths … **Adjusted disease-free survival at 2, 5, and 10 years is 96%, 87%, and 74%**, respectively"
  - closest text in source: "Adjusted disease-free survival at 2, 5, and 10 years is 96%, 87%, and 74%, respectively"
- `PMC:PMC3195981` *(abstract only)*: "an alternative treatment to craniofacial resection for the management of primary intestinal-type sinonasal adenocarcinoma"
  - closest text in source: "Intestinal-type adenocarcinoma of the sinonasal tract is very rare and is responsible for less than 4% of tumours of the sinuses"
