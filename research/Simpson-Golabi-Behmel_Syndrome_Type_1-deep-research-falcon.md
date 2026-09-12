---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T16:52:47.629346'
end_time: '2026-09-01T17:01:28.210901'
duration_seconds: 520.58
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Simpson-Golabi-Behmel Syndrome Type 1
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 11
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Simpson-Golabi-Behmel_Syndrome_Type_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Simpson-Golabi-Behmel Syndrome Type 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Simpson-Golabi-Behmel Syndrome Type 1** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
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
- **Disease Name:** Simpson-Golabi-Behmel Syndrome Type 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Simpson-Golabi-Behmel Syndrome Type 1** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Simpson–Golabi–Behmel Syndrome Type 1: Disease Characteristics Report

## Executive summary

Simpson–Golabi–Behmel syndrome type 1 (SGBS1) is a congenital X-linked overgrowth and multiple-malformation syndrome caused primarily by germline loss-of-function variants in **GPC3**, which encodes the cell-surface heparan-sulfate proteoglycan glypican-3. Its major manifestations are prenatal and postnatal overgrowth, macrocephaly, organomegaly, characteristic craniofacial and skeletal findings, congenital cardiac/genitourinary/gastrointestinal abnormalities, variable neurodevelopmental impairment, and predisposition to embryonal tumors—especially Wilms tumor and hepatic tumors. Expression is usually greatest in hemizygous males, but symptomatic heterozygous females occur. Prevalence and incidence remain unknown, reflecting extreme rarity, variable expression, early lethality, and probable underdiagnosis. There is no disease-modifying treatment; current practice comprises molecular diagnosis, multidisciplinary supportive care, tumor and cardiac surveillance, and reproductive counseling. (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2019cugcforsimpsongolabibehmel pages 4-5, vuillaume2019cugcforsimpsongolabibehmel pages 1-2)

The principal quantitative genetic dataset available in the retrieved literature comprised **86 distinct GPC3 variants in 120 unrelated families and 152 affected males**. Large deletions represented 34.9%, frameshift variants 24.4%, nonsense variants 16.3%, missense variants 8.1%, large duplications 8.1%, splice-site variants 4.7%, translocations 2.3%, and in-frame indels 1.2%. (vuillaume2019cugcforsimpsongolabibehmel pages 1-2)

