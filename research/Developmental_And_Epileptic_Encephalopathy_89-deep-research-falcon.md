---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T02:29:18.520941'
end_time: '2026-08-27T02:40:44.230110'
duration_seconds: 685.71
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Developmental and Epileptic Encephalopathy 89
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 10
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 2
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Developmental_And_Epileptic_Encephalopathy_89-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental and Epileptic Encephalopathy 89
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental and Epileptic Encephalopathy 89** covering all of the
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
- **Disease Name:** Developmental and Epileptic Encephalopathy 89
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental and Epileptic Encephalopathy 89** covering all of the
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


# Developmental and Epileptic Encephalopathy 89 (DEE89): Disease Characteristics Report

## Executive summary and evidence limits

Developmental and epileptic encephalopathy 89 (DEE89) is an ultra-rare, autosomal-recessive neurodevelopmental disorder caused by biallelic loss-of-function variants in **GAD1**, which encodes glutamate decarboxylase 67 (GAD67), the principal enzyme supporting basal γ-aminobutyric acid (GABA) production in the central nervous system. The defining phenotype is early-infantile epilepsy followed by—or accompanied by—severe developmental impairment, hypotonia or weakness, and occasional craniofacial or skeletal abnormalities. The disease was established from only six unrelated affected individuals, so most percentages below describe that ascertainment cohort rather than population-level frequencies. (neuray2020earlyinfantileonsetepilepsy pages 3-3, neuray2020earlyinfantileonsetepilepsy pages 1-1, OpenTargets Search: developmental and epileptic encephalopathy 89-GAD1)

The foundational primary report is Neuray et al., **“Early-infantile onset epilepsy and developmental delay caused by bi-allelic GAD1 variants,”** published online 10 July 2020 in *Brain*, volume 143, pages 2388–2397; PMID **32282878**; DOI/URL: https://doi.org/10.1093/brain/awaa178. Its abstract states: **“Mice lacking GAD1 show neonatal mortality, but the human phenotype associated with GAD1 disruption is poorly characterized. Neuray et al. describe six patients with biallelic GAD1 mutations, presenting with early-infantile onset epilepsy, neurodevelopmental delay, muscle weakness and non-CNS manifestations.”** No substantive 2023–2024 DEE89-specific cohort, natural-history study, treatment trial, or mechanistic patient study was identified; recent literature largely discusses DEEs generally rather than expanding this disease-specific evidence base. (neuray2020earlyinfantileonsetepilepsy pages 3-3, neuray2020earlyinfantileonsetepilepsy pages 1-1)

| Domain | Evidence-based finding | Evidence level/limitations |
|---|---|---|
| Identity/identifiers | Developmental and epileptic encephalopathy 89 (DEE89) is linked to **MONDO:0030856** and **OMIM 619124**; Open Targets shows a single associated target, **GAD1**, with supporting literature including PMID **32282878**. The evidence base is disease-level aggregation plus a small primary human case series. (OpenTargets Search: developmental and epileptic encephalopathy 89-GAD1, neuray2020earlyinfantileonsetepilepsy pages 1-1) | Identifier linkage is strong, but disease characterization is based on very limited published human data. |
| Causal gene/inheritance | DEE89 is caused by **biallelic GAD1** variants encoding **GAD67/glutamate decarboxylase 1**; inheritance is **autosomal recessive**. In the reported cohort, **5/6 families** had homozygous variants and **1/6** had compound heterozygous variants; **4/6** affected individuals were born to consanguineous parents. (neuray2020earlyinfantileonsetepilepsy pages 3-3, neuray2020earlyinfantileonsetepilepsy pages 1-1) | Human genetic evidence is consistent, but numbers come from only **6 unrelated families**. |
| Foundational evidence | The foundational report is **Neuray et al., Brain, July 2020, DOI: 10.1093/brain/awaa178, PMID 32282878**, describing **6 affected individuals from 6 unrelated families** and introducing **GAD1 as a new gene associated with developmental and epileptic encephalopathy**. (neuray2020earlyinfantileonsetepilepsy pages 1-1, neuray2020earlyinfantileonsetepilepsy pages 3-3) | Single primary series; no larger replication cohort identified in the gathered evidence. |
| Onset/seizures | Seizure onset occurred at **2-6 months** (early-infantile onset). Seizure types were predominantly **focal motor seizures**, with some **epileptic spasms** and **bilateral motor seizures**. Seizures were **pharmacologically controlled in 3/6** and **drug-resistant in 3/6**. (neuray2020earlyinfantileonsetepilepsy pages 3-3) | Denominators preserved from the only cohort; no standardized natural-history registry available. |
| Development/neuromuscular | All reported individuals had **severe developmental delay/intellectual disability**; most had **no speech or communication**, with only **1/6** retaining basic/simple speech. **Reduced muscle strength/weakness or hypotonia** was present in **5/6**. Variable extracerebral features included **skeletal abnormalities, dysmorphic features, and cleft palate**. (neuray2020earlyinfantileonsetepilepsy pages 3-3, neuray2020earlyinfantileonsetepilepsy pages 1-1, neuray2020earlyinfantileonsetepilepsy pages 1-2) | Core phenotype is consistent, but extracerebral manifestations are variable and based on few cases. |
| MRI/EEG | **MRI** was reportedly normal in **4/6** and abnormal in **2/6**, with **ventricular enlargement** or **global atrophy**. **EEG** abnormalities included **burst-suppression**, **diffuse slowing with multifocal/generalized sharp waves**, and **hypsarrhythmia**. (neuray2020earlyinfantileonsetepilepsy pages 3-3) | Imaging appears nonspecific; EEG spectrum is broad and not disease-exclusive. |
| Variants | Seven reported **ultrarare germline** GAD1 variants were: **c.87C>G p.Tyr29Ter**, **c.568delC p.Gln190Serfs*11**, **c.670delC p.Leu224Serfs*5**, **c.971T>G p.Phe324Cys**, **c.1040C>T p.Thr347Met**, **c.1591C>T p.Arg531***, **c.1691A>G p.Asn564Ser**. Variant classes included **nonsense, frameshift, missense**; multiple alleles are predicted **loss-of-function** via nonsense-mediated decay or catalytic disruption. (neuray2020earlyinfantileonsetepilepsy pages 6-6, neuray2020earlyinfantileonsetepilepsy pages 5-6) | Functional interpretation is strongest for null alleles; allele-frequency details were not extracted in this conversation. |
| Mechanism | **GAD1/GAD67** is the major CNS enzyme for converting **glutamate to GABA** and contributes about **90% of baseline GABA**. Bi-allelic loss of function is inferred to reduce GABA synthesis, disturb **inhibitory/excitatory balance**, lower seizure threshold, and impair neurodevelopment; persistent severe disability despite seizure freedom in **3/6** supports a developmental effect beyond seizures alone. (neuray2020earlyinfantileonsetepilepsy pages 6-7, neuray2020earlyinfantileonsetepilepsy pages 6-6, neuray2020earlyinfantileonsetepilepsy pages 1-1, neuray2020earlyinfantileonsetepilepsy pages 5-6) | Mechanistic chain is biologically plausible and supported by human genetics plus model data, but direct patient biochemical assays were not summarized here. |
| Treatment | No disease-specific targeted therapy was identified. Management in the cohort was standard antiseizure treatment with **3/6** achieving seizure control and **3/6** remaining drug-resistant. No DEE89-specific clinical intervention trial was found. (neuray2020earlyinfantileonsetepilepsy pages 3-3) | Evidence is limited to case-based supportive epilepsy care; no controlled treatment studies or precision therapies are available in the gathered evidence. |
| Epidemiology/trials | No robust **prevalence**, **incidence**, or survival estimates were identified. The human literature currently consists of a **very small number of published cases**. Clinical trial search found **no relevant DEE89/GAD1-specific interventional trials**. (OpenTargets Search: developmental and epileptic encephalopathy 89-GAD1, neuray2020earlyinfantileonsetepilepsy pages 3-3) | Major evidence gap; epidemiology and prognosis remain undefined. |
| Model organism | **Gad1-null mice** show **neonatal lethality** and **severe cleft palate**, supporting the gene’s role in development but limiting detailed postnatal neurological modeling. Animal data also support a role for GAD/GABA pathway deficiency in seizures. (neuray2020earlyinfantileonsetepilepsy pages 6-7, neuray2020earlyinfantileonsetepilepsy pages 1-1) | Useful for biological plausibility, but existing model limitations reduce fidelity for full human DEE89 natural history. |


