---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T15:11:05.255076'
end_time: '2026-04-05T15:24:48.895358'
duration_seconds: 823.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Myeloid Leukemia, FLT3-Mutated
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
- **Disease Name:** Acute Myeloid Leukemia, FLT3-Mutated
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Acute Myeloid Leukemia, FLT3-Mutated** covering all of the
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
- **Disease Name:** Acute Myeloid Leukemia, FLT3-Mutated
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Acute Myeloid Leukemia, FLT3-Mutated** covering all of the
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


# Comprehensive Research Report: Acute Myeloid Leukemia, FLT3-Mutated

## Target Disease
- **Disease name:** Acute Myeloid Leukemia (AML), FLT3-mutated
- **Category:** Hematologic malignancy (myeloid neoplasm)
- **MONDO ID:** Not identified for the *FLT3-mutated AML subtype* in the retrieved sources (the evidence set includes MONDO terms for AML more generally via OpenTargets, but not a specific subtype identifier extractable here).

---

## 1. Disease Information

### 1.1 Concise overview
Acute myeloid leukemia (AML) is an aggressive hematologic malignancy characterized by the accumulation of immature hematopoietic precursors (blasts) in the bone marrow and peripheral blood. (negotei2023areviewof pages 1-3)

**FLT3-mutated AML** refers to AML harboring activating mutations in **FLT3 (FMS-related receptor tyrosine kinase 3)**; these mutations occur in ~30% of newly diagnosed AML patients. (fedorov2023targetingflt3mutation pages 1-2)

**Key concept—driver alteration:** Activating FLT3 mutations are typically **somatic** lesions that confer proliferative/survival advantages to leukemic clones through constitutive signaling. (fedorov2023targetingflt3mutation pages 1-2)

### 1.2 Synonyms and alternative names
Commonly used in clinical and research contexts:
- “FLT3-mutated AML” / “FLT3+ AML” (short2023treatmentofolder pages 1-2)
- “FLT3-ITD AML” (internal tandem duplication) (fedorov2023targetingflt3mutation pages 1-2)
- “FLT3-TKD AML” (tyrosine kinase domain point mutation) (fedorov2023targetingflt3mutation pages 1-2)

### 1.3 Key identifiers (availability in retrieved evidence)
- **ICD-9/ICD-10 codes (AML overall)** were used in Global Burden of Disease (GBD) methods; these are not subtype-specific codes and are used for AML broadly. (zhou2024globalregionaland pages 2-4)
- **ELN (European LeukemiaNet) 2022 risk classification** provides risk-grouping rules relevant to FLT3-ITD (no longer using allelic ratio). (lachowiez2023comparisonandvalidation pages 1-2, fedorov2023targetingflt3mutation pages 1-2)
- **MeSH / Orphanet / OMIM / subtype-specific MONDO** identifiers for “FLT3-mutated AML” were not retrieved as explicit identifiers in the accessible text evidence.

