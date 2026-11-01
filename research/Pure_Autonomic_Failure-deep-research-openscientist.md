---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T13:18:10.963041'
end_time: '2026-10-24T13:32:26.700060'
duration_seconds: 855.74
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Pure Autonomic Failure
  mondo_id: MONDO:0018608
  category: Complex
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Bradbury Eggleston syndrome; Bradbury-Eggleston syndrome; PAF; Pure dysautonomia;
    Pure idiopatic dysautonomia; idiopathic orthostatic hypotension
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
citation_count: 29
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 22
  quotes_valid: 22
  relevance_assessed: 30
  on_topic: 24
  validator_version: 0.4.0
term_validation:
  total_terms: 33
  verified: 30
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 6
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0012694
    reported_labels:
    - Clinical sign
    ontology_label: Enlarged thalamic volume
  - term_id: HP:0002019
    reported_labels:
    - Symptom
    ontology_label: Constipation
  - term_id: UBERON:0002260
    reported_labels:
    - "intermediolateral nucleus \u2014 spinal cord lateral horn"
    ontology_label: ventral root of spinal cord
  - term_id: NCIT:C61721
    reported_labels:
    - Approved for OH; first-line pressor
    - midodrine
    ontology_label: Diethylpropion
  - term_id: NCIT:C66878
    reported_labels:
    - FDA-approved for nOH; 3 RCTs (see below)
    - droxidopa
    ontology_label: Lapatinib Ditosylate
  - term_id: NCIT:C29082
    reported_labels:
    - Adjunct; use with caution
    ontology_label: Guaifenesin/Codeine
  - term_id: NCIT:C47629
    reported_labels:
    - Better in MSA/mild disease; less effective in PAF
    ontology_label: Nalbuphine Hydrochloride
  - term_id: NCIT:C61763
    reported_labels:
    - Caution (hyponatremia)
    ontology_label: Ferrous Fumarate
  - term_id: CHEBI:28918
    reported_labels:
    - L-DOPA
    ontology_label: (R)-adrenaline
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0042136
    ontology_label: obsolete neurotransmitter biosynthetic process
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
  path: Pure_Autonomic_Failure-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pure_Autonomic_Failure-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pure Autonomic Failure
- **MONDO ID:** MONDO:0018608 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Bradbury Eggleston syndrome; Bradbury-Eggleston syndrome; PAF; Pure dysautonomia; Pure idiopatic dysautonomia; idiopathic orthostatic hypotension
- **Category:** Complex

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Pure Autonomic Failure** covering all of the
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

# Pure Autonomic Failure (MONDO:0018608) — Comprehensive Disease Characteristics Report

## Summary

**Pure Autonomic Failure (PAF; Bradbury–Eggleston syndrome)** is a rare, sporadic, adult/late-onset **peripheral α-synucleinopathy**. It has **no Mendelian causal gene**; its central causal protein is **α-synuclein, encoded by *SNCA* (HGNC:11138; chromosome 4q22.1)**, which misfolds and aggregates as Lewy-body-type neuronal cytoplasmic inclusions predominantly within the **peripheral autonomic nervous system** — postganglionic sympathetic neurons, sympathetic ganglia, the intermediolateral columns of the spinal cord, and distal autonomic axons of the heart and bladder. The resulting degeneration and biochemical dysfunction of noradrenergic neurons (tyrosine-hydroxylase depletion, impaired vesicular catecholamine storage, postganglionic denervation) produces a profound **norepinephrine deficiency** and the hallmark clinical feature of **neurogenic orthostatic hypotension (nOH)**, together with genitourinary, gastrointestinal, and sudomotor autonomic failure. Although PAF is historically regarded as an isolated condition, it is now understood as a **localized/prodromal synucleinopathy**: approximately **30% of patients phenoconvert over ~6 years** to a central synucleinopathy — multiple system atrophy (MSA), dementia with Lewy bodies (DLB), or Parkinson's disease (PD).

Diagnosis rests on autonomic function testing demonstrating neurogenic OH, low supine plasma norepinephrine without orthostatic rise, cutaneous phosphorylated α-synuclein on skin biopsy, CSF α-synuclein seed-amplification assays (αSyn-PMCA), and reduced cardiac sympathetic imaging (¹²³I-MIBG scintigraphy). There is **no disease-modifying therapy**; management is **symptomatic** and pathophysiology-guided — non-pharmacologic measures (salt/fluid loading, compression garments, physical counter-maneuvers, head-up sleeping) plus **norepinephrine-replacing drugs (midodrine, droxidopa)**, which are preferred in PAF because of its low peripheral sympathetic reserve, balanced carefully against comorbid neurogenic supine hypertension.

This report synthesizes 11 confirmed findings and 37 reviewed papers across all 15 requested sections. The strongest, best-supported conclusions are: (1) PAF is molecularly an α-synucleinopathy with a peripheral noradrenergic lesion; (2) the biochemical signature is tyrosine-hydroxylase deficiency with relatively preserved norepinephrine transporter; (3) roughly one-third of patients phenoconvert, with identifiable clinical and biomarker predictors; and (4) droxidopa and midodrine are the evidence-supported, pathophysiology-matched therapies for the orthostatic hypotension.

---

## 1. Disease Information

