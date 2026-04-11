---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T16:04:48.892443'
end_time: '2026-04-04T16:13:16.365315'
duration_seconds: 507.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Rabies
  mondo_id: ''
  category: Infectious Disease
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
- **Disease Name:** Rabies
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Rabies** covering all of the
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
- **Disease Name:** Rabies
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Rabies** covering all of the
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


# Rabies — Comprehensive Disease Characteristics Report (Infectious Disease)

## Executive summary (current understanding)
Rabies is an acute, progressive encephalitis caused by a neurotropic, negative-sense single-stranded RNA virus in the family *Rhabdoviridae* (genus *Lyssavirus*), classically transmitted via bites/saliva exposure from infected mammals (especially dogs). Once clinical symptoms begin, rabies is almost invariably fatal; therefore, the public-health focus is on prevention through vaccination of reservoir animals and prompt human post-exposure prophylaxis (PEP). (kaye2024rabiesvaccinefor pages 1-2)

Recent work (2023–2024) emphasizes (i) narrowing data gaps in global mortality estimation and program capacity using infrastructure-based indices, (ii) implementation science around One Health approaches (mass dog vaccination, surveillance, and bite case management), (iii) improved characterization of long-term immunity after vaccine-sparing intradermal PEP regimens, and (iv) continued development of rabies monoclonal antibodies (mAbs) as alternatives to rabies immunoglobulin (RIG). (bonaparte2023evaluationofcountry pages 1-2, ghosh2024rabiescontrolin pages 1-2, ya2024evaluationofone pages 1-2, chen2025circulatingantibody’srole pages 12-13)

| Aspect | Key recent finding/statistic | Source (first author, year) | Publication venue | DOI/URL | Evidence type |
|---|---|---|---|---|---|
| Global burden and dog-mediated fraction | Rabies causes ~59,000 human deaths annually worldwide; >99% of human rabies deaths/cases are linked to infected dogs, with highest burden in Asia and Africa (ghosh2024rabiescontrolin pages 1-2, mwanyalu2025documentingchallengesin pages 1-2, okech2025participatoryapproachin pages 1-2) | Ghosh, 2024 | *Lancet Regional Health – Southeast Asia* | https://doi.org/10.1016/j.lansea.2024.100452 | Epidemiologic analysis / One Health program study |
| STOP-R modeled deaths in endemic countries | STOP-R index estimated 40,111 human rabies deaths in 2022 (95% CI 25,854–74,344) across DMRVV-endemic countries; projected 32,349 by 2030 (bonaparte2023evaluationofcountry pages 1-2, bonaparte2023evaluationofcountry pages 6-7) | Bonaparte, 2023 | *Frontiers in Veterinary Science* | https://doi.org/10.3389/fvets.2023.1147543 | Modeling study |
| Bangladesh dog population and mass dog vaccination | Estimated dog population 1,668,140; density 12.83 dogs/km²; human:dog ratio 86.70; MDV vaccinated mean 21,295 dogs/district/year out of ~26,065 estimated dogs; 70% annual pulse coverage is the operational target for interruption of transmission (ghosh2024rabiescontrolin pages 1-2) | Ghosh, 2024 | *Lancet Regional Health – Southeast Asia* | https://doi.org/10.1016/j.lansea.2024.100452 | National program analysis / forecasting |
| Kenya (Lamu County) implementation barriers | From 2020–2022, 73% (11/16) of facilities had human rabies vaccine stock-outs; 19% (3/16) had both vaccine and RIG; only 25% of health workers said first action was wound washing; 86% did not know recommended vaccine/RIG dosage and schedule (mwanyalu2025documentingchallengesin pages 1-2) | Mwanyalu, 2025 | *One Health Outlook* | https://doi.org/10.1186/s42522-024-00129-1 | Mixed-methods implementation study |
| PEP immunogenicity durability | After IPC intradermal PEP, all but 2 participants seroconverted by day 14; 87.0% retained neutralizing antibody titers ≥0.5 IU/mL at 12 months; IL-4 and IFN-γ T-cell responses persisted up to 1 year (ya2024evaluationofone pages 1-2, ya2024evaluationofone pages 2-3, ya2024evaluationofone pages 3-4) | Ya, 2024 | *NPJ Vaccines* | https://doi.org/10.1038/s41541-024-01030-8 | Prospective human immunogenicity study |
| Fatal PEP breakthrough infections | Systematic review identified 122 fatal breakthrough infections despite receipt of cell-culture vaccine; median exposure-to-symptom onset 20 days (IQR 16–24); deviations from core PEP practices in 56% (68/122) of cases (whitehouse2023humanrabiesdespite pages 1-3, whitehouse2023humanrabiesdespite pages 4-6) | Whitehouse, 2023 | *The Lancet Infectious Diseases* | https://doi.org/10.1016/S1473-3099(22)00641-7 | Systematic review |
| Diagnostic accuracy: human tests | Meta-analysis: human ELISA median sensitivity 90.5%, specificity 95.0%; human RT-PCR median sensitivity 94.4%, specificity 97.7%; RT-PCR detects viral RNA from saliva, CSF, and tissue samples (candiapuma2025evaluatingrabiestest pages 8-9, candiapuma2025evaluatingrabiestest pages 2-4, candiapuma2025evaluatingrabiestest pages 14-16) | Candia-Puma, 2025 | *Diagnostics* | https://doi.org/10.3390/diagnostics15040412 | Systematic review and meta-analysis |
| Diagnostic accuracy: canine/postmortem comparator tests | DFAT on brain tissue remains traditional postmortem gold standard, but pooled canine DFAT performance was variable (median sensitivity 79.2%, specificity 95.0%); canine rapid immunochromatographic tests had median sensitivity 93.5% and specificity 99.1% (candiapuma2025evaluatingrabiestest pages 9-12, candiapuma2024rabiestestaccuracy pages 1-3, candiapuma2024rabiestestaccuracy pages 12-14) | Candia-Puma, 2025 | *Diagnostics* | https://doi.org/10.3390/diagnostics15040412 | Systematic review and meta-analysis |
| ACIP PrEP schedule update | U.S. ACIP 2022 recommends a 2-dose intramuscular rabies PrEP series on days 0 and 7 for risk categories 1–4, replacing the older 3-dose primary series for many at-risk groups (rao2022useofa media 7550c3e2) | Rao, 2022 | *MMWR* | https://doi.org/10.15585/mmwr.mm7118a2 | U.S. guideline / expert recommendation |
| Dog vaccination threshold for elimination | Achieving ~70% dog vaccination coverage is repeatedly cited as the key herd-immunity threshold for interrupting dog-mediated rabies transmission (blumberg2024eliminationofdogmediated pages 1-2, beron2024dogmediatedrabiesvirus pages 1-3, ghosh2024rabiescontrolin pages 1-2) | Blumberg, 2024 | *Revue Scientifique et Technique de l'OIE* | https://doi.org/10.20506/rst.se.3560 | Expert review / public health policy |
| Real-world One Health surveillance / IBCM relevance | Uganda reported 190 human deaths in 2021–2024 and identified weak surveillance/PEP scarcity as drivers of a “cycle of neglect,” supporting integrated bite case management as a practical One Health response (okech2025participatoryapproachin pages 1-2) | Okech, 2025 | *Frontiers in Tropical Diseases* | https://doi.org/10.3389/fitd.2025.1662211 | Surveillance systems / implementation research |


