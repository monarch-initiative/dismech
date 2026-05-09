---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T15:01:39.822705'
end_time: '2026-05-06T15:23:47.588648'
duration_seconds: 1327.77
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Carotid Stenosis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Carotid Stenosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Carotid Stenosis** covering all of the
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
- **Disease Name:** Carotid Stenosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Carotid Stenosis** covering all of the
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


## Comprehensive Disease Characteristics Report: Carotid Stenosis

### Target disease
Carotid stenosis refers to narrowing of the extracranial carotid arteries—most commonly the internal carotid artery (ICA)—usually due to atherosclerotic plaque, and is clinically important because it increases risk of transient ischemic attack (TIA) and ischemic stroke. Contemporary sources emphasize that stroke risk is not determined solely by percent luminal narrowing; “vulnerable” plaque features can confer risk even with <50% stenosis. (miceli2024molecularpathwaysof pages 1-2, pakizer2024diagnosticaccuracyof pages 1-7)

---

## 1. Disease Information

### 1.1 Concise overview
* **Asymptomatic carotid artery stenosis (aCAS)** is defined as extracranial carotid stenosis **“without a history of ipsilateral ischemic stroke or transient ischemic attack.”** (kim2023asymptomaticcarotidartery pages 1-1)
* “Symptomatic carotid disease” in guideline usage generally refers to carotid-territory ischemic events in a defined recent time window; e.g., one guideline defines symptomatic disease as ≥1 ischemic event in the carotid territory in the **preceding 6 months**. (ristow2024brazilianangiologyand pages 14-16)

### 1.2 Key identifiers (ontology/coding)
* **MeSH**: Carotid Stenosis **D016893**. (NCT03121209 chunk 4, NCT02089217 chunk 6)
* **MeSH parent**: Carotid Artery Diseases **D002340**. (NCT03121209 chunk 4, NCT06653387 chunk 3)
* **MONDO ID**: Not found in the retrieved evidence set; requires direct MONDO lookup (not evidenced here). (artifact-00)
* **ICD-10/ICD-11**: Not present in retrieved full text; requires direct ICD source lookup (not evidenced here). (artifact-00)

### 1.3 Synonyms and alternative names (clinical)
* Carotid artery stenosis (CAS)
* Internal carotid artery stenosis
* Extracranial carotid atherosclerotic disease
* High-grade carotid stenosis (often ≥70% by NASCET in interventional literature) (spiliopoulos2024cirsestandardsof pages 1-2)
* Near-occlusion / “string sign” (definitions vary by modality and center) (trochowski2024currentpracticein pages 4-5, naylor2023editorschoice– pages 11-12)

