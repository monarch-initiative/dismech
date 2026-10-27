---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T22:00:03.160877'
end_time: '2026-10-25T22:16:54.380889'
duration_seconds: 1011.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Premature Ovarian Failure 24
  mondo_id: MONDO:0970995
  category: Mendelian
  causal_genes: SYCP2L
  omim_id: OMIM:620840
  synonyms: POF24; SYCP2L-related primary ovarian insufficiency; SYCP2L-related premature
    ovarian insufficiency
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 5
  relevance_assessed: 16
  on_topic: 5
  validator_version: 0.4.0
term_validation:
  total_terms: 22
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 3
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0970995
    reported_labels:
    - MONDO
    ontology_label: premature ovarian failure 24
  - term_id: HP:0000820
    reported_labels:
    - menopausal/genitourinary
    ontology_label: Abnormality of the thyroid gland
  labels_variant: 5
  unresolvable_prefixes:
  - MGI
  - RGD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Premature_Ovarian_Failure_24-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Premature_Ovarian_Failure_24-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Premature Ovarian Failure 24
- **MONDO ID:** MONDO:0970995 (if available)
- **Causal gene(s):** SYCP2L
- **OMIM:** OMIM:620840
- **Synonyms:** POF24; SYCP2L-related primary ovarian insufficiency; SYCP2L-related premature ovarian insufficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Premature Ovarian Failure 24** covering all of the
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

# Premature Ovarian Failure 24 (POF24): A Comprehensive Disease Characterization

**Disease:** Premature Ovarian Failure 24 (POF24)
**Causal gene:** **SYCP2L** (synaptonemal complex protein 2-like)
**OMIM:** 620840 | **MONDO:** MONDO:0970995 | **Gene OMIM:** 616799 | **HGNC:** 21537
**Category:** Mendelian, autosomal recessive

---

## Summary

**Premature Ovarian Failure 24 (POF24) is a rare, autosomal-recessive form of primary/premature ovarian insufficiency (POI) caused by biallelic loss-of-function variants in the gene SYCP2L.** SYCP2L (synaptonemal complex protein 2-like) is an oocyte-specific paralogue of the synaptonemal-complex lateral-element protein SYCP2. Uniquely among synaptonemal complex proteins, SYCP2L functions after meiotic prophase is complete: it localizes to the centromeres of dictyate-arrested primordial oocytes — the finite, non-renewable pool of germ cells laid down perinatally — where it promotes their long-term survival. When SYCP2L function is lost, this primordial reserve depletes prematurely and the ovary fails before the age of 40, producing the hypergonadotropic (high-FSH) amenorrhea, low anti-Müllerian hormone (AMH), and infertility that define POI.

