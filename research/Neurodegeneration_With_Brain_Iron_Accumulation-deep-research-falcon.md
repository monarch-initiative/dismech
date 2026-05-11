---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T14:45:17.385408'
end_time: '2026-05-10T14:55:06.244448'
duration_seconds: 588.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodegeneration With Brain Iron Accumulation
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodegeneration With Brain Iron Accumulation
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Neurodegeneration With Brain Iron Accumulation** covering all of the
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
- **Disease Name:** Neurodegeneration With Brain Iron Accumulation
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Neurodegeneration With Brain Iron Accumulation** covering all of the
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


# Neurodegeneration With Brain Iron Accumulation (NBIA) — Comprehensive Research Report (Genetic)

## 1. Disease Information

### 1.1 Overview (definition; current understanding)
Neurodegeneration with brain iron accumulation (NBIA) refers to a genetically heterogeneous group of progressive neurodegenerative disorders characterized by abnormal iron deposition in deep gray nuclei—classically the globus pallidus and substantia nigra—visible on iron-sensitive MRI sequences. (iankova2021emergingdiseasemodifyingtherapies pages 1-2, schneider2025neurodegenerationwithbrain pages 1-2)

Direct abstract-supported statement (Frontiers in Neurology review, published **2021-04-15**): NBIA is described as “a heterogeneous group of progressive neurodegenerative diseases characterized by iron deposition in the globus pallidus and the substantia nigra.” (iankova2021emergingdiseasemodifyingtherapies pages 1-2)

### 1.2 Key identifiers
- **MONDO**: **MONDO_0018307** (“neurodegeneration with brain iron accumulation”) (OpenTargets Search: Neurodegeneration with brain iron accumulation)
- **Other identifiers (OMIM, Orphanet, ICD-10/ICD-11, MeSH)**: Not retrievable from the current tool evidence set; should be filled by targeted queries to OMIM/Orphanet/MeSH/ICD resources outside this run.

### 1.3 Synonyms / alternative names
- “NBIA disorders” (iankova2021emergingdiseasemodifyingtherapies pages 1-2)
- Frequently referenced subtype names: **PKAN**, **PLAN/INAD**, **BPAN**, **MPAN** (iankova2021emergingdiseasemodifyingtherapies pages 1-2, spaull2021towardsprecisiontherapies pages 2-4)

### 1.4 Evidence source type
The characterization in this report is derived primarily from **aggregated disease-level resources** (peer-reviewed reviews) and **cohort/registry/trial records** (ClinicalTrials.gov) plus **human cohort studies** (PLAN cohort, chelation cohorts). (iankova2021emergingdiseasemodifyingtherapies pages 1-2, dehnavi2023phenotypeandgenotype pages 1-2, NCT02587858 chunk 1, NCT02174848 chunk 1, NCT04182763 chunk 1)

## 2. Etiology

### 2.1 Disease causal factors
NBIA is primarily **genetic/monogenic** in etiology, comprising multiple distinct gene-defined entities (at least ~15 monogenic disorders noted in 2021), unified by basal ganglia iron accumulation. (iankova2021emergingdiseasemodifyingtherapies pages 1-2, uygun2025quantitativeironmeasurements pages 2-2)

While iron accumulation is a defining feature, reviews emphasize that only a subset of NBIA forms arise from **primary defects in iron homeostasis genes** (notably aceruloplasminemia and neuroferritinopathy), whereas many other NBIA genes map to pathways such as coenzyme A biosynthesis, lipid metabolism, and autophagy. (iankova2021emergingdiseasemodifyingtherapies pages 1-2, spaull2021towardsprecisiontherapies pages 2-4)

### 2.2 Risk factors
- **Genetic**: Pathogenic variants in NBIA-associated genes (examples emphasized across sources: **PANK2, PLA2G6, C19orf12, WDR45, CP, FTL, ATP13A2, FA2H, COASY**). (schneider2025neurodegenerationwithbrain pages 3-4, schneider2025neurodegenerationwithbrain pages 1-2, OpenTargets Search: Neurodegeneration with brain iron accumulation)
- **Consanguinity** (for autosomal recessive NBIA subtypes): In the 2023 Iranian PLAN cohort, all late-onset PLAN adult cases were reported from consanguineous parents. (dehnavi2023phenotypeandgenotype pages 9-11)
- **Environmental**: No specific environmental risk factors were identified in the retrieved evidence; NBIA is treated as primarily genetic in the included sources.

### 2.3 Protective factors
Not identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Not identified in the retrieved evidence.

## 3. Phenotypes

### 3.1 Core clinical phenotype spectrum (across NBIA)
NBIA disorders present with a broad neurologic phenotype, prominently movement disorders (dystonia, parkinsonism, chorea), pyramidal signs/spasticity, cognitive decline, neuropsychiatric features, speech disorders, and ocular abnormalities in some subtypes. (iankova2021emergingdiseasemodifyingtherapies pages 1-2, spaull2021towardsprecisiontherapies pages 2-4, schneider2025neurodegenerationwithbrain pages 1-2)

### 3.2 Subtype-specific phenotypes with quantitative data (PLAN/INAD)
A 2023 cohort study of **25 genetically confirmed PLAN patients** (18 INAD, 7 late-onset PLAN) quantified symptoms and progression.
- **INAD (n=18)**
  - Initial presentation: gross motor regression in **55.55%**. (dehnavi2023phenotypeandgenotype pages 4-5)
  - During disease course: visual disturbance **77.77%**, bulbar dysfunction **77.77%**, cognitive impairment **61.11%**, seizures **27.77%**, hearing impairment **27.77%**. (dehnavi2023phenotypeandgenotype pages 4-5)
  - Onset: 0–108 months (mean **22.4 months**). (dehnavi2023phenotypeandgenotype pages 4-5)
  - Progression (INAD-RS): mean decline **0.58 points/month**, and “**Sixty percent of the maximum potential loss in the INAD-RS had occurred within 60 months of symptom onset**.” (dehnavi2023phenotypeandgenotype pages 1-2, dehnavi2023phenotypeandgenotype pages 4-5)
- **Late-onset PLAN adults (n=7)**
  - Common features: hypokinesia **6/7**, hand tremor **3/7**, cerebellar atrophy **4/7 (57%)**; iron deposition in globus pallidus and substantia nigra occurred in 1 patient in this cohort excerpt. (dehnavi2023phenotypeandgenotype pages 9-11)

