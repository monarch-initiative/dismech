---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T07:18:31.312353'
end_time: '2026-08-20T07:30:04.127033'
duration_seconds: 692.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Fibrosis of the Extraocular Muscles
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
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Congenital_Fibrosis_of_the_Extraocular_Muscles-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Fibrosis of the Extraocular Muscles
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Fibrosis of the Extraocular Muscles** covering all of the
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
- **Disease Name:** Congenital Fibrosis of the Extraocular Muscles
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Fibrosis of the Extraocular Muscles** covering all of the
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


# Congenital Fibrosis of the Extraocular Muscles (CFEOM): Disease-Characteristics Report

## Executive summary

Congenital fibrosis of the extraocular muscles (CFEOM) is a genetically heterogeneous **congenital cranial dysinnervation disorder (CCDD)**. Despite its historical name, it is primarily a developmental neurologic disorder: abnormal specification or axon growth/guidance of ocular motor neurons produces deficient or aberrant innervation, followed secondarily by extraocular-muscle hypoplasia, contracture, and fibrosis. The defining manifestations are congenital, usually nonprogressive restrictive ophthalmoplegia, strabismus, and frequently ptosis. CFEOM1 is most often caused by dominant **KIF21A** variants, CFEOM2 by biallelic **PHOX2A** loss-of-function variants, and CFEOM3 by dominant **TUBB3** variants; rarer CFEOM-like phenotypes involve **TUBA1A** and **TUBB2B**. Mechanisms converge on motor-neuron specification, neuronal microtubule dynamics, kinesin–microtubule interactions, and cranial-axon pathfinding. (fritzsch2023evolutionanddevelopment pages 16-18, whitman2021axonalgrowthabnormalities pages 6-8, puri2023tubb3andkif21a pages 20-21)

There is no disease-modifying pharmacotherapy. Current care consists of amblyopia prevention, refractive correction, ocular-surface protection, and individualized strabismus and ptosis surgery. Population prevalence, health-related quality-of-life scores, long-term prospective outcomes, and controlled treatment-response rates remain poorly characterized.

## 1. Disease information

### Definition and classification

CFEOM is a Mendelian CCDD characterized by congenital restriction of eye movements, generally accompanied by incomitant strabismus and ptosis. Human autopsy, MRI, and model-organism data shifted the accepted interpretation from a primary extraocular-muscle disease to **primary developmental dysinnervation with secondary muscle fibrosis**. In genetically confirmed CFEOM1, human pathology showed absence of the superior division of cranial nerve III (CN III) and corresponding motor neurons; MRI showed profound hypoplasia of the superior rectus and levator palpebrae superioris and abnormalities of ocular motor nerves. (whitman2021axonalgrowthabnormalities pages 6-8)

**Common names:** congenital fibrosis of the extraocular muscles; CFEOM; congenital external ophthalmoplegia; congenital restrictive ophthalmoplegia; generalized fibrosis syndrome; congenital ophthalmoplegia; and, historically, congenital fibrosis syndrome. “CFEOM” should be preferred because congenital external ophthalmoplegia has broader differential diagnoses.

**Disease-level versus patient-level evidence:** This report synthesizes aggregated disease-level resources, cohorts, pedigrees, case series, neuroimaging, animal models, and biochemical experiments. It does not contain identifiable EHR-derived patient data. The 2022 Chinese study, for example, aggregated 122 affected individuals from 96 families, while the recent large oCCDD genomics study analyzed 467 unsolved pedigrees. (jia2022clinicalandgenetic pages 13-14, jurgens2025expandingthegenetics pages 38-41)

### Identifiers

Identifiers should be represented at both umbrella and subtype levels because CFEOM is genetically heterogeneous.

- **OMIM phenotype entries commonly used:** CFEOM1, **135700**; CFEOM2, **602078**; CFEOM3A, **600638**. Individual gene–disease records should also be linked for KIF21A, PHOX2A, and TUBB3.
- **Orphanet:** “Congenital fibrosis of the extraocular muscles” and subtype records are available through the Orphanet nomenclature portal: https://www.orpha.net/.
- **MONDO:** use the current MONDO record returned for “congenital fibrosis of extraocular muscles” in the release being ingested; subtype mappings should be preserved. A MONDO identifier was not independently recoverable from the retrieved primary-literature corpus and should therefore be database-validated rather than inferred.
- **ICD-10-CM:** no highly specific CFEOM code; coding usually uses congenital malformation of eye/ocular motor disorder, strabismus, ophthalmoplegia, or ptosis codes according to manifestation.
- **ICD-11:** use the applicable developmental anomaly/ocular-motility category, supplemented by an Orphanet or OMIM identifier where the implementation permits rare-disease extension codes.
- **MeSH:** no uniquely specific CFEOM descriptor was established from the retrieved literature; indexing commonly falls under ophthalmoplegia, strabismus, eye-movement disorders, and congenital abnormalities.

The following table provides the core genotype–phenotype structure.

