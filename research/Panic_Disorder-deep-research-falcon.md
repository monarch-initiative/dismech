---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T17:00:53.686316'
end_time: '2026-04-24T17:31:30.479359'
duration_seconds: 1836.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Panic Disorder
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Panic Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Panic Disorder** covering all of the
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
- **Disease Name:** Panic Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Panic Disorder** covering all of the
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


# Panic Disorder — Disease Characteristics Research Report (Psychiatric)

**Target disease:** Panic disorder (PD)  
**Category:** Psychiatric (Anxiety or fear-related disorders)  
**MONDO ID:** Not identified from the retrieved sources (gap in current evidence set).  
**MeSH ID:** Not identified from the retrieved sources (gap in current evidence set).  

## Executive summary (current understanding)
Panic disorder is characterized by recurrent, unexpected panic attacks accompanied by persistent concern/worry about additional attacks or maladaptive behavioral change, and it frequently becomes chronic and recurrent, with substantial functional impairment, comorbidity, and relapse risk after treatment discontinuation. ICD-11 classifies panic disorder as **6B01** and separates it from agoraphobia (which can be diagnosed comorbidly), aligning its taxonomy more closely with DSM-5 while simplifying symptom-count requirements. Mechanistically, converging evidence supports dysfunction of distributed fear/interoceptive circuitry (amygdala–insula–PFC–brainstem/PAG–hypothalamus), with contributions from GABAergic, serotonergic, noradrenergic, glutamatergic, neuroendocrine (HPA-axis), inflammatory (e.g., IL-6), neuropeptide (orexin), and neuroplasticity (BDNF/TrkB) systems, as well as chemosensory/acid–CO2 and lactate-related pathways. Recent (2023–2025) work further supports a polygenic architecture and highlights peripheral (visceral afferent) and central neuronal cell types in genetic enrichment analyses. (domschke2025taxonomyofanxiety pages 1-2, domschke2025taxonomyofanxiety pages 3-4, moraes2024neurochemicalandgenetic pages 1-2, moraes2024neurochemicalandgenetic pages 2-3, zugliani2019pharmacologicalandneuromodulatory pages 2-3, mitchell2025genomewidemetaanalysisidentifies pages 3-10)

## 1. Disease information

### 1.1 What is the disease?
Panic disorder is defined clinically by recurrent, unexpected panic attacks with at least one attack followed by persistent concern/worry about recurrence or consequences and/or maladaptive behavioral change. DSM-style criteria summary appears in multiple clinical reviews and trial summaries. (locke2015diagnosisandmanagement pages 3-4, zugliani2019pharmacologicalandneuromodulatory pages 1-2)

### 1.2 Key identifiers and classification
Key identifiers directly supported by retrieved evidence:
- **ICD-11:** **6B01 – Panic disorder** (domschke2025taxonomyofanxiety pages 1-2)
- **ICD-10:** **F41.0 – Panic disorder [episodic paroxysmal anxiety]** (domschke2025taxonomyofanxiety pages 1-2)

ICD-11 taxonomy notes:
- Panic disorder and agoraphobia can be diagnosed **separately and comorbidly** in ICD-11. (domschke2025taxonomyofanxiety pages 1-2, domschke2025taxonomyofanxiety pages 3-4)
- ICD-11 simplifies diagnostic operationalization compared with ICD-10 by omitting strict minimum symptom-count requirements in the descriptions summarized in the retrieved taxonomy review. (domschke2025taxonomyofanxiety pages 3-4)

### 1.3 Synonyms and alternative names
- Panic disorder (PD) (domschke2025taxonomyofanxiety pages 1-2)
- Episodic paroxysmal anxiety (ICD-10 descriptor) (domschke2025taxonomyofanxiety pages 1-2)

### 1.4 Evidence-source type
The information synthesized here is derived from aggregated disease-level resources: systematic reviews/meta-analyses, large epidemiologic burden analyses, neuroimaging/network studies, and clinical trials/registries. (papola2023cbttreatmentdelivery pages 1-2, yang2021globalregionaland pages 1-2, moraes2024neurochemicalandgenetic pages 1-2)

