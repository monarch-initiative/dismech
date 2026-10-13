---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-12T18:23:46.568029'
end_time: '2026-10-12T19:16:20.531487'
duration_seconds: 3153.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mitochondrial Pyruvate Carrier Deficiency
  mondo_id: MONDO:0013877
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
citation_count: 22
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 22
  on_topic: 21
  validator_version: 0.3.0
term_validation:
  total_terms: 34
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 0
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0000252
    reported_labels:
    - Physical/structural
    ontology_label: Microcephaly
  - term_id: HP:0001252
    reported_labels:
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0001508
    reported_labels:
    - Clinical sign
    ontology_label: Failure to thrive
  - term_id: HP:0003542
    reported_labels:
    - Laboratory
    ontology_label: Increased circulating pyruvate concentration
  - term_id: HP:0001999
    reported_labels:
    - Physical
    ontology_label: Abnormal facial shape
  - term_id: HP:0002119
    reported_labels:
    - Imaging/structural
    ontology_label: Ventriculomegaly
  - term_id: HP:0002240
    reported_labels:
    - related
    ontology_label: Hepatomegaly
  - term_id: HP:0001942
    reported_labels:
    - Laboratory
    ontology_label: Metabolic acidosis
  - term_id: CL:0000540
    reported_labels:
    - Tissue/cell level:** nervous tissue and neurons
    ontology_label: neuron
  - term_id: UBERON:0000955
    reported_labels:
    - Primary organ:** brain
    ontology_label: brain
  labels_variant: 1
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
  path: Mitochondrial_Pyruvate_Carrier_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mitochondrial_Pyruvate_Carrier_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Pyruvate Carrier Deficiency
- **MONDO ID:** MONDO:0013877 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Pyruvate Carrier Deficiency** covering all of the
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

# Mitochondrial Pyruvate Carrier Deficiency — Comprehensive Disease Characteristics Report

**Disease:** Mitochondrial Pyruvate Carrier Deficiency (MPC deficiency)
**MONDO ID:** MONDO:0013877 · **OMIM:** 614741 · **Orphanet:** ORPHA:319652
**Category:** Mendelian (autosomal recessive inborn error of metabolism)
**Report date:** 2026-10-12

---

## Summary

