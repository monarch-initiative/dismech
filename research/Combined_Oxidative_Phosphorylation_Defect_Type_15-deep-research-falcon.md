---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-16T03:44:40.801719'
end_time: '2026-09-16T03:57:16.453983'
duration_seconds: 755.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Defect Type 15
  mondo_id: MONDO:0013987
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 52
  verified: 51
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013987
    reported_labels:
    - if available
    ontology_label: combined oxidative phosphorylation defect type 15
  obsolete_terms:
  - term_id: GO:0005751
    ontology_label: obsolete mitochondrial respiratory chain complex IV
    replaced_by: GO:0045277
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Combined_Oxidative_Phosphorylation_Defect_Type_15-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 15
- **MONDO ID:** MONDO:0013987 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 15** covering all of the
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
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 15
- **MONDO ID:** MONDO:0013987 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 15** covering all of the
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


# Combined Oxidative Phosphorylation Defect Type 15 (COXPD15): Research Report

## Executive summary

Combined oxidative phosphorylation defect type 15 is an ultra-rare, autosomal-recessive mitochondrial encephalomyopathy caused by biallelic loss-of-function variants in **TACO1**, the nuclear gene encoding the mitochondrial translational activator of cytochrome-c-oxidase subunit I. Despite its historical “combined OXPHOS defect” name, the demonstrated biochemical signature is predominantly an **isolated respiratory-chain complex IV deficiency** caused by defective translation of mitochondrial **MT-CO1/COXI**. The reported human phenotype is a childhood- or adolescent-onset, slowly progressive spastic-ataxic disorder with optic atrophy, learning or developmental difficulties, short stature, lactate elevation, and Leigh-like or cystic white-matter abnormalities. Evidence remains limited to a few consanguineous pedigrees and individual cases; prevalence, penetrance, survival, and treatment-response rates therefore cannot be estimated reliably. (weraarpachai2012identificationandcharacterization pages 62-66, weraarpachai2012identificationandcharacterization pages 66-72, oktay2020confirmationoftaco1 pages 3-5)

The principal evidence base is summarized below.

| Domain | Knowledge-base fact | Evidence type/strength |
|---|---|---|
| Identity | Combined oxidative phosphorylation defect type 15 (COXPD15); **MONDO:0013987**. | Curated disease-ontology identifier; strong identity evidence (OpenTargets Search: combined oxidative phosphorylation deficiency 15-MSTO1, OpenTargets Search: combined oxidative phosphorylation defect type 15-TACO1) |
| Causal gene | Caused by **biallelic loss-of-function variants in TACO1**, encoding translational activator of cytochrome-c oxidase I. | Human genetic segregation plus patient-cell functional evidence; strong, but based on very few families (OpenTargets Search: combined oxidative phosphorylation defect type 15-TACO1, oktay2020confirmationoftaco1 pages 3-5, weraarpachai2012identificationandcharacterizationa pages 62-66) |
| Inheritance | **Autosomal recessive**; affected individuals were homozygous and parents/unaffected siblings were heterozygous in reported consanguineous pedigrees. | Human familial segregation; strong for inheritance, small case count (weraarpachai2012identificationandcharacterization pages 66-72, oktay2020confirmationoftaco1 pages 3-5) |
| Pathogenic variants | Reported frameshifts include **c.472dupC (historically 472insC), p.His158ProfsTer8** and **c.252_253delCT, p.Cys85PhefsTer15**; both predict premature termination and loss of function. | Human sequencing and segregation; c.472dupC may be a rare Turkish founder allele; limited families (oktay2020confirmationoftaco1 pages 3-5, weraarpachai2012identificationandcharacterizationa pages 62-66) |
| Onset/course | Typical reported onset is **childhood to adolescence, approximately 4–16 years**, followed by slow but progressive neurologic decline; marked intrafamilial variability occurs. | Human case-series evidence; moderate strength because numbers are very small (weraarpachai2012identificationandcharacterization pages 66-72, weraarpachai2012identificationandcharacterizationa pages 147-151, weraarpachai2012identificationandcharacterization pages 147-151) |
| Core phenotype | Progressive **spastic-ataxic syndrome** with gait impairment, pyramidal signs, cerebellar/upper-limb ataxia, dysarthria, dysphagia, dystonic movements, weakness, amyotrophy, and eventual loss of ambulation in severe cases. | Recurrent human clinical observations; moderate strength, no reliable percentages (weraarpachai2012identificationandcharacterization pages 66-72, oktay2020confirmationoftaco1 pages 3-5) |
| Ophthalmologic phenotype | Progressive **optic atrophy and visual loss**; one reported patient became legally blind, with visual acuities of 20/400 and 20/250. | Human clinical, fundus, and OCT evidence; moderate strength, few examined patients (oktay2020confirmationoftaco1 pages 3-5) |
| Neurodevelopment/growth | Learning difficulty or mild cognitive impairment, developmental/speech delay or regression, and **short stature** have been reported. | Human case evidence; limited and not sufficiently numerous for frequency estimates (weraarpachai2012identificationandcharacterization pages 66-72, oktay2020confirmationoftaco1 pages 3-5, weraarpachai2012identificationandcharacterizationa pages 66-72) |
| Neuroimaging | MRI may show Leigh-like lesions and/or progressive **leukoencephalopathy**: confluent periventricular and cerebellar T2 hyperintensities, cystic white-matter defects, cerebral/white-matter atrophy, thin corpus callosum, and middle cerebellar peduncle involvement; patterns vary between families. | Human MRI/MRS evidence; moderate strength, phenotype appears variable (oktay2020confirmationoftaco1 pages 3-5, weraarpachai2012identificationandcharacterizationa pages 66-72) |
| Laboratory phenotype | Elevated lactate was documented in serum (**4.1 mmol/L**) and CSF (**3.2 mmol/L**); MRS may show a strong lactate peak. | Human biochemical/imaging evidence; supportive but neither universal nor disease-specific (weraarpachai2012identificationandcharacterization pages 66-72, oktay2020confirmationoftaco1 pages 3-5) |
| Respiratory-chain defect | Predominantly **isolated complex IV/cytochrome-c-oxidase deficiency**, with approximately **15% residual activity in skeletal muscle** and **29% in fibroblasts** in the original family; other respiratory complexes were largely normal. | Human tissue and cell enzyme assays; strong disease-specific functional evidence, but values derive from a small number of subjects (weraarpachai2012identificationandcharacterization pages 147-151, weraarpachai2012identificationandcharacterization pages 66-72) |
| Molecular mechanism | TACO1 loss impairs efficient translation/completion of mitochondrial **MT-CO1/COXI**, producing truncated products, reduced COXI synthesis, destabilization of COX subunits, defective complex-IV assembly, and impaired oxidative phosphorylation. Downstream ATP deficiency and high-energy-tissue injury are biologically compelling but partly inferred rather than directly quantified in patients. | Patient-cell pulse-labeling, BN-PAGE, biochemical, and mouse evidence; strong upstream mechanism, inferred distal tissue cascade (weraarpachai2012identificationandcharacterization pages 62-66, weraarpachai2012identificationandcharacterization pages 151-155, richman2016lossofthe pages 1-2) |
| Functional rescue | Expression of wild-type **TACO1** in patient fibroblasts restored COXI synthesis and complex-IV assembly/activity to **104% of control**. | Direct patient-cell complementation; very strong causal evidence, preclinical only (weraarpachai2012identificationandcharacterization pages 62-66, weraarpachai2012identificationandcharacterizationa pages 62-66) |
| Mouse model | Homozygous ENU-derived **Taco1 p.Ile164Asn (I164N)** mice develop approximately 50% reduced complex-IV activity, impaired COXI translation, adult-onset visual/retinal disease, motor dysfunction, mild cerebellar pathology, and cardiac hypertrophy. | Genetically defined mammalian model; strong mechanistic support, incomplete recapitulation of human disease (richman2016lossofthe pages 11-12, richman2016lossofthe pages 1-2, richman2016lossofthe pages 11-11) |
| Gene–environment interaction | Murine cytomegalovirus infection selectively worsened COXI/assembled complex-IV deficiency in mutant heart and altered neuromuscular morphology and tissue-specific mTOR signaling; equivalent effects in humans remain **unproven**. | Controlled mouse experiment; moderate preclinical evidence, human inference only (ferreira2020murinecytomegalovirusinfection pages 2-3, ferreira2020murinecytomegalovirusinfection pages 1-2) |
| Treatment/trials | **No disease-specific approved therapy and no TACO1-targeted registered clinical trial were identified.** Current care is supportive and extrapolated from general mitochondrial/Leigh-syndrome practice; wild-type cellular rescue has not yet translated into human gene therapy. | Negative trial/database search plus literature review; absence-of-evidence conclusion, not proof that no local/off-label interventions exist (OpenTargets Search: combined oxidative phosphorylation deficiency 15-MSTO1, OpenTargets Search: combined oxidative phosphorylation defect type 15-TACO1) |
| Evidence limitation | Published human evidence comprises only a few consanguineous pedigrees and individual cases; phenotype frequencies, penetrance, prevalence, survival, sex effects, and treatment-response rates cannot be estimated reliably. | Critical evidence-quality assessment; high confidence that available human data are sparse (oktay2020confirmationoftaco1 pages 3-5, weraarpachai2012identificationandcharacterizationa pages 147-151, oktay2020confirmationoftaco1 pages 7-8) |


