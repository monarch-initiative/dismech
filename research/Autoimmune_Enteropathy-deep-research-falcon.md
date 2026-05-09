---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T15:07:29.268498'
end_time: '2026-05-07T15:23:21.055685'
duration_seconds: 951.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autoimmune Enteropathy
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autoimmune Enteropathy
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Autoimmune Enteropathy** covering all of the
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
- **Disease Name:** Autoimmune Enteropathy
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Autoimmune Enteropathy** covering all of the
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


# Autoimmune Enteropathy (AIE) — Disease Characteristics Research Report

## Executive summary
Autoimmune enteropathy (AIE) is a rare immune-mediated enteropathy defined by chronic/protracted diarrhea with malabsorption and characteristic small-intestinal mucosal injury (villous blunting/atrophy with crypt injury), after exclusion of more common causes of villous atrophy such as celiac disease and infection (shihaz2022autoimmuneenteropathyin pages 1-6, gentile2012autoimmuneenteropathya pages 2-4, umetsu2018autoimmuneenteropathies pages 1-2). Contemporary adult cohorts emphasize that AIE often presents as secretory, high-volume watery diarrhea with severe nutritional consequences and frequent need for corticosteroids and steroid-sparing immunosuppression, yet long-term outcomes remain unsatisfactory with substantial relapse risk (li2024clinicalmanifestationsdiagnosis pages 9-11, li2025comprehensiveinsightsinto pages 3-4).

A key recent development (2024) is a 16-patient adult cohort from Peking Union Medical College Hospital that quantified histopathology and outcomes and highlighted goblet/Paneth cell depletion and neutrophilic crypt injury as potentially useful diagnostic clues in adults, especially when anti-enterocyte antibodies are undetectable (li2024clinicalmanifestationsdiagnosis pages 9-11, li2024clinicalmanifestationsdiagnosis media 05afd713, li2024clinicalmanifestationsdiagnosis media ec9b1a39). A second recent development (2023–2025) is the growing use of genotype-informed diagnosis and targeted therapy in immune dysregulation syndromes that can manifest as AIE (e.g., CTLA4/LRBA with abatacept; STAT3 gain-of-function with pathway-directed therapy), supported by expanding sequencing-based yields in “AIE” case series and IPEX/IPEX-like cohorts (li2025comprehensiveinsightsinto pages 1-2, gambineri2018clinicalimmunologicaland pages 1-2).

## 1. Disease information

### 1.1 Definition and overview
AIE is described as “an uncommon to rare clinical entity characterized by intractable diarrhoea, varying levels of villous atrophy of the small intestine, [and] presence of circulating auto antibodies to enterocytes” (quote) (shihaz2022autoimmuneenteropathyin pages 1-6). It is considered among the major differentials of seronegative villous atrophy and refractory diarrhea and may involve small bowel predominantly, but gastric and colonic involvement can occur (shihaz2022autoimmuneenteropathyin pages 1-6, shihaz2022autoimmuneenteropathyin pages 6-10).

### 1.2 Key identifiers / ontologies
* **MeSH (ClinicalTrials.gov browse term):** Autoimmune enteropathy (MeSH-like browse term shown in NCT record) (NCT04280510 chunk 1).
* **MONDO ID / OMIM / Orphanet / ICD-10/11:** Not reliably retrievable from the tool-accessible corpus used here; these are typically obtained from MONDO/Orphanet/OMIM pages and coding references, which were not available in the retrieved texts.

### 1.3 Synonyms / alternative names
* Autoimmune enteropathy (AIE) (shihaz2022autoimmuneenteropathyin pages 1-6, umetsu2018autoimmuneenteropathies pages 1-2)
* Autoimmune enteritis (used variably in the literature and clinical trial context) (NCT00258180 chunk 1)

### 1.4 Evidence source type
The evidence in this report is derived from aggregated disease-level resources (reviews and cohorts) and individual case reports, rather than EHR-only sources (gentile2012autoimmuneenteropathya pages 2-4, li2024clinicalmanifestationsdiagnosis pages 9-11, li2025comprehensiveinsightsinto pages 3-4).

## 2. Etiology

### 2.1 Disease causal factors
AIE is heterogeneous. A major etiologic theme is immune dysregulation with loss of tolerance at the intestinal mucosa; monogenic immune regulatory disorders frequently manifest with “AIE-like” enteropathy, especially with early onset (umetsu2018autoimmuneenteropathies pages 1-2, chen2020areviewof pages 2-4, gambineri2018clinicalimmunologicaland pages 1-2).

A recent adult AIE synthesis states (abstract quote): “Pathogenesis might involve genetic predisposition, aberrant immune homeostasis, comorbidities of autoimmune diseases and environmental trigger.” (li2025comprehensiveinsightsinto pages 1-2).

### 2.2 Risk factors
**Genetic / syndromic risk factors (primary immune regulatory disorders):**
* **FOXP3 (IPEX syndrome, X-linked):** IPEX is a prototypic syndromic cause; FOXP3 encodes a transcription factor required for thymus-derived regulatory T cells (Tregs), and “tTreg cell dysfunction is the main pathogenic event” (abstract quote) (arienzo2025paediatriccongenitalenteropathies pages 8-10, gambineri2018clinicalimmunologicaland pages 1-2). A review of AIE-associated syndromes notes “to date, over 70 mutations have been identified in the FOXP3 gene” (chen2020areviewof pages 2-4).
* **CTLA4 haploinsufficiency (dominant) and LRBA deficiency (recessive):** LRBA deficiency presents with immune dysregulation/enteropathy and overlaps clinically with CTLA4 haploinsufficiency; LRBA impacts CTLA-4 biology (chen2020areviewof pages 2-4). In a 26-patient Tregopathy series, LRBA was the most frequent diagnosis (13/26), with CTLA4 defects in 5/26 (iyengar2025tregopathyinfocus pages 5-7).
* **STAT3 gain-of-function (GOF):** A 2023 review describes STAT3-GOF as a multi-organ immune regulatory disorder and lists enteropathy among manifestations (abstract quote: “disease … can encompass a wide range of clinical manifestations such as: enteropathy…”) (shihaz2022autoimmuneenteropathyin pages 6-10).
* **AIRE (APECED/APS-1):** APECED is a monogenic central tolerance disorder; GI/enteropathy can be part of the phenotype, and autoantibodies linked to GI dysfunction (e.g., TPH antibodies) are reported (enache2025diagnosticchallengesin pages 8-10).

**Comorbid immunodeficiency/autoimmunity:** AIE often co-occurs with other autoimmune disease and immunodeficiency (e.g., CVID). One adult review reports ~18% concurrent CVID and ~80% predisposition to autoimmunity (shihaz2022autoimmuneenteropathyin pages 1-6).

