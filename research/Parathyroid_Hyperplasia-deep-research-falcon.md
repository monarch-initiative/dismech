---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T19:32:07.215873'
end_time: '2026-05-07T19:50:44.778585'
duration_seconds: 1117.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Parathyroid Hyperplasia
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 78
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Parathyroid Hyperplasia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Parathyroid Hyperplasia** covering all of the
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
- **Disease Name:** Parathyroid Hyperplasia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Parathyroid Hyperplasia** covering all of the
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


# Comprehensive Disease Characteristics Report: Parathyroid Hyperplasia

## Target disease
**Disease name:** Parathyroid hyperplasia (clinical entity spanning PHPT-associated multigland disease; CKD-related secondary hyperplasia; autonomous tertiary disease) (jha2023molecularandclinical pages 8-9, vetter2024whatisthe pages 1-3, costea2025tertiaryhyperparathyroidismin pages 4-6)  
**Category:** Complex (etiologies include sporadic, hereditary, and CKD-driven mineral-bone disorder) (jha2023molecularandclinical pages 8-9, vetter2024whatisthe pages 1-3)

### MONDO / ontology note
A specific MONDO identifier for the standalone label “parathyroid hyperplasia” was not retrieved in the current full-text corpus. However, MONDO identifiers are available for closely related entities used in practice (e.g., *hereditary hyperparathyroidism* **MONDO_0016166**) via Open Targets (OpenTargets Search: Hyperparathyroidism,Secondary hyperparathyroidism,Primary hyperparathyroidism-CASR,PTH,GCM2,MEN1,CDC73,RET). This report therefore uses ontology annotations at the phenotype/mechanism/action level (HPO/GO/UBERON/MAXO) plus gene/syndrome identifiers for hereditary forms.

---

## 1. Disease information
### 1.1 Concise overview (current clinical understanding)
“Parathyroid hyperplasia” refers to enlargement/proliferation of parathyroid tissue and is used in different ways depending on clinical context:  
* **Primary hyperparathyroidism (PHPT) context:** multigland involvement historically called “hyperplasia,” now often termed **multiglandular parathyroid disease (MGD)** in WHO 2022 terminology; clinically defined by **>1 abnormal gland** rather than a histologic gold standard (jha2023molecularandclinical pages 8-9, chakrabarty2024imagingrecommendationsfor pages 3-5).  
* **Secondary hyperparathyroidism (SHPT) context:** CKD-driven compensatory hyperplasia due to chronic disturbances in phosphate/calcitriol/calcium homeostasis (vetter2024whatisthe pages 1-3, hiramitsu2023treatmentforsecondary pages 1-2).  
* **Tertiary hyperparathyroidism (tHPT) context:** autonomous hyperparathyroidism after prolonged SHPT (often post-transplant), typically multiglandular (vetter2024whatisthe pages 10-12, costea2025tertiaryhyperparathyroidismin pages 4-6).

Direct abstract-supported statement (PHPT): a 2024 review summarizes causes/relative proportions and states that in PHPT, solitary adenoma is ~80–85% and multiglandular disease is ~10–15% (chakrabarty2024imagingrecommendationsfor pages 1-2).

### 1.2 Key identifiers (retrieved in corpus)
* **MONDO (related):** hereditary hyperparathyroidism **MONDO_0016166** (Open Targets) (OpenTargets Search: Hyperparathyroidism,Secondary hyperparathyroidism,Primary hyperparathyroidism-CASR,PTH,GCM2,MEN1,CDC73,RET).  
* **ClinicalTrials.gov:** NCT03027557 (DENOCINA trial in PHPT) (NCT03027557 chunk 1, NCT03027557 chunk 3); NCT01421407 (HIFU for SHPT; withdrawn, 0 enrollment) (NCT01421407 chunk 1).

*Not retrievable from the current corpus:* ICD-10/ICD-11 codes, MeSH IDs, and Orphanet IDs specifically for “parathyroid hyperplasia.”

### 1.3 Synonyms / alternative names
* **Multiglandular parathyroid disease (MGD)** (preferred term in PHPT setting per WHO 2022 updates) (chakrabarty2024imagingrecommendationsfor pages 3-5).  
* “Four-gland hyperplasia,” “diffuse hyperplasia” (common in surgical series/management discussions) (pavlidis2023updateonthe pages 1-2).  
* Renal/CKD-associated “parathyroid hyperplasia” in SHPT (vetter2024whatisthe pages 1-3, hiramitsu2023treatmentforsecondary pages 1-2).

### 1.4 Evidence source types represented here
* Aggregated disease-level resources: major reviews and systematic reviews (Endocrine Reviews 2023; genetics review 2024; imaging review 2024; MRI systematic review 2023) (jha2023molecularandclinical pages 7-8, english2024geneticsofhereditary pages 8-9, chakrabarty2024imagingrecommendationsfor pages 1-2, scheepers2023diagnosticperformanceof pages 13-14).  
* Human clinical cohorts: atypical parathyroid adenoma/carcinoma comparative cohort with complication frequencies (Frontiers Endocrinology 2023) (chen2023clinicalandgenetic pages 1-2, chen2023clinicalandgenetic pages 6-8).  
* Clinical trials registry records: NCT03027557; NCT01421407 (NCT03027557 chunk 1, NCT01421407 chunk 1).  
* Human molecular profiling: transcriptome/miRNA/lncRNA profiling of sporadic parathyroid adenomas (2024) (verdelli2024heterogeneoustranscriptionallandscapes pages 1-2).

---

## 2. Etiology
### 2.1 Disease causal factors
#### A) PHPT-associated multigland disease (“primary hyperplasia” / MGD)
PHPT is defined as inappropriate excess PTH relative to calcium due to intrinsic parathyroid pathology; etiologies include **single adenoma, MGD (hyperplasia/double adenomas), and carcinoma** (jha2023molecularandclinical pages 8-9, chakrabarty2024imagingrecommendationsfor pages 1-2). In PHPT, MGD is enriched in hereditary cases (jha2023molecularandclinical pages 8-9, jha2023molecularandclinical pages 1-2).

#### B) CKD-related SHPT (“secondary hyperplasia”)
Secondary hyperparathyroidism in CKD arises from disturbed mineral metabolism: early CKD features increased FGF-23 with reduced activated vitamin D; progressive CKD yields hyperphosphatemia, reduced activated vitamin D, hypocalcemia, and **compensatory parathyroid hyperplasia** (hiramitsu2023treatmentforsecondary pages 1-2). A 2024 surgical review explicitly links chronic hypocalcemia, hyperphosphatemia, and low calcitriol to parathyroid hyperplasia (vetter2024whatisthe pages 1-3).

#### C) Autonomous tertiary hyperparathyroidism (tHPT)
A 2024 review describes the mechanistic progression: prolonged SHPT stimulation can cause nodular remodeling, reduced calcium-sensing/vitamin-D receptor sensitivity, and autonomy; this is the conceptual basis for tertiary HPT, often after kidney transplantation (vetter2024whatisthe pages 1-3). A narrative review defines tertiary HPT as “autonomous parathyroid gland function, hypercalcemia, and progressive enlargement of all four parathyroid glands” (costea2025tertiaryhyperparathyroidismin pages 4-6).

### 2.2 Risk factors
#### Genetic (hereditary PHPT / multigland disease)
Hereditary forms are clinically important because they are often multiglandular and change operative strategy and family management. Direct abstract-supported statement: “Approximately 15% of patients with PHPT have an underlying heritable form” (jha2023molecularandclinical pages 1-2). A 2024 review states hereditary forms account for **>10%** of PHPT and provides penetrance estimates for syndromes (english2024geneticsofhereditary pages 1-2).

Key hereditary genes/syndromes include **MEN1, CDC73 (HPT-JT), RET (MEN2A), CDKN1B (MEN4), CASR/GNA11/AP2S1 (FHH1–3 differential), and GCM2 (FIHP)** (jha2023molecularandclinical pages 15-16, jha2023molecularandclinical pages 23-24, english2024geneticsofhereditary pages 1-2). In one selected high-risk cohort, germline variants were identified in **28.2% (11/39)**, comprising **MEN1 (17.9%)** and **CDC73 (10.2%)** (preprint; interpret cautiously) (qadir2024moleculargeneticsin pages 1-3).

#### Environmental/iatrogenic and clinical risk factors
* In PHPT, causes may include sporadic disease and associations such as prior radiation exposure or sarcoidosis in some settings (review-level statements) (chakrabarty2024imagingrecommendationsfor pages 1-2).  
* For persistence/recurrence after PHPT surgery (a practical “risk factor” for adverse outcome), multigland hyperplasia/double adenomas carry higher risk (pavlidis2023updateonthe pages 1-2).

### 2.3 Protective factors
The retrieved corpus does not provide validated “protective factors” (genetic or environmental) that reduce risk of developing parathyroid hyperplasia. However, **appropriate CKD-mineral bone disorder management** (phosphate control, vitamin D correction) is mechanistically protective against SHPT progression (vetter2024whatisthe pages 1-3, hiramitsu2023treatmentforsecondary pages 1-2).

### 2.4 Gene–environment interactions
Direct gene–environment interaction studies specific to “parathyroid hyperplasia” were not retrieved in the current corpus. Clinically, gene-driven multigland PHPT (e.g., MEN1) and environment/organ-disease-driven SHPT (CKD) represent distinct but sometimes overlapping pathways to gland enlargement (english2024geneticsofhereditary pages 1-2, vetter2024whatisthe pages 1-3).

---

## 3. Phenotypes
Major phenotypes and suggested HPO mappings are summarized in the phenotype table below.

| Phenotype | Suggested HPO term(s) | Frequency / data from sources | Key citations |
|---|---|---|---|
| Hypercalcemia / hypercalcemic crisis | Hypercalcemia [HP:0003072]; Hypercalcemic crisis [HP:0100742] | PHPT is biochemically defined by elevated calcium with unsuppressed/inappropriately normal PTH; in atypical parathyroid adenoma, hypercalcemic crisis occurred in 22.8% overall; subgroup data: 0% and 39.1% in APA, 50.0% and 61.9% in parathyroid carcinoma cohorts (chen2023clinicalandgenetic pages 1-2, chen2023clinicalandgenetic pages 6-8, english2024geneticsofhereditary pages 1-2) | (chen2023clinicalandgenetic pages 1-2, chen2023clinicalandgenetic pages 6-8, english2024geneticsofhereditary pages 1-2) |
| Elevated parathyroid hormone | Increased circulating parathyroid hormone level [HP:0032369] | Severe SHPT (intact PTH >300 pg/mL) occurs in ~33% of CKD-related SHPT cases; in APA median serum PTH was 593.0 pg/mL; recurrence risk after surgery rises when 6-month PTH is ≥80 pg/mL (hiramitsu2023treatmentforsecondary pages 1-2, chen2023clinicalandgenetic pages 1-2, pavlidis2023updateonthe pages 1-2) | (hiramitsu2023treatmentforsecondary pages 1-2, chen2023clinicalandgenetic pages 1-2, pavlidis2023updateonthe pages 1-2) |
| Nephrolithiasis / renal calcification | Nephrolithiasis [HP:0000787]; Nephrocalcinosis [HP:0000129] | Urolithiasis was more frequent in APA than benign lesions (57.0% vs 29.6%); nephrolithiasis/renal calcification occurred in 87.5% and 43.5% of APA subgroups and 88.2% and 71.4% of carcinoma subgroups; PHPT is broadly associated with kidney stones and CKD (chen2023clinicalandgenetic pages 1-2, chen2023clinicalandgenetic pages 6-8, jha2023molecularandclinical pages 1-2) | (chen2023clinicalandgenetic pages 1-2, chen2023clinicalandgenetic pages 6-8, jha2023molecularandclinical pages 1-2) |
| Chronic kidney disease / renal failure | Chronic kidney disease [HP:0012622]; Renal insufficiency [HP:0000083] | CKD is a recognized morbidity of PHPT; in parathyroid carcinoma literature renal involvement including stones and renal failure occurred in 37.2% (347/932) across 27 studies; CKD also drives secondary hyperplasia/SHPT (jha2023molecularandclinical pages 7-8, roser2023diagnosisandmanagement pages 3-5, vetter2024whatisthe pages 1-3) | (jha2023molecularandclinical pages 7-8, roser2023diagnosisandmanagement pages 3-5, vetter2024whatisthe pages 1-3) |
| Bone involvement / renal osteodystrophy | Abnormality of the skeleton [HP:0000924]; Renal osteodystrophy [HP:0003338] | Bone involvement in APA was 35.4% vs 62.0% in parathyroid carcinoma; subgroup data showed bone involvement in 33.3% and 39.1% of APA and 58.8% and 71.4% of carcinoma cases; SHPT causes osteodystrophy and fractures (chen2023clinicalandgenetic pages 1-2, chen2023clinicalandgenetic pages 6-8, hiramitsu2023treatmentforsecondary pages 1-2) | (chen2023clinicalandgenetic pages 1-2, chen2023clinicalandgenetic pages 6-8, hiramitsu2023treatmentforsecondary pages 1-2) |
| Fragility fractures / fractures | Pathologic fracture [HP:0002659]; Increased susceptibility to fractures [HP:0002757] | Fragility fractures were reported in 33.3% and 17.4% of APA subgroups and 31.3% and 28.6% of carcinoma subgroups; PHPT is associated with fractures, and parathyroidectomy reduced overall fracture risk by 15% in a later meta-analysis summarized in retrieved literature (primary source data here from 2023 cohorts/reviews) (chen2023clinicalandgenetic pages 6-8, jha2023molecularandclinical pages 1-2) | (chen2023clinicalandgenetic pages 6-8, jha2023molecularandclinical pages 1-2) |
| Osteoporosis / cortical bone loss / osteopenia | Osteoporosis [HP:0000939]; Osteopenia [HP:0000938]; Decreased bone mineral density [HP:0004349] | Bone involvement in hyperparathyroid disease commonly includes osteoporosis/osteopenia; carcinoma review reported bone manifestations in 45.8% overall and noted preferential cortical loss (e.g., distal one-third radius BMD reduction) (roser2023diagnosisandmanagement pages 3-5, roser2023diagnosisandmanagement pages 7-8) | (roser2023diagnosisandmanagement pages 3-5, roser2023diagnosisandmanagement pages 7-8) |
| Bone and muscle pain / weakness | Bone pain [HP:0002653]; Muscular hypotonia [HP:0001252] / Muscle weakness [HP:0001324] | In parathyroid carcinoma review, bone plus muscle pain/weakness formed part of the 45.8% overall bone-manifestation category; these symptoms are also highlighted among common presentations of hyperparathyroid disease (roser2023diagnosisandmanagement pages 3-5) | (roser2023diagnosisandmanagement pages 3-5) |
| Gastrointestinal symptoms | Abdominal pain [HP:0002027]; Nausea [HP:0002018]; Vomiting [HP:0002013] | Gastrointestinal symptoms occurred in 17.7% of APA vs 41.8% of parathyroid carcinoma; GI complications were also more common in tertiary HPT hemodialysis cohorts in later literature (chen2023clinicalandgenetic pages 1-2) | (chen2023clinicalandgenetic pages 1-2) |
| Neuropsychiatric symptoms / fatigue | Neuropsychiatric abnormality [HP:0011446]; Fatigue [HP:0012378] | In carcinoma literature, fatigue occurred in 13.6% (127 patients), and neuropsychiatric symptoms were also commonly reported; PHPT can present with nonspecific symptoms that delay diagnosis (roser2023diagnosisandmanagement pages 3-5, jha2023molecularandclinical pages 1-2) | (roser2023diagnosisandmanagement pages 3-5, jha2023molecularandclinical pages 1-2) |
| Multiglandular disease / four-gland hyperplasia | Multiple endocrine gland hyperplasia [HP:0006779] | Multigland disease accounts for about 10–15% of PHPT; in tertiary HPT, ~90% had multiglandular disease, with only 10% single-gland disease and 30% two-gland involvement reported in one 2024 review (chakrabarty2024imagingrecommendationsfor pages 1-2, pavlidis2023updateonthe pages 1-2, vetter2024whatisthe pages 10-12) | (chakrabarty2024imagingrecommendationsfor pages 1-2, pavlidis2023updateonthe pages 1-2, vetter2024whatisthe pages 10-12) |
| Hypocalciuria in familial hypocalciuric hypercalcemia differential | Hypocalciuria [HP:0012023] | Important differential phenotype rather than direct complication: most FHH patients have UCCR <0.01; about 80–95% of FHH cases show calcium/creatinine clearance ratio <0.01, helping distinguish FHH from PHPT/hyperplasia (english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 23-24) | (english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 23-24) |


