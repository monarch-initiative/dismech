---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T19:33:03.770368'
end_time: '2026-05-07T19:41:35.190634'
duration_seconds: 511.42
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Papular xanthoma
  mondo_id: ''
  category: Rare Dermatologic Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Papular xanthoma
- **MONDO ID:**  (if available)
- **Category:** Rare Dermatologic Disorder

## Research Objectives

Please provide a comprehensive research report on **Papular xanthoma** covering all of the
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
- **Disease Name:** Papular xanthoma
- **MONDO ID:**  (if available)
- **Category:** Rare Dermatologic Disorder

## Research Objectives

Please provide a comprehensive research report on **Papular xanthoma** covering all of the
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


# Papular Xanthoma (PX) — Comprehensive Disease Characteristics Report

## Target disease
- **Disease name:** Papular xanthoma (PX)
- **Category:** Rare dermatologic disorder; cutaneous non‑Langerhans cell histiocytosis (xanthomatous)
- **MONDO / Orphanet / OMIM / MeSH / ICD identifiers:** Not available in the retrieved full-text sources used for this report; should be obtained from MONDO/Orphanet/ICD/MeSH databases in a separate curation step.

## Evidence base and recency note
Papular xanthoma is very rare and much of the literature consists of case reports/series. The most directly informative *recent* source retrieved here is a 2023 case report with literature review (Journal of Cutaneous Pathology, May 2023). Several key clinicopathologic facts come from a foundational 10‑case series (2002) and pediatric case reports (2010–2020). (francois2023multiplepapularxanthomas pages 2-2, breier2002papularxanthomaa pages 1-2, ramessur2020eruptivepapulesin pages 1-2)

**PMID note:** PMIDs were not present in the retrieved text extracts; therefore this report cites DOI/URLs and the tool-provided context IDs.

---

## 1. Disease information

### 1.1 Overview (what is the disease?)
Papular xanthoma (PX) is a rare, primarily cutaneous, **xanthomatous** lesion characterized by a dermal proliferation/infiltrate of **lipid-laden (“foamy”) histiocytes/macrophages**, typically occurring with **normal serum lipid profiles (normolipemic)** and classified among **cutaneous non‑Langerhans cell histiocytoses**. (breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2, breier2002papularxanthomaa pages 1-2)

### 1.2 Synonyms / alternative names
- “Papular xanthoma” (primary term)
- “Papular xanthomatosis” is used in some contexts for papular xanthoma presentations (as reflected in older terminology and diagnostic criteria discussions). (ramessur2020eruptivepapulesin pages 1-2, breier2002papularxanthomaa pages 1-2)

### 1.3 Evidence source type
The current understanding is derived predominantly from **aggregated disease-level literature** (case series and reviews) plus **individual patient case reports**, rather than EHR-scale evidence. (breier2002papularxanthomaa pages 2-4, francois2023multiplepapularxanthomas pages 2-2, ramessur2020eruptivepapulesin pages 1-2)

### 1.4 Key recent and authoritative sources (publication date; URL)
- Francois et al. “Multiple papular xanthomas mimicking juvenile xanthogranulomas in an infant: A case report and review of the literature.” **May 2023**. https://doi.org/10.1111/cup.14244 (francois2023multiplepapularxanthomas pages 2-2)
- Breier et al. “Papular xanthoma: a clinicopathological study of 10 cases.” **Apr 2002**. https://doi.org/10.1034/j.1600-0560.2002.290402.x (breier2002papularxanthomaa pages 1-2)
- Ramessur et al. “Eruptive papules in a 4-year-old girl” (Diagnosis: papular xanthoma). **Jan 2020**. https://doi.org/10.1111/pde.14023 (ramessur2020eruptivepapulesin pages 1-2)
- Baykal et al. “The clinical spectrum of xanthomatous lesions of the eyelids.” **May 2017**. https://doi.org/10.1111/ijd.13637 (baykal2017theclinicalspectrum pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**No single genetic cause or infectious agent** was identified in the retrieved literature excerpts. PX is framed as a clinicopathologic entity within non‑Langerhans cell histiocytoses, defined by a macrophage/foam-cell infiltrate pattern rather than a known monogenic defect. (breier2002papularxanthomaa pages 2-4, breier2002papularxanthomaa pages 1-2)

