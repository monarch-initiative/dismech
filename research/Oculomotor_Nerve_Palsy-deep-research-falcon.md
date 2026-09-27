---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T07:13:03.078116'
end_time: '2026-08-20T07:25:50.181692'
duration_seconds: 767.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Oculomotor Nerve Palsy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Oculomotor_Nerve_Palsy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oculomotor Nerve Palsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Oculomotor Nerve Palsy** covering all of the
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
- **Disease Name:** Oculomotor Nerve Palsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Oculomotor Nerve Palsy** covering all of the
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


# Oculomotor Nerve Palsy: Disease-Characteristics Research Report

**Scope.** Oculomotor nerve palsy (ONP; third cranial nerve palsy) is a **clinical syndrome rather than one etiologically uniform disease**. This report distinguishes (1) common acquired CN III palsy from (2) congenital oculomotor dysinnervation, especially congenital fibrosis of the extraocular muscles (CFEOM). Evidence is disease-level and aggregated unless explicitly labeled as a case series, registry record, or model-organism result.

## Executive summary

CN III supplies the levator palpebrae superioris, superior/medial/inferior recti, inferior oblique, and parasympathetic fibers to the iris sphincter and ciliary muscle. Accordingly, complete palsy causes ptosis, a “down-and-out” eye, severe ophthalmoplegia and binocular diplopia, with variable mydriasis and impaired accommodation. New acquired palsy is a diagnostic emergency because a posterior communicating artery (PComA) aneurysm can compress the nerve; pupil sparing reduces but does **not** eliminate that possibility.

The best recent etiologic study, a 2024 referral-center cohort of 633 isolated cases, found microvascular disease in 26.5%, vascular anomalies in 17.4%, neoplasm in 13.6%, inflammation in 12.5%, idiopathic disease in 9.5%, and trauma in 8.4%. Intracranial aneurysms comprised 89/110 vascular anomalies. The cohort was 99.2% unilateral and had a median age of 59 years, but referral bias limits population inference. (kim2024etiologicaldistributionof pages 4-7, kim2024etiologicaldistributionof pages 3-4, kim2024etiologicaldistributionof pages 2-3)

Congenital disease belongs chiefly to the congenital cranial dysinnervation disorders. Dominant missense variants in **KIF21A**, **TUBB3**, and rarely **TUBA1A** disrupt microtubule behavior, kinesin interactions, or axon guidance; biallelic loss-of-function variants in **PHOX2A** cause CFEOM2. These developmental disorders are non-progressive but may cause amblyopia, corneal injury, abnormal head posture, and syndromic neurologic abnormalities. (fritzsch2023evolutionanddevelopment pages 16-18, puri2023tubb3andkif21a pages 1-2, jurgens2021novelvariantsin pages 1-2)

The following table maps the highest-yield evidence.

| domain | key finding/statistic | evidence type and population | source/date/URL | caveat |
|---|---|---|---|---|
| Acquired etiology | In 633 patients with isolated oculomotor nerve palsy, etiologies were microvascular 26.5%, vascular anomalies 17.4%, neoplastic 13.6%, inflammatory 12.5%, idiopathic 9.5%, traumatic 8.4%; congenital 4.1%; infectious 1.9%. MRI was performed in 96.1%; incidence showed peaks before age 10 and in the 60s; men:women 1.3:1. (kim2024etiologicaldistributionof pages 1-2, kim2024etiologicaldistributionof pages 4-7, kim2024etiologicaldistributionof pages 3-4, kim2024etiologicaldistributionof pages 2-3) | Retrospective referral-hospital cohort; human clinical; n=633 isolated CN III palsy cases | Kim et al., *Eur J Neurol* (Feb 2024), doi:10.1111/ene.16261, https://doi.org/10.1111/ene.16261 | Referral bias likely; single-center retrospective study; incidence estimate cited in paper but not population-based within this cohort. |
| Recovery/prognosis | In 65 CN III palsy cases, ischemic and compressive etiologies were most common (24.6% each). Complete recovery rates: ischemic 9/16, compressive 1/16, trauma 5/13, inflammation 6/10, idiopathic 2/10. Better long-term outcome associated with symptom onset <7 days and isolated nerve involvement. (srimanan2024retrospectiveanalysisof pages 2-4, srimanan2024retrospectiveanalysisof pages 6-7) | Retrospective tertiary-hospital cohort; human clinical; n=65 CN III palsy cases within larger ocular motor palsy study | Srimanan & Panyakorn, *Clin Ophthalmol* (Feb 2024), doi:10.2147/OPTH.S449127, https://doi.org/10.2147/OPTH.S449127 | Single-center; mixed referral population; prognostic modeling includes all third/fourth/sixth nerve palsies, though CN III data are reported separately. |
| Congenital genetics / MRI | In 122 CCDD patients from 96 families, all had restrictive eye movements; 47.9% had multiple congenital malformations. MRI in 94 patients showed cranial-nerve hypoplasia in essentially all except HGPPS cases; 17.0% had additional craniocerebral malformations. WES found 10 pathogenic variants in KIF21A, TUBB3, and CHN1 across 43 families; novel variants included KIF21A p.F355S, TUBB3 p.S78T, CHN1 p.H217R. In CFEOM, mutation detection was 63.6% (42/66), with KIF21A 73.8% and TUBB3 26.2% among solved CFEOM probands. (jia2022clinicalandgenetic pages 1-2, jia2022clinicalandgenetic pages 7-8, jia2022clinicalandgenetic pages 12-13, jia2022clinicalandgenetic pages 13-14) | Cohort with MRI + whole-exome sequencing; human congenital cranial dysinnervation disorders; n=122 | Jia et al., *Orphanet J Rare Dis* (Dec 2022), doi:10.1186/s13023-022-02582-5, https://doi.org/10.1186/s13023-022-02582-5 | CCDD cohort, not isolated acquired CN III palsy; data most directly inform congenital oculomotor dysinnervation/CFEOM. |
| Developmental mechanism | Pathogenic TUBB3 missense variants alter microtubule dynamics and cranial axon guidance; pathogenic KIF21A missense variants alter kinesin function and can phenocopy TUBB3 variants. CFEOM reflects hypoplasia of the oculomotor nerve with failed superior-division innervation of levator palpebrae superioris and superior rectus. (puri2023tubb3andkif21a pages 1-2, puri2023tubb3andkif21a pages 2-3, puri2023tubb3andkif21a pages 3-5) | Review synthesizing human genetics, MRI, in vitro and mouse studies | Puri, Barry & Engle, *Front Neurosci* (4 Aug 2023), doi:10.3389/fnins.2023.1226181, https://doi.org/10.3389/fnins.2023.1226181 | Mechanistic synthesis, not a treatment or epidemiology study; focuses on congenital disease biology rather than common acquired palsy. |
| Additional causal gene | Three unrelated probands with CFEOM had novel heterozygous TUBA1A missense variants: c.1216C>G p.His406Asp, c.467G>A p.Arg156His, c.1193T>G p.Met398Arg. MRI showed small oculomotor-innervated muscles and asymmetric caudate/lateral ventricular abnormalities; 2/3 also had malformations of cortical development. (jurgens2021novelvariantsin pages 1-2, jurgens2021novelvariantsin pages 9-10) | Primary sequencing study; human congenital CFEOM/tubulinopathy; n=3 probands | Jurgens et al., *Eur J Hum Genet* (1 Mar 2021 online), doi:10.1038/s41431-020-00804-7, https://doi.org/10.1038/s41431-020-00804-7 | Very small case series; supports rare congenital etiology only. |
| Clinical trial / acupuncture | Randomized parallel triple-masked interventional trial in ONP; estimated enrollment 177. Compared ocular electroacupuncture vs ocular acupuncture vs sham acupuncture over 6 weeks; primary outcome was change in ocular motor nerve function subscale at 6 weeks. Last known status: RECRUITING; overall registry status listed as UNKNOWN. (NCT03099447 chunk 1, NCT03099447 chunk 2) | ClinicalTrials.gov registry entry; interventional; adults with complete ONP | NCT03099447, first posted 4 Apr 2017, https://clinicaltrials.gov/study/NCT03099447 | Registry record only; no posted results in provided context; efficacy remains unproven here. |
| Clinical trial / retrospective acupuncture cohort | Observational retrospective cohort of ocular motor nerve palsy treated by ocular acupuncture; estimated enrollment 900; includes oculomotor, trochlear, and abducens palsy. Primary outcome: investigator-assessed clinical efficacy rate; last known status NOT_YET_RECRUITING, overall status UNKNOWN. (NCT03461809 chunk 1) | ClinicalTrials.gov registry entry; observational retrospective cohort | NCT03461809, first posted 12 Mar 2018, https://clinicaltrials.gov/study/NCT03461809 | Mixed ocular motor palsies; registry-only description; no posted outcomes in context. |
| Clinical trial / genetics registry | Large observational genetics study of strabismus/CCDDs and related anomalies; estimated enrollment 20,000; recruiting. Includes Third Nerve Palsy, Fourth Nerve Palsy, Sixth Nerve Palsy, CFEOM, DRS, Möbius, HGPPS, and related phenotypes; biospecimens include DNA. Primary outcome is gene discovery/characterization. (NCT03059420 chunk 1, NCT03059420 chunk 2) | ClinicalTrials.gov registry entry; observational genetics cohort | NCT03059420, recruiting; first posted 23 Feb 2017; updated 11 Feb 2026, https://clinicaltrials.gov/study/NCT03059420 | Broad congenital cranial dysinnervation/strabismus study, not specific to isolated acquired CN III palsy; observational, not therapeutic. |


