---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-22T22:09:02.691219'
end_time: '2026-04-22T22:26:01.343502'
duration_seconds: 1018.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alport Syndrome
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Alport Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Alport Syndrome** covering all of the
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
- **Disease Name:** Alport Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Alport Syndrome** covering all of the
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


## Comprehensive Disease Characteristics Report: Alport Syndrome (Genetic)

### Executive summary
Alport syndrome is an inherited type IV collagen basement-membrane disorder caused by pathogenic variants in **COL4A3, COL4A4, and/or COL4A5**, classically presenting with **persistent microscopic haematuria**, progressive kidney disease (often to kidney failure), and variably **sensorineural hearing loss** and **ocular abnormalities**. Contemporary expert guidance emphasizes **early, genotype-first diagnosis** (joint COL4A3/4/5 testing) and **early renin–angiotensin system (RAS) blockade** as standard of care, with **SGLT2 inhibitors** considered in proteinuric adults with CKD. (torra2025diagnosismanagementand pages 1-2, kang2024acomprehensivereview pages 5-6)

| Domain | Item | Key details | Evidence |
|---|---|---|---|
| Identifiers | MONDO | **MONDO_0018965** (Alport syndrome); related MONDO subtype entries also represented in Open Targets for autosomal dominant, autosomal recessive, and X-linked Alport syndrome | (torra2025diagnosismanagementand pages 1-2) |
| Identifiers | OMIM disease IDs | **Alport syndrome OMIM#308940**; **XLAS OMIM#301050**; **ARAS OMIM#203780**; **ADAS OMIM#104200** | (liang2023moleculardynamicsand pages 1-2) |
| Identifiers | Causal gene OMIM* | **COL4A5 OMIM*303630**, **COL4A3 OMIM*120070**, **COL4A4 OMIM*120131** | (liang2023moleculardynamicsand pages 1-2) |
| Definition | Core disease definition | Rare hereditary glomerular nephropathy caused by pathogenic variants in **COL4A3, COL4A4, COL4A5**, disrupting the **α3α4α5 type IV collagen** network in basement membranes, especially GBM | (kang2024acomprehensivereview pages 1-3, torra2025diagnosismanagementand pages 1-2) |
| Definition | Core clinical triad | Kidney disease with **persistent microscopic hematuria → proteinuria → CKD/kidney failure**, plus **sensorineural hearing loss** and **ocular abnormalities** | (kang2024acomprehensivereview pages 1-3, torra2025diagnosismanagementand pages 1-2, kang2024acomprehensivereview pages 3-5) |
| Inheritance | Genetic forms | **X-linked (COL4A5)**, **autosomal recessive (biallelic COL4A3/COL4A4)**, **autosomal dominant (heterozygous COL4A3/COL4A4)**, and **digenic** forms recognized | (kang2024acomprehensivereview pages 1-3, torra2025diagnosismanagementand pages 1-2, kang2024acomprehensivereview pages 3-5, daga2022the2019and pages 2-3) |
| Epidemiology | Prevalence estimates | Historical phenotype-based estimates range from about **1:5,000** to **1:17,000**; another review cites about **1 in 50,000**; workshop-era genomic discussion suggests pathogenic **COL4A3-5** variants may be much more common than classic clinical estimates | (torra2025diagnosismanagementand pages 1-2, kang2024acomprehensivereview pages 1-3, savige2021consensusstatementon pages 1-2, daga2022the2019and pages 1-2) |
| Epidemiology | Population-genomic estimate | Workshop report cites **X-linked Alport prevalence ~1 in 2,000** from gnomAD-era population analysis; rare heterozygous COL4A3/4/5 variants reported up to **0.94%** in the UK population | (daga2022the2019and pages 2-3, daga2022the2019and pages 3-4) |
| Subtype distribution | Relative frequencies | XLAS is most common; one 2024 review reports **~80% XLAS**, **10–15% ARAS**, **20–30% ADAS** (overlap reflects evolving nomenclature/ascertainment); another review cites **~85% X-linked** and **~15% AR** | (kang2024acomprehensivereview pages 3-5, adone2023alportsyndromea pages 3-4) |
| Natural history | XLAS renal prognosis | In males with XLAS, about **50% reach ESKD before age 20** in one review; another review reports males with **COL4A5** variants have about **90% risk of ESKD by age 40** | (kang2024acomprehensivereview pages 5-6, adone2023alportsyndromea pages 3-4) |
| Natural history | Female XLAS prognosis | Females with XLAS are not just “carriers”; review estimates **up to 25% may progress to CKD G5** over lifetime; another review cites **~15–30% ESKD risk by age 60** | (kang2024acomprehensivereview pages 3-5, adone2023alportsyndromea pages 3-4) |
| Natural history | ARAS and ADAS prognosis | ARAS: **~62% progress to ESKD**, mean ESKD about **21 years**; ADAS: microhematuria in **~92%**, estimated kidney survival about **67 years** | (kang2024acomprehensivereview pages 5-6) |
| Hearing phenotype | Frequencies | In XLAS males, hearing loss occurs in about **50% by ~15 years**, **75% by 25**, **90% by 40**; in XLAS females, about **10% by 40** and **~20% by 60**; ARAS hearing loss about **64%** | (kang2024acomprehensivereview pages 5-6) |
| Ocular phenotype | Frequencies | Ocular abnormalities in about **30–40% of males** and **~15% of females** overall; **anterior lenticonus** is pathognomonic and seen in **~15% of affected XLAS males**; ARAS ocular manifestations about **17%** | (kang2024acomprehensivereview pages 5-6, kang2024acomprehensivereview pages 3-5) |
| Pathology | Characteristic biopsy findings | Light microscopy often nonspecific (**FSGS, mesangial hypercellularity, interstitial foam cells**); EM shows **GBM thinning/thickening, irregularity, lamellation, basket-weave change, intramembranous microspherules**; type IV collagen staining patterns vary by inheritance | (lee2024pathologicaldiagnosisof pages 2-5, lee2024pathologicaldiagnosisof media 9c957d59, lee2024pathologicaldiagnosisof media 091648f1) |
| Diagnostics | First-line testing | 2024 ERKNet/ERA/ESPN guideline: **joint genetic analysis of COL4A3/4/5 is the key initial diagnostic test** in persistent hematuria, proteinuria, unexplained kidney failure, FSGS of unknown origin, and possibly cystic kidney disease | (torra2025diagnosismanagementand pages 1-2) |
| Diagnostics | Expanded testing indications | Beyond classic phenotype, testing should also be considered in **persistent proteinuria, steroid-resistant nephrotic syndrome, FSGS, familial IgA nephropathy/glomerulonephritis, and ESKD without obvious cause** | (savige2021consensusstatementon pages 1-2, savige2021consensusstatementon pages 2-3) |
| Diagnostics | Role of biopsy vs genetics | Biopsy remains useful, but reviews/guidelines emphasize that **NGS increasingly reduces need for invasive biopsy** and can identify atypical, female, monoallelic, and digenic disease | (lee2024pathologicaldiagnosisof pages 2-5, chen2025novelcol4a3–col4a5variants pages 3-4, torra2025diagnosismanagementand pages 1-2) |
| Treatment guidance | Standard of care | **Early renin–angiotensin system blockade (ACE inhibitor/ARB)** is the standard disease-slowing therapy; early diagnosis is important because treatment started early improves renal outcomes | (torra2025diagnosismanagementand pages 1-2, kang2024acomprehensivereview pages 8-10) |
| Treatment guidance | SGLT2 inhibitors | Guideline states **SGLT2 inhibitors may be added in adults with proteinuria and CKD**; pediatric/young adult dapagliflozin RCT protocol (**DOUBLE PRO-TECT Alport, NCT05944016**) is underway | (torra2025diagnosismanagementand pages 1-2) |
| Treatment research | Bardoxolone methyl | CARDINAL enrolled **157** patients; on-treatment eGFR differences favored bardoxolone at **48 weeks (+9.2 mL/min/1.73 m²)** and **100 weeks (+7.4)**, but **3 patients in each group developed kidney failure**, albuminuria rose on treatment, liver enzyme elevations were common, and FDA approval was rejected | (ruggenenti2023thecardinaltrial pages 1-2, ruggenenti2023thecardinaltrial pages 3-4, sarfraz2025systematicreviewof pages 3-5, ruggenenti2023thecardinaltrial pages 4-5) |
| Current trial landscape | Notable ongoing/recent studies | **Lademirsen/SAR339375** phase 2 terminated for futility with no unexpected safety findings; **RG-012** phase 1 completed; observational dapagliflozin cohort **NCT06226896** active; Alport Therapy Registry **NCT02378805** recruiting for long-term real-world outcomes | (NCT03373786 chunk 1, NCT02855268 chunk 1, NCT06226896 chunk 1, NCT02378805 chunk 2) |


