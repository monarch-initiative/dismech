---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:37:26.676794'
end_time: '2026-05-09T09:50:32.891969'
duration_seconds: 786.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Kaposi Sarcoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kaposi Sarcoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Kaposi Sarcoma** covering all of the
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
- **Disease Name:** Kaposi Sarcoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Kaposi Sarcoma** covering all of the
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


# Kaposi Sarcoma (KS): Disease Characteristics Research Report

## Target Disease
- **Disease name:** Kaposi sarcoma (KS)
- **Category:** Vascular (angioproliferative) tumor/neoplasm of endothelial lineage, strongly associated with an oncogenic herpesvirus (KSHV/HHV-8), typically requiring immune dysfunction/immunosuppression as a cofactor (russo2024kaposi’ssarcomaevaluation pages 1-2, denaro2024managementandfuture pages 1-2).
- **Key identifiers (available in retrieved sources):**
  - **ICD-10:** **C46** (Kaposi sarcoma) and **B21.0** (HIV disease resulting in Kaposi’s sarcoma) are used for surveillance in CDC WONDER analyses (raja2025kaposisarcomaincidence pages 1-2).
  - **Open Targets / EFO:** **EFO_0000558** (Kaposi’s sarcoma) and **EFO_0002613** (iatrogenic Kaposi’s sarcoma) appear in Open Targets disease entities (OpenTargets Search: Kaposi sarcoma).
  - **MONDO (available from Open Targets as susceptibility entity):** **MONDO_0007845** (“Kaposi sarcoma, susceptibility to”) (OpenTargets Search: Kaposi sarcoma).
  - **Note on missing IDs:** This tool run did not retrieve a MONDO identifier explicitly for KS itself (distinct from the “susceptibility to” concept), nor MeSH/Orphanet/OMIM IDs; these would normally be retrieved from ontology portals (e.g., MONDO, MeSH Browser, Orphanet) but were not available within the current evidence set.

### Synonyms / alternative names
- “Kaposi’s sarcoma” (with apostrophe), “KS” (russo2024kaposi’ssarcomaevaluation pages 1-2, patel2023clinicalmanagementof pages 2-4).
- Subtype descriptors commonly used: **classic KS**, **endemic (African) KS**, **iatrogenic/post-transplant KS**, **epidemic/HIV-associated KS**; some reviews describe a proposed **HIV-negative MSM-associated subtype** (denaro2024managementandfuture pages 1-2, patel2023clinicalmanagementof pages 2-4).

### Evidence provenance
This report is derived from **aggregated disease-level resources** (peer-reviewed reviews and epidemiologic studies) plus **cohort studies/trials**, not from individual EHRs (russo2024kaposi’ssarcomaevaluation pages 1-2, patel2023clinicalmanagementof pages 2-4, raja2025kaposisarcomaincidence pages 1-2, volkow2023impactofvalganciclovir pages 1-2, akanbi2023incidentkaposisarcoma pages 2-4).

---

## 1. Disease Information (overview and current understanding)
Kaposi sarcoma is a vascular/angioproliferative tumor that most often presents with **cutaneous lesions** but may involve **mucosal surfaces and visceral organs**, particularly when host immune function is impaired (e.g., HIV infection or iatrogenic immunosuppression) (russo2024kaposi’ssarcomaevaluation pages 1-2, patel2023clinicalmanagementof pages 2-4). Multiple sources emphasize that **HHV-8/KSHV infection is the necessary etiologic agent**, with immune dysfunction acting as a key enabling factor for tumorigenesis (denaro2024managementandfuture pages 2-5, denaro2024managementandfuture pages 1-2).

**Current clinical-epidemiologic classification**: four major subtypes (classic, endemic, iatrogenic, epidemic/HIV-associated) are widely accepted, with a proposed fifth subtype in HIV-negative MSM described in recent reviews (denaro2024managementandfuture pages 1-2, patel2023clinicalmanagementof pages 2-4).

---

## 2. Etiology

### 2.1 Primary causal factor (infectious)
- **Kaposi sarcoma herpesvirus (KSHV) / human herpesvirus-8 (HHV-8)** is the etiologic agent of KS (denaro2024managementandfuture pages 2-5, denaro2024managementandfuture pages 1-2).
- In a clinical management review, KSHV is described as a **lifelong persistent herpesvirus** with two infection programs: **latency (default)** and **lytic replication**, infecting multiple cell types (including B cells and endothelial-lineage cells), and with disease manifestations varying by latent vs lytic phenotype (patel2023clinicalmanagementof pages 2-4).

**Direct abstract quotes (supporting etiology/definition):**
- “Kaposi sarcoma (KS) is an intermediate-grade vascular tumour that has undergone major treatment and diagnostic breakthroughs following the discovery of Human herpesvirus 8 (HHV8).” (Bagratee et al., 2025) (bagratee2025recentadvancesin pages 4-6)
- “Kaposi’s sarcoma (KS) is a cutaneous neoplasm of endothelial origin. The causative agent is the human herpes virus-8 (HHV-8) which, combined with an immune system impairment, causes cell proliferation.” (Denaro et al., 2024) (denaro2024managementandfuture pages 1-2)

### 2.2 Risk factors
**Immunodeficiency / immune dysregulation**
- HIV infection and advanced immunosuppression are strongly linked to epidemic KS and to more frequent visceral/mucosal involvement (denaro2024managementandfuture pages 2-5, patel2023clinicalmanagementof pages 2-4).
- **Iatrogenic immunosuppression** (e.g., after solid organ transplantation) is a major risk context; classic KS tends to be more indolent, while iatrogenic KS may improve when immunosuppression is reduced (denaro2024managementandfuture pages 2-5, saowapa2024evaluatingkaposisarcoma pages 1-2).