*Table: This table summarizes major recent rabies findings across burden, prevention, diagnostics, and implementation. It is useful as a compact evidence map for building a disease knowledge base entry.*

---

## 1. Disease information
### 1.1 Concise overview
Rabies is a vaccine-preventable zoonotic viral disease causing acute, progressive encephalitis/encephalomyelitis. Infection is typically acquired when virus-containing saliva from a rabid animal contacts broken skin or mucosal surfaces, most often via a bite. (kaye2024rabiesvaccinefor pages 1-2)

### 1.2 Key identifiers (knowledge-base readiness)
* **MONDO ID:** Not available from the currently retrieved primary sources; must be mapped from an ontology resource (e.g., MONDO, MeSH) outside the present evidence set.
* **MeSH / ICD-10 / ICD-11:** Not directly retrievable from the currently retrieved texts; needs dedicated ontology/database lookup.

### 1.3 Synonyms / alternative names
* “Rabies”
* “Rabies encephalitis” / “rabies encephalomyelitis” (clinical description in reviews). (kaye2024rabiesvaccinefor pages 1-2)

### 1.4 Source of information
This report is based on **aggregated disease-level resources** (systematic reviews, national program analyses, modeling studies) and **primary clinical/immunology studies** rather than EHR-derived patient cohorts, except where specific case reports are included (e.g., a fatal PEP failure case report). (ghosh2024rabiescontrolin pages 1-2, holzbauer2023fatalhumanrabies pages 3-4)

---

## 2. Etiology
### 2.1 Disease causal factors
* **Infectious cause:** Rabies virus (RABV), a bullet-shaped, negative-sense ssRNA virus in *Rhabdoviridae*; described as a “neurotropic RNA virus.” (kaye2024rabiesvaccinefor pages 1-2, kaye2024rabiesvaccinefor pages 4-7)

### 2.2 Transmission and exposure ecology
* Primary transmission occurs via **bites** and exposure to infected saliva through **mucosal membranes or broken skin**. (kaye2024rabiesvaccinefor pages 1-2)
* In endemic settings, **dogs are the dominant reservoir and driver of human infection**; multiple sources reiterate that dog bites account for **>99%** of human rabies deaths/cases. (das2025globalperspectiveson pages 1-2, okech2025participatoryapproachin pages 1-2, ghosh2024rabiescontrolin pages 1-2)

### 2.3 Risk factors
**Exposure-related**
* Bite location and severity (head/neck/face; multiple wounds; highly innervated sites such as fingers/face) are repeatedly over-represented among fatal “breakthrough” infections despite PEP. (whitehouse2023humanrabiesdespite pages 1-3, whitehouse2023humanrabiesdespite pages 4-6)

**Health-system related (implementation risk factors)**
* Inadequate wound washing knowledge/practice and **vaccine/RIG stockouts** are documented barriers in elimination programs and increase the likelihood of missed or incomplete PEP. For example, in a Kenya case study, **73%** of facilities had human rabies vaccine stock-outs and only **19%** had both vaccine and RIG. (mwanyalu2025documentingchallengesin pages 1-2)

**Host-related**
* Immunocompromise may contribute to rare PEP failures. A U.S. case report of fatal rabies after prompt ACIP-recommended PEP described no neutralizing antibodies by RFFIT and possible underlying immunodeficiency (IgM MGUS with reduced IgA/IgG). (holzbauer2023fatalhumanrabies pages 3-4)

### 2.4 Protective factors
* **Prompt and correct PEP** (wound cleansing + vaccine ± passive immunization for severe exposures) is highly protective at the population level and is the central preventive intervention described across public health and clinical sources. (kaye2024rabiesvaccinefor pages 1-2, mwanyalu2025documentingchallengesin pages 1-2)
* **Mass dog vaccination** achieving high coverage is protective at the population level by interrupting dog-to-dog transmission and reducing human exposures. (ghosh2024rabiescontrolin pages 1-2)

