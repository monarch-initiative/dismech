---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T11:53:25.864633'
end_time: '2026-04-05T12:00:24.489449'
duration_seconds: 418.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Promyelocytic Leukemia, PML-RARA
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Promyelocytic Leukemia, PML-RARA
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Acute Promyelocytic Leukemia, PML-RARA** covering all of the
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
- **Disease Name:** Acute Promyelocytic Leukemia, PML-RARA
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Acute Promyelocytic Leukemia, PML-RARA** covering all of the
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


# Acute Promyelocytic Leukemia (APL) with PML::RARA fusion — Disease Characteristics Research Report

**Target disease:** Acute promyelocytic leukemia (APL) driven by the **PML::RARA** fusion (canonical t(15;17)).  
**Category:** Genetically defined subtype of acute myeloid leukemia (AML). (iyer2023thetreatmentof pages 1-2, guarnera2024acutepromyelocyticleukemialike pages 1-2)

| Field | Value | Evidence/source (author-year) | PMID/DOI/URL when available |
|---|---|---|---|
| Disease name | Acute promyelocytic leukemia (APL), PML::RARA | Iyer et al. 2023; Gill et al. 2023 (iyer2023thetreatmentof pages 1-2, gill2023acutepromyelocyticleukaemia pages 1-2) | DOI: 10.3389/fonc.2022.1062524; https://doi.org/10.3389/fonc.2022.1062524 ; DOI: 10.1186/s12885-023-10612-z; https://doi.org/10.1186/s12885-023-10612-z |
| Synonyms / alternative names | APL; acute promyelocytic leukaemia; FAB AML-M3; PML-RARα / PML::RARA-positive APL | Almeida et al. 2023; Guarnera et al. 2024 (almeida2023acutepromyelocyticleukemia pages 1-2, guarnera2024acutepromyelocyticleukemialike pages 1-2) | DOI: 10.3390/futurepharmacol3010012; https://doi.org/10.3390/futurepharmacol3010012 ; DOI: 10.3390/cancers16244192; https://doi.org/10.3390/cancers16244192 |
| Category | Acute myeloid leukemia (AML) subtype / genetically defined AML with recurrent fusion | Iyer et al. 2023; Guarnera et al. 2024 (iyer2023thetreatmentof pages 1-2, guarnera2024acutepromyelocyticleukemialike pages 1-2) | DOI: 10.3389/fonc.2022.1062524; https://doi.org/10.3389/fonc.2022.1062524 ; DOI: 10.3390/cancers16244192; https://doi.org/10.3390/cancers16244192 |
| Key molecular lesion | Balanced translocation t(15;17) generating PML::RARA fusion; fusion acts as a transcriptional repressor, blocks myeloid differentiation, and disrupts PML nuclear bodies | Iyer et al. 2023; Bercier & de Thé 2024 (iyer2023thetreatmentof pages 1-2, bercier2024historyofdeveloping pages 4-6) | DOI: 10.3389/fonc.2022.1062524; https://doi.org/10.3389/fonc.2022.1062524 ; DOI: 10.3390/cancers16071351; https://doi.org/10.3390/cancers16071351 |
| Variants / related fusions | Rare APL-like RARA fusion variants exist (e.g., PLZF::RARA / ZBTB16::RARA and other non-PML RARA fusions); some are ATO-insensitive and diagnostically important mimics | Guarnera et al. 2024; Bercier & de Thé 2024 (guarnera2024acutepromyelocyticleukemialike pages 1-2, bercier2024historyofdeveloping pages 6-7) | DOI: 10.3390/cancers16244192; https://doi.org/10.3390/cancers16244192 ; DOI: 10.3390/cancers16071351; https://doi.org/10.3390/cancers16071351 |
| Key identifiers supported in context | ICD-10: C92.4 | Matsuda et al. 2022 (not a context ID source for disease biology, but present in retrieved evidence); leave unsupported identifiers blank in this artifact context. Within context IDs, no MONDO/OMIM/Orphanet code was directly supported. (gill2023acutepromyelocyticleukaemia pages 1-2, iyer2023thetreatmentof pages 1-2) | ICD-10 C92.4 referenced in retrieved literature; disease-level context IDs do not provide additional identifier codes |
| Epidemiology: proportion of AML | ~10% of AML; also reported as ~15% of AML; review of European incidence notes 8–15% of AML | Ghiaur et al. 2024; Iyer et al. 2023; Guarnera et al. 2024 (ghiaur2024acutepromyelocyticleukemia pages 1-2, iyer2023thetreatmentof pages 1-2, guarnera2024acutepromyelocyticleukemialike pages 1-2) | DOI: 10.3390/cancers16061160; https://doi.org/10.3390/cancers16061160 ; DOI: 10.3389/fonc.2022.1062524; https://doi.org/10.3389/fonc.2022.1062524 ; DOI: 10.3390/cancers16244192; https://doi.org/10.3390/cancers16244192 |
| Epidemiology: incidence | Population-based annual incidence averaged 0.32 per 100,000 in Hong Kong cohort; European review cited incidence of 0.12 per 100,000 person-years | Gill et al. 2023; Guarnera et al. 2024 (gill2023acutepromyelocyticleukaemia pages 1-2, guarnera2024acutepromyelocyticleukemialike pages 1-2) | DOI: 10.1186/s12885-023-10612-z; https://doi.org/10.1186/s12885-023-10612-z ; DOI: 10.3390/cancers16244192; https://doi.org/10.3390/cancers16244192 |
| Hallmark complication: coagulopathy / DIC / bleeding | Characteristic aggressive coagulopathy with DIC and primary hyperfibrinolysis; severe hemorrhagic syndrome is a major cause of early death, often involving cerebral or pulmonary bleeding | Iyer et al. 2023; Almeida et al. 2023; Gill et al. 2023 (iyer2023thetreatmentof pages 1-2, almeida2023acutepromyelocyticleukemia pages 1-2, gill2023acutepromyelocyticleukaemia pages 1-2) | DOI: 10.3389/fonc.2022.1062524; https://doi.org/10.3389/fonc.2022.1062524 ; DOI: 10.3390/futurepharmacol3010012; https://doi.org/10.3390/futurepharmacol3010012 ; DOI: 10.1186/s12885-023-10612-z; https://doi.org/10.1186/s12885-023-10612-z |
| Hallmark complication: differentiation syndrome | Important treatment-related inflammatory/vasoactive syndrome during differentiation therapy (ATRA/ATO); associated with leukocytosis and can contribute to early morbidity/mortality if not rapidly recognized and treated | Iyer et al. 2023; Ghiaur et al. 2024 (iyer2023thetreatmentof pages 2-4, ghiaur2024acutepromyelocyticleukemia pages 1-2) | DOI: 10.3389/fonc.2022.1062524; https://doi.org/10.3389/fonc.2022.1062524 ; DOI: 10.3390/cancers16061160; https://doi.org/10.3390/cancers16061160 |
| Early death context | Early death remains the major obstacle to cure; real-world studies reported 30-day/very-early death burdens, including 144 early deaths in a 1991–2021 population cohort and 12.5% 7-day early death in a single-center cohort | Gill et al. 2023; Infante et al. 2023 (gill2023acutepromyelocyticleukaemia pages 1-2) | DOI: 10.1186/s12885-023-10612-z; https://doi.org/10.1186/s12885-023-10612-z ; DOI: 10.1007/s00277-023-05422-z; https://doi.org/10.1007/s00277-023-05422-z |