*Table: This table maps major clinical and laboratory phenotypes relevant to parathyroid hyperplasia and hyperparathyroidism to suggested HPO terms, with recent quantitative data where available. It is useful for structuring phenotype annotations in a disease knowledge base.*

### 3.1 Clinical phenotype highlights with recent quantitative data
* **Bone involvement** is common in hyperparathyroid states. In a 2023 cohort comparing atypical parathyroid adenoma (APA) vs carcinoma, bone involvement was **35.4% in APA vs 62.0% in carcinoma** (chen2023clinicalandgenetic pages 1-2).  
* **Renal calcification/nephrolithiasis** is frequent: urolithiasis was **57.0% in APA vs 29.6% in benign lesions** (chen2023clinicalandgenetic pages 1-2), and nephrolithiasis/renal calcification frequencies were reported up to 87.5% in one APA subgroup (chen2023clinicalandgenetic pages 6-8).  
* **Systemic symptoms / fatigue** are reported in advanced hyperparathyroid disease: fatigue frequency **13.6%** in a carcinoma systematic review subset (roser2023diagnosisandmanagement pages 3-5).

### 3.2 Quality-of-life impact
A 2023 SHPT surgical review states parathyroidectomy is associated with improved quality of life (alongside improved bone density, fracture risk, and survival) (hiramitsu2023treatmentforsecondary pages 1-2). Quantitative QoL instrument scores (e.g., SF-36/EQ-5D) were not present in the retrieved corpus.

---

## 4. Genetic / molecular information
### 4.1 Causal genes (human hereditary PHPT and differential diagnoses)
Key hereditary genes are summarized here and in the genetics table:

| Gene | Syndrome / phenotype | Inheritance | Typical parathyroid pattern | Key statistics / notes | Key citations |
|---|---|---|---|---|---|
| **MEN1** | Multiple endocrine neoplasia type 1 (syndromic hereditary PHPT) | Autosomal dominant | Typically **multifocal/multiglandular disease**; often described clinically as hyperplasia/MGD rather than single adenoma | Most common syndromic cause of hereditary PHPT; hereditary PHPT accounts for ~10% to >10% of PHPT overall; MEN1 penetrance for PHPT reported ~90% by age 70; somatic **MEN1** alterations also occur in sporadic tumors (~12–35% in reviews) (english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, simonds2020clinicalandmolecular pages 3-4) | PMID **36778668** cited via Open Targets; review DOI: 10.1210/endrev/bnad009 (OpenTargets Search: Hyperparathyroidism,Secondary hyperparathyroidism,Primary hyperparathyroidism-CASR,PTH,GCM2,MEN1,CDC73,RET, english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, simonds2020clinicalandmolecular pages 3-4) |
| **CDC73** | Hyperparathyroidism-jaw tumor syndrome (HPT-JT); also familial isolated PHPT and parathyroid carcinoma predisposition | Autosomal dominant | Can present with multigland disease, but especially important for **carcinoma-risk PHPT**; not limited to diffuse hyperplasia | HPT-JT has incomplete penetrance; reported parathyroid carcinoma risk ~20–25%; in a selected high-risk Indian cohort, 4/39 (10.2%) had **CDC73** variants; germline **CDC73** was the commonest abnormality in atypical parathyroid adenoma and carcinoma cohorts in one study (qadir2024moleculargeneticsin pages 1-3, jha2023molecularandclinical pages 15-16, simonds2020clinicalandmolecular pages 4-6) | Review DOI: 10.1210/endrev/bnad009; cohort DOI: 10.21203/rs.3.rs-5299691/v1 (qadir2024moleculargeneticsin pages 1-3, jha2023molecularandclinical pages 15-16, simonds2020clinicalandmolecular pages 4-6) |
| **RET** | Multiple endocrine neoplasia type 2A (MEN2A) | Autosomal dominant | Usually **not the dominant parathyroid presentation**; may cause parathyroid tumors/hyperplasia, often with medullary thyroid carcinoma and pheochromocytoma | Lower penetrance than MEN1; English et al. report MEN2 PHPT ~5–15%; large MEN2A cohort (1085 patients) had only 10 patients initially presenting with PHPT, suggesting low yield of RET testing in isolated PHPT (english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 15-16) | Review DOI: 10.1007/s42000-023-00508-9; review DOI: 10.1210/endrev/bnad009 (english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 15-16) |
| **CDKN1B** | MEN4 (MEN1-like syndrome) | Autosomal dominant | Often **multiglandular / MEN1-like hereditary PHPT** rather than isolated single-gland disease | MEN4 is rarer than MEN1; penetrance for PHPT reported ~75% in review summaries; included on hereditary PHPT testing panels because results affect surgical planning and family testing (english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, simonds2020clinicalandmolecular pages 4-6) | Review DOI: 10.1007/s42000-023-00508-9; ClinVar/Open Targets evidence noted for CDKN1B (OpenTargets Search: Hyperparathyroidism,Secondary hyperparathyroidism,Primary hyperparathyroidism-CASR,PTH,GCM2,MEN1,CDC73,RET, english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, simonds2020clinicalandmolecular pages 4-6) |
| **CASR** | Familial hypocalciuric hypercalcemia type 1 (FHH1); related neonatal severe hyperparathyroidism when biallelic severe loss-of-function | Autosomal dominant for FHH1; biallelic severe forms for NSHPT | Usually **not classic hyperplastic PHPT**; causes lifelong mild hypercalcemia with inappropriately normal/high PTH and can mimic PHPT; important differential diagnosis to avoid unnecessary PTX | FHH prevalence ~1.3 per 100,000 and accounts for about 2% of apparent PHPT; UCCR <0.01 typical in ~80–95% of FHH; CASR is among the most frequently positive genes in hereditary PHPT testing cohorts (11/19 positives in one UK series were CASR) (english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 23-24) | PMIDs in Open Targets include **15572418**, **27434672**; review DOI: 10.1007/s42000-023-00508-9 (OpenTargets Search: Hyperparathyroidism,Secondary hyperparathyroidism,Primary hyperparathyroidism-CASR,PTH,GCM2,MEN1,CDC73,RET, english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 23-24) |
| **GNA11** | Familial hypocalciuric hypercalcemia type 2 (FHH2) | Autosomal dominant | Usually **FHH phenotype rather than true multigland hyperplasia** | Included in hereditary hypercalcemia/PHPT differential; like CASR-related FHH, tends to show hypocalciuria and generally benign course rather than surgically correctable hyperplasia (english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 15-16, jha2023molecularandclinical pages 23-24) | Review DOI: 10.1210/endrev/bnad009; review DOI: 10.1007/s42000-023-00508-9 (english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 15-16, jha2023molecularandclinical pages 23-24) |
| **AP2S1** | Familial hypocalciuric hypercalcemia type 3 (FHH3) | Autosomal dominant | Usually **FHH mimic**, not classic multigland hyperplasia | Nearly all pathogenic variants affect **Arg15** in reported series; in a UK hereditary PHPT testing cohort, 1/19 pathogenic findings was **AP2S1**; clinically relevant because parathyroidectomy usually does not correct FHH (english2024geneticsofhereditary pages 8-9, jha2023molecularandclinical pages 23-24) | Review DOI: 10.1007/s42000-023-00508-9; review DOI: 10.1210/endrev/bnad009 (english2024geneticsofhereditary pages 8-9, jha2023molecularandclinical pages 23-24) |
| **GCM2** | Familial isolated hyperparathyroidism (FIHP); activating variants also linked to hereditary PHPT | Usually autosomal dominant with variable/low penetrance | Can be associated with **multigland disease / familial hyperplasia-like PHPT**, but penetrance is variable and many families remain unexplained | Activating **GCM2** variants reported in ~18% of FIHP in some series; among FIHP kindreds pre-screened negative for MEN1/CASR/CDC73, only ~10–20% carry **GCM2** variants, leaving ~80–90% unexplained; low penetrance has raised questions about routine panel inclusion in all settings (jha2023molecularandclinical pages 23-24, qadir2024moleculargeneticsin pages 9-11) | PMIDs in Open Targets include **27745835**, **39024449**, **36653562** (OpenTargets Search: Hyperparathyroidism,Secondary hyperparathyroidism,Primary hyperparathyroidism-CASR,PTH,GCM2,MEN1,CDC73,RET, jha2023molecularandclinical pages 23-24, qadir2024moleculargeneticsin pages 9-11) |


*Table: This table summarizes the main hereditary genes linked to parathyroid hyperplasia, multiglandular disease, or closely related hereditary PHPT phenotypes. It highlights inheritance, the usual parathyroid pattern, and key statistics that help distinguish true multigland disease from mimics such as familial hypocalciuric hypercalcemia.*

Notable gene-level points (selected):
* **MEN1** is the most common syndromic cause of hereditary PHPT; sporadic tumors also frequently show somatic MEN1 alterations (review summaries) (english2024geneticsofhereditary pages 1-2, simonds2020clinicalandmolecular pages 3-4).  
* **CDC73 (HPT-JT)** confers clinically important carcinoma risk (reported ~20–25% in a 2023 review summary) and needs long-term surveillance approaches in carriers (jha2023molecularandclinical pages 15-16, simonds2020clinicalandmolecular pages 4-6).  
* **CASR/GNA11/AP2S1** mutations cause familial hypocalciuric hypercalcemia (FHH), which mimics PHPT but is usually not corrected by parathyroidectomy (jha2023molecularandclinical pages 15-16, jha2023molecularandclinical pages 23-24).

### 4.2 Pathogenic variants / variant types
The retrieved corpus did not provide a comprehensive ClinVar-style variant catalog for parathyroid hyperplasia. However, one 2024 cohort report lists multiple MEN1 and CDC73 variants detected by NGS panel in a selected high-risk set (qadir2024moleculargeneticsin pages 1-3). For knowledge base entry, variant-level data should be completed by targeted ClinVar/HGMD extraction.

