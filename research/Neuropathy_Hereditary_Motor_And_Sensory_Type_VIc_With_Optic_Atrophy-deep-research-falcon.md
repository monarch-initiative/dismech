---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T16:04:52.589205'
end_time: '2026-08-27T16:15:33.865456'
duration_seconds: 641.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neuropathy Hereditary Motor And Sensory Type VIc With Optic Atrophy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 4
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Neuropathy_Hereditary_Motor_And_Sensory_Type_VIc_With_Optic_Atrophy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neuropathy Hereditary Motor And Sensory Type VIc With Optic Atrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neuropathy Hereditary Motor And Sensory Type VIc With Optic Atrophy** covering all of the
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
- **Disease Name:** Neuropathy Hereditary Motor And Sensory Type VIc With Optic Atrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neuropathy Hereditary Motor And Sensory Type VIc With Optic Atrophy** covering all of the
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


# Comprehensive disease-characteristics report

## Executive summary

**Neuropathy, hereditary motor and sensory, type VIc, with optic atrophy (HMSN6C/CMT6C)** is an exceptionally rare, autosomal-recessive, childhood-onset axonal neuropathy caused by biallelic loss-of-function variants in **PDXK**, encoding cytosolic pyridoxal kinase. Reduced PDXK activity lowers pyridoxal-5′-phosphate (PLP), the active coenzyme form of vitamin B6, producing progressive length-dependent sensorimotor axonopathy followed by bilateral optic atrophy. The defining 2019 study comprised only five affected people from two families; consequently, most frequency estimates below describe that ascertainment cohort rather than the wider disease population. Oral PLP is a plausible disease-modifying treatment, but evidence remains limited to an uncontrolled two-patient observation. (chelban2019pdxkmutationscause pages 1-2)

| domain | best-supported finding | evidence type/sample | knowledge-base annotation |
|---|---|---|---|
| Disease identity | Hereditary motor and sensory neuropathy type VIc with optic atrophy is a rare Mendelian neuropathy mapped to MONDO:0032792 and OMIM 618511 (OpenTargets Search: Neuropathy hereditary motor and sensory type VIc with optic atrophy, chelban2019pdxkmutationscause pages 1-2) | Aggregated disease mapping plus primary human case series | MONDO:0032792; OMIM:618511; category: Mendelian disease |
| Causal gene | Disease is caused by biallelic pathogenic variants in **PDXK** (pyridoxal kinase) (OpenTargets Search: Neuropathy hereditary motor and sensory type VIc with optic atrophy, chelban2019pdxkmutationscause pages 1-2) | Human genetics; 5 affected individuals from 2 unrelated families | Gene: PDXK; mechanism class: inherited enzyme deficiency |
| Inheritance | Autosomal recessive inheritance with segregation in both families (chelban2019pdxkmutationscause pages 6-7, chelban2019pdxkmutationscause pages 1-2) | Family-based segregation | Inheritance: autosomal recessive |
| Original human evidence base | Foundational report described **5 original patients from 2 families** (Cypriot family with 3 affected siblings; Scottish/Italian family with 2 affected sisters) (chelban2019pdxkmutationscause pages 4-6, chelban2019pdxkmutationscause pages 1-2) | Primary human clinical study | Evidence cohort size: n=5, families=2 |
| Core neuropathy phenotype | Early childhood-onset, progressive, length-dependent **sensorimotor axonal polyneuropathy** with distal wasting/weakness, areflexia, pes cavus, and marked sensory loss (chelban2019pdxkmutationscause pages 4-6, chelban2019pdxkmutationscause pages 7-9) | Clinical phenotyping and NCS/EMG | HPO candidates: peripheral axonal neuropathy; distal muscle weakness; areflexia; pes cavus; sensory impairment |
| Ophthalmic phenotype | **Bilateral optic atrophy/optic disc pallor** with visual and color vision loss, typically later than neuropathy and in adulthood in the original family 1 (chelban2019pdxkmutationscause pages 6-7, chelban2019pdxkmutationscause pages 7-9) | Fundoscopy, VEPs, visual exam | HPO candidates: optic atrophy; decreased visual acuity; dyschromatopsia |
| Onset/progression | Onset ages in original cases were 2, 5, 7, 7, and 9 years; upper-limb weakness later; optic atrophy at 29-31 years in family 2 and 40-50 years in family 1 (chelban2019pdxkmutationscause pages 6-7, chelban2019pdxkmutationscause pages 7-9) | Patient-level natural history | Temporal profile: childhood onset, chronic progressive, lifelong |
| Electrophysiology/pathology | NCS showed severe sensorimotor axonal neuropathy; early disease may show absent sensory responses with relatively preserved motor responses; EMG showed chronic denervation; nerve biopsy showed longstanding axonopathy without demyelination (chelban2019pdxkmutationscause pages 6-7, chelban2019pdxkmutationscause pages 13-14, chelban2019pdxkmutationscause pages 7-9) | NCS/EMG and sural nerve biopsy | Pathology: axonopathy; not primary demyelinating neuropathy |
| Key variants | Foundational variants: **c.682G>A p.Ala228Thr** and **c.659G>A p.Arg220Gln**; later review also notes **c.225T>A p.Asn75Lys** in another family/cases (chelban2019pdxkmutationscause pages 7-9, bunik2023thetherapeuticpotential pages 4-5) | Primary human genetics plus later review synthesis | Variant examples for curation: missense, germline, biallelic |
| Molecular defect | Mutations reduce ATP-related catalytic function of PDXK: altered conformation around the ATP-binding pocket, no ATPγS binding for p.Ala228Thr under tested conditions, and reduced catalytic efficiency (chelban2019pdxkmutationscause pages 7-9, chelban2019pdxkmutationscause pages 9-11) | Recombinant protein biophysics/enzymology | Functional consequence: loss of function / reduced enzyme activity |
| Biochemical signature | Affected individuals had **low plasma PLP** and **low erythrocyte/dried-blood-spot PDXK activity** compared with controls (chelban2019pdxkmutationscause pages 14-15, chelban2019pdxkmutationscause pages 9-11) | Patient biochemistry | Biomarkers: low pyridoxal-5'-phosphate (PLP); reduced PDXK activity |
| Treatment evidence | Two long-surviving siblings received **oral PLP 50 mg/day**; plasma PLP rose and remained stable through **24 months**, with improvements in motor scores, pain, fatigue, walking, and lower NFL, while sensory exam and vision were unchanged (chelban2019pdxkmutationscause pages 14-15, chelban2019pdxkmutationscause pages 1-2) | Uncontrolled therapeutic observation; n=2 | Intervention: pyridoxal 5'-phosphate supplementation; response: biochemical correction with partial clinical benefit |
| Expert/recent interpretation | 2023-2024 reviews highlight PDXK neuropathy as a **vitamin B6-responsive complex inherited neuropathy** and recommend considering PDXK testing in early-onset autosomal recessive polyneuropathy with optic atrophy (bunik2023thetherapeuticpotential pages 4-5, rossor2024theevolvingspectrum pages 1-2) | Recent expert reviews | Clinical application: prioritize molecular diagnosis because a treatable subtype exists |
| Major evidence gaps | No robust prevalence/incidence estimates, penetrance data, founder-frequency estimates, standardized diagnostic criteria, randomized treatment trials, or disease-specific animal knock-in natural history models were identified; treatment data remain limited to small uncontrolled reports (rossor2024theevolvingspectrum pages 1-2, chelban2019pdxkmutationscause pages 14-15) | Evidence synthesis across primary and review sources | Evidence gap flag: very rare disease with sparse literature |


*Table: This table condenses the best-supported disease-characteristics evidence for PDXK-associated hereditary motor and sensory neuropathy type VIc with optic atrophy. It highlights identifiers, core phenotype, causal variants, biochemical mechanism, treatment signal, and the main evidence gaps relevant for knowledge-base curation.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** neuropathy, hereditary motor and sensory, type VIc, with optic atrophy.
* **Synonyms:** HMSN6C; CMT6C; Charcot–Marie–Tooth disease type 6C; PDXK-related neuropathy; hereditary polyneuropathy with optic atrophy due to impaired vitamin-B6 metabolism.
* **MONDO:** **MONDO:0032792**.
* **OMIM phenotype:** **618511**.
* **Causal gene:** **PDXK**, pyridoxal kinase; Ensembl **ENSG00000160209**.
* **Inheritance/category:** Mendelian, autosomal recessive.
* **Orphanet, MeSH, ICD-10 and ICD-11:** no retrieved evidence established disease-specific entries. Broader hereditary motor and sensory neuropathy/CMT or hereditary optic-atrophy codes may be used clinically, but these should not be represented as exact HMSN6C mappings without terminology-service verification. Open Targets currently links MONDO:0032792 specifically to PDXK and cites PMIDs 31187503 and 32522499. (OpenTargets Search: Neuropathy hereditary motor and sensory type VIc with optic atrophy)

