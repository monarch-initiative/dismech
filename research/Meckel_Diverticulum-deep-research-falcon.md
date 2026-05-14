---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T11:45:08.926375'
end_time: '2026-05-09T11:56:13.950390'
duration_seconds: 665.02
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Meckel Diverticulum
  mondo_id: ''
  category: Congenital
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Meckel Diverticulum
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Meckel Diverticulum** covering all of the
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
- **Disease Name:** Meckel Diverticulum
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Meckel Diverticulum** covering all of the
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


# Meckel Diverticulum (Congenital) — Disease Characteristics Research Report

## Scope, evidence base, and limitations
This report synthesizes evidence from recent peer‑reviewed clinical series and reviews retrieved via the provided tools, prioritizing 2023–2025 sources where available. Primary evidence includes: a 2023 *Pediatric Radiology* review of Meckel diverticulum (MD) scintigraphy and pitfalls; a 2024 hospital series describing presentation and operative management; a 2023 adult surgical series; a 2025 multicenter pediatric symptomatic cohort; and a 2025 paper comparing pantoprazole vs ranitidine premedication in MD scintigraphy. Where identifiers (e.g., MONDO, MeSH, ICD-10) are requested, the current tool session did **not** retrieve authoritative ontology/registry pages, so those identifiers are marked as **not available from retrieved evidence**.

**Key sources (publication date; URL):**
- Aboughalia et al., Nov 2023, *Pediatric Radiology* — https://doi.org/10.1007/s00247-022-05527-z (aboughalia2023meckeldiverticulumscintigraphy pages 1-3)
- Hernández et al., Dec 2023, *Frontiers in Surgery* — https://doi.org/10.3389/fsurg.2023.1327545 (hernandez2023meckelsdiverticulumanalysis pages 2-4, hernandez2023meckelsdiverticulumanalysis pages 1-2)
- Jarboa et al., Dec 2024, *Turkish Journal of Surgery* — https://doi.org/10.47717/turkjsurg.2024.6446 (jarboa2024theclinicalpresentation pages 1-2)
- Önner et al., Jun 2025, *Pediatric Radiology* — https://doi.org/10.1007/s00247-025-06284-5 (onner2025premedicationinpediatric pages 1-3, onner2025premedicationinpediatric pages 3-4, onner2025premedicationinpediatric pages 4-6, onner2025premedicationinpediatric media a6df16f3, onner2025premedicationinpediatric media 9c9d2a7f)
- Zvizdic et al., Oct 2025, *Pediatric Surgery International* — https://doi.org/10.1007/s00383-025-06197-2 (zvizdic2025diverseclinicalfeatures pages 2-4)

---

## 1. Disease information
### 1.1. Overview (definition; current understanding)
Meckel diverticulum is a **congenital true diverticulum** of the ileum caused by failed involution/obliteration of the **omphalomesenteric (vitelline) duct** during embryogenesis; the duct normally involutes during approximately the **5th–9th week** of gestation. (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, dyn2023mechanicalileusof pages 1-3, hernandez2023meckelsdiverticulumanalysis pages 1-2)

**Direct abstract-supported definition (recent):** Aboughalia et al. describe MD as the “commonest congenital GI anomaly” resulting from aberrant involution of the omphalomesenteric duct, and emphasize that **ectopic gastric mucosa** is the scintigraphic target for Tc‑99m pertechnetate imaging. (aboughalia2023meckeldiverticulumscintigraphy pages 1-3)

### 1.2. Key identifiers
Not reliably extractable from the retrieved full-text evidence in this tool session:
- **MONDO ID:** not available from retrieved evidence.
- **MeSH:** not available from retrieved evidence.
- **ICD-10/ICD-11:** not available from retrieved evidence.
- **OMIM/Orphanet:** not available from retrieved evidence.

### 1.3. Synonyms / alternative names
Synonyms used across sources:
- **Meckel’s diverticulum** (standard) (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, jarboa2024theclinicalpresentation pages 1-2, zvizdic2025diverseclinicalfeatures pages 2-4)
- **Meckel diverticulum** (without possessive) (aboughalia2023meckeldiverticulumscintigraphy pages 1-3)
- **Vitelline/omphalomesenteric duct remnant** (conceptual synonym) (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, dyn2023mechanicalileusof pages 1-3, hernandez2023meckelsdiverticulumanalysis pages 1-2)

### 1.4. Source granularity
The evidence base includes both:
- **Aggregated disease-level resources/reviews** (e.g., imaging technique and pitfalls) (aboughalia2023meckeldiverticulumscintigraphy pages 1-3)
- **Institutional or multicenter clinical cohorts** (adult and pediatric) (jarboa2024theclinicalpresentation pages 1-2, zvizdic2025diverseclinicalfeatures pages 2-4, hernandez2023meckelsdiverticulumanalysis pages 2-4)

---

