---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:42:50.312847'
end_time: '2026-04-04T12:49:22.510845'
duration_seconds: 392.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MYO6 Hearing Loss
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MYO6 Hearing Loss
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MYO6 Hearing Loss** covering all of the
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
- **Disease Name:** MYO6 Hearing Loss
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MYO6 Hearing Loss** covering all of the
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


## Comprehensive Research Report: MYO6 Hearing Loss (DFNA22 / DFNB37)

### Executive summary
MYO6-related hearing loss comprises non-syndromic sensorineural hearing loss (SNHL) caused by pathogenic variants in **MYO6 (myosin VI)**. Two canonical Mendelian entities are recognized in the literature: **DFNA22 (autosomal dominant NSHL)** and **DFNB37 (autosomal recessive NSHL)**. Clinical presentation is typically postlingual and progressive in DFNA22, with variable onset and severity; DFNB37 represents recessive disease reported in prior families and summarized in later cohorts and reviews. Quantitative cohort data indicate MYO6 is a non-trivial contributor to autosomal dominant SNHL (e.g., ~2.4% in a large Japanese ADSNHL cohort), with measurable progression rates and characteristic hair-cell structural/synaptic mechanisms. Recent 2024 studies expand variant spectrum and provide functional validation in zebrafish and mouse models, while a 2022 gene-editing study demonstrates preclinical therapeutic rescue in a semi-dominant mouse model. (oka2020clinicalcharacteristicsand pages 1-3, kim2018aclinicalguidance pages 5-8, miyoshi2024pathophysiologyofhuman pages 1-2, yin2023functionalanddevelopmental pages 1-2, buonfiglio2024insilicoand pages 2-4, xue2022geneeditingin pages 1-2)

| Disease / scope | Inheritance | Key cohort / clinical statistics | Representative variant(s) | Study (year, journal) | URL | Key mechanistic note | Evidence |
|---|---|---|---|---|---|---|---|
| DFNA22 (MYO6-related dominant nonsyndromic hearing loss) | Autosomal dominant | In a Japanese cohort, MYO6 variants explained 2.40% of autosomal dominant sensorineural hearing loss (32/1336 families); overall deterioration estimated at 0.57 dB/year, accelerating to 1.07 dB/year after age 40 | Multiple truncating, splice, missense variants; recurrent p.R1166X noted across families | Oka et al. 2020, *Genes* | https://doi.org/10.3390/genes11030273 | Mutant MYO6 shortened espin1-induced microvilli in CL4 cells, supporting malformed stereocilia as a disease mechanism | (oka2020clinicalcharacteristicsand pages 1-3, oka2020clinicalcharacteristicsand pages 3-5) |
| DFNA22 (Korean ADNSHL cohort guidance) | Autosomal dominant | DFNA22 frequency 6.2% (5/81) in one Korean ADNSHL cohort; combined Korean cohorts 6.7% (9/134); most cases moderate, gradually progressive, often with preserved speech scores | p.R205X recurrent in 3/5 MYO6 families (~60%); novel p.G223R, p.T158R | Kim et al. 2018, *The Journal of Gene Medicine* | https://doi.org/10.1002/jgm.3019 | MYO6 is concentrated in the actin-rich cuticular plate and helps anchor/stabilize stereocilia; clinical profile supports hearing aids or middle-ear implants, CI in selected cases | (kim2018aclinicalguidance pages 1-5, kim2018aclinicalguidance pages 5-8) |
| Foundational DFNA22 family | Autosomal dominant | Childhood/postlingual onset with first audiometric abnormalities at 6–8 years, symptoms at 8–10 years; by ~50 years, affected individuals typically had profound sensorineural deafness | p.C442Y | Melchionda et al. 2001, *American Journal of Human Genetics* | https://doi.org/10.1086/323156 | First human MYO6 deafness report; mapped DFNA22 to 6q13 and linked MYO6 motor-domain dysfunction to progressive hearing loss | (melchionda2001myo6thehuman pages 1-3) |
| DFNA22 semi-dominant therapeutic model | Semi-dominant mouse model of dominant MYO6 disease | In vivo allele-selective editing efficiency of mutant allele averaged 4.05%; rescue of ABR, DPOAE, hair-bundle morphology, and calcium homeostasis observed up to 5 months after treatment | p.C442Y | Xue et al. 2022, *Molecular Therapy* | https://doi.org/10.1016/j.ymthe.2021.06.015 | Supports dominant-negative / toxic mutant allele targeting as a plausible therapeutic strategy; MYO6 is localized near stereocilia base/cuticular plate | (xue2022geneeditingin pages 1-2) |
| DFNA22 / early-onset Chinese family | Autosomal dominant presentation reported for cis MYO6 alleles | Progressive sensorineural hearing loss with onset around 8–10 years; severe, progressive course | cis p.Trp793Gly + p.Lys794Asn | Ji et al. 2024, *Frontiers in Genetics* | https://doi.org/10.3389/fgene.2023.1275633 | MYO6 is essential for stereocilia bundle organization, mechanotransduction, endocytosis, ion-channel regulation, anchoring of stereocilia, and vesicle movement | (ji2024novelciscompound pages 1-2, ji2024novelciscompound pages 2-3) |
| Dominant Argentine family with functional validation | Autosomal dominant | Postlingual progressive hearing loss with variable expressivity; affected relatives had onset in their 30s; mild-moderate to severe/profound HL reported; one family member received CI | p.Arg925Ser | Buonfiglio et al. 2024, *NAR Genomics and Bioinformatics* | https://doi.org/10.1093/nargab/lqae162 | Structural modeling showed altered electrostatic charge in the SAH region; zebrafish rescue assays supported reduced MYO6 function in auditory hair-cell biology | (buonfiglio2024insilicoand pages 1-2, buonfiglio2024insilicoand pages 2-4, buonfiglio2024insilicoand media e17c45f9, buonfiglio2024insilicoand media 24cec060) |
| DFNB37 / recessive MYO6-related hearing loss | Autosomal recessive | MYO6 is established as a cause of recessive nonsyndromic hearing loss; specific prevalence is less well quantified than DFNA22 in available excerpts | Recessive MYO6 variants including nonsense, frameshift, missense reported in prior literature | Ahmed et al. 2003 and summarized in later reviews/cohorts | Not available in retrieved full text; summarized in later studies | Loss of MYO6 function disrupts stereocilia maintenance and can produce fused/branched stereocilia, consistent with loss-of-function pathogenesis | (kim2018aclinicalguidance pages 1-5, hilgert2008asplicesitemutation pages 1-2, oka2020clinicalcharacteristicsand pages 12-13) |
| Inner-hair-cell synaptic pathophysiology | Model-organism mechanistic evidence relevant to DFNA22/DFNB37 | In Myo6 knockout mice, exocytosis from IHCs was significantly reduced before and after hearing onset; mature p.C442Y/C442Y IHCs also showed reduced exocytosis and calcium current | knockout Myo6−/−; p.C442Y | Yin et al. 2023, *Cell Death Discovery* | https://doi.org/10.1038/s41420-023-01473-3 | Demonstrates ribbon-synapse dysfunction downstream of MYO6 defects: smaller readily releasable pool and slower sustained release contribute to hearing loss | (yin2023functionalanddevelopmental pages 1-2) |
| MYO6 function in hair cells (review synthesis) | Dominant and recessive forms summarized | Review-level synthesis, not a prevalence study | Multiple ClinVar/pathogenic MYO6 variants | Miyoshi et al. 2024, *Frontiers in Physiology* | https://doi.org/10.3389/fphys.2024.1374901 | MYO6 uniquely moves toward the pointed end of F-actin and “tethers plasma membrane to the F-actin core, keeps stereocilia in place and mediates vesicle transport including endocytosis” | (miyoshi2024pathophysiologyofhuman pages 5-6, miyoshi2024pathophysiologyofhuman pages 1-2) |