### 2.3 Protective factors
No specific protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Direct gene–environment interaction evidence was not identified in the retrieved corpus; however, reviews acknowledge possible “environmental trigger” in adult AIE pathogenesis (li2025comprehensiveinsightsinto pages 1-2).

## 3. Phenotypes

### 3.1 Core gastrointestinal phenotype
Across cohorts and reviews, the dominant phenotype is **chronic, profuse watery diarrhea** with malabsorption and marked nutritional impact (shihaz2022autoimmuneenteropathyin pages 1-6, umetsu2018autoimmuneenteropathies pages 1-2, li2025comprehensiveinsightsinto pages 3-4).

**Adult quantitative phenotype (case-review of 208 adults):**
* Stool frequency **≥10/day in 83%**; daily volume up to **1,000–10,000 mL** (li2025comprehensiveinsightsinto pages 3-4).
* Median weight loss **16.0 kg** (IQR 10.0–25.8) (li2025comprehensiveinsightsinto pages 3-4).
* Gluten-free diet ineffective in **86%** of tested cases (li2025comprehensiveinsightsinto pages 3-4).

**Adult cohort phenotype (Peking cohort, 2011–2023; n=16):**
* Diarrhea described as **secretory diarrhea** (li2024clinicalmanifestationsdiagnosis pages 9-11).

**Pediatric phenotype:**
Pediatric AIE most commonly presents in infancy (often within first 6 months) with severe/intractable diarrhea and failure to thrive (umetsu2018autoimmuneenteropathies pages 1-2). A review of AIE and transplant highlights that pediatric diarrhea may be extremely voluminous (reported up to ~5000 mL/day) and is often non-bloody; electrolyte abnormalities and inability to tolerate feeds are common and parenteral nutrition may be required (ahmed2019autoimmuneenteropathyan pages 1-2).

### 3.2 Extra-intestinal phenotypes (autoimmunity/immune dysregulation)
AIE frequently occurs with extra-intestinal autoimmune disease, particularly in syndromic/monogenic contexts (umetsu2018autoimmuneenteropathies pages 1-2, gentile2012autoimmuneenteropathya pages 1-2). Examples include endocrinopathies (type 1 diabetes, thyroiditis), autoimmune hepatitis, hematologic autoimmunity, and renal disease (umetsu2018autoimmuneenteropathies pages 1-2, gentile2012autoimmuneenteropathya pages 1-2).

In a 40-patient AIE cohort (age 2 months–73 years), onset was “uniformly with secretory-type diarrhea” and multiple immune/autoimmune comorbidities were reported (e.g., CVID/hypogammaglobulinemia, uveitis, hepatitis, cholangitis, adrenal insufficiency, glomerulopathy) (villanacci2019clinicalmanifestationsand pages 2-3).

### 3.3 Laboratory abnormalities
Adult reviews report nutritional and systemic abnormalities such as fat-soluble vitamin deficiencies (up to 90%), elevated transaminases (up to 67%), and mild hypogammaglobulinemia (up to 33%) (shihaz2022autoimmuneenteropathyin pages 6-10).

### 3.4 Suggested HPO terms (examples)
* Chronic diarrhea: **HP:0002014**
* Secretory diarrhea: (no single canonical HPO term; use **HP:0002014** plus clinical annotation)
* Malabsorption: **HP:0002024**
* Weight loss: **HP:0001824**
* Failure to thrive: **HP:0001508**
* Protein-losing enteropathy / hypoalbuminemia (if present): **HP:0003073** (hypoalbuminemia)
* Villous atrophy: **HP:0031079** (if used in your HPO version; otherwise capture under abnormal small intestinal morphology)
* Autoimmune hepatitis: **HP:0005390**
* Type 1 diabetes mellitus: **HP:0100651**
* Autoimmune thyroiditis / hypothyroidism: **HP:0000821**

(These term IDs are provided as ontology suggestions; confirm exact IDs against the HPO release used by your knowledge base.)

## 4. Genetic / molecular information

### 4.1 Causal genes and inheritance patterns (syndromic/monogenic AIE)
* **FOXP3 (IPEX):** X-linked (hemizygous males). In a large cohort of 173 patients with an IPEX phenotype, **44 distinct FOXP3 variants** were identified among **88 FOXP3-positive** cases (9 novel) (gambineri2018clinicalimmunologicaland pages 1-2).
* **LRBA deficiency:** Autosomal recessive; characterized as immune dysregulation with enteropathy and reduced CTLA4 levels (chen2020areviewof pages 2-4).
* **CTLA4 haploinsufficiency:** Autosomal dominant; immune dysregulation with enteropathy; targeted therapy is clinically used (chen2020areviewof pages 2-4, iyengar2025tregopathyinfocus pages 5-7).
* **STAT3 GOF:** Autosomal dominant immune dysregulation syndrome with enteropathy among the clinical spectrum (shihaz2022autoimmuneenteropathyin pages 6-10).
* **AIRE (APECED/APS-1):** Central tolerance defect with GI manifestations in subsets; associated autoantibodies include TPH antibodies linked to GI dysfunction (enache2025diagnosticchallengesin pages 8-10).

### 4.2 Genetic testing yield in “adult AIE” cohorts
A recent adult AIE review reported that genetic screening found pathogenic variants in **20/48 (41.6%)** AIE patients, including CTLA4, STAT3, LRBA, STAT1 and others (li2025comprehensiveinsightsinto pages 1-2). This supports an emerging practice: when adult AIE is diagnosed (especially with systemic features), targeted panels or exome sequencing can identify actionable immune regulatory disorders (li2025comprehensiveinsightsinto pages 1-2).

### 4.3 Variant classes and functional consequences (high-level)
Detailed variant-by-variant classification (ACMG pathogenicity, allele frequency in gnomAD, etc.) was not extractable from the retrieved evidence; the cohort evidence above supports that diverse variant classes exist across immune regulatory genes (gambineri2018clinicalimmunologicaland pages 1-2).

### 4.4 Suggested MONDO/GO/CL ontology hooks (examples)
* **Cell types (Cell Ontology, CL):** regulatory T cell (**CL:0000815**), CD4-positive T cell (**CL:0000624**), B cell (**CL:0000236**), intestinal epithelial cell / enterocyte (use appropriate CL/Uberon-linked cell types)
* **GO biological processes:** immune tolerance, regulation of T cell activation, apoptotic process, inflammatory response (supported conceptually by immune-dysregulation mechanisms and crypt apoptosis) (arienzo2025paediatriccongenitalenteropathies pages 8-10, iyengar2025tregopathyinfocus pages 5-7)

