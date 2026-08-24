---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T15:28:52.144746'
end_time: '2026-08-20T15:40:11.552734'
duration_seconds: 679.41
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Adult Granulosa Cell Tumor of Ovary
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 8
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Adult_Granulosa_Cell_Tumor_of_Ovary-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Adult Granulosa Cell Tumor of Ovary
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Adult Granulosa Cell Tumor of Ovary** covering all of the
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
- **Disease Name:** Adult Granulosa Cell Tumor of Ovary
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Adult Granulosa Cell Tumor of Ovary** covering all of the
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


# Adult Granulosa Cell Tumor of the Ovary: Disease Characteristics Report

**Scope.** This report concerns **adult-type granulosa cell tumor (AGCT)**, not juvenile granulosa cell tumor. Evidence is disease-level and aggregated from cohorts, molecular studies, reviews, and ClinicalTrials.gov; it is **not derived from an individual patient/EHR**. Because AGCT is rare, most treatment evidence consists of retrospective series, small phase II studies, or case reports rather than phase III trials.

## Executive summary

AGCT is a rare, usually indolent but malignant ovarian sex cord–stromal tumor. It commonly presents around the peri-menopausal years, is frequently confined to one ovary at diagnosis, and may secrete estrogen, inhibin, and anti-Müllerian hormone (AMH). Its defining molecular event is the **somatic FOXL2 NM_023067.4:c.402C>G, p.(Cys134Trp)** variant, present in approximately 95–97% of tumors. Recurrence can occur decades after apparently curative surgery, making lifelong surveillance appropriate. Surgery is the principal treatment; evidence supporting adjuvant chemotherapy, endocrine treatment, or molecularly targeted therapy remains limited. (salkeni2024advancedgranulosacell pages 2-3, salkeni2024advancedgranulosacell pages 1-2, nemejcova2024anextensiveimmunohistochemical pages 1-2)