*Table: This table condenses the most actionable identifiers, epidemiology, phenotype frequencies, diagnostic recommendations, and current treatment evidence for Alport syndrome. It is designed as a knowledge-base-ready snapshot with context-ID citations mapped to the retrieved evidence.*

---

## 1. Disease Information

### 1.1 Overview / definition
Alport syndrome is a hereditary glomerular nephropathy due to defects in the **α3–α4–α5 type IV collagen network** of basement membranes, especially the glomerular basement membrane (GBM), driven by pathogenic variants in **COL4A3, COL4A4, and COL4A5**. (kang2024acomprehensivereview pages 1-3, torra2025diagnosismanagementand pages 1-2)

A widely used clinical framing is the kidney–ear–eye triad: kidney disease with persistent haematuria progressing to CKD/kidney failure, plus hearing loss and ocular abnormalities. (torra2025diagnosismanagementand pages 1-2, kang2024acomprehensivereview pages 3-5)

### 1.2 Key identifiers (available from tool-accessible sources)
- **MONDO:** **MONDO_0018965** (Alport syndrome) (torra2025diagnosismanagementand pages 1-2)
- **OMIM disease IDs (from primary abstract text):** Alport syndrome **OMIM#308940**; X-linked **OMIM#301050**; autosomal recessive **OMIM#203780**; autosomal dominant **OMIM#104200** (liang2023moleculardynamicsand pages 1-2)
- **Causal genes (OMIM gene entries cited in abstract):** **COL4A5 (OMIM*303630)**, **COL4A3 (OMIM*120070)**, **COL4A4 (OMIM*120131)** (liang2023moleculardynamicsand pages 1-2)

**Not retrievable with current tool evidence:** Orphanet ORPHA ID, ICD-10/ICD-11 codes, and MeSH ID were not present in the retrieved documents/records and therefore cannot be asserted here without external database access.

### 1.3 Synonyms / alternative names
- “X-linked Alport syndrome (XLAS)”, “autosomal recessive Alport syndrome (ARAS)”, “autosomal dominant Alport syndrome (ADAS)” (liang2023moleculardynamicsand pages 1-2)
- “COL4A3/4/5 glomerulopathy” is used in guideline framing for the broader genotypic spectrum (torra2025diagnosismanagementand pages 1-2)
- “Alport spectrum” has been discussed as an umbrella term in genomics-era nomenclature discussions. (daga2022the2019and pages 3-4)