The evidence is predominantly **aggregated disease-level information derived from a very small number of published individual patients**, not an EHR cohort or population registry. The foundational article was received October 1, 2018, accepted June 7, 2019, and published in *Annals of Neurology* in July 2019: Chelban et al., PMID **31187503**, DOI/URL: https://doi.org/10.1002/ana.25524. (chelban2019pdxkmutationscause pages 1-2)

**Exact abstract quotation:** “We identified biallelic mutations in PDXK in 5 individuals from 2 unrelated families with primary axonal polyneuropathy and optic atrophy.” (chelban2019pdxkmutationscause pages 1-2)

## 2. Etiology, risk, protection, and environment

The primary cause is **germline biallelic PDXK dysfunction**. The original families carried homozygous missense variants affecting evolutionarily conserved residues near the ATP-binding site. Segregation supported recessive inheritance. No infectious, autoimmune, toxic, occupational, lifestyle, sex-specific, or environmental cause has been demonstrated. (chelban2019pdxkmutationscause pages 7-9)

Family history and parental carrier status are the principal recognized risk factors. For two carrier parents, standard autosomal-recessive counseling gives a 25% affected, 50% carrier, and 25% non-carrier probability for each pregnancy. Penetrance cannot be estimated rigorously, although all reported biallelic individuals in the founding pedigrees were affected. No protective human alleles, modifier genes, anticipation, or germline-mosaicism cases have been reported.

A clinically important mechanistic interaction is possible with **vitamin-B6 availability or PDXK-inhibiting exposures**, but disease-specific gene–environment data do not exist. Isoniazid, levodopa, gentamicin and D-penicillamine can reduce functional PLP; methylxanthines can inhibit B6-metabolism enzymes; and several antiepileptic drugs enhance PLP catabolism. These are mechanistic analogies, not proven HMSN6C modifiers. (chelban2019pdxkmutationscause pages 13-14)

Excess pyridoxine itself can cause sensory neuropathy and may inhibit PDXK; therefore, unsupervised high-dose pyridoxine should not be equated with targeted PLP replacement. This distinction is important because the reported treatment used PLP, not conventional pyridoxine. (chelban2019pdxkmutationscause pages 11-13)

## 3. Phenotypes

### Human phenotype spectrum

In the original cohort, all five patients had childhood-onset, progressive, length-dependent sensorimotor axonal neuropathy: **5/5 (100%)**. Recorded onset ages were 2, 5, 7, 7 and 9 years (median 7; range 2–9). Initial manifestations were lower-limb weakness/wasting, impaired balance, difficulty running, and distal sensory dysfunction. Upper-limb weakness appeared by ages 12–17 in the older family and during the twenties in the younger family. (chelban2019pdxkmutationscause pages 6-7, chelban2019pdxkmutationscause pages 4-6)

Core findings included distal lower-limb and hand-muscle wasting, weakness of ankle dorsiflexion/plantar flexion and finger extensors, areflexia, loss of pain and vibration sensation, impaired proprioception, positive Romberg sign, pes cavus, hammer toes, and hand clawing. Cognition and coordination were reported as normal; seizures were absent. Suggested HPO annotations include **Peripheral axonal neuropathy**, **Sensorimotor neuropathy**, **Distal muscle weakness**, **Muscle atrophy**, **Areflexia (HP:0001284)**, **Impaired vibration sensation**, **Impaired proprioception**, **Positive Romberg sign**, **Pes cavus (HP:0001761)**, **Hammer toe**, and **Claw hand**. (chelban2019pdxkmutationscause pages 6-7, chelban2019pdxkmutationscause pages 7-9)

Bilateral optic-disc pallor/atrophy was documented in all clinically examined affected individuals in the founding report. Recorded onset/recognition was ages 29 and 31 in the younger family and 40, 47 and 50 in the older family. Visual acuity and color discrimination could become severely impaired; visual fields were reportedly preserved in assessed patients. VEP amplitudes declined substantially over 20 years in an older patient, consistent with progressive optic-axonal loss. Suggested HPO terms are **Optic atrophy (HP:0000648)**, **Decreased visual acuity**, **Dyschromatopsia**, and **Abnormal visual evoked potentials**. (chelban2019pdxkmutationscause pages 6-7, chelban2019pdxkmutationscause pages 7-9)

Nerve-conduction studies showed sensorimotor, predominantly axonal neuropathy in all assessed patients. An early clue was absent sensory responses despite relatively preserved motor responses. EMG showed chronic length-dependent denervation without myopathy. Sural-nerve biopsy in one patient demonstrated severe depletion of small and large myelinated axons, regenerative clusters, and no demyelinating or onion-bulb process. (chelban2019pdxkmutationscause pages 6-7, chelban2019pdxkmutationscause pages 13-14, chelban2019pdxkmutationscause pages 7-9)

### Functional and quality-of-life effects

Advanced untreated disease caused impaired transfers, high-stepping gait, dependence on frames or two-person assistance, wheelchair use, difficult neuropathic pain, and severe visual disability. No EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life dataset was identified. CMTNS2, Neuropathy Impairment Scale, MRC sum score, ambulation, pain, and fatigue were used instead. (chelban2019pdxkmutationscause pages 11-13, chelban2019pdxkmutationscause pages 4-6)

All phenotype percentages must be interpreted cautiously: the sample consisted of related patients selected for neuropathy plus optic atrophy, making ascertainment bias substantial.

## 4. Genetic and molecular information

### Gene and variants

**PDXK** encodes cytosolic pyridoxal kinase, which phosphorylates pyridoxal, pyridoxine and pyridoxamine vitamers and is essential for maintaining intracellular PLP. PLP supports more than 70 human enzymes involved in amino-acid, neurotransmitter and intermediary metabolism. (chelban2019pdxkmutationscause pages 7-9)

Reported variants include:

1. **NM_003681:c.682G>A, p.(Ala228Thr)**—homozygous in affected members of the Cypriot family and heterozygous in unaffected relatives. It was absent from 150 Cypriot controls and absent homozygously from gnomAD; 7/250,586 alleles were heterozygous, allele frequency approximately **2.793×10⁻⁵** in the database version used in 2019. (chelban2019pdxkmutationscause pages 7-9)
2. **c.659G>A, p.(Arg220Gln)**—homozygous in two affected Scottish/Italian sisters and heterozygous in each parent. It was absent homozygously from gnomAD and present in 5/250,146 European alleles, approximately **1.999×10⁻⁵**; reported CADD score 24. (chelban2019pdxkmutationscause pages 7-9)
3. **c.225T>A, p.(Asn75Lys)**—reported subsequently in two children from another family. A 2023 review describes reduced dimer stability, increased degradation, and very low PDXK activity and PLP. The associated primary report is Keller et al., *Neuromuscular Disorders* 2020;30:583–589, PMID **32522499**. (bunik2023thetherapeuticpotential pages 13-14, bunik2023thetherapeuticpotential pages 4-5)

These are germline missense variants. The functional evidence supports **partial loss of function/hypomorphic enzyme deficiency**, not gain of function or dominant-negative disease. Current ClinVar classifications and present-day gnomAD frequencies should be rechecked directly before clinical reporting because classifications and population datasets evolve.

No established modifier gene, protective allele, epigenetic signature, recurrent copy-number variant, aneuploidy, translocation, inversion, or somatic contribution has been reported.

## 5. Environmental information

No environmental factor is known to cause HMSN6C in the absence of biallelic PDXK variants. Diet, smoking, alcohol, exercise, pollution, radiation, occupational exposure and infectious agents have not been evaluated in disease cohorts. Drug- or nutrition-induced PLP depletion could theoretically worsen biochemical insufficiency, but this remains untested. Conversely, adequate nutrition cannot compensate reliably for defective intracellular PL phosphorylation; the available therapeutic observation used pharmacological PLP replacement. (chelban2019pdxkmutationscause pages 11-13, chelban2019pdxkmutationscause pages 13-14)

## 6. Mechanism and pathophysiology

### Causal chain

The best-supported chain is:

**biallelic PDXK missense variant → altered ATP-binding pocket or dimer stability → reduced pyridoxal-kinase catalytic activity → reduced intracellular and circulating PLP → impaired PLP-dependent amino-acid/neurotransmitter metabolism → selective vulnerability of long peripheral sensory and motor axons and retinal ganglion-cell axons → chronic axonal degeneration → distal weakness, sensory ataxia, areflexia and optic atrophy.** (chelban2019pdxkmutationscause pages 7-9, chelban2019pdxkmutationscause pages 9-11)

