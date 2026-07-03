---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-11T20:32:59.050345'
end_time: '2026-06-11T20:40:16.812682'
duration_seconds: 437.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SRPX2-related Speech-Epilepsy-Polymicrogyria Boundary
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_tokens: 12000
    max_embedded_images: 8
citation_count: 24
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: SRPX2-related_Speech_Epilepsy_Polymicrogyria-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SRPX2-related Speech-Epilepsy-Polymicrogyria Boundary
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SRPX2-related Speech-Epilepsy-Polymicrogyria Boundary** covering all of the
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
- **Disease Name:** SRPX2-related Speech-Epilepsy-Polymicrogyria Boundary
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SRPX2-related Speech-Epilepsy-Polymicrogyria Boundary** covering all of the
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


# SRPX2-related Speech–Epilepsy–Polymicrogyria Boundary (Mendelian) — Research Report

## Executive summary
SRPX2-related disease is a rare **X-linked neurodevelopmental disorder spectrum** centered on (i) **focal (rolandic/centrotemporal) epilepsy**, (ii) **speech/oromotor dyspraxia and language impairment**, and (iii) in some individuals, **bilateral perisylvian polymicrogyria (PMG)** involving speech-related cortical regions. Current mechanistic understanding places SRPX2 within a **FOXP2-regulated network** and links SRPX2 dysfunction to **abnormal neuronal migration and altered tubulin acetylation**, with preclinical evidence that pathway-targeted intervention (tubacin) can prevent downstream epileptiform activity in a rodent developmental model. (rudolf2009fromrolandicepilepsy pages 1-2, roll2010molecularnetworksimplicated pages 1-2, salmi2013tubacinpreventsneuronal pages 1-2)


## 1. Disease information
### 1.1 Concise overview
“SRPX2-related Speech–Epilepsy–Polymicrogyria Boundary” refers to a clinical continuum spanning **rolandic epilepsy with speech dyspraxia** (historically termed RESDX in the cited literature) and more overt **perisylvian cortical malformation phenotypes** (bilateral perisylvian PMG) with epilepsy and neurodevelopmental impairment. (rudolf2009fromrolandicepilepsy pages 1-2, bernardo2024xlinkedepilepsiesa pages 19-21)

### 1.2 Key identifiers (as available in retrieved evidence)
* **Gene:** SRPX2 (OMIM **300642**) (roll2010molecularnetworksimplicated pages 1-2)
* **Related clinical entities mentioned with OMIM IDs:**
  * Rolandic epilepsy–speech dyspraxia (OMIM **300643**) (roll2010molecularnetworksimplicated pages 1-2)
  * Bilateral perisylvian polymicrogyria (OMIM **300388**) (roll2010molecularnetworksimplicated pages 1-2)
* **OpenTargets disease identifiers returned in this run (aggregated resource):**
  * **MONDO_0015587:** rolandic epilepsy–speech dyspraxia syndrome (OpenTargets Search: -SRPX2)
  * **Orphanet 163721:** Rolandic epilepsy – speech dyspraxia (OpenTargets Search: -SRPX2)

**Not found in retrieved context:** ICD-10/ICD-11 codes, MeSH IDs, and a MONDO term explicitly corresponding to the user’s exact label (“speech-epilepsy-polymicrogyria boundary”).

### 1.3 Synonyms / alternative names (from evidence)
* Rolandic epilepsy–speech dyspraxia (RESDX / rolandic epilepsy–speech dyspraxia syndrome) (rudolf2009fromrolandicepilepsy pages 1-2, OpenTargets Search: -SRPX2)
* Bilateral perisylvian polymicrogyria (BPP) / bilateral peri-sylvian PMG (royer2007molecularevolutionof pages 2-3, bernardo2024xlinkedepilepsiesa pages 19-21)
* X-linked polymicrogyria gene association context (SRPX2 as a prominent X-linked PMG gene) (bernardo2024xlinkedepilepsiesa pages 19-21)

### 1.4 Evidence source type
The information summarized here is derived from a mix of:
* **Aggregated resources:** OpenTargets disease–gene associations (OpenTargets Search: -SRPX2)
* **Primary mechanistic research:** FOXP2→SRPX2/uPAR regulation (Human Molecular Genetics, 2010) and rodent in utero silencing/rescue studies (Brain, 2013) (roll2010molecularnetworksimplicated pages 1-2, salmi2013tubacinpreventsneuronal pages 1-2)
* **Clinical/genetics reviews:** epilepsy-aphasia/rolandic spectrum and X-linked PMG gene reviews (2009–2024) (rudolf2009fromrolandicepilepsy pages 1-2, bernardo2024xlinkedepilepsiesa pages 19-21)


