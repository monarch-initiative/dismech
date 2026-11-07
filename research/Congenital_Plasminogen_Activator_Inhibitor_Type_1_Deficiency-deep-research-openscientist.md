---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-02T23:46:36.989110'
end_time: '2026-11-02T23:58:30.296754'
duration_seconds: 713.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Plasminogen Activator Inhibitor Type 1 Deficiency
  mondo_id: MONDO:0013227
  category: Mendelian
  causal_genes: SERPINE1
  omim_id: OMIM:613329
  synonyms: congenital PAI-1 deficiency
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 4
  validator_version: 0.4.0
term_validation:
  total_terms: 36
  verified: 32
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 9
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CL:0000115
    reported_labels:
    - endothelium
    - Tissue/cell level:** vascular **endothelium
    ontology_label: endothelial cell
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Plasminogen_Activator_Inhibitor_Type_1_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Plasminogen_Activator_Inhibitor_Type_1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Plasminogen Activator Inhibitor Type 1 Deficiency
- **MONDO ID:** MONDO:0013227 (if available)
- **Causal gene(s):** SERPINE1
- **OMIM:** OMIM:613329
- **Synonyms:** congenital PAI-1 deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Plasminogen Activator Inhibitor Type 1 Deficiency** covering all of the
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

# Congenital Plasminogen Activator Inhibitor Type 1 (PAI-1) Deficiency — Comprehensive Disease Characterization

**Causal gene: SERPINE1** (encoding plasminogen activator inhibitor‑1, PAI‑1). **MONDO:0013227 · OMIM:613329.**

> **Summary answer.** Congenital PAI‑1 deficiency is an extremely rare, autosomal‑recessive bleeding disorder caused by biallelic loss‑of‑function mutations in **SERPINE1**, the gene that encodes plasminogen activator inhibitor‑1 (PAI‑1), the principal physiologic inhibitor of tissue‑type (tPA) and urokinase‑type (uPA) plasminogen activators. Absence of PAI‑1 removes the brake on plasminogen activation, causing a hyperfibrinolytic state in which hemostatic fibrin clots are degraded prematurely. Clinically this produces moderate, characteristically **trauma‑/surgery‑provoked and delayed bleeding** (plus menorrhagia and easy bruising) with **normal routine coagulation tests**; it responds well to antifibrinolytic drugs (tranexamic acid, ε‑aminocaproic acid). Chronic complete deficiency also has extra‑hemostatic consequences (notably cardiac fibrosis) and pleiotropic effects on cellular senescence/aging.

Evidence base: predominantly **human clinical** (case reports and the Old Order Amish founder kindred), supported by **model‑organism** (Serpine1‑knockout mouse), **in vitro** (CRISPR knockout endothelial cells and iPSC‑cardiomyocytes), and **computational/structural** data. There is no large registry; most knowledge is disease‑level/aggregated from small series plus one extended pedigree, not population EHR.

---

## 1. Disease Information

**Overview.** PAI‑1 deficiency is a disorder of the fibrinolytic (clot‑dissolving) system. PAI‑1 normally down‑regulates fibrinolysis; when it is absent, plasminogen activators act unopposed, plasmin is generated in excess, and fibrin clots lyse prematurely, producing a bleeding diathesis (Jain & Acharya 2019, PMID 31427261; Mehta & Shapiro 2008, PMID 19141166).

**Key identifiers.**
- **MONDO:** MONDO:0013227
- **OMIM:** 613329 (Plasminogen activator inhibitor‑1 deficiency)
- **Gene:** SERPINE1 (HGNC:8583; NCBI Gene 5054; Ensembl ENSG00000106366; UniProt protein P05121), chromosome **7q22.1**
- **Orphanet:** ORPHA:465 (congenital PAI‑1 deficiency)
- **ICD‑10:** D68.8 (other specified coagulation defects) — no PAI‑1‑specific code; **ICD‑11:** 3B19.Y (other specified coagulation defects) / fibrinolysis defect
- **MeSH:** no dedicated descriptor; indexed under *Plasminogen Activator Inhibitor 1* (D017395) and *Hemorrhagic Disorders*

**Synonyms / alternative names.** Congenital PAI‑1 deficiency; complete PAI‑1 deficiency; plasminogen activator inhibitor type 1 deficiency; PAI‑1 deficiency; SERPINE1‑related bleeding disorder.

