---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T09:01:02.114120'
end_time: '2026-05-11T09:08:35.542852'
duration_seconds: 453.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tooth and Nail Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tooth and Nail Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Tooth and Nail Syndrome** covering all of the
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
- **Disease Name:** Tooth and Nail Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Tooth and Nail Syndrome** covering all of the
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


# Tooth and Nail Syndrome (Witkop Tooth-and-Nail Syndrome; TNS) — Disease Characteristics Report

## Target disease
- **Disease name:** Tooth and Nail Syndrome (Witkop tooth-and-nail syndrome)
- **Category:** Genetic; ectodermal dysplasia
- **MONDO ID:** Not identified in the retrieved evidence (requires external ontology lookup beyond the current corpus).

## Key references prioritized for recency
- McMillan KB et al. *Oral and Maxillofacial Surgery* (published online 2022; journal issue **Jul 2023**) — zygomatic implant rehabilitation case series (3 siblings; up to 15-year follow-up). https://doi.org/10.1007/s10006-022-01107-5 (mcmillan2023surgicalandprosthetic pages 1-2)
- Castilho NL et al. *Dentistry Journal* **Dec 2023** — systematic review of syndromes with oligodontia including Witkop syndrome. https://doi.org/10.3390/dj11120279 (castilho2023oligodontiainthe pages 13-15)
- Cammarata‑Scalisi F et al. *Clinical Oral Investigations* **Dec 2024** — review of genetic entities in tooth agenesis citing MSX1/Witkop and the implant case series. https://doi.org/10.1007/s00784-024-05941-7 (cammaratascalisi2024maingeneticentities pages 8-9)
- Jumlongras D et al. *American Journal of Human Genetics* **Jul 2001** — primary causal-variant paper identifying MSX1 S202X. https://doi.org/10.1086/321271 (jumlongras2001anonsensemutation pages 1-2)

## Artifact summary table
| Category | Finding | Details | Evidence |
|---|---|---|---|
| Preferred disease name | Tooth and Nail Syndrome | Also called Witkop syndrome; a rare ectodermal dysplasia primarily affecting teeth and nails | (memarpour2011witkoptoothand pages 3-5, memarpour2011witkoptoothand pages 1-3) |
| Synonyms / alternative names | Nomenclature | Witkop tooth-and-nail syndrome; tooth-and-nail syndrome (TNS); hypodontia-nail dysplasia syndrome; nail dysgenesis and hypodontia | (devadas2005witkoptoothand pages 1-3, memarpour2011witkoptoothand pages 5-5) |
| Inheritance | Mode of inheritance | Autosomal dominant | (memarpour2011witkoptoothand pages 3-5, bergqvist2017geneticsofsyndromic pages 4-4, jumlongras2001anonsensemutation pages 1-2) |
| Causal gene | Gene | **MSX1** | (memarpour2011witkoptoothand pages 1-3, jumlongras2001anonsensemutation pages 1-2) |
| Key variant evidence | Pathogenic variant example | Heterozygous nonsense variant **MSX1 S202X (Ser202Stop)** identified in an affected family; cosegregated with disease | (jumlongras2001anonsensemutation pages 1-2, jumlongras2001anonsensemutation pages 4-7) |
| OMIM identifier | OMIM | **189500** | (bergqvist2017geneticsofsyndromic pages 4-4) |
| Incidence estimate | Frequency | Reported as approximately **1–2 per 10,000** in some case literature; another report cites rarity without robust population-based confirmation | (altugatac2008witkoptoothand pages 1-2, devadas2005witkoptoothand pages 1-3, jumlongras2001anonsensemutation pages 1-2) |
| Core dental phenotype | Teeth | Congenital hypodontia/oligodontia; teeth may be widely spaced, conical, narrow-crowned; commonly missing mandibular incisors, second molars, and maxillary canines | (devadas2005witkoptoothand pages 1-3, memarpour2011witkoptoothand pages 1-3) |
| Core nail phenotype | Nails | Nail dysplasia with thin, brittle, spoon-shaped/ridged, slow-growing nails; toenails often more severely affected; nail changes may improve with age | (devadas2005witkoptoothand pages 1-3, memarpour2011witkoptoothand pages 1-3, bergqvist2017geneticsofsyndromic pages 4-4) |