### 3.3 MRI / neuroradiology phenotypes
- MRI is central for NBIA diagnosis and subtype pattern recognition; iron-sensitive sequences (e.g., T2*, SWI) and quantitative mapping (R2* or QSM) can detect and quantify brain iron. (uygun2025quantitativeironmeasurements pages 2-2, romano2022longtermneuroradiologicaland pages 1-2)
- PKAN hallmark: “**eye-of-the-tiger**” sign. (spaull2021towardsprecisiontherapies pages 6-8, romano2022longtermneuroradiologicaland pages 1-2)
- PLAN/INAD: early **cerebellar atrophy** is common and may precede obvious basal ganglia iron in some cases; iron deposition in globus pallidus/substantia nigra can occur. (dehnavi2023phenotypeandgenotype pages 4-5)
- BPAN: reports describe a characteristic midbrain/substantia nigra pattern (T1 hyperintense halo) in association with iron changes. (spaull2021towardsprecisiontherapies pages 6-8)

### 3.4 Suggested HPO terms (non-exhaustive)
Based on phenotypes emphasized in retrieved evidence:
- Dystonia — **HP:0001332**
- Parkinsonism / Bradykinesia — **HP:0001300**, **HP:0002067**
- Spasticity — **HP:0001257**
- Cognitive impairment — **HP:0100543**
- Developmental regression / psychomotor regression — **HP:0002376**
- Cerebellar atrophy — **HP:0001272**
- Ataxia / gait ataxia — **HP:0001251**
- Bulbar dysfunction / dysphagia / dysarthria — **HP:0002015**, **HP:0001260**
- Seizures — **HP:0001250**
- Visual impairment — **HP:0000505**

(HP codes are suggested ontology mappings; the evidence supports the clinical concepts but does not itself provide HPO annotations.) (iankova2021emergingdiseasemodifyingtherapies pages 1-2, dehnavi2023phenotypeandgenotype pages 4-5)

### 3.5 Quality of life impact
NBIA is typically progressive with severe disability and premature mortality in many forms; published sources in the retrieved evidence characterize the conditions as “devastating,” with progressive motor and cognitive decline. (spaull2021towardsprecisiontherapies pages 2-4, uygun2025quantitativeironmeasurements pages 2-2)

## 4. Genetic / Molecular Information

### 4.1 Causal genes and subtype architecture
Authoritative reviews and datasets emphasize the major NBIA entities and genes:
- **PKAN**: PANK2 (schneider2025neurodegenerationwithbrain pages 1-2, marupudi2024genetictargetsand pages 3-4)
- **PLAN/INAD**: PLA2G6 (dehnavi2023phenotypeandgenotype pages 1-2, dehnavi2023phenotypeandgenotype pages 4-5)
- **MPAN**: C19orf12 (schneider2025neurodegenerationwithbrain pages 3-4, marupudi2024genetictargetsand pages 3-4)
- **BPAN**: WDR45 (X-linked dominant) (spaull2021towardsprecisiontherapies pages 6-8, marupudi2024genetictargetsand pages 4-5)
- **Aceruloplasminemia**: CP (schneider2025neurodegenerationwithbrain pages 3-4)
- **Neuroferritinopathy**: FTL (dominant) (schneider2025neurodegenerationwithbrain pages 3-4)

OpenTargets disease–target associations for NBIA (MONDO_0018307) also highlight **PLA2G6, PANK2, C19orf12, ATP13A2, WDR45, CP, COASY** among top associated targets (evidence sizes shown). (OpenTargets Search: Neurodegeneration with brain iron accumulation)

### 4.2 Variant classes and ACMG classification (PLAN example)
In the 2023 PLAN cohort (25 individuals), PLA2G6 variant spectrum included: **15 missense (75%)**, **2 nonsense (10%)**, **1 frameshift (5%)**, **2 splice-site (10%)**; ACMG classifications: **40% pathogenic**, **50% likely pathogenic**, **10% VUS**. Only two variants had gnomAD allele frequencies reported in that paper excerpt (0.0059% and 0.0007%). (dehnavi2023phenotypeandgenotype pages 9-11)

### 4.3 Inheritance patterns
- Many NBIA subtypes are **autosomal recessive** (e.g., PKAN, PLAN, MPAN, aceruloplasminemia). (spaull2021towardsprecisiontherapies pages 6-8, marupudi2024genetictargetsand pages 3-4)
- Some NBIA forms are **autosomal dominant** (e.g., neuroferritinopathy/FTL) or **X-linked dominant** (BPAN/WDR45). (schneider2025neurodegenerationwithbrain pages 3-4, marupudi2024genetictargetsand pages 4-5)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
Not identified in the retrieved evidence.

## 5. Environmental Information
No NBIA-specific environmental or infectious drivers were identified in the retrieved evidence; the dominant explanatory framework in the retrieved sources is genetic causation with downstream metabolic and cellular pathway disruption. (iankova2021emergingdiseasemodifyingtherapies pages 1-2, spaull2021towardsprecisiontherapies pages 2-4)

## 6. Mechanism / Pathophysiology

### 6.1 Mechanistic themes (cross-NBIA)
Retrieved reviews converge on several pathway “classes”:
- **Coenzyme A (CoA) biosynthesis defects** (notably PKAN) (iankova2021emergingdiseasemodifyingtherapies pages 1-2, spaull2021towardsprecisiontherapies pages 5-6)
- **Lipid metabolism / membrane remodeling defects** (notably PLAN) (iankova2021emergingdiseasemodifyingtherapies pages 1-2, marupudi2024genetictargetsand pages 3-4)
- **Autophagy dysfunction** (notably BPAN/WDR45) (spaull2021towardsprecisiontherapies pages 6-8, schneider2025neurodegenerationwithbrain pages 3-4)
- **Mitochondrial dysfunction** as a common downstream theme across multiple subtypes (schneider2025neurodegenerationwithbrain pages 1-2, marupudi2024genetictargetsand pages 7-8)
- **Iron homeostasis primary defects** in a subset (aceruloplasminemia, neuroferritinopathy) (iankova2021emergingdiseasemodifyingtherapies pages 1-2, schneider2025neurodegenerationwithbrain pages 3-4)

A proposed unifying hypothesis cited in reviews is impairment in transferrin receptor (TfR1) recycling/palmitoylation affecting cellular iron handling, although the causal linkage between iron accumulation and neurodegeneration is not fully proven. (iankova2021emergingdiseasemodifyingtherapies pages 1-2, spaull2021towardsprecisiontherapies pages 2-4)

### 6.2 Causal chains (examples)
- **PKAN (PANK2 loss-of-function)** → impaired pantothenate phosphorylation → **CoA deficiency** → mitochondrial/metabolic dysfunction and oxidative stress → basal ganglia neurodegeneration with iron accumulation detectable on MRI. (marupudi2024genetictargetsand pages 3-4, spaull2021towardsprecisiontherapies pages 5-6)
- **PLAN/INAD (PLA2G6 dysfunction)** → defective phospholipase/lipid remodeling → axonal spheroids and neuroaxonal dystrophy pathology → neurodegeneration with cerebellar atrophy and variable iron deposition. (marupudi2024genetictargetsand pages 3-4, dehnavi2023phenotypeandgenotype pages 4-5)
- **BPAN (WDR45)** → impaired autophagy → iron overload plus mitochondrial dysfunction and reduced ferritin reported in reviews. (spaull2021towardsprecisiontherapies pages 6-8)