| Subtype / OMIM status | Principal gene | Inheritance | Hallmark ocular phenotype | Associated / systemic findings | Principal developmental mechanism |
|---|---|---|---|---|---|
| CFEOM1 / OMIM not asserted here | **KIF21A** | Autosomal dominant; often familial, can be de novo | Congenital bilateral ptosis; eyes typically fixed infraducted; severe limitation of upgaze with variable horizontal restriction | Usually isolated ocular phenotype, though syndromic presentations are reported in some variant contexts; MRI/human pathology show hypoplastic superior rectus and levator with oculomotor nerve abnormalities (whitman2021axonalgrowthabnormalities pages 6-8, fritzsch2023evolutionanddevelopment pages 14-16) | Gain-of-function/missense mechanism that reduces KIF21A autoinhibition, alters kinesin-microtubule behavior, and stalls superior-division CN III axon growth/guidance during development (whitman2021axonalgrowthabnormalities pages 6-8, puri2023tubb3andkif21a pages 20-21) |
| CFEOM2 / OMIM not asserted here | **PHOX2A** | Autosomal recessive | Congenital bilateral ptosis with exotropia at rest and profound restriction of ocular movements | MRI evidence of absent oculomotor and trochlear nerves; may be accompanied by pupil abnormalities in classic descriptions; generally a cranial motor neuron specification disorder (fritzsch2023evolutionanddevelopment pages 16-18) | Loss of PHOX2A function disrupts specification/development of oculomotor and trochlear motor neuron nuclei, causing failure of normal innervation to extraocular muscles (fritzsch2023evolutionanddevelopment pages 16-18) |
| CFEOM3 / OMIM not asserted here | **TUBB3** | Autosomal dominant; variable expressivity, including de novo cases | Variable congenital ophthalmoplegia, often asymmetric; ptosis may be unilateral or bilateral; limited upgaze common, horizontal deficits variable | Can be isolated or syndromic; reported associations include additional cranial/peripheral neuropathy features and white-matter/brain abnormalities depending on variant (fritzsch2023evolutionanddevelopment pages 16-18, jia2022clinicalandgenetic pages 13-14) | Missense variants in neuronal β-tubulin III alter microtubule dynamics and kinesin interaction, impairing cranial axon growth, maintenance, and guidance (fritzsch2023evolutionanddevelopment pages 16-18, puri2023tubb3andkif21a pages 20-21) |
| Rare CFEOM-associated phenotype / OMIM not asserted here | **TUBA1A** | Typically autosomal dominant / de novo in reported cases | CFEOM phenotype with congenital ophthalmoplegia/ptosis | May occur with or without malformations of cortical development; broader tubulinopathy features can be present (jia2022clinicalandgenetic pages 13-14) | Altered α-tubulin function perturbs neuronal microtubules, cranial axon guidance, and in some cases cortical development (jia2022clinicalandgenetic pages 13-14) |
| Rare CFEOM-associated phenotype / OMIM not asserted here | **TUBB2B** | Typically autosomal dominant in reported families | CFEOM/ophthalmoplegia phenotype | Can be associated with polymicrogyria and broader axon dysinnervation syndrome rather than isolated CFEOM (jia2022clinicalandgenetic pages 13-14) | Altered β-tubulin/kinesin-binding interface disrupts axon guidance and brain development (jia2022clinicalandgenetic pages 13-14) |


*Table: This table summarizes the main genetically defined CFEOM subtypes and rarer tubulin-associated presentations, highlighting inheritance, distinguishing ocular findings, systemic associations, and developmental mechanisms. It is useful as a compact knowledge-base scaffold when exact identifiers are uncertain or subtype boundaries overlap.*

## 2. Etiology, risk, and protective factors

### Causal factors

The principal cause is a **germline pathogenic variant affecting ocular motor-neuron development**:

- **KIF21A:** usually heterozygous missense variants causing autosomal-dominant CFEOM1 and occasionally CFEOM3-like or syndromic phenotypes. Variants cluster in motor/stalk regions and reduce normal autoinhibition, producing an altered or gain-of-function state. (fritzsch2023evolutionanddevelopment pages 16-18, puri2023tubb3andkif21a pages 20-21)
- **PHOX2A:** biallelic loss-of-function variants causing autosomal-recessive CFEOM2 through failure of oculomotor and trochlear motor-neuron specification. (fritzsch2023evolutionanddevelopment pages 16-18)
- **TUBB3:** heterozygous missense variants causing autosomal-dominant CFEOM3, ranging from isolated ocular disease to multisystem neurodevelopmental tubulinopathy. (fritzsch2023evolutionanddevelopment pages 16-18, puri2023tubb3andkif21a pages 20-21)
- **TUBA1A and TUBB2B:** rare dominant/de novo tubulinopathy-associated CFEOM phenotypes, sometimes with cortical malformations such as polymicrogyria. These should not be treated as equally common causes of classic isolated CFEOM. (jia2022clinicalandgenetic pages 13-14)

### Genetic risk factors

A pathogenic familial allele, an affected parent, and consanguinity in recessive PHOX2A disease are the clinically relevant risk factors. Dominant cases may also arise de novo. Variable expressivity is particularly important in TUBB3-related and some KIF21A-related disease; absence of severe ophthalmoplegia in a parent does not automatically exclude familial transmission. (fritzsch2023evolutionanddevelopment pages 16-18, fritzsch2023evolutionanddevelopment pages 14-16)

A common allele is not evidence of causality: the KIF21A 3′-UTR deletion c.*690del has a reported gnomAD allele frequency of **0.1377**, including 156 homozygotes, and is therefore incompatible with being a highly penetrant cause of rare dominant CFEOM. The frameshift c.4602_4606del, p.(Thr1535GlnfsTer3), was reported as a VUS rather than an established pathogenic allele. (puri2023tubb3andkif21a pages 20-21)

### Environmental, lifestyle, infectious, and protective factors

No reproducible toxin, infection, radiation exposure, diet, smoking behavior, occupation, or other environmental exposure is established as a cause or modifier of genetically defined CFEOM. No validated protective allele, diet, medication, or lifestyle intervention prevents the developmental dysinnervation. Accordingly, conventional gene–environment interaction models are not currently supported. These are evidence gaps, not proof that modifiers cannot exist.

## 3. Phenotypes

### Core ocular phenotype

| Phenotype | Type and suggested HPO term | Onset/course | Typical pattern and impact |
|---|---|---|---|
| Restrictive ophthalmoplegia | Sign: **Ophthalmoplegia, HP:0000602**; limitation of extraocular movement | Congenital; chronic and usually nonprogressive | Vertical restriction is prominent; horizontal restriction varies. Limits visual-field access and drives compensatory head posture. |
| Ptosis | Sign: **Blepharoptosis, HP:0000508** | Congenital; stable, severity variable | Usually bilateral in CFEOM1/2; may be asymmetric in CFEOM3. Severe ptosis can obstruct the visual axis and contribute to amblyopia. |
| Strabismus | Sign: **Strabismus, HP:0000486** | Congenital; persistent | CFEOM1 commonly has infraducted eyes; CFEOM2 typically exotropia; CFEOM3 is variable/asymmetric. |
| Absent or limited upgaze | Sign: limitation of upward gaze; map to the most specific current HPO ocular-motility term | Congenital; stable | Characteristic of CFEOM1 and frequent in CFEOM3. |
| Abnormal head posture | Physical manifestation: **Abnormal head posture, HP:0002186** | Early childhood onward | Chin elevation or face turn compensates for restricted primary gaze; may impair mobility and cause musculoskeletal discomfort. |
| Amblyopia/reduced acuity | Complication: **Amblyopia, HP:0000646**; **Reduced visual acuity, HP:0007663** | Develops during childhood visual maturation | Related to ptosis, anisometropia, or strabismus; potentially preventable with early ophthalmic care. |
| Refractive error | Clinical sign: **Abnormality of refraction, HP:0000539** | Childhood | Requires cycloplegic refraction and correction. |
| Pupil abnormality | Sign: **Abnormality of the pupil, HP:0000615** | Congenital | Particularly relevant in PHOX2A/CFEOM2 and selected TUBB3 phenotypes. |

