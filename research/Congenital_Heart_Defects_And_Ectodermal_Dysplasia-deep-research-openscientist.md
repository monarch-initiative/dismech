---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T17:10:51.753118'
end_time: '2026-10-24T17:29:11.727304'
duration_seconds: 1099.97
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Heart Defects And Ectodermal Dysplasia
  mondo_id: MONDO:0044303
  category: Mendelian
  causal_genes: PRKD1
  omim_id: not recorded
  synonyms: CHDED; CHDFIDD; congenital heart defects, dysmorphic facial features,
    and intellectual developmental disorder; telangiectasia-ectodermal dysplasia-brachydactyly-cardiac
    anomaly syndrome; TEBC syndrome; PRKD1-related syndrome
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
citation_count: 14
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 8
  off_topic: 1
  off_topic_references:
  - PMID:15590638
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 44
  verified: 43
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 13
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0007394
    reported_labels:
    - Telangiectasia** of childhood onset
    ontology_label: Prominent superficial blood vessels
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Heart_Defects_And_Ectodermal_Dysplasia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Heart_Defects_And_Ectodermal_Dysplasia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Heart Defects And Ectodermal Dysplasia
- **MONDO ID:** MONDO:0044303 (if available)
- **Causal gene(s):** PRKD1
- **OMIM:** not recorded
- **Synonyms:** CHDED; CHDFIDD; congenital heart defects, dysmorphic facial features, and intellectual developmental disorder; telangiectasia-ectodermal dysplasia-brachydactyly-cardiac anomaly syndrome; TEBC syndrome; PRKD1-related syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Heart Defects And Ectodermal Dysplasia** covering all of the
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

# Congenital Heart Defects and Ectodermal Dysplasia (CHDED / TEBC Syndrome): A Comprehensive Disease Characterization

**Disease:** Congenital Heart Defects and Ectodermal Dysplasia (CHDED)
**Causal gene:** *PRKD1* (protein kinase D1; HGNC:9407; NCBI Gene 5587; UniProt Q15139)
**MONDO ID:** MONDO:0044303 · **OMIM:** #617364
**Synonyms:** CHDED; CHDFIDD; congenital heart defects, dysmorphic facial features, and intellectual developmental disorder; telangiectasia–ectodermal dysplasia–brachydactyly–cardiac anomaly (TEBC) syndrome; PRKD1-related syndrome; PRKD1 gain-of-function syndrome
**Category:** Mendelian, autosomal dominant

---

## Summary

Congenital Heart Defects and Ectodermal Dysplasia (**CHDED**, also called **TEBC syndrome**) is an ultra-rare, autosomal dominant, multisystem developmental disorder caused by heterozygous — usually *de novo* — pathogenic variants in **PRKD1**, the gene encoding **protein kinase D1**, a diacylglycerol/PKC-activated serine–threonine kinase. The disorder is defined by the co-occurrence of **congenital heart defects** and **ectodermal dysplasia**, frequently accompanied by **telangiectasia**, **brachydactyly/skeletal anomalies**, **facial dysmorphism**, and variable **neurodevelopmental, renal, endocrine, and cerebrovascular** features. Only approximately 8–10 molecularly confirmed patients had been reported in the literature as of 2024–2025, so all disease-level knowledge derives from aggregated individual case reports and functional/model-organism studies rather than population registries.

A central, well-supported conclusion of this investigation is that *PRKD1* exhibits a **dual genetic architecture**. **Biallelic truncating (loss-of-function) variants** cause an isolated recessive outflow-tract malformation (**truncus arteriosus**), first mapped in consanguineous families, whereas **heterozygous missense (and in-frame splice) variants clustered in the catalytic kinase domain** cause the dominant syndromic disorder CHDED. Population constraint data (gnomAD pLI ≈ 0; LOEUF ≈ 0.81) indicate that simple haploinsufficiency is largely tolerated, arguing that the dominant syndrome operates through a **gain-of-function / dominant-negative** mechanism — a conclusion reinforced by newer clinical-genetics reports that explicitly term the disorder a "**PRKD1 gain-of-function syndrome**."

Mechanistically, PRKD1 functions downstream of PKC/diacylglycerol and directly phosphorylates the class IIa histone deacetylase **HDAC5**, driving its nuclear export and thereby **derepressing MEF2** transcription factors that govern cardiac gene programs. A parallel, proposed branch links PRKD1 to an **endothelial ITGB2/JAM2 tight-junction pathway** implicated in brain and organ calcification. GTEx expression data show PRKD1 is enriched in **arteries, fibroblasts, nerve, and renal medulla**, mirroring the vascular/outflow-tract, ectodermal, and renal phenotypes. Diagnosis is genotype-driven (trio exome/genome sequencing); there is **no disease-specific or molecularly targeted therapy**, and management is entirely supportive and multidisciplinary.

---

## Key Findings

### F001 — CHDED is an autosomal dominant syndrome caused by *PRKD1* variants