### 2.5 Gene–environment interactions
Rabies is not primarily a genetic disease; gene–environment interactions are not well-defined in the retrieved evidence. Rare apparent PEP failures likely reflect a combination of **exposure intensity/anatomy + host immune status + care delivery factors** rather than a known host genetic predisposition. (whitehouse2023humanrabiesdespite pages 1-3, holzbauer2023fatalhumanrabies pages 3-4)

---

## 3. Phenotypes (clinical presentation)
### 3.1 Core clinical phenotypes
From a 2024 narrative review, typical clinical features include a prodrome (fever, headache, fatigue) progressing to encephalomyelitis with hydrophobia and aerophobia; the review reports hydrophobia in ~80% and paralytic rabies in ~20%. (kaye2024rabiesvaccinefor pages 1-2)

**Suggested HPO terms (examples; require final confirmation against HPO):**
* Hydrophobia (HP term to be mapped)
* Aerophobia (HP term to be mapped)
* Fever (HP:0001945)
* Headache (HP:0002315)
* Encephalitis (HP:0002383)
* Paralysis (HP:0003470)
* Dysphagia (HP:0002015)
* Agitation / behavioral change (HPO mapping required)

### 3.2 Natural history and temporal development
A 2024 review describes five stages: **incubation (days to years), prodrome, acute neurologic illness, coma, death**. (kaye2024rabiesvaccinefor pages 1-2)

**Notable 2023 update (breakthrough cases):** In fatal breakthrough infections after PEP, median time from exposure to symptom onset was **20 days (IQR 16–24)**, reflecting very short incubation in many high-risk exposures. (whitehouse2023humanrabiesdespite pages 1-3)

### 3.3 Quality of life impact
Rabies causes severe neuropsychiatric and neurologic symptoms culminating in coma and death; quality-of-life instruments are not reported in the retrieved sources. Impact is inferred as profound due to near-universal fatality after symptom onset. (kaye2024rabiesvaccinefor pages 1-2)

---

## 4. Genetic / molecular information
Rabies is caused by a viral pathogen rather than human germline variants.

### 4.1 “Causal genes” / variants (human)
Not applicable as a primary etiology in the retrieved evidence.

### 4.2 Viral molecular targets relevant to prevention/therapy
* Rabies virus **glycoprotein G** is the major neutralization target, underpinning vaccine-induced and passive antibody protection, and is the target of mAbs discussed as RIG alternatives. (chen2025circulatingantibody’srole pages 12-13)

---

