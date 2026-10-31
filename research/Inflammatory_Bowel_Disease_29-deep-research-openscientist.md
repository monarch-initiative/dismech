---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T03:57:09.537147'
end_time: '2026-10-31T04:52:36.759620'
duration_seconds: 3327.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Inflammatory Bowel Disease 29
  mondo_id: MONDO:0054849
  category: Mendelian
  causal_genes: INAVA
  omim_id: OMIM:618077
  synonyms: not recorded
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
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 5
  relevance_assessed: 12
  on_topic: 6
  validator_version: 0.4.0
term_validation:
  total_terms: 50
  verified: 47
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 41
  labels_matching: 13
  labels_mismatched: 22
  mislabelled_terms:
  - term_id: MONDO:0054849
    reported_labels:
    - MONDO
    - inflammatory bowel disease 29
    ontology_label: inflammatory bowel disease 29
  - term_id: HP:0002028
    reported_labels:
    - Symptom
    ontology_label: Chronic diarrhea
  - term_id: HP:0002573
    reported_labels:
    - Sign
    ontology_label: Hematochezia
  - term_id: HP:0002027
    reported_labels:
    - Symptom
    ontology_label: Abdominal pain
  - term_id: HP:0001824
    reported_labels:
    - Sign
    ontology_label: Weight loss
  - term_id: HP:0002024
    reported_labels:
    - Lab/clinical
    ontology_label: Malabsorption
  - term_id: HP:0100275
    reported_labels:
    - Physical manifestation
    ontology_label: Diffuse cerebellar atrophy
  - term_id: HP:0011227
    reported_labels:
    - Lab abnormality
    ontology_label: Elevated circulating C-reactive protein concentration
  - term_id: HP:0003565
    reported_labels:
    - Lab abnormality
    ontology_label: Elevated erythrocyte sedimentation rate
  - term_id: HP:0001903
    reported_labels:
    - Lab abnormality
    ontology_label: Anemia
  - term_id: HP:0001369
    reported_labels:
    - Extraintestinal
    ontology_label: Arthritis
  - term_id: HP:0000554
    reported_labels:
    - Extraintestinal
    ontology_label: Uveitis
  - term_id: HP:0012219
    reported_labels:
    - Extraintestinal
    ontology_label: Erythema nodosum
  - term_id: HP:0030151
    reported_labels:
    - Extraintestinal
    ontology_label: Cholangitis
  - term_id: GO:0036464
    reported_labels:
    - cytosolic biomolecular condensates
    ontology_label: cytoplasmic ribonucleoprotein granule
  - term_id: NCIT:C29281
    reported_labels:
    - aminosalicylic acid class
    ontology_label: Nafcillin Sodium
  - term_id: NCIT:C442
    reported_labels:
    - corticosteroid
    ontology_label: Dioxin Compound
  - term_id: NCIT:C569
    reported_labels:
    - immunosuppressant
    ontology_label: IgM
  - term_id: NCIT:C1965
    reported_labels:
    - infliximab
    ontology_label: Lutein
  - term_id: NCIT:C90555
    reported_labels:
    - vedolizumab
    ontology_label: CEA/Tetanus Toxoid T Helper Epitope Fusion Protein-Expressing
      DNA Plasmid Vaccine
  - term_id: NCIT:C82407
    reported_labels:
    - ustekinumab
    ontology_label: pTVG-HP Plasmid DNA Vaccine
  - term_id: NCIT:C116834
    reported_labels:
    - tofacitinib, upadacitinib
    ontology_label: CNS 2
  labels_variant: 6
  obsolete_terms:
  - term_id: GO:0032088
    ontology_label: obsolete negative regulation of NF-kappaB transcription factor
      activity
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Inflammatory_Bowel_Disease_29-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Inflammatory_Bowel_Disease_29-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inflammatory Bowel Disease 29
- **MONDO ID:** MONDO:0054849 (if available)
- **Causal gene(s):** INAVA
- **OMIM:** OMIM:618077
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Inflammatory Bowel Disease 29** covering all of the
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

# Inflammatory Bowel Disease 29 (IBD29): A Comprehensive Disease Characteristics Report

**Disease:** Inflammatory Bowel Disease 29 (IBD29)
**MONDO ID:** MONDO:0054849 · **OMIM:** 618077 · **Causal gene:** **INAVA** (Innate Immunity Activator; formerly *C1orf106*; HGNC:25599; UniProt Q3KP66; Entrez 55765; Ensembl ENSG00000163362; locus 1q32.1)

---

## Summary

**Inflammatory Bowel Disease 29 (IBD29; OMIM 618077; MONDO:0054849) is a multifactorial, polygenic susceptibility form of inflammatory bowel disease caused by variation in the gene INAVA** (Innate Immunity Activator, formerly named *C1orf106*). It is not a distinct clinical syndrome with a unique presentation; rather, it is a molecularly defined genetic contribution to common IBD, so affected individuals present clinically as either **Crohn disease (CD)** or **ulcerative colitis (UC)**. UniProt curates the entry as disease variant DI-05306: "susceptibility associated with variants affecting the gene." Two variants anchor the genetic architecture: a common intronic regulatory SNP **rs7554511** (risk allele C) that lowers INAVA transcription and expression, and a rare coding missense variant **p.Tyr333Phe (rs41313912)** that destabilizes the protein.

