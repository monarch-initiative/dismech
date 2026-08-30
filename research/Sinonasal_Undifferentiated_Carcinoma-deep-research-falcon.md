---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T13:53:45.563662'
end_time: '2026-08-27T13:58:57.193078'
duration_seconds: 311.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sinonasal Undifferentiated Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 4
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Sinonasal_Undifferentiated_Carcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sinonasal Undifferentiated Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Sinonasal Undifferentiated Carcinoma** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sinonasal Undifferentiated Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Sinonasal Undifferentiated Carcinoma** covering all of the
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


# Sinonasal Undifferentiated Carcinoma: Disease Characteristics Report

**Target disease:** Sinonasal undifferentiated carcinoma (SNUC)  
**Category:** Rare, high-grade epithelial malignancy of the nasal cavity and paranasal sinuses  
**Evidence scope:** Disease-level synthesis from peer-reviewed human studies and reviews, supplemented by interventional-trial records. It is not an individual-patient/EHR analysis. Because historical “SNUC” series included tumors now recognized as NUT carcinoma and SMARCB1- or SMARCA4-deficient carcinoma, older estimates require caution.

## Executive summary

SNUC is a rapidly progressive, poorly differentiated carcinoma arising in the sinonasal tract. Modern pathology treats it as a **diagnosis of exclusion**, not a generic label for every undifferentiated sinonasal tumor. Genuine SNUC commonly carries a somatic **IDH2 p.Arg172 hotspot mutation**, whereas SWI/SNF-deficient sinonasal carcinomas are separate entities. Most patients present in the fifth to sixth decade with obstruction, epistaxis, headache, or visual symptoms and already have extensive local disease. Management is multidisciplinary and generally combines platinum-based chemotherapy, radiotherapy, and selected surgery. The strongest contemporary treatment-selection evidence supports using response to induction chemotherapy to guide definitive chemoradiation versus surgery. Prospective phase II studies are now testing pembrolizumab-containing induction therapy and enasidenib for IDH2-mutant recurrent or metastatic disease. (thawani2023thecontemporarymanagement pages 12-14, NCT05925491 chunk 1, thawani2023thecontemporarymanagement pages 14-15, NCT06176989 chunk 1, mito2018immunohistochemicaldetectionand pages 1-2, agaimy2022proceedingsofthe pages 1-2)

The principal quantitative findings are summarized below.

