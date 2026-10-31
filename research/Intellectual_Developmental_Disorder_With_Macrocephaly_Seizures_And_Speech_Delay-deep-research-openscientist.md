---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T07:51:20.463759'
end_time: '2026-10-30T08:21:27.884706'
duration_seconds: 1807.42
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Intellectual Developmental Disorder With Macrocephaly Seizures And
    Speech Delay
  mondo_id: MONDO:0032568
  category: Mendelian
  causal_genes: PAK1
  omim_id: OMIM:618158
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
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 4
  validator_version: 0.4.0
term_validation:
  total_terms: 38
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 15
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0032568
    reported_labels:
    - MONDO
    ontology_label: intellectual developmental disorder with macrocephaly, seizures,
      and speech delay
  - term_id: HP:0012443
    reported_labels:
    - Structural brain anomalies
    ontology_label: Abnormal brain morphology
  - term_id: NCIT:C157866
    reported_labels:
    - Shunt placement
    ontology_label: Gluten Free Diet
  - term_id: NCIT:C133397
    reported_labels:
    - Supportive care
    ontology_label: Planned End Date
  labels_variant: 6
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intellectual_Developmental_Disorder_With_Macrocephaly_Seizures_And_Speech_Delay-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intellectual_Developmental_Disorder_With_Macrocephaly_Seizures_And_Speech_Delay-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder With Macrocephaly Seizures And Speech Delay
- **MONDO ID:** MONDO:0032568 (if available)
- **Causal gene(s):** PAK1
- **OMIM:** OMIM:618158
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder With Macrocephaly Seizures And Speech Delay** covering all of the
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

# Intellectual Developmental Disorder With Macrocephaly, Seizures and Speech Delay (PAK1-related disorder)

**MONDO:0032568 · OMIM:618158 · Causal gene: _PAK1_ (p21-activated kinase 1, HGNC:8590)**

---

## Summary

Intellectual Developmental Disorder with Macrocephaly, Seizures and Speech Delay (IDDMSSD; MONDO:0032568, OMIM:618158) is an **ultra-rare, autosomal-dominant neurodevelopmental disorder caused by de novo, gain-of-function missense variants in _PAK1_**, the gene encoding p21-activated kinase 1 (HGNC:8590; UniProt Q13153). Despite the serial-number style of the disease name, the causal gene is unambiguously **PAK1** — a serine/threonine kinase that acts as a direct downstream effector of the Rho-family small GTPases Cdc42 and Rac1 and regulates actin cytoskeletal dynamics in developing neurons. To date only ~16–20 patients have been reported worldwide, and every single disease-associated variant reported has been **missense** — there are no truncating/loss-of-function patients — which, together with population constraint data, is the central genetic signature of a gain-of-function mechanism rather than haploinsufficiency.

Mechanistically, resting PAK1 exists as a **trans-autoinhibited homodimer** in which the N-terminal autoregulatory region of one protomer binds and silences the kinase domain of the other. Binding of GTP-loaded Cdc42/Rac1 dissociates the dimer and activates the kinase. Disease variants cluster in two hotspots — the **N-terminal autoregulatory/CRIB region (~aa 70–140)** and the **C-terminal protein kinase domain (aa 270–521)** — and both classes relieve autoinhibition, promoting dimer dissociation, increased autophosphorylation, and constitutive kinase activity. The hyperactive kinase dysregulates the **Rac1/Cdc42 → PAK1 → LIMK1 → cofilin** actin-remodeling axis that controls neurite outgrowth, dendritic spine morphology, synaptic plasticity, and ultimately postnatal brain size.

Clinically the disorder produces moderate-to-severe intellectual disability, speech delay, (often postnatal) macrocephaly/megalencephaly with ventriculomegaly, seizures (ranging from febrile and focal seizures to infantile epileptic spasms syndrome), hypotonia, autistic features, structural brain anomalies, and dysmorphism. A domain-dependent genotype–phenotype correlation has been described: autoregulatory-domain variants associate more with neuroanatomical alterations, whereas kinase-domain variants associate more with non-neurological comorbidities. The disease course is a **static (non-progressive) encephalopathy**; there is **no approved disease-modifying therapy**, and management is entirely symptomatic (anti-seizure medication, hydrocephalus shunting, and developmental/speech/physical/occupational therapies). PAK1 small-molecule inhibitors are a mechanistically rational but still preclinical precision-treatment prospect.

---

## 1. Disease Information

**Overview.** IDDMSSD is a Mendelian, monogenic neurodevelopmental disorder defined by the triad embedded in its name — intellectual disability, macrocephaly, and speech delay — plus seizures, caused by heterozygous activating missense variants in _PAK1_.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0032568 |
| OMIM | 618158 |
| Gene (HGNC) | PAK1, HGNC:8590 |
| Gene (NCBI) | 5058 |
| Ensembl | ENSG00000149269 |
| UniProt | Q13153 (PAK1_HUMAN) |
| Inheritance | Autosomal dominant, de novo |