### 4.3 Epigenetics and regulatory mechanisms
A 2023 Endocrine Reviews synthesis notes that reduced **CASR** expression is common in sporadic PHPT tumors and may be driven by **epigenetic deregulation** (hypermethylation and histone modifications) and altered upstream regulators (jha2023molecularandclinical pages 11-12). The same review highlights broad epigenetic alterations and noncoding RNA regulation as potentially reversible contributors (jha2023molecularandclinical pages 11-12).

### 4.4 Recent omics: 2024 transcriptome/lncRNA profiling
A 2024 study profiled 32 sporadic parathyroid adenomas with gene, microRNA, and lncRNA expression, clustering tumors by a MEN1/CDC73/GCM2/CASR/VDR/CCND1/CDKN1B gene set; CDC73 and CDKN1B expression drove clustering, and distinct lncRNA patterns were associated with biochemical severity differences (verdelli2024heterogeneoustranscriptionallandscapes pages 1-2, verdelli2024heterogeneoustranscriptionallandscapes pages 7-9). This provides a current example of molecular heterogeneity relevant to understanding why some tumors behave more “quiescent” vs “severe” clinically (verdelli2024heterogeneoustranscriptionallandscapes pages 7-9).

---

## 5. Environmental information
The dominant “environmental” drivers in the retrieved corpus are **organ-disease mediated** exposures, especially CKD-related mineral and endocrine disturbance:
* CKD-related drivers: hyperphosphatemia, calcitriol deficiency, hypocalcemia, elevated FGF23, and related inflammatory/oxidative mechanisms contribute to hyperplasia and SHPT progression (hiramitsu2023treatmentforsecondary pages 1-2, costea2025tertiaryhyperparathyroidismin pages 2-4).  
* No infectious triggers were identified in the retrieved corpus.

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (representative)
#### SHPT (CKD) → hyperplasia → autonomy (tHPT)
1. CKD causes phosphate retention, increased FGF23, reduced activated vitamin D, and hypocalcemia (hiramitsu2023treatmentforsecondary pages 1-2).  
2. Chronic hypocalcemia/hyperphosphatemia/low calcitriol stimulate parathyroid gland growth → diffuse hyperplasia (vetter2024whatisthe pages 1-3).  
3. Over time, nodular remodeling and decreased VDR/CaSR sensitivity emerge; somatic changes may shift to monoclonal proliferation, contributing to autonomy and refractoriness (tHPT) (vetter2024whatisthe pages 1-3).  
4. tHPT manifests as persistent high PTH with hypercalcemia and multigland enlargement, often requiring surgical management (costea2025tertiaryhyperparathyroidismin pages 4-6, vetter2024whatisthe pages 10-12).

#### PHPT multigland disease (MGD)
PHPT MGD reflects intrinsic multi-gland pathology (often genetic susceptibility-driven) and is described clinically by multiple abnormal glands; WHO 2022 favors MGD terminology and notes limited histologic discriminability between adenoma vs hyperplasia in practice (jha2023molecularandclinical pages 8-9, chakrabarty2024imagingrecommendationsfor pages 3-5).

### 6.2 Key molecular pathways and processes
* **Calcium sensing / CaSR signaling:** CaSR is central to chief-cell sensing of ionized calcium and PTH regulation; reviews note that many sporadic tumors show reduced CASR expression and that Casr loss models cause severe hyperparathyroidism (simonds2020clinicalandmolecular pages 1-3, jha2023molecularandclinical pages 11-12).  
* **Vitamin D receptor (VDR) signaling:** SHPT progression involves decreased VDR expression in nodular hyperplasia; VDRAs are core therapies (hiramitsu2023treatmentforsecondary pages 1-2, sevva2024pharmaceuticalmanagementof pages 2-3).  
* **Tumor suppressor pathways:** MEN1/CDC73 biology shapes hereditary and sporadic tumorigenesis and is a key part of modern molecular classification (jha2023molecularandclinical pages 10-11, verdelli2024heterogeneoustranscriptionallandscapes pages 1-2).  
* **Epigenetic and noncoding RNA regulation:** DNA methylation/histone modification and miRNA/lncRNA changes (e.g., C19MC, NEAT1, HOXA-AS RNAs) are implicated in heterogeneity and tumor biology (jha2023molecularandclinical pages 11-12, verdelli2024heterogeneoustranscriptionallandscapes pages 7-9).

### 6.3 Suggested ontology terms
* **GO biological processes (examples):** regulation of hormone secretion; calcium ion homeostasis; regulation of cell population proliferation; epigenetic regulation of gene expression (supported mechanistically by CaSR/VDR signaling and epigenetic findings) (jha2023molecularandclinical pages 11-12, verdelli2024heterogeneoustranscriptionallandscapes pages 7-9).  
* **Cell Ontology (CL) (examples):** parathyroid chief cell (primary endocrine cell type producing PTH; referenced mechanistically in PHPT) (simonds2020clinicalandmolecular pages 1-3).  
* **CHEBI examples:** calcium(2+) and phosphate as key ions driving biochemical phenotype (implied by CKD/PHPT mineral metabolism discussions) (hiramitsu2023treatmentforsecondary pages 1-2, vetter2024whatisthe pages 1-3).

---

## 7. Anatomical structures affected
### 7.1 Primary organ
* **Parathyroid gland** (UBERON:0001132) — diffuse hyperplasia or multigland neoplasia (PHPT-MGD, SHPT, tHPT) (vetter2024whatisthe pages 1-3, jha2023molecularandclinical pages 8-9).

### 7.2 Major secondary organ systems (complications)
* **Skeletal system / bone** (e.g., cortical bone loss, fractures, renal osteodystrophy): frequent and clinically significant (jha2023molecularandclinical pages 7-8, chen2023clinicalandgenetic pages 1-2).  
* **Kidney / urinary tract** (nephrolithiasis, nephrocalcinosis, renal failure/CKD): frequent and clinically significant (jha2023molecularandclinical pages 7-8, roser2023diagnosisandmanagement pages 3-5).  
* **Cardiovascular system** (particularly in CKD-related SHPT/tHPT; broader morbidity links): noted in SHPT/tHPT overviews (vetter2024whatisthe pages 1-3, hiramitsu2023treatmentforsecondary pages 1-2).

### 7.3 Subcellular/localization (mechanistic)
* **Plasma membrane**: CaSR localization is central to extracellular calcium sensing (simonds2020clinicalandmolecular pages 1-3).  
* **Nucleus/chromatin**: epigenetic regulation (histone marks H3K4/H3K27) implicated via lncRNA–histone interactions and menin/parafibromin biology (verdelli2024heterogeneoustranscriptionallandscapes pages 7-9, verdelli2024heterogeneoustranscriptionallandscapes pages 1-2).

---

## 8. Temporal development
* **PHPT MGD** may present earlier in hereditary disease compared with sporadic single-adenoma disease; genetic testing is recommended in young onset (≤40), recurrent disease, or multigland disease (jha2023molecularandclinical pages 1-2).  
* **SHPT** typically evolves with CKD progression and can advance to nodular hyperplasia (hiramitsu2023treatmentforsecondary pages 1-2).  
* **tHPT** occurs after prolonged SHPT; persistent post-transplant hyperparathyroidism remains common, with reported rates declining from ~70% at 1 year to ~43% at 2 years after transplantation in cited series (vetter2024whatisthe pages 1-3).

---

## 9. Inheritance and population
### 9.1 Epidemiology (PHPT as the major primary context)
A 2023 Endocrine Reviews article provides sex-stratified incidence estimates for PHPT: **~66 per 100,000 person-years in women** and **~25 per 100,000 in men** (jha2023molecularandclinical pages 7-8). It also reports that PHPT is associated with fractures, kidney stones, CKD, and increased mortality (jha2023molecularandclinical pages 7-8).

### 9.2 Heritable fraction and penetrance
* Heritable PHPT fraction: “Approximately 15%” in one 2023 synthesis (jha2023molecularandclinical pages 1-2).  
* Penetrance examples from a 2024 genetics review: MEN1 PHPT ~90% by age 70; MEN2 ~5–15%; MEN4 ~75%; HPT-JT ~95% (review summary table) (english2024geneticsofhereditary pages 1-2).

---

## 10. Diagnostics
### 10.1 Diagnostic workup summary (labs + imaging)

| Workup component | What to measure/use | Key findings or performance statistics | Notes specific to multigland disease / secondary HPT | Key citations |
|---|---|---|---|---|
| Biochemical diagnosis | Serum total calcium, ionized calcium, intact PTH | PHPT is diagnosed by hypercalcemia with elevated or inappropriately normal PTH; one cohort used serum Ca >2.70 mmol/L and/or ionized Ca >1.28 mmol/L with unsuppressed PTH as diagnostic thresholds | Biochemistry alone cannot reliably distinguish adenoma from hyperplasia/MGD; markedly high calcium and PTH may raise concern for carcinoma rather than benign MGD | (chakrabarty2024imagingrecommendationsfor pages 1-2, chen2023clinicalandgenetic pages 1-2, english2024geneticsofhereditary pages 1-2) |
| Mineral metabolism panel | Serum phosphate, 25-OH vitamin D, renal function | In CKD-related SHPT, progressive hyperphosphatemia and reduced active vitamin D drive hypocalcemia and compensatory parathyroid hyperplasia; vitamin D status is important for surgical outcomes and recurrence risk | Particularly important in SHPT/tHPT to separate CKD-mineral bone disorder from primary disease and to optimize pre-/post-operative management | (pavlidis2023updateonthe pages 1-2, vetter2024whatisthe pages 1-3, hiramitsu2023treatmentforsecondary pages 1-2) |
| Urinary calcium assessment | Urinary calcium-to-creatinine clearance ratio (UCCR/UCCR) | Majority of FHH patients have UCCR <0.01; FHH accounts for about 2% of patients initially considered to have PHPT in some series | Essential when apparent PHPT presents with mild hypercalcemia or familial disease; helps avoid unnecessary parathyroidectomy in FHH | (english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 23-24) |
| Neck ultrasound | First-line anatomic localization | Widely used first-line tool; pooled sensitivity for US in prior meta-analysis about 80% for PHPT localization | Lower sensitivity in MGD and renal hyperplasia; in renal HPT/hyperplastic glands, sonography sensitivity reported around 62% | (scheepers2023diagnosticperformanceof pages 13-14, vetter2024whatisthe pages 10-12, chakrabarty2024imagingrecommendationsfor media a62b0df1) |
| Sestamibi scintigraphy / SPECT/CT | Functional localization with 99mTc-sestamibi, often with SPECT/CT | Prior meta-analysis pooled sensitivity about 83% for MIBI in PHPT localization | Performance drops in MGD: reported MIBI sensitivity about 44% for MGD; in renal HPT/hyperplastic glands scintigraphy sensitivity around 55% | (scheepers2023diagnosticperformanceof pages 13-14, scheepers2023diagnosticperformanceof pages 14-15, vetter2024whatisthe pages 10-12) |
| 4DCT | Multiphasic CT for localization and MGD prediction | One meta-analysis cited sensitivity 81.0% for 4DCT vs 65.0% for MIBI; MGD sensitivity reported about 60%; 4DCT MGD prediction scores: composite score specificity 72% (>=4), 86% (>=5), 100% (=6), CT-only score specificity 74% (>=3) and 88% (>=4) | Helpful when first-line imaging is negative or recurrent disease is suspected; exposes patients to ionizing radiation; useful for predicting MGD before surgery | (chakrabarty2024imagingrecommendationsfor pages 9-11, scheepers2023diagnosticperformanceof pages 13-14, scheepers2023diagnosticperformanceof pages 14-15) |
| MRI / 4D MRI | Radiation-free localization, dynamic contrast-enhanced protocols | Conventional MRI sensitivity 39.1%-94.3%; 4D MRI sensitivity 55.6%-100%; first-line 4D MRI often 64%-100%; reported MGD sensitivity 67%-100%; one review cited 92% for single-gland disease and 74% for MGD | Attractive in younger patients, recurrent disease, and when radiation avoidance matters; superior to conventional imaging in some reoperative/MGD settings | (chakrabarty2024imagingrecommendationsfor pages 9-11, scheepers2023diagnosticperformanceof pages 13-14, scheepers2023diagnosticperformanceof pages 9-11, scheepers2023diagnosticperformanceof pages 1-2) |
| 18F-FCH PET/CT | High-resolution functional imaging | Reported as superior to ultrasound and MIBI; accepted as an alternative first-line modality in some centers | Useful in difficult localization, persistent/recurrent disease, and MGD; increasingly used before reoperation | (chakrabarty2024imagingrecommendationsfor pages 9-11, pavlidis2023updateonthe pages 1-2, scheepers2023diagnosticperformanceof pages 2-4, chakrabarty2024imagingrecommendationsfor media a62b0df1) |
| PET/MRI | Hybrid metabolic + high-contrast soft tissue imaging | 18F-FCH PET/MRI sensitivity 84.2%-100%; specificity 96.0%-100% in reported studies; described as highest diagnostic accuracy among MRI-based approaches | Particularly useful for MGD, pediatric patients, and complex surgical planning while minimizing radiation | (scheepers2023diagnosticperformanceof pages 13-14, scheepers2023diagnosticperformanceof pages 9-11, chakrabarty2024imagingrecommendationsfor pages 9-11) |
| Intraoperative PTH monitoring | Rapid ioPTH during parathyroidectomy | In PHPT/reoperative disease, PTH <=40 pg/mL or >=50% drop from baseline minimizes persistence risk; Miami criterion (>50% drop at >=10 min) is used in tertiary/renal HPT surgery literature | In SHPT, formal ioPTH criteria are less established because all hyperplastic glands must be removed; nevertheless, intraoperative monitoring may support completeness of resection | (pavlidis2023updateonthe pages 1-2, costea2025tertiaryhyperparathyroidismin pages 10-12, hiramitsu2023treatmentforsecondary pages 1-2) |
| Postoperative surveillance | Serum calcium and PTH follow-up | Six-month calcium >=9.8 mg/dL and PTH >=80 pg/mL indicate higher recurrence risk after PHPT surgery | Four-gland hyperplasia/double adenomas have higher persistence/recurrence risk, so long-term follow-up is especially important | (pavlidis2023updateonthe pages 1-2) |
| Strategy for MGD / renal hyperplasia | Bilateral neck exploration, selective imaging, four-gland assessment | Figure-based management algorithms recommend imaging for planning, then bilateral neck exploration with subtotal or total parathyroidectomy for MGD; in tHPT, 90% have multiglandular disease | In SHPT/tHPT, localization imaging is adjunctive; operative four-gland exploration remains the most reliable strategy because hyperplasia is often diffuse/multiglandular | (vetter2024whatisthe pages 10-12, vetter2024whatisthe pages 1-3, chakrabarty2024imagingrecommendationsfor media 9629bfff) |