*Table: This table summarizes the core nomenclature, identifiers, inheritance, genetic cause, incidence estimates, and hallmark tooth/nail manifestations of Tooth and Nail Syndrome based only on the retrieved evidence. It is useful as a compact reference for disease knowledge-base curation.*

---

## 1. Disease information

### 1.1 Overview (what is the disease?)
Tooth and Nail Syndrome (TNS), also called **Witkop syndrome**, is a **rare autosomal dominant ectodermal dysplasia** in which the abnormalities are largely restricted to **teeth (hypodontia/oligodontia, abnormal tooth shape)** and **nails (nail dysplasia)**. (jumlongras2001anonsensemutation pages 1-2, mcmillan2023surgicalandprosthetic pages 1-2)

The AJHG causal-variant paper explicitly summarizes the disorder as: “**Witkop syndrome, also known as tooth and nail syndrome (TNS), is a rare autosomal dominant disorder. Affected individuals have nail dysplasia and several congenitally missing teeth.**” (jumlongras2001anonsensemutation pages 1-2)

### 1.2 Synonyms and alternative names
- Witkop syndrome (memarpour2011witkoptoothand pages 1-3)
- Tooth and nail syndrome (TNS) (jumlongras2001anonsensemutation pages 1-2)
- Nail dysgenesis and hypodontia (jumlongras2001anonsensemutation pages 1-2, mcmillan2023surgicalandprosthetic pages 1-2)
- Hypodontia and nail dysplasia syndrome / tooth–nail dysplasia (bibliographic synonym evidence) (memarpour2011witkoptoothand pages 5-5)

### 1.3 Key identifiers
- **OMIM:** **189500** (explicitly shown as “TNS [MIM 189500]” in the AJHG paper and also listed in a nail-disorders genetics review) (jumlongras2001anonsensemutation pages 1-2, bergqvist2017geneticsofsyndromic pages 4-4)
- **Orphanet / ICD-10 / ICD-11 / MeSH / MONDO:** Not identified in the retrieved evidence; must be added via dedicated ontology/database lookup not available in this run.

### 1.4 Evidence source type
The available information is mostly from:
- **Aggregated genetics evidence** (linkage + sequencing; plus mouse model corroboration) (jumlongras2001anonsensemutation pages 1-2)
- **Family-based case series / case reports** and dental management publications (memarpour2011witkoptoothand pages 1-3, mcmillan2023surgicalandprosthetic pages 1-2)
- **Recent reviews and systematic review synthesis** of syndromic oligodontia (castilho2023oligodontiainthe pages 13-15, cammaratascalisi2024maingeneticentities pages 8-9)

---

## 2. Etiology

### 2.1 Primary causal factors
**Genetic etiology (germline):** The best-supported causal gene in the retrieved evidence is **MSX1**.
- A three-generation family study identified a heterozygous nonsense variant in MSX1 that cosegregated with disease. The abstract states that “**a heterozygous stop mutation in the homeodomain of MSX1 cosegregated with the phenotype**.” (jumlongras2001anonsensemutation pages 1-2)

### 2.2 Risk factors
- **Family history / autosomal dominant inheritance** is the major risk factor (jumlongras2001anonsensemutation pages 1-2, memarpour2011witkoptoothand pages 1-3).
- No environmental risk factors were identified in the retrieved evidence.