### 1.5 Identifiers/definition artifact
| Category | Value | Key notes | Evidence |
|---|---|---|---|
| Disease name | Panic disorder | Anxiety/fear-related disorder characterized by recurrent unexpected panic attacks with persistent concern about recurrence/consequences and/or maladaptive behavioral change | (domschke2025taxonomyofanxiety pages 1-2, locke2015diagnosisandmanagement pages 3-4) |
| ICD-11 code/name | **6B01 – Panic disorder** | ICD-11 places panic disorder within **Anxiety or fear-related disorders**; agoraphobia is separated and can be diagnosed comorbidly | (domschke2025taxonomyofanxiety pages 1-2, domschke2025taxonomyofanxiety pages 3-4, walter2024psychischestörungenin pages 1-2) |
| ICD-10 code/name | **F41.0 – Panic disorder [episodic paroxysmal anxiety]** | ICD-10 wording explicitly includes the synonym “episodic paroxysmal anxiety” | (domschke2025taxonomyofanxiety pages 1-2) |
| DSM-style diagnostic summary | Recurrent, **unexpected** panic attacks; at least one attack followed by **≥1 month** of persistent worry/concern about additional attacks or their consequences, and/or significant maladaptive behavioral change; not better explained by substances, medical illness, or another mental disorder | Core panic-attack symptoms include abrupt surge of intense fear peaking within minutes, often with palpitations, sweating, trembling, dyspnea, dizziness, chest discomfort, paresthesias, etc. | (locke2015diagnosisandmanagement pages 3-4, zugliani2019pharmacologicalandneuromodulatory pages 1-2) |
| Common synonyms / alternative names | Panic disorder; Panic disorder with/without agoraphobia (historical usage in older literature); Episodic paroxysmal anxiety | “Panic attacks disorder” is **not** established in the retrieved evidence as a formal standard synonym; “panic attacks” may be coded separately in ICD-11 when isolated | (domschke2025taxonomyofanxiety pages 1-2, domschke2025[taxonomyofanxiety pages 1-2, domschke2025taxonomyofanxiety pages 3-4) |
| ICD-11 note: relation to agoraphobia | Panic disorder and agoraphobia are **distinct disorders** in ICD-11 | Unlike ICD-10’s closer linkage, ICD-11 allows separate and comorbid diagnosis, aligning more closely with DSM-5 | (domschke2025taxonomyofanxiety pages 1-2, domschke2025taxonomyofanxiety pages 3-4) |
| ICD-11 note: isolated panic attacks | ICD-11 allows coding of **isolated panic attacks** in addition to other mental or somatic disorders | This is described as consistent with DSM-5; isolated panic attacks that do not meet full panic-disorder criteria can still be coded | (domschke2025taxonomyofanxiety pages 1-2, domschke2025[taxonomyofanxiety pages 1-2) |
| ICD-11 diagnostic-guideline differences | ICD-11 simplifies operationalization relative to ICD-10 by omitting subcategorizations and strict minimum symptom-count requirements in the retrieved summaries | This may improve clinical practicality but may also affect diagnostic precision; further validation was noted as needed | (domschke2025taxonomyofanxiety pages 1-2, domschke2025taxonomyofanxiety pages 3-4) |


*Table: This table summarizes the core coding identifiers and diagnostic definition of panic disorder across ICD-11, ICD-10, and DSM-style criteria. It is useful for aligning terminology, ontology mapping, and case-definition rules in a disease knowledge base.*

## 2. Etiology

### 2.1 Disease causal factors (multifactorial)
Current evidence supports a multifactorial model combining:
- **Polygenic susceptibility** (moderate heritability and SNP-heritability; shared genetics with internalizing traits) (mitchell2025genomewidemetaanalysisidentifies pages 1-3, mitchell2025genomewidemetaanalysisidentifies pages 3-10)
- **Stress/trauma-related environmental exposures** (childhood adversities) (zhang2023associationbetweenpanic pages 1-6)
- **Neurobiological mechanisms** involving fear circuitry, interoception, neuroendocrine and immune signaling, and chemosensory/metabolic sensitivity (moraes2024neurochemicalandgenetic pages 1-2, moraes2024neurochemicalandgenetic pages 2-3)

### 2.2 Risk factors
#### Genetic risk factors
Family-based evidence summarized in a 2024 systematic review indicates increased familial aggregation, with one cited study reporting ~25% of first-degree relatives diagnosed and up to threefold higher prevalence among first-degree relatives, with stronger familiality for a respiratory subtype. (moraes2024neurochemicalandgenetic pages 1-2)

A large GWAS meta-analysis (preprint) reports that panic disorder is diagnosed in **~2–4%** and provides twin/family heritability estimates in the **40–50%** range for panic disorder (contextualized as background). (mitchell2025genomewidemetaanalysisidentifies pages 1-3)

GWAS/meta-analytic findings:
- “First genome-wide significant loci” for panic attacks and panic disorder were reported (16 loci for panic attacks; 7 loci for panic disorder), and panic attack vs panic disorder genetic correlation was extremely high (**rg = 1.00, S.E. = 0.01**). (mitchell2025genomewidemetaanalysisidentifies pages 1-3)
- SNP heritability (liability scale, prevalence assumptions) estimated **8–15% for panic disorder** (and 11–18% for panic attacks), with higher raw estimates in the largest cohort (10–20% for panic disorder). (mitchell2025genomewidemetaanalysisidentifies pages 1-3, mitchell2025genomewidemetaanalysisidentifies pages 3-10)
- Strong genetic correlations with anxiety disorders (**rg = 0.90–0.94**), major depression (**rg = 0.78–0.84**), PTSD symptoms (**rg = 0.63–0.67**), and neuroticism (**rg = 0.62–0.66**). (mitchell2025genomewidemetaanalysisidentifies pages 3-10, mitchell2025genomewidemetaanalysisidentifies pages 10-15)

Candidate genes highlighted in the 2024 systematic review include **NPSR1, HTR1A, SLC6A2**, consistent with roles in arousal/anxiety and monoaminergic signaling. (moraes2024neurochemicalandgenetic pages 3-4)

#### Environmental and psychosocial risk factors
- **Adverse childhood experiences (ACEs):** Meta-analysis (34 studies; 192,182 participants) reported an overall association between ACEs and PD with pooled **OR = 2.2 (CI 1.82–2.58)**; specific ACEs included sexual abuse (OR 1.92), physical abuse (OR 1.71), parental alcoholism (OR 1.83), parental separation/loss (OR 1.82). (zhang2023associationbetweenpanic pages 1-6)
- **Smoking:** A 2023 VBM study notes cigarette smoking increases likelihood of developing anxiety disorders including PD and that PD patients who smoke can show different structural brain patterns; PD-associated gray matter reductions in amygdala/hippocampus were driven by non-smokers and absent in smoking subjects, indicating smoking may confound/modulate PD neuroimaging markers. (kunas2023themodulatingimpact pages 1-2)
- **Triggers and modifiers in clinical practice:** Caffeine, stimulants, nicotine and medication/substance factors may trigger or exacerbate panic symptoms; clinical sources also emphasize that medical illnesses and medications can mimic panic symptoms and must be excluded. (locke2015diagnosisandmanagement pages 3-4)

### 2.3 Protective factors
Protective factors specific to panic disorder were not quantitatively addressed in the retrieved primary literature set. (Evidence gap)

### 2.4 Gene–environment interactions
Direct gene×environment interaction results specific to panic disorder were not present in the retrieved evidence set. (Evidence gap)

## 3. Phenotypes

### 3.1 Core phenotype set (with suggested HPO mappings)
Panic disorder phenotypes include recurrent unexpected panic attacks, anticipatory anxiety, avoidance/agoraphobic behavior, and prominent autonomic/somatic symptoms such as palpitations and dyspnea, contributing to substantial functional impairment and QoL reduction. (zugliani2019pharmacologicalandneuromodulatory pages 1-2, kim2021functionalimpairmentin pages 1-2)

Key quantitative phenotype/course features:
- Recurrence reported as **56%** (PD without agoraphobia) and **58%** (PD with agoraphobia) in a VR-assessment feasibility paper summarizing prior literature. (kim2023feasibilityofthe pages 1-2)
- Relapse after medication discontinuation reported as **25–50% within 6 months** in a treatment-trials review. (zugliani2019pharmacologicalandneuromodulatory pages 1-2)
- Median age of onset reported as **32 years** in a concentrated CBT implementation study. (iversen2022thebergen4day pages 1-2)

Phenotype artifact (HPO suggestions + quantified features):
| Phenotype (plain language) | Suggested HPO term(s) | Notes on frequency/severity/course | Supporting evidence with quantitative stats | Key sources |
|---|---|---|---|---|
| Recurrent unexpected panic attacks | HP: recurrent panic attacks; HP: anxiety attack | Core defining feature; abrupt, episodic surges of fear with autonomic/cognitive symptoms; often chronic/recurrent if untreated | DSM-style definition requires recurrent unexpected attacks; lifetime prevalence of panic disorder reported as 1.6–2.2% in one review and ~2–5% in broader literature (zugliani2019pharmacologicalandneuromodulatory pages 1-2, zhang2023associationbetweenpanic pages 1-6) | (zugliani2019pharmacologicalandneuromodulatory pages 1-2, locke2015diagnosisandmanagement pages 3-4, zhang2023associationbetweenpanic pages 1-6) |
| Persistent worry about more attacks or their consequences | HP: anticipatory anxiety; HP: excessive worry | Required for diagnosis when present for ≥1 month after an attack; contributes to chronicity and avoidance | DSM-style criteria specify ≥1 month of persistent concern/worry or maladaptive behavioral change after an attack (locke2015diagnosisandmanagement pages 3-4, zugliani2019pharmacologicalandneuromodulatory pages 1-2) | (locke2015diagnosisandmanagement pages 3-4, zugliani2019pharmacologicalandneuromodulatory pages 1-2) |
| Maladaptive behavioral change / avoidance after attacks | HP: avoidance behavior; HP: agoraphobia; HP: maladaptive behavior | Common downstream phenotype; may include avoiding exercise, crowds, public places, or situations associated with bodily sensations | ICD-11/DSM-aligned summaries emphasize maladaptive behavioral change; 76.7% of one clinical sample had panic disorder with agoraphobia (domschke2025taxonomyofanxiety pages 1-2, iversen2022thebergen4day pages 1-2) | (domschke2025taxonomyofanxiety pages 1-2, iversen2022thebergen4day pages 1-2, locke2015diagnosisandmanagement pages 3-4) |
| Palpitations / racing heart | HP: palpitations | One of the most common somatic symptoms during attacks; part of autonomic arousal profile | Palpitations noted as the most common physical symptom in primary-care diagnostic review; panic attacks also associated with altered breathing and heart-rate physiology (locke2015diagnosisandmanagement pages 3-4, mitchell2025genomewidemetaanalysisidentifies pages 10-15) | (locke2015diagnosisandmanagement pages 3-4, mitchell2025genomewidemetaanalysisidentifies pages 10-15) |
| Dyspnea / shortness of breath / hyperventilation | HP: dyspnea; HP: hyperventilation | Prominent somatic symptom; relevant for respiratory/interoceptive subtype and differential diagnosis | Panic disorder commonly presents with dyspnea; VR paradigms and mechanistic work highlight hyperventilation and respiratory triggers; CO2 sensitivity is implicated mechanistically (kim2023feasibilityofthe pages 1-2, zugliani2019pharmacologicalandneuromodulatory pages 2-3, moraes2024neurochemicalandgenetic pages 1-2) | (kim2023feasibilityofthe pages 1-2, zugliani2019pharmacologicalandneuromodulatory pages 2-3, moraes2024neurochemicalandgenetic pages 1-2) |
| Dizziness / lightheadedness | HP: dizziness | Common acute symptom; important in medical differential diagnosis | Narrative review of somatic symptoms identifies dizziness among common and clinically important panic symptoms (locke2015diagnosisandmanagement pages 3-4) | (locke2015diagnosisandmanagement pages 3-4) |
| Chest discomfort / chest pain | HP: chest pain | Common panic symptom; major contributor to emergency/medical presentations | Biobehavioral review highlights non-cardiac chest pain as one of the key somatic symptoms that mimic medical illness in panic disorder (locke2015diagnosisandmanagement pages 3-4) | (locke2015diagnosisandmanagement pages 3-4) |
| Paresthesias / tingling / numbness | HP: paresthesia | Episodic somatic manifestation during attacks | Listed among frequent panic-attack somatic symptoms in diagnostic and differential review literature (locke2015diagnosisandmanagement pages 3-4) | (locke2015diagnosisandmanagement pages 3-4) |
| Fear in enclosed/public places and escape-related avoidance | HP: agoraphobia; HP: claustrophobia-like fear | Often associated with panic disorder; may worsen disability and chronicity | In one implementation study, 76.7% had PD with agoraphobia; VR assessment modules used elevator/daily-environment exposure to capture these symptoms (iversen2022thebergen4day pages 1-2, kim2023feasibilityofthe pages 1-2) | (iversen2022thebergen4day pages 1-2, kim2023feasibilityofthe pages 1-2) |
| Heightened interoceptive sensitivity / misinterpretation of bodily sensations | HP: abnormality of interoception; HP: somatic anxiety | Mechanistically important and clinically linked to panic severity; can amplify autonomic sensations into panic | Large genomic study describes “heightened awareness and misinterpretation of bodily sensations”; insula-centered network abnormalities and interoceptive exposure paradigms support this phenotype (mitchell2025genomewidemetaanalysisidentifies pages 10-15, you2024abnormalinsulanetwork pages 14-19) | (mitchell2025genomewidemetaanalysisidentifies pages 10-15, you2024abnormalinsulanetwork pages 14-19) |
| Functional impairment in work, social, and family life | HP: impaired social functioning; HP: reduced ability to work; HP: impaired family functioning | Major quality-of-life phenotype; often persists beyond acute attacks | In 267 PD patients, higher PDSS, depression, and anxiety sensitivity scores correlated with greater impairment; PDSS and ASI-R predicted lost and underproductive days (kim2021functionalimpairmentin pages 1-2) | (kim2021functionalimpairmentin pages 1-2) |
| Depressive symptoms / depressed mood comorbidity | HP: depressed mood | Common comorbidity that worsens impairment, autonomic dysregulation, and course | In one 30-patient clinic implementation sample, 56.7% had comorbid depression; broader reviews note frequent mood-disorder comorbidity (iversen2022thebergen4day pages 1-2, locke2015diagnosisandmanagement pages 3-4) | (iversen2022thebergen4day pages 1-2, locke2015diagnosisandmanagement pages 3-4) |
| Generalized anxiety and other anxiety disorder comorbidity | HP: generalized anxiety; HP: anxiety | Very common; may increase severity and complicate diagnosis/treatment | 80.4% of people with PD had comorbid anxiety, mood, or substance use disorders in one review; in one sample, 16.7% had GAD and 66.7% had any psychiatric comorbidity (zhang2023associationbetweenpanic pages 1-6, iversen2022thebergen4day pages 1-2) | (zhang2023associationbetweenpanic pages 1-6, iversen2022thebergen4day pages 1-2) |
| PTSD comorbidity / trauma-related symptoms | HP: posttraumatic stress symptoms | Bidirectionally associated with panic disorder; may mark more severe course | About 69% of individuals seeking treatment for PTSD met current criteria for panic attacks; PTSD predicted subsequent PD onset (HR=1.601), and PD predicted later PTSD (HR=1.210) (berenz2019timecourseof pages 1-3) | (berenz2019timecourseof pages 1-3) |
| Chronic/recurrent course | HP: recurrent episodes; HP: chronic course | Long-term recurrence and persistence are common | Recurrence rates reported as 56% for PD without agoraphobia and 58% for PD with agoraphobia; up to 30% may remain with full disorder after 3–6 years (kim2023feasibilityofthe pages 1-2, zugliani2019pharmacologicalandneuromodulatory pages 1-2) | (kim2023feasibilityofthe pages 1-2, zugliani2019pharmacologicalandneuromodulatory pages 1-2) |
| Relapse after treatment discontinuation | HP: disease relapse | Important temporal phenotype affecting prognosis and management | 25–50% relapse within 6 months after drug discontinuation in treatment review (zugliani2019pharmacologicalandneuromodulatory pages 1-2) | (zugliani2019pharmacologicalandneuromodulatory pages 1-2) |
| Adult onset | HP: adult onset | Usually adult-onset, though anxiety vulnerability can begin earlier; onset often in early/mid-adulthood | Median age of onset reported as 32 years in one implementation study; mean age in that clinical sample was 38.0 years (iversen2022thebergen4day pages 1-2) | (iversen2022thebergen4day pages 1-2) |
| Residual phobic/panic symptoms despite treatment | HP: residual symptoms; HP: persistent anxiety | Common even after partial response; contributes to reduced QoL | Treatment review notes residual panic/phobic symptoms are common and 20–40% do not fully respond to pharmacotherapy, with similar proportion not improving with CBT (zugliani2019pharmacologicalandneuromodulatory pages 1-2) | (zugliani2019pharmacologicalandneuromodulatory pages 1-2) |


*Table: This table summarizes core panic disorder phenotypes, suggested HPO mappings, and clinically useful quantitative features such as recurrence, relapse, comorbidity, and age at onset. It is useful for structured disease knowledge base entry and phenotype annotation.*

### 3.2 Quality of life and functioning
Functional impairment in work/social/family domains is strongly associated with panic severity (PDSS), depression symptoms, and anxiety sensitivity; PDSS and ASI-R predicted lost and underproductive days in a 267-patient sample. (kim2021functionalimpairmentin pages 1-2)

## 4. Genetic/Molecular information

### 4.1 Causal genes
No single high-penetrance causal gene is established for panic disorder in the retrieved evidence; PD is supported as **polygenic** with many loci of small effect. (mitchell2025genomewidemetaanalysisidentifies pages 1-3)

### 4.2 Pathogenic variants
Specific pathogenic/likely pathogenic variants in the Mendelian sense are not established in the retrieved PD literature; GWAS risk variants and loci are described. (mitchell2025genomewidemetaanalysisidentifies pages 1-3)

### 4.3 Modifier genes / epigenetics
The retrieved 2024 systematic review emphasizes genetic and epigenetic contributions but does not provide a validated modifier-gene framework for clinical use. (moraes2024neurochemicalandgenetic pages 1-2)

## 5. Environmental information
Beyond psychosocial exposures (ACEs) and lifestyle factors (smoking, caffeine/stimulants), panic disorder frequently presents with somatic symptoms that mimic medical disease, leading to high healthcare utilization; distinguishing panic symptoms from medical illness is a key clinical concern. (locke2015diagnosisandmanagement pages 3-4)

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic model (causal chain)
A clinically useful causal chain supported by the retrieved literature is:
1) **Predisposition** (polygenic risk; familial aggregation; early adversity) → (mitchell2025genomewidemetaanalysisidentifies pages 1-3, zhang2023associationbetweenpanic pages 1-6)
2) **Threat/interoceptive sensitivity and dysregulated fear circuitry** (amygdala–insula–PFC–PAG–hypothalamus; salience/interoception network changes) → (moraes2024neurochemicalandgenetic pages 1-2, you2024abnormalinsulanetwork pages 14-19)
3) **Physiologic perturbation** (CO2/H+ sensitivity, abnormal lactate/glutamate coupling, autonomic arousal) and neurochemical imbalance (GABA/5-HT/NE/glutamate) → (moraes2024neurochemicalandgenetic pages 2-3, zugliani2019pharmacologicalandneuromodulatory pages 2-3)
4) **Panic attacks** with reinforcing avoidance/anticipatory anxiety leading to chronicity and functional impairment. (zugliani2019pharmacologicalandneuromodulatory pages 1-2)

