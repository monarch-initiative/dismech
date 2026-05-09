---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T15:16:00.898206'
end_time: '2026-05-08T15:26:15.455085'
duration_seconds: 614.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Familial Adenomatous Polyposis
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Adenomatous Polyposis
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Familial Adenomatous Polyposis** covering all of the
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
- **Disease Name:** Familial Adenomatous Polyposis
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Familial Adenomatous Polyposis** covering all of the
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


# Familial Adenomatous Polyposis (FAP): Disease Characteristics Research Report (2026-05-08)

## Executive summary
Familial adenomatous polyposis (FAP) is an autosomal dominant hereditary colorectal adenomatous polyposis syndrome caused primarily by germline loss-of-function pathogenic variants in **APC**, leading to the development of hundreds-to-thousands of colorectal adenomas beginning in late childhood/adolescence and (if untreated) an approximately inevitable progression to colorectal cancer (CRC). (joo2025geneticsgenomicsand pages 1-2, kyriakidis2023updatedperspectiveson pages 1-2, ditonno2023molecularpathwaysof pages 1-2)

Key 2023–2024 themes in the literature retrieved here include: (i) **personalized endoscopic surveillance protocols** proposed by the European FAP Consortium to standardize lower- and upper-GI surveillance and endoscopic interventions, with prospective evaluation planned; (ii) expanding focus on **APC post-zygotic (somatic) mosaicism** and the need for mosaicism-aware testing strategies; and (iii) persistent lack of an ideal **chemopreventive** drug despite many trials, with new pathway targets (eg, mTOR) and ongoing/early-phase strategies. (kyriakidis2023updatedperspectiveson pages 10-12, aelvoet2023personalizedendoscopicsurveillance pages 3-5, aelvoet2023personalizedendoscopicsurveillance pages 5-6)

---

## 1. Disease information

### 1.1 Definition and overview
FAP is a hereditary cancer syndrome characterized by extensive colorectal adenomatous polyposis (classically hundreds-to-thousands of adenomas) starting in adolescence; without risk-reducing surgery, CRC is near-certain by mid-adulthood (often by ~50 years). (kyriakidis2023updatedperspectiveson pages 1-2, ditonno2023molecularpathwaysof pages 1-2)

Attenuated FAP (AFAP/aFAP) is a milder clinical form typically presenting with **fewer than 100** colorectal adenomas and later onset (often >40 years), and is also associated with specific regions of APC pathogenic variants. (kyriakidis2023updatedperspectiveson pages 1-2, ditonno2023molecularpathwaysof pages 2-4)

### 1.2 Key identifiers and synonyms
A structured set of identifiers/synonyms is summarized in the artifact below; note that **MONDO/Orphanet/ICD/MeSH identifiers were not directly retrievable from the tool-accessed evidence** in this run, so those are flagged as “not retrieved.”

| Identifier system | Identifier/code | Name used in system | Notes |
|---|---|---|---|
| OMIM | #175100 | Familial adenomatous polyposis | OMIM number explicitly reported in a 2023 FAP case report; FAP described as APC-related hereditary colorectal polyposis (kyriakidis2023updatedperspectiveson pages 1-2, ditonno2023molecularpathwaysof pages 1-2) |
| Orphanet | not retrieved in tool evidence | not retrieved in tool evidence | Not directly retrieved from gathered evidence |
| ICD-10 | not retrieved in tool evidence | not retrieved in tool evidence | Not directly retrieved from gathered evidence |
| ICD-11 | not retrieved in tool evidence | not retrieved in tool evidence | Not directly retrieved from gathered evidence |
| MeSH | not retrieved in tool evidence | not retrieved in tool evidence | Not directly retrieved from gathered evidence |
| MONDO | not retrieved in tool evidence | not retrieved in tool evidence | Not directly retrieved from gathered evidence |

| Synonym / related entity | Relationship to FAP | Notes |
|---|---|---|
| Classic FAP | Core disease form | Defined by hundreds to thousands of colorectal adenomas; commonly operationalized as ≥100 adenomas in comparative guideline/review evidence (zare2025guidelinesforfamilial pages 1-2, kyriakidis2023updatedperspectiveson pages 1-2, zare2025guidelinesforfamilial pages 4-4) |
| Attenuated FAP (AFAP, aFAP) | Recognized milder allelic/clinical form | Later onset, usually <100 adenomas, milder phenotype; APC-associated (kyriakidis2023updatedperspectiveson pages 2-4, kyriakidis2023updatedperspectiveson pages 1-2, ditonno2023molecularpathwaysof pages 2-4) |
| APC-associated polyposis conditions | Broader umbrella related to FAP | Supported indirectly by evidence discussing APC-driven polyposis spectrum and APC-specific variants/promoter disease; exact formal label not retrieved in tool evidence (joo2025geneticsgenomicsand pages 1-2, ditonno2023molecularpathwaysof pages 1-2) |
| Gardner syndrome | Historical/phenotypic variant related to FAP | Exact definition not retrieved in tool evidence; extracolonic features such as osteomas, dental abnormalities, skin lesions, and CHRPE are reported within FAP spectrum, consistent with historical Gardner terminology (joo2025geneticsgenomicsand pages 1-2, ditonno2023molecularpathwaysof pages 1-2) |
| Turcot syndrome | Historical overlap term | Exact definition not retrieved in tool evidence; medulloblastoma is listed among extracolonic malignant risks in FAP, consistent with historical overlap usage (joo2025geneticsgenomicsand pages 1-2, kyriakidis2023updatedperspectiveson pages 1-2) |


