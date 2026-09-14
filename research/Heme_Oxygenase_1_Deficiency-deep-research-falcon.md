---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-21T21:06:12.546541'
end_time: '2026-08-21T21:17:35.866060'
duration_seconds: 683.32
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Heme Oxygenase 1 Deficiency
  mondo_id: ''
  category: Mendelian
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
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Heme_Oxygenase_1_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Heme Oxygenase 1 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Heme Oxygenase 1 Deficiency** covering all of the
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
- **Disease Name:** Heme Oxygenase 1 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Heme Oxygenase 1 Deficiency** covering all of the
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


# Heme Oxygenase-1 Deficiency: Disease Characteristics Report

## Executive summary and evidence limits

Heme oxygenase-1 deficiency is an ultra-rare, usually severe autosomal-recessive disorder caused by biallelic pathogenic variants in **HMOX1**. Loss of inducible HO-1-mediated heme degradation produces a distinctive combination of Coombs-negative intravascular hemolysis, paradoxically low/normal bilirubin, very high LDH and ferritin, leukocytosis, thrombocytosis, systemic inflammation, endothelial injury, nephropathy, hepatic iron deposition, and absent or dysfunctional spleen. Pulmonary fibrosis, hemophagocytic flares, pericardial disease, and AA amyloidosis expand the recognized spectrum. The strongest systematic clinical evidence remains a 2021 review of nine independent patients; therefore, percentages below are case-series proportions, not population estimates. Publications in 2023–2024 added renal-amyloidosis and pulmonary/variant reports, but no cohort, guideline, approved disease-modifying treatment, or disease-specific clinical trial was identified.

**Evidence classes:** *human clinical* denotes affected patients; *model* denotes knockout animals; *in vitro* denotes patient or engineered cells. Broader associations involving common HMOX1 promoter polymorphisms are not equivalent to Mendelian HO-1 deficiency.

## 1. Disease information

### Definition and nomenclature