### 2.2 Risk factors
- **Age:** PX occurs in both children and adults; adult disease may show a biphasic pattern (adolescence and middle age) in the 10-case series. (breier2002papularxanthomaa pages 1-2)
- **Lipid dysregulation (possible, not required):** Although PX is classically normolipemic, exceptions exist. Pediatric cases with abnormal lipid profiles have been reported and authors argue lipid criteria may need reevaluation. (arbuckle2010casereport—papularxanthoma pages 1-3, ramessur2020eruptivepapulesin pages 1-2)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was identified in the retrieved sources.

---

## 3. Phenotypes

### 3.1 Cutaneous phenotypes (symptoms/signs)
**Core phenotype:** Asymptomatic **yellow/yellow‑brown papules** (sometimes papulonodules), often widespread; may be solitary or disseminated. (breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2, choudhary2015papularxanthomain pages 1-2)

**Distribution:**
- Adult series: trunk and extremities predominated; head less common; most were solitary lesions (9/10). (breier2002papularxanthomaa pages 1-2)
- Pediatric PX: often head, trunk, extremities with sparing of mucosa, palms, soles, and generally flexures (except axillae), though presentations vary. (ramessur2020eruptivepapulesin pages 1-2, choudhary2015papularxanthomain pages 1-2)

**Periorbital/eyelid involvement:** PX can present with yellowish papulonodular lesions “often located around the eyes” in periorbital lesion reviews; eyelid involvement is illustrated in an eyelid-focused review of xanthomatous lesions. (rebora2011periorbitallesions. pages 4-5, baykal2017theclinicalspectrum pages 1-2)

### 3.2 Laboratory abnormalities
- Classically **normal lipid profile** is part of diagnostic criteria, but not universal. (ramessur2020eruptivepapulesin pages 1-2, arbuckle2010casereport—papularxanthoma pages 1-3)
- Example pediatric workup with normal lipids and other labs: CBC, LFTs, TFTs, immunoglobulins, serum protein electrophoresis (SPEP), and imaging (liver/spleen ultrasound) all normal in one case. (ramessur2020eruptivepapulesin pages 1-2)

### 3.3 Phenotype characteristics (onset/severity/progression/frequency)
- **Childhood onset:** In pediatric cases, onset is reported in the **first year of life in ~90%** and most regress within **five years**. (ramessur2020eruptivepapulesin pages 1-2)
- **Course:** Childhood PX is typically self‑limited; adult PX may be more persistent/progressive. (choudhary2015papularxanthomain pages 1-2, francois2023multiplepapularxanthomas pages 2-2)
- **Residual changes:** “Anetoderma-like scars” after resolution reported in **up to 60%** of pediatric cases. (ramessur2020eruptivepapulesin pages 1-2)

### 3.4 Quality of life impact
Formal QoL instruments (e.g., DLQI, PROMIS) were not reported in the retrieved sources. The main impacts described are cosmetic burden and potential residual atrophic/hyperpigmented scarring after lesion regression in children. (ramessur2020eruptivepapulesin pages 1-2)

### 3.5 Suggested HPO terms (phenotype encoding)
(These are suggested mappings based on described clinical findings; ontology IDs should be verified during curation.)
- Yellow papules / xanthomatous papules → **Xanthoma**; **Skin papule** (ramessur2020eruptivepapulesin pages 1-2, choudhary2015papularxanthomain pages 1-2)
- Periorbital distribution → **Periorbital skin lesion** (rebora2011periorbitallesions. pages 4-5)
- Post-inflammatory hyperpigmentation / residual hyperpigmented macules → **Hyperpigmentation of the skin** (ramessur2020eruptivepapulesin pages 1-2)
- Atrophic/anethoderma-like scarring → **Atrophic scar** / **Anetoderma** (ramessur2020eruptivepapulesin pages 1-2)

---

## 4. Genetic/Molecular information

### 4.1 Causal genes
No causal genes or recurrent pathogenic variants were identified in the retrieved PX evidence.