| Domain | Best-supported finding | Quantitative data | Evidence type/source year |
|---|---|---|---|
| Definition/classification | Genuine SNUC is now treated as a diagnosis of exclusion among poorly differentiated sinonasal carcinomas and should be separated from SWI/SNF-deficient and NUT carcinomas. | No single numeric metric; classification shift emphasized in modern reviews and pathology overviews. | Review/pathology synthesis, 2022-2023 (thawani2023thecontemporarymanagement pages 14-15, agaimy2022proceedingsofthe pages 1-2) |
| Epidemiology | SNUC is extremely rare and represents a small fraction of sinonasal malignancies. | ~5% of sinonasal malignancies; annual incidence ~0.02/100,000/year; male incidence 0.03/100,000/year vs female 0.01/100,000/year; median age 50-60 years. | Review summarizing SEER and prior series, 2023 (thawani2023thecontemporarymanagement pages 12-14) |
| Presentation at diagnosis | Symptoms are nonspecific and advanced local disease is common. | Nasal obstruction 20.0%; epistaxis 17.1%; diplopia/visual symptoms 15.0%; headache 12.1%; orbital involvement 42.9%; stage IV at diagnosis 72.9%. | Review citing systematic/retrospective SNUC studies, 2023 (thawani2023thecontemporarymanagement pages 12-14) |
| Metastatic behavior | SNUC has substantial regional and distant metastatic risk. | Regional metastasis 5-16%; distant metastasis 20-30%; common sites include bone, cervical lymph nodes, lung, brain, liver. | Review of primary SNUC literature, 2023 (thawani2023thecontemporarymanagement pages 12-14) |
| Pathology/IHC | Typical phenotype supports epithelial differentiation but not specific lineage. | Commonly positive/variable: AE1/AE3, CAM5.2, CK8, CK7/8/19; typically negative: S-100, CK5/6, p40, CD45, desmin, myogenin, MelanA, HMB45. | Review plus multi-institutional pathology study, 2018-2023 (thawani2023thecontemporarymanagement pages 14-15, mito2018immunohistochemicaldetectionand pages 1-2) |
| Molecular genetics: IDH | IDH2 hotspot mutation is the strongest recurrent molecular feature of genuine SNUC. | IDH2-mutant frequency reported as 62.5% (10/16), 54.5% (6/11), and 82.4% (14/17) across cited SNUC series; multi-institutional cohort found mutant IDH1/2 IHC positive in 26/53 SNUC (49%), with NGS showing frequent IDH2 R172X and rare IDH1 R132C. | Primary molecular pathology 2018 plus review 2023 (thawani2023thecontemporarymanagement pages 14-15, mito2018immunohistochemicaldetectionand pages 1-2) |
| Molecular co-alterations in IDH2-mutant SNUC | Additional recurrent alterations occur but appear secondary to the IDH-defined subtype. | In one cited SNUC study: TP53 41.7% (5/12), CDKN2A/2B loss 33.3% (4/12), MYC amplification 33.3% (4/12), SETD2 mutation 25% (3/12). Another cohort reported TP53 55%, KIT-activating mutations 45%, PI3K-pathway mutations 36% among IDH-mutant carcinomas. | Primary molecular study 2018 and review 2023 (thawani2023thecontemporarymanagement pages 14-15, mito2018immunohistochemicaldetectionand pages 1-2) |
| Differential diagnosis | SWI/SNF-deficient sinonasal carcinomas are distinct from genuine SNUC and generally lack the characteristic IDH2 mutation. | SMARCB1 deficiency reported in 9/142 cases (6%) in one review summary; <150 SMARCB1-deficient sinonasal carcinoma cases reported overall in pathology overview; all studied SWI/SNF-deficient cases lacked oncogenic IDH2 mutations. | Pathology overview/review, 2022-2023 (thawani2023thecontemporarymanagement pages 14-15, agaimy2022proceedingsofthe pages 1-2) |
| Imaging/staging | Imaging usually shows a large invasive noncalcified mass; staging may use AJCC or modified Kadish. | MRI pattern described qualitatively; no robust SNUC-specific pooled sensitivity/specificity identified here. | Review, 2023 (thawani2023thecontemporarymanagement pages 14-15) |
| Multimodality local control | Combined-modality therapy is favored; trimodality improves locoregional control over less intensive approaches. | Locoregional control: trimodality 63.9% vs bimodality 49.2% vs surgery alone 31.3%. | Meta-analytic summary in review, 2023 (thawani2023thecontemporarymanagement pages 14-15) |
| Radiotherapy note | IMRT at adequate dose is preferred; some benefit statements derive from broader sinonasal-cancer data rather than SNUC-only cohorts. | RT dose threshold commonly cited as >=60 Gy; where survival/toxicity comparisons are mentioned, they are not always SNUC-exclusive. | Mixed evidence; review, 2021-2023; explicitly not always SNUC-specific (thawani2023thecontemporarymanagement pages 14-15) |
| Induction chemotherapy-guided management | Response to induction chemotherapy is a major prognostic and treatment-selection factor in SNUC. | Amit cohort: 95 treatment-naive patients; regimen cisplatin 60-80 mg/m2 day 1 plus etoposide 100-120 mg/m2 or docetaxel 75 mg/m2 days 1-3 every 21 days for 1-5 cycles (median 3). Review summary reports 5-year survival 66% with IC+CRT and 43% with IC+surgery+RT; progression-free survival 74% vs 55%, respectively. | Primary cohort summarized in 2023 review; outcome table in 2022 critical review (thawani2023thecontemporarymanagement pages 14-15, konig2020theroleof pages 5-6) |
| Survival | Prognosis remains poor overall despite aggressive therapy. | Median survival ~22 months reported in pathology study background; historical review table reports 5-year OS ranging from 19% (XRT only) to 66% in modern IC-guided multimodality cohorts. | Primary pathology background 2018 and review-of-studies 2022 (mito2018immunohistochemicaldetectionand pages 1-2, konig2020theroleof pages 5-6) |
| Current trial: pembrolizumab | Ongoing phase II study tests adding pembrolizumab to neoadjuvant chemotherapy in locally advanced SNUC. | NCT05925491; recruiting; phase II; planned n=28; pembrolizumab 200 mg + cisplatin 75 mg/m2 (or carboplatin AUC5) + docetaxel 75 mg/m2 every 3 weeks for 3 cycles; primary endpoint ORR. | Interventional trial registry, first posted 2023; active update 2026 (NCT05925491 chunk 1) |
| Current trial: enasidenib | Ongoing phase II study targets IDH2-mutant recurrent/metastatic or unresectable sinonasal/skull-base tumors including SNUC. | NCT06176989; recruiting; phase II; planned n=40; enasidenib 100 mg orally daily; includes documented somatic IDH2 R140/R172 mutations; SNUC-specific secondary endpoints include CBR, PFS, OS. | Interventional trial registry, first posted 2023; active update 2026 (NCT06176989 chunk 1) |
| All-sinonasal context (explicitly not SNUC-specific) | Overall sinonasal malignancies are rare as a group; this should not be mistaken for SNUC incidence. | Sinonasal malignancies overall: 0.5-1.0/100,000 incidence. | All-sinonasal review statistic, not SNUC-specific, 2023 (thawani2023thecontemporarymanagement pages 14-15) |


*Table: This table compiles the most supported, SNUC-specific findings available from the gathered sources, emphasizing quantitative epidemiology, presentation, molecular features, treatment outcomes, and active trials. It also explicitly flags when a statistic applies to all sinonasal malignancies rather than genuine SNUC.*

## 1. Disease information

### Definition and classification

SNUC is a rare, highly aggressive carcinoma of the nasal cavity or paranasal sinuses showing epithelial differentiation but no definable squamous, glandular, melanocytic, lymphoid, or neuroendocrine lineage. It was first described in 1986 in eight patients and was initially thought to arise from Schneiderian epithelium or nasal ectoderm. Contemporary classification has narrowed the diagnosis by removing molecularly defined mimics from the former “wastebasket” category. (turrizanoni2022molecularbiomarkersin pages 5-6, thawani2023thecontemporarymanagement pages 12-14, thawani2023thecontemporarymanagement pages 14-15)

A useful exact description from the 2018 molecular-pathology study is that SNUC “is considered a diagnosis of exclusion, and has historically represented a heterogeneous group of tumors.” That study showed why combined morphology, immunohistochemistry, and sequencing are now necessary. (mito2018immunohistochemicaldetectionand pages 1-2)

### Identifiers and synonyms