## 2. Etiology
### 2.1. Disease causal factors
**Primary cause:** embryologic failure of regression/obliteration of the omphalomesenteric (vitelline) duct, yielding a persistent diverticulum in the distal ileum. (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, dyn2023mechanicalileusof pages 1-3, hernandez2023meckelsdiverticulumanalysis pages 1-2)

### 2.2. Risk factors
In the retrieved evidence, “risk factors” are primarily **demographic and anatomic correlates** rather than genetic/environmental exposures:
- **Male sex**: multiple cohorts show strong male predominance among symptomatic MD cases (e.g., 80.1% male in a pediatric symptomatic cohort; 88.5% male in an 8‑year mixed series; 81.4% male in an adult surgical cohort). (zvizdic2025diverseclinicalfeatures pages 2-4, jarboa2024theclinicalpresentation pages 1-2, hernandez2023meckelsdiverticulumanalysis pages 2-4)
- **Longer diverticulum length**: Jarboa et al. conclude that “the longer Meckel's diverticulum is, the more prone it is to developing complications” (from abstract text). (jarboa2024theclinicalpresentation pages 1-2)

**Environmental risk factors:** not identified in the retrieved evidence.

### 2.3. Protective factors
No genetic or environmental protective factors were identified in the retrieved evidence.

### 2.4. Gene–environment interactions
No gene–environment interaction evidence was identified in the retrieved evidence.

---

## 3. Phenotypes (clinical manifestations)
### 3.1. Core phenotype spectrum
MD can be asymptomatic/incidental or symptomatic with major presentations including **painless lower GI bleeding**, **intestinal obstruction**, **diverticulitis/peritonitis**, and less commonly **perforation**. (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, zvizdic2025diverseclinicalfeatures pages 2-4, hernandez2023meckelsdiverticulumanalysis pages 1-2)

Aboughalia et al. summarize major complications as: “painless bleeding, diverticulitis, perforation, bowel obstruction (from intussusception, volvulus, fibrous bands or Littre hernia) and rarely malignancy.” (aboughalia2023meckeldiverticulumscintigraphy pages 1-3)

### 3.2. Presentation frequencies (recent cohorts)
- **Pediatric symptomatic multicenter cohort (n=151)**: obstruction 38.4%, GI bleeding 37.8%, peritonitis 23.8%; 63.6% had multiple symptoms. (zvizdic2025diverseclinicalfeatures pages 2-4)
- **Mixed clinical series (n=104)**: among emergency presentations: abdominal pain 42.5%, obstruction 25%, bleeding per rectum 15%, acute abdomen 11.3%, intussusception 6.2%. (jarboa2024theclinicalpresentation pages 1-2)
- **Adult surgical series (n=27)**: symptom mechanisms included obstruction (13/27), inflammation (5/27), bleeding (3/27), perforation (1/27); abdominal pain was common (22/27). (hernandez2023meckelsdiverticulumanalysis pages 2-4)

### 3.3. Suggested HPO terms (non-exhaustive)
Based on the phenotype spectrum reported in the retrieved evidence:
- GI bleeding/hematochezia: **HP:0001892 (Gastrointestinal hemorrhage)**; **HP:0001903 (Hematochezia)**
- Abdominal pain/acute abdomen: **HP:0002027 (Abdominal pain)**; **HP:0030654 (Acute abdomen)**
- Bowel obstruction/ileus: **HP:0002583 (Intestinal obstruction)**
- Intussusception: **HP:0002029 (Intussusception)**
- Vomiting: **HP:0002013 (Vomiting)**
- Diarrhea: **HP:0002014 (Diarrhea)**
- Peritonitis: **HP:0002586 (Peritonitis)**
- Anemia (secondary to bleeding): **HP:0001903 (Anemia)**

**Frequency note:** HPO mapping above is qualitative; frequencies should be taken from cohort data cited in Section 3.2. (jarboa2024theclinicalpresentation pages 1-2, zvizdic2025diverseclinicalfeatures pages 2-4, hernandez2023meckelsdiverticulumanalysis pages 2-4)

### 3.4. Quality of life impact
Formal patient-reported quality-of-life instruments (e.g., EQ‑5D/SF‑36) were not described in the retrieved evidence. Clinically, presentations such as GI bleeding, acute abdomen, and obstruction typically require emergency evaluation and surgery (pediatric and adult cohorts), implying substantial acute functional impact. (jarboa2024theclinicalpresentation pages 1-2, zvizdic2025diverseclinicalfeatures pages 2-4)

---

## 4. Genetic / molecular information
### 4.1. Causal genes / pathogenic variants
No monogenic etiology, causal genes, or pathogenic variants were identified in the retrieved evidence, consistent with MD being primarily a **developmental anatomic anomaly** rather than a single-gene disorder in routine clinical characterization. (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, hernandez2023meckelsdiverticulumanalysis pages 1-2)

### 4.2. Modifier genes / epigenetics / chromosomal abnormalities
No evidence identified in retrieved documents.

