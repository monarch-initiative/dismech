---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T10:08:20.803880'
end_time: '2026-09-01T10:16:19.842593'
duration_seconds: 479.04
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth disease dominant intermediate G (CMTDIG), caused
    by heterozygous NEFL variants
  mondo_id: MONDO:0036484
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 33
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0036484
    reported_labels:
    - if available
    - MONDO
    ontology_label: Charcot-Marie-Tooth disease, dominant intermediate G
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Charcot-Marie-Tooth_Disease_Dominant_Intermediate_G-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth disease dominant intermediate G (CMTDIG), caused by heterozygous NEFL variants
- **MONDO ID:** MONDO:0036484 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth disease dominant intermediate G (CMTDIG), caused by heterozygous NEFL variants** covering all of the
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
- **Disease Name:** Charcot-Marie-Tooth disease dominant intermediate G (CMTDIG), caused by heterozygous NEFL variants
- **MONDO ID:** MONDO:0036484 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth disease dominant intermediate G (CMTDIG), caused by heterozygous NEFL variants** covering all of the
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


# Charcot–Marie–Tooth disease, dominant intermediate G (CMTDIG)

## Executive summary and evidence scope

CMTDIG is an ultrarare, autosomal-dominant hereditary sensorimotor neuropathy caused by a heterozygous pathogenic variant in **NEFL**, which encodes neurofilament light chain (NF-L). Its defining “intermediate” physiology lies between conventionally demyelinating and axonal CMT. Importantly, NEFL disease is a continuous allelic spectrum: reports may label patients **CMTDIG/dominant-intermediate CMT G**, **CMT1F**, or **CMT2E** according to nerve-conduction findings rather than a sharp biological boundary. MONDO:0036484 is directly associated with NEFL in aggregated disease-target evidence. (OpenTargets Search: Charcot-Marie-Tooth disease dominant intermediate G-NEFL, medina2024customizedantisenseoligonucleotidebased pages 1-2, marina2024novelgeneticand pages 1-3)

The strongest CMTDIG-like primary evidence is a multigenerational family with heterozygous **NEFL c.1189G>A, p.Glu397Lys (E397K)**, intermediate-to-demyelinating conduction velocities, axonal loss, and secondary demyelinating pathology. Most recent mechanistic work instead uses the severe p.Asn98Ser (N98S) CMT2E model; those findings are biologically relevant to dominant NEFL neuropathy but are not automatically variant-specific evidence for p.Glu397Lys. (zuchner2004thenovelneurofilament pages 1-2, zuchner2004thenovelneurofilament pages 6-7, marina2024novelgeneticand pages 1-3)