(Confirm term IDs against the versions used in your ontology pipeline.)

## 5. Environmental information
No robust environmental toxin/lifestyle/infectious triggers were identified as causal from the retrieved corpus; infectious causes are primarily part of the **differential diagnosis** and are typically excluded in AIE workups (ahmed2019autoimmuneenteropathyan pages 1-2, gentile2012autoimmuneenteropathya pages 1-2).

## 6. Mechanism / pathophysiology

### 6.1 Current understanding (causal chain)
AIE is thought to arise from breakdown of immune tolerance at the intestinal mucosa, often involving defective regulatory pathways (FOXP3/Tregs; CTLA4 checkpoint function; LRBA-mediated CTLA4 trafficking), leading to dysregulated effector immune responses and epithelial injury (chen2020areviewof pages 2-4, gambineri2018clinicalimmunologicaland pages 1-2, iyengar2025tregopathyinfocus pages 5-7). The histologic consequence is villous blunting/atrophy with crypt injury and apoptosis, accompanied by mucosal inflammation; goblet and Paneth cell depletion are often observed (gentile2012autoimmuneenteropathya pages 2-4, li2024clinicalmanifestationsdiagnosis pages 9-11).

### 6.2 Pathways and immune components
* **Treg dysfunction:** FOXP3 is required for Treg maintenance; IPEX exemplifies systemic autoimmunity driven by Treg dysfunction (abstract quote: “tTreg cell dysfunction is the main pathogenic event…”) (arienzo2025paediatriccongenitalenteropathies pages 8-10).
* **CTLA4 pathway:** CTLA4 acts as an inhibitory checkpoint supporting peripheral tolerance (chen2020areviewof pages 2-4). LRBA regulates intracellular vesicle trafficking and “maintains [CTLA4] intracellular stores,” explaining reduced functional CTLA4 and immune dysregulation (iyengar2025tregopathyinfocus pages 5-7).
* **STAT3 GOF signaling:** STAT3 GOF is associated with effector T cell accumulation and decreased Tregs, contributing to autoimmunity including enteropathy (shihaz2022autoimmuneenteropathyin pages 6-10).

### 6.3 Suggested GO terms and CL terms
* **GO:** regulation of T cell activation; immune tolerance; epithelial cell apoptotic process; leukocyte migration; inflammatory response.
* **CL:** regulatory T cell (Treg), CD4 T cell, CD8 T cell, plasma cell (as a differential when absent in CVID-associated enteropathy), intestinal epithelial cell.

## 7. Anatomical structures affected

### 7.1 Organ/system level
Primary involvement is the **small intestine** (duodenum/ileum often biopsied), with possible stomach and colon involvement (shihaz2022autoimmuneenteropathyin pages 1-6, shihaz2022autoimmuneenteropathyin pages 6-10). Endoscopic abnormalities include edema, villous blunting, mucosal hyperemia in duodenum/ileum (li2024clinicalmanifestationsdiagnosis pages 9-11).

### 7.2 Tissue/cell level
The key target tissue is intestinal mucosa/epithelium, with enterocyte injury and crypt apoptosis; goblet and Paneth cell depletion is frequent (li2024clinicalmanifestationsdiagnosis pages 9-11).

**UBERON suggestions (examples):** small intestine (UBERON:0002108), duodenum (UBERON:0002114), ileum (UBERON:0002116), intestinal epithelium.

## 8. Temporal development

### 8.1 Onset
* **Pediatric:** typically within the first 6 months (often weeks of life), frequently severe and life-threatening (ahmed2019autoimmuneenteropathyan pages 1-2, umetsu2018autoimmuneenteropathies pages 1-2).
* **Adult:** median age at diagnosis reported around 49–55 years with diagnostic delay (median symptom duration 1.5 years in one series) (umetsu2018autoimmuneenteropathies pages 1-2, li2025comprehensiveinsightsinto pages 3-4).

### 8.2 Progression/course
Course can be chronic and relapsing. In a 16-patient adult cohort, relapse-free survival declined over time: **62.5% (6 months), 55.6% (12 months), 37.0% (48 months)** (li2024clinicalmanifestationsdiagnosis pages 9-11).

## 9. Inheritance and population

### 9.1 Epidemiology
AIE is extremely rare; pediatric incidence is estimated at **<1/100,000** (umetsu2018autoimmuneenteropathies pages 1-2). Precise adult prevalence is not established.

### 9.2 Inheritance patterns (for genetic etiologies)
* FOXP3/IPEX: X-linked (gambineri2018clinicalimmunologicaland pages 1-2)
* LRBA deficiency: autosomal recessive (chen2020areviewof pages 2-4)
* CTLA4 haploinsufficiency: autosomal dominant (chen2020areviewof pages 2-4)
* AIRE/APECED: classically autosomal recessive (central tolerance defect) (enache2025diagnosticchallengesin pages 8-10)
* STAT3 GOF: often autosomal dominant in reported syndromic disease (supported by “germline” GOF framing in the review) (shihaz2022autoimmuneenteropathyin pages 6-10)

## 10. Diagnostics

### 10.1 Clinical criteria and evolving diagnostic frameworks
AIE diagnostic criteria historically included protracted diarrhea refractory to diet, autoimmunity/autoantibodies, and absence of severe immunodeficiency (shihaz2022autoimmuneenteropathyin pages 1-6, villanacci2019clinicalmanifestationsand pages 1-2). A 2024 adult cohort notes that diagnosis was based on “the 2007 diagnostic criteria” and discusses later iterations (2018, 2022) with emphasis on histology and supporting features (li2024clinicalmanifestationsdiagnosis pages 9-11).

### 10.2 Histopathology (key data)
AIE histology often features villous atrophy/blunting with crypt injury (crypt lymphocytosis, apoptotic bodies), relative paucity of surface IELs (compared with classic celiac), and goblet/Paneth cell loss (gentile2012autoimmuneenteropathya pages 2-4, li2024clinicalmanifestationsdiagnosis pages 9-11).

**Adult cohort quantitative histology (Li 2024, n=16):**
* Villous blunting **100%**
* Deep crypt lymphocytic infiltration **67%**
* Apoptotic bodies **50%**
* Mild intraepithelial lymphocytosis **69%**
* Reduced/absent goblet cells (duodenum) **94%**
* Reduced/absent Paneth cells (duodenum) **94%**
* Neutrophil infiltration (duodenum) **100%** (li2024clinicalmanifestationsdiagnosis pages 9-11)