---

## 5. Environmental information
No specific environmental, lifestyle, or infectious causal contributors were identified in the retrieved evidence.

---

## 6. Mechanism / pathophysiology
### 6.1. Core mechanistic chain (accepted clinical mechanism)
1) **Embryologic persistence** of the omphalomesenteric duct produces an ileal true diverticulum. (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, dyn2023mechanicalileusof pages 1-3)
2) Many MD contain **ectopic mucosa**, especially **gastric mucosa** (up to ~50–60% in an imaging-focused review; 55.6% ectopic tissue in a pediatric symptomatic cohort). (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, zvizdic2025diverseclinicalfeatures pages 2-4)
3) **Ectopic gastric mucosa** can drive ulceration and **painless lower GI bleeding**, particularly in pediatrics; Aboughalia et al. state MD with ectopic gastric mucosa account for “>50% of unexplained pediatric lower GI bleeding.” (aboughalia2023meckeldiverticulumscintigraphy pages 1-3)
4) Obstruction arises via **intussusception, volvulus, fibrous bands, inflammation, or enteroliths**, producing acute abdomen, vomiting, distention, and requiring surgical management. (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, zvizdic2025diverseclinicalfeatures pages 2-4, dyn2023mechanicalileusof pages 1-3)

### 6.2. Suggested GO biological process terms (examples)
- **GO:0002526** acute inflammatory response (diverticulitis/peritonitis context)
- **GO:0006954** inflammatory response
- **GO:0007596** blood coagulation / hemostasis (bleeding context)
- **GO:0006950** response to stress (acute hemorrhage/ischemia context)

### 6.3. Suggested cell types (Cell Ontology; examples)
Mechanism centers on mucosal epithelium and ectopic gastric tissue:
- **Gastric parietal cell** (acid secretion; scintigraphic signal retention discussion in premedication paper) (onner2025premedicationinpediatric pages 4-6)
- **Intestinal epithelial cell** (ileal mucosa)
- **Smooth muscle cell** (bowel motility/obstruction context)

### 6.4. Advanced molecular profiling
No transcriptomic/proteomic/metabolomic or single-cell/spatial omics evidence was identified in retrieved documents.

---

## 7. Anatomical structures affected
### 7.1. Organ / system level
- Primary: **small intestine (ileum)**; classically antimesenteric border near the ileocecal valve. (jarboa2024theclinicalpresentation pages 1-2, dyn2023mechanicalileusof pages 1-3)
- Complication involvement: intestinal lumen (bleeding), peritoneum (peritonitis), mesentery/bands (obstruction/volvulus). (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, zvizdic2025diverseclinicalfeatures pages 2-4)

### 7.2. Suggested UBERON terms (examples)
- **UBERON:0002108** small intestine
- **UBERON:0002116** ileum
- **UBERON:0001155** ileocecal valve
- **UBERON:0003688** peritoneum

---

## 8. Temporal development
- **Onset:** congenital (anomaly present at birth), but symptomatic presentation is age-dependent.
  - Pediatric symptomatic median age 6.7 years (IQR 1.5–10.8) in a multicenter cohort. (zvizdic2025diverseclinicalfeatures pages 2-4)
  - Adult cohorts demonstrate presentations in adulthood with varied complications and frequent diagnostic uncertainty. (hernandez2023meckelsdiverticulumanalysis pages 2-4)
- **Course pattern:** asymptomatic/incidental in many; episodic or acute presentations when complicated (bleeding, obstruction, diverticulitis/peritonitis). (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, jarboa2024theclinicalpresentation pages 1-2)

---

## 9. Inheritance and population
### 9.1. Epidemiology (prevalence/incidence; demographics)
- Population prevalence estimates in retrieved evidence are typically around **~1–3%** and **~2–3%**. (dyn2023mechanicalileusof pages 1-3, aboughalia2023meckeldiverticulumscintigraphy pages 1-3)
- Sex ratio: male predominance among symptomatic presentations is repeatedly noted.
  - Imaging review provides a male:female ratio around **~2–3:1**. (aboughalia2023meckeldiverticulumscintigraphy pages 1-3)
  - Pediatric symptomatic cohort: **80.1% male**. (zvizdic2025diverseclinicalfeatures pages 2-4)
  - Adult surgical cohort: **81.4% male**. (hernandez2023meckelsdiverticulumanalysis pages 2-4)

### 9.2. Inheritance pattern
No inheritance pattern was reported in retrieved evidence; MD is generally treated clinically as a sporadic congenital developmental anomaly (not demonstrated as Mendelian in the retrieved sources).

---