CFEOM1 classically presents with bilateral ptosis, eyes fixed below the horizontal midline, absent vertical movement, and variably limited horizontal movement. CFEOM2 combines bilateral ptosis, exotropia, severe movement restriction, and absent CN III/CN IV on MRI. CFEOM3 is more variable and often asymmetric, with variable ptosis and limited upgaze. (fritzsch2023evolutionanddevelopment pages 16-18, fritzsch2023evolutionanddevelopment pages 14-16)

### Syndromic manifestations

Variant-specific TUBB3 disease may add facial weakness, additional cranial neuropathies, peripheral neuropathy, developmental delay, intellectual disability, corpus-callosal or white-matter abnormalities, and other brain malformations. TUBA1A/TUBB2B disease can include cortical malformations. These findings are not obligatory in classic isolated CFEOM and should trigger broader neurologic evaluation. (fritzsch2023evolutionanddevelopment pages 16-18, jia2022clinicalandgenetic pages 13-14)

In the 2022 Chinese CCDD cohort, **46/96 families (47.9%)** had multiple congenital malformations. Among 88 families with high-resolution MRI, **15/88 (17.0%)** had additional craniocerebral malformations. These percentages concern a mixed CCDD cohort and must not be presented as CFEOM-specific population frequencies. (jia2022clinicalandgenetic pages 13-14)

### Quality of life

No robust CFEOM-specific EQ-5D, SF-36, PROMIS, or utility-weight dataset was found. Likely burdens include restricted field of binocular single vision, abnormal head posture, cosmetic/social effects of ptosis and strabismus, repeated surgery, amblyopia risk, and—where syndromic—neurologic disability. These impacts are clinically credible but lack disease-specific population estimates.

## 4. Genetic and molecular information

### Principal genes and variant classes

- **KIF21A** — dominant missense variants are the canonical mechanism. The recurrent p.Arg954Trp allele remains a representative pathogenic variant. Most disease alleles alter motor/stalk-domain autoinhibition rather than simply abolishing protein production. (whitman2021axonalgrowthabnormalities pages 6-8, jurgens2025expandingthegenetics pages 36-37)
- **PHOX2A** — recessive nonsense, frameshift, splice, or damaging missense variants causing loss of function.
- **TUBB3** — dominant missense variants; genotype strongly influences whether disease remains ocular or includes broader cranial/peripheral nerve and cerebral involvement. Reported variants with syndromic phenotypes include p.Arg262His and p.Arg380Cys; the Chinese cohort also associated p.Glu410Lys with syndromic findings. (jia2022clinicalandgenetic pages 13-14)
- **TUBA1A/TUBB2B** — predominantly heterozygous missense alleles with combined CFEOM and malformation-of-cortical-development phenotypes. (jia2022clinicalandgenetic pages 13-14)

All established CFEOM variants are **germline**. Somatic mosaicism is not a recognized principal mechanism, although low-level parental germline or somatic mosaicism may theoretically explain recurrence after an apparently de novo case. Population databases should be checked using the exact transcript and genome build; highly penetrant causal alleles are expected to be absent or exceptionally rare.

### Diagnostic yields and recent genomics

In the 2022 Chinese cohort, WES identified ten pathogenic variants in **KIF21A, TUBB3, and CHN1** across 43 families; 42 of the 43 genetically solved probands had CFEOM. Novel reported variants included KIF21A c.1064T>C, p.Phe355Ser; TUBB3 c.232T>A, p.Ser78Thr; and CHN1 c.650A>G, p.His217Arg. The authors concluded that “**KIF21A and TUBB3 were the common pathogenic genes in Chinese CFEOM**” and that MRI plus WES supported diagnosis. (jia2022clinicalandgenetic pages 13-14)

A later analysis of **467 previously unsolved oCCDD pedigrees**, including 198 CFEOM probands, found pathogenic/likely pathogenic variants in **43/467 (9.2%)** and prioritized VUS in another **70/467 (15.0%)**. Candidate findings extended beyond established genes to MYH10, KIF21B, TUBB6, TUBA4A, KIF5C, and others, but these newer gene associations require independent replication and functional validation before routine designation as definitive CFEOM genes. (jurgens2025expandingthegenetics pages 8-12, jurgens2025expandingthegenetics pages 38-41)

### Modifier genes, epigenetics, and chromosomal abnormalities

No replicated CFEOM modifier gene or disease-specific epigenetic signature is established. Structural variants and chromosomal disruptions can produce oCCDD phenocopies or syndromic disease, so genome sequencing or chromosomal microarray is appropriate in unresolved syndromic cases. The recent 467-pedigree study explicitly integrated structural-variant analysis and found extensive heterogeneity. (jurgens2025expandingthegenetics pages 8-12, jurgens2025expandingthegenetics pages 38-41)

## 5. Environmental information

