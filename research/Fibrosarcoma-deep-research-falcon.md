---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T15:01:09.022904'
end_time: '2026-05-07T15:18:43.534133'
duration_seconds: 1054.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fibrosarcoma
  mondo_id: ''
  category: Cancer
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
- **Disease Name:** Fibrosarcoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Fibrosarcoma** covering all of the
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
- **Disease Name:** Fibrosarcoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Fibrosarcoma** covering all of the
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


# Fibrosarcoma — Disease Characteristics Research Report (Cancer)

## Executive summary
Fibrosarcoma is a malignant mesenchymal (fibroblastic) tumor diagnosis that, in contemporary practice, is best understood as a **family of entities and mimics** spanning classic “adult-type” fibrosarcoma patterns, **congenital/infantile fibrosarcoma (CFS/IFS)**, and related fusion-defined fibroblastic/spindle-cell neoplasms (including sclerosing epithelioid fibrosarcoma and low-grade fibromyxoid sarcoma). A major recent trend is the use of **fusion genes (notably NTRK fusions)** to improve classification, diagnostics, and targeted therapy selection—particularly in IFS, where TRK inhibitors have shown high response rates and are now implemented in real-world pediatric oncology. (tang2023progressiveinsightsinto pages 3-6, tang2023progressiveinsightsinto pages 12-13)

## 1. Disease information
### 1.1 Definition and overview
* **Infantile fibrosarcoma (IFS)**: a rare pediatric malignant spindle-cell soft-tissue sarcoma of mesenchymal origin, typically presenting as a **single localized painless mass** that **grows rapidly** but often has a **relatively indolent biological behavior** and **favorable prognosis** compared with many adult sarcomas. (wang2023larotrectinibtreatmentfor pages 1-2, li2024characterizationofthe pages 1-2)
* In IFS, the disease is frequently described as **molecularly defined by NTRK fusion proteins**, most commonly **ETV6::NTRK3**. (wang2023larotrectinibtreatmentfor pages 1-2, suurmeijer2024kinasefusionpositive pages 1-3)

### 1.2 Key identifiers (available from retrieved evidence)
* **MONDO** (from Open Targets evidence context):
  * adult fibrosarcoma: **MONDO_0002676** (OpenTargets Search: Fibrosarcoma,Infantile fibrosarcoma-NTRK3,NTRK1,NTRK2)
  * pediatric fibrosarcoma: **MONDO_0002678** (OpenTargets Search: Fibrosarcoma,Infantile fibrosarcoma-NTRK3,NTRK1,NTRK2)
  * congenital fibrosarcoma: **MONDO_0004557** (OpenTargets Search: Fibrosarcoma,Infantile fibrosarcoma-NTRK3,NTRK1,NTRK2)
* **EFO**: “fibrosarcoma” **EFO_0002087** (OpenTargets Search: Fibrosarcoma,Infantile fibrosarcoma-NTRK3,NTRK1,NTRK2)

**Note:** Direct retrieval of **MeSH**, **ICD-10/ICD-11**, **Orphanet**, and **OMIM** identifiers for fibrosarcoma was not available in the current tool context/evidence set; these should be populated from ontology sources (e.g., MeSH Browser, ICD-11, Orphanet, OMIM) during downstream curation.

### 1.3 Synonyms and alternative names (from retrieved evidence)
* **Congenital fibrosarcoma / congenital fibrosarcoma (CFS)** and **infantile fibrosarcoma (IFS)** are used closely and discussed together in recent reviews. (tang2023progressiveinsightsinto pages 3-6, tang2023progressiveinsightsinto pages 12-13)
* Some recent pathology literature describes **IFS-like** tumors and **adult fibrosarcoma-like** patterns within broader kinase fusion–positive spindle-cell tumor spectra (especially in bone). (suurmeijer2024kinasefusionpositive pages 1-3)

### 1.4 Evidence provenance
The information in this report is derived from **aggregated disease-level resources and peer-reviewed literature** (reviews, clinical studies/case series, and clinical trial registry entries) rather than individual EHR records, except where case reports are explicitly discussed. (wang2023larotrectinibtreatmentfor pages 1-2, sahni2023limbsalvageof pages 5-7, NCT03834961 chunk 1)

