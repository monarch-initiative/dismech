---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T14:28:41.991130'
end_time: '2026-08-20T14:39:43.305588'
duration_seconds: 661.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: OPTN-related Open Angle Glaucoma
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 46
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 6
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: OPTN-related_Open_Angle_Glaucoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** OPTN-related Open Angle Glaucoma
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **OPTN-related Open Angle Glaucoma** covering all of the
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
- **Disease Name:** OPTN-related Open Angle Glaucoma
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **OPTN-related Open Angle Glaucoma** covering all of the
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


# OPTN-Related Open-Angle Glaucoma: Disease-Characteristics Research Report

## Executive summary

**OPTN-related open-angle glaucoma**—historically **GLC1E**—is a rare Mendelian form of open-angle glaucoma caused most convincingly by heterozygous pathogenic variation in **OPTN**, particularly **p.Glu50Lys (E50K)**. It usually manifests as adult-onset **normal-tension glaucoma (NTG)**: progressive retinal ganglion-cell (RGC) and optic-nerve degeneration, optic-disc cupping, retinal nerve-fiber-layer (RNFL) thinning, and corresponding visual-field loss despite untreated intraocular pressure (IOP) remaining below 21 mmHg. It should be distinguished from common, complex primary open-angle glaucoma (POAG), in which OPTN variants generally explain only a small fraction of disease. (trivli2020primaryopenangle pages 1-2, salvetat2023pharmaceuticalapproachesto pages 1-2, swarup2018alteredfunctionsand pages 1-3)

The evidence hierarchy is important. E50K has family segregation, cellular, animal-model, and human stem-cell evidence. By contrast, **M98K is better regarded as a population-dependent susceptibility/modifier allele**, and many other reported variants remain insufficiently validated. Current treatment is not genotype-specific: clinicians lower IOP even when it is statistically normal, monitor structural and functional progression, and escalate to laser or surgery when necessary. No approved OPTN-directed therapy or qualifying OPTN-specific interventional clinical trial was identified. (salvetat2023pharmaceuticalapproachesto pages 1-2, swarup2018alteredfunctionsand pages 1-3, sirohi2015aglaucomaassociatedvariant pages 1-2)

The following table provides a compact ontology-ready summary; the narrative below expands the evidence and identifies gaps.