*Table: Compact knowledge-base summary of COXPD15 identity, genetics, phenotype, mechanism, models, and treatment status. It distinguishes strong human or functional evidence from small-sample observations and preclinical inference.*

## 1. Disease information

**Definition.** COXPD15 is a nuclear-encoded mitochondrial translation disorder in which TACO1 deficiency impairs synthesis of COXI, destabilizes complex-IV assembly, and causes progressive neurological, visual, and neuromuscular disease. Clinical labels overlap with **late-onset Leigh syndrome**, **TACO1-related mitochondrial disease**, and **autosomal-recessive spastic ataxia with leukoencephalopathy and optic atrophy**. (weraarpachai2012identificationandcharacterization pages 66-72, oktay2020confirmationoftaco1 pages 3-5, weraarpachai2012identificationandcharacterizationa pages 62-66)

**Identifiers and nomenclature**

- MONDO: **MONDO:0013987**, “combined oxidative phosphorylation defect type 15.” Open Targets maps this disease to **TACO1/ENSG00000136463**. (OpenTargets Search: combined oxidative phosphorylation deficiency 15-MSTO1, OpenTargets Search: combined oxidative phosphorylation defect type 15-TACO1)
- OMIM disease: commonly catalogued as **Combined oxidative phosphorylation deficiency 15, COXPD15; OMIM 615119**; TACO1 gene: **OMIM 612958**.
- Gene name: **TACO1**, translational activator of cytochrome-c oxidase I; older name **CCDC44**.
- ICD-10/ICD-11 and MeSH do not provide a disease-specific COXPD15 code. Cases are generally represented under broader mitochondrial metabolism/mitochondrial encephalopathy or Leigh-syndrome categories. Such broad coding should not be treated as equivalent to a molecular TACO1 diagnosis.
- A disease-specific Orphanet identifier could not be verified from the retrieved evidence; broader Leigh syndrome and mitochondrial complex-IV-deficiency records may be used by clinical databases.

The evidence is primarily **aggregated disease-level literature derived from deeply characterized individual patients and families**, not EHR-scale population data. The 2020 confirmation paper described two additional independent consanguineous families after the original single extended Turkish pedigree. (oktay2020confirmationoftaco1 pages 3-5, oktay2020confirmationoftaco1 pages 7-8)

## 2. Etiology

### Causal and risk factors