*Table: This table compacts the highest-yield evidence identified for oculomotor nerve palsy, separating common acquired clinical data from rarer congenital genetic mechanisms and ongoing registry studies. It is useful as a source map for etiology, prognosis, molecular biology, and current trial activity.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** oculomotor nerve palsy/paralysis.
* **Synonyms:** third nerve palsy, third cranial nerve palsy, CN III palsy, oculomotor neuropathy, oculomotor nerve paralysis; “external ophthalmoplegia” may describe motor involvement without parasympathetic dysfunction but is not fully synonymous.
* **MONDO:** **MONDO:0001309**, “oculomotor nerve paralysis.” Open Targets maps this term to MONDO_0001309; its automated target associations should not be interpreted as a curated causal-gene list for ordinary acquired CN III palsy. (OpenTargets Search: oculomotor nerve palsy)
* **MeSH:** **D015840, Oculomotor Nerve Diseases**. ClinicalTrials.gov also maps diplopia to D004172 and ocular motility disorders to D015835. (NCT03099447 chunk 1)
* **ICD-10-CM:** commonly coded under **H49.0-** (third [oculomotor] nerve palsy; laterality-specific extensions). Local coding systems should be checked before database ingestion.
* **ICD-11:** falls within paralytic strabismus/ocular motor nerve palsy classifications; an exact leaf code was not verified in the retrieved primary sources.
* **OMIM/Orphanet:** there is no single etiologically adequate OMIM entry for all ONP. Congenital subtypes should instead be represented by their syndrome entries—CFEOM1/KIF21A, CFEOM2/PHOX2A, CFEOM3/TUBB3—and gene-disease records. CFEOM is MeSH C580012 in the trial-derived ontology. (NCT03059420 chunk 2)

### Clinical concept

CN III dysfunction is diagnosed by weakness of its innervated extraocular muscles, with or without ptosis or pupillary involvement. A 2024 study operationalized ONP as exotropia, vertical misalignment and/or ptosis, with or without pupillary involvement. (srimanan2024retrospectiveanalysisof pages 2-4)

## 2. Etiology, risk factors, and protective factors

### Acquired causes

The 2024 cohort reported microvascular 168/633 (26.5%), vascular anomaly 110/633 (17.4%), neoplastic 86/633 (13.6%), inflammatory 79/633 (12.5%), idiopathic 60/633 (9.5%), traumatic 53/633 (8.4%), stroke/other vascular 4.4%, congenital 4.1%, and infectious 1.9%. Primary CNS tumors included meningioma and pituitary adenoma, each 24/69 primary tumors; vascular anomalies included aneurysm 89/110, dural arteriovenous fistula 10/110, cavernous malformation 9/110, and AVM 2/110. (kim2024etiologicaldistributionof pages 4-7, kim2024etiologicaldistributionof pages 3-4)

Additional causes include midbrain infarction or hemorrhage, cavernous-sinus/orbital-apex disease, Tolosa–Hunt syndrome, demyelination, recurrent painful ophthalmoplegic neuropathy, Miller Fisher syndrome, neurosurgical/iatrogenic injury, and infections affecting nerve, meninges, cavernous sinus, or orbital apex. The cited cohort required pathogen-compatible serology/CSF for infectious classification and MRI lesions plus steroid responsiveness for presumed inflammatory disease. (kim2024etiologicaldistributionof pages 2-3)

### Risk factors