| Domain | Key facts | Suggested ontology terms | Key evidence |
|---|---|---|---|
| Identifiers / synonyms | Simpson-Golabi-Behmel syndrome type 1 (SGBS1) is a rare congenital overgrowth-malformation syndrome caused by GPC3 loss of function; OMIM disease identifier **#312870**; Open Targets disease identifier **MONDO:0020602**. Common names/synonyms in the literature: Simpson-Golabi-Behmel syndrome, SGBS, SGBS1. Evidence is largely from aggregated disease-level reviews/guidelines plus published case reports/series, not EHR cohorts. | MONDO:0020602 | (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2019cugcforsimpsongolabibehmel pages 1-2, OpenTargets Search: Simpson-Golabi-Behmel syndrome type 1-GPC3) |
| Causal gene / inheritance | Primary causal gene: **GPC3** (glypican 3), Xq26.3; OMIM gene **#300037**; Open Targets target **ENSG00000147257**. Inheritance is **X-linked**; males typically show full penetrance, while female carriers are often asymptomatic or mildly affected, though clinically significant affected females have been reported. | HGNC:4451; SO:0001483 loss_of_function_variant | (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2019cugcforsimpsongolabibehmel pages 1-2, OpenTargets Search: Simpson-Golabi-Behmel syndrome type 1-GPC3) |
| Variant spectrum | Review data identified **86 distinct GPC3 variants** in **120 unrelated families** involving **152 male patients**. Reported classes: **large deletions 34.9%**, **frameshift 24.4%**, **nonsense 16.3%**, **missense 8.1%**, **large duplications 8.1%**, **splice-site 4.7%**, **translocations 2.3%**, **in-frame indels 1.2%**. Variants are predominantly germline **loss-of-function** defects; only **18%** were reported as de novo in the mutation update. | SO:0000159 deletion; SO:0001589 frameshift_variant; SO:0001587 stop_gained; SO:0001629 splice_site_variant; SO:1000032 chromosomal_duplication | (vuillaume2019cugcforsimpsongolabibehmel pages 1-2, vuillaume2018mutationupdatefor pages 13-14) |
| Hallmark phenotypes | Core phenotype includes **fetal macrosomia/pre- and postnatal overgrowth**, **macrocephaly**, **organomegaly**, **coarse/distinctive facies**, **extremity abnormalities**, **supernumerary nipples**, and variable **cardiac, skeletal, gastrointestinal, genitourinary malformations**; **learning difficulties/intellectual disability** occur variably. Typical presentation is **from birth/congenital**. Suggested HPO terms: overgrowth **HP:0001548**, fetal macrosomia **HP:0001524**, macrocephaly **HP:0000256**, organomegaly **HP:0002742**, coarse facial features **HP:0000280**, supernumerary nipple **HP:0100807**, congenital heart defect **HP:0001627**, skeletal abnormality **HP:0000924**, cryptorchidism **HP:0000028**, intellectual disability **HP:0001249**. | HPO terms listed in cell | (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2019cugcforsimpsongolabibehmel pages 1-2, vuillaume2018mutationupdatefor pages 1-2) |
| Tumor predisposition | Documented tumor predisposition is an established component of SGBS1, with emphasis on **Wilms tumor** and **liver tumors/hepatoblastoma**; **gonadoblastoma** surveillance is also recommended in guidance. Exact tumor incidence was not available in the gathered evidence set, so risk should be described qualitatively rather than numerically here. | HP:0002669 Neoplasm; NCIT:C3434 Wilms Tumor; NCIT:C3728 Hepatoblastoma; NCIT:C3088 Gonadoblastoma | (vuillaume2019cugcforsimpsongolabibehmel pages 4-5, vuillaume2018mutationupdatefor pages 1-2, vuillaume2018mutationupdatefor pages 13-14, vuillaume2019cugcforsimpsongolabibehmel pages 1-2) |
| Diagnosis | Diagnosis combines clinical recognition with molecular confirmation. Reported methods include **PCR/direct sequencing (Sanger)** and **MLPA** on peripheral-blood genomic DNA; analytical sensitivity/specificity for coding-exon and flanking-intron variant detection was described as **nearly 100%** in the clinical utility guideline. Prenatal diagnosis has been reported using ultrasound findings plus molecular testing, including detection of partial **GPC3** deletions. | NCIT:C16444 Sanger Sequencing; NCIT:C111298 Multiplex Ligation-dependent Probe Amplification | (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2019cugcforsimpsongolabibehmel pages 1-2, vuillaume2019cugcforsimpsongolabibehmel pages 5-6) |
| Management / surveillance | Management is **multidisciplinary and largely symptomatic**: neonatal hypoglycemia treatment, surgery for congenital malformations, specialist management for arrhythmia/conduction disease, and developmental supports (e.g., speech/learning services). Guidance recommends screening in affected males and symptomatic carrier females for **Wilms tumors, liver tumors, and gonadoblastoma**, plus **regular cardiac follow-up**. Prenatal molecular diagnosis can be offered to at-risk pregnancies of known female carriers. | NCIT:C51932 Supportive Care; NCIT:C17428 Surgical Procedure; NCIT:C15709 Genetic Counseling; NCIT:C47891 Ultrasound | (vuillaume2019cugcforsimpsongolabibehmel pages 4-5, vuillaume2019cugcforsimpsongolabibehmel pages 5-6) |
| Mechanism | Causal chain: **GPC3 loss-of-function** leads to defective cell-surface glypican regulation of morphogen signaling, which leads to dysregulated developmental growth control and organ patterning, resulting in overgrowth, congenital malformations, and tumor susceptibility. The gathered evidence supports dysregulation of **WNT**, **Hedgehog**, **FGF**, and **BMP** pathways; Hedgehog hyperactivation with elevated Sonic/Indian Hedgehog proteins has been reported in GPC3-null models. Some downstream links to specific human phenotypes remain inferred from model systems rather than directly demonstrated in patient tissues. | GO:0060070 canonical Wnt signaling pathway; GO:0007224 smoothened signaling pathway; GO:0008543 fibroblast growth factor receptor signaling pathway; GO:0030509 BMP signaling pathway | (vuillaume2018mutationupdatefor pages 1-2, vuillaume2018mutationupdatefor pages 13-14) |
| Model organisms | **Gpc3-targeted/deletion mouse models** recapitulate major developmental features, including **developmental overgrowth**, **perinatal death**, **renal dysplasia**, **accessory spleens**, **impaired lung development**, **polydactyly**, and **placentomegaly**. These models support an upstream developmental-regulatory role for GPC3 and are useful for mechanism studies, but they do not fully quantify human neurodevelopmental or tumor outcomes. | NCBITaxon:10090; CL/GO not disease-specific here | (vuillaume2018mutationupdatefor pages 13-14) |
| Epidemiology / prognosis | **Prevalence is unknown** and the disorder is likely **underdiagnosed**. Prognosis is **generally favorable in many cases**, but can be **life-threatening at birth or in infancy** because of major congenital malformations, especially severe diaphragmatic or other structural defects; otherwise many patients may have near-normal life expectancy, tempered by cardiac and tumor risks and by variable neurodevelopmental burden. | Orphan disease epidemiology not firmly established in gathered evidence | (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2019cugcforsimpsongolabibehmel pages 4-5, vuillaume2019cugcforsimpsongolabibehmel pages 1-2) |
| Recent developments / evidence gaps | 2021-2023 literature expanded **prenatal diagnosis**, **familial female expression**, and unusual presentations (e.g., disorders of sex development), while 2024 search results indicate continuing phenotype-spectrum work. No **SGBS1-specific disease-modifying therapy** or **interventional trial** was identified in the gathered evidence. Important gaps remain in **robust prevalence/incidence**, **tumor-risk quantification**, **standardized surveillance intervals/ages**, **natural-history cohorts**, and **omics-based biomarkers**. Oncology trials targeting **GPC3** in cancer should **not** be interpreted as treatments for germline GPC3 deficiency. | NCIT:C16084 Clinical Trial; NCIT:C15220 Biomarker | (vuillaume2019cugcforsimpsongolabibehmel pages 4-5, OpenTargets Search: Simpson-Golabi-Behmel syndrome type 1-GPC3, vuillaume2018mutationupdatefor pages 13-14) |