*Table: This table summarizes the current diagnostic workup for parathyroid hyperplasia and related hyperparathyroid states, including key laboratory tests, localization imaging, intraoperative monitoring, and special considerations for multigland disease and CKD-related secondary/tertiary hyperparathyroidism.*

Key recent imaging developments relevant to “hyperplasia” (MGD):  
* MRI systematic review (Dec 2023): conventional MRI sensitivity 39.1–94.3%; 4D MRI 55.6–100%; PET/MRI (18F-FCH) 84.2–100% (scheepers2023diagnosticperformanceof pages 13-14, scheepers2023diagnosticperformanceof pages 9-11). In MGD specifically, reported MRI sensitivities 67–100%, versus MIBI ~44% and 4DCT ~60% in cited comparisons (scheepers2023diagnosticperformanceof pages 14-15).  
* 2024 imaging review: provides a dedicated management branch for MGD (formerly hyperplasia) recommending imaging for planning and then bilateral neck exploration with subtotal/total parathyroidectomy (algorithm figure) (chakrabarty2024imagingrecommendationsfor media a62b0df1). The same source includes a summary table of imaging modalities (advantages/limitations) (chakrabarty2024imagingrecommendationsfor media 9629bfff).

### 10.2 Key differential diagnosis: familial hypocalciuric hypercalcemia (FHH)
A 2024 genetics review recommends urinary calcium-to-creatinine clearance ratio (UCCR) testing; most FHH cases have **UCCR < 0.01**, supporting distinction from PHPT/MGD and preventing unnecessary surgery (english2024geneticsofhereditary pages 1-2).

### 10.3 Genetics in diagnosis
Genetic testing is recommended for individuals with multigland disease, recurrent PHPT, young onset, or family history (jha2023molecularandclinical pages 1-2). A 2024 genetics review similarly recommends testing when hereditary PHPT is suspected (e.g., young age, multigland/hyperplasia, carcinoma, known familial mutation) because results guide surgery and surveillance (english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2).

---

## 11. Outcome / prognosis
### 11.1 Persistence/recurrence after PHPT surgery
A 2023 surgical-management review reports recurrence after parathyroidectomy historically 4–10%, decreasing to 2.5–5% with modern advances; hyperplasia/MGD is a risk factor for persistence/recurrence (pavlidis2023updateonthe pages 1-2). It provides pragmatic thresholds: intraoperative PTH ≤40 pg/mL or ≥50% drop predicts low persistence risk; and at 6 months, calcium ≥9.8 mg/dL and PTH ≥80 pg/mL indicate recurrence risk (pavlidis2023updateonthe pages 1-2).

### 11.2 Renal/transplant outcomes in tHPT
A 2024 transplant-focused surgical review reports that (in cited retrospective comparisons) parathyroidectomy produced higher PTH normalization and lower kidney allograft loss versus cinacalcet (9% vs 33% graft failure) (vetter2024whatisthe pages 10-12).

---

## 12. Treatment

| Context | Treatment / implementation | Real-world use / indication | Key outcomes or statistics | Trial / source |
|---|---|---|---|---|
| PHPT with multigland disease (formerly “hyperplasia”; WHO 2022 favors MGD terminology) | Bilateral neck exploration (BNE) with subtotal or total parathyroidectomy | Preferred operative pathway when multigland disease is suspected/localized poorly; imaging mainly supports planning, but definitive management is surgical exploration | Figure-based algorithm recommends imaging ± parathyroid venous sampling, then BNE followed by subtotal/total parathyroidectomy for MGD; multigland disease/hyperplasia is associated with higher persistence/recurrence risk after surgery than single-gland disease (chakrabarty2024imagingrecommendationsfor media a62b0df1, pavlidis2023updateonthe pages 1-2) | Chakrabarty 2024; Pavlidis 2023 (chakrabarty2024imagingrecommendationsfor media a62b0df1, pavlidis2023updateonthe pages 1-2) |
| PHPT, persistent/recurrent disease risk management | Intraoperative PTH monitoring during parathyroidectomy | Used to reduce risk of persistence in resection for pHPT, including cases with multigland disease | Intraoperative PTH ≤ 40 pg/mL or a ≥50% drop from baseline minimized persistence risk; recurrence risk higher with double adenomas/four-gland hyperplasia; modern recurrence rates reported ~2.5–5% (pavlidis2023updateonthe pages 1-2) | Pavlidis 2023 (pavlidis2023updateonthe pages 1-2) |
| PHPT managed medically when surgery is not performed or delayed | Cinacalcet, denosumab, or combination (plus vitamin D) | Investigated for biochemical control and bone protection in primary hyperparathyroidism; not curative for multigland disease but relevant where surgery is deferred/inappropriate | DENOCINA phase 3 trial enrolled 46 patients; combined arm used denosumab 60 mg every 6 months + cinacalcet 30 mg daily + vitamin D 50 μg daily; endpoints included DXA BMD, serum calcium, PTH, bone turnover markers, nephrolithiasis/nephrocalcinosis imaging outcomes (NCT03027557 chunk 1, NCT03027557 chunk 2, NCT03027557 chunk 3) | NCT03027557 / DENOCINA (NCT03027557 chunk 1, NCT03027557 chunk 2, NCT03027557 chunk 3) |
| CKD-related secondary hyperparathyroidism (SHPT) | Phosphate control: dietary phosphate restriction and phosphate binders | First-line background management to reduce chronic parathyroid stimulation in CKD-mineral bone disorder | Standard therapy in SHPT; used alongside vitamin D analogs and calcimimetics before considering surgery (vetter2024whatisthe pages 1-3, sevva2024pharmaceuticalmanagementof pages 2-3, NCT01421407 chunk 1) | Vetter 2024; Sevva 2024; NCT01421407 background (vetter2024whatisthe pages 1-3, sevva2024pharmaceuticalmanagementof pages 2-3, NCT01421407 chunk 1) |
| CKD-related SHPT | Vitamin D receptor activators/analogs (calcitriol, alfacalcidol/alphacalcidol, doxercalciferol, paricalcitol; others in regional practice) | Common medical therapy for hypocalcemia-driven PTH excess | Recommended pharmacologic option in CKD SHPT; used with phosphate lowering and/or calcimimetics; tertiary HPT review notes they lower PTH, though vascular calcification effects remain debated (vetter2024whatisthe pages 1-3, sevva2024pharmaceuticalmanagementof pages 2-3, costea2025tertiaryhyperparathyroidismin pages 9-10) | Vetter 2024; Sevva 2024; Costea 2025 (vetter2024whatisthe pages 1-3, sevva2024pharmaceuticalmanagementof pages 2-3, costea2025tertiaryhyperparathyroidismin pages 9-10) |
| CKD-related SHPT | Calcimimetics: cinacalcet (oral) | Widely used for refractory biochemical SHPT on dialysis | Background/eligibility in HIFU trial required PTH >800 pg/mL despite ≥3 months cinacalcet >30 mg/day ± vitamin D; cinacalcet also reported to improve endothelial dysfunction/cardiac hypertrophy in hemodialysis patients in reviewed literature (NCT01421407 chunk 1, vetter2024whatisthe pages 17-18) | NCT01421407; Vetter 2024 (NCT01421407 chunk 1, vetter2024whatisthe pages 17-18) |
| CKD-related SHPT | Calcimimetics: etelcalcetide (IV during dialysis) | Real-world dialysis implementation as second-generation calcimimetic | In a 2018–2023 retrospective cohort of 52 dialysis patients, 34/52 (65.4%) received cinacalcet and etelcalcetide; 29/33 (87.9%) treated with etelcalcetide had significant PTH reduction, up to 57% from baseline; none required parathyroidectomy for refractory PTH or drug toxicity in that series (sevva2024pharmaceuticalmanagementof pages 1-2) | Sevva 2024 (sevva2024pharmaceuticalmanagementof pages 1-2) |
| CKD-related SHPT, drug-refractory disease | Parathyroidectomy (subtotal PTX, total PTX with autotransplantation, or total PTX without autotransplantation; sometimes with transcervical thymectomy) | Reserved for refractory SHPT, severe symptoms, or failure/cost issues of medical therapy | Review emphasizes PTx remains one of the most important therapies despite calcimimetics; complete removal of all glands is crucial to prevent persistence/recurrence; PTx associated with improved bone density, fracture risk, survival, and quality of life (hiramitsu2023treatmentforsecondary pages 1-2) | Hiramitsu 2023 (hiramitsu2023treatmentforsecondary pages 1-2) |
| CKD-related SHPT in transplant candidates | Subtotal PTX or total PTX with autotransplantation | Preferred when future kidney transplantation is anticipated | 2024 surgical review recommends subtotal PTX or total PTX with autotransplantation for transplant-eligible patients; total PTX can be considered for non-transplant candidates (vetter2024whatisthe pages 1-3) | Vetter 2024 (vetter2024whatisthe pages 1-3) |
| Post-transplant tertiary hyperparathyroidism (tHPT) | Subtotal parathyroidectomy with four-gland exploration | Favored surgical approach for persistent autonomous post-transplant disease, usually multiglandular | Review states 90% of tHPT patients have multigland disease; subtotal PTX is favored because it has lower hypoparathyroidism risk than total PTX with autotransplantation with similar cure rates (vetter2024whatisthe pages 10-12) | Vetter 2024 (vetter2024whatisthe pages 10-12) |
| Post-transplant tertiary hyperparathyroidism (tHPT) | Timing of parathyroidectomy before vs after transplant | Individualized based on suspected autonomy, graft considerations, and biochemical persistence | If autonomy is suspected, surgery ideally precedes transplantation; if post-transplant surgery is needed, many centers delay until ~1 year; persistent sHPT/tHPT reported to decline from 70% at 1 year to 43% at 2 years post-transplant (vetter2024whatisthe pages 1-3); a meta-analysis of 223 patients found no significant difference between pre- vs post-transplant PTX for follow-up PTH or calcium (vetter2024whatisthe pages 1-3) | Vetter 2024; Karniadakis 2025 abstracted in search results (vetter2024whatisthe pages 1-3) |
| Post-transplant tertiary hyperparathyroidism (tHPT) | Surgery vs cinacalcet | Comparative management for persistent autonomous disease after transplant | Retrospective comparison cited in 2024 review found parathyroidectomy achieved higher PTH normalization and lower graft failure than cinacalcet (9% vs 33% allograft loss) (vetter2024whatisthe pages 10-12) | Vetter 2024 (vetter2024whatisthe pages 10-12) |
| Procedural/ablative alternative for SHPT | High-intensity focused ultrasound (HIFU; TH-One device) | Investigational non-surgical ablation for uncontrolled SHPT in chronic hemodialysis with 1–2 enlarged glands on ultrasound | Randomized open-label trial planned primary endpoint of ≥30% reduction in mean serum iPTH at 6 months and secondary endpoint of achieving KDIGO-range PTH; required uncontrolled disease despite cinacalcet; study was withdrawn with actual enrollment = 0 (NCT01421407 chunk 1) | NCT01421407 (NCT01421407 chunk 1) |


*Table: This table summarizes treatment strategies and real-world implementation of therapies for parathyroid hyperplasia across primary multigland disease, CKD-related secondary hyperparathyroidism, and post-transplant tertiary hyperparathyroidism. It highlights surgical standards, medical therapies, response statistics, and relevant clinical trial identifiers.*