### 1.4 Evidence provenance: patient-level vs aggregated resources
Evidence summarized below is derived from (i) **expert guideline consensus** (systematic review + graded recommendations), (ii) **peer-reviewed reviews**, (iii) **observational cohorts/case series**, and (iv) **ClinicalTrials.gov trial registry records**. (torra2025diagnosismanagementand pages 1-2, kang2024acomprehensivereview pages 5-6, NCT02855268 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary causal factor:** germline pathogenic variants affecting type IV collagen α3/α4/α5 chain formation, encoded by **COL4A3, COL4A4, COL4A5**. (kang2024acomprehensivereview pages 1-3, torra2025diagnosismanagementand pages 1-2)

**Mechanistic framing:** mutations disrupt α3α4α5(IV) heterotrimer formation and basement membrane integrity, rendering the GBM vulnerable under filtration pressure, leading to haematuria and progressive injury. (kang2024acomprehensivereview pages 1-3)

### 2.2 Risk factors
- **Genetic risk:** inheritance mode and variant type strongly influence risk of early kidney failure (e.g., severe disease in males with XLAS; earlier and more severe course in ARAS than ADAS). (kang2024acomprehensivereview pages 5-6, kang2024acomprehensivereview pages 3-5)
- **Proteinuria** is emphasized as a major risk factor for progression to CKD/ESKD in Alport syndrome. (kang2024acomprehensivereview pages 3-5)

**Candidate genetic modifiers:** co-occurring variants in podocyte or non-collagenous ECM genes (e.g., **CRB2, LAMA5, LAMB2, NUP107, MYO1E, PLCE1**) may contribute to phenotypic variability (nephrotic-range proteinuria, FSGS, ESKD) in some patients, based on a small case series. (lujinschi2025candidategeneticmodifiers pages 1-2)

### 2.3 Protective factors
Direct genetic or environmental protective factors were not identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
Direct gene–environment interaction evidence for Alport syndrome was not identified in the retrieved evidence set.

---

## 3. Phenotypes

### 3.1 Core renal phenotypes
- **Persistent microscopic haematuria** (hallmark feature) with subsequent **proteinuria** and progressive decline in kidney function. (torra2025diagnosismanagementand pages 1-2, kang2024acomprehensivereview pages 3-5)
- Pediatric cohort example (Southwestern China): hematuria + proteinuria in **85% (34/40)**; pure hematuria **15% (6/40)**; nephrotic-range proteinuria in **10/40**. (chen2025novelcol4a3–col4a5variants pages 3-4)

**Suggested HPO terms (examples):**
- Hematuria **HP:0000790**
- Proteinuria **HP:0000093**
- Chronic kidney disease **HP:0012622**
- End-stage renal disease **HP:0003774**

### 3.2 Auditory phenotypes
- **Sensorineural hearing loss** is common and progressive; one review reports (XLAS males) ~**50% by ~15 years**, **75% by 25**, **90% by 40**; and (XLAS females) **10% by 40** and **~20% by 60**. (kang2024acomprehensivereview pages 5-6)

**Suggested HPO term:** Sensorineural hearing impairment **HP:0000407**.

### 3.3 Ocular phenotypes
- **Anterior lenticonus** is described as pathognomonic; one review reports it in ~**15% of males with XLAS**. (kang2024acomprehensivereview pages 5-6)
- Other ocular findings include maculopathy with flecks; ocular abnormalities overall reported in ~**30–40% of males** and **~15% of females**. (kang2024acomprehensivereview pages 3-5)

**Suggested HPO terms (examples):**
- Anterior lenticonus **HP:0001132**
- Cataract **HP:0000518**
- Abnormal retinal pigmentation / dot-and-fleck retinopathy (phenotype-mapping required to exact HPO term)

### 3.4 Other features
Hypertension becomes more frequent with age, especially in males with XLAS. (kang2024acomprehensivereview pages 3-5)

**Suggested HPO term:** Hypertension **HP:0000822**.

### 3.5 Quality-of-life impact
Direct quantitative quality-of-life instrument results (e.g., SF-36, EQ-5D, PROMIS) were not available in the retrieved evidence.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **COL4A5** (X-linked), **COL4A3** and **COL4A4** (autosomal dominant/recessive), with digenic combinations reported. (torra2025diagnosismanagementand pages 1-2, kang2024acomprehensivereview pages 3-5)

### 4.2 Pathogenic variant classes and functional consequences
Across cohorts and variant interpretation guidance, pathogenic variants include missense (often glycine substitutions in Gly-X-Y collagen repeats), nonsense, frameshift, splice variants, and CNVs; splice variants may require functional confirmation (e.g., minigene assays). (chen2025novelcol4a3–col4a5variants pages 3-4, lee2024pathologicaldiagnosisof pages 2-5, savige2021consensusstatementon pages 1-2)

**Example splice-variant mechanistic evidence (human):** a COL4A5 intronic variant **c.4298–20T>A** was shown (minigene assay) to cause intron 46 retention and predicted impairment of α5(IV) structure, supporting classification as likely pathogenic with mild XLAS phenotype. (liang2023moleculardynamicsand pages 1-2)

### 4.3 Variant interpretation standards (ACMG/AMP refinement)
A consensus statement refined ACMG/AMP variant interpretation for COL4A3–COL4A5 and broadened recommended testing indications beyond the classic phenotype. Key challenges include **hypomorphic variants**, variable inheritance, and inability to define a universal benign MAF threshold. (savige2021consensusstatementon pages 1-2, savige2021consensusstatementon pages 2-3)

**Direct abstract quote (Savige 2021):**
- “extended the indications for screening for pathogenic variants in the COL4A5, COL4A3 and COL4A4 genes beyond the classical Alport phenotype … to include persistent proteinuria, steroid-resistant nephrotic syndrome, focal and segmental glomerulosclerosis (FSGS), familial IgA glomerulonephritis and end-stage kidney failure without an obvious cause.” (savige2021consensusstatementon pages 1-2)

### 4.4 Modifier genes
Evidence from a small case series suggests co-occurring variants in podocyte/ECM genes (e.g., **CRB2, PLCE1, MYO1E, NUP107, LAMA5, LAMB2**) may modify severity (e.g., nephrotic syndrome, FSGS, ESKD), but authors emphasize uncertainty and need for validation. (lujinschi2025candidategeneticmodifiers pages 1-2, lujinschi2025candidategeneticmodifiers pages 2-4)

### 4.5 Epigenetics / chromosomal abnormalities
No disease-specific epigenetic or chromosomal-abnormality evidence was identified in the retrieved evidence set.

---

## 5. Environmental Information

No specific environmental toxin, pollution, occupational exposure, or infectious trigger evidence was identified in the retrieved evidence set as a causal contributor to Alport syndrome (a monogenic disorder). Lifestyle factors were also not described in a disease-specific manner in the retrieved evidence.

---

## 6. Mechanism / Pathophysiology

### 6.1 Core causal chain (current understanding)
1) **Pathogenic COL4A3/4/5 variant** → 2) defective assembly/stability of α3α4α5(IV) collagen network in GBM → 3) compromised filtration barrier integrity under physiologic pressure → 4) haematuria and progressive glomerular injury → 5) proteinuria and CKD progression to ESKD; with parallel basement-membrane pathology in cochlea/eye contributing to hearing/ocular phenotypes. (kang2024acomprehensivereview pages 1-3, torra2025diagnosismanagementand pages 1-2)

### 6.2 Fibrosis and inflammation (downstream mechanisms)
A mechanistic mouse study linked COL4A5 deficiency to renal fibrosis via HA/CD44/TGFβ signaling, proposing HAS2/CD44 as potential targets: “COL4A5 deficiency may lead to HAS2 overexpression and HA accumulation to activate CD44-TGFβ signaling, thereby promoting fibrosis”. ()

### 6.3 Suggested GO / CL terms (knowledge-base oriented; not evidence claims)
- **GO biological process:** extracellular matrix organization (GO:0030198); basement membrane organization (GO:0071711); collagen fibril organization (GO:0030199); renal fibrosis (commonly mapped to “extracellular matrix organization” + “response to TGF-beta”) 
- **Cell Ontology (CL):** podocyte (CL:0000653); glomerular endothelial cell (CL:0002139); mesangial cell (CL:0000650)