### 1.4 Evidence source type
Most information below is derived from aggregated, disease-level resources (reviews, guidelines, and large registry/GBD studies) and from primary clinical trials (RATIFY, ADMIRAL, QuANTUM-First). (stone2017midostaurinpluschemotherapy pages 1-2, perl2019gilteritiniborchemotherapy pages 1-2, chen2024globalnationaland pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
FLT3-mutated AML is driven by activating mutations in FLT3 leading to constitutive receptor signaling (PI3K, STAT5, RAS pathways), increasing leukemic cell survival and proliferation. (fedorov2023targetingflt3mutation pages 1-2)

### 2.2 Risk factors (AML overall; population-level)
Recent GBD-based analyses identify major modifiable risk factors associated with AML burden and mortality, including:
- **Smoking**
- **High body mass index (BMI)**
- **Occupational exposure to benzene and formaldehyde** (chen2024globalnationaland pages 1-2, zhou2024globalregionaland pages 13-16)

GBD 2021 global statistics show **incident AML cases increased from 79,372 (1990) to 144,645 (2021)**, while **age-standardized incidence rate (ASIR)** changed slightly (1.77 to 1.73 per 100,000). (zhou2024globalregionaland pages 2-4)

In older adults (60–89 years), 2019 estimates report **61,559 incident cases**, **53,620 deaths**, and **990,656 DALYs**, and identify smoking, high BMI, and occupational benzene/formaldehyde as significant risk factors for mortality in 2019. (chen2024globalnationaland pages 1-2)

### 2.3 Protective factors
No specific genetic or environmental protective factors for FLT3-mutated AML were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No explicit gene–environment interaction evidence specific to FLT3-mutated AML was retrieved.

---

## 3. Phenotypes

### 3.1 Core clinical and laboratory phenotype (FLT3-ITD emphasis)
Across multiple sources, **FLT3-ITD AML** is repeatedly associated with **higher disease burden** and adverse clinical presentation:
- Higher leukocyte counts and increased blast percentage at presentation, and higher relapse likelihood. (jalte2023flt3mutationsin pages 3-4)
- Higher disease burden and inferior overall and relapse-free survival. (fedorov2023targetingflt3mutation pages 1-2)

General AML symptom cluster (not FLT3-specific but relevant to marrow failure) includes **infections, anemia, and bleeding** due to impaired normal hematopoiesis. (chen2024globalnationaland pages 1-2)

**Frequency data gap:** The retrieved sources did not provide robust population-level percentages for individual presenting symptoms (e.g., exact frequency of fever, bruising, etc.) specific to FLT3-mutated AML.

### 3.2 Suggested HPO terms (examples)
- Leukocytosis — **HP:0001974** (supported qualitatively for FLT3-ITD: higher leukocyte counts) (jalte2023flt3mutationsin pages 3-4)
- Increased circulating blasts / blasts in blood — **HP:0031846** (blast expansion implied) (jalte2023flt3mutationsin pages 3-4)
- Bone marrow failure — **HP:0005528** (mechanistic basis: disrupted hematopoiesis) (jalte2023flt3mutationsin pages 2-3, chen2024globalnationaland pages 1-2)
- Anemia — **HP:0001903** (AML symptom statement) (chen2024globalnationaland pages 1-2)
- Thrombocytopenia — **HP:0001873** (common severe AE; also typical AML cytopenia) (perl2019gilteritiniborchemotherapy pages 1-2)
- Recurrent infections / infection susceptibility — **HP:0002719** (AML symptom statement) (chen2024globalnationaland pages 1-2)
- Bleeding — **HP:0001892** (AML symptom statement) (chen2024globalnationaland pages 1-2)
- Fever — **HP:0001945** (common AML presentation; not quantified here)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **FLT3** (fms related receptor tyrosine kinase 3). (fedorov2023targetingflt3mutation pages 1-2)

### 4.2 Pathogenic variant classes (somatic)
Two main mutation classes:
- **FLT3-ITD** (internal tandem duplications in juxtamembrane domain): ~25% of newly diagnosed AML. (fedorov2023targetingflt3mutation pages 1-2)
- **FLT3-TKD** (point mutations in the activation loop): ~7–10% of newly diagnosed AML. (fedorov2023targetingflt3mutation pages 1-2)

### 4.3 Co-mutations and modifying context
FLT3 mutations are enriched in AML with normal karyotype and are frequently co-mutated with **NPM1** and/or **DNMT3A**. (short2023treatmentofolder pages 1-2)

### 4.4 Relapse genetics
FLT3 mutations may emerge at relapse; FLT3-ITD arises more commonly at relapse than TKD (8% vs 2%). (fedorov2023targetingflt3mutation pages 1-2)

In up to ~75% of patients with FLT3-ITD at diagnosis, the mutation persists at relapse, often with higher allelic burden. (fedorov2023targetingflt3mutation pages 1-2)

### 4.5 Resistance genetics (high clinical relevance)
Resistance to FLT3 inhibitors can be:
- **On-target FLT3 mutations**, notably the **gatekeeper FLT3 F691L** (reported as conferring resistance to all current FLT3 inhibitors in one synthesis). (fedorov2023targetingflt3mutation pages 9-10)
- **Activation-loop FLT3 mutations** (e.g., D835 variants) with class-specific resistance patterns (particularly relevant for type II inhibitors). (smith2022molecularprofileof pages 2-3)
- **Off-target RAS/MAPK pathway mutations** (NRAS, KRAS, PTPN11, CBL, BRAF) emerging under selective pressure. (fedorov2023targetingflt3mutation pages 9-10)

---

## 5. Environmental Information

Environmental risk factors are better established for AML overall (not specifically FLT3-mutated AML): smoking, high BMI, and occupational exposures to benzene and formaldehyde contribute to AML-related burden and mortality in GBD analyses. (chen2024globalnationaland pages 1-2, zhou2024globalregionaland pages 13-16)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (from mutation to phenotype)
1) **FLT3 activating mutation (ITD/TKD)** → 2) **Constitutive FLT3 signaling** via PI3K, STAT5, and RAS → 3) increased leukemic cell survival/proliferation and impaired differentiation → 4) accumulation of myeloblasts (bone marrow and blood) with suppression of normal hematopoiesis → 5) clinical manifestations (cytopenia-related infections/anemia/bleeding, leukocytosis/blast burden) and higher relapse risk. (fedorov2023targetingflt3mutation pages 1-2, jalte2023flt3mutationsin pages 3-4, chen2024globalnationaland pages 1-2)

### 6.2 Key downstream pathways and therapeutic implications
- FLT3 signaling engages **PI3K, STAT5, and RAS**. (fedorov2023targetingflt3mutation pages 1-2)
- **STAT5-driven MCL-1 upregulation** contributes to resistance to BCL-2 inhibition (venetoclax); FLT3 inhibitors can downregulate MCL-1, providing rationale for combination therapy. (fedorov2023targetingflt3mutation pages 2-4)

### 6.3 Bone marrow microenvironment mechanisms
A “protective environment within the bone marrow” makes eradication of FLT3-mutant cells difficult and contributes to resistance. (fedorov2023targetingflt3mutation pages 1-2)

Mechanistic studies highlight stromal/niche-derived signals (e.g., CXCL12, FGF2) as mediators of FLT3 inhibitor resistance via MAPK pathway reactivation and leukemia stem cell protection. (fedorov2023targetingflt3mutation pages 9-10, anderson2023microenvironmentalcxcl12deletion pages 10-12)

### 6.4 Suggested GO (biological process) terms (examples)
- **GO:0008283** cell population proliferation (consistent with proliferative signaling) (fedorov2023targetingflt3mutation pages 1-2)
- **GO:0006915** apoptotic process (inhibited; AML pathogenesis includes impaired apoptosis) (negotei2023areviewof pages 1-3)
- **GO:0030154** cell differentiation / myeloid cell differentiation (blocked in FLT3-ITD) (jalte2023flt3mutationsin pages 3-4)
- **GO:0007169** transmembrane receptor protein tyrosine kinase signaling pathway (FLT3 RTK) (fedorov2023targetingflt3mutation pages 1-2)
- **GO:0070371** ERK1 and ERK2 cascade (MAPK resistance axis) (fedorov2023targetingflt3mutation pages 9-10)