*Table: This table summarizes the highest-confidence evidence gathered for developmental and epileptic encephalopathy 89, preserving small-cohort denominators and highlighting where the literature is strong versus sparse. It is useful as a compact evidence map for knowledge-base curation.*

## 1. Disease information

### Definition

DEE89 is a monogenic developmental and epileptic encephalopathy in which the underlying GAD1 defect directly disrupts neurodevelopment while deficient inhibitory neurotransmission promotes epilepsy. The “developmental and epileptic” designation is important: developmental disability is not merely a consequence of recurrent seizures. In the original cohort, severe intellectual/developmental impairment persisted in all patients even though three became seizure-free, supporting parallel developmental and epileptic effects. (neuray2020earlyinfantileonsetepilepsy pages 6-6)

### Identifiers and synonyms

- **MONDO:** MONDO:0030856.
- **OMIM phenotype:** **619124**.
- **Causal gene:** **GAD1**, Ensembl ENSG00000128683; approved name *glutamate decarboxylase 1*.
- **Common names:** developmental and epileptic encephalopathy 89; DEE89; GAD1-related developmental and epileptic encephalopathy; GAD1-related early-infantile epilepsy and developmental delay.
- **Orphanet:** no disease-specific Orphanet identifier was established in the retrieved evidence.
- **ICD-10/ICD-11:** no unique DEE89 code. Cases are coded under broader genetic/developmental epileptic encephalopathy, epilepsy, intellectual disability, and developmental-disorder categories.
- **MeSH:** no unique disease heading; broader headings include *Epileptic Encephalopathies*, *Epilepsy*, and *Neurodevelopmental Disorders*.

Open Targets links MONDO:0030856 to one associated target, GAD1, and cites PMID 32282878 plus ClinVar records, providing aggregated disease-level corroboration of the primary case-series evidence. (OpenTargets Search: developmental and epileptic encephalopathy 89-GAD1)

**Source granularity:** available information is mainly an aggregated publication-level case series, not longitudinal EHR evidence. Database entries subsequently aggregate those individual reports.

## 2. Etiology, risk, and protective factors

### Causal factor

The established cause is **germline biallelic GAD1 variation**, generally producing loss of GAD67 function. Five of six reported families had homozygous variants and one had compound-heterozygous variants. Four affected individuals were born to consanguineous parents. (neuray2020earlyinfantileonsetepilepsy pages 3-3)

### Risk factors

- **Genetic:** two pathogenic or likely pathogenic alleles in trans are the principal risk factor. Parental consanguinity increases the probability that both parents carry the same rare allele, but is not mechanistically required.
- **Family history:** affected siblings would be expected in some families under recessive inheritance, although the founding report comprised one characterized patient per unrelated family.
- **Environmental, infectious, lifestyle, age, or sex risk:** none has been demonstrated. The reported patients represented diverse ancestries—Persian, Pakistani, African American, Sudanese, Egyptian, and Turkish—arguing against restriction to one population, but the sample is too small for demographic inference. (neuray2020earlyinfantileonsetepilepsy pages 1-2)

### Protective factors and gene–environment interaction

No protective allele, modifier gene, diet, exposure, or validated gene–environment interaction is known. Fever, sleep deprivation, illness, or medication nonadherence may trigger seizures in epilepsy generally, but these should not be entered as DEE89 causal factors without disease-specific evidence. Likewise, adequate vitamin B6 is required biochemically for pyridoxal-5′-phosphate-dependent decarboxylases, but neither pyridoxine deficiency nor pyridoxine responsiveness has been demonstrated as a DEE89 mechanism or treatment.

## 3. Phenotypes

Observed frequencies are from **n=6** and therefore have very wide uncertainty.

