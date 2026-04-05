---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T16:35:32.678541'
end_time: '2026-04-04T16:52:51.575042'
duration_seconds: 1038.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Soil-transmitted helminthiases
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 83
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Soil-transmitted helminthiases
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Soil-transmitted helminthiases** covering all of the
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
- **Disease Name:** Soil-transmitted helminthiases
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Soil-transmitted helminthiases** covering all of the
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


# Comprehensive Research Report: Soil-transmitted helminthiases (STH)

**Prepared for:** disease knowledge base curation  
**Target disease:** Soil-transmitted helminthiases (STH) (infectious disease/NTD complex)  
**Primary recent anchor sources (2023–2024):** Chen et al. 2024 (GBD 2021 analysis), Keiser 2023 (therapeutics pipeline), Emerson et al. 2024 (policy analysis), Manuel et al. 2024 (soil qPCR surveillance), multiple 2024 systematic reviews/meta-analyses and clinical studies. (chen2024globalburdenof pages 1-2, chen2024globalburdenof media e4718bac, keiser2023presentdrugsand pages 4-5, emerson2024needfora pages 6-7, manuel2024soilsurveillancefor pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
Soil-transmitted helminthiases are intestinal nematode infections transmitted via eggs/larvae contaminating soil in settings with inadequate sanitation. In current global-control framing, the most important human STH species are **Ascaris lumbricoides** (roundworm; ascariasis), **Trichuris trichiura** (whipworm; trichuriasis), and hookworms (**Necator americanus**, **Ancylostoma duodenale**). (chen2024globalburdenof pages 1-2, keiser2023presentdrugsand pages 2-3)

### 1.2 Synonyms / alternative names
- Soil-transmitted helminth infections; soil-transmitted helminthiasis (STH) (chen2024globalburdenof pages 1-2)  
- Geohelminthiasis (common in public-health literature; not explicitly evidenced in retrieved corpus)  
- Ascariasis; trichuriasis; hookworm infection (chen2024globalburdenof pages 1-2)

### 1.3 Key identifiers (ontology/classification)
- **MONDO / MeSH / ICD-10 / ICD-11:** Not retrievable from the currently collected full texts using the available tools; therefore **IDs cannot be cited** here. This report is based on aggregated disease-level literature rather than individual EHR-derived definitions. (chen2024globalburdenof pages 1-2)

**Suggested ontology placeholders (to be validated externally):**
- MONDO: “soil-transmitted helminthiasis” (placeholder; verify)  
- MeSH: “Helminthiasis” / “Ascaris lumbricoides” / “Trichuris trichiura” / “Hookworm Infections” (placeholders; verify)

---

## 2. Etiology

### 2.1 Causal factors
- **Infectious cause:** intestinal nematode infection (A. lumbricoides, T. trichiura, hookworms). (chen2024globalburdenof pages 1-2)
- **Environmental mechanism:** exposure to infective eggs/larvae in soil or via fecally contaminated environments; transmission is strongly associated with inadequate sanitation and hygiene. (oyeyemi2023soiltransmittedhelminthiasis(sth) pages 1-2, lebu2023soiltransmittedhelminthsa pages 1-2)

### 2.2 Risk factors (recent quantitative evidence)
**Individual/household behaviors (WASH):**
- In schoolchildren in northwestern Tanzania (2021), not washing hands with water and soap was associated with higher odds of STH infection (**aOR 1.4, 95% CI 1.0–2.1**), while washing hands after using the toilet was protective (**aOR 0.6, 95% CI 0.4–0.9**). (justine2024prevalenceinfectionintensity pages 7-9)

**Sociodemographic:**
- In the same Tanzania study, mother’s occupation as a farmer was associated with increased odds of infection (**aOR 1.2**; the paper reports significance and provides a CI). (justine2024prevalenceinfectionintensity pages 1-2, justine2024prevalenceinfectionintensity pages 7-9)
- In rural Gabon (2020 survey), overall STH prevalence was high (64.8%), with higher prevalence in adults (75.9%) than elders (39.3%) and sex differences for hookworm. (mouandza2024prevalenceandsociodemographic pages 1-2)

**Macro-environment / climate / ecology (spatial modeling):**
- Philippines (national survey; Bayesian geostatistics): male sex increased odds across species (e.g., **hookworm OR 2.142**, 97.5% CrI 1.537–2.998) and higher temperature increased odds for A. lumbricoides and T. trichiura (ORs ~1.15). Vegetation index and higher soil pH were negatively associated with A. lumbricoides risk. (tsheten2024riskmappingand pages 1-2)

### 2.3 Protective factors
- **Hand hygiene** (toilet-associated handwashing) shows protective association in Tanzania (aOR 0.6). (justine2024prevalenceinfectionintensity pages 7-9)
- **Integrated interventions** combining preventive chemotherapy with WASH/education can reduce reinfection in some settings (e.g., narrative evidence from Kenya/Thailand and systematic syntheses; magnitude varies by design and context). (ugwu2024theimpactof pages 12-14, manuel2024soilsurveillancefor pages 15-16)

### 2.4 Gene–environment interactions
Human host genetic susceptibility and explicit GxE interactions were **not** identified in the retrieved 2023–2024 corpus. Mechanistically, immunologic context (prior exposures, age, co-infections) changes infection outcomes and could be viewed as a “host-context × exposure” interaction, but not in a classical genetic sense. (mair2024theadaptiveimmune pages 1-2, mair2024theadaptiveimmune pages 2-3)

---

## 3. Phenotypes (clinical features)

### 3.1 Clinical manifestations (human)
From a GBD-focused clinical summary:
- **Ascaris**: larval migration can cause pulmonary symptoms (“larva migrants’ pneumonia and allergic symptoms”); adult worms can cause gastrointestinal dysfunction and mechanical bowel obstruction. (chen2024globalburdenof pages 1-2)
- **Hookworm**: skin penetration can cause dermatitis; infection can cause respiratory symptoms and anemia. (chen2024globalburdenof pages 1-2)
- **Trichuris**: mechanical damage to intestinal wall tissue, leading to malnutrition/emaciation/fatigue and iron deficiency anemia. (chen2024globalburdenof pages 1-2)

From a 2023 co-infection–focused review:
- Moderate-to-high intensity infections can produce gastrointestinal symptoms including vomiting, diarrhea, abdominal pain, weight loss; chronic infections are associated with micronutrient deficiency/iron deficiency, stunting, cognitive growth retardation, and school absenteeism/poor performance. (lebu2023soiltransmittedhelminthsa pages 1-2)

### 3.2 Quantitative complication statistics (examples)
- Pediatric anemia associations from the 2023 review: children with intestinal helminths had increased odds of anemia (example reported **aOR 8.87**, 95% CI 2.28–34.58); parasite-specific meta-analytic ORs included hookworm **OR 3.3**, Ascaris **OR 1.57**, Trichuris **OR 1.66** (context: co-infection/anemia literature). (lebu2023soiltransmittedhelminthsa pages 7-9)

### 3.3 Age of onset / typical course
STH infections are most prevalent and burdensome in children and adolescents; globally, the highest age-standardized prevalence and DALY rates occur in ages **5–9 years**. (chen2024globalburdenof pages 1-2)

### 3.4 Suggested HPO terms (for knowledge-base mapping; ontology suggestions)
*(Ontology suggestions; require validation against HPO releases)*
- Abdominal pain (HP:0002027)  
- Diarrhea (HP:0002014)  
- Vomiting (HP:0002013)  
- Iron deficiency anemia (HP:0001891)  
- Weight loss (HP:0001824)  
- Malnutrition (HP:0004395)  
- Failure to thrive / Growth delay (HP:0001508)  
- Stunted growth / Short stature (HP:0004322 or related)  
- Eosinophilia (HP:0001880) (common in helminth infection; not directly quantified in retrieved evidence)

### 3.5 Quality of life impact
STH burden is concentrated in resource-poor settings and is linked to reduced quality of life through anemia and nutritional/growth impacts; the burden is reflected in DALYs and in disability sources such as nutritional deficiency and growth retardation. (agrawal2024prevalenceandcorrelates pages 9-10)

---

## 4. Genetic/Molecular Information

### 4.1 Human causal genes / pathogenic variants
STH are **infectious** diseases; there are no single-gene Mendelian “causal genes” in humans. Host genetic susceptibility was not extractable from the retrieved corpus.

### 4.2 Parasite genetic markers relevant to drug resistance (key current question)
**Current marker candidates:** canonical benzimidazole-resistance–associated SNPs in parasite **β-tubulin** at codons **167, 198, 200** (e.g., F167Y, E198A, F200Y) are widely used in veterinary nematodes and are monitored in human STH. (coffeng2024predictingtherisk pages 1-2, ramkhelawan2024singlenucleotidepolymorphisms pages 1-2)

**Recent evidence (2024) suggests uncertainty in humans:**
- A multi-country assay evaluation and application (bioRxiv, Jun 2024) concluded it **“could not provide compelling evidence”** that known β-tubulin SNPs serve as reliable markers of benzimidazole resistance in human STH; associations with drug pressure and individual response were inconsistent. (levecke2024theassessmentof pages 1-6)
- Deep-amplicon sequencing in T. trichiura (Dec 2024) reported **no evidence** linking either of two β-tubulin genes to benzimidazole resistance and suggested resistance markers likely exist outside β-tubulin. (gandasegui2024deepampliconsequencingof pages 1-2)

---

## 5. Environmental Information

Key environmental drivers include sanitation infrastructure, hygiene behaviors, local climate suitability (temperature/rainfall), and soil conditions (e.g., soil pH) that affect egg/larvae survival and transmission intensity. Quantitative associations from spatial models in the Philippines and WASH behaviors in Tanzania support these links. (tsheten2024riskmappingand pages 1-2, justine2024prevalenceinfectionintensity pages 7-9)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high-level)
1. **Exposure** to infective eggs/larvae from fecally contaminated environments. (oyeyemi2023soiltransmittedhelminthiasis(sth) pages 1-2)
2. **Establishment** of intestinal infection (adult worms), with species-specific tissue interactions (intestinal wall damage for Trichuris; blood loss for hookworm; obstruction/migration for Ascaris). (chen2024globalburdenof pages 1-2)
3. **Downstream morbidity** via (a) reduced nutrient absorption/intake, (b) chronic blood loss/iron deficiency, and (c) immune modulation and co-infection effects. (chen2024globalburdenof pages 1-2, lebu2023soiltransmittedhelminthsa pages 1-2)

