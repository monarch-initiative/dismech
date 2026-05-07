---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T08:56:56.164188'
end_time: '2026-05-07T09:17:04.335760'
duration_seconds: 1208.17
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Malignant Non-Dysgerminomatous Germ Cell Tumor Of Ovary
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Malignant Non-Dysgerminomatous Germ Cell Tumor Of Ovary
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Malignant Non-Dysgerminomatous Germ Cell Tumor Of Ovary** covering all of the
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
- **Disease Name:** Malignant Non-Dysgerminomatous Germ Cell Tumor Of Ovary
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Malignant Non-Dysgerminomatous Germ Cell Tumor Of Ovary** covering all of the
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


# Comprehensive Research Report: Malignant Non‑Dysgerminomatous Germ Cell Tumor of Ovary

## Target Disease
- **Disease name (requested):** Malignant Non‑Dysgerminomatous Germ Cell Tumor Of Ovary
- **Canonical entity used in this report:** *Malignant ovarian germ cell tumor* (malignant OvGCT) excluding dysgerminoma (i.e., non‑dysgerminomatous / non‑seminomatous malignant ovarian germ cell tumors). Core malignant non‑dysgerminomatous subtypes include **yolk sac tumor**, **embryonal carcinoma**, **choriocarcinoma**, **immature teratoma**, and **mixed germ cell tumor**. (margioulasiarkou2023therapeuticmanagementand pages 1-2, saani2023clinicalchallengesin pages 1-2)
- **MONDO ID:** **MONDO_0018171** (*malignant germ cell tumor of ovary*). (OpenTargets Search: ovarian germ cell tumor)
- **Category:** Rare non‑epithelial ovarian cancer (germ cell tumor group). (saani2023clinicalchallengesin pages 1-2)

### Executive summary (high‑value facts)
- Malignant ovarian germ cell tumors are **rare (≈2–5% of ovarian cancers)**, occur primarily in **adolescents/young adults**, and are typically **highly chemosensitive**. (saani2023clinicalchallengesin pages 1-2, sakaguchimukaida2023systematicreviewof pages 1-2)
- Recommended diagnostic work‑up includes **pelvic ultrasound + cross‑sectional staging (CT/MRI) + serum tumor markers** (AFP, β‑hCG, LDH; often CA125) and expert pathology with immunohistochemistry and, when needed, **12p/i(12p) testing**. (saani2023clinicalchallengesin pages 2-3, margioulasiarkou2023therapeuticmanagementand pages 12-13)
- Standard management is **fertility‑sparing surgery** when safe plus **platinum‑based chemotherapy** (most commonly **BEP**) for higher‑risk disease; **stage I** outcomes are excellent with **~90% long‑term disease‑free survival** in reported series. (saani2023clinicalchallengesin pages 5-6, margioulasiarkou2023therapeuticmanagementand pages 16-17)
- For advanced disease where surgery may be morbid, a 2023 systematic review reported **NACT response ≈95.8%** and broadly similar survival ranges vs primary debulking in biased comparator cohorts. (sakaguchimukaida2023systematicreviewof pages 1-2)

