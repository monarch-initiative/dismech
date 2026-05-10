---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T23:47:14.513347'
end_time: '2026-05-10T00:00:41.805825'
duration_seconds: 807.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Metastatic Colorectal Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Metastatic Colorectal Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Colorectal Cancer** covering all of the
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
- **Disease Name:** Metastatic Colorectal Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Colorectal Cancer** covering all of the
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


# Metastatic Colorectal Cancer (mCRC): Disease Characteristics Research Report (2023–2024 prioritized)

## Target Disease
- **Disease name:** Metastatic colorectal cancer (mCRC)
- **Category:** Malignant neoplasm of the colon/rectum with distant metastasis (advanced solid tumor)
- **Ontology/IDs (available in retrieved evidence):**
  - **MONDO (colorectal cancer):** **MONDO_0005575** (OpenTargets disease list) (OpenTargets Search: metastatic colorectal cancer)
  - **EFO (metastatic colorectal cancer):** **EFO_1001480** (OpenTargets disease list) (OpenTargets Search: metastatic colorectal cancer)
- **Common synonyms:** metastatic colon cancer; metastatic rectal cancer; stage IV colorectal cancer; disseminated colorectal cancer (usage consistent with NCCN and real‑world studies) (garciacarbonero2024realworldstudyon pages 1-2, benson2024coloncancerversion pages 2-3)
- **Other identifiers requested (ICD-10/ICD-11, MeSH, OMIM, Orphanet):** not retrieved from the tool-accessible sources in this run; should be added from ICD/MeSH browsers and NCI Thesaurus during curation.
- **Evidence source types represented here:** clinical guidelines (NCCN), interventional clinical trials, registry/real‑world cohort studies (SEER, hospital cohorts), and biomarker-focused reviews (benson2024coloncancerversion pages 2-3, cutsem2023anchorcrcresults pages 1-2, desai2024divarasibpluscetuximab pages 1-2, nakamura2024ctdnabasedmolecularresidual pages 1-2, jeriyabar2024survivalanalysisof pages 1-2).

## 1. Disease Information (overview and definitions)
Metastatic colorectal cancer (mCRC) refers to colorectal carcinoma that has spread beyond the primary colon/rectal site to distant organs (stage IV disease in TNM/AJCC frameworks). NCCN Colon Cancer v3.2024 frames management of “disseminated metastatic CRC” as dependent on therapy goals, prior therapy, tumor mutational profile, and toxicity profiles, underscoring that mCRC is both a systemic disease and a biomarker-stratified therapeutic entity in contemporary care (benson2024coloncancerversion pages 2-3).

A key current concept is that **mCRC is not a single disease**, but rather a collection of molecularly defined subgroups (e.g., MSI‑H/dMMR, BRAF V600E, KRAS G12C, HER2‑amplified) that map to distinct, actionable treatment paths in guidelines and in clinical practice algorithms (benson2024coloncancerversion pages 2-3, benson2024coloncancerversion pages 15-16, benson2024coloncancerversion media afa7e635).

## 2. Etiology (causal factors, risk/protective factors, GxE)
**Direct etiologic and exposure‑based risk/protective factor evidence was not retrieved in this run** (e.g., obesity, diet, alcohol, smoking, IBD, aspirin, microbiome). This section should be supplemented from large epidemiologic resources and preventive guidelines (USPSTF, WHO, GBD), as requested in the template.

**Genetic contributions relevant to CRC (and thus to mCRC development):** A precision medicine review notes that **germline pathogenic variants occur in ~6–10% of CRC patients**, with Lynch syndrome genes (MLH1/MSH2/MSH6/PMS2) most common; NCCN recommends genetic testing when personal/family history suggests hereditary risk (underwood2024precisionmedicinefor pages 2-4).

## 3. Phenotypes (clinical presentation, QoL; HPO mapping)
### 3.1 Key phenotypic concepts in mCRC
The clinically dominant phenotype is **distant organ metastasis**, most commonly to the liver and lung, with rarer sites (brain, bone) contributing to morbidity and worse survival (jeriyabar2024survivalanalysisof pages 4-6, jeriyabar2024survivalanalysisclinical pages 1-2).

### 3.2 Metastatic patterns and frequencies (SEER)
A SEER analysis of 23,278 patients with metastatic CRC (2010–2020) found that **93.32% had a solitary metastatic site**; **liver-only metastasis was ~70%** (70.06% early-onset; 69.97% average-onset), while lung-only metastasis was ~17–19% and brain-only metastasis ~0.56–1.03% (jeriyabar2024survivalanalysisof pages 4-6). A separate SEER analysis (2010–2021) reported **brain metastasis at diagnosis in 0.92% (228/24,703)** of mCRC patients (jeriyabar2024survivalanalysisclinical pages 1-2).

### 3.3 Survival-linked phenotype severity (brain metastasis)
Patients with brain metastases at diagnosis had **median overall survival 6 months vs 21 months** in those without brain metastasis in the SEER cohort (jeriyabar2024survivalanalysisclinical pages 1-2).

### 3.4 Suggested HPO terms (examples)
(These are suggested mappings for knowledge-base structuring; specific term IDs should be verified against HPO.)
- **Hepatic metastases:** “Metastatic neoplasm of the liver” (HPO mapping candidate) (jeriyabar2024survivalanalysisof pages 4-6)
- **Pulmonary metastases:** “Pulmonary metastases” (candidate) (jeriyabar2024survivalanalysisof pages 4-6)
- **Brain metastases:** “Brain metastasis” (candidate) (jeriyabar2024survivalanalysisclinical pages 1-2)
- **Elevated carcinoembryonic antigen (CEA):** “Increased circulating carcinoembryonic antigen level” (candidate; discussed as prognostic in SEER modeling and ctDNA comparisons) (ren2024survivaloutcomeand pages 6-8, parikh2024minimalresidualdisease pages 1-2)

Quality-of-life (QoL) measurement details were limited in retrieved evidence; however, ANCHOR CRC reported patient-reported symptom improvement ≥30% across cycles using Patient Global Impression of Changes in BRAF V600E mCRC treated with targeted triplet therapy (cutsem2023anchorcrcresults pages 1-2).

## 4. Genetic / Molecular Information (drivers, variants, biomarkers)
### 4.1 Core molecular profiling recommended in mCRC (NCCN v3.2024)
NCCN Colon Cancer v3.2024 recommends **baseline molecular testing** in metastatic CRC that explicitly includes **KRAS/NRAS**, **BRAF**, **HER2 amplification**, and **MSI/MMR status** (if not previously done), and it prefers **NGS panels** because they also detect **rare actionable alterations** such as **NTRK** and **RET** fusions; testing may use tissue or blood (liquid) biopsy (benson2024coloncancerversion pages 2-3).

