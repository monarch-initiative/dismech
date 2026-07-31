---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:16:38.120280'
end_time: '2026-07-31T00:25:40.556864'
duration_seconds: 542.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Non-Syndromic Intellectual Disability
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 37
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Dominant_Non-Syndromic_Intellectual_Disability-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Non-Syndromic Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Non-Syndromic Intellectual Disability** covering all of the
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
- **Disease Name:** Autosomal Dominant Non-Syndromic Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Non-Syndromic Intellectual Disability** covering all of the
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


# Autosomal Dominant Non-Syndromic Intellectual Disability: Disease Characteristics Report

## Executive summary and scope

**Autosomal dominant non-syndromic intellectual disability (AD-NSID)** is not one uniform disorder. It is an umbrella for genetically heterogeneous neurodevelopmental disorders in which a heterozygous pathogenic variant causes intellectual and adaptive-function impairment as the principal phenotype, without a consistently recognizable congenital-malformation or multisystem syndrome. The preferred umbrella identifier is **MONDO:0015802**. It should be kept distinct from broader **autosomal dominant intellectual disability (MONDO:0100172)** and from numbered, gene-specific OMIM/MONDO entities. “Non-syndromic,” “nonspecific,” “isolated,” and “autosomal dominant mental retardation” are historical or alternative terms; however, “non-syndromic” is provisional because deeper phenotyping often identifies speech, behavioral, epileptic, growth, or subtle dysmorphic features. Open Targets currently associates MONDO:0015802 with genes including **TLK2, ASH1L, STAG1, CLTC, CAMK2A, CIC, NAA15, TRIP12, KMT5B, TRIO, SET, and DLG4**. This is a representative—not exhaustive—list and changes as gene–disease validity is reassessed. (OpenTargets Search: autosomal dominant intellectual disability)

Most evidence is aggregated from disease databases, gene-discovery studies, and mixed DD/ID sequencing cohorts, not from a single disease-specific EHR registry. Consequently, epidemiologic and phenotype frequencies reported for general ID/DD must not be interpreted as exact frequencies for MONDO:0015802.

