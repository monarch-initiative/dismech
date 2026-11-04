---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T18:28:52.732147'
end_time: '2026-11-04T19:06:05.330328'
duration_seconds: 2232.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: TOPORS-Related Retinopathy
  mondo_id: MONDO:0700233
  category: Mendelian
  causal_genes: TOPORS
  omim_id: not recorded
  synonyms: retinitis pigmentosa 31; RP31
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
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 10
  off_topic: 1
  off_topic_references:
  - PMID:18356260
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 33
  verified: 31
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 21
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0007894
    reported_labels:
    - retinal pigment epithelial atrophy
    - Perivascular RPE atrophy
    ontology_label: Fundus hypopigmentation
  - term_id: GO:0120289
    reported_labels:
    - photoreceptor outer segment disc assembly
    ontology_label: obsolete positive regulation of aspartic endopeptidase activity,
      intramembrane cleaving
  - term_id: UBERON:0001789
    reported_labels:
    - photoreceptor outer segment
    ontology_label: outer nuclear layer of retina
  - term_id: MONDO:0009299
    reported_labels:
    - orofaciodigital syndrome
    ontology_label: 46 XX gonadal dysgenesis
  - term_id: HP:0000512
    reported_labels:
    - Reduced/abolished ERG
    ontology_label: Abnormal electroretinogram
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0120289
    ontology_label: obsolete positive regulation of aspartic endopeptidase activity,
      intramembrane cleaving
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: TOPORS-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: TOPORS-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TOPORS-Related Retinopathy
- **MONDO ID:** MONDO:0700233 (if available)
- **Causal gene(s):** TOPORS
- **OMIM:** not recorded
- **Synonyms:** retinitis pigmentosa 31; RP31
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **TOPORS-Related Retinopathy** covering all of the
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

# TOPORS-Related Retinopathy (Retinitis Pigmentosa 31, RP31): A Comprehensive Disease Characterization

**Disease:** TOPORS-Related Retinopathy · **Causal gene:** *TOPORS* (topoisomerase I-binding arginine/serine-rich protein, E3 ubiquitin/SUMO ligase; HGNC:21653; NCBI Gene 10210) · **MONDO:** MONDO:0700233 · **OMIM:** #609923 (RP31) · **Gene locus:** 9p21.1 · **Category:** Mendelian, autosomal dominant

---

## Summary