**Data source type.** Disease‑level aggregated knowledge drawn from individual patient reports and one large, well‑characterized pedigree (Old Order Amish). No population‑scale EHR or registry prevalence exists; the Dutch RBiN cohort (PMID 42780071) is among the few systematic patient series (14 PAI‑1‑deficient patients).

---

## 2. Etiology

**Causal factor — genetic.** The disease is monogenic: homozygous or compound‑heterozygous loss‑of‑function variants in **SERPINE1** abolish functional PAI‑1. The canonical mutation is the Old Order Amish founder frameshift **SERPINE1 c.699_700dupTA** (exon 4), causing complete, "absolute" PAI‑1 deficiency (Fay et al. 1997, PMID 9207454; Khan et al. 2021, PMID 33439236). It is **not** infectious or primarily environmental.

**Genetic risk factors.** Biallelic null SERPINE1 genotype is both necessary and sufficient. Carrier (heterozygous) status is clinically silent for bleeding (Fay 1997). Consanguinity/endogamy (as in the Amish) raises homozygosity risk; a founder effect concentrates the c.699_700dupTA allele in that community.

**Environmental risk factors (for bleeding events, not for the disease itself).** Trauma, surgery, dental extraction, menstruation, childbirth, and antithrombotic/antiplatelet drugs unmask or worsen bleeding. Bleeding is overwhelmingly **provoked** rather than spontaneous (Mehta & Shapiro 2008).

**Protective factors.** Antifibrinolytic prophylaxis (tranexamic acid, ε‑aminocaproic acid) prevents provoked bleeding. Intriguingly, at the systemic level **loss of PAI‑1 is itself "protective" against aging/metabolic pathology**: PAI‑1 is a pro‑senescence factor, and null carriers show longer leukocyte telomeres, lower fasting insulin, and extended lifespan (Khan et al. 2017, PMID 29152572) — a protective‑direction pleiotropy opposite to the hemostatic deficit.

**Gene–environment interaction.** Genotype sets a lifelong hyperfibrinolytic baseline; the *phenotype* (a bleed) emerges only when a hemostatic challenge (trauma/surgery/menses) occurs. In mouse models, hemodynamic stress (angiotensin II, norepinephrine) is required to reveal cardiac hemorrhage/fibrosis in PAI‑1‑/‑ animals (Pettey et al. 2025, PMID 41332700), a clear G×E pattern.

---

## 3. Phenotypes

All manifestations are hemostatic or their sequelae. Onset is **congenital** (lifelong), severity **mild‑to‑moderate**, course **episodic/provoked and non‑progressive** (Mehta & Shapiro 2008, PMID 19141166; Fay 1997, PMID 9207454).

| Phenotype | Type | Characteristics / frequency | Suggested HPO |
|---|---|---|---|
| Abnormal bleeding tendency | Clinical sign | Core feature, provoked/delayed; essentially all homozygotes | HP:0001892 (Abnormal bleeding) |
| Prolonged/delayed bleeding after surgery or trauma | Clinical sign | Hallmark; "delayed rebleeding" after initial hemostasis | HP:0004846 (Prolonged bleeding after surgery) |
| Menorrhagia / heavy menstrual bleeding | Symptom | Common and often most burdensome in affected women | HP:0000132 (Menorrhagia) |
| Epistaxis | Symptom | Reported, mild‑moderate | HP:0000421 (Epistaxis) |
| Easy bruising | Clinical sign | Frequent | HP:0000978 (Bruising susceptibility) |
| Joint bleeding (hemarthrosis) | Clinical sign | After mild trauma; reported in severe cases | HP:0005261 (Hemarthrosis) |
| Intracranial hemorrhage | Clinical sign | After mild head trauma; serious but uncommon | HP:0002170 (Intracranial hemorrhage) |
| Postpartum/obstetric hemorrhage | Clinical sign | Risk period in affected women | HP:0011891 (Postpartum hemorrhage) |
| Myocardial/cardiac fibrosis | Physical/imaging | 6/9 (67%) young adult homozygotes with late gadolinium enhancement vs 0/8 controls (P=0.001) | HP:0001637 (Abnormal myocardium/fibrosis) |
| Enhanced fibrinolysis / shortened clot lysis | Laboratory abnormality | Universal; functional diagnostic signature | HP:0040239 / lab finding |
| Delayed wound healing | Clinical sign | Reported with congenital deficiency (in vitro corroboration) | HP:0001058 (Poor wound healing) |