**Transplant / immunosuppression-related risk (quantitative):**
- One evidence-based review states that transplant recipients have a roughly **60-fold increased risk** of iatrogenic KS (denaro2024managementandfuture pages 2-5).
- A kidney-transplant meta-analysis estimated KS prevalence **1.5%** overall, with higher prevalence in African and Middle Eastern recipients (**1.7%** each) vs Western recipients (**0.07%**) and increased odds in males (**OR 2.36**) (Saowapa et al., 2024; published Jan 2024) (saowapa2024evaluatingkaposisarcoma pages 1-2).

**Demographic/geographic risk patterns**
- Classic KS is described as more frequent in older men and in Mediterranean/Eastern European/Middle Eastern ancestry groups (denaro2024managementandfuture pages 2-5, denaro2024managementandfuture pages 1-2).

### 2.3 Protective factors
- **Antiretroviral therapy (ART)** for HIV is consistently associated with **reduced KS incidence** and improved outcomes, interpreted as immune reconstitution and improved HIV control (raja2025kaposisarcomaincidence pages 1-2, akanbi2023incidentkaposisarcoma pages 2-4).

### 2.4 Gene–environment / host–virus interactions
- Mechanistically, KSHV’s latent and lytic programs, host immune impairment, and inflammatory/angiogenic cytokine environments (e.g., IL-6, VEGF) interact to drive angioproliferation and lesion evolution (denaro2024managementandfuture pages 2-5, patel2023clinicalmanagementof pages 2-4).

---

## 3. Phenotypes (clinical manifestations)

### 3.1 Core phenotypes and HPO suggestions
KS lesions are classically described as violaceous/purple macules, papules, plaques, and nodules; transplant-associated and HIV-associated disease may be disseminated and involve mucosal and visceral sites (patel2023clinicalmanagementof pages 2-4, saowapa2024evaluatingkaposisarcoma pages 1-2).

**Cutaneous lesions (symptom/sign)**
- **Description:** Cutaneous lesions are common and often lower-extremity predominant (russo2024kaposi’ssarcomaevaluation pages 1-2, patel2023clinicalmanagementof pages 2-4).
- **HPO suggestions:** *Cutaneous hemangioma/vascular lesion*, *Skin nodule*, *Purpura*, *Hyperpigmented skin lesion* (proposed mappings).

**Mucosal/oral involvement (clinical sign)**
- **Description:** Oral/oropharyngeal disease is recognized in KS, especially in epidemic KS (patel2023clinicalmanagementof pages 2-4).
- **HPO suggestions:** *Oral mucosal lesion*, *Gingival lesion*, *Palatal lesion* (proposed mappings).

**Visceral involvement (clinical sign/complication)**
- **GI involvement:** KS may involve GI tract; endoscopic biopsy is recommended for suspicious lesions (patel2023clinicalmanagementof pages 2-4).
- **Pulmonary involvement:** Pulmonary/airway KS can occur; bronchoscopy is important but biopsy is often avoided due to bleeding risk (patel2023clinicalmanagementof pages 2-4).
- **HPO suggestions:** *Gastrointestinal hemorrhage*, *Abdominal pain*, *Dyspnea*, *Hemoptysis* (proposed mappings).

**Lymphatic involvement and edema**
- Lymphedema is noted as part of disseminated disease definitions in trials and is a recognized complication (volkow2023impactofvalganciclovir pages 1-2).
- **HPO suggestion:** *Lymphedema*.

### 3.2 Frequency, onset, and progression (with quantitative examples)
- In a mixed-subtype retrospective cohort (Padua, Italy; 1993–2022; **n=86**), **cutaneous involvement** occurred in **77.9%**, and **lower-limb involvement** in **51.16%**; **61.63%** had single-site disease (Russo et al., published Feb 2024) (russo2024kaposi’ssarcomaevaluation pages 1-2, russo2024kaposi’ssarcomaevaluation pages 2-4).
- Classic KS is described as typically **slow-growing** with visceral involvement in **<10%** (denaro2024managementandfuture pages 2-5).

### 3.3 Quality-of-life impact
Direct QoL instrument results (e.g., EQ-5D/SF-36) were not available in the retrieved evidence set; however, reviews emphasize symptom palliation, edema reduction, and psychological support as important treatment goals (denaro2024managementandfuture pages 1-2).

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **No germline causal gene** was established in the retrieved evidence as determinative for KS; KS is primarily an **infection-associated malignancy**. Some reviews discuss host genetic associations (e.g., cytokine pathways) but without a definitive single-gene Mendelian etiology in this evidence set (revenko2026classickaposisarcoma pages 1-2).

### 4.2 Molecular/target annotations (host)
Open Targets highlights disease–target associations including **IL6** and **TOP2A** (the latter consistent with cytotoxic chemotherapy targets), and retinoid receptor family members (RARA/RARB/RARG/RXR*) (OpenTargets Search: Kaposi sarcoma). This is *association evidence* and should not be interpreted as causal.

---

## 5. Environmental Information

### 5.1 Infectious agent
- KSHV/HHV-8 is the relevant infectious agent (denaro2024managementandfuture pages 1-2, patel2023clinicalmanagementof pages 2-4).

