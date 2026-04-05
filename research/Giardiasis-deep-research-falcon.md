---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T14:03:08.389617'
end_time: '2026-04-04T14:13:43.519561'
duration_seconds: 635.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Giardiasis
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Giardiasis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Giardiasis** covering all of the
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
- **Disease Name:** Giardiasis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Giardiasis** covering all of the
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


## Comprehensive Disease Characteristics Report: Giardiasis (Infectious)

### Executive summary (current understanding)
Giardiasis is an intestinal protozoal infection caused by *Giardia duodenalis* (synonyms used in current literature: *Giardia lamblia*, *Giardia intestinalis*) that primarily colonizes the proximal small intestine and adheres to the epithelial surface without deep tissue invasion. Infection is acquired predominantly via fecal–oral transmission through contaminated water and food and is facilitated by a low infectious dose and environmentally persistent cysts. Clinical disease ranges from asymptomatic carriage to acute or prolonged diarrheal illness with malabsorption and weight loss; in children, prolonged/recurrent infection is associated with impaired growth and neurocognitive sequelae. (rossi2024protozoaninfectionsacquired pages 21-23, sosnowski2024enterictuftcell pages 52-57)

A 2024 national surveillance analysis from Germany illustrates that giardiasis remains a persistent public-health burden in high-income settings, with both imported and autochthonous transmission and clear age/sex/seasonal patterns. (hommes2024autochthonousandimported pages 1-2)

---

## 1. Disease information

