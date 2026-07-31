---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:39:51.002669'
end_time: '2026-07-31T00:53:09.293512'
duration_seconds: 798.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Holoprosencephaly 12 With or Without Pancreatic Agenesis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Holoprosencephaly_12_With_or_Without_Pancreatic_Agenesis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Holoprosencephaly 12 With or Without Pancreatic Agenesis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Holoprosencephaly 12 With or Without Pancreatic Agenesis** covering all of the
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
- **Disease Name:** Holoprosencephaly 12 With or Without Pancreatic Agenesis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Holoprosencephaly 12 With or Without Pancreatic Agenesis** covering all of the
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


# Holoprosencephaly 12 With or Without Pancreatic Agenesis

## Executive summary

Holoprosencephaly 12 with or without pancreatic agenesis (HPE12; **OMIM 618500; MONDO:0032787**) is an ultra-rare congenital developmental syndrome defined by holoprosencephaly (HPE) and variably absent or dysfunctional pancreas. The syndrome-defining molecular lesion is the recurrent heterozygous **CNOT1** variant **NM_016284.5:c.1603C>T, p.(Arg535Cys)**, observed de novo. It must not be confused with **CDON-related HPE11**: curated disease-target data associate HPE12 with CNOT1 (ENSG00000125107), whereas the initial CDON hit has negligible support for this entity. (OpenTargets Search: holoprosencephaly 12 with or without pancreatic agenesis-CDON, OpenTargets Search: holoprosencephaly 12 with or without pancreatic agenesis-CNOT1)

The best syndrome-specific synthesis available through 2022 comprised only six individuals/fetuses: HPE occurred in **6/6**, pancreatic abnormalities in **5/6**, pancreatic agenesis in **4/6**, intrauterine growth restriction in **4/6**, and gallbladder agenesis in **2/6**. These denominators are extremely small and subject to ascertainment bias. (cospain2022fetaldescriptionof pages 5-11, cospain2022fetaldescriptionof pages 11-11)

The clinical spectrum extends from lethal or pregnancy-terminating fetal semilobar HPE with total pancreatic agenesis to postnatal neurodevelopmental disability with endocrine/exocrine pancreatic insufficiency. A 2024 report additionally described p.Arg535Cys-associated HPE with late-onset diabetes, suggesting that normal pancreatic function in infancy does not eliminate later metabolic risk; the primary full text was not available for detailed extraction, so this extension should be treated as provisional. No disease-modifying treatment or disease-specific clinical trial was identified. Current care consists of prenatal and molecular diagnosis, genetic counseling, multidisciplinary HPE management, insulin when endocrine failure develops, and pancreatic enzyme/nutritional replacement when exocrine insufficiency is present.

