---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T10:51:23.974678'
end_time: '2026-05-09T11:06:46.978319'
duration_seconds: 923.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Opitz G/BBB syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Opitz G/BBB syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Opitz G/BBB syndrome** covering all of the
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
- **Disease Name:** Opitz G/BBB syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Opitz G/BBB syndrome** covering all of the
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


# Opitz G/BBB syndrome (Opitz syndrome; telecanthus-hypospadias syndrome): Disease characteristics research report

## Target disease
- **Disease name:** Opitz G/BBB syndrome (also “Opitz syndrome,” “telecanthus-hypospadias syndrome,” “BBB syndrome,” “G syndrome,” “Opitz-Frias syndrome”) (baldini2019understandingthemolecular pages 97-101, vagha2023ararecase pages 1-5)
- **Category:** Mendelian / multiple congenital anomaly syndrome with midline developmental defects (migliore2022specc1lmutationsare pages 1-2, micale2023opitzsyndromeimproving pages 1-2)
- **MONDO ID:** *Not found in retrieved sources* (see Limitations)

---

## 1) Disease information

### Definition and current understanding
Opitz G/BBB syndrome (OS) is a rare, genetically heterogeneous congenital malformation syndrome in which **midline structures are primarily affected**, classically presenting with **hypertelorism/telecanthus** and **genitourinary anomalies (especially hypospadias in males)**, with variable involvement of the airway/foregut, heart, anorectal region, and central nervous system (migliore2022specc1lmutationsare pages 1-2, micale2023opitzsyndromeimproving pages 1-2).

A 2023 peer-reviewed review in *Pediatric Research* summarizes OS as “a rare, genetically heterogeneous disorder that primarily affects midline structures,” listing key features including hypertelorism/telecanthus, cleft lip/palate, laryngo-tracheo-esophageal anomalies, congenital heart defects, anorectal anomalies, and hypospadias (micale2023opitzsyndromeimproving pages 1-2).  

### Key identifiers (from retrieved evidence)
- **OMIM/“MIM” disease IDs:** 300000 (X-linked), 145410 (autosomal dominant) (migliore2022specc1lmutationsare pages 1-2, wang2025heartfailurecaused pages 1-3, sarno2021firsttrimesterultrasound pages 1-3)
- **MID1 gene OMIM/“MIM”:** 300552 (migliore2022specc1lmutationsare pages 1-2, sarno2021firsttrimesterultrasound pages 1-3)
- **Orphanet / ICD-10 / ICD-11 / MeSH / MONDO:** *Not found in retrieved sources*.

### Synonyms and alternative names
Synonyms reported in the retrieved sources include: **BBB syndrome, G syndrome, Opitz-G, Opitz-Frias**, and **telecanthus-hypospadias syndrome** (baldini2019understandingthemolecular pages 97-101).

### Evidence provenance
The retrieved evidence is primarily from **aggregated disease-level resources and literature synthesis** (peer-reviewed review/research articles) plus **case reports** and **prenatal case studies** (micale2023opitzsyndromeimproving pages 1-2, sarno2021firsttrimesterultrasound pages 1-3, vagha2023ararecase pages 1-5).

---

## 2) Etiology

### Disease causal factors
**Primary cause:** germline genetic variants affecting midline development.

**Genetic heterogeneity and subtypes**
- **X-linked Opitz G/BBB syndrome (XLOS):** due to hemizygous pathogenic variants in **MID1** (also referred to as **TRIM18**) at **Xp22.2** (migliore2022specc1lmutationsare pages 1-2, micale2023opitzsyndromeimproving pages 1-2). 
- **Autosomal dominant Opitz G/BBB / “type 2” historical locus:** linked to **22q11.2 genomic losses**; some families reported with **SPECC1L** pathogenic variants at **22q11.23** (migliore2022specc1lmutationsare pages 1-2, bhoj2019phenotypicspectrumassociated pages 1-5). Multiple sources emphasize that SPECC1L-associated disease may be better conceptualized as a partially overlapping, distinct “SPECC1L syndrome” rather than canonical Opitz G/BBB (migliore2022specc1lmutationsare pages 1-2, bhoj2019phenotypicspectrumassociated pages 1-5).

### Risk factors
- **Sex:** X-linked form predominates in males; female carriers can be mildly affected (often hypertelorism only) but severe fetal female presentations have been reported, potentially influenced by X-inactivation (tessier2020hydrothoraxinfetal pages 1-2).
- **Family history:** in XLOS, carrier mothers are common (listyasari2022clinicallessonlearned pages 3-3).

No environmental/toxic/infectious risk factors were identified in the retrieved sources.

### Protective factors / gene–environment interactions
No protective factors or gene–environment interactions were identified in the retrieved sources.

---

## 3) Phenotypes (with HPO suggestions)

### Core phenotype spectrum (MID1-related Opitz G/BBB)
Across review and case-based evidence, the most recurrent features are:

1) **Ocular hypertelorism / telecanthus**  
- **Type:** clinical sign / craniofacial dysmorphism  
- **HPO:** HP:0000316 (Hypertelorism), HP:0000506 (Telecanthus)  
- **Notes/frequency:** described as a main sign (migliore2022specc1lmutationsare pages 1-2). 

2) **Hypospadias (and other male genital anomalies)**  
- **Type:** congenital urogenital malformation  
- **HPO:** HP:0000047 (Hypospadias), HP:0000028 (Cryptorchidism), HP:0000033 (Bifid scrotum)  
- **Notes:** listed among major findings of OS (migliore2022specc1lmutationsare pages 1-2). 