CFEOM is not known to be infectious, toxic, occupational, nutritional, radiation-induced, inflammatory, or lifestyle-mediated. Smoking, alcohol, diet, and exercise do not have established effects on disease occurrence. Environmental interventions cannot reverse embryonic cranial dysinnervation, although ordinary eye safety, ocular-surface care, and adherence to amblyopia treatment can reduce secondary morbidity.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** pathogenic variant in PHOX2A, KIF21A, TUBB3, or another microtubule/axon-development gene.
2. **Developmental cellular defect:** failure of ocular motor-neuron specification (PHOX2A) or abnormal microtubule dynamics, motor-protein regulation, axon elongation, and guidance (KIF21A/TUBB3).
3. **Neuroanatomic consequence:** absent, hypoplastic, stalled, or misrouted CN III/IV/VI axons and abnormal innervation of extraocular muscles.
4. **Secondary tissue consequence:** denervation-related extraocular-muscle hypoplasia, contracture, and fibrosis.
5. **Clinical phenotype:** congenital ophthalmoplegia, fixed strabismus, ptosis, compensatory head posture, and amblyopia risk. (fritzsch2023evolutionanddevelopment pages 16-18, whitman2021axonalgrowthabnormalities pages 6-8)

### KIF21A mechanism

KIF21A is an anterograde kinesin. Normally, interaction between the motor domain and the third coiled-coil stalk domain maintains a closed, autoinhibited state. CFEOM-associated missense variants attenuate this autoinhibition, increase microtubule association, and dysregulate cortical microtubule growth. In knock-in mice, superior-division CN III axons stall proximally in bulb-like enlargements containing abnormal growth cones and degenerating axons; distal nerve and target muscles are hypoplastic. (whitman2021axonalgrowthabnormalities pages 6-8, puri2023tubb3andkif21a pages 20-21)

### PHOX2A mechanism

PHOX2A is a transcription factor required for development/specification of oculomotor and trochlear motor neurons. Loss of function prevents proper formation of these nuclei, explaining the MRI absence of CN III and CN IV and the profound CFEOM2 phenotype. (fritzsch2023evolutionanddevelopment pages 16-18)

### TUBB3 mechanism

TUBB3 encodes neuron-enriched βIII-tubulin. Pathogenic missense variants alter microtubule behavior and interactions with kinesin motors, producing variant-specific errors in cranial axon growth, guidance, maintenance, and—in some alleles—cortical neuronal migration. This explains the continuum from isolated CFEOM3 to multisystem tubulinopathy. (fritzsch2023evolutionanddevelopment pages 16-18, puri2023tubb3andkif21a pages 20-21)

### Suggested ontology annotations

- **GO biological process:** axon guidance (GO:0007411); neuron projection development (GO:0031175); cranial nerve development; microtubule-based movement (GO:0007018); microtubule polymerization/depolymerization; motor-neuron differentiation; neuron migration.
- **GO cellular component:** microtubule (GO:0005874); neuronal growth cone (GO:0030426); axon (GO:0030424); kinesin complex (GO:0005871); cytoplasm and cytoskeleton.
- **Cell Ontology:** motor neuron (CL:0000100); cranial motor neuron where available; skeletal muscle cell/myocyte (CL:0000188); extraocular-muscle fiber as the most specific supported term.

There is no established primary metabolic, immune, inflammatory, apoptotic, or oxidative-stress pathway. The “fibrosis” is downstream of dysinnervation rather than evidence of a systemic fibrosing disorder.

### Molecular profiling and advanced technologies

No validated diagnostic transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic CFEOM signature was found. Current molecular evidence is dominated by pedigree sequencing, structural/biochemical assays, neuroimaging, and engineered animal models. The large recent genomics study demonstrates the value of combined exome/genome and structural-variant analysis but also shows that most previously unsolved pedigrees remain without a definitive molecular diagnosis. (jurgens2025expandingthegenetics pages 8-12, jurgens2025expandingthegenetics pages 38-41)

## 7. Anatomical structures affected

**Primary nervous-system structures:** oculomotor nucleus and nerve (CN III), especially its superior division in KIF21A-CFEOM1; trochlear nucleus/nerve (CN IV), particularly in PHOX2A disease; and variably abducens pathways (CN VI). The midbrain and rostral hindbrain are the critical developmental regions.

**Primary orbital structures:** superior, inferior, medial, and lateral rectus; superior and inferior oblique; and levator palpebrae superioris. In KIF21A-CFEOM1, superior rectus and levator hypoplasia are especially prominent. Human MRI of 14 genetically affected individuals from six families demonstrated muscle hypoplasia and motor-nerve abnormalities. (whitman2021axonalgrowthabnormalities pages 6-8)

**Secondary structures:** eyelids, visual pathways affected by amblyopia, and—depending on genotype—corpus callosum, cerebral white matter, cortex, basal ganglia, additional cranial nerves, and peripheral nerves.

**Suggested UBERON terms:** eye (UBERON:0000970); extraocular muscle (use the current specific UBERON EOM record); oculomotor nerve (UBERON:0001643); trochlear nerve; abducens nerve; midbrain (UBERON:0001891); hindbrain (UBERON:0002028); upper eyelid; superior rectus muscle; levator palpebrae superioris.

Disease is typically bilateral in CFEOM1/2, whereas CFEOM3 may be unilateral, bilateral, or markedly asymmetric. (fritzsch2023evolutionanddevelopment pages 16-18)

## 8. Temporal development

The initiating defect occurs during embryonic ocular motor-neuron development. Clinical signs are present at birth or recognized in early infancy. The dysinnervation is **nonprogressive**, but secondary consequences evolve: amblyopia develops during the sensitive period of visual maturation; abnormal head posture and contractures may become more apparent with growth; and surgical alignment can drift or require revision. There are no defined early/intermediate/end-stage categories, remissions, or relapsing episodes.

The principal intervention window is early childhood: clear the visual axis, correct refractive error, treat amblyopia, and establish the most functional head position possible. The underlying nerve-development defect does not spontaneously recover.

## 9. Inheritance and population

### Inheritance

- **CFEOM1/KIF21A:** autosomal dominant; familial or de novo.
- **CFEOM2/PHOX2A:** autosomal recessive; recurrence risk is 25% for each pregnancy when both parents are carriers.
- **CFEOM3/TUBB3:** autosomal dominant; familial or de novo, with variable expressivity.
- **TUBA1A/TUBB2B-associated phenotypes:** usually dominant/de novo, although individual pedigrees require variant-specific assessment. (fritzsch2023evolutionanddevelopment pages 16-18, fritzsch2023evolutionanddevelopment pages 14-16)