### 5.2 Immunosuppressive exposures
- Post-transplant immunosuppression is strongly associated with iatrogenic KS; reduction/withdrawal of immunosuppression is a key management lever and can lead to remissions (saowapa2024evaluatingkaposisarcoma pages 1-2).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (current model)
1. **KSHV acquisition and persistence**: KSHV establishes lifelong infection with a default latent program; virus can enter multiple cell types and persist in latently infected cells (patel2023clinicalmanagementof pages 2-4).
2. **Immune impairment enables tumorigenesis**: HIV infection or iatrogenic immunosuppression reduces immune surveillance, enabling expansion of infected cells and pro-angiogenic inflammation (denaro2024managementandfuture pages 2-5, patel2023clinicalmanagementof pages 2-4).
3. **Latent and lytic gene expression promotes angiogenesis/inflammation**: Reviews emphasize that both latent and lytic phases contribute to pathogenesis, including cytokine dysregulation and angiogenic signaling (denaro2024managementandfuture pages 2-5, patel2023clinicalmanagementof pages 2-4).
4. **Lesion development with KSHV-infected spindle cells**: KS lesions are characterized by spindle cells with endothelial characteristics and aberrant angiogenesis (li2024mappingherpesvirusdrivenimpacts pages 5-9, li2024mappingherpesvirusdrivenimpacts pages 1-5).

### 6.2 Cell types (CL suggestions)
- **Endothelial cells** (spindle cells with endothelial characteristics) are central (CL: *endothelial cell*; proposed) (li2024mappingherpesvirusdrivenimpacts pages 5-9, li2024mappingherpesvirusdrivenimpacts pages 1-5).
- **B cells** are a KSHV-infected reservoir/cell type relevant across KSHV diseases (CL: *B cell*) (patel2023clinicalmanagementof pages 2-4).
- **Fibroblast-like stromal cells / tumor-associated fibroblast-like cells** implicated in xenograft microenvironment and CXCL12 signaling (CL: *fibroblast*) (li2024mappingherpesvirusdrivenimpacts pages 5-9).

### 6.3 Pathway/process annotations (GO suggestions)
Evidence-supported processes to map include:
- **Angiogenesis / blood vessel morphogenesis** (GO: *angiogenesis*, *blood vessel development*) (denaro2024managementandfuture pages 2-5, li2024mappingherpesvirusdrivenimpacts pages 5-9).
- **Inflammatory response / cytokine-mediated signaling** (e.g., IL-6-related biology) (GO: *cytokine-mediated signaling pathway*) (denaro2024managementandfuture pages 2-5, patel2023clinicalmanagementof pages 2-4).
- **Immune evasion and immune system process** (GO: *immune system process*) (patel2023clinicalmanagementof pages 2-4).

### 6.4 Recent developments (2023–2024 priority)
**Patient-derived xenograft (PDX) models and spatial transcriptomics (2024)**
- A 2024 bioRxiv preprint established orthotopic KS PDX models with high engraftment and demonstrated expansion of LANA+ KSHV-infected endothelial regions and increased viral transcripts by spatial transcriptomics (Li et al., posted Sep 2024) (li2024mappingherpesvirusdrivenimpacts pages 5-9, li2024mappingherpesvirusdrivenimpacts pages 1-5).
- Quantitative highlights: KS tumors maintained in **27/28** PDXs up to **272 days**; LANA+ cell density increased mean **4.3-fold**; LANA+ fraction **15%→62%**; dual LANA+/Ki-67+ cells **1%→5.6%** (li2024mappingherpesvirusdrivenimpacts pages 5-9).

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue involvement (UBERON suggestions)
- **Skin** (UBERON: *skin*)—primary site in many cases (russo2024kaposi’ssarcomaevaluation pages 1-2).
- **Lymph node** (UBERON: *lymph node*)—may be involved, including without skin lesions in some contexts (patel2023clinicalmanagementof pages 2-4).
- **Gastrointestinal tract** (UBERON: *gastrointestinal tract*) (patel2023clinicalmanagementof pages 2-4).
- **Respiratory system / lung / bronchus** (UBERON: *lung*, *bronchus*) (patel2023clinicalmanagementof pages 2-4).

### 7.2 Subcellular and compartments
Not specifically addressed in the retrieved KS-focused evidence; KSHV latency as episomes and latent gene expression are described at a conceptual level (patel2023clinicalmanagementof pages 2-4).

---

## 8. Temporal Development

### 8.1 Onset patterns
- Classic KS: typically older age at onset (median ~70 years reported) (denaro2024managementandfuture pages 2-5).
- Endemic KS: includes childhood forms (median age 4–9 years in one review summary) (denaro2024managementandfuture pages 2-5).

### 8.2 Progression and staging
- KS can be indolent (classic) or aggressive with visceral and nodal disease (HIV-associated) (denaro2024managementandfuture pages 2-5).
- Detailed staging systems for classic KS were not extracted textually here, but the Denaro 2024 review includes staging tables and a systemic therapy management table (image evidence below) (denaro2024managementandfuture media 1e1c9584).

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent statistics)

**United States (registry-based; 1999–2020)**
- “From 1999 to 2020, **27,886 KS cases and 4,380 deaths occurred**.” (Raja et al., published Nov 2025) (raja2025kaposisarcomaincidence pages 1-2).
- Sex disparity: “Overall AAIR was **0.99 in men versus 0.10 in women**, and AAMR **0.16 versus 0.01**” per 100,000 (raja2025kaposisarcomaincidence pages 1-2).
- Race disparity: “Black men experienced the highest AAIR (**2.23**) and AAMR (**0.40**)… exceeding White men (**0.79** and **0.13**)” (raja2025kaposisarcomaincidence pages 1-2).

**Nigeria (HIV clinic cohort; 2006–2016; ART eligibility expansion)**
- Overall incident KS: **2.35 per 1,000 person-years** (95% CI 2.01–2.74) (Akanbi et al., published Sep 2023) (akanbi2023incidentkaposisarcoma pages 2-4).
- Incidence declined from **2.53** to **1.58** per 1,000 PY comparing 2006–2009 vs 2010–2016 (akanbi2023incidentkaposisarcoma pages 2-4).
- ART use strongly reduced risk (**adjusted HR ~0.17**) and male sex increased risk (**HR ~1.64**) (akanbi2023incidentkaposisarcoma pages 6-7).

