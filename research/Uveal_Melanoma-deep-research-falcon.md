---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T23:02:08.129936'
end_time: '2026-04-05T23:16:20.362727'
duration_seconds: 852.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Uveal Melanoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 69
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Uveal Melanoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Uveal Melanoma** covering all of the
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
- **Disease Name:** Uveal Melanoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Uveal Melanoma** covering all of the
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


## Comprehensive Research Report: Uveal Melanoma (UM)

### Target disease and classification
**Disease overview and definition.** Uveal melanoma (UM) is a malignant neoplasm arising from melanocytes in the uveal tract (iris, ciliary body, choroid) and is the most common primary malignant intraocular tumor in adults. (pasarica2024pathologicalandmolecular pages 1-2, NCT07063875 chunk 1)

**Category.** Rare ocular cancer (melanoma subtype); primary intraocular malignancy. (pasarica2024pathologicalandmolecular pages 1-2, NCT07063875 chunk 1)

**Key identifiers (available in current evidence corpus).**
- **MeSH preferred term:** *Uveal Melanoma*; **MeSH ID:** **D000098943** (as listed in ClinicalTrials.gov MeSH tagging). (NCT07063875 chunk 1)
- **ICD-O site codes used in SEER registry studies:** **C69.3 (choroid)**; **C69.4 (ciliary body and iris)**; melanoma morphology codes 8720–8790 were used to identify melanoma histologies. (weinberger2025uvealmelanoma5year pages 1-2)
- **AJCC staging:** AJCC **8th edition** TNM staging is the current standard for iris and posterior uveal melanoma. (pasarica2024pathologicalandmolecular pages 2-4)

**Identifiers not retrievable from current tool corpus.** MONDO ID, Orphanet ID, and OMIM disease entries were not available in the retrieved documents; therefore they cannot be asserted here without external ontology lookup.

**Common synonyms / alternative names (used in the evidence corpus).**
- Ocular melanoma (when referring broadly to intraocular melanoma subtypes) (lissak2024whatsetsuveal pages 1-3)
- Posterior uveal melanoma (commonly meaning choroid/ciliary body) (pasarica2024pathologicalandmolecular pages 2-4)

**Data provenance (EHR vs aggregated resources).** Most epidemiology and outcomes statistics cited here derive from **aggregated registry resources** (e.g., SEER; national insurance databases) and multi-center cohorts, rather than single-institution EHR alone. (weinberger2025uvealmelanoma5year pages 2-4, toth2024incidenceandmortality pages 1-2)

---

## 1. Disease information (current understanding)
UM is biologically distinct from cutaneous melanoma and is characterized by: (i) a small number of recurrent initiating driver mutations (GNAQ/GNA11 axis), (ii) strong prognostic dependence on secondary alterations (e.g., BAP1 loss, monosomy 3), and (iii) marked hepatotropism, with the liver being the predominant metastatic site. (pasarica2024pathologicalandmolecular pages 1-2, iavarone2025ocularmelanomaa pages 4-6)

Recent reviews emphasize that effective local control of the primary tumor has not translated into major improvements in population-level survival, largely because micrometastatic disease is often present at diagnosis and metastasis can occur years later. (pasarica2024pathologicalandmolecular pages 1-2, weinberger2025uvealmelanoma5year pages 1-2)

---

## 2. Etiology and risk factors
### 2.1 Causal factors and mechanistic etiologies
**Somatic oncogenesis.** UM tumorigenesis is typically initiated by mutually exclusive activating mutations in **GNAQ** or **GNA11** (and less commonly PLCB4 or CYSLTR2), with secondary alterations (BAP1 inactivation; SF3B1; EIF1AX) shaping metastatic risk. (pasarica2024pathologicalandmolecular pages 1-2, iavarone2025ocularmelanomaa pages 4-6)

### 2.2 Risk factors (human epidemiology)
**Phenotype and ancestry.** Registry and review data consistently indicate increased UM incidence among people with **light pigmentation phenotypes** (e.g., light eye color, sun-sensitive skin) and strong predominance in White populations in US registries (≈98% White in SEER-based analyses). (weinberger2025uvealmelanoma5year pages 2-4, jager2020uvealmelanoma pages 2-3)

**Ultraviolet radiation (UVR): subsite-specific associations (2024 registry analysis).** A large US registry study linking satellite-based ambient UVR to ocular melanoma incidence (2000–2019) found **no association with total ocular melanoma** overall, but observed **increased incidence for ciliary body/iris melanoma** in the highest UVR quartile and **reduced incidence for choroidal melanoma** in that quartile (Q4 vs Q1 IRR 1.63 for ciliary body/iris; IRR 0.86 for choroid). (arockiaraj2024ambientultravioletradiation pages 1-2)

**Germline predisposition.** Germline susceptibility is uncommon but clinically important. A 2025 high-risk sequencing study summarized that **BAP1 is the only known high-penetrance UM susceptibility gene**, with pathogenic/likely pathogenic germline BAP1 variants estimated at ~**2% of all UM** and up to ~**25% of familial UM**; 1–4% of cases are reported as familial. (repo2025germlinecancersusceptibility pages 1-3)

**Germline BAP1 and outcomes.** In a 2024 cohort that included six germline BAP1 carriers, **5/6 developed metastases**, consistent with high metastatic risk in this subgroup. (wadt2024characterizationofsomatic pages 1-2)

### 2.3 Protective factors
No protective genetic or environmental factors with quantitative effect estimates were available in the retrieved evidence corpus.

### 2.4 Gene–environment interactions
Evidence in this corpus supports a plausible interaction between **pigmentation genetics/phenotype** and ocular environmental exposures (including light exposure), but does not provide definitive causal interaction models. For example, risk is linked to pigmentation-associated loci (e.g., HERC2/OCA2) and UVR associations appear subsite-dependent (iris/ciliary body vs choroid). (jager2020uvealmelanoma pages 2-3, arockiaraj2024ambientultravioletradiation pages 1-2)

---

## 3. Phenotypes (clinical presentation)
### 3.1 Common presenting symptoms with frequencies
Large clinical cohorts show that UM can be asymptomatic or present with nonspecific visual symptoms.

**Posterior UM cohort (n=1,449):**
- **Blurred vision:** 39% (559/1,449)
- **Visual field defect (“shadow”):** 16% (277/1,449)
- **Photopsia and/or floaters:** 12% (176/1,449)
- **Asymptomatic:** 28% (400/1,449)
- **Retinal detachment (recorded subset):** 63% (245/391) with exudative detachments among those with recorded RD status
- **Mean symptom duration:** 4 months (SD 5)
(fili2021presentingsymptomsare pages 1-2)

**Enucleation cohort (n=69):** blurred vision 49%, visual field shadow 26%, photopsia/floaters 10%, no symptoms 13%. (sabazade2022vasculogenicmimicrycorrelates pages 1-3)

**Classic symptom profile in a high-citation review:** blurred vision 38%, photopsia 9%, floaters 7%, visual field loss 6%, ~30% asymptomatic. (kaliki2017uvealmelanomarelatively pages 4-6)

### 3.2 Phenotype ontology suggestions (HPO)
Suggested HPO mappings (not exhaustive; terms named for KB usability):
- Blurred vision → **HP:0000622 (Blurred vision)** (supported by cohort symptom data). (fili2021presentingsymptomsare pages 1-2)
- Visual field defect/shadow → **HP:0001129 (Visual field defect)**. (fili2021presentingsymptomsare pages 1-2)
- Photopsia → **HP:0001100 (Photopsia)**. (fili2021presentingsymptomsare pages 1-2)
- Floaters → **HP:0000628 (Vitreous floaters)**. (fili2021presentingsymptomsare pages 1-2)
- Metamorphopsia/distorted vision → **HP:0000570 (Metamorphopsia)**. (fili2021presentingsymptomsare pages 1-2)
- Exudative retinal detachment → **HP:0000541 (Retinal detachment)** (subtype not explicitly coded in HPO; record as RD and add free-text qualifier). (fili2021presentingsymptomsare pages 1-2)