**Quality‑of‑life impact.** Generally modest between events; episodic bleeds (especially menorrhagia, surgical/obstetric bleeding) can cause anemia, activity restriction, and procedural anxiety. With antifibrinolytic management, daily functioning is typically near‑normal. No validated disease‑specific QoL instrument exists; generic bleeding‑disorder tools (e.g., ISTH‑BAT bleeding assessment) apply.

---

## 4. Genetic / Molecular Information

- **Causal gene:** **SERPINE1** (HGNC:8583; OMIM gene 173360; 7q22.1), encoding PAI‑1 (serpin clade E, member 1).
- **Pathogenic variants.** Reported variants are **loss‑of‑function/null**:
  - **c.699_700dupTA** (exon 4 frameshift) — Amish founder allele; **germline**, classified **pathogenic** (ACMG: PVS1 null + segregation + absent antigen) (Khan 2021, PMID 33439236; Fay 1997, PMID 9207454).
  - Other families carry distinct frameshift/truncating SERPINE1 defects (only a few genetically characterized; Mehta & Shapiro 2008, PMID 19141166).
- **Variant class / consequence:** frameshift → premature stop → **complete loss of function** (no measurable PAI‑1 antigen/activity). Not gain‑of‑function, not dominant‑negative.
- **Allele frequency:** biallelic null genotype is vanishingly rare in gnomAD; the founder allele is enriched only in the Amish subpopulation.
- **Somatic vs germline:** germline.
- **Modifier genes:** other fibrinolytic components (plasminogen, α2‑antiplasmin, TAFI, tPA/uPA levels) and the common **SERPINE1 promoter 4G/5G polymorphism (rs1799889)** modulate *PAI‑1 level* in the general population but are not the cause of congenital deficiency; they are plausible phenotype modifiers.
- **Epigenetic information:** SERPINE1 expression is strongly inducible (TGF‑β, hypoxia, inflammation) but no disease‑specific epigenetic lesion is implicated in congenital deficiency.
- **Chromosomal abnormalities:** none; this is a single‑gene point/indel disorder.

---

## 5. Environmental Information

- **Environmental factors:** none cause the disorder. Environmental/physiologic *triggers of bleeding* include trauma, surgery, dental procedures, menstruation, and childbirth. Antithrombotics/NSAIDs can aggravate bleeding.
- **Lifestyle factors:** contact sports and activities with trauma risk increase bleed likelihood; alcohol may affect fibrinolysis marginally.
- **Infectious agents:** not applicable — non‑infectious Mendelian disease.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Biallelic null **SERPINE1** mutation (e.g., c.699_700dupTA) **leads to** absence of functional PAI‑1 protein (loss of function; confirmed by undetectable PAI‑1 antigen/activity).
2. Loss of PAI‑1 **results in** failure to inhibit tissue‑type (tPA) and urokinase‑type (uPA) plasminogen activators (de‑repression of the principal serpin brake).
3. Unopposed tPA/uPA activity **leads to** increased conversion of plasminogen to **plasmin** (enhanced plasmin generation — demonstrated in patients and in CRISPR PAI‑1‑knockout endothelial cells).
4. Excess pericellular and fluid‑phase plasmin **results in** accelerated proteolysis of fibrin (and fibrinogen) — i.e., **hyperfibrinolysis**.
5. Hyperfibrinolysis **leads to** premature dissolution of newly formed hemostatic clots → **delayed rebleeding** after an initially normal clot forms.
6. When a hemostatic challenge (trauma, surgery, menses, delivery) occurs, premature clot lysis **results in** the clinical bleed (mucosal, surgical, joint, intracranial). *(Branch A — the bleeding phenotype.)*
7. **Branch B (tissue remodeling, chronic):** chronically unopposed plasmin/plasminogen activation **leads to** excess activation of matrix metalloproteinases and degradation of vascular/extracellular matrix; under hemodynamic stress this **results in** microvascular rupture, hemorrhage, and subsequent reparative/replacement **cardiac fibrosis** (demonstrated in PAI‑1‑/‑ mice; associated with late gadolinium enhancement in human homozygotes — the human step is *associative/inferred*, mouse step *demonstrated*).
8. **Branch C (senescence/aging):** because PAI‑1 is a pro‑senescence SASP effector downstream of TGF‑β, its absence **leads to** reduced cellular‑senescence signaling, associated with longer telomeres and favorable metabolic/longevity measures (*inferred* from carrier associations and murine accelerated‑aging models).