3) **Laryngo–tracheo–esophageal defects** (including laryngeal cleft / TE fistula in some descriptions)  
- **Type:** congenital airway/foregut malformations  
- **HPO (examples):** HP:0008750 (Laryngeal cleft), HP:0100835 (Tracheoesophageal fistula), HP:0002776 (Feeding difficulties)  
- **Notes:** emphasized as “main clinical signs” in an OS genetics review (migliore2022specc1lmutationsare pages 1-2). 

4) **Cleft lip and/or palate**  
- **Type:** craniofacial malformation  
- **HPO:** HP:0000204 (Cleft upper lip), HP:0000175 (Cleft palate)  
- **Frequency (reported in a 2023 case-report synthesis):** “over half” of individuals had cleft lip/palate (vagha2023ararecase pages 1-5).

5) **Congenital heart defects**  
- **Type:** structural cardiovascular malformations  
- **HPO (examples):** HP:0001629 (Ventricular septal defect), HP:0001631 (Atrial septal defect), HP:0001708 (Coarctation of aorta), HP:0001643 (Patent ductus arteriosus)  
- **Notes:** CHD is repeatedly listed in OS clinical summaries (migliore2022specc1lmutationsare pages 1-2, vagha2023ararecase pages 1-5).

6) **Anorectal anomalies (imperforate/ectopic anus)**  
- **Type:** gastrointestinal malformation  
- **HPO:** HP:0002023 (Anal atresia) / HP:0002037 (Anorectal malformation)  
- **Notes:** described in multiple OS summaries (migliore2022specc1lmutationsare pages 1-2).

7) **Central nervous system malformations and neurodevelopmental phenotype**  
- **Type:** congenital CNS malformations + neurodevelopmental disorder  
- **HPO (examples):** HP:0001274 (Agenesis of corpus callosum), HP:0001305 (Dandy-Walker malformation), HP:0002079 (Ventriculomegaly), HP:0001263 (Global developmental delay), HP:0001249 (Intellectual disability)  
- **Frequency:** developmental delay reported as ~one-third of affected males in a fetal-case letter (tessier2020hydrothoraxinfetal pages 1-2) and about 50% in a prenatal case report/review (sarno2021firsttrimesterultrasound pages 1-3), indicating variability and/or ascertainment differences.

8) **Rare fetal/early-life features expanding phenotype**
- **Fetal hydrothorax** has been proposed as a rare additional prenatal feature based on two fetal cases with de novo MID1 variants (tessier2020hydrothoraxinfetal pages 1-2).

### SPECC1L-related (autosomal dominant) phenotype (overlap and distinctions)
A critical nosology review emphasizes that **SPECC1L-related disease overlaps** with Opitz-like craniofacial findings (hypertelorism, prominent forehead, broad nasal bridge, anteverted nares, cleft lip/palate), but **canonical laryngeal malformations and male genital anomalies are reportedly absent** in SPECC1L cohorts (bhoj2019phenotypicspectrumassociated pages 1-5). Instead, characteristic findings include:
- **Branchial fistulae** (HPO: HP:0009794) 
- **Omphalocele / abdominal wall defects** (HPO: HP:0001539) 
- **Congenital diaphragmatic hernia (CDH)** (HPO: HP:0000776) 
- **Müllerian anomalies such as bicornuate uterus/uterus didelphys** (HPO: HP:0000136 / HP:0000130)  
These are specifically emphasized in a 2020 *AJMG A* paper concluding that “SPECC1L is a bona fide CDH gene” and recommending consideration of SPECC1L-related Opitz-like syndrome in CDH patients with compatible craniofacial findings (wild2020congenitaldiaphragmatichernia pages 1-2).

### Quality of life impact
Quality-of-life instruments (e.g., EQ-5D/SF-36) were not reported in the retrieved sources. Clinical impact is inferred from multisystem anomalies requiring multidisciplinary care and surgical interventions (vagha2023ararecase pages 1-5).

---

## 4) Genetic / molecular information

### Causal genes
- **MID1 (TRIM18)** — X-linked form (Xp22.2) (migliore2022specc1lmutationsare pages 1-2, micale2023opitzsyndromeimproving pages 1-2)
- **SPECC1L** — reported in autosomal dominant families with Opitz-like phenotypes (22q11.23) (micale2023opitzsyndromeimproving pages 1-2, bhoj2019phenotypicspectrumassociated pages 1-5)

### Pathogenic variant classes (MID1)
MID1 disease-causing variants are distributed across the locus and include **missense, nonsense, indels/frameshifts, splice variants, and large deletions/duplications** (baldini2019understandingthemolecular pages 9-13, micale2023opitzsyndromeimproving pages 1-2). A 2023 diagnostic-focused review notes: “MID1 is not expressed in blood and mRNA studies are hardly accessible in routine diagnostics,” and highlights minigene assays for splicing effects (micale2023opitzsyndromeimproving pages 1-2).

**Observed/implicated mechanism:** Many MID1 alleles are predicted loss-of-function (LoF), and LoF is stated to be the likely mechanism in a genetic heterogeneity review (migliore2022specc1lmutationsare pages 1-2).

### Population frequency / carrier frequency
Allele frequencies in gnomAD or similar resources were not extractable from the retrieved sources.

### Modifier genes / epigenetics
A review notes phenotypic variability and mentions possible interactions between MID1 and MID2 in shaping phenotype (migliore2022specc1lmutationsare pages 8-10), but no specific validated modifier variants were extractable from the retrieved sources.