### 3.3 Onset, progression, and QoL impact
UM is typically diagnosed in older adults; SEER data show a median age at diagnosis around **63 years**. (weinberger2025uvealmelanoma5year pages 1-2)

Vision-related QoL impact is substantial because initial symptoms and treatment toxicities commonly involve visual acuity decline and retinal complications, particularly after radiotherapy. (semeniuk2024currentandemerging pages 2-3)

---

## 4. Genetic/molecular information and mechanism/pathophysiology
### 4.1 Core molecular architecture and classes
UM is characterized by **(i) early initiating oncogenic mutations** and **(ii) secondary progression alterations** with strong prognostic significance. A 2024 diagnostics review states: early/initiating mutations include **GNAQ, GNA11, PLCB4, CYSLTR2**; secondary progression alterations include **BAP1 inactivation** and **SF3B1/EIF1AX mutations**. (pasarica2024pathologicalandmolecular pages 1-2)

A mechanistic review describes Gαq/Gα11 signaling as a central upstream axis that feeds into **PLCβ→PKC→MAPK**, **PI3K/AKT/mTOR**, and **YAP/TAZ** transcriptional programs. (iavarone2025ocularmelanomaa pages 4-6)

A commonly used genomic stratification scheme (TCGA-based) emphasizes chromosome 3 and 8q copy-number status, yielding risk classes with distinct metastasis rates; one validation study reported **5-year cumulative distant metastasis rates**: 4% (class A), 20% (B), 33% (C), 63% (D). (pasarica2024pathologicalandmolecular pages 1-2, pasarica2024pathologicalandmolecular pages 9-10)

**Structured summary artifact.** The table below summarizes initiating vs progression drivers, approximate frequencies where available, and prognostic associations.

| Category | Gene/Alteration | Approx. frequency/range (reported) | Key pathway/mechanism | Prognostic association | Key supporting citation IDs |
|---|---|---:|---|---|---|
| Initiating | **GNAQ** hotspot mutation (Q209, less often R183) | ~45–55%; ~45% in some summaries | Constitutive Gαq activation; PLCβ→PKC→MAPK/ERK, PI3K/AKT/mTOR, TRIO/RhoA→YAP/TAZ | Early oncogenic driver; not independently linked to markedly increased metastatic risk in meta-analysis | (ambrosio2026amultifacetedapproach pages 9-12, kastelan2026precisiononcologyin pages 4-5, dore2026clinicalmolecularpathology pages 3-5, lamasfrancis2024impactofdriver pages 1-2) |
| Initiating | **GNA11** hotspot mutation (Q209, less often R183) | ~30–40%; ~42% in some summaries | Same Gαq-driven signaling as GNAQ; constitutive PLCβ/PKC/MAPK and YAP/TAZ activation | Early driver; associated in some reports with shorter disease-specific survival and more high-risk cytogenetics than GNAQ | (ambrosio2026amultifacetedapproach pages 9-12, kastelan2026precisiononcologyin pages 4-5, dore2026clinicalmolecularpathology pages 3-5) |
| Initiating | **PLCB4** activating mutation | ~3–4% (rare; 1–5% in some reviews) | Downstream effector of Gαq; activates PKC and convergent MAPK signaling | Rare initiating event; mainly biologically convergent with GNAQ/GNA11 rather than independently prognostic | (pasarica2024pathologicalandmolecular pages 1-2, kastelan2026precisiononcologyin pages 4-5, dore2026clinicalmolecularpathology pages 3-5) |
| Initiating | **CYSLTR2** activating mutation (e.g., p.L129Q) | ~2–4% (rare; 1–5% in some reviews) | GPCR upstream of Gαq; produces GNAQ-like signaling | Rare initiating event; prognostic effect less established than secondary alterations | (pasarica2024pathologicalandmolecular pages 1-2, kastelan2026precisiononcologyin pages 4-5, dore2026clinicalmolecularpathology pages 3-5) |
| Progression | **BAP1** loss/inactivation (often with monosomy 3) | ~40–45%; ~1/3 in some summaries; 47% in one review; 84% of metastatic UM in one review | Tumor suppressor loss; chromatin regulation/deubiquitination defects, dedifferentiation, metastatic phenotype, altered methylation state | Strongest adverse molecular marker; significantly increases metastasis risk; associated with early metastasis and poor survival | (iavarone2025ocularmelanomaa pages 4-6, kastelan2026precisiononcologyin pages 4-5, dore2026clinicalmolecularpathology pages 3-5, lamasfrancis2024impactofdriver pages 1-2, wadt2024characterizationofsomatic pages 1-2) |
| Progression | **Monosomy 3** | ~45–50% | Cytogenetic hallmark tightly linked to BAP1 loss and high-risk molecular class | High metastatic risk, poor prognosis, earlier dissemination | (iavarone2025ocularmelanomaa pages 4-6, kastelan2026precisiononcologyin pages 4-5, lamasfrancis2024impactofdriver pages 1-2, pasarica2024pathologicalandmolecular pages 9-10) |
| Progression | **SF3B1** mutation (often R625) | ~15–25%; 20–25% in some reviews | Aberrant 3' splice-site usage / altered RNA splicing | Intermediate-risk group; characteristically associated with late-onset metastasis rather than early dissemination | (iavarone2025ocularmelanomaa pages 4-6, kastelan2026precisiononcologyin pages 4-5, dore2026clinicalmolecularpathology pages 3-5) |
| Progression | **EIF1AX** mutation | ~8–19%; 8–15% in some reviews | Translation initiation factor alteration; typically with disomy 3 | Low metastatic risk; favorable prognosis / excellent survival | (ambrosio2026amultifacetedapproach pages 9-12, kastelan2026precisiononcologyin pages 4-5, dore2026clinicalmolecularpathology pages 3-5) |
| Progression | **8q gain / amplification** | ~40–55% | Copy-number gain that augments metastatic potential; may involve drivers in the 8q region | Adverse; often co-occurs with monosomy 3 and worsens metastatic risk | (kastelan2026precisiononcologyin pages 4-5, lamasfrancis2024impactofdriver pages 1-2, pasarica2024pathologicalandmolecular pages 9-10) |
| Progression / Protective | **6p gain / amplification** | Not consistently quantified in provided evidence | Cytogenetic change associated with disomy 3 / class 1 biology | Favorable or relatively protective prognostic association | (ambrosio2026amultifacetedapproach pages 9-12, iavarone2025ocularmelanomaa pages 4-6, lamasfrancis2024impactofdriver pages 1-2, pasarica2024pathologicalandmolecular pages 9-10) |
| Prognostic biomarker | **PRAME** expression positive | ~29.9% PRAME+ in prospective COOG2 cohort | RNA expression biomarker that refines metastatic-risk stratification within GEP classes | Worse outcomes than PRAME-negative tumors; increases risk within both class 1 and class 2 tumors | (harbour202415geneexpressionprofile pages 5-6, harbour202415geneexpressionprofile pages 17-18, harbour202415geneexpressionprofile pages 1-2) |
| Prognostic classifier | **TCGA group A** | Not a frequency; 5-year distant metastasis rate **4%** | Integrated chromosome 3/8q-based molecular subclass | Lowest-risk TCGA class | (pasarica2024pathologicalandmolecular pages 1-2, pasarica2024pathologicalandmolecular pages 9-10) |
| Prognostic classifier | **TCGA group B** | Not a frequency; 5-year distant metastasis rate **20%** | Integrated chromosome 3/8q-based molecular subclass | Low-intermediate risk | (pasarica2024pathologicalandmolecular pages 1-2, pasarica2024pathologicalandmolecular pages 9-10) |
| Prognostic classifier | **TCGA group C** | Not a frequency; 5-year distant metastasis rate **33%** | Integrated chromosome 3/8q-based molecular subclass | Intermediate-high risk | (pasarica2024pathologicalandmolecular pages 1-2, pasarica2024pathologicalandmolecular pages 9-10) |
| Prognostic classifier | **TCGA group D** | Not a frequency; 5-year distant metastasis rate **63%** | Integrated chromosome 3/8q-based molecular subclass | Highest-risk TCGA class | (pasarica2024pathologicalandmolecular pages 1-2, pasarica2024pathologicalandmolecular pages 9-10) |