## 2. Etiology
### 2.1 Primary causal factors
**Molecular (fusion-driven) oncogenesis** is central in many fibrosarcoma-related entities:
* In IFS, **t(12;15)(p13;q25)** leading to **ETV6::NTRK3** is strongly associated with tumorigenesis and provides a direct drug target. (wang2023larotrectinibtreatmentfor pages 1-2)
* Reviews emphasize that **fusion genes** are prevalent drivers across fibrosarcoma subtypes and are increasingly leveraged for subcategorization and targeted treatment. (tang2023progressiveinsightsinto pages 3-6)

### 2.2 Risk factors
Robust, population-level risk factor data specific to fibrosarcoma was not captured in the current evidence set. For IFS specifically, disease onset is predominantly in infancy (often congenital presentation), implying **developmental/embryonal** rather than lifestyle-driven risk in many cases. (wang2023larotrectinibtreatmentfor pages 1-2)

### 2.3 Protective factors / gene–environment interactions
No high-confidence protective factors or gene–environment interaction evidence specific to fibrosarcoma was retrieved in the current evidence set.

## 3. Phenotypes
### 3.1 Core clinical phenotypes (IFS emphasized due to strong evidence base)
* **Localized painless soft-tissue mass** (symptom/sign): typical in IFS; often rapidly enlarging. (wang2023larotrectinibtreatmentfor pages 1-2)
* **Congenital presentation**: ~**40%** of IFS may be present at birth (as summarized in a 2023 case report/review). (wang2023larotrectinibtreatmentfor pages 1-2)

Suggested HPO terms (mapping for KB curation; not all were explicitly coded in the evidence text):
* Localized mass: **HP:0002664 (Tumor)** / **HP:0100242 (Soft tissue mass)**
* Pain absent: **HP:0030199 (Painless)** (conceptual)
* Rapid growth: **HP:0003676 (Rapidly progressive)** (conceptual)

### 3.2 Laboratory/immunophenotype-related phenotypes
IFS lacks a unique IHC marker; reported IHC patterns include:
* Frequent **vimentin positivity** and often **desmin/S100 negativity**, with lack of a specific immunohistochemical tumor marker overall. (li2024characterizationofthe pages 1-2)

## 4. Genetic / molecular information
### 4.1 Causal genes and recurrent alterations
Key genes strongly implicated via recurrent fusions:
* **NTRK3** (ETV6::NTRK3) in IFS/CFS; a central oncogenic driver and therapeutic target. (wang2023larotrectinibtreatmentfor pages 1-2, OpenTargets Search: Fibrosarcoma,Infantile fibrosarcoma-NTRK3,NTRK1,NTRK2)
* Broader kinase-fusion spectra include **NTRK1, NTRK3, RET, BRAF, RAF1** across spindle-cell tumors with fibrosarcoma-like morphologies (including IFS-like and adult FS-like). (suurmeijer2024kinasefusionpositive pages 1-3)