---

## 5) Environmental information
No specific environmental or lifestyle contributors were identified in the retrieved sources.

---

## 6) Mechanism / pathophysiology

### Key molecular functions of MID1 relevant to disease
MID1 is a **TRIM family E3 ubiquitin ligase** that associates with **microtubules** and forms complexes affecting signaling and translation (baldini2019understandingthemolecular pages 13-18, baldini2019understandingthemolecular pages 9-13). Mechanistic summaries in the retrieved sources support the following chain:

**Upstream genetic lesion → MID1 loss/dysfunction → PP2A dysregulation and microtubule/RNP perturbation → altered developmental patterning and tissue fusion → midline malformations**.

Key mechanistic elements:
- **MID1–PP2A axis and translation control:** MID1 ubiquitinates components of the PP2A regulatory axis, and loss/depletion of MID1 increases PP2A and can disrupt **mTORC1 signaling**, consistent with a MID1–PP2A–mTOR functional axis (baldini2019understandingthemolecular pages 13-18).
- **Microtubule association:** MID1 microtubule binding depends on the C-terminal region (B30.2/COS/PRY-SPRY-containing), and truncating variants can disrupt microtubule association and transport (baldini2019understandingthemolecular pages 9-13). In a 2024 human organoid paper, a C-terminal patient variant affecting the B30.2 region “showed no filamentous organization and no co-localization with the microtubule cytoskeleton” (frank2024absenceofthe pages 2-4).

### 2024 organoid and transcriptomic evidence (recent development)
A key 2024 advance is the use of genome-edited **human iPSC-derived brain organoids** to interrogate MID1 isoform-function: the Life Science Alliance paper reports that absence of RING-domain-containing MID1 isoforms causes early patterning defects and neurogenic deficits, with transcriptome deregulation preceding neural induction (frank2024absenceofthe pages 1-2, frank2024absenceofthe pages 2-4). The figures directly illustrate reduced neural tissue, PCA transcriptome separation, and expanded choroid plexus-like (TTR-positive) structures (frank2024absenceofthe media 7494b3f8, frank2024absenceofthe media 8e0af7e5, frank2024absenceofthe media f851948f, frank2024absenceofthe media 42fc7635).

### Suggested ontology mappings (mechanism)
- **GO biological process (examples):**
  - GO:0007275 (multicellular organism development)
  - GO:0007067 (mitotic nuclear division) / broader neurogenesis-related processes (supported by organoid “neurogenic deficit”) (frank2024absenceofthe pages 2-4)
  - GO:0016567 (protein ubiquitination) (supported by MID1 E3 ligase function) (baldini2019understandingthemolecular pages 13-18, frank2024absenceofthe pages 1-2)
  - GO:0008017 (microtubule binding) / GO:0007018 (microtubule-based movement) (supported by MID1 microtubule association/transport) (baldini2019understandingthemolecular pages 9-13)
  - GO:0032008 (positive regulation of TOR signaling) / GO:0031929 (TOR signaling) (supported by MID1–PP2A–mTORC1 axis) (baldini2019understandingthemolecular pages 13-18, frank2024absenceofthe pages 1-2)
- **GO cellular component (examples):**
  - GO:0005874 (microtubule)
  - GO:0005829 (cytosol)
- **Cell Ontology (CL) (examples for neurodevelopmental context):**
  - CL:0000540 (neuron)
  - CL:0000679 (glial cell) / CL:0000127 (astrocyte) (as downstream candidate; not directly enumerated in retrieved evidence)
  - CL:0000125 (ventricular zone neural progenitor / broadly neural stem/progenitor) consistent with organoid VZ-like regions (frank2024absenceofthe pages 2-4)
- **UBERON (examples):**
  - UBERON:0000955 (brain)
  - UBERON:0001893 (cerebellum) (supported by cerebellar vermis anomalies) (baldini2019understandingthemolecular pages 9-13, tessier2020hydrothoraxinfetal pages 1-2)
  - UBERON:0002367 (larynx), UBERON:0003126 (trachea), UBERON:0001043 (esophagus) (supported by laryngo-tracheo-esophageal malformations) (migliore2022specc1lmutationsare pages 1-2)
  - UBERON:0000056 (urethra/urogenital tract) (supported by hypospadias and genital anomalies) (migliore2022specc1lmutationsare pages 1-2)

### Immune system involvement
No human OS immunophenotyping evidence was found in the retrieved sources. (A 2024 EAE model paper links Mid1 to T cell migration via mTOR/microtubule pathways, but this is not presented as OS pathogenesis evidence.) (wei2024midline1regulateseffector pages 13-13).

---

## 7) Anatomical structures affected
**Primary systems:** craniofacial midline, urogenital, airway/foregut, cardiovascular, CNS (migliore2022specc1lmutationsare pages 1-2).

**Examples (UBERON):**
- Face/craniofacial region (hypertelorism; clefting)
- Larynx–trachea–esophagus axis (laryngo-tracheo-esophageal anomalies) (migliore2022specc1lmutationsare pages 1-2)
- Heart (congenital heart defects) (migliore2022specc1lmutationsare pages 1-2)
- Brain (corpus callosum/cerebellar vermis anomalies) (migliore2022specc1lmutationsare pages 1-2, tessier2020hydrothoraxinfetal pages 1-2)

---

