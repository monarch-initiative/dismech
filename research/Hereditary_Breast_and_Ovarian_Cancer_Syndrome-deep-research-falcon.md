---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T16:42:07.405968'
end_time: '2026-04-05T16:56:24.014796'
duration_seconds: 856.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Breast and Ovarian Cancer Syndrome
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 89
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Breast and Ovarian Cancer Syndrome
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Hereditary Breast and Ovarian Cancer Syndrome** covering all of the
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
- **Disease Name:** Hereditary Breast and Ovarian Cancer Syndrome
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Hereditary Breast and Ovarian Cancer Syndrome** covering all of the
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


# Hereditary Breast and Ovarian Cancer (HBOC) Syndrome — Comprehensive Disease Characteristics Report (2023–2024 prioritized)

## Disease characteristics at a glance
Hereditary Breast and Ovarian Cancer syndrome (HBOC) is an autosomal-dominant inherited cancer predisposition syndrome most commonly caused by heterozygous germline pathogenic/likely pathogenic variants (P/LPVs) in **BRCA1** and **BRCA2**, conferring high lifetime risks of breast and ovarian cancer and an expanded spectrum including fallopian tube/primary peritoneal cancers and, particularly for BRCA2, male breast, prostate, and pancreatic cancers. (bouras2023overviewofthe pages 1-2, mastrodomenico2023personalizedsystemictherapies pages 1-2)

Two tables are provided to support knowledge-base population: (i) genes and quantitative risk estimates and (ii) interventions with effect sizes/uptake and MAXO mappings.