### 2.3 Protective factors
No genetic or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was identified in the retrieved evidence.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum
**Dental phenotypes**
- **Congenital hypodontia/oligodontia** with variable expressivity (jumlongras2001anonsensemutation pages 1-2, memarpour2011witkoptoothand pages 1-3).
- Commonly missing teeth (described in family case series): “**Mandibular incisors, second molars, and maxillary canines are the most frequently missing teeth.**” (abstract quote) (memarpour2011witkoptoothand pages 1-3)
- Tooth shape abnormalities: “**Tooth shape may vary, and conical and narrow crowns are common.**” (abstract quote) (memarpour2011witkoptoothand pages 1-3)
- The AJHG paper notes substantial variability but emphasizes that “**congenitally missing teeth and nail dysplasia are the consistent diagnostic features**” (jumlongras2001anonsensemutation pages 1-2).

**Nail phenotypes**
- Nail dysplasia affecting fingernails and especially toenails; often worse in childhood and may improve with age (jumlongras2001anonsensemutation pages 1-2, memarpour2011witkoptoothand pages 1-3).
- AJHG introduction provides detailed description: nails are “**thin, slow-growing, brittle, and spoon-shaped (koilonychia)**,” sometimes with “**marked longitudinal ridges and pitting**,” and “**Toenails are usually more severely affected than fingernails**.” (jumlongras2001anonsensemutation pages 1-2)
- Pediatric Dermatology abstract corroborates: nails “**may be spoon-shaped, ridged, slow-growing, and easily broken**.” (memarpour2011witkoptoothand pages 1-3)

### 3.2 Age of onset / temporal features
- Nail defects can be present at birth; AJHG notes that in rare cases “**nails … are absent at birth**,” and that “**nail defects … are alleviated with age**.” (jumlongras2001anonsensemutation pages 1-2)
- Some clinical literature suggests the condition is more often recognized in early childhood as tooth eruption patterns become apparent (case-based discussion) (devadas2005witkoptoothand pages 1-3).

### 3.3 Severity and progression
- **Variable expressivity** is explicitly reported (“**The expressivity of tooth and nail defects is highly variable**”). (jumlongras2001anonsensemutation pages 1-2)
- Nail findings may lessen with age and can be difficult to detect in adulthood. (jumlongras2001anonsensemutation pages 1-2, memarpour2011witkoptoothand pages 1-3)

### 3.4 Frequency among affected individuals
Because most available evidence is case/family series, robust phenotype frequencies are not available. However, quantitative data points include:
- In the AJHG family, one affected individual had **28 congenitally missing permanent teeth**. (jumlongras2001anonsensemutation pages 4-7)
- In a 2023 systematic review dataset, Witkop syndrome cases with MSX1 mutations showed an **average of 16.75 permanent teeth missing (four cases)**. (castilho2023oligodontiainthe pages 13-15)

### 3.5 Quality of life impact
TNS can lead to compromised aesthetics and function, and reduced quality of life due to missing/malformed teeth and atrophic jaws; the 2023 case series notes impacts on “**aesthetics, reduced function, and overall quality of life**” in the context of tooth absence and alveolar atrophy. (mcmillan2023surgicalandprosthetic pages 1-2)

### 3.6 Suggested HPO terms (non-exhaustive; mapping based on described phenotypes)
- Hypodontia / oligodontia (HP:0000668 / HP:0000677)
- Abnormality of tooth morphology; conical teeth (HP:0006482; conical incisors HP:0000698)
- Widely spaced teeth / diastema (HP:0000699)
- Koilonychia (HP:0001810)
- Nail dystrophy (HP:0002164)
- Onychorrhexis (brittle nails; often captured under nail dystrophy)

*Note: HPO IDs are suggested mappings; these ontology IDs were not directly provided in the retrieved texts and should be verified during curation.*

---

## 4. Genetic / molecular information

### 4.1 Causal gene(s)
- **MSX1** is the causal gene supported by linkage + sequencing and segregation evidence. (jumlongras2001anonsensemutation pages 1-2, jumlongras2001anonsensemutation pages 4-7)

