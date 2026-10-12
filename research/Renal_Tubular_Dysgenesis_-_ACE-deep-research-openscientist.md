---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-09T13:25:54.425281'
end_time: '2026-10-09T13:40:15.663298'
duration_seconds: 861.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Renal Tubular Dysgenesis - ACE
  mondo_id: MONDO:0700337
  category: Mendelian
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
citation_count: 24
reference_validation:
  total_references: 24
  verified: 22
  not_found: 2
  unverifiable: 0
  confabulation_rate: 0.083
  relevance_assessed: 22
  on_topic: 19
  unresolved_references:
  - PMID:32808512
  - PMID:18406804
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 2
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: UBERON:0002048
    reported_labels:
    - Lung (hypoplasia via oligohydramnios)
    ontology_label: lung
  - term_id: UBERON:0003129
    reported_labels:
    - Skull / cranial bones (ossification defect)
    ontology_label: skull
  - term_id: UBERON:0001155
    reported_labels:
    - Colon (microcolon; novel RTD assoc., PMID 30071301)
    ontology_label: colon
  - term_id: CL:1000697
    reported_labels:
    - Juxtaglomerular (renin-producing) cell
    ontology_label: kidney interstitial suppressor macrophage
  - term_id: HP:0001562
    reported_labels:
    - Prenatal sign
    ontology_label: Oligohydramnios
  - term_id: HP:0002615
    reported_labels:
    - Clinical sign
    ontology_label: Hypotension
  - term_id: HP:0001903
    reported_labels:
    - Lab
    ontology_label: Anemia
  labels_variant: 7
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Renal_Tubular_Dysgenesis_-_ACE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Renal_Tubular_Dysgenesis_-_ACE-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Renal Tubular Dysgenesis - ACE
- **MONDO ID:** MONDO:0700337 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Renal Tubular Dysgenesis - ACE** covering all of the
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

# Renal Tubular Dysgenesis, ACE Type (RTD-ACE) — Comprehensive Disease Report

**Disease:** Renal Tubular Dysgenesis, ACE type (RTD-ACE)
**MONDO ID:** MONDO:0700337 · **OMIM:** 267430 (Renal Tubular Dysgenesis) · **Orphanet:** ORPHA:97369 · **Category:** Mendelian (autosomal recessive)
**Causal gene:** *ACE* (angiotensin I–converting enzyme; HGNC:2707; gene OMIM 106180; chromosome 17q23.3)

---

## Summary

Renal Tubular Dysgenesis of the ACE type (RTD-ACE) is a rare, autosomal recessive developmental disorder of the kidney caused by biallelic loss-of-function (LoF) variants in *ACE*, the gene encoding angiotensin I–converting enzyme. It is one subtype within a broader genetic RTD spectrum produced by inactivating mutations in any of the four core renin–angiotensin system (RAS) genes — *AGT* (angiotensinogen), *REN* (renin), *ACE*, and *AGTR1* (angiotensin II receptor type 1). The defining lesion is **fetal angiotensin II deficiency**: without functional ACE, angiotensin I cannot be converted to the active octapeptide angiotensin II, the fetal RAS is inactive, renal perfusion pressure collapses, proximal tubules fail to differentiate, and the fetus becomes anuric. The clinical hallmark is a combination of persistent fetal anuria → oligohydramnios/anhydramnios → Potter sequence with pulmonary hypoplasia, together with refractory neonatal hypotension and defective skull ossification (large fontanelles, wide sutures). Perinatal mortality is very high.

Across genetically solved RTD families, *ACE* is the single most common cause, accounting for roughly two-thirds (≈65%) of families (Gribouval et al. 2012, [PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)). Critically, disease severity is similar regardless of which RAS gene is mutated, which points strongly to a **single unifying mechanism — loss of fetal angiotensin II signaling** — rather than any ACE-specific effect. This human genetic convergence is mirrored in mouse genetics: knockouts of *Ace*, *Agt*, and the combined *Agtr1a/Agtr1b* receptors all produce a nearly identical renal phenotype of vascular thickening, medullary atrophy/tubular lesions, hypotension, and perinatal lethality.

Although RTD-ACE was historically considered uniformly lethal, the clinical spectrum is expanding. With aggressive neonatal blood-pressure support, mechanical ventilation, and early dialysis, survivors are now reported living from years into adulthood with variable chronic kidney disease (CKD). A distinct **atypical presentation** of biallelic *ACE* LoF is also recognized: progressive childhood CKD with polyuria–polydipsia and anemia that is disproportionate to the degree of renal failure. This disproportionate anemia is mechanistically explained by the loss of angiotensin II's direct pro-erythropoietic action (both as an erythropoietin secretagogue and as a direct AT1-mediated growth factor for erythroid progenitors) — the same angiotensin II deficiency that drives the renal phenotype.