* **Microvascular:** older age, diabetes mellitus, hypertension, dyslipidemia, and smoking. In the 2024 study, microvascular palsy required acute onset, at least one such risk factor, no explanatory MRI lesion, and spontaneous recovery within one year. (kim2024etiologicaldistributionof pages 2-3)
* **Aneurysmal/compressive:** female sex and intracranial-aneurysm risk factors are relevant at the population level. In the 633-person series, vascular anomalies were more frequent in women (27.1%) than men (9.6%). (kim2024etiologicaldistributionof pages 4-7)
* **Trauma:** head injury, including road-traffic injury; trauma predominates more strongly in younger patients.
* **Inflammatory/infectious:** systemic inflammatory disease, immunosuppression, meningitis, cavernous-sinus infection, and relevant regional pathogens.
* **Genetic:** pathogenic variants causing CFEOM/CCDDs; these are causes of congenital dysinnervation rather than susceptibility alleles for typical late-onset ischemic palsy.

### Protective factors and gene–environment interaction

No replicated **genetic protective variant** specific to ONP was identified. Environmental protection is therefore inferred from cause prevention: control blood pressure, diabetes and lipids; stop smoking; prevent head injury; promptly treat infection; and manage aneurysm risk. Evidence for a CN III-specific diet, supplement, or exercise regimen is absent.

The clearest gene–environment framework is not a proven locus interaction but reduced neural-repair reserve with aging plus vascular or traumatic injury. Generic peripheral-nerve mouse experiments show that aging and chronic denervation reduce Schwann-cell c-Jun and regenerative support; restoring c-Jun normalized regeneration. This is biologically relevant but **indirect evidence**, not a demonstrated CN III intervention. (wagstaff2021failuresofnerve pages 1-2)

## 3. Phenotypes

| Phenotype | Type/course | Suggested HPO term |
|---|---|---|
| Ptosis | Clinical sign; partial or complete; congenital or acute | **HP:0000508 Ptosis**; congenital ptosis **HP:0007911** |
| Binocular diplopia | Symptom; acute in acquired ONP; disappears when either eye is covered | **HP:0000651 Diplopia** |
| External ophthalmoplegia | Sign; impaired adduction, elevation and depression; severity variable | **HP:0000544 External ophthalmoplegia** |
| Exotropia/hypotropia, “down-and-out” eye | Physical sign from unopposed lateral rectus/superior oblique | **HP:0000577 Exotropia**, **HP:0000545 Myopia** is not appropriate; use strabismus **HP:0000486** plus vertical deviation annotation |
| Mydriasis/anisocoria | Parasympathetic sign; may be absent | **HP:0011499 Anisocoria**, **HP:0000554 Tonic pupil** only if specifically established |
| Impaired pupillary light response/accommodation | Functional sign | **HP:0007686 Abnormal pupillary function** |
| Periorbital pain/headache | Symptom, particularly aneurysmal or inflammatory disease | **HP:0002315 Headache**, **HP:0100608 Miosis** should not be used for typical compressive ONP |
| Aberrant regeneration/synkinesis | Late sign after severe injury; lid elevation or pupil constriction with attempted gaze | **HP:0012378 Abnormal eye movement**; add synkinesis concept where supported |
| CFEOM | Congenital, non-progressive restrictive ophthalmoplegia with ptosis | **HP:0001491 CFEOM**, **HP:0007911 congenital ptosis** |
| Amblyopia | Pediatric complication of misalignment/ptosis | **HP:0000646 Amblyopia** |

In the 633-person acquired/congenital cohort, 628/633 (99.2%) were unilateral and five were bilateral; right and left sides were approximately equal. Age ranged from 2 months to 85 years, with peaks before age ten and in the 60s. (kim2024etiologicaldistributionof pages 2-3)

CFEOM is defined by congenital ptosis and non-progressive paralytic strabismus, particularly restricted upgaze, with variable restriction of down- and horizontal gaze. The eye cannot be moved actively **or passively** into restricted positions because chronic dysinnervation produces secondary muscle fibrosis. Long-term effects include amblyopia, corneal injury, and neck/back discomfort from compensatory head posture. (puri2023tubb3andkif21a pages 1-2)

**Quality of life.** Diplopia impairs reading, driving, mobility, depth judgment, work, and fall safety; ptosis impairs the superior visual field; congenital disease affects visual development and posture. No robust ONP-specific EQ-5D or SF-36 population estimates were found. The acupuncture trial planned a physical/psychological ONP quality-of-life questionnaire but has no results in the retrieved registry. (NCT03099447 chunk 1)

## 4. Genetic and molecular information

### Causal genes in congenital disease

* **KIF21A**: usually heterozygous missense, autosomal dominant or de novo; principally CFEOM1. Variants weaken motor-domain/stalk autoinhibition, causing excessive microtubule interaction and oculomotor axon stalling. Mouse knock-in models reproduce stalled CN III axons and hypoplastic target muscles. (fritzsch2023evolutionanddevelopment pages 16-18, puri2023tubb3andkif21a pages 3-5)
* **TUBB3**: heterozygous, often de novo missense variants; CFEOM3 or broader tubulinopathy. Variants alter microtubule dynamics, kinesin binding and axon guidance. Recurrent substitutions include p.Arg262Cys/His, p.Ala302Thr, p.Arg380Cys, p.Glu410Lys and p.Asp417Asn; syndromic findings may include facial weakness, axonal neuropathy, joint contractures, neurodevelopmental impairment and white-matter/basal-ganglia malformations. (puri2023tubb3andkif21a pages 1-2, puri2023tubb3andkif21a pages 2-3, puri2023tubb3andkif21a pages 3-5)
* **PHOX2A**: biallelic loss-of-function, autosomal recessive CFEOM2; defective specification/survival of oculomotor and trochlear motor neurons. Mouse loss causes absent CN III/IV nuclei and nerves. (fritzsch2023evolutionanddevelopment pages 16-18)
* **TUBA1A**: rare heterozygous missense CFEOM/tubulinopathy. Three reported variants are c.1216C>G p.His406Asp, c.467G>A p.Arg156His and c.1193T>G p.Met398Arg. Residues affect α/β-tubulin longitudinal or protofilament lateral interfaces; two of three probands had cortical malformations. **PMID 33649541**, published online March 1, 2021; https://doi.org/10.1038/s41431-020-00804-7. (jurgens2021novelvariantsin pages 1-2, NCT03059420 chunk 2)
* Other CCDD genes can create overlapping ocular-motor phenotypes: **TUBB2B, CHN1, ECEL1, MYF5, COL25A1, MAFB, SALL4, HOXA1, ROBO3, ACKR3/CXCR7** and others. They should not automatically be labeled as isolated CN III-palsy genes. Open Targets associations such as MAPT largely reflect phenotype/text-mining links and are not evidence that MAPT causes ordinary acquired ONP. (OpenTargets Search: oculomotor nerve palsy, NCT03059420 chunk 2)