### 4.2 Pathogenic variants (example)
- **MSX1 S202X (Ser202Stop)** (nonsense; premature stop) in the MSX1 homeodomain.
  - Evidence: “**a nonsense mutation (S202X) in MSX1 cosegregated with the TNS phenotype**” (jumlongras2001anonsensemutation pages 1-2)
  - Molecular detail: a “**C→A transversion at nucleotide position 605 in exon 2 … producing a premature stop codon (S202X / Ser202Stop)**” (jumlongras2001anonsensemutation pages 4-7)
  - Population control data: mutation absent from **132 normal control chromosomes** (implying very low allele frequency in controls). (jumlongras2001anonsensemutation pages 4-7)

**Variant class:** nonsense (loss-of-function consistent). (jumlongras2001anonsensemutation pages 4-7)

### 4.3 Somatic vs germline
The causal variant evidence is from inherited familial disease (germline). (jumlongras2001anonsensemutation pages 1-2)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No modifier gene, epigenetic, or chromosomal abnormality evidence specific to TNS was identified in the retrieved corpus.

---

## 5. Environmental information
No non-genetic contributing factors (toxins, lifestyle, infections) were identified in the retrieved evidence.

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (current evidence-based model)
1. **MSX1 loss-of-function** (e.g., nonsense variant truncating the homeodomain) (jumlongras2001anonsensemutation pages 4-7)
2. Disruption of developmental gene regulation in **ectodermal/mesenchymal interactions** critical for **tooth formation** and **nail development** (supported by expression and knockout data) (jumlongras2001anonsensemutation pages 1-2)
3. Clinical manifestations:
   - **Tooth agenesis** and tooth-shape abnormalities (jumlongras2001anonsensemutation pages 1-2, memarpour2011witkoptoothand pages 1-3)
   - **Nail plate dysplasia** (thin, brittle, koilonychia, ridging) (jumlongras2001anonsensemutation pages 1-2, memarpour2011witkoptoothand pages 1-3)

### 6.2 Supporting model-organism evidence
The AJHG paper reports that Msx1 knockout mice show both tooth and nail phenotypes: “**not only was tooth development disrupted … but nail development was affected as well. Nail plates in Msx1-null mice were defective and were thinner than those of their wild-type littermates.**” (jumlongras2001anonsensemutation pages 1-2)

### 6.3 Suggested GO biological process terms (to be curated/validated)
- Tooth development / odontogenesis (GO:0042476)
- Epithelial cell differentiation / keratinization processes relevant to nail plate formation

### 6.4 Suggested CL terms (cell types; to be curated/validated)
- Odontoblast (CL:0000069)
- Ameloblast (CL:0000031)
- Keratinocyte (CL:0000312)

*Note: GO/CL terms are suggested mappings; they are not explicitly listed in the retrieved papers and should be validated.*

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue level
- **Teeth / dentition** (primary and/or permanent) (jumlongras2001anonsensemutation pages 1-2)
- **Nails** (finger and toe; toenails often more affected) (jumlongras2001anonsensemutation pages 1-2, memarpour2011witkoptoothand pages 1-3)
- Severe **maxillary alveolar atrophy** can occur secondary to missing dentition (notably in severe cases requiring complex implant solutions). (mcmillan2023surgicalandprosthetic pages 1-2)

### 7.2 Suggested UBERON terms (to be curated/validated)
- Tooth (UBERON:0001091)
- Nail (UBERON:0001828)
- Maxilla (UBERON:0002397)

---

## 8. Temporal development
- **Onset:** congenital/early childhood; nails may be abnormal/absent at birth in rare cases (jumlongras2001anonsensemutation pages 1-2); dental agenesis becomes evident as eruption fails (memarpour2011witkoptoothand pages 1-3).
- **Course:** lifelong dental agenesis; nail abnormalities may **improve with age**. (jumlongras2001anonsensemutation pages 1-2, memarpour2011witkoptoothand pages 1-3)

---