*Table: This table condenses the highest-yield disease knowledge-base fields for Simpson-Golabi-Behmel syndrome type 1, including identifiers, genetics, phenotype, mechanism, management, and evidence gaps. It is aligned to the gathered evidence and highlights the key quantitative variant data needed for structured curation.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Simpson–Golabi–Behmel syndrome type 1
* **Common synonyms:** Simpson–Golabi–Behmel syndrome; SGBS; SGBS1; Simpson dysmorphia syndrome; Golabi–Rosen syndrome; bulldog syndrome. The last three are historical terms and are less suitable as preferred labels.
* **MONDO:** **MONDO:0020602**
* **OMIM phenotype:** **312870**
* **Causal-gene OMIM entry:** **GPC3, 300037**
* **Gene:** **GPC3**, glypican 3; Ensembl **ENSG00000147257**; chromosome Xq26.3. Open Targets identifies GPC3 as the sole associated target and assigns a target–disease association score of 0.767, driven predominantly by human genetic evidence. (OpenTargets Search: Simpson-Golabi-Behmel syndrome type 1-GPC3)
* **Orphanet:** SGBS is represented as a rare genetic overgrowth syndrome, although an exact Orpha identifier was not verified in the retrieved full-text evidence and should be validated directly before database import.
* **ICD:** No highly specific ICD-10-CM code was verified. It is generally coded under congenital malformation or overgrowth-syndrome categories. ICD-11 mapping should likewise be verified against the current release rather than inferred.
* **MeSH:** No disease-specific MeSH descriptor was established in the retrieved evidence; indexing may use broader headings such as congenital abnormalities, overgrowth, or X-linked genetic diseases.

The evidence base is **aggregated disease-level knowledge** derived from published families, case series, mutation compilations, clinical-utility guidance, and model systems—not a representative EHR cohort. Consequently, phenotype frequencies are vulnerable to ascertainment and publication bias. The 2019 clinical-utility guideline describes presentation as typically evident from birth. (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2019cugcforsimpsongolabibehmel pages 1-2)

## 2. Etiology, risk factors, protective factors, and environment

### Causal factor

The primary cause is a **germline loss-of-function alteration of GPC3**. Hemizygous pathogenic variants cause the classical phenotype in males. Most variants truncate the protein or delete one or more exons; pathogenic structural rearrangements also occur. The reviewed gene contains eight exons and produces an approximately 2.3-kb transcript. (vuillaume2019cugcforsimpsongolabibehmel pages 1-2, vuillaume2018mutationupdatefor pages 1-2)

### Genetic risk

A pathogenic familial GPC3 allele is the principal risk factor. Under X-linked transmission, a heterozygous mother has, for each pregnancy, a 50% probability of transmitting the altered allele; sons who inherit it are generally affected, while daughters who inherit it are heterozygous and may be asymptomatic or variably affected. Male-to-male transmission does not occur. The mutation update found only **18% of reported variants to be de novo**, indicating that familial transmission is important, although this proportion is subject to referral bias. (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2018mutationupdatefor pages 13-14)

Female expression is plausibly influenced by skewed X-chromosome inactivation and variant/rearrangement context, but no validated modifier gene or clinically actionable modifier allele was established in the retrieved evidence. “Complete penetrance in males” is reported in the clinical-utility guideline; expressivity is nevertheless markedly variable. (vuillaume2019cugcforsimpsongolabibehmel pages 2-4)

### Environmental, infectious, and lifestyle factors

No toxin, infection, diet, smoking exposure, occupation, or lifestyle factor is established as a cause of SGBS1. Maternal or postnatal environment may alter general outcomes of congenital heart disease, hypoglycemia, respiratory compromise, or cancer, but these are nonspecific modifiers rather than etiologic factors. No replicated gene–environment interaction or protective environmental factor has been demonstrated.

### Protective factors

No genetic protective variant, dietary intervention, medication, or exposure is known to prevent expression after inheritance of a pathogenic GPC3 variant. Early recognition and surveillance are **risk-mitigating clinical measures**, not biological protection against disease onset.

## 3. Phenotypes

SGBS1 begins during fetal development. Severity ranges from mild dysmorphism and learning difficulty to lethal multisystem malformations. Reliable percentages for most individual manifestations were not recoverable from the available evidence; qualitative frequencies are therefore preferable to invented precision. Core features compiled across the mutation review and clinical guideline include the following. (vuillaume2019cugcforsimpsongolabibehmel pages 1-2, vuillaume2018mutationupdatefor pages 1-2)

