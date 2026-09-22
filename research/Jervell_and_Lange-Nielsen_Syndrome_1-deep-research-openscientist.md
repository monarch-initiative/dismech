---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T14:45:40.440796'
end_time: '2026-09-06T15:12:38.876076'
duration_seconds: 1618.44
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Jervell and Lange-Nielsen Syndrome 1
  mondo_id: MONDO:0024540
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
citation_count: 25
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 20
  quotes_valid: 20
  relevance_assessed: 25
  on_topic: 16
  validator_version: 0.2.1
term_validation:
  total_terms: 35
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 16
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0024540
    reported_labels:
    - if available
    ontology_label: Jervell and Lange-Nielsen syndrome 1
  - term_id: UBERON:0002215
    reported_labels:
    - stria vascularis
    - Strial marginal cell
    ontology_label: synchondrosis
  - term_id: UBERON:0007499
    reported_labels:
    - endolymph
    ontology_label: epithelial sac
  - term_id: CL:0000710
    reported_labels:
    - marginal cell of stria vascularis
    ontology_label: neurecto-epithelial cell
  - term_id: UBERON:0002228
    reported_labels:
    - spiral ganglion
    ontology_label: rib
  - term_id: HP:0011473
    reported_labels:
    - Achlorhydria
    ontology_label: Villous atrophy
  - term_id: HP:0003637
    reported_labels:
    - Hypergastrinemia
    ontology_label: Reduced circulating 4-Hydroxyphenylpyruvate dioxygenase activity
  labels_variant: 5
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
  path: Jervell_and_Lange-Nielsen_Syndrome_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Jervell_and_Lange-Nielsen_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Jervell and Lange-Nielsen Syndrome 1
- **MONDO ID:** MONDO:0024540 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Jervell and Lange-Nielsen Syndrome 1** covering all of the
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

# Jervell and Lange-Nielsen Syndrome Type 1 (JLNS1): A Comprehensive Disease Characteristics Report

**Disease:** Jervell and Lange-Nielsen Syndrome 1 · **MONDO:** 0024540 · **OMIM:** #220400 · **Category:** Mendelian (autosomal recessive channelopathy)

---

## Summary

Jervell and Lange-Nielsen syndrome type 1 (JLNS1) is a rare, severe **autosomal recessive cardio-auditory channelopathy** caused by **biallelic loss-of-function mutations in *KCNQ1*** (the α-subunit of the slow delayed-rectifier potassium current, I<sub>Ks</sub>). *KCNQ1* mutations account for roughly **90% of JLNS**, with the remainder (JLNS2) caused by biallelic *KCNE1* mutations encoding the β-subunit. The syndrome is defined by the combination of **profound congenital bilateral sensorineural deafness** and **extreme QT-interval prolongation** (mean QTc ~557 ms; diagnostic threshold >500 ms) with a very high risk of syncope, torsades de pointes, and sudden cardiac death. Prevalence is estimated at 1/1,000,000 to 1/200,000.

The unifying mechanism is loss of the same I<sub>Ks</sub> channel in two tissues. In **ventricular cardiomyocytes**, loss of I<sub>Ks</sub> removes the repolarization reserve that shortens the action potential during sympathetic activation, producing marked QT prolongation and adrenergically-triggered arrhythmia. In the **cochlea**, the KCNQ1/KCNE1 channel sits at the apical membrane of strial marginal cells and vestibular dark cells, where it secretes K⁺ into the endolymph to complete the cochlear K⁺ cycle and maintain the high-K⁺, +80 mV endocochlear potential essential for hearing; its loss collapses endolymph K⁺ secretion and causes deafness. A *Kcnq1* knockout mouse faithfully recapitulates the inner-ear pathology. A third, under-recognized arm of the disease is **gastrointestinal**: the same channel recycles K⁺ across the parietal-cell apical membrane, so its loss causes **hypochlorhydria, compensatory hypergastrinemia, gastric mucosal hyperplasia, and secondary iron-deficiency anemia**.

Clinically, JLNS1 is one of the most malignant forms of long QT syndrome: 86% of patients have cardiac events, half are symptomatic by age 3, and >25% die suddenly. **Beta-blockers are first-line but only partially effective** (51% event despite therapy), so high-risk patients (QTc >550 ms, syncope in the first year of life) require **left cardiac sympathetic denervation and/or an implantable cardioverter-defibrillator**. Deafness is managed with **cochlear implantation**, with auditory outcomes comparable to non-syndromic deafness provided strict peri-operative cardiac precautions are followed. Emerging **KCNQ1 suppression-and-replacement (SupRep) gene therapy** offers a mutation-independent, proof-of-concept correction strategy of particular relevance to JLNS1's biallelic-null genotype.

---

## Key Findings

### Finding 1 — JLNS1 is an autosomal recessive channelopathy caused by biallelic *KCNQ1* mutations (~90% of cases)

JLNS is caused by homozygous or compound heterozygous mutations in **KCNQ1 (JLNS1, ~90–90.5% of cases)** or **KCNE1 (JLNS2)**, encoding the α- and β-subunits, respectively, of the slow delayed-rectifier potassium current I<sub>Ks</sub>. Inheritance is autosomal recessive; heterozygous carriers manifest the milder, dominantly-inherited Romano-Ward LQT1 phenotype. Prevalence is estimated between 1/1,000,000 and 1/200,000 worldwide. KCNE1-associated JLNS2 tends to follow a more benign clinical course than KCNQ1-associated JLNS1.