## 10. Diagnostics
### 10.1. Imaging and endoscopic testing
**Tc‑99m pertechnetate Meckel scintigraphy (Meckel scan):**
- Aboughalia et al. describe Tc‑99m pertechnetate scintigraphy as emphasizing ectopic gastric mucosa and report **~90% accuracy in children** (review-level estimate). (aboughalia2023meckeldiverticulumscintigraphy pages 1-3)
- In a large pediatric symptomatic cohort, Tc‑99m scan was **positive in 80.7%** of bleeding cases (46/57). (zvizdic2025diverseclinicalfeatures pages 2-4)
- Limitations/pitfalls: the imaging review emphasizes attention to normal tracer biodistribution and labeling-agent effects (e.g., stannous ion persistence) to avoid misinterpretation. (aboughalia2023meckeldiverticulumscintigraphy pages 1-3)

**Optimization of scintigraphy via premedication (recent development):**
- Önner et al. highlight that “H2 receptor antagonists enhance the sensitivity of Meckel scintigraphy… by delaying the luminal release of 99mTc‑pertechnetate from the parietal and mucus cells,” and compared ranitidine vs pantoprazole after ranitidine withdrawal. (onner2025premedicationinpediatric pages 4-6)
- In 141 children, scan-quality categories were similar between pantoprazole and ranitidine (no significant differences), and positive scans were surgically confirmed; pantoprazole was “equivalent” to ranitidine in scan quality and lesion‑to‑background ratios. (onner2025premedicationinpediatric pages 1-3, onner2025premedicationinpediatric pages 3-4, onner2025premedicationinpediatric pages 4-6)

**Ultrasound and CT (real-world yields in symptomatic pediatric cohort):**
- In Zvizdic et al., ultrasound detected no MD (0% yield in their cohort), while CT identified MD in **11.9%** (5/42). (zvizdic2025diverseclinicalfeatures pages 2-4)

### 10.2. Operative/pathology confirmation
Multiple cohorts emphasize that MD is often diagnosed definitively intraoperatively and confirmed by histopathology, including ectopic tissue assessment. (zvizdic2025diverseclinicalfeatures pages 2-4, hernandez2023meckelsdiverticulumanalysis pages 2-4)

### 10.3. Suggested differential diagnoses (from presentation overlap)
The retrieved evidence specifically emphasizes diagnostic challenge and underdiagnosis in non-bleeding cases, implying common differentials by syndrome (acute abdomen/bleeding/obstruction), including appendicitis-like presentations and other causes of pediatric lower GI bleeding. (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, hernandez2023meckelsdiverticulumanalysis pages 1-2)

---

## 11. Outcome / prognosis
### 11.1. Surgical outcomes (recent pediatric multicenter data)
In 151 pediatric symptomatic cases, postoperative complications occurred in **~5.3%** with **no mortality** reported during follow-up. (zvizdic2025diverseclinicalfeatures pages 2-4)

### 11.2. Adult outcomes
Adult series report variable hospital length of stay and high rates of diagnostic uncertainty before surgery; quantitative mortality was not extractable from the retrieved adult cohort snippets. (hernandez2023meckelsdiverticulumanalysis pages 2-4)

---

## 12. Treatment
### 12.1. Standard of care (current practice)
Surgery is repeatedly described as the cornerstone/definitive management for symptomatic MD:
- Adult cohort: all 27 cases underwent resection via diverticulectomy or segmental small bowel resection with anastomosis. (hernandez2023meckelsdiverticulumanalysis pages 2-4)
- Pediatric multicenter cohort: segmental small-bowel resection (80.8%) was more common than simple diverticulectomy (19.2%), reflecting complicated presentations and need to resect adjacent bowel. (zvizdic2025diverseclinicalfeatures pages 2-4)

### 12.2. Surgical modalities (real-world implementations)
- Pediatric cohort: laparotomy 72.2%, laparoscopy 23.2%, conversion 4.6%. (zvizdic2025diverseclinicalfeatures pages 2-4)
- Adult cohort: totally laparoscopic, laparoscopic-assisted, and open approaches were all used. (hernandez2023meckelsdiverticulumanalysis pages 2-4)

### 12.3. Incidental/asymptomatic MD resection (expert controversy)
Incidental MD management remains debated in practice; however, cohort data show incidental resections occur:
- Jarboa et al.: 23% incidental findings; authors state that resection of incidental MD “does not increase the risk of morbidity” (from abstract conclusion). (jarboa2024theclinicalpresentation pages 1-2)
- Hernández et al.: asymptomatic incidental diverticula were resected in 5 patients in their adult series. (hernandez2023meckelsdiverticulumanalysis pages 2-4)

### 12.4. MAXO suggestions (examples)
- **Diverticulectomy / surgical excision of diverticulum** (MAXO term: surgical excision procedure)
- **Segmental small bowel resection with anastomosis** (MAXO: intestinal resection)
- **Laparoscopic surgery** (MAXO: minimally invasive surgical procedure)

### 12.5. Pharmacotherapy
No disease-modifying pharmacotherapy exists for the anatomic lesion itself in the retrieved evidence. Acid suppression is used diagnostically to optimize scintigraphy rather than treat the diverticulum (premedication for imaging). (onner2025premedicationinpediatric pages 1-3, onner2025premedicationinpediatric pages 4-6)