### 12.1 PHPT multigland disease (MGD)
* Standard approach is surgical exploration (bilateral neck exploration) and subtotal or total parathyroidectomy, consistent with modern imaging-guided algorithms (chakrabarty2024imagingrecommendationsfor media a62b0df1).  
* Intraoperative PTH monitoring criteria are used to reduce persistence risk in PHPT surgery (pavlidis2023updateonthe pages 1-2).

### 12.2 SHPT (CKD-related hyperplasia)
* **Medical therapy:** phosphate control, VDRAs, and calcimimetics (vetter2024whatisthe pages 1-3, sevva2024pharmaceuticalmanagementof pages 2-3).  
* **Real-world implementation (2018–2023 cohort):** IV etelcalcetide during dialysis reduced PTH in **29/33 (87.9%)** patients, up to **57%** reduction from baseline, with no parathyroidectomies required in that series (sevva2024pharmaceuticalmanagementof pages 1-2).  
* **Surgery:** parathyroidectomy remains key for drug-refractory disease; a 2023 review emphasizes that for SHPT, complete removal of all glands is needed to avoid persistence/recurrence and notes improved bone density, fracture risk, survival, and QoL after surgery (hiramitsu2023treatmentforsecondary pages 1-2).

### 12.3 tHPT (autonomous, often post-transplant)
A 2024 review emphasizes multigland disease (~90%) and generally favors subtotal parathyroidectomy with four-gland exploration (vetter2024whatisthe pages 10-12).

### 12.4 Experimental/procedural
* **HIFU for SHPT:** NCT01421407 planned an endpoint of ≥30% iPTH reduction at 6 months but was withdrawn with 0 enrollment (NCT01421407 chunk 1).  
* **PHPT medical therapy trial:** NCT03027557 (DENOCINA) tested denosumab and cinacalcet regimens in PHPT (NCT03027557 chunk 1, NCT03027557 chunk 3).

### 12.5 Suggested MAXO terms (examples)
* Parathyroidectomy (MAXO:0000004) (supported clinically across PHPT-MGD, SHPT, tHPT) (chakrabarty2024imagingrecommendationsfor media a62b0df1, hiramitsu2023treatmentforsecondary pages 1-2, vetter2024whatisthe pages 10-12).  
* Treatment with calcimimetic (e.g., cinacalcet/etelcalcetide) (MAXO term to be selected in downstream curation) (sevva2024pharmaceuticalmanagementof pages 1-2, sevva2024pharmaceuticalmanagementof pages 2-3).  
* Vitamin D supplementation/therapy (VDRAs) (MAXO curation candidate) (vetter2024whatisthe pages 1-3, sevva2024pharmaceuticalmanagementof pages 2-3).

---

## 13. Prevention
* **Primary/secondary prevention for SHPT progression (CKD):** dietary phosphate restriction and phosphate binders plus vitamin D/VDRAs to reduce chronic parathyroid stimulation are standard mechanistic approaches (vetter2024whatisthe pages 1-3, sevva2024pharmaceuticalmanagementof pages 2-3).  
* **Secondary prevention for hereditary PHPT/MGD:** genetic testing when indicated and cascade testing in relatives can enable earlier detection and tailored surveillance/surgical planning (english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 1-2).  
* **Postoperative secondary prevention:** vitamin D status is emphasized as a factor for good outcomes after PHPT surgery and is routinely assessed and corrected (pavlidis2023updateonthe pages 1-2).

---

## 14. Other species / natural disease
No naturally occurring non-human species datasets for “parathyroid hyperplasia” were retrieved in the current corpus.

---

## 15. Model organisms
Direct primary model-organism papers were not retrieved as full text in the current corpus; however, authoritative reviews cite several mechanistic models relevant to hyperplasia/tumorigenesis:
* Parathyroid-specific **Casr** loss → severe hyperparathyroidism (jha2023molecularandclinical pages 11-12).  
* **MEN1** loss → parathyroid hyperplasia/adenomas (verdelli2024heterogeneoustranscriptionallandscapes pages 1-2).  
* **CDC73** deletion → tumor formation (verdelli2024heterogeneoustranscriptionallandscapes pages 1-2).  
* **CDKN1B (p27)** loss → adenoma predisposition (verdelli2024heterogeneoustranscriptionallandscapes pages 1-2).

---

# Key structured summaries for knowledge-base ingestion
The following tables consolidate the most actionable structured content.

## Clinical classification and definitions
| Classification / concept | Concise definition | Typical biochemical pattern | Typical gland involvement | Terminology / key notes | Key citations |
|---|---|---|---|---|---|
| Primary parathyroid hyperplasia in PHPT / multigland disease (MGD) | In primary hyperparathyroidism, excess PTH arises from intrinsic parathyroid disease; multigland disease includes diffuse four-gland hyperplasia and double adenomas, rather than a single adenoma. | Usually hypercalcemia with inappropriately normal or elevated PTH; phosphate often low-normal/low in PHPT. | More than one gland affected; commonly 4-gland hyperplasia or double adenomas. | WHO 2022 favors **“multiglandular parathyroid disease (MGD)”** over “hyperplasia” in the PHPT setting; histology alone does not reliably distinguish hyperplasia from adenoma, so distinction is largely clinical (single- vs multigland disease). | (jha2023molecularandclinical pages 8-9, chakrabarty2024imagingrecommendationsfor pages 1-2, pavlidis2023updateonthe pages 1-2, chakrabarty2024imagingrecommendationsfor pages 3-5, english2024geneticsofhereditary pages 1-2) |
| Sporadic PHPT with MGD frequency context | Sporadic PHPT is usually single-gland, but a minority present with MGD/hyperplasia. | Hypercalcemia with elevated or unsuppressed PTH. | Solitary adenoma ~80–85%; MGD/hyperplasia ~10–15%; double adenoma ~4–5%. | Hyperplasia/MGD is clinically important because it raises risk of persistence/recurrence after surgery. | (chakrabarty2024imagingrecommendationsfor pages 1-2, pavlidis2023updateonthe pages 1-2) |
| Secondary parathyroid hyperplasia (CKD-related SHPT) | CKD-associated disturbances in phosphate, calcitriol, calcium, and FGF23-Klotho signaling chronically stimulate the glands, causing compensatory hyperplasia that may progress to nodular hyperplasia. | PTH elevated; calcium typically low or normal; phosphate often elevated in advanced CKD; calcitriol reduced. | Usually diffuse multigland involvement of all 4 glands; nodular remodeling may emerge over time. | Recent reviews note that the term **“hyperplasia” is generally reserved for secondary hyperplasia in CKD**. Severe SHPT (iPTH >300 pg/mL) was reported in ~33% in one 2023 review. | (jha2023molecularandclinical pages 7-8, vetter2024whatisthe pages 1-3, hiramitsu2023treatmentforsecondary pages 1-2, sevva2024pharmaceuticalmanagementof pages 1-2) |
| Tertiary parathyroid hyperplasia / tertiary hyperparathyroidism (tHPT) | Autonomous hyperparathyroidism that develops after prolonged SHPT, classically after kidney transplantation or longstanding CKD, when glands lose normal calcium/vitamin D responsiveness. | Persistently elevated PTH with **hypercalcemia**; phosphate variable, often less overtly elevated than in SHPT and may normalize after transplant. | Predominantly multigland disease; progressive enlargement of all 4 glands is typical. | One 2024 review reported ~90% of tHPT patients have multigland disease; persistent post-transplant disease remains common, declining from ~70% at 1 year to ~43% at 2 years in cited series. | (vetter2024whatisthe pages 10-12, vetter2024whatisthe pages 1-3, costea2025tertiaryhyperparathyroidismin pages 4-6, costea2025tertiaryhyperparathyroidismin pages 2-4) |
| Transition from SHPT to tHPT | Chronic polyclonal stimulation in SHPT can evolve to nodular/partly monoclonal growth with reduced CaSR/VDR sensitivity, producing autonomy and medical refractoriness. | SHPT: high PTH with low/normal Ca; tHPT: high PTH with high Ca. | Starts as diffuse CKD-related multigland hyperplasia and can progress to autonomous multigland disease. | This mechanistic transition explains why refractory renal hyperparathyroidism often requires subtotal or total parathyroidectomy rather than medical therapy alone. | (vetter2024whatisthe pages 1-3, hiramitsu2023treatmentforsecondary pages 1-2, costea2025tertiaryhyperparathyroidismin pages 4-6) |


*Table: This table summarizes the main clinical classifications of parathyroid hyperplasia and related multigland disease, contrasting primary PHPT-associated MGD with CKD-related secondary hyperplasia and autonomous tertiary disease. It also highlights the WHO 2022 terminology shift toward 'multiglandular parathyroid disease' in PHPT.*

## Genetics (syndromes, inheritance, patterns)
| Gene | Syndrome / phenotype | Inheritance | Typical parathyroid pattern | Key statistics / notes | Key citations |
|---|---|---|---|---|---|
| **MEN1** | Multiple endocrine neoplasia type 1 (syndromic hereditary PHPT) | Autosomal dominant | Typically **multifocal/multiglandular disease**; often described clinically as hyperplasia/MGD rather than single adenoma | Most common syndromic cause of hereditary PHPT; hereditary PHPT accounts for ~10% to >10% of PHPT overall; MEN1 penetrance for PHPT reported ~90% by age 70; somatic **MEN1** alterations also occur in sporadic tumors (~12–35% in reviews) (english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, simonds2020clinicalandmolecular pages 3-4) | PMID **36778668** cited via Open Targets; review DOI: 10.1210/endrev/bnad009 (OpenTargets Search: Hyperparathyroidism,Secondary hyperparathyroidism,Primary hyperparathyroidism-CASR,PTH,GCM2,MEN1,CDC73,RET, english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, simonds2020clinicalandmolecular pages 3-4) |
| **CDC73** | Hyperparathyroidism-jaw tumor syndrome (HPT-JT); also familial isolated PHPT and parathyroid carcinoma predisposition | Autosomal dominant | Can present with multigland disease, but especially important for **carcinoma-risk PHPT**; not limited to diffuse hyperplasia | HPT-JT has incomplete penetrance; reported parathyroid carcinoma risk ~20–25%; in a selected high-risk Indian cohort, 4/39 (10.2%) had **CDC73** variants; germline **CDC73** was the commonest abnormality in atypical parathyroid adenoma and carcinoma cohorts in one study (qadir2024moleculargeneticsin pages 1-3, jha2023molecularandclinical pages 15-16, simonds2020clinicalandmolecular pages 4-6) | Review DOI: 10.1210/endrev/bnad009; cohort DOI: 10.21203/rs.3.rs-5299691/v1 (qadir2024moleculargeneticsin pages 1-3, jha2023molecularandclinical pages 15-16, simonds2020clinicalandmolecular pages 4-6) |
| **RET** | Multiple endocrine neoplasia type 2A (MEN2A) | Autosomal dominant | Usually **not the dominant parathyroid presentation**; may cause parathyroid tumors/hyperplasia, often with medullary thyroid carcinoma and pheochromocytoma | Lower penetrance than MEN1; English et al. report MEN2 PHPT ~5–15%; large MEN2A cohort (1085 patients) had only 10 patients initially presenting with PHPT, suggesting low yield of RET testing in isolated PHPT (english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 15-16) | Review DOI: 10.1007/s42000-023-00508-9; review DOI: 10.1210/endrev/bnad009 (english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 15-16) |
| **CDKN1B** | MEN4 (MEN1-like syndrome) | Autosomal dominant | Often **multiglandular / MEN1-like hereditary PHPT** rather than isolated single-gland disease | MEN4 is rarer than MEN1; penetrance for PHPT reported ~75% in review summaries; included on hereditary PHPT testing panels because results affect surgical planning and family testing (english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, simonds2020clinicalandmolecular pages 4-6) | Review DOI: 10.1007/s42000-023-00508-9; ClinVar/Open Targets evidence noted for CDKN1B (OpenTargets Search: Hyperparathyroidism,Secondary hyperparathyroidism,Primary hyperparathyroidism-CASR,PTH,GCM2,MEN1,CDC73,RET, english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, simonds2020clinicalandmolecular pages 4-6) |
| **CASR** | Familial hypocalciuric hypercalcemia type 1 (FHH1); related neonatal severe hyperparathyroidism when biallelic severe loss-of-function | Autosomal dominant for FHH1; biallelic severe forms for NSHPT | Usually **not classic hyperplastic PHPT**; causes lifelong mild hypercalcemia with inappropriately normal/high PTH and can mimic PHPT; important differential diagnosis to avoid unnecessary PTX | FHH prevalence ~1.3 per 100,000 and accounts for about 2% of apparent PHPT; UCCR <0.01 typical in ~80–95% of FHH; CASR is among the most frequently positive genes in hereditary PHPT testing cohorts (11/19 positives in one UK series were CASR) (english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 23-24) | PMIDs in Open Targets include **15572418**, **27434672**; review DOI: 10.1007/s42000-023-00508-9 (OpenTargets Search: Hyperparathyroidism,Secondary hyperparathyroidism,Primary hyperparathyroidism-CASR,PTH,GCM2,MEN1,CDC73,RET, english2024geneticsofhereditary pages 8-9, english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 23-24) |
| **GNA11** | Familial hypocalciuric hypercalcemia type 2 (FHH2) | Autosomal dominant | Usually **FHH phenotype rather than true multigland hyperplasia** | Included in hereditary hypercalcemia/PHPT differential; like CASR-related FHH, tends to show hypocalciuria and generally benign course rather than surgically correctable hyperplasia (english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 15-16, jha2023molecularandclinical pages 23-24) | Review DOI: 10.1210/endrev/bnad009; review DOI: 10.1007/s42000-023-00508-9 (english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 15-16, jha2023molecularandclinical pages 23-24) |
| **AP2S1** | Familial hypocalciuric hypercalcemia type 3 (FHH3) | Autosomal dominant | Usually **FHH mimic**, not classic multigland hyperplasia | Nearly all pathogenic variants affect **Arg15** in reported series; in a UK hereditary PHPT testing cohort, 1/19 pathogenic findings was **AP2S1**; clinically relevant because parathyroidectomy usually does not correct FHH (english2024geneticsofhereditary pages 8-9, jha2023molecularandclinical pages 23-24) | Review DOI: 10.1007/s42000-023-00508-9; review DOI: 10.1210/endrev/bnad009 (english2024geneticsofhereditary pages 8-9, jha2023molecularandclinical pages 23-24) |
| **GCM2** | Familial isolated hyperparathyroidism (FIHP); activating variants also linked to hereditary PHPT | Usually autosomal dominant with variable/low penetrance | Can be associated with **multigland disease / familial hyperplasia-like PHPT**, but penetrance is variable and many families remain unexplained | Activating **GCM2** variants reported in ~18% of FIHP in some series; among FIHP kindreds pre-screened negative for MEN1/CASR/CDC73, only ~10–20% carry **GCM2** variants, leaving ~80–90% unexplained; low penetrance has raised questions about routine panel inclusion in all settings (jha2023molecularandclinical pages 23-24, qadir2024moleculargeneticsin pages 9-11) | PMIDs in Open Targets include **27745835**, **39024449**, **36653562** (OpenTargets Search: Hyperparathyroidism,Secondary hyperparathyroidism,Primary hyperparathyroidism-CASR,PTH,GCM2,MEN1,CDC73,RET, jha2023molecularandclinical pages 23-24, qadir2024moleculargeneticsin pages 9-11) |