The necessary causal factor is a **biallelic pathogenic germline TACO1 genotype**. Reported pathogenic alleles are severe frameshifts predicted to cause nonsense-mediated decay or absent protein:

- **c.472dupC**—originally reported as 472insC—**p.His158ProfsTer8**.
- **c.252_253delCT, p.Cys85PhefsTer15**. (oktay2020confirmationoftaco1 pages 3-5, weraarpachai2012identificationandcharacterizationa pages 62-66)

Both were homozygous in affected individuals and heterozygous in parents; healthy siblings in the informative family were heterozygous. The c.472dupC allele occurred on a shared haplotype in Turkish families, supporting a **rare founder mutation**, although its population carrier frequency has not been established. (oktay2020confirmationoftaco1 pages 3-5)

No common susceptibility loci, validated modifier genes, environmental primary causes, or somatic TACO1 causes are known. Apparent sex differences in the original pedigree—boys losing ambulation near age 10 while affected girls remained ambulatory into their twenties—suggest possible biological or stochastic modifiers, but the sample is far too small to establish sex as a risk factor. (weraarpachai2012identificationandcharacterization pages 147-151)

### Protective factors and gene–environment interaction

No protective human allele, diet, lifestyle exposure, or prophylactic drug has been demonstrated. In Taco1-mutant mice, murine cytomegalovirus infection further reduced COXI and assembled complex IV in the heart and altered neuromuscular morphology and tissue-specific mTOR signaling. This is credible **preclinical gene–environment evidence**, but it does not establish cytomegalovirus or another infection as a human COXPD15 trigger. (ferreira2020murinecytomegalovirusinfection pages 2-3, ferreira2020murinecytomegalovirusinfection pages 1-2)

## 3. Phenotypes

Reliable percentages cannot be assigned because only a few families have been published. “Recurrent” below means observed across more than one reported patient/family, not a population frequency.

| Phenotype and type | Characteristics | Suggested HPO term |
|---|---|---|
| Progressive gait impairment; clinical sign | Usually begins in childhood/adolescence; spastic and ataxic components; progressive loss of independent walking in severe cases | Spastic gait **HP:0002064**; gait ataxia **HP:0002066** |
| Cerebellar/limb ataxia; sign | Progressive; upper limbs and gait involved | Cerebellar ataxia **HP:0001251**; limb ataxia **HP:0002070** |
| Pyramidal syndrome; sign | Hyperreflexia, spastic paraplegia or tetraparesis | Spasticity **HP:0001257**; pyramidal signs **HP:0007256** |
| Dysarthria/dysphagia; symptom/sign | Progressive bulbar and cerebellar dysfunction | Dysarthria **HP:0001260**; dysphagia **HP:0002015** |
| Dystonic movements; sign | Reported in the original family | Dystonia **HP:0001332** |
| Weakness, amyotrophy, myopathy/neuropathy; sign/test | Variable; electrophysiology may evolve from myopathic to sensorimotor neuropathic findings | Muscle weakness **HP:0001324**; muscle atrophy **HP:0003202**; sensorimotor neuropathy **HP:0007141** |
| Optic atrophy and visual loss; sign | Progressive and potentially severe; one patient had acuities of 20/400 and 20/250 and was legally blind | Optic atrophy **HP:0000648**; decreased visual acuity **HP:0007663** |
| Developmental/speech delay, learning difficulty; neurodevelopmental | Mild to moderate and variable; developmental regression has also been described | Global developmental delay **HP:0001263**; learning disability **HP:0001328**; speech delay **HP:0000750** |
| Short stature; physical manifestation | Reported in the original pedigree | Short stature **HP:0004322** |
| Lactic acid elevation; laboratory | Serum 4.1 mmol/L and CSF 3.2 mmol/L in an original patient; MRS lactate peak in a later case | Lactic acidosis **HP:0003128**; elevated CSF lactate **HP:0011971** |
| Complex-IV deficiency; laboratory/pathology | Approximately 15% residual activity in skeletal muscle and 29% in fibroblasts in the original family | Decreased mitochondrial complex IV activity **HP:0011925** |
| Leukoencephalopathy; imaging | Periventricular/cerebellar T2 hyperintensity, cystic defects, atrophy, thin corpus callosum, and middle cerebellar peduncle involvement | Leukoencephalopathy **HP:0002352**; cerebral white-matter atrophy **HP:0012444** |
| Leigh-like lesions; imaging | Bilateral symmetric basal-ganglia lesions were described in the original pedigree, whereas basal-ganglia abnormalities were absent in later families | Bilateral basal ganglia lesions **HP:0007146** |

These manifestations substantially impair mobility, communication, swallowing, vision, education, and independence. No disease-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or other quality-of-life study was found. The functional impact is therefore inferred from loss of ambulation, legal blindness, learning disability, and progressive neurological impairment rather than quantified by validated instruments. (weraarpachai2012identificationandcharacterization pages 66-72, oktay2020confirmationoftaco1 pages 3-5)

## 4. Genetic and molecular information

**Causal gene.** TACO1 is located on chromosome 17q and encodes a 297-amino-acid precursor with an approximately 26-amino-acid mitochondrial targeting sequence; the mature matrix protein is approximately 29.8 kDa and participates in an approximately 74-kDa complex. It binds or functionally recognizes MT-CO1 mRNA and associates with the mitochondrial ribosome, promoting efficient full-length COXI translation. (weraarpachai2012identificationandcharacterization pages 62-66, weraarpachai2012identificationandcharacterizationa pages 62-66, richman2016lossofthe pages 1-2)

**Variant interpretation.** Both reported human variants are germline, homozygous frameshifts with premature termination and are appropriately regarded as pathogenic/likely pathogenic loss-of-function alleles when segregation, phenotype, and functional evidence are considered. The original c.472dupC variant markedly reduced transcript and eliminated detectable TACO1 protein. It was absent from 100 historical controls; current ancestry-specific gnomAD frequencies were not available in the retrieved evidence. (weraarpachai2012identificationandcharacterization pages 62-66, oktay2020confirmationoftaco1 pages 3-5)