* **Preferred name:** sinonasal undifferentiated carcinoma.
* **Synonyms:** SNUC; undifferentiated carcinoma of the sinonasal tract; undifferentiated carcinoma of the nasal cavity and paranasal sinuses.
* **MONDO/OMIM/Orphanet:** A confidently verified disease-specific identifier was not available in the retrieved evidence; these fields should remain unresolved rather than assigning an identifier for a broader sinonasal cancer.
* **ICD-10-CM:** No histology-specific SNUC code. Coding is anatomical, usually **C30.0** (malignant neoplasm of nasal cavity) or a **C31.x** paranasal-sinus code.
* **ICD-O:** Registration requires a topography code for the involved sinonasal site plus the applicable undifferentiated-carcinoma morphology code; local registry verification is advised.
* **MeSH:** No clearly verified SNUC-specific descriptor was identified; indexing generally uses broader “Paranasal Sinus Neoplasms,” “Nasal Cavity Neoplasms,” and “Carcinoma, Undifferentiated.”

These are aggregated disease-resource mappings, whereas the clinical and molecular evidence below derives from cohorts, case series, pathology collections, and trial registries.

## 2. Etiology, risk, and protective factors

### Causal and susceptibility factors

The initiating cause is unknown. SNUC is ordinarily a **sporadic somatic cancer**, not a Mendelian syndrome. Recurrent IDH2 mutations define a large molecular subgroup but are tumor drivers/biomarkers rather than inherited susceptibility variants. No validated germline causal gene, founder mutation, carrier frequency, penetrance estimate, or familial inheritance pattern has been established. (thawani2023thecontemporarymanagement pages 14-15, mito2018immunohistochemicaldetectionand pages 1-2)

Possible environmental associations are weak and largely hypothesis-generating. Seven of eight patients in the original series had tobacco exposure; individual occupational histories included coal work and chrome plating with exposure to sulfuric/chromic acids, nickel, zinc, copper, and metallic dust. Nickel refining and softwood/furniture exposure have also been reported. These observations are too sparse and confounded to establish causality. (thawani2023thecontemporarymanagement pages 12-14)

EBV is **not established as causal**. One geographically stratified study detected EBV RNA in 7/11 Asian cases but 0/11 Western cases; a later Taiwanese series found no EBV in 36 cases, and additional studies failed to confirm an association. HPV DNA likewise is generally absent; p16 staining should not be interpreted as proof of HPV-driven disease. (thawani2023thecontemporarymanagement pages 12-14, thawani2023thecontemporarymanagement pages 14-15)

### Protective factors and gene–environment interaction

No genetic protective allele, diet, medication, vaccine, or lifestyle intervention has been shown specifically to prevent SNUC. No reproducible gene–environment interaction has been demonstrated. Avoidance of tobacco and recognized occupational carcinogens is prudent general cancer prevention, but its SNUC-specific effect size is unknown.

## 3. Phenotypes

SNUC usually has **adult, insidious onset followed by rapid progression**. Symptoms often mimic benign rhinosinusitis, delaying diagnosis. In a systematic review of 140 patients, nasal obstruction occurred in 20.0%, epistaxis in 17.1%, diplopia or other visual symptoms in 15.0%, and headache in 12.1%; orbital involvement was present in 42.9%. In another 128-patient analysis, 72.9% had stage IV disease at diagnosis. (thawani2023thecontemporarymanagement pages 12-14)

Suggested phenotype annotations include:

* Nasal obstruction — **HP:0001742, Nasal obstruction**; progressive, sometimes unilateral.
* Epistaxis — **HP:0000421**.
* Headache — **HP:0002315**.
* Diplopia — **HP:0000651**.
* Visual impairment — **HP:0000505**; may result from orbital/apical or optic-pathway invasion.
* Proptosis — **HP:0000520**, when orbital extension displaces the globe.
* Facial pain — **HP:0010828**; cranial neuropathy or facial numbness may accompany perineural/skull-base spread.
* Anosmia — **HP:0000458**, biologically plausible with superior nasal/olfactory involvement, although a reliable SNUC-specific frequency was not retrieved.
* Cervical lymphadenopathy — **HP:0025280**, reflecting regional metastasis.

Severity is commonly high and progression continuous rather than episodic. Quality of life can be impaired by nasal obstruction, bleeding, pain, disturbed vision, cranial-nerve dysfunction, disfigurement, and treatment effects on smell, vision, swallowing, speech, dentition, endocrine function, and cognition. No validated SNUC-specific EQ-5D, SF-36, or PROMIS distribution was identified; quantitative quality-of-life claims should therefore not be extrapolated from mixed sinonasal cohorts.

## 4. Genetic, molecular, and epigenetic information

### IDH-defined genuine SNUC

The best-established alteration is a **somatic IDH2 hotspot mutation at codon R172**, with reported frequencies of 10/16 (62.5%), 6/11 (54.5%), and 14/17 (82.4%) across molecular series. In a 193-tumor multi-institutional study, mutation-specific IDH1/2 immunohistochemistry was positive in 26/53 SNUCs (49%) and 0/132 histologic mimics. Sequencing found frequent IDH2 R172 substitutions—R172S/G associated with strong staining and R172T with weak or sometimes negative staining—and a rare **IDH1 p.R132C** mutation. Consequently, negative mutation-specific IHC does not exclude an IDH mutation; sequencing is required when suspicion remains. (thawani2023thecontemporarymanagement pages 14-15, mito2018immunohistochemicaldetectionand pages 1-2)

