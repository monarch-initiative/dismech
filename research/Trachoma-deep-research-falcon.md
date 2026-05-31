---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T17:10:16.027469'
end_time: '2026-04-04T17:17:34.890443'
duration_seconds: 438.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Trachoma
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Trachoma
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Trachoma** covering all of the
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
- **Disease Name:** Trachoma
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Trachoma** covering all of the
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


# Trachoma — Disease Characteristics Research Report (Infectious Disease)

## Executive summary
Trachoma is a neglected tropical eye disease caused by conjunctival strains/serovars A–C of *Chlamydia trachomatis* and is the leading infectious cause of blindness globally. Repeated ocular infections in childhood drive chronic conjunctival inflammation that can progress to conjunctival scarring, trichiasis, corneal opacity, and irreversible visual impairment or blindness. Control and elimination efforts are organized around WHO’s SAFE strategy (Surgery, Antibiotics, Facial cleanliness, Environmental improvement) and population-based prevalence surveys graded with the WHO simplified system. Recent work (2023–2024) emphasizes improved surveillance in low-prevalence/post-MDA settings using nucleic acid amplification tests (NAATs) and serology (e.g., Pgp3 antibodies) because clinical TF correlates imperfectly with ocular infection after MDA. (sitoe2024ongoingtransmissionof pages 1-2, ageed2024eliminatingtrachomain pages 2-3)

## 1. Disease information
### 1.1 Overview and current definition
Trachoma is an infectious conjunctivitis/keratoconjunctivitis caused by ocular strains of *Chlamydia trachomatis*; repeated infection episodes lead to chronic inflammation and a cicatricial disease that may culminate in trichiasis and corneal opacity/blindness. (sahin2023chlamydialeyeinfections pages 1-4, sitoe2024ongoingtransmissionof pages 1-2)

### 1.2 Key identifiers (ontology and clinical coding)
* **MONDO ID:** Not identified in the retrieved full-text evidence in this run.
* **MeSH / ICD-10 / ICD-11:** Not identified in the retrieved full-text evidence in this run.

Because these identifiers are typically available from controlled vocabularies (e.g., MeSH, ICD, MONDO) rather than primary papers, and were not present in the retrieved texts, this report cannot provide verified codes without additional ontology/database retrieval.

### 1.3 Synonyms / alternative names
* “Blinding trachoma,” “classical trachoma,” “trachomatous disease,” and “chlamydial eye infection” are used in the clinical and public health literature. (sahin2023chlamydialeyeinfections pages 1-4, antwiadjei2017relationshipbetweenthe pages 29-35)

### 1.4 Evidence sources
The information summarized here is predominantly from aggregated disease-level resources and population-based survey literature (WHO-aligned grading and elimination criteria; country surveys; systematic reviews) rather than from EHR-derived patient-level datasets. (hardingesch2023tropicaldataapproach pages 1-2, antwiadjei2017relationshipbetweenthe pages 29-35)

## 2. Etiology
### 2.1 Causal factors
* **Infectious agent:** *Chlamydia trachomatis* (ocular serovars A–C) causes trachoma. (sahin2023chlamydialeyeinfections pages 1-4)
* **Mechanistic cause:** Repeated conjunctival infections in childhood trigger recurrent inflammation that drives conjunctival fibrosis/scarring and downstream eyelid/corneal complications. (toumasis2024insightsintopathogenesis pages 9-10, sitoe2024ongoingtransmissionof pages 1-2)

### 2.2 Transmission and risk factors
**Transmission routes:** Direct or indirect transfer of ocular/nasal secretions (including fomites) and mechanical transmission via flies are emphasized in recent reviews and programmatic literature. (sahin2023chlamydialeyeinfections pages 1-4, toumasis2024insightsintopathogenesis pages 10-12, ageed2024eliminatingtrachomain pages 2-3)

**Environmental and social risk factors:** Overcrowding and poor hygiene/sanitation are consistently linked to higher transmission intensity; recent syntheses stress WASH and fly control as key determinants of sustained transmission. (toumasis2024insightsintopathogenesis pages 10-12, ageed2024eliminatingtrachomain pages 2-3)

### 2.3 Protective factors
Protective factors supported in the retrieved evidence are primarily **environmental/behavioral**: improved access to water for hygiene, sanitation (latrine access/use), facial cleanliness, and reductions in fly–eye contact are repeatedly cited as associated with lower risk/prevalence. (ageed2024eliminatingtrachomain pages 2-3)

### 2.4 Host genetic susceptibility and gene–environment interplay
While trachoma is not a monogenic disorder, multiple studies support the concept that **host immune-genetic variation modifies risk of severe sequelae** (scarring, trichiasis) given similar exposure, implying gene–environment interaction (host variants shaping inflammatory/fibrotic response in settings with repeated infection). (derrick2015trachomaandocular pages 5-6, atik2008identificationofnovel pages 2-3)

## 3. Phenotypes (clinical presentation)
### 3.1 WHO simplified grading: definitions and phenotype mapping
WHO’s simplified clinical grading system defines five key signs (TF, TI, TS, TT, CO), used in field surveys and elimination decision-making. Exact definitions from a WHO-aligned grading summary are provided in the artifact table. (antwiadjei2017relationshipbetweenthe pages 29-35)