Mitochondrial Pyruvate Carrier (MPC) Deficiency is an **ultra-rare autosomal recessive inborn error of mitochondrial energy metabolism** caused by biallelic loss-of-function variants in **MPC1** (chromosome 6q27, HGNC:24515), the gene encoding one of the two obligate subunits of the mitochondrial pyruvate carrier. The MPC is a ~150-kDa heterocomplex of MPC1 and MPC2 embedded in the inner mitochondrial membrane, and it constitutes the **sole point of entry of pyruvate into the mitochondrial matrix**. When the carrier fails, glucose-derived pyruvate cannot reach pyruvate dehydrogenase (PDH) or the TCA cycle: it is shunted to lactate, producing lactic acidosis and hyperpyruvatemia, while the mitochondrion is starved of acetyl-CoA and reducing equivalents, producing a cellular energy deficit ([PMID: 22628558](https://pubmed.ncbi.nlm.nih.gov/22628558/); [PMID: 22628554](https://pubmed.ncbi.nlm.nih.gov/22628554/); [PMID: 35895232](https://pubmed.ncbi.nlm.nih.gov/35895232/)).

Clinically, the disease presents in the neonatal period or infancy with **developmental delay, microcephaly, hypotonia, growth failure, facial dysmorphism, and persistently elevated serum lactate and pyruvate**, sometimes with a Leigh-like encephalopathy ([PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/); [PMID: 34873722](https://pubmed.ncbi.nlm.nih.gov/34873722/)). The single most useful biochemical discriminator is a **severe hyperlactatemia with a NORMAL lactate/pyruvate (L/P) ratio and normal PDH complex activity** — a fingerprint that separates MPC deficiency from PDH complex deficiency (also normal L/P ratio but distinguished by functional pyruvate-transport assays) and from respiratory-chain defects (which raise the L/P ratio) ([PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)). Confirmation is molecular (MPC1 sequencing) supported by functional studies in digitonin-permeabilized fibroblasts and rescue of pyruvate-driven oxygen consumption by wild-type MPC1 reconstitution ([PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/); [PMID: 34873722](https://pubmed.ncbi.nlm.nih.gov/34873722/)).

Fewer than ~15–20 patients have been reported worldwide, so there is **no established prevalence/incidence figure and no disease-specific clinical trial**. Management is supportive and mechanism-driven: **metabolic bypass** with a ketogenic diet and anaplerotic substrates aims to deliver acetyl-CoA to the TCA cycle downstream of the broken carrier. This approach rescues *Mpc1*-null mouse embryos when given to pregnant dams, but in the index human patient a ketogenic diet (and bicarbonate, thiamine, 2-chloropropionate) failed to correct severe hyperlactatemia — so treatment expectations must be tempered ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/); [PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)). No curative or approved targeted therapy exists; genetic counseling and (where available) prenatal diagnosis are central to care.

---

## Key Findings

### Finding 1 — Biallelic MPC1 mutations disrupt the MPC1/MPC2 heterocomplex that imports pyruvate into mitochondria

The molecular basis of the disease was established by two landmark 2012 *Science* papers. Bricker et al. (*A mitochondrial pyruvate carrier required for pyruvate uptake in yeast, Drosophila, and humans*, [PMID: 22628558](https://pubmed.ncbi.nlm.nih.gov/22628558/)) identified MPC1 and MPC2 as essential components of the ~150-kDa mitochondrial pyruvate carrier conserved across yeast, *Drosophila*, and humans, and mapped a causal locus to **MPC1** in three families whose children suffered lactic acidosis and hyperpyruvatemia: *"Human genetic studies of three families with children suffering from lactic acidosis and hyperpyruvatemia revealed a causal locus that mapped to MPC1, changing single amino acids that are conserved throughout eukaryotes."* In parallel, Herzig et al. (*Identification and functional expression of the mitochondrial pyruvate carrier*, [PMID: 22628554](https://pubmed.ncbi.nlm.nih.gov/22628554/)) independently proved the carrier is a heterocomplex: *"We report that MPC is a heterocomplex formed by two members of a family of previously uncharacterized membrane proteins that are conserved from yeast to mammals."* Co-expression of MPC1 and MPC2 conferred pyruvate transport in *Lactococcus lactis*, and yeast MPC mutants showed severe defects in mitochondrial pyruvate uptake. Together these define the disrupted molecular entity (the MPC1/MPC2 heterocomplex) and establish MPC1 variants as the cause of a human disease.

### Finding 2 — Clinical phenotype and an expanding variant spectrum, including Leigh-like presentations

Jiang et al. 2022 (*Identification and characterization of novel MPC1 gene variants causing mitochondrial pyruvate carrier deficiency*, [PMID: 34873722](https://pubmed.ncbi.nlm.nih.gov/34873722/)) characterized the clinical and molecular spectrum in six patients from three unrelated families (European, Kuwaiti, Chinese), reporting three novel pathogenic MPC1 variants. They summarize the disease succinctly: *"MPC deficiency (OMIM#614741) due to pathogenic MPC1 variants is a rare autosomal recessive disease involving developmental delay, microcephaly, growth failure, and increased serum lactate and pyruvate."* One patient presented as a **Leigh-like syndrome**. Patient fibroblasts showed decreased MPC1 and MPC2 protein, and — critically — *"We rescued pyruvate-driven oxygen consumption rate in patient's fibroblasts by reconstituting with wild-type MPC1,"* providing functional proof of causality. Mechanistically the variants act either by destabilizing the MPC complex or by abolishing pyruvate-uptake activity.

### Finding 3 — Mouse genetics: complete Mpc1 loss is embryonic-lethal and rescued by maternal ketogenic diet

Vanderperre et al. 2016 (*Embryonic Lethality of Mitochondrial Pyruvate Carrier 1 Deficient Mouse Can Be Rescued by a Ketogenic Diet*, [PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/)) showed that complete MPC1 loss in mice *"resulted in embryonic lethality at around E13.5."* Mutant mouse embryonic fibroblasts had defective pyruvate-driven respiration and perturbed metabolite profiles, restored by MPC1 re-expression. ¹³C-tracing revealed the key metabolic rewiring: *"MPC deficiency causes increased glutaminolysis and reduced contribution of glucose-derived pyruvate to the TCA cycle."* Mutant embryonic brains showed morphological defects, lactic acidosis, depleted TCA intermediates, energy deficit, and perturbed neurotransmitter balance. Strikingly, a maternal ketogenic diet rescued development: *"these changes were reversed when the pregnant dams were fed a ketogenic diet, which provides acetyl-CoA directly to the TCA cycle and bypasses the need for a functional MPC."* Zou et al. 2018 ([PMID: 29175325](https://pubmed.ncbi.nlm.nih.gov/29175325/)) confirmed complete MPC1 deficiency is embryonic lethal and that **fatty-acid oxidation alleviates the energy deficit** in partial-loss models. This provides the in vivo proof-of-concept for metabolic bypass therapy.

### Finding 4 — The diagnostic signature: severe hyperlactatemia with NORMAL L/P ratio, normal PDH activity, impaired pyruvate oxidation in permeabilized fibroblasts

The first biochemically defined case, Brivet et al. 2003 (*Impaired mitochondrial pyruvate importation in a patient and a fetus at risk*, [PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)), remains the diagnostic touchstone. A child of consanguineous parents presented at birth with hypotonia, mild facial dysmorphism, and periventricular cysts, with *"marked metabolic acidosis, hyperlactacidemia with normal lactate/pyruvate molar ratios, normoglycemia, and normal ammonia."* Lactate ranged 5–14 mmol/L. Crucially, *"Pyruvate dehydrogenase (PDHC) activity was normal in lymphocytes and fibroblasts"* — excluding the main differential. In digitonin-permeabilized fibroblasts, acetyl-carnitine/TCA-intermediate production from [2-¹⁴C]pyruvate and ¹⁴CO₂ release from [1-¹⁴C]pyruvate were severely impaired, whereas [U-¹⁴C]malate decarboxylation was normal; patient cells phenocopied control cells treated with the specific MPC inhibitor α-cyano-4-hydroxycinnamate. The authors concluded: *"Our results are consistent with a defect of mitochondrial pyruvate transport in the patient."* A prenatal diagnosis identified an affected fetus.

| Biochemical feature | MPC deficiency | PDH complex deficiency | Respiratory-chain defect |
|---|---|---|---|
| Blood lactate | Markedly elevated | Elevated | Elevated |
| L/P ratio | **Normal** | **Normal** | **Elevated** |
| PDH activity | **Normal** | **Reduced** | Normal |
| Pyruvate transport (permeabilized fibroblasts) | **Impaired** | Normal | Normal |
| Ammonia | Normal | Normal | Variable |

### Finding 5 — Three distinct molecular mechanisms among patient MPC1 variants (A58G, R97W, L79H)

Oonthonpan et al. 2019 (*Two human patient mitochondrial pyruvate carrier mutations reveal distinct molecular mechanisms of dysfunction*, [PMID: 31145700](https://pubmed.ncbi.nlm.nih.gov/31145700/)) dissected two human MPC1 alleles and revealed that disease arises through at least three separable biochemical lesions. The *MPC1* c.289C>T allele yields both a mis-spliced truncation (p.A58G) and a full-length point mutant (p.R97W); *MPC1* c.236T>A encodes p.L79H. Using patient fibroblasts and complementation of CRISPR MPC1-null C2C12 cells, they found: *"Truncated MPC1 A58G protein was intrinsically unstable and failed to form MPC complexes. The MPC1 R97W protein was less stable but when overexpressed formed complexes with MPC2 that retained pyruvate transport activity. Conversely, MPC1 L79H protein formed stable complexes with MPC2, but these complexes failed to transport pyruvate."* Thus the carrier can fail at **(1) protein stability/assembly** (A58G), **(2) partial instability but retained transport** (R97W), or **(3) assembly-competent but transport-dead** (L79H). These variants are tied to clinical disease: *"Two reported human MPC1 mutations cause developmental abnormalities, neurological problems, metabolic deficits, and for one patient, early death."*

| Variant | Nomenclature | Complex assembly | Transport activity | Mechanism |
|---|---|---|---|---|
| A58G | c.289C>T (mis-splice) | Fails to assemble | Absent | Intrinsic instability |
| R97W | c.289C>T (full-length) | Assembles (when overexpressed) | Retained | Reduced stability |
| L79H | c.236T>A | Stable complex | **Absent** | Transport-dead carrier |

### Finding 6 — MPC is an obligate, non-redundant, druggable node; partial pharmacological inhibition is benign/beneficial, contrasting with severe complete genetic loss

The MPC is described as *"the sole point of entry of pyruvate into the mitochondrial matrix"* ([PMID: 35895232](https://pubmed.ncbi.nlm.nih.gov/35895232/)), explaining why complete loss is catastrophic and non-bypassable at the import step. Paradoxically, **partial pharmacological inhibition is therapeutically useful** in other contexts: MSDC-0160 (an insulin sensitizer and MPC modulator) in 6-OHDA Parkinson's rats improved motor behavior, decreased dopaminergic denervation, reduced mTOR activity and neuroinflammation, and increased ketogenesis, β-oxidation, and glutamate oxidation ([PMID: 35895232](https://pubmed.ncbi.nlm.nih.gov/35895232/)). Quansah et al. 2018 ([PMID: 29793507](https://pubmed.ncbi.nlm.nih.gov/29793507/)) note the neuroprotective mechanisms *"involve augmentation of autophagy via attenuation of the activity of the mammalian target of rapamycin (mTOR) in neurons, as well as the inhibition of neuroinflammation."* Thiazolidinedione-class MPC modulators are in development for type 2 diabetes and NASH ([PMID: 36830630](https://pubmed.ncbi.nlm.nih.gov/36830630/); [PMID: 40001526](https://pubmed.ncbi.nlm.nih.gov/40001526/)). The dose–response contrast (partial inhibition tolerable/beneficial vs. complete genetic loss lethal) is biologically informative for understanding the disease and for drug safety.

### Finding 7 — Ultra-rare, autosomal recessive with consanguinity; sits in the "normal L/P ratio" congenital lactic acidosis differential

MPC deficiency is extremely rare. The literature comprises a handful of families: the consanguineous index patient (Brivet 2003, [PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)), three families in Bricker 2012 ([PMID: 22628558](https://pubmed.ncbi.nlm.nih.gov/22628558/)), six patients in three families in Jiang 2022 ([PMID: 34873722](https://pubmed.ncbi.nlm.nih.gov/34873722/)), and three further Chinese cases in Jiang 2023 ([PMID: 37899339](https://pubmed.ncbi.nlm.nih.gov/37899339/)) — well under 20 reported individuals. Jiang 2022 states: *"To date, two MPC1 variants in four cases have been reported, though only one with a detailed clinical description."* No formal prevalence/incidence figure is established. Its principal differential, pyruvate dehydrogenase complex deficiency (PDCD), has an incidence of *"about 1 in 42,000 live births annually in the USA"* ([PMID: 37688338](https://pubmed.ncbi.nlm.nih.gov/37688338/)). Other differentials sharing congenital lactic acidosis include pyruvate carboxylase deficiency (adds hyperammonemia; [PMID: 32145058](https://pubmed.ncbi.nlm.nih.gov/32145058/)), ECHS1 deficiency ([PMID: 31908952](https://pubmed.ncbi.nlm.nih.gov/31908952/)), and respiratory-chain complex defects (which raise the L/P ratio).

### Finding 8 — Somatic MPC1 downregulation in cancer mirrors Warburg reprogramming (distinct from germline disease)

Although not the Mendelian disease itself, somatic loss of MPC1 illuminates the cellular consequences of carrier loss. Xue et al. 2021 (*Mitochondrial pyruvate carrier 1: a novel prognostic biomarker*, [PMID: 34059057](https://pubmed.ncbi.nlm.nih.gov/34059057/)) report that *"MPC1 expression is significantly decreased in cancer tissue and associated with poor prognosis."* High MPC1 expression is favorable in KIRC, LUAD, PAAD, and PRAD; low MPC1 in breast-invasive carcinoma associates with shorter survival. MPC is *"frequently lost or downregulated"* in colorectal cancer ([PMID: 42758364](https://pubmed.ncbi.nlm.nih.gov/42758364/)), while MPC2 overexpression drives OXPHOS and progression in diffuse large B-cell lymphoma ([PMID: 40287899](https://pubmed.ncbi.nlm.nih.gov/40287899/)). These are acquired/somatic expression changes, not germline coding variants, but they demonstrate at the cellular level that MPC loss forces a glycolytic (Warburg-type) shift — the same metabolic rerouting seen in the inherited disease.

### Finding 9 — Management is metabolic bypass and supportive care; no curative or approved targeted therapy

No disease-specific trial exists. The therapeutic rationale derives from (a) the animal proof-of-concept that a ketogenic diet bypasses the carrier by supplying acetyl-CoA directly to the TCA cycle and rescues *Mpc1*-null mice ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/)), with fatty-acid oxidation alleviating partial-loss energy deficits ([PMID: 29175325](https://pubmed.ncbi.nlm.nih.gov/29175325/)); and (b) extrapolation from the mechanistically analogous PDCD, where *"Ketogenic diet therapy (KDT) is commonly used to bypass defective glucose metabolism"* ([PMID: 42341672](https://pubmed.ncbi.nlm.nih.gov/42341672/)), with earlier initiation and greater carbohydrate restriction improving longevity and mental development ([PMID: 9409363](https://pubmed.ncbi.nlm.nih.gov/9409363/)). Dichloroacetate is used in PDCD ([PMID: 41898592](https://pubmed.ncbi.nlm.nih.gov/41898592/)). Importantly, in the original MPC-deficient patient, these measures failed: *"Hyperlactacidemia was severe (5-14 mmol/l) and not corrected with bicarbonate, thiamine (10 mg/d), 2-chloropropionate (100 mg/kg/d) and a ketogenic diet"* ([PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)).

---

## Section-by-Section Report

### 1. Disease Information

MPC deficiency is a Mendelian inborn error of mitochondrial energy metabolism in which pyruvate cannot be transported from the cytosol into the mitochondrial matrix, blocking its oxidation. **Key identifiers:** MONDO:0013877; OMIM 614741 ("Mitochondrial pyruvate carrier deficiency"); Orphanet ORPHA:319652; MeSH concept mapping to mitochondrial metabolism/lactic acidosis (no dedicated MeSH heading). No specific ICD-10 code exists; it is captured under E88.4-type mitochondrial/metabolic disorder codes. **Synonyms/alternative names:** MPC deficiency, mitochondrial pyruvate carrier 1 deficiency, MPYCD (OMIM phenotype symbol). **Source type:** Information is derived from aggregated disease-level resources and individual case reports/case series (not large EHR cohorts), reflecting extreme rarity.

### 2. Etiology

**Causal factor:** genetic — biallelic (homozygous or compound heterozygous) loss-of-function variants in **MPC1** disrupting the MPC1/MPC2 heterocomplex ([PMID: 22628558](https://pubmed.ncbi.nlm.nih.gov/22628558/)). **Genetic risk factor:** the only established risk factor is carrying two pathogenic MPC1 alleles; **consanguinity** increases homozygosity risk (the index patient was from a consanguineous union; [PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)). No MPC2-caused human disease has been definitively reported. **Environmental risk/protective factors:** none established as causal; catabolic stress (fasting, intercurrent illness) can precipitate metabolic crises generically in mitochondrial disease. **Protective/modifier factors:** dietary ketosis and fatty-acid oxidation partially bypass the defect in models (acetyl-CoA supplied downstream), functioning as a metabolic "protective" intervention ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/); [PMID: 29175325](https://pubmed.ncbi.nlm.nih.gov/29175325/)). **Gene–environment interaction:** genotype (residual carrier function) interacts with dietary carbon source — the key actionable GxE axis.

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset | Frequency |
|---|---|---|---|---|
| Developmental delay / intellectual disability | Neurodevelopmental | HP:0001263 / HP:0001249 | Infancy | Common |
| Microcephaly | Physical/structural | HP:0000252 | Congenital/infantile | Reported |
| Hypotonia | Clinical sign | HP:0001252 | Neonatal | Reported |
| Growth failure / failure to thrive | Clinical sign | HP:0001508 | Infancy | Common |
| Lactic acidosis (hyperlactatemia) | Laboratory | HP:0003128 / HP:0002151 | Neonatal/infantile | Hallmark (all) |
| Hyperpyruvatemia (elevated pyruvate) | Laboratory | HP:0003542 | Neonatal | Hallmark |
| Facial dysmorphism | Physical | HP:0001999 | Congenital | Reported (index case) |
| Periventricular cysts / brain abnormality | Imaging/structural | HP:0002119 | Congenital | Reported (index case) |
| Leigh-like encephalopathy | Clinical syndrome | HP:0002240 (related) | Infantile | Subset |
| Metabolic acidosis | Laboratory | HP:0001942 | Neonatal | Common |

Onset is predominantly **neonatal to infantile**; severity ranges from severe/lethal to milder, with variable expressivity. Progression is generally **progressive/episodic** with metabolic decompensations. Quality-of-life impact is substantial where neurodevelopmental impairment and recurrent acidosis occur; no disease-specific QoL instrument data exist (not available) ([PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/); [PMID: 34873722](https://pubmed.ncbi.nlm.nih.gov/34873722/)).

### 4. Genetic / Molecular Information

**Causal gene:** MPC1 (HGNC:24515; NCBI Gene 51660; chromosome 6q27; UniProt Q9Y5U8; OMIM gene 614738). **MPC2** (HGNC:21606; UniProt O95563) is the obligate partner subunit; no confirmed human MPC2-disease has been established. **Variant classes reported:** missense (p.R97W, p.L79H, novel variants in Jiang 2022/2023) and splice-altering/truncating (c.289C>T causing mis-splice → p.A58G). Classification follows ACMG/AMP; reported disease alleles are pathogenic/likely pathogenic with functional support. **Allele frequencies:** pathogenic alleles are absent or ultra-rare in gnomAD (consistent with recessive, ultra-rare disease). **Origin:** germline. **Functional consequence:** loss of function via (1) failed assembly/instability, (2) reduced stability, or (3) assembly-competent but transport-dead carrier ([PMID: 31145700](https://pubmed.ncbi.nlm.nih.gov/31145700/)). **Modifier genes:** none validated; genes governing fatty-acid oxidation/ketogenesis and glutaminolysis are candidate metabolic modifiers inferred from mouse data ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/); [PMID: 29175325](https://pubmed.ncbi.nlm.nih.gov/29175325/)). **Epigenetic/chromosomal abnormalities:** none described for the Mendelian disease (somatic promoter/expression changes occur in cancers; [PMID: 34059057](https://pubmed.ncbi.nlm.nih.gov/34059057/)).

### 5. Environmental Information

No environmental toxin, infectious agent, or occupational exposure causes MPC deficiency — it is a monogenic disease. Lifestyle/dietary carbon source is the single relevant non-genetic lever (ketogenic vs. high-carbohydrate), acting as a disease-modifying rather than disease-causing factor ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/)). Catabolic stressors (fasting, febrile illness) can trigger decompensation. Infectious agents: not applicable.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Biallelic loss-of-function **MPC1** variants are inherited → **leads to** reduced/absent functional MPC1 protein or an assembly-/transport-defective subunit ([PMID: 22628558](https://pubmed.ncbi.nlm.nih.gov/22628558/); [PMID: 31145700](https://pubmed.ncbi.nlm.nih.gov/31145700/)).
2. Defective MPC1 → **results in** failure to form (or function of) the MPC1/MPC2 heterocomplex in the inner mitochondrial membrane ([PMID: 22628554](https://pubmed.ncbi.nlm.nih.gov/22628554/)).
3. Non-functional MPC → **blocks** the obligate import of cytosolic pyruvate into the mitochondrial matrix (the carrier is the sole entry point) ([PMID: 35895232](https://pubmed.ncbi.nlm.nih.gov/35895232/)).
4. Pyruvate cannot reach PDH/TCA → **branches** into two consequences:
   - **4a.** Cytosolic pyruvate is reduced to lactate by LDH → **causes** hyperlactatemia + hyperpyruvatemia with a **normal L/P ratio** (because the cytosolic NADH/NAD⁺ redox state is not the primary lesion) and metabolic acidosis ([PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)).
   - **4b.** The TCA cycle is deprived of glucose-derived acetyl-CoA → **compensated by** increased glutaminolysis and fatty-acid oxidation to replenish TCA intermediates, which is insufficient in high-demand tissues ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/); [PMID: 29175325](https://pubmed.ncbi.nlm.nih.gov/29175325/)).
5. Reduced TCA flux and OXPHOS substrate supply → **produces** a cellular energy (ATP) deficit, most impactful in energy-hungry neurons ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/)).
6. Energy deficit + depleted TCA intermediates + perturbed neurotransmitter precursor pools → **results in** impaired brain development, microcephaly, developmental delay, hypotonia, and (in a subset) Leigh-like encephalopathy (*inferred* in humans from mouse brain phenotypes) ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/); [PMID: 34873722](https://pubmed.ncbi.nlm.nih.gov/34873722/)).
7. **Therapeutic branch:** supplying ketone bodies/fatty acids → **delivers** acetyl-CoA downstream of the carrier → **partially restores** TCA flux and rescues the phenotype in mice; variable/unproven in humans ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/); [PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)).

```
MPC1 LoF variant
      │
      ▼
No functional MPC1/MPC2 heterocomplex (inner mito membrane)
      │
      ▼
Pyruvate import into matrix BLOCKED  ◄── sole entry point
      │
      ├────────────► Pyruvate → Lactate (LDH)
      │                 → hyperlactatemia + hyperpyruvatemia
      │                 → NORMAL L/P ratio, normal PDH activity
      │
      └────────────► TCA cycle starved of acetyl-CoA
                        → ↑ glutaminolysis, ↑ β-oxidation (compensation)
                        → ATP/energy deficit (brain)
                        → developmental delay, microcephaly,
                          hypotonia, Leigh-like encephalopathy
                               ▲
                               │  Ketogenic diet / fatty acids
                               └── supply acetyl-CoA downstream (BYPASS)
```

**Molecular pathways / processes:** pyruvate metabolism (KEGG hsa00620), TCA cycle (hsa00020), OXPHOS, glutaminolysis, fatty-acid β-oxidation. **GO suggestions:** pyruvate transmembrane transport (GO:0006850); pyruvate metabolic process (GO:0006090); tricarboxylic acid cycle (GO:0006099); generation of precursor metabolites and energy (GO:0006091); mitochondrial pyruvate transmembrane transporter activity (GO:1990830). **Cellular component:** mitochondrial inner membrane (GO:0005743); mitochondrial pyruvate carrier complex (GO:0120242). **Cell types (CL):** neuron (CL:0000540), hepatocyte (CL:0000182), skeletal muscle myocyte (CL:0000188). **Metabolic/biochemical abnormality:** enzyme-transport defect at the inner mitochondrial membrane; secondary lactate/pyruvate accumulation. **Immune involvement:** none primary. **Chemical entities (CHEBI):** pyruvate (CHEBI:15361), lactate (CHEBI:24996), acetyl-CoA (CHEBI:15351).

### 7. Anatomical Structures Affected

- **Primary organ:** brain (UBERON:0000955) — central nervous system (UBERON:0001017) is most vulnerable due to high ATP demand; manifestations include microcephaly, developmental delay, periventricular cysts, Leigh-like changes.
- **Secondary/systemic:** systemic metabolic acidosis affecting multiple organs; growth failure reflects whole-body energy deficit. Liver (UBERON:0002107) and skeletal muscle (UBERON:0001134) are metabolically relevant (mouse muscle-specific and hepatic MPC studies; [PMID: 31305240](https://pubmed.ncbi.nlm.nih.gov/31305240/); [PMID: 36830630](https://pubmed.ncbi.nlm.nih.gov/36830630/)).
- **Body systems:** nervous system (primary), metabolic/endocrine, musculoskeletal.
- **Tissue/cell level:** nervous tissue and neurons (CL:0000540) are the principal affected population.
- **Subcellular:** mitochondrion (GO:0005739), inner mitochondrial membrane (GO:0005743) — the site of the defective carrier.
- **Lateralization:** systemic/bilateral (not applicable as a localized lesion).

### 8. Temporal Development

**Onset:** congenital/neonatal to infantile; metabolic acidosis and dysmorphism may be present at birth ([PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)). **Onset pattern:** acute neonatal decompensation or subacute infantile presentation. **Progression:** chronic, lifelong, often progressive with episodic metabolic crises; severe cases may be lethal in early life (one reported early death; [PMID: 31145700](https://pubmed.ncbi.nlm.nih.gov/31145700/)). **Critical period:** early neurodevelopment is the window of greatest vulnerability and of greatest therapeutic opportunity — mouse data suggest that bypassing the defect during gestation/early life is decisive ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/)); by analogy with PDCD, earlier dietary intervention improves outcomes ([PMID: 9409363](https://pubmed.ncbi.nlm.nih.gov/9409363/)).

### 9. Inheritance and Population

**Inheritance:** autosomal recessive ([PMID: 34873722](https://pubmed.ncbi.nlm.nih.gov/34873722/)). **Penetrance:** presumed complete in biallelic LoF, with **variable expressivity** (severe lethal to Leigh-like to milder). **Epidemiology:** ultra-rare; <20 reported patients; no validated prevalence/incidence (not available). **Consanguinity:** documented (index case; [PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)). **Carrier frequency / founder effects:** not established; pathogenic alleles are not recurrent population founders. **Populations:** reported cases span European, Kuwaiti, and Chinese ancestries ([PMID: 34873722](https://pubmed.ncbi.nlm.nih.gov/34873722/); [PMID: 37899339](https://pubmed.ncbi.nlm.nih.gov/37899339/)) — no ethnic predilection beyond consanguinity. **Sex ratio:** no sex bias expected (autosomal); not quantified. **Anticipation / mosaicism:** not applicable/not reported.

### 10. Diagnostics

**Laboratory:** elevated blood/CSF lactate (5–14 mmol/L) and pyruvate with a **normal L/P molar ratio**; normoglycemia; normal ammonia; metabolic acidosis ([PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)). **Key discriminating assay:** normal PDH complex activity in lymphocytes/fibroblasts combined with **impaired pyruvate oxidation/transport in digitonin-permeabilized fibroblasts** (patient cells phenocopy MPC-inhibitor-treated controls) ([PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)). **Functional confirmation:** rescue of pyruvate-driven oxygen consumption in patient fibroblasts by wild-type MPC1 reconstitution ([PMID: 34873722](https://pubmed.ncbi.nlm.nih.gov/34873722/)). **Genetic testing:** targeted MPC1 sequencing / mitochondrial-disease or lactic-acidosis gene panels; WES/WGS for undifferentiated congenital lactic acidosis — the most efficient route given phenotype overlap. **Imaging:** brain MRI may show periventricular cysts, structural anomalies, or Leigh-like signal changes. **Differential diagnosis:** PDH complex deficiency (normal L/P but normal pyruvate transport, reduced PDH), pyruvate carboxylase deficiency (hyperammonemia; [PMID: 32145058](https://pubmed.ncbi.nlm.nih.gov/32145058/)), ECHS1 deficiency ([PMID: 31908952](https://pubmed.ncbi.nlm.nih.gov/31908952/)), and respiratory-chain defects (elevated L/P ratio). **Screening:** no newborn-screening marker; prenatal diagnosis is feasible (demonstrated functionally in an at-risk fetus; [PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)) and molecularly once the familial variant is known.

### 11. Outcome / Prognosis

Prognosis is variable and can be severe. Outcomes range from early death (one reported; [PMID: 31145700](https://pubmed.ncbi.nlm.nih.gov/31145700/)) to survival with developmental delay and recurrent metabolic acidosis ([PMID: 34873722](https://pubmed.ncbi.nlm.nih.gov/34873722/)). **Morbidity** is dominated by neurodevelopmental disability. Formal survival rates, life expectancy, and validated prognostic biomarkers are **not available** given the tiny cohort. **Prognostic factors (inferred):** severity of the biochemical defect (transport-dead vs. partial-function alleles), earliness of diagnosis, and responsiveness to metabolic bypass. No disease-specific QoL data exist.

### 12. Treatment

No curative or FDA-approved targeted therapy exists; management is **supportive and metabolic-bypass–based** (NCIT concepts: Ketogenic Diet, C92206; Supportive Care, C133445; Dietary Supplement/Nutritional Support):

- **Ketogenic diet** — supplies acetyl-CoA directly to the TCA cycle, bypassing the carrier; rescues *Mpc1*-null mice ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/)); by analogy to PDCD, early/strict implementation improves outcomes ([PMID: 42341672](https://pubmed.ncbi.nlm.nih.gov/42341672/); [PMID: 9409363](https://pubmed.ncbi.nlm.nih.gov/9409363/)). **Caveat:** failed to correct hyperlactatemia in the index MPC patient ([PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)).
- **Anaplerotic substrates / fatty-acid oxidation support** — alleviates energy deficit in partial-loss mouse models ([PMID: 29175325](https://pubmed.ncbi.nlm.nih.gov/29175325/)).
- **Acute acidosis management** — bicarbonate buffering (variably effective), thiamine, cofactor trials (largely ineffective in index case; [PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)).
- **Dichloroacetate** — used in the analogous PDCD to lower lactate ([PMID: 41898592](https://pubmed.ncbi.nlm.nih.gov/41898592/)); not validated in MPC deficiency.
- **Supportive/rehabilitative care** — developmental therapies, nutrition, neurologic management.
- **Experimental/future:** gene-replacement or MPC1 reconstitution is mechanistically plausible (wild-type MPC1 rescues patient fibroblasts; [PMID: 34873722](https://pubmed.ncbi.nlm.nih.gov/34873722/)) but no clinical program exists. No NCT trials are registered specifically for MPC deficiency. **Pharmacogenomics:** not applicable.

### 13. Prevention

Primary prevention of this monogenic disease is through **genetic counseling, carrier testing in at-risk/consanguineous families, prenatal diagnosis, and preimplantation genetic testing** once the familial MPC1 variant is known ([PMID: 12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/)). Secondary/tertiary prevention focuses on early metabolic-bypass initiation and avoidance of catabolic triggers to prevent neurodevelopmental deterioration and acidotic crises. No vaccine, public-health, or environmental intervention applies.

### 14. Other Species / Natural Disease

The MPC and MPC1/MPC2 subunits are **evolutionarily conserved from yeast to mammals** ([PMID: 22628554](https://pubmed.ncbi.nlm.nih.gov/22628554/); [PMID: 22628558](https://pubmed.ncbi.nlm.nih.gov/22628558/)). Orthologs: mouse *Mpc1* (NCBI Gene 55951), *Drosophila* and *Saccharomyces cerevisiae* MPC homologs. No naturally occurring companion-animal or wildlife disease is catalogued in OMIA for MPC1 (not available). No zoonotic potential (genetic disease). Comparative biology shows strong mechanistic conservation, making model-organism findings highly translatable.

### 15. Model Organisms

- **Mouse (NCBI Taxon 10090):** whole-body *Mpc1* knockout → embryonic lethality ~E13.5 with lactic acidosis, glutaminolysis shift, brain defects, and neurotransmitter imbalance; rescued by maternal ketogenic diet ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/)). A CRISPR partial-deficiency line is viable, with fatty-acid oxidation offsetting energy deficit ([PMID: 29175325](https://pubmed.ncbi.nlm.nih.gov/29175325/)). Skeletal-muscle-specific MPC deletion reroutes glucose to lactate and drives leanness ([PMID: 31305240](https://pubmed.ncbi.nlm.nih.gov/31305240/)); hepatic MPC models inform metabolic-disease biology ([PMID: 36830630](https://pubmed.ncbi.nlm.nih.gov/36830630/)).
- **Cellular/in vitro:** patient fibroblasts; CRISPR MPC1-null C2C12 myoblasts used for complementation/mechanism dissection ([PMID: 31145700](https://pubmed.ncbi.nlm.nih.gov/31145700/)); MEFs ([PMID: 27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/)).
- **Invertebrate/yeast:** *Drosophila* and *S. cerevisiae* MPC mutants were foundational for discovering the carrier and remain tractable for transport studies ([PMID: 22628558](https://pubmed.ncbi.nlm.nih.gov/22628558/); [PMID: 22628554](https://pubmed.ncbi.nlm.nih.gov/22628554/)).
- **Phenotype recapitulation:** mouse models reproduce lactic acidosis, energy deficit, and brain pathology; **limitation:** complete knockout is embryonic-lethal, so adult/chronic human-like neurodevelopmental progression is hard to model with the null allele — hypomorphic/conditional models better mirror surviving patients.

---

## Mechanistic Model / Interpretation

The disease is best understood as a **single-point metabolic bottleneck**. Pyruvate stands at the crossroads of glycolysis, the TCA cycle, and gluconeogenesis; the MPC is the one door through which it must pass to be oxidized. When MPC1 fails, the door is shut. Two consequences follow in parallel: carbon backs up as lactate (producing the clinical hyperlactatemia with a telltale normal L/P ratio and normal PDH activity), and the mitochondrion is starved of the acetyl-CoA it would have made from pyruvate (producing an energy deficit). Cells attempt compensation by burning glutamine and fatty acids, but the brain — with its high, continuous ATP demand and limited metabolic flexibility during development — cannot fully adapt, yielding the neurodevelopmental phenotype.

The genotype-to-mechanism mapping is unusually clean (Finding 5): different patient alleles fail at different steps (assembly, stability, or transport), yet all converge on the same downstream block. This convergence explains why the clinical picture is relatively stereotyped despite allelic heterogeneity, and it predicts that **any therapy acting downstream of the carrier** (ketone bodies, anaplerotic substrates) should help regardless of the specific variant — the logic behind metabolic bypass. The mouse ketogenic-diet rescue is the strongest support for this model, while the index patient's failure to respond is the strongest caution: human CNS damage may already be established by the time of diagnosis, and bypass may be incomplete in tissues with high obligate glucose oxidation.

The dose–response contrast with pharmacology (Finding 6) is conceptually important: *partial* MPC inhibition is tolerable and even beneficial (insulin sensitization, neuroprotection), whereas *complete* genetic loss is lethal. This nonlinearity frames both the disease (why total loss is catastrophic) and the drug-development landscape (why MPC modulators target partial inhibition).

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [22628558](https://pubmed.ncbi.nlm.nih.gov/22628558/) | MPC required for pyruvate uptake (yeast/fly/human) | Human genetics + model | Establishes MPC1 as causal gene |
| [22628554](https://pubmed.ncbi.nlm.nih.gov/22628554/) | Identification of the MPC | In vitro/model | Defines MPC1/MPC2 heterocomplex |
| [12649063](https://pubmed.ncbi.nlm.nih.gov/12649063/) | Impaired mitochondrial pyruvate importation | Human clinical | Diagnostic signature; index patient |
| [34873722](https://pubmed.ncbi.nlm.nih.gov/34873722/) | Novel MPC1 variants causing MPC deficiency | Human clinical + functional | Phenotype spectrum; rescue proof |
| [31145700](https://pubmed.ncbi.nlm.nih.gov/31145700/) | Two patient MPC mutations, distinct mechanisms | In vitro/functional | Three molecular mechanisms |
| [27176894](https://pubmed.ncbi.nlm.nih.gov/27176894/) | Mpc1-null mouse rescued by ketogenic diet | Model organism | In vivo mechanism + therapy POC |
| [29175325](https://pubmed.ncbi.nlm.nih.gov/29175325/) | FAO alleviates MPC1-deficiency energy deficit | Model organism | Metabolic compensation |
| [35895232](https://pubmed.ncbi.nlm.nih.gov/35895232/) | MSDC-0160 attenuates neurodegeneration | Model/pharmacology | MPC as sole entry; partial inhibition |
| [29793507](https://pubmed.ncbi.nlm.nih.gov/29793507/) | MPC inhibition neuroprotection | Review | Downstream mTOR/neuroinflammation |
| [37688338](https://pubmed.ncbi.nlm.nih.gov/37688338/) | Amino-acid ratios for PDCD | Human clinical | PDCD incidence; differential |
| [42341672](https://pubmed.ncbi.nlm.nih.gov/42341672/) | Ketogenic diet in PDH deficiency | Human/guideline | Bypass rationale |
| [9409363](https://pubmed.ncbi.nlm.nih.gov/9409363/) | KD outcomes in PDH deficiency | Human clinical | Early intervention benefit |
| [34059057](https://pubmed.ncbi.nlm.nih.gov/34059057/) | MPC1 as cancer prognostic biomarker | Human/computational | Somatic MPC1 loss parallels |
| [37899339](https://pubmed.ncbi.nlm.nih.gov/37899339/) | 3 Chinese MPC-deficiency cases | Human clinical | Expands case count |
| [31305240](https://pubmed.ncbi.nlm.nih.gov/31305240/) | Muscle MPC deletion rewires glucose | Model organism | Tissue-specific metabolism |

**Consistency:** Independent lines (human genetics, patient biochemistry, cellular complementation, and mouse genetics) converge on the same mechanism — a strong, internally consistent evidence base. **Challenge/tension:** The chief tension is therapeutic — ketogenic diet rescues mice but failed in the index human patient, indicating the model may overstate real-world efficacy or that timing/tissue factors limit translation.

---

## Limitations and Knowledge Gaps

1. **Tiny cohort (<20 patients).** No prevalence/incidence, survival statistics, penetrance estimates, or validated QoL data exist.
2. **Therapeutic uncertainty.** The only direct human treatment evidence (index patient) is a *negative* result for ketogenic diet on lactate; efficacy, timing, and best substrate mix remain unknown.
3. **Genotype–phenotype correlation is preliminary.** Only a few alleles are mechanistically characterized; modifiers are unidentified.
4. **MPC2 disease status unresolved.** No definitive human MPC2-caused phenotype is established, leaving the recessive locus landscape incomplete.
5. **Model limitation.** Complete-null mice are embryonic-lethal, so chronic human-like neurodevelopmental progression is not directly modeled.
6. **No biomarkers for prognosis or treatment response** beyond lactate/pyruvate and L/P ratio.
7. **No natural-disease/veterinary counterpart** documented (OMIA), limiting comparative insight.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international MPC-deficiency registry** (via metabolic networks) to aggregate genotype, phenotype, treatment, and natural-history data across the scattered case reports.
2. **Hypomorphic/conditional and CNS-specific Mpc1 mouse models** to recapitulate survivable, progressive neurodevelopmental disease and rigorously test ketogenic/anaplerotic/triheptanoin regimens with dose–timing optimization.
3. **Systematic deep-mutational scanning of MPC1** (assembly + transport assays in MPC1-null C2C12/HEK cells) to pre-classify all possible variants into the three mechanistic buckets (assembly-fail, unstable, transport-dead) for rapid clinical interpretation.
4. **Patient-derived iPSC neurons/organoids** to measure neuronal energy deficit and screen bypass substrates and candidate small molecules in a human CNS context.
5. **Test gene-replacement (AAV-MPC1) proof-of-concept** in cells and models, leveraging the demonstrated rescue by wild-type MPC1 reconstitution.
6. **Prospective evaluation of early, strict ketogenic-diet initiation** (modeled on PDCD outcome data) with standardized lactate, neurodevelopmental, and MRI endpoints.
7. **Resolve the MPC2-disease question** by targeted re-analysis of undiagnosed congenital lactic-acidosis cohorts (normal L/P ratio, normal PDH) for biallelic MPC2 variants.

---

*Report compiled from 9 confirmed findings and 42 reviewed papers over 5 investigation iterations. Evidence types are annotated as human clinical, model organism, in vitro, or computational throughout.*


## Artifacts

- [OpenScientist final report](Mitochondrial_Pyruvate_Carrier_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mitochondrial_Pyruvate_Carrier_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 11 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000252` (1 mention) - the report calls it "Physical/structural"; HP calls it **Microcephaly**
- `HP:0001252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotonia**
- `HP:0001508` (1 mention) - the report calls it "Clinical sign"; HP calls it **Failure to thrive**
- `HP:0003542` (1 mention) - the report calls it "Laboratory"; HP calls it **Increased circulating pyruvate concentration**
- `HP:0001999` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal facial shape**
- `HP:0002119` (1 mention) - the report calls it "Imaging/structural"; HP calls it **Ventriculomegaly**
- `HP:0002240` (1 mention) - the report calls it "related"; HP calls it **Hepatomegaly**
- `HP:0001942` (1 mention) - the report calls it "Laboratory"; HP calls it **Metabolic acidosis**
- `CL:0000540` (2 mentions) - the report calls it "Tissue/cell level:** nervous tissue and neurons"; CL calls it **neuron**
- `UBERON:0000955` (1 mention) - the report calls it "Primary organ:** brain"; UBERON calls it **brain**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005739` (1 mention) - the report calls it "Subcellular:** mitochondrion"; GO calls it **mitochondrion**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.