* **Prenatal/postnatal overgrowth:** congenital physical sign; often fetal macrosomia followed by childhood overgrowth; variable persistence. Suggested HPO: **HP:0001524 Fetal macrosomia**, **HP:0001548 Overgrowth**.
* **Macrocephaly:** congenital or early-childhood sign, usually stable relative to growth. **HP:0000256**.
* **Macroglossia:** congenital physical manifestation that can impair feeding or airway function. **HP:0000158**.
* **Organomegaly/visceromegaly:** congenital sign involving liver, kidney, spleen, or other viscera. **HP:0003270 Organomegaly**.
* **Characteristic/coarse facies:** broad or coarse face, large mouth, broad nose, and related dysmorphism; usually recognizable from infancy. **HP:0000280 Coarse facial features**.
* **Supernumerary nipples:** congenital, generally stable and medically minor. **HP:0002558**.
* **Skeletal/limb abnormalities:** broad hands, short or broad distal phalanges, syndactyly or polydactyly, rib/vertebral abnormalities, and pectus deformity; congenital and generally nonprogressive. Suggested terms: **HP:0010442 Polydactyly**, **HP:0001159 Syndactyly**, **HP:0000767 Pectus excavatum**, **HP:0000924 Abnormality of the skeletal system**.
* **Congenital heart disease and electrical disease:** structural lesions, cardiomyopathy, conduction abnormalities, or arrhythmias may occur. Severity ranges from incidental to life-threatening. **HP:0001627**, **HP:0011675 Arrhythmia**, **HP:0001638 Cardiomyopathy**. Regular cardiac follow-up is recommended. (vuillaume2019cugcforsimpsongolabibehmel pages 4-5)
* **Diaphragmatic hernia and pulmonary hypoplasia:** uncommon but major determinants of neonatal mortality. **HP:0000776**, **HP:0002089**. The clinical guideline identifies congenital malformations, especially diaphragmatic hernia, as causes of early life-threatening disease. (vuillaume2019cugcforsimpsongolabibehmel pages 4-5)
* **Genitourinary abnormalities:** cryptorchidism, hypospadias, renal anomalies, and occasionally more extensive disorders of sex development. **HP:0000028**, **HP:0000047**, **HP:0000077**.
* **Gastrointestinal abnormalities:** congenital structural defects, including anorectal anomalies, may occur. **HP:0002027 Abnormality of the gastrointestinal tract**.
* **Neonatal hypoglycemia:** laboratory abnormality requiring prompt treatment. **HP:0001943**. (vuillaume2019cugcforsimpsongolabibehmel pages 4-5)
* **Developmental delay, learning difficulty, or intellectual disability:** variable, usually mild-to-moderate when present; may impair education, communication, independence, and adult employment. **HP:0001263**, **HP:0001328**, **HP:0001249**. (vuillaume2019cugcforsimpsongolabibehmel pages 4-5)
* **Embryonal tumors:** primarily Wilms tumor and liver tumors; gonadoblastoma is also a surveillance concern. **HP:0002669 Neoplasm**. (vuillaume2019cugcforsimpsongolabibehmel pages 4-5, vuillaume2018mutationupdatefor pages 1-2)

No validated SGBS1-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life study was identified. Quality-of-life burden is therefore inferred from congenital surgery, cardiac disease, developmental disability, cancer surveillance, and family reproductive burden rather than measured with standardized instruments.

## 4. Genetic and molecular information

**GPC3** encodes an approximately 70-kDa glycosylphosphatidylinositol-anchored heparan-sulfate proteoglycan located on the outer plasma membrane. The disease mechanism is predominantly **loss of function**, not gain of function or dominant negativity. Disease-associated changes include whole/partial-gene deletions, exon-level deletions or duplications, frameshift, nonsense, canonical splice, missense, in-frame indel, and chromosomal rearrangement variants. (vuillaume2018mutationupdatefor pages 1-2, vuillaume2019cugcforsimpsongolabibehmel pages 1-2)

The observed distribution—34.9% large deletions, 24.4% frameshift, and 16.3% nonsense—strongly supports haploinsufficiency/absence of functional protein as the central mechanism. The 86 reported variants span the coding region and include complex rearrangements. (vuillaume2018mutationupdatefor pages 1-2, vuillaume2019cugcforsimpsongolabibehmel pages 1-2)

Variants are constitutional/germline. A tumor arising in an affected person can acquire additional somatic alterations, but a somatic GPC3 variant alone is not equivalent to inherited SGBS1. Pathogenic alleles are expected to be absent or extremely rare from reference populations; however, exact gnomAD allele frequencies must be checked per variant. No single recurrent founder allele or robust population-specific carrier frequency was established.

Large Xq26 rearrangements may encompass neighboring genes, potentially producing a contiguous-gene phenotype. Copy-number analysis is consequently essential. No reproducible GPC3-associated DNA-methylation “episignature,” histone abnormality, or clinically validated epigenetic diagnostic test was found. Likewise, no established human modifier gene explains inter- or intrafamilial variation.

## 5. Environmental information

SGBS1 is not an environmentally acquired, infectious, occupational, or lifestyle-mediated disease. There is no zoonotic, transmissible, or exposure-related component. Standard avoidance of tobacco, alcohol, radiation, and toxins during pregnancy remains general prenatal-health advice but is not specific prevention for GPC3-associated disease.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A germline hemizygous **GPC3 loss-of-function variant** leads to absent or deficient functional glypican-3 at the external plasma membrane.
2. Loss of this heparan-sulfate co-receptor leads to abnormal extracellular presentation, sequestration, or receptor engagement of developmental morphogens.
3. This results in dysregulated **Hedgehog, WNT, FGF, and BMP signaling**; Hedgehog hyperactivation with increased Sonic and Indian Hedgehog proteins is demonstrated in Gpc3-null models, whereas the exact direction and magnitude of each pathway in every human tissue remain context-dependent. (vuillaume2018mutationupdatefor pages 1-2, vuillaume2018mutationupdatefor pages 13-14)
4. Dysregulated morphogen signaling leads to abnormal control of proliferation, apoptosis, polarity, differentiation, and organ patterning during embryogenesis.
5. Excess developmental growth and disturbed patterning result in fetal/postnatal overgrowth, macrocephaly, visceromegaly, skeletal/limb abnormalities, and cardiac, renal, pulmonary, gastrointestinal, and genital malformations.
6. **Branch:** severe structural defects lead to respiratory or cardiac compromise and can result in perinatal death.
7. **Branch:** disturbed developmental growth restraint is inferred to increase susceptibility to embryonal neoplasia, resulting particularly in Wilms tumor and hepatic tumors; the complete tumor-initiating sequence in human SGBS1 tissues remains incompletely demonstrated.
8. Altered nervous-system development is inferred to contribute to variable developmental delay and learning disability.