| Domain | Current evidence | Suggested ontology/identifier |
|---|---|---|
| Scope / definition | Autosomal dominant non-syndromic intellectual disability is best treated as a heterogeneous umbrella disorder rather than a single uniform entity. Open Targets maps **autosomal dominant non-syndromic intellectual disability** to **MONDO:0015802** and lists representative associated genes including **TLK2, ASH1L, STAG1, CLTC, CAMK2A, CIC, NAA15, TRIP12, KMT5B, TRIO, SET, DLG4**; broader autosomal dominant ID is separated as **MONDO:0100172**. NSID denotes ID as the principal/isolated phenotype, though many reported “non-syndromic” cases may later accrue additional neurodevelopmental features (OpenTargets Search: autosomal dominant intellectual disability, maia2021intellectualdisabilitygenomics pages 1-2). | **MONDO:0015802**; related umbrella: **MONDO:0100172** |
| Disease level vs patient level evidence | Available evidence is mainly aggregated from disease/gene discovery studies, sequencing cohorts, and reviews; this is not primarily an EHR-derived single-disease registry. Most current knowledge comes from heterogeneous DD/ID/NDD cohorts in which AD de novo etiologies are overrepresented (li2024triowholeexomesequencing pages 1-2, ko2023genomewidesequencingmodalities pages 2-4, maia2021intellectualdisabilitygenomics pages 1-2). | Evidence type: aggregated disease/gene-level resource |
| Cardinal phenotype: intellectual disability | ID is defined by impaired intellectual functioning and adaptive behavior; overall ID prevalence is commonly cited at **1–3%** worldwide, with GDD/ID together affecting nearly **2%** of the pediatric population. Severity can range mild to profound; severe/profound forms are more often monogenic (maia2021intellectualdisabilitygenomics pages 1-2, ko2023genomewidesequencingmodalities pages 1-2, liaci2021neuronalcytoskeletonin pages 1-2). | **HPO:** Intellectual disability **HP:0001249**; Global developmental delay **HP:0001263** |
| Common associated neurodevelopmental phenotypes | Across DD/ID cohorts and mechanism reviews, common co-phenotypes include developmental delay, speech/language delay, seizures/epilepsy, autism/behavioral abnormalities, microcephaly, and dysmorphic features; these often increase diagnostic yield even when the target label is “non-syndromic” (li2024triowholeexomesequencing pages 1-2, ko2023genomewidesequencingmodalities pages 2-4, wayhelova2024exomesequencingimproves pages 1-2, kim2024diagnosticyieldof pages 1-2). | **HPO:** Developmental delay **HP:0001263**; Speech delay **HP:0000750**; Seizure **HP:0001250**; Autism **HP:0000717**; Behavioral abnormality **HP:0000708**; Microcephaly **HP:0000252**; Facial dysmorphism **HP:0001999** |
| Representative causal genes: synaptic / excitability | Representative AD genes linked in umbrella resources or cohort literature include **GRIN1, DLG4, CAMK2A, TRIO, NRXN1, STXBP1, DYRK1A, KIF1A, GNB1**; these converge on synapse formation/function, neuronal signaling, and plasticity (OpenTargets Search: autosomal dominant intellectual disability, vas2023regulatorydenovo pages 1-2, ford2023dendriticspineand pages 1-2). | HGNC gene symbols; **GO:** synapse organization **GO:0050808**; regulation of synaptic plasticity **GO:0048167** |
| Representative causal genes: chromatin / transcription / cohesin | Representative AD genes include **ASH1L, KMT5B, STAG1, CIC, TLK2, ARID1B, KANSL1, WDR5** and related chromatin modifiers highlighted as strong ASD/ID susceptibility factors affecting dendritic spine and synapse biology (OpenTargets Search: autosomal dominant intellectual disability, vas2023regulatorydenovo pages 1-2, ford2023dendriticspineand pages 1-2). | HGNC gene symbols; **GO:** chromatin organization **GO:0006325**; regulation of transcription by RNA polymerase II **GO:0006357** |
| Representative causal genes: cytoskeleton / trafficking / neuronal morphogenesis | Reviews emphasize convergence of many ID genes on cytoskeleton dynamics and Rho GTPase-regulated neuronal migration, neuritogenesis, and synaptic plasticity; examples include **TRIO, KIF1A, CLTC** and Rho-pathway-related genes in broader ID biology (liaci2021neuronalcytoskeletonin pages 1-2). | **GO:** actin cytoskeleton organization **GO:0030036**; microtubule cytoskeleton organization **GO:0000226**; neuron projection development **GO:0031175** |
| Variant classes / molecular lesion types | Relevant pathogenic mechanisms include coding **missense, nonsense, frameshift, splice**, **CNVs**, **small structural variants**, and increasingly **regulatory de novo mutations in fetal-brain enhancers**. Vas et al. showed regulatory DNMs enriched in fetal brain-specific enhancers, with recurrent enhancer clusters linked to **CSMD1, OLFM1, POU3F3** (vas2023regulatorydenovo pages 1-2, kim2024diagnosticyieldof pages 1-2). | Variant classes per ACMG/AMP; regulatory regions / enhancers |
| Inheritance / de novo contribution | AD ID is often caused by **de novo** variants, especially in moderate/severe disease. In a Finnish ID cohort, **75%** of variants in known ID genes were de novo/suspected de novo, including **64% autosomal dominant** and **11% X-linked**; only **25%** were inherited (jarvela2021exomesequencingreveals pages 1-2). Trio-WES in unexplained DD/ID also concluded that de novo variants in AD genes are major contributors, especially in non-consanguineous families (li2024triowholeexomesequencing pages 1-2). | Inheritance: **autosomal dominant**; de novo germline origin |
| Mosaicism / recurrence risk | Apparent de novo AD findings do not guarantee negligible recurrence risk. In a trio genome-wide study of 500 families, **12 cases of apparent mosaicism** were identified, including **9 parental** and **3 proband** mosaic cases; empirical recurrence for a child with a de novo dominant condition is often cited as ~**1%**, but parental gonadal mosaicism can raise risk substantially (cook2021somaticmosaicismdetected pages 1-2). | Counseling concept: parental/gonadal mosaicism; somatic mosaicism |
| Anatomy / organ systems | Primary affected organ/system is the **central nervous system**, especially cortical and hippocampal circuits supporting cognition, learning, and adaptive behavior. Reviews also note involvement of excitation/inhibition balance and, in some genetic subgroups, broader multisystem findings despite a nominally nonsyndromic label (liaci2021neuronalcytoskeletonin pages 1-2, ford2023dendriticspineand pages 1-2). | **UBERON:** brain **UBERON:0000955**; cerebral cortex **UBERON:0000956**; hippocampus **UBERON:0002421** |
| Cells / subcellular processes | Mechanistic evidence highlights **neurons**, especially **pyramidal neurons**, dendrites, dendritic spines, and synapses; abnormal neuronal migration, neuritogenesis, and synaptic plasticity are recurrent themes. Subcellular emphasis includes chromatin, actin/microtubule cytoskeleton, and synaptic compartments (liaci2021neuronalcytoskeletonin pages 1-2, ford2023dendriticspineand pages 1-2). | **CL:** neuron **CL:0000540**; pyramidal neuron **CL:0000598**; **GO CC:** dendrite **GO:0030425**; dendritic spine **GO:0043197**; synapse **GO:0045202**; nucleus **GO:0005634** |
| Pathophysiology / causal chain | Upstream lesions include de novo coding or regulatory variants affecting chromatin regulation, transcription, enhancer activity, cytoskeleton dynamics, trafficking, and synaptic proteins. Downstream consequences include altered neuronal migration/neuritogenesis, abnormal dendritic spine and synapse morphogenesis, impaired network formation, excitation/inhibition imbalance, and finally impaired cognition/adaptive behavior (liaci2021neuronalcytoskeletonin pages 1-2, vas2023regulatorydenovo pages 1-2, ford2023dendriticspineand pages 1-2). | **GO:** neuron migration **GO:0001764**; axonogenesis **GO:0007409**; dendrite morphogenesis **GO:0048813**; learning or memory **GO:0007611** |
| Diagnostic workflow | Current evidence supports **trio exome sequencing as first-tier** for unexplained DD/ID/NDD, with **genome sequencing** used early or after nondiagnostic CMA/exome, particularly where structural, intronic, or regulatory variants are suspected. Standard pre-genomic workup often includes history/exam, CMA, Fragile X or targeted testing when indicated, and phenotype-guided metabolic testing (ko2023genomewidesequencingmodalities pages 1-2, wayhelova2024exomesequencingimproves pages 1-2, wigby2024evidencereviewand pages 1-2, kim2024diagnosticyieldof pages 1-2). | ACMG-aligned genome-wide testing strategy |
| Recent diagnostic yield data (2023–2024 priority) | Recent cohorts report: trio-WES **49.7% (86/173)** in unexplained DD/ID; syndromic **57.8%** vs non-syndromic **47.2%** (li2024triowholeexomesequencing pages 1-2). Trio-ES in severe pediatric NDDs **48.9% (44/90)**, with **53.2%** of causative variants novel (wayhelova2024exomesequencingimproves pages 1-2). Singleton WES in undiagnosed rare pediatric disease **43% (25/58)** and clinical utility/actionability **76%** (slaba2024diagnosticefficacyand pages 1-2). Trio-WGS after prior chromosome analysis/CMA/CES gave an additional **19.2% (10/52)** diagnoses, **8/10** due to AD de novo variants (kim2024diagnosticyieldof pages 1-2). First-line GS review found mean diagnostic yield **45%** for first-line GS and management changes **24–100%** depending on cohort (wigby2024evidencereviewand pages 1-2). | Diagnostic modalities: WES, WGS, CMA |
| Real-world implementation | Real-world implementation now centers on clinical genetics and pediatric neurology pathways using trio-based ES/GS, ACMG-guided variant classification, and phenotype-driven reanalysis. ES/GS findings influence surveillance, reproductive counseling, and personalized management even when no disease-specific drug exists (wayhelova2024exomesequencingimproves pages 1-2, wigby2024evidencereviewand pages 1-2, slaba2024diagnosticefficacyand pages 1-2). | ACMG/AMP variant classification framework |
| Management / treatment | There is **no single disease-specific pharmacotherapy** for the umbrella disorder. Care is supportive and phenotype-directed: developmental therapies, speech/language therapy, educational support, behavioral management, seizure treatment when present, surveillance based on the molecular diagnosis, and genetic counseling. Reviews note that no pharmacological therapies are currently available for ID broadly, although pathway-based therapeutic opportunities are being explored (liaci2021neuronalcytoskeletonin pages 1-2, slaba2024diagnosticefficacyand pages 1-2). | **MAXO:** genetic counseling; developmental therapy; speech therapy; educational intervention; seizure management |
| Prevention / family planning | Primary prevention is generally not available for de novo monogenic disease; practical prevention focuses on **genetic counseling**, discussion of recurrence including mosaicism, and reproductive options after molecular diagnosis. Earlier genomic diagnosis can shorten the diagnostic odyssey and inform family planning (kim2024diagnosticyieldof pages 1-2, slaba2024diagnosticefficacyand pages 1-2, cook2021somaticmosaicismdetected pages 1-2). | **MAXO:** genetic counseling; reproductive counseling |
| Model systems / mechanistic platforms | Evidence includes animal and neuronal model studies summarized in reviews, especially mouse models of chromatin modifiers (**ARID1B, KANSL1, WDR5, ZMIZ1**) and systems-biology approaches emphasizing convergent neuronal network defects. These models are useful for studying dendritic spine, synapse, and developmental circuitry abnormalities (liaci2021neuronalcytoskeletonin pages 1-2, ford2023dendriticspineand pages 1-2). | Model categories: mouse models; neuronal cultures; systems biology |
| Evidence limitations | Disease boundaries are porous: “non-syndromic” cases may later show additional features; many data come from mixed DD/ID/NDD cohorts rather than pure MONDO:0015802 cohorts; gene lists change rapidly; penetrance/expressivity are often incompletely quantified; and few disorder-specific natural history or treatment trials exist (maia2021intellectualdisabilitygenomics pages 1-2, wayhelova2024exomesequencingimproves pages 1-2, slaba2024diagnosticefficacyand pages 1-2). | Curation note: maintain umbrella-vs-gene-specific distinction |