Hallmark fusion summary (including DFSP, LGFMS/SEF context from a 2023 review):
| Entity/subtype | Key fusion/alteration | Evidence/frequency | Typical age group | Clinical utility (diagnostic/therapeutic) | Key source (DOI URL) and year |
|---|---|---|---|---|---|
| Congenital/infantile fibrosarcoma (CFS/IFS) | **ETV6::NTRK3** from t(12;15)(p13;q25) | Reported in **~85%** of IFS cases; canonical defining lesion (wang2023larotrectinibtreatmentfor pages 1-2, li2024characterizationofthe pages 1-2) | Predominantly infants; most common soft-tissue sarcoma in children **<1 year** (wang2023larotrectinibtreatmentfor pages 1-2, li2024characterizationofthe pages 1-2) | Strong **diagnostic marker**; supports **TRK inhibitor** use such as larotrectinib in fusion-positive disease (wang2023larotrectinibtreatmentfor pages 1-2, sahni2023limbsalvageof pages 5-7) | Wang et al., Front Oncol, 2023, https://doi.org/10.3389/fonc.2023.1206833 |
| Congenital/infantile fibrosarcoma (variant fusions) | **EML4::NTRK3**, **LMNA::NTRK1**, **PHIP::BRAF** | Reported as additional/non-canonical fusions in CFS/IFS; Tang 2023 cites case-level responses including near-complete response to crizotinib in **LMNA::NTRK1** and proposed trametinib relevance for **PHIP::BRAF** (tang2023progressiveinsightsinto pages 3-6, tang2023progressiveinsightsinto pages 12-13) | Infants/young children (tang2023progressiveinsightsinto pages 3-6) | Helps refine diagnosis in ETV6-negative cases; suggests **targeted therapy** options matched to kinase alteration (tang2023progressiveinsightsinto pages 3-6, tang2023progressiveinsightsinto pages 12-13) | Tang et al., Front Cell Dev Biol, 2023, https://doi.org/10.3389/fcell.2023.1284428 |
| Dermatofibrosarcoma protuberans (DFSP) | **COL1A1::PDGFB** | Identified in **172 cases (91.4%)**; described as recurrent/classic DFSP fusion (tang2023progressiveinsightsinto pages 3-6) | Not specified in provided snippet | High-value **diagnostic marker**; PDGFB-axis relevance for molecular classification and targeted approaches (tang2023progressiveinsightsinto pages 3-6) | Tang et al., Front Cell Dev Biol, 2023, https://doi.org/10.3389/fcell.2023.1284428 |
| DFSP (alternative fusions) | **COL1A2::PDGFB**, **COL6A3::PDGFD**, **EMILIN2::PDGFD**, **SLC2A5::BTBD7** | RNA-seq has uncovered alternative fusions beyond COL1A1::PDGFB (tang2023progressiveinsightsinto pages 3-6) | Not specified in provided snippet | Expands **molecular diagnosis**, especially for atypical/classic-fusion-negative DFSP (tang2023progressiveinsightsinto pages 3-6) | Tang et al., Front Cell Dev Biol, 2023, https://doi.org/10.3389/fcell.2023.1284428 |
| Kinase fusion–positive spindle cell tumors (bone/soft tissue spectrum; IFS-like, adult FS-like, MPNST-like, LPFNT-like, myxoma-like) | **NTRK3, NTRK1, RET, BRAF, RAF1** fusions | Combined literature series: **NTRK3 n=6, NTRK1 n=4, RET n=2, BRAF n=2, RAF1 n=1**; **73%** occurred in patients **<30 years**; NTRK3 associated with high-grade morphology in **5/6** and NTRK1 with lower grade in **3/4** (suurmeijer2024kinasefusionpositive pages 1-3) | Mostly children and young adults; some older adults reported (suurmeijer2024kinasefusionpositive pages 1-3) | Fusion status aids **classification**, supports **pan-TRK IHC**/RNA sequencing workup, and identifies actionable kinase targets (suurmeijer2024kinasefusionpositive pages 1-3) | Suurmeijer et al., Genes Chromosomes Cancer, 2024, https://doi.org/10.1002/gcc.23205 |
| Low-grade fibromyxoid sarcoma (LGFMS) | **FUS::BBF2H7** (as reported in Tang 2023) | Listed by Tang 2023 as a key recurrent fusion in LGFMS (tang2023progressiveinsightsinto pages 12-13, tang2023progressiveinsightsinto media b1dcbf19) | Not specified in provided snippet | Important **diagnostic** fusion for subtype assignment (tang2023progressiveinsightsinto pages 12-13) | Tang et al., Front Cell Dev Biol, 2023, https://doi.org/10.3389/fcell.2023.1284428 |
| Sclerosing epithelioid fibrosarcoma (SEF) | **FUS rearrangements rare in pure SEF** | Tang 2023 notes **FUS rearrangements are rare in pure SEF**; SEF also described as aggressive (tang2023progressiveinsightsinto pages 12-13) | Not specified in provided snippet | Molecular findings may help with **differential diagnosis**, but rarity limits routine fusion-based definition from provided evidence (tang2023progressiveinsightsinto pages 12-13) | Tang et al., Front Cell Dev Biol, 2023, https://doi.org/10.3389/fcell.2023.1284428 |
| Fibrosarcoma-related entities overview table | Multiple subtype-defining fusions summarized in a single review table | Tang 2023 Table 1 summarizes DFSP, CFS/IFS, LGFMS and associated hallmark fusions (tang2023progressiveinsightsinto media b1dcbf19) | Mixed by subtype | Useful as a compact **classification/knowledge-base curation** reference (tang2023progressiveinsightsinto media b1dcbf19) | Tang et al., Front Cell Dev Biol, 2023, https://doi.org/10.3389/fcell.2023.1284428 |