*Table: This table condenses the core disease-definition, molecular, epidemiologic, identifier, and complication facts for acute promyelocytic leukemia with PML::RARA. It is useful as a quick-reference artifact for populating disease knowledge-base summary fields.*

## 1. Disease information

### Overview (what is the disease?)
Acute promyelocytic leukemia (APL) is an AML subtype defined in most cases by a balanced **t(15;17)** chromosomal translocation that creates the **PML::RARA** fusion oncoprotein. This fusion enforces a differentiation block at the promyelocyte stage and is associated with a distinctive, high-risk hemorrhagic/coagulopathic presentation. (iyer2023thetreatmentof pages 1-2, bercier2024historyofdeveloping pages 4-6, gill2023acutepromyelocyticleukaemia pages 1-2)

### Common synonyms and alternative names
Commonly used names include **acute promyelocytic leukemia**, **acute promyelocytic leukaemia**, **APL**, **FAB AML-M3**, and **PML-RARα / PML::RARA-positive APL**. (almeida2023acutepromyelocyticleukemia pages 1-2, guarnera2024acutepromyelocyticleukemialike pages 1-2)

### Key identifiers and classification systems
* **ICD-10:** **C92.4** (acute promyelocytic leukemia) is used in real-world health services research for APL. (guarnera2024acutepromyelocyticleukemialike pages 1-2)
* **Molecular hallmark:** PML::RARA fusion transcript. (iyer2023thetreatmentof pages 1-2, ghiaur2024acutepromyelocyticleukemia pages 1-2)
* **MONDO / Orphanet / OMIM / MeSH:** Not directly extractable from the retrieved full-text evidence in this run; therefore not asserted here.