### 9.2 Population demographics
- Mixed-subtype cohort (Italy): strong male predominance (**89.53%**) (russo2024kaposi’ssarcomaevaluation pages 1-2).
- Kidney transplant meta-analysis: male predominance (**OR 2.36**) (saowapa2024evaluatingkaposisarcoma pages 1-2).

---

## 10. Diagnostics

### 10.1 Clinical and pathology diagnosis (gold standards)
- Diagnosis relies on **biopsy** with histopathology and immunohistochemistry (russo2024kaposi’ssarcomaevaluation pages 1-2).
- A 2023 clinical management review emphasizes **skin biopsy** showing spindle cells and **KSHV LANA immunohistochemistry** positivity as a diagnostic standard; GI lesions should be biopsied during endoscopy, and bronchoscopy is used to evaluate suspected pulmonary KS (biopsy often avoided due to bleeding risk) (patel2023clinicalmanagementof pages 2-4).

### 10.2 Virologic testing
- A contemporary review reports strong performance of LANA IHC and highlights PCR-based detection; it reports that LANA-1 positivity was “**100% (50/50)** of KS cases being positive and all other non-KS lesions being negative” in one cited series (Bagratee et al., 2025) (bagratee2025recentadvancesin pages 4-6).

### 10.3 Imaging
- FDG-PET/CT can help define extent of disease in some contexts (patel2023clinicalmanagementof pages 2-4).

### 10.4 Differential diagnosis
- KS has histopathologic mimics (e.g., angiosarcoma, hemangioma/vascular lesions, pyogenic granuloma) emphasized in the contemporary diagnostic review (bagratee2025recentadvancesin pages 4-6).

---

## 11. Outcomes / Prognosis

### 11.1 Real-world outcomes (retrospective cohort; 1993–2022)
- In the 86-patient cohort, “A persistent response was observed in approximately **65%** of patients, with a **22% relapse rate** (at least 2 years). The overall survival ranges from **90 to 70%** at 2 to 10 years after the diagnosis. Iatrogenic KS demonstrated a higher mortality (**52.9%**).” (Russo et al., 2024 abstract) (russo2024kaposi’ssarcomaevaluation pages 1-2).

### 11.2 Early mortality in disseminated HIV-KS with IRIS risk
- Severe IRIS-KS is described as high mortality (reported 25–40% in background) and pulmonary involvement is particularly high-risk (volkow2023impactofvalganciclovir pages 1-2).

---

## 12. Treatment

### 12.1 Treatment principles by subtype (current practice)
- **Epidemic/HIV-associated KS**: ART is foundational; systemic therapy and local therapy used per extent, with careful evaluation of visceral disease (patel2023clinicalmanagementof pages 2-4, akanbi2023incidentkaposisarcoma pages 2-4).
- **Iatrogenic/post-transplant KS**: reduction/withdrawal of immunosuppression and regimen modification (e.g., mTOR inhibitor conversion is discussed in transplant-focused literature; within retrieved evidence, immunosuppression reduction is the key described strategy) (saowapa2024evaluatingkaposisarcoma pages 1-2).
- **Classic KS**: local therapy for limited disease; systemic chemotherapy and emerging immunotherapies/targeted strategies for advanced disease; evidence base is more limited than in HIV-KS (denaro2024managementandfuture pages 1-2).

### 12.2 Systemic chemotherapy
- Reviews summarize cytotoxic regimens (anthracyclines, vinca alkaloids, paclitaxel), with reported response rates often in the **70–90%** range but frequently transient in classic KS (denaro2024managementandfuture pages 2-5).

### 12.3 Antiviral/virus-targeted strategies (recent clinical trial evidence)
**Valganciclovir in disseminated KS to mitigate severe IRIS-KS (PLOS ONE, May 2023)**
- Trial design: valganciclovir **900 mg BID** for four weeks before cART and continued to week 48 vs cART initiation alone (volkow2023impactofvalganciclovir pages 1-2).
- Key outcomes (direct abstract numbers): severe-IRIS-KS attributable mortality **0/20** vs **3/20** (p=0.09); pulmonary KS mortality **0/5** vs **3/4** (P=0.048); among survivors at week 48, **82%** achieved **>80% remission** (volkow2023impactofvalganciclovir pages 1-2).

### 12.4 Repurposed/adjunct antiretroviral class drugs in classic KS (phase II, 2024)
- Indinavir + chemotherapy strategy in advanced classic KS (Cancer Research Communications; Aug 2024): **22/22** evaluable patients responded to debulking chemotherapy; **16** entered indinavir maintenance; overall response rate **75%** with estimated median response duration **43 months** (sgadari2024clinicalefficacyof pages 1-2).

### 12.5 Post-transplant KS management outcomes (meta-analysis)
- In kidney transplant recipients, reduction/withdrawal of immunosuppression alone resulted in **47.8% complete remissions** across included studies (Saowapa et al., Jan 2024) (saowapa2024evaluatingkaposisarcoma pages 1-2).

### 12.6 Immunotherapy and emerging strategies
- Contemporary expert review notes “new therapies… focus on chemotherapy-sparing options that seek to target the underlying viral pathogenesis or immunotherapy strategies” (Patel et al., 2023) (patel2023clinicalmanagementof pages 2-4).
- Clinical trials registered on ClinicalTrials.gov in the current tool state include checkpoint inhibitor strategies (e.g., intralesional nivolumab NCT03316274; pembrolizumab phase II in classic/endemic KS NCT03469804; etc.), but trial outcomes were not retrieved here because only trial registry metadata (not results) were available.

