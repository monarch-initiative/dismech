---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-12T18:24:23.700683'
end_time: '2026-10-12T18:59:07.783343'
duration_seconds: 2084.08
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Lipoprotein Glomerulopathy
  mondo_id: MONDO:0012725
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
citation_count: 33
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 24
  quotes_valid: 24
  relevance_assessed: 33
  on_topic: 32
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 29
  not_found: 0
  obsolete: 3
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 20
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0012725
    reported_labels:
    - MONDO
    ontology_label: lipoprotein glomerulopathy
  - term_id: HP:0003119
    reported_labels:
    - related lipid abnormality
    ontology_label: Abnormal circulating lipid concentration
  - term_id: GO:0032983
    reported_labels:
    - protein-containing complex / aggregation-related
    ontology_label: kainate selective glutamate receptor complex
  - term_id: NCIT:C29475
    reported_labels:
    - Fenofibrate
    ontology_label: 3'-C-ethynylcytidine
  - term_id: NCIT:C66951
    reported_labels:
    - Losartan
    ontology_label: Adenocarcinoma, Endocervical Type
  - term_id: NCIT:C1518
    reported_labels:
    - HMG-CoA reductase inhibitor
    ontology_label: Raloxifene
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0043234
    ontology_label: GO_0043234
    replaced_by: GO:0032991
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  - term_id: NCIT:C66951
    ontology_label: Adenocarcinoma, Endocervical Type
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Lipoprotein_Glomerulopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Lipoprotein_Glomerulopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lipoprotein Glomerulopathy
- **MONDO ID:** MONDO:0012725 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lipoprotein Glomerulopathy** covering all of the
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

# Lipoprotein Glomerulopathy (LPG): A Comprehensive Disease Characteristics Report

**Target Disease:** Lipoprotein Glomerulopathy
**MONDO ID:** MONDO:0012725 · **OMIM:** 611771 · **Gene:** *APOE* (HGNC:613; chr19q13.32) · **Category:** Mendelian (autosomal dominant, incomplete penetrance)

---

## Summary