Reported co-alterations include **TP53**, **CDKN2A/CDKN2B** loss, **MYC** amplification, **SETD2**, activating **KIT**, and PI3K-pathway mutations. In one 12-case IDH2-mutant set, TP53 alterations occurred in 41.7%, CDKN2A/2B loss and MYC amplification each in 33.3%, and SETD2 mutation in 25%. A separate analysis reported TP53 in 55%, activating KIT alterations in 45%, and PI3K-pathway alterations in 36% of IDH-mutant carcinomas. These are somatic tumor findings and are not established ACMG-classified germline variants. (thawani2023thecontemporarymanagement pages 14-15, mito2018immunohistochemicaldetectionand pages 1-2)

Mechanistically, neomorphic mutant IDH2 is expected to convert α-ketoglutarate to the oncometabolite D-2-hydroxyglutarate, inhibiting α-ketoglutarate-dependent dioxygenases and producing widespread epigenetic/differentiation abnormalities. This mechanistic model is biologically well established across IDH-mutant cancers, but SNUC-specific methylome, metabolomic, and causal functional data remain limited.

Suggested annotations: **IDH2** (HGNC:5383); **IDH1** (HGNC:5382); GO:0045944 positive regulation of transcription, GO:0016491 oxidoreductase activity, GO:0007049 cell cycle, GO:0006281 DNA repair, GO:0043067 regulation of programmed cell death, and GO:0048870 cell motility.

### Critical distinction from SWI/SNF-deficient tumors

Historical reports sometimes counted loss of **SMARCB1/INI1** or **SMARCA4/BRG1** as SNUC alterations. Current expert pathology instead recognizes SMARCB1-deficient sinonasal carcinoma, SMARCB1-deficient adenocarcinoma, SMARCA4-deficient carcinoma, and SMARCA4-deficient teratocarcinosarcoma as distinct SWI/SNF-driven entities. The pathology overview states that studied SWI/SNF-deficient tumors lacked the oncogenic IDH2 mutations “characteristic of genuine SNUC.” (agaimy2022proceedingsofthe pages 1-2)

Thus, loss of nuclear INI1 or BRG1 should prompt reclassification rather than annotation as a SNUC “causal gene.” SMARCB1 maps to 22q11.2 and SMARCA4 to chromosome 19; their proteins are chromatin-remodeling tumor suppressors. In SWI/SNF-deficient tumors, biallelic deletion or inactivating mutation causes protein loss and altered transcriptional/differentiation programs. (thawani2023thecontemporarymanagement pages 14-15, agaimy2022proceedingsofthe pages 1-2)

No validated SNUC modifier genes, germline pathogenic variants, recurrent constitutional chromosomal abnormality, or population allele-frequency estimates were identified. WES/WGS, single-cell, spatial-transcriptomic, proteomic, lipidomic, and metabolomic findings remain research-grade rather than validated disease characteristics.

## 5. Environmental and infectious information

Potential non-genetic contributors are tobacco and occupational exposure to nickel, chromium/chromic acid, metallic dust, coal-related material, and wood/furniture dust, but evidence is based on very small historical series. Alcohol, diet, exercise, radiation, ambient air pollution, and specific medications have no established SNUC-specific associations. EBV and HPV are not accepted etiologic agents for genuine SNUC. (thawani2023thecontemporarymanagement pages 12-14, thawani2023thecontemporarymanagement pages 14-15)

## 6. Mechanism and pathophysiology

A defensible causal model is:

1. **Upstream event:** an acquired epithelial-cell driver, commonly IDH2 R172 mutation, arises in sinonasal mucosa.
2. **Molecular consequence:** mutant enzyme generates D-2-hydroxyglutarate, plausibly disrupting dioxygenase-dependent chromatin regulation and differentiation.
3. **Cellular consequence:** lineage maturation fails while proliferation, cell-cycle activity, DNA-repair programs, invasion, and survival pathways become dysregulated. Gene-expression comparison with sinonasal squamous carcinoma identified differences involving **CLCA2, ARID2, MAP1LC3A, SMAD4, HELLS, MAPKAPK5-AS1, and KRT16**, although direction and functional importance require further validation. (thawani2023thecontemporarymanagement pages 14-15)
4. **Tissue consequence:** sheets/nests of high-grade epithelial cells develop necrosis, marked mitotic activity, lymphovascular invasion, perineural invasion, and destructive growth through bone.
5. **Clinical consequence:** obstruction and bleeding arise locally; orbital/skull-base invasion produces visual and neurologic symptoms; lymphovascular dissemination produces cervical-node and distant metastases. (thawani2023thecontemporarymanagement pages 12-14, thawani2023thecontemporarymanagement pages 14-15)

Relevant cell ontology suggestions are **CL:0000066 epithelial cell**, **CL:0000115 endothelial cell** for vascular invasion, **CL:0000235 macrophage**, and **CL:0000084 T cell** for the tumor microenvironment. The precise tumor cell of origin is unresolved. Suggested biological-process terms include GO:0008283 cell population proliferation, GO:0007155 cell adhesion, GO:0030335 positive regulation of cell migration, GO:0001525 angiogenesis, GO:0006915 apoptotic process, and GO:0006355 regulation of DNA-templated transcription.

No reproducible SNUC-specific immune-cell atlas, immune-evasion mechanism, metabolic signature beyond the inferred IDH oncometabolite pathway, or CRISPR dependency screen was found.

## 7. Anatomical structures affected

