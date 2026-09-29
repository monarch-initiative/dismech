---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T14:38:08.612190'
end_time: '2026-09-07T14:52:57.760848'
duration_seconds: 889.15
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intermittent Explosive Disorder
  mondo_id: MONDO:0001521
  category: Psychiatric
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
  relevance_assessed: 33
  on_topic: 26
  validator_version: 0.2.1
term_validation:
  total_terms: 27
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 10
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0000718
    reported_labels:
    - Aggressive behavior
    - Frequent (DSM-5 low-threshold criterion)
    - Subset (high-severity subtype)
    ontology_label: Aggressive behavior
  - term_id: HP:0000752
    reported_labels:
    - Behavioral abnormality
    ontology_label: Hyperactivity
  - term_id: NCIT:C494
    reported_labels:
    - Fluoxetine
    ontology_label: Fentanyl
  - term_id: NCIT:C1505
    reported_labels:
    - SSRI
    ontology_label: Dietary Supplement
  - term_id: NCIT:C557
    reported_labels:
    - Valproic Acid
    ontology_label: Hydroxychloroquine
  - term_id: NCIT:C15271
    reported_labels:
    - Cognitive Behavioral Therapy
    ontology_label: Liver Transplantation
  - term_id: NCIT:C16327
    reported_labels:
    - Deep Brain Stimulation
    ontology_label: Behavioral Medicine
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intermittent_Explosive_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intermittent_Explosive_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intermittent Explosive Disorder
- **MONDO ID:** MONDO:0001521 (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Intermittent Explosive Disorder** covering all of the
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

# Intermittent Explosive Disorder (MONDO:0001521): A Comprehensive Disease Characteristics Report

## Summary

**Intermittent Explosive Disorder (IED)** is a common but under-recognized psychiatric impulse-control disorder defined by recurrent, impulsive, and disproportionate aggressive outbursts (verbal aggression, property destruction, or physical assault) that are out of proportion to any provocation and not better explained by another disorder. Pooled global estimates place lifetime prevalence at ~5% (12-month ~4.4%), making IED one of the most prevalent psychiatric conditions—yet only a small minority of affected people ever receive care. IED has a distinctive natural history: it emerges early (mean onset ~age 12), is highly persistent into adulthood, and temporally precedes most of its many comorbidities (mood, anxiety, substance use, and eating disorders), positioning it as a developmental "gateway" disorder and a strategic target for early intervention.

Mechanistically, the evidence converges on a **frontolimbic regulatory-failure model**. Functional imaging shows amygdala hyperreactivity to social threat (angry faces) coupled with orbitofrontal/ventromedial prefrontal hypoactivation and a loss of amygdala–OFC functional coupling; structural imaging shows reduced gray matter across this same frontolimbic network. At the neurochemical level, central serotonergic tone is low (reduced CSF 5-HIAA in impulsive-aggressive populations), and at the cognitive level patients exhibit a hostile attribution bias and maladaptive social-emotional information processing. Peripheral biology shows a pro-inflammatory signature (elevated CRP and IL-6), blunted morning cortisol (HPA hypoactivity), and kynurenine-pathway dysregulation. These abnormalities arise from a polygenic/multifactorial vulnerability interacting with childhood trauma and exposure to interpersonal violence; IED-specific genetics remain almost entirely unstudied.

Treatment rests on two evidence-based pillars: **SSRIs (notably fluoxetine)**, which reduce impulsive aggression and irritability in randomized controlled trials, and **multicomponent cognitive-behavioral therapy (CBT)**, which is the most effective psychological modality and outperforms supportive psychotherapy in RCTs. Despite proven treatments, fewer than 5% of affected individuals consult a professional about their anger attacks, underscoring a large treatment gap. Major knowledge gaps remain in IED-specific genetics, epigenetics, and validated animal models.

---

## Key Findings

### Finding 1 — IED is a common, male-predominant impulse-control disorder (~5% lifetime prevalence)

A systematic review and meta-analysis of 29 studies (N = 182,112 across 17 countries) established pooled **lifetime prevalence of 5.1% (95% CI 3.4–7.5%)** and **12-month prevalence of 4.4% (95% CI 2.9–6.7%)** ([PMID: 40834564](https://pubmed.ncbi.nlm.nih.gov/40834564/)). Prevalence is higher in clinical (10.5%), refugee (8.5%), and adolescent populations. The single strongest demographic risk factor is male gender (**OR = 3.39**), alongside younger age, trauma exposure, and psychiatric comorbidity. DSM-5 criteria (which added verbal aggression thresholds and a frequency criterion) yield lower estimates than DSM-IV. This positions IED among the most prevalent psychiatric disorders worldwide.

> *"pooled lifetime and 12-month prevalence estimates were 5.1 % (95 % CI: 3.4-7.5 %) and 4.4 % (95 % CI: 2.9-6.7 %), respectively"* — [PMID: 40834564](https://pubmed.ncbi.nlm.nih.gov/40834564/)

> *"Male gender (OR = 3.39), younger age, trauma exposure, and psychiatric comorbidities (mood, anxiety, and substance use disorders) emerged as robust risk factors"* — [PMID: 40834564](https://pubmed.ncbi.nlm.nih.gov/40834564/)

### Finding 2 — IED neurobiology centers on the amygdala–orbitofrontal circuit and serotonergic dysfunction

A systematic review of 24 studies across seven databases described a **multifactorial etiology** emphasizing the **amygdala and orbitofrontal cortex (OFC)** in emotional regulation and impulse control, with **serotonergic signaling** as the principal therapeutic target and childhood trauma/adverse family environment as developmental contributors ([PMID: 40023093](https://pubmed.ncbi.nlm.nih.gov/40023093/); [PMID: 39314952](https://pubmed.ncbi.nlm.nih.gov/39314952/)). Critically, this review noted that IED-*specific* genetic studies were largely absent.

> *"emphasizing the role of the amygdala and orbitofrontal cortex in emotional regulation and impulse control, and supporting interventions that target serotonergic signaling"* — [PMID: 40023093](https://pubmed.ncbi.nlm.nih.gov/40023093/)

> *"childhood trauma and adverse family environment may significantly contribute to the development of IED"* — [PMID: 40023093](https://pubmed.ncbi.nlm.nih.gov/40023093/)

### Finding 3 — fMRI shows amygdala hyperreactivity, OFC hypoactivation, and loss of amygdala–OFC coupling

In a controlled fMRI study (n = 10 IED vs 10 healthy controls), individuals with IED exhibited **exaggerated amygdala reactivity and diminished OFC activation to angry faces**, and—unlike controls—**failed to demonstrate amygdala–OFC coupling** during responses to social threat ([PMID: 17210136](https://pubmed.ncbi.nlm.nih.gov/17210136/)). A larger replication (n = 20 IED vs 20 HC) found greater amygdala responses to angry vs neutral faces, and amygdala activation **correlated with the number of prior aggressive acts** ([PMID: 27145325](https://pubmed.ncbi.nlm.nih.gov/27145325/)). This provides direct human evidence that the "bottom-up" threat signal is amplified while "top-down" prefrontal control is deficient and functionally disconnected.

> *"individuals with IED exhibited exaggerated amygdala reactivity and diminished OFC activation to faces expressing anger"* — [PMID: 17210136](https://pubmed.ncbi.nlm.nih.gov/17210136/)

> *"aggressive subjects failed to demonstrate amygdala-OFC coupling during responses to angry faces"* — [PMID: 17210136](https://pubmed.ncbi.nlm.nih.gov/17210136/)

> *"amygdala activation to angry faces was correlated with number of prior aggressive acts"* — [PMID: 27145325](https://pubmed.ncbi.nlm.nih.gov/27145325/)

### Finding 4 — IED shows reduced frontolimbic gray matter volume correlating inversely with aggression

A voxel-based morphometry study (n = 168: 53 healthy controls, 58 psychiatric controls, 57 IED) found **significantly lower gray matter volume in IED** in the orbitofrontal cortex, ventral medial prefrontal cortex, anterior cingulate cortex, amygdala, insula, and uncus, versus both control groups. Differences were not attributable to confounders or comorbidity, and gray matter volume **correlated inversely with aggression** ([PMID: 29560894](https://pubmed.ncbi.nlm.nih.gov/29560894/)). This structural deficit maps precisely onto the functional circuit implicated by fMRI, suggesting a stable morphometric substrate for the disorder.

> *"Gray matter volume was found to be significantly lower in subjects with IED compared with healthy control subjects and psychiatric controls in orbitofrontal cortex, ventral medial prefrontal cortex, anterior cingulate cortex, amygdala, insula, and uncus"* — [PMID: 29560894](https://pubmed.ncbi.nlm.nih.gov/29560894/)

### Finding 5 — Low central serotonergic function is associated with impulsive aggression

In mentally disordered violent offenders, subjects with impulse control disorder had **lower mean CSF 5-HIAA** (the principal serotonin metabolite), and suicide attempters among them had significantly lower CSF 5-HIAA ([PMID: 10823300](https://pubmed.ncbi.nlm.nih.gov/10823300/)). A review of more than 20 CSF studies confirmed a consistent link between low CSF 5-HIAA and suicidal/violent behavior, concluding that *"aggression dyscontrol may partly explain the association between suicide and serotonin"* ([PMID: 9616798](https://pubmed.ncbi.nlm.nih.gov/9616798/)). Childhood trauma interacts with this system: low CSF 5-HIAA combined with childhood violence exposure predicted adult violent acts ([PMID: 21356560](https://pubmed.ncbi.nlm.nih.gov/21356560/)). This underlies the rationale for serotonergic pharmacotherapy.

> *"Subjects with impulse control disorder also had lower mean CSF 5-HIAA"* — [PMID: 10823300](https://pubmed.ncbi.nlm.nih.gov/10823300/)

> *"aggression dyscontrol may partly explain the association between suicide and serotonin"* — [PMID: 9616798](https://pubmed.ncbi.nlm.nih.gov/9616798/)

### Finding 6 — IED features hostile attribution bias and maladaptive social-emotional information processing

Using a validated video-based Social Emotional Information Processing (SEIP) assessment (75 IED vs 75 HC), IED participants showed **reduced encoding of relevant social information, elevated hostile attribution bias, elevated negative emotional responses, and greater endorsement of physically and relationally aggressive responses** to ambiguous social stimuli ([PMID: 28012305](https://pubmed.ncbi.nlm.nih.gov/28012305/)). An emotion-attribution task (n = 242) showed IED subjects **over-attribute anger** to non-anger stories and less reliably identify sadness ([PMID: 33662604](https://pubmed.ncbi.nlm.nih.gov/33662604/)). This cognitive layer is the direct target of CBT.

> *"IED participants displayed reduced encoding of relevant information from the film clips, elevated hostile attribution bias, elevated negative emotional response, and elevated endorsement of physically aggressive and relationally aggressive responses"* — [PMID: 28012305](https://pubmed.ncbi.nlm.nih.gov/28012305/)

> *"Participants with IED correctly identified anger stories and misattributed anger to non-anger stories significantly more often than PC and HC participants"* — [PMID: 33662604](https://pubmed.ncbi.nlm.nih.gov/33662604/)

### Finding 7 — Peripheral inflammation, blunted cortisol, and kynurenine dysregulation

IED shows a reproducible peripheral biology. Plasma **CRP and IL-6 are significantly higher** in IED (n = 69) than in psychiatric (n = 61) or healthy controls (n = 67), correlating with aggression ([PMID: 24352431](https://pubmed.ncbi.nlm.nih.gov/24352431/)). **Morning salivary cortisol is significantly lower** in IED (p < 0.05), correlating inversely with trait anger (r = −0.26) and aggression (r = −0.25); CRP correlates inversely with morning cortisol (r = −0.28), suggesting HPA hypoactivity ([PMID: 36863129](https://pubmed.ncbi.nlm.nih.gov/36863129/)). Plasma kynurenine is reduced (−48%) with modest reductions in quinolinic acid, indicating tryptophan/kynurenine pathway dysregulation ([PMID: 27318828](https://pubmed.ncbi.nlm.nih.gov/27318828/)). Notably, inflammatory markers were **not** reduced by fluoxetine or divalproex treatment, and neither drug reduced aggression in that particular sample ([PMID: 26277033](https://pubmed.ncbi.nlm.nih.gov/26277033/)), suggesting inflammation may be a trait correlate rather than a treatment-responsive mediator.

> *"Both plasma C-reactive protein and interleukin 6 levels were significantly higher in participants with intermittent explosive disorder compared with psychiatric or normal controls"* — [PMID: 24352431](https://pubmed.ncbi.nlm.nih.gov/24352431/)

> *"Morning, but not evening, salivary cortisol levels were significantly lower in IED (p < 0.05), compared with control, study participants"* — [PMID: 36863129](https://pubmed.ncbi.nlm.nih.gov/36863129/)

### Finding 8 — Early adolescent onset, high persistence, and temporal precedence over comorbidities

The National Comorbidity Survey Replication Adolescent Supplement (n = 6,483) found lifetime IED in 7.8% of adolescents, with **mean age at onset of 12.0 years** and high persistence (80.1% of lifetime cases met 12-month criteria); IED-related injuries requiring medical attention occurred 52.5 times per 100 lifetime cases ([PMID: 22752056](https://pubmed.ncbi.nlm.nih.gov/22752056/)). IED onset preceded substance use disorder in **92.5%** of comorbid cases ([PMID: 28252880](https://pubmed.ncbi.nlm.nih.gov/28252880/)) and eating disorders in ≥70% of comorbid cases ([PMID: 28324677](https://pubmed.ncbi.nlm.nih.gov/28324677/)). Co-occurring anxiety markedly worsens functional impairment (adults 45.7% vs 28.2% severe impairment; [PMID: 26422701](https://pubmed.ncbi.nlm.nih.gov/26422701/)). In the São Paulo survey, 76.8% of IED cases had ≥1 other psychiatric disorder ([PMID: 32285139](https://pubmed.ncbi.nlm.nih.gov/32285139/)).

> *"Intermittent explosive disorder had an early age at onset (mean age, 12.0 years) and was highly persistent, as indicated by 80.1% of lifetime cases"* — [PMID: 22752056](https://pubmed.ncbi.nlm.nih.gov/22752056/)

> *"onset of IED preceded that of SUD in 92.5% of comorbid IED + SUD cases"* — [PMID: 28252880](https://pubmed.ncbi.nlm.nih.gov/28252880/)

### Finding 9 — Substantial comorbidity, suicidality, and a large treatment gap

The China Mental Health Survey (n = 28,140 adults) reported weighted 12-month IED prevalence of 1.23% and lifetime 1.54%; **61.87% had ≥1 comorbid disorder** (mood disorders most common, 55.1%). Five behavioral subtypes were identified, and the "destroy property and hurt people" subtype had the highest comorbidity (OR 17.2, 95% CI 7.4–41.8). Suicidal ideation affected 4.45%, plans 1.79%, and attempts/gestures 0.88%. Critically, only **4.77% ever consulted a professional** about their anger attacks and 7.27% accessed mental health services ([PMID: 41895057](https://pubmed.ncbi.nlm.nih.gov/41895057/)).

> *"Comorbidity was common, with 61.87% of individuals with IED having at least one comorbid disorder, most notably mood disorders (55.1%)"* — [PMID: 41895057](https://pubmed.ncbi.nlm.nih.gov/41895057/)

> *"4.77% had ever consulted a medical doctor or other professional about their anger attacks, and 7.27% accessed mental health services"* — [PMID: 41895057](https://pubmed.ncbi.nlm.nih.gov/41895057/)

### Finding 10 — Environmental risk (childhood trauma, interpersonal violence); IED-specific genetics unstudied

Childhood trauma and adverse family environment significantly contribute to IED development ([PMID: 40023093](https://pubmed.ncbi.nlm.nih.gov/40023093/)). Exposure to interpersonal violence (experiencing or witnessing) is associated with IED diagnosis, with gender moderating the pathway via emotion regulation and social information processing ([PMID: 33977809](https://pubmed.ncbi.nlm.nih.gov/33977809/)). Broader serotonergic candidate-gene work (e.g., TPH2 haplotypes influencing risk-taking/aggression; [PMID: 20043001](https://pubmed.ncbi.nlm.nih.gov/20043001/)) implicates the serotonin system but is **not IED-specific**. No GWAS, twin heritability estimate, or validated animal model exists specifically for IED.

> *"genetic studies focusing on IED were largely lacking, despite many examining the genetics underlying aggression as a general trait or other related disorders"* — [PMID: 40023093](https://pubmed.ncbi.nlm.nih.gov/40023093/)

### Finding 11 — SSRIs (fluoxetine) reduce impulsive aggression

In a double-blind RCT of fluoxetine in 100 IED subjects, treatment produced a **sustained reduction in OAS-M aggression and irritability apparent by week 2** (p < 0.01 aggression, p < 0.001 irritability), superior CGI-I response (p < 0.001), and full/partial remission in 46% ([PMID: 19389333](https://pubmed.ncbi.nlm.nih.gov/19389333/)). Baseline neuroticism and harm avoidance inversely predict antiaggressive SSRI response ([PMID: 21795983](https://pubmed.ncbi.nlm.nih.gov/21795983/)).

> *"Fluoxetine treatment resulted in a sustained reduction in OAS-M aggression, and OAS-M irritability scores, apparent as early as week 2"* — [PMID: 19389333](https://pubmed.ncbi.nlm.nih.gov/19389333/)

### Finding 12 — Multicomponent CBT is efficacious in randomized controlled trials

A meta-analysis of 12 RCTs and 14 case studies found that **CBT showed significant effectiveness reducing aggression and achieving full remission**, outperforming pharmacological treatments ([PMID: 39821512](https://pubmed.ncbi.nlm.nih.gov/39821512/)). An RCT (n = 44) showed CBT **superior to supportive psychotherapy** in decreasing aggressive and relational aggression, maintained at 3-month follow-up ([PMID: 36229112](https://pubmed.ncbi.nlm.nih.gov/36229112/)). An earlier pilot RCT (n = 45) demonstrated CBT reduced aggression, anger, hostile thinking, and depressive symptoms with large effect sizes maintained at follow-up ([PMID: 18837604](https://pubmed.ncbi.nlm.nih.gov/18837604/)). Lower baseline trait anger predicts remission ([PMID: 37856378](https://pubmed.ncbi.nlm.nih.gov/37856378/)).

> *"psychological treatments, particularly cognitive behavioural therapy (CBT), showed significant effectiveness in reducing aggression and achieving full remission compared to pharmacological treatments"* — [PMID: 39821512](https://pubmed.ncbi.nlm.nih.gov/39821512/)

> *"the cognitive behavioral intervention was superior to supportive psychotherapy in decreasing aggressive behavior and relational aggression"* — [PMID: 36229112](https://pubmed.ncbi.nlm.nih.gov/36229112/)

---

## Section-by-Section Disease Characteristics

### 1. Disease Information

**Overview.** IED is a DSM-5/ICD-11 impulse-control disorder characterized by recurrent behavioral outbursts representing a failure to control aggressive impulses, manifesting as verbal aggression or physical aggression toward property, animals, or others. The outbursts are impulsive/anger-based (not premeditated), grossly out of proportion to provocation, cause distress or functional impairment, and are not better explained by another disorder.

**Key identifiers:**
- **MONDO:** MONDO:0001521
- **ICD-10:** F63.81 (Intermittent explosive disorder)
- **ICD-11:** 6C73 (Intermittent explosive disorder), within Impulse control disorders
- **DSM-5:** 312.34, Disruptive, Impulse-Control, and Conduct Disorders chapter
- **MeSH:** Disruptive, Impulse Control, and Conduct Disorders; "Intermittent explosive disorder" indexed term
- **OMIM/Orphanet:** No dedicated Mendelian entry (not a monogenic disorder)

**Synonyms:** intermittent explosive disorder; IED; episodic dyscontrol syndrome (historical); anger attacks (colloquial/related construct).

**Data source type:** Information is derived from aggregated disease-level resources—epidemiological surveys (NCS-R, China Mental Health Survey, São Paulo Megacity), case-control neuroimaging/biomarker studies, and RCTs—rather than individual EHR-level data.

### 2. Etiology

**Causal factors.** IED is multifactorial: a polygenic/heritable vulnerability affecting serotonergic and frontolimbic emotion-regulation systems interacts with early-life environmental adversity ([PMID: 40023093](https://pubmed.ncbi.nlm.nih.gov/40023093/)). There is no single causal gene, infectious agent, or toxin.

**Genetic risk factors.** IED-specific genetics are essentially unstudied; no GWAS or twin heritability estimate exists specifically for IED. Candidate-gene evidence from the broader impulsive-aggression literature implicates the serotonin system (e.g., TPH2 haplotypes influencing risk-taking/aggression; [PMID: 20043001](https://pubmed.ncbi.nlm.nih.gov/20043001/)). Suggested susceptibility genes by analogy (not IED-validated): **TPH2, SLC6A4 (5-HTTLPR), HTR2A, HTR1B, MAOA, COMT**.

**Environmental risk factors.** Male sex (OR 3.39), younger age, childhood trauma, adverse family environment, and exposure to interpersonal violence ([PMID: 40834564](https://pubmed.ncbi.nlm.nih.gov/40834564/); [PMID: 33977809](https://pubmed.ncbi.nlm.nih.gov/33977809/)).

**Protective factors.** Lower trait anger and lower neuroticism/harm avoidance predict better treatment outcomes and remission ([PMID: 37856378](https://pubmed.ncbi.nlm.nih.gov/37856378/); [PMID: 21795983](https://pubmed.ncbi.nlm.nih.gov/21795983/)). Genetic protective factors are unknown.

**Gene–environment interactions.** Low CSF 5-HIAA (serotonergic vulnerability) combined with childhood violence exposure predicts adult violent behavior—demonstrating a serotonin × early-adversity interaction ([PMID: 21356560](https://pubmed.ncbi.nlm.nih.gov/21356560/)).

### 3. Phenotypes

| Phenotype | Type | Onset | Progression | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Impulsive aggressive outbursts | Behavioral | Childhood/adolescence (~12 y) | Episodic, recurrent | Defining feature (100%) | HP:0000718 (Aggressive behavior) |
| Irritability / anger | Behavioral/affective | Adolescence | Fluctuating | Very frequent | HP:0000737 (Irritability) |
| Verbal aggression | Behavioral | Adolescence | Episodic | Frequent (DSM-5 low-threshold criterion) | HP:0000718 |
| Property destruction / physical assault | Behavioral | Adolescence | Episodic | Subset (high-severity subtype) | HP:0000718 |
| Impulsivity | Behavioral | Early | Trait-stable | High | HP:0100710 (Impulsivity) |
| Hostile attribution bias | Cognitive | — | Trait | Characteristic | HP:0000752 (Behavioral abnormality) |
| Suicidal ideation/behavior | Behavioral | Variable | Episodic | Ideation ~4.5% | HP:0031589 (Suicidal ideation) |

**Quality of life.** Severe functional impairment is common, especially with comorbid anxiety (45.7% severe impairment in adults vs 28.2% without IED; [PMID: 26422701](https://pubmed.ncbi.nlm.nih.gov/26422701/)); IED-related injuries requiring medical attention occur ~52.5 times per 100 lifetime cases ([PMID: 22752056](https://pubmed.ncbi.nlm.nih.gov/22752056/)).

### 4. Genetic / Molecular Information

No causal genes, pathogenic variants, chromosomal abnormalities, or IED-specific epigenetic changes have been established. This is a major, explicitly documented gap ([PMID: 40023093](https://pubmed.ncbi.nlm.nih.gov/40023093/)). By analogy to the impulsive-aggression literature, serotonergic genes (TPH2, SLC6A4, HTR2A, MAOA) are plausible modifier/susceptibility loci but are unvalidated for IED. No somatic variants are relevant (this is a neurodevelopmental/psychiatric, not neoplastic, condition).

### 5. Environmental Information

**Environmental/lifestyle factors:** childhood trauma, adverse family environment, and exposure to (experiencing or witnessing) interpersonal violence are the principal established non-genetic contributors ([PMID: 40023093](https://pubmed.ncbi.nlm.nih.gov/40023093/); [PMID: 33977809](https://pubmed.ncbi.nlm.nih.gov/33977809/)). Substance use is highly comorbid and typically follows IED onset ([PMID: 28252880](https://pubmed.ncbi.nlm.nih.gov/28252880/)). **Infectious agents:** none implicated.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

```
1. Polygenic/serotonergic vulnerability + childhood trauma / interpersonal-violence exposure
        │  (gene × environment interaction; PMID 21356560)
        ▼
2. Low central serotonergic tone (reduced CSF 5-HIAA) → impaired top-down inhibitory
   modulation of limbic circuits  [demonstrated correlationally; PMID 10823300, 9616798]
        ▼
3. Structural + functional frontolimbic deficit:
   ├─ Reduced gray matter in OFC / vmPFC / ACC / amygdala / insula  (PMID 29560894)
   └─ Amygdala hyperreactivity + OFC hypoactivation to social threat  (PMID 17210136)
        ▼
4. Loss of amygdala–OFC functional coupling → failure to regulate the amygdala threat
   response  (PMID 17210136)
        ▼
5. Biased social-emotional information processing: hostile attribution bias,
   over-attribution of anger, endorsement of aggressive responses  (PMID 28012305, 33662604)
        ▼
6. Impulsive, disproportionate aggressive outburst = clinical IED
        │
        └─ Correlated peripheral biology (may amplify / mark trait, not proven causal):
           elevated CRP/IL-6 (PMID 24352431), blunted morning cortisol / HPA
           hypoactivity (PMID 36863129), kynurenine dysregulation (PMID 27318828)
```

**Upstream vs downstream.** Genetic/serotonergic vulnerability and early adversity are upstream; frontolimbic structural/functional deficits are intermediate; biased social cognition and the outburst are downstream. The inflammatory/HPA/kynurenine signatures are best interpreted as **correlated trait markers**—they were not reduced by treatment even when aggression measures were tracked ([PMID: 26277033](https://pubmed.ncbi.nlm.nih.gov/26277033/)), arguing against a simple causal role.

**Molecular pathways / neurochemistry:** serotonergic (5-HT) signaling is central (CHEBI:28790 serotonin; CHEBI:27823 5-HIAA). Tryptophan–kynurenine metabolism is dysregulated.

**Suggested GO / CL terms:** GO:0007610 (behavior), GO:0007194 (negative regulation of adenylate cyclase activity—serotonergic signaling), GO:0051966 (regulation of synaptic transmission, glutamatergic), GO:0006954 (inflammatory response), GO:0051384 (response to glucocorticoid), GO:0042755 (feeding-behavior related, contextual). Cell types: CL:0000617 (GABAergic neuron), CL:0000540 (neuron), CL:0000129 (microglial cell, for inflammatory contribution), and serotonergic neurons of the raphe nuclei.

### 7. Anatomical Structures Affected

**Organ/system level:** central nervous system (nervous system). **Primary structures (UBERON):**
- Amygdala — UBERON:0001876
- Orbitofrontal cortex / ventromedial prefrontal cortex — UBERON:0004167 (orbitofrontal cortex)
- Anterior cingulate cortex — UBERON:0009835
- Insular cortex — UBERON:0034891
- Uncus / medial temporal lobe

**Tissue/cell level:** gray matter (cortical and subcortical neurons and glia); frontolimbic circuit. **Subcellular (GO CC):** synapse (GO:0045202), neuronal cell body. **Lateralization:** bilateral frontolimbic involvement; no consistent lateralization reported.

### 8. Temporal Development

**Onset:** early, mean age ~12 years (adolescent-onset); insidious/chronic pattern ([PMID: 22752056](https://pubmed.ncbi.nlm.nih.gov/22752056/)). **Progression:** episodic outbursts on a chronic, highly persistent course (80.1% of lifetime cases active in the past 12 months). **Course:** typically chronic and lifelong without treatment; individual outbursts are acute and short-lived. **Critical period:** adolescence represents both the window of vulnerability and the optimal window for early intervention, given that IED precedes most comorbidities.

### 9. Inheritance and Population

**Epidemiology:** lifetime prevalence ~5.1% (12-month ~4.4%) globally ([PMID: 40834564](https://pubmed.ncbi.nlm.nih.gov/40834564/)); lower in some national surveys using strict DSM-5 criteria (China lifetime 1.54%; [PMID: 41895057](https://pubmed.ncbi.nlm.nih.gov/41895057/)). **Sex ratio:** male-predominant (OR 3.39). **Inheritance:** multifactorial/polygenic; no Mendelian pattern, penetrance, anticipation, founder effect, or carrier frequency is defined (IED-specific genetics unstudied). **Geographic distribution:** worldwide across 17+ countries; higher in clinical, refugee, and adolescent populations.

### 10. Diagnostics

**Clinical criteria:** DSM-5 (312.34) and ICD-11 (6C73). Diagnosis is clinical, based on history of recurrent, impulsive, disproportionate aggressive outbursts. Screening tools include the IED Screening Questionnaire (IED-SQ; validated Turkish adaptation, Cronbach's α 0.74, 95% correct classification; [PMID: 40352072](https://pubmed.ncbi.nlm.nih.gov/40352072/)), the Overt Aggression Scale–Modified (OAS-M), Buss-Perry Aggression Questionnaire, and Barratt Impulsiveness Scale. Laboratory behavioral aggression paradigms (Taylor Aggression Paradigm, Point-Subtraction Aggression Paradigm) distinguish IED from non-aggressive groups ([PMID: 39073143](https://pubmed.ncbi.nlm.nih.gov/39073143/)).

**Research biomarkers (not clinically deployed):** elevated CRP/IL-6, blunted morning cortisol, reduced plasma kynurenine, reduced CSF 5-HIAA. **Imaging (research):** fMRI amygdala hyperreactivity; structural MRI frontolimbic gray-matter reduction. **Genetic testing:** not indicated (no causal genes). **Differential diagnosis:** bipolar disorder, borderline/antisocial personality disorder, ADHD, oppositional defiant/conduct disorder, substance intoxication, psychotic disorders, and organic causes (e.g., traumatic brain injury; note misdiagnosis risk with chronic traumatic encephalopathy in men with anger problems, [PMID: 32849206](https://pubmed.ncbi.nlm.nih.gov/32849206/)).

### 11. Outcome / Prognosis

IED is chronic and persistent but not directly life-threatening; **mortality risk is indirect**, mediated by suicidality (ideation ~4.5%, attempts ~0.9%; [PMID: 41895057](https://pubmed.ncbi.nlm.nih.gov/41895057/)), injuries from outbursts, and downstream comorbidities. Morbidity includes substantial functional impairment, injury (52.5 medically-attended injuries per 100 lifetime cases), legal, occupational, and relational harm. **Prognostic factors:** lower trait anger predicts remission after CBT ([PMID: 37856378](https://pubmed.ncbi.nlm.nih.gov/37856378/)); lower neuroticism/harm avoidance predicts SSRI response ([PMID: 21795983](https://pubmed.ncbi.nlm.nih.gov/21795983/)); comorbid anxiety predicts worse impairment ([PMID: 26422701](https://pubmed.ncbi.nlm.nih.gov/26422701/)). Recovery is achievable with treatment (fluoxetine full/partial remission ~46%; CBT durable remission).

### 12. Treatment

| Modality | Agent/Approach | Evidence | NCIT suggestion |
|---|---|---|---|
| Pharmacotherapy (first-line) | **Fluoxetine (SSRI)** | RCT: sustained aggression/irritability reduction, 46% remission ([PMID: 19389333](https://pubmed.ncbi.nlm.nih.gov/19389333/)) | NCIT:C494 (Fluoxetine) |
| Pharmacotherapy | Other SSRIs (class effect) | Meta-analytic support ([PMID: 39821512](https://pubmed.ncbi.nlm.nih.gov/39821512/)) | NCIT:C1505 (SSRI) |
| Pharmacotherapy (off-label) | Mood stabilizers (divalproex) | Mixed; no aggression reduction in one RCT sample ([PMID: 26277033](https://pubmed.ncbi.nlm.nih.gov/26277033/)) | NCIT:C557 (Valproic Acid) |
| Psychotherapy (first-line) | **Multicomponent CBT** | RCT superior to supportive therapy ([PMID: 36229112](https://pubmed.ncbi.nlm.nih.gov/36229112/); [PMID: 18837604](https://pubmed.ncbi.nlm.nih.gov/18837604/)) | NCIT:C15271 (Cognitive Behavioral Therapy) |
| Experimental | Deep brain stimulation | Off-label, case-level ([PMID: 39821512](https://pubmed.ncbi.nlm.nih.gov/39821512/)) | NCIT:C16327 (Deep Brain Stimulation) |

**Pharmacogenomics:** temperament (neuroticism, harm avoidance) predicts SSRI antiaggressive response, but no validated pharmacogenetic marker exists. **Personalized medicine:** CBT is broadly effective across demographics/comorbidities, with trait anger as the main outcome modifier.

### 13. Prevention

**Primary prevention:** reduce childhood trauma and interpersonal-violence exposure; early identification given adolescent onset. **Secondary prevention:** screening (IED-SQ) in adolescents and high-risk (trauma-exposed, refugee, clinical) populations; because IED precedes most comorbidities, early treatment could prevent downstream SUD, mood, anxiety, and eating disorders. **Tertiary prevention:** CBT and SSRIs to prevent injuries, suicidality, and functional decline. **Immunization/prophylaxis:** not applicable. **Public health:** address the large treatment gap (<5% consult a professional; [PMID: 41895057](https://pubmed.ncbi.nlm.nih.gov/41895057/)) through awareness and access.

### 14. Other Species / Natural Disease

No naturally occurring IED equivalent is defined in veterinary medicine. However, **non-human primate models of impulsive aggression** provide translational relevance: monkeys with low CSF 5-HIAA show deficits in impulse control, unrestrained/violent aggression, and excessive alcohol intake, with maternal/paternal genetic and early-rearing (parental deprivation) influences ([PMID: 10414617](https://pubmed.ncbi.nlm.nih.gov/10414617/)). Orthologous serotonergic genes (TPH2, SLC6A4, HTR2A, MAOA) are conserved across mammals. NCBI Taxon: *Homo sapiens* (9606); *Macaca* spp. for the primate model.

### 15. Model Organisms

There is **no validated animal model specific to IED**. The closest is the low-CSF-5-HIAA non-human primate model of impulsive aggression ([PMID: 10414617](https://pubmed.ncbi.nlm.nih.gov/10414617/)), which recapitulates impulse-control deficits, aggression, and gene × early-adversity interactions but does not reproduce the full DSM-5 syndrome. Rodent models of aggression (e.g., MAOA knockout, resident-intruder paradigms) exist for aggression generally but are not IED-validated. This is a priority gap for mechanistic and therapeutic research.

---

## Mechanistic Model / Interpretation

IED is best understood as a **circuit-level regulatory failure disorder**. The unifying model has three tiers:

**Tier 1 — Predisposition (upstream):** heritable/polygenic serotonergic vulnerability (reflected in low central 5-HT tone) combines with early-life adversity (trauma, interpersonal violence). These interact—low CSF 5-HIAA is most dangerous when paired with childhood violence exposure.

**Tier 2 — Neural substrate (intermediate):** the frontolimbic emotion-regulation circuit is both structurally reduced (less gray matter in OFC/vmPFC/ACC/amygdala/insula) and functionally miswired (amygdala hyperreactivity + OFC hypoactivation + loss of amygdala–OFC coupling). The amygdala's threat alarm fires excessively, and the prefrontal "brake" is weak and disconnected.

**Tier 3 — Cognitive/behavioral output (downstream):** this circuit dysfunction produces a hostile attribution bias—ambiguous social cues are read as threatening/angry—and a readiness to endorse aggressive responses, culminating in the impulsive, disproportionate outburst.

The **peripheral biology** (inflammation, HPA hypoactivity, kynurenine shifts) forms a parallel correlated axis. Because these markers did not normalize with treatment even in a trial that tracked aggression, they are most parsimoniously trait markers or bidirectional correlates rather than upstream causes—an important interpretive caution for biomarker development.

Treatments map onto the model: **SSRIs** boost the deficient serotonergic tone (Tier 1/2), while **CBT** directly retrains the biased social-emotional processing (Tier 3). Their combination is mechanistically complementary.

---

## Evidence Base Summary

| Domain | Key PMIDs | Contribution |
|---|---|---|
| Epidemiology | [40834564](https://pubmed.ncbi.nlm.nih.gov/40834564/), [22752056](https://pubmed.ncbi.nlm.nih.gov/22752056/), [41895057](https://pubmed.ncbi.nlm.nih.gov/41895057/), [32285139](https://pubmed.ncbi.nlm.nih.gov/32285139/) | Prevalence, onset, persistence, comorbidity, treatment gap |
| Neuroimaging (functional) | [17210136](https://pubmed.ncbi.nlm.nih.gov/17210136/), [27145325](https://pubmed.ncbi.nlm.nih.gov/27145325/) | Amygdala hyperreactivity, OFC hypoactivation, coupling loss |
| Neuroimaging (structural) | [29560894](https://pubmed.ncbi.nlm.nih.gov/29560894/) | Frontolimbic gray-matter reduction |
| Neurochemistry | [10823300](https://pubmed.ncbi.nlm.nih.gov/10823300/), [9616798](https://pubmed.ncbi.nlm.nih.gov/9616798/), [21356560](https://pubmed.ncbi.nlm.nih.gov/21356560/), [27318828](https://pubmed.ncbi.nlm.nih.gov/27318828/) | Low serotonin, kynurenine, gene×environment |
| Peripheral biomarkers | [24352431](https://pubmed.ncbi.nlm.nih.gov/24352431/), [36863129](https://pubmed.ncbi.nlm.nih.gov/36863129/), [26277033](https://pubmed.ncbi.nlm.nih.gov/26277033/) | Inflammation, cortisol, treatment non-response of markers |
| Social cognition | [28012305](https://pubmed.ncbi.nlm.nih.gov/28012305/), [33662604](https://pubmed.ncbi.nlm.nih.gov/33662604/) | Hostile attribution bias |
| Etiology/genetics review | [40023093](https://pubmed.ncbi.nlm.nih.gov/40023093/), [39314952](https://pubmed.ncbi.nlm.nih.gov/39314952/), [33977809](https://pubmed.ncbi.nlm.nih.gov/33977809/), [20043001](https://pubmed.ncbi.nlm.nih.gov/20043001/) | Multifactorial etiology; genetics gap; environmental risk |
| Treatment | [19389333](https://pubmed.ncbi.nlm.nih.gov/19389333/), [39821512](https://pubmed.ncbi.nlm.nih.gov/39821512/), [36229112](https://pubmed.ncbi.nlm.nih.gov/36229112/), [18837604](https://pubmed.ncbi.nlm.nih.gov/18837604/), [21795983](https://pubmed.ncbi.nlm.nih.gov/21795983/), [37856378](https://pubmed.ncbi.nlm.nih.gov/37856378/) | SSRI + CBT efficacy, outcome predictors |
| Comorbidity | [28252880](https://pubmed.ncbi.nlm.nih.gov/28252880/), [28324677](https://pubmed.ncbi.nlm.nih.gov/28324677/), [26422701](https://pubmed.ncbi.nlm.nih.gov/26422701/) | Temporal precedence over SUD, ED, anxiety |
| Animal model | [10414617](https://pubmed.ncbi.nlm.nih.gov/10414617/) | Non-human primate impulsive-aggression model |

---

## Limitations and Knowledge Gaps

1. **Genetics essentially unstudied.** No GWAS, no twin heritability estimate, and no validated candidate variants exist *specifically for IED*. All genetic inference is borrowed from the broader impulsive-aggression literature ([PMID: 40023093](https://pubmed.ncbi.nlm.nih.gov/40023093/)).
2. **No IED-specific animal model.** The primate low-5-HIAA model recapitulates impulsive aggression but not the full DSM-5 syndrome.
3. **Epigenetics unexplored.** No DNA methylation or histone-modification studies specific to IED.
4. **Biomarker causality unresolved.** Inflammation, HPA, and kynurenine findings are correlational; they did not respond to treatment, arguing against a straightforward causal role ([PMID: 26277033](https://pubmed.ncbi.nlm.nih.gov/26277033/)).
5. **Small imaging samples.** Landmark fMRI studies had n = 10–20 per group; replication and larger connectivity studies are needed.
6. **Diagnostic heterogeneity.** DSM-IV vs DSM-5 criteria yield substantially different prevalence estimates, complicating cross-study comparison.
7. **Treatment evidence base is modest.** The pharmacotherapy RCT literature is limited to a small number of trials, mostly fluoxetine; no head-to-head SSRI-vs-CBT-vs-combination trial exists.

---

## Proposed Follow-up Experiments / Actions

1. **IED-specific GWAS / polygenic scoring.** Assemble well-phenotyped DSM-5 IED cohorts for a genome-wide association study and test serotonergic polygenic risk scores; this is the single largest gap.
2. **Epigenomic profiling.** Perform EWAS (blood DNA methylation) in IED vs controls, stratified by childhood-trauma exposure, to test the gene × environment interaction at the molecular level.
3. **Large-scale connectivity imaging.** Replicate amygdala–OFC coupling deficits with adequately powered resting-state and task fMRI plus DTI, and test whether connectivity normalizes after CBT/SSRI.
4. **Combination-therapy RCT.** Run a factorial trial of SSRI vs CBT vs combination vs placebo, with aggression, functioning, and neuroimaging/biomarker endpoints, to define optimal first-line strategy.
5. **Biomarker mediation study.** Longitudinally test whether inflammation/HPA/kynurenine markers mediate or merely correlate with aggression, using cross-lagged designs.
6. **Develop a validated rodent/primate IED model** incorporating early adversity and serotonergic manipulation to enable mechanistic and drug-discovery work.
7. **Close the treatment gap.** Implement and evaluate adolescent screening (IED-SQ) programs given early onset and precedence over comorbidities, testing whether early IED treatment prevents downstream SUD/mood/anxiety/eating disorders.

---

*Report compiled from a 5-iteration autonomous investigation: 12 confirmed findings, 73 papers reviewed. Evidence types span human clinical epidemiology, case-control neuroimaging and biomarker studies, randomized controlled trials, and non-human primate models.*


## Artifacts

- [OpenScientist final report](Intermittent_Explosive_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intermittent_Explosive_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 33 |
| On topic | 26 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 20 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000718` (3 mentions) - the report calls it "Aggressive behavior", "Frequent (DSM-5 low-threshold criterion)", "Subset (high-severity subtype)"; HP calls it **Aggressive behavior**
- `HP:0000752` (1 mention) - the report calls it "Behavioral abnormality"; HP calls it **Hyperactivity**
- `NCIT:C494` (1 mention) - the report calls it "Fluoxetine"; NCIT calls it **Fentanyl**
- `NCIT:C1505` (1 mention) - the report calls it "SSRI"; NCIT calls it **Dietary Supplement**
- `NCIT:C557` (1 mention) - the report calls it "Valproic Acid"; NCIT calls it **Hydroxychloroquine**
- `NCIT:C15271` (1 mention) - the report calls it "Cognitive Behavioral Therapy"; NCIT calls it **Liver Transplantation**
- `NCIT:C16327` (1 mention) - the report calls it "Deep Brain Stimulation"; NCIT calls it **Behavioral Medicine**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007194` (1 mention) - the report calls it "negative regulation of adenylate cyclase activity—serotonergic signaling"; GO calls it **negative regulation of adenylate cyclase activity**
- `GO:0042755` (1 mention) - the report calls it "feeding-behavior related, contextual"; GO calls it **eating behavior**
- `CL:0000129` (1 mention) - the report calls it "microglial cell, for inflammatory contribution"; CL calls it **microglial cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000718` - called "Aggressive behavior", "Frequent (DSM-5 low-threshold criterion)", "Subset (high-severity subtype)"