*Table: This table summarizes the main hereditary genes linked to parathyroid hyperplasia, multiglandular disease, or closely related hereditary PHPT phenotypes. It highlights inheritance, the usual parathyroid pattern, and key statistics that help distinguish true multigland disease from mimics such as familial hypocalciuric hypercalcemia.*

## Diagnostics (labs, imaging, performance statistics)
| Workup component | What to measure/use | Key findings or performance statistics | Notes specific to multigland disease / secondary HPT | Key citations |
|---|---|---|---|---|
| Biochemical diagnosis | Serum total calcium, ionized calcium, intact PTH | PHPT is diagnosed by hypercalcemia with elevated or inappropriately normal PTH; one cohort used serum Ca >2.70 mmol/L and/or ionized Ca >1.28 mmol/L with unsuppressed PTH as diagnostic thresholds | Biochemistry alone cannot reliably distinguish adenoma from hyperplasia/MGD; markedly high calcium and PTH may raise concern for carcinoma rather than benign MGD | (chakrabarty2024imagingrecommendationsfor pages 1-2, chen2023clinicalandgenetic pages 1-2, english2024geneticsofhereditary pages 1-2) |
| Mineral metabolism panel | Serum phosphate, 25-OH vitamin D, renal function | In CKD-related SHPT, progressive hyperphosphatemia and reduced active vitamin D drive hypocalcemia and compensatory parathyroid hyperplasia; vitamin D status is important for surgical outcomes and recurrence risk | Particularly important in SHPT/tHPT to separate CKD-mineral bone disorder from primary disease and to optimize pre-/post-operative management | (pavlidis2023updateonthe pages 1-2, vetter2024whatisthe pages 1-3, hiramitsu2023treatmentforsecondary pages 1-2) |
| Urinary calcium assessment | Urinary calcium-to-creatinine clearance ratio (UCCR/UCCR) | Majority of FHH patients have UCCR <0.01; FHH accounts for about 2% of patients initially considered to have PHPT in some series | Essential when apparent PHPT presents with mild hypercalcemia or familial disease; helps avoid unnecessary parathyroidectomy in FHH | (english2024geneticsofhereditary pages 1-2, jha2023molecularandclinical pages 23-24) |
| Neck ultrasound | First-line anatomic localization | Widely used first-line tool; pooled sensitivity for US in prior meta-analysis about 80% for PHPT localization | Lower sensitivity in MGD and renal hyperplasia; in renal HPT/hyperplastic glands, sonography sensitivity reported around 62% | (scheepers2023diagnosticperformanceof pages 13-14, vetter2024whatisthe pages 10-12, chakrabarty2024imagingrecommendationsfor media a62b0df1) |
| Sestamibi scintigraphy / SPECT/CT | Functional localization with 99mTc-sestamibi, often with SPECT/CT | Prior meta-analysis pooled sensitivity about 83% for MIBI in PHPT localization | Performance drops in MGD: reported MIBI sensitivity about 44% for MGD; in renal HPT/hyperplastic glands scintigraphy sensitivity around 55% | (scheepers2023diagnosticperformanceof pages 13-14, scheepers2023diagnosticperformanceof pages 14-15, vetter2024whatisthe pages 10-12) |
| 4DCT | Multiphasic CT for localization and MGD prediction | One meta-analysis cited sensitivity 81.0% for 4DCT vs 65.0% for MIBI; MGD sensitivity reported about 60%; 4DCT MGD prediction scores: composite score specificity 72% (>=4), 86% (>=5), 100% (=6), CT-only score specificity 74% (>=3) and 88% (>=4) | Helpful when first-line imaging is negative or recurrent disease is suspected; exposes patients to ionizing radiation; useful for predicting MGD before surgery | (chakrabarty2024imagingrecommendationsfor pages 9-11, scheepers2023diagnosticperformanceof pages 13-14, scheepers2023diagnosticperformanceof pages 14-15) |
| MRI / 4D MRI | Radiation-free localization, dynamic contrast-enhanced protocols | Conventional MRI sensitivity 39.1%-94.3%; 4D MRI sensitivity 55.6%-100%; first-line 4D MRI often 64%-100%; reported MGD sensitivity 67%-100%; one review cited 92% for single-gland disease and 74% for MGD | Attractive in younger patients, recurrent disease, and when radiation avoidance matters; superior to conventional imaging in some reoperative/MGD settings | (chakrabarty2024imagingrecommendationsfor pages 9-11, scheepers2023diagnosticperformanceof pages 13-14, scheepers2023diagnosticperformanceof pages 9-11, scheepers2023diagnosticperformanceof pages 1-2) |
| 18F-FCH PET/CT | High-resolution functional imaging | Reported as superior to ultrasound and MIBI; accepted as an alternative first-line modality in some centers | Useful in difficult localization, persistent/recurrent disease, and MGD; increasingly used before reoperation | (chakrabarty2024imagingrecommendationsfor pages 9-11, pavlidis2023updateonthe pages 1-2, scheepers2023diagnosticperformanceof pages 2-4, chakrabarty2024imagingrecommendationsfor media a62b0df1) |
| PET/MRI | Hybrid metabolic + high-contrast soft tissue imaging | 18F-FCH PET/MRI sensitivity 84.2%-100%; specificity 96.0%-100% in reported studies; described as highest diagnostic accuracy among MRI-based approaches | Particularly useful for MGD, pediatric patients, and complex surgical planning while minimizing radiation | (scheepers2023diagnosticperformanceof pages 13-14, scheepers2023diagnosticperformanceof pages 9-11, chakrabarty2024imagingrecommendationsfor pages 9-11) |
| Intraoperative PTH monitoring | Rapid ioPTH during parathyroidectomy | In PHPT/reoperative disease, PTH <=40 pg/mL or >=50% drop from baseline minimizes persistence risk; Miami criterion (>50% drop at >=10 min) is used in tertiary/renal HPT surgery literature | In SHPT, formal ioPTH criteria are less established because all hyperplastic glands must be removed; nevertheless, intraoperative monitoring may support completeness of resection | (pavlidis2023updateonthe pages 1-2, costea2025tertiaryhyperparathyroidismin pages 10-12, hiramitsu2023treatmentforsecondary pages 1-2) |
| Postoperative surveillance | Serum calcium and PTH follow-up | Six-month calcium >=9.8 mg/dL and PTH >=80 pg/mL indicate higher recurrence risk after PHPT surgery | Four-gland hyperplasia/double adenomas have higher persistence/recurrence risk, so long-term follow-up is especially important | (pavlidis2023updateonthe pages 1-2) |
| Strategy for MGD / renal hyperplasia | Bilateral neck exploration, selective imaging, four-gland assessment | Figure-based management algorithms recommend imaging for planning, then bilateral neck exploration with subtotal or total parathyroidectomy for MGD; in tHPT, 90% have multiglandular disease | In SHPT/tHPT, localization imaging is adjunctive; operative four-gland exploration remains the most reliable strategy because hyperplasia is often diffuse/multiglandular | (vetter2024whatisthe pages 10-12, vetter2024whatisthe pages 1-3, chakrabarty2024imagingrecommendationsfor media 9629bfff) |


*Table: This table summarizes the current diagnostic workup for parathyroid hyperplasia and related hyperparathyroid states, including key laboratory tests, localization imaging, intraoperative monitoring, and special considerations for multigland disease and CKD-related secondary/tertiary hyperparathyroidism.*