The primary sites are the **nasal cavity** (UBERON:0001707) and **paranasal sinuses** (UBERON:0001825), particularly ethmoid, maxillary, sphenoid, and frontal sinuses. Contiguous spread may involve sinonasal mucosa, bone, orbit, cribriform plate, anterior or middle cranial fossa, dura, brain, cranial nerves, nasopharynx, clivus, palate, pterygoid structures, and facial soft tissue. AJCC T4b disease includes orbital apex, middle cranial fossa, dura, brain, non-V2 cranial nerves, nasopharynx, or clivus. (thawani2023thecontemporarymanagement pages 62-70, thawani2023thecontemporarymanagement pages 14-15)

At tissue level this is an epithelial malignancy with destructive invasion into connective tissue, bone, vessels, nerves, and sometimes neural tissue. Regional dissemination involves cervical lymph nodes; distant sites include lung, bone, brain, and liver. Disease is usually centered asymmetrically or unilaterally but can cross midline when extensive. Nuclear and cytosolic compartments are mechanistically relevant to transcription/chromatin regulation and IDH2 metabolism, respectively.

## 8. Temporal development

Presentation is generally in middle-aged or older adults, with median age approximately 50–60 years. Onset is often clinically insidious because early symptoms resemble inflammatory sinonasal disease, but biological progression is rapid. Most tumors are locally advanced at diagnosis, and the course without effective treatment is progressive rather than relapsing-remitting. (thawani2023thecontemporarymanagement pages 12-14)

Staging should use **AJCC eighth-edition site-specific TNM**. Modified Kadish staging is also reported: stage A is confined to the nasal cavity, while stage D denotes nodal or distant metastasis. Treatment-induced remission can occur, especially after platinum-based induction therapy, but local, regional, and distant relapse remain important. No credible spontaneous-remission pattern is established. The early induction-chemotherapy response interval is a critical decision window because response strongly informs the choice of definitive local therapy. (thawani2023thecontemporarymanagement pages 14-15)

## 9. Inheritance, epidemiology, and population

SNUC accounts for approximately 3–5% of sinonasal carcinomas/malignancies. SEER recorded 318 cases from 1973–2010, corresponding to an annual incidence of approximately **0.02 per 100,000**. Incidence was estimated at 0.03 per 100,000 in males and 0.01 in females, implying roughly a 3:1 incidence ratio. The median age is 50–60 years. (thawani2023thecontemporarymanagement pages 12-14, mito2018immunohistochemicaldetectionand pages 1-2)

For context, all sinonasal malignancies together occur at approximately 0.5–1.0 per 100,000; that broader statistic must not be assigned to SNUC itself. (thawani2023thecontemporarymanagement pages 14-15)

No reliable ethnic predisposition, endemic distribution, founder effect, consanguinity association, anticipation, mosaicism, carrier state, or reproductive recurrence risk is established. Because the relevant variants are usually somatic, Mendelian inheritance fields are **not applicable**.

## 10. Diagnostics

### Clinical and imaging work-up

Evaluation should include nasal endoscopy, contrast-enhanced CT for bone destruction, and contrast-enhanced MRI for orbit, skull base, dura, brain, and perineural disease. Typical imaging shows a large, noncalcified invasive mass; MRI is approximately isointense to muscle on T1, iso- to hyperintense on T2, and heterogeneously enhancing after gadolinium. Chest/body imaging or FDG-PET/CT is appropriate for nodal and distant staging. Imaging is not histologically specific. (thawani2023thecontemporarymanagement pages 14-15)

### Biopsy and pathology

Histology shows small-to-medium pleomorphic cells in ribbons, sheets, nests, trabeculae, or organoid arrangements, with scant cytoplasm, hyperchromatic nuclei, prominent nucleoli, high mitotic activity, necrosis, and possible lymphovascular/perineural invasion. Broad-spectrum epithelial markers support carcinoma: AE1/AE3, CAM5.2, CK7, CK8, and CK19 are commonly positive or variably expressed. (thawani2023thecontemporarymanagement pages 14-15, thawani2023thecontemporarymanagement pages 12-14)

A practical exclusion panel should include:

* **p40/CK5/6:** usually negative in genuine SNUC; diffuse positivity favors squamous carcinoma.
* **S100/SOX10 and melanocytic markers Melan-A/HMB45:** exclude melanoma and selected neural/multiphenotypic tumors.
* **CD45:** excludes lymphoma.
* **Desmin/myogenin:** exclude rhabdomyosarcoma.
* **Synaptophysin/chromogranin/INSM1:** evaluate neuroendocrine carcinoma; focal neuroendocrine-marker expression can occur in SNUC without neuroendocrine morphology.
* **NUT IHC:** excludes NUT carcinoma.
* **INI1/SMARCB1 and BRG1/SMARCA4:** retained expression supports genuine SNUC; loss defines separate SWI/SNF-deficient entities.
* **EBER-ISH:** excludes EBV-associated nasopharyngeal-type carcinoma/NK-T-cell processes where appropriate.
* **Mutation-specific IDH1/2 IHC followed by tumor NGS:** identifies the IDH-mutant subgroup, but sequencing is essential after negative/weak IHC because R172T and rare IDH1 variants may be missed. (thawani2023thecontemporarymanagement pages 14-15, mito2018immunohistochemicaldetectionand pages 1-2, agaimy2022proceedingsofthe pages 1-2)

### Genetic and omics testing