*Table: This table summarizes fibrosarcoma-related entities and their hallmark molecular alterations using only the supported evidence snippets. It highlights which fusions are most diagnostically informative and which currently have therapeutic implications, especially for NTRK-driven infantile fibrosarcoma.*

### 4.2 Pathogenic variants / classification / somatic vs germline
* The clinically dominant alterations discussed are **somatic gene fusions** (e.g., ETV6::NTRK3) detected in tumor tissue by FISH and/or sequencing. (wang2023larotrectinibtreatmentfor pages 1-2, sanchez2021treatmentofinfantile pages 4-6)

### 4.3 Molecular testing modalities (practical)
* **FISH** for ETV6 rearrangement was used in IFS diagnosis and can confirm gene breakage consistent with ETV6::NTRK3; high-throughput sequencing can confirm the fusion. (wang2023larotrectinibtreatmentfor pages 1-2)
* **NGS (DNA- or RNA-based)** panels are commonly used in real-world pediatric practice to confirm NTRK fusions before TRK inhibitor therapy. (vince2024beyondclinicaltrials pages 1-2)
* **Pan-TRK immunohistochemistry** can support screening in NTRK-fusion tumors and was positive in NTRK-fusion positive tumors in a kinase fusion–positive spindle-cell tumor series. (suurmeijer2024kinasefusionpositive pages 1-3, NCT03834961 chunk 1)

### 4.4 Recent (2024) single-cell transcriptomics in IFS
A 2024 scRNA-seq study profiled four IFS tumors and reported:
* A cellular atlas comprising **14 cell populations**.
* Potential novel diagnostic markers: **POSTN, IGFBP2, CTHRC1**.
* Tumor microenvironment interactions dominated by **endothelial cells and macrophages**, supporting a mechanistic role for tumor–stroma/immune crosstalk. (li2024characterizationofthe pages 1-2)

## 5. Environmental information
No specific environmental toxin/lifestyle/infectious causal agents were retrieved in the current evidence set for fibrosarcoma.

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (IFS, NTRK fusion-driven model)
1. **Chromosomal translocation** (e.g., t(12;15)) produces **ETV6::NTRK3** fusion. (wang2023larotrectinibtreatmentfor pages 1-2)
2. The fusion encodes an **oncogenic TRK fusion protein** (kinase-driven), acting as a tumor-initiating/maintaining driver and creating a **drug target**. (wang2023larotrectinibtreatmentfor pages 1-2, orbach2020spotlightonthe pages 5-6)
3. This driver state underlies clinical responsiveness to **TRK inhibitors** (larotrectinib/entrectinib), enabling tumor shrinkage, organ/limb sparing, and integration into neoadjuvant strategies. (sahni2023limbsalvageof pages 5-7, NCT03834961 chunk 1)

### 6.2 Immune microenvironment and cellular processes (2024 scRNA-seq)
* The IFS microenvironment shows strong cell–cell communication signatures involving **endothelial cells** and **macrophages** that may promote tumorigenesis through ligand–receptor interactions. (li2024characterizationofthe pages 1-2)

Suggested ontology terms:
* GO biological processes (suggested): **GO:0001525 (angiogenesis)**; **GO:0006954 (inflammatory response)**; **GO:0008283 (cell population proliferation)**.
* CL cell types (suggested): **CL:0000115 (endothelial cell)**; **CL:0000235 (macrophage)**.

## 7. Anatomical structures affected
### 7.1 Organ/tissue localization
Fibrosarcoma/IFS are **soft tissue tumors**; IFS often occurs in extremities and other soft tissue sites in infancy (case reports include lower extremity masses). (wang2023larotrectinibtreatmentfor pages 1-2)

Suggested UBERON terms (for KB curation):
* Soft tissue: **UBERON:0000479**
* Lower limb: **UBERON:0002101** (when extremity presentation)

## 8. Temporal development
### 8.1 Onset
* IFS: typically in **children under 1 year**; a significant subset may be present at birth (~40%). (wang2023larotrectinibtreatmentfor pages 1-2)