| domain | disease-specific finding | suggested ontology terms/IDs where confidently known | evidence type | caveat |
|---|---|---|---|---|
| Disease identity | Holoprosencephaly 12 with or without pancreatic agenesis is a Mendelian syndrome associated with recurrent heterozygous de novo **CNOT1** p.Arg535Cys and characterized by HPE in all reported syndrome cases, often with pancreatic agenesis/insufficiency (OpenTargets Search: holoprosencephaly 12 with or without pancreatic agenesis-CNOT1, cospain2022fetaldescriptionof pages 5-11, cospain2022fetaldescriptionof pages 1-5, cospain2022fetaldescriptionof pages 11-11) | MONDO: **MONDO_0032787**; gene: **CNOT1** | Human case reports/series; curated disease-target association | Open Targets links MONDO_0032787 most strongly to **CNOT1**; older literature and some databases may still mention other HPE genes in broader differential |
| Causal variant | Reported syndrome-defining variant is **CNOT1 c.1603C>T, p.(Arg535Cys)**, heterozygous and de novo in reported families/cases (cospain2022fetaldescriptionof pages 5-11, cospain2022fetaldescriptionof pages 1-5) | HGVS: **c.1603C>T**, **p.Arg535Cys** | Human WES + parental confirmation | Current disease entity appears driven by this specific recurrent missense variant rather than generic CNOT1 haploinsufficiency |
| Inheritance | Observed inheritance in reported cases is **autosomal dominant, de novo** (cospain2022fetaldescriptionof pages 5-11, cospain2022fetaldescriptionof pages 1-5) | inheritance term label: autosomal dominant; de novo | Human trio sequencing | Penetrance outside reported Arg535Cys cases is unknown for this syndrome definition |
| Brain phenotype | HPE present in all reported syndrome cases; semilobar and lobar forms have both been described, including fetal semilobar HPE with severe midline defects (cospain2022fetaldescriptionof pages 5-11, cospain2022fetaldescriptionof pages 1-5, cospain2022fetaldescriptionof pages 11-11) | HPO labels: holoprosencephaly; semilobar holoprosencephaly; lobar holoprosencephaly | Human fetal/postnatal phenotyping, imaging, autopsy | Exact HPO IDs not confirmed here; severity is variable across reported individuals |
| Pancreas phenotype | Pancreatic anomalies occurred in **5/6** reported Arg535Cys cases; **pancreatic agenesis** documented in **4/6** and pancreatic endocrine/exocrine insufficiency in others (cospain2022fetaldescriptionof pages 1-5, cospain2022fetaldescriptionof pages 11-11) | HPO labels: pancreatic agenesis; exocrine pancreatic insufficiency; diabetes mellitus | Human case series, autopsy | Small sample size; one reported case lacked pancreatic anomaly |
| Endocrine phenotype | Pancreatic endocrine failure may present as **neonatal diabetes** in pancreas agenesis; a newer 2024 report indicates **late-onset diabetes mellitus** can also occur with CNOT1 p.Arg535Cys (cospain2022fetaldescriptionof pages 1-5, cospain2022fetaldescriptionof pages 11-11, OpenTargets Search: holoprosencephaly 12 with or without pancreatic agenesis-CDON) | HPO labels: neonatal diabetes mellitus; diabetes mellitus | Human case reports; review citing newer case | The late-onset diabetes primary report was not directly extracted here; treat as recent extension of phenotype pending full-text confirmation |
| Exocrine phenotype | Exocrine pancreatic insufficiency is part of the reported spectrum and may occur with or without complete agenesis (cospain2022fetaldescriptionof pages 1-5, cospain2022fetaldescriptionof pages 11-11) | HPO label: exocrine pancreatic insufficiency | Human case series | Frequency is imprecise because some reports summarize insufficiency and agenesis together |
| Growth/fetal phenotype | **Intrauterine growth restriction (IUGR)** was reported in **4/6** syndrome cases; broader pancreas agenesis literature shows severe fetal growth restriction, especially after 36 weeks (cospain2022fetaldescriptionof pages 11-11, poppel2024pancreasagenesisand pages 7-8) | HPO label: intrauterine growth restriction | Human case series; semiquantitative literature analysis | Growth restriction data in van Poppel 2024 are for pancreas agenesis broadly, not exclusively CNOT1-associated disease |
| Craniofacial phenotype | Recurrent dysmorphology includes median/large facial cleft, cleft lip/palate, hypertelorism, low-set/posteriorly rotated ears, epicanthal folds, nasal bridge anomalies, microcephaly, and related midline craniofacial defects (cospain2022fetaldescriptionof pages 1-5, cospain2022fetaldescriptionof pages 11-11) | HPO labels: cleft lip; cleft palate; hypertelorism; low-set ears; microcephaly; epicanthal folds | Human fetal autopsy and case summaries | Frequencies per feature are not established due to very small case count |
| Anatomy affected | Primary anatomical structures are the **forebrain/midline brain** and **pancreas**; fetal autopsy also reported **arhinencephaly**, absent corpus callosum, and occasional **gallbladder agenesis** (cospain2022fetaldescriptionof pages 1-5, cospain2022fetaldescriptionof pages 11-11) | UBERON labels: forebrain, cerebral hemisphere, pancreas, gallbladder; HPO labels: arhinencephaly; agenesis of corpus callosum | Human autopsy/imaging | Some anatomy terms are labels only because exact ontology IDs were not verified here |
| Molecular mechanism | CNOT1 encodes the scaffold of the **CCR4-NOT** complex, a regulator of gene expression, RNA stability, and mRNA deadenylation; syndrome mechanism has been proposed to impair pancreatic and neurologic development, with discussion of abnormal **SHH** pathway regulation in embryogenesis (cospain2022fetaldescriptionof pages 5-11, vissers2020denovovariants pages 1-2) | GO labels: mRNA deadenylation; regulation of mRNA stability; gene expression; signaling by Hedgehog | Human genetics; functional studies in related CNOT1 models/reviews | Direct disease-specific mechanistic proof for Arg535Cys remains limited in the extracted evidence; much mechanistic support is inferential or from broader CNOT1/CCR4-NOT biology |
| Broader CNOT1 function | Independent 2020 CNOT1 cohort established that other de novo CNOT1 variants cause neurodevelopmental disorder, supporting dosage-sensitive developmental roles for CNOT1 (vissers2020denovovariants pages 1-2) | gene: CNOT1; pathway label: CCR4-NOT complex | Human cohort; Drosophila functional assays | These variants generally do **not** define HPE12/pancreatic agenesis; they broaden CNOT1 disease biology rather than this exact syndrome |
| Diagnostics | Suggested workflow: prenatal ultrasound may detect severe HPE; fetal MRI refines brain anomalies; diagnosis has been achieved by **whole-exome sequencing** with parental confirmation; fetal autopsy can reveal pancreatic agenesis missed prenatally (cospain2022fetaldescriptionof pages 1-5, malta2023holoprosencephalyreviewof pages 9-11) | MAXO/clinical labels: prenatal ultrasound, fetal MRI, whole-exome sequencing, Sanger confirmation, fetal autopsy | Human fetal case report; HPE review | Pancreas visualization prenatally can be limited, especially early gestation |
| Differential molecular testing | In HPE generally, chromosomal analysis/CMA first, then multigene HPE panels or exome sequencing; exome can increase diagnosis in previously negative cases (malta2023holoprosencephalyreviewof pages 9-11) | test labels: karyotype, chromosomal microarray, multigene panel, exome sequencing | Review of HPE diagnostics | This is general HPE guidance, not a syndrome-specific practice guideline for CNOT1 |
| Supportive treatment | No disease-specific molecular therapy identified; management is supportive and organ-based, including **insulin replacement** for diabetes and **pancreatic enzyme replacement therapy** for exocrine insufficiency/pancreas agenesis, plus multidisciplinary HPE care (feeding, neurologic, endocrine, developmental support) (malta2023holoprosencephalyreviewof pages 9-11, OpenTargets Search: holoprosencephaly 12 with or without pancreatic agenesis-CDON) | MAXO labels: insulin therapy; pancreatic enzyme replacement therapy; supportive care | General pancreatic agenesis/NDM management; HPE review | Evidence comes largely from analogous pancreas agenesis/neonatal diabetes care rather than CNOT1-specific interventional studies |
| Prognosis | Prognosis is guarded because HPE has high mortality and universal neurodevelopmental burden in severe forms; reported syndrome outcomes range from termination of pregnancy/fetal demise to infant death or survival with developmental impairment (cospain2022fetaldescriptionof pages 11-11, malta2023holoprosencephalyreviewof pages 4-6) | HPO labels: global developmental delay; intellectual disability | Human case summaries; general HPE outcome literature | Long-term natural history for CNOT1 Arg535Cys syndrome is poorly defined because only a few cases are known |
| Evidence gaps | No disease-specific clinical trials were identified; protective factors, modifier genes, population prevalence, and validated biomarkers remain undefined for this ultra-rare syndrome (OpenTargets Search: holoprosencephaly 12 with or without pancreatic agenesis-CDON, OpenTargets Search: holoprosencephaly 12 with or without pancreatic agenesis-CNOT1) | label: evidence gap / not established | Database curation + literature synthesis | Many counseling points must rely on extrapolation from general HPE and pancreas agenesis literature rather than syndrome-specific data |


