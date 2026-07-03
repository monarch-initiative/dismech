---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-13T17:59:36.665812'
end_time: '2026-06-13T18:09:37.953439'
duration_seconds: 601.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Cerebellar Ataxia With Late-Onset Spasticity
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Cerebellar_Ataxia_With_Late_Onset_Spasticity-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Cerebellar Ataxia With Late-Onset Spasticity
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Cerebellar Ataxia With Late-Onset Spasticity** covering all of the
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
- **Disease Name:** Autosomal Recessive Cerebellar Ataxia With Late-Onset Spasticity
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Cerebellar Ataxia With Late-Onset Spasticity** covering all of the
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


# Comprehensive Research Report: Autosomal Recessive Cerebellar Ataxia With Late-Onset Spasticity (ARCA-LOS)

## Executive summary
Autosomal recessive cerebellar ataxia with late-onset spasticity (ARCA-LOS) is a Mendelian neurodegenerative spastic-ataxia phenotype on the ataxia–hereditary spastic paraplegia (HSP) continuum, strongly linked to **biallelic loss-of-function or deleterious variants in GBA2** (glucosylceramidase beta 2), a non-lysosomal glucosylceramidase in sphingolipid metabolism. Across case series and mechanistic studies, the disorder is characterized by **cerebellar ataxia plus corticospinal tract signs (spasticity, pyramidal weakness)** with variable additional findings (neuropathy, cognitive involvement, cataracts, thin corpus callosum/white matter abnormalities, hypogonadism). Recent work (2022–2024) has expanded mechanistic understanding through patient-cell biochemistry, transcriptomics, and larger clinical series with enzymatic assays and imaging descriptions. (OpenTargets Search: Autosomal recessive cerebellar ataxia with spasticity,Hereditary spastic paraplegia type 46,SPG46,spastic ataxia-GBA2, martin2013lossoffunction pages 1-2, malekkou2018biochemicalcharacterizationof pages 1-3, kakouri2022transcriptomiccharacterizationof pages 1-2, cioffi2024hereditaryspasticparaparesis pages 1-2, cioffi2024hereditaryspasticparaparesis pages 4-7)

## Evidence map (high-level)
| Disease term | MONDO ID | Primary causal gene | Inheritance | Core phenotype | Notable lab/biochemical findings | Key supporting publications | Evidence type |
|---|---|---|---|---|---|---|---|
| Autosomal recessive cerebellar ataxia with late-onset spasticity | MONDO_0018129 | **GBA2** (ENSG00000070610) | Autosomal recessive | Spastic ataxia with overlap of cerebellar ataxia and spastic paraplegia; gait ataxia, limb spasticity/weakness; variable neuropathy and additional neurologic/extraneurologic features (kakouri2020analyzinggeneexpression pages 1-3, kakouri2022transcriptomiccharacterizationof pages 1-2, OpenTargets Search: Autosomal recessive cerebellar ataxia with spasticity,Hereditary spastic paraplegia type 46,SPG46,spastic ataxia-GBA2) | GBA2 is a non-lysosomal glucosylceramidase in sphingolipid metabolism; disease-associated dysfunction linked to altered glucosylceramide/ceramide handling (kakouri2022transcriptomiccharacterizationof pages 1-2, malekkou2018biochemicalcharacterizationof pages 1-3) | Open Targets disease-target association to GBA2 with literature PMID 23332917; MONDO mapping for the disease term (OpenTargets Search: Autosomal recessive cerebellar ataxia with spasticity,Hereditary spastic paraplegia type 46,SPG46,spastic ataxia-GBA2) | Human disease ontology / disease-target association |
| SPG46 (hereditary spastic paraplegia type 46) | MONDO_0018129* | **GBA2** (ENSG00000070610) | Autosomal recessive | Complex HSP phenotype with spastic paraplegia, cerebellar atrophy/ataxia, mental impairment, cataract, hypogonadism in males; variable corpus callosum and cerebellar atrophy on imaging (martin2013lossoffunction pages 1-2, cioffi2024hereditaryspasticparaparesis pages 1-2) | Missense example **c.1888C>T (p.Arg630Trp)** with absent residual GBA2 activity in blood cells in one homozygous subject; GBA2 catalyzes glucosylceramide to glucose + ceramide (martin2013lossoffunction pages 1-2) | Martin et al., 2013, *Am J Hum Genet* 92:238-244, DOI: 10.1016/j.ajhg.2012.11.021; Cioffi et al., 2024, *Neurogenetics* 25:51-67, DOI: 10.1007/s10048-024-00749-9 (martin2013lossoffunction pages 1-2, cioffi2024hereditaryspasticparaparesis pages 1-2) | Human genetics, enzyme assay, zebrafish functional model |
| Spastic ataxia (GBA2-associated; Cypriot family) | MONDO_0018129* | **GBA2** (ENSG00000070610) | Autosomal recessive | Mixed cerebellar ataxia and spasticity; main features include gait ataxia, spasticity, limb weakness; can include neuropathy, pyramidal/extrapyramidal signs, oculomotor abnormalities, cognitive involvement, seizures, retinopathy, hypogonadism (kakouri2020analyzinggeneexpression pages 1-3) | Homozygous **c.1780G>C (p.Asp594His)** causes marked reduction/abolishment of non-lysosomal glucosylceramidase activity, ~2-fold increased glucosylceramide in patient LCLs, and ~3-fold compensatory increase in lysosomal GBA activity (malekkou2018biochemicalcharacterizationof pages 1-3) | Malekkou et al., 2018, *Int J Mol Sci* 19:3099, DOI: 10.3390/ijms19103099; Kakouri et al., 2020, *Int J Mol Sci* 21:6722, DOI: 10.3390/ijms21186722 (malekkou2018biochemicalcharacterizationof pages 1-3, kakouri2020analyzinggeneexpression pages 1-3) | Human clinical report, patient-derived lymphoblastoid cells, pathway analysis |
| GBA2-associated spastic ataxia transcriptomic model | MONDO_0018129* | **GBA2** (ENSG00000070610) | Autosomal recessive | SA tissues/cells from patients with homozygous **c.1780G>C** used to study disease mechanisms; symptoms framed as overlap between ataxia and spastic paraplegia (kakouri2022transcriptomiccharacterizationof pages 1-2) | RNA-seq across LCLs, fibroblasts, and iPSC-derived neurons found **5217** significantly altered genes; implicated oxidative stress, neuroinflammation, sphingolipid signaling/metabolism, PI3K-Akt, and MAPK pathways (kakouri2022transcriptomiccharacterizationof pages 1-2) | Kakouri et al., 2022, *Cell & Bioscience* 12:29, DOI: 10.1186/s13578-022-00754-1 (kakouri2022transcriptomiccharacterizationof pages 1-2) | Patient cells, iPSC-derived neurons, transcriptomics |
| SPG46 / GBA2 literature synthesis | MONDO_0018129* | **GBA2** (ENSG00000070610) | Autosomal recessive | Review notes ~30 families and 62 patients reported worldwide; phenotypes span complicated HSP, recessive cerebellar ataxia, and Marinesco-Sjögren-like syndrome; notable features include upper gaze palsy and movement disorders (cioffi2024hereditaryspasticparaparesis pages 1-2) | GBA2 activity measurable in lymphoblasts/leucocytes; pathogenic mechanism linked to glucosylceramide accumulation and disturbed ganglioside/sphingolipid metabolism (cioffi2024hereditaryspasticparaparesis pages 1-2) | Cioffi et al., 2024, *Neurogenetics* 25:51-67, DOI: 10.1007/s10048-024-00749-9 (cioffi2024hereditaryspasticparaparesis pages 1-2) | Human case series and literature review |