## 2. Etiology
### 2.1 Disease causal factors
**Primary causal factor:** pathogenic variation in **SRPX2** (X-linked) in a subset of affected families, with phenotypes involving epilepsy and/or structural malformation of speech cortex. The Brain 2013 paper explicitly frames the prior human findings as: “**Two missense mutations in the sushi repeat-containing protein SRPX2 had been previously identified in epileptic disorders with or without structural developmental alteration of the speech cortex**.” (salmi2013tubacinpreventsneuronal pages 1-2)

**Important nuance:** the causal role of at least one reported missense variant (p.N327S) has been questioned due to co-inheritance with another missense change in most affected members of that family. (salmi2013tubacinpreventsneuronal pages 2-2)

### 2.2 Risk factors
* **Genetic risk factor:** SRPX2 missense variants reported in two families/case series, including **p.N327S** (rolandic epilepsy + verbal dyspraxia) and **p.Y72S** (bilateral perisylvian PMG), as summarized in the Brain 2013 study (which built a rodent model to assess consequences). (salmi2013tubacinpreventsneuronal pages 2-2)
* **Broader X-linked PMG context:** A 2024 narrative review places SRPX2 among the most frequently discussed X-linked PMG genes (with DDX3X and SRPX2 highlighted) and states SRPX2 was initially related to “**Rolandic seizures, ID, speech delay, oro-facial dyspraxia, and abnormalities in brain speech areas**.” (bernardo2024xlinkedepilepsiesa pages 19-21)

**Environmental risk factors / protective factors / gene–environment interactions:** Not specifically described in the retrieved SRPX2-focused context. (Evidence gap)


## 3. Phenotypes
### 3.1 Core phenotypes (qualitative, given limited frequency data in retrieved texts)
Below are key phenotypes supported by the retrieved literature; quantitative penetrance/frequency estimates for SRPX2-specific cohorts were not available in the extracted passages.

1) **Speech and language impairment / dyspraxia**
* Described as **speech delay**, **verbal/oral dyspraxia**, and **oro-facial dyspraxia**, often central to the syndrome designation. (rudolf2009fromrolandicepilepsy pages 1-2, bernardo2024xlinkedepilepsiesa pages 19-21)
* Suggested HPO terms (mapping suggestion; not asserted as extracted HPO annotations):
  * HP:0000750 Speech delay
  * HP:0002465 Dysarthria
  * HP:0011445 Oromotor apraxia
  * HP:0000738 Aphasia / language impairment (broad)

2) **Epilepsy (rolandic/centrotemporal focal seizures; spectrum overlap)**
* SRPX2 is linked to rolandic epilepsy with centrotemporal spikes in the broader rolandic/epilepsy-aphasia spectrum review context. (rudolf2009fromrolandicepilepsy pages 1-2)
* Suggested HPO terms:
  * HP:0001250 Seizures
  * HP:0002373 Febrile seizures (if present; not established in extracted SRPX2 passages)
  * HP:0020219 Centrotemporal spikes (EEG) (phenotype representation)

3) **Polymicrogyria / bilateral perisylvian polymicrogyria**
* A disease-associated SRPX2 mutation (Y72) is discussed in the context of “**rolandic seizures and bilateral perisylvian polymicrogyria**.” (royer2007molecularevolutionof pages 2-3)
* Suggested HPO terms:
  * HP:0002126 Polymicrogyria
  * HP:0002325 Bilateral perisylvian polymicrogyria

4) **Neurodevelopmental impairment / intellectual disability (variable)**
* A 2009 review states the rolandic epilepsy–speech dyspraxia presentation includes “**variable degrees of mental retardation**” (historical terminology). (rudolf2009fromrolandicepilepsy pages 1-2)
* Suggested HPO terms:
  * HP:0001249 Intellectual disability
  * HP:0001263 Global developmental delay

### 3.2 Age of onset, progression, severity
* In the rolandic epilepsy spectrum, seizures are typically **childhood-onset** and EEG features often activate in drowsiness/sleep, consistent with classic centrotemporal-spike epilepsies (review-level). (rudolf2009fromrolandicepilepsy pages 1-2)
* SRPX2 phenotypes range from epilepsy with **structurally normal MRI** in some reports to epilepsy with **perisylvian PMG** in others, consistent with a “boundary” phenotype spanning functional and malformative presentations. (rudolf2009fromrolandicepilepsy pages 1-2, salmi2013tubacinpreventsneuronal pages 1-2)

### 3.3 Quality-of-life impact
Direct QoL instrument data (EQ-5D/SF-36/PROMIS) were not identified in retrieved evidence; however, the clinical features (speech dyspraxia, epilepsy, PMG) are expected to significantly impact communication and daily functioning. (Evidence gap)