Upstream events are GPC3 deficiency and morphogen dysregulation; downstream events are altered cellular behavior, malformed organs, overgrowth, and tumor susceptibility. Appropriate GO annotations include **GO:0007224 smoothened signaling pathway**, **GO:0060070 canonical Wnt signaling pathway**, **GO:0008543 fibroblast growth factor receptor signaling pathway**, **GO:0030509 BMP signaling pathway**, **GO:0008283 cell population proliferation**, **GO:0048513 animal organ development**, and **GO:0007275 multicellular organism development**.

Relevant cell classes are broad rather than a single targeted lineage: embryonic mesenchymal cells (**CL:0000134 mesenchymal cell**), chondrocytes (**CL:0000138**), cardiomyocytes (**CL:0000746**), renal epithelial/nephron progenitor lineages, hepatoblasts, pulmonary epithelial cells, placental trophoblasts, and neural progenitors. These cell assignments are biologically plausible and supported principally by affected-organ and mouse-model phenotypes, not by a definitive human single-cell atlas.

No consistent SGBS1 metabolomic, lipidomic, proteomic, spatial-transcriptomic, or patient single-cell signature has been clinically validated. No SGBS1-specific CRISPR screen, organoid diagnostic assay, or multi-omics classifier was identified. These remain research opportunities rather than current applications.

## 7. Anatomical structures affected

Primary systems include:

* **Whole-body growth axis and placenta:** placentomegaly and fetal overgrowth; UBERON suggestions **UBERON:0001987 placenta**, **UBERON:0000468 multicellular organism**.
* **Craniofacial complex and tongue:** **UBERON:0007811 cranium**, **UBERON:0001723 tongue**.
* **Skeleton and limbs:** axial skeleton, ribs, vertebrae, hands, feet, digits; **UBERON:0004288 skeleton of hand**, **UBERON:0001464 skeletal system**.
* **Heart:** structural myocardium and cardiac conduction system; **UBERON:0000948 heart**.
* **Kidneys and urinary tract:** **UBERON:0002113 kidney**.
* **Liver and abdominal viscera:** **UBERON:0002107 liver**.
* **Lungs and diaphragm:** **UBERON:0002048 lung**, **UBERON:0001103 diaphragm**.
* **Gastrointestinal tract:** **UBERON:0005409 alimentary part of gastrointestinal system**.
* **Testes and external genitalia:** **UBERON:0000473 testis**.
* **Central nervous system:** developmental involvement underlying variable cognition; **UBERON:0000955 brain**.

At the subcellular level, the primary compartment is the **external side of the plasma membrane/cell surface**, where GPI-anchored glypican-3 regulates extracellular morphogens. Suggested GO Cellular Component annotations are **GO:0009986 cell surface**, **GO:0005886 plasma membrane**, and **GO:0031225 anchored component of membrane**. There is no characteristic lateralization; anomalies may be bilateral, unilateral, or asymmetric according to organ and individual.

## 8. Temporal development

Onset is prenatal, with fetal macrosomia, enlarged organs, increased nuchal thickness, polyhydramnios, or structural malformations sometimes detectable by ultrasound. Ultrasound findings are not pathognomonic, and many diagnoses are made postnatally. Clinically recognizable overgrowth and dysmorphism are usually present at birth. (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2019cugcforsimpsongolabibehmel pages 1-2)

There is no accepted formal staging system. A practical course is:

1. **Prenatal/perinatal phase:** overgrowth and congenital malformations; highest risk from diaphragmatic hernia, pulmonary hypoplasia, severe heart disease, and hypoglycemia.
2. **Infancy/childhood:** surgical treatment of malformations, developmental assessment, growth monitoring, and intensive embryonal-tumor surveillance.
3. **Later childhood/adolescence:** learning, speech, orthopedic, cardiac, and psychosocial needs; some childhood tumor risks decline with age.
4. **Adulthood:** congenital traits persist; available natural-history data are sparse, but many less severely affected patients survive with near-normal life expectancy. Cardiac and individual tumor-related follow-up remains clinically relevant. (vuillaume2019cugcforsimpsongolabibehmel pages 4-5)

The condition is lifelong rather than episodic or remitting. Structural anomalies do not spontaneously remit, although treated hypoglycemia or surgically corrected lesions can resolve. The prenatal period and first years of life are the most important intervention windows.

## 9. Inheritance and population

Inheritance is **X-linked**, conventionally described as X-linked recessive, although clinically affected heterozygous females demonstrate that the label does not imply absolute female nonpenetrance. Male penetrance is reported as complete, while severity is highly variable. Female carriers are usually asymptomatic or mildly affected. (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2019cugcforsimpsongolabibehmel pages 1-2)

No genetic anticipation is known. Maternal germline mosaicism is biologically possible and should be considered after an apparently de novo result, although its frequency is unknown. Consanguinity is not a major determinant of this X-linked condition. No well-established founder effect, ethnic enrichment, regional endemicity, or reliable carrier frequency has been demonstrated.

Prevalence and incidence are unknown. The literature review identified only 152 affected males across 120 unrelated families, illustrating rarity but not population prevalence. SGBS1 occurs across geographic and ancestral groups. The observed sex ratio is strongly male-biased for clinically recognized classical disease, but this is not evidence that females cannot be affected. (vuillaume2019cugcforsimpsongolabibehmel pages 1-2)

