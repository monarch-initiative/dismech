---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T19:32:39.108478'
end_time: '2026-04-05T19:42:05.919010'
duration_seconds: 566.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MSI-High Colorectal Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MSI-High Colorectal Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **MSI-High Colorectal Cancer** covering all of the
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
- **Disease Name:** MSI-High Colorectal Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **MSI-High Colorectal Cancer** covering all of the
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


## Disease Characteristics Research Report: MSI‑High Colorectal Cancer (MSI‑H CRC)

**Scope note (evidence limitations):** The tool-accessible corpus in this run is rich for definitions, molecular causes, diagnostic workflows, clinicopathologic correlates, and immunotherapy outcomes (especially 2023–2024). It is less complete for formal ICD/MeSH identifiers, population incidence/prevalence in registries (e.g., SEER/GBD), and non-immunotherapy treatments, and does not include POLE/POLD1-specific primary data for CRC within the retrieved evidence; those gaps are flagged where relevant.

### Target Disease
- **Disease Name:** MSI‑High Colorectal Cancer (MSI‑H CRC)
- **MONDO ID:** *Subtype not retrieved in current evidence*; parent disease **colorectal cancer MONDO:0005575** (Open Targets disease mapping; see Open Targets output embedded in state) (colle2023brafv600erasmutations pages 1-2)
- **Category:** Digestive system cancer; molecular subtype defined by DNA repair deficiency (dMMR/MSI‑H)

---

## 1. Disease Information

### 1.1 What is MSI‑High colorectal cancer?
MSI‑H CRC is a molecular subtype of colorectal adenocarcinoma characterized by **microsatellite instability (MSI)**, which is the tumor phenotype resulting from a **deficient DNA mismatch repair (dMMR) system** (parente2023thedaytodaypractice pages 2-3, ros2023immunotherapyforcolorectal pages 2-4). In practical clinical terms, CRC is classified as dMMR when **immunohistochemistry (IHC) shows loss of expression of ≥1 mismatch repair proteins** (MLH1, MSH2, MSH6, PMS2) (parente2023thedaytodaypractice pages 2-3, normanno2024resistancetoimmune pages 1-3). MSI itself can be detected by molecular assays (PCR or NGS) as instability at microsatellite loci (ros2023immunotherapyforcolorectal pages 2-4, fan2024oncologicalcharacteristicstreatments pages 4-5).

**Abstract-supported definition (verbatim):** Parente et al. (2023) describe that “Deficit in one or more MMR proteins, configuring deficient MMR status (dMMR), leads to frameshift mutations particularly clustered in microsatellite repeats. Thus, microsatellite instability (MSI) is the epiphenomenon of dMMR.” (Digestive Diseases; published May 2023; https://doi.org/10.1159/000531003) (parente2023thedaytodaypractice pages 2-3).

### 1.2 Common synonyms/alternative names
- dMMR CRC / MMR‑deficient CRC
- MSI/dMMR CRC
- Microsatellite instability‑high colorectal carcinoma
These are used interchangeably in the reviewed sources (parente2023thedaytodaypractice pages 2-3, normanno2024resistancetoimmune pages 1-3, ros2023immunotherapyforcolorectal pages 2-4, fan2024oncologicalcharacteristicstreatments pages 4-5).

### 1.3 Key identifiers (availability in this run)
- **MONDO:** Parent disease colorectal cancer **MONDO:0005575** (Open Targets mapping) (colle2023brafv600erasmutations pages 1-2)
- **MeSH / ICD‑10 / ICD‑11 / Orphanet / OMIM (disease-level):** not explicitly retrievable from the current evidence payload; MSI‑H CRC is primarily treated as a molecular subtype rather than a separate rare-disease entity.

### 1.4 Evidence source type
The synthesized disease characterization in this report is derived from **aggregated disease-level resources**, including multi-center trials, nationwide testing datasets, reviews, and retrospective cohort studies—not single-patient EHR narratives (parente2023thedaytodaypractice pages 2-3, colle2023brafv600erasmutations pages 1-2, fan2024oncologicalcharacteristicstreatments pages 4-5, fountzilas2024nationwiderealworlddata pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors
MSI‑H CRC arises when the DNA mismatch repair system fails, due to:
1) **Germline pathogenic variants** in MMR genes (Lynch syndrome) (normanno2024resistancetoimmune pages 1-3, fan2024oncologicalcharacteristicstreatments pages 1-2)
2) **Somatic MMR gene alterations** (normanno2024resistancetoimmune pages 1-3, fan2024oncologicalcharacteristicstreatments pages 1-2)
3) **Epigenetic silencing**, most prominently **MLH1 promoter hypermethylation**, leading to loss of MLH1 (and often PMS2) protein expression (parente2023thedaytodaypractice pages 2-3, normanno2024resistancetoimmune pages 1-3, mei2022clinicopathologicalcharacteristicsof pages 6-7)