Figure/Table evidence from this paper includes a table of diagnostic criteria and a figure summarizing histopathology frequencies (li2024clinicalmanifestationsdiagnosis media 05afd713, li2024clinicalmanifestationsdiagnosis media ec9b1a39).

### 10.3 Autoantibodies
Anti-enterocyte and anti-goblet cell antibodies are considered supportive but imperfect; sensitivity/specificity are incompletely defined and positivity can occur in other conditions (IBD, HIV, allergic enteropathy, celiac disease) (gentile2012autoimmuneenteropathya pages 2-4, enache2025diagnosticchallengesin pages 8-10).

**Adult AIE case-review (208 adults):** AE antibody positive **52%**, AG antibody positive **13%** (li2025comprehensiveinsightsinto pages 3-4).

### 10.4 Differential diagnosis
Major differentials include:
* Celiac disease (including seronegative or refractory forms)
* CVID enteropathy / immunodeficiency-associated enteropathy
* Drug-induced immune-mediated enteropathy (e.g., checkpoint inhibitor injury)
* Infectious enteritis
* GVHD-like injury patterns (particularly in transplant settings)
(umetsu2018autoimmuneenteropathies pages 1-2)

### 10.5 Genetic testing strategy (current implementation)
Given overlap with IPEX-like disorders and meaningful therapeutic implications (e.g., abatacept for CTLA4/LRBA defects), next-generation sequencing panels or exome sequencing are increasingly relevant when AIE is severe, early-onset, refractory, or accompanied by multi-system autoimmunity/immunodeficiency (li2025comprehensiveinsightsinto pages 1-2, gambineri2018clinicalimmunologicaland pages 1-2).

## 11. Outcome / prognosis

### 11.1 Adult outcomes (statistics)
* Adult cohort (n=16): **2 deaths** from multiple organ failure; **1 non-Hodgkin lymphoma** during follow-up; relapse-free survival **62.5% (6 mo), 55.6% (12 mo), 37.0% (48 mo)** (li2024clinicalmanifestationsdiagnosis pages 9-11).
* Adult case-review (208 adults): **14% mortality** reported (li2025comprehensiveinsightsinto pages 3-4).

### 11.2 Prognostic factors
Robust prognostic biomarkers were not definitively extractable from the retrieved evidence, although the adult cohort suggested that certain histopathologic features (e.g., goblet/Paneth cell depletion) may have diagnostic/prognostic relevance (li2024clinicalmanifestationsdiagnosis pages 9-11).

## 12. Treatment

### 12.1 First-line and conventional immunosuppression
Corticosteroids are a common first-line therapy (shihaz2022autoimmuneenteropathyin pages 1-6, gentile2012autoimmuneenteropathya pages 1-2). In the 16-patient adult cohort, “All patients received glucocorticoid therapy as the initial medication,” and **14/16** achieved clinical response in a median of **5 days (IQR 3–20)** (abstract quote) (li2024clinicalmanifestationsdiagnosis pages 9-11). Immunosuppressants are commonly added for steroid dependence or refractory disease (li2024clinicalmanifestationsdiagnosis pages 9-11, shihaz2022autoimmuneenteropathyin pages 6-10).

**MAXO suggestions (examples):** systemic glucocorticoid therapy; immunosuppressive agent therapy; total parenteral nutrition.

### 12.2 Targeted/precision therapy in monogenic immune dysregulation
**Abatacept (CTLA4-Ig):** A 2023 case report describes a patient with immune-mediated enteropathy with CTLA4/LRBA variants and reports rapid clinical and laboratory regression with abatacept, supporting CTLA4-pathway targeting in severe disease (shihaz2022autoimmuneenteropathyin pages 6-10).

**HSCT:** For IPEX and some severe immune dysregulation disorders, HSCT is described as the only known effective cure in classic IPEX-focused reviews (arienzo2025paediatriccongenitalenteropathies pages 8-10), and HSCT is discussed as definitive for IPEX-associated disease in AIE-oriented reviews (shihaz2022autoimmuneenteropathyin pages 6-10).

### 12.3 Supportive and nutritional care
Severe malnutrition and need for parenteral nutrition are common, especially in severe pediatric disease and in adult cases with high-volume secretory diarrhea (ahmed2019autoimmuneenteropathyan pages 1-2, umetsu2018autoimmuneenteropathies pages 1-2, li2025comprehensiveinsightsinto pages 3-4).

## 13. Prevention
No established primary prevention strategies are identified; emphasis is on early recognition in high-risk contexts (early-onset polyautoimmunity, immunodeficiency, refractory villous atrophy) and timely genetic diagnosis to enable targeted treatment (li2025comprehensiveinsightsinto pages 1-2, gambineri2018clinicalimmunologicaland pages 1-2).

## 14. Other species / natural disease
No naturally occurring animal disease analogs were identified in the retrieved evidence corpus.

## 15. Model organisms
Classic mechanistic inference frequently references the **scurfy mouse** model (Foxp3 deficiency) as an immune dysregulation model relevant to IPEX-like enteropathy (gambineri2018clinicalimmunologicaland pages 1-2). Detailed model organism phenotype mapping was not available in the retrieved excerpts.

## Recent developments and expert analysis (prioritizing 2023–2024)

### 2024 — adult cohort refining histologic diagnostic clues and outcomes
Li et al. (World Journal of Gastroenterology; May 2024) provide updated adult AIE histology quantitation and outcomes. Their abstract highlights frequent goblet and Paneth cell depletion and notes that patients “fulfilled the 2018 diagnostic criteria but did not match the 2022 diagnostic criteria due to undetectable anti-enterocyte antibodies,” supporting a pragmatic, histology-forward diagnostic approach when serology is negative (li2024clinicalmanifestationsdiagnosis pages 9-11). This paper’s Table/Figure summary is available in extracted images (li2024clinicalmanifestationsdiagnosis media 05afd713, li2024clinicalmanifestationsdiagnosis media ec9b1a39).

### 2023 — targeted therapy for CTLA4-pathway disease
A 2023 case report of abatacept in immune-mediated enteropathy with CTLA4/LRBA variants argues for early consideration of abatacept in severe disease pending further testing (shihaz2022autoimmuneenteropathyin pages 6-10). While case-report evidence is low-level, it aligns with the increasingly accepted paradigm that “genetic diagnosis guides treatment” in immune dysregulation-associated enteropathies (concept supported by the adult AIE genetics review and IPEX-like cohorts) (li2025comprehensiveinsightsinto pages 1-2, gambineri2018clinicalimmunologicaland pages 1-2).