| Phenotype | Character, onset/course, observed frequency | Suggested HPO term |
|---|---|---|
| Early-infantile seizures | Onset **2–6 months**; focal motor seizures predominated, with epileptic spasms and bilateral motor seizures in some patients; chronic and variably treatment-resistant | Seizure HP:0001250; Infantile onset HP:0003593; Focal motor seizure HP:0011153; Epileptic spasms HP:0011097 |
| Developmental delay/intellectual disability | Severe in **6/6**; persistent despite seizure freedom in some; major lifelong functional effect expected | Global developmental delay HP:0001263; Severe intellectual disability HP:0010864 |
| Absent/severely impaired speech | Most had no speech or effective communication; one had basic/simple language | Absent speech HP:0001344; Delayed speech and language development HP:0000750 |
| Hypotonia, weakness, poor motor control | Reduced strength or hypotonia in **5/6**, ranging from mild hypotonia to limited head control | Muscular hypotonia HP:0001252; Muscle weakness HP:0001324; Head lag HP:0002421 |
| Abnormal EEG | Burst suppression, hypsarrhythmia, diffuse slowing, and multifocal/generalized sharp waves | EEG with burst suppression HP:0010851; Hypsarrhythmia HP:0002521; EEG abnormality HP:0002353 |
| Brain-imaging abnormality | MRI normal in **4/6**; ventricular enlargement or global cerebral atrophy in **2/6** | Cerebral atrophy HP:0002059; Ventriculomegaly HP:0002119 |
| Dysmorphism | Variable thick eyebrows, protruding ears, wide mouth, retrognathia, infraorbital creases, or depressed nasal bridge | Thick eyebrow HP:0000574; Protruding ear HP:0000411; Wide mouth HP:0000154; Retrognathia HP:0000278; Depressed nasal bridge HP:0005280 |
| Skeletal/abdominal findings | Variable scoliosis, clinodactyly, or diastasis recti | Scoliosis HP:0002650; Clinodactyly HP:0030084; Diastasis recti HP:0001540 |
| Cleft palate | Reported in one patient; biologically concordant with the mouse knockout but not a universal feature | Cleft palate HP:0000175 |

These features and frequencies derive from the original six-person series. EEG abnormalities included burst suppression, hypsarrhythmia, and diffuse slowing with multifocal or generalized sharp waves; MRI was nonspecific and often normal. (neuray2020earlyinfantileonsetepilepsy pages 3-3, neuray2020earlyinfantileonsetepilepsy pages 4-5)

**Quality-of-life impact:** no EQ-5D, SF-36, PROMIS, caregiver-burden, or disease-specific QoL measurements have been published. Nevertheless, severe communication, motor, cognitive, and seizure impairments imply dependence for daily activities and substantial caregiver burden. That conclusion is clinical inference, not a measured DEE89 outcome.

## 4. Genetic and molecular information

### Gene and protein

**GAD1** encodes the 67-kDa glutamate decarboxylase isoform, **GAD67**. The protein has an N-terminal targeting/dimerization region, a central pyridoxal-5′-phosphate-binding region, and a C-terminal catalytic region. GAD67 supplies approximately 90% of constitutive basal CNS GABA, whereas GAD65 has a more activity-responsive presynaptic role. (neuray2020earlyinfantileonsetepilepsy pages 1-2, neuray2020earlyinfantileonsetepilepsy pages 1-1, neuray2020earlyinfantileonsetepilepsy pages 5-6)

Suggested annotations include **HGNC:4092** (GAD1), UniProt **Q99259**, and enzyme class glutamate decarboxylase, EC 4.1.1.15. The biochemical reaction is L-glutamate → GABA + CO₂, requiring pyridoxal 5′-phosphate (**ChEBI:18405**) as cofactor; substrates/products include L-glutamate (**ChEBI:29985**) and 4-aminobutanoate/GABA (**ChEBI:16865**).

### Reported disease alleles

Seven ultrarare germline variants were reported:

1. **c.87C>G, p.(Tyr29Ter)** — nonsense.
2. **c.568delC, p.(Gln190SerfsTer11)** — frameshift.
3. **c.670delC, p.(Leu224SerfsTer5)** — frameshift.
4. **c.971T>G, p.(Phe324Cys)** — missense.
5. **c.1040C>T, p.(Thr347Met)** — missense.
6. **c.1591C>T, p.(Arg531Ter)** — nonsense.
7. **c.1691A>G, p.(Asn564Ser)** — missense. (neuray2020earlyinfantileonsetepilepsy pages 6-6)

The truncating variants are expected to cause nonsense-mediated decay or truncated protein. Missense substitutions affect conserved functional regions and were computationally predicted to impair stability or catalysis; four of seven reported alleles involved the PLP-binding domain. The aggregate disease mechanism is therefore **loss of function**, not gain of function or dominant-negative activity. (neuray2020earlyinfantileonsetepilepsy pages 6-6, neuray2020earlyinfantileonsetepilepsy pages 5-6)

The source paper described the variants as ultrarare and GAD1 as intolerant of damaging variation, but exact gnomAD/TOPMed allele counts and current per-variant ClinVar classifications were not available in the retrieved full-text evidence. These should be refreshed directly from ClinVar and gnomAD before production curation. Open Targets identified two associated ClinVar records, RCV006436612 and RCV004820862. (OpenTargets Search: developmental and epileptic encephalopathy 89-GAD1)

### Other genomic mechanisms

No disease-causing recurrent copy-number variant, translocation, inversion, repeat expansion, mitochondrial variant, somatic mosaicism, modifier gene, methylation signature, or other DEE89-specific epigenetic abnormality is established. Large deletions disrupting both GAD1 alleles would be mechanistically plausible but were not documented in the founding cohort.

## 5. Environmental information

DEE89 is a genetic Mendelian disease. No toxin, radiation, pollution, occupational exposure, smoking, alcohol, diet, infection, or other environmental exposure has been shown to cause it. There is no zoonotic or infectious component. Environmental conditions may alter seizure threshold nonspecifically, but no DEE89-specific interaction has been quantified.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic damaging GAD1 variants produce absent or impaired GAD67.
2. **Primary biochemical defect:** reduced PLP-dependent decarboxylation of glutamate to GABA.
3. **Cellular effect:** diminished GABA supply in inhibitory neurons compromises inhibitory synaptic transmission and maturation of GABAergic networks.
4. **Circuit effect:** excitation–inhibition imbalance and network hypersynchrony lower seizure threshold, generating early-infantile epilepsy and encephalopathic EEG patterns.
5. **Developmental effect:** GABA is also a developmental signal affecting neuronal migration, synaptogenesis, and circuit maturation. Thus GAD67 deficiency can directly impair cognition and motor development independently of seizure burden.
6. **Downstream clinical manifestations:** seizures, severe developmental/intellectual disability, absent speech, hypotonia/weakness, and occasionally cerebral atrophy.
7. **Extraneural development:** GAD1 expression in embryonic limb mesenchyme and pharyngeal structures, together with reduced fetal movement, may contribute to skeletal abnormalities and cleft palate; the human evidence remains provisional. (neuray2020earlyinfantileonsetepilepsy pages 8-9, neuray2020earlyinfantileonsetepilepsy pages 6-7, neuray2020earlyinfantileonsetepilepsy pages 1-1)

The observation that all six patients remained severely impaired while three achieved seizure control is an important human “natural experiment”: suppressing seizures alone does not reverse the upstream neurodevelopmental defect. (neuray2020earlyinfantileonsetepilepsy pages 6-6)