*Table: This table condenses key disease-entity, genotype, clinical, and mechanistic facts for MYO6-related hearing loss into a knowledge-base-ready format. It emphasizes dominant DFNA22, recessive DFNB37, quantitative cohort data, representative variants, and recent mechanistic studies.*

---

## 1. Disease information

### 1.1 What is the disease?
**MYO6 hearing loss** refers to **hereditary non-syndromic sensorineural hearing loss** caused by pathogenic variants in **MYO6**, encoding the unconventional actin motor **myosin VI** expressed in cochlear hair cells. Dominant disease is historically mapped as **DFNA22**, and recessive disease is referred to as **DFNB37** in the hearing-loss locus nomenclature. (alde2023autosomaldominantnonsyndromic pages 10-11, kim2018aclinicalguidance pages 1-5, melchionda2001myo6thehuman pages 1-3)

### 1.2 Key identifiers (available from retrieved sources)
- **Gene:** MYO6 (myosin VI)
- **OMIM Gene (MIM):** **600970** (reported in the foundational DFNA22 mapping report) (melchionda2001myo6thehuman pages 1-3)
- **Locus / disease designations:** **DFNA22** (autosomal dominant NSHL), **DFNB37** (autosomal recessive NSHL) (kim2018aclinicalguidance pages 1-5, hilgert2008asplicesitemutation pages 1-2, melchionda2001myo6thehuman pages 1-3)
- **Cytogenetic locus:** reported as **6q13** in early mapping and many clinical series; later papers also cite **6q14.1** for MYO6 (melchionda2001myo6thehuman pages 1-3, ji2024novelciscompound pages 1-2)

**Not retrievable from the currently accessed full texts:** MONDO disease ID for “MYO6 hearing loss”, Orphanet ID, MeSH identifier, and ICD-10/ICD-11 code mapping. These should be filled by direct queries to OMIM/Orphanet/MONDO/MeSH/ICD resources in a subsequent curation pass.

### 1.3 Synonyms / alternative names
- DFNA22 hearing loss; MYO6-related autosomal dominant non-syndromic hearing loss (ADNSHL) (kim2018aclinicalguidance pages 1-5, melchionda2001myo6thehuman pages 1-3)
- DFNB37 hearing loss; MYO6-related autosomal recessive non-syndromic hearing loss (ARNSHL) (kim2018aclinicalguidance pages 1-5, hilgert2008asplicesitemutation pages 1-2)
- Non-syndromic sensorineural hearing loss due to MYO6 variants (oka2020clinicalcharacteristicsand pages 1-3)