**Supporting detail by category.**
- *Molecular pathways:* fibrinolysis / plasminogen‑activation system (KEGG "Complement and coagulation cascades" hsa04610; Reactome "Dissolution of Fibrin Clot" R‑HSA‑75205). PAI‑1 is a downstream effector of **TGF‑β** signaling (relevant to fibrosis) and of hypoxia/inflammatory induction.
- *Cellular processes:* pericellular proteolysis, cell migration/adhesion (PAI‑1–vitronectin axis), angiogenesis, inflammation, and **cellular senescence** (GO:0090398). PAI‑1‑KO endothelial cells show disordered, multidirectional migration and impaired directed wound closure (Sano et al. 2026, PMID 42946217).
- *Protein dysfunction:* **loss of a metastable serpin.** Active PAI‑1 is metastable and normally converts to a latent form; it inhibits proteases via its reactive‑center loop and binds vitronectin (Sharp et al. 1999, PMID 10368279). In disease the protein is simply **absent** (truncated), not misfolded/aggregated.
- *Tissue‑damage mechanisms:* hemorrhage, and (under stress) plasmin‑mediated matrix degradation → fibrosis.
- *Biochemical abnormality:* absent serine‑protease‑inhibitor (anti‑tPA/anti‑uPA) activity.
- *GO terms:* serine‑type endopeptidase inhibitor activity (GO:0004867); negative regulation of fibrinolysis (GO:0051918); plasminogen activation (GO:0031639); negative regulation of plasminogen activation. *CL cell types:* endothelial cell (CL:0000115), hepatocyte (CL:0000182, systemic PAI‑1 source), platelet (CL:0000233, α‑granule PAI‑1 store), cardiomyocyte (CL:0000746), adipocyte (CL:0000136).

---

## 7. Anatomical Structures Affected