### Human sequencing evidence

In 122 Chinese patients from 96 CCDD families, WES detected ten pathogenic variants in **KIF21A, TUBB3,** or **CHN1** across 43 families. Novel variants included KIF21A c.1064T>C p.Phe355Ser, TUBB3 c.232T>A p.Ser78Thr, and CHN1 c.650A>G p.His217Arg. CFEOM’s molecular diagnostic rate was 42/66 (63.6%) and 100% in familial cases; among solved CFEOM families, 31/42 involved KIF21A and 11/42 TUBB3. (jia2022clinicalandgenetic pages 1-2, jia2022clinicalandgenetic pages 7-8)

Variants were filtered against population databases including gnomAD with a >1% MAF exclusion threshold and validated by Sanger sequencing/segregation. Exact gnomAD allele frequencies and ClinVar accessions for each variant were not available in the retrieved text and must be obtained variant-by-variant before production annotation. (jia2022clinicalandgenetic pages 13-14)

No validated modifier genes, characteristic somatic variants, DNA-methylation signature, chromosomal abnormality, or ONP-specific epigenetic mechanism is established. Germline variants dominate congenital disease; acquired palsy is generally non-genetic and lesion-based.

## 5. Environmental, lifestyle and infectious information

Relevant non-genetic exposures include head trauma, neurosurgical/endovascular procedures, smoking and vascular-metabolic exposures. No consistent toxin, radiation, occupational exposure, alcohol dose, nutritional deficiency, or pollution association specific to isolated ONP was verified.

Infectious mechanisms include meningitis, direct neuritis, vasculitis, cavernous-sinus thrombosis and orbital-apex inflammation. The 2024 series attributed 12/633 (1.9%) cases to infection using compatible clinical, serologic and CSF evidence. Pathogens are heterogeneous; no single organism defines the disease. (kim2024etiologicaldistributionof pages 3-4, kim2024etiologicaldistributionof pages 2-3)

## 6. Mechanism and pathophysiology

### Acquired causal chains

1. **Microvascular:** diabetes/hypertension/dyslipidemia/smoking → small-vessel injury and endoneurial ischemia → focal demyelination/axonal dysfunction of CN III → ophthalmoplegia, ptosis and diplopia. Superficial pupillomotor fibers may be relatively spared, but pupil sparing is not an absolute discriminator.
2. **Compressive aneurysm:** PComA aneurysm enlargement/rupture → mechanical deformation and compromised perfusion of the nearby cisternal CN III → preferential superficial parasympathetic-fiber injury → painful ophthalmoplegia with mydriasis, potentially followed by subarachnoid hemorrhage. The cisternal nerve lies about 1.7 mm from PComA in cited anatomical synthesis. (ge2025oculomotornervepalsy pages 2-3)
3. **Tumor/inflammation/cavernous sinus:** mass, infiltrate, granulomatous inflammation or thrombosis → fascicular compression, inflammation and impaired conduction; neighboring CN IV, V1/V2 or VI deficits indicate regional extension.
4. **Trauma:** stretch, shear, contusion or avulsion → axonal disruption/Wallerian degeneration → incomplete or misdirected reinnervation and possible synkinesis.
5. **Congenital:** pathogenic KIF21A/tubulin/PHOX2A alteration → abnormal motor-neuron specification or microtubule-dependent axon extension/targeting → hypoplastic CN III divisions and denervated extraocular muscles → secondary muscle hypoplasia/fibrosis, ptosis and fixed strabismus. (puri2023tubb3andkif21a pages 1-2, jurgens2021novelvariantsin pages 1-2)

### Cellular/molecular annotations

Suggested biological-process terms include **GO:0007409 axonogenesis**, **GO:0007411 axon guidance**, **GO:0031175 neuron projection development**, **GO:0007017 microtubule-based process**, **GO:0007018 microtubule-based movement**, **GO:0042552 myelination**, **GO:0048679 regulation of axon regeneration**, and **GO:0008219 cell death**. Relevant cell types include oculomotor motor neuron, parasympathetic preganglionic neuron, Schwann cell (**CL:0002573**), macrophage (**CL:0000235**), vascular endothelial cell (**CL:0000115**), and extraocular skeletal myocyte.

Generic peripheral-nerve injury studies support NMNAT2 depletion followed by SARM1 NADase activation as an upstream programmed-axon-death mechanism; downstream Schwann-cell dedifferentiation, c-JUN activation, myelinophagy, macrophage recruitment, Büngner-band formation, axon regrowth and remyelination support repair. The review states that “NMNAT2 and SARM1 are required for axon survival and degeneration, respectively.” These pathways have **not** been molecularly profiled specifically in human CN III palsy. (arthurfarraj2021lessonsfrominjury pages 1-2)

A direct mouse experiment found that aging/chronic denervation reduced Schwann-cell c-Jun and that genetic restoration “restores regeneration to control levels.” This is model-organism evidence, not a clinical therapy. (wagstaff2021failuresofnerve pages 1-2)

No reproducible CN III-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic or multi-omic signature was identified. This is a major research gap.

## 7. Anatomical structures affected

* **Nucleus/fascicle:** oculomotor nuclear complex and Edinger–Westphal region in the midbrain; fascicles traverse the tegmentum.
* **Cisternal segment:** exits ventral midbrain, passes between posterior cerebral and superior cerebellar arteries and near PComA.
* **Cavernous sinus/superior orbital fissure/orbit:** lesions here may involve other ocular motor or trigeminal nerves.
* **Targets:** levator palpebrae superioris, superior rectus, medial rectus, inferior rectus, inferior oblique; ciliary ganglion, iris sphincter and ciliary muscle.
* **Secondary tissues:** cornea from exposure, visual cortex/visual development through amblyopia, and cervical musculoskeletal structures from abnormal head posture.

Suggested UBERON annotations: **oculomotor nerve (CN III)**, midbrain, cavernous sinus, orbit, extraocular muscle, ciliary ganglion, iris and cornea. Exact UBERON accessions should be resolved against the production ontology release. Subcellular compartments particularly relevant to congenital disease are the microtubule cytoskeleton (**GO:0015630**), kinesin complex, axon and growth cone.

CFEOM MRI shows hypoplastic CN III and underdeveloped superior rectus/levator muscles, with variable inferior-division and CN VI involvement. TUBB3 variants may additionally cause corpus-callosum, anterior-commissure, basal-ganglia, thalamic, brainstem and cerebellar abnormalities. (puri2023tubb3andkif21a pages 1-2, puri2023tubb3andkif21a pages 3-5)

## 8. Temporal development