**TOPORS-Related Retinopathy is a rare, non-syndromic, adult-onset autosomal dominant rod–cone dystrophy (retinitis pigmentosa) caused by heterozygous truncating loss-of-function variants in the *TOPORS* gene at chromosome 9p21.1.** The gene — not to be confused with the serial "retinitis pigmentosa 31 / RP31" naming — encodes a 1045-amino-acid RING-domain dual ubiquitin/SUMO1 E3 ligase. Disease arises through **haploinsufficiency**: the absence of mutant protein in patients, combined with the ubiquitous expression of *TOPORS*, favors a reduced-dosage mechanism over a dominant-negative one. TOPORS mutations account for approximately **1% of all autosomal dominant retinitis pigmentosa (adRP)** ([PMID: 17924349](https://pubmed.ncbi.nlm.nih.gov/17924349/), [PMID: 18509552](https://pubmed.ncbi.nlm.nih.gov/18509552/)).

Mechanistically, TOPORS is a **component of the photoreceptor sensory (connecting) cilium**, localizing to basal bodies and centrosomes. Its loss impairs ciliary trafficking and the formation of photoreceptor outer segments, as demonstrated by zebrafish morpholino knockdown that produces defective retinal development rescuable by human *TOPORS* mRNA ([PMID: 21159800](https://pubmed.ncbi.nlm.nih.gov/21159800/)). A parallel retinal mechanism involves **ubiquitin-proteasome proteostasis**: a retinal yeast two-hybrid screen identified the 26S proteasome subunit PSMC1/P26s4 as a TOPORS interactor localizing to the centrosome and the RPE/photoreceptor interface ([PMID: 26872363](https://pubmed.ncbi.nlm.nih.gov/26872363/)). Clinically this produces the classic RP triad — night blindness, progressive peripheral visual-field constriction, and bone-spicule retinal pigmentation — sometimes preceded by a distinctive early perivascular cuff of RPE atrophy around the vascular arcades.

A striking feature of this gene is **dual inheritance**: while heterozygous truncating variants cause retina-only adRP, biallelic hypomorphic missense alleles (notably p.Pro10Gln, a Dominican founder allele) instead cause recessive **syndromic ciliopathies** — Joubert syndrome and oral-facial-digital syndrome ([PMID: 37227088](https://pubmed.ncbi.nlm.nih.gov/37227088/)). This allele-specific, dosage-dependent pattern unifies TOPORS disease around primary-cilium dysfunction. There is **no approved disease-specific therapy** for RP31; management is supportive, with genetic counseling and treatment of complications such as cataract and cystoid macular edema. Progression is slow but relentless, and nutritional supplementation (vitamin A / DHA) has only low-certainty evidence of benefit.

---

## Key Findings

### Finding 1 — *TOPORS* haploinsufficiency at 9p21.1 causes autosomal dominant RP (RP31)

*TOPORS* is a three-exon gene encoding a 1045-amino-acid RING-domain E3 ubiquitin/SUMO ligase located at chromosome **9p21.1**. It was identified as the RP31 gene by positional cloning. Heterozygous truncating mutations — an insertion in a French-Canadian family and a deletion in a German family, with later-described alleles such as p.Glu808X and p.Arg857GlyfsX9 — segregate with adRP. The authors concluded that **"The ubiquitous nature of TOPORS expression and a lack of mutant protein in patients are highly suggestive of haploinsufficiency, rather than a dominant negative effect"** ([PMID: 17924349](https://pubmed.ncbi.nlm.nih.gov/17924349/)). A follow-up mutation screen established that **"Point mutations and small insertions or deletions in TOPORS cause approximately 1% of adRP"** ([PMID: 18509552](https://pubmed.ncbi.nlm.nih.gov/18509552/)).

This finding anchors the disease: the causal gene is unambiguously *TOPORS*, the inheritance is autosomal dominant, the molecular lesion is loss of function, and the pathogenic mechanism is haploinsufficiency (reduced gene dosage below a functional threshold in photoreceptors).

**Ontology suggestions:** HGNC:21653 (*TOPORS*); MONDO:0700233; parent disease MONDO:0019200 (retinitis pigmentosa); GO:0061630 (ubiquitin protein ligase activity); GO:0019789 (SUMO transferase activity).

### Finding 2 — A distinctive early perivascular RPE atrophy phenotype (variable)

The original description noted **"a distinct phenotype … at the earlier stages of the disease, with an unusual perivascular cuff of retinal pigment epithelium atrophy, which was found surrounding the superior and inferior arcades in the retina"** ([PMID: 17924349](https://pubmed.ncbi.nlm.nih.gov/17924349/)). However, this feature is **not universal**: a subsequent report of two additional probands found that **"Contrary to previous reports, no distinct clinical phenotype was seen in these patients,"** who showed typical advanced adRP ([PMID: 18509552](https://pubmed.ncbi.nlm.nih.gov/18509552/)).

**Interpretation:** Perivascular RPE atrophy may be an early, stage-dependent and variably expressed sign rather than a constant diagnostic marker. It should raise suspicion for *TOPORS* in an adRP pedigree, but its absence does not exclude the diagnosis.

**Ontology suggestions:** HP:0007894 (retinal pigment epithelial atrophy); HP:0000488 (retinopathy); HP:0000510 (rod-cone dystrophy).

### Finding 3 — TOPORS is a photoreceptor connecting-cilium/basal-body protein; loss impairs outer-segment formation

TOPORS localizes to **the basal bodies of the photoreceptor connecting cilium and to centrosomes** of cultured cells, and is **"a novel component of the photoreceptor sensory cilium"** ([PMID: 21159800](https://pubmed.ncbi.nlm.nih.gov/21159800/)). Functional confirmation came from zebrafish: **"Morpholino-mediated silencing of topors in zebrafish embryos demonstrates in another species a comparable retinal problem as seen in humans, resulting in defective retinal development and failure to form outer segments"** ([PMID: 21159800](https://pubmed.ncbi.nlm.nih.gov/21159800/)). The retinal defect was rescuable by human *TOPORS* mRNA, confirming conservation.

**Interpretation:** This places RP31 within the broad class of **retinal ciliopathies**. The photoreceptor connecting cilium is the trafficking conduit between the inner segment (where proteins are synthesized) and the outer segment (the light-sensing compartment). Reduced TOPORS dosage impairs this trafficking, preventing proper outer-segment assembly/maintenance and leading to photoreceptor degeneration.

**Ontology suggestions:** GO:0060271 (cilium assembly); GO:0032391 (photoreceptor connecting cilium); GO:0120289 (photoreceptor outer segment disc assembly); CL:0000210 (photoreceptor cell); CL:0000604 (retinal rod cell); CL:0000573 (retinal cone cell); UBERON:0001789 (photoreceptor outer segment).

### Finding 4 — TOPORS is a dual ubiquitin/SUMO1 E3 ligase (STUbL) with pleiotropic nuclear functions

Beyond the retina, TOPORS is a **RING-domain dual ubiquitin and SUMO1 E3 ligase** that localizes to PML nuclear bodies and functions as a **SUMO-targeted ubiquitin ligase (STUbL)**. It **"promotes DPC repair by functioning as a SUMO-targeted ubiquitin ligase (STUbL), combining ubiquitin ligase activity through its RING domain with poly-SUMO binding via SUMO-interacting motifs, analogous to the STUbL RNF4"** ([PMID: 38649616](https://pubmed.ncbi.nlm.nih.gov/38649616/)). It regulates **p53** — it is **"an ubiquitin and small ubiquitin-like modifier ubiquitin-protein isopeptide ligase (SUMO E3) ligase"** ([PMID: 19473992](https://pubmed.ncbi.nlm.nih.gov/19473992/)) — along with NKX3.1 and SUMOylated DNMT1 crosslinks. In mice, *Topors* deficiency produces genomic instability: **"heterozygotes were found to have an increased incidence of malignancy, involving a variety of tissues"** ([PMID: 20429939](https://pubmed.ncbi.nlm.nih.gov/20429939/)).

**Interpretation:** TOPORS is a multifunctional, ubiquitously expressed protein. Its DNA-protein-crosslink-repair and p53-regulatory roles explain its emerging cancer biology (it modulates sensitivity to DNA hypomethylating agents in myeloid malignancy), but these nuclear functions are **largely distinct from — though mechanistically illuminating of — the retinal ciliary phenotype**. The post-mitotic photoreceptor is likely most sensitive to the loss of the ciliary/proteostatic pool of TOPORS rather than its genome-maintenance role.

**Ontology suggestions:** GO:0016567 (protein ubiquitination); GO:0016925 (protein sumoylation); GO:0006302 (double-strand break repair); GO:0016605 (PML body).

### Finding 5 — Substantial quality-of-life burden and treatable complications

Although RP31 itself is non-fatal, it imposes a real burden. In Australian adults with inherited retinal diseases, **"Median EQ-5D-5L utility was 0.88 and 0.91 among people with widespread and central involvement, respectively"** — the lower utility (0.88) applies to widespread retinal disease such as RP ([PMID: 38226448](https://pubmed.ncbi.nlm.nih.gov/38226448/)). Depression is an independent determinant of function: **"The RP patients with depression had poorer vision-related functions compared with those patients without depression, which cannot be explained by the visual acuity"** ([PMID: 18356260](https://pubmed.ncbi.nlm.nih.gov/18356260/)). Posterior subcapsular cataract and cystoid macular edema are frequent RP complications; cataract surgery helps: **"Mean best-corrected visual acuity significantly improved after cataract surgery, from 1.09 ± 0.69 preoperatively to 0.614 ± 0.448 at 1 month postoperatively"** ([PMID: 29217020](https://pubmed.ncbi.nlm.nih.gov/29217020/)), though RP surgery carries elevated risk of posterior capsular opacification, cystoid macular edema and zonular weakness ([PMID: 39206084](https://pubmed.ncbi.nlm.nih.gov/39206084/), [PMID: 33489339](https://pubmed.ncbi.nlm.nih.gov/33489339/)).

**Interpretation:** Management should be holistic — not only ophthalmic (treating cataract and macular edema) but also addressing mental-health comorbidity, which independently worsens functional outcomes.

### Finding 6 — TOPORS is a dual-inheritance ciliopathy gene

TOPORS causes disease through two genetically and clinically distinct routes. **Heterozygous truncating variants → non-syndromic adRP (RP31).** In contrast, **biallelic hypomorphic missense variants → recessive syndromic ciliopathy**: **"homozygosity for a TOPORS missense variant (c.29C > A; p.(Pro10Gln)) was identified in individuals with the ciliopathy oral-facial-digital syndrome in two families of Dominican descent"** and also in Joubert syndrome ([PMID: 37227088](https://pubmed.ncbi.nlm.nih.gov/37227088/)). The p.Pro10Gln allele is a **Dominican founder allele** with high carrier frequency (identified in the BioMe biobank of 1880 Dominican individuals): the authors note their data **"nominates TOPORS as a novel causal gene for JBTS and suggests that TOPORS variants should be considered in the differential of ciliopathy-spectrum disease in individuals of Dominican ancestry"** ([PMID: 37227088](https://pubmed.ncbi.nlm.nih.gov/37227088/)).

**Interpretation:** This is the unifying insight of the investigation. A gene-dosage/allele-type model explains the whole TOPORS disease spectrum:

| Genotype | Allele effect | Residual function | Phenotype | Inheritance |
|---|---|---|---|---|
| Heterozygous truncating (LOF) | ~50% dosage | Haploinsufficient in photoreceptors only | Retina-only adRP (RP31) | Autosomal dominant |
| Biallelic missense (e.g., p.Pro10Gln) | Hypomorphic | Low but non-zero, multisystem deficit | Syndromic ciliopathy (Joubert / OFD) | Autosomal recessive |

Dual-inheritance behavior is now a recognized feature of a minority of IRD genes ([PMID: 42321002](https://pubmed.ncbi.nlm.nih.gov/42321002/)).

**Ontology suggestions:** MONDO:0018772 (Joubert syndrome); MONDO:0009299 (orofaciodigital syndrome); GO:0060271 (cilium assembly).

### Finding 7 — Retinal TOPORS interactome links it to ubiquitin-proteasome proteostasis at the photoreceptor/RPE interface

A yeast two-hybrid screen of a **human retinal cDNA library** identified the 26S proteasome regulatory subunit 4 (P26s4/PSMC1) as a TOPORS interactor: **"The screen led to isolation of the 26 S protease regulatory subunit 4 (P26s4/PSMC1), an ATPase indispensable for correct functioning of UPS-mediated proteostasis"** ([PMID: 26872363](https://pubmed.ncbi.nlm.nih.gov/26872363/)). Crucially, **"TOPORS and P26s4 co-localise at the centrosome in cultured cells"** ([PMID: 26872363](https://pubmed.ncbi.nlm.nih.gov/26872363/)), with strong P26s4 reactivity at the RPE/photoreceptor interface in mouse retina. Additional TOPORS substrates relevant to retinal homeostasis include DJ-1/PARK7 and APOBEC2; in zebrafish, Toporsa interacts with Ubc9 and Pou6f2, and SUMOylation regulates APOBEC2 localization during retina regeneration ([PMID: 25190811](https://pubmed.ncbi.nlm.nih.gov/25190811/)).

**Interpretation:** This provides a **second, complementary retinal mechanism** beyond ciliary trafficking: TOPORS couples the ubiquitin-proteasome system to the centrosome/basal body. Photoreceptors have extraordinary protein turnover demands (outer-segment discs are shed and renewed daily), making them exquisitely sensitive to any reduction in proteostatic capacity. Reduced TOPORS dosage may therefore degrade both ciliary trafficking **and** protein quality control at the connecting cilium / RPE interface.

**Ontology suggestions:** GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process); GO:0005813 (centrosome); CL:0002586 (retinal pigment epithelial cell); UBERON:0001782 (retinal pigment epithelium).

### Finding 8 — Adult-onset non-syndromic rod-cone dystrophy, confirmed across diverse cohorts

Recent cohorts reaffirm the clinical picture. In a UAE series of non-syndromic adult-onset rod-cone dystrophy (symptomatic at or after age 16), **"Autosomal dominant RCD was noted in two cases, related to TOPORS and PRPF31"** ([PMID: 42627262](https://pubmed.ncbi.nlm.nih.gov/42627262/)). A 2024 case report described a novel *TOPORS* mutation with clinical findings in adRP ([PMID: 38592336](https://pubmed.ncbi.nlm.nih.gov/38592336/)). A Belgian adRP cohort also identified a novel frameshift *TOPORS* mutation among splicing-factor-dominated adRP ([PMID: 28076437](https://pubmed.ncbi.nlm.nih.gov/28076437/)). Together these confirm *TOPORS* as a recurrent, if rare, cause of **adult-onset dominant rod-cone dystrophy across diverse populations** (French-Canadian, German, US, Belgian, Chinese, Emirati).

**Ontology suggestions:** HP:0000510 (rod-cone dystrophy); HP:0007737 (bone spicule-like pigmentary changes); HP:0000662 (nyctalopia); HP:0001133 (constriction of peripheral visual field).

### Finding 9 — Slow, quantifiable progression; weak evidence for nutritional therapy

RP (including RP31) progresses slowly but measurably. In X-linked RP, **"Using different clinical biomarkers, XLRP progresses at a rate of 4 to 19% per year"** ([PMID: 33258268](https://pubmed.ncbi.nlm.nih.gov/33258268/)). Ellipsoid-zone (EZ) width on OCT is the most reliable structural biomarker: **"The ellipsoid zone line width declined with a yearly average rate of 76.4 μm (4.16%/year)"** in a sibling cohort ([PMID: 29940899](https://pubmed.ncbi.nlm.nih.gov/29940899/)). Cone function by full-field flicker ERG declines ~18.7%/year ([PMID: 33364083](https://pubmed.ncbi.nlm.nih.gov/33364083/)). For therapy, a Cochrane review is unequivocal: **"At this time, there is no proven therapy for RP"** ([PMID: 32573764](https://pubmed.ncbi.nlm.nih.gov/32573764/)). DHA slowed some visual-field outcomes only in post-hoc/ancillary analyses in XLRP ([PMID: 26469750](https://pubmed.ncbi.nlm.nih.gov/26469750/)). Progression is heterogeneous even between affected siblings ([PMID: 29940899](https://pubmed.ncbi.nlm.nih.gov/29940899/)).

**Interpretation:** EZ width should be the primary structural endpoint for any future RP31 natural-history study or trial. No supplement has proven efficacy; vitamin A/DHA should be discussed as low-certainty, not standard-of-care.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1. Heterozygous truncating variant in TOPORS (9p21.1), e.g. p.Glu808X, p.Arg857GlyfsX9
      │  leads to
      ▼
2. Nonsense-mediated decay / absence of mutant protein → ~50% reduction in
   functional TOPORS dosage (HAPLOINSUFFICIENCY; mutant protein not detected in patients)
      │  results in
      ▼
3. Reduced TOPORS at the photoreceptor connecting-cilium basal body / centrosome
      │
      ├──► BRANCH A (ciliary trafficking; DEMONSTRATED):
      │      impaired protein transport through the connecting cilium
      │          │ leads to
      │          ▼
      │      failure of photoreceptor OUTER-SEGMENT formation/maintenance
      │      (shown in zebrafish knockdown)
      │
      └──► BRANCH B (proteostasis; INFERRED for retina):
             reduced TOPORS–PSMC1(26S proteasome) coupling at the centrosome
             and RPE/photoreceptor interface
                 │ leads to
                 ▼
             impaired ubiquitin-proteasome protein quality control in cells
             with extreme protein-turnover demand
      │
      ▼  (branches converge)
4. Progressive PHOTORECEPTOR DEGENERATION (rods first, then cones)
      │  results in
      ▼
5. Rod dysfunction → nyctalopia (night blindness); sometimes early
   perivascular RPE atrophy around arcades
      │  leads to
      ▼
6. Progressive mid-peripheral then peripheral visual-field constriction;
   bone-spicule pigmentation; later cone involvement → central acuity loss
      │  leads to
      ▼
7. Secondary complications: posterior subcapsular cataract, cystoid macular
   edema → further visual impairment and reduced quality of life
```

Steps 1–2 and Branch A are **demonstrated** (human genetics + zebrafish). Branch B is **supported by protein-interaction/localization data but not yet proven to drive degeneration in vivo** — it is the strongest candidate second mechanism. Steps 5–7 are **clinically established** for RP generally and observed in RP31 cohorts.

### Dual-inheritance dosage model

```
TOPORS functional dosage ───────────────────────────────────────►
   0% ............ low (hypomorphic) ............ 50% ............ 100%
   │                      │                          │                │
 (lethal?)        BIALLELIC missense          HETEROZYGOUS         normal
                  p.Pro10Gln (Dominican       truncating LOF
                  founder) → RECESSIVE         → DOMINANT
                  SYNDROMIC ciliopathy         RETINA-ONLY adRP
                  (Joubert / OFD)              (RP31)
```

The retina is the most dosage-sensitive tissue (50% is enough to cause isolated retinopathy), whereas multisystem ciliopathy requires a deeper, biallelic reduction in function.

### Upstream vs downstream summary

| Level | Element | Status |
|---|---|---|
| Upstream trigger | *TOPORS* truncating variant, haploinsufficiency | Demonstrated (human) |
| Proximal molecular | Loss of basal-body/centrosomal TOPORS; impaired cilium trafficking | Demonstrated (localization + zebrafish) |
| Parallel molecular | Reduced UPS proteostasis (PSMC1/DJ-1/APOBEC2) | Supported (interactome) |
| Cellular | Outer-segment failure → photoreceptor death | Demonstrated / inferred |
| Tissue | Rod > cone loss; RPE atrophy | Clinical |
| Organ | Progressive retinal degeneration | Clinical |
| Secondary | Cataract, CME, QoL/mental-health burden | Clinical |

---

## Section-by-Section Disease Characterization

### 1. Disease Information
Non-syndromic, adult-onset autosomal dominant retinitis pigmentosa caused by *TOPORS*. **Identifiers:** OMIM #609923 (RP31); MONDO:0700233; gene *TOPORS* HGNC:21653, NCBI Gene 10210, Ensembl ENSG00000197579; locus 9p21.1. **Synonyms:** Retinitis pigmentosa 31, RP31, TOPORS-related adRP, TOPORS-related rod-cone dystrophy. **Source type:** aggregated disease-level resources (OMIM, Orphanet) plus individual case reports/cohorts.

### 2. Etiology
**Primary cause:** genetic — heterozygous truncating (nonsense/frameshift/insertion/deletion) LOF variants in *TOPORS* (germline). **Genetic risk:** carrying one pathogenic *TOPORS* allele (autosomal dominant). No established environmental risk or protective factors specific to RP31; general RP care avoids excessive vitamin A toxicity. **Gene–environment interactions:** not characterized for RP31.

### 3. Phenotypes (suggested HPO terms with typical characteristics)

| Phenotype | HPO | Type | Onset | Progression | Frequency |
|---|---|---|---|---|---|
| Nyctalopia (night blindness) | HP:0000662 | Symptom | Adult | Progressive | Typical/early |
| Peripheral field constriction | HP:0001133 | Sign | Adult | Progressive | Typical |
| Rod-cone dystrophy | HP:0000510 | Sign | Adult | Progressive | Defining |
| Bone-spicule pigmentation | HP:0007737 | Sign | Adult | Progressive | Common |
| Perivascular RPE atrophy | HP:0007894 | Sign | Early | — | Variable |
| Reduced/abolished ERG | HP:0000512 | Lab | Adult | Progressive | Typical |
| Posterior subcapsular cataract | HP:0007787 | Complication | Adult | Progressive | Common (RP) |
| Cystoid macular edema | HP:0011505 | Complication | Adult | Fluctuating | Common (RP) |

**Severity:** variable; **QoL impact:** EQ-5D-5L utility ~0.88 for widespread retinal involvement ([PMID: 38226448](https://pubmed.ncbi.nlm.nih.gov/38226448/)); depression independently worsens function ([PMID: 18356260](https://pubmed.ncbi.nlm.nih.gov/18356260/)).

### 4. Genetic / Molecular Information
**Causal gene:** *TOPORS* (OMIM *609507), 3 exons, 1045 aa, RING-domain dual ubiquitin/SUMO1 E3 ligase. **Variant types:** truncating — nonsense (p.Glu808X), frameshift (p.Arg857GlyfsX9), small insertions/deletions; classified pathogenic/likely pathogenic per ACMG. **Allele frequency:** rare/absent in gnomAD for truncating adRP alleles. **Origin:** germline. **Functional consequence:** loss of function → haploinsufficiency. **Dual-inheritance allele:** biallelic missense p.Pro10Gln (c.29C>A), hypomorphic, Dominican founder → recessive ciliopathy ([PMID: 37227088](https://pubmed.ncbi.nlm.nih.gov/37227088/)). **Modifier genes / epigenetics / chromosomal abnormalities:** none established for RP31.

### 5. Environmental Information
No established environmental, lifestyle, or infectious contributors. The disease is monogenic/Mendelian.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and mechanistic model above. Key pathways: cilium assembly (GO:0060271), ubiquitin/SUMO conjugation (GO:0016567, GO:0016925), proteasomal degradation (GO:0043161). Cell types: photoreceptors (CL:0000210; CL:0000604 rod; CL:0000573 cone), RPE (CL:0002586). Subcellular: connecting cilium/basal body (GO:0032391), centrosome (GO:0005813), PML body (GO:0016605).

### 7. Anatomical Structures Affected
**Primary organ:** eye/retina (UBERON:0000970 eye; UBERON:0000966 retina). **Tissue/cell:** neural retina photoreceptor layer, RPE; rods affected before cones. **Subcellular:** photoreceptor outer segment (UBERON:0001789), connecting cilium, centrosome/basal body. **Localization:** bilateral, typically symmetric; early perivascular RPE atrophy around superior/inferior vascular arcades.

### 8. Temporal Development
**Onset:** adult (symptomatic at/after ~age 16); insidious, chronic. **Course:** slowly progressive, lifelong, no remission. **Progression rate:** EZ width ~4.2%/year; cone ffERG ~18.7%/year; overall biomarker decline ~4–19%/year ([PMID: 33258268](https://pubmed.ncbi.nlm.nih.gov/33258268/), [PMID: 29940899](https://pubmed.ncbi.nlm.nih.gov/29940899/), [PMID: 33364083](https://pubmed.ncbi.nlm.nih.gov/33364083/)); heterogeneous even between siblings.

### 9. Inheritance and Population
**Inheritance:** autosomal dominant (truncating LOF). **Penetrance:** high but may be age-dependent; **expressivity:** variable. **Frequency:** ~1% of adRP ([PMID: 18509552](https://pubmed.ncbi.nlm.nih.gov/18509552/)); overall RP prevalence ~1 in 3,700–4,000 (RP31 is a small fraction of that). **Founder effect:** p.Pro10Gln in Dominican ancestry (recessive syndromic form). **Sex ratio:** no strong predilection; autosomal. No anticipation or repeat-expansion mechanism.

### 10. Diagnostics
**Genetic testing** is definitive: WES/WGS or targeted adRP/IRD NGS gene panels including *TOPORS*; single-gene testing after a suggestive pedigree. **Clinical tests:** full-field ERG (reduced/abolished rod then cone responses), OCT (EZ width — key biomarker), fundus autofluorescence, visual fields (progressive constriction), fundus exam (bone spicules, perivascular RPE atrophy). **Differential diagnosis:** other adRP genes — *RHO*, *RP1*, *PRPH2*, splicing factors *PRPF31/PRPF8/SNRNP200* ([PMID: 28076437](https://pubmed.ncbi.nlm.nih.gov/28076437/)), *NR2E3*, *PROM1*; and distinguishing syndromic ciliopathies when biallelic *TOPORS* variants are found.

### 11. Outcome / Prognosis
**Not life-limiting** (no mortality). **Morbidity:** progressive, irreversible vision loss leading to legal blindness in many over decades; EZ loss and ERG decline predict course. **Complications:** cataract (PSC), cystoid macular edema, posterior capsular opacification. **Recovery:** none spontaneously; cataract surgery can improve acuity (logMAR 1.09→0.61) ([PMID: 29217020](https://pubmed.ncbi.nlm.nih.gov/29217020/)). **Prognostic biomarkers:** EZ width, ffERG amplitude.

### 12. Treatment
**No approved disease-specific therapy** — **"there is no proven therapy for RP"** ([PMID: 32573764](https://pubmed.ncbi.nlm.nih.gov/32573764/)). **Supportive:** low-vision aids, genetic counseling. **Complication management:** phacoemulsification + IOL for cataract (NCIT: Phacoemulsification); carbonic anhydrase inhibitors / anti-VEGF considered for CME. **Nutritional:** vitamin A/DHA — low-certainty, not standard-of-care; DHA benefit only in post-hoc analyses ([PMID: 26469750](https://pubmed.ncbi.nlm.nih.gov/26469750/)). **Experimental/future:** because the mechanism is LOF/haploinsufficiency, RP31 is theoretically amenable to **gene augmentation** (AAV-*TOPORS*); antisense/RNA approaches are advancing for other adRP genes (e.g., *PRPF31*, *RHO*) but none exists for *TOPORS* yet.

### 13. Prevention
No primary prevention (genetic disease). **Secondary/tertiary:** regular ophthalmic monitoring; early cataract/CME management. **Genetic counseling** (50% transmission risk, autosomal dominant); carrier/cascade testing; prenatal/preimplantation genetic testing available for known familial variants. For Dominican-ancestry families, counsel on the recessive syndromic p.Pro10Gln allele.

### 14. Other Species / Natural Disease
**Orthologs:** zebrafish *toporsa/toporsb* (retinal model), mouse *Topors* (Gene 106021; KO → genomic instability/malignancy, [PMID: 20429939](https://pubmed.ncbi.nlm.nih.gov/20429939/)), *Drosophila* *dtopors* (meiotic/nuclear-structure role, [PMID: 21900273](https://pubmed.ncbi.nlm.nih.gov/21900273/)). No well-documented naturally occurring companion-animal RP31 equivalent; mechanism conserved across vertebrates. Not zoonotic.

### 15. Model Organisms
**Zebrafish** morpholino knockdown — best disease-relevant model; recapitulates outer-segment failure, rescuable by human mRNA ([PMID: 21159800](https://pubmed.ncbi.nlm.nih.gov/21159800/)). **Mouse** *Topors* knockout — models the genomic-instability/tumor role, not the retinal phenotype directly ([PMID: 20429939](https://pubmed.ncbi.nlm.nih.gov/20429939/)). **Cellular:** hTERT-RPE1 and 661W cells used for TOPORS/PSMC1 centrosomal localization ([PMID: 26872363](https://pubmed.ncbi.nlm.nih.gov/26872363/)). **Limitation:** no published knock-in mouse replicating human haploinsufficiency adRP; a *Topors*+/− retinal-aging model is a clear gap.

---

## Evidence Base

| PMID | Title (abbreviated) | Supports / Role |
|---|---|---|
| [17924349](https://pubmed.ncbi.nlm.nih.gov/17924349/) | *Mutations in TOPORS cause adRP with perivascular RPE atrophy* | Establishes *TOPORS*/9p21.1 as RP31 gene; haploinsufficiency; perivascular phenotype |
| [18509552](https://pubmed.ncbi.nlm.nih.gov/18509552/) | *Mutations in TOPORS cause 1% of adRP* | Quantifies contribution; variable phenotype |
| [21159800](https://pubmed.ncbi.nlm.nih.gov/21159800/) | *TOPORS … is a cilia-centrosomal protein* | Ciliary localization; zebrafish outer-segment failure |
| [26872363](https://pubmed.ncbi.nlm.nih.gov/26872363/) | *TOPORS interacts with PSMC1 (26S subunit)* | Retinal proteostasis mechanism |
| [37227088](https://pubmed.ncbi.nlm.nih.gov/37227088/) | *TOPORS as a novel causal gene for Joubert syndrome* | Dual inheritance; recessive syndromic ciliopathy; Dominican founder allele |
| [38649616](https://pubmed.ncbi.nlm.nih.gov/38649616/) | *TOPORS/RNF4 STUbL activities* | Defines STUbL / DPC-repair molecular function |
| [19473992](https://pubmed.ncbi.nlm.nih.gov/19473992/) | *Plk1-mediated phosphorylation of Topors regulates p53* | Dual ligase; p53 regulation |
| [20429939](https://pubmed.ncbi.nlm.nih.gov/20429939/) | *Topors deficiency → genetic instability/malignancy in mice* | In vivo tumor-suppressor function; mouse KO |
| [42627262](https://pubmed.ncbi.nlm.nih.gov/42627262/) | *Non-syndromic adult-onset rod-cone dystrophy* | Confirms TOPORS in recent AD RCD cohort |
| [38592336](https://pubmed.ncbi.nlm.nih.gov/38592336/) | *adRP secondary to TOPORS: novel mutation* | Recent clinical confirmation |
| [28076437](https://pubmed.ncbi.nlm.nih.gov/28076437/) | *Splicing-factor genes in Belgian adRP* | Novel TOPORS frameshift; differential-diagnosis context |
| [38226448](https://pubmed.ncbi.nlm.nih.gov/38226448/) | *EQ-5D-5L utilities in IRD* | QoL burden |
| [18356260](https://pubmed.ncbi.nlm.nih.gov/18356260/) | *Depression and QoL in RP* | Mental-health comorbidity |
| [29217020](https://pubmed.ncbi.nlm.nih.gov/29217020/) | *Cataract surgery outcomes in retinal dystrophy* | Treatable complication |
| [39206084](https://pubmed.ncbi.nlm.nih.gov/39206084/) / [33489339](https://pubmed.ncbi.nlm.nih.gov/33489339/) | *Cataract surgery in RP* | Surgical risks/benefits |
| [32573764](https://pubmed.ncbi.nlm.nih.gov/32573764/) | *Cochrane: vitamin A / fish oils for RP* | No proven therapy |
| [26469750](https://pubmed.ncbi.nlm.nih.gov/26469750/) | *DHAX trial (DHA in XLRP)* | Weak/ancillary nutritional evidence |
| [33258268](https://pubmed.ncbi.nlm.nih.gov/33258268/) / [29940899](https://pubmed.ncbi.nlm.nih.gov/29940899/) / [33364083](https://pubmed.ncbi.nlm.nih.gov/33364083/) | *RP natural history / biomarkers* | Progression rates (EZ, ffERG) |
| [25190811](https://pubmed.ncbi.nlm.nih.gov/25190811/) | *Apobec2 / Toporsa in zebrafish retina regeneration* | TOPORS–SUMO–APOBEC2 retinal axis |
| [42321002](https://pubmed.ncbi.nlm.nih.gov/42321002/) | *Dual-inheritance IRD genes* | Context for dual-inheritance behavior |
| [21900273](https://pubmed.ncbi.nlm.nih.gov/21900273/) | *dTopors in Drosophila meiosis* | Conservation; nuclear-structure role |

**Evidence source distribution:** human clinical genetics (multiple cohorts/case reports), in vitro/cell biology (yeast two-hybrid, co-IP, localization), model organism (zebrafish, mouse, Drosophila), and systematic review/Cochrane for therapy.

---

## Limitations and Knowledge Gaps

1. **No RP31-specific natural-history study.** Progression rates cited are from RP broadly (largely XLRP/*USH2A*); gene-specific RP31 kinetics are unknown.
2. **Branch B (proteostasis) is not proven in vivo.** The TOPORS–PSMC1 link rests on interaction/localization data; whether reduced proteostasis drives photoreceptor death in a *TOPORS*+/− retina is untested.
3. **No haploinsufficiency mouse model** replicating the adRP phenotype; existing KO models the genome-instability/cancer role instead.
4. **Small patient numbers.** RP31 is ~1% of adRP; genotype–phenotype correlation (e.g., which truncating positions cause perivascular atrophy) is underpowered.
5. **Penetrance/expressivity not precisely quantified** for *TOPORS* adRP.
6. **No targeted therapy or trial** exists for *TOPORS*; gene-augmentation feasibility (promoter, dosage, AAV tropism to photoreceptors) is unexplored.
7. **Dual-inheritance thresholds** (how much residual function separates retina-only from syndromic disease) are inferred, not measured.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a *Topors* heterozygous / photoreceptor-conditional mouse** and perform longitudinal OCT/ERG to test whether haploinsufficiency alone causes age-dependent rod-cone degeneration, and to directly test the proteostasis (Branch B) hypothesis.
2. **Patient-derived iPSC retinal organoids** carrying truncating *TOPORS* alleles to quantify outer-segment formation, ciliary trafficking, and proteasome function; test AAV-*TOPORS* rescue.
3. **RP31-specific natural-history registry** using EZ width (OCT) as the primary structural endpoint and ffERG as functional endpoint, to establish gene-specific progression rates for future trial design.
4. **Deep genotype–phenotype study** across all reported *TOPORS* families to test whether perivascular RPE atrophy correlates with variant position/type, and to estimate penetrance/expressivity.
5. **Structure–function dosage experiments** on the p.Pro10Gln hypomorph vs truncating alleles to quantify the residual-activity threshold separating retina-only from syndromic ciliopathy.
6. **Gene-augmentation proof-of-concept:** optimize AAV-*TOPORS* vector/promoter for photoreceptor dosage; because the mechanism is LOF, augmentation (rather than suppression/editing) is the rational strategy.
7. **Carrier-screening guidance for Dominican-ancestry populations** given the p.Pro10Gln founder allele, to inform recessive-ciliopathy counseling.

---

*Report compiled from 9 confirmed findings across 5 investigation iterations and 48 reviewed papers. Evidence spans human clinical genetics, cell biology, and model-organism studies. All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](TOPORS-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](TOPORS-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 10 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:18356260` (6 mentions) - Depression and the vision-related quality of life in patients with retinitis pigmentosa.
  - shared terms: function

Weighed against this report's own most characteristic terms: `topor`, `rp31`, `adrp`, `retinal`, `disease`, `gene`, `photoreceptor`, `function`, `rpe`, `mechanism`, `autosomal`, `dominant`, `genetic`, `truncating`, `atrophy`, `cause`, `haploinsufficiency`, `allele`, `cataract`, `clinical`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 29 |
| Terms named correctly | 21 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0007894` (2 mentions) - the report calls it "retinal pigment epithelial atrophy", "Perivascular RPE atrophy"; HP calls it **Fundus hypopigmentation**
- `GO:0120289` (1 mention) - the report calls it "photoreceptor outer segment disc assembly"; GO calls it **obsolete positive regulation of aspartic endopeptidase activity, intramembrane cleaving**
- `UBERON:0001789` (2 mentions) - the report calls it "photoreceptor outer segment"; UBERON calls it **outer nuclear layer of retina**
- `MONDO:0009299` (1 mention) - the report calls it "orofaciodigital syndrome"; MONDO calls it **46 XX gonadal dysgenesis**
- `HP:0000512` (1 mention) - the report calls it "Reduced/abolished ERG"; HP calls it **Abnormal electroretinogram**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0120289` (obsolete positive regulation of aspartic endopeptidase activity, intramembrane cleaving) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007737` (2 mentions) - the report calls it "bone spicule-like pigmentary changes", "Bone-spicule pigmentation"; HP calls it **Spicular pigmentation of the retina**, and lists "Bone spicule pigmentation of the retina" among its other names
- `HP:0000662` (2 mentions) - the report calls it "nyctalopia", "Nyctalopia (night blindness)"; HP calls it **Nyctalopia**, and lists "Night blindness" among its other names
- `HP:0001133` (2 mentions) - the report calls it "constriction of peripheral visual field", "Peripheral field constriction"; HP calls it **Constriction of peripheral visual field**, and lists "Visual field constriction" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0007894` - called "retinal pigment epithelial atrophy", "Perivascular RPE atrophy"
- `HP:0000510` - called "rod-cone dystrophy", "Rod-cone dystrophy"
- `HP:0007737` - called "bone spicule-like pigmentary changes", "Bone-spicule pigmentation"
- `HP:0000662` - called "nyctalopia", "Nyctalopia (night blindness)"
- `HP:0001133` - called "constriction of peripheral visual field", "Peripheral field constriction"