### Evidence source type
The available evidence includes (i) **aggregated disease-level resources** (reviews), (ii) **population-based outcomes research** (registry/cohort), and (iii) **mechanistic primary research** (cell/mouse/xenograft models). (iyer2023thetreatmentof pages 1-2, gill2023acutepromyelocyticleukaemia pages 1-2, dai2023targetinghdac3to pages 1-2)

## 2. Etiology

### Disease causal factors (genetic/mechanistic)
The primary causal lesion in classical APL is the **PML::RARA fusion** generated by **t(15;17)**, which acts as a dominant-negative regulator of retinoic acid receptor signaling and disrupts PML nuclear bodies, producing a differentiation block. (bercier2024historyofdeveloping pages 4-6, guarnera2024acutepromyelocyticleukemialike pages 1-2)

### Risk factors
Robust, population-level external risk factors (environmental/lifestyle) were not identifiable from the retrieved evidence.

However, several studies highlight **presentation severity features** that act as strong clinical risk factors for early mortality (a major outcome determinant):
* **Leukocytosis/high WBC** is repeatedly linked to higher early death risk in population-based and real-world cohorts. (gill2023acutepromyelocyticleukaemia pages 1-2, iyer2023thetreatmentof pages 2-4)
* A real-world cohort focusing on very early death reported associations with **DIC score severity** and elevated creatinine (independent predictor of 7‑day ED). (guarnera2024acutepromyelocyticleukemialike pages 1-2)

### Protective factors
No specific protective genetic or environmental factors were extractable from the retrieved evidence.

### Gene–environment interactions
No direct gene–environment interaction evidence was extractable from the retrieved evidence.

## 3. Phenotypes

### Core clinical phenotypes (human clinical)
APL typically presents as an acute leukemia with cytopenias plus a prominent **thrombo-hemorrhagic diathesis** driven by severe coagulopathy, often described as **DIC** with hyperfibrinolysis. (iyer2023thetreatmentof pages 1-2, almeida2023acutepromyelocyticleukemia pages 1-2)

**Key clinical manifestations and laboratory abnormalities** supported by the retrieved evidence:
* **Coagulopathy / DIC / hyperfibrinolysis** → major driver of early death. (iyer2023thetreatmentof pages 1-2, gill2023acutepromyelocyticleukaemia pages 1-2)
* **Severe hemorrhage**, often intracranial and pulmonary in reports/reviews. (almeida2023acutepromyelocyticleukemia pages 1-2)
* **Differentiation syndrome (DS)** as a treatment complication during differentiation therapy (ATRA/ATO), described as systemic inflammatory/vasoactive syndrome and included among causes of early morbidity/mortality. (iyer2023thetreatmentof pages 2-4, ghiaur2024acutepromyelocyticleukemia pages 1-2)
* **Typical immunophenotype** (supporting diagnosis): commonly **CD33+**, **CD13+**, **HLA‑DR negative**, and often low-frequency **CD34** expression. (guarnera2024acutepromyelocyticleukemialike pages 1-2)

### Phenotype characteristics
* **Temporal profile:** onset is typically acute/subacute (acute leukemia presentation); early deaths cluster within the first days to 30 days after diagnosis, highlighting the time-critical nature of supportive care and prompt ATRA initiation. (iyer2023thetreatmentof pages 1-2, gill2023acutepromyelocyticleukaemia pages 1-2)
* **Frequency/importance:** coagulopathy is consistently described as a hallmark feature and leading cause of early death. (iyer2023thetreatmentof pages 1-2, guarnera2024acutepromyelocyticleukemialike pages 1-2)

### Quality of life impact
Direct QoL instrument results (e.g., EQ‑5D, SF‑36, PROMIS) were not extractable from the retrieved evidence; however, real-world reviews emphasize that early mortality and acute complications can prevent patients from receiving curative therapy, and that treatment toxicities (QT prolongation, hepatic toxicity, neurotoxicity, DS) require close monitoring. (ghiaur2024acutepromyelocyticleukemia pages 1-2, guarnera2024acutepromyelocyticleukemialike pages 1-2)

### Suggested HPO terms (examples; mapping suggestions)
* **Disseminated intravascular coagulation** (HP:0001979)  
* **Thrombocytopenia** (HP:0001873)  
* **Hemorrhage** (HP:0001892) / **Intracranial hemorrhage** (HP:0002170)  
* **Hyperfibrinolysis** (HP:0003253; if used)  
* **Leukocytosis** (HP:0001974) / **Hyperleukocytosis** (HP:0001974 with qualifier)  
* **Acute myeloid leukemia** (HP:0004808)  
* **Differentiation syndrome** (not consistently represented as a single HPO term in all releases; may require synonym mapping)