| Domain | Compact summary |
|---|---|
| Epidemiology / incidence | Malignant ovarian germ cell tumors (MOGCTs) account for ~2–5% of ovarian cancers; yearly incidence reported as ~4 per 100,000 overall, with pediatric/adolescent incidence ~2.6 per 100,000 girls/year; OvGCT incidence in females age 15–19 is ~1.2 per 100,000. Regional proportion among ovarian tumors is higher in Asia (4.2%) and Central/South America (3.9%) than North America (2.0%) and Europe (1.3%). (saani2023clinicalchallengesin pages 1-2, margioulasiarkou2023therapeuticmanagementand pages 1-2, travis2024adolescentandyoung pages 3-4) |
| Typical age | Predominantly affects adolescents and young adults; common age range ~18–30 years, with many cases between ages 10–25 and OvGCTs the leading gynecologic cancer in women <25 years. (saani2023clinicalchallengesin pages 2-3, travis2024adolescentandyoung pages 3-4, sakaguchimukaida2023systematicreviewof pages 1-2) |
| Key non-dysgerminomatous subtypes | Non-dysgerminomatous / non-seminomatous ovarian GCT subtypes include yolk sac tumor, embryonal carcinoma, choriocarcinoma, immature teratoma, and mixed germ cell tumor; WHO 2020-based classifications in recent reviews list these as core malignant entities. (margioulasiarkou2023therapeuticmanagementand pages 1-2, saani2023clinicalchallengesin pages 1-2) |
| Core serum markers | AFP: hallmark of yolk sac tumor and may rise in immature teratoma; β-hCG: choriocarcinoma and some embryonal carcinoma; LDH: supportive for dysgerminoma but commonly included in diagnostic panels for all suspicious GCTs; CA125 often added in work-up. In pure ovarian immature teratoma, AFP elevation was 34% in children, rising to 83% when microscopic yolk-sac foci/Heifetz lesions were present; MaGIC pragmatic AFP cutoff compatible with IT diagnosis: <1000 kU/L (~<1210 ng/mL). (saani2023clinicalchallengesin pages 2-3, margioulasiarkou2023therapeuticmanagementand pages 12-13, pashankar2024consensusandcontroversy pages 2-3, saani2023clinicalchallengesin pages 3-5) |
| Imaging / staging | Initial imaging: pelvic/abdominal ultrasound; staging commonly adds abdomino-pelvic CT or MRI and chest X-ray/low-dose chest CT/thoracic CT. PET is reserved for selected cases. FIGO staging is used. Complete surgical staging may include peritoneal washings/cytology, full peritoneal inspection, omental biopsy/omentectomy, biopsies of suspicious peritoneal sites, and excision of enlarged nodes; routine lymphadenectomy/contralateral ovarian biopsy are generally discouraged. (saani2023clinicalchallengesin pages 2-3, margioulasiarkou2023therapeuticmanagementand pages 12-13, margioulasiarkou2023therapeuticmanagementand pages 4-5, margioulasiarkou2023therapeuticmanagementand pages 5-7) |
| Standard treatment | Standard care is fertility-sparing surgery when oncologically safe, usually unilateral salpingo-oophorectomy/oophorectomy with staging, followed by risk-adapted surveillance and/or platinum-based chemotherapy. BEP is the most used regimen; guideline summaries report 3 cycles after complete resection and 4 cycles if macroscopic residual disease, with bleomycin often omitted after cycle 3. Stage IA pure dysgerminoma and well-differentiated stage IA immature teratoma are often managed with surgery alone/surveillance. (saani2023clinicalchallengesin pages 5-6, saani2023clinicalchallengesin pages 3-5, margioulasiarkou2023therapeuticmanagementand pages 16-17) |
| Outcomes / survival stats | Most patients present with early-stage disease (60–70%). Stage I disease has ~90% long-term disease-free survival; BEP-based outcomes are reported as 82–100% for early-stage and ~75% for late-stage disease. In advanced MOGCT systematic-review data, neoadjuvant chemotherapy (NACT) response rate was ~95.8%; OS and DFS in comparator studies were broadly similar to primary debulking surgery (OS 87–100% vs 70–100%; DFS 87–100% vs 70–100%). (saani2023clinicalchallengesin pages 5-6, saani2023clinicalchallengesin pages 3-5, sakaguchimukaida2023systematicreviewof pages 1-2) |
| Key molecular alterations / biomarkers | Overall genomic burden is low with relatively stable copy-number profiles. Non-dysgerminomatous features include recurrent KRAS mutations and PIK3CA/AKT1 amplification in ovarian yolk sac tumors; chromosome 12p gain/i(12p) is present in most OvGCTs except many pure immature teratomas; KIT mutations/amplification are characteristic of dysgerminoma; TP53 alterations are largely linked to cisplatin resistance. Candidate circulating biomarkers include miR-371~373 and miR-302 clusters (e.g., miR-371a-3p). Diagnostic IHC markers include SALL4, OCT3/4, PLAP, NANOG, AFP, glypican-3, SOX2/SOX10. (travis2024adolescentandyoung pages 3-4, saani2023clinicalchallengesin pages 14-16, margioulasiarkou2023therapeuticmanagementand pages 12-13, saani2023clinicalchallengesin pages 9-10, travis2024adolescentandyoung pages 11-12, OpenTargets Search: ovarian germ cell tumor) |
| Key controversy: immature teratoma adjuvant chemotherapy | Major controversy is whether fully resected stage I ovarian immature teratoma—especially grade 2–3 or IC disease—needs adjuvant BEP versus surveillance. MaGIC 2024 supports surveillance after surgery for pediatric IT regardless of stage/grade and notes adult stage I evidence also supports surgery alone; NCCN/ESMO still generally recommend postoperative chemotherapy for most adults except FIGO IA grade 1. No randomized trial has shown DFS/OS benefit for adjuvant chemotherapy; lymph-node positivity is low (up to 8%), while lymphedema risk after lymphadenectomy can be up to 36%. Growing teratoma syndrome has reported incidence ~12–23% in some series. (pashankar2024consensusandcontroversy pages 4-6, pashankar2024consensusandcontroversy pages 6-7, pashankar2024consensusandcontroversy pages 7-8, margioulasiarkou2023therapeuticmanagementand pages 7-8, margioulasiarkou2023therapeuticmanagementand pages 16-17, saani2023clinicalchallengesin pages 6-8, margioulasiarkou2023therapeuticmanagementand media 71d74127) |
| Key ongoing clinical trials | **NCT02429687 (MOGCT-01):** randomized phase 3, newly diagnosed stage IIA–IVB MOGCT after surgery; paclitaxel-carboplatin (TC/PT) vs BEP; estimated enrollment ~129; primary endpoint PFS, with OS, response, and toxicity secondary; follow-up up to 5 years. **NCT03067181:** COG randomized phase 3 across pediatric/adult GCTs including stage I ovarian immature teratoma and stage I non-seminomatous malignant ovarian GCTs; estimated enrollment ~1,780; compares observation for low-risk disease and carboplatin- vs cisplatin-based bleomycin/etoposide regimens (CEb/PEb/BEC/BEP); endpoints include OS/EFS, ototoxicity, serum miRNA, AFP/HCG correlates, and long-term follow-up up to 10 years. (NCT02429687 chunk 1, NCT03067181 chunk 2, NCT03067181 chunk 1) |


*Table: This table condenses the most actionable facts for malignant ovarian non-dysgerminomatous germ cell tumors, including incidence, biomarkers, treatment, outcomes, molecular features, controversies, and active trials. It is useful as a rapid-reference summary for a disease knowledge base entry.*

---

## 1. Disease Information