### 6.5 Suggested CL (cell type) terms (examples)
- Hematopoietic stem cell — **CL:0000037** (FLT3 expression context) (fedorov2023targetingflt3mutation pages 1-2)
- Myeloid progenitor cell — **CL:0000763** (progenitor compartment) (negotei2023areviewof pages 1-3)
- Leukemia stem cell (concept used in microenvironment paper; map to hematopoietic stem/progenitor-like malignant cell; precise CL term may vary) (anderson2023microenvironmentalcxcl12deletion pages 10-12)

### 6.6 Recent developments (2023–2024 emphasis)
- Resistance biology increasingly integrates microenvironmental protection and adaptive signaling (CXCL12/p38 axis; MAPK reactivation) and suggests combination strategies to suppress adaptive resistance. (anderson2023microenvironmentalcxcl12deletion pages 10-12, fedorov2023targetingflt3mutation pages 9-10)
- 2024 AML therapeutic landscape reviews emphasize multiple newly approved targeted agents including FLT3 inhibitors and expanding combination strategies. (kantarjian2024currentstatusand pages 2-3)

---

## 7. Anatomical Structures Affected

### 7.1 Primary anatomical sites
- **Bone marrow**: primary site of blast accumulation and microenvironmental protection. (negotei2023areviewof pages 1-3, fedorov2023targetingflt3mutation pages 1-2)
- **Peripheral blood**: circulating blasts; abnormal precursor accumulation in marrow and blood. (negotei2023areviewof pages 1-3)

### 7.2 Extramedullary disease
Extramedullary involvement can occur in AML, including FLT3-mutated subsets, but the retrieved evidence did not provide organ-specific frequencies (e.g., spleen/liver infiltration rates) for FLT3-mutated AML.

### 7.3 Suggested UBERON terms
- Bone marrow — **UBERON:0002371** (negotei2023areviewof pages 1-3)
- Peripheral blood — **UBERON:0000178** (negotei2023areviewof pages 1-3)

---

## 8. Temporal Development

### 8.1 Onset
AML is an acute leukemia, with incidence increasing with age; ~80% of new AML cases occur in individuals aged ≥60. (chen2024globalnationaland pages 1-2)