**HPO term suggestions (non-exhaustive):**
* Follicular conjunctivitis (TF): HP:0000509 (Conjunctivitis) + HP:0030057 (Follicular conjunctivitis; if not available, use conjunctivitis with qualifier)
* Conjunctival scarring (TS): HP:0031095 (Conjunctival scarring; if unavailable, map to conjunctival fibrosis)
* Trichiasis (TT): HP:0009796 (Trichiasis)
* Entropion (often accompanying TT): HP:0000656 (Entropion)
* Corneal opacity (CO): HP:0007957 (Corneal opacity)
* Visual impairment/blindness (advanced): HP:0000505 (Visual impairment), HP:0000618 (Blindness)

### 3.2 Natural history, onset, progression
Trachoma commonly begins in childhood as “active” disease (TF/TI), and later in life a subset develop progressive scarring and trichiasis, which can continue even when ocular infection is no longer detectable—emphasizing a chronic, scarring phenotype with long latency. (toumasis2024insightsintopathogenesis pages 9-10, sitoe2024ongoingtransmissionof pages 1-2)

### 3.3 Quality-of-life impact
Advanced disease (TT/CO) causes pain (from lashes rubbing cornea), ocular surface damage, and progressive visual impairment/blindness, with major functional and socioeconomic consequences in endemic, low-resource communities. (ageed2024eliminatingtrachomain pages 2-3)

## 4. Genetic / molecular information
### 4.1 Causal genes
Trachoma is **not** caused by pathogenic germline variants in a single gene; instead, genetic evidence supports **susceptibility modifiers** affecting inflammatory and fibrotic responses.

### 4.2 Modifier/susceptibility loci (examples)
Evidence includes HLA/KIR, cytokine/TNF-region, and other inflammatory pathway variants associated with scarring and/or trichiasis in population studies:
* **HLA-C2 dose effect with scarring risk** in Gambians; risk further increased by **KIR2DL2/KIR2DL3 heterozygosity** (reviewed with reported ORs up to ~5.95 in HLA-C2 homozygotes with both KIR2DL2 and KIR2DL3). (derrick2015trachomaandocular pages 5-6)
* **TNF-locus region variants** associated with severe sequelae in Gambians, including TNF promoter and linked-region SNPs; e.g., **TNF-308A** (dominant) associated with increased trichiasis risk (OR 1.52, 95% CI 1.07–2.15) and **TNF-238** associated with scarring in one analysis (OR 1.46, 95% CI 1.06–2.01). (natividad2007geneticvariationat pages 2-3)
* **Nepal (Tharu ethnicity) TT risk/protection combinations** across inflammatory genes (logic regression). A protective multilocus combination was associated with ~5-fold lower TT risk (OR 0.2, 95% CI 0.11–0.33), while a risk combination was associated with substantially higher TT risk (OR 13.5, 95% CI 3.3–22). (atik2008identificationofnovel pages 1-2)

### 4.3 Interpretation and limitations (expert analysis)
A genomics-focused synthesis emphasizes that many reported associations have modest sample sizes, multiple-testing/epistasis concerns, and heterogeneous phenotyping across settings; overall, the weight of evidence supports **polygenic, context-dependent susceptibility** rather than deterministic variants. (derrick2015trachomaandocular pages 5-6)

## 5. Environmental information
Key environmental drivers in endemic settings include limited WASH infrastructure and fly breeding conditions (e.g., sanitation and exposed feces), which influence exposure intensity and reinfection rates. Environmental improvement (latrines/sanitation, water access for hygiene, fly control) is repeatedly described as central to sustained transmission reduction beyond the transient impact of antibiotic campaigns. (toumasis2024insightsintopathogenesis pages 10-12, ageed2024eliminatingtrachomain pages 2-3)

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (trigger → pathology)
1. **Initial trigger:** Repeated conjunctival infection with ocular *C. trachomatis* strains in early life. (toumasis2024insightsintopathogenesis pages 9-10, sitoe2024ongoingtransmissionof pages 1-2)
2. **Innate activation:** Infected epithelial cells trigger innate immune responses with chemokine/cytokine production and recruitment of immune cells. (toumasis2024insightsintopathogenesis pages 9-10)
3. **Inflammatory amplification:** Recurrent infection episodes sustain chronic inflammation; evidence points to TH1/IFNγ-associated resolution signals but also TH17-associated inflammatory signatures that may worsen scarring risk. (toumasis2024insightsintopathogenesis pages 9-10)
4. **Tissue remodeling/fibrosis:** Increased matrix remodeling (e.g., elevated MMPs), goblet cell depletion, and collagen deposition remodel the tarsal conjunctiva into fibrotic scar tissue, distorting eyelids. (toumasis2024insightsintopathogenesis pages 9-10)
5. **Clinical sequelae:** Eyelid distortion leads to trichiasis/entropion, corneal abrasion and opacity, visual impairment/blindness. (ageed2024eliminatingtrachomain pages 2-3, antwiadjei2017relationshipbetweenthe pages 29-35)

### 6.2 Molecular/cellular processes (GO) and cell types (CL)
**Suggested GO Biological Process terms (examples):**
* GO:0006954 inflammatory response
* GO:0006955 immune response
* GO:0007165 signal transduction (innate immune receptor pathways)
* GO:0030198 extracellular matrix organization
* GO:0043062 extracellular structure organization
* GO:0001525 angiogenesis (pannus/vascularization in chronic disease; referenced in clinical descriptions) (sahin2023chlamydialeyeinfections pages 1-4)