### 1.4 Evidence provenance
This report synthesizes **aggregated** disease-level evidence from clinical practice guidelines, systematic reviews/meta-analyses, observational cohorts/registries, and ClinicalTrials.gov records rather than individual EHR case reports. (bushnell20242024guidelinefor pages 25-26, pakizer2024diagnosticaccuracyof pages 1-7, poorthuis2024predictionofsevere pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
* **Primary cause**: atherosclerotic plaque development at the carotid bifurcation/ICA leading to progressive narrowing and embolic risk. (ristow2024brazilianangiologyand pages 14-16, miceli2024molecularpathwaysof pages 1-2)
* **Mechanistic cause of stroke**: plaque rupture/ulceration → thrombus formation → artery-to-artery embolization; this can occur even with non-severe stenosis when plaque is “vulnerable”. (miceli2024molecularpathwaysof pages 1-2, musialek2025strokeriskmanagement pages 61-62)

### 2.2 Risk factors (human clinical/epidemiologic)
Direct, quantified risk-factor effect estimates (e.g., HR per smoking pack-year) were not extracted from the retrieved set. However, vascular risk-factor control is consistently emphasized as the cornerstone of modern management, and multiple studies incorporate common cardiovascular risk factors (hypertension, dyslipidemia, diabetes, smoking) in risk prediction and plaque vulnerability frameworks. (bushnell20242024guidelinefor pages 25-26, poorthuis2024predictionofsevere pages 1-2)

### 2.3 Protective factors
* **Statin-based lipid-lowering therapy** is recommended/considered beneficial for reducing stroke risk in asymptomatic atherosclerotic carotid stenosis. (bushnell20242024guidelinefor pages 25-26)
* In a guideline summary of PCSK9 inhibitor trials, evolocumab was reported to reduce ischemic stroke by **25%** (95% CI 0.62–0.92). (ristow2024brazilianangiologyand pages 8-9)

### 2.4 Gene–environment interactions
No carotid-stenosis-specific gene–environment interaction study was retrieved; the disease is treated as complex/multifactorial with pleiotropic cardiometabolic genetic architecture and strong environmental/lifestyle contributions. (poorthuis2024predictionofsevere pages 1-2)

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (suggested HPO terms)
* **Transient ischemic attack** — *HP:0002323* (symptom/clinical event). (ristow2024brazilianangiologyand pages 14-16)
* **Ischemic stroke** — *HP:0002140* (complication/outcome). (ristow2024brazilianangiologyand pages 8-9)
* **Amaurosis fugax / transient monocular blindness** — *HP:0001107* (carotid-territory symptom; used in trial eligibility definitions). (NCT04547387 chunk 2)
* **Cognitive impairment** (reported as an outcome/association in CREST-H condition ontology) — *HP:0100543* (NCT03121209 chunk 4)

### 3.2 Imaging phenotypes (suggested HPO terms where applicable)
* **Carotid artery stenosis** (phenotypic abnormality) — *HP:0025492* (suggested).
* **Atherosclerotic plaque** — *HP:0033678* (suggested).
* **Intraplaque hemorrhage (IPH)** — suggested as an imaging phenotype; MRI-based IPH is a high-risk feature used in guideline selection criteria. (ristow2024brazilianangiologyand pages 13-14)

### 3.3 Onset, progression, and frequency
* aCAS is often discovered incidentally or via vascular screening in high-risk populations; a 2023 review reports population prevalence **0.1%–3.1%**. (kim2023asymptomaticcarotidartery pages 1-2)
* In a large 2024 registry-derived cohort, **severe (≥70%) baseline asymptomatic** stenosis prevalence was **6.3%** (n=26,384). (poorthuis2024predictionofsevere pages 1-2)

### 3.4 Quality-of-life impact
Quality-of-life impact is largely mediated through neurologic events (TIA/stroke) and possible cognitive effects; CREST-H explicitly couples carotid stenosis with cognitive dysfunction as an outcome area. (NCT03121209 chunk 4)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes
Carotid stenosis is a **complex** disease; no single causal gene was identified in the retrieved evidence set, and no Mendelian carotid stenosis gene list (OMIM-style) was retrieved.

### 4.2 Polygenic architecture and cardiometabolic loci
A 2024 multi-trait genetic colocalization analysis identified shared loci across cardiovascular and cerebrovascular diseases linked to blood pressure, lipid traits, and carotid intima-media thickness (cIMT), mapping to genes including **LDLR** and **SH2B3**, among others—consistent with polygenic cardiometabolic mechanisms relevant to carotid atherosclerosis phenotypes. (poorthuis2024predictionofsevere pages 1-2)

### 4.3 Mendelian randomization (example)
A 2024 Mendelian randomization study reported **no significant association** between genetically predicted vitamin D status/deficiency and carotid plaque risk (e.g., OR≈1.0). This supports caution when inferring causality from observational vitamin D–atherosclerosis associations. (poorthuis2024predictionofsevere pages 1-2)

### 4.4 Molecular biomarkers and pathways (see Mechanism)
Recent molecular reviews emphasize inflammatory cytokines, oxidized LDL pathways, and extracellular-matrix proteolysis (e.g., MMPs) in plaque vulnerability. (miceli2024molecularpathwaysof pages 1-2, miceli2024molecularpathwaysof pages 2-3)

---

## 5. Environmental Information

### 5.1 Lifestyle/clinical risk environment
The retrieved guideline evidence centers on medical risk-factor management (lipids, antithrombotics, blood pressure) rather than discrete environmental toxicants. (bushnell20242024guidelinefor pages 25-26)

### 5.2 Infectious agents
No infectious etiology was identified or suggested in the retrieved evidence set.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (atherosclerosis → stenosis → events)
1. **Atherogenesis** in carotid artery wall with lipid accumulation and immune activation → plaque growth and luminal narrowing. (miceli2024molecularpathwaysof pages 1-2)
2. **Plaque vulnerability phenotype** (thin fibrous cap, lipid-rich necrotic core, IPH, neovascularization, ulceration) increases rupture/embolization propensity, potentially **even when stenosis is <50%**. (miceli2024molecularpathwaysof pages 1-2)
3. **Rupture/ulceration** → local thrombosis and embolization → **TIA/stroke**. (miceli2024molecularpathwaysof pages 1-2, miceli2024molecularpathwaysof pages 10-11)

A 2024 molecular review characterizes vulnerable plaque heterogeneity and notes an immune-mediated cascade culminating in **“thromboinflammation.”** (miceli2024molecularpathwaysof pages 1-2)

### 6.2 Key molecular pathways and mediators (examples)
* **Inflammatory cytokines/mediators**: IL-6, IL-17 and others are described as elevated in unstable plaque contexts. (miceli2024molecularpathwaysof pages 2-3)
* **Oxidized LDL / lipid oxidation**: oxidized LDL is highlighted as a lipid-related marker linked to instability and thrombogenicity. (miceli2024molecularpathwaysof pages 1-2)
* **Extracellular matrix remodeling**: matrix metalloproteinases (e.g., MMP-9) contribute to fibrous-cap weakening by degrading collagen/elastin/proteoglycans. (miceli2024molecularpathwaysof pages 2-3)
* **Thrombotic/hemostatic coupling**: platelet/coagulation interactions and fibrinolytic enzymes contribute to embolic risk. (miceli2024molecularpathwaysof pages 2-3)

### 6.3 Cell types (suggested Cell Ontology terms)
* Vascular endothelial cell — *CL:0000115* (endothelial dysfunction/leukocyte recruitment) (miceli2024molecularpathwaysof pages 2-3)
* Vascular smooth muscle cell — *CL:0000192* (cap stability/ECM production) (miceli2024molecularpathwaysof pages 5-7)
* Macrophage — *CL:0000235* (inflammation, protease secretion, lipid handling) (miceli2024molecularpathwaysof pages 5-7)
* Platelet — *CL:0000233* (thromboinflammation) (miceli2024molecularpathwaysof pages 10-11)

### 6.4 Suggested GO Biological Process terms (non-exhaustive)
* Inflammatory response — *GO:0006954* (miceli2024molecularpathwaysof pages 2-3)
* Leukocyte migration — *GO:0050900*
* Extracellular matrix disassembly — *GO:0022617* (MMP activity) (miceli2024molecularpathwaysof pages 2-3)
* Response to oxidative stress — *GO:0006979* (miceli2024molecularpathwaysof pages 2-3)
* Blood coagulation — *GO:0007596* (miceli2024molecularpathwaysof pages 2-3)

### 6.5 Recent developments (2023–2024)
A major 2023–2024 theme is shifting from stenosis-percent thresholds alone to multi-parameter risk stratification incorporating vulnerable plaque imaging and biomarkers. A 2024 imaging meta-analysis supports that CT and MRI can detect vulnerable plaque with high accuracy compared with histology, enabling “stenosis and beyond” risk frameworks. (pakizer2024diagnosticaccuracyof pages 1-7)

---

## 7. Anatomical Structures Affected

### 7.1 Primary anatomy (suggested UBERON terms)
* Common carotid artery — *UBERON:0001649* (suggested)
* Internal carotid artery — *UBERON:0001647* (suggested)
* Carotid bifurcation / carotid bulb region (site of plaque formation; suggested)

### 7.2 Secondary organs/systems
* Brain/central nervous system: downstream ischemic injury causing TIA/stroke. (ristow2024brazilianangiologyand pages 8-9)

### 7.3 Subcellular/cellular compartments (suggested GO Cellular Component terms)
* Extracellular matrix — *GO:0031012* (ECM remodeling) (miceli2024molecularpathwaysof pages 2-3)

---

## 8. Temporal Development

### 8.1 Onset
Typically adult/older-adult onset as part of systemic atherosclerosis. (kim2023asymptomaticcarotidartery pages 1-2)

### 8.2 Progression
Atherosclerotic progression can be monitored by serial duplex ultrasound; AHA/ASA notes that for ACS >50%, surveillance every 6–12 months might be reasonable. (bushnell20242024guidelinefor pages 25-26)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent quantitative evidence)
* **General prevalence**: 0.1%–3.1% (2023 review). (kim2023asymptomaticcarotidartery pages 1-2)
* **High-risk registry cohort**: 6.3% prevalence of severe (≥70%) baseline asymptomatic stenosis (2024). (poorthuis2024predictionofsevere pages 1-2)

### 9.2 Population burden and stroke attribution
A 2024 guideline summary reports that ischemic strokes constitute **80–85%** of all strokes and that **~25% of ischemic strokes** are associated with cervical carotid artery disease. (ristow2024brazilianangiologyand pages 8-9)

### 9.3 Inheritance pattern
Complex, polygenic; shared cardiometabolic genetic loci and pathways are implicated rather than single-gene inheritance. (poorthuis2024predictionofsevere pages 1-2)

---

## 10. Diagnostics

### 10.1 First-line imaging: duplex ultrasound (DUS)
Real-world practice uses velocity thresholds to grade stenosis, but inter-center variability persists.
* In a 2024 UK/Ireland audit, common thresholds were PSV **>125 cm/s** for >50% stenosis and PSV **>230 cm/s** for >70% stenosis, with frequent use of PSV ratios (2–4 for moderate, >4 for severe). (trochowski2024currentpracticein pages 1-2)