Anticipation is not established. Penetrance is often high for classic KIF21A-CFEOM1 but is variant- and family-dependent; expressivity is particularly variable in CFEOM3. Germline mosaicism should be discussed after an apparently de novo result because recurrence risk is low but not zero.

### Epidemiology

CFEOM is very rare, but no reliable population-based prevalence, incidence, carrier-frequency, sex-ratio, mortality, or geographic-distribution estimate was recovered. Published cohorts are referral- and ancestry-dependent and should not be used as population prevalence samples. The Chinese cohort demonstrates worldwide occurrence and genetic heterogeneity but does not establish higher risk in Chinese ancestry. (jia2022clinicalandgenetic pages 13-14)

No consistent sex bias is expected for autosomal disease. Founder effects may exist in individual PHOX2A families or populations, but no universal founder allele is established.

## 10. Diagnostics

### Clinical assessment

Diagnosis begins with congenital onset, nonprogressive restrictive motility, ptosis, globe position, forced-duction findings, and family history. Examination should include visual acuity appropriate for age, cycloplegic refraction, amblyopia assessment, pupil examination, ocular alignment in multiple gaze positions, head posture, eyelid function, Bell phenomenon, corneal exposure, fundus/optic-nerve examination, and complete neurologic/dysmorphology review.

### Imaging

Obtain thin-section, high-resolution MRI of the brainstem, cranial nerves, and orbits when feasible. MRI can identify absent/hypoplastic or misdirected ocular motor nerves, extraocular-muscle hypoplasia, and syndromic cerebral abnormalities. In one broad Chinese CCDD cohort, all MRI-assessed patients except those with horizontal-gaze-palsy/progressive-scoliosis had cranial-nerve hypoplasia; MRI plus WES was judged diagnostically supportive. (jia2022clinicalandgenetic pages 13-14)

### Genetic-testing algorithm

1. **Phenotype-directed multigene panel** covering at least KIF21A, PHOX2A, TUBB3, TUBA1A, and TUBB2B, with relevant oCCDD differential genes such as CHN1, MAFB, SALL4, HOXA1, ROBO3, ACKR3, and ECEL1.
2. If a classic familial phenotype strongly suggests one gene, targeted sequencing may be efficient—KIF21A for classic CFEOM1 and PHOX2A for classic recessive CFEOM2—but a panel generally better addresses overlap.
3. **Trio WES** for negative or syndromic cases; the Chinese cohort used WES followed by Sanger validation and segregation/de novo analysis. (jia2022clinicalandgenetic pages 13-14)
4. **WGS with CNV/structural-variant analysis** for persistently unsolved cases, especially when syndromic. A large recent study pre-screened 403/467 probands for known oCCDD genes and then applied exome/genome sequencing to unresolved pedigrees. (jurgens2025expandingthegenetics pages 38-41)
5. **Chromosomal microarray** where developmental delay, multiple congenital anomalies, or a chromosomal syndrome is suspected.

Karyotyping/FISH are not first-line unless a specific rearrangement is suspected. Mitochondrial DNA and repeat-expansion testing are not routine CFEOM tests. RNA sequencing may help resolve splice variants but is not an established clinical standard. A VUS must not direct irreversible treatment or predictive testing without additional evidence.

### Differential diagnosis

Important alternatives include Duane retraction syndrome, Möbius syndrome, isolated congenital CN III/IV/VI palsy, congenital myasthenic syndrome, congenital myopathy, mitochondrial external ophthalmoplegia, MYF5-related external ophthalmoplegia with rib/vertebral anomalies, HOXA1/SALL4/ROBO3-related CCDD, orbital fibrosis, thyroid eye disease, congenital ptosis without ophthalmoplegia, and mechanical restrictive strabismus. Congenital stability, characteristic nerve/MRI anatomy, associated anomalies, and molecular testing distinguish these entities.

### Screening

CFEOM is not included in routine newborn biochemical screening. Appropriate strategies are clinical newborn/infant eye examination in known families, cascade testing of relatives after identification of a pathogenic variant, and prenatal or preimplantation genetic testing when the familial variant is known.

## 11. Outcome and prognosis

CFEOM itself is not expected to shorten life in isolated disease; no disease-specific survival or mortality statistics exist. Morbidity is primarily visual and functional. Without timely care, ptosis, strabismus, and anisometropia can produce irreversible amblyopia. Persistent ophthalmoplegia and limited binocular visual fields remain lifelong even after successful alignment surgery.

Prognosis depends on genotype, baseline visual acuity, amblyopia, severity and symmetry of restriction, head posture, Bell phenomenon/corneal protection, and syndromic neurologic involvement. Surgery can improve primary-position alignment, head posture, eyelid position, and appearance, but does not restore normal innervation or full motility. Controlled long-term response rates and validated CFEOM-specific prognostic biomarkers are unavailable.

## 12. Treatment

### Current clinical strategy

1. **Protect vision early:** cycloplegic refraction, glasses, occlusion or atropine penalization for amblyopia when indicated, and management of corneal exposure.
2. **Characterize restriction:** repeated motility measurements, head posture, eyelid function, and forced ductions when surgery is planned.
3. **Strabismus surgery:** individualized recession of tight muscles, often large inferior-rectus recession for marked infraduction; horizontal rectus surgery, transposition procedures, adjustable sutures, or periosteal fixation may be considered by experienced surgeons. Multiple procedures are often necessary.
4. **Ptosis surgery:** levator or frontalis-sling procedures, timed cautiously because poor Bell phenomenon and limited upgaze increase exposure-keratopathy risk.
5. **Neurologic/developmental care:** indicated for TUBB3/TUBA1A/TUBB2B syndromic disease.

**Suggested NCIt intervention mappings:** strabismus surgery; extraocular-muscle recession; extraocular-muscle resection; tendon transposition; ptosis repair; frontalis suspension; amblyopia therapy; corrective-lens therapy. Exact NCIt codes should be validated against the current thesaurus release.