## 10. Diagnostics

### Clinical evaluation

Evaluation should document prenatal and postnatal growth, head circumference, dysmorphism, macroglossia, nipples, hands/feet, chest and spine, genitalia, developmental status, and family history. Initial investigations commonly include glucose assessment in neonates, echocardiography and ECG, abdominal/renal ultrasound, and targeted imaging or functional testing based on malformations. There is no diagnostic serum enzyme assay or validated circulating biomarker.

### Genetic-testing strategy

1. **GPC3 sequencing** should detect small coding and splice-region variants.
2. **Deletion/duplication analysis** by MLPA, exon-level array, or validated NGS copy-number analysis is essential because large deletions are the largest reported variant class.
3. If negative but suspicion remains high, use a comprehensive overgrowth/malformation panel or exome/genome sequencing with copy-number and structural-variant calling.
4. **Chromosomal microarray** is useful for larger Xq26 deletions/duplications and possible contiguous-gene syndromes.
5. **Genome sequencing** may resolve complex rearrangements or intronic/regulatory variants missed by conventional tests.
6. Confirm clinically important variants and test the mother and other at-risk relatives for segregation and counseling.

The clinical-utility guideline reports nearly 100% analytical sensitivity and specificity for detectable coding-exon/flanking-intron variants, but this must not be misread as 100% overall diagnostic yield because promoter, deep-intronic, mosaic, and difficult structural variants can escape a particular assay. PCR, Sanger sequencing, and MLPA were the established methods in the reviewed series. (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2019cugcforsimpsongolabibehmel pages 1-2)

Karyotyping and FISH are not preferred first-line tests but may characterize visible or targeted rearrangements. Mitochondrial-DNA and repeat-expansion testing are not relevant. RNA sequencing may help resolve a suspected splice variant, but it is not routine. There is no established diagnostic proteomic, metabolomic, epigenomic, or liquid-biopsy assay.

### Differential diagnosis

The principal differential is **Beckwith–Wiedemann spectrum**, which shares macrosomia, macroglossia, visceromegaly, neonatal hypoglycemia, and embryonal tumors. Distinguishing features include the X-linked pedigree and GPC3 variant in SGBS1 versus 11p15 imprinting abnormalities or CDKN1C variants in Beckwith–Wiedemann spectrum. Other considerations include Perlman syndrome, Sotos syndrome, Weaver syndrome, Malan syndrome, PI3K-AKT-related overgrowth, and nonsyndromic familial tall stature. The clinical guideline explicitly identifies Beckwith–Wiedemann syndrome as the major differential. (vuillaume2019cugcforsimpsongolabibehmel pages 2-4)

There is no population newborn screen. Appropriate screening is phenotype-triggered testing and cascade testing in an identified family.

## 11. Outcome and prognosis

Prognosis is heterogeneous. Severe congenital diaphragmatic, pulmonary, cardiac, or other malformations can cause fetal, neonatal, or infant death. In survivors without severe malformations, prognosis is often relatively favorable and life expectancy may be normal, although cardiac complications, tumors, developmental disability, and repeated procedures create substantial morbidity. (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2019cugcforsimpsongolabibehmel pages 4-5)

No reliable 5-year or 10-year survival estimate, disease-specific mortality rate, or validated prognostic calculator exists. Important adverse prognostic factors are severe congenital malformations, respiratory compromise, major heart disease or arrhythmia, malignant tumor development, and more substantial neurodevelopmental impairment. No molecular prognostic biomarker beyond broad genotype/structural-variant context has been validated.

Recovery from the underlying genetic syndrome is not expected. Individual complications—hypoglycemia, hernia, cryptorchidism, congenital cardiac lesions, orthopedic problems, or cancer—may be successfully treated. No standardized long-term disability or quality-of-life dataset was identified.

## 12. Treatment and real-world implementation

There is **no approved etiologic pharmacotherapy, gene therapy, RNA therapy, cell therapy, or GPC3-replacement treatment**. Care is individualized and multidisciplinary. (vuillaume2019cugcforsimpsongolabibehmel pages 4-5)

* Treat neonatal hypoglycemia promptly with glucose-based neonatal protocols. Suggested NCIt concepts: **Supportive Care**, **Glucose Administration**.
* Stabilize airway and respiration; repair diaphragmatic hernia and other structural defects when indicated. NCIt: **Surgical Procedure**.
* Manage congenital heart disease, cardiomyopathy, conduction disease, and arrhythmia according to pediatric cardiology standards; maintain longitudinal ECG/echocardiographic follow-up. (vuillaume2019cugcforsimpsongolabibehmel pages 4-5)
* Correct cryptorchidism, hypospadias, gastrointestinal anomalies, skeletal deformity, and feeding/airway problems when clinically indicated.
* Provide physical, occupational, speech-language, educational, and neuropsychological support. Moderate or mild psychomotor delay and learning difficulty may remain functionally important in adulthood. (vuillaume2019cugcforsimpsongolabibehmel pages 4-5)
* Coordinate tumor surveillance and promptly refer suspicious lesions to pediatric oncology.

Surveillance for **Wilms tumor, liver tumors, and gonadoblastoma** is recommended by the clinical-utility guidance, including affected males and symptomatic females. Exact ages and intervals were not supplied in the retrieved guideline excerpt; therefore, local overgrowth-syndrome protocols and genetics/oncology consultation should determine abdominal/renal ultrasound and alpha-fetoprotein schedules rather than relying on an uncited universal schedule. (vuillaume2019cugcforsimpsongolabibehmel pages 4-5)