**Visual evidence (cropped table):** duplex velocity thresholds and grading variability across centers are shown in a retrieved table image. (trochowski2024currentpracticein media 5fb82bca, trochowski2024currentpracticein media 4b772e98)

### 10.2 CTA/MRA corroboration
ESVS 2023 recommends corroborating DUS estimates with CTA/MRA (or repeat DUS by another operator) when considering CEA; and for CAS, recommends CTA/MRA to evaluate arch and extra-/intracranial circulation. (naylor2023editorschoice– pages 12-13)

### 10.3 Diagnostic performance (ESVS 2023 summary)
Compared with DSA reference, reported sensitivity/specificity are high for occlusion and moderate-to-high for stenosis by modality (DUS/CTA/CEMRA). (naylor2023editorschoice– pages 12-13)

### 10.4 Vulnerable plaque imaging (2024 evidence)
A 2024 systematic review/meta-analysis comparing noninvasive imaging to histology reports vulnerable plaque detection accuracy of **MRI 90%**, **CT 86%**, and **US 80%**, supporting greater use of CT/MRI compositional assessment for risk stratification. (pakizer2024diagnosticaccuracyof pages 1-7)

### 10.5 Differential diagnosis (high-level)
The retrieved evidence explicitly highlights entities that can mimic or extend “stenosis-only” paradigms (e.g., symptomatic non-stenotic carotid plaques) and emphasizes non-stenotic high-risk plaque features. (spiliopoulos2024cirsestandardsof pages 6-7)

### 10.6 Screening
AHA/ASA 2024: **routine population screening is not recommended** to reduce stroke risk. (bushnell20242024guidelinefor pages 25-26)

---

## 11. Outcome / Prognosis

### 11.1 Recent prognosis statistics
In a 2024 cohort (≈70,000 patient-years), there were **1,124 strokes** and **2,484 cardiovascular events** in a population used to validate a severe-ACAS prediction model; the burden concentrated in higher PACAS risk groups. (poorthuis2024predictionofsevere pages 1-2)

### 11.2 Procedural risks (CAS vs emergency CAS)
A 2024 real-world series reported in-hospital stroke/death of **0.8%** after elective CAS in symptomatic patients, versus **7.8%** complication rate for emergency CAS in acute stroke settings, emphasizing the importance of indication and context. (keil2024electivecarotidstenting pages 1-2)

---

## 12. Treatment

### 12.1 Medical therapy (best/intensive medical therapy)
AHA/ASA 2024 notes **statin-based medical therapy** is beneficial to reduce stroke risk in asymptomatic atherosclerotic carotid stenosis. (bushnell20242024guidelinefor pages 25-26)

### 12.2 Revascularization: CEA, CAS, and transcarotid approaches
* AHA/ASA 2024: for **asymptomatic extracranial carotid stenosis >70%**, shared decision-making is recommended to choose between revascularization and medical management; effectiveness of revascularization in those at high perioperative risk is not established. (bushnell20242024guidelinefor pages 25-26)
* CIRSE 2024: CAS has an established role, but evidence syntheses generally show higher peri-procedural stroke risk vs CEA and emphasize careful patient selection, embolic protection, blood pressure control, and structured follow-up. (spiliopoulos2024cirsestandardsof pages 6-7, spiliopoulos2024cirsestandardsof pages 7-9)

### 12.3 CAS best-practice elements (CIRSE 2024)
* Recommended DAPT example regimen: aspirin 75–100 mg + clopidogrel 75 mg; aspirin continued indefinitely after one month (practice standard). (spiliopoulos2024cirsestandardsof pages 6-7)
* Post-procedure surveillance: baseline DUS with follow-up at 1 and 6 months, then annually. (spiliopoulos2024cirsestandardsof pages 6-7)

### 12.4 TCAR and device innovation
ClinicalTrials.gov records show ongoing real-world implementation and evaluation of transcarotid neuroprotection systems, micromesh/covered stents, and TCAR strategies (e.g., NCT06653387; NCT04547387). (NCT06653387 chunk 3, NCT04547387 chunk 2)

### 12.5 Treatment ontology (suggested MAXO terms)
* Carotid endarterectomy — *MAXO:0000578* (suggested)
* Carotid artery stenting — *MAXO:0000793* (suggested)
* Statin therapy — *MAXO:0000746* (suggested)
* Antiplatelet therapy — *MAXO:0000744* (suggested)

---

## 13. Prevention

### 13.1 Primary prevention
AHA/ASA 2024 emphasizes prevention via evidence-based cardiovascular risk reduction; for carotid stenosis specifically it discourages routine screening and recommends statin-based therapy when asymptomatic stenosis is present. (bushnell20242024guidelinefor pages 25-26)

### 13.2 Secondary prevention / surveillance
For ACS >50%, periodic carotid DUS every 6–12 months might be reasonable to monitor progression and stroke risk. (bushnell20242024guidelinefor pages 25-26)

---

## 14. Other Species / Natural Disease
No retrieved primary evidence directly addressed naturally occurring carotid stenosis in non-human species or veterinary epidemiology; this section is therefore evidence-limited in the current tool-retrieved corpus.

---

## 15. Model Organisms
No retrieved primary evidence directly described dedicated carotid stenosis model organisms (e.g., mouse carotid flow-modification models) in a way that could be cited here; model-organism content is a gap in the retrieved evidence.

---

## Key evidence tables
The following artifacts summarize identifiers and quantitative thresholds.