## 9. Inheritance and population

### 9.1 Inheritance
- **Autosomal dominant** (jumlongras2001anonsensemutation pages 1-2, memarpour2011witkoptoothand pages 1-3)
- Expressivity is “highly variable.” (jumlongras2001anonsensemutation pages 1-2)

### 9.2 Epidemiology statistics (limited)
- Incidence estimates reported in multiple sources: approximately **~1–2 per 10,000** (jumlongras2001anonsensemutation pages 1-2, memarpour2011witkoptoothand pages 1-3, mcmillan2023surgicalandprosthetic pages 1-2). These appear to be historical estimates rather than modern population-based studies.

No robust prevalence/incidence studies by geography/ancestry or sex ratio were identified in the retrieved evidence.

---

## 10. Diagnostics

### 10.1 Clinical and radiographic diagnosis
Diagnosis is typically based on:
- Clinical examination documenting the combination of **congenitally missing teeth** and **nail dysplasia** (jumlongras2001anonsensemutation pages 1-2)
- **Dental radiographs** to confirm absence of tooth germs/eruption failure (family case series used clinical + radiographic evaluation). (memarpour2011witkoptoothand pages 1-3)

### 10.2 Genetic testing
- **Targeted sequencing of MSX1** can provide molecular confirmation, supported by the known causal nonsense variant and segregation evidence. (jumlongras2001anonsensemutation pages 1-2, jumlongras2001anonsensemutation pages 4-7)

### 10.3 Differential diagnosis
The 2023 case series places Witkop syndrome within a broader ectodermal dysplasia differential (e.g., Fried syndrome, Clouston syndrome). (mcmillan2023surgicalandprosthetic pages 1-2)

### 10.4 Standardized diagnostic criteria
No formal consensus criteria were identified in the retrieved evidence.

---

## 11. Outcome / prognosis
- The condition is typically limited to teeth and nails; most affected individuals reported have normal hair and sweat gland function (jumlongras2001anonsensemutation pages 1-2, memarpour2011witkoptoothand pages 1-3).
- Nail findings may improve with age (jumlongras2001anonsensemutation pages 1-2, memarpour2011witkoptoothand pages 1-3).
- Long-term functional outcomes depend heavily on dental rehabilitation; modern implant-based prosthodontics can provide durable restoration in severe adult cases (mcmillan2023surgicalandprosthetic pages 1-2).

No mortality or survival impacts were identified in the retrieved evidence.

---

## 12. Treatment

### 12.1 Current applications / real-world implementations
Treatment is **supportive and multidisciplinary**.

**Dental rehabilitation**
- Multidisciplinary dental care is emphasized for missing teeth and functional/aesthetic outcomes (pediatric dentists, orthodontists, surgeons, prosthodontists). (mcmillan2023surgicalandprosthetic pages 1-2)
- Early restorative approaches in children can include interim prostheses and ongoing adjustments during growth (case-series management approach). (memarpour2011witkoptoothand pages 3-5)

**Implant-supported rehabilitation (recent development)**
- A key recent development is use of **zygomatic implants** for severe maxillary atrophy in ectodermal dysplasia/Witkop syndrome.
  - McMillan et al. report a **familial case series of 3 siblings** treated with zygomatic implants and prosthetic rehabilitation with **follow-up up to 15 years**. (mcmillan2023surgicalandprosthetic pages 1-2)
  - Reported follow-up detail: patients were surveilled on a **6-month recall** schedule for 15 years and had “**no significant implant pathology with minor bone loss to the first thread**” and patient satisfaction with aesthetics/function/longevity. (mcmillan2023surgicalandprosthetic pages 1-2)

### 12.2 Pharmacotherapy
No disease-modifying pharmacotherapy was identified in the retrieved evidence.

### 12.3 Suggested MAXO terms (to be curated/validated)
- Dental prosthesis placement
- Dental implant insertion
- Orthodontic treatment
- Genetic counseling

