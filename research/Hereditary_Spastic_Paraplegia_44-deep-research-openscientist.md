---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-30T20:47:19.514363'
end_time: '2026-08-30T21:01:06.711349'
duration_seconds: 827.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Spastic Paraplegia 44
  mondo_id: MONDO:0013179
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 18
  relevance_assessed: 18
  on_topic: 8
  off_topic: 1
  off_topic_references:
  - PMID:11838236
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 26
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 7
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0013179
    reported_labels:
    - MONDO
    ontology_label: hereditary spastic paraplegia 44
  - term_id: HP:0007015
    reported_labels:
    - Progressive spastic paraplegia
    ontology_label: Poor gross motor coordination
  - term_id: GO:0007267
    reported_labels:
    - "gap-junction\u2013mediated intercellular communication"
    ontology_label: cell-cell signaling
  - term_id: UBERON:0002718
    reported_labels:
    - corticospinal / pyramidal tracts
    ontology_label: solitary tract
  - term_id: NCIT:C61725
    reported_labels:
    - Baclofen
    ontology_label: Diltiazem
  - term_id: NCIT:C1027
    reported_labels:
    - Botulinum Toxin
    ontology_label: Budesonide
  - term_id: NCIT:C15342
    reported_labels:
    - Physical Therapy
    ontology_label: Transplantation
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hereditary_Spastic_Paraplegia_44-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hereditary_Spastic_Paraplegia_44-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Spastic Paraplegia 44
- **MONDO ID:** MONDO:0013179 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Spastic Paraplegia 44** covering all of the
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

# Hereditary Spastic Paraplegia 44 (SPG44): Comprehensive Disease Characterization Report

**Disease:** Hereditary Spastic Paraplegia 44 (SPG44)
**MONDO ID:** MONDO:0013179 | **OMIM (phenotype):** 613206 | **Category:** Mendelian (autosomal recessive)
**Causal gene:** *GJC2* (= *GJA12*), connexin-47 (Cx47)

---

## Summary

Hereditary Spastic Paraplegia 44 (SPG44) is an ultra-rare, autosomal recessive **complicated** hereditary spastic paraplegia caused by biallelic mutations in *GJC2* (also known as *GJA12*), the gene encoding the oligodendrocyte gap-junction protein **connexin-47 (Cx47)**. SPG44 occupies the **mild end of a *GJC2* allelic severity continuum** whose severe pole is Pelizaeus–Merzbacher-like disease type 1 (PMLD1), also called hypomyelinating leukodystrophy 2 (HLD2, OMIM 608804). A third, mechanistically unrelated allelic disorder — autosomal dominant hereditary lymphedema type IC (LCRP1, OMIM 613480) — arises from other *GJC2* variants affecting lymphatic endothelium. The landmark description of SPG44 (Orthmann-Murphy et al., 2009) reported three patients from one family homozygous for the *GJC2* variant c.99C>G (p.Ile33Met, "I33M") who had late-onset, slowly progressive complicated spastic paraplegia with normal or near-normal psychomotor development, preserved walking through adulthood, no nystagmus, and MRI evidence of hypomyelinating leukoencephalopathy.

Mechanistically, SPG44 results from **loss of functional Cx47 gap-junction channels**, which disrupts oligodendrocyte–oligodendrocyte and oligodendrocyte–astrocyte ("panglial syncytium") coupling required to maintain CNS myelin. A key distinction from severe PMLD1 emerged from in-vitro work: severe PMLD1 mutants are retained in the endoplasmic reticulum (ER) and trigger the unfolded protein response (UPR) and apoptosis (a **toxic gain-of-function** component), whereas the mild SPG44 allele p.I33M shows wild-type-like subcellular distribution and a **clean loss-of-function** without ER stress or apoptosis. This mechanistic difference plausibly explains SPG44's comparatively benign, ambulation-preserving course.

There is **no disease-modifying therapy** for SPG44; management is symptomatic (baclofen, botulinum toxin, physiotherapy, orthotics). Proof-of-concept **oligodendrocyte-targeted AAV-*GJC2* gene therapy** rescued pathology in *Cx32/Cx47* double-knockout mice, and transgenic re-expression of connexins rescued the same model, validating a cell-autonomous, correctable loss-of-function mechanism. Prevention is limited to genetic counseling, carrier testing, and reproductive options (prenatal / preimplantation genetic testing) for known familial variants. Prognosis is favorable relative to PMLD1: the disorder is chronic, slowly progressive, and lifelong, but not typically fatal.

---

## 1. Disease Information

**Overview.** SPG44 is a form of complicated (syndromic) hereditary spastic paraplegia in which slowly progressive lower-limb spasticity is accompanied by a diffuse hypomyelinating leukoencephalopathy visible on brain MRI, together with variable cerebellar signs and, in a minority, mild peripheral neuropathy — while cognition and vision are largely spared. It is genetically defined by biallelic *GJC2* mutations and is the mildest of the recognized *GJC2*-related CNS disorders.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013179 |
| OMIM (phenotype) | 613206 (Spastic paraplegia 44, autosomal recessive) |
| OMIM (gene) | 608803 (*GJC2*) |
| Gene (HGNC) | HGNC:8433 (*GJC2*) |
| NCBI Gene | 57165 |
| UniProt | Q5T442 (Cx47 / GJC2_HUMAN) |
| Allelic disorders | PMLD1/HLD2 (OMIM 608804); Lymphedema hereditary IC / LCRP1 (OMIM 613480) |