*Table: This table summarizes the main initiating drivers, secondary prognostic alterations, and molecular classifiers in uveal melanoma. It is useful for quickly linking each alteration to approximate frequency, biology, and metastatic-risk implications.*

### 4.2 Prognostic molecular testing: 15-GEP and PRAME (2024 prospective validation)
A large prospective multi-center study (COOG2; n=1,577) validated integration of a **15-gene expression profile (15-GEP)** with **PRAME RNA expression** for prognostic stratification, and concluded the integrated classifier supports “risk-adjusted metastatic surveillance and adjuvant trial stratification”. (harbour202415geneexpressionprofile pages 1-2)

Quantitatively, **5-year metastasis-free survival (MFS)** differed strongly by integrated status:
- Class 1/PRAME−: **95.6%**
- Class 1/PRAME+: **80.6%**
- Class 2/PRAME−: **58.3%**
- Class 2/PRAME+: **44.8%**
(harbour202415geneexpressionprofile pages 1-2)

A Kaplan–Meier visualization of these strata is available in the retrieved figure region. (harbour202415geneexpressionprofile media 9fd22c19)

### 4.3 Epigenetics and chromatin state
Inferred from molecular subclassification, monosomy 3 and BAP1 aberrancy are associated with a distinct methylation pattern and dedifferentiation/metastatic phenotype. (pasarica2024pathologicalandmolecular pages 9-10, iavarone2025ocularmelanomaa pages 4-6)

### 4.4 Mechanistic causal chain (conceptual)
A consensus mechanistic chain supported by the retrieved evidence is:
1) **Initiation** via constitutively active Gαq/Gα11 signaling (GNAQ/GNA11; or PLCB4/CYSLTR2), activating PKC/MAPK and YAP/TAZ programs → 2) **Progression** via acquisition of high-risk chromosomal changes (monosomy 3; 8q gain) and tumor suppressor loss (BAP1) or splicing alterations (SF3B1) → 3) **Metastatic competence** with strong **liver tropism** and poor survival once metastasis occurs. (iavarone2025ocularmelanomaa pages 4-6, kastelan2026precisiononcologyin pages 4-5, pasarica2024pathologicalandmolecular pages 1-2)

### 4.5 Suggested GO (biological process) and CL (cell type) terms
These suggestions are consistent with the mechanisms described in the cited sources:
- GO: **MAPK cascade**; **PI3K/AKT signaling**; **Hippo signaling / YAP/TAZ-mediated transcription**; **RNA splicing** (SF3B1); **chromatin organization** (BAP1). (iavarone2025ocularmelanomaa pages 4-6, dore2026clinicalmolecularpathology pages 3-5)
- CL: **melanocyte** (tumor cell-of-origin; uveal melanocytes). (pasarica2024pathologicalandmolecular pages 1-2)

---

## 5. Diagnostics and staging
### 5.1 Diagnostic workup (real-world clinical implementation)
A contemporary prospective uveal melanoma cohort (COOG2) used multimodal ophthalmic evaluation including **fundus photography, OCT, and ocular ultrasonography**, and staged tumors using **AJCC 8th edition**; baseline systemic staging commonly included **CT chest/abdomen/pelvis**, and surveillance emphasized liver imaging. (harbour202415geneexpressionprofile pages 2-4)

A 2024 plaque brachytherapy cohort reported UM diagnostic modalities including **A-scan and B-scan echography, fluorescein angiography, indocyanine green angiography, OCT, and MRI**, with AJCC 8th edition staging. (laliscia2024iodineplaquebrachytherapy pages 1-2)

### 5.2 AJCC 8th edition staging (key concepts)
AJCC 8th edition organizes T category by **largest basal diameter** and **tumor thickness**, with subclassifications for **ciliary body involvement** and **extraocular extension**; higher stage correlates with higher metastatic risk (e.g., Stage II ~3.1× and Stage III ~9.3× metastasis risk versus Stage I in one validation). (pasarica2024pathologicalandmolecular pages 2-4)

### 5.3 Differential diagnosis
Differential diagnosis (“pseudomelanomas”) is widely recognized in the clinical literature but specific differential lists and distinguishing features were not directly retrievable from the 2023–2024 focused evidence pulled here.

---

## 6. Epidemiology, population, natural history, and prognosis
### 6.1 Incidence and demographics (registry-based)
**United States (SEER 1975–2020 update).** Mean age-adjusted incidence: **5.6 per million** (95% CI 5.5–5.7), with higher incidence in males (6.3/million) than females (5.0/million), median age 63 years, and heavy predominance in White patients (~98%). Incidence overall was stable, with a small annual increase (APC 0.5%) in White patients. (weinberger2025uvealmelanoma5year pages 2-4)

**Hungary nationwide (NHIF 2012–2021).** Age-standardized incidence ranged **6.40–10.96 per 1,000,000 person-years**; anatomic distribution was mostly choroidal (90%); all-cause mortality declined during 2012–2021 but could not be attributed clearly to improved treatments. (toth2024incidenceandmortality pages 1-2)

### 6.2 Outcomes and metastatic behavior
**Primary treatment pattern shifts without survival improvement (US SEER).** Surgery-alone decreased from 93% (1975–1977) to 21% (2017–2020), while radiation increased from 1% to 58%, but 5-year relative survival remained unchanged at ~82.8% (1975–2016). (weinberger2025uvealmelanoma5year pages 1-2)

**Metastatic prognosis.** In a SEER-linked analysis (2000–2019), mortality after metastatic uveal melanoma was reported as **80% by 1 year** and **92% by 2 years**. (arockiaraj2024ambientultravioletradiation pages 1-2)

---

## 7. Treatment
### 7.1 Local therapy for primary UM (real-world use)
**Plaque brachytherapy and proton/charged-particle radiotherapy** are the main globe-sparing modalities, with enucleation reserved for select cases (e.g., very large tumors, unfavorable location, or complications). Candidate selection is often driven by tumor size and proximity to critical structures such as the optic nerve. (semeniuk2024currentandemerging pages 2-3)

**Plaque brachytherapy outcomes (2024 series).** A 2024 125I plaque brachytherapy cohort (n=50) reported 5-year outcomes: **local control 83.0%**, **metastasis-free survival 90.3%**, **overall survival 92.1%**; radiation retinopathy grade 1–3 occurred in **18%**. (laliscia2024iodineplaquebrachytherapy pages 1-2)

**Radiotherapy complications (2024 review synthesis).** A 2024 review summarized commonly reported complications after plaque brachytherapy including cataracts (~20%), radiation maculopathy (~25%), vitreous hemorrhage (~18%), retinal detachment (~2%), and secondary glaucoma (~23%). (semeniuk2024currentandemerging pages 2-3)

**Charged-particle therapy vs brachytherapy (2024 meta-analysis).** Charged-particle therapy had lower local recurrence than brachytherapy (OR **0.38**, 95% CI 0.24–0.60), with no statistically significant differences in mortality, enucleation, or cataract; secondary glaucoma risk may be higher with charged-particle therapy. (tseng2024comparingefficacyof pages 1-2)

**Proton therapy outcomes (2024–2025 evidence).**
- A 2024 proton therapy review described a large cohort with **10-year local control 92.1%**, metastasis-free survival 76.4%, overall survival 64.1%, and eye retention 87.3%. (chan2024protontherapyin pages 6-7)
- A 2025 systematic review/meta-analysis of proton therapy for choroidal melanoma reported local control **88% at 10 years** and overall survival **39% at 10 years**, with common complications including glaucoma (~17.9–27%), optic neuropathy (~12.8–64%), and cataracts (~29.6–39.8%). (miao2025efficacyandsafety pages 1-2)

### 7.2 Systemic therapy for metastatic UM (2023–2024 prioritized)
**Tebentafusp (TCR-bispecific gp100×CD3; ImmTAC).** Tebentafusp is the first systemic therapy in UM with demonstrated overall survival benefit in a molecularly defined group (HLA-A*02:01-positive). Pivotal-trial-level summaries report median OS **21.6 vs 16.9 months** (HR 0.68). (saldanha2025howwetreat pages 1-2)