---

## 7. Anatomical Structures Affected

### 7.1 Organ level
- **Kidney (glomerulus/GBM)** is primary. (torra2025diagnosismanagementand pages 1-2)
- **Inner ear (cochlea)** involvement manifests as sensorineural hearing loss. (kang2024acomprehensivereview pages 5-6)
- **Eye** involvement includes lens and retina findings (e.g., lenticonus, macular flecks). (kang2024acomprehensivereview pages 5-6)

### 7.2 Tissue/cell level and pathology localization
Renal biopsy pathology shows GBM ultrastructural abnormalities (thinning/thickening, irregularity, lamellation/basket-weaving) on electron microscopy; light microscopy changes are often nonspecific (including FSGS). (lee2024pathologicaldiagnosisof pages 2-5)

**Visual evidence (electron microscopy + collagen IV staining patterns):** representative EM and collagen IV staining patterns are shown in Lee 2024 Figures 2–3 (lee2024pathologicaldiagnosisof media 9c957d59, lee2024pathologicaldiagnosisof media 091648f1).

**Suggested UBERON terms (examples):**
- Kidney **UBERON:0002113**
- Glomerular basement membrane **UBERON:0005174**
- Cochlea **UBERON:0001684**
- Lens capsule / retina (map to appropriate UBERON terms as needed)

---

## 8. Temporal Development

### 8.1 Onset
In a pediatric cohort, onset was often preschool-aged (1–6 years) in **65%**. (chen2025novelcol4a3–col4a5variants pages 3-4)

### 8.2 Progression
A typical course described in reviews begins with microscopic haematuria, then proteinuria, then progressive CKD/ESKD. (kang2024acomprehensivereview pages 5-6)

---

## 9. Inheritance and Population

### 9.1 Inheritance patterns
- **X-linked (COL4A5)**, **autosomal recessive (biallelic COL4A3/COL4A4)**, **autosomal dominant (heterozygous COL4A3/COL4A4)**, and **digenic** inheritance are all recognized. (torra2025diagnosismanagementand pages 1-2, kang2024acomprehensivereview pages 3-5)

### 9.2 Epidemiology
Multiple prevalence estimates appear across sources:
- Guideline excerpt cites phenotype-based prevalence estimates ranging from **1:5,000 (Utah)** to **1:17,000 (Sweden)**. (torra2025diagnosismanagementand pages 1-2)
- Workshop-era population-genetic analysis cites **X-linked prevalence ~1 in 2,000** (gnomAD-based) and reports rare heterozygous COL4 variants up to **0.94%** in a UK population dataset, highlighting that genomic prevalence may exceed classic clinical estimates. (daga2022the2019and pages 2-3, daga2022the2019and pages 3-4)

### 9.3 Genotype–phenotype / prognosis statistics
From a 2024 review:
- **XLAS males:** ~**50% reach ESKD before age 20**. (kang2024acomprehensivereview pages 5-6)
- **XLAS hearing loss:** ~**50% by ~15 years**, **75% by 25**, **90% by 40**. (kang2024acomprehensivereview pages 5-6)
- **ARAS:** ~**62% progress to ESKD** with mean ESKD age ~**21 years**; hearing loss ~**64%**; ocular manifestations ~**17%**. (kang2024acomprehensivereview pages 5-6)
- **ADAS:** microhematuria ~**92%**; estimated kidney survival ~**67 years**. (kang2024acomprehensivereview pages 5-6)

---

## 10. Diagnostics

### 10.1 Clinical tests
- **Urinalysis** is emphasized as an effective screening test for persistent microhematuria and proteinuria. (kang2024acomprehensivereview pages 5-6)

### 10.2 Pathology (biopsy)
- Light microscopy is often nonspecific; EM provides key diagnostic ultrastructure: GBM thinning/thickening, irregularity, lamellation (“basket-weave”), intramembranous microspherules. (lee2024pathologicaldiagnosisof pages 2-5, lee2024pathologicaldiagnosisof media 9c957d59)
- Thin basement membrane disease thresholds cited: suspicion at GBM thickness **≤250 nm in adults** (≤180 nm in children). (lee2024pathologicaldiagnosisof pages 2-5)
- Type IV collagen immunostaining patterns vary by inheritance; autosomal dominant cases may be missed by collagen staining alone. (lee2024pathologicaldiagnosisof pages 2-5, lee2024pathologicaldiagnosisof media 091648f1)

### 10.3 Genetic testing (recommended approach)
The ERKNet/ERA/ESPN guideline states: “Genetic diagnostics comprising joint analysis of COL4A3/4/5 genes is already the key diagnostic test during the initial evaluation” of individuals with persistent haematuria, proteinuria, unexplained kidney failure, FSGS of unknown cause, and possibly cystic kidney disease. (torra2025diagnosismanagementand pages 1-2)

**Expanded testing indications:** persistent proteinuria, steroid-resistant nephrotic syndrome, FSGS, familial IgA glomerulonephritis, and ESKD without an obvious cause. (savige2021consensusstatementon pages 1-2, savige2021consensusstatementon pages 2-3)

### 10.4 Differential diagnosis / phenocopies
The consensus statement notes phenocopies of Alport syndrome may include other predominantly haematuric disorders (examples are listed in the paper), supporting careful differential diagnosis when COL4 variants are not identified. (savige2021consensusstatementon pages 3-4)

---

## 11. Outcome / Prognosis

### 11.1 Major prognostic factors (evidence-based)
- **Inheritance subtype and sex** (e.g., males with XLAS have earlier and more severe progression; ARAS typically severe/early; ADAS generally later but variable). (kang2024acomprehensivereview pages 5-6)
- **Proteinuria** as a progression risk marker. (kang2024acomprehensivereview pages 3-5)

### 11.2 Kidney failure outcomes
Quantified outcomes by subtype are summarized in Sections 9.3 and artifact table; hard survival metrics (life expectancy) were not directly available in the retrieved evidence.

---

## 12. Treatment

### 12.1 Standard-of-care pharmacotherapy
**RAS blockade** (ACE inhibitor or ARB) is the main disease-modifying standard of care, started early to slow progression. (torra2025diagnosismanagementand pages 1-2, kang2024acomprehensivereview pages 8-10)

**MAXO suggestions:** ACE inhibitor therapy; Angiotensin receptor blocker therapy; Blood pressure control; Proteinuria management.