No SGBS1-directed interventional clinical trial was identified. Multiple trials found by a GPC3 search concern **GPC3-expressing cancers** and use antibodies, imaging agents, CAR-T, or CAR-NK products. These aim to attack tumor cells expressing GPC3 and are not treatments for constitutional GPC3 deficiency; extrapolation to SGBS1 would be mechanistically inappropriate.

## 13. Prevention

Primary prevention through lifestyle modification or vaccination is impossible because SGBS1 is genetic. Effective reproductive-risk reduction requires genetic counseling, identification of the familial variant, and informed use of prenatal diagnosis or preimplantation genetic testing. Prenatal molecular diagnosis can be offered to known carriers. (vuillaume2019cugcforsimpsongolabibehmel pages 4-5, vuillaume2019cugcforsimpsongolabibehmel pages 5-6)

Secondary prevention consists of early molecular diagnosis, cascade testing, prenatal ultrasound in at-risk pregnancies, neonatal glucose and cardiopulmonary assessment, developmental screening, and tumor surveillance. Tertiary prevention comprises cardiac follow-up, timely surgery, rehabilitation, educational intervention, and surveillance intended to detect treatable tumors before symptoms or metastasis. There is no vaccine, chemoprophylaxis, or disease-specific public-health environmental intervention.

## 14. Other species and natural disease

No naturally occurring veterinary syndrome definitively equivalent to human SGBS1 was established in the retrieved literature. Accordingly, there is no recognized breed predisposition, veterinary transmission concern, or zoonotic potential.

GPC3 orthologs are evolutionarily conserved across vertebrates. Relevant experimental species include **Mus musculus** (NCBI Taxon **10090**) and potentially zebrafish and other developmental models, but naturally occurring disease should be distinguished from engineered loss-of-function models.

## 15. Model organisms

Targeted **Gpc3-null mice** reproduce important elements of human SGBS1: developmental overgrowth, placentomegaly, renal dysplasia, accessory spleens, abnormal lung development, polydactyly, and perinatal death. These findings provide in-vivo evidence that GPC3 is an upstream regulator of embryonic growth and patterning and support Hedgehog-pathway dysregulation. (vuillaume2018mutationupdatefor pages 13-14)

Model limitations are substantial: murine lethality and anomaly frequencies do not precisely mirror human survival or expressivity; cognition and human educational outcomes are difficult to model; and the model does not establish quantitative human tumor risk. Cellular SGBS-derived preadipocyte lines are widely used in adipogenesis research, but their utility as a complete disease model is limited because an immortalized or selected cell line cannot represent multisystem embryogenesis.

## Recent developments, 2023–2024, and evidence gaps

The recent literature has emphasized broader ascertainment rather than a new therapy: prenatal copy-number diagnoses, affected females, intrafamilial variability, atypical presentations, and adult diagnoses that can mimic acromegaly. A 2024 phenotype-spectrum and tumor-risk review and a 2024 disease review were identified by the search, but their full text was unavailable to the evidence extractor; numerical claims from those papers are therefore not reproduced without verification. This limitation is important because older tumor estimates are based on small, publication-biased series.

Priority research needs are: prospective international natural-history registries; genotype- and sex-stratified penetrance estimates; standardized tumor incidence and surveillance endpoints; systematic female-carrier cohorts; long-term adult cardiac and cancer outcomes; patient-reported quality-of-life measures; patient-derived organoids or iPSCs; tissue-resolved pathway profiling; and safe approaches to restoring appropriate GPC3 function during the relevant developmental window.

## Key sources and abstract-level quotations

1. **Vuillaume et al., “Mutation update for the GPC3 gene involved in Simpson-Golabi-Behmel syndrome and review of the literature.” Human Mutation. Published June 2018.** DOI/URL: https://doi.org/10.1002/humu.23428. The retrieved evidence reports 57 previously published plus 29 new variants, yielding 86 distinct variants across 120 families, and describes GPC3 as a 70-kDa proteoglycan regulating WNT, Hedgehog, FGF, and BMP signaling. (vuillaume2018mutationupdatefor pages 1-2, vuillaume2018mutationupdatefor pages 13-14)

2. **Vuillaume et al., “CUGC for Simpson-Golabi-Behmel syndrome (SGBS).” European Journal of Human Genetics. Published January 2019; 27:663–668.** DOI/URL: https://doi.org/10.1038/s41431-019-0339-z. This is the principal retrieved clinical-utility source for testing, differential diagnosis, management, penetrance, and prognosis. (vuillaume2019cugcforsimpsongolabibehmel pages 2-4, vuillaume2019cugcforsimpsongolabibehmel pages 4-5, vuillaume2019cugcforsimpsongolabibehmel pages 1-2)

3. **Foundational GPC3 discovery literature:** Open Targets links the SGBS1–GPC3 association to **PMID:8589713** and additional human genetic reports including **PMID:10814714, PMID:9950367, PMID:16158429, PMID:17850639, and PMID:18203194**. These database links provide primary-literature anchors for curation, although individual claims should be checked against each original article before assigning variant-level evidence. (OpenTargets Search: Simpson-Golabi-Behmel syndrome type 1-GPC3)