| Domain | Curated statement | Suggested ontology IDs/terms | Evidence type/strength | Key source/date/PMID or DOI |
|---|---|---|---|---|
| Disease identity | OPTN-related open-angle glaucoma corresponds to the Mendelian glaucoma locus **GLC1E** and is best regarded as a **rare monogenic subset of open-angle glaucoma, often presenting as normal-tension glaucoma (NTG)** rather than a separate common POAG entity. **OMIM 137760 (GLC1E)** is commonly used in the literature; use the broader **MONDO:0005338 open-angle glaucoma** only as a parent term, with caution because a disease-specific MONDO for OPTN-related glaucoma was not confirmed here. | OMIM:137760 (GLC1E, use with caution if local curation confirms); MONDO:0005338 open-angle glaucoma (broader parent); MeSH/ICD disease mapping not verified in current context | Human genetic literature + review synthesis; moderate strength for GLC1E identity, lower strength for ontology cross-mapping gaps (OpenTargets Search: open-angle glaucoma-OPTN, trivli2020primaryopenangle pages 1-2, swarup2018alteredfunctionsand pages 1-3) | Rezaie et al. discovery paper cited in reviews; Trivli 2020 DOI:10.3892/mmr.2020.11215; Swarup 2018 DOI:10.3389/fimmu.2018.01287 |
| Source type | This knowledge-base entry should be based on **aggregated disease-level resources and published case/family studies**, not EHR-derived evidence. | ECO conceptually: literature evidence; disease knowledgebase curation | Curatorial statement; high confidence | Review/resource-based synthesis (trivli2020primaryopenangle pages 1-2, milla2024nextgenerationsequencingbasedgene pages 1-2) |
| Causal gene | **OPTN (optineurin)** is the causal gene implicated in GLC1E; it lies on **chromosome 10p13** and encodes a multifunctional adaptor involved in vesicle trafficking, autophagy, and signaling. | HGNC:17142 OPTN; Ensembl: ENSG00000123240; chromosomal location: 10p13 | Strong human genetic and molecular evidence (OpenTargets Search: open-angle glaucoma-OPTN, trivli2020primaryopenangle pages 1-2, swarup2018alteredfunctionsand pages 1-3) | Open Targets context for OPTN–open-angle glaucoma association; Trivli 2020 DOI:10.3892/mmr.2020.11215; Swarup 2018 DOI:10.3389/fimmu.2018.01287 |
| Inheritance | Inheritance is **autosomal dominant** for the clearest familial OPTN-associated disease, especially **E50K**; penetrance appears **age-dependent and incomplete/incompletely defined**. Reviews note segregation of E50K in affected individuals over ~30 years in a large family, while most other alleles have weaker evidence. | HPO inheritance term: HP:0000006 Autosomal dominant inheritance | Human family evidence; moderate for AD, limited for exact penetrance (swarup2018alteredfunctionsand pages 1-3, trivli2020primaryopenangle pages 1-2) | Swarup 2018 DOI:10.3389/fimmu.2018.01287; Trivli 2020 DOI:10.3892/mmr.2020.11215 |
| Variant spectrum | Reported glaucoma-associated OPTN variants are mostly **missense**. The **strongest disease-causing allele is p.Glu50Lys (E50K)**. Other reported variants include **M98K, H26D, H486R, E322K, R545Q** and others, but not all have equivalent evidence. | Sequence Ontology: SO:0001583 missense_variant | Human genetic + mechanistic literature; moderate overall, strongest for E50K (swarup2018alteredfunctionsand pages 1-3, rozpedekkaminska2020thegeneticand pages 26-28, venkatesan2025proteinmisfoldingand pages 8-9) | Swarup 2018 DOI:10.3389/fimmu.2018.01287; Rozpędek-Kamińska 2020 DOI:10.3390/ijms21114171; Venkatesan 2025 DOI:10.3389/fcell.2025.1595121 |
| Variant interpretation: E50K | **E50K** is the best-supported pathogenic OPTN glaucoma allele: dominant family segregation, repeated mechanistic support, and disease-recapitulating mouse/hPSC-RGC models. | HGVS protein: p.Glu50Lys; ClinVar classification not directly verified in current context | Strongest OPTN-specific evidence (human + animal + in vitro) (swarup2018alteredfunctionsand pages 1-3, nagabhushana2010regulationofendocytic pages 1-2, huang2024acquisitionofneurodegenerative pages 1-2) | Nagabhushana 2010 DOI:10.1186/1471-2121-11-4; Huang 2024 DOI:10.1186/s40478-024-01872-2; Swarup 2018 DOI:10.3389/fimmu.2018.01287 |
| Variant interpretation: M98K | **M98K** is best treated as a **disputed or population-dependent risk/modifier allele**, not a universally established monogenic pathogenic variant. Association appears stronger in some Asian cohorts and weaker/absent in others. | HGVS protein: p.Met98Lys; classify cautiously as risk allele/uncertain modifier unless lab-specific evidence supports pathogenicity | Mixed human association + mechanistic data; lower certainty than E50K (swarup2018alteredfunctionsand pages 1-3, sirohi2015aglaucomaassociatedvariant pages 1-2) | Swarup 2018 DOI:10.3389/fimmu.2018.01287; Sirohi 2015 DOI:10.1371/journal.pone.0138289 |
| Variant interpretation: H486R/R545Q/others | **H486R, R545Q, E322K and several other alleles** have been reported, but the current context does not provide enough evidence for definitive pathogenic classification, penetrance, or population frequency. | Use ACMG/AMP categories only after external verification; likely VUS/uncertain in this context | Limited evidence/data gap (rozpedekkaminska2020thegeneticand pages 26-28, swarup2018alteredfunctionsand pages 1-3) | Rozpędek-Kamińska 2020 DOI:10.3390/ijms21114171; Swarup 2018 DOI:10.3389/fimmu.2018.01287 |
| Epidemiology | OPTN mutations account for only a **small minority of POAG/NTG**, often cited around **~1% or less of sporadic NTG/POAG**, while Mendelian forms overall account for about **5% of POAG**. Disease prevalence for the specific OPTN-related entity is not established. | MONDO:0005338 parent disease epidemiology only; no disease-specific ORDO/MONDO confirmed | Human literature; moderate for rarity, low for exact prevalence (trivli2020primaryopenangle pages 1-2, swarup2018alteredfunctionsand pages 1-3) | Trivli 2020 DOI:10.3892/mmr.2020.11215; Swarup 2018 DOI:10.3389/fimmu.2018.01287 |
| Core phenotype | Typical phenotype is **adult-onset open-angle glaucomatous optic neuropathy**, often **normal-tension glaucoma** with optic disc cupping, RNFL loss, retinal ganglion cell degeneration, and progressive visual field loss despite IOP in the statistically normal range. | HPO: HP:0000505 Visual field defect; HP:0001138 Increased cup-to-disc ratio; HP:0007773 Optic atrophy; HP:0001103 Visual loss; HP:0000548 Abnormality of the optic nerve; parent glaucoma terms as local ontology allows | Human clinical + guideline/review evidence; strong for general NTG phenotype, moderate for OPTN-specific mapping (salvetat2023pharmaceuticalapproachesto pages 1-2, mallick2016updateonnormal pages 1-2, swarup2018alteredfunctionsand pages 1-3) | Salvetat 2023 DOI:10.3390/ph16081172; Mallick 2016 DOI:10.4103/2008-322X.183914; Swarup 2018 DOI:10.3389/fimmu.2018.01287 |
| Age of onset/course | Onset is usually **adult** and disease course is **chronic and progressive**. E50K familial disease showed age-dependent expression in adults; exact median onset for OPTN-specific disease remains insufficiently quantified here. | HPO: HP:0003581 Adult onset; HP:0003676 Progressive | Human family/review evidence; moderate (swarup2018alteredfunctionsand pages 1-3, salvetat2023pharmaceuticalapproachesto pages 1-2) | Swarup 2018 DOI:10.3389/fimmu.2018.01287; Salvetat 2023 DOI:10.3390/ph16081172 |
| IOP phenotype | A substantial subset of OPTN-related disease presents with **IOP consistently <21 mmHg**, i.e., NTG; however, some literature places OPTN within the broader POAG spectrum. | HPO suggestion: Normal intraocular pressure phenotype not confirmed in HPO here; clinical descriptor “normal-tension glaucoma” | Human clinical/review evidence; moderate (salvetat2023pharmaceuticalapproachesto pages 1-2, swarup2018alteredfunctionsand pages 1-3) | Salvetat 2023 DOI:10.3390/ph16081172; Swarup 2018 DOI:10.3389/fimmu.2018.01287 |
| Affected anatomy | Primary structures affected: **retina**, **retinal nerve fiber layer**, **optic nerve head**, **optic nerve**, and likely **trabecular meshwork** for some pathway interactions, though the major neurodegenerative target is the RGC/optic nerve axis. | UBERON: retina (UBERON:0000966); optic nerve (UBERON:0000978); optic nerve head (UBERON term should be externally verified); trabecular meshwork (UBERON term externally verify) | Human/animal/in vitro evidence; moderate-strong for retina/optic nerve, weaker for TM relevance (huang2024acquisitionofneurodegenerative pages 1-2, tsai2024glaucomaanimalmodels pages 1-2, trivli2020primaryopenangle pages 1-2) | Huang 2024 DOI:10.1186/s40478-024-01872-2; Tsai 2024 DOI:10.3390/ijms25020906; Trivli 2020 DOI:10.3892/mmr.2020.11215 |
| Cell types | Main vulnerable cells are **retinal ganglion cells (RGCs)**; secondary involvement includes **astrocytes/glia** and possibly **trabecular meshwork cells** in broader glaucoma biology. | CL:0000740 retinal ganglion cell; CL:0000127 astrocyte; trabecular meshwork cell CL term externally verify | Strong for RGCs, moderate for glia/TM (huang2024acquisitionofneurodegenerative pages 1-2, tsai2024glaucomaanimalmodels pages 1-2, swarup2018alteredfunctionsand pages 1-3) | Huang 2024 DOI:10.1186/s40478-024-01872-2; Tsai 2024 DOI:10.3390/ijms25020906; Swarup 2018 DOI:10.3389/fimmu.2018.01287 |
| Subcellular localization | Relevant subcellular compartments include **Golgi/recycling endosomes**, **autophagosomes/lysosomes**, and **mitochondria/mitophagy machinery**. | GO:0005794 Golgi apparatus; GO:0005768 endosome; GO:0005776 autophagosome; GO:0005764 lysosome; GO:0005739 mitochondrion | Strong mechanistic evidence (nagabhushana2010regulationofendocytic pages 1-2, huang2024acquisitionofneurodegenerative pages 1-2, venkatesan2025proteinmisfoldingand pages 6-7) | Nagabhushana 2010 DOI:10.1186/1471-2121-11-4; Huang 2024 DOI:10.1186/s40478-024-01872-2; Venkatesan 2025 DOI:10.3389/fcell.2025.1595121 |
| Major mechanism: trafficking | OPTN normally regulates **endocytic recycling/vesicle trafficking**; **E50K impairs transferrin receptor trafficking**, enlarges recycling endosomes, slows vesicle dynamics, and alters Rab8 interactions. | GO:0006897 endocytosis; GO:0006886 intracellular protein transport; GO:0032456 endocytic recycling; GO:0005515 protein binding; RAB8 pathway annotation as local pathway system allows | In vitro mechanistic evidence; strong (nagabhushana2010regulationofendocytic pages 1-2) | Nagabhushana 2010 DOI:10.1186/1471-2121-11-4 |
| Major mechanism: autophagy/mitophagy | OPTN is an **autophagy receptor**; glaucoma-associated mutants perturb **autophagic flux**, cargo sequestration, and **mitophagy**. TBK1-mediated phosphorylation enhances LC3 binding and selective autophagy functions. | GO:0006914 autophagy; GO:0000422 mitophagy; GO:0005776 autophagosome; GO:0016236 macroautophagy; GO:0000045 autophagosome assembly | Strong review + human cell evidence (venkatesan2025proteinmisfoldingand pages 6-7, huang2024acquisitionofneurodegenerative pages 1-2, swarup2018alteredfunctionsand pages 1-3) | Huang 2024 DOI:10.1186/s40478-024-01872-2; Swarup 2018 DOI:10.3389/fimmu.2018.01287; Venkatesan 2025 DOI:10.3389/fcell.2025.1595121 |
| Major mechanism: TBK1 axis | OPTN interacts with **TBK1**, a major partner in NTG biology. For E50K and M98K, altered TBK1 coupling/phosphorylation is implicated in autophagy-related retinal cell death. | GO:0006468 protein phosphorylation; GO:0032480 negative regulation of type I interferon production/innate immune pathways as context-dependent; pathway label “OPTN-TBK1 autophagy axis” | Strong mechanistic support; human genetics indirect, cell/animal strong (venkatesan2025proteinmisfoldingand pages 6-7, sirohi2015aglaucomaassociatedvariant pages 1-2, swarup2018alteredfunctionsand pages 1-3) | Sirohi 2015 DOI:10.1371/journal.pone.0138289; Swarup 2018 DOI:10.3389/fimmu.2018.01287 |
| Major mechanism: neurodegeneration | Downstream biology includes **RGC neurite retraction, protein accumulation, apoptosis/caspase activation, reactive gliosis, and optic nerve degeneration**. | GO:0043524 negative regulation of neuron apoptotic process (or apoptosis terms as appropriate); GO:0097458 neuron part morphogenesis; GO:0006915 apoptotic process; GO:0006954 inflammatory response | Strong in vitro/animal evidence (huang2024acquisitionofneurodegenerative pages 18-20, huang2023elucidatingcellularmechanisms pages 46-51, swarup2018alteredfunctionsand pages 1-3) | Huang 2024 DOI:10.1186/s40478-024-01872-2; Swarup 2018 DOI:10.3389/fimmu.2018.01287 |
| Signaling/metabolic mechanisms | Recent 2024 hPSC-RGC work links OPTN(E50K) to **impaired autophagic-lysosomal degradation**, **AMPK activation**, and **reduced mTORC1 signaling**; mTORC1 inhibition in control RGCs recapitulated disease features, while mTOR-independent autophagy induction was rescuing. | GO:0005773 vacuole/lysosome system; GO:0010506 regulation of autophagy; GO:0032008 positive regulation of TOR signaling / GO:0031929 TORC1 signaling; AMPK pathway terms via Reactome/GO locally | Strong recent human-cell evidence (huang2024acquisitionofneurodegenerative pages 1-2, huang2024acquisitionofneurodegenerative pages 18-20, huang2024acquisitionofneurodegenerative pages 14-16) | Huang 2024 DOI:10.1186/s40478-024-01872-2 |
| Inflammation/immune involvement | Neuroinflammation is increasingly implicated in NTG models; OPTN biology also intersects innate immune signaling. For OPTN(E50K), reactive gliosis and, in later literature, inflammasome activation are suggested, but OPTN-specific human evidence remains limited. | GO:0006954 inflammatory response; GO:0045087 innate immune response; CL astrocyte/microglia terms locally as needed | Moderate, mostly model/review-based (tsai2024glaucomaanimalmodels pages 1-2, swarup2018alteredfunctionsand pages 1-3) | Tsai 2024 DOI:10.3390/ijms25020906; Swarup 2018 DOI:10.3389/fimmu.2018.01287 |
| Risk factors beyond OPTN | General NTG risk factors likely modify disease expression: **older age, female sex, family history, vascular dysregulation, Raynaud phenomenon, migraine, nocturnal hypotension, myopia, smoking, systemic hypertension/impaired glucose tolerance**, and possibly sleep apnea. These are **not OPTN-specific** but clinically relevant modifiers. | HPO/ExO environmental annotations as local system allows; HP:0000822 hypertension; HP:0001279 migraine; myopia term if used locally | General NTG/POAG evidence, extrapolated to OPTN carriers with caution (mallick2016updateonnormal pages 1-2, salvetat2023pharmaceuticalapproachesto pages 1-2) | Mallick 2016 DOI:10.4103/2008-322X.183914; Salvetat 2023 DOI:10.3390/ph16081172 |
| Protective factors/data gaps | No well-established **OPTN-specific protective genetic variants** were identified in the current context. Lifestyle or metabolic neuroprotective strategies are experimental and not validated as preventive measures for OPTN carriers. | Data gap | Low/insufficient evidence | No definitive evidence in current context |
| Diagnosis | Diagnosis follows **standard NTG/POAG workup**: Goldmann applanation tonometry, gonioscopy, slit-lamp/fundus examination, OCT/RNFL imaging, and automated perimetry; importantly, clinicians must **exclude nonglaucomatous optic neuropathy** when cupping occurs with normal IOP. | LOINC/NCIT local mapping: tonometry, gonioscopy, OCT, perimetry; HPO phenotypes above | Strong guideline/review evidence for clinical workup; indirect for OPTN-specific diagnosis (salvetat2023pharmaceuticalapproachesto pages 1-2, mallick2016updateonnormal pages 1-2) | Salvetat 2023 DOI:10.3390/ph16081172; Mallick 2016 DOI:10.4103/2008-322X.183914 |
| Genetic testing | A practical approach is **multigene glaucoma panel testing** (including OPTN, MYOC, TBK1, WDR36, CYP1B1 and others) in familial/early-onset/NTG cases; recent NGS panel work supports molecular diagnosis but stresses need for segregation and functional follow-up for rare variants. | HGNC genes for panel: OPTN, MYOC, TBK1, WDR36, CYP1B1; sequence analysis | Human molecular diagnostics evidence; moderate (milla2024nextgenerationsequencingbasedgene pages 1-2, trivli2020primaryopenangle pages 1-2) | Milla 2024 DOI:10.1371/journal.pone.0282133; Trivli 2020 DOI:10.3892/mmr.2020.11215 |
| Differential diagnosis | Differential diagnosis includes **other causes of optic nerve cupping/optic neuropathy** rather than glaucoma alone, especially in normal-IOP presentations. | HPO optic atrophy spectrum; non-glaucomatous optic neuropathy terms locally | Guideline/review evidence; moderate (salvetat2023pharmaceuticalapproachesto pages 1-2) | Salvetat 2023 DOI:10.3390/ph16081172 |
| Prognosis | Disease is typically **progressive** and can lead to irreversible visual disability/blindness if untreated. Even with IOP lowering, some NTG patients continue to progress, implying non-IOP mechanisms. OPTN-specific long-term survival/mortality data are unavailable. | HPO: HP:0003676 Progressive; HP:0001103 Visual loss | Strong for progressive visual morbidity; low for OPTN-specific natural history estimates (salvetat2023pharmaceuticalapproachesto pages 1-2, mallick2016updateonnormal pages 1-2) | Salvetat 2023 DOI:10.3390/ph16081172; Mallick 2016 DOI:10.4103/2008-322X.183914 |
| Quality of life | Visual field loss and optic neuropathy reduce **visual function and quality of life**; glaucoma models/reviews emphasize impact on independence and psychological burden, but OPTN-specific QoL studies were not identified. | PROM/QoL terms not specifically mapped here | General glaucoma evidence; indirect for OPTN-specific disease (tsai2024glaucomaanimalmodels pages 1-2, salvetat2023pharmaceuticalapproachesto pages 1-2) | Tsai 2024 DOI:10.3390/ijms25020906; Salvetat 2023 DOI:10.3390/ph16081172 |
| Standard treatment | **No OPTN-specific approved therapy exists.** Management follows NTG/POAG care with **IOP lowering as standard of care**, even when baseline IOP is normal. Typical medical options include prostaglandin analogs, beta-blockers, alpha-agonists, carbonic anhydrase inhibitors; surgery is used when needed. | NCIT examples: prostaglandin analog therapy; trabeculectomy; laser trabeculoplasty; minimally invasive glaucoma surgery | Strong clinical standard-of-care evidence, indirect for genotype specificity (salvetat2023pharmaceuticalapproachesto pages 1-2, mallick2016updateonnormal pages 1-2, tsai2024glaucomaanimalmodels pages 1-2) | Salvetat 2023 DOI:10.3390/ph16081172; Mallick 2016 DOI:10.4103/2008-322X.183914; Tsai 2024 DOI:10.3390/ijms25020906 |
| Treatment targets | Reviews commonly cite a target of roughly **30% IOP reduction** in NTG management; this is a clinical principle extrapolated to OPTN-related disease, not a genotype-tested threshold. | Clinical management rule; no ontology term needed | General NTG evidence; indirect to OPTN (mallick2016updateonnormal pages 1-2, salvetat2023pharmaceuticalapproachesto pages 1-2) | Mallick 2016 DOI:10.4103/2008-322X.183914; Salvetat 2023 DOI:10.3390/ph16081172 |
| Experimental therapeutics | Preclinical work supports **TBK1-axis modulation**, **autophagy correction**, and **neuroprotective strategies**; in 2024 hPSC-RGCs, **trehalose** rescued neurite/protein-accumulation phenotypes via mTOR-independent autophagy induction. These remain experimental. | CHEBI: trehalose (local CHEBI mapping can be added); GO autophagy terms above | Strong preclinical, no clinical validation (huang2024acquisitionofneurodegenerative pages 1-2, huang2024acquisitionofneurodegenerative pages 18-20, sirohi2015aglaucomaassociatedvariant pages 1-2) | Huang 2024 DOI:10.1186/s40478-024-01872-2; Sirohi 2015 DOI:10.1371/journal.pone.0138289 |
| Animal models | Key models include **OPTN E50K knock-in/transgenic mice**, which show **RGC loss** and **reactive gliosis**, and are used as NTG-like models beyond IOP elevation. | NCBI Taxon:10090 Mus musculus; phenotype terms: RGC loss, gliosis | Strong model evidence (tsai2024glaucomaanimalmodels pages 1-2, swarup2018alteredfunctionsand pages 1-3) | Tsai 2024 DOI:10.3390/ijms25020906; Swarup 2018 DOI:10.3389/fimmu.2018.01287 |
| Human cellular models | **Isogenic hPSC-/iPSC-derived retinal ganglion cells carrying OPTN(E50K)** reproduce neurodegenerative phenotypes, autophagy defects, AMPK activation, mTORC1 reduction, protein accumulation, and neurite retraction; useful for mechanistic studies and drug screening. | CL:0000740 retinal ganglion cell; EFO/pluripotent stem cell terms locally | Strong recent human in vitro evidence (huang2024acquisitionofneurodegenerative pages 1-2, huang2024acquisitionofneurodegenerative pages 18-20, huang2024acquisitionofneurodegenerative pages 16-18) | Huang 2024 DOI:10.1186/s40478-024-01872-2 |
| Evidence gaps/curation cautions | Key gaps: no confirmed disease-specific MONDO ID in current context; limited penetrance estimates; uncertain pathogenicity for several non-E50K alleles; sparse allele-frequency data; minimal OPTN-specific prognosis/QoL/prevention data; many management statements are extrapolated from general NTG/POAG rather than genotype-stratified studies. | Curation flag: evidence gap/needs external verification | High-confidence curation caveat | Synthesized from all cited contexts (OpenTargets Search: open-angle glaucoma-OPTN, salvetat2023pharmaceuticalapproachesto pages 1-2, milla2024nextgenerationsequencingbasedgene pages 1-2, swarup2018alteredfunctionsand pages 1-3) |