### 4.2 Molecular/cellular identity (immunophenotype)
PX lesions show a macrophage/histiocyte immunophenotype:
- **CD68 positive** histiocytes are typical. (breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2, choudhary2015papularxanthomain pages 1-2)
- **S100 negative** and **CD1a negative** are repeatedly reported, supporting non‑Langerhans lineage. (breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2)
- **Factor XIIIa (FXIIIa):** variable across reports—positive in at least one pediatric case report and negative in the 10-case adult series and in an infant case review; this variability is important for differential diagnosis with juvenile xanthogranuloma and related entities. (ramessur2020eruptivepapulesin pages 1-2, breier2002papularxanthomaa pages 1-2, francois2023multiplepapularxanthomas pages 2-2)

### 4.3 Suggested GO/CL terms (mechanistic annotation)
(Conceptual mapping consistent with lesion composition; requires ontology verification.)
- CL: **macrophage** / **histiocyte** (dominant foamy cells) (breier2002papularxanthomaa pages 2-4, breier2002papularxanthomaa pages 1-2)
- GO Biological Process: **lipid metabolic process** / **foam cell differentiation** (inferred from “xanthomatized/foamy” macrophages; mechanistic detail not experimentally established for PX in these sources) (breier2002papularxanthomaa pages 2-4)

---

## 5. Environmental information
No specific toxins, occupational exposures, lifestyle factors, or infectious triggers were established as causal. Some case-based associations have been reported with inflammatory/eruptive contexts (viral/drug eruptions) but without mechanistic proof. (ramessur2020eruptivepapulesin pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Current understanding
PX is best understood as a **localized cutaneous accumulation/proliferation of lipid-laden macrophages** in the dermis, producing yellow papules/nodules. Histologically it is typically **well delimited** with **dense infiltrates of xanthomatized cells** and variable **Touton giant cells**, and with **relative absence of inflammatory cells** and lack of an early “primitive histiocytic” phase in classic descriptions. (breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2)

### 6.2 Relationship to juvenile xanthogranuloma (JXG)
PX is repeatedly emphasized as a key histopathologic/clinical mimic of JXG; some authors consider PX within a spectrum/variant of xanthogranuloma (xanthomatous pattern). (francois2023multiplepapularxanthomas pages 2-2, ramessur2020eruptivepapulesin pages 1-2)

### 6.3 Evidence gaps
No pathway-level (e.g., MAPK, PI3K-AKT) or omics profiling findings (transcriptomics/proteomics) were identified in the retrieved PX sources.

---

## 7. Anatomical structures affected

### 7.1 Organ and tissue level
- **Primary:** Skin—**dermis** (papillary/reticular dermis depending on case). (breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2)
- **Sites:** trunk, extremities, head/neck; **periorbital/eyelid** region in some patients. (breier2002papularxanthomaa pages 1-2, rebora2011periorbitallesions. pages 4-5, baykal2017theclinicalspectrum pages 1-2)

### 7.2 Cell types (Cell Ontology suggestions)
- Foamy histiocytes/macrophages (dominant infiltrate). (breier2002papularxanthomaa pages 2-4, breier2002papularxanthomaa pages 1-2)

### 7.3 Subcellular/localization (GO CC suggestions)
Not directly studied in retrieved sources; lipid-laden/foamy cytoplasm implies lipid droplets/lysosomal compartments, but this remains inferential here.

### 7.4 UBERON suggestions
- Skin of trunk/limb regions; periorbital skin/eyelid skin (verify exact UBERON terms during curation). (breier2002papularxanthomaa pages 1-2, rebora2011periorbitallesions. pages 4-5)

---

## 8. Temporal development

### 8.1 Onset
- **Children:** commonly within the first year of life (~90% in pediatric descriptions), but later onset can occur (example onset at age 3 years). (ramessur2020eruptivepapulesin pages 1-2)
- **Adults:** series shows onset across adolescence to middle age with biphasic occurrence. (breier2002papularxanthomaa pages 1-2)

### 8.2 Progression/course
- Pediatric disease often flattens and regresses over years, leaving transient hyperpigmentation and sometimes anetoderma-like scars. (ramessur2020eruptivepapulesin pages 1-2)
- Adults may have more persistent/progressive or recurrent lesions per literature summaries. (francois2023multiplepapularxanthomas pages 2-2, choudhary2015papularxanthomain pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology
No population prevalence/incidence estimates were found in retrieved sources.

**Case-count statistics from reviews/series:**
- 2002 clinicopathologic series noted: “**Until now, 43 cases of cutaneous PX have been described**” (at that time). (breier2002papularxanthomaa pages 2-4)
- 2023 literature review summary cited **~53–54 patients** reported across **~22 reports**, and that **18** had follow-up (median 28 months; mean 41.3 months) with **2** recurrent/persistent lesions. (francois2023multiplepapularxanthomas pages 2-2, francois2023multiplepapularxanthomas pages 2-3)

### 9.2 Inheritance
No inheritance pattern is established in the retrieved literature. A family history of hypercholesterolemia was noted in one pediatric PX case, but causality/inheritance specific to PX was not established. (ramessur2020eruptivepapulesin pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical criteria
Winkelmann’s PX diagnostic criteria (as reproduced in a pediatric diagnostic case discussion) include:
1) generalized asymptomatic yellowish papulonodular lesions without coalescing plaques,
2) **normal lipid profile**,
3) no visceral involvement,
4) foamy-cell predominant infiltrate,
5) absence of primitive histiocytic phase and inflammatory cells. (ramessur2020eruptivepapulesin pages 1-2)