### 6.3 Biochemical and cellular processes (ontology suggestions)
**GO Biological Process (suggested)**
- iron ion homeostasis; cellular iron ion homeostasis
- autophagy
- lipid metabolic process; phospholipid catabolic process
- mitochondrial organization; oxidative phosphorylation
- response to oxidative stress; lipid peroxidation

**GO Cellular Component (suggested)**
- mitochondrion; mitochondria-associated membranes
- lysosome
- autophagosome

**Cell Ontology (CL) cell types implicated by phenotype/anatomy (suggested)**
- striatal medium spiny neuron; pallidal neuron (basal ganglia neuronal types)
- dopaminergic neuron (substantia nigra)
- astrocyte; oligodendrocyte (for iron handling and white matter findings)

(These are suggested mappings; specific GO/CL term IDs were not provided in the retrieved texts.) (iankova2021emergingdiseasemodifyingtherapies pages 1-2, schneider2025neurodegenerationwithbrain pages 1-2, dehnavi2023phenotypeandgenotype pages 4-5)

### 6.4 Iron as a mechanistic driver and oxidative stress
A 2024 chelator-focused review states that brain iron accumulation in NBIA is “hypothesized to be the cause of oxidative stress, leading to the degeneration of brain tissue.” (Marupudi & Xiong, **2024-03**, DOI: 10.1021/acsbiomedchemau.3c00066) (marupudi2024genetictargetsand pages 1-2)

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary: central nervous system (movement disorder and cognitive/psychiatric decline). (iankova2021emergingdiseasemodifyingtherapies pages 1-2, schneider2025neurodegenerationwithbrain pages 1-2)

### 7.2 Regional neuroanatomy
- Globus pallidus and substantia nigra are the canonical sites of iron deposition across NBIA. (iankova2021emergingdiseasemodifyingtherapies pages 1-2)
- Cerebellum: cerebellar atrophy is prominent in PLAN/INAD cohorts. (dehnavi2023phenotypeandgenotype pages 4-5)

**UBERON suggestions**
- globus pallidus; substantia nigra; cerebellum; basal ganglia

## 8. Temporal Development

### 8.1 Onset patterns
NBIA has wide onset range (infancy through adulthood), depending on subtype and even within gene-defined entities (e.g., PLAN spectrum). (spaull2021towardsprecisiontherapies pages 6-8, dehnavi2023phenotypeandgenotype pages 1-2)

PLAN cohort onset data: in INAD, onset ranged from **0 to 108 months** (mean **22.4 months**). (dehnavi2023phenotypeandgenotype pages 4-5)

### 8.2 Progression
Progression is typically neurodegenerative and progressive. Quantitative longitudinal metric (INAD-RS) in the PLAN cohort: mean decline **0.58 points/month**; a large fraction of functional loss accrued within 5 years from onset. (dehnavi2023phenotypeandgenotype pages 1-2, dehnavi2023phenotypeandgenotype pages 4-5)

## 9. Inheritance and Population

### 9.1 Overall NBIA prevalence
A 2021 review reports combined NBIA prevalence of approximately **1–9 per 1,000,000**. (iankova2021emergingdiseasemodifyingtherapies pages 1-2)

### 9.2 Subtype epidemiology — PLAN genetic prevalence (2024)
A 2024 study estimated PLAN genetic prevalence using ClinVar/HGMD/gnomAD allele frequencies:
- Overall genetic prevalence (including pathogenic and/or conflicting variants): **1 in 987,267 to 1 in 1,570,079 pregnancies**. (Kurtovic‑Kozaric et al., **2024-10**, DOI: 10.1186/s13023-024-03275-x) (kurtovickozaric2024anestimationof pages 1-2)
- Highest estimated prevalence:
  - African/African-American: **1 in 421,960 to 1 in 365,197**
  - East Asian: **1 in 683,978 to 1 in 190,771** (kurtovickozaric2024anestimationof pages 1-2)
- Carrier frequency estimates: approximately **1 in 497 to 1 in 627** individuals. (kurtovickozaric2024anestimationof pages 4-6)
- Global burden projection: **82–127 affected births/year** based on global births. (kurtovickozaric2024anestimationof pages 4-6)

Interpretation from that paper: the authors emphasize likely **underdiagnosis** and the need for expanded sequencing in non-European populations. (kurtovickozaric2024anestimationof pages 1-2)

## 10. Diagnostics

### 10.1 Clinical and imaging diagnostics
- MRI is a primary diagnostic modality; iron-sensitive sequences identify characteristic patterns, sometimes before overt clinical features. (schneider2025neurodegenerationwithbrain pages 3-4, romano2022longtermneuroradiologicaland pages 1-2)
- Quantitative approaches:
  - **R2*** relaxometry used to quantify pallidal iron and track response to chelation in NBIA cohorts. (romano2022longtermneuroradiologicaland pages 2-4)
  - **QSM** highlighted as potentially more sensitive for early detection/quantitation of iron. (uygun2025quantitativeironmeasurements pages 2-2)

### 10.2 Genetic testing strategy
Diagnosis is suspected from phenotype + MRI and confirmed by genetic testing; recommended approaches include single-gene testing when phenotype/MRI is highly characteristic (e.g., PKAN eye-of-the-tiger), multigene panels, or WES/WGS for broader heterogeneity. (spaull2021towardsprecisiontherapies pages 2-4)

PLAN cohort confirms real-world approach: whole-exome sequencing followed by Sanger co-segregation, ACMG classification, and MAF checks in gnomAD. (dehnavi2023phenotypeandgenotype pages 2-4, dehnavi2023phenotypeandgenotype pages 9-11)

### 10.3 Differential diagnosis
Not systematically extracted in the retrieved evidence.

## 11. Outcome / Prognosis
Quantitative survival estimates were not retrieved. However, NBIA is consistently described as progressive and severely disabling, often with premature mortality in severe childhood-onset forms. (spaull2021towardsprecisiontherapies pages 2-4, uygun2025quantitativeironmeasurements pages 2-2)

## 12. Treatment

### 12.1 Symptomatic vs disease-modifying treatment landscape
Reviews consistently state that NBIA treatment is largely symptomatic and that proven disease-modifying treatments remain limited, motivating mechanistically targeted (precision) therapies. (spaull2021towardsprecisiontherapies pages 2-4, marupudi2024genetictargetsand pages 1-2)

### 12.2 Iron chelation (deferiprone and others)
**Deferiprone (DFP)** is repeatedly highlighted because it can cross the blood–brain barrier and has been tested in PKAN and other NBIA contexts. (romano2022longtermneuroradiologicaland pages 1-2)

