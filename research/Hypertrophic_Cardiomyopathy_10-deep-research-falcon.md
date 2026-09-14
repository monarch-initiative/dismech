---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T05:46:50.706714'
end_time: '2026-09-06T05:58:40.309019'
duration_seconds: 709.6
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 10
  mondo_id: MONDO:0012112
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 39
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 0
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0012112
    reported_labels:
    - if available
    ontology_label: hypertrophic cardiomyopathy 10
  - term_id: HP:0005110
    reported_labels:
    - 'D166H family: **62%**, approximately three times the rate cited for general
      HCM. Episodic or persistent'
    ontology_label: Atrial fibrillation
  - term_id: HP:0001698
    reported_labels:
    - Common in generic HCM but absent in the reported D166H family
    ontology_label: Pericardial effusion
  - term_id: GO:0030017
    reported_labels:
    - GO cellular component:** sarcomere
    ontology_label: sarcomere
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hypertrophic_Cardiomyopathy_10-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 10
- **MONDO ID:** MONDO:0012112 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 10** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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
- **Disease Name:** Hypertrophic Cardiomyopathy 10
- **MONDO ID:** MONDO:0012112 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 10** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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


# Hypertrophic Cardiomyopathy 10 (MYL2-related HCM): Research Report

## Executive summary and evidence scope

Hypertrophic cardiomyopathy 10 (HCM10) is a rare, principally autosomal-dominant sarcomeric cardiomyopathy caused by pathogenic variants in **MYL2**, which encodes ventricular/slow-skeletal myosin regulatory light chain 2 (RLC). It is characterized by otherwise unexplained left-ventricular hypertrophy (LVH), but expression is age-dependent and highly variable: carriers may remain phenotype-negative, develop apical or conventional HCM, or—depending on the allele—show restrictive physiology, atrial fibrillation (AF), heart failure, or sudden-death risk. MYL2 variants are rare relative to **MYH7** and **MYBPC3**. Most clinical-management evidence therefore comes from unstratified HCM cohorts, not HCM10 specifically. (glavaski2023hypertrophiccardiomyopathygenetic pages 2-4, yadav2019hereditaryheartdisease pages 1-2)

The strongest subtype-specific human data concern **p.Glu22Lys**, **p.Arg58Gln**, and **p.Asp166His**. The following evidence map distinguishes those findings from generic HCM guidance.

| Domain | MYL2-specific evidence | Quantitative finding | Evidence type | Key limitation |
|---|---|---|---|---|
| Founder allele and modifiers | **MYL2 c.64G>A, p.Glu22Lys** occurred in 14 HCM families sharing a founder haplotype. Hypertension, obesity, or another sarcomeric variant increased disease expression. (claes2016hypertrophicremodellingin pages 1-1, claes2016hypertrophicremodellingin pages 4-5) | 38 carriers; HCM in **89%** of carriers with an additional hypertrophy-promoting factor; hypertension in **71%** of affected carriers with an additional factor. | Human family and segregation study | Low penetrance and generally mild phenotype when isolated; estimates may be founder-population dependent. |
| Familial restrictive phenotype | **MYL2 c.496G>C, p.Asp166His** segregated with HCM and was associated with restrictive filling, atrial enlargement, atrial fibrillation, heart failure, and embolic or arrhythmic events. (bortoli2020novelmissensevariant pages 1-4, bortoli2020novelmissensevariant pages 4-7) | 12 additional carriers: **11 with HCM** and 1 borderline; LOD **5.35**; AF **62%**; restrictive filling **38%**; no LV outflow obstruction. | Human multigenerational family study with structural modelling | Single-family phenotype may reflect shared genetic or environmental modifiers; classified as likely pathogenic in the study. |
| Patient-cell phenotype | Patient-derived cardiomyocytes carrying **MYL2 p.Arg58Gln (R58Q)** reproduced hypertrophy, myofibrillar disarray, abnormal calcium handling, and irregular beating. (zhou2019inducedpluripotentstem pages 4-7, zhou2019inducedpluripotentstem pages 8-9) | Cell area **4100 ± 171 versus 3200 ± 144 μm²**; disarray **42% versus 21%**; irregular beating **30.3% versus 2.4%**; L-type calcium-current density reduced **45.3%**. | Human patient-derived iPSC cardiomyocytes and myectomy tissue | Single-patient line compared with a maternal control; cells were immature and not reported as an isogenic pair. |
| Phosphorylation rescue | In R58Q biochemical and muscle-fibre systems, a **Ser15-to-Asp phosphomimetic** restored actin interaction, ATPase activity, and force while shifting myosin toward the disordered-relaxed state. (yadav2019phosphomimetic‐mediatedinvitro pages 8-10) | MLCK phosphorylation increased maximal active isometric force by approximately **30%** in prior R58Q trabecula experiments; phosphomimetic measures approached wild-type levels. | Recombinant protein, reconstituted porcine cardiac fibres, and transgenic-mouse tissue | Preclinical in vitro or ex vivo rescue only; no S15D-R58Q animal or human therapeutic study. |
| Contemporary clinical guidance | **2023 ESC** and **2024 AHA/ACC multisociety** guidance supports phenotype-led imaging, genetic testing and counselling, cascade screening, sudden-death risk assessment, and treatment of eligible HCM. (sanghvi2025hypertrophiccardiomyopathymanagement pages 14-15, ramonfaur2024eighteen‐monthreal‐worldexperience pages 12-12) | Guideline-level recommendations; no MYL2-specific treatment-effect estimate was reported. | Evidence-based clinical-practice guidelines | **Generic HCM evidence is not genotype-stratified for MYL2-HCM10** and does not establish variant-specific efficacy or prognosis. |


*Table: Compact evidence map linking major MYL2 variants to family, patient-cell, and functional findings. It distinguishes subtype-specific observations from contemporary HCM guidance that was not stratified by MYL2 genotype.*

**Evidence notation:** “human” means affected families, myocardial tissue, or patient-derived cells; “model” means transgenic animals or engineered tissue; “in vitro” means biochemical or reconstituted-muscle experiments. PMID values were not available in the retrieved full texts; DOI URLs are supplied instead rather than risking incorrect PMID assignment.

