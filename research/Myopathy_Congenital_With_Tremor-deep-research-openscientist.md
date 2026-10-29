---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-28T17:20:51.197501'
end_time: '2026-10-28T17:59:03.931467'
duration_seconds: 2292.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Myopathy, Congenital, with Tremor
  mondo_id: MONDO:0032797
  category: Mendelian
  causal_genes: not recorded
  omim_id: not recorded
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
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 8
  on_topic: 8
  validator_version: 0.4.0
term_validation:
  total_terms: 31
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 24
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0032797
    reported_labels:
    - MONDO
    ontology_label: myopathy, congenital, with tremor
  - term_id: GO:0030017
    reported_labels:
    - sarcomere, cellular component
    - sarcomere
    - Subcellular level:** The **sarcomere
    ontology_label: sarcomere
  - term_id: UBERON:0003672
    reported_labels:
    - axial skeletal muscle
    ontology_label: dentition
  labels_variant: 2
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
  path: Myopathy_Congenital_With_Tremor-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Myopathy_Congenital_With_Tremor-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myopathy, Congenital, with Tremor
- **MONDO ID:** MONDO:0032797 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Myopathy, Congenital, with Tremor** covering all of the
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

# Myopathy, Congenital, with Tremor (CMYO16 / "Myotrem") — Comprehensive Disease Report

**Target disease:** Myopathy, Congenital, with Tremor
**MONDO ID:** MONDO:0032797 · **OMIM:** #618524 · **MedGen:** C5231401 (UID 1684886)
**Causal gene:** **MYBPC1** (slow skeletal myosin-binding protein C; sMyBP-C) — HGNC:7549; NCBI Gene 4604; UniProt Q00872; chromosome 12q23.2

---

## Summary