### 8.2 Course/progression
* IFS masses may **grow rapidly** yet show **relatively indolent biological behavior** overall in many cases. (wang2023larotrectinibtreatmentfor pages 1-2)
* Metastases are uncommon but can occur; genomic profiling in recurrent/metastatic cases can reveal resistance mechanisms and acquired mutations. (kubota2025currentmanagementof pages 1-2)

## 9. Inheritance and population
### 9.1 Inheritance
No evidence in the retrieved set supports a germline inheritance pattern for fibrosarcoma/IFS; the key drivers described are **tumor (somatic) fusions**. (wang2023larotrectinibtreatmentfor pages 1-2)

### 9.2 Epidemiology
Disease-specific population incidence/prevalence for fibrosarcoma was not directly retrieved.

However, for the broader biomarker epidemiology of **NTRK fusion–positive tumors** (relevant because many IFS are NTRK-fusion driven), one large series summarized in a 2025 review reported **0.30%** NTRK-positive tumors overall (889/295,676), with **higher frequency in children (1.34%)** than adults (0.28%). (kubota2025currentmanagementof pages 1-2)

## 10. Diagnostics
### 10.1 Clinical/imaging and pathology workflow (IFS example)
A contemporary IFS diagnostic workup described in a 2023 newborn case report included:
* **Imaging** (MRI/CT) to define mass extent and vascular involvement.
* **Biopsy** (e.g., ultrasound-guided fine-needle biopsy) with **histopathology** showing spindle-cell tumor.
* **Immunohistochemistry** (e.g., vimentin positivity; variable results for other markers; lack of a specific marker).
* **Molecular confirmation** with **FISH** demonstrating ETV6 breakage and **sequencing** confirming **ETV6::NTRK3**. (wang2023larotrectinibtreatmentfor pages 1-2)

### 10.2 NTRK fusion testing and implementation
Real-world pediatric oncology practice shows NTRK fusion testing is commonly performed via **DNA/RNA NGS panels**, often triggered by tumor behavior (poor response/progression/aggressiveness) or tumor type suggestive of NTRK fusions, and is required to justify TRK inhibitor use. (vince2024beyondclinicaltrials pages 1-2)

## 11. Outcome / prognosis
### 11.1 TRK inhibitor outcomes (IFS and pediatric NTRK-fused tumors)
* An international consensus review summarized larotrectinib activity in IFS: among 29 treated IFS patients (28 evaluable), overall tumor response rate **96%** (CI reported in the review). (orbach2020spotlightonthe pages 5-6)
* A 2023 case report also cited pooled trial outcomes including IFS: **27/28 responses (96%)**, median PFS **28.3 months**, **67%** progression-free at 12 months, and estimated 12‑month survival **88%** (with median OS 44.4 months cited). (sahni2023limbsalvageof pages 5-7)
* A 2024 real-world Brazilian cohort (17 pediatric NTRK-fused tumors; 11 soft-tissue sarcomas) treated with larotrectinib reported centrally reviewed imaging responses in 14 patients: **11/14 objective responses** (2 complete, 9 partial) and 3 stable disease; most adverse events were grade 1–2. At median 25 months observation, **15/17** were alive (4 no evidence of disease; 11 alive with disease, mostly without progression). (vince2024beyondclinicaltrials pages 1-2)

## 12. Treatment
### 12.1 Standard modalities
For IFS, standard care historically emphasizes **surgical resection** (with or without chemotherapy), with attention to avoiding mutilating surgery when possible. (orbach2020spotlightonthe pages 5-6, kubota2025currentmanagementof pages 8-9)

Suggested MAXO terms:
* Surgical tumor resection: **MAXO:0000468 (surgical excision)** (suggested)
* Chemotherapy: **MAXO:0000647** (suggested)

### 12.2 Targeted therapy: TRK inhibitors (tumor-agnostic precision oncology)
**Larotrectinib**
* Mechanism: TRK inhibitor targeting NTRK fusion proteins; used orally including liquid formulations for infants. (orbach2020spotlightonthe pages 5-6)
* Implementation examples:
  * Newborn IFS treated at 20 days with oral larotrectinib showed significant tumor shrinkage without adverse effects in a case report. (wang2023larotrectinibtreatmentfor pages 1-2)
  * Limb-salvage case achieved complete response at 8 months. (sahni2023limbsalvageof pages 5-7)