### 12.2 SGLT2 inhibitors (recent developments and trials)
The ERKNet/ERA/ESPN guideline notes SGLT2 inhibitors “may be added in adults with proteinuria and chronic kidney disease.” (torra2025diagnosismanagementand pages 1-2)

Clinical research is expanding into younger patients:
- **DOUBLE PRO-TECT Alport (NCT05944016)** protocol: multicenter, randomized, double-blind, placebo-controlled; ages 10–39; randomized 2:1 to dapagliflozin 10 mg/day vs placebo for 48 weeks; primary endpoint change in UACR at week 48; key secondary eGFR change at week 52. ()
- **Observational dapagliflozin effectiveness study (NCT06226896)**: prospective cohort comparing dapagliflozin+ACEi/ARB vs ACEi/ARB alone for 24 months; primary endpoint eGFR change at 24 months; secondary includes proteinuria change and composite progression outcomes. (NCT06226896 chunk 1)

**MAXO suggestions:** SGLT2 inhibitor therapy; Albuminuria reduction therapy.

### 12.3 microRNA-21 targeting (RG-012 / lademirsen)
- **RG-012 (NCT03373786)** phase 1 completed (n=4): primary outcomes adverse events and change in renal miR-21; involved renal biopsies pre/post dosing in Part A. (NCT03373786 chunk 1)
- **Lademirsen/SAR339375 (NCT02855268)** phase 2 terminated (n=43): annualized eGFR change at week 48 was a primary endpoint; **terminated after futility analysis** with “No unexpected safety findings”. (NCT02855268 chunk 1)

**MAXO suggestions:** Antisense oligonucleotide therapy; Clinical trial enrollment.

### 12.4 Bardoxolone methyl (CARDINAL) — efficacy signals vs outcome/safety concerns
A Bardoxolone methyl phase 2/3 program (CARDINAL) reported on-treatment eGFR differences versus placebo:
- mean difference at 48 weeks **+9.2 mL/min/1.73 m²** (97.5% CI 5.1 to 13.4; p<0.001)
- mean difference at 100 weeks **+7.4 mL/min/1.73 m²** (95% CI 3.1 to 11.7; p<0.001)
- effect diminished after washout but persisted at week 52 (**+5.4 mL/min/1.73 m²**). (sarfraz2025systematicreviewof pages 3-5)

However, a detailed commentary emphasizes lack of demonstrated nephroprotection on hard outcomes and substantial safety signals:
- “exactly the same number of patients (n = 3) in each group developed kidney failure” (ruggenenti2023thecardinaltrial pages 3-4)
- liver enzyme elevations: “increase in liver enzymes in **70 of the 77 (90.9%)** bardoxolone-treated patients” (ruggenenti2023thecardinaltrial pages 1-2)
- FDA rejection and advisory committee unanimous vote against approval. (ruggenenti2023thecardinaltrial pages 4-5)

**MAXO suggestions:** NRF2 activator therapy (investigational; not recommended in practice based on safety/efficacy concerns);
Drug safety monitoring.

### 12.5 Advanced therapeutics (gene/RNA/editing; recent research)
Recent preclinical and translational directions include exon-skipping, AAV-based gene therapy approaches, and iPSC-derived organoids for therapeutic testing.
- **Exon skipping (mouse model):** podocyte-specific exon 21 skipping after disease onset “restored truncated collagen IV α5 expression, improved renal function, and ameliorated glomerular and tubular pathology,” including reversal of glomerular injury when initiated after proteinuria onset. ()
- **Kidney organoid model (human iPSC):** COL4A5 mutation-corrected iPSCs restored collagen α5(IV) expression in organoids; a chemical chaperone (4-phenyl butyric acid) showed potential to correct GBM abnormalities in mild phenotypes. ()

---

## 13. Prevention

Because Alport syndrome is genetic, prevention is primarily **genetic and secondary prevention**:
- **Cascade genetic testing** to identify at-risk relatives was recommended in workshop-era guidance. (daga2022the2019and pages 2-3)
- **Early detection of haematuria/proteinuria** and early initiation of kidney-protective therapy (RAS blockade) is emphasized as improving prognosis. (kang2024acomprehensivereview pages 8-10)

**MAXO suggestions:** Genetic counseling; Cascade genetic screening; Early ACE inhibitor therapy.

---

## 14. Other Species / Natural Disease

Naturally occurring Alport-like diseases in companion animals were not identified in the retrieved evidence.

---

## 15. Model Organisms and Experimental Models

### 15.1 Mouse models
- **Col4a3−/−** mice are widely used and show ocular anomalies similar to human AS; studies describe altered collagen IV expression and retinal/corneal/lens abnormalities. ()
- A novel **Col4a5 splicing-mutation** mouse (CRISPR/Cas9) showed progressive kidney deterioration, fibrosis, and immune cell infiltration, serving as an XLAS model. ()

### 15.2 Human in vitro models
- **iPSC-derived collagen α5(IV)-expressing kidney organoids** model mild vs severe AS and can be used for drug discovery and testing restoration strategies. ()

---

## Recent developments (2023–2024 emphasis) and real-world implementation highlights
- **Genotype-first diagnosis:** guideline-level recommendation for joint COL4A3/4/5 analysis as key initial test (implementation: broader NGS adoption, reduced need for biopsy in many cases). (torra2025diagnosismanagementand pages 1-2, lee2024pathologicaldiagnosisof pages 2-5)
- **Expanded testing indications** beyond classical triad to include FSGS and unexplained ESKD—reflecting genomic medicine’s reclassification of glomerular diseases. (savige2021consensusstatementon pages 1-2, savige2021consensusstatementon pages 2-3)
- **SGLT2 inhibitor movement into AS:** guideline “may be added” for proteinuric adults plus multiple ongoing/proposed studies including pediatric RCT design. (torra2025diagnosismanagementand pages 1-2)
- **miR-21 targeting and other molecular therapies:** early-phase RG-012 completed with biomarker endpoints; lademirsen terminated for futility (showing the field’s iterative learning). (NCT03373786 chunk 1, NCT02855268 chunk 1)

---