| Concept/Identifier type | Identifier/value | Notes/definition snippet | Source (PMID/DOI/URL) | Publication year |
|---|---|---|---|---|
| MeSH | **D016893 — Carotid Stenosis** | MeSH term explicitly listed in CREST-related ClinicalTrials.gov records; placed under broader carotid artery/cerebrovascular disease hierarchy (NCT03121209 chunk 4, NCT05465122 chunk 2, NCT02089217 chunk 6, NCT05465122 chunk 3) | ClinicalTrials.gov NCT03121209; NCT02089217; NCT05465122 | 2014–2022 |
| Broader MeSH parent | **D002340 — Carotid Artery Diseases** | Ancestor term for carotid stenosis in trial ontology metadata; useful for broader disease mapping (NCT04547387 chunk 2, NCT03121209 chunk 4, NCT05465122 chunk 3, NCT06653387 chunk 3) | ClinicalTrials.gov NCT04547387; NCT03121209; NCT05465122; NCT06653387 | 2018–2024 |
| Clinical syndrome term | **Asymptomatic carotid artery stenosis (aCAS)** | Defined as stenosis of the extracranial carotid arteries **without a history of ipsilateral ischemic stroke or transient ischemic attack**; severe aCAS often referenced as **≥70%** (kim2023asymptomaticcarotidartery pages 1-1) | Kim et al. 2023, J NeuroInterv Surg. DOI: https://doi.org/10.1136/jnis-2022-018732 | 2023 |
| Guideline clinical term | **Symptomatic carotid disease / symptomatic carotid stenosis** | Brazilian guideline defines symptomatic disease as **one or more ischemic events in the carotid territory within the previous 6 months**; includes index/recurrent/recent event terminology (ristow2024brazilianangiologyand pages 14-16) | von Ristow et al. 2024. DOI: https://doi.org/10.1590/1677-5449.202300942 | 2024 |
| Guideline measurement system | **NASCET stenosis measurement** | ESVS 2023 adopts NASCET unless otherwise stated; mapping given as **NASCET 50% ≈ ECST 75%** and **NASCET 70% ≈ ECST 85%** (naylor2023editorschoice– pages 11-12) | Naylor et al. 2023. DOI: https://doi.org/10.1016/j.ejvs.2022.04.011 | 2023 |
| Guideline synonym/alternative scale | **ECST stenosis measurement** | Alternative European measurement method cross-mapped to NASCET in ESVS 2023; relevant when harmonizing older literature and imaging reports (naylor2023editorschoice– pages 11-12) | Naylor et al. 2023. DOI: https://doi.org/10.1016/j.ejvs.2022.04.011 | 2023 |
| Guideline lesion subtype | **Chronic near-occlusion (CNO) / near-occlusion** | ESVS describes angiographic near-occlusion using ≥2 features: delayed contrast filling, collateral recruitment, smaller distal ipsilateral ICA vs contralateral ICA, or distal ICA diameter ≤ ipsilateral ECA (naylor2023editorschoice– pages 11-12) | Naylor et al. 2023. DOI: https://doi.org/10.1016/j.ejvs.2022.04.011 | 2023 |
| Imaging/diagnostic synonym | **High-grade carotid stenosis** | CIRSE notes high-grade stenosis is characterized as **≥70% by NASCET**; symptomatic status linked to focal neurologic symptoms within prior 6 months (spiliopoulos2024cirsestandardsof pages 1-2) | Spiliopoulos et al. 2024. DOI: https://doi.org/10.1007/s00270-024-03707-y | 2024 |
| ICD coding note | **ICD-10 commonly used clinically: I65.2 (Occlusion and stenosis of carotid artery)** | No retrieved evidence passage explicitly provided ICD text/code mapping, so this should be treated as a common clinical coding note requiring direct verification in ICD source before KB ingestion | Not directly evidenced in retrieved context | — |
| MONDO note | **MONDO ID not found in retrieved sources** | No MONDO identifier was present in the retrieved guideline, trial, or review evidence set for carotid stenosis (bushnell20242024guidelinefor pages 25-26, kim2023asymptomaticcarotidartery pages 1-1) | Not available in retrieved sources | — |


*Table: This table compiles key carotid stenosis identifiers, naming conventions, and core definitional terms from the retrieved evidence base. It is useful for normalizing disease labels across guidelines, trials, and ontology-linked knowledge base entries.*