*Table: This table compacts the most actionable current evidence for autosomal dominant non-syndromic intellectual disability into a knowledge-base-ready format. It emphasizes scope, representative mechanisms and genes, ontology suggestions, modern diagnostic practice, and key evidence limitations.*

## 1. Disease information

ID is defined by significant limitations in both intellectual functioning and adaptive behavior—conceptual, social, and practical skills—with onset during the developmental period. Global developmental delay (GDD) is used in young children, generally under five years, when standardized intellectual assessment is not yet reliable. The older IQ-only definition is insufficient; adaptive impairment is essential. ID overall affects approximately **1–3%** of the population, while GDD/ID together affect nearly **2% of children**. These figures cover all etiologies, not specifically AD-NSID. Mild ID represents approximately 85% of ID, moderate 10%, severe 3.5%, and profound 1.5% in commonly cited aggregate classifications. (maia2021intellectualdisabilitygenomics pages 1-2, ko2023genomewidesequencingmodalities pages 1-2, liaci2021neuronalcytoskeletonin pages 1-2)

**Key identifiers and terminology**

- **MONDO:** MONDO:0015802, autosomal dominant non-syndromic intellectual disability.
- **Related MONDO:** MONDO:0100172, intellectual disability, autosomal dominant.
- **MeSH:** *Intellectual Disability* is the applicable broad concept; there is no uniquely specific MeSH descriptor for the AD-NSID umbrella.
- **ICD-10:** F70–F79 classify intellectual disabilities by severity; they do not encode AD-NSID etiology.
- **ICD-11:** 6A00, disorders of intellectual development, with severity extensions; again, inheritance is not encoded.
- **OMIM/Orphanet:** individual gene-defined disorders generally have separate entries; no single OMIM number adequately represents the full umbrella.
- **Synonyms:** autosomal dominant nonsyndromic ID; autosomal dominant non-syndromic mental retardation; isolated autosomal dominant intellectual disability; nonspecific autosomal dominant ID.

## 2. Etiology, risk, protection, and gene–environment interaction

### Genetic causes

The defining cause is a **germline heterozygous pathogenic variant**. Moderate-to-severe cases are frequently de novo; familial transmission is more readily observed in mild disease because affected adults may reproduce. A 2024 review estimated that more than 400 genes have been associated with autosomal-dominant ID, while broader ID databases contain well over 1,500 established genes. (hou2024a10yearreview pages 5-7, wayhelova2024exomesequencingimproves pages 1-2)

Variant classes include missense, nonsense, frameshift, splice-altering and in-frame variants; exon-level or larger CNVs; balanced/complex structural rearrangements; and regulatory variants. Mechanisms differ by gene and allele: **haploinsufficiency/loss of function**, dominant-negative effects, and gain of function are all possible. Therefore, a gene cannot be assigned one universal molecular mechanism without allele-specific evidence.

The Finnish exome study of 39 ID families found pathogenic/likely pathogenic variants in **25/39 (64%)**. Among variants in known ID genes, **75% were de novo or suspected de novo—64% autosomal dominant and 11% X-linked—whereas 25% were inherited**. This mixed syndromic/non-syndromic cohort supports the dominant de novo contribution but is not a prevalence study of AD-NSID. The abstract states: “**de novo variants were the most common variants underlying ID in the studied Finnish population**.” Published March 12, 2021; DOI: https://doi.org/10.1007/s00439-021-02268-1. (jarvela2021exomesequencingreveals pages 1-2)

### Regulatory and chromosomal causes

De Vas et al. sequenced 21 ID trios and analyzed another 30 exome-negative probands. Regulatory de novo variants were enriched in fetal-brain-specific enhancers, including recurrent enhancer clusters linked to **CSMD1, OLFM1, and POU3F3**. Luciferase assays showed allele-specific activity for most tested variants, and CRISPR mutation/epigenome editing altered putative target-gene expression. Their exact conclusion was that these results “**provide new evidence to indicate that DNMs in fetal brain-specific enhancers play an essential role in the aetiology of ID**.” This is primary genomic, in-vitro reporter, and CRISPR functional evidence, but the small cohort does not establish clinical penetrance for each regulatory variant. Published February 28, 2023; DOI: https://doi.org/10.26508/lsa.202201843. (vas2023regulatorydenovo pages 1-2)