Prospective long-term NBIA cohort (Romano et al., **2022-08**, DOI: 10.3390/jcm11154524):
- Dose: **15 mg/kg BID** (30 mg/kg/day) (romano2022longtermneuroradiologicaland pages 2-4)
- Follow-up: **5.5 ± 2.3 years** (range 2.4–9.6) (romano2022longtermneuroradiologicaland pages 2-4)
- Quantitative MRI outcome: GPi R2* decreased significantly (left **47.6 ± 6.4 Hz → 37.3 ± 5.8 Hz**; right **48.4 ± 6.2 Hz → 37.9 ± 6.6 Hz**, both p<0.0001). (romano2022longtermneuroradiologicaland pages 4-7)
- Clinical outcome: “substantial stability” overall; correlation between radiology and clinical measures not significant. (romano2022longtermneuroradiologicaland pages 1-2, romano2022longtermneuroradiologicaland pages 4-7)

Neuroferritinopathy case series (Marchand et al., **2022-08**, DOI: 10.1002/mds.29145):
- Deferiprone **30 mg/kg/day** in 4 patients, with reports including >11-year stabilization in one patient and marked improvements in some individuals; hematologic risk (neutropenia) observed and requires monitoring. (marchand2022conservativeironchelation pages 3-4, marchand2022conservativeironchelation pages 1-2)

Other chelators discussed in the 2024 review include deferoxamine and deferasirox; limitations include BBB penetration and toxicity concerns, and new delivery methods (intranasal and nanocarriers) are proposed to improve CNS targeting. (marupudi2024genetictargetsand pages 1-2, marupudi2024genetictargetsand pages 5-6, marupudi2024genetictargetsand pages 7-8)

### 12.3 Substrate replacement / pathway-bypass strategies (PKAN)
- A 2021 review reports that a randomized controlled trial of **fosmetpantotenate** did not show significant benefit and extensions were terminated early. (iankova2021emergingdiseasemodifyingtherapies pages 1-2)
- ClinicalTrials.gov confirms fosmetpantotenate study **NCT03041116** listed as terminated (trial details limited in our extracted clinical-trial chunk set). (spaull2021towardsprecisiontherapies pages 2-4)
- **CoA-Z** (OHSU) is an investigational product intended to bypass metabolic defects in PKAN; trial **NCT04182763** is completed with 77 participants, with a randomized double-blind phase followed by open-label period and safety/molecular endpoints. (NCT04182763 chunk 1)

### 12.4 PLAN-targeted approaches
A 2021 review highlights **deuterated polyunsaturated fatty acids (D-PUFA)** to reduce mitochondrial lipid peroxidation in PLAN and discusses **desipramine** repurposing in infantile neuroaxonal dystrophy to block ceramide accumulation, with gene replacement in preclinical stage. (iankova2021emergingdiseasemodifyingtherapies pages 1-2)

### 12.5 Clinical trials and real-world implementations
Key NBIA clinical trial and infrastructure resources identified in this evidence set:
- **TIRCON**: an international NBIA network reported to include a global patient registry/biobank with baseline and follow-up data of **>400 NBIA patients** and to have run a randomized deferiprone trial in PKAN. (uygun2025quantitativeironmeasurements pages 2-2)
- **NBIAready** natural history patient-reported outcomes study: **NCT02587858**, observational; estimated enrollment 300; online assessments every ~6 months for 5–10 years. (NCT02587858 chunk 1)
- **Deferiprone in PKAN**: NCT01741532 (MRI R2* brain iron change over 18 months as key endpoint) and extension NCT02174848 (Phase 3, 68 participants; BAD scale, PGI-I; safety endpoints). (NCT01741532 chunk 2, NCT02174848 chunk 1)

### 12.6 MAXO term suggestions (treatments/actions)
- Iron chelation therapy (e.g., deferiprone) — “iron chelation”
- Magnetic resonance imaging (diagnostic imaging)
- Whole-exome sequencing / genome sequencing (genetic diagnostic procedure)
- Symptomatic dystonia management (e.g., baclofen, botulinum toxin; noted in case-report literature but not a primary evidence focus here) (schneider2025neurodegenerationwithbrain pages 1-2)

(MAXO IDs not provided in the retrieved evidence; terms are suggested for mapping.)

## 13. Prevention
No primary prevention strategies were identified in the retrieved evidence. For genetic NBIA, prevention in practice is typically via **genetic counseling** and reproductive options; the retrieved evidence supports the role of genetic testing and counseling but does not provide prevention-specific programs or guidelines. (schneider2025neurodegenerationwithbrain pages 3-4)

## 14. Other Species / Natural Disease
Not identified in the retrieved evidence.

## 15. Model Organisms
The retrieved evidence set includes review-level statements that animal and cell models are used to evaluate candidate therapies (e.g., 4′-phosphopantetheine in PKAN models; D-PUFA in PLAN models; preclinical gene replacement), but detailed model organism phenotypes were not extracted in the current snippets. (iankova2021emergingdiseasemodifyingtherapies pages 1-2, spaull2021towardsprecisiontherapies pages 2-4)

## 2023–2024 Developments (prioritized)

1) **2024: Therapeutic delivery and chelator engineering focus** — A 2024 ACS review synthesizes chelator options for NBIA and emphasizes future directions such as **intranasal delivery** and **nanocarrier approaches** to bypass BBB and reduce systemic toxicity, alongside gene-therapy modalities (ASO, AAV, CRISPR). (Marupudi & Xiong, **2024-03**, DOI: 10.1021/acsbiomedchemau.3c00066) (marupudi2024genetictargetsand pages 5-6, marupudi2024genetictargetsand pages 6-7, marupudi2024genetictargetsand pages 7-8)

2) **2023: Quantitative natural history metrics in PLAN/INAD** — The 2023 Orphanet cohort reports INAD-RS progression (0.58 points/month) and symptom frequencies, supporting more standardized endpoints for trials and care. (Dehnavi et al., **2023-07**, DOI: 10.1186/s13023-023-02780-9) (dehnavi2023phenotypeandgenotype pages 4-5)

3) **2024: Global genetic prevalence estimates for PLAN** — PLAN prevalence and carrier frequencies were estimated from gnomAD and variant databases with population-stratified projections; results highlight underdiagnosis and the need for sequencing in underrepresented ancestries. (Kurtovic‑Kozaric et al., **2024-10**, DOI: 10.1186/s13023-024-03275-x) (kurtovickozaric2024anestimationof pages 1-2, kurtovickozaric2024anestimationof pages 4-6)

## Visual evidence (figure/table)
A key synthesis figure and tables summarizing NBIA genes, pathways, and trialed/in-development therapies were retrieved from Spaull et al. 2021 (Figure 1 and Tables 1–2). (spaull2021towardsprecisiontherapies media e9e8d758, spaull2021towardsprecisiontherapies media efb687c0, spaull2021towardsprecisiontherapies media 7e7d49af, spaull2021towardsprecisiontherapies media c661aa84)