> "Most mutations (90.5%) are on the KCNQ1 gene; mutations on the KCNE1 gene are associated with a more benign course." — [PMID: 17646758](https://pubmed.ncbi.nlm.nih.gov/17646758/)

> "Jervell and Lange-Nielsen syndrome (JLNS) is a rare but severe autosomal recessive disease characterized by profound congenital deafness and a prolonged QTc interval (greater than 500 milliseconds)... The prevalence of JLNS is about 1/1000000 to 1/200000 around the world." — [PMID: 32508908](https://pubmed.ncbi.nlm.nih.gov/32508908/)

**Ontology anchors:** Gene *KCNQ1* (HGNC:6294), *KCNE1* (HGNC:6240); MONDO:0024540; OMIM #220400. GO:0005249 (voltage-gated potassium channel activity); GO:0086003 (cardiac muscle cell contraction); CHEBI:29103 (potassium ion, K⁺).

### Finding 2 — JLNS is a severe, early-onset LQTS variant with a high cardiac-event rate and only partial beta-blocker efficacy

In the landmark international registry of 186 JLNS patients (Schwartz/Denjoy et al., 2006), **86% had cardiac events and 50% were symptomatic by age 3**, with markedly prolonged repolarization (**mean QTc 557 ± 65 ms**). Approximately **95% of arrhythmic events were triggered by emotion or exercise** (sympathetic activation), consistent with the LQT1 mechanism. **QTc >550 ms and a history of syncope in the first year of life are independent predictors of cardiac arrest/sudden death.** Beta-blockers, although first-line, provide only partial protection: 51% of patients had events despite therapy and 29% suffered cardiac arrest or sudden death. Females are at somewhat lower risk. More than 25% of JLNS patients die suddenly.

> "Most patients (86%) had cardiac events and 50% were symptomatic already by age 3. Their QTc was markedly prolonged (557 +/- 65 ms)." — [PMID: 17646758](https://pubmed.ncbi.nlm.nih.gov/17646758/)

> "A QTc>550 ms and history of syncope during the first year of life are independent predictors of subsequent CA/SD." — [PMID: 17646758](https://pubmed.ncbi.nlm.nih.gov/17646758/)

> "beta-blockers have only partial efficacy as 51% of the patients had events despite therapy and 29% had CA/SD." — [PMID: 17646758](https://pubmed.ncbi.nlm.nih.gov/17646758/)

The nationwide Spanish paediatric LQTS registry (371 children) corroborates this risk profile: major arrhythmic events clustered in "high-risk genotypes" — explicitly including Jervell-Lange-Nielsen — and in children with QTc ≥550 ms or very early (fetal/neonatal) presentation ([PMID: 42466893](https://pubmed.ncbi.nlm.nih.gov/42466893/)).

**Ontology anchors:** HP:0001657 (Prolonged QT interval); HP:0004308 (Ventricular arrhythmia / torsade de pointes); HP:0001279 (Syncope); HP:0001645 (Sudden cardiac death); HP:0001695 (Cardiac arrest).

### Finding 3 — Mechanism: loss of KCNQ1/KCNE1 I<sub>Ks</sub> abolishes marginal-cell K⁺ secretion into endolymph, causing deafness

The KCNQ1/KCNE1 channel is expressed at the **apical membrane of strial marginal cells in the cochlea and vestibular dark cells**, where it secretes K⁺ into the endolymph. This step completes the **cochlear K⁺ recycling cycle** required to maintain the high-K⁺, +80 mV endolymph and endocochlear potential (EP) that drives sensory hair-cell mechanotransduction. An additional KCNQ1/KCNE1-mediated K⁺-diffusion potential contributes to EP formation within the stria vascularis. Loss of this channel collapses endolymph K⁺ secretion, producing **profound congenital sensorineural deafness**.

> "Deafness results also from mutations of KCNQ1 or KCNE1, subunits of a K(+) channel that carries K(+) from strial marginal cells and vestibular dark cells into endolymph." — [PMID: 12097719](https://pubmed.ncbi.nlm.nih.gov/12097719/)

> "An additional K(+)-diffusion potential formed by KCNQ1/KCNE1-K" — [PMID: 20012478](https://pubmed.ncbi.nlm.nih.gov/20012478/)

The detailed K⁺ cycle (from [PMID: 12031509](https://pubmed.ncbi.nlm.nih.gov/12031509/)) situates KCNQ1/KCNE1 as the **final apical secretory step**: K⁺ enters the strial marginal cell basolaterally via SLC12A2 (NKCC1) and Na⁺/K⁺-ATPase, then exits apically into endolymph via KCNQ1/KCNE1, "which concludes the cochlear cycle." The same architecture operates in the vestibular labyrinth via dark cells, explaining associated vestibular dysfunction.

**Ontology anchors:** UBERON:0002215 (stria vascularis); UBERON:0002227 (cochlea); UBERON:0007499 (endolymph); CL:0000710 (marginal cell of stria vascularis); GO:0071805 (potassium ion transmembrane transport); GO:0042472 (inner ear morphogenesis). HP:0000407 (Sensorineural hearing impairment); HP:0000365 (Hearing impairment).

### Finding 4 — The *Kcnq1* knockout mouse recapitulates JLNS inner-ear pathology

*Kcnq1* (Kvlqt1) knockout mice are **deaf and display circling behavior** (vestibular dysfunction). Temporal-bone histopathology reveals **marked atrophy of the stria vascularis, contraction/collapse of the endolymphatic compartments, complete degeneration of the organ of Corti, and secondary spiral-ganglion degeneration** — findings that parallel human JLNS temporal-bone pathology and reflect disturbed endolymph production by the stria vascularis.

> "Kcnq1 knockout mice were deaf and demonstrated circling behavior. They exhibited a marked atrophy of the stria vascularis, contraction of the endolymphatic compartments, and collapse and adhesion of surrounding membranes. There was a complete degeneration of the organ of Corti and an associated degeneration of the spiral ganglion." — [PMID: 15891643](https://pubmed.ncbi.nlm.nih.gov/15891643/)

**Ontology anchors:** NCBITaxon:10090 (*Mus musculus*); model gene *Kcnq1* (NCBI Gene ID 16535). UBERON:0002365 (organ of Corti); UBERON:0002228 (spiral ganglion).

### Finding 5 — Management combines cardiac risk reduction with cochlear implantation

Cardiac management centers on **beta-blockers as first-line therapy** (partial protection only), escalating in high-risk patients (QTc >550 ms, syncope in the first year, aborted arrest) to **ICD implantation and/or left cardiac sympathetic denervation (LCSD)**, alongside strict avoidance of QT-prolonging drugs and sympathetic triggers. Atrial pacing combined with beta-blockade has been proposed for selected young high-risk patients ([PMID: 27451284](https://pubmed.ncbi.nlm.nih.gov/27451284/)). **Cochlear implantation** is the standard hearing rehabilitation and yields auditory/language outcomes **not worse than in non-syndromic sensorineural deafness**, provided cardiac events are controlled and strict peri-operative precautions are used (beta-blockade, avoidance of sympathetic stimulation and QT-prolonging drugs, defibrillator standby, magnesium). Importantly, LQTS/JLNS syncope can be **misdiagnosed as epilepsy**, delaying correct therapy.

> "Fatal Arrhythmias were encountered intra-operatively in five patients which was treated with cardiac pacing." — [PMID: 31846911](https://pubmed.ncbi.nlm.nih.gov/31846911/)

> "The auditory and language outcome after cochlear implantation in this syndrome is not worse than those in patients with non-syndromic sensorineural deafness." — [PMID: 18805595](https://pubmed.ncbi.nlm.nih.gov/18805595/)

> "Current treatment strategies include high doses of beta-blocker medication, left cardiac sympathetic denervation, and ICD placement, which is challenging in young children." — [PMID: 27451284](https://pubmed.ncbi.nlm.nih.gov/27451284/)

**Ontology anchors (NCIT):** Beta-adrenergic blocker therapy (propranolol, nadolol); Implantable cardioverter-defibrillator; Left cardiac sympathetic denervation (sympathectomy); Cochlear implantation.

### Finding 6 — Heterozygous carriers have milder LQT1; a common founder allele (R518X) exists

Heterozygous carriers of JLNS-causing *KCNQ1* variants show a substantially milder phenotype than homozygous JLNS patients, illustrating a **gene-dosage effect**. In a genotype-stratified cohort, mean QTc was **551 ± 54 ms in JLNS homozygotes vs 441 ± 32 ms in heterozygous-JLNS carriers and 467 ± 36 ms in heterozygous non-JLNS carriers**. The recessive JLNS phenotype (deafness + long QTc + ~47% cumulative aborted cardiac arrest) contrasts starkly with the benign dominant LQT1 phenotype of heterozygotes (QTc ~462 ms, ~1% arrest). The nonsense variant **p.R518X (c.1552C>T) in *KCNQ1*** is a common founder allele that causes JLNS when biallelic and LQT1 when heterozygous; in Sweden it is an old founder mutation (~28 generations) with heterozygote prevalence ~1:2,000–4,000, clustering geographically. **Consanguinity** contributes to JLNS in inbred families.

> "the mean QTc was 551 ± 54 ms for JLNS, 441 ± 32 ms for HTZ-JLNS, and 467 ± 36 ms for HTZ-Non-JLNS" — [PMID: 38825991](https://pubmed.ncbi.nlm.nih.gov/38825991/)

> "The R518X/KCNQ1 mutation is a common cause of autosomal recessive (Jervell and Lange Nielsen Syndrome- JLNS) and autosomal dominant long QT syndrome (LQTS) worldwide." — [PMID: 24552659](https://pubmed.ncbi.nlm.nih.gov/24552659/)

> "Clinical phenotype ranged from expectedly severe in JLNS to surprisingly benign in LQTS (QTc 576 ± 61 ms vs. 462 ± 34 ms, cumulative incidence of (aborted) cardiac arrest 47% vs. 1%" — [PMID: 24552659](https://pubmed.ncbi.nlm.nih.gov/24552659/)

**Variant nomenclature:** *KCNQ1* p.Arg518* (R518X), c.1552C>T — nonsense (loss-of-function), Pathogenic. At least one highly inbred family displayed apparent pseudo-dominant transmission with a milder phenotype and hearing/QT severity correlating ([PMID: 23668803](https://pubmed.ncbi.nlm.nih.gov/23668803/)).

### Finding 7 — JLNS has an extra-cardiac gastrointestinal phenotype: hypochlorhydria, hypergastrinemia, and iron-deficiency anemia

In a Swedish cohort of 14 patients with biallelic *KCNQ1* mutations, **a history of iron-deficiency anemia was present in 12/14 and subjective GI symptoms in 13/14**. Objective findings included elevated gastrin (7/9), elevated pepsinogen (6/7), elevated fecal calprotectin (9/9), and gastric mucosal hyperplasia/dysplasia (3/5 endoscoped). Elevated gastrin correlated significantly with iron deficiency/anemia (p = 0.039). **KCNQ1 is essential for gastric acid secretion**, recycling K⁺ across the parietal-cell apical membrane to supply the H⁺/K⁺-ATPase; its loss causes **hypochlorhydria → impaired dietary iron absorption → iron-deficiency anemia**, with compensatory **hypergastrinemia** that constitutes a potential long-term gastric-cancer risk factor.

> "A history of iron-deficiency anaemia in 12 of 14 patients and subjective gastrointestinal symptoms in 13 of 14 patients was revealed." — [PMID: 22805636](https://pubmed.ncbi.nlm.nih.gov/22805636/)

> "We propose that the Jervell and Lange-Nielsen Syndrome phenotypically includes gastrointestinal symptoms/signs and secondary iron-deficiency anaemia owing to hypochlorhydria on the basis of KCNQ1 mutations. The resultant elevated gastrin level is a potential risk factor for later gastrointestinal cancer." — [PMID: 22805636](https://pubmed.ncbi.nlm.nih.gov/22805636/)

**Ontology anchors:** HP:0001891 (Iron deficiency anemia); HP:0011473 (Achlorhydria); HP:0003637 (Hypergastrinemia); UBERON:0000945 (stomach); CL:0000162 (parietal cell); GO:0030007 (intracellular potassium ion homeostasis); CHEBI:29103 (potassium ion). Body system: digestive/gastrointestinal (UBERON:0001007).

### Finding 8 — I<sub>Ks</sub> is a multi-subunit regulated complex; patient iPSC-cardiomyocytes recapitulate LQT1 and reveal therapeutic limits for null-I<sub>Ks</sub> JLNS

The I<sub>Ks</sub> channel complex is built from **Kv7.1 (KCNQ1) co-assembled with the β-subunit KCNE1**, plus accessory regulators **PIP2, calmodulin, and yotiao (AKAP9)**. This regulatory flexibility lets one channel serve both cardiac repolarization and endolymph K⁺ maintenance. Patient-derived **iPSC-cardiomyocytes** from LQT1/*KCNQ1* carriers reproduce the disease: markedly **prolonged action-potential duration (APD)** due to reduced KCNQ1-mediated I<sub>Ks</sub>, with some mutations (e.g., R190Q, M437V) acting via dominant-negative trafficking defects. The **NOS1AP modifier locus** interacts with prolonged repolarization to modulate arrhythmia risk and penetrance. Critically, **I<sub>Ks</sub>-activator compounds shorten APD in LQT2 but not LQT1**, because LQT1/JLNS I<sub>Ks</sub> is intrinsically impaired — implying that channel-activator strategies have limited utility when I<sub>Ks</sub> is **biallelically null**, as in JLNS1.

> "The IKs channel complex is formed by the co-assembly of Kv7.1 (KCNQ1), a voltage-gated potassium channel, with its β-subunit, KCNE1 and the association of numerous accessory regulatory molecules such as PIP2, calmodulin, and yotiao." — [PMID: 32581825](https://pubmed.ncbi.nlm.nih.gov/32581825/)

> "The duration of the action potential was markedly prolonged in 'ventricular' and 'atrial' cells derived from patients with long-QT syndrome type 1, as compared with cells from control subjects." — [PMID: 20660394](https://pubmed.ncbi.nlm.nih.gov/20660394/)

> "DHA-gly shortened APD in vitro and QT interval ex vivo in WT and LQT2 rabbits, but not in LQT1" — [PMID: 40794559](https://pubmed.ncbi.nlm.nih.gov/40794559/)

Additional supporting model data: iPSC-CM from an M437V *KCNQ1* patient exhibited APD prolongation from reduced I<sub>Ks</sub> ([PMID: 31245483](https://pubmed.ncbi.nlm.nih.gov/31245483/)); human iPSC-CM engineered heart tissue has a low repolarization reserve making it a sensitive QT/arrhythmia test system ([PMID: 29925535](https://pubmed.ncbi.nlm.nih.gov/29925535/)); *NOS1AP* minor alleles associate with NOS1 loss-of-function that aggravates the arrhythmia phenotype in prolonged-repolarization syndromes ([PMID: 32061134](https://pubmed.ncbi.nlm.nih.gov/32061134/)).

**Ontology anchors:** GO:0086089 (voltage-gated potassium channel activity involved in cardiac repolarization); GO:1990573 (potassium ion import across plasma membrane); regulators AKAP9/yotiao, CALM1 (calmodulin); PIP2 (phosphatidylinositol 4,5-bisphosphate). Model: hiPSC-cardiomyocyte.

### Finding 9 — KCNQ1 suppression-and-replacement (SupRep) gene therapy is a mutation-independent proof-of-concept for LQT1/JLNS1

A dual-component **KCNQ1 "suppression-and-replacement" (SupRep)** gene therapy achieves **mutation-independent suppression of endogenous KCNQ1** (via shRNA) combined with delivery of an **shRNA-immune replacement KCNQ1 cDNA**. In TSA201 cells and LQT1 patient iPSC-cardiomyocytes, it **corrected the prolonged action-potential/QT phenotype** — the first proof-of-principle gene therapy for complete correction of long QT syndrome type 1. Because it is mutation-independent, a single construct could in principle treat any *KCNQ1* genotype, including the biallelic null alleles of JLNS1 — an important conceptual advance, since channel-activator drugs cannot rescue a null channel.

> "This study provides the first proof-of-principle gene therapy for complete correction of long QT syndrome." — [PMID: 33504163](https://pubmed.ncbi.nlm.nih.gov/33504163/)

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

```
Biallelic loss-of-function mutation in KCNQ1 (e.g., R518X; homozygous/compound het)
        │  leads to
        ▼
Absent or non-functional Kv7.1 α-subunit → failure to form functional KCNQ1/KCNE1 IKs channel
        │  results in
        ▼
Loss of the slow delayed-rectifier K+ current (IKs) in multiple K+-transporting epithelia/myocytes
        │
        ├──[CARDIAC BRANCH]──────────────────────────────────────────────┐
        │  Loss of IKs removes repolarization reserve in ventricular      │
        │  cardiomyocytes → prolonged action-potential duration →         │
        │  QT prolongation (QTc ~557 ms). Under sympathetic activation    │
        │  (emotion/exercise, ~95% of triggers), inadequate IKs upregulation
        │  → early afterdepolarizations → torsades de pointes →           │
        │  syncope / cardiac arrest / sudden death (>25%).                │
        │                                                                 │
        ├──[COCHLEAR BRANCH]─────────────────────────────────────────────┤
        │  Loss of apical KCNQ1/KCNE1 in strial marginal cells &          │
        │  vestibular dark cells → failure of K+ secretion into endolymph │
        │  → collapse of K+-rich endolymph & +80 mV endocochlear potential│
        │  → loss of hair-cell mechanotransduction driving force →        │
        │  (developmentally) strial atrophy, endolymphatic collapse,      │
        │  organ of Corti degeneration → profound congenital deafness     │
        │  (+ vestibular dysfunction).                                    │
        │                                                                 │
        └──[GASTRIC BRANCH]──────────────────────────────────────────────┘
           Loss of parietal-cell apical KCNQ1 K+ recycling → impaired
           H+/K+-ATPase-driven acid secretion → hypochlorhydria →
           (a) impaired iron absorption → iron-deficiency anemia
           (b) compensatory hypergastrinemia → gastric mucosal
               hyperplasia/dysplasia → potential long-term cancer risk.
```

The elegance of JLNS1's pathophysiology is that a **single molecular lesion** — loss of one K⁺ channel — produces a multi-organ syndrome because **KCNQ1/KCNE1 performs the same biophysical job (K⁺ efflux/recycling) in three different epithelia**. Upstream is the genetic lesion and channel loss; downstream are the tissue-specific consequences. The cardiac and cochlear arms are the classic defining dyad; the gastric arm is a more recently characterized, under-recognized systemic extension. The cardiac arm is specifically an **adrenergic/gene–environment phenotype**: I<sub>Ks</sub> is the current the healthy heart recruits (via β-adrenergic/PKA signaling anchored by yotiao/AKAP9) to shorten repolarization during sympathetic drive; without it, sympathetic stress becomes dangerous, which is why ~95% of events are triggered by emotion or exercise.

### Comparison of phenotypic arms

| Tissue / cell type | Normal KCNQ1/KCNE1 role | Consequence of loss | Clinical manifestation |
|---|---|---|---|
| Ventricular cardiomyocyte | I<sub>Ks</sub> repolarization reserve, esp. under β-adrenergic drive | Prolonged APD/QT, EADs | QTc ~557 ms, torsades, syncope, SCD |
| Strial marginal cell (UBERON:0002215) / vestibular dark cell | Apical K⁺ secretion into endolymph; EP maintenance | Endolymph K⁺ / EP collapse; strial atrophy | Profound congenital sensorineural deafness; vestibular dysfunction |
| Gastric parietal cell (CL:0000162) | Apical K⁺ recycling for H⁺/K⁺-ATPase | Hypochlorhydria; hypergastrinemia | Iron-deficiency anemia; gastric hyperplasia |

### Genotype–phenotype and dosage

| Genotype | Representative QTc | Deafness | Cardiac-arrest risk |
|---|---|---|---|
| Biallelic *KCNQ1* LOF (JLNS1) | ~551–576 ms | Profound, congenital | ~47% cumulative |
| Heterozygous JLNS-allele carrier | ~441 ms | Normal hearing | ~1% |
| Heterozygous non-JLNS LQT1 allele | ~467 ms | Normal hearing | Low |
| Biallelic *KCNE1* (JLNS2) | Prolonged | Present | More benign than JLNS1 |

---

## Section-by-Section Reference Compilation

### 1. Disease Information
JLNS1 is an autosomal recessive cardio-auditory syndrome (deafness + long QT). Identifiers: **MONDO:0024540; OMIM #220400; Orphanet ORPHA:90647**; ICD-10 **I45.81** (long QT syndrome); MeSH **D029593** (Jervell-Lange Nielsen Syndrome). Synonyms: Jervell and Lange-Nielsen syndrome; cardioauditory syndrome of Jervell and Lange-Nielsen; surdo-cardiac syndrome; long QT syndrome with deafness. Information is derived predominantly from **aggregated disease-level resources** (international LQTS registries, OMIM, Orphanet) and case series rather than individual EHR.

### 2. Etiology
**Primary cause is genetic** — biallelic LOF mutations in *KCNQ1* (JLNS1) or *KCNE1* (JLNS2) (Findings 1, 6). No infectious or purely environmental cause. **Genetic risk factors:** the causal variants; **founder alleles** (R518X) and **consanguinity** increase incidence in specific populations. **Modifiers:** *NOS1AP* polymorphisms interact with prolonged repolarization to modulate arrhythmia penetrance ([PMID: 32061134](https://pubmed.ncbi.nlm.nih.gov/32061134/)). **Acquired arrhythmia multipliers (triggers, not disease cause):** QT-prolonging drugs, sympathetic activation (emotion, exercise, sudden auditory stimuli), electrolyte disturbance. **Protective factors:** female sex confers lower cardiac risk; strict trigger avoidance and beta-blockade reduce events. **Gene–environment interaction:** the phenotype is fundamentally adrenergic — I<sub>Ks</sub> loss becomes clinically dangerous under sympathetic stress (95% of events triggered by emotion/exercise).

### 3. Phenotypes
Core phenotypes: **profound bilateral congenital sensorineural deafness** (HP:0000407; essentially fully penetrant, congenital, stable, severe) and **prolonged QT interval / torsades / syncope / sudden death** (HP:0001657, HP:0004308, HP:0001279, HP:0001645; onset neonatal–early childhood, 50% symptomatic by age 3, severe, episodic-triggered). Extra-cardiac: **iron-deficiency anemia** (HP:0001891, ~85%), **hypochlorhydria/hypergastrinemia**, GI symptoms; **vestibular dysfunction** (delayed motor milestones from balance impairment). Quality-of-life impact is substantial: lifelong deafness plus activity restriction (avoidance of competitive sport/emotional stress), device dependence (ICD/cochlear implant), and the psychological burden of sudden-death risk.

### 4. Genetic / Molecular Information
**Causal genes:** *KCNQ1* (11p15.5–15.4; OMIM *607542; HGNC:6294) — ~90%; *KCNE1* (21q22.12; OMIM *176261; HGNC:6240) — JLNS2. **Variant types:** nonsense (e.g., R518X), missense, frameshift, splice-site — predominantly loss-of-function; JLNS requires biallelic hits. Functional consequence: **loss of function / loss of I<sub>Ks</sub>**; some heterozygous LQT1 alleles act dominant-negative (trafficking defects, e.g., R190Q, M437V). **Origin:** germline. **Allele frequency:** individual pathogenic alleles are rare in gnomAD; founder alleles are regionally enriched. **Modifier:** *NOS1AP*. Epigenetic/chromosomal contributions: none established.

### 5. Environmental Information
No toxin, radiation, pollution, occupational, or infectious cause. Relevant **acquired arrhythmia modifiers**: QT-prolonging medications, hypokalemia/hypomagnesemia, sympathetic triggers. Lifestyle: avoidance of strenuous/competitive exercise and emotional stressors is recommended.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and Mechanistic Model above (Findings 3, 4, 7, 8). Molecular pathway: β-adrenergic (PKA/cAMP) → yotiao/AKAP9-anchored phosphorylation normally augments I<sub>Ks</sub>; channel loss removes this adaptive repolarization response. Cellular processes: ion transport, membrane repolarization, endolymph homeostasis, acid secretion. Protein dysfunction: loss/trafficking failure of Kv7.1. Cell types: ventricular cardiomyocytes, strial marginal cells, vestibular dark cells, gastric parietal cells.

### 7. Anatomical Structures Affected
**Primary organs:** heart (ventricular myocardium/conduction — UBERON:0000948, UBERON:0002349) and inner ear (cochlea/stria vascularis UBERON:0002227/0002215; vestibular labyrinth). **Secondary:** stomach (UBERON:0000945), hematologic system (secondary anemia), brain (secondary hypoxic-ischemic injury from arrests). **Body systems:** cardiovascular, nervous/sensory (auditory + vestibular), digestive. **Subcellular:** apical plasma membrane of epithelial cells (GO:0016324); cardiomyocyte sarcolemma. **Lateralization:** bilateral (hearing) and systemic (cardiac).

### 8. Temporal Development
**Onset:** deafness is **congenital**; cardiac events begin in infancy/early childhood (50% symptomatic by age 3; fetal/neonatal bradycardia can be a harbinger of malignant genotype). **Course:** deafness is stable/non-progressive; the cardiac phenotype is **lifelong and episodic**, with arrhythmic events triggered by adrenergic stress. **Critical period:** first year of life — syncope then is a strong predictor of subsequent cardiac arrest/sudden death. Untreated natural history carries very high early mortality.

### 9. Inheritance and Population
**Autosomal recessive.** Prevalence 1/1,000,000–1/200,000. **Penetrance** of deafness essentially complete in biallelic patients; cardiac severity variable/expressivity variable. **Founder effects** (R518X in Sweden, ~28 generations, carrier ~1:2,000–4,000) and **consanguinity** raise regional incidence. School-based ECG screening of deaf children found JLNS in ~0.9% ([PMID: 34308870](https://pubmed.ncbi.nlm.nih.gov/34308870/)). Sex ratio ~equal for the syndrome, but **females have lower cardiac-event risk**.

### 10. Diagnostics
**ECG** (Bazett QTc; diagnostic >500 ms, often >550) with exercise stress testing; **audiometry** (profound bilateral SNHL). **Genetic testing** is confirmatory: single-gene *KCNQ1*/*KCNE1* testing, LQTS/hearing-loss gene panels, or WES/WGS. Genetic testing is essential to distinguish true JLNS from the coincidental co-occurrence of independent deafness (e.g., *PCDH15*) and LQT genes ([PMID: 41563185](https://pubmed.ncbi.nlm.nih.gov/41563185/)). Supportive: elevated gastrin/pepsinogen/calprotectin and iron studies for the GI arm. **Differential diagnosis:** Romano-Ward LQTS with unrelated deafness, Pendred syndrome (deafness+goiter), Usher/Waardenburg (deafness without LQT), other LQTS genotypes; seizure disorders (syncope misdiagnosed as epilepsy).

### 11. Outcome / Prognosis
Malignant without treatment: >25% sudden death; 86% cardiac-event rate; 29% cardiac arrest/SD even on beta-blockers. **Prognostic factors:** QTc >550 ms, syncope in first year, aborted arrest, male sex, high-risk genotype = worse; female sex, controlled triggers, LCSD/ICD = better. Deafness causes permanent disability mitigated by cochlear implantation. With comprehensive management (beta-blockers + LCSD/ICD + implant), survival and function improve substantially.

### 12. Treatment
**Pharmacotherapy:** beta-blockers (propranolol, nadolol) first-line (NCIT: beta-adrenergic blocker therapy); mexiletine adjunct in some LQTS. **Device/interventional:** ICD; left cardiac sympathetic denervation (thoracoscopic — 73% arrhythmia reduction in ventricular-arrhythmia cohorts, [PMID: 24268954](https://pubmed.ncbi.nlm.nih.gov/24268954/)); atrial pacing + beta-blockade in selected young patients; catheter ablation of triggering PVCs in refractory storm ([PMID: 33040543](https://pubmed.ncbi.nlm.nih.gov/33040543/)). **Deafness:** cochlear implantation. **Supportive:** iron supplementation for the anemia arm. **Experimental/advanced:** KCNQ1 SupRep gene therapy (mutation-independent proof-of-concept, [PMID: 33504163](https://pubmed.ncbi.nlm.nih.gov/33504163/)); note I<sub>Ks</sub>-activator drugs fail in LQT1/null-I<sub>Ks</sub> ([PMID: 40794559](https://pubmed.ncbi.nlm.nih.gov/40794559/)).

### 13. Prevention
No primary prevention of the genetic disease. **Genetic counseling** and **carrier/cascade screening** in affected families; prenatal/preimplantation testing feasible. **Secondary prevention:** ECG screening of congenitally deaf children detects unrecognized JLNS ([PMID: 34308870](https://pubmed.ncbi.nlm.nih.gov/34308870/)). **Tertiary prevention:** trigger avoidance (QT-prolonging drugs, competitive sport, sudden loud stimuli), beta-blockade, device therapy, and peri-operative arrhythmia precautions during cochlear implantation.

### 14. Other Species / Natural Disease
Orthologous gene *Kcnq1* in mouse (NCBI Gene 16535, NCBITaxon:10090) and rat. No prominent naturally-occurring companion-animal JLNS equivalent is established; the disease is studied primarily via engineered rodent models. The mechanism (KCNQ1-dependent endolymph K⁺ secretion and cardiac repolarization) is **evolutionarily conserved** across mammals.

### 15. Model Organisms
**Mouse *Kcnq1* knockout** — the key model, reproducing deafness, circling/vestibular dysfunction, strial atrophy, and organ-of-Corti degeneration (Finding 4; [PMID: 15891643](https://pubmed.ncbi.nlm.nih.gov/15891643/)); species differences in ventricular repolarization reserve limit full recapitulation of the human QT phenotype. **Human iPSC-derived cardiomyocytes / engineered heart tissue** from LQT1/*KCNQ1* patients recapitulate APD/QT prolongation and serve as platforms for mechanism and therapy testing (Findings 8, 9; [PMID: 20660394](https://pubmed.ncbi.nlm.nih.gov/20660394/), [PMID: 31245483](https://pubmed.ncbi.nlm.nih.gov/31245483/), [PMID: 29925535](https://pubmed.ncbi.nlm.nih.gov/29925535/)). **Guinea-pig cardiomyocyte** pharmacological LQT1 models are used for modifier (NOS1AP) studies ([PMID: 32061134](https://pubmed.ncbi.nlm.nih.gov/32061134/)). **Rabbit LQT1 models** test I<sub>Ks</sub>-activator pharmacology ([PMID: 40794559](https://pubmed.ncbi.nlm.nih.gov/40794559/)).

---

## Evidence Base

| PMID | Role in this report | Evidence type |
|---|---|---|
| [17646758](https://pubmed.ncbi.nlm.nih.gov/17646758/) | Natural history: 90.5% KCNQ1, QTc 557 ms, 86% events, partial beta-blocker efficacy, risk predictors | Human registry (186 pts) |
| [32508908](https://pubmed.ncbi.nlm.nih.gov/32508908/) | Definition, AR inheritance, prevalence, QTc>500 ms | Human case + review |
| [12097719](https://pubmed.ncbi.nlm.nih.gov/12097719/) | KCNQ1/KCNE1 K⁺ transport into endolymph by marginal/dark cells | Review/mechanism |
| [20012478](https://pubmed.ncbi.nlm.nih.gov/20012478/) | KCNQ1/KCNE1 contributes to endocochlear potential | Mechanism |
| [12031509](https://pubmed.ncbi.nlm.nih.gov/12031509/) | Full cochlear/vestibular K⁺ cycle; KCNQ1/KCNE1 apical secretory step | Review |
| [15891643](https://pubmed.ncbi.nlm.nih.gov/15891643/) | Kcnq1 KO mouse recapitulates inner-ear pathology | Mouse model |
| [22805636](https://pubmed.ncbi.nlm.nih.gov/22805636/) | GI phenotype: hypochlorhydria, hypergastrinemia, iron-deficiency anemia | Human cohort (14 pts) |
| [24552659](https://pubmed.ncbi.nlm.nih.gov/24552659/) | R518X founder allele; severe recessive vs benign dominant phenotype | Human genealogy/genetics |
| [38825991](https://pubmed.ncbi.nlm.nih.gov/38825991/) | Gene-dosage QTc stratification | Human cohort |
| [31846911](https://pubmed.ncbi.nlm.nih.gov/31846911/) | Peri-operative arrhythmia risk in cochlear implantation | Human case series |
| [18805595](https://pubmed.ncbi.nlm.nih.gov/18805595/) | Cochlear implant outcomes equal to non-syndromic deafness | Human review |
| [27451284](https://pubmed.ncbi.nlm.nih.gov/27451284/) | Cardiac treatment options; atrial pacing + beta-blockade | Human |
| [32581825](https://pubmed.ncbi.nlm.nih.gov/32581825/) | I<sub>Ks</sub> complex composition (KCNQ1/KCNE1/PIP2/CaM/yotiao) | Review |
| [20660394](https://pubmed.ncbi.nlm.nih.gov/20660394/) | Patient iPSC-CM recapitulate APD prolongation | In vitro |
| [31245483](https://pubmed.ncbi.nlm.nih.gov/31245483/) | M437V KCNQ1 iPSC-CM: reduced I<sub>Ks</sub>, prolonged APD | In vitro |
| [29925535](https://pubmed.ncbi.nlm.nih.gov/29925535/) | hiPSC-CM engineered heart tissue as QT/arrhythmia test system | In vitro |
| [40794559](https://pubmed.ncbi.nlm.nih.gov/40794559/) | I<sub>Ks</sub>-activator fails in LQT1 | Rabbit/in vitro |
| [33504163](https://pubmed.ncbi.nlm.nih.gov/33504163/) | KCNQ1-SupRep gene therapy proof-of-concept | In vitro/iPSC-CM |
| [32061134](https://pubmed.ncbi.nlm.nih.gov/32061134/) | NOS1AP modifier of arrhythmia penetrance | GP-CM/iPSC-CM |
| [42466893](https://pubmed.ncbi.nlm.nih.gov/42466893/) | JLNS as high-risk genotype in paediatric LQTS registry | Human registry (371) |
| [34308870](https://pubmed.ncbi.nlm.nih.gov/34308870/) | JLNS prevalence (~0.9%) in deaf-school ECG screening | Human screening |
| [41563185](https://pubmed.ncbi.nlm.nih.gov/41563185/) | Genetic testing distinguishes true JLNS from coincidental deafness+LQT | Human case |
| [24268954](https://pubmed.ncbi.nlm.nih.gov/24268954/) | Thoracoscopic LCSD reduces ventricular arrhythmia burden | Human series |
| [33040543](https://pubmed.ncbi.nlm.nih.gov/33040543/) | Ablation of triggering PVC in JLNS arrhythmia storm | Human case |
| [23668803](https://pubmed.ncbi.nlm.nih.gov/23668803/) | Inbred family; hearing/QT severity correlation; consanguinity | Human family study |

---

## Limitations and Knowledge Gaps

1. **Rarity limits epidemiology.** Prevalence estimates span a five-fold range (1/1,000,000–1/200,000); incidence and geographic/variant distribution data are sparse outside founder populations.
2. **GI phenotype based on a single small cohort.** The hypochlorhydria/anemia/hypergastrinemia arm rests largely on 14 Swedish patients ([PMID: 22805636](https://pubmed.ncbi.nlm.nih.gov/22805636/)); the proposed long-term gastric-cancer risk is inferred, not demonstrated longitudinally.
3. **Model species differences.** Mice have different ventricular repolarization reserve, so the *Kcnq1* KO reproduces deafness far better than the human QT/arrhythmia phenotype; iPSC-CMs model the cardiac arm but not the intact organ or the auditory/gastric arms.
4. **Therapeutic gap for null I<sub>Ks</sub>.** Beta-blockers are only partially effective and I<sub>Ks</sub>-activators cannot rescue biallelic-null channels; SupRep gene therapy remains pre-clinical (in vitro/iPSC-CM only), with no in vivo JLNS1 efficacy data.
5. **Modifier landscape incomplete.** Beyond *NOS1AP*, the genetic/environmental determinants of the wide cardiac-severity variability are not fully mapped.
6. **Abstract availability.** Several key papers (e.g., PMID 17646758, 38825991, 27451284, 33504163, 31846911) had limited/no abstract text available; claims rely on the verified snippets recorded during the investigation.

## Proposed Follow-up Experiments / Actions

1. **Advance KCNQ1-SupRep toward in vivo proof of concept** in a humanized/biallelic-null JLNS1 model (AAV delivery to cardiomyocytes; evaluate QT correction and safety), given that activator drugs cannot rescue null I<sub>Ks</sub>.
2. **Longitudinal GI surveillance cohort** to quantify hypochlorhydria, hypergastrinemia, iron-deficiency anemia frequency, and gastric-neoplasia risk across JLNS1 patients internationally; test iron/gastrin as biomarkers.
3. **Multi-organ JLNS1 modeling** — inner-ear-specific vs cardiac-specific conditional *Kcnq1* knockouts, plus iPSC-derived otic and gastric organoids — to dissect tissue-specific consequences and test correction per arm.
4. **Genotype–phenotype and modifier studies** in an expanded JLNS registry to identify modifiers (beyond *NOS1AP*) explaining cardiac-severity variability and refine risk stratification.
5. **Prospective ECG screening programs** in congenitally deaf children (building on [PMID: 34308870](https://pubmed.ncbi.nlm.nih.gov/34308870/)) to reduce first-event sudden death through early diagnosis and beta-blockade.
6. **Peri-operative protocol standardization** for cochlear implantation in LQTS/JLNS (beta-blockade, magnesium, defibrillator standby, pacing readiness), validated across centers.

---

*Report compiled from an autonomous 5-iteration literature-based investigation. Evidence types are labeled human clinical, model organism, or in vitro throughout. All quoted snippets were verified against source abstracts where available.*


## Artifacts

- [OpenScientist final report](Jervell_and_Lange-Nielsen_Syndrome_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Jervell_and_Lange-Nielsen_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 20 |
| Quoted claims found in source | 20 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 28 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0024540` (3 mentions) - the report calls it "if available"; MONDO calls it **Jervell and Lange-Nielsen syndrome 1**
- `UBERON:0002215` (2 mentions) - the report calls it "stria vascularis", "Strial marginal cell"; UBERON calls it **synchondrosis**
- `UBERON:0007499` (1 mention) - the report calls it "endolymph"; UBERON calls it **epithelial sac**
- `CL:0000710` (1 mention) - the report calls it "marginal cell of stria vascularis"; CL calls it **neurecto-epithelial cell**
- `UBERON:0002228` (1 mention) - the report calls it "spiral ganglion"; UBERON calls it **rib**
- `HP:0011473` (1 mention) - the report calls it "Achlorhydria"; HP calls it **Villous atrophy**
- `HP:0003637` (1 mention) - the report calls it "Hypergastrinemia"; HP calls it **Reduced circulating 4-Hydroxyphenylpyruvate dioxygenase activity**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CHEBI:29103` (2 mentions) - the report calls it "potassium ion, K⁺", "potassium ion"; CHEBI calls it **potassium(1+)**, and lists "POTASSIUM ION" among its other names
- `HP:0004308` (2 mentions) - the report calls it "Ventricular arrhythmia / torsade de pointes"; HP calls it **Ventricular arrhythmia**, and lists "Ventricular arrhythmias" among its other names
- `UBERON:0002227` (2 mentions) - the report calls it "cochlea"; UBERON calls it **spiral organ of cochlea**, and lists "cochlear spiral organ" among its other names
- `UBERON:0002365` (1 mention) - the report calls it "organ of Corti"; UBERON calls it **exocrine gland**, and lists "glandula exocrina" among its other names
- `GO:0086089` (1 mention) - the report calls it "voltage-gated potassium channel activity involved in cardiac repolarization"; GO calls it **voltage-gated potassium channel activity involved in atrial cardiac muscle cell action potential repolarization**, and lists "voltage-gated potassium channel activity involved in atrial cardiomyocyte action potential repolarization" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CHEBI:29103` - called "potassium ion, K⁺", "potassium ion"
- `UBERON:0002215` - called "stria vascularis", "Strial marginal cell"
- `CL:0000162` - called "parietal cell", "Gastric parietal cell"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
