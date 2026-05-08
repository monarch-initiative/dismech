---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T13:05:01.493973'
end_time: '2026-05-08T13:24:12.915859'
duration_seconds: 1151.42
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Diffuse Large B-Cell Lymphoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 58
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Diffuse Large B-Cell Lymphoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Diffuse Large B-Cell Lymphoma** covering all of the
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
- **Disease Name:** Diffuse Large B-Cell Lymphoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Diffuse Large B-Cell Lymphoma** covering all of the
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


## Comprehensive Disease Characteristics Report: Diffuse Large B‑Cell Lymphoma (DLBCL)

### Target disease
- **Disease name:** Diffuse large B‑cell lymphoma (DLBCL)
- **Category:** Aggressive mature B‑cell non‑Hodgkin lymphoma (large B‑cell lymphoma family) (guma2023seomgotelclinicalguidelines pages 1-2, karsten2024sequencingoftherapy pages 1-2)
- **MONDO ID / MeSH / ICD codes:** Not retrievable from the tool evidence corpus in this run; therefore not asserted here.

---

## 1. Disease information

### 1.1 Overview / definition
Diffuse large B‑cell lymphoma (DLBCL) is the most frequent histologic subtype of non‑Hodgkin lymphoma and serves as a clinical paradigm for aggressive lymphoma management (guma2023seomgotelclinicalguidelines pages 1-2). It is a biologically heterogeneous malignancy; transcriptomic and genomic analyses have repeatedly shown that “DLBCL” encompasses multiple molecularly distinct diseases with differing pathway dependencies and outcomes (shimkus2023molecularclassificationand pages 1-2, karsten2024sequencingoftherapy pages 1-2).

Frontline anti‑CD20 chemoimmunotherapy (historically R‑CHOP) cures a substantial fraction of patients, but a major minority relapse or are refractory (vodicka2022diffuselargebcell pages 1-2, melody2024sequencingofcellular pages 1-2).

### 1.2 Common synonyms / alternative names
- **DLBCL, NOS** (not otherwise specified) is the dominant category in practice and in pivotal trials (yazdy2024fdaapprovalsummary pages 1-3, yazdy2024fdaapprovalsummary pages 3-4).
- **Large B‑cell lymphoma (LBCL)** is often used as an umbrella term in trials that include DLBCL and related aggressive B‑cell lymphomas (e.g., ZUMA‑7, EPCORE NHL‑1) (locke2022axicabtageneciloleucelas pages 1-3, thieblemont2023epcoritamabanovel pages 1-2).

### 1.3 Evidence source type
The information below is derived from **aggregated disease-level resources** (WHO/ICC classification reviews and clinical guidelines) and **clinical trial/registry-level evidence** rather than individual EHR case summaries (kurz2023largebcelllymphomas pages 5-7, guma2023seomgotelclinicalguidelines pages 1-2, tilly2022polatuzumabvedotinin pages 1-4, westin2023survivalwithaxicabtagene pages 1-2).

---

## 2. Etiology

### 2.1 Causal factors and disease drivers (molecular)
DLBCL pathogenesis reflects deregulation of B‑cell developmental programs and oncogenic signaling. Key mechanistic themes include:
- **B‑cell receptor (BCR) signaling and downstream NF‑κB activation**, especially prominent in activated B‑cell–like (ABC) biology (shimkus2023molecularclassificationand pages 1-2, vodicka2022diffuselargebcell pages 2-4).
- **Genetic subtype–specific driver constellations**, e.g. **MCD subtype** defined by co‑occurrence of **MYD88 L265P** and **CD79B** mutations; **BN2** associated with **BCL6 fusions** and **NOTCH2** mutations; **N1** with **NOTCH1**; and **A53** with **TP53** mutation/aneuploidy (jaffe2024bandtnkcell pages 3-5, vodicka2022diffuselargebcell pages 2-4).

### 2.2 Risk factors (clinical/epidemiologic)
- **Age:** Incidence rises with age; median age at diagnosis is reported around the mid‑60s to late‑60s in reviews/guidelines (karsten2024sequencingoftherapy pages 1-2, guma2023seomgotelclinicalguidelines pages 1-2).
- **Sex:** Male predominance is noted in population data (Spain sex ratio ~1.37) (guma2023seomgotelclinicalguidelines pages 1-2).
- **Immune context and site:** DLBCL arising in immune‑privileged sites (CNS, testis, vitreoretina) share convergent biology, frequently involving MYD88 and CD79B alterations; these site associations support a role for local immune microenvironments in disease evolution (jaffe2024bandtnkcell pages 5-7).

### 2.3 Infectious agents
- **EBV-positive DLBCL, NOS** is an established entity in modern classification frameworks (WHO/ICC), indicating EBV can be etiologically relevant for a subset (jaffe2024bandtnkcell pages 5-7).

### 2.4 Protective factors / gene–environment interactions
Not identified from the retrieved sources in this run.

---

## 3. Phenotypes (clinical presentation)

### 3.1 Presentation spectrum (supported by retrieved evidence)
The retrieved sources primarily support **pathologic and anatomic phenotypes** rather than symptom frequency.
- **Nodal and extranodal disease:** DLBCL encompasses nodal and diverse extranodal presentations; immune‑privileged site DLBCL (primary CNS, testis, vitreoretinal) are highlighted as biologically coherent forms, often with MYD88 and CD79B mutations (jaffe2024bandtnkcell pages 5-7).
- **Pathology phenotypes:** Morphologic patterns include centroblastic, immunoblastic, and anaplastic variants; this is part of standard pathology descriptions (guma2023seomgotelclinicalguidelines pages 1-2).

### 3.2 Cell-of-origin (COO) phenotype
COO is a major biological phenotype:
- **GCB vs ABC (and unclassified/type 3)** by gene expression profiling; one guideline reports approximate distributions **GCB ~56%, ABC ~32%, type 3 ~11%** (guma2023seomgotelclinicalguidelines pages 1-2).

### 3.3 Quality of life impact
Direct QoL burden data for newly diagnosed DLBCL were not available in retrieved evidence. However, patient‑reported outcomes (PROs) have been analyzed in the second‑line CAR‑T context; in older patients (≥65) treated on ZUMA‑7, mean PRO changes at days 100 and 150 favored axi‑cel vs standard of care for global health/physical functioning and EQ‑5D VAS (trial subgroup report) (westin2023survivalwithaxicabtagene pages 1-2).

### 3.4 Suggested HPO terms (proposed; limited direct frequency support in retrieved evidence)
Because symptom-level frequencies were not retrieved, the following are **ontology suggestions** commonly used for DLBCL knowledge bases and should be validated against primary clinical resources:
- **Lymphadenopathy** (HP:0002716)
- **B symptoms** (e.g., Fever HP:0001945; Night sweats HP:0030166; Weight loss HP:0001824)
- **Extranodal mass** (use site-specific terms, e.g., CNS involvement)