### 10.2 Histopathology
Typical biopsy features include a **well-delimited dermal tumor/infiltrate** with a small grenz zone and **dense infiltrate of foamy/xanthomatized histiocytes** with **numerous Touton-type giant cells** (though Touton cells may be absent in some pediatric lesions). (breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2, choudhary2015papularxanthomain pages 1-2)

### 10.3 Immunohistochemistry
Common IHC profile:
- **CD68+** histiocytes (breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2)
- **S100−, CD1a−** (helps exclude Langerhans cell histiocytosis) (breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2)
- **FXIIIa**: may be positive or negative depending on case/series; therefore should not be used as a sole discriminator. (ramessur2020eruptivepapulesin pages 1-2, breier2002papularxanthomaa pages 1-2, francois2023multiplepapularxanthomas pages 2-2)

### 10.4 Recommended workup (real-world practice)
From case reports and eyelid review guidance, commonly implemented evaluation includes:
- **Fasting lipid profile** (including repeat testing if abnormal) (arbuckle2010casereport—papularxanthoma pages 1-3, ramessur2020eruptivepapulesin pages 1-2)
- Screening for systemic disease/visceral involvement (e.g., ultrasound imaging in pediatric cases; chest X-ray in one report) (ramessur2020eruptivepapulesin pages 1-2, choudhary2015papularxanthomain pages 1-2)
- Additional labs sometimes used: **serum protein electrophoresis** (SPEP) (arbuckle2010casereport—papularxanthoma pages 1-3)
- **Biopsy with histopathologic confirmation** and IHC (ramessur2020eruptivepapulesin pages 1-2, choudhary2015papularxanthomain pages 1-2)
- For xanthomatous eyelid lesions broadly: obtain history, exclude xanthelasma palpebrarum, detailed derm/systemic exam, biopsy, and “appropriate specific imaging screens.” (baykal2017theclinicalspectrum pages 1-2)

### 10.5 Differential diagnosis (key discriminators)
- **Juvenile xanthogranuloma (JXG):** key mimic; PX is more monomorphic/foamy and lacks prominent inflammatory milieu/primitive histiocytic phase described for JXG in classic teaching. (ramessur2020eruptivepapulesin pages 1-2, francois2023multiplepapularxanthomas pages 2-2)
- **Xanthoma disseminatum (XD):** differentiated clinically by plaque tendency, flexural involvement, diabetes insipidus/mucosal involvement (in XD), and by histologic inflammatory features. (ramessur2020eruptivepapulesin pages 1-2)
- **Benign cephalic histiocytosis:** considered in facial-limited pediatric case; distinguished histologically (BCH lacks lipid-laden histiocytes). (arbuckle2010casereport—papularxanthoma pages 1-3)
- Other clinical misdiagnoses reported: xanthoma, atheroma, keloid, histiocytoma, Spitz nevus, clear cell acanthoma, perioral dermatitis. (breier2002papularxanthomaa pages 2-4, breier2002papularxanthomaa pages 1-2, arbuckle2010casereport—papularxanthoma pages 1-3)

---

## 11. Outcome / Prognosis