*Table: This table summarizes ontology-ready core facts for OPTN-related open-angle glaucoma, separating well-supported evidence such as the E50K/GLC1E association from broader NTG extrapolations and unresolved data gaps. It is designed to support structured disease knowledge-base curation.*

---

## 1. Disease information

### Definition and scope

Glaucoma is a chronic progressive optic neuropathy defined by loss of RGC bodies and axons, RNFL thinning, characteristic optic-nerve-head cupping, and irreversible visual-field defects. NTG is the open-angle subtype in which glaucomatous structural and functional damage occurs without measured untreated IOP elevation. The 2023 Japanese definition cited in a recent review describes NTG as POAG in which IOP remains within the statistically normal range during development of glaucomatous optic neuropathy. (salvetat2023pharmaceuticalapproachesto pages 1-2)

For knowledge-base purposes, **OPTN-related open-angle glaucoma should be modeled as a rare genetic child of open-angle glaucoma/NTG**, not as synonymous with all NTG. Open Targets records an OPTN–open-angle-glaucoma association for **ENSG00000123240** and the broader disease **MONDO:0005338**, supported by five evidence records and literature including PMID **11834836**. (OpenTargets Search: open-angle glaucoma-OPTN)

### Identifiers and synonyms

- **Preferred name:** OPTN-related open-angle glaucoma
- **Common synonyms:** glaucoma 1, open-angle, E; **GLC1E**; optineurin-related glaucoma; OPTN-associated glaucoma; familial normal-tension glaucoma due to OPTN
- **Gene:** OPTN, optineurin; Ensembl **ENSG00000123240**; chromosome **10p13**. (OpenTargets Search: open-angle glaucoma-OPTN, trivli2020primaryopenangle pages 1-2)
- **OMIM:** **137760** is commonly used for GLC1E in secondary disease resources; confirm against the live OMIM record before production ingestion.
- **MONDO:** no disease-specific OPTN child identifier was verified by the available tools; use **MONDO:0005338, open-angle glaucoma**, as a parent rather than claiming it uniquely denotes OPTN disease. (OpenTargets Search: open-angle glaucoma-OPTN)
- **ICD-10-CM:** typically coded clinically under primary open-angle or low/normal-tension glaucoma, with eye and stage modifiers; there is no OPTN-genotype-specific ICD-10 code.
- **ICD-11/MeSH/Orphanet:** no genotype-specific identifier was verified in the retrieved evidence. Map to open-angle/normal-tension glaucoma and preserve OPTN as the molecular qualifier.