For p.Ala228Thr, circular dichroism showed altered secondary/tertiary conformation, while isothermal titration calorimetry detected no ATPγS association under the tested conditions. Recombinant enzyme studies showed PL Km 31.9 versus 14.5 μmol/L for wild type and markedly impaired MgATP kinetics: k0.5 174.4 versus 53.4 μmol/L and Vmax 6.3 versus 16.8 pmol/h. Patient dried-blood-spot PDXK activities were 0.5–1.19 pmol/spot/hour versus a control range of 2.6–14.7, and plasma PLP values cited for representative variants were 7.8 and 9 nmol/L versus 25–75 nmol/L. (chelban2019pdxkmutationscause pages 9-11)

PDXK expression is high in human tibial nerve and present in peripheral sensory neurons. In nine of eleven analyzed brain regions it coexpressed with neuronal/synaptic genes, whereas the tibial-nerve module was enriched for oxidation–reduction genes. Rat B6 deficiency preserves brain PDXK more effectively than peripheral-tissue activity, providing a plausible explanation for prominent peripheral disease without epilepsy, although this remains inferential for humans. (chelban2019pdxkmutationscause pages 13-14, chelban2019pdxkmutationscause pages 9-11)

**Upstream:** PDXK structural/catalytic dysfunction and PLP deficiency. **Downstream:** deficient PLP-enzyme activity, altered neuronal metabolism, axonal injury and neurofilament release. Oxidative-redox and mitochondrial involvement is suggested by coexpression and phenotypic similarity to other optic-atrophy/axonopathy disorders, but direct mitochondrial failure has not been established in HMSN6C. Immune-mediated inflammation, fibrosis, ischemia, necrosis, or a disease-specific methylation mechanism is not supported.

Suggested ontology annotations include **pyridoxal kinase activity (GO:0008478)**, vitamin-B6 metabolic process, pyridoxal-phosphate biosynthetic process, amino-acid metabolic process, neurotransmitter metabolic process, axon maintenance, axon degeneration, cytosol (**GO:0005829**), neuron (**CL:0000540**), peripheral sensory neuron, motor neuron, and retinal ganglion cell (**CL:0000740**). Cell-type involvement is inferred from phenotype/expression rather than histological counting.

No disease-specific single-cell patient dataset, spatial transcriptomics, patient proteome, metabolome beyond B6 vitamers, lipidome, multi-omics integration, CRISPR screen, organoid, or iPSC-neuron model was identified. GTEx bulk expression and public mouse single-cell RNA-seq were used for contextual localization, not disease-state profiling. (chelban2019pdxkmutationscause pages 7-9, chelban2019pdxkmutationscause pages 9-11)

## 7. Anatomical structures affected

The primary system is the **peripheral nervous system**, especially long sensory and motor axons of the lower and subsequently upper limbs. Secondary denervation affects distal skeletal muscle. The visual system is involved bilaterally at the optic discs/optic nerves, most plausibly through retinal-ganglion-cell axons. Brain MRI and optic-nerve/chiasm CT were normal in evaluated older patients, arguing against a gross central structural lesion. (chelban2019pdxkmutationscause pages 6-7, chelban2019pdxkmutationscause pages 7-9)

Suggested UBERON annotations are peripheral nerve, tibial nerve, sural nerve, spinal nerve, skeletal muscle, retina, optic nerve and optic disc. Subcellular annotations include cytosol, PDXK homodimer/active site, axon and neuronal cytoskeleton. The optic phenotype is bilateral; limb findings were described as symmetrical and length dependent.

## 8. Temporal development

Onset is insidious during early childhood, not congenital or acute. In the original cohort, lower-limb dysfunction began at 2–9 years, upper-limb involvement emerged later, and optic atrophy became evident from the late twenties through the fifth decade. Disease is chronic, lifelong and progressively length dependent. (chelban2019pdxkmutationscause pages 6-7, chelban2019pdxkmutationscause pages 4-6)

A practical staging model, not yet formally validated, is:

1. **Early:** childhood imbalance, running difficulty, distal lower-limb weakness, absent sensory responses.
2. **Intermediate:** pes cavus, areflexia, sensory ataxia, upper-limb weakness and optic-disc pallor.
3. **Advanced untreated:** severe distal axonal loss, neuropathic pain, visual loss, assistive-device dependence and wheelchair use.

No spontaneous remission, episodic course, relapsing-remitting pattern, or acute crises have been reported. Earlier PLP initiation is biologically favored because longstanding axonal and optic-nerve loss may be irreversible; however, the optimal treatment window is unknown. (chelban2019pdxkmutationscause pages 14-15, chelban2019pdxkmutationscause pages 13-14)

## 9. Inheritance and population

Inheritance is autosomal recessive. The founding cohort included three affected siblings of Cypriot origin and two affected sisters with Scottish paternal and Italian maternal ancestry. Both sexes can be affected; the five original cases comprised one male and four females, which is far too small to infer a sex ratio. (chelban2019pdxkmutationscause pages 6-7, chelban2019pdxkmutationscause pages 4-6)

Disease-specific prevalence, incidence, carrier frequency, geographic distribution, penetrance, age distribution and mortality rates are unknown. The background estimate of CMT overall—approximately 1 in 2,500—must not be assigned to HMSN6C. The primary paper noted that only approximately 25% of autosomal-recessive CMT cases then had an identified cause, underscoring possible underdiagnosis rather than establishing HMSN6C prevalence. (chelban2019pdxkmutationscause pages 2-3, chelban2019pdxkmutationscause pages 1-2)

The homozygous regions in both families suggest autozygosity, but the retrieved text does not establish parental consanguinity. No founder effect or anticipation has been proven. Heterozygous relatives were clinically unaffected and one carrier had PDXK activity within the normal range. (chelban2019pdxkmutationscause pages 11-13, chelban2019pdxkmutationscause pages 7-9)

## 10. Diagnostics

### Recommended approach

Suspect PDXK-related HMSN6C in a patient with childhood-onset recessive-appearing, length-dependent axonal sensorimotor neuropathy—especially early absent sensory responses—plus optic-disc pallor, dyschromatopsia or visual loss. The 2024 complex-neuropathy review lists PDXK under axonal sensory/motor neuropathy with optic atrophy and emphasizes that more than 250 genes can underlie complex neuropathies, many represented by only a handful of families. (rossor2024theevolvingspectrum pages 1-2, rossor2024theevolvingspectrum pages 9-10)

Recommended evaluation includes:

* detailed pedigree, neurological examination and standardized CMTNS2/NIS/MRC scoring;
* nerve-conduction studies and EMG;
* ophthalmology/neuro-ophthalmology examination, acuity, color plates, fundoscopy, visual fields, OCT where available, and VEPs;
* fasting or consistently timed plasma PLP/B6-vitamer profile, recognizing that supplementation can confound results;
* PDXK activity in erythrocytes/dried blood spots where a validated specialist assay exists;
* plasma neurofilament light as a research/monitoring biomarker, not a disease-specific diagnostic test;
* molecular confirmation by a comprehensive inherited-neuropathy/optic-atrophy panel containing **PDXK**, or WES/WGS with deletion/duplication and segregation analysis. (chelban2019pdxkmutationscause pages 11-13, chelban2019pdxkmutationscause pages 7-9)

WGS plus homozygosity mapping identified the variant in family 1; WES identified the variant in family 2. Thus, exome/genome sequencing has demonstrated utility. Single-gene testing is suitable for a highly characteristic biochemical phenotype or familial cascade testing. CMA, karyotype, FISH, mitochondrial-DNA analysis and repeat-expansion tests are not first-line tests for confirmed PDXK disease but may be appropriate when the broader differential warrants them. RNA sequencing may resolve suspected splice variants; no established proteomic, metabolomic, epigenomic or liquid-biopsy diagnostic exists. (chelban2019pdxkmutationscause pages 2-3, chelban2019pdxkmutationscause pages 7-9)

### Differential diagnosis

Important alternatives include SLC25A46-related HMSN6B, OPA1 “DOA+,” MFN2-related CMT2A, SLC52A2 riboflavin-transporter deficiency, mitochondrial Leber optic neuropathy, Costeff syndrome/OPA3, KLC2-related SPOAN, SPG7 and other complex inherited neuropathies. SLC25A46 commonly adds spasticity/cerebellar ataxia; SLC52A2 often includes bulbar weakness, sensory ataxia and hearing loss; mitochondrial LHON follows maternal inheritance. (rossor2024theevolvingspectrum pages 9-10)