Large CNVs explain approximately **10–14% of ID overall**, mostly de novo, but many produce syndromic phenotypes and should not automatically be labeled AD-NSID. (maia2021intellectualdisabilitygenomics pages 1-2)

### Environmental, infectious, and lifestyle factors

No toxin, pathogen, diet, exercise pattern, smoking exposure, or occupational factor is established as a cause of a genetically confirmed AD-NSID disorder. Prenatal infection, hypoxic–ischemic injury, prematurity complications, neonatal meningitis, toxins, severe malnutrition, and other acquired insults are important **alternative or additive causes of DD/ID**, not causes of Mendelian inheritance. They may worsen developmental outcome in an affected child, but quantitative AD-NSID-specific gene–environment interaction data are unavailable. (liaci2021neuronalcytoskeletonin pages 1-2)

No validated genetic or environmental **protective factor** prevents expression after a highly penetrant pathogenic variant. Favorable modifiers may exist, but none is sufficiently validated for clinical annotation. Early enriched education, communication support, and rehabilitation improve function rather than biologically preventing the genotype.

## 3. Phenotypes and quality-of-life effects

The cardinal phenotype is developmental-onset impairment of cognition and adaptive functioning. Severity ranges from mild learning disability to profound dependence. Onset is congenital/developmental but recognition usually occurs in infancy or childhood through delayed milestones, speech delay, school difficulty, or impaired adaptive skills. The disorder is generally chronic and lifelong, not relapsing-remitting. Skills may continue to develop slowly; true neurodegeneration or loss of milestones should trigger evaluation for a different or additional diagnosis.

| Phenotype | Typical characteristics | Suggested HPO term |
|---|---|---|
| Intellectual disability | Universal by definition; mild to profound; lifelong | HP:0001249 |
| Global developmental delay | Common presenting label in children under five | HP:0001263 |
| Delayed speech/language | Frequent across AD-ID genes; severity variable | HP:0000750 |
| Motor developmental delay | Variable; often less severe than language/cognitive delay | HP:0001270 |
| Impaired adaptive functioning | Conceptual, social, and practical limitations | HP:0011446, Abnormality of higher mental function, plus domain-specific terms |
| Behavioral abnormality | Autism, attention problems, anxiety, aggression, or stereotypy may occur but are not defining | HP:0000708; HP:0000717 for autism |
| Seizures/epilepsy | Gene-dependent rather than universal; may shift classification toward a syndromic/developmental epileptic encephalopathy | HP:0001250 |
| Hypotonia | Variable, often early childhood | HP:0001252 |
| Microcephaly or macrocephaly | Gene-dependent; not required | HP:0000252 / HP:0000256 |
| Subtle facial dysmorphism | May emerge with systematic examination and challenges a strict “non-syndromic” designation | HP:0001999 |

Quality-of-life impact is dominated by communication limitations, educational needs, reduced independence, social participation barriers, caregiver burden, and need for lifelong support. Gene-specific QoL, EQ-5D, SF-36, survival, and phenotype-frequency datasets are generally absent. A 2024 consensus analysis found that phenotype descriptions in novel Mendelian disorder reports were superficial or deficient in more than 87% of publications across prioritized domains, illustrating why exact frequencies, adulthood outcomes, sleep, pain, and QoL remain uncertain.

## 4. Genetic and molecular information

### Representative gene architecture

The following mechanistic groups are useful for curation; they are not an exhaustive diagnostic panel:

- **Chromatin, transcription, and cohesin:** ASH1L, KMT5B, STAG1, CIC, SET, TLK2, NAA15, TRIP12; broader AD-ID genes include ARID1B and other chromatin regulators.
- **Synapse and excitability:** CAMK2A, DLG4, GRIN1, GNB1 and gene-specific disorders involving STXBP1 or NRXN1.
- **Rho-GTPase/cytoskeletal development:** TRIO and related neuronal morphogenesis pathways.
- **Vesicle trafficking/transport:** CLTC, KIF1A, DYNC1H1.

Open Targets supports the association of the first set with MONDO:0015802 but does not, by itself, establish allele-level pathogenicity. Each variant requires ClinGen/ClinVar review, ACMG/AMP classification, segregation analysis, population frequency evaluation, and mechanism compatibility. (OpenTargets Search: autosomal dominant intellectual disability)

### Pathogenic variants and classification

Pathogenic/likely pathogenic variants are ordinarily absent or extremely rare in population databases such as gnomAD, although gene-specific reduced penetrance can complicate interpretation. A 2024 trio-WES study filtered variants at **minor allele frequency ≤0.01**, but the threshold for a severe de novo dominant disorder is usually much lower and should be set using disease prevalence, penetrance, and allelic heterogeneity. A VUS does **not** establish diagnosis and must not guide predictive testing or irreversible reproductive decisions. (li2024triowholeexomesequencing pages 2-3)

Most causal variants are constitutional germline variants. Postzygotic mosaicism in the proband can attenuate severity; parental somatic/gonadal mosaicism can make an apparently de novo variant recurrent. In 500 genome-wide-sequenced families, Cook et al. identified **12 apparent mosaic cases: nine parental and three proband**; six were not recognized as mosaic by Sanger sequencing. The authors concluded that genome-wide detection “**can permit more accurate genetic counseling**.” Published 2021; DOI: https://doi.org/10.1101/mcs.a006125. (cook2021somaticmosaicismdetected pages 1-2)

No consistently validated modifier gene, protective allele, or umbrella-specific episignature exists. Some individual chromatin disorders have blood DNA-methylation signatures, but those results should be recorded under the specific gene-defined disorder rather than generalized to AD-NSID.

## 5. Environmental information

Environmental exposures, lifestyle factors, and infectious agents are **not primary etiologies** once a causal AD variant is established. Their clinical relevance is principally differential diagnosis, prevention of additional brain injury, and optimization of general health. There is no AD-NSID-specific evidence that smoking, alcohol use by the affected person, diet, or exercise changes penetrance. Prenatal alcohol or teratogen exposure may create a blended phenotype. Routine immunization is appropriate but does not prevent the genetic disorder.

