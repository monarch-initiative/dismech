---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T17:02:54.423649'
end_time: '2026-07-31T17:14:59.989179'
duration_seconds: 725.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Diaphragmatic Hernia
  mondo_id: ''
  category: Congenital
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 47
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Congenital_Diaphragmatic_Hernia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Diaphragmatic Hernia
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Congenital Diaphragmatic Hernia** covering all of the
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
- **Disease Name:** Congenital Diaphragmatic Hernia
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Congenital Diaphragmatic Hernia** covering all of the
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


# Congenital Diaphragmatic Hernia: Disease-Characteristics Research Report

**Scope and evidence note.** This report prioritizes human clinical and genomic evidence from 2023–2024, supplemented by the authoritative 2022 *Nature Reviews Disease Primers* review and model-organism literature. The retrieval corpus supplied DOI URLs but not PubMed identifiers for most papers; therefore, DOI-linked citations are provided rather than inventing PMIDs. Ontology identifiers marked “suggested” should be validated against the current ontology release before database ingestion.

| domain | key quantitative finding | evidence type | source/year/DOI |
|---|---:|---|---|
| Epidemiology | Prevalence ~2.3 per 10,000 live births | Human clinical review | Rivas & Clugston 2024, Pediatr Res, doi:10.1038/s41390-023-02905-7 (rivas2024theetiologyof pages 1-2) |
| Genetics | Identifiable genetic cause in ~30–40% of cases; chromosomal defects ~10%; de novo variants 10–22% | Human genomic review | Rivas & Clugston 2024, doi:10.1038/s41390-023-02905-7; Liu & Yu 2024, doi:10.1136/wjps-2024-000884 (rivas2024theetiologyof pages 1-2) |
| Genetics | Common variants explain 19% heritability of susceptibility | Human GWAS/genome sequencing | Qiao et al. 2024, Am J Hum Genet, doi:10.1016/j.ajhg.2024.08.024 (qiao2024commonvariantsincrease pages 1-3, qiao2024commonvariantsincrease pages 15-16) |
| Genetics | De novo damaging variants account for ~25% population attributable risk | Human trio genomics | Qiao et al. 2024, doi:10.1016/j.ajhg.2024.08.024 (qiao2024commonvariantsincrease pages 15-16, qiao2024commonvariantsincrease pages 16-17) |
| Phenotype / outcome | Associated malformations in ~40% of patients, especially cardiovascular/urogenital | Human clinical review | Liu & Yu 2024, doi:10.1136/wjps-2024-000884 (liu2024roleofgenetics pages 1-2) |
| Phenotype / outcome | Mortality 20–30% in high-resource settings; >50% of survivors have long-term morbidity | Human clinical reviews | Rivas & Clugston 2024, doi:10.1038/s41390-023-02905-7; Zani et al. 2022, doi:10.1038/s41572-022-00362-w (rivas2024theetiologyof pages 1-2, zani2022congenitaldiaphragmatichernia pages 1-2) |
| Prenatal prognostic markers | Liver herniation: survival ~45% vs 74% without liver-up; ECMO need 80% vs 25% | Human prognostic review | Perveen et al. 2022, Front Pediatr, doi:10.3389/fped.2022.932463 (perveen2022cellularmolecularand pages 1-2) |
| Prenatal prognostic markers | O/E-TFLV >35%: survival 94% vs 56% when <35% | Human prognostic review | Perveen et al. 2022, doi:10.3389/fped.2022.932463 (perveen2022cellularmolecularand pages 1-2) |
| Fetal therapy | TOTAL severe left CDH: FETO survival 40% vs 15% expectant management | Human interventional trial summary/review | Zani et al. 2022, Nat Rev Dis Primers, doi:10.1038/s41572-022-00362-w (zani2022congenitaldiaphragmatichernia pages 8-9) |
| Model organisms | Nitrofen rat model induces CDH with pulmonary hypoplasia in ~70% | Animal teratogen model | Liu & Yu 2024, doi:10.1136/wjps-2024-000884 (liu2024roleofgenetics pages 3-4) |
| Model organisms | Conditional Wt1 deletion: CDH incidence ~80% and PPF deletion penetrance 80–90% | Genetic mouse model | Rivas & Clugston 2024, doi:10.1038/s41390-023-02905-7 (rivas2024theetiologyof pages 4-5) |


*Table: This table summarizes high-yield quantitative findings for congenital diaphragmatic hernia across epidemiology, genetics, prognosis, fetal therapy, and model systems. It is useful as a compact evidence backbone for a disease knowledge base entry.*

## 1. Disease information

### Definition and classification