---

## 1. Disease information

### Definition

HCM10 is the **MYL2-related subtype of hypertrophic cardiomyopathy**, a primary myocardial disorder in which LV wall thickening is not explained solely by pressure loading, valvular disease, athletic remodeling, or infiltration. Histologic hallmarks shared with sarcomeric HCM are cardiomyocyte hypertrophy, myofibrillar disarray, and interstitial fibrosis. Preservation or elevation of ejection fraction is common early, despite impaired relaxation and diastolic filling. (glavaski2023hypertrophiccardiomyopathygenetic pages 2-4, yadav2019hereditaryheartdisease pages 1-2)

### Identifiers and terminology

- **MONDO:** MONDO:0012112, as specified in the target record.
- **OMIM disease:** commonly catalogued as *Cardiomyopathy, hypertrophic, 10* (**CMH10/HCM10; OMIM 608758**).
- **Causal gene:** **MYL2**, commonly catalogued as OMIM 160781; HGNC-approved symbol MYL2.
- **Synonyms:** hypertrophic cardiomyopathy 10; CMH10; MYL2-related hypertrophic cardiomyopathy; familial hypertrophic cardiomyopathy due to ventricular myosin regulatory light-chain variants; cardiac regulatory myosin light-chain cardiomyopathy.
- **MeSH:** use the broader term *Cardiomyopathy, Hypertrophic*.
- **ICD-10-CM:** I42.1 for obstructive HCM and I42.2 for other HCM; there is no MYL2-specific code.
- **ICD-11:** code under hypertrophic cardiomyopathy; no gene-specific subdivision was established in the retrieved evidence.
- **Orphanet:** use the broader familial/genetic HCM entry; a reliably verified HCM10-specific ORPHA identifier was not recovered.

The report synthesizes **aggregated disease-level resources and published families**, not individual EHR records. Some detailed phenotypes derive from single families or one patient-derived cell line and should not be interpreted as population-wide frequencies. (bortoli2020novelmissensevariant pages 1-4, bortoli2020novelmissensevariant pages 4-7, zhou2019inducedpluripotentstem pages 4-7)

---

## 2. Etiology

### Causal factors and genetic risk

The initiating lesion is generally a **heterozygous germline MYL2 variant** affecting the myosin lever arm, phosphorylation-dependent regulation, or actin–myosin cycling. Reported HCM-associated substitutions include p.Ala13Thr, p.Phe18Leu, p.Glu22Lys, p.Asn47Lys, p.Arg58Gln, p.Pro95Ala, p.Lys104Glu, p.Asp166Val, and p.Asp166His, although contemporary pathogenicity must be evaluated variant by variant. MYL2 is a rare HCM gene and many historical assertions require re-evaluation under ACMG/AMP and ClinGen standards. (glavaski2023hypertrophiccardiomyopathygenetic pages 2-4, yadav2019hereditaryheartdisease pages 1-2)

**Strong family evidence:**

- **c.64G>A, p.Glu22Lys (E22K):** 38 carriers from 14 families shared a founder haplotype. The allele alone showed low penetrance and usually mild expression. With hypertension, obesity, or another sarcomeric variant, HCM occurred in **89%** of carriers; hypertension was present in **71%** of affected carriers who had an additional risk factor. This is direct human evidence for gene–environment/genetic-background interaction. (claes2016hypertrophicremodellingin pages 1-1, claes2016hypertrophicremodellingin pages 4-5)
- **c.496G>C, p.Asp166His (D166H):** absent from gnomAD at publication, classified by the investigators as likely pathogenic, and segregated with disease at LOD 5.35. Of 12 additional carriers, 11 had HCM and one had borderline wall thickness. Structural modeling placed the altered conserved terminal residue against the bent myosin lever arm. (bortoli2020novelmissensevariant pages 1-4)
- **p.Arg58Gln (R58Q):** associated with apical HCM and reproduced disease-related cellular abnormalities in patient-derived cardiomyocytes. (zhou2019inducedpluripotentstem pages 4-7)

### Environmental and lifestyle modifiers

Hypertension, obesity, diabetes, renal dysfunction, sleep apnea, alcohol exposure, cardiac loading, and physical activity can modify the broader HCM phenotype, but only hypertension/obesity were directly evaluated in an MYL2 founder cohort. These factors are **modifiers**, not primary causes of HCM10. (claes2016hypertrophicremodellingin pages 1-1, claes2016hypertrophicremodellingin pages 4-5, hao2026hypertrophiccardiomyopathycomprehensive pages 8-9)

No infectious agent, toxin, radiation, or occupational exposure is established as a cause of HCM10. There is no validated genetic “protective allele.” Clinically useful protective measures are control of blood pressure and obesity, avoidance of dehydration or drugs that worsen obstruction where relevant, and longitudinal surveillance. Immunization has no disease-specific preventive role.

---

## 3. Phenotypes

| Phenotype | Characteristics and frequency | Suggested HPO term |
|---|---|---|
| LV hypertrophy | Variable; asymmetric, apical, or relatively mild in restrictive disease. E22K may remain subclinical without modifiers. | HP:0001712, Left ventricular hypertrophy |
| Apical HCM | Documented with R58Q; chronic, variably symptomatic. | HP:0001712 plus apical localization annotation |
| Diastolic dysfunction/restrictive filling | D166H family: restrictive filling in **38%**, sometimes with maximum wall thickness ≤15 mm. | HP:0005117, Elevated filling pressure/diastolic dysfunction; HP:0002092 where restrictive cardiomyopathy is coded |
| Atrial enlargement | D166H mean left-atrial diameter rose from **45±12 to 54±14 mm**. | HP:0030680, Left atrial enlargement; HP:0006698, Biatrial enlargement |
| Atrial fibrillation | D166H family: **62%**, approximately three times the rate cited for general HCM. Episodic or persistent. | HP:0005110 |
| Ventricular arrhythmia/SCD risk | Nonsustained VT in the R58Q index patient; ventricular fibrillation and death occurred in the D166H pedigree. Frequency is not generalizable. | HP:0004756; HP:0001663; HP:0001645 |
| LV outflow-tract obstruction | Common in generic HCM but absent in the reported D166H family. | HP:0001698 |
| Heart failure/exercise intolerance | Dyspnea, restrictive physiology, pulmonary hypertension, end-stage disease, and transplantation occurred in severe family members. | HP:0001635; HP:0001648; HP:0002094; HP:0003236 |
| Syncope/chest pain/palpitations | Recognized HCM symptoms, but MYL2-specific frequencies are unavailable. | HP:0001279; HP:0001681; HP:0001962 |
| Histopathology | Cardiomyocyte hypertrophy, myofibrillar disarray, interstitial/pericellular fibrosis. | HP:0001639; HP:0005144; HP:0001685 |