### 12.7 Treatment ontology (MAXO suggestions)
- **Antiretroviral therapy** (MAXO: *antiretroviral therapy*; proposed) (akanbi2023incidentkaposisarcoma pages 2-4).
- **Reduction/withdrawal of immunosuppression** (MAXO: *immunosuppressive therapy adjustment*) (saowapa2024evaluatingkaposisarcoma pages 1-2).
- **Systemic chemotherapy** (MAXO: *chemotherapy*) (denaro2024managementandfuture pages 2-5).
- **Antiviral therapy (valganciclovir)** (MAXO: *antiviral therapy*) (volkow2023impactofvalganciclovir pages 1-2).

### 12.8 Treatment algorithm (visual evidence)
The Denaro 2024 evidence-based review includes a systemic therapy management table (Table 6), serving as a practical algorithm for systemic treatment lines/dosing in classic KS.

(denaro2024managementandfuture media 1e1c9584)

---

## 13. Prevention

### 13.1 Primary prevention
- No licensed KSHV vaccine is referenced in the retrieved evidence.

### 13.2 Secondary prevention (early HIV diagnosis and ART initiation)
- In Nigeria, ART eligibility expansion was associated with reduced incident KS, likely through earlier care/ART initiation (akanbi2023incidentkaposisarcoma pages 1-2, akanbi2023incidentkaposisarcoma pages 2-4).
- A US registry analysis contextualizes ART introduction (1996) with subsequent declines in KS incidence and improved survival, while noting persistent disparities (raja2025kaposisarcomaincidence pages 1-2).

### 13.3 Tertiary prevention (preventing complications/relapse)
- In transplant-associated KS, balancing immunosuppression reduction with graft function is emphasized, with immunosuppression reduction producing remissions in many cases (saowapa2024evaluatingkaposisarcoma pages 1-2).

---

## 14. Other Species / Natural Disease
No veterinary/natural disease evidence was retrieved in the current tool context; this section is therefore **not populated** from evidence and should be revisited with targeted veterinary literature searches.

---

## 15. Model Organisms

### 15.1 Patient-derived xenografts (2024)
- A 2024 KS PDX platform supports mechanistic and therapeutic investigations, including spatial transcriptomics readouts and tumor microenvironment signaling (e.g., CXCL12→CXCR4) (li2024mappingherpesvirusdrivenimpacts pages 5-9, li2024mappingherpesvirusdrivenimpacts pages 1-5).
- This addresses a known limitation: rapid loss of KSHV infection when KS tumor cells are explanted into culture (li2024mappingherpesvirusdrivenimpacts pages 1-5).

---