### 1.1 What is the disease?
Malignant ovarian germ cell tumors (OvGCTs) arise from **primitive germ cells** and represent a rare subset of ovarian malignancies. They are often **large and rapidly progressive**, predominantly affecting adolescents and young adults. (saani2023clinicalchallengesin pages 2-3)

**Non‑dysgerminomatous malignant OvGCTs** correspond to non‑seminomatous histologies, especially **yolk sac tumor**, **embryonal carcinoma**, **choriocarcinoma**, **immature teratoma**, and **mixed germ cell tumor**. (margioulasiarkou2023therapeuticmanagementand pages 1-2, saani2023clinicalchallengesin pages 1-2)

### 1.2 Key identifiers (ontology/coding)
- **MONDO:** MONDO_0018171 (*malignant germ cell tumor of ovary*) (OpenTargets Search: ovarian germ cell tumor)
- **Other identifiers (OMIM/Orphanet/ICD‑10/ICD‑11/MeSH):** Not directly retrievable from the currently accessible evidence set and therefore not asserted.

### 1.3 Synonyms / alternative names
- Malignant ovarian germ cell tumor(s) (MOGCTs) (sakaguchimukaida2023systematicreviewof pages 1-2)
- Ovarian germ cell tumor (OvGCT) (travis2024adolescentandyoung pages 3-4)
- Ovarian non‑seminomatous/non‑dysgerminomatous germ cell tumor (conceptual grouping based on subtype list) (margioulasiarkou2023therapeuticmanagementand pages 1-2, saani2023clinicalchallengesin pages 1-2)

### 1.4 Evidence type
This report is derived from **aggregated disease‑level resources** (peer‑reviewed reviews/guideline syntheses and trial registry records), not from individual EHR case series extraction. (margioulasiarkou2023therapeuticmanagementand pages 1-2, saani2023clinicalchallengesin pages 5-6, NCT02429687 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors (current understanding)
- **Developmental origin:** OvGCTs are described as largely **originating in utero**, with incidence peaking in adolescence/young adulthood. (travis2024adolescentandyoung pages 3-4)
- **Genetic/molecular drivers:** OvGCTs show **low somatic mutation rates** and relatively stable copy number profiles overall, with subtype‑specific alterations (e.g., KRAS in yolk sac tumors) and characteristic chromosomal changes (12p gain in many post‑pubertal GCTs). (travis2024adolescentandyoung pages 3-4)

### 2.2 Risk factors
**Genetic / developmental risk context**
- **Gonadal dysgenesis / disorders of sex development (DSD):** Individuals with gonadal dysgenesis have substantially increased risk of OvGCT, with quoted **excess risk ranging 0–60% depending on syndrome**, and **prophylactic gonadectomy** is advised for high‑risk syndromes (examples listed: **Turner’s and Swyer**). (travis2024adolescentandyoung pages 3-4)

**Demographic / geographic context**
- Regional variation in the proportion of ovarian tumors that are OvGCTs is reported (North America ~2%, Europe ~1.3%, Central/South America ~3.9%, Asia ~4.2%). (travis2024adolescentandyoung pages 3-4)
- One review notes higher prevalence in women of Asian and African descent and large regional variation in proportion of ovarian tumors classified as GCTs. (saani2023clinicalchallengesin pages 1-2)

**Environmental / lifestyle risk factors**
- No specific, well‑supported environmental or lifestyle risk factors were identified in the retrieved sources.

### 2.3 Protective factors
No protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No explicit gene–environment interaction evidence was identified in the retrieved evidence.

---

## 3. Phenotypes

### 3.1 Common presenting phenotypes (with suggested HPO terms)
Clinical presentation is commonly dominated by symptoms of a rapidly enlarging pelvic mass.
- **Abdominal/pelvic pain** (HPO: **HP:0002027 Abdominal pain**) (saani2023clinicalchallengesin pages 2-3)
- **Palpable abdominal/pelvic mass** (HPO: **HP:0003270 Abdominal mass**; also consider **HP:0000023 Abdominal distension**) (saani2023clinicalchallengesin pages 2-3)

Age of onset is typically adolescence/young adulthood (HPO context: **HP:0003593 Infantile onset** not applicable; instead use onset annotations in metadata). OvGCTs are described as leading gynecologic malignancies in women <25 and incidence peaks in adolescence. (travis2024adolescentandyoung pages 3-4)

### 3.2 Laboratory abnormalities / biomarkers (with suggested HPO terms)
- **Elevated alpha‑fetoprotein (AFP)**—classically with yolk sac tumor; can be elevated in immature teratoma. (HPO: **HP:0031963 Increased circulating alpha-fetoprotein**) (saani2023clinicalchallengesin pages 2-3, pashankar2024consensusandcontroversy pages 2-3)
- **Elevated β‑hCG**—classically with choriocarcinoma; can be produced by embryonal carcinoma. (HPO: **HP:0031936 Elevated human chorionic gonadotropin**) (saani2023clinicalchallengesin pages 2-3, saani2023clinicalchallengesin pages 3-5)
- **Elevated LDH**—supportive for dysgerminoma but often included in work‑up panels. (HPO: **HP:0031965 Elevated lactate dehydrogenase**) (saani2023clinicalchallengesin pages 2-3, margioulasiarkou2023therapeuticmanagementand pages 12-13)

**Quantitative data (immature teratoma):** In a pediatric trial (INT‑0106) AFP was elevated in **34%** of children with pure ovarian immature teratoma (mean 32 ng/mL, range 13–60), versus **83%** with Heifetz lesions/microscopic yolk‑sac foci (mean 304 ng/mL, range 80–1045). (pashankar2024consensusandcontroversy pages 2-3)

### 3.3 Quality of life impact
The disease and its treatment can impact fertility and long‑term health. A 2024 JCO review emphasizes the need to de‑intensify therapy because late effects of cisplatin‑based therapy (e.g., ototoxicity, neurotoxicity, cardiovascular disease) have emerged as important survivorship issues in germ cell tumors. (travis2024adolescentandyoung pages 3-4)

---

## 4. Genetic / Molecular Information

### 4.1 Recurrently implicated genes (somatic; subtype‑dependent)
The retrieved 2023–2024 reviews describe the following patterns:
- **KRAS** recurrent mutations in ovarian yolk sac tumors (travis2024adolescentandyoung pages 3-4)
- **PIK3CA** and **AKT1** amplification in ovarian yolk sac tumors (travis2024adolescentandyoung pages 3-4)
- **KIT** mutation/amplification in dysgerminoma (included here for context/contrast) (travis2024adolescentandyoung pages 3-4)
- **TP53** alterations largely restricted to cisplatin‑resistant GCTs; MDM2 amplification linked to cisplatin resistance (travis2024adolescentandyoung pages 3-4)

Open Targets’ disease‑gene aggregation for “malignant germ cell tumor of ovary” lists evidence linking the disease to **KIT, KRAS, TP53, DICER1, CDKN2A, FANCM**, among others, with supporting PMIDs surfaced by the platform. (OpenTargets Search: ovarian germ cell tumor)

### 4.2 Chromosomal abnormalities / structural features
- **Gain of chromosome 12p / i(12p):** described as a near‑universal feature of post‑pubertal GCTs, present in most OvGCTs; pure mature/immature teratomas are notable exceptions. (travis2024adolescentandyoung pages 3-4)
- A 2023 review summarizes copy‑number changes and notes **12p gains essentially in all tumors except pure immature teratomas**, and reports additional focal deletions in yolk sac tumors. (saani2023clinicalchallengesin pages 9-10)

### 4.3 Epigenetic information
No disease‑specific epigenetic mechanisms were identified in the retrieved evidence.

### 4.4 Molecular profiling / emerging biomarkers
- **Circulating microRNAs:** miR‑371~373 and miR‑302 clusters are highlighted as promising serum biomarkers, with the **M371 test (miR‑371a‑3p)** specifically referenced as a promising circulating biomarker for malignant GCTs (utility in ovarian/pediatric GCTs still being defined). (travis2024adolescentandyoung pages 11-12, saani2023clinicalchallengesin pages 14-16)

---

## 5. Environmental Information
No robust environmental toxins, lifestyle exposures, or infectious triggers were identified in the retrieved evidence as causal or modifying factors for malignant ovarian non‑dysgerminomatous GCTs.

---

## 6. Mechanism / Pathophysiology

### 6.1 High‑level causal chain (current model)
1) **Developmental mis‑specification or persistence of primordial germ cells (PGCs)** (described as in‑utero origin and PGC biology) → 2) acquisition of **subtype‑specific genetic/copy‑number changes** (e.g., 12p gain in many tumors; KRAS in yolk sac tumors) → 3) emergence of malignant histologies with characteristic differentiation programs (e.g., endodermal differentiation in yolk sac tumors) → 4) clinically rapid growth presenting as pelvic/abdominal mass/pain and secretion of oncofetal markers (AFP, β‑hCG) that enable monitoring. (travis2024adolescentandyoung pages 3-4, saani2023clinicalchallengesin pages 2-3)

