---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-03T10:23:39.089171'
end_time: '2026-05-03T10:35:32.242369'
duration_seconds: 713.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Canavan disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Canavan disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Canavan disease** covering all of the
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
- **Disease Name:** Canavan disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Canavan disease** covering all of the
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


# Canavan Disease (Aspartoacylase deficiency) — Disease Characteristics Research Report

## Executive summary (current understanding)
Canavan disease (CD) is an ultra-rare, typically early-infantile onset leukodystrophy caused by biallelic loss-of-function variants in **ASPA**, leading to deficient **aspartoacylase** activity and pathologic accumulation of **N-acetyl-L-aspartate (NAA)**, with characteristic spongiform degeneration/vacuolation and dys-/hypomyelination in CNS white matter. (bley2021thenaturalhistory pages 1-2, corti2023adenoassociatedvirusmediatedgene pages 1-2, grønbækthygesen2024cellularandmolecular pages 1-2)

---

## 1. Disease information
### 1.1 What is the disease?
Canavan disease is a severe neurodegenerative leukodystrophy characterized histologically by insufficient myelination with progressive spongy degeneration of brain white matter. (bley2021thenaturalhistory pages 1-2)

### 1.2 Key identifiers (cross-references)
* **OMIM/MIM (disease):** **MIM #271900** (bley2021thenaturalhistory pages 1-2)
* **OMIM (gene):** **ASPA (OMIM 608034)** (matalon2002canavandiseaseprenatal pages 14-16)
* **ClinicalTrials.gov (active gene therapy trials):** NCT04998396; NCT04833907 (NCT04998396 chunk 1, NCT04833907 chunk 1)
* **MONDO ID:** Not identified in the retrieved primary literature corpus; should be added from MONDO/OMIM cross-reference during database integration (e.g., via MONDO registry). (no direct evidence in retrieved texts)