No disease-associated missense allele, structural rearrangement, chromosomal aneuploidy, repeat expansion, mitochondrial-DNA mutation, established modifier gene, or reproducible epigenetic signature has been demonstrated in human COXPD15. The mouse **Taco1 p.Ile164Asn** allele is a model allele, not a reported human pathogenic variant. (richman2016lossofthe pages 11-12, richman2016lossofthe pages 1-2)

## 5. Environmental information

COXPD15 is not caused by toxins, radiation, pollution, occupation, diet, smoking, alcohol, or infection. No lifestyle association has been studied. General mitochondrial stressors—prolonged fasting, severe illness, dehydration, fever, anesthesia, and mitochondrially toxic drugs—are clinically relevant precautions by extrapolation from mitochondrial medicine, but none has been evaluated specifically in TACO1 patients.

The only direct environmental experiment is MCMV infection in mice. Infection exacerbated the cardiac complex-IV defect but not the liver defect, while mutant animals retained broadly effective antiviral lymphocyte responses. Thus, infection can modify biochemical disease expression in a model without being the inherited cause. (ferreira2020murinecytomegalovirusinfection pages 2-3)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic TACO1 loss-of-function leads to** loss or marked reduction of mitochondrial matrix TACO1 protein.  
2. **Loss of TACO1 leads to** inefficient translation and completion of mitochondrial **MT-CO1/COXI**, despite relatively preserved MT-CO1 RNA abundance.  
3. **Defective COXI synthesis results in** truncated COXI products and instability of newly synthesized COXI, COXII, and COXIII.  
4. **Loss of core COX subunits leads to** defective complex-IV assembly, accumulation of a small approximately 135-kDa subcomplex, and severe isolated cytochrome-c-oxidase deficiency.  
5. **Complex-IV deficiency results in** impaired electron transfer to oxygen, reduced respiratory capacity and proton-motive-force generation; diminished ATP production and altered redox balance are strongly inferred from OXPHOS biology and supported in the mouse, but were not comprehensively quantified in human tissues.  
6. **Bioenergetic/redox failure leads to** lactate accumulation and selective dysfunction of energy-demanding neurons, oligodendroglial/white-matter systems, retinal ganglion cells/optic nerve, skeletal muscle, and peripheral motor pathways. This cellular selectivity is partly inferred.  
7. **Tissue dysfunction results in** spasticity, ataxia, weakness, optic atrophy, cognitive/learning impairment, leukoencephalopathy, and progressive disability.  
8. **Branch—environmental stress:** viral infection in Taco1-mutant mice **leads to** tissue-specific mTOR and neuromuscular changes and further cardiac complex-IV impairment; translation to humans is unproven. (weraarpachai2012identificationandcharacterization pages 62-66, weraarpachai2012identificationandcharacterization pages 151-155, ferreira2020murinecytomegalovirusinfection pages 2-3, richman2016lossofthe pages 1-2)

The strongest causality experiment is complementation: wild-type TACO1 restored patient-cell COXI synthesis, complex-IV assembly, and COX activity to **104% of control**. This demonstrates that the upstream lesion is TACO1 deficiency rather than a coincident mtDNA abnormality. (weraarpachai2012identificationandcharacterization pages 62-66, weraarpachai2012identificationandcharacterizationa pages 62-66)

**Suggested ontology annotations**

- GO biological process: mitochondrial translation (**GO:0032543**); mitochondrial gene expression (**GO:0140053**); respiratory electron transport chain (**GO:0022904**); oxidative phosphorylation (**GO:0006119**); ATP metabolic process (**GO:0046034**); cellular response to oxidative stress (**GO:0034599**, downstream/inferred).
- GO molecular function: RNA binding (**GO:0003723**), supported by mouse biochemical evidence.
- GO cellular component: mitochondrial matrix (**GO:0005759**); mitochondrial ribosome (**GO:0005761**, association); respiratory-chain complex IV (**GO:0005751**, downstream affected complex); mitochondrial inner membrane (**GO:0005743**).
- Suggested CL terms: neuron **CL:0000540**; Purkinje neuron **CL:0000121**; retinal ganglion cell **CL:0000740**; oligodendrocyte **CL:0000128**; skeletal muscle fiber **CL:0000188**; cardiomyocyte **CL:0000746**. Purkinje and retinal involvement is supported particularly by the mouse; oligodendrocyte involvement is inferred from imaging.

No disease-specific single-cell, spatial-transcriptomic, patient proteomic, metabolomic, lipidomic, epigenomic, or CRISPR-screen study was identified through 2024. Human molecular profiling is principally targeted enzyme analysis, pulse-labeling, immunoblotting, and BN-PAGE.

## 7. Anatomical structures affected

The principal system is the **central nervous system**, particularly cerebral white matter, cerebellar systems, corticospinal tracts, optic nerves/visual pathways, and variably basal ganglia. Peripheral nerve and skeletal muscle involvement can emerge during progression. Human cardiac disease has not been established, although mutant mice develop cardiac hypertrophy. (oktay2020confirmationoftaco1 pages 3-5, richman2016lossofthe pages 11-12)

Suggested anatomy annotations include brain **UBERON:0000955**, cerebral white matter **UBERON:0002437**, cerebellum **UBERON:0002037**, basal ganglion **UBERON:0002420**, corpus callosum **UBERON:0002336**, middle cerebellar peduncle, optic nerve **UBERON:0000962**, retina **UBERON:0000966**, spinal cord **UBERON:0002240**, peripheral nerve **UBERON:0001021**, and skeletal muscle tissue **UBERON:0001134**. MRI abnormalities are usually bilateral, but the precise distribution varies; fixed lateralization is not characteristic.

At the subcellular level, the initiating defect is in the **mitochondrial matrix translation apparatus**, while the affected enzyme is embedded in the **inner mitochondrial membrane**.

## 8. Temporal development