Acquired palsy usually begins acutely or subacutely. Aneurysmal palsy and associated pain can evolve over hours to days; microvascular palsy is typically acute; tumors may be progressive; inflammatory disease may fluctuate or relapse. Congenital palsy/CFEOM is present from infancy and generally non-progressive, although secondary fibrosis, amblyopia and postural complications evolve over time.

Microvascular recovery usually occurs over weeks to months; absence of improvement by roughly 12 weeks, progression, new neurologic signs or recurrence requires diagnostic reconsideration. In a 2024 hospital cohort, complete recovery occurred in 9/16 ischemic, 1/16 compressive, 5/13 traumatic, 6/10 inflammatory and 2/10 idiopathic CN III cases. Across ocular motor palsies, onset documented within seven days and isolated nerve involvement predicted better outcome. (srimanan2024retrospectiveanalysisof pages 6-7)

## 9. Inheritance and population epidemiology

Published population estimates place acquired ONP incidence at approximately **3.7–4.0 per 100,000 person-years**. Incidence rises markedly with age. The 633-case referral cohort had median age 59 years, male:female ratio 1.3:1 and dual age peaks before age ten and in the 60s; these distributions should not be treated as population prevalence. (kim2024etiologicaldistributionof pages 1-2, kim2024etiologicaldistributionof pages 2-3)

Acquired ONP is usually sporadic and multifactorial. CFEOM1/KIF21A and many TUBB3/TUBA1A disorders are autosomal dominant, often de novo, with variable expressivity. PHOX2A-related CFEOM2 is autosomal recessive; consanguinity therefore increases risk. Penetrance is high for classic familial CFEOM but exact variant-specific estimates differ. Genetic anticipation is not established. Germline mosaicism is theoretically relevant after an apparently de novo result but was not quantified. Founder variants and carrier frequencies are not adequately defined in the retrieved evidence.

## 10. Diagnostics

### Immediate clinical assessment

Document onset, pain/headache, trauma, vascular risks, cancer/infection/inflammatory history and neurologic symptoms. Examine visual acuity, fields, pupils in light/dark, eyelid position, ductions, alignment, fundus and all cranial nerves. Determine complete versus partial, pupil-involving versus pupil-sparing, isolated versus non-isolated and congenital versus acquired disease.

**Emergency principle:** a new acquired CN III palsy—especially painful, pupil-involving, partial/progressive, or occurring in a young patient without vascular risks—requires urgent vascular imaging for aneurysm. Modern CTA or MRA is first-line; catheter angiography is reserved for unresolved high suspicion or intervention planning. Pupil sparing alone should not be used to defer imaging.

MRI brain/orbits with and without gadolinium, thin sections along CN III, diffusion-weighted imaging, and MRA evaluates midbrain infarction, nerve enhancement, cavernous sinus, orbital apex and tumor. In the 2024 etiologic cohort, MRI was obtained in 608/633 (96.1%). (kim2024etiologicaldistributionof pages 2-3)

### Laboratory and ancillary tests

Testing is hypothesis-driven: glucose/HbA1c, blood pressure, lipids, CBC/chemistry, ESR/CRP in older patients where giant-cell arteritis is plausible, infectious serology/CSF when indicated, thyroid studies, acetylcholine-receptor/MuSK antibodies for myasthenia, and lumbar puncture for meningitis/inflammation/malignancy when imaging and context warrant. EMG has limited routine value for CN III but may help characterize extraocular muscle denervation in specialist centers.

### Genetic testing

For congenital non-progressive ptosis/ophthalmoplegia, obtain high-resolution cranial-nerve/orbital MRI and a CCDD/CFEOM panel including **KIF21A, TUBB3, PHOX2A, TUBA1A, TUBB2B, CHN1, ECEL1, MYF5, COL25A1, MAFB, SALL4, HOXA1, ROBO3** and phenotype-driven genes. Trio WES/GS is appropriate after a negative panel or in syndromic cases; CNV analysis should accompany sequencing. CMA/karyotype/FISH are reserved for multiple congenital anomalies or suspected chromosomal disease. Mitochondrial and repeat-expansion testing are not routine unless the broader phenotype suggests them. MRI plus WES achieved a 63.6% molecular diagnosis in the reported CFEOM cohort. (jia2022clinicalandgenetic pages 7-8)

### Differential diagnosis

Exclude myasthenia gravis, thyroid eye disease, orbital myositis/mass, restrictive strabismus, skew deviation, internuclear ophthalmoplegia, dorsal midbrain syndrome, Horner syndrome, Adie pupil, pharmacologic mydriasis, CPEO/mitochondrial disease, Miller Fisher syndrome and recurrent painful ophthalmoplegic neuropathy. Proptosis, chemosis, sensory loss, optic neuropathy or multiple cranial neuropathies localize away from an isolated nerve lesion.

There is no general-population or newborn screening program. Cascade genetic testing is appropriate after identifying a pathogenic congenital variant.

## 11. Outcome and prognosis

ONP itself generally does not reduce life expectancy; mortality is determined by the underlying aneurysm, stroke, malignancy, infection or trauma. Therefore, disease-specific five- or ten-year survival statistics are not meaningful for ONP as a syndrome.

A 2020 tertiary-center series reported complete or partial recovery in 69.7% of acquired third-nerve palsies, but setting and etiologic composition constrain generalization. The 2024 etiology-specific complete-recovery figures demonstrate that inflammatory and ischemic palsies fare better than compressive disease. (srimanan2024retrospectiveanalysisof pages 2-4, srimanan2024retrospectiveanalysisof pages 6-7)

Poor prognostic features include complete palsy, severe axonal injury, compressive/neoplastic etiology, multiple cranial nerves, delayed treatment of the cause, prolonged denervation and aberrant regeneration. Persistent diplopia, ptosis, fixed strabismus, amblyopia, exposure keratopathy and synkinesis are the main disabilities. No validated molecular prognostic biomarker exists.

## 12. Treatment and current applications

### Cause-directed treatment

1. **PComA/intracranial aneurysm:** urgent neurosurgical/endovascular assessment; clipping, coiling, stent/balloon-assisted coiling or flow diversion according to rupture status and anatomy. The purpose is prevention/treatment of hemorrhage and decompression or exclusion of the aneurysm—not merely ocular realignment.
2. **Microvascular palsy:** observation after adequate imaging/evaluation, vascular-risk control, analgesia and temporary diplopia treatment. There is no proven drug that accelerates CN III regeneration.
3. **Inflammatory disease:** corticosteroids or disease-specific immunotherapy only after excluding infection and defining the disorder. The 2024 cohort used oral corticosteroid 1 mg/kg/day for at least two weeks with taper in inflammatory cases, but this was not randomized evidence. (srimanan2024retrospectiveanalysisof pages 2-4)
4. **Infection/cavernous-sinus thrombosis:** organism-directed antimicrobial therapy and source control; anticoagulation according to the underlying thrombosis protocol.
5. **Tumor:** surgery, radiation or systemic therapy according to pathology and location.
6. **Trauma:** treat associated injuries, protect the eye, observe for recovery, then rehabilitate alignment.