### 4.2 Key somatic drivers and actionable alterations (with prevalence where available)
- **RAS mutations**: ~50–55% of CRC (KRAS ~50%, NRAS ~4%, HRAS <1%); KRAS G12C ~3–4% of CRC (ashouri2024exploringpredictiveand pages 2-5).
- **BRAF V600E**: ~8–12% (review estimate) and often described as ~10–15% of mCRC with poor prognosis (underwood2024precisionmedicinefor pages 2-4, cutsem2023anchorcrcresults pages 1-2).
- **HER2 amplification/overexpression**: ~2–6% in mCRC; NCCN recommends universal testing for mCRC in a 2024 biomarker review summary (ashouri2024exploringpredictiveand pages 6-8).
- **NTRK fusions**: ~0.7% (underwood2024precisionmedicinefor pages 2-4).
- **RET fusions**: ~0.2% (underwood2024precisionmedicinefor pages 2-4).
- **MSI-H/dMMR**: stage IV prevalence ~4% in a 2024 biomarker review summary; Spanish real-world cohort observed 6% MMR-deficient among tested mCRC (ashouri2024exploringpredictiveand pages 8-9, garciacarbonero2024realworldstudyon pages 1-2).

### 4.3 Biomarker definitions and testing criteria (examples)
- **HER2 testing criteria:** IHC 3+ indicates overexpression; IHC 2+ is equivocal and should trigger FISH; **FISH ratio ≥2** confirms amplification (ashouri2024exploringpredictiveand pages 6-8, ashouri2024exploringpredictiveand pages 8-9).

### 4.4 OpenTargets disease–target associations (useful for knowledge graphs)
OpenTargets lists high-scoring associations for metastatic colorectal cancer including VEGF pathway targets (e.g., KDR/FLT1/FLT4/TEK) and BRAF/RET (OpenTargets Search: metastatic colorectal cancer). These associations are not treatment recommendations per se, but can support structured knowledge-base linking of mCRC to canonical therapeutic targets.

## 5. Environmental Information
No CTD/TOXNET/WHO/CDC exposure-specific evidence was retrieved in this run; this section remains incomplete.

## 6. Mechanism / Pathophysiology
### 6.1 Key pathway-level mechanisms directly supported by retrieved evidence
- **EGFR–RAS–MAPK pathway dependence and resistance:** RAS mutations drive constitutive downstream signaling and **render EGFR antibodies ineffective**; NCCN guidance states tumors with KRAS/NRAS mutations should not receive cetuximab or panitumumab (benson2024coloncancerversion pages 2-3, ashouri2024exploringpredictiveand pages 2-5). In KRAS G12C tumors, adaptive feedback through EGFR is a major resistance mechanism to KRAS G12C inhibitors, motivating dual KRAS G12C/EGFR blockade (desai2024divarasibpluscetuximab pages 1-2).
- **BRAF V600E feedback activation via EGFR:** BRAF inhibitor monotherapy is ineffective in BRAF V600E mCRC because BRAF blockade induces feedback activation; combining **BRAF inhibition + EGFR blockade** is the mechanistic basis for BEACON and related regimens (cutsem2023anchorcrcresults pages 1-2, cotan2024prognosticandpredictive pages 10-11).

### 6.2 Immune biology: MSI-H/dMMR as an immunotherapy-responsive state
dMMR/MSI-H tumors show strong sensitivity to immune checkpoint inhibition, establishing MSI/MMR as a mechanistic and predictive biomarker for therapy selection (garciacarbonero2024realworldstudyon pages 1-2, ashouri2024exploringpredictiveand pages 8-9).

### 6.3 Suggested GO biological process terms (candidates)
(IDs should be verified during ontology curation.)
- EGFR signaling pathway; MAPK cascade; negative regulation of EGFR signaling (adaptive feedback); DNA mismatch repair; adaptive immune response; T cell activation.

### 6.4 Suggested Cell Ontology (CL) cell types (candidates)
- Tumor-infiltrating T lymphocytes (for ICI mechanisms); colorectal epithelial tumor cells; cancer-associated fibroblasts (not directly evidenced here; include only after adding mechanistic primary sources).

## 7. Anatomical Structures Affected (UBERON mapping candidates)
Based on SEER distributions and mCRC clinical phenotype:
- **Primary sites:** colon (UBERON: colon), rectum (UBERON: rectum) (implicit in all mCRC sources).
- **Most common metastatic sites:** liver (UBERON: liver), lung (UBERON: lung) (jeriyabar2024survivalanalysisof pages 4-6).
- **Less common but high-impact metastatic sites:** brain (UBERON: brain) (jeriyabar2024survivalanalysisclinical pages 1-2); bone metastases discussed as prognostic in SEER hazard models (ren2024survivaloutcomeand pages 5-6).

## 8. Temporal Development (onset, progression)
### 8.1 Age distribution and “early-onset” metastatic CRC
In SEER (2010–2020), **17.79%** of metastatic CRC cases were classified as **early-onset (<50 years)**, and early-onset cases had improved median OS compared with average-onset cases (30 vs 18 months) (jeriyabar2024survivalanalysisof pages 1-2).

### 8.2 Molecular residual disease (MRD) as a temporal progression marker
ctDNA-based MRD can precede radiologic recurrence. In CIRCULATE-Japan GALAXY, ctDNA positivity preceded radiologic recurrence by a **median 5.9 months** (nakamura2024ctdnabasedmolecularresidual pages 1-2).

## 9. Inheritance and Population (epidemiology)
### 9.1 Survival statistics (SEER)
- **Median overall survival (stage IV mCRC, age-stratified):** 30 months (early-onset) vs 18 months (average-onset) in a SEER analysis (2010–2020) (jeriyabar2024survivalanalysisof pages 1-2).
- **Brain metastasis subgroup:** median OS 6 months vs 21 months without brain metastasis (SEER 2010–2021) (jeriyabar2024survivalanalysisclinical pages 1-2).

### 9.2 Metastatic site prevalence
- Liver-only metastasis ~70%; lung-only ~16.76% (early-onset) vs 19.33% (average-onset); brain-only 0.56% vs 1.03% in the SEER 2010–2020 metastatic CRC cohort (jeriyabar2024survivalanalysisof pages 4-6).

### 9.3 Germline contribution
A precision medicine review reports germline mutations in ~6–10% of CRC patients (Lynch genes most common), relevant for family risk and cascade testing (underwood2024precisionmedicinefor pages 2-4).

## 10. Diagnostics
### 10.1 Guideline-positioned molecular diagnostics (NCCN v3.2024)
NCCN recommends baseline metastatic molecular profiling including **KRAS/NRAS, BRAF, HER2 amplification, and MSI/MMR**, with preference for **NGS** panels to capture rare fusions (e.g., **NTRK, RET**) and to support biomarker-directed therapy selection; testing may be tissue- or blood-based (benson2024coloncancerversion pages 2-3).

### 10.2 Liquid biopsy / ctDNA (recent developments and real-world implementation)
ctDNA is increasingly implemented for MRD/risk stratification and surveillance, but evidence shows mixed clinical utility in routine practice.