## Source URLs and publication dates (where available in evidence)
- ERKNet/ERA/ESPN guideline (published Dec 2025; labeled “2024 guideline”): https://doi.org/10.1093/ndt/gfae265 (torra2025diagnosismanagementand pages 1-2)
- Kang et al., comprehensive review (Sep 2024): https://doi.org/10.23876/j.krcp.24.065 (kang2024acomprehensivereview pages 1-3)
- Lee et al., pathological diagnosis (Aug 2024): https://doi.org/10.23876/j.krcp.24.063 (lee2024pathologicaldiagnosisof pages 2-5)
- Savige et al., molecular diagnostics consensus (Apr 2021): https://doi.org/10.1038/s41431-021-00858-1 (savige2021consensusstatementon pages 1-2)
- Daga et al., international workshops report (Mar 2022): https://doi.org/10.1038/s41431-022-01075-0 (daga2022the2019and pages 2-3)
- Ruggenenti commentary on CARDINAL (Feb 2023): https://doi.org/10.1159/000529471 (ruggenenti2023thecardinaltrial pages 1-2)
- ClinicalTrials.gov: NCT02855268; NCT03373786; NCT06226896 (NCT06226896 chunk 1, NCT03373786 chunk 1, NCT02855268 chunk 1)

---

## Limitations of this report (evidence access)
- PMID-specific citations were requested; however, **PMIDs were not available in the retrieved evidence snippets for most sources**, and this report therefore cites using the provided context IDs plus DOI/URL where available.
- Orphanet, ICD, and MeSH identifiers could not be extracted from the available tool-retrieved documents.
- Several therapeutic and mechanistic claims in the field (e.g., additional 2023–2024 RCTs or specific registry outcomes) may exist but were not accessible in the retrieved evidence set and are not stated here.

References

1. (torra2025diagnosismanagementand pages 1-2): Roser Torra, Beata Lipska-Zietkiewicz, Frederic Acke, Corinne Antignac, Jan Ulrich Becker, Emilie Cornec-Le Gall, Albertien M van Eerde, Nicolas Feltgen, Rossella Ferrari, Daniel P Gale, Susie Gear, Oliver Gross, Stefanie Haeberle, Laurence Heidet, Rachel Lennon, Laura Massella, Kristina Pfau, Maria del Prado Venegas Pizarro, Rezan Topaloglu, Tanja Wlodkowski, Heidi Zealey, Oana Ailioaie, Marina Aksenova, Peter Barany, Moumita Barua, Elisa Benetti, Lisa Bonebrake, Olivier Bonny, Antonia Bouts, Olivia Boyer, Gianluca Caridi, Cristina Castro-Alonso, Kathleen Claes, Peter Conlon, George Claudiu Costea, Stéphane Decramer, Constantinos Deltas, Erol Demir, Nathalie Demoulin, Mark Eijgelsheim, Francesco Emma, Frances Flinter, Monica Furlano, Danica Galešić Ljubanović, Valentine Gillion, Ana Marta Gomes, Dieter Haffner, Julia Hoefele, Svetlana Jovicic Pavlovic, Clifford Kashtan, Stefan Kohl, Martin Konrad, Matjaž Kopač, Sandrine Lemoine, Max Christoph Liebau, Francesca Lugani, Alvaro Madrid, Andrew Mallett, Antonio Mastrangelo, Anamarija Meglič, Esther Meijer, Jeffrey Miner, Sevgı Mır, Kar Hui Ng, João Paulo Oliveira, Maria Vanessa Perez Gomez, Anna Maria Pinto, Ann Raes, Michelle Rheault, Judy Savige, Christoph Schwarz, Angel Manuel Sevillano Prieto, Ekamol Tantisattamo, Velibor Tasic, Kálmán Tory, Neil Turner, Andre Weinstock, and Izabela Zakrocka. Diagnosis, management and treatment of the alport syndrome – 2024 guideline on behalf of erknet, era and espn. Nephrology Dialysis Transplantation, 40:1091-1106, Dec 2025. URL: https://doi.org/10.1093/ndt/gfae265, doi:10.1093/ndt/gfae265. This article has 43 citations and is from a domain leading peer-reviewed journal.

2. (kang2024acomprehensivereview pages 5-6): Eunjeong Kang, Byung Hwa Park, Hajeong Lee, Hee Gyung Kang, Ji Hyun Kim, Ye Na Kim, Yeonsoon Jung, Hark Rim, and Ho Sik Shin. A comprehensive review of alport syndrome: definition, pathophysiology, clinical manifestations, and diagnostic considerations. Kidney Research and Clinical Practice, 44:566-575, Sep 2024. URL: https://doi.org/10.23876/j.krcp.24.065, doi:10.23876/j.krcp.24.065. This article has 6 citations.

3. (liang2023moleculardynamicsand pages 1-2): Lei Liang, Haotian Wu, Zeyu Cai, and Jianrong Zhao. Molecular dynamics and minigene assay of new splicing variant c.4298-20t>a of col4a5 gene that cause alport syndrome. Frontiers in Genetics, Feb 2023. URL: https://doi.org/10.3389/fgene.2023.1059322, doi:10.3389/fgene.2023.1059322. This article has 9 citations and is from a peer-reviewed journal.

4. (kang2024acomprehensivereview pages 1-3): Eunjeong Kang, Byung Hwa Park, Hajeong Lee, Hee Gyung Kang, Ji Hyun Kim, Ye Na Kim, Yeonsoon Jung, Hark Rim, and Ho Sik Shin. A comprehensive review of alport syndrome: definition, pathophysiology, clinical manifestations, and diagnostic considerations. Kidney Research and Clinical Practice, 44:566-575, Sep 2024. URL: https://doi.org/10.23876/j.krcp.24.065, doi:10.23876/j.krcp.24.065. This article has 6 citations.

5. (kang2024acomprehensivereview pages 3-5): Eunjeong Kang, Byung Hwa Park, Hajeong Lee, Hee Gyung Kang, Ji Hyun Kim, Ye Na Kim, Yeonsoon Jung, Hark Rim, and Ho Sik Shin. A comprehensive review of alport syndrome: definition, pathophysiology, clinical manifestations, and diagnostic considerations. Kidney Research and Clinical Practice, 44:566-575, Sep 2024. URL: https://doi.org/10.23876/j.krcp.24.065, doi:10.23876/j.krcp.24.065. This article has 6 citations.

6. (daga2022the2019and pages 2-3): Sergio Daga, Jie Ding, Constantinos Deltas, Judy Savige, Beata S. Lipska-Ziętkiewicz, Julia Hoefele, Frances Flinter, Daniel P. Gale, Marina Aksenova, Hirofumi Kai, Laura Perin, Moumita Barua, Roser Torra, Jeff H. Miner, Laura Massella, Danica Galešić Ljubanović, Rachel Lennon, Andrè B. Weinstock, Bertrand Knebelmann, Agne Cerkauskaite, Susie Gear, Oliver Gross, A. Neil Turner, Margherita Baldassarri, Anna Maria Pinto, and Alessandra Renieri. The 2019 and 2021 international workshops on alport syndrome. European Journal of Human Genetics, 30:507-516, Mar 2022. URL: https://doi.org/10.1038/s41431-022-01075-0, doi:10.1038/s41431-022-01075-0. This article has 41 citations and is from a domain leading peer-reviewed journal.