## Cross-subtype comparison table
| Subtype (common name) | Gene(s) | Inheritance | Core clinical features | Characteristic MRI features | Pathway/mechanism themes | Notable disease-modifying/experimental therapies or trials |
|---|---|---|---|---|---|---|
| PKAN (pantothenate kinase-associated neurodegeneration) | **PANK2** | Autosomal recessive | Progressive dystonia, rigidity/bradykinesia, spasticity, dysarthria, postural instability, feeding/communication difficulty; classic childhood-onset and atypical later-onset forms (iankova2021emergingdiseasemodifyingtherapies pages 1-2, schneider2025neurodegenerationwithbrain pages 1-2, marupudi2024genetictargetsand pages 3-4) | Iron accumulation in globus pallidus; classic **“eye-of-the-tiger”** sign; MRI R2* used to quantify pallidal iron (spaull2021towardsprecisiontherapies pages 6-8, romano2022longtermneuroradiologicaland pages 1-2, NCT01741532 chunk 2) | Defective CoA biosynthesis, mitochondrial dysfunction, impaired dopamine metabolism, lipid peroxidation/possible ferroptosis, downstream iron dyshomeostasis (spaull2021towardsprecisiontherapies pages 5-6, marupudi2024genetictargetsand pages 3-4) | **Deferiprone** phase 3 TIRCON/NCT01741532 and extension NCT02174848; radiologic iron reduction with trend to slower progression. **Fosmetpantotenate** phase 3 NCT03041116 terminated/negative. **CoA-Z** completed NCT04182763. 4′-phosphopantetheine and **PZ-2891** discussed as precision approaches (iankova2021emergingdiseasemodifyingtherapies pages 1-2, spaull2021towardsprecisiontherapies pages 2-4, marupudi2024genetictargetsand pages 5-6, NCT02174848 chunk 1, NCT04182763 chunk 1) |
| PLAN / INAD (PLA2G6-associated neurodegeneration; infantile neuroaxonal dystrophy spectrum) | **PLA2G6** | Autosomal recessive | Infantile psychomotor/gross motor regression, bulbar dysfunction, visual disturbance, cognitive impairment; later-onset dystonia-parkinsonism with hypokinesia, tremor, ataxic gait, cognitive/psychiatric features (iankova2021emergingdiseasemodifyingtherapies pages 1-2, dehnavi2023phenotypeandgenotype pages 1-2, dehnavi2023phenotypeandgenotype pages 4-5) | Early **cerebellar atrophy** common; may show iron deposition in globus pallidus/substantia nigra; white-matter/callosal abnormalities and optic atrophy reported (spaull2021towardsprecisiontherapies pages 6-8, dehnavi2023phenotypeandgenotype pages 2-4, dehnavi2023phenotypeandgenotype pages 4-5) | Lipid metabolism/phospholipase dysfunction, axonal spheroids, mitochondrial dysfunction, lipid peroxidation, α-synuclein/tau-related pathology (spaull2021towardsprecisiontherapies pages 6-8, marupudi2024genetictargetsand pages 3-4) | No proven disease-modifying therapy; **D-PUFA** proposed to reduce mitochondrial lipid peroxidation; **desipramine** repurposing discussed for infantile neuroaxonal dystrophy; gene therapy remains preclinical (iankova2021emergingdiseasemodifyingtherapies pages 1-2, spaull2021towardsprecisiontherapies pages 2-4) |
| MPAN (mitochondrial membrane protein-associated neurodegeneration) | **C19orf12** | Usually autosomal recessive; rare monoallelic cases reported | Dystonia-parkinsonism, optic atrophy, axonal neuropathy, cognitive/psychiatric features; Lewy body pathology described (iankova2021emergingdiseasemodifyingtherapies pages 1-2, spaull2021towardsprecisiontherapies pages 6-8, marupudi2024genetictargetsand pages 3-4) | T2 hypointensity/iron-related signal in globus pallidus and substantia nigra; basal ganglia iron accumulation (spaull2021towardsprecisiontherapies pages 6-8, marupudi2024genetictargetsand pages 3-4) | Mitochondrial membrane dysfunction, lipid metabolism abnormalities, iron dyshomeostasis (iankova2021emergingdiseasemodifyingtherapies pages 1-2, marupudi2024genetictargetsand pages 3-4) | No established disease-modifying therapy; **deferiprone** reported in case literature with variable response (iankova2021emergingdiseasemodifyingtherapies pages 1-2, marupudi2024genetictargetsand pages 5-6) |
| BPAN (beta-propeller protein-associated neurodegeneration) | **WDR45** | X-linked dominant | Developmental delay/intellectual disability followed later by parkinsonism-dystonia; cognitive decline and neuropsychiatric features (iankova2021emergingdiseasemodifyingtherapies pages 1-2, spaull2021towardsprecisiontherapies pages 6-8) | T2 hypointensity in globus pallidus/substantia nigra with characteristic **T1 hyperintense halo in the substantia nigra** / midbrain halo pattern (spaull2021towardsprecisiontherapies pages 6-8) | Defective autophagy, reduced ferritin, mitochondrial dysfunction, iron overload (spaull2021towardsprecisiontherapies pages 6-8) | No proven disease-modifying therapy; small studies/case experience with **deferiprone** showed mixed clinical effects (spaull2021towardsprecisiontherapies pages 6-8) |
| Aceruloplasminemia | **CP** | Autosomal recessive | Neurologic disease with movement disorder/cognitive features; systemic iron overload with diabetes often prominent at presentation (schneider2025neurodegenerationwithbrain pages 3-4) | Brain iron accumulation; systemic iron deposition can involve retina, pancreas, liver (schneider2025neurodegenerationwithbrain pages 3-4) | Direct iron-homeostasis defect due to absent/defective ferroxidase activity and impaired iron mobilization (iankova2021emergingdiseasemodifyingtherapies pages 1-2, schneider2025neurodegenerationwithbrain pages 3-4) | No established causal therapy in gathered evidence; iron chelation is part of general NBIA disease-modifying rationale, but subtype-specific trial evidence not detailed here (iankova2021emergingdiseasemodifyingtherapies pages 1-2, schneider2025neurodegenerationwithbrain pages 3-4) |
| Neuroferritinopathy | **FTL** | Autosomal dominant | Progressive movement disorder phenotype within NBIA spectrum (schneider2025neurodegenerationwithbrain pages 3-4, marchand2022conservativeironchelation pages 1-2) | Brain iron overload with MRI R2* tracking regional iron burden (marchand2022conservativeironchelation pages 2-3, marchand2022conservativeironchelation pages 4-5) | Direct iron-homeostasis defect from abnormal ferritin configuration/iron storage (iankova2021emergingdiseasemodifyingtherapies pages 1-2, schneider2025neurodegenerationwithbrain pages 3-4) | **Deferiprone** conservative chelation (30 mg/kg/day) in small series/cases: stabilization or improvement in some patients, R2* reductions in some regions, but neutropenia risk requires monitoring (marchand2022conservativeironchelation pages 2-3, marchand2022conservativeironchelation pages 3-4, marchand2022conservativeironchelation pages 1-2) |