---

## 13. Prevention
No primary prevention (preventing occurrence) strategies were identified; MD is congenital. Secondary/tertiary prevention in practice includes:
- maintaining clinical suspicion and appropriate workup for unexplained pediatric lower GI bleeding (Tc‑99m pertechnetate scan) (aboughalia2023meckeldiverticulumscintigraphy pages 1-3, zvizdic2025diverseclinicalfeatures pages 2-4)
- surgical management to prevent recurrent bleeding/obstruction once symptomatic and diagnosed (zvizdic2025diverseclinicalfeatures pages 2-4, hernandez2023meckelsdiverticulumanalysis pages 2-4)

---

## 14. Other species / natural disease
No evidence was retrieved in this tool session describing naturally occurring Meckel diverticulum in non-human species.

---

## 15. Model organisms
No specific animal or experimental model organism evidence for MD was retrieved in this tool session.

---

## Recent developments (2023–2025) and expert analysis (authoritative sources)
1) **Updated scintigraphy technique and pitfalls (2023):** The *Pediatric Radiology* review emphasizes modern best practices and common interpretive pitfalls for Tc‑99m pertechnetate imaging, highlighting the continued central role of scintigraphy for suspected bleeding MD in children. (aboughalia2023meckeldiverticulumscintigraphy pages 1-3)
2) **Evidence on real-world diagnostic yields (2025 pediatric multicenter):** Ultrasound and CT had low preoperative detection rates in symptomatic MD, while Tc‑99m scans were frequently positive in bleeding presentations (80.7%). This supports a bleeding‑phenotype–guided diagnostic pathway. (zvizdic2025diverseclinicalfeatures pages 2-4)
3) **Protocol adaptation after ranitidine withdrawal (2025):** Önner et al. provide practical evidence that IV pantoprazole can substitute for ranitidine without degrading scan quality metrics, reflecting real-world protocol change driven by drug availability and safety considerations. (onner2025premedicationinpediatric pages 1-3, onner2025premedicationinpediatric pages 3-4, onner2025premedicationinpediatric pages 4-6, onner2025premedicationinpediatric media a6df16f3, onner2025premedicationinpediatric media 9c9d2a7f)

---

## Evidence summary table
The following table consolidates quantitative findings extracted from the retrieved sources.