**Suggested CL cell types (examples):**
* CL:0000066 epithelial cell (conjunctival epithelial)
* CL:0000451 dendritic cell (antigen presentation)
* CL:0000542 lymphocyte (T cell subsets)
* CL:0000236 B cell
* CL:0000623 natural killer cell (noted in genetic models involving KIR/HLA and conjunctival infiltrates in scarring disease) (derrick2015trachomaandocular pages 5-6)

### 6.3 Recent developments (2023–2024) in mechanism research
* **Local immune kinetics in models:** A 2024 non-human primate (NHP) trachoma model is used to characterize conjunctival immune responses and highlights the importance of local immunity in acute disease (supporting vaccine/therapeutic development). (paulet2024multimodalmucosaland pages 21-22)
* **Tear/cytokine biomarker kinetics:** Longitudinal profiling of tear cytokines and antimicrobial proteins shows evidence of inflammatory responses before/during/after detectable infection and increased chemokines in successive infection episodes, providing a mechanistic rationale for why repeated infection increases scarring risk. (toumasis2024insightsintopathogenesis pages 9-10)

## 7. Anatomical structures affected
### 7.1 Primary organs/tissues
* **Primary site:** Conjunctiva (especially upper tarsal conjunctiva) and ocular surface. (antwiadjei2017relationshipbetweenthe pages 29-35)
* **Secondary/complications:** Eyelid margin (trichiasis/entropion) and cornea (opacity). (ageed2024eliminatingtrachomain pages 2-3, antwiadjei2017relationshipbetweenthe pages 29-35)

**UBERON term suggestions:**
* Conjunctiva: UBERON:0000970
* Eyelid: UBERON:0001711
* Cornea: UBERON:0000964

## 8. Temporal development
### 8.1 Onset
Typically begins in childhood as active disease (TF/TI), with chronic consequences manifesting later after cumulative infections. (sitoe2024ongoingtransmissionof pages 1-2, antwiadjei2017relationshipbetweenthe pages 29-35)

### 8.2 Progression
Progression is generally chronic and cumulative; repeated reinfection/inflammation increases scarring risk, and established scarring can continue to progress over years, necessitating long-term services for TT even after infection prevalence decreases. (toumasis2024insightsintopathogenesis pages 9-10, sitoe2024ongoingtransmissionof pages 1-2)

## 9. Inheritance and population
### 9.1 Epidemiology (recent statistics)
**Global endemicity and burden:**
* A Brazil-focused 2024 ecological study cites that in **2023**, **115.7 million** people lived in trachoma-endemic regions, with **1.5 million** experiencing sequelae, across **40 countries**. (maciel2024trachomaassociatedmorbidityand pages 1-2)
* In program operations literature (Tropical Data), trachoma surveys have been scaled: between **29 Feb 2016 and 24 Apr 2023**, **3,373 surveys** across **50 countries** examined **10,818,502** people. (hardingesch2023tropicaldataapproach pages 1-2)

**Country/program example (Mozambique):**
* Baseline mapping (2011–2015) and SAFE led to large-scale reductions; by **2022**, **54 of 66 endemic districts** in Mozambique had stopped MDA after reaching TF <5%, but persistent/recrudescent TF remained in a subset. (sitoe2024ongoingtransmissionof pages 2-3)

### 9.2 Sex/age distribution
Active trachoma is concentrated in children (1–9 years used for TF-based decision thresholds), while TT is measured in adults (≥15 years) and reflects cumulative exposure and scarring. (sitoe2024ongoingtransmissionof pages 1-2, hardingesch2023tropicaldataapproach pages 1-2)

### 9.3 Genetics (population-level susceptibility)
Genetic susceptibility is multifactorial; associations include HLA/KIR and cytokine-region variants across African and Asian populations, but these do not imply Mendelian inheritance patterns for the disease. (derrick2015trachomaandocular pages 5-6, atik2008identificationofnovel pages 1-2)

## 10. Diagnostics
### 10.1 Standard clinical diagnosis and grading
Clinical diagnosis and population monitoring rely on the **WHO simplified grading system** (TF/TI/TS/TT/CO). (antwiadjei2017relationshipbetweenthe pages 29-35)

### 10.2 Programmatic diagnostics: emerging additions (2023–2024 emphasis)
A key 2024 Mozambique analysis argues that in low-prevalence/post-MDA settings, **TF does not consistently correlate with ocular infection**, motivating adjunct testing:
* **NAAT/PCR** from conjunctival swabs for ocular *C. trachomatis* nucleic acid. (sitoe2024ongoingtransmissionof pages 1-2)
* **Serology** from dried blood spots, particularly anti-Pgp3 antibodies; Mozambique field surveys implemented multiplex bead assays and modeled seroconversion rates as an indicator of transmission intensity. (sitoe2024ongoingtransmissionof pages 1-2, sitoe2024ongoingtransmissionof pages 3-4)

**Concrete 2022 Mozambique enhanced survey data (children 1–9 years):**
* TF: **1.1–6.0%**
* PCR infection: **1.1–4.8%**
* Pgp3 seroprevalence: **8.8–24.3%**
* Pgp3 seroconversion rate: **1.9–6.0 per 100 children-year**
These discordances illustrate how TF, PCR infection, and serology can diverge and why multi-indicator surveillance is being operationalized. (sitoe2024ongoingtransmissionof pages 1-2, sitoe2024ongoingtransmissionof pages 4-6)