INAVA encodes a **dual-function cytoplasmic/nuclear scaffold protein** that sits at the intersection of two processes central to IBD pathogenesis: the intestinal epithelial barrier and innate immune signaling. In **epithelial cells**, INAVA stabilizes adherens and tight junctions by restraining cytohesin-1/ARNO–driven ARF6 activation and by organizing cortical actin through a ROCK-dependent mechanism; loss of INAVA produces a "leaky gut" with increased permeability and heightened sensitivity to TNF-α and enteric pathogens. In **myeloid cells (macrophages)**, INAVA is required for optimal pattern-recognition-receptor (PRR)–induced MAPK and NF-κB activation, cytokine secretion, and intracellular bacterial clearance, acting through recruitment of 14-3-3τ and amplification of TRAF6-dependent polyubiquitination within biomolecular condensates. The IBD-risk genotypes reduce both functions, so that ordinary microbial exposure in a genetically susceptible gut is converted into **chronic, relapsing mucosal inflammation**.

There is **no INAVA-specific therapy**; IBD29 is managed with standard IBD pharmacotherapy (5-aminosalicylates, corticosteroids, immunomodulators, and biologics such as anti-TNF agents). A pharmacogenomic signal links *C1orf106* polymorphisms to variability in infliximab trough levels, and the underlying cell biology nominates druggable nodes (p38α, mTOR, and Rho-ROCK pathways) that shift INAVA between its inflammatory-condensate and barrier-promoting functions. This report synthesizes seven confirmed findings from five iterations of investigation, grounded in six primary mechanistic/clinical papers.

---

## 1. Disease Information

**Overview.** IBD29 is a Mendelian-registry-labeled but mechanistically **polygenic/multifactorial susceptibility** form of inflammatory bowel disease. The number "29" is a serial OMIM susceptibility-locus designation and does **not** indicate a distinct clinical phenotype; the "IBD##" series catalogs genes and loci that confer susceptibility to CD and/or UC. For IBD29 the responsible gene is **INAVA / C1orf106**. Affected individuals present with the standard spectrum of chronic relapsing intestinal inflammation (CD or UC).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | 618077 |
| MONDO | MONDO:0054849 |
| Causal gene | INAVA (HGNC:25599; Entrez 55765; Ensembl ENSG00000163362) |
| UniProt (protein) | Q3KP66 (663 aa) |
| UniProt disease | DI-05306 |
| Cytogenetic locus | 1q32.1 |
| MeSH (parent) | Inflammatory Bowel Diseases (D015212) |
| ICD-10 | K50 (Crohn disease) / K51 (ulcerative colitis) — IBD29 inherits the code of the manifesting subtype |
| ICD-11 | DD70 (Crohn disease) / DD71 (ulcerative colitis) |

**Synonyms / alternative names.** The causal gene has been known as *C1orf106* (chromosome 1 open reading frame 106) and *INAVA*. No disease-specific synonyms are recorded for IBD29 beyond "inflammatory bowel disease 29" and the OMIM designation; the clinical presentations are referred to by their subtype names (Crohn disease, ulcerative colitis).

**Source of information.** The information is derived from **aggregated, disease-level and gene-level resources** (OMIM, UniProt, HGNC, GWAS meta-analyses) and from **mechanistic studies in human macrophages, human intestinal epithelial cells, patient-derived hiPSC intestinal spheroids, and knockout mice**, rather than from a single patient EHR cohort.

**MONDO term suggestion:** MONDO:0054849 (inflammatory bowel disease 29); parent MONDO:0005265 (inflammatory bowel disease).

---

## 2. Etiology

**Primary causes.** IBD29 is **genetically driven susceptibility acting in concert with the gut microbial environment**. It is not infectious or toxin-caused in a classical sense; rather, inherited reduction of INAVA function lowers two protective barriers — epithelial integrity and myeloid antimicrobial signaling — so that the normal luminal microbiota triggers and sustains inflammation (gene–environment interaction).