## 8) Temporal development
**Onset:** typically **congenital**; many features detectable prenatally (sarno2021firsttrimesterultrasound pages 1-3, tessier2020hydrothoraxinfetal pages 1-2).

**Prenatal imaging findings (examples):**
- First-trimester ultrasound (12 weeks) in XLOS: increased nuchal translucency, heart defects, cleft lip/palate, enlarged fourth ventricle, absence of ductus venosus (sarno2021firsttrimesterultrasound pages 1-3).
- Fetal hydrothorax/hydrops in MID1 de novo cases at ~24–25 weeks, with clefting and CNS anomalies (tessier2020hydrothoraxinfetal pages 1-2).

Course is typically lifelong, with outcomes depending on severity of airway/cardiac/CNS involvement (vagha2023ararecase pages 1-5).

---

## 9) Inheritance and population

### Inheritance
- **X-linked** (MID1): males primarily affected; heterozygous females can be mildly affected and may show hypertelorism (tessier2020hydrothoraxinfetal pages 1-2, listyasari2022clinicallessonlearned pages 3-3).
- **Autosomal dominant** (22q11.2 losses; SPECC1L in some families): reported in the literature and discussed as a distinct but overlapping spectrum (migliore2022specc1lmutationsare pages 1-2, bhoj2019phenotypicspectrumassociated pages 1-5).

### Epidemiology
Two sources cite a male incidence of approximately **1:50,000–1:100,000** for X-linked Opitz G/BBB syndrome (sarno2021firsttrimesterultrasound pages 1-3, vagha2023ararecase pages 5-6).  

**Diagnostic yield statistic:** MID1 pathogenic variants were reported to explain **~20–30% of screened OS cases** in one review, highlighting genetic heterogeneity and the need for broader testing when MID1 is negative (migliore2022specc1lmutationsare pages 1-2).

---

## 10) Diagnostics

### Clinical recognition
Suspicion arises from the combination of hypertelorism/telecanthus with hypospadias and/or airway/foregut malformations, often with clefting and CHD (migliore2022specc1lmutationsare pages 1-2, vagha2023ararecase pages 1-5).

### Genetic testing approaches (evidence-based elements)
- **MID1 sequencing (XLOS):** standard approach when X-linked phenotype suspected; family segregation helps interpret uncertain variants (listyasari2022clinicallessonlearned pages 3-3).
- **CNV/structural variant testing:** OS can be caused by “whole gene or intragenic large deletions” of MID1 (micale2023opitzsyndromeimproving pages 1-2). In prenatal evaluation, chromosomal microarray (aCGH) was used before confirming a familial MID1 variant (sarno2021firsttrimesterultrasound pages 1-3).
- **Splicing/intronic variant interpretation:** A 2023 paper emphasizes the diagnostic challenge that “MID1 is not expressed in blood,” and supports **minigene assays** to functionally test intronic/splice-altering variants for ACMG/AMP classification (micale2023opitzsyndromeimproving pages 1-2).
- **22q11.2 evaluation / SPECC1L testing:** autosomal dominant cases may involve 22q11.2 genomic losses; SPECC1L pathogenic variants are reported in some families but are “not common in sporadic cases,” and missense interpretation can be challenging (migliore2022specc1lmutationsare pages 1-2).

### Prenatal diagnostics
When a familial MID1 variant is known, prenatal genetic testing (e.g., chorionic villus sampling with targeted PCR) can enable early molecular diagnosis (sarno2021firsttrimesterultrasound pages 1-3).

### Differential diagnosis (from retrieved sources)
SPECC1L-related phenotypes overlap with Teebi hypertelorism and Baraitser–Winter spectrum; the literature explicitly discusses nosology and overlap, emphasizing that SPECC1L cases may lack canonical laryngeal and male genital findings (bhoj2019phenotypicspectrumassociated pages 1-5, migliore2022specc1lmutationsare pages 1-2).

---

## 11) Outcome / prognosis
Prognosis depends on severity of airway/feeding complications, congenital heart disease, and CNS involvement (vagha2023ararecase pages 1-5). Severe cardiac involvement can occur; a 2025 case report describes heart failure in a patient with MID1-related OS (wang2025heartfailurecaused pages 1-3). Quantitative survival or life-expectancy estimates were not found in the retrieved sources.

---

## 12) Treatment / management (applications and real-world implementation)

No disease-specific pharmacotherapy was identified in the retrieved sources; management is primarily **supportive and surgical**, tailored to malformations.

### Surgical/interventional management (examples)
- **Hypospadias repair** often requires staged surgery; a 2023 clinical case underscores coordinated care across pediatrics, urology/pediatric surgery, cardiology, and craniofacial surgery (vagha2023ararecase pages 1-5).

### Supportive/multidisciplinary care
A 2023 clinical summary stresses “multidisciplinary” evaluation and attention to cardiovascular, neurologic, and respiratory involvement (vagha2023ararecase pages 5-6).

### Experimental/clinical trials
No interventional trials specific to Opitz G/BBB syndrome were identified in the retrieved trial set. One trial was retrieved for **22q11.2 deletion syndrome** (NCT05149898; completed Phase 2; transdermal cannabidiol gel), which may be relevant to a subset of autosomal dominant Opitz-like presentations linked to 22q11.2; however, this is not an Opitz-specific trial and no Opitz subgroup results were available from retrieved evidence.

### MAXO suggestions (management actions; conceptual mapping)
- MAXO:0000495 (surgical repair of congenital anomaly) — e.g., hypospadias repair, cleft repair
- MAXO:0000747 (genetic counseling)
- MAXO:0000127 (diagnostic genetic testing)
- MAXO:0001020 (multidisciplinary care)