## 4. Genetic / molecular information
### 4.1 Causal gene
* **SRPX2** (sushi repeat containing protein X-linked 2; OMIM 300642). (roll2010molecularnetworksimplicated pages 1-2)

### 4.2 Pathogenic variants (from retrieved evidence)
* **SRPX2 p.N327S** — reported with rolandic epilepsy and verbal dyspraxia; causality questioned due to co-inheritance of another missense variant in most affected members. (salmi2013tubacinpreventsneuronal pages 2-2)
* **SRPX2 p.Y72S** — associated with bilateral perisylvian polymicrogyria; discussed near an evolutionarily interesting residue R75K in structural modeling of a sushi domain. (royer2007molecularevolutionof pages 2-3)

**Variant types in evidence:** missense variants. (salmi2013tubacinpreventsneuronal pages 2-2)

**Population allele frequencies / ClinVar classifications:** not available in retrieved context. (Evidence gap)

### 4.3 Functional consequences
Rodent model evidence supports a **loss-of-normal-developmental-function** interpretation:
* “**Wild-type, but not the mutant human SRPX2 proteins, rescued the neuronal migration phenotype caused by Srpx2 silencing in utero**” and increased alpha-tubulin acetylation. (salmi2013tubacinpreventsneuronal pages 1-2)

### 4.4 Modifier genes / epigenetics
Not established for SRPX2 in retrieved context.
* A 2024 X-linked epilepsy review emphasizes that “epigenetic regulation and X-chromosome inactivation” can complicate X-linked genotype–phenotype correlations generally, which is relevant to interpreting female carriers, but is not SRPX2-specific evidence in the extracted lines. (bernardo2024xlinkedepilepsiesa pages 22-23)


## 5. Environmental information
No SRPX2-specific environmental, lifestyle, toxin, or infectious contributors were identified in the retrieved texts. (Evidence gap)


## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic concepts
Two complementary mechanistic frames emerge from the retrieved evidence:

#### A) FOXP2 → SRPX2/uPAR transcriptional network (speech-related gene regulation)
* The 2010 Human Molecular Genetics study provides experimental evidence that FOXP2 represses SRPX2 and uPAR and links this to speech-related disorders and epilepsy/malformation contexts. It reports that FOXP2 transfection reduced SRPX2 transcripts by **43.6%** and uPAR transcripts by **38.6%**, and inhibited SRPX2 and uPAR promoter activity by ~**80.2%** and **77.5%**, respectively. (roll2010molecularnetworksimplicated pages 1-2)
* Mechanistic variants in FOXP2 demonstrate disruption of this repression:
  * FOXP2 p.R553H abolishes regulation/binding (roll2010molecularnetworksimplicated pages 5-7)
  * FOXP2 p.M406T shows significant loss of SRPX2 promoter repression and altered intracellular localization (roll2010molecularnetworksimplicated pages 5-7, roll2010molecularnetworksimplicated pages 7-9)

Suggested GO biological process terms (mechanism mapping suggestions):
* GO:0006355 regulation of transcription, DNA-templated
* GO:0007399 nervous system development

#### B) Neuronal migration defects and tubulin acetylation (developmental epilepsy mechanism)
The 2013 Brain study provides a causal chain in a developmental rodent model:
1) **Trigger:** in utero Srpx2 knockdown
2) **Upstream cellular process:** **abnormal neuronal migration** during cortical development
3) **Biochemical link:** altered **alpha-tubulin acetylation** (wild-type SRPX2 increases acetylation; mutant does not rescue) (salmi2013tubacinpreventsneuronal pages 1-2)
4) **Downstream electrophysiology:** “**spontaneous epileptiform activity**” recorded postnatally (salmi2013tubacinpreventsneuronal pages 1-2)
5) **Pharmacologic prevention in utero:** “**The neuronal migration defects and the post-natal epileptic consequences were prevented early in embryos by maternal administration of tubulin deacetylase inhibitor tubacin**.” (salmi2013tubacinpreventsneuronal pages 1-2)

Suggested GO terms:
* GO:0001764 neuron migration
* GO:0000226 microtubule cytoskeleton organization

Suggested cell types (CL term suggestions):
* CL:0000540 neuron
* CL:0000127 cortical neuron (more specific mapping as appropriate)

### 6.2 Expert interpretation (authoritative-source synthesis)
A 2024 review of X-linked epilepsies frames SRPX2 as a gene initially linked to rolandic seizures and language/oromotor phenotypes and places it among key X-linked PMG genes, supporting the view that SRPX2 sits at a boundary between **functional epilepsy-aphasia phenotypes** and **structural migration/cortical organization disorders**. (bernardo2024xlinkedepilepsiesa pages 19-21)