**Genetic risk factors.**
- **rs7554511** — common intronic tag SNP at 1q32.1 (GRCh38 chr1:200,908,434 C>A). The **risk allele is C (the common allele)**; the minor allele A has MAF ≈ 0.21 in European gnomAD/TOPMED and ≈ 0.14 globally. Risk carriers (rs7554511-C) express **lower INAVA RNA and protein**, attributable to decreased transcription driven by the intronic region containing the C variant ([PMID: 28436939](https://pubmed.ncbi.nlm.nih.gov/28436939/)).
- **p.Tyr333Phe (rs41313912)** — rare coding missense variant (NC_000001.11:g.200908897A>G/T), UniProt feature VAR_080249, annotated "in IBD29; decreases protein stability." Minor-allele (T) frequency ≈ 0.4% in 1000 Genomes, ≈ 1% in ALFA.
- The INAVA/C1orf106 locus was identified in genome-wide association meta-analyses of IBD and sits within the broader polygenic IBD risk architecture (>240 IBD loci known).

**Environmental risk factors (general IBD, applicable to IBD29).** Enteric microbial exposure/dysbiosis, smoking (risk factor for CD, protective for UC), diet (Western, low-fiber), NSAID use, enteric infections, and early-life antibiotic exposure. Food insecurity is associated with higher odds of IBD (adjusted OR 1.78, 95% CI 1.42–2.23; [PMID: 42847277](https://pubmed.ncbi.nlm.nih.gov/42847277/)). Family history and sex are standard demographic modifiers of IBD risk.

**Protective factors.** The ancestral/minor allele of rs7554511 (A) is associated with higher INAVA expression and thus lower risk. No INAVA-specific environmental protective factor is established. In general IBD, breastfeeding, high dietary fiber, and (for UC) smoking and appendectomy are reported protective associations; the evidence for a protective role of *Helicobacter pylori* in IBD remains inconsistent ([PMID: 42895565](https://pubmed.ncbi.nlm.nih.gov/42895565/)).

**Gene–environment interaction.** The mechanistic core of IBD29 is a GxE interaction: reduced INAVA function is clinically silent until the epithelium is challenged. C1orf106-deficient mice are **hypersensitive to TNF-α–induced increases in epithelial permeability** and show increased susceptibility to intestinal pathogens — i.e., the phenotype emerges on microbial/cytokine challenge ([PMID: 29420262](https://pubmed.ncbi.nlm.nih.gov/29420262/); [PMID: 31022698](https://pubmed.ncbi.nlm.nih.gov/31022698/)).

---

## 3. Phenotypes

Because IBD29 manifests as CD or UC, its phenotype spectrum is that of IBD. Core and extraintestinal phenotypes with suggested HPO terms:

| Phenotype | Type | HPO term | Typical characteristics |
|---|---|---|---|
| Chronic diarrhea | Symptom | HP:0002028 | Childhood–adult onset; episodic/relapsing; very common |
| Hematochezia / bloody stool | Sign | HP:0002573 | Prominent in UC; relapsing |
| Abdominal pain | Symptom | HP:0002027 | Common; fluctuating |
| Weight loss | Sign | HP:0001824 | Moderate–severe in active CD |
| Malabsorption | Lab/clinical | HP:0002024 | More in CD (small-bowel) |
| Intestinal/perianal fistula | Physical manifestation | HP:0100275 | CD complication (penetrating, B3) |
| Intestinal obstruction | Physical manifestation | HP:0005214 | CD stricturing (B2) |
| Elevated CRP | Lab abnormality | HP:0011227 | Tracks disease activity |
| Elevated ESR | Lab abnormality | HP:0003565 | Tracks disease activity |
| Anemia | Lab abnormality | HP:0001903 | Iron-deficiency / chronic disease |
| Arthritis | Extraintestinal | HP:0001369 | Peripheral/axial |
| Uveitis | Extraintestinal | HP:0000554 | Ocular |
| Erythema nodosum | Extraintestinal | HP:0012219 | Cutaneous |
| Primary sclerosing cholangitis | Extraintestinal | HP:0030151 | Hepatobiliary (esp. UC) |
| Increased colorectal cancer risk | Complication | HP:0003003 | Long-standing colitis |

**Onset / severity / progression / frequency.** Onset is most often in adolescence/young adulthood with a second smaller peak later in life; severity is **variable**; the course is characteristically **relapsing-remitting (episodic)**. Frequencies above are qualitative for IBD at large (no IBD29-genotype-stratified phenotype frequencies are published).

**Quality-of-life impact.** IBD substantially reduces health-related quality of life; developmental, emotional, and cognitive factors modulate subjective symptom burden ([PMID: 42652338](https://pubmed.ncbi.nlm.nih.gov/42652338/)). Fatigue, urgency, diet restriction, and psychosocial burden are major contributors.

---

## 4. Genetic / Molecular Information

**Causal gene.** **INAVA (C1orf106)**, 1q32.1; Entrez 55765; HGNC:25599; UniProt Q3KP66 (663 aa); Ensembl ENSG00000163362.

**Protein features.** INAVA contains a **coiled-coil region (aa 118–147)**, **three nuclear localization signals**, large **intrinsically disordered regions**, and a bifunctional **DUF3338 domain renamed CUPID**. It localizes to both cytoplasm and nucleus and translocates to the nucleus upon NOD2 stimulation.

**Pathogenic / risk variants.**

| Variant | rsID | Type | Classification | Frequency | Functional consequence |
|---|---|---|---|---|---|
| Intronic tag SNP (risk allele C) | rs7554511 | Regulatory (intronic) | Common risk allele | minor allele A MAF ~0.21 EUR, ~0.14 global | ↓ transcription → ↓ INAVA RNA/protein (loss-of-function-leaning) |
| p.Tyr333Phe | rs41313912 | Missense (coding) | "in IBD29" (UniProt VAR_080249) | minor allele T ~0.4% 1000G, ~1% ALFA | ↓ protein stability; ↑ ubiquitination/turnover (loss of function) |

- **Somatic vs germline:** germline susceptibility variants (not somatic).
- **Functional consequence:** both variants converge on **reduced INAVA function/dosage** — rs7554511-C lowers expression; p.Y333F destabilizes the protein. The IBD-risk coding variant **increases C1orf106 ubiquitination and turnover with consequent functional impairments** ([PMID: 29420262](https://pubmed.ncbi.nlm.nih.gov/29420262/)).

**Modifier genes.** No INAVA-specific modifier genes are established; IBD29 operates within the broader polygenic IBD background (NOD2, IL23R, ATG16L1, IL10, etc.).

**Epigenetic information.** No IBD29/INAVA-specific DNA-methylation or histone-modification data are established; the rs7554511 effect is transcriptional/regulatory.

**Chromosomal abnormalities.** None described for IBD29; it is a single-gene susceptibility locus, not a structural/aneuploidy disorder.

**Gene/GO annotation suggestions:** INAVA (HGNC:25599); GO:0032088 (negative regulation of NF-κB), GO:0038061 (NIK/NF-κB signaling), GO:0007010 (cytoskeleton organization), GO:0045216 (cell-cell junction organization).

---

## 5. Environmental Information

- **Environmental factors.** The dominant environmental input is the **enteric microbiota**; INAVA loss increases susceptibility to intestinal pathogens and impairs intracellular bacterial clearance in macrophages. No specific toxin/radiation/occupational exposure is implicated for IBD29 beyond general IBD risk factors.
- **Lifestyle factors.** General IBD lifestyle associations apply: smoking (divergent for CD vs UC), Western diet, NSAIDs, stress; food insecurity associated with higher IBD odds ([PMID: 42847277](https://pubmed.ncbi.nlm.nih.gov/42847277/)).
- **Infectious agents.** No single pathogen causes IBD29. The commensal/pathobiont microbiota acts as the environmental trigger converting genetic susceptibility to inflammation; enteric pathogens precipitate barrier breakdown in INAVA-deficient models.

**CHEBI suggestion:** tumor necrosis factor (challenge agent in models); lipopolysaccharide (PRR ligand); muramyl dipeptide (NOD2 ligand).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Inheritance of an INAVA risk genotype** (rs7554511-C lowering expression, and/or p.Y333F destabilizing the protein) → **leads to** reduced functional INAVA protein dosage in intestinal epithelial and myeloid cells. *(Demonstrated: expression and stability data, PMIDs 28436939, 29420262.)*

2. **Branch A — Epithelial barrier arm.** Reduced INAVA → **fails to restrain** cytohesin-1–dependent ARF6 activation (INAVA normally promotes cytohesin-1 degradation) and **impairs** CUPID–ARNO-driven lateral-membrane F-actin assembly and ROCK-dependent cortical actin-belt dynamics → **results in** destabilized adherens/tight junctions, defective cell polarity and migration → **leads to** increased intestinal epithelial permeability ("leaky gut"). *(Demonstrated: PMIDs 29420262, 30355448, 40161582.)*

3. **Branch B — Myeloid innate-immune arm.** Reduced INAVA → **fails to recruit** 14-3-3τ and **fails to amplify** TRAF6-dependent polyubiquitination within IL-1β-induced biomolecular condensates → **results in** sub-optimal MAPK and NF-κB activation, reduced cytokine secretion, and **impaired intracellular bacterial clearance**. *(Demonstrated: PMIDs 28436939, 30355448, 34251416.)*

4. **Convergence under microbial/cytokine challenge.** Leaky epithelium (Branch A) **permits** increased luminal-microbe translocation; impaired myeloid clearance (Branch B) **fails to eliminate** translocated microbes → **leads to** persistent antigenic/microbial stimulation of the lamina propria. *(Inferred synthesis of both arms, supported by TNF-α hypersensitivity in vivo, PMID 31022698.)*

5. **Persistent stimulation → leads to** chronic mucosal immune activation, cytokine-driven tissue injury, and the relapsing-remitting clinical phenotype of CD/UC. *(Inferred from model phenotypes + IBD pathophysiology.)*

### Mechanistic detail by category

- **Molecular pathways.** Cytohesin-1/ARNO → **ARF6** GTPase signaling (junctional actin); **Rho–ROCK** (cortical actin belt); **MAPK** and **NF-κB** (PRR-driven inflammation); **TRAF6** polyubiquitination; **p38α/MAPK** and **mTOR** (condensate dynamics).
- **Cellular processes.** Cell–cell junction assembly (GO:0034329), actin cytoskeleton organization (GO:0030036), cell polarity/migration, inflammatory signaling, intracellular bacterial killing, biomolecular-condensate (liquid–liquid phase separation) assembly and resolution.
- **Protein dysfunction.** p.Y333F is a **destabilizing loss-of-function** variant (increased ubiquitination/turnover); rs7554511-C causes **reduced dosage**. INAVA is a bifunctional scaffold; the CUPID/DUF3338 domain mediates both the barrier (ARNO binding) and inflammatory (TRAF6 amplification) activities.
- **Immune system involvement.** Defective innate antimicrobial response in macrophages (PRR→MAPK/NF-κB, bacterial clearance) rather than classical autoimmunity; downstream chronic inflammation.
- **Tissue-damage mechanisms.** Barrier failure → microbial translocation → sustained inflammation → mucosal injury; TNF-α amplifies permeability.
- **Molecular profiling.** Risk-allele macrophages show lower INAVA RNA/protein and reduced PRR-induced cytokines ([PMID: 28436939](https://pubmed.ncbi.nlm.nih.gov/28436939/)); INAVA condensates contain ubiquitin and E3 ligase βTrCP2 ([PMID: 34251416](https://pubmed.ncbi.nlm.nih.gov/34251416/)).

### Causal-chain diagram

```
 INAVA risk genotype (rs7554511-C ↓expr; p.Y333F ↓stability)
                    │  ↓ functional INAVA
        ┌───────────┴─────────────┐
   BRANCH A (epithelium)      BRANCH B (macrophage)
   ↑cytohesin-1→↑ARF6         ↓14-3-3τ recruitment
   ↓CUPID-ARNO F-actin        ↓TRAF6 ubiquitination (condensates)
   ↓ROCK actin belt           ↓MAPK/NF-κB, ↓cytokines
        │                         │
  junction instability      impaired bacterial clearance
        │                         │
   ↑epithelial permeability  microbes not eliminated
        └──────────┬──────────────┘
          microbial translocation + persistence
                    │  (× TNF-α, enteric challenge)
          chronic lamina propria inflammation
                    │
            Crohn disease / ulcerative colitis
```

**GO/CL term suggestions:** GO:0043123 (positive regulation of NF-κB), GO:0007015 (actin filament organization), GO:0034329 (cell junction assembly), GO:0071345 (cellular response to cytokine stimulus); CL:0000235 (macrophage), CL:0002253 (epithelial cell of large intestine), CL:0000160 (goblet cell).

---

## 7. Anatomical Structures Affected

- **Organ level.** Primary: **intestine** (colon and/or small bowel) — UBERON:0000160 (intestine), UBERON:0001155 (colon), UBERON:0002108 (small intestine). Secondary/complication: perianal region (fistulae), hepatobiliary tract (PSC), joints, eyes, skin. Body system: **digestive system** (UBERON:0001007), with immune-system involvement.
- **Tissue / cell level.** Intestinal **epithelium** (UBERON:0001277 intestinal mucosa; UBERON:0000483 epithelium) and **lamina propria** immune infiltrate. Key cells: **intestinal epithelial cells** (CL:0002253), **macrophages** (CL:0000235), and junction-forming enterocytes.
- **Subcellular level.** INAVA localizes to **cytoplasm** and **nucleus** (GO:0005737, GO:0005634); functions at the **lateral plasma membrane / cell–cell junction** (GO:0016323, GO:0005912 adherens junction) and in **cytosolic biomolecular condensates** (GO:0036464).
- **Localization / lateralization.** Mucosal inflammation is typically **patchy/segmental in CD** and **continuous, diffuse colonic in UC**; not a lateralized disease.

---

## 8. Temporal Development

- **Onset.** Chronic/insidious; most commonly adolescence to young adulthood, consistent with IBD. No IBD29-specific age-of-onset data beyond general IBD.
- **Progression.** CD can progress from inflammatory (B1) to stricturing (B2) or penetrating (B3) behavior; UC can extend proximally. Progression rate is **variable**.
- **Course pattern.** Characteristically **relapsing-remitting (episodic)**; chronic lifelong.
- **Remission.** Both spontaneous and, more reliably, **treatment-induced** remission occur.
- **Critical periods / intervention windows.** Early effective control of inflammation ("treat-to-target") and barrier protection are the principal opportunities; mechanistically, challenge-dependent barrier failure suggests windows around enteric infection/antibiotic exposure.

---

## 9. Inheritance and Population

- **Epidemiology.** IBD29 has no separate prevalence/incidence; it contributes to the IBD population. IBD affects **>7 million people worldwide**; incidence has plateaued in high-income countries but is rising in lower- and middle-income regions ([PMID: 42953891](https://pubmed.ncbi.nlm.nih.gov/42953891/)).
- **Inheritance pattern.** **Multifactorial / polygenic susceptibility** (not simple Mendelian), despite the OMIM "IBD29" designation. INAVA is one susceptibility locus among many.
- **Penetrance / expressivity.** **Incomplete penetrance** and **variable expressivity** — the risk genotype is common but most carriers do not develop IBD; manifestation requires additional genetic and environmental hits.
- **Anticipation / mosaicism / founder effects.** Not applicable/not described.
- **Consanguinity.** Not a driver (common-variant susceptibility, not recessive rare disease).
- **Allele frequency.** rs7554511 risk allele C is the **common** allele (minor allele A MAF ~0.14–0.21); p.Y333F is rare (~0.4–1%).
- **Population demographics.** The locus was defined in predominantly European GWAS meta-analyses; the INAVA region shows pleiotropy with extraintestinal immune traits, with chromosome-1 enrichment in IBD–iridocyclitis genetic correlation ([PMID: 39472800](https://pubmed.ncbi.nlm.nih.gov/39472800/)). Sex ratio and geographic distribution follow general IBD patterns.

---

## 10. Diagnostics

IBD29 is diagnosed as its manifesting IBD subtype; genetic findings are supportive/research-level, not stand-alone diagnostic.

- **Laboratory tests.** CRP (HP:0011227), ESR (HP:0003565), CBC (anemia HP:0001903), **fecal calprotectin/lactoferrin** (mucosal inflammation markers), albumin, iron studies.
- **Biomarkers.** Fecal calprotectin; serologies (ASCA, pANCA) for CD/UC distinction; genotype (rs7554511, rs41313912) as research biomarkers.
- **Imaging.** CT/MR enterography, intestinal ultrasound.
- **Endoscopy / biopsy / pathology.** Ileocolonoscopy with biopsy is the diagnostic cornerstone; histology shows chronic active inflammation, crypt architectural distortion, and (CD) non-caseating granulomas.
- **Genetic testing.** WES/WGS or IBD gene panels can detect INAVA variants; single-gene testing (rs7554511, p.Y333F) has research/pharmacogenomic value but is **not standard clinical diagnostic** for common IBD. CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing are **not applicable**.
- **Omics-based diagnostics.** Transcriptomic risk-allele effects on INAVA expression demonstrated in macrophages; not a routine clinical assay.
- **Clinical criteria / differential diagnosis.** ECCO/ACG guidelines; differentials include infectious colitis, ischemic colitis, microscopic colitis, Behçet disease, intestinal TB, and drug-induced enteropathy.
- **Screening.** No population genetic screening for IBD29; colorectal cancer surveillance for long-standing colitis.

---

## 11. Outcome / Prognosis

- **Survival / mortality.** IBD (and thus IBD29) is generally **not life-limiting** with modern therapy; mortality is driven by complications (surgery, severe flares, colorectal cancer, thromboembolism). No IBD29-specific survival figures.
- **Morbidity / function / QoL.** Substantial — fatigue, urgency, surgery, disability, and reduced quality of life; psychosocial and developmental factors modulate symptom burden ([PMID: 42652338](https://pubmed.ncbi.nlm.nih.gov/42652338/)).
- **Complications.** Strictures, fistulae, abscesses, obstruction, perforation, malnutrition, anemia, extraintestinal manifestations, and increased colorectal cancer risk (HP:0003003).
- **Recovery potential.** Remission achievable with therapy; disease is chronic with relapse risk.
- **Prognostic factors.** Disease extent/behavior, age at onset, smoking, early biologic response, and biomarker trajectories (CRP, calprotectin). *C1orf106* genotype is a candidate pharmacogenomic predictor of infliximab exposure (see §12).

---

## 12. Treatment

**No INAVA-targeted therapy exists; IBD29 is treated with standard IBD therapy** matched to subtype and severity.

| Modality | Examples | NCIT suggestion |
|---|---|---|
| Aminosalicylates | mesalamine (5-ASA) | NCIT:C29281 (aminosalicylic acid class) |
| Corticosteroids | prednisone, budesonide | NCIT:C442 (corticosteroid) |
| Immunomodulators | azathioprine, 6-MP, methotrexate | NCIT:C569 (immunosuppressant) |
| Anti-TNF biologics | infliximab, adalimumab | NCIT:C1965 (infliximab) |
| Anti-integrin | vedolizumab | NCIT:C90555 |
| Anti-IL-12/23 | ustekinumab | NCIT:C82407 |
| JAK inhibitors | tofacitinib, upadacitinib | NCIT:C116834 |
| Surgery | resection, colectomy, fistula repair | NCIT:C15329 (surgery) |

- **Pharmacogenomics.** Polymorphisms in *C1orf106* (together with *IL1RN* and *IL10*) contribute to variability in post-induction **infliximab trough levels** in a cohort of 189 Crohn disease patients (multivariate model AUROC 0.758 training / 0.733 testing) ([PMID: 33163192](https://pubmed.ncbi.nlm.nih.gov/33163192/)).
- **Mechanistically nominated druggable nodes.** **p38α and mTOR inhibitors** enhance resolution of INAVA inflammatory condensates; **Rho-ROCK inhibitors** recruit INAVA to intercellular junctions (pro-barrier), and ROCK inhibition rescues C1ORF106-knockdown actin/polarity defects ([PMID: 34251416](https://pubmed.ncbi.nlm.nih.gov/34251416/); [PMID: 40161582](https://pubmed.ncbi.nlm.nih.gov/40161582/)). These are **experimental/preclinical** leads, not approved IBD29 therapies.
- **Advanced/RNA/gene/cell therapy.** No INAVA-specific gene, cell, or RNA therapy is in clinical use.
- **Supportive care.** Nutrition, iron repletion, smoking cessation (CD), vaccination before immunosuppression.
- **Strategy.** Treat-to-target with step-up or top-down algorithms; genotype-guided dosing remains investigational.

---

## 13. Prevention

- **Primary prevention.** No specific primary prevention for IBD29; general IBD risk-factor modification (smoking cessation for CD, dietary measures, judicious antibiotic/NSAID use).
- **Secondary prevention.** Early detection of flares via fecal calprotectin monitoring; colorectal cancer surveillance colonoscopy in long-standing colitis.
- **Tertiary prevention.** Maintenance therapy to prevent relapse, strictures, and surgery; bone, thrombosis, and infection prophylaxis during immunosuppression.
- **Immunization.** Age-appropriate and pre-biologic vaccination (not disease-causing but part of IBD management).
- **Genetic screening / counseling.** No carrier or prenatal screening is indicated for a common polygenic susceptibility variant; genetic counseling emphasizes **multifactorial, low-penetrance** risk.
- **Public-health / environmental.** General IBD measures (diet, microbiome health). No specific environmental intervention established for IBD29.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs.** INAVA orthologs: mouse *Inava* (Entrez 67313; MGI:1921579; chr1 E4), rat *Inava* (289399), chimpanzee (101058404), chicken (430729), and zebrafish paralogs (563192, 567844). Human gene ENSG00000163362.
- **Natural disease in other species.** No well-characterized spontaneous INAVA-associated enteropathy is catalogued in companion animals or wildlife (OMIA); IBD-like disease in dogs/cats is multifactorial and not ascribed to INAVA.
- **Comparative biology.** The barrier and innate-immune functions of INAVA appear conserved in mouse (knockout phenotypes mirror human barrier susceptibility), supporting evolutionary conservation of the mechanism.
- **Transmission / zoonosis.** Not applicable — IBD29 is a non-communicable, genetically influenced disease.

---

## 15. Model Organisms

| Model | Type | Key phenotype | Reference |
|---|---|---|---|
| *C1orf106/Inava* knockout mouse | Mammalian, germline KO | Intestinal epithelial **barrier defects**, increased susceptibility to intestinal pathogens | [PMID: 29420262](https://pubmed.ncbi.nlm.nih.gov/29420262/) |
| *C1orf106*-deficient mouse | Mammalian KO | **Hypersensitivity to TNF-α–induced epithelial permeability** with increased diarrhea | [PMID: 31022698](https://pubmed.ncbi.nlm.nih.gov/31022698/) |
| Human colonic epithelial cell knockdown | In vitro / cellular | Impaired actin belt, cell polarity, barrier | [PMID: 40161582](https://pubmed.ncbi.nlm.nih.gov/40161582/) |
| Patient-derived **hiPSC intestinal spheroids** (p.Y333F) | iPSC-derived organoid | Cell-polarity defects reproduced by the IBD variant; rescued by ROCK inhibition | [PMID: 40161582](https://pubmed.ncbi.nlm.nih.gov/40161582/) |
| Primary human macrophages | In vitro (human) | PRR/IL-1β signaling, 14-3-3τ recruitment, condensate dynamics | [PMID: 28436939](https://pubmed.ncbi.nlm.nih.gov/28436939/); [PMID: 30355448](https://pubmed.ncbi.nlm.nih.gov/30355448/) |

- **Genetic model types available.** Knockout mice; cell-line knockdowns; patient-specific iPSC-derived intestinal models carrying p.Y333F.
- **Phenotype recapitulation.** Strong for the **barrier arm** (mouse KO leaky-gut and pathogen susceptibility; iPSC spheroid polarity defects) and for the **myeloid signaling arm** (human macrophage assays).
- **Limitations.** Mouse KO is a complete-loss model whereas human risk is partial-dosage; spontaneous colitis is challenge-dependent, not fully autonomous; the common human risk allele is regulatory, so knockouts overstate effect size.
- **Resources.** MGI (MGI:1921579), IMPC/IMSR for mouse lines; Cellosaurus for iPSC lines.

---

## Mechanistic Model / Interpretation

INAVA is best understood as a **molecular rheostat that couples epithelial barrier integrity to innate-immune antimicrobial competence**, using a single bifunctional CUPID (DUF3338) domain. In the resting epithelium, CUPID binds the cytohesin ARF-GEF **ARNO** to build lateral-membrane F-actin that underpins cell–cell junctions, and INAVA restrains cytohesin-1/ARF6 to keep adherens junctions stable; ROCK-dependent actin-belt dynamics maintain polarity. Upon inflammatory stimulation (IL-1β, NOD2 agonists), INAVA switches modes — relocating into **biomolecular condensates** where CUPID amplifies TRAF6-dependent polyubiquitination (with βTrCP2 and ubiquitin) to drive MAPK/NF-κB signaling and bacterial clearance. ARNO negatively regulates this inflammatory arm, embodying a built-in barrier-versus-inflammation toggle.

IBD29 genotypes **turn the rheostat down**: rs7554511-C lowers total INAVA, and p.Y333F accelerates its degradation. The two arms fail together — a leakier epithelium admits more microbes while macrophages clear them less efficiently — so that under the everyday challenge of the gut microbiota (and amplifying signals like TNF-α), the system tips into chronic inflammation. This dual-hit, challenge-dependent model explains why the risk allele is common yet low-penetrance, why the phenotype is the familiar CD/UC spectrum rather than a unique syndrome, and why both barrier-directed (ROCK) and inflammation-directed (p38α/mTOR) interventions are mechanistically plausible.

---

## Evidence Base

| PMID | Role | Contribution |
|---|---|---|
| [28436939](https://pubmed.ncbi.nlm.nih.gov/28436939/) | Core (human macrophage) | INAVA required for PRR-induced MAPK/NF-κB, cytokines, bacterial clearance via 14-3-3τ; rs7554511-C carriers have lower INAVA RNA/protein via decreased intronic-driven transcription |
| [29420262](https://pubmed.ncbi.nlm.nih.gov/29420262/) | Core (Science; mouse + mechanism) | C1orf106 stabilizes adherens junctions by promoting cytohesin-1 degradation → limiting ARF6; KO mice have barrier defects/pathogen susceptibility; IBD risk variant ↑ubiquitination/turnover |
| [31022698](https://pubmed.ncbi.nlm.nih.gov/31022698/) | Supporting (mouse) | C1orf106 interacts with cytohesins; KO mice hypersensitive to TNF-α–induced permeability with diarrhea |
| [30355448](https://pubmed.ncbi.nlm.nih.gov/30355448/) | Core (eLife; mechanism) | CUPID/DUF3338 domain binds ARNO for barrier F-actin and amplifies TRAF6 polyubiquitination in IL-1β puncta |
| [34251416](https://pubmed.ncbi.nlm.nih.gov/34251416/) | Supporting (J Cell Biol) | INAVA puncta are biomolecular condensates with ubiquitin + βTrCP2; p38α/mTOR inhibitors resolve them; ROCK inhibition drives barrier function |
| [40161582](https://pubmed.ncbi.nlm.nih.gov/40161582/) | Supporting (iPSC/cellular) | C1ORF106 KD impairs actin belt/polarity/migration; p.Y333F reproduces defect; ROCK inhibition rescues |
| [33163192](https://pubmed.ncbi.nlm.nih.gov/33163192/) | Supporting (pharmacogenomics) | C1orf106 polymorphisms contribute to infliximab trough-level variability (AUROC ~0.73–0.76) |
| [39472800](https://pubmed.ncbi.nlm.nih.gov/39472800/) | Context | IBD genetic pleiotropy with iridocyclitis, chromosome-1 enrichment |
| [42953891](https://pubmed.ncbi.nlm.nih.gov/42953891/) | Context (epidemiology) | IBD affects >7 million worldwide; rising incidence in LMICs |

**Key verbatim support.**
- "Upon PRR stimulation, INAVA was required for optimal MAPK and NF-κB activation, cytokine secretion, and intracellular bacterial clearance. INAVA recruited 14-3-3τ..." (PMID 28436939)
- "C1orf106 regulates adherens junction stability by regulating the degradation of cytohesin-1... By limiting cytohesin-1-dependent ARF6 activation, C1orf106 stabilizes adherens junctions." (PMID 29420262)
- "Both activities require INAVA's DUF3338 domain (renamed CUPID). CUPID stably binds the cytohesin ARF-GEF ARNO to effect lateral membrane F-actin assembly..." (PMID 30355448)
- "IL-1β-induced INAVA puncta are biomolecular condensates... The condensates contain ubiquitin and the E3 ligase βTrCP2." (PMID 34251416)
- "an inhibition of ROCK rescues the actin belt and cell polarity phenotypes in C1ORF106 KD cells..." (PMID 40161582)

---

## Limitations and Knowledge Gaps

1. **No IBD29-genotype-stratified clinical data** — phenotype frequencies, age of onset, severity, and prognosis are inferred from general IBD, not from INAVA-genotype-defined cohorts.
2. **Dosage vs knockout gap** — most in vivo mechanism comes from complete-loss mouse models, whereas the common human risk is partial expression reduction; effect sizes may be overstated.
3. **Regulatory variant mechanism** — the precise transcription-factor/enhancer basis of the rs7554511 effect is not fully resolved; no methylation/chromatin data specific to IBD29.
4. **Epidemiology is non-specific** — no prevalence/incidence, penetrance estimate, or carrier-adjusted risk is quantified for the INAVA locus alone.
5. **Druggable nodes are preclinical** — p38α/mTOR/ROCK leads derive from cellular/condensate biology; none is validated clinically for IBD29.
6. **Pharmacogenomic finding is single-cohort** (n=189) and needs replication before clinical use.
7. **Limited literature depth** — the investigation rests on ~6 primary mechanistic papers; additional GWAS fine-mapping and functional validation would strengthen causal attribution.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype-stratified clinical cohort study** — correlate rs7554511/p.Y333F carriage with IBD subtype, age at onset, behavior (B1/B2/B3), extraintestinal manifestations, and surgery rates.
2. **Fine-mapping and functional enhancer dissection** of the rs7554511 region (CRISPRi/MPRA) to confirm the causal regulatory element and transcription factors.
3. **Knock-in allelic-series mice** (p.Y333F and expression-lowering alleles) to model partial loss and test challenge-dependent colitis (DSS, TNF-α, enteric infection).
4. **Patient iPSC organoid barrier/immune co-cultures** to quantify permeability and macrophage clearance under risk vs protective genotypes, with ROCK/p38α/mTOR inhibitor rescue.
5. **Replicate and extend the infliximab pharmacogenomics** in larger multi-ancestry IBD cohorts; test whether INAVA genotype predicts biologic response.
6. **Microbiome × genotype interaction studies** to identify specific pathobionts that precipitate inflammation in INAVA-deficient hosts.
7. **Condensate-targeting proof-of-concept** — test whether modulating INAVA condensate dynamics shifts the barrier/inflammation balance in vivo.


## Artifacts

- [OpenScientist final report](Inflammatory_Bowel_Disease_29-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Inflammatory_Bowel_Disease_29-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 41 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 22 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0054849` (4 mentions) - the report calls it "MONDO", "inflammatory bowel disease 29"; MONDO calls it **inflammatory bowel disease 29**
- `HP:0002028` (1 mention) - the report calls it "Symptom"; HP calls it **Chronic diarrhea**
- `HP:0002573` (1 mention) - the report calls it "Sign"; HP calls it **Hematochezia**
- `HP:0002027` (1 mention) - the report calls it "Symptom"; HP calls it **Abdominal pain**
- `HP:0001824` (1 mention) - the report calls it "Sign"; HP calls it **Weight loss**
- `HP:0002024` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Malabsorption**
- `HP:0100275` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Diffuse cerebellar atrophy**
- `HP:0011227` (2 mentions) - the report calls it "Lab abnormality"; HP calls it **Elevated circulating C-reactive protein concentration**
- `HP:0003565` (2 mentions) - the report calls it "Lab abnormality"; HP calls it **Elevated erythrocyte sedimentation rate**
- `HP:0001903` (2 mentions) - the report calls it "Lab abnormality"; HP calls it **Anemia**
- `HP:0001369` (1 mention) - the report calls it "Extraintestinal"; HP calls it **Arthritis**
- `HP:0000554` (1 mention) - the report calls it "Extraintestinal"; HP calls it **Uveitis**
- `HP:0012219` (1 mention) - the report calls it "Extraintestinal"; HP calls it **Erythema nodosum**
- `HP:0030151` (1 mention) - the report calls it "Extraintestinal"; HP calls it **Cholangitis**
- `GO:0036464` (1 mention) - the report calls it "cytosolic biomolecular condensates"; GO calls it **cytoplasmic ribonucleoprotein granule**
- `NCIT:C29281` (1 mention) - the report calls it "aminosalicylic acid class"; NCIT calls it **Nafcillin Sodium**
- `NCIT:C442` (1 mention) - the report calls it "corticosteroid"; NCIT calls it **Dioxin Compound**
- `NCIT:C569` (1 mention) - the report calls it "immunosuppressant"; NCIT calls it **IgM**
- `NCIT:C1965` (1 mention) - the report calls it "infliximab"; NCIT calls it **Lutein**
- `NCIT:C90555` (1 mention) - the report calls it "vedolizumab"; NCIT calls it **CEA/Tetanus Toxoid T Helper Epitope Fusion Protein-Expressing DNA Plasmid Vaccine**
- `NCIT:C82407` (1 mention) - the report calls it "ustekinumab"; NCIT calls it **pTVG-HP Plasmid DNA Vaccine**
- `NCIT:C116834` (1 mention) - the report calls it "tofacitinib, upadacitinib"; NCIT calls it **CNS 2**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0032088` (obsolete negative regulation of NF-kappaB transcription factor activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0005214` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Intestinal obstruction**
- `HP:0003003` (2 mentions) - the report calls it "Complication"; HP calls it **Colon cancer**
- `GO:0032088` (1 mention) - the report calls it "negative regulation of NF-κB"; GO calls it **obsolete negative regulation of NF-kappaB transcription factor activity**
- `GO:0038061` (1 mention) - the report calls it "NIK/NF-κB signaling"; GO calls it **non-canonical NF-kappaB signal transduction**, and lists "NIK/NF-kappaB signaling" among its other names
- `GO:0043123` (1 mention) - the report calls it "positive regulation of NF-κB"; GO calls it **positive regulation of canonical NF-kappaB signal transduction**, and lists "positive regulation of I-kappaB kinase/NF-kappaB cascade" among its other names
- `CL:0002253` (2 mentions) - the report calls it "epithelial cell of large intestine", "intestinal epithelial cells"; CL calls it **epithelial cell of large intestine**, and lists "epithelial cell of colon" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0054849` - called "MONDO", "inflammatory bowel disease 29"
- `CL:0000235` - called "macrophage", "macrophages"
- `CL:0002253` - called "epithelial cell of large intestine", "intestinal epithelial cells"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.