**ctDNA-guided response/prognosis with tebentafusp (2024).** In a prospective cohort of 69 metastatic UM patients treated with tebentafusp, baseline detectable ctDNA was strongly prognostic (median OS **12.9 vs 40.5 months** for detectable vs undetectable), and a ≥90% ctDNA reduction at 12 weeks correlated with longer OS (median **21.2 vs 12.9 months**). (rodrigues2024prospectiveassessmentof pages 1-2)

**Long-term tebentafusp follow-up (2024).** A phase 1/2 long-term follow-up (median follow-up 48.5 months) reported median OS **17.4 months**, with OS rates **62% (1-year)**, **40% (2-year)**, **23% (3-year)**, **14% (4-year)**; ctDNA clearance associated with markedly improved survival. (sacco2024longtermsurvivalfollowup pages 1-2)

**Structured therapy summary artifact.**

| Modality | Setting | Key outcomes/statistics | Key adverse events | Implementation notes | Primary sources (URLs; publication month/year) | Citation IDs |
|---|---|---|---|---|---|---|
| **Tebentafusp** | Unresectable/metastatic UM; HLA-A*02:01-positive adults | Phase 3 IMCgp100-202: median OS **21.6 vs 16.9 months**, HR **0.68**; 6-month PFS **31% vs 19%**; ORR about **9%**. Prospective 2024 ctDNA cohort: median PFS **2.8 months**, median OS **21.8 months**, ORR **10%**. Meta-analysis: pooled 1-year OS **69%**, 2-year OS **42%**, 3-year OS **26%**; pooled median PFS **2.74 months**, pooled median OS **19.78 months**. ctDNA: baseline detectable ctDNA associated with shorter OS (**12.9 vs 40.5 months**); ≥90% ctDNA reduction at 12 weeks associated with longer OS (**21.2 vs 12.9 months**); ctDNA clearance in earlier long-term study associated with **100% 1-year**, **73% 2-year**, **45% 3-year** OS | CRS very common: **89%** in review of pivotal data; pooled CRS **86%** in meta-analysis. Other common AEs: rash **85%**, pyrexia **79%**, pruritus **72%**, hypotension **43%**; grade 3/4 TRAEs **44%** in phase 3-style data; pooled grade ≥3 TRAEs **40%** | First systemic therapy with demonstrated OS benefit in mUM; restricted to **HLA-A*02:01** (~45–50% eligible). Step-up dosing and monitoring required during first infusions due to CRS. Radiographic response may underestimate benefit; ctDNA is promising but still investigational | Saldanha et al., *ESMO Open* https://doi.org/10.1016/j.esmoop.2025.104496 (Apr 2025); Rodrigues et al., *Nature Communications* https://doi.org/10.1038/s41467-024-53145-0 (Oct 2024); Sacco et al., *J Immunother Cancer* https://doi.org/10.1136/jitc-2024-009028 (Jun 2024); Wang et al., *Front Oncol* https://doi.org/10.3389/fonc.2025.1667282 (Oct 2025) | (saldanha2025howwetreat pages 1-2, rodrigues2024prospectiveassessmentof pages 1-2, sacco2024longtermsurvivalfollowup pages 1-2, wang2025evaluatingtheefficacy pages 1-2, wang2025evaluatingtheefficacy pages 7-10) |
| **Ipilimumab + nivolumab** | Advanced/metastatic UM, typically HLA-unrestricted | Current corpus contains only limited higher-level comparative evidence. A 2025 retrospective real-world series outside the cited context reported ORR **21%**, median PFS **5.8 months**, median OS **12.3 months**, but this item is **not available as a citable context ID here**. Within current citable corpus, reviews state dual ICI has some activity but substantially less robust evidence than tebentafusp and no randomized OS advantage established in the provided evidence | Immune-related toxicity can be substantial; specific citable rates not robustly available in current context for this regimen alone | For this artifact, note **evidence gap in current citable corpus**; tebentafusp remains preferred for eligible HLA-A*02:01-positive patients, while dual ICI is often considered for others in practice | Maurer et al., *Clin Exp Med* https://doi.org/10.1007/s10238-024-01497-8 (Oct 2024); Saldanha et al., *ESMO Open* https://doi.org/10.1016/j.esmoop.2025.104496 (Apr 2025) | (saldanha2025howwetreat pages 1-2) |
| **Liver-directed percutaneous therapies** (radioembolization, TACE, immunoembolization, percutaneous hepatic perfusion, thermal therapies) | Metastatic UM with liver-dominant disease | Systematic review of **26 studies / 955 patients**: median OS **16 months**, median PFS **8.2 months**, median ORR **39%** | Predominantly hematologic and gastrointestinal adverse events after percutaneous hepatic procedures | Important because liver is the dominant metastatic site in UM; used especially for liver-predominant disease and often combined with systemic strategies in practice | Inì et al., *Technology in Cancer Research & Treatment* https://doi.org/10.1177/15330338251343144 (May 2025) | (arockiaraj2024ambientultravioletradiation pages 1-2) |
| **Tebentafusp + ctDNA monitoring** | Metastatic UM on tebentafusp | ddPCR feasible in most patients: **97%** had a trackable mutation; ctDNA detectable at baseline in ~**61%**. Strong prognostic/predictive signal for baseline detectability and early reduction | Biomarker study; safety details not primary endpoint in provided excerpt | Useful implementation adjunct for response/prognosis assessment, but **not yet standard-of-care validated** | Rodrigues et al., *Nature Communications* https://doi.org/10.1038/s41467-024-53145-0 (Oct 2024) | (rodrigues2024prospectiveassessmentof pages 1-2) |
| **NCT06246149 – Adjuvant tebentafusp in high-risk ocular melanoma** | Adjuvant / high-risk ocular melanoma after local therapy | Phase 3; recruiting; planned enrollment **290** | Not yet reported | Important ongoing study testing earlier use of tebentafusp beyond overt metastatic disease | ClinicalTrials.gov NCT06246149 (recruiting) | (saldanha2025howwetreat pages 1-2) |
| **NCT07063875 – Tebentafusp + IL-2** | Metastatic UM combination immunotherapy | Phase 1/2; recruiting; planned enrollment **8** | Not yet reported | Exploratory combination intended to intensify immune activation/T-cell persistence | ClinicalTrials.gov NCT07063875 (recruiting) | (NCT07063875 chunk 1) |
| **NCT06070012 – First-line tebentafusp in HLA-A*02:01-positive previously untreated mUM** | First-line metastatic UM | Phase 2; recruiting; planned enrollment **44** | Not yet reported | Focuses on untreated HLA-A*02:01-positive metastatic disease and may refine biomarker use | ClinicalTrials.gov NCT06070012 (recruiting) | (saldanha2025howwetreat pages 1-2) |
| **NCT06627244 – Tebentafusp + radioembolization** | Metastatic UM with liver-directed combination strategy | Phase 2; recruiting; planned enrollment **30** | Not yet reported | Directly tests systemic tebentafusp plus liver-directed radiation embolization | ClinicalTrials.gov NCT06627244 (recruiting) | (saldanha2025howwetreat pages 1-2) |
| **NCT06626516 – Tebentafusp with liver-directed therapy (LDT)** | Metastatic UM | Phase 1/2; recruiting; planned enrollment **109** | Not yet reported | Broader platform for combining tebentafusp with liver-directed treatment | ClinicalTrials.gov NCT06626516 (recruiting) | (saldanha2025howwetreat pages 1-2) |
| **NCT07276386 – Melphalan/HDS via PHP + tebentafusp** | Metastatic UM | Phase 2; recruiting; planned enrollment **18** | Not yet reported | Evaluates tebentafusp with percutaneous hepatic perfusion/melphalan strategy | ClinicalTrials.gov NCT07276386 (recruiting) | (saldanha2025howwetreat pages 1-2) |


*Table: This table summarizes the main systemic and liver-directed treatment options for metastatic uveal melanoma, with emphasis on tebentafusp outcomes, biomarker data, and ongoing combination/adjuvant trials. It is useful for quickly comparing efficacy, toxicity, and real-world implementation constraints such as HLA restriction and liver-dominant disease management.*

