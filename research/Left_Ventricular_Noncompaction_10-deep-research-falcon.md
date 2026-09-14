---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T14:28:56.148872'
end_time: '2026-09-06T14:45:21.060075'
duration_seconds: 984.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Left Ventricular Noncompaction 10
  mondo_id: MONDO:0014163
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 50
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 10
  validator_version: 0.2.1
term_validation:
  total_terms: 5
  verified: 5
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014163
    reported_labels:
    - if available
    ontology_label: left ventricular noncompaction 10
  - term_id: HP:0011664
    reported_labels:
    - Imaging sign; congenital substrate or later-recognized trait; severity and progression
      variable
    ontology_label: Left ventricular noncompaction cardiomyopathy
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Left_Ventricular_Noncompaction_10-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Left Ventricular Noncompaction 10
- **MONDO ID:** MONDO:0014163 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Left Ventricular Noncompaction 10** covering all of the
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
- **Disease Name:** Left Ventricular Noncompaction 10
- **MONDO ID:** MONDO:0014163 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Left Ventricular Noncompaction 10** covering all of the
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


# Left Ventricular Noncompaction 10: Disease-Characteristics Report

## Executive summary and scope

**Left ventricular noncompaction 10 (LVNC10)** is the numbered, **MYBPC3-related** form of left-ventricular noncompaction/hypertrabeculation. Its key identifiers are **MONDO:0014163** and **OMIM #615396**. The disease-defining gene is **MYBPC3**, encoding cardiac myosin-binding protein C (cMyBP-C); Open Targets maps MONDO:0014163 specifically to MYBPC3 (Ensembl ENSG00000134571). (OpenTargets Search: Left ventricular noncompaction 10)

The evidence base is unusually heterogeneous. Variant-level evidence specific to LVNC10 comes mainly from small families and severe neonatal cases, whereas most prevalence, diagnostic, prognostic, and treatment data concern **LVNC of any genetic cause**. Those generic data should not be entered as subtype-specific facts without an explicit qualifier. Contemporary ESC thinking also treats left-ventricular hypertrabeculation as a potentially dynamic imaging trait rather than, by itself, a distinct cardiomyopathy. (grasso2024thenew2023 pages 1-2)

The following evidence map summarizes the distinction between LVNC10-specific and generic LVNC findings.