| Domain | Metric/threshold | Population/setting | Value(s) | Source with URL/DOI | Publication date/year |
|---|---|---|---|---|---|
| Epidemiology | Severe asymptomatic carotid artery stenosis (ACAS) prevalence | REACH-derived cohort, adults 45–80 years, no prior carotid procedures, n=26,384 | Severe baseline ACAS (≥70%) in 1,662/26,384 = **6.3%**; during ~70,000 patient-years: **1,124 strokes** and **2,484 CVD events**; high-risk PACAS group (27.7% of cohort) had **11.4%** severe ACAS prevalence and accounted for **56.6%** of incident strokes and **64.9%** of incident CVD events (poorthuis2024predictionofsevere pages 1-2) | Poorthuis et al., *Stroke* 2024. https://doi.org/10.1161/strokeaha.123.046894 | 2024 |
| Epidemiology | Population prevalence of asymptomatic carotid artery stenosis | General population review of aCAS | Estimated prevalence **0.1%–3.1%**; population-attributable stroke risk **0.7%** (kim2023asymptomaticcarotidartery pages 1-2, kim2023asymptomaticcarotidartery pages 1-1) | Kim et al., *J NeuroInterv Surg* 2023. https://doi.org/10.1136/jnis-2022-018732 | 2023 |
| Epidemiology | Historic randomized trial outcomes in asymptomatic disease | ACAS and ACST-1 trial populations | **ACAS**: n=1,662; perioperative risk **2.3%**; 5-year stroke **5.1% CEA vs 11.0% BMT**. **ACST-1**: n=3,120; 5-year stroke **6.4% CEA vs 11.8% BMT**. **ACST-2**: n=3,625; perioperative/study rates **3.7% CAS vs 2.7% CEA**; 5-year **5.3% CAS vs 4.5% CEA** (kim2023asymptomaticcarotidartery pages 1-2) | Kim et al., *J NeuroInterv Surg* 2023. https://doi.org/10.1136/jnis-2022-018732 | 2023 |
| Ultrasound grading | Common threshold for moderate carotid stenosis | UK & Ireland vascular units audit, 46 responding units | For **>50% stenosis**: PSV **>125 cm/s** used by **81%**; velocity ratio **2.0–4.0** used by **71%**; EDV used by **36%** (trochowski2024currentpracticein pages 2-3, trochowski2024currentpracticein pages 1-2, trochowski2024currentpracticein media 5fb82bca) | Trochowski et al., *J Vasc Soc Great Britain & Ireland* 2024. https://doi.org/10.54522/jvsgbi.2024.156 | 2024 |
| Ultrasound grading | Common threshold for severe carotid stenosis | UK & Ireland vascular units audit, 46 responding units | For **>70% stenosis**: PSV **>230 cm/s** used by **90%**; velocity ratio **>4.0** used by **86%**; EDV used by **43%** (trochowski2024currentpracticein pages 4-5, trochowski2024currentpracticein pages 3-4, trochowski2024currentpracticein pages 1-2, trochowski2024currentpracticein media 4b772e98) | Trochowski et al., *J Vasc Soc Great Britain & Ireland* 2024. https://doi.org/10.54522/jvsgbi.2024.156 | 2024 |
| Ultrasound grading | Near-occlusion/string sign criteria | UK & Ireland vascular units audit | Near-occlusion most often defined by narrow colour Doppler channel (**89%**) and velocity measurement (**76%**); a few units used **<20 cm/s** or **>400 cm/s** criteria; substantial variability remained (trochowski2024currentpracticein pages 4-5, trochowski2024currentpracticein media 5fb82bca) | Trochowski et al., *J Vasc Soc Great Britain & Ireland* 2024. https://doi.org/10.54522/jvsgbi.2024.156 | 2024 |
| Guidelines | Diagnostic performance of noninvasive imaging for stenosis/occlusion | ESVS 2023 guideline summary of DUS/CTA/CEMRA vs DSA | For **occlusion**: DUS/CTA/CEMRA sensitivity **97/97/99%**, specificity **99/99/99%**. For **stenosis**: DUS sensitivity **89%**, specificity **84%**; CTA sensitivity **75–85%**, specificity **93–96%**; CEMRA sensitivity **94–95%**, specificity **92–93%** (naylor2023editorschoice– pages 12-13) | Naylor et al., *Eur J Vasc Endovasc Surg* 2023. https://doi.org/10.1016/j.ejvs.2022.04.011 | 2023 |
| Guidelines | Stenosis measurement equivalence | ESVS 2023 guideline | **NASCET 50% ≈ ECST 75%**; **NASCET 70% ≈ ECST 85%** (naylor2023editorschoice– pages 11-12) | Naylor et al., *Eur J Vasc Endovasc Surg* 2023. https://doi.org/10.1016/j.ejvs.2022.04.011 | 2023 |
| Imaging vulnerable plaque | Accuracy for detecting vulnerable plaque vs histology | Systematic review/meta-analysis of CT, MRI, US | Vulnerable plaque detection accuracy: **MRI 90% (95% CI 82–95%)**, **CT 86% (76–92%)**, **US 80% (75–84%)** (pakizer2024diagnosticaccuracyof pages 1-7) | Pakizer et al., *Eur Heart J Cardiovasc Imaging* 2024. https://doi.org/10.1101/2023.09.25.23296124 | 2024 |
| Imaging vulnerable plaque | Sensitivity/specificity for vulnerable plaque | Meta-analysis analysis 1 | **CT** sensitivity/specificity/accuracy **86%/87%/86%**; **MRI 91%/91%/90%**; **US 84%/73%/80%** (pakizer2024diagnosticaccuracyof pages 28-33) | Pakizer et al., *Eur Heart J Cardiovasc Imaging* 2024. https://doi.org/10.1101/2023.09.25.23296124 | 2024 |
| Imaging vulnerable plaque | Accuracy for vulnerable plaque characteristics | Meta-analysis analysis 2 | Vulnerable characteristic accuracy: **CT 89%**, **MRI 86%**, **US 77%**; MRI visualized all **13** evaluated plaque characteristics (pakizer2024diagnosticaccuracyof pages 11-15, pakizer2024diagnosticaccuracyof pages 1-7) | Pakizer et al., *Eur Heart J Cardiovasc Imaging* 2024. https://doi.org/10.1101/2023.09.25.23296124 | 2024 |
| Treatment outcomes | Recommended peri-procedural antiplatelet regimen after CAS | CIRSE standards of practice | DAPT recommended: **aspirin 75–100 mg + clopidogrel 75 mg**, with aspirin continued indefinitely after **1 month**; surveillance DUS at **1 month, 6 months, then yearly** (spiliopoulos2024cirsestandardsof pages 6-7, spiliopoulos2024cirsestandardsof pages 2-4) | Spiliopoulos et al., *Cardiovasc Intervent Radiol* 2024. https://doi.org/10.1007/s00270-024-03707-y | 2024 |
| Treatment outcomes | CAS 30-day mortality/stroke in modern series | CIRSE guidance citing a 700-case series | **3.3%** 30-day mortality/stroke (spiliopoulos2024cirsestandardsof pages 6-7) | Spiliopoulos et al., *Cardiovasc Intervent Radiol* 2024. https://doi.org/10.1007/s00270-024-03707-y | 2024 |
| Treatment outcomes | Elective vs emergency CAS complications | Single-center 2012–2022 experience; 141 elective CAS, 158 emergency CAS | Elective symptomatic in-hospital stroke/death **0.8%**; asymptomatic elective CAS **0 complications**; emergency CAS procedure-related complications **7.8%** (keil2024electivecarotidstenting pages 1-2) | Keil et al., *RöFo* 2024. https://doi.org/10.1055/a-2175-4029 | 2024 |
| Guidelines | Screening and surveillance for asymptomatic extracranial carotid stenosis | AHA/ASA primary prevention guideline | **Routine population screening not recommended**; for **ACS >70%**, shared decision-making on revascularization vs medical management recommended; for **ACS >50%**, duplex ultrasound every **6–12 months** might be reasonable; statin-based therapy beneficial (bushnell20242024guidelinefor pages 25-26) | Bushnell et al., *Stroke* 2024. https://doi.org/10.1161/str.0000000000000475 | 2024 |
| Epidemiology / Guidelines | Global stroke burden and carotid contribution | Brazilian guideline summary | **12.2 million strokes/year** globally; incidence increased **50%** over 17 years; **80–85%** of strokes are ischemic; around **25%** of ischemic strokes are associated with cervical carotid artery disease (ristow2024brazilianangiologyand pages 8-9) | von Ristow et al., *J Vasc Bras* 2024. https://doi.org/10.1590/1677-5449.202300942 | 2024 |
| Treatment outcomes / Prevention | Lipid-lowering trial estimates relevant to carotid/vascular prevention | Brazilian guideline summary of PCSK9 evidence | Evolocumab lowered combined outcomes by **15%** (95% CI **0.79–0.92**, p<0.001) and reduced ischemic stroke by **25%** (95% CI **0.62–0.92**, p<0.005); alirocumab reduced outcomes from **3.3% to 1.7%** (OR **0.52**, 95% CI **0.31–0.90**, p=0.02) (ristow2024brazilianangiologyand pages 8-9) | von Ristow et al., *J Vasc Bras* 2024. https://doi.org/10.1590/1677-5449.202300942 | 2024 |


*Table: This table compiles recent numerical thresholds, prevalence estimates, imaging performance measures, treatment complication rates, and guideline recommendations relevant to carotid stenosis. It is useful as a quick-reference evidence summary for diagnostics, prognosis, and management.*

---

## Selected direct abstract quotes supporting key claims
* On symptomatic non-stenotic disease: “Symptomatic non-stenotic carotid plaques (SyNC) are an under-researched and under-recognized source of stroke.” (keil2024electivecarotidstenting pages 2-3)
* On vulnerable plaque concept and features: “Vulnerable plaques are characterized by… neovascularization; lipid-rich necrotic cores (LRNCs); intraplaque hemorrhage (IPH); thin fibrous caps; plaque surface ulceration…” and can matter “also in the case of non-significant (less than 50%) stenosis.” (miceli2024molecularpathwaysof pages 1-2)

---

## Notes on evidence limitations (important for KB ingestion)
* Formal ICD-10/ICD-11 and MONDO mappings were not present in the retrieved full text; they should be sourced directly from the respective coding/ontology databases rather than inferred. (artifact-00)
* Several widely used stenosis-grade cutoffs and peri-procedural risk thresholds are discussed across guidelines, but the retrieved ESVS excerpts did not capture all numeric recommendations verbatim; where necessary, this report relies on other 2024 guideline sources and practice standards present in the retrieved corpus. (bushnell20242024guidelinefor pages 25-26, ristow2024brazilianangiologyand pages 13-14)


References

1. (miceli2024molecularpathwaysof pages 1-2): Giuseppe Miceli, Maria Grazia Basso, Chiara Pintus, Andrea Roberta Pennacchio, Elena Cocciola, Mariagiovanna Cuffaro, Martina Profita, Giuliana Rizzo, and Antonino Tuttolomondo. Molecular pathways of vulnerable carotid plaques at risk of ischemic stroke: a narrative review. International Journal of Molecular Sciences, 25:4351, Apr 2024. URL: https://doi.org/10.3390/ijms25084351, doi:10.3390/ijms25084351. This article has 73 citations.

