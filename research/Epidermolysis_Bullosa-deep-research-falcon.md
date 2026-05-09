---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T15:56:57.033771'
end_time: '2026-05-08T16:11:07.201699'
duration_seconds: 850.17
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Epidermolysis Bullosa
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 51
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Epidermolysis Bullosa
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Epidermolysis Bullosa** covering all of the
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
- **Disease Name:** Epidermolysis Bullosa
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Epidermolysis Bullosa** covering all of the
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


# Epidermolysis Bullosa (EB): Disease Characteristics Research Report (Mendelian)

## Target Disease
- **Disease name:** Epidermolysis bullosa (EB)
- **Category:** Mendelian / monogenic genodermatoses
- **Ontology identifiers available in retrieved sources:**
  - OpenTargets disease: **EFO_1000690 ("epidermolysis bullosa")**; related: **MONDO_0019276 ("inherited epidermolysis bullosa")** (OpenTargets Search: Epidermolysis bullosa)
  - **MONDO IDs for specific subtypes** appear in OpenTargets output (e.g., EBS generalized intermediate MONDO_0007554; etc.) (OpenTargets Search: Epidermolysis bullosa)
- **Key external identifiers (OMIM, Orphanet, ICD-10/ICD-11, MeSH):** Not directly retrievable from the current tool outputs; should be added from OMIM/Orphanet/ICD/MeSH in a follow-on curation step.
- **Common synonyms / alternative names:** “Inherited epidermolysis bullosa”, “EB simplex (EBS)”, “Junctional EB (JEB)”, “Dystrophic EB (DEB)”, “Kindler EB / Kindler syndrome” (bardhan2020epidermolysisbullosa pages 1-2, bischof2024emerginggenetherapeutics pages 1-2).
- **Evidence source note:** The information summarized below is primarily from aggregated disease-level resources (reviews, registries, clinical trials) and includes patient-level case aggregation in systematic reviews and registry cohorts (bardhan2020epidermolysisbullosa pages 1-2, hwang2024therapiesforcutaneous pages 1-3, suru2024epidemiologicalcharacteristicsof pages 6-9).

---

## 1. Disease Information (definitions and current understanding)

### Concise disease overview
EB is an inherited, heterogeneous group of rare genetic dermatoses characterized by mucocutaneous fragility and blister formation that can be triggered by minimal mechanical trauma (bardhan2020epidermolysisbullosa pages 1-2). A widely used framing is that EB comprises >30 subtypes grouped into **four major categories**—**EB simplex, junctional EB, dystrophic EB, and Kindler EB**—defined primarily by the **plane of tissue cleavage** within the skin, reflecting the underlying molecular defect (bardhan2020epidermolysisbullosa pages 1-2).