### 6.2 Key pathways and processes (with ontology suggestions)
Mechanism summary artifact (GO/CL/UBERON suggestions and quantitative results):
| Domain | Key findings | Example quantitative results | Suggested GO biological process terms | Suggested CL cell types | Suggested UBERON anatomy terms | Key citations |
|---|---|---|---|---|---|---|
| Neurocircuitry | Panic disorder involves a distributed fear circuit including amygdala, thalamus, hippocampus, insula, prefrontal cortex, dorsal periaqueductal gray (dPAG), dorsomedial hypothalamus (DMH), and posterior hypothalamic nuclei; imaging reviews note PFC hypoactivity with hyperactivity in fear-relevant regions such as the amygdala. | Family/neurobiologic review synthesized 33 studies including 17 animal studies; PD lifetime prevalence ~4.7% used as disease context in the review. | GO:0001662 behavioral fear response; GO:0007610 behavior; GO:0050896 response to stimulus; GO:0007626 locomotory behavior | CL:0000540 neuron; CL:0000700 dopaminergic neuron; CL:0000099 GABAergic neuron | UBERON:0001870 amygdala; UBERON:0002421 hippocampus; UBERON:0001897 thalamus; UBERON:0001893 insula; UBERON:0000451 prefrontal cortex; UBERON:0002142 hypothalamus; UBERON:0002681 periaqueductal gray | (moraes2024neurochemicalandgenetic pages 1-2, zugliani2019pharmacologicalandneuromodulatory pages 2-3, ohi2025clinicalfeaturesand pages 4-4) |
| Neurotransmitters | Reduced GABAA and serotonin receptor binding in the amygdala, altered glutamate signaling, noradrenergic CO2-sensitive locus coeruleus responses, and GABAergic inhibition of hypothalamic panic-related nuclei are all implicated; benzodiazepine efficacy supports GABA-A involvement. | Activity-dependent brain lactate increased in PD vs controls (p = 0.0018); baseline glutamate predicted Glx/Cr increase after CCK-4 (p < 0.0001); minimum Glx/Cr correlated with maximum API panic scores (p = 0.009); baseline Glx/Cr correlated with maximum heart rate (p = 0.027). | GO:0007214 gamma-aminobutyric acid signaling pathway; GO:0007210 serotonin receptor signaling pathway; GO:0007218 neuropeptide signaling pathway; GO:0007268 chemical synaptic transmission; GO:0006836 neurotransmitter transport | CL:0000099 GABAergic neuron; CL:0000851 glutamatergic neuron; CL:0000738 serotonergic neuron; CL:0000700 dopaminergic neuron; CL:0000699 noradrenergic neuron | UBERON:0001870 amygdala; UBERON:0002142 hypothalamus; UBERON:0002681 periaqueductal gray; UBERON:0001891 brainstem | (moraes2024neurochemicalandgenetic pages 1-2, moraes2024neurochemicalandgenetic pages 3-4, moraes2024neurochemicalandgenetic pages 2-3, zugliani2019pharmacologicalandneuromodulatory pages 2-3) |
| Endocrine | HPA-axis dysregulation is reported but not fully consistent across studies; panic provocation activates cortisol responses, and neuroactive steroids that positively modulate GABAA may relate to symptom reduction. | CCK-4 challenge increased plasma cortisol about 10–15 min post-challenge (p = 0.0002); 3a,5a-THDOC increased after CCK-4 (p = 0.005); DEX-CRH testing found greater baseline cortisol at two pre-CRH time points in PD, while no baseline ACTH differences were seen in one study. | GO:0006958 complement activation? no; GO:0043401 steroid hormone mediated signaling pathway; GO:0031960 response to corticosteroid; GO:0002025 regulation of heart rate; GO:0001659 temperature homeostasis? no; GO:0032496 response to lipopolysaccharide? no | CL:0000393 corticotroph; CL:0000679 endocrine cell; CL:0000540 neuron | UBERON:0000945 hypothalamus-pituitary axis; UBERON:0002142 hypothalamus; UBERON:0000007 pituitary gland; UBERON:0002369 adrenal gland | (moraes2024neurochemicalandgenetic pages 3-4, moraes2024neurochemicalandgenetic pages 2-3) |
| Immune / inflammation | Stress-linked inflammatory involvement is suggested by elevated IL-6 and leptin; evidence remains limited and mostly peripheral, but supports immune-system participation in a subset of patients. | IL-6 and leptin increased during treatment timepoints; PD patients had higher IL-6 at visit 4 than MDD and healthy controls, and IL-6 correlated with PDSS items. | GO:0006954 inflammatory response; GO:0034097 response to cytokine; GO:0001816 cytokine production | CL:0000988 hematopoietic cell; CL:0000542 lymphocyte; CL:0000775 neutrophil; CL:0000235 macrophage | UBERON:0000178 blood; UBERON:0004538 blood plasma | (moraes2024neurochemicalandgenetic pages 1-2, moraes2024neurochemicalandgenetic pages 3-4) |
| Interoception / network | Panic disorder shows disrupted interoceptive and salience-network processing centered on the insula, with abnormal sensorimotor-occipital-cerebellar connectivity and reduced efficiency of the right middle insula; heightened awareness and misinterpretation of bodily sensations are a recurring conceptual theme. | In graph analysis, global efficiency was lower in PD (aEg 0.199 ± 0.008 vs 0.201 ± 0.006, t = -2.150, P = 0.033), characteristic path length was higher (aLp 0.694 ± 0.037 vs 0.682 ± 0.033, t = 2.285, P = 0.023), and right middle-insula nodal efficiency was reduced (t = -3.882, P < 0.001 FDR); right mid-insula FC was negatively correlated with PDSS. | GO:0007166 cell surface receptor signaling pathway; GO:0050877 nervous system process; GO:0050905 neuromuscular process; GO:0007600 sensory perception | CL:0000540 neuron; CL:0002608 visceral sensory neuron; CL:0000127 astrocyte | UBERON:0001893 insula; UBERON:0002245 cerebellum; UBERON:0000955 brain; UBERON:0001891 brainstem | (you2024abnormalinsulanetwork pages 14-19, mitchell2025genomewidemetaanalysisidentifies pages 10-15) |
| Genetics / cell types | PD is polygenic; recent GWAS/meta-analysis identified first genome-wide significant loci for panic phenotypes and highlighted genes linked to GABAergic inhibition and autonomic/cardiovascular regulation (e.g., IQSEC3, TNNI3K, ECE1). Cell-type enrichment implicates limbic and cerebellar neurons plus visceral afferent neurons from lung and heart, and astrocytes. | Panic attacks/disorder showed rg = 1.00 (S.E. = 0.01); SNP heritability was estimated at 11–18% for panic attacks and 8–15% for panic disorder, with raw estimates up to 16–27% and 10–20%; enrichment included limbic system cells (FDR = 3.8 × 10^-6), lung visceral neurons (FDR = 8.2 × 10^-4), heart visceral neurons (FDR = 3.1 × 10^-4), astrocytes (FDR = 1.7 × 10^-3). | GO:0007268 chemical synaptic transmission; GO:0023052 signaling; GO:0002027 regulation of heart rate; GO:0003013 circulatory system process; GO:0007611 learning or memory | CL:0000099 GABAergic neuron; CL:0000851 glutamatergic neuron; CL:0002608 visceral sensory neuron; CL:0000127 astrocyte; CL:0000540 neuron | UBERON:0000955 brain; UBERON:0001870 amygdala; UBERON:0002245 cerebellum; UBERON:0002048 lung; UBERON:0000948 heart | (mitchell2025genomewidemetaanalysisidentifies pages 3-10, mitchell2025genomewidemetaanalysisidentifies pages 1-3) |
| Metabolic / chemosensory sensitivity | Metabolic and chemosensory models emphasize abnormal lactate handling, altered glutamate-lactate coupling, pH/acid-sensing pathways, and CO2 sensitivity of panic-relevant brainstem circuitry. | Activity-dependent lactate was increased in PD (p = 0.0018); PD showed reduced Glx responses and weaker temporal lactate-Glx coupling; locus coeruleus neurons are described as CO2/H+ sensitive, and benzodiazepines can block CO2-induced panic attacks. | GO:0006091 generation of precursor metabolites and energy; GO:0019752 carboxylic acid metabolic process; GO:0006939 smooth muscle contraction? no; GO:0007584 response to nutrient; GO:0007585 respiratory gaseous exchange | CL:0000699 noradrenergic neuron; CL:0000540 neuron; CL:0002608 visceral sensory neuron | UBERON:0001891 brainstem; UBERON:0002681 periaqueductal gray; UBERON:0002142 hypothalamus | (moraes2024neurochemicalandgenetic pages 2-3, zugliani2019pharmacologicalandneuromodulatory pages 2-3, moraes2024neurochemicalandgenetic pages 1-2) |
| Neuropeptides / neuroplasticity | Orexin neurons in the dorsomedial/perifornical hypothalamus can trigger panic-like reactions; BDNF/TrkB signaling in dPAG has panicolytic-like effects through GABAA-dependent mechanisms. These pathways are among the most specific translational leads beyond monoamines. | Systematic review reports that systemic ORX-1 receptor antagonists blocked panic responses in translational models; BDNF/TrkB effects were localized particularly to dPAG, though no single pooled human effect size was reported in the excerpt. | GO:0007218 neuropeptide signaling pathway; GO:0031547 brain-derived neurotrophic factor receptor signaling pathway; GO:0051966 regulation of synaptic transmission, glutamatergic | CL:0000540 neuron; CL:0000679 endocrine cell | UBERON:0002142 hypothalamus; UBERON:0002681 periaqueductal gray | (moraes2024neurochemicalandgenetic pages 1-2) |