## Consolidated subtype and statistics summary
| Subtype | Etiology/context | Common sites | Key quantitative notes | Key citations |
|---|---|---|---|---|
| Classic KS | HHV-8/KSHV-associated; typically older men of Mediterranean/Jewish origin; generally indolent | Predominantly lower extremity skin; GI tract and lung are the most common metastatic/visceral sites when present | Median age ~70 years; visceral involvement reported in **<10%**; systemic chemotherapy responses often **70–90%** but usually transient (denaro2024managementandfuture pages 2-5, denaro2024managementandfuture pages 1-2) | (denaro2024managementandfuture pages 2-5, denaro2024managementandfuture pages 1-2) |
| Epidemic/HIV-associated KS | HHV-8/KSHV plus HIV-related immunosuppression; more aggressive than classic KS | Skin, mucosa, lymph nodes, GI tract, respiratory tract | Historical 5-year OS about **12%** pre-ART; with effective ART, survival improved to **68–95%** (denaro2024managementandfuture pages 2-5). In a Nigerian HIV cohort, incidence declined from **2.53 to 1.58 per 1,000 person-years** after ART eligibility expansion; ART use associated with markedly lower KS risk (**adjusted HR ~0.17**), while male sex increased risk (**HR ~1.64**) (akanbi2023incidentkaposisarcoma pages 6-7, akanbi2023incidentkaposisarcoma pages 2-4) | (denaro2024managementandfuture pages 2-5, akanbi2023incidentkaposisarcoma pages 6-7, akanbi2023incidentkaposisarcoma pages 2-4) |
| Endemic/African KS | HHV-8/KSHV in sub-Saharan Africa; affects adults and children; pediatric disease can be aggressive/lymphadenopathic | Skin, lymph nodes; may have visceral disease; pediatric nodal disease notable | Childhood median age reported **4–9 years**; some series/reviews report aggressive exophytic disease with **bony invasion 31%** and **lymphedema 17%** (denaro2024managementandfuture pages 2-5, bagratee2025recentadvancesin pages 4-6) | (denaro2024managementandfuture pages 2-5, bagratee2025recentadvancesin pages 4-6) |
| Iatrogenic/transplant-associated KS | HHV-8/KSHV with prolonged immunosuppression, especially after solid-organ transplantation or corticosteroid exposure | Cutaneous lesions common; visceral and nodal involvement may occur, sometimes without skin lesions | Transplant recipients have about **60-fold increased risk** of KS (denaro2024managementandfuture pages 2-5). Kidney transplant meta-analysis: pooled prevalence **1.5%** overall; **1.7%** in African and Middle Eastern recipients vs **0.07%** in Western recipients; male predominance **OR 2.36**; cyclosporine-based immunosuppression in **79.6%** of KS cases; reduction/withdrawal of immunosuppression alone achieved **47.8% complete remissions** (saowapa2024evaluatingkaposisarcoma pages 1-2). In a retrospective cohort, iatrogenic KS mortality reached **52.9%** (russo2024kaposi’ssarcomaevaluation pages 1-2) | (denaro2024managementandfuture pages 2-5, russo2024kaposi’ssarcomaevaluation pages 1-2, saowapa2024evaluatingkaposisarcoma pages 1-2) |
| HIV-negative MSM-associated KS | Proposed fifth subtype; HHV-8/KSHV without HIV infection; usually milder than epidemic KS | Often localized cutaneous and/or mucosal disease | Recognized as a distinct but less well-characterized subtype in recent reviews; robust epidemiologic estimates remain limited (denaro2024managementandfuture pages 2-5, patel2023clinicalmanagementof pages 2-4) | (denaro2024managementandfuture pages 2-5, patel2023clinicalmanagementof pages 2-4) |
| KS overall clinical presentation | Angioproliferative/vascular endothelial tumor driven by HHV-8/KSHV, often requiring immunosuppression or immune dysregulation as cofactor | Skin most common; oral cavity/mucosa, lymph nodes, GI tract, lungs/airways also involved | In a single-center cohort of **86** KS patients, **89.53%** were male, **43.02%** had classic KS, and **77.9%** had cutaneous involvement; **61.63%** had single-site disease and **51.16%** had lower-limb involvement (russo2024kaposi’ssarcomaevaluation pages 1-2, russo2024kaposi’ssarcomaevaluation pages 2-4) | (russo2024kaposi’ssarcomaevaluation pages 1-2, russo2024kaposi’ssarcomaevaluation pages 2-4) |
| Real-world outcomes across mixed KS cohort | Multidisciplinary management using surgery, ART, chemotherapy, radiotherapy, or combinations | Depends on subtype and extent; skin predominant overall | In the 86-patient cohort, persistent response occurred in about **65%**, relapse in **22%** (≥2 years), and overall survival ranged from **90% to 70%** at **2 to 10 years** after diagnosis (russo2024kaposi’ssarcomaevaluation pages 1-2) | (russo2024kaposi’ssarcomaevaluation pages 1-2) |
| United States epidemiology (all KS) | Population-level burden reflects ART-era declines but persistent disparities | Not site-specific; registry analysis of all KS | From **1999–2020**, there were **27,886 KS cases** and **4,380 deaths**. Overall AAIR: **0.99** in men vs **0.10** in women; AAMR: **0.16** vs **0.01**. Black men had the highest AAIR/AAMR (**2.23/0.40**) vs White men (**0.79/0.13**). Incidence declined **46.7%** in men and **58.9%** in women; male mortality declined **66.4%** (raja2025kaposisarcomaincidence pages 1-2) | (raja2025kaposisarcomaincidence pages 1-2) |
| Disseminated HIV-KS with IRIS risk | Advanced HIV-associated KS starting cART; high HHV-8 viral load linked to severe IRIS-KS | Disseminated disease defined by pulmonary, lymph-node, GI involvement, lymphedema, or ≥30 skin lesions | In an RCT of valganciclovir before/with cART, severe-IRIS-KS attributable mortality was **0/20** vs **3/20** in controls; in pulmonary KS, mortality was **0/5** vs **3/4**; among survivors at week 48, **82%** achieved **>80% remission** (volkow2023impactofvalganciclovir pages 1-2) | (volkow2023impactofvalganciclovir pages 1-2) |
| Advanced classic KS trial | Elderly patients with progressive/advanced classic KS treated with debulking chemotherapy followed by indinavir maintenance | Primarily cutaneous disease burden requiring systemic control | In a phase II trial, **22/22** evaluable patients responded to debulking chemotherapy; **16** entered indinavir maintenance; overall response rate at end of maintenance was **75%** with estimated median response duration **43 months** (sgadari2024clinicalefficacyof pages 1-2) | (sgadari2024clinicalefficacyof pages 1-2) |
| Experimental model systems (KS PDX) | Patient-derived xenografts from cutaneous KS biopsies in immunodeficient mice; useful for mechanistic and translational studies | Orthotopic cutaneous KS xenografts retaining infected endothelial/spindle-cell populations | Tumors were maintained in **27/28** PDXs (up to **272 days**); LANA+ endothelial cell density increased a mean **4.3-fold**; LANA+ cells increased from **15% to 62%**; dual LANA+/Ki-67+ cells increased from **1% to 5.6%** (li2024mappingherpesvirusdrivenimpacts pages 5-9, li2024mappingherpesvirusdrivenimpacts pages 1-5) | (li2024mappingherpesvirusdrivenimpacts pages 5-9, li2024mappingherpesvirusdrivenimpacts pages 1-5) |


*Table: This table summarizes Kaposi sarcoma subtypes, risk contexts, anatomic patterns, and key quantitative epidemiology, treatment, and model-system findings extracted from the gathered evidence. It is useful as a compact evidence map for subtype-specific disease characterization and recent outcome statistics.*

---

## Key “expert opinion” perspectives (authoritative reviews)
- KS and other KSHV-associated diseases are “often underdiagnosed… in the United States and worldwide,” and emerging therapies aim to target viral pathogenesis or employ immunotherapy approaches (Patel et al., 2023, Expert Review of Anti-infective Therapy) (patel2023clinicalmanagementof pages 2-4).
- For classic KS specifically, Denaro et al. (2024) emphasize limited high-quality evidence and the importance of multidisciplinary referral centers and clinical trial enrollment (denaro2024managementandfuture pages 1-2).

---