**Myopathy, Congenital, with Tremor (MONDO:0032797) is Congenital Myopathy-16 (CMYO16), also called "Myotrem" or myogenic-tremor myopathy (OMIM #618524). Its causal gene is *MYBPC1*, which encodes slow skeletal muscle myosin-binding protein C (sMyBP-C).** This is an autosomal dominant skeletal-muscle disorder characterized by onset in infancy of hypotonia and a distinctive high-frequency (~10–11 Hz) tremor of the limbs, together with mild proximal and axial muscle weakness. The clinical course is comparatively benign: weakness tends to stabilize or improve after adolescence, and the condition is managed supportively.

An important note for knowledge-base curation: the disease name "Myopathy, Congenital, with Tremor" is easily confused with a separate, single de novo case of a tremor-associated myopathy caused by *MYH7* (β-cardiac/slow skeletal myosin heavy chain) reported in 2023. During this investigation an early draft mis-assigned the gene to *MYH7*; that was corrected. **The MYH7 tremor case is explicitly described by its own authors as a "first-of-its-kind" report distinct from the classical MYBPC1 entity.** Following the MONDO/OMIM identifiers given in the research template, the disease in scope here is unambiguously the *MYBPC1* disease, CMYO16. *MYH7* findings are retained in this report only as clearly-labeled comparative/contextual material.

Mechanistically, all reported pathogenic variants are heterozygous missense changes clustered in the N-terminal **M-motif** of sMyBP-C (e.g., p.Tyr247His, p.Glu248Lys, p.Leu259Pro, p.Leu263Arg). These variants dysregulate the binding of sMyBP-C's N-terminus to myosin and perturb actomyosin cross-bridge cycling and stretch activation in slow (type-1) muscle fibers. The resulting aberrant, pulsatile myofilament activity is the proposed sarcomeric origin of the "myogenic tremor." The disease is ultra-rare (~16 patients from ~8 families reported by mid-2024), has a favorable natural history, and is modeled by an E248K knock-in mouse that recapitulates the myopathy.

---

## 1. Disease Information

**Overview.** CMYO16 is an autosomal dominant congenital myopathy defined by the combination of infantile hypotonia, mild and comparatively non-progressive skeletal muscle weakness (proximal and axial predominant), and a hallmark high-frequency postural/action tremor of myogenic (sarcomeric) origin. OMIM/MedGen summarize it as: *"Congenital myopathy-16 (CMYO16) is an autosomal dominant muscle disorder characterized by onset of hypotonia and tremor in infancy… proximal muscle weakness, and a high-frequency tremor of the limbs… course tends to stabilize after adolescence (summary by Stavusis et al., 2019)."*

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0032797 |
| OMIM (phenotype) | #618524 (CMYO16) |
| OMIM (gene) | *160794* (MYBPC1) |
| MedGen | C5231401 / UID 1684886 |
| HGNC | 7549 (MYBPC1) |
| NCBI Gene | 4604 |
| UniProt | Q00872 (MYPC1_HUMAN) |
| Orphanet | No dedicated code identified; falls under "congenital myopathy" grouping |
| ICD-11 | 8C70 (Congenital myopathies) — closest mapping |
| ICD-10 | G71.2 (Congenital myopathies) — closest mapping |

**Synonyms / alternative names:** Congenital Myopathy-16 (CMYO16); "Myotrem"; Myogenic tremor myopathy; Myopathy, congenital, with tremor.

**Information source type:** Aggregated disease-level resources (OMIM, MedGen, HPO) combined with a small number of primary case series (individual-patient clinical/genetic data from ~8 families). There is no large EHR/registry dataset for this ultra-rare disorder.

---

## 2. Etiology

**Primary cause — genetic.** CMYO16 is a monogenic Mendelian disorder caused by heterozygous (autosomal dominant) missense variants in *MYBPC1*. There is no known environmental, infectious, or toxic cause. The disease arises either from inheritance within multigeneration families or from de novo variants.

**Genetic risk factors.** The causal variants themselves are the risk determinant. They cluster in the NH2-terminal **M-motif** of sMyBP-C:
- **p.Tyr247His (Y247H)** and **p.Glu248Lys (E248K)** — segregating in two three-generation families (Stavusis et al., 2019; [PMID: 31025394](https://pubmed.ncbi.nlm.nih.gov/31025394/)).
- **p.Leu263Arg (L263R)** — de novo in 3 individuals; **p.Leu259Pro (L259P)** — de novo in 1 individual (Shashi et al., 2019; [PMID: 31264822](https://pubmed.ncbi.nlm.nih.gov/31264822/)).

These variants are absent from population controls, affect residues conserved across vertebrates, and are predicted damaging (ACMG pathogenic/likely pathogenic; recurrent de novo events support pathogenicity).

**Environmental risk factors / protective factors / gene–environment interactions:** None identified. No modifier alleles, protective variants, dietary, lifestyle, occupational, or infectious factors have been reported. Given the Mendelian, highly penetrant nature of the condition, environmental contributions are not expected to be major.

---

## 3. Phenotypes

The phenotype spectrum and official HPO frequencies are drawn from the 7-patient cohort annotated to OMIM:618524 (Stavusis et al., 2019; [PMID: 31025394](https://pubmed.ncbi.nlm.nih.gov/31025394/)).

| Phenotype | HPO term | Frequency | Type |
|---|---|---|---|
| Flexion contracture | HP:0001371 | 7/7 (100%) | Physical manifestation |
| Postural tremor | HP:0002174 | 6/7 (86%) | Clinical sign |
| Axial muscle weakness | HP:0003327 | 6/7 (86%) | Clinical sign |
| Scoliosis | HP:0002650 | 5/7 (71%) | Physical manifestation |
| Tongue tremor | HP:0031947 | 3/7 (43%) | Clinical sign |
| Scapular winging | HP:0003691 | 3/7 | Clinical sign |
| Spinal rigidity | HP:0003306 | 3/7 | Clinical sign |
| Lumbar hyperlordosis | HP:0002938 | 3/7 | Physical manifestation |
| High palate | HP:0000218 | 3/7 | Physical manifestation |
| Proximal muscle weakness | HP:0003701 | present | Clinical sign |
| Distal muscle weakness | HP:0002460 | present | Clinical sign |
| Myopathic EMG abnormalities | HP:0003458 | 2/2 | Laboratory abnormality |
| Micrognathia | HP:0000347 | minor | Physical manifestation |
| Narrow mouth | HP:0000160 | minor | Physical manifestation |
| Prominent nasolabial fold | HP:0005272 | minor | Physical manifestation |
| Autosomal dominant inheritance | HP:0000006 | — | Inheritance |

Additional recognized features reported in later series include neonatal respiratory distress with **laryngeal stridor** and **undulating/undulatory tongue movements** (Neurol Clin Pract 2024, [PMID: 38690148](https://pubmed.ncbi.nlm.nih.gov/38690148/); Pediatr Neurol 2023, [PMID: 37392669](https://pubmed.ncbi.nlm.nih.gov/37392669/)).

**Phenotype characteristics.**
- **Age of onset:** Infancy/congenital — hypotonia and tremor present from early infancy.
- **Severity:** Mild overall; tremor is the most conspicuous and functionally relevant feature.
- **Progression:** Weakness is mild and tends to stabilize or improve after adolescence (gradual clinical improvement). Tremor persists. Scoliosis and contractures may require orthopedic attention.
- **Frequency:** See table above (per-phenotype percentages from the core cohort).

**Quality-of-life impact:** The persistent high-frequency tremor can impair fine motor tasks and handwriting; scoliosis, flexion contractures and spinal rigidity may affect posture, mobility, and comfort. Formal QoL instrument data (EQ-5D, SF-36, PROMIS) are not available for this ultra-rare disease. Overall, because weakness is mild and tends to improve, long-term functional prognosis is relatively favorable.

---

## 4. Genetic / Molecular Information

**Causal gene.** *MYBPC1* (OMIM *160794; HGNC:7549; NCBI Gene 4604; UniProt Q00872), chromosome **12q23.2**, encoding **slow skeletal muscle myosin-binding protein C (sMyBP-C)**. sMyBP-C is a thick-filament accessory protein of the C-zone that regulates actomyosin interactions and contractile kinetics; it also functionally recruits muscle creatine kinase to the myosin filament (NCBI Gene 4604 summary).

**Pathogenic variants (CMYO16-causing subset).** All are heterozygous **missense** changes in the **N-terminal M-motif**:

| Variant (protein) | Domain | Families / individuals | Origin | Reference |
|---|---|---|---|---|
| p.Tyr247His (Y247H) | M-motif | one 3-generation family | inherited (AD) | Stavusis 2019 ([PMID: 31025394](https://pubmed.ncbi.nlm.nih.gov/31025394/)) |
| p.Glu248Lys (E248K) | M-motif | one 3-generation family | inherited (AD) | Stavusis 2019 ([PMID: 31025394](https://pubmed.ncbi.nlm.nih.gov/31025394/)) |
| p.Leu259Pro (L259P) | M-motif | 1 individual | de novo | Shashi 2019 ([PMID: 31264822](https://pubmed.ncbi.nlm.nih.gov/31264822/)) |
| p.Leu263Arg (L263R) | M-motif | 3 individuals | de novo | Shashi 2019 ([PMID: 31264822](https://pubmed.ncbi.nlm.nih.gov/31264822/)) |

**Variant classification:** Pathogenic / likely pathogenic by ACMG/AMP criteria (absent from controls, conserved residues, recurrent de novo, functional evidence).
**Variant type/class:** Missense (single-nucleotide substitutions).
**Allele frequency:** Absent or extremely rare in population databases (gnomAD); not present in healthy controls.
**Somatic vs germline:** Germline (inherited or de novo germline).
**Functional consequences:** Not simple loss of function. Biochemically, **Y247H and E248K markedly INCREASE N-terminal binding of sMyBP-C to myosin**, whereas **L263R DECREASES M-motif binding to myosin** — divergent biochemical effects that converge on dysregulated actomyosin cross-bridge cycling. This is best described as a dominant gain-of-dysfunction / dysregulatory mechanism rather than haploinsufficiency.

**Allelic disorders (same gene, different phenotype — important for ClinVar interpretation).** ClinVar lists ~52 pathogenic/likely-pathogenic *MYBPC1* records (of ~523 total), but only the small set of N-terminal M-motif missense variants cause CMYO16. Other *MYBPC1* variants cause:
- **Distal arthrogryposis type 1B (DA1B)** — OMIM 614335.
- **Lethal congenital contracture syndrome 4 (LCCS4)** — OMIM 614915 (recessive, lethal).

**Modifier genes / epigenetics / chromosomal abnormalities:** None reported. No DNA-methylation, histone, or large-scale chromosomal abnormality is implicated. Sex-dependent modification of progression is suggested by the mouse model (below) but no human modifier gene is defined.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious factors are implicated in CMYO16. It is a purely genetic Mendelian disorder. There are no reported toxic, occupational, dietary, or pathogen-related contributors. **(Not applicable.)**

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A heterozygous **missense variant in the N-terminal M-motif of *MYBPC1*** (e.g., Y247H, E248K, L259P, L263R) **results in** an altered sMyBP-C N-terminus.
2. The altered M-motif **changes the strength of sMyBP-C's binding to the myosin filament** — increased binding (Y247H/E248K) or decreased binding (L263R). *(Demonstrated biochemically; Stavusis 2019, Shashi 2019.)*
3. Altered sMyBP-C–myosin tethering **dysregulates actomyosin cross-bridge cycling and stretch activation** within the C-zone of slow (type-1) fibers. *(Inferred from biochemistry + myofilament physiology.)*
4. This **leads to** aberrant, pulsatile/oscillatory myofilament activity in slow-twitch fibers (aberrant stretch activation). *(Supported by ex-vivo myofilament studies; Int J Mol Sci 2025, [PMID: 40508067](https://pubmed.ncbi.nlm.nih.gov/40508067/).)*
5. Sarcomere-level oscillation **is picked up by muscle spindles** and **produces** a high-frequency (~10–11 Hz) postural/action tremor — the **"myogenic tremor"** — potentially amplified by a segmental spinal central loop. *(Proposed mechanism; sarcomere-origin model supported by electrophysiology in the comparative MYH7 case, [PMID: 37070061](https://pubmed.ncbi.nlm.nih.gov/37070061/).)*
6. In parallel (branch), chronic contractile dysfunction of slow fibers **results in** mild hypotonia, proximal/axial weakness, and secondary musculoskeletal features (flexion contractures, scoliosis, spinal rigidity).
7. In some neonates, involvement of laryngeal/pharyngeal musculature **leads to** stridor and respiratory distress and undulating tongue movements.

```
MYBPC1 M-motif missense
        │
        ▼
Altered sMyBP-C N-terminus ── binding to myosin ↑ (Y247H/E248K) or ↓ (L263R)
        │
        ▼
Dysregulated actomyosin cross-bridge cycling / stretch activation (type-1 fibers)
        │
        ├──► Aberrant pulsatile myofilament oscillation ──► muscle spindle pickup
        │                                                     │
        │                                                     ▼
        │                                        ~10–11 Hz MYOGENIC TREMOR
        │                                        (± spinal central-loop amplification)
        │
        └──► Chronic mild contractile deficit
                     │
                     ├──► Hypotonia, proximal/axial weakness
                     ├──► Flexion contractures, scoliosis, spinal rigidity
                     └──► (neonatal) laryngeal stridor, undulating tongue
```

### Detail by category

- **Molecular pathways / biochemical abnormalities:** The core defect is in the **sarcomeric thick-filament regulatory system**. sMyBP-C normally modulates the kinetics of myosin cross-bridge attachment via its N-terminal M-motif interacting with myosin S2/head and actin. Variants shift this equilibrium, altering cross-bridge cycling and stretch-activation responses. No canonical signaling cascade (Wnt/MAPK/mTOR/PI3K-AKT) is implicated — this is a structural/mechanochemical sarcomere disease.
- **Cellular processes:** Dysregulated excitation–contraction coupling and myofilament mechanics in slow-twitch skeletal myofibers; aberrant pulsatile activity. No prominent apoptosis, autophagy, or inflammation is reported as primary.
- **Protein dysfunction:** Dominant gain-of-dysfunction. Both increased and decreased sMyBP-C–myosin binding are pathogenic, indicating that precise tuning of this interaction is required and that perturbation in either direction disrupts contractile regulation.
- **Metabolic changes:** sMyBP-C recruits muscle creatine kinase (CKM) to the myosin filament, linking the contractile machinery to local ATP buffering; perturbation may locally affect energy delivery to the cross-bridge, though this is not fully established in CMYO16.
- **Immune involvement:** None.
- **Tissue damage mechanisms:** Primarily functional/mechanical rather than degenerative; muscle biopsy shows myopathic changes (see Diagnostics).
- **Suggested GO terms:** GO:0006936 (muscle contraction), GO:0030049 (muscle filament sliding), GO:0032036 (myosin heavy chain binding), GO:0005859 (muscle myosin complex), GO:0030017 (sarcomere, cellular component).
- **Suggested CL terms:** CL:0000189 (slow muscle cell), CL:0008002 (skeletal muscle fiber), CL:0000188 (cell of skeletal muscle).

### Molecular profiling

No transcriptomic, proteomic, metabolomic, or lipidomic disease-signature datasets are published for CMYO16 specifically. Mechanistic evidence comes from targeted biochemistry (binding assays), ex-vivo myofilament physiology, and the knock-in mouse (below).

---

## 7. Anatomical Structures Affected

- **Organ/body system level:** Skeletal muscle (musculoskeletal system). Secondary involvement of the axial skeleton (scoliosis, spinal rigidity, lumbar hyperlordosis) and, in neonates, the **larynx/upper airway** (stridor) and **tongue** (tremor/undulating movements).
- **Tissue level:** Striated skeletal **muscle tissue**, with predominant effect on **slow (type-1) fibers** (sMyBP-C is the slow-fiber MyBP-C isoform). UBERON:0001134 (skeletal muscle tissue); UBERON:0003672 (axial skeletal muscle); UBERON:0001737 (larynx); UBERON:0001723 (tongue).
- **Cell level:** Slow skeletal muscle fibers (CL:0000189); muscle spindle sensory apparatus is implicated in tremor propagation.
- **Subcellular level:** The **sarcomere** (GO:0030017), specifically the **C-zone of the A-band thick filament** where MyBP-C resides; the **muscle myosin complex** (GO:0005859). No mitochondrial, nuclear, ER, or lysosomal primary defect.
- **Localization / lateralization:** Bilateral and generally symmetric; proximal and axial predominance of weakness; tremor affects limbs (postural/action) and can involve facial/tongue musculature.

---

## 8. Temporal Development

- **Onset:** Congenital/infantile — hypotonia and tremor from early infancy; onset pattern is insidious/chronic (not acute).
- **Progression:** Mild and slowly evolving; **weakness tends to stabilize or improve after adolescence** ("gradual clinical improvement"). Tremor typically persists. Scoliosis/contractures may progress and need monitoring.
- **Course pattern:** Chronic, lifelong, but non-degenerative and relatively stable/improving — distinguishing it from progressive muscular dystrophies.
- **Critical periods:** The neonatal period carries the main acute risk (respiratory distress/stridor requiring non-invasive ventilation in a minority). Childhood/adolescence is the window of functional improvement.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant** (HP:0000006). Both inherited (multigeneration families) and de novo variants reported.
- **Penetrance:** Appears high in reported families (variants segregate with disease across three generations), though the small sample precludes precise estimates.
- **Expressivity:** Variable — ranging from predominantly tremor with minimal weakness to neonatal respiratory compromise.
- **Mosaicism / anticipation / founder effects / consanguinity:** No genetic anticipation (not a repeat-expansion disorder). No founder effect or consanguinity role (dominant; de novo events documented). Germline mosaicism not specifically reported for human CMYO16 (notably documented in the porcine MYH7 model — a different gene — see comparative section).
- **Carrier frequency:** Not applicable in the recessive sense (dominant disorder); causal variants are vanishingly rare in the population.
- **Epidemiology:** **Ultra-rare.** By mid-2024, approximately **16 patients from ~8 families** had been reported (13 patients/6 families plus 3 new patients/2 families; Neurol Clin Pract 2024, [PMID: 38690148](https://pubmed.ncbi.nlm.nih.gov/38690148/)). No prevalence/incidence estimates per 100,000 are available. No sex predilection established in humans (the mouse model shows sex-dependent progression). No specific geographic/ethnic clustering reported.

---

## 10. Diagnostics

**Clinical / laboratory:**
- **EMG:** Myopathic abnormalities (HP:0003458), present in those tested.
- **Serum CK:** Typically normal or mildly elevated (congenital myopathy pattern).
- **Muscle biopsy:** Myopathic changes; specific uniform CMYO16 histopathology is not firmly codified given the small cohort.
- **Tremor characterization:** Quantitative accelerometry/EMG shows a distinctive **high-frequency ~10–11 Hz postural/action tremor**; this myogenic signature is a key diagnostic clue distinguishing it from central (e.g., essential, parkinsonian) tremor.
- **Imaging:** Muscle MRI and spine imaging (for scoliosis) are supportive but no pathognomonic pattern is defined.

**Genetic testing (definitive):**
- **First-line:** Gene panel for congenital myopathies including *MYBPC1*, or exome/genome sequencing.
- **Targeted/single-gene:** *MYBPC1* sequencing, focusing interpretation on **N-terminal M-motif missense variants** (CMYO16), while recognizing that other *MYBPC1* variants cause DA1B (OMIM 614335) or LCCS4 (OMIM 614915).
- WES/WGS are highly useful given phenotypic overlap with other congenital myopathies. CMA, karyotyping, FISH, mtDNA testing, and repeat-expansion testing are **not** indicated (no structural, mitochondrial, or repeat basis).

**Clinical criteria / differential diagnosis:** No formal consensus diagnostic criteria exist. Differential diagnoses include other congenital myopathies (nemaline, core, centronuclear), other MyBP-C/arthrogryposis phenotypes, central tremor disorders, and the rare *MYH7* tremor-myopathy case. The combination of congenital hypotonia + mild non-progressive weakness + a sarcomere-origin high-frequency tremor + an M-motif *MYBPC1* variant is diagnostic.

**Screening:** No population newborn screening. Cascade/predictive genetic testing and genetic counseling are appropriate for at-risk relatives in known families.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** Generally favorable; the disorder is not typically life-limiting. The main acute risk is **neonatal respiratory impairment** (laryngeal stridor requiring non-invasive ventilation) in a minority of cases.
- **Morbidity/function:** Mild myopathy "invariably associated with a distinctive myogenic tremor and hypotonia with gradual clinical improvement" (Neurol Clin Pract 2024, [PMID: 38690148](https://pubmed.ncbi.nlm.nih.gov/38690148/)). Persistent tremor and musculoskeletal features (scoliosis, contractures) are the main long-term morbidities.
- **Recovery potential:** Weakness tends to stabilize/improve after adolescence; tremor persists.
- **Prognostic factors:** Neonatal respiratory involvement marks a more severe early course; otherwise prognosis is good.
- **QoL measures:** No disease-specific validated instruments reported.

---

## 12. Treatment

**No disease-modifying or gene-specific therapy exists.** Management is **supportive and multidisciplinary**:
- **Respiratory:** Neonatal monitoring; non-invasive ventilation for stridor/respiratory distress when present.
- **Orthopedic:** Monitoring and management of scoliosis, flexion contractures, spinal rigidity (bracing, physiotherapy, surgery if indicated).
- **Rehabilitation:** Physical therapy, occupational therapy; stretching for contractures; mobility support.
- **Tremor management:** No established pharmacotherapy proven for this myogenic tremor; because it is sarcomere-origin rather than central, classic central-tremor drugs may be less effective (unproven).
- **Pharmacogenomics / gene therapy / cell therapy / RNA therapy / immunotherapy:** None available or in trials specifically for CMYO16.
- **Experimental:** No registered disease-specific clinical trials (ClinicalTrials.gov) identified. Future sarcomere-modulating agents are conceptually relevant but untested here.
- **Genetic counseling** is a core component (autosomal dominant; 50% transmission risk; de novo recurrence counseling).

Suggested NCIT intervention concepts: Supportive Care; Physical Therapy; Occupational Therapy; Mechanical Ventilation; Orthopedic Surgery; Genetic Counseling.

---

## 13. Prevention

- **Primary prevention:** Not applicable (genetic disorder). **Genetic counseling** and, where desired, **preimplantation genetic testing (PGT)** or **prenatal testing** in families with a known variant.
- **Secondary prevention:** Early detection of at-risk relatives via cascade genetic testing; early neonatal respiratory surveillance in affected pedigrees.
- **Tertiary prevention:** Proactive orthopedic and respiratory management to prevent complications (scoliosis progression, contracture, airway compromise).
- **Immunization / public health / environmental / prophylaxis:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Human gene / orthologs:** *MYBPC1* (NCBI Gene 4604). Orthologs exist across vertebrates (the affected M-motif residues are conserved across vertebrates, which underpins their pathogenicity).
- **Natural disease in other species (same gene):** No well-characterized naturally occurring *MYBPC1* M-motif tremor-myopathy is documented in companion animals or livestock to date.
- **Comparative note (different gene, analogous phenotype):** A naturally occurring **MYH7** tremor-myopathy, "**Campus syndrome (CPS),**" occurs in pigs — a de novo germline (and somatic mosaic) in-frame insertion in *MYH7* exon 30 (c.4320_4321insCCCGCC; p.Ala1440_Ala1441insProAla) causing progressive postural tremor in ~9% of a founder boar's offspring, with dominant inheritance confirmed by backcross ([PMID: 23153285](https://pubmed.ncbi.nlm.nih.gov/23153285/)). This is a *different gene* from CMYO16 but illustrates that sarcomere thick-filament defects can produce dominant tremor-myopathy across species. It is included only for comparative biology; it is **not** the MONDO:0032797 disease.

---

## 15. Model Organisms

- **Mouse (primary model):** An **E248K knock-in mouse (E248K-KI)** carrying the human variant recapitulates the myopathy and shows **sex-dependent, muscle-specific progression with aging** (Dominguez-Martin / Kontrogianni-Konstantopoulos group, *JCI Insight* 2025;10(15):e182471, [PMID: 40569690](https://pubmed.ncbi.nlm.nih.gov/40569690/)). This is the key tool for studying disease mechanism and testing interventions.
- **Ex-vivo myofilament studies:** Implicate **aberrant stretch activation / pulsatile myofilament activity** in slow-twitch fibers as a tremor driver (*Int J Mol Sci* 2025;26:5252, [PMID: 40508067](https://pubmed.ncbi.nlm.nih.gov/40508067/)).
- **Model strengths:** The E248K-KI reproduces the myopathy and allows dissection of age- and sex-dependent progression and myofilament physiology.
- **Model limitations:** Tremor phenotyping in mice is challenging; central-loop amplification of a myogenic tremor may differ between species; only one variant (E248K) is modeled as a knock-in so far.
- **Resources:** MGI (mouse *Mybpc1*); model generated by academic groups rather than large repositories.

---

## Mechanistic Model / Interpretation

CMYO16 is best understood as a **sarcomere thick-filament regulatory disease** in which precise tuning of the sMyBP-C N-terminal M-motif's interaction with myosin is essential for normal slow-fiber contractile kinetics. The striking biochemical observation that **opposite effects on binding (increased for Y247H/E248K, decreased for L263R) both cause the same clinical entity** indicates that the M-motif functions as a finely balanced mechanochemical regulator; perturbation in either direction destabilizes cross-bridge cycling and stretch activation. The resulting aberrant, oscillatory myofilament activity in slow-twitch fibers is sensed by muscle spindles and manifests as a distinctive ~10–11 Hz **myogenic tremor** — a tremor whose origin is the muscle itself rather than the central nervous system, possibly reinforced by a segmental spinal reflex loop.

This "bottom-up" tremor model is conceptually supported by electrophysiological work on an analogous sarcomere-myopathy patient, in whom the authors proposed that *"the tremor originates at the sarcomere level within muscles, which is then picked up by muscle spindles and leads to activating input to the neuraxis segment"* ([PMID: 37070061](https://pubmed.ncbi.nlm.nih.gov/37070061/)). The branch to weakness/hypotonia reflects chronic mild contractile inefficiency, and the musculoskeletal and airway features are downstream mechanical consequences. The E248K knock-in mouse and ex-vivo myofilament studies provide experimental validation of the sarcomeric-origin hypothesis.

---

## Evidence Base

| PMID | Role in this report | Key support |
|---|---|---|
| [31025394](https://pubmed.ncbi.nlm.nih.gov/31025394/) (Stavusis 2019, *Ann Neurol*) | Foundational | Identified Y247H/E248K in two 3-generation families; defined "myogenic tremor"; source of OMIM:618524 HPO frequencies |
| [31264822](https://pubmed.ncbi.nlm.nih.gov/31264822/) (Shashi 2019, *Hum Mutat*) | Foundational | De novo L263R (×3) and L259P (×1); divergent M-motif binding effects |
| [38690148](https://pubmed.ncbi.nlm.nih.gov/38690148/) (Neurol Clin Pract 2024) | Epidemiology/natural history | ~16 patients/~8 families; mild myopathy with tremor + gradual improvement; neonatal stridor |
| [37392669](https://pubmed.ncbi.nlm.nih.gov/37392669/) (Pediatr Neurol 2023) | Phenotype | Respiratory distress with stridor; undulating tongue movements |
| [40569690](https://pubmed.ncbi.nlm.nih.gov/40569690/) (*JCI Insight* 2025) | Model organism | E248K knock-in mouse recapitulates myopathy; sex-/muscle-specific progression |
| [40508067](https://pubmed.ncbi.nlm.nih.gov/40508067/) (*Int J Mol Sci* 2025) | Mechanism | Aberrant stretch activation/pulsatile myofilament activity as tremor driver |
| [37070061](https://pubmed.ncbi.nlm.nih.gov/37070061/) (Vial 2023) | Comparative / correction | Explicitly states myogenic tremor is classically an *MYBPC1* entity; reports a *distinct* first-of-its-kind *MYH7* case — anchors the gene correction |
| [23153285](https://pubmed.ncbi.nlm.nih.gov/23153285/) | Comparative biology | Natural *MYH7* tremor-myopathy (porcine Campus syndrome) — different gene, analogous phenotype |

**Note on the gene correction.** Early in this investigation the disease was provisionally attributed to *MYH7* based on the "myogenic tremor" literature. Authoritative identifier mapping (MONDO:0032797 = OMIM #618524 = CMYO16 = MedGen C5231401) and the explicit statement in [PMID: 37070061](https://pubmed.ncbi.nlm.nih.gov/37070061/) — *"The concept of a myopathy with associated tremor ('myogenic tremor') in humans has been previously described for specific MYBPC1… variants. Here we report for the first time an individual with tremor who was found to have a de-novo likely pathogenic variant in Myosin Heavy Chain 7 (MYH7)"* — confirm that **CMYO16 is an *MYBPC1* disease.** The report is curated accordingly; *MYH7* content is retained only as clearly-labeled comparative material.

---

## Limitations and Knowledge Gaps

1. **Ultra-rare disease:** Only ~16 patients/~8 families reported; all epidemiologic, penetrance, expressivity, and prognostic statements rest on very small numbers.
2. **No prevalence/incidence estimates** per 100,000; no registry.
3. **Limited variant spectrum:** Only four M-motif missense variants are established; genotype–phenotype correlations are preliminary.
4. **No omics signatures** (transcriptomic/proteomic/metabolomic) specific to CMYO16.
5. **Tremor mechanism partly inferred:** The sarcomere-origin model is strongly supported but the precise contribution of central (spinal-loop) amplification in humans is not fully resolved; key electrophysiology quotes come from an analogous *MYH7* case rather than a *MYBPC1* patient.
6. **No targeted therapy or clinical trials;** management is supportive and largely empirical.
7. **Histopathology** of CMYO16 is not uniformly codified.
8. **Biopsy/QoL data** are sparse; no validated disease-specific QoL instrument.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the patient registry:** Aggregate all reported *MYBPC1* M-motif cases (GeneMatcher, international networks) to refine penetrance, expressivity, natural history, and the frequency of neonatal respiratory involvement.
2. **Direct tremor electrophysiology in *MYBPC1* patients:** Perform accelerometry + multi-level EMG coherence studies specifically in CMYO16 patients to confirm sarcomere-origin and quantify any central-loop amplification (replicating the *MYH7*-case paradigm).
3. **Model additional variants:** Generate knock-in mice/iPSC-myotubes for L263R and Y247H to compare increased- vs decreased-binding mechanisms side by side with E248K.
4. **Myofilament mechanics:** Systematic ex-vivo stretch-activation assays across variants to define the biophysical signature that produces oscillation.
5. **Structural studies:** Cryo-EM/modeling of the sMyBP-C M-motif–myosin interface to explain how opposite binding changes converge on tremorgenesis.
6. **Therapeutic screening:** Use E248K-KI mice and patient myotubes to test sarcomere modulators (myosin inhibitors/activators) for tremor suppression.
7. **Biomarker/omics profiling:** Muscle transcriptomics/proteomics from patient biopsies to identify downstream signatures and candidate modifiers.
8. **Standardize diagnostic criteria** and biopsy interpretation for CMYO16 to aid differentiation from central tremor and other congenital myopathies.

---

*Report compiled from OMIM/MedGen/HPO annotations and primary literature. Causal gene: **MYBPC1** (sMyBP-C), chromosome 12q23.2. Disease: Congenital Myopathy-16 (CMYO16 / "Myotrem"), OMIM #618524, MONDO:0032797.*


## Artifacts

- [OpenScientist final report](Myopathy_Congenital_With_Tremor-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Myopathy_Congenital_With_Tremor-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 8 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 29 |
| Terms named correctly | 24 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032797` (6 mentions) - the report calls it "MONDO"; MONDO calls it **myopathy, congenital, with tremor**
- `GO:0030017` (2 mentions) - the report calls it "sarcomere, cellular component", "sarcomere", "Subcellular level:** The **sarcomere"; GO calls it **sarcomere**
- `UBERON:0003672` (1 mention) - the report calls it "axial skeletal muscle"; UBERON calls it **dentition**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000006` (2 mentions) - the report calls it "Autosomal dominant inheritance", "Autosomal dominant", "Inheritance:** **Autosomal dominant"; HP calls it **Autosomal dominant inheritance**, and lists "Autosomal dominant" among its other names
- `CL:0000189` (2 mentions) - the report calls it "slow muscle cell", "Cell level:** Slow skeletal muscle fibers"; CL calls it **slow muscle cell**, and lists "slow muscle fiber" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003458` - called "Myopathic EMG abnormalities", "EMG:** Myopathic abnormalities"
- `HP:0000006` - called "Autosomal dominant inheritance", "Autosomal dominant", "Inheritance:** **Autosomal dominant"
- `GO:0030017` - called "sarcomere, cellular component", "sarcomere", "Subcellular level:** The **sarcomere"
- `CL:0000189` - called "slow muscle cell", "Cell level:** Slow skeletal muscle fibers"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.