## 7. Anatomical structures affected
### 7.1 Organ/system level
* **Central nervous system**, especially **speech-related cortical regions** in the rolandic/perisylvian areas (review-level and mechanistic framing). (rudolf2009fromrolandicepilepsy pages 1-2, salmi2013tubacinpreventsneuronal pages 1-2)

### 7.2 Tissue/cell level
* **Developing cerebral cortex** with involvement of **neuronal migration** processes (rat in utero model). (salmi2013tubacinpreventsneuronal pages 1-2)

Suggested UBERON terms (mapping suggestions):
* UBERON:0000955 brain
* UBERON:0001870 cerebral cortex
* UBERON:0002771 frontal lobe operculum / perisylvian cortex (depending on ontology granularity)


## 8. Temporal development
* The rolandic epilepsy spectrum is described as childhood-onset with centrotemporal EEG features often activated by sleep/drowsiness (review-level). (rudolf2009fromrolandicepilepsy pages 1-2)
* The developmental mechanism is prenatal/early developmental: Srpx2 perturbation in utero produces migration defects with later postnatal epileptiform activity in the animal model. (salmi2013tubacinpreventsneuronal pages 1-2)


## 9. Inheritance and population
### 9.1 Inheritance
* SRPX2-related rolandic epilepsy–speech dyspraxia has been described as **X-linked** (RESDX) in review-level evidence. (rudolf2009fromrolandicepilepsy pages 1-2)
* A 2024 review notes SRPX2-associated PMG phenotypes have been observed to affect males, with the implication that skewed X-inactivation can modulate female phenotypes. (bernardo2024xlinkedepilepsiesa pages 19-21)

### 9.2 Epidemiology
No robust SRPX2-specific prevalence/incidence estimates were identified in the retrieved texts.

A relevant background statistic from a 2024 review (X-linked PMG, not SRPX2-specific): **epilepsy is observed in approximately 80% of X-linked PMG cases**. (bernardo2024xlinkedepilepsiesa pages 19-21)


## 10. Diagnostics
### 10.1 Clinical evaluation (real-world implementation)
SRPX2-related phenotypes lie at the intersection of epilepsy-aphasia spectrum and malformations of cortical development, suggesting a practical diagnostic approach:
* **EEG** to identify centrotemporal spikes / focal epileptiform patterns in rolandic epilepsy presentations (review-level). (rudolf2009fromrolandicepilepsy pages 1-2)
* **Brain MRI** to evaluate for **bilateral perisylvian polymicrogyria** and related cortical malformations where clinically indicated. The SRPX2 disease concept explicitly includes cases “with or without structural developmental alteration of the speech cortex.” (salmi2013tubacinpreventsneuronal pages 1-2)

### 10.2 Genetic testing
A PMG review recommends exploring genetic testing and notes challenges including de novo variants, mosaicism, and CNVs in PMG broadly; it explicitly includes SRPX2 in a suggested malformations-of-cortical-development gene panel. (james2022thegeneticlandscape pages 7-8)

In practice (inference consistent with review statements), SRPX2 evaluation is typically performed via:
* **NGS epilepsy and/or malformations-of-cortical-development panels** including SRPX2 (james2022thegeneticlandscape pages 7-8)
* **WES/WGS** when phenotype is broader or when panel testing is negative (review-level general recommendation in PMG). (james2022thegeneticlandscape pages 7-8)

### 10.3 Differential diagnosis (high-level)
Not systematically enumerated in retrieved context; however, SRPX2 sits within the set of genes implicated in PMG and epilepsy-aphasia spectrum. The 2024 X-linked epilepsy review highlights multiple X-linked PMG genes and emerging genes; SRPX2 is discussed among these. (bernardo2024xlinkedepilepsiesa pages 19-21)


## 11. Outcome / prognosis
SRPX2-specific long-term outcomes, mortality, and validated prognostic factors were not identified in the retrieved context.

Based on syndrome descriptions, disability burden is primarily driven by seizure control, degree of speech/oromotor impairment, and presence/extent of cortical malformation and intellectual disability (review-level). (rudolf2009fromrolandicepilepsy pages 1-2, bernardo2024xlinkedepilepsiesa pages 19-21)


## 12. Treatment
### 12.1 Current standard clinical management (real-world)
No SRPX2-specific controlled treatment studies were identified in retrieved texts.

For polymicrogyria broadly, a 2022 review summarizes real-world management as **symptomatic**:
* “**The first-line treatment for those with seizures is anti-seizure medications**.” (james2022thegeneticlandscape pages 7-8)
* Surgical candidacy may depend on lesion laterality/extent: unilateral focal PMG may be considered for resective surgery; bilateral PMG is generally not a good candidate for resection (review-level). (james2022thegeneticlandscape pages 7-8)
* Supportive therapies: “**Occupational therapy, physiotherapy, and speech therapy may help**” some affected individuals. (james2022thegeneticlandscape pages 7-8)