*Note: MAXO IDs were not provided in the retrieved evidence and should be assigned during ontology curation.*

---

## 13. Prevention
- No primary prevention is available for this monogenic condition.
- **Genetic counseling** is recommended in case-based literature due to autosomal dominant inheritance and multi-generational transmission. (memarpour2011witkoptoothand pages 3-5, memarpour2011witkoptoothand pages 1-3)

---

## 14. Other species / natural disease
No naturally occurring veterinary analogs were identified in the retrieved evidence.

---

## 15. Model organisms
- **Msx1 knockout mouse** is directly relevant and recapitulates aspects of both tooth and nail defects (defective thinner nail plates; disrupted tooth development). (jumlongras2001anonsensemutation pages 1-2)

---

## Expert opinion / analysis (synthesis of authoritative sources)

1. **MSX1 is a high-confidence causal gene** for tooth-and-nail syndrome because the human familial segregation of a truncating homeodomain variant is supported by mechanistic plausibility and an aligned mouse phenotype (tooth and nail developmental defects). (jumlongras2001anonsensemutation pages 1-2, jumlongras2001anonsensemutation pages 4-7)
2. **Modern rehabilitation is increasingly implant-centered in adults**, and the 2023 long-follow-up case series suggests that zygomatic implant strategies can reduce the need for repeated extensive grafting in severely atrophic maxillae while maintaining long-term function. (mcmillan2023surgicalandprosthetic pages 1-2)
3. **Phenotypic variability is substantial**, so diagnosis should integrate teeth+nails findings and family history rather than dental findings alone; oligodontia overlaps with many syndromes and demands careful syndromic evaluation (supported by the systematic review context). (jumlongras2001anonsensemutation pages 1-2, castilho2023oligodontiainthe pages 13-15)

---

## Data availability / limitations of this report
- Several requested identifiers (MONDO, Orphanet, MeSH, ICD-10/11) were not present in the retrieved full texts and therefore could not be cited here.
- Many epidemiologic statistics appear to be historical estimates rather than modern population-based studies.
- Most clinical evidence is from case reports/series; randomized trials and formal guidelines specific to Witkop/TNS were not retrieved.


References

1. (mcmillan2023surgicalandprosthetic pages 1-2): Kale B. McMillan, Dane C. McMillan, Kevin Arce, and Thomas J. Salinas. Surgical and prosthetic rehabilitation of siblings with witkop tooth and nail syndrome using zygomatic implants: a familial case series of 3 patients with up to 15-year follow-up. Oral and Maxillofacial Surgery, 27:711-719, Jul 2023. URL: https://doi.org/10.1007/s10006-022-01107-5, doi:10.1007/s10006-022-01107-5. This article has 4 citations and is from a peer-reviewed journal.

2. (castilho2023oligodontiainthe pages 13-15): Natália Lopes Castilho, Kêmelly Karolliny Moreira Resende, Juliana Amorim dos Santos, Renato Assis Machado, Ricardo D. Coletta, Eliete Neves Silva Guerra, Ana Carolina Acevedo, and Hercílio Martelli-Junior. Oligodontia in the clinical spectrum of syndromes: a systematic review. Dentistry Journal, 11:279, Dec 2023. URL: https://doi.org/10.3390/dj11120279, doi:10.3390/dj11120279. This article has 12 citations and is from a peer-reviewed journal.

3. (cammaratascalisi2024maingeneticentities pages 8-9): Francisco Cammarata-Scalisi, Colin E. Willoughby, Jinia R. El-Feghaly, Antonio Cárdenas Tadich, Maykol Araya Castillo, Shadi Alkhatib, Marwa Abd Elsalam Elsherif, Rabab K. El-Ghandour, Riccardo Coletta, Antonino Morabito, and Michele Callea. Main genetic entities associated with tooth agenesis. Clinical oral investigations, 29 1:9, Dec 2024. URL: https://doi.org/10.1007/s00784-024-05941-7, doi:10.1007/s00784-024-05941-7. This article has 8 citations and is from a domain leading peer-reviewed journal.