**Overview.** PAF is a chronic, slowly progressive degenerative disorder of the autonomic nervous system characterized by isolated (at onset) autonomic failure in the absence of other neurological deficits. The cardinal manifestation is **neurogenic orthostatic hypotension**. Pathologically it is defined by **predominantly peripheral deposition of α-synuclein** and degeneration of postganglionic sympathetic neurons ([PMID: 31515103](https://pubmed.ncbi.nlm.nih.gov/31515103/); [PMID: 24095130](https://pubmed.ncbi.nlm.nih.gov/24095130/)).

> "Pathologically, PAF is characterized by predominantly peripheral deposition of α-synuclein." — [PMID: 31515103](https://pubmed.ncbi.nlm.nih.gov/31515103/)

> "characterized by isolated peripheral autonomic dysfunction and decreased norepinephrine synthesis" — [PMID: 24095130](https://pubmed.ncbi.nlm.nih.gov/24095130/)

**Key identifiers.**
- **MONDO:** MONDO:0018608
- **MeSH:** Pure Autonomic Failure (D054970)
- **ICD-10:** G90.3 (multi-system degeneration of the autonomic nervous system); **ICD-11:** autonomic nervous system disorder range
- **Orphanet:** ORPHA:95429 (Pure autonomic failure)
- **OMIM:** Not recorded as a Mendelian entry (sporadic disease; no causal gene registered)

**Synonyms / alternative names.** Bradbury–Eggleston syndrome; PAF; pure dysautonomia; pure idiopathic dysautonomia; idiopathic orthostatic hypotension.

**Information source.** Information is derived from **aggregated disease-level resources** (OMIM/Orphanet/MeSH, clinical cohort studies, autopsy series, and natural-history registries such as the Natural History Study of the Synucleinopathies and the Queen Square cohort), not single-patient EHR extraction.

---

## 2. Etiology

**Primary cause.** PAF is a **sporadic neurodegenerative α-synucleinopathy**. The proximal molecular cause is **misfolding and aggregation of α-synuclein (SNCA)** into β-sheet-rich fibrils forming intraneuronal Lewy bodies in peripheral autonomic neurons. No environmental trigger or infectious agent is established as causal.

**Genetic risk factors.** PAF occurs sporadically with **no established Mendelian inheritance** ([PMID: 24095130](https://pubmed.ncbi.nlm.nih.gov/24095130/): "PAF occurs sporadically"). However, rare *SNCA* lesions can produce a PAF-like noradrenergic/cardiac denervation phenotype, directly implicating α-synuclein dosage and structure (see Section 4). As a member of the α-synucleinopathy family, PAF likely shares susceptibility architecture (e.g., *SNCA* common variants, *GBA* variants) with PD/DLB, though PAF-specific GWAS data are lacking.

**Environmental risk factors.** Older age is the dominant demographic risk factor (mean onset ~63 years). A modest male predominance is observed (~64% male in large cohorts). No specific toxin, occupational exposure, or lifestyle factor has been causally linked.

**Protective factors.** None established genetically or environmentally for PAF specifically.

**Gene–environment interactions.** Not characterized for PAF. The disease is best modeled as a predominantly stochastic/age-related proteinopathy with rare monogenic (SNCA-dosage) phenocopies.

---

## 3. Phenotypes

The core phenotype is **neurogenic orthostatic hypotension** with multi-system autonomic failure. Autonomic failure manifests across genitourinary, bowel, and thermoregulatory domains ([PMID: 31515103](https://pubmed.ncbi.nlm.nih.gov/31515103/): "Autonomic failure may also manifest as genitourinary, bowel, and thermoregulatory dysfunction.").

| Phenotype | Type | HPO term | Onset/Severity/Course | Frequency |
|---|---|---|---|---|
| Neurogenic orthostatic hypotension (dizziness, presyncope, syncope) | Clinical sign / symptom | HP:0004926 (Orthostatic hypotension); HP:0001278 (Syncope) | Adult/late-onset; moderate–severe; progressive | Universal (defining feature) |
| Supine hypertension | Clinical sign | HP:0012694 | Co-occurs with nOH; variable | Common (>50% of nOH patients across dysautonomias) |
| Erectile/sexual dysfunction, urinary urgency/retention | Symptom | HP:0000012 (Abnormality of the urinary system); HP:0000144 | Often early; progressive | Common |
| Constipation / bowel dysmotility | Symptom | HP:0002019 | Progressive | Common |
| Anhidrosis / hypohidrosis (thermoregulatory/sudomotor failure) | Clinical sign | HP:0000966 / HP:0000821 | Progressive | Common |
| REM sleep behavior disorder (dream enactment) | Behavioral/sleep | HP:0002494 | Often prodromal | Frequent; prodromal synucleinopathy marker |

**Quality-of-life impact.** nOH substantially impairs daily functioning, increasing risk of falls, syncope, and functional disability; orthostatic symptoms limit upright activity. The combination of OH + RBD marks a "malignant" phenotype associated with cognitive impairment, postural instability, and reduced survival ([PMID: 31142660](https://pubmed.ncbi.nlm.nih.gov/31142660/): "The combination of OH and RBD was associated with cognitive impairment and more rapid progression of postural instability").

---

## 4. Genetic / Molecular Information

**Causal gene.** There is **no Mendelian causal gene** for sporadic PAF. The **causal protein is α-synuclein (*SNCA*, HGNC:11138; OMIM gene 163890; chromosome 4q22.1)**, which is the aggregating species in all PAF neuropathology.

**Rare *SNCA* lesions producing a PAF-like phenotype** ([PMID: 14736756](https://pubmed.ncbi.nlm.nih.gov/14736756/); [PMID: 31178336](https://pubmed.ncbi.nlm.nih.gov/31178336/)):

| Variant | Type | Functional consequence | Phenotype |
|---|---|---|---|
| *SNCA* whole-gene **triplication** (Iowa kindred) | Copy-number / structural | **Gain of function via overexpression** of normal α-synuclein | Lewy body parkinsonism with cardiac sympathetic denervation and orthostatic hypotension |
| *SNCA* **E46K** | Missense | Aggregation-prone; aggressive Lewy body disease | Can present as PAF with severe cutaneous p-synuclein and small-fiber denervation |

> "cardiac sympathetic denervation cosegregates with parkinsonism" … "where disease is caused by overexpression of normal alpha-synuclein" — [PMID: 14736756](https://pubmed.ncbi.nlm.nih.gov/14736756/)

> "All E46K-SNCA carriers had moderate to severe p-synuclein deposits and small fiber neurodegeneration" — [PMID: 31178336](https://pubmed.ncbi.nlm.nih.gov/31178336/)

These establish **SNCA gene dosage/structure as mechanistically sufficient** to produce the cardiac noradrenergic denervation characteristic of PAF, even though sporadic PAF carries no recurrent germline mutation.

**Variant classification.** The triplication and E46K are pathogenic for Lewy body disease; no recurrent pathogenic variant exists for sporadic PAF. Allele frequencies of these lesions are effectively absent in gnomAD (private/family-specific).

**Somatic vs germline.** The SNCA lesions above are germline. Sporadic PAF is not driven by an identified somatic variant.

**Modifier genes / epigenetics / chromosomal abnormalities.** Not characterized specifically for PAF beyond the SNCA-dosage effect (a copy-number/structural mechanism). The *SNCA* triplication is itself a large-scale genomic (copy-number) abnormality.

---

## 5. Environmental Information

- **Environmental factors / toxins:** None established as causal for PAF.
- **Lifestyle factors:** None causally linked. Dietary salt/fluid status strongly modulates *symptom severity* (volume depletion worsens nOH) but is not etiologic.
- **Infectious agents:** Not applicable — PAF is a degenerative proteinopathy, not an infectious or post-infectious disorder.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **α-synuclein (SNCA) misfolds and aggregates** into β-sheet-rich, seeding-competent fibrils in peripheral autonomic neurons (gain of toxic function) — **leads to** →
2. **Intraneuronal Lewy-body / Lewy-neurite inclusions form** in sympathetic ganglia, intermediolateral columns of the spinal cord, and distal autonomic axons of heart and bladder — **results in** →
3. **Noradrenergic neuron dysfunction**: tyrosine-hydroxylase (TH) depletion, impaired vesicular catecholamine storage, and postganglionic denervation — **leads to** →
4. **Deficient norepinephrine release** at sympathetic vascular terminals (very low supine plasma NE, no orthostatic rise) — **results in** →
5. **Failure of baroreflex-mediated vasoconstriction** on standing — **leads to** →
6. **Neurogenic orthostatic hypotension and multi-system autonomic failure** (urogenital, GI, sudomotor), the clinical manifestation.
7. **Branch (in ~30% over ~6 yr):** α-synuclein pathology **spreads to the CNS** (locus coeruleus, substantia nigra) — **leads to** phenoconversion to:
   - **PD / DLB** — if sympathetic intraneuronal Lewy-type synucleinopathy with low NE, OR
   - **MSA** — if preserved noradrenergic status (normal supine NE, intact pupils, cardiovagal responses).

Steps 1–2 (prion-like seeding/spread) are **partly inferred** from CSF seed-amplification assays and animal models rather than fully demonstrated in situ in living humans.

### Supporting detail by category

- **Protein dysfunction:** α-synuclein misfolding/aggregation (loss of normal synaptic function + toxic gain of function). CSF αSyn-PMCA is positive in ~94% of PAF, confirming seeding-competent misfolded α-synuclein ([PMID: 33881777](https://pubmed.ncbi.nlm.nih.gov/33881777/)). In PAF/PD the aggregates are **neuronal cytoplasmic inclusions (Lewy bodies)**, in contrast to the **glial cytoplasmic inclusions** of MSA ([PMID: 24095130](https://pubmed.ncbi.nlm.nih.gov/24095130/): "they take the form of neuronal cytoplasmic inclusions called Lewy bodies in PAF and PD").
- **Biochemical abnormality:** Profound **tyrosine-hydroxylase deficiency** (the rate-limiting catecholamine-synthesis enzyme, tyrosine→L-DOPA) with **relatively preserved norepinephrine transporter (NET)** in sympathetic nerves — "normal abundance of the NE transporter (NET) protein, together with very low levels of tyrosine hydroxylase (TH)" ([PMID: 29162745](https://pubmed.ncbi.nlm.nih.gov/29162745/)). This suggests synthetic dysfunction may precede/exceed outright structural denervation.
- **Dual lesion (imaging):** Cardiac sympathetic PET shows that "PAF entails moderately decreased cardiac sympathetic innervation and a substantial vesicular storage defect in residual nerves" ([PMID: 32945121](https://pubmed.ncbi.nlm.nih.gov/32945121/)) — i.e., both denervation and a vesicular catecholamine storage defect.
- **Cellular processes:** Neurodegeneration of noradrenergic neurons; baroreflex failure.
- **Molecular pathways / metabolic changes:** Catecholamine biosynthesis pathway disrupted at the TH step (tyrosine → L-DOPA → dopamine → norepinephrine).

**Suggested GO terms:** **GO:0042423** (catecholamine biosynthetic process), **GO:0042136** (neurotransmitter biosynthetic process), **GO:0007268** (chemical synaptic transmission), GO:0003018 (vascular process in circulatory system). **GO cellular component:** GO:0097413 (Lewy body); synaptic vesicle (GO:0008021). **CL terms:** CL:0000540 (neuron), **CL:0011103 (sympathetic noradrenergic neuron / postganglionic sympathetic neuron)**.

---

## 7. Anatomical Structures Affected

**Organ / system level.**
- **Primary:** Peripheral autonomic nervous system — sympathetic ganglia, postganglionic sympathetic nerves. **Body systems:** autonomic (sympathetic) nervous system; cardiovascular (blood-pressure regulation); genitourinary; gastrointestinal; integumentary (sudomotor).
- **Secondary (with phenoconversion):** central nervous system (locus coeruleus, substantia nigra).

**Autopsy-defined pathology** ([PMID: 9255396](https://pubmed.ncbi.nlm.nih.gov/9255396/)): cell loss in **intermediolateral columns** (spinal cord) and **sympathetic ganglia**; Lewy bodies in substantia nigra, locus coeruleus, substantia innominata, and sympathetic ganglia; and in **distal autonomic axons** — epicardial fat (cardiac), periadrenal adipose nerve fascicles, and nerves in the muscularis of the urinary bladder. "Sites of autonomic nerve involvement correlated with clinical symptomatology."

> "histopathologically by cell loss in intermediolateral columns and sympathetic ganglia" — [PMID: 9255396](https://pubmed.ncbi.nlm.nih.gov/9255396/)

> "Lewy bodies in this disease may be seen in distal axons at a great length from their primary cell bodies" — [PMID: 9255396](https://pubmed.ncbi.nlm.nih.gov/9255396/)

**Tissue / cell level.** Nervous tissue; **postganglionic sympathetic noradrenergic neurons** (CL:0011103). **Subcellular:** neuronal cytoplasm (Lewy-body inclusions; GO:0097413 Lewy body); synaptic vesicle catecholamine storage compartment (vesicular storage defect).

**Localization (UBERON):** UBERON:0001806 (sympathetic ganglion / paravertebral ganglion), UBERON:0002260 (intermediolateral nucleus — spinal cord lateral horn), UBERON:0000948 (heart), UBERON:0001255 (urinary bladder), UBERON:0001872 (locus coeruleus), UBERON:0002038 (substantia nigra). **Lateralization:** bilateral/systemic.

---

## 8. Temporal Development

- **Onset:** Adult/late-onset; mean age ~63 years (63.1 yr in meta-analysis). **Pattern:** insidious, chronic.
- **Progression:** Slowly progressive over years to decades. Disease course is **chronic and progressive**; nOH is often a relatively late and severe sign of autonomic degeneration. In some patients the "pure" peripheral phase is stable for many years (Queen Square median follow-up ~10 yr).
- **Critical transition / phenoconversion:** ~30% convert to a central synucleinopathy over a mean of ~6.4 years (meta-analysis); independent cohorts report ~33% over ~10–13 years. This defines a **critical window** for prognostication and potential future neuroprotective intervention.
- **Duration:** Chronic, lifelong.

---

## 9. Inheritance and Population

**Epidemiology.** PAF is rare (Orphanet ORPHA:95429). Precise population prevalence/incidence estimates are not well established; it is the least common of the primary chronic autonomic failure syndromes. Cohort demographics: mean onset ~63 years, **male predominance ~64%** (meta-analytic cohort, [PMID: 42081229](https://pubmed.ncbi.nlm.nih.gov/42081229/)).

**Inheritance.** **Sporadic / non-Mendelian** (multifactorial, age-related). No inheritance pattern, penetrance, anticipation, founder effect, consanguinity role, or carrier frequency applies to sporadic PAF. The rare SNCA triplication kindred shows autosomal-dominant transmission of a Lewy body phenotype that includes PAF-like cardiac denervation, but this is a phenocopy, not sporadic PAF.

**Population demographics.** No specific ethnic/geographic predilection established. Sex ratio modestly male-skewed; age distribution concentrated in older adults.

---

## 10. Diagnostics

**Autonomic function testing** is the diagnostic cornerstone: demonstration of **neurogenic** OH (sustained BP fall on standing/head-up tilt with inadequate heart-rate compensation and blunted NE response).

**Biomarkers and tests:**

| Test | Finding in PAF | Performance | PMID |
|---|---|---|---|
| Supine plasma **norepinephrine** | Low (often <100–200 pg/mL), no orthostatic rise | Differentiates peripheral (PAF/PD) vs central (MSA) lesion | [24095130](https://pubmed.ncbi.nlm.nih.gov/24095130/), [40696849](https://pubmed.ncbi.nlm.nih.gov/40696849/) |
| **Cutaneous p-synuclein** (distal-leg skin biopsy) | Present in 22/22 (100%) PAF | Total p-syn score >3: 100% specificity, 82% sensitivity vs MSA | [39608812](https://pubmed.ncbi.nlm.nih.gov/39608812/) |
| **CSF αSyn-PMCA** (seed amplification) | Positive in ~94% of PAF | Confirms α-synucleinopathy; MSA-type kinetics + NfL predict MSA conversion | [33881777](https://pubmed.ncbi.nlm.nih.gov/33881777/) |
| **¹²³I-MIBG** cardiac scintigraphy | Reduced/absent uptake (PAF/PD); intact in MSA | "most sensitive test for early detection of autonomic dysfunction" | [38216420](https://pubmed.ncbi.nlm.nih.gov/38216420/) |
| CSF/plasma **NfL** + αSyn oligomers | Elevated NfL predicts conversion | Prognostic | [33881777](https://pubmed.ncbi.nlm.nih.gov/33881777/) |
| NM-MRI / FDOPA-PET | Reduced LC/SN contrast in high-conversion-risk PAF | Early CNS involvement biomarker | [39825743](https://pubmed.ncbi.nlm.nih.gov/39825743/) |

> "Total p-syn score >3 distinguished PAF from MSA with 100% specificity and 82% sensitivity." — [PMID: 39608812](https://pubmed.ncbi.nlm.nih.gov/39608812/)

> "αSyn-PMCA is almost invariably positive in the CSF of patients with PAF establishing this condition as α-synucleinopathy." — [PMID: 33881777](https://pubmed.ncbi.nlm.nih.gov/33881777/)

> "MIBG myocardial scintigraphy is the most sensitive test for early detection of autonomic dysfunction." — [PMID: 38216420](https://pubmed.ncbi.nlm.nih.gov/38216420/)

**Genetic testing.** Not routinely indicated for sporadic PAF. *SNCA* copy-number/sequence testing is relevant only where a strong family history of Lewy body disease suggests an SNCA-dosage phenocopy.

**Differential diagnosis.** MSA (preserved supine NE, intact pupils/cardiovagal responses, glial inclusions), PD/DLB with autonomic failure, dopamine-β-hydroxylase deficiency, diabetic/amyloid autonomic neuropathy, and non-neurogenic OH (volume depletion, drugs). The **supine plasma NE level** is a key discriminator — a *normal* supine NE in a PAF-like presentation is a red flag for later MSA conversion ([PMID: 35790426](https://pubmed.ncbi.nlm.nih.gov/35790426/); [PMID: 40696849](https://pubmed.ncbi.nlm.nih.gov/40696849/)).

**Screening.** No population screening for PAF. Research-grade risk stratification of RBD patients and PAF patients identifies individuals at high prodromal risk for synucleinopathy conversion.

---

## 11. Outcome / Prognosis

PAF itself is relatively benign in its "pure" peripheral phase compared with MSA, but it carries a substantial risk of **phenoconversion** to a more disabling central synucleinopathy.

**Phenoconversion** ([PMID: 42081229](https://pubmed.ncbi.nlm.nih.gov/42081229/)): In a meta-analysis of 9 studies / 900 PAF patients, 270/900 (**30%**) phenoconverted over mean 6.4 years — **12% to MSA, 11% to DLB, 7% to PD** (pooled incidence ~5.6/100 person-years). The Queen Square cohort (n=281, median 10-yr follow-up) reported 33% conversion ([PMID: 40397689](https://pubmed.ncbi.nlm.nih.gov/40397689/)).

> "270 of 900 individuals with PAF (30%) experienced phenoconversion to a central α-synucleinopathy (12% to MSA, 11% to DLB, 7% to PD)" — [PMID: 42081229](https://pubmed.ncbi.nlm.nih.gov/42081229/)

> "Of these, 33% (91) converted to a more widespread synucleinopathy" — [PMID: 40397689](https://pubmed.ncbi.nlm.nih.gov/40397689/)

**Prognostic factors** ([PMID: 38366572](https://pubmed.ncbi.nlm.nih.gov/38366572/); [PMID: 40696849](https://pubmed.ncbi.nlm.nih.gov/40696849/)):
- Faster phenoconversion associated with **urinary dysfunction (HR 5.9)**, **sexual dysfunction (HR 3.6)**, subtle motor signs (HR 2.7), dysphagia (HR 2.5), speech changes (HR 2.4).
- **Noradrenergic status bifurcates trajectory:** low supine NE + Lewy bodies → PD/DLB; preserved/normal NE, normal pupils, intact cardiovagal response → MSA. Younger age + higher supine NE favor MSA.
- OH + RBD "malignant" phenotype → cognitive decline, postural instability, reduced survival ([PMID: 31142660](https://pubmed.ncbi.nlm.nih.gov/31142660/)).

> "Faster phenoconversion from study enrolment to any diagnosis was associated with urinary and sexual dysfunction" — [PMID: 38366572](https://pubmed.ncbi.nlm.nih.gov/38366572/)

**Morbidity.** Falls, syncope, injury, and functional disability from nOH; supine hypertension risks target-organ damage. **Mortality** is driven largely by the central synucleinopathy following conversion (MSA conveys the worst prognosis).

---

## 12. Treatment

**Treatment is symptomatic — there is no disease-modifying therapy.** Drug selection is **pathophysiology-guided**: because PAF has **peripheral noradrenergic degeneration and low sympathetic reserve**, patients respond better to **norepinephrine "replacers"** (midodrine, droxidopa) than to NE "enhancers" (pyridostigmine, atomoxetine), which require spared postganglionic fibers (as in MSA) ([PMID: 32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/); [PMID: 31996627](https://pubmed.ncbi.nlm.nih.gov/31996627/); [PMID: 33705537](https://pubmed.ncbi.nlm.nih.gov/33705537/)).

> "those with peripheral noradrenergic degeneration (pure autonomic failure, Parkinson's disease) and low plasma norepinephrine, tend to respond better to 'norepinephrine replacers' (midodrine and droxidopa)" — [PMID: 32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/)

> "Patients with peripheral sympathetic denervation respond better to norepinephrine agonists/precursors such as droxidopa" — [PMID: 31996627](https://pubmed.ncbi.nlm.nih.gov/31996627/)

**Non-pharmacologic (first-line):** increased fluid and dietary salt, compression stockings/abdominal binders, physical counter-maneuvers, head-up sleeping, portioned meals, bolus water drinking.

**Pharmacologic:**

| Drug | Class / mechanism | Evidence | NCIT |
|---|---|---|---|
| **Midodrine** | α1-adrenergic agonist (direct pressor) | Approved for OH; first-line pressor | NCIT:C61721 |
| **Droxidopa** (L-threo-DOPS) | Norepinephrine prodrug | FDA-approved for nOH; 3 RCTs (see below) | NCIT:C66878 |
| **Fludrocortisone** | Mineralocorticoid (volume expander) | Adjunct; use with caution | NCIT:C29082 |
| **Pyridostigmine** | Acetylcholinesterase inhibitor (NE enhancer) | Better in MSA/mild disease; less effective in PAF | NCIT:C47629 |
| **Ampreloxetine** | Selective norepinephrine reuptake inhibitor | Phase 2 positive (emerging) | — |
| Desmopressin | Vasopressin analog (nocturnal polyuria) | Caution (hyponatremia) | NCIT:C61763 |

**Droxidopa RCT evidence** ([PMID: 28494751](https://pubmed.ncbi.nlm.nih.gov/28494751/); [PMID: 27538531](https://pubmed.ncbi.nlm.nih.gov/27538531/)): Pooled analysis (n=460) showed droxidopa significantly reduced OHQ composite (−2.68±2.20 vs −1.82±2.34; P<0.001) and dizziness/lightheadedness, improved activities of daily living, and raised upright systolic BP (11.5±20.5 vs 4.8±21.0 mmHg; P<0.001), with low supine-hypertension rates (≤7.9% vs ≤4.6% placebo). **NNT for OHSA item-1 improvement was <10.**

> "Droxidopa improved virtually all nOH symptom scores compared with placebo, significantly reducing OHQ composite score (−2.68 ± 2.20 vs −1.82 ± 2.34 units; P < 0.001)" — [PMID: 28494751](https://pubmed.ncbi.nlm.nih.gov/28494751/)

> "The NNT for droxidopa for improvement in OHSA Item 1 was <10" — [PMID: 27538531](https://pubmed.ncbi.nlm.nih.gov/27538531/)

**Durability caveat:** Benefit is largely short-term; durability beyond weeks 1–2 was inconsistent across endpoints ([PMID: 25487613](https://pubmed.ncbi.nlm.nih.gov/25487613/); [PMID: 25350981](https://pubmed.ncbi.nlm.nih.gov/25350981/), the latter a randomized-withdrawal study that failed its primary endpoint though secondary/composite outcomes favored droxidopa).

**Ampreloxetine** (NRI) raised seated SBP (+29.9 mmHg vs placebo; P=0.0112) and improved symptoms in a phase 2 nOH trial ([PMID: 34657222](https://pubmed.ncbi.nlm.nih.gov/34657222/)).

> "Seated blood pressure increased 15.7 mmHg 4 h after ampreloxetine and decreased 14.2 mmHg after placebo" — [PMID: 34657222](https://pubmed.ncbi.nlm.nih.gov/34657222/)

**Key therapeutic trade-off:** nOH and neurogenic **supine hypertension** are hemodynamically opposed — "Because nOH and nSH are hemodynamically opposed, therapies to treat one condition may exacerbate the other" ([PMID: 33687577](https://pubmed.ncbi.nlm.nih.gov/33687577/)) — requiring individualized balancing (e.g., short-acting nocturnal antihypertensives, avoiding late-day pressors).

---

## 13. Prevention

- **Primary prevention:** None available (no modifiable cause).
- **Secondary prevention:** Early recognition of nOH and identification of high-conversion-risk patients (biomarker/clinical stratification) for enrollment in neuroprotective trials and close monitoring.
- **Tertiary prevention:** Fall prevention, management of supine hypertension to limit target-organ damage, patient education on high-risk situations (heat, large meals, posture, dehydration).
- **Genetic counseling:** Generally not applicable (sporadic); relevant only for rare SNCA-dosage kindreds.
- **Immunization / public-health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* (NCBI:txid9606) is the species with the natural disease. No recognized spontaneous PAF-equivalent in companion animals is documented in OMIA.
- **Orthologous gene:** *Snca* in mouse (NCBI Gene ID 20617); SNCA orthologs are conserved across vertebrates.
- **Comparative biology:** α-synuclein aggregation and autonomic/cardiac sympathetic denervation mechanisms are evolutionarily conserved and modeled experimentally (see Section 15).
- **Transmission:** Not applicable (non-infectious, non-zoonotic). Note the experimental "prion-like" seeding behavior of α-synuclein is a laboratory phenomenon, not natural transmission.

---

## 15. Model Organisms

**Dedicated PAF mouse model** ([PMID: 32071315](https://pubmed.ncbi.nlm.nih.gov/32071315/)): injection of **α-synuclein preformed fibrils into autonomic ganglia of human A53T α-synuclein transgenic (TgM83) mice** produces α-synuclein pathology **confined to the autonomic nervous system with autonomic dysfunction and NO motor features** — recapitulating the "pure" peripheral phenotype.

> "in the pure autonomic failure (PAF), α-synuclein (α-Syn) pathology is confined within the autonomic nervous system with no motor features, but mouse models recapitulating PAF without motor dysfunction are lacking" — [PMID: 32071315](https://pubmed.ncbi.nlm.nih.gov/32071315/)

**Broader rodent synucleinopathy models** ([PMID: 23933655](https://pubmed.ncbi.nlm.nih.gov/23933655/)): genetic and toxin-induced models reproduce cardiovascular autonomic dysfunction and sympathetic denervation that often **precede motor signs**:

> "cardiovascular autonomic impairments including orthostatic hypotension and sympathetic denervation may precede the development of the cardinal motor symptoms" — [PMID: 23933655](https://pubmed.ncbi.nlm.nih.gov/23933655/)

**Human genetic "model":** the SNCA-triplication kindred confirms gene-dosage causality for cardiac denervation + parkinsonism ([PMID: 14736756](https://pubmed.ncbi.nlm.nih.gov/14736756/)).

**Model types:** mammalian (mouse — A53T TgM83, MGI resources); induced (fibril-injection, toxin). **Genetic models:** transgenic human α-synuclein (A53T). **Recapitulation:** autonomic-restricted pathology without motor involvement (good model for the "pure" peripheral phase). **Limitations:** phenoconversion to human-like MSA/DLB/PD subtypes and the TH-selective biochemical lesion are incompletely modeled.

---

## Mechanistic Model / Interpretation

```
            SNCA (α-synuclein) misfolding & aggregation (toxic gain of function)
                                   │  [CSF αSyn-PMCA + in ~94%]
                                   ▼
     Lewy-body inclusions in peripheral autonomic neurons
     (sympathetic ganglia, IML columns, cardiac & bladder axons)  [autopsy: 9255396]
                                   │
                                   ▼
     Noradrenergic neuron dysfunction:
     ↓Tyrosine hydroxylase  +  vesicular storage defect  +  denervation
     (NET relatively preserved)              [29162745, 32945121]
                                   │
                                   ▼
     ↓↓ Norepinephrine release (low supine plasma NE, no orthostatic rise)
                                   │
                                   ▼
     Baroreflex vasoconstriction failure on standing
                                   │
                                   ▼
     NEUROGENIC ORTHOSTATIC HYPOTENSION  +  urogenital/GI/sudomotor failure
                                   │
                                   ▼  (~30% over ~6 yr; CNS spread to LC/SN)
            ┌──────────────────────┴──────────────────────┐
            ▼                                              ▼
   Low NE + Lewy type                           Preserved NE, normal pupils,
   → PD / DLB                                    intact cardiovagal → MSA
   [34669076, 40696849]                          [35790426, 40696849]
```

The model is internally consistent and well-supported through step 6 (clinical manifestation). The upstream seeding/spreading steps (1–2) and the CNS-spread branch (step 7) are supported by seed-amplification assays, imaging, and animal models but remain partly **inferred** rather than directly demonstrated in situ in living humans. Branch assignment is supported by [PMID: 34669076](https://pubmed.ncbi.nlm.nih.gov/34669076/): "the form of PAF that involves sympathetic intraneuronal synucleinopathy and noradrenergic deficiency can phenoconvert to PD or DLB-but not to MSA."

---

## Evidence Base

| PMID | Role in report | Key contribution |
|---|---|---|
| [31515103](https://pubmed.ncbi.nlm.nih.gov/31515103/) | Supports F001, F008 | Defines peripheral α-synuclein pathology; multi-system phenotype |
| [24095130](https://pubmed.ncbi.nlm.nih.gov/24095130/) | Supports F001, F005, F006 | Peripheral autonomic dysfunction, NE deficiency, sporadic occurrence, neuronal vs glial inclusions |
| [9255396](https://pubmed.ncbi.nlm.nih.gov/9255396/) | Supports F005 | Autopsy distribution of Lewy bodies / IML & ganglion cell loss / distal axons |
| [29162745](https://pubmed.ncbi.nlm.nih.gov/29162745/) | Supports F009 | TH-deficient, NET-preserved biochemical lesion |
| [32945121](https://pubmed.ncbi.nlm.nih.gov/32945121/) | Supports F001, F010 | Dual lesion: denervation + vesicular storage defect (PET) |
| [33881777](https://pubmed.ncbi.nlm.nih.gov/33881777/) | Supports F003, F010 | CSF αSyn-PMCA positivity; NfL + oligomers predict conversion |
| [39608812](https://pubmed.ncbi.nlm.nih.gov/39608812/) | Supports F003 | Cutaneous p-synuclein diagnostic performance |
| [38216420](https://pubmed.ncbi.nlm.nih.gov/38216420/) | Supports F003 | MIBG scintigraphy |
| [42081229](https://pubmed.ncbi.nlm.nih.gov/42081229/) | Supports F002 | Meta-analytic phenoconversion rates (30%) |
| [38366572](https://pubmed.ncbi.nlm.nih.gov/38366572/) | Supports F002 | Clinical predictors of phenoconversion |
| [40397689](https://pubmed.ncbi.nlm.nih.gov/40397689/) | Supports F002 | Queen Square natural history (33% conversion) |
| [40696849](https://pubmed.ncbi.nlm.nih.gov/40696849/) | Supports F002, prognosis | Multimodal autonomic biomarkers predict conversion; MSA vs LBD |
| [34669076](https://pubmed.ncbi.nlm.nih.gov/34669076/) | Supports F010 branch | PD/DLB vs MSA conversion pathways |
| [14736756](https://pubmed.ncbi.nlm.nih.gov/14736756/) | Supports F006, F007 | SNCA triplication → cardiac denervation + parkinsonism (gene dosage) |
| [31178336](https://pubmed.ncbi.nlm.nih.gov/31178336/) | Supports F006 | E46K-SNCA skin p-synuclein + small-fiber loss |
| [32071315](https://pubmed.ncbi.nlm.nih.gov/32071315/) | Supports F007 | Dedicated PAF mouse model |
| [23933655](https://pubmed.ncbi.nlm.nih.gov/23933655/) | Supports F007 | Rodent autonomic denervation precedes motor signs |
| [31142660](https://pubmed.ncbi.nlm.nih.gov/31142660/) | Supports F008 | OH+RBD malignant phenotype |
| [32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/), [31996627](https://pubmed.ncbi.nlm.nih.gov/31996627/), [33705537](https://pubmed.ncbi.nlm.nih.gov/33705537/) | Supports F004 | Pathophysiology-guided drug selection |
| [33687577](https://pubmed.ncbi.nlm.nih.gov/33687577/) | Supports F004 | nOH/supine-hypertension trade-off |
| [28494751](https://pubmed.ncbi.nlm.nih.gov/28494751/), [27538531](https://pubmed.ncbi.nlm.nih.gov/27538531/) | Supports F011 | Droxidopa pooled efficacy; NNT<10 |
| [25487613](https://pubmed.ncbi.nlm.nih.gov/25487613/), [25350981](https://pubmed.ncbi.nlm.nih.gov/25350981/) | Challenges durability | Short-term benefit; inconsistent long-term/withdrawal endpoints |
| [34657222](https://pubmed.ncbi.nlm.nih.gov/34657222/) | Supports F011 | Ampreloxetine phase 2 |
| [39825743](https://pubmed.ncbi.nlm.nih.gov/39825743/) | Diagnostics/prognosis | NM-MRI + FDOPA-PET early CNS involvement |
| [35790426](https://pubmed.ncbi.nlm.nih.gov/35790426/), [42444112](https://pubmed.ncbi.nlm.nih.gov/42444112/) | Diagnostics | Normal supine NE flags MSA conversion; prodromal MSA criteria validation |

---

## Limitations and Knowledge Gaps

1. **No PAF-specific genetics/GWAS.** Susceptibility architecture is inferred from the broader α-synucleinopathy family; no PAF-specific common-variant or modifier-gene data exist.
2. **Prevalence/incidence are poorly quantified.** PAF is rare and often reclassified upon phenoconversion, confounding epidemiologic estimates.
3. **Upstream mechanism partly inferred.** Prion-like seeding and spread (steps 1–2, 7) rely on seed-amplification assays and animal models, not direct in vivo human demonstration.
4. **Treatment durability uncertain.** Droxidopa's long-term efficacy is inconsistent; one randomized-withdrawal trial failed its primary endpoint ([PMID: 25350981](https://pubmed.ncbi.nlm.nih.gov/25350981/)). Most PAF-specific treatment data derive from mixed nOH cohorts rather than PAF-only trials.
5. **No disease-modifying therapy.** Nothing yet alters phenoconversion risk or α-synuclein accumulation.
6. **Conversion prediction imperfect.** Biomarkers improve but do not perfectly predict which patients convert or to which subtype.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective biomarker-stratified cohort** combining supine plasma NE, pupillometry, cardiovagal responses, CSF αSyn-PMCA kinetics, NfL, and NM-MRI/FDOPA-PET to build a validated conversion-risk calculator (building on [PMID: 40696849](https://pubmed.ncbi.nlm.nih.gov/40696849/), [39825743](https://pubmed.ncbi.nlm.nih.gov/39825743/)).
2. **Neuroprotective trials in high-risk PAF** — target the prodromal window using α-synuclein–directed agents (immunotherapy, aggregation inhibitors) with phenoconversion as the endpoint.
3. **PAF-only pragmatic treatment trials** of droxidopa vs midodrine vs ampreloxetine with durability (≥6-month) and supine-hypertension co-endpoints.
4. **Mechanistic work on the TH-selective lesion** ([PMID: 29162745](https://pubmed.ncbi.nlm.nih.gov/29162745/)) — determine whether restoring catecholamine synthesis (e.g., optimized L-DOPS dosing, TH cofactor support) rescues function before structural denervation is complete.
5. **Refine the TgM83 ganglionic-fibril model** ([PMID: 32071315](https://pubmed.ncbi.nlm.nih.gov/32071315/)) to model phenoconversion branches and test anti-spreading therapeutics.
6. **Harmonize diagnostic criteria** to incorporate skin p-synuclein, seed amplification, and MIBG, and prospectively validate against autopsy (extending [PMID: 42444112](https://pubmed.ncbi.nlm.nih.gov/42444112/)).

---

*Report compiled from 11 confirmed findings and 37 reviewed papers. Evidence source types span human clinical (cohorts, RCTs, autopsy), model organism (transgenic/fibril mouse, rodent), in vitro/ex vivo (skin biopsy, CSF seed amplification), and imaging. Ontology suggestions: MONDO:0018608; HGNC:11138 (SNCA); HP:0004926, HP:0012694, HP:0000012, HP:0002019, HP:0000966, HP:0002494; GO:0042423, GO:0007268, GO:0097413; CL:0011103; UBERON:0001806, UBERON:0002260, UBERON:0000948, UBERON:0001255, UBERON:0001872, UBERON:0002038; CHEBI:18357 (noradrenaline), CHEBI:28918 (L-DOPA); NCIT:C66878 (droxidopa), NCIT:C61721 (midodrine).*


## Artifacts

- [OpenScientist final report](Pure_Autonomic_Failure-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pure_Autonomic_Failure-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 22 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 30 |
| On topic | 24 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 20 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012694` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Enlarged thalamic volume**
- `HP:0002019` (2 mentions) - the report calls it "Symptom"; HP calls it **Constipation**
- `UBERON:0002260` (2 mentions) - the report calls it "intermediolateral nucleus — spinal cord lateral horn"; UBERON calls it **ventral root of spinal cord**
- `NCIT:C61721` (2 mentions) - the report calls it "Approved for OH; first-line pressor", "midodrine"; NCIT calls it **Diethylpropion**
- `NCIT:C66878` (2 mentions) - the report calls it "FDA-approved for nOH; 3 RCTs (see below)", "droxidopa"; NCIT calls it **Lapatinib Ditosylate**
- `NCIT:C29082` (1 mention) - the report calls it "Adjunct; use with caution"; NCIT calls it **Guaifenesin/Codeine**
- `NCIT:C47629` (1 mention) - the report calls it "Better in MSA/mild disease; less effective in PAF"; NCIT calls it **Nalbuphine Hydrochloride**
- `NCIT:C61763` (1 mention) - the report calls it "Caution (hyponatremia)"; NCIT calls it **Ferrous Fumarate**
- `CHEBI:28918` (1 mention) - the report calls it "L-DOPA"; CHEBI calls it **(R)-adrenaline**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0042136` (obsolete neurotransmitter biosynthetic process) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002494` (2 mentions) - the report calls it "Behavioral/sleep"; HP calls it **Abnormal rapid eye movement sleep**, and lists "Abnormal REM sleep" among its other names
- `CL:0011103` (3 mentions) - the report calls it "sympathetic noradrenergic neuron / postganglionic sympathetic neuron", "postganglionic sympathetic noradrenergic neurons"; CL calls it **sympathetic neuron**
- `UBERON:0001806` (2 mentions) - the report calls it "sympathetic ganglion / paravertebral ganglion"; UBERON calls it **sympathetic ganglion**
- `UBERON:0001872` (2 mentions) - the report calls it "locus coeruleus"; UBERON calls it **parietal lobe**, and lists "lobus parietalis" among its other names
- `CHEBI:18357` (1 mention) - the report calls it "noradrenaline"; CHEBI calls it **(R)-noradrenaline**, and lists "(-)-noradrenaline" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0011103` - called "sympathetic noradrenergic neuron / postganglionic sympathetic neuron", "postganglionic sympathetic noradrenergic neurons"
- `NCIT:C61721` - called "Approved for OH; first-line pressor", "midodrine"
- `NCIT:C66878` - called "FDA-approved for nOH; 3 RCTs (see below)", "droxidopa"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.