### 7.3 MAXO suggestions (treatments)
These MAXO suggestions are provided for KB normalization (names provided; ontology IDs not available in corpus):
- Plaque brachytherapy (episcleral plaque radiotherapy) (laliscia2024iodineplaquebrachytherapy pages 1-2)
- Proton beam therapy (charged-particle radiotherapy) (miao2025efficacyandsafety pages 1-2)
- Enucleation (eye removal surgery) (referenced as comparator in reviews) (semeniuk2024currentandemerging pages 2-3)
- Tebentafusp therapy (bispecific T-cell engager / TCR-bispecific) (rodrigues2024prospectiveassessmentof pages 1-2)
- Liver-directed embolization/perfusion/ablation (interventional radiology) (arockiaraj2024ambientultravioletradiation pages 1-2)

---

## 8. Prevention and surveillance
### 8.1 Primary prevention
No validated primary-prevention interventions (analogous to vaccines) exist for UM in the current evidence corpus. Risk reduction is generally limited by the uncertain/heterogeneous role of UVR, especially for posterior UM. (arockiaraj2024ambientultravioletradiation pages 1-2)

### 8.2 Secondary prevention: metastatic surveillance (expert consensus and major review)
**Risk-adapted surveillance using molecular prognostics (2023 expert review).** A Nature Reviews Clinical Oncology review recommends surveillance stratified by molecular risk (GEP class and PRAME): e.g., annual imaging for low risk, 6–12 month imaging for intermediate risk, and 3–6 month imaging for high risk early after treatment, with continued surveillance given potential for late metastases. (carvajal2023advancesinthe pages 5-7)

**Delphi expert consensus (2025; surveys conducted 2024–2025).** A multidisciplinary Delphi panel produced consensus surveillance guidance for intermediate- and high-risk UM, favoring contrast-enhanced hepatic imaging (CT/MRI) over ultrasound and not recommending PET/CT for routine surveillance. It also proposed specific surveillance frequencies (e.g., intermediate risk at least every 3–6 months for 5 years, then annually to ≥10 years; high risk every 3–6 months in years 1–5 and every 6–12 months in years 6–10, with consideration beyond 10 years). (alban2025metastaticuvealmelanoma pages 7-9, alban2025metastaticuvealmelanoma pages 5-7)

---

## 9. Other species and model organisms
While detailed veterinary natural-disease epidemiology was not retrieved, the UM research ecosystem includes diverse model systems. A 2026 Cancer Research paper reports development of an immune-competent genetically engineered mouse model incorporating stepwise alterations (GNAQ Q209L expression, BAP1 deletion, MYC activation) that produces intraocular tumors and recapitulates features of aggressive class 2 UM, including immunosuppressive macrophage populations and exhausted T cells (supporting immunotherapy research). (paduszynska2024comprehensiveinsightsinto pages 11-13)

---

## 10. Recent developments (2023–2024 priority highlights)
1) **Prospective validation of integrated prognostic biomarkers (15-GEP + PRAME) at multi-center scale (COOG2; published Oct 2024)** enabling risk-adjusted surveillance and trial stratification. (harbour202415geneexpressionprofile pages 1-2, harbour202415geneexpressionprofile media 9fd22c19)
2) **Prospective ctDNA monitoring during tebentafusp therapy (published Oct 2024)** showing strong prognostic and predictive utility of ctDNA detectability and early reduction. (rodrigues2024prospectiveassessmentof pages 1-2)
3) **Radiotherapy comparative evidence synthesis (Apr 2024; Oct 2024)** refining when proton/charged-particle therapy may reduce local recurrence compared with plaque brachytherapy, while highlighting uncertainty in survival differences and complication tradeoffs. (tseng2024comparingefficacyof pages 1-2, semeniuk2024currentandemerging pages 2-3)
4) **Large registry-based UVR analysis (Feb 2024)** supporting the view that UVR risk is subsite-dependent (ciliary body/iris vs choroid), rather than uniformly causal across UM. (arockiaraj2024ambientultravioletradiation pages 1-2)

---

## 11. Data/statistics snapshot (for KB fields)
- US incidence (SEER 1975–2020): **5.6 per million/year**; 5-year relative survival **82.8%** (stable across decades). (weinberger2025uvealmelanoma5year pages 1-2)
- Hungary incidence (2012–2021): **6.40–10.96 per 1,000,000 person-years**. (toth2024incidenceandmortality pages 1-2)
- Metastasis risk stratification by TCGA class: **5-year distant metastasis 4% (A), 20% (B), 33% (C), 63% (D)**. (pasarica2024pathologicalandmolecular pages 1-2)
- Integrated 15-GEP/PRAME (COOG2): **5-year MFS 95.6% (class1/PRAME−) vs 44.8% (class2/PRAME+)**. (harbour202415geneexpressionprofile pages 1-2, harbour202415geneexpressionprofile media 9fd22c19)
- Tebentafusp ctDNA (prospective cohort): baseline ctDNA detectable → OS **12.9 vs 40.5 months**; ≥90% reduction at 12 weeks → OS **21.2 vs 12.9 months**. (rodrigues2024prospectiveassessmentof pages 1-2)

---

## Evidence type notes
- Registry epidemiology: SEER and national insurance datasets (human population-level). (weinberger2025uvealmelanoma5year pages 2-4, toth2024incidenceandmortality pages 1-2)
- Prognostic biomarkers: prospective multi-center cohort (human clinical). (harbour202415geneexpressionprofile pages 1-2)
- Tebentafusp outcomes/biomarkers: prospective cohort and phase 1/2 follow-up (human clinical). (rodrigues2024prospectiveassessmentof pages 1-2, sacco2024longtermsurvivalfollowup pages 1-2)
- Model organisms: genetically engineered mouse model (preclinical). (paduszynska2024comprehensiveinsightsinto pages 11-13)

---

## Key source URLs and publication dates (selected)
- Carvajal RD et al. **Jan 2023**, *Nat Rev Clin Oncol*: https://doi.org/10.1038/s41571-022-00714-1 (carvajal2023advancesinthe pages 5-7)
- Arockiaraj BM et al. **Feb 2024**, *Eye*: https://doi.org/10.1038/s41433-024-02959-9 (arockiaraj2024ambientultravioletradiation pages 1-2)
- Rodrigues M et al. **Oct 2024**, *Nat Commun*: https://doi.org/10.1038/s41467-024-53145-0 (rodrigues2024prospectiveassessmentof pages 1-2)
- Harbour JW et al. **Oct 2024**, *J Clin Oncol*: https://doi.org/10.1200/JCO.24.00447 (harbour202415geneexpressionprofile pages 1-2)
- Sacco JJ et al. **Jun 2024**, *J Immunother Cancer*: https://doi.org/10.1136/jitc-2024-009028 (sacco2024longtermsurvivalfollowup pages 1-2)
- Tseng Y-H et al. **Apr 2024**, *Eye*: https://doi.org/10.1038/s41433-024-03035-y (tseng2024comparingefficacyof pages 1-2)
- Weinberger Y et al. **Dec 2025**, *Ocular Oncol Pathol* (SEER update): https://doi.org/10.1159/000543151 (weinberger2025uvealmelanoma5year pages 1-2)


References

1. (pasarica2024pathologicalandmolecular pages 1-2): Mihai Adrian Păsărică, Paul Filip Curcă, Christiana Diana Maria Dragosloveanu, Alexandru Călin Grigorescu, and Cosmin Ionuț Nisipașu. Pathological and molecular diagnosis of uveal melanoma. Diagnostics, 14:958, May 2024. URL: https://doi.org/10.3390/diagnostics14090958, doi:10.3390/diagnostics14090958. This article has 11 citations.

2. (NCT07063875 chunk 1): Anthony Joshua, FRACP. Adding IL-2 to Tebentafusp to Eradicate Cancer Progression. St Vincent's Hospital, Sydney. 2025. ClinicalTrials.gov Identifier: NCT07063875