*Table: This table summarizes the main pathophysiologic domains implicated in panic disorder, combining recent human and translational evidence with ontology suggestions for structured annotation. It is useful for mapping disease mechanisms to biological processes, cell types, and anatomical sites in a knowledge base.*

Notable quantitative mechanistic findings include:
- Increased activity-dependent **brain lactate** in PD vs controls (p = 0.0018) and altered lactate–Glx coupling. (moraes2024neurochemicalandgenetic pages 2-3)
- CCK-4 panic induction: cortisol increase ~10–15 minutes post-challenge (p = 0.0002); 3α,5α-THDOC increase (p = 0.005); glutamate-related correlates with panic and heart rate. (moraes2024neurochemicalandgenetic pages 3-4)
- Insula network changes: reduced global efficiency and reduced right mid-insula nodal efficiency, correlated with symptom scales (PDSS). (you2024abnormalinsulanetwork pages 14-19)

### 6.3 Cell types and anatomy
Genetic enrichment analyses implicate both central and peripheral cell types, including limbic-system neurons, cerebellar granule/Purkinje neurons, excitatory and inhibitory neurons, visceral afferent neurons from lung and heart, and astrocytes. (mitchell2025genomewidemetaanalysisidentifies pages 3-10)

## 7. Anatomical structures affected
Primary structures implicated include brain fear/interoception circuits and autonomic/visceral afferent systems:
- **Brain:** amygdala, hippocampus, thalamus, insula, prefrontal cortex, periaqueductal gray, hypothalamus. (moraes2024neurochemicalandgenetic pages 1-2, zugliani2019pharmacologicalandneuromodulatory pages 2-3)
- **Peripheral/autonomic:** lung and heart visceral neuron enrichment in genetic analyses, consistent with prominent respiratory/cardiac symptoms. (mitchell2025genomewidemetaanalysisidentifies pages 3-10)