Reported onset spans approximately **4–16 years**, later than classical infantile Leigh syndrome. Early features include gait instability, delayed or worsening speech, learning difficulty, and visual abnormalities. Progression is chronic and generally slow, evolving toward spastic ataxia, dysarthria/dysphagia, severe visual loss, weakness, neuropathy, and reduced or lost ambulation. (weraarpachai2012identificationandcharacterization pages 66-72, weraarpachai2012identificationandcharacterizationa pages 147-151)

The original index patient developed gait instability and worsening speech at age five and could no longer stand or walk by approximately age ten. In the same pedigree, three affected girls became symptomatic at 14–16 years and remained ambulatory into their twenties. Later families demonstrated progressive white-matter and cerebral atrophy. No validated staging system, remission pattern, longitudinal biomarker trajectory, or therapeutic window has been defined. (weraarpachai2012identificationandcharacterization pages 147-151, weraarpachai2012identificationandcharacterization pages 66-72, oktay2020confirmationoftaco1 pages 3-5)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two carrier parents, Mendelian recurrence expectations are 25% affected, 50% carrier, and 25% unaffected/non-carrier for each pregnancy, assuming full penetrance of a severe biallelic genotype. Actual penetrance cannot be calculated from the few reported pedigrees.

All well-characterized families in the retrieved primary literature were consanguineous and Turkish. The c.472dupC shared haplotype suggests a Turkish founder allele, but this does not establish that disease is confined to Turkish ancestry. Consanguinity increases the probability of homozygosity but is not itself a biological cause. (weraarpachai2012identificationandcharacterization pages 66-72, oktay2020confirmationoftaco1 pages 3-5)

No incidence, point prevalence, carrier frequency, sex ratio, or geographic distribution estimate exists for COXPD15. The observed within-family sex difference is hypothesis-generating only. There is no anticipation mechanism because repeat expansion is not implicated. Germline mosaicism has not been reported but cannot be excluded as a low residual counseling risk after apparently de novo findings; all established cases instead support inherited recessive alleles.

## 10. Diagnostics

### Recommended approach

1. **Clinical suspicion:** childhood/adolescent progressive spastic ataxia, optic atrophy, learning difficulty, short stature, and characteristic white-matter disease or Leigh-like MRI.
2. **Baseline laboratory evaluation:** serum lactate, pyruvate, blood gas, CK, liver/renal profile, glucose, amino acids, acylcarnitines, and urine organic acids. Lactate can support mitochondrial disease but is neither sensitive nor TACO1-specific.
3. **Neuroimaging:** brain MRI with diffusion and spectroscopy. Reported findings include periventricular and cerebellar T2 hyperintensity, cystic rarefaction, cerebral/white-matter atrophy, thin corpus callosum, middle cerebellar peduncles, variable basal-ganglia lesions, and an MRS lactate peak. (oktay2020confirmationoftaco1 pages 3-5, weraarpachai2012identificationandcharacterizationa pages 66-72)
4. **Functional assessment:** ophthalmology with acuity, color vision, visual fields, fundus photography, OCT, and visual evoked potentials; neurological examination; PT/OT/speech and swallowing evaluations; ECG/echocardiography; audiology; pulmonary function where indicated; EMG and nerve-conduction testing when weakness or neuropathy is present.
5. **Molecular confirmation:** sequence and deletion/duplication analysis of **TACO1**, preferably within a broad nuclear-plus-mtDNA mitochondrial/Leigh or spastic-ataxia panel, trio WES, or WGS. Both published alleles are small indels detectable by standard NGS and confirmable by Sanger sequencing. WES proved effective in the additional families. (oktay2020confirmationoftaco1 pages 3-5)
6. **Functional confirmation for novel/VUS alleles:** fibroblast or muscle complex-IV activity, respiratory studies, TACO1 immunoblotting, BN-PAGE, mitochondrial translation pulse-labeling, RNA analysis, and ideally rescue with wild-type TACO1. These are specialist/research assays rather than routine clinical tests. (weraarpachai2012identificationandcharacterization pages 62-66, weraarpachai2012identificationandcharacterization pages 72-78)

Muscle biopsy in the original family showed generalized COX deficiency without ragged-red fibers and approximately 15% residual complex-IV activity, with other complexes normal. Fibroblasts retained approximately 29% activity. A normal muscle morphology or non-elevated lactate would not exclude disease. (weraarpachai2012identificationandcharacterization pages 147-151, weraarpachai2012identificationandcharacterization pages 66-72)

CMA, karyotyping, FISH, repeat-expansion testing, and isolated mtDNA sequencing are not first-line tests for this nuclear single-gene disorder. WGS may detect coding, splice, copy-number, and regulatory variants missed by panels/WES. RNA sequencing may clarify splice or expression effects, but no validated COXPD15 RNA-seq diagnostic signature exists.

**Differential diagnosis:** other nuclear complex-IV defects and Leigh-spectrum genes—including SURF1, SCO1, SCO2, COA genes, PET100, PET117, NDUFA4, and FASTKD5—as well as OPA1, SLC25A46, mitochondrial aminoacyl-tRNA-synthetase disorders, hereditary spastic ataxias, complicated hereditary spastic paraplegias, and inherited leukodystrophies. The combination of optic atrophy, spastic ataxia, cystic leukoencephalopathy, and isolated complex-IV deficiency should prioritize TACO1.

Population newborn screening is unavailable. Once a familial variant is known, cascade carrier testing, prenatal diagnosis, and preimplantation genetic testing are technically feasible.

## 11. Outcome and prognosis

The disorder is progressive and potentially severely disabling, but published TACO1 disease has generally progressed more slowly than classical infantile Leigh syndrome. Severe outcomes include loss of independent ambulation, legal blindness, dysphagia, weakness/amyotrophy, and extensive white-matter disease. Some patients remained ambulatory into their twenties, demonstrating substantial variable expressivity. (weraarpachai2012identificationandcharacterization pages 147-151, oktay2020confirmationoftaco1 pages 3-5)

