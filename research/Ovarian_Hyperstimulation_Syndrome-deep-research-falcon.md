---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-25T18:28:46.863045'
end_time: '2026-08-25T18:39:46.340524'
duration_seconds: 659.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ovarian Hyperstimulation Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 3
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Ovarian_Hyperstimulation_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ovarian Hyperstimulation Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Ovarian Hyperstimulation Syndrome** covering all of the
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
- **Disease Name:** Ovarian Hyperstimulation Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Ovarian Hyperstimulation Syndrome** covering all of the
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


# Ovarian Hyperstimulation Syndrome: Disease-Characteristics Report

**Evidence cut-off:** the search prioritized 2023–2024 publications, supplemented by earlier primary and systematic evidence where necessary. Evidence is labeled as human clinical, in vitro, animal-model, registry, or database evidence. OHSS-specific advanced-omics and quality-of-life literature remains sparse.

The table below summarizes the principal evidence suitable for knowledge-base ingestion.

| Domain | Current finding | Quantitative evidence | Evidence type/source year | Knowledge-base annotations |
|---|---|---|---|---|
| Identifiers | Ovarian hyperstimulation syndrome (OHSS) is a primarily iatrogenic complication of controlled ovarian stimulation/ART; rare spontaneous forms also occur. MONDO identifier available. | MONDO:0011972; MeSH: D016471 (OpenTargets Search: ovarian hyperstimulation syndrome-FSHR,VEGFA,KDR,LHCGR, mares2024ovarianhyperstimulationsyndrome pages 1-2, NCT06333691 chunk 1) | Database association + clinical review, 2024 | MONDO:0011972; MeSH:D016471; category: complex/iatrogenic ovarian disorder |
| Epidemiology | Current incidence in modern IVF practice is low but not eliminated, with early and late forms recognized. | Danish cohort: 1.2% annual incidence across 186,168 cycles; Chinese study: 1.14% mean annual incidence across 1,581,703 cycles; Australian prospective antagonist-cycle cohort: 2.1% overall, 1.2% early, 0.9% late OHSS (mares2024ovarianhyperstimulationsyndrome pages 1-2) | Human cohort/review, 2024 | ICD/phenotype note: early OHSS vs late OHSS; adult female reproductive-age population |
| Main trigger and VEGF mechanism | Final oocyte maturation exposure to exogenous hCG, or endogenous hCG from pregnancy, drives luteinized granulosa-cell VEGF production; VEGF/VEGFR2-mediated vascular hyperpermeability causes third-spacing, hemoconcentration, oliguria, pleural effusion, and thrombosis risk. | Moderate-severe OHSS reported in 3-8% in older mechanistic literature; severe OHSS 0.1-3% in some IVF series; VEGF elevated in OHSS granulosa cells and follicular fluid (sun2022tie1contributesto pages 1-2, sun2022tie1contributesto pages 2-3) | Human clinical + in vitro + animal model, 2022; review 2024 | Genes: VEGFA, KDR, FSHR, LHCGR; GO:0001525 angiogenesis, GO:0001568 blood vessel development, GO:0043114 regulation of vascular permeability; CL: granulosa cell, endothelial cell |
| Major risk factors | Consistently supported risk factors are PCOS/high ovarian reserve, young age, high AMH, high estradiol on trigger day, high follicle count, and high oocyte yield; prior OHSS also used clinically. | High-risk thresholds used in trials/reviews include AMH >3.4 ng/mL, peak E2 >3500 pg/mL, >25 follicles, >24 oocytes; trial eligibility often used E2 >3000-4000 pg/mL or >20 follicles/oocytes (wu2022comparisonofthe pages 1-2, salama2017sequentiale2levels pages 1-2, NCT06333691 chunk 1, NCT04351126 chunk 1, NCT02620605 chunk 1) | Human meta-analysis/trial protocols, 2022-2024 | HPO suggestions: Polycystic ovary morphology, elevated anti-Müllerian hormone, hyperestrogenemia; risk annotation: prior OHSS, PCOS |
| Hallmark phenotypes | Hallmarks are ovarian enlargement, abdominal distension/pain, ascites, nausea/vomiting, dyspnea/pleural effusion, oliguria, hemoconcentration, electrolyte disturbance, and thromboembolism in severe disease. | Severe criteria examples include Hct >45%, WBC >15,000/mm3, ovaries >100 mm, moderate-or-higher ascites; elevated AST/ALT occurs in ~30% of severe cases (mares2024ovarianhyperstimulationsyndrome pages 3-5, NCT02392520 chunk 1) | Human review + trial criteria, 2024/2015 registry text | HPO: Ascites, Pleural effusion, Abdominal distension, Oliguria, Hemoconcentration, Dyspnea, Enlarged ovary; imaging: transvaginal ultrasound |
| Prevention (standard/current) | Standard prevention centers on identifying high-risk patients, using GnRH antagonist stimulation, minimizing hCG exposure, GnRH agonist trigger where appropriate, individualized gonadotropin dosing, and freeze-all/cryopreservation strategies in high responders. | Antagonist-based prospective cohort incidence 2.1%; individualized follitropin-d in PCOS study: moderate OHSS 0% vs 5.9% and severe 0% vs 17.6% versus standard dosing (mares2024ovarianhyperstimulationsyndrome pages 1-2, salama2017sequentiale2levels pages 1-2) | Human review 2024 + case-control study 2024 | NCIT/management concepts: risk-adapted ovarian stimulation, embryo cryopreservation; ontology hints: CHEBI gonadotropins, GnRH agonists/antagonists |
| Prevention (drug evidence, adjunctive) | Among pharmacologic adjuncts, calcium, cabergoline, HES, and metformin have the strongest evidence; albumin is not favored because of limited benefit and possible pregnancy-rate reduction. | Network meta-analysis: calcium RR 0.14 (95% CI 0.04-0.46), HES RR 0.25 (0.07-0.73), cabergoline RR 0.43 (0.24-0.71); earlier network meta-analysis: aspirin RR 0.07, IV calcium RR 0.11, cabergoline RR 0.17, metformin RR 0.20, HES RR 0.26; albumin pregnancy RR 0.85 vs placebo (wu2022comparisonofthe pages 1-2, guo2016pharmacologicinterventionsin pages 1-2, guo2016pharmacologicinterventionsin pages 7-9) | RCT network meta-analyses, 2016/2022 | CHEBI/Drug terms: cabergoline, calcium gluconate, hydroxyethyl starch, metformin, aspirin; note: adjunct prophylaxis |
| Established management | Mild-moderate OHSS is generally managed conservatively with monitoring, fluid/electrolyte management, urine output assessment, and thrombosis risk assessment; severe disease may require hospitalization, paracentesis, albumin, and ICU-level support. | Review notes severe complications include renal impairment, respiratory distress, thromboembolism; severe early OHSS trial criteria used regression over 2-21 days and monitored Hct, WBC, ovary size, ascites, E2, progesterone, VEGF (mares2024ovarianhyperstimulationsyndrome pages 3-5, NCT02392520 chunk 1) | Clinical review 2024 + interventional protocol | NCIT suggestions: Paracentesis, Albumin administration, Intensive care unit care, Thromboprophylaxis; HPO: Acute kidney injury/oliguria, hydrothorax |
| Experimental trials | Active/recent interventional research includes calcium+diosmin vs cabergoline regimens, fludrocortisone for presumed mineralocorticoid deficiency physiology, early cabergoline timing, letrozole prophylaxis, montelukast, and luteal-phase cetrorelix for established severe early OHSS. These remain experimental/non-standard. | NCT06333691 (completed, n=180); NCT04351126 (completed, n=107); NCT03996434 (completed, n=300); NCT02670304 (completed, n=100); NCT03794037 (suspended, n=20); NCT02392520 (planned n=40) (NCT06333691 chunk 1, NCT04351126 chunk 1, NCT03996434 chunk 1, NCT03794037 chunk 1, NCT02670304 chunk 1, NCT02392520 chunk 1) | ClinicalTrials.gov records, 2015-2025 updates | Trial annotations: prevention vs treatment; drug terms: diosmin, fludrocortisone, letrozole, montelukast, cetrorelix |
| Genetics/model evidence | Genetic susceptibility is supported but incompletely standardized clinically. FSHR mutations are linked to spontaneous OHSS; common FSHR/LHCGR polymorphisms influence ovarian response and may modify OHSS risk. Functional human-cell/rat evidence supports an EGR1-TIE1-PI3K-AKT axis upstream of VEGF in granulosa cells. | Open Targets disease-target evidence: FSHR (5 literature links), VEGFA (5), LHCGR (3), KDR (1); TIE1 knockdown attenuated OHSS progression in rat models and abolished hCG-induced VEGF in SVOG cells (OpenTargets Search: ovarian hyperstimulation syndrome-FSHR,VEGFA,KDR,LHCGR, sun2022tie1contributesto pages 1-2, sun2022tie1contributesto pages 2-3, sun2022tie1contributesto pages 7-9, alviggi2018clinicalrelevanceof pages 15-16) | Database + systematic review + in vitro/animal study, 2018-2022 | Genes: FSHR, LHCGR, VEGFA, KDR, TIE1, EGR1; GO:0030335 positive regulation of cell migration/vascular remodeling context, GO:0001933 negative regulation of protein phosphorylation not established clinically; CL: granulosa-lutein cell; model: induced rat OHSS |
| Outcomes/prognosis | Most cases resolve with supportive care, but severe OHSS can be life-threatening. In recent small 2023 case-series data, pregnancy was often achieved but preterm birth was common; evidence remains limited. | 15-patient case series: 73.3% achieved pregnancy; preterm delivery 33.3% at 32-37 weeks, 33.3% at 28-32 weeks, 6.7% before 28 weeks; 73.3% severe OHSS (alfaraj2023pregnancyoutcomesof pages 1-2, alfaraj2023pregnancyoutcomesof pages 7-8) | Human case series, 2023 | Outcome annotations: hospitalization, preterm birth, pregnancy continuation; evidence level: limited/small single-center |