| domain | high-confidence finding | quantitative evidence | suggested ontology terms | evidence type/source year |
|---|---|---|---|---|
| identity/MONDO | Adult-type granulosa cell tumor (AGCT) is a rare ovarian sex cord-stromal malignancy and the dominant malignant granulosa-cell subtype; MONDO mapping in retrieved evidence points to ovarian granulosa cell tumor, while exact subtype mapping should be verified | AGCT comprises ~85–95% of granulosa cell tumors; ovarian granulosa cell tumors represent ~2–5% of ovarian tumors/cancers; incidence about 1 per 100,000 in the U.S. (salkeni2024advancedgranulosacell pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2) | Suggested: MONDO: ovarian granulosa cell tumor = MONDO_0023283; MONDO subtype for adult-type AGCT needs verification; MeSH/ICD/Ontology mapping needs verification | Human review 2024; systematic review 2023 (salkeni2024advancedgranulosacell pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2) |
| epidemiology | Usually diagnosed in adult/perimenopausal women; many cases present early stage | Median diagnosis age 46 years in review; typical age 50–55 years in large IHC cohort; 50–80% detected at FIGO IA (salkeni2024advancedgranulosacell pages 1-2, nemejcova2024anextensiveimmunohistochemical pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2) | Suggested: HP:0003596 Adult onset; NCIT: Perimenopausal; FIGO stage terms need verification | Human review/cohort 2023–2024 (salkeni2024advancedgranulosacell pages 1-2, nemejcova2024anextensiveimmunohistochemical pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2) |
| core phenotypes | Common manifestations include abdominal/pelvic symptoms and endocrine manifestations, but not all tumors are estrogenic | Iranian cohort: abdominal pain 56%; menopause in 69.2%; review notes up to 30% do not produce estrogen (salkeni2024advancedgranulosacell pages 2-3, salkeni2024advancedgranulosacell pages 1-2) | Suggested: HP:0002027 Abdominal pain; HP:0000132 Abnormality of female internal genitalia; HP:0000857 Menstrual irregularity; HP:0008222 Precocious puberty/endometrial effect terms may apply case-by-case and need verification | Human cohort/review 2024 (salkeni2024advancedgranulosacell pages 2-3, salkeni2024advancedgranulosacell pages 1-2) |
| anatomy | Primary site is ovary, arising from granulosa cells within sex cord-stromal tissue; recurrent/metastatic disease can involve abdomen/pelvis | Ovarian tumors in 81.3% of cohort; recurrences often abdominal in case literature; model tumors obliterate ovarian tissue (salkeni2024advancedgranulosacell pages 2-3, llano2023theoncogenicfoxl2 pages 3-4) | Suggested: UBERON:0000992 ovary; CL:0000501 granulosa cell; UBERON female gonad-associated stroma terms need verification | Human cohort 2024; mouse model 2023 (salkeni2024advancedgranulosacell pages 2-3, llano2023theoncogenicfoxl2 pages 3-4) |
| FOXL2 genomics | Somatic FOXL2 c.402C>G (p.C134W) is the central driver lesion in most AGCTs | Present in ~95–97% of AGCTs; 223/225 tested tumors positive in the 290-case IHC/molecular cohort; Open Targets links FOXL2 to ovarian granulosa cell tumor (salkeni2024advancedgranulosacell pages 2-3, salkeni2024advancedgranulosacell pages 1-2, nemejcova2024anextensiveimmunohistochemical pages 1-2, OpenTargets Search: adult granulosa cell tumor of ovary) | Suggested: HGNC:FOXL2; Sequence variant FOXL2 p.C134W; MONDO_0023283 association | Human cohort/review 2024; disease-target association resource (salkeni2024advancedgranulosacell pages 2-3, salkeni2024advancedgranulosacell pages 1-2, nemejcova2024anextensiveimmunohistochemical pages 1-2, OpenTargets Search: adult granulosa cell tumor of ovary) |
| secondary genomics | Recurrent secondary alterations occur in a subset, especially in recurrent/advanced disease, but AGCT remains genomically relatively homogeneous | Review of 423 samples: TERT promoter 56%, KMT2D 16.8%, CDKN2A/B deletions 10.2%, TP53 8.3%, MTAP deletion 5.8%, PIK3CA 5.4%; independent 93-case study: KMT2D 10/93 (10.8%); whole-genome study found chromosome 12 and 14 gain and chromosome 22 loss; TP53-mutant high-grade subgroup in 3 patients (salkeni2024advancedgranulosacell pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2, salkeni2024advancedgranulosacell pages 6-7) | Suggested: HGNC:TERT, KMT2D, CDKN2A, CDKN2B, TP53, MTAP, PIK3CA; CNV gain chr12/14, loss chr22; NCIT somatic mutation/CNV terms | Human genomic studies/review 2020–2024 (salkeni2024advancedgranulosacell pages 1-2, salkeni2024advancedgranulosacell pages 6-7, jung2023immunohistochemicalmarkersof pages 1-2) |
| pathways | Strongest mechanistic support centers on FOXL2-mutant interaction with TGFβ/SMAD signaling; PI3K/AKT and hormone signaling are also implicated | FOXL2C134W binds SMAD4/SMAD2/3 and induces EMT-like gene expression; mouse FOXL2 C134W tumors showed transcriptomic changes consistent with gain-of-function affecting TGFβ signaling; recurrent tumors altered LHCGR, INSL3, CYP19A1 and showed immune/hormone pathway enrichment (llano2023theoncogenicfoxl2 pages 11-12, khlebus2023comparativetumormicroenvironment pages 1-2, khlebus2023comparativetumormicroenvironment pages 10-10) | Suggested GO: TGF-beta receptor signaling pathway; epithelial to mesenchymal transition; PI3K-AKT signaling; steroid hormone biosynthetic process; CL granulosa cell/fibroblast/macrophage | Human mechanistic study 2020; mouse causal model 2023; human transcriptomics 2023 (llano2023theoncogenicfoxl2 pages 11-12, khlebus2023comparativetumormicroenvironment pages 1-2, khlebus2023comparativetumormicroenvironment pages 10-10) |
| pathology/IHC | Diagnosis relies on morphology plus sex cord-stromal markers; large 2024 cohort defines a practical immunophenotype | In 290 AGCTs: SF1 100%, FOXL2 98%, PR 94%, CD99 90%, AR 82%, inhibin A 78%, calretinin 45%, ER 41%; PD-L1 uniformly negative; HER2 negative; p53 aberrant in 1%; CTLA4 ~70% (nemejcova2024anextensiveimmunohistochemical pages 1-2) | Suggested: NCIT Immunohistochemistry; HGNC/NCIT markers SF1/NR5A1, FOXL2, PR/PGR, AR, CD99, INHA, CALB2, ESR1, CTLA4, PD-L1/CD274, HER2/ERBB2 | Human pathology cohort 2024 (nemejcova2024anextensiveimmunohistochemical pages 1-2) |
| biomarkers | Inhibin and AMH are the best-supported circulating biomarkers for diagnosis/follow-up; endocrine activity is variable | Review: inhibin A/B produced in almost all patients and correlates with disease activity; AMH sensitivity 89% and specificity 93%; up to 30% of tumors are non-estrogenic (salkeni2024advancedgranulosacell pages 2-3) | Suggested: CHEBI/NCIT inhibin A, inhibin B, anti-Mullerian hormone, estradiol; LOINC assay mappings need verification | Human review 2024 (salkeni2024advancedgranulosacell pages 2-3) |
| imaging/diagnostics | MRI often shows cystic, solid, or cystic-solid ovarian masses with hemorrhagic features; pathology confirmation remains required | 10-case AGCT with normal estrogen: ages 28–81, mean 54±16; metastatic lesions all cystic; described “honeycomb” and “Swiss cheese” signs; high DWI signal in solid components (khlebus2023comparativetumormicroenvironment pages 2-3, salkeni2024advancedgranulosacell pages 2-3) | Suggested: NCIT Magnetic Resonance Imaging; RadLex ovarian mass/cystic lesion terms need verification | Human imaging series 2024 (source retrieved in search results; no citeable context ID available) |
| natural history/prognosis | Prognosis is often favorable initially but late recurrence is a defining feature; very long follow-up is needed | Recurrence about 20% in reviews; one-third relapse between 4–8 years in 2021 review; latency typically 5–10 years and can exceed 20 years; recurrence rates across series 10–64%; average relapse 48–57 months; 10-year survival ~90% stage I vs 17–33% stage III–IV (salkeni2024advancedgranulosacell pages 2-3, salkeni2024advancedgranulosacell pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2) | Suggested: NCIT recurrent neoplasm; HP recurrent ovarian neoplasm term needs verification; FIGO stage ontology terms need verification | Human reviews 2021–2024 (salkeni2024advancedgranulosacell pages 2-3, salkeni2024advancedgranulosacell pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2) |
| prognostic factors | Prognostic biomarker evidence is limited and heterogeneous; some IHC markers correlate with worse outcomes | Review found worse prognosis associated with CD56, GATA-4, and SMAD3 expression; ER, AMH, and inhibin were not prognostic; Ki-67, p53, β-catenin, HER2 inconsistent (jung2023immunohistochemicalmarkersof pages 8-9, jung2023immunohistochemicalmarkersof pages 1-2) | Suggested: HGNC/NCIT NCAM1(CD56), GATA4, SMAD3, MKI67, TP53, CTNNB1, ERBB2 | Systematic review 2023 (jung2023immunohistochemicalmarkersof pages 8-9, jung2023immunohistochemicalmarkersof pages 1-2) |
| standard treatments | Surgery is the cornerstone; systemic therapy is used for advanced/recurrent disease, but evidence is mostly retrospective/small-series | Review notes surgery is standard; CAP response rate 60% and PVB 66% in small series; systemic chemotherapy remains standard for advanced disease (salkeni2024advancedgranulosacell pages 2-3, salkeni2024advancedgranulosacell pages 1-2) | Suggested NCIT: Oophorectomy, Hysterectomy, Cytoreductive Surgery, Adjuvant Chemotherapy, Cyclophosphamide, Doxorubicin, Cisplatin, Vinblastine, Bleomycin, Etoposide, Paclitaxel, Carboplatin | Human review 2024; historical clinical evidence summarized therein (salkeni2024advancedgranulosacell pages 2-3, salkeni2024advancedgranulosacell pages 1-2) |
| endocrine/targeted therapy | Hormonal and precision approaches are increasingly used in recurrent disease; evidence remains early | Review reports long partial responses with temozolomide+TRC102 (>12 months in 2 AGCT patients) and paclitaxel+nilotinib (>5 years in 2 AGCT patients); JNK inhibition reduced growth in patient-derived xenografts; TILs from 11 patients showed 100% autologous tumor reactivity and 57% reactivity to FOXL2 peptides in vitro (salkeni2024advancedgranulosacell pages 6-7) | Suggested NCIT: Aromatase inhibitor, letrozole, exemestane, leuprolide acetate, temozolomide, nilotinib, JNK inhibitor, tumor-infiltrating lymphocyte therapy | Human review 2024 summarizing case/preclinical evidence (salkeni2024advancedgranulosacell pages 6-7) |
| experimental trials | Multiple modern interventional studies are testing endocrine, NOTCH/gamma-secretase, and TGFβ/activin-axis strategies | NCT06169124 phase 2 darolutamide + leuprolide acetate + exemestane, active-not-recruiting, planned n=17; NCT05872204 phase 2 abemaciclib + letrozole, recruiting, planned n=100 rare ER+ ovarian cancers; NCT05348356 phase 2 nirogacestat, completed, n=53, 150 mg BID; NCT06254781 luspatercept single-patient completed study, n=1 (NCT06254781 chunk 1, NCT05348356 chunk 1) | Suggested NCIT: Clinical Trial, Darolutamide, Leuprolide Acetate, Exemestane, Abemaciclib, Letrozole, Nirogacestat, Luspatercept | ClinicalTrials.gov evidence 2022–2025 (NCT06254781 chunk 1, NCT05348356 chunk 1) |
| prevention | No established primary prevention or population screening strategy is supported by retrieved evidence; management focuses on surveillance after treatment | No validated population screening biomarker or prevention intervention identified in gathered evidence; long-term follow-up emphasized because relapse may occur decades later (salkeni2024advancedgranulosacell pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2) | Suggested NCIT: Surveillance, Follow-Up; secondary prevention/screening mappings need verification | Human reviews 2023–2024 (salkeni2024advancedgranulosacell pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2) |
| environmental/inherited risks | Evidence for environmental causes, protective factors, or common hereditary predisposition is currently limited/unclear in retrieved data | No consistent environmental risk factor identified in gathered evidence; AGCT is primarily characterized as a somatic FOXL2-driven neoplasm; isolated hereditary reports exist for sex cord-stromal tumors but not enough for routine AGCT risk assignment here (salkeni2024advancedgranulosacell pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2) | Suggested: Etiology unknown/nonhereditary in most cases; germline predisposition terms need verification | Review-level evidence; evidence gap noted (salkeni2024advancedgranulosacell pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2) |
| tumor microenvironment | Recurrent AGCT shows stromal depletion and myeloid enrichment, suggesting relapse-associated microenvironment remodeling | 24 tumors analyzed (8 primary, 16 recurrent); 31 DEGs; recurrent tumors had increased neutrophils/macrophages and decreased CAFs/endothelial cells; CAF depletion validated in independent datasets (khlebus2023comparativetumormicroenvironment pages 2-3, khlebus2023comparativetumormicroenvironment pages 9-10, khlebus2023comparativetumormicroenvironment pages 1-2) | Suggested GO/CL: macrophage, neutrophil, endothelial cell, fibroblast/cancer-associated fibroblast, hormone signaling, immune response | Human transcriptomic/TME study 2023 (khlebus2023comparativetumormicroenvironment pages 2-3, khlebus2023comparativetumormicroenvironment pages 9-10, khlebus2023comparativetumormicroenvironment pages 1-2) |
| models | The best current causal model is the Foxl2 C134W knock-in mouse; additional PI3K/PTEN/FOXO and other models support pathway biology but do not fully recapitulate human AGCT | In Foxl2+/C134W mice, all females developed ovarian tumors before 18 months; 50% of mutant females produced offspring after 6 months with WT males; primordial follicles markedly reduced; no recurrent driver beyond C134W identified in tumors; review of models notes existing mouse models do not completely recapitulate human molecular phenotype (llano2023theoncogenicfoxl2 pages 3-4, llano2023theoncogenicfoxl2 pages 2-3, llano2023theoncogenicfoxl2 pages 3-3, liu2015foxo13andpten pages 1-2) | Suggested: NCBITaxon:10090 mouse; CL granulosa cell; GO TGF-beta signaling, follicle development, PI3K-AKT signaling | Mouse causal model 2023; prior mouse model review 2015 (llano2023theoncogenicfoxl2 pages 3-4, llano2023theoncogenicfoxl2 pages 2-3, llano2023theoncogenicfoxl2 pages 3-3, liu2015foxo13andpten pages 1-2) |