7. (savige2021consensusstatementon pages 1-2): Judy Savige, Helen Storey, Elizabeth Watson, Jens Michael Hertz, Constantinos Deltas, Alessandra Renieri, Francesca Mari, Pascale Hilbert, Pavlina Plevova, Peter Byers, Agne Cerkauskaite, Martin Gregory, Rimante Cerkauskiene, Danica Galesic Ljubanovic, Francesca Becherucci, Carmela Errichiello, Laura Massella, Valeria Aiello, Rachel Lennon, Louise Hopkinson, Ania Koziell, Adrian Lungu, Hansjorg Martin Rothe, Julia Hoefele, Miriam Zacchia, Tamara Nikuseva Martic, Asheeta Gupta, Albertien van Eerde, Susie Gear, Samuela Landini, Viviana Palazzo, Laith al-Rabadi, Kathleen Claes, Anniek Corveleyn, Evelien Van Hoof, Micheel van Geel, Maggie Williams, Emma Ashton, Hendica Belge, Elisabeth Ars, Agnieszka Bierzynska, Concetta Gangemi, and Beata S. Lipska-Ziętkiewicz. Consensus statement on standards and guidelines for the molecular diagnostics of alport syndrome: refining the acmg criteria. European Journal of Human Genetics, 29:1186-1197, Apr 2021. URL: https://doi.org/10.1038/s41431-021-00858-1, doi:10.1038/s41431-021-00858-1. This article has 137 citations and is from a domain leading peer-reviewed journal.

8. (daga2022the2019and pages 1-2): Sergio Daga, Jie Ding, Constantinos Deltas, Judy Savige, Beata S. Lipska-Ziętkiewicz, Julia Hoefele, Frances Flinter, Daniel P. Gale, Marina Aksenova, Hirofumi Kai, Laura Perin, Moumita Barua, Roser Torra, Jeff H. Miner, Laura Massella, Danica Galešić Ljubanović, Rachel Lennon, Andrè B. Weinstock, Bertrand Knebelmann, Agne Cerkauskaite, Susie Gear, Oliver Gross, A. Neil Turner, Margherita Baldassarri, Anna Maria Pinto, and Alessandra Renieri. The 2019 and 2021 international workshops on alport syndrome. European Journal of Human Genetics, 30:507-516, Mar 2022. URL: https://doi.org/10.1038/s41431-022-01075-0, doi:10.1038/s41431-022-01075-0. This article has 41 citations and is from a domain leading peer-reviewed journal.

9. (daga2022the2019and pages 3-4): Sergio Daga, Jie Ding, Constantinos Deltas, Judy Savige, Beata S. Lipska-Ziętkiewicz, Julia Hoefele, Frances Flinter, Daniel P. Gale, Marina Aksenova, Hirofumi Kai, Laura Perin, Moumita Barua, Roser Torra, Jeff H. Miner, Laura Massella, Danica Galešić Ljubanović, Rachel Lennon, Andrè B. Weinstock, Bertrand Knebelmann, Agne Cerkauskaite, Susie Gear, Oliver Gross, A. Neil Turner, Margherita Baldassarri, Anna Maria Pinto, and Alessandra Renieri. The 2019 and 2021 international workshops on alport syndrome. European Journal of Human Genetics, 30:507-516, Mar 2022. URL: https://doi.org/10.1038/s41431-022-01075-0, doi:10.1038/s41431-022-01075-0. This article has 41 citations and is from a domain leading peer-reviewed journal.

10. (adone2023alportsyndromea pages 3-4): Avanti Adone and Ashish P Anjankar. Alport syndrome: a comprehensive review. Cureus, Oct 2023. URL: https://doi.org/10.7759/cureus.47129, doi:10.7759/cureus.47129. This article has 24 citations.

11. (lee2024pathologicaldiagnosisof pages 2-5): Kyoung Bun Lee, Minsun Jung, and Beom Jin Lim. Pathological diagnosis of alport syndrome. Kidney Research and Clinical Practice, 44:406-410, Aug 2024. URL: https://doi.org/10.23876/j.krcp.24.063, doi:10.23876/j.krcp.24.063. This article has 3 citations.

12. (lee2024pathologicaldiagnosisof media 9c957d59): Kyoung Bun Lee, Minsun Jung, and Beom Jin Lim. Pathological diagnosis of alport syndrome. Kidney Research and Clinical Practice, 44:406-410, Aug 2024. URL: https://doi.org/10.23876/j.krcp.24.063, doi:10.23876/j.krcp.24.063. This article has 3 citations.

13. (lee2024pathologicaldiagnosisof media 091648f1): Kyoung Bun Lee, Minsun Jung, and Beom Jin Lim. Pathological diagnosis of alport syndrome. Kidney Research and Clinical Practice, 44:406-410, Aug 2024. URL: https://doi.org/10.23876/j.krcp.24.063, doi:10.23876/j.krcp.24.063. This article has 3 citations.

14. (savige2021consensusstatementon pages 2-3): Judy Savige, Helen Storey, Elizabeth Watson, Jens Michael Hertz, Constantinos Deltas, Alessandra Renieri, Francesca Mari, Pascale Hilbert, Pavlina Plevova, Peter Byers, Agne Cerkauskaite, Martin Gregory, Rimante Cerkauskiene, Danica Galesic Ljubanovic, Francesca Becherucci, Carmela Errichiello, Laura Massella, Valeria Aiello, Rachel Lennon, Louise Hopkinson, Ania Koziell, Adrian Lungu, Hansjorg Martin Rothe, Julia Hoefele, Miriam Zacchia, Tamara Nikuseva Martic, Asheeta Gupta, Albertien van Eerde, Susie Gear, Samuela Landini, Viviana Palazzo, Laith al-Rabadi, Kathleen Claes, Anniek Corveleyn, Evelien Van Hoof, Micheel van Geel, Maggie Williams, Emma Ashton, Hendica Belge, Elisabeth Ars, Agnieszka Bierzynska, Concetta Gangemi, and Beata S. Lipska-Ziętkiewicz. Consensus statement on standards and guidelines for the molecular diagnostics of alport syndrome: refining the acmg criteria. European Journal of Human Genetics, 29:1186-1197, Apr 2021. URL: https://doi.org/10.1038/s41431-021-00858-1, doi:10.1038/s41431-021-00858-1. This article has 137 citations and is from a domain leading peer-reviewed journal.