Congenital diaphragmatic hernia (CDH) is a developmental defect in which incomplete formation or closure of the diaphragm permits abdominal viscera to enter the thorax. The resulting disease is not merely a mechanical hernia: disrupted fetal lung growth causes pulmonary hypoplasia, abnormal pulmonary vascular development and persistent pulmonary hypertension of the newborn (PPHN), often accompanied by cardiac dysfunction. A concise 2024 definition states that CDH is “characterized by failure of diaphragm closure during embryonic development, leading to pulmonary hypoplasia and pulmonary hypertension.” [Review; published August 2024; DOI: https://doi.org/10.1136/wjps-2024-000884] (liu2024roleofgenetics pages 1-2)

**Anatomic forms.** Bochdalek/posterolateral defects predominate. Recent reviews give somewhat different distributions because of classification and ascertainment differences: approximately 70–95% are Bochdalek defects and about 85% of these are left-sided; Morgagni/anterior defects account for approximately 3% in one modern morphologic classification, while eventration accounts for 2–3% and central tendon defects for 1–2%. Right-sided and bilateral defects are less common but often severe. (liu2024roleofgenetics pages 1-2, rivas2024theetiologyof pages 1-2)

### Key identifiers and synonyms

Suggested database mappings are:

- **MONDO:** congenital diaphragmatic hernia; commonly mapped as **MONDO:0005711**, but release-level verification is advised.
- **ICD-10-CM:** **Q79.0**, congenital diaphragmatic hernia.
- **ICD-11:** congenital diaphragmatic hernia under developmental anomalies of the respiratory system/diaphragm; verify the current extension code in the target ICD-11 release.
- **MeSH:** *Hernias, Diaphragmatic, Congenital*.
- **OMIM:** genetically heterogeneous; **DIH1/diaphragmatic hernia 1, OMIM 142340** is often used as an entry point, but CDH should not be represented as a single Mendelian disorder.
- **Orphanet:** congenital diaphragmatic hernia; verify the current ORPHA identifier against Orphanet before production ingestion.
- **Synonyms:** congenital diaphragmatic defect, congenital diaphragmatic hernia/defect, Bochdalek hernia, posterolateral diaphragmatic hernia, Morgagni hernia, anterior diaphragmatic hernia and congenital diaphragmatic eventration. Bochdalek and Morgagni designate anatomic subtypes, not exact synonyms for all CDH.

The evidence summarized here is **aggregated disease-level information** from cohorts, registries, reviews and trials, not individual EHR-derived patient data.

## 2. Etiology and risk/protective factors

CDH is etiologically heterogeneous and usually sporadic. Approximately 30–40% of patients have an identifiable chromosomal or single-gene contribution; chromosomal defects account for about 10%, while de novo coding variants account for roughly 10–22%. More than 70 syndromes and approximately 150 implicated gene variants have been reported. Complex CDH has a much higher genetic diagnostic yield than isolated disease. (rivas2024theetiologyof pages 1-2, liu2024roleofgenetics pages 1-2, liu2024roleofgenetics pages 2-3)

### Genetic risk

Established or strongly supported genes include **GATA4, GATA6, ZFPM2/FOG2, NR2F2/COUP-TFII, WT1, MYRF, LONP1, ALDH1A2, STRA6, CRABP1, FREM1, PIGN, KIF7, PBX1, EFNB1, FZD2, GPC3** and **SLIT3**. Relevant recurrent regions include **8p23.1** (including GATA4), **15q26** (including NR2F2), **11p13** (WT1/PAX6), and 17q regions involving FZD2. Disease-associated variants include de novo loss-of-function and missense SNVs, small indels, inherited dominant variants with incomplete penetrance, recessive/biallelic variants, and large deletions or other CNVs. Most clinically causal variants are germline; somatic mutation is not an established general mechanism. (schreiner2021geneticsofdiaphragmatic pages 2-3, liu2024roleofgenetics pages 12-12, perveen2022cellularmolecularand pages 7-7)

The major 2024 genomic development was a study of 1,469 affected individuals, including 1,064 parent-child trios and 6,133 ancestry-matched controls. It found 15 de novo candidate genes, including eight novel candidates, and two replicated common-variant loci: **rs55705711 at 3p14.3**, near **WNT5A** (OR 1.65; P=5.1×10⁻¹⁷), and **rs7777647 at 7q36.3**, near regulatory elements of **SHH** (OR 1.27; P=1.9×10⁻⁹). Common variants explained an estimated 19% of susceptibility heritability, whereas damaging de novo variants accounted for approximately 25% of population-attributable risk. This supports a liability model in which polygenic background and rare, large-effect variants act additively. [Human genome sequencing/GWAS; published November 2024; DOI: https://doi.org/10.1016/j.ajhg.2024.08.024] (qiao2024commonvariantsincrease pages 1-3, qiao2024commonvariantsincrease pages 15-16, qiao2024commonvariantsincrease pages 9-11)

Penetrance and expressivity are variable. Identical **GATA4** variants in monozygotic twins have been associated with CDH in only one twin, illustrating incomplete penetrance and likely modifier or environmental effects. No genetic anticipation or repeat-expansion mechanism is established. Germline mosaicism is theoretically relevant to recurrence after an apparently de novo variant, but robust CDH-specific frequency estimates are unavailable. Founder effects and carrier frequencies are not established for CDH overall because it is genetically heterogeneous. (schreiner2021geneticsofdiaphragmatic pages 2-3)

### Environmental and lifestyle associations

Reported maternal associations include age, smoking, alcohol exposure, pregestational diabetes and agricultural pesticide exposure. These are epidemiologic associations rather than proof of individual causation, and evidence outside retinoid biology remains limited. There is no infectious cause and CDH is not transmissible. (liu2024roleofgenetics pages 1-2)

The best-developed gene–environment hypothesis concerns **vitamin A/retinoic acid signaling**. Retinoic acid is synthesized from dietary vitamin A through retinaldehyde dehydrogenases, including **ALDH1A2/RALDH2**. Vitamin-A deficiency causes diaphragmatic defects in rodents; nitrofen inhibits RALDH2 and lowers fetal retinoic acid during a critical developmental window; supplementation reduces defect incidence or size in several models. Ethanol can perturb retinol metabolism, providing a plausible interaction between exposure and genetically reduced pathway reserve. Human dietary studies are supportive but do not justify high-dose vitamin-A prophylaxis, which itself can be teratogenic. (liu2024roleofgenetics pages 12-12, rivas2024theetiologyof pages 1-2, rivas2024theetiologyof pages 4-5)

No reproducible genetic “protective variant” is established. Adequate—not excessive—maternal nutrition and avoidance of known teratogens are prudent general measures, but no intervention has been proven to prevent sporadic CDH.

## 3. Phenotypes

| Phenotype | Type, onset and course | Frequency/severity and impact | Suggested HPO term |
|---|---|---|---|
| Diaphragmatic defect/visceral herniation | Congenital structural sign; stable anatomically until repaired | Defining feature; size ranges from small defect to near-total hemidiaphragm agenesis | Diaphragmatic hernia, **HP:0000776** |
| Pulmonary hypoplasia | Congenital developmental manifestation; severe and non-reversible at birth, with compensatory growth thereafter | Nearly universal in clinically important neonatal CDH; major mortality determinant | Pulmonary hypoplasia, **HP:0002089** |
| Neonatal respiratory distress/failure | Symptom/sign beginning immediately after birth in severe disease | Variable from mild oxygen need to refractory failure requiring ECLS | Neonatal respiratory distress; respiratory failure |
| PPHN | Cardiopulmonary sign, neonatal onset; fluctuating with transitional circulation | Major cause of death; in a 2024 genomic cohort, 45% had PH at one month | Pulmonary hypertension, **HP:0002092** |
| Cardiac dysfunction/hypoplasia | Prenatal or neonatal sign | Particularly left-ventricular hypoplasia/dysfunction in left CDH; worsens systemic perfusion | Abnormal cardiac morphology/function |
| Feeding difficulty, growth failure and GERD | Usually infancy/childhood; may be chronic | More than 10% require tube access; substantial nutritional and caregiver burden | Feeding difficulties, **HP:0011968**; gastroesophageal reflux, **HP:0002020**; failure to thrive |
| Chronic lung disease/recurrent infection | Childhood, chronic or episodic | Chronic lung disease in up to 50%; respiratory infections in 10–70% during year one | Chronic lung disease; recurrent respiratory infections |
| Neurodevelopmental, executive and behavioral impairment | Childhood; variable, often persistent | Risk rises after prolonged ventilation, ECLS or patch repair; autism/ADHD risks are elevated | Global developmental delay, **HP:0001263**; behavioral abnormality |
| Hearing impairment | Infancy/childhood, sometimes progressive | Associated with critical illness, ototoxic exposure and ECMO; exact pooled frequency varies | Sensorineural hearing impairment |
| Chest-wall deformity/scoliosis | Childhood/adolescence, progressive | Chest asymmetry >50%, scoliosis ~30%, pectus excavatum ~20% | Scoliosis, **HP:0002650**; pectus excavatum, **HP:0000767** |
| Recurrent hernia | Post-repair complication | May reach 50% by age three after large patch-repaired defects | Recurrent diaphragmatic hernia |

Associated malformations occur in approximately 40%, especially cardiovascular and urogenital anomalies; complex cases can also have gastrointestinal, CNS, craniofacial or skeletal abnormalities. In a 2024 genomic cohort, 37% had complex CDH; among these, cardiovascular anomalies occurred in 54%, neurodevelopmental sequelae in 25%, and gastrointestinal anomalies in 17%. (liu2024roleofgenetics pages 1-2, qiao2024commonvariantsincrease pages 6-7)

Quality-of-life impact extends beyond organ morbidity. More than half of survivors have complex long-term morbidity; 77% of surveyed families described the experience as very or extremely stressful, and parental post-traumatic stress symptoms are common. Exercise capacity, school performance, feeding, sleep, repeated admissions and chronic specialist care can all be affected. (zani2022congenitaldiaphragmatichernia pages 14-15, zani2022congenitaldiaphragmatichernia pages 1-2)

## 4. Genetic and molecular information

### Variant interpretation and testing implications

No single CDH gene accounts for more than approximately 1–3% of cases. Variant classification should therefore follow ACMG/AMP criteria using phenotype fit, inheritance, population frequency, predicted loss-of-function intolerance, segregation and functional data. Pathogenic variants are generally extremely rare or absent from population reference databases; a numerical allele-frequency threshold cannot be assigned uniformly across all genes. A **VUS must not be treated as causal** without additional evidence. (qiao2024commonvariantsincrease pages 3-4)

Representative functional mechanisms include:

- **Haploinsufficiency/loss of function:** GATA4, ZFPM2, NR2F2, WT1, MYRF, GATA6 and several chromatin regulators.
- **Recessive hypomorphic or loss-of-function disease:** ALDH1A2 and PIGN in appropriate syndromic contexts.
- **Regulatory/common susceptibility:** WNT5A- and SHH-adjacent loci identified in 2024.
- **Chromatin/transcriptional regulation:** SIN3A, STAG2, POGZ and other constrained genes identified by de novo burden analyses. Conditional Sin3a loss in mice causes membranous diaphragm and lung hypoplasia. (qiao2024commonvariantsincrease pages 13-15, qiao2024commonvariantsincrease pages 9-11)

Epigenetic dysregulation is biologically plausible because multiple implicated genes regulate chromatin and transcription, and **ALYREF** may affect epigenetic modifications. Nevertheless, no validated CDH-specific methylation signature is ready for routine diagnosis. Modifier genes are likely but few have been clinically validated.

## 5. Environmental information

CDH is not an infectious, occupationally acquired or lifestyle disease of the affected infant. The relevant exposure period is early embryogenesis. Maternal tobacco, alcohol, diabetes, nutritional inadequacy and pesticide exposure are candidate risks, but effect estimates are heterogeneous and residual confounding is important. Nitrofen is a research teratogen, not a common documented human exposure. Radiation and pollution have no established disease-specific causal role. (liu2024roleofgenetics pages 1-2, rivas2024theetiologyof pages 1-2)

**CHEBI suggestions:** retinoic acid (**CHEBI:15367**), retinol/vitamin A, retinaldehyde, nitric oxide (**CHEBI:16480**) and sildenafil. Ontology identifiers should be release-checked.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream developmental disturbance:** genetic, chromosomal and/or retinoid-pathway perturbation affects lateral plate/septum-transversum mesenchyme and pleuroperitoneal folds (PPFs) during approximately gestational weeks 4–12.
2. **Defective PPF expansion/fusion and myogenesis:** abnormal mesenchymal signaling and impaired migration of somite-derived muscle progenitors produce amuscular regions or failure of posterolateral closure.
3. **Primary lung-development defect:** altered mesenchymal–epithelial signaling, including deficient airway smooth-muscle progenitor function and FGF10 signaling, reduces branching morphogenesis before or independently of visceral compression.
4. **Secondary mechanical hit:** herniated stomach, bowel, spleen and/or liver compress the ipsilateral and contralateral fetal lungs, further reducing airway and vascular growth.
5. **Pulmonary vascular disease:** reduced vascular bed, excessive smooth-muscle proliferation, endothelial dysfunction, increased endothelin-1 signaling and impaired vasodilator responsiveness produce high pulmonary vascular resistance and right-to-left shunting.
6. **Clinical phenotype:** hypoxemia, hypercapnia, PPHN, ventricular dysfunction and systemic hypoperfusion cause neonatal respiratory/circulatory failure; ventilator injury and oxygen toxicity can add downstream chronic lung damage. (perveen2022cellularmolecularand pages 2-4, liu2024roleofgenetics pages 2-3, liu2024roleofgenetics pages 3-4, perveen2022cellularmolecularand pages 1-2)

The “dual-hit” model—primary abnormal lung development followed by compression—is better supported than a compression-only explanation. Molecular pathways include retinoic-acid/RAR signaling, GATA4–ZFPM2 transcriptional regulation, WT1 and NR2F2/COUP-TFII programs, WNT5A patterning, SHH signaling and FGF10-dependent branching. Relevant processes include mesenchymal differentiation, muscle-progenitor migration, epithelial–mesenchymal signaling, extracellular-matrix organization, airway branching, angiogenesis and pulmonary vascular remodeling. (friedmacher2022geneticallymodifiedmouse pages 2-3, liu2024roleofgenetics pages 3-4, perveen2022cellularmolecularand pages 4-5)

**GO suggestions:** diaphragm development; lung morphogenesis (**GO:0060425**); branching involved in lung morphogenesis; respiratory-system development; skeletal-muscle cell differentiation; mesenchymal-cell migration; angiogenesis (**GO:0001525**); smooth-muscle-cell proliferation; response to retinoic acid; extracellular-matrix organization (**GO:0030198**).

**Cell Ontology suggestions:** mesenchymal cell (**CL:0000134**), skeletal-muscle progenitor, smooth-muscle cell (**CL:0000192**), pulmonary-artery endothelial cell, lung epithelial cell, fibroblast (**CL:0000057**) and mesothelial cell (**CL:0000077**).

### Molecular profiling

Reported metabolic features include elevated lactate, ATP depletion and changes in antioxidant, glycolytic and nucleotide metabolites. Hypoxia increases reactive oxygen species, promoting endothelial dysfunction and smooth-muscle hyperplasia. Transcriptomic studies identify altered mesenchymal, vascular and developmental programs, but no transcriptomic, proteomic, lipidomic or metabolomic signature is clinically validated. Patient-derived fibroblasts and iPSCs, animal lung transcriptomics and emerging single-cell/spatial methods are research tools, not diagnostic standards. (perveen2022cellularmolecularand pages 5-6, perveen2022cellularmolecularand pages 4-5)

## 7. Anatomical structures affected

The primary site is the diaphragm—usually the left posterolateral hemidiaphragm. Herniated organs can include stomach, small and large bowel, spleen, liver and occasionally kidney. The lungs and pulmonary vasculature are the principal secondary targets; the heart, especially the left ventricle in left-sided disease, is compressed and developmentally affected. Gastrointestinal, musculoskeletal and nervous systems become important in long-term morbidity. (zani2022congenitaldiaphragmatichernia pages 1-2, zani2022congenitaldiaphragmatichernia pages 2-3)

**Suggested UBERON mappings:** diaphragm (**UBERON:0001103**), pleuroperitoneal fold, lung (**UBERON:0002048**), pulmonary artery, thoracic cavity, abdominal cavity, liver (**UBERON:0002107**) and left/right hemidiaphragm where available. At the subcellular level there is no single target organelle; nuclear transcription/chromatin regulation and mitochondrial/metabolic dysfunction are gene- or context-specific rather than universal.

## 8. Temporal development and natural history

The lesion originates during embryonic diaphragm formation, with PPF development around week 5 and pleuroperitoneal canal closure by approximately week 8. Clinical onset is therefore congenital, although detection may be prenatal, at birth or—especially for smaller defects—later in childhood or adulthood. (liu2024roleofgenetics pages 2-3)

Severe neonatal disease evolves rapidly over minutes to days as fetal circulation transitions and pulmonary vascular resistance fails to fall. Surgery corrects anatomy but does not immediately reverse hypoplastic lung or vascular disease. Survivors have a chronic, lifelong risk of pulmonary limitation, GERD, feeding/growth problems, recurrence, scoliosis and neurodevelopmental or hearing impairment. There is no “remission” in a conventional sense; stabilization, repair and developmental lung growth can produce major functional improvement.

Critical windows are early gestation for causation, mid-gestation for severity assessment, 27–29 weeks for FETO in selected severe disease, delivery for lung-protective stabilization and infancy/childhood for surveillance and rehabilitation. (NCT06179472 chunk 2, NCT06179472 chunk 1)

## 9. Inheritance and population epidemiology

Global birth prevalence is approximately **2.3 per 10,000 live births**, with estimates ranging from about 1:2,000 to 1:3,500 depending on inclusion of stillbirths and terminations. Approximately 50–60% are isolated. Males constituted 59% of a large 2024 genomic cohort, but sex effects are modest and population dependent. (perveen2022cellularmolecularand pages 1-2, rivas2024theetiologyof pages 1-2, zani2022congenitaldiaphragmatichernia pages 2-3, qiao2024commonvariantsincrease pages 6-7)

Most cases are sporadic and multifactorial. Depending on the causal lesion, inheritance may be autosomal dominant with incomplete penetrance, autosomal recessive, X-linked/syndromic, or chromosomal; de novo dominant variation is prominent. Expressivity is highly variable. Consanguinity mainly matters for rare recessive syndromic forms. There is no meaningful universal carrier frequency. Geographic outcome disparities are pronounced: mortality is approximately 20–30% in high-resource settings but can exceed 90% in low-resource settings, reflecting prenatal detection, neonatal intensive care, surgery and ECLS access rather than known population-genetic differences. (rivas2024theetiologyof pages 1-2, zani2022congenitaldiaphragmatichernia pages 1-2)

## 10. Diagnostics

### Prenatal diagnosis and severity assessment

Routine fetal ultrasonography can show intrathoracic stomach/bowel or liver, mediastinal shift, abnormal cardiac axis and reduced lung area. Detection rose from approximately 15% in the 1980s to 60–80% by the 2010s. Fetal echocardiography evaluates structural heart disease and ventricular function; MRI quantifies total fetal lung volume and liver herniation. (zani2022congenitaldiaphragmatichernia pages 1-2)

Key prognostic measures are observed-to-expected lung-to-head ratio (**O/E-LHR**), MRI observed-to-expected total fetal lung volume (**O/E-TFLV**), liver position and defect side. LHR <1 historically indicates poor prognosis. O/E-TFLV >35% was associated with 94% survival versus 56% below 35%; intrathoracic liver was associated with 45% versus 74% survival and ECMO use of 80% versus 25%. No single measure predicts an individual outcome perfectly. (perveen2022cellularmolecularand pages 1-2)

### Postnatal diagnosis

Chest radiography typically shows bowel loops or stomach in the hemithorax, mediastinal shift and a paucity of abdominal gas. Echocardiography assesses PPHN, shunts and ventricular function. Serial blood gases, oxygenation index, lactate, blood pressure, renal/hepatic chemistry and coagulation monitor severity; none is a CDH-specific diagnostic biomarker. CT or MRI is reserved for equivocal late presentations, recurrence or complex anatomy. Biopsy and pathology are not routinely required.

### Genetic workflow

Offer genetic counseling and prenatal/postnatal testing, especially for non-isolated disease. A practical sequence is karyotype when aneuploidy is suspected, **chromosomal microarray** for pathogenic CNVs, then trio **exome or genome sequencing** for SNVs/indels and additional structural variants. Prenatal cells are commonly obtained by second-trimester amniocentesis or first-trimester chorionic-villus sampling. Rapid sequencing can return results in approximately seven days in urgent settings. (zani2022congenitaldiaphragmatichernia pages 5-6, zani2022congenitaldiaphragmatichernia pages 3-4)

Reported diagnostic yield was **57% in complex/syndromic CDH** in one series—73% cytogenetic and 27% single-gene diagnoses—but only **2% in isolated CDH** under older, largely cytogenetic testing strategies. Yield in isolated disease may rise with modern trio genome analysis but remains lower than in complex cases. (perveen2022cellularmolecularand pages 5-6)

Targeted single-gene tests are appropriate only when phenotype strongly indicates a syndrome. Mitochondrial DNA and repeat-expansion testing are not routine. RNA-seq, methylomics, proteomics, metabolomics and liquid biopsy remain investigational.

Differential diagnoses include congenital pulmonary airway malformation, bronchopulmonary sequestration, diaphragmatic eventration/paralysis, congenital lung hypoplasia, cystic thoracic lesions, hiatal hernia and transient radiographic confusion with pneumothorax.

## 11. Outcomes and prognosis

High-income-center mortality is approximately 20–30%, while population survival—including fetal deaths and terminations—is about two-thirds. In a 2024 genomic cohort, 17% died before discharge, 30% required ECMO and 45% still had pulmonary hypertension at one month. Prognosis is worse with low O/E-LHR or O/E-TFLV, liver-up position, right-sided or bilateral disease, large C/D defect, associated anomalies/genetic diagnosis, severe ventricular dysfunction, persistent PH, prolonged ventilation and ECLS requirement. (zani2022congenitaldiaphragmatichernia pages 1-2, zani2022congenitaldiaphragmatichernia pages 2-3, qiao2024commonvariantsincrease pages 6-7)

Complications include chylothorax (5–10%), recurrent hernia, bowel obstruction, GERD, feeding failure, chronic lung disease, recurrent respiratory infection, hearing loss and neurodevelopmental impairment. Thoracoscopic repair has been associated with a 3.5-fold higher recurrence risk, and recurrence after large patch repair may approach 50% by age three. Ventilation/perfusion mismatch occurs in more than 60% of survivors. (zani2022congenitaldiaphragmatichernia pages 12-13)

Survival statistics are not equivalent to complete recovery. More than half of survivors have chronic morbidity, and robust adult life-expectancy data remain limited. Multidisciplinary longitudinal follow-up is therefore part of disease treatment, not optional surveillance.

## 12. Treatment and current implementation

### Postnatal stabilization

Delivery should occur at a tertiary center when prenatal CDH is known. Avoid routine bag-mask ventilation; promptly intubate, decompress the stomach with an oro-/nasogastric tube and use lung-protective ventilation. Management prioritizes permissive hypercapnia, avoidance of high peak pressures and adequate preductal oxygenation rather than “normalizing” all blood gases. Echocardiography-guided hemodynamic care addresses PPHN and ventricular dysfunction. (zani2022congenitaldiaphragmatichernia pages 1-2, zani2022congenitaldiaphragmatichernia pages 8-9)

Pulmonary/cardiac therapies may include inhaled nitric oxide, sildenafil, milrinone, prostacyclin-class agents and vasoactive support, individualized to physiology. iNO is used in up to 60%, but aggregate evidence shows limited benefit and possible harm if it delays ECLS; it should not be considered uniformly effective. Surfactant is not routinely beneficial in term CDH unless another indication exists. There is no established pharmacogenomic algorithm. (NCT06179472 chunk 2, zani2022congenitaldiaphragmatichernia pages 8-9)

**Suggested NCIt terms:** mechanical ventilation, high-frequency oscillatory ventilation, inhaled nitric oxide therapy, extracorporeal membrane oxygenation, sildenafil therapy, milrinone therapy and supportive care.

### ECLS/ECMO

Approximately 30% of severe cases require extracorporeal support. ECLS is considered for refractory hypoxemia, acidosis, hemodynamic failure or severe PH despite optimized ventilation and cardiovascular care. In selected high-risk infants, ECLS improved survival; however, mortality approaches 80% after four weeks of support. Repair during versus after ECLS remains center- and physiology-dependent. (zani2022congenitaldiaphragmatichernia pages 1-2, zani2022congenitaldiaphragmatichernia pages 8-9)

### Surgical repair

Repair follows physiologic stabilization rather than emergency closure at birth; about 80% undergo repair during the first week. Small defects receive primary closure. Large defects require a prosthetic patch or muscle flap, preferably configured as a dome/cone without tension. Open abdominal repair remains common; thoracoscopic repair is generally reserved for stable, lower-risk infants because recurrence is higher in some series. (zani2022congenitaldiaphragmatichernia pages 10-11)

### Fetal therapy

Fetoscopic endoluminal tracheal occlusion (**FETO**) temporarily traps fetal lung fluid to stimulate lung growth. In the TOTAL severe-left trial, survival was **40% with FETO versus 15% with expectant care**; moderate-left disease showed 63% versus 50%, a non-significant difference. Severe right-sided observational data showed 41% versus 15%. Benefits must be balanced against preterm prelabor rupture of membranes, preterm birth, balloon displacement, fetal injury and fatal airway obstruction if emergency delivery precedes balloon removal. (zani2022congenitaldiaphragmatichernia pages 8-9)

Current implementation remains concentrated in specialist fetal centers. Examples include **NCT06179472**, using balloon placement at 27–29 weeks and removal near 34 weeks for severe left CDH (O/E-LHR <30%) or right CDH (<45%) with liver up, and **NCT06739356**, an 80-participant North American registry tracking survival, PH, oxygen dependence and complications through 24 months. **NCT05962346** is a 20-patient severe-left pilot using O/E-LHR <25%. Trial records are dynamic and should be checked directly at https://clinicaltrials.gov/. (NCT06179472 chunk 2, NCT06739356 chunk 1, NCT05962346 chunk 1)

NIV-NAVA is being compared with assist-control ventilation in **NCT05839340** (estimated n=18), reflecting attempts to reduce ventilator asynchrony and barotrauma. No approved gene, RNA or cell therapy exists. Amniotic-fluid stem-cell extracellular vesicles and prenatal pulmonary-vascular drugs remain preclinical. (liu2024roleofgenetics pages 2-3, NCT05839340 chunk 1)

### Nutrition and rehabilitation

Term infants may require more than 125 kcal/kg/day and 2.3 g/kg/day protein; over 10% require feeding-tube access. Follow-up should include pulmonology, cardiology, surgery, gastroenterology/nutrition, audiology, neurodevelopment, physiotherapy and psychosocial support. (zani2022congenitaldiaphragmatichernia pages 10-11)

## 13. Prevention

There is no proven primary prevention for most sporadic CDH and no vaccine or prophylactic drug. General preconception measures include diabetes optimization, smoking/alcohol avoidance, medication/teratogen review and adequate guideline-concordant nutrition. High-dose vitamin A should not be used experimentally because excess retinoids are teratogenic.

Secondary prevention means early detection and severity stratification through routine prenatal ultrasound, referral for fetal MRI/echocardiography and delivery planning at an expert center. FETO is treatment for a highly selected affected fetus, not population prevention.

Tertiary prevention includes lung-protective ventilation, timely ECLS when indicated, tension-free repair, recurrence surveillance, immunization according to standard pediatric schedules, respiratory-infection prevention, nutritional support, hearing screening, neurodevelopmental assessment and long-term cardiopulmonary follow-up. Families with a pathogenic variant or chromosomal diagnosis should receive recurrence-risk counseling and discussion of prenatal diagnosis or preimplantation genetic testing. Empiric recurrence counseling is appropriate when testing is negative, acknowledging multifactorial risk.

## 14. Other species and natural disease

Naturally occurring congenital diaphragmatic defects are reported sporadically in domestic mammals, including dogs, cats and livestock, but robust breed-specific prevalence, VBO mappings and validated Mendelian veterinary loci were not established in the retrieved evidence. These defects are congenital, not zoonotic, and have no cross-species transmission.

Relevant taxa for experimental work include **Mus musculus** (NCBI Taxonomy 10090), **Rattus norvegicus** (10116) and fetal sheep, **Ovis aries** (9940). Orthologues of WT1, GATA4, ZFPM2, NR2F2 and retinoid-pathway genes are evolutionarily conserved, enabling comparative developmental study.

## 15. Model organisms

The **nitrofen rat model** is the most widely used induced model: maternal exposure around embryonic day 9 produces CDH with pulmonary hypoplasia in approximately 70% of offspring. It reproduces diaphragm defects, reduced branching, vascular remodeling and PH and is useful for prenatal drug, ventilation and FETO studies. Limitations are teratogen-specific off-target effects, variable defect penetrance and uncertain equivalence to human environmental exposure. (liu2024roleofgenetics pages 3-4, rivas2024theetiologyof pages 7-8)

Vitamin-A-deficient rodents and RAR-mutant mice directly test the retinoid hypothesis. Vitamin A repletion reduces defects in several models, but RAR-null animals often have low CDH penetrance and extensive cranial, vertebral, limb, cardiac and foregut abnormalities unlike typical isolated human CDH. (nakamura2020transgenicanimalmodels pages 1-2, friedmacher2022geneticallymodifiedmouse pages 1-2)

Genetic mouse models include **Wt1**, **Nr2f2/Coup-tf2**, **Gata4**, **Zfpm2/Fog2**, **Slit3**, **Kif7**, **Tcf21/Msc**, **Gli2/Gli3**, **Fbln4**, **Lrp1** and others. They reproduce different components—amuscular diaphragm, posterolateral defects, failed mesenchymal attachment, lung hypoplasia, abnormal alveoli or impaired branching. Conditional Wt1 deletion produces approximately 80–90% penetrance in relevant mesenchymal/PPF compartments, while conditional Nr2f2 deletion produces about 50% CDH. (friedmacher2022geneticallymodifiedmouse pages 3-4, nakamura2020transgenicanimalmodels pages 2-4, rivas2024theetiologyof pages 4-5)

These models are strongest for lineage tracing, developmental timing, tissue-specific gene function and testing retinoid or regenerative interventions. Their limitations include strain effects, incomplete penetrance, syndromic phenotypes, small fetal anatomy and frequent embryonic/perinatal lethality that prevents study of chronic survivor morbidity. Eighteen phenotypically relevant transgenic mouse models were catalogued by 2020, but no single model captures the full human spectrum. (nakamura2020transgenicanimalmodels pages 1-2, friedmacher2022geneticallymodifiedmouse pages 7-8)

## Evidence synthesis and expert interpretation

The current expert view is that CDH is a **developmental systems disorder** rather than a simple hole in the diaphragm. The strongest integrated model combines (1) genetically and environmentally sensitive PPF/mesenchymal development, (2) a primary lung-development defect, (3) secondary thoracic compression and (4) downstream pulmonary vascular and cardiac maladaptation. The 2024 genome study materially advances this model by showing that common polygenic susceptibility coexists with rare de novo variation rather than defining mutually exclusive disease classes. (liu2024roleofgenetics pages 2-3, qiao2024commonvariantsincrease pages 15-16)

Major unmet needs are improved individual prognostication, diverse-population genomics, functional validation of candidate variants, standardized cardiovascular treatment, safer fetal therapy, and adult natural-history data. Current molecular findings support better diagnosis and counseling, but—with the exception of selecting recognized syndromic care—do not yet direct genotype-specific therapy.

References

1. (rivas2024theetiologyof pages 1-2): Juan F. Garcia Rivas and Robin D. Clugston. The etiology of congenital diaphragmatic hernia: the retinoid hypothesis 20 years later. Pediatric Research, 95:912-921, Nov 2024. URL: https://doi.org/10.1038/s41390-023-02905-7, doi:10.1038/s41390-023-02905-7. This article has 24 citations and is from a domain leading peer-reviewed journal.

2. (qiao2024commonvariantsincrease pages 1-3): Lu Qiao, Carrie L. Welch, Rebecca Hernan, Julia Wynn, Usha S. Krishnan, Jill M. Zalieckas, Terry Buchmiller, Julie Khlevner, Aliva De, Christiana Farkouh-Karoleski, Amy J. Wagner, Andreas Heydweiller, Andreas C. Mueller, Annelies de Klein, Brad W. Warner, Carlo Maj, Dai Chung, David J. McCulley, David Schindel, Douglas Potoka, Elizabeth Fialkowski, Felicitas Schulz, Florian Kipfmuller, Foong-Yen Lim, Frank Magielsen, George B. Mychaliska, Gudrun Aspelund, Heiko Martin Reutter, Howard Needelman, J. Marco Schnater, Jason C. Fisher, Kenneth Azarow, Mahmoud Elfiky, Markus M. Nöthen, Melissa E. Danko, Mindy Li, Przemyslaw Kosiński, Rene M.H. Wijnen, Robert A. Cusick, Samuel Z. Soffer, Suzan C.M. Cochius-Den Otter, Thomas Schaible, Timothy Crombleholme, Vincent P. Duron, Patricia K. Donahoe, Xin Sun, Frances A. High, Charlotte Bendixen, Erwin Brosens, Yufeng Shen, and Wendy K. Chung. Common variants increase risk for congenital diaphragmatic hernia within the context of de novo variants. Nov 2024. URL: https://doi.org/10.1016/j.ajhg.2024.08.024, doi:10.1016/j.ajhg.2024.08.024. This article has 16 citations.

3. (qiao2024commonvariantsincrease pages 15-16): Lu Qiao, Carrie L. Welch, Rebecca Hernan, Julia Wynn, Usha S. Krishnan, Jill M. Zalieckas, Terry Buchmiller, Julie Khlevner, Aliva De, Christiana Farkouh-Karoleski, Amy J. Wagner, Andreas Heydweiller, Andreas C. Mueller, Annelies de Klein, Brad W. Warner, Carlo Maj, Dai Chung, David J. McCulley, David Schindel, Douglas Potoka, Elizabeth Fialkowski, Felicitas Schulz, Florian Kipfmuller, Foong-Yen Lim, Frank Magielsen, George B. Mychaliska, Gudrun Aspelund, Heiko Martin Reutter, Howard Needelman, J. Marco Schnater, Jason C. Fisher, Kenneth Azarow, Mahmoud Elfiky, Markus M. Nöthen, Melissa E. Danko, Mindy Li, Przemyslaw Kosiński, Rene M.H. Wijnen, Robert A. Cusick, Samuel Z. Soffer, Suzan C.M. Cochius-Den Otter, Thomas Schaible, Timothy Crombleholme, Vincent P. Duron, Patricia K. Donahoe, Xin Sun, Frances A. High, Charlotte Bendixen, Erwin Brosens, Yufeng Shen, and Wendy K. Chung. Common variants increase risk for congenital diaphragmatic hernia within the context of de novo variants. Nov 2024. URL: https://doi.org/10.1016/j.ajhg.2024.08.024, doi:10.1016/j.ajhg.2024.08.024. This article has 16 citations.

4. (qiao2024commonvariantsincrease pages 16-17): Lu Qiao, Carrie L. Welch, Rebecca Hernan, Julia Wynn, Usha S. Krishnan, Jill M. Zalieckas, Terry Buchmiller, Julie Khlevner, Aliva De, Christiana Farkouh-Karoleski, Amy J. Wagner, Andreas Heydweiller, Andreas C. Mueller, Annelies de Klein, Brad W. Warner, Carlo Maj, Dai Chung, David J. McCulley, David Schindel, Douglas Potoka, Elizabeth Fialkowski, Felicitas Schulz, Florian Kipfmuller, Foong-Yen Lim, Frank Magielsen, George B. Mychaliska, Gudrun Aspelund, Heiko Martin Reutter, Howard Needelman, J. Marco Schnater, Jason C. Fisher, Kenneth Azarow, Mahmoud Elfiky, Markus M. Nöthen, Melissa E. Danko, Mindy Li, Przemyslaw Kosiński, Rene M.H. Wijnen, Robert A. Cusick, Samuel Z. Soffer, Suzan C.M. Cochius-Den Otter, Thomas Schaible, Timothy Crombleholme, Vincent P. Duron, Patricia K. Donahoe, Xin Sun, Frances A. High, Charlotte Bendixen, Erwin Brosens, Yufeng Shen, and Wendy K. Chung. Common variants increase risk for congenital diaphragmatic hernia within the context of de novo variants. Nov 2024. URL: https://doi.org/10.1016/j.ajhg.2024.08.024, doi:10.1016/j.ajhg.2024.08.024. This article has 16 citations.

5. (liu2024roleofgenetics pages 1-2): Siyuan Liu and Lan Yu. Role of genetics and the environment in the etiology of congenital diaphragmatichernia. World Journal of Pediatric Surgery, 7:e000884, Aug 2024. URL: https://doi.org/10.1136/wjps-2024-000884, doi:10.1136/wjps-2024-000884. This article has 5 citations and is from a peer-reviewed journal.

6. (zani2022congenitaldiaphragmatichernia pages 1-2): Augusto Zani, Wendy K. Chung, Jan Deprest, Matthew T. Harting, Tim Jancelewicz, Shaun M. Kunisaki, Neil Patel, Lina Antounians, Pramod S. Puligandla, and Richard Keijzer. Congenital diaphragmatic hernia. Jun 2022. URL: https://doi.org/10.1038/s41572-022-00362-w, doi:10.1038/s41572-022-00362-w. This article has 279 citations.

7. (perveen2022cellularmolecularand pages 1-2): Shahana Perveen, Marta Frigeni, Helene Benveniste, and Dalibor Kurepa. Cellular, molecular, and metabolic aspects of developing lungs in congenital diaphragmatic hernia. Frontiers in Pediatrics, Nov 2022. URL: https://doi.org/10.3389/fped.2022.932463, doi:10.3389/fped.2022.932463. This article has 10 citations.

8. (zani2022congenitaldiaphragmatichernia pages 8-9): Augusto Zani, Wendy K. Chung, Jan Deprest, Matthew T. Harting, Tim Jancelewicz, Shaun M. Kunisaki, Neil Patel, Lina Antounians, Pramod S. Puligandla, and Richard Keijzer. Congenital diaphragmatic hernia. Jun 2022. URL: https://doi.org/10.1038/s41572-022-00362-w, doi:10.1038/s41572-022-00362-w. This article has 279 citations.

9. (liu2024roleofgenetics pages 3-4): Siyuan Liu and Lan Yu. Role of genetics and the environment in the etiology of congenital diaphragmatichernia. World Journal of Pediatric Surgery, 7:e000884, Aug 2024. URL: https://doi.org/10.1136/wjps-2024-000884, doi:10.1136/wjps-2024-000884. This article has 5 citations and is from a peer-reviewed journal.

10. (rivas2024theetiologyof pages 4-5): Juan F. Garcia Rivas and Robin D. Clugston. The etiology of congenital diaphragmatic hernia: the retinoid hypothesis 20 years later. Pediatric Research, 95:912-921, Nov 2024. URL: https://doi.org/10.1038/s41390-023-02905-7, doi:10.1038/s41390-023-02905-7. This article has 24 citations and is from a domain leading peer-reviewed journal.

11. (liu2024roleofgenetics pages 2-3): Siyuan Liu and Lan Yu. Role of genetics and the environment in the etiology of congenital diaphragmatichernia. World Journal of Pediatric Surgery, 7:e000884, Aug 2024. URL: https://doi.org/10.1136/wjps-2024-000884, doi:10.1136/wjps-2024-000884. This article has 5 citations and is from a peer-reviewed journal.

12. (schreiner2021geneticsofdiaphragmatic pages 2-3): Yannick Schreiner, Thomas Schaible, and Neysan Rafat. Genetics of diaphragmatic hernia. European Journal of Human Genetics, 29:1729-1733, Oct 2021. URL: https://doi.org/10.1038/s41431-021-00972-0, doi:10.1038/s41431-021-00972-0. This article has 25 citations and is from a domain leading peer-reviewed journal.

13. (liu2024roleofgenetics pages 12-12): Siyuan Liu and Lan Yu. Role of genetics and the environment in the etiology of congenital diaphragmatichernia. World Journal of Pediatric Surgery, 7:e000884, Aug 2024. URL: https://doi.org/10.1136/wjps-2024-000884, doi:10.1136/wjps-2024-000884. This article has 5 citations and is from a peer-reviewed journal.

14. (perveen2022cellularmolecularand pages 7-7): Shahana Perveen, Marta Frigeni, Helene Benveniste, and Dalibor Kurepa. Cellular, molecular, and metabolic aspects of developing lungs in congenital diaphragmatic hernia. Frontiers in Pediatrics, Nov 2022. URL: https://doi.org/10.3389/fped.2022.932463, doi:10.3389/fped.2022.932463. This article has 10 citations.

15. (qiao2024commonvariantsincrease pages 9-11): Lu Qiao, Carrie L. Welch, Rebecca Hernan, Julia Wynn, Usha S. Krishnan, Jill M. Zalieckas, Terry Buchmiller, Julie Khlevner, Aliva De, Christiana Farkouh-Karoleski, Amy J. Wagner, Andreas Heydweiller, Andreas C. Mueller, Annelies de Klein, Brad W. Warner, Carlo Maj, Dai Chung, David J. McCulley, David Schindel, Douglas Potoka, Elizabeth Fialkowski, Felicitas Schulz, Florian Kipfmuller, Foong-Yen Lim, Frank Magielsen, George B. Mychaliska, Gudrun Aspelund, Heiko Martin Reutter, Howard Needelman, J. Marco Schnater, Jason C. Fisher, Kenneth Azarow, Mahmoud Elfiky, Markus M. Nöthen, Melissa E. Danko, Mindy Li, Przemyslaw Kosiński, Rene M.H. Wijnen, Robert A. Cusick, Samuel Z. Soffer, Suzan C.M. Cochius-Den Otter, Thomas Schaible, Timothy Crombleholme, Vincent P. Duron, Patricia K. Donahoe, Xin Sun, Frances A. High, Charlotte Bendixen, Erwin Brosens, Yufeng Shen, and Wendy K. Chung. Common variants increase risk for congenital diaphragmatic hernia within the context of de novo variants. Nov 2024. URL: https://doi.org/10.1016/j.ajhg.2024.08.024, doi:10.1016/j.ajhg.2024.08.024. This article has 16 citations.

16. (qiao2024commonvariantsincrease pages 6-7): Lu Qiao, Carrie L. Welch, Rebecca Hernan, Julia Wynn, Usha S. Krishnan, Jill M. Zalieckas, Terry Buchmiller, Julie Khlevner, Aliva De, Christiana Farkouh-Karoleski, Amy J. Wagner, Andreas Heydweiller, Andreas C. Mueller, Annelies de Klein, Brad W. Warner, Carlo Maj, Dai Chung, David J. McCulley, David Schindel, Douglas Potoka, Elizabeth Fialkowski, Felicitas Schulz, Florian Kipfmuller, Foong-Yen Lim, Frank Magielsen, George B. Mychaliska, Gudrun Aspelund, Heiko Martin Reutter, Howard Needelman, J. Marco Schnater, Jason C. Fisher, Kenneth Azarow, Mahmoud Elfiky, Markus M. Nöthen, Melissa E. Danko, Mindy Li, Przemyslaw Kosiński, Rene M.H. Wijnen, Robert A. Cusick, Samuel Z. Soffer, Suzan C.M. Cochius-Den Otter, Thomas Schaible, Timothy Crombleholme, Vincent P. Duron, Patricia K. Donahoe, Xin Sun, Frances A. High, Charlotte Bendixen, Erwin Brosens, Yufeng Shen, and Wendy K. Chung. Common variants increase risk for congenital diaphragmatic hernia within the context of de novo variants. Nov 2024. URL: https://doi.org/10.1016/j.ajhg.2024.08.024, doi:10.1016/j.ajhg.2024.08.024. This article has 16 citations.

17. (zani2022congenitaldiaphragmatichernia pages 14-15): Augusto Zani, Wendy K. Chung, Jan Deprest, Matthew T. Harting, Tim Jancelewicz, Shaun M. Kunisaki, Neil Patel, Lina Antounians, Pramod S. Puligandla, and Richard Keijzer. Congenital diaphragmatic hernia. Jun 2022. URL: https://doi.org/10.1038/s41572-022-00362-w, doi:10.1038/s41572-022-00362-w. This article has 279 citations.

18. (qiao2024commonvariantsincrease pages 3-4): Lu Qiao, Carrie L. Welch, Rebecca Hernan, Julia Wynn, Usha S. Krishnan, Jill M. Zalieckas, Terry Buchmiller, Julie Khlevner, Aliva De, Christiana Farkouh-Karoleski, Amy J. Wagner, Andreas Heydweiller, Andreas C. Mueller, Annelies de Klein, Brad W. Warner, Carlo Maj, Dai Chung, David J. McCulley, David Schindel, Douglas Potoka, Elizabeth Fialkowski, Felicitas Schulz, Florian Kipfmuller, Foong-Yen Lim, Frank Magielsen, George B. Mychaliska, Gudrun Aspelund, Heiko Martin Reutter, Howard Needelman, J. Marco Schnater, Jason C. Fisher, Kenneth Azarow, Mahmoud Elfiky, Markus M. Nöthen, Melissa E. Danko, Mindy Li, Przemyslaw Kosiński, Rene M.H. Wijnen, Robert A. Cusick, Samuel Z. Soffer, Suzan C.M. Cochius-Den Otter, Thomas Schaible, Timothy Crombleholme, Vincent P. Duron, Patricia K. Donahoe, Xin Sun, Frances A. High, Charlotte Bendixen, Erwin Brosens, Yufeng Shen, and Wendy K. Chung. Common variants increase risk for congenital diaphragmatic hernia within the context of de novo variants. Nov 2024. URL: https://doi.org/10.1016/j.ajhg.2024.08.024, doi:10.1016/j.ajhg.2024.08.024. This article has 16 citations.

19. (qiao2024commonvariantsincrease pages 13-15): Lu Qiao, Carrie L. Welch, Rebecca Hernan, Julia Wynn, Usha S. Krishnan, Jill M. Zalieckas, Terry Buchmiller, Julie Khlevner, Aliva De, Christiana Farkouh-Karoleski, Amy J. Wagner, Andreas Heydweiller, Andreas C. Mueller, Annelies de Klein, Brad W. Warner, Carlo Maj, Dai Chung, David J. McCulley, David Schindel, Douglas Potoka, Elizabeth Fialkowski, Felicitas Schulz, Florian Kipfmuller, Foong-Yen Lim, Frank Magielsen, George B. Mychaliska, Gudrun Aspelund, Heiko Martin Reutter, Howard Needelman, J. Marco Schnater, Jason C. Fisher, Kenneth Azarow, Mahmoud Elfiky, Markus M. Nöthen, Melissa E. Danko, Mindy Li, Przemyslaw Kosiński, Rene M.H. Wijnen, Robert A. Cusick, Samuel Z. Soffer, Suzan C.M. Cochius-Den Otter, Thomas Schaible, Timothy Crombleholme, Vincent P. Duron, Patricia K. Donahoe, Xin Sun, Frances A. High, Charlotte Bendixen, Erwin Brosens, Yufeng Shen, and Wendy K. Chung. Common variants increase risk for congenital diaphragmatic hernia within the context of de novo variants. Nov 2024. URL: https://doi.org/10.1016/j.ajhg.2024.08.024, doi:10.1016/j.ajhg.2024.08.024. This article has 16 citations.

20. (perveen2022cellularmolecularand pages 2-4): Shahana Perveen, Marta Frigeni, Helene Benveniste, and Dalibor Kurepa. Cellular, molecular, and metabolic aspects of developing lungs in congenital diaphragmatic hernia. Frontiers in Pediatrics, Nov 2022. URL: https://doi.org/10.3389/fped.2022.932463, doi:10.3389/fped.2022.932463. This article has 10 citations.

21. (friedmacher2022geneticallymodifiedmouse pages 2-3): Florian Friedmacher, Udo Rolle, and Prem Puri. Genetically modified mouse models of congenital diaphragmatic hernia: opportunities and limitations for studying altered lung development. Frontiers in Pediatrics, May 2022. URL: https://doi.org/10.3389/fped.2022.867307, doi:10.3389/fped.2022.867307. This article has 6 citations.

22. (perveen2022cellularmolecularand pages 4-5): Shahana Perveen, Marta Frigeni, Helene Benveniste, and Dalibor Kurepa. Cellular, molecular, and metabolic aspects of developing lungs in congenital diaphragmatic hernia. Frontiers in Pediatrics, Nov 2022. URL: https://doi.org/10.3389/fped.2022.932463, doi:10.3389/fped.2022.932463. This article has 10 citations.

23. (perveen2022cellularmolecularand pages 5-6): Shahana Perveen, Marta Frigeni, Helene Benveniste, and Dalibor Kurepa. Cellular, molecular, and metabolic aspects of developing lungs in congenital diaphragmatic hernia. Frontiers in Pediatrics, Nov 2022. URL: https://doi.org/10.3389/fped.2022.932463, doi:10.3389/fped.2022.932463. This article has 10 citations.

24. (zani2022congenitaldiaphragmatichernia pages 2-3): Augusto Zani, Wendy K. Chung, Jan Deprest, Matthew T. Harting, Tim Jancelewicz, Shaun M. Kunisaki, Neil Patel, Lina Antounians, Pramod S. Puligandla, and Richard Keijzer. Congenital diaphragmatic hernia. Jun 2022. URL: https://doi.org/10.1038/s41572-022-00362-w, doi:10.1038/s41572-022-00362-w. This article has 279 citations.

25. (NCT06179472 chunk 2): Inna Lobeck. Infant Survival and Long-term Outcome Following Fetoscopic Endoluminal Tracheal Occlusion in Severe Left and Right Congenital Diaphragmatic Hernia, A Phase III Trial. Inna Lobeck. 2024. ClinicalTrials.gov Identifier: NCT06179472

26. (NCT06179472 chunk 1): Inna Lobeck. Infant Survival and Long-term Outcome Following Fetoscopic Endoluminal Tracheal Occlusion in Severe Left and Right Congenital Diaphragmatic Hernia, A Phase III Trial. Inna Lobeck. 2024. ClinicalTrials.gov Identifier: NCT06179472

27. (zani2022congenitaldiaphragmatichernia pages 5-6): Augusto Zani, Wendy K. Chung, Jan Deprest, Matthew T. Harting, Tim Jancelewicz, Shaun M. Kunisaki, Neil Patel, Lina Antounians, Pramod S. Puligandla, and Richard Keijzer. Congenital diaphragmatic hernia. Jun 2022. URL: https://doi.org/10.1038/s41572-022-00362-w, doi:10.1038/s41572-022-00362-w. This article has 279 citations.

28. (zani2022congenitaldiaphragmatichernia pages 3-4): Augusto Zani, Wendy K. Chung, Jan Deprest, Matthew T. Harting, Tim Jancelewicz, Shaun M. Kunisaki, Neil Patel, Lina Antounians, Pramod S. Puligandla, and Richard Keijzer. Congenital diaphragmatic hernia. Jun 2022. URL: https://doi.org/10.1038/s41572-022-00362-w, doi:10.1038/s41572-022-00362-w. This article has 279 citations.

29. (zani2022congenitaldiaphragmatichernia pages 12-13): Augusto Zani, Wendy K. Chung, Jan Deprest, Matthew T. Harting, Tim Jancelewicz, Shaun M. Kunisaki, Neil Patel, Lina Antounians, Pramod S. Puligandla, and Richard Keijzer. Congenital diaphragmatic hernia. Jun 2022. URL: https://doi.org/10.1038/s41572-022-00362-w, doi:10.1038/s41572-022-00362-w. This article has 279 citations.

30. (zani2022congenitaldiaphragmatichernia pages 10-11): Augusto Zani, Wendy K. Chung, Jan Deprest, Matthew T. Harting, Tim Jancelewicz, Shaun M. Kunisaki, Neil Patel, Lina Antounians, Pramod S. Puligandla, and Richard Keijzer. Congenital diaphragmatic hernia. Jun 2022. URL: https://doi.org/10.1038/s41572-022-00362-w, doi:10.1038/s41572-022-00362-w. This article has 279 citations.

31. (NCT06739356 chunk 1): Anthony Johnson. North American Fetal Therapy Network for Long-term Outcome Following Fetoscopic Endoluminal Tracheal Occlusion in Severe Left and Right Congenital Diaphragmatic Hernia. The University of Texas Health Science Center, Houston. 2025. ClinicalTrials.gov Identifier: NCT06739356

32. (NCT05962346 chunk 1): Mauro H. Schenone. Fetal Endoscopic Tracheal Occlusion for Congenital Diaphragmatic Hernia. Mauro H. Schenone. 2026. ClinicalTrials.gov Identifier: NCT05962346

33. (NCT05839340 chunk 1): Anne Greenough. Neurally Adjusted Ventilatory Assist for Neonates With Congenital Diaphragmatic Hernias. King's College Hospital NHS Trust. 2023. ClinicalTrials.gov Identifier: NCT05839340

34. (rivas2024theetiologyof pages 7-8): Juan F. Garcia Rivas and Robin D. Clugston. The etiology of congenital diaphragmatic hernia: the retinoid hypothesis 20 years later. Pediatric Research, 95:912-921, Nov 2024. URL: https://doi.org/10.1038/s41390-023-02905-7, doi:10.1038/s41390-023-02905-7. This article has 24 citations and is from a domain leading peer-reviewed journal.

35. (nakamura2020transgenicanimalmodels pages 1-2): Hiroki Nakamura, Takashi Doi, Prem Puri, and Florian Friedmacher. Transgenic animal models of congenital diaphragmatic hernia: a comprehensive overview of candidate genes and signaling pathways. Pediatric Surgery International, 36:991-997, Jun 2020. URL: https://doi.org/10.1007/s00383-020-04705-0, doi:10.1007/s00383-020-04705-0. This article has 20 citations and is from a peer-reviewed journal.

36. (friedmacher2022geneticallymodifiedmouse pages 1-2): Florian Friedmacher, Udo Rolle, and Prem Puri. Genetically modified mouse models of congenital diaphragmatic hernia: opportunities and limitations for studying altered lung development. Frontiers in Pediatrics, May 2022. URL: https://doi.org/10.3389/fped.2022.867307, doi:10.3389/fped.2022.867307. This article has 6 citations.

37. (friedmacher2022geneticallymodifiedmouse pages 3-4): Florian Friedmacher, Udo Rolle, and Prem Puri. Genetically modified mouse models of congenital diaphragmatic hernia: opportunities and limitations for studying altered lung development. Frontiers in Pediatrics, May 2022. URL: https://doi.org/10.3389/fped.2022.867307, doi:10.3389/fped.2022.867307. This article has 6 citations.

38. (nakamura2020transgenicanimalmodels pages 2-4): Hiroki Nakamura, Takashi Doi, Prem Puri, and Florian Friedmacher. Transgenic animal models of congenital diaphragmatic hernia: a comprehensive overview of candidate genes and signaling pathways. Pediatric Surgery International, 36:991-997, Jun 2020. URL: https://doi.org/10.1007/s00383-020-04705-0, doi:10.1007/s00383-020-04705-0. This article has 20 citations and is from a peer-reviewed journal.

39. (friedmacher2022geneticallymodifiedmouse pages 7-8): Florian Friedmacher, Udo Rolle, and Prem Puri. Genetically modified mouse models of congenital diaphragmatic hernia: opportunities and limitations for studying altered lung development. Frontiers in Pediatrics, May 2022. URL: https://doi.org/10.3389/fped.2022.867307, doi:10.3389/fped.2022.867307. This article has 6 citations.

## Artifacts

- [Edison artifact artifact-00](Congenital_Diaphragmatic_Hernia-deep-research-falcon_artifacts/artifact-00.md)