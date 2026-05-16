---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-13T14:34:26.200834'
end_time: '2026-05-13T14:52:41.140757'
duration_seconds: 1094.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Pulmonary Airway Malformation
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Pulmonary Airway Malformation
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Congenital Pulmonary Airway Malformation** covering all of the
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
- **Disease Name:** Congenital Pulmonary Airway Malformation
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Congenital Pulmonary Airway Malformation** covering all of the
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


## Comprehensive Research Report: Congenital Pulmonary Airway Malformation (CPAM)

### 1. Disease Information
**Definition/overview.** Congenital pulmonary airway malformation (CPAM) is a congenital lung malformation characterized by abnormal airway development producing cystic and/or solid pulmonary lesions, most often limited to a single lobe, and commonly detected on prenatal ultrasonography. CPAM is historically referred to as **congenital cystic adenomatoid malformation (CCAM)**; however, CPAM is preferred because “only three of five types are cystic” and only one type is “adenomatoid.” (cancemi2024congenitallungmalformations pages 5-6, pederiva2023congenitallungmalformations pages 1-6)

**Synonyms/alternative names.**
- Congenital cystic adenomatoid malformation (CCAM) (pederiva2023congenitallungmalformations pages 1-6, bertolino2024congenitalpulmonaryairway pages 1-2)
- Congenital lung malformation / congenital thoracic malformation (broader umbrella terms used in reviews) (eber2024lungmalformationspredicting pages 1-2, pederiva2023congenitallungmalformations pages 1-6)

**Key identifiers.** In the retrieved evidence, CPAM is consistently referred to as a congenital lung malformation entity but **explicit OMIM/Orphanet/MONDO/MeSH codes were not available** in the accessible full texts; thus identifiers cannot be reliably populated from this tool-based retrieval.

**Evidence provenance.** The information summarized here is derived primarily from aggregated disease-level resources (reviews and cohort studies) and supplemented by case series/case reports and ClinicalTrials.gov registry entries (pederiva2023congenitallungmalformations pages 1-6, bertolino2024congenitalpulmonaryairway pages 1-2, kunisaki2021narrativereviewof pages 1-2, NCT05701514 chunk 1).


### 2. Etiology
**Developmental etiology.** CPAM is considered a developmental disorder of lung branching/airway morphogenesis, rather than an infectious disease, with most cases occurring sporadically and without clear maternal risk factors. A narrative review notes these lesions are “generally sporadic” and not associated with karyotype anomalies (kunisaki2021narrativereviewof pages 1-2).

**Somatic mosaic driver mutations (current understanding).** A major 2023 synthesis and a high-impact 2024 genetics letter support a model in which many CPAMs—especially types 1 and 3—are driven by **somatic mosaic oncogenic RAS–MAPK pathway variants**, most commonly **KRAS** (pederiva2023congenitallungmalformations pages 13-16, windrich2024rasmapkpathwaymutations pages 1-2).