The clinically relevant test is **somatic tumor profiling**, preferably an NGS panel covering IDH2 R172/R140, IDH1 R132, TP53, CDKN2A/B, MYC copy number, PI3K-pathway genes, and other actionable alterations. RNA sequencing may be used if a fusion-defined differential remains possible. WES/WGS can help difficult cases but has no established advantage over focused DNA/RNA profiling in routine SNUC. Germline testing, CMA, karyotyping, mitochondrial testing, and repeat-expansion testing are not routine unless personal/family history independently suggests a hereditary syndrome.

### Differential diagnosis and screening

Major alternatives are olfactory neuroblastoma, high-grade neuroendocrine carcinoma, poorly differentiated squamous carcinoma, NUT carcinoma, SMARCB1- or SMARCA4-deficient carcinoma, lymphoma, melanoma, rhabdomyosarcoma, Ewing sarcoma, and EBV-associated carcinoma. Precise separation is mandatory because prognosis and targeted trials differ. (mito2018immunohistochemicaldetectionand pages 1-2, agaimy2022proceedingsofthe pages 1-2)

There is no population screening test, blood biomarker, liquid-biopsy standard, carrier screen, or surveillance program for asymptomatic individuals.

## 11. Outcome and prognosis

SNUC has historically had poor outcomes, with an often-cited median survival of approximately **22 months** despite multimodal therapy. Regional metastasis occurs in approximately 5–16% and distant metastasis in 20–30%. (thawani2023thecontemporarymanagement pages 12-14, mito2018immunohistochemicaldetectionand pages 1-2)

Outcomes vary substantially with stage, resectability, radiotherapy dose, treatment combination, and induction response. A review table reported historical five-year overall survival of 19% with radiotherapy alone versus 46% with surgery plus radiotherapy in one series, and 60% versus 9%, respectively, in another. In the modern induction-guided cohort, summarized five-year survival was 66% for induction chemotherapy followed by chemoradiation and 43% for induction followed by surgery and radiotherapy; corresponding progression-free estimates were 74% and 55%. These nonrandomized comparisons are subject to response-based selection and should not be interpreted as universal regimen effects. (konig2020theroleof pages 5-6)

Across a meta-analysis, locoregional control was 63.9% with trimodality therapy, 49.2% with bimodality therapy, and 31.3% with surgery alone; another meta-analysis did not find a survival advantage for three modalities over two, though combination treatment remained superior to a single modality. (thawani2023thecontemporarymanagement pages 14-15)

Adverse prognostic features include T4/skull-base or intracranial extension, nodal/distant disease, inability to deliver definitive local treatment, and poor induction-chemotherapy response. IDH-mutant tumors may have a more favorable biology in some series, but mutation-specific prognostication is not yet sufficiently standardized for treatment de-escalation.

Long-term morbidity may include visual loss, cranial neuropathy, anosmia, dysphagia, xerostomia, dental injury, endocrine dysfunction, cognitive effects, and facial/skull-base surgical morbidity. Robust SNUC-specific disability and patient-reported-outcome statistics are unavailable.

## 12. Treatment and current applications

### Standard multidisciplinary strategy

There is no randomized, universally accepted curative algorithm. Care should occur at a high-volume skull-base/head-and-neck center with expert pathology review.

1. **Induction chemotherapy:** A major contemporary approach uses a platinum doublet to measure chemosensitivity. In a 95-patient treatment-naïve cohort, cisplatin 60–80 mg/m² on day 1 was combined with etoposide 100–120 mg/m² or docetaxel 75 mg/m² on days 1–3 every 21 days for 1–5 cycles (median three). Favorable responders generally had superior outcomes and were often directed to definitive chemoradiation; poor responders with resectable disease were considered for surgery followed by adjuvant therapy. (thawani2023thecontemporarymanagement pages 14-15)
2. **Radiotherapy:** Definitive or postoperative IMRT, usually at least 60 Gy in the reviewed literature, is a central component. IMRT improves dose conformity near the optic apparatus and brain and was associated in retrospective data with better survival/recurrence outcomes and lower toxicity than older conventional techniques. Proton therapy may reduce normal-tissue dose in selected skull-base cases, but SNUC-specific comparative evidence is limited. (thawani2023thecontemporarymanagement pages 14-15)
3. **Surgery:** Endoscopic endonasal or craniofacial resection is used when complete resection is anatomically feasible and consistent with functional goals. Open craniofacial resection has increasingly been replaced by endoscopic or combined approaches in selected patients. Surgery alone is inadequate for most advanced SNUCs. (thawani2023thecontemporarymanagement pages 14-15)
4. **Systemic agents:** Cisplatin, etoposide, docetaxel, paclitaxel, and 5-fluorouracil are used in multimodal regimens. Recurrent/metastatic management is individualized because no SNUC-specific systemic standard has prospective phase III validation.

Suggested NCI Thesaurus intervention concepts include platinum-based chemotherapy, cisplatin, carboplatin, etoposide, docetaxel, paclitaxel, fluorouracil, intensity-modulated radiation therapy, proton-beam radiation therapy, endoscopic resection, craniofacial resection, pembrolizumab, and enasidenib. Exact NCIt codes should be resolved against the current NCIt release rather than inferred.

### Recent and emerging research

**NeoPeSino—NCT05925491** is a recruiting, single-arm phase II study in 28 planned patients with treatment-naïve stage III–IVB SNUC. It administers pembrolizumab 200 mg, cisplatin 75 mg/m² or carboplatin AUC5, and docetaxel 75 mg/m² every three weeks for three cycles before standard local therapy; the primary endpoint is RECIST 1.1 objective response. The hypothesis is that adding perioperative checkpoint blockade may maintain activity while reducing overall treatment burden, but no efficacy results are yet available. First posted June 29, 2023; ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT05925491. (NCT05925491 chunk 1)