*Table: This artifact summarizes disease identifiers explicitly supported by the gathered evidence and distinguishes between directly retrieved identifiers versus those not retrieved. The second table clarifies commonly used synonyms and historical related entities relevant to interpreting FAP literature and knowledge-base mapping.*

**Evidence source type note:** The overview/identifier information above is derived from aggregated review/guideline-type resources plus some patient-level case series/case reports. (joo2025geneticsgenomicsand pages 1-2, kyriakidis2023updatedperspectiveson pages 1-2, alhassan2024surveillancecomplianceand pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause (genetic):** Germline pathogenic variants in **APC** (tumor suppressor) are the main cause of autosomal dominant FAP, with tumor initiation typically requiring a somatic “second hit” in the remaining functional allele, activating Wnt/β-catenin signaling. (joo2025geneticsgenomicsand pages 1-2, ditonno2023molecularpathwaysof pages 2-4)

**Direct abstract quote (mechanistic framing):** A 2023 mechanistic review describes FAP as being “based on a loss of function mutation in adenomatous polyposis coli (APC), a tumor-suppressor gene, inherited following a Mendelian pattern.” (ditonno2023molecularpathwaysof pages 1-2)

### 2.2 Risk factors
#### Genetic risk factors
* **APC pathogenic variant location and phenotype:** Classical FAP tends to be associated with truncating variants; mutation site influences phenotype severity, including extracolonic risks (eg, desmoids). (kyriakidis2023updatedperspectiveson pages 2-4, ditonno2023molecularpathwaysof pages 2-4)
* **De novo APC variants:** Up to ~30% of APC pathogenic variants may occur de novo, contributing to apparently sporadic presentations. (joo2025geneticsgenomicsand pages 1-2)
* **Somatic (post-zygotic) mosaicism:** Post-zygotic APC mosaicism is a clinically important cause of FAP-like phenotypes and complicates detection when only leukocyte DNA is tested. A 2024 systematic review/meta-analysis across CRC/polyposis syndromes (27 studies, 2272 patients) reported an overall mosaicism prevalence of **8.79%** (95% CI 5.1–14.70%), and emphasized incorporating mosaicism screening into routine testing for at-risk patients. (moraes2024genomicmosaicismin pages 9-11)
  * **Real-world diagnostic yield:** In a Danish nationwide re-evaluation of “colorectal polyposis of unknown etiology” (>100 cumulative adenomas), adding WGS and mosaicism screening increased variant detection; **pathogenic variants were detected in 16/27 families (60%)**, and the registry’s proportion of families with known etiology increased to **93%**. (karstensen2024reevaluatingthegenotypes pages 1-2)

#### Environmental/lifestyle and other non-genetic contributors
Non-genetic contributors are increasingly discussed as potential modifiers/alternative mechanisms in multi-adenoma patients, including environmental factors and bacterial genotoxins (eg, colibactin-producing *E. coli*), but specific quantified gene–environment interactions were not retrieved in the evidence set used here. (joo2025geneticsgenomicsand pages 1-2)

### 2.3 Protective factors
Specific, validated protective lifestyle factors or protective genetic alleles were not quantified in the retrieved evidence. A 2025 cohort (postoperative patients) suggested procedural choices may reduce desmoid risk (see below). ()

### 2.4 Gene–environment interactions
The retrieved evidence notes that moderate-risk genes and inherited cancer risk may be influenced by **gene–gene or gene–environment interactions** in general (NCCN guideline discussion of multigene testing), but it does not provide FAP-specific interaction estimates. (hodan2024geneticfamilialhighriskassessment pages 6-7)

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (with HPO term suggestions)
A structured phenotype-to-HPO mapping (with only evidence-supported frequencies/risks) is provided below.

| Phenotype | HPO term (suggest) | Evidence-based frequency/risk (with age if stated) | Notes (onset/clinical relevance) | Key citations (IDs) |
|---|---|---|---|---|
| Colorectal adenomatous polyposis | HP:0002671 Colorectal polyposis | Classic FAP: hundreds to thousands of adenomas; attenuated FAP: usually <100 adenomas; polyps typically begin in adolescence / late childhood | Core defining phenotype of FAP; attenuated form has later onset and milder burden | (joo2025geneticsgenomicsand pages 1-2, kyriakidis2023updatedperspectiveson pages 1-2, ditonno2023molecularpathwaysof pages 1-2, ditonno2023molecularpathwaysof pages 2-4) |
| Colorectal cancer | HP:0003003 Colon carcinoma | ~100% lifetime risk if untreated; near-certain CRC by ~50 years without prophylactic surgery; CRC around age 39 in one cited clinical summary | Principal malignant consequence and rationale for prophylactic colectomy and early surveillance | (kyriakidis2023updatedperspectiveson pages 1-2, alhassan2024surveillancecomplianceand pages 1-2, ditonno2023molecularpathwaysof pages 1-2) |
| Duodenal adenomas / duodenal cancer | HP:0100837 Duodenal adenoma; HP:0006749 Duodenal carcinoma | Duodenal cancer cumulative risk ~4.5% by age 57 years and ~18% by age 75 years | Major extracolonic GI manifestation; upper GI surveillance is standard; European FAP Consortium recommends resection of duodenal adenomas ≥10 mm | (kyriakidis2023updatedperspectiveson pages 1-2, aelvoet2023personalizedendoscopicsurveillance pages 3-5, aelvoet2023personalizedendoscopicsurveillance pages 5-6) |
| Gastric polyposis / gastric cancer | HP:0034390 Gastric polyposis; HP:0006753 Stomach carcinoma | Upper GI polyps in ~50% (clinical summary); gastric cancer risk not quantified in retrieved evidence | Fundic gland polyposis and gastric adenomas are recognized; recent concern about gastric cancer during surveillance, but numeric lifetime risk not quantified in retrieved evidence | (alhassan2024surveillancecomplianceand pages 1-2, aelvoet2023personalizedendoscopicsurveillance pages 3-5, aelvoet2023personalizedendoscopicsurveillance pages 5-6) |
| Desmoid tumors | HP:0010302 Desmoid tumor | 20% reported frequency in FAP; in a 2025 postoperative cohort, 21/202 (10.4%) developed intra-abdominal desmoids after surgery | Often mesenteric/intra-abdominal; major cause of morbidity and important in surgical decision-making; risk linked to genotype and operative factors | (kyriakidis2023updatedperspectiveson pages 1-2, ditonno2023molecularpathwaysof pages 1-2) |
| Congenital hypertrophy of retinal pigment epithelium (CHRPE) | HP:0007759 Congenital hypertrophy of retinal pigment epithelium | 60% | Common extracolonic feature that may precede intestinal manifestations and aid recognition of APC-associated disease | (kyriakidis2023updatedperspectiveson pages 1-2) |
| Osteomas | HP:0002796 Osteoma | 20% | Classic extracolonic manifestation within the Gardner-spectrum phenotype of FAP | (kyriakidis2023updatedperspectiveson pages 1-2, ditonno2023molecularpathwaysof pages 1-2) |
| Dental abnormalities | HP:0100339 Abnormality of dentition | not quantified in retrieved evidence | Includes dental anomalies/supernumerary teeth in APC-associated disease; may precede intestinal polyposis and support early recognition | (joo2025geneticsgenomicsand pages 1-2, ditonno2023molecularpathwaysof pages 1-2) |
| Thyroid cancer | HP:0009726 Thyroid carcinoma | 1%–2% (papillary thyroid carcinoma in cited review) | Recognized extracolonic malignancy; often cited as papillary/cribriform-morular thyroid carcinoma in APC-associated disease | (kyriakidis2023updatedperspectiveson pages 1-2, joo2025geneticsgenomicsand pages 1-2) |
| Hepatoblastoma | HP:0002898 Hepatoblastoma | 1%–2% | Rare pediatric extracolonic malignancy associated with FAP/APC pathogenic variants | (kyriakidis2023updatedperspectiveson pages 1-2, ditonno2023molecularpathwaysof pages 2-4) |
| Medulloblastoma | HP:0002885 Medulloblastoma | 1%–2% | Rare CNS malignancy reported in the FAP spectrum; historically overlaps with Turcot terminology | (kyriakidis2023updatedperspectiveson pages 1-2, joo2025geneticsgenomicsand pages 1-2) |


*Table: This table maps major familial adenomatous polyposis phenotypes to suggested HPO terms and summarizes only the frequencies or risks explicitly supported in the retrieved evidence. It is useful for building structured phenotype annotations for a disease knowledge base while preserving citation traceability.*

### 3.2 Upper GI disease and emerging concern for gastric cancer
Upper GI manifestations (duodenal and gastric polyposis/adenomas) are major contributors to morbidity after colorectal risk reduction. A European FAP Consortium paper emphasizes improved upper-GI lesion detection (eg, using NBI/BLI to distinguish gastric adenomas among fundic gland polyps) and provides consensus thresholds for intervention. (aelvoet2023personalizedendoscopicsurveillance pages 3-5, aelvoet2023personalizedendoscopicsurveillance pages 5-6)

### 3.3 Quality of life impact (evidence example)
A 2024 single-center cohort of surgically treated FAP patients in Saudi Arabia used SF-36 and reported mean domain scores above 60, while also documenting surveillance adherence gaps (see “Diagnostics/Screening” for implementation implications). (alhassan2024surveillancecomplianceand pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
* **APC** (tumor suppressor; central gatekeeper in colorectal tumorigenesis; Wnt signaling regulator). (ditonno2023molecularpathwaysof pages 1-2, ditonno2023molecularpathwaysof pages 2-4)

### 4.2 Pathogenic variant types and functional consequences
* Many classical FAP germline variants are **nonsense or frameshift** truncating variants (reported in a 2023 mechanistic review as common, up to ~80% of cases in that review’s summary framing). (ditonno2023molecularpathwaysof pages 2-4)
* Variant type/location influences residual APC function and thereby phenotype. (ditonno2023molecularpathwaysof pages 2-4)

### 4.3 Mosaicism and structural variants (diagnostic relevance)
* Mosaicism detection can require analysis beyond blood (eg, adenoma tissue). (kyriakidis2023updatedperspectiveson pages 2-4, karstensen2024reevaluatingthegenotypes pages 1-2)
* WGS can uncover structural variants missed by standard testing; in the Danish cohort, WGS identified additional APC structural variants. (karstensen2024reevaluatingthegenotypes pages 1-2)

### 4.4 Modifier genes and epigenetics
The retrieved evidence set references phenotypic variability and broader polyposis genetics, but does not provide a definitive, quantified list of FAP modifier genes or epigenetic signatures suitable for a curated knowledge base entry. (joo2025geneticsgenomicsand pages 1-2, ditonno2023molecularpathwaysof pages 2-4)

---

## 5. Environmental information
Specific environmental exposures causally linked to FAP onset are not applicable in the same way as multifactorial diseases because FAP is primarily monogenic (APC). Environmental and microbial factors are discussed as potential contributors/modifiers of colorectal carcinogenesis and polyposis phenotype variability, but detailed exposure-specific statistics were not retrieved here. (joo2025geneticsgenomicsand pages 1-2, ditonno2023molecularpathwaysof pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Canonical pathway: APC loss → Wnt/β-catenin activation → adenoma initiation
A key mechanistic chain in FAP is loss of APC function, disabling the β-catenin “destruction complex,” leading to nuclear β-catenin accumulation and transcriptional activation of proliferative programs. (ditonno2023molecularpathwaysof pages 2-4)

**Upstream event:** germline APC loss-of-function variant (first hit). **Downstream events:** somatic second hit in APC, adenoma formation, accumulation of additional driver events for carcinoma progression. (ditonno2023molecularpathwaysof pages 2-4)

### 6.2 “Two-hit” and “just-right” signaling concepts
The 2023 mechanistic review describes a Knudson two-hit model and summarizes evidence that the second hit may be selected to retain partial control of β-catenin signaling (“just-right” model), avoiding lethal overactivation while still promoting growth. (ditonno2023molecularpathwaysof pages 2-4)

### 6.3 Immune/microbiome/inflammation as modifiers (emerging themes)
Recent reviews highlight possible modifier mechanisms including gut microbiota changes, mucosal barrier immunity, immune microenvironment/inflammation, and hormonal factors (eg, estrogen) as potential chemoprevention targets, though this run did not retrieve specific multi-omics signatures for FAP. (ditonno2023molecularpathwaysof pages 1-2)

### 6.4 Suggested ontology terms
* **GO biological processes (suggest):** Wnt signaling pathway (GO:0016055), regulation of β-catenin-mediated signaling (GO:1904888), regulation of cell proliferation (GO:0042127), epithelial cell proliferation (GO:0050673).
* **CL cell types (suggest):** intestinal epithelial cell (CL:0000066), colonic epithelial cell (CL:0000584).

(These are ontology suggestions aligned to mechanisms described in retrieved sources; they are not explicitly enumerated in those sources.) (ditonno2023molecularpathwaysof pages 2-4)

---

## 7. Anatomical structures affected

### 7.1 Organ-level
* **Primary:** colon and rectum (adenomatous polyposis; CRC risk). (kyriakidis2023updatedperspectiveson pages 1-2)
* **Major secondary GI sites:** duodenum and stomach (adenomas/polyposis; cancer risks). (kyriakidis2023updatedperspectiveson pages 1-2, aelvoet2023personalizedendoscopicsurveillance pages 3-5)
* **Other extracolonic sites:** thyroid, retina (CHRPE), mesentery/abdominal soft tissues (desmoids), bone/dentition. (joo2025geneticsgenomicsand pages 1-2, kyriakidis2023updatedperspectiveson pages 1-2)

### 7.2 UBERON term suggestions
* Colon: UBERON:0001155
* Rectum: UBERON:0001052
* Duodenum: UBERON:0002114
* Stomach: UBERON:0000945
* Thyroid gland: UBERON:0002046

(Anatomy ontology suggestions; not explicitly provided in retrieved sources.)

---

## 8. Temporal development

### 8.1 Onset
Polyps commonly begin in late childhood/adolescence; one clinical summary reports typical polyp onset around age ~16 years. (alhassan2024surveillancecomplianceand pages 1-2)

### 8.2 Progression
Without prophylactic intervention, CRC can develop early; one clinical summary reports CRC around age ~39 years, and reviews emphasize near-certain CRC by ~50 years without surgery. (alhassan2024surveillancecomplianceand pages 1-2, kyriakidis2023updatedperspectiveson pages 1-2)

---

## 9. Inheritance and population

### 9.1 Inheritance
Autosomal dominant inheritance is consistently described, with high/near-complete penetrance for colorectal polyposis/CRC in the absence of intervention. (kyriakidis2023updatedperspectiveson pages 1-2, ditonno2023molecularpathwaysof pages 1-2)

### 9.2 Epidemiology (statistics)
* **Prevalence:** ~2.29–3.2 per 100,000 (reported in 2023 reviews). (kyriakidis2023updatedperspectiveson pages 1-2, ditonno2023molecularpathwaysof pages 1-2)
* **Birth incidence:** ~1 in 8,500 (reported in a 2025 review of adenomatous polyposis genetics). (joo2025geneticsgenomicsand pages 1-2)
* **Contribution to CRC burden:** ≤0.5% to ~1% of CRC, depending on the source framing. (joo2025geneticsgenomicsand pages 1-2, kyriakidis2023updatedperspectiveson pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical criteria and endoscopy
FAP is clinically diagnosed by extensive adenoma burden (often operationalized as **≥100 colorectal adenomas**), and/or by identification of a pathogenic/likely pathogenic APC variant. (kyriakidis2023updatedperspectiveson pages 2-4, zare2025guidelinesforfamilial pages 4-4)

### 10.2 Genetic testing strategies (current practice themes)
* **When familial APC variant known:** single-site testing is recommended (as summarized in a 2023 clinical genetics review referencing NCCN). (kyriakidis2023updatedperspectiveson pages 2-4)
* **When etiology uncertain:** multigene panels and, if negative, expanded approaches such as WGS and mosaicism assessment in adenomas can improve yield. (karstensen2024reevaluatingthegenotypes pages 1-2)

### 10.3 Screening and surveillance: recent real-world protocols and implementation
#### European FAP Consortium (2023) personalized endoscopic surveillance (real-world implementation)
The European FAP Consortium published consensus-based protocols for:
* Lower GI surveillance in patients with ileorectal/ileosigmoid anastomosis (IRA/ISA) and ileal pouch-anal anastomosis (IPAA). (aelvoet2023personalizedendoscopicsurveillance pages 3-5)
* Upper GI surveillance (duodenum and stomach) with intervention thresholds and variable surveillance intervals based on endoscopic findings. (aelvoet2023personalizedendoscopicsurveillance pages 5-6)

**Intervention thresholds (explicit):** endoscopic polypectomy/papillectomy indications include duodenal/ampullary adenomas ≥10 mm (or rapidly progressive ampullary lesion), gastric adenomas ≥5 mm, optical suspicion of HGD, and optional duodenal adenoma ≥5 mm when ≥20 duodenal adenomas are present. (aelvoet2023personalizedendoscopicsurveillance pages 3-5)

**Visual evidence (flowcharts):**
* Lower GI post-surgical surveillance flowcharts (IRA/ISA and IPAA): (aelvoet2023personalizedendoscopicsurveillance media 06b7c6ab)
* Upper GI duodenum/stomach surveillance flowchart: (aelvoet2023personalizedendoscopicsurveillance media 86c4e959)

#### Surveillance adherence (implementation gap)
A 2024 Saudi cohort study of surgically treated FAP patients reported incomplete adherence to recommended surveillance: 78% compliance for pre-operative colonoscopy and EGD, but 38% for initial and 27% for post-operative colonoscopy; thyroid ultrasound compliance was 14%. (alhassan2024surveillancecomplianceand pages 1-2)

**NCCN 2024 guideline limitation in this run:** Although the NCCN Version 3.2024 document was retrieved and includes extensive multigene testing guidance, this run did not retrieve the FAP-specific surveillance interval/timing tables from that document’s text chunks; therefore, NCCN-specific ages/intervals for FAP surveillance cannot be quoted verbatim from the evidence available here. (hodan2024geneticfamilialhighriskassessment pages 7-8, hodan2024geneticfamilialhighriskassessment pages 8-9, zare2025guidelinesforfamilial pages 4-4)

---

## 11. Outcome / prognosis

### 11.1 CRC risk
Untreated classic FAP is associated with near-certain CRC (often framed as ~100% lifetime CRC risk). (kyriakidis2023updatedperspectiveson pages 1-2, alhassan2024surveillancecomplianceand pages 1-2)

### 11.2 Desmoid morbidity
Desmoid tumors are a major morbidity driver. In a 2025 postoperative registry cohort (2000–2023; n=202 surgical patients), 21/202 (10.4%) developed intra-abdominal desmoids, and the authors concluded that a minimally invasive rectal-sparing colectomy “appears protective” for desmoid development. ()

---

## 12. Treatment

### 12.1 Surgical and interventional (standard of care)
Risk-reducing colorectal surgery (colectomy or proctocolectomy with reconstruction strategies such as IPAA vs IRA) is the mainstay to prevent CRC. Reviews emphasize prophylactic colectomy as the “gold-standard” risk reduction approach, typically completed by age ~40 in one 2023 review summary, while other sources describe prophylactic colectomy recommended in adolescence/young adulthood depending on phenotype. (kyriakidis2023updatedperspectiveson pages 1-2, alhassan2024surveillancecomplianceand pages 1-2)

### 12.2 Endoscopic management (emerging practice)
European FAP Consortium protocols formalize endoscopic removal thresholds and surveillance intervals aiming to prevent cancer while reducing surgical interventions, with prospective evaluation planned in a 5-year multi-center study. (aelvoet2023personalizedendoscopicsurveillance pages 3-5, aelvoet2023personalizedendoscopicsurveillance pages 5-6)

### 12.3 Pharmacotherapy / chemoprevention (current evidence state)
Multiple chemopreventive agents have been studied (eg, aspirin, celecoxib, sulindac, DFMO-based combinations, erlotinib combinations, metformin, fish oil, turmeric, vitamin C), but a 2023 review concluded no agent yet meets criteria for a durable, safe, clinically meaningful long-term chemoprevention strategy in FAP. (kyriakidis2023updatedperspectiveson pages 10-12)

**Pathway-targeting development:** The same 2023 review highlights interest in targeting novel pathways including **mTOR** (eg, small pilot experiences with rapamycin/sirolimus showing reductions in polyp size/grade but with adverse events) and notes ongoing trials/strategies such as TUPELO (REC-4881; MAPK inhibitor) and obeticholic acid. (kyriakidis2023updatedperspectiveson pages 10-12)

### 12.4 MAXO term suggestions (treatment actions)
* Prophylactic colectomy / proctocolectomy: MAXO:0001112 (surgical excision; term suggestion)
* Endoscopic polypectomy: MAXO:0000016 (endoscopic resection; term suggestion)
* Cancer surveillance (endoscopic): MAXO:0000127 (screening/surveillance; term suggestion)

(Ontology term suggestions; not explicitly enumerated in retrieved sources.)

---

## 13. Prevention

### 13.1 Secondary prevention (dominant strategy)
Early detection and removal of adenomas via endoscopic surveillance and prophylactic surgery is the dominant prevention strategy described across sources. (alhassan2024surveillancecomplianceand pages 1-2, aelvoet2023personalizedendoscopicsurveillance pages 3-5)

### 13.2 Tertiary prevention
Post-surgical surveillance of retained rectum/pouch and upper GI tract aims to prevent advanced neoplasia and manage adenoma burden. (aelvoet2023personalizedendoscopicsurveillance pages 3-5, aelvoet2023personalizedendoscopicsurveillance pages 5-6)

---

## 14. Other species / natural disease
No naturally occurring FAP-equivalent disease in non-human species was retrieved in this evidence set.

---

## 15. Model organisms
Although APC-driven tumorigenesis is commonly studied in genetically engineered mouse models, this run did not retrieve a primary source within the evidence set that explicitly details specific model organism resources (eg, APC^Min/+ phenotypic recapitulation) in a citable way for this report.

---

## Expert interpretation and evidence gaps (authoritative source synthesis)
A 2025 guideline-comparison review argues that most FAP management recommendations remain **expert-consensus–driven** due to the limited high-quality evidence base typical of rare diseases, and highlights ongoing disagreements (eg, adenoma thresholds and surveillance intensity across jurisdictions). (zare2025guidelinesforfamilial pages 1-2)

The European FAP Consortium’s 2023 surveillance strategy is an example of expert-driven standardization intended to be validated prospectively, reflecting a broader trend toward **personalized surveillance and endoscopic intervention** rather than relying solely on prophylactic colectomy. (aelvoet2023personalizedendoscopicsurveillance pages 3-5, aelvoet2023personalizedendoscopicsurveillance pages 5-6)

---

## Reference URLs and publication dates (from retrieved sources)
* Kyriakidis F. et al. “Updated Perspectives on the Diagnosis and Management of Familial Adenomatous Polyposis.” *The Application of Clinical Genetics* (Aug 2023). https://doi.org/10.2147/tacg.s372241 (kyriakidis2023updatedperspectiveson pages 1-2)
* Ditonno I. et al. “Molecular Pathways of Carcinogenesis in Familial Adenomatous Polyposis.” *Int J Mol Sci* (Mar 2023). https://doi.org/10.3390/ijms24065687 (ditonno2023molecularpathwaysof pages 1-2)
* Aelvoet A.S. et al. “Personalized endoscopic surveillance…” *Endoscopy International Open* (Jan 2023). https://doi.org/10.1055/a-2011-1933 (aelvoet2023personalizedendoscopicsurveillance pages 3-5)
* Alhassan N. et al. “Surveillance Compliance and Quality of Life…” *J Epidemiol Glob Health* (Jan 2024). https://doi.org/10.1007/s44197-023-00171-8 (alhassan2024surveillancecomplianceand pages 1-2)
* Hodan R. et al. “NCCN… Version 3.2024.” *JNCCN* (Dec 2024). https://doi.org/10.6004/jnccn.2024.0061 (hodan2024geneticfamilialhighriskassessment pages 6-7)
* Karstensen J.G. et al. “Re-evaluating the genotypes…” *Eur J Hum Genet* (Published online Mar 12, 2024). https://doi.org/10.1038/s41431-024-01585-z (karstensen2024reevaluatingthegenotypes pages 1-2)
* de Moraes F.C.A. et al. “Genomic mosaicism in colorectal cancer and polyposis syndromes…” *Int J Colorectal Dis* (Dec 2024). https://doi.org/10.1007/s00384-024-04776-8 (moraes2024genomicmosaicismin pages 9-11)
* Zare B., Monahan K.J. “Guidelines for FAP…” *Familial Cancer* (Apr 2025). https://doi.org/10.1007/s10689-025-00462-y (zare2025guidelinesforfamilial pages 1-2)


References

1. (joo2025geneticsgenomicsand pages 1-2): Jihoon E. Joo, Julen Viana-Errasti, Daniel D. Buchanan, and Laura Valle. Genetics, genomics and clinical features of adenomatous polyposis. Familial Cancer, Apr 2025. URL: https://doi.org/10.1007/s10689-025-00460-0, doi:10.1007/s10689-025-00460-0. This article has 11 citations and is from a peer-reviewed journal.

2. (kyriakidis2023updatedperspectiveson pages 1-2): Filippos Kyriakidis, Dionysios Kogias, Theodora Maria Venou, Eleni Karlafti, and Daniel Paramythiotis. Updated perspectives on the diagnosis and management of familial adenomatous polyposis. The Application of Clinical Genetics, 16:139-153, Aug 2023. URL: https://doi.org/10.2147/tacg.s372241, doi:10.2147/tacg.s372241. This article has 22 citations.

3. (ditonno2023molecularpathwaysof pages 1-2): Ilaria Ditonno, Domenico Novielli, Francesca Celiberto, Salvatore Rizzi, Maria Rendina, Enzo Ierardi, Alfredo Di Leo, and Giuseppe Losurdo. Molecular pathways of carcinogenesis in familial adenomatous polyposis. International Journal of Molecular Sciences, 24:5687, Mar 2023. URL: https://doi.org/10.3390/ijms24065687, doi:10.3390/ijms24065687. This article has 36 citations.

4. (kyriakidis2023updatedperspectiveson pages 10-12): Filippos Kyriakidis, Dionysios Kogias, Theodora Maria Venou, Eleni Karlafti, and Daniel Paramythiotis. Updated perspectives on the diagnosis and management of familial adenomatous polyposis. The Application of Clinical Genetics, 16:139-153, Aug 2023. URL: https://doi.org/10.2147/tacg.s372241, doi:10.2147/tacg.s372241. This article has 22 citations.

5. (aelvoet2023personalizedendoscopicsurveillance pages 3-5): Arthur S. Aelvoet, Maria Pellisé, Barbara A.J. Bastiaansen, Monique E. van Leerdam, Rodrigo Jover, Francesc Balaguer, Michal F. Kaminski, John G. Karstensen, Jean-Christophe Saurin, Roel Hompes, Patrick M.M. Bossuyt, Luigi Ricciardiello, Andrew Latchford, and Evelien Dekker. Personalized endoscopic surveillance and intervention protocols for patients with familial adenomatous polyposis: the european fap consortium strategy. Endoscopy International Open, 11:E386-E393, Jan 2023. URL: https://doi.org/10.1055/a-2011-1933, doi:10.1055/a-2011-1933. This article has 26 citations and is from a peer-reviewed journal.

6. (aelvoet2023personalizedendoscopicsurveillance pages 5-6): Arthur S. Aelvoet, Maria Pellisé, Barbara A.J. Bastiaansen, Monique E. van Leerdam, Rodrigo Jover, Francesc Balaguer, Michal F. Kaminski, John G. Karstensen, Jean-Christophe Saurin, Roel Hompes, Patrick M.M. Bossuyt, Luigi Ricciardiello, Andrew Latchford, and Evelien Dekker. Personalized endoscopic surveillance and intervention protocols for patients with familial adenomatous polyposis: the european fap consortium strategy. Endoscopy International Open, 11:E386-E393, Jan 2023. URL: https://doi.org/10.1055/a-2011-1933, doi:10.1055/a-2011-1933. This article has 26 citations and is from a peer-reviewed journal.

7. (ditonno2023molecularpathwaysof pages 2-4): Ilaria Ditonno, Domenico Novielli, Francesca Celiberto, Salvatore Rizzi, Maria Rendina, Enzo Ierardi, Alfredo Di Leo, and Giuseppe Losurdo. Molecular pathways of carcinogenesis in familial adenomatous polyposis. International Journal of Molecular Sciences, 24:5687, Mar 2023. URL: https://doi.org/10.3390/ijms24065687, doi:10.3390/ijms24065687. This article has 36 citations.

8. (zare2025guidelinesforfamilial pages 1-2): Benjamin Zare and Kevin J. Monahan. Guidelines for familial adenomatous polyposis (fap): challenges in defining clinical management for a rare disease. Familial Cancer, Apr 2025. URL: https://doi.org/10.1007/s10689-025-00462-y, doi:10.1007/s10689-025-00462-y. This article has 12 citations and is from a peer-reviewed journal.

9. (zare2025guidelinesforfamilial pages 4-4): Benjamin Zare and Kevin J. Monahan. Guidelines for familial adenomatous polyposis (fap): challenges in defining clinical management for a rare disease. Familial Cancer, Apr 2025. URL: https://doi.org/10.1007/s10689-025-00462-y, doi:10.1007/s10689-025-00462-y. This article has 12 citations and is from a peer-reviewed journal.

10. (kyriakidis2023updatedperspectiveson pages 2-4): Filippos Kyriakidis, Dionysios Kogias, Theodora Maria Venou, Eleni Karlafti, and Daniel Paramythiotis. Updated perspectives on the diagnosis and management of familial adenomatous polyposis. The Application of Clinical Genetics, 16:139-153, Aug 2023. URL: https://doi.org/10.2147/tacg.s372241, doi:10.2147/tacg.s372241. This article has 22 citations.

11. (alhassan2024surveillancecomplianceand pages 1-2): Noura Alhassan, Hadeel Helmi, Abdullah Alzamil, Afraj Alshammari, Atheer Altamimi, Sulaiman Alshammari, Thamer Bin Traiki, Saleh Albanyan, Khayal AlKhayal, Ahmad Zubaidi, and Omar Al-Obeed. Surveillance compliance and quality of life assessment among surgical patients with familial adenomatous polyposis syndrome. Journal of Epidemiology and Global Health, 14:86-93, Jan 2024. URL: https://doi.org/10.1007/s44197-023-00171-8, doi:10.1007/s44197-023-00171-8. This article has 6 citations and is from a peer-reviewed journal.

12. (moraes2024genomicmosaicismin pages 9-11): Francisco Cezar Aquino de Moraes, Nayara Rozalem Moretti, Vitor Kendi Tsuchiya Sano, Cristiane Wen Tsing Ngan, and Rommel Mario Rodríguez Burbano. Genomic mosaicism in colorectal cancer and polyposis syndromes: a systematic review and meta-analysis. International Journal of Colorectal Disease, Dec 2024. URL: https://doi.org/10.1007/s00384-024-04776-8, doi:10.1007/s00384-024-04776-8. This article has 1 citations and is from a peer-reviewed journal.

13. (karstensen2024reevaluatingthegenotypes pages 1-2): John Gásdal Karstensen, Thomas v. Overeem Hansen, Johan Burisch, Malene Djursby, Helle Højen, Majbritt Busk Madsen, Niels Jespersen, and Anne Marie Jelsig. Re-evaluating the genotypes of patients with adenomatous polyposis of unknown etiology: a nationwide study. European Journal of Human Genetics, 32:588-592, Mar 2024. URL: https://doi.org/10.1038/s41431-024-01585-z, doi:10.1038/s41431-024-01585-z. This article has 6 citations and is from a domain leading peer-reviewed journal.

14. (hodan2024geneticfamilialhighriskassessment pages 6-7): Rachel Hodan, Samir Gupta, Jennifer M. Weiss, Lisen Axell, Carol A. Burke, Lee-May Chen, Daniel C. Chung, Katherine M. Clayback, Seth Felder, Zachariah Foda, Francis M. Giardiello, William Grady, Susan Gustafson, Andrea Hagemann, Michael J. Hall, Heather Hampel, Gregory Idos, Nora Joseph, Nawal Kassem, Bryson Katona, Kaitlyn Kelly, AnnMarie Kieber-Emmons, Sonia Kupfer, Katie Lang, Xavier Llor, Arnold J. Markowitz, Mariana Moreno Prats, Mariana Niell-Swiller, Darryl Outlaw, Sara Pirzadeh-Miller, Niloy Jewel Samadder, David Shibata, Peter P. Stanich, Benjamin J. Swanson, Brittany M. Szymaniak, Jeanna Welborn, Georgia L. Wiesner, Matthew B. Yurgelun, Mary Dwyer, Susan Darlow, and Zeenat Diwan. Genetic/familial high-risk assessment: colorectal, endometrial, and gastric, version 3.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, 22 10:695-711, Dec 2024. URL: https://doi.org/10.6004/jnccn.2024.0061, doi:10.6004/jnccn.2024.0061. This article has 97 citations.

15. (aelvoet2023personalizedendoscopicsurveillance media 06b7c6ab): Arthur S. Aelvoet, Maria Pellisé, Barbara A.J. Bastiaansen, Monique E. van Leerdam, Rodrigo Jover, Francesc Balaguer, Michal F. Kaminski, John G. Karstensen, Jean-Christophe Saurin, Roel Hompes, Patrick M.M. Bossuyt, Luigi Ricciardiello, Andrew Latchford, and Evelien Dekker. Personalized endoscopic surveillance and intervention protocols for patients with familial adenomatous polyposis: the european fap consortium strategy. Endoscopy International Open, 11:E386-E393, Jan 2023. URL: https://doi.org/10.1055/a-2011-1933, doi:10.1055/a-2011-1933. This article has 26 citations and is from a peer-reviewed journal.

16. (aelvoet2023personalizedendoscopicsurveillance media 86c4e959): Arthur S. Aelvoet, Maria Pellisé, Barbara A.J. Bastiaansen, Monique E. van Leerdam, Rodrigo Jover, Francesc Balaguer, Michal F. Kaminski, John G. Karstensen, Jean-Christophe Saurin, Roel Hompes, Patrick M.M. Bossuyt, Luigi Ricciardiello, Andrew Latchford, and Evelien Dekker. Personalized endoscopic surveillance and intervention protocols for patients with familial adenomatous polyposis: the european fap consortium strategy. Endoscopy International Open, 11:E386-E393, Jan 2023. URL: https://doi.org/10.1055/a-2011-1933, doi:10.1055/a-2011-1933. This article has 26 citations and is from a peer-reviewed journal.

17. (hodan2024geneticfamilialhighriskassessment pages 7-8): Rachel Hodan, Samir Gupta, Jennifer M. Weiss, Lisen Axell, Carol A. Burke, Lee-May Chen, Daniel C. Chung, Katherine M. Clayback, Seth Felder, Zachariah Foda, Francis M. Giardiello, William Grady, Susan Gustafson, Andrea Hagemann, Michael J. Hall, Heather Hampel, Gregory Idos, Nora Joseph, Nawal Kassem, Bryson Katona, Kaitlyn Kelly, AnnMarie Kieber-Emmons, Sonia Kupfer, Katie Lang, Xavier Llor, Arnold J. Markowitz, Mariana Moreno Prats, Mariana Niell-Swiller, Darryl Outlaw, Sara Pirzadeh-Miller, Niloy Jewel Samadder, David Shibata, Peter P. Stanich, Benjamin J. Swanson, Brittany M. Szymaniak, Jeanna Welborn, Georgia L. Wiesner, Matthew B. Yurgelun, Mary Dwyer, Susan Darlow, and Zeenat Diwan. Genetic/familial high-risk assessment: colorectal, endometrial, and gastric, version 3.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, 22 10:695-711, Dec 2024. URL: https://doi.org/10.6004/jnccn.2024.0061, doi:10.6004/jnccn.2024.0061. This article has 97 citations.

18. (hodan2024geneticfamilialhighriskassessment pages 8-9): Rachel Hodan, Samir Gupta, Jennifer M. Weiss, Lisen Axell, Carol A. Burke, Lee-May Chen, Daniel C. Chung, Katherine M. Clayback, Seth Felder, Zachariah Foda, Francis M. Giardiello, William Grady, Susan Gustafson, Andrea Hagemann, Michael J. Hall, Heather Hampel, Gregory Idos, Nora Joseph, Nawal Kassem, Bryson Katona, Kaitlyn Kelly, AnnMarie Kieber-Emmons, Sonia Kupfer, Katie Lang, Xavier Llor, Arnold J. Markowitz, Mariana Moreno Prats, Mariana Niell-Swiller, Darryl Outlaw, Sara Pirzadeh-Miller, Niloy Jewel Samadder, David Shibata, Peter P. Stanich, Benjamin J. Swanson, Brittany M. Szymaniak, Jeanna Welborn, Georgia L. Wiesner, Matthew B. Yurgelun, Mary Dwyer, Susan Darlow, and Zeenat Diwan. Genetic/familial high-risk assessment: colorectal, endometrial, and gastric, version 3.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, 22 10:695-711, Dec 2024. URL: https://doi.org/10.6004/jnccn.2024.0061, doi:10.6004/jnccn.2024.0061. This article has 97 citations.