No 5- or 10-year survival, median life expectancy, standardized disability outcome, mortality rate, or disease-specific quality-of-life score is available. Likewise, no validated prognostic biomarker exists. Earlier onset, severe complex-IV deficiency, rapid loss of mobility, bulbar dysfunction, extensive MRI progression, or cardiopulmonary involvement are clinically plausible adverse indicators, but none has been validated in a COXPD15 cohort.

## 12. Treatment

There is **no approved disease-modifying or TACO1-specific treatment**, and the trial search found no registered TACO1/COXPD15 interventional study. Published evidence does not support a disease-specific response rate for coenzyme Q10, riboflavin, thiamine, l-carnitine, arginine, ketogenic diet, antioxidants, or other “mitochondrial cocktails.” Their use would be individualized and extrapolated from broader mitochondrial practice rather than supported by COXPD15 trials.

Recommended management is multidisciplinary supportive care:

- Physical and occupational therapy, mobility aids, contracture prevention, orthoses, and fall prevention—NCIT concepts: **Physical Therapy**, **Occupational Therapy**, **Rehabilitation Therapy**.
- Speech-language therapy and augmentative communication; swallowing assessment and nutritional support, with gastrostomy if aspiration or inadequate intake becomes significant—NCIT: **Speech Therapy**, **Nutritional Support**, **Gastrostomy**.
- Ophthalmic low-vision services and educational accommodations—NCIT: **Supportive Care**.
- Management of spasticity or dystonia using individualized physiotherapy and medications such as baclofen or botulinum toxin when appropriate; monitor sedation and respiratory/swallowing effects.
- Surveillance and standard treatment for seizures, neuropathic pain, cardiomyopathy, arrhythmia, respiratory weakness, scoliosis, and aspiration if they occur.
- During illness: avoid prolonged fasting and dehydration; provide timely glucose-containing fluids when catabolic; monitor lactate, acid-base status, glucose, and organ function. Avoid clearly mitochondrially toxic medications where reasonable and review anesthetic plans with a mitochondrial specialist.

Wild-type TACO1 complementation restored patient-cell complex-IV function to 104% of control, furnishing a strong proof of principle for gene replacement. However, no viral-vector gene therapy, CRISPR therapy, mRNA therapy, ASO, cell therapy, or targeted small molecule has entered COXPD15 clinical testing. (weraarpachai2012identificationandcharacterization pages 62-66, weraarpachai2012identificationandcharacterizationa pages 62-66)

## 13. Prevention

Because the causal lesion is inherited, lifestyle modification cannot prevent disease in an individual with a pathogenic biallelic genotype.

- **Primary prevention:** genetic counseling, carrier testing of adult relatives, reproductive partner testing, preimplantation genetic testing, and prenatal diagnosis after familial variants are established.
- **Secondary prevention:** molecular diagnosis before irreversible visual, white-matter, or mobility loss; cascade testing of at-risk siblings; baseline ophthalmic, neurological, swallowing, cardiac, and hearing assessments.
- **Tertiary prevention:** vaccination according to standard schedules, rapid treatment of infection, avoidance of catabolism, aspiration precautions, mobility/contracture management, nutritional support, and surveillance for cardiopulmonary complications. The mouse infection study supports minimizing infectious stress but does not justify special antiviral prophylaxis in humans. (ferreira2020murinecytomegalovirusinfection pages 2-3, ferreira2020murinecytomegalovirusinfection pages 1-2)

There is no COXPD15 newborn-screening program, vaccine, chemoprophylaxis, or population public-health intervention.

## 14. Other species and natural disease

No naturally occurring veterinary TACO1 disease was identified in companion animals, livestock, or wildlife. Consequently, no breed-specific VBO annotation, veterinary prevalence, or zoonotic risk applies. COXPD15 is inherited and noncommunicable; there is no cross-species transmission.

TACO1 function is evolutionarily conserved sufficiently for mouse modeling, although the yeast ortholog **YGR021W** could be deleted without a comparable respiratory phenotype. This limits yeast fidelity and indicates mammal-specific or redundant translation biology. (weraarpachai2012identificationandcharacterization pages 78-84, weraarpachai2012identificationandcharacterizationa pages 62-66)

Suggested taxa are human **NCBI Taxon 9606**, laboratory mouse **10090**, and budding yeast **559292**.

## 15. Model organisms and experimental systems

### Patient-derived cellular model

Fibroblasts from the original patient reproduce absent TACO1, a roughly **65% reduction in COXI synthesis**, truncated COXI products, secondary loss of COXII/III, a small approximately 135-kDa assembly intermediate, and severe complex-IV deficiency. Wild-type cDNA rescue normalizes the biochemical defect, making these cells the most directly disease-relevant functional model. A limitation is that fibroblasts do not reproduce neuron-, optic-nerve-, muscle-, or white-matter-specific pathology. (weraarpachai2012identificationandcharacterization pages 62-66, weraarpachai2012identificationandcharacterization pages 151-155)

### Mouse model

The ENU-derived homozygous **Taco1 p.Ile164Asn (I164N)** mouse loses TACO1 protein and develops reduced COXI translation, approximately 50% lower complex-IV activity, reduced respiration, adult-onset visual impairment and retinal degeneration, motor dysfunction on hanging-wire/rotarod testing, mild Purkinje-cell shrinkage or loss, and cardiac hypertrophy. Molecular abnormalities are detectable from approximately four weeks, while overt symptoms emerge near 20 weeks; adult evaluations included 30-week-old mice. (richman2016lossofthe pages 11-12, richman2016lossofthe pages 1-2, richman2016lossofthe pages 11-11)

This model recapitulates late onset, visual and motor disease, and isolated complex-IV deficiency. Limitations include an engineered missense allele rather than the human frameshift-null genotypes, milder or different neuropathology, and cardiac involvement not yet established in patients.