**NCT06176989** is an NCI single-arm phase II trial enrolling 40 patients with recurrent/metastatic or unresectable IDH2 R140/R172-mutant sinonasal/skull-base tumors, including SNUC. Enasidenib 100 mg orally daily is given continuously; endpoints include PFS, safety, and SNUC-specific clinical benefit, PFS, and OS. This is the clearest real-world translation of the IDH2 discovery, but it remains experimental. First posted December 20, 2023; ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT06176989. (NCT06176989 chunk 1)

No approved SNUC-specific gene therapy, cell therapy, RNA therapy, CAR-T product, or pharmacogenomic dosing guideline exists. The enasidenib trial also explores UGT1A1 genotype–toxicity association, but this is not yet a validated SNUC pharmacogenomic recommendation. (NCT06176989 chunk 1)

Supportive care should include pain management, nutrition, dental care before radiation, ophthalmology and endocrinology when relevant, swallowing/speech therapy, psychosocial support, smoking cessation, and rehabilitation for visual, neurologic, or functional deficits.

## 13. Prevention

**Primary prevention:** No SNUC-specific intervention is proven. Avoid tobacco and minimize occupational exposure to nickel, chromium compounds, metallic and wood dust using engineering controls and personal protective equipment. This is precautionary rather than supported by a quantified SNUC risk reduction. No vaccine is applicable because HPV and EBV are not established causes.

**Secondary prevention:** Population screening is not recommended because incidence is approximately 0.02/100,000/year and no validated precursor lesion or screening assay exists. Persistent unilateral obstruction, recurrent epistaxis, cranial neuropathy, proptosis, or visual change warrants prompt endoscopic examination and imaging.

**Tertiary prevention:** Complete multimodal therapy, dental/visual/endocrine protection, rehabilitation, and surveillance imaging aim to reduce recurrence and treatment complications. Genetic counseling and family screening are not routinely indicated because SNUC is not established as inherited.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart specifically equivalent to molecularly confirmed human SNUC was identified. Dogs, cats, and other animals develop nasal carcinomas, but those should not be annotated as SNUC without matching histology and molecular classification. There is no evidence of zoonotic transmission or cross-species contagion. Comparative orthology of IDH2, TP53, and SWI/SNF genes is strong, but evolutionary conservation alone does not establish a natural-disease model.

## 15. Model organisms and experimental systems

The retrieved literature did not identify a standardized genetically engineered mouse, rat, zebrafish, organoid, patient-derived xenograft, or authenticated cell-line model that reproducibly recapitulates **genuine IDH2-mutant SNUC**. Most mechanistic inference comes from human tumor tissue, retrospective cohorts, immunohistochemistry, and targeted sequencing. The 2018 primary study analyzed 53 expert-confirmed SNUCs and 132 mimics, demonstrating diagnostic specificity of mutant-IDH IHC but not providing a causal animal model. (mito2018immunohistochemicaldetectionand pages 1-2)

Priority model-development needs are:

* patient-derived organoids and xenografts retaining IDH2 R172 and native epigenetic state;
* conditional IDH2 R172 knock-in in sinonasal epithelial progenitors;
* isogenic cell systems to test whether mutant IDH2 is sufficient for blocked differentiation;
* immunocompetent models for checkpoint therapy;
* functional screens for IDH, PI3K, DNA-repair, and chromatin dependencies.

Such models would permit testing enasidenib, chemotherapy resistance, radiation response, and rational immunotherapy combinations. Their key limitation will be uncertainty about the human cell of origin and the rarity/heterogeneity of source tissue.

## Evidence appraisal and key gaps

The strongest evidence consists of expert-reviewed human pathology cohorts, registry epidemiology, and retrospective multidisciplinary series. There are no randomized SNUC-specific trials, and most treatment comparisons are vulnerable to stage, resectability, institutional, and response-selection bias. Recent molecular classification also means that older cohorts may be contaminated by entities now excluded from SNUC. The most consequential knowledge gaps are validated incidence by modern molecular definition, prospective treatment outcomes, SNUC-specific patient-reported quality of life, immune and single-cell atlases, liquid-biopsy biomarkers, preventive risk estimates, and faithful experimental models.

### Principal sources and publication dates

* Thawani R, et al. **The contemporary management of cancers of the sinonasal tract in adults.** *CA Cancer J Clin.* 2023;73:72–112. Published online/issue information reported August 2023. DOI/URL: https://doi.org/10.3322/caac.21752. (thawani2023thecontemporarymanagement pages 14-15, thawani2023thecontemporarymanagement pages 12-14)
* Mito JK, et al. **Immunohistochemical Detection and Molecular Characterization of IDH-mutant Sinonasal Undifferentiated Carcinomas.** *Am J Surg Pathol.* 2018;42:1067–1075. Published August 2018. DOI/URL: https://doi.org/10.1097/PAS.0000000000001064. Exact abstract conclusion: “IDH-mutant sinonasal carcinoma may represent a distinct pathobiological entity with therapeutic implications.” (mito2018immunohistochemicaldetectionand pages 1-2)
* Agaimy A. **SWI/SNF-deficient Sinonasal Neoplasms: An Overview.** *Head Neck Pathol.* 2022;16:168–178. Published March 21, 2022. DOI/URL: https://doi.org/10.1007/s12105-022-01416-x. (agaimy2022proceedingsofthe pages 1-2)
* Turri-Zanoni M, et al. **Molecular Biomarkers in Sinonasal Cancers: New Frontiers in Diagnosis and Treatment.** *Curr Oncol Rep.* 2022;24:55–67. Published January 2022. DOI/URL: https://doi.org/10.1007/s11912-021-01154-3. (turrizanoni2022molecularbiomarkersin pages 5-6)