This report is based on **aggregated disease-level databases, published families, cohorts, reviews, and experimental models**, not individual EHR-derived observations.

### Landmark discovery

Rezaie and colleagues reported “Adult-onset primary open-angle glaucoma caused by mutations in optineurin” in *Science* on **8 February 2002**, DOI [10.1126/science.1066901](https://doi.org/10.1126/science.1066901), PMID **11834836**. Subsequent synthesis reports OPTN variants in 16.7% of the originally studied linked families, but only about 1% or less of sporadic NTG; thus the original family statistic must not be interpreted as population prevalence. E50K segregated with glaucoma in affected members older than approximately 30 years. (OpenTargets Search: open-angle glaucoma-OPTN, swarup2018alteredfunctionsand pages 1-3)

---

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The clearest etiology is a **heterozygous germline OPTN variant with dominant toxic or altered-function effects**, especially E50K. OPTN is a multifunctional cytoplasmic adaptor involved in Golgi integrity, endosomal trafficking, autophagy/mitophagy, and inflammatory signaling. Disease is principally a neurodegeneration of RGCs and their axons rather than an infectious, neoplastic, or primary metabolic disorder. (venkatesan2025proteinmisfoldingand pages 6-7, trivli2020primaryopenangle pages 1-2, swarup2018alteredfunctionsand pages 1-3)

### Genetic risk factors

- **E50K/p.Glu50Lys:** strongest causal evidence; dominant segregation and extensive functional/model support.
- **M98K/p.Met98Lys:** mechanistically active in experimental systems, but human association is stronger in some Asian populations and absent or weak in several Caucasian studies; curate as a risk/modifier allele unless case-level segregation and classification justify otherwise. (swarup2018alteredfunctionsand pages 1-3, sirohi2015aglaucomaassociatedvariant pages 1-2)
- **H26D, E322K, H486R, R545Q and other reported missense alleles:** evidence is heterogeneous and generally weaker than for E50K. Do not automatically label all as pathogenic. (rozpedekkaminska2020thegeneticand pages 26-28, venkatesan2025proteinmisfoldingand pages 8-9, swarup2018alteredfunctionsand pages 1-3)
- **Modifier/cognate pathway genes:** TBK1 is a strong mechanistic partner and an independent cause of familial NTG through copy-number gain; MYOC, WDR36 and CYP1B1 are relevant differential or panel genes. OPTN overexpression can increase endogenous MYOC in trabecular-meshwork cells, but a reproducible OPTN-specific modifier architecture has not been established. (trivli2020primaryopenangle pages 1-2)

### Environmental and systemic modifiers

No exposure is known to create the germline disorder. General NTG/POAG factors may affect penetrance or progression: age, family history, myopia, thin central cornea, vascular dysregulation, migraine, Raynaud phenomenon, nocturnal hypotension, excessive antihypertensive treatment, smoking, metabolic disease, and sleep apnea/hypoxic stress. These data are **extrapolated from general NTG**, not demonstrated OPTN-specific gene–environment interactions. (trivli2020primaryopenangle pages 1-2, mallick2016updateonnormal pages 1-2)

Mechanistically plausible interactions include oxidative stress, hypoxia/ischemia–reperfusion, and aging increasing autophagic and mitochondrial demand in already vulnerable OPTN-mutant RGCs. However, prospective carrier studies quantifying such interactions are lacking.

### Protective factors

No validated OPTN protective allele, diet, supplement, or lifestyle intervention is established. Avoidance of smoking, treatment of sleep apnea, review of excessive nocturnal blood-pressure reduction, and general cardiovascular health are reasonable clinical measures but are not proven to prevent OPTN glaucoma. Experimental autophagy-enhancing or metabolic interventions cannot yet be considered protective therapy.

---

## 3. Phenotypes

### Core manifestations

1. **Glaucomatous optic neuropathy**—clinical sign; chronic and progressive; commonly bilateral but potentially asymmetric. Suggested HPO: **Abnormality of the optic nerve (HP:0000587)** and **optic atrophy (HP:0000648; verify current HPO label/ID before ingestion)**.
2. **Optic-disc excavation/increased cup-to-disc ratio**—clinical sign detected by fundoscopy/OCT. Suggested HPO: **Increased cup-to-disc ratio (HP:0001138)**.
3. **RNFL thinning and RGC loss**—structural signs; progressive and irreversible. Suggested HPO: abnormal retinal morphology/RNFL thinning; use exact current HPO child after ontology validation.
4. **Visual-field defect**—functional sign, initially often arcuate, paracentral, or nasal-step loss; may advance to severe constriction. Suggested HPO: **Visual field defect (HP:0001123; validate current ID)**.
5. **Reduced vision/blindness**—late morbidity rather than an early symptom. Suggested HPO: **Visual impairment** and **blindness**.
6. **Normal untreated IOP**—laboratory/physiologic characteristic in the predominant NTG presentation, conventionally consistently **<21 mmHg**. (salvetat2023pharmaceuticalapproachesto pages 1-2, mallick2016updateonnormal pages 1-2)
7. **Open anterior-chamber angle**—gonioscopic sign required for classification as open-angle disease. (salvetat2023pharmaceuticalapproachesto pages 1-2, mallick2016updateonnormal pages 1-2)

### Onset, frequency, severity, and progression

Disease is generally **adult-onset, insidious, chronic, and progressive**. E50K expression was age-dependent in the landmark family, with segregation reported in affected people older than 30 years. Exact median onset, sex ratio, bilateral frequency, and phenotype-specific percentages have not been robustly established for molecularly confirmed OPTN cases. E50K has repeatedly been described as the most severe OPTN glaucoma allele, but quantitative genotype-specific natural-history datasets remain small. (swarup2018alteredfunctionsand pages 1-3, sirohi2015aglaucomaassociatedvariant pages 1-2)

Patients may be asymptomatic until substantial field loss occurs. Severity varies from mild structural damage to advanced, disabling visual-field loss and blindness. There is no episodic or relapsing-remitting pattern and no spontaneous restoration of dead RGCs.

### Quality of life

Loss of peripheral and central visual field affects mobility, driving, reading, fall risk, independence, and psychological well-being. The chronic threat of irreversible blindness and the burden of lifelong drops and surveillance further reduce quality of life. No EQ-5D, SF-36, PROMIS, or glaucoma-specific quality-of-life dataset restricted to OPTN carriers was identified. General glaucoma evidence should therefore be labeled indirect. (salvetat2023pharmaceuticalapproachesto pages 1-2, tsai2024glaucomaanimalmodels pages 1-2)

---

## 4. Genetic and molecular information

### Gene and protein

**OPTN** encodes a 577-amino-acid adaptor containing coiled-coil regions, an LC3-interacting region, a ubiquitin-binding domain and a C-terminal zinc finger. It is expressed in retina, brain and multiple other tissues and participates in vesicular trafficking, autophagy, mitophagy, innate immune signaling and cellular homeostasis. Relevant partners include TBK1, LC3, RAB8, myosin VI, TBC1D17, huntingtin and transferrin receptor. (venkatesan2025proteinmisfoldingand pages 6-7, swarup2018alteredfunctionsand pages 1-3, sirohi2015aglaucomaassociatedvariant pages 1-2)

### Pathogenic-variant curation

| Variant | Evidence-based interpretation | Functional consequence |
|---|---|---|
| **E50K, p.Glu50Lys** | Best-supported dominant pathogenic allele; family segregation plus animal and human-cell validation | Altered/misfolded oligomers, increased TBK1/RAB8 interactions, impaired endosomal recycling and autophagic-lysosomal clearance; RGC-selective degeneration (venkatesan2025proteinmisfoldingand pages 8-9, venkatesan2025proteinmisfoldingand pages 6-7, nagabhushana2010regulationofendocytic pages 1-2) |
| **M98K, p.Met98Lys** | Population-dependent susceptibility/modifier; not equivalent to E50K | Increased TBK1 activation and Ser177 phosphorylation, excessive autophagosome formation, transferrin-receptor degradation and autophagy-dependent retinal-cell death in vitro (swarup2018alteredfunctionsand pages 1-3, sirohi2015aglaucomaassociatedvariant pages 1-2) |
| **H26D, E322K, H486R, R545Q and others** | Reported associations; classification requires current ClinVar submission-level review, population frequency, segregation and functional evidence | Variable or incompletely established (rozpedekkaminska2020thegeneticand pages 26-28, venkatesan2025proteinmisfoldingand pages 8-9) |

Most reported glaucoma alleles are missense. The disease is germline, not somatic. Precise gnomAD/TOPMed frequencies and current ClinVar classifications could not be verified with the available tools and should not be inferred. Similarly, no recurrent pathogenic large chromosomal rearrangement at OPTN was established; TBK1 duplication is a separate NTG cause.

### Penetrance, modifiers, and epigenetics

Penetrance is **incomplete and age-dependent**, but no reliable numeric penetrance curve is available. Expressivity is variable. Anticipation, germline mosaicism, consanguinity effects, and a specific founder effect have not been established. No validated OPTN-specific DNA-methylation or histone-modification biomarker is available. Reported microRNA/long-noncoding-RNA changes in E50K mice are exploratory and not clinical epigenetic tests.

---

## 5. Environmental information

There is no infectious agent, toxin, radiation exposure, or occupational exposure known to be necessary or sufficient. General NTG literature implicates vascular insufficiency, disturbed autoregulation, nocturnal hypotension, vasospasm, transient hypoxia, oxidative stress and possibly sleep apnea. Smoking and high BMI have been associated with glaucoma-related traits, but neither is an OPTN-specific causal exposure. (mallick2016updateonnormal pages 1-2)

No vaccine or antimicrobial intervention is applicable.

---

## 6. Mechanism and pathophysiology

### Integrated causal chain

**Upstream trigger:** heterozygous mutant OPTN—most convincingly E50K—alters OPTN conformation, localization and partner binding.

**Intermediate cellular defects:**

1. **Vesicular trafficking failure.** In vitro, E50K enlarged recycling endosomes, slowed mutant vesicle dynamics, reduced transferrin uptake, enhanced association with RAB8/transferrin receptor and slowed RAB8 vesicles. The authors concluded: “The E50K mutant impairs trafficking at the recycling endosomes due to altered interactions with Rab8 and transferrin receptor.” DOI [10.1186/1471-2121-11-4](https://doi.org/10.1186/1471-2121-11-4), published January 2010. (nagabhushana2010regulationofendocytic pages 1-2)

2. **OPTN–TBK1/autophagy dysregulation.** TBK1 phosphorylates OPTN near its LC3-interacting region, enhancing cargo capture. E50K can enhance OPTN–TBK1 interaction and disturb RAB8 trafficking/autophagosome formation. M98K experimentally activates TBK1 and increases Ser177-dependent autophagosome formation and retinal-cell death; TBK1 knockdown or inhibition reduced these effects. (venkatesan2025proteinmisfoldingand pages 6-7, sirohi2015aglaucomaassociatedvariant pages 1-2)

3. **Autophagic-lysosomal failure and altered mitophagy.** OPTN normally links ubiquitinated cargo and damaged mitochondria to LC3-positive autophagosomes. E50K can reduce effective cargo clearance and promote protein accumulation, whereas M98K may drive maladaptive excessive autophagic degradation. Thus “more” versus “less” autophagy is context- and variant-dependent; autophagic flux, rather than static LC3 abundance, is the relevant measure. (venkatesan2025proteinmisfoldingand pages 8-9, huang2024acquisitionofneurodegenerative pages 1-2, sirohi2015aglaucomaassociatedvariant pages 1-2)

4. **Energy-stress signaling.** The major 2024 development was an isogenic human hPSC-RGC study. Its abstract states: “We identified an impairment of autophagic-lysosomal degradation and decreased mTORC1 signaling via activation of the stress sensor AMPK, along with subsequent neurodegeneration in OPTN(E50K) RGCs.” Pharmacologic mTORC1 inhibition produced disease-like changes in control RGCs, while mTOR-independent autophagy induction reduced protein accumulation and restored neurite outgrowth. *Acta Neuropathologica Communications*, **16 October 2024**, DOI [10.1186/s40478-024-01872-2](https://doi.org/10.1186/s40478-024-01872-2). (huang2024acquisitionofneurodegenerative pages 1-2)

5. **Mitochondrial dysfunction, oxidative stress and apoptosis.** Defective mitophagy permits damaged mitochondria, energetic failure and reactive-oxygen stress; downstream caspase activation, neurite retraction and RGC death follow. RGCs are especially vulnerable because of their long axons and high energetic demand. (venkatesan2025proteinmisfoldingand pages 8-9, huang2023elucidatingcellularmechanisms pages 46-51, tsai2024glaucomaanimalmodels pages 1-2)

6. **Glial/inflammatory amplification.** E50K mice display persistent reactive gliosis. General glaucoma models implicate microglia, astrocytes, innate immunity and oxidative/ischemic injury; direct OPTN-specific human inflammatory evidence remains limited. (tsai2024glaucomaanimalmodels pages 1-2, swarup2018alteredfunctionsand pages 1-3)

**Clinical endpoint:** progressive RGC somal and axonal loss → RNFL thinning and optic-disc cupping → corresponding visual-field loss → irreversible visual disability/blindness.

### Ontology suggestions

- **GO biological processes:** autophagy (**GO:0006914**), mitophagy (**GO:0000422**), autophagosome assembly (**GO:0000045**), endocytic recycling, intracellular vesicle-mediated transport, protein phosphorylation, apoptotic process (**GO:0006915**), inflammatory response (**GO:0006954**), response to oxidative stress (**GO:0006979**).
- **GO cellular components:** Golgi apparatus (**GO:0005794**), endosome (**GO:0005768**), autophagosome (**GO:0005776**), lysosome (**GO:0005764**), mitochondrion (**GO:0005739**).
- **Cell Ontology:** retinal ganglion cell (**CL:0000740**), astrocyte (**CL:0000127**); retinal microglial and trabecular-meshwork cell IDs should be checked against the current CL release.

### Molecular profiling and advanced technologies

The 2023 precursor hPSC-RGC work found **75 downregulated and 117 upregulated genes**, with changes involving protein clearance, trafficking and neurite outgrowth; mutant cells also showed LC3 accumulation, active caspase-3 elevation and increased excitability. (huang2023elucidatingcellularmechanisms pages 39-46, huang2023elucidatingcellularmechanisms pages 46-51)

The 2024 study used isogenic CRISPR-edited embryonic-stem-cell and patient-iPSC pairs, RGC differentiation, autophagy sensors, immunoblotting, microscopy and morphometry. Trehalose treatment restored neurite morphology and shifted LC3-II and pS6 toward control values; for example, reported treatment comparisons included **p=0.03** for LC3-II and **p=0.029** for pS6. (huang2024acquisitionofneurodegenerative pages 14-16, huang2023elucidatingcellularmechanisms pages 82-86, huang2024acquisitionofneurodegenerative pages 16-18)

No validated OPTN-specific clinical single-cell, spatial-transcriptomic, proteomic, metabolomic or lipidomic signature was identified. These remain research opportunities.

---

## 7. Anatomical structures affected

- **Organ:** eye; secondary extension along the central visual pathway may occur as a consequence of optic-nerve degeneration.
- **Primary tissues:** neural retina/RNFL, optic-nerve head including lamina region, and optic nerve.
- **Principal cell:** RGC; secondary reactive cells include astrocytes and microglia. Trabecular-meshwork cells are relevant to conventional POAG and OPTN/MYOC interactions, but E50K NTG is principally an RGC/optic-nerve disease. (trivli2020primaryopenangle pages 1-2, huang2024acquisitionofneurodegenerative pages 1-2, tsai2024glaucomaanimalmodels pages 1-2)
- **Suggested UBERON:** retina **UBERON:0000966**; optic nerve **UBERON:0000978**. Validate optic-nerve-head, RNFL and trabecular-meshwork child terms before ingestion.
- **Subcellular sites:** Golgi, recycling endosome, autophagosome, lysosome and mitochondrion.
- **Lateralization:** commonly bilateral, often asymmetric; robust OPTN-specific proportions are unavailable.

---

## 8. Temporal development

The typical course is adult-onset and insidious. A genetically susceptible RGC may compensate for decades before aging, metabolic demand, vascular stress or declining proteostasis crosses a threshold. Early disease consists of OCT/RNFL or optic-disc changes with little subjective impairment; intermediate disease shows reproducible field loss; advanced disease threatens fixation and functional independence. Disease is chronic and lifelong, with variable progression. (salvetat2023pharmaceuticalapproachesto pages 1-2, swarup2018alteredfunctionsand pages 1-3)

There is no spontaneous remission. IOP-lowering treatment can slow progression, but cannot restore dead RGCs. The critical intervention window is therefore **before substantial RNFL and field loss**, supporting cascade testing and surveillance of at-risk relatives.

---

## 9. Inheritance and population

### Inheritance

The best-established pattern is **autosomal dominant** with age-dependent, incomplete penetrance and variable expressivity. Each child of a heterozygous carrier has a 50% probability of inheriting the variant, although inheritance does not predict age of onset or severity. Genetic anticipation is not established. (swarup2018alteredfunctionsand pages 1-3)

### Epidemiology

A disease-specific prevalence or incidence per 100,000 has not been established. Reviews estimate that approximately **5% of all POAG is Mendelian**, whereas OPTN mutations explain approximately **1% or less of sporadic NTG** and around **1–2% of POAG** in some summaries. These estimates vary by ancestry, ascertainment and variant interpretation. (trivli2020primaryopenangle pages 1-2, swarup2018alteredfunctionsand pages 1-3, sirohi2015aglaucomaassociatedvariant pages 1-2)

For context—not OPTN-specific—NTG represents about **20–40% of POAG in Caucasian or African populations** and **47–92% in some Asian POAG series**. A 2023 review estimated NTG at **30–40% of all glaucoma cases**. These figures must not be used as OPTN prevalence. (salvetat2023pharmaceuticalapproachesto pages 1-2)

M98K association appears ancestry-dependent, stronger in some Asian datasets. No reliable carrier frequency, sex ratio, founder distribution, or geographic incidence for pathogenic E50K was identified. Consanguinity is not expected to be a major determinant of a dominant disorder.

---

## 10. Diagnostics

### Clinical diagnosis

A diagnosis requires evidence that the eye truly has glaucoma and that the angle is open, while excluding mimics. Core investigations are:

1. history, pedigree, medication and vascular-risk review;
2. repeated Goldmann applanation tonometry, preferably including diurnal assessment when indicated;
3. pachymetry because thin cornea can cause IOP underestimation;
4. gonioscopy confirming an open angle;
5. dilated stereoscopic optic-disc examination and photography;
6. OCT of peripapillary RNFL and macular ganglion-cell complex;
7. standard automated perimetry, repeated to establish a reproducible defect and progression;
8. selected blood-pressure monitoring, neuroimaging or neuro-ophthalmic assessment when the pattern is atypical. (salvetat2023pharmaceuticalapproachesto pages 1-2, mallick2016updateonnormal pages 1-2)

Direct abstract quote: “Goldmann applanation tonometry, gonioscopy, slit lamp biomicroscopy, optical coherence tomography and visual field analysis are the main tools of investigation for the diagnosis of NTG.” DOI [10.4103/2008-322X.183914](https://doi.org/10.4103/2008-322X.183914), published April 2016. (mallick2016updateonnormal pages 1-2)

### Genetic testing

A **multigene glaucoma panel** is generally preferable to isolated OPTN sequencing for familial NTG, early-onset disease, or a strong pedigree. At minimum, relevant genes include OPTN, TBK1 with deletion/duplication analysis, MYOC, WDR36 and CYP1B1, with broader validated panels adding other glaucoma/optic-neuropathy genes. Sanger confirmation and family segregation are particularly important for non-E50K findings.

A 2024 72-gene panel study found nine rare variants in **16% of 61 POAG patients**, distributed across CYP1B1, SIX6, CARD10, MFN1, OPTC, OPTN and WDR36. The authors cautioned that segregation and functional work are needed to establish contribution. *PLOS ONE*, **19 January 2024**, DOI [10.1371/journal.pone.0282133](https://doi.org/10.1371/journal.pone.0282133). (milla2024nextgenerationsequencingbasedgene pages 1-2)

- **Single-gene sequencing:** reasonable when a known familial OPTN variant is present.
- **Panel:** preferred first-line assay in genetically heterogeneous glaucoma.
- **WES/WGS:** useful when panel testing is negative in a strongly familial case; WGS may detect noncoding or structural variants but interpretation remains difficult.
- **CMA/karyotype/FISH:** not routine; targeted copy-number testing is more appropriate for TBK1.
- **Mitochondrial DNA and repeat-expansion testing:** not routine for classic OPTN glaucoma, but may be used for an alternative inherited optic-neuropathy phenotype.
- **RNA/proteomics/metabolomics/liquid biopsy:** research only.

### Differential diagnosis

Exclude ocular hypertension without neuropathy, high-tension POAG with missed peaks, angle-closure or secondary glaucoma, physiologic cupping, high-myopia-related disc changes, ischemic or compressive optic neuropathy, optic neuritis, hereditary optic atrophy (e.g., OPA1) and mitochondrial optic neuropathy. Atypical pallor exceeding cupping, marked color-vision loss, vertical-meridian field defects, rapid decline, pain, or neurologic signs should prompt neuro-ophthalmic investigation.

### Screening

There is no newborn screening. Offer **cascade variant testing and lifelong ophthalmic surveillance** to adult relatives when a pathogenic familial variant is known. A negative test for the familial variant substantially reduces that monogenic risk but does not eliminate ordinary population POAG risk.

---

## 11. Outcome and prognosis

OPTN glaucoma affects morbidity rather than general survival. No disease-specific mortality or reduced life expectancy is established. Visual prognosis depends on baseline damage, age, rate of RNFL/field loss, IOP achieved, adherence, vascular factors and treatment response.

Untreated progression can produce irreversible bilateral visual disability or blindness. Lowering IOP reduces risk but does not eliminate it, because OPTN-linked autophagic, mitochondrial and axonal mechanisms are not directly corrected. No validated molecular prognostic biomarker beyond genotype itself exists. E50K may signal a relatively severe phenotype, but current data do not support a precise individualized progression calculator. (salvetat2023pharmaceuticalapproachesto pages 1-2, swarup2018alteredfunctionsand pages 1-3)

Recovery of lost RGCs or established visual field is not expected with present care. Treatment aims to preserve remaining function.

---

## 12. Treatment

### Standard clinical management

There is **no approved OPTN-specific therapy**. Management follows NTG/POAG algorithms:

1. establish baseline structural and functional damage and an individualized target IOP;
2. lower IOP even if it begins in the normal range—often approximately **30% below untreated baseline**, commonly toward 12–14 mmHg when safely achievable;
3. reassess OCT, disc and visual fields and lower the target further if progression continues;
4. address adherence, drop technique, nocturnal hypotension and relevant systemic/vascular factors;
5. escalate to laser or surgery when drops are inadequate or poorly tolerated. (salvetat2023pharmaceuticalapproachesto pages 1-2, mallick2016updateonnormal pages 1-2)

### Pharmacotherapy

- **Prostaglandin analogues**—increase uveoscleral outflow; generally first-line.
- **Beta-blockers**—reduce aqueous production; monitor bradycardia, bronchospasm and nocturnal hypotension.
- **Alpha-2 agonists such as brimonidine**—reduce production and increase outflow.
- **Topical carbonic-anhydrase inhibitors**—reduce aqueous production.
- **Rho-kinase inhibitors**—increase trabecular outflow where approved.
- Fixed combinations may reduce bottle burden.

Suggested NCIt intervention concepts: pharmacologic IOP reduction, prostaglandin analogue therapy, beta-adrenergic antagonist therapy, carbonic-anhydrase inhibitor therapy and alpha-2 adrenergic agonist therapy; exact NCIt codes should be checked against the current release.

Adverse effects include ocular hyperemia/irritation, surface disease, prostaglandin-associated iris/periocular changes, beta-blocker cardiopulmonary effects and alpha-agonist allergy or fatigue. No OPTN pharmacogenomic dosing guideline exists.

### Laser and surgery

Selective laser trabeculoplasty can be considered when sufficient trabecular outflow reserve exists, although absolute pressure reduction may be limited at low baseline IOP. Trabeculectomy, tube surgery and selected minimally invasive glaucoma surgery are options when progression continues, but NTG requires careful balancing of very low target pressure against hypotony risk. (tsai2024glaucomaanimalmodels pages 1-2)

Suggested NCIt concepts: **laser trabeculoplasty**, **trabeculectomy**, **glaucoma drainage-device implantation**, and **minimally invasive glaucoma surgery**.

### Experimental precision therapies

- **Autophagy modulation:** in 2024 human E50K RGCs, mTOR-independent induction with trehalose reduced protein accumulation and restored neurite outgrowth. This is preclinical and does not justify clinical trehalose prescribing. (huang2024acquisitionofneurodegenerative pages 18-20, huang2024acquisitionofneurodegenerative pages 14-16)
- **TBK1 modulation:** TBK1 inhibition reduced M98K-driven autophagy/cell death in vitro, but systemic TBK1 has important immune functions, creating on-target safety concerns. (swarup2018alteredfunctionsand pages 1-3, sirohi2015aglaucomaassociatedvariant pages 1-2)
- **Mitochondrial/neuroprotective therapies:** antioxidants, metabolic support, caspase inhibition and regenerative RGC strategies remain experimental.
- **Gene replacement/editing, ASO/siRNA and cell replacement:** no validated OPTN clinical implementation. Dominant altered-function E50K may require allele-specific silencing or correction rather than simple gene addition.

The clinical-trial search returned no relevant OPTN-directed glaucoma interventional trial and no NCT identifier suitable for inclusion. This negative result should be periodically rechecked.

---

## 13. Prevention

### Primary prevention

The inherited allele cannot currently be prevented after conception. No vaccine, chemoprophylaxis or proven lifestyle program prevents disease in carriers. Reproductive options after counseling may include prenatal diagnosis or preimplantation genetic testing when a clearly pathogenic familial variant is known; these are individual choices, not treatment recommendations.

### Secondary prevention

This is the most actionable level: cascade genetic testing, periodic tonometry, gonioscopy, disc photography, OCT and perimetry can identify presymptomatic structural change and permit early pressure lowering. Testing should focus on a known familial pathogenic variant or use a validated panel when the familial cause is unknown.

### Tertiary prevention

Adherence to IOP-lowering treatment, serial progression analysis, low-vision referral when needed, fall-risk reduction, driving assessment and timely laser/surgery help prevent advanced disability. Review excessive nocturnal antihypertensive effects and treat relevant sleep or vascular disorders in coordination with the patient’s physician; evidence remains general NTG rather than OPTN-specific. (mallick2016updateonnormal pages 1-2)

---

## 14. Other species and natural disease

**Homo sapiens:** NCBI Taxon **9606**; human OPTN is the disease gene.

No well-established naturally occurring OPTN-related glaucoma syndrome in a companion-animal breed or wildlife population was identified. Accordingly, no VBO breed annotation, veterinary prevalence or zoonotic significance can be assigned. The disease is noninfectious and nontransmissible.

OPTN structure and autophagy functions are evolutionarily conserved, permitting mouse and vertebrate experimental modeling. This conservation is mechanistically valuable, but species differences in RGC subtype composition, optic-nerve anatomy and lifespan limit direct prediction of human penetrance and treatment response. (huang2024acquisitionofneurodegenerative pages 1-2, tsai2024glaucomaanimalmodels pages 1-2)

---

## 15. Model organisms and experimental systems

### Mouse models

- **E50K transgenic and knock-in mice, Mus musculus (Taxon 10090):** reproduce RGC loss, retinal/optic-nerve injury and reactive gliosis without requiring chronic IOP elevation; useful for NTG neurodegeneration, inflammation, autophagy and neuroprotection. (tsai2024glaucomaanimalmodels pages 1-2, swarup2018alteredfunctionsand pages 1-3)
- **Limitations:** expression level and promoter may not match the human heterozygous state; mice lack a human-like macula and have different RGC subtype distributions. Reviews emphasize that each glaucoma model captures only part of human disease. (tsai2024glaucomaanimalmodels pages 1-2)

### Human stem-cell models

Isogenic CRISPR-edited hESC/iPSC-derived RGCs carrying E50K are the strongest recent human model. They show normal initial RGC generation followed by smaller somata, reduced neurite complexity/length, altered excitability, OPTN/protein accumulation, impaired autophagic-lysosomal degradation, AMPK activation and reduced mTORC1 signaling. Correction or isogenic wild-type comparators reduce background-genome confounding. (huang2023elucidatingcellularmechanisms pages 39-46, huang2024acquisitionofneurodegenerative pages 1-2)

Their main applications are causal-pathway analysis, temporal profiling and phenotype-based drug screening. Limitations include developmental immaturity, absence of full lamina/vascular/immune architecture and incomplete modeling of decades-long aging.

### Conventional cell systems

HeLa and retinal-cell cultures have established trafficking and TBK1/autophagy mechanisms. However, the historical **RGC-5 line has identity and differentiation limitations**, and findings should be confirmed in primary RGCs, human isogenic RGCs or in vivo models. (swarup2018alteredfunctionsand pages 1-3, nagabhushana2010regulationofendocytic pages 1-2)

### Other induced models

Ocular-hypertension, optic-nerve-crush, ischemia–reperfusion, excitotoxic and autoimmune glaucoma models help dissect downstream injury but do not reproduce the initiating OPTN genotype. The 2024 hPSC study validated selected autophagy findings in a mouse ocular-hypertension model, supporting pathway convergence across genetic and pressure-mediated glaucoma. (huang2024acquisitionofneurodegenerative pages 14-16, tsai2024glaucomaanimalmodels pages 1-2)

---

## Evidence assessment and critical gaps

1. **High confidence:** OPTN is linked to GLC1E/open-angle glaucoma; E50K is the best-supported dominant allele; the core phenotype is frequently NTG; RGC/optic-nerve degeneration and trafficking/autophagy dysfunction are central.
2. **Moderate confidence:** E50K generally confers severe, age-dependent disease and TBK1/mitochondrial pathways materially contribute.
3. **Low or variant-dependent confidence:** pathogenicity of M98K, H486R, R545Q and many rare variants; precise penetrance; founder effects and ancestry-specific risk.
4. **Major missing data:** molecularly confirmed prevalence/incidence, prospective carrier natural history, allele-frequency tables, genotype-specific treatment response, quality-of-life measures, protective factors, clinical omics biomarkers and OPTN-directed trials.
5. **Curation rule:** do not transfer general NTG statistics or interventions into an OPTN-specific field without labeling them as extrapolated evidence.

### Selected primary and recent sources

- Rezaie T, et al. *Science*. **8 February 2002**. “Adult-onset primary open-angle glaucoma caused by mutations in optineurin.” PMID **11834836**; DOI: [10.1126/science.1066901](https://doi.org/10.1126/science.1066901). (OpenTargets Search: open-angle glaucoma-OPTN, swarup2018alteredfunctionsand pages 1-3)
- Nagabhushana A, et al. *BMC Cell Biology*. **January 2010**. E50K and endocytic recycling. DOI: [10.1186/1471-2121-11-4](https://doi.org/10.1186/1471-2121-11-4). (nagabhushana2010regulationofendocytic pages 1-2)
- Sirohi K, et al. *PLOS ONE*. **16 September 2015**. M98K–TBK1–Ser177/autophagy mechanism. DOI: [10.1371/journal.pone.0138289](https://doi.org/10.1371/journal.pone.0138289). (sirohi2015aglaucomaassociatedvariant pages 1-2)
- Salvetat ML, et al. *Pharmaceuticals*. **17 August 2023**. Current NTG treatment review. DOI: [10.3390/ph16081172](https://doi.org/10.3390/ph16081172). (salvetat2023pharmaceuticalapproachesto pages 1-2)
- Milla E, et al. *PLOS ONE*. **19 January 2024**. Adult-glaucoma NGS panel study. DOI: [10.1371/journal.pone.0282133](https://doi.org/10.1371/journal.pone.0282133). (milla2024nextgenerationsequencingbasedgene pages 1-2)
- Tsai T, et al. *International Journal of Molecular Sciences*. **11 January 2024**. Animal models beyond chronic IOP elevation. DOI: [10.3390/ijms25020906](https://doi.org/10.3390/ijms25020906). (tsai2024glaucomaanimalmodels pages 1-2)
- Huang KC, et al. *Acta Neuropathologica Communications*. **October 2024**. Isogenic OPTN(E50K) human RGCs, autophagy and mTORC1. DOI: [10.1186/s40478-024-01872-2](https://doi.org/10.1186/s40478-024-01872-2). (huang2024acquisitionofneurodegenerative pages 18-20, huang2024acquisitionofneurodegenerative pages 1-2)

References

1. (trivli2020primaryopenangle pages 1-2): Alexandra Trivli, Maria Zervou, George Goulielmos, Demetrios Spandidos, and Efstathios Detorakis. Primary open angle glaucoma genetics: the common variants and their clinical associations. Molecular Medicine Reports, 22:1103-1110, Jun 2020. URL: https://doi.org/10.3892/mmr.2020.11215, doi:10.3892/mmr.2020.11215. This article has 47 citations and is from a peer-reviewed journal.

2. (salvetat2023pharmaceuticalapproachesto pages 1-2): Maria Letizia Salvetat, Francesco Pellegrini, Leopoldo Spadea, Carlo Salati, and Marco Zeppieri. Pharmaceutical approaches to normal tension glaucoma. Pharmaceuticals, 16:1172, Aug 2023. URL: https://doi.org/10.3390/ph16081172, doi:10.3390/ph16081172. This article has 39 citations.

3. (swarup2018alteredfunctionsand pages 1-3): Ghanshyam Swarup and Zuberwasim Sayyad. Altered functions and interactions of glaucoma-associated mutants of optineurin. Frontiers in Immunology, Jun 2018. URL: https://doi.org/10.3389/fimmu.2018.01287, doi:10.3389/fimmu.2018.01287. This article has 86 citations and is from a peer-reviewed journal.

4. (sirohi2015aglaucomaassociatedvariant pages 1-2): Kapil Sirohi, Asha Kumari, Vegesna Radha, and Ghanshyam Swarup. A glaucoma-associated variant of optineurin, m98k, activates tbk1 to enhance autophagosome formation and retinal cell death dependent on ser177 phosphorylation of optineurin. PLOS ONE, 10:e0138289, Sep 2015. URL: https://doi.org/10.1371/journal.pone.0138289, doi:10.1371/journal.pone.0138289. This article has 54 citations and is from a peer-reviewed journal.

5. (OpenTargets Search: open-angle glaucoma-OPTN): Open Targets Query (open-angle glaucoma-OPTN, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (milla2024nextgenerationsequencingbasedgene pages 1-2): Elena Milla, Javier Laguna, Mª. Socorro Alforja, Beatriz Pascual, María José Gamundi, Emma Borràs, Imma Hernán, María Jesús Muniesa, Marta Pazos, Susana Duch, Miguel Carballo, and Meritxell Jodar. Next-generation sequencing-based gene panel tests for the detection of rare variants and hypomorphic alleles associated with primary open-angle glaucoma. PLOS ONE, 19:e0282133, Jan 2024. URL: https://doi.org/10.1371/journal.pone.0282133, doi:10.1371/journal.pone.0282133. This article has 6 citations and is from a peer-reviewed journal.

7. (rozpedekkaminska2020thegeneticand pages 26-28): Wioletta Rozpędek-Kamińska, Radosław Wojtczak, Jacek P. Szaflik, Jerzy Szaflik, and Ireneusz Majsterek. The genetic and endoplasmic reticulum-mediated molecular mechanisms of primary open-angle glaucoma. International Journal of Molecular Sciences, 21:4171, Jun 2020. URL: https://doi.org/10.3390/ijms21114171, doi:10.3390/ijms21114171. This article has 31 citations.

8. (venkatesan2025proteinmisfoldingand pages 8-9): Arunkumar Venkatesan and Audrey M. Bernstein. Protein misfolding and mitochondrial dysfunction in glaucoma. Frontiers in Cell and Developmental Biology, Apr 2025. URL: https://doi.org/10.3389/fcell.2025.1595121, doi:10.3389/fcell.2025.1595121. This article has 20 citations.

9. (nagabhushana2010regulationofendocytic pages 1-2): Ananthamurthy Nagabhushana, Madhavi L Chalasani, Nishant Jain, Vegesna Radha, Nandini Rangaraj, Dorairajan Balasubramanian, and Ghanshyam Swarup. Regulation of endocytic trafficking of transferrin receptor by optineurin and its impairment by a glaucoma-associated mutant. BMC Cell Biology, 11:4-4, Jan 2010. URL: https://doi.org/10.1186/1471-2121-11-4, doi:10.1186/1471-2121-11-4. This article has 133 citations.

10. (huang2024acquisitionofneurodegenerative pages 1-2): Kang-Chieh Huang, Cátia Gomes, Yukihiro Shiga, Nicolas Belforte, Kirstin B. VanderWall, Sailee S. Lavekar, Clarisse M. Fligor, Jade Harkin, Shelby M. Hetzer, Shruti V. Patil, Adriana Di Polo, and Jason S. Meyer. Acquisition of neurodegenerative features in isogenic optn(e50k) human stem cell-derived retinal ganglion cells associated with autophagy disruption and mtorc1 signaling reduction. Acta Neuropathologica Communications, Oct 2024. URL: https://doi.org/10.1186/s40478-024-01872-2, doi:10.1186/s40478-024-01872-2. This article has 10 citations and is from a peer-reviewed journal.

11. (mallick2016updateonnormal pages 1-2): Jyotiranjan Mallick, Lily Devi, PradeepK Malik, and Jogamaya Mallick. Update on normal tension glaucoma. Journal of Ophthalmic & Vision Research, 11:204-208, Apr 2016. URL: https://doi.org/10.4103/2008-322x.183914, doi:10.4103/2008-322x.183914. This article has 213 citations and is from a peer-reviewed journal.

12. (tsai2024glaucomaanimalmodels pages 1-2): Teresa Tsai, Sabrina Reinehr, Leonie Deppe, Alexandra Strubbe, Nils Kluge, H. Burkhard Dick, and Stephanie C. Joachim. Glaucoma animal models beyond chronic iop increase. International Journal of Molecular Sciences, 25:906, Jan 2024. URL: https://doi.org/10.3390/ijms25020906, doi:10.3390/ijms25020906. This article has 25 citations.

13. (venkatesan2025proteinmisfoldingand pages 6-7): Arunkumar Venkatesan and Audrey M. Bernstein. Protein misfolding and mitochondrial dysfunction in glaucoma. Frontiers in Cell and Developmental Biology, Apr 2025. URL: https://doi.org/10.3389/fcell.2025.1595121, doi:10.3389/fcell.2025.1595121. This article has 20 citations.

14. (huang2024acquisitionofneurodegenerative pages 18-20): Kang-Chieh Huang, Cátia Gomes, Yukihiro Shiga, Nicolas Belforte, Kirstin B. VanderWall, Sailee S. Lavekar, Clarisse M. Fligor, Jade Harkin, Shelby M. Hetzer, Shruti V. Patil, Adriana Di Polo, and Jason S. Meyer. Acquisition of neurodegenerative features in isogenic optn(e50k) human stem cell-derived retinal ganglion cells associated with autophagy disruption and mtorc1 signaling reduction. Acta Neuropathologica Communications, Oct 2024. URL: https://doi.org/10.1186/s40478-024-01872-2, doi:10.1186/s40478-024-01872-2. This article has 10 citations and is from a peer-reviewed journal.

15. (huang2023elucidatingcellularmechanisms pages 46-51): Kang-Chieh Huang. Elucidating cellular mechanisms underlying retinal ganglion cell neurodegeneration in a human pluripotent stem cell-derived model. Text, Jan 2023. URL: https://doi.org/10.25394/pgs.21585657.v1, doi:10.25394/pgs.21585657.v1. This article has 0 citations and is from a peer-reviewed journal.

16. (huang2024acquisitionofneurodegenerative pages 14-16): Kang-Chieh Huang, Cátia Gomes, Yukihiro Shiga, Nicolas Belforte, Kirstin B. VanderWall, Sailee S. Lavekar, Clarisse M. Fligor, Jade Harkin, Shelby M. Hetzer, Shruti V. Patil, Adriana Di Polo, and Jason S. Meyer. Acquisition of neurodegenerative features in isogenic optn(e50k) human stem cell-derived retinal ganglion cells associated with autophagy disruption and mtorc1 signaling reduction. Acta Neuropathologica Communications, Oct 2024. URL: https://doi.org/10.1186/s40478-024-01872-2, doi:10.1186/s40478-024-01872-2. This article has 10 citations and is from a peer-reviewed journal.

17. (huang2024acquisitionofneurodegenerative pages 16-18): Kang-Chieh Huang, Cátia Gomes, Yukihiro Shiga, Nicolas Belforte, Kirstin B. VanderWall, Sailee S. Lavekar, Clarisse M. Fligor, Jade Harkin, Shelby M. Hetzer, Shruti V. Patil, Adriana Di Polo, and Jason S. Meyer. Acquisition of neurodegenerative features in isogenic optn(e50k) human stem cell-derived retinal ganglion cells associated with autophagy disruption and mtorc1 signaling reduction. Acta Neuropathologica Communications, Oct 2024. URL: https://doi.org/10.1186/s40478-024-01872-2, doi:10.1186/s40478-024-01872-2. This article has 10 citations and is from a peer-reviewed journal.

18. (huang2023elucidatingcellularmechanisms pages 39-46): Kang-Chieh Huang. Elucidating cellular mechanisms underlying retinal ganglion cell neurodegeneration in a human pluripotent stem cell-derived model. Text, Jan 2023. URL: https://doi.org/10.25394/pgs.21585657.v1, doi:10.25394/pgs.21585657.v1. This article has 0 citations and is from a peer-reviewed journal.

19. (huang2023elucidatingcellularmechanisms pages 82-86): Kang-Chieh Huang. Elucidating cellular mechanisms underlying retinal ganglion cell neurodegeneration in a human pluripotent stem cell-derived model. Text, Jan 2023. URL: https://doi.org/10.25394/pgs.21585657.v1, doi:10.25394/pgs.21585657.v1. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](OPTN-related_Open_Angle_Glaucoma-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.