*Table: This compact table summarizes high-confidence, evidence-backed facts for adult-type ovarian granulosa cell tumor across disease identity, biology, diagnosis, prognosis, treatment, and models. It is designed for rapid knowledge-base population and flags ontology mappings that need verification.*

## 1. Disease information

### Definition and classification

AGCT is a malignant neoplasm showing granulosa-cell differentiation and belongs to the ovarian **sex cord–stromal tumor** family. Adult-type tumors constitute approximately 85–95% of granulosa cell tumors and about 90% of malignant ovarian sex cord–stromal tumors; estimates of their share of all ovarian tumors or cancers range from roughly 1–5%, depending on the denominator and registry. The estimated U.S. incidence is approximately **1 per 100,000 women per year**. (salkeni2024advancedgranulosacell pages 1-2, nemejcova2024anextensiveimmunohistochemical pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2)

**Suggested identifiers and terminology**

- **MONDO:** MONDO:0023283, *ovarian granulosa cell tumor*; MONDO:0006036 is the broader *granulosa cell tumor*. A dedicated adult-type child term should be verified in the target ontology release. Open Targets maps ovarian granulosa cell tumor to MONDO:0023283. (OpenTargets Search: adult granulosa cell tumor of ovary)
- **Synonyms:** adult-type granulosa cell tumor; adult granulosa cell tumor; ovarian adult granulosa cell tumor; AGCT; aGCT; adult-type ovarian granulosa cell tumour.
- **Category:** rare malignant ovarian sex cord–stromal/endocrine neoplasm.
- **ICD-10-CM:** generally coded by behavior and ovarian site, most often C56.- for malignant ovarian neoplasm; morphology-specific registry coding is preferable. ICD-11 and ICD-O-3 morphology/site codes should be checked against the locally implemented release rather than inferred from text literature.
- **MeSH:** *Granulosa Cell Tumor* and *Ovarian Neoplasms*.
- No AGCT-specific OMIM entry establishing a Mendelian disorder was identified. FOXL2 has an OMIM disease relationship with blepharophimosis syndrome, but that germline disorder must not be conflated with the usual **somatic** FOXL2-mutant AGCT.

## 2. Etiology, risk, and protective factors

AGCT is best understood as a predominantly sporadic, somatically initiated neoplasm. The principal causal event is FOXL2 p.Cys134Trp; the 2023 knock-in mouse study provides unusually strong causal evidence that this single variant can initiate granulosa-cell transformation. (llano2023theoncogenicfoxl2 pages 9-10, llano2023theoncogenicfoxl2 pages 3-4)

No reproducible environmental, infectious, dietary, smoking, occupational, reproductive, or lifestyle cause has been established. Likewise, no validated protective allele, diet, medication, or behavioral intervention is known. Age and female ovarian anatomy describe the affected population but are not proven modifiable causes. Evidence for gene–environment interaction is insufficient.

Routine germline inheritance is not supported: the canonical FOXL2 variant is somatic, and there is no established autosomal-dominant, autosomal-recessive, X-linked, mitochondrial, anticipation, founder, carrier-frequency, or consanguinity pattern. Germline evaluation may nevertheless be appropriate when personal or family history suggests a cancer-predisposition syndrome; isolated reports do not establish population-level AGCT susceptibility.

## 3. Phenotypes

Phenotypes vary with tumor size, rupture, stage, and endocrine activity.