### Ontology-ready mechanism annotations

- **GO biological process:** glutamate decarboxylation to GABA; GABA biosynthetic process (**GO:0009449**); gamma-aminobutyric acid signaling pathway (**GO:0007214**); chemical synaptic transmission (**GO:0007268**); regulation of membrane potential (**GO:0042391**); nervous-system development (**GO:0007399**).
- **GO molecular function:** glutamate decarboxylase activity (**GO:0004351**); pyridoxal-phosphate binding (**GO:0030170**).
- **GO cellular component:** cytosol (**GO:0005829**), neuron projection (**GO:0043005**), presynapse (**GO:0098793**).
- **Cell Ontology:** neuron (**CL:0000540**); GABAergic neuron (**CL:0000617**); interneuron (**CL:0000099**). Particular interneuron subclasses have not been shown to be selectively vulnerable in DEE89.

There is no DEE89-specific evidence for apoptosis, autophagy, primary mitochondrial failure, immune activation, chronic inflammation, or a distinct metabolic signature beyond deficient GABA biosynthesis. No patient-derived transcriptomics, proteomics, metabolomics, lipidomics, single-cell, spatial-transcriptomic, multi-omic, CRISPR-screen, iPSC, or organoid study was found.

## 7. Anatomical structures affected

The **central nervous system** is primary, especially neuronal networks of the cerebral cortex and other GABAergic circuits. Suggested anatomy terms are brain (**UBERON:0000955**), cerebral cortex (**UBERON:0000956**), central nervous system (**UBERON:0001017**), and synapse (**UBERON:0001035**). No consistent focal lesion or lateralization has been reported; effects are presumed bilateral and network-wide.

Secondary or variably involved structures include skeletal muscle function, axial skeleton, digits, palate, and craniofacial structures. Weakness may reflect central hypotonia rather than primary myopathy; biopsy or EMG evidence for a muscle-intrinsic lesion is absent. Relevant subcellular sites are cytosol and inhibitory synaptic compartments, not mitochondria, lysosome, or nucleus as primary disease organelles. (neuray2020earlyinfantileonsetepilepsy pages 8-9, neuray2020earlyinfantileonsetepilepsy pages 3-3)

## 8. Temporal development and natural history

- **Prenatal/congenital:** most affected infants were not recognized prenatally; cleft palate or skeletal abnormalities may be congenital in a minority.
- **Onset:** seizures began at **2–6 months**, an early-infantile, generally subacute presentation.
- **Early course:** epileptic spasms, focal motor seizures, or bilateral motor seizures occur with markedly abnormal EEG.
- **Later course:** severe developmental delay, speech impairment, and weakness become prominent. Seizures may remit with medication or remain drug-resistant.
- **Duration:** presumed lifelong. No validated staging system exists.
- **Remission:** seizure freedom occurred in **3/6**, but developmental disability persisted; **3/6** remained drug-resistant. (neuray2020earlyinfantileonsetepilepsy pages 3-3)

No longitudinal cohort defines progression rate, regression frequency, adult phenotype, critical therapeutic window, or late complications. Early infancy is nevertheless a plausible intervention window because both seizures and GABA-dependent circuit development are active then; this remains expert mechanistic inference rather than trial evidence.

## 9. Inheritance and population

### Inheritance

Inheritance is **autosomal recessive**. For two confirmed heterozygous carrier parents, each pregnancy has an expected 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of an unaffected non-carrier. Penetrance for clearly biallelic null or severely damaging genotypes appears high, but cannot be estimated formally. Expressivity is variable, particularly for seizure control, MRI abnormalities, weakness, and extracerebral features.

There is no evidence for anticipation. Germline mosaicism is not required to explain recurrence but remains a theoretical residual risk if a variant appears de novo. No founder effect or carrier-frequency estimate is established. Consanguinity was present in **4/6** founding families, reflecting recessive ascertainment rather than proof of a population-specific disease. (neuray2020earlyinfantileonsetepilepsy pages 3-3, neuray2020earlyinfantileonsetepilepsy pages 1-2)

### Epidemiology

No prevalence, incidence, sex ratio, life-table, regional distribution, or ancestry-specific rate is available. Six ethnically diverse unrelated cases were reported initially. DEE89 should therefore be described as **ultra-rare, prevalence unknown**, not assigned a numerical population rate. (neuray2020earlyinfantileonsetepilepsy pages 1-2)

## 10. Diagnostics

### Clinical evaluation

Suspect DEE89 in an infant with seizures beginning in the first months of life, severe developmental delay or stagnation, hypotonia/weakness, and an encephalopathic EEG—particularly with consanguinity or affected siblings. EEG documents seizure type and background severity but is not specific. Brain MRI evaluates structural causes and complications; a normal MRI does not exclude DEE89 because **4/6** reported scans were normal. Routine blood, urine, CSF, enzyme, or tissue biomarkers have not been validated. (neuray2020earlyinfantileonsetepilepsy pages 3-3)

### Molecular confirmation

1. Use a comprehensive developmental-epilepsy panel including **GAD1**, trio exome sequencing, or trio genome sequencing.
2. Confirm candidate variants by an orthogonal method and establish **trans** phase through parental testing.
3. Evaluate sequence variants, exon-level deletions/duplications, splice variants, and—if WGS/RNA studies are available—deep intronic or regulatory defects.
4. Apply ACMG/AMP criteria using population rarity, predicted loss of function, segregation, phenotype concordance, and functional evidence.

WES was effective in the founding families. WGS can add CNV, structural, noncoding, and difficult-splice detection. CMA may be appropriate in unexplained developmental delay but will usually miss small GAD1 variants; karyotype and FISH have no disease-specific role. Mitochondrial and repeat-expansion tests are guided by the differential diagnosis, not DEE89 itself. No diagnostic RNA-seq, proteomic, metabolomic, epigenomic, or liquid-biopsy signature is validated.

### Differential diagnosis

Important alternatives include other early-infantile DEEs—**STXBP1, KCNQ2, SCN2A, SCN8A, CDKL5, KCNT1, DNM1, AP2M1, WWOX, PCDH12**, and metabolic epilepsies such as **ALDH7A1/PNPO**-related vitamin-B6-dependent epilepsy. Structural brain disease, congenital infection, hypoxic injury, and inborn errors of metabolism should be assessed clinically. DEE89 is distinguished by confirmed biallelic GAD1 pathogenic variants; no electroclinical feature is pathognomonic.

### Screening

DEE89 is not on routine newborn-screening panels, and no validated biochemical newborn marker exists. Targeted carrier, cascade, prenatal, or preimplantation testing is appropriate once familial variants are known.