### 2023 — APECED cohorts highlight GI autoimmunity as an early diagnostic clue
A Frontiers in Immunology 2023 cohort of pediatric APECED patients with GI manifestations notes that expanded diagnostic criteria could allow earlier recognition when non-endocrine manifestations (including gastro-enteropathy) appear early, emphasizing the need to consider autoimmune enteropathy within broader immune dysregulation syndromes (shihaz2022autoimmuneenteropathyin pages 6-10).

## Clinical trials and real-world research programs
* **NCT04280510 (ENTEROPATH):** Prospective observational cohort (France; start 2020-02-27; recruiting as of 2025-09) studying mechanisms of immune enteropathies, including autoimmune enteropathy, with targeted sequencing, immune profiling, and biopsy-based analyses; target enrollment **200** adults (NCT04280510 chunk 1). URL: https://clinicaltrials.gov/study/NCT04280510
* **NCT03866538:** Open-label randomized budesonide withdrawal trial in immune-mediated enteropathies (includes autoimmune enteropathy) terminated due to recruitment difficulty; actual enrollment **1** (NCT03866538 chunk 1). URL: https://clinicaltrials.gov/study/NCT03866538
* **NCT00258180:** Phase II high-dose cyclophosphamide for severe autoimmune enteropathy; actual enrollment **3** (NCT00258180 chunk 1). URL: https://clinicaltrials.gov/study/NCT00258180