### 1.3 Synonyms / alternative names
* **Aspartoacylase deficiency** (rossler2023canavan’sspongiformleukodystrophy pages 1-4)
* **Spongy degeneration of the CNS / spongiform leukodystrophy** (rossler2023canavan’sspongiformleukodystrophy pages 1-4, matalon2002canavandiseaseprenatal pages 1-3)
* **N-acetylaspartic aciduria** (sass2019aspartoacylasedeficiency(canavan pages 4-6)
* **Van Bogaert–Bertrand disease** (janson2002clinicalprotocol.gene pages 1-2)

### 1.4 Evidence provenance (patient-level vs aggregated resources)
Evidence in this report is derived from a mix of (i) aggregated cohort natural history (23 cases plus literature comparison), (ii) individual case report/review, (iii) mechanistic review synthesizing multiple experimental studies, (iv) interventional trial protocols and expanded-access records, and (v) animal-model pathology studies. (bley2021thenaturalhistory pages 1-2, rossler2023canavan’sspongiformleukodystrophy pages 1-4, grønbækthygesen2024cellularandmolecular pages 1-2, NCT04998396 chunk 1, takeda2024myelinlesionin pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors
**Genetic cause (primary):** Autosomal recessive biallelic pathogenic variants in **ASPA** leading to aspartoacylase deficiency, impaired NAA hydrolysis, and NAA accumulation in CNS. (matalon2002canavandiseaseprenatal pages 14-16, bley2021thenaturalhistory pages 1-2)

**Mechanistic cause:** ASPA normally hydrolyzes NAA to acetate and aspartate; ASPA deficiency leads to NAA accumulation and white matter pathology. (corti2023adenoassociatedvirusmediatedgene pages 1-2, grønbækthygesen2024cellularandmolecular pages 1-2)

### 2.2 Risk factors
* **Genetic risk factor:** Being a carrier of an ASPA pathogenic variant; disease occurs in children with biallelic variants. (matalon2002canavandiseaseprenatal pages 14-16)
* **Population risk:** Elevated carrier frequency estimates reported for Ashkenazi Jewish populations (range ~1/40 to 1/82). (matalon2002canavandiseaseprenatal pages 14-16)

### 2.3 Protective factors
No validated protective genetic or environmental factors were identified in the retrieved sources. (no direct evidence)

### 2.4 Gene–environment interactions
Recent mechanistic synthesis emphasizes that phenotype is a **spectrum** influenced by “genetic and environmental factors,” but specific gene–environment interaction mechanisms were not defined in the retrieved sources. (grønbækthygesen2024cellularandmolecular pages 7-8)

---

## 3. Phenotypes
### 3.1 Core clinical phenotypes (human)
**Typical age of onset:** “Onset of symptoms was between 0 and 6 months.” (bley2021thenaturalhistory pages 1-2)

**Early hallmark phenotypes:** Severe psychomotor disability and macrocephaly emerging in infancy (“Macrocephaly became apparent between 4 and 18 months of age”). (bley2021thenaturalhistory pages 1-2)

**Common early manifestations (frequency from cohort):** Within first 6 months, developmental delay (17/23), macrocephaly (12/23), abnormal eye movements (12/23). (bley2021thenaturalhistory pages 1-2)

**Seizures:** Rare in the first year but “increase in frequency over time,” with highest frequency toward end of first decade. (bley2021thenaturalhistory pages 1-2, bley2021thenaturalhistory pages 6-7)

**Imaging-associated clinical trajectory:** Progressive disease with early white matter edema/vacuolation that can progress toward atrophy/ventriculomegaly in later phases. (rossler2023canavan’sspongiformleukodystrophy pages 4-6)

### 3.2 Suggested HPO terms (examples; non-exhaustive)
* Developmental delay — **HP:0001263**
* Hypotonia — **HP:0001252**
* Macrocephaly — **HP:0000256**
* Abnormal eye movements / nystagmus — **HP:0000639**
* Seizures — **HP:0001250**
* Spasticity — **HP:0001257**
* Leukodystrophy / abnormal white matter — **HP:0002415**

(bley2021thenaturalhistory pages 1-2, rossler2023canavan’sspongiformleukodystrophy pages 1-4, corti2023adenoassociatedvirusmediatedgene pages 1-2)

### 3.3 Quality-of-life impact
Formal QoL instruments (EQ-5D/SF-36/PROMIS) were not reported in the retrieved sources. Functional impact is substantial, with severe psychomotor disability and limited milestone acquisition. (bley2021thenaturalhistory pages 1-2, matalon2002canavandiseaseprenatal pages 1-3)

---

## 4. Genetic / molecular information
### 4.1 Causal gene
* **ASPA** (aspartoacylase). Loss of ASPA activity causes Canavan disease. (matalon2002canavandiseaseprenatal pages 14-16, grønbækthygesen2024cellularandmolecular pages 1-2)

### 4.2 Pathogenic variant classes and molecular consequences
* **Loss-of-function** is the dominant mechanism at the gene level. (matalon2002canavandiseaseprenatal pages 14-16)
* A major contemporary concept is that many missense ASPA variants cause disease by **protein destabilization → misfolding → protein quality control/proteasomal degradation**, leading to reduced cellular abundance and functional enzyme loss. (grønbækthygesen2024cellularandmolecular pages 1-2, grønbækthygesen2024cellularandmolecular pages 21-22)

**Direct abstract/review quotes supporting this concept:**
* The 2024 review states data “**effectively categorize CD as a protein misfold- ing disorder (proteinopathy)**.” (grønbækthygesen2024cellularandmolecular pages 22-24)

### 4.3 Genotype–phenotype considerations / “mild” alleles
CD phenotypes are “better described as a spectrum of severity.” (grønbækthygesen2024cellularandmolecular pages 7-8)

The 2024 review notes candidate variants associated with milder presentations (reflecting residual activity/partial function), including **R71H** and **Y288C** among others. (grønbækthygesen2024cellularandmolecular pages 8-9)

### 4.4 Allele frequencies / population data
Carrier frequency in Ashkenazi Jewish populations has been estimated in the range **~1/40–1/82** (estimates vary by study and time). (matalon2002canavandiseaseprenatal pages 14-16)

### 4.5 Modifier genes / epigenetics
The natural history study observed that phenotype concordance among siblings but variability among individuals with identical mutations suggests unknown modifiers. (bley2021thenaturalhistory pages 1-2)

No specific modifier genes or epigenetic signatures were identified in the retrieved sources. (no direct evidence)

---

## 5. Environmental information
No established non-genetic environmental or lifestyle causal contributors were identified in the retrieved sources; CD is primarily a Mendelian metabolic leukodystrophy driven by ASPA deficiency. (matalon2002canavandiseaseprenatal pages 14-16, bley2021thenaturalhistory pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Core causal chain (molecular → cellular → tissue → clinical)
1. **Trigger:** Biallelic ASPA loss-of-function variants cause reduced/absent ASPA enzyme activity. (matalon2002canavandiseaseprenatal pages 14-16)
2. **Biochemical consequence:** Failure to hydrolyze **NAA → acetate + aspartate**, causing **NAA accumulation**. (grønbækthygesen2024cellularandmolecular pages 1-2, corti2023adenoassociatedvirusmediatedgene pages 1-2)
3. **Cellular/tissue consequence:** Oligodendrocyte dysfunction, hypomyelination/dysmyelination, and spongiform white-matter vacuolation. (corti2023adenoassociatedvirusmediatedgene pages 1-2, bley2021thenaturalhistory pages 1-2)
4. **Clinical consequence:** Early-infantile onset progressive neurologic impairment, macrocephaly, psychomotor disability, and later seizures/spasticity. (bley2021thenaturalhistory pages 1-2, corti2023adenoassociatedvirusmediatedgene pages 1-2)

### 6.2 Pathway schematic (recent visual evidence)
A 2024 review figure provides a neuron–oligodendrocyte schematic of the **NAA cycle** and how ASPA deficiency disrupts NAA catabolism in Canavan disease. (grønbækthygesen2024cellularandmolecular media eaa25b8f)

### 6.3 Molecular mechanism of many missense variants (2024 concept)
The 2024 mechanistic review synthesizes high-throughput and computational evidence that many pathogenic ASPA variants reduce protein stability and abundance (fold destabilization), linking CD to proteostasis/PQC mechanisms and motivating potential small-molecule stabilizers or degradation blockers. (grønbækthygesen2024cellularandmolecular pages 21-22, grønbækthygesen2024cellularandmolecular pages 22-24)

### 6.4 Suggested ontology terms
**GO biological processes (examples):**
* N-acetylaspartate metabolic process (supported conceptually by ASPA function) (grønbækthygesen2024cellularandmolecular pages 1-2)
* Myelination / CNS myelination (bley2021thenaturalhistory pages 1-2, corti2023adenoassociatedvirusmediatedgene pages 1-2)

**Cell types (CL examples):**
* Oligodendrocyte (central role; oligodendrocyte dysfunction highlighted) (corti2023adenoassociatedvirusmediatedgene pages 1-2, grønbækthygesen2024cellularandmolecular pages 1-2)
* Astrocyte (astrocyte activation/gliosis in models) (takeda2024myelinlesionin pages 2-6)

---

## 7. Anatomical structures affected
### 7.1 Primary organs/systems
* **Central nervous system** white matter (leukodystrophy; spongiform degeneration). (bley2021thenaturalhistory pages 1-2, rossler2023canavan’sspongiformleukodystrophy pages 1-4)

### 7.2 Imaging-anatomy patterns
MRI typically shows diffuse white matter involvement; the 2023 review notes frequent involvement of basal ganglia/thalami with overall widespread supratentorial and infratentorial white matter changes, and MRS shows an elevated NAA peak. (rossler2023canavan’sspongiformleukodystrophy pages 4-6)

### 7.3 Suggested UBERON terms (examples)
* Brain white matter
* Cerebral cortex
* Brainstem

(rossler2023canavan’sspongiformleukodystrophy pages 4-6)

---

## 8. Temporal development
* **Onset:** early infancy; often uneventful perinatal period. (bley2021thenaturalhistory pages 1-2)
* **Progression:** progressive neurodevelopmental stagnation/decline; seizures increase over the first decade. (bley2021thenaturalhistory pages 6-7)
* **Critical window for intervention (inferred from early course):** early diagnosis in the first 1–2 years is emphasized by natural history timing and by trial eligibility (most gene therapy protocols enroll infants/toddlers). (bley2021thenaturalhistory pages 1-2, NCT04998396 chunk 1, NCT04833907 chunk 1)

---

## 9. Inheritance and population
### 9.1 Inheritance
Autosomal recessive; carriers are asymptomatic. (matalon2002canavandiseaseprenatal pages 12-14)

### 9.2 Population distribution / founder effects
CD historically associated with Ashkenazi Jewish populations, but more recent cohorts note diagnoses “more frequently outside Ashkenazi Jewish communities than previously reported,” and many new diagnoses occur without known Ashkenazi ancestry. (bley2021thenaturalhistory pages 1-2, matalon2002canavandiseaseprenatal pages 14-16)

### 9.3 Prevalence/incidence
Quantitative prevalence/incidence estimates were not available in the retrieved evidence corpus (e.g., Orphanet registry data not retrieved). This is a gap for the knowledge base entry. (no direct evidence)

---

## 10. Diagnostics
### 10.1 Core diagnostic biomarkers and tests
**Metabolite biomarker:** Elevated **NAA** in **urine/blood** and/or **brain**. (bley2021thenaturalhistory pages 1-2)

**Neuroimaging:** MRI is the principal imaging tool; MR spectroscopy is diagnostically important because it shows a markedly elevated NAA peak. (rossler2023canavan’sspongiformleukodystrophy pages 1-4, rossler2023canavan’sspongiformleukodystrophy pages 4-6)

**Genetic testing:** Molecular confirmation by ASPA mutation analysis is part of standard diagnosis. (bley2021thenaturalhistory pages 1-2)

**Direct quote (diagnostic statement):** “**CD is diagnosed by detection of elevated NAA in urine or blood or in brain by proton MR spectroscopy [...], as well as by ASPA mutation analysis**.” (bley2021thenaturalhistory pages 1-2)

### 10.2 Screening (carrier/prenatal)
Because the disorder is autosomal recessive, carrier testing and prenatal/preimplantation genetic testing are feasible once familial variants are known. (matalon2002canavandiseaseprenatal pages 14-16, rossler2023canavan’sspongiformleukodystrophy pages 1-4)

---

## 11. Outcomes / prognosis
Earlier sources describe reduced survival and progressive disability, with severe early-onset forms often fatal in childhood/adolescence; cohort-level survival statistics are not comprehensively captured in the retrieved recent sources, but reduced life expectancy and progressive course are consistent across clinical descriptions. (matalon2002canavandiseaseprenatal pages 1-3, corti2023adenoassociatedvirusmediatedgene pages 1-2, rossler2023canavan’sspongiformleukodystrophy pages 1-4)

---

## 12. Treatment
### 12.1 Supportive care (standard of care)
No established curative therapy is cited in the retrieved sources; care is described as multidisciplinary and supportive (nutrition/feeding, seizure management, monitoring neurologic complications). (matalon2002canavandiseaseprenatal pages 1-3, matalon2002canavandiseaseprenatal pages 12-14)

**MAXO suggestions (examples):**
* Seizure management
* Nutritional support / enteral feeding
* Physical therapy / rehabilitation

(matalon2002canavandiseaseprenatal pages 12-14)

### 12.2 Advanced therapeutics (2023–2024: gene therapy emphasis)
**Key concept:** Gene replacement is a rational approach because CD is a monogenic enzyme deficiency, and rAAV vectors (notably AAV9 and Olig001) are in active clinical development. (corti2023adenoassociatedvirusmediatedgene pages 1-2, ceravolo2024updateonleukodystrophies pages 8-10)

**Real-world implementation (trial operations):** Two major programs include a systemic AAV9 approach (BBP-812/CANaspire) and an intracerebroventricular oligodendrocyte-targeting approach (MYR-101/CAN-GT). (NCT04998396 chunk 1, NCT04833907 chunk 1)

| Program/Trial name | Vector/approach | Route | Phase/Study type | Ages | Key endpoints/biomarkers | Source (with year, URL) |
|---|---|---|---|---|---|---|
| rAAV-Olig001-ASPA / MYR-101 (NCT04833907) | Oligodendrocyte-targeting rAAV-Olig001 carrying **ASPA**; single-dose gene therapy | Intracerebroventricular neurosurgical delivery to two predefined sites | Phase 1/2, open-label interventional | 3-60 months; cohorts: <15 mo, 15-36 mo, >36-60 mo | Safety/AEs (CTCAE v5.0); cerebral myelination by SyMRI; brain NAA by MRS; CSF NAA; GMFM-88; Mullen Scales; spasticity; seizure/EEG (NCT04833907 chunk 1) | ClinicalTrials.gov, 2021, https://clinicaltrials.gov/study/NCT04833907 (NCT04833907 chunk 1) |
| BBP-812 / CANaspire (NCT04998396) | Recombinant AAV9 delivering human **ASPA** (BBP-812) | Single IV infusion | Phase 1/2, open-label interventional | Up to 30 months | Safety/AEs; urine NAA and CNS NAA by MRS to 12 months; GMFM-88; Bayley-4; Vineland-3; requires elevated urinary NAA and biallelic **ASPA** variants for entry (NCT04998396 chunk 1) | ClinicalTrials.gov, 2021, https://clinicaltrials.gov/study/NCT04998396 (NCT04998396 chunk 1) |
| Single-patient IND (NCT05317780) | rAAV9-CB6-ASPA with peri-vector immunomodulation (rituximab, sirolimus) | Simultaneous IV + ICV | Expanded access, open-label single-patient IND | 18-24 months (single previously identified male child) | Change from baseline in brain NAA, brain water content/morphology, clinical status, peripheral NAA; vector genomes in blood; immune responses to ASPA/AAV; routine safety labs (NCT05317780 chunk 1, corti2023adenoassociatedvirusmediatedgene pages 1-2) | ClinicalTrials.gov, 2022, https://clinicaltrials.gov/study/NCT05317780 (NCT05317780 chunk 1) |
| AAV2-ASPA neurosurgical protocol | Recombinant AAV2 carrying **ASPA**; direct gene transfer to affected brain regions | Intraparenchymal neurosurgical brain delivery | Clinical protocol / early interventional gene-therapy study | Pediatric Canavan disease patients; protocol planned 21 patients | Quantitative NAA in brain, blood, urine, CSF; MRI/MRS markers of myelination, water content, and morphology; neurological assessments (janson2002clinicalprotocol.gene pages 1-2) | Janson et al., *Human Gene Therapy*, 2002, https://doi.org/10.1089/104303402760128612 (janson2002clinicalprotocol.gene pages 1-2) |


*Table: This table summarizes the main Canavan disease clinical gene therapy programs and studies identified in the evidence, including vector platform, route, study design, age ranges, and core biomarkers. It is useful for comparing how current and historical programs differ in delivery strategy and outcome measures.*

**Recent clinical report (2023):** A published treated case used dual i.v. + i.c.v. rAAV9-CB6-ASPA with prophylactic immunomodulation; assessments included antibody monitoring, vector genomes by qPCR, imaging (MRI/DTI), and NAA measurements in CSF/brain by mass spectrometry and MRS. (corti2023adenoassociatedvirusmediatedgene pages 1-2)

**MAXO suggestions (examples):**
* Gene therapy (AAV-mediated gene transfer)
* Intracerebroventricular administration
* Intravenous administration
* Immunosuppressive therapy / immune modulation

(NCT04998396 chunk 1, NCT04833907 chunk 1, NCT05317780 chunk 1)

### 12.3 Expert opinion / analysis (authoritative synthesis)
The 2024 leukodystrophy trials review emphasizes that “gene therapy is emerging as a potential treatment avenue” for leukodystrophies and notes ongoing in vivo AAV ASPA programs for Canavan disease, while acknowledging the need for optimized delivery and adjunct approaches such as immunomodulation. (ceravolo2024updateonleukodystrophies pages 8-10)

---

## 13. Prevention
### 13.1 Primary prevention
Primary prevention is feasible through **carrier screening** in at-risk populations and family-based testing, given autosomal recessive inheritance and known carrier frequencies in some populations. (matalon2002canavandiseaseprenatal pages 14-16)

### 13.2 Secondary prevention
Early diagnosis using urine/blood NAA and MRI/MRS may allow earlier supportive interventions and eligibility for clinical trials with age-limited enrollment windows. (bley2021thenaturalhistory pages 1-2, NCT04998396 chunk 1)

### 13.3 Tertiary prevention
Multidisciplinary supportive care aims to reduce complications (nutrition/aspiration risk, seizure control). (matalon2002canavandiseaseprenatal pages 12-14)

---

## 14. Other species / natural disease
The retrieved evidence focuses on engineered rodent models; naturally occurring non-human disease was not identified in the retrieved corpus (outside mention of a naturally occurring “tremor rat” model with a large deletion including ASPA and other genes, complicating attribution). (grønbækthygesen2024cellularandmolecular pages 8-9)

---

## 15. Model organisms
### 15.1 Rat model (2024: Aspa knockout rat)
A TALEN-generated **Aspa-knockout rat** shows vacuolation with swollen axons, hypomyelination, and astrocyte activation, particularly in brainstem reticular formation and motor pathways, but notably **did not show overt neurologic signs** in the examined cohorts. (takeda2024myelinlesionin pages 1-2, takeda2024myelinlesionin pages 2-6)

### 15.2 Mouse and other rodent models (review synthesis)
Multiple Aspa mouse models and a “tremor rat” are described; engineered Aspa−/− mice can show macroencephaly, ataxia/tremor, seizures in some animals, and elevated urine NAA. (grønbækthygesen2024cellularandmolecular pages 8-9)

### 15.3 Model utility and limitations
* **Utility:** Reproduces key CNS pathology (vacuolation/spongiform change, hypomyelination) for testing NAA/pathogenesis hypotheses and gene therapy. (takeda2024myelinlesionin pages 2-6, grønbækthygesen2024cellularandmolecular pages 8-9)
* **Limitation:** Species/model differences in overt clinical phenotypes (e.g., rat model with strong histopathology but minimal early neurologic signs). (takeda2024myelinlesionin pages 1-2)

---

## Key recent developments (prioritizing 2023–2024)
1. **Mechanistic reframing (2024):** A 2024 ASPA-focused review synthesizes high-throughput and structural evidence indicating many ASPA missense variants act through folding destabilization and PQC-mediated degradation, with the explicit conclusion that data “effectively categorize CD as a protein misfold- ing disorder (proteinopathy).” (grønbækthygesen2024cellularandmolecular pages 22-24, grønbækthygesen2024cellularandmolecular pages 21-22)
2. **Clinical translation (2023):** A published AAV9-ASPA gene therapy case report details dual-route delivery (i.v.+i.c.v.) and immunomodulation with multimodal biomarker tracking (NAA in CSF/brain, MRI/DTI). (corti2023adenoassociatedvirusmediatedgene pages 1-2)
3. **Active trials (2021–present, still current in 2023–2024 landscape):** BBP-812 (AAV9, IV) and MYR-101 (Olig001, ICV) are ongoing/active programs with NAA (urine/CSF/brain) and myelination imaging as key pharmacodynamic endpoints. (NCT04998396 chunk 1, NCT04833907 chunk 1)
4. **New animal model (2024):** A clean Aspa-knockout rat model provides a platform with human-like white-matter vacuolation/hypomyelination for mechanistic and therapeutic studies. (takeda2024myelinlesionin pages 1-2)

---

## URLs and publication dates (selected key sources)
* Grønbæk-Thygesen & Hartmann-Petersen. *Cell & Bioscience*. **Apr 2024**. https://doi.org/10.1186/s13578-024-01224-6 (grønbækthygesen2024cellularandmolecular pages 1-2)
* Ceravolo et al. *Journal of Neurology*. **Sep 2024**. https://doi.org/10.1007/s00415-023-11996-5 (ceravolo2024updateonleukodystrophies pages 8-10)
* Corti et al. *Molecular Therapy – Methods & Clinical Development*. **Sep 2023**. https://doi.org/10.1016/j.omtm.2023.06.001 (corti2023adenoassociatedvirusmediatedgene pages 1-2)
* Rossler et al. *Journal of Ultrasound*. **Feb 2023**. https://doi.org/10.1007/s40477-022-00667-2 (rossler2023canavan’sspongiformleukodystrophy pages 1-4)
* Takeda et al. *Experimental Animals*. **Mar 2024**. https://doi.org/10.1538/expanim.23-0089 (takeda2024myelinlesionin pages 1-2)
* Bley et al. *Orphanet Journal of Rare Diseases*. **May 2021**. https://doi.org/10.1186/s13023-020-01659-3 (bley2021thenaturalhistory pages 1-2)
* ClinicalTrials.gov: NCT04998396 (CANaspire/BBP-812). First posted **2021**. https://clinicaltrials.gov/study/NCT04998396 (NCT04998396 chunk 1)
* ClinicalTrials.gov: NCT04833907 (CAN-GT/MYR-101). First posted **2021**. https://clinicaltrials.gov/study/NCT04833907 (NCT04833907 chunk 1)

---

## Known gaps (not resolved in retrieved evidence set)
* **MONDO ID**, **ICD-10/ICD-11**, **MeSH** identifiers were not present in the retrieved full-text/records; these should be populated from external ontology registries during integration. (no direct evidence)
* **Point prevalence/incidence** values were not retrieved from Orphanet/registries in this tool run; should be added from Orphanet/GBD/national registries. (no direct evidence)

References

1. (bley2021thenaturalhistory pages 1-2): Annette Bley, Jonas Denecke, Alfried Kohlschütter, Gerhard Schön, Sandra Hischke, Philipp Guder, Tatjana Bierhals, Heather Lau, Maja Hempel, and Florian S. Eichler. The natural history of canavan disease: 23 new cases and comparison with patients from literature. Orphanet Journal of Rare Diseases, May 2021. URL: https://doi.org/10.1186/s13023-020-01659-3, doi:10.1186/s13023-020-01659-3. This article has 54 citations and is from a peer-reviewed journal.

2. (corti2023adenoassociatedvirusmediatedgene pages 1-2): Manuela Corti, Barry J. Byrne, Dominic J. Gessler, Grace Thompson, Samantha Norman, Jenna Lammers, Kirsten E. Coleman, Cristina Liberati, Melissa E. Elder, Maria L. Escolar, Ibrahim S. Tuna, Clementina Mesaros, Gary I. Kleiner, Deborah S. Barbouth, Heather L. Gray-Edwards, Nathalie Clement, Brian D. Cleaver, and Guangping Gao. Adeno-associated virus-mediated gene therapy in a patient with canavan disease using dual routes of administration and immune modulation. Molecular Therapy - Methods &amp; Clinical Development, 30:303-314, Sep 2023. URL: https://doi.org/10.1016/j.omtm.2023.06.001, doi:10.1016/j.omtm.2023.06.001. This article has 30 citations.

3. (grønbækthygesen2024cellularandmolecular pages 1-2): Martin Grønbæk-Thygesen and Rasmus Hartmann-Petersen. Cellular and molecular mechanisms of aspartoacylase and its role in canavan disease. Cell &amp; Bioscience, Apr 2024. URL: https://doi.org/10.1186/s13578-024-01224-6, doi:10.1186/s13578-024-01224-6. This article has 12 citations and is from a peer-reviewed journal.

4. (matalon2002canavandiseaseprenatal pages 14-16): Reuben Matalon and Kimberlee Michals Matalon. Canavan disease prenatal diagnosis and genetic counseling. Obstetrics and gynecology clinics of North America, 29 2:297-304, Jun 2002. URL: https://doi.org/10.1016/s0889-8545(01)00003-1, doi:10.1016/s0889-8545(01)00003-1. This article has 28 citations and is from a peer-reviewed journal.

5. (NCT04998396 chunk 1):  A Study of AAV9 Gene Therapy in Participants With Canavan Disease (CANaspire Clinical Trial). Aspa Therapeutics. 2021. ClinicalTrials.gov Identifier: NCT04998396

6. (NCT04833907 chunk 1):  rAAV-Olig001-ASPA Gene Therapy for Treatment of Children With Typical Canavan Disease. Myrtelle Inc.. 2021. ClinicalTrials.gov Identifier: NCT04833907

7. (rossler2023canavan’sspongiformleukodystrophy pages 1-4): Leon Rossler, Stefan Lemburg, Almut Weitkämper, Charlotte Thiels, Sabine Hoffjan, Huu Phuc Nguyen, Thomas Lücke, and Christoph M. Heyer. Canavan’s spongiform leukodystrophy (aspartoacylase deficiency) with emphasis on sonographic features in infancy: description of a case report and review of the literature. Journal of Ultrasound, 26:757-764, Feb 2023. URL: https://doi.org/10.1007/s40477-022-00667-2, doi:10.1007/s40477-022-00667-2. This article has 11 citations.

8. (matalon2002canavandiseaseprenatal pages 1-3): Reuben Matalon and Kimberlee Michals Matalon. Canavan disease prenatal diagnosis and genetic counseling. Obstetrics and gynecology clinics of North America, 29 2:297-304, Jun 2002. URL: https://doi.org/10.1016/s0889-8545(01)00003-1, doi:10.1016/s0889-8545(01)00003-1. This article has 28 citations and is from a peer-reviewed journal.

9. (sass2019aspartoacylasedeficiency(canavan pages 4-6): Jörn Oliver Sass and Ina Knerr. Aspartoacylase deficiency (canavan disease, n-acetylaspartic aciduria). Human Pathobiochemistry, pages 15-21, Mar 2019. URL: https://doi.org/10.1007/978-981-13-2977-7\_2, doi:10.1007/978-981-13-2977-7\_2. This article has 1 citations.

10. (janson2002clinicalprotocol.gene pages 1-2): Christopher Janson, Scott McPhee, Larissa Bilaniuk, John Haselgrove, Mark Testaiuti, Andrew Freese, Dah-Jyuu Wang, David Shera, Peter Hurh, Joan Rupin, Elizabeth Saslow, Olga Goldfarb, Michael Goldberg, Ghassem Larijani, William Sharrar, Larisa Liouterman, Angelique Camp, Edwin Kolodny, Jude Samulski, and Paola Leone. Clinical protocol. gene therapy of canavan disease: aav-2 vector for neurosurgical delivery of aspartoacylase gene (aspa) to the human brain. Human gene therapy, 13 11:1391-412, Jul 2002. URL: https://doi.org/10.1089/104303402760128612, doi:10.1089/104303402760128612. This article has 329 citations and is from a peer-reviewed journal.

11. (takeda2024myelinlesionin pages 1-2): Shuji Takeda, Rika Hoshiai, Miyuu Tanaka, Takeshi Izawa, Jyoji Yamate, Takashi Kuramoto, and Mitsuru Kuwamura. Myelin lesion in the aspartoacylase (aspa) knockout rat, an animal model for canavan disease. Experimental Animals, 73:347-356, Mar 2024. URL: https://doi.org/10.1538/expanim.23-0089, doi:10.1538/expanim.23-0089. This article has 0 citations and is from a peer-reviewed journal.

12. (grønbækthygesen2024cellularandmolecular pages 7-8): Martin Grønbæk-Thygesen and Rasmus Hartmann-Petersen. Cellular and molecular mechanisms of aspartoacylase and its role in canavan disease. Cell &amp; Bioscience, Apr 2024. URL: https://doi.org/10.1186/s13578-024-01224-6, doi:10.1186/s13578-024-01224-6. This article has 12 citations and is from a peer-reviewed journal.

13. (bley2021thenaturalhistory pages 6-7): Annette Bley, Jonas Denecke, Alfried Kohlschütter, Gerhard Schön, Sandra Hischke, Philipp Guder, Tatjana Bierhals, Heather Lau, Maja Hempel, and Florian S. Eichler. The natural history of canavan disease: 23 new cases and comparison with patients from literature. Orphanet Journal of Rare Diseases, May 2021. URL: https://doi.org/10.1186/s13023-020-01659-3, doi:10.1186/s13023-020-01659-3. This article has 54 citations and is from a peer-reviewed journal.

14. (rossler2023canavan’sspongiformleukodystrophy pages 4-6): Leon Rossler, Stefan Lemburg, Almut Weitkämper, Charlotte Thiels, Sabine Hoffjan, Huu Phuc Nguyen, Thomas Lücke, and Christoph M. Heyer. Canavan’s spongiform leukodystrophy (aspartoacylase deficiency) with emphasis on sonographic features in infancy: description of a case report and review of the literature. Journal of Ultrasound, 26:757-764, Feb 2023. URL: https://doi.org/10.1007/s40477-022-00667-2, doi:10.1007/s40477-022-00667-2. This article has 11 citations.

15. (grønbækthygesen2024cellularandmolecular pages 21-22): Martin Grønbæk-Thygesen and Rasmus Hartmann-Petersen. Cellular and molecular mechanisms of aspartoacylase and its role in canavan disease. Cell &amp; Bioscience, Apr 2024. URL: https://doi.org/10.1186/s13578-024-01224-6, doi:10.1186/s13578-024-01224-6. This article has 12 citations and is from a peer-reviewed journal.

16. (grønbækthygesen2024cellularandmolecular pages 22-24): Martin Grønbæk-Thygesen and Rasmus Hartmann-Petersen. Cellular and molecular mechanisms of aspartoacylase and its role in canavan disease. Cell &amp; Bioscience, Apr 2024. URL: https://doi.org/10.1186/s13578-024-01224-6, doi:10.1186/s13578-024-01224-6. This article has 12 citations and is from a peer-reviewed journal.

17. (grønbækthygesen2024cellularandmolecular pages 8-9): Martin Grønbæk-Thygesen and Rasmus Hartmann-Petersen. Cellular and molecular mechanisms of aspartoacylase and its role in canavan disease. Cell &amp; Bioscience, Apr 2024. URL: https://doi.org/10.1186/s13578-024-01224-6, doi:10.1186/s13578-024-01224-6. This article has 12 citations and is from a peer-reviewed journal.

18. (grønbækthygesen2024cellularandmolecular media eaa25b8f): Martin Grønbæk-Thygesen and Rasmus Hartmann-Petersen. Cellular and molecular mechanisms of aspartoacylase and its role in canavan disease. Cell &amp; Bioscience, Apr 2024. URL: https://doi.org/10.1186/s13578-024-01224-6, doi:10.1186/s13578-024-01224-6. This article has 12 citations and is from a peer-reviewed journal.

19. (takeda2024myelinlesionin pages 2-6): Shuji Takeda, Rika Hoshiai, Miyuu Tanaka, Takeshi Izawa, Jyoji Yamate, Takashi Kuramoto, and Mitsuru Kuwamura. Myelin lesion in the aspartoacylase (aspa) knockout rat, an animal model for canavan disease. Experimental Animals, 73:347-356, Mar 2024. URL: https://doi.org/10.1538/expanim.23-0089, doi:10.1538/expanim.23-0089. This article has 0 citations and is from a peer-reviewed journal.

20. (matalon2002canavandiseaseprenatal pages 12-14): Reuben Matalon and Kimberlee Michals Matalon. Canavan disease prenatal diagnosis and genetic counseling. Obstetrics and gynecology clinics of North America, 29 2:297-304, Jun 2002. URL: https://doi.org/10.1016/s0889-8545(01)00003-1, doi:10.1016/s0889-8545(01)00003-1. This article has 28 citations and is from a peer-reviewed journal.

21. (ceravolo2024updateonleukodystrophies pages 8-10): Giorgia Ceravolo, Kristina Zhelcheska, Violetta Squadrito, David Pellerin, Eloisa Gitto, Louise Hartley, and Henry Houlden. Update on leukodystrophies and developing trials. Journal of Neurology, 271:593-605, Sep 2024. URL: https://doi.org/10.1007/s00415-023-11996-5, doi:10.1007/s00415-023-11996-5. This article has 18 citations and is from a domain leading peer-reviewed journal.

22. (NCT05317780 chunk 1):  Canavan-Single Patient IND. University of Florida. ClinicalTrials.gov Identifier: NCT05317780