| Domain | Subtype-specific finding | Generic LVNC context | Evidence type/source/date | Identifiers/ontology suggestions | Confidence/limitations |
|---|---|---|---|---|---|
| Nosology | LVNC10 is the **MYBPC3-related** numbered subtype of left ventricular noncompaction. | **Generic LVNC:** Hypertrabeculation with deep intertrabecular recesses and a thin compacted myocardial layer; it may be a cardiomyopathy phenotype or dynamic trait rather than a distinct disease. (OpenTargets Search: Left ventricular noncompaction 10, grasso2024thenew2023 pages 1-2) | Aggregated disease resource; Open Targets, accessed 2026; ESC-guideline commentary, Apr 2024 | MONDO:0014163; OMIM #615396; MYBPC3; HP:0011664 | **High** for disease–gene mapping; nosologic interpretation remains debated. |
| Inheritance | Heterozygous MYBPC3 disease is generally autosomal dominant with incomplete penetrance and variable expressivity; biallelic truncating variants cause a severe recessive-like neonatal phenotype. (probst2011sarcomeregenemutations pages 8-9, wessels2015compoundheterozygousor pages 1-2) | **Generic LVNC:** Autosomal dominant inheritance predominates, but autosomal recessive, X-linked, and mitochondrial forms occur. (sedaghathamedani2017clinicalgeneticsand pages 1-2, hirono2022leftventricularnoncompaction pages 1-2) | Human family series; Probst et al., Aug 2011; Wessels et al., Oct 2015 | Germline inheritance; MYBPC3 | **Moderate–high**; no LVNC10-specific population penetrance estimate. HCM-derived estimates are not LVNC10-specific. |
| Key variants | Dutch founder truncating alleles **MYBPC3 c.2373dup, p.(Trp792fs)** and **c.2827C>T, p.(Arg943\*)** occurred as compound-heterozygous or homozygous genotypes. c.2373dup causes aberrant splicing, exon-24 skipping, frameshift, premature termination, and no detectable truncated protein. (wessels2015compoundheterozygousor pages 2-3, wessels2015compoundheterozygousor pages 5-6) | **Generic LVNC:** Many sarcomeric genes overlap with HCM and DCM; interpretation must consider variant class, segregation, phenotype, and population frequency. (mazzarotto2020thegeneticarchitecture pages 1-3, grasso2024thenew2023 pages 1-2) | Human neonatal series and RNA/protein analysis; Wessels et al., Oct 2015; https://doi.org/10.1038/ejhg.2014.211 | MYBPC3; frameshift; nonsense; germline | **High** for reported families; transcript accession and population allele frequencies were not established here. |
| Severe biallelic phenotype | Four infants presented at approximately 4–7 weeks; three had LVNC, all had septal defects, feeding difficulty or failure to thrive and dyspnea, and all died from cardiac failure before 13 weeks. Among 21 reported biallelic truncating cases, 15 died before age 1 and 13/21 (62%) had structural defects. (wessels2015compoundheterozygousor pages 2-3, wessels2015compoundheterozygousor pages 1-2, wessels2015compoundheterozygousor pages 3-4) | **Generic LVNC:** Pediatric genetic disease may include congenital heart defects and have more severe outcomes than adult sarcomeric disease. | Human case series and literature review; Wessels et al., Oct 2015 | Suggested HPO: HP:0011664; failure to thrive; dyspnea; heart failure; atrial or ventricular septal defect | **High** for this rare biallelic phenotype, but evidence is small and ascertainment-enriched; it is not representative of typical heterozygous LVNC10. |
| Heterozygous phenotype | MYBPC3 variants can produce LVNC, HCM, mixed LVNC/HCM, or clinically silent carriage within families; MYBPC3 accounted for 8% of variants in one 63-proband isolated-LVNC series. (probst2011sarcomeregenemutations pages 8-9) | **Generic LVNC:** Presentation ranges from incidental imaging findings to systolic dysfunction, heart failure, arrhythmia, thromboembolism, transplantation, and sudden death. (hirono2022leftventricularnoncompaction pages 1-2, wang2017awideand pages 1-2) | Human cohort and family evidence; Probst et al., Aug 2011; Wang et al., Sep 2017 | Suggested HPO: HP:0011664; cardiomyopathy; arrhythmia; reduced LVEF | **Moderate**; small numbers preclude reliable MYBPC3 variant-specific frequency or severity estimates. |
| Diagnosis | No imaging criterion is specific for MYBPC3-related LVNC10; diagnosis requires pathogenic or likely pathogenic MYBPC3 evidence, a compatible cardiac phenotype, and segregation assessment. | **Generic LVNC:** Echo thresholds include Chin X/Y ≤0.5 and Jenni noncompacted-to-compacted ratio >2 in systole; CMR thresholds include Petersen ratio ≥2.3 in diastole and Jacquier trabeculated mass >20%. Physiologic hypertrabeculation can occur in athletes and pregnancy. (martineztittonel2025leftventricularnoncompaction pages 5-7, mazzarotto2020thegeneticarchitecture pages 1-3) | Imaging literature and reviews; criteria synthesized through 2025; ESC framing, 2023–2024 | HP:0011664; CMR; echocardiography | **Moderate**; criteria have imperfect concordance and may overdiagnose disease. Morphology alone does not establish LVNC10. |
| Epidemiology | No reliable prevalence or incidence estimate exists for genetically confirmed LVNC10. | **Generic adult LVNC:** A 2024 meta-analysis estimated prevalence at 0.5% and CMR detection at 1.3%. Published prevalence ranged from 0.014% to 14.79%, reflecting criteria and ascertainment heterogeneity. (llerenavelastegui2024prevalenceclinicalmanifestations pages 1-2) | Systematic review and meta-analysis; Llerena-Velastegui et al., Oct 2024; https://doi.org/10.14740/cr1673 | MONDO:0014163 for subtype; MONDO:0018901 for generic LVNC | **Low** for extrapolation to LVNC10; generic imaging prevalence must not be assigned to the genetic subtype. |
| Prognosis | MYBPC3 was identified as a genetic predictor of major adverse cardiac events in a genotype–phenotype review; biallelic truncation predicts an exceptionally poor neonatal course. (wessels2015compoundheterozygousor pages 1-2, wang2017awideand pages 1-2) | **Generic LVNC:** Among 2,501 patients, event rates per 100 person-years were cardiovascular mortality 1.92, all-cause mortality 2.16, stroke or systemic embolism 1.54, HF admission 3.53, transplantation 1.24, ventricular arrhythmia 2.17, and device implantation 2.66. LVEF—not trabeculation extent—was the major outcome determinant. (aung2020prognosticsignificanceof pages 1-2) | Human systematic review and meta-analysis; Aung et al., Jan 2020; https://doi.org/10.1161/CIRCIMAGING.119.009712 | Suggested HPO: reduced LVEF; ventricular arrhythmia; thromboembolism; sudden cardiac death | **High** for generic LVNC outcomes; **low–moderate** for subtype-specific extrapolation. |
| Thromboembolism | No MYBPC3-specific thromboembolic rate is established. | **Generic LVNC:** TE prevalence was 2.6% in children and 6.2% in adults; annual incidence was 1.4% and 2.9%, respectively. Pediatric LVEF <40% was associated with TE, OR 9.47 and 95% CI 1.35–188.23. (hirono2022thromboemboliceventsin pages 1-2) | Systematic review and meta-analysis; Hirono et al., May 2022; https://doi.org/10.1136/openhrt-2021-001908 | Suggested HPO: thromboembolism; stroke; reduced LVEF | **Moderate** because heterogeneity was high; anticoagulation cannot be based on trabeculation alone. |
| Molecular mechanism | Truncating MYBPC3 alleles support loss of function and haploinsufficiency. In one compound-heterozygous LVNC case, myocardial MYBPC3 transcript fell approximately 50% and protein approximately 80%, with myocyte misalignment, vacuolization, hyperplasia, and major fibrosis. (kolokotronis2019biallelicmutationin pages 7-9, wessels2015compoundheterozygousor pages 5-6) | **Generic LVNC inference:** Sarcomeric dysfunction may impair force regulation and drive hypertrophic or dilated remodeling; how it specifically generates hypertrabeculation is unproven. | Human cardiac-tissue and molecular assays; Kolokotronis et al., Aug 2019; Wessels et al., Oct 2015 | Suggested GO: sarcomere organization; cardiac muscle contraction; actin–myosin interaction; suggested CL: cardiomyocyte | **Moderate** for sarcomeric loss of function; **low** for a direct causal bridge to noncompaction morphology. |
| 2024 cellular research | MYBPC3 c.1377delC iPSC-cardiomyocytes showed sarcomere disruption, damaged mitochondria, abnormal calcium signals, increased respiration, and upregulated electron-transport genes. MYBPC3 p.Asp389Val organoids showed hypercontractility, faster calcium cycling, oxidative stress, and reduced mitochondrial membrane potential; mavacamten rescued hypercontractility. (desai2024mybpc3d389vvariant pages 1-2, mori2024metabolicremodelingand pages 1-2) | **Generic context:** These are HCM or dilated-phase HCM models, not validated LVNC models. | Human iPSC-CM and organoid experiments; Mori et al., Jul 2024, https://doi.org/10.1038/s41598-024-62530-0; Desai et al., Nov 2024, https://doi.org/10.3390/cells13221913 | Suggested GO: calcium-ion homeostasis; mitochondrial electron transport; oxidative stress; cardiac muscle contraction; CL: cardiomyocyte, endothelial cell, fibroblast, macrophage | **Moderate** for MYBPC3 cellular mechanisms; **low** for direct application to LVNC10 morphology or treatment. |
| Animal models | Zebrafish mybpc3 knockout or knockdown produces ventricular hypertrophy, cardiomyocyte hyperplasia, diastolic dysfunction, altered calcium reuptake, arrhythmogenic alternans, reduced endurance, and downregulated actin-filament processes. (da’as2022transcriptomeprofileidentifies pages 11-13, chen2013inactivationofmyosin pages 1-2) | **Generic context:** These models reproduce HCM and heart-failure traits, **not demonstrated LV noncompaction**. | Stable-knockout and morpholino zebrafish; Chen et al., Sep 2013, https://doi.org/10.1161/JAHA.113.000231; Da’as et al., Aug 2022, https://doi.org/10.3390/ijms23168840 | NCBI Taxon 7955; mybpc3 ortholog; suggested GO: actin cytoskeleton organization, calcium-ion transport, cardiac muscle contraction | **Moderate** for conserved sarcomeric and electrophysiologic dysfunction; species anatomy and absent LVNC morphology limit translation. |
| Management | No approved LVNC10-specific pharmacotherapy, gene therapy, RNA therapy, or genotype-guided drug regimen exists. Management follows the expressed phenotype: guideline-directed HF therapy, arrhythmia treatment, ICD under standard risk indications, selective anticoagulation, and transplantation or mechanical support for end-stage disease. | **Generic LVNC:** Reduced LVEF, NYHA class III/IV, ventricular tachycardia, fibrosis or LGE, and clinical arrhythmia are more actionable than trabeculation burden. (llerenavelastegui2024prevalenceclinicalmanifestations pages 1-2, aung2020prognosticsignificanceof pages 1-2) | Cardiomyopathy and HF guideline extrapolation plus LVNC outcome evidence; ESC framework, 2023–2024 | Suggested NCIT: echocardiography; cardiac MRI; genetic testing; anticoagulant therapy; implantable cardioverter-defibrillator; heart transplantation | **Moderate**; no randomized LVNC10 treatment trials. Mavacamten organoid rescue is not clinical evidence for LVNC10. |
| Screening and prevention | Offer genetic counseling and MYBPC3 testing with copy-number analysis to an affected proband; when a pathogenic or likely pathogenic variant is found, use cascade testing plus ECG and echocardiographic surveillance of first-degree relatives. In severe neonatal disease, test both parents and assess biallelic recurrence risk. | **Generic LVNC:** Avoid diagnosing disease solely from trabeculation; deep phenotyping and multidisciplinary variant interpretation are recommended. (wessels2015compoundheterozygousor pages 3-4, grasso2024thenew2023 pages 1-2) | Human segregation evidence and ESC cardiomyopathy-genetics framework, 2015–2024 | MYBPC3; germline testing; cascade screening; prenatal or preimplantation testing when familial variants are established | **Moderate–high**; surveillance intervals should be individualized. No primary prevention or protective allele is established. |
| Current research | No interventional trial specific to MYBPC3-related LVNC10 was identified. | **Generic LVNC:** **NCT06024759** is a recruiting, case-only registry of 500 adults followed for 10 years to assess genetic variants, myocardial strain, LV dysfunction, arrhythmia markers, and predictors of ICD implantation; it started Sep 1, 2023, with estimated completion in Aug 2033. (NCT06024759 chunk 1, NCT06024759 chunk 2) | ClinicalTrials.gov observational registry; first posted Sep 6, 2023; status verified Oct 2023 | NCT06024759; adult LVNC registry | **High** for retrieved registry design and status; not subtype-specific, randomized, or therapeutic. |


*Table: Compact evidence map separating MYBPC3-specific LVNC10 findings from broader LVNC data. It highlights variant-level evidence, diagnostic uncertainty, outcomes, mechanisms, models, management, and current registry research.*

---

## 1. Disease information

### Definition

LVNC morphology consists of prominent ventricular trabeculae, deep intertrabecular recesses communicating with the ventricular cavity, and a relatively thin compacted epicardial layer. In LVNC10, that cardiac phenotype is associated with a pathogenic or likely pathogenic germline variant in **MYBPC3**. The phenotype can occur alone or overlap hypertrophic cardiomyopathy (HCM), dilated cardiomyopathy (DCM), congenital heart defects, and arrhythmia. (probst2011sarcomeregenemutations pages 8-9, hirono2022leftventricularnoncompaction pages 1-2)