### 10.3 Differential diagnosis
Not comprehensively extractable from the retrieved evidence in this run; clinically, other causes of chronic/follicular conjunctivitis (viral, allergic, other bacterial) are typical differentials, but specific evidence-backed differentials were not captured in the cited texts.

## 11. Outcome / prognosis
The major morbidity is vision loss due to corneal opacity following trichiasis-related corneal damage. Trachoma is a long-latency disease; even after transmission wanes, TT services may be needed for years because scarring disease can persist/progress. (sitoe2024ongoingtransmissionof pages 1-2, antwiadjei2017relationshipbetweenthe pages 29-35)

## 12. Treatment
### 12.1 Standard treatment and control framework (SAFE)
SAFE remains the backbone of trachoma management and elimination:
* **Surgery:** for TT; one described approach is bilamellar tarsal rotation procedure (BTRP). (ageed2024eliminatingtrachomain pages 2-3)
* **Antibiotics:** typically azithromycin mass drug administration (MDA) as the population-level antibiotic arm. (sitoe2024ongoingtransmissionof pages 1-2)
* **Facial cleanliness** and **Environmental improvement:** to reduce reinfection/transmission and sustain gains. (sitoe2024ongoingtransmissionof pages 1-2, ageed2024eliminatingtrachomain pages 2-3)

**MAXO term suggestions:**
* Antibiotic therapy: MAXO:0000058 (if using a general antibiotic therapy term)
* Mass drug administration: MAXO term not confirmed in retrieved evidence; would be mapped under population-level preventive treatment.
* Trichiasis surgery / eyelid surgery: MAXO:0001070 (surgical procedure; specify eyelid correction if available)

### 12.2 Real-world implementation data (program thresholds)
WHO-aligned operational thresholds for district-level decisions based on TF in children 1–9 years include:
* TF ≥30% → ≥5 years A/F/E
* TF 10–29.9% → 3 years A/F/E
* TF 5–9.9% → 1 year A/F/E
* TF <5% → transition away from district-wide A/F/E toward surveillance
(hardingesch2023tropicaldataapproach pages 1-2)

### 12.3 Antibiotic MDA: benefits and monitoring considerations
Recent program evaluations emphasize that in post-MDA settings, clinical signs may not track infection; therefore NAAT/PCR and serology are being incorporated into surveillance to inform decisions and monitor potential ongoing transmission. (sitoe2024ongoingtransmissionof pages 1-2)

## 13. Prevention
### 13.1 Primary prevention
Primary prevention is dominated by SAFE’s F and E components (facial cleanliness, sanitation, water access, fly control) and broader socioeconomic improvements. (toumasis2024insightsintopathogenesis pages 10-12, ageed2024eliminatingtrachomain pages 2-3)

### 13.2 Secondary prevention (screening/surveillance)
Population-based prevalence surveys (TIS/TSS) using WHO simplified grading are central; Tropical Data provides standardized methodologies and electronic data capture to support ministries of health in survey-based decision making. (hardingesch2023tropicaldataapproach pages 1-2)

### 13.3 Tertiary prevention
Timely surgery for TT prevents continued corneal abrasion and reduces progression to corneal opacity and blindness. (ageed2024eliminatingtrachomain pages 2-3, antwiadjei2017relationshipbetweenthe pages 29-35)

## 14. Other species / natural disease
This run retrieved an NHP experimental infection model used to study acute trachoma-like disease and local immune responses, supporting comparative pathology and vaccine research. (paulet2024multimodalmucosaland pages 21-22)

## 15. Model organisms and experimental systems
### 15.1 Non-human primate model (2024)
A 2024 PLOS NTD study reports an NHP conjunctival *C. trachomatis* infection model with clinical findings similar to acute human trachoma and a staged conjunctival immune response, positioning this model for preclinical evaluation of vaccines/therapeutics. (paulet2024multimodalmucosaland pages 21-22)

### 15.2 In vitro / molecular profiling
The retrieved evidence in this run included review-level discussion of immune pathways and tissue remodeling; detailed single-cell/spatial multi-omics for trachoma specifically was not captured in the cited evidence.

## Key recent developments (2023–2024) — synthesis
1. **Surveillance innovation:** Field programs are integrating **PCR and serology** (Pgp3, Ct694) into impact surveys to resolve ambiguity where TF is poorly correlated with infection after MDA. (sitoe2024ongoingtransmissionof pages 1-2, sitoe2024ongoingtransmissionof pages 3-4)
2. **Quantitative transmission inference:** District-level **seroconversion rate (SCR)** modeling is increasingly used to quantify ongoing transmission intensity at low TF prevalence. (sitoe2024ongoingtransmissionof pages 1-2, sitoe2024ongoingtransmissionof pages 4-6)
3. **Program scale/quality infrastructure:** Tropical Data reports millions examined under standardized protocols, reflecting maturation of implementation science and QA/QC for elimination decision-making. (hardingesch2023tropicaldataapproach pages 1-2)