---

## 13) Prevention
Primary prevention is not established because the disorder is genetic. Prevention in practice is **reproductive risk management**:
- **Genetic counseling and cascade testing** in families with known MID1 variants (listyasari2022clinicallessonlearned pages 3-3).
- **Prenatal diagnosis** when familial mutation is known (sarno2021firsttrimesterultrasound pages 1-3).

---

## 14) Other species / natural disease
No naturally occurring veterinary syndrome explicitly corresponding to Opitz G/BBB was identified in the retrieved sources.

---

## 15) Model organisms
A MID1 knockout mouse model is described as reproducing key neuroanatomical features: Mid1 knockout (Mid1-/Y) mice show cerebellar abnormalities consistent with patient findings, with defects evident during embryogenesis (baldini2019understandingthemolecular pages 1-9, baldini2019understandingthemolecular pages 9-13). Mechanistic investigations in these models implicate altered subcellular localization of RNA exosome components and reduced SNARE proteins/complex assembly in embryonic cerebella, suggesting disrupted RNA regulation and vesicular trafficking during development (baldini2019understandingthemolecular pages 1-9).

**Model type:** mammalian genetic model (mouse) and human iPSC-derived brain organoids (frank2024absenceofthe pages 2-4, baldini2019understandingthemolecular pages 9-13).

---

## Recent developments (2023–2024 highlights)
1) **Improved clinical interpretation of MID1 intronic variants (2023):** emphasizes limited accessibility of patient mRNA studies (“MID1 is not expressed in blood”) and supports functional **minigene assays** for splicing effects and ACMG/AMP reclassification (micale2023opitzsyndromeimproving pages 1-2). Publication: Aug 2023; https://doi.org/10.1038/s41390-022-02237-y.
2) **Human brain organoid disease modeling of MID1 isoform mechanisms (2024):** absence of RING-domain-containing isoforms causes early patterning defects, reduced neural tissue, and increased choroid plexus-like structures with early transcriptomic changes (frank2024absenceofthe pages 1-2, frank2024absenceofthe pages 2-4). Publication: Jan 2024; https://doi.org/10.26508/lsa.202302288. Representative figure evidence in the retrieved paper is shown in (frank2024absenceofthe media 7494b3f8, frank2024absenceofthe media 8e0af7e5, frank2024absenceofthe media f851948f, frank2024absenceofthe media 42fc7635).

---

## Data/knowledge gaps and limitations (based on retrieved corpus)
- **Ontology/terminology IDs:** MONDO, Orphanet (ORPHA), ICD-10/ICD-11, and MeSH identifiers were not present in the retrieved sources; therefore they cannot be asserted with citations here.
- **Epidemiology:** only a coarse male incidence range was available; prevalence, sex ratio across subtypes, and population-specific estimates were not available.
- **Variant-level statistics:** specific recurrent variants, allele frequencies (gnomAD), and penetrance estimates were not extractable.
- **Treatment outcomes:** no controlled treatment studies specific to Opitz G/BBB were retrieved; management evidence is largely clinical practice/case-based.

---

## Quick-reference summary table