## Evidence limitations and gaps (for knowledge base completion)
- This tool run did not retrieve **MeSH**, **Orphanet**, **OMIM**, or a definitive **MONDO ID for Kaposi sarcoma** (as distinct from “susceptibility to”), nor did it retrieve a standardized list of HPO terms with validated frequencies.
- Checkpoint inhibitor efficacy in KS was not populated with outcome data here because results papers were not retrieved (only trial registry entries).
- Additional targeted searches (e.g., NCCN guideline text, WHO/ICD-11, MeSH Browser, MONDO release files, and key KS immunotherapy trial publications) would be needed for a fully populated ontology-first knowledge base entry.


References

1. (russo2024kaposi’ssarcomaevaluation pages 1-2): Irene Russo, Dario Marino, Claudia Cozzolino, Paolo Del Fiore, Fitnete Nerjaku, Silvia Finotto, Annamaria Cattelan, Maria Luisa Calabrò, Anna Belloni Fortina, Francesco Russano, Marcodomenico Mazza, Sara Galuppo, Elisabetta Bezzon, Marta Sbaraglia, Marco Krengli, Antonella Brunello, Simone Mocellin, Stefano Piaserico, and Mauro Alaibac. Kaposi’s sarcoma: evaluation of clinical features, treatment outcomes, and prognosis in a single-center retrospective case series. Cancers, 16:691, Feb 2024. URL: https://doi.org/10.3390/cancers16040691, doi:10.3390/cancers16040691. This article has 19 citations.

2. (denaro2024managementandfuture pages 1-2): Nerina Denaro, Alice Indini, Lucia Brambilla, Angelo Valerio Marzano, Ornella Garrone, and Athanasia Tourlaki. Management and future therapeutic perspectives of classic kaposi’s sarcoma: an evidence-based review. OncoTargets and Therapy, 17:961-976, Nov 2024. URL: https://doi.org/10.2147/ott.s468787, doi:10.2147/ott.s468787. This article has 8 citations.

3. (raja2025kaposisarcomaincidence pages 1-2): Ahsan Raza Raja, Philippos Apolinario Costa, and Muhammad Hyder Junejo. Kaposi sarcoma incidence and mortality trends and disparities in the united states. Infectious Agents and Cancer, Nov 2025. URL: https://doi.org/10.1186/s13027-025-00710-x, doi:10.1186/s13027-025-00710-x. This article has 1 citations and is from a peer-reviewed journal.

