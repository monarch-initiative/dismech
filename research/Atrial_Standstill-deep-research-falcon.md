---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T13:29:19.226250'
end_time: '2026-05-06T13:54:43.180669'
duration_seconds: 1523.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Atrial Standstill
  mondo_id: ''
  category: Heart Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Atrial Standstill
- **MONDO ID:**  (if available)
- **Category:** Heart Disorder

## Research Objectives

Please provide a comprehensive research report on **Atrial Standstill** covering all of the
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
- **Disease Name:** Atrial Standstill
- **MONDO ID:**  (if available)
- **Category:** Heart Disorder

## Research Objectives

Please provide a comprehensive research report on **Atrial Standstill** covering all of the
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


# Atrial Standstill — Comprehensive Disease Characteristics Research Report

**Target disease:** Atrial standstill (AS)  
**Category:** Heart disorder (arrhythmia / atrial cardiomyopathy)  
**Report scope:** Evidence is primarily from peer‑reviewed human case reports/families and focused cohorts/reviews. No EHR-derived aggregate datasets were retrieved in this run.

## Executive summary
Atrial standstill is a rare atrial arrhythmia/atrial myopathy defined by the **absence of atrial electrical activity and loss of atrial mechanical contraction**, producing **absent P waves**, atrial electrical silence on intracardiac recordings, and typically **junctional/escape bradycardia**. It can be **transient vs persistent/permanent** and **partial vs diffuse**, and may progress over time from focal right atrial involvement to biatrial electrical failure. AS may arise from **acquired/reversible causes** (e.g., hyperkalemia, drug toxicity, myocarditis/MI) or **genetic/syndromic atrial cardiomyopathies**, notably involving **SCN5A** and **EMD** among others. Clinically important complications include **thromboembolism/stroke** from atrial stasis and need for **permanent pacing**; contemporary real‑world reports demonstrate physiologic pacing approaches such as **left bundle branch area pacing (LBBAP)** in patients with AS and giant atria. (zheng2022leftbundlebranch pages 1-2, anand2024atrialstandstillin pages 1-3, agrawal2017persistentatrialstandstill pages 3-4, ishikawa2020cardiacemerinopathy pages 1-4)

---

## 1. Disease information