There are no internationally validated HMSN6C-specific clinical criteria, newborn-screening program, or population screening recommendation. Cascade testing of relatives is appropriate after a familial variant is established.

## 11. Outcome and prognosis

Untreated progression in the older family suggested eventual wheelchair dependence and blindness. Nevertheless, survival data are inadequate: one patient died at 71 from leukemia, an unrelated cause, while affected siblings were alive into their seventies/eighties. No five- or ten-year survival rate, disease-specific mortality, or life-expectancy estimate exists. (chelban2019pdxkmutationscause pages 6-7, chelban2019pdxkmutationscause pages 4-6, chelban2019pdxkmutationscause pages 1-2)

Major morbidity consists of irreversible axonal sensory loss, distal weakness/atrophy, falls, deformity, neuropathic pain, loss of independent mobility and bilateral visual disability. The likely prognostic determinants are age at treatment, baseline axonal reserve, duration of neuropathy, and degree of optic-nerve loss, but none has been validated. Plasma neurofilament light tracked axonal injury and fell with biochemical correction in two patients, making it a candidate response biomarker rather than a validated prognostic marker. (chelban2019pdxkmutationscause pages 11-13)

## 12. Treatment and current applications

### Targeted PLP replacement

The only reported disease-directed intervention is **oral pyridoxal-5′-phosphate**, 50 mg/day, given to two older siblings. Plasma PLP increased within two weeks and remained stable at 1, 3, 12, 18 and 24 months without reported adverse effects. Improvement appeared after approximately three months without additional physiotherapy. At 18 months, MRC sums improved by 8 and 6 points; NIS improved by 5 and 4; CMTNS2 improved by 4 and 2. At 24 months both walked unaided with a high-stepping gait, pain had subsided, and plasma NFL was 2.5-fold below pretreatment. Sensory examination and vision did not improve, while distal electrophysiological responses remained stable and proximal EMG recruitment improved. (chelban2019pdxkmutationscause pages 11-13)

**Exact abstract quotation:** “We rescued the clinical and biochemical profile with PLP supplementation in 1 family, improvement in power, pain, and fatigue contributing to patients regaining their ability to walk independently during the first year of PLP normalization.” (chelban2019pdxkmutationscause pages 1-2)

This is compelling precision-medicine evidence but remains **very low certainty clinically**: n=2, open label, no placebo control, no masking, and potentially placebo-sensitive pain/fatigue outcomes. The authors themselves noted severe pre-existing axonal loss, limited proximal electrophysiology and inability to conduct a randomized study in such a rare disease. Prompt treatment with specialist monitoring is rational after molecular/biochemical confirmation, but dosage should not be generalized without metabolic-neurology supervision. (chelban2019pdxkmutationscause pages 14-15)

The 2023 review, published June 22, 2023, concludes that identifying vitamin-responsive molecular subtypes may enable tailored B1/B3/B6 therapy and specifically argues for PDXK screening and prompt PLP supplementation in early-onset recessive polyneuropathy. DOI/URL: https://doi.org/10.3390/biology12070897. (bunik2023thetherapeuticpotential pages 4-5, bunik2023thetherapeuticpotential pages 1-2)

### Supportive management

Supportive care should follow CMT practice: physical and occupational therapy; stretching and strengthening without overwork; ankle–foot orthoses, canes/walkers and wheelchairs as needed; fall prevention; podiatry and orthopedic management of cavovarus/contractures; neuropathic-pain treatment; low-vision rehabilitation; and educational/occupational accommodations. These measures are extrapolated from CMT care rather than tested specifically in HMSN6C.

No disease-specific gene therapy, CRISPR therapy, RNA therapy, cell therapy, surgery, immunotherapy, pharmacogenomic guideline or combination regimen has been established. Searches found no relevant registered PDXK interventional trial. Suggested NCIT intervention labels include **Dietary Supplementation**, **Vitamin Therapy**, **Physical Therapy**, **Occupational Therapy**, **Orthotic Device**, **Pain Management**, and **Genetic Counseling**; exact NCIT codes should be terminology-validated before ingestion.

## 13. Prevention

Because this is a recessive genetic disorder, primary prevention through lifestyle change, vaccination or infection control is not applicable. Reproductive prevention options after familial variant identification include carrier testing, partner testing, prenatal diagnosis and preimplantation genetic testing. Genetic counseling should discuss recurrence risk, limitations of phenotype prediction and the possibility of early treatment.

Secondary prevention consists of cascade testing and early clinical/biochemical surveillance of biallelic relatives before irreversible axonal or optic-nerve loss. Tertiary prevention includes PLP treatment under specialist monitoring, rehabilitation, orthoses, fall prevention, foot care and serial ophthalmic assessment. Avoidance of unnecessary high-dose pyridoxine and consideration of medications that deplete/inactivate PLP are prudent, although no HMSN6C-specific avoidance study exists. (chelban2019pdxkmutationscause pages 11-13, chelban2019pdxkmutationscause pages 13-14)

There is no newborn-screening program, vaccine, public-health control measure or established prophylactic drug for carriers.

## 14. Other species and natural disease

PDXK and vitamin-B6 metabolism are evolutionarily conserved. The disease-associated Arg220 and Ala228 residues are conserved across eutherian species. No naturally occurring PDXK-HMSN6C analogue, affected animal breed, VBO term or zoonotic transmission was identified. This is not an infectious disease and has no zoonotic potential. (chelban2019pdxkmutationscause pages 7-9, chelban2019pdxkmutationscause pages 9-11)

Species used experimentally include mouse (*Mus musculus*, NCBI Taxon 10090), rat (*Rattus norvegicus*, 10116), fruit fly (*Drosophila melanogaster*, 7227), and nematode (*Caenorhabditis elegans*, 6239). Ortholog-specific NCBI Gene identifiers should be checked directly before database loading.

## 15. Model organisms

Available models are mechanistic rather than faithful patient-variant models:

* **Mouse Pdxk knockout:** preweaning lethality, limiting study of chronic human neuropathy.
* **Dietary PLP-deficient mouse:** abnormal walking and axonal peripheral neuropathy with preserved myelin; symptoms reversed with PLP.
* **B6-deficient rat:** peripheral-tissue PDXK activity falls faster than brain activity and reverses with PLP.
* **C. elegans PDXK knockout:** sensory–motor integration defects rescued by a wild-type transgene.
* **Drosophila PDXK knockdown:** impaired climbing, eye/ommatidial abnormalities and reduced longevity, rescued by wild-type expression.
* **Pharmacological PLP-depletion models:** reproduce axonal neuropathy but have off-target and exposure-specific effects. (chelban2019pdxkmutationscause pages 13-14)

These models support causality, tissue selectivity and reversibility of B6-dependent dysfunction, but none reproduces the exact human p.Ala228Thr, p.Arg220Gln or p.Asn75Lys genotype together with decades-long neuropathy and adult optic atrophy. A knock-in mouse or patient-derived iPSC sensory-neuron/retinal-ganglion-cell system would be valuable for defining treatment timing, intracellular PLP flux and reversibility.

## Evidence appraisal and recent-development perspective

The 2019 primary study provides unusually strong mechanistic triangulation for a rare disease—segregation, rarity, protein structure, enzyme kinetics, patient biochemistry, pathology and treatment response—but only five initial patients and two treated subjects. The 2020 report expanded the allelic spectrum, while 2023 and 2024 authoritative reviews positioned PDXK neuropathy as a clinically actionable, vitamin-responsive complex inherited neuropathy. The 2024 review was published in July 2024, DOI/URL: https://doi.org/10.1097/WCO.0000000000001307. (rossor2024theevolvingspectrum pages 1-2, bunik2023thetherapeuticpotential pages 13-14, bunik2023thetherapeuticpotential pages 4-5)

Accordingly, the most defensible current expert interpretation is: **test PDXK early in recessive childhood axonal neuropathy with optic atrophy, measure PLP before supplementation, confirm segregation and biochemical dysfunction where possible, and consider prompt specialist-supervised PLP replacement—while documenting outcomes because efficacy and long-term safety remain based on uncontrolled ultra-rare-disease evidence.**

References