| Study (year, journal) | Population (pediatric/adult; n) | Key epidemiology (prevalence/incidence/sex ratio) | Presentation frequencies | Ectopic mucosa frequencies | Diagnostic performance stats | Treatment approach stats | Outcomes/complications |
|---|---|---|---|---|---|---|---|
| Aboughalia 2023, *Pediatric Radiology* | Review; population-level | Incidence/prevalence 2–3% of population; male:female ~2–3:1; “rule of 2s” includes ~2 ft from ileocecal valve and ~2 inches long (aboughalia2023meckeldiverticulumscintigraphy pages 1-3) | Meckel diverticula with ectopic gastric mucosa account for >50% of unexplained pediatric lower GI bleeding; complications listed include painless bleeding, diverticulitis, perforation, bowel obstruction, rare malignancy (aboughalia2023meckeldiverticulumscintigraphy pages 1-3) | Gastric mucosa up to 50–60%; pancreatic mucosa up to 16% (aboughalia2023meckeldiverticulumscintigraphy pages 1-3) | Tc-99m pertechnetate scintigraphy accuracy ~90% in children (aboughalia2023meckeldiverticulumscintigraphy pages 1-3) | NR (aboughalia2023meckeldiverticulumscintigraphy pages 1-3) | NR quantitatively in snippet (aboughalia2023meckeldiverticulumscintigraphy pages 1-3) |
| Jarboa 2024, *Turkish Journal of Surgery* | Mixed clinical series; n=104 | Present in ~2–3% of population; male 92/104 (88.5%); symptomatic 80/104 (77%); incidental 24/104 (23%) (jarboa2024theclinicalpresentation pages 1-2) | Abdominal pain 34/80 (42.5%); intestinal obstruction 20/80 (25%); bleeding per rectum 12/80 (15%); acute abdomen 9/80 (11.3%); intussusception 5/80 (6.2%) (jarboa2024theclinicalpresentation pages 1-2) | Ectopic gastric mucosa 30/104 (28.8%); background review figures: gastric ~50%, pancreatic ~5% (jarboa2024theclinicalpresentation pages 1-2) | Diagnostic workup used US, endoscopy/capsule, CT, MRI, enterography, Meckel scan; no sensitivity/specificity reported in snippet (jarboa2024theclinicalpresentation pages 1-2) | Small bowel resection 41/91 (45.1%); stapled resection 44/91 (48.3%); ligation of base 6/91 (6.4%) (jarboa2024theclinicalpresentation pages 1-2) | Authors state incidental resection did not increase morbidity; no numeric mortality in snippet (jarboa2024theclinicalpresentation pages 1-2) |
| Hernández 2023, *Frontiers in Surgery* | Adult series; n=27 | Male 22/27 (81.4%); symptomatic group n=22 with 18 male and 4 female; mean diverticulum–ileocecal valve distance 63.4 cm (hernandez2023meckelsdiverticulumanalysis pages 2-4, hernandez2023meckelsdiverticulumanalysis pages 1-2) | Abdominal pain 22/27 (85% in abstract; 22 cases in evidence table); vomiting 10/27; diarrhea 6/27; mechanisms: obstruction 13/27, inflammation 5/27, bleeding 3/27, perforation 1/27; 82% of symptomatic patients had ≥2 symptoms (hernandez2023meckelsdiverticulumanalysis pages 2-4, hernandez2023meckelsdiverticulumanalysis pages 1-2) | Gastric ectopic mucosa 9/27; normal ileal mucosa 13/27 (hernandez2023meckelsdiverticulumanalysis pages 2-4) | Positive perioperative 99mTc scan in 2/22 symptomatic patients (9%) (hernandez2023meckelsdiverticulumanalysis pages 2-4, hernandez2023meckelsdiverticulumanalysis pages 1-2) | Totally laparoscopic 8/22; laparoscopic-assisted 8/22; laparotomy 6/22; diverticulectomy 6/27; small-bowel resection with end-to-end anastomosis 6/27; lateral-to-lateral anastomosis 15/27; incidental asymptomatic diverticula resected in 5 patients (hernandez2023meckelsdiverticulumanalysis pages 2-4, hernandez2023meckelsdiverticulumanalysis pages 1-2) | Symptomatic group average hospital stay 7.3 days; no mortality figure in snippet (hernandez2023meckelsdiverticulumanalysis pages 1-2) |
| Zvizdic 2025, *Pediatric Surgery International* | Pediatric symptomatic series; n=151 | Male 80.1%; median age 6.7 years (IQR 1.5–10.8); strong male predominance ~4:1 (zvizdic2025diverseclinicalfeatures pages 2-4) | Intestinal obstruction 38.4%; GI bleeding 37.8%; peritonitis 23.8%; acute abdomen 62.3%; multiple symptoms 63.6%; obstruction due to intussusception 72.4%, with ileo-ileal invagination 64.3% of those (zvizdic2025diverseclinicalfeatures pages 2-4) | Ectopic tissue 55.6%; gastric 48.3%; pancreatic 2.6%; both gastric and pancreatic 4.6% (zvizdic2025diverseclinicalfeatures pages 2-4) | Tc-99m scan positive in 46/57 bleeding patients (80.7%); CT identified MD in 5/42 (11.9%); preoperative diagnosis in non-bleeding cases 3.2%; abdominal US detected no MD (0%) (zvizdic2025diverseclinicalfeatures pages 2-4) | Laparotomy 72.2%; laparoscopy 23.2%; conversion 4.6%; segmental small-bowel resection with primary anastomosis 80.8%; diverticulectomy 19.2% (zvizdic2025diverseclinicalfeatures pages 2-4) | Postoperative complications 5.3% in evidence summary / 3.2% in abstract text; no postoperative mortality; follow-up 3–12 years (zvizdic2025diverseclinicalfeatures pages 2-4) |
| Kaka 2023, clinical cohort | Pediatric series; n=25 | Mean age 4.604 ± 3.482 years (range 7 days–11 years); male 17/25 (68%), nearly 2:1 (kaka2023outcomesofdifferent pages 4-8) | Vomiting 17/25 (68%); abdominal distention 16/25 (64%); rectal bleeding 14/25 (56%); abdominal pain 12/25 (48%) (kaka2023outcomesofdifferent pages 4-8) | Isolated gastric mucosa 10/25 (40%); mixed gastric/pancreatic 7/25 (28%); isolated pancreatic 3/25 (12%); no ectopic mucosa 5/25 (20%) (kaka2023outcomesofdifferent pages 4-8) | Preoperative diagnosis described as difficult; no scan sensitivity/specificity reported (kaka2023outcomesofdifferent pages 4-8) | Emergency laparotomy 16/25 (64%); laparoscopy 9/25 (36%) (kaka2023outcomesofdifferent pages 4-8) | No quantitative mortality/complication rate in snippet (kaka2023outcomesofdifferent pages 4-8) |
| De Dyn 2023, *Acta Chirurgica Belgica* | Review/case-based adult-focused evidence | Population prevalence 1–3%; symptomatic male:female 3:1; asymptomatic adults 1:1; typical adult location 60–90 cm from ileocecal valve (range 10–150 cm), neonates 30–50 cm (dyn2023mechanicalileusof pages 1-3) | Common complications are hemorrhage and obstruction (dyn2023mechanicalileusof pages 1-3) | Ectopic/dystopic mucosa 30–50%; gastric fundus/corpus 15.3%; antral/pyloric 3.06%; duodenal 4.08%; pancreatic 2.04%; mixed 3.06% (dyn2023mechanicalileusof pages 1-3) | CT in reported case showed mechanical SBO with hyperdense lesion; no general sensitivity/specificity reported (dyn2023mechanicalileusof pages 1-3) | Diagnostic/therapeutic laparoscopy used in reported case (dyn2023mechanicalileusof pages 1-3) | One cited series reported complications in 41.5% of 3,032 surgically removed diverticula (dyn2023mechanicalileusof pages 1-3) |
| Sagar 2021, *Journal of the Royal Society of Medicine* | Systematic review | Present in 2–4% of population; most studies suggest incidence 0.6–4%; complications 3–4 times greater in males; historical complication rate 25%, more recent 4–16% (sagar2021meckelsdiverticuluma pages 1-2) | Adult obstruction 14–53%; ulceration 54%; common presentations include bleeding, obstruction, intussusception, ulceration, diverticulitis, perforation (sagar2021meckelsdiverticuluma pages 1-2) | NR quantitatively in snippet beyond relationship to ectopic gastric mucosa and bleeding (sagar2021meckelsdiverticuluma pages 1-2) | Preoperative diagnosis improved with technetium-99m pertechnetate scan and diagnostic laparoscopy; no pooled sensitivity/specificity in snippet (sagar2021meckelsdiverticuluma pages 1-2) | Narrow and long diverticula in young suggested for prophylactic excision in review snippet (sagar2021meckelsdiverticuluma pages 1-2) | Complication rate range 4–16% in more recent literature (sagar2021meckelsdiverticuluma pages 1-2) |