| Domain | Best-supported finding | Evidence type/sample | Key quantitative detail | Confidence/limitation |
|---|---|---|---|---|
| Disease identity | CMTDIG is the dominant-intermediate NEFL-associated CMT entity and overlaps clinically/genetically with NEFL-related CMT1F and CMT2E classifications rather than forming a sharply isolated syndrome | Disease-target aggregation plus review/cohort synthesis | MONDO:0036484 linked to NEFL; review notes NEFL variants cause demyelinating, axonal, and intermediate CMT forms; NF-related CMT accounts for ~1% of diagnosed CMT cases (OpenTargets Search: Charcot-Marie-Tooth disease dominant intermediate G-NEFL, marina2024novelgeneticand pages 1-3) | Moderate confidence; nomenclature is stable but human reports often classify the same NEFL families as CMT1F, CMT2E, or intermediate depending on conduction/pathology |
| Foundational human family | Heterozygous NEFL p.Glu397Lys was reported in a multigenerational family with autosomal dominant, clinically heterogeneous neuropathy in the intermediate/demyelinating range | Human clinical family study; 3 generations, 6 mutation carriers/affected relatives described (zuchner2004thenovelneurofilament pages 1-2, zuchner2004thenovelneurofilament pages 6-7) | Variant absent in 65 controls; by 2004, 11 NEFL mutations affecting 8 amino acids had been reported, ~2% of 323 CMT cases screened (zuchner2004thenovelneurofilament pages 1-2, zuchner2004thenovelneurofilament pages 7-10) | High confidence for this family; low generalizability because subtype-specific literature is sparse and older |
| 2024 variant landscape | Modern literature synthesis reports a broader NEFL disease spectrum with mostly heterozygous missense variants acting through gain-of-function mechanisms; somatic mosaicism can also be pathogenic | 2024 retrospective case study + literature review | 34 distinct CMT-causing NEFL variants in 174 reported patients; first reported pathogenic somatic NEFL mosaicism at 15% for p.Pro8Ser father (marina2024novelgeneticand pages 1-3, marina2024novelgeneticand pages 18-19) | High confidence for counts at publication date; counts will change as new cases accumulate |
| Core phenotypes / natural history | NEFL-related CMT commonly causes distal-predominant sensorimotor neuropathy with foot deformity and variable onset/severity; severe alleles can produce early-onset multisystem neuromuscular phenotypes | Human family studies | p.Glu397Lys family: onset ranged from age 4 to 82 years, with two clinically/electrophysiologically healthy carriers at age 21; severe family with NEFL nonsense variant had 4 affected members, infantile hypotonia, contractures, scoliosis, wheelchair dependence, and one death at 35 years likely from respiratory insufficiency (zuchner2004thenovelneurofilament pages 6-7, agrawal2014expandingthephenotype pages 3-4, agrawal2014expandingthephenotype pages 4-5) | High confidence for variable expressivity and age-dependent/incomplete penetrance; phenotype frequencies across CMTDIG specifically are unavailable |
| Electrophysiology and pathology | Dominant-intermediate labeling is supported by slowed motor conduction plus mixed axonal-demyelinating nerve pathology | Human electrophysiology and sural nerve biopsy | Motor NCVs in reported NEFL family ranged 27–43 m/s; peroneal NCV 25–27 m/s in some subjects; myelin area 12–16% versus ~23% normal; onion bulbs, loss of large myelinated fibers, atrophic axons, regenerated clusters (zuchner2004thenovelneurofilament pages 1-2, zuchner2004thenovelneurofilament pages 6-7, zuchner2004thenovelneurofilament pages 7-10) | High confidence in family-level evidence; pathology is based on very small numbers and may not represent all NEFL variants |
| Mechanism / pathophysiology | Pathogenic NEFL variants disrupt neurofilament assembly/organization, axonal caliber, intracellular transport, and likely axon-Schwann-cell interactions; some effects are modulated by post-translational regulation such as O-GlcNAcylation | Cell biology, review synthesis, and inference from human pathology | Neurofilament assembly defect and organelle transport disruption highlighted in 2024 review; 2023 O-GlcNAc study identified 5 NF-L O-GlcNAc sites and showed mutant NF-L can resist O-GlcNAc effects on assembly; severe NCV slowing may reflect axon/axonal-caliber loss and secondary demyelination (marina2024novelgeneticand pages 1-3, medina2024molecularphenotypicanalysisa pages 30-35) | Moderate confidence; aggregation/assembly defects are demonstrated in models, while the precise causal link to each human phenotype remains partly inferred |
| Model organisms and human cellular models | N98S is the best-developed experimental NEFL model, reproducing inclusion pathology and axonal structural abnormalities; patient iPSC-derived motor neurons recapitulate disease-relevant biomarkers | Knock-in mouse and patient-derived iPSC motor neuron models | NeflN98S/+ mice showed tremor, hindlimb clasping, inclusions in spinal neurons, abnormalities by postnatal day 7, fewer neurofilaments, more microtubules, and reduced axonal diameters; P8R mice were behaviorally similar to wild type (feliciano2021allelespecificgeneediting pages 1-3, marina2024novelgeneticand pages 1-3) | High confidence for N98S model validity; model findings may not extrapolate to all NEFL variants or specifically to p.Glu397Lys/CMTDIG |
| Experimental therapy | Allele-preferential ASO therapy is the most advanced NEFL-targeted approach currently gathered, with biomarker rescue in a preclinical human model | 2024 preclinical therapeutic study in patient iPSC-derived motor neurons | ASO produced ~20% reduction of mutant p.N98S allele expression and ~38% reduction of total NEFL transcript, with decreased supernatant NF-L and peripherin biomarkers (medina2024customizedantisenseoligonucleotidebased pages 11-12) | Moderate confidence; strong proof-of-concept but not yet human clinical efficacy or safety data for NEFL/CMTDIG |
| Diagnostics | Diagnosis currently depends on clinical neuropathy assessment plus molecular testing, with WGS improving but not replacing phenotype-driven workflows | Specialist-center cohort and hereditary neuropathy testing studies | In a 1515-patient inherited neuropathy center cohort, intermediate CMT accounted for 205/1515 (13.5%) and had 81.0% genetic diagnosis; overall diagnostic rate 76.9%, WGS diagnostic uplift 3.5%, true 100KGP WGS rate 19.7% (46/233) (marina2024novelgeneticand pages 1-3) | Moderate confidence for general CMT diagnostics; no CMTDIG-specific diagnostic algorithm validated beyond identifying heterozygous NEFL variants via panels/WES/WGS |
| Treatment gap / current care | No disease-modifying therapy specific to NEFL-related CMTDIG was identified; present real-world management is supportive, while NEFL-targeted precision therapy remains preclinical | Evidence gap plus broader CMT practice context | Clinical trial searches retrieved broader CMT studies but no NEFL/CMTDIG-specific interventional trial; customized ASO remains preclinical proof-of-concept (medina2024customizedantisenseoligonucleotidebased pages 11-12) | High confidence for current treatment gap; limitation is absence of subtype-specific management trials and sparse published QoL/outcome data |


*Table: This table summarizes the strongest currently gathered evidence for NEFL-related dominant-intermediate Charcot-Marie-Tooth disease and overlapping NEFL neuropathies. It is calibrated to separate well-supported family/model findings from areas where evidence remains sparse or indirect.*

## 1. Disease information

### Definition and classification

CMTDIG is a chronic, usually slowly progressive, inherited peripheral neuropathy characterized by length-dependent distal weakness and wasting, foot deformity, depressed reflexes, and variable sensory loss. “Intermediate” generally denotes motor nerve-conduction velocities (MNCVs) between classic demyelinating and axonal ranges; NEFL families may cross those thresholds within the same pedigree. In the p.Glu397Lys family, lower-limb MNCVs ranged approximately **27–43 m/s**, and some peroneal values were **25–27 m/s**. Biopsy nevertheless showed both chronic axonopathy and demyelination/remyelination. (zuchner2004thenovelneurofilament pages 1-2, zuchner2004thenovelneurofilament pages 6-7, zuchner2004thenovelneurofilament pages 7-10)

### Identifiers and synonyms