---

## 4. Genetic / molecular information

### 4.1 Key genetic alterations (recurrent)
- **MYC rearrangement**: ~12% by FISH in one review (vodicka2022diffuselargebcell pages 2-4).
- **Double-/triple-hit genetics (MYC with BCL2 and/or BCL6 rearrangements):** ~10% in a review; associated with inferior outcomes on standard R‑CHOP (vodicka2022diffuselargebcell pages 2-4).
- **Protein overexpression (“double expressor”):** MYC protein overexpression occurs in ~50% and MYC/BCL2 double expression in ~33% in a review, associated with worse outcomes (vodicka2022diffuselargebcell pages 2-4).

### 4.2 WHO-HAEM5/ICC changes for high-grade biology
WHO‑HAEM5 refined “double hit” categorization to include **MYC and BCL2 rearranged** cases (allowing additional BCL6 breaks), while **excluding MYC/BCL6-only** cases from that entity (kurz2023largebcelllymphomas pages 5-7). WHO‑HAEM5 notes MYC rearrangements occur in ~10% of DLBCL morphologies; among these, ~40% are MYC/BCL2 double‑hit and 10–15% have additional BCL6 breaks (kurz2023largebcelllymphomas pages 5-7).

### 4.3 Molecular subtype systems (NGS-based)
Multiple algorithms partition DLBCL into genetically defined subtypes:
- Chapuy clusters (C1–C5) and NCI/LymphGen subtypes (e.g., **MCD, BN2, N1, EZB**) with mapping between them (chan2023evolvingtherapeuticlandscape pages 10-12, vodicka2022diffuselargebcell pages 2-4).
- ICC commentary highlights that current genomic systems still leave **~35–40% of cases unassigned**, and the ICC considered routine genomic subtyping premature for day‑to‑day diagnosis (jaffe2024bandtnkcell pages 5-7).

### 4.4 Pathways and mechanistic chain (current understanding)
A simplified causal chain supported by retrieved sources:
1. **Initiating lesions** (e.g., MYD88/CD79B co-mutations in MCD; BCL2 translocations/EZH2 mutations in EZB; TP53 alterations in A53) create survival/proliferation advantages (jaffe2024bandtnkcell pages 3-5, vodicka2022diffuselargebcell pages 2-4).
2. **Pathway activation** (BCR→NF‑κB; NOTCH signaling; epigenetic deregulation in GC programs) drives malignant expansion and treatment resistance (shimkus2023molecularclassificationand pages 1-2, vodicka2022diffuselargebcell pages 2-4).
3. **Clinical heterogeneity** emerges (site‑specific entities such as CNS/testis; variable response to standard chemoimmunotherapy), motivating targeted and immune‑effector therapies (jaffe2024bandtnkcell pages 5-7, trabolsi2024bispecificantibodiesand pages 1-2).

### 4.5 Ontology suggestions (molecular/cellular)
- **Candidate GO biological process terms:**
  - B cell receptor signaling pathway (GO:0050853)
  - NF‑κB signaling (GO:0043122)
  - Regulation of apoptotic process (GO:0042981)
- **Candidate Cell Ontology (CL) terms:**
  - B cell (CL:0000236)
  - Germinal center B cell (CL:0000844)
  - Activated B cell (CL:0000788)

---

## 5. Environmental information
No specific chemical/toxic exposures or lifestyle risk modifiers were supported by the retrieved evidence corpus in this run.

---

## 6. Mechanism / pathophysiology

### 6.1 Immune-privileged site biology
DLBCLs in **CNS/testis/vitreoretina** share convergent genetic features (notably **MYD88** and **CD79B**), and ICC discussions treat testicular DLBCL as closely related to primary CNS DLBCL (jaffe2024bandtnkcell pages 5-7). This supports a model where local immune privilege and immune escape shape selection for particular oncogenic programs.

### 6.2 Immune effector therapies as mechanism-based interventions
- **CAR‑T (CD19-directed):** provides effector-cell–mediated killing; durable disease-free outcomes consistent with cure are reported in a fraction of high‑risk rel/ref patients at longer follow-up, but implementation is constrained by manufacturing time and specialized-center requirements (trabolsi2024bispecificantibodiesand pages 1-2).
- **Bispecific antibodies (CD20×CD3):** redirect endogenous T cells to CD20+ malignant B cells; can be administered more broadly (including community settings) and generally show reduced severity of immune toxicities compared with CAR‑T, though evidence of cure as monotherapy remains limited at current follow-up (trabolsi2024bispecificantibodiesand pages 1-2, melody2024sequencingofcellular pages 1-2).

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue level (supported)
- **Lymph nodes** (diagnostic biopsy site of choice) (guma2023seomgotelclinicalguidelines pages 1-2).
- **Immune-privileged organs/sites:** CNS and testis (and related sites) with coherent DLBCL biology (jaffe2024bandtnkcell pages 5-7).

### 7.2 Ontology suggestions
- **UBERON:** lymph node (UBERON:0000029); central nervous system (UBERON:0001016); testis (UBERON:0000473).

---

## 8. Temporal development

### 8.1 Typical onset
Predominantly a disease of older adults; median age around 65–68 years in guideline/review sources (guma2023seomgotelclinicalguidelines pages 1-2, karsten2024sequencingoftherapy pages 1-2).

### 8.2 Course and relapse
Even with effective frontline therapy, **~30–40%** of patients are refractory or relapse within several years in multiple reviews (vodicka2022diffuselargebcell pages 1-2, melody2024sequencingofcellular pages 1-2).

---

## 9. Inheritance and population

### 9.1 Inheritance
DLBCL is primarily a **somatic** malignancy; germline inheritance patterns are not supported by the retrieved evidence corpus in this run.

### 9.2 Epidemiology (recently cited statistics)
- **Spain (2021):** ~6,933 cases, crude incidence **5.53 per 100,000/year**, median age 68, sex ratio 1.37, and 5‑year relative survival ~55.6% (2002–2013) (guma2023seomgotelclinicalguidelines pages 1-2).
- **US/Western Europe (projection/estimate):** a 2024 expert review cites ~60,000 expected new diagnoses in 2023 and a US incidence projection from 29,108 (2020) to 32,443 (2025) (trabolsi2024bispecificantibodiesand pages 1-2).

---

## 10. Diagnostics

### 10.1 Tissue diagnosis (core principle)
Excisional/incisional lymph node biopsy reviewed by an experienced hemopathologist is recommended; fine‑needle aspiration alone is inadequate (guma2023seomgotelclinicalguidelines pages 1-2).