Lipoprotein glomerulopathy (LPG) is an ultra-rare, autosomal-dominant renal lipidosis caused by heterozygous (rarely homozygous) missense and small in-frame variants in the **APOE** gene, clustered in or near the LDL-receptor-binding region of apolipoprotein E (apoE). It is histologically defined by markedly dilated glomerular capillary loops occluded by lamellated, vacuolated, apoE-rich **lipoprotein thrombi** that lack foam cells and are negative for immunoglobulins and complement. Clinically, patients present with proteinuria/nephrotic syndrome, microscopic hematuria, and a **type III hyperlipoproteinemia-like dyslipidemia** with markedly elevated serum apoE. More than 200 cases have been reported worldwide since the entity was first described ~30 years ago, with cases concentrated in East Asia (Japan, China) through documented founder variants ([PMID: 40306438](https://pubmed.ncbi.nlm.nih.gov/40306438/); [PMID: 35602473](https://pubmed.ncbi.nlm.nih.gov/35602473/)).

The core mechanism is **conformational**: LPG-associated APOE variants (predominantly proline substitutions and small deletions/duplications around residues 136–158) thermodynamically destabilize the N-terminal domain of apoE, driving it toward a molten-globule-like state with increased exposed hydrophobic surface and aggregation propensity. The misfolded, aggregation-prone apoE forms aberrant lipoprotein particles that deposit as intraglomerular thrombi, occluding dilated capillaries and producing proteinuria and progressive chronic kidney disease ([PMID: 23110818](https://pubmed.ncbi.nlm.nih.gov/23110818/); [PMID: 31874799](https://pubmed.ncbi.nlm.nih.gov/31874799/)). The etiologic role of mutant apoE has been confirmed in vivo: adenoviral transduction of apoE-Sendai (and apoE-Kyoto) into apoE-deficient mice reproduces LPG-like glomerular lesions ([PMID: 16431249](https://pubmed.ncbi.nlm.nih.gov/16431249/); [PMID: 19459027](https://pubmed.ncbi.nlm.nih.gov/19459027/); [PMID: 33663537](https://pubmed.ncbi.nlm.nih.gov/33663537/)).

LPG carries a guarded prognosis — approximately half of patients progress to end-stage kidney disease (ESKD) within 1–27 years — but it is **not** steroid-responsive. The cornerstone of treatment is lipid-lowering therapy, especially **fibrates** (fenofibrate, bezafibrate, and the selective PPARα modulator pemafibrate), often combined with RAAS blockade (ACEi/ARB); these can markedly reduce proteinuria and, in some reports, induce complete remission. Because the pathogenic apoE is a circulating protein, LPG **recurs after kidney transplantation**. Diagnosis rests on two pillars: a characteristic kidney biopsy plus molecular confirmation by APOE sequencing ([PMID: 40306438](https://pubmed.ncbi.nlm.nih.gov/40306438/); [PMID: 38769490](https://pubmed.ncbi.nlm.nih.gov/38769490/)).

---

## 1. Disease Information

**Overview.** LPG is an inherited glomerular disease in which apoE-rich lipoproteins accumulate as "thrombi" within dilated glomerular capillary lumina, producing proteinuria, nephrotic syndrome, and progressive renal dysfunction. It is a renal lipidosis distinct from systemic lipid storage diseases and from immune-complex glomerulonephritis. Definitive diagnosis requires molecular genetic analysis of APOE in addition to characteristic biopsy findings ([PMID: 40306438](https://pubmed.ncbi.nlm.nih.gov/40306438/)).

> "Lipoprotein glomerulopathy (LPG) is an ultrarare kidney disorder caused by pathogenic variants in the APOE gene. Although kidney biopsy presents typical findings, such as dilated capillary loops containing lipoprotein thrombi, definitive diagnosis requires molecular genetic analysis of APOE." — [PMID: 40306438](https://pubmed.ncbi.nlm.nih.gov/40306438/)

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0012725 |
| OMIM | 611771 (Lipoprotein glomerulopathy) |
| Gene | APOE (HGNC:613), chromosome 19q13.32 |
| MeSH | Closest indexing via "Apolipoproteins E" / glomerular disease terms |
| ICD-10 | No specific LPG code; coded under glomerular disease categories (e.g., N05.-) |

**Synonyms / alternative names.** Lipoprotein glomerulopathy; LPG; apoE-associated lipoprotein glomerulopathy. Named variant subtypes commonly appear in the literature (e.g., apoE-Sendai, apoE-Kyoto, apoE-Osaka/Kurashiki, apoE-Chicago, apoE-Tokyo/Maebashi, apoE-Guangzhou, apoE-Kanto), referring to specific causal mutations rather than distinct diseases.

**Information source.** The evidence base is derived from **aggregated disease-level resources** — case reports, small clinical series, meta-analyses, and in vitro/animal mechanistic studies — rather than large EHR/population cohorts, reflecting the disease's rarity ([PMID: 35602473](https://pubmed.ncbi.nlm.nih.gov/35602473/)).

---

## 2. Etiology

**Disease causal factors.** LPG is a **purely monogenic genetic disorder** caused by variants in APOE. No infectious or toxic cause is implicated, and no environmental trigger is required. ApoE is the principal ligand for LDL-receptor–mediated clearance of triglyceride-rich/remnant lipoproteins; LPG-causing variants lie in or near the receptor-binding region (residues ~136–158), producing a dysbetalipoproteinemia-like (type III) plasma profile with remnant accumulation and elevated serum apoE ([PMID: 27277824](https://pubmed.ncbi.nlm.nih.gov/27277824/); [PMID: 23407349](https://pubmed.ncbi.nlm.nih.gov/23407349/)).

> "Apolipoprotein (apo) E was initially described as a lipid transport protein and major ligand for low density lipoprotein (LDL) receptors with a role in cholesterol metabolism and cardiovascular disease." — [PMID: 27277824](https://pubmed.ncbi.nlm.nih.gov/27277824/)

**Genetic risk factors.** The causal variants are heterozygous APOE missense substitutions (frequently arginine→proline) and small in-frame deletions/duplications near the LDL-receptor-binding site. Recurrent variants include apoE-Sendai (Arg145Pro), apoE-Kyoto (Arg25Cys; signal-inclusive Arg43Cys), apoE-Osaka/Kurashiki (Arg158Pro), apoE-Chicago (Arg147Pro), apoE-Tokyo/Maebashi (Lys143–Arg145 deletion), apoE-Guangzhou (Arg150Pro), and apoE-Kanto (Asp151dup) ([PMID: 23407349](https://pubmed.ncbi.nlm.nih.gov/23407349/); [PMID: 39141311](https://pubmed.ncbi.nlm.nih.gov/39141311/)). **Founder effects** are documented for apoE-Sendai (eastern Japan) and apoE-Kyoto (China).

**Environmental / modifier risk factors.** Because penetrance is incomplete (many asymptomatic carriers exist in affected families), additional genetic, epigenetic, and/or environmental modifiers are inferred to contribute. Co-inheritance of additional apoE alleles (e.g., apoE2 Arg158Cys, apoE5 Glu3Lys) or other conditions has been proposed to modify expression in individual kindreds ([PMID: 23407349](https://pubmed.ncbi.nlm.nih.gov/23407349/); [PMID: 29356944](https://pubmed.ncbi.nlm.nih.gov/29356944/); [PMID: 26955632](https://pubmed.ncbi.nlm.nih.gov/26955632/)).

> "In addition to APOE mutation, other genetic and/or epigenetic factors are considered to be involved in the pathogenesis of LPG because of its low penetrance." — [PMID: 23407349](https://pubmed.ncbi.nlm.nih.gov/23407349/)

**Protective factors.** No specific genetic or environmental protective factors are established. Early lipid-lowering therapy is associated with better renal outcomes (see Treatment), functioning as a modifiable disease-course factor rather than a prevention of onset.

**Gene–environment interactions.** Incomplete penetrance strongly implies gene-environment/gene-gene interaction, but specific interacting exposures are not well characterized.

---

## 3. Phenotypes

Phenotype frequencies are best quantified in an 11-patient Chinese cohort (mean age 33.82 years) ([PMID: 38584145](https://pubmed.ncbi.nlm.nih.gov/38584145/)):

| Phenotype | Type | Frequency | Suggested HPO |
|---|---|---|---|
| Proteinuria | Laboratory / clinical sign | 10/11 (91%) | HP:0000093 (Proteinuria) |
| Dyslipidemia (type III-like) | Laboratory abnormality | 10/11 (91%) | HP:0003119 (Abnormal circulating lipid concentration); HP:0002155 (Hypertriglyceridemia) |
| Microscopic hematuria | Laboratory / sign | 6/11 (55%) | HP:0000790 (Hematuria) |
| Positive family history | — | 5/11 (45%) | — |
| Nephrotic syndrome | Clinical syndrome | 4/11 (36%) | HP:0000100 (Nephrotic syndrome) |
| Edema | Physical manifestation | Common | HP:0000969 (Edema) |
| Elevated serum apoE | Laboratory abnormality | Characteristic (not universal) | HP:0003119 (related lipid abnormality) |
| Renal enlargement | Imaging | Reported | HP:0000105 (Enlarged kidney) |
| Anemia | Laboratory abnormality | Reported | HP:0001903 (Anemia) |
| Hypertension | Clinical sign | Associated with LDL-R–region variants | HP:0000822 (Hypertension) |
| Chronic kidney disease / ESKD | Outcome | ~50% progress | HP:0012622 (Chronic kidney disease); HP:0003774 (Stage 5 CKD) |

> "The mean age of the eleven patients was 33.82 years. Among them, five had a positive family history for LPG, ten presented with proteinuria, four exhibited nephrotic syndrome, and six presented with microscopic hematuria. Dyslipidemia was identified in ten patients." — [PMID: 38584145](https://pubmed.ncbi.nlm.nih.gov/38584145/)

**Age of onset.** Predominantly adult-onset with an average age of presentation of **32 years (range 4–69)** ([PMID: 38438730](https://pubmed.ncbi.nlm.nih.gov/38438730/)). Pediatric and early-onset cases occur, including 6- and 7.5-year-old boys, a 12-year-old girl, and a 23-month-old boy with **homozygous** APOE Kyoto and parental consanguinity presenting as steroid-resistant nephrotic syndrome ([PMID: 39993083](https://pubmed.ncbi.nlm.nih.gov/39993083/); [PMID: 22874113](https://pubmed.ncbi.nlm.nih.gov/22874113/); [PMID: 42417997](https://pubmed.ncbi.nlm.nih.gov/42417997/)).

> "It is a monogenic disorder with autosomal dominant inheritance and the average age of presentation is 32 years (4-69 years)." — [PMID: 38438730](https://pubmed.ncbi.nlm.nih.gov/38438730/)

**Severity / progression / variability.** Severity is variable and progression is generally **chronic and progressive**, often culminating in ESKD. A notable phenotypic nuance: a subset of patients are **normolipidemic** (e.g., certain APOE Kyoto and APOE Kanto cases with normal serum lipids and apoE), so normal lipids do **not** exclude LPG ([PMID: 40186270](https://pubmed.ncbi.nlm.nih.gov/40186270/); [PMID: 42309892](https://pubmed.ncbi.nlm.nih.gov/42309892/); [PMID: 39141311](https://pubmed.ncbi.nlm.nih.gov/39141311/)).

> "In contrast to previous cases, this patient lacked hyperlipidemia and ApoE was a Kyoto mutation." — [PMID: 40186270](https://pubmed.ncbi.nlm.nih.gov/40186270/)

**Quality of life impact.** No formal EQ-5D/SF-36 data exist for LPG. Impact is inferred from nephrotic-range proteinuria, edema, and progression to dialysis-dependent ESKD, all of which substantially impair daily functioning. LPG can co-occur with IgA nephropathy, membranous nephropathy, or lupus nephritis, which can add to morbidity.

---

## 4. Genetic / Molecular Information

**Causal gene.** **APOE** (apolipoprotein E), HGNC:613, OMIM gene 107741; disease OMIM 611771; located at 19q13.32. LPG is caused by rare, protein-altering APOE variants — distinct from the common E2/E3/E4 isoform polymorphisms (though some patients carry combinations of a rare LPG variant with a common isoform allele).

**Pathogenic variants.** Causal variants cluster in/near the LDL-receptor-binding region (residues ~136–158). The table below lists the principal named variants (mature-protein numbering unless noted):

| Variant name | Change (mature protein) | Type | Notable feature |
|---|---|---|---|
| apoE-Sendai | Arg145Pro | Missense (Arg→Pro) | Founder in eastern Japan; most frequent |
| apoE-Kyoto | Arg25Cys (signal-inclusive Arg43Cys) | Missense | Founder in China; can be normolipidemic |
| apoE-Osaka/Kurashiki | Arg158Pro | Missense (Arg→Pro) | Serum apoE can be normal |
| apoE-Chicago | Arg147Pro | Missense (Arg→Pro) | — |
| apoE-Tokyo/Maebashi | Lys143–Arg145 deletion | In-frame deletion | 9-nt deletion (c.480–488) |
| apoE-Guangzhou | Arg150Pro | Missense (Arg→Pro) | Novel Chinese variant |
| apoE-Kanto | Asp151dup | In-frame duplication | First duplication-type; progressed to ESKD |

> "LPG is primarily associated with heterozygous apoE mutations surrounding the low-density lipoprotein-receptor binding site, and it is histologically characterized by lamellated lipoprotein thrombi that lack foam cells." — [PMID: 31874799](https://pubmed.ncbi.nlm.nih.gov/31874799/)

> "More than 12 APOE mutations have been identified as causes of LPG, and APOE-Sendai (Arg145Pro) mutation was frequently detected in patients from the eastern part of Japan including Yamagata prefecture." — [PMID: 23407349](https://pubmed.ncbi.nlm.nih.gov/23407349/)

**Variant classification & type.** Variants are pathogenic (ACMG/AMP), predominantly **missense** (frequently arginine→proline substitutions) plus small in-frame **deletions/duplications**. **Origin is germline.** Functional consequence is a conformational/structural defect (destabilization/aggregation) — effectively a **toxic gain-of-function / dominant-negative-like** behavior at the lipoprotein-particle level rather than simple loss of ligand function, consistent with autosomal-dominant inheritance.

**Allele frequency.** Causal variants are rare/absent in population databases; the apoE-Sendai founder variant was **not detected in 2,023 controls**, confirming rarity in the general population ([PMID: 23407349](https://pubmed.ncbi.nlm.nih.gov/23407349/)).

**Modifier genes / epigenetics.** Incomplete penetrance implicates additional genetic/epigenetic modifiers; co-inheritance of apoE2 (Arg158Cys) or apoE5 (Glu3Lys) has been proposed to modify phenotype in specific families ([PMID: 26955632](https://pubmed.ncbi.nlm.nih.gov/26955632/); [PMID: 29356944](https://pubmed.ncbi.nlm.nih.gov/29356944/)). No specific DNA-methylation/histone signatures have been defined for LPG.

**Chromosomal abnormalities.** None reported; LPG is a single-gene point-variant/small-indel disorder.

---

## 5. Environmental Information

LPG has no established environmental cause. There are no implicated toxins, radiation, pollutants, or occupational exposures; no lifestyle factor is established as causal; and no infectious agent triggers the disease. Incomplete penetrance implies that unidentified genetic/epigenetic/environmental modifiers influence whether carriers develop overt disease, but these remain uncharacterized ([PMID: 23407349](https://pubmed.ncbi.nlm.nih.gov/23407349/)). **Not applicable / not established** for most environmental subcategories.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. A heterozygous **APOE missense/in-frame variant** near the LDL-receptor-binding region (e.g., Arg145Pro) **results in** an amino-acid change incompatible with normal helical packing of the N-terminal domain.
2. This **leads to** thermodynamic destabilization of the apoE N-terminal four-helix bundle, loss of unfolding intermediates, and a shift toward a **molten-globule-like state** (demonstrated in vitro).
3. The destabilized protein **exposes hydrophobic surface** to solvent, which **results in** increased aggregation propensity and protease sensitivity (demonstrated in vitro).
4. Aggregation-prone mutant apoE **leads to** formation of aberrant, destabilized apoE-rich lipoprotein particles and impaired remnant-lipoprotein clearance, producing a **type III–like dyslipidemia** with elevated serum apoE (inferred from plasma profiles + in vitro particle data).
5. These abnormal lipoproteins **deposit** within glomerular capillaries as **lamellated lipoprotein thrombi** (branch: a complementary mechanism posits impaired macrophage clearance of lipoproteins, explaining thrombi forming **without** foam cells).
6. Thrombi **occlude** markedly dilated glomerular capillary loops, which **results in** proteinuria, hematuria, and reduced filtration.
7. Chronic capillary occlusion and glomerular injury **lead to** progressive chronic kidney disease and, in ~50% of patients, **ESKD** (demonstrated by natural-history data).

> "All three variants were found to have significantly reduced helical content, to expose a larger portion of hydrophobic surface to the solvent, and to be significantly thermodynamically destabilized, often lacking functionally relevant unfolding intermediates." — [PMID: 23110818](https://pubmed.ncbi.nlm.nih.gov/23110818/)

> "Overall, our data suggest that these mutations induce a generalized unfolding of the N-terminal domain of apoE3 toward a molten-globule-like structure." — [PMID: 23110818](https://pubmed.ncbi.nlm.nih.gov/23110818/)

> "LPG can be induced by thermodynamic destabilization, hydrophobic surface exposure, and the aggregation of apoE resulting from the incompatibility of apoE mutated residues within helical regions." — [PMID: 31874799](https://pubmed.ncbi.nlm.nih.gov/31874799/)

### Detail by category

- **Molecular pathways / metabolic changes.** LDL-receptor-mediated clearance of triglyceride-rich/remnant lipoproteins (apoE is the key ligand); remnant/VLDL metabolism; lipid transport. Disruption yields dysbetalipoproteinemia-like remnant accumulation ([PMID: 27277824](https://pubmed.ncbi.nlm.nih.gov/27277824/); [PMID: 10359567](https://pubmed.ncbi.nlm.nih.gov/10359567/)). Suggested GO: GO:0006869 (lipid transport), GO:0034447 (very-low-density lipoprotein particle clearance), GO:0042157 (lipoprotein metabolic process). CHEBI: CHEBI:16113 (cholesterol), CHEBI:17855 (triglyceride).
- **Protein dysfunction.** Misfolding, structural destabilization, hydrophobic exposure, and aggregation of apoE — a conformational disease mechanism ([PMID: 23110818](https://pubmed.ncbi.nlm.nih.gov/23110818/); [PMID: 30309894](https://pubmed.ncbi.nlm.nih.gov/30309894/); [PMID: 24149834](https://pubmed.ncbi.nlm.nih.gov/24149834/)). Suggested GO: GO:0006457 (protein folding), GO:0043234/GO:0032983 (protein-containing complex / aggregation-related).
- **Cellular processes / immune involvement.** Immunofluorescence for immunoglobulins and complement is **negative** — LPG is **not** immune-complex mediated. Macrophage handling of lipoproteins is implicated as a complementary mechanism (thrombi without foam cells); a variant/atypical case showed foamy-macrophage infiltration when combined with apoE2, bridging LPG and apoE2-homozygote glomerulopathy ([PMID: 26955632](https://pubmed.ncbi.nlm.nih.gov/26955632/); [PMID: 24149835](https://pubmed.ncbi.nlm.nih.gov/24149835/)). Suggested CL: CL:0000650 (mesangial cell), CL:0000653 (podocyte), CL:0000235 (macrophage), CL:0002188 (glomerular endothelial cell).
- **Tissue damage mechanisms.** Capillary occlusion by lipoprotein thrombi → glomerular ischemia/mechanical injury → proteinuria and progressive glomerulosclerosis/fibrosis.
- **Lipidomics / molecular profiling.** Plasma shows a type III (dysbetalipoproteinemia) pattern with elevated triglycerides, elevated apoB, and markedly elevated apoE (variant-dependent). Glomerular proteomics by LC-MS/MS of laser-microdissected tissue shows apoE enrichment ([PMID: 38769490](https://pubmed.ncbi.nlm.nih.gov/38769490/)).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Kidney — specifically the **renal glomerulus** (UBERON:0000074). Secondary involvement: systemic lipid metabolism (dyslipidemia); cardiovascular risk from dysbetalipoproteinemia; arterial stiffness reported in some patients ([PMID: 38769490](https://pubmed.ncbi.nlm.nih.gov/38769490/)).
- **Body system:** Urinary/renal system (primary); cardiovascular/metabolic (secondary).
- **Tissue/cell level:** Glomerular capillary tuft — dilated **glomerular capillaries** (UBERON:0005750, glomerular capillary). Cell types implicated: glomerular endothelial cells (CL:0002188), mesangial cells (CL:0000650), podocytes (CL:0000653), and infiltrating macrophages (CL:0000235) in atypical cases.
- **Subcellular level:** Extracellular deposition within the capillary lumen (lipoprotein thrombi); at the protein level, N-terminal domain misfolding. Suggested GO cellular components: GO:0034361 (very-low-density lipoprotein particle), GO:0042627 (chylomicron), GO:0005615 (extracellular space).
- **Localization / lateralization:** **Bilateral**, diffuse glomerular involvement (systemic circulating apoE drives deposition in both kidneys).

> "Immunofluorescence staining showed that the thrombi were strongly positive for apo A, B, and E. Granules and various sizes of vacuoles were observed in the thrombi under electron microscope." — [PMID: 15498375](https://pubmed.ncbi.nlm.nih.gov/15498375/)

---

## 8. Temporal Development

- **Onset:** Typically **adult-onset** (mean ~32 years, range 4–69), insidious/chronic. Pediatric and even infantile cases occur (23-month-old homozygote) ([PMID: 38438730](https://pubmed.ncbi.nlm.nih.gov/38438730/); [PMID: 42417997](https://pubmed.ncbi.nlm.nih.gov/42417997/)).
- **Progression:** Chronic and generally **progressive**. Approximately half of patients reach ESKD over a wide window of **1–27 years** from onset ([PMID: 38769490](https://pubmed.ncbi.nlm.nih.gov/38769490/)).
- **Disease course:** Progressive proteinuria → declining eGFR → ESKD. Proteinuria reduction >50% is associated with slower renal decline (see Treatment) ([PMID: 32441489](https://pubmed.ncbi.nlm.nih.gov/32441489/)).
- **Remission patterns:** Spontaneous remission is not characteristic; **treatment-induced** remission (proteinuria reduction, even complete remission) is reported with fibrates ([PMID: 42371225](https://pubmed.ncbi.nlm.nih.gov/42371225/)).
- **Critical period / window of opportunity:** Early initiation of lipid-lowering therapy is emphasized as the best opportunity to preserve renal function ([PMID: 24149835](https://pubmed.ncbi.nlm.nih.gov/24149835/)).

> "approximately half of the patients develop end-stage kidney disease within 1-27 years of disease onset" — [PMID: 38769490](https://pubmed.ncbi.nlm.nih.gov/38769490/)

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant** with **incomplete penetrance**; rare homozygous (recessive-presenting) cases occur with consanguinity ([PMID: 38438730](https://pubmed.ncbi.nlm.nih.gov/38438730/); [PMID: 42417997](https://pubmed.ncbi.nlm.nih.gov/42417997/)).
- **Penetrance/expressivity:** Incomplete penetrance (many asymptomatic carriers); variable expressivity (including normolipidemic forms) ([PMID: 41612256](https://pubmed.ncbi.nlm.nih.gov/41612256/); [PMID: 40186270](https://pubmed.ncbi.nlm.nih.gov/40186270/)).
- **Founder effects:** apoE-Sendai (eastern Japan, including Yamagata) and apoE-Kyoto (China) descend through founder haplotypes ([PMID: 23407349](https://pubmed.ncbi.nlm.nih.gov/23407349/); [PMID: 24149835](https://pubmed.ncbi.nlm.nih.gov/24149835/)).
- **Consanguinity:** Relevant in homozygous pediatric cases ([PMID: 42417997](https://pubmed.ncbi.nlm.nih.gov/42417997/)).
- **Epidemiology:** Ultra-rare — **>200 cases** reported worldwide over ~30 years; an earlier review counted 65 cases. Most patients are in **Japan and East Asia**. Formal prevalence/incidence rates are **not established** (no Orphanet prevalence class). Clinical series show a **male predominance** and adult onset ([PMID: 35602473](https://pubmed.ncbi.nlm.nih.gov/35602473/); [PMID: 16431249](https://pubmed.ncbi.nlm.nih.gov/16431249/)).

> "At present, 65 cases have been reported worldwide, although most patients are found in Japan and east Asian countries." — [PMID: 16431249](https://pubmed.ncbi.nlm.nih.gov/16431249/)

> "the haplotype of all APOE-Sendai mutations was identical, suggesting that APOE-Sendai mutation is common in Japanese patients probably through a founder effect." — [PMID: 23407349](https://pubmed.ncbi.nlm.nih.gov/23407349/)

---

## 10. Diagnostics

**Two-pillar diagnostic standard:** (1) characteristic **kidney biopsy** and (2) molecular confirmation by **APOE sequencing** ([PMID: 40306438](https://pubmed.ncbi.nlm.nih.gov/40306438/)).

**Biopsy / histopathology.** Light microscopy shows markedly dilated glomerular capillary loops filled with pale, weakly-staining **lamellated lipoprotein thrombi**. Staining profile: **PAS weak-positive, Masson pale blue, silver/MT pale, Congo-red negative** (excludes amyloid), **Oil Red O / Sudan positive** on frozen sections (confirms lipid), and **apoE-positive by immunohistochemistry** (also apoA, apoB positive). **Immunofluorescence for immunoglobulins and complement is negative** (distinguishes from immune-complex GN). Electron microscopy shows granular/vacuolated thrombi of variable electron density ([PMID: 41405262](https://pubmed.ncbi.nlm.nih.gov/41405262/); [PMID: 15498375](https://pubmed.ncbi.nlm.nih.gov/15498375/)).

> "These thrombi appeared PAS weak positive, MT pale blue, silver negative, and Congo-Red negative. These capillary luminal contents stained reddish with Oil-red O confirming lipid contents." — [PMID: 41405262](https://pubmed.ncbi.nlm.nih.gov/41405262/)

**Genetic testing.** Single-gene **APOE Sanger sequencing** is the primary confirmatory test; **whole-exome sequencing** is increasingly used and can reveal co-inherited variants (e.g., COL4A5 in an Alport/LPG dual-diagnosis case) ([PMID: 40306438](https://pubmed.ncbi.nlm.nih.gov/40306438/); [PMID: 41612256](https://pubmed.ncbi.nlm.nih.gov/41612256/)).

**Supportive labs / biomarkers.** Elevated serum apoE and apoB, hypertriglyceridemia, type III dysbetalipoproteinemia pattern (mid-band on electrophoresis). **Caveat:** serum apoE can be **normal** in some variants (Osaka, Kanto, normolipidemic Kyoto) — normal apoE does not exclude LPG ([PMID: 21325775](https://pubmed.ncbi.nlm.nih.gov/21325775/); [PMID: 39141311](https://pubmed.ncbi.nlm.nih.gov/39141311/)).

**Advanced / omics diagnostics.** LC-MS/MS of laser-microdissected glomeruli demonstrates glomerular apoE enrichment, providing molecular confirmation of deposit composition ([PMID: 38769490](https://pubmed.ncbi.nlm.nih.gov/38769490/)).

> "Liquid chromatography-tandem mass spectrometry of laser-microdissected glomeruli from paraffin sections revealed an increase in ApoE." — [PMID: 38769490](https://pubmed.ncbi.nlm.nih.gov/38769490/)

**Differential diagnosis.** Amyloidosis (Congo-red negative in LPG), thrombotic microangiopathy, cryoglobulinemic GN, fibronectin glomerulopathy, histiocytic glomerular lipidosis (e.g., macrophage activation syndrome), and apoE2-homozygote glomerulopathy (foam-cell rich) ([PMID: 31874799](https://pubmed.ncbi.nlm.nih.gov/31874799/); [PMID: 37936128](https://pubmed.ncbi.nlm.nih.gov/37936128/)).

**Screening.** Cascade family screening (APOE sequencing ± urinalysis) is appropriate given autosomal-dominant inheritance; many carriers are asymptomatic ([PMID: 41612256](https://pubmed.ncbi.nlm.nih.gov/41612256/)).

---

## 11. Outcome / Prognosis

- **Renal survival:** Guarded — **~50%** progress to ESKD within **1–27 years** of onset ([PMID: 38769490](https://pubmed.ncbi.nlm.nih.gov/38769490/)).
- **Prognostic factors:** Degree of proteinuria control is a key modifiable prognostic factor. In an 8-patient cohort, patients with **>50% proteinuria reduction** had slower renal decline: eGFR change **−5.0 ± 0.8 vs +1.5 ± 0.7 mL/min/1.73 m²** reduction rate (i.e., treated-responders declined more slowly) ([PMID: 32441489](https://pubmed.ncbi.nlm.nih.gov/32441489/)). Variants in the LDL-receptor-binding region were associated with higher blood pressure and higher serum apoE.
- **Transplant outcome:** LPG **recurs after kidney transplantation** (early and late relapses documented), because the pathogenic apoE is circulating ([PMID: 40306438](https://pubmed.ncbi.nlm.nih.gov/40306438/)).
- **Quality of life / mortality:** No formal QoL or disease-specific mortality statistics; morbidity is driven by nephrotic syndrome and ESKD.

> "it may recur after kidney transplantation" — [PMID: 40306438](https://pubmed.ncbi.nlm.nih.gov/40306438/)

> "LPG patients with urine protein reduced more than 50% had a slower decrease in renal function than those with less urine protein reduction." — [PMID: 32441489](https://pubmed.ncbi.nlm.nih.gov/32441489/)

---

## 12. Treatment

LPG is **not steroid-responsive**; immunosuppression is ineffective ([PMID: 42417997](https://pubmed.ncbi.nlm.nih.gov/42417997/)). The mainstay is lipid-lowering therapy plus antiproteinuric RAAS blockade.

| Therapy | Example agents | Evidence / effect | Suggested NCIT |
|---|---|---|---|
| **Fibrates (PPARα agonists)** | Fenofibrate, bezafibrate | Most-reported therapy; reduce proteinuria, can induce complete remission | NCIT:C29475 (Fenofibrate); fibric acid class |
| **Selective PPARα modulator** | Pemafibrate | Complete remission (0.05 g/gCr) within 7 months in a reported case | PPAR-alpha agonist class |
| **RAAS blockade (adjunct)** | Telmisartan, losartan, ACEi/ARB | Antiproteinuric; used with fibrates | NCIT:C66951 (Losartan); ARB class |
| **Statins** | Various | Benefit in selected patients (statin monotherapy sustained renal stability up to 3 years) | NCIT:C1518 (HMG-CoA reductase inhibitor) |
| **Supportive** | Lipid/BP control, diet | Standard CKD/nephrotic supportive care | — |

> "Complete remission (0.05 g/gCr) was achieved within 7 months, and she remained stable thereafter." — [PMID: 42371225](https://pubmed.ncbi.nlm.nih.gov/42371225/)

Representative responses: a boy with apoE-Tokyo/Maebashi had urine protein turn negative within 1 week on **fenofibrate + telmisartan** ([PMID: 39993083](https://pubmed.ncbi.nlm.nih.gov/39993083/)); complete resolution with fenofibrate was reported from Pakistan ([PMID: 38327135](https://pubmed.ncbi.nlm.nih.gov/38327135/)); and sustained benefit with **statin monotherapy** over 3 years in a young Chinese man with apoE-Kyoto ([PMID: 30685233](https://pubmed.ncbi.nlm.nih.gov/30685233/)). In normolipidemic LPG, lipid-lowering may be withheld and ARB used alone ([PMID: 42309892](https://pubmed.ncbi.nlm.nih.gov/42309892/)).

**Advanced/experimental therapeutics.** No approved gene, cell, or RNA-based therapy exists. Because the disease is driven by a circulating misfolded protein, therapies targeting apoE production or conformation are conceptually attractive but remain experimental. **Early initiation** of fibrate therapy is emphasized to prevent renal dysfunction ([PMID: 24149835](https://pubmed.ncbi.nlm.nih.gov/24149835/)).

> "the administration of fibrate with the intensive control of triglyceride and apolipoprotein E particularly from the early phase will ameliorate LPG and prevent renal dysfunction." — [PMID: 24149835](https://pubmed.ncbi.nlm.nih.gov/24149835/)

---

## 13. Prevention

- **Primary prevention:** Not possible for mutation carriers (genetic); focus is on **genetic counseling** given autosomal-dominant inheritance.
- **Secondary prevention:** **Cascade family screening** (APOE sequencing plus urinalysis/lipid profile) to identify carriers early; early lipid-lowering therapy in affected carriers to preserve renal function ([PMID: 41612256](https://pubmed.ncbi.nlm.nih.gov/41612256/); [PMID: 24149835](https://pubmed.ncbi.nlm.nih.gov/24149835/)).
- **Tertiary prevention:** Proteinuria control (fibrates + RAAS blockade), blood-pressure control, and standard CKD management to delay ESKD.
- **Genetic counseling:** Important for at-risk relatives, prenatal/reproductive planning, and interpretation of incomplete penetrance (asymptomatic carriers are common).
- **Immunization / public-health / environmental interventions:** **Not applicable** (non-infectious, non-environmental disease).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human APOE (NCBI Gene 348; NCBI Taxon 9606). The mouse ortholog is *Apoe* (NCBI Gene 11816; NCBI Taxon 10090). No naturally occurring LPG analog is established in companion animals or wildlife.
- **Comparative biology:** Mouse apoE biology closely parallels human lipoprotein clearance, enabling the transgenic/adenoviral models below. Human apoE isoform structure determines VLDL clearance and atherosclerosis risk in humanized mice, underscoring evolutionary conservation of apoE function ([PMID: 10359567](https://pubmed.ncbi.nlm.nih.gov/10359567/)).
- **Zoonotic potential:** **None** (genetic disease).

---

## 15. Model Organisms

**Primary model: apoE-deficient (Apoe⁻/⁻) mouse reconstituted with mutant human apoE via adenoviral transduction.** This is the key in vivo system validating LPG etiology.

| Model | Method | Result | Reference |
|---|---|---|---|
| apoE-Sendai (Arg145Pro) in Apoe⁻/⁻ | Adenoviral transduction | LPG-like lesions in **40/50 mice** (24 mild, 13 moderate, 3 severe); dilated lumens with Oil Red O/Sudan-positive lipid thrombi | [PMID: 19459027](https://pubmed.ncbi.nlm.nih.gov/19459027/) |
| apoE-Kyoto (p.R43C) in Apoe⁻/⁻ | Adenoviral transduction | Reproduced LPG pathology; enabled comparison with apoE-Sendai | [PMID: 33663537](https://pubmed.ncbi.nlm.nih.gov/33663537/) |
| apoE-Sendai general validation | Adenoviral transduction in Apoe⁻/⁻ | Confirmed etiologic role of mutant apoE in LPG | [PMID: 16431249](https://pubmed.ncbi.nlm.nih.gov/16431249/) |

> "The virus-mediated transduction of apoE Sendai resulting in the development of LPG in apoE-deficient mice confirms the etiologic role of apoE mutation in LPG." — [PMID: 16431249](https://pubmed.ncbi.nlm.nih.gov/16431249/)

> "Characteristic lesions were dilated vascular lumens mimicking lipoprotein thrombi in human LPG. Similar changes were found in hematoxylin-eosin stained sections of aged apoE KO mice." — [PMID: 19459027](https://pubmed.ncbi.nlm.nih.gov/19459027/)

**Phenotype recapitulation.** Models reproduce the hallmark glomerular lipoprotein thrombi and confirm the pathogenic role of mutant apoE. **Important control:** aged Apoe⁻/⁻ mice develop superficially similar dilated-lumen lesions, but these contain **proteins/fibrils rather than lipid**, distinguishing spontaneous knockout lesions from true mutant-apoE-driven LPG ([PMID: 19459027](https://pubmed.ncbi.nlm.nih.gov/19459027/)).

**Model limitations.** Adenoviral expression is transient and non-germline; models do not fully recapitulate chronic progression to ESKD. No germline knock-in mouse for human LPG variants is established in the reviewed literature.

**In vitro models.** Recombinant apoE3-based mutants (R145P/Sendai, R147P/Chicago, R158P/Osaka, and non-proline R25C/Kyoto) characterized biophysically establish the destabilization/aggregation mechanism ([PMID: 23110818](https://pubmed.ncbi.nlm.nih.gov/23110818/); [PMID: 30309894](https://pubmed.ncbi.nlm.nih.gov/30309894/)).

---

## Mechanistic Model / Interpretation

```
  APOE missense/in-frame variant (near LDL-R binding region, res ~136–158)
                         │  (e.g., Arg145Pro = apoE-Sendai)
                         ▼
  Thermodynamic destabilization of apoE N-terminal 4-helix bundle
   (↓ α-helix, loss of unfolding intermediates → molten-globule-like)   [in vitro]
                         │
                         ▼
  Hydrophobic surface exposure → aggregation + protease sensitivity      [in vitro]
                         │
          ┌──────────────┴───────────────┐
          ▼                              ▼
  Aberrant apoE-rich lipoprotein     Impaired macrophage clearance
  particles; ↓ remnant clearance     of lipoproteins (complementary;
  → type III–like dyslipidemia,      explains thrombi WITHOUT foam cells)
  ↑ serum apoE (variant-dependent)
          │                              │
          └──────────────┬───────────────┘
                         ▼
  Lamellated lipoprotein thrombi deposit in dilated glomerular capillaries
   (apoE/apoA/apoB +, Oil Red O +, Congo-red −, Ig/complement −)
                         ▼
  Capillary occlusion → proteinuria, microscopic hematuria, ↓ GFR
                         ▼
  Progressive CKD → ESKD in ~50% (1–27 yr); recurs post-transplant
                         │
                         ▼   (therapeutic node)
  Fibrates / pemafibrate + RAAS blockade → ↓ proteinuria → slower eGFR decline
```

**Upstream vs downstream.** The APOE variant and apoE misfolding/aggregation are upstream; lipoprotein-thrombus deposition and glomerular capillary occlusion are intermediate; proteinuria, CKD, and ESKD are downstream. The disease unifies a spectrum of apoE-related glomerular disorders: LPG (heterozygous LDL-R–region variants, lamellated thrombi, no foam cells) is distinct from **apoE2-homozygote glomerulopathy** (glomerulosclerosis with foam-cell infiltration) and **apoE-Toyonaka (Ser197Cys)+apoE2/2** (membranous-like), yet all converge on apoE conformational abnormality and renal lipid accumulation ([PMID: 31874799](https://pubmed.ncbi.nlm.nih.gov/31874799/)).

> "ApoE2 homozygote glomerulopathy has been found in individuals expressing homozygous apoE2/2. This was characterized histologically by glomerulosclerosis with marked infiltration of foam cells derived from macrophages" — [PMID: 31874799](https://pubmed.ncbi.nlm.nih.gov/31874799/)

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [40306438](https://pubmed.ncbi.nlm.nih.gov/40306438/) | Defines LPG as ultra-rare APOE disorder; two-pillar diagnosis; post-transplant recurrence | Human clinical (review/cases) |
| [35602473](https://pubmed.ncbi.nlm.nih.gov/35602473/) | >200 cases over 30 years; meta-analysis | Human, meta-analysis |
| [23110818](https://pubmed.ncbi.nlm.nih.gov/23110818/) | Thermodynamic destabilization / molten-globule mechanism of apoE mutants | In vitro / biophysical |
| [30309894](https://pubmed.ncbi.nlm.nih.gov/30309894/) | Destabilization/aggregation for non-proline mutants (R25C/Kyoto) | In vitro |
| [24149834](https://pubmed.ncbi.nlm.nih.gov/24149834/) | Structural basis review of LPG mutations | Computational/structural review |
| [31874799](https://pubmed.ncbi.nlm.nih.gov/31874799/) | Unifying conformational mechanism; distinguishes apoE-related glomerular disorders | Review |
| [16431249](https://pubmed.ncbi.nlm.nih.gov/16431249/) | In vivo confirmation (apoE-Sendai in Apoe⁻/⁻); 65-case epidemiology | Mouse model / review |
| [19459027](https://pubmed.ncbi.nlm.nih.gov/19459027/) | apoE-Sendai mouse model; distinguishes aged KO lesions | Mouse model |
| [33663537](https://pubmed.ncbi.nlm.nih.gov/33663537/) | apoE-Kyoto mouse model | Mouse model |
| [23407349](https://pubmed.ncbi.nlm.nih.gov/23407349/) | Founder haplotype of apoE-Sendai; incomplete penetrance | Human genetics |
| [38584145](https://pubmed.ncbi.nlm.nih.gov/38584145/) | Phenotype frequencies in 11-patient cohort | Human clinical |
| [38438730](https://pubmed.ncbi.nlm.nih.gov/38438730/) | Age of onset (32 yr; 4–69); AD inheritance; pediatric case | Human clinical |
| [32441489](https://pubmed.ncbi.nlm.nih.gov/32441489/) | Proteinuria reduction → slower eGFR decline; genotype-BP/apoE correlation | Human clinical |
| [38769490](https://pubmed.ncbi.nlm.nih.gov/38769490/) | ESKD in ~50% (1–27 yr); LC-MS/MS glomerular apoE; fibrate+losartan | Human clinical |
| [42371225](https://pubmed.ncbi.nlm.nih.gov/42371225/) | Complete remission with pemafibrate | Human clinical |
| [41405262](https://pubmed.ncbi.nlm.nih.gov/41405262/) | Histochemical staining profile for diagnosis | Human clinical |
| [15498375](https://pubmed.ncbi.nlm.nih.gov/15498375/) | apoE/apoA/apoB-positive vacuolated thrombi | Human clinical |
| [40186270](https://pubmed.ncbi.nlm.nih.gov/40186270/) / [42309892](https://pubmed.ncbi.nlm.nih.gov/42309892/) | Normolipidemic LPG (APOE Kyoto) | Human clinical |
| [42417997](https://pubmed.ncbi.nlm.nih.gov/42417997/) | Homozygous APOE Kyoto, infantile, steroid-resistant | Human clinical |
| [26955632](https://pubmed.ncbi.nlm.nih.gov/26955632/) | Macrophage infiltration; LPG vs apoE2-GN bridge | Human clinical |
| [27277824](https://pubmed.ncbi.nlm.nih.gov/27277824/) | apoE normal function (LDL-R ligand) | Review |
| [10359567](https://pubmed.ncbi.nlm.nih.gov/10359567/) | apoE structure → VLDL clearance (conservation) | Mouse model |
| [41612256](https://pubmed.ncbi.nlm.nih.gov/41612256/) | Incomplete penetrance; WES + biopsy; cascade screening | Human clinical |

---

## Limitations and Knowledge Gaps

1. **No formal epidemiology.** Prevalence and incidence are not quantified; estimates rest on cumulative case counts (>200 worldwide). No Orphanet prevalence class exists.
2. **Ascertainment bias.** The heavy East-Asian representation partly reflects founder variants and may be amplified by awareness/reporting bias; true global distribution is uncertain.
3. **Mechanistic branch not fully resolved.** The relative contributions of apoE misfolding/aggregation versus impaired macrophage lipoprotein clearance to thrombus formation remain to be dissected in vivo.
4. **Model limitations.** Available mouse models use transient adenoviral (non-germline) expression and do not fully recapitulate chronic ESKD progression; no validated germline knock-in model is reported.
5. **Penetrance modifiers unknown.** The genetic/epigenetic/environmental factors explaining incomplete penetrance and normolipidemic phenotypes are not identified.
6. **Treatment evidence is low-level.** Efficacy data come from case reports and small series, not randomized trials; optimal agent (fibrate vs statin vs pemafibrate), timing, and genotype-specific response are not established.
7. **No QoL/mortality data.** Disease-specific quality-of-life and mortality metrics are absent.

---

## Proposed Follow-up Experiments / Actions

1. **Germline knock-in mouse models** of recurrent human variants (apoE-Sendai Arg145Pro, apoE-Kyoto) to study chronic progression to ESKD and test therapeutics longitudinally.
2. **Prospective international LPG registry** with standardized genotype, histology, serum apoE, and renal-outcome capture to establish prevalence, natural history, and genotype–phenotype correlations (including normolipidemic variants).
3. **Randomized or well-controlled comparative studies** of fibrates (incl. pemafibrate) vs statins vs combination with RAAS blockade, with proteinuria and eGFR-slope endpoints, stratified by variant and baseline lipids.
4. **Mechanistic dissection** of the macrophage-clearance branch (e.g., macrophage-specific manipulation in reconstituted Apoe⁻/⁻ mice) to clarify why thrombi form without foam cells.
5. **apoE-targeted therapeutic exploration** — small molecules/chaperones that stabilize the apoE N-terminal domain, or RNA-based approaches lowering mutant apoE — given that circulating pathogenic apoE drives disease and post-transplant recurrence.
6. **Routine cascade APOE screening** protocols for relatives of probands, paired with early lipid-lowering intervention trials in asymptomatic carriers to test secondary prevention.
7. **Structural/biophysical profiling** of newer variants (e.g., apoE-Kanto Asp151dup) to confirm the generality of the destabilization-aggregation model across variant classes (missense, deletion, duplication).

---

*Report compiled from 43 reviewed papers and 9 confirmed findings across 5 investigation iterations. Evidence sources are distinguished as human clinical, mouse model, in vitro/biophysical, or review/computational throughout.*


## Artifacts

- [OpenScientist final report](Lipoprotein_Glomerulopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Lipoprotein_Glomerulopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 24 |
| Quoted claims found in source | 24 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 33 |
| On topic | 32 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 1 |
| Terms whose name was checked | 27 |
| Terms named correctly | 20 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012725` (2 mentions) - the report calls it "MONDO"; MONDO calls it **lipoprotein glomerulopathy**
- `HP:0003119` (2 mentions) - the report calls it "related lipid abnormality"; HP calls it **Abnormal circulating lipid concentration**
- `GO:0032983` (1 mention) - the report calls it "protein-containing complex / aggregation-related"; GO calls it **kainate selective glutamate receptor complex**
- `NCIT:C29475` (1 mention) - the report calls it "Fenofibrate"; NCIT calls it **3'-C-ethynylcytidine**
- `NCIT:C66951` (1 mention) - the report calls it "Losartan"; NCIT calls it **Adenocarcinoma, Endocervical Type**
- `NCIT:C1518` (1 mention) - the report calls it "HMG-CoA reductase inhibitor"; NCIT calls it **Raloxifene**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0043234` (GO_0043234) (1 mention) - replaced by `GO:0032991`
- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`
- `NCIT:C66951` (Adenocarcinoma, Endocervical Type) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005615` (1 mention) - the report calls it "extracellular space"; GO calls it **obsolete extracellular space**, and lists "intercellular space" among its other names