*Table: This table summarizes the disease labels, ontology mapping, causal gene, phenotype, biochemical findings, and supporting studies for GBA2-associated autosomal recessive spastic ataxia/SPG46. It is useful for quickly aligning nomenclature across disease resources and the core human/mechanistic evidence base.*

---

## 1. Disease information
### 1.1 Concise overview
“Spastic ataxia (SA)” is commonly used as the umbrella clinical concept for disorders overlapping **cerebellar ataxia** and **spastic paraplegia**. A representative definition from recent mechanistic work states: **“Spastic ataxia (SA) is a group of rare neurodegenerative diseases, characterized by mixed features of generalized ataxia and spasticity.”** (Published 2020-09-14; *Int J Mol Sci*; URL https://doi.org/10.3390/ijms21186722) (kakouri2020analyzinggeneexpression pages 1-3)

Within this clinical space, ARCA-LOS corresponds to a specific ontology entity in Open Targets: **MONDO_0018129 (“autosomal recessive cerebellar ataxia with late-onset spasticity”)** with a curated disease–target association to **GBA2** supported by PubMed literature (PMID 23332917) (OpenTargets Search: Autosomal recessive cerebellar ataxia with spasticity,Hereditary spastic paraplegia type 46,SPG46,spastic ataxia-GBA2).

### 1.2 Key identifiers
* **MONDO:** **MONDO_0018129** (Open Targets) (OpenTargets Search: Autosomal recessive cerebellar ataxia with spasticity,Hereditary spastic paraplegia type 46,SPG46,spastic ataxia-GBA2)
* **Other identifiers (OMIM/Orphanet/ICD/MeSH):** Not retrieved in the documents available in this run; therefore not asserted here.

### 1.3 Synonyms / alternative names used in the literature
The retrieved literature uses partially overlapping disease labels for GBA2-related disease:
* **Spastic ataxia (SA)** (kakouri2020analyzinggeneexpression pages 1-3, kakouri2022transcriptomiccharacterizationof pages 1-2)
* **SPG46 / Hereditary spastic paraparesis (paraplegia) type 46** (martin2013lossoffunction pages 1-2, cioffi2024hereditaryspasticparaparesis pages 1-2)
* “Autosomal recessive cerebellar ataxia with spasticity” (as part of the SPG46/ARCA spectrum) (cioffi2024hereditaryspasticparaparesis pages 1-2, cioffi2024hereditaryspasticparaparesis pages 4-7)

### 1.4 Evidence source type
The information summarized here is derived from:
* **Aggregated disease-level resources:** Open Targets MONDO mapping and gene association (OpenTargets Search: Autosomal recessive cerebellar ataxia with spasticity,Hereditary spastic paraplegia type 46,SPG46,spastic ataxia-GBA2)
* **Primary human genetics and case series:** Martin 2013 (SPG46), Cioffi 2024 (Italian series) (martin2013lossoffunction pages 1-2, cioffi2024hereditaryspasticparaparesis pages 1-2, cioffi2024hereditaryspasticparaparesis pages 4-7)
* **Patient-derived cell studies:** Malekkou 2018 (LCL biochemistry), Kakouri 2022 (RNA-seq on patient-derived cell types) (malekkou2018biochemicalcharacterizationof pages 1-3, kakouri2022transcriptomiccharacterizationof pages 1-2)
* **Natural history/registry trials and rehabilitation trials in related spastic ataxias:** ClinicalTrials.gov records (NCT04297891 chunk 1, NCT05768750 chunk 1, NCT06261424 chunk 3)

---

## 2. Etiology
### 2.1 Primary causal factors
**Genetic (Mendelian, autosomal recessive): GBA2**
* A core mechanistic/genetic statement from *Am J Hum Genet* (2013-02-07) reports: **“Spastic paraplegia 46 refers to a locus mapped to chromosome 9 that accounts for a complicated autosomal-recessive form of hereditary spastic paraplegia (HSP). With next-generation sequencing in three independent families, we identiﬁed four different mutations in GBA2…”** (URL https://doi.org/10.1016/j.ajhg.2012.11.021) (martin2013lossoffunction pages 1-2)
* A 2024 review/case series similarly states: **“SPG46 is a rare, early-onset and autosomal recessive HSP, linked to biallelic GBA2 mutations.”** (Published online 2024-02-09; *Neurogenetics*; URL https://doi.org/10.1007/s10048-024-00749-9) (cioffi2024hereditaryspasticparaparesis pages 1-2)

### 2.2 Risk factors
For this Mendelian condition, the dominant risk factor is **biallelic pathogenic GBA2 variation**. Non-genetic risk factors were not identified in the retrieved sources.

### 2.3 Protective factors / gene–environment interactions
No protective factors or gene–environment interactions were identified in the retrieved sources.

---

## 3. Phenotypes (clinical features)
### 3.1 Core phenotype and variability
A broad clinical description of spastic ataxia notes: **“Their main characteristics include gait ataxia, spasticity, and weakness in the limbs.”** (Kakouri 2020; *Int J Mol Sci*; 2020-09-14; https://doi.org/10.3390/ijms21186722) (kakouri2020analyzinggeneexpression pages 1-3)

Additional features reported as potentially present include: **“neuropathy, pyramidal and extrapyramidal involvement, oculomotor abnormalities, cognitive involvement, seizures, retinopathy, and hypogonadism”** (kakouri2020analyzinggeneexpression pages 1-3).

In GBA2-related SPG46, the phenotype is frequently “complex” HSP. The 2013 report describes the overall phenotype as: **“a complex HSP with mental impairment, cataract, and hypogonadism in males associated with various degrees of corpus callosum and cerebellar atrophy on brain imaging.”** (martin2013lossoffunction pages 1-2)

### 3.2 Quantitative phenotype statistics (from a 2024 Italian SPG46 series)
In a multicenter Italian case series (n=5) of SPG46 with biallelic GBA2 variants, key summary statistics included:
* **Mean onset:** 6.8 years
* **Mean disease duration/progression:** 32 years
* **Mean age at last exam:** 38.6 years
* **Core findings (counts):** spasticity **5/5**, cerebellar syndrome **4/5**, peripheral neuropathy **4/5**, bilateral cataracts **4/5**; imaging white matter abnormalities **4/5**, thin corpus callosum **2/5** (cioffi2024hereditaryspasticparaparesis pages 2-4, cioffi2024hereditaryspasticparaparesis pages 4-7)

### 3.3 Suggested HPO terms (not exhaustive)
Based on the clinical descriptions in the retrieved sources:
* Cerebellar ataxia — **HP:0001251**
* Spasticity — **HP:0001257**
* Gait ataxia — **HP:0002066**
* Pyramidal weakness — **HP:0002493**
* Peripheral neuropathy — **HP:0009830**
* Cognitive impairment / intellectual disability — **HP:0100543 / HP:0001249**
* Cataract — **HP:0000518**
* Hypogonadism (male) — **HP:0000026**
* Thin corpus callosum — **HP:0002079**
* White matter abnormalities — **HP:0002500**
* Oculomotor abnormality / gaze palsy — **HP:0000602**

(These HPO identifiers are provided as ontology suggestions; the underlying phenotypes are supported by the cited sources.) (kakouri2020analyzinggeneexpression pages 1-3, martin2013lossoffunction pages 1-2, cioffi2024hereditaryspasticparaparesis pages 1-2, cioffi2024hereditaryspasticparaparesis pages 4-7)

### 3.4 Quality-of-life impact
Formal QoL instruments specific to GBA2/SPG46 were not identified in the retrieved papers. However, recent spastic ataxia natural history efforts explicitly incorporate **PROMIS** domains (“physical function”, “social roles and activities”) to quantify functional impact longitudinally (NCT04297891; first posted 2020-03-06; updated 2022-05-18) (NCT04297891 chunk 2).

---

## 4. Genetic / molecular information
### 4.1 Causal gene
* **Gene:** **GBA2** (glucosylceramidase beta 2)
* **Role:** microsomal/non-lysosomal glucosylceramidase; catalyzes glucosylceramide → glucose + ceramide; also hydrolyzes bile acid 3-O-glucosides (martin2013lossoffunction pages 1-2, malekkou2018biochemicalcharacterizationof pages 1-3)

### 4.2 Pathogenic variants (examples from retrieved primary sources)
**Martin et al., 2013 (Am J Hum Genet; 2013-02-07)**
* Missense variant example: **c.1888C>T (p.Arg630Trp)** (martin2013lossoffunction pages 1-2)

**Cioffi et al., 2024 (Neurogenetics; published online 2024-02-09)**
* Previously reported variants in their series/literature context: **c.472G>A (p.Gly158Arg)**; **c.2063G>A (p.Cys688Thr)** (cioffi2024hereditaryspasticparaparesis pages 4-7)
* New variants (examples in the excerpt): **c.1786G>T (p.Gly596Trp)** (homozygous) and truncating variants including **p.Gln674*** and **p.Trp551*** as part of compound heterozygous genotypes (cioffi2024hereditaryspasticparaparesis pages 4-7)

**Cypriot family (patient-cell functional work)**
* **c.1780G>C (p.Asp594His)** identified as causal in a consanguineous family with spastic ataxia and used for downstream mechanistic studies (kakouri2020analyzinggeneexpression pages 1-3, kakouri2022transcriptomiccharacterizationof pages 1-2, malekkou2018biochemicalcharacterizationof pages 1-3)

### 4.3 Variant type/class and functional consequence
Across the retrieved sources, pathogenicity is frequently consistent with **loss of function (LoF)**:
* Martin 2013: “three truncating variants and one missense variant” with **absent residual GBA2 activity** in blood cells for a homozygous missense case; the paper frames the mechanism as “Loss of Function of Glucocerebrosidase GBA2…” (martin2013lossoffunction pages 1-2)
* Malekkou 2018: the c.1780G>C variant leads to markedly reduced enzyme activity and substrate accumulation (malekkou2018biochemicalcharacterizationof pages 1-3)

### 4.4 Population frequency
Detailed allele frequencies from gnomAD/1000G were not present in the retrieved excerpts. However, Martin 2013 reports absence of c.1888C>T in **1,038 control chromosomes** and **~6,500 exomes** (Exome Variant Server) (martin2013lossoffunction pages 1-2).

### 4.5 Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes or epigenetic/chromosomal mechanisms were identified in the retrieved sources.

---

## 5. Environmental information
No environmental, lifestyle, or infectious triggers were reported in the retrieved sources; this appears primarily a genetic neurodegenerative disorder in the available evidence.

---

## 6. Mechanism / pathophysiology
### 6.1 Primary biochemical mechanism: sphingolipid metabolism disruption
A key mechanistic statement from Malekkou 2018 (2018-10-10; *Int J Mol Sci*) is:
* **“The GBA2 gene encodes the non-lysosomal glucosylceramidase (NLGase), an enzyme that catalyzes the conversion of glucosylceramide (GlcCer) to ceramide and glucose.”** (https://doi.org/10.3390/ijms19103099) (malekkou2018biochemicalcharacterizationof pages 1-3)

This aligns with Martin 2013’s description that GBA2 “catalyzes the conversion of glucosylceramide to free glucose and ceramide” and emphasizes a lipid/ceramide axis in motor neuron pathology (martin2013lossoffunction pages 1-2).

### 6.2 Patient-cell biochemical consequences (quantitative)
In lymphoblastoid cell lines from patients homozygous for **c.1780G>C (p.Asp594His)**, Malekkou 2018 reports:
* **“the mutation strongly reduce NLGase activity both intracellularly and at the plasma membrane level”**
* **“a two-fold increase of GlcCer content”**
* **“the activity of GCase was three-fold higher in LCLs derived from patients compared to controls”**
* concluding: **“loss of function with abolishment of the enzymatic activity and accumulation of GlcCer accompanied by a compensatory increase in GCase.”** (malekkou2018biochemicalcharacterizationof pages 1-3)

### 6.3 Transcriptomic mechanisms (2022; pathway-level)
Kakouri 2022 performed RNA-seq in LCLs, fibroblasts, and iPSC-derived neurons from patients homozygous for c.1780G>C and reports:
* **“a total of 5217 genes with significantly altered expression”**
* enriched pathways including **“oxidative stress, neuroinflammation, sphingolipid signaling and metabolism, PI3K-Akt and MAPK signaling pathways.”** (Published 2022-03-??; *Cell & Bioscience*; https://doi.org/10.1186/s13578-022-00754-1) (kakouri2022transcriptomiccharacterizationof pages 1-2)

### 6.4 Neurodevelopmental / neuronal vulnerability and model-organism support
Martin 2013 provides functional model evidence: zebrafish knockdown of the GBA2 ortholog caused abnormal motor behavior and motoneuron axonal defects, rescued by wild-type but not mutant human mRNA (martin2013lossoffunction pages 1-2). This supports a causal chain: **GBA2 LoF → altered ceramide/GlcCer handling → neuronal (motoneuron/corticospinal) structural/functional defects → spasticity and ataxia phenotypes** (martin2013lossoffunction pages 1-2, malekkou2018biochemicalcharacterizationof pages 1-3).

### 6.5 Suggested ontology terms (GO biological processes; CL cell types)
* **GO:0006665** sphingolipid metabolic process (mechanism supported by GBA2 enzymology and GlcCer accumulation) (martin2013lossoffunction pages 1-2, malekkou2018biochemicalcharacterizationof pages 1-3)
* **GO:0006687** glycosphingolipid metabolic process (malekkou2018biochemicalcharacterizationof pages 1-3)
* **GO:0001525** angiogenesis (not suggested)
* **GO:0006954** inflammatory response / neuroinflammation (supported as an enriched pathway in transcriptomics) (kakouri2022transcriptomiccharacterizationof pages 1-2)
* **GO:0006979** response to oxidative stress (enriched pathway) (kakouri2022transcriptomiccharacterizationof pages 1-2)

Cell types (CL suggestions based on affected systems described):
* Purkinje cell — **CL:0000121** (cerebellar involvement implied; not directly proven in the excerpts)
* Upper motor neuron / corticospinal neuron — (CL term depends on chosen ontology slice; suggested due to HSP hallmark “upper motor neurons”) (cioffi2024hereditaryspasticparaparesis pages 1-2)
* Motor neuron — **CL:0000100** (supported by zebrafish motoneuron phenotype) (martin2013lossoffunction pages 1-2)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
The disorder primarily affects the **nervous system**, especially long motor pathways and cerebellar circuits.

Kakouri 2020 notes the affected structures can include **“the cerebellum, the corpus callosum, the pyramidal track, as well as the spinocerebellar tract and/or the sensory tracts of the spinal cord.”** (kakouri2020analyzinggeneexpression pages 1-3)

SPG46 imaging in Martin 2013 includes “corpus callosum and cerebellar atrophy” (martin2013lossoffunction pages 1-2). The 2024 series reports frequent white matter abnormalities and thin corpus callosum (cioffi2024hereditaryspasticparaparesis pages 4-7).

### 7.2 Suggested UBERON terms
* Cerebellum — **UBERON:0002037**
* Corpus callosum — **UBERON:0002330**
* Spinal cord — **UBERON:0002240**
* Corticospinal tract — (UBERON term varies by resource; suggested due to pyramidal signs/HSP framing)

---

## 8. Temporal development
### 8.1 Onset
There is phenotypic heterogeneity in age at onset across labels (spastic ataxia vs SPG46 series):
* Kakouri 2022 states spastic ataxias are “characterized by an early age of onset, usually before the age of 20 years.” (kakouri2022transcriptomiccharacterizationof pages 1-2)
* Cioffi 2024 SPG46 series: mean onset **6.8 years** with one congenital case (cioffi2024hereditaryspasticparaparesis pages 2-4, cioffi2024hereditaryspasticparaparesis pages 4-7)

Because the target disease label includes “late-onset spasticity,” an important interpretation is that **spasticity may appear later than cerebellar features**, but the retrieved excerpts did not provide a formal staging model for this timing.

### 8.2 Progression
The Italian SPG46 cohort had a **slowly progressive** course with mean disease duration **32 years** (cioffi2024hereditaryspasticparaparesis pages 2-4, cioffi2024hereditaryspasticparaparesis pages 4-7).

---

## 9. Inheritance and population
### 9.1 Inheritance
Autosomal recessive inheritance is consistently reported:
* “complicated autosomal-recessive form” (Martin 2013) (martin2013lossoffunction pages 1-2)
* “autosomal recessive HSP, linked to biallelic GBA2 mutations” (Cioffi 2024) (cioffi2024hereditaryspasticparaparesis pages 1-2)

### 9.2 Epidemiology / counts
No prevalence/incidence for ARCA-LOS specifically was found in the retrieved sources.

However, Cioffi 2024 provides literature-based counts:
* “About thirty families” and **“62 patients… described worldwide”** (cioffi2024hereditaryspasticparaparesis pages 1-2)
* A broader literature summary in the same work notes **“67 cases from 36 families”** (cioffi2024hereditaryspasticparaparesis pages 4-7)

The same review also notes an apparent higher prevalence in Mediterranean countries (qualitative) (cioffi2024hereditaryspasticparaparesis pages 4-7).

---

## 10. Diagnostics
### 10.1 Clinical evaluation
Diagnosis relies on recognition of combined cerebellar and pyramidal signs (ataxia + spasticity) and evaluation for additional multisystem signs (neuropathy, cataracts, cognitive changes), supported by imaging and genetic testing (kakouri2020analyzinggeneexpression pages 1-3, martin2013lossoffunction pages 1-2, cioffi2024hereditaryspasticparaparesis pages 1-2).

### 10.2 Imaging
Reported imaging findings across SPG46 include:
* corpus callosum involvement / thin corpus callosum
* cerebellar atrophy
* white matter abnormalities

These are specifically mentioned in Martin 2013 (“corpus callosum and cerebellar atrophy”) and in Cioffi 2024 (WMA and TCC frequencies in their cohort) (martin2013lossoffunction pages 1-2, cioffi2024hereditaryspasticparaparesis pages 4-7).

### 10.3 Biomarkers / enzyme assays (actionable diagnostic adjunct)
A prominent diagnostic biomarker is **measured GBA2 enzymatic activity**.

Martin 2013 emphasizes feasibility of clinical enzyme measurement: **“The missense variant was also found at the homozygous state in a simplex subject in whom no residual glucocerebrosidase activity of GBA2 could be evidenced in blood cells, opening the way to a possible measurement of this enzyme activity in clinical practice.”** (martin2013lossoffunction pages 1-2)

Cioffi 2024 provides an explicit leukocyte assay approach and values, including proband activities as low as **0.01 nmol/mg** vs control mean **3.9 nmol/mg** (ref 2.5–5.3), and stresses diagnostic usefulness of enzyme testing (cioffi2024hereditaryspasticparaparesis pages 2-4, cioffi2024hereditaryspasticparaparesis pages 4-7).

### 10.4 Genetic testing
The available evidence supports the utility of multi-gene panels/exome sequencing in spastic-ataxia phenotypes (implied by targeted sequencing approaches and exome usage in Martin 2013 and modern cohort screening in Cioffi 2024) (martin2013lossoffunction pages 1-2, cioffi2024hereditaryspasticparaparesis pages 1-2).

### 10.5 Differential diagnosis
The retrieved sources did not provide a structured differential diagnosis list specific to ARCA-LOS; however, they note that spastic ataxia can be caused by many genes (e.g., SACS, FXN, SPG7, POLR3A, NKX6-2, GBA2) (kakouri2020analyzinggeneexpression pages 1-3).

---

## 11. Outcome / prognosis
No survival statistics were identified. Available evidence supports chronic, slowly progressive disability in long-duration cohorts (e.g., mean disease duration ~32 years in one SPG46 cohort) (cioffi2024hereditaryspasticparaparesis pages 4-7).

---

## 12. Treatment
### 12.1 Disease-modifying therapy
No established disease-modifying therapy for GBA2-related ARCA-LOS/SPG46 was identified in the retrieved sources.

### 12.2 Symptomatic/supportive and rehabilitative care (real-world implementations)
Although not specific to GBA2/SPG46, spastic ataxia rehabilitation trials and natural history efforts provide practical implementation templates for similar phenotypes:

**Natural history / trial readiness platform**
* **NCT04297891** “Phenotypes, Biomarkers and Pathophysiology in Spastic Ataxias” (first posted 2020-03-06; last update 2022-05-18; start 2020-09-01; primary completion estimated 2024-06) includes standardized ataxia/spasticity scales (SARA, SPRS), PROMIS PROs, biosampling, multi-omics, and multimodal MRI; also includes digital monitoring via mHealth/wearables (NCT04297891 chunk 1, NCT04297891 chunk 2).

**Rehabilitation / functional interventions**
* **NCT05768750** (submitted 2023-03-03; start 2022-12-01; estimated completion 2024-12-01) tests a pragmatic **12-week home-based rehabilitation program** in ARSACS with balance and spasticity measures (Modified Ashworth Scale) and feasibility/acceptability assessments (NCT05768750 chunk 1, NCT05768750 chunk 2).
* **NCT06261424** (2024 record) evaluates supervised rehabilitation in spastic ataxias (explicitly ARSACS or SPG7), incorporating objective biomechanical/physiologic endpoints (surface EMG, instrumented gait metrics) and health-economic evaluation (NCT06261424 chunk 3).

These programs are directly relevant to real-world care for spastic-ataxia phenotypes (including GBA2-related disease) because they operationalize measurable outcomes (SARA/SPRS, gait speed, balance tests, spasticity scales) and scalable delivery models (home programs with tele-follow-ups). (NCT05768750 chunk 1, NCT06261424 chunk 3)

### 12.3 Suggested MAXO terms (examples)
* Physical therapy — **MAXO:0000018** (supportive; supported indirectly via rehabilitation trial designs) (NCT05768750 chunk 1, NCT06261424 chunk 3)
* Occupational therapy — MAXO term suggested
* Genetic counseling — MAXO term suggested (autosomal recessive inheritance)

---

## 13. Prevention
Primary prevention is not applicable in the usual sense for a recessive genetic disorder; prevention is primarily **reproductive and family-risk management**:
* **Carrier testing and cascade testing** in affected families (supported by the AR inheritance evidence base) (martin2013lossoffunction pages 1-2, cioffi2024hereditaryspasticparaparesis pages 1-2)
* **Genetic counseling** for recurrence risk and reproductive options

No vaccination or environmental prevention strategies were identified.

---

## 14. Other species / natural disease
No naturally occurring non-human disease analogous to ARCA-LOS due to GBA2 was identified in the retrieved sources.

---

## 15. Model organisms
### 15.1 Zebrafish motor neuron model
Martin 2013 provides direct model-organism evidence that reduced GBA2 function causes motor neuron defects, including abnormal motor behavior and motoneuron axonal shortening/branching, and rescue with wild-type human mRNA (martin2013lossoffunction pages 1-2).

### 15.2 Mouse knockout observations
Malekkou 2018 notes that **GBA2-knockout mice** can show non-neurologic phenotypes (e.g., male infertility) and do not necessarily reproduce the neurologic phenotype despite brain GlcCer accumulation, highlighting model limitations; in contrast, zebrafish knockdown shows motor neuron defects (malekkou2018biochemicalcharacterizationof pages 1-3).

---

## Recent developments (prioritized 2023–2024)
1. **Large Italian SPG46 case series and literature synthesis (2024):** Identification of multiple novel and known GBA2 variants, detailed phenotype frequencies, and a strong emphasis on **GBA2 activity assays** as clinically useful biomarkers (Published online 2024-02-09; https://doi.org/10.1007/s10048-024-00749-9) (cioffi2024hereditaryspasticparaparesis pages 1-2, cioffi2024hereditaryspasticparaparesis pages 4-7).
2. **Modern mechanistic profiling (2022):** RNA-seq across patient-derived tissues/cells implicating oxidative stress, neuroinflammation, and major signaling pathways in GBA2-associated spastic ataxia, offering a framework for biomarker and target discovery (https://doi.org/10.1186/s13578-022-00754-1) (kakouri2022transcriptomiccharacterizationof pages 1-2).
3. **Clinical implementation research (2024):** Interventional rehabilitation trials in spastic ataxias with objective gait/EMG endpoints and explicit health-economic evaluation (NCT06261424) (NCT06261424 chunk 3).

---

## Limitations of this report
* The run did not retrieve OMIM/Orphanet/ICD/MeSH identifiers directly; thus they are not reported.
* The primary PubMed-indexed paper explicitly titled for “autosomal-recessive cerebellar ataxia with spasticity” due to GBA2 (Open Targets cites PMID 23332917) was not available in full text within the retrieved document set, so the report relies on accessible primary/secondary sources (OpenTargets Search: Autosomal recessive cerebellar ataxia with spasticity,Hereditary spastic paraplegia type 46,SPG46,spastic ataxia-GBA2).

---

## Key references (with URLs and dates where available)
* Martin E, et al. *Am J Hum Genet*. 2013-02-07. “Loss of Function of Glucocerebrosidase GBA2…” https://doi.org/10.1016/j.ajhg.2012.11.021 (martin2013lossoffunction pages 1-2)
* Malekkou A, et al. *Int J Mol Sci*. 2018-10-10. https://doi.org/10.3390/ijms19103099 (malekkou2018biochemicalcharacterizationof pages 1-3)
* Kakouri AC, et al. *Int J Mol Sci*. 2020-09-14. https://doi.org/10.3390/ijms21186722 (kakouri2020analyzinggeneexpression pages 1-3)
* Kakouri AC, et al. *Cell & Bioscience*. 2022. https://doi.org/10.1186/s13578-022-00754-1 (kakouri2022transcriptomiccharacterizationof pages 1-2)
* Cioffi E, et al. *Neurogenetics*. Published online 2024-02-09. https://doi.org/10.1007/s10048-024-00749-9 (cioffi2024hereditaryspasticparaparesis pages 1-2, cioffi2024hereditaryspasticparaparesis pages 4-7)
* ClinicalTrials.gov NCT04297891. First posted 2020-03-06; updated 2022-05-18 (NCT04297891 chunk 1, NCT04297891 chunk 2)
* ClinicalTrials.gov NCT05768750. Submitted 2023-03-03; start 2022-12-01 (NCT05768750 chunk 1)
* ClinicalTrials.gov NCT06261424. 2024 record (NCT06261424 chunk 3)


References

1. (OpenTargets Search: Autosomal recessive cerebellar ataxia with spasticity,Hereditary spastic paraplegia type 46,SPG46,spastic ataxia-GBA2): Open Targets Query (Autosomal recessive cerebellar ataxia with spasticity,Hereditary spastic paraplegia type 46,SPG46,spastic ataxia-GBA2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (martin2013lossoffunction pages 1-2): Elodie Martin, Rebecca Schüle, Katrien Smets, Agnès Rastetter, Amir Boukhris, José L. Loureiro, Michael A. Gonzalez, Emeline Mundwiller, Tine Deconinck, Marc Wessner, Ludmila Jornea, Andrés Caballero Oteyza, Alexandra Durr, Jean-Jacques Martin, Ludger Schöls, Chokri Mhiri, Foudil Lamari, Stephan Züchner, Peter De Jonghe, Edor Kabashi, Alexis Brice, and Giovanni Stevanin. Loss of function of glucocerebrosidase gba2 is responsible for motor neuron defects in hereditary spastic paraplegia. American journal of human genetics, 92 2:238-44, Feb 2013. URL: https://doi.org/10.1016/j.ajhg.2012.11.021, doi:10.1016/j.ajhg.2012.11.021. This article has 215 citations and is from a highest quality peer-reviewed journal.

3. (malekkou2018biochemicalcharacterizationof pages 1-3): Anna Malekkou, Maura Samarani, Anthi Drousiotou, Christina Votsi, Sandro Sonnino, Marios Pantzaris, Elena Chiricozzi, Eleni Zamba-Papanicolaou, Massimo Aureli, Nicoletta Loberto, and Kyproula Christodoulou. Biochemical characterization of the gba2 c.1780g&gt;c missense mutation in lymphoblastoid cells from patients with spastic ataxia. Oct 2018. URL: https://doi.org/10.3390/ijms19103099, doi:10.3390/ijms19103099. This article has 13 citations.

4. (kakouri2022transcriptomiccharacterizationof pages 1-2): Andrea C. Kakouri, Christina Votsi, Anastasis Oulas, Paschalis Nicolaou, Massimo Aureli, Giulia Lunghi, Maura Samarani, Giacomo M. Compagnoni, Sabrina Salani, Alessio Di Fonzo, Thalis Christophides, George A. Tanteles, Eleni Zamba-Papanicolaou, Marios Pantzaris, George M. Spyrou, and Kyproula Christodoulou. Transcriptomic characterization of tissues from patients and subsequent pathway analyses reveal biological pathways that are implicated in spastic ataxia. Cell & Bioscience, Mar 2022. URL: https://doi.org/10.1186/s13578-022-00754-1, doi:10.1186/s13578-022-00754-1. This article has 3 citations and is from a peer-reviewed journal.

5. (cioffi2024hereditaryspasticparaparesis pages 1-2): Ettore Cioffi, Gianluca Coppola, Olimpia Musumeci, Salvatore Gallone, Gabriella Silvestri, Salvatore Rossi, Fiorella Piemonte, Jessica D’Amico, Alessandra Tessa, Filippo Maria Santorelli, and Carlo Casali. Hereditary spastic paraparesis type 46 (spg46): new gba2 variants in a large italian case series and review of the literature. Neurogenetics, 25:51-67, Feb 2024. URL: https://doi.org/10.1007/s10048-024-00749-9, doi:10.1007/s10048-024-00749-9. This article has 1 citations and is from a peer-reviewed journal.

6. (cioffi2024hereditaryspasticparaparesis pages 4-7): Ettore Cioffi, Gianluca Coppola, Olimpia Musumeci, Salvatore Gallone, Gabriella Silvestri, Salvatore Rossi, Fiorella Piemonte, Jessica D’Amico, Alessandra Tessa, Filippo Maria Santorelli, and Carlo Casali. Hereditary spastic paraparesis type 46 (spg46): new gba2 variants in a large italian case series and review of the literature. Neurogenetics, 25:51-67, Feb 2024. URL: https://doi.org/10.1007/s10048-024-00749-9, doi:10.1007/s10048-024-00749-9. This article has 1 citations and is from a peer-reviewed journal.

7. (kakouri2020analyzinggeneexpression pages 1-3): Andrea C. Kakouri, Christina Votsi, Marios Tomazou, George Minadakis, Evangelos Karatzas, Kyproula Christodoulou, and George M. Spyrou. Analyzing gene expression profiles from ataxia and spasticity phenotypes to reveal spastic ataxia related pathways. International Journal of Molecular Sciences, 21:6722, Sep 2020. URL: https://doi.org/10.3390/ijms21186722, doi:10.3390/ijms21186722. This article has 5 citations.

8. (NCT04297891 chunk 1): Dr. Rebecca Schule. Phenotypes, Biomarkers and Pathophysiology in Spastic Ataxias. Dr. Rebecca Schule. 2020. ClinicalTrials.gov Identifier: NCT04297891

9. (NCT05768750 chunk 1): Cynthia Gagnon. A Home-based Rehabilitation in ARSACS. Université de Sherbrooke. 2022. ClinicalTrials.gov Identifier: NCT05768750

10. (NCT06261424 chunk 3): Elise Duchesne. Effects of a Supervised Rehabilitation Program on Disease Severity in Spastic Ataxias. Laval University. 2024. ClinicalTrials.gov Identifier: NCT06261424

11. (cioffi2024hereditaryspasticparaparesis pages 2-4): Ettore Cioffi, Gianluca Coppola, Olimpia Musumeci, Salvatore Gallone, Gabriella Silvestri, Salvatore Rossi, Fiorella Piemonte, Jessica D’Amico, Alessandra Tessa, Filippo Maria Santorelli, and Carlo Casali. Hereditary spastic paraparesis type 46 (spg46): new gba2 variants in a large italian case series and review of the literature. Neurogenetics, 25:51-67, Feb 2024. URL: https://doi.org/10.1007/s10048-024-00749-9, doi:10.1007/s10048-024-00749-9. This article has 1 citations and is from a peer-reviewed journal.

12. (NCT04297891 chunk 2): Dr. Rebecca Schule. Phenotypes, Biomarkers and Pathophysiology in Spastic Ataxias. Dr. Rebecca Schule. 2020. ClinicalTrials.gov Identifier: NCT04297891

13. (NCT05768750 chunk 2): Cynthia Gagnon. A Home-based Rehabilitation in ARSACS. Université de Sherbrooke. 2022. ClinicalTrials.gov Identifier: NCT05768750

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Cerebellar_Ataxia_With_Late_Onset_Spasticity-deep-research-falcon_artifacts/artifact-00.md)