The D166H family’s AF and restrictive pattern may be allele-specific or reflect shared modifiers; the authors explicitly cautioned against broad generalization from one pedigree. (bortoli2020novelmissensevariant pages 1-4, bortoli2020novelmissensevariant pages 4-7)

**Quality of life:** symptoms can limit exercise, work, and daily activity and increase anxiety concerning arrhythmia and familial risk. No MYL2-specific EQ-5D, SF-36, KCCQ, or HCMSQ dataset was found. Generic HCM trials show that gradient and symptom reduction can improve patient-reported health, but this has not been separately demonstrated in HCM10.

---

## 4. Genetic and molecular information

### Gene and protein

**MYL2** encodes the ventricular and slow-twitch skeletal-muscle myosin RLC. RLC wraps around an IQ motif in the MYH7 neck/lever arm, stabilizes lever-arm stiffness, and tunes force generation and actin–myosin kinetics. Its N terminus contains an EF-hand-like divalent-cation-binding region and a conserved **Ser15 phosphorylation site** regulated by cardiac myosin light-chain kinase. (yadav2019phosphomimetic‐mediatedinvitro pages 8-10, yadav2019hereditaryheartdisease pages 1-2)

### Variant interpretation

- Most established HCM10 alleles are **heterozygous missense, germline variants**, consistent with dominant inheritance and a poison-peptide/altered-function mechanism rather than simple haploinsufficiency.
- **p.Asp166His** was absent from gnomAD in the 2020 report and classified likely pathogenic by its authors; current ClinVar submissions and population releases should be checked at implementation time. (bortoli2020novelmissensevariant pages 1-4)
- **p.Glu22Lys** has strong founder/segregation evidence but reduced penetrance; classification should account for ancestry, phenotype, and coexisting hypertrophy drivers. (claes2016hypertrophicremodellingin pages 1-1)
- **p.Arg58Gln** has human phenotype, tissue, iPSC, mouse, and biochemical functional support. (yadav2019phosphomimetic‐mediatedinvitro pages 8-10, zhou2019inducedpluripotentstem pages 4-7)
- A **homozygous c.403-1G>C splice variant** causes a distinct infantile cardioskeletal myopathy with type-I fiber disease and early cardiac death. This recessive syndrome should not be conflated with dominant HCM10.

No recurrent pathogenic chromosomal deletion, translocation, inversion, aneuploidy, somatic MYL2 driver, or repeat expansion defines HCM10. CMA, karyotyping, FISH, and repeat-expansion assays are therefore not first-line tests.

### Modifiers and epigenetics

Other sarcomeric variants, hypertension, and obesity demonstrably modify E22K penetrance. Broader HCM work implicates polygenic background and epigenetic regulation, but no validated MYL2-specific modifier gene, methylation signature, or clinical epigenomic biomarker is established. (claes2016hypertrophicremodellingin pages 1-1, claes2016hypertrophicremodellingin pages 4-5)

---

## 5. Environmental information

HCM10 is not environmentally acquired. Relevant exposures act by changing ventricular load, energetics, or arrhythmia susceptibility:

- **Hypertension:** strongest directly demonstrated MYL2 modifier.
- **Obesity/metabolic disease:** may increase hypertrophic loading and symptom burden.
- **Exercise:** does not cause the mutation; intensity should be individualized through shared decision-making rather than universal prohibition.
- **Alcohol, dehydration, stimulants, and vasodilating agents:** may aggravate arrhythmia or dynamic obstruction in susceptible patients, although no MYL2-specific effect size exists.
- **Smoking:** increases general cardiovascular risk but is not a proven HCM10 penetrance determinant.
- **Infection:** not etiologic; myocarditis remains a differential diagnosis.

The E22K founder study provides the clearest real-world gene–environment observation: the variant often required an additional hypertrophy-promoting exposure or genotype for overt disease. (claes2016hypertrophicremodellingin pages 1-1)

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous **MYL2 missense variant** alters ventricular RLC structure or phosphorylation-dependent regulation, which **leads to** abnormal support of the MYH7 lever arm. (bortoli2020novelmissensevariant pages 1-4, yadav2019phosphomimetic‐mediatedinvitro pages 8-10)
2. Altered lever-arm mechanics **lead to** variant-specific changes in actin binding, ATPase activity, cross-bridge recruitment/detachment, force, and myofilament calcium responsiveness. These changes are demonstrated in biochemical and transgenic systems but are not identical for every allele. (yadav2019phosphomimetic‐mediatedinvitro pages 8-10)
3. **R58Q branch:** reduced phosphorylation and excessive stabilization of the ATP-conserving super-relaxed state **lead to** fewer working myosin heads and abnormal force kinetics; this was experimentally improved by Ser15 phosphomimicry. (yadav2019phosphomimetic‐mediatedinvitro pages 8-10)
4. **D166H branch:** deformation near the bent lever arm is predicted to **lead to** abnormal cross-bridge geometry; this remains structural inference rather than direct kinetic demonstration. (bortoli2020novelmissensevariant pages 1-4)
5. Sarcomere inefficiency and altered mechanosensing **lead to** compensatory hypertrophic signaling and energetic stress; specific downstream MAPK/mTOR/PI3K attribution in human HCM10 remains incompletely demonstrated.
6. Calcium-handling remodeling **leads to** prolonged calcium decay and electrical instability. R58Q iPSC-cardiomyocytes showed reduced L-type calcium current, abnormal transients, and irregular beating. (zhou2019inducedpluripotentstem pages 4-7, zhou2019inducedpluripotentstem pages 8-9)
7. Chronic cardiomyocyte stress **leads to** cellular hypertrophy, sarcomere disarray, and fibrosis, which **result in** impaired relaxation, ventricular stiffness, and—in some alleles—apical or restrictive remodeling. (bortoli2020novelmissensevariant pages 4-7, zhou2019inducedpluripotentstem pages 4-7)
8. **Obstructive branch:** hypertrophy plus mitral–septal geometry may **result in** LV outflow obstruction; this is common in general HCM but was absent in the D166H family. **Nonobstructive/restrictive branch:** atrial-pressure loading **leads to** atrial enlargement, AF, pulmonary hypertension, embolism, and heart failure. (bortoli2020novelmissensevariant pages 1-4, bortoli2020novelmissensevariant pages 4-7)
9. Fibrosis, disarray, calcium instability, and chamber remodeling **lead to** ventricular arrhythmia, sudden death, or end-stage heart failure in a minority of affected patients. The relative contribution of each pathway in HCM10 is inferred from combined human and model evidence.