*Table: This table summarizes concise, ontology-oriented findings for Holoprosencephaly 12 with or without pancreatic agenesis, emphasizing the recurrent CNOT1 p.Arg535Cys syndrome, core phenotypes, mechanisms, diagnostics, and supportive care. It is designed to help map evidence into disease knowledge base fields while clearly marking limitations and extrapolations.*

## 1. Disease information

### Definition

HPE is failure of the embryonic prosencephalon to divide completely into paired cerebral hemispheres. HPE12 is the specific CNOT1-associated syndrome in which this forebrain malformation occurs with or without pancreatic agenesis or pancreatic endocrine/exocrine dysfunction. General HPE is classified radiologically as alobar, semilobar, lobar, middle-interhemispheric, and microform disease; p.Arg535Cys cases have included predominantly semilobar and lobar forms. (cospain2022fetaldescriptionof pages 5-11, cospain2022fetaldescriptionof pages 1-5, cospain2022fetaldescriptionof pages 11-11, malta2023holoprosencephalyreviewof pages 4-6)

### Identifiers and synonyms

- **MONDO:** MONDO:0032787.
- **OMIM phenotype:** 618500.
- **Gene:** CNOT1, CCR4-NOT transcription complex subunit 1; Ensembl ENSG00000125107.
- **Common names:** holoprosencephaly 12 with or without pancreatic agenesis; HPE12; CNOT1-related holoprosencephaly–pancreatic agenesis syndrome; pancreatic agenesis and holoprosencephaly syndrome.
- **Orphanet:** no confidently verified disease-specific identifier was recovered.
- **MeSH:** no specific descriptor; index under *Holoprosencephaly*, *Pancreatic Diseases/congenital abnormalities*, and *Pancreas/abnormalities*.
- **ICD-10:** no HPE12-specific code; HPE is generally represented under Q04.2, with separate coding for congenital pancreatic absence/malformation and diabetes as applicable.
- **ICD-11:** no syndrome-specific code verified in the retrieved sources.

This report is an aggregation of published fetal and postnatal cases and disease-level resources, not an analysis of individual EHR records. Open Targets recognizes the disease–CNOT1 association but displayed no underlying evidence rows in the queried record, illustrating the limited database depth for this ultra-rare entity. (OpenTargets Search: holoprosencephaly 12 with or without pancreatic agenesis-CNOT1)

## 2. Etiology, risks, protection, and gene–environment interaction

### Primary cause

The established cause is a **germline heterozygous de novo missense variant in CNOT1, c.1603C>T, p.Arg535Cys**. Parental Sanger testing in the fetal report confirmed de novo occurrence. The affected residue lies in a CNOT1 HEAT-repeat region. Available evidence supports a highly allele-specific developmental effect: other de novo CNOT1 variants usually cause a broader neurodevelopmental disorder without the characteristic HPE–pancreas combination. (cospain2022fetaldescriptionof pages 5-11, cospain2022fetaldescriptionof pages 1-5, vissers2020denovovariants pages 1-2)

### Genetic risk factors and modifiers

No validated modifier gene, susceptibility locus, protective allele, founder variant, or polygenic score is known for HPE12. Broader HPE is genetically heterogeneous and may be oligogenic, but this has not been demonstrated for CNOT1 p.Arg535Cys. The recurrence risk for parents after a confirmed de novo variant is low but not zero because parental germline mosaicism cannot be excluded. An affected individual would theoretically have a 50% transmission probability under autosomal-dominant inheritance, but reproductive fitness and penetrance data are unavailable.

### Environmental factors

No environmental exposure has been shown specifically to cause or modify CNOT1-HPE12. General HPE risk literature implicates poorly controlled maternal diabetes and several teratogenic exposures, but extrapolation to this monogenic syndrome should be cautious. General HPE guidance reports that periconceptional folic-acid supplementation was associated with risk reduction of up to 73%; this observational association is not proof that folate prevents CNOT1-associated disease. (malta2023holoprosencephalyreviewof pages 9-11)

No infectious trigger, occupational exposure, smoking effect, alcohol threshold, sex effect, or protective lifestyle intervention has been established for HPE12. There is likewise no validated gene–environment interaction involving CNOT1 p.Arg535Cys.

## 3. Phenotypes

The phenotype begins prenatally and is structural rather than progressive at its origin; downstream neurologic, nutritional, and endocrine consequences are lifelong. Frequencies below refer to the six published syndrome cases unless otherwise stated. (cospain2022fetaldescriptionof pages 11-11)