## 8. Temporal development
- **Typical onset:** often adult onset; median onset **32 years** reported in an implementation cohort. (iversen2022thebergen4day pages 1-2)
- **Course:** recurrent/chronic; recurrence rates 56–58% reported in literature summarized by VR assessment study; persistence up to 3–6 years in up to 30% and relapse 25–50% within 6 months after drug discontinuation in a treatment review. (kim2023feasibilityofthe pages 1-2, zugliani2019pharmacologicalandneuromodulatory pages 1-2)

## 9. Inheritance and population

### 9.1 Epidemiology (panic disorder and broader anxiety burden)
Panic disorder lifetime prevalence varies by source in the retrieved evidence:
- 1.6–2.2% (clinical-trials review) (zugliani2019pharmacologicalandneuromodulatory pages 1-2)
- “Up to 4%” (implementation cohort background) (iversen2022thebergen4day pages 1-2)
- 4.7% (systematic review background) (moraes2024neurochemicalandgenetic pages 1-2)
- 2–4% (GWAS background statement) (mitchell2025genomewidemetaanalysisidentifies pages 1-3)

Broader global anxiety disorder burden provides context:
- GBD 2019: **45.82 million incident cases**, **301.39 million prevalent cases**, **28.68 million DALYs** (2019). (yang2021globalregionaland pages 1-2)
- Another GBD-derived summary reports global prevalence **4.05%** and states: “Women are **1.66 times** more likely to be affected by anxiety disorders than men.” (javaid2023epidemiologyofanxiety pages 1-2)

### 9.2 Inheritance pattern
Inheritance is **multifactorial/polygenic**, with twin/family heritability in the ~40–50% range noted in GWAS background context and SNP-heritability ~8–15% for panic disorder in GWAS meta-analysis estimates. (mitchell2025genomewidemetaanalysisidentifies pages 1-3)

## 10. Diagnostics

### 10.1 Clinical criteria
- DSM-style criteria summarized in the retrieved primary-care review: recurrent unexpected panic attacks with ≥1 month worry/behavioral change; rule-outs include substances/medical conditions and other mental disorders. (locke2015diagnosisandmanagement pages 3-4)
- ICD-11 code and taxonomy: **6B01**; panic disorder separable from agoraphobia and can be comorbid; ICD-11 also allows coding of isolated panic attacks. (domschke2025taxonomyofanxiety pages 1-2, domschke2025[taxonomyofanxiety pages 1-2)

### 10.2 Differential diagnosis
Medical conditions and medications can mimic panic symptoms, including hyperthyroidism, pheochromocytoma, arrhythmias, obstructive pulmonary disease, temporal lobe epilepsy, and stimulant/bronchodilator/thyroxine effects; withdrawal states are also relevant. (locke2015diagnosisandmanagement pages 3-4)

### 10.3 Scales and tests
- **Panic Disorder Severity Scale (PDSS)** is used widely, including as primary endpoint in VR and telehealth trials; it is used alongside measures of anxiety sensitivity, body sensations, depression, and disability. (NCT04985019 chunk 1, seki2025videoconferencedeliveredcognitivebehavioral pages 1-2)
- Physiologic assessment in VR paradigms includes **heart rate variability (HRV)** indices that differ between PD and controls and correlate with symptom scales. (kim2023feasibilityofthe pages 1-2)

## 11. Outcome / prognosis
Key prognosis-relevant statistics from a treatment-trials review:
- **20–40%** do not fully respond to pharmacotherapy; similar proportion do not improve with CBT (zugliani2019pharmacologicalandneuromodulatory pages 1-2)
- **25–50%** relapse within 6 months after drug discontinuation (zugliani2019pharmacologicalandneuromodulatory pages 1-2)
- Up to **30%** remain with full disorder after 3–6 years (zugliani2019pharmacologicalandneuromodulatory pages 1-2)

## 12. Treatment

### 12.1 Evidence-based treatments
A structured treatment summary artifact (with quantitative efficacy and implementation notes):
| Intervention | Examples | Evidence of efficacy with quantitative results | Real-world / implementation notes | Suggested MAXO terms | Citations |
|---|---|---|---|---|---|
| Psychotherapy | Face-to-face individual CBT; face-to-face group CBT; guided self-help CBT | Network meta-analysis of 74 RCTs (n=6,699): group CBT vs treatment as usual SMD -0.47 (95% CI -0.87 to -0.07), individual CBT SMD -0.43 (95% CI -0.70 to -0.15), guided self-help SMD -0.42 (95% CI -0.77 to -0.07); no major acceptability differences across CBT formats (papola2023cbttreatmentdelivery pages 1-2). Concentrated Bergen 4-day treatment: remission 80.0% post-treatment and 86.7% at 3-month follow-up; no dropouts (iversen2022thebergen4day pages 1-2). | Evidence supports multiple delivery formats with similar efficacy; concentrated exposure-based CBT has been implemented in a new clinic with high satisfaction and zero dropout in the reported cohort | cognitive behavioral therapy; exposure therapy; guided self-help psychotherapy | (papola2023cbttreatmentdelivery pages 1-2, iversen2022thebergen4day pages 1-2) |
| Pharmacotherapy | SSRIs: paroxetine, escitalopram; SNRIs/venlafaxine; benzodiazepines: clonazepam, alprazolam; MAOI: tranylcypromine | Review notes 20-40% do not fully respond to pharmacotherapy; 25-50% relapse within 6 months after drug discontinuation; up to 30% remain with full disorder after 3-6 years (zugliani2019pharmacologicalandneuromodulatory pages 1-2). Comparative/open trial evidence confirmed efficacy of tranylcypromine, paroxetine, clonazepam, alprazolam, and escitalopram; vortioxetine showed open-label improvement (zugliani2019pharmacologicalandneuromodulatory pages 1-2). | Medications remain common in routine care; in one clinic sample 60% used psychotropic medication, including SSRIs 36.7% and benzodiazepines 26.7% (iversen2022thebergen4day pages 1-2). Benzodiazepines are effective acutely but long-term use is cautioned in broader anxiety literature | selective serotonin reuptake inhibitor therapy; serotonin-norepinephrine reuptake inhibitor therapy; benzodiazepine therapy; monoamine oxidase inhibitor therapy | (zugliani2019pharmacologicalandneuromodulatory pages 1-2, iversen2022thebergen4day pages 1-2) |
| Adjunct CBT after pharmacotherapy | Videoconference-delivered CBT added to usual care for persistent symptoms after medication | Randomized assessor-blinded trial (n=30): PDSS change at 16 weeks was -7.92 with videoconference-CBT vs 0.75 with usual care; between-group difference -8.67 (95% CI -11.80 to -5.54; P<.0001). Response 80% vs 6.7%; remission 66.7% vs 0.0% (seki2025videoconferencedeliveredcognitivebehavioral pages 1-2). | Demonstrates a practical stepped-care model for patients still symptomatic after first-line pharmacotherapy; home-based telehealth delivery may improve access where expert CBT is scarce | telehealth cognitive behavioral therapy; adjunct psychotherapy | (seki2025videoconferencedeliveredcognitivebehavioral pages 1-2) |
| Digital CBT / internet-based CBT | Guided internet CBT; app-based CBT; self-guided digital CBT | Guided self-help CBT was efficacious in panic-disorder network meta-analysis with SMD -0.42 vs treatment as usual; unguided self-help was not clearly superior (papola2023cbttreatmentdelivery pages 1-2). A 2025 meta-analysis of digital CBT for panic/agoraphobia found overall g=0.70 vs passive controls and g=-0.05 vs active controls, suggesting parity with traditional CBT; interoceptive exposure improved outcomes (jung2025digitalcognitivebehavioral pages 1-2). | Remote delivery accelerated after COVID-19; therapist-supported internet CBT across psychiatric disorders yields effects similar to face-to-face CBT in broader meta-analysis, supporting implementation potential (hedman‐lagerlof2023therapist‐supportedinternet‐basedcognitive pages 10-10). Digital formats can reduce access barriers and support stepped care | internet-based cognitive behavioral therapy; app-delivered psychotherapy; digital therapeutic intervention | (papola2023cbttreatmentdelivery pages 1-2, jung2025digitalcognitivebehavioral pages 1-2, hedman‐lagerlof2023therapist‐supportedinternet‐basedcognitive pages 10-10) |
| Virtual reality (VR) interventions | Mobile self-guided VR-CBT; VR exposure therapy; VR-based assessment modules | Completed randomized trial of mobile self-guided VR-CBT enrolled 40 adults with DSM-defined panic disorder; primary outcome was PDSS at 4 weeks, with secondary physiologic and symptom measures including HRV and body-sensation scales (NCT04985019 chunk 1). Quantitative trial results were not reported in the retrieved registry excerpt. | Real-world implementation includes smartphone/mobile delivery and self-guided exposure content; VR modules can target daily-environment exposure, relaxation, and interoceptive exposure, and were feasible with no discontinuation in a feasibility study (kim2023feasibilityofthe pages 1-2) | virtual reality exposure therapy; mobile health intervention; self-guided psychotherapy | (NCT04985019 chunk 1, kim2023feasibilityofthe pages 1-2) |
| Neuromodulation | Repetitive transcranial magnetic stimulation (rTMS/TMS) | Review of clinical trials from 2010-2018 found efficacy in only 1 of 2 RCTs; open trials suggested TMS may be effective if delivered for 4 or more weeks, but evidence remained mixed and limited (zugliani2019pharmacologicalandneuromodulatory pages 1-2). | Still investigational for panic disorder; not supported as robustly as CBT or standard medications | transcranial magnetic stimulation | (zugliani2019pharmacologicalandneuromodulatory pages 1-2) |
| Treatment-resistant / augmentation approaches | Quetiapine augmentation; pindolol; vortioxetine; experimental augmentation strategies | Quetiapine augmentation was not superior to placebo; pindolol and d-fenfluramine were ineffective in blocking flumazenil-induced panic attacks; vortioxetine appeared promising in open trials (zugliani2019pharmacologicalandneuromodulatory pages 1-2). | Use remains limited by weak evidence, small samples, and off-label status in many cases | drug augmentation therapy; off-label pharmacotherapy | (zugliani2019pharmacologicalandneuromodulatory pages 1-2) |
| Long-term treatment strategy | Continuation therapy; relapse prevention; combined/stepped care | Relapse after medication discontinuation is common (25-50% within 6 months), supporting continuation planning and psychotherapy integration (zugliani2019pharmacologicalandneuromodulatory pages 1-2). Combined CBT-pharmacotherapy has not fully eliminated nonresponse, but telehealth/digital CBT may expand access for maintenance and next-step care (zugliani2019pharmacologicalandneuromodulatory pages 1-2, seki2025videoconferencedeliveredcognitivebehavioral pages 1-2). | Practical models include medication first in routine care, then referral to specialist CBT, videoconference CBT, or digital self-help/guided CBT depending access and severity | relapse prevention intervention; maintenance therapy; stepped-care intervention | (zugliani2019pharmacologicalandneuromodulatory pages 1-2, seki2025videoconferencedeliveredcognitivebehavioral pages 1-2) |


*Table: This table summarizes the main evidence-based and emerging treatments for panic disorder, including quantitative efficacy data where available. It also highlights implementation formats such as telehealth, internet-based CBT, and VR that are relevant for real-world care delivery.*

Key points with 2023–2025 evidence emphasis:
- CBT delivery-format network meta-analysis (published 2023) supports that face-to-face individual/group CBT and guided self-help outperform treatment as usual, with broadly similar efficacy across formats. (papola2023cbttreatmentdelivery pages 1-2)
- Videoconference CBT RCT (2025) demonstrated large clinical benefit for patients still symptomatic after medication: PDSS change −7.92 vs 0.75 at 16 weeks; response 80% vs 6.7%; remission 66.7% vs 0%. (seki2025videoconferencedeliveredcognitivebehavioral pages 1-2)
- Pharmacotherapy evidence summary: SSRIs, TCAs, MAOIs and benzodiazepines show efficacy, but there is a significant nonresponse fraction and high relapse after discontinuation. (zugliani2019pharmacologicalandneuromodulatory pages 1-2)
- VR/digital implementation: ClinicalTrials.gov records support feasibility and ongoing/complete testing of mobile VR-CBT for PD with PDSS endpoints and physiologic measures (e.g., HRV). (NCT04985019 chunk 1)

### 12.2 MAXO suggestions
MAXO codes were not retrieved; suggested MAXO-aligned labels include: cognitive behavioral therapy, exposure therapy, SSRI therapy, SNRI therapy, benzodiazepine therapy, MAOI therapy, transcranial magnetic stimulation, telehealth psychotherapy, internet-based CBT, and virtual reality exposure therapy. (papola2023cbttreatmentdelivery pages 1-2, seki2025videoconferencedeliveredcognitivebehavioral pages 1-2, zugliani2019pharmacologicalandneuromodulatory pages 1-2, NCT04985019 chunk 1)

## 13. Prevention
Formal prevention trials or guideline-level preventive interventions specific to panic disorder were not included in the retrieved evidence set. Risk reduction implied by evidence includes targeting childhood adversity at population level and minimizing triggers (e.g., caffeine/stimulants) in susceptible individuals, but these are not quantified as preventive effect sizes here. (zhang2023associationbetweenpanic pages 1-6, locke2015diagnosisandmanagement pages 3-4)

## 14. Other species / natural disease
No naturally occurring panic-disorder analog in other species was identified in the retrieved evidence set.

## 15. Model organisms
Evidence supports use of translational animal paradigms centered on panic-like circuitry:
- Systematic review highlights **dPAG** and hypothalamic orexin pathways; ORX-1 antagonists block panic responses in translational models, and BDNF/TrkB effects in dPAG show panicolytic-like patterns mediated via GABAA mechanisms. (moraes2024neurochemicalandgenetic pages 1-2)
- Selectively bred **Carioca rat lines** (CHF/CLF) are used to study defensive behaviors and fear circuitry; dPAG electrical stimulation paradigms show line differences and support circuit specificity (dPAG as panic-linked circuitry distinct from generalized anxiety). (lages2023pharmacologicalandphysiological pages 6-7, lages2023pharmacologicalandphysiological pages 1-2)

## Recent developments (prioritizing 2023–2024)
1) **Neurochemical/genetic synthesis (2024, Translational Psychiatry):** Consolidated evidence for altered GABAA/serotonin signaling in amygdala, orexin-triggered panic circuits, IL-6/leptin signals, lactate/glutamate abnormalities, and BDNF/TrkB effects in dPAG. URL: https://doi.org/10.1038/s41398-024-02966-0 (Jul 2024). (moraes2024neurochemicalandgenetic pages 1-2)
2) **CBT delivery formats network meta-analysis (2023, Psychological Medicine):** 74 RCTs (n=6,699) comparing CBT formats, supporting guided self-help and in-person CBT with similar efficacy and acceptability. URL: https://doi.org/10.1017/S0033291722003683 (Dec 2023). (papola2023cbttreatmentdelivery pages 1-2)
3) **Childhood adversity meta-analysis (2023, Psychological Medicine):** Quantified ACE–PD association (pooled OR 2.2). URL: https://doi.org/10.1017/S0033291721004505 (Nov 2023). (zhang2023associationbetweenpanic pages 1-6)
4) **Insula network neuroimaging (2024, Brazilian Journal of Psychiatry):** Graph-theory evidence implicating insula efficiency/connectivity with symptom correlations. URL: https://doi.org/10.47626/1516-4446-2023-3520 (Jun 2024). (you2024abnormalinsulanetwork pages 14-19)