*Table: This table compiles the main quantitative findings explicitly available from the retrieved evidence on Meckel diverticulum, including epidemiology, presentation patterns, ectopic mucosa frequencies, diagnostic yields, surgery, and outcomes. It is useful as a compact evidence summary for knowledge-base population and cross-study comparison.*

---

## Visual evidence (scintigraphy protocol update)
Önner et al. (2025) provide a graphical abstract and tabulated scan-quality outcomes comparing pantoprazole vs ranitidine premedication for pediatric Meckel scintigraphy; the retrieved figure/table images support equivalence in scan-quality categories used operationally in nuclear medicine protocols. (onner2025premedicationinpediatric media a6df16f3, onner2025premedicationinpediatric media 9c9d2a7f)


References

1. (aboughalia2023meckeldiverticulumscintigraphy pages 1-3): Hassan A. Aboughalia, Safia H. E. Cheeney, Saeed Elojeimy, Lisa C. Blacklock, and Marguerite T. Parisi. Meckel diverticulum scintigraphy: technique, findings and diagnostic pitfalls. Pediatric Radiology, 53:493-508, Nov 2023. URL: https://doi.org/10.1007/s00247-022-05527-z, doi:10.1007/s00247-022-05527-z. This article has 21 citations and is from a peer-reviewed journal.

2. (hernandez2023meckelsdiverticulumanalysis pages 2-4): Juan David Hernández, Gustavo Valencia, Felipe Girón, Andrés Mauricio García Sierra, Ricardo E. Núñez-Rocha, Lina M. Rodríguez, Carlos Eduardo Rey Chaves, Eduardo Emilio Londoño, and Ricardo Nassar. Meckel's diverticulum: analysis of 27 cases in an adult population. Frontiers in Surgery, Dec 2023. URL: https://doi.org/10.3389/fsurg.2023.1327545, doi:10.3389/fsurg.2023.1327545. This article has 21 citations.

3. (hernandez2023meckelsdiverticulumanalysis pages 1-2): Juan David Hernández, Gustavo Valencia, Felipe Girón, Andrés Mauricio García Sierra, Ricardo E. Núñez-Rocha, Lina M. Rodríguez, Carlos Eduardo Rey Chaves, Eduardo Emilio Londoño, and Ricardo Nassar. Meckel's diverticulum: analysis of 27 cases in an adult population. Frontiers in Surgery, Dec 2023. URL: https://doi.org/10.3389/fsurg.2023.1327545, doi:10.3389/fsurg.2023.1327545. This article has 21 citations.

4. (jarboa2024theclinicalpresentation pages 1-2): Lutfi Jarboa, Ahmad Zarour, Sherif Mustafa, Salahaldeen Dawdi, Idress Suliman, Tejeswe Gutti, Salah Mansor, and Mohamed Said Ghali. The clinical presentation of meckel's diverticulum: eight years experience. Turkish journal of surgery, 40 4:343-348, Dec 2024. URL: https://doi.org/10.47717/turkjsurg.2024.6446, doi:10.47717/turkjsurg.2024.6446. This article has 4 citations.

