---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T22:05:29.915598'
end_time: '2026-05-06T22:25:50.420351'
duration_seconds: 1220.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Susac Syndrome
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Susac Syndrome
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Susac Syndrome** covering all of the
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
- **Disease Name:** Susac Syndrome
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Susac Syndrome** covering all of the
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


## Susac Syndrome — Comprehensive Disease Characteristics Report

### Target disease
- **Disease name:** Susac syndrome (SuS)  
- **Category:** Autoimmune (immune-mediated microvascular endotheliopathy)  
- **MONDO / Orphanet / OMIM / MeSH / ICD identifiers:** **Not available from the full-text sources retrieved in this run**; these should be filled via direct lookup in Orphanet/Monarch (MONDO)/MeSH/ICD resources during curation rather than inferred. (bose2023susacsyndromeneurological pages 1-2, david2022susacsyndromea pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview
Susac syndrome is a rare, immune-mediated, ischemia-producing **occlusive microvascular endotheliopathy** that affects the **brain, retina, and inner ear**, producing a characteristic clinical triad of **encephalopathy/central nervous system dysfunction**, **branch retinal artery occlusions (BRAO)**, and **sensorineural hearing loss**. (bose2023susacsyndromeneurological pages 1-2, jarius2014clinicalparaclinicaland pages 1-2, bullock2023useofdisease pages 1-2)

### 1.2 Synonyms / alternative names
- **Susac syndrome / Susac’s syndrome** (jarius2014clinicalparaclinicaland pages 1-2)
- **Retinocochleocerebral syndrome** (concept consistent with tri-organ involvement; commonly used term in the literature though not explicitly enumerated in the extracted snippets) (bose2023susacsyndromeneurological pages 1-2, david2022susacsyndromea pages 1-2)

### 1.3 Evidence source type
Most available evidence is derived from:
- **Case reports and case series**, reflecting rarity (jarius2014clinicalparaclinicaland pages 1-2, bose2023susacsyndromeneurological pages 1-2)
- **Retrospective cohorts** (fuchs2025clinicalcharacterizationand pages 1-2)
- **Prospective observational cohorts / registries and biomarker studies** on ClinicalTrials.gov (NCT01273792 chunk 1, NCT01481662 chunk 1, NCT06881368 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
Current evidence supports SuS as a primarily **immune-mediated endotheliopathy** of small vessels, with converging support for **CD8+ cytotoxic T-cell (CTL)–mediated endothelial injury** and (in a subset) **humoral/complement involvement**. (gross2019cd8+tcellmediated pages 1-2, bose2023susacsyndromeneurological pages 1-2, jarius2014clinicalparaclinicaland pages 1-2)

**Direct abstract quote (mechanism; primary literature):**
- Gross et al. (Nature Communications, 2019) report: “*CTLs adhere to CNS microvessels … and polarize granzyme B, which most likely results in the observed endothelial cell injury and microhemorrhages*” and that “*Blocking T-cell adhesion by anti-α4 integrin-intervention ameliorates the disease in the preclinical model*.” (gross2019cd8+tcellmediated pages 1-2)

### 2.2 Risk factors
**Demographic risk:** young adult onset and female predominance are repeatedly observed in cohorts/series. (david2022susacsyndromea pages 1-2, seifertheld2017susacssyndromeclinical pages 6-10)

**Possible infectious triggers (limited evidence):** In an Israeli series of 7 patients, **recent cytomegalovirus (CMV) exposure** was “serologically evident in three patients,” and one had a high antistreptolysin titer—interpreted as potentially supporting a post-infectious mechanism (observational association, not proof of causality). (wilfyarkoni2020increasedincidenceof pages 2-3)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No gene–environment interactions were identified in the retrieved evidence.

---

## 3. Phenotypes

### 3.1 Core phenotype triad (with suggested HPO terms)
1. **Brain involvement / encephalopathy**: confusion, cognitive dysfunction, behavioral/psychiatric features, focal neurological symptoms, headache.  
   - **HPO suggestions:** Encephalopathy; Cognitive impairment; Headache; Behavioral abnormality; Confusion; Focal neurological deficit.  
   - Frequency examples: encephalopathy is part of triad; in one 16-patient series, encephalopathy occurred at some point in most patients but was present at onset in **6/16 (37.5%)**. (bose2023susacsyndromeneurological pages 1-2)

2. **Retinal involvement**: BRAO, arterial wall hyperfluorescence (AWH), visual field defects; may be clinically silent.  
   - **HPO suggestions:** Branch retinal artery occlusion; Visual field defect; Scotoma; Visual impairment.  
   - In a 16-patient series, objective retinal ischemia was documented in **~11/16**. (bose2023susacsyndromeneurological pages 6-8)

3. **Vestibulocochlear involvement**: sensorineural hearing loss, tinnitus, vertigo/balance problems.  
   - **HPO suggestions:** Sensorineural hearing impairment; Tinnitus; Vertigo.  
   - In the 16-patient series, hearing loss occurred in **12/16 (75%)** at any stage. (bose2023susacsyndromeneurological pages 6-8)

### 3.2 Neurocognitive and neuropsychiatric manifestations (2024 review)
A 2024 review highlights that cognitive deficits range from subtle to profound, with executive function and short-term recall frequently affected; psychiatric manifestations may include anxiety, mood disorders, or psychosis, and attribution may be confounded by steroid side effects. (koncz2024theneurocognitiveand pages 1-2)

**Direct abstract quote (2024 review):** “*Executive function and short-term recall are affected frequently. Psychiatric manifestations may be absent or may include anxiety, mood disorders or psychosis.*” (koncz2024theneurocognitiveand pages 1-2)

### 3.3 Phenotype characteristics (onset, progression)
- **Onset pattern:** often subacute with headache and focal deficits (75% in one 16-patient series). (bose2023susacsyndromeneurological pages 1-2)
- **Triad completeness at onset:** often incomplete; 13% at first presentation in the 16-patient series, but 80% eventually developed the triad. (bose2023susacsyndromeneurological pages 6-8)

### 3.4 Quality-of-life impact
Functional impairment is substantial in a subset. In a 20-patient multicenter cohort, ~50% resumed employment while 25% did not return to work. (fuchs2025clinicalcharacterizationand pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes / pathogenic variants
No causal genes or pathogenic germline variants were identified in the retrieved evidence; SuS is not established as a monogenic disorder in these sources.

### 4.2 Modifier genes, epigenetics, chromosomal abnormalities
No evidence identified in the retrieved texts.

---

## 5. Environmental Information

- **Environmental exposures:** An Israeli case series explicitly reported that **toxic environmental exposure was not reported** and no common demographic characteristics were found. (wilfyarkoni2020increasedincidenceof pages 2-3)
- **Lifestyle factors:** not described in the extracted evidence.
- **Infectious agents:** limited observational association with CMV/streptococcal serology in a small series. (wilfyarkoni2020increasedincidenceof pages 2-3)

---

## 6. Mechanism / Pathophysiology

A current working model is that immune dysregulation causes microvascular endothelial injury and occlusion leading to ischemia in brain/retina/inner ear.

### 6.1 Proposed mechanistic chain (upstream → downstream)
1. **Activated cytotoxic CD8+ T cells** expand and target microvessels (oligoclonal expansion; activated phenotype). (gross2019cd8+tcellmediated pages 1-2)
2. **CTL adhesion to microvessels** with **granzyme B polarization** causes endothelial injury and microhemorrhages. (gross2019cd8+tcellmediated pages 1-2)
3. In a subset, **AECA** (complement-activating IgG1) may contribute to microvascular injury. (jarius2014clinicalparaclinicaland pages 1-2)
4. **Complement deposition** is seen in tissue in some cases (C4d deposition in ~30% of vessels in one series), supporting a humoral component. (bose2023susacsyndromeneurological pages 1-2)
5. **Microinfarcts and ischemic lesions** develop in affected organs, producing the clinical triad. (bose2023susacsyndromeneurological pages 1-2, david2022susacsyndromea pages 1-2)

A structured mechanism table (cell types, GO/CL suggestions) is provided below.

| Mechanism component | Evidence summary | Upstream/downstream | Cell types (CL suggestions) | Pathways/GO biological process terms | Key primary sources (PMID if known, else DOI/URL and year) |
|---|---|---|---|---|---|
| Immune-mediated endotheliopathy as initiating lesion | Susac syndrome is consistently described as an immune-mediated occlusive microvascular endotheliopathy affecting precapillary arterioles of the brain, retina, and inner ear, providing the unifying mechanism for the clinical triad. Pathology is centered on small-vessel endothelial injury rather than primary demyelination. (bose2023susacsyndromeneurological pages 1-2, david2022susacsyndromea pages 1-2, fuchs2025clinicalcharacterizationand pages 1-2) | Upstream disease-defining process | Endothelial cell (CL: 0000115); vascular endothelial cell (CL: 0002543) | GO: endothelial cell apoptotic process; blood vessel morphogenesis; regulation of vascular permeability; inflammatory response | Bose et al., J Neurol 2023, https://doi.org/10.1007/s00415-023-11891-z; David et al., Autoimmun Rev 2022, https://doi.org/10.1016/j.autrev.2022.103097; Fuchs et al., Neurol Neuroimmunol Neuroinflamm 2025, https://doi.org/10.1212/NXI.0000000000200357 |
| CD8+ cytotoxic T-cell adhesion to CNS microvessels | In SuS, oligoclonally expanded activated CD8+ CTLs adhere to CNS microvessels and polarize granzyme B toward endothelium, which is proposed to drive endothelial injury and microhemorrhages. CSF/blood immune phenotyping showed increased activated CD8+ cells and reduced intrathecal CD4/CD8 ratio, supporting a cytotoxic T-cell process. (gross2019cd8+tcellmediated pages 1-2, bose2023susacsyndromeneurological pages 5-6) | Upstream to endothelial damage; proximal effector mechanism | CD8-positive, alpha-beta T cell (CL: 0000625); effector memory CD8-positive, alpha-beta T cell (suggested CL family term); endothelial cell (CL: 0000115) | GO: leukocyte cell-cell adhesion; T cell activation; granzyme-mediated apoptotic signaling pathway; cell killing; transendothelial migration | Gross et al., Nat Commun 2019, https://doi.org/10.1038/s41467-019-13593-5; Bose et al., J Neurol 2023, https://doi.org/10.1007/s00415-023-11891-z |
| Targetability of T-cell trafficking / anti-α4 integrin evidence | In a transgenic model recapitulating SuS-like endothelial injury, blocking T-cell adhesion with anti-α4 integrin ameliorated disease; similarly, disease severity decreased in four SuS patients treated with natalizumab along with other therapies. This supports leukocyte adhesion/trafficking as a targetable step. (gross2019cd8+tcellmediated pages 1-2) | Therapeutic interruption of upstream effector step | CD8-positive, alpha-beta T cell (CL: 0000625); endothelial cell (CL: 0000115) | GO: integrin-mediated signaling pathway; leukocyte migration; leukocyte adhesion to vascular endothelial cell | Gross et al., Nat Commun 2019, https://doi.org/10.1038/s41467-019-13593-5 |
| Humoral autoimmunity / AECA subset | Anti-endothelial cell antibodies (AECA) were detected in 25% (5/20) of definite SuS cases, with median titers far higher than controls; titers >1:320 were exclusive to SuS. AECA positivity persisted over time in some patients, but seropositivity did not clearly segregate with severity, suggesting pathogenicity in a subset rather than all cases. (jarius2014clinicalparaclinicaland pages 1-2) | Upstream or parallel contributor to endothelial injury in a subset | B cell (CL: 0000236); plasma cell (CL: 0000786); endothelial cell (CL: 0000115) | GO: immunoglobulin mediated immune response; complement activation, classical pathway; antigen binding | Jarius et al., J Neuroinflammation 2014, https://doi.org/10.1186/1742-2094-11-46 |
| Complement-activating AECA subclass | In all seropositive cases in the international multicenter study, AECA belonged to complement-activating IgG1; many samples also had IgA and 45% had IgM AECA. This supports the plausibility of antibody-mediated complement fixation on endothelium. (jarius2014clinicalparaclinicaland pages 1-2, jarius2014clinicalparaclinicaland pages 8-9) | Upstream/parallel humoral amplification mechanism | B cell (CL: 0000236); plasma cell (CL: 0000786); endothelial cell (CL: 0000115) | GO: complement activation; classical pathway; Fc receptor signaling pathway; humoral immune response | Jarius et al., J Neuroinflammation 2014, https://doi.org/10.1186/1742-2094-11-46 |
| Complement deposition in tissue (C4d) | Brain histology in the 2023 UK series showed C4d immunostaining with complement deposition in capillaries and venules in ~30% of vessels, interpreted as evidence of humoral-mediated microangiopathy. This complements earlier pathology reports linking vascular immune injury to ischemic damage. (bose2023susacsyndromeneurological pages 1-2) | Intermediate amplification step between immune attack and ischemic injury | Endothelial cell (CL: 0000115); perivascular lymphocyte (suggested immune cell term) | GO: complement activation; membrane attack complex assembly; regulation of endothelial cell injury | Bose et al., J Neurol 2023, https://doi.org/10.1007/s00415-023-11891-z |
| Endothelial necrosis and vascular narrowing/occlusion | Histology/autopsy studies show endothelial cell necrosis, perivascular lymphocytic infiltration, vascular narrowing/occlusion, and small-vessel vasculitic change. These lesions mechanistically link immune attack to reduced perfusion in affected organs. (bose2023susacsyndromeneurological pages 1-2, david2022susacsyndromea pages 1-2, cvikova2024casereportsusac pages 1-2) | Intermediate lesion-forming step | Endothelial cell (CL: 0000115); lymphocyte (CL: 0000542); CD8-positive, alpha-beta T cell (CL: 0000625) | GO: endothelial cell death; vasculature development; inflammatory response; regulation of blood circulation | Bose et al., J Neurol 2023, https://doi.org/10.1007/s00415-023-11891-z; Cviková et al., Front Neurol 2024, https://doi.org/10.3389/fneur.2024.1339438 |
| Microinfarcts and microangiopathic ischemic injury | Multiple microinfarcts involving gray matter, white matter, deep nuclei, brainstem, and corpus callosum were found on biopsy/autopsy; these are the tissue-level consequence of occluded microvessels. This explains diffusion-restricted lesions and the characteristic callosal MRI abnormalities. (bose2023susacsyndromeneurological pages 1-2, david2022susacsyndromea pages 1-2, gross2019cd8+tcellmediated pages 1-2) | Downstream tissue injury | Neuron (CL: 0000540); oligodendrocyte (CL: 0000128); astrocyte (CL: 0000127); endothelial cell (CL: 0000115) | GO: response to ischemia; cell death; axon injury response; gliogenesis | Bose et al., J Neurol 2023, https://doi.org/10.1007/s00415-023-11891-z; Gross et al., Nat Commun 2019, https://doi.org/10.1038/s41467-019-13593-5 |
| Brain involvement in the clinical triad | Cerebral microvascular injury produces encephalopathy, headache, focal deficits, cognitive dysfunction, psychiatric/behavioral change, and typical MRI lesions (especially corpus callosum “snowballs,” pericallosal lesions, leptomeningeal enhancement). This is the brain arm of the triad. (bose2023susacsyndromeneurological pages 1-2, david2022susacsyndromea pages 1-2, koncz2024theneurocognitiveand pages 1-2) | Downstream organ-level manifestation | Neuron (CL: 0000540); astrocyte (CL: 0000127); microglial cell (CL: 0000129); endothelial cell (CL: 0000115) | GO: response to ischemia; cognition; regulation of synaptic signaling; neuroinflammatory response | Bose et al., J Neurol 2023, https://doi.org/10.1007/s00415-023-11891-z; Koncz et al., Neurol Sci 2024, https://doi.org/10.1007/s10072-024-07672-9 |
| Retinal involvement in the clinical triad | The same occlusive microangiopathy in retinal arterioles causes BRAO, arterial wall hyperfluorescence, scotomas, and sometimes clinically silent retinal ischemia detectable on FA/OCT. This is the ocular arm of the triad and one of the most actionable diagnostic windows into ongoing microvascular disease. (cvikova2024casereportsusac pages 7-8, fuchs2025clinicalcharacterizationand pages 1-2) | Downstream organ-level manifestation | Retinal vascular endothelial cell (suggest endothelial cell term); retinal ganglion cell (CL suggestion); pericyte (CL suggestion) | GO: retina vasculature development; response to hypoxia; visual perception; blood vessel occlusion | Cviková et al., Front Neurol 2024, https://doi.org/10.3389/fneur.2024.1339438; Fuchs et al., Neurol Neuroimmunol Neuroinflamm 2025, https://doi.org/10.1212/NXI.0000000000200357 |
| Cochlear/vestibular involvement in the clinical triad | Occlusive injury of inner-ear microvessels, especially the apical cochlea, leads to low- to middle-frequency sensorineural hearing loss, tinnitus, and sometimes vertigo/vestibular dysfunction. This is the ear arm of the triad and may be irreversible when infarction is advanced. (cvikova2024casereportsusac pages 7-8, fuchs2025clinicalcharacterizationand pages 1-2) | Downstream organ-level manifestation | Cochlear hair cell (CL suggestion); vestibular hair cell (CL suggestion); endothelial cell (CL: 0000115) | GO: sensory perception of sound; inner ear development; response to ischemia | Cviková et al., Front Neurol 2024, https://doi.org/10.3389/fneur.2024.1339438; Fuchs et al., Neurol Neuroimmunol Neuroinflamm 2025, https://doi.org/10.1212/NXI.0000000000200357 |
| Integrated causal chain | Working model: immune dysregulation → CD8+ CTL adhesion to microvessels ± AECA/complement activation in a subset → endothelial injury/necrosis and vascular narrowing → occlusive microangiopathy and microinfarcts → brain/retina/cochlea ischemia → encephalopathy, BRAO/retinal ischemia, and hearing loss/vertigo. (gross2019cd8+tcellmediated pages 1-2, jarius2014clinicalparaclinicaland pages 1-2, bose2023susacsyndromeneurological pages 1-2, david2022susacsyndromea pages 1-2) | Full upstream-to-downstream disease map | CD8-positive, alpha-beta T cell (CL: 0000625); B cell (CL: 0000236); endothelial cell (CL: 0000115); neuron (CL: 0000540); cochlear hair cell (CL suggestion) | GO: immune effector process; complement activation; endothelial cell death; response to ischemia; sensory perception of sound; visual perception | Gross et al., Nat Commun 2019, https://doi.org/10.1038/s41467-019-13593-5; Jarius et al., J Neuroinflammation 2014, https://doi.org/10.1186/1742-2094-11-46; Bose et al., J Neurol 2023, https://doi.org/10.1007/s00415-023-11891-z; David et al., Autoimmun Rev 2022, https://doi.org/10.1016/j.autrev.2022.103097 |


*Table: This table summarizes the current mechanistic model of Susac syndrome, from upstream immune injury to downstream ischemic damage in brain, retina, and cochlea. It is useful for knowledge-base curation because it links causal steps, cell types, ontology suggestions, and primary evidence.*

### 6.2 Targetability and translational implications
Gross et al. provide mechanistic and translational evidence that **blocking α4-integrin–mediated T-cell adhesion** can ameliorate disease in a preclinical model and report decreased severity in four treated patients (observational), highlighting leukocyte trafficking as a therapeutic target. (gross2019cd8+tcellmediated pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ level (with UBERON suggestions)
- **Brain/CNS** (UBERON: brain; meninges) → encephalopathy, headache, focal deficits, cognitive/psychiatric symptoms. (bose2023susacsyndromeneurological pages 1-2, david2022susacsyndromea pages 1-2)
- **Eye/retina** (UBERON: retina; retinal artery) → BRAO/AWH, visual field defects, sometimes silent involvement. (cvikova2024casereportsusac pages 7-8, fuchs2025clinicalcharacterizationand pages 1-2)
- **Inner ear/cochlea + semicircular canals** (UBERON: cochlea; vestibular apparatus) → SNHL, tinnitus, vertigo. (bose2023susacsyndromeneurological pages 1-2, cvikova2024casereportsusac pages 7-8)

### 7.2 Tissue/cell level (CL suggestions)
- **Vascular endothelium** (CL: endothelial cell) is the main target. (bose2023susacsyndromeneurological pages 1-2, gross2019cd8+tcellmediated pages 1-2)
- **CD8+ T cells** (CL: CD8-positive alpha-beta T cell) are strongly implicated. (gross2019cd8+tcellmediated pages 1-2)

### 7.3 Subcellular / molecular compartments
Not specifically described in the retrieved evidence.

---

## 8. Temporal Development

### 8.1 Onset and course
SuS may follow **monocyclic/monophasic**, **polycyclic**, or **chronic-continuous** courses. (bose2023susacsyndromeneurological pages 8-9, vodopivec2016treatmentofsusac pages 1-3)

### 8.2 Relapse timing
In a 20-patient cohort, **cerebral and inner-ear exacerbations were most common in the first year**, whereas **retinal exacerbations** occurred more frequently mainly **within the first 2 years**. (fuchs2025clinicalcharacterizationand pages 1-2)

### 8.3 Diagnostic delay
Diagnostic delay is common due to incomplete triad at onset; a UK series reported **mean time to diagnosis of 3 months**. (bose2023susacsyndromeneurological pages 6-8)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent quantitative estimates)
A nationwide Austrian survey (adults >19 years) estimated:
- **Annual incidence:** 0.024 per 100,000 (95% CI 0.010–0.047)  
- **Minimum 5-year period prevalence:** 0.148 per 100,000 (95% CI 0.071–0.272) (seifertheld2017susacssyndromeclinical pages 6-10)

### 9.2 Demographics
- Female predominance is typical (e.g., female:male 3:1 in one 16-patient series). (bose2023susacsyndromeneurological pages 1-2)
- Mean onset in the 20–40 range is common across studies; for example mean age 35.6 in Bose et al., and mean onset 38.9 in a later multicenter cohort. (bose2023susacsyndromeneurological pages 1-2, fuchs2025clinicalcharacterizationand pages 1-2)

A structured table of key statistics is provided below.

| Finding/statistic | Value | Population/cohort | Notes | Source (include DOI/URL and year) |
|---|---:|---|---|---|
| Annual incidence | 0.024 per 100,000 (95% CI 0.010–0.047) | Adult Susac syndrome patients in Austria; nationwide survey, 8 newly diagnosed over 5 years | Adults >19 years only; minimum annual incidence estimate | Seifert-Held et al., *Int J Neurosci* 2017, doi:10.1080/00207454.2016.1254631, https://doi.org/10.1080/00207454.2016.1254631 (seifertheld2017susacssyndromeclinical pages 6-10) |
| Minimum 5-year prevalence | 0.148 per 100,000 (95% CI 0.071–0.272) | Adult Susac syndrome patients in Austria; nationwide survey (n=10) | Minimum 5-year period prevalence in adults >19 years | Seifert-Held et al., *Int J Neurosci* 2017, doi:10.1080/00207454.2016.1254631, https://doi.org/10.1080/00207454.2016.1254631 (seifertheld2017susacssyndromeclinical pages 1-6, seifertheld2017susacssyndromeclinical pages 6-10) |
| Sex ratio | Female:male = 3:1 | UK case series, 16 patients | Mean age 35.6 years (range 18–60) | Bose et al., *J Neurol* 2023, doi:10.1007/s00415-023-11891-z, https://doi.org/10.1007/s00415-023-11891-z (bose2023susacsyndromeneurological pages 1-2) |
| Mean age at onset / sex ratio | Mean age 38.9 years; female:male = 1.86 | Multicenter retrospective cohort, 20 patients | Mean follow-up 55.9 months | Fuchs et al., *Neurol Neuroimmunol Neuroinflamm* 2025, doi:10.1212/NXI.0000000000200357, https://doi.org/10.1212/NXI.0000000000200357 (fuchs2025clinicalcharacterizationand pages 1-2) |
| Diagnostic delay | Mean 3 months | UK case series, 16 patients | Delay attributed in part to incomplete/sequential triad | Bose et al., *J Neurol* 2023, doi:10.1007/s00415-023-11891-z, https://doi.org/10.1007/s00415-023-11891-z (bose2023susacsyndromeneurological pages 6-8) |
| Complete clinical triad at onset | 13% initially | UK case series, 16 patients | Full triad uncommon at first presentation | Bose et al., *J Neurol* 2023, doi:10.1007/s00415-023-11891-z, https://doi.org/10.1007/s00415-023-11891-z (bose2023susacsyndromeneurological pages 6-8) |
| Complete clinical triad over disease course | 80% eventually | UK case series, 16 patients | Supports repeated reassessment over time | Bose et al., *J Neurol* 2023, doi:10.1007/s00415-023-11891-z, https://doi.org/10.1007/s00415-023-11891-z (bose2023susacsyndromeneurological pages 6-8) |
| Cognitive improvement during follow-up | 75% improved | Multicenter retrospective cohort, 20 patients | Improvement measured during mean 55.9-month follow-up | Fuchs et al., *Neurol Neuroimmunol Neuroinflamm* 2025, doi:10.1212/NXI.0000000000200357, https://doi.org/10.1212/NXI.0000000000200357 (fuchs2025clinicalcharacterizationand pages 1-2) |
| Return to work | Approximately 50% resumed employment | Multicenter retrospective cohort, 20 patients | Employment used as a practical long-term outcome | Fuchs et al., *Neurol Neuroimmunol Neuroinflamm* 2025, doi:10.1212/NXI.0000000000200357, https://doi.org/10.1212/NXI.0000000000200357 (fuchs2025clinicalcharacterizationand pages 1-2) |
| Failure to return to work | 25% did not return to work | Multicenter retrospective cohort, 20 patients | Indicates substantial functional morbidity despite treatment | Fuchs et al., *Neurol Neuroimmunol Neuroinflamm* 2025, doi:10.1212/NXI.0000000000200357, https://doi.org/10.1212/NXI.0000000000200357 (fuchs2025clinicalcharacterizationand pages 1-2) |
| Serum IgG anti-endothelial cell antibodies (AECA) positivity | 25% (5/20) of definite Susac syndrome patients | International multicenter serologic study; 20 definite SuS patients, 70 controls | Controls: 4.3% (3/70); median titer in SuS 1:3200 | Jarius et al., *J Neuroinflammation* 2014, doi:10.1186/1742-2094-11-46, https://doi.org/10.1186/1742-2094-11-46 (jarius2014clinicalparaclinicaland pages 1-2) |
| AECA subclass | Complement-activating IgG1 subclass in all seropositive cases | International multicenter serologic study | Supports humoral/complement-mediated contribution in a subset | Jarius et al., *J Neuroinflammation* 2014, doi:10.1186/1742-2094-11-46, https://doi.org/10.1186/1742-2094-11-46 (jarius2014clinicalparaclinicaland pages 1-2) |


*Table: This table summarizes high-yield epidemiology, diagnostic timing, prognosis, and serologic findings for Susac syndrome from major cohort and multicenter studies. It is useful for quickly comparing incidence, demographic patterns, functional outcomes, and AECA-related mechanistic evidence.*

---

## 10. Diagnostics

### 10.1 Clinical criteria
A practical widely cited approach is the **European Susac Consortium (EuSaC) 2016 criteria**, which define brain, retinal, and vestibulocochlear involvement with specific required clinical/imaging findings, yielding definite/probable/possible diagnoses. (cvikova2024casereportsusac pages 7-8, cvikova2024casereportsusac media 1cd8097f)

### 10.2 Key tests and real-world implementation
Modern practice emphasizes multimodal confirmation:
- Brain MRI (callosal/pericallosal lesions; “snowballs”) (bose2023susacsyndromeneurological pages 1-2)
- Fluorescein angiography (BRAO/AWH) and OCT/SD-OCT (cvikova2024casereportsusac pages 7-8, wilfyarkoni2020increasedincidenceof pages 2-3)
- Audiogram ± vestibular testing (cvikova2024casereportsusac pages 7-8, fuchs2025clinicalcharacterizationand pages 1-2)
- CSF (typically raised protein; OCB usually absent) (bose2023susacsyndromeneurological pages 1-2, cvikova2024casereportsusac pages 7-8)

A structured diagnostic/workflow table (with ontology suggestions) is provided below.

| Domain | Key tests/findings | Practical notes (what to order/when) | Ontology suggestions (HPO/LOINC/RadLex where applicable) | Key sources (DOI/URL, year) |
|---|---|---|---|---|
| EuSaC diagnostic framework | Definite SuS requires all 3 domains; probable = 2/3; possible = 1/3. Brain: new cognitive/behavioral change and/or focal neurologic symptoms and/or new headache **plus** typical MRI lesions including at least one corpus callosum “snowball.” Retina: BRAO or arterial wall hyperfluorescence (AWH) on fluorescein angiography, or branch ischemia on fundoscopy/SD-OCT. Vestibulocochlear: new tinnitus and/or hearing loss and/or peripheral vertigo with supportive testing. | In suspected SuS, deliberately evaluate **brain + retina + inner ear**, even if only one domain is symptomatic. Repeat testing over time because the full triad is often absent initially. | HPO: Encephalopathy; Cognitive impairment; Headache; Branch retinal artery occlusion; Sensorineural hearing impairment; Tinnitus; Vertigo. RadLex: brain MRI; fluorescein angiography; SD-OCT; audiogram. | Front Neurol review summarizing EuSaC 2016 criteria and table image extraction (https://doi.org/10.3389/fneur.2024.1339438, 2024) (cvikova2024casereportsusac pages 7-8, cvikova2024casereportsusac media 1cd8097f) |
| Brain MRI: core diagnostic imaging | Typical MRI: hyperintense multifocal small round lesions, especially central corpus callosum “snowballs”; pericallosal lesions common. Internal capsule “string of pearls” pattern is evocative. | Order brain MRI early in any unexplained encephalopathy/headache/focal deficits when SuS is possible. Sagittal FLAIR/T2 sequences are particularly helpful for callosal lesions. MRI can strongly support diagnosis when triad is incomplete. | RadLex: MRI brain, FLAIR, diffusion-weighted MRI. HPO: Abnormal brain MRI; Corpus callosum lesion. | J Neurol case series/review (https://doi.org/10.1007/s00415-023-11891-z, 2023); Autoimmun Rev scoping review (https://doi.org/10.1016/j.autrev.2022.103097, 2022) (bose2023susacsyndromeneurological pages 1-2, david2022susacsyndromea pages 1-2) |
| Leptomeningeal enhancement | Post-contrast MRI may show multifocal leptomeningeal enhancement; reported in ~23–44% historically, and up to 56–100% in some newer contrast-enhanced FLAIR series. Association of callosal microischemic lesions plus leptomeningeal enhancement is highly suggestive/pathognomonic in context. | If routine MRI is equivocal but suspicion remains high, include contrast-enhanced FLAIR when available. Particularly useful in active cerebral disease and headache-dominant presentations. | RadLex: Contrast-enhanced FLAIR MRI; leptomeningeal enhancement. HPO: Leptomeningeal enhancement; Headache. | Front Neurol review (https://doi.org/10.3389/fneur.2024.1339438, 2024); Autoimmun Rev review (https://doi.org/10.1016/j.autrev.2022.103097, 2022) (cvikova2024casereportsusac pages 7-8, david2022susacsyndromea pages 1-2) |
| Vessel-wall / black-blood MRI | Black-blood high-resolution vessel-wall MRI can show circumferential wall thickening/enhancement and periarterial/periadventitial enhancement, interpreted as inflammatory endothelial injury/vasculopathy. | Consider when standard MRI is nondiagnostic, differential includes CNS vasculitis/MS, or when monitoring suspected ongoing vascular inflammatory activity. Best viewed as an adjunct, not a replacement for standard MRI + retinal/audiologic testing. | RadLex: Vessel wall MRI; black-blood MRI. | Front Neurol review/case report (https://doi.org/10.3389/fneur.2024.1339438, 2024) (cvikova2024casereportsusac pages 1-2, cvikova2024casereportsusac pages 7-8) |
| Retinal fluorescein angiography (FFA/FA) | Hallmark retinal findings: branch retinal artery occlusions (BRAO), arterial wall hyperfluorescence (AWH), and later microaneurysms. BRAOs may be clinically silent; FFA is often diagnostic even when fundus exam is subtle. | Order FA/FFA in **all** suspected SuS cases, even without visual complaints. Repeat during follow-up/relapse surveillance, since retinal activity may recur and may be more frequent within first 2 years. | HPO: Branch retinal artery occlusion; Scotoma; Visual field defect. RadLex: Fluorescein angiography. | Neurol Neuroimmunol Neuroinflamm cohort (https://doi.org/10.1212/NXI.0000000000200357, 2025); Front Neurol review (https://doi.org/10.3389/fneur.2024.1339438, 2024) (fuchs2025clinicalcharacterizationand pages 1-2, cvikova2024casereportsusac pages 7-8) |
| OCT / SD-OCT | SD-OCT can show characteristic signs of retinal branch ischemia; OCT was used in real-world cohorts to detect acute swelling and chronic ischemic thinning corresponding to BRAO territories. Helpful when fundoscopy is normal/subtle. | Add OCT/SD-OCT alongside FFA, especially if ophthalmic symptoms are absent or minimal. Useful for baseline documentation and longitudinal monitoring of retinal structural damage. | RadLex: Optical coherence tomography; spectral-domain OCT. HPO: Retinal ischemia; Visual field defect. | Front Neurol review (https://doi.org/10.3389/fneur.2024.1339438, 2024); BMC Neurol case series (https://doi.org/10.1186/s12883-020-01892-0, 2020) (cvikova2024casereportsusac pages 7-8, wilfyarkoni2020increasedincidenceof pages 2-3) |
| Audiogram / vestibulocochlear testing | Tonal audiogram typically shows sensorineural hearing loss affecting low-to-middle frequencies, often due to apical cochlear infarction; audiogram becomes abnormal in almost all tested patients. Vestibular testing may support peripheral vertigo. | Order audiogram at baseline in any suspected or confirmed case, even if hearing symptoms are mild. Add vestibular testing (e.g., calorics/VEMP/video head impulse) if vertigo or imbalance is reported. High-frequency loss does **not** exclude SuS. | HPO: Sensorineural hearing impairment; Tinnitus; Vertigo. LOINC/general: audiogram/hearing assessment. | Front Neurol review (https://doi.org/10.3389/fneur.2024.1339438, 2024); Neurol Neuroimmunol Neuroinflamm cohort (https://doi.org/10.1212/NXI.0000000000200357, 2025) (cvikova2024casereportsusac pages 7-8, fuchs2025clinicalcharacterizationand pages 1-2) |
| CSF profile | Typical CSF pattern is pauci-inflammatory: mild to moderate protein elevation, mild lymphocytic pleocytosis in up to ~45%, and oligoclonal bands/intrathecal IgG synthesis are rare. In one 2023 series, 12/14 had raised protein and OCBs were absent in all 13 tested. | Perform CSF mainly to support diagnosis and exclude mimics (MS, infection, ADEM, vasculitis). SuS CSF usually supports a non-MS inflammatory microangiopathy rather than classic demyelinating disease. | LOINC/general: CSF total protein; CSF white blood cell count; CSF oligoclonal bands. HPO: Elevated CSF protein; CSF pleocytosis. | J Neurol 2023 (https://doi.org/10.1007/s00415-023-11891-z, 2023); Front Neurol 2024 (https://doi.org/10.3389/fneur.2024.1339438, 2024) (bose2023susacsyndromeneurological pages 1-2, cvikova2024casereportsusac pages 7-8) |
| Histopathology / mechanistic adjuncts | Brain pathology shows multiple microinfarcts, endothelial cell necrosis, perivascular lymphocytic infiltration; complement deposition (C4d) seen in a subset (~30% of vessels in one case series). AECA are present in only a subset of patients, so not currently a routine standalone diagnostic biomarker. | Biopsy is not routine; reserve for highly atypical cases or when alternative diagnoses remain strongly suspected. Mechanistic findings support autoimmune endotheliopathy but are not required for bedside diagnosis. | GO: complement activation; leukocyte adhesion; endothelial cell injury. CL: CD8-positive alpha-beta T cell; endothelial cell. | J Neurol 2023 (https://doi.org/10.1007/s00415-023-11891-z, 2023); J Neuroinflammation 2014 (https://doi.org/10.1186/1742-2094-11-46, 2014); Nat Commun 2019 (https://doi.org/10.1038/s41467-019-13593-5, 2019) (bose2023susacsyndromeneurological pages 1-2, jarius2014clinicalparaclinicaland pages 1-2, gross2019cd8+tcellmediated pages 1-2) |
| Real-world diagnostic workflow | Practical workup in contemporary cohorts combines neurology + ophthalmology + otology review with MRI, FFA/OCT, audiogram/vestibular testing, and CSF. Prospective cohorts/registries are using the same multimodal workup plus neurocognitive and disability scales. | In routine care, if SuS is suspected: order brain MRI with contrast, urgent FFA with OCT, audiogram, and CSF; repeat retina/ear testing because domains can emerge sequentially. Natural-history studies are collecting these same tests prospectively, showing these are current real-world implementations rather than experimental-only tools. | HPO: Cognitive impairment; Visual field defect; Sensorineural hearing impairment. RadLex: MRI/FFA/OCT. Functional scales used in cohorts: MoCA, mRS, SF-36, Barthel. | Neurol Neuroimmunol Neuroinflamm 2025 (https://doi.org/10.1212/NXI.0000000000200357, 2025); ClinicalTrials.gov NCT06881368, NCT01481662, NCT01273792 (2010–2025 registry records) (fuchs2025clinicalcharacterizationand pages 1-2, NCT01273792 chunk 1, NCT06881368 chunk 2, NCT01481662 chunk 1, NCT06881368 chunk 1) |


*Table: This table summarizes the main diagnostic domains, tests, and real-world workflow for Susac syndrome, including imaging, ophthalmic, audiologic, and CSF findings. It is useful as a knowledge-base-ready quick reference linking practical clinical actions with ontology suggestions and primary sources.*

### 10.3 Visual evidence (table/figures)
- EuSaC diagnostic criteria table and example imaging (MRI “snowballs”; retinal angiography features) were extracted from a 2024 Frontiers in Neurology paper. (cvikova2024casereportsusac media 1cd8097f, cvikova2024casereportsusac media 4d784135, cvikova2024casereportsusac media bcac5361, cvikova2024casereportsusac media 5a95f86e)

### 10.4 Differential diagnosis (examples noted in protocols)
Prospective cohort protocols explicitly exclude key mimics such as multiple sclerosis, CADASIL, mitochondrial disease, CNS tumors, and Lyme disease, reflecting real-world diagnostic workups. (NCT06881368 chunk 2, NCT01481662 chunk 1)

---

## 11. Outcome / Prognosis

### 11.1 Functional outcomes
In a multicenter cohort (n=20):
- **Cognitive function improved in 75%** during follow-up. (fuchs2025clinicalcharacterizationand pages 1-2)
- **~50% resumed employment; 25% did not return to work**, indicating persistent morbidity in a substantial subset. (fuchs2025clinicalcharacterizationand pages 1-2)

### 11.2 Prognostic factors
Severe cerebral involvement at onset, male sex, and elevated CSF protein were associated with worse prognosis in disability/dependency in one multicenter study. (fuchs2025clinicalcharacterizationand pages 1-2)

---

## 12. Treatment

### 12.1 Current approach (evidence type: expert consensus + observational)
There are **no randomized controlled trials**; treatment is guided by expert consensus, retrospective series, and analogy to other immune-mediated microvascular diseases. (fuchs2025clinicalcharacterizationand pages 1-2, david2022susacsyndromea pages 4-5)

Commonly described regimens include:
- **High-dose corticosteroids** (e.g., IV methylprednisolone induction followed by slow taper) (david2022susacsyndromea pages 4-5, bose2023susacsyndromeneurological pages 1-2)
- **IVIG** as induction/relapse management or adjunct, often used more frequently in relapsing disease (bose2023susacsyndromeneurological pages 1-2, david2022susacsyndromea pages 4-5)
- **Escalation/maintenance immunosuppression**: mycophenolate mofetil, azathioprine, cyclophosphamide, rituximab (david2022susacsyndromea pages 4-5, cvikova2024casereportsusac pages 7-8)
- **Adjunct antiplatelet therapy** is frequently used (e.g., aspirin noted in an Austrian cohort; antiplatelet agents frequently used in reviews). (seifertheld2017susacssyndromeclinical pages 6-10, david2022susacsyndromea pages 4-5)

### 12.2 Treatment strategy / algorithm (real-world)
A 2023 UK series proposed a severity- and response-guided therapeutic algorithm based on long-term management experience, emphasizing early aggressive therapy in severe cases to reduce morbidity/disability. (bose2023susacsyndromeneurological pages 1-2)

### 12.3 Suggested MAXO terms (examples; to be mapped in ontology curation)
- High-dose glucocorticoid therapy; Intravenous immunoglobulin therapy; Immunosuppressive therapy; B-cell depletion therapy (rituximab); Therapeutic plasma exchange; Antiplatelet therapy.

---

## 13. Prevention

No established primary prevention is described in the retrieved evidence. Given rarity and unclear triggers, prevention focuses on:
- **Secondary/tertiary prevention via early recognition and aggressive treatment** to prevent irreversible brain/retinal/cochlear damage. (bose2023susacsyndromeneurological pages 1-2, bullock2023useofdisease pages 1-2)

---

## 14. Other Species / Natural Disease

No naturally occurring SuS analog in non-human species was identified in the retrieved evidence.

---

## 15. Model Organisms

A **transgenic mouse model** recapitulating key features of SuS-like CTL-mediated endotheliopathy was reported in a major mechanistic study and was used to demonstrate benefit of anti-α4 integrin intervention. (gross2019cd8+tcellmediated pages 1-2)

---

# Recent developments (prioritizing 2023–2024)

1. **Diagnostic sharpening and multimodal workflows (2023–2024):**
   - 2023 long-term UK experience emphasized “red flags,” characteristic callosal MRI lesions, and the need for ophthalmic FA/OCT because eye involvement may be subtle/silent. (bose2023susacsyndromeneurological pages 1-2)
   - 2024 Frontiers review emphasizes black-blood vessel-wall MRI and provides a concise operationalization of EuSaC criteria and updated imaging prevalence ranges. (cvikova2024casereportsusac pages 7-8)

2. **Neuropsychiatric/cognitive phenotype focus (2024):**
   - 2024 review highlights gaps in standardized cognitive phenotyping and calls for longitudinal data capture and treatment-outcome correlations in neuropsychiatric domains. (koncz2024theneurocognitiveand pages 1-2)

3. **Real-world research infrastructure (ongoing):**
   - Multiple prospective observational cohorts and biomarker studies are active/registered (France AP-HP CARESS cohorts; Charité biomarker study), indicating field-wide movement toward standardized phenotyping, biospecimen banking, and imaging biomarkers (DTI, OCT, MRI). (NCT01273792 chunk 1, NCT01481662 chunk 1, NCT06881368 chunk 1)

---

# Current applications / real-world implementations

- **Clinical implementation of multimodal triad testing:** brain MRI + fluorescein angiography/OCT + audiometry/vestibular testing is explicitly used in real-world cohorts and is also embedded in prospective registries/trials. (wilfyarkoni2020increasedincidenceof pages 2-3, NCT01481662 chunk 1)
- **Monitoring tools and biomarkers:** fluorescein angiography is described as an excellent biomarker of retinal disease activity, though not necessarily reflective of brain/ear activity; formal symptom/damage scoring tools have been proposed to standardize longitudinal assessment. (bullock2023useofdisease pages 1-2)

---

# Evidence limitations (for knowledge-base curation)

- **Coding identifiers (Orphanet/MONDO/MeSH/ICD/OMIM)** were not extractable from the retrieved full text; populate via direct terminology database lookup. 
- Many treatment conclusions rely on **observational evidence and expert opinion**; RCTs are not available in retrieved sources. (david2022susacsyndromea pages 4-5, fuchs2025clinicalcharacterizationand pages 1-2)
- Genetic causality is not established in these sources.

---

# URLs and publication dates (examples of key sources cited)

- Bose et al. *Journal of Neurology* — Published online **22 Aug 2023**. https://doi.org/10.1007/s00415-023-11891-z (bose2023susacsyndromeneurological pages 1-2)  
- Koncz et al. *Neurological Sciences* — Published online **2 Jul 2024**. https://doi.org/10.1007/s10072-024-07672-9 (koncz2024theneurocognitiveand pages 1-2)  
- Cviková et al. *Frontiers in Neurology* — **Feb 2024**. https://doi.org/10.3389/fneur.2024.1339438 (cvikova2024casereportsusac pages 7-8)  
- Gross et al. *Nature Communications* — **2019**. https://doi.org/10.1038/s41467-019-13593-5 (gross2019cd8+tcellmediated pages 1-2)  
- Jarius et al. *Journal of Neuroinflammation* — **2014**. https://doi.org/10.1186/1742-2094-11-46 (jarius2014clinicalparaclinicaland pages 1-2)  
- Seifert-Held et al. *International Journal of Neuroscience* — **Sep 2017**. https://doi.org/10.1080/00207454.2016.1254631 (seifertheld2017susacssyndromeclinical pages 6-10)  
- ClinicalTrials.gov: NCT01273792 (2010), NCT01481662 (2011), NCT06881368 (2025). (NCT01273792 chunk 1, NCT01481662 chunk 1, NCT06881368 chunk 1)


References

1. (bose2023susacsyndromeneurological pages 1-2): Smriti Bose, Athanasios Papathanasiou, Sameep Karkhanis, Jason P. Appleton, Dominic King, Ruchika Batra, Susan P. Mollan, and Saiju Jacob. Susac syndrome: neurological update (clinical features, long-term observational follow-up and management of sixteen patients). Journal of Neurology, 270:6193-6206, Aug 2023. URL: https://doi.org/10.1007/s00415-023-11891-z, doi:10.1007/s00415-023-11891-z. This article has 28 citations and is from a domain leading peer-reviewed journal.

2. (david2022susacsyndromea pages 1-2): Clémence David, Karim Sacré, Marie-Cécile Henri-Feugeas, Isabelle Klein, Serge Doan, Fleur Aubart Cohen, Eric Jouvent, and Thomas Papo. Susac syndrome: a scoping review. Autoimmunity Reviews, 21:103097, Jun 2022. URL: https://doi.org/10.1016/j.autrev.2022.103097, doi:10.1016/j.autrev.2022.103097. This article has 55 citations and is from a peer-reviewed journal.

3. (jarius2014clinicalparaclinicaland pages 1-2): Sven Jarius, Ilka Kleffner, Jan M Dörr, Jaume Sastre-Garriga, Zsolt Illes, Eric Eggenberger, Colin Chalk, Marius Ringelstein, Orhan Aktas, Xavier Montalban, Kai Fechner, Winfried Stöcker, Erich B Ringelstein, Friedemann Paul, and Brigitte Wildemann. Clinical, paraclinical and serological findings in susac syndrome: an international multicenter study. Journal of Neuroinflammation, 11:46, Mar 2014. URL: https://doi.org/10.1186/1742-2094-11-46, doi:10.1186/1742-2094-11-46. This article has 165 citations and is from a peer-reviewed journal.

4. (bullock2023useofdisease pages 1-2): Danielle R. Bullock, Robert T. Spencer, Richard K. Vehe, Sunil Srivastava, and Robert M. Rennebohm. Use of disease assessment tools to increase the value of case reports on susac syndrome: two case reports. Journal of Medical Case Reports, Apr 2023. URL: https://doi.org/10.1186/s13256-023-03838-9, doi:10.1186/s13256-023-03838-9. This article has 2 citations and is from a peer-reviewed journal.

5. (fuchs2025clinicalcharacterizationand pages 1-2): Lior Fuchs, Adi Wilf-Yarkoni, Hadar Kolb, Ifat Vigiser, Keren Regev, Dinah Zur, Zohar Habot-Wilner, Yahav Oron, Viktoria Furer, Nitai Shimon, Mark A. Hellmann, Itay Lotan, Eitan Auriel, Robert Rennebohm, Ori Elkayam, and Arnon Karni. Clinical characterization and prognostic risk factors of susac syndrome. Neurology Neuroimmunology &amp; Neuroinflammation, Mar 2025. URL: https://doi.org/10.1212/nxi.0000000000200357, doi:10.1212/nxi.0000000000200357. This article has 5 citations.

6. (NCT01273792 chunk 1): Jan-Markus Dörr. Investigation of Biomarkers in Susac Syndrome. Charite University, Berlin, Germany. 2010. ClinicalTrials.gov Identifier: NCT01273792

7. (NCT01481662 chunk 1):  Epidemiological, Clinical and Etiological Features of SUSAC's Syndrome. Assistance Publique - Hôpitaux de Paris. 2011. ClinicalTrials.gov Identifier: NCT01481662

8. (NCT06881368 chunk 1):  Phenotypic and Etiological Characterization of Susac Syndrome. Assistance Publique - Hôpitaux de Paris. 2025. ClinicalTrials.gov Identifier: NCT06881368

9. (gross2019cd8+tcellmediated pages 1-2): Catharina C. Gross, Céline Meyer, Urvashi Bhatia, Lidia Yshii, Ilka Kleffner, Jan Bauer, Anna R. Tröscher, Andreas Schulte-Mecklenbeck, Sebastian Herich, Tilman Schneider-Hohendorf, Henrike Plate, Tanja Kuhlmann, Markus Schwaninger, Wolfgang Brück, Marc Pawlitzki, David-Axel Laplaud, Delphine Loussouarn, John Parratt, Michael Barnett, Michael E. Buckland, Todd A. Hardy, Stephen W. Reddel, Marius Ringelstein, Jan Dörr, Brigitte Wildemann, Markus Kraemer, Hans Lassmann, Romana Höftberger, Eduardo Beltrán, Klaus Dornmair, Nicholas Schwab, Luisa Klotz, Sven G. Meuth, Guillaume Martin-Blondel, Heinz Wiendl, and Roland Liblau. Cd8+ t cell-mediated endotheliopathy is a targetable mechanism of neuro-inflammation in susac syndrome. Nature Communications, Dec 2019. URL: https://doi.org/10.1038/s41467-019-13593-5, doi:10.1038/s41467-019-13593-5. This article has 150 citations and is from a highest quality peer-reviewed journal.

10. (seifertheld2017susacssyndromeclinical pages 6-10): Thomas Seifert-Held, Beate J. Langner-Wegscheider, Martina Komposch, Philipp Simschitz, Claudia Franta, Barbara Teuchner, Hans Offenbacher, Ferdinand Otto, Johann Sellner, Helmut Rauschka, and Franz Fazekas. Susac's syndrome: clinical course and epidemiology in a central european population. International Journal of Neuroscience, 127:776-780, Sep 2017. URL: https://doi.org/10.1080/00207454.2016.1254631, doi:10.1080/00207454.2016.1254631. This article has 65 citations and is from a peer-reviewed journal.

11. (wilfyarkoni2020increasedincidenceof pages 2-3): A. Wilf-Yarkoni, O. Elkayam, O. Elkayam, O. Aizenstein, Y. Oron, V. Furer, V. Furer, Dinah Zur, Dinah Zur, M. Goldstein, M. Goldstein, D. Barequet, D. Barequet, H. Hallevi, A. Karni, A. Karni, Z. Habot-Wilner, Z. Habot-Wilner, and K. Regev. Increased incidence of susac syndrome: a case series study. BMC Neurology, Sep 2020. URL: https://doi.org/10.1186/s12883-020-01892-0, doi:10.1186/s12883-020-01892-0. This article has 37 citations and is from a peer-reviewed journal.

12. (bose2023susacsyndromeneurological pages 6-8): Smriti Bose, Athanasios Papathanasiou, Sameep Karkhanis, Jason P. Appleton, Dominic King, Ruchika Batra, Susan P. Mollan, and Saiju Jacob. Susac syndrome: neurological update (clinical features, long-term observational follow-up and management of sixteen patients). Journal of Neurology, 270:6193-6206, Aug 2023. URL: https://doi.org/10.1007/s00415-023-11891-z, doi:10.1007/s00415-023-11891-z. This article has 28 citations and is from a domain leading peer-reviewed journal.

13. (koncz2024theneurocognitiveand pages 1-2): Rebecca Koncz, Miranda J. Say, Andrew Gleason, and Todd A. Hardy. The neurocognitive and neuropsychiatric manifestations of susac syndrome: a brief review of the literature and future directions. Neurological Sciences, 45:5181-5187, Jul 2024. URL: https://doi.org/10.1007/s10072-024-07672-9, doi:10.1007/s10072-024-07672-9. This article has 2 citations and is from a peer-reviewed journal.

14. (bose2023susacsyndromeneurological pages 5-6): Smriti Bose, Athanasios Papathanasiou, Sameep Karkhanis, Jason P. Appleton, Dominic King, Ruchika Batra, Susan P. Mollan, and Saiju Jacob. Susac syndrome: neurological update (clinical features, long-term observational follow-up and management of sixteen patients). Journal of Neurology, 270:6193-6206, Aug 2023. URL: https://doi.org/10.1007/s00415-023-11891-z, doi:10.1007/s00415-023-11891-z. This article has 28 citations and is from a domain leading peer-reviewed journal.

15. (jarius2014clinicalparaclinicaland pages 8-9): Sven Jarius, Ilka Kleffner, Jan M Dörr, Jaume Sastre-Garriga, Zsolt Illes, Eric Eggenberger, Colin Chalk, Marius Ringelstein, Orhan Aktas, Xavier Montalban, Kai Fechner, Winfried Stöcker, Erich B Ringelstein, Friedemann Paul, and Brigitte Wildemann. Clinical, paraclinical and serological findings in susac syndrome: an international multicenter study. Journal of Neuroinflammation, 11:46, Mar 2014. URL: https://doi.org/10.1186/1742-2094-11-46, doi:10.1186/1742-2094-11-46. This article has 165 citations and is from a peer-reviewed journal.

16. (cvikova2024casereportsusac pages 1-2): Martina Cviková, Jakub Štefela, Vít Všianský, Michal Dufek, Irena Doležalová, Jan Vinklárek, Roman Herzig, Markéta Zemanová, Vladimír Červeňák, Jaroslav Brichta, Veronika Bárková, David Kouřil, Petr Aulický, Pavel Filip, and Viktor Weiss. Case report: susac syndrome—two ends of the spectrum, single center case reports and review of the literature. Frontiers in Neurology, Feb 2024. URL: https://doi.org/10.3389/fneur.2024.1339438, doi:10.3389/fneur.2024.1339438. This article has 8 citations and is from a peer-reviewed journal.

17. (cvikova2024casereportsusac pages 7-8): Martina Cviková, Jakub Štefela, Vít Všianský, Michal Dufek, Irena Doležalová, Jan Vinklárek, Roman Herzig, Markéta Zemanová, Vladimír Červeňák, Jaroslav Brichta, Veronika Bárková, David Kouřil, Petr Aulický, Pavel Filip, and Viktor Weiss. Case report: susac syndrome—two ends of the spectrum, single center case reports and review of the literature. Frontiers in Neurology, Feb 2024. URL: https://doi.org/10.3389/fneur.2024.1339438, doi:10.3389/fneur.2024.1339438. This article has 8 citations and is from a peer-reviewed journal.

18. (bose2023susacsyndromeneurological pages 8-9): Smriti Bose, Athanasios Papathanasiou, Sameep Karkhanis, Jason P. Appleton, Dominic King, Ruchika Batra, Susan P. Mollan, and Saiju Jacob. Susac syndrome: neurological update (clinical features, long-term observational follow-up and management of sixteen patients). Journal of Neurology, 270:6193-6206, Aug 2023. URL: https://doi.org/10.1007/s00415-023-11891-z, doi:10.1007/s00415-023-11891-z. This article has 28 citations and is from a domain leading peer-reviewed journal.

19. (vodopivec2016treatmentofsusac pages 1-3): Ivana Vodopivec and Sashank Prasad. Treatment of susac syndrome. Current Treatment Options in Neurology, 18:1-8, Dec 2016. URL: https://doi.org/10.1007/s11940-015-0386-x, doi:10.1007/s11940-015-0386-x. This article has 48 citations and is from a peer-reviewed journal.

20. (seifertheld2017susacssyndromeclinical pages 1-6): Thomas Seifert-Held, Beate J. Langner-Wegscheider, Martina Komposch, Philipp Simschitz, Claudia Franta, Barbara Teuchner, Hans Offenbacher, Ferdinand Otto, Johann Sellner, Helmut Rauschka, and Franz Fazekas. Susac's syndrome: clinical course and epidemiology in a central european population. International Journal of Neuroscience, 127:776-780, Sep 2017. URL: https://doi.org/10.1080/00207454.2016.1254631, doi:10.1080/00207454.2016.1254631. This article has 65 citations and is from a peer-reviewed journal.

21. (cvikova2024casereportsusac media 1cd8097f): Martina Cviková, Jakub Štefela, Vít Všianský, Michal Dufek, Irena Doležalová, Jan Vinklárek, Roman Herzig, Markéta Zemanová, Vladimír Červeňák, Jaroslav Brichta, Veronika Bárková, David Kouřil, Petr Aulický, Pavel Filip, and Viktor Weiss. Case report: susac syndrome—two ends of the spectrum, single center case reports and review of the literature. Frontiers in Neurology, Feb 2024. URL: https://doi.org/10.3389/fneur.2024.1339438, doi:10.3389/fneur.2024.1339438. This article has 8 citations and is from a peer-reviewed journal.

22. (NCT06881368 chunk 2):  Phenotypic and Etiological Characterization of Susac Syndrome. Assistance Publique - Hôpitaux de Paris. 2025. ClinicalTrials.gov Identifier: NCT06881368

23. (cvikova2024casereportsusac media 4d784135): Martina Cviková, Jakub Štefela, Vít Všianský, Michal Dufek, Irena Doležalová, Jan Vinklárek, Roman Herzig, Markéta Zemanová, Vladimír Červeňák, Jaroslav Brichta, Veronika Bárková, David Kouřil, Petr Aulický, Pavel Filip, and Viktor Weiss. Case report: susac syndrome—two ends of the spectrum, single center case reports and review of the literature. Frontiers in Neurology, Feb 2024. URL: https://doi.org/10.3389/fneur.2024.1339438, doi:10.3389/fneur.2024.1339438. This article has 8 citations and is from a peer-reviewed journal.

24. (cvikova2024casereportsusac media bcac5361): Martina Cviková, Jakub Štefela, Vít Všianský, Michal Dufek, Irena Doležalová, Jan Vinklárek, Roman Herzig, Markéta Zemanová, Vladimír Červeňák, Jaroslav Brichta, Veronika Bárková, David Kouřil, Petr Aulický, Pavel Filip, and Viktor Weiss. Case report: susac syndrome—two ends of the spectrum, single center case reports and review of the literature. Frontiers in Neurology, Feb 2024. URL: https://doi.org/10.3389/fneur.2024.1339438, doi:10.3389/fneur.2024.1339438. This article has 8 citations and is from a peer-reviewed journal.

25. (cvikova2024casereportsusac media 5a95f86e): Martina Cviková, Jakub Štefela, Vít Všianský, Michal Dufek, Irena Doležalová, Jan Vinklárek, Roman Herzig, Markéta Zemanová, Vladimír Červeňák, Jaroslav Brichta, Veronika Bárková, David Kouřil, Petr Aulický, Pavel Filip, and Viktor Weiss. Case report: susac syndrome—two ends of the spectrum, single center case reports and review of the literature. Frontiers in Neurology, Feb 2024. URL: https://doi.org/10.3389/fneur.2024.1339438, doi:10.3389/fneur.2024.1339438. This article has 8 citations and is from a peer-reviewed journal.

26. (david2022susacsyndromea pages 4-5): Clémence David, Karim Sacré, Marie-Cécile Henri-Feugeas, Isabelle Klein, Serge Doan, Fleur Aubart Cohen, Eric Jouvent, and Thomas Papo. Susac syndrome: a scoping review. Autoimmunity Reviews, 21:103097, Jun 2022. URL: https://doi.org/10.1016/j.autrev.2022.103097, doi:10.1016/j.autrev.2022.103097. This article has 55 citations and is from a peer-reviewed journal.