### 6.2 Immune modulation and co-infections
STH infections can skew toward **type 2 immunity (TH2: IL-4, IL-5, IL-13)** with potential suppression of TH1 responses, affecting susceptibility and outcomes of co-infections (malaria, HIV, TB) in context-dependent ways. (lebu2023soiltransmittedhelminthsa pages 2-3)

### 6.3 Mechanistic insights from model systems (2024)
**Trichuris muris (mouse whipworm; model for human T. trichiura):**
- In laboratory mice, **Th1 vs Th2 polarization is a major determinant** of infection outcome; wild mice show the same general framework but quantitatively different cytokine responses and age-dependent effects, highlighting translational limitations. (mair2024theadaptiveimmune pages 1-2, mair2024theadaptiveimmune pages 2-3)

**Heligmosomoides polygyrus (mouse small-intestinal helminth; immunology/mucus model):**
- Infection induces an **IL-13–dependent** colonic mucus response with goblet cell hyperplasia and increased mucin sialylation, alongside upregulation of goblet-cell products (RELM-β, trefoil factors), and shifts in mucus-associated microbiome (e.g., Ruminococcus gnavus expansion). (mules2024asmallintestinal pages 1-2)

### 6.4 Suggested GO biological process terms (for knowledge-base mapping)
*(Ontology suggestions; require validation)*
- GO:0006954 inflammatory response  
- GO:0042110 T cell activation  
- GO:0042092 type 2 immune response  
- GO:0030574 collagen catabolic process / tissue remodeling (for chronic mucosal effects; not directly evidenced)  
- GO:0007586 digestion / GO:0007584 response to nutrient levels (for malnutrition link; conceptual)

### 6.5 Suggested Cell Ontology (CL) terms
*(Ontology suggestions; require validation)*
- Goblet cell (CL:0000160) (mules2024asmallintestinal pages 1-2)  
- CD4-positive, alpha-beta T cell (CL:0000624) (mair2024theadaptiveimmune pages 1-2)  
- Regulatory T cell (CL:0000815) (conceptually relevant; not directly evidenced in quoted snippets)

---

## 7. Anatomical Structures Affected

### 7.1 Organ-level (UBERON suggestions)
- Intestine (UBERON:0000160), large intestine/colon (UBERON:0001155), small intestine (UBERON:0002108)  
- Lung (UBERON:0002048) (larval migration/pulmonary symptoms) (chen2024globalburdenof pages 1-2)

### 7.2 Tissue/cell-level
- Intestinal epithelium; mucosa; goblet cells (mules2024asmallintestinal pages 1-2)

---

## 8. Temporal Development