- **Organ/system level — primary:** blood & hemostatic system (UBERON:0000178 blood; cardiovascular system UBERON:0004535). Bleeding sites: nasal mucosa (epistaxis), oral cavity/gingiva, uterus/endometrium (menorrhagia), joints (hemarthrosis), and brain (intracranial hemorrhage).
- **Secondary/complication organs:** **heart** (myocardial fibrosis; UBERON:0000948), **brain** (UBERON:0000955, hemorrhage), musculoskeletal (joints UBERON:0001485), and **skin/soft tissue** (bruising, delayed wound healing; UBERON:0002097).
- **Tissue/cell level:** vascular **endothelium** (CL:0000115) and sub‑endothelial matrix; connective tissue/ECM; **platelets** (α‑granule PAI‑1); hepatocytes and adipocytes as systemic PAI‑1 sources; cardiomyocytes/cardiac interstitium in the fibrosis branch.
- **Subcellular (GO Cellular Component):** secreted/**extracellular space** (GO:0005615); PAI‑1 is stored in platelet **secretory (α‑)granules** (GO:0031093) and associates with extracellular matrix via vitronectin.
- **Localization / lateralization:** bleeding is site‑dependent and typically focal to the site of trauma (not inherently lateralized); cardiac fibrosis tends to be regional (epicardial/posterior septum in models; patchy late gadolinium enhancement in humans).

---

## 8. Temporal Development

- **Onset:** congenital (genotype present from birth); bleeding often first noted in childhood with trauma, circumcision, or menarche.
- **Onset pattern:** chronic/insidious trait with acute, provoked bleeding episodes.
- **Progression:** the hemostatic defect is **stable and non‑progressive**; course is **episodic/provoked**. Characteristic *delayed* bleeding (initial clot then lysis) is a temporal signature.
- **Duration:** lifelong.
- **Patterns/critical periods:** menarche/menstruation, surgery/dental procedures, trauma, pregnancy/delivery, and the neonatal period (analogy from PAI‑1‑/‑ pups showing age‑window vulnerability to intracerebral hemorrhage; Leroux et al. 2014, PMID 24709679) are windows of vulnerability and of intervention (peri‑procedural antifibrinolytics). The cardiac‑fibrosis branch is a slow, adult‑emerging process.

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** (only homozygotes/compound heterozygotes are symptomatic; heterozygotes are asymptomatic for bleeding) (Fay 1997, PMID 9207454).
- **Penetrance/expressivity:** complete deficiency reliably produces a hyperfibrinolytic laboratory state; *clinical* bleeding is high‑penetrance but **provocation‑dependent** with variable expressivity (severity ranges from easy bruising to intracranial bleeds).
- **Anticipation / mosaicism:** not applicable / not reported.
- **Founder effect & consanguinity:** classic **founder effect** (c.699_700dupTA) in the **Old Order Amish**; endogamy increases homozygote frequency.
- **Carrier frequency:** low in the general population; elevated within the Amish founder community.
- **Epidemiology:** **extremely rare**; precise prevalence/incidence not established (only a handful of families worldwide plus the Amish kindred and small cohorts such as RBiN). Orphanet classifies it as a rare coagulation disorder.
- **Demographics:** no ethnic predilection beyond the Amish founder cluster; **sex ratio ≈ 1:1 genotypically**, but clinical burden is greater in women (menorrhagia, obstetric hemorrhage). Age distribution: lifelong, all ages.

---

## 10. Diagnostics

**Core principle:** routine coagulation (PT, aPTT) and platelet function tests are **normal**, so a high index of suspicion plus specialized fibrinolysis testing is required (Jain & Acharya 2019, PMID 31427261).

- **Laboratory / biomarkers:**
  - **PAI‑1 antigen (ELISA):** undetectable in complete deficiency.
  - **PAI‑1 activity assay:** low/absent — but note the key pitfall that activity assays are poorly discriminating at the **low end** ("normal ranges begin at zero"), so a low value cannot by itself prove deficiency (Mehta & Shapiro 2008, PMID 19141166).
  - **Global fibrinolysis assays:** shortened **euglobulin clot lysis time**, shortened turbidimetric **clot lysis time**, and **enhanced plasmin generation** — functional confirmation of hyperfibrinolysis.
  - Ancillary: tPA/α2‑antiplasmin/plasminogen levels to exclude mimics.
- **Genetic testing (definitive):** **single‑gene SERPINE1 sequencing** is the gold standard; bleeding‑disorder/fibrinolysis **gene panels** or **WES/WGS** are useful when the phenotype is non‑specific. CMA/karyotype/FISH/mtDNA/repeat testing are **not applicable**. Targeted variant testing (e.g., c.699_700dupTA) enables **cascade testing** in founder families.
- **Imaging:** cardiac **MRI with late gadolinium enhancement** detects the associated myocardial fibrosis (Khan 2021, PMID 33439236); CT/MRI for suspected intracranial hemorrhage.
- **Clinical criteria / differential diagnosis:** no formal diagnostic criteria. Differentials among hyperfibrinolytic bleeding disorders: **α2‑antiplasmin deficiency** (typically more severe bleeding), **Quebec platelet disorder** (uPA‑rich platelets, gain‑of‑function), **tPA excess**, and acquired hyperfibrinolysis (DIC, liver disease, APL). Distinguish by specific factor assays and SERPINE1 genetics.
- **Screening:** no newborn screening. **Carrier/cascade screening** and prenatal/preimplantation testing are feasible in founder families via targeted variant analysis.

---

## 11. Outcome / Prognosis

- **Survival/life expectancy:** generally **normal** with trauma avoidance and antifibrinolytic management; mortality is driven only by severe unprovoked events (e.g., intracranial hemorrhage after head trauma). No disease‑specific mortality rate is established.
- **Morbidity:** episodic bleeding, iron‑deficiency anemia from menorrhagia, procedural/obstetric bleeding risk. Long‑term, absolute deficiency is associated with **cardiac fibrosis** (potential arrhythmia/cardiomyopathy risk; Khan 2021, PMID 33439236).
- **Recovery:** bleeds resolve with antifibrinolytic therapy; the underlying trait is permanent.
- **Prognostic factors:** completeness of deficiency (absolute vs partial), access to antifibrinolytic prophylaxis, and exposure to hemostatic challenges. Reduced PAI‑1 is paradoxically associated with favorable metabolic/aging markers (Khan 2017, PMID 29152572).
- **Prognostic biomarkers:** PAI‑1 antigen/activity (deficiency confirmation); cardiac MRI late gadolinium enhancement (fibrosis burden).

---

## 12. Treatment

- **Pharmacotherapy — first line:** **antifibrinolytic lysine analogues**: **tranexamic acid** (NCIT:C835; CHEBI:48669) and **ε‑aminocaproic acid** (NCIT:C28987; CHEBI:28402). They competitively block plasminogen's lysine‑binding to fibrin, stabilizing clots, and are effective both to **treat** and **prevent (peri‑procedural prophylaxis)** bleeding (Fay 1997, PMID 9207454; Jain & Acharya 2019, PMID 31427261). Documented peri‑operative regimens for dental/oral surgery (Morimoto 2004, PMID 15357795; Kajihara 2003, PMID 12632627; Tanimura 1994, PMID 8015955).
- **Pharmacogenomics:** none specific.
- **Advanced/experimental therapeutics:** **PAI‑1 mRNA lipid‑nanoparticle replacement** restores circulating PAI‑1 in preclinical models (Ferraresso et al. 2025, PMID 40917690) — a mechanism‑directed future therapy. No approved gene therapy, cell therapy, siRNA/ASO, or monoclonal antibody for this indication. Recombinant/plasma‑derived PAI‑1 is not a standard product.
- **Supportive/interventional:** local hemostatic measures, iron supplementation/transfusion for anemia, hormonal management of menorrhagia (combined with tranexamic acid), and careful peri‑operative/obstetric planning.
- **Treatment outcomes:** most bleeding events are controlled with antifibrinolytics (Mehta & Shapiro 2008, PMID 19141166). Adverse effects of antifibrinolytics: GI upset, and theoretical thrombosis risk (low in this deficiency context).
- **Strategy/personalization:** genotype‑confirmed deficiency → lifelong plan of **antifibrinolytic prophylaxis around hemostatic challenges**, trauma precautions, and (where relevant) cardiac surveillance. NCIT intervention terms: Tranexamic Acid (C835), Aminocaproic Acid (C28987), Antifibrinolytic Agent (C77096).

---

## 13. Prevention

- **Primary prevention:** not preventable (germline). **Preconception genetic counseling** and **carrier/cascade screening** in founder families reduce recurrence; prenatal/preimplantation genetic testing available.
- **Secondary prevention:** early molecular diagnosis in bleeders with normal routine coagulation tests; identification of at‑risk relatives.
- **Tertiary prevention (complication avoidance):** **peri‑procedural and menstrual antifibrinolytic prophylaxis**, trauma avoidance/contact‑sport counseling, iron repletion, obstetric planning, and cardiac monitoring for fibrosis.
- **Immunization / public‑health / environmental measures:** not applicable.
- **Counseling:** autosomal‑recessive recurrence risk (25% for carrier×carrier couples); explain asymptomatic carrier status and provocation‑dependent bleeding.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** human **SERPINE1** (Gene 5054) is conserved; mouse **Serpine1** (Gene 18787; *Mus musculus*, **NCBI Taxon 10090**), rat Serpine1 (Rattus norvegicus, Taxon 10116). Orthologs exist across vertebrates.
- **Natural disease in animals:** no well‑established spontaneous congenital PAI‑1‑deficiency disease is cataloged in companion animals (not a recognized OMIA entry); knowledge derives from engineered models rather than natural disease.
- **Comparative biology:** mechanism (serpin inhibition of tPA/uPA → fibrinolysis control) is evolutionarily conserved. A key **species difference**: mouse knockouts have mild hyperfibrinolysis and thrombosis resistance **without impaired baseline hemostasis**, whereas humans show provoked/delayed bleeding (Lijnen 1996, PMID 8739849).
- **Transmission / zoonosis:** not applicable.

---

## 15. Model Organisms

- **Mouse (primary model):** constitutive **Serpine1‑knockout** mice are viable and fertile; they display a **mild hyperfibrinolytic state and resistance to venous/arterial thrombosis without impaired hemostasis** (Lijnen 1996, PMID 8739849; Wu & Zhao 2002, PMID 12769655). Disease‑relevant bleeding phenotypes are **challenge‑dependent**:
  - Neonatal (postnatal day 3–5) PAI‑1‑/‑ pups develop **intracerebral hemorrhage** after minor trauma, modeling age‑windowed vascular vulnerability (Leroux et al. 2014, PMID 24709679).
  - Angiotensin II or norepinephrine infusion causes **epicardial hemorrhage then posterior‑septal cardiac fibrosis** in PAI‑1‑/‑ hearts (Pettey et al. 2025, PMID 41332700/42946663), recapitulating the human cardiac‑fibrosis association.
- **In vitro / cellular models:** CRISPR/Cas9 **PAI‑1‑knockout human endothelial cells** (markedly increased plasmin generation; disordered migration, reversed by aprotinin/recombinant PAI‑1/EACA; Sano et al. 2026, PMID 42946217) and patient‑derived **iPSC‑cardiomyocytes** (Khan 2021, PMID 33439236).
- **Genetic model types available:** constitutive knockout; transgenic PAI‑1‑overexpressing mice (opposite, pro‑thrombotic phenotype) as comparators; cellular CRISPR knockouts and iPSC lines.
- **Phenotype recapitulation & limitations:** models capture the **hyperfibrinolysis/anti‑thrombotic axis** and, under stress, the **hemorrhage→fibrosis** branch; the main limitation is that mice **do not spontaneously bleed at baseline**, underscoring species differences in hemostatic reserve.
- **Resources:** MGI (Serpine1), IMPC/IMSR for knockout strains.

---

## Key Supported vs. Refuted Hypotheses

**Supported:**
- SERPINE1 biallelic null variants cause complete PAI‑1 deficiency (frameshift c.699_700dupTA) → autosomal‑recessive bleeding (Fay 1997; Khan 2021).
- Mechanism is hyperfibrinolysis from unopposed tPA/uPA → excess plasmin → premature clot lysis (Jain & Acharya 2019; Sano 2026).
- Antifibrinolytics are effective first‑line therapy (Fay 1997; multiple case reports).
- Chronic absolute deficiency is associated with cardiac fibrosis (Khan 2021; mouse models).
- PAI‑1 loss has protective pleiotropy in senescence/metabolism/longevity (Khan 2017).

**Refuted / not supported:**
- Heterozygous carriers do **not** have a clinically significant bleeding disorder (Fay 1997).
- Spontaneous (unprovoked) major bleeding is **not** typical, unlike in procoagulant factor deficiencies (Mehta & Shapiro 2008).
- Mouse baseline hemostasis is **not** impaired by PAI‑1 loss (contrasts with humans) (Lijnen 1996).

## Limitations and Future Directions
- **Rarity** limits prevalence estimates, genotype–phenotype breadth, and controlled treatment data; most evidence is from one founder kindred and small case series.
- **Assay limitations** (PAI‑1 activity insensitive at low range) make molecular confirmation essential.
- Open questions: natural history and management of the **cardiac‑fibrosis** complication; clinical translation of **PAI‑1 mRNA‑LNP replacement**; and whether partial/quantitative deficiencies cause milder, under‑recognized bleeding.

---
*Evidence types: human clinical (Fay 1997; Khan 2017/2021; Mehta & Shapiro 2008; case reports), reviews (Jain & Acharya 2019; Mehta & Shapiro 2008), model organism (Lijnen 1996; Leroux 2014; Pettey 2025; Wu & Zhao 2002), in vitro (Sano 2026; Ferraresso 2025), structural/computational (Sharp 1999; Kihn 2022).*


## Artifacts

- [OpenScientist final report](Congenital_Plasminogen_Activator_Inhibitor_Type_1_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Plasminogen_Activator_Inhibitor_Type_1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 15 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000115` (2 mentions) - the report calls it "endothelium", "Tissue/cell level:** vascular **endothelium"; CL calls it **endothelial cell**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011891` (1 mention) - the report calls it "Postpartum hemorrhage"; HP calls it **Post-partum hemorrhage**
- `HP:0001637` (1 mention) - the report calls it "Abnormal myocardium/fibrosis"; HP calls it **Abnormal myocardium morphology**
- `GO:0004867` (1 mention) - the report calls it "GO terms:* serine‑type endopeptidase inhibitor activity"; GO calls it **serine-type endopeptidase inhibitor activity**
- `GO:0005615` (1 mention) - the report calls it "extracellular space"; GO calls it **obsolete extracellular space**, and lists "intercellular space" among its other names
- `GO:0031093` (1 mention) - the report calls it "secretory (α‑)granules"; GO calls it **platelet alpha granule lumen**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000115` - called "endothelium", "Tissue/cell level:** vascular **endothelium"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.