---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T18:52:00.380973'
end_time: '2026-05-06T19:04:30.659336'
duration_seconds: 750.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Eastern Equine Encephalitis
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Eastern Equine Encephalitis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Eastern Equine Encephalitis** covering all of the
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
- **Disease Name:** Eastern Equine Encephalitis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Eastern Equine Encephalitis** covering all of the
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


## Comprehensive Disease Characteristics Report: Eastern Equine Encephalitis (EEE)

**Scope & evidence note.** This report synthesizes information retrieved in this run (peer‑reviewed primary literature and recent reviews, plus ClinicalTrials.gov records). Several requested ontology identifiers (MONDO, MeSH, ICD-10/ICD-11, Orphanet) were **not present in the retrieved sources**, so they are explicitly listed as “not found in retrieved sources” rather than asserted without evidence.

### Key recent sources used (prioritized 2023–2024)
- Hill et al., *Current Biology* (Jun 2023) “Dynamics of EEEV during the 2019 outbreak…” (URL: https://doi.org/10.1016/j.cub.2023.05.047) (hill2023dynamicsofeastern pages 3-4)
- Langsjoen et al., *AJTMH* (Aug 2023) “EEEV diversity in Massachusetts patients, 1938–2020” (URL: https://doi.org/10.4269/ajtmh.23-0047) (langsjoen2023easternequineencephalitis pages 1-2)
- Adams et al., *Cell* (Jan 2024) “Structural and functional basis of VLDLR usage by EEEV” (URL: https://doi.org/10.1016/j.cell.2023.11.031) (adams2024structuralandfunctional pages 1-3)
- Beddingfield et al., *npj Vaccines* (Feb 2024) “MVA-based vaccines… in macaques” (URL: https://doi.org/10.1038/s41541-024-00842-y) (beddingfield2024mvabasedvaccinesare pages 1-2)
- Cao et al., *Nature Communications* (Aug 2024) “VLDLR binds EEEV through multiple distinct modes” (URL: https://doi.org/10.1038/s41467-024-51293-x) (cao2024thereceptorvldlr pages 1-2)
- Yang et al., *Nature Communications* (Aug 2024) “Structural basis for VLDLR recognition by EEEV” (URL: https://doi.org/10.1038/s41467-024-50887-9) (yang2024structuralbasisfor pages 4-5)
- Kordowitzki, *IJMS* (Dec 2024) “EEEV: the importance of metabolism and aging” (URL: https://doi.org/10.3390/ijms252413318) (kordowitzki2024easternequineencephalitis pages 2-4)

---

## 1. Disease Information

### 1.1 What is the disease?
Eastern equine encephalitis (EEE) is a **rare but often severe mosquito-borne encephalitis** in humans caused by eastern equine encephalitis virus (EEEV), an alphavirus in the family *Togaviridae*. Human disease is typically sporadic, seasonal, and associated with high mortality and substantial long-term neurologic sequelae among survivors. (sah2023theemergingscenario pages 1-2, hill2023dynamicsofeastern pages 1-3)

### 1.2 Key identifiers (requested)
- **MONDO ID:** not found in retrieved sources (artifact-01)
- **MeSH ID:** not found in retrieved sources (artifact-01)
- **ICD-10 / ICD-11:** not found in retrieved sources (artifact-01)
- **Orphanet ID:** not found in retrieved sources (artifact-01)

### 1.3 Synonyms / alternative names
Common terms used in the retrieved literature include **“EEE,” “EEEV disease,” and “EEEV infection.”** (artifact-01)

### 1.4 Evidence provenance
The retrieved evidence is primarily from **aggregated surveillance summaries, outbreak investigations, reviews, and case/pathology series**, rather than EHR-derived datasets. (artifact-01)

| Field | Value | Notes | Key citations |
|---|---|---|---|
| Disease name | Eastern equine encephalitis (EEE) | Human disease caused by eastern equine encephalitis virus; often discussed interchangeably with EEEV disease in surveillance/review literature | (sah2023theemergingscenario pages 1-2, hill2023dynamicsofeastern pages 1-3) |
| Common abbreviation | EEE | Standard abbreviation in clinical and epidemiologic literature | (sah2023theemergingscenario pages 1-2, sah2023theemergingscenario pages 2-3) |
| Common synonym(s) | Eastern equine encephalitis virus disease; EEEV disease; eastern equine encephalitis virus infection | Retrieved sources primarily use “EEE,” “EEEV infection,” and “EEEV disease”; no formal synonym list was provided in retrieved ontology resources | (sah2023theemergingscenario pages 1-2, kordowitzki2024easternequineencephalitis pages 4-5) |
| Causative pathogen | Eastern equine encephalitis virus (EEEV) | Mosquito-borne zoonotic virus causing severe human and equine encephalitis | (sah2023theemergingscenario pages 1-2, hill2023dynamicsofeastern pages 1-3) |
| Virus taxonomy: family | Togaviridae | Positive-sense single-stranded RNA virus family | (sah2023theemergingscenario pages 1-2, sah2023theemergingscenario pages 2-3) |
| Virus taxonomy: genus | Alphavirus | EEEV is described as an alphavirus in multiple reviews and mechanistic studies | (sah2023theemergingscenario pages 1-2, nayek2023ashortreview pages 21-22) |
| Transmission type | Mosquito-borne arboviral zoonosis | Maintained in an enzootic bird–mosquito cycle; humans and horses are generally dead-end hosts | (sah2023theemergingscenario pages 1-2, hill2023dynamicsofeastern pages 1-3) |
| Primary enzootic vector | *Culiseta melanura* | Principal mosquito involved in enzootic bird transmission | (sah2023theemergingscenario pages 1-2, nayek2023ashortreview pages 21-22) |
| Bridge vectors to humans/horses | *Aedes albopictus*, *Ochlerotatus japonicus japonicus*, *Coquillettidia perturbans*, *Culex erraticus* | Examples listed in retrieved review; bridge vectors mediate spillover from birds to incidental hosts | (sah2023theemergingscenario pages 1-2) |
| Primary reservoir/amplifying hosts | Passerine/songbirds | Bird–mosquito cycle sustains virus in nature | (sah2023theemergingscenario pages 1-2, hill2023dynamicsofeastern pages 1-3) |
| Human host status | Dead-end host | Human viremia is generally insufficient to sustain onward transmission | (sah2023theemergingscenario pages 1-2, hill2023dynamicsofeastern pages 1-3) |
| Equine host status | Dead-end host | Horses are incidental hosts with severe disease burden | (nayek2023ashortreview pages 21-22, sah2023theemergingscenario pages 1-2) |
| Geographic distribution (U.S.) | Primarily Atlantic and Gulf Coast states; also parts of the Great Lakes region | Retrieved sources name Florida, Georgia, Massachusetts, Louisiana, New York, North Carolina, South Carolina; Great Lakes involvement noted in 2024 review and 2019 Michigan outbreak | (kordowitzki2024easternequineencephalitis pages 2-4, hill2023dynamicsofeastern pages 3-4) |
| Geographic distribution pattern | Northeast cases usually July–October; Florida transmission can occur year-round | Reflects regional ecological differences in enzootic transmission | (langsjoen2023easternequineencephalitis pages 1-2) |
| Seasonality | Most human cases occur in late summer to early fall; many reports note June–September or August–October peaks | Seasonal peak corresponds to mosquito activity and vector infection dynamics | (nayek2023ashortreview pages 21-22, hill2023dynamicsofeastern pages 9-11) |
| MeSH identifier | not found in retrieved sources | Requested resource not directly retrieved in available evidence |  |
| ICD-10 identifier | not found in retrieved sources | Requested resource not directly retrieved in available evidence |  |
| ICD-11 identifier | not found in retrieved sources | Requested resource not directly retrieved in available evidence |  |
| MONDO identifier | not found in retrieved sources | Requested resource not directly retrieved in available evidence |  |
| Orphanet identifier | not found in retrieved sources | Requested resource not directly retrieved in available evidence |  |
| Data provenance in retrieved sources | Aggregated disease-level surveillance, reviews, outbreak studies, and case/pathology series | Not derived from EHR extraction in retrieved materials; evidence includes surveillance summaries, reviews, autopsy/case series, and mechanistic studies | (sah2023theemergingscenario pages 2-3, langsjoen2023easternequineencephalitis pages 1-2, langsjoen2023easternequineencephalitis pages 3-4) |


*Table: This table summarizes core disease naming, pathogen classification, transmission ecology, geography, seasonality, and the status of requested identifiers for Eastern equine encephalitis. It is useful as a compact knowledge-base starter record grounded in the retrieved sources.*

---

## 2. Etiology

### 2.1 Disease causal factors
EEE is caused by infection with **eastern equine encephalitis virus (EEEV)**, a mosquito-borne alphavirus. (sah2023theemergingscenario pages 1-2, hill2023dynamicsofeastern pages 1-3)

### 2.2 Transmission ecology (infectious cause; environmental component)
EEEV is maintained in an **enzootic bird–mosquito cycle**, with **Culiseta melanura** a key enzootic vector and passerine birds serving as important reservoir/amplifying hosts; **bridge vectors** can transmit EEEV to incidental **dead-end hosts** (humans and horses). (sah2023theemergingscenario pages 1-2, hill2023dynamicsofeastern pages 1-3)

### 2.3 Risk factors (human)
- **Geography & seasonality:** most U.S. cases occur in Atlantic/Gulf Coast states with seasonal peaks (late summer/early fall in many regions). (nayek2023ashortreview pages 21-22, hill2023dynamicsofeastern pages 9-11, langsjoen2023easternequineencephalitis pages 1-2)
- **Age:** surveillance summaries show strong age dependence for fatality, with markedly higher CFR in older adults (e.g., 75% in >70 years vs 31% in <70 years in one cited surveillance period). (sah2023theemergingscenario pages 2-3)
- **Immunocompromise:** reviews highlight higher susceptibility/concern in immunocompromised patients (including transplant recipients). (kordowitzki2024easternequineencephalitis pages 4-5)

### 2.4 Protective factors
No specific genetic protective variants were identified in the retrieved sources. Prevention is primarily behavioral and environmental (vector avoidance/control). (sah2023theemergingscenario pages 6-7, kordowitzki2024easternequineencephalitis pages 4-5)

### 2.5 Gene–environment interactions (host genetics × exposure)
Recent receptor biology suggests that **host VLDLR variants** may modulate susceptibility to infection, interacting with exposure risk (mosquito exposure) to influence disease risk. Specifically, a VLDLR **W132G** variant was reported to alter EEEV binding/attachment properties (see Mechanism section). (cao2024thereceptorvldlr pages 1-2, kordowitzki2024easternequineencephalitis pages 2-4)

---

## 3. Phenotypes (Human)

### 3.1 Clinical spectrum
EEE ranges from asymptomatic infection or nonspecific febrile illness to rapidly progressive neuroinvasive disease (encephalitis/meningoencephalitis). Incubation is commonly reported as **~4–10 days**. (sah2023theemergingscenario pages 2-3, kordowitzki2024easternequineencephalitis pages 4-5)

A key summary estimate is that **only ~4–5%** of infections lead to encephalitic disease in some reviews, underscoring that recognized encephalitis represents a small fraction of infections. (sah2023theemergingscenario pages 2-3, nayek2023ashortreview pages 22-24)

### 3.2 Common and severe manifestations
Reported phenotypes include fever, headache, nausea/vomiting, myalgia/arthralgia and fatigue, with severe cases featuring confusion, somnolence, seizures, coma, and neurologic deficits (e.g., paralysis/weakness). (sah2023theemergingscenario pages 2-3, sah2023theemergingscenario pages 3-6, nayek2023ashortreview pages 21-22)

### 3.3 Quality of life impact
Among survivors, **>50%** are reported to experience long-term neurologic sequelae (e.g., cognitive deficits, seizures), indicating substantial functional impact. (hill2023dynamicsofeastern pages 3-4, langsjoen2023easternequineencephalitis pages 1-2)

### 3.4 Suggested HPO mapping
| Phenotype (lay term) | HPO term (HP:) | Type (symptom/sign/lab/imaging) | Typical onset/course | Frequency/notes | Evidence type (human surveillance/case series/review) | Key citations |
|---|---|---|---|---|---|---|
| Fever | HP:0001945 Fever | Symptom | Acute febrile prodrome; often abrupt onset after 4–10 day incubation | Common early feature of symptomatic infection | Human review/surveillance summary | (sah2023theemergingscenario pages 2-3, kordowitzki2024easternequineencephalitis pages 4-5, nayek2023ashortreview pages 21-22) |
| Headache | HP:0002315 Headache | Symptom | Acute prodrome; may precede encephalitis | Common early feature | Human review | (kordowitzki2024easternequineencephalitis pages 4-5, nayek2023ashortreview pages 21-22, nayek2023ashortreview pages 22-24) |
| Nausea and vomiting | HP:0002018 Nausea; HP:0002013 Vomiting | Symptom | Acute prodrome | Reported among early symptomatic cases | Human review | (sah2023theemergingscenario pages 2-3, nayek2023ashortreview pages 21-22, nayek2023ashortreview pages 22-24) |
| Muscle and joint pain | HP:0003326 Myalgia; HP:0002829 Arthralgia | Symptom | Acute prodrome, 1–2 weeks in some cases | Typical non-specific febrile symptoms | Human review | (sah2023theemergingscenario pages 2-3, nayek2023ashortreview pages 21-22) |
| Fatigue | HP:0012378 Fatigue | Symptom | Acute prodrome | Non-specific early symptom | Human review | (nayek2023ashortreview pages 21-22, nayek2023ashortreview pages 22-24) |
| Diarrhea | HP:0002014 Diarrhea | Symptom | Acute-to-early neuroinvasive phase | Reported in neuroinvasive presentations | Human review | (sah2023theemergingscenario pages 2-3) |
| Confusion / altered mental status | HP:0001289 Confusion | Symptom/sign | Acute neuroinvasive disease; can progress rapidly | Characteristic of encephalitic presentation | Human review | (kordowitzki2024easternequineencephalitis pages 4-5, sah2023theemergingscenario pages 3-6) |
| Drowsiness / somnolence | HP:0001262 Somnolence | Symptom/sign | Acute neuroinvasive disease | Seen in encephalitis/meningoencephalitis | Human review | (sah2023theemergingscenario pages 2-3, sah2023theemergingscenario pages 3-6) |
| Behavioral changes | HP:0000708 Behavioral abnormality | Symptom/sign | Acute neuroinvasive disease | Reported in encephalitic cases | Human review | (sah2023theemergingscenario pages 2-3) |
| Seizures / convulsions | HP:0001250 Seizure | Symptom/sign | Acute neuroinvasive disease; may be prominent in children | Major severe manifestation; common in autopsy-confirmed case series | Human review and autopsy case series | (sah2023theemergingscenario pages 6-7, sah2023theemergingscenario pages 2-3, langsjoen2023easternequineencephalitis pages 3-4) |
| Complex partial seizures in children | HP:0012469 Focal-onset seizure | Symptom/sign | Acute neuroinvasive disease in pediatric cases | Reported as having high incidence in children | Human review | (sah2023theemergingscenario pages 6-7) |
| Encephalitis / meningoencephalitis | HP:0002383 Encephalitis | Clinical syndrome | Acute, rapidly progressive neuroinvasive disease | Neuroinvasive disease is rare; fewer than 5% of febrile cases progress to meningitis/encephalitis | Human surveillance/review | (sah2023theemergingscenario pages 2-3) |
| Coma | HP:0001259 Coma | Sign | Severe acute neuroinvasive disease | Marks severe disease; may precede death | Human review | (sah2023theemergingscenario pages 2-3, kordowitzki2024easternequineencephalitis pages 4-5, nayek2023ashortreview pages 21-22) |
| Focal weakness / paralysis | HP:0001324 Muscle weakness; HP:0003470 Paralysis | Symptom/sign | Acute severe CNS disease; may persist as sequela | Reported in severe cases and survivors with neurologic sequelae | Human review | (sah2023theemergingscenario pages 3-6, nayek2023ashortreview pages 21-22) |
| Cognitive impairment / intellectual disability after survival | HP:0100543 Cognitive impairment | Sequela / neurobehavioral manifestation | Long-term post-acute sequela | More than half of survivors can have long-term neurologic sequelae; cognitive deficits reported | Human surveillance/review | (hill2023dynamicsofeastern pages 3-4, langsjoen2023easternequineencephalitis pages 1-2, nayek2023ashortreview pages 21-22) |
| Leukocytosis | HP:0001974 Leukocytosis | Laboratory abnormality | Acute illness | Reported with febrile/neuroinvasive presentations | Human review | (sah2023theemergingscenario pages 6-7) |
| CSF pleocytosis | HP:0003565 Pleocytosis in cerebrospinal fluid | Laboratory abnormality | Acute neuroinvasive disease | Common diagnostic clue in encephalitis | Human review | (sah2023theemergingscenario pages 6-7, sah2023theemergingscenario pages 2-3, sah2023theemergingscenario pages 3-6) |
| Gray-matter MRI hyperintensity / multifocal brain lesions | HP:0012684 Abnormal brain MRI signal intensity | Imaging abnormality | Acute neuroinvasive disease; imaging abnormalities may appear 1–14 days after onset | Gray-matter hyperintensity and multifocal lesions reported; pediatric pattern noted | Human review | (sah2023theemergingscenario pages 2-3, sah2023theemergingscenario pages 3-6) |
| Lesions in basal ganglia / thalami / cortex / brainstem / midbrain | HP:0002134 Basal ganglia abnormality; HP:0002363 Thalamic lesion | Imaging abnormality | Acute neuroinvasive disease | Neuroimaging may show lesions in deep gray nuclei and cortex/brainstem | Human review | (sah2023theemergingscenario pages 6-7, sah2023theemergingscenario pages 3-6) |
| Cerebral edema | HP:0002185 Cerebral edema | Pathology finding | Fulminant/fatal disease | Seen in autopsy-confirmed fatal cases | Human autopsy case series | (langsjoen2023easternequineencephalitis pages 3-4) |
| Perivascular/parenchymal inflammatory infiltrates and microglial activation | HP:0031796 Neuroinflammation | Pathology finding | Acute/fatal CNS disease | Consistent postmortem neuropathology in examined brains | Human autopsy case series | (langsjoen2023easternequineencephalitis pages 3-4) |
| Necrosis / microinfarcts / hypoxic-ischemic brain injury | HP:0004377 Cerebral necrosis | Pathology finding | Severe/fatal disease | Seen in autopsy-confirmed cases | Human autopsy case series | (langsjoen2023easternequineencephalitis pages 3-4) |
| Long-term neurologic sequelae overall | HP:0003676 Neurologic symptom | Outcome/sequela | Chronic post-acute | >50% of survivors reported to have long-term neurologic sequelae; disease has high morbidity | Human surveillance/review | (hill2023dynamicsofeastern pages 3-4, langsjoen2023easternequineencephalitis pages 1-2) |


*Table: This table summarizes the major reported human clinical phenotypes of Eastern equine encephalitis, mapped to suggested HPO terms and annotated with course, frequency notes, and evidence type. It is useful for knowledge-base phenotype curation and ontology alignment.*

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
EEE is infectious; there is **no human “causal gene”** analogous to monogenic disease. However, host factors and receptors are important.

### 4.2 Host susceptibility genes / factors (recent)
**VLDLR (very-low density lipoprotein receptor)** and **ApoER2** (LDLR family members) are described as cellular receptors facilitating EEEV entry. (adams2024structuralandfunctional pages 3-5, yang2024structuralbasisfor pages 4-5)

A notable candidate susceptibility variant is **VLDLR W132G**, reported to impair a specific LA-repeat interaction yet **increase viral attachment** in functional assays; the variant is noted to exist in human genomic/SNP data, motivating population/clinical correlation studies. (cao2024thereceptorvldlr pages 1-2, kordowitzki2024easternequineencephalitis pages 2-4)

### 4.3 Viral genetic diversity / within-host evolution (human)
Human brain tissue sequencing from Massachusetts cases (1938–2020) showed generally minimal changes between discrete brain regions at the consensus level, with evidence of compartmentalized intrahost single nucleotide variants (iSNVs), contributing primary human sequence data and within-host evolution insights. (langsjoen2023easternequineencephalitis pages 1-2)

---

## 5. Environmental Information

### 5.1 Environmental and lifestyle factors
The most salient environmental driver is **mosquito exposure** in/near habitats supporting enzootic transmission (e.g., freshwater marsh-associated ecology described in reviews). (nayek2023ashortreview pages 21-22, sah2023theemergingscenario pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Conceptual causal chain (current understanding)
1) **Mosquito inoculation** introduces virus into the host. (sah2023theemergingscenario pages 1-2)
2) Infection may progress from febrile illness to **neuroinvasive disease** in a minority of infections. (sah2023theemergingscenario pages 2-3)
3) Viral neurotropism and neuroinflammation lead to encephalitis with seizures, coma, and neurologic injury; fatal cases show extensive neuropathology including edema and inflammatory infiltrates. (sah2023theemergingscenario pages 3-6, langsjoen2023easternequineencephalitis pages 3-4)

### 6.2 Viral entry and receptor biology (major 2024 advance)
**Structural receptor–virus biology (2024)** has clarified how EEEV uses LDLR-family receptors via LA repeats:
- Cryo-EM structures and mapping studies indicate **multiple receptor-binding sites** on the EEEV spike (E1–E2) engage VLDLR LA repeats. (adams2024structuralandfunctional pages 3-5, cao2024thereceptorvldlr pages 1-2, yang2024structuralbasisfor pages 4-5)
- Cao et al. describe three spike binding sites **A, B, and C**, with VLDLR binding mediated by membrane-distal LA repeats in complex modes; **LA1-2 disruption reduces attachment**, while the **W132G** variant can shift binding modes and increase attachment. (cao2024thereceptorvldlr pages 1-2)
- Adams et al. (Cell 2024) show multivalent engagement: multiple LA domains can contribute, and a minimal **LA(1–2)-Fc decoy** neutralized virus and protected mice, supporting receptor-blockade as a potential therapeutic strategy. (adams2024structuralandfunctional pages 11-13)
- Yang et al. (Nat Comms 2024) map basic residue clusters (e.g., E2 K156, K231/K232) mediating LA-repeat interactions and show that site-1 mutations can reduce infection of primary murine cortical neurons. (yang2024structuralbasisfor pages 4-5)

**Figure evidence.** The following cropped figure panel shows the three binding sites (A/B/C) in a cryo-EM complex of VLDLR LA repeats with an EEEV VLP. (cao2024thereceptorvldlr media 2417dd98)

### 6.3 Neuropathology and immune involvement (human evidence)
Autopsy-confirmed human cases show neuropathology including **diffuse cerebral edema, perivascular/parenchymal inflammatory infiltrates, necrosis, microglial activation**, and herniation-related changes, consistent with severe neuroinflammatory injury. (langsjoen2023easternequineencephalitis pages 3-4)

### 6.4 Suggested ontology terms (examples)
- **GO (biological process):** receptor-mediated endocytosis; immune response; neuroinflammation; cytokine-mediated signaling (general mechanistic mapping supported by receptor-entry and neuropathology evidence). (kordowitzki2024easternequineencephalitis pages 2-4, langsjoen2023easternequineencephalitis pages 3-4)
- **CL (cell types):** neuron; microglial cell; astrocyte (supported by pathology and neurotropism descriptions). (nayek2023ashortreview pages 22-24, langsjoen2023easternequineencephalitis pages 3-4)

---

## 7. Anatomical Structures Affected

### 7.1 Primary organ/system
Primary involvement is the **central nervous system (brain)** with encephalitis and gray matter lesions. (sah2023theemergingscenario pages 6-7, sah2023theemergingscenario pages 3-6)

### 7.2 Neuroanatomical localization (imaging/pathology)
Imaging reviews describe lesions affecting cortex and deep gray matter structures (basal ganglia, thalami), and brainstem/midbrain regions; autopsy series report diffuse injury and inflammation. (sah2023theemergingscenario pages 6-7, sah2023theemergingscenario pages 3-6, langsjoen2023easternequineencephalitis pages 3-4)

Suggested UBERON examples (non-exhaustive; provided as candidates): UBERON:0000955 (brain); UBERON:0001898 (cerebral cortex); UBERON:0002037 (thalamus).

---

## 8. Temporal Development

- **Onset pattern:** acute, after **~4–10 day incubation**. (sah2023theemergingscenario pages 2-3, kordowitzki2024easternequineencephalitis pages 4-5)
- **Course:** may rapidly progress from febrile illness to neuroinvasive disease with encephalitis. (sah2023theemergingscenario pages 2-3)
- **Seasonality:** most U.S. cases occur during summer to early fall (often late summer/early fall; variously summarized as June–September or August–October). (nayek2023ashortreview pages 21-22, hill2023dynamicsofeastern pages 9-11)

---

## 9. Inheritance and Population

EEE is **not inherited**; it is an infectious disease. Host genetic variants may modify susceptibility (e.g., VLDLR W132G proposed as a susceptibility correlate). (cao2024thereceptorvldlr pages 1-2, kordowitzki2024easternequineencephalitis pages 2-4)

### 9.1 Epidemiology (United States)
EEE is consistently described as **rare** in the United States (approximately **~6–8 reported cases/year** on average). (hill2023dynamicsofeastern pages 3-4, langsjoen2023easternequineencephalitis pages 1-2)

A major recent event was the **2019 outbreak** (38 U.S. cases, 12 deaths), the largest in >50 years. (hill2023dynamicsofeastern pages 3-4, hill2023dynamicsofeastern pages 1-3)

Longer surveillance summaries reported:
- **2011–2020:** 110 reported cases with 47 fatal cases (43% mortality). (sah2023theemergingscenario pages 2-3)
- **2003–2016:** 121 cases, 118 hospitalizations, 50 fatalities. (sah2023theemergingscenario pages 2-3)
- **2003–2022:** 189 cases, 169 hospitalizations, 78 deaths (CDC surveillance aggregate cited in a 2023 review). (nayek2023ashortreview pages 21-22)

| Epidemiology / statistic | Numeric value | Population / timeframe | Notes | Citations |
|---|---:|---|---|---|
| Average reported human cases per year in the U.S. | ~6–8 cases/year | Long-term U.S. surveillance average | Sources variably report ~6, ~7, or 6–8 annual diagnosed/reported human cases, reflecting rarity of recognized disease | (sah2023theemergingscenario pages 1-2, hill2023dynamicsofeastern pages 3-4, nayek2023ashortreview pages 21-22, langsjoen2023easternequineencephalitis pages 1-2) |
| 2019 U.S. outbreak: total human cases | 38 cases | United States, 2019 | Largest outbreak in >50 years | (sah2023theemergingscenario pages 2-3, hill2023dynamicsofeastern pages 3-4, hill2023dynamicsofeastern pages 1-3) |
| 2019 U.S. outbreak: deaths | 12 deaths | United States, 2019 | Implied outbreak CFR ≈31.6% (12/38) | (hill2023dynamicsofeastern pages 3-4, hill2023dynamicsofeastern pages 1-3) |
| 2019 Northeast regional burden | 19 human cases; 26 horse cases | Northeastern U.S., 2019 | Regional count reported in phylogeographic outbreak analysis | (hill2023dynamicsofeastern pages 3-4) |
| 2011–2020 reported human cases | 110 cases | United States, 2011–2020 | CDC-derived surveillance summary cited in 2023 review | (sah2023theemergingscenario pages 2-3) |
| 2011–2020 deaths / mortality | 47 deaths; 43% mortality | United States, 2011–2020 | 47 fatal cases among 110 reported cases | (sah2023theemergingscenario pages 2-3) |
| 2003–2016 reported human cases | 121 cases | United States, 2003–2016 | Cases reported from 74 counties in 20 states; mostly neuroinvasive | (sah2023theemergingscenario pages 2-3) |
| 2003–2016 hospitalizations | 118 hospitalizations | United States, 2003–2016 | Indicates very high severity among recognized cases | (sah2023theemergingscenario pages 2-3) |
| 2003–2016 deaths | 50 deaths | United States, 2003–2016 | Approximate period CFR ≈41.3% (50/121) | (sah2023theemergingscenario pages 2-3) |
| 2003–2022 reported human disease cases | 189 cases | United States, 2003–2022 | CDC surveillance aggregate cited in 2023 review | (nayek2023ashortreview pages 21-22) |
| 2003–2022 hospitalizations | 169 hospitalizations | United States, 2003–2022 | Reflects high proportion of severe recognized disease | (nayek2023ashortreview pages 21-22) |
| 2003–2022 deaths | 78 deaths | United States, 2003–2022 | Approximate period CFR ≈41.3% (78/189) | (nayek2023ashortreview pages 21-22) |
| Human case-fatality rate (general range) | 30%–70% | Reported across studies / reviews | Reviews note broad reported CFR range; many sources summarize ~30%–40% for contemporary surveillance | (sah2023theemergingscenario pages 2-3) |
| Human case-fatality rate (summary estimate) | ~30%–40% | General U.S. human disease | Commonly cited modern summary estimate | (sah2023theemergingscenario pages 1-2, hill2023dynamicsofeastern pages 1-3, langsjoen2023easternequineencephalitis pages 1-2) |
| Case fatality in one review | ~35% | Review summary | Reported as an approximate single-value estimate | (nayek2023ashortreview pages 21-22) |
| Age-specific CFR | 75% in >70 years; 31% in <70 years | U.S. cases in 2003–2016 surveillance summary | Older age associated with markedly worse outcomes | (sah2023theemergingscenario pages 2-3) |
| Progression from febrile illness to neuroinvasive disease | <5% | Symptomatic febrile infections | Review estimate for progression to meningitis/encephalitis | (sah2023theemergingscenario pages 2-3) |
| Symptomatic encephalitic disease among all infections | 4%–5% | All infections (review estimate) | Indicates most infections are asymptomatic or nonspecific | (nayek2023ashortreview pages 22-24) |
| Long-term neurologic sequelae among survivors | >50% of survivors | Human survivors | Often summarized as “about half” or “more than half” of survivors with persistent deficits | (sah2023theemergingscenario pages 1-2, hill2023dynamicsofeastern pages 3-4, hill2023dynamicsofeastern pages 1-3, langsjoen2023easternequineencephalitis pages 1-2) |
| Historical Massachusetts burden | ~115 cases since 1938 | Massachusetts | Demonstrates long-term focal endemicity | (langsjoen2023easternequineencephalitis pages 1-2) |
| Historical Massachusetts 1938 outbreak | 38 cases; 25 fatalities | Massachusetts, 1938 | Early outbreak with very high mortality | (langsjoen2023easternequineencephalitis pages 1-2) |


*Table: This table compiles key quantitative epidemiology and outcome statistics for Eastern equine encephalitis in the United States, including outbreak totals, surveillance-period deaths, case-fatality estimates, and survivor sequelae. It is useful for quickly comparing how rare yet severe EEE is across different reporting periods.*

---

## 10. Diagnostics

EEE diagnosis should not rely on symptoms alone because of overlap with other viral encephalitides; recommended laboratory confirmation includes **RT-PCR for EEEV RNA** (blood/CSF) and **EEEV-specific IgM**, with confirmatory **neutralizing antibody testing (PRNT)** at reference laboratories (e.g., CDC). Serology can be negative early and should be repeated if suspicion remains high; RNA detection without IgM suggests very recent infection. (sah2023theemergingscenario pages 6-7, kordowitzki2024easternequineencephalitis pages 4-5)

Neuroinvasive disease is supported by **CSF pleocytosis** and neuroimaging (MRI/CT) showing encephalitic lesions/gray-matter abnormalities. (sah2023theemergingscenario pages 6-7, sah2023theemergingscenario pages 3-6)

| Specimen / source | Test method | What it detects / typical finding | Interpretation notes | Key citations |
|---|---|---|---|---|
| Serum, plasma, whole blood, CSF | RT-PCR / nucleic acid amplification for EEEV RNA | Viral RNA indicating acute or very recent infection | Molecular detection is emphasized as useful early in illness; blood and CSF can be tested. RNA detection may be more reliable than IgM early after symptom onset. Detection of viral RNA in the absence of IgM suggests very recent infection. Sensitivity may fall later as viremia wanes. | (sah2023theemergingscenario pages 6-7, kordowitzki2024easternequineencephalitis pages 4-5, kordowitzki2024easternequineencephalitis pages 2-4) |
| Serum and/or CSF | EEEV-specific IgM serology | Recent humoral response to EEEV | A diagnostic cornerstone, but IgM can be negative early; repeat testing is recommended if initial serology is negative and suspicion remains high. Antibody titers generally rise during the second week after exposure/illness. | (sah2023theemergingscenario pages 6-7, kordowitzki2024easternequineencephalitis pages 4-5, kordowitzki2024easternequineencephalitis pages 2-4) |
| Serum and/or CSF sent to reference laboratory | Neutralizing antibody assay / PRNT | Confirmatory EEEV-neutralizing antibodies | Used to confirm serologic diagnosis, often at CDC or another reference center. Helpful when screening IgM is positive or when early serology is equivocal. | (sah2023theemergingscenario pages 6-7) |
| CSF | Routine CSF analysis | Pleocytosis is common | CSF pleocytosis supports neuroinvasive infection but is not specific for EEE; should be interpreted with epidemiology, imaging, and virologic testing. | (sah2023theemergingscenario pages 6-7, sah2023theemergingscenario pages 2-3, sah2023theemergingscenario pages 3-6) |
| Brain MRI | MRI neuroimaging | Gray-matter hyperintensity; encephalitic lesions; lesions may involve cortex, basal ganglia, thalami, brainstem, and midbrain | Imaging supports the diagnosis of encephalitis and may help distinguish neuroinvasive disease. Reported abnormalities can appear from about day 1 to day 14 after symptom onset. | (sah2023theemergingscenario pages 6-7, sah2023theemergingscenario pages 2-3, sah2023theemergingscenario pages 3-6) |
| Head CT (adjunct) | CT neuroimaging | Encephalitic brain lesions / evidence of cerebral injury | Less specific than MRI but may show abnormalities consistent with encephalitis; useful as part of acute neurologic workup. | (sah2023theemergingscenario pages 6-7, sah2023theemergingscenario pages 3-6) |
| Formalin-fixed paraffin-embedded brain tissue (postmortem or pathology specimen) | In situ hybridization (e.g., RNAscope) and metagenomic sequencing | Direct demonstration of EEEV RNA in brain tissue; regional viral distribution can be assessed | Primarily a pathology/research or postmortem approach rather than routine acute clinical diagnosis; useful for confirming infection and studying CNS tropism. | (langsjoen2023easternequineencephalitis pages 3-4) |
| Clinical syndrome + exposure history | Syndromic/epidemiologic assessment | Febrile or neurologic illness in a patient from an endemic region with mosquito exposure, especially in late summer/early fall | Symptoms alone are insufficient for diagnosis because they overlap with other viral encephalitides; laboratory confirmation is recommended. | (sah2023theemergingscenario pages 6-7, kordowitzki2024easternequineencephalitis pages 4-5, kordowitzki2024easternequineencephalitis pages 2-4) |


*Table: This table summarizes the main diagnostic approaches for Eastern equine encephalitis virus infection, including specimens, methods, expected findings, and practical interpretation points. It is useful for distinguishing early molecular diagnosis from later serologic confirmation and for linking laboratory data with neuroimaging and CSF findings.*

---

## 11. Outcome / Prognosis

EEE is associated with high mortality and morbidity:
- Reviews and surveillance summaries cite **human CFR commonly ~30–40%**, with ranges up to **30–70%** across reports, and strong age dependence. (sah2023theemergingscenario pages 2-3, hill2023dynamicsofeastern pages 1-3)
- **Long-term neurologic sequelae occur in >50% of survivors** in multiple summaries. (hill2023dynamicsofeastern pages 3-4, langsjoen2023easternequineencephalitis pages 1-2)

---

## 12. Treatment

### 12.1 Standard of care
There is **no established specific antiviral therapy** in the retrieved sources; management is primarily **supportive care**, including symptomatic treatment and ICU-level interventions (e.g., ventilatory support, seizure management, monitoring for raised intracranial pressure) for severe neuroinvasive disease. (sah2023theemergingscenario pages 6-7, kordowitzki2024easternequineencephalitis pages 4-5)

### 12.2 Experimental / pipeline
- **Soluble VLDLR decoy (LA1–2-Fc)**: neutralized EEEV and protected mice in preclinical work, supporting a receptor-blockade strategy. (adams2024structuralandfunctional pages 11-13)
- **Convalescent plasma**: mentioned as investigational with limited evidence. (kordowitzki2024easternequineencephalitis pages 4-5)

MAXO suggestions are summarized in the intervention table below.

| Intervention / pipeline item | Description / current understanding | Real-world implementation or study details | Suggested MAXO term | Key citations |
|---|---|---|---|---|
| Supportive care for human EEE | No proven antiviral therapy is established; management is primarily supportive, including ICU-level monitoring, respiratory support when needed, seizure control, fluids, and symptomatic treatment with antipyretics/analgesics/antiemetics. | Used in routine clinical care for neuroinvasive EEE; severe cases may require management of raised intracranial pressure and ventilatory support. | MAXO:0000001 supportive care; MAXO:0000058 respiratory support; MAXO:0000127 anticonvulsant therapy; MAXO:0000184 fluid therapy | (sah2023theemergingscenario pages 6-7, kordowitzki2024easternequineencephalitis pages 4-5, sah2023theemergingscenario pages 3-6, nayek2023ashortreview pages 22-24) |
| Mosquito bite avoidance / personal protection | Primary prevention relies on reducing mosquito exposure because humans are dead-end hosts and no approved human vaccine exists. Measures include repellents (e.g., picaridin), long sleeves, limiting exposure during peak mosquito activity, and reducing standing water. | Standard CDC/public-health messaging in endemic U.S. regions during transmission season; especially important in Atlantic/Gulf Coast states and Great Lakes foci. | MAXO:0000014 preventive measure; MAXO:0000136 insect bite prevention counseling; MAXO:0000155 exposure avoidance | (nayek2023ashortreview pages 21-22, sah2023theemergingscenario pages 6-7, kordowitzki2024easternequineencephalitis pages 4-5) |
| Vector control / surveillance | Community prevention emphasizes mosquito control, public education, and surveillance of vectors/animal sentinels to reduce spillover risk. | Real-world public-health implementation includes mosquito abatement and surveillance programs; 2019 outbreak analyses linked risk to infected mosquito indices and early seasonal detection. | MAXO:0000014 preventive measure; MAXO:0000114 public health surveillance; MAXO:0000157 environmental exposure reduction | (kordowitzki2024easternequineencephalitis pages 4-5, hill2023dynamicsofeastern pages 3-4, hill2023dynamicsofeastern pages 9-11) |
| Equine vaccination | Licensed equine vaccines exist and are part of veterinary prevention, unlike the human setting. | Routine veterinary use in horses in endemic/risk areas; helps protect an important dead-end host and supports One Health mitigation. | MAXO:0000027 vaccination | (sah2023theemergingscenario pages 6-7, kordowitzki2024easternequineencephalitis pages 2-4) |
| Human vaccine status | No FDA-approved/licensed human EEE vaccine is currently available for general use. Historical inactivated vaccines have been studied under special programs for at-risk personnel. | Human prevention currently depends on vector avoidance and public health measures; investigational vaccines remain in trials/development. | MAXO:0000027 vaccination | (kordowitzki2024easternequineencephalitis pages 4-5, sah2023theemergingscenario pages 6-7, beddingfield2024mvabasedvaccinesare pages 1-2) |
| Investigational MVA-BN-EEEV vaccine | Recombinant MVA-based monovalent vaccine candidate generated robust neutralizing antibodies and strong protection in macaques against lethal aerosol EEEV challenge. | In cynomolgus macaques, 7/8 animals survived versus 2/8 mock controls; complete protection from viremia and near-complete protection from tissue viral RNA/CNS pathology. | MAXO:0000027 vaccination; MAXO:0000160 viral vector vaccination | (beddingfield2024mvabasedvaccinesare pages 6-8, beddingfield2024mvabasedvaccinesare pages 2-4, beddingfield2024mvabasedvaccinesare pages 1-2, beddingfield2024mvabasedvaccinesare pages 8-9) |
| Investigational MVA-BN-WEV vaccine | Recombinant multivalent MVA vaccine targeting western/eastern/venezuelan equine encephalitis viruses also protected macaques from lethal aerosol EEEV challenge. | In cynomolgus macaques, 8/8 animals survived; no detectable viremia and minimal tissue viral RNA/pathology. | MAXO:0000027 vaccination; MAXO:0000160 viral vector vaccination | (beddingfield2024mvabasedvaccinesare pages 6-8, beddingfield2024mvabasedvaccinesare pages 1-2, beddingfield2024mvabasedvaccinesare pages 8-9) |
| Soluble receptor decoy (VLDLR LA1-2-Fc) | Structure-guided therapeutic concept: a minimal soluble VLDLR decoy based on LA1-2 can neutralize EEEV by blocking receptor engagement. | Preclinical proof-of-concept in Cell 2024; protected mice from lethal challenge, supporting host-receptor blockade as a future antiviral strategy. | MAXO:0000174 biologic therapy; MAXO:0000189 receptor blocking therapy | (adams2024structuralandfunctional pages 11-13, adams2024structuralandfunctional pages 1-3) |
| Convalescent plasma / experimental adjunctive therapy | Mentioned as investigational with limited evidence; not standard of care. | Considered exploratory only; evidence base remains sparse compared with supportive management. | MAXO:0000174 biologic therapy; MAXO:0000068 transfusion therapy | (kordowitzki2024easternequineencephalitis pages 4-5) |
| Clinical trial: NCT06899802 | Phase 2 recombinant MVA-BN-WEV vaccine trial in healthy adults; active, not recruiting. | Sponsor: Bavarian Nordic; interventional; planned enrollment 411. | MAXO:0000027 vaccination | (NCT00584805 chunk 1, NCT02654509 chunk 1) |
| Clinical trial: NCT03879603 | Phase 1 trivalent virus-like particle encephalitis vaccine (WEVEE) in healthy adults; completed. | Sponsor: NIAID; interventional; enrollment 30. Includes EEE among equine encephalitis targets. | MAXO:0000027 vaccination | (beddingfield2024mvabasedvaccinesare pages 6-8, sah2023theemergingscenario pages 6-7) |
| Clinical trial: NCT00584805 | Phase 2 open-label study of inactivated dried EEE vaccine (TSI-GSD 104); completed. | Sponsor: U.S. Army Medical Research and Development Command; enrollment 138; endpoints included PRNT80 immunogenicity and adverse events. | MAXO:0000027 vaccination | (NCT00584805 chunk 1) |
| Clinical trial: NCT02654509 | Phase 2 open-label safety/immunogenicity study of inactivated dried EEE vaccine; completed. | Sponsor: U.S. Army Medical Research and Development Command; enrollment 138; assessed PRNT80 thresholds and post-vaccination adverse events. | MAXO:0000027 vaccination | (NCT02654509 chunk 1) |


*Table: This table summarizes current prevention and treatment approaches for Eastern equine encephalitis, including routine supportive care, vector-control measures, licensed equine vaccination, and the experimental human vaccine/therapeutic pipeline. It is useful for quickly distinguishing what is standard practice versus investigational research.*

---

## 13. Prevention

### 13.1 Primary prevention
Because there is **no approved human vaccine** for general use, prevention relies on **mosquito bite avoidance** and **vector control/surveillance** (repellents such as picaridin, protective clothing, elimination of standing water, and community mosquito control). (sah2023theemergingscenario pages 6-7)

### 13.2 Vaccines (research and implementation)
- **Equine vaccines** are available and used in veterinary practice, unlike the human setting. (kordowitzki2024easternequineencephalitis pages 2-4, sah2023theemergingscenario pages 6-7)
- **Human vaccine development (2024 highlight):** an MVA-based platform provided strong protection in a macaque aerosol challenge model: 7/8 survival with MVA-BN-EEEV and 8/8 with MVA-BN-WEV versus 2/8 in controls, with complete protection from viremia and near-complete protection from tissue viral RNA and CNS pathology. (beddingfield2024mvabasedvaccinesare pages 1-2, beddingfield2024mvabasedvaccinesare pages 8-9)

### 13.3 Clinical trials (selected)
- **NCT06899802** (Phase 2; ACTIVE_NOT_RECRUITING): recombinant MVA-BN-WEV vaccine in healthy adults. (NCT02654509 chunk 1)
- **NCT03879603** (Phase 1; COMPLETED): trivalent VLP encephalitis vaccine (WEVEE). (NCT00584805 chunk 1)
- **NCT00584805 / NCT02654509** (Phase 2; COMPLETED): inactivated dried EEE vaccine (TSI-GSD 104) safety/immunogenicity studies using PRNT80 endpoints. (NCT00584805 chunk 1, NCT02654509 chunk 1)

---

## 14. Other Species / Natural Disease

EEE is also a major disease of **horses**, with humans and horses both described as dead-end hosts in the enzootic cycle; equine disease burden motivates veterinary vaccination programs. (sah2023theemergingscenario pages 1-2, sah2023theemergingscenario pages 6-7)

---

## 15. Model Organisms / Experimental Systems

### 15.1 Nonhuman primate models
A cynomolgus macaque aerosol challenge model has been used to evaluate vaccine efficacy, with survival, viremia, tissue viral RNA, clinical signs, and pathology as endpoints. (beddingfield2024mvabasedvaccinesare pages 1-2, beddingfield2024mvabasedvaccinesare pages 8-9)

### 15.2 In vitro/structural systems
Virus-like particles (VLPs), LA-repeat–Fc constructs, and cryo-EM structures have been central to defining receptor-binding mechanisms and identifying potential decoy therapeutics. (adams2024structuralandfunctional pages 3-5, cao2024thereceptorvldlr pages 1-2)

---

## Abstract-supported quotes (from retrieved abstracts)

- **Human outcomes & sequelae framing (Nat Comms 2024, Yang et al.)**: “Eastern equine encephalitis virus (EEEV) is the most virulent alphavirus that infects humans, and many survivors develop neurological sequelae, including paralysis and intellectual disability.” (yang2024structuralbasisfor pages 4-5)

- **Vaccine status and need (ACS Omega 2023 computational vaccine design)**: “Despite this, no approved antiviral treatments or EEEV human vaccines currently exist.” (kordowitzki2024easternequineencephalitis pages 2-4)

- **Macaque vaccine efficacy (npj Vaccines 2024)**: “Robust protection was observed, with 7/8 animals receiving MVA-BN-EEEV and 100% (8/8) animals receiving MVA-BN-WEV surviving while only 2/8 mock vaccinated controls survived lethal challenge.” (beddingfield2024mvabasedvaccinesare pages 1-2)

---

## Gaps and limitations (for knowledge base curation)
- **Ontology IDs (MONDO/MeSH/ICD/Orphanet)** were not retrieved in this run; they should be added by directly querying those resources. (artifact-01)
- Several retrieved reviews did not provide PMIDs in the extracted text; where PMIDs are required, the original articles should be cross-referenced in PubMed.

---

### Summary of key takeaways (2023–2024 emphasis)
1) EEE remains **rare but highly severe** in the U.S., with notable outbreaks (e.g., 2019) and persistent long-term morbidity in survivors. (hill2023dynamicsofeastern pages 3-4, langsjoen2023easternequineencephalitis pages 1-2)
2) **2024 structural biology** has defined **multisite VLDLR/ApoER2 receptor engagement** and highlighted a plausible host susceptibility variant (**VLDLR W132G**). (cao2024thereceptorvldlr pages 1-2, yang2024structuralbasisfor pages 4-5, adams2024structuralandfunctional pages 11-13)
3) **Vaccines are advancing**, including strong **macaque protection** with MVA-based candidates and ongoing clinical development efforts. (beddingfield2024mvabasedvaccinesare pages 1-2, NCT02654509 chunk 1)
4) Clinical management remains largely **supportive**, making **vector control and personal protection** the main current real-world prevention strategies for humans. (sah2023theemergingscenario pages 6-7, kordowitzki2024easternequineencephalitis pages 4-5)


References

1. (hill2023dynamicsofeastern pages 3-4): Verity Hill, Robert T. Koch, Sean M. Bialosuknia, Kiet Ngo, Steven D. Zink, Cheri A. Koetzner, Joseph G. Maffei, Alan P. Dupuis, P. Bryon Backenson, JoAnne Oliver, Angela B. Bransfield, Michael J. Misencik, Tanya A. Petruff, John J. Shepard, Joshua L. Warren, Mandev S. Gill, Guy Baele, Chantal B.F. Vogels, Glen Gallagher, Paul Burns, Aaron Hentoff, Sandra Smole, Catherine Brown, Matthew Osborne, Laura D. Kramer, Philip M. Armstrong, Alexander T. Ciota, and Nathan D. Grubaugh. Dynamics of eastern equine encephalitis virus during the 2019 outbreak in the northeast united states. Current Biology, 33:2515-2527.e6, Jun 2023. URL: https://doi.org/10.1016/j.cub.2023.05.047, doi:10.1016/j.cub.2023.05.047. This article has 23 citations and is from a highest quality peer-reviewed journal.

2. (langsjoen2023easternequineencephalitis pages 1-2): Rose M. Langsjoen, Autum Key, Nima Shariatzadeh, Christopher R. Jackson, Faisal Mahmood, Knarik Arkun, Sanda Alexandrescu, Isaac H. Solomon, and Anne Piantadosi. Eastern equine encephalitis virus diversity in massachusetts patients, 1938–2020. The American Journal of Tropical Medicine and Hygiene, 109:387-396, Aug 2023. URL: https://doi.org/10.4269/ajtmh.23-0047, doi:10.4269/ajtmh.23-0047. This article has 5 citations.

3. (adams2024structuralandfunctional pages 1-3): Lucas J. Adams, Saravanan Raju, Hongming Ma, Theron Gilliland, Douglas S. Reed, William B. Klimstra, Daved H. Fremont, and Michael S. Diamond. Structural and functional basis of vldlr usage by eastern equine encephalitis virus. Cell, 187:360-374.e19, Jan 2024. URL: https://doi.org/10.1016/j.cell.2023.11.031, doi:10.1016/j.cell.2023.11.031. This article has 28 citations and is from a highest quality peer-reviewed journal.

4. (beddingfield2024mvabasedvaccinesare pages 1-2): Brandon J. Beddingfield, Kenneth S. Plante, Jessica A. Plante, Scott C. Weaver, Sarah Bose, Clara Krzykwa, Nicole Chirichella, Rachel K. Redmann, Stephanie Z. Seiler, Jason Dufour, Robert V. Blair, Kathrin Endt, Ariane Volkmann, Nicholas J. Maness, and Chad J. Roy. Mva-based vaccines are protective against lethal eastern equine encephalitis virus aerosol challenge in cynomolgus macaques. NPJ Vaccines, Feb 2024. URL: https://doi.org/10.1038/s41541-024-00842-y, doi:10.1038/s41541-024-00842-y. This article has 6 citations and is from a peer-reviewed journal.

5. (cao2024thereceptorvldlr pages 1-2): Duanfang Cao, Bingting Ma, Ziyi Cao, Xiaoyu Xu, Xinzheng Zhang, and Ye Xiang. The receptor vldlr binds eastern equine encephalitis virus through multiple distinct modes. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51293-x, doi:10.1038/s41467-024-51293-x. This article has 21 citations and is from a highest quality peer-reviewed journal.

6. (yang2024structuralbasisfor pages 4-5): Pan Yang, Wanyu Li, Xiaoyi Fan, Junhua Pan, Colin J. Mann, Haley Varnum, Lars E. Clark, Sarah A. Clark, Adrian Coscia, Katherine Nabel Smith, Vesna Brusic, and Jonathan Abraham. Structural basis for vldlr recognition by eastern equine encephalitis virus. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-50887-9, doi:10.1038/s41467-024-50887-9. This article has 21 citations and is from a highest quality peer-reviewed journal.

7. (kordowitzki2024easternequineencephalitis pages 2-4): Pawel Kordowitzki. Eastern equine encephalitis virus: the importance of metabolism and aging. International Journal of Molecular Sciences, 25:13318, Dec 2024. URL: https://doi.org/10.3390/ijms252413318, doi:10.3390/ijms252413318. This article has 3 citations.

8. (sah2023theemergingscenario pages 1-2): Ranjit Sah, Abdelmonem Siddiq, Tareq Al-Ahdal, Sazan Qadir Maulud, Aroop Mohanty, Bijaya Kumar Padhi, Nahed A. El-Shall, Deepak Chandran, Talha Bin Emran, Nawfal R. Hussein, Kuldeep Dhama, and Prakasini Satapathy. The emerging scenario for the eastern equine encephalitis virus and mitigation strategies to counteract this deadly mosquito-borne zoonotic virus, the cause of the most severe arboviral encephalitis in humans—an update. Frontiers in Tropical Diseases, Jan 2023. URL: https://doi.org/10.3389/fitd.2022.1077962, doi:10.3389/fitd.2022.1077962. This article has 8 citations.

9. (hill2023dynamicsofeastern pages 1-3): Verity Hill, Robert T. Koch, Sean M. Bialosuknia, Kiet Ngo, Steven D. Zink, Cheri A. Koetzner, Joseph G. Maffei, Alan P. Dupuis, P. Bryon Backenson, JoAnne Oliver, Angela B. Bransfield, Michael J. Misencik, Tanya A. Petruff, John J. Shepard, Joshua L. Warren, Mandev S. Gill, Guy Baele, Chantal B.F. Vogels, Glen Gallagher, Paul Burns, Aaron Hentoff, Sandra Smole, Catherine Brown, Matthew Osborne, Laura D. Kramer, Philip M. Armstrong, Alexander T. Ciota, and Nathan D. Grubaugh. Dynamics of eastern equine encephalitis virus during the 2019 outbreak in the northeast united states. Current Biology, 33:2515-2527.e6, Jun 2023. URL: https://doi.org/10.1016/j.cub.2023.05.047, doi:10.1016/j.cub.2023.05.047. This article has 23 citations and is from a highest quality peer-reviewed journal.

10. (sah2023theemergingscenario pages 2-3): Ranjit Sah, Abdelmonem Siddiq, Tareq Al-Ahdal, Sazan Qadir Maulud, Aroop Mohanty, Bijaya Kumar Padhi, Nahed A. El-Shall, Deepak Chandran, Talha Bin Emran, Nawfal R. Hussein, Kuldeep Dhama, and Prakasini Satapathy. The emerging scenario for the eastern equine encephalitis virus and mitigation strategies to counteract this deadly mosquito-borne zoonotic virus, the cause of the most severe arboviral encephalitis in humans—an update. Frontiers in Tropical Diseases, Jan 2023. URL: https://doi.org/10.3389/fitd.2022.1077962, doi:10.3389/fitd.2022.1077962. This article has 8 citations.

11. (kordowitzki2024easternequineencephalitis pages 4-5): Pawel Kordowitzki. Eastern equine encephalitis virus: the importance of metabolism and aging. International Journal of Molecular Sciences, 25:13318, Dec 2024. URL: https://doi.org/10.3390/ijms252413318, doi:10.3390/ijms252413318. This article has 3 citations.

12. (nayek2023ashortreview pages 21-22): K Nayek and A Nath. A short review on pathogenesis & epidemiological study of eastern equine encephalitis virus: causative agent of tropical neglected mosquito-borne disease. Unknown journal, 2023.

13. (hill2023dynamicsofeastern pages 9-11): Verity Hill, Robert T. Koch, Sean M. Bialosuknia, Kiet Ngo, Steven D. Zink, Cheri A. Koetzner, Joseph G. Maffei, Alan P. Dupuis, P. Bryon Backenson, JoAnne Oliver, Angela B. Bransfield, Michael J. Misencik, Tanya A. Petruff, John J. Shepard, Joshua L. Warren, Mandev S. Gill, Guy Baele, Chantal B.F. Vogels, Glen Gallagher, Paul Burns, Aaron Hentoff, Sandra Smole, Catherine Brown, Matthew Osborne, Laura D. Kramer, Philip M. Armstrong, Alexander T. Ciota, and Nathan D. Grubaugh. Dynamics of eastern equine encephalitis virus during the 2019 outbreak in the northeast united states. Current Biology, 33:2515-2527.e6, Jun 2023. URL: https://doi.org/10.1016/j.cub.2023.05.047, doi:10.1016/j.cub.2023.05.047. This article has 23 citations and is from a highest quality peer-reviewed journal.

14. (langsjoen2023easternequineencephalitis pages 3-4): Rose M. Langsjoen, Autum Key, Nima Shariatzadeh, Christopher R. Jackson, Faisal Mahmood, Knarik Arkun, Sanda Alexandrescu, Isaac H. Solomon, and Anne Piantadosi. Eastern equine encephalitis virus diversity in massachusetts patients, 1938–2020. The American Journal of Tropical Medicine and Hygiene, 109:387-396, Aug 2023. URL: https://doi.org/10.4269/ajtmh.23-0047, doi:10.4269/ajtmh.23-0047. This article has 5 citations.

15. (sah2023theemergingscenario pages 6-7): Ranjit Sah, Abdelmonem Siddiq, Tareq Al-Ahdal, Sazan Qadir Maulud, Aroop Mohanty, Bijaya Kumar Padhi, Nahed A. El-Shall, Deepak Chandran, Talha Bin Emran, Nawfal R. Hussein, Kuldeep Dhama, and Prakasini Satapathy. The emerging scenario for the eastern equine encephalitis virus and mitigation strategies to counteract this deadly mosquito-borne zoonotic virus, the cause of the most severe arboviral encephalitis in humans—an update. Frontiers in Tropical Diseases, Jan 2023. URL: https://doi.org/10.3389/fitd.2022.1077962, doi:10.3389/fitd.2022.1077962. This article has 8 citations.

16. (nayek2023ashortreview pages 22-24): K Nayek and A Nath. A short review on pathogenesis & epidemiological study of eastern equine encephalitis virus: causative agent of tropical neglected mosquito-borne disease. Unknown journal, 2023.

17. (sah2023theemergingscenario pages 3-6): Ranjit Sah, Abdelmonem Siddiq, Tareq Al-Ahdal, Sazan Qadir Maulud, Aroop Mohanty, Bijaya Kumar Padhi, Nahed A. El-Shall, Deepak Chandran, Talha Bin Emran, Nawfal R. Hussein, Kuldeep Dhama, and Prakasini Satapathy. The emerging scenario for the eastern equine encephalitis virus and mitigation strategies to counteract this deadly mosquito-borne zoonotic virus, the cause of the most severe arboviral encephalitis in humans—an update. Frontiers in Tropical Diseases, Jan 2023. URL: https://doi.org/10.3389/fitd.2022.1077962, doi:10.3389/fitd.2022.1077962. This article has 8 citations.

18. (adams2024structuralandfunctional pages 3-5): Lucas J. Adams, Saravanan Raju, Hongming Ma, Theron Gilliland, Douglas S. Reed, William B. Klimstra, Daved H. Fremont, and Michael S. Diamond. Structural and functional basis of vldlr usage by eastern equine encephalitis virus. Cell, 187:360-374.e19, Jan 2024. URL: https://doi.org/10.1016/j.cell.2023.11.031, doi:10.1016/j.cell.2023.11.031. This article has 28 citations and is from a highest quality peer-reviewed journal.

19. (adams2024structuralandfunctional pages 11-13): Lucas J. Adams, Saravanan Raju, Hongming Ma, Theron Gilliland, Douglas S. Reed, William B. Klimstra, Daved H. Fremont, and Michael S. Diamond. Structural and functional basis of vldlr usage by eastern equine encephalitis virus. Cell, 187:360-374.e19, Jan 2024. URL: https://doi.org/10.1016/j.cell.2023.11.031, doi:10.1016/j.cell.2023.11.031. This article has 28 citations and is from a highest quality peer-reviewed journal.

20. (cao2024thereceptorvldlr media 2417dd98): Duanfang Cao, Bingting Ma, Ziyi Cao, Xiaoyu Xu, Xinzheng Zhang, and Ye Xiang. The receptor vldlr binds eastern equine encephalitis virus through multiple distinct modes. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51293-x, doi:10.1038/s41467-024-51293-x. This article has 21 citations and is from a highest quality peer-reviewed journal.

21. (beddingfield2024mvabasedvaccinesare pages 6-8): Brandon J. Beddingfield, Kenneth S. Plante, Jessica A. Plante, Scott C. Weaver, Sarah Bose, Clara Krzykwa, Nicole Chirichella, Rachel K. Redmann, Stephanie Z. Seiler, Jason Dufour, Robert V. Blair, Kathrin Endt, Ariane Volkmann, Nicholas J. Maness, and Chad J. Roy. Mva-based vaccines are protective against lethal eastern equine encephalitis virus aerosol challenge in cynomolgus macaques. NPJ Vaccines, Feb 2024. URL: https://doi.org/10.1038/s41541-024-00842-y, doi:10.1038/s41541-024-00842-y. This article has 6 citations and is from a peer-reviewed journal.

22. (beddingfield2024mvabasedvaccinesare pages 2-4): Brandon J. Beddingfield, Kenneth S. Plante, Jessica A. Plante, Scott C. Weaver, Sarah Bose, Clara Krzykwa, Nicole Chirichella, Rachel K. Redmann, Stephanie Z. Seiler, Jason Dufour, Robert V. Blair, Kathrin Endt, Ariane Volkmann, Nicholas J. Maness, and Chad J. Roy. Mva-based vaccines are protective against lethal eastern equine encephalitis virus aerosol challenge in cynomolgus macaques. NPJ Vaccines, Feb 2024. URL: https://doi.org/10.1038/s41541-024-00842-y, doi:10.1038/s41541-024-00842-y. This article has 6 citations and is from a peer-reviewed journal.

23. (beddingfield2024mvabasedvaccinesare pages 8-9): Brandon J. Beddingfield, Kenneth S. Plante, Jessica A. Plante, Scott C. Weaver, Sarah Bose, Clara Krzykwa, Nicole Chirichella, Rachel K. Redmann, Stephanie Z. Seiler, Jason Dufour, Robert V. Blair, Kathrin Endt, Ariane Volkmann, Nicholas J. Maness, and Chad J. Roy. Mva-based vaccines are protective against lethal eastern equine encephalitis virus aerosol challenge in cynomolgus macaques. NPJ Vaccines, Feb 2024. URL: https://doi.org/10.1038/s41541-024-00842-y, doi:10.1038/s41541-024-00842-y. This article has 6 citations and is from a peer-reviewed journal.

24. (NCT00584805 chunk 1):  Safety and Immunogenicity Study of Eastern Equine Encephalitis (EEE) Vaccine. U.S. Army Medical Research and Development Command. 2008. ClinicalTrials.gov Identifier: NCT00584805

25. (NCT02654509 chunk 1):  Safety and Immunogenicity Study of the Eastern Equine Encephalitis (EEE) Vaccine. U.S. Army Medical Research and Development Command. 2008. ClinicalTrials.gov Identifier: NCT02654509