There is no approved CFEOM-specific drug, pharmacogenomic algorithm, gene therapy, cell therapy, ASO, siRNA, immune therapy, or CRISPR treatment. Experimental work showing correction of mutant tubulin–kinesin interaction in a mouse/biochemical system is mechanistic proof of principle, not a clinically available therapy. The broader mechanistic literature shows that altered TUBB3–kinesin interaction can be experimentally rescued, supporting future target discovery. (puri2023tubb3andkif21a pages 20-21)

A recruiting observational study, **NCT03059420**, “Genetic Studies of Strabismus, Congenital Cranial Dysinnervation Disorders (CCDDs), and Their Associated Anomalies,” is designed for genetic/phenotypic discovery rather than therapeutic efficacy: https://clinicaltrials.gov/study/NCT03059420.

## 13. Prevention

Primary lifestyle or vaccine prevention is not applicable to a congenital Mendelian dysinnervation disorder. Reproductive prevention options include genetic counseling, carrier testing for relatives in PHOX2A families, cascade testing in dominant families, prenatal diagnosis, and preimplantation genetic testing for a known familial pathogenic variant.

Secondary prevention consists of early ophthalmologic detection and prevention of amblyopia or corneal exposure. Tertiary prevention includes optimized alignment/head posture, low-vision or educational support where necessary, and surveillance for neurologic complications in syndromic tubulinopathies. Population screening is not justified by current prevalence and intervention evidence.

## 14. Other species and natural disease

No well-validated naturally occurring veterinary disease that is genetically and phenotypically equivalent to human CFEOM was identified. There is no zoonotic transmission or cross-species infectious susceptibility. The relevant genes and ocular motor-development programs are evolutionarily conserved across vertebrates, enabling engineered mouse and zebrafish studies; conservation should not be confused with naturally occurring animal disease.

Suggested taxonomy identifiers for experimental work include **Mus musculus, NCBI Taxon 10090**, and **Danio rerio, NCBI Taxon 7955**.

## 15. Model organisms and experimental systems

### KIF21A mouse models

Knock-in mice carrying the orthologous human CFEOM1 mutation reproduce ptosis/globe retraction and selective superior-division CN III pathology. Axons form proximal bulbs with enlarged growth cones, stall, and degenerate; distal nerves and superior rectus/levator targets become hypoplastic. These models strongly recapitulate developmental dysinnervation but do not reproduce every aspect of human visual behavior or surgical disease. (whitman2021axonalgrowthabnormalities pages 6-8)

### PHOX2A mice

Loss-of-function models fail to specify or maintain oculomotor and trochlear motor-neuron populations, directly supporting the upstream transcription-factor mechanism of CFEOM2. (fritzsch2023evolutionanddevelopment pages 16-18)

### TUBB3 systems

TUBB3 knock-in mice and recombinant tubulin assays model variant-specific microtubule and kinesin defects. In vitro work shows that disease-associated substitutions can impair kinesin motility/ATPase function, while engineered compensatory kinesin changes can restore axonal growth in experimental systems. These are powerful mechanistic models but do not establish safety or feasibility of analogous human treatment. (puri2023tubb3andkif21a pages 20-21)

Zebrafish and other vertebrate systems are useful for rapid analysis of cranial-axon pathfinding and conserved ocular motor circuitry, but the best directly disease-relevant evidence presently comes from mouse knock-in and recombinant microtubule–motor assays.

## Recent developments and expert interpretation