| Disease / synonym(s) | Key identifiers in retrieved evidence | Genetic form / locus / gene | Hallmark clinical features supported in retrieved evidence | Representative recent references (year; DOI URL) |
|---|---|---|---|---|
| Opitz G/BBB syndrome; Opitz syndrome; BBB syndrome; G syndrome; Opitz-Frias syndrome; telecanthus-hypospadias syndrome (baldini2019understandingthemolecular pages 97-101, vagha2023ararecase pages 1-5) | OMIM/MIM: 300000 (X-linked Opitz G/BBB / XLOS), 145410 (autosomal dominant Opitz syndrome / OS); MID1 gene OMIM/MIM: 300552; MONDO: not found in retrieved sources; Orphanet: not found in retrieved sources; ICD-10/ICD-11: not found in retrieved sources; MeSH: not found in retrieved sources (migliore2022specc1lmutationsare pages 1-2, micale2023opitzsyndromeimproving pages 1-2, wang2025heartfailurecaused pages 1-3, sarno2021firsttrimesterultrasound pages 1-3) | Genetically heterogeneous disorder affecting midline development. X-linked form caused by hemizygous pathogenic variants in MID1/TRIM18 at Xp22.2; autosomal-dominant form linked to 22q11.2 genomic losses, with some families carrying heterozygous SPECC1L variants at 22q11.23 (migliore2022specc1lmutationsare pages 1-2, micale2023opitzsyndromeimproving pages 1-2) | Hypertelorism/telecanthus; hypospadias; laryngo-tracheo-esophageal defects; cleft lip and/or palate; congenital heart defects; anorectal anomalies; cryptorchidism/bifid or hypoplastic scrotum; CNS anomalies including Dandy-Walker malformation and agenesis/hypoplasia of corpus callosum or cerebellar vermis; developmental delay/intellectual disability with variable expressivity (migliore2022specc1lmutationsare pages 1-2, micale2023opitzsyndromeimproving pages 1-2, vagha2023ararecase pages 1-5, tessier2020hydrothoraxinfetal pages 1-2) | Micale et al., 2023; https://doi.org/10.1038/s41390-022-02237-y (micale2023opitzsyndromeimproving pages 1-2) · Vagha et al., 2023; https://doi.org/10.7759/cureus.37411 (vagha2023ararecase pages 1-5) |
| X-linked Opitz G/BBB syndrome (XLOS) (sarno2021firsttrimesterultrasound pages 1-3) | OMIM/MIM: 300000; MID1 OMIM/MIM: 300552; prevalence in males reported as 1:50,000-1:100,000 in retrieved sources; other identifiers not found in retrieved sources (sarno2021firsttrimesterultrasound pages 1-3, vagha2023ararecase pages 5-6) | X-linked inheritance; MID1/TRIM18 loss-of-function variants including missense, nonsense, indels, splice-site variants, and whole-gene/intragenic deletions (micale2023opitzsyndromeimproving pages 1-2, vagha2023ararecase pages 5-6) | Core findings include hypertelorism/telecanthus and hypospadias, often with cleft lip/palate, heart defects, laryngo-tracheo-esophageal anomalies, genital anomalies, and variable neurodevelopmental involvement; prenatal findings reported include increased nuchal translucency, cleft lip/palate, heart defects, enlarged fourth ventricle, absent ductus venosus, hydrothorax, and vermis defects (vagha2023ararecase pages 1-5, tessier2020hydrothoraxinfetal pages 1-2, sarno2021firsttrimesterultrasound pages 1-3) | Sarno et al., 2021; https://doi.org/10.1080/14767058.2019.1677594 (sarno2021firsttrimesterultrasound pages 1-3) · Micale et al., 2023; https://doi.org/10.1038/s41390-022-02237-y (micale2023opitzsyndromeimproving pages 1-2) |
| Autosomal dominant Opitz syndrome; 22q11.2-related / SPECC1L-related Opitz G/BBB syndrome (migliore2022specc1lmutationsare pages 1-2, wild2020congenitaldiaphragmatichernia pages 1-2) | OMIM/MIM: 145410 in retrieved sources; 22q11.2 region implicated; MONDO/Orphanet/ICD/MeSH not found in retrieved sources (migliore2022specc1lmutationsare pages 1-2) | Autosomal dominant form linked to 22q11.2 genomic losses; some families reported with heterozygous SPECC1L pathogenic variants at 22q11.23, though retrieved evidence notes SPECC1L mutations are not common in sporadic OS and may represent a distinct SPECC1L syndrome spectrum (migliore2022specc1lmutationsare pages 1-2, bhoj2019phenotypicspectrumassociated pages 1-5) | Overlaps with Opitz craniofacial phenotype (hypertelorism, prominent forehead, broad nasal bridge, anteverted nares, cleft lip/palate), but canonical laryngeal malformations and male genital anomalies may be absent; relatively characteristic SPECC1L-associated findings include branchial fistulae, omphalocele, congenital diaphragmatic hernia, bicornuate uterus/uterus didelphys, umbilical hernia, vesicoureteral reflux, and deafness (bhoj2019phenotypicspectrumassociated pages 1-5, wild2020congenitaldiaphragmatichernia pages 1-2, bhoj2019phenotypicspectrumassociated pages 11-14) | Migliore et al., 2022; https://doi.org/10.3390/genes13020252 (migliore2022specc1lmutationsare pages 1-2) · Wild et al., 2020; https://doi.org/10.1002/ajmg.a.61878 (wild2020congenitaldiaphragmatichernia pages 1-2) |


*Table: This table compacts the retrieved evidence on Opitz G/BBB syndrome into names, identifiers, genetic subtypes, hallmark features, and representative references. It is useful as a quick-reference artifact for disease knowledge base population and cross-checking genotype-phenotype distinctions.*

References

1. (baldini2019understandingthemolecular pages 97-101): R Baldini. Understanding the molecular mechanisms underlying the pathogenesis of opitz g/bbb syndrome exploiting the mid1 knock-out …. Unknown journal, 2019.

2. (vagha2023ararecase pages 1-5): Jayant Vagha, Ajinkya Wazurkar, Keta Vagha, Sham Lohiya, and Ashish Varma. A rare case of telecanthus-hypospadias syndrome in a pediatric patient. Cureus, Apr 2023. URL: https://doi.org/10.7759/cureus.37411, doi:10.7759/cureus.37411. This article has 0 citations.

3. (migliore2022specc1lmutationsare pages 1-2): Chiara Migliore, Anna Vendramin, Shane McKee, Paolo Prontera, Francesca Faravelli, Rani Sachdev, Patricia Dias, Martina Mascaro, Danilo Licastro, and Germana Meroni. Specc1l mutations are not common in sporadic cases of opitz g/bbb syndrome. Genes, 13:252, Jan 2022. URL: https://doi.org/10.3390/genes13020252, doi:10.3390/genes13020252. This article has 4 citations.

4. (micale2023opitzsyndromeimproving pages 1-2): Lucia Micale, Federica Russo, Martina Mascaro, Silvia Morlino, Grazia Nardella, Carmela Fusco, Luigi Bisceglia, Germana Meroni, and Marco Castori. Opitz syndrome: improving clinical interpretation of intronic variants in mid1 gene. Pediatric Research, 93:1208-1215, Aug 2023. URL: https://doi.org/10.1038/s41390-022-02237-y, doi:10.1038/s41390-022-02237-y. This article has 4 citations and is from a domain leading peer-reviewed journal.

5. (wang2025heartfailurecaused pages 1-3): Yu Wang, Xiang Wu, and Kun Wang. Heart failure caused by opitz syndrome: a case report and literature review. BMC Cardiovascular Disorders, Dec 2025. URL: https://doi.org/10.1186/s12872-025-05297-0, doi:10.1186/s12872-025-05297-0. This article has 0 citations and is from a peer-reviewed journal.