## Treatments and real-world implementation
| Context | Treatment / implementation | Real-world use / indication | Key outcomes or statistics | Trial / source |
|---|---|---|---|---|
| PHPT with multigland disease (formerly “hyperplasia”; WHO 2022 favors MGD terminology) | Bilateral neck exploration (BNE) with subtotal or total parathyroidectomy | Preferred operative pathway when multigland disease is suspected/localized poorly; imaging mainly supports planning, but definitive management is surgical exploration | Figure-based algorithm recommends imaging ± parathyroid venous sampling, then BNE followed by subtotal/total parathyroidectomy for MGD; multigland disease/hyperplasia is associated with higher persistence/recurrence risk after surgery than single-gland disease (chakrabarty2024imagingrecommendationsfor media a62b0df1, pavlidis2023updateonthe pages 1-2) | Chakrabarty 2024; Pavlidis 2023 (chakrabarty2024imagingrecommendationsfor media a62b0df1, pavlidis2023updateonthe pages 1-2) |
| PHPT, persistent/recurrent disease risk management | Intraoperative PTH monitoring during parathyroidectomy | Used to reduce risk of persistence in resection for pHPT, including cases with multigland disease | Intraoperative PTH ≤ 40 pg/mL or a ≥50% drop from baseline minimized persistence risk; recurrence risk higher with double adenomas/four-gland hyperplasia; modern recurrence rates reported ~2.5–5% (pavlidis2023updateonthe pages 1-2) | Pavlidis 2023 (pavlidis2023updateonthe pages 1-2) |
| PHPT managed medically when surgery is not performed or delayed | Cinacalcet, denosumab, or combination (plus vitamin D) | Investigated for biochemical control and bone protection in primary hyperparathyroidism; not curative for multigland disease but relevant where surgery is deferred/inappropriate | DENOCINA phase 3 trial enrolled 46 patients; combined arm used denosumab 60 mg every 6 months + cinacalcet 30 mg daily + vitamin D 50 μg daily; endpoints included DXA BMD, serum calcium, PTH, bone turnover markers, nephrolithiasis/nephrocalcinosis imaging outcomes (NCT03027557 chunk 1, NCT03027557 chunk 2, NCT03027557 chunk 3) | NCT03027557 / DENOCINA (NCT03027557 chunk 1, NCT03027557 chunk 2, NCT03027557 chunk 3) |
| CKD-related secondary hyperparathyroidism (SHPT) | Phosphate control: dietary phosphate restriction and phosphate binders | First-line background management to reduce chronic parathyroid stimulation in CKD-mineral bone disorder | Standard therapy in SHPT; used alongside vitamin D analogs and calcimimetics before considering surgery (vetter2024whatisthe pages 1-3, sevva2024pharmaceuticalmanagementof pages 2-3, NCT01421407 chunk 1) | Vetter 2024; Sevva 2024; NCT01421407 background (vetter2024whatisthe pages 1-3, sevva2024pharmaceuticalmanagementof pages 2-3, NCT01421407 chunk 1) |
| CKD-related SHPT | Vitamin D receptor activators/analogs (calcitriol, alfacalcidol/alphacalcidol, doxercalciferol, paricalcitol; others in regional practice) | Common medical therapy for hypocalcemia-driven PTH excess | Recommended pharmacologic option in CKD SHPT; used with phosphate lowering and/or calcimimetics; tertiary HPT review notes they lower PTH, though vascular calcification effects remain debated (vetter2024whatisthe pages 1-3, sevva2024pharmaceuticalmanagementof pages 2-3, costea2025tertiaryhyperparathyroidismin pages 9-10) | Vetter 2024; Sevva 2024; Costea 2025 (vetter2024whatisthe pages 1-3, sevva2024pharmaceuticalmanagementof pages 2-3, costea2025tertiaryhyperparathyroidismin pages 9-10) |
| CKD-related SHPT | Calcimimetics: cinacalcet (oral) | Widely used for refractory biochemical SHPT on dialysis | Background/eligibility in HIFU trial required PTH >800 pg/mL despite ≥3 months cinacalcet >30 mg/day ± vitamin D; cinacalcet also reported to improve endothelial dysfunction/cardiac hypertrophy in hemodialysis patients in reviewed literature (NCT01421407 chunk 1, vetter2024whatisthe pages 17-18) | NCT01421407; Vetter 2024 (NCT01421407 chunk 1, vetter2024whatisthe pages 17-18) |
| CKD-related SHPT | Calcimimetics: etelcalcetide (IV during dialysis) | Real-world dialysis implementation as second-generation calcimimetic | In a 2018–2023 retrospective cohort of 52 dialysis patients, 34/52 (65.4%) received cinacalcet and etelcalcetide; 29/33 (87.9%) treated with etelcalcetide had significant PTH reduction, up to 57% from baseline; none required parathyroidectomy for refractory PTH or drug toxicity in that series (sevva2024pharmaceuticalmanagementof pages 1-2) | Sevva 2024 (sevva2024pharmaceuticalmanagementof pages 1-2) |
| CKD-related SHPT, drug-refractory disease | Parathyroidectomy (subtotal PTX, total PTX with autotransplantation, or total PTX without autotransplantation; sometimes with transcervical thymectomy) | Reserved for refractory SHPT, severe symptoms, or failure/cost issues of medical therapy | Review emphasizes PTx remains one of the most important therapies despite calcimimetics; complete removal of all glands is crucial to prevent persistence/recurrence; PTx associated with improved bone density, fracture risk, survival, and quality of life (hiramitsu2023treatmentforsecondary pages 1-2) | Hiramitsu 2023 (hiramitsu2023treatmentforsecondary pages 1-2) |
| CKD-related SHPT in transplant candidates | Subtotal PTX or total PTX with autotransplantation | Preferred when future kidney transplantation is anticipated | 2024 surgical review recommends subtotal PTX or total PTX with autotransplantation for transplant-eligible patients; total PTX can be considered for non-transplant candidates (vetter2024whatisthe pages 1-3) | Vetter 2024 (vetter2024whatisthe pages 1-3) |
| Post-transplant tertiary hyperparathyroidism (tHPT) | Subtotal parathyroidectomy with four-gland exploration | Favored surgical approach for persistent autonomous post-transplant disease, usually multiglandular | Review states 90% of tHPT patients have multigland disease; subtotal PTX is favored because it has lower hypoparathyroidism risk than total PTX with autotransplantation with similar cure rates (vetter2024whatisthe pages 10-12) | Vetter 2024 (vetter2024whatisthe pages 10-12) |
| Post-transplant tertiary hyperparathyroidism (tHPT) | Timing of parathyroidectomy before vs after transplant | Individualized based on suspected autonomy, graft considerations, and biochemical persistence | If autonomy is suspected, surgery ideally precedes transplantation; if post-transplant surgery is needed, many centers delay until ~1 year; persistent sHPT/tHPT reported to decline from 70% at 1 year to 43% at 2 years post-transplant (vetter2024whatisthe pages 1-3); a meta-analysis of 223 patients found no significant difference between pre- vs post-transplant PTX for follow-up PTH or calcium (vetter2024whatisthe pages 1-3) | Vetter 2024; Karniadakis 2025 abstracted in search results (vetter2024whatisthe pages 1-3) |
| Post-transplant tertiary hyperparathyroidism (tHPT) | Surgery vs cinacalcet | Comparative management for persistent autonomous disease after transplant | Retrospective comparison cited in 2024 review found parathyroidectomy achieved higher PTH normalization and lower graft failure than cinacalcet (9% vs 33% allograft loss) (vetter2024whatisthe pages 10-12) | Vetter 2024 (vetter2024whatisthe pages 10-12) |
| Procedural/ablative alternative for SHPT | High-intensity focused ultrasound (HIFU; TH-One device) | Investigational non-surgical ablation for uncontrolled SHPT in chronic hemodialysis with 1–2 enlarged glands on ultrasound | Randomized open-label trial planned primary endpoint of ≥30% reduction in mean serum iPTH at 6 months and secondary endpoint of achieving KDIGO-range PTH; required uncontrolled disease despite cinacalcet; study was withdrawn with actual enrollment = 0 (NCT01421407 chunk 1) | NCT01421407 (NCT01421407 chunk 1) |


*Table: This table summarizes treatment strategies and real-world implementation of therapies for parathyroid hyperplasia across primary multigland disease, CKD-related secondary hyperparathyroidism, and post-transplant tertiary hyperparathyroidism. It highlights surgical standards, medical therapies, response statistics, and relevant clinical trial identifiers.*

---

# Visual evidence (imaging review)
The 2024 imaging review contains (i) a table comparing imaging modalities and (ii) a management algorithm with a dedicated multigland disease branch supporting bilateral neck exploration with subtotal/total parathyroidectomy (chakrabarty2024imagingrecommendationsfor media 9629bfff, chakrabarty2024imagingrecommendationsfor media a62b0df1).

---

# Limitations of this synthesis
* ICD/MeSH/Orphanet/MONDO identifiers specific to “parathyroid hyperplasia” were not available in the retrieved full texts; ontology anchoring is therefore provided via related MONDO entities, gene syndromes, and HPO/GO/UBERON mappings.  
* Several key areas (variant cataloging with allele frequencies; standardized QoL instruments; dedicated SHPT/tHPT RCTs beyond trial registry records) require targeted database retrieval beyond the current evidence set.


References

1. (jha2023molecularandclinical pages 8-9): S. Jha and W. Simonds. Molecular and clinical spectrum of primary hyperparathyroidism. Endocrine reviews, Mar 2023. URL: https://doi.org/10.1210/endrev/bnad009, doi:10.1210/endrev/bnad009. This article has 68 citations and is from a domain leading peer-reviewed journal.

2. (vetter2024whatisthe pages 1-3): Diana Vetter and Thomas Schachtner. What is the role of surgery in secondary and tertiary hyperparathyroidism? Advances in Kidney Transplantation [Working Title], Aug 2024. URL: https://doi.org/10.5772/intechopen.1006528, doi:10.5772/intechopen.1006528. This article has 0 citations.

3. (costea2025tertiaryhyperparathyroidismin pages 4-6): Mirona Costea, D. Tilici, D. Păun, V. Nimigean, S. Paun, and R. Dǎnciulescu-Miulescu. Tertiary hyperparathyroidism in diabetic nephropathy: an underrecognized complication—a narrative review. Biomedicines, Oct 2025. URL: https://doi.org/10.3390/biomedicines13112604, doi:10.3390/biomedicines13112604. This article has 2 citations.