Suggested NCIt concepts include **aneurysm clipping**, **endovascular coil embolization**, **corticosteroid therapy**, **antimicrobial therapy**, **radiation therapy**, **strabismus surgery**, **botulinum toxin injection**, **prism therapy**, and **occlusion therapy**; exact NCIt codes should be resolved in the current release.

### Symptomatic and rehabilitative treatment

Temporary occlusion, fogging or Fresnel prisms may reduce diplopia; prisms are often limited by large incomitant deviations. Lubrication and corneal protection are used if eyelid closure or corneal sensation is compromised. Botulinum toxin to the antagonist lateral rectus is sometimes used in selected partial/acute palsies, but evidence is heterogeneous and it can cause ptosis or vertical deviation.

After alignment stabilizes, strabismus surgery may combine lateral-rectus weakening, medial-rectus strengthening, transposition or globe-fixation procedures. Ptosis repair is delayed until alignment and corneal-protection risks are addressed. Surgery improves primary-position alignment more reliably than full motility; repeated procedures may be required. CFEOM surgery is similarly individualized and does not restore normal innervation.

No approved gene, cell, RNA, CRISPR or regenerative therapy exists for ONP. Pharmacogenomic guidance is not established.

### Trials

* **NCT03099447:** randomized, parallel, triple-masked ocular electroacupuncture versus acupuncture versus sham; estimated n=177, six weeks. Registry status is **UNKNOWN** (last known recruiting), and no results were available; efficacy remains unproven. https://clinicaltrials.gov/study/NCT03099447. (NCT03099447 chunk 1)
* **NCT03461809:** retrospective acupuncture cohort across CN III/IV/VI palsies, estimated n=900; status **UNKNOWN**, with no posted results in the retrieved record. https://clinicaltrials.gov/study/NCT03461809. (NCT03461809 chunk 1)
* **NCT03059420:** recruiting Boston Children’s/Howard Hughes observational genetics cohort, estimated n=20,000, including CFEOM and third-nerve palsy; not a treatment trial. https://clinicaltrials.gov/study/NCT03059420. (NCT03059420 chunk 1, NCT03059420 chunk 2)

## 13. Prevention

* **Primary:** control diabetes, hypertension and dyslipidemia; stop smoking; use seatbelts/helmets and fall/occupational injury prevention; manage infection and aneurysm risk according to established disease-specific guidance.
* **Secondary:** urgent recognition and CTA/MRA of new acquired palsy to prevent aneurysmal rupture or identify treatable tumor, stroke, infection or inflammation. There is no evidence-based screening of asymptomatic average-risk people for ONP.
* **Tertiary:** prevent amblyopia in children, corneal exposure, falls and driving injury; use temporary diplopia control, rehabilitation and delayed alignment surgery.
* **Genetic:** counseling, cascade testing, and reproductive options—including prenatal or preimplantation testing—are appropriate only after a familial pathogenic variant is established. No vaccine specifically prevents ONP; routine immunization may indirectly prevent selected neuroinvasive infections.

## 14. Other species and natural disease

Oculomotor neuropathy occurs naturally in domestic animals, including dogs, cats and horses, usually from trauma, inflammation, neoplasia, vascular disease or multifocal neurologic disease rather than a common breed-specific Mendelian syndrome. A 2024 report described bilateral idiopathic oculomotor neuropathy in a cat, but sufficient full text was unavailable for detailed annotation. Evidence is therefore limited to case-level veterinary observations. There is no zoonotic transmission of “oculomotor palsy”; only an underlying infectious cause could itself be transmissible.

Relevant taxa are **Homo sapiens (NCBI Taxon 9606)**, **Mus musculus (10090)**, **Rattus norvegicus (10116)**, **Danio rerio (7955)**, **Drosophila melanogaster (7227)**, **Felis catus (9685)**, **Canis lupus familiaris (9615)** and **Equus caballus (9796)**.

## 15. Model organisms

* **Kif21a knock-in mouse:** reproduces CFEOM1-like oculomotor axon stalling and hypoplastic extraocular targets; strong developmental-mechanism model, but not acquired palsy. (fritzsch2023evolutionanddevelopment pages 16-18)
* **Phox2a-null mouse:** lacks normal oculomotor/trochlear nuclei and nerves, modeling recessive CFEOM2; severe developmental phenotype limits therapeutic extrapolation. (fritzsch2023evolutionanddevelopment pages 16-18)
* **Tubb3 variant/knockout mouse and neuronal culture:** tests variant-specific microtubule dynamics, kinesin interaction and axon guidance. Simple loss of Tubb3 does not fully reproduce dominant human missense disease, demonstrating that substitution-specific altered function—not haploinsufficiency—is central. (puri2023tubb3andkif21a pages 1-2, jurgens2021novelvariantsin pages 1-2)
* **Tuba1a mutant mouse:** models cortical-development/tubulin defects, often with severe or perinatal-lethal brain phenotypes; it incompletely models isolated human CFEOM. (jurgens2021novelvariantsin pages 1-2, jurgens2021novelvariantsin pages 9-10)
* **Generic peripheral-nerve injury models:** mouse sciatic-nerve crush/transection and chronic denervation define SARM1/NMNAT2 axon death and Schwann-cell c-JUN repair programs. Their anatomy and target-distance differ substantially from human CN III, so they provide pathway hypotheses rather than validated ONP therapies. (arthurfarraj2021lessonsfrominjury pages 1-2, wagstaff2021failuresofnerve pages 1-2)

## Evidence-supported abstract quotations

* Puri et al. (published **August 4, 2023**) state: “Human pathogenic TUBB3 missense variants result in altered TUBB3 function” and cause errors in cranial axon growth/guidance; KIF21A variants likewise “cause errors in cranial axon growth and guidance.” https://doi.org/10.3389/fnins.2023.1226181. (puri2023tubb3andkif21a pages 1-2)
* Jurgens et al. (published online **March 1, 2021**; PMID **33649541**) report: “we identified 3 unrelated probands with CFEOM who harbored novel heterozygous TUBA1A missense variants.” https://doi.org/10.1038/s41431-020-00804-7. (jurgens2021novelvariantsin pages 1-2, NCT03059420 chunk 2)
* Wagstaff et al. (**January 21, 2021**) report that genetically restoring Schwann-cell c-Jun “restores regeneration to control levels” in aging/chronic-denervation mouse models. https://doi.org/10.7554/eLife.62232. (wagstaff2021failuresofnerve pages 1-2)
* Jessen and Mirsky (**February 11, 2019**) describe repair Schwann cells as activating functions that “engineer myelin clearance, prevent neuronal death, and help axon growth and guidance.” https://doi.org/10.3389/fncel.2019.00033. (jessen2019thesuccessand pages 1-2)