PMIDs were not exposed in the retrieved full-text records and therefore are not fabricated here; DOI links provide stable primary-source resolution.

References

1. (thawani2023thecontemporarymanagement pages 12-14): Rajat Thawani, Myung Sun Kim, Asad Arastu, Zizhen Feng, Malinda T. West, Nicholas F. Taflin, Kyaw Zin Thein, Ryan Li, Mathew Geltzeiler, Nancy Lee, Clifton David Fuller, Jennifer R. Grandis, Charalampos S. Floudas, Michael C. Heinrich, Ehab Hanna, and Ravi A. Chandra. The contemporary management of cancers of the sinonasal tract in adults. CA: A Cancer Journal for Clinicians, 73:72-112, Aug 2023. URL: https://doi.org/10.3322/caac.21752, doi:10.3322/caac.21752. This article has 174 citations and is from a domain leading peer-reviewed journal.

2. (NCT05925491 chunk 1):  Pembrolizumab in Locally Advanced Sinonasal Carcinoma. Istituti Clinici Scientifici Maugeri SpA. 2024. ClinicalTrials.gov Identifier: NCT05925491

3. (thawani2023thecontemporarymanagement pages 14-15): Rajat Thawani, Myung Sun Kim, Asad Arastu, Zizhen Feng, Malinda T. West, Nicholas F. Taflin, Kyaw Zin Thein, Ryan Li, Mathew Geltzeiler, Nancy Lee, Clifton David Fuller, Jennifer R. Grandis, Charalampos S. Floudas, Michael C. Heinrich, Ehab Hanna, and Ravi A. Chandra. The contemporary management of cancers of the sinonasal tract in adults. CA: A Cancer Journal for Clinicians, 73:72-112, Aug 2023. URL: https://doi.org/10.3322/caac.21752, doi:10.3322/caac.21752. This article has 174 citations and is from a domain leading peer-reviewed journal.

4. (NCT06176989 chunk 1):  Enasidenib in IDH2-Mutated Malignant Sinonasal and Skull Base Tumors. National Cancer Institute (NCI). 2024. ClinicalTrials.gov Identifier: NCT06176989

5. (mito2018immunohistochemicaldetectionand pages 1-2): Jeffrey K. Mito, Justin A. Bishop, Peter M. Sadow, Edward B. Stelow, William C. Faquin, Stacey E. Mills, Jeffrey F. Krane, Christopher A. French, Christopher D.M. Fletcher, Jason L. Hornick, Lynette M. Sholl, and Vickie Y. Jo. Immunohistochemical detection and molecular characterization of idh-mutant sinonasal undifferentiated carcinomas. The American Journal of Surgical Pathology, 42:1067–1075, Aug 2018. URL: https://doi.org/10.1097/pas.0000000000001064, doi:10.1097/pas.0000000000001064. This article has 70 citations.

6. (agaimy2022proceedingsofthe pages 1-2): Abbas Agaimy. Proceedings of the north american society of head and neck pathology, los angeles, ca, march 20, 2022: swi/snf-deficient sinonasal neoplasms: an overview. Head and Neck Pathology, 16:168-178, Mar 2022. URL: https://doi.org/10.1007/s12105-022-01416-x, doi:10.1007/s12105-022-01416-x. This article has 31 citations and is from a peer-reviewed journal.

7. (konig2020theroleof pages 5-6): Marton König, Terje Osnes, Øyvind Bruland, Kirsten Sundby Hall, Åse Bratland, and Torstein R. Meling. The role of adjuvant treatment in craniofacial malignancy: a critical review. Frontiers in Oncology, Aug 2022. URL: https://doi.org/10.3389/fonc.2020.01402, doi:10.3389/fonc.2020.01402. This article has 10 citations.

8. (turrizanoni2022molecularbiomarkersin pages 5-6): Mario Turri-Zanoni, Giacomo Gravante, and Paolo Castelnuovo. Molecular biomarkers in sinonasal cancers: new frontiers in diagnosis and treatment. Current Oncology Reports, 24:55-67, Jan 2022. URL: https://doi.org/10.1007/s11912-021-01154-3, doi:10.1007/s11912-021-01154-3. This article has 40 citations and is from a peer-reviewed journal.

9. (thawani2023thecontemporarymanagement pages 62-70): Rajat Thawani, Myung Sun Kim, Asad Arastu, Zizhen Feng, Malinda T. West, Nicholas F. Taflin, Kyaw Zin Thein, Ryan Li, Mathew Geltzeiler, Nancy Lee, Clifton David Fuller, Jennifer R. Grandis, Charalampos S. Floudas, Michael C. Heinrich, Ehab Hanna, and Ravi A. Chandra. The contemporary management of cancers of the sinonasal tract in adults. CA: A Cancer Journal for Clinicians, 73:72-112, Aug 2023. URL: https://doi.org/10.3322/caac.21752, doi:10.3322/caac.21752. This article has 174 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Sinonasal_Undifferentiated_Carcinoma-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.