Suggested MAXO terms (mapping suggestions):
* MAXO:0000016 antiepileptic drug therapy
* MAXO:0000757 speech therapy
* MAXO:0000445 occupational therapy

### 12.2 Experimental / preclinical therapeutics
A key preclinical development is the 2013 Brain study showing in utero prevention of downstream epileptiform activity in a rodent model:
* “**The neuronal migration defects and the post-natal epileptic consequences were prevented… by maternal administration of tubulin deacetylase inhibitor tubacin**.” (salmi2013tubacinpreventsneuronal pages 1-2)

This is **not** a current human therapy, but it provides mechanistic support for targeting microtubule/tubulin acetylation pathways in SRPX2-related developmental epilepsy mechanisms.


## 13. Prevention
No established primary prevention exists beyond genetic counseling for families.

For PMG broadly, the 2022 review highlights the importance of **genetic testing and counseling** and notes that risk assessment depends on inheritance and the identified cause. (james2022thegeneticlandscape pages 7-8)


## 14. Other species / natural disease
No naturally occurring SRPX2-related disease in other species was identified in the retrieved context.


## 15. Model organisms
A mechanistically informative **rat in utero gene-silencing model** exists:
* Srpx2 silencing in utero produces neuronal migration defects and postnatal epileptiform activity, with rescue by wild-type human SRPX2 but not mutant SRPX2; tubacin prevents defects and epileptiform outcomes. (salmi2013tubacinpreventsneuronal pages 1-2)


## 2023–2024 “latest research” highlights (within retrieved evidence)
* **2024 (International Journal of Molecular Sciences; published Apr 2024; DOI: 10.3390/ijms25074110):** SRPX2 highlighted among principal X-linked PMG genes and linked to rolandic seizures, ID, speech delay, and orofacial dyspraxia. Provides review-level consolidation of SRPX2 positioning in X-linked PMG/epilepsy gene landscape. (bernardo2024xlinkedepilepsiesa pages 19-21)
* **2023 (International Journal of Developmental Neuroscience; published Aug 2023; DOI: 10.1002/jdn.10290):** broader context review on X-linked neuronal migration disorders, emphasizing limited epidemiologic data for neuronal migration disorders and the contribution of cortical malformations to refractory epilepsy. (edey2023x‐linkedneuronalmigration pages 5-6)

**Limitation:** No 2023–2024 primary SRPX2 case series or variant reclassification papers were successfully retrieved in the current tool run; therefore, recent patient counts, novel variants, and modern ACMG/ClinVar interpretations are not included here.