## 4. Genetic / molecular information

### Causal genes and chromosomal abnormalities
* **Causal fusion:** **PML::RARA** (PML fused to retinoic acid receptor alpha, RARA) created by **t(15;17)**. (bercier2024historyofdeveloping pages 4-6, iyer2023thetreatmentof pages 1-2)
* **Disease definition:** the PML::RARA fusion is described as the hallmark/defining lesion and therapeutic target of ATRA and ATO. (ghiaur2024acutepromyelocyticleukemia pages 1-2)

### Variant fusions / molecular heterogeneity
Non-canonical **RARA fusion partners** (often termed “APL-like AML”) are rare but clinically critical because some are less sensitive/insensitive to arsenic-based therapy; a 2024 review summarizes that these entities are diagnostically challenging and heterogeneous. (guarnera2024acutepromyelocyticleukemialike pages 1-2, bercier2024historyofdeveloping pages 6-7)

### Somatic co-mutations (modifiers)
A 2024 MRD-focused review notes that co-mutations such as **FLT3, WT1, NRAS, KRAS** occur and may affect prognosis, supporting broader molecular profiling beyond the fusion transcript in some contexts. (kegyes2024mrdinacute pages 6-7)

### Epigenetic / post-translational regulation relevant to therapy response
Primary mechanistic literature and reviews converge on a pathway where ATO binding to the PML moiety drives post-translational modifications (SUMOylation/ubiquitination) leading to fusion degradation:
* A 2023 Cell Death & Differentiation study summarizes ATO-induced **SUMOylation** and **ubiquitination** of PML‑RARα (including roles for **PIAS1** and **RNF4**) as central to its degradation, and proposes **HDAC3** as a modulator of this degradative pathway (via PML‑RARα deacetylation affecting PIAS1-mediated SUMOylation). (dai2023targetinghdac3to pages 1-2)
* A 2024 historical/mechanistic review emphasizes that **PML nuclear bodies** are hubs for post-translational modifications including SUMOylation and ubiquitination and are disrupted by PML‑RARA. (bercier2024historyofdeveloping pages 6-7)

### Suggested GO terms (mechanism-related; examples)
* **GO:0003700** DNA-binding transcription factor activity (fusion TF behavior)  
* **GO:0006355** regulation of transcription, DNA-templated (altered transcriptional programs)  
* **GO:0032182** SUMOylation  
* **GO:0016567** protein ubiquitination  
* **GO:0030433** ubiquitin-dependent protein catabolic process  
* **GO:0006915** apoptosis (ATO dose-dependent apoptosis)  
* **GO:0030154** cell differentiation (ATRA-induced granulocytic differentiation)

## 5. Environmental information
No specific environmental or infectious etiologic agents were extractable from the retrieved evidence.

## 6. Mechanism / pathophysiology

### Causal chain (current understanding)
1) **Initiating lesion:** t(15;17) generates **PML::RARA**. (bercier2024historyofdeveloping pages 4-6, iyer2023thetreatmentof pages 1-2)  
2) **Nuclear/transcriptional effects:** the fusion represses RARA target gene programs and disrupts PML nuclear bodies, leading to **blocked granulocytic differentiation** and abnormal promyelocyte accumulation. (guarnera2024acutepromyelocyticleukemialike pages 1-2, bercier2024historyofdeveloping pages 4-6)  
3) **System-level clinical phenotype:** the leukemia has a characteristic **coagulopathy/DIC and bleeding** phenotype responsible for high early mortality without immediate recognition and treatment. (iyer2023thetreatmentof pages 1-2, gill2023acutepromyelocyticleukaemia pages 1-2)  
4) **Therapeutic mechanism (differentiation therapy):** ATRA and ATO directly target the molecular lesion and associated nuclear structures:
   * **ATRA** relieves PML‑RARA–driven transcriptional repression and promotes terminal differentiation. (bercier2024historyofdeveloping pages 4-6, dai2023targetinghdac3to pages 1-2)
   * **ATO** binds the PML component and promotes post-translational modification cascades that drive **PML‑RARA degradation** and restoration of functional PML nuclear bodies. (dai2023targetinghdac3to pages 1-2, bercier2024historyofdeveloping pages 6-7)

### Cellular processes / pathways highlighted by authoritative sources
A 2024 review describing “classic” APL biology states that PML::RARA “represses the transcription of RARa target genes and disrupts PML nuclear bodies, with subsequent impairment of differentiation, self-renewal, and response to DNA damage.” (guarnera2024acutepromyelocyticleukemialike pages 1-2)