## 11. Outcome and prognosis

No five- or ten-year survival, mortality rate, life expectancy, SUDEP incidence, or adult-outcome estimate exists. Gad1-null mouse neonatal lethality must not be extrapolated directly to humans with hypomorphic or partial-loss alleles.

Known morbidity is substantial: severe intellectual and communication disability occurred in all six original patients; weakness/hypotonia occurred in five; and half had drug-resistant epilepsy. Prognostic separation based on variant class is not yet possible. Seizure control does not guarantee cognitive recovery, because severe disability persisted in seizure-free patients. Potential complications follow from severe DEE generally—status epilepticus, aspiration, feeding difficulty, contractures/scoliosis, immobility, medication adverse effects, and SUDEP risk—but disease-specific rates are unknown. (neuray2020earlyinfantileonsetepilepsy pages 3-3, neuray2020earlyinfantileonsetepilepsy pages 6-6)

## 12. Treatment

### Current management

There is no approved GAD1- or DEE89-specific therapy. Management should be multidisciplinary:

- **Antiseizure medication:** individualized by seizure type and EEG; **3/6** founding patients achieved pharmacological control and **3/6** were drug-resistant. Published evidence does not support one drug as uniquely effective. (neuray2020earlyinfantileonsetepilepsy pages 3-3)
- **Rescue planning:** emergency benzodiazepine plan and education regarding prolonged seizures/status epilepticus.
- **Developmental care:** early physical, occupational, speech/augmentative-communication, and feeding therapies.
- **Orthopedic and nutritional care:** surveillance for scoliosis, contractures, aspiration, poor growth, and need for adaptive equipment.
- **Safety:** seizure precautions and counseling regarding SUDEP.

Possible NCIt mappings include **Anticonvulsant Agent (C264)**, **Physical Therapy (C15308)**, **Occupational Therapy (C15310)**, **Speech Therapy (C15312)**, **Genetic Counseling (C15246)**, and **Palliative/Supportive Care (C15292)**; exact NCIt codes should be verified against the current release before database import.

### Precision and experimental therapies

No DEE89-specific gene replacement, CRISPR editing, ASO, mRNA, cell therapy, or targeted small-molecule program has entered clinical trials, and the retrieved ClinicalTrials.gov search found no relevant interventional study. Increasing GAD1 expression, replacing GAD67, stabilizing residual enzyme, or augmenting GABAergic signaling are conceptual strategies, but chronic nonspecific GABA enhancement can cause sedation and may not restore early developmental signaling. Pyridoxine or PLP should not be represented as evidence-based DEE89 therapy absent biochemical deficiency or a supervised diagnostic trial for vitamin-B6-dependent epilepsy.

No pharmacogenomic response marker, response rate beyond the six-person series, treatment algorithm, or controlled adverse-event dataset exists.

## 13. Prevention

- **Primary prevention:** the sporadic occurrence of recessive alleles cannot be prevented by lifestyle or vaccination. Reproductive carrier testing, preimplantation genetic testing, chorionic-villus sampling, or amniocentesis can prevent or identify recurrence in families with known variants.
- **Secondary prevention:** no population screening program exists. Rapid genomic testing in early infantile DEE can shorten the diagnostic odyssey and support early seizure treatment and developmental intervention.
- **Tertiary prevention:** optimize seizure control, rescue therapy, vaccination and infection management, nutrition, aspiration precautions, mobility, bone health, communication support, and orthopedic surveillance.
- **Counseling:** offer parental testing, recurrence-risk counseling, cascade testing of adult relatives, and discussion of reproductive options.

There is no vaccine, environmental remediation, behavioral prophylaxis, or preventive medication specific to DEE89.

## 14. Other species and natural disease

No naturally occurring veterinary GAD1-associated syndrome equivalent to human DEE89 was identified, and there is no infectious transmission or zoonotic potential. Orthologs are evolutionarily conserved in vertebrates, including mouse *Gad1* and zebrafish *gad1b*, reflecting conservation of GABA synthesis. Natural breed associations and Vertebrate Breed Ontology annotations are unavailable.

## 15. Model organisms

### Mouse

Constitutive **Gad1-null mice** develop severe cleft palate and die neonatally. This strongly supports GAD1’s developmental and craniofacial roles but prevents characterization of postnatal seizures, cognition, and long-term disease progression. More generally, disruption of GAD enzymes or GABA-A receptor components can produce spontaneous seizures, supporting the proposed inhibitory-network mechanism. (neuray2020earlyinfantileonsetepilepsy pages 6-7, neuray2020earlyinfantileonsetepilepsy pages 1-1)

Suggested taxonomy is *Mus musculus*, NCBI Taxon **10090**. Useful future models would include conditional interneuron-specific knockouts, hypomorphic or patient-variant knock-ins, and temporally controlled alleles that survive beyond birth.

### Other model systems

No DEE89-specific zebrafish, Drosophila, *C. elegans*, patient-iPSC, neuronal culture, cerebral organoid, or humanized model was identified in the retrieved literature. These represent high-priority gaps. Patient-variant knock-in neurons could quantify GABA production, firing, synaptic inhibition, and rescue by gene replacement or residual-function modulators.

## Current expert assessment and knowledge-base recommendations

DEE89 has a compelling gene–disease relationship because multiple unrelated families carried biallelic ultrarare damaging GAD1 variants, the phenotype matches loss of inhibitory neurotransmission, and the mouse knockout supports developmental consequences. Nevertheless, clinical validity is much stronger than clinical actionability: diagnosis can be made molecularly, but prognosis and treatment remain based on six cases and general DEE practice. The most defensible knowledge-base entry should therefore preserve exact denominators, label mechanistic assignments as human-genetic plus model-supported, and mark epidemiology, QoL, long-term survival, biomarkers, genotype–phenotype correlation, and precision treatment as unknown. (OpenTargets Search: developmental and epileptic encephalopathy 89-GAD1, neuray2020earlyinfantileonsetepilepsy pages 6-6, neuray2020earlyinfantileonsetepilepsy pages 1-1)

**Principal reference:** Neuray C, Maroofian R, Scala M, et al. *Early-infantile onset epilepsy and developmental delay caused by bi-allelic GAD1 variants.* **Brain.** Published online 10 July 2020;143(8):2388–2397. PMID: **32282878**. DOI: https://doi.org/10.1093/brain/awaa178. (neuray2020earlyinfantileonsetepilepsy pages 3-3, neuray2020earlyinfantileonsetepilepsy pages 1-1)

References