## 5. Environmental information
Key environmental/lifestyle contributors in the retrieved evidence relate primarily to:
* **Dog ecology and free-roaming dog density** (relevant to sustained transmission and outbreaks). (beron2024dogmediatedrabiesvirus pages 1-3)
* **Resource limitations and conflict/poverty** that influence vaccine access, surveillance, and program performance (e.g., stockouts, underreporting). (mwanyalu2025documentingchallengesin pages 1-2, bonaparte2023evaluationofcountry pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (high-level)
1. **Exposure/inoculation** via bite/saliva →
2. Local replication and entry into peripheral nerves →
3. Neuroinvasion and spread within the CNS →
4. Progressive encephalitis/encephalomyelitis →
5. Coma and death.

A 2024 narrative review attributes death to “a massive inflammatory response in the CNS.” (kaye2024rabiesvaccinefor pages 1-2)

### 6.2 Immune evasion / immune response (current themes)
* The 2024 review frames a major research target as “preventing the virus from evading the host’s innate immune response.” (kaye2024rabiesvaccinefor pages 4-7)

### 6.3 Suggested ontology terms
**GO Biological Process (examples; to be curated):**
* innate immune response (GO:0045087)
* inflammatory response (GO:0006954)
* response to virus (GO:0009615)

**Cell Ontology (CL) likely involved:**
* neurons (CL:0000540)
* microglia (CL:0000129)
* astrocytes (CL:0000127)

**UBERON anatomical structures:**
* brain (UBERON:0000955)
* spinal cord (UBERON:0002240)
* peripheral nerve (UBERON:0001021)

### 6.4 Advanced technologies / recent developments
A 2024 review discusses exploratory approaches (e.g., CRISPR/Cas9, iPSC-based strategies) and AAV delivery as research directions, but these are not yet established clinical interventions for rabies. (kaye2024rabiesvaccinefor pages 4-7)

---

## 7. Anatomical structures affected
* **Primary system:** Central nervous system (encephalitis/encephalomyelitis). (kaye2024rabiesvaccinefor pages 1-2)
* **Anatomical correlates of risk:** Exposures to highly innervated sites (e.g., face/fingers) are associated with short incubation and higher risk even with PEP. (whitehouse2023humanrabiesdespite pages 4-6)

---

## 8. Temporal development
* Typical incubation is described as **days to years** (broad range) in a 2024 narrative review; in contrast, breakthrough infections after PEP show **very short incubation** with median 20 days. (kaye2024rabiesvaccinefor pages 1-2, whitehouse2023humanrabiesdespite pages 1-3)

---

## 9. Inheritance and population
### 9.1 Epidemiology (recent data)
**Global**
* Bangladesh analysis provides a clear statement: “Rabies… kills an estimated **59,000** people each year worldwide” and notes that “over **29 million** individuals worldwide receive post-exposure prophylaxis (PEP)… resulting… [in] economic loss of **US$ 8.6 billion**.” (Published Aug 2024; https://doi.org/10.1016/j.lansea.2024.100452) (ghosh2024rabiescontrolin pages 1-2)

**Global estimates with uncertainty / program monitoring**
* A 2023 modeling study (STOP-R) estimated **40,111** deaths in 2022 (95% CI 25,854–74,344) in dog-mediated rabies virus variant endemic countries, projected to **32,349** by 2030 (95% CI 21,110–57,019). (Published 09 May 2023; https://doi.org/10.3389/fvets.2023.1147543) (bonaparte2023evaluationofcountry pages 1-2, bonaparte2023evaluationofcountry pages 6-7)

**Regional distribution**
* Multiple sources emphasize highest burden in **Asia and Africa**. (blumberg2024eliminationofdogmediated pages 1-2, ghosh2024rabiescontrolin pages 1-2)

### 9.2 Population demographics
* Many sources highlight disproportionate burden in children; however, quantitative child-specific fractions are not consistently available in the 2023–2024 sources retrieved here.

---

## 10. Diagnostics
### 10.1 Current diagnostic concepts
* Postmortem diagnosis has historically relied on **direct fluorescent antibody testing (DFAT) on brain tissue** as a gold standard comparator, but performance varies across studies. (candiapuma2025evaluatingrabiestest pages 2-4, candiapuma2024rabiestestaccuracy pages 12-14)
* Antemortem diagnosis can use **RT-PCR** detection of viral RNA from **saliva, CSF, and tissue samples**. (candiapuma2025evaluatingrabiestest pages 2-4)

### 10.2 Recent quantitative diagnostic accuracy synthesis (2025)
A 2025 systematic review/meta-analysis reported:
* **Human ELISA** (8 studies; n=2,837): sensitivity range 85.9–99.9% (median **90.5%**), specificity range 69.0–99.8% (median **95.0%**). (https://doi.org/10.3390/diagnostics15040412; published Feb 2025) (candiapuma2025evaluatingrabiestest pages 8-9)
* **Human RT-PCR** (5 studies; n=456): sensitivity range 87.5–95.5% (median **94.4%**), specificity range 83.3–99.8% (median **97.7%**). (candiapuma2025evaluatingrabiestest pages 9-12)
* The same review documents use of specimen types including **serum, saliva, CSF, skin, oral swab, hair, and cornea** across studies, reflecting multi-specimen strategies for antemortem diagnosis. (candiapuma2025evaluatingrabiestest pages 8-9)

**Important limitation:** specimen-specific antemortem performance for nuchal skin biopsy vs saliva vs CSF is not fully extractable from the provided excerpts; individual-study review would be required for test-by-specimen operating characteristics. (candiapuma2025evaluatingrabiestest pages 8-9, candiapuma2025evaluatingrabiestest pages 2-4)

---

## 11. Outcome / prognosis
* Once symptomatic, rabies has a near-100% case fatality, which is repeatedly emphasized in reviews and public-health analyses. (kaye2024rabiesvaccinefor pages 1-2, ghosh2024rabiescontrolin pages 1-2)

### 11.1 Breakthrough infections despite PEP (2023 systematic review)
A 2023 *Lancet Infectious Diseases* systematic review (published May 2023; https://doi.org/10.1016/S1473-3099(22)00641-7) identified **122** fatal breakthrough infections (1980–2022) after receipt of modern cell-culture vaccine before symptom onset. Deviations from core PEP practices were present in **56%** of cases, severe wound patterns were common, and median incubation was **20 days**. (whitehouse2023humanrabiesdespite pages 1-3)

---

## 12. Treatment
### 12.1 Standard of care (prevention-focused)
* A 2024 narrative review states that PEP includes **wound cleaning, human rabies immunoglobulin (HRIG), and inactivated rabies vaccines**. (kaye2024rabiesvaccinefor pages 1-2)

### 12.2 ACIP (U.S.) PrEP schedule (guideline-based)
* ACIP 2022 recommends a **2-dose IM pre-exposure series** (days **0 and 7**) for risk categories 1–4 (e.g., laboratory workers with live virus, frequent bat handlers, veterinarians, and certain travelers). (Published May 2022; https://doi.org/10.15585/mmwr.mm7118a2) (rao2022useofa media 7550c3e2)

### 12.3 Passive immunization: RIG and mAbs (latest research direction)
* A 2025 review summarizes that modern mAb cocktails are designed to meet WHO expectations of binding **two or more non-overlapping epitopes** on glycoprotein G and reports markedly higher early circulating antibody levels than HRIG in referenced studies (e.g., “over 10 times higher than that of HRIG” by day 1 for a cited mAb combination). (Published Jul 2025; https://doi.org/10.3390/vaccines13070775) (chen2025circulatingantibody’srole pages 12-13)

**Clinical trials (pipeline evidence):** Multiple interventional trials exist evaluating rabies immune globulins and mAbs in simulated or real PEP contexts, including SYN023 programs and other candidates (e.g., NCT04644484; NCT03961555). (NCT04644484 chunk 1/2; NCT03961555 chunk 1/2/3)

### 12.4 Treatment outcomes: immunogenicity after PEP (2024 primary data)
A prospective immunology study in Cambodia assessed immunity for 12 months after a WHO-recommended, vaccine-sparing IPC intradermal PEP regimen:
* At day 14, “**all except two individuals seroconverted**” for neutralizing antibodies ≥0.5 IU/mL, and **87%** maintained ≥0.5 IU/mL at 12 months. (Published Nov 2024; https://doi.org/10.1038/s41541-024-01030-8) (ya2024evaluationofone pages 2-3)
* Median neutralizing antibody titers were 0.05 IU/mL at day 7 and 3.38 IU/mL at day 14; titers remained near/above the protective threshold at month 6 and month 12. (ya2024evaluationofone pages 2-3)

**MAXO suggestions (examples):**
* Rabies post-exposure prophylaxis (MAXO mapping required)
* Rabies vaccination (MAXO mapping required)
* Passive immunization (rabies immunoglobulin / monoclonal antibody) (MAXO mapping required)

---

## 13. Prevention
### 13.1 Primary prevention
* **Mass dog vaccination** is repeatedly emphasized; achieving **70% coverage** in annual pulse vaccination campaigns is expected to substantially reduce dog rabies and thereby human rabies. (ghosh2024rabiescontrolin pages 1-2)

### 13.2 Secondary prevention
* **PEP after exposure**: prompt wound care and vaccination are central. Bangladesh’s national analysis reiterates massive PEP utilization globally: “over **29 million** individuals worldwide receive post-exposure prophylaxis (PEP).” (ghosh2024rabiescontrolin pages 1-2)

### 13.3 Public health implementation (real-world)
* Bangladesh: national One Health program analysis supports that increases in mass dog vaccination and anti-rabies vaccine (human) correlate with declining human rabies risk, suggesting feasibility of progress toward “Zero by 30.” (ghosh2024rabiescontrolin pages 1-2)
* Kenya (Lamu): persistent stockouts and health worker knowledge gaps demonstrate operational constraints that directly undermine timely PEP and elimination targets. (mwanyalu2025documentingchallengesin pages 1-2)

---

## 14. Other species / natural disease
* Rabies (lyssavirus infections) affects **warm-blooded vertebrates**; dogs are emphasized as the only domestic animal functioning as reservoir, vector, and victim, whereas other domestic species are spillover/bellwethers. (https://doi.org/10.3390/pathogens14060586; published Jun 2025) (candiapuma2025evaluatingrabiestest pages 17-19)

---

## 15. Model organisms
This report’s retrieved sources focus on clinical/public-health and do not comprehensively enumerate model systems. However, a 2024 narrative review describes multiple preclinical approaches including mouse studies of combination therapies and immunomodulation, and exploratory gene-therapy concepts (e.g., AAV-mediated RNAi). (kaye2024rabiesvaccinefor pages 4-4)

---

# Expert interpretation and synthesis (authoritative analysis)
1. **The primary scientific bottleneck is not vaccine efficacy but delivery fidelity.** The 2023 systematic review of fatal breakthrough infections found that in **56%** of reported deaths there were deviations from core PEP practices, and RIG administration errors (e.g., absent RIG, IM-only RIG without wound infiltration) were common. This supports the expert consensus that “failures” are frequently system/implementation failures rather than intrinsic biologic failure. (whitehouse2023humanrabiesdespite pages 1-3, whitehouse2023humanrabiesdespite pages 4-6)
2. **Program evaluation is moving toward measurable capacity indices and implementation science.** STOP-R (2023) illustrates an approach to infer rabies burden and elimination capacity from country-level infrastructure metrics, addressing surveillance gaps that limit direct measurement. (bonaparte2023evaluationofcountry pages 1-2)
3. **Vaccine-sparing intradermal regimens can yield durable immunity, supporting scale-up in resource-limited settings.** The NPJ Vaccines 2024 immunology study shows robust neutralizing antibody responses and persistence (87% ≥0.5 IU/mL at 12 months) under a shortened regimen, relevant where PEP cost/access limits completion. (ya2024evaluationofone pages 2-3)
4. **Diagnostics are modernizing toward molecular/immunologic methods, but evidence heterogeneity remains.** A 2025 meta-analysis supports high median performance for human RT-PCR and ELISA, while emphasizing variability and the need for protocol modernization and antemortem access. (candiapuma2025evaluatingrabiestest pages 8-9, candiapuma2025evaluatingrabiestest pages 14-16)

---

# Evidence gaps / not fully resolved from retrieved sources
* **Ontology identifiers** (MONDO, MeSH, ICD-10/11) could not be extracted from the current evidence set and require targeted database lookup.
* **Specimen-specific antemortem diagnostic accuracy** (e.g., nuchal skin biopsy vs saliva vs CSF) is not fully extractable from the provided excerpts.
* **Comprehensive HPO/GO/CL/MAXO mappings** require dedicated ontology queries; suggestions above are plausible but should be validated.

---

# Key URLs and publication dates (from retrieved sources)
* Ghosh et al., *Lancet Regional Health – Southeast Asia* (Aug 2024): https://doi.org/10.1016/j.lansea.2024.100452 (ghosh2024rabiescontrolin pages 1-2)
* Ya et al., *NPJ Vaccines* (Nov 2024): https://doi.org/10.1038/s41541-024-01030-8 (ya2024evaluationofone pages 1-2)
* Whitehouse et al., *Lancet Infectious Diseases* (May 2023): https://doi.org/10.1016/S1473-3099(22)00641-7 (whitehouse2023humanrabiesdespite pages 1-3)
* Bonaparte et al., *Frontiers in Veterinary Science* (09 May 2023): https://doi.org/10.3389/fvets.2023.1147543 (bonaparte2023evaluationofcountry pages 1-2)
* Rao et al., ACIP PrEP recommendations, *MMWR* (May 2022): https://doi.org/10.15585/mmwr.mm7118a2 (rao2022useofa media 7550c3e2)
* Candia-Puma et al., *Diagnostics* (Feb 2025): https://doi.org/10.3390/diagnostics15040412 (candiapuma2025evaluatingrabiestest pages 9-12)


References

1. (kaye2024rabiesvaccinefor pages 1-2): Alan D Kaye, Dominique M Perilloux, Elizabeth Field, Cody A Orvin, Spencer C Zaheri, William C Upshaw, Raju Behara, Tomasina Q Parker-Actlis, Adam M Kaye, Shahab Ahmadzadeh, Sahar Shekoohi, and Giustino Varrassi. Rabies vaccine for prophylaxis and treatment of rabies: a narrative review. Cureus, Jun 2024. URL: https://doi.org/10.7759/cureus.62429, doi:10.7759/cureus.62429. This article has 20 citations.

2. (bonaparte2023evaluationofcountry pages 1-2): Sarah C. Bonaparte, Janae Moodie, Eduardo A. Undurraga, and Ryan M. Wallace. Evaluation of country infrastructure as an indirect measure of dog-mediated human rabies deaths. Frontiers in Veterinary Science, May 2023. URL: https://doi.org/10.3389/fvets.2023.1147543, doi:10.3389/fvets.2023.1147543. This article has 20 citations and is from a peer-reviewed journal.

3. (ghosh2024rabiescontrolin pages 1-2): Sumon Ghosh, Mohammad Nayeem Hasan, Nirmalendu Deb Nath, Najmul Haider, Daleniece Higgins Jones, Md. Kamrul Islam, M. Mujibur Rahaman, Hasan Sayedul Mursalin, Nadim Mahmud, Md. Kamruzzaman, Md. Fazlay Rabby, Shotabdi Kar, Sayed Mohammed Ullah, Md. Rashed Ali Shah, Afsana Akter Jahan, Md. Sohel Rana, Sukanta Chowdhury, Md. Jamal Uddin, Thankam S. Sunil, Be-Nazir Ahmed, Umme Ruman Siddiqui, S.M. Golam Kaisar, and Md. Nazmul Islam. Rabies control in bangladesh and prediction of human rabies cases by 2030: a one health approach. The Lancet Regional Health - Southeast Asia, 27:100452, Aug 2024. URL: https://doi.org/10.1016/j.lansea.2024.100452, doi:10.1016/j.lansea.2024.100452. This article has 16 citations.

4. (ya2024evaluationofone pages 1-2): Nisa Ya, Heidi Auerswald, Sothy Touch, Saraden In, Chanvannak Yun, Pisey Thai, Sotheary Sann, Borita Heng, Chanthy Leng, Veasna Duong, Yik Sing Peng, Sowath Ly, and Tineke Cantaert. Evaluation of one year immunity following rabies post-exposure prophylaxis in dog bite cases. NPJ Vaccines, Nov 2024. URL: https://doi.org/10.1038/s41541-024-01030-8, doi:10.1038/s41541-024-01030-8. This article has 4 citations and is from a peer-reviewed journal.

5. (chen2025circulatingantibody’srole pages 12-13): Qingjun Chen, Li Cai, Xinjun Lv, Si Liu, Cheng Liu, Jiayang Liu, Xiaoqiang Liu, Chuanlin Wang, Zhenggang Zhu, and Wenwu Yin. Circulating antibody’s role during post-exposure prophylaxis, and beyond for rabies: a review. Vaccines, Jul 2025. URL: https://doi.org/10.3390/vaccines13070775, doi:10.3390/vaccines13070775. This article has 0 citations.

6. (mwanyalu2025documentingchallengesin pages 1-2): Nassoro Mwanyalu, Athman Mwatondo, Veronicah Chuchu, Kimani Maina, Mathew Muturi, Mathew Mutiiria, Daniel Chepkwony, Maurice Owiny, and Peninah Munyua. Documenting challenges in achieving rabies elimination by 2030 in low-middle income countries; a kenyan case study from lamu county, 2020–2022: mixed methods approach. One Health Outlook, Feb 2025. URL: https://doi.org/10.1186/s42522-024-00129-1, doi:10.1186/s42522-024-00129-1. This article has 8 citations.

7. (okech2025participatoryapproachin pages 1-2): Samuel George Okech, Rabina Ghimire, Terence Odoch, Sonja Hartnack, Doreen Agado, Dickson Akankwatsa, Felister Apio, Priscilla Babirye, Stella Maris Lunkuse, Maria Flavia Nakanjako, John Opolot, Frederic Lohr, Juliet Kiguli, Clovice Kankya, Monique Lechenne, and Salome Dürr. Participatory approach in designing a one health rabies surveillance form for integrated bite case management in uganda. Frontiers in Tropical Diseases, Nov 2025. URL: https://doi.org/10.3389/fitd.2025.1662211, doi:10.3389/fitd.2025.1662211. This article has 0 citations.

8. (bonaparte2023evaluationofcountry pages 6-7): Sarah C. Bonaparte, Janae Moodie, Eduardo A. Undurraga, and Ryan M. Wallace. Evaluation of country infrastructure as an indirect measure of dog-mediated human rabies deaths. Frontiers in Veterinary Science, May 2023. URL: https://doi.org/10.3389/fvets.2023.1147543, doi:10.3389/fvets.2023.1147543. This article has 20 citations and is from a peer-reviewed journal.

9. (ya2024evaluationofone pages 2-3): Nisa Ya, Heidi Auerswald, Sothy Touch, Saraden In, Chanvannak Yun, Pisey Thai, Sotheary Sann, Borita Heng, Chanthy Leng, Veasna Duong, Yik Sing Peng, Sowath Ly, and Tineke Cantaert. Evaluation of one year immunity following rabies post-exposure prophylaxis in dog bite cases. NPJ Vaccines, Nov 2024. URL: https://doi.org/10.1038/s41541-024-01030-8, doi:10.1038/s41541-024-01030-8. This article has 4 citations and is from a peer-reviewed journal.

10. (ya2024evaluationofone pages 3-4): Nisa Ya, Heidi Auerswald, Sothy Touch, Saraden In, Chanvannak Yun, Pisey Thai, Sotheary Sann, Borita Heng, Chanthy Leng, Veasna Duong, Yik Sing Peng, Sowath Ly, and Tineke Cantaert. Evaluation of one year immunity following rabies post-exposure prophylaxis in dog bite cases. NPJ Vaccines, Nov 2024. URL: https://doi.org/10.1038/s41541-024-01030-8, doi:10.1038/s41541-024-01030-8. This article has 4 citations and is from a peer-reviewed journal.

11. (whitehouse2023humanrabiesdespite pages 1-3): Erin R Whitehouse, Anna Mandra, Jesse Bonwitt, Erin A Beasley, Joanna Taliano, and Agam K Rao. Human rabies despite post-exposure prophylaxis: a systematic review of fatal breakthrough infections after zoonotic exposures. The Lancet Infectious Diseases, 23:e167-e174, May 2023. URL: https://doi.org/10.1016/s1473-3099(22)00641-7, doi:10.1016/s1473-3099(22)00641-7. This article has 73 citations and is from a highest quality peer-reviewed journal.

12. (whitehouse2023humanrabiesdespite pages 4-6): Erin R Whitehouse, Anna Mandra, Jesse Bonwitt, Erin A Beasley, Joanna Taliano, and Agam K Rao. Human rabies despite post-exposure prophylaxis: a systematic review of fatal breakthrough infections after zoonotic exposures. The Lancet Infectious Diseases, 23:e167-e174, May 2023. URL: https://doi.org/10.1016/s1473-3099(22)00641-7, doi:10.1016/s1473-3099(22)00641-7. This article has 73 citations and is from a highest quality peer-reviewed journal.

13. (candiapuma2025evaluatingrabiestest pages 8-9): Mayron Antonio Candia-Puma, Leydi Pola-Romero, Haruna Luz Barazorda-Ccahuana, Luis Daniel Goyzueta-Mamani, Alexsandro Sobreira Galdino, Ricardo Andrez Machado-de-Ávila, Rodolfo Cordeiro Giunchetti, Eduardo Antonio Ferraz Coelho, and Miguel Angel Chávez-Fumagalli. Evaluating rabies test accuracy: a systematic review and meta-analysis of human and canine diagnostic methods. Diagnostics, 15:412, Feb 2025. URL: https://doi.org/10.3390/diagnostics15040412, doi:10.3390/diagnostics15040412. This article has 1 citations.

14. (candiapuma2025evaluatingrabiestest pages 2-4): Mayron Antonio Candia-Puma, Leydi Pola-Romero, Haruna Luz Barazorda-Ccahuana, Luis Daniel Goyzueta-Mamani, Alexsandro Sobreira Galdino, Ricardo Andrez Machado-de-Ávila, Rodolfo Cordeiro Giunchetti, Eduardo Antonio Ferraz Coelho, and Miguel Angel Chávez-Fumagalli. Evaluating rabies test accuracy: a systematic review and meta-analysis of human and canine diagnostic methods. Diagnostics, 15:412, Feb 2025. URL: https://doi.org/10.3390/diagnostics15040412, doi:10.3390/diagnostics15040412. This article has 1 citations.

15. (candiapuma2025evaluatingrabiestest pages 14-16): Mayron Antonio Candia-Puma, Leydi Pola-Romero, Haruna Luz Barazorda-Ccahuana, Luis Daniel Goyzueta-Mamani, Alexsandro Sobreira Galdino, Ricardo Andrez Machado-de-Ávila, Rodolfo Cordeiro Giunchetti, Eduardo Antonio Ferraz Coelho, and Miguel Angel Chávez-Fumagalli. Evaluating rabies test accuracy: a systematic review and meta-analysis of human and canine diagnostic methods. Diagnostics, 15:412, Feb 2025. URL: https://doi.org/10.3390/diagnostics15040412, doi:10.3390/diagnostics15040412. This article has 1 citations.

16. (candiapuma2025evaluatingrabiestest pages 9-12): Mayron Antonio Candia-Puma, Leydi Pola-Romero, Haruna Luz Barazorda-Ccahuana, Luis Daniel Goyzueta-Mamani, Alexsandro Sobreira Galdino, Ricardo Andrez Machado-de-Ávila, Rodolfo Cordeiro Giunchetti, Eduardo Antonio Ferraz Coelho, and Miguel Angel Chávez-Fumagalli. Evaluating rabies test accuracy: a systematic review and meta-analysis of human and canine diagnostic methods. Diagnostics, 15:412, Feb 2025. URL: https://doi.org/10.3390/diagnostics15040412, doi:10.3390/diagnostics15040412. This article has 1 citations.

17. (candiapuma2024rabiestestaccuracy pages 1-3): Mayron Antonio Candia-Puma, Leydi Pola-Romero, Haruna Luz Barazorda-Ccahuana, Luis Daniel Goyzueta-Mamani, Alexsandro Sobreira Galdino, Ricardo Andrez Machado-de-Ávila, Rodolfo Cordeiro Giunchetti, Eduardo Antonio Ferraz Coelho, and Miguel Angel Chávez-Fumagalli. Rabies test accuracy: comprehensive systematic review and meta-analysis for human and canine diagnostics. MedRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.05.24316773, doi:10.1101/2024.11.05.24316773. This article has 1 citations.

18. (candiapuma2024rabiestestaccuracy pages 12-14): Mayron Antonio Candia-Puma, Leydi Pola-Romero, Haruna Luz Barazorda-Ccahuana, Luis Daniel Goyzueta-Mamani, Alexsandro Sobreira Galdino, Ricardo Andrez Machado-de-Ávila, Rodolfo Cordeiro Giunchetti, Eduardo Antonio Ferraz Coelho, and Miguel Angel Chávez-Fumagalli. Rabies test accuracy: comprehensive systematic review and meta-analysis for human and canine diagnostics. MedRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.05.24316773, doi:10.1101/2024.11.05.24316773. This article has 1 citations.

19. (rao2022useofa media 7550c3e2): Agam K. Rao, Deborah Briggs, Susan M. Moore, Florence Whitehill, Doug Campos-Outcalt, Rebecca L. Morgan, Ryan M. Wallace, José R. Romero, Lynn Bahta, Sharon E. Frey, and Jesse D. Blanton. Use of a modified preexposure prophylaxis vaccination schedule to prevent human rabies: recommendations of the advisory committee on immunization practices — united states, 2022. MMWR. Morbidity and Mortality Weekly Report, 71:619-627, May 2022. URL: https://doi.org/10.15585/mmwr.mm7118a2, doi:10.15585/mmwr.mm7118a2. This article has 66 citations.

20. (blumberg2024eliminationofdogmediated pages 1-2): L. H. Blumberg. Elimination of dog-mediated human rabies: scientific tools, one health and partnerships. Revue Scientifique et Technique de l'OIE, Special Edition:70-73, Dec 2024. URL: https://doi.org/10.20506/rst.se.3560, doi:10.20506/rst.se.3560. This article has 1 citations.

21. (beron2024dogmediatedrabiesvirus pages 1-3): AJ Beron, R Keshavamurthy, C Boutelle, and R Wallace. Dog-mediated rabies virus transmission is driven by free-roaming dog density, haiti 2018–2023. Unknown journal, 2024.

22. (holzbauer2023fatalhumanrabies pages 3-4): Stacy M Holzbauer, Caroline A Schrodt, Rajesh M Prabhu, Rebecca J Asch-Kendrick, Malia Ireland, Carrie Klumb, Melanie J Firestone, Gongping Liu, Katie Harry, Jana M Ritter, Min Z Levine, Lillian A Orciari, Kimberly Wilkins, Pamela Yager, Crystal M Gigante, James A Ellison, Hui Zhao, Michael Niezgoda, Yu Li, Robin Levis, Dorothy Scott, Panayampalli S Satheshkumar, Brett W Petersen, Agam K Rao, W Robert Bell, Sonja M Bjerk, Sara Forrest, Wangcai Gao, Richard Dasheiff, Kari Russell, Melissa Pappas, Jessica Kiefer, Wesley Bickler, Anthony Wiseman, Joel Jurantee, R Ross Reichard, Kirk E Smith, Ruth Lynfield, Joni Scheftel, Ryan M Wallace, and Jesse Bonwitt. Fatal human rabies infection with suspected host-mediated failure of post-exposure prophylaxis following a recognized zoonotic exposure-minnesota, 2021. Clinical infectious diseases : an official publication of the Infectious Diseases Society of America, 77:1201-1208, Mar 2023. URL: https://doi.org/10.1093/cid/ciad098, doi:10.1093/cid/ciad098. This article has 18 citations.

23. (kaye2024rabiesvaccinefor pages 4-7): Alan D Kaye, Dominique M Perilloux, Elizabeth Field, Cody A Orvin, Spencer C Zaheri, William C Upshaw, Raju Behara, Tomasina Q Parker-Actlis, Adam M Kaye, Shahab Ahmadzadeh, Sahar Shekoohi, and Giustino Varrassi. Rabies vaccine for prophylaxis and treatment of rabies: a narrative review. Cureus, Jun 2024. URL: https://doi.org/10.7759/cureus.62429, doi:10.7759/cureus.62429. This article has 20 citations.

24. (das2025globalperspectiveson pages 1-2): Moumita Das, Valeriia Yustyniuk, Andres M. Perez, and Maria Sol Perez Aguirreburualde. Global perspectives on rabies control and elimination: a scoping review of dog owners’ knowledge, attitudes, and practices. Pathogens, 14:728, Jul 2025. URL: https://doi.org/10.3390/pathogens14080728, doi:10.3390/pathogens14080728. This article has 3 citations.

25. (candiapuma2025evaluatingrabiestest pages 17-19): Mayron Antonio Candia-Puma, Leydi Pola-Romero, Haruna Luz Barazorda-Ccahuana, Luis Daniel Goyzueta-Mamani, Alexsandro Sobreira Galdino, Ricardo Andrez Machado-de-Ávila, Rodolfo Cordeiro Giunchetti, Eduardo Antonio Ferraz Coelho, and Miguel Angel Chávez-Fumagalli. Evaluating rabies test accuracy: a systematic review and meta-analysis of human and canine diagnostic methods. Diagnostics, 15:412, Feb 2025. URL: https://doi.org/10.3390/diagnostics15040412, doi:10.3390/diagnostics15040412. This article has 1 citations.

26. (kaye2024rabiesvaccinefor pages 4-4): Alan D Kaye, Dominique M Perilloux, Elizabeth Field, Cody A Orvin, Spencer C Zaheri, William C Upshaw, Raju Behara, Tomasina Q Parker-Actlis, Adam M Kaye, Shahab Ahmadzadeh, Sahar Shekoohi, and Giustino Varrassi. Rabies vaccine for prophylaxis and treatment of rabies: a narrative review. Cureus, Jun 2024. URL: https://doi.org/10.7759/cureus.62429, doi:10.7759/cureus.62429. This article has 20 citations.