**Entrectinib**
* Discussed as an orally available selective inhibitor targeting NTRK/ROS1/ALK; clinical trial analyses show activity in NTRK fusion–positive tumors. (orbach2020spotlightonthe pages 9-9)

Suggested MAXO terms:
* Targeted therapy: **MAXO:0000749 (targeted molecular therapy)** (suggested)

### 12.3 Clinical trials and real-world studies (examples)
* **NCT03834961** (Children’s Oncology Group; Phase II): neoadjuvant larotrectinib for previously untreated TRK fusion solid tumors; primary objective includes ORR in **infantile fibrosarcoma**, with incorporation of pan-TRK IHC screening and ctDNA monitoring, and long-term neurocognitive follow-up. (NCT03834961 chunk 1)
* **NCT05236257** (EPI VITRAKVI; observational): compares larotrectinib-treated IFS patients with historical controls; requires molecular confirmation of an NTRK fusion. (NCT05236257 chunk 1)

## 13. Prevention
No primary prevention or population screening strategies specific to fibrosarcoma/IFS were retrieved. Given the rarity and early-life onset of IFS, prevention is largely not established; secondary prevention is focused on timely diagnosis, molecular testing, and referral for appropriate multimodal therapy. (vince2024beyondclinicaltrials pages 1-2, NCT03834961 chunk 1)

## 14. Other species / natural disease
Comparative oncology evidence in the retrieved set includes canine fibrosarcoma proteomic work indicating that fibrosarcoma/soft tissue sarcoma biology can be studied in companion animals, but detailed cross-species natural history for “fibrosarcoma” per se was not extracted in the current evidence snippets. (tang2023progressiveinsightsinto pages 3-6)

## 15. Model organisms
No dedicated in vivo genetic model organism data for fibrosarcoma was retrieved in the current evidence set.

---