- **Holoprosencephaly — 6/6.** Congenital, severe but variable; semilobar and lobar disease reported. Suggested HPO: holoprosencephaly, semilobar holoprosencephaly, lobar holoprosencephaly. Neurologic consequences include severe developmental delay, motor impairment, spasticity/dystonia, epilepsy, impaired communication, and feeding dysfunction, although exact HPE12-specific frequencies are unavailable.
- **Pancreatic abnormality — 5/6; total agenesis — 4/6.** Congenital and permanent. Suggested HPO: pancreatic agenesis; pancreatic hypoplasia; exocrine pancreatic insufficiency.
- **Diabetes/endocrine insufficiency.** Often neonatal when pancreatic tissue is absent, but later onset may occur. Suggested HPO: neonatal diabetes mellitus; hyperglycemia; insulin deficiency; diabetes mellitus. Longitudinal screening is warranted even if neonatal glycemia is normal.
- **Exocrine pancreatic insufficiency.** Leads to malabsorption, steatorrhea, poor growth, and fat-soluble-vitamin deficiency. Frequency cannot be separated reliably from agenesis in the small reports.
- **Intrauterine growth restriction — 4/6.** Suggested HPO: intrauterine growth retardation; small for gestational age. The 2024 analysis of 49 pancreatic-agenesis cases of all etiologies found reduced birth weight, length, and head circumference, with stronger growth effects from 36 weeks and no detected sex difference; this is contextual rather than CNOT1-specific evidence. One CNOT1 case had head circumference at the 0.5th centile. (poppel2024pancreasagenesisand pages 7-8)
- **Craniofacial midline anomalies.** Reported findings include cleft lip/palate, large median facial cleft, hypertelorism, abnormal nasal bridge, epicanthal folds, low-set/posteriorly rotated ears, and microcephaly. Suggested HPO terms correspond to each named feature. Facial severity generally parallels brain severity in HPE.
- **Central nervous system anatomy.** Reported fetal findings include fusion of frontal and parietal lobes, arhinencephaly, and absent corpus callosum. Suggested HPO: arhinencephaly; agenesis of corpus callosum; abnormal cerebral hemisphere morphology.
- **Gallbladder agenesis — 2/6.** Suggested HPO: absent gallbladder.
- **Developmental impairment.** Surviving patients have developmental delay of variable severity. General HPE evidence indicates developmental delay is virtually universal and seizures occur in about 50%; hydrocephalus occurs in 16–40%, but neither rate is established specifically in HPE12. (malta2023holoprosencephalyreviewof pages 4-6)

There are no disease-specific EQ-5D, SF-36, PROMIS, or caregiver-burden studies. Quality of life is expected to be strongly affected by motor and cognitive disability, communication limitations, epilepsy, dysphagia, dependency for daily activities, diabetes management, and malabsorption. This inference should not be represented as measured HPE12-specific patient-reported outcome data.

A key fetal case illustrates severity: ultrasound at 15 weeks + 2 days identified semilobar HPE and a large facial cleft; termination occurred at 17 weeks + 1 day. Autopsy confirmed semilobar HPE, arhinencephaly, absent corpus callosum, unilateral cleft lip/palate, and total pancreatic agenesis. (cospain2022fetaldescriptionof pages 1-5)

## 4. Genetic and molecular information

### Gene and variant

- **Gene:** CNOT1; approved name *CCR4-NOT transcription complex subunit 1*.
- **Causal allele:** NM_016284.5:c.1603C>T; NP_057368.3:p.Arg535Cys, subject to transcript-version verification.
- **Variant class:** heterozygous germline missense, recurrent de novo.
- **Disease mechanism:** likely allele-specific altered function or hypomorphism affecting developmental RNA regulation, rather than simple generic CNOT1 haploinsufficiency.
- **Population frequency:** the allele is expected to be absent or exceptionally rare in population databases, but a verified gnomAD allele count was not available in the retrieved evidence.
- **ACMG/ClinVar:** the case literature treats the recurrent allele as causative; a current ClinVar accession and review status were not verified and should be checked directly before clinical reporting.
- **Somatic status:** not a somatic disease; reported alleles are constitutional.

The distinction between this allele-specific syndrome and broader CNOT1-related neurodevelopmental disorder is important. A 2020 cohort identified 39 individuals with other heterozygous de novo CNOT1 variants and developmental delay, intellectual disability, motor/speech delay, hypotonia, seizures, and behavioral abnormalities. Drosophila experiments showed that wild-type human CNOT1 rescued learning/memory phenotypes, while tested mutants produced absent or partial rescue; nevertheless, CNOT1 abundance and CCR4-NOT assembly could remain intact. These data support functional impairment but do not establish the exact p.Arg535Cys mechanism. (vissers2020denovovariants pages 1-2)

No validated HPE12 modifier genes, epigenetic signature, recurrent copy-number change, translocation, inversion, methylation abnormality, or chromosomal hotspot has been established.

## 5. Environmental information

HPE12 is fundamentally a genetic embryopathy. No toxin, radiation exposure, pollutant, diet, exercise pattern, smoking behavior, alcohol use, or pathogen has been causally connected to the syndrome. General HPE teratogens and maternal diabetes remain relevant to differential etiologic assessment, but do not replace identification of the pathogenic CNOT1 allele. There is no zoonotic or communicable component.

## 6. Mechanism and pathophysiology

### Upstream molecular defect

CNOT1 is the principal scaffold of the conserved **CCR4-NOT complex**, which coordinates mRNA deadenylation and decay, translation, gene-expression control, and protein quality regulation. The recurrent Arg535Cys substitution lies in a structured HEAT-repeat region and is proposed to perturb developmental regulatory interactions rather than eliminate the entire complex. (cospain2022fetaldescriptionof pages 5-11, vissers2020denovovariants pages 1-2)

### Proposed causal chain