## 6. Mechanism and pathophysiology

### Integrated causal chain

1. **Upstream genetic lesion:** a coding, splice, CNV, structural, or fetal-brain regulatory variant alters dosage or function of an AD-ID gene.
2. **Molecular dysregulation:** disturbed chromatin remodeling/transcription, enhancer activity, RNA/protein regulation, Rho-GTPase signaling, microtubule/actin dynamics, vesicle transport, glutamatergic signaling, or postsynaptic scaffolding.
3. **Cellular effects:** altered neural progenitor programs, neuronal migration, neurite extension, dendritic arborization, spine morphogenesis, synapse formation and plasticity.
4. **Circuit effects:** inefficient cortical/hippocampal connectivity and, in some genes, excitation–inhibition imbalance.
5. **Clinical manifestation:** impaired learning, memory, language, executive function, and adaptive behavior.

The cytoskeleton review describes this hierarchy from molecular defect to “cell compartment and functions, circuits, cognition, and behavior.” It identifies cytoskeletal disruption affecting neuronal migration, neuritogenesis, and synaptic plasticity, and notes convergence on Rho-GTPase signaling. Published June 7, 2021; DOI: https://doi.org/10.3390/ijms22116167. (liaci2021neuronalcytoskeletonin pages 1-2)

Chromatin modifiers can also act upstream of synaptic pathology. Animal models and human postmortem evidence show abnormal dendritic-spine/synapse morphogenesis and plasticity; ARID1B, KANSL1, and WDR5 are highlighted examples. This evidence is mechanistically informative but is not specific to every MONDO:0015802 gene. Published January 19, 2023; DOI: https://doi.org/10.3389/fnmol.2022.1048713. (ford2023dendriticspineand pages 1-2)

**Suggested GO biological-process terms:** chromatin organization (GO:0006325); regulation of transcription by RNA polymerase II (GO:0006357); nervous system development (GO:0007399); neuron migration (GO:0001764); neuron projection development (GO:0031175); axonogenesis (GO:0007409); dendrite morphogenesis (GO:0048813); synapse organization (GO:0050808); regulation of synaptic plasticity (GO:0048167); actin cytoskeleton organization (GO:0030036); learning or memory (GO:0007611).

**Suggested cell types:** neuron (CL:0000540), pyramidal neuron (CL:0000598), excitatory neuron and inhibitory interneuron where gene-specific evidence exists, neural stem/progenitor cell for prenatal chromatin/enhancer mechanisms. No immune-cell or inflammatory mechanism is consistently implicated in the umbrella disorder.

No reproducible umbrella-level metabolomic, lipidomic, proteomic, or circulating biomarker signature exists. WGS plus regulatory epigenomics and functional CRISPR assays represent the most relevant recent multi-omic advance. (vas2023regulatorydenovo pages 1-2)

## 7. Anatomical structures affected

The **central nervous system** is primary, especially cerebral cortex and hippocampal networks involved in cognition and memory. Cerebellar involvement may occur in individual genotypes. Peripheral organs are not obligatorily involved; consistent congenital or multisystem abnormalities should prompt a gene-specific syndromic diagnosis.

Suggested annotations are brain (UBERON:0000955), cerebral cortex (UBERON:0000956), hippocampus (UBERON:0002421), nervous tissue, neuron (CL:0000540), pyramidal neuron (CL:0000598), nucleus (GO:0005634), chromatin, cytoskeleton, dendrite (GO:0030425), dendritic spine (GO:0043197), and synapse (GO:0045202). Effects are bilateral and network-level; there is no characteristic lateralization. (liaci2021neuronalcytoskeletonin pages 1-2, ford2023dendriticspineand pages 1-2)

## 8. Temporal development

The biological lesion is present from conception or arises early postzygotically. Vulnerability is greatest during prenatal neurogenesis, neuronal migration, circuit assembly, and early-childhood synaptic maturation. Clinical onset is insidious and developmental rather than acute. The course is usually stable/nondegenerative but lifelong; developmental gains occur at a slower rate and may plateau. There are no validated early/intermediate/end-stage categories and no expected remission. Early childhood is the principal intervention window because communication systems, adaptive skills, and educational supports can be introduced during maximal developmental plasticity.

## 9. Inheritance and population

Inheritance is autosomal dominant. An affected heterozygous parent generally has a **50% transmission probability per pregnancy**, although expression may vary. Many moderate/severe cases are de novo, so family history is often negative. In the 2024 trio-WES cohort, **95.4%** had no family history of epilepsy or DD/ID, emphasizing that a negative pedigree does not exclude dominant disease. (li2024triowholeexomesequencing pages 2-3)

Penetrance is high for many severe de novo loss-of-function disorders but gene- and allele-specific. Expressivity can vary widely. Anticipation is not a general feature; repeat-expansion disorders belong in the differential rather than the core AD-NSID category. Consanguinity is not a risk factor for AD-NSID, though it raises the probability of an alternative recessive diagnosis. Founder effects and carrier frequencies are variant-specific; there is no meaningful aggregate carrier frequency because affected heterozygotes are not asymptomatic “carriers.”

For a confirmed de novo variant absent from parental blood, counseling commonly starts with an empirical recurrence risk near **1%**, reflecting possible gonadal mosaicism. If a parent is mosaic, recurrence can be substantially higher and depends on germ-cell involvement; Cook et al. explain a theoretical range from approximately **1–2% to as high as 50%**. Deep sequencing of multiple parental tissues or paternal sperm can refine risk in selected families. (cook2021somaticmosaicismdetected pages 1-2)

There is no reliable incidence or prevalence specifically for MONDO:0015802, no established ethnic concentration, geographic endemicity, or robust sex ratio. Autosomal inheritance predicts broadly similar biological risk in males and females; ascertainment may differ because males are more often referred for neurodevelopmental assessment.

## 10. Diagnostics

### Clinical assessment

