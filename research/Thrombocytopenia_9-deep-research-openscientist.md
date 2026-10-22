---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T16:27:29.772014'
end_time: '2026-10-22T16:59:35.392279'
duration_seconds: 1925.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Thrombocytopenia 9
  mondo_id: MONDO:0957572
  category: Mendelian
  causal_genes: THPO
  omim_id: not recorded
  synonyms: THC9
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
citation_count: 20
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 15
  relevance_assessed: 20
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 24
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 7
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0957572
    reported_labels:
    - MONDO
    ontology_label: thrombocytopenia 9
  - term_id: HP:0001873
    reported_labels:
    - Laboratory abnormality
    ontology_label: Thrombocytopenia
  - term_id: HP:0001903
    reported_labels:
    - Laboratory abnormality
    ontology_label: Anemia
  - term_id: UBERON:0002107
    reported_labels:
    - liver, site of TPO synthesis
    ontology_label: liver
  - term_id: CHEBI:51354
    reported_labels:
    - eltrombopag
    ontology_label: benzylpenicillin(1-)
  - term_id: NCIT:C66919
    reported_labels:
    - Romiplostim
    ontology_label: Photoimmunotherapy
  - term_id: NCIT:C62408
    reported_labels:
    - Eltrombopag
    ontology_label: Perinephric
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Thrombocytopenia_9-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Thrombocytopenia_9-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Thrombocytopenia 9
- **MONDO ID:** MONDO:0957572 (if available)
- **Causal gene(s):** THPO
- **OMIM:** not recorded
- **Synonyms:** THC9
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Thrombocytopenia 9** covering all of the
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

# Thrombocytopenia 9 (THC9): A Comprehensive Disease Characterization Report

**Disease:** Thrombocytopenia 9 (THC9)
**MONDO ID:** MONDO:0957572
**Causal gene:** **THPO** (thrombopoietin; HGNC:11795; NCBI Gene 7066; UniProt P40225; chromosome 3q27.1)
**Synonym:** THC9
**Category:** Mendelian, autosomal recessive

---

## Summary

**Thrombocytopenia 9 (THC9) is an ultra-rare inherited thrombocytopenia caused by biallelic loss-of-function variants in *THPO*, the gene encoding thrombopoietin (TPO).** TPO is the master cytokine of platelet production: secreted constitutively by the liver, it binds its receptor MPL (c-Mpl) on megakaryocytes and hematopoietic stem cells (HSCs), triggering JAK2 activation and the downstream STAT5, PI3K–AKT, and MAPK/ERK signaling cascades that drive megakaryopoiesis and maintain the HSC pool. When TPO ligand activity is deficient, megakaryocyte and platelet production fails, producing a hypoproductive (central) thrombocytopenia. Critically, because the lesion lies in the ligand and **not** in the MPL receptor, THC9 is mechanistically distinct from receptor-defect disorders and is predicted to respond to receptor-level pharmacology.

