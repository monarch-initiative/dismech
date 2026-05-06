---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T18:25:24.078039'
end_time: '2026-05-06T18:39:57.063645'
duration_seconds: 872.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hantavirus Pulmonary Syndrome
  mondo_id: ''
  category: Infectious
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
- **Disease Name:** Hantavirus Pulmonary Syndrome
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Hantavirus Pulmonary Syndrome** covering all of the
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
- **Disease Name:** Hantavirus Pulmonary Syndrome
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Hantavirus Pulmonary Syndrome** covering all of the
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


## Comprehensive research report: Hantavirus Pulmonary Syndrome (HPS) / Hantavirus Cardiopulmonary Syndrome (HCPS)

### Target disease
- **Disease name:** Hantavirus Pulmonary Syndrome (HPS), also called **Hantavirus Cardiopulmonary Syndrome (HCPS)** (chen2023zoonotichantaviridaewith pages 1-2)
- **Category:** Infectious (zoonotic viral disease)
- **MONDO ID:** Not retrievable from the provided full texts in this run (evidence gap).

---

## 1. Disease information (overview, identifiers, synonyms)

### Concise overview
HPS/HCPS is a severe acute zoonotic disease caused by New World orthohantaviruses. A 2023 review of Sin Nombre virus (SNV) describes HPS as **“a life-threatening illness named for the predominance of infection of pulmonary endothelial cells.”** (publication date: Nov 2023; URL: https://doi.org/10.3390/biology12111413) (jacob2023sinnombrevirus pages 1-2).

### Key identifiers (available from retrieved sources)
- **MeSH IDs (from ClinicalTrials.gov record):**
  - MeSH **D018804**: “Hantavirus Pulmonary Syndrome”
  - MeSH **D018778**: “Hantavirus Infections” (NCT00128180 chunk 2)

**ICD-10 / ICD-11 / Orphanet / MONDO identifiers:** Not present in the retrieved full texts and therefore cannot be cited here (evidence gap).

### Common synonyms and alternative names
- Hantavirus pulmonary syndrome (HPS)
- Hantavirus cardiopulmonary syndrome (HCPS) (chen2023zoonotichantaviridaewith pages 1-2)

### Evidence source type
Information here is derived from **aggregated disease-level resources** (reviews, surveillance/tooling papers, and a clinical trial registry entry), not individual EHR-only datasets (jacob2023sinnombrevirus pages 1-2, cintron2023hantanetanew pages 1-2, NCT00128180 chunk 2).

---

## 2. Etiology

### Disease causal factors
- **Infectious cause:** New World orthohantaviruses; commonly cited etiologic agents include **Sin Nombre virus (SNV)** in North America and **Andes virus (ANDV)** in South America (jacob2023sinnombrevirus pages 1-2, chen2023zoonotichantaviridaewith pages 1-2).

### Risk factors (exposure-related)
- **Primary transmission route:** exposure to **aerosolized rodent excreta/secreta** (urine/feces/saliva), described in the SNV review (2023; https://doi.org/10.3390/biology12111413) (jacob2023sinnombrevirus pages 1-2).
- **Reservoir:** the SNV review identifies the primary reservoir as the **deer mouse (*Peromyscus maniculatus*)** (jacob2023sinnombrevirus pages 1-2).
- **Human-to-human transmission:** limited evidence is noted mainly for **ANDV** (cintron2023hantanetanew pages 1-2, tortosa2024seroprevalenceofhantavirus pages 1-2).

### Protective factors
Not identified in the retrieved evidence (gap).

### Gene–environment interaction
Host genetic susceptibility/protective loci were not identified in the retrieved evidence (gap).

---

## 3. Phenotypes, temporal course, and anatomy affected

### Core clinical course (current understanding)
HPS/HCPS typically progresses from a prodrome to rapid cardiopulmonary decompensation:
- **Prodrome:** fever and myalgias, often with gastrointestinal symptoms (simpson2010hantaviruspulmonarysyndrome. pages 7-10).
- **Dyspnea is often late**; once dyspnea occurs, rapid deterioration is common: **“Patients presenting with dyspnea typically require intubation and mechanical ventilation within 1 to 6 hours.”** (Simpson et al., 2010; URL: https://doi.org/10.1016/j.idc.2009.10.011; publication date: Mar 2010) (simpson2010hantaviruspulmonarysyndrome. pages 7-10).
- **Hemodynamic pattern:** shock physiology includes **myocardial depression** and relative intravascular volume depletion; volume repletion may not improve cardiac output (simpson2010hantaviruspulmonarysyndrome. pages 7-10).

### Key phenotypes (suggested HPO terms)
Below are phenotype elements repeatedly described in clinical summaries of HPS/HCPS:
- **Fever** (HPO: HP:0001945) (simpson2010hantaviruspulmonarysyndrome. pages 7-10)
- **Myalgia** (HP:0003326) (simpson2010hantaviruspulmonarysyndrome. pages 7-10)
- **Headache** (HP:0002315) (llah2018hantavirusinducedcardiopulmonary pages 1-2)
- **Nausea / vomiting / diarrhea** (HP:0002018 / HP:0002013 / HP:0002014) (simpson2010hantaviruspulmonarysyndrome. pages 7-10)
- **Dyspnea** (HP:0002094) (simpson2010hantaviruspulmonarysyndrome. pages 7-10)
- **Acute respiratory distress / noncardiogenic pulmonary edema** (HP:0002106, HP:0002091) (simpson2010hantaviruspulmonarysyndrome. pages 7-10)
- **Shock / hypotension** (HP:0001251 / HP:0002615) (simpson2010hantaviruspulmonarysyndrome. pages 7-10)
- **Thrombocytopenia** (HP:0001873) — reported in **79% at presentation** in one review (simpson2010hantaviruspulmonarysyndrome. pages 7-10)
- **Hemoconcentration / elevated hematocrit** (HP:0001899) — hematocrits up to **77%** reported (simpson2010hantaviruspulmonarysyndrome. pages 7-10)
- **Leukocytosis** (HP:0001974) (simpson2010hantaviruspulmonarysyndrome. pages 7-10)

### Laboratory abnormalities and suggested mappings
- **Thrombocytopenia** (HP:0001873) (simpson2010hantaviruspulmonarysyndrome. pages 7-10)
- **Leukocytosis with left shift** (HP:0001974) (simpson2010hantaviruspulmonarysyndrome. pages 7-10)
- **Hemoconcentration** (HP:0001899) (simpson2010hantaviruspulmonarysyndrome. pages 7-10)

### Anatomical structures and cell types affected
- **Primary organ/system:** lung (respiratory system), with pulmonary edema/alveolar flooding and pleural effusions described in clinical-pathology summaries (simpson2010hantaviruspulmonarysyndrome. pages 7-10).
  - Suggested UBERON terms: **lung** (UBERON:0002048), **pulmonary alveolus** (UBERON:0002299).
- **Key cellular target:** **endothelial cells** (CL:0000115), emphasized across reviews and mechanistic papers as a principal tropism (jacob2023sinnombrevirus pages 1-2, llah2018hantavirusinducedcardiopulmonary pages 1-2).
- **Cardiovascular involvement:** myocardial depression/cardiogenic shock is commonly described as a major contributor to death (simpson2010hantaviruspulmonarysyndrome. pages 7-10).

### Quality-of-life impact
Not quantified in the retrieved evidence for 2023–2024 HPS/HCPS survivor cohorts; a long-term QOL cohort exists in the retrieved library (2025) but was not captured with extractable evidence snippets in this run (gap).

---

## 4. Genetic/molecular information

### Causal genes and pathogenic variants
HPS/HCPS is not a monogenic disorder; no causal human germline variants were identified in the retrieved evidence (gap).

### Pathogen genome/proteins (molecular identifiers)
Hantaviruses are **negative-sense, tri-segmented RNA viruses** with S/M/L genome segments encoding nucleoprotein, glycoproteins, and RNA polymerase (cintron2023hantanetanew pages 1-2, llah2018hantavirusinducedcardiopulmonary pages 1-2).

---

## 5. Environmental information

### Environmental/lifestyle contributors
The dominant environmental determinant is **rodent exposure**, particularly aerosolized exposures in contaminated settings (jacob2023sinnombrevirus pages 1-2).

---

## 6. Mechanism / pathophysiology (causal chain, pathways, immune processes)

### Causal chain (current synthesis)
1. **Exposure and entry:** inhalation of aerosolized rodent excreta containing infectious virus (jacob2023sinnombrevirus pages 1-2).
2. **Primary infection of endothelial cells:** endothelial tropism is a recurring core concept in HPS/HCPS, including the SNV review emphasis on pulmonary endothelial infection (jacob2023sinnombrevirus pages 1-2, llah2018hantavirusinducedcardiopulmonary pages 1-2).
3. **Barrier dysfunction and vascular leak:** clinical disease is characterized by pulmonary capillary leak and edema (llah2018hantavirusinducedcardiopulmonary pages 1-2, llah2018hantavirusinducedcardiopulmonary pages 2-3).
4. **Cardiopulmonary failure:** patients develop severe hypoxemia, shock, and myocardial depression (simpson2010hantaviruspulmonarysyndrome. pages 7-10).

### Viral entry factors and upstream host determinants
- Pathogenic orthohantaviruses preferentially use **β3 integrin** for entry; mechanistic review content also implicates linkage to **VEGFR2** signaling complexes (taylor2025pathogenicityandvirulence pages 10-12, llah2018hantavirusinducedcardiopulmonary pages 1-2).
- **Protocadherin-1** is also implicated in entry (jeyachandran2025differentialtropismsof pages 27-28).

### Key downstream permeability pathways
- **VEGF/VEGFR2 – VE-cadherin axis:** a mechanistic framework links pathogenic hantaviruses to sensitization of endothelium to permeability signaling and **VE-cadherin** disruption (taylor2025pathogenicityandvirulence pages 10-12, llah2018hantavirusinducedcardiopulmonary pages 2-3).
- **Kallikrein–kinin / bradykinin signaling:** implicated in increased vascular permeability and highlighted as a candidate therapeutic axis (taylor2025pathogenicityandvirulence pages 10-12).

### Immune mechanisms and inflammation
- **Hypercytokinemia:** multiple cytokines/chemokines are reported elevated in pathogenic orthantohantavirus disease, including IL-6 and CXCL10 among others (taylor2025pathogenicityandvirulence pages 10-12).
- **Type I interferon–linked innate lymphoid activation (2024):** In a 2024 PLOS Pathogens study (publication date: Jul 2024; https://doi.org/10.1371/journal.ppat.1012390), hantavirus infection was associated with strong inflammation and altered innate lymphoid cells; **ILC2 frequency increased**, and in vitro activation was **type I interferon–dependent** (garcia2024innatelymphoidcells pages 1-2). While this cohort was PUUV-HFRS, the authors frame these responses in the broader context of hantaviruses causing HFRS and HPS (garcia2024innatelymphoidcells pages 1-2).
- **IL-6 trans-signaling and endothelial barrier dysfunction (2025 mechanistic extension):** IL-6 trans-signaling in infected endothelial cells increased cytokine secretion and disrupted barrier integrity via VE-cadherin changes, supporting a plausible mechanism for vascular leak (maleki2025il6transsignalingmediates pages 1-2).

### Suggested ontology terms for mechanisms
- **GO biological process:**
  - regulation of endothelial cell barrier (e.g., “regulation of endothelial cell permeability”)
  - inflammatory response
  - cytokine-mediated signaling pathway
  - regulation of vasculature development / VEGF signaling
- **Cell types (CL):**
  - endothelial cell (CL:0000115)
  - innate lymphoid cell (general class) / ILC2 (as used in the 2024 study) (garcia2024innatelymphoidcells pages 1-2)

### Recent developments: omics and advanced models
A 2025 PLOS Pathogens study used **human primary lung endothelial cells**, multiple iPSC-derived cell types, and **human 3D distal lung organoids**, reporting differential tropism (ANDV broad, SNV more restricted to pulmonary endothelium) and **transcriptomic programs of injury/inflammation and suppressed lipid metabolism** in infected lung epithelial cells; the study reports deposition at **NCBI GEO GSE232641** (publication date: Aug 2025; URL: https://doi.org/10.1371/journal.ppat.1013401) (jeyachandran2025differentialtropismsof pages 1-2).

---

## 7. Anatomical structures affected (structured)

- **Primary:** lung (UBERON:0002048), pulmonary microvascular endothelium (CL:0000115) (jacob2023sinnombrevirus pages 1-2, llah2018hantavirusinducedcardiopulmonary pages 1-2)
- **Secondary/complication-prone:** cardiovascular system—myocardial depression and shock physiology (simpson2010hantaviruspulmonarysyndrome. pages 7-10)
- **Subcellular (suggested, not directly evidenced here):** intercellular junction complexes (VE-cadherin), consistent with barrier disruption mechanisms (maleki2025il6transsignalingmediates pages 1-2)

---

## 8. Temporal development (onset/progression)

- **Onset:** acute (prodrome then rapid progression) (simpson2010hantaviruspulmonarysyndrome. pages 7-10).
- **Progression:** rapid, with respiratory failure sometimes requiring intubation within hours after dyspnea begins (simpson2010hantaviruspulmonarysyndrome. pages 7-10).
- **Critical period:** early cardiopulmonary phase is a narrow window for escalation to intensive support (mechanical ventilation, vasopressors, ECMO) (simpson2010hantaviruspulmonarysyndrome. pages 7-10, llah2018hantavirusinducedcardiopulmonary pages 3-4).

---

## 9. Inheritance and population

### Epidemiology and geographic distribution
- HPS/HCPS is primarily a disease of the **Americas**, associated with New World hantaviruses (chen2023zoonotichantaviridaewith pages 1-2).
- Global burden context: a 2023 review summarizes that ~150,000–200,000 hantavirus cases (HFRS or HCPS/HPS combined) are reported annually and provides HCPS/HPS CFR ranges (publication date: Aug 2023; URL: https://doi.org/10.3390/v15081705) (chen2023zoonotichantaviridaewith pages 1-2).

### Relevant statistics (recent)
- **Background seroprevalence (non-epidemic settings):** 2024 systematic review/meta-analysis (publication date: Sep 2024; URL: https://doi.org/10.1186/s12889-024-20014-w) estimates global hantavirus IgG seroprevalence **2.93% (95% CI 2.34–3.67%)**, with regional estimates Americas **2.43%**, Europe **2.98%**, Asia **6.84%**, Africa **2.21%** (tortosa2024seroprevalenceofhantavirus pages 1-2).

### Mortality / prognosis statistics
- **Case fatality ranges:** reviews commonly cite **~30–50%** for HCPS/HPS, with virus-specific CFRs such as ANDV ~40% and SNV 30–50% (chen2023zoonotichantaviridaewith pages 1-2).

---

## 10. Diagnostics

### Clinical and laboratory confirmation
A 2023 surveillance/genomic epidemiology paper (HantaNet; publication date: Nov 2023; URL: https://doi.org/10.3390/v15112208) summarizes laboratory confirmation for U.S. surveillance as compatible illness plus one of:
- **hantavirus-reactive IgM**, or
- rising hantavirus-specific **IgG titers**, or
- detection of **hantavirus RNA**, or
- hantavirus-reactive **immunohistochemistry** (cintron2023hantanetanew pages 1-2).

### Differential diagnosis
Not systematically extractable from the retrieved evidence snippets in this run (gap).

---

## 11. Outcome / prognosis

- The acute course is frequently fulminant, with high mortality driven by rapid respiratory failure and shock (simpson2010hantaviruspulmonarysyndrome. pages 7-10).
- Elevated lactate has been described as a poor prognostic marker in early series, with some exceptions in ECMO-treated patients (simpson2010hantaviruspulmonarysyndrome. pages 7-10).

---

## 12. Treatment (current applications and evidence)

### Standard of care: supportive critical care
- Management is primarily **supportive**; advanced respiratory and hemodynamic support are central, and ECMO is used for refractory cardiopulmonary failure (llah2018hantavirusinducedcardiopulmonary pages 3-4).

**Suggested MAXO terms:** mechanical ventilation, extracorporeal membrane oxygenation, vasopressor therapy, intensive care (supportive care).

### Antiviral therapy: ribavirin (clinical trial evidence)
A placebo-controlled, double-blind North American trial (publication date: Nov 2004; URL: https://doi.org/10.1086/425007) found **no evidence of benefit** for IV ribavirin in confirmed HCPS cases:
- survival without ECMO: **70% ribavirin vs 62% placebo**
- **2 deaths** in each arm
- among ECMO-treated subjects, **3 of 7** died
- trial stopped early for slow accrual/futility (mertz2004placebocontrolleddoubleblindtrial pages 1-2).

**Suggested MAXO terms:** antiviral therapy; ribavirin administration.

### Corticosteroids: methylprednisolone
- A methylprednisolone RCT is registered (ClinicalTrials.gov **NCT00128180**), with inclusion/exclusion criteria for presumptive HCPS and a linked publication (PMID 23784924) (NCT00128180 chunk 2).
- A review summarizes that the methylprednisolone trial showed **no benefit** on mortality or key physiologic outcomes (llah2018hantavirusinducedcardiopulmonary pages 4-5).

**Suggested MAXO terms:** corticosteroid therapy.

### Passive immunotherapy (immune plasma)
A review describes immune plasma as promising and references a non-randomized multicenter trial reporting a “marked difference in mortality,” but the effect size and statistical details were not extractable in the provided evidence snippets (llah2018hantavirusinducedcardiopulmonary pages 4-5). This remains an evidence gap for precise quantitative synthesis in this report.

**Suggested MAXO terms:** passive immunization; convalescent plasma therapy.

### Vaccination (pipeline)
- A Phase 1 trial of an **Andes virus DNA vaccine** is listed as completed (ClinicalTrials.gov **NCT03682107**) (trial listing in tool output; not accompanied by extractable results in the evidence snippets provided in this run).

**Suggested MAXO terms:** vaccination.

---

## 13. Prevention

### Primary prevention (current implementation)
Prevention focuses on interrupting rodent-to-human transmission:
- rodent control and reducing contact with contaminated rodent excreta, with emphasis on avoiding aerosolization (jacob2023sinnombrevirus pages 1-2, iheukwumere2025hantavirusestransmissiondynamics pages 1-2).

### Public health surveillance and outbreak response (real-world implementation)
A 2023 paper describes **HantaNet**, a MicrobeTrace-powered visualization and analytics tool for **hantavirus classification and genomic surveillance**, intended to reduce reporting delays and improve outbreak detection (publication date: Nov 2023; URL: https://doi.org/10.3390/v15112208) (cintron2023hantanetanew pages 1-2).

The retrieved figure below depicts the HantaNet workflow and S/M/L segment visualization dashboard (cintron2023hantanetanew media 48129cbd).

---

## 14. Other species / natural disease

- **Reservoirs:** rodents are the main reservoirs for medically important New World hantaviruses; deer mouse is the primary SNV reservoir (jacob2023sinnombrevirus pages 1-2).
- **Zoonotic potential:** primary transmission is rodent-to-human; limited person-to-person transmission is described mainly for ANDV (cintron2023hantanetanew pages 1-2, tortosa2024seroprevalenceofhantavirus pages 1-2).

---

## 15. Model organisms and experimental models

- **Animal models:** hamster models are widely referenced in the therapeutic development literature for Andes virus disease (contextualized in reviews; not fully extractable here with quantitative model outcomes) (llah2018hantavirusinducedcardiopulmonary pages 4-5).
- **Human experimental systems (recent):** human endothelial cell infection systems and **3D distal lung organoids** support mechanistic and antiviral candidate studies, enabling transcriptomic/lipidomic profiling (jeyachandran2025differentialtropismsof pages 1-2).

---

## Expert opinion / analysis (authoritative synthesis)
Across reviews and mechanistic papers, expert consensus is that HPS/HCPS severity is driven less by overt cytolysis and more by **endothelial dysfunction with dysregulated permeability and immune activation**, implicating VEGF/VE-cadherin signaling and inflammatory cytokine networks (taylor2025pathogenicityandvirulence pages 10-12, llah2018hantavirusinducedcardiopulmonary pages 2-3). The failure of ribavirin to show benefit in established cardiopulmonary-phase disease in the 2004 RCT reinforces the clinical emphasis on **early recognition and rapid escalation of supportive critical care**, including ECMO in refractory cases (mertz2004placebocontrolleddoubleblindtrial pages 1-2, llah2018hantavirusinducedcardiopulmonary pages 3-4).

---

## Evidence gaps relative to the template
- **Formal disease identifiers:** ICD-10/ICD-11, MONDO, Orphanet not extractable from retrieved texts.
- **Host genetic susceptibility/protective factors:** not identified in retrieved evidence.
- **Quantitative prevention effectiveness (interventional studies) and immune plasma effect sizes:** not extractable from snippets; would require targeted retrieval of the cited primary trial reports.



References

1. (chen2023zoonotichantaviridaewith pages 1-2): Ji-Ming Chen, Rui-Xu Chen, Huan-Yu Gong, Xiu Wang, Ming-Hui Sun, Yu-Fei Ji, Su-Mei Tan, and Jian-Wei Shao. Zoonotic hantaviridae with global public health significance. Viruses, Aug 2023. URL: https://doi.org/10.3390/v15081705, doi:10.3390/v15081705. This article has 35 citations.

2. (jacob2023sinnombrevirus pages 1-2): Andrew T. Jacob, Benjamin M. Ziegler, Stefania M. Farha, Lyla R. Vivian, Cora A. Zilinski, Alexis R. Armstrong, Andrew J. Burdette, Dia C. Beachboard, and Christopher C. Stobart. Sin nombre virus and the emergence of other hantaviruses: a review of the biology, ecology, and disease of a zoonotic pathogen. Biology, 12:1413, Nov 2023. URL: https://doi.org/10.3390/biology12111413, doi:10.3390/biology12111413. This article has 18 citations.

3. (NCT00128180 chunk 2):  Efficacy of Methylprednisolone for Hantavirus Cardiopulmonary Syndrome. University of New Mexico. 2003. ClinicalTrials.gov Identifier: NCT00128180

4. (cintron2023hantanetanew pages 1-2): Roxana Cintron, Shannon L. M. Whitmer, Evan Moscoso, Ellsworth M. Campbell, Reagan Kelly, Emir Talundzic, Melissa Mobley, Kuo Wei Chiu, Elizabeth Shedroff, Anupama Shankar, Joel M. Montgomery, John D. Klena, and William M. Switzer. Hantanet: a new microbetrace application for hantavirus classification, genomic surveillance, epidemiology and outbreak investigations. Viruses, 15:2208, Nov 2023. URL: https://doi.org/10.3390/v15112208, doi:10.3390/v15112208. This article has 4 citations.

5. (tortosa2024seroprevalenceofhantavirus pages 1-2): Fernando Tortosa, Fernando Perre, Celia Tognetti, Lucia Lossetti, Gabriela Carrasco, German Guaresti, Ayelén Iglesias, Yesica Espasandin, and Ariel Izcovich. Seroprevalence of hantavirus infection in non-epidemic settings over four decades: a systematic review and meta-analysis. BMC Public Health, Sep 2024. URL: https://doi.org/10.1186/s12889-024-20014-w, doi:10.1186/s12889-024-20014-w. This article has 15 citations and is from a peer-reviewed journal.

6. (simpson2010hantaviruspulmonarysyndrome. pages 7-10): S. Simpson, L. Spikes, Saurin Patel, and I. Faruqi. Hantavirus pulmonary syndrome. Infectious disease clinics of North America, 24 1:159-73, Mar 2010. URL: https://doi.org/10.1016/j.idc.2009.10.011, doi:10.1016/j.idc.2009.10.011. This article has 55 citations and is from a peer-reviewed journal.

7. (llah2018hantavirusinducedcardiopulmonary pages 1-2): Sibghat T. Llah, Sheema Mir, Sumaiya Sharif, Salman Khan, and Mohammed A. Mir. Hantavirus induced cardiopulmonary syndrome: a public health concern. Journal of Medical Virology, 90:1003-1009, Jun 2018. URL: https://doi.org/10.1002/jmv.25054, doi:10.1002/jmv.25054. This article has 50 citations and is from a peer-reviewed journal.

8. (llah2018hantavirusinducedcardiopulmonary pages 2-3): Sibghat T. Llah, Sheema Mir, Sumaiya Sharif, Salman Khan, and Mohammed A. Mir. Hantavirus induced cardiopulmonary syndrome: a public health concern. Journal of Medical Virology, 90:1003-1009, Jun 2018. URL: https://doi.org/10.1002/jmv.25054, doi:10.1002/jmv.25054. This article has 50 citations and is from a peer-reviewed journal.

9. (taylor2025pathogenicityandvirulence pages 10-12): Shannon L. Taylor, Connie S. Schmaljohn, Evan P. Williams, and Colleen B. Jonsson. Pathogenicity and virulence of rodent-borne orthohantaviruses. Virulence, Sep 2025. URL: https://doi.org/10.1080/21505594.2025.2553784, doi:10.1080/21505594.2025.2553784. This article has 4 citations and is from a peer-reviewed journal.

10. (jeyachandran2025differentialtropismsof pages 27-28): Arjit Vijey Jeyachandran, Joseph Ignatius Irudayam, Swati Dubey, Nikhil Chakravarty, Maria Daskou, Anne Zaiss, Gustavo Garcia, Bindu Konda, Aayushi Shah, Aditi Venkatraman, Baolong Su, Cheng Wang, Qi Cui, Kevin J. Williams, Sonal Srikanth, Ashok Kumar, Yanhong Shi, Arjun Deb, Robert Damoiseaux, Barry R. Stripp, Arunachalam Ramaiah, and Vaithilingaraja Arumugaswami. Differential tropisms of old and new world hantaviruses influence virulence and developing host-directed antiviral candidates. PLOS Pathogens, 21:e1013401, Aug 2025. URL: https://doi.org/10.1371/journal.ppat.1013401, doi:10.1371/journal.ppat.1013401. This article has 1 citations and is from a highest quality peer-reviewed journal.

11. (garcia2024innatelymphoidcells pages 1-2): Marina García, Anna Carrasco García, Whitney Weigel, Wanda Christ, Ronaldo Lira-Junior, Lorenz Wirth, Johanna Tauriainen, Kimia Maleki, Giulia Vanoni, Antti Vaheri, Satu Mäkelä, Jukka Mustonen, Johan Nordgren, Anna Smed-Sörensen, Tomas Strandin, Jenny Mjösberg, and Jonas Klingström. Innate lymphoid cells are activated in hfrs, and their function can be modulated by hantavirus-induced type i interferons. PLOS Pathogens, 20:e1012390, Jul 2024. URL: https://doi.org/10.1371/journal.ppat.1012390, doi:10.1371/journal.ppat.1012390. This article has 7 citations and is from a highest quality peer-reviewed journal.

12. (maleki2025il6transsignalingmediates pages 1-2): Kimia T. Maleki, Linda Niemetz, Wanda Christ, Julia Wigren Byström, Therese Thunberg, Clas Ahlm, and Jonas Klingström. Il-6 trans-signaling mediates cytokine secretion and barrier dysfunction in hantavirus-infected cells and correlates to severity in hfrs. PLOS Pathogens, 21:e1013042, Apr 2025. URL: https://doi.org/10.1371/journal.ppat.1013042, doi:10.1371/journal.ppat.1013042. This article has 5 citations and is from a highest quality peer-reviewed journal.

13. (jeyachandran2025differentialtropismsof pages 1-2): Arjit Vijey Jeyachandran, Joseph Ignatius Irudayam, Swati Dubey, Nikhil Chakravarty, Maria Daskou, Anne Zaiss, Gustavo Garcia, Bindu Konda, Aayushi Shah, Aditi Venkatraman, Baolong Su, Cheng Wang, Qi Cui, Kevin J. Williams, Sonal Srikanth, Ashok Kumar, Yanhong Shi, Arjun Deb, Robert Damoiseaux, Barry R. Stripp, Arunachalam Ramaiah, and Vaithilingaraja Arumugaswami. Differential tropisms of old and new world hantaviruses influence virulence and developing host-directed antiviral candidates. PLOS Pathogens, 21:e1013401, Aug 2025. URL: https://doi.org/10.1371/journal.ppat.1013401, doi:10.1371/journal.ppat.1013401. This article has 1 citations and is from a highest quality peer-reviewed journal.

14. (llah2018hantavirusinducedcardiopulmonary pages 3-4): Sibghat T. Llah, Sheema Mir, Sumaiya Sharif, Salman Khan, and Mohammed A. Mir. Hantavirus induced cardiopulmonary syndrome: a public health concern. Journal of Medical Virology, 90:1003-1009, Jun 2018. URL: https://doi.org/10.1002/jmv.25054, doi:10.1002/jmv.25054. This article has 50 citations and is from a peer-reviewed journal.

15. (mertz2004placebocontrolleddoubleblindtrial pages 1-2): G. J. Mertz, L. Miedzinski, D. Goade, A. T. Pavia, B. Hjelle, C. O. Hansbarger, H. Levy, F. T. Koster, K. Baum, A. Lindemulder, W. Wang, L. Riser, H. Fernandez, and R. J. Whitley. Placebo-controlled, double-blind trial of intravenous ribavirin for the treatment of hantavirus cardiopulmonary syndrome in north america. Clinical infectious diseases : an official publication of the Infectious Diseases Society of America, 39 9:1307-13, Nov 2004. URL: https://doi.org/10.1086/425007, doi:10.1086/425007. This article has 234 citations.

16. (llah2018hantavirusinducedcardiopulmonary pages 4-5): Sibghat T. Llah, Sheema Mir, Sumaiya Sharif, Salman Khan, and Mohammed A. Mir. Hantavirus induced cardiopulmonary syndrome: a public health concern. Journal of Medical Virology, 90:1003-1009, Jun 2018. URL: https://doi.org/10.1002/jmv.25054, doi:10.1002/jmv.25054. This article has 50 citations and is from a peer-reviewed journal.

17. (iheukwumere2025hantavirusestransmissiondynamics pages 1-2): I. H. Iheukwumere, C. M. Iheukwumere, B. C. Unaeze, V. E Ike, H. C. Nnadozie, and S. O. Onyema. Hantaviruses, transmission dynamics, clinical outcomes, and preventive approaches: a review. IPS Journal of Basic and Clinical Medicine, 2:115-121, Oct 2025. URL: https://doi.org/10.54117/ijbcm.v2i4.21, doi:10.54117/ijbcm.v2i4.21. This article has 0 citations.

18. (cintron2023hantanetanew media 48129cbd): Roxana Cintron, Shannon L. M. Whitmer, Evan Moscoso, Ellsworth M. Campbell, Reagan Kelly, Emir Talundzic, Melissa Mobley, Kuo Wei Chiu, Elizabeth Shedroff, Anupama Shankar, Joel M. Montgomery, John D. Klena, and William M. Switzer. Hantanet: a new microbetrace application for hantavirus classification, genomic surveillance, epidemiology and outbreak investigations. Viruses, 15:2208, Nov 2023. URL: https://doi.org/10.3390/v15112208, doi:10.3390/v15112208. This article has 4 citations.