The gene–disease relationship was established by whole-exome sequencing of a POI cohort (He et al., 2021, [PMID: 32303603](https://pubmed.ncbi.nlm.nih.gov/32303603/)), which identified two homozygous pathogenic variants and demonstrated through in-vitro functional assays that the mutant proteins are mislocalized and loss-of-function. An independent Iranian cohort subsequently reported a novel homozygous nonsense variant in SYCP2L in a woman with amenorrhea, confirming the link (Bakhshalizadeh et al., 2024, [PMID: 38521400](https://pubmed.ncbi.nlm.nih.gov/38521400/)). The mechanistic foundation was laid earlier by a landmark mouse and human-genetics study showing that Sycp2l-null female mice undergo accelerated, age-progressive oocyte loss, and that a common SYCP2L intronic SNP (rs2153157) modulates age at natural menopause and ovarian reserve (Zhou et al., 2015, [PMID: 26362258](https://pubmed.ncbi.nlm.nih.gov/26362258/)). SYCP2L is thus a **dosage-sensitive regulator of ovarian lifespan**: common regulatory variants shift menopause timing by years, whereas complete biallelic loss causes frank POI.

POF24 has no disease-specific therapy. Management follows general POI care: estrogen-based hormone therapy continued at least until the natural age of menopause (~51 years) to mitigate the cardiovascular, skeletal, cognitive, and mortality consequences of early estrogen deprivation, and fertility management primarily through oocyte donation, since spontaneous conception is rare. The condition is ultra-rare at the individual-gene level — SYCP2L explains only a small fraction of the ~3.5% of women affected by POI overall — and much of its molecular, epidemiological, and therapeutic profile is inferred from the broader POI literature and the Sycp2l mouse model rather than from POF24 patients directly.

---

## Section 1. Disease Information

**Overview.** POF24 is a Mendelian form of premature/primary ovarian insufficiency (POI), a condition in which ovarian function ceases before age 40. Clinically it is defined by amenorrhea (or oligomenorrhea) together with biochemically elevated follicle-stimulating hormone (FSH) and estrogen deficiency, arising from premature exhaustion of the ovarian follicular reserve. POF24 denotes the subset of POI caused specifically by biallelic SYCP2L variants.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| Disease OMIM | 620840 (Premature ovarian failure 24) |
| MONDO | MONDO:0970995 |
| Causal gene | SYCP2L |
| Gene OMIM | 616799 |
| HGNC | 21537 |
| NCBI Gene | 221711 |
| Ensembl gene | ENSG00000153157 |
| UniProt | Q5T4T6 (SYC2L_HUMAN) |
| ICD-10 | E28.31 (Premature menopause) / E28.39 (Other primary ovarian failure) |
| ICD-11 | 5A80.1 (Primary ovarian failure) |
| MeSH | "Primary Ovarian Insufficiency" (D016649) |

**Synonyms:** POF24; SYCP2L-related primary ovarian insufficiency; SYCP2L-related premature ovarian insufficiency.

**Information source.** The disease-level entry is derived from aggregated resources (OMIM, ClinVar, MONDO) that themselves rest on a small number of individual-patient reports (He 2021; Bakhshalizadeh 2024). The underlying evidence is case-level whole-exome sequencing data, not population EHR aggregation.

---

## Section 2. Etiology

**Primary cause — genetic.** POF24 is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in SYCP2L**. There is no environmental, infectious, or toxic trigger required; the disease is monogenic and recessive (Finding F001). The two originally reported pathogenic alleles (NM_001040274) are c.150_151del (p.Ser52Profs*7, a frameshift) and c.999A>G (p.Ile333Met, a missense), both found in the homozygous state in POI patients (He 2021, [PMID: 32303603](https://pubmed.ncbi.nlm.nih.gov/32303603/)). A third, independent allele is a novel homozygous nonsense variant reported by Bakhshalizadeh 2024 ([PMID: 38521400](https://pubmed.ncbi.nlm.nih.gov/38521400/)).

**Genetic risk factors / modifiers.** Beyond the fully penetrant recessive alleles, **common SYCP2L variation acts as a quantitative modifier of ovarian reserve**. The intronic SNP rs2153157 is a genome-wide significant locus for age at natural menopause (He 2009, [PMID: 19448621](https://pubmed.ncbi.nlm.nih.gov/19448621/); replicated across ancestries in the PAGE study, Carty 2013, [PMID: 23508249](https://pubmed.ncbi.nlm.nih.gov/23508249/)) and associates with serum AMH and IVF response (Rosa 2023, [PMID: 37417852](https://pubmed.ncbi.nlm.nih.gov/37417852/); Laisk-Podar 2015, [PMID: 26099445](https://pubmed.ncbi.nlm.nih.gov/26099445/)). This positions SYCP2L dosage on a continuum from common-variant modulation of menopause timing to Mendelian POI (Finding F005).

**Environmental risk factors.** None are specific to POF24. General POI risk factors (iatrogenic ovarian damage from chemotherapy/radiotherapy/surgery, smoking, autoimmunity) are independent of the SYCP2L genotype but could in principle act additively on an already-reduced reserve. No gene–environment interaction has been demonstrated for SYCP2L.

**Protective factors.** No genetic or environmental protective factors specific to POF24 are documented. By extrapolation from the dosage model, alleles that increase SYCP2L transcript abundance (the more efficiently spliced rs2153157 allele) associate with *later* menopause and higher ovarian reserve — effectively "protective" at the population level, though not studied in carriers of pathogenic alleles.

---

## Section 3. Phenotypes

The phenotype is that of POI, manifesting in adolescence to early adulthood. Because only a handful of patients have been reported, frequencies are qualitative and drawn from the general POI picture.

| Phenotype | Type | HPO term | Characteristics |
|---|---|---|---|
| Primary or secondary amenorrhea | Clinical sign | HP:0000786 (Amenorrhea) / HP:0000132 | Adolescent/young-adult onset; the presenting feature |
| Elevated FSH (hypergonadotropic) | Lab abnormality | HP:0008232 (Elevated circulating FSH) | FSH typically >25 IU/L on two occasions |
| Low anti-Müllerian hormone | Lab abnormality | HP (reduced ovarian reserve-related) | Reflects depleted follicle pool |
| Decreased/absent ovarian follicles | Physical/imaging | HP:0008209 (Premature ovarian insufficiency) | Small ovaries, few/no antral follicles on ultrasound |
| Infertility | Clinical | HP:0000789 (Infertility) | Often the reason for presentation |
| Estrogen deficiency symptoms (hot flashes, vaginal dryness) | Symptoms | HP:0000820 (menopausal/genitourinary) | Vasomotor and genitourinary |

**Age of onset:** adult-onset / late-adolescent; by definition before age 40. **Severity:** moderate to severe (complete ovarian failure). **Progression:** progressive follicular depletion; once POI is established it is generally stable/irreversible, though ~5–10% of POI patients show intermittent spontaneous ovarian activity. **Quality-of-life impact:** substantial — infertility, vasomotor symptoms, genitourinary syndrome, mood disturbance, and long-term bone/cardiovascular/cognitive risk all impair daily functioning (Faubion 2015, [PMID: 25845383](https://pubmed.ncbi.nlm.nih.gov/25845383/)).

---

## Section 4. Genetic / Molecular Information

**Causal gene.** SYCP2L (HGNC:21537; gene OMIM 616799; Ensembl ENSG00000153157), located at chromosome **6p24.2** (GRCh38 chr6:10,886,831–10,979,320); canonical transcript ENST00000283141; reference transcript NM_001040274 (Finding F004).

**Protein.** SYCP2L (UniProt Q5T4T6) is an **812-amino-acid, oocyte-specific armadillo-repeat protein**, annotated as an "Oocyte-specific protein that localizes to centromeres at the dictyate stage and regulates the survival of primordial oocytes," with subcellular localization to the nucleus and chromosome/centromere. It is a paralogue of the synaptonemal-complex lateral-element protein SYCP2 and contains an SYCP2 armadillo-repeat-like region (Finding F006).

**Pathogenic variants reported.**

| Variant (NM_001040274) | Protein | Type | dbSNP | gnomAD v4 allele frequency |
|---|---|---|---|---|
| c.150_151del (reported); c.154_155del | p.Ser52Profs*7 | Frameshift (LoF) | rs1196215011 | Exome 2.7×10⁻⁶; genome 6.6×10⁻⁶ |
| c.999A>G | p.Ile333Met | Missense | rs189836527 | Exome 1.2×10⁻⁵; genome 3.3×10⁻⁵ |
| Novel nonsense (Bakhshalizadeh 2024) | truncation | Nonsense (LoF) | — | Ultra-rare |

**Variant classification.** ClinVar (queried Oct 2025) contains 171 SYCP2L variant records; variants are explicitly annotated to "Premature ovarian failure 24," including ≥2 classified **Likely pathogenic** plus multiple **Uncertain significance (VUS)** (Finding F009). Most variants remain VUS, reflecting the gene's recent discovery and limited case counts.

**Functional consequence.** **Loss of function.** In-vitro analysis of the two POI-associated variants showed that mutant SYCP2L proteins exhibited mislocalization and loss of function (He 2021, [PMID: 32303603](https://pubmed.ncbi.nlm.nih.gov/32303603/)). Centromere localization requires the C-terminal portion of the protein, which is truncated by nonsense/frameshift alleles: "Centromere localization of SYCP2L requires its C-terminal portion, which is missing in truncated variants resulting from low-frequency nonsense mutations identified in humans" (Zhou 2015, [PMID: 26362258](https://pubmed.ncbi.nlm.nih.gov/26362258/)) (Finding F006).

**Population genetics / constraint.** gnomAD constraint metrics indicate SYCP2L is **not strongly haploinsufficient**: pLI ≈ 0, LOEUF/oe_lof = 0.78 (90% CI 0.66–0.92), lof_z = 2.1, mis_z = 1.3. Heterozygous LoF is therefore tolerated — fully consistent with recessive inheritance. 234 predicted-LoF variants exist in gnomAD (max AF ~6×10⁻⁵), none homozygous at appreciable frequency (Finding F004).

**Modifier genes.** No specific modifier genes are established for POF24. TDRD3 has been studied alongside SYCP2L for effects on ovarian reserve (Rosa 2023, [PMID: 37417852](https://pubmed.ncbi.nlm.nih.gov/37417852/)), but not as a modifier of SYCP2L disease.

**Epigenetic information.** No disease-specific methylation/chromatin findings. Notably, SYCP2L appears among smoking-associated differentially methylated regions in prostate tumor tissue (Burton 2016, [PMID: 27142338](https://pubmed.ncbi.nlm.nih.gov/27142338/)) — relevant to gene regulation generally but not to POF24 pathogenesis.

**Chromosomal abnormalities.** POF24 is a single-gene disorder; large-scale structural abnormalities are not part of its definition.

---

## Section 5. Environmental Information

POF24 is a monogenic disorder with **no established environmental, lifestyle, or infectious contribution** to its primary cause. Environmental factors relevant to POI in general (cytotoxic chemotherapy, pelvic radiation, ovarian surgery, smoking) act independently of SYCP2L and would be classified as *iatrogenic* or acquired POI rather than POF24. No infectious agent is implicated.

---

## Section 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in SYCP2L** (frameshift, nonsense, or deleterious missense) **leads to** a truncated or mislocalized SYCP2L protein. *(Demonstrated — in-vitro functional assays, He 2021.)*
2. Loss/mislocalization of SYCP2L **results in** failure to target the centromeres of dictyate-stage (arrested primordial) oocytes, because centromere localization requires the C-terminal domain that truncating variants remove. *(Demonstrated — Zhou 2015.)*
3. Absence of functional SYCP2L at the oocyte centromere **leads to** impaired survival of primordial oocytes. *(Demonstrated in mouse; inferred in human.)*
4. Impaired oocyte survival **results in** accelerated, age-progressive depletion of the finite, non-renewable primordial-follicle reserve established perinatally. *(Demonstrated — Sycp2l-null mice show more rapid pool depletion.)*
5. Premature exhaustion of the follicular reserve **leads to** loss of ovarian estrogen and inhibin production and failure of folliculogenesis. *(Inferred from reserve depletion.)*
6. Loss of ovarian negative feedback (low estrogen/inhibin) **results in** compensatory hypothalamic-pituitary drive and **elevated FSH** (hypergonadotropic state). *(Established endocrine physiology.)*
7. Follicular depletion + hypoestrogenism **results in** amenorrhea, infertility, low AMH, and the clinical syndrome of **premature ovarian insufficiency (POF24)**. *(Clinical observation.)*

> **Branch point:** The same SYCP2L dosage axis branches by allele severity. *Complete biallelic LoF* → step 7 (frank POI, POF24). *Partial reduction* from common regulatory variants (rs2153157 altering U12 minor-intron splicing efficiency) → milder shift: earlier age at natural menopause and lower AMH, without frank disease (Finding F005).

### Detailed mechanism

**Molecular pathway / cellular process.** SYCP2L operates in the biology of **meiotic arrest and oocyte maintenance** rather than a classical signaling cascade. As a paralogue of the synaptonemal-complex lateral-element protein SYCP2, it is co-opted post-meiotically to the centromere of oocytes that are arrested at the dictyate (diplotene) stage of meiosis I — the state in which the entire primordial reserve waits, sometimes for decades, until ovulation. SYCP2L "localizes to centromeres of dictyate stage oocytes, which represent the limited pool of primordial oocytes that are formed perinatally and remain arrested till ovulation" (Zhou 2015, [PMID: 26362258](https://pubmed.ncbi.nlm.nih.gov/26362258/)). Its demonstrated biological function is to **regulate the survival of these primordial oocytes**: "the pool of primordial oocytes becomes more rapidly depleted in SYCP2L-deficient than in wild-type females, such that with aging, fewer oocytes undergo maturation in developing follicles" (Findings F002, F006).

**Protein dysfunction.** The defect is **loss of function via mislocalization**: pathogenic missense and truncating variants prevent SYCP2L from reaching the centromere, abolishing its protective role (He 2021). Truncations remove the C-terminal centromere-targeting region (Zhou 2015).

**Tissue damage mechanism.** The downstream "injury" is accelerated germ-cell (oocyte) attrition — effectively a failure of cell maintenance/survival leading to progressive loss of the oocyte pool over time, rather than fibrosis, ischemia, or inflammation.

**Immune / metabolic involvement.** None established; POF24 is not an autoimmune or metabolic form of POI.

**Upstream vs downstream.** *Upstream:* the SYCP2L mutation and protein mislocalization (molecular). *Midstream:* oocyte centromere dysfunction and primordial-oocyte death (cellular). *Downstream:* reserve depletion → hypoestrogenism/elevated FSH → amenorrhea/infertility (organ/endocrine/clinical).

**Suggested ontology terms.**
- **GO (biological process):** oocyte development / female meiotic nuclear division (GO:0007143), meiotic cell cycle (GO:0051321), germ cell development (GO:0007281), regulation of cell survival; synaptonemal complex assembly (GO:0007130, paralogue-family context).
- **GO (cellular component):** condensed chromosome, centromeric region (GO:0000779); nucleus (GO:0005634); synaptonemal complex (GO:0000795, paralogue context).
- **CL (cell type):** oocyte (CL:0000023), egg cell (CL:0000025); specifically the dictyate-arrested primordial-follicle oocyte.

---

## Section 7. Anatomical Structures Affected

- **Primary organ:** **Ovary** (UBERON:0000992). Within it, the **ovarian follicle** (UBERON:0001305) and specifically the **primordial follicle** are the targets.
- **Body system:** Female reproductive / endocrine system (UBERON:0000474, reproductive system).
- **Secondary / complication organs:** Through estrogen deficiency, **bone** (osteoporosis), **cardiovascular system** (early atherosclerosis), **brain** (cognition/mood), and **genitourinary tract** (genitourinary syndrome of menopause) are secondarily affected (Faubion 2015).
- **Cell type:** **Oocyte** (CL:0000023), specifically the dictyate-arrested primordial oocyte. Granulosa and somatic follicular cells are affected secondarily to oocyte loss.
- **Subcellular compartments:** **Nucleus** (GO:0005634) and **centromere / condensed chromosome centromeric region** (GO:0000779) — the precise sites of SYCP2L localization.
- **Localization / lateralization:** **Bilateral** ovarian involvement (both ovaries affected).

---

## Section 8. Temporal Development

- **Onset:** The underlying lesion is congenital (germline), but the ovarian reserve is initially established; the clinical phenotype is **adult/late-adolescent onset**, by definition before age 40. The process is **insidious and chronic** — progressive follicular attrition rather than an acute event.
- **Progression:** The reserve depletes progressively; once POI is clinically manifest it is generally stable and irreversible. The mouse model demonstrates the time-dependence directly: "Female mice lacking SYCP2L undergo a significantly higher progressive loss of oocytes with age compared with wild-type females and are less fertile" (Zhou 2015, [PMID: 26362258](https://pubmed.ncbi.nlm.nih.gov/26362258/)).
- **Disease course / duration:** Chronic, lifelong (ovarian failure is permanent).
- **Remission:** No true remission; however, ~5–10% of POI patients in general show intermittent spontaneous ovarian activity and rare spontaneous conception (Lee 2026, [PMID: 42712473](https://pubmed.ncbi.nlm.nih.gov/42712473/)).
- **Critical period / intervention window:** The window is before and around diagnosis — initiating hormone therapy early (ideally at diagnosis) and considering fertility preservation before the reserve is exhausted.

---

## Section 9. Inheritance and Population

**Inheritance pattern:** **Autosomal recessive** — biallelic LoF required; heterozygous LoF is tolerated (gnomAD constraint, Finding F004).

**Penetrance / expressivity:** Presumed high penetrance for biallelic LoF, but formal penetrance cannot be estimated from the few reported cases; expressivity (age of ovarian failure) is likely variable, consistent with the dosage model.

**Consanguinity / founder effects:** The reported cases are homozygous, and at least one cohort (Bakhshalizadeh 2024, Iranian) is ethnically homogeneous — consistent with a role for consanguinity in surfacing recessive alleles. No specific founder mutation or geographic clustering has been established.

**Carrier frequency:** Not formally estimated; individual pathogenic alleles are ultra-rare in gnomAD (AF ~10⁻⁵–10⁻⁶), so carrier frequency is very low.

**Epidemiology.** POF24 itself has no published prevalence — it is a rare single-gene subset of POI. The parent condition POI affects **1–3.7% of women**, with recent meta-analytic estimates of **~3.5%** ("Premature ovarian insufficiency (POI) is characterised by amenorrhea associated with elevated follicle stimulating hormone (FSH) under the age of 40 years and affects 1-3.7% women. Genetic factors explain 20-30% of POI cases" — Bakhshalizadeh 2024, [PMID: 38521400](https://pubmed.ncbi.nlm.nih.gov/38521400/); "New data indicate a higher prevalence of POI, 3.5%" — ESHRE 2025, [PMID: 39652037](https://pubmed.ncbi.nlm.nih.gov/39652037/)). SYCP2L accounts for only a small fraction of the genetic cases (Finding F003).

**Sex ratio:** The phenotype manifests in **females** only (ovarian failure). SYCP2L is oocyte-specific; males carrying biallelic variants are not reported to have a corresponding phenotype.

---

## Section 10. Diagnostics

**Clinical/laboratory diagnosis of POI (the clinical layer):**
- Serum **FSH** elevated, typically **>25 IU/L** on two occasions ≥4 weeks apart (ESHRE criterion).
- Low **estradiol**; low **anti-Müllerian hormone (AMH)** reflecting depleted reserve.
- **Amenorrhea/oligomenorrhea** for ≥4 months before age 40.
- **Pelvic ultrasound:** small ovaries, reduced/absent antral follicle count.
- LOINC examples: FSH (15067-2), Estradiol (14715-7), AMH (38476-8).

**Genetic diagnosis (establishes POF24 specifically):**
- **Whole-exome sequencing (WES)** is the method by which SYCP2L was discovered and remains the primary route to diagnosis; it is well suited to a genetically heterogeneous condition where any single gene explains few cases (He 2021; Bakhshalizadeh 2024: "WES revealed diverse genetic causes, including a novel homozygous nonsense variant in SYCP2L, impacting synaptonemal complex (SC) assembly").
- **Multigene POI panels** including SYCP2L, or **single-gene sequencing** once suspected.
- **WGS** adds value for non-coding/splice and structural variants.
- **Karyotype** and **FMR1 premutation testing** are standard in POI workup to exclude Turner syndrome and Fragile-X-associated POI — important differentials.

**Differential diagnosis:** Turner syndrome (45,X and mosaics), FMR1 premutation-associated POI, autoimmune oophoritis, iatrogenic POI (chemo/radiation/surgery), galactosemia-associated POI, and other monogenic POI genes.

**Omics-based diagnostics:** Not routinely used; research only.

**Screening:** No population newborn or carrier screening exists. Cascade genetic testing of relatives after a proband is identified, and genetic counseling, are appropriate.

---

## Section 11. Outcome / Prognosis

**Reproductive prognosis:** Poor. Fertility is severely compromised; in a 324-woman POI cohort the overall spontaneous pregnancy rate was **8.6%**, and of those who had children after diagnosis **53.9% used oocyte donation** (Cambray 2023, [PMID: 36763040](https://pubmed.ncbi.nlm.nih.gov/36763040/)). Spontaneous resumption of ovarian function occurs in ~**5–10%** of POI generally (Lee 2026, [PMID: 42712473](https://pubmed.ncbi.nlm.nih.gov/42712473/)).

**Survival/morbidity:** POI is not directly life-shortening, but untreated early estrogen deprivation carries significant long-term morbidity: "The long-term consequences of premature or early menopause include adverse effects on cognition, mood, cardiovascular, bone, and sexual health, as well as an increased risk of early mortality" (Faubion 2015, [PMID: 25845383](https://pubmed.ncbi.nlm.nih.gov/25845383/)) (Finding F008). Complications include osteoporosis/fracture, cardiovascular disease, cognitive and mood effects, genitourinary syndrome, and reduced quality of life.

**Prognostic modifiers:** Hormone therapy mitigates (though not entirely) the bone, cardiovascular, and mortality risks. Earlier diagnosis and treatment improve outcomes.

---

## Section 12. Treatment

There is **no disease-specific or curative therapy** for POF24; management follows evidence-based POI care (ESHRE 2025, [PMID: 39652037](https://pubmed.ncbi.nlm.nih.gov/39652037/) — 145 recommendations).

**Hormone therapy (HT/MHT) — cornerstone.** Estrogen replacement (with a progestogen if the uterus is intact) to restore physiological estrogen levels. "Multiple medical societies recommend providing hormone therapy at least until the natural age of menopause" (Faubion 2015, [PMID: 25845383](https://pubmed.ncbi.nlm.nih.gov/25845383/)) (Finding F008). Transdermal estradiol is often preferred for its favorable thrombotic profile. NCIT: Hormone Replacement Therapy (C62604); Estrogen Therapy.

**Fertility management.** **Oocyte/embryo donation** is the mainstay and the most effective route to pregnancy (Cambray 2023). Early **fertility preservation** (oocyte cryopreservation) may be considered if diagnosed before reserve exhaustion, though usually the reserve is already depleted at presentation.

**Supportive care.** Bone protection (calcium, vitamin D, DXA monitoring), cardiovascular risk management, management of genitourinary and vasomotor symptoms, and psychological support.

**Pharmacogenomics / targeted / gene / cell therapy:** None established or applicable; no SYCP2L-directed therapy exists.

---

## Section 13. Prevention

- **Primary prevention:** Not possible for a germline recessive disorder. **Genetic counseling** and reproductive planning (carrier testing of partners in consanguineous families, preimplantation genetic testing, prenatal/cascade testing) can prevent recurrence in at-risk families.
- **Secondary prevention:** Early recognition of POI symptoms and prompt FSH/AMH testing enables early HT initiation.
- **Tertiary prevention:** Hormone therapy and lifestyle measures to prevent osteoporosis, cardiovascular disease, and other complications of hypoestrogenism.
- **Immunization/public health/prophylaxis:** Not applicable (non-infectious, non-environmental Mendelian disease).

---

## Section 14. Other Species / Natural Disease

- **Orthologous genes:** Mouse *Sycp2l* (NCBI Gene 637277; MGI:2685114; Ensembl ENSMUSG00000038651); rat *Sycp2l* (NCBI Gene 364688; RGD:1564922) (Finding F007). SYCP2L is conserved across vertebrates; a Xenopus orthologue (the karyoskeletal/nucleolar protein historically called NO145) was characterized in oocytes ([PMID: 11739789](https://pubmed.ncbi.nlm.nih.gov/11739789/); [PMID: 17374641](https://pubmed.ncbi.nlm.nih.gov/17374641/)).
- **Natural disease in animals:** No naturally occurring SYCP2L-related ovarian-failure disease is documented in companion animals or wildlife (no OMIA entry identified). SYCP2L appears as a candidate gene for reproductive/egg-production traits in livestock (goat, duck) studies ([PMID: 36757519](https://pubmed.ncbi.nlm.nih.gov/36757519/); [PMID: 35768515](https://pubmed.ncbi.nlm.nih.gov/35768515/)), underscoring conserved reproductive relevance but not a disease model.
- **Comparative biology:** The mouse recapitulates the core mechanism (accelerated oocyte loss), making SYCP2L function evolutionarily conserved for ovarian-reserve maintenance.
- **Zoonotic potential:** None (non-infectious).

---

## Section 15. Model Organisms

- **Principal model:** The **constitutive Sycp2l-knockout mouse** (Zhou et al., 2015, [PMID: 26362258](https://pubmed.ncbi.nlm.nih.gov/26362258/)) (Finding F007). *Mus musculus* (NCBI Taxon 10090).
- **Phenotype recapitulation:** Strong for the core disease mechanism — null females show "a significantly higher progressive loss of oocytes with age compared with wild-type females and are less fertile," plus more rapid depletion of the primordial oocyte pool and reduced fertility, recapitulating accelerated reproductive aging / ovarian-reserve failure.
- **Model limitations:** Mice are subfertile with accelerated aging rather than showing the complete, early, frank ovarian failure of human biallelic LoF; species differences in reproductive lifespan limit direct translation of timing. The model captures the *reserve-depletion* mechanism but not the full human clinical syndrome (endocrine thresholds, symptom burden).
- **Applications:** Studying primordial-oocyte survival, centromere function in arrested oocytes, and genetic/dosage control of ovarian lifespan.
- **Other systems:** No established zebrafish, Drosophila, C. elegans, or organoid/iPSC model specific to POF24; in-vitro cell assays were used to demonstrate variant mislocalization (He 2021).

---

## Mechanistic Model / Interpretation

```
   SYCP2L biallelic LoF variant (frameshift / nonsense / deleterious missense)
                        │  (DEMONSTRATED: in-vitro functional assay, He 2021)
                        ▼
   Truncated / mislocalized SYCP2L protein  ──► fails C-terminal centromere targeting
                        │  (DEMONSTRATED: Zhou 2015)
                        ▼
   Loss of SYCP2L at centromeres of dictyate-arrested PRIMORDIAL OOCYTES
                        │  (mouse-demonstrated; human-inferred)
                        ▼
   Impaired survival → accelerated, age-progressive OOCYTE LOSS
                        │
                        ▼
   Premature depletion of the finite, non-renewable PRIMORDIAL-FOLLICLE RESERVE
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
  ↓ estrogen / inhibin         failed folliculogenesis
          │                           │
          ▼                           ▼
  loss of negative feedback     amenorrhea, low AMH, infertility
          │
          ▼
  ↑ FSH (hypergonadotropic)  ───►  CLINICAL POF24 (POI before age 40)
          │
          ▼
  Long-term hypoestrogenism complications: bone, CV, cognition, mortality
```

**DOSAGE AXIS (the unifying theme):**

| SYCP2L dosage | Mechanism | Phenotype |
|---|---|---|
| Normal (two functional alleles) | Full centromere protection of oocytes | Normal menopause (~51 y) |
| Common variant rs2153157 (reduced splicing efficiency) | ↓ steady-state transcript | Earlier menopause, lower AMH, altered IVF response |
| Biallelic LoF | Protein absent/mislocalized | POF24 — frank POI before 40 |

The central insight of this investigation is that **SYCP2L is a dosage-sensitive determinant of ovarian lifespan.** The same gene whose common regulatory variation nudges menopause timing by months-to-years at the population level causes frank, early ovarian failure when both copies are abolished. This continuity — from GWAS locus (He 2009; Carty 2013) to quantitative AMH/IVF effects (Rosa 2023; Laisk-Podar 2015) to Mendelian disease (He 2021; Bakhshalizadeh 2024) — is unusually complete for a POI gene and strongly corroborates the causal model.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [32303603](https://pubmed.ncbi.nlm.nih.gov/32303603/) | Homozygous SYCP2L variants in POI | Human clinical + in-vitro | **Establishes gene–disease link**; two homozygous variants; mislocalization/LoF |
| [38521400](https://pubmed.ncbi.nlm.nih.gov/38521400/) | Diverse genetic causes of amenorrhea (Iranian cohort) | Human clinical | **Independent confirmation**; novel homozygous nonsense variant; POI definition/prevalence |
| [26362258](https://pubmed.ncbi.nlm.nih.gov/26362258/) | Accelerated reproductive aging in Sycp2l-null mice | Mouse + human genetics | **Core mechanism**; centromere localization, oocyte survival, splicing SNP |
| [19448621](https://pubmed.ncbi.nlm.nih.gov/19448621/) | GWAS of menarche/menopause | Human genetics | SYCP2L (6p24.2) as age-at-menopause locus |
| [23508249](https://pubmed.ncbi.nlm.nih.gov/23508249/) | PAGE replication study | Human genetics | rs2153157 replicates across ancestries |
| [37417852](https://pubmed.ncbi.nlm.nih.gov/37417852/) | SYCP2L/TDRD3 and ovarian reserve | Human clinical | AA genotype → lower AMH (p=0.01) |
| [26099445](https://pubmed.ncbi.nlm.nih.gov/26099445/) | Reproductive-ageing variants in IVF | Human clinical | rs2153157 → rFSH/oocyte and pregnancy chances |
| [39652037](https://pubmed.ncbi.nlm.nih.gov/39652037/) | ESHRE POI guideline 2025 | Guideline | POI prevalence ~3.5%; management framework |
| [25845383](https://pubmed.ncbi.nlm.nih.gov/25845383/) | Long-term consequences of early menopause | Review | Complications + HT-until-natural-menopause recommendation |
| [36763040](https://pubmed.ncbi.nlm.nih.gov/36763040/) | Family building after POI (n=324) | Human cohort | Spontaneous pregnancy 8.6%; oocyte donation 53.9% |
| [42712473](https://pubmed.ncbi.nlm.nih.gov/42712473/) | Spontaneous conception in POI (case) | Case report | 5–10% spontaneous ovarian recovery |

Most citation snippets in the knowledge state were verified against stored abstracts. Two snippets attributed to PMID 32303603 ("mutant SYCP2L proteins exhibited mislocalisation and loss of function"; "SYCP2L is a novel gene found to be responsible for human POI") were flagged as not exactly matching the stored abstract text; the substantive claims they support are nonetheless consistent with the paper's verified findings and with the independent mouse data, and their exact wording should be re-confirmed against the full text.

---

## Limitations and Knowledge Gaps

1. **Very few patients.** POF24 rests on a handful of reported individuals/families. Penetrance, expressivity, and genotype–phenotype correlations cannot be quantified reliably.
2. **No disease-level epidemiology.** Prevalence/incidence specific to SYCP2L-POI is unknown; all epidemiology is extrapolated from POI broadly.
3. **Human mechanism partly inferred.** The oocyte-centromere survival mechanism is demonstrated in mouse and in-vitro assays; direct human histological/functional confirmation is lacking.
4. **Variant interpretation.** Most SYCP2L ClinVar variants remain VUS; functional assays exist for only a few alleles.
5. **Citation caveat.** Two in-vitro/novel-gene quotations attributed to He 2021 did not exactly match stored abstract text (flagged "mismatch"); conclusions are corroborated by independent evidence but exact wording should be re-verified.
6. **No non-mouse models, no therapeutics pipeline, and no autoimmune/metabolic involvement data** specific to this gene.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the patient series** via GeneMatcher/POI consortia to accumulate additional biallelic SYCP2L families, enabling penetrance and genotype–phenotype analysis.
2. **Functional validation of VUS**: systematic centromere-localization/oocyte-survival assays (and AlphaFold-guided structural modeling of the armadillo-repeat/C-terminal domain) to reclassify the many SYCP2L VUS.
3. **Humanized/knock-in mouse models** carrying patient-specific alleles (e.g., p.Ile333Met) to test whether missense alleles phenocopy nulls and to time reserve depletion.
4. **Define the molecular partners** of SYCP2L at the dictyate-oocyte centromere (proteomics/IP-MS) to clarify how it promotes oocyte survival.
5. **Quantify carrier frequency and any founder effect** in consanguineous populations (e.g., Iranian cohorts) using targeted population screening.
6. **Correlate SYCP2L dosage with AMH trajectories** longitudinally to test the dosage model prospectively and assess rs2153157 as a clinical ovarian-reserve biomarker.
7. **Re-verify flagged citations** against full-text He 2021 to ensure exact-quote integrity for the knowledge base.

---

*Report compiled from 5 investigation iterations, 9 confirmed findings, and 34 reviewed papers. Evidence source types: human clinical (case series, cohorts), model organism (Sycp2l-null mouse), in-vitro (variant functional assays), and computational (gnomAD constraint, ontology mapping).*


## Artifacts

- [OpenScientist final report](Premature_Ovarian_Failure_24-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Premature_Ovarian_Failure_24-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 10 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0970995` (2 mentions) - the report calls it "MONDO"; MONDO calls it **premature ovarian failure 24**
- `HP:0000820` (1 mention) - the report calls it "menopausal/genitourinary"; HP calls it **Abnormality of the thyroid gland**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0008232` (1 mention) - the report calls it "Elevated circulating FSH"; HP calls it **Elevated circulating follicle stimulating hormone level**, and lists "Elevated follicle stimulating hormone" among its other names
- `GO:0000779` (2 mentions) - the report calls it "centromere / condensed chromosome centromeric region"; GO calls it **condensed chromosome, centromeric region**
- `GO:0005634` (2 mentions) - the report calls it "Nucleus", "Subcellular compartments:** **Nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `CL:0000023` (2 mentions) - the report calls it "Oocyte", "Cell type:** **Oocyte"; CL calls it **oocyte**
- `UBERON:0000992` (1 mention) - the report calls it "Ovary", "Primary organ:** **Ovary"; UBERON calls it **ovary**, and lists "animal ovary" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005634` - called "Nucleus", "Subcellular compartments:** **Nucleus"
- `CL:0000023` - called "Oocyte", "Cell type:** **Oocyte"
- `UBERON:0000992` - called "Ovary", "Primary organ:** **Ovary"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`, `RGD`.