## Evidence table for knowledge base integration
| Domain | Key points | Quantitative data (if any) | Key sources (first author year journal) | URL |
|---|---|---:|---|---|
| Definition | Autoimmune enteropathy (AIE) is a rare immune-mediated enteropathy characterized by chronic/intractable diarrhea, malabsorption, and small-intestinal villous injury; it affects children and adults and may occur as isolated disease or in syndromic/monogenic immune dysregulation. (shihaz2022autoimmuneenteropathyin pages 1-6, umetsu2018autoimmuneenteropathies pages 1-2) | Pediatric incidence estimated **<1/100,000** in one review. (umetsu2018autoimmuneenteropathies pages 1-2) | Shihaz 2022 *Adv Dig Med*; Umetsu 2018 *Virchows Arch* | https://doi.org/10.1002/aid2.13234 ; https://doi.org/10.1007/s00428-017-2243-7 |
| Diagnosis | Core adult diagnostic framework emphasizes **chronic diarrhea (>6 weeks)**, malabsorption, characteristic small-bowel histology, and exclusion of other causes of villous atrophy; anti-enterocyte/anti-goblet cell antibodies are supportive rather than required. Earlier pediatric criteria included severe diarrhea refractory to exclusion diet, autoimmunity/autoantibodies, and absence of severe immunodeficiency. (shihaz2022autoimmuneenteropathyin pages 6-10, umetsu2018autoimmuneenteropathies pages 1-2, li2024clinicalmanifestationsdiagnosis pages 9-11, villanacci2019clinicalmanifestationsand pages 1-2) | Adult median age at diagnosis reported as **55 years** in one series/review. (shihaz2022autoimmuneenteropathyin pages 1-6, umetsu2018autoimmuneenteropathies pages 1-2) | Shihaz 2022 *Adv Dig Med*; Umetsu 2018 *Virchows Arch*; Li 2024 *World J Gastroenterol*; Villanacci 2019 *Clin Immunol* | https://doi.org/10.1002/aid2.13234 ; https://doi.org/10.1007/s00428-017-2243-7 ; https://doi.org/10.3748/wjg.v30.i19.2523 ; https://doi.org/10.1016/j.clim.2019.07.001 |
| Histology | Key histopathology includes **villous blunting/atrophy**, crypt hyperplasia, deep crypt lymphocytic infiltration, increased crypt apoptotic bodies, mononuclear lamina propria inflammation, and frequent **goblet- and Paneth-cell loss**; surface intraepithelial lymphocytosis is often only mild/minimal. Histologic patterns may mimic celiac disease, chronic active duodenitis, GVHD, or mixed injury. (gentile2012autoimmuneenteropathya pages 2-4, arienzo2025paediatriccongenitalenteropathies pages 8-10, li2024clinicalmanifestationsdiagnosis pages 9-11, villanacci2019clinicalmanifestationsand pages 1-2) | In the Peking cohort (n=16 adults), duodenal biopsy showed villous blunting **100%**, deep crypt lymphocytic infiltration **67%**, apoptotic bodies **50%**, mild IEL increase **69%**, reduced/absent goblet cells **94%**, reduced/absent Paneth cells **94%**, neutrophil infiltration **100%**; ileal goblet-cell loss **62%**, Paneth-cell loss **69%**. In the 40-patient series, histologic patterns were celiac-like **50%**, mixed **35%**, chronic active duodenitis **10%**, GVHD-like **5%**. (li2024clinicalmanifestationsdiagnosis pages 9-11, villanacci2019clinicalmanifestationsand pages 1-2) | Li 2024 *World J Gastroenterol*; Gentile 2012 *Curr Gastroenterol Rep*; Villanacci 2019 *Clin Immunol* | https://doi.org/10.3748/wjg.v30.i19.2523 ; https://doi.org/10.1007/s11894-012-0276-2 ; https://doi.org/10.1016/j.clim.2019.07.001 |
| Autoantibodies | **Anti-enterocyte (AEA/AE)** and **anti-goblet cell (AGA/AG)** antibodies are helpful adjuncts but are neither sufficiently sensitive nor specific to establish diagnosis alone; they can also occur in IBD, HIV, allergic enteropathy, celiac disease, and CVID-associated enteropathy. (shihaz2022autoimmuneenteropathyin pages 6-10, gentile2012autoimmuneenteropathya pages 2-4, enache2025diagnosticchallengesin pages 8-10) | Reviews report AEA/AGA in **50% to >90%** of cases; one review cites AEA in **22/26 (85%)** and **13/15 (87%)** cohorts, while another notes isolated AIE AEA positivity around **80–90%** but nonspecific. (shihaz2022autoimmuneenteropathyin pages 1-6, gentile2012autoimmuneenteropathya pages 2-4, enache2025diagnosticchallengesin pages 8-10) | Gentile 2012 *Curr Gastroenterol Rep*; Shihaz 2022 *Adv Dig Med*; Enache 2025 *Diagnostics* | https://doi.org/10.1007/s11894-012-0276-2 ; https://doi.org/10.1002/aid2.13234 ; https://doi.org/10.3390/diagnostics15121511 |
| Genetics | AIE can be syndromic/monogenic, especially in early-onset disease. Established associations include **FOXP3** (IPEX, X-linked), **LRBA** deficiency (autosomal recessive), **CTLA4** haploinsufficiency (autosomal dominant), **STAT3** gain-of-function, and **AIRE**-related APECED/APS-1. Adult AIE also shows heterogeneous predisposition genes. (chen2020areviewof pages 2-4, li2025comprehensiveinsightsinto pages 1-2, gambineri2018patientswiththe pages 1-2, gambineri2018clinicalimmunologicaland pages 1-2) | In a 173-patient IPEX/IPEX-like cohort, **44 distinct FOXP3 variants** were found in **88** IPEX patients (including **9 novel** variants), and **19 disease-associated variants in 9 genes** were identified among **85** FOXP3-wild-type IPEX-like patients. In an adult AIE review, pathogenic variants were reported in **20/48 (41.6%)** genetically screened patients. (li2025comprehensiveinsightsinto pages 1-2, gambineri2018clinicalimmunologicaland pages 1-2) | Gambineri 2018 *Front Immunol*; Li 2025 *Orphanet J Rare Dis*; Chen 2020 *Dig Dis Sci* | https://doi.org/10.3389/fimmu.2018.02411 ; https://doi.org/10.1186/s13023-025-03731-2 ; https://doi.org/10.1007/s10620-020-06540-8 |
| Mechanism | Central mechanism is **loss of immune tolerance**, especially defective **regulatory T-cell (Treg)** function. FOXP3 mutations impair Treg development/function; LRBA deficiency disrupts intracellular **CTLA-4 trafficking/storage**; CTLA4 haploinsufficiency reduces cell-contact–dependent suppression; STAT3 GOF promotes immune dysregulation/autoimmunity; these converge on mucosal immune activation, epithelial apoptosis, and enterocyte loss. (chen2020areviewof pages 2-4, gambineri2018patientswiththe pages 1-2, gambineri2018clinicalimmunologicaland pages 1-2, iyengar2025tregopathyinfocus pages 5-7) | FOXP3/IPEX median onset reported at **2 months**, with **87%** manifesting in the first year in one summarized cohort. (chen2020areviewof pages 2-4) | Gambineri 2018 *Front Immunol*; Chen 2020 *Dig Dis Sci*; Vogel 2023 *Front Pediatr*; Iyengar 2025 *Front Immunol* | https://doi.org/10.3389/fimmu.2018.02411 ; https://doi.org/10.1007/s10620-020-06540-8 ; https://doi.org/10.3389/fped.2022.770077 ; https://doi.org/10.3389/fimmu.2025.1658140 |
| Epidemiology | AIE is very rare and true prevalence/incidence in adults is not well defined. Adult disease is often diagnosed late and may overlap with primary immunodeficiency/CVID and other autoimmune disorders. (umetsu2018autoimmuneenteropathies pages 1-2, enache2025diagnosticchallengesin pages 8-10) | Pediatric incidence estimate **<1/100,000**; median symptom duration before diagnosis in one adult series/review was **1.5 years**. (umetsu2018autoimmuneenteropathies pages 1-2) | Umetsu 2018 *Virchows Arch*; Enache 2025 *Diagnostics* | https://doi.org/10.1007/s00428-017-2243-7 ; https://doi.org/10.3390/diagnostics15121511 |
| Prognosis | Long-term outcomes remain suboptimal despite immunosuppression. Adult patients can relapse, require ongoing maintenance therapy/nutritional support, and may develop severe complications including multiorgan failure or lymphoma. (li2024clinicalmanifestationsdiagnosis pages 9-11) | In the 16-patient adult cohort, median follow-up was **20.5 months**; **2/16** died of multiple organ failure and **1/16** developed non-Hodgkin lymphoma. Relapse-free survival was **62.5% at 6 months**, **55.6% at 12 months**, and **37.0% at 48 months**. (li2024clinicalmanifestationsdiagnosis pages 9-11) | Li 2024 *World J Gastroenterol* | https://doi.org/10.3748/wjg.v30.i19.2523 |
| Treatment | First-line therapy is usually **corticosteroids**; steroid-sparing agents include **azathioprine**, **tacrolimus/cyclosporine**, **sirolimus**, and selected biologics/targeted agents such as **abatacept** for CTLA4/LRBA-related disease. Nutritional support, including **TPN**, is often necessary. HSCT is considered definitive for some severe monogenic forms (e.g., IPEX-like disorders). (shihaz2022autoimmuneenteropathyin pages 6-10, li2024clinicalmanifestationsdiagnosis pages 9-11, iyengar2025tregopathyinfocus pages 5-7) | In the Peking adult cohort, **14/16** responded clinically to initial glucocorticoids within median **5 days** (IQR **3–20**); **9/16** received immunosuppressants for steroid dependence/refractoriness or maintenance. Shihaz cites abnormal gastroscopy in ~**58%**, capsule endoscopy abnormalities in ~**47%**, fat-soluble vitamin deficiencies in up to **90%**, and mild hypogammaglobulinemia up to **33%**, supporting need for supportive care. In a 26-patient Tregopathy series, targeted therapy achieved complete control in **8/14 (57%)** treated patients; **5** underwent HSCT and **4** were doing well. (shihaz2022autoimmuneenteropathyin pages 6-10, li2024clinicalmanifestationsdiagnosis pages 9-11, iyengar2025tregopathyinfocus pages 5-7) | Li 2024 *World J Gastroenterol*; Shihaz 2022 *Adv Dig Med*; Iyengar 2025 *Front Immunol*; Musabak 2023 *World J Clin Cases* | https://doi.org/10.3748/wjg.v30.i19.2523 ; https://doi.org/10.1002/aid2.13234 ; https://doi.org/10.3389/fimmu.2025.1658140 ; https://doi.org/10.12998/wjcc.v11.i26.6176 |
| Clinical trials | Current formal trial activity is limited. Ongoing observational work is studying pathogenesis of adult immune enteropathies with sequencing and immune profiling; a budesonide withdrawal trial in immune-mediated enteropathies was terminated for poor recruitment; an older phase II cyclophosphamide trial enrolled very few patients. (NCT04280510 chunk 1, NCT00258180 chunk 1, NCT03866538 chunk 1) | **NCT04280510** recruiting observational cohort, target **200** adults, started **2020-02-27**; **NCT03866538** budesonide phase 4 trial terminated, actual enrollment **1**; **NCT00258180** phase II cyclophosphamide trial completed with actual enrollment **3**. (NCT04280510 chunk 1, NCT00258180 chunk 1, NCT03866538 chunk 1) | ClinicalTrials.gov records NCT04280510, NCT03866538, NCT00258180 | https://clinicaltrials.gov/study/NCT04280510 ; https://clinicaltrials.gov/study/NCT03866538 ; https://clinicaltrials.gov/study/NCT00258180 |