*Table: Compact comparison of the principal NBIA disorders, summarizing genes, inheritance, hallmark phenotypes, MRI signatures, mechanisms, and disease-modifying or investigational therapies supported by the gathered evidence.*

## Evidence limitations and gaps (important for knowledge base curation)
- This run did not retrieve OMIM/Orphanet/ICD/MeSH entries directly; MONDO was available via OpenTargets. (OpenTargets Search: Neurodegeneration with brain iron accumulation)
- Several key randomized trial results (e.g., published deferiprone RCT results in Lancet Neurology referenced in trial record/reviews) were not directly retrieved as full papers in this run; consequently, effect-size estimates beyond MRI/scale descriptions in the extracted records are limited. (NCT01741532 chunk 2, iankova2021emergingdiseasemodifyingtherapies pages 1-2)
- Environmental factors, protective factors, gene–environment interactions, and systematic differential diagnosis lists were not present in the retrieved evidence set.

## URLs and publication dates (selected key sources)
- Marupudi N, Xiong MP. **Genetic Targets and Applications of Iron Chelators for NBIA**. *ACS Bio & Med Chem Au*. **2024-03**. https://doi.org/10.1021/acsbiomedchemau.3c00066 (marupudi2024genetictargetsand pages 1-2)
- Dehnavi AZ et al. **Phenotype and genotype heterogeneity of PLAN**. *Orphanet J Rare Dis*. **2023-07**. https://doi.org/10.1186/s13023-023-02780-9 (dehnavi2023phenotypeandgenotype pages 1-2)
- Kurtovic‑Kozaric A et al. **Global genetic prevalence of PLAN**. *Orphanet J Rare Dis*. **2024-10**. https://doi.org/10.1186/s13023-024-03275-x (kurtovickozaric2024anestimationof pages 1-2)
- Romano N et al. **Long-term deferiprone in NBIA**. *J Clin Med*. **2022-08**. https://doi.org/10.3390/jcm11154524 (romano2022longtermneuroradiologicaland pages 2-4)
- ClinicalTrials.gov: **NCT04182763 (CoA‑Z in PKAN)** (posted 2019; completed 2025) https://clinicaltrials.gov/study/NCT04182763 (NCT04182763 chunk 1)
- ClinicalTrials.gov: **NCT02174848 (TIRCON-EXT deferiprone extension)** (posted 2014; completed 2018; results posted 2019) https://clinicaltrials.gov/study/NCT02174848 (NCT02174848 chunk 1)
- ClinicalTrials.gov: **NCT02587858 (NBIAready natural history PROs)** (posted 2015) https://clinicaltrials.gov/study/NCT02587858 (NCT02587858 chunk 1)


References

1. (iankova2021emergingdiseasemodifyingtherapies pages 1-2): Vassilena Iankova, Ivan Karin, Thomas Klopstock, and Susanne A. Schneider. Emerging disease-modifying therapies in neurodegeneration with brain iron accumulation (nbia) disorders. Frontiers in Neurology, Apr 2021. URL: https://doi.org/10.3389/fneur.2021.629414, doi:10.3389/fneur.2021.629414. This article has 87 citations and is from a peer-reviewed journal.

2. (schneider2025neurodegenerationwithbrain pages 1-2): Susanne A. Schneider. Neurodegeneration with brain iron accumulation. Current Neurology and Neuroscience Reports, 16:1-9, Jan 2025. URL: https://doi.org/10.1007/s11910-015-0608-3, doi:10.1007/s11910-015-0608-3. This article has 38 citations and is from a domain leading peer-reviewed journal.