The founding description of the disease (Dasouki et al., 2013, [PMID: 24085763](https://pubmed.ncbi.nlm.nih.gov/24085763/)) identified a homozygous *THPO* missense variant, c.112C>T (p.Arg38Cys, also written R17C when the 21-amino-acid signal peptide is excluded), in the receptor-binding domain, in two siblings from a consanguineous Micronesian family with autosomal recessive aplastic anemia. The variant is a **partial** loss-of-function allele, and the family displayed a striking gene-dosage phenotypic gradient: homozygotes developed trilineage marrow failure (aplastic anemia), heterozygous carriers had mild thrombocytopenia, and a wild-type sibling had normal platelet counts. This dosage sensitivity places THC9 on a continuum from mild isolated thrombocytopenia to full marrow aplasia.

THC9 is best understood in contrast to its molecular mirror image. Whereas biallelic coding loss-of-function *THPO* variants reduce TPO activity and cause THC9/aplastic anemia, dominant gain-of-function mutations in the *THPO* 5′-untranslated region (5′UTR) increase TPO translation and instead cause hereditary (familial) essential thrombocythemia (THCYT1, OMIM 187950). The *THPO* gene therefore functions as a bidirectional rheostat that sets total body platelet mass. Because the MPL receptor remains intact in THC9, TPO-receptor agonists (romiplostim, eltrombopag) are a mechanistically rational therapy, with allogeneic hematopoietic stem cell transplantation (HSCT), and experimentally gene therapy, addressing the marrow-failure end of the spectrum.

---

## 1. Disease Information

THC9 is a Mendelian, autosomal-recessive inherited thrombocytopenia / bone marrow failure disorder caused by deficiency of thrombopoietin (TPO), the principal physiological regulator of platelet production. The clinical presentation ranges from isolated thrombocytopenia to aplastic anemia depending on allele dosage and residual TPO activity.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0957572 |
| Gene | *THPO* (HGNC:11795; NCBI Gene 7066) |
| OMIM (disease) | Not separately recorded in template; *THPO* gene = OMIM 600044 |
| Synonym | THC9 |
| Contrast disorder | THCYT1 / hereditary essential thrombocythemia, OMIM 187950 (5′UTR gain-of-function) |

**Synonyms / alternative names:** Thrombocytopenia 9; THC9; (in the index family presented as) autosomal recessive aplastic anemia due to thrombopoietin deficiency.

**Information source:** The disease-level characterization is derived primarily from a small number of **individual patient reports** (notably a single consanguineous Micronesian family, Dasouki 2013) supplemented by **aggregated disease-level resources** (OMIM, MONDO) and extensive **model-organism and mechanistic literature** on the TPO–MPL axis. The evidence base for THC9 as a distinct human entity is narrow (essentially one index family), so much of the phenotype and treatment rationale is extrapolated from TPO/MPL biology and from the related receptor disorder congenital amegakaryocytic thrombocytopenia (CAMT, MPL-related).

---

## 2. Etiology

**Primary cause — genetic:** Biallelic (homozygous or compound heterozygous) loss-of-function variants in *THPO*. In the index family the variant was homozygous c.112C>T (p.Arg38Cys / R17C), a missense change in the TPO receptor-binding domain. In vitro, the mutant TPO retained only a 2–3-fold reduced capacity to sustain TPO-dependent UT7-TPO cells, consistent with a **partial** loss-of-function allele rather than a null.

> "Whole-exome sequencing identified a novel homozygous missense mutation in thrombopoietin (THPO, c.112C>T) in both affected siblings." — [PMID: 24085763](https://pubmed.ncbi.nlm.nih.gov/24085763/)

> "the R17C partial loss-of-function allele results in aplastic anemia in the homozygous state and mild thrombocytopenia in the heterozygous state in our family" — [PMID: 24085763](https://pubmed.ncbi.nlm.nih.gov/24085763/)

**Genetic risk factors:** The causal variant itself is the risk factor; consanguinity is a strong contributor given the autosomal-recessive inheritance (the index family was consanguineous and Micronesian). Heterozygous carriers have a subclinical/mild thrombocytopenia risk (gene-dosage effect).

**Environmental risk factors:** None established. THC9 is a monogenic disorder; no toxins, lifestyle, or occupational exposures are known to cause or trigger it.

**Protective factors:** None specifically documented. By mechanistic inference, any residual TPO activity (as with the partial-LoF R17C allele retaining ~30–50% function) is protective against the most severe marrow-failure phenotype; a single wild-type *THPO* allele is sufficient for near-normal (mildly reduced) platelet counts.

**Gene–environment interactions:** No specific GxE interactions are documented for THC9. The monogenic, highly penetrant nature of the biallelic genotype leaves little room for environmental modification, though this is untested.

---

## 3. Phenotypes

The core phenotype is **hypoproductive (central) thrombocytopenia** with a dosage-dependent spectrum extending to pancytopenia/aplastic anemia in biallelic cases.

| Phenotype | Type | HPO term | Onset / severity / frequency |
|---|---|---|---|
| Thrombocytopenia | Laboratory abnormality | HP:0001873 | Carriers: mild; biallelic: severe. Core feature (~100% of affected) |
| Aplastic anemia / pancytopenia | Lab + clinical | HP:0001915 (aplastic anemia); HP:0001876 (pancytopenia) | Biallelic homozygotes; childhood-onset in index family |
| Anemia | Laboratory abnormality | HP:0001903 | Part of biallelic marrow failure |
| Leukopenia / neutropenia | Laboratory abnormality | HP:0001882 / HP:0001875 | Part of biallelic marrow failure |
| Abnormal bleeding / bruising | Clinical sign | HP:0001892 (abnormal bleeding) | Proportional to platelet count; mild in carriers |
| Reduced megakaryocytes | Histopathology | HP:0005528 (bone marrow hypocellularity) | Hypoproductive marrow |

**Phenotype characteristics:**
- **Age of onset:** Childhood in biallelic homozygotes (aplastic anemia in the index siblings); carriers show lifelong mild thrombocytopenia.
- **Severity:** Variable and dosage-dependent — mild (heterozygotes) to severe (biallelic marrow failure).
- **Progression:** The biallelic form is progressive toward marrow failure, consistent with the role of TPO/MPL in HSC maintenance (progressive HSC loss, as seen with MPL-inactivating mutations). Carrier thrombocytopenia appears stable.
- **Frequency among affected individuals:** Thrombocytopenia is universal; the extension to trilineage aplasia depends on genotype and residual TPO activity.

**Quality-of-life impact:** Dominated by bleeding risk (in severe thrombocytopenia) and, in the biallelic marrow-failure form, by anemia-related fatigue, infection risk from neutropenia, and the burden of transfusion dependence or HSCT. Formal EQ-5D/SF-36 data specific to THC9 are **not available** given the rarity.

---

## 4. Genetic / Molecular Information

**Causal gene:** *THPO* (thrombopoietin), chromosome 3q27.1, HGNC:11795, NCBI Gene 7066, gene OMIM 600044. The protein TPO (UniProt P40225) comprises a 21-amino-acid signal peptide, an N-terminal receptor-binding (EPO-like) domain, and a heavily glycosylated C-terminal domain that stabilizes the circulating protein.

**Pathogenic variants:**
- **Founding variant:** c.112C>T, p.Arg38Cys (p.Arg17Cys / R17C using mature-protein numbering that excludes the signal peptide). Located in the receptor-binding domain.
- **Variant classification:** Pathogenic/likely pathogenic in the recessive, biallelic context, supported by functional data (2–3-fold reduced ability to sustain TPO-dependent cells) and co-segregation with a gene-dosage phenotype.
- **Variant type:** Missense (partial loss-of-function). Other predicted loss-of-function classes (nonsense, frameshift, splice) would be expected to cause THC9 if biallelic, but the human evidence base is currently limited to the R17C missense allele.
- **Allele frequency:** The index variant is novel/private (consanguineous family); THC9 alleles are vanishingly rare in gnomAD.
- **Somatic vs germline:** Germline.
- **Functional consequence:** Loss of function (reduced receptor-binding/signaling capacity of the TPO ligand). This is distinct from, and directionally opposite to, the gain-of-function 5′UTR mutations that cause hereditary thrombocythemia.

**THPO directional genotype–phenotype dichotomy:**

> "we identified a one-base deletion in the 5'-untranslated region of the TPO gene in affected but not in nonaffected family members. In vitro experiments showed that the identified mutation increased TPO production." — [PMID: 9694695](https://pubmed.ncbi.nlm.nih.gov/9694695/)

> "The presence of AUG codons located upstream of the physiological start site can inhibit translation by causing premature initiation and thereby preventing the ribosome from reaching the physiological start codon, as in the case of thrombopoietin (TPO)." — [PMID: 10828006](https://pubmed.ncbi.nlm.nih.gov/10828006/)

| *THPO* variant class | Location | Effect on TPO | Phenotype | Inheritance |
|---|---|---|---|---|
| Missense / predicted LoF | Coding / receptor-binding domain | ↓ TPO activity | **THC9** (thrombocytopenia → aplastic anemia) | Autosomal recessive |
| 5′UTR deletion / uAUG disruption | 5′UTR | ↑ TPO translation/production | Hereditary essential thrombocythemia (THCYT1) | Autosomal dominant |

**Modifier genes:** Not specifically defined for THC9. Mechanistically, variants in *MPL*, *JAK2*, and downstream signaling genes would be expected to modify TPO responsiveness, but no modifiers are established.

**Epigenetic information:** *THPO* expression is partly controlled at the translational level by the 5′UTR uORF/stem-loop architecture rather than by classical DNA methylation/histone changes relevant to THC9. No disease-specific epigenetic signature is reported.

**Chromosomal abnormalities:** None characteristic; THC9 is a single-gene disorder, not a copy-number/structural syndrome.

---

## 5. Environmental Information

- **Environmental factors:** None causal. THC9 is monogenic.
- **Lifestyle factors:** None established.
- **Infectious agents:** Not applicable — THC9 is not infectious. (Note: TPO levels rise non-specifically in sepsis/inflammation, [PMID: 35665097](https://pubmed.ncbi.nlm.nih.gov/35665097/), which is relevant to diagnostic interpretation but not to THC9 causation.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A biallelic loss-of-function variant in *THPO* (e.g., c.112C>T / R17C in the receptor-binding domain) **results in** thrombopoietin protein with reduced receptor-binding/signaling capacity.
2. Reduced functional TPO **leads to** diminished engagement of the MPL (c-Mpl) receptor on megakaryocytes and hematopoietic stem cells.
3. Deficient MPL engagement **results in** reduced JAK2 activation and receptor tyrosine phosphorylation.
4. Reduced JAK2 signaling **leads to** attenuated downstream STAT5, PI3K–AKT, and MAPK/ERK cascade activity.
5. Attenuated signaling **results in** (branch A) impaired megakaryocyte proliferation, differentiation, and maturation → reduced platelet production → **thrombocytopenia**; and (branch B) impaired HSC maintenance/quiescence → progressive HSC attrition → **trilineage marrow failure / aplastic anemia** in biallelic cases.
6. Reduced anti-apoptotic (AKT–Bcl-xL) signaling in megakaryocytes/platelets **contributes to** decreased platelet survival, compounding the thrombocytopenia (inferred from TPO-RA apoptosis studies).
7. Thrombocytopenia **leads to** the clinical bleeding phenotype (bruising, mucocutaneous bleeding), proportional to platelet count.

Steps 1–5 are well supported by human genetics plus model-organism and in vitro data; the branch to full marrow failure (step 5B) is supported by MPL-null biology and the index family's aplastic anemia phenotype. The anti-apoptotic contribution (step 6) is inferred from TPO-RA pharmacodynamics rather than demonstrated directly in THC9 patients.

### Supporting detail

**Molecular pathways:** The TPO→MPL→JAK2 axis activating STAT5, PI3K-AKT, and MAPK/ERK (KEGG hsa04630 JAK-STAT signaling; Reactome signaling by MPL).

> "Tpo binding to Mpl triggers activation of Janus kinase 2 (Jak2) and phosphorylation of the receptor, as well as activation of several intracellular signalling cascades that mediate cellular responses" — [PMID: 38491305](https://pubmed.ncbi.nlm.nih.gov/38491305/)

**Cellular processes:** Megakaryocyte proliferation/differentiation/maturation (GO:0030219 megakaryocyte differentiation; GO:0030220 platelet formation), HSC maintenance and quiescence (GO:0061484 hematopoietic stem cell homeostasis), and anti-apoptotic regulation.

> "mutation of which resulted in thrombocytopenia, deficient megakaryopoiesis, low hematopoietic stem cell (HSC) number and function" — [PMID: 38491305](https://pubmed.ncbi.nlm.nih.gov/38491305/)

> "Patients with inactivating mutations in Mpl develop thrombocytopenia and aplastic anemia because of progressive loss of HSCs" — [PMID: 21289307](https://pubmed.ncbi.nlm.nih.gov/21289307/)

**Protein dysfunction:** Loss of function of the secreted TPO ligand — reduced affinity/efficacy at the receptor-binding interface (R17C) rather than misfolding or aggregation.

**Anti-apoptotic / survival signaling:** TPO-R signaling exerts anti-apoptotic effects on platelets and megakaryocytes via AKT-regulated Bcl-xL/Bax/Bak balance; loss of this input reduces platelet survival.

**Immune system involvement:** THC9 is a production defect, **not** an autoimmune or immune-destructive thrombocytopenia — an important distinction from immune thrombocytopenia (ITP). Neutropenia in the biallelic marrow-failure form predisposes to infection as a downstream complication.

**GO / CL / UBERON / CHEBI term suggestions:** GO:0038162 (thrombopoietin-mediated signaling pathway), GO:0030219 (megakaryocyte differentiation), GO:0030220 (platelet formation); CL:0000556 (megakaryocyte), CL:0000037 (hematopoietic stem cell), CL:0000233 (platelet); UBERON:0002371 (bone marrow), UBERON:0002107 (liver, site of TPO synthesis); CHEBI:51354 (eltrombopag).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Bone marrow (UBERON:0002371) — the site of defective megakaryopoiesis and HSC attrition. Liver (UBERON:0002107) is the primary site of TPO synthesis and is therefore the source organ of the deficient signal (though the liver itself is structurally normal).
- **Secondary / complications:** Any tissue susceptible to hemorrhage from thrombocytopenia (skin/mucosa; CNS in severe cases). In biallelic marrow failure, generalized effects of anemia and neutropenia.
- **Body system:** Hematopoietic/hematologic system (and, by extension, hemostatic system).

**Tissue and cell level:**
- Hematopoietic tissue; specifically the megakaryocyte lineage (CL:0000556), hematopoietic stem cells (CL:0000037), and the end-product platelets (CL:0000233). All three hematopoietic lineages are affected in the biallelic marrow-failure state.

**Subcellular level:**
- Plasma membrane receptor signaling platform (MPL receptor; GO:0005886 plasma membrane); cytoplasmic JAK-STAT signaling; the secretory pathway for TPO in hepatocytes.

**Localization / lateralization:** Systemic/bilateral — a diffuse hematopoietic process, not a localized or lateralized lesion.

---

## 8. Temporal Development

- **Onset:** Childhood in biallelic homozygotes (the index siblings presented with aplastic anemia in childhood); carriers exhibit lifelong, usually incidentally detected, mild thrombocytopenia. Onset is **insidious/chronic** rather than acute.
- **Progression:** The biallelic form is **progressive** toward marrow failure, mirroring the progressive HSC loss documented for MPL-inactivating mutations. Carrier thrombocytopenia is **stable**.
- **Disease course:** Chronic, lifelong. Without definitive treatment (HSCT) the biallelic marrow-failure form carries the morbidity/mortality of aplastic anemia.
- **Remission patterns:** No spontaneous remission; treatment-induced improvement is possible with TPO-RA (ligand bypass) or cure with HSCT.
- **Critical periods:** Early recognition before irreversible HSC depletion is the key window for intervention, by analogy to the reversibility demonstrated when MPL expression is restored in murine models.

---

## 9. Inheritance and Population

**Epidemiology:** Ultra-rare; prevalence and incidence are not formally established (essentially a single reported family plus mechanistic extrapolation). No reliable per-100,000 figures exist.

**Inheritance:** **Autosomal recessive** for the full disease (biallelic). A clear **gene-dosage effect** is observed, such that heterozygous carriers manifest mild thrombocytopenia — a semi-dominant feature at the level of platelet count.

- **Penetrance:** Biallelic genotype appears highly penetrant for thrombocytopenia; carrier phenotype is mild and may be subclinical.
- **Expressivity:** Variable — from mild isolated thrombocytopenia to aplastic anemia depending on residual TPO activity.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects / consanguinity:** The index family was consanguineous and of Micronesian ancestry; consanguinity is the principal route to the biallelic state. No broad founder haplotype is established.
- **Carrier frequency:** Unknown; expected to be very low.

**Population demographics:** Reported in a Micronesian family; no established ethnic predilection beyond the role of consanguinity. No sex bias is expected for an autosomal-recessive hematopoietic gene. Age distribution skews to childhood presentation for the severe form.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Complete blood count:** Thrombocytopenia (isolated in mild cases; with anemia ± neutropenia/pancytopenia in biallelic marrow failure).
- **Bone marrow examination:** Reduced/hypoproductive megakaryocytes; hypocellular marrow in the aplastic form.
- **Serum/plasma TPO level — a key discriminating test.** In most hypoproductive marrow-failure thrombocytopenias, TPO is **elevated** because of reduced receptor-mediated clearance when platelet/megakaryocyte mass is low. In THC9, the defect is the **ligand itself**, so TPO should be **low/absent or inappropriately normal** — an inverted pattern relative to classic aplastic anemia or CAMT. (The inverted expectation in THC9 is a mechanistic inference.)

> "plasma TPO levels markedly elevated in patients with AA or ChemoT" — [PMID: 11345828](https://pubmed.ncbi.nlm.nih.gov/11345828/)

> "TPO is produced in the liver at a constant rate and cleared by TPO receptors on platelets. TPO levels are inversely proportional to the rate of platelet production." — [PMID: 23821332](https://pubmed.ncbi.nlm.nih.gov/23821332/)

> "these new criteria enable us to clearly differentiate ITP from aplastic anemia and other forms of hypoplastic thrombocytopenia" — [PMID: 37957517](https://pubmed.ncbi.nlm.nih.gov/37957517/)

**Genetic testing (definitive):**
- **Single-gene *THPO* testing**, inherited-thrombocytopenia / bone-marrow-failure **gene panels**, **whole-exome sequencing** (the modality by which THC9 was originally discovered), and **whole-genome sequencing** are all appropriate. WES/WGS are especially valuable given the broad differential of inherited thrombocytopenias (>50 genes).
- CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing are **not relevant** to this single-nucleotide-variant, single-gene disorder.

**Clinical criteria / differential diagnosis:** Distinguish from:
- **CAMT (MPL-related)** — receptor defect; elevated TPO.
- **Immune thrombocytopenia (ITP)** — destruction, normal/slightly ↑ TPO, elevated immature platelet fraction, normal marrow.
- Other inherited thrombocytopenias (e.g., *GFI1B*-related [PMID: 41766040](https://pubmed.ncbi.nlm.nih.gov/41766040/), *NFE2*-related [PMID: 42152485](https://pubmed.ncbi.nlm.nih.gov/42152485/)) — distinguished by marrow morphology, associated features (α-granule deficiency, dysmegakaryopoiesis), and genetics.
- Acquired marrow failure (aplastic anemia, MDS [PMID: 26500138](https://pubmed.ncbi.nlm.nih.gov/26500138/)).

**Screening:** Cascade genetic testing of at-risk relatives in known families; carrier detection shows mild thrombocytopenia.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No THC9-specific survival statistics exist. Prognosis tracks with severity: isolated mild thrombocytopenia carries a good prognosis, whereas the biallelic aplastic-anemia form carries the substantial morbidity/mortality of marrow failure (bleeding, infection) unless treated with HSCT.
- **Morbidity:** Bleeding risk (thrombocytopenia), anemia-related fatigue, and infection risk (neutropenia) in the severe form; transfusion dependence.
- **Complications:** Hemorrhage; in marrow failure, infections and transfusion-related complications; potential clonal evolution risk inherent to inherited marrow-failure syndromes (not specifically quantified for THC9).
- **Recovery potential:** The HSC-maintenance defect may be reversible if the TPO/MPL signal is restored early, by analogy to murine models in which restoring Mpl expression replenished the HSC pool and corrected platelet production.
- **Prognostic factors:** Residual TPO activity (allele severity), genotype (biallelic vs carrier), age at presentation, and degree of marrow involvement.

---

## 12. Treatment

**Central therapeutic logic:** THC9 is a **ligand deficiency with an intact MPL receptor**, making receptor-level pharmacology mechanistically rational.

**Pharmacotherapy / TPO-receptor agonists (TPO-RA):**
- **Romiplostim** (NCIT:C66919) — a peptibody carrying four TPO-mimetic peptides that directly activate MPL.
- **Eltrombopag** (NCIT:C62408) — an oral small-molecule MPL agonist acting via a distinct (transmembrane) mechanism.

> "A second generation of TPO receptor agonists, romiplostim and eltrombopag, has been developed." — [PMID: 23821332](https://pubmed.ncbi.nlm.nih.gov/23821332/)

> "TPO is produced in the liver at a constant rate and cleared by TPO receptors on platelets. TPO levels are inversely proportional to the rate of platelet production." — [PMID: 23821332](https://pubmed.ncbi.nlm.nih.gov/23821332/)

TPO-RAs are already applied to rare inherited thrombocytopenias and to aplastic anemia, supporting their use in TPO-ligand deficiency ([PMID: 38925157](https://pubmed.ncbi.nlm.nih.gov/38925157/)). Pharmacodynamically, platelet counts rise after a ~5-day delay and peak at ~12–14 days; part of the benefit is anti-apoptotic (AKT–Bcl-xL) support of megakaryocytes/platelets ([PMID: 25132654](https://pubmed.ncbi.nlm.nih.gov/25132654/)). A caveat for THC9 is that a ligand-replacement strategy and a receptor-agonist strategy are not identical: in disorders where the block is *downstream* of the receptor (e.g., NFE2-related maturation defect), TPO-RAs fail ([PMID: 42152485](https://pubmed.ncbi.nlm.nih.gov/42152485/)) — reinforcing that TPO-RA rationality in THC9 depends specifically on the receptor and its signaling being intact.

**Advanced/curative therapeutics:**
- **Allogeneic HSCT** (NCIT:C15431) — curative for the marrow-failure end of the spectrum (as established for MPL-related CAMT).
- **Gene therapy (proof of concept):** Lentiviral re-expression of Mpl in Mpl-deficient mice replenished the HSC pool and corrected platelet production, with demonstrated reversibility of HSC loss.

> "restoration of Mpl expression from transcriptionally targeted vectors prevents lethal adverse reactions of ectopic Mpl expression, replenishes the HSC pool, restores stem cell properties, and corrects platelet production" — [PMID: 21289307](https://pubmed.ncbi.nlm.nih.gov/21289307/)

For THC9 specifically, the defect is the *ligand*, so either receptor agonism (bypassing the missing ligand) or, conceptually, *THPO* gene/protein replacement would be rational; the Mpl-restoration data establish the reversibility principle for the axis.

**Supportive care:** Platelet transfusion for acute bleeding; red-cell transfusion and infection prophylaxis in marrow failure.

**Treatment outcomes / adverse events:** The principal TPO-RA safety concerns are **thrombosis** and rare, usually reversible, marrow **reticulin fibrosis**.

> "Thrombotic complications are also an area of concern and need further close follow-up." — [PMID: 22872157](https://pubmed.ncbi.nlm.nih.gov/22872157/)

Real-world ITP data show thrombosis typically occurs in patients with additional thrombotic risk factors ([PMID: 27793553](https://pubmed.ncbi.nlm.nih.gov/27793553/)).

**Personalized medicine:** Genotype-guided — confirming a *THPO* ligand defect (vs an *MPL* receptor defect or a downstream transcription-factor defect) supports TPO-RA use, because receptor agonists cannot rescue a non-functional receptor or a downstream maturation block but can bypass a missing ligand.

---

## 13. Prevention

- **Primary prevention:** Not applicable to a monogenic disorder beyond **genetic counseling** and reproductive planning. In consanguineous families, carrier screening and counseling reduce the recurrence risk of the biallelic state.
- **Secondary prevention:** Early genetic diagnosis (cascade testing of relatives) and monitoring of platelet counts to pre-empt bleeding complications; early recognition before irreversible HSC depletion.
- **Tertiary prevention:** Prevent bleeding (platelet support), infection (in neutropenia), and manage marrow failure (HSCT) to prevent complications.
- **Immunization / public health / environmental / prophylaxis:** Not applicable as causal measures; standard infection prophylaxis applies in marrow-failure patients.
- **Counseling:** Autosomal-recessive recurrence risk (25% for carrier×carrier); carriers should be informed of mild thrombocytopenia and reproductive implications.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *THPO* is conserved across mammals and in zebrafish. Mouse *Thpo* (NCBI Gene 21832) and its receptor *Mpl* are the principal experimental orthologs; zebrafish possess a thrombopoietin receptor (zTpoR) with partly divergent signaling.
- **Natural disease in other species:** No well-characterized spontaneous *THPO*-deficiency disease is cataloged in companion animals (OMIA did not surface a defined natural analog); the knowledge base is dominated by engineered models.
- **Comparative biology:** The TPO–MPL–JAK2 axis is evolutionarily conserved as the dominant thrombopoietic regulator, validating cross-species modeling. Zebrafish thrombopoiesis additionally engages an unconventional zTpoR–Mapk14a (p38) interaction not seen in human TpoR ([PMID: 40089183](https://pubmed.ncbi.nlm.nih.gov/40089183/)), a caveat for cross-species extrapolation.
- **Transmission / zoonosis:** Not applicable (genetic disease).

---

## 15. Model Organisms

**Mouse (primary model):**
- ***Thpo*-knockout and *Mpl*-knockout mice** recapitulate the core phenotype: profound thrombocytopenia while retaining ~10% of normal platelet counts of fully functional platelets, which prevents abnormal bleeding — demonstrating TPO as the dominant but not sole regulator of platelet production.

> "Even though these mice are profoundly thrombocytopenic they maintain a basal level of approximately 10% of the normal count of fully functional platelets." — [PMID: 11012175](https://pubmed.ncbi.nlm.nih.gov/11012175/)

- IL-3Rα/Mpl double knockouts show no further platelet reduction, indicating the residual TPO-independent thrombopoiesis is not IL-3-driven ([PMID: 11012175](https://pubmed.ncbi.nlm.nih.gov/11012175/)).
- *Mpl*-knockout mice also develop **aplastic anemia from progressive HSC loss**, which is **reversible** upon Mpl re-expression — modeling the marrow-failure extension of THC9 and establishing gene-therapy proof of concept ([PMID: 21289307](https://pubmed.ncbi.nlm.nih.gov/21289307/)).
- Mpl cytoplasmic-tyrosine knock-in mutants (e.g., Y599/Y582) dissect which signaling outputs drive megakaryopoiesis vs HSC maintenance ([PMID: 38491305](https://pubmed.ncbi.nlm.nih.gov/38491305/), [PMID: 32417303](https://pubmed.ncbi.nlm.nih.gov/32417303/)).

**Phenotype recapitulation:** High — murine TPO/MPL loss reproduces hypoproductive thrombocytopenia and the HSC/aplastic-anemia phenotype. **Limitations:** residual ~10% platelet production differs from the variable human severity; murine MPL responds less efficiently to human-designed TPO-RA (romiplostim), complicating preclinical drug testing ([PMID: 32417303](https://pubmed.ncbi.nlm.nih.gov/32417303/)).

**Other systems:** Zebrafish thrombopoiesis (with the divergent zTpoR–Mapk14a axis) and in vitro TPO-dependent cell lines (UT7-TPO, used to quantify the R17C functional deficit; 32D cells for signaling). iPSC/organoid megakaryopoiesis systems are applicable but not yet reported specifically for THC9.

**Resources:** MGI (mouse *Thpo*/*Mpl*), ZFIN (zebrafish), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

```
   THPO biallelic LoF (e.g., c.112C>T / R17C, receptor-binding domain)
                     │  results in
                     ▼
     Thrombopoietin with reduced receptor-binding/signaling activity
                     │  leads to
                     ▼
        Deficient engagement of MPL (c-Mpl) on MKs and HSCs
                     │  results in
                     ▼
        ↓ JAK2 activation / receptor phosphorylation
                     │  leads to
                     ▼
      ↓ STAT5 · ↓ PI3K–AKT · ↓ MAPK/ERK signaling
              │                               │
   (branch A) │ impaired megakaryopoiesis     │ (branch B) impaired HSC
              ▼                               ▼  maintenance/quiescence
   ↓ platelet production +            progressive HSC attrition
   ↓ AKT–Bcl-xL platelet survival              │
              │                                ▼
              ▼                     trilineage marrow failure /
        THROMBOCYTOPENIA  ───────▶  APLASTIC ANEMIA (biallelic, dosage-dependent)
              │
              ▼
     bleeding / bruising (proportional to platelet count)

   MIRROR IMAGE:  THPO 5'UTR GAIN-of-function → ↑TPO translation
                  → thrombocythemia (THCYT1, dominant)
```

The unifying concept is that **THPO gene dosage sets whole-body platelet mass as a bidirectional rheostat.** Coding loss-of-function turns the rheostat down (THC9: thrombocytopenia → aplastic anemia, recessive), while 5′UTR gain-of-function turns it up (hereditary thrombocythemia, dominant). Within THC9, a continuous dose–response from residual TPO activity (allele severity) to clinical severity explains why heterozygous carriers are mildly thrombocytopenic and biallelic homozygotes develop marrow failure. The intactness of the MPL receptor is the single most therapeutically consequential feature, because it means the downstream machinery is fully competent and only the input signal is missing — exactly the situation that receptor agonists (romiplostim, eltrombopag) and ligand/gene replacement are designed to correct.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [24085763](https://pubmed.ncbi.nlm.nih.gov/24085763/) | *Exome sequencing reveals a thrombopoietin ligand mutation in a Micronesian family with AR aplastic anemia* | **Founding evidence** — identifies THPO c.112C>T (R17C), partial LoF, dosage-dependent spectrum |
| [38491305](https://pubmed.ncbi.nlm.nih.gov/38491305/) | *Differential in vivo roles of Mpl cytoplasmic tyrosines* | Defines TPO→MPL→JAK2 cascade; links to thrombocytopenia & HSC defects |
| [21289307](https://pubmed.ncbi.nlm.nih.gov/21289307/) | *Lentiviral gene transfer regenerates HSCs in Mpl-deficient aplastic anemia* | HSC-loss mechanism; reversibility / gene-therapy proof of concept |
| [11012175](https://pubmed.ncbi.nlm.nih.gov/11012175/) | *IL-3 does not contribute to platelet production in c-Mpl-deficient mice* | Knockout phenotype: ~10% residual platelets; TPO as dominant regulator |
| [23821332](https://pubmed.ncbi.nlm.nih.gov/23821332/) | *The biology of thrombopoietin and TPO-RA* | TPO physiology/clearance; introduces romiplostim & eltrombopag |
| [11345828](https://pubmed.ncbi.nlm.nih.gov/11345828/) | *Diagnostic value of TPO levels...* | Marrow-failure thrombocytopenias show ↑TPO (contrast to THC9 ↓TPO) |
| [37957517](https://pubmed.ncbi.nlm.nih.gov/37957517/) | *Reference guide for ITP diagnosis, 2023* | TPO/IPF to differentiate hypoplastic thrombocytopenias |
| [9694695](https://pubmed.ncbi.nlm.nih.gov/9694695/) | *Familial ET with 5'UTR THPO deletion* | Opposite GoF mechanism (thrombocythemia) |
| [10828006](https://pubmed.ncbi.nlm.nih.gov/10828006/) | *Translational pathophysiology* | uAUG/5'UTR translational control of TPO |
| [38925157](https://pubmed.ncbi.nlm.nih.gov/38925157/) | *TPO-RA in pediatrics* | TPO-RA use in rare inherited thrombocytopenias/SAA |
| [22872157](https://pubmed.ncbi.nlm.nih.gov/22872157/) | *Thrombopoietin-receptor agonists* | Thrombosis as key TPO-RA adverse event |
| [32417303](https://pubmed.ncbi.nlm.nih.gov/32417303/) | *Signaling of murine MPL after TPO/romiplostim* | Preclinical caveat: murine MPL less responsive to romiplostim |
| [25132654](https://pubmed.ncbi.nlm.nih.gov/25132654/) | *TPO-RA effect on platelet apoptosis* | Anti-apoptotic AKT–Bcl-xL contribution |

**Supporting / contextual (differential and adjacent biology):** [PMID: 41766040](https://pubmed.ncbi.nlm.nih.gov/41766040/) (GFI1B-related IT), [PMID: 42152485](https://pubmed.ncbi.nlm.nih.gov/42152485/) (NFE2-related, TPO-RA-refractory — highlights a downstream defect distinct from THC9), [PMID: 26500138](https://pubmed.ncbi.nlm.nih.gov/26500138/) (MDS thrombocytopenia), [PMID: 18496561](https://pubmed.ncbi.nlm.nih.gov/18496561/) (familial ET / JAK2), [PMID: 40089183](https://pubmed.ncbi.nlm.nih.gov/40089183/) (zebrafish zTpoR–Mapk14a), [PMID: 35665097](https://pubmed.ncbi.nlm.nih.gov/35665097/) (TPO in sepsis — diagnostic confounder).

---

## Limitations and Knowledge Gaps

1. **Narrow human evidence base.** The human characterization of THC9 rests essentially on a **single consanguineous family** with one missense allele (R17C). The full mutational spectrum (nonsense/frameshift/splice nulls), the range of phenotypes, penetrance, and natural history are therefore not well defined.
2. **Epidemiology unknown.** No prevalence/incidence estimates, no defined carrier frequency, no established ethnic distribution beyond the consanguinity route.
3. **Serum TPO in THC9 is an inference.** The expectation of low/inappropriately-normal TPO (vs the elevated TPO of other marrow-failure states) follows from the ligand-loss mechanism but has not been robustly measured in a THC9 cohort — and a receptor-binding-domain missense variant could still produce detectable (but non-functional) protein, complicating immunoassay interpretation.
4. **Treatment data are extrapolated.** No THC9-specific clinical trials of TPO-RA, HSCT, or gene therapy exist; efficacy is inferred from TPO/MPL biology and from related disorders (CAMT, SAA, ITP). TPO-RA response in a ligand defect with a missense (partial) mutation is plausible but unproven in patients.
5. **Model-organism caveats.** Murine MPL responds less efficiently to the human-designed agonist romiplostim ([PMID: 32417303](https://pubmed.ncbi.nlm.nih.gov/32417303/)), and zebrafish signaling diverges ([PMID: 40089183](https://pubmed.ncbi.nlm.nih.gov/40089183/)), limiting direct preclinical translation of drug responses.
6. **Genotype–phenotype quantitation.** The relationship between residual TPO activity and clinical severity is qualitatively clear (dosage effect) but not quantitatively mapped.

---

## Proposed Follow-up Experiments / Actions

1. **Case ascertainment & registry.** Use GeneMatcher/Matchmaker Exchange and inherited-thrombocytopenia panels to find additional biallelic *THPO* families; build a small natural-history registry to define penetrance, severity distribution, and progression to marrow failure.
2. **Measure serum/plasma TPO in confirmed THC9 patients** (ideally with both immunoassay and a bioassay) to test the predicted low/non-functional-ligand pattern and establish TPO level as a discriminating diagnostic (vs elevated TPO in CAMT/aplastic anemia).
3. **Functional characterization of new alleles.** Express candidate *THPO* variants in UT7-TPO / 32D systems and in iPSC-derived megakaryopoiesis to quantify residual activity and correlate with phenotype.
4. **Therapeutic proof-of-concept.** Trial a TPO-RA (eltrombopag/romiplostim) in a confirmed THC9 patient with monitoring of platelet response, marrow reticulin, and thrombosis risk; compare the response of a ligand defect with the receptor-defect (CAMT) and downstream-defect (NFE2/GFI1B) comparators, which help define where TPO-RA will and will not work.
5. **Ligand/gene replacement modeling.** Test recombinant TPO or *THPO* gene replacement in a *Thpo*-null mouse and in patient iPSC-megakaryocyte systems to establish whether supplying ligand (rather than agonizing the receptor) better restores HSC maintenance.
6. **Diagnostic algorithm integration.** Incorporate "low/normal TPO + central thrombocytopenia + *THPO* biallelic variant" into inherited-thrombocytopenia diagnostic guidelines to distinguish THC9 from ITP, CAMT, and acquired marrow failure.

---

*Evidence source types: human clinical genetics (index family, PMID 24085763); model organism (mouse Thpo/Mpl knockouts and gene-therapy models; zebrafish); in vitro (UT7-TPO/32D functional and signaling assays); and mechanistic/clinical pharmacology reviews. Where claims rest on inference from TPO/MPL biology rather than direct THC9 observation, this is stated explicitly.*


## Artifacts

- [OpenScientist final report](Thrombocytopenia_9-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Thrombocytopenia_9-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 20 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957572` (2 mentions) - the report calls it "MONDO"; MONDO calls it **thrombocytopenia 9**
- `HP:0001873` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Thrombocytopenia**
- `HP:0001903` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Anemia**
- `UBERON:0002107` (2 mentions) - the report calls it "liver, site of TPO synthesis"; UBERON calls it **liver**
- `CHEBI:51354` (1 mention) - the report calls it "eltrombopag"; CHEBI calls it **benzylpenicillin(1-)**
- `NCIT:C66919` (1 mention) - the report calls it "Romiplostim"; NCIT calls it **Photoimmunotherapy**
- `NCIT:C62408` (1 mention) - the report calls it "Eltrombopag"; NCIT calls it **Perinephric**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0038162` (1 mention) - the report calls it "thrombopoietin-mediated signaling pathway"; GO calls it **erythropoietin-mediated signaling pathway**
- `UBERON:0002371` (2 mentions) - the report calls it "bone marrow", "Primary:** Bone marrow"; UBERON calls it **bone marrow**
- `NCIT:C15431` (1 mention) - the report calls it "Allogeneic HSCT"; NCIT calls it **Hematopoietic Cell Transplantation**, and lists "HSCT" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002371` - called "bone marrow", "Primary:** Bone marrow"