- **Pelvic or abdominal pain/fullness:** common presenting symptom; a 2013–2023 Iranian cohort reported abdominal pain in **56%**. Suggested HPO: **HP:0002027 Abdominal pain**, HP:0031507 Pelvic pain. Severity ranges from mild pressure to acute pain from hemorrhage or rupture.
- **Adnexal/pelvic mass and abdominal distension:** generally progressive until diagnosis. Suggested HPO: HP:0000149 Ovarian mass and HP:0003270 Abdominal distention, subject to ontology-version verification.
- **Abnormal uterine bleeding or menstrual irregularity:** caused by estrogenic stimulation in many reproductive-age or postmenopausal patients. Suggested HPO: **HP:0000132 Abnormal uterine bleeding**, HP:0000858 Menstrual irregularity.
- **Postmenopausal bleeding/endometrial proliferation:** clinically important because prolonged unopposed estrogen may cause endometrial hyperplasia or carcinoma. Suggested HPO: postmenopausal bleeding and endometrial hyperplasia terms, with IDs verified locally.
- **Precocious puberty:** characteristic mainly of juvenile GCT and uncommon in adult-type disease; it should not be treated as a core AGCT phenotype.
- **Laboratory abnormalities:** elevated inhibin B, inhibin A, AMH, or estradiol. Up to **30%** of tumors may not produce estrogen, so normal estrogen does not exclude AGCT. AMH has reported sensitivity of **89%** and specificity of **93%** in the summarized literature. Suggested HPO: abnormal circulating inhibin/AMH/estradiol terms where available. (salkeni2024advancedgranulosacell pages 2-3)

Quality-of-life burden includes pain, anxiety related to late relapse, surgical menopause after bilateral surgery, infertility or reduced fertility, and cumulative toxicity from repeated operations or systemic treatment. Robust AGCT-specific EQ-5D, SF-36, or PROMIS population estimates were not identified.

## 4. Genetic and molecular information

### Central driver

**FOXL2** encodes a forkhead transcription factor required for granulosa-cell identity and ovarian function. The somatic missense variant **c.402C>G, p.Cys134Trp** is detected in approximately **95–97%** of AGCTs; a 2024 series confirmed it in **223/225** tested tumors. It is therefore a highly informative diagnostic marker, although a negative result does not absolutely exclude AGCT. (salkeni2024advancedgranulosacell pages 2-3, salkeni2024advancedgranulosacell pages 1-2, nemejcova2024anextensiveimmunohistochemical pages 1-2)

Functionally, mutant FOXL2 acquires altered DNA-binding and protein-interaction properties. It forms a FOXL2–SMAD4–SMAD2/3 complex at a novel hybrid motif, creates enhancer-like chromatin, and activates genes involved in epithelial-to-mesenchymal transition, stemness, proliferation, and survival. TGF-β inhibition mitigated this transcriptional program in experimental systems. (llano2023theoncogenicfoxl2 pages 11-12)

### Secondary alterations

A 2024 review of 423 molecularly profiled tumors reported FOXL2 in 100% of that selected dataset, **TERT-promoter variants 56%, KMT2D 16.8%, CDKN2A/B deletion 10.2%, TP53 8.3%, MTAP deletion 5.8%, and PIK3CA 5.4%**. Frequencies differ by cohort, platform, stage, and inclusion of recurrent tumors; another 93-case study found KMT2D inactivation in 10.8%. These are tumor-acquired alterations, not established germline causes. (salkeni2024advancedgranulosacell pages 1-2)

Whole-genome studies have described gains of chromosomes 12 and 14 and loss of chromosome 22. A small **TP53-mutant, high-mitotic/high-tumor-mutation-burden subgroup** may represent high-grade transformation. Intrapatient comparisons found 29–80% of mutations unique to individual samples, demonstrating evolutionary heterogeneity. FOXL2-wild-type tumors may contain DICER1, TERT, or TP53 alterations and require especially careful pathologic review.

No validated modifier gene currently predicts penetrance or clinical severity. Population allele frequencies are not meaningful for the canonical FOXL2 lesion because it is a tumor-specific somatic variant; germline population frequency should be effectively absent. Somatic variants should be interpreted using AMP/ASCO/CAP oncology criteria, not automatically labeled as hereditary ACMG pathogenic variants.

## 5. Environmental information

No toxin, radiation exposure, pollution source, diet, alcohol pattern, smoking behavior, occupation, or pathogen has a proven causal role. AGCT is not infectious or transmissible. Associations inferred from general ovarian-cancer datasets should not be transferred to this biologically distinct sex cord–stromal tumor without subtype-specific evidence.

## 6. Mechanism and pathophysiology

A supported causal chain is:

1. **Upstream somatic event:** FOXL2 p.Cys134Trp arises in an ovarian granulosa cell.
2. **Transcriptional rewiring:** mutant FOXL2 changes DNA-site selection and hijacks SMAD4/SMAD2/3.
3. **Pathway disturbance:** TGF-β/activin signaling, steroidogenesis, apoptosis, cell-cycle control, EMT-like programs, and PI3K–AKT cross-talk become dysregulated.
4. **Cellular phenotype:** sustained granulosa-cell survival/proliferation, altered follicular organization, stromal remodeling, endocrine secretion, and eventual invasive tumor growth.
5. **Clinical manifestations:** ovarian mass, pain/rupture, estrogen-mediated uterine effects, and—after clonal evolution—late abdominal or pelvic recurrence. (llano2023theoncogenicfoxl2 pages 11-12, llano2023theoncogenicfoxl2 pages 9-10, llano2023theoncogenicfoxl2 pages 3-4)

**Suggested GO annotations:** transcription-factor binding; regulation of transcription by RNA polymerase II; TGF-beta receptor signaling; SMAD protein signal transduction; granulosa-cell differentiation; ovarian follicle development; steroid biosynthesis; cell-cycle regulation; apoptotic signaling; PI3K–AKT signaling; epithelial-to-mesenchymal transition.

**Suggested cell terms:** CL:0000501 granulosa cell; ovarian stromal fibroblast; endothelial cell; macrophage; neutrophil. The latter cell populations relate primarily to the tumor microenvironment rather than the initiating clone.

### Molecular profiling and tumor microenvironment

RNA sequencing of 24 tumors—8 primary and 16 recurrent—identified **31 differentially expressed genes**. LHCGR and INSL3 were enriched in primary tumors, whereas CYP19A1 was enriched in recurrence. Recurrent tumors showed immune/hormone pathway enrichment, increased inferred macrophage and neutrophil fractions, and reduced endothelial cells and cancer-associated fibroblasts; fibroblast depletion was replicated in independent datasets. These findings are observational, computationally deconvolved, and potentially confounded by non-paired samples and prior treatments. (khlebus2023comparativetumormicroenvironment pages 2-3, khlebus2023comparativetumormicroenvironment pages 9-10, khlebus2023comparativetumormicroenvironment pages 10-10, khlebus2023comparativetumormicroenvironment pages 1-2)

Current AGCT-specific single-cell and spatial-transcriptomic evidence remains limited. Bulk RNA-seq cannot fully resolve malignant granulosa-cell states or fibroblast and myeloid subtypes. Similarly, clinically validated proteomic, metabolomic, or lipidomic signatures are not yet available.

## 7. Anatomical structures affected

The primary organ is the **ovary**—suggested **UBERON:0000992**—usually involving one ovary at presentation. The neoplastic lineage is the follicular **granulosa cell**. Histologically involved compartments include ovarian cortex/stroma, follicle-like structures, tumor vasculature, and fibrous stroma.