1. **De novo CNOT1 p.Arg535Cys** alters CCR4-NOT regulatory function during early embryogenesis.
2. Altered post-transcriptional control disturbs the abundance or translation of developmental transcripts.
3. Experimental interpretation from the original syndrome work proposes abnormal persistence of **SHH** signaling and impaired **GATA4/GATA6** activity during differentiation.
4. Forebrain midline patterning fails, producing HPE and associated craniofacial midline defects.
5. Pancreatic endoderm specification and differentiation are reduced or abolished, producing pancreatic agenesis/hypoplasia.
6. Absent endocrine pancreas causes insulin deficiency, fetal growth restriction and neonatal or later diabetes; absent exocrine pancreas causes maldigestion, malabsorption and failure to thrive. (cospain2022fetaldescriptionof pages 5-11, poppel2024pancreasagenesisand pages 7-8)

The SHH/GATA causal model is biologically plausible but remains less securely established than the human genotype–phenotype association. It should be annotated as experimental/proposed, not as a fully validated linear pathway.

### Suggested ontology annotations

- **GO biological process:** mRNA poly(A)-tail shortening/deadenylation; mRNA catabolic process; regulation of mRNA stability; translational regulation; forebrain development; pancreas development; endocrine pancreas development; embryonic pattern specification; Hedgehog signaling.
- **GO cellular component:** CCR4-NOT complex; cytoplasm; nucleus; ribonucleoprotein complex.
- **Cell Ontology labels:** neuroepithelial cell; radial glial cell; neural progenitor cell; forebrain neuron; definitive endodermal cell; pancreatic progenitor cell; pancreatic beta cell; pancreatic acinar cell; ductal epithelial cell.

### Molecular profiling and advanced technologies

No disease-specific patient single-cell atlas, spatial transcriptomic dataset, proteomic signature, metabolomic or lipidomic biomarker, epigenomic signature, or CRISPR screen was found. Functional evidence includes developmental differentiation experiments reported by the original investigators and Drosophila assays for broader CNOT1 variants. Related mouse evidence shows that loss of another CCR4-NOT component, CNOT3, disrupts beta-cell identity and mRNA deadenylation, but this is pathway-level supportive evidence rather than an HPE12 model.

There is no evidence that immune dysregulation, inflammation, fibrosis, ischemia, mitochondrial dysfunction, or protein aggregation is a primary mechanism.

## 7. Anatomical structures affected

- **Primary nervous system:** prosencephalon/forebrain, cerebral hemispheres, interhemispheric midline, olfactory structures, corpus callosum, hypothalamic–pituitary region by broader HPE inference.
- **Primary digestive/endocrine system:** pancreatic primordium and resulting endocrine and exocrine pancreas.
- **Craniofacial structures:** frontonasal region, orbits, nose, upper lip, palate, ears.
- **Occasional hepatobiliary involvement:** gallbladder agenesis.

Suggested UBERON labels include forebrain, cerebral hemisphere, corpus callosum, olfactory bulb, hypothalamus, pituitary gland, pancreas, pancreatic islet, pancreatic acinus, gallbladder, palate and upper lip. Exact identifiers should be ontology-validated before database import.

HPE is intrinsically a bilateral midline-separation defect; clefts and other facial anomalies may be unilateral or asymmetric. Pancreatic agenesis is systemic rather than lateralized.

## 8. Temporal development

The causal window is early embryogenesis, during forebrain cleavage and pancreatic specification. Structural disease is congenital and can be detected in the first or early second trimester. Severe alobar/semilobar HPE may be visible by first-trimester ultrasound; fetal MRI improves anatomical characterization. The pancreas can be difficult to assess early: one report noted more reliable prenatal evaluation after approximately 19 weeks, while the index fetus underwent termination at 17 weeks and pancreatic agenesis was discovered only at autopsy. (cospain2022fetaldescriptionof pages 5-11, cospain2022fetaldescriptionof pages 1-5, malta2023holoprosencephalyreviewof pages 9-11)

The malformations do not remit. Neurologic manifestations are chronic, while seizures, hydrocephalus, feeding problems and endocrine abnormalities may emerge or evolve postnatally. Pancreatic agenesis is permanent; diabetes commonly presents neonatally but the 2024 late-onset report suggests continued surveillance is appropriate. There are no formal disease stages, remission patterns, or validated progression-rate estimates.

## 9. Inheritance and population

Inheritance is best described as **autosomal dominant due to recurrent de novo mutation**. Penetrance of HPE among the six known p.Arg535Cys cases was 100%, while pancreatic involvement was incomplete at 5/6. These figures cannot be generalized confidently because the cohort is tiny and identified through severe phenotypes. Expressivity is variable. Anticipation has not been reported. Germline mosaicism remains a theoretical recurrence mechanism. No founder effect, consanguinity association, carrier frequency, ethnic enrichment, geographic cluster, sex ratio, or sex-specific severity is known.

Disease-specific prevalence and incidence cannot be estimated from the handful of reported cases. For context only, HPE overall is much more common embryonically than among live births because of fetal loss. General HPE and pancreatic-agenesis epidemiology should not be assigned to HPE12. A 2024 semiquantitative analysis found only **49 published complete pancreatic-agenesis cases of all causes** with sufficient growth data from 1950 through January 2023, underscoring the rarity of even the broader phenotype. (poppel2024pancreasagenesisand pages 7-8)

## 10. Diagnostics

### Prenatal assessment

1. Detailed fetal ultrasound for HPE subtype, facial clefts, growth and associated anomalies.
2. Fetal MRI to delineate cerebral separation, commissures, deep gray structures, posterior fossa and pituitary region.
3. Deliberate imaging of pancreas and gallbladder when HPE is found, recognizing limited prenatal sensitivity.
4. Amniocentesis or chorionic-villus sampling for cytogenetic and molecular diagnosis.
5. Fetal autopsy after loss or termination, with explicit examination of pancreas, gallbladder, brain and pituitary. In the reported fetus, autopsy identification of pancreatic agenesis materially guided molecular interpretation and counseling. (cospain2022fetaldescriptionof pages 1-5)