2. (pakizer2024diagnosticaccuracyof pages 1-7): David Pakizer, Jiří Kozel, Patrick Taffé, Jolanda Elmers, Janusz Feber, Patrik Michel, David Školoudík, and Gaia Sirimarco. Diagnostic accuracy of carotid plaque instability by noninvasive imaging: a systematic review and meta-analysis. European heart journal. Cardiovascular Imaging, Sep 2024. URL: https://doi.org/10.1101/2023.09.25.23296124, doi:10.1101/2023.09.25.23296124. This article has 19 citations.

3. (kim2023asymptomaticcarotidartery pages 1-1): Hyun Woo Kim, Robert W Regenhardt, Salvatore A D'Amato, Michael I Nahhas, Adam A Dmytriw, Joshua A Hirsch, Scott B Silverman, and Juan Carlos Martinez-Gutierrez. Asymptomatic carotid artery stenosis: a summary of current state of evidence for revascularization and emerging high-risk features. Journal of NeuroInterventional Surgery, 15:717-722, Sep 2023. URL: https://doi.org/10.1136/jnis-2022-018732, doi:10.1136/jnis-2022-018732. This article has 57 citations and is from a domain leading peer-reviewed journal.

4. (ristow2024brazilianangiologyand pages 14-16): Arno von Ristow, Bernardo Massière, Guilherme Vieira Meirelles, I. Casella, M. Morales, Ricardo Cesar Rocha Moreira, R. Procópio, Tércio Ferreira Oliveira, Walter Junior Boim de Araujo, E. Joviliano, and Júlio Cesar Peclat de Oliveira. Brazilian angiology and vascular surgery society guidelines for the treatment of extracranial cerebrovascular disease. Jornal Vascular Brasileiro, May 2024. URL: https://doi.org/10.1590/1677-5449.202300942, doi:10.1590/1677-5449.202300942. This article has 5 citations.

5. (NCT03121209 chunk 4): Randolph S. Marshall, MD. Carotid Revascularization and Medical Management for Asymptomatic Carotid Stenosis Trial - Hemodynamics (CREST-H). Columbia University. 2018. ClinicalTrials.gov Identifier: NCT03121209

6. (NCT02089217 chunk 6): James F. Meschia. Carotid Revascularization and Medical Management for Asymptomatic Carotid Stenosis Trial. Mayo Clinic. 2014. ClinicalTrials.gov Identifier: NCT02089217

7. (NCT06653387 chunk 3):  A Single-arm, Pivotal Study to Evaluate Acute Device and Technical Success of the CGuard Prime Carotid Stent System When Used in Conjunction to the ENROUTE Transcarotid Neuroprotection System in Patients Undergoing Carotid Artery Stenting Via the Transcarotid Artery Revascularization Approach. InspireMD. 2024. ClinicalTrials.gov Identifier: NCT06653387

8. (spiliopoulos2024cirsestandardsof pages 1-2): Stavros Spiliopoulos, Raphaël Blanc, Roberto Gandini, Stefan Müller-Hülsbeck, Wolfgang Reith, and Ornella Moschovaki-Zeiger. Cirse standards of practice on carotid artery stenting. Cardiovascular and Interventional Radiology, 47:705-716, Apr 2024. URL: https://doi.org/10.1007/s00270-024-03707-y, doi:10.1007/s00270-024-03707-y. This article has 18 citations and is from a peer-reviewed journal.

9. (trochowski2024currentpracticein pages 4-5): S. Trochowski, A. Akhtar, K. Bond, A. Corby, C. Hiscocks, D. Howard, R. Potter, P. Rothwell, E. Waldegrave, A. Webb, and O. Llwyd. Current practice in ultrasound grading of carotid artery stenosis in the uk and ireland. Journal of Vascular Societies Great Britain &amp; Ireland, 4:41-47, Nov 2024. URL: https://doi.org/10.54522/jvsgbi.2024.156, doi:10.54522/jvsgbi.2024.156. This article has 2 citations.

10. (naylor2023editorschoice– pages 11-12): Ross Naylor, Barbara Rantner, Stefano Ancetti, Gert J. de Borst, Marco De Carlo, Alison Halliday, Stavros K. Kakkos, Hugh S. Markus, Dominick J.H. McCabe, Henrik Sillesen, Jos C. van den Berg, Melina Vega de Ceniga, Maarit A. Venermo, Frank E.G. Vermassen, ESVS Guidelines Committee, George A. Antoniou, Frederico Bastos Goncalves, Martin Bjorck, Nabil Chakfe, Raphael Coscas, Nuno V. Dias, Florian Dick, Robert J. Hinchliffe, Philippe Kolh, Igor B. Koncar, Jes S. Lindholt, Barend M.E. Mees, Timothy A. Resch, Santi Trimarchi, Riikka Tulamo, Christopher P. Twine, Anders Wanhainen, Document Reviewers, Sergi Bellmunt-Montoya, Richard Bulbulia, R Clement Darling, Hans-Henning Eckstein, Athanasios Giannoukas, Mark J.W. Koelemay, David Lindström, Marc Schermerhorn, and David H. Stone. Editor's choice – european society for vascular surgery (esvs) 2023 clinical practice guidelines on the management of atherosclerotic carotid and vertebral artery disease. European Journal of Vascular and Endovascular Surgery, 65:7-111, Jan 2023. URL: https://doi.org/10.1016/j.ejvs.2022.04.011, doi:10.1016/j.ejvs.2022.04.011. This article has 881 citations and is from a domain leading peer-reviewed journal.

11. (bushnell20242024guidelinefor pages 25-26): Cheryl Bushnell, Walter N. Kernan, Anjail Z. Sharrief, Seemant Chaturvedi, John W. Cole, William K. Cornwell, Christine Cosby-Gaither, Sarah Doyle, Larry B. Goldstein, Olive Lennon, Deborah A. Levine, Mary Love, Eliza Miller, Mai Nguyen-Huynh, Jennifer Rasmussen-Winkler, Kathryn M. Rexrode, Nicole Rosendale, Satyam Sarma, Daichi Shimbo, Alexis N. Simpkins, Erica S. Spatz, Lisa R. Sun, Vin Tangpricha, Dawn Turnage, Gabriela Velazquez, and Paul K. Whelton. 2024 guideline for the primary prevention of stroke: a guideline from the american heart association/american stroke association. Stroke, Dec 2024. URL: https://doi.org/10.1161/str.0000000000000475, doi:10.1161/str.0000000000000475. This article has 333 citations and is from a highest quality peer-reviewed journal.

12. (poorthuis2024predictionofsevere pages 1-2): MD Michiel H.F. Poorthuis, PhD Steven H.J. Hageman, PhD Aernoud, MD T.L. Fiolet, PhD Jaap Kappelle, PhD Michiel L. Bots, P. Steg, MD Frank L.J. Visseren, PhD Deepak L. Bhatt, and M. M. G. J. D. Md. Prediction of severe baseline asymptomatic carotid stenosis and subsequent risk of stroke and cardiovascular disease. Stroke, 55:2632-2640, Nov 2024. URL: https://doi.org/10.1161/strokeaha.123.046894, doi:10.1161/strokeaha.123.046894. This article has 13 citations and is from a highest quality peer-reviewed journal.