Secondary disease most commonly involves pelvic or abdominal/peritoneal sites; advanced disease may affect bowel serosa, omentum, liver surface/parenchyma, lymph nodes, or distant organs. Relevant systems include reproductive, endocrine, gastrointestinal, and peritoneal systems. Subcellular emphasis is nuclear/chromatin localization of FOXL2 and SMAD transcriptional complexes—suggested GO:0005634 nucleus and GO:0000785 chromatin.

## 8. Temporal development

AGCT is primarily an adult/perimenopausal-onset disease. Reviews give a median diagnosis age near **46 years**, while the 2024 pathology cohort describes a typical range around **50–55 years**. It often grows indolently and is detected at FIGO stage I; 50–80% of cases in reviewed series were stage IA. (salkeni2024advancedgranulosacell pages 1-2, nemejcova2024anextensiveimmunohistochemical pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2)

The course is chronic and relapse-prone rather than self-limited. Approximately 20% recur in contemporary summaries, although heterogeneous series report 10–64%. Typical latency is 5–10 years, recurrence may occur after more than 20 years, and one review estimated an average 48–57 months. Thus, a five-year disease-free interval is not equivalent to cure. (salkeni2024advancedgranulosacell pages 2-3, salkeni2024advancedgranulosacell pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2)

FIGO ovarian staging is used: stage I confined to ovary/ovaries; stage II pelvic extension; stage III peritoneal or retroperitoneal nodal disease; stage IV distant metastasis. Tumor rupture is particularly relevant within stage I risk assessment.

## 9. Inheritance and population

AGCT affects persons with ovaries; the practical sex ratio is overwhelmingly female, while rare extraovarian or testicular granulosa-cell tumors are distinct entities. No consistently high-risk ancestry or endemic geography is established. Registry differences likely reflect ascertainment and coding rather than demonstrated genetic founder effects.

The disease has no established Mendelian inheritance, penetrance estimate, carrier frequency, anticipation, or germline mosaicism model. The FOXL2 driver is somatic. Genetic counseling is indicated only when the broader personal/family cancer history or unusual pathology raises concern for a germline syndrome.

## 10. Diagnostics

### Recommended workflow

1. **Clinical evaluation:** pelvic/abdominal symptoms, menstrual or postmenopausal bleeding, endocrine manifestations, fertility goals, and prior AGCT history.
2. **Imaging:** pelvic ultrasound initially; contrast CT for staging; MRI for lesion characterization or surgical planning. AGCT may be solid, cystic, or mixed with hemorrhage. A 2024 ten-case MRI series of estrogen-normal AGCT described T2-hyperintense cystic areas, diffusion restriction in solid components, hemorrhagic fluid levels, and occasional “honeycomb” or “Swiss-cheese” appearance; these are supportive, not diagnostic.
3. **Serum biomarkers:** inhibin B ± inhibin A, AMH, and estradiol. CA-125 is nonspecific. Baseline values are valuable for longitudinal surveillance.
4. **Histopathology:** variable diffuse, trabecular, insular, microfollicular, or cystic growth; grooved “coffee-bean” nuclei and Call–Exner bodies are classic but neither uniformly present nor individually specific.
5. **Immunohistochemistry:** in a 290-tumor 2024 cohort, positivity was SF1 100%, FOXL2 98%, PR 94%, CD99 90%, AR 82%, inhibin A 78%, calretinin 45%, and ER 41%. Tumors were microsatellite stable and uniformly PD-L1- and HER2-negative; aberrant p53 occurred in only 1%. (nemejcova2024anextensiveimmunohistochemical pages 1-2)
6. **Tumor molecular testing:** targeted FOXL2 c.402C>G testing is useful in morphologically difficult cases. Broader NGS can investigate FOXL2-wild-type, high-grade, recurrent, or treatment-refractory tumors. WES/WGS is not required routinely; CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion assays have no standard diagnostic role.

### Differential diagnosis

Important mimics include juvenile granulosa cell tumor, thecoma/fibrothecoma, Sertoli–Leydig cell tumor, sex cord tumor with annular tubules, endometrioid carcinoma with sex-cord-like areas, small-cell carcinoma, carcinoid/neuroendocrine tumor, metastatic carcinoma, and uterine-type tumors involving the ovary. Morphology, age, reticulin pattern, SF1/FOXL2/inhibin expression, epithelial markers, and FOXL2 sequencing resolve most cases.

There is no validated population screening test. Incidental AMH/inhibin testing in asymptomatic average-risk women is not recommended.

## 11. Outcomes and prognosis

Early-stage survival is excellent but does not eliminate late recurrence. A systematic review summarized five- and ten-year overall survival near **97% and 95%**, respectively, in predominantly early-stage populations. By stage, a 2024 review reported approximately **90% ten-year survival for stage I** versus **17–33% for stages III–IV**. (salkeni2024advancedgranulosacell pages 2-3, jung2023immunohistochemicalmarkersof pages 1-2)

Major adverse prognostic factors are advanced FIGO stage, tumor rupture, residual disease/incomplete cytoreduction, large tumor burden, high mitotic activity or high-grade transformation, and recurrence. Proposed molecular/IHC factors remain unvalidated. A 2023 review found associations between poorer outcome and CD56, GATA4, or SMAD3 expression, whereas ER, AMH, and inhibin were not prognostic; results for Ki-67, p53, β-catenin, and HER2 were inconsistent. (jung2023immunohistochemicalmarkersof pages 8-9, jung2023immunohistochemicalmarkersof pages 1-2)

Long-term morbidity includes infertility, surgical menopause, endocrine symptoms, recurrent abdominal operations, bowel or vascular involvement, chemotherapy toxicity, and psychological distress. Evidence for AGCT-specific disability or quality-of-life scores is sparse.

## 12. Treatment

### Surgery

Complete surgical resection and staging are the cornerstone. For post-reproductive patients, hysterectomy with bilateral salpingo-oophorectomy is commonly used. Carefully selected stage IA patients desiring fertility may undergo unilateral salpingo-oophorectomy with preservation of the uterus and contralateral ovary, followed by close surveillance. Cyst rupture or tumor spillage should be avoided. Recurrent disease should be assessed for complete secondary cytoreduction at an experienced multidisciplinary center.

Suggested NCIt terms include **Oophorectomy**, **Salpingo-oophorectomy**, **Hysterectomy**, **Surgical Staging**, and **Cytoreductive Surgery**.

### Systemic therapy

Observation is usual after completely staged low-risk stage IA disease. For high-risk stage I or stage II–IV disease, adjuvant chemotherapy may be considered, but a clear survival advantage has not been established. Common regimens include **BEP**—bleomycin, etoposide, cisplatin—and paclitaxel/carboplatin. Historical small series reported response rates of approximately **60% for CAP** and **66% for PVB**, but these estimates are imprecise and should not be interpreted as modern comparative efficacy. (salkeni2024advancedgranulosacell pages 2-3)

Toxicities include cisplatin nephrotoxicity, neurotoxicity and ototoxicity; etoposide myelosuppression and secondary leukemia risk; bleomycin pulmonary toxicity; and taxane neuropathy/alopecia. No AGCT-specific CPIC pharmacogenomic algorithm is established.