### Key experimental findings

**Human R58Q iPSC-cardiomyocytes:** cell area was **4100±171 versus 3200±144 μm²**; disarray occurred in **42% versus 21%**; irregular beating in **30.3% versus 2.4%**; L-type calcium-current density fell **45.3%** at 0 mV; and calcium-transient decay was prolonged (**1.8±0.3 versus 1.3±0.2 seconds**). Myectomy tissue showed hypertrophy, disarray, and interstitial/pericellular fibrosis. (zhou2019inducedpluripotentstem pages 4-7)

**R58Q biochemical rescue:** R58Q reduced rigor actin affinity, ATPase Vmax, and maximal isometric force and favored the super-relaxed state. An S15D phosphomimetic shifted myosin toward the disordered-relaxed state and restored force and ATPase behavior toward wild type; MLCK phosphorylation increased maximal force by approximately **30%** in prior trabecular experiments. This is preclinical, not a demonstrated therapy. (yadav2019phosphomimetic‐mediatedinvitro pages 8-10)

Short source excerpts supporting these conclusions include: “**Myosin regulatory light chain phosphorylation is important for cardiac muscle mechanics/function**” and the R58Q iPSC study title’s summary that cells “**show hypertrophy, myofibrillar disarray, and calcium perturbations**.” (yadav2019phosphomimetic‐mediatedinvitro pages 8-10, dolder2025experimentalmodelsof pages 36-36)

### Suggested ontology annotations

- **GO biological process:** cardiac muscle contraction (GO:0060048); actin–myosin filament sliding (GO:0033275); regulation of cardiac muscle contraction (GO:0055117); muscle filament sliding (GO:0030049); calcium-ion homeostasis (GO:0055074); cardiac muscle hypertrophy (GO:0003300); response to oxidative stress (GO:0006979).
- **GO cellular component:** sarcomere (GO:0030017); myosin complex (GO:0016459); A band (GO:0031672); myofibril (GO:0030016); contractile fiber (GO:0043292).
- **Cell Ontology:** cardiac muscle cell/cardiomyocyte (CL:0000746); ventricular cardiac muscle cell (CL:0002131); cardiac fibroblast (use current CL release); endothelial cell (CL:0000115); cardiac-resident macrophage only as a secondary remodeling cell, not a primary target.

No subtype-specific single-cell atlas, spatial transcriptomic dataset, lipidomic signature, CRISPR screen, or integrated human multi-omics study was identified. Available transcriptomic/proteomic findings are largely mouse or generic HCM and should not be treated as HCM10 biomarkers.

---

## 7. Anatomical structures affected

- **Primary organ/system:** heart and cardiovascular system.
- **Primary sites:** left-ventricular myocardium, interventricular septum, or LV apex; atria become secondarily enlarged with restrictive filling/AF.
- **Secondary sites:** mitral valve/LV outflow tract in obstructive disease; pulmonary circulation in advanced diastolic failure; cerebral/systemic circulation through AF-related embolism.
- **Tissues/cells:** ventricular myocardium and cardiomyocytes are primary; interstitial fibroblasts contribute to fibrosis; microvascular and conduction-system remodeling are secondary.
- **Subcellular localization:** thick filament, myosin neck/lever arm, sarcomere, myofibril; downstream calcium-handling machinery and mitochondria may remodel.
- **Lateralization:** not left/right-sided in the usual sense; ventricular hypertrophy is often asymmetric rather than unilateral.

Suggested anatomy terms include **UBERON:0000948 heart**, **UBERON:0002084 heart left ventricle**, **UBERON:0002094 interventricular septum**, and ventricular myocardium terms from the current UBERON release.

---

## 8. Temporal development

Dominant HCM10 is generally **chronic and lifelong at the genetic level**, with insidious, age-dependent phenotypic emergence. Onset ranges from childhood to late adulthood; a normal study at one age does not establish lifelong nonpenetrance. E22K may remain mild until an additional loading or genetic factor appears. D166H showed progression toward atrial enlargement, AF, restrictive physiology, and advanced heart failure in some relatives. (bortoli2020novelmissensevariant pages 1-4, claes2016hypertrophicremodellingin pages 1-1)

For sarcomeric HCM overall—not MYL2 alone—a 2024 meta-analysis found **57% penetrance** among nonproband relatives, mean diagnosis age **38 years**, and **15% phenotypic conversion** over about eight years beginning at a mean age of 16. Incidentally identified population carriers had much lower penetrance, approximately **11%**. The paper concluded that penetrance is “**highly variable and influenced by currently undefined and context-dependent genetic and environmental factors**.” These estimates must not be entered as HCM10-specific frequencies. (hao2026hypertrophiccardiomyopathycomprehensive pages 8-9)

There is no spontaneous genetic remission. Symptoms or obstruction may improve with treatment, but surveillance remains necessary. Critical intervention windows include presymptomatic cascade detection, emergence of hypertrophy or arrhythmia, pregnancy planning, and transition from pediatric to adult care.

---

## 9. Inheritance and population