### 1.4 Evidence source type
Evidence summarized here is primarily from **aggregated cohort studies and primary family studies** (human genetics/audiology), complemented by **mouse and zebrafish functional studies** and **mechanistic review synthesis**. (oka2020clinicalcharacteristicsand pages 1-3, yin2023functionalanddevelopmental pages 1-2, buonfiglio2024insilicoand pages 2-4, xue2022geneeditingin pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** pathogenic germline variants in **MYO6**, producing altered myosin VI function in hair cells, which disrupts stereocilia architecture, membrane–actin tethering/endocytic trafficking, and/or inner hair cell synaptic physiology. (oka2020clinicalcharacteristicsand pages 1-3, miyoshi2024pathophysiologyofhuman pages 5-6, yin2023functionalanddevelopmental pages 1-2)

### 2.2 Risk factors
- **Genetic:** family history consistent with autosomal dominant (DFNA22) or autosomal recessive (DFNB37) inheritance; specific variants including truncating, splice, and missense variants in MYO6. (oka2020clinicalcharacteristicsand pages 1-3, kim2018aclinicalguidance pages 1-5, hilgert2008asplicesitemutation pages 1-2)
- **Environmental:** For the Argentine family report, common environmental causes (ototoxic drugs, infection, acoustic trauma) were explicitly ruled out during clinical assessment, supporting a genetic etiology. (buonfiglio2024insilicoand pages 2-4)

### 2.3 Protective factors / gene–environment interaction
No MYO6-specific protective variants or gene–environment interaction evidence was identified in the retrieved texts.

---

## 3. Phenotypes (clinical presentation)

### 3.1 Core phenotype
- **Sensorineural hearing loss** that is frequently **postlingual** and **progressive** in DFNA22, with variable severity (mild to profound) and variable audiogram configurations reported across families and cohorts. (kim2018aclinicalguidance pages 5-8, melchionda2001myo6thehuman pages 1-3)

### 3.2 Age of onset, severity, progression (quantitative where available)
- In the foundational DFNA22 Italian family (MYO6 missense p.C442Y), onset occurred in childhood (symptoms ~8–10 years; first audiometric abnormalities ~6–8 years) and individuals “invariably have profound sensorineural deafness” by ~50 years. (melchionda2001myo6thehuman pages 1-3)
- In a large Japanese cohort study (8074 families), most MYO6-associated cases were juvenile-onset, progressive, and **deterioration accelerated after age 40**; estimated progression **0.57 dB/year overall** and **1.07 dB/year after age 40**. (oka2020clinicalcharacteristicsand pages 1-3)
- In a Korean DFNA22 cohort, onset ranged from perilingual to late-forties and the severity was often moderate with gradual progression and relatively preserved speech scores (≥60% reported in their summary of cohort phenotype). (kim2018aclinicalguidance pages 5-8)
- In a 2024 Chinese family report, affected relatives had **progressive SNHL with onset around 8–10 years**, described as severe and progressive. (ji2024novelciscompound pages 1-2)
- In a 2024 Argentine family report, multiple affected members had postlingual progressive HL; mild–moderate cases were described in several individuals and severe–profound in one; onset in their thirties is described for affected women in the figure caption text, and hearing aids were used by most affected individuals, with one cochlear implant recipient. (buonfiglio2024insilicoand pages 2-4, buonfiglio2024insilicoand media e17c45f9)

### 3.3 HPO term suggestions (non-exhaustive)
Based on reported phenotypes:
- Hearing impairment: **HP:0000365** (supported by general association context) (miyoshi2024pathophysiologyofhuman pages 1-2)
- Sensorineural hearing impairment: **HP:0000407** (implied across cohorts describing SNHL) (oka2020clinicalcharacteristicsand pages 1-3, ji2024novelciscompound pages 1-2)
- Progressive hearing impairment: **HP:0001733** (progression described across families/cohorts) (oka2020clinicalcharacteristicsand pages 1-3, melchionda2001myo6thehuman pages 1-3)
- Postlingual onset hearing impairment: **HP:0008554** (postlingual described) (melchionda2001myo6thehuman pages 1-3)

### 3.4 Quality of life impact
No disease-specific QoL instruments (e.g., EQ-5D/SF-36) were reported in the retrieved texts; functional impact is inferred from the need for hearing aids and occasional cochlear implantation. (kim2018aclinicalguidance pages 5-8, buonfiglio2024insilicoand media e17c45f9)

---

## 4. Genetic / molecular information

### 4.1 Causal gene
- **MYO6** encodes **myosin VI**, an unconventional actin motor. (kim2018aclinicalguidance pages 1-5, melchionda2001myo6thehuman pages 1-3)

### 4.2 Pathogenic variants and classes
Cohorts demonstrate a broad variant spectrum including nonsense, frameshift, splice-site, and missense variants:
- Japanese cohort: 27 variants across 33 families (including nonsense, frameshift, splicing, and missense); ACMG classification included pathogenic/likely pathogenic/VUS calls. (oka2020clinicalcharacteristicsand pages 3-5)
- Korean cohort: recurrent truncation **p.R205X** and novel missense **p.G223R** and **p.T158R** (motor domain). (kim2018aclinicalguidance pages 5-8)
- Foundational DFNA22: missense **p.C442Y** segregating in an Italian family. (melchionda2001myo6thehuman pages 1-3)
- 2024 Chinese family: cis compound heterozygous variants **p.Trp793Gly** and **p.Lys794Asn** associated with early-onset progressive SNHL. (ji2024novelciscompound pages 1-2)
- 2024 Argentine family: novel **c.2775G>C (p.Arg925Ser)** classified as likely pathogenic using ACMG/AMP and ClinGen hearing-loss gene-specific criteria; functional validation in zebrafish supported reduced function. (buonfiglio2024insilicoand pages 2-4)

**Allele frequency:** Buonfiglio et al. describe filtering for variants <0.1% in 1000 Genomes and gnomAD during WES analysis, but the specific numeric allele frequency for p.Arg925Ser was not captured in the retrieved text excerpt. (buonfiglio2024insilicoand pages 2-4)

### 4.3 Functional consequence (current understanding)
Evidence supports that MYO6 variants can lead to loss of normal hair-cell structural/synaptic function.
- In vitro: multiple patient-derived MYO6 variants caused severely shortened espin1-induced microvilli in an epithelial cell model, consistent with stereocilia structural pathology. (oka2020clinicalcharacteristicsand pages 1-3)
- In vivo: MYO6 loss-of-function is associated with profound hearing loss and stereocilia fusion/bifurcation in animal models (review synthesis). (miyoshi2024pathophysiologyofhuman pages 5-6)

### 4.4 Modifier genes, epigenetics, chromosomal abnormalities
No MYO6-specific modifier genes, epigenetic mechanisms, or recurrent chromosomal abnormalities were identified in the retrieved texts.

---

## 5. Environmental information
The retrieved evidence focuses on Mendelian genetic causation. Environmental etiologies were explicitly excluded in at least one family workup (ototoxic drugs, infections, acoustic trauma). (buonfiglio2024insilicoand pages 2-4)

---

## 6. Mechanism / pathophysiology

### 6.1 Key mechanistic concepts (current understanding)
- **Stereocilia biology:** Stereocilia are actin-rich mechanosensors required for hearing. Unconventional myosins (including MYO6) are essential for developing and maintaining stereocilia. (miyoshi2024pathophysiologyofhuman pages 1-2)
- **MYO6 functional roles (review synthesis):** MYO6 “tethers plasma membrane to the F-actin core, keeps stereocilia in place and mediates vesicle transport including endocytosis.” (miyoshi2024pathophysiologyofhuman pages 5-6)

### 6.2 Causal chain (example synthesis)
1) **Pathogenic MYO6 variant** → 2) altered myosin VI motor/structural function and/or altered dosage → 3) impaired stereocilia anchoring/maintenance and/or vesicle trafficking; plus downstream inner hair cell synaptic dysfunction → 4) progressive loss of mechanoelectrical transduction efficiency and synaptic output → 5) progressive SNHL and worsening audiometric thresholds. This chain is supported by cellular microvilli defects and mouse synaptic physiology data. (oka2020clinicalcharacteristicsand pages 1-3, yin2023functionalanddevelopmental pages 1-2)