### 11.1 Overall prognosis
- **Children:** typically favorable with spontaneous regression over years; a case followed for 3 years showed progressive reduction in lesions and residual atrophic hyperpigmented macules. (ramessur2020eruptivepapulesin pages 1-2)
- **Adults:** more likely to persist, recur, or associate with systemic disease per 2023 review summary. (francois2023multiplepapularxanthomas pages 2-2)

### 11.2 Complications
- Residual **anetoderma-like scarring** (up to 60% in pediatric descriptions) and hyperpigmentation are notable cutaneous sequelae. (ramessur2020eruptivepapulesin pages 1-2)

---

## 12. Treatment

### 12.1 Current management (real-world implementation)
- **Observation / expectant management** is commonly used in children because lesions are self-limiting. (choudhary2015papularxanthomain pages 1-2)
- There is **no consistently effective standard therapy** established for adults in the retrieved excerpts. (choudhary2015papularxanthomain pages 1-2, francois2023multiplepapularxanthomas pages 2-2)

### 12.2 Reported therapies
- One pediatric report notes an adult case report of PX “resolved satisfactorily with **doxycycline**” (secondary mention; primary adult doxycycline paper not retrieved here). (choudhary2015papularxanthomain pages 1-2)

### 12.3 MAXO (treatment ontology) suggestions
(Require MAXO ID verification during curation.)
- Watchful waiting / observation (pediatric) (choudhary2015papularxanthomain pages 1-2)
- Skin biopsy (diagnostic procedure; also a medical action) (ramessur2020eruptivepapulesin pages 1-2)
- Systemic antibiotic therapy (doxycycline) — only case-level mention (choudhary2015papularxanthomain pages 1-2)

---