Normanno et al. (2024) explicitly state that dMMR arises from “germline/somatic mutations or epigenetic silencing (e.g., MLH1 promoter hypermethylation…)” and list core MMR proteins **MSH2, MSH6, PMS2, MLH1** (published May 2024; https://doi.org/10.37349/etat.2024.00231) (normanno2024resistancetoimmune pages 1-3).

### 2.2 Risk factors (genetic)
- **Lynch syndrome** is caused by germline pathogenic variants in MLH1/MSH2/MSH6/PMS2 (and EPCAM deletions can lead to MSH2 silencing, noted in review) (normanno2024resistancetoimmune pages 1-3, fan2024oncologicalcharacteristicstreatments pages 1-2).
- Population prevalence of Lynch syndrome is reported as **~1 in 280–400 individuals** (Normanno 2024) (normanno2024resistancetoimmune pages 1-3).

### 2.3 Risk factors (non-genetic/environmental)
The retrieved evidence in this run does not provide primary, quantitative MSI‑H‑specific environmental or lifestyle risk modifiers beyond general CRC epidemiology. This is a gap relative to the template requirements.

### 2.4 Protective factors / gene–environment interactions
Not directly supported by the retrieved evidence in this run.

---

## 3. Phenotypes (clinical and pathological)

### 3.1 Key clinicopathologic features
Across studies and reviews, MSI‑H/dMMR CRC is associated with a characteristic “immune‑rich” histopathology:
- **Proximal/right‑sided colon predominance** (proximal localization) (dogan2024therelationshipbetween pages 1-2)
- **Mucinous differentiation** and other histologic patterns (medullary, signet‑ring) enriched in MSI/dMMR disease (dogan2024therelationshipbetween pages 1-2)
- **Tumor‑infiltrating lymphocytes (TILs)** and **Crohn’s‑like reaction** are significantly associated with dMMR in a 200‑case series (P < .001 and P = .001, respectively) (dogan2024therelationshipbetween pages 1-2)

**Abstract-supported statements (verbatim/near-verbatim):** In a 200‑case CRC resection cohort, Doğan et al. (2024) report significant differences in “tumor‑infiltrating lymphocytes… Crohn’s‑like reaction… mucinous differentiation… and presence of metastatic lymph nodes” between MMR‑preserved sporadic cases and Lynch candidates (published Sep 2024; https://doi.org/10.5152/tjg.2024.23366) (dogan2024therelationshipbetween pages 1-2).

### 3.2 Phenotype characteristics (onset, progression, frequency)
- **Frequency among CRC:** MSI/dMMR comprises about **15%** of CRC overall in several reviews (normanno2024resistancetoimmune pages 1-3, fan2024oncologicalcharacteristicstreatments pages 1-2).
- **Stage distribution (enrichment in earlier stages):** about **20%** in stage I–II, **~13%** in stage III, and **~4–5%** in stage IV/metastatic CRC (normanno2024resistancetoimmune pages 1-3). Another 2024 review summarizes ~20% in stage II, ~12% in stage III, and ~4% in stage IV (fan2024oncologicalcharacteristicstreatments pages 1-2).

### 3.3 Suggested HPO terms (examples)
Because MSI‑H CRC is a tumor subtype, phenotype capture often maps to neoplastic and histopathologic features rather than symptoms. Suggested HPO terms include:
- **Colorectal carcinoma** (HP:0003003; commonly used for colorectal cancer phenotyping)
- **Mucinous adenocarcinoma** (HPO term exists for mucinous carcinoma phenotypes; confirm exact ID during curation)
- **Increased tumor-infiltrating lymphocytes** (no single universal HPO term; may be represented via pathology annotations rather than HPO)

*Note:* Exact HPO identifiers for histopathology descriptors should be validated against the current HPO release; the present run did not include an HPO lookup tool.

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes (core MMR machinery)
Core genes repeatedly cited:
- **MLH1, MSH2, MSH6, PMS2** (parente2023thedaytodaypractice pages 2-3, normanno2024resistancetoimmune pages 1-3, fan2024oncologicalcharacteristicstreatments pages 1-2)

These correspond to proteins assessed by IHC to define dMMR in routine clinical practice (parente2023thedaytodaypractice pages 2-3, ros2023immunotherapyforcolorectal pages 2-4).

### 4.2 Pathogenic variant classes and origin
- **Germline (Lynch syndrome):** pathogenic/likely pathogenic variants in MMR genes (normanno2024resistancetoimmune pages 1-3)
- **Somatic/epigenetic (sporadic MSI‑H CRC):** MLH1 promoter hypermethylation and somatic MMR alterations (normanno2024resistancetoimmune pages 1-3, fan2024oncologicalcharacteristicstreatments pages 1-2)

### 4.3 Epigenetic information
- **MLH1 promoter hypermethylation** is a major mechanism for sporadic MSI‑H CRC (normanno2024resistancetoimmune pages 1-3, fan2024oncologicalcharacteristicstreatments pages 1-2).
- A narrative review excerpt reports that **~80% of dMMR CRCs show MLH1 promoter methylation** (mei2022clinicopathologicalcharacteristicsof pages 6-7).

### 4.4 Molecular profiling / immune microenvironment
MSI‑H/dMMR CRC is described as **hypermutated**, yielding more neoantigens and an immune‑inflamed microenvironment with immune checkpoint upregulation, supporting response to PD‑1/PD‑L1 and CTLA‑4 blockade (parente2023thedaytodaypractice pages 2-3, normanno2024resistancetoimmune pages 1-3, ros2023immunotherapyforcolorectal pages 2-4).

### 4.5 Suggested GO (process) and CL (cell type) terms
Based on the mechanistic chain (dMMR → frameshift mutations → neoantigens → T‑cell infiltration → checkpoint upregulation):
- **GO biological processes (suggestions):** DNA mismatch repair; response to DNA damage stimulus; antigen processing and presentation (MHC class I); T cell activation; interferon‑gamma signaling.
- **Cell Ontology (CL) suggestions:** cytotoxic T cell (CD8+ T cell); T helper 1 cell; tumor-associated macrophage.

*Note:* Exact GO/CL IDs should be validated during curation; the run did not include ontology lookup tooling.

---

## 5. Environmental Information

MSI‑H CRC is defined by tumor DNA repair biology and is most directly linked to genetic/epigenetic mechanisms. The retrieved evidence does not provide MSI‑H‑specific environmental toxicant, infectious, or lifestyle causation signals. This section should be populated from dedicated epidemiologic literature (not captured here).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (current understanding)
1) **Upstream trigger:** loss of function in MMR (germline mutation, somatic mutation, or MLH1 promoter hypermethylation) (normanno2024resistancetoimmune pages 1-3, fan2024oncologicalcharacteristicstreatments pages 1-2)
2) **Genomic consequence:** accumulation of insertion/deletion errors at microsatellite repeats → **frameshift mutations** (parente2023thedaytodaypractice pages 2-3)
3) **Immunogenic consequence:** high tumor mutational burden and frameshift-derived neoantigens → increased immune infiltration and checkpoint expression (PD‑1/PD‑L1/CTLA‑4) (parente2023thedaytodaypractice pages 2-3, normanno2024resistancetoimmune pages 1-3, ros2023immunotherapyforcolorectal pages 2-4)
4) **Therapeutic implication:** strong rationale for immune checkpoint blockade; however, a subset (~30%) exhibit primary resistance to single-agent PD‑1 therapy (normanno2024resistancetoimmune pages 1-3).

