---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T12:29:59.161902'
end_time: '2026-09-25T12:44:13.621258'
duration_seconds: 854.46
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Pyomyositis
  mondo_id: MONDO:0019168
  category: Infectious Disease
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 36
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 36
  on_topic: 24
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 16
  verified: 15
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 3
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0019168
    reported_labels:
    - MONDO
    ontology_label: pyomyositis
  - term_id: HP:0100279
    reported_labels:
    - Muscle swelling
    ontology_label: Ulcerative colitis
  labels_variant: 3
  obsolete_terms:
  - term_id: HP:0002355
    ontology_label: obsolete Difficulty walking
    replaced_by: HP:0001288
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Pyomyositis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pyomyositis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pyomyositis
- **MONDO ID:** MONDO:0019168 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Pyomyositis** covering all of the
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

# Pyomyositis (MONDO:0019168): A Comprehensive Disease Characterization

**Category:** Infectious Disease | **MONDO:** 0019168 | **ICD-10:** M60.0 | **ICD-11:** FB32.0 | **MeSH:** D011649

*Evidence base: 15 confirmed findings across 5 investigation iterations, drawn from 58 primary papers and reviews. All clinical/epidemiologic data are human (hospital-based case series, cohorts, systematic reviews, administrative datasets); mechanistic support includes murine in vivo models. Pyomyositis is **not a genetic disease**, so genetic/inheritance sections are largely* Not Applicable.

---

## Summary

**Pyomyositis is a primary pyogenic bacterial infection of striated skeletal muscle, most often caused by *Staphylococcus aureus*, that produces an intramuscular abscess in a large muscle group—classically the thigh, iliopsoas, obturator, or gluteal muscles.** It is fundamentally an *acquired infectious disease*, not a genetic or heritable disorder; there are no causal human genes, and host susceptibility is instead governed by acquired immunocompromising states. The disease was historically termed "tropical pyomyositis" because of its high incidence in tropical climates, but it is increasingly recognized in temperate, high-income countries where its incidence has more than tripled in recent decades, largely because of its association with immunodeficiency states such as HIV/AIDS, diabetes mellitus, malignancy, and organ transplantation.

The pathophysiology is best understood as a two-hit process: transient or occult *S. aureus* bacteremia seeds skeletal muscle that has been rendered locally vulnerable by antecedent trauma or vigorous exercise. Normal skeletal muscle is intrinsically resistant to hematogenous infection, so muscle injury—reported in roughly one-third of patients—is thought to be a necessary permissive lesion, a mechanism directly supported by a murine "Trojan Horse" model in which intravenous MRSA alone produced no muscle infection unless muscle injury and ischemia were also present. Once seeded, the infection evolves through the classic three-stage Chiedozi progression: an invasive stage (diffuse inflammation, antibiotic-responsive), a suppurative stage (abscess formation, requiring drainage—the stage at which most patients present), and a late septic stage (bacteremia, metastatic abscesses, septic shock).

Diagnosis rests on MRI, which is essentially 100% sensitive and is the modality of choice for defining site, extent, and multifocality; ultrasound and blood cultures are less reliable (culture-negative disease is common). Treatment is stage-dependent: anti-staphylococcal antibiotics alone cure early disease, while drainage plus antibiotics is required once an abscess forms. Prognosis is excellent with timely intervention—most patients recover full function—but reported mortality ranges from 1% to 23%, driven by diagnostic delay, sepsis, hypoalbuminemia, inappropriate initial antibiotics, and advanced disease at presentation. Because the disease is non-heritable and no *S. aureus* vaccine exists, prevention relies on control of predisposing conditions, *S. aureus* decolonization, and early detection.

---

## Section 1 — Disease Information