6. (sarno2021firsttrimesterultrasound pages 1-3): Laura Sarno, Giuseppe Maria Maruotti, Antonella Izzo, Cristina Mazzaccara, Luigi Carbone, Giuseppina Esposito, Marco Di Cresce, Gabriele Saccone, Angelo Sirico, Rita Genesio, Nunzia Mollo, Pasquale Martinelli, Anna Conti, Fulvio Zullo, and Giulia Frisso. First trimester ultrasound features of x-linked opitz syndrome and early molecular diagnosis: case report and review of the literature. The Journal of Maternal-Fetal & Neonatal Medicine, 34:3089-3093, Oct 2021. URL: https://doi.org/10.1080/14767058.2019.1677594, doi:10.1080/14767058.2019.1677594. This article has 3 citations.

7. (bhoj2019phenotypicspectrumassociated pages 1-5): Elizabeth J. Bhoj, Damien Haye, Annick Toutain, Dominique Bonneau, Irene Kibæk Nielsen, Ida Bay Lund, Pauline Bogaard, Stine Leenskjold, Kadri Karaer, Katherine T. Wild, Katheryn L. Grand, Mirena C. Astiazaran, Luis A. Gonzalez-Nieto, Ana Carvalho, Daphné Lehalle, Shivarajan M. Amudhavalli, Elena Repnikova, Carol Saunders, Isabelle Thiffault, Irfan Saadi, Dong Li, Hakon Hakonarson, Yoann Vial, Elaine Zackai, Patrick Callier, Séverine Drunat, and Alain Verloes. Phenotypic spectrum associated with specc1l pathogenic variants: new families and critical review of the nosology of teebi, opitz gbbb, and baraitser-winter syndromes. European Journal of Medical Genetics, 62:103588, Dec 2019. URL: https://doi.org/10.1016/j.ejmg.2018.11.022, doi:10.1016/j.ejmg.2018.11.022. This article has 39 citations and is from a peer-reviewed journal.

8. (tessier2020hydrothoraxinfetal pages 1-2): Aude Tessier, Lucile Boutaud, Ange‐Line Bruel, Christel Thauvin‐Robinet, Philippe Roth, Valérie Malan, Marie‐Paule Beaujard, Amale Achaiaa, Judite de Oliveira, Julie Steffann, Ferechte Encha‐Razavi, Laurence Faivre, Bettina Bessières, and Tania Attié‐Bitach. Hydrothorax in fetal cases of opitz g/<scp>bbb</scp> diagnosis: extending the phenotype? Clinical Genetics, 98:620-621, Sep 2020. URL: https://doi.org/10.1111/cge.13840, doi:10.1111/cge.13840. This article has 1 citations and is from a peer-reviewed journal.

9. (listyasari2022clinicallessonlearned pages 3-3): Nurin A. Listyasari, Gorjana Robevska, Katie L. Ayers, Tiong Yang Tan, Andrew H. Sinclair, and Sultana M.H. Faradz. Clinical lesson learned from genetic analysis in patients prior to surgical repair of hypospadias. Asian Journal of Urology, 9:186-189, Apr 2022. URL: https://doi.org/10.1016/j.ajur.2022.02.006, doi:10.1016/j.ajur.2022.02.006. This article has 0 citations.

10. (wild2020congenitaldiaphragmatichernia pages 1-2): K. Taylor Wild, Tia Gordon, Elizabeth J. Bhoj, Haowei Du, Shalini N. Jhangiani, Jennifer E. Posey, James R. Lupski, Daryl A. Scott, and Elaine H. Zackai. Congenital diaphragmatic hernia as a prominent feature of a specc1l‐related syndrome. American Journal of Medical Genetics Part A, 182:2919-2925, Sep 2020. URL: https://doi.org/10.1002/ajmg.a.61878, doi:10.1002/ajmg.a.61878. This article has 12 citations.

11. (baldini2019understandingthemolecular pages 9-13): R Baldini. Understanding the molecular mechanisms underlying the pathogenesis of opitz g/bbb syndrome exploiting the mid1 knock-out …. Unknown journal, 2019.

12. (migliore2022specc1lmutationsare pages 8-10): Chiara Migliore, Anna Vendramin, Shane McKee, Paolo Prontera, Francesca Faravelli, Rani Sachdev, Patricia Dias, Martina Mascaro, Danilo Licastro, and Germana Meroni. Specc1l mutations are not common in sporadic cases of opitz g/bbb syndrome. Genes, 13:252, Jan 2022. URL: https://doi.org/10.3390/genes13020252, doi:10.3390/genes13020252. This article has 4 citations.

13. (baldini2019understandingthemolecular pages 13-18): R Baldini. Understanding the molecular mechanisms underlying the pathogenesis of opitz g/bbb syndrome exploiting the mid1 knock-out …. Unknown journal, 2019.

14. (frank2024absenceofthe pages 2-4): Sarah Frank, Elisa Gabassi, Stephan Käseberg, Marco Bertin, Lea Zografidou, Daniela Pfeiffer, Heiko Brennenstuhl, Sven Falk, Marisa Karow, and Susann Schweiger. Absence of the ring domain in mid1 results in patterning defects in the developing human brain. Life Science Alliance, 7:e202302288, Jan 2024. URL: https://doi.org/10.26508/lsa.202302288, doi:10.26508/lsa.202302288. This article has 8 citations and is from a peer-reviewed journal.