## Knowledge gaps and curation cautions

ONP has no unified molecular signature because it is a final common phenotype of ischemia, compression, inflammation, trauma, infection and developmental dysinnervation. Gene associations must therefore be attached to the appropriate congenital syndrome, not indiscriminately to all ONP. No validated protective allele, modifier gene, epigenetic signature, fluid biomarker, pharmacogenomic rule, disease-specific omics diagnostic, or approved regenerative therapy exists. Recent clinical literature remains dominated by retrospective referral cohorts; randomized treatment evidence is sparse, and the registered acupuncture studies have no available results. The strongest immediate real-world application remains **rapid anatomical diagnosis—especially exclusion of aneurysm—followed by cause-specific treatment and staged ocular rehabilitation**.

References

1. (kim2024etiologicaldistributionof pages 4-7): Hyun‐Jae Kim, Hyo‐Jung Kim, Jeong‐Yoon Choi, Hee Kyung Yang, Jeong‐Min Hwang, and Ji‐Soo Kim. Etiological distribution of isolated oculomotor nerve palsy: analysis of 633 patients and literature review. European Journal of Neurology, Feb 2024. URL: https://doi.org/10.1111/ene.16261, doi:10.1111/ene.16261. This article has 18 citations and is from a domain leading peer-reviewed journal.

2. (kim2024etiologicaldistributionof pages 3-4): Hyun‐Jae Kim, Hyo‐Jung Kim, Jeong‐Yoon Choi, Hee Kyung Yang, Jeong‐Min Hwang, and Ji‐Soo Kim. Etiological distribution of isolated oculomotor nerve palsy: analysis of 633 patients and literature review. European Journal of Neurology, Feb 2024. URL: https://doi.org/10.1111/ene.16261, doi:10.1111/ene.16261. This article has 18 citations and is from a domain leading peer-reviewed journal.

3. (kim2024etiologicaldistributionof pages 2-3): Hyun‐Jae Kim, Hyo‐Jung Kim, Jeong‐Yoon Choi, Hee Kyung Yang, Jeong‐Min Hwang, and Ji‐Soo Kim. Etiological distribution of isolated oculomotor nerve palsy: analysis of 633 patients and literature review. European Journal of Neurology, Feb 2024. URL: https://doi.org/10.1111/ene.16261, doi:10.1111/ene.16261. This article has 18 citations and is from a domain leading peer-reviewed journal.

4. (fritzsch2023evolutionanddevelopment pages 16-18): Bernd Fritzsch. Evolution and development of extra-ocular nerves and muscles in vertebrates. Unknown journal, Jun 2023. URL: https://doi.org/10.20944/preprints202306.0416.v1, doi:10.20944/preprints202306.0416.v1.

5. (puri2023tubb3andkif21a pages 1-2): Dharmendra Puri, Brenda J. Barry, and Elizabeth C. Engle. Tubb3 and kif21a in neurodevelopment and disease. Frontiers in Neuroscience, Aug 2023. URL: https://doi.org/10.3389/fnins.2023.1226181, doi:10.3389/fnins.2023.1226181. This article has 43 citations and is from a peer-reviewed journal.

6. (jurgens2021novelvariantsin pages 1-2): Julie A. Jurgens, Brenda J. Barry, Gabrielle Lemire, Wai-Man Chan, Mary C. Whitman, Sherin Shaaban, Caroline D. Robson, Sarah MacKinnon, Eleina M. England, Hugh J. McMillan, Christopher Kelly, Brandon M. Pratt, Anne O’Donnell-Luria, Daniel G. MacArthur, Kym M. Boycott, David G. Hunter, and Elizabeth C. Engle. Novel variants in tuba1a cause congenital fibrosis of the extraocular muscles with or without malformations of cortical brain development. European Journal of Human Genetics, 29:816-826, Mar 2021. URL: https://doi.org/10.1038/s41431-020-00804-7, doi:10.1038/s41431-020-00804-7. This article has 32 citations and is from a domain leading peer-reviewed journal.

7. (kim2024etiologicaldistributionof pages 1-2): Hyun‐Jae Kim, Hyo‐Jung Kim, Jeong‐Yoon Choi, Hee Kyung Yang, Jeong‐Min Hwang, and Ji‐Soo Kim. Etiological distribution of isolated oculomotor nerve palsy: analysis of 633 patients and literature review. European Journal of Neurology, Feb 2024. URL: https://doi.org/10.1111/ene.16261, doi:10.1111/ene.16261. This article has 18 citations and is from a domain leading peer-reviewed journal.

8. (srimanan2024retrospectiveanalysisof pages 2-4): Worapot Srimanan and Somboon Panyakorn. Retrospective analysis of factors related to the long-term recovery of third, fourth, and sixth cranial nerve palsy with etiologies and clinical course in a tertiary hospital. Clinical Ophthalmology (Auckland, N.Z.), 18:441-450, Feb 2024. URL: https://doi.org/10.2147/opth.s449127, doi:10.2147/opth.s449127. This article has 12 citations.

9. (srimanan2024retrospectiveanalysisof pages 6-7): Worapot Srimanan and Somboon Panyakorn. Retrospective analysis of factors related to the long-term recovery of third, fourth, and sixth cranial nerve palsy with etiologies and clinical course in a tertiary hospital. Clinical Ophthalmology (Auckland, N.Z.), 18:441-450, Feb 2024. URL: https://doi.org/10.2147/opth.s449127, doi:10.2147/opth.s449127. This article has 12 citations.

10. (jia2022clinicalandgenetic pages 1-2): Hongyan Jia, Qian Ma, Yi Liang, Dan Wang, Qinglin Chang, Bo Zhao, Zongrui Zhang, Jing Liang, Jing Song, Yidi Wang, Ranran Zhang, Zhanhan Tu, and Yonghong Jiao. Clinical and genetic characteristics of chinese patients with congenital cranial dysinnervation disorders. Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02582-5, doi:10.1186/s13023-022-02582-5. This article has 12 citations and is from a peer-reviewed journal.

