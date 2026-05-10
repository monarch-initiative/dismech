---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T12:52:34.704031'
end_time: '2026-05-10T13:12:03.968124'
duration_seconds: 1169.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Frias syndrome
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** Frias syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Frias syndrome** covering all of the
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
- **Disease Name:** Frias syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Frias syndrome** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Frias syndrome

### Scope note (terminology disambiguation)
“Frias syndrome” in contemporary genetics literature most commonly refers to **14q22q23 microdeletion syndrome** (a contiguous-gene deletion syndrome involving developmental genes such as *BMP4* and *OTX2*). It should not be confused with **Martinez–Frías syndrome** (a distinct, primarily gastrointestinal/neonatal-diabetes syndrome).

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
**Frias syndrome (14q22q23 microdeletion syndrome)** is an **extremely rare** contiguous deletion of chromosome 14q characterized by a core triad of **pituitary**, **eye**, and **hand/foot** anomalies, frequently accompanied by **intellectual disability** and **facial dysmorphism**. (kera2021anophthalmiaglobaldevelopmental pages 1-2)

**Direct abstract quote (definition):** “**14q22q23 microdeletion syndrome, also called Frias syndrome, is an extremely rare partial deletion of the long arm of chromosome 14 characterized by the anomalies of the pituitary gland, eyes, and hand/foot. Intellectual disability and facial dysmorphism are other common manifestations.**” (Kera et al., Cureus, published **2021-07-14**; https://doi.org/10.7759/cureus.16395) (kera2021anophthalmiaglobaldevelopmental pages 1-2)

### 1.2 Key identifiers
- **OMIM:** Frías syndrome reported as **OMIM: 609640** in the BMP4-haploinsufficiency-focused AJMG paper. (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2)
- **MONDO ID:** Not identified in the retrieved evidence; requires confirmation from MONDO/OMIM cross-references outside the current retrieved set. (kera2021anophthalmiaglobaldevelopmental pages 1-2)
- **MeSH / ICD-10 / ICD-11 / Orphanet:** Not available in the retrieved full text evidence set; should be looked up in OMIM/Orphanet/ICD browsers during knowledge-base ingestion. (kera2021anophthalmiaglobaldevelopmental pages 1-2)

### 1.3 Synonyms / alternative names
- **14q22q23 microdeletion syndrome** (explicit) (kera2021anophthalmiaglobaldevelopmental pages 1-2)
- **14q22–q23 contiguous gene deletion syndrome** (used in diagnostic genetics discussions) (apamgarduno2019therelevanceof pages 1-4)

### 1.4 Evidence source type
Knowledge is derived primarily from:
- **Human case reports and small case series** with chromosomal microarray-defined deletions (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 1-2)
- **Letters/reviews summarizing compiled cases** of syndromic microphthalmia/anophthalmia due to *OTX2*-region deletions (apamgarduno2019therelevanceof pages 1-4)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** **Heterozygous interstitial microdeletions** in **chromosome 14q22–q23** that remove one copy (haploinsufficiency) of developmental regulators. (kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2)

**Key genes implicated (recurrently deleted):**
- *BMP4* and *OTX2* are repeatedly highlighted as major drivers of the phenotype in 14q22q23 deletions. (kera2021anophthalmiaglobaldevelopmental pages 1-2)
- *SIX1* and *SIX6* may be included depending on breakpoints and are discussed as contributors to pituitary/optic nerve/craniofacial phenotypes. (kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2)

**Direct abstract quote (genetic interpretation):** “**Haploinsufficiency of the genes bone morphogenetic protein 4 (BMP4) and orthodenticle homeobox 2 (OTX2) accounts for most of the phenotypic abnormalities seen in these patients.**” (Kera et al., Cureus, **2021-07-14**; https://doi.org/10.7759/cureus.16395) (kera2021anophthalmiaglobaldevelopmental pages 1-2)

### 2.2 Risk factors
For a contiguous-gene microdeletion syndrome, “risk factors” are primarily genetic:
- **De novo CNVs**: documented in at least one reported case where “both parents had normal karyotypes,” consistent with a de novo event. (apamgarduno2019therelevanceof pages 1-4)
- **Familial transmission**: also documented—one report described a mother and two affected daughters sharing the same 14q22.1–q22.3 deletion. (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2)

Environmental risk factors, protective factors, and gene–environment interactions specific to Frias syndrome were not identified in the retrieved evidence.

---

## 3. Phenotypes

A structured phenotype-to-HPO mapping derived from retrieved clinical reports is provided in the artifact below.

| Phenotype domain | Core phenotype(s) reported in Frias syndrome / 14q22q23 microdeletion | Suggested HPO term(s) | Onset / severity / variability notes | Key supporting evidence |
|---|---|---|---|---|
| Ocular | Anophthalmia, microphthalmia, mild exophthalmia, ptosis, hypertelorism, absent/rudimentary optic nerves, optic chiasm abnormalities, corneal opacity, need for glasses in some cases | HP:0000528 Anophthalmia; HP:0000568 Microphthalmia; HP:0000613 Photophobia not supported; HP:0000532 Abnormality of eye morphology; HP:0000653 Optic nerve hypoplasia; HP:0000508 Ptosis; HP:0000316 Hypertelorism; HP:0000603 Corneal opacity; HP:0000622 Exophthalmos | Typically congenital/neonatal; often severe and among the most recognizable features, but variable expressivity is substantial, including milder ocular findings in some familial BMP4 deletions (kera2021anophthalmiaglobaldevelopmental pages 1-2, apamgarduno2019therelevanceof pages 1-4, kera2021anophthalmiaglobaldevelopmental pages 4-7, blackburn2019variableexpressivityof pages 2-3, martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2) | Kera 2021; Apam-Garduño 2019; Blackburn 2019; Martínez-Fernández 2014 (kera2021anophthalmiaglobaldevelopmental pages 1-2, apamgarduno2019therelevanceof pages 1-4, blackburn2019variableexpressivityof pages 2-3, martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2) |
| Pituitary / endocrine | Pituitary hypoplasia/aplasia, high-riding posterior pituitary, possible hypopituitarism and growth hormone deficiency, growth retardation/short stature | HP:0000822 Pituitary hypoplasia; HP:0003070 Growth hormone deficiency; HP:0001508 Failure to thrive; HP:0004322 Short stature; HP:0001510 Growth delay | Congenital structural abnormality with variable endocrine expression; some patients have GH deficiency/growth retardation, while others have normal hormone studies and no pituitary dysfunction despite similar regional deletions (kera2021anophthalmiaglobaldevelopmental pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 2-4, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 4-7) | Kera 2021; Martínez-Frías 2014; Apam-Garduño 2019 (kera2021anophthalmiaglobaldevelopmental pages 2-4, kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2) |
| Limb / digits | Short square hands, short digits, broad halluces, proximal syndactyly, postaxial or preaxial polydactyly, pes cavus, progressive distal phalangeal hypoplasia | HP:0009381 Short hand; HP:0001169 Syndactyly; HP:0010442 Postaxial polydactyly; HP:0100259 Preaxial polydactyly; HP:0001761 Pes cavus; HP:0009882 Short distal phalanx | Usually congenital; severity ranges from subtle hand/foot changes to frank poly/syndactyly; hallmark in many reports but absent in at least one recent case, showing reduced penetrance/variable expressivity (kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, apamgarduno2019therelevanceof pages 4-5, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 4-7) | Martínez-Fernández 2014; Kera 2021; Apam-Garduño 2019; Martínez-Frías 2014 (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, apamgarduno2019therelevanceof pages 4-5, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 4-7) |
| Neurodevelopment / CNS | Global developmental delay, psychomotor delay, moderate intellectual disability, speech delay/dysarthria/logoclonia, seizures, corpus callosum hypoplasia, ventriculomegaly, polymicrogyria, deep gray matter and white matter abnormalities | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability; HP:0001270 Motor delay; HP:0001250 Seizure; HP:0002079 Corpus callosum abnormality; HP:0002119 Ventriculomegaly; HP:0012650 Polymicrogyria; HP:0002500 Abnormal cerebral white matter morphology | Congenital structural CNS findings may become clearer over infancy/childhood; neurodevelopmental impairment is common but severity varies from mild psychomotor delay to severe global delay with seizures (martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2, apamgarduno2019therelevanceof pages 1-4, kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 4-7) | Kera 2021; Apam-Garduño 2019; Martínez-Fernández 2014; Martínez-Frías 2014 (apamgarduno2019therelevanceof pages 1-4, martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 4-7) |
| Hearing | Mild right hearing loss, bilateral sensorineural hearing loss reported in OTX2-region deletions; hearing may also be normal in some patients | HP:0000365 Hearing impairment; HP:0000407 Sensorineural hearing impairment | Variable; not universal. Reported in some familial/de novo cases and literature summaries, but normal hearing documented in at least one patient with 14q22.3-q23.2 deletion (kera2021anophthalmiaglobaldevelopmental pages 1-2, apamgarduno2019therelevanceof pages 1-4, martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2) | Apam-Garduño 2019; Kera 2021; Martínez-Fernández 2014; Martínez-Frías 2014 (apamgarduno2019therelevanceof pages 1-4, martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2) |
| Feeding / airway | Oropharyngeal dysphagia, aspiration, severe protein-calorie malnutrition, increased secretions, tracheomalacia, tracheostomy requirement, gastroesophageal reflux, bilateral choanal atresia | HP:0002015 Dysphagia; HP:0002093 Respiratory insufficiency not directly established; HP:0002020 Gastroesophageal reflux; HP:0000453 Choanal atresia; HP:0002205 Tracheomalacia; HP:0004395 Malnutrition | Can present neonatally or in early childhood; severity may be high in complex cases, requiring feeding tubes and airway support. Reflux/aspiration and choanal atresia broaden the respiratory/feeding phenotype beyond classic ocular-limb findings (kera2021anophthalmiaglobaldevelopmental pages 4-7, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2) | Kera 2021; Martínez-Frías 2014 (kera2021anophthalmiaglobaldevelopmental pages 4-7, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2) |
| Cardiac | Atrial septal defect, ventricular septal defect; cardiac malformations noted in literature summaries of OTX2-region deletions | HP:0001631 Atrial septal defect; HP:0001629 Ventricular septal defect; HP:0001627 Abnormal heart morphology | Reported as variable/less frequent than ocular-pituitary findings; present in some cases and reviews but not clearly universal across the syndrome (apamgarduno2019therelevanceof pages 1-4, kera2021anophthalmiaglobaldevelopmental pages 4-7) | Apam-Garduño 2019; Kera 2021 (apamgarduno2019therelevanceof pages 1-4, kera2021anophthalmiaglobaldevelopmental pages 4-7) |
| Renal / genitourinary | Congenital genitourinary malformations; renal anomalies noted in some 14q21-q23 deletion reports | HP:0000078 Abnormality of the genitourinary system; HP:0000119 Abnormal renal morphology | Reported variably in literature summaries; current retrieved evidence does not define a single dominant renal phenotype or frequency (kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2, apamgarduno2019therelevanceof pages 1-4) | Kera 2021; Martínez-Frías 2014; Apam-Garduño 2019 (kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2, apamgarduno2019therelevanceof pages 1-4) |
| Craniofacial | Facial dysmorphism, depressed nasal bridge, small nostrils, abnormal auricles/ear anomalies, downslanting palpebral fissures, bilateral ptosis, hypertelorism, choanal atresia | HP:0001999 Facial dysmorphism; HP:0000431 Broad nasal bridge / HP:0005280 Depressed nasal bridge; HP:0000582 Downslanted palpebral fissures; HP:0000508 Ptosis; HP:0000316 Hypertelorism; HP:0000377 Abnormal pinna morphology; HP:0000453 Choanal atresia | Congenital and common; often recognizable at birth. Facial phenotype ranges from relatively mild familial presentations to complex dysmorphism with airway involvement (kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2, martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2) | Martínez-Fernández 2014; Martínez-Frías 2014; Kera 2021 (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2) |


*Table: This table summarizes core clinical features reported for Frias syndrome (14q22q23 microdeletion syndrome), with suggested HPO terms and brief notes on onset, variability, and supporting evidence. It is useful for structured phenotype curation in a disease knowledge base.*

### 3.1 Core phenotype domains and clinical spectrum
**Pituitary/endocrine:** pituitary hypoplasia/aplasia and endocrine dysfunction (often GH axis) are a commonly described part of the syndrome spectrum, but may be absent in some patients even with overlapping deletions. (kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2)

**Ocular/visual pathway:** anophthalmia/microphthalmia and optic nerve/chiasm abnormalities are prominent and typically congenital. (kera2021anophthalmiaglobaldevelopmental pages 1-2, apamgarduno2019therelevanceof pages 1-4)

**Limb/digits:** syndactyly/polydactyly/short digits are common in many cases, but can be absent (illustrating variable expressivity). (kera2021anophthalmiaglobaldevelopmental pages 4-7)

**Neurodevelopment:** global developmental delay and intellectual disability are frequently reported; seizures and brain malformations can occur. (martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2, apamgarduno2019therelevanceof pages 1-4)

**Feeding/airway (expanded phenotype):** severe dysphagia, tracheomalacia, feeding-tube dependence, and tracheostomy were reported in a child with 14q22q23 deletion, highlighting that morbidity can be multisystem and substantial in individual cases. (kera2021anophthalmiaglobaldevelopmental pages 2-4, kera2021anophthalmiaglobaldevelopmental pages 4-7)

### 3.2 Age of onset, severity, progression
- Many key manifestations are **congenital/neonatal**, particularly ocular and craniofacial anomalies. (kera2021anophthalmiaglobaldevelopmental pages 1-2)
- Severity is **highly variable** and is influenced by deletion size/content and possibly additional diagnoses. (kera2021anophthalmiaglobaldevelopmental pages 1-2, blackburn2019variableexpressivityof pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes / genomic lesion
Frias syndrome is best conceptualized as a **contiguous-gene deletion syndrome**, where the causal unit is the **14q22q23 deletion** rather than a single-gene variant, although **haploinsufficiency of *BMP4*** has been proposed as a major driver of the classic “Frías syndrome” phenotype in some families. (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2)

**Evidence of implicated genes:**
- Case with 14q22.2q23.1 deletion containing **BMP4, OTX2, SIX1, SIX6**. (kera2021anophthalmiaglobaldevelopmental pages 1-2)
- 6.5 Mb 14q22.3-q23.2 deletion including **SIX1, SIX4, SIX6**. (martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2)
- Familial 4.06 Mb 14q22.1–q22.3 deletion including **BMP4**. (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2)

### 4.2 Pathogenic variant class
- **Copy-number variant (CNV):** heterozygous interstitial deletions (Mb-scale) detected by array-CGH/CMA. (apamgarduno2019therelevanceof pages 1-4, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2)

### 4.3 Functional consequence
- Predominantly **haploinsufficiency** of key developmental regulators (*BMP4*, *OTX2*, *SIX* genes). (kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2)

### 4.4 Inheritance pattern
- Mixed: **de novo** CNVs and **familial** CNVs have both been reported. (apamgarduno2019therelevanceof pages 1-4, martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2)

A structured summary is provided below.

| Entity | Also called | Genetic lesion type | Key genes commonly deleted | Key papers (year, journal) | Notes on inheritance (de novo vs familial) with evidence IDs |
|---|---|---|---|---|---|
| Frias syndrome | 14q22q23 microdeletion syndrome; 14q22–q23 contiguous gene deletion syndrome | Interstitial heterozygous microdeletion of chromosome 14q22.1–q23.2/14q22.2–q23.1; contiguous-gene deletion syndrome | BMP4, OTX2, SIX1, SIX6; some reports also include SIX4 and additional neighboring genes depending on breakpoint | Martínez-Fernández et al. 2014, *Am J Med Genet A*; Martínez-Frías et al. 2014, *Am J Med Genet A*; Kera et al. 2021, *Cureus*; Apam-Garduño et al. 2019, *Ophthalmic Genetics* (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 1-2, apamgarduno2019therelevanceof pages 1-4) | Evidence supports both familial and de novo occurrence. Familial transmission: a mother and two affected daughters with a 4.06 Mb 14q22.1–q22.3 deletion including **BMP4** were reported, supporting inherited autosomal dominant transmission of the deletion in that pedigree (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2). De novo occurrence: a 7.16 Mb 14q22.2–q23.2 deletion including **OTX2** and **SIX6** was reported with normal parental karyotypes, supporting a de novo event (apamgarduno2019therelevanceof pages 1-4). Some additional case reports lack explicit parental testing or inheritance data (kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2) |
| 14q22q23 microdeletion involving OTX2/BMP4 region | Frias syndrome spectrum; OTX2/BMP4-region deletion syndrome | Variable-size 14q22.2–q23.2 microdeletions, often 1.28–9.66 Mb in compiled cases | OTX2 and BMP4 are recurrently implicated; SIX6 frequently co-deleted in ocular/pituitary phenotypes; SIX1/SIX4 may also be included in larger deletions | Blackburn et al. 2019, *Eur J Hum Genet*; Apam-Garduño et al. 2019, *Ophthalmic Genetics*; Kera et al. 2021, *Cureus* (blackburn2019variableexpressivityof pages 2-3, apamgarduno2019therelevanceof pages 4-5, kera2021anophthalmiaglobaldevelopmental pages 1-2) | Review-level evidence indicates marked phenotypic variability due to breakpoint/gene-content differences. Inheritance is mixed across the literature: inherited multigenerational 14q22 deletion families exist, but de novo deletions are also documented; no aggregate de novo/familial frequency was available in the retrieved evidence (blackburn2019variableexpressivityof pages 2-3, apamgarduno2019therelevanceof pages 1-4, apamgarduno2019therelevanceof pages 4-5) |


*Table: This table summarizes the disease entity commonly called Frias syndrome/14q22q23 microdeletion syndrome, its lesion type, recurrent genes, core papers, and the available evidence on familial versus de novo inheritance.*

---

## 5. Environmental Information
No Frias-syndrome-specific environmental contributors, protective factors, or infectious triggers were identified in the retrieved sources.

---

## 6. Mechanism / Pathophysiology

### 6.1 Mechanistic causal chain (current model)
**Upstream trigger:** heterozygous deletion of 14q22q23 developmental regulators (CNV). (kera2021anophthalmiaglobaldevelopmental pages 1-2)

**Molecular mechanisms (gene/pathway level):**
- **BMP4** is a **TGF-β superfamily** ligand with broad roles in embryogenesis. (blackburn2019variableexpressivityof pages 1-2)
  - **Direct abstract quote (BMP4 mechanism and functions):** “**Microphthalmia with brain and digital anomalies (MCOPS6… ) is an autosomal dominant disorder caused by loss-of-function variants or large deletions involving BMP4… a member of the TGF-β protein superfamily. BMP4 has a number of roles in embryonic development including neurogenesis, lens induction… limb and digit patterning… as well as tooth formation.**” (Blackburn et al., Eur J Hum Genet, published online **2019-05-03**; https://doi.org/10.1038/s41431-019-0423-4) (blackburn2019variableexpressivityof pages 1-2)
- **BMP4 signaling** proceeds via type I/II serine/threonine kinase receptors with **SMAD-dependent and SMAD-independent** downstream signaling. (blackburn2019variableexpressivityof pages 2-3)
- **OTX2** functions as a transcription factor critical for pituitary/brain/sensory development; in microdeletion contexts it is associated with ocular defects and pituitary malformations. (apamgarduno2019therelevanceof pages 1-4)
- **SIX genes (SIX1/SIX6)** are discussed as contributors to craniofacial/pituitary/optic nerve phenotypes, consistent with the syndrome’s triad. (kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2)

**Tissue/cellular consequences (developmental biology):** impaired patterning and morphogenesis of (i) eye/optic nerve/visual pathways, (ii) pituitary/hypothalamic region, (iii) limb/digit patterning, with variable additional effects on craniofacial structures, CNS development, and other organs depending on breakpoint. (kera2021anophthalmiaglobaldevelopmental pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2)

**Downstream clinical manifestations:** congenital anophthalmia/microphthalmia, pituitary anomalies ± GH deficiency/growth delay, limb anomalies, neurodevelopmental delay, and variable multisystem disease (e.g., feeding/airway, cardiac). (kera2021anophthalmiaglobaldevelopmental pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 2-4)

### 6.2 Relevant pathway context and model-organism evidence (recent)
A 2024 zebrafish-focused review underscores that **TGF-β and BMP pathways** are essential for craniofacial development and that zebrafish enable mechanistic dissection of developmental signaling and gene–environment modifiers; it also notes that human disease and malformations can arise from pathway perturbations. (Fox & Waskiewicz, Frontiers in Cell and Developmental Biology, **2024-02-07**; https://doi.org/10.3389/fcell.2024.1338070) (fox2024transforminggrowthfactor pages 1-2)

### 6.3 Ontology suggestions
**GO Biological Process (examples, to be curated to match exact gene annotations):**
- GO:0001501 skeletal system development
- GO:0030326 embryonic limb morphogenesis
- GO:0001654 eye development
- GO:0001947 heart morphogenesis (for cases with CHD)
- GO:0021517 ventral midbrain development / broader neurodevelopment terms (case dependent)

**Cell Ontology (CL) candidates (high-level, developmentally relevant):**
- CL:0000135 neural crest cell (craniofacial patterning context; supported by BMP/TGF-β craniofacial review) (fox2024transforminggrowthfactor pages 1-2)

**UBERON (anatomy) candidates:**
- UBERON:0000970 eye
- UBERON:0000007 pituitary gland
- UBERON:0002101 limb

---

## 7. Anatomical Structures Affected
Based on reported phenotypes:
- **Eye and visual pathway** (optic nerve/chiasm). (apamgarduno2019therelevanceof pages 1-4)
- **Pituitary/hypothalamic region** (structural pituitary anomalies and endocrine effects). (kera2021anophthalmiaglobaldevelopmental pages 2-4)
- **Limbs/digits**. (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2)
- **Brain** (corpus callosum, cortical malformations, hydrocephalus in some individuals). (apamgarduno2019therelevanceof pages 1-4, kera2021anophthalmiaglobaldevelopmental pages 2-4)
- **Airway/GI feeding structures** in some severe cases (dysphagia, tracheomalacia). (kera2021anophthalmiaglobaldevelopmental pages 2-4)
- **Heart** (ASD/VSD in at least one case). (kera2021anophthalmiaglobaldevelopmental pages 1-2)

---

## 8. Temporal Development
- **Onset:** predominantly **congenital/neonatal**, particularly ocular anomalies and craniofacial findings. (kera2021anophthalmiaglobaldevelopmental pages 1-2)
- **Course:** variable; neurodevelopmental impairment and seizures may emerge with age; endocrine abnormalities may require longitudinal screening. (martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 2-4)
- **Critical periods:** prenatal development; thus prenatal detection via CNV testing is plausible (not directly documented in retrieved sources, but consistent with CNV nature). (apamgarduno2019therelevanceof pages 1-4)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
Disease-specific prevalence/incidence for Frias syndrome was not available in the retrieved sources, consistent with its description as “extremely rare” and “only a few cases reported.” (kera2021anophthalmiaglobaldevelopmental pages 1-2)

However, relevant statistics from the associated **microphthalmia/anophthalmia (M/A)** literature provide context:
- **Chromosomal rearrangements in M/A:** “In **10%–15%** of patients, the cause of M/A is secondary to chromosomal rearrangements.” (Apam-Garduño et al., published online **2019-12-06**; https://doi.org/10.1080/13816810.2019.1698618) (apamgarduno2019therelevanceof pages 1-4)
- **OTX2 contribution to M/A:** “Heterozygous mutations… (*OTX2*)… account for **0.7%–10%** of patients with M/A.” (apamgarduno2019therelevanceof pages 1-4)
- **Case-count signal:** “since 1991, **17 patients** have been diagnosed with syndromic M/A associated with a chromosomal deletion involving the *OTX2* gene.” (apamgarduno2019therelevanceof pages 1-4)

### 9.2 Inheritance
- **Familial inheritance** documented for a specific deletion (mother and two daughters), consistent with autosomal dominant transmission of the deletion in that pedigree. (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2)
- **De novo** documented in at least one *OTX2*-region deletion case (normal parental karyotypes). (apamgarduno2019therelevanceof pages 1-4)

Penetrance/expressivity are **variable**; reduced penetrance is explicitly emphasized for BMP4-related MAC-spectrum disorders, supporting variable expressivity as a key counseling point for deletions involving *BMP4*. (blackburn2019variableexpressivityof pages 1-2)

---

## 10. Diagnostics

### 10.1 Genetic testing (current practice)
**Chromosomal microarray (CMA/aCGH)** is the principal diagnostic modality in the retrieved cases, enabling precise breakpoint and gene-content determination. (apamgarduno2019therelevanceof pages 1-4, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2)

**Karyotype vs microarray (quantitative diagnostic yield context):**
- “Standard karyotype… rate of detection is **7%–15%**” (in syndromic M/A), while “Analysis with aCGH allows the identification of cryptic chromosomal abnormalities in **10%–15%**” of those with syndromic M/A and normal karyotype. (apamgarduno2019therelevanceof pages 1-4)

### 10.2 Clinical tests and evaluations (phenotype-driven)
- Ophthalmologic evaluation and neuroimaging to characterize eye/optic pathway and CNS anomalies. (apamgarduno2019therelevanceof pages 1-4)
- Endocrine evaluation (GH axis/hypopituitarism), because pituitary dysfunction can be present and variable. (kera2021anophthalmiaglobaldevelopmental pages 2-4)
- Audiology, cardiology, feeding/swallow assessment, and airway evaluation in multisystem cases. (kera2021anophthalmiaglobaldevelopmental pages 2-4)

A structured summary of real-world diagnostic and management actions is provided below.

| Domain | Specific tests/interventions | Real-world notes | Evidence type (case report/review) | Key citations with year+URL | Evidence IDs |
|---|---|---|---|---|---|
| Genetic test | Chromosomal microarray / array-CGH (aCGH/CMA) | Highest-yield test in retrieved literature for defining 14q22q23 deletions and breakpoints; identified 4.06 Mb familial deletion including **BMP4**, 6.5 Mb deletion including **SIX1/SIX4/SIX6**, and 7.16 Mb **OTX2**-region deletion; useful when routine karyotype is normal and for genotype-phenotype correlation | Case report/series; diagnostic review | Apam-Garduño et al., 2019, *Ophthalmic Genetics*, https://doi.org/10.1080/13816810.2019.1698618; Martínez-Fernández et al., 2014, *Am J Med Genet A*, https://doi.org/10.1002/ajmg.a.36224; Martínez-Frías et al., 2014, *Am J Med Genet A*, https://doi.org/10.1002/ajmg.a.36330 | (apamgarduno2019therelevanceof pages 1-4, martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2) |
| Genetic test | Standard karyotype | Can confirm an interstitial deletion once suspected, but may miss submicroscopic lesions; one report states detection rate for chromosomal anomalies in syndromic microphthalmia/anophthalmia is ~7%–15%; parental karyotypes may help establish de novo status | Case report; review/letter | Apam-Garduño et al., 2019, *Ophthalmic Genetics*, https://doi.org/10.1080/13816810.2019.1698618 | (apamgarduno2019therelevanceof pages 1-4) |
| Genetic test | FISH / targeted molecular cytogenetics | Mentioned as adjunctive testing in a familial Frías syndrome study when high-resolution G-banded karyotype was apparently normal; useful if a specific 14q22 deletion is suspected | Thesis/report-derived evidence | Martínez-Fernández, 2016, *Estudio clínico epidemiológico...* (no stable journal URL available in retrieved evidence) | (fernandez2016estudioclínicoepidemiológico pages 62-63) |
| Imaging / endocrine eval | Brain MRI; pituitary-focused neuroimaging; hormone testing including GH-axis assessment | MRI can identify absent/hypoplastic optic tracts/chiasm, corpus callosum abnormalities, hydrocephalus, high-riding posterior pituitary, and other CNS anomalies; pituitary structure/function is variable, so endocrine evaluation is warranted even if imaging appears normal | Case report; review | Kera et al., 2021, *Cureus*, https://doi.org/10.7759/cureus.16395; Apam-Garduño et al., 2019, *Ophthalmic Genetics*, https://doi.org/10.1080/13816810.2019.1698618; Martínez-Frías et al., 2014, *Am J Med Genet A*, https://doi.org/10.1002/ajmg.a.36330 | (kera2021anophthalmiaglobaldevelopmental pages 2-4, kera2021anophthalmiaglobaldevelopmental pages 4-7, apamgarduno2019therelevanceof pages 1-4, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2) |
| Ophthalmology | Comprehensive ophthalmologic exam; visual pathway evaluation; orbital/brain imaging; ptosis repair when indicated | Ocular disease is often congenital and severe (anophthalmia/microphthalmia, optic nerve/chiasm anomalies), but some familial BMP4 deletions show milder findings such as exophthalmia/ptosis; surgical ptosis correction was reported in one child | Case report/series | Kera et al., 2021, *Cureus*, https://doi.org/10.7759/cureus.16395; Martínez-Fernández et al., 2014, *Am J Med Genet A*, https://doi.org/10.1002/ajmg.a.36224 | (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 4-7) |
| Hearing | Audiology / hearing assessment | Hearing loss is variable rather than universal; mild unilateral hearing loss reported in one familial case, while another 14q22.3-q23.2 deletion case had normal hearing; because contiguous deletions involving **OTX2/SIX6** can include deafness, audiologic surveillance is reasonable | Case report; review/letter | Martínez-Fernández et al., 2014, *Am J Med Genet A*, https://doi.org/10.1002/ajmg.a.36224; Apam-Garduño et al., 2019, *Ophthalmic Genetics*, https://doi.org/10.1080/13816810.2019.1698618; Martínez-Frías et al., 2014, *Am J Med Genet A*, https://doi.org/10.1002/ajmg.a.36330 | (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, apamgarduno2019therelevanceof pages 1-4, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2) |
| Feeding / airway | Feeding-tube support; gastrostomy; airway evaluation for tracheomalacia; tracheostomy when necessary | Severe dysphagia/airway disease can dominate management in complex cases; one child required gastrostomy, then developed respiratory compromise from tracheomalacia necessitating tracheostomy, later complicated by MRSA tracheitis and fatal sepsis | Case report | Kera et al., 2021, *Cureus*, https://doi.org/10.7759/cureus.16395 | (kera2021anophthalmiaglobaldevelopmental pages 2-4, kera2021anophthalmiaglobaldevelopmental pages 4-7) |
| Cardiac | Echocardiography / cardiology assessment and follow-up | Cardiac defects are not universal but have been documented, including secundum ASD and restrictive VSD; one patient was followed in pediatric cardiology | Case report; review | Kera et al., 2021, *Cureus*, https://doi.org/10.7759/cureus.16395; Apam-Garduño et al., 2019, *Ophthalmic Genetics*, https://doi.org/10.1080/13816810.2019.1698618 | (kera2021anophthalmiaglobaldevelopmental pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 4-7, apamgarduno2019therelevanceof pages 1-4) |
| Surgery | Diaphragmatic hernia repair; ptosis correction; neurosurgical shunt procedures | Management is phenotype-driven rather than syndrome-specific; reported surgeries include neonatal diaphragmatic hernia repair, bilateral ptosis correction, and ventriculoperitoneal shunt placement for hydrocephalus | Case report/series | Martínez-Fernández et al., 2014, *Am J Med Genet A*, https://doi.org/10.1002/ajmg.a.36224; Kera et al., 2021, *Cureus*, https://doi.org/10.7759/cureus.16395 | (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 2-4) |
| Multidisciplinary management | Coordinated care across genetics, ophthalmology, endocrinology, neurology, ENT/audiology, nutrition/feeding, pulmonology/airway, cardiology, rehabilitation | No formal disease-specific guideline was retrieved, but the multisystem phenotype and real-world cases support multidisciplinary follow-up and individualized supportive care | Inference grounded in case reports/review | Kera et al., 2021, *Cureus*, https://doi.org/10.7759/cureus.16395; Apam-Garduño et al., 2019, *Ophthalmic Genetics*, https://doi.org/10.1080/13816810.2019.1698618 | (kera2021anophthalmiaglobaldevelopmental pages 2-4, kera2021anophthalmiaglobaldevelopmental pages 4-7, apamgarduno2019therelevanceof pages 1-4) |
| Growth hormone / endocrine treatment | Consider endocrine referral and GH-axis evaluation; GH therapy reported in related 14q22q23 microdeletion literature | Retrieved evidence did not include the full primary report, but a literature summary cited “three children with microdeletions of 14q22q23” who had abnormal pituitary development and response to growth hormone therapy; direct treatment-effect details were not available in current context | Review/letter summarizing prior case series | Apam-Garduño et al., 2019, *Ophthalmic Genetics*, https://doi.org/10.1080/13816810.2019.1698618 | (apamgarduno2019therelevanceof pages 5-5) |


*Table: This table summarizes the main diagnostic approaches and phenotype-directed management reported for Frias syndrome / 14q22q23 microdeletion syndrome. It highlights the central role of chromosomal microarray, the variability of multisystem involvement, and the supportive, multidisciplinary nature of current care.*

### 10.3 Differential diagnosis
Within the retrieved corpus, Frias syndrome overlaps with:
- Other causes of syndromic M/A (SOX2-related, single-gene *BMP4* loss-of-function, *OTX2* sequence variants). (blackburn2019variableexpressivityof pages 1-2, apamgarduno2019therelevanceof pages 1-4)

---

## 11. Outcome / Prognosis
Prognosis is **case-dependent** and driven by the degree of multisystem involvement:
- One familial case report noted **neonatal death** after diaphragmatic hernia repair in an affected newborn. (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2)
- Another detailed case described severe airway/infectious complications culminating in death from sepsis at age seven (MRSA tracheitis context). (kera2021anophthalmiaglobaldevelopmental pages 2-4)

No cohort-level survival statistics were retrieved.

---

## 12. Treatment

### 12.1 Current applications / real-world implementations
There is **no syndrome-specific curative therapy** in the retrieved evidence; treatment is **supportive and multidisciplinary**, directed at organ-specific manifestations:
- **Surgical interventions**: diaphragmatic hernia repair, ptosis correction, ventriculoperitoneal shunt for hydrocephalus. (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2, kera2021anophthalmiaglobaldevelopmental pages 2-4)
- **Feeding/airway support**: gastrostomy/feeding tubes, tracheostomy where needed. (kera2021anophthalmiaglobaldevelopmental pages 2-4)
- **Cardiology follow-up** for congenital heart defects (ASD/VSD). (kera2021anophthalmiaglobaldevelopmental pages 1-2)

### 12.2 Growth hormone therapy
A literature summary cited “three children with microdeletions of 14q22q23” with abnormal pituitary development and “response to growth hormone therapy,” but the underlying primary report was not retrievable in the present context, so effect sizes/dosing/outcomes cannot be extracted here. (apamgarduno2019therelevanceof pages 5-5)

### 12.3 MAXO (Medical Action Ontology) suggestions (examples)
- Chromosomal microarray analysis (genetic diagnostic test)
- Ophthalmologic evaluation
- Endocrine evaluation / growth hormone replacement therapy (case-dependent)
- Gastrostomy tube placement
- Tracheostomy
- Surgical repair of congenital diaphragmatic hernia
- Ventriculoperitoneal shunt placement

### 12.4 Clinical trials
No disease-specific clinical trials for Frias syndrome/14q22q23 microdeletion were identified in the retrieved ClinicalTrials.gov search results. (apamgarduno2019therelevanceof pages 1-4)

---

## 13. Prevention
No primary prevention is available for de novo CNVs. Practical prevention is mainly **reproductive/genetic counseling**:
- For **de novo** deletions: recurrence risk is generally low but not zero (not quantified in retrieved sources).
- For **familial** deletions: recurrence risk can be substantial; family testing and counseling are relevant. (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2)

Prenatal testing is plausible via CNV detection (CMA), but no prenatal case was retrieved in this evidence set.

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary analog or OMIA entry was identified in the retrieved evidence.

---

## 15. Model Organisms

### 15.1 Available model evidence (gene/pathway level)
- A 2024 review synthesizes zebrafish evidence demonstrating the importance of **TGF-β/BMP signaling** in craniofacial development and positions zebrafish as a useful model for human craniofacial diseases caused by pathway perturbations. (Fox & Waskiewicz, **2024-02-07**, https://doi.org/10.3389/fcell.2024.1338070) (fox2024transforminggrowthfactor pages 1-2)

### 15.2 Limitations (syndrome-level)
No model organism replicating the **combined** haploinsufficiency of *BMP4* + *OTX2* ± *SIX1/SIX6* (i.e., the contiguous deletion syndrome) was found in the retrieved corpus.

---

## Recent developments and latest research (prioritizing 2023–2024)
- **Pathway-level advances (2024):** A 2024 Frontiers review emphasizes that TGF-β/BMP signaling is critical across stages of craniofacial development and highlights zebrafish as an experimentally tractable system for dissecting mechanisms and potentially gene–environment interactions affecting craniofacial phenotypes relevant to BMP pathway perturbations. (Published **2024-02-07**; https://doi.org/10.3389/fcell.2024.1338070) (fox2024transforminggrowthfactor pages 1-2)
- **Genetic diagnostics (2024 broader field):** A 2024 Genes review (not specific to Frias syndrome) reinforces the role of **cytogenomic microarray** in evaluating unexplained congenital and syndromic findings, supporting current diagnostic practice for contiguous-gene deletion syndromes. (Published **2024-05-23**; https://doi.org/10.3390/genes15060677) (bonati2024contiguousgenesyndromes pages 1-2)

Direct 2023–2024 Frias-syndrome-specific primary case reports were not retrieved beyond the above pathway/diagnostic context; the most directly informative Frias syndrome case report in the retrieved set remains 2021 (Cureus). (kera2021anophthalmiaglobaldevelopmental pages 1-2)

---

## Expert opinion / analysis (evidence-grounded)
1. **Frias syndrome is best treated as a CNV-defined developmental disorder** where phenotype severity and organ involvement are largely driven by gene content and breakpoint variation; hence, high-resolution CNV testing (CMA/aCGH) is central to diagnosis and counseling. (apamgarduno2019therelevanceof pages 1-4, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2)
2. **Variable expressivity and reduced penetrance** are important counseling concepts, especially where *BMP4* is involved, as BMP4-related disorders can lack classic “hallmark” findings in some carriers. (blackburn2019variableexpressivityof pages 1-2)
3. **Clinical management is inherently multidisciplinary** and supportive, because patients can present with severe ocular impairment plus endocrine, neurologic, feeding/airway, and cardiac issues in different combinations. (kera2021anophthalmiaglobaldevelopmental pages 2-4, martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2)

---

## Key statistics and data (from recent/authoritative sources)
- M/A chromosomal rearrangements: **10%–15%** (apamgarduno2019therelevanceof pages 1-4)
- *OTX2* heterozygous mutation contribution to M/A: **0.7%–10%** (apamgarduno2019therelevanceof pages 1-4)
- Published *OTX2* deletion-associated syndromic M/A cases since 1991: **17 patients** (apamgarduno2019therelevanceof pages 1-4)
- MAC-spectrum prevalence estimates (context): coloboma ~**1/5000**, microphthalmia ~**1/7000**, anophthalmia ~**1/30,000** live births. (blackburn2019variableexpressivityof pages 1-2)
- OTX2 endocrine-ocular association (as stated in one review-like excerpt in the Frias case report): coexistence of ocular manifestations and GH deficiency highest at **30%** in OTX2 mutations. (kera2021anophthalmiaglobaldevelopmental pages 2-4)

---

## Evidence gaps (for knowledge-base completion)
- Formal MONDO/Orphanet/ICD/MeSH identifiers were not retrievable from the current paper set.
- Frias-syndrome-specific prevalence/incidence and standardized clinical diagnostic criteria remain sparse.
- Detailed endocrine treatment outcome data (e.g., GH therapy dosing/response) requires retrieval of the primary 2014 Molecular Cytogenetics series referenced secondarily. (apamgarduno2019therelevanceof pages 5-5)


References

1. (kera2021anophthalmiaglobaldevelopmental pages 1-2): Jeslin Kera, Pankaj Watal, and Syed A Ali. Anophthalmia, global developmental delay, and severe dysphagia in a young girl with 14q22q23 microdeletion syndrome. Cureus, Jul 2021. URL: https://doi.org/10.7759/cureus.16395, doi:10.7759/cureus.16395. This article has 0 citations.

2. (martinez‐fernandez2014haploinsufficiencyofbmp4 pages 1-2): María Luisa Martínez‐Fernández, Eva Bermejo‐Sánchez, Belén Fernández, Alexandra MacDonald, Joaquín Fernández‐Toral, and María Luisa Martínez‐Frías. Haploinsufficiency of bmp4 gene may be the underlying cause of frías syndrome. American Journal of Medical Genetics Part A, 164:338-345, Feb 2014. URL: https://doi.org/10.1002/ajmg.a.36224, doi:10.1002/ajmg.a.36224. This article has 15 citations.

3. (apamgarduno2019therelevanceof pages 1-4): David Apam-Garduño, Vianney Cortés-González, Luis Quintana-Fernández, Daniel Martínez-Anaya, Patricia Pérez-Vera, and Cristina Villanueva-Mendoza. The relevance of the cytogenetic analysis in syndromic microphthalmia/anophthalmia. Ophthalmic Genetics, 40:584-587, Nov 2019. URL: https://doi.org/10.1080/13816810.2019.1698618, doi:10.1080/13816810.2019.1698618. This article has 1 citations and is from a peer-reviewed journal.

4. (martinez‐frias2014interstitialdeletion14q22.3‐q23.2 pages 1-2): María Luisa Martínez‐Frías, Javier Gonzalo Ocejo‐Vinyals, Rosa Arteaga, María Luisa Martínez‐Fernández, Alexandra MacDonald, Elena Pérez‐Belmonte, Eva Bermejo‐Sánchez, and Salvador Martínez. Interstitial deletion 14q22.3‐q23.2: genotype–phenotype correlation. American Journal of Medical Genetics Part A, 164:639-647, Mar 2014. URL: https://doi.org/10.1002/ajmg.a.36330, doi:10.1002/ajmg.a.36330. This article has 15 citations.

5. (kera2021anophthalmiaglobaldevelopmental pages 4-7): Jeslin Kera, Pankaj Watal, and Syed A Ali. Anophthalmia, global developmental delay, and severe dysphagia in a young girl with 14q22q23 microdeletion syndrome. Cureus, Jul 2021. URL: https://doi.org/10.7759/cureus.16395, doi:10.7759/cureus.16395. This article has 0 citations.

6. (blackburn2019variableexpressivityof pages 2-3): Patrick R. Blackburn, Cinthya J. Zepeda-Mendoza, Teresa M. Kruisselbrink, Lisa A. Schimmenti, Sixto García-Miñaur, María Palomares, Julián Nevado, María A. Mori, Guylène Le Meur, Eric W. Klee, Cédric Le Caignec, Pablo Lapunzina, Bertrand Isidor, and Dusica Babovic-Vuksanovic. Variable expressivity of syndromic bmp4-related eye, brain, and digital anomalies: a review of the literature and description of three new cases. European Journal of Human Genetics, 27:1379-1388, May 2019. URL: https://doi.org/10.1038/s41431-019-0423-4, doi:10.1038/s41431-019-0423-4. This article has 18 citations and is from a domain leading peer-reviewed journal.

7. (kera2021anophthalmiaglobaldevelopmental pages 2-4): Jeslin Kera, Pankaj Watal, and Syed A Ali. Anophthalmia, global developmental delay, and severe dysphagia in a young girl with 14q22q23 microdeletion syndrome. Cureus, Jul 2021. URL: https://doi.org/10.7759/cureus.16395, doi:10.7759/cureus.16395. This article has 0 citations.

8. (apamgarduno2019therelevanceof pages 4-5): David Apam-Garduño, Vianney Cortés-González, Luis Quintana-Fernández, Daniel Martínez-Anaya, Patricia Pérez-Vera, and Cristina Villanueva-Mendoza. The relevance of the cytogenetic analysis in syndromic microphthalmia/anophthalmia. Ophthalmic Genetics, 40:584-587, Nov 2019. URL: https://doi.org/10.1080/13816810.2019.1698618, doi:10.1080/13816810.2019.1698618. This article has 1 citations and is from a peer-reviewed journal.

9. (blackburn2019variableexpressivityof pages 1-2): Patrick R. Blackburn, Cinthya J. Zepeda-Mendoza, Teresa M. Kruisselbrink, Lisa A. Schimmenti, Sixto García-Miñaur, María Palomares, Julián Nevado, María A. Mori, Guylène Le Meur, Eric W. Klee, Cédric Le Caignec, Pablo Lapunzina, Bertrand Isidor, and Dusica Babovic-Vuksanovic. Variable expressivity of syndromic bmp4-related eye, brain, and digital anomalies: a review of the literature and description of three new cases. European Journal of Human Genetics, 27:1379-1388, May 2019. URL: https://doi.org/10.1038/s41431-019-0423-4, doi:10.1038/s41431-019-0423-4. This article has 18 citations and is from a domain leading peer-reviewed journal.

10. (fox2024transforminggrowthfactor pages 1-2): Sabrina C. Fox and Andrew J. Waskiewicz. Transforming growth factor beta signaling and craniofacial development: modeling human diseases in zebrafish. Frontiers in Cell and Developmental Biology, Feb 2024. URL: https://doi.org/10.3389/fcell.2024.1338070, doi:10.3389/fcell.2024.1338070. This article has 11 citations.

11. (fernandez2016estudioclínicoepidemiológico pages 62-63): ML Martínez Fernández. Estudio clínico epidemiológico de las alteraciones cromosómicas estructurales como causa de anomalías congénitas humanas. Unknown journal, 2016.

12. (apamgarduno2019therelevanceof pages 5-5): David Apam-Garduño, Vianney Cortés-González, Luis Quintana-Fernández, Daniel Martínez-Anaya, Patricia Pérez-Vera, and Cristina Villanueva-Mendoza. The relevance of the cytogenetic analysis in syndromic microphthalmia/anophthalmia. Ophthalmic Genetics, 40:584-587, Nov 2019. URL: https://doi.org/10.1080/13816810.2019.1698618, doi:10.1080/13816810.2019.1698618. This article has 1 citations and is from a peer-reviewed journal.

13. (bonati2024contiguousgenesyndromes pages 1-2): Maria Teresa Bonati, Agnese Feresin, Paolo Prontera, Paola Michieletto, Valeria Gambacorta, Giampietro Ricci, and Eva Orzan. Contiguous gene syndromes and hearing loss: a clinical report of xq21 deletion and comprehensive literature review. Genes, 15:677, May 2024. URL: https://doi.org/10.3390/genes15060677, doi:10.3390/genes15060677. This article has 0 citations.