## Expert opinions and analysis (authoritative sources)
- ICD-11 nosology experts emphasize separation of panic disorder from agoraphobia (comorbid diagnosability) and simplification of symptom-count minima; they note implications for clinical practicability and diagnostic accuracy that warrant further evaluation. (domschke2025taxonomyofanxiety pages 3-4)
- High-quality psychotherapy synthesis concludes there are no major efficacy differences among guided self-help and face-to-face CBT formats for panic disorder, which supports health-system scaling via guided/self-help models when specialist availability is limited. (papola2023cbttreatmentdelivery pages 1-2)

## Data/statistics highlights (recent studies)
- Global anxiety disorders (GBD 2019): **301.39 million prevalent**, **45.82 million incident**, **28.68 million DALYs** (2019). (yang2021globalregionaland pages 1-2)
- Sex ratio for anxiety disorders globally: women **1.66×** more likely to be affected (GBD-derived summary). (javaid2023epidemiologyofanxiety pages 1-2)
- Panic disorder relapse post-medication discontinuation: **25–50% within 6 months**; chronic persistence up to **30%** at 3–6 years (review). (zugliani2019pharmacologicalandneuromodulatory pages 1-2)
- Telehealth CBT (videoconference): response **80%** vs **6.7%** and remission **66.7%** vs **0%** at 16 weeks in symptomatic patients after pharmacotherapy. (seki2025videoconferencedeliveredcognitivebehavioral pages 1-2)

## Limitations of this report (evidence gaps)
- MONDO and MeSH identifiers were not retrievable from the current tool-retrieved corpus and are therefore not asserted here.
- Several requested items (protective factors, explicit gene×environment interaction results, validated biomarker tests for diagnosis, comprehensive omics) were not present in the retrieved evidence set.
- PMID-level citation mapping is incomplete because multiple retrieved sources did not include PMIDs in the available text chunks; URLs/DOIs and publication dates are provided when available in evidence.


References

1. (domschke2025taxonomyofanxiety pages 1-2): Katharina Domschke and Peter Zwanzger. Taxonomy of anxiety disorders-a comparison of icd‑10 and icd‑11. Der Nervenarzt, Jul 2025. URL: https://doi.org/10.1007/s00115-025-01842-6, doi:10.1007/s00115-025-01842-6. This article has 1 citations.