13. (musialek2025strokeriskmanagement pages 61-62): Piotr Musialek, Leo H Bonati, Richard Bulbulia, Alison Halliday, Birgit Bock, Laura Capoccia, Hans-Henning Eckstein, Iris Q Grunwald, Peck Lin Lip, Andre Monteiro, Kosmas I Paraskevas, Anna Podlasek, Barbara Rantner, Kenneth Rosenfield, Adnan H Siddiqui, Henrik Sillesen, Isabelle Van Herzeele, Tomasz J Guzik, Lucia Mazzolai, Victor Aboyans, and Gregory Y H Lip. Stroke risk management in carotid atherosclerotic disease: a clinical consensus statement of the esc council on stroke and the esc working group on aorta and peripheral vascular diseases. Cardiovascular Research, 121:13-43, Aug 2025. URL: https://doi.org/10.1093/cvr/cvad135, doi:10.1093/cvr/cvad135. This article has 52 citations and is from a domain leading peer-reviewed journal.

14. (ristow2024brazilianangiologyand pages 8-9): Arno von Ristow, Bernardo Massière, Guilherme Vieira Meirelles, I. Casella, M. Morales, Ricardo Cesar Rocha Moreira, R. Procópio, Tércio Ferreira Oliveira, Walter Junior Boim de Araujo, E. Joviliano, and Júlio Cesar Peclat de Oliveira. Brazilian angiology and vascular surgery society guidelines for the treatment of extracranial cerebrovascular disease. Jornal Vascular Brasileiro, May 2024. URL: https://doi.org/10.1590/1677-5449.202300942, doi:10.1590/1677-5449.202300942. This article has 5 citations.

15. (NCT04547387 chunk 2):  TCAR Cerebral Protection And MicroNET-Covered Stent To Reduce Strokes. John Paul II Hospital, Krakow. 2020. ClinicalTrials.gov Identifier: NCT04547387

16. (ristow2024brazilianangiologyand pages 13-14): Arno von Ristow, Bernardo Massière, Guilherme Vieira Meirelles, I. Casella, M. Morales, Ricardo Cesar Rocha Moreira, R. Procópio, Tércio Ferreira Oliveira, Walter Junior Boim de Araujo, E. Joviliano, and Júlio Cesar Peclat de Oliveira. Brazilian angiology and vascular surgery society guidelines for the treatment of extracranial cerebrovascular disease. Jornal Vascular Brasileiro, May 2024. URL: https://doi.org/10.1590/1677-5449.202300942, doi:10.1590/1677-5449.202300942. This article has 5 citations.

17. (kim2023asymptomaticcarotidartery pages 1-2): Hyun Woo Kim, Robert W Regenhardt, Salvatore A D'Amato, Michael I Nahhas, Adam A Dmytriw, Joshua A Hirsch, Scott B Silverman, and Juan Carlos Martinez-Gutierrez. Asymptomatic carotid artery stenosis: a summary of current state of evidence for revascularization and emerging high-risk features. Journal of NeuroInterventional Surgery, 15:717-722, Sep 2023. URL: https://doi.org/10.1136/jnis-2022-018732, doi:10.1136/jnis-2022-018732. This article has 57 citations and is from a domain leading peer-reviewed journal.

18. (miceli2024molecularpathwaysof pages 2-3): Giuseppe Miceli, Maria Grazia Basso, Chiara Pintus, Andrea Roberta Pennacchio, Elena Cocciola, Mariagiovanna Cuffaro, Martina Profita, Giuliana Rizzo, and Antonino Tuttolomondo. Molecular pathways of vulnerable carotid plaques at risk of ischemic stroke: a narrative review. International Journal of Molecular Sciences, 25:4351, Apr 2024. URL: https://doi.org/10.3390/ijms25084351, doi:10.3390/ijms25084351. This article has 73 citations.

19. (miceli2024molecularpathwaysof pages 10-11): Giuseppe Miceli, Maria Grazia Basso, Chiara Pintus, Andrea Roberta Pennacchio, Elena Cocciola, Mariagiovanna Cuffaro, Martina Profita, Giuliana Rizzo, and Antonino Tuttolomondo. Molecular pathways of vulnerable carotid plaques at risk of ischemic stroke: a narrative review. International Journal of Molecular Sciences, 25:4351, Apr 2024. URL: https://doi.org/10.3390/ijms25084351, doi:10.3390/ijms25084351. This article has 73 citations.

20. (miceli2024molecularpathwaysof pages 5-7): Giuseppe Miceli, Maria Grazia Basso, Chiara Pintus, Andrea Roberta Pennacchio, Elena Cocciola, Mariagiovanna Cuffaro, Martina Profita, Giuliana Rizzo, and Antonino Tuttolomondo. Molecular pathways of vulnerable carotid plaques at risk of ischemic stroke: a narrative review. International Journal of Molecular Sciences, 25:4351, Apr 2024. URL: https://doi.org/10.3390/ijms25084351, doi:10.3390/ijms25084351. This article has 73 citations.

21. (trochowski2024currentpracticein pages 1-2): S. Trochowski, A. Akhtar, K. Bond, A. Corby, C. Hiscocks, D. Howard, R. Potter, P. Rothwell, E. Waldegrave, A. Webb, and O. Llwyd. Current practice in ultrasound grading of carotid artery stenosis in the uk and ireland. Journal of Vascular Societies Great Britain &amp; Ireland, 4:41-47, Nov 2024. URL: https://doi.org/10.54522/jvsgbi.2024.156, doi:10.54522/jvsgbi.2024.156. This article has 2 citations.

22. (trochowski2024currentpracticein media 5fb82bca): S. Trochowski, A. Akhtar, K. Bond, A. Corby, C. Hiscocks, D. Howard, R. Potter, P. Rothwell, E. Waldegrave, A. Webb, and O. Llwyd. Current practice in ultrasound grading of carotid artery stenosis in the uk and ireland. Journal of Vascular Societies Great Britain &amp; Ireland, 4:41-47, Nov 2024. URL: https://doi.org/10.54522/jvsgbi.2024.156, doi:10.54522/jvsgbi.2024.156. This article has 2 citations.

23. (trochowski2024currentpracticein media 4b772e98): S. Trochowski, A. Akhtar, K. Bond, A. Corby, C. Hiscocks, D. Howard, R. Potter, P. Rothwell, E. Waldegrave, A. Webb, and O. Llwyd. Current practice in ultrasound grading of carotid artery stenosis in the uk and ireland. Journal of Vascular Societies Great Britain &amp; Ireland, 4:41-47, Nov 2024. URL: https://doi.org/10.54522/jvsgbi.2024.156, doi:10.54522/jvsgbi.2024.156. This article has 2 citations.

