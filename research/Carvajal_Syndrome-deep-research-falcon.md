---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-04-26T02:15:14.137184'
end_time: '2026-04-26T02:15:14.141395'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Carvajal Syndrome
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Carvajal Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Carvajal Syndrome** covering all of the
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
- **Disease Name:** Carvajal Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Carvajal Syndrome** covering all of the
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


# Carvajal Syndrome (Genetic Cardiocutaneous Syndrome) — Comprehensive Disease Characteristics Report

## Target Disease
- **Disease name:** Carvajal syndrome
- **Category:** Genetic cardiocutaneous syndrome (desmosomal disease)
- **Probable MONDO concept(s) observed in retrieved curated evidence:** *arrhythmogenic cardiomyopathy with wooly hair and keratoderma* (**MONDO:0011581**) (sun2021hairandskin pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
Carvajal syndrome is a rare inherited **cardiocutaneous disorder** classically defined by the triad of **woolly/curly hair**, **palmoplantar keratoderma (often striate/focal)**, and **predominantly left-ventricular (LV) cardiomyopathy** that often presents in childhood and may progress to heart failure, malignant ventricular arrhythmias, sudden death, or need for heart transplantation. It is most commonly caused by **pathogenic variants in the desmosomal gene DSP (desmoplakin)**, reflecting shared reliance of epidermis and myocardium on desmosome-mediated mechanical coupling. (sun2021hairandskin pages 4-5, karvonen2022anoveldesmoplakin pages 8-8)

### 1.2 Key identifiers and ontology mappings (from retrieved sources)
- **OMIM:** Carvajal syndrome **OMIM #605656** (review) (sun2021hairandskin pages 1-2). Another excerpt cites **MIM #605,676** in the context of “dilated cardiomyopathy with wooly hair and keratoderma” (Carvajal syndrome) (binfadel2025genotypeandcardiac pages 1-2).
- **Related disorder (for differential/synonymy):** Naxos disease **OMIM #601214** (sun2021hairandskin pages 1-2).
- **MONDO:** In Open Targets curated associations, the closely aligned disease concept is **“arrhythmogenic cardiomyopathy with wooly hair and keratoderma” (MONDO_0011581)** linked to **DSP** (sun2021hairandskin pages 1-2).
- **ICD-10/ICD-11, MeSH, Orphanet:** Not explicitly present in the retrieved full-text excerpts; mapping should therefore be confirmed in those databases separately (limitation of current evidence set). (sun2021hairandskin pages 1-2, binfadel2025genotypeandcardiac pages 1-2)

### 1.3 Synonyms / alternative names
- **“Naxos disease variant”** (explicitly used as *Naxos disease variant (Carvajal syndrome)*) (binfadel2025genotypeandcardiac pages 1-2).
- Combined/overlapping nomenclature in the literature includes: **“Naxos-Carvajal disease,” “Carvajal/Naxos syndrome,” “Naxos-like syndrome,”** reflecting phenotypic overlap between desmosomal cardiocutaneous disorders. (molho‐pessach2015twonovelhomozygous pages 5-6)

### 1.4 Evidence provenance: individual vs aggregated resources
Most available information in the retrieved set is derived from **case reports/series**, small cohorts, and **systematic or narrative reviews** rather than large EHR-based datasets, which is typical for ultra-rare syndromes. (sun2021hairandskin pages 1-2, binfadel2025genotypeandcardiac pages 1-2, polivka2016combinationofpalmoplantar pages 2-3)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline **DSP (desmoplakin)** variants causing defective desmosome structure/function, resulting in combined skin/hair and myocardial disease (a “desmosomal disease”). (sun2021hairandskin pages 1-2, karvonen2022anoveldesmoplakin pages 8-8)

**Abstract-supported primary claim (quote):** A review of DSP cardiomyopathy notes: “**The first association between DSP genetic variants and the presence of a myocardial disease referred to patients with Carvajal syndrome.**” (Apr 2023; URL: https://doi.org/10.3390/jcm12072660) (brandao2023desmoplakincardiomyopathycomprehensive pages 1-2)

### 2.2 Risk factors
- **Genetic risk factors (causal):** Bi-allelic (homozygous or compound heterozygous) **loss-of-function (LoF)** DSP variants are strongly associated with classic Carvajal syndrome; variant location influences cutaneous/cardiac patterns (see Genotype–Phenotype below). (sun2021hairandskin pages 4-5, molho‐pessach2015twonovelhomozygous pages 3-5, ziołkowska2024carvajalsyndromerelated pages 1-2, williams2011noveldesmoplakinmutation pages 2-5)
- **Family structure/consanguinity:** Consanguinity increases risk of homozygous disease, illustrated by a consanguineous pedigree with severe childhood cardiomyopathy. (williams2011noveldesmoplakinmutation pages 2-5, williams2011noveldesmoplakinmutation pages 1-2)

### 2.3 Protective factors
No specific genetic or environmental protective factors were identified in the retrieved evidence excerpts.

### 2.4 Gene–environment interactions
No direct GxE studies were identified in the retrieved evidence excerpts. However, the desmosomal mechanism implies that **mechanical stress** could plausibly modulate myocardial injury risk; this remains to be substantiated by disease-specific studies (not established in the provided sources).

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (with characteristics)
**Classic triad (high-level):**
- **Woolly/curly hair** (often congenital)
- **Palmoplantar keratoderma (PPK)** (often striate or focal; tends to appear in early childhood)
- **Cardiomyopathy** (commonly LV-dominant dilated/arrhythmogenic phenotype; childhood onset) (sun2021hairandskin pages 4-5, karvonen2022anoveldesmoplakin pages 8-8, polivka2016combinationofpalmoplantar pages 2-3)

**Representative image evidence:** A 2024 Carvajal case report shows cutaneous findings (woolly hair and palmoplantar keratoderma) and a 4-chamber cardiac MRI with dilated ventricles and reduced systolic function (Sep 2024; URL: https://doi.org/10.33963/v.phj.101664). (ziołkowska2024carvajalsyndromerelated media 9732cda8)

**Additional/variable features reported in reviews/series:** poor dentition/enamel defects, nail dystrophy, ichthyosis/erythrokeratodermia-spectrum skin changes in related DSP cardiocutaneous phenotypes. (sun2021hairandskin pages 4-5)

### 3.2 Age of onset / progression
- Hair findings can be evident at birth; keratoderma often appears in toddler age and can precede cardiac disease, serving as an early clinical cue. (williams2011noveldesmoplakinmutation pages 1-2)
- In a systematic review of genetic desmosomal diseases with PPK + hair anomalies, the **median age of first cardiac manifestation was 8 years** (range 3–35). (polivka2016combinationofpalmoplantar pages 2-3)

### 3.3 Frequency statistics (recently cited quantitative data)
- **Systematic review evidence (2016):** In 458 desmosomal disease patients analyzed, the **combination of PPK + hair shaft anomalies** was associated with high cardiac risk: **129/161 (80.1%)** had cardiac disease, and skin features had led to cardiac monitoring in only 2.3%. (Sep 2016; URL: https://doi.org/10.1136/jmedgenet-2015-103403) (polivka2016combinationofpalmoplantar pages 2-3)
- **Pediatric cohort outcomes (2025):** In a Saudi cohort of 10 pediatric patients with “Naxos disease variant” (Carvajal syndrome), all had woolly hair, half had PPK, 9/10 had frequent PVCs, 3 received ICDs, 4 underwent heart transplantation, and 3 died while waiting for transplant; 8/10 were homozygous for DSP mutations. (Mar 2025; URL: https://doi.org/10.1186/s13023-025-03612-8) (binfadel2025genotypeandcardiac pages 1-2)

### 3.4 Quality of life impact
Direct validated QoL instrument results (e.g., SF-36, EQ-5D) were not identified in the retrieved excerpts. Clinically, progressive heart failure, ICD shocks, transplantation, and visible cutaneous manifestations imply major QoL burden. (binfadel2025genotypeandcardiac pages 1-2, ziołkowska2024carvajalsyndromerelated pages 1-2)

### 3.5 Suggested HPO terms (non-exhaustive)
- **Woolly hair:** HP:0002210
- **Curly hair:** HP:0002224
- **Palmoplantar keratoderma:** HP:0000972
- **Striate palmoplantar keratoderma:** HP:0007574
- **Dilated cardiomyopathy:** HP:0001644
- **Arrhythmogenic cardiomyopathy:** HP:0031677
- **Ventricular tachycardia:** HP:0004756
- **Premature ventricular contractions:** HP:0011703
- **Heart failure:** HP:0001635
- **Myocardial fibrosis (imaging/pathology):** HP:0012337
- **Left ventricular noncompaction (subset):** HP:0001695 (supported by a Carvajal family report) (williams2011noveldesmoplakinmutation pages 2-5)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **DSP (desmoplakin)** is the primary causal gene for classic Carvajal syndrome. (sun2021hairandskin pages 1-2, karvonen2022anoveldesmoplakin pages 8-8)

### 4.2 Pathogenic variant classes and examples (from retrieved primary reports)
**Loss-of-function (LoF) is a common mechanism**:
- **Homozygous DSP frameshift truncation:** 5208_5209delAG → frameshift downstream of amino acid 1736 with premature truncation of the predominant cardiac isoform DSP-1; associated with severe early-onset biventricular cardiomyopathy, woolly hair, and acantholytic PPK. (Jul 2011; URL: https://doi.org/10.1007/s00392-011-0345-9) (williams2011noveldesmoplakinmutation pages 2-5, williams2011noveldesmoplakinmutation pages 1-2)
- **Compound heterozygous DSP variants (2024 case):** de novo truncation **c.1339C>T** and a paternally inherited missense **c.8204G>C (p.Gly2735Ala)** associated with severe biventricular cardiomyopathy and arrhythmia requiring transplant; the missense was reported as extremely rare in gnomAD in the case report narrative. (Sep 2024; URL: https://doi.org/10.33963/v.phj.101664) (ziołkowska2024carvajalsyndromerelated pages 1-2)

**Genotype–phenotype correlation clues (review-level):** DSP variant location appears to correlate with cardiocutaneous phenotype patterns; truncations removing the C-terminus are emphasized in classic Carvajal syndrome, while other domain-localized variants can yield overlapping dominant or recessive DSP cardiomyopathy phenotypes. (sun2021hairandskin pages 4-5)

### 4.3 Variant interpretation framework
The retrieved case literature and reviews interpret truncating/LoF DSP variants as pathogenic and frequently invoke **nonsense-mediated decay (NMD) / haploinsufficiency** as a mechanism in some dominant DSP cardiocutaneous syndromes. (maruthappu2019loss‐of‐functiondesmoplakini pages 7-11, ziołkowska2024carvajalsyndromerelated pages 1-2)

### 4.4 Modifier genes / epigenetics
No validated modifier genes specific to Carvajal syndrome were identified in the retrieved excerpts.

**Research direction note:** A completed exploratory study tested feasibility of **cardiomyocyte-derived DNA** for genetic/epigenetic analyses of ACM genes including **DSP** (NCT03177018). (NCT03177018 chunk 1)

---

## 5. Environmental Information
No specific environmental, lifestyle, or infectious triggers were identified as causal in the retrieved evidence excerpts. The disease is primarily genetic, though clinical management often includes avoidance of arrhythmia triggers in broader ACM practice (not directly evidenced here).

---

## 6. Mechanism / Pathophysiology

### 6.1 Core mechanism (causal chain)
**Upstream trigger:** Germline DSP pathogenic variants → **desmosome dysfunction**.

**Cellular/tissue consequence:** Impaired anchoring of intermediate filaments (keratin/desmin) and altered desmosomal protein localization → compromised mechanical integrity and electrical coupling, contributing to **conduction defects**, myocardial injury and remodeling (fibrosis/fibrofatty replacement), and progressive cardiomyopathy. (maruthappu2019loss‐of‐functiondesmoplakini pages 7-11, brandao2023desmoplakincardiomyopathycomprehensive pages 1-2)

**Clinical manifestation:** LV-dominant or biventricular cardiomyopathy with ventricular arrhythmias and heart failure plus cutaneous phenotypes (woolly hair, PPK). (sun2021hairandskin pages 4-5, williams2011noveldesmoplakinmutation pages 2-5)

### 6.2 Mechanistic evidence highlights
- A dominant DSP cardiocutaneous cohort paper links DSP LoF to cardiac structural/electrical pathology, stating mislocalization of desmosomal proteins with reduced connexin 43 is associated with “**conduction defects, fibrofatty infiltration and cardiomyopathy**.” (Jan 2019; URL: https://doi.org/10.1111/bjd.17388) (maruthappu2019loss‐of‐functiondesmoplakini pages 7-11)
- A clinical review frames DSP as essential for cardiomyocyte cell-to-cell adhesion and summarizes the emerging entity of “desmoplakin cardiomyopathy,” characterized by LV involvement, extensive fibrosis, high arrhythmic risk, and episodes of acute myocardial injury, building historically from Carvajal syndrome observations. (Apr 2023; URL: https://doi.org/10.3390/jcm12072660) (brandao2023desmoplakincardiomyopathycomprehensive pages 1-2)

### 6.3 Suggested ontology terms
**GO biological process (examples):**
- Desmosome organization (GO:0031581)
- Cell-cell adhesion (GO:0098609)
- Intermediate filament organization (GO:0045109)
- Cardiac muscle tissue remodeling (GO:0055001)
- Regulation of cardiac conduction (e.g., GO terms around cardiac muscle cell action potential/conduction)

**Cell Ontology (CL) — key cell types implicated:**
- Keratinocyte (CL:0000312)
- Cardiomyocyte / cardiac muscle cell (CL:0000746)

**GO cellular component (examples):**
- Desmosome (GO:0030057)
- Intercalated disc (GO:0014704)

---

## 7. Anatomical Structures Affected

### 7.1 Organ-level
- **Heart** (primary): LV-dominant or biventricular cardiomyopathy with fibrosis and arrhythmia, often severe in pediatric cases. (binfadel2025genotypeandcardiac pages 1-2, ziołkowska2024carvajalsyndromerelated pages 1-2, williams2011noveldesmoplakinmutation pages 2-5)
- **Skin** (primary): palmoplantar keratoderma (including acantholytic variants in some reports). (williams2011noveldesmoplakinmutation pages 2-5, williams2011noveldesmoplakinmutation pages 1-2)
- **Hair** (primary): woolly/curly hair, often congenital. (sun2021hairandskin pages 4-5, ziołkowska2024carvajalsyndromerelated media 9732cda8)

### 7.2 Suggested UBERON terms
- Heart (UBERON:0000948)
- Left ventricle (UBERON:0002084)
- Right ventricle (UBERON:0002085)
- Palm skin (UBERON:0001514) and plantar skin (UBERON:0001516)
- Hair follicle (UBERON:0002074)

---

## 8. Temporal Development

### 8.1 Onset
- Cutaneous/hair findings often appear **early** (hair congenital; keratoderma in toddler age), potentially enabling pre-symptomatic identification of children at risk for cardiac death. (williams2011noveldesmoplakinmutation pages 1-2)

### 8.2 Progression / staging (clinical)
- Disease can progress from asymptomatic or mild early findings to **progressive ventricular dysfunction**, ventricular arrhythmias, syncope, and end-stage heart failure requiring transplant. (binfadel2025genotypeandcardiac pages 1-2, ziołkowska2024carvajalsyndromerelated pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Inheritance
- **Classically autosomal recessive** (homozygous/compound heterozygous DSP variants), with consanguinity frequently reported. (williams2011noveldesmoplakinmutation pages 2-5, williams2011noveldesmoplakinmutation pages 1-2)
- **Dominant DSP cardiocutaneous phenotypes** with Carvajal-like features have been described, underscoring variable expressivity and penetrance depending on variant class and location. (maruthappu2019loss‐of‐functiondesmoplakini pages 7-11)

### 9.2 Epidemiology
Robust prevalence/incidence estimates were not identified in the retrieved excerpts. The 2025 cohort and prior literature note geographic clustering and reports from regions including Greece/Turkey/Israel/Saudi Arabia/India/Ecuador, but these are not population-based estimates. (binfadel2025genotypeandcardiac pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical recognition
The combination of **woolly hair** and **PPK** (especially when distinct from family members) is emphasized as a clinical cue that should **prompt cardiac evaluation and genetic testing**. (sun2021hairandskin pages 1-2, karvonen2022anoveldesmoplakin pages 8-8, maruthappu2019loss‐of‐functiondesmoplakini pages 7-11)

### 10.2 Cardiac testing used in real-world practice (from cohorts/case reports)
- ECG and Holter monitoring to detect ventricular ectopy and VT (binfadel2025genotypeandcardiac pages 1-2, ziołkowska2024carvajalsyndromerelated pages 1-2)
- Echocardiography for ventricular size and systolic function (binfadel2025genotypeandcardiac pages 1-2)
- Cardiac MRI to evaluate ventricular dilation/dysfunction and fibrosis (ziołkowska2024carvajalsyndromerelated pages 1-2, ziołkowska2024carvajalsyndromerelated media 9732cda8)
- Biomarkers such as troponin/pro-BNP are suggested for DSP cardiomyopathy surveillance in a DSP-PPK context. (karvonen2022anoveldesmoplakin pages 8-8)

### 10.3 Genetic testing
Molecular confirmation via DSP sequencing (single-gene, panel, or exome) is used in reported cases and recommended when dermatologic warning signs are present. (karvonen2022anoveldesmoplakin pages 8-8, williams2011noveldesmoplakinmutation pages 2-5)

### 10.4 Differential diagnosis
- **Naxos disease** (typically JUP-related, classically more right-ventricular ARVC phenotype) vs Carvajal (more LV-dominant DCM/ACM) is repeatedly emphasized. (sun2021hairandskin pages 4-5, binfadel2025genotypeandcardiac pages 1-2)
- Other desmosomal cardiocutaneous disorders with PPK + hair anomalies (systematic review context). (polivka2016combinationofpalmoplantar pages 2-3)

---

## 11. Outcome / Prognosis

### 11.1 Prognostic patterns
- Severe pediatric disease may lead to transplantation or early death; in the 10-patient Saudi pediatric cohort, 4 underwent transplant and 3 died awaiting transplant. (binfadel2025genotypeandcardiac pages 1-2)
- Reviews summarize a high-risk course where a substantial fraction develop heart failure and many die before early adulthood without intervention, though survival into adulthood is reported in some families/cases. (sun2021hairandskin pages 4-5, molho‐pessach2015twonovelhomozygous pages 3-5)

### 11.2 Prognostic factors
Severity of cutaneous signs (e.g., presence of PPK in some dominant DSP families) was associated with more severe cardiac symptoms in one cohort, suggesting potential phenotype-based risk stratification. (maruthappu2019loss‐of‐functiondesmoplakini pages 7-11)

---

## 12. Treatment

### 12.1 Current applications / real-world implementations
Carvajal syndrome management is primarily supportive and follows cardiomyopathy and arrhythmia standards of care:
- Guideline-directed **heart failure pharmacotherapy** (e.g., ACE inhibitor/diuretics/beta-blockers; specific drugs reported in pediatric series include captopril, furosemide, carvedilol, digoxin) (molho‐pessach2015twonovelhomozygous pages 3-5)
- **Antiarrhythmic therapy** and rhythm monitoring (ziołkowska2024carvajalsyndromerelated pages 1-2)
- **ICD implantation** for uncontrolled/high-risk ventricular arrhythmias (binfadel2025genotypeandcardiac pages 1-2, ziołkowska2024carvajalsyndromerelated pages 1-2)
- **Catheter ablation** in selected arrhythmia cases (ziołkowska2024carvajalsyndromerelated pages 1-2)
- **Heart transplantation** for end-stage disease (binfadel2025genotypeandcardiac pages 1-2, ziołkowska2024carvajalsyndromerelated pages 1-2, williams2011noveldesmoplakinmutation pages 2-5)

### 12.2 Suggested MAXO terms (examples)
- Heart failure pharmacotherapy (MAXO:0000602)
- Implantation of cardioverter-defibrillator (MAXO:0000507)
- Catheter ablation (MAXO:0000460)
- Heart transplantation (MAXO:0000473)
- Genetic counseling (MAXO:0000066)

### 12.3 Experimental / research landscape (clinical trials/registries)
While there are no Carvajal-specific interventional trials in the retrieved trial set, multiple **2022–2024 observational studies explicitly include DSP variant carriers** and are therefore relevant for desmoplakin cardiomyopathy / Carvajal-related phenotypes:

1) **Bio-SCOTCH registry** (ClinicalTrials.gov **NCT06446271**; start **2024-06-26**; recruiting; n=750; includes DSP arm up to ~50): biomarker discovery and natural history across genetic cardiomyopathies including DSP. URL: https://clinicaltrials.gov/study/NCT06446271 (NCT06446271 chunk 1)

2) **CharACTPET-MR** hybrid PET-MRI characterization in genetically diagnosed arrhythmogenic cardiomyopathy (ClinicalTrials.gov **NCT05450783**; start **2022-09-01**; recruiting; n=80): evaluates PET-MR patterns, prognostic associations (death, transplant, resuscitated sudden death, unstable VT, HF hospitalization, myocarditis), and immune correlates; inclusion lists DSP among genotypes. URL: https://clinicaltrials.gov/study/NCT05450783 (NCT05450783 chunk 1)

3) **Cardiomyocyte DNA aspiration feasibility study** (ClinicalTrials.gov **NCT03177018**; start **2016-09-13**; completed; n=34): feasibility of obtaining cardiomyocytes during voltage mapping for DNA extraction; includes DSP in molecular/epigenetic targets. URL: https://clinicaltrials.gov/study/NCT03177018 (NCT03177018 chunk 1)

---

## 13. Prevention
No primary prevention exists for the genetic cause. Evidence-supported preventive strategies are **secondary/tertiary prevention** through early detection and complication avoidance:
- **Cascade screening / genetic counseling** for relatives, especially in settings with consanguinity. (binfadel2025genotypeandcardiac pages 1-2, williams2011noveldesmoplakinmutation pages 2-5)
- **Long-term cardiac monitoring** in individuals with PPK + hair shaft anomalies due to high cardiac risk in systematic review data. (polivka2016combinationofpalmoplantar pages 2-3)

---

## 14. Other Species / Natural Disease
No naturally occurring non-human Carvajal syndrome analogs were identified in the retrieved evidence excerpts.

---

## 15. Model Organisms
No specific Carvajal-focused animal models were identified in the retrieved evidence excerpts. Mechanistic inference is nevertheless consistent with established desmosome biology in cardiomyocytes and keratinocytes (review-level). (brandao2023desmoplakincardiomyopathycomprehensive pages 1-2)

---

## Recent Developments (prioritizing 2023–2024)

1) **Conceptual consolidation of “desmoplakin cardiomyopathy” (2023):** A comprehensive review describes DSP cardiomyopathy as increasingly recognized, characterized by frequent LV involvement, extensive fibrosis, high arrhythmic risk, and episodes of acute myocardial injury, while explicitly linking the historical first DSP-myocardial disease association to Carvajal syndrome. Publication date **Apr 2023**; URL: https://doi.org/10.3390/jcm12072660 (brandao2023desmoplakincardiomyopathycomprehensive pages 1-2)

2) **Expanded genotype evidence with detailed contemporary management (2024 case):** A 19-year-old with classic cutaneous findings and severe biventricular dysfunction had compound DSP variants and required ICD, antiarrhythmics, ablation, and ultimately transplantation, illustrating current real-world management pathways and genotype–phenotype expansion. Publication date **Sep 2024**; URL: https://doi.org/10.33963/v.phj.101664 (ziołkowska2024carvajalsyndromerelated pages 1-2, ziołkowska2024carvajalsyndromerelated media 9732cda8)

3) **New DSP-focused observational infrastructure (2024):** Bio-SCOTCH (NCT06446271) is a large prospective biomarker registry explicitly enrolling DSP variant carriers, representing a practical path to improved risk prediction and earlier intervention in DSP-related cardiomyopathies. Start date **2024-06-26**; URL: https://clinicaltrials.gov/study/NCT06446271 (NCT06446271 chunk 1)

---

## Expert opinion / consensus themes (authoritative sources in retrieved set)
- Dermatologic findings are repeatedly emphasized as an underused “warning signal” for life-threatening cardiomyopathy, with systematic review evidence indicating that PPK + hair anomalies warrant long-term cardiac monitoring. (polivka2016combinationofpalmoplantar pages 2-3)
- DSP variant heterogeneity and genotype–phenotype complexity are stressed; early diagnosis and regular cardiac surveillance are prioritized. (pigors2015desmoplakinmutationswith pages 1-2, karvonen2022anoveldesmoplakin pages 8-8)

---

## Structured summary table
The following table condenses key disease facts for knowledge-base ingestion:

| Domain | Key facts |
|---|---|
| Identifiers / synonyms | **Carvajal syndrome**; OMIM **605656** / **605676** reported in the literature excerpts; often described as **“Naxos disease variant”** or a related **cardiocutaneous syndrome**; related comparator: **Naxos disease OMIM 601214** (sun2021hairandskin pages 1-2, binfadel2025genotypeandcardiac pages 1-2, brandao2023desmoplakincardiomyopathycomprehensive pages 1-2, binfadel2025genotypeandcardiac pages 9-9) |
| Primary evidence source type | Evidence is mainly from **aggregated disease reviews**, **case reports/series**, and small **retrospective cohorts** rather than EHR-scale datasets; knowledge remains based on rare-patient observations (sun2021hairandskin pages 1-2, binfadel2025genotypeandcardiac pages 1-2, brandao2023desmoplakincardiomyopathycomprehensive pages 1-2) |
| Causal gene | **DSP (desmoplakin)** is the principal causal gene for classic Carvajal syndrome; disease belongs to the desmosomal cardiocutaneous disorders (sun2021hairandskin pages 1-2, pigors2015desmoplakinmutationswith pages 1-2, brandao2023desmoplakincardiomyopathycomprehensive pages 1-2) |
| Variant types / molecular pattern | Predominantly **loss-of-function/truncating** DSP variants, especially **C-terminal** changes in classic recessive disease; reported mechanisms include **frameshift**, **nonsense**, **compound heterozygous**, and homozygous truncating variants; some cases involve **nonsense-mediated decay / haploinsufficiency** (ziołkowska2024carvajalsyndromerelated pages 1-2, maruthappu2019loss‐of‐functiondesmoplakini pages 7-11, williams2011noveldesmoplakinmutation pages 2-5, williams2011noveldesmoplakinmutation pages 1-2) |
| Inheritance | Usually **autosomal recessive** in classic Carvajal syndrome, often in **consanguineous** families; **dominant DSP cardiocutaneous phenotypes** with overlapping “Carvajal-like” features are also reported (sun2021hairandskin pages 4-5, karvonen2022anoveldesmoplakin pages 8-8, maruthappu2019loss‐of‐functiondesmoplakini pages 7-11, williams2011noveldesmoplakinmutation pages 1-2) |
| Hallmark phenotype triad | **Woolly/curly hair + palmoplantar keratoderma (often striate/focal) + cardiomyopathy**; additional features may include poor dentition, nail changes, skin fragility, or ichthyosis depending on DSP variant location (sun2021hairandskin pages 1-2, sun2021hairandskin pages 4-5, molho‐pessach2015twonovelhomozygous pages 3-5) |
| Typical cardiac phenotype | Classically **left-ventricular–predominant dilated/arrhythmogenic cardiomyopathy**; many patients show **biventricular** disease, myocardial fibrosis, heart failure, ventricular arrhythmias, and sometimes **LV non-compaction** features (sun2021hairandskin pages 4-5, molho‐pessach2015twonovelhomozygous pages 3-5, ziołkowska2024carvajalsyndromerelated pages 1-2, williams2011noveldesmoplakinmutation pages 2-5, williams2011noveldesmoplakinmutation pages 1-2) |
| Usual onset / course | Hair changes are often **congenital**; keratoderma develops in **infancy/toddler years**; cardiac manifestations commonly begin in **childhood** and are often **progressive**, with reported median first cardiac manifestation around **8 years** (range **3–35**) (polivka2016combinationofpalmoplantar pages 2-3, williams2011noveldesmoplakinmutation pages 1-2) |
| Key statistics | In a systematic review of desmosomal disease, the combination of **PPK + hair shaft anomalies** carried **80.1%** risk of cardiac disease (**129/161** patients) (source review summary). In a 10-patient Saudi pediatric Carvajal cohort: **100% woolly hair**, **50% PPK**, **9/10 frequent PVCs**, **3/10 ICD**, **4/10 heart transplant**, **3/10 died while awaiting transplant** (binfadel2025genotypeandcardiac pages 1-2, polivka2016combinationofpalmoplantar pages 2-3) |
| Pathophysiology | DSP dysfunction impairs **desmosome–intermediate filament anchoring**, weakening mechanical coupling in **myocardium** and **epidermis**; downstream effects include desmosomal protein mislocalization, conduction abnormalities, fibrosis/fibrofatty replacement, and cardiomyopathy (sun2021hairandskin pages 1-2, maruthappu2019loss‐of‐functiondesmoplakini pages 7-11, brandao2023desmoplakincardiomyopathycomprehensive pages 1-2) |
| Diagnostic clues | Early **woolly hair** and **PPK** should trigger cardiac workup; diagnosis integrates **clinical triad**, **family history/consanguinity**, and **molecular confirmation of DSP variants** (karvonen2022anoveldesmoplakin pages 8-8, williams2011noveldesmoplakinmutation pages 2-5, williams2011noveldesmoplakinmutation pages 1-2) |
| Cardiac diagnostics | Typical evaluations include **ECG**, **Holter**, **echocardiography**, **cardiac MRI** (for fibrosis, ventricular function, LV/RV involvement), and sometimes biopsy/histology; asymptomatic DSP carriers may still warrant surveillance (binfadel2025genotypeandcardiac pages 1-2, karvonen2022anoveldesmoplakin pages 8-8, ziołkowska2024carvajalsyndromerelated pages 1-2) |
| Surveillance / prevention | Long-term **cardiac monitoring** is recommended for patients with **PPK + hair anomalies** and for at-risk relatives; **genetic counseling**, **cascade/family screening**, and early specialist follow-up are emphasized (binfadel2025genotypeandcardiac pages 1-2, pigors2015desmoplakinmutationswith pages 1-2, maruthappu2019loss‐of‐functiondesmoplakini pages 7-11, williams2011noveldesmoplakinmutation pages 2-5) |
| Management options | Standard **heart-failure therapy**, antiarrhythmics, **ICD**, **catheter ablation**, and **heart transplantation** for advanced disease; management is multidisciplinary (cardiology, dermatology, genetics) (sun2021hairandskin pages 4-5, molho‐pessach2015twonovelhomozygous pages 3-5, ziołkowska2024carvajalsyndromerelated pages 1-2) |
| Prognosis | Potentially severe, with **early heart failure**, malignant ventricular arrhythmias, **sudden cardiac death**, and transplant need in childhood/adolescence; prognosis is variable but can be poor without early recognition and intervention (binfadel2025genotypeandcardiac pages 1-2, sun2021hairandskin pages 4-5, williams2011noveldesmoplakinmutation pages 1-2) |


*Table: This table condenses the core identifiers, genotype, phenotype, diagnostics, prognosis, and management points for Carvajal syndrome from the gathered evidence. It is useful as a quick-reference summary for a disease knowledge base entry.*

---

## Key direct abstract quotes (for knowledge base evidence)
- “**The first association between DSP genetic variants and the presence of a myocardial disease referred to patients with Carvajal syndrome.**” (Apr 2023; https://doi.org/10.3390/jcm12072660) (brandao2023desmoplakincardiomyopathycomprehensive pages 1-2)
- Systematic review summary statement: “**Palmoplantar keratoderma (PPK), hair shaft anomalies and skin fragility are the major features in the 458 patients analysed… The combination of PPK and hair shaft anomalies… is at high risk of cardiac disease (129/161, 80.1%).**” (Sep 2016; https://doi.org/10.1136/jmedgenet-2015-103403) (polivka2016combinationofpalmoplantar pages 2-3)

---

## Limitations of this report (evidence-bound)
- Formal ICD/Orphanet/MeSH identifiers, population prevalence/incidence, and validated QoL metrics were not present in the retrieved excerpts and should be supplemented by targeted queries to OMIM/Orphanet/MeSH and epidemiology registries.
- Model organism evidence and disease-specific epigenetic profiling were not identified in the current evidence set.


References

1. (sun2021hairandskin pages 1-2): Qisi Sun, Lara Wine Lee, E Kevin Hall, Keith A. Choate, and Robert W. Elder. Hair and skin predict cardiomyopathies: carvajal and erythrokeratodermia cardiomyopathy syndromes. Pediatric Dermatology, 38:31-38, Dec 2021. URL: https://doi.org/10.1111/pde.14478, doi:10.1111/pde.14478. This article has 27 citations and is from a peer-reviewed journal.

2. (sun2021hairandskin pages 4-5): Qisi Sun, Lara Wine Lee, E Kevin Hall, Keith A. Choate, and Robert W. Elder. Hair and skin predict cardiomyopathies: carvajal and erythrokeratodermia cardiomyopathy syndromes. Pediatric Dermatology, 38:31-38, Dec 2021. URL: https://doi.org/10.1111/pde.14478, doi:10.1111/pde.14478. This article has 27 citations and is from a peer-reviewed journal.

3. (karvonen2022anoveldesmoplakin pages 8-8): V. Karvonen, L. Harjama, K. Heliö, K. Kettunen, O. Elomaa, J.W. Koskenvuo, J. Kere, S. Weckström, M. Holmström, J. Saarela, A. Ranki, T. Heliö, and K. Hannula‐Jouppi. A novel desmoplakin mutation causes dilated cardiomyopathy with palmoplantar keratoderma as an early clinical sign. Journal of the European Academy of Dermatology and Venereology, 36:1349-1358, May 2022. URL: https://doi.org/10.1111/jdv.18164, doi:10.1111/jdv.18164. This article has 11 citations and is from a domain leading peer-reviewed journal.

4. (binfadel2025genotypeandcardiac pages 1-2): Maha Binfadel, Mohamed Umair Aleem, Mohammed Alhabdan, Nadiah Alruwaili, Zuhair AlHassnan, Olga Vriz, Sahar Tulbah, and Dimpna Calila Albert-Brotons. Genotype and cardiac outcome in patients with cardiocutaneous syndrome (naxos disease variant: carvajal syndrome). Orphanet Journal of Rare Diseases, Mar 2025. URL: https://doi.org/10.1186/s13023-025-03612-8, doi:10.1186/s13023-025-03612-8. This article has 1 citations and is from a peer-reviewed journal.

5. (molho‐pessach2015twonovelhomozygous pages 5-6): Vered Molho‐Pessach, Sivan Sheffer, Rula Siam, Spiro Tams, Ihab Siam, Rula Awwad, Sofia Babay, Julius Golender, Natalia Simanovsky, Yuval Ramot, and Abraham Zlotogorski. Two novel homozygous desmoplakin mutations in carvajal syndrome. Pediatric Dermatology, 32:641-646, Sep 2015. URL: https://doi.org/10.1111/pde.12541, doi:10.1111/pde.12541. This article has 27 citations and is from a peer-reviewed journal.

6. (polivka2016combinationofpalmoplantar pages 2-3): Laura Polivka, Christine Bodemer, and Smail Hadj-Rabia. Combination of palmoplantar keratoderma and hair shaft anomalies, the warning signal of severe arrhythmogenic cardiomyopathy: a systematic review on genetic desmosomal diseases. Journal of Medical Genetics, 53:289-295, Sep 2016. URL: https://doi.org/10.1136/jmedgenet-2015-103403, doi:10.1136/jmedgenet-2015-103403. This article has 45 citations and is from a domain leading peer-reviewed journal.

7. (brandao2023desmoplakincardiomyopathycomprehensive pages 1-2): Mariana Brandão, Riccardo Bariani, Ilaria Rigato, and Barbara Bauce. Desmoplakin cardiomyopathy: comprehensive review of an increasingly recognized entity. Journal of Clinical Medicine, 12:2660, Apr 2023. URL: https://doi.org/10.3390/jcm12072660, doi:10.3390/jcm12072660. This article has 54 citations.

8. (molho‐pessach2015twonovelhomozygous pages 3-5): Vered Molho‐Pessach, Sivan Sheffer, Rula Siam, Spiro Tams, Ihab Siam, Rula Awwad, Sofia Babay, Julius Golender, Natalia Simanovsky, Yuval Ramot, and Abraham Zlotogorski. Two novel homozygous desmoplakin mutations in carvajal syndrome. Pediatric Dermatology, 32:641-646, Sep 2015. URL: https://doi.org/10.1111/pde.12541, doi:10.1111/pde.12541. This article has 27 citations and is from a peer-reviewed journal.

9. (ziołkowska2024carvajalsyndromerelated pages 1-2): Lidia Ziółkowska, Dorota Piekutowska-Abramczuk, Karolina Borowiec, Elżbieta Ciara, Maciej Sterliński, and Elżbieta Katarzyna Biernacka. Carvajal syndrome related to two distinct molecular variants in desmoplakin gene. Polish Heart Journal, 82:914-915, Sep 2024. URL: https://doi.org/10.33963/v.phj.101664, doi:10.33963/v.phj.101664. This article has 1 citations.

10. (williams2011noveldesmoplakinmutation pages 2-5): Tatjana Williams, Wolfram Machann, Leif Kühler, Henning Hamm, Josef Müller-Höcker, Michael Zimmer, Georg Ertl, Oliver Ritter, Meinrad Beer, and Jost Schönberger. Novel desmoplakin mutation: juvenile biventricular cardiomyopathy with left ventricular non-compaction and acantholytic palmoplantar keratoderma. Clinical Research in Cardiology, 100:1087-1093, Jul 2011. URL: https://doi.org/10.1007/s00392-011-0345-9, doi:10.1007/s00392-011-0345-9. This article has 57 citations and is from a peer-reviewed journal.

11. (williams2011noveldesmoplakinmutation pages 1-2): Tatjana Williams, Wolfram Machann, Leif Kühler, Henning Hamm, Josef Müller-Höcker, Michael Zimmer, Georg Ertl, Oliver Ritter, Meinrad Beer, and Jost Schönberger. Novel desmoplakin mutation: juvenile biventricular cardiomyopathy with left ventricular non-compaction and acantholytic palmoplantar keratoderma. Clinical Research in Cardiology, 100:1087-1093, Jul 2011. URL: https://doi.org/10.1007/s00392-011-0345-9, doi:10.1007/s00392-011-0345-9. This article has 57 citations and is from a peer-reviewed journal.

12. (ziołkowska2024carvajalsyndromerelated media 9732cda8): Lidia Ziółkowska, Dorota Piekutowska-Abramczuk, Karolina Borowiec, Elżbieta Ciara, Maciej Sterliński, and Elżbieta Katarzyna Biernacka. Carvajal syndrome related to two distinct molecular variants in desmoplakin gene. Polish Heart Journal, 82:914-915, Sep 2024. URL: https://doi.org/10.33963/v.phj.101664, doi:10.33963/v.phj.101664. This article has 1 citations.

13. (maruthappu2019loss‐of‐functiondesmoplakini pages 7-11): T. Maruthappu, A. Pósafalvi, Silvia Castelletti, P. Delaney, P. Syrris, Edel.A. O’Toole, Kathleen J. Green, Perry M. Elliott, PD Lambiase, PD Lambiase, Andrew Tinker, William J. McKenna, and D. Kelsell. Loss‐of‐function desmoplakin i and ii mutations underlie dominant arrhythmogenic cardiomyopathy with a hair and skin phenotype. British Journal of Dermatology, 180:1114-1122, Jan 2019. URL: https://doi.org/10.1111/bjd.17388, doi:10.1111/bjd.17388. This article has 58 citations and is from a highest quality peer-reviewed journal.

14. (NCT03177018 chunk 1):  DNA Analysis From Isolated Cardiomyocytes in the Molecular Diagnosis of Arrhythmogenic Right Ventricular Cardiomyopathy/Dysplasia. University Hospital, Toulouse. 2016. ClinicalTrials.gov Identifier: NCT03177018

15. (NCT06446271 chunk 1):  Biomarkers in SCOTland CardiomyopatHy Registry (Bio-SCOTCH). NHS Greater Glasgow and Clyde. 2024. ClinicalTrials.gov Identifier: NCT06446271

16. (NCT05450783 chunk 1):  Tissue and Metabolic Characterization of Arrhythmogenic Cardiomyopathies by Hybrid PET-MRI Imaging, Impact of the Observed Profiles on the Phenotype and on the Evolution of Cardiomyopathy. Nantes University Hospital. 2022. ClinicalTrials.gov Identifier: NCT05450783

17. (pigors2015desmoplakinmutationswith pages 1-2): M. Pigors, A. Schwieger-Briel, R. Cosgarea, A. Diaconeasa, L. Bruckner-Tuderman, T. Fleck, and C. Has. Desmoplakin mutations with palmoplantar keratoderma, woolly hair and cardiomyopathy. Acta dermato-venereologica, 95 3:337-40, Mar 2015. URL: https://doi.org/10.2340/00015555-1974, doi:10.2340/00015555-1974. This article has 47 citations and is from a domain leading peer-reviewed journal.

18. (binfadel2025genotypeandcardiac pages 9-9): Maha Binfadel, Mohamed Umair Aleem, Mohammed Alhabdan, Nadiah Alruwaili, Zuhair AlHassnan, Olga Vriz, Sahar Tulbah, and Dimpna Calila Albert-Brotons. Genotype and cardiac outcome in patients with cardiocutaneous syndrome (naxos disease variant: carvajal syndrome). Orphanet Journal of Rare Diseases, Mar 2025. URL: https://doi.org/10.1186/s13023-025-03612-8, doi:10.1186/s13023-025-03612-8. This article has 1 citations and is from a peer-reviewed journal.