### 6.3 Cellular processes and pathways (GO term suggestions)
- Actin cytoskeleton organization (GO:0030036) (supported conceptually by stereocilia actin core dependence) (miyoshi2024pathophysiologyofhuman pages 1-2)
- Endocytosis (GO:0006897) (MYO6 mediates vesicle transport including endocytosis) (miyoshi2024pathophysiologyofhuman pages 5-6)
- Synaptic vesicle exocytosis (GO:0016079) / regulated exocytosis (GO:0045055) (reduced exocytosis in Myo6 knockout IHCs) (yin2023functionalanddevelopmental pages 1-2)

### 6.4 Cell types (CL suggestions)
- Cochlear inner hair cell: **CL:0000601** (IHC physiology studies) (yin2023functionalanddevelopmental pages 1-2)
- Cochlear outer hair cell: **CL:0000602** (MYO6 is expressed in inner and outer hair cells per review) (alde2023autosomaldominantnonsyndromic pages 10-11)

### 6.5 Anatomical structures (UBERON suggestions)
- Cochlea: **UBERON:0001768** (general locus of pathology in studies) (yin2023functionalanddevelopmental pages 1-2)
- Organ of Corti: **UBERON:0002470** (MYO6 expression/role in hair cells of organ of Corti) (alde2023autosomaldominantnonsyndromic pages 10-11)
- Stereocilium: **UBERON:0002302** (core affected structure) (miyoshi2024pathophysiologyofhuman pages 1-2)

### 6.6 Recent developments (2023–2024)
- **2023 mouse synapse physiology:** Myo6 knockout and deafness-inducing point mutation altered IHC ribbon synapse exocytosis kinetics and vesicle pool properties, providing downstream synaptic mechanism detail. (yin2023functionalanddevelopmental pages 1-2)
- **2024 mechanistic review:** comprehensive synthesis of myosin-linked hearing loss, emphasizing stereocilia trafficking uncertainties and variant–phenotype correlations. (miyoshi2024pathophysiologyofhuman pages 1-2)
- **2024 functional validation of novel human variant:** zebrafish knockdown/rescue assays and structural modeling supported pathogenicity of p.Arg925Ser in MYO6. (buonfiglio2024insilicoand pages 2-4)

---

## 7. Anatomical structures affected