## Structured quick reference table
| Category | Item | Exact definition / key finding | Year / threshold | Evidence |
|---|---|---|---|---|
| Definition / agent | Trachoma | Neglected tropical eye disease caused by conjunctival strains/serovars A-C of *Chlamydia trachomatis*; repeated childhood ocular infection leads to conjunctival scarring, trichiasis, corneal opacity, and blindness | Current understanding | (sahin2023chlamydialeyeinfections pages 1-4, sitoe2024ongoingtransmissionof pages 1-2, hardingesch2023tropicaldataapproach pages 1-2) |
| WHO simplified grading | TF | Trachomatous inflammation-follicular: presence of **5 or more follicles**, each **at least 0.5 mm diameter**, in the **central part of the upper tarsal conjunctiva** | WHO field grade | (antwiadjei2017relationshipbetweenthe pages 29-35) |
| WHO simplified grading | TI | Trachomatous inflammation-intense: **pronounced inflammatory thickening** of the upper tarsal conjunctiva **obscuring more than half** of the normal deep tarsal vessels | WHO field grade | (antwiadjei2017relationshipbetweenthe pages 29-35) |
| WHO simplified grading | TS | Trachomatous scarring: **easily visible scars** in the tarsal conjunctiva | WHO field grade | (antwiadjei2017relationshipbetweenthe pages 29-35) |
| WHO simplified grading | TT | Trachomatous trichiasis: **at least one eyelash rubbing on the eyeball**, or evidence of recent removal of in-turned eyelashes | WHO field grade | (antwiadjei2017relationshipbetweenthe pages 29-35) |
| WHO simplified grading | CO | Corneal opacity: **easily visible corneal opacity over the pupil**, dense enough that **at least part of the pupil margin is blurred** | WHO field grade | (antwiadjei2017relationshipbetweenthe pages 29-35) |
| Elimination criteria | TT criterion | TT **unknown to the health system** in adults aged **≥15 years** must be **<0.2%** in each formerly endemic district | WHO elimination as a public health problem | (sitoe2024ongoingtransmissionof pages 1-2, hardingesch2023tropicaldataapproach pages 1-2) |
| Elimination criteria | TF criterion | TF in children aged **1-9 years** must be **<5%** in each formerly endemic district | WHO elimination as a public health problem | (sitoe2024ongoingtransmissionof pages 1-2, hardingesch2023tropicaldataapproach pages 1-2) |
| Elimination criteria | Service criterion | Evidence that the health system can **identify and manage incident TT cases** | WHO elimination as a public health problem | (sitoe2024ongoingtransmissionof pages 1-2) |
| Programmatic TF thresholds | TF ≥30% | At least **5 years** of A/F/E interventions (antibiotics, facial cleanliness, environmental improvement) | WHO programmatic threshold | (hardingesch2023tropicaldataapproach pages 1-2) |
| Programmatic TF thresholds | TF 10-29.9% | **3 years** of A/F/E interventions | WHO programmatic threshold | (hardingesch2023tropicaldataapproach pages 1-2) |
| Programmatic TF thresholds | TF 5-9.9% | **1 year** of A/F/E interventions | WHO programmatic threshold | (hardingesch2023tropicaldataapproach pages 1-2) |
| Programmatic TF thresholds | TF <5% | No further district-wide A/F/E intervention indicated; transition to surveillance/program review | WHO programmatic threshold | (antwiadjei2017relationshipbetweenthe pages 51-56, hardingesch2023tropicaldataapproach pages 1-2) |
| Control strategy | SAFE | **S**urgery for trichiasis; **A**ntibiotics (usually azithromycin MDA); **F**acial cleanliness; **E**nvironmental improvement (water, sanitation, fly control) | Current WHO strategy | (sitoe2024ongoingtransmissionof pages 1-2, hardingesch2023tropicaldataapproach pages 1-2) |
| Epidemiology | Population in endemic regions | Estimated **115.7 million** people resided in trachoma-endemic regions globally | 2023 | (maciel2024trachomaassociatedmorbidityand pages 1-2) |
| Epidemiology | People going blind | **1.8 million** people worldwide were going blind from trachoma | June 2021 | (hardingesch2023tropicaldataapproach pages 1-2) |
| Epidemiology | Countries achieving elimination | **18 countries** had achieved elimination as a public health problem | As of July 2023 | (sitoe2024ongoingtransmissionof pages 1-2) |
| Epidemiology | Endemic countries | Trachoma remained endemic in **40 countries** | 2023 | (maciel2024trachomaassociatedmorbidityand pages 1-2) |
| Epidemiology / Mozambique | TF prevalence range | In four enhanced impact survey districts, TF prevalence in children 1-9 years ranged **1.1%-6.0%** | Mozambique 2022 | (sitoe2024ongoingtransmissionof pages 1-2) |
| Epidemiology / Mozambique | PCR-confirmed ocular infection range | Ocular *C. trachomatis* nucleic acid prevalence ranged **1.1%-4.8%** | Mozambique 2022 | (sitoe2024ongoingtransmissionof pages 1-2) |
| Epidemiology / Mozambique | Pgp3 seroprevalence range | Anti-Pgp3 seroprevalence ranged **8.8%-24.3%** in children 1-9 years | Mozambique 2022 | (sitoe2024ongoingtransmissionof pages 1-2) |
| Epidemiology / Mozambique | Seroconversion rate range | Pgp3 seroconversion rates ranged **1.9-6.0 per 100 children per year** | Mozambique 2022 | (sitoe2024ongoingtransmissionof pages 1-2) |
| Diagnostics | Clinical grading | Population-based surveys and bedside diagnosis primarily use the **WHO simplified grading system** | Standard programmatic method | (sitoe2024ongoingtransmissionof pages 1-2, hardingesch2023tropicaldataapproach pages 1-2, antwiadjei2017relationshipbetweenthe pages 29-35) |
| Diagnostics | NAAT / PCR | Conjunctival swab nucleic acid amplification testing detects ocular *C. trachomatis* infection and is useful where TF correlates poorly with infection after MDA | Current adjunct / research-programmatic use | (sahin2023chlamydialeyeinfections pages 1-4, sitoe2024ongoingtransmissionof pages 1-2) |
| Diagnostics | Pgp3 serology | Dried blood spot serology for **anti-Pgp3 antibodies** is a promising population-level indicator of transmission intensity and post-MDA surveillance | Current adjunct / research-programmatic use | (sitoe2024ongoingtransmissionof pages 1-2) |