- **Inheritance:** usually autosomal dominant, with a 50% transmission probability from a heterozygous parent.
- **Penetrance:** incomplete, age-dependent, allele- and context-dependent. E22K is a particularly clear example of low penetrance without additional risk factors. (claes2016hypertrophicremodellingin pages 1-1)
- **Expressivity:** highly variable, ranging from no hypertrophy to apical HCM, restrictive filling, arrhythmia, or advanced heart failure.
- **Anticipation:** not established.
- **Germline mosaicism:** biologically possible but no characteristic HCM10 rate is known.
- **Founder effect:** demonstrated for E22K in 14 related founder-haplotype families. (claes2016hypertrophicremodellingin pages 1-1)
- **Consanguinity:** not relevant to usual dominant HCM10, but important in recessive MYL2 infantile myopathy.
- **Sex:** no reliable MYL2-specific sex ratio. Generic HCM is genetically expected to affect both sexes, although ascertainment and expression differ.

No robust prevalence, incidence, carrier-frequency, ethnicity-specific frequency, or geographic distribution has been established for HCM10. Generic clinically apparent HCM is often estimated near **1:500**, while broader imaging/genomic definitions yield higher estimates; these figures must not be assigned to MYL2-HCM10. MYL2 constitutes only a small minority of molecularly diagnosed HCM. (glavaski2023hypertrophiccardiomyopathygenetic pages 2-4)

---

## 10. Diagnostics

### Clinical workflow

1. **History and examination:** dyspnea, chest pain, palpitations, syncope, exercise intolerance, family HCM/SCD, hypertension, skeletal weakness, and a three-generation pedigree.
2. **ECG and ambulatory monitoring:** LVH/repolarization abnormalities, conduction disease, AF, nonsustained VT, or other arrhythmia. The D166H family included first-degree AV block and left anterior hemiblock. (bortoli2020novelmissensevariant pages 4-7)
3. **Transthoracic echocardiography:** maximal wall thickness, distribution of hypertrophy, systolic/diastolic function, left-atrial size, systolic anterior mitral motion, and resting/provoked LVOT gradient.
4. **CMR:** useful when echocardiography is equivocal, for apical disease, wall-thickness definition, apical aneurysm, and late-gadolinium-enhancement fibrosis assessment.
5. **Exercise testing:** functional capacity and provoked obstruction when clinically appropriate.
6. **Laboratory biomarkers:** BNP/NT-proBNP and troponin may support severity assessment but are neither HCM10-specific nor diagnostic.
7. **Biopsy:** not routine; when available, may show hypertrophy, disarray, and fibrosis. It is reserved mainly for unresolved infiltrative/metabolic differentials.

Contemporary practice should follow the **2023 ESC cardiomyopathy guideline** and **2024 AHA/ACC multisociety HCM guideline**. A systematic comparison found broad agreement on echocardiography, genetic testing, family screening, and medical/invasive management, but differences in CMR use and SCD-risk frameworks. (sanghvi2025hypertrophiccardiomyopathymanagement pages 14-15, ramonfaur2024eighteen‐monthreal‐worldexperience pages 12-12)

### Clinical criteria and differential diagnosis

In adults, otherwise unexplained maximal LV wall thickness around **≥15 mm** generally supports HCM; lower thresholds may be meaningful in first-degree relatives or genotype-positive individuals. Pediatric interpretation uses body-size-adjusted z scores. Exclude hypertensive remodeling, aortic stenosis, athlete’s heart, amyloidosis, Fabry disease, glycogen-storage disease, mitochondrial disease, RASopathies, and myocarditis.

### Genetic testing

- Test an affected proband using a **validated cardiomyopathy panel** that includes MYL2 and other definitive HCM genes, with deletion/duplication analysis where technically appropriate.
- Confirm a pathogenic/likely pathogenic result and offer **targeted cascade testing** to relatives with pre- and post-test genetic counseling.
- Do not use a VUS for predictive testing or irreversible clinical decisions.
- If panel testing is negative despite strong familial disease, updated panel reanalysis, WES, or WGS may detect overlooked coding, splice, structural, or deep-intronic variants. WGS/WES are adjuncts, not substitutes for careful phenotype and variant interpretation.
- CMA, FISH, karyotype, mtDNA, and repeat-expansion tests are indicated only when syndromic clues or another diagnosis warrants them.
- RNA sequencing can clarify suspected splice variants but is not routine diagnostic testing.

Genetic results are most actionable for etiologic confirmation, cascade screening, and reproductive counseling; current SCD decisions remain phenotype-led. (sanghvi2025hypertrophiccardiomyopathymanagement pages 14-15)

---

## 11. Outcome and prognosis

The course ranges from asymptomatic longevity to AF, embolic stroke, ventricular arrhythmia, restrictive or systolic heart failure, transplantation, and sudden death. D166H is associated within one pedigree with high AF/restrictive burden and adverse outcomes, but it does not establish an MYL2-wide prognosis. (bortoli2020novelmissensevariant pages 1-4, bortoli2020novelmissensevariant pages 4-7)

Generic optimally treated HCM mortality is reported at **<1% annually**, with near-normal life expectancy possible when recognized and managed appropriately; this is not an HCM10-specific survival estimate. Prognostic assessment should incorporate prior cardiac arrest/VT, unexplained syncope, family SCD, maximal wall thickness, apical aneurysm, LVEF <50%, nonsustained VT, LVOT obstruction, atrial size, symptoms, and CMR fibrosis—not genotype alone. (sanghvi2025hypertrophiccardiomyopathymanagement pages 14-15, kasiakogias2025exploringthecurrent pages 10-11)

Important morbidity includes reduced exercise capacity, anxiety, device burden, AF/stroke, heart-failure hospitalization, and treatment adverse effects. No validated MYL2-specific prognostic biomarker or calculator exists.

---

## 12. Treatment

There is **no approved MYL2-genotype-specific therapy**. Management follows the clinical HCM phenotype.

### Phenotype-directed algorithm