1. (chelban2019pdxkmutationscause pages 1-2): V. Chelban, M. Wilson, J. Warman Chardon, J. Vandrovcova, M. N. Zanetti, E. Zamba-Papanicolaou, S. Efthymiou, S. Pope, M. Conte, Giancarlo Abis, Yo-Tsen Liu, Eloise Tribollet, Nourelhoda A. Haridy, J. Botía, M. Ryten, Paschalis Nicolaou, A. Minaidou, K. Christodoulou, K. Kernohan, Alison J Eaton, M. Osmond, Yoko A. Ito, P. Bourque, J. Jepson, O. Bello, F. Bremner, C. Cordivari, M. Reilly, M. Foiani, A. Heslegrave, H. Zetterberg, S. Heales, N. Wood, James E. Rothman, K. Boycott, P. Mills, P. Clayton, H. Houlden, Yamna Mohamed El Mhammed Stanislav Blagovesta Lionel Wol Kriouile Khorassani Aguennouz Groppa Marinova Kara, Y. Kriouile, M. Khorassani, M. Aguennouz, S. Groppa, Blagovesta Marinova Karashova, L. Van Maldergem, W. Nachbauer, S. Boesch, L. Arning, D. Timmann, B. Cormand, B. Pérez-Dueñas, G. Di Rosa, J. Goraya, T. Sultan, J. Mine, D. Avdjieva, H. Kathom, R. Tincheva, S. Banu, M. Pineda-Marfa, P. Veggiotti, Michel D. Ferrari, A. M. van den Maagdenberg, A. Verrotti, G. Marseglia, S. Savasta, M. García-Silva, A. M. Ruiz, Barbara H. Garavaglia, E. Borgione, S. Portaro, B. M. Sánchez, Richard S. Boles, S. Papacostas, M. Vikelis, James E. Rothman, P. Giunti, H. Houlden, V. Chelban, V. Salpietro, E. Oconnor, S. Efthymiou, D. Kullmann, R. Kaiyrzhanov, Roisin Sullivan, Alaa Khan, W. Y. Yau, I. Hostettler, E. Papanicolaou, E. Dardiotis, S. Maqbool, Shahnaz Ibrahim, S. Kirmani, N. Rana, Osama M Atawneh, Shen-Yang Lim, Farooq Shaikh, G. Koutsis, M. Breza, S. Mangano, C. Scuderi, Giovanna Morello, T. Stojkovic, E. Torti, M. Zollo, G. Heimer, Y. Dauvilliers, P. Striano, I. Al-Khawaja, Fuad Al-Mutairi, F. Alkuraya, Hamed Sherifa, M. Rizig, N. Okubadejo, O. Ojo, O. Oshinaike, K. Wahab, A. Bello, S. Abubakar, Yahaya O Obiabo, E. Nwazor, O. Ekenze, U. Williams, A. Iyagba, L. Taiwo, M. Komolafe, O. Oguntunde, S. Pchelina, Konstantin Senkevich, Nourelhoda A. Haridy, C. Shashkin, Nazira Zharkynbekova, Kairgali Koneyev, Ganieva Manizha, Maksudjon Isrofilov, Ulviyya Guliyeva, K. Salayev, Samson Khachatryan, S. Rossi, Gabriella Silvestri, Thomas Bourinaris, G. Xiromerisiou, L. Fidani, C. Spanaki, and A. Tucci. Pdxk mutations cause polyneuropathy responsive to pyridoxal 5′‐phosphate supplementation. Annals of Neurology, 86:225-240, Jul 2019. URL: https://doi.org/10.1002/ana.25524, doi:10.1002/ana.25524. This article has 94 citations and is from a highest quality peer-reviewed journal.