### 7.1 Primary organ/system
- **Auditory system**, specifically the **inner ear cochlea** and **hair-cell stereocilia**. (miyoshi2024pathophysiologyofhuman pages 1-2, yin2023functionalanddevelopmental pages 1-2)

### 7.2 Tissue/cellular/subcellular localization
- MYO6 is reported localized to basal regions of stereocilia and cuticular plate regions in hair cells; disruption leads to stereocilia abnormalities. (xue2022geneeditingin pages 1-2, kim2018aclinicalguidance pages 1-5)

---

## 8. Temporal development

### 8.1 Onset
- Postlingual childhood onset is common in DFNA22 families, but onset can be variable including adult-onset. (kim2018aclinicalguidance pages 5-8, melchionda2001myo6thehuman pages 1-3)

### 8.2 Progression
- Progressive course is typical, with some cohorts noting acceleration after age 40. (oka2020clinicalcharacteristicsand pages 1-3)

---

## 9. Inheritance and population

### 9.1 Inheritance
- **DFNA22:** autosomal dominant MYO6-related NSHL (kim2018aclinicalguidance pages 1-5, melchionda2001myo6thehuman pages 1-3)
- **DFNB37:** autosomal recessive MYO6-related NSHL (kim2018aclinicalguidance pages 1-5, hilgert2008asplicesitemutation pages 1-2)

### 9.2 Epidemiology / contribution to hereditary hearing loss (statistics)
- **2.40% of Japanese ADSNHL** in one large cohort was attributed to MYO6 variants (32/1336 ADSNHL families). (oka2020clinicalcharacteristicsand pages 1-3)
- **6.2% DFNA22 frequency** in one Korean autosomal-dominant NSHL cohort (5/81 families) and 6.7% in combined Korean cohorts (9/134). (kim2018aclinicalguidance pages 5-8)

**Population prevalence/incidence for MYO6 hearing loss as a standalone entity** was not identified in the retrieved texts; most literature reports are family-based or cohort contribution estimates.

---

## 10. Diagnostics

### 10.1 Clinical tests
Common audiology evaluations described include:
- Pure-tone audiometry and PTA (0.5, 1, 2, 4 kHz) (buonfiglio2024insilicoand pages 2-4)
- Auditory brainstem response (ABR), tympanometry, and speech audiometry in family studies (buonfiglio2024insilicoand pages 2-4)

### 10.2 Genetic testing
- Targeted gene panels, massively parallel sequencing, and WES are used to identify MYO6 variants, followed by Sanger segregation confirmation and ACMG/AMP classification. (oka2020clinicalcharacteristicsand pages 3-5, buonfiglio2024insilicoand pages 2-4, ji2024novelciscompound pages 1-2)
- Buonfiglio et al. explicitly reference ClinGen hearing-loss gene-specific criteria (HL-EP) in variant interpretation. (buonfiglio2024insilicoand pages 2-4)

### 10.3 Differential diagnosis
Not explicitly detailed in retrieved texts; in practice, differential includes other genetic SNHL etiologies and non-genetic causes. Environmental causes were excluded in at least one family evaluation. (buonfiglio2024insilicoand pages 2-4)

---

## 11. Outcome / prognosis

### 11.1 Hearing trajectory
- Longitudinal progression can be substantial: the foundational DFNA22 family demonstrated profound deafness by ~50 years. (melchionda2001myo6thehuman pages 1-3)
- Cohort-estimated progression rates: 0.57 dB/year overall and 1.07 dB/year after age 40 in a Japanese series. (oka2020clinicalcharacteristicsand pages 1-3)
- Many DFNA22 cases may remain moderate with preserved speech scores in certain cohorts, supporting prolonged benefit from amplification. (kim2018aclinicalguidance pages 5-8)

### 11.2 Mortality
No disease-specific mortality signal reported for non-syndromic MYO6 hearing loss in retrieved texts.

---

## 12. Treatment

### 12.1 Current clinical management (real-world implementation)
- **Hearing aids** are commonly used in affected individuals in reported families; a 2024 Argentine family report notes multiple relatives equipped with hearing aids. (buonfiglio2024insilicoand media e17c45f9)
- **Cochlear implantation (CI):** considered in select DFNA22 cases; the Argentine family figure notes one CI recipient, and a DFNA review notes favorable outcomes in DFNA22 patients in literature. (buonfiglio2024insilicoand media e17c45f9, alde2023autosomaldominantnonsyndromic pages 10-11)

**MAXO term suggestions (illustrative):**
- Hearing aid therapy (MAXO term not retrieved in texts; suggested for ontology mapping)
- Cochlear implantation (MAXO term not retrieved in texts; suggested for ontology mapping)

### 12.2 Emerging / experimental therapeutics
- **Preclinical allele-selective gene editing:** AAV-PHP.eB–mediated delivery of SaCas9/sgRNA to target the mutant Myo6C442Y allele showed allele-biased editing and rescued multiple auditory outcomes up to 5 months in a semi-dominant mouse model, supporting genome editing as a candidate strategy for semi-dominant MYO6 deafness. (xue2022geneeditingin pages 1-2)

### 12.3 Clinical trials
No MYO6 hearing-loss interventional clinical trials were identified in the retrieved clinical trial set. The retrieved NCT record pertains to a breast-cancer observational study involving nuclear myosin VI and is not applicable to MYO6 hearing loss.