- **August 2023:** Puri, Barry, and Engle synthesized evidence that TUBB3 and KIF21A variants alter microtubule dynamics and microtubule–kinesin interactions. Their abstract states that neuronal migration and axon guidance require “**precise control of microtubule dynamics and microtubule-based cargo transport**,” succinctly capturing the current mechanistic model. DOI: https://doi.org/10.3389/fnins.2023.1226181. (puri2023tubb3andkif21a pages 20-21)
- **March 2024:** a four-generation Chinese family study reported genetic investigation of CFEOM with keratoconus (DOI: https://doi.org/10.1016/j.heliyon.2024.e28036). This is relevant to phenotypic expansion but does not establish keratoconus as a general CFEOM feature.
- **Online 2024 / print July 2025:** the 467-pedigree oCCDD study found pathogenic/likely pathogenic variants in only 9.2% of previously unsolved probands and VUS in 15.0%, emphasizing substantial remaining genetic heterogeneity. It nominated multiple candidate genes, but expert interpretation should remain conservative until replication and functional confirmation. DOI: https://doi.org/10.1016/j.gim.2024.101216. (jurgens2025expandingthegenetics pages 8-12, jurgens2025expandingthegenetics pages 38-41)

## Evidence limitations

The strongest evidence consists of human pedigrees, genotype–phenotype cohorts, MRI/pathology, knock-in mice, and in-vitro microtubule–kinesin assays. Major limitations are referral bias, small subtype-specific cohorts, inconsistent historical classification, lack of population registries, sparse standardized surgical outcomes, and virtually no disease-specific quality-of-life or prospective natural-history data. Candidate-gene findings from unsolved oCCDD cohorts must not be conflated with definitively validated CFEOM genes. No claim of environmental protection, pharmacologic efficacy, or advanced-omics biomarker is currently justified.

References

1. (fritzsch2023evolutionanddevelopment pages 16-18): Bernd Fritzsch. Evolution and development of extra-ocular nerves and muscles in vertebrates. Unknown journal, Jun 2023. URL: https://doi.org/10.20944/preprints202306.0416.v1, doi:10.20944/preprints202306.0416.v1.

2. (whitman2021axonalgrowthabnormalities pages 6-8): Mary C. Whitman. Axonal growth abnormalities underlying ocular cranial nerve disorders. Sep 2021. URL: https://doi.org/10.1146/annurev-vision-093019-114307, doi:10.1146/annurev-vision-093019-114307. This article has 22 citations and is from a peer-reviewed journal.

3. (puri2023tubb3andkif21a pages 20-21): Dharmendra Puri, Brenda J. Barry, and Elizabeth C. Engle. Tubb3 and kif21a in neurodevelopment and disease. Frontiers in Neuroscience, Aug 2023. URL: https://doi.org/10.3389/fnins.2023.1226181, doi:10.3389/fnins.2023.1226181. This article has 43 citations and is from a peer-reviewed journal.

4. (jia2022clinicalandgenetic pages 13-14): Hongyan Jia, Qian Ma, Yi Liang, Dan Wang, Qinglin Chang, Bo Zhao, Zongrui Zhang, Jing Liang, Jing Song, Yidi Wang, Ranran Zhang, Zhanhan Tu, and Yonghong Jiao. Clinical and genetic characteristics of chinese patients with congenital cranial dysinnervation disorders. Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02582-5, doi:10.1186/s13023-022-02582-5. This article has 12 citations and is from a peer-reviewed journal.

5. (jurgens2025expandingthegenetics pages 38-41): Julie A. Jurgens, Brenda J. Barry, Wai-Man Chan, Sarah E. Mackinnon, M. Whitman, Paola M. Matos Ruiz, Brandon M Pratt, E. England, Lynn Pais, G. Lemire, E. Groopman, Carmen Glaze, Kathryn A Russell, M. Singer-Berk, Silvio Alessandro Di Gioia, Arthur S. Lee, Caroline Andrews, Sherin Shaaban, Megan M Wirth, Sarah Bekele, Melissa Toffoloni, Victoria R Bradford, Emma E. Foster, Lindsay Berube, Cristina Rivera-Quiles, Fiona M. Mensching, Alba Sanchis-Juan, Jack M. Fu, Isaac Wong, Xuefang Zhao, M. Wilson, B. Weisburd, M. Lek, Hugo Abarca-Barriga, C. Al-Haddad, Jeffrey Berman, E. Bothun, J. Capasso, O. Chacón-Camacho, Lan-Yun Chang, Stephen P Christiansen, M. Ciccarelli, M. Cordonnier, G. F. Cox, Cynthia J. Curry, L. Dagi, Thomas Lee Dahm, Karen David, B. Davitt, T. de Berardinis, J. Demer, J. Desir, F. D’Esposito, A. Drack, Eric Eggenberger, J. Elder, A. Elliott, K. Epley, H. Feldman, Carlos R. Ferreira, Maree P. Flaherty, A. B. Fulton, C. Gerth-Kahlert, I. Gottlob, Stephen Grill, D. Halliday, F. Hanisch, Eleanor Hay, G. Heidary, C. Holder, Jonathan C. Horton, A. Iannaccone, Sherwin J. Isenberg, S. Johnston, A. Kahana, J. Katowitz, M. Kazlas, Natalie C Kerr, Virginia E. Kimonis, M. Ko, Feray Koç, D. Larsen, G. Lay-Son, D. Ledoux, Alex V Levin, Richard Levy, Christopher J. Lyons, D. Mackey, Adriano Magli, Iason S. Mantagos, Candice Marti, I. Maystadt, Fiona McKenzie, Manoj P Menezes, Claudia N. Mikail, David T. Miller, K. B. Miller, M. Mills, K. Miyana, H. U. Møller, L. Mullineaux, J. Nishimura, A. Noble, P. K. Pandey, Piero Pavone, Johann Penzien, R. Petersen, James A. Phalen, A. Poduri, C. R. Polo, L. Prasov, F. Ramos, Maria Ramos-Cáceres, Richard M. Robb, Béatrice Rossillion, Mustafa Sahin, Harvey S Singer, Lois E. H. Smith, J. A. Sorkin, J. Soul, S. Staffieri, Heather Stalker, S. Stasheff, Sonya Strassberg, Mitchell B. Strominger, D. Taranath, Ioan T. Thomas, Elias I. Traboulsi, M. C. Ugrin, Deborah K. Vanderveen, Andrea L. Vincent, Marlene C. Vogel G, B. Wabbels, A. Wong, C. Woods, Carolyn Wu, Edward Yang, A. Yeung, Terri L. Young, J. Zenteno, Alexandra A. Zubcov-Iwantscheff, Johan Zwaan, Harrison Brand, M. Talkowski, D. MacArthur, A. O’Donnell-Luria, C. Robson, David G. Hunter, and Elizabeth C. Engle. Expanding the genetics and phenotypes of ocular congenital cranial dysinnervation disorders. Genetics in medicine : official journal of the American College of Medical Genetics, 27:101216-101216, Jul 2025. URL: https://doi.org/10.1016/j.gim.2024.101216, doi:10.1016/j.gim.2024.101216. This article has 20 citations.

6. (fritzsch2023evolutionanddevelopment pages 14-16): Bernd Fritzsch. Evolution and development of extra-ocular nerves and muscles in vertebrates. Unknown journal, Jun 2023. URL: https://doi.org/10.20944/preprints202306.0416.v1, doi:10.20944/preprints202306.0416.v1.

7. (jurgens2025expandingthegenetics pages 36-37): Julie A. Jurgens, Brenda J. Barry, Wai-Man Chan, Sarah E. Mackinnon, M. Whitman, Paola M. Matos Ruiz, Brandon M Pratt, E. England, Lynn Pais, G. Lemire, E. Groopman, Carmen Glaze, Kathryn A Russell, M. Singer-Berk, Silvio Alessandro Di Gioia, Arthur S. Lee, Caroline Andrews, Sherin Shaaban, Megan M Wirth, Sarah Bekele, Melissa Toffoloni, Victoria R Bradford, Emma E. Foster, Lindsay Berube, Cristina Rivera-Quiles, Fiona M. Mensching, Alba Sanchis-Juan, Jack M. Fu, Isaac Wong, Xuefang Zhao, M. Wilson, B. Weisburd, M. Lek, Hugo Abarca-Barriga, C. Al-Haddad, Jeffrey Berman, E. Bothun, J. Capasso, O. Chacón-Camacho, Lan-Yun Chang, Stephen P Christiansen, M. Ciccarelli, M. Cordonnier, G. F. Cox, Cynthia J. Curry, L. Dagi, Thomas Lee Dahm, Karen David, B. Davitt, T. de Berardinis, J. Demer, J. Desir, F. D’Esposito, A. Drack, Eric Eggenberger, J. Elder, A. Elliott, K. Epley, H. Feldman, Carlos R. Ferreira, Maree P. Flaherty, A. B. Fulton, C. Gerth-Kahlert, I. Gottlob, Stephen Grill, D. Halliday, F. Hanisch, Eleanor Hay, G. Heidary, C. Holder, Jonathan C. Horton, A. Iannaccone, Sherwin J. Isenberg, S. Johnston, A. Kahana, J. Katowitz, M. Kazlas, Natalie C Kerr, Virginia E. Kimonis, M. Ko, Feray Koç, D. Larsen, G. Lay-Son, D. Ledoux, Alex V Levin, Richard Levy, Christopher J. Lyons, D. Mackey, Adriano Magli, Iason S. Mantagos, Candice Marti, I. Maystadt, Fiona McKenzie, Manoj P Menezes, Claudia N. Mikail, David T. Miller, K. B. Miller, M. Mills, K. Miyana, H. U. Møller, L. Mullineaux, J. Nishimura, A. Noble, P. K. Pandey, Piero Pavone, Johann Penzien, R. Petersen, James A. Phalen, A. Poduri, C. R. Polo, L. Prasov, F. Ramos, Maria Ramos-Cáceres, Richard M. Robb, Béatrice Rossillion, Mustafa Sahin, Harvey S Singer, Lois E. H. Smith, J. A. Sorkin, J. Soul, S. Staffieri, Heather Stalker, S. Stasheff, Sonya Strassberg, Mitchell B. Strominger, D. Taranath, Ioan T. Thomas, Elias I. Traboulsi, M. C. Ugrin, Deborah K. Vanderveen, Andrea L. Vincent, Marlene C. Vogel G, B. Wabbels, A. Wong, C. Woods, Carolyn Wu, Edward Yang, A. Yeung, Terri L. Young, J. Zenteno, Alexandra A. Zubcov-Iwantscheff, Johan Zwaan, Harrison Brand, M. Talkowski, D. MacArthur, A. O’Donnell-Luria, C. Robson, David G. Hunter, and Elizabeth C. Engle. Expanding the genetics and phenotypes of ocular congenital cranial dysinnervation disorders. Genetics in medicine : official journal of the American College of Medical Genetics, 27:101216-101216, Jul 2025. URL: https://doi.org/10.1016/j.gim.2024.101216, doi:10.1016/j.gim.2024.101216. This article has 20 citations.

8. (jurgens2025expandingthegenetics pages 8-12): Julie A. Jurgens, Brenda J. Barry, Wai-Man Chan, Sarah E. Mackinnon, M. Whitman, Paola M. Matos Ruiz, Brandon M Pratt, E. England, Lynn Pais, G. Lemire, E. Groopman, Carmen Glaze, Kathryn A Russell, M. Singer-Berk, Silvio Alessandro Di Gioia, Arthur S. Lee, Caroline Andrews, Sherin Shaaban, Megan M Wirth, Sarah Bekele, Melissa Toffoloni, Victoria R Bradford, Emma E. Foster, Lindsay Berube, Cristina Rivera-Quiles, Fiona M. Mensching, Alba Sanchis-Juan, Jack M. Fu, Isaac Wong, Xuefang Zhao, M. Wilson, B. Weisburd, M. Lek, Hugo Abarca-Barriga, C. Al-Haddad, Jeffrey Berman, E. Bothun, J. Capasso, O. Chacón-Camacho, Lan-Yun Chang, Stephen P Christiansen, M. Ciccarelli, M. Cordonnier, G. F. Cox, Cynthia J. Curry, L. Dagi, Thomas Lee Dahm, Karen David, B. Davitt, T. de Berardinis, J. Demer, J. Desir, F. D’Esposito, A. Drack, Eric Eggenberger, J. Elder, A. Elliott, K. Epley, H. Feldman, Carlos R. Ferreira, Maree P. Flaherty, A. B. Fulton, C. Gerth-Kahlert, I. Gottlob, Stephen Grill, D. Halliday, F. Hanisch, Eleanor Hay, G. Heidary, C. Holder, Jonathan C. Horton, A. Iannaccone, Sherwin J. Isenberg, S. Johnston, A. Kahana, J. Katowitz, M. Kazlas, Natalie C Kerr, Virginia E. Kimonis, M. Ko, Feray Koç, D. Larsen, G. Lay-Son, D. Ledoux, Alex V Levin, Richard Levy, Christopher J. Lyons, D. Mackey, Adriano Magli, Iason S. Mantagos, Candice Marti, I. Maystadt, Fiona McKenzie, Manoj P Menezes, Claudia N. Mikail, David T. Miller, K. B. Miller, M. Mills, K. Miyana, H. U. Møller, L. Mullineaux, J. Nishimura, A. Noble, P. K. Pandey, Piero Pavone, Johann Penzien, R. Petersen, James A. Phalen, A. Poduri, C. R. Polo, L. Prasov, F. Ramos, Maria Ramos-Cáceres, Richard M. Robb, Béatrice Rossillion, Mustafa Sahin, Harvey S Singer, Lois E. H. Smith, J. A. Sorkin, J. Soul, S. Staffieri, Heather Stalker, S. Stasheff, Sonya Strassberg, Mitchell B. Strominger, D. Taranath, Ioan T. Thomas, Elias I. Traboulsi, M. C. Ugrin, Deborah K. Vanderveen, Andrea L. Vincent, Marlene C. Vogel G, B. Wabbels, A. Wong, C. Woods, Carolyn Wu, Edward Yang, A. Yeung, Terri L. Young, J. Zenteno, Alexandra A. Zubcov-Iwantscheff, Johan Zwaan, Harrison Brand, M. Talkowski, D. MacArthur, A. O’Donnell-Luria, C. Robson, David G. Hunter, and Elizabeth C. Engle. Expanding the genetics and phenotypes of ocular congenital cranial dysinnervation disorders. Genetics in medicine : official journal of the American College of Medical Genetics, 27:101216-101216, Jul 2025. URL: https://doi.org/10.1016/j.gim.2024.101216, doi:10.1016/j.gim.2024.101216. This article has 20 citations.

## Artifacts

- [Edison artifact artifact-00](Congenital_Fibrosis_of_the_Extraocular_Muscles-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.