4. (OpenTargets Search: Hyperparathyroidism,Secondary hyperparathyroidism,Primary hyperparathyroidism-CASR,PTH,GCM2,MEN1,CDC73,RET): Open Targets Query (Hyperparathyroidism,Secondary hyperparathyroidism,Primary hyperparathyroidism-CASR,PTH,GCM2,MEN1,CDC73,RET, 37 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (chakrabarty2024imagingrecommendationsfor pages 3-5): Nivedita Chakrabarty, Abhishek Mahajan, Sandip Basu, and Anil K. D’Cruz. Imaging recommendations for diagnosis and management of primary parathyroid pathologies: a comprehensive review. Cancers, 16:2593, Jul 2024. URL: https://doi.org/10.3390/cancers16142593, doi:10.3390/cancers16142593. This article has 25 citations.

6. (hiramitsu2023treatmentforsecondary pages 1-2): Takahisa Hiramitsu, Yuki Hasegawa, Kenta Futamura, Manabu Okada, Norihiko Goto, Shunji Narumi, Yoshihiko Watarai, Yoshihiro Tominaga, and Toshihiro Ichimori. Treatment for secondary hyperparathyroidism focusing on parathyroidectomy. Frontiers in Endocrinology, Apr 2023. URL: https://doi.org/10.3389/fendo.2023.1169793, doi:10.3389/fendo.2023.1169793. This article has 47 citations.

7. (vetter2024whatisthe pages 10-12): Diana Vetter and Thomas Schachtner. What is the role of surgery in secondary and tertiary hyperparathyroidism? Advances in Kidney Transplantation [Working Title], Aug 2024. URL: https://doi.org/10.5772/intechopen.1006528, doi:10.5772/intechopen.1006528. This article has 0 citations.

8. (chakrabarty2024imagingrecommendationsfor pages 1-2): Nivedita Chakrabarty, Abhishek Mahajan, Sandip Basu, and Anil K. D’Cruz. Imaging recommendations for diagnosis and management of primary parathyroid pathologies: a comprehensive review. Cancers, 16:2593, Jul 2024. URL: https://doi.org/10.3390/cancers16142593, doi:10.3390/cancers16142593. This article has 25 citations.

9. (NCT03027557 chunk 1): Peter Vestergaard. Treatment of Primary Hyperparathyroidism With Denosumab and Cinacalcet.. Peter Vestergaard. 2017. ClinicalTrials.gov Identifier: NCT03027557

10. (NCT03027557 chunk 3): Peter Vestergaard. Treatment of Primary Hyperparathyroidism With Denosumab and Cinacalcet.. Peter Vestergaard. 2017. ClinicalTrials.gov Identifier: NCT03027557

11. (NCT01421407 chunk 1):  Efficacy and Safety of High Intensity Focused Ultrasound (HIFU) Device to Treat Secondary Hyperparathyroidism. Theraclion. 2011. ClinicalTrials.gov Identifier: NCT01421407

12. (pavlidis2023updateonthe pages 1-2): Efstathios T Pavlidis and Theodoros E Pavlidis. Update on the current management of persistent and recurrent primary hyperparathyroidism after parathyroidectomy. World Journal of Clinical Cases, 11:2213-2225, Apr 2023. URL: https://doi.org/10.12998/wjcc.v11.i10.2213, doi:10.12998/wjcc.v11.i10.2213. This article has 23 citations.

13. (jha2023molecularandclinical pages 7-8): S. Jha and W. Simonds. Molecular and clinical spectrum of primary hyperparathyroidism. Endocrine reviews, Mar 2023. URL: https://doi.org/10.1210/endrev/bnad009, doi:10.1210/endrev/bnad009. This article has 68 citations and is from a domain leading peer-reviewed journal.

14. (english2024geneticsofhereditary pages 8-9): Katherine A. English, Kate E. Lines, and Rajesh V. Thakker. Genetics of hereditary forms of primary hyperparathyroidism. Hormones (Athens, Greece), 23:3-14, Dec 2024. URL: https://doi.org/10.1007/s42000-023-00508-9, doi:10.1007/s42000-023-00508-9. This article has 41 citations.

15. (scheepers2023diagnosticperformanceof pages 13-14): Max H. M. C. Scheepers, Zaid Al-Difaie, Lloyd Brandts, Andrea Peeters, Bjorn Winkens, Mahdi Al-Taher, Sanne M. E. Engelen, Tim Lubbers, Bas Havekes, Nicole D. Bouvy, and Alida A. Postma. Diagnostic performance of magnetic resonance imaging for parathyroid localization of primary hyperparathyroidism: a systematic review. Diagnostics, 14:25, Dec 2023. URL: https://doi.org/10.3390/diagnostics14010025, doi:10.3390/diagnostics14010025. This article has 10 citations.

16. (chen2023clinicalandgenetic pages 1-2): Yingyu Chen, An Song, Min Nie, Yan Jiang, Mei Li, Weibo Xia, Ou Wang, and Xiaoping Xing. Clinical and genetic analysis of atypical parathyroid adenoma compared with parathyroid carcinoma and benign lesions in a chinese cohort. Frontiers in Endocrinology, Jan 2023. URL: https://doi.org/10.3389/fendo.2023.1027598, doi:10.3389/fendo.2023.1027598. This article has 19 citations.

17. (chen2023clinicalandgenetic pages 6-8): Yingyu Chen, An Song, Min Nie, Yan Jiang, Mei Li, Weibo Xia, Ou Wang, and Xiaoping Xing. Clinical and genetic analysis of atypical parathyroid adenoma compared with parathyroid carcinoma and benign lesions in a chinese cohort. Frontiers in Endocrinology, Jan 2023. URL: https://doi.org/10.3389/fendo.2023.1027598, doi:10.3389/fendo.2023.1027598. This article has 19 citations.

18. (verdelli2024heterogeneoustranscriptionallandscapes pages 1-2): Chiara Verdelli, Silvia Carrara, Riccardo Maggiore, Paolo Dalino Ciaramella, and Sabrina Corbetta. Heterogeneous transcriptional landscapes in human sporadic parathyroid gland tumors. International Journal of Molecular Sciences, 25:10782, Oct 2024. URL: https://doi.org/10.3390/ijms251910782, doi:10.3390/ijms251910782. This article has 3 citations.

19. (jha2023molecularandclinical pages 1-2): S. Jha and W. Simonds. Molecular and clinical spectrum of primary hyperparathyroidism. Endocrine reviews, Mar 2023. URL: https://doi.org/10.1210/endrev/bnad009, doi:10.1210/endrev/bnad009. This article has 68 citations and is from a domain leading peer-reviewed journal.

20. (english2024geneticsofhereditary pages 1-2): Katherine A. English, Kate E. Lines, and Rajesh V. Thakker. Genetics of hereditary forms of primary hyperparathyroidism. Hormones (Athens, Greece), 23:3-14, Dec 2024. URL: https://doi.org/10.1007/s42000-023-00508-9, doi:10.1007/s42000-023-00508-9. This article has 41 citations.

21. (jha2023molecularandclinical pages 15-16): S. Jha and W. Simonds. Molecular and clinical spectrum of primary hyperparathyroidism. Endocrine reviews, Mar 2023. URL: https://doi.org/10.1210/endrev/bnad009, doi:10.1210/endrev/bnad009. This article has 68 citations and is from a domain leading peer-reviewed journal.

22. (jha2023molecularandclinical pages 23-24): S. Jha and W. Simonds. Molecular and clinical spectrum of primary hyperparathyroidism. Endocrine reviews, Mar 2023. URL: https://doi.org/10.1210/endrev/bnad009, doi:10.1210/endrev/bnad009. This article has 68 citations and is from a domain leading peer-reviewed journal.

23. (qadir2024moleculargeneticsin pages 1-3): Ajaz Qadir, Raiz Ahmad Misgar, Ankit Chhabra, Imtiyaz Ahmad Bhat, Mir Iftikhar Bashir, Arshad Iqbal Wani, Munir Ahmad Wani, and Ajaz Ahmad Malik. Molecular genetics in familial primary hyperparathyroidism: a study from northern india. Nov 2024. URL: https://doi.org/10.21203/rs.3.rs-5299691/v1, doi:10.21203/rs.3.rs-5299691/v1.

24. (roser2023diagnosisandmanagement pages 3-5): Pia Roser, Bianca M Leca, Claudia Coelho, Klaus-Martin Schulte, Jackie Gilbert, Eftychia E Drakou, Christos Kosmas, Ling Ling Chuah, Husam Wassati, Alexander D Miras, James Crane, Simon J B Aylwin, Ashley B Grossman, and Georgios K Dimitriadis. Diagnosis and management of parathyroid carcinoma: a state-of-the-art review. Endocrine-Related Cancer, Apr 2023. URL: https://doi.org/10.1530/erc-22-0287, doi:10.1530/erc-22-0287. This article has 80 citations and is from a domain leading peer-reviewed journal.

25. (roser2023diagnosisandmanagement pages 7-8): Pia Roser, Bianca M Leca, Claudia Coelho, Klaus-Martin Schulte, Jackie Gilbert, Eftychia E Drakou, Christos Kosmas, Ling Ling Chuah, Husam Wassati, Alexander D Miras, James Crane, Simon J B Aylwin, Ashley B Grossman, and Georgios K Dimitriadis. Diagnosis and management of parathyroid carcinoma: a state-of-the-art review. Endocrine-Related Cancer, Apr 2023. URL: https://doi.org/10.1530/erc-22-0287, doi:10.1530/erc-22-0287. This article has 80 citations and is from a domain leading peer-reviewed journal.

26. (simonds2020clinicalandmolecular pages 3-4): William F. Simonds. Clinical and molecular genetics of primary hyperparathyroidism. Hormone and Metabolic Research, 52:578-587, Mar 2020. URL: https://doi.org/10.1055/a-1132-6223, doi:10.1055/a-1132-6223. This article has 12 citations and is from a peer-reviewed journal.

27. (simonds2020clinicalandmolecular pages 4-6): William F. Simonds. Clinical and molecular genetics of primary hyperparathyroidism. Hormone and Metabolic Research, 52:578-587, Mar 2020. URL: https://doi.org/10.1055/a-1132-6223, doi:10.1055/a-1132-6223. This article has 12 citations and is from a peer-reviewed journal.

28. (qadir2024moleculargeneticsin pages 9-11): Ajaz Qadir, Raiz Ahmad Misgar, Ankit Chhabra, Imtiyaz Ahmad Bhat, Mir Iftikhar Bashir, Arshad Iqbal Wani, Munir Ahmad Wani, and Ajaz Ahmad Malik. Molecular genetics in familial primary hyperparathyroidism: a study from northern india. Nov 2024. URL: https://doi.org/10.21203/rs.3.rs-5299691/v1, doi:10.21203/rs.3.rs-5299691/v1.

29. (jha2023molecularandclinical pages 11-12): S. Jha and W. Simonds. Molecular and clinical spectrum of primary hyperparathyroidism. Endocrine reviews, Mar 2023. URL: https://doi.org/10.1210/endrev/bnad009, doi:10.1210/endrev/bnad009. This article has 68 citations and is from a domain leading peer-reviewed journal.

30. (verdelli2024heterogeneoustranscriptionallandscapes pages 7-9): Chiara Verdelli, Silvia Carrara, Riccardo Maggiore, Paolo Dalino Ciaramella, and Sabrina Corbetta. Heterogeneous transcriptional landscapes in human sporadic parathyroid gland tumors. International Journal of Molecular Sciences, 25:10782, Oct 2024. URL: https://doi.org/10.3390/ijms251910782, doi:10.3390/ijms251910782. This article has 3 citations.

31. (costea2025tertiaryhyperparathyroidismin pages 2-4): Mirona Costea, D. Tilici, D. Păun, V. Nimigean, S. Paun, and R. Dǎnciulescu-Miulescu. Tertiary hyperparathyroidism in diabetic nephropathy: an underrecognized complication—a narrative review. Biomedicines, Oct 2025. URL: https://doi.org/10.3390/biomedicines13112604, doi:10.3390/biomedicines13112604. This article has 2 citations.

32. (simonds2020clinicalandmolecular pages 1-3): William F. Simonds. Clinical and molecular genetics of primary hyperparathyroidism. Hormone and Metabolic Research, 52:578-587, Mar 2020. URL: https://doi.org/10.1055/a-1132-6223, doi:10.1055/a-1132-6223. This article has 12 citations and is from a peer-reviewed journal.

33. (sevva2024pharmaceuticalmanagementof pages 2-3): Christina Sevva, Dimitrios Divanis, Ariti Tsinari, Petros Grammenos, Styliani Laskou, Stylianos Mantalobas, Eleni Paschou, Vasiliki Magra, Periklis Kopsidas, Isaak Kesisoglou, Vassilios Liakopoulos, and Konstantinos Sapalidis. Pharmaceutical management of secondary hyperparathyroidism and the role of surgery: a 5-year retrospective study. Medicina, 60:812, May 2024. URL: https://doi.org/10.3390/medicina60050812, doi:10.3390/medicina60050812. This article has 3 citations.

34. (jha2023molecularandclinical pages 10-11): S. Jha and W. Simonds. Molecular and clinical spectrum of primary hyperparathyroidism. Endocrine reviews, Mar 2023. URL: https://doi.org/10.1210/endrev/bnad009, doi:10.1210/endrev/bnad009. This article has 68 citations and is from a domain leading peer-reviewed journal.

35. (chakrabarty2024imagingrecommendationsfor media a62b0df1): Nivedita Chakrabarty, Abhishek Mahajan, Sandip Basu, and Anil K. D’Cruz. Imaging recommendations for diagnosis and management of primary parathyroid pathologies: a comprehensive review. Cancers, 16:2593, Jul 2024. URL: https://doi.org/10.3390/cancers16142593, doi:10.3390/cancers16142593. This article has 25 citations.

36. (scheepers2023diagnosticperformanceof pages 14-15): Max H. M. C. Scheepers, Zaid Al-Difaie, Lloyd Brandts, Andrea Peeters, Bjorn Winkens, Mahdi Al-Taher, Sanne M. E. Engelen, Tim Lubbers, Bas Havekes, Nicole D. Bouvy, and Alida A. Postma. Diagnostic performance of magnetic resonance imaging for parathyroid localization of primary hyperparathyroidism: a systematic review. Diagnostics, 14:25, Dec 2023. URL: https://doi.org/10.3390/diagnostics14010025, doi:10.3390/diagnostics14010025. This article has 10 citations.

37. (chakrabarty2024imagingrecommendationsfor pages 9-11): Nivedita Chakrabarty, Abhishek Mahajan, Sandip Basu, and Anil K. D’Cruz. Imaging recommendations for diagnosis and management of primary parathyroid pathologies: a comprehensive review. Cancers, 16:2593, Jul 2024. URL: https://doi.org/10.3390/cancers16142593, doi:10.3390/cancers16142593. This article has 25 citations.

38. (scheepers2023diagnosticperformanceof pages 9-11): Max H. M. C. Scheepers, Zaid Al-Difaie, Lloyd Brandts, Andrea Peeters, Bjorn Winkens, Mahdi Al-Taher, Sanne M. E. Engelen, Tim Lubbers, Bas Havekes, Nicole D. Bouvy, and Alida A. Postma. Diagnostic performance of magnetic resonance imaging for parathyroid localization of primary hyperparathyroidism: a systematic review. Diagnostics, 14:25, Dec 2023. URL: https://doi.org/10.3390/diagnostics14010025, doi:10.3390/diagnostics14010025. This article has 10 citations.

39. (scheepers2023diagnosticperformanceof pages 1-2): Max H. M. C. Scheepers, Zaid Al-Difaie, Lloyd Brandts, Andrea Peeters, Bjorn Winkens, Mahdi Al-Taher, Sanne M. E. Engelen, Tim Lubbers, Bas Havekes, Nicole D. Bouvy, and Alida A. Postma. Diagnostic performance of magnetic resonance imaging for parathyroid localization of primary hyperparathyroidism: a systematic review. Diagnostics, 14:25, Dec 2023. URL: https://doi.org/10.3390/diagnostics14010025, doi:10.3390/diagnostics14010025. This article has 10 citations.

40. (scheepers2023diagnosticperformanceof pages 2-4): Max H. M. C. Scheepers, Zaid Al-Difaie, Lloyd Brandts, Andrea Peeters, Bjorn Winkens, Mahdi Al-Taher, Sanne M. E. Engelen, Tim Lubbers, Bas Havekes, Nicole D. Bouvy, and Alida A. Postma. Diagnostic performance of magnetic resonance imaging for parathyroid localization of primary hyperparathyroidism: a systematic review. Diagnostics, 14:25, Dec 2023. URL: https://doi.org/10.3390/diagnostics14010025, doi:10.3390/diagnostics14010025. This article has 10 citations.

41. (costea2025tertiaryhyperparathyroidismin pages 10-12): Mirona Costea, D. Tilici, D. Păun, V. Nimigean, S. Paun, and R. Dǎnciulescu-Miulescu. Tertiary hyperparathyroidism in diabetic nephropathy: an underrecognized complication—a narrative review. Biomedicines, Oct 2025. URL: https://doi.org/10.3390/biomedicines13112604, doi:10.3390/biomedicines13112604. This article has 2 citations.

42. (chakrabarty2024imagingrecommendationsfor media 9629bfff): Nivedita Chakrabarty, Abhishek Mahajan, Sandip Basu, and Anil K. D’Cruz. Imaging recommendations for diagnosis and management of primary parathyroid pathologies: a comprehensive review. Cancers, 16:2593, Jul 2024. URL: https://doi.org/10.3390/cancers16142593, doi:10.3390/cancers16142593. This article has 25 citations.

43. (NCT03027557 chunk 2): Peter Vestergaard. Treatment of Primary Hyperparathyroidism With Denosumab and Cinacalcet.. Peter Vestergaard. 2017. ClinicalTrials.gov Identifier: NCT03027557

44. (costea2025tertiaryhyperparathyroidismin pages 9-10): Mirona Costea, D. Tilici, D. Păun, V. Nimigean, S. Paun, and R. Dǎnciulescu-Miulescu. Tertiary hyperparathyroidism in diabetic nephropathy: an underrecognized complication—a narrative review. Biomedicines, Oct 2025. URL: https://doi.org/10.3390/biomedicines13112604, doi:10.3390/biomedicines13112604. This article has 2 citations.

45. (vetter2024whatisthe pages 17-18): Diana Vetter and Thomas Schachtner. What is the role of surgery in secondary and tertiary hyperparathyroidism? Advances in Kidney Transplantation [Working Title], Aug 2024. URL: https://doi.org/10.5772/intechopen.1006528, doi:10.5772/intechopen.1006528. This article has 0 citations.

46. (sevva2024pharmaceuticalmanagementof pages 1-2): Christina Sevva, Dimitrios Divanis, Ariti Tsinari, Petros Grammenos, Styliani Laskou, Stylianos Mantalobas, Eleni Paschou, Vasiliki Magra, Periklis Kopsidas, Isaak Kesisoglou, Vassilios Liakopoulos, and Konstantinos Sapalidis. Pharmaceutical management of secondary hyperparathyroidism and the role of surgery: a 5-year retrospective study. Medicina, 60:812, May 2024. URL: https://doi.org/10.3390/medicina60050812, doi:10.3390/medicina60050812. This article has 3 citations.