### Cell types (suggested CL terms)
* **Promyelocyte** (CL:0000576) — malignant differentiation-arrested population  
* **Myeloid progenitor cell** (e.g., CL:0000763 for myeloid progenitor)  
* **Granulocyte / neutrophil lineage cells** (CL:0000775; mature differentiation outcome)

## 7. Anatomical structures affected

### Primary organs/systems
APL is a hematologic malignancy primarily involving **bone marrow** and **peripheral blood**, with secondary system involvement driven by coagulopathy/bleeding (e.g., central nervous system hemorrhage) and treatment complications. (gill2023acutepromyelocyticleukaemia pages 1-2, almeida2023acutepromyelocyticleukemia pages 1-2)

### Suggested UBERON terms
* **Bone marrow** (UBERON:0002371)  
* **Blood** (UBERON:0000178)  
* **Brain** (UBERON:0000955) — relevant due to intracranial hemorrhage emphasis

### Subcellular localization
Key disease biology centers on **nuclear bodies** (PML nuclear bodies) and nuclear transcriptional regulation. (bercier2024historyofdeveloping pages 6-7, guarnera2024acutepromyelocyticleukemialike pages 1-2)

## 8. Temporal development

### Onset and progression
Disease onset is acute, with clinically important outcomes (especially hemorrhagic deaths) occurring early after presentation/diagnosis if ATRA and supportive care are delayed. A treatment review explicitly highlights “high risk of early death without prompt initiation of treatment at first clinical suspicion.” (iyer2023thetreatmentof pages 1-2)

### Stages/course
A clinically meaningful “stage-like” construct used in practice is **risk stratification by presenting WBC (and historically platelets)** (e.g., WBC >10×10^9/L classified as high-risk in many schemas), which correlates with early death risk and guides intensity/adjunctive cytoreduction. (iyer2023thetreatmentof pages 2-4)

## 9. Inheritance and population

### Inheritance pattern
APL (PML::RARA) is a **somatic** fusion-driven leukemia; germline Mendelian inheritance is not supported by the retrieved evidence.

### Epidemiology (incidence; demographic notes)
* **Incidence:** A population-based study (1991–2021) reported annual incidence averaging **0.32 per 100,000** in its population. (gill2023acutepromyelocyticleukaemia pages 1-2)
* A 2024 review reports APL accounts for **8–15%** of AML and cites a European incidence estimate of **0.12 per 100,000 person-years**. (guarnera2024acutepromyelocyticleukemialike pages 1-2)
* Age/sex in the population-based cohort: median age **44 years** (range 1–97); 374 males/387 females. (gill2023acutepromyelocyticleukaemia pages 1-2)

## 10. Diagnostics

### Diagnostic concept
APL is a time-critical diagnosis because its defining biology creates a high immediate risk of fatal hemorrhage. Molecular confirmation is recommended, but treatment is emphasized as urgent when APL is suspected clinically. (iyer2023thetreatmentof pages 1-2, bercier2024historyofdeveloping pages 4-6)

### Clinical/pathology tests
* **Morphology:** promyelocyte accumulation in blood/marrow; may show Auer rods. (bercier2024historyofdeveloping pages 4-6)
* **Flow cytometry phenotype:** often CD33+/CD13+, HLA‑DR negative, low-frequency CD34 expression. (guarnera2024acutepromyelocyticleukemialike pages 1-2)

### Genetic/molecular diagnostics
* **RT-PCR / real-time quantitative PCR (RQ-PCR)** for detection of the APL-specific **PML::RARA** lesion is described as a route to rapid molecular confirmation, and is used for MRD monitoring in at least high-risk patients. (bercier2024historyofdeveloping pages 4-6)
* Population-based studies report use of **karyotype** plus **RT-PCR for PML‑RARA** for confirmation. (gill2023acutepromyelocyticleukaemia pages 1-2)

### MRD (measurable residual disease)
* PCR-based detection of PML‑RARA in remission can anticipate relapse; a 2024 MRD review notes that RT-PCR positivity can precede morphologic relapse by **1–4 months** and that “molecular relapse” emerged from this predictive capacity. (kegyes2024mrdinacute pages 6-7)
* A treatment review cautions that “a positive PML‑RARA PCR at count recovery does not necessarily portend resistant disease,” emphasizing interpretation in context of timing/clinical course. (iyer2023thetreatmentof pages 2-4)

## 11. Outcome / prognosis

### Modern curability contrasted with early-death risk
A 2023 treatment review states in its abstract that APL has been transformed into a “highly curable cancer with **long-term survival exceeding 90%**,” but also emphasizes that early death remains a major risk without rapid therapy. (iyer2023thetreatmentof pages 1-2)