3. (weinberger2025uvealmelanoma5year pages 1-2): Yehonatan Weinberger, James Bena, and Arun D. Singh. Uveal melanoma: 5-year update on incidence, treatment, and survival (seer 1975–2020). Ocular Oncology and Pathology, 11:30-36, Dec 2025. URL: https://doi.org/10.1159/000543151, doi:10.1159/000543151. This article has 12 citations and is from a peer-reviewed journal.

4. (pasarica2024pathologicalandmolecular pages 2-4): Mihai Adrian Păsărică, Paul Filip Curcă, Christiana Diana Maria Dragosloveanu, Alexandru Călin Grigorescu, and Cosmin Ionuț Nisipașu. Pathological and molecular diagnosis of uveal melanoma. Diagnostics, 14:958, May 2024. URL: https://doi.org/10.3390/diagnostics14090958, doi:10.3390/diagnostics14090958. This article has 11 citations.

5. (lissak2024whatsetsuveal pages 1-3): Karina Lissak, Zuzanna Szczepaniak, Agata Konopka, Natalia Wdowiak, Martyna Choinka, Małgorzata Komarów, Dominika Karasińska, Jakub Kalisiak, Mateusz Koralewicz, Milena Orzeł, and Bartłomiej Orzeł. What sets uveal melanoma apart, and how can we address it? a comprehensive review of pathophysiology, diagnosis and treatment. Quality in Sport, 23:55123, Sep 2024. URL: https://doi.org/10.12775/qs.2024.23.55123, doi:10.12775/qs.2024.23.55123. This article has 1 citations.

6. (weinberger2025uvealmelanoma5year pages 2-4): Yehonatan Weinberger, James Bena, and Arun D. Singh. Uveal melanoma: 5-year update on incidence, treatment, and survival (seer 1975–2020). Ocular Oncology and Pathology, 11:30-36, Dec 2025. URL: https://doi.org/10.1159/000543151, doi:10.1159/000543151. This article has 12 citations and is from a peer-reviewed journal.

7. (toth2024incidenceandmortality pages 1-2): Gábor Tóth, Béla Muzsik, Attila Szajkó, Pál Kerber, Elek Dinya, Béla Csákány, Zoltán Zsolt Nagy, and János Németh. Incidence and mortality of uveal melanoma in hungary: a nationwide study. Cancers, 16:931, Feb 2024. URL: https://doi.org/10.3390/cancers16050931, doi:10.3390/cancers16050931. This article has 5 citations.

8. (iavarone2025ocularmelanomaa pages 4-6): Lucia Iavarone, Renato Franco, Federica Zito Marino, Giuseppe D’Abbronzo, Giuseppe Argenziano, Camila Scharf, Grazia Nucci, Andrea Ronchi, and Gerardo Cazzato. Ocular melanoma: a comprehensive review with a focus on molecular biology. International Journal of Molecular Sciences, 26:9799, Oct 2025. URL: https://doi.org/10.3390/ijms26199799, doi:10.3390/ijms26199799. This article has 6 citations.

9. (jager2020uvealmelanoma pages 2-3): Martine J. Jager, C. L. Shields, Colleen M. Cebulla, Mohamed H. Abdel-Rahman, Hans E. Grossniklaus, Marc-Henri Stern, Richard D. Carvajal, Rubens N. Belfort, Renbing Jia, J. A. Shields, and B. Damato. Uveal melanoma. Nature Reviews Disease Primers, 6:1-25, Apr 2020. URL: https://doi.org/10.1038/s41572-020-0158-0, doi:10.1038/s41572-020-0158-0. This article has 954 citations.

10. (arockiaraj2024ambientultravioletradiation pages 1-2): Basilica M. Arockiaraj, Elizabeth K. Cahoon, Michael R. Sargen, Erping Long, Margaret A. Tucker, and Jim Z. Mai. Ambient ultraviolet radiation and ocular melanoma incidence in the united states, 2000−2019. Eye, 38:1618-1625, Feb 2024. URL: https://doi.org/10.1038/s41433-024-02959-9, doi:10.1038/s41433-024-02959-9. This article has 14 citations and is from a peer-reviewed journal.

11. (repo2025germlinecancersusceptibility pages 1-3): P. Repo, Eveliina Jakkula, Juho Hiltunen, Heidi Putkuri, Aleksandra Staskiewicz‐Tuikkanen, Reetta‐Stiina Järvinen, M. Täll, V. Raivio, Ranaa Al-Jamal, T. Kivelä, and J. Turunen. Germline cancer susceptibility variants in patients with uveal melanoma. Pigment Cell & Melanoma Research, Aug 2025. URL: https://doi.org/10.1111/pcmr.70041, doi:10.1111/pcmr.70041. This article has 0 citations and is from a domain leading peer-reviewed journal.

12. (wadt2024characterizationofsomatic pages 1-2): Karin A. W. Wadt, Katja Harbst, Mette M. B. Sjøl, Frida Rosengren, Christina Westmose Yde, Kristoffer Staal Rohrberg, Marlene Richter Jensen, Steffen Heegaard, Jens Folke Kiilgaard, Anne-Marie Gerdes, Nicholas Hayward, and Göran B. Jönsson. Characterization of somatic mutations in sporadic uveal melanoma and uveal melanoma in patients with germline bap1 pathogenic variants. PLOS ONE, 19:e0306386, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0306386, doi:10.1371/journal.pone.0306386. This article has 1 citations and is from a peer-reviewed journal.

13. (fili2021presentingsymptomsare pages 1-2): Maria Fili, Stefan Seregard, and Gustav Stålhammar. Presenting symptoms are associated with uveal melanoma-related death. Ophthalmology, 128:1107-1109, Jul 2021. URL: https://doi.org/10.1016/j.ophtha.2020.11.023, doi:10.1016/j.ophtha.2020.11.023. This article has 11 citations and is from a highest quality peer-reviewed journal.

14. (sabazade2022vasculogenicmimicrycorrelates pages 1-3): Shiva Sabazade, Viktor Gill, Christina Herrspiegel, and Gustav Stålhammar. Vasculogenic mimicry correlates to presenting symptoms and mortality in uveal melanoma. Journal of Cancer Research and Clinical Oncology, 148:587-597, Nov 2022. URL: https://doi.org/10.1007/s00432-021-03851-9, doi:10.1007/s00432-021-03851-9. This article has 20 citations and is from a peer-reviewed journal.

15. (kaliki2017uvealmelanomarelatively pages 4-6): S Kaliki and C L Shields. Uveal melanoma: relatively rare but deadly cancer. Eye, 31:241-257, Feb 2017. URL: https://doi.org/10.1038/eye.2016.275, doi:10.1038/eye.2016.275. This article has 877 citations and is from a peer-reviewed journal.

16. (semeniuk2024currentandemerging pages 2-3): Oleksii Semeniuk, Esther Yu, and Mark J. Rivard. Current and emerging radiotherapy options for uveal melanoma. Cancers, 16:1074, Mar 2024. URL: https://doi.org/10.3390/cancers16051074, doi:10.3390/cancers16051074. This article has 14 citations.

17. (pasarica2024pathologicalandmolecular pages 9-10): Mihai Adrian Păsărică, Paul Filip Curcă, Christiana Diana Maria Dragosloveanu, Alexandru Călin Grigorescu, and Cosmin Ionuț Nisipașu. Pathological and molecular diagnosis of uveal melanoma. Diagnostics, 14:958, May 2024. URL: https://doi.org/10.3390/diagnostics14090958, doi:10.3390/diagnostics14090958. This article has 11 citations.

18. (ambrosio2026amultifacetedapproach pages 9-12): M Ambrosio. A multi-faceted approach to uncover novel vulnerabilities in uveal melanoma: from etiology to the identification of prognostic biomarkers. Unknown journal, 2026.

19. (kastelan2026precisiononcologyin pages 4-5): Snježana Kaštelan, Fanka Gilevska, Zora Tomić, Josipa Živko, and Tamara Nikuševa-Martić. Precision oncology in ocular melanoma: integrating molecular and liquid biopsy biomarkers. Current Issues in Molecular Biology, 48:131, Jan 2026. URL: https://doi.org/10.3390/cimb48020131, doi:10.3390/cimb48020131. This article has 0 citations.