---

## 13. Prevention
No MYO6-specific primary prevention interventions are established in the retrieved literature. Secondary prevention includes early genetic diagnosis and audiologic monitoring, consistent with progressive courses and possible acceleration after midlife. (oka2020clinicalcharacteristicsand pages 1-3)

---

## 14. Other species / natural disease
- Mouse models (e.g., Snell’s waltzer; Myo6 knockout; Myo6 point mutation models) demonstrate deafness/vestibular phenotypes and provide mechanistic support for MYO6 function in hair cells. (yin2023functionalanddevelopmental pages 1-2, melchionda2001myo6thehuman pages 1-3)
- Zebrafish assays (myo6b knockdown/rescue) were used to assess functional impact of a novel human MYO6 variant. (buonfiglio2024insilicoand pages 2-4)

---

## 15. Model organisms

### 15.1 Mouse models
- **Myo6−/−** knockout mice used to study IHC ribbon synapse physiology (reduced exocytosis). (yin2023functionalanddevelopmental pages 1-2)
- **Myo6C442Y** point mutation models (including semi-dominant models) used for mechanistic and gene-editing rescue studies. (yin2023functionalanddevelopmental pages 1-2, xue2022geneeditingin pages 1-2)

### 15.2 Zebrafish
- **myo6b** is expressed in lateral line hair cells; morpholino knockdown with rescue by wild-type vs mutant human MYO6 RNA provides an in vivo functional assay for variant interpretation. (buonfiglio2024insilicoand pages 2-4)

---

## Visual evidence (figure/table)
- Pedigree and audiograms for a MYO6 p.Arg925Ser family and ACMG/HL-EP evidence table for variant classification are available from Buonfiglio et al. 2024 (Figure 1; Table 1). (buonfiglio2024insilicoand media e17c45f9, buonfiglio2024insilicoand media 24cec060)

---

## Expert opinion / authoritative synthesis (2024)
A 2024 NIH-authored review emphasizes that while stereocilia biology and the roles of unconventional myosins (including MYO6) are well-established, “less is known about how myosins traffic in a stereocilium using their motor function, and how each variant correlates with a clinical condition,” highlighting ongoing uncertainty in variant-to-phenotype prediction and the need for functional assays and longitudinal clinical data. (miyoshi2024pathophysiologyofhuman pages 1-2)

---

## URLs and publication dates (as available in retrieved sources)
- Miyoshi et al., *Frontiers in Physiology* — Published 18 Mar 2024 — https://doi.org/10.3389/fphys.2024.1374901 (miyoshi2024pathophysiologyofhuman pages 1-2)
- Buonfiglio et al., *NAR Genomics and Bioinformatics* — Advance access date noted as 11 Dec 2024 — https://doi.org/10.1093/nargab/lqae162 (buonfiglio2024insilicoand pages 1-2)
- Ji et al., *Frontiers in Genetics* — Published 11 Jan 2024 — https://doi.org/10.3389/fgene.2023.1275633 (ji2024novelciscompound pages 1-2)
- Yin et al., *Cell Death Discovery* — 2023 — https://doi.org/10.1038/s41420-023-01473-3 (yin2023functionalanddevelopmental pages 1-2)
- Aldè et al., *Biomedicines* — Jun 2023 — https://doi.org/10.3390/biomedicines11061616 (alde2023autosomaldominantnonsyndromic pages 10-11)
- Oka et al., *Genes* — Mar 2020 — https://doi.org/10.3390/genes11030273 (oka2020clinicalcharacteristicsand pages 1-3)
- Kim et al., *Journal of Gene Medicine* — Apr 2018 — https://doi.org/10.1002/jgm.3019 (kim2018aclinicalguidance pages 1-5)
- Melchionda et al., *American Journal of Human Genetics* — 2001 (electronically published Jul 20, 2001 noted) — https://doi.org/10.1086/323156 (melchionda2001myo6thehuman pages 1-3)
- Xue et al., *Molecular Therapy* — 2022 (article in press text shows 2021 DOI acceptance; published in journal volume later) — https://doi.org/10.1016/j.ymthe.2021.06.015 (xue2022geneeditingin pages 1-2)

---

## Limitations / gaps for knowledge-base completion
1) **Disease-level identifiers** (MONDO, Orphanet, ICD-10/11, MeSH) were not present in the retrieved full texts and require direct database lookup.
2) **Variant allele frequencies** (exact gnomAD values) and **ClinVar/ClinGen assertions** were not fully extractable from the accessed excerpts; Buonfiglio 2024 provides methodology and classification framework but not all numerical frequencies in the excerpted text.
3) **Population prevalence/incidence** for MYO6 hearing loss as a distinct entity remains sparsely reported in the retrieved materials; available statistics are mainly cohort contribution rates.


References

1. (oka2020clinicalcharacteristicsand pages 1-3): Shin-ichiro Oka, Timothy F. Day, Shin-ya Nishio, Hideaki Moteki, Maiko Miyagawa, Shinya Morita, Shuji Izumi, Tetsuo Ikezono, Satoko Abe, Jun Nakayama, Misako Hyogo, Nobuhiko Okamoto, Natsumi Uehara, Chie Oshikawa, Shin-ichiro Kitajiri, and Shin-ichi Usami. Clinical characteristics and in vitro analysis of myo6 variants causing late-onset progressive hearing loss. Genes, 11:273, Mar 2020. URL: https://doi.org/10.3390/genes11030273, doi:10.3390/genes11030273. This article has 29 citations.