### Molecular workflow

- Begin with **chromosomal microarray**, with karyotype when aneuploidy or rearrangement is suspected, because chromosomal causes are common in HPE generally.
- Use an HPE/midline-malformation panel that includes CNOT1, SHH, ZIC2, SIX3, TGIF1, CDON, GLI2 and other validated genes.
- If HPE co-occurs with pancreatic agenesis, prioritize direct analysis of **CNOT1 c.1603C>T**, while also considering PTF1A, PDX1, GATA6, GATA4, RFX6 and other pancreatic-development genes according to phenotype.
- Trio WES or WGS is appropriate when panel/CMA testing is negative or when the presentation is syndromic. General HPE evidence suggests exome sequencing can diagnose approximately 22% of previously unresolved cases. Confirm candidate variants and parental status by Sanger sequencing. (malta2023holoprosencephalyreviewof pages 9-11)
- WGS may identify noncoding or structural lesions missed by WES, but no HPE12-specific incremental-yield study exists.
- FISH, mitochondrial DNA analysis and repeat-expansion testing are not routine unless another diagnosis is suspected.

### Postnatal investigations

Brain MRI; EEG when seizures are suspected; swallowing and feeding assessment; glucose, insulin/C-peptide, ketones and HbA1c; fecal elastase, fat-soluble vitamins and nutritional indices; abdominal ultrasound/MRI; pituitary hormones, serum sodium/osmolality, thyroid and adrenal evaluation; ophthalmology, hearing, cardiac and renal assessment as clinically indicated.

There are no universally accepted HPE12-specific diagnostic criteria, biomarker, liquid biopsy, RNA diagnostic, or newborn-screening program.

### Differential diagnosis

Important alternatives include chromosomal HPE, SHH/ZIC2/SIX3/TGIF1/CDON-related HPE, Smith–Lemli–Opitz syndrome, pseudotrisomy 13, and other midline disorders. In HPE plus pancreatic agenesis/neonatal diabetes, consider **PTF1A** deficiency—often with cerebellar agenesis—plus GATA6, GATA4, PDX1, RFX6 and PTF1A enhancer disorders. CNOT1 p.Arg535Cys is distinguished by its recurrent de novo occurrence and combined HPE–pancreatic phenotype.

## 11. Outcome and prognosis

Syndrome-specific survival curves, five- or ten-year survival, life expectancy and prognostic biomarkers do not exist. Outcomes among the six reports ranged from medical termination to infant death at 16 months and survival with developmental disability. (cospain2022fetaldescriptionof pages 11-11)

General HPE—not HPE12-specific—has high early mortality. A 2023 review reported 33% mortality within 24 hours, 58% by one month and approximately 29% survival at one year. A separate European registry study of arhinencephaly/HPE estimated survival of 58.1% at one week, 47.4% at one year and 35.6% at ten years; differences reflect cohorts, case definitions and eras. (malta2023holoprosencephalyreviewof pages 4-6)

Prognosis is driven primarily by HPE subtype, brainstem/hypothalamic dysfunction, respiratory and feeding safety, epilepsy, hydrocephalus, endocrine crises, infection risk, and adequacy of diabetes and nutritional management. In general HPE, non-alobar subtype, female sex and less typical facial anomalies were associated with longer survival, but these predictors are unvalidated in HPE12.

Recovery of malformed brain or absent pancreas is not expected. Function may improve through seizure control, nutrition, communication support and rehabilitation. No formal HPE12 quality-of-life or disability-scale data are available.

## 12. Treatment and real-world implementation

There is no therapy that reverses the embryonic defect and no evidence-based genotype-directed drug for CNOT1 p.Arg535Cys.

### Endocrine and pancreatic care

- **Insulin replacement** for neonatal or later diabetes, with continuous glucose monitoring and pump therapy as feasible. Suggested MAXO: insulin therapy; blood-glucose monitoring; continuous glucose monitoring.
- **Pancreatic enzyme replacement therapy (PERT)** with feeds/meals for exocrine insufficiency, with dose titration to symptoms, growth and nutritional markers. Suggested MAXO: pancreatic enzyme replacement.
- Supplement calories, essential fatty acids and vitamins A, D, E and K when deficient; monitor growth and bone health.

These actions are extrapolated from pancreatic agenesis care. A 2023 six-patient PTF1A pancreatic-agenesis series stated that “Insulin replacement is the treatment of choice”; enzyme replacement was also used. Contemporary neonatal-diabetes practice increasingly uses NGS to establish etiology and direct precision care, but no alternative to insulin is known for absent pancreatic beta-cell mass.

### Neurologic and supportive care

Antiseizure medication guided by seizure type and EEG; treatment of dystonia/spasticity; physical, occupational, speech and augmentative-communication therapies; swallow evaluation, texture modification, aspiration precautions, and nasogastric/gastrostomy feeding when needed; management of reflux, constipation and respiratory secretions; shunting for clinically significant hydrocephalus; cleft and craniofacial surgery when medically appropriate; and vision/hearing services.

Suggested MAXO labels include brain MRI, electroencephalography, antiseizure pharmacotherapy, gastrostomy, dysphagia therapy, physical therapy, occupational therapy, speech therapy, augmentative communication, ventriculoperitoneal shunt placement, cleft repair and genetic counseling.

No validated pharmacogenomic recommendation, gene therapy, cell therapy, ASO/siRNA treatment, CRISPR intervention, immunotherapy or CNOT1-targeted small molecule exists. No disease-specific ClinicalTrials.gov study was found, and treatment-response rates or adverse-event datasets are unavailable.

## 13. Prevention