20. (dore2026clinicalmolecularpathology pages 3-5): Stefano Dore, Matteo Sacchi, Antonio Pinna, Giuseppe Palmieri, and Panagiotis Paliogiannis. Clinical molecular pathology and treatment developments in advanced uveal melanoma: state of the art. Oncology Research, Jan 2026. URL: https://doi.org/10.32604/or.2025.071831, doi:10.32604/or.2025.071831. This article has 0 citations and is from a peer-reviewed journal.

21. (lamasfrancis2024impactofdriver pages 1-2): David Lamas-Francis, Carmen Antía Rodríguez-Fernández, Elia de Esteban-Maciñeira, Paula Silva-Rodríguez, María Pardo, Manuel Bande-Rodríguez, and María José Blanco-Teijeiro. Impact of driver mutations on metastasis-free survival in uveal melanoma: a meta-analysis. Cancers, 16:2510, Jul 2024. URL: https://doi.org/10.3390/cancers16142510, doi:10.3390/cancers16142510. This article has 4 citations.

22. (harbour202415geneexpressionprofile pages 5-6): J. William Harbour, Zelia M. Correa, Amy C. Schefler, Prithvi Mruthyunjaya, Miguel A. Materin, Thomas A. Aaberg, Alison H. Skalet, David A. Reichstein, Ezekiel Weis, Ivana K. Kim, Timothy S. Fuller, Hakan Demirci, Kisha D. Piggott, Basil K. Williams, Eugene Shildkrot, Antonio Capone, Scott C. Oliver, Scott D. Walter, John Mason, Devron H. Char, Michael Altaweel, Jill R. Wells, Jay S. Duker, Peter G. Hovland, Dan S. Gombos, Tony Tsai, Cameron Javid, Brian P. Marr, Ang Gao, Christina L. Decatur, James J. Dollar, Stefan Kurtenbach, and Song Zhang. 15-gene expression profile and <i>prame</i> as integrated prognostic test for uveal melanoma: first report of collaborative ocular oncology group study no. 2 (coog2.1). Journal of Clinical Oncology, 42:3319-3329, Oct 2024. URL: https://doi.org/10.1200/jco.24.00447, doi:10.1200/jco.24.00447. This article has 52 citations and is from a highest quality peer-reviewed journal.

23. (harbour202415geneexpressionprofile pages 17-18): J. William Harbour, Zelia M. Correa, Amy C. Schefler, Prithvi Mruthyunjaya, Miguel A. Materin, Thomas A. Aaberg, Alison H. Skalet, David A. Reichstein, Ezekiel Weis, Ivana K. Kim, Timothy S. Fuller, Hakan Demirci, Kisha D. Piggott, Basil K. Williams, Eugene Shildkrot, Antonio Capone, Scott C. Oliver, Scott D. Walter, John Mason, Devron H. Char, Michael Altaweel, Jill R. Wells, Jay S. Duker, Peter G. Hovland, Dan S. Gombos, Tony Tsai, Cameron Javid, Brian P. Marr, Ang Gao, Christina L. Decatur, James J. Dollar, Stefan Kurtenbach, and Song Zhang. 15-gene expression profile and <i>prame</i> as integrated prognostic test for uveal melanoma: first report of collaborative ocular oncology group study no. 2 (coog2.1). Journal of Clinical Oncology, 42:3319-3329, Oct 2024. URL: https://doi.org/10.1200/jco.24.00447, doi:10.1200/jco.24.00447. This article has 52 citations and is from a highest quality peer-reviewed journal.

24. (harbour202415geneexpressionprofile pages 1-2): J. William Harbour, Zelia M. Correa, Amy C. Schefler, Prithvi Mruthyunjaya, Miguel A. Materin, Thomas A. Aaberg, Alison H. Skalet, David A. Reichstein, Ezekiel Weis, Ivana K. Kim, Timothy S. Fuller, Hakan Demirci, Kisha D. Piggott, Basil K. Williams, Eugene Shildkrot, Antonio Capone, Scott C. Oliver, Scott D. Walter, John Mason, Devron H. Char, Michael Altaweel, Jill R. Wells, Jay S. Duker, Peter G. Hovland, Dan S. Gombos, Tony Tsai, Cameron Javid, Brian P. Marr, Ang Gao, Christina L. Decatur, James J. Dollar, Stefan Kurtenbach, and Song Zhang. 15-gene expression profile and <i>prame</i> as integrated prognostic test for uveal melanoma: first report of collaborative ocular oncology group study no. 2 (coog2.1). Journal of Clinical Oncology, 42:3319-3329, Oct 2024. URL: https://doi.org/10.1200/jco.24.00447, doi:10.1200/jco.24.00447. This article has 52 citations and is from a highest quality peer-reviewed journal.

25. (harbour202415geneexpressionprofile media 9fd22c19): J. William Harbour, Zelia M. Correa, Amy C. Schefler, Prithvi Mruthyunjaya, Miguel A. Materin, Thomas A. Aaberg, Alison H. Skalet, David A. Reichstein, Ezekiel Weis, Ivana K. Kim, Timothy S. Fuller, Hakan Demirci, Kisha D. Piggott, Basil K. Williams, Eugene Shildkrot, Antonio Capone, Scott C. Oliver, Scott D. Walter, John Mason, Devron H. Char, Michael Altaweel, Jill R. Wells, Jay S. Duker, Peter G. Hovland, Dan S. Gombos, Tony Tsai, Cameron Javid, Brian P. Marr, Ang Gao, Christina L. Decatur, James J. Dollar, Stefan Kurtenbach, and Song Zhang. 15-gene expression profile and <i>prame</i> as integrated prognostic test for uveal melanoma: first report of collaborative ocular oncology group study no. 2 (coog2.1). Journal of Clinical Oncology, 42:3319-3329, Oct 2024. URL: https://doi.org/10.1200/jco.24.00447, doi:10.1200/jco.24.00447. This article has 52 citations and is from a highest quality peer-reviewed journal.

26. (harbour202415geneexpressionprofile pages 2-4): J. William Harbour, Zelia M. Correa, Amy C. Schefler, Prithvi Mruthyunjaya, Miguel A. Materin, Thomas A. Aaberg, Alison H. Skalet, David A. Reichstein, Ezekiel Weis, Ivana K. Kim, Timothy S. Fuller, Hakan Demirci, Kisha D. Piggott, Basil K. Williams, Eugene Shildkrot, Antonio Capone, Scott C. Oliver, Scott D. Walter, John Mason, Devron H. Char, Michael Altaweel, Jill R. Wells, Jay S. Duker, Peter G. Hovland, Dan S. Gombos, Tony Tsai, Cameron Javid, Brian P. Marr, Ang Gao, Christina L. Decatur, James J. Dollar, Stefan Kurtenbach, and Song Zhang. 15-gene expression profile and <i>prame</i> as integrated prognostic test for uveal melanoma: first report of collaborative ocular oncology group study no. 2 (coog2.1). Journal of Clinical Oncology, 42:3319-3329, Oct 2024. URL: https://doi.org/10.1200/jco.24.00447, doi:10.1200/jco.24.00447. This article has 52 citations and is from a highest quality peer-reviewed journal.

27. (laliscia2024iodineplaquebrachytherapy pages 1-2): CONCETTA LALISCIA, FRANCO PERRONE, FEDERICA CRESTI, FRANCESCA GUIDO, TAIUSHA FUENTES, CECILIA TRIPPA, FABIOLA PAIAR, GUGLIELMO PELLEGRINI, and FEDERICA GENOVESI EBERT. Iodine plaque brachytherapy a customized conservative approach to the management of medium/large-sized uveal melanoma. In Vivo, 38:1814-1822, Jan 2024. URL: https://doi.org/10.21873/invivo.13633, doi:10.21873/invivo.13633. This article has 5 citations and is from a peer-reviewed journal.

28. (tseng2024comparingefficacyof pages 1-2): Yu-Hsuan Tseng, Chia-An Hsu, and Yu-Bai Chou. Comparing efficacy of charged-particle therapy with brachytherapy in treatment of uveal melanoma. Eye, 38:1882-1890, Apr 2024. URL: https://doi.org/10.1038/s41433-024-03035-y, doi:10.1038/s41433-024-03035-y. This article has 4 citations and is from a peer-reviewed journal.