CHDED (MIM #617364; MONDO:0044303) is an **autosomal dominant** disorder caused by **heterozygous pathogenic variants in PRKD1**, characterized mainly by congenital heart defects and ectodermal dysplasia with variable skeletal, neurodevelopmental, facial, and other features. It is also known as **TEBC** (telangiectasia–ectodermal dysplasia–brachydactyly–cardiac anomaly) syndrome and **CHDFIDD**. Most dominant cases arise from *de novo* missense variants, and only ~8–10 patients were described as of 2024.

> *"Congenital heart disease and ectodermal dysplasia syndrome (CHDED syndrome) (MIM: 617364) is an autosomal dominant disorder cause by PRKD1 gene pathogenic variants, characterised mainly by congenital heart defects (CHD) and ectodermal dysplasia, along with other variable clinical features (including skeletal defects)."* — [PMID: 41136760](https://pubmed.ncbi.nlm.nih.gov/41136760/)

> *"Telangiectasia-ectodermal dysplasia-brachydactyly-cardiac anomaly (TEBC) syndrome is a rare autosomal dominant condition, recently linked to the protein kinase D1 (PRKD1) gene."* — [PMID: 38677542](https://pubmed.ncbi.nlm.nih.gov/38677542/)

### F002 — Dual genetic architecture: dominant missense (syndromic) vs. recessive truncating (isolated truncus arteriosus)

Shaheen et al. (2015) first mapped *PRKD1* by autozygosity in two consanguineous Saudi families with **truncus arteriosus (TA)**, identifying **homozygous truncating mutations** — a recessive loss-of-function mechanism causing isolated outflow-tract defects. In contrast, syndromic CHDED/TEBC is caused by **heterozygous (usually *de novo*) missense variants** acting via a gain-of-function/dominant mechanism (e.g., p.Arg603His / c.1808G>A; p.Val712Met / c.2134G>A). Newer reports explicitly describe a "PRKD1 Gain-of-Function Syndrome." A novel splice variant (c.1906-1G>T) causing exon 14 skipping was reported in a familial case.

> *"we demonstrate in two multiplex consanguineous families that we are able to map TA to regions of autozygosity in which whole-exome sequencing revealed homozygous truncating mutations in PRKD1 (encoding a kinase derepressor of MAF2) and NRP1"* — [PMID: 25713110](https://pubmed.ncbi.nlm.nih.gov/25713110/)

> *"The patient had a de novo, heterozygous pathogenic variant, c.1808G > A, p.(Arg603His), in the PRKD1 gene."* — [PMID: 39740729](https://pubmed.ncbi.nlm.nih.gov/39740729/)

| Feature | Recessive form | Dominant form (CHDED/TEBC) |
|---|---|---|
| Zygosity | Biallelic (homozygous) | Heterozygous |
| Variant type | Truncating (LoF) | Missense / in-frame splice |
| Mechanism | Loss of function | Gain-of-function / dominant-negative |
| Phenotype | Isolated truncus arteriosus | Multisystem syndrome |
| Typical origin | Consanguinity | *De novo* (rarely inherited) |
| Landmark ref. | [PMID: 25713110](https://pubmed.ncbi.nlm.nih.gov/25713110/) | [PMID: 27479907](https://pubmed.ncbi.nlm.nih.gov/27479907/) |

### F005 — *PRKD1* established as a genome-wide-significant syndromic CHD gene (Sifrim 2016)

Sifrim et al. (2016, *Nature Genetics*) exome-sequenced **1,891 CHD probands** (610 syndromic, 1,281 nonsyndromic) and identified **three genome-wide-significant syndromic-CHD disorders** caused by *de novo* mutations in **CHD4, CDK13, and PRKD1**. Syndromic CHD showed enrichment of *de novo* protein-truncating variants in known CHD genes, whereas nonsyndromic CHD showed enrichment of inherited PTVs — evidence for "distinct genetic architectures." This is the landmark study establishing *PRKD1* as a cause of dominant syndromic CHD, complementing the earlier recessive TA mapping.

> *"We identified three genome-wide significant S-CHD disorders caused by DNMs in CHD4, CDK13 and PRKD1."* — [PMID: 27479907](https://pubmed.ncbi.nlm.nih.gov/27479907/)

> *"Our study finds evidence for distinct genetic architectures underlying the low sibling recurrence risk in S-CHD and NS-CHD."* — [PMID: 27479907](https://pubmed.ncbi.nlm.nih.gov/27479907/)

### F004 — Phenotype spectrum: four cardinal features plus neurodevelopmental, renal, and cerebrovascular involvement

Across the ~8–10 reported patients, the **core tetrad** comprises:

1. **Congenital heart defects** — atrioventricular septal defect (partial/complete; HP:0006695), pulmonary/pulmonic stenosis (HP:0001642), coarctation of the aorta (HP:0001680), bicuspid aortic valve (HP:0001647), truncus arteriosus, tetralogy of Fallot (HP:0001636), partial anomalous pulmonary venous return (PAPVR);
2. **Ectodermal dysplasia** (HP:0000968) affecting hair, nails, teeth, and skin;
3. **Telangiectasia** of childhood onset (HP:0007394);
4. **Brachydactyly / skeletal defects** (HP:0001156).

Additional variable features include facial dysmorphism (HP:0001999), intellectual disability (HP:0001249) with microcephaly (HP:0000252), multicystic renal dysplasia (HP:0000003), nephrocalcinosis/renal calcification (HP:0000121), cerebral (deep white-matter) calcification (HP:0002514) with seizures (HP:0001250), increased intracranial pressure, bifid uvula (HP:0000193), sagittal craniosynostosis (HP:0004440), hormonal resistance, and (in an adult) bilateral carotid artery dissection.

> *"The proband presents with partial atrioventricular septal defect, brachydactyly, ectodermal dysplasia, telangiectasia that developed in childhood, intellectual disability with microcephaly, multicystic renal dysplasia and moderate hormonal resistance."* — [PMID: 38677542](https://pubmed.ncbi.nlm.nih.gov/38677542/)

> *"Individuals with a heterozygous mutation in PRKD1 may have facial dysmorphism, ectodermal dysplasia and may have CHDs such as pulmonary stenosis, atrioventricular septal defects, coarctation of the aorta and bicuspid aortic valve."* — [PMID: 38419169](https://pubmed.ncbi.nlm.nih.gov/38419169/)

> *"Previously unreported features were noted including high intracranial pressure (ICP), partial anomalous pulmonary venous return (PAPVR), and bifid uvula."* — [PMID: 36308391](https://pubmed.ncbi.nlm.nih.gov/36308391/)

### F009 — Pathogenic missense variants cluster in the catalytic kinase domain

PRKD1 (UniProt Q15139, 912 aa) comprises two phorbol-ester/DAG-binding **C1 zinc fingers** (~residues 146–196 and 270–320), a **pleckstrin-homology (PH) domain** (~422–541), and a C-terminal **serine/threonine kinase domain** (~583–839), with the catalytic proton-acceptor active site at Asp706 and activation-loop autophosphorylation/PKC sites at Ser738/Ser742 (also reported as Ser744/Ser748). Reported pathogenic CHDED missense variants map **inside the kinase domain**: **p.Arg603His** (c.1808G>A), **p.Val712Met** (c.2134G>A), and the splice variant **c.1906-1G>T**, which causes skipping of exon 14 within the kinase-domain-encoding region. Relevant GO annotations: GO:0004672 (protein kinase activity), GO:0004697 (diacylglycerol-dependent serine/threonine kinase activity), GO:0005524 (ATP binding), GO:0006468 (protein phosphorylation).

> *"We identified a novel heterozygous splice variant in PRKD1 (c.1906-1 G > T) in the proband, inherited from the affected father. Transcript analysis confirmed that the PRKD1 splice variant caused the complete skipping of exon 14."* — [PMID: 41136760](https://pubmed.ncbi.nlm.nih.gov/41136760/)

> *"We report on the 8th patient carrying a heterozygous de novo variation of PRKD1 c.2134G > A, p. (Val712Met)"* — [PMID: 38677542](https://pubmed.ncbi.nlm.nih.gov/38677542/)

### F008 — gnomAD constraint supports gain-of-function, not haploinsufficiency

*PRKD1* (ENSG00000184304; HGNC:9407; chr14q12; GRCh38 14:29,576,479–30,191,898, minus strand; canonical transcript ENST00000331968 with 18 exons; protein 912 aa). gnomAD v2 constraint metrics: **pLI ≈ 0** (8.5e-14), **observed/expected LoF = 0.66** (LOEUF oe_lof_upper = 0.81; obs 63 vs. exp 95.9 LoF variants), **missense Z = 1.47** (oe_mis = 0.90), **LoF Z = 2.85**. PRKD1 is only moderately LoF-constrained and is **not predicted to be haploinsufficient** (pLI ≈ 0): simple heterozygous loss of function is largely tolerated in the general population, consistent with a gain-of-function/dominant-negative basis for the dominant syndrome.

> *"Expanding the Phenotypic Spectrum of PRKD1 Gain-of-Function Syndrome"* — [PMID: 42792942](https://pubmed.ncbi.nlm.nih.gov/42792942/) (title framing independently supports the gain-of-function inference)

### F003 — Core molecular mechanism: PKC → PKD1 → HDAC5 phosphorylation/nuclear export → MEF2 derepression

*PRKD1* encodes a serine/threonine protein kinase activated downstream of PKC/DAG via activation-loop phosphorylation (Ser744/Ser748). A core validated function is **direct phosphorylation of class IIa histone deacetylase HDAC5**, driving its CRM1-dependent **nuclear export** and thereby **derepressing MEF2** transcription factors that control cardiac gene programs. Shaheen et al. describe PRKD1 as "a kinase derepressor of MEF2." *Prkd1*-null mice are embryonic lethal, and tissue-specific deletion causes abnormal cardiac remodeling. A gain-of-function missense variant would be expected to **increase** HDAC5 phosphorylation and MEF2 activity.

> *"protein kinase D (PKD), a downstream effector of PKC, directly phosphorylates HDAC5 and stimulates its nuclear export"* — [PMID: 15367659](https://pubmed.ncbi.nlm.nih.gov/15367659/)

> *"Previous work has demonstrated that Prkd1(-/-) is embryonic lethal and that its tissue-specific deletion results in abnormal heart remodelling"* — [PMID: 25713110](https://pubmed.ncbi.nlm.nih.gov/25713110/)

### F006 — Brain/organ calcification via a proposed PRKD1–ITGB2–JAM2 endothelial tight-junction pathway

Watanabe et al. (2025) reported a 9-month-old girl with CHDED (*de novo* p.Arg603His) presenting with heart defects, ectodermal dysplasia, seizures, and **bilateral deep cerebral white-matter calcifications** (seizures controlled with levetiracetam). Reviewing prior cases, calcifications occurred in **3 of 8 patients** (2 renal, 1 brain). The authors propose that PRKD1 acts in a **common pathway with ITGB2 and JAM2** — both established primary familial brain calcification genes — where PRKD1 partners with integrin ITGB2 and JAM2 maintains endothelial tight junctions, implicating **neurovascular unit / blood–brain-barrier dysfunction**.

> *"We propose that PRKD1 and two genes, ITGB2 and JAM2, which are known to be associated with brain calcification, act through a common signaling pathway abnormality."* — [PMID: 39740729](https://pubmed.ncbi.nlm.nih.gov/39740729/)

> *"At 6 months of age, she had generalized seizures, and a CT scan revealed calcifications in the bilateral deep cerebral white matter."* — [PMID: 39740729](https://pubmed.ncbi.nlm.nih.gov/39740729/)

### F012 — PRKD1 expression is enriched in arterial/vascular, fibroblast, nerve, and renal-medulla tissue

GTEx v8 median expression shows *PRKD1* is highest in **cultured fibroblasts (45.8 TPM)** and **arteries** — aorta 24.8, tibial 21.3, coronary 19.4 TPM — plus testis (22.2), tibial nerve (21.6), prostate (21.5), **kidney medulla (20.1)**, ovary (19.3), and bladder (18.7), but **low in adult heart left ventricle (1.4 TPM)**, skeletal muscle (0.9), liver (0.8), and whole blood (0.04). The strong arterial/vascular-smooth-muscle, fibroblast (mesenchymal), and renal-medulla expression parallels the disease's outflow-tract/arterial heart defects (truncus arteriosus, coarctation, bicuspid aortic valve), cutaneous telangiectasia, carotid artery dissection, and renal dysplasia/nephrocalcinosis.

> *"Congenital Heart Disease, Bilateral Carotid Dissections, and Ectodermal Dysplasia in an Adult Patient"* — [PMID: 42792942](https://pubmed.ncbi.nlm.nih.gov/42792942/) (vascular manifestation matches PRKD1's high arterial expression)

**Affected anatomy (UBERON):** heart (UBERON:0000948), cardiac outflow tract (UBERON:0004145), aorta (UBERON:0000947), skin (UBERON:0002097), kidney (UBERON:0002113), brain (UBERON:0000955), teeth (UBERON:0001091), hair follicle (UBERON:0002073).
**Cell types (CL):** endothelial cell (CL:0000115), vascular smooth muscle cell (CL:0000359), fibroblast (CL:0000057), cardiac neural crest-derived cells, keratinocyte (CL:0000312).

### F007 — *Prkd1* mouse models recapitulate cardiac developmental defects

*Prkd1* knockout is embryonic lethal, and tissue-specific deletion produces abnormal heart remodeling. Waheed-Ullah et al. (2024) analyzed a *Prkd1* transgenic mouse model to study its role in cardiogenesis and CHD, framing PRKD1 as "an essential protein kinase" important in cardiac morphogenesis. Mouse *Prkd1* (NCBI Gene 18760) is the ortholog of human *PRKD1* (NCBI Gene 5587; HGNC:9407); the kinase is broadly conserved.

> *"To obtain a greater appreciation for the role that this essential protein kinase plays in cardiogenesis and CHD, we have analysed a Prkd1 transgenic mouse model"* — [PMID: 38419169](https://pubmed.ncbi.nlm.nih.gov/38419169/)

### F011 — Epidemiology and inheritance: ultra-rare, mostly *de novo*, with rare familial transmission and variable expressivity

CHDED/TEBC is **ultra-rare**: only ~8–10 molecularly confirmed patients reported as of 2024–2025; no population prevalence/incidence estimates exist. Inheritance is **autosomal dominant**. Most dominant cases are *de novo* heterozygous missense (e.g., p.Arg603His, p.Val712Met), but **vertical transmission occurs** — a familial case showed an affected father transmitting a splice variant (c.1906-1G>T) to an affected son with differential manifestation (TOF + sagittal craniosynostosis in the son vs. septal defects only in the father), demonstrating **intrafamilial variable expressivity**. No sex predilection, founder effect, anticipation, or carrier-frequency data are established; the separate recessive TA form was enriched by consanguinity in Saudi families.

> *"To date, eight patients with CHDED have been described."* — [PMID: 39740729](https://pubmed.ncbi.nlm.nih.gov/39740729/)

> *"born of non-consanguineous Asian Indian origin couple with affected father and unaffected mother"* — [PMID: 41136760](https://pubmed.ncbi.nlm.nih.gov/41136760/)

### F010 — Management is symptomatic/multidisciplinary; no targeted therapy exists

No CHDED/TEBC-specific or PRKD1-targeted therapy, clinical trial, gene therapy, or approved drug exists (ultra-rare; no NCT trials identified). Management is **supportive and organ-directed**: surgical/interventional repair of congenital heart defects (AVSD/VSD closure, coarctation repair, valve management); antiepileptic drugs for seizures (**levetiracetam** was effective and resolved seizures in the brain-calcification patient); dental, dermatologic, and hair/nail care for ectodermal dysplasia; neurodevelopmental/early-intervention and physical/occupational/speech therapy for developmental delay; nephrology surveillance for renal dysplasia/calcification; neurosurgical management of raised intracranial pressure/craniosynostosis; and vascular surveillance given reported carotid dissection in an adult. Genetic counseling is indicated.

> *"The seizures resolved with the administration of levetiracetam."* — [PMID: 39740729](https://pubmed.ncbi.nlm.nih.gov/39740729/)

### F014 — Diagnosis rests on trio exome/genome sequencing plus multi-organ imaging; no biomarker exists

All reported CHDED diagnoses were **molecular**, via trio whole-exome sequencing (WES) identifying *de novo*/inherited heterozygous *PRKD1* variants, often after SNP-microarray excluded CNVs including the **22q11.2 deletion**. WES/WGS and multigene congenital-heart/syndromic-CHD panels (which include *PRKD1* alongside *CDK13*, *CHD4*) are the recommended approach; single-gene *PRKD1* testing applies when the phenotype is recognized. Supporting phenotyping includes echocardiography/cardiac imaging; brain/renal CT or ultrasound for calcifications; EEG for seizures; renal ultrasound for multicystic dysplasia; skeletal radiographs for brachydactyly/craniosynostosis; and dental/dermatologic exam. **No specific laboratory biomarker** exists; diagnosis is genotype-driven. Differential diagnoses include 22q11.2 deletion/DiGeorge, other ectodermal dysplasias, Adams–Oliver and TEBC-overlapping syndromes, and PHACE/other CHD syndromes.

> *"Whole exome sequencing was performed on a 7-year-old male proband with CHD"* — [PMID: 41136760](https://pubmed.ncbi.nlm.nih.gov/41136760/)

> *"molecular karyotyping to exclude 22q11.2 deletion syndrome"* — [PMID: 25713110](https://pubmed.ncbi.nlm.nih.gov/25713110/)

---

## Mechanistic Model / Interpretation

### Integrated causal chain (F013)

The following ordered chain runs from the initiating genetic lesion to the clinical manifestations. Steps are marked **[demonstrated]** (directly shown experimentally) or **[inferred]** (plausible but not yet proven for patient variants).

1. A **heterozygous, usually *de novo* missense variant** in the PRKD1 kinase domain (e.g., p.Arg603His, p.Val712Met) or an **in-frame splice alteration** (exon-14 skipping) arises. **[demonstrated: human genetics — [PMID: 27479907](https://pubmed.ncbi.nlm.nih.gov/27479907/), [39740729](https://pubmed.ncbi.nlm.nih.gov/39740729/), [41136760](https://pubmed.ncbi.nlm.nih.gov/41136760/)]**
2. This **alters PRKD1 serine/threonine kinase catalytic output** — gain-of-function/dominant-negative rather than haploinsufficiency (supported by gnomAD pLI ≈ 0 and "gain-of-function syndrome" framing). **[inferred]**
3. Dysregulated **PKC/DAG → PKD1 signaling** perturbs direct substrate phosphorylation, canonically **class IIa HDAC5 phosphorylation and CRM1-dependent nuclear export**. **[demonstrated in cardiomyocytes — [PMID: 15367659](https://pubmed.ncbi.nlm.nih.gov/15367659/)]**
4. Altered HDAC5 export changes **MEF2-dependent transcriptional programs** ("PRKD1 a derepressor of MEF2"). **[demonstrated in model systems; inferred for patient variants]**
5. In parallel, PRKD1 dysfunction disturbs an **endothelial ITGB2/JAM2 tight-junction pathway**. **[inferred — [PMID: 39740729](https://pubmed.ncbi.nlm.nih.gov/39740729/)]**
6. These transcriptional/cytoskeletal/junctional perturbations **disrupt morphogenesis of PRKD1-expressing lineages** — cardiac neural crest and second-heart-field/outflow-tract mesenchyme, vascular endothelium/smooth muscle, ectodermal appendages, and renal/neural tissue. **[inferred from expression + model data]**
7. **Branching to clinical manifestations** (see diagram below).

```
  Heterozygous de novo PRKD1 kinase-domain missense / splice variant
        (p.Arg603His, p.Val712Met, c.1906-1G>T)      [demonstrated]
                         |
                         v
   Altered PKD1 catalytic output (gain-of-function / dominant-negative)  [inferred]
                         |
         +---------------+-----------------------+
         v                                       v
  PKC/DAG -> PKD1 -> HDAC5 phospho /        PRKD1-ITGB2 / JAM2
  nuclear export -> MEF2 derepression        endothelial tight-junction
  [demonstrated in cardiomyocytes]           branch  [inferred]
         |                                       |
         v                                       v
  Dysregulated cardiac / mesenchymal       Neurovascular-unit / BBB
  transcriptional programs                 dysfunction; calcification
         |                                       |
         v                                       v
  Disrupted morphogenesis of PRKD1-expressing lineages
  (cardiac neural crest, OFT mesenchyme, endothelium/VSMC,
   ectoderm, renal, neural)  [inferred from expression+models]
                         |
   +---------+---------+---------+---------+---------+---------+
   v         v         v         v         v         v         v
  CHD     Ectodermal  Telangi-  Brachy-   Neuro:    Renal:    Endocrine:
  (OFT,   dysplasia   ectasia + dactyly / microceph dysplasia hormonal
  septal, (hair/nail/ carotid   cranio-   ID, brain /nephro-  resistance
  valve,  teeth/skin) dissection synostosis calcif,  calcinosis
  arch)                                    seizures
```

**Upstream vs. downstream.** The mutation and altered kinase activity are the most upstream events. The **PKD1→HDAC5→MEF2** axis and the **ITGB2/JAM2** branch are midstream signaling nodes. The tissue-specific morphogenetic failures and resulting malformations are the downstream clinical endpoints.

**Key GO terms:** GO:0007507 (heart development), GO:0003151 (outflow tract morphogenesis), GO:0001525 (angiogenesis), GO:0016477 (cell migration), GO:0006468 (protein phosphorylation), GO:0000122 (negative regulation of transcription). **Subcellular (GO CC):** GO:0005829 (cytosol), GO:0005794 (Golgi apparatus), GO:0005634 (nucleus), GO:0005886 (plasma membrane).

### Final synthesis (F015)

Integrating all findings: **CHDED/TEBC** (MONDO:0044303, OMIM #617364, HGNC:9407 *PRKD1*, chr14q12) is autosomal dominant and ultra-rare (~8–10 patients). Pathogenic heterozygous missense/splice variants cluster in the **catalytic kinase domain** (aa ~583–839; p.Arg603His, p.Val712Met, c.1906-1G>T); gnomAD constraint (pLI ≈ 0, LOEUF ≈ 0.81) argues against haploinsufficiency and for **gain-of-function/dominant-negative**, contrasting with biallelic truncating LoF causing recessive isolated truncus arteriosus. Mechanism: **PKC/DAG → PKD1 → HDAC5 nuclear export → MEF2 transcription** (demonstrated in cardiomyocytes) plus a parallel **endothelial ITGB2/JAM2** branch; GTEx shows PRKD1 enriched in **arteries/fibroblasts/kidney-medulla** matching the outflow-tract, vascular, ectodermal, and renal phenotypes. Diagnosis is by trio WES/WGS; management is supportive; mouse *Prkd1* knockout is embryonic-lethal with cardiac remodeling defects.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [25713110](https://pubmed.ncbi.nlm.nih.gov/25713110/) | Positional mapping of PRKD1, NRP1, PRDM1 in truncus arteriosus | Establishes recessive LoF arm; PRKD1 as MEF2 derepressor; mouse KO lethality; 22q11.2 exclusion |
| [27479907](https://pubmed.ncbi.nlm.nih.gov/27479907/) | Distinct genetic architectures for syndromic/nonsyndromic CHD (Sifrim 2016, *Nat Genet*) | Landmark: PRKD1 genome-wide-significant dominant syndromic CHD gene by *de novo* mutation |
| [15367659](https://pubmed.ncbi.nlm.nih.gov/15367659/) | PKC/PKD mediate cardiac hypertrophy via HDAC5 nuclear export | Demonstrates the core PKD1→HDAC5→MEF2 mechanistic step |
| [38677542](https://pubmed.ncbi.nlm.nih.gov/38677542/) | PRKD1-related TEBC syndrome: case report & review | Phenotype tetrad + neuro/renal/endocrine; 8th patient (p.Val712Met) |
| [39740729](https://pubmed.ncbi.nlm.nih.gov/39740729/) | Brain calcification in CHDED | p.Arg603His; ITGB2/JAM2 branch; levetiracetam; case count (8 patients) |
| [41136760](https://pubmed.ncbi.nlm.nih.gov/41136760/) | TOF & craniosynostosis in familial CHDED (novel splice variant) | Familial AD transmission; c.1906-1G>T exon-14 skipping; variable expressivity; WES |
| [38419169](https://pubmed.ncbi.nlm.nih.gov/38419169/) | Deletion of PRKD1 in mouse embryonic heart | CHD types; *Prkd1* transgenic mouse model; "essential protein kinase" |
| [36308391](https://pubmed.ncbi.nlm.nih.gov/36308391/) | Increased intracranial pressure in CHDED | Phenotype expansion: ICP, PAPVR, bifid uvula |
| [42792942](https://pubmed.ncbi.nlm.nih.gov/42792942/) | Expanding PRKD1 Gain-of-Function Syndrome (adult) | "Gain-of-function" framing; carotid dissections; vascular manifestation |

**Supporting mechanistic literature (PKD1 biology).** A substantial body of cardiomyocyte and lymphocyte signaling work corroborates the PKD1→HDAC5→MEF2 axis and PKD1 activation requirements: PKC-dependent activation-loop phosphorylation at Ser744/Ser748 ([PMID: 15590638](https://pubmed.ncbi.nlm.nih.gov/15590638/)); spatiotemporal PKD activation and HDAC5 export in adult cardiomyocytes ([PMID: 21795686](https://pubmed.ncbi.nlm.nih.gov/21795686/), [PMID: 22581927](https://pubmed.ncbi.nlm.nih.gov/22581927/)); AKAP-Lbc scaffolding of PKD→HDAC5 in hypertrophy ([PMID: 18951085](https://pubmed.ncbi.nlm.nih.gov/18951085/)); and PKD/CaMKIIδ upregulation redistributing HDAC5 in heart failure ([PMID: 18218981](https://pubmed.ncbi.nlm.nih.gov/18218981/)). These papers were used to understand normal PKD1 function; they concern hypertrophy/heart-failure signaling in adult myocardium rather than the developmental malformation that defines CHDED, so they support the mechanistic model indirectly.

**Note on evidence source types.** Disease-defining evidence is **human clinical** (case reports and the Sifrim exome cohort). Mechanistic evidence is **in vitro / model-organism** (cardiomyocyte signaling, mouse knockouts). Constraint and expression inferences are **computational** (gnomAD, GTEx). The gain-of-function conclusion is an **inference** triangulated from constraint data and the clinical "gain-of-function syndrome" framing, not yet a direct biochemical demonstration for patient variants.

---

## Section-by-Section Coverage

**1. Disease information.** See F001. Identifiers: MONDO:0044303; OMIM #617364; HGNC:9407 (*PRKD1*). Orphanet/ICD-11 entries are not firmly recorded for this ultra-rare entity. Information is derived from **aggregated individual case reports**, not EHR/registry data.

**2. Etiology.** Primary cause is **genetic** — heterozygous *de novo* (rarely inherited) *PRKD1* missense/splice variants (F001, F002). No established environmental risk or protective factors; no gene–environment interactions documented. The only "modifier"-type observation is intrafamilial variable expressivity (F011).

**3. Phenotypes.** See F004, with HPO terms and the one quantified frequency available (calcification in 3/8 patients). Onset is **congenital** for heart/skeletal features; telangiectasia develops in childhood; seizures/ICP are childhood-onset; carotid dissection was adult-onset. Severity and quality-of-life impact are variable and dominated by cardiac and neurodevelopmental burden; no formal QoL instrument data exist for this disorder.

**4. Genetic/molecular information.** Causal gene *PRKD1* (F001, F008, F009). Variant types: missense (p.Arg603His, p.Val712Met), in-frame splice (c.1906-1G>T → exon-14 skipping) for the dominant syndrome; truncating (biallelic) for the recessive form. Functional consequence: likely gain-of-function/dominant-negative (dominant) vs. loss-of-function (recessive). Germline origin; no somatic/cancer association relevant here. No established modifier genes; no epigenetic or chromosomal-abnormality associations beyond excluding 22q11.2.

**5. Environmental information.** Not applicable — no toxic, lifestyle, or infectious contributors identified for this Mendelian disorder.

**6. Mechanism/pathophysiology.** Full causal chain in the Mechanistic Model section (F003, F006, F013).

**7. Anatomical structures affected.** Organ level: heart (outflow tract, septa, valves, aortic arch), skin/ectodermal appendages, arteries/vasculature, kidney, brain, skeleton, endocrine axes. UBERON/CL terms listed in F012.

**8. Temporal development.** Congenital onset of structural defects; childhood emergence of telangiectasia, seizures, calcifications; the critical window is **embryonic cardiac/neural-crest morphogenesis**. The structural malformation course is non-progressive once formed, but complications (ICP, seizures, vascular dissection) can be progressive/episodic.

**9. Inheritance and population.** See F011. Autosomal dominant, mostly *de novo*; penetrance appears high but with **variable expressivity**; no prevalence/incidence, founder, anticipation, or carrier-frequency data.

**10. Diagnostics.** See F014. Trio WES/WGS; syndromic-CHD gene panels; confirmatory cardiac/renal/brain imaging and EEG; no biomarker.

**11. Outcome/prognosis.** No formal survival data. Prognosis is driven by severity of CHD (and its surgical repair) and by neurodevelopmental/renal/vascular complications. Recovery of structural defects is surgical; neurodevelopmental deficits persist.

**12. Treatment.** See F010. Supportive and multidisciplinary; NCIT concepts: surgical repair of cardiac defect, anticonvulsant therapy (levetiracetam), supportive care, genetic counseling. No pharmacogenomic or targeted options.

**13. Prevention.** No primary prevention (genetic etiology). Secondary/tertiary prevention via early cardiac/renal/neuro surveillance and complication management. **Genetic counseling** (autosomal dominant; mostly *de novo* with low recurrence, but 50% for an affected transmitting parent); prenatal/preimplantation and cascade testing possible once a familial variant is known.

**14. Other species / natural disease.** Mouse *Prkd1* (NCBI Gene 18760) is the conserved ortholog; no naturally occurring companion-animal disease reported. No zoonotic relevance.

**15. Model organisms.** Mouse is the principal model (F007): *Prkd1* knockout is embryonic lethal; tissue-specific deletion causes abnormal heart remodeling; a *Prkd1* transgenic model was used to study cardiogenesis/CHD ([PMID: 38419169](https://pubmed.ncbi.nlm.nih.gov/38419169/)). Limitation: existing mouse data model loss-of-function, whereas the dominant human syndrome is gain-of-function — a **knock-in** of a patient missense allele would be required to fully recapitulate CHDED.

---

## Limitations and Knowledge Gaps

- **Very small sample size.** Only ~8–10 molecularly confirmed dominant cases exist, so phenotype frequencies, penetrance, expressivity, and genotype–phenotype correlations are preliminary and subject to ascertainment bias.
- **Gain-of-function is inferred, not biochemically proven for patient variants.** The conclusion rests on gnomAD constraint (tolerance of LoF) and the clinical "gain-of-function syndrome" label. No published enzyme-kinetic or cellular assay directly demonstrates increased (or dominant-negative) kinase activity for p.Arg603His or p.Val712Met.
- **No patient-allele animal model.** Mouse data are from knockouts/transgenics modeling loss-of-function; they do not test the dominant missense mechanism.
- **The ITGB2/JAM2 calcification branch is a hypothesis.** It is proposed from gene-pathway overlap, not demonstrated for PRKD1 variants.
- **No epidemiology, QoL, survival, or natural-history data.** Prevalence/incidence are unknown; long-term outcomes are inferred from individual case follow-up.
- **No targeted therapy or clinical trial.** Management is entirely empirical/supportive.

---

## Proposed Follow-up Experiments / Actions

1. **Functional validation of gain-of-function.** Express patient variants (p.Arg603His, p.Val712Met) in cells and measure in-vitro kinase activity, activation-loop autophosphorylation, and HDAC5 phosphorylation/nuclear export vs. wild-type and kinase-dead controls to directly test the gain-of-function vs. dominant-negative hypothesis.
2. **Knock-in animal model.** Generate a heterozygous *Prkd1* patient-allele knock-in mouse (or zebrafish) to test whether it recapitulates outflow-tract/septal defects and ectodermal/renal phenotypes — the decisive test of the dominant mechanism.
3. **Test the ITGB2/JAM2 branch.** Use co-immunoprecipitation, endothelial tight-junction/permeability assays, and blood–brain-barrier models with PRKD1 variants to confirm or refute the proposed calcification pathway.
4. **Patient registry and deep phenotyping.** Establish an international CHDED/TEBC registry (via GeneMatcher and syndromic-CHD consortia) to accumulate cases, quantify penetrance/expressivity, and define genotype–phenotype correlations.
5. **Developmental expression mapping.** Single-cell/spatial transcriptomics of PRKD1 in human and mouse embryonic heart (outflow tract, cardiac neural crest), skin, and kidney to pinpoint the vulnerable cell populations.
6. **Diagnostic standardization.** Ensure *PRKD1* is included in all syndromic-CHD and ectodermal-dysplasia gene panels; define a recommended multi-organ imaging/surveillance protocol (echocardiography, brain/renal imaging for calcification, EEG, vascular imaging for dissection risk).

---

*Report generated from a 5-iteration autonomous investigation (15 confirmed findings, 36 papers reviewed). Evidence source types are indicated throughout: human clinical (case reports, exome cohort), model organism (mouse), in vitro (cardiomyocyte signaling), and computational (gnomAD constraint, GTEx expression).*


## Artifacts

- [OpenScientist final report](Congenital_Heart_Defects_And_Ectodermal_Dysplasia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Heart_Defects_And_Ectodermal_Dysplasia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 8 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:15590638` (3 mentions) - Dual phospholipase C/diacylglycerol requirement for protein kinase D1 activation in lymphocytes.
  - shared terms: kinase

Weighed against this report's own most characteristic terms: `prkd1`, `variant`, `patient`, `defect`, `heart`, `chded`, `dominant`, `kinase`, `gene`, `ectodermal`, `cardiac`, `heterozygous`, `gain-of-function`, `renal`, `novo`, `missense`, `syndrome`, `arg603his`, `calcification`, `phenotype`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 16 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0007394` (1 mention) - the report calls it "Telangiectasia** of childhood onset"; HP calls it **Prominent superficial blood vessels**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001156` (1 mention) - the report calls it "Brachydactyly / skeletal defects"; HP calls it **Brachydactyly**, and lists "Brachydactyly syndrome" among its other names
- `GO:0000122` (1 mention) - the report calls it "negative regulation of transcription"; GO calls it **negative regulation of transcription by RNA polymerase II**