Assessment should include prenatal/perinatal and three-generation history; growth and dysmorphology examination; formal developmental, cognitive, language, and adaptive testing; hearing and vision evaluation; neurologic examination; and autism/behavioral screening. EEG is indicated for seizures or suspicious episodes, MRI for abnormal neurologic examination, regression, focal signs, abnormal head growth, or a genotype-specific indication. Routine biopsy is not useful. Metabolic testing should be phenotype-directed, particularly for regression, episodic decompensation, organomegaly, movement disorder, or unusual biochemical findings.

### Current genetic-testing algorithm

1. **Trio ES or GS early/first tier**, with CNV calling and ACMG/AMP interpretation.
2. If ES is used, ensure adequate CNV detection; add **CMA** where platform/payer practice requires it or CNV sensitivity is insufficient.
3. Use **Fragile X testing**, repeat-expansion assays, methylation testing, mitochondrial testing, or single-gene testing when clinically indicated because standard ES may miss these mechanisms.
4. For nondiagnostic ES, perform periodic reanalysis, then GS to detect structural, deep-intronic, regulatory, repeat, low-level mosaic, or poorly covered variants.
5. RNA sequencing or methylation studies may resolve splice variants or gene-specific episignatures, but are not universal diagnostic tests.

Recent implementation data are strong:

- **Li et al., November 2024:** trio-WES diagnosed **86/173 (49.7%)** unexplained DD/ID cases. SNVs accounted for **54/173 (31.2%)** and CNVs for **36/173 (20.8%)**; 22 SNVs were novel. Yield was **57.8% in syndromic versus 47.2% in non-syndromic DD/ID**. Exact abstract conclusion: “**De novo variants in autosomal dominant genes are significant contributors to DD/ID**.” DOI: https://doi.org/10.1038/s41598-024-79431-x. (li2024triowholeexomesequencing pages 1-2)
- **Wayhelova et al., February 2024:** trio-based ES yielded **44/90 (48.9%)** diagnoses in severe pediatric NDD/MCA; **25/47 (53.2%)** causative variants were novel, and ES detected intragenic CNVs through a 6-Mb duplication. DOI: https://doi.org/10.1186/s13023-024-03056-6. (wayhelova2024exomesequencingimproves pages 1-2)
- **Kim et al., August 2, 2024:** after chromosome analysis, CMA, and clinical exome were nondiagnostic, trio-WGS solved an additional **10/52 (19.2%)**; **8/10** were AD de novo diagnoses. Reasons included small structural variants, uncovered/new genes, low variant allele fraction, coverage, and interpretation. DOI: https://doi.org/10.3390/diagnostics14151680. (kim2024diagnosticyieldof pages 1-2)
- **Wigby et al., February 2024:** across 71 GS studies and more than 13,000 patients, unweighted mean yield was **45%** for first-line GS, **33%** after prior testing, and **33%** in exome-negative cohorts; reported management changes ranged **24–100%**. DOI: https://doi.org/10.1038/s41525-024-00396-x. (wigby2024evidencereviewand pages 1-2)
- **Slaba et al., November 2024:** singleton WES diagnosed **25/58 (43%)** undiagnosed pediatric patients; **76%** of diagnosed cases had at least one management change. DOI: https://doi.org/10.1038/s41598-024-79872-4. (slaba2024diagnosticefficacyand pages 1-2)

Differential diagnosis includes syndromic AD-ID, X-linked or recessive ID, chromosomal disorders, Fragile X, imprinting disorders, developmental epileptic encephalopathy, autism without ID, cerebral palsy/perinatal injury, fetal alcohol spectrum disorder, congenital infection, metabolic disease, hypothyroidism, hearing/vision impairment, and neurodegenerative disorders. Clinical phenotype alone often cannot reliably distinguish them.

Population newborn screening is not available. After finding a familial variant, cascade testing, prenatal diagnosis, and preimplantation genetic testing are technically possible. Predictive testing of asymptomatic minors requires careful consideration because onset is developmental and penetrance may be allele-specific.

## 11. Outcome and prognosis

No umbrella-specific 5-year survival, life expectancy, or disease-specific mortality rate is available. In genuinely non-syndromic ID without epilepsy, severe motor impairment, swallowing dysfunction, or organ disease, life expectancy may approach that of the general population, but this cannot be assumed for every genotype. Morbidity is chiefly lifelong cognitive, communication, adaptive, educational, vocational, and social disability.

Major prognostic factors are severity of early developmental impairment, language acquisition, epilepsy, autism/behavioral comorbidity, motor and feeding ability, access to communication and educational services, and the specific molecular diagnosis. There is no validated molecular prognostic biomarker across AD-NSID. Recovery to fully typical cognition is uncommon, but meaningful functional gains are expected with individualized support. Regression, new neurologic signs, or unexpectedly rapid deterioration warrants reassessment for seizures, medication effects, psychiatric illness, sleep disorder, or an alternative/blended diagnosis.

## 12. Treatment and current applications

There is no approved disease-modifying pharmacotherapy, gene therapy, RNA therapy, cell therapy, immunotherapy, or surgery for the MONDO:0015802 umbrella. The 2021 mechanistic review states that “**no pharmacological therapies are currently available**” for ID broadly. Molecular diagnosis nevertheless changes surveillance, avoids unnecessary testing, informs recurrence counseling, and occasionally identifies a genotype-specific comorbidity or treatment. (liaci2021neuronalcytoskeletonin pages 1-2, slaba2024diagnosticefficacyand pages 1-2)

**Standard multidisciplinary management**

- Individualized early developmental intervention, special education, and behavioral supports.
- Speech-language therapy and augmentative/alternative communication.
- Occupational and physical therapy for adaptive, sensory, fine-motor, gross-motor, or hypotonia-related needs.
- Standard evidence-based treatment for epilepsy, ADHD, anxiety, sleep disturbance, constipation, feeding problems, and other comorbidities.
- Hearing, vision, dental, nutritional, sleep, and safeguarding assessment.
- Transition planning, supported decision-making, vocational support, respite, and caregiver mental-health support.

Suggested MAXO annotations include genetic counseling, developmental assessment, neuropsychological assessment, speech-language therapy, occupational therapy, physical therapy, educational intervention, augmentative communication, EEG, brain MRI, genomic sequencing, and seizure management. Precise MAXO IDs should be verified against the current ontology release before database ingestion.