Key recent quantitative results:
- **Oligometastatic/metastatic CRC after curative-intent procedures:** plasma-only multiomic MRD assay: postprocedure ctDNA at 3 weeks was associated with shorter RFS (**HR 5.27**) and OS (**HR 12.83**) (Clinical Cancer Research, May 2024) (parikh2024minimalresidualdisease pages 1-2).
- **Large prospective observational evidence (CIRCULATE-Japan GALAXY, Nature Medicine Sep 2024):** MRD positivity associated with inferior DFS (**HR 11.99**) and OS (**HR 9.68**); ctDNA positivity preceded radiologic recurrence by median **5.9 months**; ctDNA-negative had very low recurrence (e.g., 5.27% in a surveillance analysis subset) (nakamura2024ctdnabasedmolecularresidual pages 1-2).
- **Real-world adoption and limitations (Mayo Clinic):** 84% of ctDNA assays did not change management; guidelines had not endorsed routine ctDNA surveillance and further data are needed (JCO Precision Oncology, Feb 2024) (emiloju2024tumorinformedcirculatingtumor pages 1-2).
- **Incremental benefit of adding serial ctDNA to NCCN-guided imaging surveillance:** only **1.6%** of patients achieved curative surgical intervention attributable to ctDNA surveillance in one cohort (JAMA Network Open, Dec 2024) (ji2024circulatingtumordna pages 1-2).

**Abstract quote examples (ctDNA):**
- Nature Medicine (Sep 2024) states ctDNA MRD detection is associated with recurrence and survival: “ctDNA positivity during the MRD window… inferior disease-free survival (DFS; hazard ratio (HR): 11.99…) and overall survival (OS; HR: 9.68…)” (nakamura2024ctdnabasedmolecularresidual pages 1-2).
- JAMA Network Open (Dec 2024) summary: adding serial ctDNA assays “led to curative surgical intervention in **1.6%** of patients” (ji2024circulatingtumordna pages 1-2).

## 11. Outcome / Prognosis
### 11.1 Prognostic drivers (molecular and clinical)
- **BRAF V600E** is consistently a poor-prognosis marker; a 2024 biomarker review reports OS **10.8 vs 16.4 months** for BRAF-mutant vs wild-type in pooled data (ashouri2024exploringpredictiveand pages 6-8).
- **Metastatic site** influences prognosis: in a SEER-based model, organ metastases (brain, bone, liver, lung) were independent adverse prognostic factors with HRs ~1.26–1.75 (ren2024survivaloutcomeand pages 5-6).
- **ctDNA positivity** is a strong predictor of recurrence and mortality risk in resectable and oligometastatic settings (nakamura2024ctdnabasedmolecularresidual pages 1-2, parikh2024minimalresidualdisease pages 1-2).

## 12. Treatment (current standard, 2023–2024 advances, real-world implementation)
### 12.1 NCCN 2024: biomarker-driven treatment paradigm
NCCN Colon Cancer v3.2024 highlights that treatment selection in metastatic disease is driven by the **mutational profile**, and provides explicit biomarker-linked therapy pathways (benson2024coloncancerversion pages 2-3, benson2024coloncancerversion media afa7e635).

A representative NCCN systemic therapy decision figure (including “biomarker-directed” regimens and lines of therapy) is shown here:
- **NCCN Figure (cropped):** biomarker-directed second-line and later options (BRAF V600E, HER2, KRAS G12C, NTRK, RET; also incorporates MMR/MSI and POLE/POLD1) (benson2024coloncancerversion media afa7e635).

### 12.2 Immunotherapy for MSI-H/dMMR mCRC
A Spanish real-world paper reiterates guideline consensus that all mCRC should be tested for MSI/dMMR and summarizes pivotal trial efficacy:
- KEYNOTE-177: PFS benefit (16.5 vs 8.2 months) in untreated MSI-H/dMMR mCRC (garciacarbonero2024realworldstudyon pages 1-2).
- CheckMate-142: ORR 31% nivolumab monotherapy and 69% nivolumab+ipilimumab (garciacarbonero2024realworldstudyon pages 1-2).

**Real-world implementation gap:** In Spain (May 2020–May 2021), testing reached 84% overall, but only 29% of dMMR/MSI-H tumors received first-line immunotherapy (garciacarbonero2024realworldstudyon pages 1-2).

**Abstract quote example (testing policy):** “Clinical practice guidelines recommend that all patients with metastatic colorectal cancer (mCRC) should be tested for mismatch repair deficiency (dMMR) or microsatellite instability-high (MSI-H).” (Clinical & Translational Oncology, Aug 2024) (garciacarbonero2024realworldstudyon pages 1-2).

### 12.3 KRAS G12C: KRAS inhibitor + EGFR antibody combinations (major 2024 development)
- **Divarasib + cetuximab (Nature Medicine, Dec 2024)**: ORR **62.5%** (KRAS G12C inhibitor–naïve), median PFS **8.1 months**, DOR **6.9 months** (desai2024divarasibpluscetuximab pages 1-2).
- **NCCN v3.2024** also recognizes combinations of EGFR antibodies with KRAS G12C inhibitors in non-first-line KRAS G12C disease (benson2024coloncancerversion pages 2-3).

**Abstract quote example:** “Divarasib plus cetuximab… was well tolerated with an encouraging overall response rate of **62.5%** in patients with KRAS G12C-positive colorectal cancer.” (desai2024divarasibpluscetuximab pages 1-2).

### 12.4 BRAF V600E targeted therapy
- **BEACON CRC (reported in NCCN excerpts and biomarker reviews):** encorafenib+cetuximab improved OS and PFS vs control; OS **9.3 vs 5.9 months**, PFS **4.3 vs 1.5 months** (ashouri2024exploringpredictiveand pages 6-8, benson2024coloncancerversion pages 15-16).
- **ANCHOR CRC (JCO, May 2023)** tested first-line encorafenib+binimetinib+cetuximab in BRAFV600E mCRC with ORR **47.4%**, median OS **18.3 months** (cutsem2023anchorcrcresults pages 1-2).

### 12.5 HER2-amplified mCRC targeted therapy
NCCN lists multiple anti-HER2 regimens (including T‑DXd and trastuzumab-based combinations), with reported ORRs such as **45.3%** (T‑DXd in DESTINY‑CRC01) and **38.1%** (trastuzumab+tucatinib in MOUNTAINEER) in guideline excerpts (benson2024coloncancerversion pages 15-16).

### 12.6 Suggested MAXO terms (examples; IDs should be verified)
- Immune checkpoint inhibitor therapy; monoclonal antibody therapy; small molecule kinase inhibitor therapy; combination antineoplastic therapy; tumor biomarker testing; circulating tumor DNA testing; metastasectomy; stereotactic radiotherapy.

### 12.7 Experimental / ongoing trials (from ClinicalTrials.gov retrieval)
Examples of active or completed mCRC biomarker-linked studies retrieved include:
- KRAS G12C adagrasib (KRYSTAL-1): **NCT03785249** (desai2024divarasibpluscetuximab pages 1-2)
- Tucatinib + trastuzumab: **NCT03043313** (trial record retrieved; biomarker context in NCCN/biomarker review) (benson2024coloncancerversion pages 15-16).

## 13. Prevention
Prevention/screening-specific evidence (USPSTF/WHO/CDC) was not retrieved in this run; this section is incomplete. Nevertheless, ctDNA and biomarker reviews emphasize that CRC has “a slow progression providing a wide treatment window” and that screening can prevent CRC and reduce mortality, contextualizing the prevention opportunity even though mCRC is an advanced endpoint (emiloju2024tumorinformedcirculatingtumor pages 1-2).