### Endocrine and targeted treatment

Because many tumors express ER, PR, or AR, aromatase inhibitors—letrozole, anastrozole, exemestane—GnRH analogues, progestins, or antiandrogen strategies are used in recurrent disease, generally with low toxicity but limited prospective response data. Molecularly guided approaches remain investigational.

Reported signals include responses longer than 12 months in two patients receiving temozolomide plus TRC102 and responses longer than five years in two patients receiving paclitaxel plus nilotinib; these are exceptional small-number observations, not definitive standards. JNK inhibition reduced growth in patient-derived xenografts. (salkeni2024advancedgranulosacell pages 6-7)

AGCT is generally immunologically “cold,” with low tumor mutational burden and absent PD-L1 in the large 2024 IHC series, making unselected checkpoint blockade biologically uncertain. Nevertheless, tumor-infiltrating lymphocytes from 11 patients reacted against autologous tumor in vitro, and 57% reacted to FOXL2 peptides, supporting antigen-directed research. (salkeni2024advancedgranulosacell pages 1-2, salkeni2024advancedgranulosacell pages 6-7, nemejcova2024anextensiveimmunohistochemical pages 1-2)

### Trials and real-world development

- **NCT06169124:** phase II darolutamide + leuprolide + exemestane for recurrent ovarian GCT; active, not recruiting; 17 participants.
- **NCT05872204:** phase II abemaciclib + letrozole in ER-positive rare ovarian cancers; recruiting; planned enrollment 100.
- **NCT05348356:** completed phase II nirogacestat, a gamma-secretase/NOTCH-pathway inhibitor, 150 mg twice daily; 53 recurrent AGCT participants; results were not available in the retrieved record. (NCT05348356 chunk 1)
- **NCT06254781:** completed single-patient luspatercept study targeting activin receptor–SMAD2/3 signaling; 1 mg/kg subcutaneously every three weeks. (NCT06254781 chunk 1)
- **NCT01042522:** randomized phase II paclitaxel/carboplatin versus BEP in advanced or recurrent sex cord–stromal tumors; 63 participants; primary endpoint progression-free survival. (NCT01042522 chunk 1, NCT01042522 chunk 7)
- Additional completed studies include paclitaxel (**NCT00006227**) and bevacizumab (**NCT00748657**).

No approved gene therapy, CRISPR therapy, CAR-T product, cell therapy, antisense oligonucleotide, or siRNA therapy exists for AGCT.

## 13. Prevention

- **Primary prevention:** none established; no vaccine, prophylactic drug, validated lifestyle modification, or risk-reducing surgery is recommended for average-risk women specifically to prevent AGCT.
- **Secondary prevention:** no population screening program. Prompt investigation of postmenopausal bleeding, endocrine abnormalities, or persistent adnexal masses may permit earlier diagnosis but is not AGCT-specific screening.
- **Tertiary prevention:** complete initial resection, avoidance of rupture, surveillance with symptoms/examination, imaging when indicated, and serial inhibin B/AMH when informative. Follow-up should extend beyond 10 years and often lifelong because relapse may occur after 20 years. (salkeni2024advancedgranulosacell pages 1-2, jung2023immunohistochemicalmarkersof pages 1-2)
- **Counseling:** discuss fertility preservation before definitive surgery or gonadotoxic chemotherapy. Routine cascade testing, prenatal testing, or preimplantation testing for somatic FOXL2 p.Cys134Trp is not appropriate.

## 14. Other species and natural disease

Naturally occurring ovarian granulosa-cell tumors are recognized in domestic species, particularly mares and cattle, and also occur in dogs and other mammals. In mares, endocrine activity can produce anestrus, persistent estrus, or stallion-like behavior; inhibin and AMH are used clinically. These tumors are useful for comparative endocrinology but should not automatically be considered homologous to human FOXL2 p.Cys134Trp AGCT without molecular confirmation.

Suggested taxa include **Homo sapiens NCBITaxon:9606**, **Mus musculus NCBITaxon:10090**, **Equus caballus NCBITaxon:9796**, **Bos taurus NCBITaxon:9913**, and **Canis lupus familiaris NCBITaxon:9615**. No zoonotic or cross-species transmission occurs. The relevant conserved gene is **FOXL2**, but species-specific variant and NCBI Gene identifiers should be resolved directly from current NCBI records.

## 15. Model organisms and experimental systems

The strongest model is the 2023 CRISPR knock-in **Foxl2+/C134W mouse**—murine p.C130W at the orthologous locus. All mutant females developed ovarian tumors before 18 months, whereas wild-type controls did not. Lesions progressed from abnormal follicles to stromal hyperplasia/atypia and then tumors with human-like granulosa morphology, Call–Exner bodies, and occasional high-grade features. Only 50% of mutant females produced offspring after six months of mating, and primordial follicles were markedly depleted. Sequencing found no recurrent additional driver, supporting sufficiency of mutant FOXL2. (llano2023theoncogenicfoxl2 pages 9-10, llano2023theoncogenicfoxl2 pages 3-4, llano2023theoncogenicfoxl2 pages 9-9, llano2023theoncogenicfoxl2 pages 2-3, llano2023theoncogenicfoxl2 pages 3-3)

Other engineered mouse systems—including granulosa-cell depletion of **Foxo1/Foxo3/Pten**, constitutive PI3K activation, inhibin/TGF-β–SMAD perturbation, β-catenin activation, and p53/Rb disruption—produce granulosa-cell tumors and help dissect proliferation, follicular signaling, and tumor suppression. However, older models do not fully recapitulate the defining molecular phenotype of human FOXL2-mutant AGCT. (liu2015foxo13andpten pages 1-2)

Cellular resources include KGN cells, COV434-derived systems, primary tumor cultures, organotypic cultures, and patient-derived xenografts. Important limitations are cell-line misclassification/history, adaptation to culture, absent immune/stromal context, and inability of xenografts to reproduce decades-long human latency.

## Evidence appraisal and knowledge gaps

The 2023–2024 literature materially strengthened three areas: causal proof for FOXL2 p.Cys134Trp in vivo; characterization of recurrence-associated hormone/TME remodeling; and a large, molecularly confirmed diagnostic IHC reference cohort. The central remaining gaps are prospective surveillance schedules, validated prognostic biomarkers, randomized evidence for adjuvant chemotherapy, reliable response estimates for endocrine therapy, AGCT-specific single-cell/spatial atlases, and adequately powered trials of FOXL2/TGF-β, NOTCH, PI3K–AKT, endocrine, or immune-directed treatment. The rarity of AGCT makes international registries, centralized pathology review, standardized biomarker collection, and adaptive basket trials especially important. (nemejcova2024anextensiveimmunohistochemical pages 1-2, khlebus2023comparativetumormicroenvironment pages 2-3, khlebus2023comparativetumormicroenvironment pages 1-2, llano2023theoncogenicfoxl2 pages 3-4)

### Key recent sources and links