### 6.2 Molecular pathways and cellular processes
- **PI3K–PTEN–AKT** and **TSC–mTOR** pathways are highlighted in a 2023 review as relevant to follicle/oocyte survival and potentially to tumorigenesis; PTEN loss/hyperactive AKT may promote genomic instability and tumor growth programs. (saani2023clinicalchallengesin pages 9-10)
- **KIT signaling** is discussed as relevant to primordial germ cell biology and is altered in dysgerminoma (context for the broader OvGCT biology). (saani2023clinicalchallengesin pages 8-9, saani2023clinicalchallengesin pages 9-10)

**Suggested GO biological process terms (examples):**
- GO:0008283 **cell population proliferation**
- GO:0006915 **apoptotic process**
- GO:0007169 **transmembrane receptor protein tyrosine kinase signaling pathway** (KIT context)
- GO:0014068 **positive regulation of phosphatidylinositol 3-kinase signaling** (PI3K/AKT context)

### 6.3 Cell types (suggested CL terms)
- **Primordial germ cell / germ cell** (Cell Ontology: e.g., CL:0000670 **primordial germ cell**; CL:0000016 **male germ cell** is not appropriate for ovary; use germ‑cell generic terms)
- **Ovarian somatic support cells** are relevant for microenvironment but not directly evidenced in retrieved texts.

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- **Primary organ:** ovary (UBERON: **UBERON:0000992 ovary**)
- Tumors are described as usually unilateral in MOGCT systematic review context. (sakaguchimukaida2023systematicreviewof pages 1-2)

### 7.2 Metastatic/secondary sites (reported patterns)
Recurrences commonly involve the **peritoneum** and **retroperitoneal lymph nodes** within the first two years. (saani2023clinicalchallengesin pages 3-5)

**Suggested UBERON terms:**
- UBERON:0002358 **peritoneum**
- UBERON:0002416 **retroperitoneum**