- **Asymptomatic genotype-positive/phenotype-negative:** surveillance, risk-factor treatment, family counseling; no prophylactic HCM drug is proven.
- **Symptomatic obstructive HCM:** a nonvasodilating beta blocker is generally first line; verapamil or diltiazem is an alternative in suitable patients. Persistent symptoms may prompt disopyramide, a cardiac myosin inhibitor, or expert-center septal reduction.
- **Mavacamten:** a reversible cardiac myosin inhibitor for eligible symptomatic obstructive HCM; requires serial echocardiography because excessive suppression can reduce LVEF. MYL2-specific efficacy has not been established.
- **Nonobstructive symptoms:** cautious diuresis for congestion and conventional management of AF or systolic dysfunction; evidence for myosin inhibitors is less certain.
- **AF:** anticoagulation and rhythm/rate management according to HCM guidance; thromboembolic risk is clinically important regardless of conventional CHA₂DS₂-VASc thresholds.
- **SCD prevention:** implantable cardioverter-defibrillator after cardiac arrest/sustained VT and for selected high-risk primary-prevention patients.
- **Refractory obstruction:** surgical septal myectomy or alcohol septal ablation at experienced centers.
- **End-stage disease:** guideline-directed heart-failure care and transplant evaluation.

Suggested NCIT annotations include beta-adrenergic blocking agent, calcium-channel blocker, antiarrhythmic agent, anticoagulant therapy, implantable cardioverter-defibrillator placement, septal myectomy, alcohol septal ablation, and heart transplantation; verify preferred NCIT concept codes against the current release.

### Current implementation and experimental therapy

A 2024 racially diverse real-world cohort of 66 obstructive-HCM patients treated with mavacamten reported ≥1 NYHA-class improvement in **72%** after at least six months, an average **80±46-mmHg** reduction in peak LVOT gradient, elimination of significant obstruction in **79.1%**, and temporary discontinuation for LVEF <50% in three patients. These results were not MYL2-stratified. (ramonfaur2024eighteen‐monthreal‐worldexperience pages 12-12)

Ongoing or recent programs include mavacamten long-term extension **NCT03723655**, VALOR-HCM **NCT04349072**, and aficamten phase 2/3 studies. Retrieved current implementation studies include NCT06116968, NCT06146660, NCT06023186, NCT06551129, and NCT06549608. No trial specifically targets MYL2-HCM10.

RLC Ser15 phosphomimicry is an experimental mechanism-directed concept: S15D rescued R58Q abnormalities in reconstituted porcine fibers, but no human gene-, RNA-, or protein-replacement therapy has demonstrated safety or efficacy. (yadav2019phosphomimetic‐mediatedinvitro pages 8-10)

---

## 13. Prevention

- **Primary prevention:** the inherited variant cannot presently be prevented after conception. Reproductive options include genetic counseling, prenatal diagnosis, and preimplantation genetic testing when a familial pathogenic variant is established.
- **Secondary prevention:** cascade genetic testing plus ECG/echocardiographic surveillance of first-degree relatives; CMR or rhythm monitoring according to phenotype.
- **Tertiary prevention:** blood-pressure and weight control, individualized exercise advice, AF anticoagulation, arrhythmia surveillance, ICD placement when indicated, and timely treatment of obstruction or heart failure.
- **Behavioral measures:** maintain hydration, avoid unreviewed stimulants/performance-enhancing agents, and address obesity, sleep apnea, smoking, and hypertension.
- **Public health:** clinician and family education and access to specialist cardiomyopathy/genetic services are more relevant than population-wide screening because HCM10 is rare.

No vaccine, antimicrobial prophylaxis, newborn biochemical screen, or population carrier-screening program is indicated specifically for HCM10.

---

## 14. Other species and natural disease

MYL2 orthologs are evolutionarily conserved across vertebrates, including mouse (*Myl2*), rat, pig, zebrafish, dog, and cat. No well-established naturally occurring veterinary disease equivalent specifically caused by an orthologous MYL2 HCM10 variant was identified in the retrieved literature. Consequently, breed-specific VBO terms, veterinary prevalence, and zoonotic transmission are not applicable. HCM10 is noninfectious and has no zoonotic potential.

Porcine cardiac fibers are useful for protein-reconstitution experiments because their sarcomeric mechanics are experimentally tractable, but this is an induced ex vivo system, not natural porcine HCM. (yadav2019phosphomimetic‐mediatedinvitro pages 8-10)

---

## 15. Model organisms and experimental systems

### Available models

1. **Patient-derived R58Q iPSC-cardiomyocytes:** reproduced cellular hypertrophy, disarray, calcium abnormalities, and irregular beating. Strength: human genetic background and direct patient relevance. Limitations: one patient, maternal rather than isogenic control, and immature iPSC-CM physiology. (zhou2019inducedpluripotentstem pages 4-7, zhou2019inducedpluripotentstem pages 8-9)
2. **Humanized transgenic mice:** R58Q, E22K, N47K, and other RLC variants have been expressed in mouse hearts to study relaxation, calcium sensitivity, force, phosphorylation, energetics, and remodeling. Strength: intact-organ physiology and longitudinal study. Limitations: species-specific myosin isoforms, heart rate, transgene dosage, and allele-specific phenotypic divergence. (yadav2019hereditaryheartdisease pages 1-2, dolder2025experimentalmodelsof pages 36-36)
3. **Reconstituted porcine papillary fibers/myosin:** permit controlled replacement with mutant or phosphomimetic RLC and direct force, ATPase, actin-binding, and SRX/DRX measurements. Limitation: lacks chronic cellular remodeling and systemic physiology. (yadav2019phosphomimetic‐mediatedinvitro pages 8-10)
4. **Human myectomy tissue:** validates hypertrophy, disarray, fibrosis, and—as emerging work suggests—variant-dependent myosin energetic states. Limitation: late-stage surgical tissue is biased toward severe disease.

### Best uses

These systems support variant classification, causal-mechanism testing, calcium/contractility assays, and preclinical evaluation of phosphorylation or myosin-modulating therapies. Future priorities are CRISPR-corrected isogenic iPSC pairs, engineered heart tissue with adult-like maturation, single-cell/spatial profiling, and allele-specific testing of myosin-inhibitor response.

---

## Knowledge-base conclusions