1. (neuray2020earlyinfantileonsetepilepsy pages 3-3): Caroline Neuray, Reza Maroofian, Marcello Scala, Tipu Sultan, Gurpur S Pai, Majid Mojarrad, Heba El Khashab, Leigh deHoll, Wyatt Yue, Hessa S Alsaif, Maria N Zanetti, Oscar Bello, Richard Person, Atieh Eslahi, Zaynab Khazaei, Masoumeh H Feizabadi, Stephanie Efthymiou, Stanislav Groppa, Blagovesta Marinova Karashova, Wolfgang Nachbauer, Sylvia Boesch, Larissa Arning, Dagmar Timmann, Bru Cormand, Belen Pérez-Dueñas, Gabriella Di Rosa, Jatinder S Goraya, Tipu Sultan, Jun Mine, Daniela Avdjieva, Hadil Kathom, Radka Tincheva, Selina Banu, Mercedes Pineda-Marfa, Pierangelo Veggiotti, Michel D Ferrari, Alberto Verrotti, Giangluigi Marseglia, Salvatore Savasta, Mayte García-Silva, Alfons Macaya Ruiz, Barbara Garavaglia, Eugenia Borgione, Simona Portaro, Benigno Monteagudo Sanchez, Richard Boles, Savvas Papacostas, Michail Vikelis, Eleni Zamba Papanicolaou, Efthymios Dardiotis, Shazia Maqbool, Shahnaz Ibrahim, Salman Kirmani, Nuzhat Noureen Rana, Osama Atawneh, George Koutsis, Marianthi Breza, Salvatore Mangano, Carmela Scuderi, Eugenia Borgione, Giovanna Morello, Tanya Stojkovic, Massimi Zollo, Gali Heimer, Yves A Dauvilliers, Pasquale Striano, Issam Al-Khawaja, Fuad Al-Mutairi, Hamed Sherifa, Hala T El-Bassyouni, Doaa R Soliman, Selahattin Tekes, Leyla Ozer, Volkan Baltaci, Suliman Khan, Christian Beetz, Khalda S Amr, Vincenzo Salpietro, Yalda Jamshidi, Fowzan S Alkuraya, and Henry Houlden. Early-infantile onset epilepsy and developmental delay caused by bi-allelic gad1 variants. Brain, 143:2388-2397, Jul 2020. URL: https://doi.org/10.1093/brain/awaa178, doi:10.1093/brain/awaa178. This article has 56 citations and is from a highest quality peer-reviewed journal.

2. (neuray2020earlyinfantileonsetepilepsy pages 1-1): Caroline Neuray, Reza Maroofian, Marcello Scala, Tipu Sultan, Gurpur S Pai, Majid Mojarrad, Heba El Khashab, Leigh deHoll, Wyatt Yue, Hessa S Alsaif, Maria N Zanetti, Oscar Bello, Richard Person, Atieh Eslahi, Zaynab Khazaei, Masoumeh H Feizabadi, Stephanie Efthymiou, Stanislav Groppa, Blagovesta Marinova Karashova, Wolfgang Nachbauer, Sylvia Boesch, Larissa Arning, Dagmar Timmann, Bru Cormand, Belen Pérez-Dueñas, Gabriella Di Rosa, Jatinder S Goraya, Tipu Sultan, Jun Mine, Daniela Avdjieva, Hadil Kathom, Radka Tincheva, Selina Banu, Mercedes Pineda-Marfa, Pierangelo Veggiotti, Michel D Ferrari, Alberto Verrotti, Giangluigi Marseglia, Salvatore Savasta, Mayte García-Silva, Alfons Macaya Ruiz, Barbara Garavaglia, Eugenia Borgione, Simona Portaro, Benigno Monteagudo Sanchez, Richard Boles, Savvas Papacostas, Michail Vikelis, Eleni Zamba Papanicolaou, Efthymios Dardiotis, Shazia Maqbool, Shahnaz Ibrahim, Salman Kirmani, Nuzhat Noureen Rana, Osama Atawneh, George Koutsis, Marianthi Breza, Salvatore Mangano, Carmela Scuderi, Eugenia Borgione, Giovanna Morello, Tanya Stojkovic, Massimi Zollo, Gali Heimer, Yves A Dauvilliers, Pasquale Striano, Issam Al-Khawaja, Fuad Al-Mutairi, Hamed Sherifa, Hala T El-Bassyouni, Doaa R Soliman, Selahattin Tekes, Leyla Ozer, Volkan Baltaci, Suliman Khan, Christian Beetz, Khalda S Amr, Vincenzo Salpietro, Yalda Jamshidi, Fowzan S Alkuraya, and Henry Houlden. Early-infantile onset epilepsy and developmental delay caused by bi-allelic gad1 variants. Brain, 143:2388-2397, Jul 2020. URL: https://doi.org/10.1093/brain/awaa178, doi:10.1093/brain/awaa178. This article has 56 citations and is from a highest quality peer-reviewed journal.