15. (frank2024absenceofthe pages 1-2): Sarah Frank, Elisa Gabassi, Stephan Käseberg, Marco Bertin, Lea Zografidou, Daniela Pfeiffer, Heiko Brennenstuhl, Sven Falk, Marisa Karow, and Susann Schweiger. Absence of the ring domain in mid1 results in patterning defects in the developing human brain. Life Science Alliance, 7:e202302288, Jan 2024. URL: https://doi.org/10.26508/lsa.202302288, doi:10.26508/lsa.202302288. This article has 8 citations and is from a peer-reviewed journal.

16. (frank2024absenceofthe media 7494b3f8): Sarah Frank, Elisa Gabassi, Stephan Käseberg, Marco Bertin, Lea Zografidou, Daniela Pfeiffer, Heiko Brennenstuhl, Sven Falk, Marisa Karow, and Susann Schweiger. Absence of the ring domain in mid1 results in patterning defects in the developing human brain. Life Science Alliance, 7:e202302288, Jan 2024. URL: https://doi.org/10.26508/lsa.202302288, doi:10.26508/lsa.202302288. This article has 8 citations and is from a peer-reviewed journal.

17. (frank2024absenceofthe media 8e0af7e5): Sarah Frank, Elisa Gabassi, Stephan Käseberg, Marco Bertin, Lea Zografidou, Daniela Pfeiffer, Heiko Brennenstuhl, Sven Falk, Marisa Karow, and Susann Schweiger. Absence of the ring domain in mid1 results in patterning defects in the developing human brain. Life Science Alliance, 7:e202302288, Jan 2024. URL: https://doi.org/10.26508/lsa.202302288, doi:10.26508/lsa.202302288. This article has 8 citations and is from a peer-reviewed journal.

18. (frank2024absenceofthe media f851948f): Sarah Frank, Elisa Gabassi, Stephan Käseberg, Marco Bertin, Lea Zografidou, Daniela Pfeiffer, Heiko Brennenstuhl, Sven Falk, Marisa Karow, and Susann Schweiger. Absence of the ring domain in mid1 results in patterning defects in the developing human brain. Life Science Alliance, 7:e202302288, Jan 2024. URL: https://doi.org/10.26508/lsa.202302288, doi:10.26508/lsa.202302288. This article has 8 citations and is from a peer-reviewed journal.

19. (frank2024absenceofthe media 42fc7635): Sarah Frank, Elisa Gabassi, Stephan Käseberg, Marco Bertin, Lea Zografidou, Daniela Pfeiffer, Heiko Brennenstuhl, Sven Falk, Marisa Karow, and Susann Schweiger. Absence of the ring domain in mid1 results in patterning defects in the developing human brain. Life Science Alliance, 7:e202302288, Jan 2024. URL: https://doi.org/10.26508/lsa.202302288, doi:10.26508/lsa.202302288. This article has 8 citations and is from a peer-reviewed journal.

20. (wei2024midline1regulateseffector pages 13-13): Yingying Wei, Wenjuan Li, Jie Huang, Zachary Braunstein, Xinxin Liu, Xinlu Li, Jeffrey Deiuliis, Jun Chen, Xinwen Min, Handong Yang, Quan Gong, Leya He, Zheng Liu, Lingli Dong, and Jixin Zhong. Midline-1 regulates effector t cell motility in experimental autoimmune encephalomyelitis via mtor/microtubule pathway. Theranostics, 14:1168-1180, Jan 2024. URL: https://doi.org/10.7150/thno.87130, doi:10.7150/thno.87130. This article has 14 citations and is from a domain leading peer-reviewed journal.

21. (vagha2023ararecase pages 5-6): Jayant Vagha, Ajinkya Wazurkar, Keta Vagha, Sham Lohiya, and Ashish Varma. A rare case of telecanthus-hypospadias syndrome in a pediatric patient. Cureus, Apr 2023. URL: https://doi.org/10.7759/cureus.37411, doi:10.7759/cureus.37411. This article has 0 citations.

22. (baldini2019understandingthemolecular pages 1-9): R Baldini. Understanding the molecular mechanisms underlying the pathogenesis of opitz g/bbb syndrome exploiting the mid1 knock-out …. Unknown journal, 2019.

23. (bhoj2019phenotypicspectrumassociated pages 11-14): Elizabeth J. Bhoj, Damien Haye, Annick Toutain, Dominique Bonneau, Irene Kibæk Nielsen, Ida Bay Lund, Pauline Bogaard, Stine Leenskjold, Kadri Karaer, Katherine T. Wild, Katheryn L. Grand, Mirena C. Astiazaran, Luis A. Gonzalez-Nieto, Ana Carvalho, Daphné Lehalle, Shivarajan M. Amudhavalli, Elena Repnikova, Carol Saunders, Isabelle Thiffault, Irfan Saadi, Dong Li, Hakon Hakonarson, Yoann Vial, Elaine Zackai, Patrick Callier, Séverine Drunat, and Alain Verloes. Phenotypic spectrum associated with specc1l pathogenic variants: new families and critical review of the nosology of teebi, opitz gbbb, and baraitser-winter syndromes. European Journal of Medical Genetics, 62:103588, Dec 2019. URL: https://doi.org/10.1016/j.ejmg.2018.11.022, doi:10.1016/j.ejmg.2018.11.022. This article has 39 citations and is from a peer-reviewed journal.