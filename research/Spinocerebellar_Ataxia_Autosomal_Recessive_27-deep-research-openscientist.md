---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-07T11:33:19.433322'
end_time: '2026-11-07T11:51:10.387109'
duration_seconds: 1070.95
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Spinocerebellar Ataxia, Autosomal Recessive 27
  mondo_id: MONDO:0032706
  category: Mendelian
  causal_genes: GDAP2
  omim_id: OMIM:618369
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
citation_count: 8
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 6
  validator_version: 0.5.1
term_validation:
  total_terms: 29
  verified: 26
  not_found: 1
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.036
  labels_checked: 11
  labels_matching: 0
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0001260
    reported_labels:
    - Clinical sign
    ontology_label: Dysarthria
  - term_id: HP:0000496
    reported_labels:
    - Clinical sign
    ontology_label: Abnormality of eye movement
  - term_id: HP:0002061
    reported_labels:
    - Clinical sign
    ontology_label: Lower limb spasticity
  - term_id: HP:0025131
    reported_labels:
    - Clinical sign
    ontology_label: Finger swelling
  - term_id: HP:0002540
    reported_labels:
    - Functional
    ontology_label: Inability to walk
  - term_id: HP:0002015
    reported_labels:
    - Clinical sign
    ontology_label: Dysphagia
  labels_variant: 5
  unresolved_terms:
  - HP:0002402
  obsolete_terms:
  - term_id: GO:0070997
    ontology_label: obsolete neuron death
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spinocerebellar_Ataxia_Autosomal_Recessive_27-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spinocerebellar_Ataxia_Autosomal_Recessive_27-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia, Autosomal Recessive 27
- **MONDO ID:** MONDO:0032706 (if available)
- **Causal gene(s):** GDAP2
- **OMIM:** OMIM:618369
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia, Autosomal Recessive 27** covering all of the
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

# Spinocerebellar Ataxia, Autosomal Recessive 27 (SCAR27) — Comprehensive Disease Report

**Disease:** Spinocerebellar Ataxia, Autosomal Recessive 27 (SCAR27)
**Causal gene:** **GDAP2** (ganglioside-induced differentiation-associated protein 2)
**Identifiers:** MONDO:0032706 · phenotype OMIM #618369 · gene OMIM *618128 · HGNC:18010 · Ensembl ENSG00000196505 · UniProt Q9NXN4
**Category:** Mendelian, monogenic, autosomal recessive

---

## Summary