2. (kim2018aclinicalguidance pages 5-8): Bong Jik Kim, Jin Hee Han, Hye‐Rim Park, Min Young Kim, Ah Reum Kim, Seung‐Ha Oh, Woong‐Yang Park, Doo Yi Oh, Seungmin Lee, and Byung Yoon Choi. A clinical guidance to dfna22 drawn from a korean cohort study with an autosomal dominant deaf population: a retrospective cohort study. The Journal of Gene Medicine, Apr 2018. URL: https://doi.org/10.1002/jgm.3019, doi:10.1002/jgm.3019. This article has 10 citations.

3. (miyoshi2024pathophysiologyofhuman pages 1-2): Takushi Miyoshi, Inna A. Belyantseva, Mrudhula Sajeevadathan, and Thomas B. Friedman. Pathophysiology of human hearing loss associated with variants in myosins. Frontiers in Physiology, Mar 2024. URL: https://doi.org/10.3389/fphys.2024.1374901, doi:10.3389/fphys.2024.1374901. This article has 18 citations.

4. (yin2023functionalanddevelopmental pages 1-2): Ning Yin, Jingjing Zhao, Panpan Zhang, Baofu Yu, Renjie Chai, and Geng-Lin Li. Functional and developmental changes in the inner hair cell ribbon synapses caused by myosin vi knockout and deafness-inducing point mutation. Cell Death Discovery, May 2023. URL: https://doi.org/10.1038/s41420-023-01473-3, doi:10.1038/s41420-023-01473-3. This article has 5 citations and is from a peer-reviewed journal.

5. (buonfiglio2024insilicoand pages 2-4): Paula I Buonfiglio, Carlos D Bruque, Lucía Salatino, Vanesa Lotersztein, Mariela Pace, Sofia Grinberg, Ana B Elgoyhen, Paola V Plazas, and Viviana Dalamón. In silico and in vivo analyses of a novel variant in myo6 identified in a family with postlingual non-syndromic hearing loss from argentina. NAR Genomics and Bioinformatics, Sep 2024. URL: https://doi.org/10.1093/nargab/lqae162, doi:10.1093/nargab/lqae162. This article has 0 citations and is from a peer-reviewed journal.

6. (xue2022geneeditingin pages 1-2): Yuanyuan Xue, Xinde Hu, Daqi Wang, Di Li, Yige Li, Fang Wang, Mingqian Huang, Xi Gu, Zhijiao Xu, Jinan Zhou, Jinghan Wang, Renjie Chai, Jun Shen, Zheng-Yi Chen, Geng-Lin Li, Hui Yang, Huawei Li, Erwei Zuo, and Yilai Shu. Gene editing in a myo6 semi-dominant mouse model rescues auditory function. Molecular Therapy, 30:105-118, Jan 2022. URL: https://doi.org/10.1016/j.ymthe.2021.06.015, doi:10.1016/j.ymthe.2021.06.015. This article has 65 citations and is from a highest quality peer-reviewed journal.

7. (oka2020clinicalcharacteristicsand pages 3-5): Shin-ichiro Oka, Timothy F. Day, Shin-ya Nishio, Hideaki Moteki, Maiko Miyagawa, Shinya Morita, Shuji Izumi, Tetsuo Ikezono, Satoko Abe, Jun Nakayama, Misako Hyogo, Nobuhiko Okamoto, Natsumi Uehara, Chie Oshikawa, Shin-ichiro Kitajiri, and Shin-ichi Usami. Clinical characteristics and in vitro analysis of myo6 variants causing late-onset progressive hearing loss. Genes, 11:273, Mar 2020. URL: https://doi.org/10.3390/genes11030273, doi:10.3390/genes11030273. This article has 29 citations.

8. (kim2018aclinicalguidance pages 1-5): Bong Jik Kim, Jin Hee Han, Hye‐Rim Park, Min Young Kim, Ah Reum Kim, Seung‐Ha Oh, Woong‐Yang Park, Doo Yi Oh, Seungmin Lee, and Byung Yoon Choi. A clinical guidance to dfna22 drawn from a korean cohort study with an autosomal dominant deaf population: a retrospective cohort study. The Journal of Gene Medicine, Apr 2018. URL: https://doi.org/10.1002/jgm.3019, doi:10.1002/jgm.3019. This article has 10 citations.

9. (melchionda2001myo6thehuman pages 1-3): Salvatore Melchionda, Nadav Ahituv, Luigi Bisceglia, Tama Sobe, Fabian Glaser, Raquel Rabionet, Maria Lourdes Arbones, Angelo Notarangelo, Enzo Di Iorio, Massimo Carella, Leopoldo Zelante, Xavier Estivill, Karen B. Avraham, and Paolo Gasparini. Myo6, the human homologue of the gene responsible for deafness in snell's waltzer mice, is mutated in autosomal dominant nonsyndromic hearing loss. American journal of human genetics, 69 3:635-40, Sep 2001. URL: https://doi.org/10.1086/323156, doi:10.1086/323156. This article has 294 citations and is from a highest quality peer-reviewed journal.