### Key definitional quote (from abstract-style text)
- Nature Reviews Disease Primers states: **“Epidermolysis bullosa (EB) is an inherited, heterogeneous group of rare genetic dermatoses characterized by mucocutaneous fragility and blister formation, inducible by often minimal trauma.”** (Sep 2020; URL: https://doi.org/10.1038/s41572-020-0210-0) (bardhan2020epidermolysisbullosa pages 1-2)

### Classification (consensus framing)
- EB is classified into four major types based on the level of tissue separation: **EBS, JEB, DEB, Kindler EB** (bardhan2020epidermolysisbullosa pages 1-2, bischof2024emerginggenetherapeutics pages 1-2).

---

## 2. Etiology

### Disease causal factors
EB is primarily caused by **germline pathogenic variants** in genes encoding structural proteins required for epithelial integrity and epidermal–dermal adhesion. A major review notes **“pathogenetic mutations in 16 distinct genes”** implicated in EB (bardhan2020epidermolysisbullosa pages 1-2). A 2024 review similarly states **EB-causing mutations can be present in at least 16 different genes** (bischof2024emerginggenetherapeutics pages 1-2).

### Genetic risk factors (causal genes by major EB type)
Causal genes are subtype-dependent. Examples explicitly present in the retrieved evidence include:
- **EBS:** KRT5, KRT14, PLEC (with a statement that **“75% of patients with EB simplex harbour mutations”** in KRT5/KRT14) (bardhan2020epidermolysisbullosa pages 6-7)
- **JEB:** LAMA3, LAMB3, LAMC2, ITGA6/ITGB4 (integrin α6β4), COL17A1 (type XVII collagen) (bardhan2020epidermolysisbullosa pages 4-5, bischof2024emerginggenetherapeutics pages 1-2)
- **DEB:** COL7A1 (type VII collagen) (bardhan2020epidermolysisbullosa pages 10-11)
- **Kindler EB:** FERMT1 (also referred to as KIND1 in some texts) (bischof2024emerginggenetherapeutics pages 1-2, suru2024epidemiologicalcharacteristicsof pages 4-6)

OpenTargets also lists strong gene–disease associations for EB consistent with these causal genes (e.g., COL7A1, KRT5) (OpenTargets Search: Epidermolysis bullosa).

### Variant classes and functional consequences (examples from retrieved evidence)
For DEB, COL7A1 variant class influences phenotype:
- Recessive COL7A1 mutations often include **premature termination codons** causing reduced mRNA and markedly reduced/absent type VII collagen (loss-of-function) (bardhan2020epidermolysisbullosa pages 10-11).
- Non-terminating variants (example: **glycine substitutions**) can impair collagen triple helix assembly and are associated with milder disease in some cases (bardhan2020epidermolysisbullosa pages 10-11).

### Environmental risk and protective factors
EB is genetic in origin; environmental factors primarily **modify clinical severity** (e.g., mechanical trauma/friction provoking blistering) rather than cause disease onset (bardhan2020epidermolysisbullosa pages 1-2, bischof2024emerginggenetherapeutics pages 1-2). Specific protective environmental factors are not well characterized in the retrieved evidence.

### Gene–environment interactions
The defining clinical trigger is **mechanical trauma acting on genetically fragile skin**, producing blistering and chronic wounds; this is inherent to the classification by tissue cleavage plane and the “minimal trauma” definition (bardhan2020epidermolysisbullosa pages 1-2, bischof2024emerginggenetherapeutics pages 1-2).

---

## 3. Phenotypes (with HPO suggestions)

### Core mucocutaneous phenotype (all major types)
- **Blistering/erosions after minor trauma** (HPO suggestion: *Skin blistering* [HP:0008064]) (bardhan2020epidermolysisbullosa pages 1-2).
- **Mucosal fragility** (HPO: *Mucosal blistering* [HP:0000770]) (bardhan2020epidermolysisbullosa pages 1-2).
- **Pain and itch** are common burdens, particularly in severe subtypes (mellerio2023itchinrecessive pages 1-2).

### Dystrophic EB / severe RDEB phenotype cluster
Severe RDEB is characterized by chronic, painful wounds and fibrotic scarring leading to deformity and strictures, including:
- **Pseudosyndactyly / mitten deformities** (HPO: *Syndactyly* [HP:0001159] / *Cutaneous syndactyly* [HP:0010692]) (sandoval2025towardsextracellularvesicles pages 1-2).
- **Microstomia** (HPO: *Microstomia* [HP:0000212]) and **esophageal strictures** (HPO: *Esophageal stricture* [HP:0002044]) (sandoval2025towardsextracellularvesicles pages 1-2).
- **High risk of aggressive cutaneous squamous cell carcinoma (cSCC)** (HPO: *Squamous cell carcinoma* [HP:0002860]) (hwang2024therapiesforcutaneous pages 1-3).

### Itch: phenotype frequency and QoL association (human prospective registry; 2023)
A large, prospective registry study in RDEB (PEBLES; 50 participants, 243 reviews) found itch is highly prevalent and severe:
- Quote: **“Itch was frequent, present in the preceding month in 93% of reviews.”** (Aug 2023; URL: https://doi.org/10.1186/s13023-023-02817-z) (mellerio2023itchinrecessive pages 1-2).
- Subtype differences: itch frequency (“always/often”) was **87%** in severe RDEB reviews vs **42%** in intermediate RDEB reviews; RDEB-pruriginosa had particularly high itch burden (mellerio2023itchinrecessive pages 4-6).
- Medication use: **61%** of reviews reported itch medication use; at index, **oral antihistamines 28%** and **emollients 24%** (mellerio2023itchinrecessive pages 6-7).
- Correlations with disease severity and QoL scores depended on subtype: correlations were present in intermediate/inversa forms but weak in severe RDEB (mellerio2023itchinrecessive pages 1-2, mellerio2023itchinrecessive pages 6-7).

### Quality-of-life impact (recent quantitative data; 2024)
A Spanish societal-burden study (2024; reference year 2022) reports large HRQoL impairment measured by EQ-5D:
- Mean EQ-5D utility index: **0.45 for severe EB** vs **0.62 for non-severe EB** (proxy/self reporting differences described) (arandareneo2024economicburdenand pages 1-2, arandareneo2024economicburdenand pages 6-7).

---

## 4. Genetic / Molecular Information

### Causal genes (core set in retrieved evidence)
EB is genetically heterogeneous; causal genes explicitly supported in the retrieved evidence include:
- **EBS:** KRT5, KRT14, PLEC (bischof2024emerginggenetherapeutics pages 1-2, bardhan2020epidermolysisbullosa pages 6-7)
- **JEB:** LAMA3, LAMB3, LAMC2, ITGA6/ITGB4, COL17A1 (bardhan2020epidermolysisbullosa pages 4-5, bischof2024emerginggenetherapeutics pages 1-2)
- **DEB:** COL7A1 (bardhan2020epidermolysisbullosa pages 10-11)
- **Kindler EB:** FERMT1 (suru2024epidemiologicalcharacteristicsof pages 4-6)

### Inheritance patterns
A Romanian population-based study (2012–2024) reported inheritance patterns among its cohort (not all specified): autosomal recessive (58), autosomal dominant (29), de novo (3), unspecified (62) (suru2024epidemiologicalcharacteristicsof pages 4-6). Dystrophic EB may be autosomal dominant, autosomal recessive, or de novo (bardhan2020epidermolysisbullosa pages 10-11).

### Functional biology summary (protein dysfunction)
EB phenotypes reflect failure of key structural proteins in keratinocyte cytoskeleton (EBS), hemidesmosomes/basement membrane zone (JEB), or anchoring fibrils (DEB). For example, dystrophic EB is “characterized by cleavage in the upper dermis” and “arising in all cases from COL7A1 mutations” with disrupted type VII collagen anchoring fibrils (bardhan2020epidermolysisbullosa pages 10-11).

### Modifier genes, epigenetics, chromosomal abnormalities
Not specifically described in the retrieved evidence; additional targeted searches (ClinGen/ClinVar/GWAS/epigenomic datasets) would be required for robust modifier and epigenetic annotation.

---

## 5. Environmental Information

- **Non-genetic contributors** primarily influence **disease expression and complications** (e.g., friction/trauma precipitating blistering; chronic wounds and infections) rather than act as primary causes (bardhan2020epidermolysisbullosa pages 1-2).
- In severe disease, downstream systemic complications include infection/sepsis-related mortality in early life for junctional forms in some cohorts (murashkin2024congenitalepidermolysisbullosa pages 1-2).

---

## 6. Mechanism / Pathophysiology (causal chains, upstream vs downstream)

### Canonical mechanistic chain
1. **Germline pathogenic variant(s)** in skin adhesion/structural genes (e.g., COL7A1, LAMB3, KRT5/KRT14). (Upstream cause) (bardhan2020epidermolysisbullosa pages 1-2, bardhan2020epidermolysisbullosa pages 10-11)
2. **Loss/dysfunction of adhesion structures** at a specific ultrastructural level (intraepidermal; lamina lucida; sublamina densa; mixed). (Core molecular defect) (bardhan2020epidermolysisbullosa pages 1-2, bischof2024emerginggenetherapeutics pages 1-2)
3. **Mechanical trauma** → **epidermal–dermal separation** → blisters/erosions. (Trigger-to-lesion mechanism) (bardhan2020epidermolysisbullosa pages 1-2, bischof2024emerginggenetherapeutics pages 1-2)
4. **Chronic wounds + inflammation + fibrosis/scarring** → deformities (pseudosyndactyly), strictures, nutritional compromise, anemia; high risk of aggressive cSCC especially in severe RDEB. (Downstream complications) (sandoval2025towardsextracellularvesicles pages 1-2, hwang2024therapiesforcutaneous pages 1-3, bardhan2020epidermolysisbullosa pages 5-6)

### Cellular and tissue structures (ontology suggestions)
- **GO biological processes (examples):** *cell adhesion*, *extracellular matrix organization*, *wound healing*, *inflammatory response*, *keratinocyte differentiation*.
- **CL cell types (examples):** *keratinocyte* (CL:0000312), *fibroblast* (CL:0000057), *immune cells* relevant to wound inflammation (e.g., macrophage CL:0000235).
- **Subcellular / structural components (GO cellular component examples):** basement membrane (GO:0005604), hemidesmosome (GO:0030056), intermediate filament (GO:0005882).

### Squamous cell carcinoma as a major downstream mechanism
A major EB review identifies SCC as a feared complication and leading cause of mortality (bardhan2020epidermolysisbullosa pages 1-2). A 2024 systematic review in RDEB-cSCC quantifies high cumulative incidence and mortality, consistent with aggressive malignant transformation in chronic wound environments (hwang2024therapiesforcutaneous pages 1-3).

---

## 7. Anatomical Structures Affected (with UBERON/CL suggestions)

### Organ and system level
- **Primary:** skin (UBERON:0002097), oral mucosa and other mucosal sites (mucocutaneous involvement) (bardhan2020epidermolysisbullosa pages 1-2).
- **Common extracutaneous sites in severe subtypes:** eyes, airway, gastrointestinal tract (e.g., esophagus), genitourinary tract (noted in RDEB descriptions) (sandoval2025towardsextracellularvesicles pages 1-2).

### Tissue and cell level
- **Tissues:** epidermis, dermis, basement membrane zone / dermal–epidermal junction (bischof2024emerginggenetherapeutics pages 1-2).
- **Cells:** basal keratinocytes (EBS), epithelial cells forming hemidesmosomes and basement membrane attachments, dermal fibroblasts contributing to fibrosis and scarring.

### Localization and laterality
Not specifically emphasized in the retrieved evidence; generally widespread (generalized types) vs localized (e.g., localized EBS) distributions occur (suru2024epidemiologicalcharacteristicsof pages 4-6).

---

## 8. Temporal Development (onset, progression, staging)

### Onset
EB often manifests **at birth or in early infancy**, particularly in severe subtypes; RDEB is noted to typically manifest at birth (sandoval2025towardsextracellularvesicles pages 1-2).

### Progression and natural history
Course depends on subtype and severity. Examples from Eastern European registry-style data:
- Romanian cohort had substantial pediatric representation, but also adult survival depending on type/subtype (suru2024epidemiologicalcharacteristicsof pages 6-9).
- Russian pediatric registry data show substantial early mortality in junctional forms, with survival probability dropping “almost to 0% in the first 100 days” for junctional congenital EB (murashkin2024congenitalepidermolysisbullosa pages 1-2).

---

## 9. Inheritance and Population

### Epidemiology (recent registry-derived estimates, prioritizing 2024)
**Romania (2012–2024; point reference 31 Dec 2023):**
- Point prevalence: **6.77 per million population**; incidence: **24.23 per million live births** (Jun 2024; URL: https://doi.org/10.3390/jcm13133742) (suru2024epidemiologicalcharacteristicsof pages 1-2).
- Major type distribution: EBS **21%**, JEB **3%**, DEB **63%**, KEB **2%**, EB NOS **11%** (suru2024epidemiologicalcharacteristicsof pages 1-2).
- Sex distribution reported as slight female preponderance (approx. 52% vs 48%) (suru2024epidemiologicalcharacteristicsof pages 6-9).

**Russian Federation children (registry as of 2024; ages 0–17):**
- Pediatric prevalence: **15.48 per 1,000,000 children**; sex ratio **boys:girls 1.08:1** (Oct 2024; URL: https://doi.org/10.15690/vsp.v23i5.2808) (murashkin2024congenitalepidermolysisbullosa pages 1-2).
- Type counts among 491 children: dystrophic **261**, simplex **191**, junctional **31**, Kindler **8** (murashkin2024congenitalepidermolysisbullosa pages 1-2).
- Five-year mean birth rate: **2.13 per 100,000 births** (2019–2023) (murashkin2024congenitalepidermolysisbullosa pages 1-2).
- Mortality: 22 deaths recorded; **junctional** accounts for **59.1%** of deaths; highest mortality in age 0–1 years (65.2% of deaths) with sepsis-related multi-organ failure noted as leading cause (murashkin2024congenitalepidermolysisbullosa pages 1-2).

### Founder effects/consanguinity
The Russian registry highlights a high-burden region (Dagestan) with “apparently” high consanguineous marriage rates (50%) corresponding to higher case counts, suggesting a role for autosomal recessive inheritance and local population structure (murashkin2024congenitalepidermolysisbullosa pages 2-3).

---

## 10. Diagnostics

### Diagnostic workflow (current standard framing)
A major authoritative review emphasizes that precise diagnosis relies on correlating:
- **Clinical phenotype**, plus
- **Electron microscopy** and **immunohistological features** (including immunofluorescence mapping), plus
- **Mutational analyses (genetic testing)** (bardhan2020epidermolysisbullosa pages 1-2).

### Real-world diagnostic utilization (Romania 2012–2024)
In the Romanian cohort:
- **83/152 (54.6%)** were clinically diagnosed only.
- **48 (31.5%)** had molecular genetic testing.
- Smaller fractions had IF mapping (IFM) and/or transmission electron microscopy (TEM), including **2** with IFM+TEM and additional cases combining IFM or TEM with genetics (suru2024epidemiologicalcharacteristicsof pages 4-6).

### Differential diagnosis
Not specifically enumerated in the retrieved evidence; standard differentials include acquired blistering diseases and other skin fragility syndromes—note that the Romanian study explicitly excluded acquired EB and other fragility syndromes (suru2024epidemiologicalcharacteristicsof pages 2-4).

---

## 11. Outcome / Prognosis (including key statistics)

### cSCC risk and outcomes in RDEB (2024 systematic review; 157 cases)
A 2024 systematic review of **157 RDEB-cSCC cases** reports:
- Cumulative risk for at least one cSCC: **7.5% by age 20** rising to **80% by age 45** (May 2024; URL: https://doi.org/10.1186/s13023-024-03190-1) (hwang2024therapiesforcutaneous pages 1-3).
- Mortality estimates: **38.7% by 35 years**, **70% by 40**, **78.7% by 55** (hwang2024therapiesforcutaneous pages 1-3).
- Tumor features: well-differentiated **64.1%**, ulcerated **59.6%**, ≥2 cm **77.6%**; median age at diagnosis **30 years** (hwang2024therapiesforcutaneous pages 1-3).

### Survival variation by EB type (2024 Romania)
Romanian survival analysis indicated poorer survival for JEB and unspecified cases compared to other types (Kaplan–Meier curves shown; see extracted figure) (suru2024epidemiologicalcharacteristicsof media bf76e012).

---

## 12. Treatment (current applications, real-world implementations, and 2023–2024 developments)

### Standard of care: supportive, multidisciplinary management
In the absence of universally curative therapy, management focuses on minimizing blister formation, wound care, symptom relief, and management of complications (including SCC) (bardhan2020epidermolysisbullosa pages 1-2).

### FDA-approved topical gene therapy for DEB (major 2023 milestone)
A 2024 review of EB gene therapeutics describes the first approved in vivo topical gene replacement product:
- Mechanism: HSV-1–based topical vector delivering functional **COL7A1** to wounds (bischof2024emerginggenetherapeutics pages 8-9).
- Phase III (GEM-3; NCT04491604; intrapatient matched wound pairs, n=31) outcomes: **71% complete wound closure at 3 months and 67% at 6 months** vs placebo ~**20–22%** (bischof2024emerginggenetherapeutics pages 8-9, prodinger2024neuelokalund pages 1-2).
- This product is widely referenced as **Vyjuvek (beremagene geperpavec, B-VEC)** and described as FDA approved in 2023 (prodinger2024neuelokalund pages 1-2, sandoval2025towardsextracellularvesicles pages 2-4).

### Implementation and payer impact (2024 economic evaluation)
Post-approval economic modeling estimates substantial payer impact in the US:
- Assumed base-case annual price **$300,000 per patient per year**.
- Estimated first-year total expenditure **$268 million** (and the therapy described as weekly lifelong administration in the summarized source) (sandoval2025towardsextracellularvesicles pages 2-4).

### Itch symptom management (2023 prospective registry evidence)
Despite frequent use of emollients and antihistamines, itch remains an unmet need in RDEB; only 61% of reviews reported using medication and satisfaction was low-moderate (mean 41.3/100) (mellerio2023itchinrecessive pages 6-7).

### Treatment of RDEB-associated cSCC (2024 systematic review)
Surgery remains the primary modality, with emerging use of anti-EGFR therapy and immunotherapy in advanced disease:
- Median survival from first cSCC diagnosis to death varied by regimen (e.g., ~2 years for surgery only; ~4–4.6 years with addition of anti-EGFR or immunotherapy in small subsets) (hwang2024therapiesforcutaneous pages 1-3).

### Other approved therapies
- **Filsuvez (Oleogel-S10)** is noted in recent reviews as an approved therapy for EB wound healing support, but detailed trial-level quantitative outcomes were not available in the retrieved evidence set here and should be curated from primary regulatory documents and pivotal trial publications (sandoval2025towardsextracellularvesicles pages 1-2).

### MAXO suggestions (examples)
- Gene therapy, topical administration: *gene therapy procedure*; *topical administration of therapeutic agent*.
- Wound care: *wound dressing*, *wound debridement* (when applicable), *pain management*, *pruritus management*.
- cSCC: *surgical excision*, *radiotherapy*, *systemic chemotherapy*, *epidermal growth factor receptor inhibitor therapy*, *immune checkpoint inhibitor therapy*.

---

## 13. Prevention

For a Mendelian disease, prevention focuses on genetic counseling and reproductive planning. The retrieved evidence set does not provide detailed guideline statements for prenatal testing/PGT/cascade testing; however, the importance of **precise molecular diagnosis** for genetic counseling and stratification is emphasized (bardhan2020epidermolysisbullosa pages 2-3).

Tertiary prevention is central in practice (e.g., preventing infections, malnutrition, contractures, strictures, and early detection of cSCC) (bardhan2020epidermolysisbullosa pages 1-2, hwang2024therapiesforcutaneous pages 1-3).

---

## 14. Other Species / Natural Disease
Not addressed in the retrieved evidence set.

---

## 15. Model Organisms
Not addressed in the retrieved evidence set.

---

## Key structured summaries (artifacts)
The following tables summarize subtype genetics/features and the most evidence-supported 2023–2024 treatment landscape.

| EB type | Primary cleavage level / skin layer | Core causal genes mentioned in retrieved evidence | Typical inheritance | Hallmark clinical features | Major complications | Supporting context |
|---|---|---|---|---|---|---|
| Epidermolysis bullosa simplex (EBS) | Intraepidermal cleavage within basal keratinocytes / epidermis | KRT5, KRT14, PLEC | Usually autosomal dominant; some autosomal recessive forms | Skin fragility and trauma-induced blistering, often from birth or infancy; may include inflammation, failure to thrive, itch, neuropathic pain; some PLEC-associated forms have muscular dystrophy | Variable severity; multisystem involvement in some forms | (bardhan2020epidermolysisbullosa pages 1-2, bischof2024emerginggenetherapeutics pages 1-2, bardhan2020epidermolysisbullosa pages 6-7, suru2024epidemiologicalcharacteristicsof pages 4-6) |
| Junctional EB (JEB) | Cleavage within the lamina lucida of the dermal-epidermal junction / basement membrane zone | LAMA3, LAMB3, LAMC2, ITGA6, ITGB4, COL17A1 | Mostly autosomal recessive | Severe mucocutaneous fragility with blistering and erosions; some forms show exuberant granulation tissue, airway and upper GI involvement | In severe JEB, high infant mortality; failure to thrive, sepsis, respiratory failure, cardiomyopathy; laryngeal disease can cause respiratory compromise and death | (bardhan2020epidermolysisbullosa pages 1-2, bardhan2020epidermolysisbullosa pages 4-5, bischof2024emerginggenetherapeutics pages 1-2, bardhan2020epidermolysisbullosa pages 6-7) |
| Dystrophic EB, dominant (DDEB) | Sublamina densa / upper dermis, due to anchoring fibril dysfunction | COL7A1 | Autosomal dominant | Trauma-induced blistering with scarring; generally milder than severe recessive disease; nail and mucosal involvement may occur | Chronic wounds and scarring; cancer risk lower than severe RDEB but elevated in some patients | (bardhan2020epidermolysisbullosa pages 4-5, bardhan2020epidermolysisbullosa pages 10-11, suru2024epidemiologicalcharacteristicsof pages 4-6) |
| Dystrophic EB, recessive (RDEB) | Sublamina densa / upper dermis, due to absent or markedly reduced type VII collagen anchoring fibrils | COL7A1 | Autosomal recessive | Congenital or early-onset severe blistering, chronic wounds, scarring, mitten deformities/pseudosyndactyly, microstomia, esophageal strictures, pain and itch | Aggressive cutaneous squamous cell carcinoma is the leading cause of death in adults with severe RDEB; also anemia, malnutrition, renal disease, infection/sepsis, fibrosis | (hwang2024therapiesforcutaneous pages 1-3, bardhan2020epidermolysisbullosa pages 5-6, bardhan2020epidermolysisbullosa pages 10-11, murashkin2024congenitalepidermolysisbullosa pages 2-3) |
| Kindler EB / Kindler syndrome | Mixed and variable cleavage planes across multiple skin levels | FERMT1 (KIND1) | Autosomal recessive | Skin fragility, blistering, and photosensitivity beginning in early childhood; progressive poikiloderma may occur | Mucosal disease and later epithelial malignancies including non-melanoma skin cancer/SCC in adults | (bardhan2020epidermolysisbullosa pages 1-2, bischof2024emerginggenetherapeutics pages 1-2, bardhan2020epidermolysisbullosa pages 10-11, suru2024epidemiologicalcharacteristicsof pages 4-6) |


*Table: This table summarizes the major epidermolysis bullosa types by tissue cleavage level, core genes, inheritance, hallmark clinical features, and major complications. It is designed as a compact ontology-ready overview for quick reference in a disease knowledge base.*

| Intervention | Target EB subtype | Mechanism | Regulatory status | Key study/trial + date | Key quantitative outcomes | Notes/limitations | Supporting context IDs |
|---|---|---|---|---|---|---|---|
| Beremagene geperpavec (B-VEC; Vyjuvek) | Dystrophic EB, especially COL7A1-related DEB/RDEB | Topical HSV-1–based in vivo gene replacement delivering functional **COL7A1** to wounded skin | **FDA approved May 2023**; EMA approval noted in 2025 sources | GEM-3 phase 3, randomized intra-patient matched wound-pair trial, **NCT04491604**; weekly topical treatment for 26 weeks; NEJM trial cited from 2022; FDA approval noted 2023 | Complete wound closure with B-VEC: **71% at 3 months** and **67% at 6 months** vs placebo **20–22%**; phase 1/2: **17/18 wounds** completely closed at 3 months; median time to closure **13.5 vs 22.5 days**; mean duration of closure **103 vs 16.5 days** | Paired-lesion design; repeated application required; topical HSV vector does not penetrate intact skin well; safety profile mainly mild-moderate AEs, and serious AEs in later summaries were not attributed to product (bischof2024emerginggenetherapeutics pages 8-9, prodinger2024neuelokalund pages 1-2, NCT04491604 chunk 1, lisinska2025genetherapiesin pages 2-4) | (bischof2024emerginggenetherapeutics pages 8-9, prodinger2024neuelokalund pages 1-2, NCT04491604 chunk 1, lisinska2025genetherapiesin pages 2-4) |
| B-VEC open-label extension | Dystrophic EB previously treated or treatment-naive | Continued topical **COL7A1** gene replacement | Post-approval/extension evidence; not a separate approval | Open-label extension **NCT04917874**; published 2025, rollover + treatment-naive participants | **47 subjects**; treatment up to **112 weeks** (median **81 weeks**); maintained wound closure in rollover subjects ranged **61.1–89.5%** through month 12; no new safety signals detected | Open-label, variable follow-up, exploratory PROs inconclusive for QoL; publication is 2025 but highly relevant for real-world durability/safety | (marinkovich2025longtermsafetyand pages 1-2) |
| Filsuvez (Oleogel-S10) | EB wound healing support across inherited EB indications in recent reviews | Topical birch triterpene oleogel intended to support re-epithelialization/wound healing | Recently approved; referenced as approved in 2022–2024 reviews | Mentioned in 2024–2025 EB therapeutic reviews | Detailed quantitative trial outcomes **not present in current retrieved evidence** | Should be included as a recent approved therapy, but the present evidence base here does not provide trial-level numeric endpoints; avoid overclaiming | (sandoval2025towardsextracellularvesicles pages 1-2, prodinger2024neuelokalund pages 1-2) |
| Supportive care / itch management (PEBLES registry) | Recessive dystrophic EB subtypes (RDEB-S, RDEB-I, RDEB-Inv, RDEB-Pru) | Symptom control with emollients, topical corticosteroids, antihistamines and related anti-pruritic measures | Standard supportive care; no disease-modifying approval claim | PEBLES prospective register study, published **2023** | Itch present in preceding month in **93% of 243 reviews** from **50 participants**; **61%** of reviews reported itch medication use; at index, emollients **12/50 (24%)**, oral antihistamines **14/50 (28%)**; mean medication satisfaction **41.3/100** | Strong evidence of unmet need: frequent itch, greater severity/distress in RDEB-S and RDEB-Pru, limited perceived efficacy of current medications | (mellerio2023itchinrecessive pages 1-2, mellerio2023itchinrecessive pages 6-7, mellerio2023itchinrecessive pages 4-6, mellerio2023itchinrecessive pages 2-4) |
| cSCC treatment in RDEB: surgery, anti-EGFR therapy, immunotherapy | RDEB-associated cutaneous squamous cell carcinoma | Oncologic local/systemic treatment after malignant transformation; anti-EGFR or immune checkpoint blockade used in advanced disease | No EB-specific regulatory approval summarized here; used in practice based on cSCC management | Systematic review of **157 cases**, published **2024** | Median survival from first cSCC diagnosis to death: **2.0 years** (surgery only), **4.0 years** (+anti-EGFR), **4.6 years** (+immunotherapy), **1.85 years** (surgery+chemotherapy), **4.0 years** (surgery+radiotherapy), **9.5 years** (surgery+chemotherapy+radiotherapy; very small n); surgery was primary treatment in **128** cases | Evidence mostly case reports/cohorts, major confounding by multimodal treatment and small sample sizes; adverse events included impaired wound healing with immunotherapy and nausea/fatigue with anti-EGFR therapy | (hwang2024therapiesforcutaneous pages 1-3) |
| Health-system implementation: projected B-VEC spending | US DEB population eligible for B-VEC | Economic implementation analysis rather than biologic mechanism | Reflects post-approval payer impact after FDA approval | JAMA Dermatology economic evaluation, **2024** | Estimated **894** US DEB patients eligible in year 1; projected spending **$268 million** first year and **$805 million** over 3 years; assumed base-case cost **$300,000/patient/year**; lifetime total cost estimated **$15–17 million/patient** | Important for real-world access and reimbursement; FDA indication included both AR and AD DEB, with limited direct trial data in dominant disease noted by authors | (sandoval2025towardsextracellularvesicles pages 2-4) |


*Table: This table summarizes the most clinically relevant epidermolysis bullosa therapies and management strategies emphasized in the retrieved 2023-2024 evidence, including approved gene therapy, supportive care, and cSCC treatment. It is useful for quickly comparing mechanisms, regulatory status, quantitative outcomes, and implementation caveats.*

---

## Notes on evidence limitations and curation gaps
1. **OMIM/Orphanet/ICD/MeSH identifiers** were not directly retrievable via the current tool calls; they should be added from those resources in a follow-on curation pass.
2. Several key topics requested for a knowledge base entry (modifier genes, epigenetics, model organisms, comparative disease in animals, and detailed prevention/genetic screening guidelines) are not covered by the retrieved documents and require targeted additional retrieval.
3. For **Filsuvez (Oleogel-S10)**, the present evidence confirms it as a recently approved therapy in reviews but does not provide pivotal-trial effect sizes; primary trial publications/regulatory assessments should be cited before adding numeric claims.

---

## Included URLs and publication dates (selected high-value sources)
- Bardhan et al. *Nature Reviews Disease Primers* (Sep 2020): https://doi.org/10.1038/s41572-020-0210-0 (bardhan2020epidermolysisbullosa pages 1-2)
- Suru et al. *Journal of Clinical Medicine* (Jun 2024): https://doi.org/10.3390/jcm13133742 (suru2024epidemiologicalcharacteristicsof pages 1-2)
- Murashkin et al. *Current Pediatrics* (Oct 2024): https://doi.org/10.15690/vsp.v23i5.2808 (murashkin2024congenitalepidermolysisbullosa pages 1-2)
- Mellerio et al. *Orphanet Journal of Rare Diseases* (Aug 2023): https://doi.org/10.1186/s13023-023-02817-z (mellerio2023itchinrecessive pages 1-2)
- Hwang et al. *Orphanet Journal of Rare Diseases* (May 2024): https://doi.org/10.1186/s13023-024-03190-1 (hwang2024therapiesforcutaneous pages 1-3)
- Aranda-Reneo et al. *Orphanet Journal of Rare Diseases* (Sep 2024): https://doi.org/10.1186/s13023-024-03328-1 (arandareneo2024economicburdenand pages 1-2)
- Bischof et al. *International Journal of Molecular Sciences* (Feb 2024): https://doi.org/10.3390/ijms25042243 (bischof2024emerginggenetherapeutics pages 1-2)



References

1. (OpenTargets Search: Epidermolysis bullosa): Open Targets Query (Epidermolysis bullosa, 30 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (bardhan2020epidermolysisbullosa pages 1-2): Ajoy Bardhan, Leena Bruckner-Tuderman, Iain L. C. Chapple, Jo-David Fine, Natasha Harper, Cristina Has, Thomas M. Magin, M. Peter Marinkovich, John F. Marshall, John A. McGrath, Jemima E. Mellerio, Rex Polson, and Adrian H. Heagerty. Epidermolysis bullosa. Nature Reviews Disease Primers, 6:1-27, Sep 2020. URL: https://doi.org/10.1038/s41572-020-0210-0, doi:10.1038/s41572-020-0210-0. This article has 551 citations.

3. (bischof2024emerginggenetherapeutics pages 1-2): Johannes Bischof, Markus Hierl, and Ulrich Koller. Emerging gene therapeutics for epidermolysis bullosa under development. International Journal of Molecular Sciences, 25:2243, Feb 2024. URL: https://doi.org/10.3390/ijms25042243, doi:10.3390/ijms25042243. This article has 37 citations.

4. (hwang2024therapiesforcutaneous pages 1-3): Austin Hwang, Andie Kwon, Corinne H. Miller, Antonia Reimer-Taschenbrecker, and Amy S. Paller. Therapies for cutaneous squamous cell carcinoma in recessive dystrophic epidermolysis bullosa: a systematic review of 157 cases. Orphanet Journal of Rare Diseases, May 2024. URL: https://doi.org/10.1186/s13023-024-03190-1, doi:10.1186/s13023-024-03190-1. This article has 13 citations and is from a peer-reviewed journal.

5. (suru2024epidemiologicalcharacteristicsof pages 6-9): Alina Suru, Sorina Dănescu, Alina Călinescu-Stîncanu, Denis Iorga, Mihai Dascălu, Adrian Baican, George-Sorin Țiplica, and Carmen Maria Sălăvăstru. Epidemiological characteristics of inherited epidermolysis bullosa in an eastern european population. Journal of Clinical Medicine, 13:3742, Jun 2024. URL: https://doi.org/10.3390/jcm13133742, doi:10.3390/jcm13133742. This article has 6 citations.

6. (bardhan2020epidermolysisbullosa pages 6-7): Ajoy Bardhan, Leena Bruckner-Tuderman, Iain L. C. Chapple, Jo-David Fine, Natasha Harper, Cristina Has, Thomas M. Magin, M. Peter Marinkovich, John F. Marshall, John A. McGrath, Jemima E. Mellerio, Rex Polson, and Adrian H. Heagerty. Epidermolysis bullosa. Nature Reviews Disease Primers, 6:1-27, Sep 2020. URL: https://doi.org/10.1038/s41572-020-0210-0, doi:10.1038/s41572-020-0210-0. This article has 551 citations.

7. (bardhan2020epidermolysisbullosa pages 4-5): Ajoy Bardhan, Leena Bruckner-Tuderman, Iain L. C. Chapple, Jo-David Fine, Natasha Harper, Cristina Has, Thomas M. Magin, M. Peter Marinkovich, John F. Marshall, John A. McGrath, Jemima E. Mellerio, Rex Polson, and Adrian H. Heagerty. Epidermolysis bullosa. Nature Reviews Disease Primers, 6:1-27, Sep 2020. URL: https://doi.org/10.1038/s41572-020-0210-0, doi:10.1038/s41572-020-0210-0. This article has 551 citations.

8. (bardhan2020epidermolysisbullosa pages 10-11): Ajoy Bardhan, Leena Bruckner-Tuderman, Iain L. C. Chapple, Jo-David Fine, Natasha Harper, Cristina Has, Thomas M. Magin, M. Peter Marinkovich, John F. Marshall, John A. McGrath, Jemima E. Mellerio, Rex Polson, and Adrian H. Heagerty. Epidermolysis bullosa. Nature Reviews Disease Primers, 6:1-27, Sep 2020. URL: https://doi.org/10.1038/s41572-020-0210-0, doi:10.1038/s41572-020-0210-0. This article has 551 citations.

9. (suru2024epidemiologicalcharacteristicsof pages 4-6): Alina Suru, Sorina Dănescu, Alina Călinescu-Stîncanu, Denis Iorga, Mihai Dascălu, Adrian Baican, George-Sorin Țiplica, and Carmen Maria Sălăvăstru. Epidemiological characteristics of inherited epidermolysis bullosa in an eastern european population. Journal of Clinical Medicine, 13:3742, Jun 2024. URL: https://doi.org/10.3390/jcm13133742, doi:10.3390/jcm13133742. This article has 6 citations.

10. (mellerio2023itchinrecessive pages 1-2): Jemima E. Mellerio, Elizabeth I. Pillay, Lesedi Ledwaba-Chapman, Alessandra Bisquera, Susan J. Robertson, Marieta Papanikolaou, John A. McGrath, Yanzhong Wang, Anna E. Martinez, and Eunice Jeffs. Itch in recessive dystrophic epidermolysis bullosa: findings of pebles, a prospective register study. Orphanet Journal of Rare Diseases, Aug 2023. URL: https://doi.org/10.1186/s13023-023-02817-z, doi:10.1186/s13023-023-02817-z. This article has 14 citations and is from a peer-reviewed journal.

11. (sandoval2025towardsextracellularvesicles pages 1-2): Aaron Gabriel W. Sandoval and Evangelos V. Badiavas. Towards extracellular vesicles in the treatment of epidermolysis bullosa. Bioengineering, 12:574, May 2025. URL: https://doi.org/10.3390/bioengineering12060574, doi:10.3390/bioengineering12060574. This article has 3 citations.

12. (mellerio2023itchinrecessive pages 4-6): Jemima E. Mellerio, Elizabeth I. Pillay, Lesedi Ledwaba-Chapman, Alessandra Bisquera, Susan J. Robertson, Marieta Papanikolaou, John A. McGrath, Yanzhong Wang, Anna E. Martinez, and Eunice Jeffs. Itch in recessive dystrophic epidermolysis bullosa: findings of pebles, a prospective register study. Orphanet Journal of Rare Diseases, Aug 2023. URL: https://doi.org/10.1186/s13023-023-02817-z, doi:10.1186/s13023-023-02817-z. This article has 14 citations and is from a peer-reviewed journal.

13. (mellerio2023itchinrecessive pages 6-7): Jemima E. Mellerio, Elizabeth I. Pillay, Lesedi Ledwaba-Chapman, Alessandra Bisquera, Susan J. Robertson, Marieta Papanikolaou, John A. McGrath, Yanzhong Wang, Anna E. Martinez, and Eunice Jeffs. Itch in recessive dystrophic epidermolysis bullosa: findings of pebles, a prospective register study. Orphanet Journal of Rare Diseases, Aug 2023. URL: https://doi.org/10.1186/s13023-023-02817-z, doi:10.1186/s13023-023-02817-z. This article has 14 citations and is from a peer-reviewed journal.

14. (arandareneo2024economicburdenand pages 1-2): Isaac Aranda-Reneo, Juan Oliva-Moreno, Luz María Peña-Longobardo, Álvaro Rafael Villar-Hernández, and Julio López-Bastida. Economic burden and health-related quality of life in patients with epidermolysis bullosa in spain. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03328-1, doi:10.1186/s13023-024-03328-1. This article has 4 citations and is from a peer-reviewed journal.

15. (arandareneo2024economicburdenand pages 6-7): Isaac Aranda-Reneo, Juan Oliva-Moreno, Luz María Peña-Longobardo, Álvaro Rafael Villar-Hernández, and Julio López-Bastida. Economic burden and health-related quality of life in patients with epidermolysis bullosa in spain. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03328-1, doi:10.1186/s13023-024-03328-1. This article has 4 citations and is from a peer-reviewed journal.

16. (murashkin2024congenitalepidermolysisbullosa pages 1-2): Nikolay N. Murashkin, Roman V. Epishev, Olga S. Orlova, Alena А. Kuratova, and Victoriya S. Polenova. Congenital epidermolysis bullosa epidemiology among children of russian federation. Current Pediatrics, 23:316-328, Oct 2024. URL: https://doi.org/10.15690/vsp.v23i5.2808, doi:10.15690/vsp.v23i5.2808. This article has 2 citations.

17. (bardhan2020epidermolysisbullosa pages 5-6): Ajoy Bardhan, Leena Bruckner-Tuderman, Iain L. C. Chapple, Jo-David Fine, Natasha Harper, Cristina Has, Thomas M. Magin, M. Peter Marinkovich, John F. Marshall, John A. McGrath, Jemima E. Mellerio, Rex Polson, and Adrian H. Heagerty. Epidermolysis bullosa. Nature Reviews Disease Primers, 6:1-27, Sep 2020. URL: https://doi.org/10.1038/s41572-020-0210-0, doi:10.1038/s41572-020-0210-0. This article has 551 citations.

18. (suru2024epidemiologicalcharacteristicsof pages 1-2): Alina Suru, Sorina Dănescu, Alina Călinescu-Stîncanu, Denis Iorga, Mihai Dascălu, Adrian Baican, George-Sorin Țiplica, and Carmen Maria Sălăvăstru. Epidemiological characteristics of inherited epidermolysis bullosa in an eastern european population. Journal of Clinical Medicine, 13:3742, Jun 2024. URL: https://doi.org/10.3390/jcm13133742, doi:10.3390/jcm13133742. This article has 6 citations.

19. (murashkin2024congenitalepidermolysisbullosa pages 2-3): Nikolay N. Murashkin, Roman V. Epishev, Olga S. Orlova, Alena А. Kuratova, and Victoriya S. Polenova. Congenital epidermolysis bullosa epidemiology among children of russian federation. Current Pediatrics, 23:316-328, Oct 2024. URL: https://doi.org/10.15690/vsp.v23i5.2808, doi:10.15690/vsp.v23i5.2808. This article has 2 citations.

20. (suru2024epidemiologicalcharacteristicsof pages 2-4): Alina Suru, Sorina Dănescu, Alina Călinescu-Stîncanu, Denis Iorga, Mihai Dascălu, Adrian Baican, George-Sorin Țiplica, and Carmen Maria Sălăvăstru. Epidemiological characteristics of inherited epidermolysis bullosa in an eastern european population. Journal of Clinical Medicine, 13:3742, Jun 2024. URL: https://doi.org/10.3390/jcm13133742, doi:10.3390/jcm13133742. This article has 6 citations.

21. (suru2024epidemiologicalcharacteristicsof media bf76e012): Alina Suru, Sorina Dănescu, Alina Călinescu-Stîncanu, Denis Iorga, Mihai Dascălu, Adrian Baican, George-Sorin Țiplica, and Carmen Maria Sălăvăstru. Epidemiological characteristics of inherited epidermolysis bullosa in an eastern european population. Journal of Clinical Medicine, 13:3742, Jun 2024. URL: https://doi.org/10.3390/jcm13133742, doi:10.3390/jcm13133742. This article has 6 citations.

22. (bischof2024emerginggenetherapeutics pages 8-9): Johannes Bischof, Markus Hierl, and Ulrich Koller. Emerging gene therapeutics for epidermolysis bullosa under development. International Journal of Molecular Sciences, 25:2243, Feb 2024. URL: https://doi.org/10.3390/ijms25042243, doi:10.3390/ijms25042243. This article has 37 citations.

23. (prodinger2024neuelokalund pages 1-2): Christine Prodinger and Martin Laimer. Neue lokal- und systemtherapien bei epidermolysis bullosa. hautnah, 23:43-49, Feb 2024. URL: https://doi.org/10.1007/s12326-024-00627-z, doi:10.1007/s12326-024-00627-z. This article has 1 citations.

24. (sandoval2025towardsextracellularvesicles pages 2-4): Aaron Gabriel W. Sandoval and Evangelos V. Badiavas. Towards extracellular vesicles in the treatment of epidermolysis bullosa. Bioengineering, 12:574, May 2025. URL: https://doi.org/10.3390/bioengineering12060574, doi:10.3390/bioengineering12060574. This article has 3 citations.

25. (bardhan2020epidermolysisbullosa pages 2-3): Ajoy Bardhan, Leena Bruckner-Tuderman, Iain L. C. Chapple, Jo-David Fine, Natasha Harper, Cristina Has, Thomas M. Magin, M. Peter Marinkovich, John F. Marshall, John A. McGrath, Jemima E. Mellerio, Rex Polson, and Adrian H. Heagerty. Epidermolysis bullosa. Nature Reviews Disease Primers, 6:1-27, Sep 2020. URL: https://doi.org/10.1038/s41572-020-0210-0, doi:10.1038/s41572-020-0210-0. This article has 551 citations.

26. (NCT04491604 chunk 1):  Ph 3 Efficacy and Safety of B-VEC for the Treatment of DEB. Krystal Biotech, Inc.. 2020. ClinicalTrials.gov Identifier: NCT04491604

27. (lisinska2025genetherapiesin pages 2-4): Wiktoria Lisińska, Patryk Cegiełka, Zuzanna Zalewska, Natalia Bien, Dorota Sobolewska-Sztychny, Joanna Narbutt, and Aleksandra Lesiak. Gene therapies in dermatological diseases: a breakthrough in treatment. International Journal of Molecular Sciences, 26:6592, Jul 2025. URL: https://doi.org/10.3390/ijms26146592, doi:10.3390/ijms26146592. This article has 0 citations.

28. (marinkovich2025longtermsafetyand pages 1-2): M. Peter Marinkovich, Amy S. Paller, Shireen V. Guide, Mercedes E. Gonzalez, Anne W. Lucky, Işın Sinem Bağcı, Brittani Agostini, Kolleen Fitzgerald, Shijie Chen, Hubert Chen, Meghan M. Conner, and Suma M. Krishnan. Long-term safety and tolerability of beremagene geperpavec-svdt (b-vec) in an open-label extension study of patients with dystrophic epidermolysis bullosa. American Journal of Clinical Dermatology, 26:623-635, Apr 2025. URL: https://doi.org/10.1007/s40257-025-00942-y, doi:10.1007/s40257-025-00942-y. This article has 12 citations and is from a peer-reviewed journal.

29. (mellerio2023itchinrecessive pages 2-4): Jemima E. Mellerio, Elizabeth I. Pillay, Lesedi Ledwaba-Chapman, Alessandra Bisquera, Susan J. Robertson, Marieta Papanikolaou, John A. McGrath, Yanzhong Wang, Anna E. Martinez, and Eunice Jeffs. Itch in recessive dystrophic epidermolysis bullosa: findings of pebles, a prospective register study. Orphanet Journal of Rare Diseases, Aug 2023. URL: https://doi.org/10.1186/s13023-023-02817-z, doi:10.1186/s13023-023-02817-z. This article has 14 citations and is from a peer-reviewed journal.