*Table: This table compiles evidence-backed facts about autoimmune enteropathy across definition, diagnosis, pathology, genetics, mechanism, prognosis, treatment, and ongoing clinical studies. It is formatted for direct use in a disease knowledge base and limited to sources retrieved in this conversation.*

## Key evidence excerpts (verbatim abstract quotes)
* AIE definition: “Autoimmune enteropathy (AIE) is an uncommon to rare clinical entity characterized by intractable diarrhoea, varying levels of villous atrophy of the small intestine, presence of circulating auto antibodies to enterocytes [1].” (shihaz2022autoimmuneenteropathyin pages 1-6)
* Adult AIE prognosis/treatment response (Li 2024): “All patients received glucocorticoid therapy as the initial medication, of which 14/16 patients achieved a clinical response in 5 (IQR: 3-20) days.” (li2024clinicalmanifestationsdiagnosis pages 9-11)
* IPEX mechanism (FOXP3/Tregs): “tTreg cell dysfunction is the main pathogenic event leading to multiorgan autoimmunity in IPEX.” (arienzo2025paediatriccongenitalenteropathies pages 8-10)
* Adult AIE pathogenesis summary: “Pathogenesis might involve genetic predisposition, aberrant immune homeostasis, comorbidities of autoimmune diseases and environmental trigger.” (li2025comprehensiveinsightsinto pages 1-2)
* STAT3 GOF phenotype includes enteropathy (abstract): “Patients present early in life… [and] can encompass a wide range of clinical manifestations such as: enteropathy…” (shihaz2022autoimmuneenteropathyin pages 6-10)

## Limitations of this report
1. Formal ontology/coding identifiers (MONDO, Orphanet, OMIM, ICD-10/11) were not retrievable from the tool-accessible literature set used in this run.
2. Variant-level details (ACMG classes, allele frequencies) were not available in the extracted excerpts; these typically require ClinVar/gnomAD/OMIM access.
3. Some evidence on biologics (e.g., vedolizumab, JAK inhibitors in AIE) exists in the broader literature but was not captured as full-text primary evidence in the retrieved corpus; thus, it is not asserted here beyond what is directly supported.


References

1. (shihaz2022autoimmuneenteropathyin pages 1-6): Ambalathu Veettil Hussain Shihaz and Jayanta Paul. Autoimmune enteropathy in adults. Advances in Digestive Medicine, 9:75-81, Oct 2022. URL: https://doi.org/10.1002/aid2.13234, doi:10.1002/aid2.13234. This article has 5 citations.

2. (gentile2012autoimmuneenteropathya pages 2-4): Nicole M. Gentile, Joseph A. Murray, and Darrell S. Pardi. Autoimmune enteropathy: a review and update of clinical management. Current Gastroenterology Reports, 14:380-385, Jul 2012. URL: https://doi.org/10.1007/s11894-012-0276-2, doi:10.1007/s11894-012-0276-2. This article has 161 citations.

3. (umetsu2018autoimmuneenteropathies pages 1-2): Sarah E. Umetsu, Ian Brown, Cord Langner, and Gregory Y. Lauwers. Autoimmune enteropathies. Virchows Archiv, 472:55-66, Oct 2018. URL: https://doi.org/10.1007/s00428-017-2243-7, doi:10.1007/s00428-017-2243-7. This article has 60 citations and is from a peer-reviewed journal.

4. (li2024clinicalmanifestationsdiagnosis pages 9-11): Mu-Han Li, Ge-Chong Ruan, Wei-Xun Zhou, Xiao-Qing Li, Sheng-Yu Zhang, Yang Chen, Xiao-Yin Bai, Hong Yang, Yu-Jie Zhang, Peng-Yu Zhao, Ji Li, and Jing-Nan Li. Clinical manifestations, diagnosis and long-term prognosis of adult autoimmune enteropathy: experience from peking union medical college hospital. World Journal of Gastroenterology, 30:2523-2537, May 2024. URL: https://doi.org/10.3748/wjg.v30.i19.2523, doi:10.3748/wjg.v30.i19.2523. This article has 7 citations.

5. (li2025comprehensiveinsightsinto pages 3-4): Muhan Li, Tianming Xu, Gechong Ruan, Chengzhu Ou, Bei Tan, Shengyu Zhang, Xiaoqing Li, Yan You, Weixun Zhou, Ji Li, and Jingnan Li. Comprehensive insights into pathogenesis, diagnosis, treatment, and prognosis in adult autoimmune enteropathy. Orphanet Journal of Rare Diseases, May 2025. URL: https://doi.org/10.1186/s13023-025-03731-2, doi:10.1186/s13023-025-03731-2. This article has 5 citations and is from a peer-reviewed journal.

6. (li2024clinicalmanifestationsdiagnosis media 05afd713): Mu-Han Li, Ge-Chong Ruan, Wei-Xun Zhou, Xiao-Qing Li, Sheng-Yu Zhang, Yang Chen, Xiao-Yin Bai, Hong Yang, Yu-Jie Zhang, Peng-Yu Zhao, Ji Li, and Jing-Nan Li. Clinical manifestations, diagnosis and long-term prognosis of adult autoimmune enteropathy: experience from peking union medical college hospital. World Journal of Gastroenterology, 30:2523-2537, May 2024. URL: https://doi.org/10.3748/wjg.v30.i19.2523, doi:10.3748/wjg.v30.i19.2523. This article has 7 citations.

7. (li2024clinicalmanifestationsdiagnosis media ec9b1a39): Mu-Han Li, Ge-Chong Ruan, Wei-Xun Zhou, Xiao-Qing Li, Sheng-Yu Zhang, Yang Chen, Xiao-Yin Bai, Hong Yang, Yu-Jie Zhang, Peng-Yu Zhao, Ji Li, and Jing-Nan Li. Clinical manifestations, diagnosis and long-term prognosis of adult autoimmune enteropathy: experience from peking union medical college hospital. World Journal of Gastroenterology, 30:2523-2537, May 2024. URL: https://doi.org/10.3748/wjg.v30.i19.2523, doi:10.3748/wjg.v30.i19.2523. This article has 7 citations.

8. (li2025comprehensiveinsightsinto pages 1-2): Muhan Li, Tianming Xu, Gechong Ruan, Chengzhu Ou, Bei Tan, Shengyu Zhang, Xiaoqing Li, Yan You, Weixun Zhou, Ji Li, and Jingnan Li. Comprehensive insights into pathogenesis, diagnosis, treatment, and prognosis in adult autoimmune enteropathy. Orphanet Journal of Rare Diseases, May 2025. URL: https://doi.org/10.1186/s13023-025-03731-2, doi:10.1186/s13023-025-03731-2. This article has 5 citations and is from a peer-reviewed journal.