- **MONDO:** [MONDO:0036484](https://monarchinitiative.org/disease/MONDO:0036484), *Charcot-Marie-Tooth disease, dominant intermediate G*.
- **EFO:** EFO:0010267, *autosomal dominant intermediate Charcot-Marie-Tooth disease type G*. (OpenTargets Search: Charcot-Marie-Tooth disease dominant intermediate G-NEFL)
- **Common names:** CMTDIG; dominant-intermediate CMT type G; DI-CMTG; DICMTG; autosomal dominant intermediate CMT type G; NEFL-related dominant-intermediate neuropathy.
- **Overlapping labels:** NEFL-related CMT2E and CMT1F. These should be retained as related entities rather than treated as exact synonyms in every patient.
- **OMIM:** NEFL-related classifications are commonly represented within the NEFL/CMT2E–CMT1F allelic spectrum; an exact CMTDIG OMIM number was not securely verified in the retrieved evidence and should not be populated without direct OMIM confirmation.
- **ICD-10-CM:** no subtype-specific code; typically **G60.0**, hereditary motor and sensory neuropathy.
- **ICD-11:** hereditary motor and sensory neuropathy/CMT category; no independently validated CMTDIG leaf code found.
- **MeSH:** *Charcot-Marie-Tooth Disease*; no NEFL/CMTDIG-specific MeSH descriptor found.

The evidence is **aggregated disease-level literature and family/cohort research**, not individual EHR data. OpenTargets aggregates five evidence records connecting MONDO:0036484 to NEFL. (OpenTargets Search: Charcot-Marie-Tooth disease dominant intermediate G-NEFL)

## 2. Etiology

### Causal factor

The cause is a **germline heterozygous pathogenic NEFL variant**, most often missense. Dominant variants generally act through toxic gain-of-function and/or dominant interference with neurofilament assembly, rather than simple haploinsufficiency. Heterozygous loss-of-function carriers can be neurologically normal, whereas biallelic loss-of-function causes an earlier recessive phenotype. (medina2024molecularphenotypicanalysis pages 13-17, feliciano2021allelespecificgeneediting pages 1-3, marina2024novelgeneticand pages 1-3)

The canonical CMTDIG-like p.Glu397Lys variant alters a highly conserved LLEGEE motif near the end of the coiled-coil rod domain. It segregated across three generations and was absent from 65 controls. (zuchner2004thenovelneurofilament pages 6-7, zuchner2004thenovelneurofilament pages 7-10)

### Risk factors

- **Genetic:** an affected parent or a de novo pathogenic NEFL allele; variant position and biochemical effect influence onset. Head-domain variants tend to present earlier, although this is not an absolute rule. (marina2024novelgeneticand pages 1-3, marina2024novelgeneticand pages 18-19)
- **Family history:** strongly informative under autosomal-dominant inheritance, but a negative history does not exclude de novo variation, age-dependent penetrance, or mosaicism.
- **Somatic mosaicism:** a 2024 report identified **15% mosaic p.Pro8Ser** in a mildly affected father, establishing that low-level mosaic NEFL variation can be clinically relevant. (marina2024novelgeneticand pages 1-3, marina2024novelgeneticand pages 18-19)
- **Trauma:** experimental work suggests nerve injury can aggravate an NEFL neuropathy phenotype, but this is not established as a population-level cause or risk estimate.

No reproducible susceptibility loci, modifier genes, sex-specific risk, infectious causes, or environmental causes have been established for CMTDIG.

### Protective factors and gene–environment interaction

No validated protective allele, diet, drug, or exposure has been demonstrated. Avoidance of neurotoxic medications, excessive alcohol, repetitive nerve compression, and preventable trauma is clinically prudent for inherited neuropathy, but is tertiary risk reduction—not prevention of the genetic disease. The nutrient-sensitive O-GlcNAc regulation of NF-L is a plausible molecular interface with cellular metabolism, but no human diet–NEFL interaction has been shown.

## 3. Phenotypes

Frequency estimates below are qualitative because no sufficiently large CMTDIG-specific natural-history cohort exists.

- **Distal lower-limb weakness and wasting** — core sign, usually symmetric and progressive; **HP:0009053** (distal lower-limb muscle weakness), **HP:0003693** (distal amyotrophy).
- **Foot drop and gait impairment** — common; can begin in childhood; **HP:0003376**, **HP:0001288**.
- **Pes cavus/other foot deformity** — frequent presenting manifestation; in one carrier it was apparent by age four; **HP:0001761**, **HP:0001839**.
- **Distal sensory loss or sensory ataxia** — variable and sometimes mild; one p.Glu397Lys subject presented prominently with sensory ataxia; **HP:0000763**, **HP:0002066**.
- **Hyporeflexia/areflexia** — expected in length-dependent neuropathy; **HP:0001265**, **HP:0001284**.
- **Reduced motor NCV** — intermediate or occasionally demyelinating range; **HP:0003431**. Sensory responses may be relatively preserved. (zuchner2004thenovelneurofilament pages 6-7)
- **Hearing impairment/deafness** — reported in the p.Glu397Lys family, including an 82-year-old with deafness and only minor neuropathy; frequency unknown; **HP:0000365**. (zuchner2004thenovelneurofilament pages 6-7, zuchner2004thenovelneurofilament pages 1-2)
- **Contractures, scoliosis, facial weakness, ptosis, shoulder weakness, respiratory impairment** — documented in a severe heterozygous NEFL nonsense-variant family, not established as typical CMTDIG features; suggested terms include **HP:0001371**, **HP:0002650**, **HP:0002058**, **HP:0000508**, and **HP:0002093**. Four relatives had infantile hypotonia, delayed milestones, progressive contractures and scoliosis; wheelchair dependence ranged from adolescence to the mid-50s, and one died at 35, probably from respiratory insufficiency. (agrawal2014expandingthephenotype pages 3-4, agrawal2014expandingthephenotype pages 4-5)
- **Muscle pathology:** usually secondary denervation, but primary muscle vulnerability is possible. A 2024 p.Phe104Val case had weakness, myalgia, cramps, Z-band changes and mini-cores; proteomics implicated cytoskeletal proteins. (marina2024novelgeneticand pages 1-3)

No behavioral or psychiatric phenotype is characteristic. Quality-of-life data specific to CMTDIG are unavailable. Functionally, foot drop, balance impairment, hand weakness in later disease, contractures, and fatigue can impair walking, falls risk, employment, self-care, and participation.

## 4. Genetic and molecular information

- **Gene:** **NEFL**, neurofilament light chain; approved human protein-coding gene, chromosome 8p21 region; Ensembl target **ENSG00000277586** in the retrieved aggregation. (OpenTargets Search: Charcot-Marie-Tooth disease dominant intermediate G-NEFL)
- **Inheritance/origin:** usually autosomal-dominant germline; de novo and somatic-mosaic cases are possible.
- **Variant spectrum:** by April 2024, **34 CMT-causing NEFL variants in 174 reported patients** had been compiled. Variants produce demyelinating, axonal, and intermediate phenotypes. (marina2024novelgeneticand pages 1-3)
- **Important dominant variants:** p.Glu397Lys for the intermediate phenotype; p.Asn98Ser, p.Pro8Arg/Ser/Leu, p.Pro22Ser/Thr, and others across head and rod domains. More than 30 pathogenic variants have been reported in modern CMT2E summaries. (medina2024customizedantisenseoligonucleotidebased pages 1-2, marina2024novelgeneticand pages 1-3, medina2024molecularphenotypicanalysisa pages 30-35)
- **Classes:** predominantly missense; rare nonsense/truncating alleles and recessive loss-of-function are reported. Variant interpretation must therefore consider inheritance and mechanism rather than assuming every NEFL loss-of-function allele causes dominant disease.
- **Population frequency:** pathogenic dominant alleles are expected to be absent or extremely rare in population databases. Exact current gnomAD allele counts were not available from the retrieved documents and should be queried variant-by-variant using the correct transcript/build.
- **Classification:** clinical laboratories should apply ACMG/AMP criteria using segregation, de novo status, population rarity, domain/hotspot evidence, phenotype, functional data, and ClinVar assertions. Variant-specific classification may differ; an NEFL VUS alone is not diagnostic.
- **Mechanism:** dominant toxic gain-of-function/dominant interference; simple haploinsufficiency is unlikely for many dominant missense disorders. (medina2024customizedantisenseoligonucleotidebased pages 11-12, feliciano2021allelespecificgeneediting pages 1-3)
- **Modifiers/epigenetics/chromosomal abnormalities:** no validated modifier gene, disease-specific methylation signature, recurrent copy-number lesion, translocation, or inversion is established.

## 5. Environmental information

CMTDIG is not caused by toxin, lifestyle, radiation, pollution, or infection. Environmental exposures may change functional reserve or aggravate symptoms but do not replace the Mendelian cause. No CMTDIG-specific data quantify effects of smoking, diet, alcohol, exercise, occupation, or infection. Exercise should be individualized to maintain strength and conditioning without overuse injury. There is no zoonotic or infectious transmission.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous pathogenic **NEFL** variant **leads to** altered NF-L structure, stoichiometry, or post-translational regulation.
2. Altered NF-L **leads to** defective neurofilament coiled-coil assembly, network organization, and—in many model systems—abnormal accumulation or aggregation.
3. Neurofilament disorganization **results in** disturbed axonal cytoskeletal architecture, organelle transport, and radial axonal growth.
4. Reduced axonal caliber and axonal dysfunction **lead to** impaired impulse conduction and length-dependent degeneration of long motor and sensory axons.
5. Axonal degeneration **results in** denervation, distal muscle atrophy, weakness, foot deformity, sensory loss, and reduced reflexes.
6. **Inferred branch:** disturbed axon–Schwann-cell signaling **leads to** secondary demyelination/remyelination, onion bulbs, and conduction velocities in the intermediate or demyelinating range.
7. **Variant-dependent branch:** severe alleles **may lead to** broader neuronal, muscular, auditory, or respiratory involvement.

### Molecular and cellular detail

NF-L monomers form coiled-coil dimers, nonpolar tetramers, unit-length filaments, and mature neurofilaments. Neurofilaments provide axonal mechanical stability, regulate radial growth and caliber, interact with microtubules, and help organize organelles and synaptic function. Relevant processes include **GO:0005882 intermediate filament**, **GO:0045109 intermediate filament organization**, **GO:0031175 neuron projection development**, **GO:0008088 axonal transport**, and **GO:0007411 axon guidance**. (medina2024customizedantisenseoligonucleotidebased pages 1-2, medina2024molecularphenotypicanalysisa pages 30-35)

Phosphorylation at NF-L head-domain residues—including Ser2, Ser55, Ser57 and Ser66—regulates severing, annealing and transport; some Pro22 substitutions abolish normal head-domain phosphorylation. (medina2024molecularphenotypicanalysisa pages 30-35)

A major 2023 development showed that NF-L is modified at **five O-GlcNAc sites**. O-GlcNAcylation regulated neurofilament assembly and NF-L interactions with itself and α-internexin, and was required for normal organelle trafficking in primary neurons. Several CMT-causing mutants had abnormal O-GlcNAc levels or resisted O-GlcNAc-dependent assembly effects. The authors’ key abstract conclusion was: **“aberrant NF O-GlcNAcylation may contribute to CMT and other neurodegenerative disorders.”** This is mechanistically compelling but not yet a patient biomarker or treatment target. Huynh et al., *Nature Communications* 2023, DOI: [10.1038/s41467-023-42227-0](https://doi.org/10.1038/s41467-023-42227-0).

Human nerve pathology shows loss of large myelinated fibers, axonal atrophy, regeneration clusters, and onion bulbs. Myelin area in studied p.Glu397Lys biopsies was approximately **12–16%**, versus about **23% normal**. These observations support primary axonopathy with secondary myelin injury rather than a purely Schwann-cell-autonomous disorder. (zuchner2004thenovelneurofilament pages 6-7, zuchner2004thenovelneurofilament pages 7-10)

**Cells:** motor neuron (**CL:0000100**), sensory neuron (**CL:0000101**), peripheral-neuron axon, Schwann cell (**CL:0002573**), and secondarily skeletal muscle fiber (**CL:0000188**). No convincing NEFL-specific immune, apoptotic, metabolic, lipidomic, single-cell, spatial-transcriptomic, or epigenomic disease program has been validated in humans.

## 7. Anatomical structures affected

- **Primary system:** peripheral nervous system; long motor and sensory nerves (**UBERON:0000010 nervous system**, **UBERON:0000381 peripheral nervous system**).
- **Principal sites:** distal lower-limb nerves and muscles first; later distal upper limbs in some patients. Involvement is usually bilateral and approximately symmetric.
- **Axonal compartments:** axoplasm and neurofilament cytoskeleton; **GO:0030424 axon**, **GO:0043209 myelin sheath**, **GO:0005882 intermediate filament**.
- **Secondary tissues:** Schwann-cell/myelin units and denervated skeletal muscle (**UBERON:0001630 muscle organ**).
- **Model-dependent CNS sites:** spinal cord, cerebellum, cortex and pons show abnormalities in N98S mice, but clinically important CNS disease is not established as a universal CMTDIG feature.

## 8. Temporal development

Onset is typically insidious and may occur from early childhood through adulthood. The p.Glu397Lys pedigree ranged from foot deformity at **age 4** to very mild neuropathy/deafness at **age 82**; two carriers were clinically and electrophysiologically normal at 21. This demonstrates age-dependent or incomplete penetrance and marked intrafamilial variability. (zuchner2004thenovelneurofilament pages 6-7, zuchner2004thenovelneurofilament pages 1-2, zuchner2004thenovelneurofilament pages 7-10)

The usual course is chronic, lifelong and slowly progressive, without spontaneous remission. Early disease often consists of pes cavus, ankle weakness or foot drop; intermediate disease adds distal wasting, gait impairment and sensory loss; advanced cases may require orthoses, walking aids, orthopedic procedures, or a wheelchair. These are pragmatic clinical phases, not validated CMTDIG staging criteria. No critical therapeutic window has been established in humans, although experimental ASO investigators argue that treatment before major axonal loss should offer the greatest benefit. (medina2024customizedantisenseoligonucleotidebased pages 11-12)

## 9. Inheritance and population

- **Inheritance:** autosomal dominant for CMTDIG; each child of a heterozygous germline carrier has a theoretical **50% transmission risk**.
- **Penetrance:** incomplete and/or age-dependent in at least some families.
- **Expressivity:** highly variable, even within one pedigree.
- **Anticipation:** not demonstrated.
- **Mosaicism:** documented; low-level parental mosaicism can alter recurrence counseling. (marina2024novelgeneticand pages 1-3, marina2024novelgeneticand pages 18-19)
- **Founder effects/consanguinity:** none established for dominant CMTDIG. Consanguinity is not a causal factor, although it matters for recessive NEFL disease.
- **Sex ratio:** no established sex bias; autosomal inheritance predicts both sexes can be affected.
- **Geography/ethnicity:** cases occur across populations; no reliable high-prevalence region is known.

CMT overall is often estimated at approximately **1 in 2,500**, but that figure must not be assigned to CMTDIG. Neurofilament-related CMT is estimated at roughly **1% of diagnosed CMT**, and CMTDIG itself is only a subset. No valid CMTDIG-specific incidence or prevalence per 100,000 is available. (medina2024customizedantisenseoligonucleotidebased pages 1-2, medina2024molecularphenotypicanalysisa pages 30-35)

## 10. Diagnostics

### Clinical and electrophysiological assessment

Diagnosis begins with a three-generation pedigree; neurologic examination for distal weakness/atrophy, pes cavus, sensory loss and reflex reduction; and nerve-conduction studies/EMG. Intermediate or discordant axonal–demyelinating findings should not exclude NEFL testing. The p.Glu397Lys study explicitly recommended considering NEFL beyond purely axonal CMT. (zuchner2004thenovelneurofilament pages 10-10, zuchner2004thenovelneurofilament pages 7-10)

Nerve or muscle biopsy is **not routinely required** after a molecular diagnosis. If performed for atypical disease, nerve pathology can show large-fiber loss, axonal atrophy, regenerative clusters and onion bulbs; muscle can show neurogenic atrophy and, rarely, nemaline rods or mini-cores. Serum creatine kinase may be normal even in severe NEFL neuromuscular disease. (agrawal2014expandingthephenotype pages 3-4, agrawal2014expandingthephenotype pages 4-5, agrawal2014expandingthephenotype pages 1-2)

### Genetic testing algorithm

1. Confirm a hereditary neuropathy phenotype and conduction category.
2. Exclude common **PMP22** duplication/deletion when clinically indicated.
3. Use a comprehensive inherited-neuropathy NGS panel that includes **NEFL** and major CMT genes.
4. If negative, proceed to trio WES or preferably WGS with copy-number, structural-variant, repeat, mitochondrial and noncoding analysis as appropriate.
5. Confirm a candidate variant by an orthogonal method, establish phase/segregation, and test parental blood for mosaicism when a variant appears de novo.
6. Interpret under ACMG/AMP criteria and correlate the variant’s mechanism with phenotype.

In a 2024 specialist-center series of **1,515** CMT-related patients, 205 (13.5%) had intermediate CMT; **81.0% (166/205)** received a genetic diagnosis. Overall yield was **76.9%**, while WGS added a **3.5% diagnostic uplift**; the true 100,000 Genomes Project WGS yield was **19.7% (46/233)** after accounting for diagnoses made elsewhere. These figures concern all CMT, not NEFL alone. Record et al., *Brain* 2024, DOI: [10.1093/brain/awae064](https://doi.org/10.1093/brain/awae064).

CMA, karyotyping and FISH have low yield for a typical single-gene phenotype unless a larger chromosomal lesion is suspected. Repeat-expansion and mitochondrial testing are differential-diagnosis tools, not direct NEFL assays. RNA-seq, proteomics and metabolomics remain research adjuncts.

### Differential diagnosis

Consider PMP22-related CMT1A/HNPP, GJB1-CMTX1, MPZ neuropathy, MFN2-CMT2A, other intermediate CMT genes, hereditary transthyretin amyloidosis, distal hereditary motor neuropathy, hereditary sensory neuropathy, hereditary spastic paraplegia, CIDP, toxic/metabolic neuropathy, Friedreich ataxia, and motor-neuron disease. Uniform familial slowing favors inherited CMT; conduction block, marked temporal dispersion, acute/subacute progression, systemic features or monoclonal protein should prompt evaluation for acquired neuropathy.

Asymptomatic relatives should receive pre-test genetic counseling. Predictive/cascade testing is appropriate only after a familial pathogenic/likely pathogenic variant is established; CMTDIG is not included in routine newborn screening.

## 11. Outcome and prognosis

Most dominant NEFL neuropathies are chronic and disabling rather than acutely lethal. There are no CMTDIG-specific 5- or 10-year survival estimates, mortality rates, or validated prognostic calculators. Life expectancy is likely near normal in mildly to moderately affected individuals, but this cannot be generalized to severe NEFL alleles. A severe four-person family included probable respiratory death at 35; that outlier should not be represented as typical CMTDIG prognosis. (agrawal2014expandingthephenotype pages 3-4)

Long-term morbidity includes gait limitation, falls, foot deformity, distal hand dysfunction, pain/cramps, contractures, scoliosis, fatigue and dependence on assistive devices. Axonal loss is generally irreversible; rehabilitation can preserve function and prevent secondary complications but does not restore lost axons. Prognosis is influenced by the specific allele, age at onset, baseline axonal loss, respiratory involvement, contractures and rate of progression. No validated molecular prognostic biomarker exists. Circulating or culture-supernatant NF-L and peripherin are promising pharmacodynamic markers, but in NEFL disease an NF-L assay may reflect both protein expression and injury, complicating interpretation. (medina2024customizedantisenseoligonucleotidebased pages 11-12)

## 12. Treatment

### Current clinical management

There is **no approved disease-modifying treatment specific to NEFL/CMTDIG**. Management is multidisciplinary and individualized:

- physical therapy, stretching, balance and low-impact aerobic conditioning (**NCIt: Physical Therapy**);
- occupational therapy and hand-function adaptations (**NCIt: Occupational Therapy**);
- ankle–foot orthoses, custom footwear, canes/walkers/wheelchairs (**NCIt: Orthopedic Device**);
- podiatry and orthopedic correction of rigid cavovarus deformity or contracture when conservative treatment fails (**NCIt: Orthopedic Surgery**);
- symptomatic treatment of neuropathic pain and cramps, with attention to sedation, cardiac risk and weakness;
- respiratory/sleep assessment for severe early-onset disease, scoliosis, morning headaches or sleep-disordered breathing;
- hearing evaluation where clinically indicated;
- avoidance, where alternatives exist, of medications with substantial peripheral-neurotoxicity.

No NEFL-specific pharmacogenomic guidance or response rate is available.

### 2023–2024 experimental developments

The leading precision strategy is suppression of the toxic mutant transcript while retaining sufficient wild-type NF-L. In 2024, Medina et al. used p.N98S patient-derived iPSC motor neurons and an RNase-H1-compatible allele-preferential ASO. Treatment reduced mutant expression by about **20%**, total NEFL transcript by **38%**, and decreased extracellular NF-L and peripherin injury markers. The abstract describes this as **“the first clinically viable genetic therapeutic for CMT2E,”** but “clinically viable” means a preclinical development strategy—not demonstrated human efficacy. *Brain*, published July 2024, DOI: [10.1093/brain/awae225](https://doi.org/10.1093/brain/awae225). (medina2024customizedantisenseoligonucleotidebased pages 11-12, medina2024customizedantisenseoligonucleotidebased pages 1-2)

Allele-specific gene editing has also rescued pathology in a human N98S model, supporting toxic-allele inactivation. Both approaches remain variant-dependent and face delivery, off-target, durability and wild-type dosage constraints. (feliciano2021allelespecificgeneediting pages 1-3)

No retrieved ClinicalTrials.gov study specifically tested an NEFL-targeted therapy in CMTDIG. Broader CMT trials cannot be assumed effective in this genotype. Cell therapy, immunotherapy and nonspecific anti-inflammatory therapy have no established CMTDIG role.

## 13. Prevention

Primary prevention by lifestyle or vaccination is impossible because the initiating lesion is genetic. Reproductive options after molecular confirmation include genetic counseling, prenatal diagnosis, and IVF with preimplantation genetic testing for monogenic disease. Counseling should cover 50% transmission risk, variable expressivity, age-dependent penetrance, de novo disease, and possible parental mosaicism.

Secondary prevention consists of cascade testing, early neurologic/orthopedic assessment, and timely orthoses or rehabilitation before fixed deformity. Tertiary prevention includes fall reduction, stretching to prevent contractures, skin and foot care for sensory loss, weight and cardiometabolic management, monitoring for respiratory/hearing complications when indicated, and avoidance of avoidable neurotoxic exposure. There is no population screening or prophylactic medication.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart specifically equivalent to human heterozygous NEFL-CMTDIG was identified. The disorder is not infectious or zoonotic and cannot be transmitted between species. Relevant orthologues include mouse **Nefl** in *Mus musculus* (**NCBI Taxonomy 10090**) and homologues in rat, zebrafish and other vertebrates. Neurofilament structure and axonal-caliber functions are evolutionarily conserved, which supports comparative modeling, but engineered model disease should not be coded as naturally occurring veterinary CMT without species-specific evidence.

## 15. Model organisms and experimental systems

### Mouse

The best-characterized model is heterozygous **Nefl N98S** knock-in mouse. It develops tremor and hindlimb clasping, neuronal inclusions in cell bodies/proximal axons, disorganized cerebellar processes, cortical and pontine abnormalities, and sciatic nerves with fewer neurofilaments, more microtubules and smaller axonal diameters. Abnormal processes were evident by **postnatal day 7**. In contrast, P8R heterozygous and homozygous mice were behaviorally indistinguishable from wild type, illustrating strong variant- and species-dependent effects. Adebola et al., *Human Molecular Genetics* 2015, DOI: [10.1093/hmg/ddu736](https://doi.org/10.1093/hmg/ddu736).

A p.Glu397Lys-proximal mouse mutation, Leu394Pro, did not reproduce human demyelination, possibly because lifespan or species biology was insufficient for secondary myelin pathology. (zuchner2004thenovelneurofilament pages 10-10)

### Cellular and human models

Transfected-cell systems demonstrate mutant-dependent filament-network abnormalities and aggregation, but overexpression can distort stoichiometry. Patient iPSC-derived motor neurons are more disease-relevant and reproduce N98S NF-L accumulation and axonal-injury biomarkers; they supported both allele-specific editing and ASO rescue. The main limitation is that cultured neurons do not fully reproduce decades-long axon–Schwann-cell interaction, biomechanics, immune context, or distal nerve length. (medina2024customizedantisenseoligonucleotidebased pages 11-12, feliciano2021allelespecificgeneediting pages 1-3)

Primary-neuron studies of O-GlcNAcylation and proposed future muscle organoids can dissect assembly, organelle transport and direct muscle vulnerability. No validated CMTDIG organoid, single-cell atlas, spatial-transcriptomic model, or high-throughput CRISPR modifier screen was identified. (marina2024novelgeneticand pages 1-3, marina2024novelgeneticand pages 18-19)

## Evidence-calibrated conclusions

1. **High confidence:** CMTDIG is a heterozygous NEFL neuropathy with dominant inheritance, marked variable expressivity, and mixed axonal/demyelinating physiology and pathology.
2. **High confidence:** p.Glu397Lys family evidence supports the intermediate designation through MNCVs, large-fiber axonal loss, onion bulbs and secondary myelin abnormalities. (zuchner2004thenovelneurofilament pages 1-2, zuchner2004thenovelneurofilament pages 6-7)
3. **Moderate-to-high confidence:** dominant variants perturb NF-L assembly, axonal caliber and intracellular transport; the contribution of aggregation and O-GlcNAc dysregulation varies by allele.
4. **High confidence:** current care is supportive; no NEFL/CMTDIG-targeted therapy has demonstrated clinical efficacy.
5. **Promising but preclinical:** allele-preferential ASO and gene editing can reduce N98S-associated pathology in human cellular models. (medina2024customizedantisenseoligonucleotidebased pages 11-12, feliciano2021allelespecificgeneediting pages 1-3)
6. **Major knowledge gaps:** CMTDIG-specific prevalence, incidence, penetrance by age, phenotype frequencies, longitudinal progression, quality-of-life statistics, circulating biomarker validation, genotype-specific treatment response, and human trial data remain unavailable.

### Key primary/recent sources

- Züchner S, et al. “The novel neurofilament light (NEFL) mutation Glu397Lys…” *Neuromuscular Disorders*. February 2004;14:147–157. **PMID: 14733962**. DOI: [10.1016/j.nmd.2003.10.003](https://doi.org/10.1016/j.nmd.2003.10.003). (zuchner2004thenovelneurofilament pages 1-2)
- Della Marina A, et al. “Novel Genetic and Biochemical Insights into the Spectrum of NEFL-Associated Phenotypes.” *Journal of Neuromuscular Diseases*. April 2024;11:625–645. DOI: [10.3233/JND-230230](https://doi.org/10.3233/JND-230230). (marina2024novelgeneticand pages 1-3)
- Huynh DT, et al. “O-GlcNAcylation regulates neurofilament-light assembly and function and is perturbed by Charcot-Marie-Tooth disease mutations.” *Nature Communications*. 2023;14. DOI: [10.1038/s41467-023-42227-0](https://doi.org/10.1038/s41467-023-42227-0).
- Medina J, et al. “Customized antisense oligonucleotide-based therapy for neurofilament-associated Charcot-Marie-Tooth disease.” *Brain*. July 2024;147:4227–4239. DOI: [10.1093/brain/awae225](https://doi.org/10.1093/brain/awae225). (medina2024customizedantisenseoligonucleotidebased pages 11-12)
- Adebola AA, et al. “Neurofilament light polypeptide gene N98S mutation in mice…” *Human Molecular Genetics*. April 2015;24:2163–2174. DOI: [10.1093/hmg/ddu736](https://doi.org/10.1093/hmg/ddu736).
- Agrawal PB, et al. “Expanding the phenotype associated with the NEFL mutation…” *JAMA Neurology*. November 2014;71:1413–1420. DOI: [10.1001/jamaneurol.2014.1432](https://doi.org/10.1001/jamaneurol.2014.1432). (agrawal2014expandingthephenotype pages 3-4, agrawal2014expandingthephenotype pages 1-2)

References

1. (OpenTargets Search: Charcot-Marie-Tooth disease dominant intermediate G-NEFL): Open Targets Query (Charcot-Marie-Tooth disease dominant intermediate G-NEFL, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (medina2024customizedantisenseoligonucleotidebased pages 1-2): Jessica Medina, Adriana Rebelo, Matt C Danzi, Elizabeth H Jacobs, Isaac R L Xu, Kathleen P Ahrens, Sitong Chen, Jacquelyn Raposo, Christopher Yanick, Stephan Zuchner, and Mario A Saporta. Customized antisense oligonucleotide-based therapy for neurofilament-associated charcot-marie-tooth disease. Brain : a journal of neurology, 147:4227-4239, Jul 2024. URL: https://doi.org/10.1093/brain/awae225, doi:10.1093/brain/awae225. This article has 9 citations.

3. (marina2024novelgeneticand pages 1-3): Adela Della Marina, Andreas Hentschel, Artur Czech, Ulrike Schara-Schmidt, Corinna Preusse, Andreas Laner, Angela Abicht, Tobias Ruck, Joachim Weis, Catherine Choueiri, Hanns Lochmüller, Heike Kölbel, and Andreas Roos. Novel genetic and biochemical insights into the spectrum of nefl-associated phenotypes. Journal of Neuromuscular Diseases, 11:625-645, Apr 2024. URL: https://doi.org/10.3233/jnd-230230, doi:10.3233/jnd-230230. This article has 12 citations and is from a peer-reviewed journal.

4. (zuchner2004thenovelneurofilament pages 1-2): Stephan Züchner, Matthias Vorgerd, Eckhart Sindern, and J.Michael Schröder. The novel neurofilament light (nefl) mutation glu397lys is associated with a clinically and morphologically heterogeneous type of charcot-marie-tooth neuropathy. Neuromuscular Disorders, 14:147-157, Feb 2004. URL: https://doi.org/10.1016/j.nmd.2003.10.003, doi:10.1016/j.nmd.2003.10.003. This article has 120 citations and is from a peer-reviewed journal.

5. (zuchner2004thenovelneurofilament pages 6-7): Stephan Züchner, Matthias Vorgerd, Eckhart Sindern, and J.Michael Schröder. The novel neurofilament light (nefl) mutation glu397lys is associated with a clinically and morphologically heterogeneous type of charcot-marie-tooth neuropathy. Neuromuscular Disorders, 14:147-157, Feb 2004. URL: https://doi.org/10.1016/j.nmd.2003.10.003, doi:10.1016/j.nmd.2003.10.003. This article has 120 citations and is from a peer-reviewed journal.

6. (zuchner2004thenovelneurofilament pages 7-10): Stephan Züchner, Matthias Vorgerd, Eckhart Sindern, and J.Michael Schröder. The novel neurofilament light (nefl) mutation glu397lys is associated with a clinically and morphologically heterogeneous type of charcot-marie-tooth neuropathy. Neuromuscular Disorders, 14:147-157, Feb 2004. URL: https://doi.org/10.1016/j.nmd.2003.10.003, doi:10.1016/j.nmd.2003.10.003. This article has 120 citations and is from a peer-reviewed journal.

7. (marina2024novelgeneticand pages 18-19): Adela Della Marina, Andreas Hentschel, Artur Czech, Ulrike Schara-Schmidt, Corinna Preusse, Andreas Laner, Angela Abicht, Tobias Ruck, Joachim Weis, Catherine Choueiri, Hanns Lochmüller, Heike Kölbel, and Andreas Roos. Novel genetic and biochemical insights into the spectrum of nefl-associated phenotypes. Journal of Neuromuscular Diseases, 11:625-645, Apr 2024. URL: https://doi.org/10.3233/jnd-230230, doi:10.3233/jnd-230230. This article has 12 citations and is from a peer-reviewed journal.

8. (agrawal2014expandingthephenotype pages 3-4): Pankaj B. Agrawal, Mugdha Joshi, Nicholas S. Marinakis, Klaus Schmitz-Abe, Pedro D. S. C. Ciarlini, Jane C. Sargent, Kyriacos Markianos, Umberto De Girolami, David A. Chad, and Alan H. Beggs. Expanding the phenotype associated with the nefl mutation: neuromuscular disease in a family with overlapping myopathic and neurogenic findings. JAMA neurology, 71 11:1413-20, Nov 2014. URL: https://doi.org/10.1001/jamaneurol.2014.1432, doi:10.1001/jamaneurol.2014.1432. This article has 46 citations and is from a highest quality peer-reviewed journal.

9. (agrawal2014expandingthephenotype pages 4-5): Pankaj B. Agrawal, Mugdha Joshi, Nicholas S. Marinakis, Klaus Schmitz-Abe, Pedro D. S. C. Ciarlini, Jane C. Sargent, Kyriacos Markianos, Umberto De Girolami, David A. Chad, and Alan H. Beggs. Expanding the phenotype associated with the nefl mutation: neuromuscular disease in a family with overlapping myopathic and neurogenic findings. JAMA neurology, 71 11:1413-20, Nov 2014. URL: https://doi.org/10.1001/jamaneurol.2014.1432, doi:10.1001/jamaneurol.2014.1432. This article has 46 citations and is from a highest quality peer-reviewed journal.

10. (medina2024molecularphenotypicanalysisa pages 30-35): J Medina. Molecular phenotypic analysis following antisense oligonucleotide treatment in a pre-clinical charcot-marie-tooth disease model. Unknown journal, 2024.

11. (feliciano2021allelespecificgeneediting pages 1-3): CM Feliciano, K Wu, and HL Watry. Allele-specific gene editing rescues pathology in a human model of charcot-marie. Unknown journal, 2021.

12. (medina2024customizedantisenseoligonucleotidebased pages 11-12): Jessica Medina, Adriana Rebelo, Matt C Danzi, Elizabeth H Jacobs, Isaac R L Xu, Kathleen P Ahrens, Sitong Chen, Jacquelyn Raposo, Christopher Yanick, Stephan Zuchner, and Mario A Saporta. Customized antisense oligonucleotide-based therapy for neurofilament-associated charcot-marie-tooth disease. Brain : a journal of neurology, 147:4227-4239, Jul 2024. URL: https://doi.org/10.1093/brain/awae225, doi:10.1093/brain/awae225. This article has 9 citations.

13. (medina2024molecularphenotypicanalysis pages 13-17): J Medina. Molecular phenotypic analysis following antisense oligonucleotide treatment in a pre-clinical charcot-marie-tooth disease model. Unknown journal, 2024.

14. (zuchner2004thenovelneurofilament pages 10-10): Stephan Züchner, Matthias Vorgerd, Eckhart Sindern, and J.Michael Schröder. The novel neurofilament light (nefl) mutation glu397lys is associated with a clinically and morphologically heterogeneous type of charcot-marie-tooth neuropathy. Neuromuscular Disorders, 14:147-157, Feb 2004. URL: https://doi.org/10.1016/j.nmd.2003.10.003, doi:10.1016/j.nmd.2003.10.003. This article has 120 citations and is from a peer-reviewed journal.

15. (agrawal2014expandingthephenotype pages 1-2): Pankaj B. Agrawal, Mugdha Joshi, Nicholas S. Marinakis, Klaus Schmitz-Abe, Pedro D. S. C. Ciarlini, Jane C. Sargent, Kyriacos Markianos, Umberto De Girolami, David A. Chad, and Alan H. Beggs. Expanding the phenotype associated with the nefl mutation: neuromuscular disease in a family with overlapping myopathic and neurogenic findings. JAMA neurology, 71 11:1413-20, Nov 2014. URL: https://doi.org/10.1001/jamaneurol.2014.1432, doi:10.1001/jamaneurol.2014.1432. This article has 46 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Charcot-Marie-Tooth_Disease_Dominant_Intermediate_G-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0036484` (8 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **Charcot-Marie-Tooth disease, dominant intermediate G**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0036484` - called "if available", "MONDO"