4. (jumlongras2001anonsensemutation pages 1-2): Dolrudee Jumlongras, Marianna Bei, Jean M. Stimson, Wen-Fang Wang, Steven R. DePalma, Christine E. Seidman, Ute Felbor, Richard Maas, Jonathan G. Seidman, and Bjorn R. Olsen. A nonsense mutation in msx1 causes witkop syndrome. American journal of human genetics, 69 1:67-74, Jul 2001. URL: https://doi.org/10.1086/321271, doi:10.1086/321271. This article has 346 citations and is from a highest quality peer-reviewed journal.

5. (memarpour2011witkoptoothand pages 3-5): Mahtab Memarpour and Fereshteh Shafiei. Witkop tooth and nail syndrome: a report of three cases in a family. Pediatric Dermatology, 28:281-285, May 2011. URL: https://doi.org/10.1111/j.1525-1470.2010.01198.x, doi:10.1111/j.1525-1470.2010.01198.x. This article has 21 citations and is from a peer-reviewed journal.

6. (memarpour2011witkoptoothand pages 1-3): Mahtab Memarpour and Fereshteh Shafiei. Witkop tooth and nail syndrome: a report of three cases in a family. Pediatric Dermatology, 28:281-285, May 2011. URL: https://doi.org/10.1111/j.1525-1470.2010.01198.x, doi:10.1111/j.1525-1470.2010.01198.x. This article has 21 citations and is from a peer-reviewed journal.

7. (devadas2005witkoptoothand pages 1-3): S. DEVADAS, B. VARMA, J. MUNGARA, T. JOSEPH, and T. R. SARASWATHI. Witkop tooth and nail syndrome: a case report. International journal of paediatric dentistry, 15 5:364-9, Sep 2005. URL: https://doi.org/10.1111/j.1365-263x.2005.00647.x, doi:10.1111/j.1365-263x.2005.00647.x. This article has 15 citations and is from a domain leading peer-reviewed journal.

8. (memarpour2011witkoptoothand pages 5-5): Mahtab Memarpour and Fereshteh Shafiei. Witkop tooth and nail syndrome: a report of three cases in a family. Pediatric Dermatology, 28:281-285, May 2011. URL: https://doi.org/10.1111/j.1525-1470.2010.01198.x, doi:10.1111/j.1525-1470.2010.01198.x. This article has 21 citations and is from a peer-reviewed journal.

9. (bergqvist2017geneticsofsyndromic pages 4-4): Christina Bergqvist, P. Ramia, O. Abbas, M. Kurban, and M. Kurban. Genetics of syndromic and non‐syndromic hereditary nail disorders. Clinical Genetics, 91:813-823, Jun 2017. URL: https://doi.org/10.1111/cge.12852, doi:10.1111/cge.12852. This article has 5 citations and is from a peer-reviewed journal.

10. (jumlongras2001anonsensemutation pages 4-7): Dolrudee Jumlongras, Marianna Bei, Jean M. Stimson, Wen-Fang Wang, Steven R. DePalma, Christine E. Seidman, Ute Felbor, Richard Maas, Jonathan G. Seidman, and Bjorn R. Olsen. A nonsense mutation in msx1 causes witkop syndrome. American journal of human genetics, 69 1:67-74, Jul 2001. URL: https://doi.org/10.1086/321271, doi:10.1086/321271. This article has 346 citations and is from a highest quality peer-reviewed journal.

11. (altugatac2008witkoptoothand pages 1-2): Ayse T. Altug-Atac and Haluk Iseri. Witkop tooth and nail syndrome and orthodontics. The Angle orthodontist, 78 2:370-80, Mar 2008. URL: https://doi.org/10.2319/100406-403.1, doi:10.2319/100406-403.1. This article has 19 citations.