---

## 8. Temporal Development

### 8.1 Onset
- Peak incidence in adolescence/young adulthood; OvGCT incidence in females aged 15–19 is reported as **~1.2 per 100,000**, and OvGCTs are the leading gynecologic malignancies in women <25. (travis2024adolescentandyoung pages 3-4)

### 8.2 Progression/course
- Tumors are described as rapidly progressive and large at presentation. (saani2023clinicalchallengesin pages 2-3)
- Relapse timing: recurrences commonly within the first **two years**. (saani2023clinicalchallengesin pages 3-5)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- **Fraction of ovarian cancers:** ~**2–5%** (saani2023clinicalchallengesin pages 1-2)
- **Incidence estimates:** ~**4 per 100,000/year** reported in one review (saani2023clinicalchallengesin pages 1-2); **2.6 per 100,000 girls/year** in an adolescent guideline review context (margioulasiarkou2023therapeuticmanagementand pages 1-2); **1.2 per 100,000** in females aged 15–19 (travis2024adolescentandyoung pages 3-4)
- **Regional proportion among ovarian tumors:** North America 2.0%, Europe 1.3%, Central/South America 3.9%, Asia 4.2%. (travis2024adolescentandyoung pages 3-4)

### 9.2 Inheritance pattern
No Mendelian inheritance pattern is established for malignant ovarian non‑dysgerminomatous GCTs in the retrieved evidence. The 2024 JCO review discusses substantial heritability in testicular GCT and polygenic architecture, suggesting common variant contributions may exist, but this is not a direct inheritance model for ovarian disease. (travis2024adolescentandyoung pages 3-4)

---

## 10. Diagnostics

### 10.1 Clinical tests and biomarkers
**Serum markers (core):** β‑hCG, AFP, LDH (often CA125 also) are recommended in suspicious ovarian masses, with serial measurement post‑op and before chemo cycles. (margioulasiarkou2023therapeuticmanagementand pages 12-13, saani2023clinicalchallengesin pages 2-3)

**Imaging:** pelvic ultrasound first; then abdomino‑pelvic CT or MRI and chest imaging (X‑ray or low‑dose CT). PET is reserved for selected cases. (margioulasiarkou2023therapeuticmanagementand pages 12-13, margioulasiarkou2023therapeuticmanagementand pages 4-5)

**Pathology/IHC and cytogenetics:** immunohistochemistry panels (SALL4, OCT3/4, PLAP, NANOG, AFP, glypican‑3, SOX2/SOX10, etc.) and **FISH for isochromosome 12p** in difficult cases are recommended. (margioulasiarkou2023therapeuticmanagementand pages 12-13)

### 10.2 Staging and surgical staging elements
FIGO staging is used; staging surgery for macroscopic stage I includes omentectomy/omental biopsy and peritoneal washings/biopsies, with selective node excision rather than routine lymphadenectomy. (saani2023clinicalchallengesin pages 2-3, margioulasiarkou2023therapeuticmanagementand pages 5-7)

### 10.3 Differential diagnosis
Not systematically detailed in the retrieved sources; diagnostic IHC/FISH recommendations imply the main differential includes other non‑epithelial ovarian tumors and mixed histologies. (margioulasiarkou2023therapeuticmanagementand pages 12-13)

---

## 11. Outcome / Prognosis

### 11.1 Survival and response
- Most patients present with early-stage disease (reported **60–70%** early stage). (saani2023clinicalchallengesin pages 5-6)
- Stage I outcomes are excellent with **~90% long-term disease-free survival** in reported series. (saani2023clinicalchallengesin pages 5-6)
- Reported survival with BEP is described as **82–100%** for early stage and **~75%** for late stage in one review. (saani2023clinicalchallengesin pages 3-5)

### 11.2 Prognostic factors
Guideline synthesis lists key adverse prognostic factors including **stage > I**, **incomplete resection**, and **yolk sac histology**; premenarche age at diagnosis is also noted as unfavorable. (margioulasiarkou2023therapeuticmanagementand pages 13-14)

---

## 12. Treatment

### 12.1 Standard of care (real-world implementation)
**Surgery (fertility-sparing when oncologically safe)**
- Unilateral salpingo‑oophorectomy/oophorectomy with staging is emphasized; contralateral ovarian biopsy is discouraged when grossly normal. (margioulasiarkou2023therapeuticmanagementand pages 16-17)

**Chemotherapy**
- **BEP (bleomycin, etoposide, cisplatin)** is the most widely used regimen; typical guidance is **3 cycles** after complete resection and **4 cycles** if macroscopic residual disease, with bleomycin often omitted after cycle 3 to reduce pulmonary toxicity. (margioulasiarkou2023therapeuticmanagementand pages 16-17)

**Surveillance**
- Active surveillance with serial markers and imaging is recommended for selected early-stage patients with normalizing markers; follow-up can extend up to **10 years** in some guidance. (margioulasiarkou2023therapeuticmanagementand pages 16-17)

**MAXO suggestions (examples):**
- MAXO:0000004 **surgical procedure** (fertility-sparing resection)
- MAXO:0000747 **chemotherapy** (BEP regimen)
- MAXO:0000058 **active surveillance**

### 12.2 Neoadjuvant chemotherapy (NACT)
A 2023 systematic review/meta-analysis of retrospective series reported that in advanced MOGCT:
- NACT was used in ~40% of advanced cases and achieved **~95.8% response rate**.
- Comparator studies showed broadly similar OS and DFS ranges vs primary debulking surgery (OS 87–100% vs 70–100%; DFS 87–100% vs 70–100%), though evidence quality was limited and bias concerns were noted. (sakaguchimukaida2023systematicreviewof pages 1-2)