### 6.2 Upstream vs downstream
- **Upstream:** MLH1 methylation; germline/somatic MMR gene alterations (normanno2024resistancetoimmune pages 1-3)
- **Downstream:** hypermutation/neoantigen burden; immune cell infiltration; checkpoint expression; treatment sensitivity/resistance patterns (normanno2024resistancetoimmune pages 1-3, ros2023immunotherapyforcolorectal pages 2-4)

---

## 7. Anatomical Structures Affected

### 7.1 Organ level
- Primary organ system: **large intestine (colon and rectum)**; MSI‑H/dMMR is enriched in **proximal/right-sided colon** in observational pathology cohorts (dogan2024therelationshipbetween pages 1-2).

### 7.2 Tissue/cell level
- Primary tissue: **colonic/rectal epithelium (glandular epithelium)** giving rise to adenocarcinoma.
- Immune microenvironment: increased TILs (dogan2024therelationshipbetween pages 1-2).

### 7.3 Suggested UBERON terms
- Colon (e.g., UBERON:0001155) and subregions such as ascending colon (right/proximal)

*Note:* Exact IDs should be validated during curation.

---

## 8. Temporal Development

- MSI‑H/dMMR is more prevalent in early-stage/localized CRC (stage I–II) than metastatic CRC (stage IV), consistent with reduced representation among metastatic cases (normanno2024resistancetoimmune pages 1-3, fan2024oncologicalcharacteristicstreatments pages 1-2).

The retrieved evidence does not provide a formal natural-history staging timeline beyond stage distribution; additional longitudinal registry studies would be needed.

---

## 9. Inheritance and Population

### 9.1 Epidemiology (proportion of CRC that is MSI‑H/dMMR)
- **~15% of CRC** overall are dMMR/MSI (normanno2024resistancetoimmune pages 1-3).
- Stage-specific distribution: **~20%** in stage I–II, **~13%** in stage III, **~4–5%** in stage IV (normanno2024resistancetoimmune pages 1-3).

### 9.2 Hereditary contribution and Lynch syndrome
- Approximately **~3% of all CRC** are attributed to germline MMR mutations in the Normanno review excerpt (normanno2024resistancetoimmune pages 1-3).
- Among MSI/dMMR CRC, about **~20% are Lynch syndrome-related** in Parente et al. (2023) (parente2023thedaytodaypractice pages 2-3).

---

## 10. Diagnostics

### 10.1 Clinical/pathology tests
**Primary diagnostic modalities:**
- **MMR IHC** (MLH1/MSH2/MSH6/PMS2): loss of one or more proteins defines dMMR (parente2023thedaytodaypractice pages 2-3).
- **PCR-based MSI**: recommended pentaplex marker sets and instability thresholds (ros2023immunotherapyforcolorectal pages 2-4).
- **NGS-based MSI**: increasingly used; can outperform some algorithms especially in low tumor purity settings (not fully explored in retrieved evidence, but NGS use and specimen constraints are noted) (fan2024oncologicalcharacteristicstreatments pages 4-5).