---

## Key Findings

### Finding 1 — RTD-ACE is caused by biallelic loss-of-function variants in *ACE*, within a RAS-gene RTD spectrum

RTD is genetically heterogeneous but mechanistically unified. The landmark study by Gribouval et al. 2005 ([PMID: 16116425](https://pubmed.ncbi.nlm.nih.gov/16116425/)) identified homozygous or compound heterozygous mutations in the genes encoding renin, angiotensinogen, angiotensin-converting enzyme, or angiotensin II receptor type 1 in 11 individuals from 9 families with autosomal recessive RTD, establishing that *ACE* is one of four RAS genes whose biallelic inactivation causes the disease. The authors wrote that affected individuals *"had homozygous or compound heterozygous mutations in the genes encoding renin, angiotensinogen, angiotensin converting enzyme or angiotensin II receptor type 1."*

Multiple subsequent ACE-specific case reports and series confirmed biallelic LoF *ACE* variants — spanning missense, frameshift, nonsense, and splice-site classes — as the most common genetic cause of RTD. For example, novel compound heterozygous *ACE* variants were reported in a family with recurrent anhydramnios ([PMID: 32329243](https://pubmed.ncbi.nlm.nih.gov/32329243/)), a homozygous novel 3′ splice-site variant (NM_000789.3:c.2642-1G>A) was found in a fetus with RTD ([PMID: 30058238](https://pubmed.ncbi.nlm.nih.gov/30058238/)), and *ACE* variants were associated with RTD plus a novel microcolon association ([PMID: 30071301](https://pubmed.ncbi.nlm.nih.gov/30071301/)). The progressive-CKD review by Fila et al. 2020 ([PMID: 32198635](https://pubmed.ncbi.nlm.nih.gov/32198635/)) states plainly: *"Bi-allelic loss of function variations in genes encoding proteins of the renin-angiotensin system (AGT, ACE, REN, AGTR1) are associated with autosomal recessive renal tubular dysgenesis."*

**Variant / molecular detail:**
- **Gene:** *ACE* (HGNC:2707), 17q23.3; reference transcript NM_000789.3.
- **Variant types observed:** missense (e.g., p.Ser346Trp, p.Asn489Asp), frameshift (p.S486Ffs*29), nonsense, and canonical splice-site (c.2642-1G>A).
- **Functional consequence:** loss of function — loss of ACE catalytic activity → no angiotensin II generation. In vitro/in silico analyses show such variants disrupt ACE protein structure ([PMID: 32329243](https://pubmed.ncbi.nlm.nih.gov/32329243/)).
- **Classification:** reported variants are generally pathogenic/likely pathogenic under ACMG/AMP criteria given the LoF mechanism, recessive segregation, and absence/rarity in population databases.

### Finding 2 — Mechanism: fetal RAS inactivity causes low renal perfusion, proximal-tubule maldevelopment, anuria, and Potter sequence

The histopathology of RTD directly demonstrates the developmental lesion. Lacoste et al. 2006 ([PMID: 16790508](https://pubmed.ncbi.nlm.nih.gov/16790508/)) found that *"Severe defects in proximal tubules were observed in all fetuses from 18 gestational weeks onward,"* establishing the timing of the proximal-tubule differentiation failure. The same study documented a strikingly increased renal renin signal — *"Renal renin expression was strikingly increased in 19 of 24 patients studied"* — reflecting compensatory upregulation of renin in the face of absent downstream angiotensin II signaling (a feedback hallmark of RAS failure). Thickened renal arterial vasculature (from arcuate to afferent arteries) is also characteristic, and ACE/angiotensinogen protein is absent or reduced in the proximal tubule.

Gribouval et al. 2005 ([PMID: 16116425](https://pubmed.ncbi.nlm.nih.gov/16116425/)) articulated the core causal chain: *"renal lesions and early anuria result from chronic low perfusion pressure of the fetal kidney, a consequence of renin-angiotensin system inactivity."* An earlier immunohistochemical study ([PMID: 7994002](https://pubmed.ncbi.nlm.nih.gov/7994002/)) had already noted large accumulations of renin in preglomerular arterioles and glomerular structures, consistent with faulty feedback and reduced glomerular perfusion.

Clinically, this produces a stereotyped cascade: persistent fetal anuria → oligohydramnios/anhydramnios → pulmonary hypoplasia and limb/facial deformation (Potter sequence); refractory neonatal hypotension unresponsive to vasopressors; and defective skull ossification with large fontanelles and wide cranial sutures (reported consistently across cases, e.g., [PMID: 32808512](https://pubmed.ncbi.nlm.nih.gov/32808512/), [PMID: 38649831](https://pubmed.ncbi.nlm.nih.gov/38649831/)).

### Finding 3 — High perinatal mortality but an expanding survivor spectrum, including progressive CKD

Classically, RTD causes near-universal perinatal death from the combination of pulmonary hypoplasia and anuric renal failure — in the Lacoste series all 29 cases resulted in perinatal death. However, the modern clinical picture is shifting. Schreiber et al. 2021 ([PMID: 34957720](https://pubmed.ncbi.nlm.nih.gov/34957720/)) reported a cohort of survivors in whom *"the patients are 5-20 years old with variable stages of chronic kidney disease,"* with 4 of 5 carrying *ACE* mutations. Numerous recent single-case reports describe neonates surviving the neonatal period with early peritoneal dialysis and intensive supportive management ([PMID: 42831903](https://pubmed.ncbi.nlm.nih.gov/42831903/), [PMID: 40930738](https://pubmed.ncbi.nlm.nih.gov/40930738/), [PMID: 40709124](https://pubmed.ncbi.nlm.nih.gov/40709124/), [PMID: 35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/)).

Biallelic *ACE* LoF can also present **atypically** as progressive childhood CKD rather than lethal neonatal disease. Fila et al. 2020 ([PMID: 32198635](https://pubmed.ncbi.nlm.nih.gov/32198635/)) reported that *"Bi-allelic loss of function mutation of ACE can have atypical and sometimes late presentation with chronic renal failure, anemia (out of proportion with the level of renal failure), and polyuro-polydipsia,"* broadening the recognized phenotypic range and emphasizing disproportionate anemia and a urinary concentrating defect as key atypical features. Survival with managed tubular and glomerular dysfunction has even been documented to adulthood in a related AGTR1-LoF patient (28 years old, GFR ~30 mL/min; [PMID: 33768328](https://pubmed.ncbi.nlm.nih.gov/33768328/)).

### Finding 4 — Mouse RAS-gene knockouts recapitulate the RTD renal vascular/tubular pathology and hypotension

The mouse genetics provide convergent, cross-species confirmation of the mechanism. *Ace*-null mice *"have low systolic blood pressures and defects in renal development and function"* ([PMID: 18406804](https://pubmed.ncbi.nlm.nih.gov/18406804/)). Combined AT1 receptor knockouts (*Agtr1a−/−Agtr1b−/−*) show vascular thickening within the kidney and atrophy of the inner renal medulla, a phenotype described as *"virtually identical to that seen in angiotensinogen-deficient (Agt-/-) and angiotensin-converting enzyme-deficient (Ace -/-) mice that are unable to synthesize angiotensin II"* ([PMID: 9860997](https://pubmed.ncbi.nlm.nih.gov/9860997/)). *Agt−/−* mice die shortly after birth from renal dysfunction with severe renal vascular and tubular lesions ([PMID: 11096065](https://pubmed.ncbi.nlm.nih.gov/11096065/)). Finally, mice with a catalytically inactivated ACE C-domain cannot concentrate urine effectively after dehydration — *"they are not able to concentrate urine after dehydration as effectively as wild-type mice"* ([PMID: 18158355](https://pubmed.ncbi.nlm.nih.gov/18158355/)) — modeling the tubular concentrating defect seen in human RTD survivors.

### Finding 5 — *ACE* is the predominant molecular cause (~65% of families), with gene-independent disease severity

The definitive genotype–phenotype survey, Gribouval et al. 2012 ([PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)), reviewed 54 distinct RAS-gene mutations across 48 unrelated families with autosomal recessive RTD. *ACE* mutations were the most frequent, found in **two-thirds of families (64.6%)**, and — crucially — *"The severity of the clinical course was similar whatever the mutated gene."* This gene-independence is the strongest human-genetic argument that a single downstream endpoint (angiotensin II deficiency / renal hypoperfusion) drives the disease. The same review generalizes the mechanism to acquired forms: *"Renal hypoperfusion, whether genetic or secondary to a variety of diseases, precludes the normal development/ differentiation of proximal tubules."* Developmental studies (Yosypiv, [PMID: 24061643](https://pubmed.ncbi.nlm.nih.gov/24061643/); [PMID: 21359618](https://pubmed.ncbi.nlm.nih.gov/21359618/)) add that loss of angiotensin II impairs ureteric-bud branching morphogenesis, causing medullary/papillary hypoplasia and the urinary concentrating defect.

### Finding 6 — Disproportionate anemia in ACE-RTD survivors reflects loss of angiotensin II–driven erythropoiesis

The anemia-out-of-proportion feature of ACE-LoF survivors ([PMID: 32198635](https://pubmed.ncbi.nlm.nih.gov/32198635/)) has a clear mechanistic basis. Angiotensin II is a physiological regulator of erythropoiesis, acting as both an erythropoietin secretagogue and a direct AT1-mediated growth factor for erythroid progenitors — Vlahakos et al. 2010 ([PMID: 20400218](https://pubmed.ncbi.nlm.nih.gov/20400218/)) state that *"angiotensin II (Ang II) is a physiologically important regulator of erythropoiesis."* Genetic proof comes from Kato/Fukamizu 2015 ([PMID: 26107632](https://pubmed.ncbi.nlm.nih.gov/26107632/)): *"knockout mice that lack angiotensin II, including angiotensinogen and renin knockout mice, exhibit anemia. The anemia of angiotensinogen knockout mice was rescued by angiotensin II infusion"* — and the rescue was re-blocked by an AT1 antagonist, while AT1a/AT1b double-knockout mice reproduced the anemia. Thus the same angiotensin II deficiency that drives renal maldevelopment independently impairs red-cell production, explaining why anemia in ACE-RTD is worse than renal EPO deficiency alone would predict.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1. Biallelic loss-of-function variant in ACE (missense/frameshift/nonsense/splice)
       | results in
2. Absent/deficient angiotensin I–converting enzyme catalytic activity
       | results in
3. Failure to convert angiotensin I -> angiotensin II (fetal RAS inactive)
       | leads to
4. Loss of AT1-receptor signaling + chronically low fetal renal perfusion pressure
       | branches into three downstream arms:

   ARM A (renal development — demonstrated histologically):
   5a. Impaired proximal-tubule differentiation (from ~18 wk gestation)
        + impaired ureteric-bud branching morphogenesis (inferred from mouse/dev studies)
        -> medullary/papillary hypoplasia, thickened preglomerular vasculature
        -> fetal anuria -> oligohydramnios/anhydramnios
        -> Potter sequence (pulmonary hypoplasia, limb/facial deformation)
        -> neonatal respiratory failure   <- major cause of perinatal death

   ARM B (hemodynamic):
   5b. Loss of angiotensin II vasopressor tone
        -> refractory neonatal hypotension (vasopressor-resistant)
        -> compensatory renin hypersecretion (feedback, no downstream effect)
        -> skull ossification defect (large fontanelles, wide sutures; perfusion-linked, inferred)

   ARM C (hematologic — manifest mainly in survivors):
   5c. Loss of angiotensin II pro-erythropoietic action (EPO secretagogue + direct AT1 growth factor)
        -> impaired erythropoiesis
        -> anemia disproportionate to renal failure
```

### Upstream vs downstream

The **upstream** node is unambiguous: *ACE* LoF → angiotensin II deficiency. Everything else is **downstream** and convergent. The human genetic evidence (gene-independent severity across *AGT/REN/ACE/AGTR1*; [PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)) and the mouse genetic evidence (phenotypic equivalence of *Ace−/−*, *Agt−/−*, and *Agtr1a/1b−/−*; [PMID: 9860997](https://pubmed.ncbi.nlm.nih.gov/9860997/)) jointly establish that the pathology is a readout of the final common endpoint — absent angiotensin II / AT1 signaling and renal hypoperfusion — not of any ACE-specific moonlighting function.

### Cell types, tissues, and processes

| Level | Structure / process | Ontology suggestion |
|---|---|---|
| Organ (primary) | Kidney | UBERON:0002113 |
| Organ (secondary) | Lung (hypoplasia via oligohydramnios) | UBERON:0002048 |
| Organ (secondary) | Skull / cranial bones (ossification defect) | UBERON:0003129 |
| Organ (rare assoc.) | Colon (microcolon; novel RTD assoc., PMID 30071301) | UBERON:0001155 |
| Tissue | Renal tubular epithelium | UBERON:0004135 |
| Cell | Proximal tubule epithelial cell | CL:1000838 |
| Cell | Juxtaglomerular (renin-producing) cell | CL:1000697 |
| Cell | Erythroid progenitor cell | CL:0000038 |
| Process | Proximal tubule / nephron differentiation | GO:0072014 / GO:0072006 |
| Process | Ureteric bud branching morphogenesis | GO:0060676 |
| Process | Renin–angiotensin regulation of blood pressure | GO:0002018 |
| Process | Regulation of erythropoiesis | GO:0045646 |
| Pathway | Renin–angiotensin system | KEGG hsa04614 |
| Chemical | Angiotensin II | CHEBI:2719 |

---

## Evidence Base

| PMID | Study (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [16116425](https://pubmed.ncbi.nlm.nih.gov/16116425/) | Mutations in RAS genes cause AR-RTD (Gribouval 2005) | Human genetic | F1, F2 — ACE as one of 4 RAS genes; hypoperfusion mechanism |
| [16790508](https://pubmed.ncbi.nlm.nih.gov/16790508/) | RTD, role of RAS (Lacoste 2006) | Human histopathology | F2, F3 — proximal-tubule defect from 18 wk; renin↑; perinatal death |
| [22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/) | Spectrum of RAS mutations in AR-RTD (Gribouval 2012) | Human genetic cohort | F5 — ACE = 64.6% of families; gene-independent severity |
| [32198635](https://pubmed.ncbi.nlm.nih.gov/32198635/) | Biallelic RAS mutations can present as progressive CKD (Fila 2020) | Human clinical | F1, F3, F6 — atypical CKD; disproportionate anemia; polyuro-polydipsia |
| [34957720](https://pubmed.ncbi.nlm.nih.gov/34957720/) | RTD secondary to RAS mutations (Schreiber 2021) | Human clinical | F3 — survivors 5–20 yr with variable CKD |
| [9860997](https://pubmed.ncbi.nlm.nih.gov/9860997/) | AT1A/AT1B double-KO mice | Mouse model | F4 — phenotype "virtually identical" to Ace−/−, Agt−/− |
| [18406804](https://pubmed.ncbi.nlm.nih.gov/18406804/) | Role of ACE (review) | Mouse model | F4 — Ace−/− low BP + renal developmental defects |
| [11096065](https://pubmed.ncbi.nlm.nih.gov/11096065/) | Lethality in Agt−/− mice | Mouse model | F4 — systemic AGT loss → perinatal death, renal lesions |
| [18158355](https://pubmed.ncbi.nlm.nih.gov/18158355/) | ACE C-domain main cleavage site | Mouse model | F4 — urinary concentrating defect |
| [26107632](https://pubmed.ncbi.nlm.nih.gov/26107632/) | Erythropoiesis/BP via AT1 (Kato 2015) | Mouse model | F6 — Ang II deficiency → anemia, rescued by Ang II |
| [20400218](https://pubmed.ncbi.nlm.nih.gov/20400218/) | RAS in regulation of erythropoiesis | Review | F6 — Ang II is a physiological erythropoiesis regulator |
| [24061643](https://pubmed.ncbi.nlm.nih.gov/24061643/) / [21359618](https://pubmed.ncbi.nlm.nih.gov/21359618/) | RAS in ureteric-bud branching | Developmental | F5 — Ang II loss impairs UB branching → medullary hypoplasia |
| [30071301](https://pubmed.ncbi.nlm.nih.gov/30071301/) | RTD + microcolon | Human clinical | F1 — ACE variants; novel gut association |
| [30058238](https://pubmed.ncbi.nlm.nih.gov/30058238/) / [32329243](https://pubmed.ncbi.nlm.nih.gov/32329243/) | Novel ACE splice/compound-het variants | Human genetic | F1 — variant spectrum (splice, frameshift, missense) |
| [33768328](https://pubmed.ncbi.nlm.nih.gov/33768328/) | Adult AGTR1 LoF survivor | Human clinical | F3 — survival with managed tubular/glomerular dysfunction |
| [35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/) / [42831903](https://pubmed.ncbi.nlm.nih.gov/42831903/) / [40930738](https://pubmed.ncbi.nlm.nih.gov/40930738/) / [40709124](https://pubmed.ncbi.nlm.nih.gov/40709124/) | ACE-RTD neonatal survivors | Human clinical | F3 — survival with dialysis/ventilation |

---

## Section-by-Section Characterization

### 1. Disease Information
RTD-ACE is a severe, prenatally-onset autosomal recessive disorder of kidney development characterized by poor differentiation of renal proximal tubules with a grossly normal kidney architecture, leading to fetal anuria, oligohydramnios, and Potter sequence. **Identifiers:** MONDO:0700337; OMIM 267430 (RTD phenotype); gene *ACE* OMIM 106180; Orphanet ORPHA:97369; ICD-10 Q63.8 (other specified congenital malformations of kidney). **Synonyms:** autosomal recessive renal tubular dysgenesis (AR-RTD); RTD; primary/hereditary RTD; RTD-ACE (ACE-related RTD). The knowledge base is derived from aggregated disease-level resources (OMIM, Orphanet) plus individual-patient case reports and small case series.

### 2. Etiology
**Primary cause:** biallelic (homozygous or compound heterozygous) loss-of-function variants in *ACE*. **Genetic risk factors:** consanguinity markedly increases risk (many reported families are consanguineous, e.g., [PMID: 30058238](https://pubmed.ncbi.nlm.nih.gov/30058238/), [PMID: 38649831](https://pubmed.ncbi.nlm.nih.gov/38649831/)); carrier parents are typically asymptomatic. **Environmental phenocopy:** acquired RTD occurs with in-utero exposure to RAS-blocking drugs (ACE inhibitors, ARBs) and NSAIDs ([PMID: 35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/)), and with any cause of severe fetal renal hypoperfusion (e.g., twin-twin transfusion), demonstrating a true **gene–environment convergence** on the same angiotensin II–deficiency / hypoperfusion endpoint ([PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)). **Protective factors:** none genetically established; postnatally, intensive supportive care is "protective" against early death.

### 3. Phenotypes
| Phenotype | Type | HPO term | Onset | Frequency |
|---|---|---|---|---|
| Oligohydramnios/anhydramnios | Prenatal sign | HP:0001562 | Prenatal | Near-universal |
| Fetal/neonatal anuria/oliguria | Clinical sign | HP:0100519 / HP:0100520 | Fetal/neonatal | Near-universal |
| Refractory arterial hypotension | Clinical sign | HP:0002615 | Neonatal | Very frequent |
| Pulmonary hypoplasia | Physical | HP:0002089 | Prenatal/neonatal | Very frequent |
| Large fontanelles / delayed skull ossification | Physical | HP:0000239 / HP:0010656 | Neonatal | Frequent |
| Renal tubular dysgenesis (proximal tubule paucity) | Lab/path | HP:0000107 context | Prenatal | Defining |
| Chronic kidney disease / ESKD (survivors) | Lab | HP:0012622 / HP:0003774 | Childhood | Survivors |
| Anemia (disproportionate) | Lab | HP:0001903 | Childhood | Survivors (atypical) |
| Polyuria–polydipsia / concentrating defect | Clinical | HP:0000103 / HP:0001959 | Childhood | Survivors (atypical) |

Severity is classically **severe/lethal**; the course in survivors is **progressive** toward CKD/ESKD. Quality-of-life impact in survivors is substantial (dialysis dependence, growth impairment, transplantation need).

### 4. Genetic/Molecular Information
**Causal gene:** *ACE* (gene OMIM 106180; HGNC:2707; 17q23.3). **Variant types:** missense, nonsense, frameshift, canonical splice-site; all loss-of-function. **Examples:** c.1454_1455insC p.(S486Ffs*29); c.1037C>G p.(Ser346Trp); c.1465A>G p.(Asn489Asp) ([PMID: 32329243](https://pubmed.ncbi.nlm.nih.gov/32329243/)); c.2642-1G>A splice ([PMID: 30058238](https://pubmed.ncbi.nlm.nih.gov/30058238/)). **Origin:** germline, biallelic. **Functional consequence:** loss of ACE enzymatic activity → no angiotensin II. **Allele frequency:** pathogenic alleles are rare/absent in gnomAD. **Modifier genes:** the other RAS genes act as a functional network; no formal modifier established, though gene-independent severity ([PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)) argues the pathway endpoint dominates. **Epigenetic/chromosomal:** no recurrent abnormalities reported.

### 5. Environmental Information
Non-genetic phenocopies: maternal ACE inhibitors/ARBs and NSAIDs in pregnancy; severe fetal renal hypoperfusion of any cause ([PMID: 35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/), [PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)). No infectious agents implicated. Relevant chemical entities: captopril/enalapril (ACE inhibitors), NSAIDs.

### 6. Mechanism / Pathophysiology
See the ordered causal chain above. Core pathway: **renin–angiotensin system (KEGG hsa04614)**. Upstream lesion = *ACE* LoF → angiotensin II deficiency; downstream = failed proximal-tubule differentiation and ureteric-bud branching (renal), loss of vasopressor tone (hemodynamic), and impaired erythropoiesis (hematologic). Compensatory renin hypersecretion is a diagnostic feedback signature ([PMID: 16790508](https://pubmed.ncbi.nlm.nih.gov/16790508/), [PMID: 7994002](https://pubmed.ncbi.nlm.nih.gov/7994002/)).

### 7. Anatomical Structures Affected
Primary: kidney (UBERON:0002113), specifically renal cortex proximal tubules and preglomerular vasculature. Secondary: lung (pulmonary hypoplasia, UBERON:0002048), cranial bones (UBERON:0003129), and rarely colon (microcolon, [PMID: 30071301](https://pubmed.ncbi.nlm.nih.gov/30071301/)). Body systems: urinary, cardiovascular (hemodynamic), respiratory, skeletal, and hematopoietic. Lateralization: **bilateral** renal involvement.

### 8. Temporal Development
Onset is **congenital/prenatal** (proximal-tubule defect from ~18 gestational weeks; [PMID: 16790508](https://pubmed.ncbi.nlm.nih.gov/16790508/)). Course: historically lethal in the perinatal period; in survivors, **chronic and progressive** toward ESKD over years ([PMID: 34957720](https://pubmed.ncbi.nlm.nih.gov/34957720/)). Critical intervention window is the immediate neonatal period (BP support, ventilation, dialysis); prenatal diagnosis enables counseling and planning.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** high/complete for biallelic LoF, though with variable expressivity (lethal vs survivor-CKD vs atypical late CKD). **Consanguinity** is a major contributor. **Carrier frequency:** low; founder effects not firmly established. **Epidemiology:** very rare (Orphanet class <1/1,000,000); exact prevalence/incidence not well quantified. **Sex ratio:** approximately equal (autosomal). *ACE* accounts for ≈65% of genetically solved families ([PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)).

### 10. Diagnostics
**Prenatal:** oligohydramnios/anhydramnios on ultrasound; enlarged echogenic kidneys with poor corticomedullary differentiation. **Postnatal labs:** anuria, refractory hypotension, markedly elevated plasma renin activity with undetectable/low ACE ([PMID: 32808512](https://pubmed.ncbi.nlm.nih.gov/32808512/)). **Imaging:** skull X-ray showing large fontanelles/wide sutures; renal ultrasound. **Histopathology (definitive morphology):** absent/paucal differentiated proximal tubules with increased renin immunostaining. **Genetic testing (definitive):** WES/WGS or RAS-gene panels (*ACE, AGT, REN, AGTR1*) — WES identified ACE variants in multiple cases ([PMID: 30058238](https://pubmed.ncbi.nlm.nih.gov/30058238/), [PMID: 35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/)). **Differential diagnosis:** ARPKD, bilateral renal agenesis/dysplasia, other CAKUT, and acquired (drug-induced) RTD. Prenatal diagnosis is available for at-risk pregnancies after family variant identification.

### 11. Outcome/Prognosis
Historically very poor — near-universal perinatal death ([PMID: 16790508](https://pubmed.ncbi.nlm.nih.gov/16790508/)). With modern intensive care and dialysis, survivors reach 5–20 years with variable CKD/ESKD ([PMID: 34957720](https://pubmed.ncbi.nlm.nih.gov/34957720/)); an adult AGTR1 survivor retained GFR ~30 mL/min with managed tubular/glomerular dysfunction ([PMID: 33768328](https://pubmed.ncbi.nlm.nih.gov/33768328/)). Complications: pulmonary hypoplasia, ESKD, growth impairment, disproportionate anemia. Prognostic factors: degree of pulmonary hypoplasia, postnatal urine-output trajectory, and feasibility of dialysis.

### 12. Treatment
No curative therapy; management is **supportive**. Neonatal: mechanical ventilation, aggressive vasopressor/blood-pressure support, early peritoneal dialysis ([PMID: 42831903](https://pubmed.ncbi.nlm.nih.gov/42831903/), [PMID: 40930738](https://pubmed.ncbi.nlm.nih.gov/40930738/)). Longer-term: renal replacement therapy and eventual kidney transplantation; fludrocortisone has been used to treat hyperkalemia/salt-wasting in a RAS-LoF survivor ([PMID: 33768328](https://pubmed.ncbi.nlm.nih.gov/33768328/)); erythropoiesis-stimulating agents for the anemia. RAS-blocking drugs are **contraindicated** (would worsen the deficiency). No gene/cell/RNA therapies exist. NCIT terms: Dialysis (NCIT:C15248), Kidney Transplantation (NCIT:C15366), Supportive Care (NCIT:C15285).

### 13. Prevention
No primary prevention of the genetic form. **Secondary/tertiary:** avoid RAS inhibitors and NSAIDs in pregnancy (prevents acquired phenocopy); prenatal and preimplantation genetic diagnosis for at-risk couples after variant identification; **genetic counseling** for consanguineous and previously affected families; cascade carrier testing. Early prenatal detection enables planned delivery at a tertiary center with neonatal dialysis capability.

### 14. Other Species / Natural Disease
No naturally occurring companion-animal RTD-ACE is well documented; the disease is primarily defined in humans. Orthologous genes are conserved — mouse *Ace* (NCBI Gene 11421), *Agt*, *Ren*, *Agtr1a/Agtr1b*. The renal mechanism is **evolutionarily conserved** across mammals, as evidenced by matching mouse knockout phenotypes. Experimental species: *Mus musculus* (NCBI:txid10090), *Rattus norvegicus*.

### 15. Model Organisms
The mouse is the primary model. Relevant genetic models: *Ace−/−* (low BP, renal developmental defects; [PMID: 18406804](https://pubmed.ncbi.nlm.nih.gov/18406804/)); *Agt−/−* (perinatal lethal, renal vascular/tubular lesions; [PMID: 11096065](https://pubmed.ncbi.nlm.nih.gov/11096065/)); *Agtr1a−/−Agtr1b−/−* double knockout (renal vascular thickening, medullary atrophy; [PMID: 9860997](https://pubmed.ncbi.nlm.nih.gov/9860997/)); ACE C-domain–inactive knock-in (urinary concentrating defect; [PMID: 18158355](https://pubmed.ncbi.nlm.nih.gov/18158355/)). **Phenotype recapitulation:** high — these models reproduce the renal vascular/tubular pathology, hypotension, concentrating defect, and anemia. **Limitations:** mouse models capture the renal and hemodynamic lesions but the human Potter-sequence/pulmonary-hypoplasia context differs, and the atypical human progressive-CKD phenotype is less directly modeled.

---

## Limitations and Knowledge Gaps

1. **Rarity and small cohorts.** Most evidence derives from single case reports and modest series; precise prevalence, incidence, penetrance, and survival statistics are not firmly established.
2. **Genotype–phenotype resolution.** Although severity appears gene-independent, it remains unclear what determines whether a given biallelic *ACE* LoF produces lethal neonatal disease versus the atypical progressive-CKD phenotype — residual ACE activity, modifier genes, or environmental factors are all plausible but untested.
3. **Inferred steps in the causal chain.** The link from angiotensin II deficiency to skull ossification defects, and the ureteric-bud branching contribution in humans, is extrapolated largely from mouse/developmental data rather than demonstrated directly in human RTD-ACE tissue.
4. **Survivor natural history.** Long-term outcomes (renal, neurocognitive, cardiovascular) in the growing survivor population are incompletely characterized; the oldest well-documented survivors are only ~20 years old.
5. **No disease-specific therapeutics.** No treatment restores fetal angiotensin II signaling during the critical developmental window; management is entirely supportive.

## Proposed Follow-up Experiments / Actions

1. **International RTD-ACE registry** to quantify prevalence, survival with modern care, and long-term survivor outcomes, enabling evidence-based prognostic counseling.
2. **Systematic ACE genotype–residual-activity correlation** (functional assays of patient variants) to test whether partial/hypomorphic activity predicts the atypical progressive-CKD phenotype versus lethal disease.
3. **Kidney-organoid and iPSC models** carrying patient *ACE* variants to dissect the human proximal-tubule differentiation defect and test whether exogenous angiotensin II (or AT1 agonism) during a developmental window rescues tubulogenesis.
4. **Prospective anemia characterization in survivors** — measure EPO, reticulocyte response, and ESA responsiveness to confirm the angiotensin II–erythropoiesis mechanism clinically and optimize anemia management.
5. **Standardized neonatal management protocol** (BP targets, timing of dialysis, ventilation strategy) evaluated prospectively, given the expanding survivor spectrum.
6. **Pharmacovigilance / public-health messaging** reinforcing avoidance of RAS inhibitors and NSAIDs in pregnancy to prevent acquired phenocopies.

---

*Report compiled from 6 confirmed findings and 42 reviewed papers over 5 investigation iterations. Evidence types are distinguished throughout as human clinical, human genetic/histopathology, mouse model, or review.*


## Artifacts

- [OpenScientist final report](Renal_Tubular_Dysgenesis_-_ACE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Renal_Tubular_Dysgenesis_-_ACE-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 2 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 19 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:32808512` (5 mentions) - Identifier did not resolve to a record
- `PMID:18406804` (6 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 16 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002048` (2 mentions) - the report calls it "Lung (hypoplasia via oligohydramnios)"; UBERON calls it **lung**
- `UBERON:0003129` (2 mentions) - the report calls it "Skull / cranial bones (ossification defect)"; UBERON calls it **skull**
- `UBERON:0001155` (1 mention) - the report calls it "Colon (microcolon; novel RTD assoc., PMID 30071301)"; UBERON calls it **colon**
- `CL:1000697` (1 mention) - the report calls it "Juxtaglomerular (renin-producing) cell"; CL calls it **kidney interstitial suppressor macrophage**
- `HP:0001562` (1 mention) - the report calls it "Prenatal sign"; HP calls it **Oligohydramnios**
- `HP:0002615` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotension**
- `HP:0001903` (1 mention) - the report calls it "Lab"; HP calls it **Anemia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0004135` (1 mention) - the report calls it "Renal tubular epithelium"; UBERON calls it **distal tubule**, and lists "renal distal tubule" among its other names
- `CL:1000838` (1 mention) - the report calls it "Proximal tubule epithelial cell"; CL calls it **kidney proximal convoluted tubule epithelial cell**
- `GO:0060676` (1 mention) - the report calls it "Ureteric bud branching morphogenesis"; GO calls it **ureteric bud formation**
- `GO:0002018` (1 mention) - the report calls it "Renin–angiotensin regulation of blood pressure"; GO calls it **renin-angiotensin regulation of aldosterone production**
- `GO:0045646` (1 mention) - the report calls it "Regulation of erythropoiesis"; GO calls it **regulation of erythrocyte differentiation**
- `CHEBI:2719` (1 mention) - the report calls it "Angiotensin II"; CHEBI calls it **Ile(5)-angiotensin II**, and lists "Angiotensin II" among its other names
- `HP:0002089` (1 mention) - the report calls it "Physical"; HP calls it **Pulmonary hypoplasia**, and lists "Hypoplastic lung" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:2707` - called "ACE", "Gene:** *ACE"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.