- In a 2024 American Journal of Respiratory and Critical Care Medicine report, somatic mosaic **KRAS** mutations were detected in **17/29 (58.6%)** CPAM type 1 lesions; the most frequent was **KRAS c.35G>A (p.G12D)** (12/17 mutated cases), with additional variants including **p.G12R, p.A11_G12dup, p.G12V, p.G12C** (URL: https://doi.org/10.1164/rccm.202311-2163le; published May 2024) (windrich2024rasmapkpathwaymutations pages 1-2, windrich2024rasmapkpathwaymutations pages 2-3).
- The same report identified a **somatic BRAF c.1799T>A (p.V600E)** mutation in a CPAM type 3 lesion, with mutant protein expression confirmed by BRAF V600E immunohistochemistry (windrich2024rasmapkpathwaymutations pages 2-3, windrich2024rasmapkpathwaymutations pages 3-3).

**Epigenetic and -omics signals.** Whole-genome methylation differences and transcriptomic pathway enrichment (Ras complex, PI3K–AKT–mTOR, mTOR signaling, Myc targets) have been reported in CPAM and may relate to dysregulated proliferation/survival programs during development (pederiva2023congenitallungmalformations pages 6-9, pederiva2023congenitallungmalformations pages 9-13).

**Risk and protective factors.** The accessible sources emphasize developmental and somatic mosaic mechanisms; **robust, reproducible environmental risk factors or protective factors** were not identified in the retrieved evidence.

**Gene–environment interactions.** No specific gene–environment interactions were identified in the retrieved evidence.


### 3. Phenotypes
**Typical clinical spectrum.** CPAM ranges from asymptomatic prenatal/postnatal findings to neonatal respiratory failure.
- Postnatal presentation “ranges from asymptomatic infants to respiratory failure” in congenital lung malformations including CPAM (pederiva2023congenitallungmalformations pages 1-6).
- Up to **~70%** may be asymptomatic in some clinical descriptions (ottomeyer2023earlyresectionof pages 6-7).

**Prenatal phenotypes and complications.** Prenatal ultrasound may show a cystic/solid lung mass with mediastinal shift; severe cases develop polyhydramnios or **hydrops fetalis**, which is the strongest adverse prognostic factor (bertolino2024congenitalpulmonaryairway pages 1-2, ottomeyer2023earlyresectionof pages 6-7).

**Postnatal symptoms/signs and complications.** Recurrent pneumonia, pneumothorax, and rarely malignancy are common cited reasons for elective resection (kunisaki2021narrativereviewof pages 1-2). In a 2010–2020 institutional series of congenital pulmonary malformations (Peru), postoperative complications after surgery included pneumonia (12.9%), pneumothorax (7.1%), atelectasis (5.7%), and others (nunezpaucar2023congenitalpulmonarymalformations pages 4-5).

**Suggested HPO terms (examples; not exhaustive).**
- Abnormality of the lung (HP:0100753)
- Congenital pulmonary airway malformation (disease-specific HPO term may not exist; often represented via structural terms)
- Respiratory distress in the newborn (HP:0002643)
- Pulmonary hypoplasia (HP:0002089) (reported as a complication in clinical series) (pederiva2023congenitallungmalformations pages 20-24)
- Pneumothorax (HP:0002107) (nunezpaucar2023congenitalpulmonarymalformations pages 4-5)
- Recurrent respiratory infections / pneumonia (HP:0002205 / HP:0002090) (nunezpaucar2023congenitalpulmonarymalformations pages 4-5, kunisaki2021narrativereviewof pages 1-2)
- Fetal hydrops (HP:0001789) (pederiva2023congenitallungmalformations pages 20-24, ottomeyer2023earlyresectionof pages 6-7)
- Mediastinal shift (HP:0030749)
- Polyhydramnios (HP:0001561)

**Phenotype frequencies (available in retrieved evidence).**
- Prenatal detection in a multidisciplinary follow-up cohort: prenatal ultrasound diagnosis in **88.8%** of CPAM cases (n=9) (mussi2024respiratoryfollowupin pages 2-3).
- In the Peru series, CPAM constituted **55.7%** (39/70) of congenital pulmonary malformations seen (nunezpaucar2023congenitalpulmonarymalformations pages 4-5).

**Quality-of-life impact.** Direct standardized QoL metrics are not reported in the accessible publications; however, the ongoing RCT includes child QoL and parental anxiety as key endpoints (NCT05701514 chunk 2).


### 4. Genetic/Molecular Information
**Causal genes.** CPAM is generally described as **not inheritable**, and the strongest current genetic evidence implicates **somatic mosaic mutations** rather than germline Mendelian inheritance for many cases (pederiva2023congenitallungmalformations pages 6-9, pederiva2023congenitallungmalformations pages 13-16).

**Pathogenic variants and molecular subtypes (best-supported).**
- **KRAS** (somatic mosaic; most frequently codon 12 variants in type 1/3) (windrich2024rasmapkpathwaymutations pages 1-2, windrich2024rasmapkpathwaymutations pages 2-3, pederiva2023congenitallungmalformations pages 9-13).
- **BRAF p.V600E** (somatic mosaic; reported in type 3 in one cohort) (windrich2024rasmapkpathwaymutations pages 2-3, windrich2024rasmapkpathwaymutations pages 3-3).
- **DICER1** (germline and/or somatic in the pleuropulmonary blastoma spectrum; relevant to CPAM type 4 vs PPB differential) (pederiva2023congenitallungmalformations pages 13-16, windrich2024rasmapkpathwaymutations pages 2-3, cancemi2024congenitallungmalformations pages 4-5).

**Putative premalignant histology-molecular correlate.** Mucinous cell clusters (MCCs) are described as common in CPAM type 1 and linked to KRAS mutations; a 2024 genetics study notes mucinous clusters “may transform into mucinous adenocarcinoma,” motivating malignancy-risk discussions in management (windrich2024rasmapkpathwaymutations pages 1-2, pederiva2023congenitallungmalformations pages 9-13).

**Epigenetics.** Differential methylation in developmental and proliferation genes across congenital lung malformations, including CPAM, has been reported (pederiva2023congenitallungmalformations pages 9-13, pederiva2023congenitallungmalformations pages 6-9).

**Modifier genes / protective variants.** Not identified in the retrieved evidence.


### 5. Mechanism / Pathophysiology
**Mechanistic model (causal chain).**
1. **Early developmental perturbation** in epithelial–mesenchymal signaling/branching morphogenesis produces abnormal airway structures (review synthesis) (pederiva2023congenitallungmalformations pages 1-6).
2. In a substantial subset, **somatic mosaic oncogenic activation of RAS–MAPK (KRAS; occasionally BRAF)** in airway epithelium drives localized dysplastic proliferation and aberrant differentiation, producing macrocystic/microcystic/solid lesions (pederiva2023congenitallungmalformations pages 13-16, windrich2024rasmapkpathwaymutations pages 1-2, windrich2024rasmapkpathwaymutations pages 3-3).
3. Lesion mass effect can cause **mediastinal shift**, impaired venous return, and fetal heart failure physiology leading to **hydrops** in high-risk cases; size-based indices (CVR) track this risk (pederiva2023congenitallungmalformations pages 20-24).
4. Postnatally, retained abnormal tissue predisposes to **air trapping**, recurrent infections, pneumothorax, and in rare circumstances neoplastic evolution (mucinous adenocarcinoma/PPB spectrum) (pederiva2023congenitallungmalformations pages 1-6, cancemi2024congenitallungmalformations pages 4-5).

**Upstream vs downstream.** Somatic KRAS/BRAF activation is an upstream lesion-driver in many cases; downstream consequences include altered proliferation/apoptosis (reported “double proliferation index” and lower apoptosis susceptibility) and pathway-level upregulation of Ras/PI3K–mTOR/Myc programs (pederiva2023congenitallungmalformations pages 6-9).

**Relevant GO biological process terms (suggestions).**
- Branching morphogenesis of an epithelial tube (GO:0061138)
- Lung development (GO:0030324)
- Regulation of epithelial cell proliferation (GO:0050678)
- Ras protein signal transduction (GO:0007265)
- MAPK cascade (GO:0000165)
- PI3K signaling (GO:0014065) / mTOR signaling

**Relevant CL (cell type) terms (suggestions).**
- Airway epithelial cell (CL:0000066)
- Alveolar type II cell (CL:0002063) (marker associations discussed in CPAM molecular phenotyping literature; see also proteomic study context) ()
- Smooth muscle cell (CL:0000192)


### 6. Inheritance and Population
**Inheritance pattern.** CPAM is typically **sporadic** and described as “not inheritable” in a 2023 authoritative review (pederiva2023congenitallungmalformations pages 6-9).

**Incidence / prevalence.** Estimates vary by study design and ascertainment.
- A 2024 review states CPAM affects **~1 in 2,500 live births** and notes that lesions often enlarge in second trimester and may regress (URL: https://doi.org/10.3390/life14080990; published Aug 2024) (bertolino2024congenitalpulmonaryairway pages 1-2).
- A 2023 Nature Reviews Disease Primers synthesis reports overall congenital lung malformation incidence of **~4 per 10,000 live births** and also notes registry-derived estimates around **~1 per 2,500 live births** for CLMs (URL: https://doi.org/10.1038/s41572-023-00470-1; published Nov 2023) (pederiva2023congenitallungmalformations pages 1-6, pederiva2023congenitallungmalformations pages 6-9).

**Sex ratio.** A male predominance is mentioned in a 2024 case report review, but robust population-level sex ratio estimates were not extracted from high-quality cohort data in the retrieved evidence (goli2024earlydetectionand pages 1-2).


### 7. Diagnostics
**Prenatal imaging.** Serial fetal ultrasound is the primary modality, typically at 18–22 weeks, characterizing lesion size, cystic vs solid features, mediastinal shift, pleural effusion, and hydrops (pederiva2023congenitallungmalformations pages 16-20, cancemi2024congenitallungmalformations pages 4-5).

**CVR (CPAM/CLM volume ratio): definition and thresholds.**
- CVR formula: lesion length × width × height × 0.52 divided by head circumference (cancemi2024congenitallungmalformations pages 5-6, kane2020theutilityof pages 1-2).
- Thresholds reported in authoritative synthesis:
  - **CVR > 1.6** associated with **~80% risk of fetal hydrops** (pederiva2023congenitallungmalformations pages 20-24).
  - **CVR > 0.84** predicts respiratory morbidities/respiratory distress at birth and is linked to likelihood of surgery (pederiva2023congenitallungmalformations pages 20-24, cancemi2024congenitallungmalformations pages 5-6).
  - **Maximum CVR < 0.40** associated with neonatal respiratory distress probability **<10%** (pederiva2023congenitallungmalformations pages 20-24).
- A systematic review emphasizes that lower thresholds (0.5–1.0; even ~0.4) may better predict broader neonatal outcomes depending on population and endpoints (kane2020theutilityof pages 1-2).

**Role of fetal MRI.** Fetal MRI can aid in lesion characterization and sometimes vascular assessment; some reviews note limited incremental value over expert ultrasound, whereas others recommend selective MRI for unclear or large lesions (bertolino2024congenitalpulmonaryairway pages 1-2, pederiva2023congenitallungmalformations pages 20-24).

**Postnatal imaging.**
- Chest radiograph is initial but limited; one synthesis states it “misses ~50% of CLMs” (pederiva2023congenitallungmalformations pages 20-24).
- **Chest CT angiography (CTA)** is described as the **gold standard** for confirmation and surgical planning, often around ~2 months or within the first 6 months depending on symptoms (pederiva2023congenitallungmalformations pages 20-24, cancemi2024congenitallungmalformations pages 5-6, ottomeyer2023earlyresectionof pages 6-7).

**Differential diagnosis.** Key entities include pulmonary sequestration (including hybrid lesions), congenital lobar overinflation (CLO), bronchogenic cyst, congenital diaphragmatic hernia, and pleuropulmonary blastoma (PPB) (pederiva2023congenitallungmalformations pages 20-24, cancemi2024congenitallungmalformations pages 4-5, gonzalez2024congenitalpulmonaryairway pages 4-5).


### 8. Outcome/Prognosis
**Natural history and prognosis.** Many lesions plateau and regress late in gestation; overall prognosis is generally excellent in the absence of hydrops and severe pulmonary hypoplasia, but outcomes vary with lesion size and physiology (bertolino2024congenitalpulmonaryairway pages 1-2, kunisaki2021narrativereviewof pages 1-2).

**Quantitative prenatal course.** A 2024 review states many CPAMs grow in the second trimester, plateau, and in “about 50%” regress by the third trimester (bertolino2024congenitalpulmonaryairway pages 1-2). A separate review of CPAM in an extreme preterm infant reports ranges of in-utero regression (8–42%) and complete resolution (11–49%) across series (ottomeyer2023earlyresectionof pages 6-7).

**Complications and malignancy risk.** Malignancy risk is discussed as a rationale for resection but remains uncertain in true incidence; the 2023 synthesis cites historical estimates and emphasizes knowledge gaps (pederiva2023congenitallungmalformations pages 6-9, pederiva2023congenitallungmalformations pages 1-6). Molecular data linking KRAS-mutant mucinous clusters to mucinous adenocarcinoma provide mechanistic plausibility for rare malignant evolution (windrich2024rasmapkpathwaymutations pages 1-2, pederiva2023congenitallungmalformations pages 9-13).


### 9. Treatment
**Prenatal interventions (high-risk lesions).**
- **Maternal corticosteroids** are described as standard-of-care for larger lesions at risk of nonimmune hydrops (kunisaki2021narrativereviewof pages 1-2).
- **Thoracoamniotic shunt** is used for large cysts with mass effect; **open fetal surgery** is rare due to morbidity; **EXIT** may be used for severe airway compromise (bertolino2024congenitalpulmonaryairway pages 2-5, kunisaki2021narrativereviewof pages 1-2).

**Postnatal management.**
- Symptomatic infants with respiratory distress may need urgent surgical resection (kunisaki2021narrativereviewof pages 1-2, ottomeyer2023earlyresectionof pages 6-7).
- Elective resection for asymptomatic lesions is debated; many centers recommend resection within the first year to reduce complications and enable compensatory lung growth (bertolino2024congenitalpulmonaryairway pages 1-2, pederiva2023congenitallungmalformations pages 1-6, ottomeyer2023earlyresectionof pages 6-7).
- Surgical approaches include open lobectomy and thoracoscopic (VATS) resections; minimally invasive approaches are common when feasible (kunisaki2021narrativereviewof pages 1-2, mussi2024respiratoryfollowupin pages 2-3).

**Real-world outcomes data (examples).**
- Peru single-center congenital pulmonary malformation cohort (2010–2020; n=70; CPAM 39/70): **lobectomy 87.1%**, postoperative pneumonia **12.9%**, pneumothorax **7.1%**, with **no in-hospital deaths** (URL: https://doi.org/10.24875/bmhim.23000055; published Sep 2023) (nunezpaucar2023congenitalpulmonarymalformations pages 4-5).
- Multidisciplinary follow-up cohort (Italy; CPAM n=9): surgery in 7/9 (77.7%), with VATS in 4, and some longer-term wheezing requiring inhaled corticosteroids (mussi2024respiratoryfollowupin pages 2-3).

**MAXO term suggestions (examples).**
- Surgical excision of lung lesion / lobectomy (MAXO term: surgical resection)
- Thoracoscopic surgery (MAXO: minimally invasive surgery)
- Prenatal corticosteroid therapy (MAXO: glucocorticoid therapy)
- Fetal thoracoamniotic shunt placement (MAXO: fetal shunt placement)
- EXIT procedure (MAXO: ex utero intrapartum treatment)


### 10. Prevention
**Primary prevention.** No validated primary prevention exists for CPAM because it is a congenital developmental malformation (pederiva2023congenitallungmalformations pages 1-6).

**Secondary prevention (risk mitigation).** Prevention in practice focuses on **prenatal detection** (screening ultrasound), risk stratification (CVR), and referral to tertiary fetal medicine/pediatric surgery centers for high-risk lesions (pederiva2023congenitallungmalformations pages 20-24, kunisaki2021narrativereviewof pages 1-2).

**Tertiary prevention.** Postnatal prevention targets avoiding recurrent infection, pneumothorax, and rare malignant transformation via appropriate imaging follow-up and (in selected patients) resection (pederiva2023congenitallungmalformations pages 1-6, kunisaki2021narrativereviewof pages 1-2).


### 11. Other Species / Natural Disease
No naturally occurring veterinary analogue or species-specific CPAM entity was identified in the retrieved evidence.


### 12. Model Organisms
The retrieved evidence emphasizes human lesion genomics and -omics rather than established animal models. However, mechanistic framing (mosaic RASopathies; epithelial driver mutations) implies relevant experimental systems could include mosaic KRAS/BRAF activation in lung epithelium during development; specific validated model organisms were not identified in the accessible evidence.


### 13. Anatomical Structures Affected
**Organ/system.** Lung (respiratory system), typically a single lobe; prenatal mass effect can involve mediastinum and fetal cardiovascular physiology (pederiva2023congenitallungmalformations pages 6-9, pederiva2023congenitallungmalformations pages 20-24).

**UBERON term suggestions.**
- Lung (UBERON:0002048)
- Lung lobe (UBERON:0002173)
- Bronchiole / airway epithelium (UBERON airway structures)
- Mediastinum (UBERON:0003729)


### 14. Temporal Development
**Onset.** Congenital; usually detected prenatally at ~18–22 weeks (pederiva2023congenitallungmalformations pages 16-20).

**Gestational course.** Lesions often grow between 20–26 weeks and plateau by ~29 weeks; a substantial fraction regress in late gestation (pederiva2023congenitallungmalformations pages 16-20, bertolino2024congenitalpulmonaryairway pages 1-2).


### 15. Recent Developments and Latest Research (2023–2024 emphasis)
**High-authority synthesis (2023).** Nature Reviews Disease Primers published a comprehensive 2023 review of congenital lung malformations, summarizing epidemiology, imaging workflows (CTA as gold standard), CVR thresholds for hydrops and neonatal distress, and highlighting the unresolved debate about resection vs conservative management for asymptomatic lesions (URL: https://doi.org/10.1038/s41572-023-00470-1; published Nov 2023) (pederiva2023congenitallungmalformations pages 1-6, pederiva2023congenitallungmalformations pages 20-24).

**Molecular genetics leap (2024).** A 2024 AJRCCM letter expanded evidence that CPAM types 1 and 3 frequently harbor somatic mosaic oncogenic RAS–MAPK variants, quantifying mutation frequencies and cataloging KRAS and BRAF variants; it also frames CPAM as “possible mosaic RASopathies,” which is mechanistically consequential and may influence long-term malignancy-risk evaluation (URL: https://doi.org/10.1164/rccm.202311-2163le; published May 2024) (windrich2024rasmapkpathwaymutations pages 1-2, windrich2024rasmapkpathwaymutations pages 2-3, windrich2024rasmapkpathwaymutations pages 3-3).

**Imaging-focused implementation guidance (2024).** A 2024 pictorial review provides practical diagnostic imaging guidance (prenatal US; CVR formula and ≥0.84 threshold; CT within first 6 months; CTA for vascular mapping; MRI alternatives) that supports real-world radiology workflow standardization (URL: https://doi.org/10.3390/children11060638; published May 2024) (cancemi2024congenitallungmalformations pages 5-6, cancemi2024congenitallungmalformations pages 4-5).


## Expert opinions and analysis (from authoritative sources)
- **Surgery vs observation remains the key unresolved question** for asymptomatic infants: clinicians “agree to surgically treat symptomatic patients,” but “there is an ongoing debate worldwide whether asymptomatic patients should be managed surgically or conservatively” (pederiva2023congenitallungmalformations pages 6-9). This uncertainty is sufficiently impactful that a multicenter RCT has been launched (CONNECT) (NCT05701514 chunk 1).
- **Size-based fetal risk prediction is central**: multiple sources emphasize that mass size/CVR is more prognostic than histologic type for perinatal outcomes (pederiva2023congenitallungmalformations pages 20-24, eber2024lungmalformationspredicting pages 1-2).
- **Molecular stratification is emerging**: KRAS/BRAF mosaicism suggests CPAM is not purely “malformative” but can be viewed as congenital tissue dysplasia driven by oncogenic mutations, potentially reshaping surveillance strategies and malignancy-risk counseling (windrich2024rasmapkpathwaymutations pages 3-3, pederiva2023congenitallungmalformations pages 13-16).


## Current applications and real-world implementations
- **Prenatal monitoring programs**: serial ultrasound with CVR tracking and selective fetal MRI for high-risk/uncertain lesions are widely implemented (pederiva2023congenitallungmalformations pages 20-24).
- **Postnatal confirmation and surgical planning**: CT angiography (often at ~2 months or within 6 months) is used for definitive characterization and vascular mapping prior to resection (pederiva2023congenitallungmalformations pages 20-24, cancemi2024congenitallungmalformations pages 5-6).
- **Multidisciplinary care pathways**: cohort follow-up models integrate pulmonology, surgery, neonatology, and radiology to manage short- and long-term respiratory complications (mussi2024respiratoryfollowupin pages 2-3).


## Relevant statistics and quantitative data highlights
- Incidence: frequently cited **~1/2,500 live births** (bertolino2024congenitalpulmonaryairway pages 1-2, kunisaki2021narrativereviewof pages 1-2).
- Prenatal natural history: **~50%** regression by third trimester in one 2024 review (bertolino2024congenitalpulmonaryairway pages 1-2).
- CVR risk thresholds: **>1.6 → ~80% hydrops risk; >0.84 → predicts respiratory morbidity; <0.40 → NRD probability <10%** (pederiva2023congenitallungmalformations pages 20-24, cancemi2024congenitallungmalformations pages 5-6).
- Genetics: somatic KRAS mutations in **17/29 (58.6%)** type 1 lesions; common **KRAS p.G12D** (windrich2024rasmapkpathwaymutations pages 1-2).


## Ongoing clinical trials/registries (real-world evidence generation)
- **CONNECT trial (NCT05701514)**: randomized trial of elective resection (6–9 months) vs watchful waiting in asymptomatic, CT-confirmed CPAM; primary endpoint exercise tolerance at 5 years (BRUCE treadmill) (registered 2023; recruiting) (NCT05701514 chunk 1, NCT05701514 chunk 2).
- **Swiss Congenital Lung Anomalies registry/biobank (NCT03044769)**: prospective 10-year registry with imaging, lung function, and tissue biomarker endpoints (registered 2016) (NCT03044769 chunk 1).
- **Molecular profiling study (NCT01732185)**: completed basic-science interventional study collecting blood and lesion/adjacent tissue for transcriptomics/proteomics and CGH-array somatic abnormalities (2012–2015; n=45) (NCT01732185 chunk 1).
- **Surgical outcomes review (NCT04449614)**: completed retrospective cohort of thoracoscopic CPAM resections (2008–2017; n=72) (NCT04449614 chunk 1).


## Visual evidence from retrieved documents
The following cropped figure-legend excerpts (manuscript draft text) summarize the presence of key classification/management figures (Stocker classification and CVR-based algorithms) in the 2023 authoritative review; the actual figure panels were not included in the accessible text, but the legends contain the quantitative thresholds and algorithm descriptions (pederiva2023congenitallungmalformations media 94ace63e, pederiva2023congenitallungmalformations media 92254196, pederiva2023congenitallungmalformations media 769ac597).


## High-yield structured summary (artifact)
| Domain | Key facts (include numeric values/thresholds) | Best recent/authoritative source (with year, journal) | Evidence note (include one short direct quote snippet when available) |
|---|---|---|---|
| Definition/synonyms | CPAM is a congenital lung malformation; older term CCAM remains common. CPAM is preferred because not all types are cystic/adenomatoid. Five histologic subtypes are recognized in modern Stocker classification. | Pederiva et al., 2023, *Nature Reviews Disease Primers*; Cancemi et al., 2024, *Children* | “congenital cystic adenomatoid malformation (CCAM)” is used as a synonym for CPAM; CPAM is preferred because “only three of five types are cystic” (pederiva2023congenitallungmalformations pages 1-6, cancemi2024congenitallungmalformations pages 5-6) |
| Incidence | Population estimates vary: CPAM/CLM incidence is often cited around 1 in 2,500 live births; broader CLM incidence reported as 4 per 10,000 live births. | Bertolino et al., 2024, *Life*; Pederiva et al., 2023, *Nature Reviews Disease Primers* | Bertolino review states CPAMs affect “1 in 2500 live births” (bertolino2024congenitalpulmonaryairway pages 1-2, pederiva2023congenitallungmalformations pages 1-6) |
| Prenatal natural history | Typically detected at 18–22 weeks; many lesions enlarge during the 2nd trimester, peak around 20–26 weeks, then plateau by ~29 weeks; ~50% may regress and become barely detectable in the 3rd trimester. Reported in-utero regression ranges 8–42%; complete prenatal resolution 11–49% in some series. | Pederiva et al., 2023, *Nature Reviews Disease Primers*; Bertolino et al., 2024, *Life*; Ottomeyer et al., 2023, *BMC Pediatrics* | “increase their size in the second trimester, reach a plateau, and, in about 50% of cases, regress” (bertolino2024congenitalpulmonaryairway pages 1-2, pederiva2023congenitallungmalformations pages 16-20, ottomeyer2023earlyresectionof pages 6-7) |
| Stocker classification overview | Modern Stocker types 0–4: type 1 is most common (~50–70% or 60–65%); type 2 ~15–30% or 10–40%; type 3 ~5–10%; type 4 ~10–15%; type 0 ~2%. Type 1 often has large cysts >2 cm; type 2 multiple small cysts; type 3 solid/microcystic; type 4 peripheral/acinar large cystic lesions. | Pederiva et al., 2023, *Nature Reviews Disease Primers*; Cancemi et al., 2024, *Children* | Stocker classification “classified into five histological subtypes” and type frequencies are summarized in recent imaging review (pederiva2023congenitallungmalformations pages 1-6, cancemi2024congenitallungmalformations pages 5-6) |
| CVR thresholds (0.40, 0.84, 1.6) | CVR = lesion length × width × height × 0.52 / head circumference. CVR <0.40: low risk, neonatal respiratory distress <10%; CVR ≥0.84: predicts respiratory distress at birth / respiratory morbidity and likely need for surgery; CVR >1.6: associated with ~80% risk of fetal hydrops. Lower neonatal-risk thresholds of 0.5–1.0 have also been proposed. | Pederiva et al., 2023, *Nature Reviews Disease Primers*; Cancemi et al., 2024, *Children*; Kane et al., 2020, *Fetal Diagnosis and Therapy* | “CVR > 1.6 associates with ~80% risk of fetal hydrops”; “A CVR value of ≥0.84 is a reliable predictor of respiratory distress at birth” (pederiva2023congenitallungmalformations pages 20-24, cancemi2024congenitallungmalformations pages 5-6, kane2020theutilityof pages 1-2) |
| Management controversy | Symptomatic CPAM is generally resected; the main controversy is asymptomatic disease. Many centers recommend elective resection in the first year, but some surgeons favor observation because the true risk of infection/malignancy is uncertain. | Pederiva et al., 2023, *Nature Reviews Disease Primers*; Bertolino et al., 2024, *Life*; Kunisaki, 2021, *Translational Pediatrics* | “there is an ongoing debate worldwide whether asymptomatic patients should be managed surgically or conservatively” (pederiva2023congenitallungmalformations pages 6-9, pederiva2023congenitallungmalformations pages 1-6, bertolino2024congenitalpulmonaryairway pages 1-2) |
| Molecular genetics (KRAS, BRAF, DICER1/PPB) | Strongest current evidence supports somatic mosaic RAS-MAPK alterations in CPAM, especially types 1 and 3. KRAS mutations found in 17/29 (58.6%) type 1 cases in one 2024 series; common variants include p.G12D, p.G12V, p.G12C, p.G12R, p.A11_G12dup. Somatic BRAF p.V600E has also been reported. Type 4/PPB overlap is linked to DICER1; PPB type 1 cases in the 2024 series had DICER1 variants rather than RAS-MAPK mutations. | Windrich et al., 2024, *American Journal of Respiratory and Critical Care Medicine*; Pederiva et al., 2023, *Nature Reviews Disease Primers* | “CPAM Type 1 results from somatic KRAS mutations”; somatic BRAF p.V600E was also detected; DICER1 is linked to PPB/type 4 biology (windrich2024rasmapkpathwaymutations pages 1-2, windrich2024rasmapkpathwaymutations pages 2-3, pederiva2023congenitallungmalformations pages 13-16, windrich2024rasmapkpathwaymutations pages 3-3) |
| Diagnostic imaging | Prenatal ultrasound is the primary screening and surveillance tool; detects lesion size, cystic/solid nature, mediastinal shift, hydrops, and systemic feeding vessel assessment by Doppler. Fetal MRI is adjunctive for unclear/large lesions and vascular anatomy. Postnatally, chest radiograph is first-line but insensitive (~50% may be missed); chest CT angiography around ~2 months or within first 6 months is the diagnostic gold standard for confirmation and surgical planning. | Pederiva et al., 2023, *Nature Reviews Disease Primers*; Cancemi et al., 2024, *Children* | “chest radiograph is first-line but misses ~50% of CLMs”; CTA is the “gold standard” for confirmation and planning (pederiva2023congenitallungmalformations pages 20-24, cancemi2024congenitallungmalformations pages 5-6, cancemi2024congenitallungmalformations pages 4-5) |
| Treatment options | Prenatal: maternal corticosteroids for larger/high-risk microcystic lesions; thoracoamniotic shunt for large macrocystic lesions with mass effect; open fetal surgery rarely used; EXIT considered for severe airway/mediastinal compromise. Postnatal: urgent surgery for respiratory distress; elective resection often in first year (median age 5 months in one review); thoracoscopic surgery is widely used when feasible. In one Peruvian CPM series, lobectomy was 87.1% of operations; postoperative pneumonia 12.9%, pneumothorax 7.1%. | Kunisaki, 2021, *Translational Pediatrics*; Ottomeyer et al., 2023, *BMC Pediatrics*; Nuñez-Paucar et al., 2023, *Boletín Médico del Hospital Infantil de México* | Maternal steroids “have become standard of care” for larger lesions at risk of hydrops; elective resection is commonly recommended, but practice varies (kunisaki2021narrativereviewof pages 1-2, ottomeyer2023earlyresectionof pages 6-7, nunezpaucar2023congenitalpulmonarymalformations pages 4-5) |
| Trials/registries | **NCT05701514 (CONNECT)**: recruiting multicenter RCT; 176 infants; elective surgery at 6–9 months vs watchful waiting; primary endpoint = exercise tolerance at 5 years. **NCT03044769**: Swiss prospective registry/biobank; longitudinal clinical, imaging, lung function, and biomarker outcomes. **NCT01732185**: completed basic-science interventional study (n=45) using transcriptomics/proteomics/CGH array on CCAM tissue. **NCT04449614**: completed retrospective observational cohort (n=72) reviewing thoracoscopic CPAM resection outcomes. | ClinicalTrials.gov records: 2023 CONNECT; 2016 Swiss CLA registry; 2012 molecular study; 2018 surgical review | CONNECT randomizes asymptomatic infants to “elective surgical resection at 6–9 months or conservative (watchful waiting) management” (NCT05701514 chunk 1, NCT05701514 chunk 2, NCT03044769 chunk 1, NCT01732185 chunk 1, NCT04449614 chunk 1) |


*Table: This table condenses the highest-yield disease-characteristic facts for congenital pulmonary airway malformation, emphasizing 2023–2024 reviews and studies plus active trial infrastructure. It highlights the quantitative thresholds, molecular discoveries, imaging standards, and unresolved management questions most useful for a knowledge-base entry.*


## Evidence limitations (for knowledge-base population)
- Standardized disease identifiers (MONDO/Orphanet/MeSH/ICD/OMIM) were not extractable from the retrieved full texts; populating those fields requires direct queries to the relevant ontology/registry resources.
- Environmental risk/protective factors, robust QoL metrics, and validated animal models were not identified in the retrieved evidence set.


References

1. (cancemi2024congenitallungmalformations pages 5-6): Giovanna Cancemi, Giulio Distefano, Gioele Vitaliti, Dario Milazzo, Giuseppe Terzo, Giuseppe Belfiore, Vincenzo Di Benedetto, Maria Grazia Scuderi, Maria Coronella, Andrea Giovanni Musumeci, Daniele Grippaldi, Letizia Antonella Mauro, Pietro Valerio Foti, Antonio Basile, and Stefano Palmucci. Congenital lung malformations: a pictorial review of imaging findings and a practical guide for diagnosis. Children, 11:638, May 2024. URL: https://doi.org/10.3390/children11060638, doi:10.3390/children11060638. This article has 22 citations.

2. (pederiva2023congenitallungmalformations pages 1-6): Federica Pederiva, Steven S. Rothenberg, Nigel Hall, Hanneke Ijsselstijn, Kenneth K. Y. Wong, Jan von der Thüsen, Pierluigi Ciet, Reuven Achiron, Adamo Pio d’Adamo, and J. Marco Schnater. Congenital lung malformations. Nature Reviews Disease Primers, 9:1-16, Nov 2023. URL: https://doi.org/10.1038/s41572-023-00470-1, doi:10.1038/s41572-023-00470-1. This article has 116 citations.

3. (bertolino2024congenitalpulmonaryairway pages 1-2): Alessia Bertolino, Silvia Bertolo, Paola Lago, and Paola Midrio. Congenital pulmonary airway malformation in preterm infants: a case report and review of the literature. Aug 2024. URL: https://doi.org/10.3390/life14080990, doi:10.3390/life14080990. This article has 6 citations.

4. (eber2024lungmalformationspredicting pages 1-2): E. Eber. Lung malformations: predicting respiratory distress at birth. Pediatric Respiratory Journal, 02:180, Nov 2024. URL: https://doi.org/10.56164/pediatrrespirj.2024.56, doi:10.56164/pediatrrespirj.2024.56. This article has 0 citations.

5. (kunisaki2021narrativereviewof pages 1-2): Shaun M. Kunisaki. Narrative review of congenital lung lesions. Translational Pediatrics, 10:1418-1431, May 2021. URL: https://doi.org/10.21037/tp-20-133, doi:10.21037/tp-20-133. This article has 78 citations and is from a peer-reviewed journal.

6. (NCT05701514 chunk 1): dr. J Marco Schnater. The COllaborative Neonatal Network for the First CPAM Trial. Erasmus Medical Center. 2023. ClinicalTrials.gov Identifier: NCT05701514

7. (pederiva2023congenitallungmalformations pages 13-16): Federica Pederiva, Steven S. Rothenberg, Nigel Hall, Hanneke Ijsselstijn, Kenneth K. Y. Wong, Jan von der Thüsen, Pierluigi Ciet, Reuven Achiron, Adamo Pio d’Adamo, and J. Marco Schnater. Congenital lung malformations. Nature Reviews Disease Primers, 9:1-16, Nov 2023. URL: https://doi.org/10.1038/s41572-023-00470-1, doi:10.1038/s41572-023-00470-1. This article has 116 citations.

8. (windrich2024rasmapkpathwaymutations pages 1-2): Jonas Windrich, Peter Braubach, Florian Länger, Jens Dingemann, Nicolaus Schwerk, Martin Wetzke, Diane M. Renz, Martin Zenker, Denny Schanze, and Christian P. Kratz. Ras-mapk pathway mutations in congenital pulmonary airway malformations. May 2024. URL: https://doi.org/10.1164/rccm.202311-2163le, doi:10.1164/rccm.202311-2163le. This article has 9 citations and is from a highest quality peer-reviewed journal.

9. (windrich2024rasmapkpathwaymutations pages 2-3): Jonas Windrich, Peter Braubach, Florian Länger, Jens Dingemann, Nicolaus Schwerk, Martin Wetzke, Diane M. Renz, Martin Zenker, Denny Schanze, and Christian P. Kratz. Ras-mapk pathway mutations in congenital pulmonary airway malformations. May 2024. URL: https://doi.org/10.1164/rccm.202311-2163le, doi:10.1164/rccm.202311-2163le. This article has 9 citations and is from a highest quality peer-reviewed journal.

10. (windrich2024rasmapkpathwaymutations pages 3-3): Jonas Windrich, Peter Braubach, Florian Länger, Jens Dingemann, Nicolaus Schwerk, Martin Wetzke, Diane M. Renz, Martin Zenker, Denny Schanze, and Christian P. Kratz. Ras-mapk pathway mutations in congenital pulmonary airway malformations. May 2024. URL: https://doi.org/10.1164/rccm.202311-2163le, doi:10.1164/rccm.202311-2163le. This article has 9 citations and is from a highest quality peer-reviewed journal.

11. (pederiva2023congenitallungmalformations pages 6-9): Federica Pederiva, Steven S. Rothenberg, Nigel Hall, Hanneke Ijsselstijn, Kenneth K. Y. Wong, Jan von der Thüsen, Pierluigi Ciet, Reuven Achiron, Adamo Pio d’Adamo, and J. Marco Schnater. Congenital lung malformations. Nature Reviews Disease Primers, 9:1-16, Nov 2023. URL: https://doi.org/10.1038/s41572-023-00470-1, doi:10.1038/s41572-023-00470-1. This article has 116 citations.

12. (pederiva2023congenitallungmalformations pages 9-13): Federica Pederiva, Steven S. Rothenberg, Nigel Hall, Hanneke Ijsselstijn, Kenneth K. Y. Wong, Jan von der Thüsen, Pierluigi Ciet, Reuven Achiron, Adamo Pio d’Adamo, and J. Marco Schnater. Congenital lung malformations. Nature Reviews Disease Primers, 9:1-16, Nov 2023. URL: https://doi.org/10.1038/s41572-023-00470-1, doi:10.1038/s41572-023-00470-1. This article has 116 citations.

13. (ottomeyer2023earlyresectionof pages 6-7): Megan Ottomeyer, Charles Huddleston, Rachel M. Berkovich, David S. Brink, Joyce M. Koenig, and Kurtis T. Sobush. Early resection of a rare congenital pulmonary airway malformation causing severe progressive respiratory distress in a preterm neonate: a case report and review of the literature. BMC Pediatrics, May 2023. URL: https://doi.org/10.1186/s12887-023-04049-3, doi:10.1186/s12887-023-04049-3. This article has 13 citations and is from a peer-reviewed journal.

14. (nunezpaucar2023congenitalpulmonarymalformations pages 4-5): Héctor Nuñez-Paucar, Noé Atamari-Anahui, and Carlos Valera-Moreno. Congenital pulmonary malformations in children in a pediatric hospital in peru, 2010-2020. Boletín Médico del Hospital Infantil de México, Sep 2023. URL: https://doi.org/10.24875/bmhim.23000055, doi:10.24875/bmhim.23000055. This article has 2 citations.

15. (pederiva2023congenitallungmalformations pages 20-24): Federica Pederiva, Steven S. Rothenberg, Nigel Hall, Hanneke Ijsselstijn, Kenneth K. Y. Wong, Jan von der Thüsen, Pierluigi Ciet, Reuven Achiron, Adamo Pio d’Adamo, and J. Marco Schnater. Congenital lung malformations. Nature Reviews Disease Primers, 9:1-16, Nov 2023. URL: https://doi.org/10.1038/s41572-023-00470-1, doi:10.1038/s41572-023-00470-1. This article has 116 citations.

16. (mussi2024respiratoryfollowupin pages 2-3): Nicole Mussi, Erika Maugeri, Michela Deolmi, Alberto Scarpa, Emilio Casolari, Giovanna Pisi, Valentina Fainardi, and Susanna Esposito. Respiratory follow-up in a cohort of children with congenital malformations affecting lung development: a cohort study. International Journal of Pediatrics and Child Health, 12:80-88, Jul 2024. URL: https://doi.org/10.12974/2311-8687.2024.12.11, doi:10.12974/2311-8687.2024.12.11. This article has 0 citations.

17. (NCT05701514 chunk 2): dr. J Marco Schnater. The COllaborative Neonatal Network for the First CPAM Trial. Erasmus Medical Center. 2023. ClinicalTrials.gov Identifier: NCT05701514

18. (cancemi2024congenitallungmalformations pages 4-5): Giovanna Cancemi, Giulio Distefano, Gioele Vitaliti, Dario Milazzo, Giuseppe Terzo, Giuseppe Belfiore, Vincenzo Di Benedetto, Maria Grazia Scuderi, Maria Coronella, Andrea Giovanni Musumeci, Daniele Grippaldi, Letizia Antonella Mauro, Pietro Valerio Foti, Antonio Basile, and Stefano Palmucci. Congenital lung malformations: a pictorial review of imaging findings and a practical guide for diagnosis. Children, 11:638, May 2024. URL: https://doi.org/10.3390/children11060638, doi:10.3390/children11060638. This article has 22 citations.

19. (goli2024earlydetectionand pages 1-2): Yasaman Dasteh Goli and Harsh Datta. Early detection and management of congenital pulmonary airway malformation in a newborn with stable clinical course. Journal of Case Reports and Images in Pediatrics, 6:5-10, Oct 2024. URL: https://doi.org/10.5348/100026z19yg2024cr, doi:10.5348/100026z19yg2024cr. This article has 0 citations.

20. (pederiva2023congenitallungmalformations pages 16-20): Federica Pederiva, Steven S. Rothenberg, Nigel Hall, Hanneke Ijsselstijn, Kenneth K. Y. Wong, Jan von der Thüsen, Pierluigi Ciet, Reuven Achiron, Adamo Pio d’Adamo, and J. Marco Schnater. Congenital lung malformations. Nature Reviews Disease Primers, 9:1-16, Nov 2023. URL: https://doi.org/10.1038/s41572-023-00470-1, doi:10.1038/s41572-023-00470-1. This article has 116 citations.

21. (kane2020theutilityof pages 1-2): Stefan C. Kane, Emanuele Ancona, Karen L. Reidy, and Ricardo Palma-Dias. The utility of the congenital pulmonary airway malformation-volume ratio in the assessment of fetal echogenic lung lesions: a systematic review. Fetal Diagnosis and Therapy, 47:171-181, Oct 2020. URL: https://doi.org/10.1159/000502841, doi:10.1159/000502841. This article has 43 citations and is from a peer-reviewed journal.

22. (gonzalez2024congenitalpulmonaryairway pages 4-5): Andrés González and Laura Laverde. Congenital pulmonary airway malformation (cpam). a case report. Medical &amp; Clinical Case Reports Journal, 2:557-562, Nov 2024. URL: https://doi.org/10.51219/mccrj/andres-gonzalez/146, doi:10.51219/mccrj/andres-gonzalez/146. This article has 0 citations.

23. (bertolino2024congenitalpulmonaryairway pages 2-5): Alessia Bertolino, Silvia Bertolo, Paola Lago, and Paola Midrio. Congenital pulmonary airway malformation in preterm infants: a case report and review of the literature. Aug 2024. URL: https://doi.org/10.3390/life14080990, doi:10.3390/life14080990. This article has 6 citations.

24. (NCT03044769 chunk 1): Isabelle Ruchonnet-Métrailler. Congenital Lung Anomalies (CLA) Swiss Database. University Hospital, Geneva. 2016. ClinicalTrials.gov Identifier: NCT03044769

25. (NCT01732185 chunk 1):  Genetic and Molecular Abnormalities in Congenital Cystic Adenomatoid Malformations. Assistance Publique - Hôpitaux de Paris. 2012. ClinicalTrials.gov Identifier: NCT01732185

26. (NCT04449614 chunk 1):  A Review of Surgical Management of Congenital Pulmonary Airway Malformations (CPAM): A Decade of Experience. King's College Hospital NHS Trust. 2018. ClinicalTrials.gov Identifier: NCT04449614

27. (pederiva2023congenitallungmalformations media 94ace63e): Federica Pederiva, Steven S. Rothenberg, Nigel Hall, Hanneke Ijsselstijn, Kenneth K. Y. Wong, Jan von der Thüsen, Pierluigi Ciet, Reuven Achiron, Adamo Pio d’Adamo, and J. Marco Schnater. Congenital lung malformations. Nature Reviews Disease Primers, 9:1-16, Nov 2023. URL: https://doi.org/10.1038/s41572-023-00470-1, doi:10.1038/s41572-023-00470-1. This article has 116 citations.

28. (pederiva2023congenitallungmalformations media 92254196): Federica Pederiva, Steven S. Rothenberg, Nigel Hall, Hanneke Ijsselstijn, Kenneth K. Y. Wong, Jan von der Thüsen, Pierluigi Ciet, Reuven Achiron, Adamo Pio d’Adamo, and J. Marco Schnater. Congenital lung malformations. Nature Reviews Disease Primers, 9:1-16, Nov 2023. URL: https://doi.org/10.1038/s41572-023-00470-1, doi:10.1038/s41572-023-00470-1. This article has 116 citations.

29. (pederiva2023congenitallungmalformations media 769ac597): Federica Pederiva, Steven S. Rothenberg, Nigel Hall, Hanneke Ijsselstijn, Kenneth K. Y. Wong, Jan von der Thüsen, Pierluigi Ciet, Reuven Achiron, Adamo Pio d’Adamo, and J. Marco Schnater. Congenital lung malformations. Nature Reviews Disease Primers, 9:1-16, Nov 2023. URL: https://doi.org/10.1038/s41572-023-00470-1, doi:10.1038/s41572-023-00470-1. This article has 116 citations.