## 13. Prevention
No primary prevention strategies are established. Practical prevention is limited to addressing modifiable lipid abnormalities if present and monitoring for associated conditions when clinically indicated. (arbuckle2010casereport—papularxanthoma pages 1-3, ramessur2020eruptivepapulesin pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring PX analog in non-human species was identified in the retrieved sources.

---

## 15. Model organisms
No PX-specific model organisms or induced experimental models were identified in the retrieved sources.

---

## Recent developments and expert-style synthesis (2023–2024 emphasis)

### Key 2023 insights
The 2023 case report with literature review consolidates modern understanding that PX can mimic JXG clinically and histologically, provides updated **case counts (~53–54 total patients)**, and emphasizes **age-dependent natural history** (self-limited in many pediatric cases vs persistence/recurrence and systemic associations more often discussed in adults). (francois2023multiplepapularxanthomas pages 2-2, francois2023multiplepapularxanthomas pages 2-3)

### Authoritative clinical perspective (workup and caution)
Eyelid-focused review literature emphasizes that xanthomatous periocular lesions can reflect a spectrum of disorders, some with systemic/malignancy associations, and recommends thorough history, systemic examination, biopsy confirmation, and appropriate imaging when evaluating these presentations. (baykal2017theclinicalspectrum pages 1-2)

---

## Summary tables

The following evidence-map table consolidates the most actionable facts for knowledge base population.

| Clinical domain | Key facts | Quantitative details | Evidence |
|---|---|---|---|
| Definition / classification | Papular xanthoma (PX) is a rare **normolipemic cutaneous non-Langerhans cell histiocytosis** and a **monomorphous xanthomatized macrophage-predominant** reaction pattern within the n-LCH spectrum. It was originally defined by Winkelmann as a distinct xanthogranulomatous/xanthomatous entity. | Largest older clinicopathologic series: **10 cases**. | (breier2002papularxanthomaa pages 1-2, breier2002papularxanthomaa pages 2-4) |
| Lipid profile status | PX is classically described as **normolipemic**, and diagnostic criteria include a **normal lipid profile** and **no visceral involvement**. However, exceptions have been reported, including pediatric cases with lipid abnormalities and historical association with dysbetalipoproteinemia, suggesting the criterion is not absolute. | In one pediatric case, triglycerides were **334 mg/dL** initially and **241 mg/dL** on repeat fasting test; cholesterol **134 mg/dL** then **145 mg/dL**. | (ramessur2020eruptivepapulesin pages 1-2, choudhary2015papularxanthomain pages 1-2, arbuckle2010casereport—papularxanthoma pages 1-3) |
| Age of onset patterns | PX occurs in both **children and adults**. Adult series showed a **biphasic occurrence** in **adolescence and middle age**. Pediatric disease usually starts **in the first year of life**, but later childhood onset also occurs. | Adult series age range **13-57 years**; pediatric onset in **~90% during the first year of life**; one case began at age **3 years**, another at **4.5 years**, another at **10 years**. | (breier2002papularxanthomaa pages 1-2, ramessur2020eruptivepapulesin pages 1-2, choudhary2015papularxanthomain pages 1-2, arbuckle2010casereport—papularxanthoma pages 1-3) |
| Distribution / anatomic sites | Lesions are typically **yellow to yellow-brown papules/nodules**, often on **trunk and extremities**; head/neck involvement can occur. Pediatric cases often involve **head, trunk, and extremities** with sparing of **mucosa, palms, soles, and usually flexures**. **Eyelid/periorbital involvement** is documented and may appear as flat plaques or papulonodular xanthomatous lesions. | In the 10-case series, trunk was most common (**50%**); **9/10** were solitary and **1/10** disseminated. | (breier2002papularxanthomaa pages 1-2, ramessur2020eruptivepapulesin pages 1-2, francois2023multiplepapularxanthomas pages 2-2, choudhary2015papularxanthomain pages 1-2, baykal2017theclinicalspectrum pages 4-6, baykal2017theclinicalspectrum pages 1-2, rebora2011periorbitallesions. pages 4-5) |
| Histopathology | PX shows a **well-delimited dermal infiltrate** of **foamy/xanthomatized histiocytes/macrophages**, often with **Touton giant cells**, a **relative absence of inflammatory cells**, and no primitive histiocytic phase. Pediatric lesions may lack giant cells and remain monomorphic. | Some childhood cases show **no multinucleated/Touton giant cells**; others show moderate/numerous Touton cells. | (breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2, francois2023multiplepapularxanthomas pages 2-2, francois2023multiplepapularxanthomas pages 2-3, ramessur2020eruptivepapulesin pages 2-2, breier2002papularxanthomaa pages 1-2, choudhary2015papularxanthomain pages 1-2) |
| Immunohistochemistry | PX usually shows **CD68 positivity** and is typically **S100-negative** and **CD1a-negative**. **Factor XIIIa** findings are variable across reports: negative in the 10-case adult series and some recent infant data, but positive in at least one pediatric case. In the 2002 series, **KiM1p** was consistently positive; **KP1/CD68** labeled mainly giant cells; HAM56 was variable. | Marker pattern summary: **CD68+**, **S100-**, **CD1a-**; **FXIIIa variable**; **KiM1p+** in the adult series. | (breier2002papularxanthomaa pages 1-2, breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2, francois2023multiplepapularxanthomas pages 2-2, francois2023multiplepapularxanthomas pages 2-3, choudhary2015papularxanthomain pages 1-2) |
| Key differential diagnoses | Important differentials include **juvenile xanthogranuloma (JXG)**, **xanthoma disseminatum (XD)**, **benign cephalic histiocytosis (BCH)**, **Spitz nevus**, **clear cell acanthoma**, **xanthoma**, **atheroma**, **keloid**, **histiocytoma**, and in some facial cases **granulomatous/perioral dermatitis**. Distinguishing features rely on biopsy and immunophenotype. | JXG is the principal histopathologic mimic; PX differs by monomorphic foamy-cell infiltrate and relative lack of inflammatory cells/primitive phase. | (breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2, francois2023multiplepapularxanthomas pages 2-2, choudhary2015papularxanthomain pages 1-2, breier2002papularxanthomaa pages 1-2, arbuckle2010casereport—papularxanthoma pages 1-3) |
| Reported associations | PX is usually isolated, but reported associations include **mycosis fungoides**, **Sezary syndrome**, later **CD3(dim)/CD4+ T-cell lymphoma**, **dysbetalipoproteinemia**, **erythrodermic chronic actinic dermatitis**, and viral/drug eruptions. Systemic associations remain uncertain overall. | Eyelid review documented at least **one patient** with PX plus **mycosis fungoides**. | (ramessur2020eruptivepapulesin pages 1-2, choudhary2015papularxanthomain pages 1-2, ramessur2020eruptivepapulesin pages 2-2, baykal2017theclinicalspectrum pages 4-6, baykal2017theclinicalspectrum pages 1-2) |
| Natural history / prognosis | Childhood PX is generally **self-limited**, with lesion flattening and residual hyperpigmentation or anetoderma-like change; adults may show **persistent, progressive, or recurrent** disease. Observation is typical in children. | Childhood lesions often regress within **1-5 years**; **most regress within 5 years**; anetoderma-like scarring reported in **up to 60%**; one child had improvement over **3 years** with no new lesions. | (breier2002papularxanthomaa pages 2-4, ramessur2020eruptivepapulesin pages 1-2, francois2023multiplepapularxanthomas pages 2-2, choudhary2015papularxanthomain pages 1-2, ramessur2020eruptivepapulesin pages 2-2) |
| Epidemiology / case counts | PX is very rare, with literature estimates differing by review date and inclusion criteria. Older and newer reviews consistently indicate only a few dozen documented patients. | Older review: **43 cutaneous cases** before the 2002 series; 2023 review states **53 reported patients** with **35** in four comprehensive series and **18** with follow-up (median **28 months**, mean **41.3 months**); another 2023 summary states **22 reports / 54 patients**. | (breier2002papularxanthomaa pages 2-4, francois2023multiplepapularxanthomas pages 2-2, francois2023multiplepapularxanthomas pages 2-3, breier2002papularxanthomaa pages 1-2) |
| Suggested workup from reported practice | Reported evaluation includes **fasting lipid profile**, **CBC/basic labs**, **serum protein electrophoresis**, **assessment for visceral/systemic involvement**, **skin biopsy with histology and immunohistochemistry**, and when periocular disease is present, broader dermatologic/systemic assessment. | Pediatric workups included normal abdominal ultrasound/chest X-ray in one case and normal liver/spleen ultrasound in another. | (ramessur2020eruptivepapulesin pages 1-2, arbuckle2010casereport—papularxanthoma pages 1-3, choudhary2015papularxanthomain pages 1-2, baykal2017theclinicalspectrum pages 1-2) |


*Table: This table compiles the main clinically actionable facts about papular xanthoma from the provided evidence, including phenotype, pathology, immunohistochemistry, associations, prognosis, and reported case statistics. It is useful as a compact evidence map for building a disease knowledge base entry.*

---

## Key evidence-supported “abstract-quote” style statements (verbatim from retrieved texts)
- Pediatric PX course statistics: “**In 90% of cases, the skin lesions have their onset during the first year of life and most regress within five years**.” (ramessur2020eruptivepapulesin pages 1-2)
- Pediatric sequelae: “**Anetoderma-like scars have been reported after resolution of lesions in up to 60% of cases**.” (ramessur2020eruptivepapulesin pages 1-2)
- 2002 rarity estimate: “**Until now, 43 cases of cutaneous PX have been described** …” (breier2002papularxanthomaa pages 2-4)
- Periorbital location statement: “**Papular xanthoma is a rare entity characterized by yellowish papulonodular lesions, clinically indistinguishable from those of juvenile xanthogranuloma, often located around the eyes**.” (rebora2011periorbitallesions. pages 4-5)

---

## Limitations of this report
- Formal disease identifiers (MONDO/Orphanet/ICD/MeSH/OMIM) and PMIDs were not present in the retrieved excerpts and therefore could not be cited here.
- Genetics/omics/pathway-level mechanisms for PX were not found in the retrieved corpus.
- Treatment evidence is limited mainly to observation in children and sparse case-level reports; no clinical trials were identified.


References

1. (francois2023multiplepapularxanthomas pages 2-2): Rony A. Francois, Grant J. Randall, Eric W. Rudnick, Stephanie J. Carstens, and Vladimir Vincek. Multiple papular xanthomas mimicking juvenile xanthogranulomas in an infant: a case report and review of the literature. Journal of Cutaneous Pathology, 50:1-7, May 2023. URL: https://doi.org/10.1111/cup.14244, doi:10.1111/cup.14244. This article has 0 citations and is from a peer-reviewed journal.

2. (breier2002papularxanthomaa pages 1-2): Friedrich Breier, Bettina Zelger, Harald Reiter, Friedrich Gschnait, and Bernhard W. H. Zelger. Papular xanthoma: a clinicopathological study of 10 cases. Journal of Cutaneous Pathology, 29:200-206, Apr 2002. URL: https://doi.org/10.1034/j.1600-0560.2002.290402.x, doi:10.1034/j.1600-0560.2002.290402.x. This article has 52 citations and is from a peer-reviewed journal.

3. (ramessur2020eruptivepapulesin pages 1-2): Ravi Ramessur, George Meligonis, and Nigel P. Burrows. Eruptive papules in a 4‐year‐old girl. Pediatric Dermatology, Jan 2020. URL: https://doi.org/10.1111/pde.14023, doi:10.1111/pde.14023. This article has 0 citations and is from a peer-reviewed journal.

4. (breier2002papularxanthomaa pages 2-4): Friedrich Breier, Bettina Zelger, Harald Reiter, Friedrich Gschnait, and Bernhard W. H. Zelger. Papular xanthoma: a clinicopathological study of 10 cases. Journal of Cutaneous Pathology, 29:200-206, Apr 2002. URL: https://doi.org/10.1034/j.1600-0560.2002.290402.x, doi:10.1034/j.1600-0560.2002.290402.x. This article has 52 citations and is from a peer-reviewed journal.

5. (baykal2017theclinicalspectrum pages 1-2): Can Baykal, Algun Polat Ekinci, Kurtulus D. Yazganoglu, and Nesimi Buyukbabani. The clinical spectrum of xanthomatous lesions of the eyelids. International Journal of Dermatology, 56:981-992, May 2017. URL: https://doi.org/10.1111/ijd.13637, doi:10.1111/ijd.13637. This article has 38 citations and is from a peer-reviewed journal.

6. (arbuckle2010casereport—papularxanthoma pages 1-3): Alan Arbuckle and Lori D. Prok. Case report—papular xanthoma in a 10‐year‐old female with abnormal lipid profile. Pediatric Dermatology, 27:86-88, Jan 2010. URL: https://doi.org/10.1111/j.1525-1470.2009.01054.x, doi:10.1111/j.1525-1470.2009.01054.x. This article has 9 citations and is from a peer-reviewed journal.

7. (choudhary2015papularxanthomain pages 1-2): Nidhi Choudhary, Shruti Jadhav, Rahul Ahar, Arghyaprasun Ghosh, Joydeep Singha, and Archana Saha. Papular xanthoma in a child: report of a rare entity. Indian Journal of Paediatric Dermatology, 16:78-80, Apr 2015. URL: https://doi.org/10.4103/2319-7250.152139, doi:10.4103/2319-7250.152139. This article has 2 citations.

8. (rebora2011periorbitallesions. pages 4-5): Alfredo Rebora. Periorbital lesions. Clinics in dermatology, 29 2:151-6, Mar 2011. URL: https://doi.org/10.1016/j.clindermatol.2010.09.006, doi:10.1016/j.clindermatol.2010.09.006. This article has 9 citations and is from a peer-reviewed journal.

9. (francois2023multiplepapularxanthomas pages 2-3): Rony A. Francois, Grant J. Randall, Eric W. Rudnick, Stephanie J. Carstens, and Vladimir Vincek. Multiple papular xanthomas mimicking juvenile xanthogranulomas in an infant: a case report and review of the literature. Journal of Cutaneous Pathology, 50:1-7, May 2023. URL: https://doi.org/10.1111/cup.14244, doi:10.1111/cup.14244. This article has 0 citations and is from a peer-reviewed journal.

10. (baykal2017theclinicalspectrum pages 4-6): Can Baykal, Algun Polat Ekinci, Kurtulus D. Yazganoglu, and Nesimi Buyukbabani. The clinical spectrum of xanthomatous lesions of the eyelids. International Journal of Dermatology, 56:981-992, May 2017. URL: https://doi.org/10.1111/ijd.13637, doi:10.1111/ijd.13637. This article has 38 citations and is from a peer-reviewed journal.

11. (ramessur2020eruptivepapulesin pages 2-2): Ravi Ramessur, George Meligonis, and Nigel P. Burrows. Eruptive papules in a 4‐year‐old girl. Pediatric Dermatology, Jan 2020. URL: https://doi.org/10.1111/pde.14023, doi:10.1111/pde.14023. This article has 0 citations and is from a peer-reviewed journal.