29. (chan2024protontherapyin pages 6-7): Adrian Wai Chan, Haibo Lin, Irini Yacoub, Arpit M. Chhabra, J. Isabelle Choi, and Charles B. Simone. Proton therapy in uveal melanoma. Cancers, 16:3497, Oct 2024. URL: https://doi.org/10.3390/cancers16203497, doi:10.3390/cancers16203497. This article has 19 citations.

30. (miao2025efficacyandsafety pages 1-2): Yuxin Miao, Tingwei Zheng, Qiuning Zhang, Meixuan Li, Qihang Lei, Qin Liu, Hongtao Luo, and Huiling Bai. Efficacy and safety of proton radiotherapy in treating choroidal melanoma: a systematic review and meta-analysis. Radiation Oncology (London, England), Jan 2025. URL: https://doi.org/10.1186/s13014-024-02580-w, doi:10.1186/s13014-024-02580-w. This article has 7 citations.

31. (saldanha2025howwetreat pages 1-2): E.F. Saldanha, M.F. Ribeiro, I. Hirsch, A. Spreafico, S.D. Saibil, and M.O. Butler. How we treat patients with metastatic uveal melanoma. ESMO Open, 10:104496, Apr 2025. URL: https://doi.org/10.1016/j.esmoop.2025.104496, doi:10.1016/j.esmoop.2025.104496. This article has 12 citations and is from a domain leading peer-reviewed journal.

32. (rodrigues2024prospectiveassessmentof pages 1-2): Manuel Rodrigues, Toulsie Ramtohul, Aurore Rampanou, José Luis Sandoval, Alexandre Houy, Vincent Servois, Léah Mailly-Giacchetti, Gaelle Pierron, Anne Vincent-Salomon, Nathalie Cassoux, Pascale Mariani, Caroline Dutriaux, Marc Pracht, Thomas Ryckewaert, Jean-Emmanuel Kurtz, Sergio Roman-Roman, Sophie Piperno-Neumann, François-Clément Bidard, Marc-Henri Stern, and Shufang Renault. Prospective assessment of circulating tumor dna in patients with metastatic uveal melanoma treated with tebentafusp. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53145-0, doi:10.1038/s41467-024-53145-0. This article has 30 citations and is from a highest quality peer-reviewed journal.

33. (sacco2024longtermsurvivalfollowup pages 1-2): Joseph J Sacco, Richard D Carvajal, Marcus O Butler, Alexander N Shoushtari, Jessica C Hassel, Alexandra Ikeguchi, Leonel Hernandez-Aya, Paul Nathan, Omid Hamid, Josep M Piulats, Matthew Rioth, Douglas B Johnson, Jason J Luke, Enrique Espinosa, Serge Leyvraz, Laura Collins, Chris Holland, and Takami Sato. Long-term survival follow-up for tebentafusp in previously treated metastatic uveal melanoma. Journal for Immunotherapy of Cancer, 12:e009028, Jun 2024. URL: https://doi.org/10.1136/jitc-2024-009028, doi:10.1136/jitc-2024-009028. This article has 33 citations and is from a domain leading peer-reviewed journal.

34. (wang2025evaluatingtheefficacy pages 1-2): Yanlin Wang, Wen Sun, and Bing Wang. Evaluating the efficacy and safety of tebentafusp in the treatment of metastatic uveal melanoma: a 2025 update systematic review and meta-analysis. Frontiers in Oncology, Oct 2025. URL: https://doi.org/10.3389/fonc.2025.1667282, doi:10.3389/fonc.2025.1667282. This article has 4 citations.

35. (wang2025evaluatingtheefficacy pages 7-10): Yanlin Wang, Wen Sun, and Bing Wang. Evaluating the efficacy and safety of tebentafusp in the treatment of metastatic uveal melanoma: a 2025 update systematic review and meta-analysis. Frontiers in Oncology, Oct 2025. URL: https://doi.org/10.3389/fonc.2025.1667282, doi:10.3389/fonc.2025.1667282. This article has 4 citations.

36. (carvajal2023advancesinthe pages 5-7): Richard D. Carvajal, Joseph J. Sacco, Martine J. Jager, David J. Eschelman, Roger Olofsson Bagge, J. William Harbour, Nicholas D. Chieng, Sapna P. Patel, Anthony M. Joshua, and Sophie Piperno-Neumann. Advances in the clinical management of uveal melanoma. Nature Reviews Clinical Oncology, 20:99-115, Jan 2023. URL: https://doi.org/10.1038/s41571-022-00714-1, doi:10.1038/s41571-022-00714-1. This article has 267 citations and is from a domain leading peer-reviewed journal.

37. (alban2025metastaticuvealmelanoma pages 7-9): Juan Alban, R. Christopher Bowen, David A. Reichstein, Meredith McKean, Jose Lutzky, Ezekiel Weis, Richard D. Carvajal, Susan Dulka, Brian G. Morse, Marcus O. Butler, Suthee Rapisuwon, Kevin B. Kim, Sanjay Chandrasekaran, Allison Betof Warner, Jonathan S. Zager, Bartosz Chmielowski, Sapna P. Patel, Leonel Fernando Hernandez-Aya, Zelia M. Correa, Leslie A. Fecher, Yana G. Najjar, Kamaneh Montazeri, Alexander N. Shoushtari, Asad Javed, Dan S. Gombos, April K. S. Salama, Katy Tsai, Frank H. Miller, Nikhil Khushalani, Rino S. Seedor, Evan J. Lipson, Sunil A. Reddy, Elizabeth Buchbinder, Shailender Bhatia, Anna Pavlick, Inderjit Mehmi, Thomas Aaberg, Alexandra P. Ikeguchi, Ivana K. Kim, Scott D. Walter, Arun D. Singh, Ryan J. Sullivan, Jacob S. Choi, Basil K. Williams Jr., Marlana Orloff, Prithvi Mruthyunjaya, Megan D. Schollenberger, Namita Gandhi, J. William Harbour, and Sunandana Chandra. Metastatic uveal melanoma surveillance: a delphi panel consensus. Cancers, 18:121, Dec 2025. URL: https://doi.org/10.3390/cancers18010121, doi:10.3390/cancers18010121. This article has 0 citations.

38. (alban2025metastaticuvealmelanoma pages 5-7): Juan Alban, R. Christopher Bowen, David A. Reichstein, Meredith McKean, Jose Lutzky, Ezekiel Weis, Richard D. Carvajal, Susan Dulka, Brian G. Morse, Marcus O. Butler, Suthee Rapisuwon, Kevin B. Kim, Sanjay Chandrasekaran, Allison Betof Warner, Jonathan S. Zager, Bartosz Chmielowski, Sapna P. Patel, Leonel Fernando Hernandez-Aya, Zelia M. Correa, Leslie A. Fecher, Yana G. Najjar, Kamaneh Montazeri, Alexander N. Shoushtari, Asad Javed, Dan S. Gombos, April K. S. Salama, Katy Tsai, Frank H. Miller, Nikhil Khushalani, Rino S. Seedor, Evan J. Lipson, Sunil A. Reddy, Elizabeth Buchbinder, Shailender Bhatia, Anna Pavlick, Inderjit Mehmi, Thomas Aaberg, Alexandra P. Ikeguchi, Ivana K. Kim, Scott D. Walter, Arun D. Singh, Ryan J. Sullivan, Jacob S. Choi, Basil K. Williams Jr., Marlana Orloff, Prithvi Mruthyunjaya, Megan D. Schollenberger, Namita Gandhi, J. William Harbour, and Sunandana Chandra. Metastatic uveal melanoma surveillance: a delphi panel consensus. Cancers, 18:121, Dec 2025. URL: https://doi.org/10.3390/cancers18010121, doi:10.3390/cancers18010121. This article has 0 citations.

39. (paduszynska2024comprehensiveinsightsinto pages 11-13): N Paduszyńska, A Dąbrowska, and MJ Gonciarz. Comprehensive insights into uveal melanoma–risk factors, pathophysiology, prognosis, and diagnostic approaches. Unknown journal, 2024.