## Structured summary table
| Topic | Summary | Publication / year | PMID / identifier(s) | URL | Citation |
|---|---|---|---|---|---|
| Disease names / synonyms / identifiers | Evidence supports the SRPX2-associated disease spectrum including **Rolandic epilepsy–speech dyspraxia** / **RESDX** / **rolandic epilepsy-speech dyspraxia syndrome** and **bilateral perisylvian polymicrogyria (BPP)** / **congenital bilateral perisylvian syndrome**. OMIM numbers explicitly mentioned for **SRPX2 (OMIM 300642)**, **Rolandic epilepsy–speech dyspraxia (OMIM 300643)**, and **bilateral perisylvian polymicrogyria (OMIM 300388)**. Open Targets context lists **MONDO_0015587 rolandic epilepsy-speech dyspraxia syndrome** and **Orphanet 163721 Rolandic epilepsy - speech dyspraxia**. | Hum Mol Genet 2010; Open Targets context; IJMS review 2024 | PMID not shown in context for 2010 paper; MONDO_0015587; Orphanet 163721; OMIM 300642/300643/300388 | https://doi.org/10.1093/hmg/ddq415 | (roll2010molecularnetworksimplicated pages 1-2, OpenTargets Search: -SRPX2, bernardo2024xlinkedepilepsiesa pages 19-21) |
| Inheritance | Reported as an **X-linked** syndrome for SRPX2-related RESDX; females may show milder or variable manifestations, plausibly influenced by skewed X-inactivation. PMG literature notes familial PMG can be autosomal dominant, autosomal recessive, or X-linked, but the SRPX2 disorder specifically is X-linked in the cited syndrome reports. | Epilepsia 2009; IJMS review 2024; PMG review 2022 | PMID not shown in context | https://doi.org/10.1111/j.1528-1167.2009.02214.x ; https://doi.org/10.3390/ijms25074110 ; https://doi.org/10.4103/aian.aian_97_22 | (rudolf2009fromrolandicepilepsy pages 1-2, bernardo2024xlinkedepilepsiesa pages 19-21, james2022thegeneticlandscape pages 7-8) |
| Core phenotype: speech / oromotor | Recurrent phenotypes across reports/reviews include **speech delay**, **verbal/oral dyspraxia**, **oro-facial dyspraxia**, and language-cortex dysfunction. These features are central to the named syndrome and often accompany epilepsy; intellectual disability may be variable. | Epilepsia 2009; IJMS review 2024 | PMID not shown in context | https://doi.org/10.1111/j.1528-1167.2009.02214.x ; https://doi.org/10.3390/ijms25074110 | (rudolf2009fromrolandicepilepsy pages 1-2, bernardo2024xlinkedepilepsiesa pages 19-21) |
| Core phenotype: epilepsy | Seizures are typically **rolandic/centrotemporal** in the classic syndrome. Reviews connect SRPX2 to focal epilepsies of the rolandic/sylvian speech areas. In X-linked PMG broadly, **epilepsy is observed in ~80% of cases**. | Epilepsia 2009; IJMS review 2024 | PMID not shown in context | https://doi.org/10.1111/j.1528-1167.2009.02214.x ; https://doi.org/10.3390/ijms25074110 | (rudolf2009fromrolandicepilepsy pages 1-2, bernardo2024xlinkedepilepsiesa pages 19-21) |
| Core phenotype: cortical malformation | SRPX2 is also linked to **bilateral perisylvian polymicrogyria**, a developmental malformation of the speech cortex; reviews note SRPX2 among the principal X-linked PMG genes. | BMC Genet 2007; IJMS review 2024; PMG review 2022 | PMID not shown in context | https://doi.org/10.1186/1471-2156-8-72 ; https://doi.org/10.3390/ijms25074110 ; https://doi.org/10.4103/aian.aian_97_22 | (royer2007molecularevolutionof pages 2-3, bernardo2024xlinkedepilepsiesa pages 19-21, james2022thegeneticlandscape pages 7-8) |
| Key SRPX2 variants | Two historically emphasized **missense variants** are **p.N327S** (reported with rolandic epilepsy and verbal dyspraxia) and **p.Y72S** (reported with bilateral perisylvian polymicrogyria / rolandic seizures). The 2013 Brain study notes that the direct causal role of **p.N327S** has been questioned because of co-inheritance of another missense variant in most affected members. | Brain 2013; BMC Genet 2007 | PMID not shown in context | https://doi.org/10.1093/brain/awt161 ; https://doi.org/10.1186/1471-2156-8-72 | (salmi2013tubacinpreventsneuronal pages 2-2, royer2007molecularevolutionof pages 2-3, salmi2013tubacinpreventsneuronal pages 1-2) |
| FOXP2 network variants (mechanistic context) | **FOXP2 p.R553H** abolishes repression/binding effects on SRPX2/uPAR regulatory sites; **FOXP2 p.M406T** causes partial loss of nuclear localization and significant loss of SRPX2 promoter repression. These FOXP2 variants are mechanistic network findings rather than primary SRPX2 disease alleles. | Hum Mol Genet 2010 | PMID not shown in context | https://doi.org/10.1093/hmg/ddq415 | (roll2010molecularnetworksimplicated pages 7-9, roll2010molecularnetworksimplicated pages 5-7, roll2010molecularnetworksimplicated pages 1-2) |
| Mechanism: FOXP2 represses SRPX2/uPAR | FOXP2 directly down-regulates **SRPX2** and **uPAR**; reported quantitative effects include **43.6% reduction of SRPX2 transcripts**, **38.6% reduction of uPAR transcripts**, and inhibition of **SRPX2** and **uPAR** promoter activity by about **80.2%** and **77.5%**, respectively. This supports a FOXP2→SRPX2/uPAR speech-disorder network. | Hum Mol Genet 2010 | PMID not shown in context | https://doi.org/10.1093/hmg/ddq415 | (roll2010molecularnetworksimplicated pages 1-2) |
| Mechanism: neuronal migration / tubulin acetylation | In utero **Srpx2 silencing** in rat cortex causes **neuronal migration defects** and later **spontaneous epileptiform activity**. **Wild-type**, but **not mutant**, human SRPX2 rescues the migration phenotype and increases **alpha-tubulin acetylation**, linking SRPX2 dysfunction to cortical development. | Brain 2013 | PMID not shown in context | https://doi.org/10.1093/brain/awt161 | (salmi2013tubacinpreventsneuronal pages 1-2) |
| Mechanism / experimental rescue | Maternal treatment with the tubulin deacetylase inhibitor **tubacin** prevented both the migration abnormalities and postnatal epileptiform consequences in the rat model, providing proof-of-principle for pathway-targeted rescue in a developmental model. This remains **preclinical**, not a human standard of care. | Brain 2013 | PMID not shown in context | https://doi.org/10.1093/brain/awt161 | (salmi2013tubacinpreventsneuronal pages 1-2, salmi2013tubacinpreventsneuronal pages 2-2) |
| Recent review perspective (2023–2024) | Recent reviews continue to place SRPX2 among important **X-linked PMG** and **X-linked epilepsy** genes. The 2024 review states SRPX2 was initially related to **Rolandic seizures, ID, speech delay, oro-facial dyspraxia, and abnormalities in brain speech areas**; the 2023 review discusses X-linked neuronal migration disorders and emphasizes limited epidemiologic data overall. | Int J Mol Sci 2024; Int J Dev Neurosci 2023 | PMID not shown in context | https://doi.org/10.3390/ijms25074110 ; https://doi.org/10.1002/jdn.10290 | (bernardo2024xlinkedepilepsiesa pages 19-21, edey2023x‐linkedneuronalmigration pages 5-6) |