*Table: This table condenses core disease definitions, WHO grading and elimination thresholds, recent epidemiology, and practical diagnostics for trachoma. It is useful as a quick-reference artifact for a disease knowledge base entry with directly cited evidence.*

## References (URLs and publication dates)
URLs and dates are embedded in the cited sources’ metadata within this report; primary examples include: Scientific Reports (Oct 2024) Mozambique enhanced impact surveys (https://doi.org/10.1038/s41598-024-71201-z) (sitoe2024ongoingtransmissionof pages 1-2); Cureus (Jan 2024) environmental interventions review (https://doi.org/10.7759/cureus.52358) (ageed2024eliminatingtrachomain pages 2-3); Ophthalmic Epidemiology (Nov 2023) Tropical Data methods (https://doi.org/10.1080/09286586.2023.2249546) (hardingesch2023tropicaldataapproach pages 1-2).

## Limitations of this evidence package
* Verified ICD/ICD-11, MeSH, and MONDO identifiers were not present in retrieved full texts; ontology/database calls would be required for authoritative codes.
* Trachoma-specific randomized trial effect sizes for azithromycin MDA on TF/infection were not retrieved in citable evidence snippets during this run; the report therefore focuses on WHO-aligned strategy components, operational thresholds, and 2022–2024 program monitoring data that were available.
* Differential diagnosis details were not captured in the retrieved evidence set.

References

1. (sitoe2024ongoingtransmissionof pages 1-2): Henis Sitoe, William Edward Oswald, Felizmina Zita, Mawo Fall, Tamimo Momade, Molly W Adams, Rebecca M Flueckiger, Scott McPherson, Sabrina Eyob, Thuy Doan, Thomas M Lietman, Benjamin F Arnold, Karana Wickens, Sarah Gwyn, Diana L Martin, Mabula Kasubi, Sarah Boyd, Ana Bakhtiari, Cristina Jimenez, Anthony W Solomon, Emma M Harding-Esch, and Jeremiah M Ngondi. Ongoing transmission of trachoma in low prevalence districts in mozambique: results from four cross-sectional enhanced impact surveys, 2022. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-71201-z, doi:10.1038/s41598-024-71201-z. This article has 3 citations and is from a peer-reviewed journal.

2. (ageed2024eliminatingtrachomain pages 2-3): Ahmed Ageed and Maaz Khan. Eliminating trachoma in africa: the importance of environmental interventions. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.52358, doi:10.7759/cureus.52358. This article has 10 citations.

3. (sahin2023chlamydialeyeinfections pages 1-4): Seçil Özdemir Şahin. Chlamydial eye infections. Infectious Diseases, Jul 2023. URL: https://doi.org/10.5772/intechopen.111372, doi:10.5772/intechopen.111372. This article has 1 citations and is from a peer-reviewed journal.

4. (antwiadjei2017relationshipbetweenthe pages 29-35): EK Antwi-Adjei. Relationship between the prevalence of trachomatous inflammation in children (age 1-9years) and the prevalence of trichiasis in adults (age 15years and above) at a …. Unknown journal, 2017.

5. (hardingesch2023tropicaldataapproach pages 1-2): Emma M Harding-Esch, Clara R Burgert-Brucker, Cristina Jimenez, Ana Bakhtiari, Rebecca Willis, Michael Dejene Bejiga, Caleb Mpyet, Jeremiah Ngondi, Sarah Boyd, Mariamo Abdala, Amza Abdou, Yilikal Adamu, Addisu Alemayehu, Wondu Alemayehu, Tawfik Al-Khatib, Sue-Chen Apadinuwe, Naomie Awaca, Marcel S Awoussi, Gilbert Baayendag, Mouctar Dieng Badiane, Robin L Bailey, Wilfrid Batcho, Zulficar Bay, Assumpta Bella, Nassirou Beido, Yak Yak Bol, Clarisse Bougouma, Christopher J Brady, Victor Bucumi, Robert Butcher, Risiate Cakacaka, Anaseini Cama, Mamoudou Camara, Eunice Cassama, Shorai Grace Chaora, Amel Chenaoui Chebbi, Alvin Blessings Chisambi, Brian Chu, Abdulai Conteh, Sidi Mohamed Coulibaly, Paul Courtright, Abdi Dalmar, Tran Minh Dat, Thully Davids, Mohamed El Amine Djaker, Maria de Fátima Costa Lopes, Djore Dézoumbé, Sarity Dodson, Philip Downs, Stephanie Eckman, Bilghis Elkhair Elshafie, Mourad Elmezoghi, Ange Aba Elvis, Paul Emerson, Emilienne EE Epée, Daniel Faktaufon, Mawo Fall, Aréty Fassinou, Fiona Fleming, Rebecca Flueckiger, Koizan Kadjo Gamael, Mackline Garae, Jambi Garap, Katie Gass, Genet Gebru, Michael M Gichangi, Emanuele Giorgi, André Goépogui, Daniela Vaz Ferreira Gómez, Diana Paola Gómez Forero, Emily W Gower, Anna Harte, Rob Henry, Harvy Alberto Honorio-Morales, Dunera R Ilako, Amadou Alfa Bio Issifou, Ellen Jones, George Kabona, Martin Kabore, Boubacar Kadri, Khumbo Kalua, Sarjo Kebba Kanyi, Shambel Kebede, Fikreab Kebede, Jeremy D Keenan, Amir B Kello, Asad Aslam Khan, Houria Khelifi, Janvier Kilangalanga, Sung Hye Kim, Robert Ko, Susan Lewallen, Thomas Lietman, Makoy Samuel Yibi Logora, Yuri A Lopez, Chad MacArthur, Colin Macleod, Felix Makangila, Brehima Mariko, Diana L Martin, Michael Masika, Patrick Massae, Marilia Massangaie, Hadley S Matendechero, Tsedeke Mathewos, Siobhain McCullagh, Aboulaye Meite, Elsa Palma Mendes, Hirpa M Abdi, Hollman Miller, Abdellahi Minnih, Sailesh Kumar Mishra, Tuduetso Molefi, Aryc Mosher, Nerkoua M’Po, Francis Mugume, Robson Mukwiza, Consity Mwale, Stephen Mwatha, Upendo Mwingira, Scott D Nash, Christophe Nassa, Nebiyu Negussu, Cece Nieba, Jean Claude Noah Noah, Christian O Nwosu, Nicholas Olobio, Rapheal Opon, Alexandre Pavluck, Isaac Phiri, Merelesita Rainima-Qaniuci, Kristen K Renneker, Martha Idalí Saboyá-Díaz, Fatoumata Sakho, Salimato Sanha, Virginia Sarah, Boubacar Sarr, Celia L Szwarcwald, Ahmad Shah Salam, Shekhar Sharma, Fikre Seife, Gloria Marina Serrano Chavez, Mactar Sissoko, Henis Mior Sitoe, Oliver Sokana, Fentahun Tadesse, Fasiah Taleo, Sandra Liliana Talero, Youcef Tarfani, Amsayaw Tefera, Rabebe Tekeraoi, Andeberhan Tesfazion, Abubaker Traina, Lamine Traoré, Julián Trujillo-Trujillo, Edridah M Tukahebwa, Praveen Vashist, Ernest B Wanyama, Supriya D.P. Warusavithana, Titus K Watitu, Sheila West, Ye Win, Geordie Woods, Aya Yajima, Georges Yaya, Alem Zecarias, Solomon Zewengiel, Akoi Zoumanigui, Pamela J Hooper, Tom Millar, Lisa Rotondo, and Anthony W Solomon. Tropical data: approach and methodology as applied to trachoma prevalence surveys. Ophthalmic Epidemiology, 30:544-560, Nov 2023. URL: https://doi.org/10.1080/09286586.2023.2249546, doi:10.1080/09286586.2023.2249546. This article has 40 citations and is from a peer-reviewed journal.

6. (toumasis2024insightsintopathogenesis pages 9-10): Panagiotis Toumasis, Georgia Vrioni, Ioannis T. Tsinopoulos, Maria Exindari, and George Samonis. Insights into pathogenesis of trachoma. Microorganisms, 12:1544, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081544, doi:10.3390/microorganisms12081544. This article has 5 citations.

7. (toumasis2024insightsintopathogenesis pages 10-12): Panagiotis Toumasis, Georgia Vrioni, Ioannis T. Tsinopoulos, Maria Exindari, and George Samonis. Insights into pathogenesis of trachoma. Microorganisms, 12:1544, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081544, doi:10.3390/microorganisms12081544. This article has 5 citations.

8. (derrick2015trachomaandocular pages 5-6): Tamsyn Derrick, Chrissy h. Roberts, Anna R. Last, Sarah E. Burr, and Martin J. Holland. Trachoma and ocular chlamydial infection in the era of genomics. Mediators of Inflammation, Sep 2015. URL: https://doi.org/10.1155/2015/791847, doi:10.1155/2015/791847. This article has 41 citations and is from a peer-reviewed journal.

9. (atik2008identificationofnovel pages 2-3): Berna Atik, Troy A. Skwor, Ram Prasad Kandel, Bassant Sharma, Him Kant Adhikari, Lori Steiner, Henry Erlich, and Deborah Dean. Identification of novel single nucleotide polymorphisms in inflammatory genes as risk factors associated with trachomatous trichiasis. PLoS ONE, 3:e3600, Oct 2008. URL: https://doi.org/10.1371/journal.pone.0003600, doi:10.1371/journal.pone.0003600. This article has 34 citations and is from a peer-reviewed journal.

10. (natividad2007geneticvariationat pages 2-3): À. Natividad, À. Natividad, Neil A. Hanchard, Martin J. Holland, O. Mahdi, O. Mahdi, Mahamadou Diakite, K. Rockett, O. Jallow, H. Joof, Dominic P. Kwiatkowski, D. Mabey, and Robin L. Bailey. Genetic variation at the tnf locus and the risk of severe sequelae of ocular chlamydia trachomatis infection in gambians. Genes and Immunity, 8:288-295, Jun 2007. URL: https://doi.org/10.1038/sj.gene.6364384, doi:10.1038/sj.gene.6364384. This article has 67 citations and is from a peer-reviewed journal.

11. (atik2008identificationofnovel pages 1-2): Berna Atik, Troy A. Skwor, Ram Prasad Kandel, Bassant Sharma, Him Kant Adhikari, Lori Steiner, Henry Erlich, and Deborah Dean. Identification of novel single nucleotide polymorphisms in inflammatory genes as risk factors associated with trachomatous trichiasis. PLoS ONE, 3:e3600, Oct 2008. URL: https://doi.org/10.1371/journal.pone.0003600, doi:10.1371/journal.pone.0003600. This article has 34 citations and is from a peer-reviewed journal.

12. (paulet2024multimodalmucosaland pages 21-22): Elodie Paulet, Vanessa Contreras, Mathilde Galhaut, Ida Rosenkrands, Martin Holland, Matthew Burton, Jes Dietrich, Anne-Sophie Gallouet, Nathalie Bosquet, Francis Relouzat, Sébastien Langlois, Frank Follmann, Roger Le Grand, Marc Labetoulle, and Antoine Rousseau. Multimodal mucosal and systemic immune characterization of a non-human primate trachoma model highlights the critical role of local immunity during acute phase disease. PLOS Neglected Tropical Diseases, 18:e0012388, Aug 2024. URL: https://doi.org/10.1371/journal.pntd.0012388, doi:10.1371/journal.pntd.0012388. This article has 0 citations and is from a domain leading peer-reviewed journal.

13. (maciel2024trachomaassociatedmorbidityand pages 1-2): Adjoane Maurício Silva Maciel, Anderson Fuentes Ferreira, Nádia Maria Girão Saraiva de Almeida, Manuella Maurício Silva Maciel, Taynara Lais Silva, Mirele Coelho Araújo, Roberto da Justa Pires Neto, and Alberto Novaes Ramos Jr. Trachoma-associated morbidity and mortality in brazil: an ecological study focusing on hospitalization and mortality data, 2000−2022. Revista da Sociedade Brasileira de Medicina Tropical, Sep 2024. URL: https://doi.org/10.1590/0037-8682-0158-2024, doi:10.1590/0037-8682-0158-2024. This article has 1 citations.

14. (sitoe2024ongoingtransmissionof pages 2-3): Henis Sitoe, William Edward Oswald, Felizmina Zita, Mawo Fall, Tamimo Momade, Molly W Adams, Rebecca M Flueckiger, Scott McPherson, Sabrina Eyob, Thuy Doan, Thomas M Lietman, Benjamin F Arnold, Karana Wickens, Sarah Gwyn, Diana L Martin, Mabula Kasubi, Sarah Boyd, Ana Bakhtiari, Cristina Jimenez, Anthony W Solomon, Emma M Harding-Esch, and Jeremiah M Ngondi. Ongoing transmission of trachoma in low prevalence districts in mozambique: results from four cross-sectional enhanced impact surveys, 2022. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-71201-z, doi:10.1038/s41598-024-71201-z. This article has 3 citations and is from a peer-reviewed journal.

15. (sitoe2024ongoingtransmissionof pages 3-4): Henis Sitoe, William Edward Oswald, Felizmina Zita, Mawo Fall, Tamimo Momade, Molly W Adams, Rebecca M Flueckiger, Scott McPherson, Sabrina Eyob, Thuy Doan, Thomas M Lietman, Benjamin F Arnold, Karana Wickens, Sarah Gwyn, Diana L Martin, Mabula Kasubi, Sarah Boyd, Ana Bakhtiari, Cristina Jimenez, Anthony W Solomon, Emma M Harding-Esch, and Jeremiah M Ngondi. Ongoing transmission of trachoma in low prevalence districts in mozambique: results from four cross-sectional enhanced impact surveys, 2022. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-71201-z, doi:10.1038/s41598-024-71201-z. This article has 3 citations and is from a peer-reviewed journal.

16. (sitoe2024ongoingtransmissionof pages 4-6): Henis Sitoe, William Edward Oswald, Felizmina Zita, Mawo Fall, Tamimo Momade, Molly W Adams, Rebecca M Flueckiger, Scott McPherson, Sabrina Eyob, Thuy Doan, Thomas M Lietman, Benjamin F Arnold, Karana Wickens, Sarah Gwyn, Diana L Martin, Mabula Kasubi, Sarah Boyd, Ana Bakhtiari, Cristina Jimenez, Anthony W Solomon, Emma M Harding-Esch, and Jeremiah M Ngondi. Ongoing transmission of trachoma in low prevalence districts in mozambique: results from four cross-sectional enhanced impact surveys, 2022. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-71201-z, doi:10.1038/s41598-024-71201-z. This article has 3 citations and is from a peer-reviewed journal.

17. (antwiadjei2017relationshipbetweenthe pages 51-56): EK Antwi-Adjei. Relationship between the prevalence of trachomatous inflammation in children (age 1-9years) and the prevalence of trichiasis in adults (age 15years and above) at a …. Unknown journal, 2017.