2. (domschke2025taxonomyofanxiety pages 3-4): Katharina Domschke and Peter Zwanzger. Taxonomy of anxiety disorders-a comparison of icd‑10 and icd‑11. Der Nervenarzt, Jul 2025. URL: https://doi.org/10.1007/s00115-025-01842-6, doi:10.1007/s00115-025-01842-6. This article has 1 citations.

3. (moraes2024neurochemicalandgenetic pages 1-2): Adriana Carvalho Natal Moraes, Clarissa Wijaya, Rafael Freire, Laiana Azevedo Quagliato, Antonio Egidio Nardi, and Peter Kyriakoulis. Neurochemical and genetic factors in panic disorder: a systematic review. Translational Psychiatry, Jul 2024. URL: https://doi.org/10.1038/s41398-024-02966-0, doi:10.1038/s41398-024-02966-0. This article has 13 citations and is from a peer-reviewed journal.

4. (moraes2024neurochemicalandgenetic pages 2-3): Adriana Carvalho Natal Moraes, Clarissa Wijaya, Rafael Freire, Laiana Azevedo Quagliato, Antonio Egidio Nardi, and Peter Kyriakoulis. Neurochemical and genetic factors in panic disorder: a systematic review. Translational Psychiatry, Jul 2024. URL: https://doi.org/10.1038/s41398-024-02966-0, doi:10.1038/s41398-024-02966-0. This article has 13 citations and is from a peer-reviewed journal.

5. (zugliani2019pharmacologicalandneuromodulatory pages 2-3): Morena M. Zugliani, Mariana C. Cabo, Antonio E. Nardi, Giampaolo Perna, and Rafael C. Freire. Pharmacological and neuromodulatory treatments for panic disorder: clinical trials from 2010 to 2018. Psychiatry Investigation, 16:50-58, Jan 2019. URL: https://doi.org/10.30773/pi.2018.12.21.1, doi:10.30773/pi.2018.12.21.1. This article has 32 citations and is from a peer-reviewed journal.

6. (mitchell2025genomewidemetaanalysisidentifies pages 3-10): Brittany L. Mitchell, Megan Skelton, Rujia Wang, Abigail R. ter Kuile, Alan E. Murphy, Genevieve Morneau-Vaillancourt, Danyang Li, Elham Assary, Matthew Hotopf, Jihua Hu, Chérie Armour, Andrew M. McIntosh, James T. R. Walters, Donald M. Lyall, Daniel J. Smith, Nathalie Kingston, John R. Bradley, Gursharan Kalsi, Sang-Hyuck Lee, Yuhao (Leo) Lin, Evangelos Vassos, Saakshi Kakar, Laura Meldrum, Iona Smith, Gemma Chavarria Ventura, Catherine M. Olsen, David C. Whiteman, Sarah E. Medland, Penelope A. Lind, Enda M. Byrne, Ian B. Hickie, Naomi R. Wray, Lukas Mach, Michela Noseda, Andreas Forstner, Harold Snieder, Catharina A. Hartman, Nicholas G. Martin, Jürgen Deckert, Nathan Skene, Jonathan R. I. Coleman, Thalia C. Eley, and Gerome Breen. Genome-wide meta-analysis identifies genetic risk factors and implicates multiple body systems in panic attacks and disorder. MedRxiv, Jun 2025. URL: https://doi.org/10.1101/2025.06.15.25329656, doi:10.1101/2025.06.15.25329656. This article has 1 citations.

7. (locke2015diagnosisandmanagement pages 3-4): AB Locke, N Kirst, and CG Shultz. Diagnosis and management of generalized anxiety disorder and panic disorder in adults. Unknown journal, 2015.

8. (zugliani2019pharmacologicalandneuromodulatory pages 1-2): Morena M. Zugliani, Mariana C. Cabo, Antonio E. Nardi, Giampaolo Perna, and Rafael C. Freire. Pharmacological and neuromodulatory treatments for panic disorder: clinical trials from 2010 to 2018. Psychiatry Investigation, 16:50-58, Jan 2019. URL: https://doi.org/10.30773/pi.2018.12.21.1, doi:10.30773/pi.2018.12.21.1. This article has 32 citations and is from a peer-reviewed journal.

9. (papola2023cbttreatmentdelivery pages 1-2): Davide Papola, Giovanni Ostuzzi, Federico Tedeschi, Chiara Gastaldon, Marianna Purgato, Cinzia Del Giovane, Alessandro Pompoli, Darin Pauley, Eirini Karyotaki, Marit Sijbrandij, Toshi A. Furukawa, Pim Cuijpers, and Corrado Barbui. Cbt treatment delivery formats for panic disorder: a systematic review and network meta-analysis of randomised controlled trials. Psychological Medicine, 53:614-624, Dec 2023. URL: https://doi.org/10.1017/s0033291722003683, doi:10.1017/s0033291722003683. This article has 54 citations and is from a highest quality peer-reviewed journal.

10. (yang2021globalregionaland pages 1-2): Xiaorong Yang, Yuan Fang, Hui Chen, Tongchao Zhang, Xiaolin Yin, Jinyu Man, Lejin Yang, and Ming Lu. Global, regional and national burden of anxiety disorders from 1990 to 2019: results from the global burden of disease study 2019. Epidemiology and Psychiatric Sciences, May 2021. URL: https://doi.org/10.1017/s2045796021000275, doi:10.1017/s2045796021000275. This article has 582 citations and is from a domain leading peer-reviewed journal.

11. (walter2024psychischestörungenin pages 1-2): Henrik Walter, Ronja Husemann, and Lars P. Hölzel. Psychische störungen in der icd-11. Nervenheilkunde, 43:167-178, Apr 2024. URL: https://doi.org/10.1055/a-2216-7277, doi:10.1055/a-2216-7277. This article has 24 citations and is from a peer-reviewed journal.