### 1.1 Overview and definition (current understanding)
Multiple sources converge on a core definition: atrial standstill is characterized by **absence of atrial electrical activity and atrial mechanical activity**. For example, a recent pacing case report states: **“Atrial standstill (AS) is a rare condition defined by the lack of atrial electrical and mechanical activities.”** (Frontiers in Cardiovascular Medicine; published **2022-03**, https://doi.org/10.3389/fcvm.2022.836964) (zheng2022leftbundlebranch pages 1-2). A noninvasive electrophysiology case report similarly defines it as total absence of atrial electrical activity in one or both atria and describes diagnostic confirmation via absent atrial mechanical contraction (Doppler “A” waves, etc.) (published **2017-03**, https://doi.org/10.1111/anec.12399) (agrawal2017persistentatrialstandstill pages 1-3, agrawal2017persistentatrialstandstill pages 3-4).

### 1.2 Key diagnostic concept
A practical set of diagnostic criteria is summarized in a 2024 case report: atrial standstill is characterized by **(1) absence of P waves**, **(2) narrow QRS**, **(3) evidence of atrial paralysis** (e.g., absent jugular venous “a” waves and absent Doppler A wave / tissue Doppler a′), and **(4) inability to stimulate/capture the atria** even with pacing (Journal of Arrhythmia; published **2024-09**, https://doi.org/10.1002/joa3.13150) (anand2024atrialstandstillin pages 1-3).

### 1.3 Synonyms / terminology
AS is described as **transient vs persistent (“permanent”)** and **partial vs total/diffuse**. A clinical review‑style case report explicitly notes classification “as transient (temporary) or persistent (also referred to as permanent)” and uses “partial atrial standstill” for one‑atrium or localized preservation of atrial activity (agrawal2017persistentatrialstandstill pages 1-3). A HeartRhythm Case Reports article also uses “permanent atrial standstill,” “partial atrial electrical standstill,” and “persistent atrial paralysis.” (suzuki2019acaseof pages 3-5)

### 1.4 Disease identifiers (ontology/coding)
The retrieved evidence contains an explicit Orphanet number and an OMIM reference, but **MONDO and MeSH identifiers were not retrieved**.

| Identifier system (Orphanet/ICD-10/OMIM/MeSH/MONDO/Other) | Code/ID | Label | Notes on evidence strength | Source (paper title, year) | URL |
|---|---|---|---|---|---|
| Orphanet | ORPHA:1344 | Atrial standstill | Reported in a classification table as an Orphanet identifier for atrial standstill; strongest explicit disease identifier found in retrieved evidence (podolec2019clinicalclassificationof pages 2-3) | *Clinical classification of rare cardiac arrhythmogenic and conduction disorders, and rare arrhythmias* (2019) | https://doi.org/10.20452/pamw.4451 |
| ICD-10 | I45.5 | Other specified heart block | Listed for atrial standstill as a **sample code** in the classification table; article notes some rare cardiac disorders are not referenced in ICD-10, so mapping should be treated cautiously (podolec2019clinicalclassificationof pages 2-3) | *Clinical classification of rare cardiac arrhythmogenic and conduction disorders, and rare arrhythmias* (2019) | https://doi.org/10.20452/pamw.4451 |
| OMIM | 108770 | Atrial standstill | OMIM number appears in a review of 1q21.1 CNVs that mentions “atrial standstill (OMIM 108770)”; indirect evidence rather than a primary disease ontology source in this conversation (podolec2019clinicalclassificationof pages 2-3) | *Prenatal phenotypes and pregnancy outcomes of fetuses with recurrent 1q21.1 microdeletions and microduplications* (2023) | https://doi.org/10.3389/fmed.2023.1207891 |
| MeSH |  | Not found in retrieved evidence | No explicit MeSH heading or ID for atrial standstill was retrieved in the available evidence (podolec2019clinicalclassificationof pages 2-3) | Not found in retrieved evidence |  |
| MONDO |  | Not found in retrieved evidence | No explicit MONDO identifier for atrial standstill was retrieved in the available evidence (podolec2019clinicalclassificationof pages 2-3) | Not found in retrieved evidence |  |
| Other | VI-1C-2 | Atrial standstill | Internal/clinical rare cardiac disease classification code (RCDD code), not a standard biomedical ontology identifier (podolec2019clinicalclassificationof pages 2-3) | *Clinical classification of rare cardiac arrhythmogenic and conduction disorders, and rare arrhythmias* (2019) | https://doi.org/10.20452/pamw.4451 |
| Other (synonym/terminology) |  | Atrial standstill (AS) | Standard abbreviation used across case reports/reviews; disease-level terminology rather than ontology identifier (zheng2022leftbundlebranch pages 1-2, kato2024atrialstandstilla pages 1-3) | *Left Bundle Branch Area Pacing in a Giant Atrium With Atrial Standstill* (2022); *Atrial Standstill: A Rare Cause of Pediatric Stroke and Management Strategies* (2024) | https://doi.org/10.3389/fcvm.2022.836964; https://doi.org/10.17264/stmarieng.15.21 |
| Other (synonym/terminology) |  | Persistent atrial standstill | Explicitly described as a persistent/permanent form in the literature; synonym reflects temporal subtype rather than distinct ontology code (agrawal2017persistentatrialstandstill pages 1-3, agrawal2017persistentatrialstandstill pages 3-4) | *Persistent atrial standstill following the Cox-maze III procedure* (2017) | https://doi.org/10.1111/anec.12399 |
| Other (synonym/terminology) |  | Permanent atrial standstill | Used interchangeably with persistent atrial standstill in retrieved evidence; terminology/synonym only (agrawal2017persistentatrialstandstill pages 1-3, suzuki2019acaseof pages 3-5) | *Persistent atrial standstill following the Cox-maze III procedure* (2017); *A case of atrial standstill with the atrial lead of a dual-chamber pacemaker implanted in the coronary sinus* (2019) | https://doi.org/10.1111/anec.12399; https://doi.org/10.1016/j.hrcr.2019.03.008 |
| Other (synonym/terminology) |  | Partial atrial standstill | Common term for regional/unilateral atrial involvement; descriptive subtype rather than separate coded disease (agrawal2017persistentatrialstandstill pages 1-3, makita2005congenitalatrialstandstill pages 1-2, suzuki2019acaseof pages 3-5) | *Persistent atrial standstill following the Cox-maze III procedure* (2017); *Congenital atrial standstill associated with coinheritance of a novel SCN5A mutation and connexin 40 polymorphisms* (2005); *A case of atrial standstill with the atrial lead of a dual-chamber pacemaker implanted in the coronary sinus* (2019) | https://doi.org/10.1111/anec.12399; https://doi.org/10.1016/j.hrthm.2005.06.032; https://doi.org/10.1016/j.hrcr.2019.03.008 |
| Other (synonym/terminology) |  | Persistent atrial paralysis | Alternate wording used in retrieved case literature; terminology/synonym only (suzuki2019acaseof pages 3-5) | *A case of atrial standstill with the atrial lead of a dual-chamber pacemaker implanted in the coronary sinus* (2019) | https://doi.org/10.1016/j.hrcr.2019.03.008 |


*Table: This table compiles disease identifiers and commonly used terminology for atrial standstill using only the retrieved evidence from the conversation. It distinguishes explicit ontology/code evidence from descriptive synonyms and flags weaker mappings such as sample ICD-10 codes.*

**Note on coding:** The ICD‑10 mapping for atrial standstill is not standardized in the retrieved evidence; one classification paper lists an ICD‑10 entry as a **sample code** and notes some rare cardiac disorders are not referenced in ICD‑10 (podolec2019clinicalclassificationof pages 2-3).

---

## 2. Etiology

### 2.1 Disease causal factors

#### 2.1.1 Genetic causes (primary atrial cardiomyopathy/channelopathy)
Evidence supports a heterogeneous genetic architecture, with strong data for **SCN5A** and for **EMD (emerin)** in a defined X‑linked syndrome.

- **SCN5A (Nav1.5)**: Familial congenital/progressive atrial standstill has been linked to loss‑of‑function SCN5A variants, sometimes with modifier effects from atrial gap junction variants.
  - Makita et al. (Heart Rhythm; **2005-10**, https://doi.org/10.1016/j.hrthm.2005.06.032) report a family with a novel **SCN5A p.Leu212Pro** and propose modifying effects of **connexin‑40 (GJA5)** polymorphisms (makita2005congenitalatrialstandstill pages 1-2).
  - Tan et al. (PACE; **2018-06**, https://doi.org/10.1111/pace.13386) report a **homozygous SCN5A p.Val1340Leu** variant with atrial standstill and sudden death risk, supported by patch‑clamp loss‑of‑function (tan2018ahomozygousscn5a pages 1-4).
- **EMD (emerin)**: Ishikawa et al. describe “cardiac emerinopathy,” a **nonsyndromic X‑linked** condition characterized by progressive atrial arrhythmias culminating in atrial standstill and associated with **LV noncompaction (LVNC)** and thromboembolism (Circulation: Arrhythmia and Electrophysiology; **2020-10**, https://doi.org/10.1161/circep.120.008712) (ishikawa2020cardiacemerinopathy pages 1-4).
- **HCN4**: A 2024 report links a novel HCN4 missense change with atrial standstill and ischemic stroke in a young patient (Journal of Arrhythmia; **2024-09**, https://doi.org/10.1002/joa3.13150) (anand2024atrialstandstillin pages 1-3).
- **CAV3**: A pediatric case report describes atrial standstill with a CAV3 p.Leu84Pro variant that was later reclassified as a VUS, emphasizing uncertainty for causality in this gene (HeartRhythm Case Reports; **2017-11**, https://doi.org/10.1016/j.hrcr.2017.07.014) (gal2017atrialstandstillin pages 1-2).

A structured gene/variant summary from the retrieved evidence is provided here:

| Gene (HGNC symbol) | Inheritance/zygosity (if described) | Variant (HGVS protein/cDNA or descriptor) | Evidence type (family/case report/cohort) | Key phenotypes/complications (stroke, LVNC, conduction disease) | Functional evidence (e.g., loss-of-function patch clamp) | Publication (year, journal) | URL |
|---|---|---|---|---|---|---|---|
| **SCN5A** | Familial; heterozygous in proband and father with incomplete penetrance; atrial phenotype modified by **GJA5** polymorphisms | **p.Leu212Pro (L212P)**; coinherited **GJA5/Cx40** polymorphisms as modifiers | Familial case report with electrophysiology and channel studies | Congenital/progressive atrial dysfunction to atrial standstill; absent P waves; right atrium not capturable by pacing; bradyarrhythmia/conduction disease; variable penetrance in family | Marked **loss-of-function** of Nav1.5 with hyperpolarizing shifts of activation/inactivation and delayed recovery; authors infer Cx40 polymorphisms may reduce atrial conduction reserve and modify phenotype (makita2005congenitalatrialstandstill pages 1-2) | Makita et al., **2005**, *Heart Rhythm* | https://doi.org/10.1016/j.hrthm.2005.06.032 |
| **SCN5A** | Familial; **homozygous** affected sisters, heterozygous relatives asymptomatic | **p.Val1340Leu (V1340L)** | Familial case report with segregation and patch clamp | Complete atrial standstill in proband, partial atrial standstill in sister; absent electrical/mechanical atrial activity; sudden death risk reported in family | **Loss-of-function** Nav1.5; reduced current density and depolarizing shift in steady-state activation (WT −35.3±1.62 mV vs V1340L −22.4±2.59 mV; P=0.001) (tan2018ahomozygousscn5a pages 1-4) | Tan et al., **2018**, *Pacing and Clinical Electrophysiology* | https://doi.org/10.1111/pace.13386 |
| **EMD** | **X-linked recessive**; affected male carriers, female carriers often asymptomatic | Start-loss, splicing, and missense **EMD** mutations (specific variants not detailed in retrieved evidence) | Targeted sequencing cohort plus family-based clinical characterization | Progressive atrial arrhythmias culminating in atrial standstill; **LVNC**; familial **stroke/thromboembolism** risk; conduction disease; need for pacemaker/defibrillator implantation | Genetic/segregation evidence; no patch-clamp assay reported in retrieved excerpt; mechanistic interpretation supports a nonsyndromic “cardiac emerinopathy” causing progressive atrial myopathy (ishikawa2020cardiacemerinopathy pages 1-4) | Ishikawa et al., **2020**, *Circulation: Arrhythmia and Electrophysiology* | https://doi.org/10.1161/circep.120.008712 |
| **HCN4** | **Autosomal dominant** familial inheritance described; heterozygous in reported patient/family | **c.2063A>C, p.Asn688Thr** | Case report with family history and multimodal cardiac evaluation | Atrial standstill in a young patient with **ischemic stroke**; absent atrial contraction; dilated right atrium; biatrial late gadolinium enhancement; familial sick sinus syndrome/conduction phenotype | No direct in vitro functional assay reported in retrieved excerpt; evidence includes segregation with familial sick sinus syndrome plus EP/MRI phenotype consistent with atrial paralysis (anand2024atrialstandstillin pages 1-3) | Anand et al., **2024**, *Journal of Arrhythmia* | https://doi.org/10.1002/joa3.13150 |
| **CAV3** | Not clearly established in retrieved evidence; pediatric single-case finding | **p.Leu84Pro (L84P)**; initially likely pathogenic, later reclassified as **VUS** | Pediatric case report | Atrial standstill with right atrial scar/electrical silence; inducible left atrial tachycardia; progressive inability to sense/capture atrium; ventricular pacing dependence; no stroke/LVNC reported in retrieved excerpt | No direct functional assay in retrieved excerpt; rarity noted (not observed in 6500 individuals in NHLBI GO Exome Sequencing Project), but causal role remains uncertain because variant was reclassified as VUS (gal2017atrialstandstillin pages 1-2) | Gal et al., **2017**, *HeartRhythm Case Reports* | https://doi.org/10.1016/j.hrcr.2017.07.014 |


*Table: This table summarizes key gene-level associations reported for atrial standstill in the retrieved evidence, including inheritance, variants, major clinical features, and available functional support. It is useful for distinguishing well-supported causal genes such as SCN5A and EMD from more tentative associations such as CAV3.*

#### 2.1.2 Acquired / potentially reversible causes
Case-based literature highlights multiple acquired triggers. Examples include **hyperkalemia**, **drug toxicity** (digoxin/digitalis, quinidine, verapamil, etc.), **reflex syncope**, and **acute myocardial infarction**, and inflammatory/infiltrative disease such as **amyloidosis**, **muscular dystrophies**, **systemic lupus**, and **cardiac sarcoidosis** (agrawal2017persistentatrialstandstill pages 3-4, suzuki2019acaseof pages 3-5, kim2016atrialstandstillin pages 1-2).

A notable mechanistic acquired example is suspected isolated **cardiac sarcoidosis**, where imaging (atrial LGE) and biopsy supported atrial fibrosis with inflammatory involvement associated with atrial electrical silence (Journal of Cardiology Cases; **2016-11**, https://doi.org/10.1016/j.jccase.2016.06.010) (kim2016atrialstandstillin pages 1-2).

### 2.2 Risk factors
**Risk factors in retrieved evidence** are largely etiologic categories rather than quantified epidemiologic risks:
- Underlying genetic cardiomyopathy/channelopathy (SCN5A; EMD; HCN4) (tan2018ahomozygousscn5a pages 1-4, ishikawa2020cardiacemerinopathy pages 1-4, anand2024atrialstandstillin pages 1-3)
- Systemic/infiltrative/inflammatory disorders (e.g., sarcoidosis, amyloidosis) (kim2016atrialstandstillin pages 1-2, agrawal2017persistentatrialstandstill pages 3-4)
- Metabolic or drug-related triggers (hyperkalemia; digoxin/digitalis; quinidine) (agrawal2017persistentatrialstandstill pages 3-4, suzuki2019acaseof pages 3-5)

### 2.3 Protective factors and gene–environment interactions
No protective genetic variants or robust gene–environment interaction analyses specific to atrial standstill were retrieved. Evidence is insufficient in this run.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum
Atrial standstill presents with a combination of electrical silence, mechanical failure, and downstream hemodynamic/thromboembolic consequences:
- **ECG:** absent P waves; junctional or ventricular escape rhythm/bradycardia (zheng2022leftbundlebranch pages 1-2, makita2005congenitalatrialstandstill pages 1-2, anand2024atrialstandstillin pages 1-3).
- **Echo Doppler:** absent transmitral/tricuspid A wave; absence of atrial contraction (agrawal2017persistentatrialstandstill pages 3-4, kato2024atrialstandstilla pages 1-3, zheng2022leftbundlebranch pages 1-2).
- **EP study:** inability to capture atria with pacing; atrial electrogram inactivity or markedly low voltage; residual activity may persist in limited regions (e.g., coronary sinus) (suzuki2019acaseof pages 1-3, suzuki2019acaseof pages 3-5).
- **Structural atrial disease:** atrial dilation/giant atrium, atrial fibrosis/scar (often inferred via low-voltage mapping or LGE on CMR) (zheng2022leftbundlebranch pages 1-2, anand2024atrialstandstillin pages 1-3, kim2016atrialstandstillin pages 1-2).
- **Complications:** thromboembolism/stroke risk due to blood stasis from absent contraction (kato2024atrialstandstilla pages 1-3, anand2024atrialstandstillin pages 1-3, ishikawa2020cardiacemerinopathy pages 1-4).

### 3.2 Phenotype-to-HPO mapping

| Phenotype/feature | Suggested HPO term (name and HP ID) | Notes |
|---|---|---|
| Absent P waves on surface ECG | Atrial standstill (HP:0011703) | Core electrical diagnostic feature of atrial standstill; reports describe no visible P waves on ECG, often with absent atrial electrograms as supportive EP evidence (agrawal2017persistentatrialstandstill pages 1-3, anand2024atrialstandstillin pages 1-3, zheng2022leftbundlebranch pages 1-2). |
| Junctional escape bradycardia / narrow-complex escape rhythm | Bradycardia (HP:0001662); Junctional rhythm (HP:0011675) | Typical rhythm disturbance when atrial activation is absent; often described as junctional or escape rhythm accompanying absent P waves (makita2005congenitalatrialstandstill pages 1-2, anand2024atrialstandstillin pages 1-3, zheng2022leftbundlebranch pages 1-2). |
| Atrial paralysis / no A wave on Doppler echocardiography | Atrial standstill (HP:0011703) | Mechanical criterion: absent atrial contraction shown by loss of A waves on mitral/tricuspid inflow Doppler, tissue Doppler a′, or jugular/pressure tracings (agrawal2017persistentatrialstandstill pages 3-4, anand2024atrialstandstillin pages 1-3, kato2024atrialstandstilla pages 1-3). |
| Inability to capture atrium on pacing / atrial inexcitability | Atrial standstill (HP:0011703) | EP criterion: failure to electrically stimulate/capture right atrium or coronary sinus even at high output; useful for confirming diagnosis and guiding lead strategy (suzuki2019acaseof pages 1-3, anand2024atrialstandstillin pages 1-3, kato2024atrialstandstilla pages 1-3). |
| Atrial dilation / giant atrium | Left atrial dilatation (HP:0001698); Right atrial dilatation (HP:0001719) | Structural atrial disease is common in reported cases, including giant atrium and marked right atrial dilation on echo/MRI (zheng2022leftbundlebranch pages 1-2, anand2024atrialstandstillin pages 1-3). |
| Thromboembolic ischemic stroke | Stroke (HP:0001297); Cerebral infarction (HP:0001296) | Important complication due to atrial blood stasis from absent contraction; reported in pediatric and young adult cases and used to justify anticoagulation (kato2024atrialstandstilla pages 1-3, anand2024atrialstandstillin pages 1-3, ishikawa2020cardiacemerinopathy pages 1-4). |
| Left ventricular noncompaction when present | Left ventricular noncompaction (HP:0006677) | Seen in syndromic/genetic forms, especially EMD-associated “cardiac emerinopathy,” and may compound thromboembolic risk (ishikawa2020cardiacemerinopathy pages 1-4). |


*Table: This table maps common atrial standstill clinical and diagnostic findings to suggested Human Phenotype Ontology terms. It is useful for structuring phenotype annotation in a disease knowledge base while preserving the diagnostic context from ECG, echocardiography, and electrophysiology studies.*

**Quality of life impact:** Not systematically quantified in retrieved evidence. However, symptomatic bradycardia, presyncope/syncope, heart failure manifestations, and stroke are repeatedly noted as major clinical impacts, often driving permanent pacing and anticoagulation decisions (zheng2022leftbundlebranch pages 1-2, anand2024atrialstandstillin pages 1-3, kato2024atrialstandstilla pages 1-3).

---

## 4. Genetic / molecular information

### 4.1 Causal genes and molecular classes
The retrieved literature supports several mechanistic classes:
- **Voltage-gated sodium channel dysfunction** (SCN5A loss-of-function) with impaired atrial excitability/conduction and progressive atrial electrical failure (tan2018ahomozygousscn5a pages 1-4, makita2005congenitalatrialstandstill pages 1-2).
- **Gap junction / conduction reserve modification** (GJA5 connexin‑40 polymorphisms proposed as modifiers in SCN5A families) (makita2005congenitalatrialstandstill pages 1-2).
- **Nuclear envelope / myocyte structural integrity disorders** (EMD, and broader laminopathy/EDMD context) causing progressive atrial myopathy leading to standstill and thromboembolism risk (ishikawa2020cardiacemerinopathy pages 1-4, valenti2022clinicalprofilearrhythmias pages 1-2).
- **Pacemaker channel association** (HCN4) in familial bradyarrhythmia syndromes with atrial standstill in a reported family (anand2024atrialstandstillin pages 1-3).

### 4.2 Variant interpretation and population frequency
Only limited population frequency information was retrieved directly: the CAV3 p.Leu84Pro variant was reported as not observed in 6500 individuals in the NHLBI GO Exome Sequencing Project but was later reclassified as a VUS, underscoring the need for cautious interpretation (gal2017atrialstandstillin pages 1-2). Broader allele-frequency statistics (e.g., gnomAD) were not retrieved in this run.

---

## 5. Environmental information
Evidence in this run is primarily clinical; nevertheless, **non-genetic contributors** include metabolic derangement (hyperkalemia), drug toxicity (digitalis/quinidine), hypoxia, and ischemic/inflammatory myocardial conditions (myocarditis, MI, sarcoidosis) reported as associated causes/precipitants (agrawal2017persistentatrialstandstill pages 3-4, suzuki2019acaseof pages 3-5, kim2016atrialstandstillin pages 1-2).

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (integrated model)
A consistent disease model across genetic and acquired contexts is:

**Trigger/primary substrate** (channelopathy; nuclear envelope myopathy; infiltrative/inflammatory disease; metabolic/drug injury) → **atrial myocyte dysfunction and/or structural remodeling** → **atrial fibrosis/scar with low-voltage substrate** → **loss of atrial excitability and conduction** (electrical silence; inability to pace-capture) → **loss of atrial mechanical contraction** (absent Doppler A waves) → **blood stasis** → **thromboembolism/stroke**; in parallel, **junctional/escape rhythms and bradycardia** drive symptoms and pacing need. Evidence for atrial fibrosis/structural disease (e.g., LGE in both atria) and electrical silence is reported in sarcoidosis-associated AS and in genetic cases with biatrial LGE (kim2016atrialstandstillin pages 1-2, anand2024atrialstandstillin pages 1-3).

### 6.2 Upstream vs downstream mechanisms
- **Upstream:** genetic loss-of-function in excitability genes (SCN5A), structural myocyte-nuclear coupling defects (EMD), or inflammatory infiltration (sarcoidosis) (tan2018ahomozygousscn5a pages 1-4, ishikawa2020cardiacemerinopathy pages 1-4, kim2016atrialstandstillin pages 1-2).
- **Downstream:** progressive atrial scarring/low-voltage substrate and eventual electrical silence; mechanical atrial paralysis; thromboembolism risk (suzuki2019acaseof pages 3-5, agrawal2017persistentatrialstandstill pages 3-4, kato2024atrialstandstilla pages 1-3).

### 6.3 Spatial progression and anatomical localization
Several reports describe progression beginning in the **high/midlateral right atrium** and spreading to the entire right atrium and then left atrium, with some patients retaining small islands of viable atrial tissue. A striking example is residual atrial electrical activity confined to the **coronary sinus**, enabling coronary-sinus atrial lead placement (suzuki2019acaseof pages 1-3, suzuki2019acaseof pages 3-5).

### 6.4 Suggested ontology terms for mechanisms (GO/CL/UBERON)
**UBERON (anatomy):**
- UBERON:0000948 (heart) — general
- UBERON:0002079 (right atrium) and UBERON:0002078 (left atrium) — atrial myocardium involvement
- UBERON:0002347 (coronary sinus) — residual atrial activity/pacing site in partial AS cases (suzuki2019acaseof pages 1-3)

**Cell Ontology (CL) (major involved cell types):**
- CL:0000746 (cardiac muscle cell / cardiomyocyte)
- CL:0002548 (cardiac fibroblast) — fibrosis substrate (mechanistic inference consistent with atrial fibrotic substrate discussed across sources)

**GO biological process (examples):**
- “cardiac muscle cell action potential” (GO:0086001)
- “regulation of heart rate” (GO:0002027)
- “cardiac conduction” (GO:0061337)
- “extracellular matrix organization” (GO:0030198)
- “fibroblast proliferation” (GO:0048144)

(These ontology suggestions are consistent with the electrophysiologic and fibrotic remodeling substrate described in the retrieved literature, although GO IDs are not explicitly cited in the sources.) (agrawal2017persistentatrialstandstill pages 3-4, kim2016atrialstandstillin pages 1-2, anand2024atrialstandstillin pages 1-3)

---

## 7. Anatomical structures affected
- **Primary organ:** heart, specifically **atrial myocardium** (right and/or left atrium) (agrawal2017persistentatrialstandstill pages 1-3, suzuki2019acaseof pages 3-5).
- **Potential focal sites of residual activity:** coronary sinus and limited atrial regions in partial AS (suzuki2019acaseof pages 1-3).
- **Secondary/systemic impact:** brain via **ischemic stroke** due to thromboembolism (anand2024atrialstandstillin pages 1-3, kato2024atrialstandstilla pages 1-3).

---

## 8. Temporal development
AS may be **intermittent or permanent** and **progressive**. Several sources describe progression from partial/focal atrial involvement to diffuse standstill, often with evolving atrial scarring and eventual atrial pacing failure risk (suzuki2019acaseof pages 3-5, agrawal2017persistentatrialstandstill pages 3-4). Recovery of atrial activity is possible in select contexts, including reports of reversal with sustained atrial/AV sequential pacing after surgery and recovery after months in a pediatric case (agrawal2017persistentatrialstandstill pages 1-3, kato2024atrialstandstilla pages 1-3).

---

## 9. Inheritance and population

### 9.1 Epidemiology
AS is consistently described as **rare**, but population prevalence/incidence estimates for atrial standstill overall were not retrieved.

A partial quantitative window comes from EDMD/laminopathy-focused systematic review data (not population-wide): in EDMD/cardiolaminopathies, the **incidence rate (IR) for atrial standstill ranged from 0 to 2 events per 100 patient-years** in the reviewed cohorts (Biology; published **2022-03**, https://doi.org/10.3390/biology11040530) (valenti2022clinicalprofilearrhythmias pages 1-2).

### 9.2 Inheritance patterns (genetic forms)
- **Autosomal dominant (variable penetrance):** HCN4 familial bradyarrhythmia/atrial standstill presentation and SCN5A family with incomplete penetrance (anand2024atrialstandstillin pages 1-3, makita2005congenitalatrialstandstill pages 1-2).
- **Autosomal recessive/biallelic effect:** Homozygous SCN5A p.Val1340Leu associated with atrial standstill and sudden death risk (tan2018ahomozygousscn5a pages 1-4).
- **X‑linked recessive:** EMD-associated “cardiac emerinopathy” with affected males requiring device therapy and asymptomatic female carriers reported (ishikawa2020cardiacemerinopathy pages 1-4).

---

## 10. Diagnostics

### 10.1 Clinical tests and diagnostic workflow (practical)
The contemporary case literature supports a multimodal workflow:
1) **ECG** (absent P waves; escape rhythm) (zheng2022leftbundlebranch pages 1-2)  
2) **Echocardiography with Doppler/TDI** (absent A wave; atrial dilation) (agrawal2017persistentatrialstandstill pages 3-4, anand2024atrialstandstillin pages 1-3)  
3) **Electrophysiology study / mapping** to confirm atrial inexcitability and identify residual viable tissue for lead placement (suzuki2019acaseof pages 1-3, suzuki2019acaseof pages 3-5)  
4) **Cardiac MRI with LGE** to assess atrial fibrosis and associated cardiomyopathy (biatrial LGE reported in genetic and inflammatory cases) (kim2016atrialstandstillin pages 1-2, anand2024atrialstandstillin pages 1-3)

A structured summary with MAXO-aligned intervention labels is provided here:

| Intervention/test | Suggested MAXO term (name and MAXO ID if known; otherwise leave blank) | Indication in atrial standstill | Evidence source |
|---|---|---|---|
| 12-lead electrocardiogram (ECG) | Electrocardiographic monitoring | First-line diagnostic test; typically shows absent P waves with junctional or ventricular escape rhythm/bradycardia, helping establish electrical atrial silence (agrawal2017persistentatrialstandstill pages 1-3, anand2024atrialstandstillin pages 1-3, zheng2022leftbundlebranch pages 1-2) | Agrawal et al., 2017, *Annals of Noninvasive Electrocardiology*; Anand et al., 2024, *Journal of Arrhythmia*; Zheng et al., 2022, *Frontiers in Cardiovascular Medicine* |
| Ambulatory ECG / Holter monitoring | Ambulatory electrocardiographic monitoring | Detects persistent bradyarrhythmia, pauses, junctional rhythm burden, and progression of atrial electrical inactivity; useful in symptomatic or pediatric cases (gal2017atrialstandstillin pages 1-2) | Gal et al., 2017, *HeartRhythm Case Reports* |
| Echocardiography with Doppler (mitral/tricuspid inflow, tissue Doppler) | Echocardiography | Demonstrates absent mechanical atrial contraction, especially loss of A waves on transmitral/tricuspid inflow or tissue Doppler; also assesses atrial dilation/giant atrium (agrawal2017persistentatrialstandstill pages 3-4, anand2024atrialstandstillin pages 1-3, kato2024atrialstandstilla pages 1-3, zheng2022leftbundlebranch pages 1-2) | Agrawal et al., 2017, *Annals of Noninvasive Electrocardiology*; Anand et al., 2024, *Journal of Arrhythmia*; Kato et al., 2024, *Journal of St. Marianna University*; Zheng et al., 2022, *Frontiers in Cardiovascular Medicine* |
| Electrophysiology (EP) study and electroanatomic mapping | Electrophysiologic study | Confirms atrial inexcitability when atria cannot be captured at high output; maps residual viable atrial tissue (often only coronary sinus or limited regions) and guides lead placement if atrial pacing is attempted (suzuki2019acaseof pages 1-3, anand2024atrialstandstillin pages 1-3, gal2017atrialstandstillin pages 1-2) | Suzuki et al., 2019, *HeartRhythm Case Reports*; Anand et al., 2024, *Journal of Arrhythmia*; Gal et al., 2017, *HeartRhythm Case Reports* |
| Cardiac magnetic resonance imaging (MRI) with late gadolinium enhancement (LGE) | Cardiac magnetic resonance imaging | Characterizes atrial cardiomyopathy/fibrosis and associated structural disease; in reported cases showed biatrial LGE, right atrial dilation, or LV noncompaction (anand2024atrialstandstillin pages 1-3, ishikawa2020cardiacemerinopathy pages 1-4) | Anand et al., 2024, *Journal of Arrhythmia*; Ishikawa et al., 2020, *Circulation: Arrhythmia and Electrophysiology* |
| Permanent pacemaker implantation: single-chamber ventricular pacemaker | Cardiac pacemaker implantation | Main symptomatic treatment for bradycardia/escape rhythm when atrial capture is absent or atrial lead placement fails; used in diffuse/persistent atrial standstill (zheng2022leftbundlebranch pages 1-2, gal2017atrialstandstillin pages 1-2) | Zheng et al., 2022, *Frontiers in Cardiovascular Medicine*; Gal et al., 2017, *HeartRhythm Case Reports* |
| Atrial lead implantation at residual excitable tissue (e.g., coronary sinus) when feasible | Cardiac pacemaker implantation | Considered in partial atrial standstill if viable atrial myocardium remains; EP mapping can identify coronary sinus or localized atrial sites suitable for sensing/capture (suzuki2019acaseof pages 1-3, agrawal2017persistentatrialstandstill pages 3-4) | Suzuki et al., 2019, *HeartRhythm Case Reports*; Agrawal et al., 2017, *Annals of Noninvasive Electrocardiology* |
| Physiologic pacing: left bundle branch area pacing (LBBAP) | Physiologic cardiac pacing | Alternative ventricular pacing strategy for patients needing permanent pacing, aiming to avoid dyssynchrony associated with right ventricular apical pacing; successfully implemented in atrial standstill with giant atrium (zheng2022leftbundlebranch pages 1-2, zheng2022leftbundlebranch media 3add666d) | Zheng et al., 2022, *Frontiers in Cardiovascular Medicine* |
| Anticoagulation for thromboembolism prevention | Anticoagulant therapy | Used because absent atrial contraction causes blood stasis and raises risk of thromboembolism/stroke; particularly relevant after ischemic stroke or with atrial standstill plus LVNC/atrial enlargement (kato2024atrialstandstilla pages 1-3, anand2024atrialstandstillin pages 1-3, ishikawa2020cardiacemerinopathy pages 1-4) | Kato et al., 2024, *Journal of St. Marianna University*; Anand et al., 2024, *Journal of Arrhythmia*; Ishikawa et al., 2020, *Circulation: Arrhythmia and Electrophysiology* |


*Table: This table summarizes the main diagnostic tests and management approaches reported for atrial standstill, including suggested MAXO-aligned intervention labels. It is useful for knowledge-base curation because it links each intervention to its clinical role and supporting source evidence.*

### 10.2 Differential diagnosis (high-level)
Within retrieved evidence, AS is contrasted clinically with atrial fibrillation in that AF has fibrillatory activity rather than true atrial electrical silence; EP recordings and inability to pace-capture support AS rather than AF (suzuki2019acaseof pages 1-3, anand2024atrialstandstillin pages 1-3).

---

## 11. Outcomes / prognosis
Outcome data are sparse and are primarily case-based, but several consistent risk themes emerge:
- **Thromboembolism/stroke risk:** 2024 pediatric/young adult cases emphasize that loss of atrial contraction “will likely cause blood flow stagnation in the atria” with highly prevalent thromboembolic complications in such settings, prompting anticoagulation strategies (kato2024atrialstandstilla pages 1-3, anand2024atrialstandstillin pages 1-3).
- **Need for chronic pacing:** symptomatic bradycardia is common, frequently requiring permanent pacing (zheng2022leftbundlebranch pages 1-2).
- **Progression / pacing failure risk:** progressive atrial disease can cause eventual atrial pacing failure, motivating careful follow-up and EP-guided lead strategies (suzuki2019acaseof pages 3-5, gal2017atrialstandstillin pages 1-2).

Quantitative cohort-level complication rates specific to atrial standstill (outside EDMD/laminopathy contexts) were not retrieved.

---

## 12. Treatment

### 12.1 Pharmacotherapy
No disease-specific pharmacologic reversal therapy is established in the retrieved evidence. However, **anticoagulation** is a recurring, real-world intervention for thromboembolism prevention:
- A 2024 HCN4-associated case states: **“The patient was started on anticoagulation therapy to prevent further thromboembolic events.”** (anand2024atrialstandstillin pages 1-3)
- A 2022 LBBAP case used **apixaban 2.5 mg bid** for embolism prevention (zheng2022leftbundlebranch pages 1-2).
- A pediatric stroke case used **edoxaban** for secondary prevention (kato2024atrialstandstilla pages 1-3).
- A post-surgical case used **warfarin** as postoperative medication (agrawal2017persistentatrialstandstill pages 1-3).

### 12.2 Device therapy (mainstay): pacemakers and lead strategies
Permanent pacing is repeatedly described as required for symptomatic bradycardia.

**Standard approaches in the case literature include:**
- **Single-chamber ventricular pacing** when atrial capture is absent or atrial lead placement fails (gal2017atrialstandstillin pages 1-2, zheng2022leftbundlebranch pages 1-2).
- **Dual-chamber pacing with atrial lead in coronary sinus** when residual atrial myocardium is present there, enabling AV sequential pacing (suzuki2019acaseof pages 3-5).
- **AV sequential pacing potentially reversing standstill** in select postoperative contexts (agrawal2017persistentatrialstandstill pages 1-3).

**Physiologic pacing development / real-world implementation:**
A notable technical development is the application of **left bundle branch area pacing (LBBAP)** in AS with a giant atrium. The 2022 case emphasizes avoidance of dyssynchrony associated with traditional RV apical pacing and reports successful LBBAP implantation with stable parameters; their figures show absent atrial activity and LBBAP capture characteristics (zheng2022leftbundlebranch media 3add666d).

### 12.3 Suggested MAXO terms (selected)
- Cardiac pacemaker implantation (MAXO ID not retrieved)
- Physiologic cardiac pacing (MAXO ID not retrieved)
- Anticoagulant therapy (MAXO ID not retrieved)

(IDs were not available in retrieved evidence; terms are provided for knowledge-base alignment.)

### 12.4 Experimental treatments / clinical trials
A ClinicalTrials.gov search did **not** retrieve atrial-standstill-specific trials. Related bradyarrhythmia physiologic pacing trials include **His bundle pacing** studies (e.g., **NCT03590353**, **NCT03685617**) in slow arrhythmias, which may be relevant to pacing strategy selection but are not AS-specific in the retrieved records.

---

## 13. Prevention
No atrial-standstill-specific primary prevention strategies were identified. Secondary/tertiary prevention in retrieved evidence centers on:
- **Stroke prevention via anticoagulation** in AS with atrial paralysis/large atria and/or prior stroke (anand2024atrialstandstillin pages 1-3, zheng2022leftbundlebranch pages 1-2, kato2024atrialstandstilla pages 1-3).
- **Monitoring atrial activity** for progression or recovery (kato2024atrialstandstilla pages 1-3).

---

## 14. Other species / natural disease
No veterinary or non-human natural disease evidence was retrieved for atrial standstill in this run.

---

## 15. Model organisms
No atrial-standstill-specific model organism studies were retrieved.

---

## Expert opinion and authoritative synthesis (interpretation grounded in retrieved sources)
Atrial standstill can be viewed as an **end-stage atrial cardiomyopathy phenotype** with a final common pathway of atrial fibrosis/low-voltage substrate and atrial paralysis, regardless of whether the upstream driver is genetic (e.g., SCN5A/EMD) or acquired (e.g., sarcoidosis, drug/metabolic injury). This framework is supported by mechanistic descriptions of progressive atrial electrogram loss, scarring, and atrial inexcitability in electrophysiology-focused case literature and by the EDMD/cardiolaminopathy systematic review emphasizing structured surveillance for atrial arrhythmias and thromboembolic prevention in high-risk genetic substrates (agrawal2017persistentatrialstandstill pages 3-4, suzuki2019acaseof pages 3-5, valenti2022clinicalprofilearrhythmias pages 1-2).

---

## Key evidence gaps (important for knowledge-base curation)
- **MONDO and MeSH IDs** for atrial standstill were not retrieved in this run; additional ontology-directed searches would be required for canonical identifiers.
- Population-level **prevalence/incidence** of atrial standstill in the general population was not retrieved; available quantitative rates are primarily within EDMD/laminopathy cohorts.
- Limited systematic data on **quality of life** and long-term outcomes outside case reports.

---

## Appendix: Visual evidence (example)
In the LBBAP case report, a figure panel demonstrates absence of atrial activity (no P waves) consistent with atrial standstill alongside pacing documentation, supporting the ECG-based definition and contemporary pacing implementation (zheng2022leftbundlebranch media 3add666d).


References

1. (zheng2022leftbundlebranch pages 1-2): Jingang Zheng, Qing-zhen Yang, Jia-sheng Zheng, Qiang Chen, and Qi Jin. Left bundle branch area pacing in a giant atrium with atrial standstill: a case report and literature review. Frontiers in Cardiovascular Medicine, Mar 2022. URL: https://doi.org/10.3389/fcvm.2022.836964, doi:10.3389/fcvm.2022.836964. This article has 3 citations and is from a peer-reviewed journal.

2. (anand2024atrialstandstillin pages 1-3): Abhinav B. Anand, Bhavik S. Shah, Girish R. Sabnis, and Ajay U. Mahajan. Atrial standstill in a young patient with ischemic stroke associated with inheritance of a novel hcn4 mutation. Journal of Arrhythmia, 40:1519-1522, Sep 2024. URL: https://doi.org/10.1002/joa3.13150, doi:10.1002/joa3.13150. This article has 2 citations and is from a peer-reviewed journal.

3. (agrawal2017persistentatrialstandstill pages 3-4): Harsh Agrawal, Kul Aggarwal, and Martin A. Alpert. Persistent atrial standstill following the cox‐maze iii procedure: reversal with sustained atrial pacing. Annals of Noninvasive Electrocardiology, 22:e12399, Mar 2017. URL: https://doi.org/10.1111/anec.12399, doi:10.1111/anec.12399. This article has 5 citations and is from a peer-reviewed journal.

4. (ishikawa2020cardiacemerinopathy pages 1-4): Taisuke Ishikawa, Hiroyuki Mishima, Julien Barc, Masanori P. Takahashi, Keiichi Hirono, Shigenori Terada, Shinya Kowase, Teruki Sato, Yasushi Mukai, Yoshiaki Yui, Kimie Ohkubo, Hiroki Kimoto, Hiroyuki Watanabe, Yukiko Hata, Takeshi Aiba, Seiko Ohno, Akiko Chishaki, Wataru Shimizu, Minoru Horie, Fukiko Ichida, Akihiko Nogami, Koh-Ichiro Yoshiura, Jean-Jacques Schott, and Naomasa Makita. Cardiac emerinopathy. Circulation: Arrhythmia and Electrophysiology, Oct 2020. URL: https://doi.org/10.1161/circep.120.008712, doi:10.1161/circep.120.008712. This article has 32 citations and is from a peer-reviewed journal.

5. (agrawal2017persistentatrialstandstill pages 1-3): Harsh Agrawal, Kul Aggarwal, and Martin A. Alpert. Persistent atrial standstill following the cox‐maze iii procedure: reversal with sustained atrial pacing. Annals of Noninvasive Electrocardiology, 22:e12399, Mar 2017. URL: https://doi.org/10.1111/anec.12399, doi:10.1111/anec.12399. This article has 5 citations and is from a peer-reviewed journal.

6. (suzuki2019acaseof pages 3-5): Yuya Suzuki, Asumi Takei, Hiroyuki Takahara, Yayoi Taniguchi, Toru Ozawa, and Nobutaka Inoue. A case of atrial standstill with the atrial lead of a dual-chamber pacemaker implanted in the coronary sinus. HeartRhythm Case Reports, 5:338-342, Jun 2019. URL: https://doi.org/10.1016/j.hrcr.2019.03.008, doi:10.1016/j.hrcr.2019.03.008. This article has 6 citations.

7. (podolec2019clinicalclassificationof pages 2-3): Piotr Podolec, Adrian Baranchuk, Josep Brugada, Piotr Kukla, Jacek Lelakowski, Grzegorz Kopeć, Paweł Rubiś, Jakub Stępniewski, Jakub Podolec, Monika Komar, Lidia Tomkiewicz-Pająk, and Paweł Tomasz Matusik. Clinical classification of rare cardiac arrhythmogenic and conduction disorders, and rare arrhythmias. Polish archives of internal medicine, 129 3:154-159, Feb 2019. URL: https://doi.org/10.20452/pamw.4451, doi:10.20452/pamw.4451. This article has 14 citations.

8. (kato2024atrialstandstilla pages 1-3): Tadahito Kato, Yosuke Osada, and Atsushi Kawaguchi. Atrial standstill: a rare cause of pediatric stroke and management strategies. Journal of St. Marianna University, 15:21-25, Jan 2024. URL: https://doi.org/10.17264/stmarieng.15.21, doi:10.17264/stmarieng.15.21. This article has 0 citations.

9. (makita2005congenitalatrialstandstill pages 1-2): Naomasa Makita, Koji Sasaki, W. Antoinette Groenewegen, Takashi Yokota, Hisashi Yokoshiki, Tomoaki Murakami, and Hiroyuki Tsutsui. Congenital atrial standstill associated with coinheritance of a novel scn5a mutation and connexin 40 polymorphisms. Heart rhythm, 2 10:1128-34, Oct 2005. URL: https://doi.org/10.1016/j.hrthm.2005.06.032, doi:10.1016/j.hrthm.2005.06.032. This article has 119 citations and is from a peer-reviewed journal.

10. (tan2018ahomozygousscn5a pages 1-4): Reina Bianca Tan, Ivan Gando, Lei Bu, Frank Cecchin, and William Coetzee. A homozygous scn5a mutation associated with atrial standstill and sudden death. Pacing and Clinical Electrophysiology, 41:1036-1042, Jun 2018. URL: https://doi.org/10.1111/pace.13386, doi:10.1111/pace.13386. This article has 31 citations.

11. (gal2017atrialstandstillin pages 1-2): Dana B. Gal, Julianne Wojciak, Jennifer Perera, Ronn E. Tanel, and Akash R. Patel. Atrial standstill in a pediatric patient with associated caveolin-3 mutation. HeartRhythm Case Reports, 3:513-516, Nov 2017. URL: https://doi.org/10.1016/j.hrcr.2017.07.014, doi:10.1016/j.hrcr.2017.07.014. This article has 4 citations.

12. (kim2016atrialstandstillin pages 1-2): Tae-Hun Kim, Hyungseop Kim, Hyoung-Seob Park, Seongwook Han, and Nam-Hee Park. Atrial standstill in suspected isolated cardiac sarcoidosis. Journal of cardiology cases, 14 5:136-138, Nov 2016. URL: https://doi.org/10.1016/j.jccase.2016.06.010, doi:10.1016/j.jccase.2016.06.010. This article has 11 citations.

13. (suzuki2019acaseof pages 1-3): Yuya Suzuki, Asumi Takei, Hiroyuki Takahara, Yayoi Taniguchi, Toru Ozawa, and Nobutaka Inoue. A case of atrial standstill with the atrial lead of a dual-chamber pacemaker implanted in the coronary sinus. HeartRhythm Case Reports, 5:338-342, Jun 2019. URL: https://doi.org/10.1016/j.hrcr.2019.03.008, doi:10.1016/j.hrcr.2019.03.008. This article has 6 citations.

14. (valenti2022clinicalprofilearrhythmias pages 1-2): Anna Chiara Valenti, Alessandro Albini, Jacopo Francesco Imberti, Marco Vitolo, Niccolò Bonini, Giovanna Lattanzi, Renate B. Schnabel, and Giuseppe Boriani. Clinical profile, arrhythmias, and adverse cardiac outcomes in emery–dreifuss muscular dystrophies: a systematic review of the literature. Biology, 11:530, Mar 2022. URL: https://doi.org/10.3390/biology11040530, doi:10.3390/biology11040530. This article has 16 citations.

15. (zheng2022leftbundlebranch media 3add666d): Jingang Zheng, Qing-zhen Yang, Jia-sheng Zheng, Qiang Chen, and Qi Jin. Left bundle branch area pacing in a giant atrium with atrial standstill: a case report and literature review. Frontiers in Cardiovascular Medicine, Mar 2022. URL: https://doi.org/10.3389/fcvm.2022.836964, doi:10.3389/fcvm.2022.836964. This article has 3 citations and is from a peer-reviewed journal.