## 14. Other Species / Natural Disease; 15. Model Organisms
No animal-model or comparative pathology evidence was retrieved in this run; these sections are incomplete.

---

## High-value structured summary (biomarker-directed therapy)
The following table synthesizes the key biomarker subgroups, testing definitions, guideline-positioned therapies, and recent efficacy numbers (2023–2024 prioritized):

| Biomarker / subgroup | Approx. prevalence in mCRC | Recommended testing method / definition | Key approved / standard therapies | Key efficacy outcomes with numbers (trial/source) | Notes |
|---|---:|---|---|---|---|
| **dMMR / MSI-H** | ~15% CRC overall; ~4% stage IV; Spanish real-world mCRC cohort: **6%** dMMR/MSI among tested patients (14/244) | Universal metastatic testing recommended; assess **MMR/MSI** if not previously done. MSI/MMR testing used to predict benefit from immune checkpoint inhibitors; also relevant for Lynch syndrome workup. Methods in practice include **IHC/PCR** in the Spanish cohort (garciacarbonero2024realworldstudyon pages 1-2, benson2024coloncancerversion pages 2-3, ashouri2024exploringpredictiveand pages 8-9) | **Pembrolizumab**; **nivolumab** ± **ipilimumab**; NCCN also links checkpoint inhibitors to **dMMR/MSI-H** or **POLE/POLD1-mutant** disease (Jun 2024 NCCN, https://doi.org/10.6004/jnccn.2024.0029) (garciacarbonero2024realworldstudyon pages 1-2, benson2024coloncancerversion pages 10-11) | **KEYNOTE-177**: 1L pembrolizumab vs chemotherapy, **median PFS 16.5 vs 8.2 mo**, **HR 0.60**, *p*=0.0002; OS trend **HR 0.74**, median OS not reached vs **36.7 mo** with crossover up to 60% (Garcia-Carbonero, **Aug 2024**, https://doi.org/10.1007/s12094-023-03309-z). **CheckMate-142**: ORR **31%** with nivolumab alone and **69%** with nivolumab+ipilimumab in reported data; Ashouri review also cites **24-mo PFS 74%** and **24-mo OS 79%** with nivolumab+ipilimumab and CheckMate-8HW **PFS NR vs 5.9 mo**, **HR 0.21** (garciacarbonero2024realworldstudyon pages 1-2, ashouri2024exploringpredictiveand pages 8-9) | First-line immunotherapy standard for MSI-H/dMMR mCRC. Real-world implementation gap persists: only **29%** of dMMR/MSI-H tumors received first-line immunotherapy in the Spanish cohort despite **84%** overall testing (garciacarbonero2024realworldstudyon pages 1-2) |
| **RAS wild-type (KRAS/NRAS WT), especially left-sided tumors** | RAS mutations ~50–55% of CRC, so WT is the complementary subgroup | NCCN: **KRAS/NRAS genotyping for all mCRC**; use tumor tissue (primary or metastasis). Anti-EGFR therapy should **not** be used in tumors with KRAS or NRAS mutation (Jun 2024 NCCN, https://doi.org/10.6004/jnccn.2024.0029) (benson2024coloncancerversion pages 2-3, benson2024coloncancerversion pages 10-11) | **Cetuximab** or **panitumumab** with chemotherapy (e.g., **FOLFOX**; also CAPEOX combinations listed by NCCN for selected settings) (benson2024coloncancerversion pages 10-11) | **PRIME**: panitumumab+FOLFOX improved **PFS HR 0.72** (95% CI 0.58–0.90; *P*=0.004) and **OS HR 0.77** (95% CI 0.64–0.94; *P*=0.009) in KRAS/NRAS WT. **PARADIGM**: median OS **37.9 vs 34.3 mo** (panitumumab vs bevacizumab) in left-sided RAS WT and **36.2 vs 31.3 mo** overall RAS WT. **CALGB/SWOG 80405**: OS **29.0 vs 30.0 mo** (cetuximab vs bevacizumab) (NCCN **Jun 2024**, https://doi.org/10.6004/jnccn.2024.0029) (benson2024coloncancerversion pages 10-11) | Benefit is strongest in molecularly selected WT disease; acquired resistance after anti-EGFR therapy is common, with secondary RAS alterations reported in ~50% within 12 months in review data (ashouri2024exploringpredictiveand pages 2-5, benson2024coloncancerversion pages 2-3) |
| **KRAS-mutant (all)** | ~50–55% CRC; common KRAS variants: **G12D 36%**, **G12V 21.8%**, **G13D 18.8%** | RAS testing by tumor genotyping; NCCN prefers **NGS panels** because they can also detect rarer actionable events (e.g., NTRK, RET). KRAS/NRAS-mutant tumors should **not** receive cetuximab/panitumumab, except EGFR antibody can be paired with a **KRAS G12C inhibitor** in non-first-line KRAS G12C disease (benson2024coloncancerversion pages 2-3) | No anti-EGFR monotherapy/standard EGFR combination in routine KRAS-mutant disease; enroll in biomarker-directed strategies if **KRAS G12C** (below) (benson2024coloncancerversion pages 2-3, cotan2024prognosticandpredictive pages 10-11) | KRAS-mutant mCRC has worse outcomes in review data: OS **20.9 vs 16.9 mo** for WT vs mutant in HORIZON II; KRAS G12C especially poor prognosis with OS **4.3 vs 23.3 mo** in cited review summary (Ashouri, **Aug 2024**, https://doi.org/10.3390/cancers16162796) (ashouri2024exploringpredictiveand pages 2-5) | Main clinical role is **negative selection** against anti-EGFR therapy, except the KRAS G12C-specific EGFR co-blockade setting (benson2024coloncancerversion pages 2-3) |
| **KRAS G12C-mutant** | ~**3–4%** of CRC; NCCN excerpt estimates KRAS G12C is ~**17% of KRAS-mutant** cases | Detect by tumor genotyping/NGS; NCCN notes tissue or blood may be used for molecular profiling, with NGS preferred for broad detection (Jun 2024 NCCN, https://doi.org/10.6004/jnccn.2024.0029) (benson2024coloncancerversion pages 2-3, benson2024coloncancerversion pages 15-16) | **Adagrasib + cetuximab**; **sotorasib + panitumumab**; emerging **divarasib + cetuximab** (trial) (benson2024coloncancerversion pages 2-3, benson2024coloncancerversion pages 15-16, desai2024divarasibpluscetuximab pages 1-2) | **KRYSTAL-1**: adagrasib monotherapy ORR **19%**, DCR **86%**, median **PFS 5.6 mo**, median **OS 19.8 mo**; adagrasib + cetuximab ORR **46%**, DCR **100%**, median **PFS 6.9 mo**, median **OS 13.4 mo** in one review summary; NCCN updated pooled data cite ORR **34.0%**, DCR **85.1%**, median **PFS 6.9 mo**, median **OS 15.9 mo** (Jun 2024 NCCN, https://doi.org/10.6004/jnccn.2024.0029) (cotan2024prognosticandpredictive pages 10-11, benson2024coloncancerversion pages 15-16). **CodeBreaK-300** early data: sotorasib+panitumumab **PFS 5.6 mo** (960 mg) vs SOC **2.2 mo** (ashouri2024exploringpredictiveand pages 2-5). **Divarasib + cetuximab** phase 1b: ORR **62.5%** (95% CI 40.6–81.2), median DOR **6.9 mo**, median **PFS 8.1 mo** in KRAS G12C inhibitor–naive patients (Nature Medicine, **Dec 2024**, https://doi.org/10.1038/s41591-023-02696-8) (desai2024divarasibpluscetuximab pages 1-2) | EGFR-mediated adaptive feedback is a major resistance mechanism, explaining why **EGFR co-blockade** outperforms KRAS G12C inhibitor monotherapy (desai2024divarasibpluscetuximab pages 1-2, cotan2024prognosticandpredictive pages 10-11) |
| **BRAF V600E-mutant** | ~**8–12%** mCRC; broader reports cite **10–15%** | Test for **BRAF** mutation as part of baseline metastatic profiling; BRAFV600E is a poor-prognosis biomarker (benson2024coloncancerversion pages 2-3, ashouri2024exploringpredictiveand pages 6-8) | **Encorafenib + cetuximab** (preferred targeted doublet in previously treated disease); triplet **encorafenib + binimetinib + cetuximab** has similar OS but more toxicity; first-line triplet under study/selected situations (benson2024coloncancerversion pages 15-16, cutsem2023anchorcrcresults pages 1-2) | **BEACON**: control vs encorafenib+cetuximab vs triplet showed OS **5.9 vs 9.3 vs 9.3 mo** and PFS **1.5 vs 4.3 vs 4.5 mo**; NCCN cites confirmed ORR **1.8% vs 19.5% vs 26.8%** (Jun 2024 NCCN, https://doi.org/10.6004/jnccn.2024.0029; Ashouri **Aug 2024** https://doi.org/10.3390/cancers16162796) (ashouri2024exploringpredictiveand pages 6-8, benson2024coloncancerversion pages 15-16). **ANCHOR CRC** first-line triplet in BRAFV600E mCRC: ORR **47.4%** (95% CI 37.0–57.9), median **PFS 5.8 mo**, median **OS 18.3 mo** (JCO, **May 2023**, https://doi.org/10.1200/jco.22.01693) (cutsem2023anchorcrcresults pages 1-2) | BRAFV600E is associated with proximal location, aggressive biology, unfavorable metastatic pattern, and reduced OS; anti-EGFR alone is insufficient because BRAF blockade triggers **EGFR feedback activation** (cutsem2023anchorcrcresults pages 1-2, ashouri2024exploringpredictiveand pages 6-8, cotan2024prognosticandpredictive pages 10-11) |
| **HER2-amplified / overexpressed (usually RAS/BRAF WT)** | ~**2–6%** mCRC; other review estimate **3–5%** | NCCN recommends **HER2 testing for all mCRC**. Methods: **IHC**, **FISH**, or **NGS**. **IHC 3+** = positive overexpression; **IHC 2+** = equivocal and should prompt FISH; **FISH ratio ≥2** confirms amplification (ashouri2024exploringpredictiveand pages 6-8, ashouri2024exploringpredictiveand pages 8-9, benson2024coloncancerversion pages 15-16) | **Fam-trastuzumab deruxtecan-nxki (T-DXd)**; **trastuzumab + pertuzumab**; **trastuzumab + lapatinib**; **trastuzumab + tucatinib** (NCCN **Jun 2024**, https://doi.org/10.6004/jnccn.2024.0029) (benson2024coloncancerversion pages 15-16) | **DESTINY-CRC01** (T-DXd): ORR **45.3%**, median **PFS 6.9 mo**, median OS not reached at reported cut; ILD/pneumonitis in **8** patients with **3 deaths**. **MyPathway** (trastuzumab+pertuzumab): ORR **32%**. **HERACLES** (trastuzumab+lapatinib): ORR **30%**, DCR **59%**, median **PFS 5.3 mo**, median **OS 11.5 mo**. **MOUNTAINEER** (trastuzumab+tucatinib): confirmed ORR **38.1%** (NCCN **Jun 2024**, https://doi.org/10.6004/jnccn.2024.0029; reviews **2024**) (cotan2024prognosticandpredictive pages 13-15, ashouri2024exploringpredictiveand pages 8-9, benson2024coloncancerversion pages 15-16) | Enriched in left-sided and **RAS/BRAF WT** tumors; may mediate anti-EGFR resistance. Responses are lower in KRAS-mutant disease in post hoc analyses (cotan2024prognosticandpredictive pages 13-15, ashouri2024exploringpredictiveand pages 8-9) |
| **NTRK fusion-positive** | ~**0.7%** | Broad **NGS** is preferred because rare actionable fusions may be missed by single-gene testing; NCCN biomarker-directed therapy figure includes **NTRK gene fusions** (benson2024coloncancerversion pages 2-3, underwood2024precisionmedicinefor pages 2-4, benson2024coloncancerversion media afa7e635) | **Larotrectinib**; **entrectinib** (Underwood review also references repotrectinib) (underwood2024precisionmedicinefor pages 2-4) | No trial efficacy numbers were present in the gathered evidence excerpts used here; therapy assignment is supported by biomarker-directed NCCN/precision oncology summaries (underwood2024precisionmedicinefor pages 2-4, benson2024coloncancerversion media afa7e635) | Rare but actionable; typically identified through broad NGS rather than stepwise hotspot testing (benson2024coloncancerversion pages 2-3, benson2024coloncancerversion media afa7e635) |
| **RET fusion-positive** | ~**0.2%** | Broad **NGS** preferred for rare fusion detection; NCCN biomarker-directed therapy figure includes **RET gene fusions** (benson2024coloncancerversion pages 2-3, underwood2024precisionmedicinefor pages 2-4, benson2024coloncancerversion media afa7e635) | **Selpercatinib** (underwood2024precisionmedicinefor pages 2-4, benson2024coloncancerversion media afa7e635) | No numeric CRC-specific efficacy outcomes were provided in the gathered excerpts used here (underwood2024precisionmedicinefor pages 2-4, benson2024coloncancerversion media afa7e635) | Very rare, but clinically actionable when found; reinforces value of comprehensive molecular profiling in mCRC (benson2024coloncancerversion pages 2-3, underwood2024precisionmedicinefor pages 2-4) |
| **POLE / POLD1-mutant (hypermutated subgroup)** | Not quantified in gathered excerpts | Mentioned by NCCN alongside **dMMR/MSI-H** as a subgroup for checkpoint inhibitor consideration; usually identified by comprehensive tumor sequencing (benson2024coloncancerversion pages 10-11) | **Checkpoint inhibitor immunotherapy** (NCCN linkage in metastatic algorithm; Jun 2024, https://doi.org/10.6004/jnccn.2024.0029) (benson2024coloncancerversion pages 10-11) | No separate efficacy figures for POLE/POLD1-mutant mCRC were available in the gathered evidence excerpts (benson2024coloncancerversion pages 10-11) | Clinically important as an additional hypermutated/immunotherapy-sensitive subset beyond MSI-H/dMMR (benson2024coloncancerversion pages 10-11) |


*Table: This table summarizes biomarker-defined treatment subgroups in metastatic colorectal cancer using gathered 2023-2024 evidence and NCCN v3.2024 excerpts. It highlights recommended testing, standard targeted/immunotherapy options, and key efficacy numbers to support rapid clinical and research reference.*

---

## Key statistics and “latest research” highlights (2023–2024)
1. **NCCN 2024** endorses broad baseline molecular profiling for metastatic CRC (KRAS/NRAS, BRAF, HER2, MSI/MMR; NGS preferred to capture NTRK/RET) and maps these biomarkers to therapy selection (benson2024coloncancerversion pages 2-3, benson2024coloncancerversion media afa7e635).
2. **KRAS G12C dual blockade** is a major 2024 advance: divarasib+cetuximab ORR **62.5%** and median PFS **8.1 months** in KRAS G12C inhibitor–naïve CRC (Nature Medicine Dec 2024) (desai2024divarasibpluscetuximab pages 1-2).
3. **ctDNA MRD** is increasingly validated as a strong prognostic tool (Nature Medicine Sep 2024: DFS HR **11.99**, OS HR **9.68**, median lead time **5.9 months**), but real-world studies show limited immediate management impact and unclear outcome benefit from routine surveillance (nakamura2024ctdnabasedmolecularresidual pages 1-2, ji2024circulatingtumordna pages 1-2, emiloju2024tumorinformedcirculatingtumor pages 1-2).
4. **Population prognosis** (SEER): early-onset metastatic CRC median OS **30 months** vs **18 months** for average-onset; liver-only metastasis ~**70%** (jeriyabar2024survivalanalysisof pages 1-2, jeriyabar2024survivalanalysisof pages 4-6).

---

## URLs and publication dates (selected, high-authority sources used)
- NCCN Colon Cancer, Version 3.2024 (JNCCN; **Jun 2024**): https://doi.org/10.6004/jnccn.2024.0029 (benson2024coloncancerversion pages 2-3)
- Divarasib + cetuximab phase 1b (Nature Medicine; **Dec 2024**): https://doi.org/10.1038/s41591-023-02696-8 (desai2024divarasibpluscetuximab pages 1-2)
- ANCHOR CRC (JCO; **May 2023**): https://doi.org/10.1200/JCO.22.01693 (cutsem2023anchorcrcresults pages 1-2)
- Real-world MSI/dMMR testing in Spain (Clin Transl Oncol; **Aug 2024**): https://doi.org/10.1007/s12094-023-03309-z (garciacarbonero2024realworldstudyon pages 1-2)
- ctDNA MRD and survival (Nature Medicine; **Sep 2024**): https://doi.org/10.1038/s41591-024-03254-6 (nakamura2024ctdnabasedmolecularresidual pages 1-2)
- Plasma-only MRD in oligometastatic CRC (Clin Cancer Res; **May 2024**): https://doi.org/10.1158/1078-0432.CCR-23-3660 (parikh2024minimalresidualdisease pages 1-2)
- Serial ctDNA surveillance cohort (JAMA Netw Open; **Dec 2024**): https://doi.org/10.1001/jamanetworkopen.2024.52661 (ji2024circulatingtumordna pages 1-2)

---

## Limitations of this report (due to tool-accessible evidence in this run)
Several requested template sections remain incomplete because primary sources for etiology/risk factors, prevention/screening guidelines, detailed phenotype/QoL instruments, microbiome/environmental contributors, and model organism data were not retrieved via the current searches. The molecular diagnostics, treatment, ctDNA/MRD, and population prognosis components are well-supported by 2023–2024 guideline/trial/registry evidence in this run (benson2024coloncancerversion pages 2-3, desai2024divarasibpluscetuximab pages 1-2, nakamura2024ctdnabasedmolecularresidual pages 1-2, jeriyabar2024survivalanalysisof pages 1-2).

References

1. (OpenTargets Search: metastatic colorectal cancer): Open Targets Query (metastatic colorectal cancer, 48 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (garciacarbonero2024realworldstudyon pages 1-2): Rocio Garcia-Carbonero, Beatriz González Astorga, Rosario Vidal Tocino, Débora Contreras Toledo, Carles Pericay, Ana Fernández Montes, Esther Falcó, Marta González Cordero, Juan José Reina Zoilo, Vicente Alonso, Nuria Rodríguez Salas, Mireia Gil-Raga, Cristina Santos, David Páez, Beatriz Anton-Pascual, Fernando Aguilar, and Pilar Morales. Real-world study on microsatellite instability and mismatch repair deficiency testing patterns among patients with metastatic colorectal cancer in spain. Clinical & Translational Oncology, 26:864-871, Aug 2024. URL: https://doi.org/10.1007/s12094-023-03309-z, doi:10.1007/s12094-023-03309-z. This article has 7 citations and is from a peer-reviewed journal.

3. (benson2024coloncancerversion pages 2-3): Al B. Benson, A. Venook, Mohamed Adam, George J. Chang, Yi-Jen Chen, K. K. Ciombor, Stacey A Cohen, Harry S. Cooper, Dustin Deming, Ignacio Garrido-Laguna, Jean L Grem, Paul Haste, J. R. Hecht, Sarah Hoffe, S. Hunt, H. Hussan, K. Johung, Nora Joseph, Natalie N. Kirilcuk, S. Krishnamurthi, Midhun Malla, Jennifer K Maratt, W. Messersmith, J. Meyerhardt, E. D. Miller, M. Mulcahy, Steven J. Nurkin, M. Overman, Aparna Parikh, Hitendra Patel, Katrina Pedersen, Leonard Saltz, Charles Schneider, David Shibata, Benjamin Shogan, J. Skibber, Constantinos T Sofocleous, Anna Tavakkoli, Christopher G. Willett, Christina Wu, Lisa A. Gurski, Jenna Snedeker, and Frankie Jones. Colon cancer, version 3.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, Jun 2024. URL: https://doi.org/10.6004/jnccn.2024.0029, doi:10.6004/jnccn.2024.0029. This article has 450 citations.

4. (cutsem2023anchorcrcresults pages 1-2): Eric Van Cutsem, Julien Taieb, Rona Yaeger, Takayuki Yoshino, Axel Grothey, Evaristo Maiello, Elena Elez, Jeroen Dekervel, Paul Ross, Ana Ruiz-Casado, Janet Graham, Takeshi Kato, Jose C. Ruffinelli, Thierry André, Edith Carrière Roussel, Isabelle Klauck, Mélanie Groc, Jean-Claude Vedovato, and Josep Tabernero. Anchor crc: results from a single-arm, phase ii study of encorafenib plus binimetinib and cetuximab in previously untreated <i>braf</i><sup>v600e</sup>-mutant metastatic colorectal cancer. Journal of Clinical Oncology, 41:2628-2637, May 2023. URL: https://doi.org/10.1200/jco.22.01693, doi:10.1200/jco.22.01693. This article has 102 citations and is from a highest quality peer-reviewed journal.

5. (desai2024divarasibpluscetuximab pages 1-2): Jayesh Desai, Guzman Alonso, Se Hyun Kim, Andres Cervantes, Thomas Karasic, Laura Medina, Einat Shacham-Shmueli, Rasha Cosman, Alejandro Falcon, Eelke Gort, Tormod Guren, Erminia Massarelli, Wilson H. Miller, Luis Paz-Ares, Hans Prenen, Alessio Amatu, Chiara Cremolini, Tae Won Kim, Victor Moreno, Sai-Hong I. Ou, Alessandro Passardi, Adrian Sacher, Armando Santoro, Rafal Stec, Susanna Ulahannan, Kathryn Arbour, Patricia Lorusso, Jia Luo, Manish R. Patel, Yoonha Choi, Zhen Shi, Sandhya Mandlekar, Mark T. Lin, Stephanie Royer-Joo, Julie Chang, Tomi Jun, Neekesh V. Dharia, Jennifer L. Schutzman, and Sae-Won Han. Divarasib plus cetuximab in kras g12c-positive colorectal cancer: a phase 1b trial. Nature Medicine, 30:271-278, Dec 2024. URL: https://doi.org/10.1038/s41591-023-02696-8, doi:10.1038/s41591-023-02696-8. This article has 142 citations and is from a highest quality peer-reviewed journal.

6. (nakamura2024ctdnabasedmolecularresidual pages 1-2): Yoshiaki Nakamura, Jun Watanabe, Naoya Akazawa, Keiji Hirata, Kozo Kataoka, Mitsuru Yokota, Kentaro Kato, Masahito Kotaka, Yoshinori Kagawa, Kun-Huei Yeh, Saori Mishima, Hiroki Yukami, Koji Ando, Masaaki Miyo, Toshihiro Misumi, Kentaro Yamazaki, Hiromichi Ebi, Kenji Okita, Atsushi Hamabe, Hiroki Sokuoka, Satoshi Kobayashi, George Laliotis, Vasily N. Aushev, Shruti Sharma, Adham Jurdi, Minetta C. Liu, Alexey Aleshin, Matthew Rabinowitz, Hideaki Bando, Hiroya Taniguchi, Ichiro Takemasa, Takeshi Kato, Daisuke Kotani, Masaki Mori, Takayuki Yoshino, and Eiji Oki. Ctdna-based molecular residual disease and survival in resectable colorectal cancer. Nature Medicine, 30:3272-3283, Sep 2024. URL: https://doi.org/10.1038/s41591-024-03254-6, doi:10.1038/s41591-024-03254-6. This article has 206 citations and is from a highest quality peer-reviewed journal.

7. (jeriyabar2024survivalanalysisof pages 1-2): Antoine Jeri-Yabar, Liliana Vittini-Hernandez, Sebastian Prado-Nuñez, and Sirish Dharmapuri. Survival analysis of metastatic early-onset colorectal cancer compared to metastatic average-onset colorectal cancer: a seer database analysis. Cancers, 16:2004, May 2024. URL: https://doi.org/10.3390/cancers16112004, doi:10.3390/cancers16112004. This article has 8 citations.

8. (benson2024coloncancerversion pages 15-16): Al B. Benson, A. Venook, Mohamed Adam, George J. Chang, Yi-Jen Chen, K. K. Ciombor, Stacey A Cohen, Harry S. Cooper, Dustin Deming, Ignacio Garrido-Laguna, Jean L Grem, Paul Haste, J. R. Hecht, Sarah Hoffe, S. Hunt, H. Hussan, K. Johung, Nora Joseph, Natalie N. Kirilcuk, S. Krishnamurthi, Midhun Malla, Jennifer K Maratt, W. Messersmith, J. Meyerhardt, E. D. Miller, M. Mulcahy, Steven J. Nurkin, M. Overman, Aparna Parikh, Hitendra Patel, Katrina Pedersen, Leonard Saltz, Charles Schneider, David Shibata, Benjamin Shogan, J. Skibber, Constantinos T Sofocleous, Anna Tavakkoli, Christopher G. Willett, Christina Wu, Lisa A. Gurski, Jenna Snedeker, and Frankie Jones. Colon cancer, version 3.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, Jun 2024. URL: https://doi.org/10.6004/jnccn.2024.0029, doi:10.6004/jnccn.2024.0029. This article has 450 citations.

9. (benson2024coloncancerversion media afa7e635): Al B. Benson, A. Venook, Mohamed Adam, George J. Chang, Yi-Jen Chen, K. K. Ciombor, Stacey A Cohen, Harry S. Cooper, Dustin Deming, Ignacio Garrido-Laguna, Jean L Grem, Paul Haste, J. R. Hecht, Sarah Hoffe, S. Hunt, H. Hussan, K. Johung, Nora Joseph, Natalie N. Kirilcuk, S. Krishnamurthi, Midhun Malla, Jennifer K Maratt, W. Messersmith, J. Meyerhardt, E. D. Miller, M. Mulcahy, Steven J. Nurkin, M. Overman, Aparna Parikh, Hitendra Patel, Katrina Pedersen, Leonard Saltz, Charles Schneider, David Shibata, Benjamin Shogan, J. Skibber, Constantinos T Sofocleous, Anna Tavakkoli, Christopher G. Willett, Christina Wu, Lisa A. Gurski, Jenna Snedeker, and Frankie Jones. Colon cancer, version 3.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, Jun 2024. URL: https://doi.org/10.6004/jnccn.2024.0029, doi:10.6004/jnccn.2024.0029. This article has 450 citations.

10. (underwood2024precisionmedicinefor pages 2-4): Patrick W. Underwood and Timothy M. Pawlik. Precision medicine for metastatic colorectal cancer: where do we stand? Cancers, 16:3870, Nov 2024. URL: https://doi.org/10.3390/cancers16223870, doi:10.3390/cancers16223870. This article has 12 citations.

11. (jeriyabar2024survivalanalysisof pages 4-6): Antoine Jeri-Yabar, Liliana Vittini-Hernandez, Sebastian Prado-Nuñez, and Sirish Dharmapuri. Survival analysis of metastatic early-onset colorectal cancer compared to metastatic average-onset colorectal cancer: a seer database analysis. Cancers, 16:2004, May 2024. URL: https://doi.org/10.3390/cancers16112004, doi:10.3390/cancers16112004. This article has 8 citations.

12. (jeriyabar2024survivalanalysisclinical pages 1-2): Antoine Jeri-Yabar, Liliana Vittini-Hernandez, Jerry K. Benites-Meza, and Sebastian Prado-Nuñez. Survival analysis, clinical characteristics, and predictors of cerebral metastases in patients with colorectal cancer. Medical Sciences, 12:47, Sep 2024. URL: https://doi.org/10.3390/medsci12030047, doi:10.3390/medsci12030047. This article has 4 citations.

13. (ren2024survivaloutcomeand pages 6-8): B. Ren, Yichen Yang, Yi Lv, and Kang-Nian Liu. Survival outcome and prognostic factors for early-onset and late-onset metastatic colorectal cancer: a population based study from seer database. Scientific Reports, Feb 2024. URL: https://doi.org/10.1038/s41598-024-54972-3, doi:10.1038/s41598-024-54972-3. This article has 40 citations and is from a peer-reviewed journal.

14. (parikh2024minimalresidualdisease pages 1-2): Aparna R. Parikh, Bryant H. Chee, Jill Tsai, Thereasa A. Rich, Kristin S. Price, Sonia A. Patel, Li Zhang, Faaiz Ibrahim, Mikaela Esquivel, Emily E. Van Seventer, Joy X. Jarnagin, Victoria M. Raymond, Carlos U. Corvera, Kenzo Hirose, Eric K. Nakakura, Ryan B. Corcoran, Katherine Van Loon, and Chloe E. Atreya. Minimal residual disease using a plasma-only circulating tumor dna assay to predict recurrence of metastatic colorectal cancer following curative intent treatment. Clinical Cancer Research, 30:2964-2973, May 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-3660, doi:10.1158/1078-0432.ccr-23-3660. This article has 20 citations and is from a highest quality peer-reviewed journal.

15. (ashouri2024exploringpredictiveand pages 2-5): Karam Ashouri, Alexandra Wong, Pooja Mittal, Lesly Torres-Gonzalez, Jae Ho Lo, Shivani Soni, Sandra Algaze, Taline Khoukaz, Wu Zhang, Yan Yang, Joshua Millstein, Heinz-Josef Lenz, and Francesca Battaglin. Exploring predictive and prognostic biomarkers in colorectal cancer: a comprehensive review. Cancers, 16:2796, Aug 2024. URL: https://doi.org/10.3390/cancers16162796, doi:10.3390/cancers16162796. This article has 18 citations.

16. (ashouri2024exploringpredictiveand pages 6-8): Karam Ashouri, Alexandra Wong, Pooja Mittal, Lesly Torres-Gonzalez, Jae Ho Lo, Shivani Soni, Sandra Algaze, Taline Khoukaz, Wu Zhang, Yan Yang, Joshua Millstein, Heinz-Josef Lenz, and Francesca Battaglin. Exploring predictive and prognostic biomarkers in colorectal cancer: a comprehensive review. Cancers, 16:2796, Aug 2024. URL: https://doi.org/10.3390/cancers16162796, doi:10.3390/cancers16162796. This article has 18 citations.

17. (ashouri2024exploringpredictiveand pages 8-9): Karam Ashouri, Alexandra Wong, Pooja Mittal, Lesly Torres-Gonzalez, Jae Ho Lo, Shivani Soni, Sandra Algaze, Taline Khoukaz, Wu Zhang, Yan Yang, Joshua Millstein, Heinz-Josef Lenz, and Francesca Battaglin. Exploring predictive and prognostic biomarkers in colorectal cancer: a comprehensive review. Cancers, 16:2796, Aug 2024. URL: https://doi.org/10.3390/cancers16162796, doi:10.3390/cancers16162796. This article has 18 citations.

18. (cotan2024prognosticandpredictive pages 10-11): Horia T. Cotan, Radu A. Emilescu, Cristian I. Iaciu, Cristina M. Orlov-Slavu, Mihaela C. Olaru, Ana M. Popa, Mariana Jinga, Cornelia Nitipir, Oliver Daniel Schreiner, and Romeo Cristian Ciobanu. Prognostic and predictive determinants of colorectal cancer: a comprehensive review. Cancers, 16:3928, Nov 2024. URL: https://doi.org/10.3390/cancers16233928, doi:10.3390/cancers16233928. This article has 19 citations.

19. (ren2024survivaloutcomeand pages 5-6): B. Ren, Yichen Yang, Yi Lv, and Kang-Nian Liu. Survival outcome and prognostic factors for early-onset and late-onset metastatic colorectal cancer: a population based study from seer database. Scientific Reports, Feb 2024. URL: https://doi.org/10.1038/s41598-024-54972-3, doi:10.1038/s41598-024-54972-3. This article has 40 citations and is from a peer-reviewed journal.

20. (emiloju2024tumorinformedcirculatingtumor pages 1-2): Oluwadunni E. Emiloju, Michael Storandt, Tyler Zemla, Nguyen Tran, Krishan Jethwa, Amit Mahipal, Jessica Mitchell, Cornelius Thiels, Kellie Mathis, Robert McWilliams, Joleen Hubbard, Frank Sinicrope, Qian Shi, and Zhaohui Jin. Tumor-informed circulating tumor dna for minimal residual disease detection in the management of colorectal cancer. JCO Precision Oncology, Feb 2024. URL: https://doi.org/10.1200/po.23.00127, doi:10.1200/po.23.00127. This article has 12 citations and is from a peer-reviewed journal.

21. (ji2024circulatingtumordna pages 1-2): Jingran Ji, Chongkai Wang, Ajay Goel, Kurt Melstrom, Yasmin Zerhouni, Lily Lai, Laleh Melstrom, Mustafa Raoof, Yuman Fong, Andreas Kaiser, and Marwan Fakih. Circulating tumor dna testing in curatively resected colorectal cancer and salvage resection. JAMA Network Open, 7:e2452661, Dec 2024. URL: https://doi.org/10.1001/jamanetworkopen.2024.52661, doi:10.1001/jamanetworkopen.2024.52661. This article has 9 citations and is from a peer-reviewed journal.

22. (benson2024coloncancerversion pages 10-11): Al B. Benson, A. Venook, Mohamed Adam, George J. Chang, Yi-Jen Chen, K. K. Ciombor, Stacey A Cohen, Harry S. Cooper, Dustin Deming, Ignacio Garrido-Laguna, Jean L Grem, Paul Haste, J. R. Hecht, Sarah Hoffe, S. Hunt, H. Hussan, K. Johung, Nora Joseph, Natalie N. Kirilcuk, S. Krishnamurthi, Midhun Malla, Jennifer K Maratt, W. Messersmith, J. Meyerhardt, E. D. Miller, M. Mulcahy, Steven J. Nurkin, M. Overman, Aparna Parikh, Hitendra Patel, Katrina Pedersen, Leonard Saltz, Charles Schneider, David Shibata, Benjamin Shogan, J. Skibber, Constantinos T Sofocleous, Anna Tavakkoli, Christopher G. Willett, Christina Wu, Lisa A. Gurski, Jenna Snedeker, and Frankie Jones. Colon cancer, version 3.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, Jun 2024. URL: https://doi.org/10.6004/jnccn.2024.0029, doi:10.6004/jnccn.2024.0029. This article has 450 citations.

23. (cotan2024prognosticandpredictive pages 13-15): Horia T. Cotan, Radu A. Emilescu, Cristian I. Iaciu, Cristina M. Orlov-Slavu, Mihaela C. Olaru, Ana M. Popa, Mariana Jinga, Cornelia Nitipir, Oliver Daniel Schreiner, and Romeo Cristian Ciobanu. Prognostic and predictive determinants of colorectal cancer: a comprehensive review. Cancers, 16:3928, Nov 2024. URL: https://doi.org/10.3390/cancers16233928, doi:10.3390/cancers16233928. This article has 19 citations.