2. (OpenTargets Search: Neuropathy hereditary motor and sensory type VIc with optic atrophy): Open Targets Query (Neuropathy hereditary motor and sensory type VIc with optic atrophy, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (chelban2019pdxkmutationscause pages 6-7): V. Chelban, M. Wilson, J. Warman Chardon, J. Vandrovcova, M. N. Zanetti, E. Zamba-Papanicolaou, S. Efthymiou, S. Pope, M. Conte, Giancarlo Abis, Yo-Tsen Liu, Eloise Tribollet, Nourelhoda A. Haridy, J. Botía, M. Ryten, Paschalis Nicolaou, A. Minaidou, K. Christodoulou, K. Kernohan, Alison J Eaton, M. Osmond, Yoko A. Ito, P. Bourque, J. Jepson, O. Bello, F. Bremner, C. Cordivari, M. Reilly, M. Foiani, A. Heslegrave, H. Zetterberg, S. Heales, N. Wood, James E. Rothman, K. Boycott, P. Mills, P. Clayton, H. Houlden, Yamna Mohamed El Mhammed Stanislav Blagovesta Lionel Wol Kriouile Khorassani Aguennouz Groppa Marinova Kara, Y. Kriouile, M. Khorassani, M. Aguennouz, S. Groppa, Blagovesta Marinova Karashova, L. Van Maldergem, W. Nachbauer, S. Boesch, L. Arning, D. Timmann, B. Cormand, B. Pérez-Dueñas, G. Di Rosa, J. Goraya, T. Sultan, J. Mine, D. Avdjieva, H. Kathom, R. Tincheva, S. Banu, M. Pineda-Marfa, P. Veggiotti, Michel D. Ferrari, A. M. van den Maagdenberg, A. Verrotti, G. Marseglia, S. Savasta, M. García-Silva, A. M. Ruiz, Barbara H. Garavaglia, E. Borgione, S. Portaro, B. M. Sánchez, Richard S. Boles, S. Papacostas, M. Vikelis, James E. Rothman, P. Giunti, H. Houlden, V. Chelban, V. Salpietro, E. Oconnor, S. Efthymiou, D. Kullmann, R. Kaiyrzhanov, Roisin Sullivan, Alaa Khan, W. Y. Yau, I. Hostettler, E. Papanicolaou, E. Dardiotis, S. Maqbool, Shahnaz Ibrahim, S. Kirmani, N. Rana, Osama M Atawneh, Shen-Yang Lim, Farooq Shaikh, G. Koutsis, M. Breza, S. Mangano, C. Scuderi, Giovanna Morello, T. Stojkovic, E. Torti, M. Zollo, G. Heimer, Y. Dauvilliers, P. Striano, I. Al-Khawaja, Fuad Al-Mutairi, F. Alkuraya, Hamed Sherifa, M. Rizig, N. Okubadejo, O. Ojo, O. Oshinaike, K. Wahab, A. Bello, S. Abubakar, Yahaya O Obiabo, E. Nwazor, O. Ekenze, U. Williams, A. Iyagba, L. Taiwo, M. Komolafe, O. Oguntunde, S. Pchelina, Konstantin Senkevich, Nourelhoda A. Haridy, C. Shashkin, Nazira Zharkynbekova, Kairgali Koneyev, Ganieva Manizha, Maksudjon Isrofilov, Ulviyya Guliyeva, K. Salayev, Samson Khachatryan, S. Rossi, Gabriella Silvestri, Thomas Bourinaris, G. Xiromerisiou, L. Fidani, C. Spanaki, and A. Tucci. Pdxk mutations cause polyneuropathy responsive to pyridoxal 5′‐phosphate supplementation. Annals of Neurology, 86:225-240, Jul 2019. URL: https://doi.org/10.1002/ana.25524, doi:10.1002/ana.25524. This article has 94 citations and is from a highest quality peer-reviewed journal.

4. (chelban2019pdxkmutationscause pages 4-6): V. Chelban, M. Wilson, J. Warman Chardon, J. Vandrovcova, M. N. Zanetti, E. Zamba-Papanicolaou, S. Efthymiou, S. Pope, M. Conte, Giancarlo Abis, Yo-Tsen Liu, Eloise Tribollet, Nourelhoda A. Haridy, J. Botía, M. Ryten, Paschalis Nicolaou, A. Minaidou, K. Christodoulou, K. Kernohan, Alison J Eaton, M. Osmond, Yoko A. Ito, P. Bourque, J. Jepson, O. Bello, F. Bremner, C. Cordivari, M. Reilly, M. Foiani, A. Heslegrave, H. Zetterberg, S. Heales, N. Wood, James E. Rothman, K. Boycott, P. Mills, P. Clayton, H. Houlden, Yamna Mohamed El Mhammed Stanislav Blagovesta Lionel Wol Kriouile Khorassani Aguennouz Groppa Marinova Kara, Y. Kriouile, M. Khorassani, M. Aguennouz, S. Groppa, Blagovesta Marinova Karashova, L. Van Maldergem, W. Nachbauer, S. Boesch, L. Arning, D. Timmann, B. Cormand, B. Pérez-Dueñas, G. Di Rosa, J. Goraya, T. Sultan, J. Mine, D. Avdjieva, H. Kathom, R. Tincheva, S. Banu, M. Pineda-Marfa, P. Veggiotti, Michel D. Ferrari, A. M. van den Maagdenberg, A. Verrotti, G. Marseglia, S. Savasta, M. García-Silva, A. M. Ruiz, Barbara H. Garavaglia, E. Borgione, S. Portaro, B. M. Sánchez, Richard S. Boles, S. Papacostas, M. Vikelis, James E. Rothman, P. Giunti, H. Houlden, V. Chelban, V. Salpietro, E. Oconnor, S. Efthymiou, D. Kullmann, R. Kaiyrzhanov, Roisin Sullivan, Alaa Khan, W. Y. Yau, I. Hostettler, E. Papanicolaou, E. Dardiotis, S. Maqbool, Shahnaz Ibrahim, S. Kirmani, N. Rana, Osama M Atawneh, Shen-Yang Lim, Farooq Shaikh, G. Koutsis, M. Breza, S. Mangano, C. Scuderi, Giovanna Morello, T. Stojkovic, E. Torti, M. Zollo, G. Heimer, Y. Dauvilliers, P. Striano, I. Al-Khawaja, Fuad Al-Mutairi, F. Alkuraya, Hamed Sherifa, M. Rizig, N. Okubadejo, O. Ojo, O. Oshinaike, K. Wahab, A. Bello, S. Abubakar, Yahaya O Obiabo, E. Nwazor, O. Ekenze, U. Williams, A. Iyagba, L. Taiwo, M. Komolafe, O. Oguntunde, S. Pchelina, Konstantin Senkevich, Nourelhoda A. Haridy, C. Shashkin, Nazira Zharkynbekova, Kairgali Koneyev, Ganieva Manizha, Maksudjon Isrofilov, Ulviyya Guliyeva, K. Salayev, Samson Khachatryan, S. Rossi, Gabriella Silvestri, Thomas Bourinaris, G. Xiromerisiou, L. Fidani, C. Spanaki, and A. Tucci. Pdxk mutations cause polyneuropathy responsive to pyridoxal 5′‐phosphate supplementation. Annals of Neurology, 86:225-240, Jul 2019. URL: https://doi.org/10.1002/ana.25524, doi:10.1002/ana.25524. This article has 94 citations and is from a highest quality peer-reviewed journal.

5. (chelban2019pdxkmutationscause pages 7-9): V. Chelban, M. Wilson, J. Warman Chardon, J. Vandrovcova, M. N. Zanetti, E. Zamba-Papanicolaou, S. Efthymiou, S. Pope, M. Conte, Giancarlo Abis, Yo-Tsen Liu, Eloise Tribollet, Nourelhoda A. Haridy, J. Botía, M. Ryten, Paschalis Nicolaou, A. Minaidou, K. Christodoulou, K. Kernohan, Alison J Eaton, M. Osmond, Yoko A. Ito, P. Bourque, J. Jepson, O. Bello, F. Bremner, C. Cordivari, M. Reilly, M. Foiani, A. Heslegrave, H. Zetterberg, S. Heales, N. Wood, James E. Rothman, K. Boycott, P. Mills, P. Clayton, H. Houlden, Yamna Mohamed El Mhammed Stanislav Blagovesta Lionel Wol Kriouile Khorassani Aguennouz Groppa Marinova Kara, Y. Kriouile, M. Khorassani, M. Aguennouz, S. Groppa, Blagovesta Marinova Karashova, L. Van Maldergem, W. Nachbauer, S. Boesch, L. Arning, D. Timmann, B. Cormand, B. Pérez-Dueñas, G. Di Rosa, J. Goraya, T. Sultan, J. Mine, D. Avdjieva, H. Kathom, R. Tincheva, S. Banu, M. Pineda-Marfa, P. Veggiotti, Michel D. Ferrari, A. M. van den Maagdenberg, A. Verrotti, G. Marseglia, S. Savasta, M. García-Silva, A. M. Ruiz, Barbara H. Garavaglia, E. Borgione, S. Portaro, B. M. Sánchez, Richard S. Boles, S. Papacostas, M. Vikelis, James E. Rothman, P. Giunti, H. Houlden, V. Chelban, V. Salpietro, E. Oconnor, S. Efthymiou, D. Kullmann, R. Kaiyrzhanov, Roisin Sullivan, Alaa Khan, W. Y. Yau, I. Hostettler, E. Papanicolaou, E. Dardiotis, S. Maqbool, Shahnaz Ibrahim, S. Kirmani, N. Rana, Osama M Atawneh, Shen-Yang Lim, Farooq Shaikh, G. Koutsis, M. Breza, S. Mangano, C. Scuderi, Giovanna Morello, T. Stojkovic, E. Torti, M. Zollo, G. Heimer, Y. Dauvilliers, P. Striano, I. Al-Khawaja, Fuad Al-Mutairi, F. Alkuraya, Hamed Sherifa, M. Rizig, N. Okubadejo, O. Ojo, O. Oshinaike, K. Wahab, A. Bello, S. Abubakar, Yahaya O Obiabo, E. Nwazor, O. Ekenze, U. Williams, A. Iyagba, L. Taiwo, M. Komolafe, O. Oguntunde, S. Pchelina, Konstantin Senkevich, Nourelhoda A. Haridy, C. Shashkin, Nazira Zharkynbekova, Kairgali Koneyev, Ganieva Manizha, Maksudjon Isrofilov, Ulviyya Guliyeva, K. Salayev, Samson Khachatryan, S. Rossi, Gabriella Silvestri, Thomas Bourinaris, G. Xiromerisiou, L. Fidani, C. Spanaki, and A. Tucci. Pdxk mutations cause polyneuropathy responsive to pyridoxal 5′‐phosphate supplementation. Annals of Neurology, 86:225-240, Jul 2019. URL: https://doi.org/10.1002/ana.25524, doi:10.1002/ana.25524. This article has 94 citations and is from a highest quality peer-reviewed journal.

6. (chelban2019pdxkmutationscause pages 13-14): V. Chelban, M. Wilson, J. Warman Chardon, J. Vandrovcova, M. N. Zanetti, E. Zamba-Papanicolaou, S. Efthymiou, S. Pope, M. Conte, Giancarlo Abis, Yo-Tsen Liu, Eloise Tribollet, Nourelhoda A. Haridy, J. Botía, M. Ryten, Paschalis Nicolaou, A. Minaidou, K. Christodoulou, K. Kernohan, Alison J Eaton, M. Osmond, Yoko A. Ito, P. Bourque, J. Jepson, O. Bello, F. Bremner, C. Cordivari, M. Reilly, M. Foiani, A. Heslegrave, H. Zetterberg, S. Heales, N. Wood, James E. Rothman, K. Boycott, P. Mills, P. Clayton, H. Houlden, Yamna Mohamed El Mhammed Stanislav Blagovesta Lionel Wol Kriouile Khorassani Aguennouz Groppa Marinova Kara, Y. Kriouile, M. Khorassani, M. Aguennouz, S. Groppa, Blagovesta Marinova Karashova, L. Van Maldergem, W. Nachbauer, S. Boesch, L. Arning, D. Timmann, B. Cormand, B. Pérez-Dueñas, G. Di Rosa, J. Goraya, T. Sultan, J. Mine, D. Avdjieva, H. Kathom, R. Tincheva, S. Banu, M. Pineda-Marfa, P. Veggiotti, Michel D. Ferrari, A. M. van den Maagdenberg, A. Verrotti, G. Marseglia, S. Savasta, M. García-Silva, A. M. Ruiz, Barbara H. Garavaglia, E. Borgione, S. Portaro, B. M. Sánchez, Richard S. Boles, S. Papacostas, M. Vikelis, James E. Rothman, P. Giunti, H. Houlden, V. Chelban, V. Salpietro, E. Oconnor, S. Efthymiou, D. Kullmann, R. Kaiyrzhanov, Roisin Sullivan, Alaa Khan, W. Y. Yau, I. Hostettler, E. Papanicolaou, E. Dardiotis, S. Maqbool, Shahnaz Ibrahim, S. Kirmani, N. Rana, Osama M Atawneh, Shen-Yang Lim, Farooq Shaikh, G. Koutsis, M. Breza, S. Mangano, C. Scuderi, Giovanna Morello, T. Stojkovic, E. Torti, M. Zollo, G. Heimer, Y. Dauvilliers, P. Striano, I. Al-Khawaja, Fuad Al-Mutairi, F. Alkuraya, Hamed Sherifa, M. Rizig, N. Okubadejo, O. Ojo, O. Oshinaike, K. Wahab, A. Bello, S. Abubakar, Yahaya O Obiabo, E. Nwazor, O. Ekenze, U. Williams, A. Iyagba, L. Taiwo, M. Komolafe, O. Oguntunde, S. Pchelina, Konstantin Senkevich, Nourelhoda A. Haridy, C. Shashkin, Nazira Zharkynbekova, Kairgali Koneyev, Ganieva Manizha, Maksudjon Isrofilov, Ulviyya Guliyeva, K. Salayev, Samson Khachatryan, S. Rossi, Gabriella Silvestri, Thomas Bourinaris, G. Xiromerisiou, L. Fidani, C. Spanaki, and A. Tucci. Pdxk mutations cause polyneuropathy responsive to pyridoxal 5′‐phosphate supplementation. Annals of Neurology, 86:225-240, Jul 2019. URL: https://doi.org/10.1002/ana.25524, doi:10.1002/ana.25524. This article has 94 citations and is from a highest quality peer-reviewed journal.

7. (bunik2023thetherapeuticpotential pages 4-5): Victoria Bunik. The therapeutic potential of vitamins b1, b3 and b6 in charcot–marie–tooth disease with the compromised status of vitamin-dependent processes. Biology, 12:897, Jun 2023. URL: https://doi.org/10.3390/biology12070897, doi:10.3390/biology12070897. This article has 13 citations.

8. (chelban2019pdxkmutationscause pages 9-11): V. Chelban, M. Wilson, J. Warman Chardon, J. Vandrovcova, M. N. Zanetti, E. Zamba-Papanicolaou, S. Efthymiou, S. Pope, M. Conte, Giancarlo Abis, Yo-Tsen Liu, Eloise Tribollet, Nourelhoda A. Haridy, J. Botía, M. Ryten, Paschalis Nicolaou, A. Minaidou, K. Christodoulou, K. Kernohan, Alison J Eaton, M. Osmond, Yoko A. Ito, P. Bourque, J. Jepson, O. Bello, F. Bremner, C. Cordivari, M. Reilly, M. Foiani, A. Heslegrave, H. Zetterberg, S. Heales, N. Wood, James E. Rothman, K. Boycott, P. Mills, P. Clayton, H. Houlden, Yamna Mohamed El Mhammed Stanislav Blagovesta Lionel Wol Kriouile Khorassani Aguennouz Groppa Marinova Kara, Y. Kriouile, M. Khorassani, M. Aguennouz, S. Groppa, Blagovesta Marinova Karashova, L. Van Maldergem, W. Nachbauer, S. Boesch, L. Arning, D. Timmann, B. Cormand, B. Pérez-Dueñas, G. Di Rosa, J. Goraya, T. Sultan, J. Mine, D. Avdjieva, H. Kathom, R. Tincheva, S. Banu, M. Pineda-Marfa, P. Veggiotti, Michel D. Ferrari, A. M. van den Maagdenberg, A. Verrotti, G. Marseglia, S. Savasta, M. García-Silva, A. M. Ruiz, Barbara H. Garavaglia, E. Borgione, S. Portaro, B. M. Sánchez, Richard S. Boles, S. Papacostas, M. Vikelis, James E. Rothman, P. Giunti, H. Houlden, V. Chelban, V. Salpietro, E. Oconnor, S. Efthymiou, D. Kullmann, R. Kaiyrzhanov, Roisin Sullivan, Alaa Khan, W. Y. Yau, I. Hostettler, E. Papanicolaou, E. Dardiotis, S. Maqbool, Shahnaz Ibrahim, S. Kirmani, N. Rana, Osama M Atawneh, Shen-Yang Lim, Farooq Shaikh, G. Koutsis, M. Breza, S. Mangano, C. Scuderi, Giovanna Morello, T. Stojkovic, E. Torti, M. Zollo, G. Heimer, Y. Dauvilliers, P. Striano, I. Al-Khawaja, Fuad Al-Mutairi, F. Alkuraya, Hamed Sherifa, M. Rizig, N. Okubadejo, O. Ojo, O. Oshinaike, K. Wahab, A. Bello, S. Abubakar, Yahaya O Obiabo, E. Nwazor, O. Ekenze, U. Williams, A. Iyagba, L. Taiwo, M. Komolafe, O. Oguntunde, S. Pchelina, Konstantin Senkevich, Nourelhoda A. Haridy, C. Shashkin, Nazira Zharkynbekova, Kairgali Koneyev, Ganieva Manizha, Maksudjon Isrofilov, Ulviyya Guliyeva, K. Salayev, Samson Khachatryan, S. Rossi, Gabriella Silvestri, Thomas Bourinaris, G. Xiromerisiou, L. Fidani, C. Spanaki, and A. Tucci. Pdxk mutations cause polyneuropathy responsive to pyridoxal 5′‐phosphate supplementation. Annals of Neurology, 86:225-240, Jul 2019. URL: https://doi.org/10.1002/ana.25524, doi:10.1002/ana.25524. This article has 94 citations and is from a highest quality peer-reviewed journal.

9. (chelban2019pdxkmutationscause pages 14-15): V. Chelban, M. Wilson, J. Warman Chardon, J. Vandrovcova, M. N. Zanetti, E. Zamba-Papanicolaou, S. Efthymiou, S. Pope, M. Conte, Giancarlo Abis, Yo-Tsen Liu, Eloise Tribollet, Nourelhoda A. Haridy, J. Botía, M. Ryten, Paschalis Nicolaou, A. Minaidou, K. Christodoulou, K. Kernohan, Alison J Eaton, M. Osmond, Yoko A. Ito, P. Bourque, J. Jepson, O. Bello, F. Bremner, C. Cordivari, M. Reilly, M. Foiani, A. Heslegrave, H. Zetterberg, S. Heales, N. Wood, James E. Rothman, K. Boycott, P. Mills, P. Clayton, H. Houlden, Yamna Mohamed El Mhammed Stanislav Blagovesta Lionel Wol Kriouile Khorassani Aguennouz Groppa Marinova Kara, Y. Kriouile, M. Khorassani, M. Aguennouz, S. Groppa, Blagovesta Marinova Karashova, L. Van Maldergem, W. Nachbauer, S. Boesch, L. Arning, D. Timmann, B. Cormand, B. Pérez-Dueñas, G. Di Rosa, J. Goraya, T. Sultan, J. Mine, D. Avdjieva, H. Kathom, R. Tincheva, S. Banu, M. Pineda-Marfa, P. Veggiotti, Michel D. Ferrari, A. M. van den Maagdenberg, A. Verrotti, G. Marseglia, S. Savasta, M. García-Silva, A. M. Ruiz, Barbara H. Garavaglia, E. Borgione, S. Portaro, B. M. Sánchez, Richard S. Boles, S. Papacostas, M. Vikelis, James E. Rothman, P. Giunti, H. Houlden, V. Chelban, V. Salpietro, E. Oconnor, S. Efthymiou, D. Kullmann, R. Kaiyrzhanov, Roisin Sullivan, Alaa Khan, W. Y. Yau, I. Hostettler, E. Papanicolaou, E. Dardiotis, S. Maqbool, Shahnaz Ibrahim, S. Kirmani, N. Rana, Osama M Atawneh, Shen-Yang Lim, Farooq Shaikh, G. Koutsis, M. Breza, S. Mangano, C. Scuderi, Giovanna Morello, T. Stojkovic, E. Torti, M. Zollo, G. Heimer, Y. Dauvilliers, P. Striano, I. Al-Khawaja, Fuad Al-Mutairi, F. Alkuraya, Hamed Sherifa, M. Rizig, N. Okubadejo, O. Ojo, O. Oshinaike, K. Wahab, A. Bello, S. Abubakar, Yahaya O Obiabo, E. Nwazor, O. Ekenze, U. Williams, A. Iyagba, L. Taiwo, M. Komolafe, O. Oguntunde, S. Pchelina, Konstantin Senkevich, Nourelhoda A. Haridy, C. Shashkin, Nazira Zharkynbekova, Kairgali Koneyev, Ganieva Manizha, Maksudjon Isrofilov, Ulviyya Guliyeva, K. Salayev, Samson Khachatryan, S. Rossi, Gabriella Silvestri, Thomas Bourinaris, G. Xiromerisiou, L. Fidani, C. Spanaki, and A. Tucci. Pdxk mutations cause polyneuropathy responsive to pyridoxal 5′‐phosphate supplementation. Annals of Neurology, 86:225-240, Jul 2019. URL: https://doi.org/10.1002/ana.25524, doi:10.1002/ana.25524. This article has 94 citations and is from a highest quality peer-reviewed journal.

10. (rossor2024theevolvingspectrum pages 1-2): Alexander M. Rossor, Saif Haddad, and Mary M. Reilly. The evolving spectrum of complex inherited neuropathies. Current Opinion in Neurology, 37:427-444, Jul 2024. URL: https://doi.org/10.1097/wco.0000000000001307, doi:10.1097/wco.0000000000001307. This article has 13 citations and is from a peer-reviewed journal.

11. (chelban2019pdxkmutationscause pages 11-13): V. Chelban, M. Wilson, J. Warman Chardon, J. Vandrovcova, M. N. Zanetti, E. Zamba-Papanicolaou, S. Efthymiou, S. Pope, M. Conte, Giancarlo Abis, Yo-Tsen Liu, Eloise Tribollet, Nourelhoda A. Haridy, J. Botía, M. Ryten, Paschalis Nicolaou, A. Minaidou, K. Christodoulou, K. Kernohan, Alison J Eaton, M. Osmond, Yoko A. Ito, P. Bourque, J. Jepson, O. Bello, F. Bremner, C. Cordivari, M. Reilly, M. Foiani, A. Heslegrave, H. Zetterberg, S. Heales, N. Wood, James E. Rothman, K. Boycott, P. Mills, P. Clayton, H. Houlden, Yamna Mohamed El Mhammed Stanislav Blagovesta Lionel Wol Kriouile Khorassani Aguennouz Groppa Marinova Kara, Y. Kriouile, M. Khorassani, M. Aguennouz, S. Groppa, Blagovesta Marinova Karashova, L. Van Maldergem, W. Nachbauer, S. Boesch, L. Arning, D. Timmann, B. Cormand, B. Pérez-Dueñas, G. Di Rosa, J. Goraya, T. Sultan, J. Mine, D. Avdjieva, H. Kathom, R. Tincheva, S. Banu, M. Pineda-Marfa, P. Veggiotti, Michel D. Ferrari, A. M. van den Maagdenberg, A. Verrotti, G. Marseglia, S. Savasta, M. García-Silva, A. M. Ruiz, Barbara H. Garavaglia, E. Borgione, S. Portaro, B. M. Sánchez, Richard S. Boles, S. Papacostas, M. Vikelis, James E. Rothman, P. Giunti, H. Houlden, V. Chelban, V. Salpietro, E. Oconnor, S. Efthymiou, D. Kullmann, R. Kaiyrzhanov, Roisin Sullivan, Alaa Khan, W. Y. Yau, I. Hostettler, E. Papanicolaou, E. Dardiotis, S. Maqbool, Shahnaz Ibrahim, S. Kirmani, N. Rana, Osama M Atawneh, Shen-Yang Lim, Farooq Shaikh, G. Koutsis, M. Breza, S. Mangano, C. Scuderi, Giovanna Morello, T. Stojkovic, E. Torti, M. Zollo, G. Heimer, Y. Dauvilliers, P. Striano, I. Al-Khawaja, Fuad Al-Mutairi, F. Alkuraya, Hamed Sherifa, M. Rizig, N. Okubadejo, O. Ojo, O. Oshinaike, K. Wahab, A. Bello, S. Abubakar, Yahaya O Obiabo, E. Nwazor, O. Ekenze, U. Williams, A. Iyagba, L. Taiwo, M. Komolafe, O. Oguntunde, S. Pchelina, Konstantin Senkevich, Nourelhoda A. Haridy, C. Shashkin, Nazira Zharkynbekova, Kairgali Koneyev, Ganieva Manizha, Maksudjon Isrofilov, Ulviyya Guliyeva, K. Salayev, Samson Khachatryan, S. Rossi, Gabriella Silvestri, Thomas Bourinaris, G. Xiromerisiou, L. Fidani, C. Spanaki, and A. Tucci. Pdxk mutations cause polyneuropathy responsive to pyridoxal 5′‐phosphate supplementation. Annals of Neurology, 86:225-240, Jul 2019. URL: https://doi.org/10.1002/ana.25524, doi:10.1002/ana.25524. This article has 94 citations and is from a highest quality peer-reviewed journal.

12. (bunik2023thetherapeuticpotential pages 13-14): Victoria Bunik. The therapeutic potential of vitamins b1, b3 and b6 in charcot–marie–tooth disease with the compromised status of vitamin-dependent processes. Biology, 12:897, Jun 2023. URL: https://doi.org/10.3390/biology12070897, doi:10.3390/biology12070897. This article has 13 citations.

13. (chelban2019pdxkmutationscause pages 2-3): V. Chelban, M. Wilson, J. Warman Chardon, J. Vandrovcova, M. N. Zanetti, E. Zamba-Papanicolaou, S. Efthymiou, S. Pope, M. Conte, Giancarlo Abis, Yo-Tsen Liu, Eloise Tribollet, Nourelhoda A. Haridy, J. Botía, M. Ryten, Paschalis Nicolaou, A. Minaidou, K. Christodoulou, K. Kernohan, Alison J Eaton, M. Osmond, Yoko A. Ito, P. Bourque, J. Jepson, O. Bello, F. Bremner, C. Cordivari, M. Reilly, M. Foiani, A. Heslegrave, H. Zetterberg, S. Heales, N. Wood, James E. Rothman, K. Boycott, P. Mills, P. Clayton, H. Houlden, Yamna Mohamed El Mhammed Stanislav Blagovesta Lionel Wol Kriouile Khorassani Aguennouz Groppa Marinova Kara, Y. Kriouile, M. Khorassani, M. Aguennouz, S. Groppa, Blagovesta Marinova Karashova, L. Van Maldergem, W. Nachbauer, S. Boesch, L. Arning, D. Timmann, B. Cormand, B. Pérez-Dueñas, G. Di Rosa, J. Goraya, T. Sultan, J. Mine, D. Avdjieva, H. Kathom, R. Tincheva, S. Banu, M. Pineda-Marfa, P. Veggiotti, Michel D. Ferrari, A. M. van den Maagdenberg, A. Verrotti, G. Marseglia, S. Savasta, M. García-Silva, A. M. Ruiz, Barbara H. Garavaglia, E. Borgione, S. Portaro, B. M. Sánchez, Richard S. Boles, S. Papacostas, M. Vikelis, James E. Rothman, P. Giunti, H. Houlden, V. Chelban, V. Salpietro, E. Oconnor, S. Efthymiou, D. Kullmann, R. Kaiyrzhanov, Roisin Sullivan, Alaa Khan, W. Y. Yau, I. Hostettler, E. Papanicolaou, E. Dardiotis, S. Maqbool, Shahnaz Ibrahim, S. Kirmani, N. Rana, Osama M Atawneh, Shen-Yang Lim, Farooq Shaikh, G. Koutsis, M. Breza, S. Mangano, C. Scuderi, Giovanna Morello, T. Stojkovic, E. Torti, M. Zollo, G. Heimer, Y. Dauvilliers, P. Striano, I. Al-Khawaja, Fuad Al-Mutairi, F. Alkuraya, Hamed Sherifa, M. Rizig, N. Okubadejo, O. Ojo, O. Oshinaike, K. Wahab, A. Bello, S. Abubakar, Yahaya O Obiabo, E. Nwazor, O. Ekenze, U. Williams, A. Iyagba, L. Taiwo, M. Komolafe, O. Oguntunde, S. Pchelina, Konstantin Senkevich, Nourelhoda A. Haridy, C. Shashkin, Nazira Zharkynbekova, Kairgali Koneyev, Ganieva Manizha, Maksudjon Isrofilov, Ulviyya Guliyeva, K. Salayev, Samson Khachatryan, S. Rossi, Gabriella Silvestri, Thomas Bourinaris, G. Xiromerisiou, L. Fidani, C. Spanaki, and A. Tucci. Pdxk mutations cause polyneuropathy responsive to pyridoxal 5′‐phosphate supplementation. Annals of Neurology, 86:225-240, Jul 2019. URL: https://doi.org/10.1002/ana.25524, doi:10.1002/ana.25524. This article has 94 citations and is from a highest quality peer-reviewed journal.

14. (rossor2024theevolvingspectrum pages 9-10): Alexander M. Rossor, Saif Haddad, and Mary M. Reilly. The evolving spectrum of complex inherited neuropathies. Current Opinion in Neurology, 37:427-444, Jul 2024. URL: https://doi.org/10.1097/wco.0000000000001307, doi:10.1097/wco.0000000000001307. This article has 13 citations and is from a peer-reviewed journal.

15. (bunik2023thetherapeuticpotential pages 1-2): Victoria Bunik. The therapeutic potential of vitamins b1, b3 and b6 in charcot–marie–tooth disease with the compromised status of vitamin-dependent processes. Biology, 12:897, Jun 2023. URL: https://doi.org/10.3390/biology12070897, doi:10.3390/biology12070897. This article has 13 citations.

## Artifacts

- [Edison artifact artifact-00](Neuropathy_Hereditary_Motor_And_Sensory_Type_VIc_With_Optic_Atrophy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.