5. (onner2025premedicationinpediatric pages 1-3): Hasan Önner, Merve Ni̇da Calderon Tobar, Mehmet Sarıkaya, Fatma Özcan Sıkı, Fari̇se Yılmaz, Muslu Kazim Körez, and Gonca Kara Gedi̇k. Premedication in pediatric meckel scintigraphy: pantoprazole versus ranitidine for optimizing scan quality. Pediatric Radiology, 55:1713-1718, Jun 2025. URL: https://doi.org/10.1007/s00247-025-06284-5, doi:10.1007/s00247-025-06284-5. This article has 1 citations and is from a peer-reviewed journal.

6. (onner2025premedicationinpediatric pages 3-4): Hasan Önner, Merve Ni̇da Calderon Tobar, Mehmet Sarıkaya, Fatma Özcan Sıkı, Fari̇se Yılmaz, Muslu Kazim Körez, and Gonca Kara Gedi̇k. Premedication in pediatric meckel scintigraphy: pantoprazole versus ranitidine for optimizing scan quality. Pediatric Radiology, 55:1713-1718, Jun 2025. URL: https://doi.org/10.1007/s00247-025-06284-5, doi:10.1007/s00247-025-06284-5. This article has 1 citations and is from a peer-reviewed journal.

7. (onner2025premedicationinpediatric pages 4-6): Hasan Önner, Merve Ni̇da Calderon Tobar, Mehmet Sarıkaya, Fatma Özcan Sıkı, Fari̇se Yılmaz, Muslu Kazim Körez, and Gonca Kara Gedi̇k. Premedication in pediatric meckel scintigraphy: pantoprazole versus ranitidine for optimizing scan quality. Pediatric Radiology, 55:1713-1718, Jun 2025. URL: https://doi.org/10.1007/s00247-025-06284-5, doi:10.1007/s00247-025-06284-5. This article has 1 citations and is from a peer-reviewed journal.

8. (onner2025premedicationinpediatric media a6df16f3): Hasan Önner, Merve Ni̇da Calderon Tobar, Mehmet Sarıkaya, Fatma Özcan Sıkı, Fari̇se Yılmaz, Muslu Kazim Körez, and Gonca Kara Gedi̇k. Premedication in pediatric meckel scintigraphy: pantoprazole versus ranitidine for optimizing scan quality. Pediatric Radiology, 55:1713-1718, Jun 2025. URL: https://doi.org/10.1007/s00247-025-06284-5, doi:10.1007/s00247-025-06284-5. This article has 1 citations and is from a peer-reviewed journal.

9. (onner2025premedicationinpediatric media 9c9d2a7f): Hasan Önner, Merve Ni̇da Calderon Tobar, Mehmet Sarıkaya, Fatma Özcan Sıkı, Fari̇se Yılmaz, Muslu Kazim Körez, and Gonca Kara Gedi̇k. Premedication in pediatric meckel scintigraphy: pantoprazole versus ranitidine for optimizing scan quality. Pediatric Radiology, 55:1713-1718, Jun 2025. URL: https://doi.org/10.1007/s00247-025-06284-5, doi:10.1007/s00247-025-06284-5. This article has 1 citations and is from a peer-reviewed journal.

10. (zvizdic2025diverseclinicalfeatures pages 2-4): Zlatan Zvizdic, Blagoje Grujic, Asmir Jonuzi, Edin Husaric, Vlatka Martinovic, Aleksandar Brkovic, Nikola Rakocevic, Amir Halilbasic, Valentina Lasic, Denis Pasalic, Emir Begagic, and Semir Vranic. Diverse clinical features of symptomatic meckel’s diverticulum: a multicenter study of 151 consecutive pediatric patients from the western balkans. Pediatric Surgery International, Oct 2025. URL: https://doi.org/10.1007/s00383-025-06197-2, doi:10.1007/s00383-025-06197-2. This article has 4 citations and is from a peer-reviewed journal.

11. (dyn2023mechanicalileusof pages 1-3): Stephan De Dyn, Ilhan Demirci, Andreas Prescher, Andreas Kopp, Bernd Klosterhalfen, and Hermann Janßen. Mechanical ileus of the small bowel due to an inflamed meckel’s diverticulum with an enterolith – a case report with literature review. Acta Chirurgica Belgica, 123:699-706, Oct 2023. URL: https://doi.org/10.1080/00015458.2022.2136047, doi:10.1080/00015458.2022.2136047. This article has 1 citations and is from a peer-reviewed journal.

12. (kaka2023outcomesofdifferent pages 4-8): WAB Kaka and SY Salim. Outcomes of different presentations of complicated meckel's diverticulum in children. Unknown journal, 2023.

13. (sagar2021meckelsdiverticuluma pages 1-2): J. Sagar, Vikas Kumar, and D. Shah. Meckel's diverticulum: a systematic review. Journal of the Royal Society of Medicine, 99:501-505, Oct 2021. URL: https://doi.org/10.1177/014107680609901011, doi:10.1177/014107680609901011. This article has 536 citations and is from a peer-reviewed journal.