15. (chen2025novelcol4a3–col4a5variants pages 3-4): Ji-Yu Chen, Xue-Mei Jiang, Ya-Bin Liao, Yan-Hua Zhang, Mi-feng Yang, Jing-Jing Cui, Jing Wang, Jia Zhang, Hong-Ye Wang, and Bo Zhao. Novel col4a3–col4a5 variants and digenic inheritance in pediatric alport syndrome from southwestern china. Scientific Reports, Aug 2025. URL: https://doi.org/10.1038/s41598-025-17027-9, doi:10.1038/s41598-025-17027-9. This article has 0 citations and is from a peer-reviewed journal.

16. (kang2024acomprehensivereview pages 8-10): Eunjeong Kang, Byung Hwa Park, Hajeong Lee, Hee Gyung Kang, Ji Hyun Kim, Ye Na Kim, Yeonsoon Jung, Hark Rim, and Ho Sik Shin. A comprehensive review of alport syndrome: definition, pathophysiology, clinical manifestations, and diagnostic considerations. Kidney Research and Clinical Practice, 44:566-575, Sep 2024. URL: https://doi.org/10.23876/j.krcp.24.065, doi:10.23876/j.krcp.24.065. This article has 6 citations.

17. (ruggenenti2023thecardinaltrial pages 1-2): Piero Ruggenenti. The cardinal trial of bardoxolone methyl in alport syndrome: when marketing interests prevail over patients clinical needs. Nephron, 147:465-469, Feb 2023. URL: https://doi.org/10.1159/000529471, doi:10.1159/000529471. This article has 16 citations.

18. (ruggenenti2023thecardinaltrial pages 3-4): Piero Ruggenenti. The cardinal trial of bardoxolone methyl in alport syndrome: when marketing interests prevail over patients clinical needs. Nephron, 147:465-469, Feb 2023. URL: https://doi.org/10.1159/000529471, doi:10.1159/000529471. This article has 16 citations.

19. (sarfraz2025systematicreviewof pages 3-5): Zouina Sarfraz, Ayesha Khan, Maryyam Liaqat, Aden Khan, Faheem Javad, Meher Saleem, Azza Sarfraz, Musfira Khalid, Muzna Sarfraz, Manish Kc, and Omar Irfan. Systematic review of management strategies for alport syndrome: implications for male patients. Health Science Reports, Mar 2025. URL: https://doi.org/10.1002/hsr2.70595, doi:10.1002/hsr2.70595. This article has 2 citations and is from a peer-reviewed journal.

20. (ruggenenti2023thecardinaltrial pages 4-5): Piero Ruggenenti. The cardinal trial of bardoxolone methyl in alport syndrome: when marketing interests prevail over patients clinical needs. Nephron, 147:465-469, Feb 2023. URL: https://doi.org/10.1159/000529471, doi:10.1159/000529471. This article has 16 citations.

21. (NCT03373786 chunk 1):  A Study of RG-012 in Subjects With Alport Syndrome. Genzyme, a Sanofi Company. 2017. ClinicalTrials.gov Identifier: NCT03373786

22. (NCT02855268 chunk 1):  Study of Lademirsen (SAR339375) in Patients With Alport Syndrome. Genzyme, a Sanofi Company. 2019. ClinicalTrials.gov Identifier: NCT02855268

23. (NCT06226896 chunk 1): Zhi-Hong Liu, MD. Effects of Dapagliflozin on Progression of Alport Syndrome. Nanjing University School of Medicine. 2023. ClinicalTrials.gov Identifier: NCT06226896

24. (NCT02378805 chunk 2): Prof. Dr. O. Gross. Alport Therapy Registry - European Initiative Towards Delaying Renal Failure in Alport Syndrome. University Hospital Goettingen. 1995. ClinicalTrials.gov Identifier: NCT02378805

25. (lujinschi2025candidategeneticmodifiers pages 1-2): Ștefan Nicolaie Lujinschi, Bogdan Marian Sorohan, Bogdan Obrișcă, Alexandra Vrabie, Elena Rusu, Diana Zilișteanu, Camelia Achim, Andreea Gabriella Andronesi, and Gener Ismail. Candidate genetic modifiers in alport syndrome: a case series. Life, 15:298, Feb 2025. URL: https://doi.org/10.3390/life15020298, doi:10.3390/life15020298. This article has 2 citations.

26. (lujinschi2025candidategeneticmodifiers pages 2-4): Ștefan Nicolaie Lujinschi, Bogdan Marian Sorohan, Bogdan Obrișcă, Alexandra Vrabie, Elena Rusu, Diana Zilișteanu, Camelia Achim, Andreea Gabriella Andronesi, and Gener Ismail. Candidate genetic modifiers in alport syndrome: a case series. Life, 15:298, Feb 2025. URL: https://doi.org/10.3390/life15020298, doi:10.3390/life15020298. This article has 2 citations.

27. (savige2021consensusstatementon pages 3-4): Judy Savige, Helen Storey, Elizabeth Watson, Jens Michael Hertz, Constantinos Deltas, Alessandra Renieri, Francesca Mari, Pascale Hilbert, Pavlina Plevova, Peter Byers, Agne Cerkauskaite, Martin Gregory, Rimante Cerkauskiene, Danica Galesic Ljubanovic, Francesca Becherucci, Carmela Errichiello, Laura Massella, Valeria Aiello, Rachel Lennon, Louise Hopkinson, Ania Koziell, Adrian Lungu, Hansjorg Martin Rothe, Julia Hoefele, Miriam Zacchia, Tamara Nikuseva Martic, Asheeta Gupta, Albertien van Eerde, Susie Gear, Samuela Landini, Viviana Palazzo, Laith al-Rabadi, Kathleen Claes, Anniek Corveleyn, Evelien Van Hoof, Micheel van Geel, Maggie Williams, Emma Ashton, Hendica Belge, Elisabeth Ars, Agnieszka Bierzynska, Concetta Gangemi, and Beata S. Lipska-Ziętkiewicz. Consensus statement on standards and guidelines for the molecular diagnostics of alport syndrome: refining the acmg criteria. European Journal of Human Genetics, 29:1186-1197, Apr 2021. URL: https://doi.org/10.1038/s41431-021-00858-1, doi:10.1038/s41431-021-00858-1. This article has 137 citations and is from a domain leading peer-reviewed journal.