### Real-world outcomes and early mortality statistics
* In a population-based cohort (1991–2021), there were **144 early deaths** (defined as first 30 days), with early deaths “almost exclusively” occurring in ATRA-based inductions (139/144); overall 5-year and 10-year OS were **68.1%** and **63.3%**, while post‑30‑day OS was **84.0%** and **78.1%**. (gill2023acutepromyelocyticleukaemia pages 1-2)
* Real-world observational work on very early death emphasizes the contribution of coagulopathy severity (DIC scores) to deaths before treatment initiation and within the first 7 days. (guarnera2024acutepromyelocyticleukemialike pages 1-2)

## 12. Treatment

### Treatment principles (current standard concept)
APL is the paradigm of molecularly targeted differentiation therapy: **all-trans retinoic acid (ATRA)** and **arsenic trioxide (ATO)** are directed at the PML::RARA-driven state and have enabled “chemotherapy-free” curative strategies for many patients. (iyer2023thetreatmentof pages 1-2, ghiaur2024acutepromyelocyticleukemia pages 1-2)

A 2024 review of ATRA/ATO complications states that the PML::RARA fusion is the molecular target of ATRA and ATO and that ATRA+ATO achieves “deep and durable molecular responses with a very low incidence of relapse,” while requiring monitoring for DS, hepatotoxicity, QT prolongation, and neurotoxicity. (ghiaur2024acutepromyelocyticleukemia pages 1-2)

### Key regimens and reported outcomes (selected evidence-based statistics)
* **ATRA- plus oral-ATO-based regimens in a population program:** In a 1991–2021 population-based study where oral-ATO-based regimens were implemented from 2013, oral-ATO use was associated with fewer early deaths and superior survival outcomes compared with earlier eras; reported incidence and survival statistics are summarized above. (gill2023acutepromyelocyticleukaemia pages 1-2)
* **Chemotherapy-free strategies in all-risk settings:** A randomized phase III non-inferiority study reported **complete remission 97%** in both ATRA‑ATO and ATRA‑ATO+chemotherapy arms; 2‑year DFS 98% vs 97% and EFS 95% vs 92% (all-risk); high-risk subgroup DFS 94% vs 87% and EFS 85% vs 78%. (guarnera2024acutepromyelocyticleukemialike pages 1-2)

### Supportive care implications (real-world implementation)
Population-based and real-world reviews emphasize that the gap between trial outcomes and real-world outcomes is largely driven by early mortality, delays in diagnosis/treatment, and variable expertise/resources for managing coagulopathy and complications. (guarnera2024acutepromyelocyticleukemialike pages 1-2, gill2023acutepromyelocyticleukaemia pages 1-2)

### Treatment complications
A dedicated complications review highlights that ATRA/ATO therapy, while less hematologically toxic than chemotherapy, can cause **differentiation syndrome**, **liver toxicity**, **QT interval prolongation**, and **neurotoxicity**, requiring “rigorous monitoring.” (ghiaur2024acutepromyelocyticleukemia pages 1-2)

### Suggested MAXO terms (examples; mapping suggestions)
* **All-trans retinoic acid therapy** (differentiation therapy)  
* **Arsenic trioxide therapy**  
* **Combination drug therapy** (ATRA + ATO)  
* **Supportive care for coagulopathy / transfusion support**  
* **Molecular monitoring (PCR-based MRD testing)**

## 13. Prevention
No established primary prevention strategies were extractable from the retrieved evidence, consistent with APL being largely a sporadic, somatic-fusion malignancy. Secondary/tertiary “prevention” in practice centers on **early suspicion**, immediate ATRA initiation, aggressive management of coagulopathy, and molecular MRD monitoring to detect relapse early. (iyer2023thetreatmentof pages 1-2, kegyes2024mrdinacute pages 6-7)

## 14. Other species / natural disease
No naturally occurring APL analog in non-human species was identified in the retrieved evidence.

## 15. Model organisms and experimental systems

### Cell line models
Reviews and mechanistic studies reference use of **cell lines** as core discovery tools to establish dominance of PML‑RARA and to probe response/resistance mechanisms to ATRA/ATO. (bercier2024historyofdeveloping pages 4-6, dai2023targetinghdac3to pages 1-2)

### Mouse and xenograft models
* A 2024 review notes that **transgenic mouse models expressing PML‑RARA** in the myeloid lineage can mimic APL and have been used to show that PML‑RARA can be a solitary initiating oncogenic event in appropriate contexts. (bercier2024historyofdeveloping pages 6-7)
* A 2023 mechanistic paper used **patient-derived xenograft (PDX)** approaches (including serial transfers) to test how modulating HDAC3 affects PML‑RARα degradation and therapy resistance. (dai2023targetinghdac3to pages 1-2)