HO-1 deficiency is an inherited failure of the inducible heme-degrading enzyme HO-1. HO-1 normally catalyzes the rate-limiting conversion of heme to **biliverdin, carbon monoxide (CO), and ferrous iron**; biliverdin is subsequently reduced to bilirubin. The disease is consequently both an enzyme deficiency and a disorder of heme detoxification, iron recycling, redox defense, and inflammatory restraint. The first molecularly defined patient was reported in 1999 by Yachie et al.; the primary paper is *J Clin Invest* 103:129–135, DOI [10.1172/JCI4165](https://doi.org/10.1172/JCI4165), PMID **9927502**. The later review was published 3 February 2021, DOI [10.3390/ijms22041514](https://doi.org/10.3390/ijms22041514). (yachie2021hemeoxygenase1deficiency pages 1-3, yachie2021hemeoxygenase1deficiency pages 15-16)

**Preferred name:** heme oxygenase-1 deficiency. **Synonyms:** HO-1 deficiency; HMOX1 deficiency; human heme oxygenase-1 deficiency; heme oxygenase 1 deficiency. “Heme oxygenase deficiency” is imprecise because HMOX2 encodes the constitutive HO-2 isozyme.

**Identifiers:**

- **Causal gene:** *HMOX1*; OMIM gene **141250** (often displayed as *141250); HGNC **5013**; NCBI Gene **3162**.
- **Disease OMIM/MONDO:** a confidently verified separate phenotype number or MONDO identifier was not available in the retrieved evidence. OMIM *141250 is the **gene entry**, not necessarily a disease-phenotype identifier, and should not be entered as such without direct database verification.
- **Orphanet:** no verified dedicated identifier found.
- **MeSH:** no disease-specific descriptor found; use “Heme Oxygenase-1” plus appropriate manifestations.
- **ICD-10/ICD-11:** no specific code identified. Practical coding would require an “other specified disorder of metabolism/hematologic disorder” code plus manifestations, varying by jurisdiction.

The evidence is principally **aggregated disease-level literature reconstructed from individual published cases**, not EHR-derived population data. The 2021 synthesis explicitly states that only nine independent cases had been described. (yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 1-3)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The primary cause is **biallelic germline HMOX1 dysfunction**. Reported genotypes include a compound exon-2 deletion/exon-3 2-bp deletion, homozygous **p.Arg44Ter (R44X)**, homozygous **p.Lys204Ter (K204X)**, homozygous **p.Gly139Val (G139V)**, and compound **c.264_269delCTGG (p.Leu89SerfsTer24)** plus **c.636+2T>A**. Most are null alleles; p.G139V retains abnormal protein with reduced HO activity and acquired peroxidase behavior. Variants are germline, not somatic. (yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 6-7, yachie2021hemeoxygenase1deficiency pages 4-6)

Population allele frequencies and current ClinVar ACMG classifications were not recoverable from the retrieved documents. Given severe recessive disease and the tiny number of families, the causal alleles are expected to be very rare, but “absent from gnomAD” should not be asserted without direct version-specific lookup.

### Risk factors

- **Genetic:** biallelic pathogenic HMOX1 variants; consanguinity was documented in the Iranian and Turkish families. The five Indian patients shared homozygous p.R44X, suggesting a founder allele. Family history may include fetal loss: the first patient’s mother had two intrauterine deaths, and the Iranian family had a spontaneous fetal loss, although causality was not genetically established. (yachie2021hemeoxygenase1deficiency pages 3-4, yachie2021hemeoxygenase1deficiency pages 6-7, yachie2021hemeoxygenase1deficiency pages 4-6)
- **Environmental/physiologic triggers:** infections, hemolysis, transfusion, hypoxemia, and other oxidative insults plausibly precipitate inflammatory deterioration because HO-1 is normally stress inducible. The Indian patients could remain well for years and then deteriorate rapidly after inflammation began. The p.G139V patient had paradoxical inflammation after red-cell transfusion. These are trigger interactions, not causes of the Mendelian disorder. (yachie2021hemeoxygenase1deficiency pages 6-7, yachie2021hemeoxygenase1deficiency pages 1-3, yachie2021hemeoxygenase1deficiency pages 4-6)
- **Age/sex/lifestyle:** no established sex, diet, smoking, occupation, toxin, or lifestyle risk effect. Onset ranged from 3 months to 15 years, and both sexes were affected. (yachie2021hemeoxygenase1deficiency pages 7-8)

### Protective factors

No validated human protective allele, diet, lifestyle, or prophylactic drug is known. Avoiding unnecessary oxidative stress, promptly treating infection, and cautious transfusion practice are biologically reasonable but untested. HO-1 induction cannot restore an absent/null enzyme. CO donors, bilirubin/biliverdin, haptoglobin–CD163 enhancement, and wild-type macrophage replacement remain experimental concepts. The review’s conclusion—“**Avoidance of exogenous stress along with appropriate treatment may prevent early death**”—is expert opinion rather than trial evidence. (yachie2021hemeoxygenase1deficiency pages 13-15)

## 3. Phenotypes

Across the nine historical patients, **fever and hemolytic anemia occurred in 9/9**; jaundice occurred in 0/9 despite hemolysis. Hematuria/proteinuria occurred in all six Japanese/Indian cases and in the US case, but were unreported in two others. Absent/hypoplastic spleen affected seven of nine; one had splenomegaly and one a normal-sized spleen. These fractions are descriptive only. (yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 8-10)

| Group / country | Sex and onset range | Genotype | Defining phenotype / labs | Course / outcome |
|---|---|---|---|---|
| Case 1, Japan | Male; onset 2 years, diagnosis 5 years | Compound heterozygote: maternal allele lacked exon 2; paternal allele had 2-bp deletion in exon 3 (HMOX1) | Recurrent fever, generalized erythematous rash, joint pain, marked hepatomegaly, asplenia, flat nasal bridge, frontal bossing, eyelid edema; leukocytosis 51,600/µL, thrombocytosis 226 × 10^4/µL, hemoglobin 4.9 g/dL, LDH 17,470 IU/L, ferritin 780 ng/mL, triglycerides 638 mg/dL, total cholesterol 552 mg/dL, bilirubin 0.1–0.3 mg/dL, serum heme 490 µM, very high haptoglobin 800–1200 mg/dL; hematuria/proteinuria; kidney/liver iron deposition; vacuolated monocytes; endothelial/coagulation-fibrinolysis abnormalities (yachie2021hemeoxygenase1deficiency pages 3-4, yachie2021hemeoxygenase1deficiency pages 4-6) | Severe multisystem disease; specific final outcome not stated in gathered evidence; first autopsy case reported in literature review context (yachie2021hemeoxygenase1deficiency pages 15-16, yachie2021hemeoxygenase1deficiency pages 4-6) |
| Cases 2–6, India | Mixed sexes: female, male, male, female, male; onset 6 months to 15 years; diagnosis 20 months to 16 years | Homozygous p.R44X nonsense mutation in all 5 cases; founder effect suggested; parental genotypes unknown/not done for some, heterozygous R44X/wild type in some families (yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 4-6) | Shared tetrad/profile: fever, asplenia, hemolytic anemia, hematuria/proteinuria, absent jaundice; prominent forehead common; growth delay variable; hypertension in most, cerebral bleeding in some; labs: CRP 4.8–30.8 mg/dL, WBC 18.5–43.2 ×10^3/mL, platelets 100–137 ×10^4/mL (one not shown), ferritin 2,000 to 15,530 ng/mL, LDH 4,000 to 21,400 IU/L, bilirubin 0.02–1.2 mg/dL, high haptoglobin despite hemolysis (yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 4-6) | Variable latent period, then often rapid deterioration. Case 2 died 5 months after diagnosis after hypertension/intracranial hemorrhage and fungal sepsis; Cases 3 and 6 also reportedly died soon after symptom onset; outcomes for Cases 4–5 unknown in gathered evidence (yachie2021hemeoxygenase1deficiency pages 4-6) |
| Case 7, Iran | Female; onset 17 months, diagnosis 3 years | Homozygous p.K204X in exon 3; both parents heterozygous carriers; consanguineous Iranian parents (yachie2021hemeoxygenase1deficiency pages 4-6, yachie2021hemeoxygenase1deficiency pages 6-7) | High fever, tachypnea, respiratory distress, massive pericardial effusion, hepatomegaly with liver iron deposition, normal-sized spleen, prolonged/recurrent fever, hemolytic anemia; leukocytosis 33.0 ×10^3/mL, platelets 100 ×10^4/mL, ferritin 27,425 ng/mL, LDH 15,350 IU/L, AST/ALT 580/813 IU/L, bilirubin 0.8 mg/dL, hyperlipidemia (yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 6-7, yachie2021hemeoxygenase1deficiency pages 4-6) | Corticosteroid ineffective; progressive deterioration over 4 admissions; died of recurrent fever, bleeding, heart failure, and ascites; diagnosis made post-mortem by whole-exome sequencing (yachie2021hemeoxygenase1deficiency pages 4-6) |
| Case 8, Turkey | Male; onset 3 months, diagnosis 20 months | Homozygous p.G139V missense mutation; son of consanguineous Turkish parents (yachie2021hemeoxygenase1deficiency pages 6-7) | Microcytic anemia resistant to iron, progressive hepatosplenomegaly, transfusion dependence; liver biopsy: severe hemophagocytosis, Kupffer cell siderosis, extramedullary hematopoiesis; slight marrow hemophagocytosis; inflammatory markers remained high (IL-1β, IL-6, TNF-α, ferritin, CRP); WBC 19.9 ×10^3/mL, platelets 47.8 ×10^4/mL, ferritin 4,855 ng/mL, LDH 15,713 IU/L, bilirubin 0.2–1.6 mg/dL; decreased HO-1 activity with abnormal peroxidase function and increased urinary peroxidation products (yachie2021hemeoxygenase1deficiency pages 6-7) | Treated with HLH2004 immunochemotherapy with sustained remission of HLH-like signs, but inflammatory activity persisted; paradoxical inflammatory response to red cell transfusion reported; longer-term outcome unknown in gathered evidence (yachie2021hemeoxygenase1deficiency pages 6-7) |
| Case 9, USA | Male; onset 4 years, diagnosis 10 years | Compound heterozygote: paternal frameshift c.264_269delCTGG (p.L89Sfs*24) and maternal splice donor c.636+2T>A (yachie2021hemeoxygenase1deficiency pages 7-8) | Interstitial lung disease with recurrent inflammatory flares; fatigue, intermittent fevers, dark urine, hypoxemia, hepatomegaly, poorly perfused hypoplastic spleen/hyposplenia, growth slowing, hemolytic anemia with schistocytes and Howell-Jolly bodies, hematuria/proteinuria; WBC 53.8 ×10^3/mL, platelets 91.4 ×10^4/mL, ferritin 1,980 ng/mL, LDH 19,706 IU/L, bilirubin 0.2 mg/dL; liver biopsy with mild sinusoidal fibrosis, microvesicular steatosis, Kupffer-cell iron; lung biopsy with extensive fibrotic nonspecific interstitial pneumonia, pleural fibrosis, scattered/pulmonary interstitial and intra-alveolar cholesterol granulomas; PBMCs failed to induce HO-1 with cobalt protoporphyrin (yachie2021hemeoxygenase1deficiency pages 6-7, yachie2021hemeoxygenase1deficiency pages 7-8) | Genetic testing for periodic fever syndromes/familial HLH initially negative; treated with corticosteroid, anti-IL-1R, anti-IL-6, and cyclosporine with minimal benefit; died at age 10 from respiratory failure; diagnosis established post-mortem by whole-exome sequencing (yachie2021hemeoxygenase1deficiency pages 6-7, yachie2021hemeoxygenase1deficiency pages 7-8) |


*Table: This table compacts the currently gathered human evidence for HMOX1 deficiency into case groups, highlighting genotype, hallmark phenotype/laboratory patterns, and outcomes. It is useful for quickly comparing the recurrent diagnostic denominators and notable phenotype expansions across the 9 reported cases.*

### Knowledge-base phenotype mapping

- **Recurrent fever**—infancy through adolescence; episodic then potentially persistent/severe; 9/9. HPO: **HP:0001954 Recurrent fever**.
- **Coombs-negative hemolytic anemia**, often severe and fragmented-cell/microangiopathic—9/9; HPO: **HP:0001878 Hemolytic anemia**, **HP:0001937 Microangiopathic hemolytic anemia**, **HP:0001892 Abnormal bleeding** where present.
- **Low or normal bilirubin despite hemolysis**—9/9 historical cases; a highly discriminating laboratory abnormality. HPO: **HP:0002905 Hypob​​ilirubinemia** if locally supported; otherwise record quantitative laboratory phenotype rather than force an HPO term. (yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 8-10)
- **Extreme LDH/hyperferritinemia**—LDH approximately 4,000–21,400 IU/L and ferritin 780–27,425 ng/mL in the tabulated cases. HPO: **HP:0031964 Elevated circulating ferritin concentration**, **HP:0025435 Elevated circulating lactate dehydrogenase concentration**. (yachie2021hemeoxygenase1deficiency pages 7-8)
- **Leukocytosis and thrombocytosis**—nearly invariant and useful in distinguishing the disorder from classic HLH-associated cytopenias. HPO: **HP:0001974 Leukocytosis**, **HP:0001894 Thrombocytosis**. (yachie2021hemeoxygenase1deficiency pages 8-10)
- **Asplenia/hyposplenia or evolving splenic dysfunction**—usually congenital/early but variable; HPO: **HP:0001746 Asplenia**, **HP:0001870 Acquired abnormality of spleen**, **HP:0031417 Hyposplenism**, and **HP:0001744 Splenomegaly** for the alternate trajectory.
- **Renal disease**—hematuria, proteinuria, glomerular endothelial swelling/detachment, mesangial proliferation, tubular atrophy, iron deposition, and later amyloidosis. HPO: **HP:0000790 Hematuria**, **HP:0000093 Proteinuria**, **HP:0000099 Glomerulonephritis**, **HP:0000077 Abnormality of the kidney**. (yachie2021hemeoxygenase1deficiency pages 10-12, yachie2021hemeoxygenase1deficiency pages 4-6)
- **Hepatomegaly/hepatic siderosis**—common; HPO: **HP:0002240 Hepatomegaly**, **HP:0001392 Abnormality of the liver**, **HP:0003233 Abnormality of iron homeostasis**.
- **Hyperlipidemia**—prominent in the first case; HPO: **HP:0003077 Hyperlipidemia**. Serum triglycerides were 638 mg/dL and cholesterol 552 mg/dL. (yachie2021hemeoxygenase1deficiency pages 3-4)
- **Systemic hyperinflammation/MAS-HLH-like episodes**—variable, particularly cases 7–9; HPO: **HP:0001945 Fever**, **HP:0410133 Hemophagocytosis**, **HP:0002910 Elevated hepatic transaminase**.
- **Vascular/coagulation disease**—hypertension, endothelial injury, extreme coagulation/fibrinolysis activation, occasional intracranial hemorrhage. HPO: **HP:0000822 Hypertension**, **HP:0002167 Neurological hemorrhage**, **HP:0001928 Abnormality of coagulation**. (yachie2021hemeoxygenase1deficiency pages 3-4, yachie2021hemeoxygenase1deficiency pages 12-13)
- **Pulmonary disease**—progressive fibrotic nonspecific interstitial pneumonia, hypoxemia, and cholesterol granulomas in the US patient; HPO: **HP:0002206 Pulmonary fibrosis**, **HP:0002091 Restrictive lung disease**, **HP:0012418 Hypoxemia**. (yachie2021hemeoxygenase1deficiency pages 6-7)
- **Growth delay and craniofacial appearance**—growth restriction was common but not universal; frontal bossing/prominent forehead, flat nasal bridge, and eyelid edema occurred in several patients. HPO: **HP:0001510 Growth delay**, **HP:0002007 Frontal bossing**, **HP:0005280 Depressed nasal bridge**, **HP:0000280 Coarse facial features** only if clinically documented.

Formal EQ-5D, SF-36, PROMIS, neurobehavioral, or disease-specific quality-of-life data do not exist. Severe anemia, recurrent hospitalization, transfusion dependence, organ failure, growth impairment, and respiratory limitation imply profound functional burden, but this has not been quantified.

## 4. Genetic and molecular information

**HMOX1** encodes the 288-amino-acid inducible heme oxygenase-1, an endoplasmic-reticulum-associated microsomal enzyme. Suggested annotations include **GO:0004392 heme oxygenase (decyclizing) activity**, **GO:0042167 heme catabolic process**, **GO:0006788 heme oxidation**, **GO:0055114 oxidation–reduction process**, and **GO:0005783 endoplasmic reticulum**.

The exon deletions, frameshift, nonsense, and canonical splice-donor variants are predicted loss-of-function. Patient cells carrying null variants failed to produce inducible HO-1 after cadmium, sodium arsenite, or cobalt protoporphyrin stimulation. p.K204Ter truncates the protein at 203 rather than 288 residues. p.G139V is mechanistically unusual: constitutive mutant protein was present, stress induction was defective, catalytic HO activity was reduced, and abnormal peroxidase activity and inflammatory cytokine production increased. (yachie2021hemeoxygenase1deficiency pages 3-4, yachie2021hemeoxygenase1deficiency pages 6-7)

No validated modifier gene, anticipation, germline mosaicism, pathogenic epigenetic signature, recurrent copy-number syndrome, aneuploidy, translocation, or inversion is known. Common HMOX1 promoter (GT)n polymorphisms regulate expression in other diseases but are **susceptibility modifiers, not established causes of this recessive deficiency**.

## 5. Environmental and infectious information

No toxin, radiation, pollutant, pathogen, or lifestyle exposure independently causes the disease. Infection can trigger systemic inflammation and is a major treatment hazard: one Indian patient died with fungal sepsis after immunosuppression. Hemolysis itself supplies excess extracellular heme; transfusion adds heme burden and provoked inflammation in the p.G139V patient. Hypoxia and vascular shear are additional endogenous stresses to HO-1-dependent cells. No zoonotic or transmissible component exists. (yachie2021hemeoxygenase1deficiency pages 6-7, yachie2021hemeoxygenase1deficiency pages 10-12, yachie2021hemeoxygenase1deficiency pages 4-6)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic HMOX1 loss or catalytic dysfunction.
2. **Primary biochemical defect:** impaired inducible conversion of heme to biliverdin, CO, and Fe²⁺, followed by reduced bilirubin production. This explains severe hemolysis accompanied by unexpectedly low bilirubin. (yachie2021hemeoxygenase1deficiency pages 1-3, yachie2021hemeoxygenase1deficiency pages 8-10)
3. **Heme/Hb accumulation and failed recycling:** extracellular oxyhemoglobin/methemoglobin and Hb–haptoglobin complexes accumulate. In the first patient, serum heme reached **490 µM** versus normal <1 µM, while haptoglobin paradoxically reached 800–1,200 mg/dL. (yachie2021hemeoxygenase1deficiency pages 3-4)
4. **Redox and metabolic injury:** unresolved heme catalyzes oxidative macromolecular and membrane damage; iron is misdistributed into renal tubular and hepatic cells rather than efficiently recycled. Loss of bilirubin/biliverdin antioxidant action and CO signaling further reduces stress tolerance.
5. **Monocyte/macrophage failure:** erythrophagocytic Kupffer and splenic macrophages cannot safely process heme, lose CD163/scavenging competence, die or become abnormally activated, and release TNF-α, IL-1β, and IL-6. Suggested GO terms: **GO:0006954 inflammatory response**, **GO:0006909 phagocytosis**, **GO:0030217 T-cell differentiation** only for downstream immune studies, **GO:0071345 cellular response to cytokine stimulus**. Cell Ontology: **CL:0000235 macrophage**, **CL:0000091 Kupffer cell**, **CL:0000576 monocyte**. (yachie2021hemeoxygenase1deficiency pages 12-13, yachie2021hemeoxygenase1deficiency pages 10-12)
6. **Endothelial dysfunction:** heme/ROS and inflammatory signaling activate NF-κB/MAPK and tissue factor, producing coagulation/fibrinolysis dysregulation, hypertension, thrombosis/bleeding, glomerular microvascular injury, and occasional cerebral hemorrhage. Cell Ontology: **CL:0000115 endothelial cell**; GO: **GO:0007596 blood coagulation**, **GO:0006979 response to oxidative stress**. (yachie2021hemeoxygenase1deficiency pages 3-4, yachie2021hemeoxygenase1deficiency pages 12-13)
7. **Downstream organ injury:** chronic inflammation, ischemia, fibrosis, iron deposition, and AA amyloid damage kidney, liver, spleen, lung, and cardiovascular tissues.

The primary patient-study abstract states that HO-1 deficiency causes “**enhanced endothelial cell injury**”; the 2021 synthesis concludes that impaired HO-1 causes “**progressive monocyte dysfunction, unregulated macrophage activation and endothelial cell dysfunction**.” These are authoritative mechanistic interpretations supported by patient tissue and cells, not merely computational inference. (yachie2021hemeoxygenase1deficiency pages 1-3, yachie2021hemeoxygenase1deficiency pages 15-16)

### Molecular profiling and advanced technology

There is no disease-specific human single-cell atlas, spatial transcriptomic study, lipidomic signature, integrated multi-omics cohort, or CRISPR screen. Whole-exome sequencing diagnosed post-mortem cases. Model metabolomics has connected HO-1 loss to impaired HIF-1α stabilization and ischemic metabolic adaptation, but this has not been validated as a diagnostic signature in affected humans. Epigenetic findings concern HMOX1 regulation generally, not the Mendelian disease.

## 7. Anatomy

**Primary organs:** blood/bone marrow, spleen, liver, kidneys, vascular endothelium, and monocyte–macrophage system. **Secondary/variable:** lung, heart/pericardium, brain vasculature, placenta, and growth tissues.

Suggested UBERON mappings include **UBERON:0000178 blood**, **UBERON:0001987 placental blood**, **UBERON:0002106 spleen**, **UBERON:0002107 liver**, **UBERON:0002113 kidney**, **UBERON:0002048 lung**, **UBERON:0000948 heart**, **UBERON:0001981 blood vessel**, **UBERON:0001225 renal tubule**, and **UBERON:0001285 glomerular capillary**. Relevant cells are erythrocytes (**CL:0000232**), erythroid progenitors (**CL:0000038**), monocytes, macrophages, Kupffer cells, renal tubular epithelial cells, hepatocytes (**CL:0000182**), podocytes (**CL:0000653**), and endothelial cells. Relevant compartments are ER membrane (**GO:0005789**), cytosol (**GO:0005829**), lysosome/phagolysosome (**GO:0005764/GO:0032010**), and extracellular blood space. No lateralization is expected.

## 8. Temporal development

Onset is usually pediatric but highly variable: **3 months–15 years** among the nine historical patients. Some children had congenital/early asplenia or growth disturbance; others remained apparently well until an inflammatory trigger. Once clinically active, disease may become rapidly progressive, with recurrent fever, worsening hemolysis, renal/endothelial injury, and multiorgan failure. The US pulmonary phenotype followed a chronic progressive course from age four to respiratory death at ten. There is no validated staging system or predictable remission pattern. (yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 6-7, yachie2021hemeoxygenase1deficiency pages 4-6)

Potential critical periods include fetal splenic/placental development, infancy with high erythrocyte turnover, and acute infections. Mouse data support fetal loss and placental vascular vulnerability, but prenatal human penetrance is unknown. A 2024 study found that HO-1 knockdown impaired trophoblast-spheroid attachment and that CO reversed this in vitro; Hmox1-null uterus showed altered angiogenesis/stress expression. This supports developmental biology but does not establish a human prenatal therapy. DOI [10.3390/cells13050376](https://doi.org/10.3390/cells13050376), published February 2024. (zenclussen2024absenceofheme pages 11-13)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Both sexes are affected; among the nine tabulated cases, six were male and three female, a sample too small to infer sex bias. Cases arose in Japan, India, Iran, Turkey, and the United States. Consanguinity contributed in two families, while the shared Indian p.R44X allele suggests a founder effect. Carrier parents are clinically unaffected, consistent with recessive transmission. (yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 6-7)

No incidence, prevalence per 100,000, carrier frequency, penetrance estimate, or population registry exists. “Nine cases by 2021” is a **reported-case count**, not prevalence. Embryonic lethality in mice and fetal losses in two families raise the possibility of prenatal under-ascertainment, but this remains an expert hypothesis. (yachie2021hemeoxygenase1deficiency pages 3-4, yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 8-10)

## 10. Diagnostics

### When to suspect the disorder

The highest-yield pattern is:

1. Coombs-negative fragmented-cell hemolytic anemia;
2. strikingly **low/normal bilirubin despite hemolysis**;
3. LDH and ferritin often in the thousands to tens of thousands;
4. leukocytosis plus thrombocytosis rather than HLH-like cytopenias;
5. asplenia/hyposplenia without congenital heart disease, or unexplained splenomegaly;
6. fever/systemic inflammation, hepatomegaly, proteinuria/hematuria, hypertension, or interstitial lung disease. (yachie2021hemeoxygenase1deficiency pages 3-4, yachie2021hemeoxygenase1deficiency pages 8-10)

### Tests

- **CBC/smear:** anemia, schistocytes/fragmented erythrocytes, nucleated RBCs, Howell–Jolly bodies, leukocytosis, thrombocytosis.
- **Hemolysis/heme:** LDH, bilirubin fractions, haptoglobin, plasma-free Hb/heme, methemoglobin, hemopexin, reticulocytes, urinalysis; direct antiglobulin testing is usually negative.
- **Inflammation/organ assessment:** ferritin, CRP/ESR, triglycerides, AST/ALT, renal function, urine protein/creatinine, coagulation/fibrinolysis markers, cytokines where available.
- **Imaging:** abdominal ultrasound/CT for spleen and liver; echocardiography for pericardial/cardiac disease; high-resolution chest CT and pulmonary function testing for respiratory disease; brain imaging when hypertensive or neurologically symptomatic.
- **Pathology:** kidney may show endothelial swelling, mesangial proliferation and tubular atrophy; liver may show Kupffer-cell/parenchymal iron, extramedullary hematopoiesis, hemophagocytosis or AA amyloid; lung may show fibrotic NSIP and cholesterol granulomas. (yachie2021hemeoxygenase1deficiency pages 6-7, yachie2021hemeoxygenase1deficiency pages 10-12, yachie2021hemeoxygenase1deficiency pages 4-6)
- **Functional assay:** absent or noninducible HO-1 protein/activity in stimulated PBMCs, monocytes, fibroblasts, or lymphoblastoid cells can support pathogenicity, especially for missense variants.

### Genetic testing strategy

Sequence **HMOX1** with deletion/duplication and splice analysis. A heme-metabolism/hemolytic-anemia/autoinflammatory panel can be used, but the laboratory must include HMOX1 and copy-number calling. WES/WGS is appropriate when the phenotype is atypical or first-line testing is negative; several cases were diagnosed by post-mortem WES. RNA sequencing may demonstrate aberrant splicing for c.636+2T>A or other splice variants. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion assays are not first-line unless another diagnosis is suspected. Cascade parental testing establishes phase. (yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 4-6)

### Differential diagnosis

Exclude thrombotic microangiopathy/HUS, autoimmune hemolysis, hereditary red-cell membrane/enzyme disorders, congenital asplenia syndromes, familial HLH/MAS, systemic juvenile idiopathic arthritis, CAPS/NOMID, vasculitis, infection, malignancy, Wilson disease, aceruloplasminemia, and other iron-recycling disorders. Low bilirubin with very high LDH/ferritin and thrombocytosis plus asplenia is especially discriminating from conventional hemolysis and HLH.

There are no standardized diagnostic criteria, newborn screen, approved enzyme assay, or population-screening program.

## 11. Outcome and prognosis

Prognosis is frequently poor but cannot be represented by five- or ten-year survival statistics. Several reported children died soon after onset or diagnosis from fungal sepsis, intracranial hemorrhage, heart failure/bleeding, or respiratory failure. The Indian p.R44X series showed prolonged asymptomatic periods followed by rapid decline; the US patient died at ten after six years of progressive lung disease. (yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 4-6)

Major morbidity includes transfusion-dependent anemia, recurrent inflammatory hospitalization, chronic kidney disease/proteinuria, hypertension, cerebral bleeding, hepatic damage/amyloidosis, splenic dysfunction and infection risk, growth failure, pulmonary fibrosis, and heart failure. Prognostic factors are unvalidated; plausible adverse markers include very early onset, sustained hyperinflammation, pulmonary fibrosis, renal amyloid, severe endothelial dysfunction, and inability to control triggers. No validated prognostic biomarker or quality-of-life instrument exists.

## 12. Treatment

### Current clinical management

There is **no approved disease-specific therapy or consensus algorithm**. Management is multidisciplinary and supportive:

- stabilize severe anemia, but transfuse cautiously and monitor inflammation/heme burden;
- promptly identify and treat infection;
- manage hypertension, renal disease/proteinuria, respiratory failure, coagulopathy, heart failure, and nutrition/growth;
- apply asplenia precautions: vaccination against encapsulated bacteria, fever action plan, and jurisdiction-appropriate antibiotic prophylaxis;
- avoid iron supplementation unless iron deficiency is objectively established—the p.G139V patient’s microcytic anemia was iron-unresponsive.

Suggested NCIt concepts include **Blood Transfusion**, **Corticosteroid Therapy**, **Immunosuppressive Therapy**, **Anti-inflammatory Therapy**, **Hematopoietic Stem Cell Transplantation**, **Gene Therapy**, and **Supportive Care**; exact NCIt codes should be resolved against the current thesaurus release.

### Reported therapies and outcomes

Corticosteroids were ineffective in the Iranian patient. The Turkish patient received HLH-2004 immunochemotherapy, achieving remission of HLH-like signs but persistent biochemical inflammation. In the US case, corticosteroids, IL-1 receptor blockade, IL-6 blockade, and cyclosporine provided minimal benefit; death followed from respiratory failure. Broad immunosuppression can increase infection risk and does not correct failed heme catabolism. (yachie2021hemeoxygenase1deficiency pages 7-8, yachie2021hemeoxygenase1deficiency pages 6-7, yachie2021hemeoxygenase1deficiency pages 4-6)

### Experimental strategies

- **Macrophage/cell replacement:** wild-type macrophages reversed disease in Hmox1-null mice, supporting replacement of the erythrophagocytic compartment. This is compelling model evidence, not proven human therapy. Primary report: *Blood* 2014;124:1522–1530, DOI [10.1182/blood-2014-02-554162](https://doi.org/10.1182/blood-2014-02-554162). (yachie2021hemeoxygenase1deficiency pages 15-16)
- **CO or CO-releasing molecules:** CO can restore anti-inflammatory/endothelial signaling and rescued implantation or vascular phenotypes in models. Safety, dosing, and efficacy in congenital deficiency are unestablished. (yachie2021hemeoxygenase1deficiency pages 13-15, yachie2021hemeoxygenase1deficiency pages 12-13, zenclussen2024absenceofheme pages 11-13)
- **Gene replacement/editing or autologous corrected hematopoietic stem cells:** mechanistically attractive because macrophages are central, but no human trial or reported implementation was identified.
- **Haptoglobin/hemopexin/CD163 pathway augmentation, biliverdin/bilirubin replacement, antioxidants, and iron redistribution therapy:** preclinical concepts only.

The ClinicalTrials.gov tool search found no relevant disease-specific interventional study and no NCT identifier. There are no established response rates, pharmacogenomic recommendations, RNA therapy, surgery, or approved targeted biologic.

## 13. Prevention

Primary prevention is limited to **genetic counseling**. For a carrier couple, each pregnancy has the standard autosomal-recessive probabilities: 25% affected, 50% carrier, and 25% unaffected/noncarrier, assuming both parental variants are confirmed. Targeted prenatal diagnosis and preimplantation genetic testing are technically feasible. Cascade testing should be offered to adult relatives.

Secondary prevention consists of early recognition in siblings or children with the diagnostic laboratory pattern, followed by HMOX1 testing before irreversible kidney, vascular, or lung injury. There is no population or newborn screening. Tertiary prevention includes asplenia vaccination/prophylaxis, infection control, blood-pressure and renal monitoring, cautious transfusion, respiratory surveillance, and avoidance of unnecessary oxidative/toxic exposures. No vaccine prevents the genetic disease itself.

## 14. Other species and natural disease

No naturally occurring veterinary HMOX1-deficiency syndrome, breed association, or zoonotic transmission was identified. Relevant taxa are **Homo sapiens (NCBI Taxon 9606)**, **Mus musculus (10090)**, **Rattus norvegicus (10116)**, and **Danio rerio (7955)**. Orthologs are Hmox1 in mouse/rat and hmox1a/hmox1b paralogs in zebrafish. Comparative evidence demonstrates strong evolutionary conservation of heme detoxification, iron recycling, macrophage survival, and vascular protection, but induced knockout phenotypes should not be mislabeled as natural animal disease.

## 15. Model organisms and experimental systems

### Mouse

Global **Hmox1-null mice** reproduce anemia, defective iron reutilization, renal/hepatic iron deposition, chronic inflammation, growth delay, oxidative-stress hypersensitivity, and splenic pathology. Depending on genetic background and age, spleens enlarge or progress from enlargement to fibrosis, atrophy, and functional hyposplenism. Null embryonic fibroblasts are hypersensitive to hemin, hydrogen peroxide, paraquat, and heavy metals. These are the highest-fidelity models for systemic disease, although mouse splenic development and survival vary by strain. Primary reports: Poss & Tonegawa, *PNAS* 1997;94:10919–10924 and 10925–10930. (yachie2021hemeoxygenase1deficiency pages 8-10, yachie2021hemeoxygenase1deficiency pages 15-16)

Macrophage-focused studies show erythrophagocytic macrophage death, reduced CD163, and altered tissue iron distribution. Infusion of wild-type macrophages can reverse key disease features, identifying macrophages as both a pathogenic hub and therapeutic target. Mouse studies also demonstrate abnormal erythroblastic islands, microcytic anemia, oxidative RBC stress, endothelial thrombosis, ischemic necrosis, inflammasome activation, and developmental/placental defects. Limitations are substantial embryonic loss, strain-dependent spleen phenotypes, and incomplete reproduction of human pulmonary or amyloid disease.

### Rat

HO-1-depleted Sprague–Dawley rats develop hemolytic anemia, poikilocytes/target cells/acanthocytes, leukocytosis, growth impairment, splenomegaly, proteinuria, mesangial expansion, focal segmental sclerosis, and podocyte edema; most died by six months. Unlike humans and mice, renal tubular/hepatic iron deposition was not prominent, illustrating species-specific iron handling. (yachie2021hemeoxygenase1deficiency pages 8-10, yachie2021hemeoxygenase1deficiency pages 10-12)

### Zebrafish and cellular systems

Zebrafish hmox1a disruption affects development and macrophage migration and is useful for imaging innate immune behavior, but duplicated genes and aquatic physiology limit direct clinical translation. Patient PBMCs, monocytes, lymphoblastoid cells, fibroblasts, HUVECs, trophoblast spheroids, and Hmox1-null embryonic fibroblasts support functional variant testing and investigation of oxidative stress, cytokines, coagulation, hypoxia, and CO rescue.

## Recent developments and expert interpretation

The most disease-relevant recent clinical developments are: (1) a 2023 report expanding the renal spectrum to **AA-type renal amyloidosis** (*Clinical Rheumatology* 42:597–606; online 2022, issue 2023; DOI [10.1007/s10067-022-06465-9](https://doi.org/10.1007/s10067-022-06465-9)); (2) a 2024 clinical/molecular report of a novel variant with inflammation, heme-metabolism abnormalities, and pulmonary disease (*Molecular Genetics and Metabolism Reports* 38:101038; DOI [10.1016/j.ymgmr.2023.101038](https://doi.org/10.1016/j.ymgmr.2023.101038)); and (3) a 2024 case report/review (*Clinical Case Reports*, DOI [10.1002/ccr3.8986](https://doi.org/10.1002/ccr3.8986)). These publications indicate continuing phenotype expansion, not a change in standard care.

Current expert analysis increasingly emphasizes **heme-detoxifying macrophages** rather than treating HO-1 merely as a generic antioxidant. A 2024 review describes macrophage HMOX1 as essential for limiting oxidative damage in hemolytic disorders and for balancing inflammation and ferroptosis (published March 2024, DOI [10.3389/fimmu.2024.1379967](https://doi.org/10.3389/fimmu.2024.1379967)). Another 2024 review stresses that erythrophagocyte HO-1 converts heme into CO, biliverdin and Fe²⁺ while controlling apoptosis, inflammation, and oxidative injury (published October 2024, DOI [10.3389/fimmu.2024.1433113](https://doi.org/10.3389/fimmu.2024.1433113)). This supports macrophage replacement or corrected hematopoietic-cell strategies, but human efficacy remains wholly unproven.

## Data-quality conclusions

The disease signature is strong and internally consistent, but evidence quality is constrained by single cases, retrospective descriptions, publication bias, and genotype/age heterogeneity. Frequencies should therefore be stored with denominators and an evidence tag such as **“9-case literature series, through 2021”**. Variant-level ClinVar/gnomAD status, current MONDO/Orphanet identifiers, exact incidence, standardized diagnostic criteria, natural-history survival, patient-reported outcomes, and treatment-response rates remain unavailable or require direct database validation. Mechanistic confidence is highest for defective heme catabolism, macrophage/endothelial dysfunction, oxidative injury, and iron misdistribution; confidence is lower for proposed CO, macrophage, stem-cell, or gene therapies because these are supported predominantly by models rather than treated patients.

References

1. (yachie2021hemeoxygenase1deficiency pages 1-3): Akihiro Yachie. Heme oxygenase-1 deficiency and oxidative stress: a review of 9 independent human cases and animal models. International Journal of Molecular Sciences, 22:1514, Feb 2021. URL: https://doi.org/10.3390/ijms22041514, doi:10.3390/ijms22041514. This article has 104 citations.

2. (yachie2021hemeoxygenase1deficiency pages 15-16): Akihiro Yachie. Heme oxygenase-1 deficiency and oxidative stress: a review of 9 independent human cases and animal models. International Journal of Molecular Sciences, 22:1514, Feb 2021. URL: https://doi.org/10.3390/ijms22041514, doi:10.3390/ijms22041514. This article has 104 citations.

3. (yachie2021hemeoxygenase1deficiency pages 7-8): Akihiro Yachie. Heme oxygenase-1 deficiency and oxidative stress: a review of 9 independent human cases and animal models. International Journal of Molecular Sciences, 22:1514, Feb 2021. URL: https://doi.org/10.3390/ijms22041514, doi:10.3390/ijms22041514. This article has 104 citations.

4. (yachie2021hemeoxygenase1deficiency pages 6-7): Akihiro Yachie. Heme oxygenase-1 deficiency and oxidative stress: a review of 9 independent human cases and animal models. International Journal of Molecular Sciences, 22:1514, Feb 2021. URL: https://doi.org/10.3390/ijms22041514, doi:10.3390/ijms22041514. This article has 104 citations.

5. (yachie2021hemeoxygenase1deficiency pages 4-6): Akihiro Yachie. Heme oxygenase-1 deficiency and oxidative stress: a review of 9 independent human cases and animal models. International Journal of Molecular Sciences, 22:1514, Feb 2021. URL: https://doi.org/10.3390/ijms22041514, doi:10.3390/ijms22041514. This article has 104 citations.

6. (yachie2021hemeoxygenase1deficiency pages 3-4): Akihiro Yachie. Heme oxygenase-1 deficiency and oxidative stress: a review of 9 independent human cases and animal models. International Journal of Molecular Sciences, 22:1514, Feb 2021. URL: https://doi.org/10.3390/ijms22041514, doi:10.3390/ijms22041514. This article has 104 citations.

7. (yachie2021hemeoxygenase1deficiency pages 13-15): Akihiro Yachie. Heme oxygenase-1 deficiency and oxidative stress: a review of 9 independent human cases and animal models. International Journal of Molecular Sciences, 22:1514, Feb 2021. URL: https://doi.org/10.3390/ijms22041514, doi:10.3390/ijms22041514. This article has 104 citations.

8. (yachie2021hemeoxygenase1deficiency pages 8-10): Akihiro Yachie. Heme oxygenase-1 deficiency and oxidative stress: a review of 9 independent human cases and animal models. International Journal of Molecular Sciences, 22:1514, Feb 2021. URL: https://doi.org/10.3390/ijms22041514, doi:10.3390/ijms22041514. This article has 104 citations.

9. (yachie2021hemeoxygenase1deficiency pages 10-12): Akihiro Yachie. Heme oxygenase-1 deficiency and oxidative stress: a review of 9 independent human cases and animal models. International Journal of Molecular Sciences, 22:1514, Feb 2021. URL: https://doi.org/10.3390/ijms22041514, doi:10.3390/ijms22041514. This article has 104 citations.

10. (yachie2021hemeoxygenase1deficiency pages 12-13): Akihiro Yachie. Heme oxygenase-1 deficiency and oxidative stress: a review of 9 independent human cases and animal models. International Journal of Molecular Sciences, 22:1514, Feb 2021. URL: https://doi.org/10.3390/ijms22041514, doi:10.3390/ijms22041514. This article has 104 citations.

11. (zenclussen2024absenceofheme pages 11-13): Maria Laura Zenclussen, Sina Ulrich, Mario Bauer, Beate Fink, Ana Claudia Zenclussen, Anne Schumacher, and Nicole Meyer. Absence of heme oxygenase-1 affects trophoblastic spheroid implantation and provokes dysregulation of stress and angiogenesis gene expression in the uterus. Cells, 13(5):376, Feb 2024. URL: https://doi.org/10.3390/cells13050376, doi:10.3390/cells13050376. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](Heme_Oxygenase_1_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.