24. (naylor2023editorschoice– pages 12-13): Ross Naylor, Barbara Rantner, Stefano Ancetti, Gert J. de Borst, Marco De Carlo, Alison Halliday, Stavros K. Kakkos, Hugh S. Markus, Dominick J.H. McCabe, Henrik Sillesen, Jos C. van den Berg, Melina Vega de Ceniga, Maarit A. Venermo, Frank E.G. Vermassen, ESVS Guidelines Committee, George A. Antoniou, Frederico Bastos Goncalves, Martin Bjorck, Nabil Chakfe, Raphael Coscas, Nuno V. Dias, Florian Dick, Robert J. Hinchliffe, Philippe Kolh, Igor B. Koncar, Jes S. Lindholt, Barend M.E. Mees, Timothy A. Resch, Santi Trimarchi, Riikka Tulamo, Christopher P. Twine, Anders Wanhainen, Document Reviewers, Sergi Bellmunt-Montoya, Richard Bulbulia, R Clement Darling, Hans-Henning Eckstein, Athanasios Giannoukas, Mark J.W. Koelemay, David Lindström, Marc Schermerhorn, and David H. Stone. Editor's choice – european society for vascular surgery (esvs) 2023 clinical practice guidelines on the management of atherosclerotic carotid and vertebral artery disease. European Journal of Vascular and Endovascular Surgery, 65:7-111, Jan 2023. URL: https://doi.org/10.1016/j.ejvs.2022.04.011, doi:10.1016/j.ejvs.2022.04.011. This article has 881 citations and is from a domain leading peer-reviewed journal.

25. (spiliopoulos2024cirsestandardsof pages 6-7): Stavros Spiliopoulos, Raphaël Blanc, Roberto Gandini, Stefan Müller-Hülsbeck, Wolfgang Reith, and Ornella Moschovaki-Zeiger. Cirse standards of practice on carotid artery stenting. Cardiovascular and Interventional Radiology, 47:705-716, Apr 2024. URL: https://doi.org/10.1007/s00270-024-03707-y, doi:10.1007/s00270-024-03707-y. This article has 18 citations and is from a peer-reviewed journal.

26. (keil2024electivecarotidstenting pages 1-2): Fee Keil, Simon Stahn, Sarah Christina Reitz, Franziska Lieschke, Richard du Mesnil de Rochemont, Elke Hattingen, and Joachim Berkefeld. Elective carotid stenting fulfills quality standards defined in guidelines. RöFo - Fortschritte auf dem Gebiet der Röntgenstrahlen und der bildgebenden Verfahren, 196:471-481, Nov 2024. URL: https://doi.org/10.1055/a-2175-4029, doi:10.1055/a-2175-4029. This article has 1 citations.

27. (spiliopoulos2024cirsestandardsof pages 7-9): Stavros Spiliopoulos, Raphaël Blanc, Roberto Gandini, Stefan Müller-Hülsbeck, Wolfgang Reith, and Ornella Moschovaki-Zeiger. Cirse standards of practice on carotid artery stenting. Cardiovascular and Interventional Radiology, 47:705-716, Apr 2024. URL: https://doi.org/10.1007/s00270-024-03707-y, doi:10.1007/s00270-024-03707-y. This article has 18 citations and is from a peer-reviewed journal.

28. (NCT05465122 chunk 2): James F. Meschia. CREST-2 Long-term Observational Extension Study. Mayo Clinic. 2022. ClinicalTrials.gov Identifier: NCT05465122

29. (NCT05465122 chunk 3): James F. Meschia. CREST-2 Long-term Observational Extension Study. Mayo Clinic. 2022. ClinicalTrials.gov Identifier: NCT05465122

30. (trochowski2024currentpracticein pages 2-3): S. Trochowski, A. Akhtar, K. Bond, A. Corby, C. Hiscocks, D. Howard, R. Potter, P. Rothwell, E. Waldegrave, A. Webb, and O. Llwyd. Current practice in ultrasound grading of carotid artery stenosis in the uk and ireland. Journal of Vascular Societies Great Britain &amp; Ireland, 4:41-47, Nov 2024. URL: https://doi.org/10.54522/jvsgbi.2024.156, doi:10.54522/jvsgbi.2024.156. This article has 2 citations.

31. (trochowski2024currentpracticein pages 3-4): S. Trochowski, A. Akhtar, K. Bond, A. Corby, C. Hiscocks, D. Howard, R. Potter, P. Rothwell, E. Waldegrave, A. Webb, and O. Llwyd. Current practice in ultrasound grading of carotid artery stenosis in the uk and ireland. Journal of Vascular Societies Great Britain &amp; Ireland, 4:41-47, Nov 2024. URL: https://doi.org/10.54522/jvsgbi.2024.156, doi:10.54522/jvsgbi.2024.156. This article has 2 citations.

32. (pakizer2024diagnosticaccuracyof pages 28-33): David Pakizer, Jiří Kozel, Patrick Taffé, Jolanda Elmers, Janusz Feber, Patrik Michel, David Školoudík, and Gaia Sirimarco. Diagnostic accuracy of carotid plaque instability by noninvasive imaging: a systematic review and meta-analysis. European heart journal. Cardiovascular Imaging, Sep 2024. URL: https://doi.org/10.1101/2023.09.25.23296124, doi:10.1101/2023.09.25.23296124. This article has 19 citations.

33. (pakizer2024diagnosticaccuracyof pages 11-15): David Pakizer, Jiří Kozel, Patrick Taffé, Jolanda Elmers, Janusz Feber, Patrik Michel, David Školoudík, and Gaia Sirimarco. Diagnostic accuracy of carotid plaque instability by noninvasive imaging: a systematic review and meta-analysis. European heart journal. Cardiovascular Imaging, Sep 2024. URL: https://doi.org/10.1101/2023.09.25.23296124, doi:10.1101/2023.09.25.23296124. This article has 19 citations.

34. (spiliopoulos2024cirsestandardsof pages 2-4): Stavros Spiliopoulos, Raphaël Blanc, Roberto Gandini, Stefan Müller-Hülsbeck, Wolfgang Reith, and Ornella Moschovaki-Zeiger. Cirse standards of practice on carotid artery stenting. Cardiovascular and Interventional Radiology, 47:705-716, Apr 2024. URL: https://doi.org/10.1007/s00270-024-03707-y, doi:10.1007/s00270-024-03707-y. This article has 18 citations and is from a peer-reviewed journal.

35. (keil2024electivecarotidstenting pages 2-3): Fee Keil, Simon Stahn, Sarah Christina Reitz, Franziska Lieschke, Richard du Mesnil de Rochemont, Elke Hattingen, and Joachim Berkefeld. Elective carotid stenting fulfills quality standards defined in guidelines. RöFo - Fortschritte auf dem Gebiet der Röntgenstrahlen und der bildgebenden Verfahren, 196:471-481, Nov 2024. URL: https://doi.org/10.1055/a-2175-4029, doi:10.1055/a-2175-4029. This article has 1 citations.