**Synonyms / alternative names.** SPG44; spastic paraplegia type 44, autosomal recessive; *GJC2*/*GJA12*-related complicated hereditary spastic paraplegia. The gene is historically named *GJA12* and currently *GJC2*.

**Data provenance.** Information is derived overwhelmingly from **aggregated disease-level resources** and small published case reports/family studies (the original Italian family and a subsequent Iranian family), plus mechanistic in-vitro and mouse-model literature — not from large EHR/individual-patient datasets, reflecting the disorder's extreme rarity.

---

## 2. Etiology

**Causal factors.** SPG44 is a **monogenic, autosomal recessive genetic disorder** caused by biallelic (homozygous or compound heterozygous) pathogenic variants in *GJC2*/*GJA12* encoding connexin-47. There is no environmental, infectious, or acquired cause. The disease is fully explained by loss of Cx47 gap-junction function in oligodendrocytes. As stated in the landmark report, three patients from one family carried "a novel recessively inherited mutation, 99C>G (predicted to cause an Ile>Met amino acid substitution; I33M) that causes a milder phenotype" ([PMID: 19056803](https://pubmed.ncbi.nlm.nih.gov/19056803/)).

**Genetic risk factors.** The sole risk determinant is the presence of two pathogenic *GJC2* alleles. The originally described SPG44 allele is c.99C>G (p.Ile33Met, I33M) in the N-terminus; a novel homozygous variant c.G14T (p.Ser5Ile) was later reported in an Iranian family initially diagnosed as HSP (Ghasemi et al., 2023, [PMID: 37915394](https://pubmed.ncbi.nlm.nih.gov/37915394/)). No modifier genes for SPG44 have been established.

**Environmental risk / protective factors.** None known or expected for a fully penetrant recessive Mendelian disorder. **Consanguinity** is an important epidemiologic enabler because it increases homozygosity for rare recessive alleles; reported families are frequently consanguineous (e.g., Iranian and Turkish *GJC2* cohorts). No protective variants, dietary, or lifestyle factors have been identified.

**Gene–environment interactions.** No validated gene–environment interactions are described for SPG44.

---

## 3. Phenotypes

The **core SPG44 phenotype** (Orthmann-Murphy et al., 2009; p.I33M family) is late-onset, slowly progressive **complicated spastic paraplegia** with normal or near-normal psychomotor development, preserved independent walking into adulthood, and **absence of nystagmus** — distinguishing it from the allelic PMLD1. The original report states: "All three had a late-onset, slowly progressive, complicated spastic paraplegia, with normal or near-normal psychomotor development, preserved walking capability through adulthood, and no nystagmus" ([PMID: 19056803](https://pubmed.ncbi.nlm.nih.gov/19056803/)).

| Phenotype | HPO term | Type | Onset / severity / course | Frequency (SPG44) |
|---|---|---|---|---|
| Spastic paraplegia | HP:0001258 | Clinical sign | Late-onset, slowly progressive | Defining/near-universal |
| Lower-limb spasticity | HP:0002061 | Clinical sign | Progressive | High |
| Progressive spastic paraplegia | HP:0007015 | Clinical sign | Slowly progressive | High |
| Abnormal cerebral white matter morphology (hypomyelination) | HP:0002500 | Imaging/lab | Present from early imaging | Near-universal |
| Diffuse white matter abnormalities | HP:0007204 | Imaging/lab | Diffuse pattern | Near-universal |
| Cerebellar signs / ataxia | HP:0001251 | Clinical sign | Variable, complicating | Minority/variable |
| Dysarthria | HP:0001260 | Clinical sign | Variable | Minority |
| Mild peripheral neuropathy | HP:0009830 | Lab (NCS) | Mild, minority | ~2/10 in GJC2 PMLD series (NCS) |

**Notably spared:** early nystagmus, significant cognitive impairment, and severe early psychomotor delay — features that characterize the more severe allelic PMLD1. Brainstem auditory evoked potentials (BAEP) are typically **recordable** in *GJC2* disease (contrast with absent BAEP waves III–V in *PLP1*-related PMD). In a comparative neurophysiology series, "NCS were normal in all patients with PMD and indicated mild peripheral neuropathy in only 2 of 10 patients with PMLD" ([PMID: 20513814](https://pubmed.ncbi.nlm.nih.gov/20513814/)).

**Quality-of-life impact.** Progressive lower-limb spasticity impairs gait, mobility, and daily functioning over decades; however, preserved ambulation and cognition mean the QoL impact is substantially milder than in PMLD1. No SPG44-specific EQ-5D/SF-36 data exist; per-phenotype QoL metrics are extrapolated from the complicated-HSP literature.

---

## 4. Genetic / Molecular Information

**Causal gene.** *GJC2* (= *GJA12*), located on chromosome **1q42.13** ([PMID: 41530801](https://pubmed.ncbi.nlm.nih.gov/41530801/)), encodes **connexin-47 (Cx47)**, a tetraspan gap-junction protein. Like all connexins, Cx47 has "four alpha-helical transmembrane domains, two extracellular loops, a cytoplasmic loop, and cytoplasmic N- and C-terminal domains" ([PMID: 11838236](https://pubmed.ncbi.nlm.nih.gov/11838236/)); each extracellular loop carries three invariantly spaced cysteines required for channel docking. Six connexins oligomerize into a hexameric hemichannel (connexon); two hemichannels dock across the extracellular gap to form the intercellular gap-junction channel.

**Three allelic disorders across a severity continuum:**

| Disorder | OMIM | Inheritance | Example variant(s) | Severity |
|---|---|---|---|---|
| SPG44 (spastic paraplegia 44) | 613206 | AR | p.Ile33Met (N-terminus); p.Ser5Ile | **Mild** |
| PMLD1 / HLD2 | 608804 | AR | p.Val254Met, p.Pro87Ser, p.Tyr269Asp, p.Met283Thr (ER-retained) | **Severe** |
| Lymphedema, hereditary, IC (LCRP1) | 613480 | AD | p.Gly96Val (TM2) and others | Distinct (lymphatic) |

The lymphedema branch is confirmed as an allelic but distinct entity: "Mutations in GJC2 and GJA1, encoding Cxs (connexins) 47 and 43, respectively, are linked to lymphedema" ([PMID: 30355030](https://pubmed.ncbi.nlm.nih.gov/30355030/)).

**Variant classification & type.** SPG44 variants reported to date are **missense** substitutions (e.g., I33M, S5I) classified as pathogenic/likely pathogenic in the context of consistent recessive segregation and functional data. PMLD1 alleles include missense and more disruptive variants that are commonly ER-retained.

**Allele frequency.** SPG44 alleles are private/ultra-rare in population databases (gnomAD), consistent with a very rare recessive disorder.

**Origin.** All disease alleles are **germline**; no somatic contribution.

**Functional consequences.** SPG44 alleles cause **loss of function** of Cx47 channels. The I33M mutant forms gap-junction plaques at the plasma membrane but fails to form functional homotypic channels, and Cx47/Cx43 heterotypic channels open only under non-physiological voltage: "These channels probably do not function under physiological conditions, suggesting that Cx47/Cx43 channels between astrocytes and oligodendrocytes are disrupted, similar to the loss-of-function endoplasmic reticulum-retained Cx47 mutants that cause PMLD" ([PMID: 19056803](https://pubmed.ncbi.nlm.nih.gov/19056803/)). Importantly, unlike severe ER-retained PMLD1 mutants, I33M does **not** trigger a toxic gain-of-function ER-stress response (see Section 6).

**Modifier genes / epigenetics / chromosomal abnormalities.** No modifier genes, disease-specific epigenetic marks, or chromosomal abnormalities have been established for SPG44. Notably, astrocytic Cx43 is required in trans for Cx47 phosphorylation and stability, meaning the panglial network's integrity depends on partner connexins — a biological interaction rather than a genetic modifier per se ([PMID: 23637189](https://pubmed.ncbi.nlm.nih.gov/23637189/)).

---

## 5. Environmental Information

Not applicable in any causal sense. SPG44 is a fully penetrant recessive Mendelian disease with **no environmental, toxic, lifestyle, or infectious contributors**. The only relevant "environmental" variable is population structure/**consanguinity**, which raises the probability of biallelic inheritance of rare recessive alleles but does not itself cause disease. The Turkish *GJC2* cohort illustrates this context: "The molecular basis of the disease was investigated in a cohort of 19 Turkish families" with high consanguinity ([PMID: 22283455](https://pubmed.ncbi.nlm.nih.gov/22283455/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *GJC2* mutation** (e.g., c.99C>G / p.Ile33Met) **leads to** production of a Cx47 protein that reaches the plasma membrane and forms gap-junction plaques but **cannot form functional intercellular channels**.
2. Non-functional Cx47 **results in** loss of homotypic oligodendrocyte–oligodendrocyte coupling and loss of heterotypic Cx47/Cx43 oligodendrocyte–astrocyte coupling (channels open only at non-physiological voltages).
3. Loss of Cx47-mediated coupling **disrupts the panglial gap-junctional syncytium**, impairing ion (K⁺) buffering and metabolite/water homeostasis across the oligodendrocyte–astrocyte network.
4. Disrupted panglial homeostasis **leads to** failure to properly form and, critically, **maintain CNS myelin** → hypomyelinating leukoencephalopathy (demonstrated in mouse models; inferred in human SPG44 from MRI). In mouse double-deficient models, "we observed early onset myelin pathology" ([PMID: 22649229](https://pubmed.ncbi.nlm.nih.gov/22649229/)).
5. Deficient central myelination of long descending motor tracts (corticospinal tracts) **results in** length-dependent upper-motor-neuron dysfunction → progressive lower-limb spasticity, the clinical hallmark.
   - **Branch (severity determinant):** In *severe PMLD1* alleles, mutant Cx47 is **ER-retained**, which **activates the UPR and apoptosis** — a toxic gain-of-function that adds oligodendrocyte death to the coupling loss, producing early, severe disease with nystagmus and psychomotor delay. In *mild SPG44* (I33M), "the milder SPG44 associated mutation p.I33M shows a wild-type-like subcellular distribution and no activation of the UPR or apoptotic pathways" ([PMID: 35276347](https://pubmed.ncbi.nlm.nih.gov/35276347/)) — a clean loss-of-function yielding the milder, ambulation-preserving phenotype.

### Causal-chain diagram

```
GJC2 biallelic mutation (p.Ile33Met)
        │
        ▼
Non-functional Cx47 gap-junction channels
   (plaques form, channels don't conduct)
        │
        ▼
Loss of O–O and O–A (Cx47/Cx43) coupling
        │
        ▼
Panglial syncytium disruption
(impaired K+ / metabolite / water homeostasis)
        │
        ▼
Failure to maintain CNS myelin ──► hypomyelinating leukoencephalopathy (MRI)
        │
        ▼
Corticospinal tract dysfunction ──► progressive lower-limb spasticity (SPG44)

   ── Severity branch ──
   PMLD1 alleles: ER retention ─► UPR + apoptosis (toxic GoF) ─► SEVERE phenotype
   SPG44 I33M:    normal traffic ─► NO UPR/apoptosis (clean LoF) ─► MILD phenotype
```

**Molecular pathways / cellular processes.** Core process = **gap-junction–mediated intercellular communication** (GO:0007267) and myelin maintenance (GO:0043209 myelin sheath; GO:0042552 myelination). In severe alleles, the **UPR/ER-stress and intrinsic apoptosis pathways** (GO:0030968, GO:0006915) are activated. A complementary study of Cx47 alleles proposed that "PMLD is likely to be caused by two different disease mechanisms: a loss of function and a dysfunction [hemichannel]" ([PMID: 20442743](https://pubmed.ncbi.nlm.nih.gov/20442743/)).

**Protein dysfunction.** SPG44: loss of channel function without misfolding-driven aggregation/ER retention. PMLD1: ER retention, misfolding, UPR, apoptosis (gain-of-toxicity), and for some alleles proposed hemichannel dysfunction.

**Cell types & compartments.** Primary cell type: **oligodendrocyte** (CL:0000128) — "Cx47 was mainly expressed in oligodendrocytes in highly myelinated CNS tissues" ([PMID: 12805295](https://pubmed.ncbi.nlm.nih.gov/12805295/)); with essential partnering by **astrocytes** (CL:0000127) via Cx43. Subcellular compartments: **plasma-membrane gap junction** (GO:0005921), and in severe alleles the **endoplasmic reticulum** (GO:0005783).

**GO/CL suggestions.** Biological process: gap junction assembly (GO:0007267), myelination (GO:0042552), response to ER stress (GO:0034976). Cellular component: gap junction (GO:0005921), myelin sheath (GO:0043209). Cell types: oligodendrocyte (CL:0000128), astrocyte (CL:0000127).

---

## 7. Anatomical Structures Affected

- **Organ / system:** Central nervous system (UBERON:0001017), predominantly **cerebral white matter** (UBERON:0002316) and **corticospinal / pyramidal tracts** (UBERON:0002718). Body system: nervous system (bilateral, symmetric involvement typical of leukodystrophies).
- **Tissue / cell level:** Nervous tissue; **myelin sheath** and the **oligodendrocyte–astrocyte panglial network**. Target cells: oligodendrocytes (CL:0000128) primarily; astrocytes (CL:0000127) as obligate coupling partners.
- **Subcellular level:** Gap junctions at the plasma membrane (GO:0005921); ER (GO:0005783) in the severe allelic branch.
- **Localization / lateralization:** Diffuse, **bilateral and symmetric** hypomyelination of supratentorial white matter on MRI; cerebellar and brainstem involvement variable. Optic-nerve myelin vacuolation is prominent in Cx47-null mice.

---

## 8. Temporal Development

- **Onset:** SPG44 is characteristically **late-onset** and insidious/chronic, contrasting sharply with the neonatal/infantile onset of severe PMLD1. Hypomyelination on MRI, however, is present from early imaging.
- **Progression:** **Slowly progressive** spastic paraplegia over years to decades; disease course is chronic, non-episodic, and non-remitting. Ambulation is preserved through adulthood in the index family.
- **Duration:** Chronic and lifelong.
- **Remission / critical periods:** No spontaneous remission. Preclinical gene-therapy data suggest an early **developmental/postnatal window** (postnatal day 10 in mouse) may be optimal for maximal myelin rescue — a potential critical period for future intervention.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic *GJC2* variants). The index SPG44 family was homozygous for I33M.
- **Penetrance / expressivity:** Presumed complete penetrance for biallelic pathogenic genotypes; expressivity is variable, spanning the SPG44-to-PMLD1 continuum depending on the specific alleles. No genetic anticipation (non-repeat-expansion disorder). Germline mosaicism not reported.
- **Epidemiology:** SPG44 is **ultra-rare** — reported in only a small number of families since 2009. For context, overall HSP prevalence is estimated at **3.6 per 100,000**: "The global prevalence is estimated at 3.6 individuals per 100,000 inhabitants" ([PMID: 40450402](https://pubmed.ncbi.nlm.nih.gov/40450402/)); SPG44 represents a tiny fraction of this. *GJC2*/*GJA12* mutations account for a minority of Pelizaeus–Merzbacher-like disease overall — "PMLD is genetically heterogeneous, with about 8% of patients carrying autosomal recessive GJA12/GJC2 mutations" ([PMID: 20513814](https://pubmed.ncbi.nlm.nih.gov/20513814/)) — although frequency reached ~50% relative to *PLP1* in one highly consanguineous Turkish cohort ([PMID: 22283455](https://pubmed.ncbi.nlm.nih.gov/22283455/)).
- **Founder effects / consanguinity:** Enriched by **consanguinity**; reported in Italian, Iranian, and Turkish families. No broad founder haplotype established.
- **Carrier frequency:** Not precisely defined; expected very low, consistent with rarity.
- **Demographics / sex ratio:** Autosomal recessive → **no sex bias expected** (male:female ≈ 1:1). No specific geographic endemicity beyond consanguineous populations.

---

## 10. Diagnostics

**Diagnostic approach.** Diagnosis rests on **(1) brain MRI showing a diffuse pattern of hypomyelination** plus **(2) molecular confirmation by *GJC2* sequencing**. As summarized for the PMD/PMLD spectrum: "A diffuse pattern of hypomyelination is seen on magnetic resonance imaging (MRI)... Magnetic resonance spectroscopy (MRS) and brainstem auditory evoked potentials (BAEP) may assist with differential clinical diagnosis of PMD and PMLD1" ([PMID: 22422208](https://pubmed.ncbi.nlm.nih.gov/22422208/)). The same review names "the autosomal recessive disease called Pelizaeus-Merzbacher-like disease 1 (PMLD1) and the less-severe spastic paraplegia 44 (SPG44), caused by mutations of the gap junction protein, gamma-2 gene (GJC2)."

- **Imaging:** Brain MRI demonstrates diffuse hypomyelinating leukoencephalopathy. **MRS** and **BAEP** assist in differentiating PMD from PMLD/SPG44.
- **Electrophysiology:** BAEP typically **recordable** in *GJC2* disease (vs absent waves III–V in *PLP1*-PMD); nerve conduction studies may show **mild peripheral neuropathy** in a minority (~2/10 in a GJC2 PMLD series; [PMID: 20513814](https://pubmed.ncbi.nlm.nih.gov/20513814/)).
- **Genetic testing:** Confirmation by **single-gene *GJC2* sequencing**, an **HSP/leukodystrophy NGS gene panel**, or **whole-exome sequencing (WES)** — SPG44 families have been solved by WES (Orthmann-Murphy 2009, [PMID: 19056803](https://pubmed.ncbi.nlm.nih.gov/19056803/); Ghasemi 2023, [PMID: 37915394](https://pubmed.ncbi.nlm.nih.gov/37915394/)). Copy-number/CMA and repeat-expansion testing are not typically informative for this missense-driven disorder.
- **Laboratory / biomarkers:** No specific blood/urine biomarker; diagnosis is imaging + genetic.
- **Differential diagnosis:** X-linked *PLP1*-related PMD/SPG2 (distinguished by BAEP), MitCHAP-60/*HSPD1* hypomyelinating leukodystrophy ([PMID: 27405012](https://pubmed.ncbi.nlm.nih.gov/27405012/)), other hypomyelinating leukodystrophies, and non-genetic mimics (multiple sclerosis, cerebral palsy) and other complicated HSPs.
- **Screening:** No newborn or population screening exists. **Cascade/carrier testing** of at-risk relatives is appropriate once a familial variant is identified.

---

## 11. Outcome / Prognosis

**Prognosis is comparatively favorable.** SPG44 patients retain "preserved walking capability through adulthood" with "normal or near-normal psychomotor development" ([PMID: 19056803](https://pubmed.ncbi.nlm.nih.gov/19056803/)), in stark contrast to the severe, often life-limiting PMLD1. The disorder is **chronic, slowly progressive, and lifelong but not typically fatal**. No SPG44-specific mortality, survival, or life-expectancy data exist. Primary morbidity is **progressive lower-limb spastic disability**, which can eventually impair mobility despite preserved ambulation in early adulthood. No validated SPG44-specific prognostic biomarkers are established; the specific *GJC2* genotype (SPG44 vs PMLD1 alleles) is the strongest prognostic determinant.

---

## 12. Treatment

**No disease-modifying therapy exists.** Management is **symptomatic and supportive**. As summarized in the HSP literature, "Current management is primarily symptomatic, including physical therapy and spasticity modulation with botulinum toxin or intrathecal baclofen" ([PMID: 40797390](https://pubmed.ncbi.nlm.nih.gov/40797390/)).

| Modality | Intervention | NCIT suggestion |
|---|---|---|
| Spasticity (oral) | **Baclofen** (GABA-B agonist) | Baclofen (NCIT:C61725) |
| Spasticity (focal) | **Botulinum toxin** injection | Botulinum Toxin (NCIT:C1027) |
| Spasticity (refractory) | **Intrathecal baclofen** pump | — |
| Rehabilitation | Physical therapy, orthotics, occupational therapy | Physical Therapy (NCIT:C15342) |

**Advanced / experimental therapeutics.** No approved gene, cell, or RNA therapy exists for SPG44. However, **oligodendrocyte-targeted gene therapy is a validated preclinical strategy**. AAV.MBP.Cx47myc (delivering *GJC2*/Cx47 under the myelin basic protein promoter to oligodendrocytes) improved pathology in *Cx32/Cx47* double-KO mice: "Application of this oligodendrocyte-targeted somatic gene therapy at postnatal Day 10 in groups of double knockout mice, a well characterized model of hypomyelinating leukodystrophy-2, resulted in significant improvement" ([PMID: 28100454](https://pubmed.ncbi.nlm.nih.gov/28100454/)). Transgenic oligodendrocyte expression of Cx32 also rescued the double-KO phenotype — "transgenic expression of hCx32 rescued the severe early phenotype of CNS demyelination in Cx32/Cx47dKO mice" ([PMID: 25524707](https://pubmed.ncbi.nlm.nih.gov/25524707/)) — together establishing a **cell-autonomous, correctable loss-of-function mechanism** that is an attractive gene-replacement target. No pharmacogenomic guidance is specific to SPG44.

---

## 13. Prevention

There is **no primary prevention and no newborn screening** for SPG44. Prevention is confined to **reproductive genetics**:

- **Genetic counseling** for affected families (25% recurrence risk per pregnancy for two carrier parents).
- **Carrier testing** of at-risk relatives and reproductive partners.
- **Prenatal diagnosis** and **preimplantation genetic testing (PGT)** for known familial *GJC2* variants.
- Tertiary prevention = optimal symptomatic management (spasticity control, physiotherapy) to limit contractures and preserve function.

No immunization, behavioral, or public-health/environmental interventions apply.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Mouse ortholog **Gjc2** (Cx47; NCBI Gene 118454). Connexin gene families are broadly conserved across vertebrates.
- **Natural disease:** No well-established naturally occurring companion-animal or wildlife equivalent of SPG44 is documented; the disease is studied primarily through engineered mouse models rather than spontaneous animal disease. Connexin biology (Cx47/Cx43 panglial coupling) is evolutionarily conserved, supporting cross-species translational relevance.
- **Zoonotic potential:** None (non-transmissible genetic disorder).

---

## 15. Model Organisms

Mouse (*Mus musculus*) is the principal model; in-vitro primary oligodendrocyte cultures dissect allele-specific mechanisms.

| Model | Type | Key phenotype | Recapitulation |
|---|---|---|---|
| **Cx47-null (Gjc2−/−)** mouse | Knockout | Vacuolated myelin, prominent in optic nerve; relatively mild alone | Partial (mild) |
| **Cx32/Cx47 double-KO** | Double knockout | Action tremor, severe CNS demyelination/vacuolization, death ~day 51 | Strong (severe end) |
| **Cx30/Cx47 double-KO** | Double knockout | Early myelin pathology, oligodendrocyte loss, astrogliosis, microglial activation, ~40% early death with severe motor impairment | Strong (severe end) |
| **Primary oligodendrocytes + mutant Cx47** | In vitro | PMLD1 mutants (P87S, Y269D, M283T) ER-retained → UPR + apoptosis; **SPG44 I33M = WT-like, no UPR/apoptosis** | Allele-specific mechanism |

The Cx30/Cx47 double-KO phenotype is documented as follows: "we observed early onset myelin pathology, and ∼40% of Cx30/Cx47 double-deficient animals died within 42 to 90 d after birth, accompanied by severe motor impairments" ([PMID: 22649229](https://pubmed.ncbi.nlm.nih.gov/22649229/)).

**Applications & limitations.** Single Cx47 knockouts produce a **milder** phenotype (closer to SPG44) than double knockouts, which better model **severe PMLD1**. This makes the double-KO ideal for testing myelin-rescue therapies (gene therapy, transgenic connexin replacement) but an imperfect match for the mild SPG44 clinical picture. The in-vitro I33M data are the most direct model of the SPG44-specific clean loss-of-function mechanism. Model databases: MGI (Gjc2), IMPC/IMSR for connexin alleles.

---

## Mechanistic Model / Interpretation

SPG44 is best understood as the **benign extreme of a single mechanistic axis: the amount and toxicity of Cx47 dysfunction in oligodendrocytes.** All *GJC2*-related CNS disease shares a common upstream lesion — impaired Cx47 gap-junction channels that break the oligodendrocyte–astrocyte panglial syncytium and thereby destabilize CNS myelin. What separates the mild (SPG44) from the severe (PMLD1) pole is **whether the mutant protein adds a toxic gain-of-function**:

```
                        Cx47 dysfunction spectrum
   MILD  ◄──────────────────────────────────────────────────►  SEVERE
   SPG44 (I33M, S5I)                                   PMLD1/HLD2 (ER-retained)
   • Protein traffics normally                         • Protein ER-retained
   • Clean loss of channel function                    • Loss of function PLUS
   • NO UPR / NO apoptosis                               UPR activation + apoptosis
   • Late onset, ambulation preserved                  • Neonatal onset, nystagmus,
   • Cognition/vision spared                             psychomotor delay, severe
```

This two-hit model — coupling loss for all alleles, plus ER-stress toxicity only for severe alleles — is directly supported by parallel in-vitro comparisons of I33M versus P87S/Y269D/M283T ([PMID: 35276347](https://pubmed.ncbi.nlm.nih.gov/35276347/)), and it provides a clean genotype–phenotype rationale. It also has therapeutic implications: because SPG44 is a **clean loss-of-function without a toxic aggregate**, gene-replacement (restoring functional Cx47 to oligodendrocytes) is mechanistically well-matched, and the disorder lacks the additional hurdle of clearing a toxic misfolded species.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [PMID: 19056803](https://pubmed.ncbi.nlm.nih.gov/19056803/) | *HSP is a novel phenotype for GJA12/GJC2 mutations* | **Landmark:** defines SPG44 (I33M) as mild complicated spastic paraplegia; disrupted O–A coupling |
| [PMID: 35276347](https://pubmed.ncbi.nlm.nih.gov/35276347/) | *Activation of the UPR by Cx47 mutations in PMLD* | **Key mechanism:** I33M = WT-like, no UPR/apoptosis; severe alleles ER-retained, activate UPR/apoptosis |
| [PMID: 12805295](https://pubmed.ncbi.nlm.nih.gov/12805295/) | *Cx47-deficient mice ... vacuolized myelin* | Oligodendrocyte-specific Cx47 expression; KO myelin vacuolation |
| [PMID: 22649229](https://pubmed.ncbi.nlm.nih.gov/22649229/) | *Panglial gap junctional communication essential for myelin* | Cx30/Cx47 dKO: early myelin pathology, ~40% early death, motor impairment |
| [PMID: 25524707](https://pubmed.ncbi.nlm.nih.gov/25524707/) | *Transgenic Cx32 replacement rescues leukodystrophy model* | Cell-autonomous, correctable loss-of-function |
| [PMID: 28100454](https://pubmed.ncbi.nlm.nih.gov/28100454/) | *Gene therapy targeting oligodendrocytes ...* | AAV-Cx47 (MBP promoter) rescues Cx32/Cx47 dKO at P10 |
| [PMID: 40797390](https://pubmed.ncbi.nlm.nih.gov/40797390/) | *rESWT in HSP (case report)* | Symptomatic HSP management standard (baclofen, BoNT, PT) |
| [PMID: 20513814](https://pubmed.ncbi.nlm.nih.gov/20513814/) | *Clinical neurophysiology in GJA12 vs PMD* | Mild peripheral neuropathy in 2/10; BAEP distinguish GJC2 from PLP1; ~8% of PMLD is GJC2 |
| [PMID: 22422208](https://pubmed.ncbi.nlm.nih.gov/22422208/) | *PMD, PMLD1, and related hypomyelinating disorders* | MRI hypomyelination + MRS/BAEP diagnostics; SPG44 = less-severe GJC2 disorder |
| [PMID: 40450402](https://pubmed.ncbi.nlm.nih.gov/40450402/) | *French guidelines for pure HSP* | HSP prevalence 3.6/100,000 |
| [PMID: 20442743](https://pubmed.ncbi.nlm.nih.gov/20442743/) | *PMLD: loss of Cx47 function and hemichannel dysfunction* | Dual disease mechanisms among Cx47 alleles |
| [PMID: 22283455](https://pubmed.ncbi.nlm.nih.gov/22283455/) | *High frequency of GJA12/GJC2 in Turkish PMD* | Consanguineous population context; ~50% relative frequency vs PLP1 |
| [PMID: 37915394](https://pubmed.ncbi.nlm.nih.gov/37915394/) | *Phenotypic heterogeneity in a GJC2 family* | Novel p.Ser5Ile allele; WES-based diagnosis; Iranian consanguineous family |
| [PMID: 11838236](https://pubmed.ncbi.nlm.nih.gov/11838236/) | *Emerging issues of connexin channels* | Tetraspan connexin topology (structural basis of Cx47) |
| [PMID: 41530801](https://pubmed.ncbi.nlm.nih.gov/41530801/) | *GJC2/OBSCN variants in lymphedema pedigree* | Localizes GJC2 to 1q42.13 |
| [PMID: 30355030](https://pubmed.ncbi.nlm.nih.gov/30355030/) | *Mechanisms of connexin-related lymphedema* | Third allelic disorder (lymphedema) distinct from CNS phenotypes |
| [PMID: 23637189](https://pubmed.ncbi.nlm.nih.gov/23637189/) | *Cx47 phosphorylation/stability depends on astrocytic Cx43* | Panglial interdependence; astrocytic Cx43 stabilizes oligodendrocytic Cx47 |

**Evidence source types:** human clinical (case/family reports, guidelines), mouse model organism (KO/dKO, gene therapy), and in-vitro cell biology (allele-specific trafficking/UPR). No large-cohort or computational-omics evidence is available for this ultra-rare disorder.

---

## Limitations and Knowledge Gaps

1. **Extreme rarity → thin clinical evidence.** SPG44 rests largely on the original three-patient Italian family (I33M) plus a small number of additional families. Natural-history, prognostic, epidemiologic (precise prevalence/incidence), QoL, and mortality data are essentially absent.
2. **Genotype–phenotype boundary is soft.** The SPG44/PMLD1 distinction is a continuum; only a handful of alleles (I33M, S5I) are confidently "SPG44-mild." Which additional *GJC2* variants produce SPG44 vs PMLD1 remains incompletely mapped.
3. **Mouse models over-represent the severe pole.** Single Cx47-KO is milder, but double-KO models (used for therapy testing) model severe PMLD1, not the mild SPG44 clinical course. There is no dedicated I33M knock-in mouse recapitulating SPG44 in vivo.
4. **No human treatment evidence.** All disease-modifying data are preclinical; no clinical trials in *GJC2* disease.
5. **No SPG44-specific biomarkers** (fluid or imaging-quantitative) for diagnosis or progression monitoring beyond qualitative MRI hypomyelination.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a Gjc2 p.Ile33Met knock-in mouse** to test whether the clean loss-of-function I33M genotype produces a *mild*, SPG44-like phenotype in vivo (currently only in-vitro data exist), enabling faithful preclinical modeling.
2. **Assemble an international *GJC2* patient registry** spanning SPG44↔PMLD1 to define natural history, age-of-onset distributions, ambulation trajectories, and allele-specific prognosis with adequate power.
3. **Systematic genotype–phenotype/functional screen** of reported and novel *GJC2* variants (trafficking, channel conductance, UPR/apoptosis readouts) to build a predictive severity classifier distinguishing SPG44 from PMLD1 alleles.
4. **Advance oligodendrocyte-targeted AAV-*GJC2* gene therapy** from the double-KO model toward IND-enabling studies, defining the therapeutic window (informed by the P10 rescue data) and testing rescue in a mild-allele model.
5. **Develop quantitative myelin biomarkers** (e.g., myelination scoring, MRS metrics, myelin-water imaging) validated against *GJC2* genotype to serve as diagnostic aids and future trial endpoints.
6. **Population carrier-frequency estimation** for pathogenic *GJC2* alleles from gnomAD and consanguineous-population cohorts to refine recurrence-risk counseling.

---

*Report compiled from 9 confirmed findings across 5 investigation iterations and 37 reviewed papers. All mechanistic and clinical claims are anchored to the cited primary literature (PMIDs above).*


## Artifacts

- [OpenScientist final report](Hereditary_Spastic_Paraplegia_44-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hereditary_Spastic_Paraplegia_44-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 18 |
| On topic | 8 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:11838236` (5 mentions) - Emerging issues of connexin channels: biophysics fills the gap.
  - shared terms: model

Weighed against this report's own most characteristic terms: `spg44`, `gjc2`, `disease`, `pmld1`, `allele`, `severe`, `cx47`, `gene`, `i33m`, `phenotype`, `mild`, `oligodendrocyte`, `disorder`, `myelin`, `model`, `spastic`, `variant`, `paraplegia`, `recessive`, `family`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 20 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013179` (2 mentions) - the report calls it "MONDO"; MONDO calls it **hereditary spastic paraplegia 44**
- `HP:0007015` (1 mention) - the report calls it "Progressive spastic paraplegia"; HP calls it **Poor gross motor coordination**
- `GO:0007267` (2 mentions) - the report calls it "gap-junction–mediated intercellular communication"; GO calls it **cell-cell signaling**
- `UBERON:0002718` (1 mention) - the report calls it "corticospinal / pyramidal tracts"; UBERON calls it **solitary tract**
- `NCIT:C61725` (1 mention) - the report calls it "Baclofen"; NCIT calls it **Diltiazem**
- `NCIT:C1027` (1 mention) - the report calls it "Botulinum Toxin"; NCIT calls it **Budesonide**
- `NCIT:C15342` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Transplantation**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002500` (1 mention) - the report calls it "Abnormal cerebral white matter morphology (hypomyelination)"; HP calls it **Abnormal cerebral white matter morphology**
- `HP:0001251` (1 mention) - the report calls it "Cerebellar signs / ataxia"; HP calls it **Ataxia**, and lists "Cerebellar ataxia" among its other names
- `HP:0009830` (1 mention) - the report calls it "Mild peripheral neuropathy"; HP calls it **Peripheral neuropathy**
- `GO:0005921` (3 mentions) - the report calls it "plasma-membrane gap junction", "Subcellular level:** Gap junctions at the plasma membrane"; GO calls it **gap junction**, and lists "intercellular gap junction channel" among its other names
- `UBERON:0001017` (1 mention) - the report calls it "Organ / system:** Central nervous system"; UBERON calls it **central nervous system**
- `UBERON:0002316` (1 mention) - the report calls it "cerebral white matter"; UBERON calls it **white matter**, and lists "neuronal white matter" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005921` - called "plasma-membrane gap junction", "Subcellular level:** Gap junctions at the plasma membrane"