No clinical trial retrieved was a disease-modifying trial specifically for AD-NSID. Relevant ID-wide studies largely concern behavioral, communication, lifestyle, or comorbidity interventions—for example written-language intervention (**NCT05851937**) and metformin for antipsychotic-associated weight gain (**NCT05744479**)—and should not be represented as treatments for the underlying genetic disease.

Research directions include restoring gene dosage, allele-specific silencing for gain-of-function alleles, ASOs, CRISPR-based correction, and pathway modulation of chromatin, Rho-GTPase/cytoskeletal, or synaptic defects. These remain gene- and variant-specific, largely preclinical concepts; the same intervention could be harmful if applied across opposite loss- and gain-of-function mechanisms.

## 13. Prevention

Primary prevention by lifestyle change or vaccination is not applicable. Prevention is principally reproductive and complication-focused:

- Preconception and postdiagnostic genetic counseling.
- Parental testing with consideration of low-level mosaicism.
- Prenatal testing by CVS/amniocentesis or PGT-M when a familial pathogenic variant is known.
- Early developmental surveillance of at-risk children.
- Prevention of secondary harm through seizure control, communication support, safe feeding, sleep care, sensory screening, vaccination, and avoidance of additional neurotoxic exposures.

Noninvasive prenatal screening does not comprehensively detect heterogeneous single-gene AD-NSID. Prenatal diagnosis should not be based on a VUS.

## 14. Other species and natural disease

There is no recognized naturally occurring veterinary disease that is directly equivalent to the heterogeneous human AD-NSID umbrella. Orthologous genes are widely conserved in mammals, zebrafish, Drosophila, and *C. elegans*, and variants may cause learning, behavior, synaptic, or developmental phenotypes. These are comparative models rather than zoonotic disease. There is no infectious transmission, cross-species transmission, or zoonotic potential. Gene-, species-, NCBI Taxon-, NCBI Gene-, and VBO-level entries should be curated separately for each causal gene/model.

## 15. Model organisms

Available systems include constitutive or conditional knockout/heterozygous mice, variant knock-in mice, zebrafish, Drosophila, cultured primary neurons, patient-derived iPSCs, induced neurons, and cerebral organoids. Chromatin-modifier models involving **ARID1B, KANSL1, WDR5**, and related genes reproduce aspects of dendritic arborization, spine morphology, synaptic signaling, learning, or behavior. Cytoskeletal models test neuronal migration, neuritogenesis, Rho-GTPase signaling, and network plasticity. Regulatory-variant studies combine human WGS with luciferase assays and CRISPR epigenome editing. (liaci2021neuronalcytoskeletonin pages 1-2, vas2023regulatorydenovo pages 1-2, ford2023dendriticspineand pages 1-2)

Model limitations are substantial: human adaptive behavior cannot be directly modeled; heterozygous null animals may not mimic a human dominant-negative or gain-of-function allele; developmental timing and cortical architecture differ across species; and behavioral assays have limited construct validity. The preferred model is therefore variant-specific and should demonstrate directionally correct molecular dysfunction before therapeutic testing.

## Evidence-quality conclusions

The strongest current evidence concerns the high contribution of de novo AD variants, the diagnostic effectiveness of trio ES/GS, and convergence on prenatal gene regulation, cytoskeletal development, and synaptic function. The weakest areas are disease-specific epidemiology, phenotype frequencies, adult natural history, QoL, penetrance, modifier genes, and treatment outcomes. A knowledge base should consequently retain **MONDO:0015802 as an umbrella**, attach variants and mechanisms to the relevant gene-specific disease whenever possible, and label statistics derived from mixed DD/ID cohorts as indirect rather than AD-NSID-specific evidence.

References

