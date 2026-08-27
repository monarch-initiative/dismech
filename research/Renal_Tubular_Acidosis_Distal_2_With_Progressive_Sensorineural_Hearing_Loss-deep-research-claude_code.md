---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T03:32:50.814346'
end_time: '2026-08-27T03:36:57.380547'
duration_seconds: 246.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Renal Tubular Acidosis, Distal, 2, With Progressive Sensorineural
    Hearing Loss
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 28
  total_cost_usd: 1.1944294000000002
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 20
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 10
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Renal Tubular Acidosis, Distal, 2, With Progressive Sensorineural Hearing Loss
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Renal Tubular Acidosis, Distal, 2, With Progressive Sensorineural Hearing Loss** covering all of the
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

I'll research this disorder now, gathering information from OMIM, Orphanet, PubMed, and gene databases.

# Research Report: Renal Tubular Acidosis, Distal, 2, With Progressive Sensorineural Hearing Loss

## 1. Disease Information

**Overview.** Renal Tubular Acidosis, Distal, 2, With Progressive Sensorineural Hearing Loss (dRTA2) is a rare, autosomal recessive Mendelian disorder caused by biallelic loss-of-function mutations in **ATP6V1B1** (also historically named *ATP6B1*), which encodes the B1 subunit of the apical vacuolar H⁺-ATPase (V-ATPase) proton pump. The defective proton pump impairs both (1) hydrogen-ion secretion by α-intercalated cells of the renal collecting duct, causing failure of urinary acidification despite systemic metabolic acidosis, and (2) acid–base/fluid homeostasis in the cochlea and endolymphatic sac, causing progressive, often early-onset, sensorineural hearing loss ([OMIM #267300](https://omim.org/entry/267300); Karet et al. 1999, PMID:9916796).

**Key identifiers:**
- **OMIM:** #267300 — RENAL TUBULAR ACIDOSIS, DISTAL, 2, WITH PROGRESSIVE SENSORINEURAL HEARING LOSS; DRTA2 ([omim.org/entry/267300](https://omim.org/entry/267300))
- **Gene locus (OMIM):** *ATP6V1B1* (formerly *ATP6B1*), 267300 gene map locus 2p13.3
- **MONDO:** MONDO:0009968 (confirmed via ClinGen condition page: [search.clinicalgenome.org/kb/conditions/MONDO:0009968](https://search.clinicalgenome.org/kb/conditions/MONDO:0009968))
- **Orphanet:** Grouped historically under ORPHA:93611/93609 "Autosomal recessive distal renal tubular acidosis with deafness" — note this specific entity has since been merged/folded into the broader "Autosomal recessive distal renal tubular acidosis" (ORPHA:18 family) nomenclature ([orpha.net](https://www.orpha.net/en/disease/detail/93611))
- **Related/allelic disorder:** OMIM #602722 — Distal RTA, 3, with or without SNHL (*ATP6V0A4*), the other major V-ATPase-associated recessive dRTA gene
- **Gene:** HGNC:ATP6V1B1 (hgnc:851), chromosome 2p13.3

**Synonyms:** dRTA2; RTA with progressive nerve deafness; ATP6B1-related distal RTA; ATP6V1B1-related distal renal tubular acidosis with deafness.

**Data derivation:** Nearly all available information derives from aggregated case series, multi-family cohort studies, and case reports (not large-scale EHR/registry data) — consistent with the disease's rarity (fewer than a few hundred molecularly confirmed cases reported in the literature to date).

---

## 2. Etiology

**Primary cause — genetic.** Biallelic (homozygous or compound heterozygous) loss-of-function pathogenic variants in *ATP6V1B1* are necessary and sufficient to cause the disease; it is a monogenic disorder with no known environmental or infectious primary cause.

**Genetic risk factors:**
- **Causal gene:** *ATP6V1B1* — pathogenic variants identified in ~10/26 (38%) of AR dRTA kindreds in early linkage cohorts, with *ATP6V0A4* accounting for a further share and residual genetic heterogeneity (further genes not yet linked) (Karet et al. 1999, PMID:9916796; Ren Fail 2013, PMID:23923981).
- **Consanguinity** substantially raises risk, given autosomal recessive inheritance and the prevalence of founder/recurrent alleles in specific populations (Turkish, Algerian, Moroccan, Tunisian, Saudi, Mexican cohorts all report recurrent homozygous variants in consanguineous families) (PMID:23923981; PMID:17216496; PMC12769223).
- **Population/founder variants:** recurrent mutations reported include c.91C>T (p.R31X), IVS6+1G>A (intron 6 splice), c.1181G>A (p.R394Q, in the newly described **dominant** disease mechanism — see below), c.232G>A (p.G78R), c.497delC, and c.1155dupC.
- **Novel dominant mechanism (2025):** Heterozygous variants at codon Arg394 (p.Arg394Gln, the most common; also p.Arg394Gly) act via a **dominant-negative mechanism** at the ATP-binding fold of the V1 domain, defining a distinct autosomal dominant form of ATP6V1B1-related dRTA that is clinically milder and has a **lower prevalence of hearing loss** than the classic recessive form; ~40% of these are de novo (Nephrol Dial Transplant 2025, PMID:39837581).

**Environmental/lifestyle risk factors:** None established as primary causes; this is a pure Mendelian disorder. (Acquired forms of dRTA exist — e.g., secondary to Sjögren syndrome, SLE, or drug toxicity — but these are etiologically and genetically distinct from ATP6V1B1-related dRTA2 and should not be conflated.)

**Protective factors:** None specific identified; there is no known modifier variant that reduces penetrance of biallelic loss-of-function *ATP6V1B1* alleles reported in the literature reviewed.

**Gene–environment interaction:** Not applicable/documented — this is a fully penetrant monogenic condition once biallelic pathogenic variants are present.

---

## 3. Phenotypes

### Renal/systemic phenotypes
| Phenotype | Category | Onset | Frequency | Suggested HPO |
|---|---|---|---|---|
| Failure to thrive / growth deficiency | Clinical sign | Infancy | Very frequent | HP:0001510 (Growth delay) / HP:0004325 (Decreased body weight) |
| Hyperchloremic normal-anion-gap metabolic acidosis | Laboratory abnormality | Infancy–childhood | Universal (defining feature) | HP:0001941 (Metabolic acidosis) |
| Hypokalemia | Laboratory abnormality | Variable | Frequent | HP:0002900 (Hypokalemia) |
| Inappropriately elevated urine pH (>5.3–5.5 despite systemic acidosis) | Laboratory abnormality | Present from onset | Universal | HP:0032263 (Impaired renal urine-acidification) — closest available term |
| Hypercalciuria | Laboratory abnormality | Childhood | Frequent | HP:0002150 (Hypercalciuria) |
| Hypocitraturia | Laboratory abnormality | Childhood | Frequent | HP:0002960 (not a standard code; use free text or HP:0012622 CKD-adjacent) |
| Nephrocalcinosis | Clinical/imaging sign | Childhood, progressive | Very frequent (>85–90% in cohorts) | HP:0000121 (Nephrocalcinosis) |
| Nephrolithiasis | Clinical sign | Variable | Frequent | HP:0000787 (Nephrolithiasis) |
| Rickets / osteomalacia | Skeletal sign | Childhood (rickets) / adulthood (osteomalacia) | Common, especially untreated | HP:0002748 (Rickets) |
| Progressive renal impairment (advanced/untreated disease) | Clinical sign | Later childhood–adult | Uncommon with treatment | HP:0000083 (Renal insufficiency) |
| Bilateral genu valgum | Skeletal sign | Childhood | Reported | HP:0002857 (Genu valgum) |

### Otologic phenotype
| Phenotype | Onset | Frequency | Suggested HPO |
|---|---|---|---|
| Progressive sensorineural hearing loss | **Onset in infancy/early childhood** in ATP6V1B1-related recessive disease (contrasts with later-onset in ATP6V0A4-related disease) | ~70% of ATP6V1B1-mutation patients (vs 39% for ATP6V0A4) (PMID:23923981; GeneReviews NBK547595) | HP:0000407 (Sensorineural hearing impairment) |
| Enlarged vestibular aqueduct (EVA) | Congenital/early | Reported in a subset | HP:0011387 (Enlarged vestibular aqueduct) |
| Mondini cochlear malformation | Congenital | Reported in some cases (e.g., PMC12769223) | HP:0002676 (Cochlear malformation) |
| Endolymphatic sac enlargement/hydrops | Congenital | Reported | Associated with HP:0011387 |

**Onset/severity/progression:** Metabolic/renal features typically present in infancy with failure to thrive; if untreated, nephrocalcinosis and rickets progress and chronic kidney disease can develop. Hearing loss is progressive and, in the recessive ATP6V1B1 form, frequently congenital or early-onset — distinguishing it clinically from the later-onset hearing loss seen with ATP6V0A4 mutations. One reported patient in a genotype-confirmed family had normal hearing despite the renal phenotype, indicating incomplete penetrance for the auditory component (PMID:17216496).

**Quality of life impact:** Untreated acidosis causes growth failure and bone disease impacting mobility and development; hearing loss, if uncorrected, impairs speech/language development in affected children, motivating early hearing-aid or cochlear-implant intervention and speech therapy (PMC12769223).

---

## 4. Genetic/Molecular Information

**Causal gene:** *ATP6V1B1* (HGNC gene symbol; historically ATP6B1), located at 2p13.3. Encodes the kidney/cochlea-enriched **B1 subunit of the cytoplasmic V1 domain** of the vacuolar H⁺-ATPase.

**Variant spectrum (illustrative, from cited cohorts):**
- c.91C>T (p.Arg31Ter) — nonsense, recurrent founder allele in multiple Mediterranean/Middle Eastern cohorts
- c.[IVS6+1G>A] (intron 6 splice donor) — recurrent, loss of function
- c.232G>A (p.Gly78Arg) — missense
- c.497delC (p.Thr166ArgfsTer9) — frameshift
- c.1155dupC (p.Ile386HisfsTer56) — frameshift
- c.988G>A (p.Glu330Lys, "E330K") — novel missense (PMID:17216496)
- c.1037C>G (p.Pro346Arg) — homozygous, Saudi consanguineous family (PMC12769223)
- **c.1181G>A (p.Arg394Gln) and c.1180C>G (p.Arg394Gly)** — heterozygous, **dominant-negative** mechanism defining a distinct AD subtype (19/20 and 1/20 index cases respectively in the largest cohort to date) (PMID:39837581)

**Variant classification:** Most reported alleles are pathogenic/likely pathogenic per ACMG criteria (nonsense, frameshift, canonical splice-site); the Arg394 variants are notable exceptions of uncertain historical significance now reclassified as pathogenic via a dominant-negative mechanism.

**Functional consequence:** Predominantly **loss of function** (nonsense-mediated decay, truncation, splice disruption) for the classic recessive disease; the Arg394 substitutions instead act via a **dominant-negative** mechanism, disrupting ATP binding/hydrolysis at the nucleotide-binding fold of the V1 domain without eliminating the protein (PMID:39837581).

**Allele frequency:** Population database (gnomAD) frequency data specifically for the classic recessive pathogenic alleles were not comprehensively retrievable in this search; the dominant p.Arg394Gln/Gly variants are reported as rare/absent in gnomAD in the discovery cohort, consistent with pathogenicity.

**Zygosity:** Recessive disease requires homozygous or compound heterozygous biallelic variants; the newly described dominant subtype requires only a single heterozygous Arg394 variant (often de novo, ~40% of cases).

**Modifier genes:** None specifically established in humans; in the MRL-*Atp6v1b1^vtx^* mouse model, the inner-ear phenotype is strain-dependent and **lost on a C57BL/6J background**, demonstrating strain-specific genetic modifiers of the inner ear phenotype (PMID:28934385).

**Related/allelic disease genes (differential diagnosis within hereditary dRTA):** *ATP6V0A4* (dRTA3, OMIM #602722, later-onset hearing loss ~39%), *SLC4A1* (AE1 anion exchanger; both AD and AR dRTA, ~15% of cases, less commonly with deafness), *FOXI1* (transcription factor for acid-secreting cell differentiation), *WDR72* (trafficking; also causes amelogenesis imperfecta) — together these five genes account for the great majority of hereditary dRTA (NCBI GeneReviews NBK547595).

**Epigenetic/chromosomal information:** No epigenetic mechanism reported. One case report describes a **contiguous gene deletion at 2p13.3** encompassing *ATP6V1B1* and the neighboring *VAX2* gene, producing dRTA plus retinal dysfunction from VAX2 haploinsufficiency — illustrating that large structural deletions at this locus can extend the phenotype (PMC4630852, "A role for VAX2 in correct retinal function revealed by a novel genomic deletion at 2p13.3").

---

## 5. Environmental Information

This is a monogenic Mendelian disorder; no toxin, occupational exposure, radiation, or infectious trigger is described as causal. Environmental factors are not primary drivers, though secondary/acquired dRTA (a phenotypically overlapping but etiologically distinct entity) can arise from autoimmune disease (Sjögren syndrome, SLE), drug toxicity (amphotericin B, lithium, ifosfamide), or toxin exposure — these should not be curated under this Mendelian gene-disease entry.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular defect:** Biallelic loss-of-function variants in *ATP6V1B1* → absent/non-functional B1 subunit of the V1 cytoplasmic domain of the vacuolar H⁺-ATPase.
2. **Cellular consequence — kidney:** The V-ATPase, normally trafficked to the **apical membrane of α-intercalated cells** in the cortical and medullary collecting duct, fails to secrete H⁺ into the tubular lumen. This proton pump is functionally coupled to the basolateral Cl⁻/HCO₃⁻ exchanger AE1 (encoded by *SLC4A1*) (Oxford NDT review, "Genetic causes and mechanisms of distal renal tubular acidosis").
3. **Physiological consequence — kidney:** Failure of net acid excretion → inability to lower urine pH below ~5.3 despite systemic metabolic acidosis → hyperchloremic, normal-anion-gap metabolic acidosis with hypokalemia (potassium wasting driven by aldosterone-mediated compensation).
4. **Downstream systemic consequences:** Chronic acidosis mobilizes bone buffer (causing rickets/osteomalacia and growth failure), promotes hypercalciuria and hypocitraturia (low urinary citrate, itself a stone/nephrocalcinosis inhibitor), driving **nephrocalcinosis and nephrolithiasis**, which can progress to chronic kidney disease if untreated.
5. **Cellular consequence — inner ear:** ATP6V1B1 is co-expressed in the **cochlea and endolymphatic sac epithelium**, where V-ATPase activity is required for normal endolymph pH/ion homeostasis. Loss of function disrupts this regulation, producing **endolymphatic sac/duct and cochlear duct enlargement (hydrops)**, sometimes visualized as Mondini malformation or enlarged vestibular aqueduct, culminating in **progressive sensorineural hearing loss** (Karet et al. 1999, PMID:9916796; mouse model data, PMID:28934385).

**Molecular pathway/complex:** Vacuolar H⁺-ATPase (V-ATPase) multi-subunit proton pump — V1 (cytosolic, ATP hydrolysis) and V0 (membrane, proton translocation) domains; B1 subunit specifically confers kidney/cochlea tissue-specific apical targeting and ATP-binding function.

**Molecular function (GO):** proton-transporting ATPase activity, rotational mechanism (GO:0046961); proton-transporting V-type ATPase, V1 domain (GO:0033180).

**Biological process (GO suggestions):**
- GO:0035494 — SNARE complex disassembly (unrelated—omit)
- GO:0015992 — proton transport
- GO:0006885 — regulation of pH
- GO:0072659 — protein localization to plasma membrane (apical V-ATPase trafficking)
- GO:0070295 — renal water absorption (adjacent process)
- GO:0034220 — monoatomic ion transmembrane transport

**Cell types (CL suggestions):**
- CL:1001432 — kidney collecting duct intercalated cell, or more specifically CL:1001225 — kidney collecting duct type A intercalated cell (α-intercalated cell)
- CL:0000601 — inner ear hair cell (auditory), CL:0002210 — vestibular hair cell, or cochlear/endolymphatic sac epithelial cell (no highly specific CL term found for endolymphatic sac epithelium specifically — consider free text with CL:0000066 epithelial cell as fallback)

**Biochemical abnormalities:** Defective apical H⁺-ATPase → failure of luminal acidification; secondary hypokalemia via aldosterone-driven distal Na⁺ reabsorption/K⁺ secretion; hypocitraturia from intracellular acidosis increasing citrate reabsorption in proximal tubule.

**Tissue damage mechanism:** Chronic acidosis-driven bone demineralization (buffering) and nephrocalcinosis-related tubulointerstitial injury; in the inner ear, endolymphatic hydrops/structural malformation rather than classical "damage," reflecting a developmental/homeostatic ion-transport defect.

**Omics/advanced technology data:** No single-cell, spatial transcriptomic, or large-scale multi-omics dataset specific to this Mendelian disease was identified in this search; mechanistic understanding derives chiefly from candidate-gene physiology and mouse models (see Model Organisms, below).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Kidney (collecting duct — cortical and medullary segments); inner ear (cochlea, endolymphatic sac/duct, vestibular apparatus)
- **Secondary:** Skeletal system (rickets/osteomalacia from chronic acidosis); occasionally eye (in contiguous 2p13.3 deletion cases involving *VAX2*, PMC4630852)
- **Body systems:** Renal/urinary, auditory/vestibular, skeletal, endocrine (secondary hyperparathyroidism from chronic acidosis and hypercalciuria)

**Tissue/cell level:**
- Renal collecting duct α-intercalated cells (apical H⁺-ATPase-expressing epithelium)
- Cochlear epithelium and endolymphatic sac epithelium

**Subcellular level (GO Cellular Component):**
- GO:0016324 — apical plasma membrane (site of V-ATPase mislocalization/dysfunction)
- GO:0033180 — proton-transporting V-type ATPase, V1 domain
- GO:0016471 — vacuolar proton-transporting V-type ATPase complex

**Localization (UBERON suggestions):**
- UBERON:0001293 — kidney collecting duct
- UBERON:0001982 — intercalated cell (if available) or UBERON:0004134 — collecting duct epithelium
- UBERON:0002365 — cochlear duct
- UBERON:0009663 — endolymphatic sac
- UBERON:0001846 — vestibular aqueduct region (or closest available UBERON term for the osseous/membranous vestibular aqueduct)

**Laterality:** Bilateral, symmetric involvement of both kidneys and both ears is typical.

---

## 8. Temporal Development

- **Onset:** Renal/metabolic features classically present in **infancy** (failure to thrive, vomiting, dehydration episodes); hearing loss in the ATP6V1B1-associated recessive form also frequently has **infantile/early-childhood onset**, distinguishing it from the typically later pediatric/adult-onset hearing loss of ATP6V0A4-related disease (GeneReviews NBK547595).
- **Onset pattern:** Insidious/chronic for the metabolic and skeletal manifestations; the hearing loss is explicitly **progressive**, per the disease name.
- **Progression:** Without alkali therapy, progressive nephrocalcinosis, rickets/osteomalacia, and growth failure occur; with adequate alkali replacement, renal and skeletal manifestations are largely controlled and growth normalizes, but **hearing loss progression is not halted by metabolic treatment** — it requires audiologic management independently (hearing aids, cochlear implants) (search synthesis from GeneReviews and PMC12769223).
- **Disease course:** Chronic, lifelong condition requiring continuous alkali therapy; renal function can be preserved long-term with good metabolic control, though nephrocalcinosis, once established, is generally irreversible.
- **Critical periods:** Early diagnosis and initiation of alkali therapy in infancy is critical to prevent growth failure/rickets; early identification of hearing loss (audiometry) and early hearing intervention are critical for speech/language development.

---

## 9. Inheritance and Population

**Epidemiology:** Precise prevalence for the specific ATP6V1B1-associated subtype is not separately tabulated in major epidemiologic databases. For hereditary dRTA overall, UK data estimate a prevalence of **0.46–1.60 per 10,000** (i.e., roughly 1 in 6,250–21,700), of which hereditary causes account for ~22% of cases (GeneReviews NBK547595). *ATP6V0A4* and *ATP6V1B1* together account for **approximately 70%** of hereditary dRTA cases; ~350 total cases of hereditary dRTA have been reported in the literature to date.

**Inheritance pattern:** Autosomal recessive (classic form) — biallelic pathogenic *ATP6V1B1* variants required, 25% recurrence risk for future siblings of an affected proband when both parents are carriers. A **newly recognized autosomal dominant** subtype exists for heterozygous p.Arg394Gln/Gly variants (50% transmission risk to offspring; ~40% de novo) (PMID:39837581).

**Penetrance/expressivity:** The renal phenotype is essentially fully penetrant in biallelic loss-of-function carriers; the auditory phenotype shows **incomplete penetrance** — approximately 70% of ATP6V1B1-mutation-positive patients develop hearing loss, and at least one reported sibling with confirmed biallelic variants had normal hearing (PMID:17216496; PMID:23923981).

**Consanguinity:** A major risk factor and frequently reported in case series (Turkish, Saudi, Algerian, Moroccan, Tunisian cohorts), consistent with recessive inheritance and enrichment of recurrent founder alleles in these populations.

**Founder effects:** Recurrent alleles (e.g., c.91C>T/p.R31X, IVS6+1G>A) reported repeatedly within specific consanguineous/regional populations (Turkey, North Africa) suggest founder mutations.

**Population demographics:** No strong sex predilection reported (autosomal disease). Geographic clustering of specific pathogenic alleles has been described in Turkish, Algerian, Moroccan, Tunisian, Mexican, Chinese, and Saudi cohorts, likely reflecting consanguinity/founder effects rather than true regional prevalence differences.

**Carrier frequency:** Specific gnomAD-derived carrier frequency data for ATP6V1B1 pathogenic alleles were not comprehensively retrieved in this search; given disease rarity, expected carrier frequency for common pathogenic alleles is low in outbred populations but may be substantially elevated in specific consanguineous or founder populations.

---

## 10. Diagnostics

**Laboratory tests:**
- Serum electrolytes/venous or arterial blood gas: hyperchloremic, normal-anion-gap metabolic acidosis, hypokalemia (e.g., case report: serum K+ 3.0 mmol/L, TCO₂ 11 mmol/L; PMC12769223)
- Urine pH: inappropriately elevated (>5.3–5.5, e.g., 8.5 in one reported case) despite systemic acidosis
- Urine anion gap: positive (reflecting impaired ammonium excretion)
- Urinary calcium/citrate: hypercalciuria, hypocitraturia
- Ammonium chloride loading test / furosemide-fludrocortisone test: used historically to confirm the urinary acidification defect in equivocal (incomplete) cases

**Imaging:**
- Renal ultrasound: medullary nephrocalcinosis (hyperechoic pyramids), the dominant imaging finding (present in up to ~86–90% of cohorts)
- Temporal bone/brain MRI or CT: cochlear malformation (e.g., Mondini deformity), enlarged vestibular aqueduct, enlarged endolymphatic sac (PMC12769223; PMC3433113 "Endolymphatic Sac Enlargement in a Girl with a Novel Mutation for Distal Renal Tubular Acidosis and Severe Deafness")
- Skeletal survey/DEXA for rickets/osteomalacia assessment when clinically indicated

**Audiologic testing:** Auditory brainstem response (ABR) in infants; standard audiometry in older children/adults; recommended as part of **annual surveillance** in genetically at-risk individuals (GeneReviews NBK547595).

**Genetic testing:**
- Multigene panel covering *ATP6V0A4*, *ATP6V1B1*, *SLC4A1*, *FOXI1*, *WDR72* is the recommended first-tier approach given phenotypic overlap
- Single-gene sequencing of *ATP6V1B1* appropriate when hearing loss is a prominent early feature (higher pretest probability than *ATP6V0A4*)
- Exome/genome sequencing appropriate when panel testing is non-diagnostic
- Testing should also assess for larger deletions (e.g., 2p13.3 contiguous gene deletion involving *ATP6V1B1* and *VAX2*, PMC4630852)

**Clinical/differential diagnosis:**
- Proximal RTA (Type 2) — preserved urinary acidification capacity, elevated fractional HCO₃⁻ excretion, distinguishes from dRTA
- Mixed RTA (Type 3, *CA2*-related) — combined proximal/distal defects, often with osteopetrosis and cerebral calcification
- *ATP6V0A4*-related dRTA3 — later-onset hearing loss (39% vs 70% for ATP6V1B1), otherwise similar renal phenotype
- *SLC4A1*-related dRTA — autosomal dominant (milder, adult-onset) or autosomal recessive (in Southeast Asian populations, often with hemolytic anemia — a separate OMIM entry, "dRTA 4, with hemolytic anemia")
- Acquired/secondary dRTA — autoimmune (Sjögren, SLE), drug-induced, obstructive uropathy — distinguished by later onset, absence of family history/biallelic genetic findings

**Screening:** No population newborn screening program exists specifically for this condition; family/cascade genetic testing and carrier screening are appropriate in consanguineous families or those with a known proband, per standard genetic counseling practice for autosomal recessive disease.

---

## 11. Outcome/Prognosis

**Survival/mortality:** With timely diagnosis and adequate alkali therapy, life expectancy is not thought to be significantly reduced; mortality data specific to this entity were not identified in this search, consistent with it being primarily a morbidity- (not mortality-) associated disorder when treated.

**Renal outcome:** Adequate, sustained alkali therapy from infancy largely normalizes growth and substantially reduces progression of nephrocalcinosis and skeletal disease; delayed diagnosis or poor treatment adherence is associated with progressive nephrocalcinosis, chronic kidney disease, and persistent growth failure/rickets.

**Auditory outcome:** Hearing loss is **progressive and not preventable by metabolic (alkali) treatment** — it requires independent audiologic monitoring and intervention (hearing aids, cochlear implantation) (synthesis from GeneReviews NBK547595 and PMC12769223).

**Complications:** Nephrocalcinosis/nephrolithiasis, chronic kidney disease (in undertreated/late-diagnosed cases), rickets/osteomalacia, growth failure, and (for the auditory component) speech/language delay if hearing loss is not addressed early.

**Prognostic factors:** Early diagnosis and treatment initiation is the strongest modifiable prognostic factor for renal/skeletal outcomes; genotype may influence auditory prognosis (ATP6V1B1 loss-of-function variants carry higher risk and earlier onset of hearing loss than ATP6V0A4 variants or the newly described dominant Arg394 ATP6V1B1 variants, which have lower hearing-loss prevalence) (PMID:39837581).

---

## 12. Treatment

**Pharmacotherapy — alkali replacement (mainstay of therapy):**
- Oral alkalinizing agents: potassium bicarbonate and/or potassium citrate/sodium citrate combinations (e.g., Polycitra-K), dosed to correct acidosis and hypokalemia; infants typically require higher doses (≥5 mEq/kg/day), tapering to 1–3 mEq/kg/day with age (GeneReviews NBK547595)
- **ADV7103 / Sibnayal®** — an EU-approved prolonged-release combination granule formulation of potassium citrate (1/3) and potassium bicarbonate (2/3), enabling twice-daily dosing and improved adherence/quality of life versus immediate-release formulations (PMC7701073; PMC12351860 "6-year treatment follow-up with an extended-release alkaline formulation (Sibnayal®)")

**Suggested NCIT terms:**
- NCIT:C15986 (Pharmacotherapy) — generic action for alkali therapy
- Consider `therapeutic_agent` binding to CHEBI potassium citrate/potassium bicarbonate where available

**Auditory/otologic management:**
- Hearing aids for mild-moderate loss
- Cochlear implantation for severe-profound bilateral sensorineural hearing loss (evaluated in the reported Saudi case, PMC12769223)
- NCIT term: consider NCIT:C15747 (Supportive Care) or a device-specific code for cochlear implantation (no clean NCIT clinical-action term identified in this search — verify via OAK before curating per repository convention)

**Rehabilitative/supportive care:**
- Speech and language therapy for children with hearing loss (NCIT:C159273 — Speech Therapy)
- Genetic counseling for families (NCIT:C15240 — Genetic Counseling)
- Nutritional/vitamin D and calcium management for rickets/osteomalacia where indicated

**Surgical/interventional:** Generally not indicated for the renal component unless complicated by symptomatic nephrolithiasis requiring urologic intervention; cochlear implant surgery for severe hearing loss, as above.

**Monitoring/surveillance:** Regular serum electrolytes and renal function (every 3–4 months in infants/young children, 6–12 months in older children/adults); annual renal ultrasound for nephrocalcinosis; **annual audiometry** for at-risk individuals (GeneReviews NBK547595).

**Experimental/investigational:** No gene therapy, targeted molecular therapy, or disease-modifying (non-alkali) pharmacotherapy specific to ATP6V1B1-related dRTA was identified in this search; management remains alkali-replacement plus supportive/audiologic care. No specific NCT-registered trials specific to ATP6V1B1-dRTA2 (as opposed to dRTA broadly) were identified.

**Treatment outcomes:** Alkali therapy effectively corrects acidosis/hypokalemia and, when initiated early, substantially improves growth and reduces nephrocalcinosis progression; it does **not** alter the course of the hearing loss.

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense for a monogenic disease — the principal preventive strategy is genetic counseling and, where desired by families, reproductive options (carrier testing, prenatal diagnosis, preimplantation genetic testing) in known-carrier or consanguineous families.

**Secondary prevention:** Early biochemical diagnosis (screening infants with unexplained failure to thrive/metabolic acidosis) and early audiologic screening in at-risk families/siblings of an affected proband allows earlier intervention.

**Tertiary prevention:** Sustained alkali therapy prevents/limits progression of nephrocalcinosis, rickets, and growth failure; regular audiologic surveillance enables timely hearing intervention to limit speech/language delay.

**Genetic counseling:** Standard autosomal recessive counseling (25% recurrence risk per pregnancy for carrier parents); for the newly described dominant Arg394 subtype, 50% transmission risk applies, with ~40% of cases arising de novo (PMID:39837581).

**Screening:** No dedicated population-level newborn screening program for this specific disorder; cascade testing within affected families is the practical screening approach.

---

## 14. Other Species / Natural Disease

No naturally occurring ATP6V1B1-related disease in companion animals or livestock was identified in this search (no OMIA entry surfaced). The primary cross-species data come from engineered/spontaneous laboratory mouse models (see Section 15).

---

## 15. Model Organisms

**Mouse models (NCBITaxon:10090):**

1. **Conventional Atp6v1b1 knockout mice** (Dou H, Finberg K, Cardell EL, Lifton R, Choo D. "Mice lacking the B1 subunit of H+-ATPase have normal hearing." *Hearing Research* 2003;180:76-84): These mice demonstrated a requirement for the B1 subunit for maximal urinary acidification upon acid challenge but **no spontaneous acidosis** and **normal hearing** — an important negative/discordant model illustrating incomplete phenotype recapitulation, likely due to compensation by the paralogous B2 subunit in this genetic background.

2. **MRL-Atp6v1b1^vtx/vtx^ ("vortex") spontaneous mutant mice** (PMID:28934385/PMID:28934385, *Hum Mol Genet* 2017;26(19):3722-3735, "Hearing loss without overt metabolic acidosis in ATP6V1B1 deficient MRL mice, a new genetic model for non-syndromic deafness with enlarged vestibular aqueducts"): A spontaneous *Atp6v1b1* mutation on the MRL/MpJ background causes profound hearing impairment associated with **enlarged endolymphatic sac, endolymphatic duct, utricle, saccule, and cochlear duct** (swollen membranous labyrinth from excess endolymph), modeling non-syndromic EVA-associated deafness — but again **without the overt metabolic acidosis** seen in human disease. Critically, this inner-ear phenotype is **lost when the mutation is bred onto a C57BL/6J background**, demonstrating strain-specific genetic modifiers — an important `HUMAN_MODEL_MISMATCH`-type caveat for translational fidelity curation (relationship: PARTIALLY_RECAPITULATES for hearing loss/EVA; FAILS_TO_RECAPITULATE for systemic acidosis, in both models).

3. **Atp6v0a4 knockout mouse** (PMC3427075, "Atp6v0a4 knockout mouse is a model of distal renal tubular acidosis with hearing loss, with additional extrarenal phenotype"): A model of the allelic disorder (dRTA3) rather than ATP6V1B1-dRTA2 itself, but relevant as a comparator model within the same V-ATPase pathway and useful for comparative pathway modeling.

**Model limitations:** No existing mouse model fully recapitulates the combined human phenotype of overt metabolic acidosis **plus** hearing loss simultaneously — the conventional knockout has neither acidosis nor deafness, while the MRL-vortex model has deafness/EVA but not spontaneous acidosis. This is a significant translational gap worth flagging as a `HUMAN_MODEL_MISMATCH` in curation, since B-subunit paralog compensation (B1/B2) and genetic background strongly modulate phenotype expression in mice in ways not yet fully mapped to human genotype-phenotype correlations.

**Cell-based/in vitro models:** No iPSC-derived or organoid model specific to ATP6V1B1-dRTA2 was identified in this search.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested term |
|---|---|
| Disease | MONDO:0009968 |
| Gene | hgnc:851 (ATP6V1B1) |
| Causal cell type | CL:1001225 (kidney collecting duct type A [α-]intercalated cell) |
| Biological process | GO:0015992 (proton transport); GO:0006885 (regulation of pH) |
| Molecular function | GO:0046961 (proton-transporting ATPase activity, rotational mechanism) |
| Cellular component | GO:0016471 (vacuolar proton-transporting V-type ATPase complex); GO:0016324 (apical plasma membrane) |
| Key phenotypes (HP) | HP:0000407 (Sensorineural hearing impairment); HP:0000121 (Nephrocalcinosis); HP:0002900 (Hypokalemia); HP:0001941 (Metabolic acidosis); HP:0002748 (Rickets); HP:0011387 (Enlarged vestibular aqueduct); HP:0002676 (Cochlear malformation) |
| Anatomy (UBERON) | UBERON:0001293 (kidney collecting duct); UBERON:0002365 (cochlear duct); UBERON:0009663 (endolymphatic sac) |
| Treatment (NCIT) | NCIT:C15986 (Pharmacotherapy); NCIT:C15240 (Genetic Counseling); NCIT:C159273 (Speech Therapy) |
| Inheritance (HP) | HP:0000007 (Autosomal recessive inheritance); HP:0000006 (Autosomal dominant, for the Arg394 subtype) |

---

## Sources

- [OMIM #267300 — RENAL TUBULAR ACIDOSIS, DISTAL, 2, WITH PROGRESSIVE SENSORINEURAL HEARING LOSS; DRTA2](https://omim.org/entry/267300)
- [OMIM #602722 — RENAL TUBULAR ACIDOSIS, DISTAL, 3, WITH OR WITHOUT SENSORINEURAL HEARING LOSS; DRTA3](https://omim.org/entry/602722)
- [Karet FE et al. 1999. Mutations in the gene encoding B1 subunit of H+-ATPase cause renal tubular acidosis with sensorineural deafness. PMID:9916796](https://pubmed.ncbi.nlm.nih.gov/9916796/)
- [Subasioglu Uzak A et al. 2013. ATP6V1B1 mutations in distal renal tubular acidosis and sensorineural hearing loss: clinical and genetic spectrum of five families. Ren Fail. PMID:23923981](https://pubmed.ncbi.nlm.nih.gov/23923981/)
- [Gil H et al. 2007. Distal RTA with nerve deafness: clinical spectrum and mutational analysis in five children. Pediatr Nephrol. PMID:17216496](https://pubmed.ncbi.nlm.nih.gov/17216496/)
- [Naveen PS et al. 2015. Distal renal tubular acidosis with nerve deafness secondary to ATP6B1 gene mutation. PMID:25579729](https://pubmed.ncbi.nlm.nih.gov/25579729/)
- [Distal Renal Tubular Acidosis With Sensorineural Deafness in a Saudi Female: Case Report (PMC12769223)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12769223/)
- [NCBI GeneReviews — Hereditary Distal Renal Tubular Acidosis (NBK547595)](https://www.ncbi.nlm.nih.gov/books/NBK547595/)
- [A novel, dominant disease mechanism of distal renal tubular acidosis with specific variants in ATP6V1B1. Nephrol Dial Transplant 2025. PMID:39837581](https://academic.oup.com/ndt/article/40/8/1531/7965960)
- [Genetic causes and mechanisms of distal renal tubular acidosis. Nephrol Dial Transplant.](https://academic.oup.com/ndt/article/27/10/3691/1830963)
- [Endolymphatic Sac Enlargement in a Girl with a Novel Mutation for Distal Renal Tubular Acidosis and Severe Deafness (PMC3433113)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3433113/)
- [A role for VAX2 in correct retinal function revealed by a novel genomic deletion at 2p13.3 causing distal RTA (PMC4630852)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4630852/)
- [Hearing loss without overt metabolic acidosis in ATP6V1B1 deficient MRL mice, a new genetic model for non-syndromic deafness with enlarged vestibular aqueducts. Hum Mol Genet 2017. PMID:28934385](https://pubmed.ncbi.nlm.nih.gov/28934385/)
- [Mice lacking the B1 subunit of H+-ATPase have normal hearing (Dou et al. 2003, Hearing Research)](https://www.researchgate.net/publication/10729920_Mice_lacking_the_B1_subunit_of_H-ATPase_have_normal_hearing)
- [Atp6v0a4 knockout mouse is a model of distal renal tubular acidosis with hearing loss (PMC3427075)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3427075/)
- [ClinGen condition page — renal tubular acidosis, distal, 2, with progressive sensorineural hearing loss (MONDO:0009968)](https://search.clinicalgenome.org/kb/conditions/MONDO:0009968)
- [Orphanet: Autosomal recessive distal renal tubular acidosis with deafness (ORPHA:93611)](https://www.orpha.net/en/disease/detail/93611)
- [NORD/MONDO disease page — renal tubular acidosis, distal, 2, with progressive sensorineural hearing loss](https://rarediseases.org/mondo-disease/renal-tubular-acidosis-distal-2-with-progressive-sensorineural-hearing-loss/)
- [Efficacy and safety of an innovative prolonged-release combination drug (ADV7103) in patients with distal renal tubular acidosis (PMC7701073)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7701073/)
- [6-year treatment follow-up with an extended-release alkaline formulation (Sibnayal®) in primary distal renal tubular acidosis (PMC12351860)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12351860/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.