The modern interpretation is important: the 2023 ESC framework regards noncompaction/hypertrabeculation as a **dynamic trait** that may be genetic and pathological but may also be adaptive, transient, or reversible in pregnancy, athletes, anemia, renal disease, or otherwise healthy hearts. Thus, morphology alone does not establish LVNC10. (grasso2024thenew2023 pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0014163.
- **OMIM:** #615396.
- **Causal gene:** MYBPC3; Ensembl ENSG00000134571.
- **Core phenotype term:** HPO **HP:0011664**, left ventricular noncompaction cardiomyopathy.
- **Synonyms:** left ventricular noncompaction 10; LVNC10; MYBPC3-related left ventricular noncompaction; MYBPC3-related noncompaction cardiomyopathy; left ventricular hypertrabeculation associated with MYBPC3.
- **Broader disease:** MONDO:0018901, left ventricular noncompaction. (OpenTargets Search: Left ventricular noncompaction 10)
- **ICD/MeSH:** No ICD-10 or ICD-11 code uniquely identifies the MYBPC3 subtype. It is ordinarily represented under cardiomyopathy or other specified cardiomyopathy, with genetic findings recorded separately. A uniquely subtype-specific MeSH descriptor was not established in the retrieved evidence.

The report is based on **aggregated disease resources, published families, cohorts, meta-analyses, experimental models, and a clinical-trial registry**, not individual EHR data.

---

## 2. Etiology

### Causal factors and genetic risk

The established causal factor is a **germline MYBPC3 variant** that disrupts cMyBP-C abundance or function. Heterozygous variants usually behave in an autosomal-dominant manner with incomplete, age-dependent penetrance and variable expressivity. Biallelic truncating variants produce a much more severe, effectively recessive neonatal phenotype. (probst2011sarcomeregenemutations pages 8-9, wessels2015compoundheterozygousor pages 2-3, wessels2015compoundheterozygousor pages 1-2)

In 63 unrelated adults with isolated LVNC, 18 heterozygous sarcomeric variants were found in 29%; MYBPC3 accounted for approximately 8%. Mutation-positive and mutation-negative patients could not be reliably distinguished clinically. This supports genetic heterogeneity and weak phenotype prediction from the gene alone. (probst2011sarcomeregenemutations pages 8-9)

In a broader 102-patient LVNC cohort, 43 pathogenic variants in 16 genes were found in 39 patients (38%); 63% were sarcomeric and 12% channelopathy-associated. Pathogenic-variant carriers had earlier onset and lower LVEF, and pathogenic variants independently predicted adverse events. These figures are **generic LVNC data**, not MYBPC3-specific penetrance estimates. (wang2017awideand pages 1-2)

### Environmental, lifestyle, and gene–environment factors

No toxin, infection, diet, smoking exposure, occupational factor, or lifestyle behavior has been shown to cause genetically defined LVNC10. Hemodynamic load can modify trabeculation and may expose or amplify an underlying cardiomyopathy phenotype, but a MYBPC3-specific gene–environment interaction has not been demonstrated. Pregnancy and intensive athletic training can increase trabeculation in people without genetic cardiomyopathy, creating an important diagnostic confounder rather than a proven cause of LVNC10. (mazzarotto2020thegeneticarchitecture pages 1-3, grasso2024thenew2023 pages 1-2)

### Protective factors

No validated protective MYBPC3 allele, diet, drug, or environmental exposure is known to prevent LVNC10. Standard cardiovascular health measures are reasonable but have not been shown to prevent expression of this monogenic disorder.

---

## 3. Phenotypes

### Core and associated phenotypes

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Left-ventricular noncompaction/hypertrabeculation | Imaging sign; congenital substrate or later-recognized trait; severity and progression variable | HP:0011664 |
| Cardiomyopathy, often mixed LVNC/HCM or LVNC/DCM | Structural/functional sign; may be asymptomatic or progressive | Use the applicable HCM/DCM HPO term plus HP:0011664 |
| Reduced LVEF/systolic dysfunction | Imaging/functional abnormality; major adverse-outcome determinant | Decreased left-ventricular ejection fraction |
| Heart failure | Symptom complex/sign; exertional dyspnea, edema, feeding difficulty in infants, fatigue | Congestive heart failure; dyspnea; exercise intolerance |
| Ventricular or atrial arrhythmia | Electrophysiologic sign; may be episodic and life-threatening | Ventricular arrhythmia; atrial fibrillation |
| Thromboembolism/stroke | Complication, especially with impaired systolic function or atrial fibrillation | Thromboembolism; ischemic stroke |
| Failure to thrive/feeding difficulty | Predominantly severe neonatal biallelic disease | Failure to thrive; feeding difficulties |
| ASD/VSD/PFO | Congenital structural findings enriched in severe biallelic cases | Atrial septal defect; ventricular septal defect; patent foramen ovale |
| Sudden cardiac death | Severe outcome related to malignant arrhythmia or advanced cardiomyopathy | Sudden cardiac death |

### Severe biallelic phenotype

Wessels et al. reported four unrelated infants with biallelic truncating MYBPC3 variants. All had feeding difficulty, failure to thrive, and dyspnea; three had clear LVNC, all had a septal defect or patent foramen ovale, and all died from cardiac failure before 13 weeks. In the authors’ review of 21 biallelic truncating cases, all had severe cardiomyopathy, 15 died before age one, and 13/21 (62%) had a structural defect. (wessels2015compoundheterozygousor pages 2-3, wessels2015compoundheterozygousor pages 1-2, wessels2015compoundheterozygousor pages 3-4)

A representative direct conclusion from the abstract is: **“Compound heterozygous or homozygous truncating MYBPC3 mutations cause lethal cardiomyopathy with features of noncompaction and septal defects.”** The study was published in *European Journal of Human Genetics* in October 2015, DOI: https://doi.org/10.1038/ejhg.2014.211. (wessels2015compoundheterozygousor pages 2-3)

### Heterozygous phenotype and quality of life

Heterozygous MYBPC3 families can include asymptomatic carriers, isolated LVNC, HCM, mixed LVNC/HCM, severe heart failure, and cerebrovascular complications. This indicates incomplete penetrance and marked intrafamilial expressivity. (probst2011sarcomeregenemutations pages 8-9, wessels2015compoundheterozygousor pages 3-4)

No LVNC10-specific EQ-5D, SF-36, or PROMIS study was identified. Functional effects are inferred from heart-failure symptoms, exercise intolerance, arrhythmia, hospital admission, ICD placement, and transplantation. Adult zebrafish models also show reduced swimming endurance, but this is experimental rather than a human quality-of-life measure. (da’as2022transcriptomeprofileidentifies pages 11-13)

---

## 4. Genetic and molecular information

### Causal gene

- **Gene:** MYBPC3, myosin-binding protein C3.
- **Protein:** cardiac myosin-binding protein C, a thick-filament-associated sarcomeric regulator.
- **Primary cell:** cardiomyocyte.
- **Subcellular site:** sarcomere/myofibril, particularly the C-zone of the A band.
- **Variant origin:** germline; no somatic LVNC10 mechanism is established. (OpenTargets Search: Left ventricular noncompaction 10, desai2024mybpc3d389vvariant pages 1-2)

### Documented variants and consequences

The best-defined severe variants are the Dutch founder alleles:

1. **MYBPC3 c.2373dup, p.(Trp792fs)** — frameshift. It creates an aberrant splice donor, causes exon-24 skipping and a frameshift after Gln791, introduces premature termination, and yielded no detectable truncated protein, consistent with transcript/protein instability and loss of function.
2. **MYBPC3 c.2827C>T, p.(Arg943\*)** — nonsense/truncating variant.

Two infants were compound heterozygous for these variants; one was homozygous for c.2373dup and one homozygous for c.2827C>T. Both alleles were recurrent founder variants in the Dutch HCM population. (wessels2015compoundheterozygousor pages 2-3, wessels2015compoundheterozygousor pages 5-6, wessels2015compoundheterozygousor pages 3-4)

A separate severe case carried an entire-gene MYBPC3 deletion in trans with de novo **p.Ser858Arg**. Myocardial MYBPC3 transcript was reduced approximately 50%, protein approximately 80%, and α-actinin approximately 50%; histology showed myocyte misalignment, vacuolization, hyperplasia, and substantial fibrosis. These findings support haploinsufficiency plus instability or dysfunction of the missense product. (kolokotronis2019biallelicmutationin pages 7-9)

### Variant interpretation

Variant classification must follow ACMG/AMP criteria and include:

- exact transcript and HGVS nomenclature;
- ClinVar/ClinGen assertions and review status;
- segregation and de novo status;
- read-depth-based copy-number analysis;
- predicted nonsense-mediated decay or splice effect;
- population frequency in gnomAD/TOPMed;
- functional evidence; and
- compatibility with the family’s HCM/DCM/LVNC spectrum.

No complete variant-level gnomAD frequencies or current ClinVar review statuses were recoverable from the retrieved papers; these fields should be populated by a live variant-specific database query rather than inferred. A VUS should **not** establish LVNC10 or direct predictive testing.

### Modifiers, epigenetics, and chromosomal abnormalities

No validated modifier gene, protective allele, LVNC10-specific methylation signature, histone alteration, or recurrent chromosomal abnormality is established. Whole-gene deletion is possible and supports inclusion of deletion/duplication analysis. The neighboring-gene extension reported with one deletion did not have an established explanatory human phenotype in the source. (kolokotronis2019biallelicmutationin pages 7-9)

---

## 5. Environmental information

No infectious agent, pollutant, radiation exposure, toxin, alcohol exposure, diet, or occupational risk is known to cause LVNC10. Pregnancy, anemia, renal disease, and intensive exercise can cause adaptive hypertrabeculation and therefore affect **phenotypic ascertainment**, but they should not be coded as established causes of MYBPC3 disease. (grasso2024thenew2023 pages 1-2)

Exercise advice should be individualized according to ventricular function, arrhythmia burden, symptoms, fibrosis, and family history rather than the trabecular appearance alone. Avoidance of smoking and cardiotoxic exposures is prudent general care, not disease-specific prevention.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A pathogenic germline **MYBPC3** truncating, splice, deletion, or functionally disruptive missense variant **leads to** reduced abundance or altered regulation of cMyBP-C in cardiomyocyte sarcomeres. (kolokotronis2019biallelicmutationin pages 7-9, wessels2015compoundheterozygousor pages 5-6)
2. Reduced or dysfunctional cMyBP-C **leads to** abnormal control of actin–myosin interaction, cross-bridge cycling, contractility, and sarcomere organization. (desai2024mybpc3d389vvariant pages 1-2, da’as2022transcriptomeprofileidentifies pages 1-2)
3. Sarcomeric dysfunction **results in** abnormal calcium handling and altered electrophysiology; zebrafish and human iPSC models demonstrate slowed calcium reuptake or abnormal calcium transients, although these are principally HCM/DCM models rather than LVNC10 models. (mori2024metabolicremodelingand pages 1-2, chen2013inactivationofmyosin pages 1-2)
4. Contractile and calcium-handling stress **leads to** energetic and mitochondrial remodeling, including oxidative stress, damaged mitochondria, altered membrane potential, increased respiration, and electron-transport gene expression in 2024 cellular models. (desai2024mybpc3d389vvariant pages 1-2, mori2024metabolicremodelingand pages 1-2)
5. These abnormalities **lead to** cardiomyocyte hypertrophy or hyperplasia, myofibrillar disarray, fibrosis, and ventricular remodeling. Human cardiac tissue demonstrates misaligned cells, vacuolization, hyperplasia, and fibrosis. (kolokotronis2019biallelicmutationin pages 7-9)
6. **Inferred branch A:** disturbed developmental growth and remodeling may **result in** persistence or exaggeration of trabeculation and a thin compact layer. This direct MYBPC3-to-noncompaction developmental step has **not been conclusively demonstrated**.
7. **Branch B:** progressive hypertrophic or dilated remodeling **results in** diastolic or systolic dysfunction and clinical heart failure.
8. **Branch C:** calcium/electrical instability and fibrotic substrate **result in** atrial or ventricular arrhythmia, syncope, ICD requirement, or sudden death.
9. **Branch D:** low-flow states, ventricular dysfunction, atrial fibrillation, and possibly recess-associated stasis **result in** intracardiac thrombosis and systemic embolism; the recess-stasis mechanism remains plausible but unproven. (hirono2022thromboemboliceventsin pages 1-2)

### Pathways, processes, and ontology suggestions

Suggested GO biological processes include **sarcomere organization**, **cardiac muscle contraction**, **actin filament organization**, **actin–myosin filament sliding**, **calcium-ion homeostasis**, **regulation of membrane potential**, **mitochondrial electron transport**, **response to oxidative stress**, **cardiomyocyte proliferation**, and **cardiac muscle hypertrophy**. Suggested cellular components include **sarcomere**, **myofibril**, **A band**, **actin cytoskeleton**, and **mitochondrion**. Relevant cell types are **cardiomyocyte** (primary), with downstream roles for cardiac fibroblasts, endothelial cells, macrophages, and other immune cells in remodeling. Spatial mapping in a 2024 cardiac-organoid study identified all these populations. (desai2024mybpc3d389vvariant pages 1-2)

No LVNC10-specific immune, lipidomic, metabolomic, epigenomic, single-cell, or spatial-transcriptomic signature has been validated. The 2024 organoid and iPSC studies are valuable mechanistic advances but modeled MYBPC3-HCM or dilated-phase HCM, not confirmed noncompaction morphology. (desai2024mybpc3d389vvariant pages 1-2, mori2024metabolicremodelingand pages 1-2)

---

## 7. Anatomical structures affected

- **Primary organ/system:** heart/cardiovascular system.
- **Primary chamber:** left ventricle; severe cases may have biventricular trabeculation or dysfunction.
- **Typical sites:** apical and mid-ventricular myocardium, especially the endocardial trabecular layer.
- **Tissues:** cardiac muscle/myocardium; compacted epicardial and noncompacted endocardial layers.
- **Cells:** ventricular cardiomyocytes; secondary remodeling involves fibroblasts, vascular/endocardial cells, and immune cells.
- **Subcellular structures:** sarcomere, thick filament, myofibril, actin–myosin apparatus, calcium-handling system, mitochondria.
- **Secondary structures:** atrial and ventricular septa in severe biallelic disease; systemic organs may be affected secondarily by heart failure or embolism. (wessels2015compoundheterozygousor pages 2-3, desai2024mybpc3d389vvariant pages 1-2)

Suggested anatomy terms include **UBERON:0000948 heart**, **UBERON:0002084 heart left ventricle**, myocardium, interventricular septum, and interatrial septum. The lesion is not meaningfully unilateral in the ordinary paired-organ sense, although ventricular distribution may be regionally asymmetric.

---

## 8. Temporal development

Heterozygous disease can be congenital in substrate but clinically silent until childhood or adulthood. Recognition may be incidental, insidious, or triggered by dyspnea, arrhythmia, syncope, embolism, or family screening. Penetrance is incomplete and age-dependent; the retrieved evidence does not provide a reliable LVNC10-specific age curve. (probst2011sarcomeregenemutations pages 8-9)

Biallelic truncating disease is a critical exception: onset is neonatal or early infantile, with diagnosis in the reported series at approximately 4–7 weeks and death at 7–12 weeks. (wessels2015compoundheterozygousor pages 2-3)

The long-term course ranges from stable imaging morphology with preserved function to progressive HCM/DCM, fibrosis, arrhythmia, end-stage heart failure, mechanical support, transplantation, or sudden death. Apparent hypertrabeculation can regress when it is pregnancy- or load-associated; this should not be interpreted as remission of genetically proven LVNC10. (grasso2024thenew2023 pages 1-2)

---

## 9. Inheritance and population

### Inheritance

- **Typical heterozygous state:** autosomal dominant, incomplete penetrance, variable expressivity.
- **Biallelic truncating state:** severe autosomal-recessive-like neonatal cardiomyopathy; clinically unaffected heterozygous parents were documented at initial evaluation. (wessels2015compoundheterozygousor pages 3-4)
- **Anticipation:** not established.
- **Germline mosaicism:** theoretically possible but not specifically documented in the retrieved LVNC10 evidence.
- **Consanguinity:** can increase biallelic risk but is not required; founder alleles can produce homozygosity or compound heterozygosity.
- **Founder effects:** c.2373dup p.(Trp792fs) and c.2827C>T p.(Arg943*) are Dutch founder alleles. (wessels2015compoundheterozygousor pages 2-3)

For a heterozygous pathogenic variant, each child generally has a 50% transmission probability, but phenotype cannot be predicted reliably. When both parents carry pathogenic MYBPC3 variants, each pregnancy has a 25% probability of inheriting both alleles, 50% of inheriting one, and 25% of inheriting neither, assuming variants are on different parental alleles and ordinary Mendelian segregation.

### Epidemiology and demographics

No trustworthy prevalence, incidence, sex ratio, carrier frequency, or geographic distribution is available for genetically confirmed LVNC10. Generic adult LVNC meta-analysis estimated a pooled prevalence of 0.5% and CMR detection of 1.3%, but reported prevalence ranged from 0.014% to 14.79% because of imaging and ascertainment heterogeneity. These values must not be assigned directly to MONDO:0014163. (llerenavelastegui2024prevalenceclinicalmanifestations pages 1-2)

A 2020 meta-analysis of 2,501 generic LVNC patients reported a mean age of 46 years and male:female ratio of 1.7. Again, these are not LVNC10-specific demographics. (aung2020prognosticsignificanceof pages 1-2)

---

## 10. Diagnostics

### Clinical work-up

A reasonable real-world evaluation includes three-generation pedigree, physical examination, 12-lead ECG, ambulatory ECG monitoring, transthoracic echocardiography, and CMR when morphology, ventricular function, or fibrosis remains uncertain. Exercise testing helps assess functional capacity and exercise-induced arrhythmia. BNP/NT-proBNP and troponin may aid heart-failure or injury assessment but are not diagnostic biomarkers for LVNC10.

### Imaging criteria

Commonly used criteria include:

- **Chin echocardiographic criterion:** X/Y ≤0.5.
- **Jenni criterion:** noncompacted-to-compacted myocardial ratio >2 at end systole, with perfused recesses.
- **Petersen CMR criterion:** NC/C ratio ≥2.3 at end diastole.
- **Jacquier CMR criterion:** trabeculated mass >20% of total LV mass. (martineztittonel2025leftventricularnoncompaction pages 5-7)

These criteria are neither mutually concordant nor genotype-specific. The 2023 ESC position cautions that hypertrabeculation occurs in healthy people, athletes, pregnancy, congenital heart disease, anemia, renal disease, and other cardiomyopathies. Diagnosis should therefore integrate function, fibrosis, arrhythmia, family history, and molecular evidence. (grasso2024thenew2023 pages 1-2)

### Differential diagnosis

Important alternatives are physiological athlete’s remodeling, pregnancy-related hypertrabeculation, sickle-cell disease or other chronic anemia, DCM or HCM with secondary trabeculation, apical HCM, endocardial fibroelastosis, arrhythmogenic cardiomyopathy, myocarditis, ischemic disease, congenital heart disease, and imaging artifact. Generic LVNC shares substantial genetic architecture with DCM and HCM. (mazzarotto2020thegeneticarchitecture pages 1-3, aung2020prognosticsignificanceof pages 1-2)

### Genetic testing

1. Use a curated cardiomyopathy panel that includes **MYBPC3** and validated LVNC/HCM/DCM genes.
2. Include exon-level deletion/duplication analysis; an entire MYBPC3 deletion has been reported. (kolokotronis2019biallelicmutationin pages 7-9)
3. In neonatal severe HCM/LVNC, actively evaluate **biallelic** MYBPC3 variation, phase the variants in parents, and consider rapid trio exome/genome sequencing.
4. WES/WGS is useful after a negative panel, in syndromic or congenital-malformation cases, or when structural/noncoding variants are suspected.
5. CMA is appropriate when multiple congenital anomalies or developmental abnormalities suggest a copy-number disorder. Karyotype/FISH, mitochondrial sequencing, and repeat-expansion testing are not routine unless phenotype directs them.
6. RNA analysis from an informative tissue can clarify splice variants; functional iPSC work remains research-grade.

Endomyocardial biopsy is not routinely needed solely to diagnose LVNC10; the ESC commentary confines biopsy mainly to selected myocarditis, restrictive, and infiltrative disorders. (grasso2024thenew2023 pages 1-2)

### Screening

When a pathogenic/likely pathogenic familial MYBPC3 variant is known, offer targeted cascade testing. First-degree relatives should receive genetic counseling and baseline ECG/echocardiography; periodic follow-up is individualized by age, genotype, symptoms, and family history. Genotype-negative relatives for the known familial variant can generally be released from variant-driven surveillance unless clinical findings independently warrant follow-up.

---

## 11. Outcomes and prognosis

The strongest subtype-specific adverse signal is biallelic truncation: all four Wessels infants died before 13 weeks, and 15/21 literature cases died before one year. (wessels2015compoundheterozygousor pages 1-2)

For generic LVNC, the 2020 meta-analysis of 28 studies and 2,501 patients found, per 100 person-years:

- cardiovascular mortality **1.92** (95% CI 1.54–2.30);
- all-cause mortality **2.16**;
- stroke/systemic embolism **1.54**;
- heart-failure admission **3.53**;
- transplantation **1.24**;
- ventricular arrhythmia **2.17**; and
- cardiac-device implantation **2.66**.

Cardiovascular mortality was similar to DCM (OR 1.10, 95% CI 0.18–6.67), and **LVEF rather than trabeculation burden** was the major determinant of outcome. The authors’ abstract states: **“Left ventricular ejection fraction—a conventional indicator of heart failure severity, not the extent of trabeculation—appears to be an important determinant of adverse outcomes.”** Published January 2020; DOI: https://doi.org/10.1161/CIRCIMAGING.119.009712. (aung2020prognosticsignificanceof pages 1-2)

The 2024 adult meta-analysis reported mortality of 12% and transplantation of 7%; NYHA III/IV status, ventricular tachycardia, and reduced LVEF predicted adverse outcomes. These remain generic estimates. (llerenavelastegui2024prevalenceclinicalmanifestations pages 1-2)

Thromboembolism prevalence was 2.6% in children and 6.2% in adults, with annual incidences of 1.4% and 2.9%. In children, LVEF <40% was associated with thromboembolism (OR 9.47; 95% CI 1.35–188.23). Published May 2022; DOI: https://doi.org/10.1136/openhrt-2021-001908. (hirono2022thromboemboliceventsin pages 1-2)

No LVNC10-specific five- or ten-year survival estimate, life expectancy, validated prognostic calculator, or quality-of-life dataset exists.

---

## 12. Treatment

### Current strategy

No therapy is approved specifically for LVNC10 or for correction of MYBPC3-related noncompaction. Care is phenotype-directed:

- **Heart failure with reduced EF:** guideline-directed therapy, ordinarily including an ARNI/ACE inhibitor/ARB, evidence-based beta blocker, mineralocorticoid-receptor antagonist, and SGLT2 inhibitor as tolerated; diuretics for congestion.
- **Arrhythmia:** beta blockade or other rhythm/rate treatment according to arrhythmia type; catheter ablation where appropriate.
- **ICD:** standard primary- or secondary-prevention indications based on LVEF, documented malignant ventricular arrhythmia, arrest, syncope, fibrosis, and the broader cardiomyopathy risk profile—not trabeculation alone.
- **Anticoagulation:** indicated for atrial fibrillation, documented intracardiac thrombus, prior systemic embolism, or another standard indication. Routine anticoagulation solely for trabeculation remains unsupported and controversial. (hirono2022thromboemboliceventsin pages 1-2)
- **Advanced disease:** cardiac resynchronization when standard criteria are met, ventricular-assist support, or heart transplantation.
- **Congenital defects:** surgical/interventional repair when hemodynamically indicated.

Suggested NCIT intervention concepts include cardiac MRI, echocardiography, genetic testing, anticoagulant therapy, implantable cardioverter-defibrillator placement, cardiac-resynchronization therapy, ventricular-assist device, and heart transplantation.

### Experimental and genotype-directed therapy

A 2024 MYBPC3 p.Asp389Val cardiac-organoid study demonstrated hypercontractility, faster calcium cycling, oxidative stress, and reduced mitochondrial membrane potential; mavacamten improved hypercontractility. The abstract states that the hypercontractile phenotype was **“rescued by the administration of a myosin inhibitor.”** Published November 19, 2024; DOI: https://doi.org/10.3390/cells13221913. This is an HCM organoid result, not clinical evidence for LVNC10, and mavacamten should not be considered an established LVNC10 therapy. (desai2024mybpc3d389vvariant pages 1-2)

A second 2024 study of MYBPC3 c.1377delC iPSC-cardiomyocytes found disrupted sarcomeres, damaged mitochondria, abnormal calcium handling, a hypermetabolic state, and increased electron-transport gene expression. Published July 2024; DOI: https://doi.org/10.1038/s41598-024-62530-0. It supplies mechanistic and drug-screening infrastructure, not a validated diagnostic or treatment. (mori2024metabolicremodelingand pages 1-2)

No LVNC10-specific gene therapy, CRISPR therapy, ASO, siRNA, cell therapy, or pharmacogenomic dosing recommendation is clinically available.

### Trials and implementation

**NCT06024759**, “Predictors of Risk in Left Ventricular Non-Compaction,” is a recruiting, observational, case-only registry targeting 500 adults and ten years of follow-up. It examines genetic variants, myocardial strain, LV dysfunction, Holter/stress-test arrhythmia markers, and predictors of ICD implantation. It began September 1, 2023, was first posted September 6, 2023, and has estimated completion in August 2033. It is generic LVNC research, not an intervention or LVNC10-specific trial. ClinicalTrials.gov URL: https://clinicaltrials.gov/study/NCT06024759. (NCT06024759 chunk 1, NCT06024759 chunk 2)

---

## 13. Prevention

### Primary prevention

The occurrence of a de novo or inherited pathogenic MYBPC3 variant cannot currently be prevented by lifestyle modification. There is no vaccine, medication, or environmental intervention that prevents LVNC10.

### Secondary prevention

- genetic counseling and cascade testing;
- serial ECG, ambulatory monitoring, echocardiography, and CMR when indicated;
- early treatment of ventricular dysfunction and arrhythmia;
- prenatal diagnosis or preimplantation genetic testing when familial pathogenic variants are known and parents desire these options;
- rapid parental testing after a severe neonatal presentation to define phase and recurrence risk.

### Tertiary prevention

Guideline-directed heart-failure therapy, rhythm surveillance, ICD use under standard indications, anticoagulation for established risk states, and timely referral for advanced-heart-failure therapy aim to prevent hospitalization, embolism, sudden death, and end-organ damage. General vaccination is appropriate for cardiovascular health but is not etiologic prevention.

---

## 14. Other species and natural disease

- **Danio rerio (zebrafish), NCBI Taxon 7955:** has a conserved mybpc3 ortholog. Experimental knockout/knockdown causes cardiac hypertrophy, diastolic dysfunction, abnormal calcium reuptake, electrical alternans, cardiomyocyte hyperplasia, and reduced endurance. (da’as2022transcriptomeprofileidentifies pages 11-13, chen2013inactivationofmyosin pages 1-2)
- **Domestic cat:** naturally occurring MYBPC3-associated HCM is documented in veterinary genetics, but the retrieved evidence did not establish a consistent natural LVNC10-equivalent syndrome or a validated breed ontology annotation.
- **Zoonosis/transmission:** not applicable; this is inherited disease, not infection.

Natural noncompaction in another species specifically attributable to orthologous MYBPC3 variation was not established by the retrieved sources.

---

## 15. Model organisms and experimental systems

### Zebrafish

Morpholino knockdown of mybpc3 produced ventricular hypertrophy, increased wall thickness, impaired diastolic relaxation, pericardial effusion, atrial dilation, prolonged action-potential duration, slowed calcium reuptake, and susceptibility to calcium-transient and action-potential alternans. Published September 2013; DOI: https://doi.org/10.1161/JAHA.113.000231. (chen2013inactivationofmyosin pages 1-2)

A stable knockout model showed larval cardiomyocyte hyperplasia, reduced chamber dimensions, increased EF, and later ventricular-wall thickening, bradycardia, and reduced swimming endurance. Transcriptomics identified downregulation of actin-filament processes and changes in hypertrophy, calcium-handling, contraction, and cardiac-development programs. Published August 2022; DOI: https://doi.org/10.3390/ijms23168840. (da’as2022transcriptomeprofileidentifies pages 11-13, da’as2022transcriptomeprofileidentifies pages 2-4)

**Limitation:** these fish reproduce HCM/heart-failure and electrophysiologic features, not demonstrated left-ventricular noncompaction. Zebrafish also lack the human four-chamber ventricular anatomy.

### Human cellular models

Patient-derived or engineered iPSC-cardiomyocytes and multicellular cardiac organoids permit contractility, calcium, mitochondrial, transcriptomic, spatial-cellular, and drug-response measurements. The 2024 studies provide evidence for sarcomere disruption, metabolic remodeling, oxidative stress, and hypercontractility. Their principal limitations are cellular immaturity, model-specific loading conditions, and modeling of HCM/dilated-HCM rather than validated LVNC morphology. (desai2024mybpc3d389vvariant pages 1-2, mori2024metabolicremodelingand pages 1-2)

### Mouse models

MYBPC3 mouse models are extensively used in HCM research, but the retrieved evidence did not identify a patient-variant mouse model that reproducibly recapitulates LVNC10 morphology. Mouse findings should therefore support cMyBP-C biology, not be asserted as direct LVNC10 validation.

---

## Recent developments and expert interpretation, 2023–2024

1. **Nosologic shift:** The 2023 ESC cardiomyopathy guidance, summarized in April 2024, treats hypertrabeculation as a dynamic trait across healthy, adaptive, congenital, hematologic, renal, and cardiomyopathic states. Expert practice consequently emphasizes deep phenotyping and genetics over an imaging ratio alone. DOI: https://doi.org/10.1093/eurheartjsupp/suae002. (grasso2024thenew2023 pages 1-2)
2. **Updated epidemiology:** The October 2024 meta-analysis estimated generic adult LVNC prevalence at 0.5%, mortality at 12%, and transplantation at 7%, while emphasizing heterogeneity and the adverse importance of NYHA III/IV status, ventricular tachycardia, and reduced LVEF. DOI: https://doi.org/10.14740/cr1673. (llerenavelastegui2024prevalenceclinicalmanifestations pages 1-2)
3. **Functional precision models:** 2024 MYBPC3 iPSC and organoid studies connected sarcomeric variants to calcium-handling defects, mitochondrial/energetic remodeling, oxidative stress, and drug-responsive hypercontractility. These are promising for variant interpretation and screening but do not yet bridge MYBPC3 dysfunction specifically to noncompaction morphogenesis. (desai2024mybpc3d389vvariant pages 1-2, mori2024metabolicremodelingand pages 1-2)
4. **Prospective risk research:** NCT06024759 is implementing a 500-person, decade-long registry combining genetics, strain, arrhythmia burden, ventricular function, and ICD outcomes. (NCT06024759 chunk 1)

## Knowledge gaps and curation cautions

- No reliable LVNC10-specific prevalence, incidence, sex ratio, penetrance curve, survival curve, or treatment-response rate exists.
- Generic LVNC statistics should be tagged as **indirect evidence** for LVNC10.
- Imaging morphology alone should not be equated with genetic disease.
- The direct developmental mechanism connecting cMyBP-C deficiency to excessive trabeculation remains inferred.
- No validated protective factor, environmental cause, epigenetic signature, circulating biomarker, or targeted therapy is established.
- Exact ClinVar status and population frequency must be checked separately for every variant and transcript version.
- PMID metadata was not consistently exposed in the retrieved full texts; DOIs and publication dates above are supplied where verified rather than assigning uncertain PMIDs.

References

1. (OpenTargets Search: Left ventricular noncompaction 10): Open Targets Query (Left ventricular noncompaction 10, 23 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (grasso2024thenew2023 pages 1-2): Maurizia Grasso, Davide Bondavalli, Viviana Vilardo, Claudia Cavaliere, Ilaria Gatti, Alessandro Di Toro, Lorenzo Giuliani, Mario Urtis, Michela Ferrari, Barbara Cattadori, Alessandra Serio, Carlo Pellegrini, and Eloisa Arbustini. The new 2023 esc guidelines for the management of cardiomyopathies: a guiding path for cardiologist decisions. European Heart Journal Supplements : Journal of the European Society of Cardiology, 26:i1-i5, Apr 2024. URL: https://doi.org/10.1093/eurheartjsupp/suae002, doi:10.1093/eurheartjsupp/suae002. This article has 18 citations.

3. (probst2011sarcomeregenemutations pages 8-9): Susanne Probst, Erwin Oechslin, Pia Schuler, Matthias Greutmann, Philipp Boyé, Walter Knirsch, Felix Berger, Ludwig Thierfelder, Rolf Jenni, and Sabine Klaassen. Sarcomere gene mutations in isolated left ventricular noncompaction cardiomyopathy do not predict clinical phenotype. Circulation: Cardiovascular Genetics, 4:367–374, Aug 2011. URL: https://doi.org/10.1161/circgenetics.110.959270, doi:10.1161/circgenetics.110.959270. This article has 268 citations.

4. (wessels2015compoundheterozygousor pages 1-2): Marja W Wessels, Johanna C Herkert, Ingrid M Frohn-Mulder, Michiel Dalinghaus, Arthur van den Wijngaard, Ronald R de Krijger, Michelle Michels, Irenaeus FM de Coo, Yvonne M Hoedemaekers, and Dennis Dooijes. Compound heterozygous or homozygous truncating mybpc3 mutations cause lethal cardiomyopathy with features of noncompaction and septal defects. European Journal of Human Genetics, 23:922-928, Oct 2015. URL: https://doi.org/10.1038/ejhg.2014.211, doi:10.1038/ejhg.2014.211. This article has 121 citations and is from a domain leading peer-reviewed journal.

5. (sedaghathamedani2017clinicalgeneticsand pages 1-2): Farbod Sedaghat-Hamedani, Jan Haas, Feng Zhu, Christian Geier, Elham Kayvanpour, Martin Liss, Alan Lai, Karen Frese, Regina Pribe-Wolferts, Ali Amr, Daniel Tian Li, Omid Shirvani Samani, Avisha Carstensen, Diana Martins Bordalo, Marion Müller, Christine Fischer, Jing Shao, Jing Wang, Ming Nie, Li Yuan, Sabine Haßfeld, Christine Schwartz, Min Zhou, Zihua Zhou, Yanwen Shu, Min Wang, Kai Huang, Qiutang Zeng, Longxian Cheng, Tobias Fehlmann, Philipp Ehlermann, Andreas Keller, Christoph Dieterich, Katrin Streckfuß-Bömeke, Yuhua Liao, Michael Gotthardt, Hugo A Katus, and Benjamin Meder. Clinical genetics and outcome of left ventricular non-compaction cardiomyopathy. European Heart Journal, 38:3449–3460, Dec 2017. URL: https://doi.org/10.1093/eurheartj/ehx545, doi:10.1093/eurheartj/ehx545. This article has 281 citations and is from a highest quality peer-reviewed journal.

6. (hirono2022leftventricularnoncompaction pages 1-2): Keiichi Hirono and Fukiko Ichida. Left ventricular noncompaction: a disorder with genotypic and phenotypic heterogeneity—a narrative review. Cardiovascular Diagnosis and Therapy, 12:495-515, Aug 2022. URL: https://doi.org/10.21037/cdt-22-198, doi:10.21037/cdt-22-198. This article has 24 citations.

7. (wessels2015compoundheterozygousor pages 2-3): Marja W Wessels, Johanna C Herkert, Ingrid M Frohn-Mulder, Michiel Dalinghaus, Arthur van den Wijngaard, Ronald R de Krijger, Michelle Michels, Irenaeus FM de Coo, Yvonne M Hoedemaekers, and Dennis Dooijes. Compound heterozygous or homozygous truncating mybpc3 mutations cause lethal cardiomyopathy with features of noncompaction and septal defects. European Journal of Human Genetics, 23:922-928, Oct 2015. URL: https://doi.org/10.1038/ejhg.2014.211, doi:10.1038/ejhg.2014.211. This article has 121 citations and is from a domain leading peer-reviewed journal.

8. (wessels2015compoundheterozygousor pages 5-6): Marja W Wessels, Johanna C Herkert, Ingrid M Frohn-Mulder, Michiel Dalinghaus, Arthur van den Wijngaard, Ronald R de Krijger, Michelle Michels, Irenaeus FM de Coo, Yvonne M Hoedemaekers, and Dennis Dooijes. Compound heterozygous or homozygous truncating mybpc3 mutations cause lethal cardiomyopathy with features of noncompaction and septal defects. European Journal of Human Genetics, 23:922-928, Oct 2015. URL: https://doi.org/10.1038/ejhg.2014.211, doi:10.1038/ejhg.2014.211. This article has 121 citations and is from a domain leading peer-reviewed journal.

9. (mazzarotto2020thegeneticarchitecture pages 1-3): Francesco Mazzarotto, Megan H. Hawley, Matteo Beltrami, Leander Beekman, Antonio de Marvao, Kathryn A. McGurk, Ben Statton, Beatrice Boschi, Francesca Girolami, Angharad M. Roberts, Elisabeth M. Lodder, Mona Allouba, Soha Romeih, Yasmine Aguib, A. John Baksi, Antonis Pantazis, Sanjay K. Prasad, Elisabetta Cerbai, Magdi H. Yacoub, Declan P. O’Regan, Stuart A. Cook, James S. Ware, Birgit Funke, Iacopo Olivotto, Connie R. Bezzina, Paul J.R. Barton, and Roddy Walsh. The genetic architecture of left ventricular non-compaction reveals both substantial overlap with other cardiomyopathies and a distinct aetiology in a subset of cases. European Heart Journal, Jan 2020. URL: https://doi.org/10.1101/2020.01.03.19015602, doi:10.1101/2020.01.03.19015602. This article has 4 citations and is from a highest quality peer-reviewed journal.

10. (wessels2015compoundheterozygousor pages 3-4): Marja W Wessels, Johanna C Herkert, Ingrid M Frohn-Mulder, Michiel Dalinghaus, Arthur van den Wijngaard, Ronald R de Krijger, Michelle Michels, Irenaeus FM de Coo, Yvonne M Hoedemaekers, and Dennis Dooijes. Compound heterozygous or homozygous truncating mybpc3 mutations cause lethal cardiomyopathy with features of noncompaction and septal defects. European Journal of Human Genetics, 23:922-928, Oct 2015. URL: https://doi.org/10.1038/ejhg.2014.211, doi:10.1038/ejhg.2014.211. This article has 121 citations and is from a domain leading peer-reviewed journal.

11. (wang2017awideand pages 1-2): Ce Wang, Yukiko Hata, Keiichi Hirono, Asami Takasaki, Sayaka Watanabe Ozawa, Hideyuki Nakaoka, Kazuyoshi Saito, Nariaki Miyao, Mako Okabe, Keijiro Ibuki, Naoki Nishida, Hideki Origasa, Xianyi Yu, Neil E. Bowles, and Fukiko Ichida. A wide and specific spectrum of genetic variants and genotype–phenotype correlations revealed by next‐generation sequencing in patients with left ventricular noncompaction. Sep 2017. URL: https://doi.org/10.1161/jaha.117.006210, doi:10.1161/jaha.117.006210. This article has 79 citations.

12. (martineztittonel2025leftventricularnoncompaction pages 5-7): Luis Elias Martínez-Tittonel, Florin Ciorba, Xavier Bayona-Huguet, and Edgardo Kaplinsky. Left ventricular non-compaction cardiomyopathy: a review of the pathophysiology, epidemiology, diagnosis, genetics, and clinical management. Jul 2025. URL: https://doi.org/10.20944/preprints202507.1652.v1, doi:10.20944/preprints202507.1652.v1.

13. (llerenavelastegui2024prevalenceclinicalmanifestations pages 1-2): Jordan Llerena-Velastegui, Almendra Lopez-Usina, and Camila Mantilla-Cisneros. Prevalence, clinical manifestations, and adverse outcomes of left ventricular noncompaction in adults: a systematic review and meta-analysis. Oct 2024. URL: https://doi.org/10.14740/cr1673, doi:10.14740/cr1673. This article has 6 citations.

14. (aung2020prognosticsignificanceof pages 1-2): Nay Aung, Sara Doimo, Fabrizio Ricci, Mihir M. Sanghvi, Cesar Pedrosa, Simon P. Woodbridge, Amer Al-Balah, Filip Zemrak, Mohammed Y. Khanji, Patricia B. Munroe, Huseyin Naci, and Steffen E. Petersen. Prognostic significance of left ventricular noncompaction. Circulation. Cardiovascular Imaging, 13:e009712-e009712, Jan 2020. URL: https://doi.org/10.1161/circimaging.119.009712, doi:10.1161/circimaging.119.009712. This article has 143 citations.

15. (hirono2022thromboemboliceventsin pages 1-2): Keiichi Hirono, Shinya Takarada, Nariaki Miyao, Hideyuki Nakaoka, Keijiro Ibuki, Sayaka Ozawa, Hideki Origasa, and Fukiko Ichida. Thromboembolic events in left ventricular non-compaction: comparison between children and adults – a systematic review and meta-analysis. Open Heart, 9(1):e001908, May 2022. URL: https://doi.org/10.1136/openhrt-2021-001908, doi:10.1136/openhrt-2021-001908. This article has 23 citations and is from a peer-reviewed journal.

16. (kolokotronis2019biallelicmutationin pages 7-9): Konstantinos Kolokotronis, Jirko Kühnisch, Eva Klopocki, Josephine Dartsch, Simone Rost, Cathleen Huculak, Giulia Mearini, Stefan Störk, Lucie Carrier, Sabine Klaassen, and Brenda Gerull. Biallelic mutation in myh7 and mybpc3 leads to severe cardiomyopathy with left ventricular noncompaction phenotype. Human Mutation, 40:1101-1114, Aug 2019. URL: https://doi.org/10.1002/humu.23757, doi:10.1002/humu.23757. This article has 46 citations and is from a domain leading peer-reviewed journal.

17. (desai2024mybpc3d389vvariant pages 1-2): Darshini Desai, Taejeong Song, Rohit R. Singh, Akhil Baby, James McNamara, Lisa C. Green, Pooneh Nabavizadeh, Mark Ericksen, Sholeh Bazrafshan, Sankar Natesan, and Sakthivel Sadayappan. Mybpc3 d389v variant induces hypercontractility in cardiac organoids. Nov 2024. URL: https://doi.org/10.3390/cells13221913, doi:10.3390/cells13221913. This article has 10 citations.

18. (mori2024metabolicremodelingand pages 1-2): Haruka Mori, Dongzhu Xu, Yuzuno Shimoda, Zixun Yuan, Yoshiko Murakata, Binyang Xi, Kimi Sato, Masayoshi Yamamoto, Kazuko Tajiri, Tomoko Ishizu, Masaki Ieda, and Nobuyuki Murakoshi. Metabolic remodeling and calcium handling abnormality in induced pluripotent stem cell-derived cardiomyocytes in dilated phase of hypertrophic cardiomyopathy with mybpc3 frameshift mutation. Jul 2024. URL: https://doi.org/10.1038/s41598-024-62530-0, doi:10.1038/s41598-024-62530-0. This article has 13 citations and is from a peer-reviewed journal.

19. (da’as2022transcriptomeprofileidentifies pages 11-13): Sahar Isa Da’as, Waseem Hasan, Rola Salem, Nadine Younes, Doua Abdelrahman, Iman A. Mohamed, Arwa Aldaalis, Ramzi Temanni, Lisa Sara Mathew, Stephan Lorenz, Magdi Yacoub, Michail Nomikos, Gheyath K. Nasrallah, and Khalid A. Fakhro. Transcriptome profile identifies actin as an essential regulator of cardiac myosin binding protein c3 hypertrophic cardiomyopathy in a zebrafish model. Aug 2022. URL: https://doi.org/10.3390/ijms23168840, doi:10.3390/ijms23168840. This article has 9 citations.

20. (chen2013inactivationofmyosin pages 1-2): Yau‐Hung Chen, Chiung‐Wen Pai, Shu‐Wei Huang, Sheng‐Nan Chang, Lian‐Yu Lin, Fu‐Tien Chiang, Jiunn‐Lee Lin, Juey‐Jen Hwang, and Chia‐Ti Tsai. Inactivation of myosin binding protein c homolog in zebrafish as a model for human cardiac hypertrophy and diastolic dysfunction. Sep 2013. URL: https://doi.org/10.1161/jaha.113.000231, doi:10.1161/jaha.113.000231. This article has 44 citations.

21. (NCT06024759 chunk 1):  Predictors of Risk in Left Ventricular Non-Compaction. London Health Sciences Centre Research Institute OR Lawson Research Institute of St. Joseph's. 2023. ClinicalTrials.gov Identifier: NCT06024759

22. (NCT06024759 chunk 2):  Predictors of Risk in Left Ventricular Non-Compaction. London Health Sciences Centre Research Institute OR Lawson Research Institute of St. Joseph's. 2023. ClinicalTrials.gov Identifier: NCT06024759

23. (da’as2022transcriptomeprofileidentifies pages 1-2): Sahar Isa Da’as, Waseem Hasan, Rola Salem, Nadine Younes, Doua Abdelrahman, Iman A. Mohamed, Arwa Aldaalis, Ramzi Temanni, Lisa Sara Mathew, Stephan Lorenz, Magdi Yacoub, Michail Nomikos, Gheyath K. Nasrallah, and Khalid A. Fakhro. Transcriptome profile identifies actin as an essential regulator of cardiac myosin binding protein c3 hypertrophic cardiomyopathy in a zebrafish model. Aug 2022. URL: https://doi.org/10.3390/ijms23168840, doi:10.3390/ijms23168840. This article has 9 citations.

24. (da’as2022transcriptomeprofileidentifies pages 2-4): Sahar Isa Da’as, Waseem Hasan, Rola Salem, Nadine Younes, Doua Abdelrahman, Iman A. Mohamed, Arwa Aldaalis, Ramzi Temanni, Lisa Sara Mathew, Stephan Lorenz, Magdi Yacoub, Michail Nomikos, Gheyath K. Nasrallah, and Khalid A. Fakhro. Transcriptome profile identifies actin as an essential regulator of cardiac myosin binding protein c3 hypertrophic cardiomyopathy in a zebrafish model. Aug 2022. URL: https://doi.org/10.3390/ijms23168840, doi:10.3390/ijms23168840. This article has 9 citations.

## Artifacts

- [Edison artifact artifact-00](Left_Ventricular_Noncompaction_10-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014163` (7 mentions) - the report calls it "if available"; MONDO calls it **left ventricular noncompaction 10**
- `HP:0011664` (7 mentions) - the report calls it "Imaging sign; congenital substrate or later-recognized trait; severity and progression variable"; HP calls it **Left ventricular noncompaction cardiomyopathy**