### 10.2 Standard pathology workup (WHO5/ICC-aligned)
A practical framework supported by guidelines and WHO5/ICC-focused diagnostic reviews:
1. **Morphology** and confirmation of B‑cell lineage with pan‑B markers (e.g., CD20, CD79a, PAX5) (zanelli2024adiagnosticapproach pages 3-5).
2. **Immunohistochemistry core panels** including **CD20, CD3, CD5, CD10, CD45, BCL2, BCL6, Ki‑67, IRF4/MUM1**, plus additional stains (e.g., EBV testing) as needed (guma2023seomgotelclinicalguidelines pages 1-2).
3. **Cell-of-origin (COO)** by gene expression profiling where feasible; IHC algorithms (e.g., Hans using CD10/BCL6/MUM1) are widely used surrogates but imperfect (guma2023seomgotelclinicalguidelines pages 1-2, zanelli2024adiagnosticapproach pages 3-5).
4. **Cytogenetics/FISH:** WHO5/ICC-aligned diagnostic reviews emphasize broad screening for **MYC, BCL2, BCL6 rearrangements** (rather than limiting to morphologically high‑grade cases) to detect double-/triple-hit biology and related entities (zanelli2024adiagnosticapproach pages 9-11, zanelli2024adiagnosticapproach pages 3-5).

### 10.3 Key molecular tests and their role
- **FISH break-apart probes** are recommended for MYC/BCL2 (and often BCL6) rearrangements, but may miss up to ~20% of cryptic rearrangements (jaffe2024bandtnkcell pages 5-7).
- **Targeted NGS panels** may support refined subtyping and prognostication but are not universally implemented; ICC considered it premature to mandate broad genomic subtyping for routine diagnosis (jaffe2024bandtnkcell pages 5-7).

---

## 11. Outcome / prognosis

### 11.1 Cure/relapse rates
- Frontline R‑CHOP historically yields ~60–70% cure probability, leaving ~30–40% refractory/relapsed (vodicka2022diffuselargebcell pages 1-2, melody2024sequencingofcellular pages 1-2).

### 11.2 Prognostic drivers in contemporary practice
- Clinical risk scores such as IPI are used (pivotal frontline pola+R‑CHP approval was restricted to IPI ≥2) (yazdy2024fdaapprovalsummary pages 1-3).
- Genomic high‑risk features include MYC rearrangements and double-/triple-hit genetics; diagnostic FISH is widely used at baseline (vodicka2022diffuselargebcell pages 2-4, guma2023seomgotelclinicalguidelines pages 1-2).

---

## 12. Treatment

### 12.1 Frontline (1L) therapy

**Chemoimmunotherapy backbone:** R‑CHOP remains a reference standard in guidelines (guma2023seomgotelclinicalguidelines pages 1-2).