Spinocerebellar ataxia, autosomal recessive 27 (**SCAR27**) is an ultra-rare, adult-onset, slowly progressive neurodegenerative disorder caused by **biallelic loss-of-function (LOF) variants in GDAP2**, the gene encoding ganglioside-induced differentiation-associated protein 2. The disease was first defined in 2018, when Eidhof and colleagues reported two unrelated patients with gene-disruptive GDAP2 mutations and onset of ataxia in the fourth decade of life; GDAP2 had not previously been implicated in any human disease ([PMID: 30084953](https://pubmed.ncbi.nlm.nih.gov/30084953/)). Despite its name ("spinocerebellar ataxia"), SCAR27 is unambiguously a GDAP2 disorder — this report follows the MONDO ID (MONDO:0032706) and causal gene provided, and should not be confused with other serially-numbered spinocerebellar ataxias caused by different genes.

Clinically, SCAR27 presents in the third-to-fourth decade with cerebellar ataxia, dysarthria, and gait difficulty, frequently accompanied by eye-movement abnormalities, lower-limb spasticity, difficulty writing (dysgraphia), and cognitive impairment that can progress to dementia. Some patients lose independent ambulation and become wheelchair-dependent. Reported neuropathology extends well beyond the cerebellum to include the inferior olive, thalamus, substantia nigra, and pyramidal tracts, with limbic (hippocampus/amygdala) tau pathology. The molecular mechanism, best characterized in a *Drosophila* knockdown model, centers on **impaired cellular stress handling** — GDAP2-deficient cells show heightened vulnerability to oxidative stress (reactive oxygen species) and nutrient deprivation. GDAP2 is a 497-amino-acid protein containing a macro domain and a CRAL-TRIO/Sec14-like domain, and (distinct from its mitochondrial paralog GDAP1) localizes to the **lysosomal membrane**.

SCAR27 is caused exclusively by loss-of-function alleles: ClinVar's pathogenic/likely-pathogenic GDAP2 variants are uniformly truncating (nonsense, frameshift) or canonical splice-site changes, and population genetic constraint data (gnomAD) are consistent with a recessive LOF mechanism rather than haploinsufficiency. There is no disease-modifying therapy; management is supportive and rehabilitative, and diagnosis rests on whole-exome sequencing or hereditary-ataxia gene panels. No faithful mammalian neurodegeneration model yet exists — all published LOF animal models are invertebrate (*Drosophila* and silkworm) — representing a major gap for mechanistic and therapeutic research.

---

## Key Findings

### Finding 1 — SCAR27 is an adult-onset autosomal recessive cerebellar ataxia caused by biallelic GDAP2 loss-of-function

The defining study established the disease entity in two unrelated patients with biallelic, gene-disruptive GDAP2 mutations, both with onset of ataxia in the fourth decade and additional features of progressive spasticity and dementia. GDAP2 was explicitly described as "a gene previously not implicated in disease." As the authors state: *"we report two unrelated patients with a new subtype of autosomal recessive cerebellar ataxia caused by biallelic, gene-disruptive mutations in GDAP2, a gene previously not implicated in disease. Both patients had onset of ataxia in the fourth decade. Other features included progressive spasticity and dementia"* ([PMID: 30084953](https://pubmed.ncbi.nlm.nih.gov/30084953/)).

This finding anchors the disease definition: an autosomal recessive, adult-onset cerebellar ataxia with a monogenic GDAP2 cause. Subsequent reports have reproduced this picture in independent families — a Chinese family ([PMID: 32437512](https://pubmed.ncbi.nlm.nih.gov/32437512/)), an additional adult-onset case ([PMID: 32428220](https://pubmed.ncbi.nlm.nih.gov/32428220/)), and a Spanish family with a novel null variant ([PMID: 40469082](https://pubmed.ncbi.nlm.nih.gov/40469082/)) — confirming the gene-disease relationship across populations.

### Finding 2 — GDAP2 links cerebellar ataxia to defective cellular stress responses

Functional work in *Drosophila* linked GDAP2 loss to impaired stress handling. Ubiquitous knockdown of fly *Gdap2* caused shortened lifespan and motor anomalies (righting defects, reduced and uncoordinated walking, compromised flight). Critically, *Gdap2* expression itself responded to stress treatments, and knockdown flies were hypersensitive to oxidative and metabolic stress: *"Gdap2 expression levels responded to stress treatments in control flies, and Gdap2 knockdown flies showed increased sensitivity to deleterious effects of stressors such as reactive oxygen species and nutrient deprivation"* ([PMID: 30084953](https://pubmed.ncbi.nlm.nih.gov/30084953/)).

On the human side, neuropathological examination demonstrated degeneration extending to the cerebellum, inferior olive, thalamus, substantia nigra, and pyramidal tracts, with tau pathology in the hippocampus and amygdala. Together these data support a model in which GDAP2 normally protects neurons against cellular stress, and its loss renders long-lived post-mitotic neurons progressively vulnerable to oxidative and nutrient stress — a plausible explanation for the adult-onset, slowly progressive neurodegeneration.

### Finding 3 — GDAP2 is a 497-aa macro-domain + CRAL-TRIO protein on 1p13.2, with constraint consistent with recessive LOF

GDAP2 (UniProt Q9NXN4) is a 497-amino-acid protein containing a **macro domain** (residues ~43–223) and a **CRAL-TRIO/Sec14-like domain** (residues ~333–481), plus a disordered region (~252–273). The gene maps to chromosome **1p13.2** (GRCh38 chr1:117,863,485–117,929,621; HGNC:18010; Ensembl ENSG00000196505). This locus assignment corrects earlier imprecise annotations.

Population constraint metrics from gnomAD v4 are consistent with a recessive, loss-of-function disease mechanism rather than dominant haploinsufficiency: pLI ≈ 0 (1.1×10⁻¹³), LOEUF (oe_lof upper bound) = 0.96, observed/expected LoF = 51/67 (oe_lof = 0.76), LoF Z = 1.66, missense Z = 0.73. In plain terms, heterozygous loss of one GDAP2 allele is tolerated in the general population — as expected for a recessive disorder where disease requires loss of **both** copies.

The macro domain is a known ADP-ribose/NAD-metabolite-binding module (associated with poly-ADP-ribose signaling and stress responses), while CRAL-TRIO/Sec14 domains bind small hydrophobic ligands (e.g., lipids). These domain assignments provide a biochemical scaffold linking GDAP2 to the stress-response and lipid/membrane biology implicated in the phenotype.

### Finding 4 — The SCAR27 clinical spectrum includes eye-movement abnormalities and dysgraphia beyond ataxia/spasticity/cognitive impairment

Curated clinical descriptions (UniProt, derived from primary literature) characterize SCAR27 as a *"progressive disease characterized by gait difficulties, eye movement abnormalities, dysarthria, and difficulty writing. Some patients may lose independent ambulation. Additional features include spasticity of the lower limbs and cognitive impairment."* This broadens the recognized phenotype to include **oculomotor abnormalities** and **dysgraphia** alongside the cardinal cerebellar, pyramidal, and cognitive features.

The phenotypic range continues to expand. A 2025 case report described progressive slurred speech (dysarthria) as an *atypical* presenting feature in a 47-year-old man — notably **without** cerebellar atrophy on MRI — whose brother had more advanced disease with dysphagia and wheelchair dependence; whole-exome sequencing identified a homozygous nonsense GDAP2 mutation ([PMID: 42633453](https://pubmed.ncbi.nlm.nih.gov/42633453/)). This underscores that SCAR27 can present with isolated dysarthria and normal neuroimaging, and should be considered in the differential diagnosis of progressive dysarthria.

### Finding 5 — Pathogenic GDAP2 variants are uniformly loss-of-function (truncating/splice), confirming the LOF mechanism

ClinVar (RefSeq NM_017686.4) lists 112 GDAP2 variants, of which 3 are Pathogenic and 6 Likely pathogenic (the remainder largely VUS/benign). Every pathogenic/likely-pathogenic single-nucleotide variant is loss-of-function:

| Variant (cDNA) | Protein | Type | Classification |
|---|---|---|---|
| c.757C>T | p.Arg253Ter | Nonsense | Pathogenic |
| c.677C>A | p.Ser226Ter | Nonsense | Likely pathogenic |
| c.760C>T | p.Gln254Ter | Nonsense | Likely pathogenic |
| c.1048C>T | p.Arg350Ter | Nonsense | Likely pathogenic |
| c.134del | p.Pro45fs | Frameshift | Likely pathogenic |
| c.1107+1G>T | — | Canonical splice | Likely pathogenic |
| c.1030+1G>T | — | Canonical splice | Likely pathogenic |

Two large multigene 1p13 copy-number variants are also classified Pathogenic in ClinVar but are not SCAR27-specific (they span additional genes). The uniform truncating/splice signature across unrelated families strongly supports **loss of function** (not gain of function or dominant negative) as the disease mechanism, consistent with the recessive inheritance and the gnomAD constraint profile.

### Finding 6 — All GDAP2 loss-of-function animal models are invertebrate; no faithful mammalian neurodegeneration model exists

A model-organism audit found that every published GDAP2 loss-of-function model is an invertebrate:

- **Drosophila** *Gdap2* knockdown — the only neuromotor LOF model, showing shortened lifespan, motor defects, and stress hypersensitivity ([PMID: 30084953](https://pubmed.ncbi.nlm.nih.gov/30084953/)).
- **Silkworm (Bombyx mori)** CRISPR/Cas9 knockout of *BmGDAP2* (2025) — extended lifespan, reduced body size, prolonged growth cycle, and 149 differentially expressed genes enriched (KEGG) in peroxidase activity, hormone synthesis, apoptosis, and longevity regulation ([PMID: 40332832](https://pubmed.ncbi.nlm.nih.gov/40332832/)).
- **Silkworm** systemic GDAP2 knockout — delayed larval development, reduced body weight, and arrest at the 4th-instar stage; GDAP2 is a direct downstream target of the bHLH transcription factor Dimm integrating insulin/IGF and juvenile-hormone signaling ([PMID: 40205793](https://pubmed.ncbi.nlm.nih.gov/40205793/)).

Importantly, the frequently-cited rodent study used GDAP2 **overexpression** (gain of dosage) in primary hippocampal neurons and an epileptic mouse — not a knockout — finding increased dendritic complexity, dysregulated excitatory synaptic transmission, and increased seizure frequency ([PMID: 35158016](https://pubmed.ncbi.nlm.nih.gov/35158016/)). This models a dosage-gain condition, not the recessive LOF of SCAR27. Ortholog gene IDs: human GDAP2 (NCBI 54834), mouse *Gdap2* (14547), rat *Gdap2* (362004), zebrafish *gdap2* (447824), *Drosophila Gdap2* (59173), *Bombyx mori BmGDAP2* (101738783). The absence of a mammalian knockout that recapitulates adult-onset neurodegeneration is the single largest experimental gap in the field.

### Finding 7 — GDAP2 localizes to the lysosomal membrane, distinguishing it from its mitochondrial paralog GDAP1

UniProt (Q9NXN4) records a single experimentally-supported Gene Ontology cellular-component annotation for GDAP2: **GO:0005765 "lysosomal membrane"** (evidence code HDA, high-throughput direct assay). This is mechanistically important because the better-known paralog **GDAP1** (mutated in Charcot-Marie-Tooth disease) localizes to the **mitochondrial outer membrane**. Thus, despite the shared "GDAP" name and domain architecture, the two paralogs operate at different organelles. A lysosomal localization for GDAP2 reorients mechanistic thinking toward lysosomal/autophagic and membrane-lipid biology (consistent with the CRAL-TRIO/Sec14 lipid-binding domain), rather than assuming a mitochondrial role by analogy to GDAP1.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in GDAP2** (nonsense, frameshift, or canonical splice-site) *results in* absent or non-functional GDAP2 protein in all tissues. *(Demonstrated — ClinVar LOF alleles; recessive inheritance.)*
2. Loss of GDAP2 *leads to* deficient cellular stress-response capacity — the protein's macro domain (ADP-ribose/NAD metabolite binding) and CRAL-TRIO/Sec14 (lipid-binding) domains normally support stress handling at the lysosomal membrane. *(Inferred from domain architecture + GO:0005765 lysosomal localization.)*
3. Deficient stress handling *results in* heightened vulnerability of cells to **oxidative stress (reactive oxygen species)** and **nutrient deprivation**. *(Demonstrated in* Drosophila *knockdown — PMID 30084953.)*
4. In long-lived post-mitotic **neurons**, chronic exposure to oxidative/metabolic stress over decades *leads to* progressive neuronal dysfunction and death. *(Inferred — explains adult onset and slow progression.)*
5. Neurodegeneration *manifests in* the cerebellum, inferior olive, thalamus, substantia nigra, and pyramidal tracts, with limbic tau pathology. *(Demonstrated — human neuropathology, PMID 30084953.)*
6. Regional degeneration *produces* the clinical phenotype:
   - Cerebellar + olivary degeneration → **ataxia, dysarthria, oculomotor abnormalities, dysgraphia**
   - Pyramidal tract involvement → **lower-limb spasticity**
   - Cortical/thalamic/limbic + tau pathology → **cognitive impairment / dementia**
   - Progressive cerebellar/brainstem loss → **loss of independent ambulation, dysphagia**

### Branch point

```
                 Biallelic GDAP2 LOF
                         |
         (lysosomal-membrane stress-response deficit)
                         |
          Heightened vulnerability to ROS + nutrient stress
                         |
        +----------------+---------------------+
   Cerebellum/        Pyramidal            Cortex/thalamus/
   inferior olive      tracts              limbic + tau
        |                 |                      |
   Ataxia, dysarthria,  Lower-limb          Cognitive decline/
   eye movements,       spasticity           dementia
   dysgraphia
```

### Upstream vs downstream

- **Upstream (initiating):** GDAP2 LOF → lysosomal/stress-response deficit (the primary, generalizable lesion present in all cells).
- **Downstream (manifesting):** selective neuronal vulnerability and regional neurodegeneration, which is what produces symptoms. The selectivity for neurons — despite GDAP2 being ubiquitously expressed — is not fully explained and is a key open question.

### Ontology term suggestions

- **Gene/protein:** HGNC:18010 (GDAP2); UniProt Q9NXN4
- **GO biological process:** response to oxidative stress (GO:0006979); cellular response to starvation/nutrient levels (GO:0009267 / GO:0031669); neuron death (GO:0070997)
- **GO cellular component:** lysosomal membrane (GO:0005765)
- **CL cell types:** cerebellar Purkinje cell (CL:0000121); granule cell; neuron (CL:0000540); inferior olivary neuron
- **UBERON anatomy:** cerebellum (UBERON:0002037); inferior olivary complex (UBERON:0002118); thalamus (UBERON:0001897); substantia nigra (UBERON:0002038); pyramidal tract (UBERON:0002435); hippocampus (UBERON:0002421); amygdala (UBERON:0001876)
- **CHEBI:** reactive oxygen species (CHEBI:26523); ADP-ribose (CHEBI:16960)
- **Disease:** MONDO:0032706; OMIM #618369

---

## Section-by-Section Disease Characterization

### 1. Disease Information
SCAR27 is an adult-onset, autosomal recessive, slowly progressive cerebellar ataxia caused by biallelic GDAP2 loss of function. **Identifiers:** MONDO:0032706; OMIM phenotype #618369; gene OMIM *618128; HGNC:18010; UniProt Q9NXN4. No specific ICD-10/ICD-11 or MeSH code is assigned to SCAR27 as a distinct entity; it falls under hereditary/recessive cerebellar ataxia categories (e.g., ICD-10 G11.1/G11.2, broadly). **Synonyms:** autosomal recessive spinocerebellar ataxia-27; GDAP2-related cerebellar ataxia; GDAP2-related spinocerebellar ataxia. The disease-level information is derived from aggregated case reports and curated database resources (OMIM, UniProt, ClinVar), not from large patient registries or EHR cohorts — reflecting the ultra-rare status.

### 2. Etiology
**Causal factor:** purely genetic — biallelic (homozygous or compound heterozygous) loss-of-function variants in GDAP2. **Genetic risk factors:** the causal variants themselves; consanguinity substantially raises risk (several reported families are consanguineous, with homozygous null alleles). No susceptibility loci, modifier genes, protective alleles, or gene-environment interactions have been established. **Environmental/lifestyle/infectious factors:** none identified as causal or contributory. Given the stress-vulnerability mechanism, oxidative or metabolic stressors are a theoretical modifier, but this is **not demonstrated** in patients.

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset | Progression | Frequency |
|---|---|---|---|---|---|
| Cerebellar ataxia / gait difficulty | Clinical sign | HP:0001251 / HP:0002066 | 3rd–4th decade | Progressive | Core (near-universal) |
| Dysarthria | Clinical sign | HP:0001260 | Adult | Progressive | Common; can be presenting feature |
| Eye-movement abnormalities | Clinical sign | HP:0000496 | Adult | Progressive | Common |
| Lower-limb spasticity | Clinical sign | HP:0002061 | Adult | Progressive | Common |
| Dysgraphia / difficulty writing | Clinical sign | HP:0025131 | Adult | Progressive | Reported |
| Cognitive impairment / dementia | Behavioral/cognitive | HP:0001268 / HP:0000726 | Adult | Progressive | Reported in multiple cases |
| Loss of independent ambulation | Functional | HP:0002540 | Late | Progressive | Subset (wheelchair dependence) |
| Dysphagia | Clinical sign | HP:0002015 | Late | Progressive | Advanced disease |
| Cervical dystonia | Clinical sign | HP:0002402 | Adult | — | Reported (Spanish family) |

**Quality-of-life impact:** progressive loss of mobility, speech, writing, and cognition causes substantial and increasing disability; advanced patients become wheelchair-dependent with dysphagia. No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disease.

### 4. Genetic / Molecular Information
**Causal gene:** GDAP2 (HGNC:18010; gene OMIM *618128; Ensembl ENSG00000196505; NCBI Gene 54834). **Variant classes:** nonsense, frameshift, and canonical splice-site — all loss-of-function (see Finding 5 table). **Functional consequence:** loss of function (LOF). **Allele frequency:** pathogenic alleles are ultra-rare/private in gnomAD. **Origin:** germline. **Modifier/epigenetic/chromosomal:** none established specific to SCAR27; two large multigene 1p13 CNVs are pathogenic but not SCAR27-specific. gnomAD constraint (pLI≈0, LOEUF 0.96) confirms heterozygous LOF tolerance consistent with recessive disease.

### 5. Environmental Information
No environmental, lifestyle, or infectious factors are implicated in SCAR27. The disease is monogenic and fully genetically determined. (Oxidative/nutrient stress is mechanistically relevant at the cellular level but is not an established patient-level environmental risk factor.)

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the full ordered causal chain. In brief: biallelic GDAP2 LOF → loss of a lysosomal-membrane, macro-domain/CRAL-TRIO stress-response protein → impaired handling of oxidative and nutrient stress → progressive, region-selective neurodegeneration (cerebellum, inferior olive, thalamus, substantia nigra, pyramidal tracts; limbic tau) → ataxia, spasticity, and cognitive decline. Key molecular features: macro domain (ADP-ribose/NAD metabolite binding), CRAL-TRIO/Sec14 lipid-binding domain, lysosomal-membrane localization. Silkworm knockout transcriptomics highlighted peroxidase activity, apoptosis, and longevity-regulation pathways ([PMID: 40332832](https://pubmed.ncbi.nlm.nih.gov/40332832/)), consistent with a stress/oxidative-homeostasis role.

### 7. Anatomical Structures Affected
**Primary organ/system:** central nervous system (nervous system). **Primary sites:** cerebellum (UBERON:0002037) and inferior olivary complex (UBERON:0002118). **Secondary involvement:** thalamus (UBERON:0001897), substantia nigra (UBERON:0002038), pyramidal tracts (UBERON:0002435), hippocampus (UBERON:0002421), amygdala (UBERON:0001876). **Tissue/cell:** nervous tissue; cerebellar neurons (Purkinje cells CL:0000121, granule cells), olivary and brainstem neurons. **Subcellular:** lysosomal membrane (GO:0005765). **Lateralization:** bilateral/symmetric (typical of neurodegenerative ataxia).

### 8. Temporal Development
**Onset:** adult, typically 3rd–4th decade (reported onsets ~32–47 years). **Onset pattern:** insidious/chronic. **Progression:** slowly progressive over years to decades; no remission. **Course:** chronic, lifelong, progressive. Advanced disease → loss of ambulation and dysphagia. No episodic or relapsing-remitting pattern. **Critical window:** none defined; because neurodegeneration is slow, there is in principle a long window for intervention if disease-modifying therapy becomes available.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** appears complete in biallelic LOF carriers (based on limited cases). **Expressivity:** variable (ranging from isolated dysarthria with normal MRI to full ataxia-spasticity-dementia). **Consanguinity:** an important contributor; homozygous null variants have been reported in consanguineous families. **Carrier frequency:** not formally established; pathogenic alleles are private/ultra-rare. **Epidemiology:** ultra-rare — only a handful of families reported worldwide (original/Netherlands, China, Spain, and others); true prevalence/incidence unknown and likely well under 1 per million. **No founder effect, anticipation, or sex bias** has been established; as an autosomal recessive disorder, males and females are affected equally.

### 10. Diagnostics
**Genetic testing is the diagnostic cornerstone:** whole-exome sequencing (WES) or hereditary-ataxia gene panels (e.g., adult-onset hereditary ataxia panels such as PanelApp) detect biallelic GDAP2 LOF variants; whole-genome sequencing and Sanger confirmation/segregation are adjuncts. **Imaging:** brain MRI may show cerebellar atrophy, but — importantly — can be normal early or in atypical presentations ([PMID: 42633453](https://pubmed.ncbi.nlm.nih.gov/42633453/)); thus normal MRI does **not** exclude SCAR27. **Routine labs and neurophysiology** are typically unremarkable. **No specific biomarker** exists. **Differential diagnosis:** other autosomal recessive cerebellar ataxias (e.g., ATM/ataxia-telangiectasia, SACS/ARSACS, COQ8A, APTX/AOA1, SYNE1, Friedreich ataxia) — distinguished by genetic testing; GDAP2 is now included on adult-onset ataxia panels. **Screening:** cascade carrier testing within affected families; no newborn or population screening.

### 11. Outcome / Prognosis
SCAR27 is a chronic, progressive, disabling neurodegenerative disease. Patients experience accumulating disability — loss of gait, speech, writing, and cognition — with a subset becoming wheelchair-dependent and developing dysphagia. No formal survival, mortality, or life-expectancy data exist given the rarity, but as an adult-onset neurodegenerative ataxia, life expectancy may be reduced in advanced disease (e.g., via aspiration/dysphagia complications). **Prognostic factors** are not formally defined; earlier/more severe cognitive and pyramidal involvement likely portends worse functional outcome. No prognostic biomarkers are established.

### 12. Treatment
There is **no disease-modifying or curative therapy** for SCAR27. Management is **supportive and rehabilitative**: physical therapy for gait/spasticity, occupational therapy (including writing aids for dysgraphia), speech therapy for dysarthria/dysphagia, antispasticity agents (e.g., baclofen — skeletal muscle relaxant class), mobility aids, swallow management, and cognitive/social support. No pharmacotherapy, gene therapy, RNA-based therapy, or targeted therapy is approved or in trials specific to GDAP2. **NCIT intervention concepts:** Physical Therapy, Occupational Therapy, Speech Therapy, Supportive Care. Because the mechanism involves oxidative/metabolic stress vulnerability, antioxidant strategies are a theoretical direction but are **not evidence-based** for this disease.

### 13. Prevention
No primary prevention exists for a monogenic recessive disorder. **Genetic counseling** is the principal preventive tool: at-risk couples (especially consanguineous) can be offered carrier testing, and families with a known GDAP2 variant can pursue **cascade testing**, **prenatal diagnosis**, or **preimplantation genetic testing (PGT-M)**. Tertiary prevention = rehabilitative management to limit complications (falls, aspiration). No immunization or public-health intervention applies.

### 14. Other Species / Natural Disease
No naturally occurring GDAP2-related disease has been reported in companion animals or wildlife (no OMIA entry for a GDAP2 natural disease). GDAP2 is evolutionarily conserved with clear orthologs: mouse *Gdap2* (NCBI 14547), rat *Gdap2* (362004), zebrafish *gdap2* (447824), *Drosophila Gdap2* (59173), and *Bombyx mori BmGDAP2* (101738783). The macro + CRAL-TRIO domain architecture and stress-response role appear conserved from insects to humans. No zoonotic or cross-species transmission component (non-infectious disease).

### 15. Model Organisms
See Finding 6. Available LOF models are **all invertebrate**:

| Model | Type | Key phenotype | PMID |
|---|---|---|---|
| *Drosophila* *Gdap2* knockdown | RNAi knockdown | Shortened lifespan, motor defects, stress hypersensitivity | [30084953](https://pubmed.ncbi.nlm.nih.gov/30084953/) |
| Silkworm *BmGDAP2* | CRISPR/Cas9 KO | Extended lifespan, reduced size, 149 DEGs (peroxidase/apoptosis/longevity) | [40332832](https://pubmed.ncbi.nlm.nih.gov/40332832/) |
| Silkworm GDAP2 | Systemic KO | Delayed development, 4th-instar arrest; Dimm target | [40205793](https://pubmed.ncbi.nlm.nih.gov/40205793/) |
| Rodent (GDAP2 **overexpression**) | Gain of dosage (not KO) | Dendritic/synaptic changes, increased seizures | [35158016](https://pubmed.ncbi.nlm.nih.gov/35158016/) |

**No mammalian knockout** recapitulating adult-onset neurodegeneration exists. The *Drosophila* knockdown best models the neuromotor/stress phenotype; silkworm models inform development/longevity biology but not neurodegeneration. iPSC-derived neurons and conditional mouse knockouts are obvious unfilled needs.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [30084953](https://pubmed.ncbi.nlm.nih.gov/30084953/) | *GDAP2 mutations implicate susceptibility to cellular stress in a new form of cerebellar ataxia* | **Landmark** — defines SCAR27; biallelic LOF; adult onset, spasticity, dementia; Drosophila stress model; human neuropathology |
| [32437512](https://pubmed.ncbi.nlm.nih.gov/32437512/) | *Novel GDAP2 pathogenic variants … SCAR27 in a Chinese family* | Independent replication of gene-disease relationship |
| [32428220](https://pubmed.ncbi.nlm.nih.gov/32428220/) | *Homozygous GDAP2 LOF variant in adult-onset cerebellar ataxia* | Additional adult-onset LOF case |
| [40469082](https://pubmed.ncbi.nlm.nih.gov/40469082/) | *ARCA-27 … novel LOF of GDAP2 in a Spanish family* | Novel premature-stop homozygous variant; onset age 32; dysarthria→ataxia, spasticity, dystonia, cognitive impairment |
| [42633453](https://pubmed.ncbi.nlm.nih.gov/42633453/) | *Progressive slurred speech as atypical presentation of GDAP2 ataxia* | Expands spectrum — isolated dysarthria, **normal MRI**, homozygous nonsense variant |
| [35158016](https://pubmed.ncbi.nlm.nih.gov/35158016/) | *GDAP2 overexpression affects neurons / synaptic transmission* | Over-expression (gain-of-dosage) rodent study — informs GDAP2 neuronal function but **not** the recessive LOF mechanism |
| [40332832](https://pubmed.ncbi.nlm.nih.gov/40332832/) | *CRISPR/Cas9 knockout of BmGDAP2 (silkworm)* | Invertebrate KO; stress/longevity transcriptomics |
| [40205793](https://pubmed.ncbi.nlm.nih.gov/40205793/) | *Dimm targets GDAP2 to regulate larval development (silkworm)* | GDAP2 regulation and developmental KO phenotype |
| [32428197](https://pubmed.ncbi.nlm.nih.gov/32428197/) / [32658981](https://pubmed.ncbi.nlm.nih.gov/32658981/) | Reply/erratum correspondence | Document ongoing variant/family reporting |

Evidence source types: human clinical/genetic (30084953, 32437512, 32428220, 40469082, 42633453; ClinVar; UniProt; OMIM); model organism (30084953 Drosophila; 40332832, 40205793 silkworm; 35158016 rodent overexpression); computational/database (gnomAD constraint; UniProt domain and GO annotation).

---

## Limitations and Knowledge Gaps

1. **Very small patient numbers.** The disease rests on a handful of families worldwide. Phenotype frequencies, penetrance, expressivity, natural history, survival, and QoL are estimates from case reports, not cohort data.
2. **No mammalian LOF model.** All knockout models are invertebrate; the only rodent study used overexpression (opposite dosage direction). This limits mechanistic dissection and preclinical therapeutic testing.
3. **Mechanism is largely inferred.** The stress-vulnerability model is best supported in flies; the lysosomal-membrane localization is from a single high-throughput assay (GO evidence code HDA) and warrants targeted validation. Exactly how GDAP2's macro and CRAL-TRIO domains execute stress protection, and why neurons are selectively vulnerable despite ubiquitous expression, remain unknown.
4. **No biomarkers or disease-modifying therapy.** Diagnosis is genetic; there are no fluid/imaging biomarkers and no targeted treatment.
5. **Imaging can be normal**, complicating recognition; clinicians may under-diagnose SCAR27 in progressive dysarthria/ataxia without cerebellar atrophy.
6. **Epidemiology unknown** — prevalence, incidence, carrier frequency, and any founder effects are not established.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional mouse knockout** (neuronal/cerebellar Cre) and characterize for adult-onset ataxia, Purkinje/olivary degeneration, tau pathology, and stress vulnerability — the single highest-priority gap.
2. **iPSC-derived cerebellar/Purkinje neurons and organoids** from patients (and isogenic LOF lines) to test oxidative/nutrient-stress sensitivity, lysosomal/autophagic function, and candidate protective compounds (e.g., antioxidants).
3. **Validate subcellular localization and interactome** of GDAP2 at the lysosomal membrane (confocal + proximity labeling/BioID), contrasting with GDAP1's mitochondrial role; define macro-domain ADP-ribose/NAD and CRAL-TRIO lipid ligands biochemically.
4. **International patient registry / GeneMatcher-driven case collection** to establish phenotype frequencies, natural history, penetrance, imaging spectrum, and genotype-phenotype correlations.
5. **Biomarker discovery** — oxidative-stress markers, neurofilament light chain (axonal injury), and lysosomal-function readouts in patient CSF/blood.
6. **Clinical awareness** — include GDAP2 on all adult-onset hereditary-ataxia panels and consider SCAR27 in progressive dysarthria/ataxia even with normal MRI; offer genetic counseling and cascade/PGT options to affected families.

---

*Report compiled from database-verified findings (OMIM, UniProt, HGNC, Ensembl, ClinVar, gnomAD, NCBI Gene) and primary literature across 5 investigation iterations. GDAP2 is the causal gene of SCAR27 (MONDO:0032706; OMIM #618369).*


## Artifacts

- [OpenScientist final report](Spinocerebellar_Ataxia_Autosomal_Recessive_27-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spinocerebellar_Ataxia_Autosomal_Recessive_27-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001260` (1 mention) - the report calls it "Clinical sign"; HP calls it **Dysarthria**
- `HP:0000496` (1 mention) - the report calls it "Clinical sign"; HP calls it **Abnormality of eye movement**
- `HP:0002061` (1 mention) - the report calls it "Clinical sign"; HP calls it **Lower limb spasticity**
- `HP:0025131` (1 mention) - the report calls it "Clinical sign"; HP calls it **Finger swelling**
- `HP:0002540` (1 mention) - the report calls it "Functional"; HP calls it **Inability to walk**
- `HP:0002015` (1 mention) - the report calls it "Clinical sign"; HP calls it **Dysphagia**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002402` (1 mention), reported as "Clinical sign" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070997` (obsolete neuron death) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005765` (4 mentions) - the report calls it "GO cellular component:** lysosomal membrane"; GO calls it **lysosomal membrane**
- `GO:0006979` (1 mention) - the report calls it "GO biological process:** response to oxidative stress"; GO calls it **response to oxidative stress**
- `CL:0000121` (2 mentions) - the report calls it "CL cell types:** cerebellar Purkinje cell"; CL calls it **Purkinje cell**, and lists "cerebellar Purkinje cell" among its other names
- `UBERON:0002037` (2 mentions) - the report calls it "UBERON anatomy:** cerebellum"; UBERON calls it **cerebellum**
- `CHEBI:26523` (1 mention) - the report calls it "CHEBI:** reactive oxygen species"; CHEBI calls it **reactive oxygen species**