1. **Core assertion:** HCM10 is a rare, dominantly inherited, germline **MYL2** sarcomeric cardiomyopathy with incomplete, age- and context-dependent penetrance.
2. **Highest-confidence human genotype–phenotype links:** E22K founder disease strongly modified by hypertension/obesity/second variants; R58Q-associated apical HCM with cellular calcium and structural abnormalities; D166H-associated restrictive/AF-predominant familial disease. (bortoli2020novelmissensevariant pages 1-4, claes2016hypertrophicremodellingin pages 1-1, zhou2019inducedpluripotentstem pages 4-7)
3. **Mechanistic core:** altered RLC lever-arm regulation, phosphorylation, myosin-state equilibrium, force/ATPase kinetics, and calcium handling precede hypertrophy, disarray, fibrosis, diastolic dysfunction, and arrhythmia. Effects are **variant-specific**, so a universal “hypercontractility” mechanism should not be assigned uncritically. (yadav2019phosphomimetic‐mediatedinvitro pages 8-10)
4. **Clinical implementation:** diagnosis, risk stratification, treatment, and prevention currently follow 2023 ESC/2024 AHA/ACC HCM guidance; no MYL2-specific drug or validated genotype-only risk algorithm exists. (sanghvi2025hypertrophiccardiomyopathymanagement pages 14-15, ramonfaur2024eighteen‐monthreal‐worldexperience pages 12-12)
5. **Major gaps:** subtype-specific prevalence, incidence, lifetime penetrance, sex/ancestry effects, prospective natural history, quality-of-life estimates, treatment response, pharmacogenomics, single-cell/spatial omics, natural veterinary disease, and clinical gene/RNA therapy remain unavailable or inadequately studied.

References

1. (glavaski2023hypertrophiccardiomyopathygenetic pages 2-4): Mila Glavaški, Lazar Velicki, and Nataša Vučinić. Hypertrophic cardiomyopathy: genetic foundations, outcomes, interconnections, and their modifiers. Aug 2023. URL: https://doi.org/10.3390/medicina59081424, doi:10.3390/medicina59081424. This article has 48 citations.

2. (yadav2019hereditaryheartdisease pages 1-2): Sunil Yadav, Yoel H. Sitbon, Katarzyna Kazmierczak, and Danuta Szczesna-Cordary. Hereditary heart disease: pathophysiology, clinical presentation, and animal models of hcm, rcm, and dcm associated with mutations in cardiac myosin light chains. Pflügers Archiv - European Journal of Physiology, 471:683-699, Jan 2019. URL: https://doi.org/10.1007/s00424-019-02257-4, doi:10.1007/s00424-019-02257-4. This article has 50 citations.

3. (claes2016hypertrophicremodellingin pages 1-1): Godelieve R.F. Claes, Florence H.J. van Tienen, Patrick Lindsey, Ingrid P.C. Krapels, Apollonia T.J.M. Helderman-van den Enden, Marije B. Hoos, Yvette E.G. Barrois, Johanna W.H. Janssen, Aimée D.C. Paulussen, Jan-Willem E.M. Sels, Simone H.H. Kuijpers, J. Peter van Tintelen, Maarten P. van den Berg, Wilfred F. Heesen, Pablo Garcia-Pavia, Andreas Perrot, Imke Christiaans, Simone Salemink, Carlo L.M. Marcelis, Hubert J.M. Smeets, Han G. Brunner, Paul G.A. Volders, and Arthur van den Wijngaard. Hypertrophic remodelling in cardiac regulatory myosin light chain (myl2) founder mutation carriers. European heart journal, 37 23:1815-22, Jun 2016. URL: https://doi.org/10.1093/eurheartj/ehv522, doi:10.1093/eurheartj/ehv522. This article has 95 citations and is from a highest quality peer-reviewed journal.

4. (claes2016hypertrophicremodellingin pages 4-5): Godelieve R.F. Claes, Florence H.J. van Tienen, Patrick Lindsey, Ingrid P.C. Krapels, Apollonia T.J.M. Helderman-van den Enden, Marije B. Hoos, Yvette E.G. Barrois, Johanna W.H. Janssen, Aimée D.C. Paulussen, Jan-Willem E.M. Sels, Simone H.H. Kuijpers, J. Peter van Tintelen, Maarten P. van den Berg, Wilfred F. Heesen, Pablo Garcia-Pavia, Andreas Perrot, Imke Christiaans, Simone Salemink, Carlo L.M. Marcelis, Hubert J.M. Smeets, Han G. Brunner, Paul G.A. Volders, and Arthur van den Wijngaard. Hypertrophic remodelling in cardiac regulatory myosin light chain (myl2) founder mutation carriers. European heart journal, 37 23:1815-22, Jun 2016. URL: https://doi.org/10.1093/eurheartj/ehv522, doi:10.1093/eurheartj/ehv522. This article has 95 citations and is from a highest quality peer-reviewed journal.

5. (bortoli2020novelmissensevariant pages 1-4): Marzia De Bortoli, Riccardo Vio, Cristina Basso, Martina Calore, Giovanni Minervini, Annalisa Angelini, Paola Melacini, Libero Vitiello, Giovanni Vazza, Gaetano Thiene, Silvio Tosatto, Domenico Corrado, Sabino Iliceto, Alessandra Rampazzo, and Chiara Calore. Novel missense variant in <i>myl2</i> gene associated with hypertrophic cardiomyopathy showing high incidence of restrictive physiology. Circulation: Genomic and Precision Medicine, Apr 2020. URL: https://doi.org/10.1161/circgen.119.002824, doi:10.1161/circgen.119.002824. This article has 23 citations.

6. (bortoli2020novelmissensevariant pages 4-7): Marzia De Bortoli, Riccardo Vio, Cristina Basso, Martina Calore, Giovanni Minervini, Annalisa Angelini, Paola Melacini, Libero Vitiello, Giovanni Vazza, Gaetano Thiene, Silvio Tosatto, Domenico Corrado, Sabino Iliceto, Alessandra Rampazzo, and Chiara Calore. Novel missense variant in <i>myl2</i> gene associated with hypertrophic cardiomyopathy showing high incidence of restrictive physiology. Circulation: Genomic and Precision Medicine, Apr 2020. URL: https://doi.org/10.1161/circgen.119.002824, doi:10.1161/circgen.119.002824. This article has 23 citations.