A directly verified quotation from a recent prenatal abstract is: **“Simpson–Golabi–Behmel syndrome type 1 (SGBS1) is a rare X-linked recessive disorder characterized by pre- and postnatal overgrowth and a broad spectrum of anomalies including craniofacial dysmorphism, heart defects, renal, and genital anomalies.”** Liu et al., *Molecular Genetics & Genomic Medicine*, published July 2021, DOI: https://doi.org/10.1002/mgg3.1750. This quotation is consistent with the independently retrieved mutation and clinical-utility evidence. (vuillaume2019cugcforsimpsongolabibehmel pages 1-2, vuillaume2018mutationupdatefor pages 1-2)

### Evidence-quality note

Most clinical knowledge derives from case reports, small family series, and retrospective literature compilations. The genetic causation evidence is strong, but phenotype frequencies, female penetrance, tumor incidence, surveillance effectiveness, and adult prognosis remain low-certainty because population-based cohorts are absent. Assertions unsupported by the retrieved full text—particularly exact tumor percentages, universal surveillance intervals, and unverified ontology or ICD mappings—have deliberately been labeled uncertain rather than presented as established facts.

References

1. (vuillaume2019cugcforsimpsongolabibehmel pages 2-4): Marie-Laure Vuillaume, Marie-Pierre Moizard, Alessandra Baumer, Edouard Cottereau, Frédéric Brioude, Anita Rauch, and Annick Toutain. Cugc for simpson-golabi-behmel syndrome (sgbs). European Journal of Human Genetics, 27:663-668, Jan 2019. URL: https://doi.org/10.1038/s41431-019-0339-z, doi:10.1038/s41431-019-0339-z. This article has 11 citations and is from a domain leading peer-reviewed journal.

2. (vuillaume2019cugcforsimpsongolabibehmel pages 4-5): Marie-Laure Vuillaume, Marie-Pierre Moizard, Alessandra Baumer, Edouard Cottereau, Frédéric Brioude, Anita Rauch, and Annick Toutain. Cugc for simpson-golabi-behmel syndrome (sgbs). European Journal of Human Genetics, 27:663-668, Jan 2019. URL: https://doi.org/10.1038/s41431-019-0339-z, doi:10.1038/s41431-019-0339-z. This article has 11 citations and is from a domain leading peer-reviewed journal.

3. (vuillaume2019cugcforsimpsongolabibehmel pages 1-2): Marie-Laure Vuillaume, Marie-Pierre Moizard, Alessandra Baumer, Edouard Cottereau, Frédéric Brioude, Anita Rauch, and Annick Toutain. Cugc for simpson-golabi-behmel syndrome (sgbs). European Journal of Human Genetics, 27:663-668, Jan 2019. URL: https://doi.org/10.1038/s41431-019-0339-z, doi:10.1038/s41431-019-0339-z. This article has 11 citations and is from a domain leading peer-reviewed journal.

4. (OpenTargets Search: Simpson-Golabi-Behmel syndrome type 1-GPC3): Open Targets Query (Simpson-Golabi-Behmel syndrome type 1-GPC3, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (vuillaume2018mutationupdatefor pages 13-14): Marie-Laure Vuillaume, Marie-Pierre Moizard, Sylvie Rossignol, Edouard Cottereau, Sandrine Vonwill, Jean-Luc Alessandri, Tiffany Busa, Estelle Colin, Marion Gérard, Fabienne Giuliano, Laetitia Lambert, Mathilde Lefevre, Udhaya Kotecha, Sheela Nampoothiri, Irène Netchine, Martine Raynaud, Frédéric Brioude, and Annick Toutain. Mutation update for the gpc3 gene involved in simpson‐golabi‐behmel syndrome and review of the literature. Human Mutation, 39:790-805, Jun 2018. URL: https://doi.org/10.1002/humu.23428, doi:10.1002/humu.23428. This article has 42 citations and is from a domain leading peer-reviewed journal.

6. (vuillaume2018mutationupdatefor pages 1-2): Marie-Laure Vuillaume, Marie-Pierre Moizard, Sylvie Rossignol, Edouard Cottereau, Sandrine Vonwill, Jean-Luc Alessandri, Tiffany Busa, Estelle Colin, Marion Gérard, Fabienne Giuliano, Laetitia Lambert, Mathilde Lefevre, Udhaya Kotecha, Sheela Nampoothiri, Irène Netchine, Martine Raynaud, Frédéric Brioude, and Annick Toutain. Mutation update for the gpc3 gene involved in simpson‐golabi‐behmel syndrome and review of the literature. Human Mutation, 39:790-805, Jun 2018. URL: https://doi.org/10.1002/humu.23428, doi:10.1002/humu.23428. This article has 42 citations and is from a domain leading peer-reviewed journal.

7. (vuillaume2019cugcforsimpsongolabibehmel pages 5-6): Marie-Laure Vuillaume, Marie-Pierre Moizard, Alessandra Baumer, Edouard Cottereau, Frédéric Brioude, Anita Rauch, and Annick Toutain. Cugc for simpson-golabi-behmel syndrome (sgbs). European Journal of Human Genetics, 27:663-668, Jan 2019. URL: https://doi.org/10.1038/s41431-019-0339-z, doi:10.1038/s41431-019-0339-z. This article has 11 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Simpson-Golabi-Behmel_Syndrome_Type_1-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 74 |
| Resolved | 71 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 1 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001524` (2 mentions) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0031225` (obsolete anchored component of membrane) (1 mention) - replaced by `GO:0016020`