- **Onset:** often childhood in endemic areas; burdens peak in school-age children globally (5–9 and 5–19). (chen2024globalburdenof pages 1-2)
- **Course:** typically chronic with frequent reinfection in high-transmission settings; reinfection can occur rapidly after treatment (e.g., Philippines meta-analysis cited pooled prevalence after treatment: 26% at 3 months; 68% at 6 months; 95% at 9 months). (tsheten2024riskmappingand pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (global)
Chen et al. (Infectious Diseases of Poverty; **Oct 2024**; DOI https://doi.org/10.1186/s40249-024-01238-9) reported for 2021:
- **642.72 million cases** and **1.38 million DALYs** globally. (chen2024globalburdenof pages 1-2)
- Global **age-standardized prevalence rate (ASPR)** **8429.89 per 100,000** (95% UI 7697.23–9362.18). (chen2024globalburdenof pages 1-2)
- Highest burden in children **5–9 years**: ASPR **16,263 per 100,000** (95% UI 14,877.06–18,003.49) and DALY rate **40.69 per 100,000** (95% UI 25.98–60.91). (chen2024globalburdenof pages 1-2)

From Chen et al.’s extracted table/figure (1990 vs 2021):
- Global ASPR decreased from **27,728.35/100,000 (1990)** to **8,429.89/100,000 (2021)** and DALY rate from **103.83/100,000 (1990)** to **18.84/100,000 (2021)**. (chen2024globalburdenof media e4718bac, chen2024globalburdenof media 2a6eff33)

### 9.2 Socioeconomic gradient
STH prevalence and DALYs are strongly negatively correlated with socio-demographic index (SDI) at regional level (e.g., prevalence r ≈ −0.8807; DALYs r ≈ −0.9069). (chen2024globalburdenof pages 1-2, chen2024globalburdenof pages 7-8)

---

## 10. Diagnostics

### 10.1 Stool microscopy (programmatic standard)
WHO’s 2030 roadmap retains **Kato–Katz** as the reference method to detect and quantify infection intensity for STH programs, with emphasis on moderate-to-heavy intensity (M&HI) infections. (stuyver2021theroleof pages 1-2)

**Performance (examples from 2021 diagnostic viewpoint):**
- Kato–Katz sensitivity for **any intensity** infection (approximate estimates): Ascaris **71.9%**, Trichuris **88.1%**, hookworm **72.6%**; for **low-intensity** infection: Ascaris **55.6%**, Trichuris **79.6%**, hookworm **69.4%**. (stuyver2021theroleof pages 3-5)

### 10.2 Molecular stool diagnostics (qPCR)
qPCR can achieve higher accuracy, particularly for low-intensity infections and post-MDA surveillance; approximate sensitivities cited include Ascaris **90.0%**, Trichuris **94.7%**, hookworm **91.9%** (and improved low-intensity performance). Implementation barriers include cost, extraction workload, time-to-result, and standardization needs. (stuyver2021theroleof pages 3-5)

### 10.3 Environmental surveillance (soil qPCR; 2024 development)
A 2024 PLOS NTD study developed a **20 g soil** DNA extraction + qPCR method for STH monitoring (Kenya/Benin/India), reporting:
- Analytical detection limits: **A. lumbricoides 0.25 eggs/g soil**, **hookworm 0.1 eggs/g**, **T. trichiura 0.5 eggs/g**. (manuel2024soilsurveillancefor pages 8-10)
- Soil qPCR prevalence across sites: **31% A. lumbricoides**, **3% T. trichiura**, **13% any hookworm**; and household soil detection was strongly associated with household infection by the same species. (manuel2024soilsurveillancefor pages 1-2)

### 10.4 Serology (2024 scoping review)
A 2024 scoping review found substantial research activity but limited operational readiness:
- No commercial serological tests identified for **Trichuris** or **hookworms**; for **Ascaris**, at least seven ELISAs are on the market. (roose2024serologicaldiagnosisof pages 1-2)
- Reported sensitivities and specificities in the literature vary widely (both 0–100%), reflecting heterogeneity in antigens, isotypes, and reference standards; lack of a true gold standard complicates validation. (roose2024serologicaldiagnosisof pages 11-12)

**Suggested diagnostic ontology mappings (placeholders):**
- LOINC/SNOMED: stool ova & parasite exam; fecal egg count (Kato–Katz); qPCR for species DNA (validate via LOINC/SNOMED catalogs).

---

## 11. Outcome / Prognosis

Population-level prognosis is dominated by **morbidity** (anemia, malnutrition, growth/cognitive impacts) rather than high mortality; overall global burden is captured as DALYs and is declining over time, but remains substantial in low-SDI settings and in children. (chen2024globalburdenof pages 1-2, lebu2023soiltransmittedhelminthsa pages 1-2)

---

## 12. Treatment

### 12.1 Current standard of care (programmatic)
Preventive chemotherapy (mass or targeted deworming) with benzimidazoles is the mainstay of control in endemic countries. (keiser2023presentdrugsand pages 2-3)

**Key agents (CHEBI suggestions):**
- Albendazole; mebendazole; ivermectin; moxidectin; oxantel pamoate; pyrantel pamoate; emodepside.

### 12.2 Efficacy of standard single-dose benzimidazoles (recent evidence)
A consistent 2023–2024 finding is that **single-dose benzimidazoles are highly effective for Ascaris** but **suboptimal for Trichuris**.
- Peru (AJTMH, **Jul 2024**, https://doi.org/10.4269/ajtmh.23-0497): albendazole had **Ascaris CR 99.6%** and **ERR 99.8%**, but Trichuris CR was low (e.g., **27.1%** in the study context). (curico2024efficacyofsingledose pages 6-7)
- Therapeutics review (Frontiers, **Nov 2023**, https://doi.org/10.3389/fitd.2023.1282725): single-dose albendazole and mebendazole had low Trichuris cure/ERR, while remaining high for Ascaris; mebendazole was weaker against hookworm than albendazole in cited estimates. (keiser2023presentdrugsand pages 2-3)

### 12.3 Combination therapy and optimized regimens (key 2024 data)
- Bayesian reanalysis incorporating diagnostic error (Scientific Reports, **Oct 2024**, https://doi.org/10.1038/s41598-024-73164-7): for Trichuris, modeled single-dose albendazole had extremely low CR/ERR, while combinations performed better; the best regimen was **albendazole + pyrantel + oxantel** (**CR 79%**, **ERR 91%**). (grolimund2024modelingtransmissionmechanism pages 4-5)
- Peru cohort: among persistent Trichuris infections, **albendazole + ivermectin** achieved **CR 75.2%** and reduced reinfection compared with albendazole alone. (curico2024efficacyofsingledose pages 6-7)
- Ivermectin MDA meta-analysis (IDoP, **Feb 2024**, https://doi.org/10.1186/s40249-024-01185-5): Trichuris prevalence reduction **49.93%** (ivermectin alone) vs **89.40%** when **albendazole was added**. (le2024effectivenessofivermectin pages 1-2)

### 12.4 Resistance monitoring and expert interpretation
- A key expert concern is that reliance on benzimidazoles creates selection pressure analogous to livestock settings; modeling suggests resistance could emerge within a decade depending on strategy and monitoring. (coffeng2024predictingtherisk pages 1-2)
- However, multiple 2024 molecular studies did not find compelling evidence that canonical β-tubulin SNPs alone explain reduced benzimidazole efficacy in human STH, highlighting the need for broader genomic/phenotypic surveillance. (levecke2024theassessmentof pages 1-6, gandasegui2024deepampliconsequencingof pages 1-2)

### 12.5 Clinical trials (selected; real-world pipeline)
- **NCT04700423** (Completed; results posted **Dec 2024**): Phase 2/3 non-inferiority trial in adolescents (12–19y) on Pemba Island comparing **moxidectin+albendazole** vs **ivermectin+albendazole** for Trichuris (primary endpoint: ERR at 14–21 days by Kato–Katz; also diagnostic comparisons incl. PCR). URL: https://clinicaltrials.gov/study/NCT04700423 (NCT04700423 chunk 1)
- **NCT06800248** (Not yet recruiting; start **Apr 2026**): Phase 3 trial comparing **emodepside (single 15 mg)** vs **mebendazole (100 mg BID ×3 days)** for Trichuris in participants ≥12 years. URL: https://clinicaltrials.gov/study/NCT06800248 (NCT06800248 chunk 1)

### 12.6 Suggested MAXO terms (treatment action mapping; validate)
- Preventive chemotherapy / mass drug administration (MDA)  
- Anthelmintic therapy  
- Combination anthelmintic therapy  
- Environmental surveillance (soil qPCR monitoring) as a public health action

---

## 13. Prevention

### 13.1 Primary prevention
- WASH improvements (sanitation, clean water, hygiene education) reduce exposure and reinfection risk; empirical evidence shows behavioral and infrastructure factors drive residual transmission. (justine2024prevalenceinfectionintensity pages 7-9, oyeyemi2023soiltransmittedhelminthiasis(sth) pages 1-2)

### 13.2 Secondary prevention (screening / monitoring)
- WHO 2030 program milestone framework emphasizes reducing **moderate-to-heavy intensity prevalence in children to <2%** and using diagnostics to guide decisions to scale down PC. (stuyver2021theroleof pages 1-2, ugwu2024theimpactof pages 1-2)
- Environmental surveillance with soil qPCR is an emerging strategy to complement stool-based surveillance where stool collection is logistically difficult and stigmatized. (manuel2024soilsurveillancefor pages 1-2)

### 13.3 Tertiary prevention
- Regular deworming to prevent anemia and nutritional sequelae; integration with anemia control (e.g., iron/folate programs) is suggested in recent reviews. (agrawal2024prevalenceandcorrelates pages 9-10)

---

## 14. Other Species / Natural Disease

A One-Health framing is increasingly emphasized because of the environmental reservoir and the extensive experience of anthelmintic resistance in livestock nematodes. Reviews note zoonotic/canine soil-transmitted nematodes (e.g., Ancylostoma ceylanicum, Toxocara spp.) can cause human disease manifestations, though these are not the core WHO STH triad. (ng’etich2024anthelminticresistancein pages 1-2)

---

## 15. Model Organisms

### 15.1 Core model systems used for STH biology and immunology
- **Trichuris muris in mice**: established model for T. trichiura; highlights Th1/Th2 polarization as determinant of outcome; wild-versus-lab comparisons underscore ecological and age-dependent differences relevant for translation to human chronic infection. (mair2024theadaptiveimmune pages 2-3, mair2024theadaptiveimmune pages 1-2)
- **Heligmosomoides polygyrus in mice**: widely used to study type-2 immunity, mucus barrier remodeling, and helminth–microbiome interactions; IL-13 dependence demonstrated for mucus alterations. (mules2024asmallintestinal pages 1-2)

### 15.2 Model limitations (expert analysis)
Laboratory mice are immunologically “naïve” relative to naturally exposed hosts; wild mouse data show quantitatively different cytokine responses and infection-history complexity, cautioning against direct extrapolation of magnitude and kinetics of immune correlates from lab models to human endemic settings. (mair2024theadaptiveimmune pages 1-2, mair2024theadaptiveimmune pages 11-12)

---

# High-value evidence summary table

| Topic | Key data | Source (with DOI/URL and year) | Evidence type |
|---|---|---|---|
| Global burden: cases/DALYs (2021) | Estimated **642.72 million cases** and **1.38 million DALYs** globally in 2021; burden highest in tropical/subtropical regions and inversely correlated with SDI. (chen2024globalburdenof pages 1-2) | Chen et al., *Infectious Diseases of Poverty* (2024), doi:10.1186/s40249-024-01238-9, https://doi.org/10.1186/s40249-024-01238-9 | GBD 2021 modeling study |
| Global burden: ASPR and DALY rate (1990 vs 2021) | Global **ASPR** declined from **27,728.35/100,000 (1990)** to **8,429.89/100,000 (2021)**; global **age-standardized DALY rate** declined from **103.83/100,000 (1990)** to **18.84/100,000 (2021)**. (chen2024globalburdenof media e4718bac, chen2024globalburdenof media 2a6eff33) | Chen et al., *Infectious Diseases of Poverty* (2024), doi:10.1186/s40249-024-01238-9, https://doi.org/10.1186/s40249-024-01238-9 | GBD 2021 modeling study / figure-table extraction |
| Key age group (5–9 years) | Children **5–9 years** had the highest burden: **ASPR 16,263/100,000** (95% UI 14,877.06–18,003.49) and **ASR of DALYs 40.69/100,000** (95% UI 25.98–60.91). (chen2024globalburdenof pages 1-2, chen2024globalburdenof pages 5-7) | Chen et al., *Infectious Diseases of Poverty* (2024), doi:10.1186/s40249-024-01238-9, https://doi.org/10.1186/s40249-024-01238-9 | GBD 2021 modeling study |
| Diagnostics: Kato-Katz performance | Kato-Katz remains WHO reference for 2030 targets; sensitivity is lower for low-intensity infection. Approximate sensitivities for **any intensity**: **Ascaris 71.9%**, **Trichuris 88.1%**, **hookworm 72.6%**; for **low intensity**: **Ascaris 55.6%**, **Trichuris 79.6%**, **hookworm 69.4%**. For moderate/heavy infections, Kato-Katz “meets” required performance. (stuyver2021theroleof pages 3-5, stuyver2021theroleof pages 1-2, stuyver2021theroleof pages 2-3) | Stuyver & Levecke, *PLOS Neglected Tropical Diseases* (2021), doi:10.1371/journal.pntd.0009422, https://doi.org/10.1371/journal.pntd.0009422 | Diagnostic viewpoint/review |
| Diagnostics: qPCR performance | qPCR achieves higher data accuracy for low-intensity and post-MDA settings; approximate sensitivities: **Ascaris 90.0%**, **Trichuris 94.7%**, **hookworm 91.9%**; low-intensity **Ascaris ~86.2%**. qPCR adoption limited by cost, extraction burden, and standardization gaps. (stuyver2021theroleof pages 3-5, grolimund2024modelingtransmissionmechanism pages 8-9) | Stuyver & Levecke, *PLOS Neglected Tropical Diseases* (2021), doi:10.1371/journal.pntd.0009422, https://doi.org/10.1371/journal.pntd.0009422 | Diagnostic viewpoint/review |
| Environmental diagnostics: soil qPCR LOD | Soil qPCR detection limits in 20 g soil: **A. lumbricoides 0.25 EPG**, **hookworm 0.1 EPG**, **T. trichiura 0.5 EPG**; qPCR and ddPCR showed good agreement (**78–85%**, species-dependent). (manuel2024soilsurveillancefor pages 15-16, manuel2024soilsurveillancefor pages 8-10) | Manuel et al., *PLOS Neglected Tropical Diseases* (2024), doi:10.1371/journal.pntd.0012416, https://doi.org/10.1371/journal.pntd.0012416 | Method-development/field validation study |
| Environmental diagnostics: soil prevalence | Across **478 soil** and **669 stool** samples from **322 households**, soil qPCR prevalence was **31% A. lumbricoides**, **3% T. trichiura**, **13% any hookworm**; STH detection in household soil was strongly associated with household infection by the same species. (manuel2024soilsurveillancefor pages 8-10, manuel2024soilsurveillancefor pages 1-2) | Manuel et al., *PLOS Neglected Tropical Diseases* (2024), doi:10.1371/journal.pntd.0012416, https://doi.org/10.1371/journal.pntd.0012416 | Field surveillance study |
| Treatment efficacy: single-dose albendazole for Trichuris | Single-dose albendazole is consistently weak for **T. trichiura**. Pooled review estimates: **ERR 74.27%** (95% CI 72.95–75.69%); model-based estimates in one 2024 synthesis were far lower (**CR 1%**, **ERR 2–20%**, depending on model framing). In Peru, current-study **CR 27.1%** and **ERR 29.8%** for Trichuris. (bekele2024efficacyofalbendazole pages 10-14, grolimund2024modelingtransmissionmechanism pages 4-5, curico2024efficacyofsingledose pages 6-7, curico2024efficacyofsingledose pages 5-6) | Bekele et al., *J Epidemiol Glob Health* (2024), doi:10.1007/s44197-024-00231-7, https://doi.org/10.1007/s44197-024-00231-7; Grolimund et al., *Scientific Reports* (2024), doi:10.1038/s41598-024-73164-7, https://doi.org/10.1038/s41598-024-73164-7; Curico et al., *Am J Trop Med Hyg* (2024), doi:10.4269/ajtmh.23-0497, https://doi.org/10.4269/ajtmh.23-0497 | Systematic review/meta-analysis; Bayesian reanalysis; prospective cohort |
| Treatment efficacy: combinations for Trichuris | Combination therapy improves Trichuris outcomes. **Albendazole + ivermectin**: pooled prevalence reduction in MDA studies **89.40%** (95% CI 73.66–95.73); Peru persistent-infection cohort **CR 75.2%**. **Albendazole + oxantel pamoate**: modeled **CR ~63%**, **ERR 90–97%**. **Albendazole + pyrantel + oxantel** had highest modeled efficacy: **CR 79%**, **ERR 91%**. (curico2024efficacyofsingledose pages 6-7, grolimund2024modelingtransmissionmechanism pages 5-6, le2024effectivenessofivermectin pages 1-2) | Curico et al., *Am J Trop Med Hyg* (2024), doi:10.4269/ajtmh.23-0497, https://doi.org/10.4269/ajtmh.23-0497; Grolimund et al., *Scientific Reports* (2024), doi:10.1038/s41598-024-73164-7, https://doi.org/10.1038/s41598-024-73164-7; Le et al., *Infectious Diseases of Poverty* (2024), doi:10.1186/s40249-024-01185-5, https://doi.org/10.1186/s40249-024-01185-5 | Cohort study; Bayesian reanalysis; systematic review/meta-analysis |
| Resistance markers: canonical loci | Putative benzimidazole resistance markers are **β-tubulin codons 167, 198, and 200** (e.g., F167Y, E198A/K/V, F200Y), established in veterinary helminths and monitored in human STH. (coffeng2024predictingtherisk pages 1-2, ramkhelawan2024singlenucleotidepolymorphisms pages 1-2, levecke2024theassessmentof pages 6-9) | Coffeng et al., *Nature Communications* (2024), doi:10.1038/s41467-024-45027-2, https://doi.org/10.1038/s41467-024-45027-2; Ramkhelawan et al., *Frontiers in Tropical Diseases* (2024), doi:10.3389/fitd.2023.1303873, https://doi.org/10.3389/fitd.2023.1303873 | Modeling study; systematic review |
| Resistance marker status in human STH | Evidence in human STH remains **inconclusive**. A 2024 pyrosequencing study found mutant codon-200 SNPs in about **half of analyzed Trichuris samples**, but **no consistent association** with drug pressure, treatment response, or sampling time, and concluded there was **no compelling evidence** that known β-tubulin SNPs currently explain resistance in human STH. Deep sequencing of *T. trichiura* likewise found **no evidence** linking either of two β-tubulin genes to benzimidazole resistance. (levecke2024theassessmentof pages 1-6, gandasegui2024deepampliconsequencingof pages 1-2) | Levecke et al., *bioRxiv* (2024), doi:10.1101/2024.06.04.597280, https://doi.org/10.1101/2024.06.04.597280; Gandasegui et al., *Int J Parasitol Drugs Drug Resist* (2024), doi:10.1016/j.ijpddr.2024.100570, https://doi.org/10.1016/j.ijpddr.2024.100570 | Preprint molecular surveillance study; deep-amplicon sequencing study |
| Implementation: Nigeria coverage gap | WHO/ESPEN program benchmark for effective preventive chemotherapy is **≥75% coverage**. In Nigeria (2021), PC reached schoolchildren in **177/774 implementation units (22.9%)**; **effective coverage** was achieved in **149/774 units (19.3%)**, far below target. Coverage by endemicity: **7.8% low**, **22.2% moderate**, **49.2% high**. (oyeyemi2023soiltransmittedhelminthiasis(sth) pages 1-2, oyeyemi2023soiltransmittedhelminthiasis(sth) pages 2-3) | Oyeyemi & Okunlola, *Scientific Reports* (2023), doi:10.1038/s41598-023-37402-8, https://doi.org/10.1038/s41598-023-37402-8 | National program analysis using WHO/ESPEN data |
| Implementation: Geshiyaro cMDA vs sMDA | In Wolaita, Ethiopia, **community-wide MDA (cMDA)** + WaSH outperformed **school-based MDA (sMDA)**. Prevalence fell from **27.4% to 5.5%** in Arm 1 and **23.0% to 4.5%** in Arm 2, versus **49.6% to 26.1%** in sMDA control Arm 3. Relative reductions: **80.1%**, **82.5%**, and **46.9%**, respectively. (mengistu2024soiltransmittedhelminth(sth) pages 1-2) | Mengistu et al., *Parasites & Vectors* (2024), doi:10.1186/s13071-024-06422-2, https://doi.org/10.1186/s13071-024-06422-2 | Longitudinal program evaluation / implementation study |


*Table: This table condenses recent high-value evidence on soil-transmitted helminthiases across burden, diagnostics, treatment, resistance, and implementation. It is designed as a quick reference for knowledge-base curation and evidence synthesis.*

---

## Appendix: Real-world implementation evidence (selected)

- **Nigeria PC coverage gap (2021; Scientific Reports Jun 2023):** Effective PC coverage benchmark is ≥75%; in 2021, effective coverage was achieved in **19.3%** of implementation units, with PC delivered to schoolchildren in 22.9% of units—indicating substantial programmatic gaps. https://doi.org/10.1038/s41598-023-37402-8 (oyeyemi2023soiltransmittedhelminthiasis(sth) pages 2-3)

- **Ethiopia Geshiyaro project (Parasites & Vectors Aug 2024):** Community-wide MDA (cMDA) + WaSH produced larger prevalence reductions than school-based MDA (sMDA): Arm 2 prevalence **23% → 4.5%** (2020→2023) vs sMDA control **49.6% → 26.1%** (2021→2023). https://doi.org/10.1186/s13071-024-06422-2 (mengistu2024soiltransmittedhelminth(sth) pages 1-2)

---

## Notes on citation requirements (PMID)
PMIDs were not available in the retrieved text snippets for most included sources. Where PubMed indexing is required, use the DOIs/URLs provided (which are authoritative) to retrieve PMIDs via PubMed/NCBI. (chen2024globalburdenof pages 1-2, roose2024serologicaldiagnosisof pages 1-2)

References

1. (chen2024globalburdenof pages 1-2): Jin Chen, Yanfeng Gong, Qin Chen, Shizhu Li, and Yibiao Zhou. Global burden of soil-transmitted helminth infections, 1990–2021. Infectious Diseases of Poverty, Oct 2024. URL: https://doi.org/10.1186/s40249-024-01238-9, doi:10.1186/s40249-024-01238-9. This article has 93 citations and is from a domain leading peer-reviewed journal.

2. (chen2024globalburdenof media e4718bac): Jin Chen, Yanfeng Gong, Qin Chen, Shizhu Li, and Yibiao Zhou. Global burden of soil-transmitted helminth infections, 1990–2021. Infectious Diseases of Poverty, Oct 2024. URL: https://doi.org/10.1186/s40249-024-01238-9, doi:10.1186/s40249-024-01238-9. This article has 93 citations and is from a domain leading peer-reviewed journal.

3. (keiser2023presentdrugsand pages 4-5): Jennifer Keiser. Present drugs and future perspectives in treating soil-transmitted helminthiasis. Frontiers in Tropical Diseases, Nov 2023. URL: https://doi.org/10.3389/fitd.2023.1282725, doi:10.3389/fitd.2023.1282725. This article has 12 citations.

4. (emerson2024needfora pages 6-7): Paul M. Emerson, Darin Evans, Matthew C. Freeman, Christy Hanson, Khumbo Kalua, Jennifer Keiser, Alejandro Krolewiecki, Lynn Leonard, Bruno Levecke, Sultani Matendechero, Arianna Rubin Means, Antonio Montresor, Denise Mupfasoni, Rachel L. Pullan, Lisa A. Rotondo, Mariana Stephens, Kristin M. Sullivan, Judd L. Walson, Tijana Williams, and Jürg Utzinger. Need for a paradigm shift in soil-transmitted helminthiasis control: targeting the right people, in the right place, and with the right drug(s). PLOS Neglected Tropical Diseases, 18:e0012521, Oct 2024. URL: https://doi.org/10.1371/journal.pntd.0012521, doi:10.1371/journal.pntd.0012521. This article has 5 citations and is from a domain leading peer-reviewed journal.

5. (manuel2024soilsurveillancefor pages 1-2): Malathi Manuel, Heather K. Amato, Nils Pilotte, Benard Chieng, Sylvie B. Araka, Joël Edoux Eric Siko, Michael Harris, Maya L. Nadimpalli, Venkateshprabhu Janagaraj, Parfait Houngbegnon, Rajeshkumar Rajendiran, Joel Thamburaj, Saravanakumar Puthupalayam Kaliappan, Allison R. Sirois, Gretchen Walch, William E. Oswald, Kristjana H. Asbjornsdottir, Sean R. Galagan, Judd L. Walson, Steven A. Williams, Adrian J. F. Luty, Sammy M. Njenga, Moudachirou Ibikounlé, Sitara S. R. Ajjampur, and Amy J. Pickering. Soil surveillance for monitoring soil-transmitted helminths: method development and field testing in three countries. PLOS Neglected Tropical Diseases, 18:e0012416, Sep 2024. URL: https://doi.org/10.1371/journal.pntd.0012416, doi:10.1371/journal.pntd.0012416. This article has 10 citations and is from a domain leading peer-reviewed journal.

6. (keiser2023presentdrugsand pages 2-3): Jennifer Keiser. Present drugs and future perspectives in treating soil-transmitted helminthiasis. Frontiers in Tropical Diseases, Nov 2023. URL: https://doi.org/10.3389/fitd.2023.1282725, doi:10.3389/fitd.2023.1282725. This article has 12 citations.

7. (oyeyemi2023soiltransmittedhelminthiasis(sth) pages 1-2): Oyetunde T. Oyeyemi and Oluyemi A. Okunlola. Soil-transmitted helminthiasis (sth) endemicity and performance of preventive chemotherapy intervention programme in nigeria (in year 2021). Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-37402-8, doi:10.1038/s41598-023-37402-8. This article has 9 citations and is from a peer-reviewed journal.

8. (lebu2023soiltransmittedhelminthsa pages 1-2): Sarah Lebu, Winnie Kibone, Chimdi C. Muoghalu, Stephen Ochaya, Aaron Salzberg, Felix Bongomin, and Musa Manga. Soil-transmitted helminths: a critical review of the impact of co-infections and implications for control and elimination. PLOS Neglected Tropical Diseases, 17:e0011496, Aug 2023. URL: https://doi.org/10.1371/journal.pntd.0011496, doi:10.1371/journal.pntd.0011496. This article has 58 citations and is from a domain leading peer-reviewed journal.

9. (justine2024prevalenceinfectionintensity pages 7-9): Nyanda C. Justine, Jeffer Bhuko, Sarah L. Rubagumya, Namanya S. Basinda, Deodatus M. Ruganuza, Maria M. Zinga, Matthieu Briet, Vyacheslav R. Misko, Filip Legein, Hussein Mohamed, Vivian Mushi, Donath S. Tarimo, Humphrey D. Mazigo, and Wim De Malsche. Prevalence, infection intensity, and risk factors for soil-transmitted helminth infections among school children in northwestern tanzania. Pathogens, 13:627, Jul 2024. URL: https://doi.org/10.3390/pathogens13080627, doi:10.3390/pathogens13080627. This article has 8 citations.

10. (justine2024prevalenceinfectionintensity pages 1-2): Nyanda C. Justine, Jeffer Bhuko, Sarah L. Rubagumya, Namanya S. Basinda, Deodatus M. Ruganuza, Maria M. Zinga, Matthieu Briet, Vyacheslav R. Misko, Filip Legein, Hussein Mohamed, Vivian Mushi, Donath S. Tarimo, Humphrey D. Mazigo, and Wim De Malsche. Prevalence, infection intensity, and risk factors for soil-transmitted helminth infections among school children in northwestern tanzania. Pathogens, 13:627, Jul 2024. URL: https://doi.org/10.3390/pathogens13080627, doi:10.3390/pathogens13080627. This article has 8 citations.

11. (mouandza2024prevalenceandsociodemographic pages 1-2): Reinne Moutongo Mouandza, Jean Romain Mourou Mbina, Bridy Moutombi Ditombi, Joyce Coella Mihindou, Dimitri Ardrin Moussavou Mabicka, Christian Mayandza, Noe Patrick Mbondoukwe, Bedrich Pongui Ngondza, Luccheri Ndong Akomezoghe, Denise Patricia Mawili Mboumba, and Marielle Karine Bouyou Akotet. Prevalence and sociodemographic risk factors of soil-transmitted helminths in rural communities living in endemic foci of onchocerciasis in southern gabon. Pathogens, 13:967, Nov 2024. URL: https://doi.org/10.3390/pathogens13110967, doi:10.3390/pathogens13110967. This article has 3 citations.

12. (tsheten2024riskmappingand pages 1-2): Tsheten Tsheten, Kefyalew Addis Alene, Angela Cadavid Restrepo, Matthew Kelly, Colleen Lau, Archie C.A. Clements, Darren J. Gray, Chona Daga, Vanessa Joy Mapalo, Fe Esperanza Espino, and Kinley Wangdi. Risk mapping and socio-ecological drivers of soil-transmitted helminth infections in the philippines: a spatial modelling study. The Lancet Regional Health - Western Pacific, 43:100974, Feb 2024. URL: https://doi.org/10.1016/j.lanwpc.2023.100974, doi:10.1016/j.lanwpc.2023.100974. This article has 18 citations.

13. (ugwu2024theimpactof pages 12-14): Sommy C. Ugwu, Michael O. Muoka, Clara MacLeod, Sarah Bick, Oliver Cumming, and Laura Braun. The impact of community based interventions for the prevention and control of soil-transmitted helminths: a systematic review and meta-analysis. PLOS Global Public Health, 4:e0003717, Oct 2024. URL: https://doi.org/10.1371/journal.pgph.0003717, doi:10.1371/journal.pgph.0003717. This article has 6 citations and is from a peer-reviewed journal.

14. (manuel2024soilsurveillancefor pages 15-16): Malathi Manuel, Heather K. Amato, Nils Pilotte, Benard Chieng, Sylvie B. Araka, Joël Edoux Eric Siko, Michael Harris, Maya L. Nadimpalli, Venkateshprabhu Janagaraj, Parfait Houngbegnon, Rajeshkumar Rajendiran, Joel Thamburaj, Saravanakumar Puthupalayam Kaliappan, Allison R. Sirois, Gretchen Walch, William E. Oswald, Kristjana H. Asbjornsdottir, Sean R. Galagan, Judd L. Walson, Steven A. Williams, Adrian J. F. Luty, Sammy M. Njenga, Moudachirou Ibikounlé, Sitara S. R. Ajjampur, and Amy J. Pickering. Soil surveillance for monitoring soil-transmitted helminths: method development and field testing in three countries. PLOS Neglected Tropical Diseases, 18:e0012416, Sep 2024. URL: https://doi.org/10.1371/journal.pntd.0012416, doi:10.1371/journal.pntd.0012416. This article has 10 citations and is from a domain leading peer-reviewed journal.

15. (mair2024theadaptiveimmune pages 1-2): Iris Mair, Jonathan Fenn, Andrew Wolfenden, Ann E. Lowe, Alex Bennett, Andrew Muir, Jacob Thompson, Olive Dieumerci, Larisa Logunova, Susanne Shultz, Janette E. Bradley, and Kathryn J. Else. The adaptive immune response to trichuris in wild versus laboratory mice: an established model system in context. PLOS Pathogens, 20:e1012119, Apr 2024. URL: https://doi.org/10.1371/journal.ppat.1012119, doi:10.1371/journal.ppat.1012119. This article has 5 citations and is from a highest quality peer-reviewed journal.

16. (mair2024theadaptiveimmune pages 2-3): Iris Mair, Jonathan Fenn, Andrew Wolfenden, Ann E. Lowe, Alex Bennett, Andrew Muir, Jacob Thompson, Olive Dieumerci, Larisa Logunova, Susanne Shultz, Janette E. Bradley, and Kathryn J. Else. The adaptive immune response to trichuris in wild versus laboratory mice: an established model system in context. PLOS Pathogens, 20:e1012119, Apr 2024. URL: https://doi.org/10.1371/journal.ppat.1012119, doi:10.1371/journal.ppat.1012119. This article has 5 citations and is from a highest quality peer-reviewed journal.

17. (lebu2023soiltransmittedhelminthsa pages 7-9): Sarah Lebu, Winnie Kibone, Chimdi C. Muoghalu, Stephen Ochaya, Aaron Salzberg, Felix Bongomin, and Musa Manga. Soil-transmitted helminths: a critical review of the impact of co-infections and implications for control and elimination. PLOS Neglected Tropical Diseases, 17:e0011496, Aug 2023. URL: https://doi.org/10.1371/journal.pntd.0011496, doi:10.1371/journal.pntd.0011496. This article has 58 citations and is from a domain leading peer-reviewed journal.

18. (agrawal2024prevalenceandcorrelates pages 9-10): Ritik Agrawal, Sweta Pattnaik, Jaya Singh Kshatri, Srikanta Kanungo, Nityananda Mandal, Subrata Kumar Palo, and Sanghamitra Pati. Prevalence and correlates of soil-transmitted helminths in schoolchildren aged 5 to 18 years in low- and middle-income countries: a systematic review and meta-analysis. Frontiers in Public Health, Mar 2024. URL: https://doi.org/10.3389/fpubh.2024.1283054, doi:10.3389/fpubh.2024.1283054. This article has 36 citations.

19. (coffeng2024predictingtherisk pages 1-2): Luc Coffeng, Wilma Stolk, and Sake J. de Vlas. Predicting the risk and speed of drug resistance emerging in soil-transmitted helminths during preventive chemotherapy. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45027-2, doi:10.1038/s41467-024-45027-2. This article has 33 citations and is from a highest quality peer-reviewed journal.

20. (ramkhelawan2024singlenucleotidepolymorphisms pages 1-2): Teniel Ramkhelawan, Pragalathan Naidoo, and Zilungile L. Mkhize-Kwitshana. Single nucleotide polymorphisms in the β-tubulin gene family of ascaris lumbricoides and their potential role in benzimidazole resistance: a systematic review. Frontiers in Tropical Diseases, Jan 2024. URL: https://doi.org/10.3389/fitd.2023.1303873, doi:10.3389/fitd.2023.1303873. This article has 2 citations.

21. (levecke2024theassessmentof pages 1-6): Bruno Levecke, Nour Rashwan, Piet Cools, Marco Albonico, Shaali M Ame, Mio Ayana, Daniel Dana, Jennifer Keiser, Antonio Montresor, Zeleke Mekonnen, Sara Roose, Somphou Sayasone, Jozef Vercruysse, Jaco J Verweij, Johnny Vlaminck, and Roger Prichard. The assessment of single nucleotide polymorphisms in the ß-tubulin genes in human soil-transmitted helminths exposed to different pressure with benzimidazole drugs. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2024.06.04.597280, doi:10.1101/2024.06.04.597280. This article has 1 citations.

22. (gandasegui2024deepampliconsequencingof pages 1-2): Javier Gandasegui, Berta Grau-Pujol, Valdemiro Novela, Osvaldo Muchisse, Maria Cambra-Pellejà, Anélsio Cossa, José Carlos Jamine, Charfudin Sacoor, Eric A.T. Brienen, Francesc Catala-Moll, Lisette van Lieshout, María Martínez-Valladares, Roger Paredes, José Muñoz, and Stephen R. Doyle. Deep-amplicon sequencing of the complete beta-tubulin gene in trichuris trichiura before and after albendazole treatment. International Journal for Parasitology: Drugs and Drug Resistance, 26:100570, Dec 2024. URL: https://doi.org/10.1016/j.ijpddr.2024.100570, doi:10.1016/j.ijpddr.2024.100570. This article has 4 citations.

23. (lebu2023soiltransmittedhelminthsa pages 2-3): Sarah Lebu, Winnie Kibone, Chimdi C. Muoghalu, Stephen Ochaya, Aaron Salzberg, Felix Bongomin, and Musa Manga. Soil-transmitted helminths: a critical review of the impact of co-infections and implications for control and elimination. PLOS Neglected Tropical Diseases, 17:e0011496, Aug 2023. URL: https://doi.org/10.1371/journal.pntd.0011496, doi:10.1371/journal.pntd.0011496. This article has 58 citations and is from a domain leading peer-reviewed journal.

24. (mules2024asmallintestinal pages 1-2): Thomas C. Mules, Francesco Vacca, Alissa Cait, Bibek Yumnam, Alfonso Schmidt, Brittany Lavender, Kate Maclean, Sophia-Louise Noble, Olivier Gasser, Mali Camberis, Graham Le Gros, and Stephen Inns. A small intestinal helminth infection alters colonic mucus and shapes the colonic mucus microbiome. International Journal of Molecular Sciences, 25:12015, Nov 2024. URL: https://doi.org/10.3390/ijms252212015, doi:10.3390/ijms252212015. This article has 7 citations.

25. (chen2024globalburdenof media 2a6eff33): Jin Chen, Yanfeng Gong, Qin Chen, Shizhu Li, and Yibiao Zhou. Global burden of soil-transmitted helminth infections, 1990–2021. Infectious Diseases of Poverty, Oct 2024. URL: https://doi.org/10.1186/s40249-024-01238-9, doi:10.1186/s40249-024-01238-9. This article has 93 citations and is from a domain leading peer-reviewed journal.

26. (chen2024globalburdenof pages 7-8): Jin Chen, Yanfeng Gong, Qin Chen, Shizhu Li, and Yibiao Zhou. Global burden of soil-transmitted helminth infections, 1990–2021. Infectious Diseases of Poverty, Oct 2024. URL: https://doi.org/10.1186/s40249-024-01238-9, doi:10.1186/s40249-024-01238-9. This article has 93 citations and is from a domain leading peer-reviewed journal.

27. (stuyver2021theroleof pages 1-2): Lieven J. Stuyver and Bruno Levecke. The role of diagnostic technologies to measure progress toward who 2030 targets for soil-transmitted helminth control programs. PLOS Neglected Tropical Diseases, 15:e0009422, Jun 2021. URL: https://doi.org/10.1371/journal.pntd.0009422, doi:10.1371/journal.pntd.0009422. This article has 33 citations and is from a domain leading peer-reviewed journal.

28. (stuyver2021theroleof pages 3-5): Lieven J. Stuyver and Bruno Levecke. The role of diagnostic technologies to measure progress toward who 2030 targets for soil-transmitted helminth control programs. PLOS Neglected Tropical Diseases, 15:e0009422, Jun 2021. URL: https://doi.org/10.1371/journal.pntd.0009422, doi:10.1371/journal.pntd.0009422. This article has 33 citations and is from a domain leading peer-reviewed journal.

29. (manuel2024soilsurveillancefor pages 8-10): Malathi Manuel, Heather K. Amato, Nils Pilotte, Benard Chieng, Sylvie B. Araka, Joël Edoux Eric Siko, Michael Harris, Maya L. Nadimpalli, Venkateshprabhu Janagaraj, Parfait Houngbegnon, Rajeshkumar Rajendiran, Joel Thamburaj, Saravanakumar Puthupalayam Kaliappan, Allison R. Sirois, Gretchen Walch, William E. Oswald, Kristjana H. Asbjornsdottir, Sean R. Galagan, Judd L. Walson, Steven A. Williams, Adrian J. F. Luty, Sammy M. Njenga, Moudachirou Ibikounlé, Sitara S. R. Ajjampur, and Amy J. Pickering. Soil surveillance for monitoring soil-transmitted helminths: method development and field testing in three countries. PLOS Neglected Tropical Diseases, 18:e0012416, Sep 2024. URL: https://doi.org/10.1371/journal.pntd.0012416, doi:10.1371/journal.pntd.0012416. This article has 10 citations and is from a domain leading peer-reviewed journal.

30. (roose2024serologicaldiagnosisof pages 1-2): Sara Roose, Fiona Vande Velde, Johnny Vlaminck, Peter Geldhof, and Bruno Levecke. Serological diagnosis of soil-transmitted helminth (ascaris, trichuris and hookworm) infections: a scoping review. PLOS Neglected Tropical Diseases, 18:e0012049, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0012049, doi:10.1371/journal.pntd.0012049. This article has 15 citations and is from a domain leading peer-reviewed journal.

31. (roose2024serologicaldiagnosisof pages 11-12): Sara Roose, Fiona Vande Velde, Johnny Vlaminck, Peter Geldhof, and Bruno Levecke. Serological diagnosis of soil-transmitted helminth (ascaris, trichuris and hookworm) infections: a scoping review. PLOS Neglected Tropical Diseases, 18:e0012049, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0012049, doi:10.1371/journal.pntd.0012049. This article has 15 citations and is from a domain leading peer-reviewed journal.

32. (curico2024efficacyofsingledose pages 6-7): Greisi Curico, Paul F. Garcia Bardales, Tackeshy N. Pinedo Vasquez, Wagner Valentino Shapiama Lopez, Maribel Paredes Olortegui, Francesca Schiaffino, Pablo Peñataro Yori, Josh M. Colston, Thomas G. Flynn, Graciela Meza Sánchez, Hermann Silva Delgado, Richard A. Oberhelman, and Margaret N. Kosek. Efficacy of single-dose albendazole and albendazole plus ivermectin for soil-transmitted helminth infection in children in the peruvian amazon. The American Journal of Tropical Medicine and Hygiene, 111:80-88, Jul 2024. URL: https://doi.org/10.4269/ajtmh.23-0497, doi:10.4269/ajtmh.23-0497. This article has 8 citations.

33. (grolimund2024modelingtransmissionmechanism pages 4-5): Carla M. Grolimund, Jürg Utzinger, Jean T. Coulibaly, Somphou Sayasone, Said M. Ali, Jennifer Keiser, and Penelope Vounatsou. Modeling transmission mechanism to infer treatment efficacy of different drugs and combination therapy against trichuris trichiura. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-73164-7, doi:10.1038/s41598-024-73164-7. This article has 1 citations and is from a peer-reviewed journal.

34. (le2024effectivenessofivermectin pages 1-2): Brandon Le, Naomi E. Clarke, Nicolas Legrand, and Susana Vaz Nery. Effectiveness of ivermectin mass drug administration in the control of soil-transmitted helminth infections in endemic populations: a systematic review and meta-analysis. Infectious Diseases of Poverty, Feb 2024. URL: https://doi.org/10.1186/s40249-024-01185-5, doi:10.1186/s40249-024-01185-5. This article has 16 citations and is from a domain leading peer-reviewed journal.

35. (NCT04700423 chunk 1): Jennifer Keiser. Efficacy and Safety of MOX/ALB vs. IVM/ALB Co-administration. Jennifer Keiser. 2021. ClinicalTrials.gov Identifier: NCT04700423

36. (NCT06800248 chunk 1):  Efficacy and Safety of Emodepside in Participants With Soil-transmitted Helminth Infections. Swiss Tropical & Public Health Institute. 2026. ClinicalTrials.gov Identifier: NCT06800248

37. (ugwu2024theimpactof pages 1-2): Sommy C. Ugwu, Michael O. Muoka, Clara MacLeod, Sarah Bick, Oliver Cumming, and Laura Braun. The impact of community based interventions for the prevention and control of soil-transmitted helminths: a systematic review and meta-analysis. PLOS Global Public Health, 4:e0003717, Oct 2024. URL: https://doi.org/10.1371/journal.pgph.0003717, doi:10.1371/journal.pgph.0003717. This article has 6 citations and is from a peer-reviewed journal.

38. (ng’etich2024anthelminticresistancein pages 1-2): Annette Imali Ng’etich, Isaac Dennis Amoah, Faizal Bux, and Sheena Kumari. Anthelmintic resistance in soil-transmitted helminths: one-health considerations. Parasitology Research, Dec 2024. URL: https://doi.org/10.1007/s00436-023-08088-8, doi:10.1007/s00436-023-08088-8. This article has 54 citations and is from a peer-reviewed journal.

39. (mair2024theadaptiveimmune pages 11-12): Iris Mair, Jonathan Fenn, Andrew Wolfenden, Ann E. Lowe, Alex Bennett, Andrew Muir, Jacob Thompson, Olive Dieumerci, Larisa Logunova, Susanne Shultz, Janette E. Bradley, and Kathryn J. Else. The adaptive immune response to trichuris in wild versus laboratory mice: an established model system in context. PLOS Pathogens, 20:e1012119, Apr 2024. URL: https://doi.org/10.1371/journal.ppat.1012119, doi:10.1371/journal.ppat.1012119. This article has 5 citations and is from a highest quality peer-reviewed journal.

40. (chen2024globalburdenof pages 5-7): Jin Chen, Yanfeng Gong, Qin Chen, Shizhu Li, and Yibiao Zhou. Global burden of soil-transmitted helminth infections, 1990–2021. Infectious Diseases of Poverty, Oct 2024. URL: https://doi.org/10.1186/s40249-024-01238-9, doi:10.1186/s40249-024-01238-9. This article has 93 citations and is from a domain leading peer-reviewed journal.

41. (stuyver2021theroleof pages 2-3): Lieven J. Stuyver and Bruno Levecke. The role of diagnostic technologies to measure progress toward who 2030 targets for soil-transmitted helminth control programs. PLOS Neglected Tropical Diseases, 15:e0009422, Jun 2021. URL: https://doi.org/10.1371/journal.pntd.0009422, doi:10.1371/journal.pntd.0009422. This article has 33 citations and is from a domain leading peer-reviewed journal.

42. (grolimund2024modelingtransmissionmechanism pages 8-9): Carla M. Grolimund, Jürg Utzinger, Jean T. Coulibaly, Somphou Sayasone, Said M. Ali, Jennifer Keiser, and Penelope Vounatsou. Modeling transmission mechanism to infer treatment efficacy of different drugs and combination therapy against trichuris trichiura. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-73164-7, doi:10.1038/s41598-024-73164-7. This article has 1 citations and is from a peer-reviewed journal.

43. (bekele2024efficacyofalbendazole pages 10-14): Temesgen Bekele, Lata Lachisa, Arega Bedasso Tsegaye, K. Bacha, and T. Ketema. Efficacy of albendazole and mebendazole against soil transmitted infections among pre-school and school age children: a systematic review and meta-analysis. Journal of Epidemiology and Global Health, 14:884-904, May 2024. URL: https://doi.org/10.1007/s44197-024-00231-7, doi:10.1007/s44197-024-00231-7. This article has 18 citations and is from a peer-reviewed journal.

44. (curico2024efficacyofsingledose pages 5-6): Greisi Curico, Paul F. Garcia Bardales, Tackeshy N. Pinedo Vasquez, Wagner Valentino Shapiama Lopez, Maribel Paredes Olortegui, Francesca Schiaffino, Pablo Peñataro Yori, Josh M. Colston, Thomas G. Flynn, Graciela Meza Sánchez, Hermann Silva Delgado, Richard A. Oberhelman, and Margaret N. Kosek. Efficacy of single-dose albendazole and albendazole plus ivermectin for soil-transmitted helminth infection in children in the peruvian amazon. The American Journal of Tropical Medicine and Hygiene, 111:80-88, Jul 2024. URL: https://doi.org/10.4269/ajtmh.23-0497, doi:10.4269/ajtmh.23-0497. This article has 8 citations.

45. (grolimund2024modelingtransmissionmechanism pages 5-6): Carla M. Grolimund, Jürg Utzinger, Jean T. Coulibaly, Somphou Sayasone, Said M. Ali, Jennifer Keiser, and Penelope Vounatsou. Modeling transmission mechanism to infer treatment efficacy of different drugs and combination therapy against trichuris trichiura. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-73164-7, doi:10.1038/s41598-024-73164-7. This article has 1 citations and is from a peer-reviewed journal.

46. (levecke2024theassessmentof pages 6-9): Bruno Levecke, Nour Rashwan, Piet Cools, Marco Albonico, Shaali M Ame, Mio Ayana, Daniel Dana, Jennifer Keiser, Antonio Montresor, Zeleke Mekonnen, Sara Roose, Somphou Sayasone, Jozef Vercruysse, Jaco J Verweij, Johnny Vlaminck, and Roger Prichard. The assessment of single nucleotide polymorphisms in the ß-tubulin genes in human soil-transmitted helminths exposed to different pressure with benzimidazole drugs. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2024.06.04.597280, doi:10.1101/2024.06.04.597280. This article has 1 citations.

47. (oyeyemi2023soiltransmittedhelminthiasis(sth) pages 2-3): Oyetunde T. Oyeyemi and Oluyemi A. Okunlola. Soil-transmitted helminthiasis (sth) endemicity and performance of preventive chemotherapy intervention programme in nigeria (in year 2021). Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-37402-8, doi:10.1038/s41598-023-37402-8. This article has 9 citations and is from a peer-reviewed journal.

48. (mengistu2024soiltransmittedhelminth(sth) pages 1-2): Birhan Mengistu, Ewnetu Firdawek Liyew, Melkie Chernet, Geremew Tasew, Rosie Maddren, Benjamin Collyer, Ufaysa Anjulo, Adugna Tamiru, Kathryn Forbes, Zelalem Mehari, Kebede Deribe, Teshale Yadeta, Mihretab Salasibew, Getachew Tollera, and Roy Anderson. Soil-transmitted helminth (sth) infections in the wolaita zone in southern ethiopia: mid-stage evaluation of the geshiyaro project and progress towards the interruption of transmission. Parasites & Vectors, Aug 2024. URL: https://doi.org/10.1186/s13071-024-06422-2, doi:10.1186/s13071-024-06422-2. This article has 3 citations and is from a peer-reviewed journal.