### 1.1 Disease overview
Giardiasis is a gastrointestinal infectious disease caused by the flagellated protozoan *Giardia duodenalis* (also referred to as *G. lamblia*/*G. intestinalis* in many sources). Symptomatic disease commonly presents with diarrhea, abdominal pain/cramps, bloating/flatulence, nausea/vomiting, malabsorption, and weight loss; chronic infection is associated with longer-term sequelae such as growth retardation, iron-deficiency anemia, cognitive impairment, and post-infectious IBS. (rossi2024protozoaninfectionsacquired pages 21-23, sosnowski2024enterictuftcell pages 52-57)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
The requested canonical identifiers (ICD-10/ICD-11, MeSH, MONDO, OMIM, Orphanet) were not present in the retrieved full texts during this tool run, so they cannot be provided with tool-supported citations here. This is a key evidence gap for knowledge base population.

### 1.3 Synonyms and alternative names (evidence-backed)
- Giardiasis
- *Giardia duodenalis* infection
- *Giardia lamblia* infection
- *Giardia intestinalis* infection (rossi2024protozoaninfectionsacquired pages 21-23, sosnowski2024enterictuftcell pages 52-57)

### 1.4 Evidence provenance
The information summarized here is derived from aggregated disease-level resources (systematic reviews, surveillance analyses, cohort studies, and clinical trial registry records), not individual EHR patient records. (hommes2024autochthonousandimported pages 1-2, vicente2024systematicreviewof pages 5-8, gutierrez2024giardialambliarisk pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Infectious cause:** *Giardia duodenalis* (intestinal protozoan). (rossi2024protozoaninfectionsacquired pages 21-23, sosnowski2024enterictuftcell pages 52-57)

**Life stages relevant to disease/transmission:**
- Trophozoite is the luminal/epithelial-surface stage associated with symptoms.
- Cyst is the environmentally resistant, stool-shed infective stage. (rossi2024protozoaninfectionsacquired pages 21-23)

**Key transmission enabling characteristics (quantitative):** low infectious dose (~10–100 cysts; one estimate notes a single cyst may confer ~2% probability of disease), heavy shedding (one estimate cited ~2.5×10^7 cysts per year from an individual), and prolonged cyst survival in water/food (weeks to months). (rossi2024protozoaninfectionsacquired pages 21-23)

### 2.2 Risk factors (human)
**Household/environmental risk factors (birth cohort, Nicaragua; qPCR-based):**
- Earthen floors: HR 1.99 (95% CI 1.23–3.20) for first Giardia-associated AGE.
- Presence of mice: HR 3.17 (95% CI 1.43–7.00). (gutierrez2024giardialambliarisk pages 6-9, gutierrez2024giardialambliarisk pages 5-6)

**Imported vs autochthonous risk patterns (Germany surveillance, 2002–2021):**
Imported cases were common and predominantly affected adults aged 20–39 years, while autochthonous incidence was highest in young children (<5 years) and males. The authors discuss plausible links of adult male excess to sexual transmission among men who have sex with men (MSM) as a hypothesis requiring further investigation. (hommes2024autochthonousandimported pages 1-2, hommes2024autochthonousandimported pages 5-7)

**Food- and water-related exposures:** drinking untreated river/spring water and lack of handwashing are described as significant risk factors in the food/water update literature; multiple large waterborne outbreaks implicate municipal water systems. (rossi2024protozoaninfectionsacquired pages 23-24)

### 2.3 Protective factors (quantitative)
**Protective factors (birth cohort, Nicaragua):**
- Indoor toilet: aHR 0.52 (95% CI 0.29–0.92).
- Breastfeeding in the first year: aHR 0.10 (95% CI 0.02–0.57).
- Dogs/cats in the home: aHR 0.54 (95% CI 0.33–0.89).
- Hand sanitizer (crude): HR 0.22 (95% CI 0.09–0.52). (gutierrez2024giardialambliarisk pages 6-9, gutierrez2024giardialambliarisk pages 1-2)

**Context-dependent effect modification:** in the same cohort, breastfeeding ≥6 months was associated with higher incidence under very poor household sanitation (no indoor toilet plus earthen floor): HR 7.79 (95% CI 2.07–29.3). (gutierrez2024giardialambliarisk pages 1-2)

### 2.4 Gene-environment interactions
No human host genetic susceptibility loci or gene–environment interaction findings were available in the retrieved evidence set for this run.

---

## 3. Phenotypes (clinical and laboratory)

### 3.1 Core clinical phenotypes
Common symptomatic disease features include diarrhea, abdominal pain/cramps, bloating/flatulence, nausea/vomiting, malabsorption, and weight loss. (rossi2024protozoaninfectionsacquired pages 21-23, hommes2024autochthonousandimported pages 4-5)

**Symptom frequencies (Germany surveillance; autochthonous):** diarrhea 80.9%, pain 52.4%, flatulence 24.4%. (hommes2024autochthonousandimported pages 4-5)

**Childhood clinical pattern (Nicaragua birth cohort):** Giardia-associated AGE was typically mild; median diarrhea duration 5 days (IQR 3–9). Bloody stools were rare (1.0%), and vomiting and fever were less frequent than in non-Giardia AGE (vomiting 19.2% vs 26.3%; fever 31.7% vs 39.3%). (gutierrez2024giardialambliarisk pages 6-9, gutierrez2024giardialambliarisk pages 5-6)

### 3.2 Quality-of-life impact
Formal QoL instruments (e.g., EQ-5D, SF-36) were not reported in the retrieved evidence excerpts; however, longer-term morbidity (post-infectious syndromes, growth/cognitive impacts) is consistently emphasized in the reviews. (rossi2024protozoaninfectionsacquired pages 21-23, sosnowski2024enterictuftcell pages 52-57)

### 3.3 Suggested HPO terms
A curated phenotype-to-HPO mapping (with quantitative notes where available) is provided in the artifact below.

| Clinical feature (plain language) | Evidence-supported details/quantitative notes (if available) | Suggested HPO term(s) | Suggested LOINC/SNOMED lab concept (optional) | Supporting evidence citation IDs |
|---|---|---|---|---|
| Diarrhea (acute) | Core manifestation of giardiasis; in German surveillance, diarrhea was reported in 80.9% of autochthonous cases. In the Nicaraguan birth cohort, Giardia-associated AGE had median diarrhea duration 5 days (IQR 3–9). | Diarrhea (HP:0002014); Acute diarrhea (HPO: needs curation) | SNOMED CT: Diarrhea | (hommes2024autochthonousandimported pages 4-5, gutierrez2024giardialambliarisk pages 5-6) |
| Diarrhea (prolonged/persistent) | Prolonged giardiasis is emphasized in children; persistent/prolonged diarrhea is linked to ongoing carriage and chronic morbidity in cohort/review literature. | Chronic diarrhea (HP:0002028); Persistent diarrhea (HPO: needs curation) | SNOMED CT: Chronic diarrhea | (gutierrez2024giardialambliarisk pages 10-11, rossi2024protozoaninfectionsacquired pages 21-23) |
| Abdominal pain / cramps | Abdominal pain/cramps are common symptomatic features; German surveillance recorded pain in 52.4% of autochthonous cases. | Abdominal pain (HP:0002027); Abdominal cramping (HPO: needs curation) | SNOMED CT: Abdominal pain | (hommes2024autochthonousandimported pages 4-5, rossi2024protozoaninfectionsacquired pages 21-23) |
| Bloating / flatulence | Bloating is repeatedly described in review literature; flatulence occurred in 24.4% of German autochthonous cases. | Abdominal bloating (HP:0003270); Flatulence (HP:0012537) | SNOMED CT: Abdominal bloating / Flatulence | (hommes2024autochthonousandimported pages 4-5, rossi2024protozoaninfectionsacquired pages 21-23) |
| Nausea / vomiting | Nausea and vomiting are recognized manifestations; in the Nicaraguan cohort, vomiting was less common in Giardia-associated AGE than other AGE (19.2% vs 26.3%). | Nausea (HP:0002018); Vomiting (HP:0002013) | SNOMED CT: Nausea / Vomiting | (gutierrez2024giardialambliarisk pages 6-9, rossi2024protozoaninfectionsacquired pages 21-23) |
| Weight loss | Weight loss is a standard clinical feature of symptomatic giardiasis, especially with malabsorption/chronic disease. | Weight loss (HP:0001824) | SNOMED CT: Weight loss | (rossi2024protozoaninfectionsacquired pages 21-23, sosnowski2024enterictuftcell pages 52-57) |
| Malabsorption | Review literature describes malabsorption as a characteristic consequence of intestinal infection and epithelial dysfunction. | Malabsorption (HP:0002024) | SNOMED CT: Malabsorption syndrome | (rossi2024protozoaninfectionsacquired pages 21-23, sosnowski2024enterictuftcell pages 52-57) |
| Dehydration | Mentioned as part of the symptomatic clinical picture in review literature, particularly in diarrheal illness. | Dehydration (HP:0001944) | SNOMED CT: Dehydration | (amorim2024giardíasediagnósticotratamento pages 6-7) |
| Fever (uncommon) | Fever was uncommon in Giardia-associated AGE; cohort data showed fever in 31.7% of Giardia AGE vs 39.3% of non-Giardia AGE, supporting relative infrequency. | Fever (HP:0001945) | SNOMED CT: Fever | (gutierrez2024giardialambliarisk pages 6-9, gutierrez2024giardialambliarisk pages 1-2) |
| Bloody stool (rare) | Bloody stool is uncommon/rare in giardiasis; the Nicaraguan cohort reported blood in stool in 1.0% of Giardia-associated AGE episodes. | Hematochezia (HP:0002573); Blood in stool (HP:0002571) | SNOMED CT: Hematochezia | (gutierrez2024giardialambliarisk pages 6-9, gutierrez2024giardialambliarisk pages 1-2) |
| Growth retardation / stunting | Chronic/recurrent giardiasis in early childhood is associated with growth retardation/stunting in multiple recent reviews and epidemiologic studies. | Growth delay (HP:0001510); Short stature (HP:0004322); Stunted growth (HPO: needs curation) |  | (rossi2024protozoaninfectionsacquired pages 21-23, sosnowski2024enterictuftcell pages 52-57) |
| Cognitive impairment | Early-childhood giardiasis is associated with cognitive impairment/intellectual deficits in review literature. | Cognitive impairment (HP:0100543); Intellectual disability (HP:0001249) |  | (rossi2024protozoaninfectionsacquired pages 21-23, vicente2024systematicreviewof pages 1-2) |
| Iron-deficiency anemia | Chronic giardiasis has been linked to iron-deficiency anemia in review literature. | Iron deficiency anemia (HP:0001891); Anemia (HP:0001903) | LOINC: Hemoglobin [Mass/volume] in Blood; Ferritin [Mass/volume] in Serum or Plasma | (rossi2024protozoaninfectionsacquired pages 21-23) |
| Post-infectious IBS | Long-term sequelae include post-infectious irritable bowel syndrome; this is specifically noted in recent reviews and model-oriented overview text. | Abnormality of the digestive system physiology (HPO: needs curation); Irritable bowel syndrome (HPO: needs curation) | SNOMED CT: Irritable bowel syndrome | (rossi2024protozoaninfectionsacquired pages 21-23, sosnowski2024enterictuftcell pages 52-57) |
| Fatigue | Post-infectious fatigue is described among longer-term sequelae following giardiasis. | Fatigue (HP:0012378) | SNOMED CT: Fatigue | (sosnowski2024enterictuftcell pages 52-57) |
| Arthritis | Arthritis/post-infectious arthritic complications are reported among sequelae in review/model overview literature. | Arthritis (HP:0001369); Arthralgia (HP:0002829) | SNOMED CT: Arthritis | (sosnowski2024enterictuftcell pages 52-57) |


*Table: This table maps common clinical features and complications of giardiasis to suggested phenotype ontology terms, with quantitative notes where recent evidence provided them. It is useful as a starting point for disease knowledge base curation and phenotype annotation.*

---

## 4. Genetic / molecular information (host and pathogen)

### 4.1 Causal genes
Giardiasis is not a monogenic human disorder; it is an infectious disease. No host causal genes/variants were identified in the retrieved evidence.

### 4.2 Pathogen genetic structure relevant to epidemiology (assemblages)
The retrieved evidence describes **eight Giardia genetic assemblages (A–H)**, with **assemblages A and B** having broad host ranges (zoonotic potential) and being most common in humans. (sosnowski2024enterictuftcell pages 52-57)

### 4.3 Epigenetics / chromosomal abnormalities
Not applicable for human germline inheritance in this context; no relevant evidence retrieved.

---

## 5. Environmental information

### 5.1 Environmental and lifestyle risk factors
Food- and waterborne transmission is strongly supported; cysts have been detected on a broad range of foods, and ready-to-eat salads and unwashed vegetables can be contaminated at nontrivial rates (e.g., 0.5–1.8% contamination of ready-to-eat salads; up to 55% contamination in unwashed vegetables in one setting). The low infectious dose (~10 cysts) implies that incomplete washing may not reliably reduce risk below an infectious threshold. (rossi2024protozoaninfectionsacquired pages 23-24)

### 5.2 Infectious agent
*Causative pathogen:* *Giardia duodenalis* (*G. lamblia*, *G. intestinalis*). (rossi2024protozoaninfectionsacquired pages 21-23, sosnowski2024enterictuftcell pages 52-57)

---

## 6. Mechanism / pathophysiology (current understanding)

### 6.1 Causal chain (high-level)
1) Ingestion of infectious cysts (food/water/fecal–oral) → 2) excystation and emergence of trophozoites → 3) colonization/attachment at the duodenal epithelial surface (ventral adhesive disc) without invasion → 4) disruption of intestinal physiology and barrier function with downstream malabsorption and diarrheal symptoms; interactions with mucus and microbiota are implicated in both susceptibility and disease phenotype → 5) in some individuals, prolonged carriage and post-infectious sequelae. (sosnowski2024enterictuftcell pages 52-57)

### 6.2 Immune and epithelial involvement (conceptual)
The retrieved evidence emphasizes mucosal immune involvement and dysbiosis/inflammation links and highlights that Giardia can perturb epithelial barrier integrity (tight junction-associated processes) and microbiota composition/function, which may contribute to chronic consequences and metabolic perturbations. (sosnowski2024enterictuftcell pages 52-57, klimczak2024theinfluenceof pages 18-19)

**Suggested ontology anchors (need curation):**
- GO Biological Process: “intestinal epithelial barrier maintenance” (GO: needs curation); “inflammatory response” (GO: needs curation)
- CL Cell types: intestinal epithelial cell (CL:0000066), goblet cell (CL:0000160), Paneth cell (CL:0000160 needs curation), macrophage (CL:0000235) (sosnowski2024enterictuftcell pages 52-57)
- UBERON: small intestine (UBERON:0002108), duodenum (UBERON:0002114) (needs curation; anatomic sites supported conceptually) (sosnowski2024enterictuftcell pages 52-57)

---

## 7. Anatomical structures affected

### 7.1 Organ level
Primary site is the gastrointestinal tract, particularly proximal small intestine/duodenum where trophozoites attach. (sosnowski2024enterictuftcell pages 52-57)

### 7.2 Tissue/cell level
Intestinal epithelium and associated mucosal immune compartment are key interfaces; barrier function and microbiota interactions are repeatedly emphasized. (sosnowski2024enterictuftcell pages 52-57, klimczak2024theinfluenceof pages 18-19)

---

## 8. Temporal development

### 8.1 Onset
Typically acute/subacute onset after exposure, but many infections are asymptomatic. (sosnowski2024enterictuftcell pages 52-57)

### 8.2 Progression and course
The clinical course ranges from self-limited diarrheal disease to prolonged infection and post-infectious syndromes. Pediatric burden is concentrated in early life; in a Nicaraguan cohort, incidence peaked at age 12–24 months. (gutierrez2024giardialambliarisk pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent data)
**Germany (national surveillance 2002–2021; published 16 May 2024):**
- 72,318 cases reported; mean annual incidence 4.4/100,000.
- 2002–2019: 69,345 cases; 34.6–35% imported; autochthonous mean annual incidence 3.1/100,000.
- Highest incidence in children <5 years (up to 8.5/100,000 in a year) and elevated incidence in adults 20–55; imported cases concentrated in adults 20–39.
- Declining trend after 2013 and sharp decline in 2020–21.
- Clinical severity: hospitalization was 11.5% among autochthonous cases; three deaths in 2002–19 (0.01%). (hommes2024autochthonousandimported pages 1-2, hommes2024autochthonousandimported pages 2-4)

**Global estimates and outbreak burden (review-level):**
- ~180 million symptomatic infections annually reported in a 2024 food/water update; another source notes symptomatic disease affects ~280 million annually.
- >140 waterborne outbreaks (2011–2017) cited; foodborne cases estimated ~23.2 million annually (likely underestimated). (rossi2024protozoaninfectionsacquired pages 21-23, sosnowski2024enterictuftcell pages 52-57)

**Pediatric cohort (Nicaragua; published Nov 2024):**
- Giardia detected in 7.5% of AGE episodes (104/1,385).
- 15.6% of children had ≥1 Giardia-associated AGE episode; 36.2% of infected children had recurrent episodes.
- Incidence of first Giardia-associated AGE 6.8 per 100 child-years (95% CI 4.5–9.1), peaking at 13.9/100 child-years at 12–24 months. (gutierrez2024giardialambliarisk pages 5-6, gutierrez2024giardialambliarisk pages 1-2)

### 9.2 Human inheritance
Not applicable (infectious etiology).

---

## 10. Diagnostics

### 10.1 Diagnostic modalities (current practice)
A 2024 systematic review on giardiasis diagnostics highlights the continued central role of microscopy/concentration methods and increasing use of immunoassays and PCR/NAAT, with tradeoffs between cost/infrastructure and analytic performance. (vicente2024systematicreviewof pages 1-2)

**Microscopy:** widely used; sensitivity limited by intermittent shedding; improved by concentration (e.g., Ritchie) and by collecting multiple stool samples. The review notes direct exam false-negative rate 42% vs 14% for concentration and that collecting three samples across days can raise sensitivity to ~94% vs ~50–70% for a single sample. (vicente2024systematicreviewof pages 10-11)

**Performance ranges (compiled across studies):**
- Direct stool microscopy sensitivity ~34.7–55%, specificity 96–100%.
- Concentration methods sensitivity ~65.2–83%.
- Antigen detection sensitivity 44–100%, specificity 68–100% (one cited ELISA 95–100% sensitivity and 100% specificity).
- Molecular assays sensitivity 58–92%, specificity 56–100% (one cited average 92% sensitivity and 100% specificity). (amal2024epidemiologicalstudyof pages 59-62)

**Molecular assays caveats:** PCR inhibitors and DNA degradation can yield false negatives; negative PCR does not fully exclude infection. Cost and infrastructure limit adoption in low-resource settings. (vicente2024systematicreviewof pages 10-11, vicente2024systematicreviewof pages 1-2)

### 10.2 Differential diagnosis and formal diagnostic criteria
Differential diagnosis and formal clinical criteria were not explicitly detailed in the retrieved excerpts; additional guideline retrieval would be needed for a knowledge base entry.

---

## 11. Outcome / prognosis
Mortality is generally low; German surveillance reported three acute giardiasis deaths in 2002–2019 (0.01% of specified cases). Morbidity can be substantial via prolonged diarrhea and longer-term sequelae such as growth retardation and cognitive effects. (hommes2024autochthonousandimported pages 2-4, rossi2024protozoaninfectionsacquired pages 21-23)

---

## 12. Treatment

### 12.1 Standard pharmacotherapy
A 2024 treatment update describes 5-nitroimidazoles as the most effective therapies, specifically naming metronidazole and tinidazole: “El tratamiento más eficaz son los 5-nitroimidazoles, en concreto el metronidazol y el tinidazol.” Tinidazole’s advantage is single-dose administration. (sanchez2024actualizacióndeltratamiento pages 1-6, sanchez2024actualizacióndeltratamiento pages 6-12)

Other agents described as alternative/second-line options (particularly after treatment failure) include albendazole/mebendazole, nitazoxanide, furazolidone, paromomycin, chloroquine, and quinacrine/mepacrine. (sanchez2024actualizacióndeltratamiento pages 1-6, thakur2024perspectivesonthe pages 4-6)

### 12.2 Refractory/resistant giardiasis (recent synthesis)
Recent treatment-oriented literature emphasizes increasing refractory disease: one cited study reported 5.8% failure across regimens involving nitroimidazoles, and another series documented metronidazole-refractory cases rising from 15% to >40% (2008–2013). Quinacrine is described as an option used in some countries for metronidazole non-responders but limited by adverse effects including vomiting and psychosis. (thakur2024perspectivesonthe pages 4-6)

Combination therapy is referenced, including metronidazole + albendazole as a combined approach discussed in the 2024 treatment update. (sanchez2024actualizacióndeltratamiento pages 1-6)

### 12.3 Emerging / experimental therapies and clinical trials
**Auranofin (repurposing; Phase IIa RCT):** ClinicalTrials.gov NCT02736968 (sponsor NIAID) is a completed, randomized, placebo-controlled Phase IIa trial. Giardiasis dosing was auranofin 6 mg orally once daily for 5 days. Primary endpoints included diarrhea resolution (<3 loose stools/24h) by Day 5 plus parasitological response (negative microscopy and/or antigen). Results were submitted 2022-11-17 and first posted 2023-01-26 in the registry, but outcome values were not present in the retrieved text chunks for this report. (NCT02736968 chunk 1, NCT02736968 chunk 2)

### 12.4 Suggested MAXO terms (needs curation)
- Antiprotozoal therapy (MAXO: needs curation)
- Oral metronidazole therapy (MAXO: needs curation)
- Oral tinidazole therapy (MAXO: needs curation)
- Stool diagnostic testing / NAAT (MAXO: needs curation)

---

## 13. Prevention

### 13.1 Primary prevention (WASH, food/water)
Key prevention principles supported by the evidence include improving sanitation and hygiene (handwashing), ensuring safe drinking water, and reducing food contamination. The low infectious dose (≈10 cysts) and prolonged environmental survival amplify the importance of water treatment and safe food handling. (sosnowski2024enterictuftcell pages 52-57, rossi2024protozoaninfectionsacquired pages 23-24)

Quantitative foodborne contamination and QMRA data in a 2024 update include: ready-to-eat salad contamination 0.5–1.8% in some studies; unwashed vegetables up to 55% in one setting; QMRA annual infection risk estimate 0.36 and 1.0% probability of illness from locally grown vegetables (as cited). (rossi2024protozoaninfectionsacquired pages 23-24)

### 13.2 Secondary prevention (early detection)
Use of more sensitive tests (antigen assays and PCR/NAAT) is recommended when symptoms persist despite negative microscopy, and collecting multiple stool specimens improves diagnostic sensitivity. (vicente2024systematicreviewof pages 10-11, vicente2024systematicreviewof pages 1-2)

### 13.3 Tertiary prevention (preventing complications)
Cohort evidence suggests modifiable household factors associated with reduced childhood burden (indoor toilet; breastfeeding in first year) and supports integrated public-health strategies that reduce early-life infection risk and recurrence. (gutierrez2024giardialambliarisk pages 1-2)

---

## 14. Other species / natural disease (One Health)
Giardia infects multiple mammalian hosts, including humans, dogs, cats, cattle and rodents, and zoonotic assemblages A and B have broad host ranges. Environmental contamination routes and animal reservoirs are supported by genotyping links (e.g., assemblage B shared between humans, a dog, and lettuce; beavers implicated in waterborne outbreaks). (sosnowski2024enterictuftcell pages 52-57, rossi2024protozoaninfectionsacquired pages 23-24)

---

## 15. Model organisms
A commonly used experimental model is *Giardia muris* infection in mice; the retrieved evidence notes this murine strain has been used experimentally since the 1960s and has a similar life cycle to *G. duodenalis*. Germ-free and conventional mouse models are used to study host–microbial dynamics and immune responses. (sosnowski2024enterictuftcell pages 52-57)

---

## Key structured summary tables

### Cross-domain key facts table
| Domain | Key findings | Best supporting source (DOI/URL, year) | Evidence citation ID |
|---|---|---|---|
| Pathogen / names | Giardiasis is caused by the intestinal protozoan *Giardia duodenalis*; common synonyms in the retrieved literature include *G. lamblia* and *G. intestinalis*. Human-infecting assemblages are mainly A and B; the parasite colonizes the proximal small intestine and attaches without mucosal invasion. | Gutiérrez & Bartelt, *Curr Trop Med Rep* (2024), https://doi.org/10.1007/s40475-024-00314-2; Hatam-Nahavandi et al., *Gut Pathog* (2024), https://doi.org/10.1186/s13099-024-00666-0 | (sosnowski2024enterictuftcell pages 52-57, rossi2024protozoaninfectionsacquired pages 21-23) |
| Transmission / infectious dose / shedding / survival | Food- and waterborne transmission is central. Infectious dose is low at about 10–100 cysts; one estimate gives a single cyst about a 2% probability of causing disease. Cysts can survive weeks to months in water/food, tolerate low temperatures, and their small size (8–12 μm) can allow passage through sand filters. One study cited in the review estimated ~2.5×10^7 cysts shed annually by one individual. | Rossi et al., preprint (2024), https://doi.org/10.20944/preprints202403.1207.v1 | (rossi2024protozoaninfectionsacquired pages 21-23) |
| Key clinical manifestations / sequelae | Typical manifestations: diarrhea, bloating, abdominal cramps/pain, nausea, vomiting, malabsorption, and weight loss. Important long-term sequelae reported across reviews include growth retardation/stunting, iron-deficiency anemia, cognitive impairment, post-infectious irritable bowel syndrome, fatigue, and arthritis. In German surveillance, common autochthonous-case symptoms were diarrhea 80.9%, pain 52.4%, and flatulence 24.4%. | Hommes et al., *Eurosurveillance* (2024), https://doi.org/10.2807/1560-7917.es.2024.29.20.2300509; Rossi et al. (2024), https://doi.org/10.20944/preprints202403.1207.v1 | (hommes2024autochthonousandimported pages 4-5, rossi2024protozoaninfectionsacquired pages 21-23) |
| Epidemiology: global burden | Review-level estimates in the retrieved evidence report ~180 million symptomatic infections annually worldwide; another retrieved source notes symptomatic disease affects ~280 million people annually. Giardiasis was ranked 11th in the FAO/WHO intestinal parasite risk list; >140 waterborne outbreaks were noted for 2011–2017, and ~23.2 million foodborne cases annually were cited as likely underestimated. | Rossi et al., preprint (2024), https://doi.org/10.20944/preprints202403.1207.v1 | (rossi2024protozoaninfectionsacquired pages 21-23, sosnowski2024enterictuftcell pages 52-57) |
| Epidemiology: Germany surveillance | Germany reported 72,318 cases from 2002–2021, mean annual incidence 4.4/100,000. From 2002–2019, 69,345 cases were reported; 34.6–35% were imported and autochthonous incidence averaged 3.1/100,000. Highest incidence occurred in young children (<5 years) and in adults 20–39 years for imported cases. Incidence declined after 2013 and dropped sharply in 2020–2021. | Hommes et al., *Eurosurveillance* (2024), https://doi.org/10.2807/1560-7917.es.2024.29.20.2300509 | (hommes2024autochthonousandimported pages 1-2, hommes2024autochthonousandimported pages 2-4) |
| Diagnostics: microscopy / concentration | Microscopy remains widely used and practical, but sensitivity is limited by intermittent shedding and operator dependence. Reported ranges from the retrieved evidence: direct stool microscopy sensitivity ~34.7–55% with specificity 96–100%; stool concentration methods improve sensitivity to ~65.2–83%. Collecting three stools across days can raise sensitivity to ~94% vs ~50–70% for a single sample. In Vicente et al., many microscopy studies reported sensitivity 60–89% and specificity often high. | Vicente et al., *Diagnostics* (2024), https://doi.org/10.3390/diagnostics14040364 | (vicente2024systematicreviewof pages 5-8, vicente2024systematicreviewof pages 10-11, amal2024epidemiologicalstudyof pages 59-62) |
| Diagnostics: antigen tests / ELISA / ICA | Antigen tests are generally more sensitive than routine microscopy and faster to run. Reported ranges in retrieved evidence: antigen detection sensitivity 44–100% and specificity 68–100%; one GSA65 ELISA reported 95–100% sensitivity and 100% specificity and detected ~30% more cases than microscopy. In Vicente et al., immunoassays commonly showed sensitivity 60–89% and specificity 80–99%, while RIDAQUICK immunochromatography often showed sensitivity 81–100% and specificity 81–100%. | Vicente et al., *Diagnostics* (2024), https://doi.org/10.3390/diagnostics14040364 | (vicente2024systematicreviewof pages 5-8, vicente2024systematicreviewof pages 8-10, amal2024epidemiologicalstudyof pages 59-62) |
| Diagnostics: PCR / NAAT | Molecular assays (PCR/qPCR/NAAT) generally provide the highest sensitivity/specificity in the retrieved evidence, but performance varies by target and stool inhibitors can cause false negatives. Reported ranges: molecular sensitivity 58–92% and specificity 56–100%; one cited study reported average 92% sensitivity and 100% specificity. Vicente et al. summarize many molecular studies with 90–99% sensitivity in 32% of articles and 100% sensitivity in 24% of articles. | Vicente et al., *Diagnostics* (2024), https://doi.org/10.3390/diagnostics14040364 | (vicente2024systematicreviewof pages 5-8, vicente2024systematicreviewof pages 10-11, amal2024epidemiologicalstudyof pages 59-62) |
| Treatments: first-line and alternatives | First-line therapy in the retrieved 2024 treatment reviews is the 5-nitroimidazole class, especially metronidazole and tinidazole; tinidazole has the convenience of single-dose treatment. Alternatives/second-line options mentioned include albendazole, mebendazole, nitazoxanide, furazolidone, paromomycin, quinacrine/mepacrine, chloroquine, and secnidazole. | Sánchez (2024), source retrieved in review corpus; Thakur et al. (2024), https://doi.org/10.5772/intechopen.1005559 | (sanchez2024actualizacióndeltratamiento pages 1-6, thakur2024perspectivesonthe pages 4-6, sanchez2024actualizacióndeltratamiento pages 6-12) |
| Treatments: refractory / resistance | Drug-refractory disease is increasingly recognized. Retrieved evidence cites metronidazole treatment failure in 5.8% in one study and reports of metronidazole-refractory cases increasing from 15% to >40% between 2008–2013 in another series. Quinacrine is used in some countries for metronidazole-refractory cases but is limited by adverse effects including vomiting and psychosis. Combination therapy after nitroimidazole failure is referenced; metronidazole + albendazole is specifically identified in a 2024 treatment review. | Thakur et al. (2024), https://doi.org/10.5772/intechopen.1005559; Sánchez (2024) | (thakur2024perspectivesonthe pages 4-6, thakur2024perspectivesonthe pages 15-17, sanchez2024actualizacióndeltratamiento pages 1-6) |
| Emerging / trial therapy | Auranofin has reached clinical testing. NCT02736968 was a completed Phase IIa randomized, single-blinded, placebo-controlled trial sponsored by NIAID; giardiasis dosing was 6 mg orally once daily for 5 days. Primary outcomes included clinical diarrhea resolution and parasitological response by Day 5; results were posted to ClinicalTrials.gov in 2023, but the retrieved record excerpts did not include outcome values. | ClinicalTrials.gov NCT02736968 (first posted 2016; results posted 2023), https://clinicaltrials.gov/study/NCT02736968 | (NCT02736968 chunk 1, NCT02736968 chunk 2) |
| Prevention / protective factors | Prevention themes in the retrieved evidence center on safe water, sanitation, hygiene, and limiting food/water exposure. In the Nicaraguan birth cohort, protective factors for first Giardia-associated AGE included an indoor toilet (aHR 0.52, 95% CI 0.29–0.92), breastfeeding in the first year (aHR 0.10, 95% CI 0.02–0.57), hand sanitizer use (HR 0.22, 95% CI 0.09–0.52), and household dogs/cats (aHR 0.54, 95% CI 0.33–0.89). Risk factors included earthen floors (HR 1.99, 95% CI 1.23–3.20), mice in the house (HR 3.17, 95% CI 1.43–7.00), and poor sanitation. | Gutiérrez et al., *PLOS Negl Trop Dis* (2024), https://doi.org/10.1371/journal.pntd.0012230 | (gutierrez2024giardialambliarisk pages 6-9, gutierrez2024giardialambliarisk pages 5-6, gutierrez2024giardialambliarisk pages 1-2) |
| Pediatric burden / age distribution | In the Nicaraguan birth cohort, 104/1,385 AGE episodes (7.5%) were Giardia-positive; 69/443 children (15.6%) had ≥1 episode and 36.2% of infected children had recurrent episodes. Incidence of first Giardia-associated AGE was 6.8/100 child-years overall and peaked at 13.9/100 child-years in ages 12–24 months. Episodes were typically mild, with blood in stool uncommon and lower vomiting/fever frequencies than AGE without Giardia. | Gutiérrez et al., *PLOS Negl Trop Dis* (2024), https://doi.org/10.1371/journal.pntd.0012230 | (gutierrez2024giardialambliarisk pages 5-6, gutierrez2024giardialambliarisk pages 1-2) |
| One Health / zoonotic aspects | Assemblages A and B support both anthroponotic and zoonotic transmission; human cases with other assemblages (C–F) are also reported in the review literature. Water studies in MENA found *G. duodenalis* prevalence of 37.7% across sampled water resources, with assemblage A frequent. Reviews emphasize overlap among human, animal, and environmental reservoirs and underrecognition of waterborne transmission. | Rossi et al. (2024), https://doi.org/10.20944/preprints202403.1207.v1; Ayed et al., *J Water Health* (2024), https://doi.org/10.2166/wh.2024.107 | (rossi2024protozoaninfectionsacquired pages 21-23) |
| Model organisms / experimental systems | Common model systems in the retrieved evidence include *Giardia muris* mouse infection models and gnotobiotic/germ-free mice susceptible to diverse human-pathogenic *Giardia* assemblages. These models are used to study mucosal immunity, microbiota dependence, vaccination, and epithelial responses; other cited systems include epithelial monolayers and some veterinary/rodent models. | Ihara et al., *Infect Immun* (2024), https://doi.org/10.1128/iai.00065-24; Sosnowski (2024) | (sosnowski2024enterictuftcell pages 52-57, bretzenberger2024giardiosebeihund pages 38-42) |


*Table: This table compiles compact, high-confidence findings on giardiasis from the retrieved evidence base, including transmission biology, burden, diagnostics, treatment, prevention, and One Health/model-system context. It is designed as a quick-reference summary with quantitative values and direct evidence IDs for traceability.*

---

## Evidence gaps and curation flags (important for knowledge base use)
1) **Canonical disease identifiers** (ICD-10/11, MeSH, MONDO, OMIM/Orphanet) were not retrievable with citable evidence in this run.
2) **PMID-preferred primary literature**: Several retrieved sources provide DOIs/URLs and summarize primary studies, but PMIDs were not consistently available in the captured excerpts.
3) **Mechanism ontology mappings (GO/CL/UBERON)**: only partial, high-confidence mappings can be suggested; many require curation.
4) **Auranofin trial outcomes**: registry record confirms design and endpoints with results posted in 2023, but outcome values were not available in retrieved text chunks.

---

## Recent developments and expert analysis (2023–2024 prioritized)
- **Diagnostics:** 2024 systematic review highlights that microscopy remains widely used but that immunoassays and PCR/NAAT offer higher sensitivity, with implementation constrained by cost/infrastructure in many regions; multi-sample collection is emphasized as a practical sensitivity-improving strategy. (vicente2024systematicreviewof pages 10-11, vicente2024systematicreviewof pages 1-2)
- **Epidemiology in high-income settings:** 2024 Germany surveillance analysis demonstrates substantial autochthonous transmission (not just travel-related) and calls for investigation of dietary/behavioral/environmental drivers, including potential sexual transmission networks. (hommes2024autochthonousandimported pages 1-2, hommes2024autochthonousandimported pages 5-7)
- **Childhood risk/protection:** 2024 Nicaraguan birth-cohort data provide granular hazard ratios linking household sanitation and breastfeeding to disease burden, supporting targeted WASH and maternal/infant interventions. (gutierrez2024giardialambliarisk pages 1-2)
- **Therapeutics:** 2024 treatment reviews emphasize decades-old drug armamentarium, emerging refractory disease, and continued exploration of repurposed candidates such as auranofin. (thakur2024perspectivesonthe pages 4-6, NCT02736968 chunk 1)


References

1. (rossi2024protozoaninfectionsacquired pages 21-23): Franca Rossi, Carmela Amadoro, Serena Santonicola, Lucio Marino, and Giampaolo Colavita. Protozoan infections acquired from food or drinking water: an update. Mar 2024. URL: https://doi.org/10.20944/preprints202403.1207.v1, doi:10.20944/preprints202403.1207.v1.

2. (sosnowski2024enterictuftcell pages 52-57): OS Sosnowski. Enteric tuft cell responses and host-microbial dynamics during giardia muris infection. Unknown journal, 2024.

3. (hommes2024autochthonousandimported pages 1-2): Franziska Hommes, Achim Dörre, Susanne C. Behnke, Klaus Stark, and Mirko Faber. Autochthonous and imported giardiasis cases: an analysis of two decades of national surveillance data, germany, 2002 to 2021. Eurosurveillance, May 2024. URL: https://doi.org/10.2807/1560-7917.es.2024.29.20.2300509, doi:10.2807/1560-7917.es.2024.29.20.2300509. This article has 5 citations and is from a domain leading peer-reviewed journal.

4. (vicente2024systematicreviewof pages 5-8): Bruno Vicente, Anna De Freitas, Marcus Freitas, and Victor Midlej. Systematic review of diagnostic approaches for human giardiasis: unveiling optimal strategies. Diagnostics, 14:364, Feb 2024. URL: https://doi.org/10.3390/diagnostics14040364, doi:10.3390/diagnostics14040364. This article has 30 citations.

5. (gutierrez2024giardialambliarisk pages 1-2): Lester Gutiérrez, Nadja A. Vielot, Roberto Herrera, Yaoska Reyes, Christian Toval-Ruíz, Patricia Blandón, Rebecca J. Rubinstein, Javier Mora, Luther A. Bartelt, Filemón Bucardo, Sylvia Becker-Dreps, and Samuel Vilchez. Giardia lamblia risk factors and burden in children with acute gastroenteritis in a nicaraguan birth cohort. PLOS Neglected Tropical Diseases, 18:e0012230, Nov 2024. URL: https://doi.org/10.1371/journal.pntd.0012230, doi:10.1371/journal.pntd.0012230. This article has 4 citations and is from a domain leading peer-reviewed journal.

6. (gutierrez2024giardialambliarisk pages 6-9): Lester Gutiérrez, Nadja A. Vielot, Roberto Herrera, Yaoska Reyes, Christian Toval-Ruíz, Patricia Blandón, Rebecca J. Rubinstein, Javier Mora, Luther A. Bartelt, Filemón Bucardo, Sylvia Becker-Dreps, and Samuel Vilchez. Giardia lamblia risk factors and burden in children with acute gastroenteritis in a nicaraguan birth cohort. PLOS Neglected Tropical Diseases, 18:e0012230, Nov 2024. URL: https://doi.org/10.1371/journal.pntd.0012230, doi:10.1371/journal.pntd.0012230. This article has 4 citations and is from a domain leading peer-reviewed journal.

7. (gutierrez2024giardialambliarisk pages 5-6): Lester Gutiérrez, Nadja A. Vielot, Roberto Herrera, Yaoska Reyes, Christian Toval-Ruíz, Patricia Blandón, Rebecca J. Rubinstein, Javier Mora, Luther A. Bartelt, Filemón Bucardo, Sylvia Becker-Dreps, and Samuel Vilchez. Giardia lamblia risk factors and burden in children with acute gastroenteritis in a nicaraguan birth cohort. PLOS Neglected Tropical Diseases, 18:e0012230, Nov 2024. URL: https://doi.org/10.1371/journal.pntd.0012230, doi:10.1371/journal.pntd.0012230. This article has 4 citations and is from a domain leading peer-reviewed journal.

8. (hommes2024autochthonousandimported pages 5-7): Franziska Hommes, Achim Dörre, Susanne C. Behnke, Klaus Stark, and Mirko Faber. Autochthonous and imported giardiasis cases: an analysis of two decades of national surveillance data, germany, 2002 to 2021. Eurosurveillance, May 2024. URL: https://doi.org/10.2807/1560-7917.es.2024.29.20.2300509, doi:10.2807/1560-7917.es.2024.29.20.2300509. This article has 5 citations and is from a domain leading peer-reviewed journal.

9. (rossi2024protozoaninfectionsacquired pages 23-24): Franca Rossi, Carmela Amadoro, Serena Santonicola, Lucio Marino, and Giampaolo Colavita. Protozoan infections acquired from food or drinking water: an update. Mar 2024. URL: https://doi.org/10.20944/preprints202403.1207.v1, doi:10.20944/preprints202403.1207.v1.

10. (hommes2024autochthonousandimported pages 4-5): Franziska Hommes, Achim Dörre, Susanne C. Behnke, Klaus Stark, and Mirko Faber. Autochthonous and imported giardiasis cases: an analysis of two decades of national surveillance data, germany, 2002 to 2021. Eurosurveillance, May 2024. URL: https://doi.org/10.2807/1560-7917.es.2024.29.20.2300509, doi:10.2807/1560-7917.es.2024.29.20.2300509. This article has 5 citations and is from a domain leading peer-reviewed journal.

11. (gutierrez2024giardialambliarisk pages 10-11): Lester Gutiérrez, Nadja A. Vielot, Roberto Herrera, Yaoska Reyes, Christian Toval-Ruíz, Patricia Blandón, Rebecca J. Rubinstein, Javier Mora, Luther A. Bartelt, Filemón Bucardo, Sylvia Becker-Dreps, and Samuel Vilchez. Giardia lamblia risk factors and burden in children with acute gastroenteritis in a nicaraguan birth cohort. PLOS Neglected Tropical Diseases, 18:e0012230, Nov 2024. URL: https://doi.org/10.1371/journal.pntd.0012230, doi:10.1371/journal.pntd.0012230. This article has 4 citations and is from a domain leading peer-reviewed journal.

12. (amorim2024giardíasediagnósticotratamento pages 6-7): Marcelo Fagundes Amorim, Gabriel Braga de Castro, Pedro Henrique Santos Victoria, and Isabela Innecco Arêas. Giardíase: diagnóstico, tratamento e abordagens multidisciplinares. Revista Ibero-Americana de Humanidades, Ciências e Educação, 10:498-504, Oct 2024. URL: https://doi.org/10.51891/rease.v10i10.15915, doi:10.51891/rease.v10i10.15915. This article has 0 citations.

13. (vicente2024systematicreviewof pages 1-2): Bruno Vicente, Anna De Freitas, Marcus Freitas, and Victor Midlej. Systematic review of diagnostic approaches for human giardiasis: unveiling optimal strategies. Diagnostics, 14:364, Feb 2024. URL: https://doi.org/10.3390/diagnostics14040364, doi:10.3390/diagnostics14040364. This article has 30 citations.

14. (klimczak2024theinfluenceof pages 18-19): Sylwia Klimczak, Kacper Packi, Alicja Rudek, Sylwia Wenclewska, Marcin Kurowski, Daniela Kurczabińska, and Agnieszka Śliwińska. The influence of the protozoan giardia lamblia on the modulation of the immune system and alterations in host glucose and lipid metabolism. International Journal of Molecular Sciences, 25:8627, Aug 2024. URL: https://doi.org/10.3390/ijms25168627, doi:10.3390/ijms25168627. This article has 24 citations.

15. (hommes2024autochthonousandimported pages 2-4): Franziska Hommes, Achim Dörre, Susanne C. Behnke, Klaus Stark, and Mirko Faber. Autochthonous and imported giardiasis cases: an analysis of two decades of national surveillance data, germany, 2002 to 2021. Eurosurveillance, May 2024. URL: https://doi.org/10.2807/1560-7917.es.2024.29.20.2300509, doi:10.2807/1560-7917.es.2024.29.20.2300509. This article has 5 citations and is from a domain leading peer-reviewed journal.

16. (vicente2024systematicreviewof pages 10-11): Bruno Vicente, Anna De Freitas, Marcus Freitas, and Victor Midlej. Systematic review of diagnostic approaches for human giardiasis: unveiling optimal strategies. Diagnostics, 14:364, Feb 2024. URL: https://doi.org/10.3390/diagnostics14040364, doi:10.3390/diagnostics14040364. This article has 30 citations.

17. (amal2024epidemiologicalstudyof pages 59-62): B Amal and H Ghadir. Epidemiological study of human giardiasis at the level from the mila region correlation with parameters weather. Unknown journal, 2024.

18. (sanchez2024actualizacióndeltratamiento pages 1-6): B Cabré Sánchez. Actualización del tratamiento de giardiasis. Unknown journal, 2024.

19. (sanchez2024actualizacióndeltratamiento pages 6-12): B Cabré Sánchez. Actualización del tratamiento de giardiasis. Unknown journal, 2024.

20. (thakur2024perspectivesonthe pages 4-6): Sarika Thakur, Alka Sharma, Reena Negi, Ram Gopal Nitharwal, and Inderjeet Kaur. Perspectives on the drug discovery of intestinal protozoan parasites. Infectious Diseases, Jun 2024. URL: https://doi.org/10.5772/intechopen.1005559, doi:10.5772/intechopen.1005559. This article has 0 citations and is from a peer-reviewed journal.

21. (NCT02736968 chunk 1):  Auranofin for Giardia Protozoa. National Institute of Allergy and Infectious Diseases (NIAID). 2016. ClinicalTrials.gov Identifier: NCT02736968

22. (NCT02736968 chunk 2):  Auranofin for Giardia Protozoa. National Institute of Allergy and Infectious Diseases (NIAID). 2016. ClinicalTrials.gov Identifier: NCT02736968

23. (vicente2024systematicreviewof pages 8-10): Bruno Vicente, Anna De Freitas, Marcus Freitas, and Victor Midlej. Systematic review of diagnostic approaches for human giardiasis: unveiling optimal strategies. Diagnostics, 14:364, Feb 2024. URL: https://doi.org/10.3390/diagnostics14040364, doi:10.3390/diagnostics14040364. This article has 30 citations.

24. (thakur2024perspectivesonthe pages 15-17): Sarika Thakur, Alka Sharma, Reena Negi, Ram Gopal Nitharwal, and Inderjeet Kaur. Perspectives on the drug discovery of intestinal protozoan parasites. Infectious Diseases, Jun 2024. URL: https://doi.org/10.5772/intechopen.1005559, doi:10.5772/intechopen.1005559. This article has 0 citations and is from a peer-reviewed journal.

25. (bretzenberger2024giardiosebeihund pages 38-42): J Bretzenberger. Giardiose bei hund und katze: risikofaktoren und therapeutische optionen–eine literaturübersicht. Unknown journal, 2024.