### 12.3 Controversies: immature teratoma adjuvant chemotherapy
A 2024 MaGIC consortium perspective emphasizes that many retrospective/consortium studies show **no DFS/OS benefit** from adjuvant chemotherapy in fully resected stage I ovarian immature teratoma, and that no randomized trials exist; MaGIC supports surveillance after surgery for pediatric IT regardless of stage/grade and supports surgery alone for adult stage I in the evidence base. (pashankar2024consensusandcontroversy pages 4-6)

A guideline comparison table image illustrates variation by stage/grade among groups (surveillance vs chemotherapy thresholds). (margioulasiarkou2023therapeuticmanagementand media 71d74127)

### 12.4 Experimental/ongoing trials (ClinicalTrials.gov)
- **NCT02429687 (MOGCT-01):** Randomized Phase 3; post‑surgery stage IIA–IVB MOGCT; **paclitaxel+carboplatin** vs **BEP**; primary endpoint PFS (follow-up up to 5 years). URL: https://clinicaltrials.gov/study/NCT02429687 (NCT02429687 chunk 1)
- **NCT03067181:** COG randomized Phase 3 across pediatric/adult GCTs including stage I ovarian immature teratoma and stage I non‑seminomatous malignant ovarian GCTs; includes **active surveillance** and compares **carboplatin‑ vs cisplatin‑based** regimens; endpoints include OS/EFS and ototoxicity, plus biomarker correlates (tumor markers and serum miRNA). URL: https://clinicaltrials.gov/study/NCT03067181 (NCT03067181 chunk 1)

---

## 13. Prevention
- **Primary prevention:** No specific modifiable environmental risk factors were identified in retrieved evidence.
- **Secondary prevention:** No population screening strategies are established; early diagnosis relies on evaluation of symptoms/mass and tumor markers/imaging. (margioulasiarkou2023therapeuticmanagementand pages 12-13)
- **Risk‑reduction in high‑risk syndromes:** prophylactic gonadectomy is recommended in high‑risk gonadal dysgenesis syndromes. (travis2024adolescentandyoung pages 3-4)

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary analogs or cross‑species transmission information were identified in the retrieved evidence.

---

## 15. Model Organisms
No specific model organism systems (mouse/zebrafish/cell lines/organoids) were described in the retrieved evidence set.

---

# Recent developments (2023–2024 emphasis)
1. **Consensus/controversy evolution for immature teratoma:** 2024 MaGIC perspective advocating surveillance in many settings vs persistent guideline recommendations for adjuvant chemotherapy in adults, highlighting a key practice gap and need for trials. (pashankar2024consensusandcontroversy pages 4-6, pashankar2024consensusandcontroversy pages 6-7)
2. **Treatment optimization / de‑intensification and survivorship:** 2024 JCO review emphasizes late effects of cisplatin and the need for innovations and trial designs that span ages/sexes, incorporating molecular risk stratification. (travis2024adolescentandyoung pages 3-4)
3. **NACT evidence consolidation:** 2023 systematic review/meta‑analysis provides quantitative synthesis (response ~95.8%, similar survival ranges vs PDS in limited comparative data), motivating prospective evaluation. (sakaguchimukaida2023systematicreviewof pages 1-2)
4. **Biomarker pipeline:** circulating miRNAs (miR‑371~373/miR‑302; M371) are highlighted as promising biomarkers, with clinical utility in ovarian/pediatric settings still being defined. (travis2024adolescentandyoung pages 11-12)

---