The MCMV challenge model is useful for studying metabolic stress, immunity, mTOR signaling, and tissue-specific reserve. Infection selectively exacerbates heart COXI/complex-IV deficiency but not liver deficiency. (ferreira2020murinecytomegalovirusinfection pages 2-3, ferreira2020murinecytomegalovirusinfection pages 1-2)

No TACO1-specific zebrafish, Drosophila, C. elegans, rat, patient iPSC-derived neuron, retinal organoid, brain organoid, or humanized mouse model was identified. A 2024 review emphasizes that patient-derived iPSCs, differentiated neurons/cardiomyocytes, and organoids can support high-throughput and personalized studies in Leigh syndrome generally, but this application has not yet been reported specifically for COXPD15.

## Recent developments and evidence gaps, 2023–2024

The most notable disease-specific 2024 publication located was **“Distinct Magnetic Resonance Imaging in a Child With a TACO1 Variant”** in *JAMA Neurology* (published online September 2024; DOI: [10.1001/jamaneurol.2024.1105](https://doi.org/10.1001/jamaneurol.2024.1105)). Its full evidence text was unavailable to the retrieval system, so variant, phenotype, and imaging details should not be entered into a knowledge base without checking the article directly. The broader 2024 review **“Disease models of Leigh syndrome: From yeast to organoids”** was published in October 2024 (DOI: [10.1002/jimd.12804](https://doi.org/10.1002/jimd.12804)); it supports expanding disease modeling toward patient-derived specialized cells and organoids but does not provide a new TACO1-specific therapy.

No 2023–2024 TACO1 interventional trial, natural-history registry analysis, multi-omics cohort, or validated biomarker study was identified. Thus, the key current expert conclusion is that COXPD15 has unusually strong mechanistic evidence—segregation, selective biochemical failure, and cellular rescue—but exceptionally weak population, therapeutic, and longitudinal evidence.

## Key primary sources and exact abstract statements

1. **Weraarpachai et al., Nature Genetics, June 2009.** “Mutation in TACO1, encoding a translational activator of COX I, results in cytochrome c oxidase deficiency and late-onset Leigh syndrome.” DOI: [10.1038/ng.390](https://doi.org/10.1038/ng.390); PMID **19503089**. The patient-cell evidence shows a specific COXI translation defect and rescue by wild-type TACO1. (weraarpachai2012identificationandcharacterization pages 62-66, weraarpachai2012identificationandcharacterizationa pages 62-66)
2. **Oktay et al., Journal of Neuromuscular Diseases, June 2020.** The abstract states: “Clinical phenotype of the patients confirms the originally reported phenotype of a childhood-onset progressive cerebellar and pyramidal syndrome with optic atrophy and learning difficulties.” It also reports that MRI showed “periventricular white matter lesions with multiple cystic defects.” DOI: [10.3233/JND-200510](https://doi.org/10.3233/JND-200510). (oktay2020confirmationoftaco1 pages 3-5)
3. **Richman et al., Nature Communications, June 2016.** *Loss of the RNA-binding protein TACO1 causes late-onset mitochondrial dysfunction in mice.* DOI: [10.1038/ncomms11884](https://doi.org/10.1038/ncomms11884); PMID **27319982**. The model establishes TACO1 binding to mt-Co1 mRNA/ribosomal association and reproduces isolated complex-IV, visual, motor, and cardiac phenotypes. (richman2016lossofthe pages 11-12, richman2016lossofthe pages 1-2)
4. **Ferreira et al., PLOS Genetics, March 2020.** The abstract states that viral infection “exacerbates the complex IV deficiency in a tissue-specific manner” and that a common stress condition “can exacerbate mitochondrial dysfunction in a genetic model of mitochondrial disease.” DOI: [10.1371/journal.pgen.1008604](https://doi.org/10.1371/journal.pgen.1008604). (ferreira2020murinecytomegalovirusinfection pages 2-3, ferreira2020murinecytomegalovirusinfection pages 1-2)

## Knowledge-base confidence statement

**High confidence:** MONDO identity, TACO1 causality, autosomal-recessive inheritance, the two frameshift alleles, impaired MT-CO1 translation, isolated complex-IV deficiency, cellular rescue, and the broad spastic-ataxic/optic/leukoencephalopathy phenotype.  
**Moderate confidence:** full phenotypic spectrum, onset range, founder effect, and sex-associated severity because the number of families is very small.  
**Low or unavailable evidence:** population prevalence, penetrance, carrier frequency, survival, formal quality of life, environmental modifiers in humans, protective factors, epigenetics, multi-omics signatures, natural veterinary disease, and treatment efficacy.

References

1. (weraarpachai2012identificationandcharacterization pages 62-66): W Weraarpachai. Identification and characterization of novel genes involved in cytochrome c oxidase deficiencies. Unknown journal, 2012.

2. (weraarpachai2012identificationandcharacterization pages 66-72): W Weraarpachai. Identification and characterization of novel genes involved in cytochrome c oxidase deficiencies. Unknown journal, 2012.

3. (oktay2020confirmationoftaco1 pages 3-5): Yavuz Oktay, Serdal Güngör, Lena Zeltner, Sarah Wiethoff, Ludger Schöls, Ece Sonmezler, Elmasnur Yilmaz, Benjamin Munro, Benjamin Bender, Christoph Kernstock, Sofie Kaemereit, Inga Liepelt, Ana Töpf, Uluc Yis, Steven Laurie, Ahmet Yaramis, Stephan Zuchner, Semra Hiz, Hanns Lochmüller, Rebecca Schüle, and Rita Horvath. Confirmation of taco1 as a leigh syndrome disease gene in two additional families. Jun 2020. URL: https://doi.org/10.3233/jnd-200510, doi:10.3233/jnd-200510. This article has 29 citations and is from a peer-reviewed journal.

4. (OpenTargets Search: combined oxidative phosphorylation deficiency 15-MSTO1): Open Targets Query (combined oxidative phosphorylation deficiency 15-MSTO1, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (OpenTargets Search: combined oxidative phosphorylation defect type 15-TACO1): Open Targets Query (combined oxidative phosphorylation defect type 15-TACO1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (weraarpachai2012identificationandcharacterizationa pages 62-66): W Weraarpachai. Identification and characterization of novel genes involved in cytochrome c oxidase deficiencies. Unknown journal, 2012.

7. (weraarpachai2012identificationandcharacterizationa pages 147-151): W Weraarpachai. Identification and characterization of novel genes involved in cytochrome c oxidase deficiencies. Unknown journal, 2012.

8. (weraarpachai2012identificationandcharacterization pages 147-151): W Weraarpachai. Identification and characterization of novel genes involved in cytochrome c oxidase deficiencies. Unknown journal, 2012.

9. (weraarpachai2012identificationandcharacterizationa pages 66-72): W Weraarpachai. Identification and characterization of novel genes involved in cytochrome c oxidase deficiencies. Unknown journal, 2012.

10. (weraarpachai2012identificationandcharacterization pages 151-155): W Weraarpachai. Identification and characterization of novel genes involved in cytochrome c oxidase deficiencies. Unknown journal, 2012.

11. (richman2016lossofthe pages 1-2): Tara R. Richman, Henrik Spåhr, Judith A. Ermer, Stefan M. K. Davies, Helena M. Viola, Kristyn A. Bates, John Papadimitriou, Livia C. Hool, Jennifer Rodger, Nils-Göran Larsson, Oliver Rackham, and Aleksandra Filipovska. Loss of the rna-binding protein taco1 causes late-onset mitochondrial dysfunction in mice. Nature Communications, Jun 2016. URL: https://doi.org/10.1038/ncomms11884, doi:10.1038/ncomms11884. This article has 97 citations and is from a highest quality peer-reviewed journal.

12. (richman2016lossofthe pages 11-12): Tara R. Richman, Henrik Spåhr, Judith A. Ermer, Stefan M. K. Davies, Helena M. Viola, Kristyn A. Bates, John Papadimitriou, Livia C. Hool, Jennifer Rodger, Nils-Göran Larsson, Oliver Rackham, and Aleksandra Filipovska. Loss of the rna-binding protein taco1 causes late-onset mitochondrial dysfunction in mice. Nature Communications, Jun 2016. URL: https://doi.org/10.1038/ncomms11884, doi:10.1038/ncomms11884. This article has 97 citations and is from a highest quality peer-reviewed journal.

13. (richman2016lossofthe pages 11-11): Tara R. Richman, Henrik Spåhr, Judith A. Ermer, Stefan M. K. Davies, Helena M. Viola, Kristyn A. Bates, John Papadimitriou, Livia C. Hool, Jennifer Rodger, Nils-Göran Larsson, Oliver Rackham, and Aleksandra Filipovska. Loss of the rna-binding protein taco1 causes late-onset mitochondrial dysfunction in mice. Nature Communications, Jun 2016. URL: https://doi.org/10.1038/ncomms11884, doi:10.1038/ncomms11884. This article has 97 citations and is from a highest quality peer-reviewed journal.

14. (ferreira2020murinecytomegalovirusinfection pages 2-3): Nicola Ferreira, Christopher E. Andoniou, Kara L. Perks, Judith A. Ermer, Danielle L. Rudler, Giulia Rossetti, Ambika Periyakaruppiah, Jamie K. Y. Wong, Oliver Rackham, Peter G. Noakes, Mariapia A. Degli-Esposti, and Aleksandra Filipovska. Murine cytomegalovirus infection exacerbates complex iv deficiency in a model of mitochondrial disease. Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008604, doi:10.1371/journal.pgen.1008604. This article has 8 citations and is from a domain leading peer-reviewed journal.

15. (ferreira2020murinecytomegalovirusinfection pages 1-2): Nicola Ferreira, Christopher E. Andoniou, Kara L. Perks, Judith A. Ermer, Danielle L. Rudler, Giulia Rossetti, Ambika Periyakaruppiah, Jamie K. Y. Wong, Oliver Rackham, Peter G. Noakes, Mariapia A. Degli-Esposti, and Aleksandra Filipovska. Murine cytomegalovirus infection exacerbates complex iv deficiency in a model of mitochondrial disease. Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008604, doi:10.1371/journal.pgen.1008604. This article has 8 citations and is from a domain leading peer-reviewed journal.

16. (oktay2020confirmationoftaco1 pages 7-8): Yavuz Oktay, Serdal Güngör, Lena Zeltner, Sarah Wiethoff, Ludger Schöls, Ece Sonmezler, Elmasnur Yilmaz, Benjamin Munro, Benjamin Bender, Christoph Kernstock, Sofie Kaemereit, Inga Liepelt, Ana Töpf, Uluc Yis, Steven Laurie, Ahmet Yaramis, Stephan Zuchner, Semra Hiz, Hanns Lochmüller, Rebecca Schüle, and Rita Horvath. Confirmation of taco1 as a leigh syndrome disease gene in two additional families. Jun 2020. URL: https://doi.org/10.3233/jnd-200510, doi:10.3233/jnd-200510. This article has 29 citations and is from a peer-reviewed journal.

17. (weraarpachai2012identificationandcharacterization pages 72-78): W Weraarpachai. Identification and characterization of novel genes involved in cytochrome c oxidase deficiencies. Unknown journal, 2012.

18. (weraarpachai2012identificationandcharacterization pages 78-84): W Weraarpachai. Identification and characterization of novel genes involved in cytochrome c oxidase deficiencies. Unknown journal, 2012.

## Artifacts

- [Edison artifact artifact-00](Combined_Oxidative_Phosphorylation_Defect_Type_15-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 52 |
| Resolved | 51 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013987` (3 mentions) - the report calls it "if available"; MONDO calls it **combined oxidative phosphorylation defect type 15**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005751` (obsolete mitochondrial respiratory chain complex IV) (1 mention) - replaced by `GO:0045277`