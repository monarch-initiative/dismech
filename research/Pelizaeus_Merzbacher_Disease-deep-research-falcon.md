---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:36.965820'
end_time: '2026-04-25T22:26:07.606108'
duration_seconds: 630.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pelizaeus-Merzbacher Disease
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pelizaeus-Merzbacher Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Pelizaeus-Merzbacher Disease** covering all of the
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
- **Disease Name:** Pelizaeus-Merzbacher Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Pelizaeus-Merzbacher Disease** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Pelizaeus–Merzbacher Disease (PMD)

### Target disease
- **Disease name:** Pelizaeus–Merzbacher disease (PMD)
- **Category:** Genetic leukodystrophy / hypomyelinating leukodystrophy
- **Primary causal gene:** **PLP1** (proteolipid protein 1)

---

## 1. Disease information

### 1.1 Overview (current understanding)
Pelizaeus–Merzbacher disease (PMD) is a **progressive X-linked hypomyelinating leukodystrophy** characterized by early neurologic onset (often infancy), with features such as nystagmus and developmental delay and later progression to spasticity/quadriplegia and ataxia. (rogac2023opticalgenomemapping pages 1-2)

A modern terminology used in parts of the literature is **hypomyelinating leukodystrophy type 1 (HLD1)** for the PLP1-associated disorder. (fukushima2024crisprcasrxmediatedknockdownof pages 1-2)

### 1.2 Key identifiers (as available in the retrieved sources)
- **OMIM (disease):** PMD **312080** (reported explicitly) (rogac2023opticalgenomemapping pages 1-2)
- **OMIM (gene):** **PLP1 300401** (reported explicitly) (rogac2023opticalgenomemapping pages 1-2)
- **MeSH:** **Pelizaeus-Merzbacher Disease (D020371)** (ClinicalTrials.gov condition browse) (NCT05659901 chunk 1)
- **MONDO:** Open Targets lists **MONDO_0010714 (Pelizeaus-Merzbacher spectrum disorder)** and subtype MONDO terms for connatal/transitional/classic PMD and PMD in female carriers. (NCT05659901 chunk 1)

**Not available in the retrieved full text for this run:** Orphanet ID and ICD-10/ICD-11 codes were not present in the available context; they should be added from Orphanet/WHO ICD sources during curation.

### 1.3 Synonyms / alternative names
- Pelizaeus–Merzbacher disease (PMD) (rogac2023opticalgenomemapping pages 1-2)
- Hypomyelinating leukodystrophy type 1 (HLD1) (fukushima2024crisprcasrxmediatedknockdownof pages 1-2)
- PLP1-related disorders (umbrella term often including PMD and SPG2) (wolf2025plp1relateddisordersa pages 3-6)

### 1.4 Evidence source type
This report integrates **aggregated disease-level sources** (e.g., clinical genetics summaries and trial registry records) with **individual-level case reports/series** and **cellular modeling studies**. (wolf2025plp1relateddisordersa pages 3-6, johari2023arehabilitationjourney pages 1-2, fukushima2024crisprcasrxmediatedknockdownof pages 1-2, NCT05659901 chunk 1)

---

## 2. Etiology

### 2.1 Primary causal factors
PMD is primarily caused by **pathogenic variants in PLP1** (Xq22) that disrupt CNS myelin formation, including **copy-number gains (duplications/triplications), sequence variants (missense/nonsense/splice/indels), and deletions**. (wolf2025plp1relateddisordersa pages 3-6, rogac2023opticalgenomemapping pages 1-2, akkus2023dörtailedenpelizaeusmerzbacher pages 1-2)

**Quantitative variant-class distribution (recent/compiled sources):**
- Xq22 microduplications/PLP1 duplications: **~60–70%** (akkus2023dörtailedenpelizaeusmerzbacher pages 1-2)
- Point mutations: **~10–25%** (akkus2023dörtailedenpelizaeusmerzbacher pages 1-2)
- Deletions: **~5–10%** (akkus2023dörtailedenpelizaeusmerzbacher pages 1-2)

A separate 2023 genetics report also states that **PLP1 duplications account for ~50–75%** of clinically manifest disease-causing variants. (rogac2023opticalgenomemapping pages 1-2)

### 2.2 Risk factors
- **Genetic:** X-linked inheritance; carrier females have a **50% transmission risk per pregnancy**. (wolf2025plp1relateddisorders pages 17-19, rogac2023opticalgenomemapping pages 1-2)
- **Sex:** Typically affects males more severely; females can be affected, in part due to **skewed X-inactivation** (clinical observation in a 2024 report). (dharni2024ararecase pages 1-2)

### 2.3 Protective factors
No protective genetic alleles or environmental protective factors were identified in the retrieved evidence for this run.

### 2.4 Gene–environment interactions
No gene–environment interactions were identified in the retrieved evidence for this run.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (symptoms/signs)
Commonly reported features include developmental delay, hypotonia, nystagmus, spasticity (paraparesis or quadriplegia), ataxia, dysarthria, dysphagia, and visual system involvement (e.g., optic atrophy). (johari2023arehabilitationjourney pages 1-2, manzke2025clinicalcharacteristicsof pages 1-2, rogac2023opticalgenomemapping pages 1-2)