| Gene | Role/pathway (HRR/MMR/tumor suppressor) | Inheritance (if stated) | Key associated cancers | Quantitative risk estimates (with age and %) | Notes |
|---|---|---|---|---|---|
| **BRCA1** | Tumor suppressor; homologous recombination repair (HRR)/DNA damage response (barili2024geneticbasisof pages 1-2, mastrodomenico2023personalizedsystemictherapies pages 2-3) | Autosomal dominant / AD stated for HBOC (bouras2023overviewofthe pages 1-2, bonetti2023omicssciencesand pages 2-3) | Female breast, ovarian, fallopian tube, primary peritoneal; also pancreatic and prostate in broader spectrum (barili2024geneticbasisof pages 1-2, bouras2023overviewofthe pages 1-2) | Breast cancer by age 70: **60–66%** (barili2024geneticbasisof pages 1-2); ovarian cancer by age 70: **41–58%** (barili2024geneticbasisof pages 1-2); alternative review estimates: breast **55–72% by age 70**, ovarian **39–44% lifetime** (mastrodomenico2023personalizedsystemictherapies pages 1-2); Asian study by age 80: Malaysia breast **40% (Malay), 49% (Indian), 55% (Chinese)**; ovarian **31%**; Singapore breast **57–61%**; ovarian **42%** (ho2024agespecificbreastand pages 1-2) | Penetrance varies by ancestry/geography and birth cohort; higher risks reported for women born after 1960 in Asian cohort (ho2024agespecificbreastand pages 1-2). Founder variants reported, e.g., BRCA1 c.4096+1G>A in Tuscany; source 2023 DOI https://doi.org/10.3390/ijms242115507 and 2024 DOI https://doi.org/10.1016/j.lanwpc.2024.101017 (ho2024agespecificbreastand pages 1-2) |
| **BRCA2** | Tumor suppressor; homologous recombination repair (HRR)/DNA damage response (barili2024geneticbasisof pages 1-2, mastrodomenico2023personalizedsystemictherapies pages 2-3) | Autosomal dominant / AD stated for HBOC (bouras2023overviewofthe pages 1-2, bonetti2023omicssciencesand pages 2-3) | Female breast, ovarian, fallopian tube, primary peritoneal; male breast, prostate, pancreatic; melanoma noted in broader literature snippet (mastrodomenico2023personalizedsystemictherapies pages 1-2, barili2024geneticbasisof pages 1-2) | Breast cancer by age 70: **55–61%** (barili2024geneticbasisof pages 1-2); ovarian cancer by age 70: **15–16.5%** (barili2024geneticbasisof pages 1-2); alternative review estimates: breast **45–69% by age 70**, ovarian **11–17% lifetime** (mastrodomenico2023personalizedsystemictherapies pages 1-2); Asian study by age 80: Malaysia breast **29% (Malay), 36% (Indian), 42% (Chinese)**; ovarian **12%**; Singapore breast **43–47%**; ovarian **20%** (ho2024agespecificbreastand pages 1-2); male risks: male breast **6–8%**, prostate **~60% by age 85**, pancreatic **3–5% by age 70** (mastrodomenico2023personalizedsystemictherapies pages 1-2) | Reduced-penetrance BRCA1/2 pathogenic variants are now recognized as a distinct category in clinical germline testing (2024 DOI https://doi.org/10.1038/s41698-024-00741-4) (speiser2023primarypreventionand pages 2-3). Founder effects are well documented; general prevalence cited as ~1:400 and ~1:40 in Ashkenazi Jewish populations (barili2024geneticbasisof pages 1-2) |
| **PALB2** | HRR-associated high-penetrance gene (nagy2024comprehensiveclinicalgenetics pages 1-2) | Not explicitly stated in snippets | Breast; included on HBOC panels (mastrodomenico2023personalizedsystemictherapies pages 1-2, nagy2024comprehensiveclinicalgenetics pages 1-2) | Lifetime breast cancer risk **33–53%** (mastrodomenico2023personalizedsystemictherapies pages 1-2) | Accounted for **9%** of P/LP variants in a 4,630-patient French HBOC cohort; retesting BRCA1/2-negative cases with expanded panels yielded clinically relevant findings in **5%** (2023 DOI https://doi.org/10.3390/cancers15133420) (bouras2023overviewofthe pages 1-2) |
| **RAD51C** | HRR-associated moderate/high-risk HBOC gene (nagy2024comprehensiveclinicalgenetics pages 1-2, mcdevitt2024emqnbestpractice pages 2-3) | Not explicitly stated in snippets | Ovarian and breast cancer spectrum; included on HBOC panels (mastrodomenico2023personalizedsystemictherapies pages 1-2, bouras2023overviewofthe pages 1-2) | No explicit lifetime % risk reported in retrieved snippets | Represented **7%** of P/LP variants in the French 13-gene cohort (2023 DOI https://doi.org/10.3390/cancers15133420) (bouras2023overviewofthe pages 1-2) |
| **RAD51D** | HRR-associated moderate/high-risk HBOC gene (nagy2024comprehensiveclinicalgenetics pages 1-2, mcdevitt2024emqnbestpractice pages 2-3) | Not explicitly stated in snippets | Ovarian and breast cancer spectrum; included on HBOC panels (mastrodomenico2023personalizedsystemictherapies pages 1-2, bouras2023overviewofthe pages 1-2) | No explicit lifetime % risk reported in retrieved snippets | Represented **2%** of P/LP variants in the French 13-gene cohort (2023 DOI https://doi.org/10.3390/cancers15133420) (bouras2023overviewofthe pages 1-2) |
| **ATM** | DNA damage response/HRR-related moderate-penetrance gene (nagy2024comprehensiveclinicalgenetics pages 1-2, mastrodomenico2023personalizedsystemictherapies pages 2-3) | Not explicitly stated in snippets | Breast/ovarian cancer spectrum; pancreatic risk context discussed in broader literature (mastrodomenico2023personalizedsystemictherapies pages 1-2, nagy2024comprehensiveclinicalgenetics pages 1-2) | No explicit lifetime % risk reported in retrieved snippets | Most common non-BRCA mutation in Thai HBOC-spectrum cohort; non-BRCA genes accounted for **35%** of P/LP findings among mutation-positive individuals (2024 DOI https://doi.org/10.1038/s41525-024-00400-4) (liu2023prophylacticinterventionsfor pages 17-19) |
| **CHEK2** | Moderate-penetrance DNA damage response gene (nagy2024comprehensiveclinicalgenetics pages 1-2) | Not explicitly stated in snippets | Breast cancer; ovarian connection suggested in early-onset OC study context (speiser2023primarypreventionand pages 2-3, bonetti2023omicssciencesand pages 2-3) | Frequency mostly **<1%** in GC-HBOC report context (speiser2023primarypreventionand pages 2-3) | Included on expanded hereditary breast/ovarian panels; moderate penetrance and management recommendations more limited than BRCA1/2 (nagy2024comprehensiveclinicalgenetics pages 1-2) |
| **TP53** | Tumor suppressor; Li-Fraumeni-associated but can appear on HBOC panels (nagy2024comprehensiveclinicalgenetics pages 1-2, bouras2023overviewofthe pages 1-2) | Not explicitly stated for HBOC in snippets | Breast cancer, ovarian cancer spectrum in some HBOC-tested families (bouras2023overviewofthe pages 1-2, barili2024geneticbasisof pages 1-2) | In a German HBOC-tested breast cancer cohort, TP53 P/LP variants in **0.6%** overall, **1.1%** in breast cancer diagnosed **<36 years**, **1.1%** in bilateral vs **0.3%** unilateral breast cancer (barili2024geneticbasisof pages 1-2) | French cohort: TP53 made up **3%** of P/LP variants; Brazilian review found TP53 c.1010G>A frequency **1.83% (61/3336)** among patients meeting HBOC criteria (2024 DOI https://doi.org/10.1186/s40001-024-01767-x) (bouras2023overviewofthe pages 1-2, liu2023prophylacticinterventionsfor pages 17-19) |
| **MLH1 / MSH2 / MSH6 / PMS2 / EPCAM** | MMR pathway genes included on some HBOC multigene panels (bouras2023overviewofthe pages 1-2, nagy2024comprehensiveclinicalgenetics pages 1-2) | Not explicitly stated in snippets | Mostly Lynch-spectrum cancers; can emerge as secondary/actionable findings in HBOC testing (nagy2024comprehensiveclinicalgenetics pages 1-2, bouras2023overviewofthe pages 2-4) | No explicit lifetime % risk for HBOC-related cancers reported in retrieved snippets | French 13-gene HBOC panel included these genes; Nagy 2024 found some P/LP variants in Lynch-associated genes during HBOC testing and used tumor immunohistochemistry to clarify causative role (2024 DOI https://doi.org/10.3390/ijms252312546) (nagy2024comprehensiveclinicalgenetics pages 1-2) |


*Table: This table summarizes key genes implicated in hereditary breast and ovarian cancer syndrome and related testing panels, with only quantitative risks explicitly reported in the retrieved evidence. It is useful for comparing BRCA1/2 with other HBOC-spectrum genes, while highlighting where recent evidence supports pathogenicity, penetrance variability, and panel-based detection.*

| Intervention | Indication/population | Reported effect size(s) and outcomes | Implementation notes (guideline/program examples, real-world uptake) | Suggested MAXO term(s) |
|---|---|---|---|---|
| Risk-reducing salpingo-oophorectomy (RRSO) / bilateral salpingo-oophorectomy | BRCA1/2 pathogenic-variant carriers at elevated ovarian cancer risk | Reduced overall mortality by **60%** and ovarian cancer-specific mortality by **79%** in a 2023 systematic review/meta-analysis; another 2024 review reports EOC risk reduction of **96%** when performed within guideline ages; cohort/guideline summaries report **80%** ovarian cancer risk reduction and **50%** breast cancer risk reduction in premenopausal women, with improved cancer-specific and overall mortality (liu2023prophylacticinterventionsfor pages 1-2, assad2024uptakeofscreening pages 1-3, inzoli2024uptakeofrisk‐reducing pages 1-2) | Guidelines cited in evidence recommend earlier timing for BRCA1 (**35–40 y**) and later for BRCA2 (**40–45 y**); North American uptake ranges **36–89%**; one urban comprehensive cancer center cohort had **74%** uptake; one Italian referral-center cohort had **96.1%** acceptance among women offered surgery; Japan insurance coverage was associated with a **3-fold** increase in monthly RRSO volume and **3.9-fold** increase in diagnosed BRCA carriers (2023–2024 literature; URLs in cited sources) (assad2024uptakeofscreening pages 1-3, liu2023prophylacticinterventionsfor pages 16-17, inzoli2024uptakeofrisk‐reducing pages 1-2) | MAXO: prophylactic salpingo-oophorectomy; preventive surgery |
| Risk-reducing mastectomy (RRM/BRRM/CRRM) | BRCA1/2 carriers seeking primary breast cancer prevention or contralateral risk reduction | Breast cancer risk reduction reported as **>90%** in one 2023 review and **87%** in a 2023 meta-analysis; contralateral risk reduction for BRCA carriers ~**91–93%** with meta-analytic **RR 0.07 (95% CI 0.04–0.15)**; mortality benefit less conclusive than for RRSO (liu2023prophylacticinterventionsfor pages 1-2, bertozzi2023riskreducingbreastand pages 6-7, liu2023prophylacticinterventionsfor pages 16-17) | Real-world uptake reported as **28%** in one synthesis; North American ranges **21–96%**; one comprehensive cancer center cohort had **60%** uptake. Post-reconstruction complications were reported in **43%**, with **72%** requiring additional medical/aesthetic surgery in one narrative review (liu2023prophylacticinterventionsfor pages 1-2, bertozzi2023riskreducingbreastand pages 6-7, assad2024uptakeofscreening pages 1-3) | MAXO: prophylactic mastectomy; contralateral prophylactic mastectomy |
| Intensified breast screening with annual MRI plus mammography/tomosynthesis | BRCA1/2 carriers who retain breasts; secondary prevention/early detection | Evidence snippets emphasize early-stage detection rather than proven mortality reduction; annual contrast-enhanced breast MRI is identified as the key component of surveillance, often alternating with mammography/tomosynthesis. Genetic testing was associated with increased subsequent uptake of breast MRI in real-world practice (liu2023prophylacticinterventionsfor pages 1-2, assad2024uptakeofscreening pages 1-3, speiser2023primarypreventionand pages 2-3) | NCCN-based management cited in 2024 cohort: alternating mammography/tomosynthesis with contrast-enhanced breast MRI; German GC-HBOC program describes annual MRI, supplemented by up to biannual ultrasound and mammography usually starting at age **40**. One center reported overall adherence to NCCN risk-management recommendations of **83%** (assad2024uptakeofscreening pages 1-3, speiser2023primarypreventionand pages 2-3) | MAXO: magnetic resonance imaging screening; mammographic screening |
| Transvaginal ultrasound (TVUS) + CA-125 surveillance | BRCA1/2 carriers delaying or declining RRSO | Evidence snippets state routine CA-125/TVUS surveillance **does not reduce ovarian cancer risk or mortality** and is unreliable for early diagnosis; used as interim surveillance rather than definitive prevention (inzoli2024uptakeofrisk‐reducing pages 1-2) | NCCN-based summary cited TVUS + CA-125 every **6–12 months** starting age **30–35** for women delaying RRSO; an Italian regional program offered TVUS and CA-125 **twice yearly** (assad2024uptakeofscreening pages 1-3, inzoli2024uptakeofrisk‐reducing pages 1-2) | MAXO: transvaginal ultrasonography; CA-125 measurement; surveillance |
| Chemoprevention with tamoxifen/raloxifene | High-risk women/BRCA carriers considering non-surgical breast cancer risk reduction | Tamoxifen reduced breast cancer incidence by ~**48%** in high-risk individuals; raloxifene by ~**25%**. In the 2023 meta-analysis, pooled chemoprevention showed a **39%** cancer-risk reduction but **did not reach statistical significance** overall (limited studies) (liu2023prophylacticinterventionsfor pages 1-2, liu2023prophylacticinterventionsfor pages 16-17) | Real-world uptake low: **6.3%** in one synthesis; U.S. preference for tamoxifen/raloxifene **12.4%**; lower uptake reported in some European settings. Evidence base and uptake are weaker than for surgery (liu2023prophylacticinterventionsfor pages 1-2, liu2023prophylacticinterventionsfor pages 17-19) | MAXO: tamoxifen chemoprevention; raloxifene chemoprevention |
| Lifestyle/weight-change intervention | BRCA carriers/high-risk women; adjunct prevention | Weight loss of **≥10 lb** between ages **18–30** was associated with **34% lower** breast cancer risk in one summarized study (liu2023prophylacticinterventionsfor pages 16-17) | Mentioned as supportive/adjunct prevention in meta-analysis synthesis rather than a guideline-standard standalone intervention (liu2023prophylacticinterventionsfor pages 16-17) | MAXO: weight reduction intervention; lifestyle intervention |
| Multigene germline testing (panel testing) for risk assessment and management selection | Individuals meeting HBOC criteria; also retesting of BRCA1/2-negative high-risk cases | In a French cohort of **4,630** suspected HBOC cases, **528** P/LP variants were found (~**11.4%** overall); retesting BRCA1/2-negative individuals with an expanded panel yielded clinically relevant findings in **5%**; in a Hungarian cohort, extended testing produced a **20.7%** P/LP detection rate and "doubled" yield versus BRCA1/2-only testing (**20.7% vs 12.1%**) (bouras2023overviewofthe pages 1-2, nagy2024comprehensiveclinicalgenetics pages 2-4) | EMQN 2024 best-practice guidance supports multigene workflows and requires BRCA1/2 CNV analysis at minimum; diagnostic yield informs screening, preventive surgery, cascade testing, and therapy selection. Thai cohort of **4,567** HBOC-spectrum patients found germline P/LP variants in **13.4%**, with non-BRCA genes accounting for **35%** of positive findings (mcdevitt2024emqnbestpractice pages 3-4, liu2023prophylacticinterventionsfor pages 17-19) | MAXO: genetic testing; multigene panel testing; cascade testing |
| PARP inhibitor therapy (e.g., olaparib; targeted therapy) | BRCA-associated breast/ovarian and other BRCA-deficient cancers; adjuvant/maintenance/metastatic settings depending tumor type | Mechanistically exploits HRD synthetic lethality; ovarian cancer meta-analysis of **20 RCTs / 7,832** participants found maintenance PARP inhibitors improved **PFS HR 0.398**, **OS HR 0.677**, **CFI HR 0.417**, **TFST HR 0.441**, **TSST HR 0.574**, but increased any-grade TEAEs **RR 1.046** and grade ≥3 TEAEs **RR 2.931** (elze2024genomicinstabilityin pages 1-2, mastrodomenico2023personalizedsystemictherapies pages 2-3, katabathina2017imagingandscreening pages 1-2, rahner2008hereditarycancersyndromes. pages 1-2, beamer2019hereditarybreastand pages 1-3) | EMQN 2024 notes ovarian tumor BRCA1/2 testing detects a pathogenic variant in ~**15%** of patients, including ~**7%** somatic-only, supporting PARP eligibility; 2024 expert reviews note FDA-approved PARP indications across BRCA-associated breast, pancreatic, prostate, and ovarian cancers (mcdevitt2024emqnbestpractice pages 3-4, cheng2024brca1brca2and pages 1-3) | MAXO: poly(ADP-ribose) polymerase inhibitor therapy; olaparib therapy |
| Platinum-based chemotherapy sensitivity-guided management | BRCA1/2-deficient or HRD-associated tumors (especially HGSC and BRCA-associated breast/ovarian cancers) | Evidence snippets state BRCA1/2-deficient/HRD tumors are more sensitive to platinum agents; non-breast/ovarian BRCA-deficient tumors showed higher genomic instability scores and are proposed as candidates for platinum/PARP strategies. One organoid model with TP53/RAD51D co-deletion showed heightened sensitivity to platinum and PARPi (elze2024genomicinstabilityin pages 1-2, mastrodomenico2023personalizedsystemictherapies pages 2-3, flaum2023assessmentofpredisposition pages 31-35) | Used as a precision oncology consequence of BRCA/HRD testing rather than a primary prevention measure; implementation depends on tumor type and confirmation of HRD/second-hit loss (elze2024genomicinstabilityin pages 1-2) | MAXO: platinum-based chemotherapy |
| Hereditary cancer registry / coordinated risk-management program | BRCA carriers requiring lifelong surveillance and surgery coordination | Qualitative rather than interventional efficacy evidence: carriers reported that centralized registries/programs could improve coordination of “burdensome, life-long risk management” (bonetti2023omicssciencesand pages 2-3) | German Consortium model cited **23** university centers and **>100** cooperating certified centers delivering standardized HBOC care; registry-focused qualitative work in Canada highlighted continuity and coordination challenges in usual care (speiser2023primarypreventionand pages 2-3, bonetti2023omicssciencesand pages 2-3) | MAXO: care coordination; hereditary cancer registry enrollment |


*Table: This table summarizes prevention, screening, diagnostic, and treatment interventions for hereditary breast and ovarian cancer syndrome using only effects and implementation details explicitly reported in the retrieved evidence. It is useful for linking management options to outcomes, real-world uptake, and best-effort MAXO action terms.*

---

## 1. Disease Information

### 1.1 Concise overview (what is the disease?)
HBOC is a genetic condition characterized by **increased risk for breast and ovarian cancers**, often with **earlier onset** than sporadic cancers, and associated risks for other malignancies depending on the causal gene. HBOC is described as an **autosomal dominant** inherited disorder/cancer predisposition. (bouras2023overviewofthe pages 1-2, mastrodomenico2023personalizedsystemictherapies pages 1-2)

A large French cohort review states that HBOC accounts for **~10–15% of breast cancers** and **~25% of ovarian cancers**. (bouras2023overviewofthe pages 1-2)

### 1.2 Key identifiers
* **OMIM (genes)**: **BRCA1 OMIM #113705**, **BRCA2 OMIM #612555** are explicitly cited in a 2023 HBOC cohort report. (bouras2023overviewofthe pages 1-2)
* **OMIM (syndrome entries)**: A review table lists familial HBOC syndrome entries **MIM 604370** and **MIM 612555**. (bonetti2023omicssciencesand pages 2-3)

**Not retrieved in the available evidence set**: MONDO ID for HBOC, Orphanet disease ID, ICD-10/ICD-11 code, and MeSH identifier for the *syndrome itself*. These identifiers likely exist in aggregated resources (e.g., MONDO/Orphanet/MeSH), but were not directly extractable from the retrieved full-text snippets used here.

### 1.3 Synonyms and alternative names
Commonly used names in the retrieved literature include:
* **Hereditary Breast and Ovarian Cancer (HBOC) syndrome** (mcdevitt2024emqnbestpractice pages 1-2, bouras2023overviewofthe pages 1-2)
* **BRCA-associated hereditary breast/ovarian cancer** (tan2024brcaandbeyond pages 2-4)
* **Hereditary breast–ovarian cancer syndrome** (kostov2022hereditarygynecologiccancer pages 5-6)

### 1.4 Evidence provenance (patient-level vs aggregated)
The knowledge summarized here is derived from a mixture of:
* **Aggregated disease-level resources** (reviews, best-practice guidelines, meta-analyses) (mcdevitt2024emqnbestpractice pages 1-2, sun2024efficacyandsafety pages 1-2)
* **Large clinical cohorts and retrospective/prospective series** (e.g., French 4,630-case panel cohort; Hungarian 513-case program; Romanian 616-case cohort; 2024 implementation cohorts) (bouras2023overviewofthe pages 1-2, nagy2024comprehensiveclinicalgenetics pages 1-2, grigore2024themoleculardetection pages 1-2, assad2024uptakeofscreening pages 1-3)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary causal mechanism (genetic):** HBOC is most frequently caused by heterozygous germline P/LP variants in **BRCA1/BRCA2**, tumor-suppressor genes essential for **homologous recombination (HR) DNA double-strand break repair**. (barili2024geneticbasisof pages 1-2, mastrodomenico2023personalizedsystemictherapies pages 2-3)

**Other genes (expanded HBOC spectrum):** Multigene testing increasingly identifies clinically actionable variants in other genes (e.g., **PALB2, RAD51C, RAD51D, TP53**, and additional moderate-penetrance genes). (bouras2023overviewofthe pages 1-2, nagy2024comprehensiveclinicalgenetics pages 1-2, mcdevitt2024emqnbestpractice pages 2-3)

### 2.2 Risk factors

#### Genetic risk factors
* **BRCA1/2 pathogenic variants:** confer high lifetime breast/ovarian cancer risks, with quantitative estimates varying by cohort and ancestry (see Section 9). (barili2024geneticbasisof pages 1-2, ho2024agespecificbreastand pages 1-2)
* **Variant-level heterogeneity / penetrance variability:** 2024 work proposes a class of **reduced penetrance pathogenic variants** in BRCA1/2 that confer moderately increased risk, affecting counseling and prevention. (speiser2023primarypreventionand pages 2-3)

#### Environmental and demographic risk modifiers
Evidence in the retrieved set is limited for specific environmental exposures; however, a meta-analysis synthesis reported a behavioral association: **≥10 lb weight loss between ages 18–30** was associated with **34% lower breast cancer risk** in one included study. (liu2023prophylacticinterventionsfor pages 16-17)

### 2.3 Protective factors
* **Risk-reducing surgeries** are the most strongly supported protective interventions (see Prevention). (liu2023prophylacticinterventionsfor pages 1-2, inzoli2024uptakeofrisk‐reducing pages 1-2)
* **Chemoprevention** evidence is less consistent in pooled analyses; a 2023 synthesis found a pooled chemoprevention effect that **did not reach statistical significance**. (liu2023prophylacticinterventionsfor pages 16-17)

### 2.4 Gene–environment interactions
Specific gene–environment interaction evidence (e.g., formal GxE interaction terms) was not directly retrieved from the evidence set.

---

## 3. Phenotypes (clinical presentation)

### 3.1 Core tumor phenotypes and subtype features

#### Breast cancer
* **Breast cancer** is the predominant phenotype; breast cancer risk increases from the **mid-20s** in BRCA carriers in one clinical testing summary. (list2021oncogenedxbrca1and pages 1-3)
* **Triple-negative breast cancer (TNBC)**: BRCA1-associated breast cancers are frequently triple-negative; one radiology review reports ~**70%** of BRCA1 carriers’ breast cancers are triple-negative vs **~10–20%** in the general population. (katabathina2017imagingandscreening pages 1-2)

#### Ovarian cancer / extrauterine pelvic serous cancers
* **High-grade serous carcinoma (HGSC)** is the most common ovarian manifestation in HBOC and is described as often originating from the **fimbrial end of the fallopian tube**. (katabathina2017imagingandscreening pages 1-2)
* A 2024 review notes HGSC accounts for **~65–75%** of ovarian cancers in the general population but **~90%** of epithelial ovarian cancers in BRCA1/2 carriers. (gootzen2024riskreducingsalpingectomywith pages 1-2)

#### Fallopian tube precursor lesions
* **Serous tubal intraepithelial carcinoma (STIC)** is described as the proposed **HGSC precursor**, typically located in the distal/fimbriated tube. (gootzen2024riskreducingsalpingectomywith pages 1-2)
* A 2023 prospective RRSO cohort using SEE-FIM identified STIC, STILs, and frequent p53 signatures in mutation carriers (p53 signature in **~32.4%**). (feng2023riskreducingsalpingooophorectomyamong pages 1-3)

#### Male phenotypes and additional cancers
* Male implications are under-recognized; a 2024 JAMA Oncology review states approximately **half of BRCA1/2 PV carriers are male**, but men undergo cancer genetic testing far less frequently (RR **0.10**, 95% CI 0.05–0.23 vs women). (cheng2024brca1brca2and pages 1-3)
* BRCA2-associated risks include male breast, prostate, and pancreatic cancers (quantitative estimates vary by source; see Section 9). (mastrodomenico2023personalizedsystemictherapies pages 1-2, list2021oncogenedxbrca1and pages 1-3)

### 3.2 Suggested HPO terms (examples)
The retrieved evidence supports mapping at least the following phenotypes to HPO:
* Breast carcinoma (from evidence of breast cancer risk) (barili2024geneticbasisof pages 1-2, list2021oncogenedxbrca1and pages 1-3)
* Ovarian carcinoma / epithelial ovarian cancer (gootzen2024riskreducingsalpingectomywith pages 1-2)
* High-grade serous carcinoma (ovary) (katabathina2017imagingandscreening pages 1-2, gootzen2024riskreducingsalpingectomywith pages 1-2)
* Triple-negative breast cancer (katabathina2017imagingandscreening pages 1-2)
* Fallopian tube carcinoma; primary peritoneal carcinoma (mastrodomenico2023personalizedsystemictherapies pages 1-2, katabathina2017imagingandscreening pages 1-2)
* Male breast cancer; prostate cancer; pancreatic cancer (mastrodomenico2023personalizedsystemictherapies pages 1-2, cheng2024brca1brca2and pages 1-3)
* Contralateral breast cancer (list2021oncogenedxbrca1and pages 1-3)
* STIC (as precursor lesion; while not strictly an HPO phenotype, it can be captured as a pathologic finding) (gootzen2024riskreducingsalpingectomywith pages 1-2)

**Frequency among affected individuals**: numeric phenotype frequencies are sparse in the retrieved set beyond TNBC (~70% of BRCA1-associated breast cancers) and HGSC predominance (~90% of EOC in BRCA carriers). (katabathina2017imagingandscreening pages 1-2, gootzen2024riskreducingsalpingectomywith pages 1-2)

**Quality-of-life impact**: evidence is indirect; risk management is characterized as burdensome and lifelong by qualitative work, supporting QoL/psychosocial impact. (bonetti2023omicssciencesand pages 2-3)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
Core causal genes and testing panel genes include:
* **BRCA1/BRCA2** (high penetrance) (barili2024geneticbasisof pages 1-2)
* Other high/moderate penetrance genes reported in clinical panels: **PALB2, TP53, RAD51C, RAD51D, BRIP1, ATM, CHEK2**, and others depending on panel composition. (mcdevitt2024emqnbestpractice pages 2-3, nagy2024comprehensiveclinicalgenetics pages 1-2, bouras2023overviewofthe pages 1-2)

### 4.2 Pathogenic variant classes and interpretation
* A 2024 review reports ClinVar counts (Dec 2023): ~**4,300** BRCA1 and ~**5,200** BRCA2 pathogenic/likely pathogenic variants; ~**80%** truncating, ~**10%** missense, ~**10%** CNVs. (barili2024geneticbasisof pages 2-4)
* Variant interpretation challenges include VUS: a best-practice review notes ClinVar contains ~**37% BRCA1** and ~**45% BRCA2** unique variants classified as VUS, motivating functional assays to improve classification. (sirera2020novelapproachesfor pages 25-30)
* 2024 clinical cohort work explicitly used ACMG criteria for variant interpretation in hereditary cancer panel testing. (nagy2024comprehensiveclinicalgenetics pages 2-4)

### 4.3 Somatic vs germline
EMQN best-practice guidance emphasizes both **tumor (somatic) and germline** BRCA testing to inform PARP inhibitor eligibility; ovarian tumor testing detects BRCA1/2 pathogenic variants in ~**15%** of patients, ~**7%** somatic-only. (mcdevitt2024emqnbestpractice pages 3-4)

### 4.4 Modifier genes / polygenic risk
EMQN notes polygenic risk scores (e.g., PRS313 in BOADICEA/CanRisk) exist but require further validation before routine use. (mcdevitt2024emqnbestpractice pages 1-2)

### 4.5 Epigenetic information
Noncoding mechanisms can contribute: a BRCA1 deep promoter variant (c.-107A>T) is described as causing promoter methylation (“secondary epimutation”) and reduced expression. (barili2024geneticbasisof pages 2-4)

### 4.6 Chromosomal abnormalities
Large rearrangements (CNVs) are an important component; EMQN requires CNV analysis at minimum and notes FFPE CNV calling challenges. (mcdevitt2024emqnbestpractice pages 3-4)

---

## 5. Environmental Information
The retrieved evidence base is limited on specific environmental toxins/infections for HBOC. Lifestyle/weight change evidence is noted under Etiology (Section 2). (liu2023prophylacticinterventionsfor pages 16-17)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (conceptual)
1. **Germline heterozygous loss-of-function** in **BRCA1/BRCA2** (tumor suppressors). (barili2024geneticbasisof pages 1-2)
2. In tumors, **biallelic inactivation** via loss of the remaining wild-type allele (“second hit”) produces **BRCA deficiency** and **homologous recombination deficiency (HRD)**. (elze2024genomicinstabilityin pages 1-2)
3. HRD shifts repair toward error-prone pathways, producing **genomic instability scars** measurable by LOH/LST/TAI signatures. (elze2024genomicinstabilityin pages 1-2, barili2024geneticbasisof pages 19-22)
4. Resulting genomic instability contributes to carcinogenesis, notably breast cancer and HGSC; and creates vulnerabilities to **platinum chemotherapy** and **PARP inhibitors** (synthetic lethality). (mastrodomenico2023personalizedsystemictherapies pages 2-3, elze2024genomicinstabilityin pages 1-2)

### 6.2 Molecular pathways and terms
**HR/HRD and genomic scars:** JNCI 2024 defines HRD features such as large-scale state transitions, genomic loss-of-heterozygosity and telomeric allelic imbalance. (elze2024genomicinstabilityin pages 1-2)

**PARP synthetic lethality:** PARP inhibitors inhibit catalytic PARylation and trap PARP on DNA, converting persistent SSBs into DSBs at replication forks; HR-deficient cells cannot repair these DSBs effectively, causing cell death. (mastrodomenico2023personalizedsystemictherapies pages 2-3)

**Ontology suggestions (best-effort):**
* GO Biological Process: homologous recombination; DNA double-strand break repair (supported by BRCA1/2 HR role) (barili2024geneticbasisof pages 1-2)
* Cell Ontology (CL): mammary epithelial cell (murine mammary organoid model); fallopian tube epithelial cell (FTE) (najafabadi2023atranscriptionalresponse pages 1-2, dai2024humanfallopiantubederived pages 1-2)

### 6.3 Tissue-of-origin in ovarian cancer
The fallopian tube origin hypothesis is supported by STIC precursor lesions in the distal tube; a 2024 review states STICs are characterized by aberrant p53 and Ki-67 immunohistochemistry and that no precursor lesions have been identified in ovaries. (gootzen2024riskreducingsalpingectomywith pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ level (primary)
* Breast (UBERON: breast)
* Ovary (UBERON: ovary)
* Fallopian tube (fimbrial end) (UBERON: fallopian tube) (katabathina2017imagingandscreening pages 1-2, gootzen2024riskreducingsalpingectomywith pages 1-2)
* Peritoneum (primary peritoneal carcinoma in spectrum) (mastrodomenico2023personalizedsystemictherapies pages 1-2)

### 7.2 Tissue/cell level
* Mammary epithelial compartment (mouse mammary organoid evidence) (najafabadi2023atranscriptionalresponse pages 1-2)
* Fallopian tube epithelium (FTE organoid and STIC precursor evidence) (dai2024humanfallopiantubederived pages 1-2, gootzen2024riskreducingsalpingectomywith pages 1-2)

### 7.3 Subcellular level
Mechanistically centered on nuclear DNA repair processes (homologous recombination, DNA damage response; PARP at DNA damage sites). (mastrodomenico2023personalizedsystemictherapies pages 2-3)

---

## 8. Temporal Development

### 8.1 Onset
* Breast cancer risk in BRCA carriers is described as increasing from the **mid-20s**; ovarian risk begins in the **mid-30s** and rises markedly in later decades. (list2021oncogenedxbrca1and pages 1-3)

### 8.2 Progression
HGSC and extrauterine pelvic serous carcinomas are typically aggressive; ovarian cancer is often diagnosed late in the general population (advanced stage common), motivating preventive surgery. (inzoli2024uptakeofrisk‐reducing pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Inheritance pattern
Autosomal dominant inheritance is repeatedly stated for HBOC. (bouras2023overviewofthe pages 1-2, mastrodomenico2023personalizedsystemictherapies pages 1-2)

### 9.2 Carrier prevalence / population frequency
* BRCA1/2 P/LPV prevalence is estimated at **~1:400–1:500** in non-Ashkenazi populations in one review, and **~1:400** in another; Ashkenazi Jewish prevalence is much higher (reported **~1:40**) due to founder mutations. (mastrodomenico2023personalizedsystemictherapies pages 1-2, barili2024geneticbasisof pages 1-2)
* A 2024 male-focused review reports population prevalence around **1 in 250** (with ancestry variation). (cheng2024brca1brca2and pages 1-3)
* A 2024 Portuguese/Brazilian admixture study cites global carrier prevalence estimates of **BRCA1 0.079%** and **BRCA2 0.124%** and provides open databases of variants. (andaluz2024usingportuguesebrca pages 1-3)

### 9.3 Penetrance / risk estimates (selected)
Risk estimates vary across studies and populations; examples:
* By age 70, breast cancer risk: **~60–66% BRCA1**, **~55–61% BRCA2**; ovarian cancer risk: **~41–58% BRCA1**, **~15–16.5% BRCA2** (2024 review). (barili2024geneticbasisof pages 1-2)
* Asian family study (Malaysia/Singapore) provides ethnicity- and region-specific cumulative risks by age 80 (e.g., Singapore BRCA1 breast ~57–61%, ovarian ~42%; BRCA2 breast ~43–47%, ovarian ~20%). (ho2024agespecificbreastand pages 1-2)

### 9.4 Founder effects and population-specific variants
* Brazil: BRCA1 c.5266dupC accounts for **26.8%** of pathogenic BRCA1 mutations in clinically selected HBOC patients; across screened Brazilian patients, frequency **~2% (120/6008)**. BRCA2 c.156_157insAlu accounts for **9.6%** of reported BRCA2 pathogenic mutations in Brazilian literature. (ribeiro2024systematicreviewof pages 1-2)
* Portugal: among Portuguese PV carriers, **59.5%** carried three founder PVs (BRCA1 c.2037delinsCC; BRCA1 c.3331_3334del; BRCA2 c.156_157insAlu). (andaluz2024usingportuguesebrca pages 1-3)
* Tuscany (Italy): BRCA1 c.4096+1G>A founder variant estimated MRCA ~**155 generations** (~**3000 years**) ago. (aretini2023thebrca1c.4096+1g>a pages 1-2)

---

## 10. Diagnostics

### 10.1 Genetic testing (current approach)
**Panel testing is now routine** in many settings due to cost decreases and expanded clinical actionability. EMQN 2024 provides best-practice laboratory guidance for HBOC genetic testing and emphasizes somatic + germline workflows, minimum-gene expectations (BRCA1/2 and PALB2 at minimum), and mandatory CNV analysis capability. (mcdevitt2024emqnbestpractice pages 2-3, mcdevitt2024emqnbestpractice pages 3-4)

**Detection rates and yield examples:**
* French 13-gene panel cohort (n=4,630): 528 P/LP variants detected; BRCA1 and BRCA2 together comprised ~75% of P/LP findings; retesting BRCA-negative cases with expanded panels yielded clinically relevant findings in **5%**. (bouras2023overviewofthe pages 1-2)
* Hungarian hereditary cancer panel: extended panel doubled detection vs BRCA1/2-only (**20.7% vs 12.1%**). (nagy2024comprehensiveclinicalgenetics pages 2-4)

**Technical confirmation methods:** One large cohort confirmed P/LP calls via Sanger for SNVs/indels, MLPA for CNVs, and PCR/RT-PCR for complex/splice variants. (bouras2023overviewofthe pages 2-4)

### 10.2 Tumor testing for therapy selection
EMQN notes ovarian tumor testing identifies BRCA1/2 pathogenic variants in ~**15%** of patients (including ~7% somatic-only), informing PARP inhibitor eligibility. (mcdevitt2024emqnbestpractice pages 3-4)

### 10.3 Imaging/screening diagnostics
A radiology review notes BRCA-associated breast cancers may appear well circumscribed and can mimic benign lesions, supporting careful biopsy of detected lesions. (katabathina2017imagingandscreening pages 1-2)

---

## 11. Outcome / Prognosis
Direct survival/prognosis statistics for HBOC carriers as a group were not comprehensively retrieved; however:
* BRCA-associated ovarian tumors (HGSC) are described as sensitive to platinum and PARP inhibitors, influencing outcomes. (katabathina2017imagingandscreening pages 1-2, elze2024genomicinstabilityin pages 1-2)

---

## 12. Treatment

### 12.1 Targeted therapy: PARP inhibitors
PARP inhibitors exploit HRD synthetic lethality in BRCA-deficient tumors. (mastrodomenico2023personalizedsystemictherapies pages 2-3)

**Breast cancer (adjuvant; 2024 review reporting OlympiA outcomes):** 1 year of adjuvant olaparib improved 4-year iDFS **82.7% vs 75.4% (HR 0.63)** and 4-year OS **89.8% vs 86.4% (HR 0.68; p=0.009)** at median 3.5-year follow-up. (tan2024brcaandbeyond pages 2-4)

**Breast cancer (metastatic):**
* OlympiAD: olaparib vs chemotherapy median PFS **7.0 vs 4.2 months (HR 0.58)**; ORR **59.9% vs 28.8%**; OS not statistically significant (median OS **19.3 vs 17.1 months; HR 0.90**). (tan2024brcaandbeyond pages 2-4)
* EMBRACA: talazoparib PFS **8.6 vs 5.6 months (HR 0.54)**; ORR **62.6% vs 27.2%**; no significant OS benefit. (tan2024brcaandbeyond pages 2-4)

**Ovarian cancer maintenance (2024 meta-analysis):** pooled improvements vs placebo: PFS **HR 0.398**, OS **HR 0.677**, with increased toxicities (any-grade TEAEs **RR 1.046**; grade ≥3 **RR 2.931**). (sun2024efficacyandsafety pages 1-2)

### 12.2 Platinum chemotherapy
HRD/BRCA1/2 deficiency predicts increased sensitivity to platinum agents across tumor types. (elze2024genomicinstabilityin pages 1-2)

### 12.3 Ongoing and example clinical trials (NCT)
Interventional studies retrieved include:
* **NCT03344965** (Olaparib in metastatic breast cancer) (arun2024brcamutatedbreastcancer pages 6-7)
* **NCT03150576** (PARTNER; neoadjuvant olaparib + chemotherapy in TNBC; gBRCA wild-type population) (abraham2024thepartnertrial pages 1-4)
* Risk-management/education/decision-support trials include **NCT04683068**, **NCT06914726**, **NCT00673335** (beamer2019hereditarybreastand pages 1-3)

---

## 13. Prevention

Key prevention approaches are summarized in artifact-01 and include:
* **RRSO**: mortality and ovarian cancer risk reduction with variable uptake (liu2023prophylacticinterventionsfor pages 1-2, assad2024uptakeofscreening pages 1-3, inzoli2024uptakeofrisk‐reducing pages 1-2)
* **Risk-reducing mastectomy**: large breast cancer risk reduction; uptake variable (bertozzi2023riskreducingbreastand pages 6-7, assad2024uptakeofscreening pages 1-3)
* **Intensified surveillance**: annual MRI with supplemental imaging per programmatic models (speiser2023primarypreventionand pages 2-3, assad2024uptakeofscreening pages 1-3)

---

## 14. Other Species / Natural Disease
No naturally occurring non-human HBOC syndrome evidence was retrieved; however, the genes and pathways are evolutionarily conserved and modeled in mice and organoids (see Model Organisms).

---

## 15. Model Organisms and Experimental Models

### 15.1 Mouse and organoid models
* **Brca2mut/WT mouse mammary organoids**: replication stress triggers a transcriptional response and selective expansion of HR-negative luminal cells; CRISPR deletion of Tspan8/Thrsp prevents expansion. (Najafabadi 2023, Nature Communications; DOI https://doi.org/10.1038/s41467-023-40956-w; publication Aug 2023) (najafabadi2023atranscriptionalresponse pages 1-2)
* **HGSOC GEMM (fallopian tube epithelium)**: Myc + Trp53-R270H under Ovgp1 promoter; lethal cancer at mean ~**14.5 months** latency; relevant to HGSOC biology including cases without HR mutations. (Blackman 2024, Cancer Research Communications; DOI https://doi.org/10.1158/2767-9764.CRC-24-0144; publication Sep 2024) (blackman2024mycissufficient pages 1-3)

### 15.2 Human and patient-derived organoids
* **Human FTE organoids (TP53 + RAD51D)**: co-deletion models early-stage HGSOC phenotypes and shows heightened sensitivity to platinum and PARPi. (Dai 2024, IJMS; DOI https://doi.org/10.3390/ijms25020886; publication Jan 2024) (dai2024humanfallopiantubederived pages 1-2)
* **Ovarian cancer patient-derived organoids (PDOs)**: establishment success **54% (7/13)**; organoids preserve histology, IHC, variants (including BRCA1) and CNVs; used for drug-response testing; cryopreservation slowed regrowth **14 vs 10 days (P<0.01)**. (Chang 2024, Cell Transplantation; DOI https://doi.org/10.1177/09636897241281869; publication Jan 2024) (chang2024ovariancancerpatientderived pages 1-2)

### 15.3 Model limitations (selected)
The HGSOC GEMM highlights limitations such as differences in mouse anatomy (ovarian bursa) and challenges modeling metastasis. (blackman2024mycissufficient pages 20-21)

---

## Direct abstract quotes supporting key claims (selected)

* EMQN best practice (HBOC testing complexity and changes): the past decade brought “significant changes to hereditary breast and ovarian cancer (HBOC) diagnostic testing with new treatments, testing methods and strategies…” (McDevitt 2024; DOI https://doi.org/10.1038/s41431-023-01507-5) (mcdevitt2024emqnbestpractice pages 1-2)
* PARP synthetic lethality mechanism in HRD: “PARP inhibitors act both by inhibiting catalytic activity and by trapping PARP on DNA… producing synthetic lethality in HR-deficient (e.g., BRCA-mutant) cells.” (Mastrodomenico 2023; DOI https://doi.org/10.3390/genes14030684) (mastrodomenico2023personalizedsystemictherapies pages 2-3)

---

## Evidence gaps and notes for knowledge-base curation
1. **Ontology identifiers** (MONDO/Orphanet/MeSH/ICD) for HBOC syndrome were not found in the retrieved full-text evidence and should be pulled directly from those resources.
2. Many penetrance estimates exist; this report intentionally cites only values explicitly present in retrieved evidence. (barili2024geneticbasisof pages 1-2, ho2024agespecificbreastand pages 1-2)
3. Environmental risk factors and formal GxE interactions were minimally represented in the retrieved evidence.

---

## Key recent authoritative sources (with URLs and publication dates)
* McDevitt et al. **EMQN best practice guidelines** — Mar 2024 — https://doi.org/10.1038/s41431-023-01507-5 (mcdevitt2024emqnbestpractice pages 1-2)
* Cheng et al. **BRCA1/2 male risks and management** — Sep 2024 — https://doi.org/10.1001/jamaoncol.2024.2185 (cheng2024brca1brca2and pages 1-3)
* Ho et al. **Asian age-specific BRCA risks (Lancet Reg Health WP)** — Mar 2024 — https://doi.org/10.1016/j.lanwpc.2024.101017 (ho2024agespecificbreastand pages 1-2)
* Barili et al. **Inherited predisposition testing review** — Feb 2024 — https://doi.org/10.3390/genes15020219 (barili2024geneticbasisof pages 1-2)
* Sun & Liu **PARPi maintenance meta-analysis** — Sep 2024 — https://doi.org/10.3389/fphar.2024.1460285 (sun2024efficacyandsafety pages 1-2)
* Assad et al. **Real-world uptake of risk management** — Apr 2024 — https://doi.org/10.1007/s10549-024-07283-0 (assad2024uptakeofscreening pages 1-3)
* Ribeiro et al. **Brazil HBOC systematic review** — Mar 2024 — https://doi.org/10.1186/s40001-024-01767-x (ribeiro2024systematicreviewof pages 1-2)


References

1. (bouras2023overviewofthe pages 1-2): Ahmed Bouras, Souhir Guidara, Mélanie Leone, Adrien Buisson, Tanguy Martin-Denavit, Sophie Dussart, Christine Lasset, Sophie Giraud, Marie-Noëlle Bonnet-Dupeyron, Zine-Eddine Kherraf, Damien Sanlaville, Sandra Fert-Ferrer, Marine Lebrun, Valerie Bonadona, Alain Calender, and Nadia Boutry-Kryza. Overview of the genetic causes of hereditary breast and ovarian cancer syndrome in a large french patient cohort. Cancers, 15:3420, Jun 2023. URL: https://doi.org/10.3390/cancers15133420, doi:10.3390/cancers15133420. This article has 17 citations.

2. (mastrodomenico2023personalizedsystemictherapies pages 1-2): Luciana Mastrodomenico, Claudia Piombino, Beatrice Riccò, Elena Barbieri, Marta Venturelli, Federico Piacentini, Massimo Dominici, Laura Cortesi, and Angela Toss. Personalized systemic therapies in hereditary cancer syndromes. Genes, 14:684, Mar 2023. URL: https://doi.org/10.3390/genes14030684, doi:10.3390/genes14030684. This article has 15 citations.

3. (barili2024geneticbasisof pages 1-2): Valeria Barili, Enrico Ambrosini, Beatrice Bortesi, Roberta Minari, Erika De Sensi, Ilenia Rita Cannizzaro, Antonietta Taiani, Maria Michiara, Angelica Sikokis, Daniela Boggiani, Chiara Tommasi, Olga Serra, Francesco Bonatti, Alessia Adorni, Anita Luberto, Patrizia Caggiati, Davide Martorana, Vera Uliana, Antonio Percesepe, Antonino Musolino, and Benedetta Pellegrino. Genetic basis of breast and ovarian cancer: approaches and lessons learnt from three decades of inherited predisposition testing. Genes, 15:219, Feb 2024. URL: https://doi.org/10.3390/genes15020219, doi:10.3390/genes15020219. This article has 55 citations.

4. (mastrodomenico2023personalizedsystemictherapies pages 2-3): Luciana Mastrodomenico, Claudia Piombino, Beatrice Riccò, Elena Barbieri, Marta Venturelli, Federico Piacentini, Massimo Dominici, Laura Cortesi, and Angela Toss. Personalized systemic therapies in hereditary cancer syndromes. Genes, 14:684, Mar 2023. URL: https://doi.org/10.3390/genes14030684, doi:10.3390/genes14030684. This article has 15 citations.

5. (bonetti2023omicssciencesand pages 2-3): G. Bonetti, G. Madeo, S. Michelini, M. Ricci, M. Cestari, S. Michelini, M. Gadler, S. Benedetti, G. Guerri, F. Cristofoli, D. Generali, C. A. Donofrio, M. Cominetti, A. Fioravanti, L. Riccio, A. Bernini, E. Fulcheri, L. Stuppia, V. Gatta, S. Cecchin, G. Marceddu, and M. Bertelli. Omics sciences and precision medicine in breast and ovarian cancer. La Clinica terapeutica, 174 Suppl 2(6):104-118, 2023. URL: https://doi.org/10.7417/ct.2023.2477, doi:10.7417/ct.2023.2477. This article has 6 citations and is from a peer-reviewed journal.

6. (ho2024agespecificbreastand pages 1-2): Weang-Kee Ho, Nur Tiara Hassan, Sook-Yee Yoon, Xin Yang, Joanna M.C. Lim, Nur Diana Binte Ishak, Peh Joo Ho, Eldarina A. Wijaya, Patsy Pei-Sze Ng, Craig Luccarini, Jamie Allen, Mei-Chee Tai, Jianbang Chiang, Zewen Zhang, Mee-Hoong See, Meow-Keong Thong, Yin-Ling Woo, Alison M. Dunning, Mikael Hartman, Cheng-Har Yip, Nur Aishah Mohd Taib, Douglas F. Easton, Jingmei Li, Joanne Ngeow, Antonis C. Antoniou, Soo-Hwang Teo, Benita Kiat-Tee Tan, Su-Ming Tan, Veronique Kiak Mien Tan, Ern Yu Tan, Geok Hoon Lim, Alexis Khng, Gaik-Siew Ch’ng, Jamil Omar, Chee-Meng Yong, Ismail Aliyas, Rozita Abdul Malik, Suguna Subramaniam, Wee-Wee Sim, Chun Sen Lim, Saw-Joo Lee, Keng-Joo Lim, Mohamad Nasir Shafiee, Fuad Ismail Ismail, Mohd Pazudin Ismail, Mohamad Faiz Mohamed Jamli, Suresh Kumarasamy, John S.H. Low, Ahmad Muzamir Ahmad Mustafa, Mary J. Makanjang, Shahila Taib, Nellie Cheah, Chee-Kin Fong, Kean-Fatt Ho, Azura Deniel, Soo Fan Ang, Ahmad Radzi Ahmad Badruddin, and Lye-Mun Tho. Age-specific breast and ovarian cancer risks associated with germline brca1 or brca2 pathogenic variants – an asian study of 572 families. The Lancet Regional Health - Western Pacific, 44:101017, Mar 2024. URL: https://doi.org/10.1016/j.lanwpc.2024.101017, doi:10.1016/j.lanwpc.2024.101017. This article has 13 citations.

7. (speiser2023primarypreventionand pages 2-3): Dorothee Speiser and Ulrich Bick. Primary prevention and early detection of hereditary breast cancer. Breast Care, 18:448-454, Aug 2023. URL: https://doi.org/10.1159/000533391, doi:10.1159/000533391. This article has 10 citations and is from a peer-reviewed journal.

8. (nagy2024comprehensiveclinicalgenetics pages 1-2): Petra Nagy, János Papp, Vince Kornél Grolmusz, Anikó Bozsik, Tímea Pócza, Edit Oláh, Attila Patócs, and Henriett Butz. Comprehensive clinical genetics, molecular and pathological evaluation efficiently assist diagnostics and therapy selection in breast cancer patients with hereditary genetic background. International Journal of Molecular Sciences, 25:12546, Nov 2024. URL: https://doi.org/10.3390/ijms252312546, doi:10.3390/ijms252312546. This article has 12 citations.

9. (mcdevitt2024emqnbestpractice pages 2-3): Trudi McDevitt, Miranda Durkie, Norbert Arnold, George J. Burghel, Samantha Butler, Kathleen B. M. Claes, Peter Logan, Rachel Robinson, Katie Sheils, Nicola Wolstenholme, Helen Hanson, Clare Turnbull, and Stacey Hume. Emqn best practice guidelines for genetic testing in hereditary breast and ovarian cancer. European Journal of Human Genetics, 32:479-488, Mar 2024. URL: https://doi.org/10.1038/s41431-023-01507-5, doi:10.1038/s41431-023-01507-5. This article has 31 citations and is from a domain leading peer-reviewed journal.

10. (liu2023prophylacticinterventionsfor pages 17-19): Taoran Liu, Jing Yu, Yangyang Gao, Xinyang Ma, Shan Jiang, Yuanyuan Gu, and Wai-kit Ming. Prophylactic interventions for hereditary breast and ovarian cancer risks and mortality in brca1/2 carriers. Cancers, 16:103, Dec 2023. URL: https://doi.org/10.3390/cancers16010103, doi:10.3390/cancers16010103. This article has 16 citations.

11. (bouras2023overviewofthe pages 2-4): Ahmed Bouras, Souhir Guidara, Mélanie Leone, Adrien Buisson, Tanguy Martin-Denavit, Sophie Dussart, Christine Lasset, Sophie Giraud, Marie-Noëlle Bonnet-Dupeyron, Zine-Eddine Kherraf, Damien Sanlaville, Sandra Fert-Ferrer, Marine Lebrun, Valerie Bonadona, Alain Calender, and Nadia Boutry-Kryza. Overview of the genetic causes of hereditary breast and ovarian cancer syndrome in a large french patient cohort. Cancers, 15:3420, Jun 2023. URL: https://doi.org/10.3390/cancers15133420, doi:10.3390/cancers15133420. This article has 17 citations.

12. (liu2023prophylacticinterventionsfor pages 1-2): Taoran Liu, Jing Yu, Yangyang Gao, Xinyang Ma, Shan Jiang, Yuanyuan Gu, and Wai-kit Ming. Prophylactic interventions for hereditary breast and ovarian cancer risks and mortality in brca1/2 carriers. Cancers, 16:103, Dec 2023. URL: https://doi.org/10.3390/cancers16010103, doi:10.3390/cancers16010103. This article has 16 citations.

13. (assad2024uptakeofscreening pages 1-3): Hadeel Assad, Maria Levitin, Nancie Petrucelli, Mark Manning, Hayley S. Thompson, Wei Chen, Hyejeong Jang, and Michael S. Simon. Uptake of screening and risk-reducing recommendations among women with hereditary breast and ovarian cancer syndrome due to pathogenic brca1/2 variants evaluated at a large urban comprehensive cancer center. Breast cancer research and treatment, 206:261-272, Apr 2024. URL: https://doi.org/10.1007/s10549-024-07283-0, doi:10.1007/s10549-024-07283-0. This article has 5 citations and is from a peer-reviewed journal.

14. (inzoli2024uptakeofrisk‐reducing pages 1-2): Alessandra Inzoli, Serena Negri, Cristina Dell'Oro, Clarissa Costa, Liliana Marchetta, Mariaclara Boccadutri, Simona Fumagalli, Gaia Roversi, Elena Maria Sala, Chiara Celi, Valentina Rossi, and Robert Fruscio. Uptake of risk‐reducing salpingo‐oophorectomy and gynaecologic surveillance among germline brca pathogenic variants carriers. Cancer Medicine, Dec 2024. URL: https://doi.org/10.1002/cam4.70321, doi:10.1002/cam4.70321. This article has 4 citations and is from a peer-reviewed journal.

15. (liu2023prophylacticinterventionsfor pages 16-17): Taoran Liu, Jing Yu, Yangyang Gao, Xinyang Ma, Shan Jiang, Yuanyuan Gu, and Wai-kit Ming. Prophylactic interventions for hereditary breast and ovarian cancer risks and mortality in brca1/2 carriers. Cancers, 16:103, Dec 2023. URL: https://doi.org/10.3390/cancers16010103, doi:10.3390/cancers16010103. This article has 16 citations.

16. (bertozzi2023riskreducingbreastand pages 6-7): Serena Bertozzi, Ambrogio Londero, Anjeza Xholli, Guglielmo Azioni, Roberta Di Vora, Michele Paudice, Ines Bucimazza, Carla Cedolini, and Angelo Cagnacci. Risk-reducing breast and gynecological surgery for brca mutation carriers: a narrative review. Journal of Clinical Medicine, 12:1422, Feb 2023. URL: https://doi.org/10.3390/jcm12041422, doi:10.3390/jcm12041422. This article has 52 citations.

17. (nagy2024comprehensiveclinicalgenetics pages 2-4): Petra Nagy, János Papp, Vince Kornél Grolmusz, Anikó Bozsik, Tímea Pócza, Edit Oláh, Attila Patócs, and Henriett Butz. Comprehensive clinical genetics, molecular and pathological evaluation efficiently assist diagnostics and therapy selection in breast cancer patients with hereditary genetic background. International Journal of Molecular Sciences, 25:12546, Nov 2024. URL: https://doi.org/10.3390/ijms252312546, doi:10.3390/ijms252312546. This article has 12 citations.

18. (mcdevitt2024emqnbestpractice pages 3-4): Trudi McDevitt, Miranda Durkie, Norbert Arnold, George J. Burghel, Samantha Butler, Kathleen B. M. Claes, Peter Logan, Rachel Robinson, Katie Sheils, Nicola Wolstenholme, Helen Hanson, Clare Turnbull, and Stacey Hume. Emqn best practice guidelines for genetic testing in hereditary breast and ovarian cancer. European Journal of Human Genetics, 32:479-488, Mar 2024. URL: https://doi.org/10.1038/s41431-023-01507-5, doi:10.1038/s41431-023-01507-5. This article has 31 citations and is from a domain leading peer-reviewed journal.

19. (elze2024genomicinstabilityin pages 1-2): Lisa Elze, Rachel S van der Post, Janet R Vos, Arjen R Mensenkamp, Samhita Pamidimarri Naga, Juliet E Hampstead, Emma Vermeulen, Michiel Oorsprong, Tom Hofste, Michiel Simons, Iris D Nagtegaal, Nicoline Hoogerbrugge, Richarda M de Voer, and Marjolijn J L Ligtenberg. Genomic instability in non–breast or ovarian malignancies of individuals with germline pathogenic variants in brca1/2. JNCI Journal of the National Cancer Institute, 116:1904-1913, Jul 2024. URL: https://doi.org/10.1093/jnci/djae160, doi:10.1093/jnci/djae160. This article has 7 citations.

20. (katabathina2017imagingandscreening pages 1-2): Venkata S. Katabathina, Christine O. Menias, and Srinivasa R. Prasad. Imaging and screening of hereditary cancer syndromes. Radiologic clinics of North America, 55 6:1293-1309, Nov 2017. URL: https://doi.org/10.1016/j.rcl.2017.06.011, doi:10.1016/j.rcl.2017.06.011. This article has 7 citations and is from a peer-reviewed journal.

21. (rahner2008hereditarycancersyndromes. pages 1-2): Nils Rahner and Verena Steinke. Hereditary cancer syndromes. Deutsches Arzteblatt international, 105 41:706-14, Oct 2008. URL: https://doi.org/10.3238/arztebl.2008.0706, doi:10.3238/arztebl.2008.0706. This article has 168 citations and is from a peer-reviewed journal.

22. (beamer2019hereditarybreastand pages 1-3): Laura Curr Beamer. Hereditary breast and hereditary ovarian cancer: implications for the oncology nurse. Seminars in Oncology Nursing, 35:47-57, Feb 2019. URL: https://doi.org/10.1016/j.soncn.2018.12.001, doi:10.1016/j.soncn.2018.12.001. This article has 8 citations.

23. (cheng2024brca1brca2and pages 1-3): Heather H. Cheng, Jeffrey W. Shevach, Elena Castro, Fergus J. Couch, Susan M. Domchek, Rosalind A. Eeles, Veda N. Giri, Michael J. Hall, Mary-Claire King, Daniel W. Lin, Stacy Loeb, Todd M. Morgan, Kenneth Offit, Colin C. Pritchard, Edward M. Schaeffer, Brittany M. Szymaniak, Jason L. Vassy, Bryson W. Katona, and Kara N. Maxwell. <i>brca1, brca2</i>, and associated cancer risks and management for male patients. JAMA Oncology, 10:1272, Sep 2024. URL: https://doi.org/10.1001/jamaoncol.2024.2185, doi:10.1001/jamaoncol.2024.2185. This article has 40 citations and is from a highest quality peer-reviewed journal.

24. (flaum2023assessmentofpredisposition pages 31-35): NAL Flaum. Assessment of predisposition to familial non-mucinous epithelial ovarian cancer. Unknown journal, 2023.

25. (mcdevitt2024emqnbestpractice pages 1-2): Trudi McDevitt, Miranda Durkie, Norbert Arnold, George J. Burghel, Samantha Butler, Kathleen B. M. Claes, Peter Logan, Rachel Robinson, Katie Sheils, Nicola Wolstenholme, Helen Hanson, Clare Turnbull, and Stacey Hume. Emqn best practice guidelines for genetic testing in hereditary breast and ovarian cancer. European Journal of Human Genetics, 32:479-488, Mar 2024. URL: https://doi.org/10.1038/s41431-023-01507-5, doi:10.1038/s41431-023-01507-5. This article has 31 citations and is from a domain leading peer-reviewed journal.

26. (tan2024brcaandbeyond pages 2-4): Joshua Zhi Chien Tan, Zewen Zhang, Hui Xuan Goh, and Joanne Ngeow. Brca and beyond: impact on therapeutic choices across cancer. Cancers, 17:8, Dec 2024. URL: https://doi.org/10.3390/cancers17010008, doi:10.3390/cancers17010008. This article has 4 citations.

27. (kostov2022hereditarygynecologiccancer pages 5-6): Stoyan Kostov, Rafał Watrowski, Yavor Kornovski, Deyan Dzhenkov, Stanislav Slavchev, Yonka Ivanova, and Angel Yordanov. Hereditary gynecologic cancer syndromes – a narrative review. OncoTargets and therapy, 15:381-405, Apr 2022. URL: https://doi.org/10.2147/ott.s353054, doi:10.2147/ott.s353054. This article has 35 citations.

28. (sun2024efficacyandsafety pages 1-2): Guojuan Sun and Yi Liu. Efficacy and safety of parp inhibitor maintenance therapy for ovarian cancer: a meta-analysis and trial sequential analysis of randomized controlled trials. Frontiers in Pharmacology, Sep 2024. URL: https://doi.org/10.3389/fphar.2024.1460285, doi:10.3389/fphar.2024.1460285. This article has 17 citations.

29. (grigore2024themoleculardetection pages 1-2): Liliana-Georgiana Grigore, Viorica-Elena Radoi, Alexandra Serban, Adina Daniela Mihai, and Ileana Stoica. The molecular detection of germline mutations in the brca1 and brca2 genes associated with breast and ovarian cancer in a romanian cohort of 616 patients. Current Issues in Molecular Biology, 46:4630-4645, May 2024. URL: https://doi.org/10.3390/cimb46050281, doi:10.3390/cimb46050281. This article has 3 citations.

30. (list2021oncogenedxbrca1and pages 1-3): G List and B BRCA. Oncogenedx: brca1 and brca2 sequencing in hereditary breast and ovarian cancer (hboc). Unknown journal, 2021.

31. (gootzen2024riskreducingsalpingectomywith pages 1-2): TA Gootzen, M. Steenbeek, Mhd van Bommel, J. IntHout, C. Kets, Rpmg Hermens, and JA de Hullu. Risk-reducing salpingectomy with delayed oophorectomy to prevent ovarian cancer in women with an increased inherited risk: insights into an alternative strategy. Familial Cancer, 23:437-445, Jun 2024. URL: https://doi.org/10.1007/s10689-024-00412-0, doi:10.1007/s10689-024-00412-0. This article has 9 citations and is from a peer-reviewed journal.

32. (feng2023riskreducingsalpingooophorectomyamong pages 1-3): Zheng Feng, Ke Zuo, Xingzhu Ju, Xiaojun Chen, Wentao Yang, Hao Wen, Lin Yu, and Xiaohua Wu. Risk-reducing salpingo-oophorectomy among chinese women at increased risk of breast and ovarian cancer. Journal of Ovarian Research, Jun 2023. URL: https://doi.org/10.1186/s13048-023-01222-1, doi:10.1186/s13048-023-01222-1. This article has 3 citations and is from a peer-reviewed journal.

33. (barili2024geneticbasisof pages 2-4): Valeria Barili, Enrico Ambrosini, Beatrice Bortesi, Roberta Minari, Erika De Sensi, Ilenia Rita Cannizzaro, Antonietta Taiani, Maria Michiara, Angelica Sikokis, Daniela Boggiani, Chiara Tommasi, Olga Serra, Francesco Bonatti, Alessia Adorni, Anita Luberto, Patrizia Caggiati, Davide Martorana, Vera Uliana, Antonio Percesepe, Antonino Musolino, and Benedetta Pellegrino. Genetic basis of breast and ovarian cancer: approaches and lessons learnt from three decades of inherited predisposition testing. Genes, 15:219, Feb 2024. URL: https://doi.org/10.3390/genes15020219, doi:10.3390/genes15020219. This article has 55 citations.

34. (sirera2020novelapproachesfor pages 25-30): N Padilla Sirera. Novel approaches for in silico identification of pathogenic variants in brca1 and brca2 hereditary breast and ovarian cancer predisposition genes. Unknown journal, 2020.

35. (barili2024geneticbasisof pages 19-22): Valeria Barili, Enrico Ambrosini, Beatrice Bortesi, Roberta Minari, Erika De Sensi, Ilenia Rita Cannizzaro, Antonietta Taiani, Maria Michiara, Angelica Sikokis, Daniela Boggiani, Chiara Tommasi, Olga Serra, Francesco Bonatti, Alessia Adorni, Anita Luberto, Patrizia Caggiati, Davide Martorana, Vera Uliana, Antonio Percesepe, Antonino Musolino, and Benedetta Pellegrino. Genetic basis of breast and ovarian cancer: approaches and lessons learnt from three decades of inherited predisposition testing. Genes, 15:219, Feb 2024. URL: https://doi.org/10.3390/genes15020219, doi:10.3390/genes15020219. This article has 55 citations.

36. (najafabadi2023atranscriptionalresponse pages 1-2): Maryam Ghaderi Najafabadi, G. Kenneth Gray, Li Ren Kong, Komal Gupta, David Perera, Huw Naylor, Joan S. Brugge, Ashok R. Venkitaraman, and Mona Shehata. A transcriptional response to replication stress selectively expands a subset of brca2-mutant mammary epithelial cells. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40956-w, doi:10.1038/s41467-023-40956-w. This article has 6 citations and is from a highest quality peer-reviewed journal.

37. (dai2024humanfallopiantubederived pages 1-2): Yilin Dai, Jing Xu, Xiaofeng Gong, Jinsong Wei, Yijun Gao, Ranran Chai, Chong Lu, Bing Zhao, and Yu Kang. Human fallopian tube-derived organoids with tp53 and rad51d mutations recapitulate an early stage high-grade serous ovarian cancer phenotype in vitro. International Journal of Molecular Sciences, 25:886, Jan 2024. URL: https://doi.org/10.3390/ijms25020886, doi:10.3390/ijms25020886. This article has 18 citations.

38. (andaluz2024usingportuguesebrca pages 1-3): Stephanie Andaluz, Bojin Zhao, Siddharth Sinha, Philip Naderev Panuringan Lagniton, Diogo Alpuim Costa, Xiaofan Ding, Miguel Brito, and San Ming Wang. Using portuguese brca pathogenic variation as a model to study the impact of human admixture on human health. BMC Genomics, Apr 2024. URL: https://doi.org/10.1186/s12864-024-10311-4, doi:10.1186/s12864-024-10311-4. This article has 1 citations and is from a peer-reviewed journal.

39. (ribeiro2024systematicreviewof pages 1-2): Andreza Amália de Freitas Ribeiro, Nilson Moreira Cipriano Junior, and Luciana Lara dos Santos. Systematic review of the molecular basis of hereditary breast and ovarian cancer syndrome in brazil: the current scenario. European Journal of Medical Research, Mar 2024. URL: https://doi.org/10.1186/s40001-024-01767-x, doi:10.1186/s40001-024-01767-x. This article has 11 citations and is from a peer-reviewed journal.

40. (aretini2023thebrca1c.4096+1g>a pages 1-2): Paolo Aretini, Silvano Presciuttini, Aldo Pastore, Alvaro Galli, Sara Panepinto, Mariella Tancredi, Matteo Ghilli, Chiara Guglielmi, Diletta Sidoti, Caterina Congregati, and Maria Adelaide Caligo. The brca1 c.4096+1g>a is a founder variant which originated in ancient times. International Journal of Molecular Sciences, 24:15507, Oct 2023. URL: https://doi.org/10.3390/ijms242115507, doi:10.3390/ijms242115507. This article has 3 citations.

41. (arun2024brcamutatedbreastcancer pages 6-7): Banu Arun, Fergus J. Couch, Jean Abraham, Nadine Tung, and Peter A. Fasching. Brca-mutated breast cancer: the unmet need, challenges and therapeutic benefits of genetic testing. British Journal of Cancer, 131:1400-1414, Aug 2024. URL: https://doi.org/10.1038/s41416-024-02827-z, doi:10.1038/s41416-024-02827-z. This article has 75 citations and is from a domain leading peer-reviewed journal.

42. (abraham2024thepartnertrial pages 1-4): Jean E. Abraham, Karen Pinilla, Alimu Dayimu, Louise Grybowicz, Nikolaos Demiris, Caron Harvey, Lynsey M. Drewett, Rebecca Lucey, Alexander Fulton, Anne N. Roberts, Joanna R. Worley, Anita Chhabra, Wendi Qian, Anne-Laure Vallier, Richard M. Hardy, Steve Chan, Tamas Hickish, Devashish Tripathi, Ramachandran Venkitaraman, Mojca Persic, Shahzeena Aslam, Daniel Glassman, Sanjay Raj, Annabel Borley, Jeremy P. Braybrooke, Stephanie Sutherland, Emma Staples, Lucy C. Scott, Mark Davies, Cheryl A. Palmer, Margaret Moody, Mark J. Churn, Jacqueline C. Newby, Mukesh B. Mukesh, Amitabha Chakrabarti, Rebecca R. Roylance, Philip C. Schouten, Nicola C. Levitt, Karen McAdam, Anne C. Armstrong, Ellen R. Copson, Emma McMurtry, Marc Tischkowitz, Elena Provenzano, and Helena M. Earl. The partner trial of neoadjuvant olaparib with chemotherapy in triple-negative breast cancer. Nature, 629:1142-1148, Apr 2024. URL: https://doi.org/10.1038/s41586-024-07384-2, doi:10.1038/s41586-024-07384-2. This article has 52 citations and is from a highest quality peer-reviewed journal.

43. (blackman2024mycissufficient pages 1-3): Alexandra Blackman, Amy C. Rees, Robert R. Bowers, Christian M. Jones, Silvia G. Vaena, Madison A. Clark, Shelby Carter, Evan D. Villamor, Della Evans, Anthony J. Emanuel, George Fullbright, Matthew S. O’Malley, Richard L. Carpenter, David T. Long, Laura S. Spruill, Martin J. Romeo, Brian C. Orr, Kristi L. Helke, and Joe R. Delaney. Myc is sufficient to generate mid-life high-grade serous ovarian and uterine serous carcinomas in a p53-r270h mouse model. Cancer Research Communications, 4:2525-2538, Sep 2024. URL: https://doi.org/10.1158/2767-9764.crc-24-0144, doi:10.1158/2767-9764.crc-24-0144. This article has 5 citations and is from a peer-reviewed journal.

44. (chang2024ovariancancerpatientderived pages 1-2): Yu-Hsun Chang, Kun-Chi Wu, Kai-Hung Wang, and Dah-Ching Ding. Ovarian cancer patient-derived organoids used as a model for replicating genetic characteristics and testing drug responsiveness: a preliminary study. Cell Transplantation, Jan 2024. URL: https://doi.org/10.1177/09636897241281869, doi:10.1177/09636897241281869. This article has 8 citations and is from a peer-reviewed journal.

45. (blackman2024mycissufficient pages 20-21): Alexandra Blackman, Amy C. Rees, Robert R. Bowers, Christian M. Jones, Silvia G. Vaena, Madison A. Clark, Shelby Carter, Evan D. Villamor, Della Evans, Anthony J. Emanuel, George Fullbright, Matthew S. O’Malley, Richard L. Carpenter, David T. Long, Laura S. Spruill, Martin J. Romeo, Brian C. Orr, Kristi L. Helke, and Joe R. Delaney. Myc is sufficient to generate mid-life high-grade serous ovarian and uterine serous carcinomas in a p53-r270h mouse model. Cancer Research Communications, 4:2525-2538, Sep 2024. URL: https://doi.org/10.1158/2767-9764.crc-24-0144, doi:10.1158/2767-9764.crc-24-0144. This article has 5 citations and is from a peer-reviewed journal.