**Polatuzumab vedotin + R‑CHP (pola‑R‑CHP):**
- **Pivotal trial:** POLARIX (NEJM, published 2022‑01; URL https://doi.org/10.1056/NEJMoa2115304) randomized **879** untreated intermediate/high‑risk patients to pola‑R‑CHP vs R‑CHOP; **2‑year PFS 76.7% vs 70.2%**, HR **0.73**; **2‑year OS 88.7% vs 88.6%** (no significant difference) (tilly2022polatuzumabvedotinin pages 1-4).
- **Regulatory:** FDA regular approval **April 2023** for previously untreated **DLBCL, NOS or HGBL with IPI ≥2**; FDA review emphasized PFS benefit and no demonstrated OS improvement (approval summary published 2024‑10; URL https://doi.org/10.1158/1078-0432.CCR-24-1729) (yazdy2024fdaapprovalsummary pages 1-3, yazdy2024fdaapprovalsummary pages 13-13).

### 12.2 Second-line (2L) early relapsed/refractory disease

**CD19 CAR‑T (axi‑cel):**
- **Primary analysis (ZUMA‑7; NEJM 2022‑02; URL https://doi.org/10.1056/NEJMoa2116133):** median EFS **8.3 vs 2.0 months**; 24‑month EFS **41% vs 16%**; HR **0.40**. ORR **83% vs 50%**; CR **65% vs 32%** (locke2022axicabtageneciloleucelas pages 1-3).
- **Overall survival follow-up (NEJM 2023‑07; URL https://doi.org/10.1056/NEJMoa2301665):** median OS not reached vs 31.1 months; **4‑year OS 54.6% vs 46.0%**, HR **0.73**; PFS HR **0.51** (westin2023survivalwithaxicabtagene pages 1-2). Kaplan–Meier OS/PFS curves are shown in the retrieved figure panels (westin2023survivalwithaxicabtagene media cdc76b37, westin2023survivalwithaxicabtagene media 1a4e56dd).
- **Regulatory:** FDA approval **April 2022** for adults with LBCL refractory to first-line chemoimmunotherapy or relapsing within 12 months; safety included CRS 92% (grade ≥3 7%), neurologic toxicity 74% (grade ≥3 25%), prolonged cytopenias 33% (approval summary published 2023‑07; URL https://doi.org/10.1158/1078-0432.CCR-23-0568) (sharma2023fdaapprovalsummary pages 1-3).

### 12.3 Third-line or later (≥3L) relapsed/refractory disease

**Epcoritamab (subcutaneous CD3×CD20 bispecific):**
- **Initial pivotal data (JCO 2023‑04; URL https://doi.org/10.1200/JCO.22.01725):** in 157 heavily pretreated LBCL patients, ORR **63.1%**, CR **38.9%**; CRS **49.7%** (grade 3 2.5%); ICANS **6.4%** (including one fatal event) (thieblemont2023epcoritamabanovel pages 1-2).
- **2‑year follow-up (Leukemia 2024‑09; URL https://doi.org/10.1038/s41375-024-02410-8):** ORR **63.1%**, CR **40.1%**; median DOR **17.3 months**; **24‑month PFS 27.8%**, **24‑month OS 44.6%**; MRD negativity in **45.4%** correlated with longer PFS/OS (thieblemont2024epcoritamabinrelapsedrefractory pages 1-2, thieblemont2024epcoritamabinrelapsedrefractory pages 4-4).

**Bispecific antibody class implementation:** Reviews emphasize that bispecific antibodies (e.g., epcoritamab and glofitamab) were initially approved **May–June 2023** and can be delivered more broadly (including community settings) than CAR‑T because they do not require individualized manufacturing and may have generally reduced immune‑toxicity severity (trabolsi2024bispecificantibodiesand pages 1-2, melody2024sequencingofcellular pages 1-2).

### 12.4 Treatment ontology (MAXO) suggestions
- Anti‑CD20 chemoimmunotherapy (e.g., rituximab + CHOP): **MAXO:0000647** (chemotherapy), **MAXO:0000171** (immunotherapy) (ontology suggestions; validate).
- CAR‑T therapy: **MAXO:0001534** (cellular immunotherapy; validate).
- Bispecific antibody therapy: **MAXO:0000171** (immunotherapy; validate).

### Evidence summary artifact (therapies)
| Setting | Regimen/Agent (target/class) | Key trial or source | Key efficacy statistics | Regulatory/implementation note | URL | Publication date | PMID if known |
|---|---|---|---|---|---|---|---|
| 1L | Pola-R-CHP (polatuzumab vedotin; anti-CD79b ADC replacing vincristine in R-CHOP backbone) | POLARIX; Tilly et al., NEJM 2022; FDA approval summary 2024 (tilly2022polatuzumabvedotinin pages 1-4, yazdy2024fdaapprovalsummary pages 1-3) | 879 patients; 2-year PFS 76.7% vs 70.2% for R-CHOP; HR 0.73 (95% CI 0.57-0.95); no OS difference at 2 years: 88.7% vs 88.6%, HR 0.94; ORR 86% vs 84%, CR 78% vs 74% (tilly2022polatuzumabvedotinin pages 1-4, yazdy2024fdaapprovalsummary pages 8-13, yazdy2024fdaapprovalsummary pages 3-4) | FDA regular approval April 2023 for previously untreated DLBCL, NOS or HGBL with IPI >=2; PFS benefit considered clinically meaningful but modest; no OS benefit shown in review (yazdy2024fdaapprovalsummary pages 1-3, yazdy2024fdaapprovalsummary pages 13-13, yazdy2024fdaapprovalsummary pages 6-8) | https://doi.org/10.1056/NEJMoa2115304 ; https://doi.org/10.1158/1078-0432.CCR-24-1729 | 2022-01-27; 2024-10 |  |
| 2L early relapse/refractory | Axicabtagene ciloleucel (axi-cel; autologous anti-CD19 CAR-T) | ZUMA-7 primary analysis; Locke et al., NEJM 2022; FDA approval summary 2023; OS follow-up Westin et al., NEJM 2023 (locke2022axicabtageneciloleucelas pages 1-3, sharma2023fdaapprovalsummary pages 1-3, westin2023survivalwithaxicabtagene pages 1-2) | Median EFS 8.3 vs 2.0 months; 24-month EFS 41% vs 16%; HR 0.40. ORR 83% vs 50%; CR 65% vs 32%. Median PFS 14.7 months vs 3.7 months; 4-year PFS 41.8% vs 24.4%; HR 0.51. Median OS not reached vs 31.1 months; 4-year OS 54.6% vs 46.0%; HR 0.73 (locke2022axicabtageneciloleucelas pages 1-3, westin2023survivalwithaxicabtagene pages 1-2, sharma2023fdaapprovalsummary pages 3-5) | FDA approval April 2022 for adults with LBCL refractory to first-line chemoimmunotherapy or relapsing within 12 months; first CAR-T approved in 2L LBCL. 94% of randomized axi-cel arm received product; specialized-center delivery required (sharma2023fdaapprovalsummary pages 1-3, sharma2023fdaapprovalsummary pages 5-6, trabolsi2024bispecificantibodiesand pages 1-2) | https://doi.org/10.1056/NEJMoa2116133 ; https://doi.org/10.1056/NEJMoa2301665 ; https://doi.org/10.1158/1078-0432.CCR-23-0568 | 2022-02-17; 2023-07-13; 2023-07 |  |
| 2L early relapse/refractory | Axicabtagene ciloleucel safety profile (same regimen; anti-CD19 CAR-T) | ZUMA-7 FDA/NEJM safety reporting (sharma2023fdaapprovalsummary pages 1-3, locke2022axicabtageneciloleucelas pages 1-3, sharma2023fdaapprovalsummary pages 5-6) | Grade >=3 AEs 91% vs 83% with standard care; CRS 92% overall, grade >=3 7%; neurologic toxicity 74%, grade >=3 25%; prolonged cytopenias 33%; fatal adverse reactions 1.8% (sharma2023fdaapprovalsummary pages 1-3, sharma2023fdaapprovalsummary pages 3-5, sharma2023fdaapprovalsummary pages 5-6) | Boxed warnings for CRS and neurologic toxicity; REMS required in US practice (sharma2023fdaapprovalsummary pages 3-5, sharma2023fdaapprovalsummary pages 14-15) | https://doi.org/10.1158/1078-0432.CCR-23-0568 ; https://doi.org/10.1056/NEJMoa2116133 | 2023-07; 2022-02-17 |  |
| 3L+ R/R | Epcoritamab monotherapy (subcutaneous CD3xCD20 bispecific T-cell engager) | EPCORE NHL-1; Thieblemont et al., JCO 2023 (thieblemont2023epcoritamabanovel pages 1-2, thieblemont2023epcoritamabanovel pages 2-3) | In 157 heavily pretreated LBCL patients, ORR 63.1% (95% CI 55.0-70.6); CR 38.9% (95% CI 31.2-46.9); median DOR 12.0 months; prior CAR-T subgroup ORR 54%, CR 34% (thieblemont2023epcoritamabanovel pages 1-2, thieblemont2023epcoritamabanovel pages 7-8) | Step-up SC dosing in 28-day cycles with initial inpatient monitoring for first full dose; prior CAR-T allowed; manageable outpatient/community-oriented administration model after step-up phase (thieblemont2023epcoritamabanovel pages 1-2, thieblemont2023epcoritamabanovel pages 2-3, trabolsi2024bispecificantibodiesand pages 1-2) | https://doi.org/10.1200/JCO.22.01725 | 2023-04 |  |
| 3L+ R/R | Epcoritamab long-term follow-up (subcutaneous CD3xCD20 bispecific) | EPCORE NHL-1 2-year follow-up; Thieblemont et al., Leukemia 2024 (thieblemont2024epcoritamabinrelapsedrefractory pages 1-2, thieblemont2024epcoritamabinrelapsedrefractory pages 4-4) | Median follow-up 25.1 months; ORR 63.1%; CR 40.1%; median DOR 17.3 months; 24-month PFS 27.8%; 24-month OS 44.6%; among CRs, 64.2% remained in CR at 24 months; MRD negativity in 45.4% correlated with longer PFS/OS (thieblemont2024epcoritamabinrelapsedrefractory pages 1-2, thieblemont2024epcoritamabinrelapsedrefractory pages 4-4, thieblemont2024epcoritamabinrelapsedrefractory pages 6-6) | Supports durability in 3L+ setting; useful after/around CAR-T failure or in CAR-T-ineligible patients (thieblemont2024epcoritamabinrelapsedrefractory pages 1-2, melody2024sequencingofcellular pages 1-2) | https://doi.org/10.1038/s41375-024-02410-8 | 2024-09 |  |
| 3L+ R/R | Epcoritamab safety (same regimen; CD3xCD20 bispecific) | EPCORE NHL-1 JCO 2023 and Leukemia 2024 (thieblemont2023epcoritamabanovel pages 1-2, thieblemont2024epcoritamabinrelapsedrefractory pages 4-6) | CRS 49.7% in 2023 report (grade 3 2.5%); ICANS 6.4% with one fatal event. At 2-year follow-up, CRS 51.0%; grade 1 31.8%, grade 2 15.9%, grade 3 3.2%; no grade 4/5 CRS; median CRS duration 2 days (thieblemont2023epcoritamabanovel pages 1-2, thieblemont2024epcoritamabinrelapsedrefractory pages 4-6) | Subcutaneous administration with step-up dosing and generally lower-grade immune toxicity than CAR-T supports broader deployment (trabolsi2024bispecificantibodiesand pages 1-2, thieblemont2024epcoritamabinrelapsedrefractory pages 4-6) | https://doi.org/10.1200/JCO.22.01725 ; https://doi.org/10.1038/s41375-024-02410-8 | 2023-04; 2024-09 |  |
| 3L+ R/R | Bispecific antibodies class note: epcoritamab and glofitamab (CD20xCD3 bispecifics) | Trabolsi 2024; Melody 2024 (trabolsi2024bispecificantibodiesand pages 1-2, melody2024sequencingofcellular pages 1-2) | Class-level data: ORRs >50% with durable remissions extending beyond 2 years in subsets; epcoritamab comparative analyses showed outcomes superior to chemoimmunotherapy/polatuzumab- or tafasitamab-based cohorts and similar to CAR-T in some indirect comparisons (melody2024sequencingofcellular pages 1-2) | Initial FDA approvals for next-generation bispecifics occurred in May-June 2023; can often be administered in community settings, unlike CAR-T which requires manufacturing time and certified centers (trabolsi2024bispecificantibodiesand pages 1-2, melody2024sequencingofcellular pages 1-2) | https://doi.org/10.1038/s41408-024-00997-w ; https://doi.org/10.3324/haematol.2024.285255 | 2024-02; 2024-07 |  |


*Table: This table summarizes major systemic therapies for DLBCL across frontline, second-line, and third-line-plus settings using pivotal 2022-2024 evidence. It highlights efficacy, regulatory context, and practical implementation features, including newer bispecific antibodies and CAR-T therapy.*

---

## 13. Prevention
No primary prevention strategies specific to DLBCL were supported by the retrieved evidence corpus in this run. Secondary prevention concepts supported indirectly include timely biopsy-based diagnosis and risk-adapted therapy selection based on IPI and high-risk genetics (MYC/BCL2/BCL6 rearrangements) (guma2023seomgotelclinicalguidelines pages 1-2, yazdy2024fdaapprovalsummary pages 1-3).

---

## 14. Other species / natural disease
Not supported by retrieved evidence in this run.

---

## 15. Model organisms
Not supported by retrieved evidence in this run.

---

## Notes on evidence gaps vs requested template
This run retrieved substantial **2022–2024** primary evidence for classification, diagnostics, and therapy, but **did not retrieve** primary ontology entries needed to assert: MONDO ID, MeSH descriptor ID, and ICD‑10/ICD‑11 codes. Additionally, symptom-level phenotype frequencies (for HPO mapping), environmental/lifestyle risk modifiers, and model organism details were not present in the retrieved corpus and are therefore not claimed.

References

1. (guma2023seomgotelclinicalguidelines pages 1-2): Josep Gumà, Natalia Palazón-Carrión, Antonio Rueda-Domínguez, Silvia Sequero, Virginia Calvo, Ramón García-Arroyo, José Gómez-Codina, Marta Llanos, Natividad Martínez-Banaclocha, and Mariano Provencio. Seom-gotel clinical guidelines on diffuse large b cell lymphoma (2022). Clinical & Translational Oncology, 25:2749-2758, Jun 2023. URL: https://doi.org/10.1007/s12094-023-03206-5, doi:10.1007/s12094-023-03206-5. This article has 6 citations and is from a peer-reviewed journal.

2. (karsten2024sequencingoftherapy pages 1-2): Imke E. Karsten, Evgenii Shumilov, Norbert Schmitz, and Georg Lenz. Sequencing of therapy for patients with diffuse large b‐cell lymphoma in the era of novel drugs. British Journal of Haematology, 205:2163-2174, Oct 2024. URL: https://doi.org/10.1111/bjh.19860, doi:10.1111/bjh.19860. This article has 19 citations and is from a domain leading peer-reviewed journal.

3. (shimkus2023molecularclassificationand pages 1-2): Gaelen Shimkus and Taichiro Nonaka. Molecular classification and therapeutics in diffuse large b-cell lymphoma. Frontiers in Molecular Biosciences, Feb 2023. URL: https://doi.org/10.3389/fmolb.2023.1124360, doi:10.3389/fmolb.2023.1124360. This article has 30 citations.

4. (vodicka2022diffuselargebcell pages 1-2): Prokop Vodicka, Pavel Klener, and Marek Trneny. Diffuse large b-cell lymphoma (dlbcl): early patient management and emerging treatment options. OncoTargets and Therapy, 15:1481-1501, Dec 2022. URL: https://doi.org/10.2147/ott.s326632, doi:10.2147/ott.s326632. This article has 86 citations.

5. (melody2024sequencingofcellular pages 1-2): Megan Melody and Leo I. Gordon. Sequencing of cellular therapy and bispecific antibodies for the management of diffuse large b-cell lymphoma. Haematologica, 109:3138-3145, Jul 2024. URL: https://doi.org/10.3324/haematol.2024.285255, doi:10.3324/haematol.2024.285255. This article has 18 citations.

6. (yazdy2024fdaapprovalsummary pages 1-3): Maryam Sarraf Yazdy, Yvette L. Kasamon, Wenjuan Gu, Lisa R. Rodriguez, Susan Jin, Vishal Bhatnagar, Nicholas C. Richardson, Marc R. Theoret, Richard Pazdur, and Nicole J. Gormley. Fda approval summary: polatuzumab vedotin in the first-line treatment of select large b-cell lymphomas. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:5521-5526, Oct 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1729, doi:10.1158/1078-0432.ccr-24-1729. This article has 9 citations.

7. (yazdy2024fdaapprovalsummary pages 3-4): Maryam Sarraf Yazdy, Yvette L. Kasamon, Wenjuan Gu, Lisa R. Rodriguez, Susan Jin, Vishal Bhatnagar, Nicholas C. Richardson, Marc R. Theoret, Richard Pazdur, and Nicole J. Gormley. Fda approval summary: polatuzumab vedotin in the first-line treatment of select large b-cell lymphomas. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:5521-5526, Oct 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1729, doi:10.1158/1078-0432.ccr-24-1729. This article has 9 citations.

8. (locke2022axicabtageneciloleucelas pages 1-3): Frederick L. Locke, David B. Miklos, Caron A. Jacobson, Miguel-Angel Perales, Marie-José Kersten, Olalekan O. Oluwole, Armin Ghobadi, Aaron P. Rapoport, Joseph McGuirk, John M. Pagel, Javier Muñoz, Umar Farooq, Tom van Meerten, Patrick M. Reagan, Anna Sureda, Ian W. Flinn, Peter Vandenberghe, Kevin W. Song, Michael Dickinson, Monique C. Minnema, Peter A. Riedell, Lori A. Leslie, Sridhar Chaganti, Yin Yang, Simone Filosto, Jina Shah, Marco Schupp, Christina To, Paul Cheng, Leo I. Gordon, and Jason R. Westin. Axicabtagene ciloleucel as second-line therapy for large b-cell lymphoma. New England Journal of Medicine, 386:640-654, Feb 2022. URL: https://doi.org/10.1056/nejmoa2116133, doi:10.1056/nejmoa2116133. This article has 1774 citations and is from a highest quality peer-reviewed journal.

9. (thieblemont2023epcoritamabanovel pages 1-2): Catherine Thieblemont, Tycel Phillips, Herve Ghesquieres, Chan Y. Cheah, Michael Roost Clausen, David Cunningham, Young Rok Do, Tatyana Feldman, Robin Gasiorowski, Wojciech Jurczak, Tae Min Kim, David John Lewis, Marjolein van der Poel, Michelle Limei Poon, Mariana Cota Stirner, Nurgul Kilavuz, Christopher Chiu, Menghui Chen, Mariana Sacchi, Brian Elliott, Tahamtan Ahmadi, Martin Hutchings, and Pieternella J. Lugtenburg. Epcoritamab, a novel, subcutaneous cd3xcd20 bispecific t-cell–engaging antibody, in relapsed or refractory large b-cell lymphoma: dose expansion in a phase i/ii trial. Journal of Clinical Oncology, 41:2238-2247, Apr 2023. URL: https://doi.org/10.1200/jco.22.01725, doi:10.1200/jco.22.01725. This article has 623 citations and is from a highest quality peer-reviewed journal.

10. (kurz2023largebcelllymphomas pages 5-7): Katrin S. Kurz, Michaela Ott, Sabrina Kalmbach, Sophia Steinlein, Claudia Kalla, Heike Horn, German Ott, and Annette M. Staiger. Large b-cell lymphomas in the 5th edition of the who-classification of haematolymphoid neoplasms—updated classification and new concepts. Cancers, 15:2285, Apr 2023. URL: https://doi.org/10.3390/cancers15082285, doi:10.3390/cancers15082285. This article has 66 citations.

11. (tilly2022polatuzumabvedotinin pages 1-4): Hervé Tilly, Franck Morschhauser, Laurie H. Sehn, Jonathan W. Friedberg, Marek Trněný, Jeff P. Sharman, Charles Herbaux, John M. Burke, Matthew Matasar, Shinya Rai, Koji Izutsu, Neha Mehta-Shah, Lucie Oberic, Adrien Chauchet, Wojciech Jurczak, Yuqin Song, Richard Greil, Larysa Mykhalska, Juan M. Bergua-Burgués, Matthew C. Cheung, Antonio Pinto, Ho-Jin Shin, Greg Hapgood, Eduardo Munhoz, Pau Abrisqueta, Jyh-Pyng Gau, Jamie Hirata, Yanwen Jiang, Mark Yan, Calvin Lee, Christopher R. Flowers, and Gilles Salles. Polatuzumab vedotin in previously untreated diffuse large b-cell lymphoma. New England Journal of Medicine, 386:351-363, Jan 2022. URL: https://doi.org/10.1056/nejmoa2115304, doi:10.1056/nejmoa2115304. This article has 1074 citations and is from a highest quality peer-reviewed journal.

12. (westin2023survivalwithaxicabtagene pages 1-2): Jason R. Westin, Olalekan O. Oluwole, Marie José Kersten, David B. Miklos, Miguel-Angel Perales, Armin Ghobadi, Aaron P. Rapoport, Anna Sureda, Caron A. Jacobson, Umar Farooq, Tom van Meerten, Matthew Ulrickson, Mahmoud Elsawy, Lori A. Leslie, Sridhar Chaganti, Michael Dickinson, Kathleen Dorritie, Patrick M. Reagan, Joseph McGuirk, Kevin W. Song, Peter A. Riedell, Monique C. Minnema, Yin Yang, Saran Vardhanabhuti, Simone Filosto, Paul Cheng, Shilpa A. Shahani, Marco Schupp, Christina To, and Frederick L. Locke. Survival with axicabtagene ciloleucel in large b-cell lymphoma. New England Journal of Medicine, 389:148-157, Jul 2023. URL: https://doi.org/10.1056/nejmoa2301665, doi:10.1056/nejmoa2301665. This article has 506 citations and is from a highest quality peer-reviewed journal.

13. (vodicka2022diffuselargebcell pages 2-4): Prokop Vodicka, Pavel Klener, and Marek Trneny. Diffuse large b-cell lymphoma (dlbcl): early patient management and emerging treatment options. OncoTargets and Therapy, 15:1481-1501, Dec 2022. URL: https://doi.org/10.2147/ott.s326632, doi:10.2147/ott.s326632. This article has 86 citations.

14. (jaffe2024bandtnkcell pages 3-5): Elaine S. Jaffe and Antonino Carbone. B- and t-/nk-cell lymphomas in the 2022 international consensus classification of mature lymphoid neoplasms and comparison with the who fifth edition. Hemato, 5:157-170, Apr 2024. URL: https://doi.org/10.3390/hemato5020013, doi:10.3390/hemato5020013. This article has 7 citations.

15. (jaffe2024bandtnkcell pages 5-7): Elaine S. Jaffe and Antonino Carbone. B- and t-/nk-cell lymphomas in the 2022 international consensus classification of mature lymphoid neoplasms and comparison with the who fifth edition. Hemato, 5:157-170, Apr 2024. URL: https://doi.org/10.3390/hemato5020013, doi:10.3390/hemato5020013. This article has 7 citations.

16. (chan2023evolvingtherapeuticlandscape pages 10-12): Jason Yongsheng Chan, Nagavalli Somasundaram, Nicholas Grigoropoulos, Francesca Lim, Michelle Limei Poon, Anand Jeyasekharan, Kheng Wei Yeoh, Daryl Tan, Georg Lenz, Choon Kiat Ong, and Soon Thye Lim. Evolving therapeutic landscape of diffuse large b-cell lymphoma: challenges and aspirations. Discover. Oncology, Jul 2023. URL: https://doi.org/10.1007/s12672-023-00754-8, doi:10.1007/s12672-023-00754-8. This article has 22 citations.

17. (trabolsi2024bispecificantibodiesand pages 1-2): Asaad Trabolsi, Artavazd Arumov, and Jonathan H. Schatz. Bispecific antibodies and car-t cells: dueling immunotherapies for large b-cell lymphomas. Blood Cancer Journal, Feb 2024. URL: https://doi.org/10.1038/s41408-024-00997-w, doi:10.1038/s41408-024-00997-w. This article has 110 citations and is from a domain leading peer-reviewed journal.

18. (zanelli2024adiagnosticapproach pages 3-5): Magda Zanelli, Francesca Sanguedolce, Maurizio Zizzo, Stefano Ricci, Alessandra Bisagni, Andrea Palicelli, Valentina Fragliasso, Benedetta Donati, Giuseppe Broggi, Ioannis Boutas, Nektarios Koufopoulos, Moira Foroni, Francesca Coppa, Andrea Morini, Paola Parente, Valeria Zuccalà, Rosario Caltabiano, Massimiliano Fabozzi, Luca Cimino, Antonino Neri, and Stefano Ascani. A diagnostic approach in large b-cell lymphomas according to the fifth world health organization and international consensus classifications and a practical algorithm in routine practice. International Journal of Molecular Sciences, 25:13213, Dec 2024. URL: https://doi.org/10.3390/ijms252313213, doi:10.3390/ijms252313213. This article has 10 citations.

19. (zanelli2024adiagnosticapproach pages 9-11): Magda Zanelli, Francesca Sanguedolce, Maurizio Zizzo, Stefano Ricci, Alessandra Bisagni, Andrea Palicelli, Valentina Fragliasso, Benedetta Donati, Giuseppe Broggi, Ioannis Boutas, Nektarios Koufopoulos, Moira Foroni, Francesca Coppa, Andrea Morini, Paola Parente, Valeria Zuccalà, Rosario Caltabiano, Massimiliano Fabozzi, Luca Cimino, Antonino Neri, and Stefano Ascani. A diagnostic approach in large b-cell lymphomas according to the fifth world health organization and international consensus classifications and a practical algorithm in routine practice. International Journal of Molecular Sciences, 25:13213, Dec 2024. URL: https://doi.org/10.3390/ijms252313213, doi:10.3390/ijms252313213. This article has 10 citations.

20. (yazdy2024fdaapprovalsummary pages 13-13): Maryam Sarraf Yazdy, Yvette L. Kasamon, Wenjuan Gu, Lisa R. Rodriguez, Susan Jin, Vishal Bhatnagar, Nicholas C. Richardson, Marc R. Theoret, Richard Pazdur, and Nicole J. Gormley. Fda approval summary: polatuzumab vedotin in the first-line treatment of select large b-cell lymphomas. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:5521-5526, Oct 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1729, doi:10.1158/1078-0432.ccr-24-1729. This article has 9 citations.

21. (westin2023survivalwithaxicabtagene media cdc76b37): Jason R. Westin, Olalekan O. Oluwole, Marie José Kersten, David B. Miklos, Miguel-Angel Perales, Armin Ghobadi, Aaron P. Rapoport, Anna Sureda, Caron A. Jacobson, Umar Farooq, Tom van Meerten, Matthew Ulrickson, Mahmoud Elsawy, Lori A. Leslie, Sridhar Chaganti, Michael Dickinson, Kathleen Dorritie, Patrick M. Reagan, Joseph McGuirk, Kevin W. Song, Peter A. Riedell, Monique C. Minnema, Yin Yang, Saran Vardhanabhuti, Simone Filosto, Paul Cheng, Shilpa A. Shahani, Marco Schupp, Christina To, and Frederick L. Locke. Survival with axicabtagene ciloleucel in large b-cell lymphoma. New England Journal of Medicine, 389:148-157, Jul 2023. URL: https://doi.org/10.1056/nejmoa2301665, doi:10.1056/nejmoa2301665. This article has 506 citations and is from a highest quality peer-reviewed journal.

22. (westin2023survivalwithaxicabtagene media 1a4e56dd): Jason R. Westin, Olalekan O. Oluwole, Marie José Kersten, David B. Miklos, Miguel-Angel Perales, Armin Ghobadi, Aaron P. Rapoport, Anna Sureda, Caron A. Jacobson, Umar Farooq, Tom van Meerten, Matthew Ulrickson, Mahmoud Elsawy, Lori A. Leslie, Sridhar Chaganti, Michael Dickinson, Kathleen Dorritie, Patrick M. Reagan, Joseph McGuirk, Kevin W. Song, Peter A. Riedell, Monique C. Minnema, Yin Yang, Saran Vardhanabhuti, Simone Filosto, Paul Cheng, Shilpa A. Shahani, Marco Schupp, Christina To, and Frederick L. Locke. Survival with axicabtagene ciloleucel in large b-cell lymphoma. New England Journal of Medicine, 389:148-157, Jul 2023. URL: https://doi.org/10.1056/nejmoa2301665, doi:10.1056/nejmoa2301665. This article has 506 citations and is from a highest quality peer-reviewed journal.

23. (sharma2023fdaapprovalsummary pages 1-3): Poornima Sharma, Yvette L. Kasamon, Xue Lin, Zhenzhen Xu, Marc R. Theoret, and Tejashri Purohit-Sheth. Fda approval summary: axicabtagene ciloleucel for second-line treatment of large b-cell lymphoma. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:4331-4337, Jul 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-0568, doi:10.1158/1078-0432.ccr-23-0568. This article has 25 citations.

24. (thieblemont2024epcoritamabinrelapsedrefractory pages 1-2): Catherine Thieblemont, Yasmin H. Karimi, Herve Ghesquieres, Chan Y. Cheah, Michael Roost Clausen, David Cunningham, Wojciech Jurczak, Young Rok Do, Robin Gasiorowski, David John Lewis, Tae Min Kim, Marjolein van der Poel, Michelle Limei Poon, Tatyana Feldman, Kim M. Linton, Anna Sureda, Martin Hutchings, Minh H. Dinh, Nurgul Kilavuz, David Soong, Thomas Mark, Mariana Sacchi, Tycel Phillips, and Pieternella J. Lugtenburg. Epcoritamab in relapsed/refractory large b-cell lymphoma: 2-year follow-up from the pivotal epcore nhl-1 trial. Leukemia, 38:2653-2662, Sep 2024. URL: https://doi.org/10.1038/s41375-024-02410-8, doi:10.1038/s41375-024-02410-8. This article has 130 citations and is from a highest quality peer-reviewed journal.

25. (thieblemont2024epcoritamabinrelapsedrefractory pages 4-4): Catherine Thieblemont, Yasmin H. Karimi, Herve Ghesquieres, Chan Y. Cheah, Michael Roost Clausen, David Cunningham, Wojciech Jurczak, Young Rok Do, Robin Gasiorowski, David John Lewis, Tae Min Kim, Marjolein van der Poel, Michelle Limei Poon, Tatyana Feldman, Kim M. Linton, Anna Sureda, Martin Hutchings, Minh H. Dinh, Nurgul Kilavuz, David Soong, Thomas Mark, Mariana Sacchi, Tycel Phillips, and Pieternella J. Lugtenburg. Epcoritamab in relapsed/refractory large b-cell lymphoma: 2-year follow-up from the pivotal epcore nhl-1 trial. Leukemia, 38:2653-2662, Sep 2024. URL: https://doi.org/10.1038/s41375-024-02410-8, doi:10.1038/s41375-024-02410-8. This article has 130 citations and is from a highest quality peer-reviewed journal.

26. (yazdy2024fdaapprovalsummary pages 8-13): Maryam Sarraf Yazdy, Yvette L. Kasamon, Wenjuan Gu, Lisa R. Rodriguez, Susan Jin, Vishal Bhatnagar, Nicholas C. Richardson, Marc R. Theoret, Richard Pazdur, and Nicole J. Gormley. Fda approval summary: polatuzumab vedotin in the first-line treatment of select large b-cell lymphomas. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:5521-5526, Oct 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1729, doi:10.1158/1078-0432.ccr-24-1729. This article has 9 citations.

27. (yazdy2024fdaapprovalsummary pages 6-8): Maryam Sarraf Yazdy, Yvette L. Kasamon, Wenjuan Gu, Lisa R. Rodriguez, Susan Jin, Vishal Bhatnagar, Nicholas C. Richardson, Marc R. Theoret, Richard Pazdur, and Nicole J. Gormley. Fda approval summary: polatuzumab vedotin in the first-line treatment of select large b-cell lymphomas. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:5521-5526, Oct 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1729, doi:10.1158/1078-0432.ccr-24-1729. This article has 9 citations.

28. (sharma2023fdaapprovalsummary pages 3-5): Poornima Sharma, Yvette L. Kasamon, Xue Lin, Zhenzhen Xu, Marc R. Theoret, and Tejashri Purohit-Sheth. Fda approval summary: axicabtagene ciloleucel for second-line treatment of large b-cell lymphoma. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:4331-4337, Jul 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-0568, doi:10.1158/1078-0432.ccr-23-0568. This article has 25 citations.

29. (sharma2023fdaapprovalsummary pages 5-6): Poornima Sharma, Yvette L. Kasamon, Xue Lin, Zhenzhen Xu, Marc R. Theoret, and Tejashri Purohit-Sheth. Fda approval summary: axicabtagene ciloleucel for second-line treatment of large b-cell lymphoma. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:4331-4337, Jul 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-0568, doi:10.1158/1078-0432.ccr-23-0568. This article has 25 citations.

30. (sharma2023fdaapprovalsummary pages 14-15): Poornima Sharma, Yvette L. Kasamon, Xue Lin, Zhenzhen Xu, Marc R. Theoret, and Tejashri Purohit-Sheth. Fda approval summary: axicabtagene ciloleucel for second-line treatment of large b-cell lymphoma. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:4331-4337, Jul 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-0568, doi:10.1158/1078-0432.ccr-23-0568. This article has 25 citations.

31. (thieblemont2023epcoritamabanovel pages 2-3): Catherine Thieblemont, Tycel Phillips, Herve Ghesquieres, Chan Y. Cheah, Michael Roost Clausen, David Cunningham, Young Rok Do, Tatyana Feldman, Robin Gasiorowski, Wojciech Jurczak, Tae Min Kim, David John Lewis, Marjolein van der Poel, Michelle Limei Poon, Mariana Cota Stirner, Nurgul Kilavuz, Christopher Chiu, Menghui Chen, Mariana Sacchi, Brian Elliott, Tahamtan Ahmadi, Martin Hutchings, and Pieternella J. Lugtenburg. Epcoritamab, a novel, subcutaneous cd3xcd20 bispecific t-cell–engaging antibody, in relapsed or refractory large b-cell lymphoma: dose expansion in a phase i/ii trial. Journal of Clinical Oncology, 41:2238-2247, Apr 2023. URL: https://doi.org/10.1200/jco.22.01725, doi:10.1200/jco.22.01725. This article has 623 citations and is from a highest quality peer-reviewed journal.

32. (thieblemont2023epcoritamabanovel pages 7-8): Catherine Thieblemont, Tycel Phillips, Herve Ghesquieres, Chan Y. Cheah, Michael Roost Clausen, David Cunningham, Young Rok Do, Tatyana Feldman, Robin Gasiorowski, Wojciech Jurczak, Tae Min Kim, David John Lewis, Marjolein van der Poel, Michelle Limei Poon, Mariana Cota Stirner, Nurgul Kilavuz, Christopher Chiu, Menghui Chen, Mariana Sacchi, Brian Elliott, Tahamtan Ahmadi, Martin Hutchings, and Pieternella J. Lugtenburg. Epcoritamab, a novel, subcutaneous cd3xcd20 bispecific t-cell–engaging antibody, in relapsed or refractory large b-cell lymphoma: dose expansion in a phase i/ii trial. Journal of Clinical Oncology, 41:2238-2247, Apr 2023. URL: https://doi.org/10.1200/jco.22.01725, doi:10.1200/jco.22.01725. This article has 623 citations and is from a highest quality peer-reviewed journal.

33. (thieblemont2024epcoritamabinrelapsedrefractory pages 6-6): Catherine Thieblemont, Yasmin H. Karimi, Herve Ghesquieres, Chan Y. Cheah, Michael Roost Clausen, David Cunningham, Wojciech Jurczak, Young Rok Do, Robin Gasiorowski, David John Lewis, Tae Min Kim, Marjolein van der Poel, Michelle Limei Poon, Tatyana Feldman, Kim M. Linton, Anna Sureda, Martin Hutchings, Minh H. Dinh, Nurgul Kilavuz, David Soong, Thomas Mark, Mariana Sacchi, Tycel Phillips, and Pieternella J. Lugtenburg. Epcoritamab in relapsed/refractory large b-cell lymphoma: 2-year follow-up from the pivotal epcore nhl-1 trial. Leukemia, 38:2653-2662, Sep 2024. URL: https://doi.org/10.1038/s41375-024-02410-8, doi:10.1038/s41375-024-02410-8. This article has 130 citations and is from a highest quality peer-reviewed journal.

34. (thieblemont2024epcoritamabinrelapsedrefractory pages 4-6): Catherine Thieblemont, Yasmin H. Karimi, Herve Ghesquieres, Chan Y. Cheah, Michael Roost Clausen, David Cunningham, Wojciech Jurczak, Young Rok Do, Robin Gasiorowski, David John Lewis, Tae Min Kim, Marjolein van der Poel, Michelle Limei Poon, Tatyana Feldman, Kim M. Linton, Anna Sureda, Martin Hutchings, Minh H. Dinh, Nurgul Kilavuz, David Soong, Thomas Mark, Mariana Sacchi, Tycel Phillips, and Pieternella J. Lugtenburg. Epcoritamab in relapsed/refractory large b-cell lymphoma: 2-year follow-up from the pivotal epcore nhl-1 trial. Leukemia, 38:2653-2662, Sep 2024. URL: https://doi.org/10.1038/s41375-024-02410-8, doi:10.1038/s41375-024-02410-8. This article has 130 citations and is from a highest quality peer-reviewed journal.