**Performance / discordance:**
- IHC and PCR concordance reported **~90–97%** in CRC (ros2023immunotherapyforcolorectal pages 2-4).
- Discordance reported around **1–10%** in one 2024 review excerpt; under standardized conditions, a positive result from either test can be used to justify ICI use (fan2024oncologicalcharacteristicstreatments pages 4-5).
- In a nationwide real‑world Greek dataset, among tumors tested by both approaches, overall discordance was **2.3% (21/904)** (published May 2024; https://doi.org/10.3390/diagnostics14111076) (fountzilas2024nationwiderealworlddata pages 1-2).

### 10.2 Sporadic vs Lynch syndrome triage (MLH1 loss workup)
A standard discriminatory concept in the retrieved sources is:
- **Sporadic dMMR/MSI‑H CRC:** often MLH1 promoter hypermethylation, with **BRAF V600E** frequently present (normanno2024resistancetoimmune pages 1-3, mei2022clinicopathologicalcharacteristicsof pages 6-7).
- **Hereditary (Lynch) suspicion:** absence of BRAF mutation and absence of MLH1 methylation raise suspicion for Lynch syndrome (mei2022clinicopathologicalcharacteristicsof pages 6-7).

In the ICI-treated metastatic cohort analysis by Colle et al. (2023), “sporadic” was operationalized as **loss of MLH1/PMS2 with BRAFV600E and/or MLH1 promoter hypermethylation, or biallelic somatic MMR mutations**, while Lynch required a detected germline MMR mutation (published Apr 2023; https://doi.org/10.1093/oncolo/oyad082) (colle2023brafv600erasmutations pages 1-2).

### 10.3 Suggested differential diagnosis considerations
The main practical differential is **false-positive/false-negative MSI/dMMR testing** due to assay pitfalls or tumor heterogeneity; misdiagnosis is explicitly discussed as a contributor to apparent ICI “resistance” (normanno2024resistancetoimmune pages 1-3).

---

## 11. Outcome / Prognosis

The retrieved evidence emphasizes predictive/prognostic implications rather than registry-derived survival by stage.
- MSI/dMMR CRC can show resistance to 5‑FU in some contexts and strong sensitivity to immune checkpoint blockade (parente2023thedaytodaypractice pages 2-3).
- A subset of metastatic MSI‑H/dMMR CRC (up to **~30%**) can show progressive disease on single-agent PD‑1 therapy (normanno2024resistancetoimmune pages 1-3).

For comprehensive long-term prognosis (5‑year OS by stage), SEER/registry sources are needed and were not included in this run.

---

## 12. Treatment

### 12.1 Immunotherapy (current real-world implementation)
**Metastatic setting**
- **KEYNOTE‑177 (NCT02563002):** Pembrolizumab as first-line therapy improved PFS vs chemotherapy. Colle et al. cite median **PFS 16.5 vs 8.2 months (HR 0.60, 95% CI 0.45–0.80; P=.0002)** (colle2023brafv600erasmutations pages 1-2). A 2023 review table reports **ORR 43.8%**, including **CR 11.1%** and **PR 32.7%**, with median PFS ~16.5 months (ros2023immunotherapyforcolorectal pages 2-4).
- **CheckMate‑142 (previously treated mCRC):** Nivolumab monotherapy ORR **31.1%** (phase II; n=74) as summarized in Normanno 2024 (normanno2024resistancetoimmune pages 1-3).

**Real-world comparative effectiveness:** A clinicogenomic cohort (Foundation Medicine testing across ~280 US clinics) reported in 138 MSI‑H mCRC patients that first‑line ICIs vs chemotherapy had median **PFS 24.87 vs 5.65 months** (AHR 0.31) and **OS not reached vs 24.1 months** (HR 0.45) (quintanilha2023comparativeeffectivenessof pages 1-2).

### 12.2 Neoadjuvant immunotherapy (2023–2024 development highlight)
Neoadjuvant ICI for localized dMMR/MSI‑H colon cancer has shown striking pathologic regression:
- **NICHE‑2:** MPR **95%**, pCR **68%** in a 2024 review excerpt (fan2024oncologicalcharacteristicstreatments pages 4-5).
- **NICHE‑3 (Nature Medicine 2024; NCT03026140):** Nivolumab + relatlimab (anti‑PD‑1 + anti‑LAG‑3) achieved pathologic response **97% (57/59)**, MPR **92%**, and pCR **68% (40/59)**, with grade 3–4 immune‑related adverse events **10%** (https://doi.org/10.1038/s41591-024-03250-w) (gooyer2024neoadjuvantnivolumaband media 4e5d7e56, gooyer2024neoadjuvantnivolumaband media 37cc97ed, gooyer2024neoadjuvantnivolumaband media 1ac973b3, gooyer2024neoadjuvantnivolumaband media 592f02c3).

### 12.3 Treatment ontology (MAXO) suggestions
- Immune checkpoint inhibitor therapy (anti‑PD‑1; anti‑CTLA‑4; anti‑LAG‑3)
- Neoadjuvant immunotherapy
- Surgical resection (colectomy/proctectomy)

*Note:* Exact MAXO IDs should be curated separately.

### 12.4 Ongoing trials (examples from ClinicalTrials.gov search)
The trial search retrieved multiple active studies of neoadjuvant/adjuvant PD‑1–based strategies in dMMR/MSI‑H colorectal cancer (e.g., NCT04643041 watch‑and‑wait distal rectal cancer; NCT06520683 adjuvant PD‑1 blockade high-risk stage II; NCT03926338 toripalimab ± celecoxib) (clinical trial tool output; not individually evidenced in text snippets in this run).

---

## 13. Prevention

No MSI‑H‑specific primary prevention strategies are evidenced in the retrieved corpus beyond the implicit prevention of Lynch-associated cancers via identification and surveillance. A complete prevention section would require guideline sources (e.g., USPSTF, NCCN) not included in the tool-evidence payload.

---

## 14. Other Species / Natural Disease

No non-human naturally occurring MSI‑H CRC evidence was retrieved in this run.

---

## 15. Model Organisms

### 15.1 MSI‑H/dMMR-specific model systems (2023 example)
Song et al. (Frontiers in Oncology 2023; https://doi.org/10.3389/fonc.2023.1223915) report:
- **Organoids** derived from intestine tumors in an **Msh2-deficient mouse model**, with MSI‑H and high frameshift mutation frequency.
- An **orthotopic intra‑cecal implantation** model from organoid-derived tumor fragments showing progressive growth and **distant metastasis to liver and lymph node**, forming adenocarcinomas “mixed with mucinous features.” The authors propose suitability for testing **neoantigen-based vaccines** and combination therapies (song2023organoidsandmetastatic pages 1-2).

---

# Summary Table (quantitative quick reference)

| Topic (definition/prevalence/diagnostic criterion/trial outcome) | Key data point(s) | Source (first author, journal, year) | PMID if available (leave blank if not in evidence) | URL | Citation ID |
|---|---|---|---|---|---|
| Definition | dMMR = loss of expression of one or more MMR proteins by IHC; MSI is the molecular phenotype caused by defective mismatch repair and associated frameshift/missense mutations and neoantigen generation | Parente, *Digestive Diseases*, 2023 |  | https://doi.org/10.1159/000531003 | (parente2023thedaytodaypractice pages 2-3) |
| Definition | Core MMR proteins implicated: **MLH1, MSH2, MSH6, PMS2**; dMMR can result from germline/somatic mutations or epigenetic silencing such as **MLH1 promoter hypermethylation** | Normanno, *Exploration of Targeted Anti-tumor Therapy*, 2024 |  | https://doi.org/10.37349/etat.2024.00231 | (normanno2024resistancetoimmune pages 1-3) |
| Prevalence | dMMR/MSI represents **~15–20% of stage II–III CRC** and **~4% of metastatic CRC** | Parente, *Digestive Diseases*, 2023 |  | https://doi.org/10.1159/000531003 | (parente2023thedaytodaypractice pages 2-3) |
| Prevalence | Stage distribution reported as **~20% in stage I–II**, **13% in stage III**, and **4–5% in stage IV/metastatic CRC** | Normanno, *Exploration of Targeted Anti-tumor Therapy*, 2024 |  | https://doi.org/10.37349/etat.2024.00231 | (normanno2024resistancetoimmune pages 1-3) |
| Prevalence | Alternative stage-specific summary: **~20% stage II**, **~12% stage III**, **~4% stage IV CRC** | Fan, *Biomarker Research*, 2024 |  | https://doi.org/10.1186/s40364-024-00640-7 | (fan2024oncologicalcharacteristicstreatments pages 1-2) |
| Hereditary vs sporadic etiology | About **~20% of dMMR/MSI CRC are Lynch syndrome-related** | Parente, *Digestive Diseases*, 2023 |  | https://doi.org/10.1159/000531003 | (parente2023thedaytodaypractice pages 2-3) |
| Hereditary vs sporadic etiology | Across all CRC, **~15% are dMMR/MSI**; most are sporadic with **MLH1 hypermethylation ~12%**, and **~3%** are due to germline MMR mutations | Normanno, *Exploration of Targeted Anti-tumor Therapy*, 2024 |  | https://doi.org/10.37349/etat.2024.00231 | (normanno2024resistancetoimmune pages 1-3) |
| Sporadic vs Lynch discriminator | **BRAF V600E** co-mutation occurs in **~30% of sporadic dMMR/MSI cases** | Normanno, *Exploration of Targeted Anti-tumor Therapy*, 2024 |  | https://doi.org/10.37349/etat.2024.00231 | (normanno2024resistancetoimmune pages 1-3) |
| Diagnostic criterion | PCR pentaplex markers often used: **NR-27, NR-21, NR-24, BAT-25, BAT-26**; MSI-H called when **≥3/5 markers unstable** (or **2 markers** when paired normal tissue is used) | Ros, *Cancers*, 2023 |  | https://doi.org/10.3390/cancers15174245 | (ros2023immunotherapyforcolorectal pages 2-4) |
| Diagnostic criterion | Alternative PCR definition reported: **two or more** single-nucleotide repeat fragment size changes **≥3 bp = MSI-H**; one or none = non-MSI-H | Fan, *Biomarker Research*, 2024 |  | https://doi.org/10.1186/s40364-024-00640-7 | (fan2024oncologicalcharacteristicstreatments pages 4-5) |
| Diagnostic performance | Concordance between **IHC and PCR** in CRC reported as **90–97%** | Ros, *Cancers*, 2023 |  | https://doi.org/10.3390/cancers15174245 | (ros2023immunotherapyforcolorectal pages 2-4) |
| Diagnostic discordance | IHC and MSI testing discordance reported at **1–10%**; under standardized conditions, a positive result from either test may justify ICI use | Fan, *Biomarker Research*, 2024 |  | https://doi.org/10.1186/s40364-024-00640-7 | (fan2024oncologicalcharacteristicstreatments pages 4-5) |
| First-line metastatic trial outcome | **KEYNOTE-177**: pembrolizumab vs chemotherapy, median **PFS 16.5 vs 8.2 months**, **HR 0.60** (95% CI 0.45–0.80; P=.0002) | Colle, *The Oncologist*, 2023 |  | https://doi.org/10.1093/oncolo/oyad082 | (colle2023brafv600erasmutations pages 1-2) |
| First-line metastatic trial outcome | **KEYNOTE-177** reported **ORR 43.8%**, including **CR 11.1%** and **PR 32.7%**, with median PFS about **16.5 months** in the PCR/IHC-defined cohort | Ros, *Cancers*, 2023 |  | https://doi.org/10.3390/cancers15174245 | (ros2023immunotherapyforcolorectal pages 2-4) |
| Real-world implementation | In a US clinicogenomic cohort of **138 MSI-H mCRC** patients receiving first-line ICIs vs chemotherapy: median **PFS 24.87 vs 5.65 months** (AHR 0.31), **OS not reached vs 24.1 months** (HR 0.45), **TTNT not reached vs 7.23 months** (AHR 0.17) | Quintanilha, unknown journal, 2023 |  |  | (quintanilha2023comparativeeffectivenessof pages 1-2) |
| Advanced disease immunotherapy outcome | **CheckMate-142** nivolumab monotherapy in previously treated dMMR/MSI mCRC: **ORR 31.1%** (phase II; n=74) | Normanno, *Exploration of Targeted Anti-tumor Therapy*, 2024 |  | https://doi.org/10.37349/etat.2024.00231 | (normanno2024resistancetoimmune pages 1-3) |
| Resistance estimate | Up to **30%** of dMMR/MSI metastatic CRC patients may show progressive disease with **single-agent anti-PD-1** therapy | Normanno, *Exploration of Targeted Anti-tumor Therapy*, 2024 |  | https://doi.org/10.37349/etat.2024.00231 | (normanno2024resistancetoimmune pages 1-3) |
| Neoadjuvant trial outcome | **NICHE-2** (ipilimumab + nivolumab): **major pathologic response 95%**, **pathologic complete response 68%** in dMMR/MSI-H colon cancer | Fan, *Biomarker Research*, 2024 |  | https://doi.org/10.1186/s40364-024-00640-7 | (fan2024oncologicalcharacteristicstreatments pages 4-5) |
| Neoadjuvant trial outcome | **NICHE-3** (nivolumab + relatlimab): **100% pathologic response**, **pCR 79%** | Fan, *Biomarker Research*, 2024 |  | https://doi.org/10.1186/s40364-024-00640-7 | (fan2024oncologicalcharacteristicstreatments pages 4-5) |
| Neoadjuvant trial outcome | Phase 2 **NICHE-3** publication: pathologic response in **57/59 (97%)**, **major pathologic response 54/59 (92%)**, **pCR 40/59 (68%)**; grade 3–4 irAEs **10%** | de Gooyer, *Nature Medicine*, 2024 |  | https://doi.org/10.1038/s41591-024-03250-w | (fan2024oncologicalcharacteristicstreatments pages 4-5) |
| Rectal cancer organ-preservation signal | Dostarlimab neoadjuvant therapy in small stage II–III rectal cancer cohort reported **clinical complete response in 12 patients** with no progression/recurrence during follow-up | Parente, *Digestive Diseases*, 2023 |  | https://doi.org/10.1159/000531003 | (parente2023thedaytodaypractice pages 2-3) |


*Table: This table compiles the main definitions, prevalence estimates, diagnostic thresholds, and headline immunotherapy outcomes for MSI-high/dMMR colorectal cancer from the gathered evidence. It is useful as a quick-reference summary for knowledge base population and citation tracking.*

---

## Recent developments and expert analysis (2023–2024 prioritized)

1) **Neoadjuvant immunotherapy is rapidly moving from proof-of-concept toward broader clinical testing** in localized dMMR colon cancer, with NICHE‑3 (2024) demonstrating very high pathologic response rates and manageable grade 3–4 irAEs at 10% (gooyer2024neoadjuvantnivolumaband media 4e5d7e56, gooyer2024neoadjuvantnivolumaband media 37cc97ed).
2) **Diagnostic accuracy and correct classification (sporadic vs Lynch; true MSI/dMMR vs assay artifact) are emphasized as prerequisites** for optimal immunotherapy selection, and misdiagnosis is explicitly raised as a cause of early ICI progression in MSI/dMMR mCRC (normanno2024resistancetoimmune pages 1-3).
3) **Real-world data show growing MSI/MMR testing uptake** and high but not perfect concordance between IHC and MSI methods (2.3% discordance in a nationwide dataset) (fountzilas2024nationwiderealworlddata pages 1-2).

---

## Gaps relative to the template (not supported by retrieved evidence here)
- Formal MeSH/ICD‑10/ICD‑11 codes and a MONDO ID specific to “MSI‑H colorectal cancer” subtype.
- MSI‑H‑specific environmental/lifestyle risk modifiers and protective factors.
- Comprehensive survival statistics (e.g., 5‑year OS) from cancer registries.
- POLE/POLD1-driven “ultramutated” CRC data within the retrieved evidence set.

These items can be filled by targeted retrieval from guideline/registry/ontology resources in a subsequent run.


References

1. (colle2023brafv600erasmutations pages 1-2): Raphael Colle, Sara Lonardi, Marine Cachanado, Michael J Overman, Elena Elez, Marwan Fakih, Francesca Corti, Priya Jayachandran, Magali Svrcek, Antoine Dardenne, Baptiste Cervantes, Alex Duval, Romain Cohen, Filippo Pietrantonio, and Thierry André. Braf v600e/ras mutations and lynch syndrome in patients with msi-h/dmmr metastatic colorectal cancer treated with immune checkpoint inhibitors. The Oncologist, 28:771-779, Apr 2023. URL: https://doi.org/10.1093/oncolo/oyad082, doi:10.1093/oncolo/oyad082. This article has 41 citations.

2. (parente2023thedaytodaypractice pages 2-3): Paola Parente, Federica Grillo, Alessandro Vanoli, Maria Cristina Macciomei, Maria Raffaella Ambrosio, Nunzia Scibetta, Emanuela Filippi, Ivana Cataldo, Luigi Baron, Giuseppe Ingravallo, Gerardo Cazzato, Laura Melocchi, Barbara Liserre, Carla Giordano, Graziana Arborea, Emanuela Pilozzi, Antonio Scapinello, Maria Costanza Aquilano, Roberta Gafà, Serena Battista, Luca Dal Santo, Michela Campora, Francesco Giuseppe Carbone, Chiara Sartori, Stefano Lazzi, Ester Hanspeter, Valentina Angerilli, Luca Mastracci, and Matteo Fassan. The day-to-day practice of mmr and msi assessment in colorectal adenocarcinoma: what we know and what we still need to explore. Digestive Diseases, 41:746-756, May 2023. URL: https://doi.org/10.1159/000531003, doi:10.1159/000531003. This article has 48 citations and is from a peer-reviewed journal.

3. (ros2023immunotherapyforcolorectal pages 2-4): Javier Ros, Iosune Baraibar, Nadia Saoudi, Marta Rodriguez, Francesc Salvà, Josep Tabernero, and Elena Élez. Immunotherapy for colorectal cancer with high microsatellite instability: the ongoing search for biomarkers. Cancers, 15:4245, Aug 2023. URL: https://doi.org/10.3390/cancers15174245, doi:10.3390/cancers15174245. This article has 53 citations.

4. (normanno2024resistancetoimmune pages 1-3): Nicola Normanno, Vincenza Caridi, Matteo Fassan, Antonio Avallone, Fortunato Ciardiello, and Carmine Pinto. Resistance to immune checkpoint inhibitors in colorectal cancer with deficient mismatch repair/microsatellite instability: misdiagnosis, pseudoprogression and/or tumor heterogeneity? Exploration of Targeted Anti-tumor Therapy, 5:495-507, May 2024. URL: https://doi.org/10.37349/etat.2024.00231, doi:10.37349/etat.2024.00231. This article has 7 citations.

5. (fan2024oncologicalcharacteristicstreatments pages 4-5): Wen-Xuan Fan, Fei Su, Yan Zhang, Xiao-Ling Zhang, Yun-Yi Du, Yang-Jun Gao, Wei-Ling Li, Wen-Qing Hu, and Jun Zhao. Oncological characteristics, treatments and prognostic outcomes in mmr-deficient colorectal cancer. Biomarker Research, Aug 2024. URL: https://doi.org/10.1186/s40364-024-00640-7, doi:10.1186/s40364-024-00640-7. This article has 27 citations and is from a peer-reviewed journal.

6. (fountzilas2024nationwiderealworlddata pages 1-2): Elena Fountzilas, Theofanis Papadopoulos, Eirini Papadopoulou, Cedric Gouedard, Helen P. Kourea, Pantelis Constantoulakis, Christina Magkou, Maria Sfakianaki, Vassiliki Kotoula, Dimitra Bantouna, Georgia Raptou, Angelica A. Saetta, Georgia Christopoulou, Dimitris Hatzibougias, Electra Michalopoulou-Manoloutsiou, Eleni Siatra, Eleftherios Eleftheriadis, Evangelia Kavoura, Loukas Kaklamanis, Antigoni Sourla, George Papaxoinis, Kitty Pavlakis, Prodromos Hytiroglou, Christina Vourlakou, Petroula Arapantoni-Dadioti, Samuel Murray, George Nasioulas, Grigorios Timologos, George Fountzilas, and Zacharenia Saridaki. Nationwide real-world data of microsatellite instability and/or mismatch repair deficiency in cancer: prevalence and testing patterns. Diagnostics, 14:1076, May 2024. URL: https://doi.org/10.3390/diagnostics14111076, doi:10.3390/diagnostics14111076. This article has 4 citations.

7. (fan2024oncologicalcharacteristicstreatments pages 1-2): Wen-Xuan Fan, Fei Su, Yan Zhang, Xiao-Ling Zhang, Yun-Yi Du, Yang-Jun Gao, Wei-Ling Li, Wen-Qing Hu, and Jun Zhao. Oncological characteristics, treatments and prognostic outcomes in mmr-deficient colorectal cancer. Biomarker Research, Aug 2024. URL: https://doi.org/10.1186/s40364-024-00640-7, doi:10.1186/s40364-024-00640-7. This article has 27 citations and is from a peer-reviewed journal.

8. (mei2022clinicopathologicalcharacteristicsof pages 6-7): Wei-Jian Mei, Mi Mi, Jing Qian, Nan Xiao, Ying Yuan, and Pei-Rong Ding. Clinicopathological characteristics of high microsatellite instability/mismatch repair-deficient colorectal cancer: a narrative review. Frontiers in Immunology, Dec 2022. URL: https://doi.org/10.3389/fimmu.2022.1019582, doi:10.3389/fimmu.2022.1019582. This article has 73 citations and is from a peer-reviewed journal.

9. (dogan2024therelationshipbetween pages 1-2): Mehmet Doğan, Mehmet Kılıç, and Hayriye Tatlı Doğan. The relationship between dna mismatch repair status and clinicopathologic characteristics in colon cancer. Turkish Journal of Gastroenterology, 35:718-725, Sep 2024. URL: https://doi.org/10.5152/tjg.2024.23366, doi:10.5152/tjg.2024.23366. This article has 3 citations and is from a peer-reviewed journal.

10. (quintanilha2023comparativeeffectivenessof pages 1-2): JCF Quintanilha, RP Graf, and VA Fisher. Comparative effectiveness of immune checkpoint inhibitors vs chemotherapy in patients with metastatic colorectal cancer with measures of microsatellite instability …. Unknown journal, 2023.

11. (gooyer2024neoadjuvantnivolumaband media 4e5d7e56): Peter G. M. de Gooyer, Yara L. Verschoor, Lauren D. W. van den Dungen, Sara Balduzzi, Hendrik A. Marsman, Marnix H. Geukes Foppen, Cecile Grootscholten, Simone Dokter, Anne G. den Hartog, Wieke H. M. Verbeek, Karlijn Woensdregt, Joris J. van den Broek, Steven J. Oosterling, Ton N. Schumacher, Koert F. D. Kuhlmann, Regina G. H. Beets-Tan, John B. A. G. Haanen, Monique E. van Leerdam, Jose G. van den Berg, and Myriam Chalabi. Neoadjuvant nivolumab and relatlimab in locally advanced mmr-deficient colon cancer: a phase 2 trial. Nature Medicine, 30:3284-3290, Sep 2024. URL: https://doi.org/10.1038/s41591-024-03250-w, doi:10.1038/s41591-024-03250-w. This article has 100 citations and is from a highest quality peer-reviewed journal.

12. (gooyer2024neoadjuvantnivolumaband media 37cc97ed): Peter G. M. de Gooyer, Yara L. Verschoor, Lauren D. W. van den Dungen, Sara Balduzzi, Hendrik A. Marsman, Marnix H. Geukes Foppen, Cecile Grootscholten, Simone Dokter, Anne G. den Hartog, Wieke H. M. Verbeek, Karlijn Woensdregt, Joris J. van den Broek, Steven J. Oosterling, Ton N. Schumacher, Koert F. D. Kuhlmann, Regina G. H. Beets-Tan, John B. A. G. Haanen, Monique E. van Leerdam, Jose G. van den Berg, and Myriam Chalabi. Neoadjuvant nivolumab and relatlimab in locally advanced mmr-deficient colon cancer: a phase 2 trial. Nature Medicine, 30:3284-3290, Sep 2024. URL: https://doi.org/10.1038/s41591-024-03250-w, doi:10.1038/s41591-024-03250-w. This article has 100 citations and is from a highest quality peer-reviewed journal.

13. (gooyer2024neoadjuvantnivolumaband media 1ac973b3): Peter G. M. de Gooyer, Yara L. Verschoor, Lauren D. W. van den Dungen, Sara Balduzzi, Hendrik A. Marsman, Marnix H. Geukes Foppen, Cecile Grootscholten, Simone Dokter, Anne G. den Hartog, Wieke H. M. Verbeek, Karlijn Woensdregt, Joris J. van den Broek, Steven J. Oosterling, Ton N. Schumacher, Koert F. D. Kuhlmann, Regina G. H. Beets-Tan, John B. A. G. Haanen, Monique E. van Leerdam, Jose G. van den Berg, and Myriam Chalabi. Neoadjuvant nivolumab and relatlimab in locally advanced mmr-deficient colon cancer: a phase 2 trial. Nature Medicine, 30:3284-3290, Sep 2024. URL: https://doi.org/10.1038/s41591-024-03250-w, doi:10.1038/s41591-024-03250-w. This article has 100 citations and is from a highest quality peer-reviewed journal.

14. (gooyer2024neoadjuvantnivolumaband media 592f02c3): Peter G. M. de Gooyer, Yara L. Verschoor, Lauren D. W. van den Dungen, Sara Balduzzi, Hendrik A. Marsman, Marnix H. Geukes Foppen, Cecile Grootscholten, Simone Dokter, Anne G. den Hartog, Wieke H. M. Verbeek, Karlijn Woensdregt, Joris J. van den Broek, Steven J. Oosterling, Ton N. Schumacher, Koert F. D. Kuhlmann, Regina G. H. Beets-Tan, John B. A. G. Haanen, Monique E. van Leerdam, Jose G. van den Berg, and Myriam Chalabi. Neoadjuvant nivolumab and relatlimab in locally advanced mmr-deficient colon cancer: a phase 2 trial. Nature Medicine, 30:3284-3290, Sep 2024. URL: https://doi.org/10.1038/s41591-024-03250-w, doi:10.1038/s41591-024-03250-w. This article has 100 citations and is from a highest quality peer-reviewed journal.

15. (song2023organoidsandmetastatic pages 1-2): Yurong Song, Travis D. Kerr, Chelsea Sanders, Lisheng Dai, Shaneen S. Baxter, Brandon Somerville, Ryan N. Baugher, Stephanie D. Mellott, Todd B. Young, Heidi E. Lawhorn, Teri M. Plona, Bingfang Xu, Lei Wei, Qiang Hu, Song Liu, Alan Hutson, Baktiar Karim, Sandra Burkett, Simone Difilippantonio, Ligia Pinto, Johannes Gebert, Matthias Kloor, Steven M. Lipkin, Shizuko Sei, and Robert H. Shoemaker. Organoids and metastatic orthotopic mouse model for mismatch repair-deficient colorectal cancer. Frontiers in Oncology, Sep 2023. URL: https://doi.org/10.3389/fonc.2023.1223915, doi:10.3389/fonc.2023.1223915. This article has 10 citations.