*Table: This table condenses the main disease names, identifiers, inheritance, phenotypes, variants, mechanisms, and key quantitative findings for the SRPX2-related speech-epilepsy-polymicrogyria spectrum. It is designed as a quick reference for integrating evidence from primary and recent review sources.*


## References (URLs in-text)
Primary and review sources used in this report are those retrieved in the current run and cited by context ID throughout (pqac-...). Key URLs include:
* Roll et al., Human Molecular Genetics (Dec 2010): https://doi.org/10.1093/hmg/ddq415 (roll2010molecularnetworksimplicated pages 1-2)
* Salmi et al., Brain (Aug 2013): https://doi.org/10.1093/brain/awt161 (salmi2013tubacinpreventsneuronal pages 1-2)
* Bernardo et al., Int J Mol Sci (Apr 2024): https://doi.org/10.3390/ijms25074110 (bernardo2024xlinkedepilepsiesa pages 19-21)
* James et al., Ann Indian Acad Neurol (Jul–Aug 2022): https://doi.org/10.4103/aian.aian_97_22 (james2022thegeneticlandscape pages 7-8)
* Rudolf et al., Epilepsia (Aug 2009): https://doi.org/10.1111/j.1528-1167.2009.02214.x (rudolf2009fromrolandicepilepsy pages 1-2)
* OpenTargets SRPX2 associations (accessed via tool): (OpenTargets Search: -SRPX2)


References

1. (rudolf2009fromrolandicepilepsy pages 1-2): Gabrielle Rudolf, Maria P. Valenti, Edouard Hirsch, and Pierre Szepetowski. From rolandic epilepsy to continuous spike‐and‐waves during sleep and landau‐kleffner syndromes: insights into possible genetic factors. Epilepsia, 50:25-28, Aug 2009. URL: https://doi.org/10.1111/j.1528-1167.2009.02214.x, doi:10.1111/j.1528-1167.2009.02214.x. This article has 108 citations and is from a domain leading peer-reviewed journal.

2. (roll2010molecularnetworksimplicated pages 1-2): Patrice Roll, Sonja C. Vernes, Nadine Bruneau, Jennifer Cillario, Magali Ponsole-Lenfant, Annick Massacrier, Gabrielle Rudolf, Manal Khalife, Edouard Hirsch, Simon E. Fisher, and Pierre Szepetowski. Molecular networks implicated in speech-related disorders: foxp2 regulates the srpx2/upar complex. Human molecular genetics, 19 24:4848-60, Dec 2010. URL: https://doi.org/10.1093/hmg/ddq415, doi:10.1093/hmg/ddq415. This article has 132 citations and is from a domain leading peer-reviewed journal.

3. (salmi2013tubacinpreventsneuronal pages 1-2): Manal Salmi, Nadine Bruneau, Jennifer Cillario, Natalia Lozovaya, Annick Massacrier, Emmanuelle Buhler, Robin Cloarec, Timur Tsintsadze, Françoise Watrin, Vera Tsintsadze, Céline Zimmer, Claude Villard, Daniel Lafitte, Carlos Cardoso, Lan Bao, Gaetan Lesca, Gabrielle Rudolf, Françoise Muscatelli, Vanessa Pauly, Ilgam Khalilov, Pascale Durbec, Yehezkel Ben-Ari, Nail Burnashev, Alfonso Represa, and Pierre Szepetowski. Tubacin prevents neuronal migration defects and epileptic activity caused by rat srpx2 silencing in utero. Brain : a journal of neurology, 136 Pt 8:2457-73, Aug 2013. URL: https://doi.org/10.1093/brain/awt161, doi:10.1093/brain/awt161. This article has 66 citations.

4. (bernardo2024xlinkedepilepsiesa pages 19-21): Pia Bernardo, Claudia Cuccurullo, Marica Rubino, Gabriella De Vita, Gaetano Terrone, Leonilda Bilo, and Antonietta Coppola. X-linked epilepsies: a narrative review. International Journal of Molecular Sciences, 25:4110, Apr 2024. URL: https://doi.org/10.3390/ijms25074110, doi:10.3390/ijms25074110. This article has 14 citations.