9. (gambineri2018clinicalimmunologicaland pages 1-2): Eleonora Gambineri, Sara Ciullini Mannurita, David Hagin, Marina Vignoli, Stephanie Anover-Sombke, Stacey DeBoer, Gesmar R. S. Segundo, Eric J. Allenspach, Claudio Favre, Hans D. Ochs, and Troy R. Torgerson. Clinical, immunological, and molecular heterogeneity of 173 patients with the phenotype of immune dysregulation, polyendocrinopathy, enteropathy, x-linked (ipex) syndrome. Frontiers in Immunology, Nov 2018. URL: https://doi.org/10.3389/fimmu.2018.02411, doi:10.3389/fimmu.2018.02411. This article has 206 citations and is from a peer-reviewed journal.

10. (shihaz2022autoimmuneenteropathyin pages 6-10): Ambalathu Veettil Hussain Shihaz and Jayanta Paul. Autoimmune enteropathy in adults. Advances in Digestive Medicine, 9:75-81, Oct 2022. URL: https://doi.org/10.1002/aid2.13234, doi:10.1002/aid2.13234. This article has 5 citations.

11. (NCT04280510 chunk 1):  Pathogenic Study of Adult Immune Enteropathies. Institut National de la Santé Et de la Recherche Médicale, France. 2020. ClinicalTrials.gov Identifier: NCT04280510

12. (NCT00258180 chunk 1):  Cyclophosphamide in Treating Young Patients With Severe Autoimmune Enteropathy. Johns Hopkins University. 2005. ClinicalTrials.gov Identifier: NCT00258180

13. (chen2020areviewof pages 2-4): Charles B. Chen, Farah Tahboub, Thomas Plesec, Marsha Kay, and Kadakkal Radhakrishnan. A review of autoimmune enteropathy and its associated syndromes. Digestive Diseases and Sciences, 65:3079-3090, Aug 2020. URL: https://doi.org/10.1007/s10620-020-06540-8, doi:10.1007/s10620-020-06540-8. This article has 36 citations and is from a peer-reviewed journal.

14. (arienzo2025paediatriccongenitalenteropathies pages 8-10): Francesca Arienzo, Isabella Giovannoni, Antonella Diamanti, Chiara Maria Trovato, Paola De Angelis, Chiara Imondi, Rita Alaggio, and Paola Francalanci. Paediatric congenital enteropathies: clinical and histological review. Diagnostics, 15:946, Apr 2025. URL: https://doi.org/10.3390/diagnostics15080946, doi:10.3390/diagnostics15080946. This article has 1 citations.

15. (iyengar2025tregopathyinfocus pages 5-7): Vaishnavi Venkatachari Iyengar, Vijaya Gowri, Akshaya Sanjay Chougule, Prasad Taur, Manisha Rajan Madkaikar, Minnie Bodhanwala, and Mukesh Manharlal Desai. Tregopathy in focus. Frontiers in Immunology, Oct 2025. URL: https://doi.org/10.3389/fimmu.2025.1658140, doi:10.3389/fimmu.2025.1658140. This article has 2 citations and is from a peer-reviewed journal.

16. (enache2025diagnosticchallengesin pages 8-10): Iulia Enache, Ioan-Cristian Nedelcu, Marina Balaban, Daniel Vasile Balaban, Alina Popp, and Mariana Jinga. Diagnostic challenges in enteropathies: a histopathological review. Diagnostics, 15:1511, Jun 2025. URL: https://doi.org/10.3390/diagnostics15121511, doi:10.3390/diagnostics15121511. This article has 7 citations.

17. (ahmed2019autoimmuneenteropathyan pages 1-2): Zunirah Ahmed, Aamer Imdad, James A. Connelly, and Sari Acra. Autoimmune enteropathy: an updated review with special focus on stem cell transplant therapy. Digestive Diseases and Sciences, 64:643-654, Nov 2019. URL: https://doi.org/10.1007/s10620-018-5364-1, doi:10.1007/s10620-018-5364-1. This article has 49 citations and is from a peer-reviewed journal.

18. (gentile2012autoimmuneenteropathya pages 1-2): Nicole M. Gentile, Joseph A. Murray, and Darrell S. Pardi. Autoimmune enteropathy: a review and update of clinical management. Current Gastroenterology Reports, 14:380-385, Jul 2012. URL: https://doi.org/10.1007/s11894-012-0276-2, doi:10.1007/s11894-012-0276-2. This article has 161 citations.

19. (villanacci2019clinicalmanifestationsand pages 2-3): Vincenzo Villanacci, Vassilios Lougaris, Alberto Ravelli, Elisabetta Buscarini, Tiziana Salviato, Paolo Lionetti, Marianna Salemme, Stefano Martelossi, Costantino De Giacomo, Diego Falchetti, Gloria Pelizzo, and Gabrio Bassotti. Clinical manifestations and gastrointestinal pathology in 40 patients with autoimmune enteropathy. Clinical Immunology, 207:10-17, Oct 2019. URL: https://doi.org/10.1016/j.clim.2019.07.001, doi:10.1016/j.clim.2019.07.001. This article has 41 citations and is from a peer-reviewed journal.

20. (villanacci2019clinicalmanifestationsand pages 1-2): Vincenzo Villanacci, Vassilios Lougaris, Alberto Ravelli, Elisabetta Buscarini, Tiziana Salviato, Paolo Lionetti, Marianna Salemme, Stefano Martelossi, Costantino De Giacomo, Diego Falchetti, Gloria Pelizzo, and Gabrio Bassotti. Clinical manifestations and gastrointestinal pathology in 40 patients with autoimmune enteropathy. Clinical Immunology, 207:10-17, Oct 2019. URL: https://doi.org/10.1016/j.clim.2019.07.001, doi:10.1016/j.clim.2019.07.001. This article has 41 citations and is from a peer-reviewed journal.

21. (NCT03866538 chunk 1): Joseph A. Murray, M.D.. Budesonide in Patients With Immune Mediated Enteropathies. Mayo Clinic. 2019. ClinicalTrials.gov Identifier: NCT03866538

22. (gambineri2018patientswiththe pages 1-2): E Gambineri, SC Mannurita, and D Hagin. Patients with the phenotype of immune dysregulation, polyendocrinopathy, enteropathy, x-linked (ipex) syndrome. Unknown journal, 2018.