### 8.2 Progression and relapse patterns (FLT3-mutated)
FLT3-ITD AML is characterized by high relapse risk after remission and persistence/emergence of FLT3-ITD at relapse in many patients. (fedorov2023targetingflt3mutation pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Inheritance
FLT3 mutations defining FLT3-mutated AML are generally **somatic**, not inherited in a Mendelian pattern in typical cases (no germline inheritance pattern was supported in the retrieved evidence set).

### 9.2 Population patterns
- AML burden disproportionately affects **older adults** and **males** in GBD analyses. (zhou2024globalregionaland pages 1-2, zhou2024globalregionaland pages 10-13)

---

## 10. Diagnostics

### 10.1 Required molecular testing
FLT3 mutation screening at diagnosis is described as mandatory, and WHO is cited as strongly advising FLT3 mutation screening in AML. (negotei2023areviewof pages 1-3)

### 10.2 Risk stratification updates (ELN 2022)
ELN 2022 removed FLT3-ITD allelic ratio from risk assignment; **FLT3-ITD positivity is classified as intermediate risk irrespective of allelic ratio or NPM1 co-mutation** (in the absence of adverse cytogenetics/other markers). (lachowiez2023comparisonandvalidation pages 1-2, fedorov2023targetingflt3mutation pages 1-2)

### 10.3 Testing workflows and MRD
Modern cohorts and validations used integrated cytogenetic and NGS approaches (karyotype, CLIA NGS, WES, fusion testing), and MRD is emphasized as a dynamic marker complementing baseline genetics. (lachowiez2023comparisonandvalidation pages 1-2)

### 10.4 FDA-approved test requirement (implementation detail)
For gilteritinib in relapsed/refractory AML, the FDA approval specifies use in patients with a FLT3 mutation “as detected by an FDA-approved test.” (pulte2021fdaapprovalsummary pages 1-3)

### 10.5 Differential diagnosis
Differential diagnosis details (e.g., AML vs MDS/AML or mixed phenotype acute leukemia) were not systematically extractable from the retrieved evidence set for this report.

---

## 11. Outcome / Prognosis

### 11.1 Baseline prognosis of FLT3-ITD AML
Prior to widespread FLT3 inhibitor use, a meta-analysis cited in a 2023 review reported **overall survival HR 1.86** and **relapse-free survival HR 1.75** for FLT3-ITD (adverse prognosis). (fedorov2023targetingflt3mutation pages 1-2)

### 11.2 Prognosis modified by FLT3 inhibitors (key trial statistics)
- **Midostaurin (frontline with intensive chemotherapy)**: RATIFY showed OS and EFS benefit (hazard ratio for death 0.78; one-sided P=0.009; hazard ratio for event/death 0.78; one-sided P=0.002). (stone2017midostaurinpluschemotherapy pages 1-2)
- **Gilteritinib (relapsed/refractory)**: ADMIRAL showed median OS 9.3 vs 5.6 months (HR 0.64). (perl2019gilteritiniborchemotherapy pages 1-2)
- **Quizartinib (newly diagnosed FLT3-ITD)**: QuANTUM-First is associated with improved OS and MRD clearance correlating with OS in post hoc analyses. (levis2022quantumfirsttrialflt3itdspecific pages 1-1)

---

## 12. Treatment

### 12.1 Current standard and approved therapies (key agents)
Evidence from recent reviews and pivotal trials supports:
- **Midostaurin + intensive chemotherapy (7+3-based induction and consolidation)** for newly diagnosed FLT3-mutated AML. (fedorov2023targetingflt3mutation pages 1-2)
- **Gilteritinib monotherapy** for relapsed/refractory FLT3-mutated AML. (fedorov2023targetingflt3mutation pages 1-2)
- **Quizartinib + chemotherapy** for newly diagnosed FLT3-ITD AML (regulatory status discussed in 2024 reviews). (cortes2024quizartinibapotent pages 1-2, leifheit2024enhancingtherapeuticefficacy pages 6-7)

A concise evidence table is provided below.

| Agent (type I/II; generation) | Setting (newly diagnosed vs R/R; with chemo or mono) | Key trial (name, PMID/DOI, year) | Key efficacy results (OS, CR/CRc, HR where available) | Regulatory notes (FDA approval month/year if explicitly available in evidence) |
|---|---|---|---|---|
| Midostaurin (Type I; 1st generation) | Newly diagnosed FLT3-mutated AML; with intensive chemotherapy (7+3) and consolidation; maintenance studied | RATIFY / CALGB 10603; DOI: 10.1056/NEJMoa1614359; 2017 | Median OS 74.7 vs 25.6 months (fedorov2023targetingflt3mutation pages 2-4, stansfield2017midostaurinanew pages 7-10); OS HR 0.78 (95% CI 0.63-0.96) (stansfield2017midostaurinanew pages 7-10); median EFS 8.2 vs 3.0 months (stansfield2017midostaurinanew pages 7-10); EFS HR 0.78 (95% CI 0.66-0.93) (cortes2024quizartinibapotent pages 1-2, stansfield2017midostaurinanew pages 7-10); CR 58.9% vs 53.5% / ~59% vs 54% (fedorov2023targetingflt3mutation pages 2-4, stansfield2017midostaurinanew pages 7-10) | FDA approved April 2017 for newly diagnosed FLT3-mutated AML (levis2017midostaurinapprovedfor pages 1-6); review notes FDA approval in 2017 (fedorov2023targetingflt3mutation pages 2-4) |
| Gilteritinib (Type I; 2nd generation) | Relapsed/refractory FLT3-mutated AML; monotherapy vs salvage chemotherapy | ADMIRAL; DOI: 10.1056/NEJMoa1902688; 2019 | Median OS 9.3 vs 5.6 months (negotei2023areviewof pages 7-8); HR for death 0.64 (95% CI 0.49-0.83) (negotei2023areviewof pages 7-8); EFS 2.8 vs 0.7 months (negotei2023areviewof pages 7-8); CR/CRh 34.0% vs 15.3% (negotei2023areviewof pages 7-8); CR 21.1% vs 10.5% (from primary trial abstract summarized in evidence search, consistent with ADMIRAL source set) | FDA approved November 28, 2018; label revised May 29, 2019 with final OS analysis (leifheit2024enhancingtherapeuticefficacy pages 6-7) |
| Quizartinib (Type II; 2nd generation) | Newly diagnosed FLT3-ITD+ AML; with induction/consolidation chemotherapy and maintenance | QuANTUM-First; NCT02668653; DOI: 10.1182/blood-2022-162739 (MRD analysis), pivotal phase 3 basis summarized in 2024 review | Median OS 31.9 vs 15.1 months (negotei2023areviewof pages 7-8); delta median OS 16.8 months (levis2022quantumfirsttrialflt3itdspecific pages 1-1); CRc by end of induction 71.6% vs 64.9% (levis2022quantumfirsttrialflt3itdspecific pages 1-1); MRD clearance associated with improved OS (levis2022quantumfirsttrialflt3itdspecific pages 1-1) | FDA approved July 2023 for FLT3-mutated AML patients per review summary; broader 2024 review states approved in US/Japan/Europe/UK for newly diagnosed FLT3-ITD+ AML with chemo and maintenance (leifheit2024enhancingtherapeuticefficacy pages 6-7, cortes2024quizartinibapotent pages 1-2) |
| Quizartinib (Type II; 2nd generation) | Relapsed/refractory FLT3-ITD+ AML; monotherapy | QuANTUM-R; pivotal phase 3, summarized in review; 2024 review context | Median OS 6.2 vs 4.7 months (negotei2023areviewof pages 7-8) | Approved in Japan as monotherapy for adult FLT3-ITD+ R/R AML in 2024 review context (month/year not explicit) (cortes2024quizartinibapotent pages 1-2) |
| Venetoclax + gilteritinib (combination, not yet standard approval as FLT3-labeled regimen) | Relapsed/refractory FLT3-mutated AML; combination oral targeted therapy | Phase Ib/II; DOI: 10.1200/JCO.22.00602; 2022 | mCRc 75% (negotei2023areviewof pages 7-8); median OS 10.0 months (negotei2023areviewof pages 7-8); FLT3 molecular response <10^-2 in 60% of evaluable responders (negotei2023areviewof pages 7-8) | Investigational/combination strategy; no FDA approval month/year stated in evidence (negotei2023areviewof pages 7-8) |


*Table: This table summarizes the principal FLT3-targeted therapies used in FLT3-mutated AML, their pivotal trial evidence, and regulatory context. It is useful for quickly comparing frontline versus relapsed/refractory use, efficacy benchmarks, and approval timing.*

### 12.2 Safety and monitoring (real-world implementation)
Gilteritinib labeling includes boxed warning for **differentiation syndrome**, and warnings for **QT prolongation**, PRES, pancreatitis, and embryo-fetal toxicity, requiring frequent ECG and chemistry monitoring. (pulte2021fdaapprovalsummary pages 1-3)

### 12.3 Combination strategies (active development)
Because FLT3-ITD can mediate venetoclax resistance and relapse, combination strategies incorporating FLT3 inhibitors with venetoclax and/or hypomethylating agents are under investigation and show encouraging early results in reviews; mechanistically, FLT3 inhibition can reduce STAT5→MCL-1 signaling that contributes to venetoclax resistance. (short2023treatmentofolder pages 1-2, fedorov2023targetingflt3mutation pages 2-4)

### 12.4 Allogeneic hematopoietic stem cell transplantation (allo-HSCT)
Given poor relapsed/refractory outcomes and high relapse risk in FLT3-ITD AML, allo-HSCT is generally recommended in first complete remission in many treatment paradigms. (fedorov2023targetingflt3mutation pages 1-2)

### 12.5 Suggested MAXO terms (examples)
- Antineoplastic chemotherapy regimen — **MAXO:0000647** (intensive induction/consolidation)
- Tyrosine kinase inhibitor therapy — **MAXO:0000644** (FLT3 inhibitors)
- Allogeneic hematopoietic stem cell transplantation — **MAXO:0000747**
- Measurable residual disease monitoring — (MAXO term availability may vary; concept supported in ELN-related sources) (lachowiez2023comparisonandvalidation pages 1-2)

---

## 13. Prevention

No primary prevention specific to FLT3-mutated AML was identified; prevention strategies for AML overall focus on modifying population-level risk factors highlighted in GBD analyses:
- Tobacco smoking reduction
- Obesity/high BMI reduction
- Occupational exposure control for benzene and formaldehyde (chen2024globalnationaland pages 1-2, zhou2024globalregionaland pages 13-16)

---

## 14. Other Species / Natural Disease

This section is not directly applicable as a “naturally occurring” transmissible disease; however, AML-like phenotypes driven by FLT3-ITD are modeled in animals (see Model Organisms).

---

## 15. Model Organisms

### 15.1 Common model systems used in FLT3-ITD AML research
- **Genetically engineered mouse models (GEMMs)** focusing on bone marrow niche resistance and leukemia stem cell biology in Flt3-ITD AML. (anderson2023microenvironmentalcxcl12deletion pages 10-12)
- **In vivo xenografts and PDX models** using FLT3-ITD AML cells to study adaptive resistance and to test inhibitor combinations. (azhar2023rationalpolypharmacologicaltargeting pages 2-3, xiao2023gnf7anovel pages 1-2)
- **Engineered Ba/F3 cells** expressing FLT3-ITD and drug-resistant variants for kinase-inhibitor testing and resistance mapping. (azhar2023rationalpolypharmacologicaltargeting pages 2-3)
- **Zebrafish transgenic/functional models** have been used to evaluate FLT3-ITD effects in development and as a disease-relevant signaling context. (he2020follistatinisa pages 15-16)

---

## Evidence-based direct quotes (abstract-level)
- “FLT3 mutations are present in 30% of newly diagnosed patients with acute myeloid leukemia.” (Fedorov et al., 2023; https://doi.org/10.3390/cancers15082312; published 15 Apr 2023) (fedorov2023targetingflt3mutation pages 1-2)
- “FLT3 mutation screening at diagnosis is mandatory…” (Negotei et al., 2023; https://doi.org/10.3390/jcm12206429; published 10 Oct 2023) (negotei2023areviewof pages 1-3)
- “In 2019, the older age group of 60 to 89 years reported 61,559 new cases of AML, with the corresponding number of deaths being 53,620, and the estimated DALYs standing at 990,656.” (Chen et al., 2024; https://doi.org/10.3389/fpubh.2023.1329529; published 11 Jan 2024) (chen2024globalnationaland pages 1-2)
- “The median overall survival in the gilteritinib group was significantly longer than that in the chemotherapy group (9.3 months vs. 5.6 months; hazard ratio for death, 0.64…)” (Perl et al., 2019; https://doi.org/10.1056/NEJMoa1902688; published Oct 31, 2019) (perl2019gilteritiniborchemotherapy pages 1-2)

---

## Limitations of this report (data not retrieved in accessible evidence)
- Subtype-specific MONDO/OMIM/Orphanet identifiers for “FLT3-mutated AML” were not located in the retrieved excerpts.
- Quantitative frequencies for many presenting symptoms and organ-specific extramedullary involvement rates were not extractable from the retrieved sources.
- Differential diagnosis details were not systematically captured from guideline texts in the available excerpts.


References

1. (negotei2023areviewof pages 1-3): Cristina Negotei, Andrei Colita, Iuliana Mitu, Anca Roxana Lupu, Mihai-Emilian Lapadat, Constanta Elena Popovici, Madalina Crainicu, Oana Stanca, and Nicoleta Mariana Berbec. A review of flt3 kinase inhibitors in aml. Journal of Clinical Medicine, 12:6429, Oct 2023. URL: https://doi.org/10.3390/jcm12206429, doi:10.3390/jcm12206429. This article has 68 citations.

2. (fedorov2023targetingflt3mutation pages 1-2): Kateryna Fedorov, Abhishek Maiti, and Marina Konopleva. Targeting flt3 mutation in acute myeloid leukemia: current strategies and future directions. Cancers, 15:2312, Apr 2023. URL: https://doi.org/10.3390/cancers15082312, doi:10.3390/cancers15082312. This article has 43 citations.

3. (short2023treatmentofolder pages 1-2): Nicholas J. Short, Daniel Nguyen, and Farhad Ravandi. Treatment of older adults with flt3-mutated aml: emerging paradigms and the role of frontline flt3 inhibitors. Blood Cancer Journal, Sep 2023. URL: https://doi.org/10.1038/s41408-023-00911-w, doi:10.1038/s41408-023-00911-w. This article has 62 citations and is from a domain leading peer-reviewed journal.

4. (zhou2024globalregionaland pages 2-4): Yeming Zhou, Guiqin Huang, Xiaoya Cai, Ying Liu, Bingxin Qian, and Dengju Li. Global, regional, and national burden of acute myeloid leukemia, 1990–2021: a systematic analysis for the global burden of disease study 2021. Biomarker Research, Sep 2024. URL: https://doi.org/10.1186/s40364-024-00649-y, doi:10.1186/s40364-024-00649-y. This article has 114 citations and is from a peer-reviewed journal.

5. (lachowiez2023comparisonandvalidation pages 1-2): Curtis A. Lachowiez, Nicola Long, Jennifer Saultz, Arpita Gandhi, Laura F. Newell, Brandon Hayes-Lattin, Richard T. Maziarz, Jessica Leonard, Daniel Bottomly, Shannon McWeeney, Jennifer Dunlap, Richard Press, Gabrielle Meyers, Ronan Swords, Rachel J. Cook, Jeffrey W. Tyner, Brian J. Druker, and Elie Traer. Comparison and validation of the 2022 european leukemianet guidelines in acute myeloid leukemia. Blood Advances, 7:1899-1909, May 2023. URL: https://doi.org/10.1182/bloodadvances.2022009010, doi:10.1182/bloodadvances.2022009010. This article has 112 citations and is from a peer-reviewed journal.

6. (stone2017midostaurinpluschemotherapy pages 1-2): Richard M. Stone, Sumithra J. Mandrekar, Ben L. Sanford, Kristina Laumann, Susan Geyer, Clara D. Bloomfield, Christian Thiede, Thomas W. Prior, Konstanze Döhner, Guido Marcucci, Francesco Lo-Coco, Rebecca B. Klisovic, Andrew Wei, Jorge Sierra, Miguel A. Sanz, Joseph M. Brandwein, Theo de Witte, Dietger Niederwieser, Frederick R. Appelbaum, Bruno C. Medeiros, Martin S. Tallman, Jürgen Krauter, Richard F. Schlenk, Arnold Ganser, Hubert Serve, Gerhard Ehninger, Sergio Amadori, Richard A. Larson, and Hartmut Döhner. Midostaurin plus chemotherapy for acute myeloid leukemia with a<i>flt3</i>mutation. New England Journal of Medicine, 377:454-464, Aug 2017. URL: https://doi.org/10.1056/nejmoa1614359, doi:10.1056/nejmoa1614359. This article has 2799 citations and is from a highest quality peer-reviewed journal.

7. (perl2019gilteritiniborchemotherapy pages 1-2): Alexander E. Perl, Giovanni Martinelli, Jorge E. Cortes, Andreas Neubauer, Ellin Berman, Stefania Paolini, Pau Montesinos, Maria R. Baer, Richard A. Larson, Celalettin Ustun, Francesco Fabbiano, Harry P. Erba, Antonio Di Stasi, Robert Stuart, Rebecca Olin, Margaret Kasner, Fabio Ciceri, Wen-Chien Chou, Nikolai Podoltsev, Christian Recher, Hisayuki Yokoyama, Naoko Hosono, Sung-Soo Yoon, Je-Hwan Lee, Timothy Pardee, Amir T. Fathi, Chaofeng Liu, Nahla Hasabou, Xuan Liu, Erkut Bahceci, and Mark J. Levis. Gilteritinib or chemotherapy for relapsed or refractory <i>flt3</i> -mutated aml. New England Journal of Medicine, 381:1728-1740, Oct 2019. URL: https://doi.org/10.1056/nejmoa1902688, doi:10.1056/nejmoa1902688. This article has 1487 citations and is from a highest quality peer-reviewed journal.

8. (chen2024globalnationaland pages 1-2): Pengyin Chen, Xinling Liu, Yao Zhao, Yuyuan Hu, Jiaxin Guo, and Haiying Wang. Global, national, and regional burden of acute myeloid leukemia among 60–89 years-old individuals: insights from a study covering the period 1990 to 2019. Frontiers in Public Health, Jan 2024. URL: https://doi.org/10.3389/fpubh.2023.1329529, doi:10.3389/fpubh.2023.1329529. This article has 34 citations.

9. (zhou2024globalregionaland pages 13-16): Yeming Zhou, Guiqin Huang, Xiaoya Cai, Ying Liu, Bingxin Qian, and Dengju Li. Global, regional, and national burden of acute myeloid leukemia, 1990–2021: a systematic analysis for the global burden of disease study 2021. Biomarker Research, Sep 2024. URL: https://doi.org/10.1186/s40364-024-00649-y, doi:10.1186/s40364-024-00649-y. This article has 114 citations and is from a peer-reviewed journal.

10. (jalte2023flt3mutationsin pages 3-4): Meryem Jalte, Meriame Abbassi, Hinde El Mouhi, Hanae Daha Belghiti, Mohamed Ahakoud, and Hicham Bekkari. Flt3 mutations in acute myeloid leukemia: unraveling the molecular mechanisms and implications for targeted therapies. Cureus, Sep 2023. URL: https://doi.org/10.7759/cureus.45765, doi:10.7759/cureus.45765. This article has 38 citations.

11. (jalte2023flt3mutationsin pages 2-3): Meryem Jalte, Meriame Abbassi, Hinde El Mouhi, Hanae Daha Belghiti, Mohamed Ahakoud, and Hicham Bekkari. Flt3 mutations in acute myeloid leukemia: unraveling the molecular mechanisms and implications for targeted therapies. Cureus, Sep 2023. URL: https://doi.org/10.7759/cureus.45765, doi:10.7759/cureus.45765. This article has 38 citations.

12. (fedorov2023targetingflt3mutation pages 9-10): Kateryna Fedorov, Abhishek Maiti, and Marina Konopleva. Targeting flt3 mutation in acute myeloid leukemia: current strategies and future directions. Cancers, 15:2312, Apr 2023. URL: https://doi.org/10.3390/cancers15082312, doi:10.3390/cancers15082312. This article has 43 citations.

13. (smith2022molecularprofileof pages 2-3): Catherine C. Smith, Mark J. Levis, Alexander E. Perl, Jason E. Hill, Matt Rosales, and Erkut Bahceci. Molecular profile of <i>flt3</i>-mutated relapsed/refractory patients with aml in the phase 3 admiral study of gilteritinib. Blood Advances, 6:2144-2155, Mar 2022. URL: https://doi.org/10.1182/bloodadvances.2021006489, doi:10.1182/bloodadvances.2021006489. This article has 88 citations and is from a peer-reviewed journal.

14. (fedorov2023targetingflt3mutation pages 2-4): Kateryna Fedorov, Abhishek Maiti, and Marina Konopleva. Targeting flt3 mutation in acute myeloid leukemia: current strategies and future directions. Cancers, 15:2312, Apr 2023. URL: https://doi.org/10.3390/cancers15082312, doi:10.3390/cancers15082312. This article has 43 citations.

15. (anderson2023microenvironmentalcxcl12deletion pages 10-12): Nicholas R. Anderson, Vipul Sheth, Hui Li, Mason W. Harris, Shaowei Qiu, David K. Crossman, Harish Kumar, Puneet Agarwal, Takashi Nagasawa, Andrew J. Paterson, Robert S. Welner, and Ravi Bhatia. Microenvironmental cxcl12 deletion enhances flt3-itd acute myeloid leukemia stem cell response to therapy by reducing p38 mapk signaling. Leukemia, 37:560-570, Dec 2023. URL: https://doi.org/10.1038/s41375-022-01798-5, doi:10.1038/s41375-022-01798-5. This article has 33 citations and is from a highest quality peer-reviewed journal.

16. (kantarjian2024currentstatusand pages 2-3): Hagop Kantarjian, Gautam Borthakur, Naval Daver, Courtney D. DiNardo, Ghayas Issa, Elias Jabbour, Tapan Kadia, Koji Sasaki, Nicholas J. Short, Musa Yilmaz, and Farhad Ravandi. Current status and research directions in acute myeloid leukemia. Blood Cancer Journal, Sep 2024. URL: https://doi.org/10.1038/s41408-024-01143-2, doi:10.1038/s41408-024-01143-2. This article has 113 citations and is from a domain leading peer-reviewed journal.

17. (zhou2024globalregionaland pages 1-2): Yeming Zhou, Guiqin Huang, Xiaoya Cai, Ying Liu, Bingxin Qian, and Dengju Li. Global, regional, and national burden of acute myeloid leukemia, 1990–2021: a systematic analysis for the global burden of disease study 2021. Biomarker Research, Sep 2024. URL: https://doi.org/10.1186/s40364-024-00649-y, doi:10.1186/s40364-024-00649-y. This article has 114 citations and is from a peer-reviewed journal.

18. (zhou2024globalregionaland pages 10-13): Yeming Zhou, Guiqin Huang, Xiaoya Cai, Ying Liu, Bingxin Qian, and Dengju Li. Global, regional, and national burden of acute myeloid leukemia, 1990–2021: a systematic analysis for the global burden of disease study 2021. Biomarker Research, Sep 2024. URL: https://doi.org/10.1186/s40364-024-00649-y, doi:10.1186/s40364-024-00649-y. This article has 114 citations and is from a peer-reviewed journal.

19. (pulte2021fdaapprovalsummary pages 1-3): E. Dianne Pulte, Kelly J. Norsworthy, Yaping Wang, Qing Xu, Hisham Qosa, Ramadevi Gudi, Donna Przepiorka, Wentao Fu, Olanrewaju O. Okusanya, Kirsten B. Goldberg, R. Angelo De Claro, Ann T. Farrell, and Richard Pazdur. Fda approval summary: gilteritinib for relapsed or refractory acute myeloid leukemia with a flt3 mutation. Clinical Cancer Research, 27:3515-3521, Feb 2021. URL: https://doi.org/10.1158/1078-0432.ccr-20-4271, doi:10.1158/1078-0432.ccr-20-4271. This article has 94 citations and is from a highest quality peer-reviewed journal.

20. (levis2022quantumfirsttrialflt3itdspecific pages 1-1): Mark J. Levis, Harry P. Erba, Pau Montesinos, Radovan Vrhovac, Elzbieta Patkowska, Heeje Kim, Pavel Zak, Po-Nan Wang, Jaime E. Connolly Rohrbach, Ken CN Chang, James Hanyok, Li Liu, Yasser Mostafa Kamel, Arnaud Lesegretain, Jorge E. Cortes, Mikkael A. Sekeres, Hervé Dombret, Sergio Amadori, Jianxiang Wang, Richard F. Schlenk, and Alexander Perl. Quantum-first trial: flt3-itd-specific mrd clearance is associated with improved overall survival. Blood, 140:546-548, Nov 2022. URL: https://doi.org/10.1182/blood-2022-162739, doi:10.1182/blood-2022-162739. This article has 10 citations and is from a highest quality peer-reviewed journal.

21. (cortes2024quizartinibapotent pages 1-2): Jorge Cortes. Quizartinib: a potent and selective flt3 inhibitor for the treatment of patients with flt3-itd–positive aml. Journal of Hematology & Oncology, Nov 2024. URL: https://doi.org/10.1186/s13045-024-01617-7, doi:10.1186/s13045-024-01617-7. This article has 30 citations and is from a domain leading peer-reviewed journal.

22. (leifheit2024enhancingtherapeuticefficacy pages 6-7): Malia E. Leifheit, Gunnar Johnson, Timothy M. Kuzel, Jeffrey R. Schneider, Edward Barker, Hyun D. Yun, Celalettin Ustun, Josef W. Goldufsky, Kajal Gupta, and Amanda L. Marzo. Enhancing therapeutic efficacy of flt3 inhibitors with combination therapy for treatment of acute myeloid leukemia. International Journal of Molecular Sciences, 25:9448, Aug 2024. URL: https://doi.org/10.3390/ijms25179448, doi:10.3390/ijms25179448. This article has 15 citations.

23. (stansfield2017midostaurinanew pages 7-10): Lindsay C. Stansfield and Daniel A. Pollyea. Midostaurin: a new oral agent targeting fms‐like tyrosine kinase 3‐mutant acute myeloid leukemia. Pharmacotherapy: The Journal of Human Pharmacology and Drug Therapy, 37:1586-1599, Dec 2017. URL: https://doi.org/10.1002/phar.2039, doi:10.1002/phar.2039. This article has 26 citations.

24. (levis2017midostaurinapprovedfor pages 1-6): Mark Levis. Midostaurin approved for flt3-mutated aml. Blood, 129:3403-3406, Jun 2017. URL: https://doi.org/10.1182/blood-2017-05-782292, doi:10.1182/blood-2017-05-782292. This article has 373 citations and is from a highest quality peer-reviewed journal.

25. (negotei2023areviewof pages 7-8): Cristina Negotei, Andrei Colita, Iuliana Mitu, Anca Roxana Lupu, Mihai-Emilian Lapadat, Constanta Elena Popovici, Madalina Crainicu, Oana Stanca, and Nicoleta Mariana Berbec. A review of flt3 kinase inhibitors in aml. Journal of Clinical Medicine, 12:6429, Oct 2023. URL: https://doi.org/10.3390/jcm12206429, doi:10.3390/jcm12206429. This article has 68 citations.

26. (azhar2023rationalpolypharmacologicaltargeting pages 2-3): Mohammad Azhar, Zachary Kincaid, Meenu Kesarwani, Jacob Menke, Joshua Schwieterman, Sekhu Ansari, Angela Reaves, Arhama Ahmed, Rammsha Shehzad, Areeba Khan, Nuha Syed, Noor Amir, Mark Wunderlich, Tahir Latif, William Seibel, and Mohammad Azam. Rational polypharmacological targeting of flt3, jak2, abl, and erk1 suppresses the adaptive resistance to flt3 inhibitors in aml. Blood Advances, 7:1460-1476, Apr 2023. URL: https://doi.org/10.1182/bloodadvances.2022007486, doi:10.1182/bloodadvances.2022007486. This article has 8 citations and is from a peer-reviewed journal.

27. (xiao2023gnf7anovel pages 1-2): Xinhua Xiao, Peihong Wang, Weina Zhang, Jiayi Wang, Mansi Cai, Hua Jiang, Yingli Wu, and Huizhuang Shan. Gnf-7, a novel flt3 inhibitor, overcomes drug resistance for the treatment of flt3‑itd acute myeloid leukemia. Cancer Cell International, Nov 2023. URL: https://doi.org/10.1186/s12935-023-03142-y, doi:10.1186/s12935-023-03142-y. This article has 5 citations and is from a peer-reviewed journal.

28. (he2020follistatinisa pages 15-16): Bai‐Liang He, Ning Yang, Cheuk Him Man, Nelson Ka‐Lam Ng, Chae‐Yin Cher, Ho‐Ching Leung, Leo Lai‐Hok Kan, Bowie Yik‐Ling Cheng, Stephen Sze‐Yuen Lam, Michelle Lu‐Lu Wang, Chun‐Xiao Zhang, Hin Kwok, Grace Cheng, Rakesh Sharma, Alvin Chun‐Hang Ma, Chi‐Wai Eric So, Yok‐Lam Kwong, and Anskar Yu‐Hung Leung. Follistatin is a novel therapeutic target and biomarker in flt3/itd acute myeloid leukemia. EMBO Molecular Medicine, Mar 2020. URL: https://doi.org/10.15252/emmm.201910895, doi:10.15252/emmm.201910895. This article has 21 citations and is from a highest quality peer-reviewed journal.