3. (OpenTargets Search: Neurodegeneration with brain iron accumulation): Open Targets Query (Neurodegeneration with brain iron accumulation, 15 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (spaull2021towardsprecisiontherapies pages 2-4): Robert V.V. Spaull, Audrey K.S. Soo, Penelope Hogarth, Susan J. Hayflick, and Manju A. Kurian. Towards precision therapies for inherited disorders of neurodegeneration with brain iron accumulation. Tremor and Other Hyperkinetic Movements, Nov 2021. URL: https://doi.org/10.5334/tohm.661, doi:10.5334/tohm.661. This article has 30 citations and is from a peer-reviewed journal.

5. (dehnavi2023phenotypeandgenotype pages 1-2): Ali Zare Dehnavi, Maryam Bemanalizadeh, Seyyed Mohammad Kahani, Mahmoud Reza Ashrafi, Mohammad Rohani, Mehran Beiraghi Toosi, Morteza Heidari, Sareh Hosseinpour, Behnam Amini, Shaghayegh Zokaei, Zahra Rezaei, Hajar Aryan, Man Amanat, Hassan Vahidnezhad, Pouria Mohammadi, Masoud Garshasbi, and Ali Reza Tavasoli. Phenotype and genotype heterogeneity of pla2g6-associated neurodegeneration in a cohort of pediatric and adult patients. Orphanet Journal of Rare Diseases, Jul 2023. URL: https://doi.org/10.1186/s13023-023-02780-9, doi:10.1186/s13023-023-02780-9. This article has 19 citations and is from a peer-reviewed journal.

6. (NCT02587858 chunk 1): Susan J. Hayflick. NBIAready: Online Collection of Natural History Patient-reported Outcome Measures. Susan J. Hayflick. 2015. ClinicalTrials.gov Identifier: NCT02587858

7. (NCT02174848 chunk 1):  Long-term Deferiprone Treatment in Patients With Pantothenate Kinase-Associated Neurodegeneration. ApoPharma. 2014. ClinicalTrials.gov Identifier: NCT02174848

8. (NCT04182763 chunk 1): Susan J. Hayflick. CoA-Z in Pantothenate Kinase-associated Neurodegeneration (PKAN). Oregon Health and Science University. 2019. ClinicalTrials.gov Identifier: NCT04182763

9. (uygun2025quantitativeironmeasurements pages 2-2): Özge Uygun, A. Özcan, Fuat Kaan Aras, Evrim Bozdemir, S. U. Ugur Iseri, Murat Gültekin, N. H. Akçakaya, Orkhan Mammadov, Gülay Kır, Dilek İnce Günal, Neşe Tuncer, Fatma Betül Özdilek, Banu Özen Barut, Ercan Köse, Hülya Apaydın, Asuman Ali, S. Çağırıcı, Pınar Topaloğlu, Alp Dinçer, and Zuhal Yapıcı. Quantitative iron measurements in the basal ganglia of nbia patients using qsm: insights from a tertiary center. Annals of clinical and translational neurology, Aug 2025. URL: https://doi.org/10.1002/acn3.70161, doi:10.1002/acn3.70161. This article has 1 citations and is from a peer-reviewed journal.

10. (schneider2025neurodegenerationwithbrain pages 3-4): Susanne A. Schneider. Neurodegeneration with brain iron accumulation. Current Neurology and Neuroscience Reports, 16:1-9, Jan 2025. URL: https://doi.org/10.1007/s11910-015-0608-3, doi:10.1007/s11910-015-0608-3. This article has 38 citations and is from a domain leading peer-reviewed journal.

11. (dehnavi2023phenotypeandgenotype pages 9-11): Ali Zare Dehnavi, Maryam Bemanalizadeh, Seyyed Mohammad Kahani, Mahmoud Reza Ashrafi, Mohammad Rohani, Mehran Beiraghi Toosi, Morteza Heidari, Sareh Hosseinpour, Behnam Amini, Shaghayegh Zokaei, Zahra Rezaei, Hajar Aryan, Man Amanat, Hassan Vahidnezhad, Pouria Mohammadi, Masoud Garshasbi, and Ali Reza Tavasoli. Phenotype and genotype heterogeneity of pla2g6-associated neurodegeneration in a cohort of pediatric and adult patients. Orphanet Journal of Rare Diseases, Jul 2023. URL: https://doi.org/10.1186/s13023-023-02780-9, doi:10.1186/s13023-023-02780-9. This article has 19 citations and is from a peer-reviewed journal.

12. (dehnavi2023phenotypeandgenotype pages 4-5): Ali Zare Dehnavi, Maryam Bemanalizadeh, Seyyed Mohammad Kahani, Mahmoud Reza Ashrafi, Mohammad Rohani, Mehran Beiraghi Toosi, Morteza Heidari, Sareh Hosseinpour, Behnam Amini, Shaghayegh Zokaei, Zahra Rezaei, Hajar Aryan, Man Amanat, Hassan Vahidnezhad, Pouria Mohammadi, Masoud Garshasbi, and Ali Reza Tavasoli. Phenotype and genotype heterogeneity of pla2g6-associated neurodegeneration in a cohort of pediatric and adult patients. Orphanet Journal of Rare Diseases, Jul 2023. URL: https://doi.org/10.1186/s13023-023-02780-9, doi:10.1186/s13023-023-02780-9. This article has 19 citations and is from a peer-reviewed journal.

13. (romano2022longtermneuroradiologicaland pages 1-2): Nicola Romano, Giammarco Baiardi, Valeria Maria Pinto, Sabrina Quintino, Barbara Gianesin, Riccardo Sasso, Andrea Diociasi, Francesca Mattioli, Roberta Marchese, Giovanni Abbruzzese, Antonio Castaldi, and Gian Luca Forni. Long-term neuroradiological and clinical evaluation of nbia patients treated with a deferiprone based iron-chelation therapy. Journal of Clinical Medicine, 11:4524, Aug 2022. URL: https://doi.org/10.3390/jcm11154524, doi:10.3390/jcm11154524. This article has 21 citations.

14. (spaull2021towardsprecisiontherapies pages 6-8): Robert V.V. Spaull, Audrey K.S. Soo, Penelope Hogarth, Susan J. Hayflick, and Manju A. Kurian. Towards precision therapies for inherited disorders of neurodegeneration with brain iron accumulation. Tremor and Other Hyperkinetic Movements, Nov 2021. URL: https://doi.org/10.5334/tohm.661, doi:10.5334/tohm.661. This article has 30 citations and is from a peer-reviewed journal.

15. (marupudi2024genetictargetsand pages 3-4): Neharika Marupudi and May P. Xiong. Genetic targets and applications of iron chelators for neurodegeneration with brain iron accumulation. ACS Bio & Med Chem Au, 4:119-130, Mar 2024. URL: https://doi.org/10.1021/acsbiomedchemau.3c00066, doi:10.1021/acsbiomedchemau.3c00066. This article has 22 citations.

16. (marupudi2024genetictargetsand pages 4-5): Neharika Marupudi and May P. Xiong. Genetic targets and applications of iron chelators for neurodegeneration with brain iron accumulation. ACS Bio & Med Chem Au, 4:119-130, Mar 2024. URL: https://doi.org/10.1021/acsbiomedchemau.3c00066, doi:10.1021/acsbiomedchemau.3c00066. This article has 22 citations.

17. (spaull2021towardsprecisiontherapies pages 5-6): Robert V.V. Spaull, Audrey K.S. Soo, Penelope Hogarth, Susan J. Hayflick, and Manju A. Kurian. Towards precision therapies for inherited disorders of neurodegeneration with brain iron accumulation. Tremor and Other Hyperkinetic Movements, Nov 2021. URL: https://doi.org/10.5334/tohm.661, doi:10.5334/tohm.661. This article has 30 citations and is from a peer-reviewed journal.

18. (marupudi2024genetictargetsand pages 7-8): Neharika Marupudi and May P. Xiong. Genetic targets and applications of iron chelators for neurodegeneration with brain iron accumulation. ACS Bio & Med Chem Au, 4:119-130, Mar 2024. URL: https://doi.org/10.1021/acsbiomedchemau.3c00066, doi:10.1021/acsbiomedchemau.3c00066. This article has 22 citations.

19. (marupudi2024genetictargetsand pages 1-2): Neharika Marupudi and May P. Xiong. Genetic targets and applications of iron chelators for neurodegeneration with brain iron accumulation. ACS Bio & Med Chem Au, 4:119-130, Mar 2024. URL: https://doi.org/10.1021/acsbiomedchemau.3c00066, doi:10.1021/acsbiomedchemau.3c00066. This article has 22 citations.

20. (kurtovickozaric2024anestimationof pages 1-2): Amina Kurtovic-Kozaric, Moriel Singer-Berk, Jordan Wood, Emily Evangelista, Leena Panwala, Amanda Hope, Stefanie M. Heinrich, Samantha Baxter, and Mark J. Kiel. An estimation of global genetic prevalence of pla2g6-associated neurodegeneration. Orphanet Journal of Rare Diseases, Oct 2024. URL: https://doi.org/10.1186/s13023-024-03275-x, doi:10.1186/s13023-024-03275-x. This article has 11 citations and is from a peer-reviewed journal.

21. (kurtovickozaric2024anestimationof pages 4-6): Amina Kurtovic-Kozaric, Moriel Singer-Berk, Jordan Wood, Emily Evangelista, Leena Panwala, Amanda Hope, Stefanie M. Heinrich, Samantha Baxter, and Mark J. Kiel. An estimation of global genetic prevalence of pla2g6-associated neurodegeneration. Orphanet Journal of Rare Diseases, Oct 2024. URL: https://doi.org/10.1186/s13023-024-03275-x, doi:10.1186/s13023-024-03275-x. This article has 11 citations and is from a peer-reviewed journal.

22. (romano2022longtermneuroradiologicaland pages 2-4): Nicola Romano, Giammarco Baiardi, Valeria Maria Pinto, Sabrina Quintino, Barbara Gianesin, Riccardo Sasso, Andrea Diociasi, Francesca Mattioli, Roberta Marchese, Giovanni Abbruzzese, Antonio Castaldi, and Gian Luca Forni. Long-term neuroradiological and clinical evaluation of nbia patients treated with a deferiprone based iron-chelation therapy. Journal of Clinical Medicine, 11:4524, Aug 2022. URL: https://doi.org/10.3390/jcm11154524, doi:10.3390/jcm11154524. This article has 21 citations.

23. (dehnavi2023phenotypeandgenotype pages 2-4): Ali Zare Dehnavi, Maryam Bemanalizadeh, Seyyed Mohammad Kahani, Mahmoud Reza Ashrafi, Mohammad Rohani, Mehran Beiraghi Toosi, Morteza Heidari, Sareh Hosseinpour, Behnam Amini, Shaghayegh Zokaei, Zahra Rezaei, Hajar Aryan, Man Amanat, Hassan Vahidnezhad, Pouria Mohammadi, Masoud Garshasbi, and Ali Reza Tavasoli. Phenotype and genotype heterogeneity of pla2g6-associated neurodegeneration in a cohort of pediatric and adult patients. Orphanet Journal of Rare Diseases, Jul 2023. URL: https://doi.org/10.1186/s13023-023-02780-9, doi:10.1186/s13023-023-02780-9. This article has 19 citations and is from a peer-reviewed journal.

24. (romano2022longtermneuroradiologicaland pages 4-7): Nicola Romano, Giammarco Baiardi, Valeria Maria Pinto, Sabrina Quintino, Barbara Gianesin, Riccardo Sasso, Andrea Diociasi, Francesca Mattioli, Roberta Marchese, Giovanni Abbruzzese, Antonio Castaldi, and Gian Luca Forni. Long-term neuroradiological and clinical evaluation of nbia patients treated with a deferiprone based iron-chelation therapy. Journal of Clinical Medicine, 11:4524, Aug 2022. URL: https://doi.org/10.3390/jcm11154524, doi:10.3390/jcm11154524. This article has 21 citations.

25. (marchand2022conservativeironchelation pages 3-4): Felix Marchand, Caroline Moreau, Gregory Kuchcinski, Vincent Huin, Luc Defebvre, and David Devos. Conservative iron chelation for neuroferritinopathy. Movement Disorders, 37:1948-1952, Aug 2022. URL: https://doi.org/10.1002/mds.29145, doi:10.1002/mds.29145. This article has 19 citations and is from a highest quality peer-reviewed journal.

26. (marchand2022conservativeironchelation pages 1-2): Felix Marchand, Caroline Moreau, Gregory Kuchcinski, Vincent Huin, Luc Defebvre, and David Devos. Conservative iron chelation for neuroferritinopathy. Movement Disorders, 37:1948-1952, Aug 2022. URL: https://doi.org/10.1002/mds.29145, doi:10.1002/mds.29145. This article has 19 citations and is from a highest quality peer-reviewed journal.

27. (marupudi2024genetictargetsand pages 5-6): Neharika Marupudi and May P. Xiong. Genetic targets and applications of iron chelators for neurodegeneration with brain iron accumulation. ACS Bio & Med Chem Au, 4:119-130, Mar 2024. URL: https://doi.org/10.1021/acsbiomedchemau.3c00066, doi:10.1021/acsbiomedchemau.3c00066. This article has 22 citations.

28. (NCT01741532 chunk 2):  Efficacy and Safety Study of Deferiprone in Patients With Pantothenate Kinase-associated Neurodegeneration (PKAN). ApoPharma. 2012. ClinicalTrials.gov Identifier: NCT01741532

29. (marupudi2024genetictargetsand pages 6-7): Neharika Marupudi and May P. Xiong. Genetic targets and applications of iron chelators for neurodegeneration with brain iron accumulation. ACS Bio & Med Chem Au, 4:119-130, Mar 2024. URL: https://doi.org/10.1021/acsbiomedchemau.3c00066, doi:10.1021/acsbiomedchemau.3c00066. This article has 22 citations.

30. (spaull2021towardsprecisiontherapies media e9e8d758): Robert V.V. Spaull, Audrey K.S. Soo, Penelope Hogarth, Susan J. Hayflick, and Manju A. Kurian. Towards precision therapies for inherited disorders of neurodegeneration with brain iron accumulation. Tremor and Other Hyperkinetic Movements, Nov 2021. URL: https://doi.org/10.5334/tohm.661, doi:10.5334/tohm.661. This article has 30 citations and is from a peer-reviewed journal.

31. (spaull2021towardsprecisiontherapies media efb687c0): Robert V.V. Spaull, Audrey K.S. Soo, Penelope Hogarth, Susan J. Hayflick, and Manju A. Kurian. Towards precision therapies for inherited disorders of neurodegeneration with brain iron accumulation. Tremor and Other Hyperkinetic Movements, Nov 2021. URL: https://doi.org/10.5334/tohm.661, doi:10.5334/tohm.661. This article has 30 citations and is from a peer-reviewed journal.

32. (spaull2021towardsprecisiontherapies media 7e7d49af): Robert V.V. Spaull, Audrey K.S. Soo, Penelope Hogarth, Susan J. Hayflick, and Manju A. Kurian. Towards precision therapies for inherited disorders of neurodegeneration with brain iron accumulation. Tremor and Other Hyperkinetic Movements, Nov 2021. URL: https://doi.org/10.5334/tohm.661, doi:10.5334/tohm.661. This article has 30 citations and is from a peer-reviewed journal.

33. (spaull2021towardsprecisiontherapies media c661aa84): Robert V.V. Spaull, Audrey K.S. Soo, Penelope Hogarth, Susan J. Hayflick, and Manju A. Kurian. Towards precision therapies for inherited disorders of neurodegeneration with brain iron accumulation. Tremor and Other Hyperkinetic Movements, Nov 2021. URL: https://doi.org/10.5334/tohm.661, doi:10.5334/tohm.661. This article has 30 citations and is from a peer-reviewed journal.

34. (marchand2022conservativeironchelation pages 2-3): Felix Marchand, Caroline Moreau, Gregory Kuchcinski, Vincent Huin, Luc Defebvre, and David Devos. Conservative iron chelation for neuroferritinopathy. Movement Disorders, 37:1948-1952, Aug 2022. URL: https://doi.org/10.1002/mds.29145, doi:10.1002/mds.29145. This article has 19 citations and is from a highest quality peer-reviewed journal.

35. (marchand2022conservativeironchelation pages 4-5): Felix Marchand, Caroline Moreau, Gregory Kuchcinski, Vincent Huin, Luc Defebvre, and David Devos. Conservative iron chelation for neuroferritinopathy. Movement Disorders, 37:1948-1952, Aug 2022. URL: https://doi.org/10.1002/mds.29145, doi:10.1002/mds.29145. This article has 19 citations and is from a highest quality peer-reviewed journal.