7. (zhou2019inducedpluripotentstem pages 4-7): Wei Zhou, J. Martijn Bos, Dan Ye, David J. Tester, Sybil Hrstka, Joseph J. Maleszewski, Steve R. Ommen, Rick A. Nishimura, Hartzell V. Schaff, Chang Sung Kim, and Michael J. Ackerman. Induced pluripotent stem cell–derived cardiomyocytes from a patient with myl2-r58q-mediated apical hypertrophic cardiomyopathy show hypertrophy, myofibrillar disarray, and calcium perturbations. Journal of Cardiovascular Translational Research, pages 1-10, Feb 2019. URL: https://doi.org/10.1007/s12265-019-09873-6, doi:10.1007/s12265-019-09873-6. This article has 57 citations and is from a peer-reviewed journal.

8. (zhou2019inducedpluripotentstem pages 8-9): Wei Zhou, J. Martijn Bos, Dan Ye, David J. Tester, Sybil Hrstka, Joseph J. Maleszewski, Steve R. Ommen, Rick A. Nishimura, Hartzell V. Schaff, Chang Sung Kim, and Michael J. Ackerman. Induced pluripotent stem cell–derived cardiomyocytes from a patient with myl2-r58q-mediated apical hypertrophic cardiomyopathy show hypertrophy, myofibrillar disarray, and calcium perturbations. Journal of Cardiovascular Translational Research, pages 1-10, Feb 2019. URL: https://doi.org/10.1007/s12265-019-09873-6, doi:10.1007/s12265-019-09873-6. This article has 57 citations and is from a peer-reviewed journal.

9. (yadav2019phosphomimetic‐mediatedinvitro pages 8-10): Sunil Yadav, Katarzyna Kazmierczak, Jingsheng Liang, Yoel H. Sitbon, and Danuta Szczesna‐Cordary. Phosphomimetic‐mediated in vitro rescue of hypertrophic cardiomyopathy linked to r58q mutation in myosin regulatory light chain. The FEBS Journal, 286:151-168, Dec 2019. URL: https://doi.org/10.1111/febs.14702, doi:10.1111/febs.14702. This article has 42 citations.

10. (sanghvi2025hypertrophiccardiomyopathymanagement pages 14-15): Mihir M Sanghvi, Eamon Dhall, C Anwar A. Chahal, Constantinos O'Mahony, Saidi A Mohiddin, Konstantinos Savvatis, Fabrizio Ricci, Patricia B Munroe, Steffen E Petersen, Nay Aung, and Mohammed Y Khanji. Hypertrophic cardiomyopathy management: a systematic review of the clinical practice guidelines and recommendations. European heart journal. Quality of care & clinical outcomes, Jan 2025. URL: https://doi.org/10.1093/ehjqcco/qcae117, doi:10.1093/ehjqcco/qcae117. This article has 16 citations.

11. (ramonfaur2024eighteen‐monthreal‐worldexperience pages 12-12): Diego Ramonfaur, Alessio Gasperetti, Victoria E. Blake, Bryana Rivers, Ali A. Kassamali, Edward K. Kasper, Lili A. Barouch, Katherine C. Wu, Jose A. Madrazo, and Richard T. Carrick. Eighteen‐month real‐world experience using mavacamten for treatment of obstructive hypertrophic cardiomyopathy in a racially diverse population. Aug 2024. URL: https://doi.org/10.1161/jaha.123.034069, doi:10.1161/jaha.123.034069. This article has 33 citations.

12. (hao2026hypertrophiccardiomyopathycomprehensive pages 8-9): Luwen Hao, Xin Chen, and Bo Qin. Hypertrophic cardiomyopathy: comprehensive insights into pathogenic genes and genotype-phenotype associations. Frontiers in Cell and Developmental Biology, Jan 2026. URL: https://doi.org/10.3389/fcell.2026.1741252, doi:10.3389/fcell.2026.1741252. This article has 1 citations.

13. (dolder2025experimentalmodelsof pages 36-36): Floor W. van den Dolder, Rafeeh Dinani, Vincent A.J. Warnaar, Sofija Vučković, Adriana S. Passadouro, Ali A. Nassar, Azhaar X. Ramsaroep, George B. Burchell, Linda J. Schoonmade, Jolanda van der Velden, and Birgit Goversen. Experimental models of hypertrophic cardiomyopathy. JACC: Basic to Translational Science, 10:511-546, Jan 2025. URL: https://doi.org/10.1016/j.jacbts.2024.10.017, doi:10.1016/j.jacbts.2024.10.017. This article has 12 citations.

14. (kasiakogias2025exploringthecurrent pages 10-11): Alexandros Kasiakogias, Christos Kaskoutis, Christos-Konstantinos Antoniou, Stavros Georgopoulos, Dimitrios Tsiachris, Petros Arsenos, Alexandrina Kouroutzoglou, Dimitrios Klettas, Charalambos Vlachopoulos, Konstantinos Tsioufis, and Konstantinos Gatzoulis. Exploring the current status of risk stratification in hypertrophic cardiomyopathy: from risk models to promising techniques. Mar 2025. URL: https://doi.org/10.3390/jcdd12030101, doi:10.3390/jcdd12030101. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](Hypertrophic_Cardiomyopathy_10-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 6 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012112` (3 mentions) - the report calls it "if available"; MONDO calls it **hypertrophic cardiomyopathy 10**
- `HP:0005110` (1 mention) - the report calls it "D166H family: **62%**, approximately three times the rate cited for general HCM. Episodic or persistent"; HP calls it **Atrial fibrillation**
- `HP:0001698` (1 mention) - the report calls it "Common in generic HCM but absent in the reported D166H family"; HP calls it **Pericardial effusion**
- `GO:0030017` (1 mention) - the report calls it "GO cellular component:** sarcomere"; GO calls it **sarcomere**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0060048` (1 mention) - the report calls it "GO biological process:** cardiac muscle contraction"; GO calls it **cardiac muscle contraction**
- `CL:0000746` (1 mention) - the report calls it "Cell Ontology:** cardiac muscle cell/cardiomyocyte"; CL calls it **cardiac muscle cell**