## Evidence highlights (direct abstract quotes)
* IFS clinical definition and fusion prevalence: “Infantile fibrosarcoma (IFS) is a rare tumor in childhood characterized by a single, localized, painless mass that grows rapidly…” and “Eighty-five percent of infantile fibrosarcomas are associated with… ETV6-NTRK3 gene fusion…” (Wang et al., 2023; https://doi.org/10.3389/fonc.2023.1206833) (wang2023larotrectinibtreatmentfor pages 1-2)
* Real-world pediatric TRK inhibitor outcomes: objective responses “in 11 of 14 patients: Complete responses: two; partial responses: nine; and stable disease: three cases” with “15 of 17 patients remain alive” at median 25 months (Vince et al., 2024; https://doi.org/10.1200/po.23.00713). (vince2024beyondclinicaltrials pages 1-2)

---

## Retrieved visual evidence
A review table summarizing fibrosarcoma-related entities and hallmark fusion genes is available (Table 1 from Tang et al., 2023). (tang2023progressiveinsightsinto media b1dcbf19)

## Limitations of this report
* The current evidence set is strongest for **infantile fibrosarcoma and NTRK fusion–driven disease**; it contains limited direct, contemporary (2023–2024) population-level epidemiology for classic adult fibrosarcoma.
* Direct identifiers for **MeSH/ICD/Orphanet/OMIM** were not retrieved through the current tools and should be added from dedicated ontology resources.


References

1. (tang2023progressiveinsightsinto pages 3-6): Xiaodi Tang, Xin-Hua Hu, Yang Wen, and Li Min. Progressive insights into fibrosarcoma diagnosis and treatment: leveraging fusion genes for advancements. Frontiers in Cell and Developmental Biology, Oct 2023. URL: https://doi.org/10.3389/fcell.2023.1284428, doi:10.3389/fcell.2023.1284428. This article has 8 citations.

2. (tang2023progressiveinsightsinto pages 12-13): Xiaodi Tang, Xin-Hua Hu, Yang Wen, and Li Min. Progressive insights into fibrosarcoma diagnosis and treatment: leveraging fusion genes for advancements. Frontiers in Cell and Developmental Biology, Oct 2023. URL: https://doi.org/10.3389/fcell.2023.1284428, doi:10.3389/fcell.2023.1284428. This article has 8 citations.

3. (wang2023larotrectinibtreatmentfor pages 1-2): Dandan Wang, Fanhui Zhang, Wanli Feng, Jiarong Pan, and Tianming Yuan. Larotrectinib treatment for infantile fibrosarcoma in newborns: a case report and literature review. Frontiers in Oncology, Jul 2023. URL: https://doi.org/10.3389/fonc.2023.1206833, doi:10.3389/fonc.2023.1206833. This article has 6 citations.

4. (li2024characterizationofthe pages 1-2): Yi Li, Qingchi Zhang, Ran Yang, Yong Zhan, Zifeng Li, Shu-yang Dai, De-qian Chen, Lian Chen, Antonio Ruggiero, Chunjing Ye, Yifei Lu, Enqing Zhou, Rui Dong, and Kuiran Dong. Characterization of the malignant cells and microenvironment of infantile fibrosarcoma via single-cell rna sequencing. Translational Pediatrics, 13:596-609, Apr 2024. URL: https://doi.org/10.21037/tp-24-66, doi:10.21037/tp-24-66. This article has 1 citations and is from a peer-reviewed journal.

5. (suurmeijer2024kinasefusionpositive pages 1-3): Albert J. H. Suurmeijer, Bin Xu, Dianne Torrence, Brendan C. Dickson, and Cristina R. Antonescu. Kinase fusion positive intra‐osseous spindle cell tumors: a series of eight cases with review of the literature. Genes, Oct 2024. URL: https://doi.org/10.1002/gcc.23205, doi:10.1002/gcc.23205. This article has 6 citations.

6. (OpenTargets Search: Fibrosarcoma,Infantile fibrosarcoma-NTRK3,NTRK1,NTRK2): Open Targets Query (Fibrosarcoma,Infantile fibrosarcoma-NTRK3,NTRK1,NTRK2, 7 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (sahni2023limbsalvageof pages 5-7): Shubham Sahni, Sameer Rastogi, Richa Yadav, and Adarsh Barwad. Limb salvage of an infant with infantile fibrosarcoma using trk inhibitor larotrectinib. ecancermedicalscience, Jul 2023. URL: https://doi.org/10.3332/ecancer.2023.1575, doi:10.3332/ecancer.2023.1575. This article has 6 citations and is from a peer-reviewed journal.

8. (NCT03834961 chunk 1):  Larotrectinib in Treating Patients With Previously Untreated TRK Fusion Solid Tumors and TRK Fusion Relapsed Acute Leukemia. Children's Oncology Group. 2019. ClinicalTrials.gov Identifier: NCT03834961

9. (tang2023progressiveinsightsinto media b1dcbf19): Xiaodi Tang, Xin-Hua Hu, Yang Wen, and Li Min. Progressive insights into fibrosarcoma diagnosis and treatment: leveraging fusion genes for advancements. Frontiers in Cell and Developmental Biology, Oct 2023. URL: https://doi.org/10.3389/fcell.2023.1284428, doi:10.3389/fcell.2023.1284428. This article has 8 citations.

10. (sanchez2021treatmentofinfantile pages 4-6): María Dolores Corral Sánchez, Víctor Galán Gómez, Ana Sastre Urgelles, Diego Plaza López de Sabando, Pedro Rubio Aparicio, Leopoldo Martínez Martínez, Eduardo Alonso Gamarra, José Juan Pozo Kreilinger, Rita María Regojo Zapata, Juan Carlos López Gutiérrez, Eugenia Antolín Alvarado, Felipe Gómez Martín, Ana María Sánchez Torres, Elena Marín Manzano, Luis González del Valle, and Antonio Pérez-Martínez. Treatment of infantile fibrosarcoma associated to an abdominal aortic aneurysm with larotrectinib: a case report. Pediatric Hematology and Oncology, 38:504-509, Feb 2021. URL: https://doi.org/10.1080/08880018.2021.1889730, doi:10.1080/08880018.2021.1889730. This article has 9 citations and is from a peer-reviewed journal.

11. (vince2024beyondclinicaltrials pages 1-2): Carolina Sgarioni Camargo Vince, Maria Sol Brassesco, Bruna Minniti Mançano, Lauro Jose Gregianin, Edna Kakitani Carbone, Adham do Amaral e Castro, Viviane Sayuri Yamachira Dwan, Roberta Zeppini Menezes da Silva, Cassia Silvestre Mariano, Juliana França da Mata, Marcelo Oliveira Silva, Eliana Maria Monteiro Caran, Carla Donato Macedo, Gildene Alves da Costa, Tereza Cristina Esteves, Luciana Nunes Silva, Sima Esther Ferman, Flavia Delgado Martins, Lilian Maria Cristófani, Vicente Odone-Filho, Marcelo Milone Silva, Rui Manuel Reis, Mara Albonei Dudeque Pianovski, Paulo Vidal Campregher, Mayara Satsuki Kunii, Karla Emilia de Sá Rodrigues, Neviçolino Pereira Carvalho Filho, and Elvis Terci Valera. Beyond clinical trials: understanding neurotrophic tropomyosin receptor kinase inhibitor challenges and efficacy in real-world pediatric oncology. JCO Precision Oncology, May 2024. URL: https://doi.org/10.1200/po.23.00713, doi:10.1200/po.23.00713. This article has 5 citations and is from a peer-reviewed journal.

12. (orbach2020spotlightonthe pages 5-6): Daniel Orbach, Monika Sparber-Sauer, Theodore W. Laetsch, Veronique Minard-Colin, Stefan S. Bielack, Michela Casanova, Nadege Corradini, Ewa Koscielniak, Monika Scheer, Simone Hettmer, Gianni Bisogno, Douglas S. Hawkins, and Andrea Ferrari. Spotlight on the treatment of infantile fibrosarcoma in the era of neurotrophic tropomyosin receptor kinase inhibitors: international consensus and remaining controversies. European Journal of Cancer, 137:183-192, Sep 2020. URL: https://doi.org/10.1016/j.ejca.2020.06.028, doi:10.1016/j.ejca.2020.06.028. This article has 74 citations and is from a domain leading peer-reviewed journal.

13. (kubota2025currentmanagementof pages 1-2): Yuta Kubota, Masanori Kawano, Tatsuya Iwasaki, Ichiro Itonaga, Nobuhiro Kaku, Toshifumi Ozaki, and Kazuhiro Tanaka. Current management of neurotrophic receptor tyrosine kinase fusion-positive sarcoma: an updated review. Japanese Journal of Clinical Oncology, 55:313-326, Feb 2025. URL: https://doi.org/10.1093/jjco/hyaf015, doi:10.1093/jjco/hyaf015. This article has 6 citations and is from a peer-reviewed journal.

14. (kubota2025currentmanagementof pages 8-9): Yuta Kubota, Masanori Kawano, Tatsuya Iwasaki, Ichiro Itonaga, Nobuhiro Kaku, Toshifumi Ozaki, and Kazuhiro Tanaka. Current management of neurotrophic receptor tyrosine kinase fusion-positive sarcoma: an updated review. Japanese Journal of Clinical Oncology, 55:313-326, Feb 2025. URL: https://doi.org/10.1093/jjco/hyaf015, doi:10.1093/jjco/hyaf015. This article has 6 citations and is from a peer-reviewed journal.

15. (orbach2020spotlightonthe pages 9-9): Daniel Orbach, Monika Sparber-Sauer, Theodore W. Laetsch, Veronique Minard-Colin, Stefan S. Bielack, Michela Casanova, Nadege Corradini, Ewa Koscielniak, Monika Scheer, Simone Hettmer, Gianni Bisogno, Douglas S. Hawkins, and Andrea Ferrari. Spotlight on the treatment of infantile fibrosarcoma in the era of neurotrophic tropomyosin receptor kinase inhibitors: international consensus and remaining controversies. European Journal of Cancer, 137:183-192, Sep 2020. URL: https://doi.org/10.1016/j.ejca.2020.06.028, doi:10.1016/j.ejca.2020.06.028. This article has 74 citations and is from a domain leading peer-reviewed journal.

16. (NCT05236257 chunk 1):  A Study Called EPI VITRAKVI to Compare Treatment Results in Patients With Infantile Fibrosarcoma (IFS), a Type of Connective Soft Tissue Cancer, Who Received a Treatment Called Larotrectinib From a Study Called SCOUT With Patient Data From an External Database. Bayer. 2022. ClinicalTrials.gov Identifier: NCT05236257