### Model limitations (from available evidence)
The retrieved evidence does not provide structured limitations analyses; however, the consistent emphasis on early death/coagulopathy as a dominant real-world outcome determinant implies that animal/cell models may incompletely capture the health-system and supportive-care drivers of early mortality.

## Expert opinions and authoritative synthesis (2023–2024 prioritized)
Recent authoritative reviews converge on two major points:
1) **APL is highly curable in principle** with ATRA+ATO-based molecularly targeted therapy (often quoted as >90% long-term survival in contemporary series), making it a flagship of targeted differentiation therapy. (iyer2023thetreatmentof pages 1-2, ghiaur2024acutepromyelocyticleukemia pages 1-2)
2) **Early death remains the critical barrier** to realizing these cure rates in real-world practice; high-quality supportive care and rapid initiation of ATRA are repeatedly highlighted as key interventions to close the trial–real-world gap. (iyer2023thetreatmentof pages 1-2, guarnera2024acutepromyelocyticleukemialike pages 1-2, gill2023acutepromyelocyticleukaemia pages 1-2)

## Key recent statistics (quick list)
* Annual APL incidence average **0.32 per 100,000** in a population study (1991–2021). (gill2023acutepromyelocyticleukaemia pages 1-2)
* APL proportion of AML reported as **~8–15%** (review). (guarnera2024acutepromyelocyticleukemialike pages 1-2)
* Early deaths (first 30 days): **144** in a 1991–2021 population cohort; predominantly in ATRA-based induction era. (gill2023acutepromyelocyticleukaemia pages 1-2)
* Overall survival in that cohort: **5-year 68.1%**, **10-year 63.3%**; post‑30‑day OS: **5-year 84.0%**, **10-year 78.1%**. (gill2023acutepromyelocyticleukaemia pages 1-2)
* Chemotherapy-free ATRA‑ATO vs ATRA‑ATO+chemotherapy trial: **97% CR** in both arms; 2‑year DFS/EFS ~**98/95%** vs **97/92%** (all-risk), and high-risk DFS/EFS **94/85%** vs **87/78%**. (guarnera2024acutepromyelocyticleukemialike pages 1-2)

## References (URLs and publication dates)
The principal sources used in this report are open-access review articles and population-based studies with embedded URLs in citations, including:
* Iyer SG et al. *Frontiers in Oncology* (Jan 2023). https://doi.org/10.3389/fonc.2022.1062524 (iyer2023thetreatmentof pages 1-2, iyer2023thetreatmentof pages 2-4)
* Gill H et al. *BMC Cancer* (Feb 2023). https://doi.org/10.1186/s12885-023-10612-z (gill2023acutepromyelocyticleukaemia pages 1-2)
* Bercier P, de Thé H. *Cancers* (Mar 2024). https://doi.org/10.3390/cancers16071351 (bercier2024historyofdeveloping pages 4-6, bercier2024historyofdeveloping pages 6-7)
* Ghiaur A et al. *Cancers* (Mar 2024). https://doi.org/10.3390/cancers16061160 (ghiaur2024acutepromyelocyticleukemia pages 1-2)
* Kegyes D et al. *Cancers* (Sep 2024). https://doi.org/10.3390/cancers16183208 (kegyes2024mrdinacute pages 6-7)
* Guarnera L et al. *Cancers* (Dec 2024). https://doi.org/10.3390/cancers16244192 (guarnera2024acutepromyelocyticleukemialike pages 1-2)
* Dai B et al. *Cell Death & Differentiation* (Mar 2023). https://doi.org/10.1038/s41418-023-01139-8 (dai2023targetinghdac3to pages 1-2)
* de Almeida TD et al. *Future Pharmacology* (Feb 2023). https://doi.org/10.3390/futurepharmacol3010012 (almeida2023acutepromyelocyticleukemia pages 1-2)

References

1. (iyer2023thetreatmentof pages 1-2): Sunil Girish Iyer, Laila Elias, Michele Stanchina, and Justin Watts. The treatment of acute promyelocytic leukemia in 2023: paradigm, advances, and future directions. Frontiers in Oncology, Jan 2023. URL: https://doi.org/10.3389/fonc.2022.1062524, doi:10.3389/fonc.2022.1062524. This article has 70 citations.