- Llano et al., **Cancer Research**, published November 2023, “The oncogenic FOXL2 C134W mutation is a key driver of granulosa cell tumors,” DOI: https://doi.org/10.1158/0008-5472.CAN-22-1880. (llano2023theoncogenicfoxl2 pages 3-4)
- Khlebus et al., **Molecular Cancer Research**, published April 2023, DOI: https://doi.org/10.1158/1541-7786.MCR-22-0623. (khlebus2023comparativetumormicroenvironment pages 1-2)
- Jung et al., **Journal of Ovarian Research**, published March 2023, DOI: https://doi.org/10.1186/s13048-023-01125-1. (jung2023immunohistochemicalmarkersof pages 1-2)
- Němejcová et al., **Virchows Archiv**, published June 2024, DOI: https://doi.org/10.1007/s00428-024-03854-0. (nemejcova2024anextensiveimmunohistochemical pages 1-2)
- Salkeni et al., **Journal of Immunotherapy and Precision Oncology**, published November 2024, DOI: https://doi.org/10.36401/JIPO-23-40. (salkeni2024advancedgranulosacell pages 2-3, salkeni2024advancedgranulosacell pages 1-2)
- Landmark FOXL2 discovery literature is indexed under PMID **19516027**; additional FOXL2–AGCT literature indexed in the retrieved disease-target resource includes PMIDs 19956657, 20693978, 21293260, and 21623383. (OpenTargets Search: adult granulosa cell tumor of ovary)

References

1. (salkeni2024advancedgranulosacell pages 2-3): Mohamad A. Salkeni, Sarah Shin, Naoko Takebe, Sally Stevens, and Alice Chen. Advanced granulosa cell tumors of the ovary: a review with a focus on current and novel therapeutic approaches. Nov 2024. URL: https://doi.org/10.36401/jipo-23-40, doi:10.36401/jipo-23-40. This article has 10 citations.

2. (salkeni2024advancedgranulosacell pages 1-2): Mohamad A. Salkeni, Sarah Shin, Naoko Takebe, Sally Stevens, and Alice Chen. Advanced granulosa cell tumors of the ovary: a review with a focus on current and novel therapeutic approaches. Nov 2024. URL: https://doi.org/10.36401/jipo-23-40, doi:10.36401/jipo-23-40. This article has 10 citations.

3. (nemejcova2024anextensiveimmunohistochemical pages 1-2): Kristýna Němejcová, Adam Šafanda, Michaela Kendall Bártů, Romana Michálková, Marián Švajdler, Tetiana Shatokhina, Jan Laco, Radoslav Matěj, Gábor Méhes, Jana Drozenová, Jitka Hausnerová, Zuzana Špůrková, Monika Náležinská, and Pavel Dundr. An extensive immunohistochemical analysis of 290 ovarian adult granulosa cell tumors with 29 markers. Virchows Archiv : an international journal of pathology, 485:427-437, Jun 2024. URL: https://doi.org/10.1007/s00428-024-03854-0, doi:10.1007/s00428-024-03854-0. This article has 13 citations.

4. (jung2023immunohistochemicalmarkersof pages 1-2): Dennis Jung, Katrin Almstedt, Marco J. Battista, Alexander Seeger, Jörg Jäkel, Walburgis Brenner, and Annette Hasenburg. Immunohistochemical markers of prognosis in adult granulosa cell tumors of the ovary – a review. Journal of Ovarian Research, Mar 2023. URL: https://doi.org/10.1186/s13048-023-01125-1, doi:10.1186/s13048-023-01125-1. This article has 21 citations and is from a peer-reviewed journal.

5. (llano2023theoncogenicfoxl2 pages 3-4): Elena Llano, Anne Laure Todeschini, Natalia Felipe-Medina, María D. Corte-Torres, Yazmine B. Condezo, Manuel Sanchez-Martin, Sara López-Tamargo, Aurora Astudillo, Xose S. Puente, Alberto M. Pendas, and Reiner A. Veitia. The oncogenic foxl2 c134w mutation is a key driver of granulosa cell tumors. Cancer research, 83:239-250, Nov 2023. URL: https://doi.org/10.1158/0008-5472.can-22-1880, doi:10.1158/0008-5472.can-22-1880. This article has 27 citations and is from a highest quality peer-reviewed journal.