*Table: This table condenses the strongest gathered evidence on ovarian hyperstimulation syndrome across identifiers, epidemiology, mechanism, risk, phenotypes, prevention, management, trials, and genetics/models. It is designed to support rapid knowledge-base population while distinguishing established care from experimental approaches.*

## 1. Disease information

### Definition and scope

Ovarian hyperstimulation syndrome (OHSS) is an acute, predominantly **iatrogenic systemic complication of controlled ovarian stimulation** used in assisted reproductive technology (ART). It combines enlarged, multicystic ovaries with increased vascular permeability, intravascular volume depletion, and fluid accumulation in third spaces. Ascites is characteristic; pleural and occasionally pericardial effusions occur in severe disease. Rare **spontaneous OHSS** occurs without exogenous gonadotropin stimulation, usually during pregnancy in association with abnormal gonadotropin-receptor activation, very high hCG, or hypothyroidism. A concise 2024 definition describes OHSS as “a systemic condition marked by the enlargement of the ovaries and heightened vascular permeability.” (mares2024ovarianhyperstimulationsyndrome pages 2-3, mares2024ovarianhyperstimulationsyndrome pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0011972.
- **MeSH:** D016471, *Ovarian Hyperstimulation Syndrome*.
- **Common names:** ovarian hyperstimulation syndrome; OHSS; ovarian hyperstimulation syndrome following ovulation induction; spontaneous ovarian hyperstimulation syndrome, when no ovarian-stimulation drugs were used.
- **OMIM/Orphanet:** OHSS is not generally represented as a classical Mendelian disorder with a dedicated OMIM phenotype. Rare FSHR-related spontaneous OHSS is better represented through the causal gene/variant and clinical phenotype than as a uniform Mendelian disease.
- **ICD:** coding varies by jurisdiction and version; an exact ICD-10/ICD-11 code was not verified in the retrieved primary sources and should be validated directly against the target release before database ingestion.

Open Targets associates MONDO:0011972 most strongly with **FSHR**, followed by **VEGFA, BRD2, KDR, LHCGR,** and **LHB**; these are disease-target associations, not proof that each gene is monogenic-causal. (OpenTargets Search: ovarian hyperstimulation syndrome-FSHR,VEGFA,KDR,LHCGR)

The present report derives from **aggregated disease-level resources, publications, and trial registries**, not individual-level EHR data. The 2023 outcome study is a retrospective 15-patient case series and is explicitly identified where used. (alfaraj2023pregnancyoutcomesof pages 1-2)

## 2. Etiology, risk factors, and protective factors

### Primary causal factors

The usual initiating sequence is:

1. Exogenous FSH/gonadotropin stimulation recruits many follicles.
2. Exogenous hCG used for final oocyte maturation—or endogenous hCG after implantation—activates luteinized follicles.
3. Luteinized granulosa cells produce excessive VEGF and other vasoactive mediators.
4. Endothelial barrier permeability rises, producing third-spacing and systemic complications. (mares2024ovarianhyperstimulationsyndrome pages 2-3, mares2024ovarianhyperstimulationsyndrome pages 1-2)

Thus, OHSS is generally **treatment-triggered and mechanistically complex**, rather than infectious, toxic, or a single-gene disease.

### Clinical risk factors

Consistently reported factors are:

- PCOS or polycystic ovarian morphology;
- young reproductive age, often under 30–35 years;
- high antral follicle count and high ovarian reserve;
- elevated AMH;
- rapidly rising or high estradiol;
- numerous developing follicles and high oocyte yield;
- previous OHSS;
- hCG exposure and establishment of pregnancy, particularly multiple gestation;
- low BMI in some cohorts, although BMI is less consistent than ovarian-reserve markers. (mares2024ovarianhyperstimulationsyndrome pages 2-3, mares2024ovarianhyperstimulationsyndrome pages 1-2, NCT06333691 chunk 1)

Frequently used high-risk thresholds include **AMH >3.4 ng/mL, peak estradiol >3,500 pg/mL, >25 follicles, or >24 oocytes**. Trials have also used E2 >3,000–4,000 pg/mL and >20 follicles or retrieved oocytes. These are risk-stratification thresholds, not universal diagnostic criteria. (NCT06333691 chunk 1, NCT04351126 chunk 1, wu2022comparisonofthe pages 1-2)

Rare non-ART triggers include pregnancy-associated spontaneous disease, severe hypothyroidism, very high endogenous hCG, and functioning gonadotroph adenoma. A 2023 systematic review identified five reported patients who developed OHSS after long-acting GnRH agonist administration 3–5 days after controlled stimulation for fertility preservation; all recovered conservatively, but causality remains uncertain.

### Genetic susceptibility and gene–environment interaction

Rare activating or sensitizing **FSHR** variants can permit hCG or TSH to activate FSHR, explaining spontaneous gestational OHSS. Common FSHR variants—including the linked codon 307/680 polymorphisms and Ser680Asn—and **LHCGR rs4073366** have been associated with ovarian-response variability or OHSS susceptibility, but their predictive value is insufficient for routine clinical genotyping. (sun2022tie1contributesto pages 1-2, alviggi2018clinicalrelevanceof pages 15-16)

The principal gene–environment interaction is therefore **receptor sensitivity × hormonal exposure**: an FSHR/LHCGR genotype may alter response to administered FSH and hCG or to pregnancy-associated hCG. PCOS/high ovarian reserve supplies a highly responsive follicle pool, while the stimulation regimen supplies the environmental/pharmacological trigger.

### Protective factors

Protective clinical strategies include individualized lower gonadotropin exposure, GnRH-antagonist stimulation, GnRH-agonist rather than hCG trigger where appropriate, avoiding unnecessary hCG luteal support, and freeze-all embryo cryopreservation in high responders. These are preventive interventions rather than intrinsic environmental factors. No validated protective allele, diet, exercise regimen, or occupational/environmental exposure has been established specifically for OHSS. (mares2024ovarianhyperstimulationsyndrome pages 1-2, wu2022comparisonofthe pages 1-2)

## 3. Phenotypes

OHSS occurs in reproductive-age adults after stimulation or during pregnancy. Severity is variable and the course is acute/episodic rather than lifelong.

- **Ovarian enlargement/multicystic ovaries:** bilateral in typical stimulation-associated disease; ultrasound may show ovaries 5–12 cm or larger. Suggested HPO: **Enlarged ovary**, **Ovarian cyst**.
- **Abdominal distension, discomfort, or severe pain:** very common across symptomatic grades; impairs mobility, sleep, eating, and work. Suggested HPO: **Abdominal distension**, **Abdominal pain**.
- **Nausea, vomiting, diarrhea:** mild-to-severe gastrointestinal symptoms. Suggested HPO: **Nausea**, **Vomiting**, **Diarrhea**.
- **Ascites:** ultrasound-only in moderate disease; clinically tense or massive in severe disease. Suggested HPO: **Ascites**.
- **Rapid weight gain/peripheral edema:** reflects fluid redistribution. Suggested HPO: **Abnormal weight gain**, **Peripheral edema**, **Anasarca**.
- **Dyspnea, pleural effusion, hypoxemia:** severe respiratory involvement. Suggested HPO: **Dyspnea**, **Pleural effusion**, **Hypoxemia**.
- **Oliguria/acute kidney injury:** caused primarily by reduced effective circulating volume and renal perfusion. Suggested HPO: **Oliguria**, **Acute kidney injury**.
- **Hemoconcentration and leukocytosis:** severe criteria commonly include hematocrit >45% and WBC >15,000/mm³. Suggested HPO: **Hemoconcentration**, **Leukocytosis**.
- **Electrolyte/acid-base abnormalities:** dilutional hyponatremia, hyperkalemia, and metabolic acidosis may occur. Suggested HPO: **Hyponatremia**, **Hyperkalemia**, **Metabolic acidosis**.
- **Hepatic dysfunction:** AST/ALT elevation occurs in approximately 30% of severe cases in the reviewed literature. Suggested HPO: **Elevated hepatic transaminase**.
- **Thrombosis:** deep venous thrombosis, pulmonary embolism, and unusual-site thromboses can occur. Suggested HPO: **Venous thrombosis**, **Pulmonary embolism**.
- **Neurologic/critical manifestations:** altered mental status, cerebral edema, respiratory failure, abdominal compartment syndrome, or multiorgan failure are rare. (mares2024ovarianhyperstimulationsyndrome pages 3-5, alfaraj2023pregnancyoutcomesof pages 2-3)

Formal per-phenotype frequencies are poorly standardized because studies use different classifications and preventive protocols. Disease-specific EQ-5D, SF-36, or PROMIS estimates were not identified. Nevertheless, pain, distension, vomiting, dyspnea, repeated monitoring, hospitalization, invasive drainage, and treatment-cycle interruption plausibly produce substantial short-term quality-of-life burden.

## 4. Genetic and molecular information

### Causal and susceptibility genes

**FSHR** is the best-supported causal gene in rare spontaneous OHSS. Reported mechanisms generally involve germline gain of abnormal sensitivity to hCG or TSH. OHSS is not routinely caused by FSHR loss of function. Exact HGVS variants, ClinVar classifications, and population frequencies were not recoverable from the retrieved full texts; they should be curated case-by-case from the original reports before a pathogenic-variant table is populated.

**LHCGR** variants may modify controlled-stimulation response. **VEGFA/KDR, TIE1, EGR1, LHB,** and possibly **BRD2** are mechanistic or association targets, not established high-penetrance causal genes for ordinary iatrogenic OHSS. Open Targets lists literature-backed associations for FSHR (five evidence records), VEGFA (five), LHCGR (three), KDR (one), LHB (two), and BRD2 (three). (OpenTargets Search: ovarian hyperstimulation syndrome-FSHR,VEGFA,KDR,LHCGR)

### Functional consequences

- FSHR sensitizing variants: receptor gain of inappropriate responsiveness to hCG/TSH.
- hCG–LHCGR signaling: induces luteinization and vasoactive-factor production.
- VEGFA–KDR/VEGFR2: increases endothelial permeability.
- EGR1–TIE1–PI3K–AKT: experimentally increases granulosa-cell VEGF; TIE1 knockdown attenuated induced OHSS in rats. (sun2022tie1contributesto pages 1-2, sun2022tie1contributesto pages 7-9)

No recurrent pathogenic chromosomal abnormality, somatic driver, founder mutation, anticipation, germline mosaicism pattern, or established carrier frequency defines OHSS. Routine ACMG-style interpretation is relevant only when evaluating a rare suspected spontaneous FSHR-mediated case.

### Pharmacogenomics, modifiers, and epigenetics

A 2018 meta-analysis found that gonadotropin/receptor genotypes affect ovarian-response measures, supporting pharmacogenomic plausibility, but concluded that further study was required before clinical implementation. No CPIC/PharmGKB-style prescribing guideline for OHSS prevention was identified. (alviggi2018clinicalrelevanceof pages 15-16)

OHSS-specific causal DNA-methylation, histone, chromatin, or validated epigenetic biomarker evidence was not established in the retrieved literature.

## 5. Environmental and lifestyle information

The dominant non-genetic exposure is **medical gonadotropin treatment**, especially hCG exposure in a high responder. No convincing evidence identifies pollution, radiation, occupational agents, smoking, alcohol, diet, or exercise as direct OHSS causes. Lifestyle modification can improve broader PCOS and fertility-treatment health but is not an acute OHSS treatment. No bacterial, viral, fungal, or parasitic trigger is recognized.

## 6. Mechanism and pathophysiology

### Integrated causal chain

**Upstream trigger:** multifollicular development followed by hCG/LHCGR signaling in luteinized granulosa cells.

**Intermediate ovarian signaling:** increased VEGFA, angiopoietin/TIE signaling, EGR1/TIE1/PI3K–AKT activation, and contribution from IL-6, IL-8, platelet-activating factor, and ovarian renin–angiotensin-system components.

**Endothelial effect:** VEGF activates KDR/VEGFR2 on endothelial cells, loosening intercellular junctions and increasing transendothelial transport.

**Systemic physiology:** protein-rich fluid leaves the vascular compartment and accumulates in peritoneal, pleural, and occasionally pericardial spaces. Effective hypovolemia produces RAAS activation, tachycardia, oliguria, renal injury, and electrolyte abnormalities. Hemoconcentration, thrombocytosis, elevated fibrinogen, immobility, and pregnancy produce a prothrombotic state.

**Clinical manifestations:** enlarged painful ovaries, ascites and distension; intestinal edema, nausea, ileus; pleural effusion and dyspnea; renal and hepatic dysfunction; thrombosis and, rarely, multiorgan failure. (mares2024ovarianhyperstimulationsyndrome pages 2-3, mares2024ovarianhyperstimulationsyndrome pages 3-5)

The strongest recent functional study found elevated TIE1 and VEGF in granulosa cells from patients and induced-OHSS rats. hCG induced TIE1 through PI3K/AKT; EGR1 bound the TIE1 promoter; TIE1 silencing abolished hCG-induced VEGF in SVOG cells and reduced ovarian weight, corpora lutea, and VEGF in rats. The abstract states: “Tie1 silencing abolished the hCG-induced VEGF level in SVOG cells and attenuated the progression of OHSS in rats.” This is compelling mechanistic evidence but not yet a validated human therapy. (sun2022tie1contributesto pages 1-2, sun2022tie1contributesto pages 2-3, sun2022tie1contributesto pages 7-9)

### Ontology suggestions

- **GO biological processes:** response to gonadotropin; ovarian follicle development; angiogenesis (GO:0001525); blood-vessel development (GO:0001568); regulation of vascular permeability (GO:0043114); PI3K signaling; inflammatory response; coagulation; fluid homeostasis.
- **Cell Ontology:** ovarian granulosa cell; granulosa-lutein cell; vascular endothelial cell; luteal cell.
- **Proteins/genes:** LHCGR, FSHR, VEGFA, KDR, TIE1, EGR1.

### Molecular profiling and advanced technologies

Targeted expression and protein assays support VEGF/TIE1/EGR1 dysregulation. However, no sufficiently replicated OHSS-specific diagnostic transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omics signature was identified. These should be recorded as **research gaps**, not negative findings.

## 7. Anatomical structures affected

- **Primary organ:** ovaries—typically bilateral, especially after controlled stimulation. UBERON suggestion: **ovary (UBERON:0000992)**.
- **Primary tissue/cells:** ovarian follicles, granulosa and granulosa-lutein cells, corpora lutea, ovarian vasculature.
- **Secondary compartments:** peritoneal cavity/ascitic space; pleural cavity; rarely pericardial cavity.
- **Secondary organs:** kidneys, lungs, liver, bowel, and venous circulation through hypovolemia, edema, congestion, and thrombosis.
- **Systems:** reproductive/endocrine, vascular, renal, respiratory, gastrointestinal, hepatic, and hematologic.
- **Subcellular/signaling localization:** plasma-membrane receptors FSHR, LHCGR, VEGFR2/KDR and TIE1; cytoplasmic PI3K–AKT signaling; nuclear EGR1-mediated transcription. Suggested GO cellular components: plasma membrane, receptor complex, cytoplasm, nucleus, cell–cell junction.

## 8. Temporal development

OHSS is adult-onset and acute. **Early OHSS** generally begins within nine days after oocyte retrieval/hCG trigger and is driven primarily by exogenous hCG. **Late OHSS** begins around day 10 or later and is driven or prolonged by endogenous pregnancy hCG. The Australian cohort reported 1.2% early and 0.9% late OHSS. (mares2024ovarianhyperstimulationsyndrome pages 1-2, NCT02620605 chunk 1)

The syndrome progresses over days from abdominal symptoms and ovarian enlargement to ascites and systemic abnormalities. Without pregnancy, it is usually self-limited as luteal activity declines. Pregnancy can prolong or exacerbate disease. Clinical-trial outcome windows assess regression over approximately 2–21 days, although critical disease may require longer hospitalization. (NCT02392520 chunk 1)

The critical intervention window is **before hCG trigger**, when ovarian response is apparent and trigger choice, dose modification, coasting, or freeze-all can still prevent severe disease.

## 9. Inheritance and population epidemiology

Modern estimates are cycle-based rather than population prevalence estimates:

- Danish cohort: **1.2% annual incidence**, 186,168 cycles.
- Chinese nationwide cohort: **1.14% mean annual incidence**, 1,581,703 cycles, with a declining trend.
- Australian prospective antagonist-protocol cohort: **2.1% overall**, including 1.2% early and 0.9% late OHSS.
- Older systematic evidence reported moderate OHSS in approximately 3–6% and severe OHSS in 0.2–1% of cycles; registry protocols cite severe rates up to 0.1–3%, reflecting heterogeneous eras and definitions. (guo2016pharmacologicinterventionsin pages 1-2, mares2024ovarianhyperstimulationsyndrome pages 1-2, NCT03996434 chunk 1)

The affected population is almost exclusively females undergoing ovarian stimulation or pregnant females with rare spontaneous disease; a male:female ratio is therefore not meaningful. Geographic variation primarily reflects ART access, patient selection, stimulation practices, reporting, and classification rather than endemic biology.

Ordinary iatrogenic OHSS has **multifactorial susceptibility**, not Mendelian inheritance. Rare FSHR-mediated spontaneous disease is germline and may show dominant functional effects, but penetrance and expressivity depend strongly on pregnancy and hormonal exposure. Founder effects, consanguinity, carrier frequency, and anticipation are not established disease-level characteristics.

## 10. Diagnostics

### Clinical diagnosis and severity

Diagnosis is clinical and is anchored to recent ovarian stimulation or pregnancy, ovarian enlargement, symptoms, ascites, and laboratory evidence of hemoconcentration or organ dysfunction. Golan-type systems grade mild, moderate, and severe disease; Navot-type systems add objective laboratory and respiratory criteria and a critical category. (mares2024ovarianhyperstimulationsyndrome pages 2-3, mares2024ovarianhyperstimulationsyndrome pages 3-5)

Representative criteria include:

- **Mild:** bloating/mild pain, enlarged ovaries.
- **Moderate:** nausea/vomiting and ultrasound ascites.
- **Severe:** massive ascites or hydrothorax, dyspnea, oliguria, Hct >45%, WBC >15,000/mm³, creatinine elevation, hepatic dysfunction, or anasarca.
- **Critical:** thrombosis, respiratory failure, severe renal failure, hemodynamic instability, or multiorgan failure. (mares2024ovarianhyperstimulationsyndrome pages 3-5, NCT02620605 chunk 1)

### Tests

- **Ultrasound:** transvaginal ultrasound for ovarian size/cysts and pelvic ascites; abdominal or thoracic imaging if extensive fluid is suspected.
- **Blood:** CBC/hematocrit, electrolytes, urea/creatinine, liver enzymes, albumin/total protein, coagulation studies where indicated.
- **Monitoring:** weight, abdominal circumference, vital signs, oxygen saturation, fluid balance, and urine output.
- **Pregnancy testing/hCG:** distinguishes pregnancy-associated persistence and informs the early/late phenotype.
- **Biomarkers:** AMH, AFC, estradiol, follicle number, and oocyte yield are useful risk predictors; VEGF is mechanistically important but not a validated routine diagnostic test.

### Differential diagnosis

Exclude ovarian torsion or rupture, ectopic or heterotopic pregnancy, intra-abdominal bleeding, pelvic infection, appendicitis, gastroenteritis, pulmonary embolism, pneumonia, heart/liver/renal disease causing effusions, and ovarian malignancy when the history or course is atypical.

### Genetic and omics testing

Routine genetic testing is **not recommended** for stimulation-associated OHSS. In recurrent or spontaneous OHSS—especially with hypothyroidism, unexpectedly low hCG, or familial recurrence—targeted **FSHR sequencing** or an appropriate receptor-signaling panel may be considered in a specialist/research setting. WES/WGS may help unresolved exceptional cases, but there is no validated diagnostic yield. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing have no routine role. No omics-based clinical diagnostic is validated.

## 11. Outcome and prognosis

Most mild and moderate cases recover completely with monitoring and supportive care. Severe disease can cause hospitalization, invasive drainage, thromboembolism, acute kidney injury, respiratory failure, ovarian torsion, hepatic dysfunction, or critical illness. Mortality is rare in contemporary care, but the retrieved sources did not provide a sufficiently current population mortality estimate. There is no relevant five- or ten-year survival metric because OHSS is an acute syndrome. (mares2024ovarianhyperstimulationsyndrome pages 1-2, mares2024ovarianhyperstimulationsyndrome pages 3-5)

A 2023 single-center case series of 15 women reported pregnancy in 73.3%; 73.3% had severe OHSS. Deliveries were frequently preterm: 33.3% at 32–37 weeks, 33.3% at 28–32 weeks, and 6.7% before 28 weeks. These estimates should not be generalized because of small sample size, severity-enriched selection, and retrospective design. Larger literature is inconsistent concerning miscarriage, hypertensive disorders, gestational diabetes, and fetal growth. (alfaraj2023pregnancyoutcomesof pages 1-2, alfaraj2023pregnancyoutcomesof pages 7-8)

Poor prognostic indicators include rising hematocrit, worsening ascites/pleural effusion, oliguria, creatinine or liver-test deterioration, hypoxemia, thromboembolic symptoms, pregnancy-associated late disease, and inability to maintain oral intake.

## 12. Treatment

### Management algorithm

1. **Mild disease:** outpatient counseling, oral hydration according to thirst, analgesia/antiemetics as appropriate, avoidance of strenuous activity and intercourse because enlarged ovaries are torsion-prone, weight/abdominal girth and urine-output monitoring, and rapid reassessment for deterioration.
2. **Moderate disease:** closer laboratory and ultrasound monitoring; assess thrombosis risk and oral intake.
3. **Severe/critical disease:** hospitalize when clinically indicated; restore effective circulating volume cautiously, correct electrolyte abnormalities, monitor renal/respiratory/hepatic status, provide thromboprophylaxis unless contraindicated, and drain tense symptomatic ascites by ultrasound-guided paracentesis. Pleural drainage or intensive care may be required for respiratory compromise. (mares2024ovarianhyperstimulationsyndrome pages 3-5, NCT02392520 chunk 1)

The goal is supportive stabilization while ovarian vasoactive activity resolves; no drug reliably reverses established OHSS immediately.

### Pharmacologic and procedural interventions

- **Cabergoline:** dopamine agonist that inhibits VEGFR2 phosphorylation; best supported as prophylaxis in high-risk cycles rather than rescue treatment.
- **Metformin:** may lower OHSS risk in PCOS, particularly in agonist protocols; it is not a universal OHSS drug.
- **GnRH antagonist/cetrorelix:** luteal re-initiation for established early disease is promising but not universally standard. A 48-woman randomized study used cetrorelix 0.25 mg/day for three days after retrieval with embryo freezing; sequential E2 tracked response better than ovarian diameter. NCT02823080. (salama2017sequentiale2levels pages 1-2)
- **Paracentesis:** relieves tense ascites, dyspnea, pain, and renal compromise; suggested NCIT concept: *Paracentesis*.
- **Albumin:** may be used selectively for intravascular support in established severe disease, but routine prophylactic albumin is not supported and may reduce pregnancy rate.
- **Anticoagulation:** risk-based prophylaxis for severe OHSS, hospitalization, immobility, or pregnancy; drug and duration should follow local obstetric/hematology guidance.

Suggested NCIT intervention concepts include ovarian-stimulation protocol modification, embryo cryopreservation, cabergoline therapy, intravenous-fluid therapy, paracentesis, thromboprophylaxis, hospitalization, and intensive-care treatment.

### Preventive-drug efficacy

A 2022 network meta-analysis found reductions in moderate-to-severe OHSS with calcium (**RR 0.14, 95% CI 0.04–0.46**), hydroxyethyl starch (**RR 0.25, 0.07–0.73**), and cabergoline (**RR 0.43, 0.24–0.71**), without detected effects on pregnancy, miscarriage, or live birth; calcium ranked highest by SUCRA at 92.4%. An earlier 31-RCT/7,181-participant network analysis also reported benefit for aspirin, calcium, cabergoline, metformin, and HES, while prophylactic albumin reduced pregnancy rate (**RR 0.85, 0.74–0.97**). HES safety concerns in other clinical contexts and heterogeneity among older trials mean these rankings should not supersede contemporary reproductive-society protocols. (wu2022comparisonofthe pages 1-2, guo2016pharmacologicinterventionsin pages 1-2, guo2016pharmacologicinterventionsin pages 7-9)

### Experimental clinical research

- **NCT06333691:** completed randomized prevention study, 180 high-risk women; calcium gluconate+diosmin, cabergoline, and cabergoline+diosmin. Registry posted March 27, 2024; a derived 2025 publication is listed. (NCT06333691 chunk 1)
- **NCT04351126:** completed phase 2, 107 participants; fludrocortisone added to conventional therapy or used prophylactically under a “defective mineralocorticoid response” hypothesis. This is not established care. (NCT04351126 chunk 1)
- **NCT03996434:** completed phase 4, 300 participants; coasting versus cetrorelix in high-risk women. (NCT03996434 chunk 1)
- **NCT05198128:** proposed quadruple-masked calcium-gluconate trial, estimated 200 participants; registry status unknown. (NCT05198128 chunk 1)
- **NCT02670304:** completed phase 4, 100 participants; letrozole versus aspirin after retrieval. (NCT02670304 chunk 1)
- **NCT03794037:** montelukast plus dydrogesterone in freeze-all cycles; suspended for lack of funding, estimated n=20. (NCT03794037 chunk 1)
- **NCT02392520:** planned luteal cetrorelix versus conventional treatment for severe early OHSS; registry status unknown. (NCT02392520 chunk 1)

Gene therapy, cell therapy, RNA therapy, genome editing, and immunotherapy have no current clinical role.

## 13. Prevention

### Primary prevention

- Assess AMH, AFC, PCOS, age, prior response/OHSS, and baseline ultrasound.
- Individualize gonadotropin dose and avoid excessive stimulation.
- Prefer a GnRH-antagonist protocol for high-risk patients.
- Use a GnRH-agonist trigger instead of hCG when clinically appropriate.
- Avoid or minimize additional hCG luteal support.
- Use cabergoline selectively in high-risk cycles.
- Consider metformin in appropriate patients with PCOS.
- Cancel or modify the cycle if risk becomes unacceptable. (mares2024ovarianhyperstimulationsyndrome pages 1-2, wu2022comparisonofthe pages 1-2)

### Secondary prevention

When excessive response is already evident, use coasting/withholding gonadotropins, alter trigger strategy, intensive monitoring, and **freeze all embryos** to avoid pregnancy-driven late OHSS. Cryopreservation is a real-world prevention strategy, although rare OHSS can still occur after agonist trigger/freeze-all.

### Tertiary prevention

Early symptom recognition, structured outpatient monitoring, prompt laboratory reassessment, thrombosis-risk evaluation, careful volume management, and timely paracentesis prevent progression and organ complications.

No vaccine, infectious prophylaxis, newborn screening, population screening, carrier screening, or public-health environmental intervention applies. Counseling before stimulation should explain warning symptoms, emergency contact pathways, and the possibility of cycle modification or deferred transfer.

## 14. Other species and natural disease

OHSS is primarily a human iatrogenic syndrome. No well-established, routinely recognized naturally occurring veterinary counterpart or zoonotic process was identified. Domestic mammals can develop ovarian enlargement or gonadotropin-related reproductive abnormalities, but these should not automatically be labeled natural OHSS without species-specific evidence. There is no transmission or zoonotic potential.

Relevant orthologous pathways—FSHR/LHCGR, VEGFA/KDR, TIE1, and PI3K–AKT—are conserved across mammals. Suggested model taxa are **Rattus norvegicus** (NCBI Taxonomy 10116) and **Mus musculus** (10090).

## 15. Model organisms and experimental systems

### Induced rat models

Immature or cycling rats are treated with gonadotropins followed by hCG to reproduce ovarian enlargement, increased corpora lutea, VEGF elevation, vascular leakage, and ascites. In Sun et al., induced rats showed increased ovarian TIE1 and VEGF, while TIE1 knockdown reduced ovarian weight, corpora lutea, and VEGF. These models are useful for causal signaling and permeability studies. Their limitations include pharmacologically compressed timing, species-specific ovarian physiology, and incomplete reproduction of human pregnancy, thrombosis, critical-care complications, and heterogeneous ART protocols. (sun2022tie1contributesto pages 1-2, sun2022tie1contributesto pages 7-9)

### Human cellular systems

Primary granulosa cells from women with OHSS and the non-tumorigenic human granulosa-lutein **SVOG** line are used with acute hCG stimulation. RT-qPCR, immunoblotting, promoter binding, silencing, and pathway inhibition support the EGR1→TIE1→PI3K/AKT→VEGF chain. Endothelial-cell systems are appropriate for permeability assays but do not reproduce the endocrine-organ context. (sun2022tie1contributesto pages 2-3)

### Genetic models and resources

No standardized commercial FSHR knock-in OHSS model was established in the retrieved evidence. Candidate research resources include MGI/IMSR for receptor or VEGF-pathway mouse lines, RGD for rat models, Cellosaurus for granulosa-cell lines, and GEO/ArrayExpress for exploratory expression datasets. Organoid, iPSC, single-cell, and spatial models remain emerging rather than validated OHSS standards.

## Overall interpretation and research gaps

Current expert understanding treats OHSS as a preventable, hCG-dependent vascular-permeability syndrome originating in an excessively luteinized ovary. The strongest evidence supports risk-adapted stimulation, antagonist protocols, agonist triggering, freeze-all strategies, and selective dopamine-agonist prophylaxis. VEGF/VEGFR2 is the central effector pathway, while EGR1–TIE1–PI3K–AKT is a promising upstream mechanism requiring clinical validation. (mares2024ovarianhyperstimulationsyndrome pages 2-3, wu2022comparisonofthe pages 1-2, sun2022tie1contributesto pages 1-2)

Priority gaps are standardized international severity criteria; contemporary population mortality and quality-of-life estimates; externally validated risk models across ancestries and ART protocols; rigorous evaluation of rare FSHR variants; and replicated single-cell, spatial, proteomic, metabolomic, and multi-omic studies. Experimental calcium/diosmin, mineralocorticoid, montelukast, letrozole, and luteal-antagonist strategies should not be represented as established therapies until adequately replicated.

### Key URLs and publication dates

- Mareș & Petca, *Ovarian hyperstimulation syndrome*, 2024: https://doi.org/10.26416/obsgin.72.4.2024.10891 (mares2024ovarianhyperstimulationsyndrome pages 2-3)
- Sun et al., *Experimental & Molecular Medicine*, January 2022: https://doi.org/10.1038/s12276-021-00722-8 (sun2022tie1contributesto pages 1-2)
- Wu et al., *Frontiers in Endocrinology*, 2022: https://doi.org/10.3389/fendo.2022.808517 (wu2022comparisonofthe pages 1-2)
- Guo et al., *Scientific Reports*, January 2016: https://doi.org/10.1038/srep19093 (guo2016pharmacologicinterventionsin pages 1-2)
- Alfaraj et al., *Cureus*, July 2023: https://doi.org/10.7759/cureus.42303 (alfaraj2023pregnancyoutcomesof pages 1-2)
- Salama et al., *BMC Women’s Health*, November 2017: https://doi.org/10.1186/s12905-017-0466-z; NCT02823080 (salama2017sequentiale2levels pages 1-2)

References

1. (OpenTargets Search: ovarian hyperstimulation syndrome-FSHR,VEGFA,KDR,LHCGR): Open Targets Query (ovarian hyperstimulation syndrome-FSHR,VEGFA,KDR,LHCGR, 13 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (mares2024ovarianhyperstimulationsyndrome pages 1-2): Alina Mareș and Aida Petca. Ovarian hyperstimulation syndrome. Obstetrica şi Ginecologia, 2024. URL: https://doi.org/10.26416/obsgin.72.4.2024.10891, doi:10.26416/obsgin.72.4.2024.10891. This article has 0 citations.

3. (NCT06333691 chunk 1): Aya Mohammed Abdallah. Comparative Study Between Calcium Gluconate With Diosmin, Cabergoline and Cabergoline With Diosmin. Minia University. 2022. ClinicalTrials.gov Identifier: NCT06333691

4. (sun2022tie1contributesto pages 1-2): Lihua Sun, Hui Tian, Songguo Xue, Hongjuan Ye, Xue Xue, Rongxiang Wang, Yu Liu, Caixia Zhang, Qiuju Chen, and Shaorong Gao. Tie1 contributes to the development of ovarian hyperstimulation syndrome under the regulation of egr1 in granulosa cells. Experimental & Molecular Medicine, 54:81-90, Jan 2022. URL: https://doi.org/10.1038/s12276-021-00722-8, doi:10.1038/s12276-021-00722-8. This article has 3 citations and is from a peer-reviewed journal.

5. (sun2022tie1contributesto pages 2-3): Lihua Sun, Hui Tian, Songguo Xue, Hongjuan Ye, Xue Xue, Rongxiang Wang, Yu Liu, Caixia Zhang, Qiuju Chen, and Shaorong Gao. Tie1 contributes to the development of ovarian hyperstimulation syndrome under the regulation of egr1 in granulosa cells. Experimental & Molecular Medicine, 54:81-90, Jan 2022. URL: https://doi.org/10.1038/s12276-021-00722-8, doi:10.1038/s12276-021-00722-8. This article has 3 citations and is from a peer-reviewed journal.

6. (wu2022comparisonofthe pages 1-2): Di Wu, Hao Shi, Yiping Yu, Ting Yu, and Jun Zhai. Comparison of the effectiveness of various medicines in the prevention of ovarian hyperstimulation syndrome: a network meta-analysis of randomized controlled trials. Frontiers in Endocrinology, Jan 2022. URL: https://doi.org/10.3389/fendo.2022.808517, doi:10.3389/fendo.2022.808517. This article has 21 citations.

7. (salama2017sequentiale2levels pages 1-2): Khalid M. Salama, Hesham M. Abo Ragab, Mohammed F. El Sherbiny, Ali A. Morsi, and Ibrahim I. Souidan. Sequential e2 levels not ovarian maximal diameter estimates were correlated with outcome of cetrotide therapy for management of women at high-risk of ovarian hyperstimulation syndrome: a randomized controlled study. BMC Women's Health, Nov 2017. URL: https://doi.org/10.1186/s12905-017-0466-z, doi:10.1186/s12905-017-0466-z. This article has 8 citations.

8. (NCT04351126 chunk 1): Muhammad saber mahmoud sayed zeafan. Management of Ovarian Hyperstimulation Syndrome as a State of Defective Mineralocorticoid Response. Ganin Fertility Center. 2019. ClinicalTrials.gov Identifier: NCT04351126

9. (NCT02620605 chunk 1): Mona M Shaban. The Influence of Timing of Cabergoline Initiation on Prevention of OHSS. Mona M Shaban. 2017. ClinicalTrials.gov Identifier: NCT02620605

10. (mares2024ovarianhyperstimulationsyndrome pages 3-5): Alina Mareș and Aida Petca. Ovarian hyperstimulation syndrome. Obstetrica şi Ginecologia, 2024. URL: https://doi.org/10.26416/obsgin.72.4.2024.10891, doi:10.26416/obsgin.72.4.2024.10891. This article has 0 citations.

11. (NCT02392520 chunk 1):  Luteal Antagonist Versus Conventional Treatment in Women With Severe Early Ovarian Hyperstimulation Syndrome (OHSS). Eugonia. 2015. ClinicalTrials.gov Identifier: NCT02392520

12. (guo2016pharmacologicinterventionsin pages 1-2): Jun-Liang Guo, Duo-Duo Zhang, Yue Zhao, Dan Zhang, Xi-Meng Zhang, Can-Quan Zhou, and Shu-Zhong Yao. Pharmacologic interventions in preventing ovarian hyperstimulation syndrome: a systematic review and network meta-analysis. Scientific Reports, Jan 2016. URL: https://doi.org/10.1038/srep19093, doi:10.1038/srep19093. This article has 48 citations and is from a peer-reviewed journal.

13. (guo2016pharmacologicinterventionsin pages 7-9): Jun-Liang Guo, Duo-Duo Zhang, Yue Zhao, Dan Zhang, Xi-Meng Zhang, Can-Quan Zhou, and Shu-Zhong Yao. Pharmacologic interventions in preventing ovarian hyperstimulation syndrome: a systematic review and network meta-analysis. Scientific Reports, Jan 2016. URL: https://doi.org/10.1038/srep19093, doi:10.1038/srep19093. This article has 48 citations and is from a peer-reviewed journal.

14. (NCT03996434 chunk 1):  Coasting Versus Antagonist Protocol in Patients at High Risk of OHSS. ClinAmygate. 2019. ClinicalTrials.gov Identifier: NCT03996434

15. (NCT03794037 chunk 1): Ahmed Saad. Montelukast for Prevention & Treatment of OHSS. Benha University. 2018. ClinicalTrials.gov Identifier: NCT03794037

16. (NCT02670304 chunk 1): Zhou Canquan. Preventive Application of Letrozole Decrease Incidence of Early Onset of OHSS. First Affiliated Hospital, Sun Yat-Sen University. 2012. ClinicalTrials.gov Identifier: NCT02670304

17. (sun2022tie1contributesto pages 7-9): Lihua Sun, Hui Tian, Songguo Xue, Hongjuan Ye, Xue Xue, Rongxiang Wang, Yu Liu, Caixia Zhang, Qiuju Chen, and Shaorong Gao. Tie1 contributes to the development of ovarian hyperstimulation syndrome under the regulation of egr1 in granulosa cells. Experimental & Molecular Medicine, 54:81-90, Jan 2022. URL: https://doi.org/10.1038/s12276-021-00722-8, doi:10.1038/s12276-021-00722-8. This article has 3 citations and is from a peer-reviewed journal.

18. (alviggi2018clinicalrelevanceof pages 15-16): Carlo Alviggi, Alessandro Conforti, Daniele Santi, Sandro C Esteves, Claus Yding Andersen, Peter Humaidan, Paolo Chiodini, Giuseppe De Placido, and Manuela Simoni. Clinical relevance of genetic variants of gonadotrophins and their receptors in controlled ovarian stimulation: a systematic review and meta-analysis. Human Reproduction Update, 24:599–614, Jun 2018. URL: https://doi.org/10.1093/humupd/dmy019, doi:10.1093/humupd/dmy019. This article has 137 citations and is from a highest quality peer-reviewed journal.

19. (alfaraj2023pregnancyoutcomesof pages 1-2): Samaher Alfaraj, Ashwaq A Alharbi, Hind J Aldabal, Yara S Alhabib, and Shihanah AlKhelaiwi. Pregnancy outcomes of assisted reproductive technology (art) cycle complicated by ovarian hyperstimulation syndrome (ohss): case series study. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.42303, doi:10.7759/cureus.42303. This article has 6 citations.

20. (alfaraj2023pregnancyoutcomesof pages 7-8): Samaher Alfaraj, Ashwaq A Alharbi, Hind J Aldabal, Yara S Alhabib, and Shihanah AlKhelaiwi. Pregnancy outcomes of assisted reproductive technology (art) cycle complicated by ovarian hyperstimulation syndrome (ohss): case series study. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.42303, doi:10.7759/cureus.42303. This article has 6 citations.

21. (mares2024ovarianhyperstimulationsyndrome pages 2-3): Alina Mareș and Aida Petca. Ovarian hyperstimulation syndrome. Obstetrica şi Ginecologia, 2024. URL: https://doi.org/10.26416/obsgin.72.4.2024.10891, doi:10.26416/obsgin.72.4.2024.10891. This article has 0 citations.

22. (alfaraj2023pregnancyoutcomesof pages 2-3): Samaher Alfaraj, Ashwaq A Alharbi, Hind J Aldabal, Yara S Alhabib, and Shihanah AlKhelaiwi. Pregnancy outcomes of assisted reproductive technology (art) cycle complicated by ovarian hyperstimulation syndrome (ohss): case series study. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.42303, doi:10.7759/cureus.42303. This article has 6 citations.

23. (NCT05198128 chunk 1): Ahmed Said Ali. Ovarian Hyperstimulation Syndrome Using Calcium Infusion. Al-Azhar University. 2022. ClinicalTrials.gov Identifier: NCT05198128

## Artifacts

- [Edison artifact artifact-00](Ovarian_Hyperstimulation_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.