11. (jia2022clinicalandgenetic pages 7-8): Hongyan Jia, Qian Ma, Yi Liang, Dan Wang, Qinglin Chang, Bo Zhao, Zongrui Zhang, Jing Liang, Jing Song, Yidi Wang, Ranran Zhang, Zhanhan Tu, and Yonghong Jiao. Clinical and genetic characteristics of chinese patients with congenital cranial dysinnervation disorders. Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02582-5, doi:10.1186/s13023-022-02582-5. This article has 12 citations and is from a peer-reviewed journal.

12. (jia2022clinicalandgenetic pages 12-13): Hongyan Jia, Qian Ma, Yi Liang, Dan Wang, Qinglin Chang, Bo Zhao, Zongrui Zhang, Jing Liang, Jing Song, Yidi Wang, Ranran Zhang, Zhanhan Tu, and Yonghong Jiao. Clinical and genetic characteristics of chinese patients with congenital cranial dysinnervation disorders. Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02582-5, doi:10.1186/s13023-022-02582-5. This article has 12 citations and is from a peer-reviewed journal.

13. (jia2022clinicalandgenetic pages 13-14): Hongyan Jia, Qian Ma, Yi Liang, Dan Wang, Qinglin Chang, Bo Zhao, Zongrui Zhang, Jing Liang, Jing Song, Yidi Wang, Ranran Zhang, Zhanhan Tu, and Yonghong Jiao. Clinical and genetic characteristics of chinese patients with congenital cranial dysinnervation disorders. Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02582-5, doi:10.1186/s13023-022-02582-5. This article has 12 citations and is from a peer-reviewed journal.

14. (puri2023tubb3andkif21a pages 2-3): Dharmendra Puri, Brenda J. Barry, and Elizabeth C. Engle. Tubb3 and kif21a in neurodevelopment and disease. Frontiers in Neuroscience, Aug 2023. URL: https://doi.org/10.3389/fnins.2023.1226181, doi:10.3389/fnins.2023.1226181. This article has 43 citations and is from a peer-reviewed journal.

15. (puri2023tubb3andkif21a pages 3-5): Dharmendra Puri, Brenda J. Barry, and Elizabeth C. Engle. Tubb3 and kif21a in neurodevelopment and disease. Frontiers in Neuroscience, Aug 2023. URL: https://doi.org/10.3389/fnins.2023.1226181, doi:10.3389/fnins.2023.1226181. This article has 43 citations and is from a peer-reviewed journal.

16. (jurgens2021novelvariantsin pages 9-10): Julie A. Jurgens, Brenda J. Barry, Gabrielle Lemire, Wai-Man Chan, Mary C. Whitman, Sherin Shaaban, Caroline D. Robson, Sarah MacKinnon, Eleina M. England, Hugh J. McMillan, Christopher Kelly, Brandon M. Pratt, Anne O’Donnell-Luria, Daniel G. MacArthur, Kym M. Boycott, David G. Hunter, and Elizabeth C. Engle. Novel variants in tuba1a cause congenital fibrosis of the extraocular muscles with or without malformations of cortical brain development. European Journal of Human Genetics, 29:816-826, Mar 2021. URL: https://doi.org/10.1038/s41431-020-00804-7, doi:10.1038/s41431-020-00804-7. This article has 32 citations and is from a domain leading peer-reviewed journal.

17. (NCT03099447 chunk 1):  Effects of Ocular Electroacupuncture on Oculomotor Nerve Palsy. First Affiliated Hospital of Harbin Medical University. 2017. ClinicalTrials.gov Identifier: NCT03099447

18. (NCT03099447 chunk 2):  Effects of Ocular Electroacupuncture on Oculomotor Nerve Palsy. First Affiliated Hospital of Harbin Medical University. 2017. ClinicalTrials.gov Identifier: NCT03099447

19. (NCT03461809 chunk 1):  A Retrospective Study of the Effects of Ocular Acupuncture on Ocular Motor Nerve Palsy. First Affiliated Hospital of Harbin Medical University. 2018. ClinicalTrials.gov Identifier: NCT03461809

20. (NCT03059420 chunk 1): Elizabeth Engle. Genetic Studies of Strabismus, Congenital Cranial Dysinnervation Disorders (CCDDs), and Their Associated Anomalies. Boston Children's Hospital. 2004. ClinicalTrials.gov Identifier: NCT03059420

21. (NCT03059420 chunk 2): Elizabeth Engle. Genetic Studies of Strabismus, Congenital Cranial Dysinnervation Disorders (CCDDs), and Their Associated Anomalies. Boston Children's Hospital. 2004. ClinicalTrials.gov Identifier: NCT03059420

22. (OpenTargets Search: oculomotor nerve palsy): Open Targets Query (oculomotor nerve palsy, 14 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

23. (wagstaff2021failuresofnerve pages 1-2): Laura J Wagstaff, Jose A Gomez-Sanchez, Shaline V Fazal, Georg W Otto, Alastair M Kilpatrick, Kirolos Michael, Liam YN Wong, Ki H Ma, Mark Turmaine, John Svaren, Tessa Gordon, Peter Arthur-Farraj, Sergio Velasco-Aviles, Hugo Cabedo, Cristina Benito, Rhona Mirsky, and Kristjan R Jessen. Failures of nerve regeneration caused by aging or chronic denervation are rescued by restoring schwann cell c-jun. Jan 2021. URL: https://doi.org/10.7554/elife.62232, doi:10.7554/elife.62232. This article has 142 citations and is from a domain leading peer-reviewed journal.

24. (ge2025oculomotornervepalsy pages 2-3): Yuanhong Ge, Qingjia Lai, Yunsen Zhang, Yao Wang, and Xuejun Xu. Oculomotor nerve palsy secondary to posterior communicating artery aneurysm: a narrative review and proposed treatment algorithm. Revista de Neurología, Nov 2025. URL: https://doi.org/10.31083/rn40930, doi:10.31083/rn40930. This article has 2 citations.

25. (arthurfarraj2021lessonsfrominjury pages 1-2): Peter Arthur-Farraj and Michael P. Coleman. Lessons from injury: how nerve injury studies reveal basic biological mechanisms and therapeutic opportunities for peripheral nerve diseases. Neurotherapeutics, 18:2200-2221, Oct 2021. URL: https://doi.org/10.1007/s13311-021-01125-3, doi:10.1007/s13311-021-01125-3. This article has 69 citations and is from a peer-reviewed journal.

26. (jessen2019thesuccessand pages 1-2): Kristjan R. Jessen and Rhona Mirsky. The success and failure of the schwann cell response to nerve injury. Frontiers in Cellular Neuroscience, Feb 2019. URL: https://doi.org/10.3389/fncel.2019.00033, doi:10.3389/fncel.2019.00033. This article has 577 citations.

## Artifacts

- [Edison artifact artifact-00](Oculomotor_Nerve_Palsy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.