10. (ji2024novelciscompound pages 1-2): Haiting Ji, Lichun Zhang, Hafiz Muhammad Jafar Hussain, Ayesha Aftab, Huiqian Yu, and Min Xiao. Novel cis compound heterozygous variants in myo6 causes early onset of non-syndromic hearing loss in a chinese family. Frontiers in Genetics, Jan 2024. URL: https://doi.org/10.3389/fgene.2023.1275633, doi:10.3389/fgene.2023.1275633. This article has 1 citations and is from a peer-reviewed journal.

11. (ji2024novelciscompound pages 2-3): Haiting Ji, Lichun Zhang, Hafiz Muhammad Jafar Hussain, Ayesha Aftab, Huiqian Yu, and Min Xiao. Novel cis compound heterozygous variants in myo6 causes early onset of non-syndromic hearing loss in a chinese family. Frontiers in Genetics, Jan 2024. URL: https://doi.org/10.3389/fgene.2023.1275633, doi:10.3389/fgene.2023.1275633. This article has 1 citations and is from a peer-reviewed journal.

12. (buonfiglio2024insilicoand pages 1-2): Paula I Buonfiglio, Carlos D Bruque, Lucía Salatino, Vanesa Lotersztein, Mariela Pace, Sofia Grinberg, Ana B Elgoyhen, Paola V Plazas, and Viviana Dalamón. In silico and in vivo analyses of a novel variant in myo6 identified in a family with postlingual non-syndromic hearing loss from argentina. NAR Genomics and Bioinformatics, Sep 2024. URL: https://doi.org/10.1093/nargab/lqae162, doi:10.1093/nargab/lqae162. This article has 0 citations and is from a peer-reviewed journal.

13. (buonfiglio2024insilicoand media e17c45f9): Paula I Buonfiglio, Carlos D Bruque, Lucía Salatino, Vanesa Lotersztein, Mariela Pace, Sofia Grinberg, Ana B Elgoyhen, Paola V Plazas, and Viviana Dalamón. In silico and in vivo analyses of a novel variant in myo6 identified in a family with postlingual non-syndromic hearing loss from argentina. NAR Genomics and Bioinformatics, Sep 2024. URL: https://doi.org/10.1093/nargab/lqae162, doi:10.1093/nargab/lqae162. This article has 0 citations and is from a peer-reviewed journal.

14. (buonfiglio2024insilicoand media 24cec060): Paula I Buonfiglio, Carlos D Bruque, Lucía Salatino, Vanesa Lotersztein, Mariela Pace, Sofia Grinberg, Ana B Elgoyhen, Paola V Plazas, and Viviana Dalamón. In silico and in vivo analyses of a novel variant in myo6 identified in a family with postlingual non-syndromic hearing loss from argentina. NAR Genomics and Bioinformatics, Sep 2024. URL: https://doi.org/10.1093/nargab/lqae162, doi:10.1093/nargab/lqae162. This article has 0 citations and is from a peer-reviewed journal.

15. (hilgert2008asplicesitemutation pages 1-2): Nele Hilgert, Vedat Topsakal, Joost van Dinther, Erwin Offeciers, Paul Van de Heyning, and Guy Van Camp. A splice-site mutation and overexpression of myo6 cause a similar phenotype in two families with autosomal dominant hearing loss. European Journal of Human Genetics, 16:593-602, Jan 2008. URL: https://doi.org/10.1038/sj.ejhg.5202000, doi:10.1038/sj.ejhg.5202000. This article has 49 citations and is from a domain leading peer-reviewed journal.

16. (oka2020clinicalcharacteristicsand pages 12-13): Shin-ichiro Oka, Timothy F. Day, Shin-ya Nishio, Hideaki Moteki, Maiko Miyagawa, Shinya Morita, Shuji Izumi, Tetsuo Ikezono, Satoko Abe, Jun Nakayama, Misako Hyogo, Nobuhiko Okamoto, Natsumi Uehara, Chie Oshikawa, Shin-ichiro Kitajiri, and Shin-ichi Usami. Clinical characteristics and in vitro analysis of myo6 variants causing late-onset progressive hearing loss. Genes, 11:273, Mar 2020. URL: https://doi.org/10.3390/genes11030273, doi:10.3390/genes11030273. This article has 29 citations.

17. (miyoshi2024pathophysiologyofhuman pages 5-6): Takushi Miyoshi, Inna A. Belyantseva, Mrudhula Sajeevadathan, and Thomas B. Friedman. Pathophysiology of human hearing loss associated with variants in myosins. Frontiers in Physiology, Mar 2024. URL: https://doi.org/10.3389/fphys.2024.1374901, doi:10.3389/fphys.2024.1374901. This article has 18 citations.

18. (alde2023autosomaldominantnonsyndromic pages 10-11): Mirko Aldè, Giovanna Cantarella, Diego Zanetti, Lorenzo Pignataro, Ignazio La Mantia, Luigi Maiolino, Salvatore Ferlito, Paola Di Mauro, Salvatore Cocuzza, Jérôme René Lechien, Giannicola Iannella, Francois Simon, and Antonino Maniaci. Autosomal dominant non-syndromic hearing loss (dfna): a comprehensive narrative review. Biomedicines, 11:1616, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061616, doi:10.3390/biomedicines11061616. This article has 57 citations.