1. (OpenTargets Search: autosomal dominant intellectual disability): Open Targets Query (autosomal dominant intellectual disability, 32 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (maia2021intellectualdisabilitygenomics pages 1-2): Nuno Maia, Maria João Nabais Sá, Manuel Melo-Pires, Arjan P. M. de Brouwer, and Paula Jorge. Intellectual disability genomics: current state, pitfalls and future challenges. BMC Genomics, Dec 2021. URL: https://doi.org/10.1186/s12864-021-08227-4, doi:10.1186/s12864-021-08227-4. This article has 125 citations and is from a peer-reviewed journal.

3. (li2024triowholeexomesequencing pages 1-2): Chengyan Li, You Wang, Cizheng Zeng, Binglong Huang, Yinhui Chen, Chupeng Xue, Ling Liu, Shiwen Rong, and Yongwen Lin. Trio-whole exome sequencing reveals the importance of de novo variants in children with intellectual disability and developmental delay. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-79431-x, doi:10.1038/s41598-024-79431-x. This article has 22 citations and is from a peer-reviewed journal.

4. (ko2023genomewidesequencingmodalities pages 2-4): Mary Hsin-Ju Ko and Hui-Ju Chen. Genome-wide sequencing modalities for children with unexplained global developmental delay and intellectual disabilities—a narrative review. Mar 2023. URL: https://doi.org/10.3390/children10030501, doi:10.3390/children10030501. This article has 14 citations.

5. (ko2023genomewidesequencingmodalities pages 1-2): Mary Hsin-Ju Ko and Hui-Ju Chen. Genome-wide sequencing modalities for children with unexplained global developmental delay and intellectual disabilities—a narrative review. Mar 2023. URL: https://doi.org/10.3390/children10030501, doi:10.3390/children10030501. This article has 14 citations.

6. (liaci2021neuronalcytoskeletonin pages 1-2): Carla Liaci, Mattia Camera, Giovanni Caslini, Simona Rando, Salvatore Contino, Valentino Romano, and G. Merlo. Neuronal cytoskeleton in intellectual disability: from systems biology and modeling to therapeutic opportunities. International Journal of Molecular Sciences, Jun 2021. URL: https://doi.org/10.3390/ijms22116167, doi:10.3390/ijms22116167. This article has 36 citations.

7. (wayhelova2024exomesequencingimproves pages 1-2): Marketa Wayhelova, Vladimira Vallova, Petr Broz, Aneta Mikulasova, Jan Smetana, Hana Dynkova Filkova, Dominika Machackova, Kristina Handzusova, Renata Gaillyova, and Petr Kuglik. Exome sequencing improves the molecular diagnostics of paediatric unexplained neurodevelopmental disorders. Orphanet Journal of Rare Diseases, Feb 2024. URL: https://doi.org/10.1186/s13023-024-03056-6, doi:10.1186/s13023-024-03056-6. This article has 18 citations and is from a peer-reviewed journal.

8. (kim2024diagnosticyieldof pages 1-2): Jaewon Kim, Jaewoong Lee, Myungshin Kim, and Dae-Hyun Jang. Diagnostic yield of trio whole-genome sequencing in children with undiagnosed developmental delay or congenital anomaly: a prospective cohort study. Diagnostics, 14:1680, Aug 2024. URL: https://doi.org/10.3390/diagnostics14151680, doi:10.3390/diagnostics14151680. This article has 6 citations.

9. (vas2023regulatorydenovo pages 1-2): Matias G De Vas, Fanny Boulet, Shweta S Joshi, Myles G Garstang, Tahir N Khan, Goutham Atla, David Parry, David Moore, Inês Cebola, Shuchen Zhang, Wei Cui, Anne K Lampe, Wayne W Lam, Jorge Ferrer, Madapura M Pradeepa, and Santosh S Atanur. Regulatory de novo mutations underlying intellectual disability. Life Science Alliance, 6:e202201843, Feb 2023. URL: https://doi.org/10.26508/lsa.202201843, doi:10.26508/lsa.202201843. This article has 7 citations and is from a peer-reviewed journal.

10. (ford2023dendriticspineand pages 1-2): Thomas James L. Ford, Byeong Tak Jeon, Hyunkyoung Lee, and Woo-Yang Kim. Dendritic spine and synapse pathology in chromatin modifier-associated autism spectrum disorders and intellectual disability. Frontiers in Molecular Neuroscience, Jan 2023. URL: https://doi.org/10.3389/fnmol.2022.1048713, doi:10.3389/fnmol.2022.1048713. This article has 30 citations.

11. (jarvela2021exomesequencingreveals pages 1-2): Irma Järvelä, Tuomo Määttä, Anushree Acharya, Juha Leppälä, Shalini N. Jhangiani, Maria Arvio, Auli Siren, Minna Kankuri-Tammilehto, Hannaleena Kokkonen, Maarit Palomäki, Teppo Varilo, Mary Fang, Trevor D. Hadley, Angad Jolly, Tarja Linnankivi, Ritva Paetau, Anni Saarela, Reetta Kälviäinen, Jan Olme, Liz M. Nouel-Saied, Diana M. Cornejo-Sanchez, Lorida Llaci, James R. Lupski, Jennifer E. Posey, Suzanne M. Leal, and Isabelle Schrauwen. Exome sequencing reveals predominantly de novo variants in disorders with intellectual disability (id) in the founder population of finland. Human Genetics, 140:1011-1029, Mar 2021. URL: https://doi.org/10.1007/s00439-021-02268-1, doi:10.1007/s00439-021-02268-1. This article has 55 citations and is from a peer-reviewed journal.

12. (cook2021somaticmosaicismdetected pages 1-2): Courtney B. Cook, Linlea Armstrong, Cornelius F. Boerkoel, Lorne A. Clarke, Christèle du Souich, Michelle K. Demos, William T. Gibson, Harinder Gill, Elena Lopez, Millan S. Patel, Kathryn Selby, Ziad Abu-Sharar, Alison M. Elliott, and Jan M. Friedman. Somatic mosaicism detected by genome-wide sequencing in 500 parent–child trios with suspected genetic disease: clinical and genetic counseling implications. Molecular Case Studies, 7:a006125, Oct 2021. URL: https://doi.org/10.1101/mcs.a006125, doi:10.1101/mcs.a006125. This article has 25 citations.

13. (wigby2024evidencereviewand pages 1-2): Kristen M. Wigby, Deanna Brockman, Gregory Costain, Caitlin Hale, Stacie L. Taylor, John Belmont, David Bick, David Dimmock, Susan Fernbach, John Greally, Vaidehi Jobanputra, Shashikant Kulkarni, Elizabeth Spiteri, and Ryan J. Taft. Evidence review and considerations for use of first line genome sequencing to diagnose rare genetic disorders. npj Genomic Medicine, Feb 2024. URL: https://doi.org/10.1038/s41525-024-00396-x, doi:10.1038/s41525-024-00396-x. This article has 26 citations and is from a peer-reviewed journal.

14. (slaba2024diagnosticefficacyand pages 1-2): Katerina Slaba, Petra Pokorna, Robin Jugas, Hana Palova, Dagmar Prochazkova, Stefania Aulicka, Klara Spanelova, Pavlina Danhofer, Ondrej Horak, Jana Tuckova, Petra Kleiblova, Renata Gaillyova, Matej Hrunka, Martin Jouza, Blanka Pinkova, Jan Papez, Petra Konecna, Jana Zidkova, Petr Stourac, Jaroslav Sterba, Regina Demlova, Eva Demlova, Petr Jabandziev, and Ondrej Slaby. Diagnostic efficacy and clinical utility of whole-exome sequencing in czech pediatric patients with rare and undiagnosed diseases. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-79872-4, doi:10.1038/s41598-024-79872-4. This article has 5 citations and is from a peer-reviewed journal.

15. (hou2024a10yearreview pages 5-7): Kexin Hou and Xinyan Zheng. A 10-year review on advancements in identifying and treating intellectual disability caused by genetic variations. Genes, 15:1118, Aug 2024. URL: https://doi.org/10.3390/genes15091118, doi:10.3390/genes15091118. This article has 9 citations.

16. (li2024triowholeexomesequencing pages 2-3): Chengyan Li, You Wang, Cizheng Zeng, Binglong Huang, Yinhui Chen, Chupeng Xue, Ling Liu, Shiwen Rong, and Yongwen Lin. Trio-whole exome sequencing reveals the importance of de novo variants in children with intellectual disability and developmental delay. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-79431-x, doi:10.1038/s41598-024-79431-x. This article has 22 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Dominant_Non-Syndromic_Intellectual_Disability-deep-research-falcon_artifacts/artifact-00.md)