3. (OpenTargets Search: developmental and epileptic encephalopathy 89-GAD1): Open Targets Query (developmental and epileptic encephalopathy 89-GAD1, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (neuray2020earlyinfantileonsetepilepsy pages 1-2): Caroline Neuray, Reza Maroofian, Marcello Scala, Tipu Sultan, Gurpur S Pai, Majid Mojarrad, Heba El Khashab, Leigh deHoll, Wyatt Yue, Hessa S Alsaif, Maria N Zanetti, Oscar Bello, Richard Person, Atieh Eslahi, Zaynab Khazaei, Masoumeh H Feizabadi, Stephanie Efthymiou, Stanislav Groppa, Blagovesta Marinova Karashova, Wolfgang Nachbauer, Sylvia Boesch, Larissa Arning, Dagmar Timmann, Bru Cormand, Belen Pérez-Dueñas, Gabriella Di Rosa, Jatinder S Goraya, Tipu Sultan, Jun Mine, Daniela Avdjieva, Hadil Kathom, Radka Tincheva, Selina Banu, Mercedes Pineda-Marfa, Pierangelo Veggiotti, Michel D Ferrari, Alberto Verrotti, Giangluigi Marseglia, Salvatore Savasta, Mayte García-Silva, Alfons Macaya Ruiz, Barbara Garavaglia, Eugenia Borgione, Simona Portaro, Benigno Monteagudo Sanchez, Richard Boles, Savvas Papacostas, Michail Vikelis, Eleni Zamba Papanicolaou, Efthymios Dardiotis, Shazia Maqbool, Shahnaz Ibrahim, Salman Kirmani, Nuzhat Noureen Rana, Osama Atawneh, George Koutsis, Marianthi Breza, Salvatore Mangano, Carmela Scuderi, Eugenia Borgione, Giovanna Morello, Tanya Stojkovic, Massimi Zollo, Gali Heimer, Yves A Dauvilliers, Pasquale Striano, Issam Al-Khawaja, Fuad Al-Mutairi, Hamed Sherifa, Hala T El-Bassyouni, Doaa R Soliman, Selahattin Tekes, Leyla Ozer, Volkan Baltaci, Suliman Khan, Christian Beetz, Khalda S Amr, Vincenzo Salpietro, Yalda Jamshidi, Fowzan S Alkuraya, and Henry Houlden. Early-infantile onset epilepsy and developmental delay caused by bi-allelic gad1 variants. Brain, 143:2388-2397, Jul 2020. URL: https://doi.org/10.1093/brain/awaa178, doi:10.1093/brain/awaa178. This article has 56 citations and is from a highest quality peer-reviewed journal.

5. (neuray2020earlyinfantileonsetepilepsy pages 6-6): Caroline Neuray, Reza Maroofian, Marcello Scala, Tipu Sultan, Gurpur S Pai, Majid Mojarrad, Heba El Khashab, Leigh deHoll, Wyatt Yue, Hessa S Alsaif, Maria N Zanetti, Oscar Bello, Richard Person, Atieh Eslahi, Zaynab Khazaei, Masoumeh H Feizabadi, Stephanie Efthymiou, Stanislav Groppa, Blagovesta Marinova Karashova, Wolfgang Nachbauer, Sylvia Boesch, Larissa Arning, Dagmar Timmann, Bru Cormand, Belen Pérez-Dueñas, Gabriella Di Rosa, Jatinder S Goraya, Tipu Sultan, Jun Mine, Daniela Avdjieva, Hadil Kathom, Radka Tincheva, Selina Banu, Mercedes Pineda-Marfa, Pierangelo Veggiotti, Michel D Ferrari, Alberto Verrotti, Giangluigi Marseglia, Salvatore Savasta, Mayte García-Silva, Alfons Macaya Ruiz, Barbara Garavaglia, Eugenia Borgione, Simona Portaro, Benigno Monteagudo Sanchez, Richard Boles, Savvas Papacostas, Michail Vikelis, Eleni Zamba Papanicolaou, Efthymios Dardiotis, Shazia Maqbool, Shahnaz Ibrahim, Salman Kirmani, Nuzhat Noureen Rana, Osama Atawneh, George Koutsis, Marianthi Breza, Salvatore Mangano, Carmela Scuderi, Eugenia Borgione, Giovanna Morello, Tanya Stojkovic, Massimi Zollo, Gali Heimer, Yves A Dauvilliers, Pasquale Striano, Issam Al-Khawaja, Fuad Al-Mutairi, Hamed Sherifa, Hala T El-Bassyouni, Doaa R Soliman, Selahattin Tekes, Leyla Ozer, Volkan Baltaci, Suliman Khan, Christian Beetz, Khalda S Amr, Vincenzo Salpietro, Yalda Jamshidi, Fowzan S Alkuraya, and Henry Houlden. Early-infantile onset epilepsy and developmental delay caused by bi-allelic gad1 variants. Brain, 143:2388-2397, Jul 2020. URL: https://doi.org/10.1093/brain/awaa178, doi:10.1093/brain/awaa178. This article has 56 citations and is from a highest quality peer-reviewed journal.

6. (neuray2020earlyinfantileonsetepilepsy pages 5-6): Caroline Neuray, Reza Maroofian, Marcello Scala, Tipu Sultan, Gurpur S Pai, Majid Mojarrad, Heba El Khashab, Leigh deHoll, Wyatt Yue, Hessa S Alsaif, Maria N Zanetti, Oscar Bello, Richard Person, Atieh Eslahi, Zaynab Khazaei, Masoumeh H Feizabadi, Stephanie Efthymiou, Stanislav Groppa, Blagovesta Marinova Karashova, Wolfgang Nachbauer, Sylvia Boesch, Larissa Arning, Dagmar Timmann, Bru Cormand, Belen Pérez-Dueñas, Gabriella Di Rosa, Jatinder S Goraya, Tipu Sultan, Jun Mine, Daniela Avdjieva, Hadil Kathom, Radka Tincheva, Selina Banu, Mercedes Pineda-Marfa, Pierangelo Veggiotti, Michel D Ferrari, Alberto Verrotti, Giangluigi Marseglia, Salvatore Savasta, Mayte García-Silva, Alfons Macaya Ruiz, Barbara Garavaglia, Eugenia Borgione, Simona Portaro, Benigno Monteagudo Sanchez, Richard Boles, Savvas Papacostas, Michail Vikelis, Eleni Zamba Papanicolaou, Efthymios Dardiotis, Shazia Maqbool, Shahnaz Ibrahim, Salman Kirmani, Nuzhat Noureen Rana, Osama Atawneh, George Koutsis, Marianthi Breza, Salvatore Mangano, Carmela Scuderi, Eugenia Borgione, Giovanna Morello, Tanya Stojkovic, Massimi Zollo, Gali Heimer, Yves A Dauvilliers, Pasquale Striano, Issam Al-Khawaja, Fuad Al-Mutairi, Hamed Sherifa, Hala T El-Bassyouni, Doaa R Soliman, Selahattin Tekes, Leyla Ozer, Volkan Baltaci, Suliman Khan, Christian Beetz, Khalda S Amr, Vincenzo Salpietro, Yalda Jamshidi, Fowzan S Alkuraya, and Henry Houlden. Early-infantile onset epilepsy and developmental delay caused by bi-allelic gad1 variants. Brain, 143:2388-2397, Jul 2020. URL: https://doi.org/10.1093/brain/awaa178, doi:10.1093/brain/awaa178. This article has 56 citations and is from a highest quality peer-reviewed journal.

7. (neuray2020earlyinfantileonsetepilepsy pages 6-7): Caroline Neuray, Reza Maroofian, Marcello Scala, Tipu Sultan, Gurpur S Pai, Majid Mojarrad, Heba El Khashab, Leigh deHoll, Wyatt Yue, Hessa S Alsaif, Maria N Zanetti, Oscar Bello, Richard Person, Atieh Eslahi, Zaynab Khazaei, Masoumeh H Feizabadi, Stephanie Efthymiou, Stanislav Groppa, Blagovesta Marinova Karashova, Wolfgang Nachbauer, Sylvia Boesch, Larissa Arning, Dagmar Timmann, Bru Cormand, Belen Pérez-Dueñas, Gabriella Di Rosa, Jatinder S Goraya, Tipu Sultan, Jun Mine, Daniela Avdjieva, Hadil Kathom, Radka Tincheva, Selina Banu, Mercedes Pineda-Marfa, Pierangelo Veggiotti, Michel D Ferrari, Alberto Verrotti, Giangluigi Marseglia, Salvatore Savasta, Mayte García-Silva, Alfons Macaya Ruiz, Barbara Garavaglia, Eugenia Borgione, Simona Portaro, Benigno Monteagudo Sanchez, Richard Boles, Savvas Papacostas, Michail Vikelis, Eleni Zamba Papanicolaou, Efthymios Dardiotis, Shazia Maqbool, Shahnaz Ibrahim, Salman Kirmani, Nuzhat Noureen Rana, Osama Atawneh, George Koutsis, Marianthi Breza, Salvatore Mangano, Carmela Scuderi, Eugenia Borgione, Giovanna Morello, Tanya Stojkovic, Massimi Zollo, Gali Heimer, Yves A Dauvilliers, Pasquale Striano, Issam Al-Khawaja, Fuad Al-Mutairi, Hamed Sherifa, Hala T El-Bassyouni, Doaa R Soliman, Selahattin Tekes, Leyla Ozer, Volkan Baltaci, Suliman Khan, Christian Beetz, Khalda S Amr, Vincenzo Salpietro, Yalda Jamshidi, Fowzan S Alkuraya, and Henry Houlden. Early-infantile onset epilepsy and developmental delay caused by bi-allelic gad1 variants. Brain, 143:2388-2397, Jul 2020. URL: https://doi.org/10.1093/brain/awaa178, doi:10.1093/brain/awaa178. This article has 56 citations and is from a highest quality peer-reviewed journal.

8. (neuray2020earlyinfantileonsetepilepsy pages 4-5): Caroline Neuray, Reza Maroofian, Marcello Scala, Tipu Sultan, Gurpur S Pai, Majid Mojarrad, Heba El Khashab, Leigh deHoll, Wyatt Yue, Hessa S Alsaif, Maria N Zanetti, Oscar Bello, Richard Person, Atieh Eslahi, Zaynab Khazaei, Masoumeh H Feizabadi, Stephanie Efthymiou, Stanislav Groppa, Blagovesta Marinova Karashova, Wolfgang Nachbauer, Sylvia Boesch, Larissa Arning, Dagmar Timmann, Bru Cormand, Belen Pérez-Dueñas, Gabriella Di Rosa, Jatinder S Goraya, Tipu Sultan, Jun Mine, Daniela Avdjieva, Hadil Kathom, Radka Tincheva, Selina Banu, Mercedes Pineda-Marfa, Pierangelo Veggiotti, Michel D Ferrari, Alberto Verrotti, Giangluigi Marseglia, Salvatore Savasta, Mayte García-Silva, Alfons Macaya Ruiz, Barbara Garavaglia, Eugenia Borgione, Simona Portaro, Benigno Monteagudo Sanchez, Richard Boles, Savvas Papacostas, Michail Vikelis, Eleni Zamba Papanicolaou, Efthymios Dardiotis, Shazia Maqbool, Shahnaz Ibrahim, Salman Kirmani, Nuzhat Noureen Rana, Osama Atawneh, George Koutsis, Marianthi Breza, Salvatore Mangano, Carmela Scuderi, Eugenia Borgione, Giovanna Morello, Tanya Stojkovic, Massimi Zollo, Gali Heimer, Yves A Dauvilliers, Pasquale Striano, Issam Al-Khawaja, Fuad Al-Mutairi, Hamed Sherifa, Hala T El-Bassyouni, Doaa R Soliman, Selahattin Tekes, Leyla Ozer, Volkan Baltaci, Suliman Khan, Christian Beetz, Khalda S Amr, Vincenzo Salpietro, Yalda Jamshidi, Fowzan S Alkuraya, and Henry Houlden. Early-infantile onset epilepsy and developmental delay caused by bi-allelic gad1 variants. Brain, 143:2388-2397, Jul 2020. URL: https://doi.org/10.1093/brain/awaa178, doi:10.1093/brain/awaa178. This article has 56 citations and is from a highest quality peer-reviewed journal.

9. (neuray2020earlyinfantileonsetepilepsy pages 8-9): Caroline Neuray, Reza Maroofian, Marcello Scala, Tipu Sultan, Gurpur S Pai, Majid Mojarrad, Heba El Khashab, Leigh deHoll, Wyatt Yue, Hessa S Alsaif, Maria N Zanetti, Oscar Bello, Richard Person, Atieh Eslahi, Zaynab Khazaei, Masoumeh H Feizabadi, Stephanie Efthymiou, Stanislav Groppa, Blagovesta Marinova Karashova, Wolfgang Nachbauer, Sylvia Boesch, Larissa Arning, Dagmar Timmann, Bru Cormand, Belen Pérez-Dueñas, Gabriella Di Rosa, Jatinder S Goraya, Tipu Sultan, Jun Mine, Daniela Avdjieva, Hadil Kathom, Radka Tincheva, Selina Banu, Mercedes Pineda-Marfa, Pierangelo Veggiotti, Michel D Ferrari, Alberto Verrotti, Giangluigi Marseglia, Salvatore Savasta, Mayte García-Silva, Alfons Macaya Ruiz, Barbara Garavaglia, Eugenia Borgione, Simona Portaro, Benigno Monteagudo Sanchez, Richard Boles, Savvas Papacostas, Michail Vikelis, Eleni Zamba Papanicolaou, Efthymios Dardiotis, Shazia Maqbool, Shahnaz Ibrahim, Salman Kirmani, Nuzhat Noureen Rana, Osama Atawneh, George Koutsis, Marianthi Breza, Salvatore Mangano, Carmela Scuderi, Eugenia Borgione, Giovanna Morello, Tanya Stojkovic, Massimi Zollo, Gali Heimer, Yves A Dauvilliers, Pasquale Striano, Issam Al-Khawaja, Fuad Al-Mutairi, Hamed Sherifa, Hala T El-Bassyouni, Doaa R Soliman, Selahattin Tekes, Leyla Ozer, Volkan Baltaci, Suliman Khan, Christian Beetz, Khalda S Amr, Vincenzo Salpietro, Yalda Jamshidi, Fowzan S Alkuraya, and Henry Houlden. Early-infantile onset epilepsy and developmental delay caused by bi-allelic gad1 variants. Brain, 143:2388-2397, Jul 2020. URL: https://doi.org/10.1093/brain/awaa178, doi:10.1093/brain/awaa178. This article has 56 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Developmental_And_Epileptic_Encephalopathy_89-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.