5. (OpenTargets Search: -SRPX2): Open Targets Query (-SRPX2, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (royer2007molecularevolutionof pages 2-3): Barbara Royer, Dinesh C Soares, Paul N Barlow, Ronald E Bontrop, Patrice Roll, Andrée Robaglia-Schlupp, Antoine Blancher, Anthony Levasseur, Pierre Cau, Pierre Pontarotti, and Pierre Szepetowski. Molecular evolution of the human srpx2 gene that causes brain disorders of the rolandic and sylvian speech areas. BMC Genetics, 8:72-72, Oct 2007. URL: https://doi.org/10.1186/1471-2156-8-72, doi:10.1186/1471-2156-8-72. This article has 36 citations.

7. (salmi2013tubacinpreventsneuronal pages 2-2): Manal Salmi, Nadine Bruneau, Jennifer Cillario, Natalia Lozovaya, Annick Massacrier, Emmanuelle Buhler, Robin Cloarec, Timur Tsintsadze, Françoise Watrin, Vera Tsintsadze, Céline Zimmer, Claude Villard, Daniel Lafitte, Carlos Cardoso, Lan Bao, Gaetan Lesca, Gabrielle Rudolf, Françoise Muscatelli, Vanessa Pauly, Ilgam Khalilov, Pascale Durbec, Yehezkel Ben-Ari, Nail Burnashev, Alfonso Represa, and Pierre Szepetowski. Tubacin prevents neuronal migration defects and epileptic activity caused by rat srpx2 silencing in utero. Brain : a journal of neurology, 136 Pt 8:2457-73, Aug 2013. URL: https://doi.org/10.1093/brain/awt161, doi:10.1093/brain/awt161. This article has 66 citations.

8. (bernardo2024xlinkedepilepsiesa pages 22-23): Pia Bernardo, Claudia Cuccurullo, Marica Rubino, Gabriella De Vita, Gaetano Terrone, Leonilda Bilo, and Antonietta Coppola. X-linked epilepsies: a narrative review. International Journal of Molecular Sciences, 25:4110, Apr 2024. URL: https://doi.org/10.3390/ijms25074110, doi:10.3390/ijms25074110. This article has 14 citations.

9. (roll2010molecularnetworksimplicated pages 5-7): Patrice Roll, Sonja C. Vernes, Nadine Bruneau, Jennifer Cillario, Magali Ponsole-Lenfant, Annick Massacrier, Gabrielle Rudolf, Manal Khalife, Edouard Hirsch, Simon E. Fisher, and Pierre Szepetowski. Molecular networks implicated in speech-related disorders: foxp2 regulates the srpx2/upar complex. Human molecular genetics, 19 24:4848-60, Dec 2010. URL: https://doi.org/10.1093/hmg/ddq415, doi:10.1093/hmg/ddq415. This article has 132 citations and is from a domain leading peer-reviewed journal.

10. (roll2010molecularnetworksimplicated pages 7-9): Patrice Roll, Sonja C. Vernes, Nadine Bruneau, Jennifer Cillario, Magali Ponsole-Lenfant, Annick Massacrier, Gabrielle Rudolf, Manal Khalife, Edouard Hirsch, Simon E. Fisher, and Pierre Szepetowski. Molecular networks implicated in speech-related disorders: foxp2 regulates the srpx2/upar complex. Human molecular genetics, 19 24:4848-60, Dec 2010. URL: https://doi.org/10.1093/hmg/ddq415, doi:10.1093/hmg/ddq415. This article has 132 citations and is from a domain leading peer-reviewed journal.

11. (james2022thegeneticlandscape pages 7-8): Jesmy James, Mary Iype, Mithran Omana Surendran, Ayyappan Anitha, and Sanjeev V. Thomas. The genetic landscape of polymicrogyria. Jul 2022. URL: https://doi.org/10.4103/aian.aian\_97\_22, doi:10.4103/aian.aian\_97\_22. This article has 14 citations and is from a peer-reviewed journal.

12. (edey2023x‐linkedneuronalmigration pages 5-6): Juliet Edey, Payam Soleimani‐Nouri, Amelia Dawson‐Kavanagh, Muhamad Saad Imran Azeem, and Vasso Episkopou. X‐linked neuronal migration disorders: gender differences and insights for genetic screening. International Journal of Developmental Neuroscience, 83:581-599, Aug 2023. URL: https://doi.org/10.1002/jdn.10290, doi:10.1002/jdn.10290. This article has 10 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](SRPX2-related_Speech_Epilepsy_Polymicrogyria-deep-research-falcon_artifacts/artifact-00.md)