2. (guarnera2024acutepromyelocyticleukemialike pages 1-2): Luca Guarnera, Emiliano Fabiani, Giulia Falconi, Giorgia Silvestrini, Maria Luigia Catanoso, Mariadomenica Divona, and Maria Teresa Voso. Acute promyelocytic leukemia-like aml: genetic perspective and clinical implications. Cancers, 16:4192, Dec 2024. URL: https://doi.org/10.3390/cancers16244192, doi:10.3390/cancers16244192. This article has 2 citations.

3. (gill2023acutepromyelocyticleukaemia pages 1-2): Harinder Gill, Radha Raghupathy, Carmen Y.Y. Lee, Yammy Yung, Hiu-Tung Chu, Michael Y. Ni, Xiao Xiao, Francis P. Flores, Rita Yim, Paul Lee, Lynn Chin, Vivian W.K. Li, Lester Au, Wing-Yan Au, Edmond S.K. Ma, Diwakar Mohan, Cyrus Rustam Kumana, and Yok-Lam Kwong. Acute promyelocytic leukaemia: population-based study of epidemiology and outcome with atra and oral-ato from 1991 to 2021. BMC Cancer, Feb 2023. URL: https://doi.org/10.1186/s12885-023-10612-z, doi:10.1186/s12885-023-10612-z. This article has 38 citations and is from a peer-reviewed journal.

4. (almeida2023acutepromyelocyticleukemia pages 1-2): Tâmara Dauare de Almeida, Fernanda Cristina Gontijo Evangelista, and Adriano de Paula Sabino. Acute promyelocytic leukemia (apl): a review of the classic and emerging target therapies towards molecular heterogeneity. Future Pharmacology, 3:162-179, Feb 2023. URL: https://doi.org/10.3390/futurepharmacol3010012, doi:10.3390/futurepharmacol3010012. This article has 10 citations.

5. (bercier2024historyofdeveloping pages 4-6): Pierre Bercier and Hugues de Thé. History of developing acute promyelocytic leukemia treatment and role of promyelocytic leukemia bodies. Cancers, 16:1351, Mar 2024. URL: https://doi.org/10.3390/cancers16071351, doi:10.3390/cancers16071351. This article has 11 citations.

6. (bercier2024historyofdeveloping pages 6-7): Pierre Bercier and Hugues de Thé. History of developing acute promyelocytic leukemia treatment and role of promyelocytic leukemia bodies. Cancers, 16:1351, Mar 2024. URL: https://doi.org/10.3390/cancers16071351, doi:10.3390/cancers16071351. This article has 11 citations.

7. (ghiaur2024acutepromyelocyticleukemia pages 1-2): Alexandra Ghiaur, Cristina Doran, Mihnea-Alexandru Gaman, Bogdan Ionescu, Aurelia Tatic, Mihaela Cirstea, Maria Camelia Stancioaica, Roxana Hirjan, and Daniel Coriu. Acute promyelocytic leukemia: review of complications related to all-trans retinoic acid and arsenic trioxide therapy. Cancers, 16:1160, Mar 2024. URL: https://doi.org/10.3390/cancers16061160, doi:10.3390/cancers16061160. This article has 17 citations.

8. (iyer2023thetreatmentof pages 2-4): Sunil Girish Iyer, Laila Elias, Michele Stanchina, and Justin Watts. The treatment of acute promyelocytic leukemia in 2023: paradigm, advances, and future directions. Frontiers in Oncology, Jan 2023. URL: https://doi.org/10.3389/fonc.2022.1062524, doi:10.3389/fonc.2022.1062524. This article has 70 citations.

9. (dai2023targetinghdac3to pages 1-2): Bo Dai, Feng Wang, Ying Wang, Jiayan Zhu, Yunxuan Li, Tingting Zhang, Lu Zhao, Li-Ling Wang, Wen-hui Gao, Jun Yu Li, A. Liang, Hongming Zhu, Ke Li, and Jiong Hu. Targeting hdac3 to overcome the resistance to atra or arsenic in acute promyelocytic leukemia through ubiquitination and degradation of pml-rarα. Cell Death & Differentiation, 30:1320-1333, Mar 2023. URL: https://doi.org/10.1038/s41418-023-01139-8, doi:10.1038/s41418-023-01139-8. This article has 33 citations and is from a domain leading peer-reviewed journal.

10. (kegyes2024mrdinacute pages 6-7): David Kegyes, Praveena S. Thiagarajan, and Gabriel Ghiaur. Mrd in acute leukemias: lessons learned from acute promyelocytic leukemia. Cancers, Sep 2024. URL: https://doi.org/10.3390/cancers16183208, doi:10.3390/cancers16183208. This article has 3 citations.