The de novo mutation cannot currently be prevented by lifestyle measures.

- **Primary prevention:** routine preconception health optimization, diabetes control, avoidance of known teratogens and standard folic-acid supplementation are reasonable for general fetal health/HPE risk, but do not specifically prevent CNOT1 mutation. General observational HPE evidence reported up to 73% lower risk with early folate use. (malta2023holoprosencephalyreviewof pages 9-11)
- **Secondary prevention/early detection:** targeted prenatal ultrasound and fetal MRI; molecular prenatal diagnosis after identification of the family variant; cascade testing is generally limited because cases are de novo.
- **Reproductive options:** genetic counseling, prenatal diagnosis by CVS/amniocentesis, and preimplantation genetic testing for a known familial variant. PGT may be considered despite low recurrence risk if parental mosaicism is suspected or if an affected individual reproduces.
- **Tertiary prevention:** early detection of diabetes, adrenal/pituitary dysfunction, aspiration, malnutrition and seizures; prompt insulin and enzyme replacement; vaccination and routine infection prevention.

There is no applicable vaccine or chemoprophylaxis specific to HPE12.

## 14. Other species and natural disease

No naturally occurring veterinary syndrome convincingly equivalent to human CNOT1 p.Arg535Cys HPE12 was identified. CNOT1 orthologs are evolutionarily conserved across vertebrates and invertebrates because CCR4-NOT is fundamental to RNA regulation. The disorder is not infectious, transmissible or zoonotic. Breed associations, VBO terms and cross-species carrier frequencies are not applicable or unknown.

## 15. Model organisms

No validated knock-in animal carrying the human Arg535Cys allele was identified in the retrieved evidence. Relevant systems include:

- **Drosophila:** used to test broader CNOT1 neurodevelopmental variants. CNOT1 depletion impaired learning/memory; wild-type human CNOT1 rescued the phenotype, while mutant constructs showed absent or partial rescue. This supports variant dysfunction but does not reproduce HPE or pancreatic agenesis. (vissers2020denovovariants pages 1-2)
- **Mouse/pathway models:** CCR4-NOT disruption has demonstrated developmental and pancreatic importance. Beta-cell-specific Cnot3 loss reduces beta-cell mass and identity and causes progressive diabetes, supporting a role for RNA deadenylation in endocrine pancreas maintenance; it is not an HPE12 model.
- **Human pluripotent-cell differentiation:** the original syndrome work used developmental differentiation approaches to support impaired pancreatic and neural development and abnormal SHH/GATA regulation. These systems are mechanistically relevant but do not capture whole-organ fetal morphogenesis.

Priority future models are CRISPR knock-in human iPSCs differentiated into forebrain organoids and pancreatic progenitors, and a conditional or constitutive Cnot1 Arg535Cys mouse. Such models could test cell-type specificity, allele-specific gain versus loss of function, SHH/GATA rescue, and therapeutic developmental windows.

## Recent developments, evidence gaps, and expert interpretation

The most informative recent contextual findings are: the **2023 HPE review** formalizing modern imaging/genomic workflows; the **2024 pancreatic-agenesis growth analysis** showing whole-body growth restriction intensifying late in gestation; and the **2024 neonatal-diabetes review**, which lists CNOT1 among six newly recognized neonatal-diabetes genes discovered from 2018 to early 2024. The reported 2024 p.Arg535Cys case with late-onset diabetes potentially broadens surveillance beyond infancy.

The central expert interpretation is that HPE12 is not simply “CNOT1 haploinsufficiency.” The striking recurrence of one missense allele and the different phenotype produced by other CNOT1 variants favor a domain- and allele-specific perturbation of CCR4-NOT developmental regulation. The strongest evidence is human recurrence and de novo status; the precise SHH/GATA molecular chain remains provisional. Pancreatic absence should be actively sought whenever HPE and p.Arg535Cys are identified, while longitudinal glucose and exocrine evaluation should continue when the pancreas appears present.

### Evidence limitations

The disease literature is dominated by isolated patients and one six-case synthesis. Accordingly, frequencies are descriptive, population statistics do not exist, penetrance is uncertain, and treatment evidence is extrapolated from general HPE, pancreatic agenesis and neonatal diabetes. No disease-specific trial, prospective registry, natural-history cohort, validated biomarker, molecular profile, or patient-reported outcome study was found.

## Selected exact abstract quotations and source details

- Cospain et al., published April 2022, DOI: https://doi.org/10.1177/10935266221095305: “Neuropathological examination confirmed the semi-lobar HPE and general autopsy disclosed a total pancreas agenesis.” The abstract also states: “Whole exome sequencing found the CNOT1 missense c.1603C>T, p.(Arg535Cys), occurring de novo in the foetus.” (cospain2022fetaldescriptionof pages 1-5)
- The same report states: “All individuals had HPE, and 4 out of 5 presented endo- and exocrine pancreatic insufficiency or total pancreas agenesis.” With the new fetus, this produced the six-case synthesis summarized above. (cospain2022fetaldescriptionof pages 5-11, cospain2022fetaldescriptionof pages 1-5)
- Malta et al., published March 2023, DOI: https://doi.org/10.3390/children10040647: “Disruption of sonic hedgehog (SHH) signaling is the main pathophysiologic mechanism underlying HPE.” This is general HPE evidence, not direct proof of the CNOT1 mechanism.
- van Poppel et al., published January 2024, DOI: https://doi.org/10.1530/ec-23-0500: “All neonates with pancreas agenesis in our study had reduced birth weight, length, and head circumference, with milder effects in those born before 36 weeks compared to after 36 weeks.” This analysis covered pancreatic agenesis of multiple genetic etiologies. (poppel2024pancreasagenesisand pages 7-8)