Pyomyositis (PM) is formally defined as *"a primary pyogenic infection of the striated skeletal muscle"* ([PMID: 29274860](https://pubmed.ncbi.nlm.nih.gov/29274860/)). It is characterized by intramuscular abscess formation arising from hematogenous spread of bacteria to muscle. It is described as *"a common masquerading disease that is frequently misdiagnosed"* ([PMID: 27090546](https://pubmed.ncbi.nlm.nih.gov/27090546/)) because its early clinical features are non-specific and overlap with many soft-tissue conditions.

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0019168 |
| ICD-10 | M60.0 (Infective myositis) |
| ICD-11 | FB32.0 |
| MeSH | D011649 (Pyomyositis) |
| SNOMED CT | 359693002 |
| OMIM | None (non-genetic disease) |

**Synonyms / alternative names:** tropical pyomyositis, tropical myositis, myositis tropicans, pyogenic myositis, primary bacterial pyomyositis, purulent infectious myositis, and Lambo abscess.

**Information source type:** The evidence base is a mixture of *aggregated disease-level resources* (systematic reviews, meta-analyses, population databases such as the US National Inpatient Sample) and *individual-patient sources* (hospital-based case series, cohort studies, and case reports). There is no single genetic or EHR-derived registry; the knowledge base is predominantly clinical-observational.

---

## Section 2 — Etiology

**Primary cause:** Pyomyositis is an **infectious disease**. The dominant causal factor is bacterial infection of skeletal muscle, overwhelmingly by *Staphylococcus aureus* (see Section 5). It is *not* genetic, and there are no Mendelian causal factors.

**Risk factors (environmental / host):** The disease is strongly associated with acquired immunocompromise. A systematic review and meta-analysis found pyomyositis significantly associated with **HIV infection (OR = 4.82; 95% CI 1.67–13.92)** and with fulfilling an **AIDS surveillance definition (OR = 6.08; 95% CI 2.79–13.23)** ([PMID: 34407271](https://pubmed.ncbi.nlm.nih.gov/34407271/)). A US population-based study reported *"significant association of pyomyositis with HIV, types 1 and 2 diabetes mellitus, hematologic malignancy, organ transplant, malnutrition, chronic kidney disease, obesity, and rheumatoid arthritis"* ([PMID: 32147332](https://pubmed.ncbi.nlm.nih.gov/32147332/)). In tropical series, *"a concurrent state of immunodeficiency is observed in up to 75% of tropical PM cases"* ([PMID: 27090546](https://pubmed.ncbi.nlm.nih.gov/27090546/)). Additional environmental/behavioral risk factors include **minor trauma, vigorous physical activity, and injection drug use**; male sex and young age are strong demographic risk factors (Section 3).

**Genetic risk factors (host):** None identified. There are no known susceptibility loci, causal variants, or modifier genes in humans. This section is *Not Applicable* at the host level.

**Protective factors:** No genetic protective factors are known. Environmental/host protective factors are the inverse of the risk factors—**immune competence, glycemic control, antiretroviral therapy with immune reconstitution, good nutrition, skin hygiene, and avoidance of muscle trauma**.

**Gene–environment interactions (pathogen side):** The relevant "genetic" element is *bacterial* virulence. *S. aureus* strains carrying **Panton-Valentine leukocidin (PVL; genes *lukS-PV*/*lukF-PV*)** interact with the host to produce more severe disease: *"Staphylococcus aureus strains carrying the genes encoding Panton-Valentine leukocidin (pvl-positive) are associated with more febrile days and higher complication rates"* ([PMID: 16452363](https://pubmed.ncbi.nlm.nih.gov/16452363/)). Thus the disease outcome is shaped by an interaction between pathogen genotype and host immune/tissue status rather than host germline variation.

---

## Section 3 — Phenotypes

The clinical phenotype is a triad of **fever, localized muscle pain/swelling, and functional impairment**. A pediatric systematic review found *"Fever, painful limp, and localized pain were the most common presenting symptoms"* ([PMID: 34411048](https://pubmed.ncbi.nlm.nih.gov/34411048/)). In adults, myalgia and fever dominate: *"Common presenting symptoms were myalgias [50 (74.62%)] and fever [49 (73.13%)]"* ([PMID: 19763666](https://pubmed.ncbi.nlm.nih.gov/19763666/)).

| Phenotype | Type | Frequency | HPO term (suggested) |
|-----------|------|-----------|----------------------|
| Fever | Symptom | ~65–73% | HP:0001945 (Fever) |
| Muscle pain / myalgia | Symptom | ~75–100% | HP:0003326 (Myalgia) |
| Muscle swelling / mass | Clinical sign | Common | HP:0100279 (Muscle swelling) |
| Painful limp / impaired mobility | Sign | Common (pediatric) | HP:0002355 (Difficulty walking) |
| Functional impairment | Sign | ~83% | HP:0002355 |
| Woody induration | Sign | Invasive stage | — |
| Leukocytosis / neutrophilia | Lab abnormality | Characteristic | HP:0001974 (Leukocytosis) |
| Elevated CRP / ESR | Lab abnormality | Characteristic | HP:0011227 (Elevated CRP) |
| Elevated creatine kinase | Lab abnormality | Often normal/mild in bacterial PM; markedly elevated in aseptic forms | HP:0003236 (Elevated serum creatine kinase) |

**Phenotype characteristics:**
- **Age of onset:** Bimodal in reports—young adults (mean 29.9 ± 14.8 yr in a North India cohort) and children (mean age ~8 yr in pediatric series). Predominantly a disease of children and young adults.
- **Severity:** Variable—from indolent localized muscle pain to fulminant septic shock.
- **Progression:** Subacute and progressive through three stages if untreated (Section 8); self-limited once appropriately treated.
- **Time to diagnosis:** Mean ~6.6 ± 3.05 days ([PMID: 34411048](https://pubmed.ncbi.nlm.nih.gov/34411048/)).

**Quality of life:** Acute functional impairment (inability to walk/use the affected limb) is common (~83% in one pediatric series), but with timely treatment full functional recovery is the norm—*"All patients improved without functional impairment at 6-month follow-up"* ([PMID: 40440680](https://pubmed.ncbi.nlm.nih.gov/40440680/)). In aseptic/autoinflammatory pyomyositis (e.g., Behçet disease), presentations can include a palpable muscle mass, severe myalgia, and ~13-fold elevated creatine kinase ([PMID: 41371187](https://pubmed.ncbi.nlm.nih.gov/41371187/)).

---

## Section 4 — Genetic / Molecular Information

**This section is largely Not Applicable at the host level.** Pyomyositis is an acquired bacterial infection, not a Mendelian/heritable disorder. There are **no causal human genes, no pathogenic germline variants, no chromosomal abnormalities, no inheritance pattern, no penetrance/expressivity, no founder effects, and no carrier frequencies** ([PMID: 34407271](https://pubmed.ncbi.nlm.nih.gov/34407271/); [PMID: 32147332](https://pubmed.ncbi.nlm.nih.gov/32147332/)). Genetic testing is not indicated for diagnosis; microbiological culture and MRI are used instead.

**The relevant molecular determinants are bacterial virulence genes:**
- ***lukS-PV / lukF-PV*** encode Panton-Valentine leukocidin, a bicomponent pore-forming leukotoxin. PVL-positive strains cause more severe, complicated musculoskeletal disease: *"Staphylococcus aureus strains carrying the genes encoding Panton-Valentine leukocidin (pvl-positive) are associated with more febrile days and higher complication rates"* ([PMID: 16452363](https://pubmed.ncbi.nlm.nih.gov/16452363/)). Severe/life-threatening PVL-SA infections including pyomyositis are documented in children ([PMID: 31567961](https://pubmed.ncbi.nlm.nih.gov/31567961/); [PMID: 33629932](https://pubmed.ncbi.nlm.nih.gov/33629932/)).
- **MRSA (methicillin resistance, *mecA*)** strains are increasingly reported, particularly in India, and complicate empiric therapy.

**Epigenetics:** Not applicable to host pathogenesis.

---

## Section 5 — Environmental / Microbiological Information

**Infectious agents (the core etiology):**

| Pathogen | Context | Evidence |
|----------|---------|----------|
| ***Staphylococcus aureus*** (MSSA & MRSA) | Predominant cause in all settings | [PMID: 34407271](https://pubmed.ncbi.nlm.nih.gov/34407271/); [PMID: 39971676](https://pubmed.ncbi.nlm.nih.gov/39971676/) |
| *Streptococcus pyogenes* (Group A) & other streptococci | Second most common bacterial cause | [PMID: 42768398](https://pubmed.ncbi.nlm.nih.gov/42768398/) |
| *Streptococcus pneumoniae* | Rare bacterial cause | [PMID: 23031303](https://pubmed.ncbi.nlm.nih.gov/23031303/) |
| Gram-negatives (*Pseudomonas*, *Klebsiella*, *E. coli*) | Immunocompromised hosts | [PMID: 39971676](https://pubmed.ncbi.nlm.nih.gov/39971676/); [PMID: 27090546](https://pubmed.ncbi.nlm.nih.gov/27090546/) |
| *Mycobacterium tuberculosis* | Tuberculous pyomyositis | [PMID: 41626125](https://pubmed.ncbi.nlm.nih.gov/41626125/) |
| *Burkholderia pseudomallei* | Melioidosis, endemic SE Asia/N Australia | [PMID: 22081283](https://pubmed.ncbi.nlm.nih.gov/22081283/) |
| Fungi, non-tuberculous mycobacteria, *Nocardia* | Opportunistic, immunocompromised | [PMID: 39971676](https://pubmed.ncbi.nlm.nih.gov/39971676/) |

*S. aureus* dominance is repeatedly confirmed: *"Tropical pyomyositis is a serious infectious disease characterised by the formation of abscesses in the skeletal muscles and is primarily caused by Staphylococcus aureus"* ([PMID: 39971676](https://pubmed.ncbi.nlm.nih.gov/39971676/)) and *"Staphylococcus aureus was the main organism isolated"* ([PMID: 34407271](https://pubmed.ncbi.nlm.nih.gov/34407271/)). In a Portuguese pediatric series, MSSA accounted for 36.0% of isolates. In the immunocompromised, the microbiology shifts: *"Immunocompromised hosts are more likely to be affected by Gram-negative organisms, Mycobacterium tuberculosis, opportunistic infections such as fungal pathogens, non-tuberculous mycobacteria, and Nocardia species"* ([PMID: 39971676](https://pubmed.ncbi.nlm.nih.gov/39971676/)).

**Environmental / lifestyle factors:** Tropical climate, minor trauma, vigorous exercise, injection drug use (e.g., oesophageal pyomyositis in an IVDU, [PMID: 25125141](https://pubmed.ncbi.nlm.nih.gov/25125141/)), and immunosuppressive states. **Non-infectious (aseptic) pyomyositis** is rare and occurs in autoinflammatory conditions such as Behçet disease ([PMID: 41371187](https://pubmed.ncbi.nlm.nih.gov/41371187/)).

**CHEBI-relevant entities:** the causative organism's PVL toxin (protein), and therapeutic antibiotics (see Section 12).

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Transient / occult bacteremia** — *S. aureus* enters the bloodstream (from skin, mucosa, or minor breach). *Leads to* circulating bacteria that transit through muscle capillaries.
2. **Antecedent muscle injury** — trauma or vigorous exercise (reported in ~31–38% of cases; [PMID: 40440680](https://pubmed.ncbi.nlm.nih.gov/40440680/)) produces a *locus minoris resistentiae* with local ischemia and hematoma. *Results in* a microenvironment that impairs bacterial clearance. **(This step is causally required — see the "Trojan Horse" experiment below.)**
3. **Muscle seeding and proliferation (invasive stage)** — bacteria colonize the damaged muscle and multiply over ~1–2 weeks. *Leads to* diffuse muscle inflammation without discrete abscess.
4. **Neutrophil-mediated suppuration + toxin production (suppurative stage)** — neutrophil influx, tissue necrosis, and PVL-mediated leukocyte lysis. *Results in* an intramuscular abscess (weeks 2–3).
5. **Branch — local extension:** abscess extends to adjacent bone (osteomyelitis), joint (septic arthritis), or fascia.
6. **Branch — hematogenous dissemination (late/septic stage):** *leads to* bacteremia, metastatic abscesses, septic emboli, endocarditis/pancarditis, septic shock, and multi-organ dysfunction (AKI, DVT, compartment syndrome).

### Detailed mechanism

**Why muscle is normally spared, and why injury matters.** Skeletal muscle is intrinsically resistant to hematogenous bacterial seeding. The pivotal experimental demonstration is a murine "Trojan Horse" model in which *"No SSIs were observed in mice injected intravenously with MRSA"* unless muscle injury and ischemia were also induced (*"mice were subjected to a surgical injury (30% hepatectomy) and rectus muscle injury and ischemia before skin closure"*) ([PMID: 28187042](https://pubmed.ncbi.nlm.nih.gov/28187042/)). This shows bacteremia alone is insufficient; a second hit of muscle injury is required for seeding—mechanistically, circulating neutrophils carry bacteria into the injured, ischemic muscle. This directly explains the clinical epidemiology: *"The disease primarily affects men and young adults, often following minor trauma"* ([PMID: 39971676](https://pubmed.ncbi.nlm.nih.gov/39971676/)).

**Immune / cellular processes.** Pyomyositis is a **neutrophil-driven (pyogenic) infection** (GO:0006954 inflammatory response; GO:0006935 chemotaxis). Impaired cell-mediated and neutrophil immunity—from HIV/AIDS, chemotherapy-induced neutropenia, hematologic malignancy, or diabetes—predisposes to disease. A striking clinical illustration is pyomyositis emerging during the chemotherapy "nadir" of transient neutropenia ([PMID: 38090454](https://pubmed.ncbi.nlm.nih.gov/38090454/)).

**Toxin-mediated tissue damage.** PVL is a pore-forming leukotoxin that lyses neutrophils, causing tissue necrosis and severe/metastatic disease. PVL genes are *"associated with enhanced inflammatory response and local disease in acute hematogenous Staphylococcus aureus osteomyelitis in children"* ([PMID: 16452363](https://pubmed.ncbi.nlm.nih.gov/16452363/)), and PVL-positive strains drive more complications requiring surgery and longer hospitalization ([PMID: 31567961](https://pubmed.ncbi.nlm.nih.gov/31567961/); [PMID: 33629932](https://pubmed.ncbi.nlm.nih.gov/33629932/)).

**Upstream vs downstream.** *Upstream:* bacteremia + muscle injury/ischemia + host immunocompromise. *Midstream:* bacterial proliferation, neutrophil recruitment, toxin release. *Downstream:* abscess formation, local extension, hematogenous dissemination, sepsis.

**Cell types / tissues (suggested ontology terms):** skeletal muscle cell / myofiber (CL:0000188), neutrophil (CL:0000775), macrophage (CL:0000235); skeletal muscle tissue (UBERON:0001134).

---

## Section 7 — Anatomical Structures Affected

**Primary tissue:** skeletal (striated) muscle — **UBERON:0001134**. Usually a single large muscle group is involved, but disease is **multifocal in ~12–40%** of cases.

**Distribution (muscle groups):** The pelvis and lower limb predominate. A pediatric systematic review reported: *"Pelvis, lower extremity, trunk and spine, in descending order, were the most commonly affected locations. Iliopsoas, obturator musculature, and gluteus musculature were the most commonly affected muscle groups"* ([PMID: 34411048](https://pubmed.ncbi.nlm.nih.gov/34411048/)). In adults, the thigh predominates: *"Most common site of involvement was thigh muscles (n = 29, 46.8%)"* ([PMID: 29338140](https://pubmed.ncbi.nlm.nih.gov/29338140/)); in the Sharma cohort the iliopsoas was most common (46.26%).

| Site | Frequency | Notes |
|------|-----------|-------|
| Thigh / quadriceps | ~40–47% (adults) | Most common overall in adults |
| Iliopsoas | Up to ~46% | Common in both children & adults |
| Obturator (externus/internus) | Common (pediatric) | [PMID: 28248876](https://pubmed.ncbi.nlm.nih.gov/28248876/) |
| Gluteal | Common | — |
| Piriformis, psoas, paravertebral | Reported | [PMID: 34540162](https://pubmed.ncbi.nlm.nih.gov/34540162/) |
| Scapular / core / deep-core muscles | Rare | [PMID: 37767417](https://pubmed.ncbi.nlm.nih.gov/37767417/); [PMID: 41981521](https://pubmed.ncbi.nlm.nih.gov/41981521/) |
| Oesophageal muscle | Very rare | [PMID: 25125141](https://pubmed.ncbi.nlm.nih.gov/25125141/) |

**Lateralization:** typically **unilateral**.

**Secondary / complication sites (body systems):** bone (osteomyelitis), joints (septic arthritis, facet joint — [PMID: 38449920](https://pubmed.ncbi.nlm.nih.gov/38449920/)), heart (endocarditis/pancarditis — [PMID: 22538039](https://pubmed.ncbi.nlm.nih.gov/22538039/)), lungs (septic emboli/necrotizing pneumonia — [PMID: 32623976](https://pubmed.ncbi.nlm.nih.gov/32623976/)), kidney (AKI), and veins (DVT). Body systems: musculoskeletal (primary), cardiovascular, respiratory, renal.

**Subcellular:** not a primary feature; relevant GO cellular components pertain to the pathogen (bacterial cell wall/membrane) rather than a host organelle defect.

---

## Section 8 — Temporal Development

**Onset:** subacute; typically over days to ~2 weeks. Mean time to diagnosis ~6.6 days ([PMID: 34411048](https://pubmed.ncbi.nlm.nih.gov/34411048/)). Age of onset predominantly children and young adults.

**The classic three-stage (Chiedozi) progression:**

| Stage | Timing | Features | Management |
|-------|--------|----------|-----------|
| **1 — Invasive** | ~first 1–2 weeks | Diffuse muscle inflammation, no abscess; crampy pain, low-grade fever, woody induration | **Antibiotics alone** |
| **2 — Suppurative / purulent** | Weeks 2–3 | Abscess, high fever, exquisite tenderness, fluctuance | **Drainage + antibiotics** |
| **3 — Late / septic** | >3 weeks if untreated | Systemic toxicity, bacteremia, metastatic abscesses, septic shock, organ dysfunction | **Aggressive drainage, IV antibiotics, ICU support** |

Most patients present in stage 2: *"Forty-nine patients (79%) presented in the suppurative stage of illness"* ([PMID: 29338140](https://pubmed.ncbi.nlm.nih.gov/29338140/)), reflecting diagnostic delay. Stage determines treatment: *"The appropriate antibiotic therapy provides a rapid regression of symptoms during the early stage of pyomyositis. In cases of MRI-confirmed abscess, surgical treatment is indicated"* ([PMID: 28248876](https://pubmed.ncbi.nlm.nih.gov/28248876/)). Early-stage pediatric cases can show *"marked improvement within 3 days"* on antibiotics alone ([PMID: 29274860](https://pubmed.ncbi.nlm.nih.gov/29274860/)).

**Course & duration:** acute/subacute and **self-limited once appropriately treated**; it is **not** chronic or relapsing-remitting. Remission is treatment-induced. The critical intervention window is the invasive stage, when antibiotics alone can achieve cure before abscess formation.

---

## Section 9 — Inheritance and Population (Epidemiology)

**Inheritance:** *Not Applicable* — non-genetic, non-heritable infectious disease. No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity role, or carrier frequency.

**Epidemiology / demographics:**
- **Sex & age:** strong male, young predominance — *"Males under the age of 20 predominated, and mortality of up to 20% was reported"* ([PMID: 34407271](https://pubmed.ncbi.nlm.nih.gov/34407271/)). North India cohort: mean age 29.9 ± 14.8 yr, 54/62 male ([PMID: 29338140](https://pubmed.ncbi.nlm.nih.gov/29338140/)). Portuguese pediatric series: 75.9% male, median age 8 yr.
- **Geographic distribution:** historically tropical ("tropical pyomyositis"), now increasingly temperate. A US population study found *"a concerning more than three-fold increase in the incident pyomyositis admissions over our study period"* (2002–2014), with affected patients younger, more likely male and Black, and more cases in the West and South ([PMID: 32147332](https://pubmed.ncbi.nlm.nih.gov/32147332/)).
- **Prevalence/incidence:** precise population rates are not well established; it remains uncommon but rising in temperate high-income settings, and is far more common in the tropics.

---

## Section 10 — Diagnostics

**Imaging (cornerstone):** MRI is the modality of choice — *"Magnetic resonance imaging had 100% sensitivity, whereas 40.7% of ultrasounds were inconclusive"* ([PMID: 40440680](https://pubmed.ncbi.nlm.nih.gov/40440680/)) and *"Magnetic resonance imaging (MRI) is the modality of choice for defining the site and extent of disease, detecting multiple foci, and guiding surgical planning"* ([PMID: 41127115](https://pubmed.ncbi.nlm.nih.gov/41127115/)). Point-of-care ultrasound can differentiate pyomyositis from cellulitis and *"led to an earlier diagnosis of PM and directly affected the immediate patient care"* ([PMID: 25245285](https://pubmed.ncbi.nlm.nih.gov/25245285/)). CT is useful for deep-core muscle disease.

**Laboratory / microbiology:** Elevated inflammatory markers (WBC, ESR, CRP) are characteristic; **creatine kinase is often normal or only mildly elevated** in bacterial pyomyositis (a useful discriminator from primary myopathies/aseptic myositis, where CK can be markedly elevated). **Cultures:** blood cultures positive in ~40%, pus cultures in ~33%; **culture-negative disease is common**. Definitive microbiology comes from aspirated/drained pus.

**Histopathology / biopsy:** confirms suppurative myositis; in aseptic forms reveals *"granulocytic-necrotizing infiltrates and fibrinoid vascular necrosis"* ([PMID: 41371187](https://pubmed.ncbi.nlm.nih.gov/41371187/)).

**Genetic / omics testing:** *Not indicated* (non-genetic disease). Molecular microbiology (e.g., CBNAAT/line-probe assay for tuberculous pyomyositis, [PMID: 41626125](https://pubmed.ncbi.nlm.nih.gov/41626125/)) may be used to identify atypical pathogens.

**Differential diagnosis:** cellulitis, deep vein thrombosis (notably mimicked in SLE — *"Pyomyositis may mimic deep vein thrombosis and be misdiagnosed"* [PMID: 35260400](https://pubmed.ncbi.nlm.nih.gov/35260400/)), necrotizing fasciitis, septic arthritis, osteomyelitis, muscle contusion/hematoma/strain, soft-tissue sarcoma, thrombophlebitis, and other infective myositides (streptococcal necrotizing myositis, tuberculous/melioidosis myositis). Imaging is central to distinguishing these entities.

---

## Section 11 — Outcome / Prognosis

**Overall:** Prognosis is **good with timely diagnosis and treatment**; most patients achieve full functional recovery (*"All patients improved without functional impairment at 6-month follow-up"* — [PMID: 40440680](https://pubmed.ncbi.nlm.nih.gov/40440680/)). However, **reported mortality ranges 1–23%**, driven largely by delay and sepsis.

**Predictors of mortality:** In a North India cohort of 67 patients, *"Twenty-eight patients developed sepsis and seven died"* (~10% mortality), with *"a statistically significant association between higher SOFA score, lower Glasgow coma scale, higher pulse rate, lower blood pressure, raised blood urea, raised serum creatinine"* ([PMID: 19763666](https://pubmed.ncbi.nlm.nih.gov/19763666/)). An independent cohort found *"Lower first-day serum albumin, initial inappropriate antibiotic therapy and advanced form of the disease at presentation were associated with increased in-hospital mortality"* ([PMID: 29338140](https://pubmed.ncbi.nlm.nih.gov/29338140/)).

**Complications:** sepsis/septic shock, metastatic abscesses, septic emboli/necrotizing pneumonia, osteomyelitis, septic arthritis, endocarditis/pancarditis, acute kidney injury, DVT, and compartment syndrome.

| Prognostic factor | Direction | Source |
|-------------------|-----------|--------|
| High SOFA score | Worse | [PMID: 19763666](https://pubmed.ncbi.nlm.nih.gov/19763666/) |
| Low GCS, hypotension, tachycardia | Worse | [PMID: 19763666](https://pubmed.ncbi.nlm.nih.gov/19763666/) |
| Raised urea/creatinine (AKI) | Worse | [PMID: 19763666](https://pubmed.ncbi.nlm.nih.gov/19763666/) |
| Low first-day serum albumin | Worse | [PMID: 29338140](https://pubmed.ncbi.nlm.nih.gov/29338140/) |
| Inappropriate initial antibiotics | Worse | [PMID: 29338140](https://pubmed.ncbi.nlm.nih.gov/29338140/) |
| Advanced stage at presentation | Worse | [PMID: 29338140](https://pubmed.ncbi.nlm.nih.gov/29338140/) |
| Early diagnosis/treatment | Better | [PMID: 40440680](https://pubmed.ncbi.nlm.nih.gov/40440680/) |

---

## Section 12 — Treatment

**Principle:** stage-dependent combination of **anti-staphylococcal antibiotics + source control (drainage)**.

**Pharmacotherapy (NCIT: Antibiotic Therapy):**
- Empiric anti-staphylococcal agents: flucloxacillin (MSSA), vancomycin (MRSA), with **clindamycin or linezolid added as anti-toxin agents** for PVL-producing strains (these suppress bacterial protein/toxin synthesis).
- Portuguese series: IV flucloxacillin + clindamycin in 55.2%, median 14 days IV and 29 days total ([PMID: 40440680](https://pubmed.ncbi.nlm.nih.gov/40440680/)).
- Pediatric systematic review: mean 9.5 ± 4.0 days IV and 22.7 ± 7.2 days oral antibiotics ([PMID: 34411048](https://pubmed.ncbi.nlm.nih.gov/34411048/)).

**Surgical / interventional (NCIT: Incision and Drainage):** Drainage is required once an abscess forms. In the pediatric review, *"Medical management alone was successful in 40% of cases (143/361)"*, with the remainder requiring drainage (open 91.3%, percutaneous 8.7%) ([PMID: 34411048](https://pubmed.ncbi.nlm.nih.gov/34411048/)). Predictors of surgical need: *"Painful limp, fever, and larger values of white cell count and erythrocyte sedimentation rate were associated with an increased need for surgery"* ([PMID: 34411048](https://pubmed.ncbi.nlm.nih.gov/34411048/)).

**Supportive care:** analgesia, fluid/hemodynamic support, ICU care for septic stage, treatment of underlying immunocompromise.

**Treatment strategy / algorithm:**
```
Suspected pyomyositis → MRI
   ├─ Invasive stage (no abscess) → IV anti-staph antibiotics → step down to oral
   └─ Suppurative/abscess → Drainage (image-guided or open) + antibiotics
                              └─ PVL/severe → add anti-toxin agent (clindamycin/linezolid)
   Septic stage → aggressive drainage + broad IV antibiotics + ICU support
```

**Pharmacogenomics / advanced therapeutics (gene/cell/RNA therapy, immunotherapy):** *Not applicable* — this is a treatable bacterial infection.

**Outcomes:** With combined therapy, functional recovery is excellent (see Section 11).

---

## Section 13 — Prevention

**No vaccine exists** for pyomyositis or for *S. aureus* (multiple *S. aureus* vaccine candidates have failed in trials). Prevention is largely secondary/tertiary.

- **Primary prevention:** control predisposing conditions (glycemic control, antiretroviral therapy/immune reconstitution in HIV, nutrition), skin hygiene, prompt wound care, avoidance of muscle trauma and injection drug use. ***S. aureus* decolonization** is the principal targeted strategy: *"S aureus colonization is a significant risk factor for subsequent infection; thus, surveillance and decolonization with topical antimicrobials and antiseptics remain the mainstay of prevention"* ([PMID: 42624765](https://pubmed.ncbi.nlm.nih.gov/42624765/)). Decolonization uses intranasal mupirocin and chlorhexidine bathing, though effectiveness wanes and drives resistance ([PMID: 41276461](https://pubmed.ncbi.nlm.nih.gov/41276461/)).
- **Secondary prevention:** early recognition and imaging (MRI/point-of-care ultrasound) to catch the invasive stage before abscess forms, enabling cure with antibiotics alone ([PMID: 25245285](https://pubmed.ncbi.nlm.nih.gov/25245285/)).
- **Tertiary prevention:** adequate drainage and appropriate antibiotics to prevent sepsis, metastatic abscesses, osteomyelitis, and contractures.
- **Genetic/newborn screening:** *Not applicable* (non-heritable).

---

## Section 14 — Other Species / Natural Disease

- **Model host species:** *Mus musculus* (**NCBITaxon:10090**) is the principal experimental host (Section 15).
- **Causative pathogen taxonomy:** *Staphylococcus aureus* (**NCBITaxon:1280**).
- **Natural disease in other species:** Pyomyositis as a distinct clinical entity is chiefly described in humans; *S. aureus* muscle/soft-tissue abscesses occur across mammals but a dedicated veterinary "pyomyositis" literature is limited. **No heritable animal ortholog exists** because the disease is infectious, not genetic.
- **Zoonotic potential:** *S. aureus* (including MRSA) can transmit between humans and animals, but pyomyositis itself is not classically a zoonosis.
- **Comparative biology:** The murine muscle-injury model recapitulates the trauma-dependent seeding mechanism, indicating conservation of the host-tissue vulnerability principle ([PMID: 28187042](https://pubmed.ncbi.nlm.nih.gov/28187042/)).

---

## Section 15 — Model Organisms

There is **no dedicated genetic "pyomyositis" model**, because the disease is infectious and non-heritable. The relevant systems are **induced infection models**:

| Model | Description | Use | Evidence |
|-------|-------------|-----|----------|
| **Murine thigh-muscle *S. aureus* infection** (often neutropenic) | MRSA/MSSA inoculated into mouse thigh, frequently in cyclophosphamide-induced neutropenic mice | Antibiotic PK/PD and efficacy studies | [PMID: 26514291](https://pubmed.ncbi.nlm.nih.gov/26514291/); [PMID: 41672145](https://pubmed.ncbi.nlm.nih.gov/41672145/); [PMID: 41778916](https://pubmed.ncbi.nlm.nih.gov/41778916/); [PMID: 38936579](https://pubmed.ncbi.nlm.nih.gov/38936579/) |
| **"Trojan Horse" muscle-injury model** | 30% hepatectomy + rectus muscle injury/ischemia + IV MRSA | Mechanistic proof that muscle injury is required for seeding | [PMID: 28187042](https://pubmed.ncbi.nlm.nih.gov/28187042/) |

- **Phenotype recapitulation:** The Trojan Horse model reproduces trauma-dependent muscle abscess formation (*"mice were subjected to a surgical injury (30% hepatectomy) and rectus muscle injury and ischemia before skin closure"*, [PMID: 28187042](https://pubmed.ncbi.nlm.nih.gov/28187042/)); the neutropenic thigh model (*"mice with a Staphylococcus aureus infection in the thigh muscle"*, [PMID: 26514291](https://pubmed.ncbi.nlm.nih.gov/26514291/)) mirrors the human predisposition of immunocompromise.
- **Limitations:** These models emphasize bacterial burden and drug response rather than the full three-stage natural history and chronic abscess of human disease, and they do not model host comorbidities such as HIV.
- **Resources:** MGI (mouse); standard laboratory *S. aureus* strains (e.g., Newman, MRSA clinical isolates).

---

## Mechanistic Model / Interpretation

The disease is best captured by a **two-hit "seed-and-soil" model**:

```
   HIT 1: Transient S. aureus bacteremia        HIT 2: Muscle injury / ischemia
   (from skin, mucosa, minor breach)            (trauma, vigorous exercise)
                 |                                          |
                 +---------------+--------------------------+
                                 v
         Neutrophils carry bacteria into injured, ischemic muscle
         (impaired local clearance = permissive "soil")
                                 |
                                 v   [modulated by host immunocompromise: HIV, DM, neutropenia]
              STAGE 1 (Invasive): diffuse myositis, no abscess  --> antibiotics cure
                                 |
                                 v   [amplified by PVL toxin -> neutrophil lysis, necrosis]
              STAGE 2 (Suppurative): intramuscular ABSCESS      --> drainage + antibiotics
                                 |
             +-------------------+------------------------+
             v                                            v
   Local extension:                            STAGE 3 (Septic):
   osteomyelitis, septic arthritis             bacteremia, metastatic abscesses,
                                               septic emboli, endocarditis, shock
```

The single most important mechanistic insight—experimentally validated—is that **muscle injury is a necessary permissive lesion**: intravenous MRSA alone caused no muscle infection in mice, but muscle injury plus bacteremia did ([PMID: 28187042](https://pubmed.ncbi.nlm.nih.gov/28187042/)). This unifies the epidemiology (young men, antecedent trauma/exercise), the microbiology (*S. aureus* predilection), and the host risk profile (immunocompromise removes the clearance safeguard). PVL toxin is the principal *severity* amplifier, converting a localized abscess into complicated, metastatic, and life-threatening disease.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|------|-----------------|--------------|
| [34407271](https://pubmed.ncbi.nlm.nih.gov/34407271/) | *Factors associated with pyomyositis: systematic review & meta-analysis* | S. aureus predominance; HIV/AIDS ORs; male-young predominance; mortality up to 20% |
| [32147332](https://pubmed.ncbi.nlm.nih.gov/32147332/) | *Pyomyositis in the United States 2002-2014* | Comorbid risk factors; >3-fold rising temperate incidence |
| [39971676](https://pubmed.ncbi.nlm.nih.gov/39971676/) | *Tropical pyomyositis* | S. aureus primary cause; immunocompromised microbiology shift; trauma link |
| [29338140](https://pubmed.ncbi.nlm.nih.gov/29338140/) | *Primary pyomyositis in North India* | Site distribution; 79% suppurative at presentation; mortality predictors |
| [19763666](https://pubmed.ncbi.nlm.nih.gov/19763666/) | *67 patients, North India* | Symptom frequencies; sepsis/death; SOFA/GCS predictors |
| [34411048](https://pubmed.ncbi.nlm.nih.gov/34411048/) | *Primary bacterial pyomyositis in children (systematic review)* | Symptom triad; 40% cured medically; surgery predictors; anatomic distribution |
| [40440680](https://pubmed.ncbi.nlm.nih.gov/40440680/) | *Pyomyositis in Children, Portugal 15-yr* | MRI 100% sensitivity; treatment durations; full recovery |
| [28187042](https://pubmed.ncbi.nlm.nih.gov/28187042/) | *"Trojan Horse" MRSA model* | Proof that muscle injury is required for seeding |
| [16452363](https://pubmed.ncbi.nlm.nih.gov/16452363/) | *PVL genes & inflammatory response* | PVL as severity determinant |
| [28248876](https://pubmed.ncbi.nlm.nih.gov/28248876/) | *Obturator externus abscess* | Stage-based treatment logic |
| [42624765](https://pubmed.ncbi.nlm.nih.gov/42624765/) | *Decolonization in S. aureus prevention* | Decolonization as mainstay of prevention |
| [29274860](https://pubmed.ncbi.nlm.nih.gov/29274860/) | *Primary pyomyositis in children* | Formal disease definition |
| [27090546](https://pubmed.ncbi.nlm.nih.gov/27090546/) | *Pyomyositis in SLE / review* | Masquerading disease; ~75% immunodeficiency |
| [26514291](https://pubmed.ncbi.nlm.nih.gov/26514291/) | *Murine thigh infection model* | Standard experimental system |
| [23031303](https://pubmed.ncbi.nlm.nih.gov/23031303/) | *Pneumococcal pyomyositis* | Non-staphylococcal bacterial cause |
| [35260400](https://pubmed.ncbi.nlm.nih.gov/35260400/) | *Thoracic pyomyositis in SLE* | DVT differential diagnosis |
| [25245285](https://pubmed.ncbi.nlm.nih.gov/25245285/) | *POCUS differentiates PM from cellulitis* | Early detection / secondary prevention |

---

## Limitations and Knowledge Gaps

1. **No precise population incidence/prevalence** — most data are hospital-based case series or administrative datasets; true community rates are unknown.
2. **Culture-negative disease is common** (~60% of blood cultures negative), limiting microbiological precision and confounding pathogen-attribution.
3. **Selection/referral bias** — the literature is dominated by severe, hospitalized cases, likely underrepresenting mild, self-limited disease.
4. **Mortality range is wide (1–23%)**, reflecting heterogeneity in setting, host comorbidity, and diagnostic delay rather than a single true figure.
5. **Model limitations** — murine models capture bacterial burden and drug response but not the full three-stage natural history or human comorbidities (HIV, chronic abscess).
6. **PVL causal weight** — much PVL severity evidence is extrapolated from osteomyelitis and other musculoskeletal infections rather than pyomyositis-specific cohorts.
7. **No host genetic susceptibility studies** — whether host immunogenetic variation modulates risk (beyond overt immunodeficiency) is unexplored.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective multicenter registry** with standardized staging, imaging, microbiology (including PVL genotyping), and outcomes to establish true incidence, mortality, and stage-specific treatment response.
2. **PVL-specific pyomyositis cohort** to quantify the independent contribution of PVL to abscess size, multifocality, metastatic spread, and surgical need.
3. **Molecular diagnostics** (16S/metagenomic sequencing on drained pus) to reduce the culture-negative gap and clarify polymicrobial/atypical etiologies.
4. **Refined animal model** combining muscle injury + controlled immunosuppression (HIV-surrogate or diabetes models) to recapitulate the full three-stage natural history for therapeutic testing.
5. **Host susceptibility study** — exome/immunogenetic screening of otherwise-healthy young men with pyomyositis to test for occult immune defects (e.g., neutrophil-function variants).
6. **Prevention trials** targeting decolonization plus risk-factor optimization in high-risk groups (HIV clinics, dialysis units, PWID programs), given waning decolonization effectiveness and rising resistance.
7. **Early-detection pathway** validating point-of-care ultrasound + inflammatory markers to catch invasive-stage disease and increase the fraction cured without drainage.

---

*Report compiled from 15 confirmed findings and 58 reviewed papers across 5 investigation iterations. Pyomyositis is characterized here as an acquired, non-genetic infectious disease; sections addressing causal genes, inheritance, and genetic screening are marked Not Applicable and reflect true biology rather than missing data.*


## Artifacts

- [OpenScientist final report](Pyomyositis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pyomyositis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 36 |
| On topic | 24 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 16 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 8 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0019168` (2 mentions) - the report calls it "MONDO"; MONDO calls it **pyomyositis**
- `HP:0100279` (1 mention) - the report calls it "Muscle swelling"; HP calls it **Ulcerative colitis**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002355` (obsolete Difficulty walking) (2 mentions) - replaced by `HP:0001288`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002355` (2 mentions) - the report calls it "Difficulty walking"; HP calls it **obsolete Difficulty walking**
- `HP:0001974` (1 mention) - the report calls it "Leukocytosis"; HP calls it **Increased total leukocyte count**, and lists "Leukocytosis" among its other names
- `HP:0011227` (1 mention) - the report calls it "Elevated CRP"; HP calls it **Elevated circulating C-reactive protein concentration**, and lists "Elevated CRP" among its other names