12. (domschke2025[taxonomyofanxiety pages 1-2): Katharina Domschke and Peter Zwanzger. [taxonomy of anxiety disorders in comparison of icd‑10 and icd‑11. german version]. Der Nervenarzt, Jun 2025. URL: https://doi.org/10.1007/s00115-025-01841-7, doi:10.1007/s00115-025-01841-7. This article has 1 citations.

13. (mitchell2025genomewidemetaanalysisidentifies pages 1-3): Brittany L. Mitchell, Megan Skelton, Rujia Wang, Abigail R. ter Kuile, Alan E. Murphy, Genevieve Morneau-Vaillancourt, Danyang Li, Elham Assary, Matthew Hotopf, Jihua Hu, Chérie Armour, Andrew M. McIntosh, James T. R. Walters, Donald M. Lyall, Daniel J. Smith, Nathalie Kingston, John R. Bradley, Gursharan Kalsi, Sang-Hyuck Lee, Yuhao (Leo) Lin, Evangelos Vassos, Saakshi Kakar, Laura Meldrum, Iona Smith, Gemma Chavarria Ventura, Catherine M. Olsen, David C. Whiteman, Sarah E. Medland, Penelope A. Lind, Enda M. Byrne, Ian B. Hickie, Naomi R. Wray, Lukas Mach, Michela Noseda, Andreas Forstner, Harold Snieder, Catharina A. Hartman, Nicholas G. Martin, Jürgen Deckert, Nathan Skene, Jonathan R. I. Coleman, Thalia C. Eley, and Gerome Breen. Genome-wide meta-analysis identifies genetic risk factors and implicates multiple body systems in panic attacks and disorder. MedRxiv, Jun 2025. URL: https://doi.org/10.1101/2025.06.15.25329656, doi:10.1101/2025.06.15.25329656. This article has 1 citations.

14. (zhang2023associationbetweenpanic pages 1-6): Joyce Zhang, Patryja Wiecaszek, Saber Sami, and Richard Meiser-Stedman. Association between panic disorder and childhood adversities: a systematic review and meta-analysis. Psychological Medicine, 53:2585-2595, Nov 2023. URL: https://doi.org/10.1017/s0033291721004505, doi:10.1017/s0033291721004505. This article has 30 citations and is from a highest quality peer-reviewed journal.

15. (mitchell2025genomewidemetaanalysisidentifies pages 10-15): Brittany L. Mitchell, Megan Skelton, Rujia Wang, Abigail R. ter Kuile, Alan E. Murphy, Genevieve Morneau-Vaillancourt, Danyang Li, Elham Assary, Matthew Hotopf, Jihua Hu, Chérie Armour, Andrew M. McIntosh, James T. R. Walters, Donald M. Lyall, Daniel J. Smith, Nathalie Kingston, John R. Bradley, Gursharan Kalsi, Sang-Hyuck Lee, Yuhao (Leo) Lin, Evangelos Vassos, Saakshi Kakar, Laura Meldrum, Iona Smith, Gemma Chavarria Ventura, Catherine M. Olsen, David C. Whiteman, Sarah E. Medland, Penelope A. Lind, Enda M. Byrne, Ian B. Hickie, Naomi R. Wray, Lukas Mach, Michela Noseda, Andreas Forstner, Harold Snieder, Catharina A. Hartman, Nicholas G. Martin, Jürgen Deckert, Nathan Skene, Jonathan R. I. Coleman, Thalia C. Eley, and Gerome Breen. Genome-wide meta-analysis identifies genetic risk factors and implicates multiple body systems in panic attacks and disorder. MedRxiv, Jun 2025. URL: https://doi.org/10.1101/2025.06.15.25329656, doi:10.1101/2025.06.15.25329656. This article has 1 citations.

16. (moraes2024neurochemicalandgenetic pages 3-4): Adriana Carvalho Natal Moraes, Clarissa Wijaya, Rafael Freire, Laiana Azevedo Quagliato, Antonio Egidio Nardi, and Peter Kyriakoulis. Neurochemical and genetic factors in panic disorder: a systematic review. Translational Psychiatry, Jul 2024. URL: https://doi.org/10.1038/s41398-024-02966-0, doi:10.1038/s41398-024-02966-0. This article has 13 citations and is from a peer-reviewed journal.

17. (kunas2023themodulatingimpact pages 1-2): Stefanie L Kunas, Kevin Hilbert, Yunbo Yang, Jan Richter, Alfons Hamm, André Wittmann, Andreas Ströhle, Bettina Pfleiderer, Martin J Herrmann, Thomas Lang, Martin Lotze, Jürgen Deckert, Volker Arolt, Hans-Ulrich Wittchen, Benjamin Straube, Tilo Kircher, Alexander L Gerlach, and Ulrike Lueken. The modulating impact of cigarette smoking on brain structure in panic disorder: a voxel-based morphometry study. Social Cognitive and Affective Neuroscience, 15:849-859, Jul 2023. URL: https://doi.org/10.1093/scan/nsaa103, doi:10.1093/scan/nsaa103. This article has 12 citations and is from a domain leading peer-reviewed journal.

18. (kim2021functionalimpairmentin pages 1-2): Hyun-Ju Kim, Ji Eun Kim, and Sang-Hyuk Lee. Functional impairment in patients with panic disorder. Psychiatry Investigation, 18:434-442, May 2021. URL: https://doi.org/10.30773/pi.2020.0425, doi:10.30773/pi.2020.0425. This article has 17 citations and is from a peer-reviewed journal.

19. (kim2023feasibilityofthe pages 1-2): Byung-Hoon Kim, Jae-Jin Kim, Jooyoung Oh, Seung-Hyun Kim, Changsu Han, Hyun-Ghang Jeong, Moon-Soo Lee, and Junhyung Kim. Feasibility of the virtual reality-based assessments in patients with panic disorder. Frontiers in Psychiatry, Jan 2023. URL: https://doi.org/10.3389/fpsyt.2023.1084255, doi:10.3389/fpsyt.2023.1084255. This article has 8 citations.

20. (iversen2022thebergen4day pages 1-2): Hanne Moe Iversen, Thorstein Olsen Eide, Mathea Harvold, Stian Solem, Gerd Kvale, Bjarne Hansen, and Kristen Hagen. The bergen 4-day treatment for panic disorder: replication and implementation in a new clinic. BMC Psychiatry, Nov 2022. URL: https://doi.org/10.1186/s12888-022-04380-6, doi:10.1186/s12888-022-04380-6. This article has 18 citations and is from a domain leading peer-reviewed journal.

21. (you2024abnormalinsulanetwork pages 14-19): Linlin You, Wenhao Jiang, Taipeng Sun, Yue Zhou, Gang Chen, Wei Xu, Chenguang Jiang, Yingying Yue, Suzhen Chen, Ying Chen, Dan Wang, and Yonggui Yuan. Abnormal insula network characteristics in panic disorder. Brazilian Journal of Psychiatry, Jun 2024. URL: https://doi.org/10.47626/1516-4446-2023-3520, doi:10.47626/1516-4446-2023-3520. This article has 2 citations.

22. (berenz2019timecourseof pages 1-3): Erin C. Berenz, Timothy P. York, Hanaan Bing-Canar, Ananda B. Amstadter, Briana Mezuk, Charles O. Gardner, and Roxann Roberson-Nay. Time course of panic disorder and posttraumatic stress disorder onsets. Social Psychiatry and Psychiatric Epidemiology, 54:639-647, Jul 2019. URL: https://doi.org/10.1007/s00127-018-1559-1, doi:10.1007/s00127-018-1559-1. This article has 39 citations and is from a domain leading peer-reviewed journal.

23. (ohi2025clinicalfeaturesand pages 4-4): Kazutaka Ohi, Daisuke Fujikane, Kentaro Takai, Ayumi Kuramitsu, Yukimasa Muto, Shunsuke Sugiyama, and Toshiki Shioiri. Clinical features and genetic mechanisms of anxiety, fear, and avoidance: a comprehensive review of five anxiety disorders. Molecular Psychiatry, 30:4928-4936, Aug 2025. URL: https://doi.org/10.1038/s41380-025-03155-1, doi:10.1038/s41380-025-03155-1. This article has 15 citations and is from a highest quality peer-reviewed journal.

24. (javaid2023epidemiologyofanxiety pages 1-2): Syed Fahad Javaid, Ibrahim Jawad Hashim, Muhammad Jawad Hashim, Emmanuel Stip, Mohammed Abdul Samad, and Alia Al Ahbabi. Epidemiology of anxiety disorders: global burden and sociodemographic associations. Middle East Current Psychiatry, May 2023. URL: https://doi.org/10.1186/s43045-023-00315-3, doi:10.1186/s43045-023-00315-3. This article has 583 citations.

25. (NCT04985019 chunk 1): Jooyoung Oh. A Validation Study of Mobile Virtual Reality-Based Self-Care and Exposure Therapy Contents for the Treatment of Panic Disorder. Gangnam Severance Hospital. 2018. ClinicalTrials.gov Identifier: NCT04985019

26. (seki2025videoconferencedeliveredcognitivebehavioral pages 1-2): Yoichi Seki, Ryo Takemura, Chihiro Sutoh, Remi Noguchi, Yoko Okamoto, Ikuyo Ohira, Shinobu Nagata, and Eiji Shimizu. Videoconference-delivered cognitive behavioral therapy in patients with symptomatic panic disorder following primary pharmacotherapy: a randomized, assessor-blinded, controlled trial. BMC Psychiatry, Sep 2025. URL: https://doi.org/10.1186/s12888-025-07320-2, doi:10.1186/s12888-025-07320-2. This article has 0 citations and is from a domain leading peer-reviewed journal.

27. (jung2025digitalcognitivebehavioral pages 1-2): Han Wool Jung, Ki Won Jang, Sangkyu Nam, Areum Kim, Junghoon Lee, Moo Eob Ahn, Sang-Kyu Lee, Yeo Jin Kim, Jae-Kyoung Shin, and Daeyoung Roh. Digital cognitive behavioral therapy for panic disorder and agoraphobia: a meta-analytic review of clinical components to maximize efficacy. Journal of Clinical Medicine, 14:1771, Mar 2025. URL: https://doi.org/10.3390/jcm14051771, doi:10.3390/jcm14051771. This article has 7 citations.

28. (hedman‐lagerlof2023therapist‐supportedinternet‐basedcognitive pages 10-10): Erik Hedman‐Lagerlöf, Per Carlbring, Frank Svärdman, Heleen Riper, Pim Cuijpers, and Gerhard Andersson. Therapist‐supported internet‐based cognitive behaviour therapy yields similar effects as face‐to‐face therapy for psychiatric and somatic disorders: an updated systematic review and meta‐analysis. World Psychiatry, 22:305-314, May 2023. URL: https://doi.org/10.1002/wps.21088, doi:10.1002/wps.21088. This article has 283 citations and is from a highest quality peer-reviewed journal.

29. (lages2023pharmacologicalandphysiological pages 6-7): Yury V. Lages, Laura Balthazar, Thomas. E. Krahe, and J. Landeira-Fernandez. Pharmacological and physiological correlates of the bidirectional fear phenotype of the carioca rats and other bidirectionally selected lines. Current Neuropharmacology, 21:1864-1883, Sep 2023. URL: https://doi.org/10.2174/1570159x20666221012121534, doi:10.2174/1570159x20666221012121534. This article has 9 citations and is from a peer-reviewed journal.

30. (lages2023pharmacologicalandphysiological pages 1-2): Yury V. Lages, Laura Balthazar, Thomas. E. Krahe, and J. Landeira-Fernandez. Pharmacological and physiological correlates of the bidirectional fear phenotype of the carioca rats and other bidirectionally selected lines. Current Neuropharmacology, 21:1864-1883, Sep 2023. URL: https://doi.org/10.2174/1570159x20666221012121534, doi:10.2174/1570159x20666221012121534. This article has 9 citations and is from a peer-reviewed journal.