PMIDs were not present in the retrieved full-text metadata and therefore are not supplied rather than risk assigning incorrect identifiers.

References

1. (OpenTargets Search: holoprosencephaly 12 with or without pancreatic agenesis-CDON): Open Targets Query (holoprosencephaly 12 with or without pancreatic agenesis-CDON, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (OpenTargets Search: holoprosencephaly 12 with or without pancreatic agenesis-CNOT1): Open Targets Query (holoprosencephaly 12 with or without pancreatic agenesis-CNOT1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (cospain2022fetaldescriptionof pages 5-11): Auriane Cospain, Marie Faoucher, Aurélie Cauchois, Wilfrid Carre, Chloé Quelin, and Christèle Dubourg. Fetal description of the pancreatic agenesis and holoprosencephaly syndrome associated to a specific cnot1 variant. Pediatric and Developmental Pathology, 25:548-552, Apr 2022. URL: https://doi.org/10.1177/10935266221095305, doi:10.1177/10935266221095305. This article has 9 citations and is from a peer-reviewed journal.

4. (cospain2022fetaldescriptionof pages 11-11): Auriane Cospain, Marie Faoucher, Aurélie Cauchois, Wilfrid Carre, Chloé Quelin, and Christèle Dubourg. Fetal description of the pancreatic agenesis and holoprosencephaly syndrome associated to a specific cnot1 variant. Pediatric and Developmental Pathology, 25:548-552, Apr 2022. URL: https://doi.org/10.1177/10935266221095305, doi:10.1177/10935266221095305. This article has 9 citations and is from a peer-reviewed journal.

5. (cospain2022fetaldescriptionof pages 1-5): Auriane Cospain, Marie Faoucher, Aurélie Cauchois, Wilfrid Carre, Chloé Quelin, and Christèle Dubourg. Fetal description of the pancreatic agenesis and holoprosencephaly syndrome associated to a specific cnot1 variant. Pediatric and Developmental Pathology, 25:548-552, Apr 2022. URL: https://doi.org/10.1177/10935266221095305, doi:10.1177/10935266221095305. This article has 9 citations and is from a peer-reviewed journal.

6. (poppel2024pancreasagenesisand pages 7-8): Mireille N M van Poppel, Christopher J Nolan, and Gernot Desoye. Pancreas agenesis and fetal growth: a semiquantitative analysis. Endocrine Connections, Jan 2024. URL: https://doi.org/10.1530/ec-23-0500, doi:10.1530/ec-23-0500. This article has 3 citations and is from a peer-reviewed journal.

7. (vissers2020denovovariants pages 1-2): Lisenka E.L.M. Vissers, Sreehari Kalvakuri, Elke de Boer, Sinje Geuer, Machteld Oud, Inge van Outersterp, Michael Kwint, Melde Witmond, Simone Kersten, Daniel L. Polla, Dilys Weijers, Amber Begtrup, Kirsty McWalter, Anna Ruiz, Elisabeth Gabau, Jenny E.V. Morton, Christopher Griffith, Karin Weiss, Candace Gamble, James Bartley, Hilary J. Vernon, Kendra Brunet, Claudia Ruivenkamp, Sarina G. Kant, Paul Kruszka, Austin Larson, Alexandra Afenjar, Thierry Billette de Villemeur, Kimberly Nugent, F. Lucy Raymond, Hanka Venselaar, Florence Demurger, Claudia Soler-Alfonso, Dong Li, Elizabeth Bhoj, Ian Hayes, Nina Powell Hamilton, Ayesha Ahmad, Rachel Fisher, Myrthe van den Born, Marjolaine Willems, Arthur Sorlin, Julian Delanne, Sebastien Moutton, Philippe Christophe, Frederic Tran Mau-Them, Antonio Vitobello, Himanshu Goel, Lauren Massingham, Chanika Phornphutkul, Jennifer Schwab, Boris Keren, Perrine Charles, Maaike Vreeburg, Lenika De Simone, George Hoganson, Maria Iascone, Donatella Milani, Lucie Evenepoel, Nicole Revencu, D. Isum Ward, Kaitlyn Burns, Ian Krantz, Sarah E. Raible, Jill R. Murrell, Kathleen Wood, Megan T. Cho, Hans van Bokhoven, Maximilian Muenke, Tjitske Kleefstra, Rolf Bodmer, and Arjan P.M. de Brouwer. De novo variants in cnot1, a central component of the ccr4-not complex involved in gene expression and rna and protein stability, cause neurodevelopmental delay. The American Journal of Human Genetics, 107:164-172, Jul 2020. URL: https://doi.org/10.1016/j.ajhg.2020.05.017, doi:10.1016/j.ajhg.2020.05.017. This article has 62 citations.

8. (malta2023holoprosencephalyreviewof pages 9-11): Maísa Malta, Rowim AlMutiri, Christine Saint Martin, and Myriam Srour. Holoprosencephaly: review of embryology, clinical phenotypes, etiology and management. Children, 10:647, Mar 2023. URL: https://doi.org/10.3390/children10040647, doi:10.3390/children10040647. This article has 42 citations.

9. (malta2023holoprosencephalyreviewof pages 4-6): Maísa Malta, Rowim AlMutiri, Christine Saint Martin, and Myriam Srour. Holoprosencephaly: review of embryology, clinical phenotypes, etiology and management. Children, 10:647, Mar 2023. URL: https://doi.org/10.3390/children10040647, doi:10.3390/children10040647. This article has 42 citations.

## Artifacts

- [Edison artifact artifact-00](Holoprosencephaly_12_With_or_Without_Pancreatic_Agenesis-deep-research-falcon_artifacts/artifact-00.md)