A 2025 clinical report of classic PMD lists: “**developmental delays, nystagmus, spastic paraparesis, optic atrophy, dysphagia, appendicular ataxia, and progressive head tremor**.” (Manzke et al.; acceptance 2024-10-30; URL https://doi.org/10.1038/s41439-024-00306-8) (manzke2025clinicalcharacteristicsof pages 1-2)

A 2024 female-infant report emphasizes neuroregression and imaging-driven diagnosis in resource-limited settings and notes supportive therapy components. (dharni2024ararecase pages 1-2)

### 3.2 Subtypes and severity (current clinical framing)
A clinically used severity framing described in a 2023 rehabilitation-focused report includes connatal (type I), transitional (type II), and classic (type III) PMD, with **SPG2 (spastic paraplegia type 2)** as a milder allelic end of the PLP1-related spectrum. (johari2023arehabilitationjourney pages 1-2)

### 3.3 Age of onset, progression, and course
- **Classic PMD:** often presents in the **first year of life**, including neonatal hypotonia and failure to meet motor milestones, with progressive severe spasticity; life expectancy is commonly between adolescence and young adulthood. (johari2023arehabilitationjourney pages 1-2)
- **Connatal PMD:** **neonatal onset** with severe hypotonia, extrapyramidal signs and laryngeal stridor; high disability and early-childhood mortality from secondary complications. (johari2023arehabilitationjourney pages 1-2)
- **Trajectory note:** nystagmus may lessen over time while other motor/cognitive impairments worsen. (manzke2025clinicalcharacteristicsof pages 1-2)

### 3.4 Quality-of-life impact
Available sources emphasize major functional dependence and need for long-term multidisciplinary management, including mobility limitations (often wheelchair use), communication impairment, and caregiver burden consistent with a chronic progressive neurodisability. (johari2023arehabilitationjourney pages 1-2, dharni2024ararecase pages 1-2)

### 3.5 Suggested HPO terms (non-exhaustive; for knowledge base mapping)
Based on phenotypes explicitly described in the retrieved sources:
- Nystagmus; developmental delay; developmental regression; infantile hypotonia; spasticity; spastic paraparesis; spastic quadriplegia; ataxia; dysarthria; dysphagia; optic atrophy; tremor; dystonia; seizures; stridor. (johari2023arehabilitationjourney pages 1-2, manzke2025clinicalcharacteristicsof pages 1-2, dharni2024ararecase pages 1-2, rogac2023opticalgenomemapping pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
- **PLP1** is the core causal gene for PMD. (rogac2023opticalgenomemapping pages 1-2, akkus2023dörtailedenpelizaeusmerzbacher pages 1-2)

### 4.2 Pathogenic variant types and functional consequences
**Copy-number gains (duplications and more complex multiplications)**
- Tandem duplications involving Xq22 and PLP1 are common; triplication/partial triplication/quintuplication and complex rearrangements are also reported. (wolf2025plp1relateddisordersa pages 3-6)

**Loss of function / deletions**
- Whole-gene deletions are reported as uncommon (“**fewer than 2%**” of PMD phenotypes). (wolf2025plp1relateddisordersa pages 3-6)

**Missense variants and misfolding/ER stress**
- Severe connatal forms are described as often associated with missense variants that cause protein misfolding and oligodendrocyte toxicity. (johari2023arehabilitationjourney pages 1-2)

### 4.3 Genotype–phenotype correlations (clinically used heuristics)
A clinical genetics summary indicates that **gene-targeted deletion/duplication analysis** accounts for **~60–70%** of pathogenic variants (largely duplications), while **sequence analysis** accounts for **~30–40%** (missense/nonsense/splice/small indels). (wolf2025plp1relateddisordersa pages 3-6)

A 2023 rehabilitation-focused synthesis suggests:
- Connatal PMD is “typically due to **missense** mutations” (johari2023arehabilitationjourney pages 1-2)
- Classic PMD (most common phenotype) is “typically due to **duplications** of PLP1” (johari2023arehabilitationjourney pages 1-2)
- SPG2 is often due to PLP1 deletions with milder phenotype (johari2023arehabilitationjourney pages 1-2)

### 4.4 Modifier genes / epigenetics
No modifier genes or epigenetic mechanisms were identified in the retrieved evidence for this run (beyond clinical mention of skewed X-inactivation affecting female carriers). (dharni2024ararecase pages 1-2)

---

## 5. Environmental information
PMD is a **monogenic** disorder; the retrieved evidence does not support specific environmental causes, lifestyle risk factors, or infectious triggers.

---

## 6. Mechanism / pathophysiology

### 6.1 Mechanistic chain (from variant to clinical manifestation)
**Upstream:** PLP1 dosage changes or missense variants alter PLP1 abundance/processing in oligodendrocytes (myelin-forming glia). (johari2023arehabilitationjourney pages 1-2, fukushima2024crisprcasrxmediatedknockdownof pages 1-2)

**Cellular stress and downstream effects:** A 2024 experimental report states that a major contributor is defective oligodendroglial myelin sheath formation triggered by “**endoplasmic reticulum (ER) stress and subsequent unfolded protein response (UPR)**.” (fukushima2024crisprcasrxmediatedknockdownof pages 1-2)

**Tissue-level outcome:** CNS hypomyelination/dysmyelination produces diffuse white matter abnormalities on MRI and progressive motor and neurologic impairment. (manzke2025clinicalcharacteristicsof pages 1-2, dharni2024ararecase pages 1-2)

### 6.2 Recent mechanistic development (2024)
A 2024 letter describes rescue of PLP1-mutant cellular phenotypes: “**incomplete cell shapes induced by PLP1 p.Ala243Val can be restored by knockdown of Rab7B using… CRISPR and CasRx (Cas13d)**,” and Rab7B knockdown promoted trafficking of mutant PLP1 to “**LAMP1-positive organelles**,” suggesting vesicle trafficking/lysosomal routing as a therapeutic lever. (Published 2024; DOI https://doi.org/10.1177/26331055241276873) (fukushima2024crisprcasrxmediatedknockdownof pages 1-2)

### 6.3 Suggested ontology terms
**GO biological processes (suggested):** myelination; response to endoplasmic reticulum stress; unfolded protein response; protein/vesicle trafficking; lysosome organization/targeting. (fukushima2024crisprcasrxmediatedknockdownof pages 1-2)

**Cell types (Cell Ontology; suggested):** oligodendrocyte. (fukushima2024crisprcasrxmediatedknockdownof pages 1-2)

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
Primary system: **central nervous system white matter** (leukodystrophy/hypomyelination). (rogac2023opticalgenomemapping pages 1-2, manzke2025clinicalcharacteristicsof pages 1-2)

### 7.2 Imaging-supported affected structures
MRI/MRS findings in classic PMD include diffuse white matter signal abnormalities and atrophy of major white-matter and hindbrain structures (corpus callosum, cerebellum), with possible brainstem/internal capsule involvement. (manzke2025clinicalcharacteristicsof pages 1-2, manzke2025clinicalcharacteristicsof media 789d293e)

**Suggested UBERON terms (examples):** brain white matter; corpus callosum; cerebellum; brainstem; internal capsule.

---

## 8. Temporal development (natural history)
PMD typically has **early onset (neonatal/infancy)** and **chronic progressive course**, with severity depending on subtype (connatal vs classic vs SPG2 spectrum). (johari2023arehabilitationjourney pages 1-2, manzke2025clinicalcharacteristicsof pages 1-2)

---

## 9. Inheritance and population

### 9.1 Inheritance
X-linked inheritance is consistently reported. (wolf2025plp1relateddisorders pages 17-19, rogac2023opticalgenomemapping pages 1-2)

Genetic counseling summary (PLP1-related disorders):
- If a mother carries the familial PLP1 variant, each pregnancy has **50% chance** of transmission; males inheriting the variant are affected; females may be asymptomatic or have mild-to-moderate signs. (wolf2025plp1relateddisorders pages 17-19)

### 9.2 Epidemiology (statistics)
A 2023 report provides an international prevalence estimate of **1:90,000–1:750,000 births**, varying by ethnic demographic context. (johari2023arehabilitationjourney pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical and MRI diagnosis
MRI is emphasized as central to diagnosis and phenotypic classification. (johari2023arehabilitationjourney pages 1-2)

A 2024 case report highlights a resource-limited workflow:
- “**Early diagnosis is crucial… with MRI serving as a potential alternative to genetic testing in resource-limited settings**.” (Published online 2024-10-03; URL https://doi.org/10.18231/j.ijn.2024.037) (dharni2024ararecase pages 1-2)
- MRI described “**bilaterally symmetrical T2/FLAIR hyperintense and T1 hypointense signal alterations in the cerebral white matter and brainstem**.” (dharni2024ararecase pages 1-2)

A 2025 imaging description (accepted 2024-10-30) reports hypomyelination with diffuse white matter hyperintensity and atrophy of the corpus callosum and cerebellum, with MRS changes (NAA/Cr decreased; mI/Cr increased). (manzke2025clinicalcharacteristicsof pages 1-2, manzke2025clinicalcharacteristicsof media 789d293e)

### 10.2 Genetic testing (real-world implementation)
A recommended testing strategy for PLP1-related disorders:
1) **Deletion/duplication (CNV) testing** (MLPA, targeted microarray, qPCR, FISH) (wolf2025plp1relateddisordersa pages 3-6)
2) If CNV negative, **PLP1 sequence analysis** for missense/nonsense/splice variants and small indels (wolf2025plp1relateddisordersa pages 3-6)
3) Alternative approaches: multigene leukodystrophy panel or exome/genome sequencing. (wolf2025plp1relateddisordersa pages 3-6)

**Modern SV resolution:** a 2023 Frontiers in Genetics report argues that optical genome mapping can resolve complex/inverted duplications not captured by standard CNV tests, improving prenatal and postnatal counseling. (Published 2023-07-25; URL https://doi.org/10.3389/fgene.2023.1173426) (rogac2023opticalgenomemapping pages 1-2)

### 10.3 Omics/biomarkers under development
The Ionis observational Rocket study explicitly targets biomarker characterization and progression measures.
- Trial brief summary includes: “**assess longitudinal changes in proteolipid protein 1 (PLP1) protein, disease-related biomarkers in CSF and blood, neuroimaging parameters… and… clinical… caregiver-reported outcome assessments**.” (ClinicalTrials.gov, last update posted 2026-04-17; URL https://clinicaltrials.gov/study/NCT05659901) (NCT05659901 chunk 1)

### 10.4 Differential diagnosis
Imaging-based differentials mentioned include **Salla disease** and other leukodystrophies, ruled out by imaging in a 2024 case report. (dharni2024ararecase pages 1-2)

---

## 11. Outcome / prognosis
Prognosis is subtype-dependent:
- **Classic PMD:** life expectancy “around young adulthood” and “commonly between adolescence to young adulthood.” (johari2023arehabilitationjourney pages 1-2)
- **Connatal PMD:** death can occur in early childhood due to secondary complications. (johari2023arehabilitationjourney pages 1-2)

Longitudinal stability can occur in some individuals (e.g., a 32-year-old classic PMD case report describes stable MRI findings over a 5-year period despite longstanding disability). (johari2023arehabilitationjourney pages 1-2)

---

## 12. Treatment

### 12.1 Current standard of care (real-world implementation)
No definitive disease-modifying therapy is established; care is supportive and multidisciplinary, addressing spasticity, communication/swallowing, function, and seizures.
- Supportive rehabilitation measures (play/occupational therapy, speech therapy, physiotherapy for spasticity/contractures, behavioral therapy) are described in a 2024 case report. (dharni2024ararecase pages 1-2)
- Symptomatic medications reported in a longitudinal case include baclofen and botulinum toxin A for spasticity (case report context). (johari2023arehabilitationjourney pages 1-2)

### 12.2 Advanced/experimental therapeutics and clinical trials (focus on 2023–2024+ developments)

**Antisense oligonucleotide (ASO) therapy targeting PLP1 duplication**
- **Orbit (ION356)**: Phase 1b open-label multiple-ascending dose study, intrathecal ION356, enrolling ~24 pediatric male participants (2–17 years) with **genetically confirmed PLP1 duplication**; start date **2024-04-10** (actual); ClinicalTrials.gov first posted **2023-11-29**; URL: https://clinicaltrials.gov/study/NCT06150716. (NCT06150716 chunk 1)

**Biomarker and progression study supporting therapy development**
- **Rocket**: Observational integrated prospective/retrospective study (up to 32 participants) requiring PLP1 duplication; start **2022-10-03**; primary completion estimated **2029-03**; measures include CSF/blood PLP1 and biomarkers, MRI/MRS, and clinical/caregiver outcomes; URL: https://clinicaltrials.gov/study/NCT05659901. (NCT05659901 chunk 1)

**Cell therapy/stem cell transplantation (historical but real-world implemented trial)**
- **HuCNS-SC intracerebral transplantation (connatal PMD)**: Phase 1 safety/preliminary efficacy, enrollment 4, completed; includes MRI myelination assessment; URL: https://clinicaltrials.gov/study/NCT01005004. (NCT01005004 chunk 1)
- Long-term follow-up study: enrollment 4, completed; URL: https://clinicaltrials.gov/study/NCT01391637. (NCT01391637 chunk 1)

### 12.3 Suggested MAXO terms (examples)
- Physical therapy; occupational therapy; speech therapy; antispasticity treatment; seizure management; intrathecal antisense oligonucleotide therapy; stem cell transplantation; genetic counseling; prenatal testing; preimplantation genetic testing (PGT).

---

## 13. Prevention
There is no primary prevention for a monogenic disorder like PMD; prevention focuses on **genetic counseling** and **reproductive options**.
- A clinical genetics resource states “**prenatal and preimplantation genetic testing (PGT) are possible**” when the familial PLP1 variant is known, while emphasizing limitations of phenotype prediction due to intrafamilial variability. (wolf2025plp1relateddisorders pages 17-19)

---

## 14. Other species / natural disease
No naturally occurring non-human PMD evidence was present in the retrieved context for this run.

---

## 15. Model organisms / experimental models

### 15.1 Cellular models and functional genomics (recent)
A 2024 study in an oligodendroglial differentiation model links PLP1 mutation to ER stress/UPR and demonstrates a functional-genomics style rescue via CRISPR/CasRx knockdown of Rab7B. (Published 2024; URL https://doi.org/10.1177/26331055241276873) (fukushima2024crisprcasrxmediatedknockdownof pages 1-2)

### 15.2 Human imaging phenotypes (for translational modeling)
A 2025 imaging figure provides a practical radiologic phenotype definition for modeling endpoints (white matter hyperintensity, corpus callosum/cerebellar atrophy, and MRS NAA/Cr↓ with mI/Cr↑), which can inform outcome measures in translational studies. (manzke2025clinicalcharacteristicsof media 789d293e)

---

## Key visual evidence (diagnostic imaging phenotype)
The following figure captures representative MRI and MR spectroscopy abnormalities reported in a patient with classic PMD.

(manzke2025clinicalcharacteristicsof media 789d293e)

---

## Summary table (for knowledge base ingestion)
| Section | Key facts | Ontology/standard terms | Key sources |
|---|---|---|---|
| Identifiers | PMD is a severe/progressive X-linked recessive hypomyelinating leukodystrophy caused by PLP1 variants; OMIM disease ID 312080 and PLP1 OMIM gene ID 300401 are explicitly reported. ClinicalTrials.gov maps the condition to MeSH term **Pelizaeus-Merzbacher Disease** (D020371). Open Targets lists **MONDO_0010714 Pelizeaus-Merzbacher spectrum disorder** and subtype MONDO terms for connatal, transitional, classic, and female-carrier disease. Disease information here is derived from aggregated disease-level resources plus individual case reports/trials. (rogac2023opticalgenomemapping pages 1-2, NCT05659901 chunk 1) | MONDO: MONDO_0010714; MONDO_0017221 connatal form; MONDO_0017222 classic form; MONDO_0017223 transitional form; MONDO_0017224 female carriers. MeSH: D020371. Suggested disease label: hypomyelinating leukodystrophy type 1 / PLP1-related disorder. | Rogac et al., Front Genet, 2023-07-25, DOI: https://doi.org/10.3389/fgene.2023.1173426 (rogac2023opticalgenomemapping pages 1-2); ClinicalTrials.gov NCT05659901, first posted 2022-12-21, https://clinicaltrials.gov/study/NCT05659901 (NCT05659901 chunk 1) |
| Etiology/Genetics | Causal gene: **PLP1**. Variant classes include duplications, deletions, and point mutations. Quantitative breakdowns reported: Xq22 microduplications/PLP1 duplications ~**60–70%** of cases, point mutations **10–25%**, deletions **5–10%**; another source states PLP1 duplications account for **50–75%** of clinically manifest variants. Gene-targeted deletion/duplication analysis detects ~**60–70%** of pathogenic variants; sequence analysis detects ~**30–40%**; whole-gene deletions occur in **<2%** of PMD phenotypes. Tandem duplications at Xq22 predominate; triplication/partial triplication/quintuplication and complex/inverted duplications are reported. Inheritance is X-linked; carrier mothers have a **50%** transmission risk per pregnancy; affected males usually more severely affected, while females may be asymptomatic or mildly/moderately affected due to skewed X-inactivation/other factors. (akkus2023dörtailedenpelizaeusmerzbacher pages 1-2, rogac2023opticalgenomemapping pages 1-2, wolf2025plp1relateddisordersa pages 3-6, wolf2025plp1relateddisorders pages 17-19, dharni2024ararecase pages 1-2) | Gene: PLP1. Suggested HGNC symbol: PLP1. HPO inheritance term suggestion: X-linked recessive inheritance. | Akkuş & Özyavuz Çubuk, Turk J Pediatr Dis, 2023-07-11/2023-08-02, DOI: https://doi.org/10.12956/tchd.1275274 (akkus2023dörtailedenpelizaeusmerzbacher pages 1-2); Rogac et al., 2023-07-25, DOI above (rogac2023opticalgenomemapping pages 1-2); Wolf & van Spaendonk, PLP1-related disorders, 2025 text excerpt (wolf2025plp1relateddisordersa pages 3-6, wolf2025plp1relateddisorders pages 17-19) |
| Phenotypes/Natural history | Core features across sources: developmental delay, infantile hypotonia, nystagmus, spasticity/spastic quadriplegia or paraparesis, ataxia, dysarthria, dysphagia, optic atrophy/visual decline, tremor, behavioral/cognitive impairment; severe forms may include dystonia, seizures, laryngeal stridor, inability to walk or speak. Classic PMD often presents in the **first year of life**; connatal PMD presents in **neonatal life** with severe hypotonia and extrapyramidal signs; SPG2 is the mildest end, often first decade onset with spastic paraparesis/ataxia/autonomic dysfunction. Nystagmus may lessen over time while motor and cognitive impairment worsen. Forms 0–4 severity grading and connatal/transitional/classic/SPG2 spectrum are described. Female cases can occur. (johari2023arehabilitationjourney pages 1-2, manzke2025clinicalcharacteristicsof pages 1-2, dharni2024ararecase pages 1-2, rogac2023opticalgenomemapping pages 1-2) | Suggested HPO: developmental delay, infantile axial hypotonia, nystagmus, spasticity, spastic paraplegia, spastic quadriplegia, ataxia, dysarthria, dysphagia, optic atrophy, tremor, seizures, dystonia, developmental regression, stridor. | Johari et al., J Med Clin Res Rev, 2023-10-14, DOI: https://doi.org/10.33425/2639-944x.1349 (johari2023arehabilitationjourney pages 1-2); Manzke et al., Hum Genome Var, accepted 2024-10-30/published 2025-01, DOI: https://doi.org/10.1038/s41439-024-00306-8 (manzke2025clinicalcharacteristicsof pages 1-2); Dharni et al., IP Indian J Neurosci, 2024-10-03, DOI: https://doi.org/10.18231/j.ijn.2024.037 (dharni2024ararecase pages 1-2) |
| Diagnostics | Recommended molecular workflow: if PLP1-related disease is suspected, start with **targeted deletion/duplication analysis** (MLPA, targeted microarray, qPCR, FISH); if negative, proceed to **PLP1 sequence analysis** for missense/nonsense/splice/small indels; multigene panel or exome/genome testing are alternatives. Real-world methods used include MLPA plus chromosomal microarray; optical genome mapping can resolve complex/inverted duplications not characterized by routine CNV assays. MRI is central: severe forms show diffuse/confluent hypomyelination; milder/SPG2 can show tigroid/patchy hypomyelination. Reported MRI/MRS findings include diffuse T2/FLAIR white-matter hyperintensity, T1 hypointensity, involvement of internal capsules/brainstem, and atrophy of corpus callosum/cerebellum with decreased **NAA/Cr** and increased **mI/Cr** ratios. WGS has been evaluated as a first-line leukodystrophy tool in LeukoSEQ. (wolf2025plp1relateddisordersa pages 3-6, rogac2023opticalgenomemapping pages 1-2, akkus2023dörtailedenpelizaeusmerzbacher pages 1-2, manzke2025clinicalcharacteristicsof pages 1-2, manzke2025clinicalcharacteristicsof media 789d293e, NCT02699190 chunk 1, dharni2024ararecase pages 1-2) | Suggested terms: MRI white matter abnormality; hypomyelination; corpus callosum atrophy; cerebellar atrophy. MeSH trial mapping: D020371. | Wolf & van Spaendonk, 2025 text excerpt (wolf2025plp1relateddisordersa pages 3-6); Rogac et al., 2023-07-25 DOI above (rogac2023opticalgenomemapping pages 1-2); Manzke et al., 2025 DOI above + Figure 1 imaging summary (manzke2025clinicalcharacteristicsof pages 1-2, manzke2025clinicalcharacteristicsof media 789d293e); LeukoSEQ NCT02699190, results first posted 2025-06-15, https://clinicaltrials.gov/study/NCT02699190 (NCT02699190 chunk 1) |
| Prognosis/Epidemiology | Reported prevalence range: **1:90,000 to 1:750,000 births**, varying by population. Prognosis depends on subtype: classic PMD is the most common phenotype and has life expectancy around **young adulthood/adolescence to young adulthood**; connatal PMD is most severe and death may occur in **early childhood**, though attentive care can prolong survival. PMD is usually chronic and progressive, though some individuals may show relative imaging stability over years despite clinical disability. (johari2023arehabilitationjourney pages 1-2, manzke2025clinicalcharacteristicsof pages 1-2) | Suggested HPO prognosis-related concepts: progressive neurologic deterioration; reduced life expectancy. | Johari et al., 2023-10-14, DOI above (johari2023arehabilitationjourney pages 1-2); Manzke et al., 2025 DOI above (manzke2025clinicalcharacteristicsof pages 1-2) |
| Treatments & trials | No definitive disease-modifying standard therapy is established; management is multidisciplinary and supportive: physiotherapy, occupational/play therapy, speech therapy, spasticity treatment (e.g., baclofen, botulinum toxin in case report), behavioral therapy, seizure counseling/antiepileptics as needed. **Rocket** observational biomarker study (**NCT05659901**) is recruiting; start **2022-10-03**, estimated completion **2029-03**, enrollment **32**, focusing on CSF/blood PLP1 biomarkers, MRI/MRS, motor/spasticity/dysphagia/cognition/behavior/sleep outcomes; includes genetically confirmed **PLP1 duplication**, males **6 months–17 years**. **Orbit** interventional ASO study of intrathecal **ION356** (**NCT06150716**) is recruiting; first posted **2023-11-29**, actual start **2024-04-10**, estimated completion **2028-06**, enrollment **24**, phase **1b**, in males **2–17 years** with **PLP1 duplication**. Historical stem-cell trials: **HuCNS-SC** intracerebral transplantation in connatal PMD (**NCT01005004**) phase 1, enrollment **4**, completed; long-term follow-up **NCT01391637**, enrollment **4**, completed. Wolf excerpt also notes antisense oligonucleotide therapy and deferiprone in trials, while curcumin was not effective in a small human group. (johari2023arehabilitationjourney pages 1-2, dharni2024ararecase pages 1-2, NCT05659901 chunk 1, NCT06150716 chunk 1, NCT01391637 chunk 1, NCT01005004 chunk 1, wolf2025plp1relateddisorders pages 17-19) | Suggested MAXO: physical therapy, occupational therapy, speech therapy, seizure management, antispasticity treatment, stem cell transplantation, intrathecal antisense oligonucleotide therapy, genetic counseling, prenatal testing/PGT. | ClinicalTrials.gov NCT05659901 https://clinicaltrials.gov/study/NCT05659901 (NCT05659901 chunk 1); NCT06150716 https://clinicaltrials.gov/study/NCT06150716 (NCT06150716 chunk 1); NCT01005004 https://clinicaltrials.gov/study/NCT01005004 (NCT01005004 chunk 1); NCT01391637 https://clinicaltrials.gov/study/NCT01391637 (NCT01391637 chunk 1); Johari et al., 2023 DOI above (johari2023arehabilitationjourney pages 1-2); Dharni et al., 2024 DOI above (dharni2024ararecase pages 1-2) |
| Models/Mechanisms | Mechanistically, PMD/HLD1 reflects defective CNS myelin formation from PLP1 dosage imbalance or mutation. One 2024 experimental paper states a “major cause” is incomplete/defective oligodendroglial myelin sheath formation triggered by **ER stress** and **unfolded protein response (UPR)**; PLP1 p.Ala243Val impairs oligodendroglial morphological differentiation, and **Rab7B** knockdown via **CRISPR/CasRx** partially restored morphology and promoted trafficking to **LAMP1-positive** organelles in an oligodendroglial cell line. Another 2024 resource reports generation of a **PLP1-C33Y human iPSC line** by CRISPR/Cas9 for disease modeling. Clinical review/case sources additionally describe PLP overexpression causing nonfunctional myelin protein and oligodendrocyte dysfunction. (fukushima2024crisprcasrxmediatedknockdownof pages 1-2, johari2023arehabilitationjourney pages 1-2) | Suggested GO: myelination; response to endoplasmic reticulum stress; unfolded protein response; protein trafficking; lysosome. Suggested CL: oligodendrocyte. Suggested UBERON: central nervous system white matter, corpus callosum, cerebellum, brainstem. | Fukushima et al., Neuroscience Insights, 2024, DOI: https://doi.org/10.1177/26331055241276873 (fukushima2024crisprcasrxmediatedknockdownof pages 1-2); Schreiber & Zafeiriou, Stem Cell Research, 2024-02, DOI: https://doi.org/10.1016/j.scr.2023.103276 (supporting model generation noted in retrieved paper list, not otherwise detailed in context); Johari et al., 2023 DOI above (johari2023arehabilitationjourney pages 1-2) |


*Table: This table condenses key disease knowledge for Pelizaeus–Merzbacher disease, including identifiers, genetics, phenotype, diagnostics, prognosis, treatment trials, and mechanisms. It emphasizes quantitative variant distributions and active clinical studies using only facts supported by the cited context IDs.*

---

## Expert synthesis / analysis (evidence-based)
1. **PLP1 CNV is the dominant genetic mechanism** in clinically manifest PMD, with duplication frequencies consistently reported in the majority range (50–75% or ~60–70%), supporting CNV-first genetic testing (MLPA/microarray/qPCR/FISH) as a pragmatic diagnostic front line before sequencing. (rogac2023opticalgenomemapping pages 1-2, akkus2023dörtailedenpelizaeusmerzbacher pages 1-2, wolf2025plp1relateddisordersa pages 3-6)
2. **Therapeutic development is shifting toward molecularly stratified cohorts**, particularly PLP1 duplication classic PMD, as evidenced by Ionis’ biomarker study (Rocket) and ASO therapeutic trial (Orbit/ION356) requiring genetic confirmation of PLP1 duplication and using CSF/blood PLP1 plus MRI/MRS and functional outcomes. (NCT05659901 chunk 1, NCT06150716 chunk 1)
3. **Mechanistic convergence on oligodendrocyte stress pathways** (ER stress/UPR) and proteostasis/trafficking suggests druggable nodes beyond PLP1 itself; the Rab7B knockdown study provides a concrete example of targeting vesicular trafficking/lysosomal routing to ameliorate a PLP1-mutation phenotype in vitro. (fukushima2024crisprcasrxmediatedknockdownof pages 1-2)

---

### Notes on limitations of this run
- ICD-10/ICD-11 codes and Orphanet identifiers were not present in the retrieved full-text context; these should be added from ICD/Orphanet sources during curation.
- Several high-priority 2023–2024 review articles and interventional clinical publications were not accessible in full text via the current retrieval; the report therefore emphasizes trials registry records and available peer-reviewed articles/case studies.


References

1. (rogac2023opticalgenomemapping pages 1-2): Mihael Rogac, Anja Kovanda, Luca Lovrečić, and Borut Peterlin. Optical genome mapping in an atypical pelizaeus-merzbacher prenatal challenge. Frontiers in Genetics, Jul 2023. URL: https://doi.org/10.3389/fgene.2023.1173426, doi:10.3389/fgene.2023.1173426. This article has 7 citations and is from a peer-reviewed journal.

2. (fukushima2024crisprcasrxmediatedknockdownof pages 1-2): Nana Fukushima, Yuki Miyamoto, and Junji Yamauchi. Crispr/casrx-mediated knockdown of rab7b restores incomplete cell shape induced by pelizaeus-merzbacher disease-associated plp1 p.ala243val. Neuroscience Insights, Jan 2024. URL: https://doi.org/10.1177/26331055241276873, doi:10.1177/26331055241276873. This article has 4 citations.

3. (NCT05659901 chunk 1):  Rocket Study: A Study to Characterize Biomarkers and Disease Progression in Participants With Pelizaeus-Merzbacher Disease. Ionis Pharmaceuticals, Inc.. 2022. ClinicalTrials.gov Identifier: NCT05659901

4. (wolf2025plp1relateddisordersa pages 3-6): NI Wolf and RML van Spaendonk. Plp1-related disorders. Unknown journal, 2025.

5. (johari2023arehabilitationjourney pages 1-2): Azri Johari, Ling Lan, and Harsh Kandpal. A rehabilitation journey with pelizaeus-merzbacher disease (pmd). Journal of Medical - Clinical Research &amp; Reviews, Oct 2023. URL: https://doi.org/10.33425/2639-944x.1349, doi:10.33425/2639-944x.1349. This article has 1 citations.

6. (akkus2023dörtailedenpelizaeusmerzbacher pages 1-2): Nejmiye AKKUŞ and Pelin ÖZYAVUZ ÇUBUK. Dört aileden pelizaeus-merzbacher sendromlu altı hastanın klinik ve moleküler sitogenetik analizleri. Turkish Journal of Pediatric Disease, pages 1-6, Jul 2023. URL: https://doi.org/10.12956/tchd.1275274, doi:10.12956/tchd.1275274. This article has 0 citations.

7. (wolf2025plp1relateddisorders pages 17-19): NI Wolf and RML van Spaendonk. Plp1-related disorders. Unknown journal, 2025.

8. (dharni2024ararecase pages 1-2): Tania Dharni, Sandeep Aggarwal, Manmeet Kaur Sodhi, Vaibhav Oberoi, Pinki Meena, Asgar Ali, Nilesh Patidar, and Ratul Khanna. A rare case of radiologically diagnosed pelizaeus-merzbacherś disease (pmd) in a female infant. IP Indian Journal of Neurosciences, 10:171-173, Oct 2024. URL: https://doi.org/10.18231/j.ijn.2024.037, doi:10.18231/j.ijn.2024.037. This article has 0 citations.

9. (manzke2025clinicalcharacteristicsof pages 1-2): Pedro Manzke, Pedro Renato P. Brandão, Talita Balieiro, Diógenes Diego de Carvalho Bispo, Maria Joana Osório, and Gustavo Barcelos Barra. Clinical characteristics of the ala21val variant in the myelin proteolipid protein 1 (plp1) gene associated with pelizaeus-merzbacher disease in a brazilian male patient. Human Genome Variation, Jan 2025. URL: https://doi.org/10.1038/s41439-024-00306-8, doi:10.1038/s41439-024-00306-8. This article has 0 citations.

10. (manzke2025clinicalcharacteristicsof media 789d293e): Pedro Manzke, Pedro Renato P. Brandão, Talita Balieiro, Diógenes Diego de Carvalho Bispo, Maria Joana Osório, and Gustavo Barcelos Barra. Clinical characteristics of the ala21val variant in the myelin proteolipid protein 1 (plp1) gene associated with pelizaeus-merzbacher disease in a brazilian male patient. Human Genome Variation, Jan 2025. URL: https://doi.org/10.1038/s41439-024-00306-8, doi:10.1038/s41439-024-00306-8. This article has 0 citations.

11. (NCT06150716 chunk 1):  Orbit Study: A Study to Evaluate the Safety, Pharmacokinetics, and Pharmacodynamics of Intrathecally Administered ION356 in Participants With Pelizaeus Merzbacher Disease (PMD). Ionis Pharmaceuticals, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06150716

12. (NCT01005004 chunk 1):  Study of Human Central Nervous System (CNS) Stem Cells Transplantation in Pelizaeus-Merzbacher Disease (PMD) Subjects. StemCells, Inc.. 2009. ClinicalTrials.gov Identifier: NCT01005004

13. (NCT01391637 chunk 1):  Long-Term Follow-Up Study of Human Stem Cells Transplanted in Subjects With Connatal Pelizaeus-Merzbacher Disease (PMD). StemCells, Inc.. 2011. ClinicalTrials.gov Identifier: NCT01391637

14. (NCT02699190 chunk 1): Adeline Vanderver, MD. LeukoSEQ: Whole Genome Sequencing as a First-Line Diagnostic Tool for Leukodystrophies. Children's Hospital of Philadelphia. 2017. ClinicalTrials.gov Identifier: NCT02699190