4. (OpenTargets Search: Kaposi sarcoma): Open Targets Query (Kaposi sarcoma, 11 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (patel2023clinicalmanagementof pages 2-4): Roshani Patel, Kathryn Lurain, Robert Yarchoan, and Ramya Ramaswami. Clinical management of kaposi sarcoma herpesvirus-associated diseases: an update on disease manifestations and treatment strategies. Expert Review of Anti-infective Therapy, 21:929-941, Aug 2023. URL: https://doi.org/10.1080/14787210.2023.2247161, doi:10.1080/14787210.2023.2247161. This article has 38 citations and is from a peer-reviewed journal.

6. (volkow2023impactofvalganciclovir pages 1-2): Patricia Volkow, Leslie Chavez Galan, Lucero Ramon-Luing, Judith Cruz-Velazquez, Patricia Cornejo-Juarez, Isabel Sada-Ovalle, Rogelio Perez-Padilla, and Beda Islas-Muñoz. Impact of valganciclovir therapy on severe iris-kaposi sarcoma mortality: an open-label, parallel, randomized controlled trial. PLOS ONE, 18:e0280209, May 2023. URL: https://doi.org/10.1371/journal.pone.0280209, doi:10.1371/journal.pone.0280209. This article has 11 citations and is from a peer-reviewed journal.

7. (akanbi2023incidentkaposisarcoma pages 2-4): Maxwell. O. Akanbi, Lucy. A. Bilaver, Chad Achenbach, Lisa. R. Hirschhorn, Adovich. S. Rivera, Orimisan. S. Adekolujo, Kehinde. U. A. Adekola, Olugbenga. A. Silas, Patricia. A. Agaba, Oche Agbaji, Nathan. Y. Shehu, Solomon. A. Sagay, Lifang Hou, and Robert. L. Murphy. Incident kaposi sarcoma during the expansion of antiretroviral therapy eligibility in nigeria: a retrospective cohort study. BMC Cancer, Sep 2023. URL: https://doi.org/10.1186/s12885-023-11402-3, doi:10.1186/s12885-023-11402-3. This article has 3 citations and is from a peer-reviewed journal.

8. (denaro2024managementandfuture pages 2-5): Nerina Denaro, Alice Indini, Lucia Brambilla, Angelo Valerio Marzano, Ornella Garrone, and Athanasia Tourlaki. Management and future therapeutic perspectives of classic kaposi’s sarcoma: an evidence-based review. OncoTargets and Therapy, 17:961-976, Nov 2024. URL: https://doi.org/10.2147/ott.s468787, doi:10.2147/ott.s468787. This article has 8 citations.

9. (bagratee2025recentadvancesin pages 4-6): Tayarv Jayd Bagratee, Veron Ramsuran, Mpumelelo Msimang, and Pratistadevi Kanaye Ramdial. Recent advances in the histopathology, molecular biology, and treatment of kaposi sarcoma: a contemporary review. International Journal of Molecular Sciences, 26:10058, Oct 2025. URL: https://doi.org/10.3390/ijms262010058, doi:10.3390/ijms262010058. This article has 2 citations.

10. (saowapa2024evaluatingkaposisarcoma pages 1-2): Sakditad Saowapa, Natchaya Polpichai, Pharit Siladech, Chalothorn Wannaphut, Manasawee Tanariyakul, Phuuwadith Wattanachayakul, and Pakin Lalitnithi. Evaluating kaposi sarcoma in kidney transplant patients: a systematic review and meta-analysis. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.52527, doi:10.7759/cureus.52527. This article has 20 citations.

11. (russo2024kaposi’ssarcomaevaluation pages 2-4): Irene Russo, Dario Marino, Claudia Cozzolino, Paolo Del Fiore, Fitnete Nerjaku, Silvia Finotto, Annamaria Cattelan, Maria Luisa Calabrò, Anna Belloni Fortina, Francesco Russano, Marcodomenico Mazza, Sara Galuppo, Elisabetta Bezzon, Marta Sbaraglia, Marco Krengli, Antonella Brunello, Simone Mocellin, Stefano Piaserico, and Mauro Alaibac. Kaposi’s sarcoma: evaluation of clinical features, treatment outcomes, and prognosis in a single-center retrospective case series. Cancers, 16:691, Feb 2024. URL: https://doi.org/10.3390/cancers16040691, doi:10.3390/cancers16040691. This article has 19 citations.

12. (revenko2026classickaposisarcoma pages 1-2): Daniela Revenko, Natali Shirron, Reut Shainer, Emily Avitan-Hersh, and Alona Zer. Classic kaposi sarcoma: current treatment strategies and emerging therapeutic approaches. Cancers, 18:1008, Mar 2026. URL: https://doi.org/10.3390/cancers18061008, doi:10.3390/cancers18061008. This article has 0 citations.

13. (li2024mappingherpesvirusdrivenimpacts pages 5-9): Xiaofan Li, Zoë Weaver Ohler, Amanda Day, Laura Bassel, Anna Grosskopf, Bahman Afsari, Takanobu Tagawa, Wendi Custer, Ralph Mangusan, Kathryn Lurain, Robert Yarchoan, Joseph Ziegelbauer, Ramya Ramaswami, and Laurie T. Krug. Mapping herpesvirus-driven impacts on the cellular milieu and transcriptional profile of kaposi sarcoma in patient-derived mouse models. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.27.615429, doi:10.1101/2024.09.27.615429. This article has 5 citations.

14. (li2024mappingherpesvirusdrivenimpacts pages 1-5): Xiaofan Li, Zoë Weaver Ohler, Amanda Day, Laura Bassel, Anna Grosskopf, Bahman Afsari, Takanobu Tagawa, Wendi Custer, Ralph Mangusan, Kathryn Lurain, Robert Yarchoan, Joseph Ziegelbauer, Ramya Ramaswami, and Laurie T. Krug. Mapping herpesvirus-driven impacts on the cellular milieu and transcriptional profile of kaposi sarcoma in patient-derived mouse models. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.27.615429, doi:10.1101/2024.09.27.615429. This article has 5 citations.

15. (denaro2024managementandfuture media 1e1c9584): Nerina Denaro, Alice Indini, Lucia Brambilla, Angelo Valerio Marzano, Ornella Garrone, and Athanasia Tourlaki. Management and future therapeutic perspectives of classic kaposi’s sarcoma: an evidence-based review. OncoTargets and Therapy, 17:961-976, Nov 2024. URL: https://doi.org/10.2147/ott.s468787, doi:10.2147/ott.s468787. This article has 8 citations.

16. (akanbi2023incidentkaposisarcoma pages 6-7): Maxwell. O. Akanbi, Lucy. A. Bilaver, Chad Achenbach, Lisa. R. Hirschhorn, Adovich. S. Rivera, Orimisan. S. Adekolujo, Kehinde. U. A. Adekola, Olugbenga. A. Silas, Patricia. A. Agaba, Oche Agbaji, Nathan. Y. Shehu, Solomon. A. Sagay, Lifang Hou, and Robert. L. Murphy. Incident kaposi sarcoma during the expansion of antiretroviral therapy eligibility in nigeria: a retrospective cohort study. BMC Cancer, Sep 2023. URL: https://doi.org/10.1186/s12885-023-11402-3, doi:10.1186/s12885-023-11402-3. This article has 3 citations and is from a peer-reviewed journal.

17. (sgadari2024clinicalefficacyof pages 1-2): Cecilia Sgadari, Biancamaria Scoppio, Orietta Picconi, Antonella Tripiciano, Francesca Maria Gaiani, Vittorio Francavilla, Angela Arancio, Massimo Campagna, Clelia Palladino, Sonia Moretti, Paolo Monini, Lucia Brambilla, and Barbara Ensoli. Clinical efficacy of the hiv protease inhibitor indinavir in combination with chemotherapy for advanced classic kaposi sarcoma treatment: a single-arm, phase ii trial in the elderly. Cancer Research Communications, 4:2112-2122, Aug 2024. URL: https://doi.org/10.1158/2767-9764.crc-24-0102, doi:10.1158/2767-9764.crc-24-0102. This article has 5 citations and is from a peer-reviewed journal.

18. (akanbi2023incidentkaposisarcoma pages 1-2): Maxwell. O. Akanbi, Lucy. A. Bilaver, Chad Achenbach, Lisa. R. Hirschhorn, Adovich. S. Rivera, Orimisan. S. Adekolujo, Kehinde. U. A. Adekola, Olugbenga. A. Silas, Patricia. A. Agaba, Oche Agbaji, Nathan. Y. Shehu, Solomon. A. Sagay, Lifang Hou, and Robert. L. Murphy. Incident kaposi sarcoma during the expansion of antiretroviral therapy eligibility in nigeria: a retrospective cohort study. BMC Cancer, Sep 2023. URL: https://doi.org/10.1186/s12885-023-11402-3, doi:10.1186/s12885-023-11402-3. This article has 3 citations and is from a peer-reviewed journal.