# Authoritative-source abstract quotations (direct)
- **Guideline review (adolescents):** “All guidelines recommend a thorough diagnostic work-up, consisting of both imaging tests and serum tumour marker measurement, as well as the use of immunohistochemical methods to confirm the diagnosis…” (Diagnostics 2023; URL: https://doi.org/10.3390/diagnostics13061080) (margioulasiarkou2023therapeuticmanagementand pages 1-2)
- **Clinical challenges review:** “GCTs represent 2–5% of ovarian cancers…” (IJERPH 2023; URL: https://doi.org/10.3390/ijerph20126089) (saani2023clinicalchallengesin pages 1-2)
- **NACT systematic review:** “NACT was used in approximately 40% of advanced MOGCT cases, with a response rate of 95.8%.” (Cancers 2023; URL: https://doi.org/10.3390/cancers15184470) (sakaguchimukaida2023systematicreviewof pages 1-2)
- **AYA GCT review:** “OvGCTs … are the leading gynecologic malignancies in women younger than 25 years.” (JCO 2024; URL: https://doi.org/10.1200/jco.23.01099) (travis2024adolescentandyoung pages 3-4)

---

# Notes on evidence gaps
Despite targeted retrieval, the current tool‑accessible corpus did not provide:
- ICD‑10/ICD‑11, MeSH, Orphanet, OMIM mappings specific to “malignant non‑dysgerminomatous ovarian germ cell tumor.”
- Robust, validated environmental/lifestyle protective factors or gene–environment interaction evidence.
- Specific animal models or standardized QoL instrument outcomes for this tumor type.

These items should be filled by direct queries to ontology services (MONDO/MeSH/Orphanet/ICD browsers) and specialized resources (SEER/GBD, GeneReviews/ClinGen/ClinVar, model organism databases) in a follow‑on extraction step.


References

1. (margioulasiarkou2023therapeuticmanagementand pages 1-2): Chrysoula Margioula-Siarkou, Stamatios Petousis, Georgia Margioula-Siarkou, George Mavromatidis, Fotios Chatzinikolaou, Emmanouel Hatzipantelis, Frédéric Guyon, and Konstantinos Dinas. Therapeutic management and prognostic factors for ovarian malignant tumours in adolescents: a comprehensive review of current guidelines. Diagnostics, 13:1080, Mar 2023. URL: https://doi.org/10.3390/diagnostics13061080, doi:10.3390/diagnostics13061080. This article has 20 citations.

2. (saani2023clinicalchallengesin pages 1-2): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 79 citations.

3. (OpenTargets Search: ovarian germ cell tumor): Open Targets Query (ovarian germ cell tumor, 26 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (sakaguchimukaida2023systematicreviewof pages 1-2): Hitomi Sakaguchi-Mukaida, Shinya Matsuzaki, Yutaka Ueda, Satoko Matsuzaki, Mamoru Kakuda, Misooja Lee, Satoki Deguchi, Mina Sakata, Michihide Maeda, Reisa Kakubari, Tsuyoshi Hisa, Seiji Mabuchi, and Shoji Kamiura. Systematic review of the survival outcomes of neoadjuvant chemotherapy in women with malignant ovarian germ cell tumors. Cancers, 15:4470, Sep 2023. URL: https://doi.org/10.3390/cancers15184470, doi:10.3390/cancers15184470. This article has 4 citations.

5. (saani2023clinicalchallengesin pages 2-3): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 79 citations.

6. (margioulasiarkou2023therapeuticmanagementand pages 12-13): Chrysoula Margioula-Siarkou, Stamatios Petousis, Georgia Margioula-Siarkou, George Mavromatidis, Fotios Chatzinikolaou, Emmanouel Hatzipantelis, Frédéric Guyon, and Konstantinos Dinas. Therapeutic management and prognostic factors for ovarian malignant tumours in adolescents: a comprehensive review of current guidelines. Diagnostics, 13:1080, Mar 2023. URL: https://doi.org/10.3390/diagnostics13061080, doi:10.3390/diagnostics13061080. This article has 20 citations.

7. (saani2023clinicalchallengesin pages 5-6): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 79 citations.

8. (margioulasiarkou2023therapeuticmanagementand pages 16-17): Chrysoula Margioula-Siarkou, Stamatios Petousis, Georgia Margioula-Siarkou, George Mavromatidis, Fotios Chatzinikolaou, Emmanouel Hatzipantelis, Frédéric Guyon, and Konstantinos Dinas. Therapeutic management and prognostic factors for ovarian malignant tumours in adolescents: a comprehensive review of current guidelines. Diagnostics, 13:1080, Mar 2023. URL: https://doi.org/10.3390/diagnostics13061080, doi:10.3390/diagnostics13061080. This article has 20 citations.

9. (travis2024adolescentandyoung pages 3-4): Lois B. Travis, Darren R. Feldman, Chunkit Fung, Jenny N. Poynter, Michelle Lockley, and A. Lindsay Frazier. Adolescent and young adult germ cell tumors: epidemiology, genomics, treatment, and survivorship. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, pages JCO2301099, Oct 2024. URL: https://doi.org/10.1200/jco.23.01099, doi:10.1200/jco.23.01099. This article has 32 citations.

10. (pashankar2024consensusandcontroversy pages 2-3): Farzana Pashankar, Matthew J. Murray, Joanna Gell, Nicola MacDonald, Jonathan Shamash, Deborah F. Billmire, Lindsay Klosterkemper, Thomas Olson, Michelle S. Hirsch, Michelle Lockley, Sara Stoneham, and A. Lindsay Frazier. Consensus and controversy in the management of paediatric and adult patients with ovarian immature teratoma: the malignant germ cell international consortium perspective. eClinicalMedicine, 69:102453, Mar 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102453, doi:10.1016/j.eclinm.2024.102453. This article has 19 citations and is from a peer-reviewed journal.

11. (saani2023clinicalchallengesin pages 3-5): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 79 citations.

12. (margioulasiarkou2023therapeuticmanagementand pages 4-5): Chrysoula Margioula-Siarkou, Stamatios Petousis, Georgia Margioula-Siarkou, George Mavromatidis, Fotios Chatzinikolaou, Emmanouel Hatzipantelis, Frédéric Guyon, and Konstantinos Dinas. Therapeutic management and prognostic factors for ovarian malignant tumours in adolescents: a comprehensive review of current guidelines. Diagnostics, 13:1080, Mar 2023. URL: https://doi.org/10.3390/diagnostics13061080, doi:10.3390/diagnostics13061080. This article has 20 citations.

13. (margioulasiarkou2023therapeuticmanagementand pages 5-7): Chrysoula Margioula-Siarkou, Stamatios Petousis, Georgia Margioula-Siarkou, George Mavromatidis, Fotios Chatzinikolaou, Emmanouel Hatzipantelis, Frédéric Guyon, and Konstantinos Dinas. Therapeutic management and prognostic factors for ovarian malignant tumours in adolescents: a comprehensive review of current guidelines. Diagnostics, 13:1080, Mar 2023. URL: https://doi.org/10.3390/diagnostics13061080, doi:10.3390/diagnostics13061080. This article has 20 citations.

14. (saani2023clinicalchallengesin pages 14-16): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 79 citations.

15. (saani2023clinicalchallengesin pages 9-10): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 79 citations.

16. (travis2024adolescentandyoung pages 11-12): Lois B. Travis, Darren R. Feldman, Chunkit Fung, Jenny N. Poynter, Michelle Lockley, and A. Lindsay Frazier. Adolescent and young adult germ cell tumors: epidemiology, genomics, treatment, and survivorship. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, pages JCO2301099, Oct 2024. URL: https://doi.org/10.1200/jco.23.01099, doi:10.1200/jco.23.01099. This article has 32 citations.

17. (pashankar2024consensusandcontroversy pages 4-6): Farzana Pashankar, Matthew J. Murray, Joanna Gell, Nicola MacDonald, Jonathan Shamash, Deborah F. Billmire, Lindsay Klosterkemper, Thomas Olson, Michelle S. Hirsch, Michelle Lockley, Sara Stoneham, and A. Lindsay Frazier. Consensus and controversy in the management of paediatric and adult patients with ovarian immature teratoma: the malignant germ cell international consortium perspective. eClinicalMedicine, 69:102453, Mar 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102453, doi:10.1016/j.eclinm.2024.102453. This article has 19 citations and is from a peer-reviewed journal.

18. (pashankar2024consensusandcontroversy pages 6-7): Farzana Pashankar, Matthew J. Murray, Joanna Gell, Nicola MacDonald, Jonathan Shamash, Deborah F. Billmire, Lindsay Klosterkemper, Thomas Olson, Michelle S. Hirsch, Michelle Lockley, Sara Stoneham, and A. Lindsay Frazier. Consensus and controversy in the management of paediatric and adult patients with ovarian immature teratoma: the malignant germ cell international consortium perspective. eClinicalMedicine, 69:102453, Mar 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102453, doi:10.1016/j.eclinm.2024.102453. This article has 19 citations and is from a peer-reviewed journal.

19. (pashankar2024consensusandcontroversy pages 7-8): Farzana Pashankar, Matthew J. Murray, Joanna Gell, Nicola MacDonald, Jonathan Shamash, Deborah F. Billmire, Lindsay Klosterkemper, Thomas Olson, Michelle S. Hirsch, Michelle Lockley, Sara Stoneham, and A. Lindsay Frazier. Consensus and controversy in the management of paediatric and adult patients with ovarian immature teratoma: the malignant germ cell international consortium perspective. eClinicalMedicine, 69:102453, Mar 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102453, doi:10.1016/j.eclinm.2024.102453. This article has 19 citations and is from a peer-reviewed journal.

20. (margioulasiarkou2023therapeuticmanagementand pages 7-8): Chrysoula Margioula-Siarkou, Stamatios Petousis, Georgia Margioula-Siarkou, George Mavromatidis, Fotios Chatzinikolaou, Emmanouel Hatzipantelis, Frédéric Guyon, and Konstantinos Dinas. Therapeutic management and prognostic factors for ovarian malignant tumours in adolescents: a comprehensive review of current guidelines. Diagnostics, 13:1080, Mar 2023. URL: https://doi.org/10.3390/diagnostics13061080, doi:10.3390/diagnostics13061080. This article has 20 citations.

21. (saani2023clinicalchallengesin pages 6-8): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 79 citations.

22. (margioulasiarkou2023therapeuticmanagementand media 71d74127): Chrysoula Margioula-Siarkou, Stamatios Petousis, Georgia Margioula-Siarkou, George Mavromatidis, Fotios Chatzinikolaou, Emmanouel Hatzipantelis, Frédéric Guyon, and Konstantinos Dinas. Therapeutic management and prognostic factors for ovarian malignant tumours in adolescents: a comprehensive review of current guidelines. Diagnostics, 13:1080, Mar 2023. URL: https://doi.org/10.3390/diagnostics13061080, doi:10.3390/diagnostics13061080. This article has 20 citations.

23. (NCT02429687 chunk 1): Beihua Kong. TC or BEP in Treating Patients With Malignant Ovarian Germ Cell Tumors. Beihua Kong. 2015. ClinicalTrials.gov Identifier: NCT02429687

24. (NCT03067181 chunk 2):  Active Surveillance, Bleomycin, Etoposide, Carboplatin or Cisplatin in Treating Pediatric and Adult Patients With Germ Cell Tumors. Children's Oncology Group. 2017. ClinicalTrials.gov Identifier: NCT03067181

25. (NCT03067181 chunk 1):  Active Surveillance, Bleomycin, Etoposide, Carboplatin or Cisplatin in Treating Pediatric and Adult Patients With Germ Cell Tumors. Children's Oncology Group. 2017. ClinicalTrials.gov Identifier: NCT03067181

26. (saani2023clinicalchallengesin pages 8-9): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 79 citations.

27. (margioulasiarkou2023therapeuticmanagementand pages 13-14): Chrysoula Margioula-Siarkou, Stamatios Petousis, Georgia Margioula-Siarkou, George Mavromatidis, Fotios Chatzinikolaou, Emmanouel Hatzipantelis, Frédéric Guyon, and Konstantinos Dinas. Therapeutic management and prognostic factors for ovarian malignant tumours in adolescents: a comprehensive review of current guidelines. Diagnostics, 13:1080, Mar 2023. URL: https://doi.org/10.3390/diagnostics13061080, doi:10.3390/diagnostics13061080. This article has 20 citations.