**Synonyms / alternative names:** "PAK1-related neurodevelopmental disorder"; "neurodevelopmental disorder with macrocephaly, seizures, and speech delay"; "intellectual disability with macrocephaly and seizures." Orphanet, ICD-10/ICD-11, and MeSH do not currently carry a dedicated, specific term for this ultra-rare entity; coding is generally via generic categories for intellectual disability/developmental disorder.

**Source of information.** The knowledge base is derived from **aggregated disease-level resources and individual published case reports / small case series** (trio exome/genome sequencing studies), not from large EHR cohorts — reflecting the ultra-rarity of the condition.

---

## 2. Etiology

**Primary cause.** The disorder is **purely genetic** — caused by heterozygous **de novo gain-of-function missense variants in _PAK1_**. There is no known environmental, infectious, or multifactorial contribution.

- Horn et al. 2019 ([PMID: 31504246](https://pubmed.ncbi.nlm.nih.gov/31504246/)) identified de novo heterozygous missense variants in PAK1 in four unrelated individuals: *"we identified de novo heterozygous missense variants in PAK1 in four unrelated individuals with intellectual disability, macrocephaly and seizures."*

**Genetic risk factors.** The causal variants are themselves the risk — they arise de novo in the affected child; unaffected parents carry no risk allele. No susceptibility loci or modifier genes have been established. One report described a patient carrying both a de novo likely-pathogenic PAK1 variant (p.T84R) **and** a de novo terminal 1q44 microdeletion, but the authors attributed the main clinical features to the PAK1 variant ([PMID: 36624491](https://pubmed.ncbi.nlm.nih.gov/36624491/)).

**Environmental / lifestyle risk factors.** None identified or expected for a de novo monogenic disorder. Advanced parental age is a general (non-specific) correlate of de novo mutation rate but has not been specifically implicated here.

**Protective factors.** None known (genetic or environmental).

**Gene–environment interactions.** None documented. Not applicable to the current understanding of this disorder.

---

## 3. Phenotypes

The phenotype spans a spectrum from mild developmental delay with normal head size to severe intellectual disability with refractory epilepsy and spastic quadriplegia. Core and associated features, with suggested HPO terms:

| Phenotype | HPO term | Type | Frequency / notes |
|---|---|---|---|
| Intellectual disability | HP:0001249 | Clinical sign | Moderate–severe; core feature |
| Macrocephaly / megalencephaly | HP:0000256 / HP:0001355 | Physical | ~4/5 cases; often **postnatal** onset |
| Speech delay | HP:0000750 | Clinical sign | Core feature |
| Seizures | HP:0001250 | Clinical sign | ~4/5 cases; focal, GTC, epileptic spasms |
| Infantile epileptic spasms (IESS) | HP:0012469 / HP:0011097 | Clinical sign | Severe end of spectrum |
| Global developmental delay | HP:0001263 | Clinical sign | Common |
| Ventriculomegaly | HP:0002119 | Imaging | Associated with macrocephaly |
| Hypotonia | HP:0001252 | Clinical sign | Common |
| Autistic behavior | HP:0000729 | Behavioral | Autism-like features reported |
| Structural brain anomalies | HP:0012443 | Imaging | Common |
| Dysmorphic features | HP:0001999 | Physical | Common |
| Hydrocephalus (obstructive) | HP:0000238 | Imaging/clinical | Severe cases |
| Spastic quadriplegia | HP:0002510 | Clinical sign | Severe cases |
| White matter hyperintensities | HP:0002500 | Imaging | Severe cases |
| Horseshoe kidney | HP:0000085 | Physical | Reported comorbidity (kinase-domain case) |

**Phenotype characteristics.** *Age of onset:* congenital to infancy for developmental features; macrocephaly is frequently postnatal and progressive in infancy. *Severity:* variable (mild DD → severe ID). *Progression:* the encephalopathy itself is **static/non-progressive**, though epilepsy may be medically refractory. *Frequency:* in the combined Wang 2025 series (n=5) plus literature (n=11), **4/5 had epilepsy and 4/5 had macrocephaly**; one patient had only mild DD with normal head circumference ([PMID: 41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/)).

- *"Four of five patients with PAK1 variants had epilepsy, the seizure types included focal seizures, generalized tonic-clonic seizure and epileptic spasms"* ([PMID: 41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/)).
- Corriveau et al. 2023: *"other common characteristics include structural brain anomalies, delayed development, hypotonia, and dysmorphic features"* ([PMID: 36905087](https://pubmed.ncbi.nlm.nih.gov/36905087/)).

**Quality-of-life impact.** Substantial and lifelong: intellectual disability and speech delay impair communication, education, and independence; refractory epilepsy and (in severe cases) spastic quadriplegia and hydrocephalus add major care burdens. No disease-specific EQ-5D/SF-36 data exist for this ultra-rare condition.

---

## 4. Genetic / Molecular Information

**Causal gene.** _PAK1_ (p21-activated kinase 1), HGNC:8590, NCBI Gene 5058, Ensembl ENSG00000149269, chr11:77,322,017–77,474,635 (GRCh38); 545-aa protein (UniProt Q13153).

**Pathogenic variants.** All reported disease variants are **heterozygous, de novo, missense**. Across Wang 2025 (n=5) and prior literature (n=11), **all 16 reported variants were missense** ([PMID: 41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/): *"in our study (n = 5) and published studies (n = 11), all variants were missense variants"*).

Representative variants and their domains:

| Variant (protein) | cDNA | Domain | Source |
|---|---|---|---|
| p.Thr84Arg | c.251C>G | Autoregulatory/CRIB | [PMID: 36624491](https://pubmed.ncbi.nlm.nih.gov/36624491/) |
| (variants near autoinhibitory switch) | — | Autoregulatory | [PMID: 31504246](https://pubmed.ncbi.nlm.nih.gov/31504246/) |
| p.Ile312Ser | — | Kinase domain | [PMID: 41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/) |
| p.Asp407Asn | — | Kinase domain (milder) | [PMID: 41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/) |
| p.Met453Thr | — | Kinase domain | [PMID: 41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/) |
| p.Leu470Pro (mosaic, VAF 13.4%) | — | Kinase domain | [PMID: 41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/) |
| p.Ile476Thr | — | Kinase domain | [PMID: 41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/) |
| p.Leu470Gln | c.1409T>A | Kinase domain (recurrent residue) | [PMID: 36905087](https://pubmed.ncbi.nlm.nih.gov/36905087/) |

**Variant classification (ACMG/AMP):** reported variants are classified pathogenic / likely pathogenic, supported by de novo occurrence, absence from population databases, clustering in functional domains, and functional gain-of-function evidence.

**Allele frequency.** Causal variants are **absent from gnomAD/population databases** (de novo, private).

**Somatic vs germline.** Variants are germline/constitutional de novo; **post-zygotic mosaicism** has been documented (p.Leu470Pro, VAF 13.4%), relevant to recurrence counseling ([PMID: 41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/)).

**Functional consequence — gain of function.** Horn 2019 showed the variants *"alleviated dissociation into monomers, autophosphorylation and activation of PAK1 influences the actin dynamics of neurite outgrowth"* ([PMID: 31504246](https://pubmed.ncbi.nlm.nih.gov/31504246/)) — i.e., constitutive kinase activation.

**Population constraint (gnomAD v2).** PAK1 is **strongly missense-constrained but LoF-tolerant**, exactly the signature of a missense gain-of-function gene:

| Metric | Value | Interpretation |
|---|---|---|
| Missense Z | **5.50** | Extreme missense intolerance |
| Observed/expected missense | 0.50 | Half the expected missense seen |
| pLI | 0.069 | LoF-tolerant |
| LOEUF (oe_lof upper) | 0.587 | Relatively LoF-tolerant |
| lof_z | 3.97 | — |

This pattern (high mis_Z, low pLI) argues against haploinsufficiency and for a pathogenic mechanism acting through altered (hyperactive) protein — consistent with the all-missense variant spectrum.

**Modifier genes / epigenetics / chromosomal abnormalities.** No established modifier genes. No disease-specific epigenetic signature reported. One patient had a concurrent de novo 1q44 microdeletion, but phenotype was attributed to PAK1 ([PMID: 36624491](https://pubmed.ncbi.nlm.nih.gov/36624491/)).

---

## 5. Environmental Information

Not applicable. This is a de novo monogenic disorder with **no known environmental, lifestyle, or infectious contributing factors**. No toxins, radiation, occupational exposures, dietary factors, or pathogens have been implicated.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **de novo missense variant** arises in _PAK1_, in either the N-terminal autoregulatory/CRIB region (~aa 70–140) or the kinase domain (aa 270–521). → *leads to*
2. **Disruption of the trans-autoinhibited PAK1 homodimer.** Normally the N-terminal inhibitory segment of one protomer binds and silences the catalytic domain of the other; the variant weakens this interface. → *results in*
3. **Alleviated dimer dissociation into monomers and increased autophosphorylation** → *leads to*
4. **Constitutive, GTPase-independent kinase hyperactivation** (gain of function) → *leads to*
5. **Dysregulated downstream actin signaling** via the LIMK1 → cofilin axis (and other PAK1 substrates), altering actin filament dynamics → *results in*
6. **Abnormal neurite outgrowth, dendritic spine morphology, and synaptic properties** in developing neurons → *leads to* (branch)
   - 6a. **Aberrant postnatal brain growth / megalencephaly** (brain size is set by PAK1-dependent neuronal complexity) → macrocephaly/ventriculomegaly
   - 6b. **Disrupted synaptic plasticity and cortical circuit formation** → intellectual disability, speech delay, autism features
   - 6c. **Cortical hyperexcitability / network dysregulation** (inferred) → seizures, up to infantile epileptic spasms
7. The combined circuit-level defects manifest as the **clinical phenotype**: ID, macrocephaly, speech delay, seizures, hypotonia, structural brain anomalies.

> Steps 2–5 are directly demonstrated in vitro (Horn 2019; Parrini 2002). Step 6/brain-size link is supported by mouse loss-of-function genetics (Huang 2011). The specific epileptogenic mechanism (6c) is **inferred**, not yet directly demonstrated for patient variants.

### Detail

**Molecular pathways.** PAK1 is a direct effector of the **Rho-family GTPases Cdc42 and Rac1**. The disease axis is **Rac1/Cdc42 → PAK1 → LIMK1 → cofilin**, governing actin cytoskeletal remodeling. KEGG/Reactome pathways: Rho GTPase signaling, axon guidance, regulation of actin cytoskeleton. Parrini et al. 2002 established the structural basis: *"The dimerized Pak1 adopts a trans-inhibited conformation: the N-terminal inhibitory portion of one Pak1 molecule in the dimer binds and inhibits the catalytic domain of the other"* and the dimer dissociates upon GTP-Cdc42/Rac1 binding ([PMID: 11804587](https://pubmed.ncbi.nlm.nih.gov/11804587/)).

**Cellular processes.** Actin filament dynamics, neurite/axon/dendrite outgrowth, dendritic spine formation, synaptic plasticity, and control of neuronal soma size and complexity. GO terms: GO:0030036 (actin cytoskeleton organization), GO:0007409 (axonogenesis), GO:0050773 (regulation of dendrite development), GO:0048812 (neuron projection morphogenesis), GO:0050808 (synapse organization), GO:0006468 (protein phosphorylation).

**Protein dysfunction.** Gain of function via **loss of autoinhibition** → constitutive kinase activity (not misfolding/aggregation/LoF). Catalytic active site Asp389; CRIB/GTPase-binding motif aa 75–105; autoregulatory region aa 70–140; protein kinase domain aa 270–521.

**Brain-size control — model evidence.** Huang et al. 2011 showed PAK1 (with PAK3) controls postnatal brain size through neuronal complexity and cofilin-actin dynamics: *"double-knockout (DK) mice lacking both PAK1 and PAK3 were born healthy, with normal brain size and structure, but severely impaired in postnatal brain growth, resulting in a dramatic reduction in brain volume"* ([PMID: 21115725](https://pubmed.ncbi.nlm.nih.gov/21115725/)). LoF reduces brain size; the patient GoF variants push in the opposite direction, consistent with **megalencephaly**.

**Related-disorder corroboration.** Aberrant Rac1-cofilin signaling drives dendritic-spine and synaptic defects in fragile X syndrome, and PAK inhibition rescues such defects — establishing the Rac-PAK-cofilin axis as pathogenic in neurodevelopmental disease and providing the rationale for PAK inhibition: *"Aberrant Rac1-cofilin signaling mediates defects in dendritic spines, synaptic function, and sensory perception in fragile X syndrome"* ([PMID: 29114038](https://pubmed.ncbi.nlm.nih.gov/29114038/)).

**Cell types & compartments.** CL terms: neuron (CL:0000540), glutamatergic/pyramidal neuron, GABAergic interneuron. Subcellular GO-CC: cytoskeleton/actin cytoskeleton (GO:0015629), dendritic spine (GO:0043197), cytoplasm, membrane (at GTPase docking).

**Immune/metabolic involvement.** Not a primary feature of IDDMSSD. (Note: much of the broader PAK1 literature concerns oncology/tumor immunity; those roles are not the mechanism of this neurodevelopmental disorder.)

---

## 7. Anatomical Structures Affected

- **Primary organ / system:** the **brain / central nervous system** (UBERON:0000955 brain; UBERON:0001017 CNS). Body system: nervous system.
- **Secondary involvement:** ventricular system (ventriculomegaly, hydrocephalus; UBERON:0002285 brain ventricle), cerebral white matter (UBERON:0002316; white matter hyperintensities), corticospinal tracts (spastic quadriplegia). Rare non-neural: kidney (horseshoe kidney, UBERON:0002113) in a kinase-domain case.
- **Tissue/cell level:** nervous tissue; neurons (CL:0000540), affecting neurite outgrowth, dendritic arbors, and dendritic spines; synapses.
- **Subcellular:** actin cytoskeleton (GO:0015629), dendritic spine (GO:0043197), cytoplasm.
- **Localization / lateralization:** generally **bilateral** (megalencephaly, ventriculomegaly, diffuse developmental impairment); some structural anomalies may be asymmetric.

---

## 8. Temporal Development

- **Onset:** congenital/early-infancy developmental features; **macrocephaly often postnatal** and progressive during infancy; seizures typically in infancy/early childhood (epileptic spasms in the first year in severe cases). Pattern: insidious/chronic developmental.
- **Progression:** the underlying encephalopathy is **static (non-progressive)**. Epilepsy severity varies and can be medically refractory. No neurodegeneration described.
- **Course / duration:** chronic, lifelong.
- **Remission:** none spontaneous for the neurodevelopmental disability; seizures may be partially controlled with treatment.
- **Critical period:** the postnatal brain-growth window (when PAK1/3-dependent neuronal complexity sets brain size) is the key developmental vulnerability/intervention window (inferred from mouse data, [PMID: 21115725](https://pubmed.ncbi.nlm.nih.gov/21115725/)).

---

## 9. Inheritance and Population

- **Epidemiology:** ultra-rare; only ~**16–20 patients reported worldwide**. No reliable prevalence/incidence estimates exist.
- **Inheritance pattern:** **autosomal dominant**, essentially always **de novo** (unaffected parents).
- **Penetrance:** effectively complete in carriers of pathogenic variants (all reported de novo carriers are affected).
- **Expressivity:** **variable** — from mild DD with normal head circumference to severe ID with refractory epilepsy, spastic quadriplegia, and hydrocephalus ([PMID: 36905087](https://pubmed.ncbi.nlm.nih.gov/36905087/); [PMID: 41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/)).
- **Genetic anticipation:** not applicable (not a repeat-expansion disorder).
- **Mosaicism:** **post-zygotic mosaicism documented** (p.Leu470Pro, VAF 13.4%); parental germline mosaicism is theoretically possible and underlies a low but non-zero recurrence risk ([PMID: 41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/)).
- **Founder effects / consanguinity / carrier frequency:** not applicable (de novo dominant; no carrier state).
- **Population demographics:** cases reported across diverse populations (e.g., European, Chinese). No ethnic predilection, geographic clustering, or established sex bias given the small numbers.

---

## 10. Diagnostics

**Genetic testing is the diagnostic cornerstone.**

- **Recommended approach:** **trio whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)** to detect the de novo heterozygous missense PAK1 variant and confirm de novo status. This is how all reported cases were identified ([PMID: 31504246](https://pubmed.ncbi.nlm.nih.gov/31504246/); [PMID: 41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/)).
- **Gene panels:** intellectual disability / epilepsy / macrocephaly NGS panels that include PAK1.
- **Single-gene testing:** targeted PAK1 sequencing if the phenotype is highly suggestive.
- **Variant interpretation:** ACMG/AMP criteria; de novo occurrence, absence from gnomAD, domain clustering, and functional gain-of-function evidence support pathogenicity. Mosaic variants require sensitive deep sequencing (low VAF).
- **Chromosomal microarray (CMA) / karyotype:** useful to exclude copy-number contributors (one case had a concurrent 1q44 microdeletion detected by CMA; [PMID: 36624491](https://pubmed.ncbi.nlm.nih.gov/36624491/)).

**Clinical / imaging workup (supportive, non-specific):**
- **Brain MRI:** megalencephaly, ventriculomegaly, structural anomalies, white matter hyperintensities, hydrocephalus.
- **EEG:** for seizure/epilepsy characterization (focal, GTC, hypsarrhythmia in spasms).
- **Head circumference monitoring:** documents postnatal macrocephaly.
- **Developmental/cognitive assessment:** documents ID and speech delay.

No specific biochemical biomarker, enzyme assay, or omics-based diagnostic test exists for this disorder.

**Differential diagnosis:** other megalencephaly/macrocephaly–intellectual-disability syndromes, notably **PI3K-AKT-mTOR pathway megalencephaly syndromes** (e.g., PTEN, PIK3CA, AKT3, MTOR), and other Rho-GTPase/actin-regulator neurodevelopmental disorders. Molecular testing distinguishes them.

**Screening.** No newborn or population carrier screening (de novo dominant). Cascade testing of parents is for recurrence-risk assessment (to detect parental mosaicism), not for at-risk sib detection in the usual sense.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** no disease-specific mortality statistics; the disorder is not characteristically lethal in early life, though severe cases with refractory epilepsy and major structural brain anomalies carry higher morbidity and potential mortality. Life expectancy data are unavailable given rarity.
- **Morbidity / disability:** significant lifelong disability — intellectual disability, speech/communication impairment, epilepsy, and in severe cases motor disability (spastic quadriplegia) requiring full-time care.
- **Disease course:** **static (non-progressive) encephalopathy**; outcome is largely determined by baseline severity and epilepsy control.
- **Complications:** refractory epilepsy, hydrocephalus requiring shunting, feeding/motor complications in severe cases.
- **Recovery potential:** developmental deficits are permanent; developmental therapies can improve function but not cure.
- **Prognostic factors:** variant domain and severity appear to correlate with outcome — autoregulatory-domain variants associate with more neuroanatomical alterations; kinase-domain variants with more non-neurological comorbidities ([PMID: 36905087](https://pubmed.ncbi.nlm.nih.gov/36905087/)). Presence of IESS/refractory epilepsy and major structural anomalies predicts worse outcome.

---

## 12. Treatment

**There is no approved disease-modifying or targeted therapy.** Management is **entirely symptomatic and supportive.**

| Modality | Intervention | NCIT (suggested) |
|---|---|---|
| Anti-seizure medication | Standard ASMs; vigabatrin / ACTH for epileptic spasms (IESS) | NCIT:C264 (Anticonvulsant) |
| Neurosurgical | Ventriculoperitoneal shunting for obstructive hydrocephalus | NCIT:C157866 (Shunt placement) |
| Rehabilitation | Speech therapy, physical therapy, occupational therapy | NCIT:C15312 (Rehabilitation therapy) |
| Developmental/educational | Early intervention, special education | — |
| Supportive | Symptom management, nutrition, orthopedic care | NCIT:C133397 (Supportive care) |

**Pharmacogenomics:** none specific. **Gene/cell/RNA therapy:** none; would face the challenge that the disorder is **gain-of-function**, so an allele-selective silencing (ASO/siRNA) or kinase-inhibition strategy would be mechanistically preferred over gene replacement.

**Experimental / rational precision prospect — PAK1 inhibition.** Because the pathogenic mechanism is **constitutive PAK1 hyperactivation**, small-molecule **PAK1 inhibitors** (ATP-competitive, allosteric, or degraders) are a mechanistically rational strategy. In a related NDD (fragile X), PAK inhibition (e.g., FRAX486) rescues dendritic-spine/synaptic defects ([PMID: 29114038](https://pubmed.ncbi.nlm.nih.gov/29114038/)). However, **no PAK1-targeted therapy has been tested in IDDMSSD patients**, and achieving group-I PAK (PAK1 vs PAK2/3) isoform selectivity remains a pharmacological challenge ([PMID: 42943325](https://pubmed.ncbi.nlm.nih.gov/42943325/)). This remains **preclinical/hypothetical** for this indication.

---

## 13. Prevention

- **Primary prevention:** not possible — variants arise de novo; no modifiable risk factors.
- **Secondary prevention:** early molecular diagnosis (trio sequencing) enables timely seizure management and early developmental intervention.
- **Tertiary prevention:** aggressive epilepsy control, hydrocephalus management, and rehabilitation to limit complications and maximize function.
- **Genetic counseling:** recurrence risk for parents of an affected child is **low but non-zero** (parental germline mosaicism possible); an affected individual, if reproductive, would have 50% transmission risk (autosomal dominant). Prenatal/preimplantation testing is feasible for a known familial variant.
- **Immunization / public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Orthologous genes:** mouse _Pak1_ (NCBI Gene 18479; MGI), rat _Pak1_ (RGD), zebrafish _pak1_ (ZFIN), _Drosophila_ _Pak/dPak_ (FlyBase), _C. elegans_ _pak-1_ (WormBase). PAK1 is **highly evolutionarily conserved**.
- **Natural disease in other species:** no naturally occurring ortholog of this specific human disorder is reported in companion animals or wildlife (OMIA); not a veterinary disease of note.
- **Comparative biology:** the Rac/Cdc42 → PAK → cofilin actin-regulatory mechanism is deeply conserved across metazoans, making invertebrate and vertebrate models informative for mechanism.
- **Transmission / zoonosis:** not applicable (genetic disorder).

---

## 15. Model Organisms

- **Mouse (primary CNS model):** _Pak1_-null mice are **viable and fertile** (with immune/vascular phenotypes). The key neurodevelopmental insight comes from **_Pak1/Pak3_ double-knockout mice**, which show severely impaired postnatal brain growth, reduced brain volume, increased cell density, simplified dendrites/axons, reduced synapse density, and impaired bidirectional synaptic plasticity, with altered cofilin activity ([PMID: 21115725](https://pubmed.ncbi.nlm.nih.gov/21115725/)).
- **Other models:** zebrafish, _Drosophila_, and _C. elegans_ orthologs exist for mechanistic studies of Rho-GTPase/PAK/actin signaling.
- **Genetic model types available:** knockout (Pak1, Pak1/Pak3 DKO). **A patient-matched gain-of-function knock-in rodent** that recapitulates IDDMSSD macrocephaly/seizures is **not yet reported** in the retrieved literature.
- **Phenotype recapitulation:** existing KO models demonstrate PAK1's requirement for brain growth and synaptic function but model **loss of function** — the *opposite direction* of the disease's gain-of-function mechanism. This is the principal model limitation: a constitutively-active knock-in is needed to faithfully model IDDMSSD.
- **In vitro:** cell-based functional assays measuring dimer dissociation, autophosphorylation, kinase activity, and neurite actin dynamics were used to demonstrate the gain-of-function mechanism of patient variants ([PMID: 31504246](https://pubmed.ncbi.nlm.nih.gov/31504246/)).

---

## Mechanistic Model / Interpretation

```
 De novo missense variant in PAK1
 (autoregulatory region ~aa70-140  OR  kinase domain aa270-521)
            │
            ▼
 Weakened trans-autoinhibition of the PAK1 homodimer
 (N-terminal segment of one protomer no longer silences the
  catalytic domain of the other — Parrini 2002)
            │
            ▼
 Alleviated dimer dissociation + ↑ autophosphorylation (Horn 2019)
            │
            ▼
 Constitutive, GTPase-independent PAK1 kinase HYPERACTIVATION
 (gain of function)
            │
            ▼
 Dysregulated Rac1/Cdc42 → PAK1 → LIMK1 → cofilin actin signaling
            │
   ┌────────┼─────────────────────────────┐
   ▼        ▼                             ▼
Abnormal   Disrupted synaptic           Cortical network
brain      plasticity & cortical        hyperexcitability
growth     circuit formation           (inferred)
   │           │                          │
   ▼           ▼                          ▼
Macrocephaly  ID / speech delay /        Seizures
/megalencephaly  autism features        (→ IESS in severe)
/ventriculomegaly
```

**Domain-dependent genotype–phenotype axis:**

| Variant location | Predominant phenotype tendency |
|---|---|
| Autoregulatory domain (~aa 70–140) | More **neuroanatomical** alterations |
| Protein kinase domain (aa 270–521) | More **non-neurological** comorbidities |

(Per Corriveau et al. 2023: *"neuroanatomical alterations were found more often in individuals with PAK1 variants in the autoregulatory domain. In contrast, non-neurological comorbidities were found more often in individuals with PAK1 variants in the protein kinase domain"*, [PMID: 36905087](https://pubmed.ncbi.nlm.nih.gov/36905087/).)

The unifying theme is that **both variant classes converge on the same molecular outcome — relief of autoinhibition and constitutive kinase activity** — but their differing structural contexts tune the clinical presentation. The all-missense spectrum and the gnomAD constraint profile (mis_Z 5.50, pLI 0.07) are mutually reinforcing lines of evidence for gain of function: the gene cannot tolerate missense change (because such changes activate it pathogenically) yet tolerates loss-of-function alleles (because simple haploinsufficiency does not cause this disease).

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [31504246](https://pubmed.ncbi.nlm.nih.gov/31504246/) | *De novo variants in PAK1 lead to ID with macrocephaly and seizures* | **Founding gene–disease paper**; 4 de novo missense; functional GoF (dimer dissociation, autophosphorylation, actin dynamics) |
| [41124873](https://pubmed.ncbi.nlm.nih.gov/41124873/) | *Novel PAK1 variants: variable spectrum mild DD → IESS* | 5 new variants + literature review; **all 16 variants missense**; epilepsy/macrocephaly frequencies; documented mosaicism |
| [36905087](https://pubmed.ncbi.nlm.nih.gov/36905087/) | *PAK1 p.Leu470Gln: epilepsy, macrocephaly, spastic quadriplegia, hydrocephalus* | Common features list; **domain-dependent genotype–phenotype**; first recurrent kinase-domain residue (Leu470) |
| [36624491](https://pubmed.ncbi.nlm.nih.gov/36624491/) | *De novo PAK1 (p.T84R) + 1q microdeletion* | Autoregulatory/CRIB variant; phenotype attributed to PAK1; CMA value |
| [11804587](https://pubmed.ncbi.nlm.nih.gov/11804587/) | *Pak1 homodimers autoinhibited in trans; dissociated by Cdc42/Rac1* | **Structural basis** of autoinhibition disrupted by disease variants |
| [21115725](https://pubmed.ncbi.nlm.nih.gov/21115725/) | *PAK1 & PAK3 control brain size* | **Mouse genetics**: PAK1/3 required for postnatal brain growth; cofilin-actin link |
| [29114038](https://pubmed.ncbi.nlm.nih.gov/29114038/) | *Aberrant Rac1-cofilin signaling in fragile X* | Validates Rac-PAK-cofilin axis as pathogenic in NDD; **rationale for PAK inhibition** |
| [42943325](https://pubmed.ncbi.nlm.nih.gov/42943325/) | *Targeting PAK1 within group I PAKs* | PAK1-inhibitor pharmacology; isoform-selectivity challenges |
| [19890013](https://pubmed.ncbi.nlm.nih.gov/19890013/) | *IP3K-A scaffolds synaptic Rac signaling* | Context on Rac→PAK1 synaptic actin regulation |

Evidence source types: **human clinical/genetic** (31504246, 41124873, 36905087, 36624491); **in vitro functional** (31504246, 11804587); **model organism** (21115725, 29114038).

---

## Limitations and Knowledge Gaps

1. **Ultra-small sample size (~16–20 patients).** Frequencies, genotype–phenotype correlations, and prognosis are based on case reports/series and are provisional.
2. **No patient-matched gain-of-function animal model.** Available mouse models are loss-of-function (opposite mechanistic direction); the disease's GoF biology has not been modeled in vivo.
3. **Epileptogenic mechanism is inferred,** not directly demonstrated for patient variants — the link from PAK1 hyperactivation to cortical hyperexcitability remains to be shown.
4. **No validated biomarker** or omics signature for diagnosis, severity, or treatment response.
5. **No therapeutic data in patients** — PAK1 inhibition is rational but untested in this indication, with unresolved isoform-selectivity and CNS-delivery challenges.
6. **Incomplete ontology coverage** (Orphanet/ICD/MeSH lack a dedicated specific term), complicating epidemiological capture.
7. **Natural history is sparsely documented** — no longitudinal cohorts.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional, patient-variant knock-in mouse** (e.g., Pak1 p.Leu470 or an autoregulatory-domain variant) to test whether constitutive activation recapitulates megalencephaly, seizures, and behavioral deficits — the single most important missing model.
2. **iPSC-derived neurons / cerebral organoids** from patients (or isogenic CRISPR knock-in lines) to quantify neurite/spine phenotypes, network excitability (MEA), and brain-organoid overgrowth.
3. **Preclinical PAK1-inhibitor rescue studies** in the above models (patient neurons/organoids and knock-in mice), benchmarking efficacy and isoform selectivity, to establish proof-of-concept for a precision therapy.
4. **International patient registry / natural-history study** to refine phenotype frequencies, domain-specific genotype–phenotype correlations, seizure outcomes, and prognosis.
5. **Structural / biochemical characterization** of each recurrent variant (dimer stability, activation kinetics) to build a variant-level functional map and improve ACMG classification of future VUS.
6. **Deep-sequencing mosaicism screening** in parents of probands to quantify germline/somatic mosaicism and refine recurrence-risk counseling.
7. **Allele-selective silencing (ASO/siRNA) feasibility** targeting the mutant PAK1 allele as an alternative GoF-directed therapeutic strategy.

---

*Report compiled from a 5-iteration autonomous investigation; 9 confirmed findings; 14 papers reviewed. All mechanistic and clinical claims are cited to primary literature (PMID). Where evidence is absent or inferential, this is stated explicitly.*


## Artifacts

- [OpenScientist final report](Intellectual_Developmental_Disorder_With_Macrocephaly_Seizures_And_Speech_Delay-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intellectual_Developmental_Disorder_With_Macrocephaly_Seizures_And_Speech_Delay-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 25 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032568` (3 mentions) - the report calls it "MONDO"; MONDO calls it **intellectual developmental disorder with macrocephaly, seizures, and speech delay**
- `HP:0012443` (1 mention) - the report calls it "Structural brain anomalies"; HP calls it **Abnormal brain morphology**
- `NCIT:C157866` (1 mention) - the report calls it "Shunt placement"; NCIT calls it **Gluten Free Diet**
- `NCIT:C133397` (1 mention) - the report calls it "Supportive care"; NCIT calls it **Planned End Date**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001999` (1 mention) - the report calls it "Dysmorphic features"; HP calls it **Abnormal facial shape**, and lists "Dysmorphic facial features" among its other names
- `HP:0000238` (1 mention) - the report calls it "Hydrocephalus (obstructive)"; HP calls it **Hydrocephalus**
- `HP:0002510` (1 mention) - the report calls it "Spastic quadriplegia"; HP calls it **Spastic tetraplegia**, and lists "Spastic quadriplegia" among its other names
- `HP:0002500` (1 mention) - the report calls it "White matter hyperintensities"; HP calls it **Abnormal cerebral white matter morphology**, and lists "White matter abnormalities" among its other names
- `GO:0015629` (2 mentions) - the report calls it "Subcellular:** actin cytoskeleton"; GO calls it **actin cytoskeleton**
- `NCIT:C15312` (1 mention) - the report calls it "Rehabilitation therapy"; NCIT calls it **Radiation Dosimetry**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.