6. (OpenTargets Search: adult granulosa cell tumor of ovary): Open Targets Query (adult granulosa cell tumor of ovary, 7 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (salkeni2024advancedgranulosacell pages 6-7): Mohamad A. Salkeni, Sarah Shin, Naoko Takebe, Sally Stevens, and Alice Chen. Advanced granulosa cell tumors of the ovary: a review with a focus on current and novel therapeutic approaches. Nov 2024. URL: https://doi.org/10.36401/jipo-23-40, doi:10.36401/jipo-23-40. This article has 10 citations.

8. (llano2023theoncogenicfoxl2 pages 11-12): Elena Llano, Anne Laure Todeschini, Natalia Felipe-Medina, María D. Corte-Torres, Yazmine B. Condezo, Manuel Sanchez-Martin, Sara López-Tamargo, Aurora Astudillo, Xose S. Puente, Alberto M. Pendas, and Reiner A. Veitia. The oncogenic foxl2 c134w mutation is a key driver of granulosa cell tumors. Cancer research, 83:239-250, Nov 2023. URL: https://doi.org/10.1158/0008-5472.can-22-1880, doi:10.1158/0008-5472.can-22-1880. This article has 27 citations and is from a highest quality peer-reviewed journal.

9. (khlebus2023comparativetumormicroenvironment pages 1-2): Eleonora Khlebus, Veena K. Vuttaradhi, Thomas Welte, Namrata Khurana, Joseph Celestino, Hannah C. Beird, Curtis Gumbs, Latasha Little, Alejandra Flores Legarreta, Bryan M. Fellman, Tri Nguyen, Barrett Lawson, Sammy Ferri-Borgogno, Samuel C. Mok, Russell R. Broaddus, David M. Gershenson, P. Andrew Futreal, and R. Tyler Hillman. Comparative tumor microenvironment analysis of primary and recurrent ovarian granulosa cell tumors. Molecular Cancer Research, 21:483-494, Apr 2023. URL: https://doi.org/10.1158/1541-7786.mcr-22-0623, doi:10.1158/1541-7786.mcr-22-0623. This article has 15 citations and is from a peer-reviewed journal.

10. (khlebus2023comparativetumormicroenvironment pages 10-10): Eleonora Khlebus, Veena K. Vuttaradhi, Thomas Welte, Namrata Khurana, Joseph Celestino, Hannah C. Beird, Curtis Gumbs, Latasha Little, Alejandra Flores Legarreta, Bryan M. Fellman, Tri Nguyen, Barrett Lawson, Sammy Ferri-Borgogno, Samuel C. Mok, Russell R. Broaddus, David M. Gershenson, P. Andrew Futreal, and R. Tyler Hillman. Comparative tumor microenvironment analysis of primary and recurrent ovarian granulosa cell tumors. Molecular Cancer Research, 21:483-494, Apr 2023. URL: https://doi.org/10.1158/1541-7786.mcr-22-0623, doi:10.1158/1541-7786.mcr-22-0623. This article has 15 citations and is from a peer-reviewed journal.

11. (khlebus2023comparativetumormicroenvironment pages 2-3): Eleonora Khlebus, Veena K. Vuttaradhi, Thomas Welte, Namrata Khurana, Joseph Celestino, Hannah C. Beird, Curtis Gumbs, Latasha Little, Alejandra Flores Legarreta, Bryan M. Fellman, Tri Nguyen, Barrett Lawson, Sammy Ferri-Borgogno, Samuel C. Mok, Russell R. Broaddus, David M. Gershenson, P. Andrew Futreal, and R. Tyler Hillman. Comparative tumor microenvironment analysis of primary and recurrent ovarian granulosa cell tumors. Molecular Cancer Research, 21:483-494, Apr 2023. URL: https://doi.org/10.1158/1541-7786.mcr-22-0623, doi:10.1158/1541-7786.mcr-22-0623. This article has 15 citations and is from a peer-reviewed journal.

12. (jung2023immunohistochemicalmarkersof pages 8-9): Dennis Jung, Katrin Almstedt, Marco J. Battista, Alexander Seeger, Jörg Jäkel, Walburgis Brenner, and Annette Hasenburg. Immunohistochemical markers of prognosis in adult granulosa cell tumors of the ovary – a review. Journal of Ovarian Research, Mar 2023. URL: https://doi.org/10.1186/s13048-023-01125-1, doi:10.1186/s13048-023-01125-1. This article has 21 citations and is from a peer-reviewed journal.

13. (NCT06254781 chunk 1):  Luspatercept in Metastatic AGCT of the Ovary. University Health Network, Toronto. 2022. ClinicalTrials.gov Identifier: NCT06254781

14. (NCT05348356 chunk 1):  Nirogacestat in Ovarian Granulosa Cell Tumors. Merck Healthcare KGaA, Darmstadt, Germany, an affiliate of Merck KGaA, Darmstadt, Germany. 2022. ClinicalTrials.gov Identifier: NCT05348356

15. (khlebus2023comparativetumormicroenvironment pages 9-10): Eleonora Khlebus, Veena K. Vuttaradhi, Thomas Welte, Namrata Khurana, Joseph Celestino, Hannah C. Beird, Curtis Gumbs, Latasha Little, Alejandra Flores Legarreta, Bryan M. Fellman, Tri Nguyen, Barrett Lawson, Sammy Ferri-Borgogno, Samuel C. Mok, Russell R. Broaddus, David M. Gershenson, P. Andrew Futreal, and R. Tyler Hillman. Comparative tumor microenvironment analysis of primary and recurrent ovarian granulosa cell tumors. Molecular Cancer Research, 21:483-494, Apr 2023. URL: https://doi.org/10.1158/1541-7786.mcr-22-0623, doi:10.1158/1541-7786.mcr-22-0623. This article has 15 citations and is from a peer-reviewed journal.

16. (llano2023theoncogenicfoxl2 pages 2-3): Elena Llano, Anne Laure Todeschini, Natalia Felipe-Medina, María D. Corte-Torres, Yazmine B. Condezo, Manuel Sanchez-Martin, Sara López-Tamargo, Aurora Astudillo, Xose S. Puente, Alberto M. Pendas, and Reiner A. Veitia. The oncogenic foxl2 c134w mutation is a key driver of granulosa cell tumors. Cancer research, 83:239-250, Nov 2023. URL: https://doi.org/10.1158/0008-5472.can-22-1880, doi:10.1158/0008-5472.can-22-1880. This article has 27 citations and is from a highest quality peer-reviewed journal.

17. (llano2023theoncogenicfoxl2 pages 3-3): Elena Llano, Anne Laure Todeschini, Natalia Felipe-Medina, María D. Corte-Torres, Yazmine B. Condezo, Manuel Sanchez-Martin, Sara López-Tamargo, Aurora Astudillo, Xose S. Puente, Alberto M. Pendas, and Reiner A. Veitia. The oncogenic foxl2 c134w mutation is a key driver of granulosa cell tumors. Cancer research, 83:239-250, Nov 2023. URL: https://doi.org/10.1158/0008-5472.can-22-1880, doi:10.1158/0008-5472.can-22-1880. This article has 27 citations and is from a highest quality peer-reviewed journal.

18. (liu2015foxo13andpten pages 1-2): Zhilin Liu, Yi A. Ren, Stephanie A. Pangas, Jaye Adams, Wei Zhou, Diego H. Castrillon, Dagmar Wilhelm, and JoAnne S. Richards. Foxo1/3 and pten depletion in granulosa cells promotes ovarian granulosa cell tumor development. Molecular Endocrinology, 29:1006-1024, Jul 2015. URL: https://doi.org/10.1210/me.2015-1103, doi:10.1210/me.2015-1103. This article has 97 citations.

19. (llano2023theoncogenicfoxl2 pages 9-10): Elena Llano, Anne Laure Todeschini, Natalia Felipe-Medina, María D. Corte-Torres, Yazmine B. Condezo, Manuel Sanchez-Martin, Sara López-Tamargo, Aurora Astudillo, Xose S. Puente, Alberto M. Pendas, and Reiner A. Veitia. The oncogenic foxl2 c134w mutation is a key driver of granulosa cell tumors. Cancer research, 83:239-250, Nov 2023. URL: https://doi.org/10.1158/0008-5472.can-22-1880, doi:10.1158/0008-5472.can-22-1880. This article has 27 citations and is from a highest quality peer-reviewed journal.

20. (NCT01042522 chunk 1):  Paclitaxel and Carboplatin or Bleomycin Sulfate, Etoposide Phosphate, and Cisplatin in Treating Patients With Advanced or Recurrent Sex Cord-Ovarian Stromal Tumors. GOG Foundation. 2010. ClinicalTrials.gov Identifier: NCT01042522

21. (NCT01042522 chunk 7):  Paclitaxel and Carboplatin or Bleomycin Sulfate, Etoposide Phosphate, and Cisplatin in Treating Patients With Advanced or Recurrent Sex Cord-Ovarian Stromal Tumors. GOG Foundation. 2010. ClinicalTrials.gov Identifier: NCT01042522

22. (llano2023theoncogenicfoxl2 pages 9-9): Elena Llano, Anne Laure Todeschini, Natalia Felipe-Medina, María D. Corte-Torres, Yazmine B. Condezo, Manuel Sanchez-Martin, Sara López-Tamargo, Aurora Astudillo, Xose S. Puente, Alberto M. Pendas, and Reiner A. Veitia. The oncogenic foxl2 c134w mutation is a key driver of granulosa cell tumors. Cancer research, 83:239-250, Nov 2023. URL: https://doi.org/10.1158/0008-5472.can-22-1880, doi:10.1158/0008-5472.can-22-1880. This article has 27 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Adult_Granulosa_Cell_Tumor_of_Ovary-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.