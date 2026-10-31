---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-23T17:32:01.353308'
end_time: '2026-10-23T18:03:38.974913'
duration_seconds: 1897.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Myopathy 18
  mondo_id: MONDO:0859514
  category: Mendelian
  causal_genes: CACNA1S
  omim_id: not recorded
  synonyms: CMYO18; CACNA1S-related congenital myopathy
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
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 16
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 14
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: DOID:0081350
    reported_labels:
    - DOID (Disease Ontology)
    ontology_label: congenital myopathy 18
  - term_id: GO:0014801
    reported_labels:
    - triad / junctional SR membrane
    ontology_label: longitudinal sarcoplasmic reticulum
  - term_id: UBERON:0002036
    reported_labels:
    - extraocular muscle, contextually
    ontology_label: striated muscle tissue
  labels_variant: 5
  unresolvable_prefixes:
  - OMIM
  - GARD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Myopathy_18-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Myopathy_18-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Myopathy 18
- **MONDO ID:** MONDO:0859514 (if available)
- **Causal gene(s):** CACNA1S
- **OMIM:** not recorded
- **Synonyms:** CMYO18; CACNA1S-related congenital myopathy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Myopathy 18** covering all of the
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

# Congenital Myopathy 18 (CMYO18) — Comprehensive Disease Characteristics Report

**Disease:** Congenital Myopathy 18 (CMYO18)
**Causal gene:** **CACNA1S** (encoding Ca_V1.1 / the α1S subunit of the skeletal-muscle dihydropyridine receptor, DHPR)
**MONDO ID:** MONDO:0859514 · **OMIM:** #620246 · **DOID:** 0081350 · **GARD:** 0026730 · **UMLS/MedGen:** C5830283
**Category:** Mendelian (autosomal recessive and autosomal dominant)

---

## Summary

Congenital Myopathy 18 (CMYO18) is an ultra-rare inherited skeletal-muscle disease caused by **loss-of-function variants in CACNA1S**, the gene encoding **Ca_V1.1 (the α1S subunit of the L-type voltage-gated calcium channel / dihydropyridine receptor, DHPR)**. It is essential to distinguish CMYO18 from the much better-known *gain-of-function/gating-pore* CACNA1S disease, hypokalemic periodic paralysis (HypoPP); although both involve the same gene, CMYO18 is a structural congenital myopathy driven by reduced Ca_V1.1 protein and impaired excitation–contraction (EC) coupling, not a channelopathy of episodic paralysis. The disease was first defined as a distinct entity by Schartner et al. in 2017 (*Dihydropyridine receptor (DHPR, CACNA1S) congenital myopathy*, Acta Neuropathologica; [PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/)) in an international cohort of 11 patients from 7 families, and it is now catalogued as OMIM #620246 and MONDO:0859514.

Mechanistically, CMYO18 is a **triadopathy / EC-coupling disorder**. Ca_V1.1 is the sarcolemmal/T-tubule voltage sensor that is physically and functionally coupled to the ryanodine receptor RyR1 on the sarcoplasmic reticulum (SR). Pathogenic CACNA1S variants reduce gene expression and/or Ca_V1.1 protein stability, which lowers the amount of functional DHPR at the triad, **impairing depolarization-induced Ca²⁺ release from the SR** and thereby weakening muscle contraction. Because Ca_V1.1 and RyR1 act in the same molecular machine, CMYO18 closely mimics RYR1-related core myopathy clinically and histologically (core-like lesions, SR dilatation) and shares the malignant-hyperthermia-susceptibility gene network (RYR1, CACNA1S, STAC3).

The clinical spectrum is broad and severity-graded by genotype. Milder forms present with neonatal hypotonia, muscle weakness, delayed motor milestones, and cold-provoked episodic weakness; intermediate forms show core-like biopsy findings and exertional rhabdomyolysis with fluctuating asymptomatic hyperCKemia; and the most severe biallelic (recessive) forms present prenatally as **fetal akinesia deformation sequence (FADS)** with progressive hydrops and stillbirth. There is no disease-modifying therapy — management is supportive, with malignant-hyperthermia anesthetic precautions. Disease models include two zebrafish *cacna1s* loss-of-function lines (mild and severe), patient-derived iPSC lines (dominant and recessive), and a naturally occurring recessive bovine disease ("early-onset muscle weakness syndrome" in Holstein cattle).

---

## 1. Disease Information

**Overview.** CMYO18 is a congenital myopathy — a structural, typically non-progressive or slowly progressive inherited muscle disease presenting at or near birth — caused by loss-of-function of **CACNA1S / Ca_V1.1 (DHPR α1S subunit)**. It belongs to the EC-coupling-defect / triadopathy subgroup of congenital myopathies, alongside RYR1- and STAC3-related disease. The founding description by Schartner et al. (2017) framed the disease around excitation–contraction coupling: *"Muscle contraction upon nerve stimulation relies on excitation-contraction coupling (ECC) to promote the rapid and generalized release of calcium within myofibers"* ([PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0859514 ("congenital myopathy 18") |
| OMIM | #620246 (CONGENITAL MYOPATHY 18; CMYO18) |
| DOID (Disease Ontology) | DOID:0081350 |
| GARD | 0026730 |
| UMLS / MedGen | C5830283 |
| Causal gene | CACNA1S — HGNC:1397, NCBI Gene ID 779, locus 1q32.1 |
| Protein | Ca_V1.1 / α1S DHPR subunit — UniProt Q13698 |

Cross-reference lookup (EBI OLS) confirmed MONDO:0859514 ↔ OMIM:620246 ↔ DOID:0081350 ↔ GARD:0026730 ↔ UMLS C5830283; the OMIM title was independently confirmed via NCBI (Finding F007).

**Synonyms / alternative names.** CMYO18; CACNA1S-related congenital myopathy; Dihydropyridine receptor (DHPR) congenital myopathy; DHPR/CACNA1S congenital myopathy.

**Data source.** Information is derived from **aggregated disease-level resources** (OMIM, MONDO, Orphanet-style catalogs) combined with **individual patient reports / small cohorts** in the primary literature (the founding 11-patient/7-family cohort plus subsequent case reports). This is not EHR-derived population data; given the rarity, all knowledge rests on case series and functional studies.

---

## 2. Etiology

**Disease causal factors.** CMYO18 is a **monogenic (Mendelian) genetic disease** caused by pathogenic variants in CACNA1S. There is no environmental or infectious cause. Mechanistically, disease variants act through **loss of gene expression and/or reduced Ca_V1.1 protein stability** (Finding F001): *"CACNA1S-related myopathy, due to pathogenic variants in the CACNA1S gene, is a recently described congenital muscle disease. Disease associated variants result in loss of gene expression and/or reduction of Cav1.1 protein stability"* ([PMID: 37930228](https://pubmed.ncbi.nlm.nih.gov/37930228/)).

**Genetic risk factors.** The causal factor is biallelic (recessive) or monoallelic (dominant) CACNA1S loss-of-function. Both inheritance modes are established: *"we generated three iPSC lines derived from patients with CMyo linked to both autosomal dominant and recessive CACNA1S variants"* ([PMID: 40885023](https://pubmed.ncbi.nlm.nih.gov/40885023/)). The severity correlates with genotype/dosage: biallelic null-type combinations produce the lethal fetal-akinesia end of the spectrum, while milder heterozygous or hypomorphic combinations produce milder weakness.

**Environmental and lifestyle risk factors.** None established as causal. However, **cold exposure** is a well-documented *trigger* of episodic weakness in milder CMYO18 (Finding F002), and **volatile anesthetics/succinylcholine** are relevant triggers because CACNA1S is a malignant-hyperthermia-susceptibility gene (Finding F003).

**Protective factors.** No genetic or environmental protective factors are established for CMYO18. (For the distinct CACNA1S disease HypoPP, trigger avoidance — controlled carbohydrate intake, regular moderate exercise — is protective, but that applies to the channelopathy, not to CMYO18.)

**Gene–environment interactions.** The principal G×E interaction is **genotype + anesthetic exposure** (malignant-hyperthermia risk in the CACNA1S/RYR1/STAC3 network) and **genotype + cold** (cold-provoked episodic weakness). These are triggers of acute events in a genetically determined disease, not modifiers of disease occurrence.

---

## 3. Phenotypes

CMYO18 phenotypes span a wide severity gradient. The table summarizes principal manifestations with suggested HPO terms.

| Phenotype | Type | Onset | Severity / course | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Neonatal hypotonia | Clinical sign | Neonatal/perinatal | Moderate–severe | Core feature | HP:0001319 (Neonatal hypotonia) |
| Axial & generalized muscle weakness | Clinical sign | Perinatal–infancy | Severe in classic cohort | Core feature | HP:0003324 (Generalized muscle weakness); HP:0003327 (Axial muscle weakness) |
| Delayed motor milestones / delayed walking | Clinical sign | Infancy | Variable | Common | HP:0001270 (Motor delay) |
| Episodic weakness, cold-provoked | Symptom | Infancy onward | Fluctuating/episodic | In milder forms | HP:0003325 (Limb-girdle muscle weakness, contextually); episodic weakness |
| Ophthalmoplegia | Clinical sign | Perinatal | Variable | 4/11 (~36%) in founding cohort | HP:0000602 (Ophthalmoplegia) |
| Ptosis | Clinical sign | Perinatal | Variable | Reported | HP:0000508 (Ptosis) |
| Exertional rhabdomyolysis / hyperCKemia | Lab abnormality | Childhood–adult | Mild expanded phenotype | Subset | HP:0003236 (Elevated CK); HP:0003201 (Rhabdomyolysis) |
| Fetal akinesia / FADS, hydrops, arthrogryposis | Physical manifestation | Prenatal | Lethal (stillbirth) | Severe biallelic forms | HP:0001989 (Fetal akinesia); HP:0001561 (Polyhydramnios); HP:0002804 (Arthrogryposis) |
| Respiratory insufficiency | Clinical sign | Neonatal (severe forms) | Severe | Severe end | HP:0002093 (Respiratory insufficiency) |

**Key supporting quotes.** Neonatal/cold phenotype: *"Both sisters had neonatal onset hypotonia, muscle weakness, and delayed walking. Episodic weakness started in infancy and continued thereafter, provoked mostly by cold exposure"* ([PMID: 38426167](https://pubmed.ncbi.nlm.nih.gov/38426167/)). Founding-cohort phenotype and ophthalmoplegia frequency: *"We describe a cohort of 11 patients from 7 families presenting with perinatal hypotonia, severe axial and generalized weakness. Ophthalmoplegia is present in four patients"* ([PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/)). Severe end: *"Trio whole exome sequencing (WES) detected compound heterozygous likely pathogenic CACNA1S gene variants associated with autosomal dominant (AD) and autosomal recessive (AR) congenital myopathy and FADS"* ([PMID: 38111203](https://pubmed.ncbi.nlm.nih.gov/38111203/)).

**Age of onset:** neonatal/perinatal for classic disease; prenatal for severe biallelic FADS; childhood–adult for mild exertional-rhabdomyolysis forms. **Progression:** generally static to slowly progressive (typical of congenital myopathies), with episodic fluctuations triggered by cold or exertion. **Quality-of-life impact:** substantial in severe forms (motor disability, respiratory support, feeding difficulty); milder forms have variable impact driven by weakness and exertional episodes. No disease-specific EQ-5D/SF-36 data exist given rarity.

---

## 4. Genetic / Molecular Information

**Causal gene.** **CACNA1S** (HGNC:1397; NCBI Gene ID 779; chromosome **1q32.1**), encoding **Ca_V1.1 / α1S subunit** of the skeletal-muscle L-type voltage-gated calcium channel (DHPR); protein UniProt **Q13698**.

**Pathogenic variants.**
- **Variant classes:** Loss-of-function mechanism predominates — variants reduce expression and/or destabilize Ca_V1.1 protein. Reported variants include missense, and biallelic combinations (including likely-pathogenic compound heterozygous variants in the FADS cases). The founding study identified **ten recessive or dominant CACNA1S mutations** across the cohort.
- **Classification:** Interpreted per **ACMG/AMP** guidelines; cohorts report class 4/5 (likely pathogenic/pathogenic) variants and VUS requiring functional/segregation support (Findings F004, F006; [PMID: 34440373](https://pubmed.ncbi.nlm.nih.gov/34440373/), [PMID: 33060286](https://pubmed.ncbi.nlm.nih.gov/33060286/)).
- **Functional consequence:** **Loss of function** — decreased Ca_V1.1 protein and major impairment of depolarization-induced Ca²⁺ release: *"Both recessive and dominant mutations correlated with a consistent phenotype, a decrease in protein level, and with a major impairment of Ca2+ release induced by depolarization in cultured myotubes"* ([PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/)).
- **Origin:** **Germline.** No somatic involvement (non-neoplastic Mendelian disease).
- **Allele frequency:** CACNA1S loss-of-function/CMYO18 alleles are individually rare; precise population frequencies in gnomAD are not catalogued for CMYO18-specific alleles. (Note: distinct HypoPP alleles such as p.Arg528His and p.Arg1239His are recurrent but cause a different disease.)

**Important disambiguation of CACNA1S variant → phenotype relationships:**

| CACNA1S phenotype | Mechanism | Representative |
|---|---|---|
| **CMYO18 (this disease)** | Loss of function — ↓Ca_V1.1, impaired EC coupling | [PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/) |
| Hypokalemic periodic paralysis (HypoPP) | Gating-pore/ω-current, S4 arginine neutralization (gain of abnormal function) | e.g. p.Arg528His, p.Arg1239His |
| Malignant hyperthermia susceptibility | EC-coupling dysregulation on anesthetic trigger | RYR1/CACNA1S/STAC3 network |

**Modifier genes.** No specific modifier genes are established for CMYO18. Functionally coupled triad partners (RYR1, STAC3, CACNB1) can produce overlapping phenotypes, and genetic background within the EC-coupling apparatus is biologically plausible as a modifier, but this is not demonstrated for CMYO18.

**Epigenetic information / chromosomal abnormalities.** None reported. CMYO18 is a single-gene SNV/indel disorder; no methylation signatures, histone-modification data, or large structural/chromosomal changes are documented.

---

## 5. Environmental Information

CMYO18 has **no environmental, toxic, occupational, or infectious cause** — it is purely genetic. Environmental factors act only as **triggers of acute events** in genetically affected individuals:
- **Cold exposure** → episodic weakness (milder forms; [PMID: 38426167](https://pubmed.ncbi.nlm.nih.gov/38426167/)).
- **Volatile anesthetics / succinylcholine** → malignant-hyperthermia risk (CACNA1S is an MHS gene; [PMID: 42189464](https://pubmed.ncbi.nlm.nih.gov/42189464/)).
- **Strenuous exertion / heat** → exertional rhabdomyolysis/heat illness in the expanded phenotype ([PMID: 32054689](https://pubmed.ncbi.nlm.nih.gov/32054689/)).

No lifestyle factors (smoking, diet, alcohol) are implicated in causation. No infectious agents are involved.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **pathogenic CACNA1S variant** (recessive biallelic or dominant monoallelic) is present in the germline → **leads to** reduced CACNA1S gene expression and/or destabilized Ca_V1.1 protein (demonstrated — reduced protein level in patient myotubes, [PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/); [PMID: 37930228](https://pubmed.ncbi.nlm.nih.gov/37930228/)).
2. Reduced Ca_V1.1 protein → **results in** fewer functional DHPR voltage sensors at the T-tubule/triad junction (demonstrated — decreased protein; inferred — proportional reduction of triad DHPR tetrads).
3. Fewer functional DHPRs → **impairs** voltage-sensor coupling to RyR1 on the SR → **results in** **major reduction of depolarization-induced SR Ca²⁺ release** (demonstrated — impaired depolarization-induced Ca²⁺ release in cultured myotubes, [PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/)).
4. Reduced cytosolic Ca²⁺ transient → **leads to** weak/insufficient actin–myosin cross-bridge activation → **results in** muscle weakness and hypotonia (inferred from EC-coupling physiology; consistent with clinical phenotype).
5. Branch — **structural/triad remodeling:** impaired EC-coupling apparatus → **leads to** SR dilatation, intermyofibrillar network disorganization, core-like lesions (predominantly type 2 fibers), and internal nuclei on biopsy (demonstrated histologically, [PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/); [PMID: 29193480](https://pubmed.ncbi.nlm.nih.gov/29193480/)).
6. Branch — **severity gradient:**
   - Mild/partial LOF → cold-provoked episodic weakness, exertional rhabdomyolysis, fluctuating hyperCKemia.
   - Severe biallelic (near-null) LOF → profound fetal akinesia → **leads to** FADS, progressive hydrops, arthrogryposis, and stillbirth (demonstrated clinically, [PMID: 38111203](https://pubmed.ncbi.nlm.nih.gov/38111203/)).

```
CACNA1S LOF variant (germline)
        │  ↓ expression / ↓ protein stability
        ▼
  ↓ Ca_V1.1 (DHPR) protein at triad
        │
        ▼
  ↓ functional DHPR voltage sensors
        │  impaired DHPR–RyR1 conformational coupling
        ▼
  ↓↓ depolarization-induced SR Ca²⁺ release  ◄── core defect
        │
   ┌────┴─────────────────────┐
   ▼                          ▼
weak contraction          triad remodeling
(hypotonia, weakness)     (SR dilatation, cores,
   │                       internal nuclei, type-2 predominance)
   ▼
Severity gradient by residual Ca_V1.1 function:
 mild → episodic/cold-provoked weakness, exertional rhabdomyolysis, hyperCKemia
 severe biallelic → fetal akinesia → FADS, hydrops, stillbirth
```

### Mechanistic detail by category

- **Molecular pathway / cellular process:** Skeletal-muscle **excitation–contraction coupling** (the signature affected pathway) — GO:0006936 (muscle contraction), GO:0051209 (release of sequestered Ca²⁺ into cytosol), GO:0010881 (regulation of cardiac muscle contraction by Ca²⁺ — paralog context). Core processes: **voltage sensing → conformational coupling → Ca²⁺ release**.
- **Protein dysfunction:** **Loss of function** of Ca_V1.1 via decreased expression/stability; reduced DHPR density rather than altered single-channel gain (contrast with HypoPP gating-pore gain-of-abnormal-function). GO:0005245 (voltage-gated calcium channel activity), GO:0005891 (voltage-gated calcium channel complex).
- **Biochemical abnormality / ion-channel defect:** Impaired L-type Ca²⁺ channel / DHPR voltage-sensor function at the triad; reduced depolarization-induced SR Ca²⁺ flux through RyR1.
- **Tissue-damage mechanism:** In the exertional subset, insufficient/dysregulated Ca²⁺ handling contributes to **rhabdomyolysis** and CK leakage ([PMID: 29193480](https://pubmed.ncbi.nlm.nih.gov/29193480/)).
- **Immune/metabolic/epigenetic involvement:** None established. Not an autoimmune, metabolic-storage, or epigenetic disease.
- **Molecular profiling:** Patient myotube studies show reduced Ca_V1.1 protein and impaired Ca²⁺ transients ([PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/)); zebrafish and iPSC models recapitulate loss-of-function physiology ([PMID: 37930228](https://pubmed.ncbi.nlm.nih.gov/37930228/); [PMID: 40885023](https://pubmed.ncbi.nlm.nih.gov/40885023/)). No large-scale CMYO18 transcriptomic/proteomic/metabolomic datasets are published.

**Cell types (CL) and biological processes (GO):** CL:0000188 (skeletal muscle cell / myofiber), CL:0008002 (skeletal muscle myoblast), CL:0000056 (myoblast). GO:0006936 (muscle contraction), GO:0051209 (release of sequestered calcium ion into cytosol), GO:0005245 (voltage-gated calcium channel activity).

---

## 7. Anatomical Structures Affected

**Organ / system level.** Primary: **skeletal muscle** (musculoskeletal system). Secondary involvement in severe forms: **respiratory muscles** (respiratory insufficiency), **extraocular muscles** (ophthalmoplegia/ptosis), bulbar/feeding musculature. In severe fetal forms, **generalized fetal akinesia** leads to secondary **joint contractures (arthrogryposis)** and **hydrops**.

**Tissue and cell level.** Striated **skeletal muscle tissue**; affected cells are **skeletal myofibers** (CL:0000188). Biopsy shows predominant involvement of **type 2 (fast) fibers** with core-like lesions: *"His muscle biopsy showed core-like structures occurring mainly in type 2 fibers"* ([PMID: 29193480](https://pubmed.ncbi.nlm.nih.gov/29193480/)).

**Subcellular level.** The defect localizes to the **triad junction** — the T-tubule membrane (where DHPR/Ca_V1.1 resides) apposed to the **sarcoplasmic reticulum** (where RyR1 resides). Pathology features **SR dilatation** and intermyofibrillar network disorganization. Relevant GO Cellular Component terms: GO:0030315 (T-tubule), GO:0016529 (sarcoplasmic reticulum), GO:0014802 (terminal cisterna), GO:0005891 (voltage-gated calcium channel complex), GO:0014801 (triad / junctional SR membrane).

**Localization (UBERON).** UBERON:0001134 (skeletal muscle tissue), UBERON:0002036 (extraocular muscle, contextually); process is **generalized and bilateral/symmetric** (not lateralized), with **axial and proximal predominance**.

---

## 8. Temporal Development

**Onset.** Typically **congenital/perinatal** (neonatal hypotonia and weakness). The severe biallelic form has **prenatal** onset (fetal akinesia). A milder subset presents in **childhood–adulthood** with exertional rhabdomyolysis/hyperCKemia. Onset pattern is generally **chronic/insidious** congenital weakness, punctuated by **episodic** acute events (cold- or exertion-provoked).

**Progression.** Consistent with congenital myopathies, the course is largely **static or slowly progressive** rather than relentlessly degenerative. Episodic weakness is **fluctuating**. Severe fetal forms are **rapidly lethal** (stillbirth). Disease duration in survivors is **chronic/lifelong**.

**Patterns.** No spontaneous remission; episodic events resolve with trigger avoidance/rest. **Critical period:** the **prenatal/perinatal window** is decisive for the severe end (fetal akinesia determines viability); perioperative periods are critical windows of vulnerability (malignant-hyperthermia risk).

---

## 9. Inheritance and Population

**Epidemiology.** CMYO18 is **ultra-rare**; precise prevalence/incidence are not established. Knowledge rests on a founding cohort of 11 patients/7 families ([PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/)) plus scattered case reports. In a single-center pediatric congenital-myopathy series, CACNA1S myopathy was a **rare** cause (identified in 1 of 12 children; RYR1 was most frequent at 41.7%) ([PMID: 42887168](https://pubmed.ncbi.nlm.nih.gov/42887168/)).

**Inheritance.** **Both autosomal recessive and autosomal dominant** ([PMID: 40885023](https://pubmed.ncbi.nlm.nih.gov/40885023/); [PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/)). The most severe (fetal akinesia) forms are **biallelic/recessive** ([PMID: 38111203](https://pubmed.ncbi.nlm.nih.gov/38111203/)).

**Penetrance / expressivity.** Expressivity is **highly variable** (mild cold-sensitive weakness → lethal FADS), correlating with genotype/residual Ca_V1.1 function. Precise penetrance figures are not established given rarity. No genetic anticipation (not a repeat-expansion disorder). Germline mosaicism, founder effects, and carrier frequencies are not specifically documented for CMYO18.

**Consanguinity.** Plausibly relevant for recessive biallelic cases (as for many ultra-rare recessive myopathies), but not systematically quantified.

**Population demographics.** No ethnic predilection, geographic clustering, or sex bias is established; congenital myopathies in general affect sexes roughly equally. Age distribution skews to **neonatal/pediatric** presentation, with a milder adult-recognized subgroup.

---

## 10. Diagnostics

**Clinical/laboratory tests.** Serum **creatine kinase (CK)** may be normal, mildly elevated, or markedly elevated (fluctuating hyperCKemia, especially in the exertional subset; [PMID: 29193480](https://pubmed.ncbi.nlm.nih.gov/29193480/), LOINC CK 2157-6).

**Muscle biopsy / histopathology.** Characteristic findings: **core-like structures (predominantly type 2 fibers)**, an abnormal **intermyofibrillar network due to SR dilatation**, **internal nuclei**, and areas of **myofibrillar disorganization** ([PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/); [PMID: 29193480](https://pubmed.ncbi.nlm.nih.gov/29193480/)). These overlap with RYR1 core myopathy, so biopsy alone is not definitive.

**Imaging.** Muscle MRI can show selective involvement patterns (e.g., a described posterior-to-anterior thigh gradient in one patient). Imaging supports but does not establish diagnosis.

**Genetic testing (definitive).** Diagnosis is achieved by **next-generation sequencing** — broad **neuromuscular/congenital-myopathy gene panels or whole-exome/trio-WES**, interpreted per **ACMG/AMP** guidelines with segregation and functional studies: *"variants filtering and interpretation according to ACMG guidelines, segregation studies, deep phenotyping of patients and relatives, transcripts and protein studies"* ([PMID: 34440373](https://pubmed.ncbi.nlm.nih.gov/34440373/)). Trio-WES established the FADS cases ([PMID: 38111203](https://pubmed.ncbi.nlm.nih.gov/38111203/)). WGS/WES and multigene panels including CACNA1S (alongside RYR1, STAC3, CACNB1, SELENON, NEB, collagen VI genes) are the recommended approach. Chromosomal microarray, karyotyping, FISH, mtDNA, and repeat-expansion testing are **not indicated** (single-gene SNV/indel disorder).

**Functional confirmation.** Reduced Ca_V1.1 protein and impaired depolarization-induced Ca²⁺ release in patient myotubes provide functional validation of candidate variants ([PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/)).

**Differential diagnosis.** RYR1-related core/multiminicore myopathy, STAC3 disorder (Native American myopathy), CACNB1-related myopathy ([PMID: 41023410](https://pubmed.ncbi.nlm.nih.gov/41023410/)), other congenital myopathies (SELENON, NEB, collagen VI), and — critically — **HypoPP** and malignant-hyperthermia susceptibility, both also CACNA1S-linked but mechanistically distinct.

**Screening.** No newborn screening exists. Cascade genetic testing of relatives and genetic counseling are appropriate once a causal variant is identified.

---

## 11. Outcome / Prognosis

**Survival / mortality.** Highly genotype-dependent. The **severe biallelic fetal-akinesia form is lethal** (stillbirth; [PMID: 38111203](https://pubmed.ncbi.nlm.nih.gov/38111203/)). Milder forms are compatible with survival into adulthood, with disability driven by weakness and respiratory involvement.

**Morbidity / function.** Chronic motor disability (hypotonia, weakness, delayed/limited ambulation), potential respiratory morbidity, and episodic weakness in milder forms. No disease-specific QoL instruments are validated for CMYO18.

**Disease course / complications.** Respiratory failure is the principal life-threatening complication in severe forms. Exertional rhabdomyolysis and malignant-hyperthermia reactions are acute risks. Recovery potential: congenital myopathies are generally non-regressive — supportive care maintains function but does not reverse the defect.

**Prognostic factors.** The strongest prognostic determinant is **genotype / residual Ca_V1.1 function** (biallelic null → fetal lethality; partial LOF → milder weakness). Degree of respiratory and bulbar involvement at presentation also predicts outcome.

---

## 12. Treatment

**There is no disease-modifying or curative therapy for CMYO18.** Management is **supportive and multidisciplinary** (NCIT: C15231 Supportive Care; C15719 Physical Therapy; C15329 Occupational Therapy; C94296 Respiratory Therapy):

- **Supportive/rehabilitative care:** physiotherapy, occupational therapy, respiratory support/ventilation as needed, nutritional/feeding support, orthopedic management of contractures.
- **Anesthetic precautions:** Because CACNA1S is a malignant-hyperthermia-susceptibility gene, **avoid volatile anesthetics and succinylcholine**; have **dantrolene** available (NCIT: C62035 Dantrolene) — a critical perioperative safety measure ([PMID: 42189464](https://pubmed.ncbi.nlm.nih.gov/42189464/); [PMID: 41300733](https://pubmed.ncbi.nlm.nih.gov/41300733/)).
- **Trigger avoidance:** cold avoidance for cold-provoked episodic weakness; avoidance of extreme exertion/heat in the rhabdomyolysis-prone subset.
- **No established pharmacotherapy, gene therapy, cell therapy, or RNA-based therapy** exists for CMYO18. (Carbonic-anhydrase inhibitors/potassium management apply to HypoPP, a *different* CACNA1S disease, not CMYO18.)

**Experimental directions.** No CMYO18-specific interventional trials (NCT IDs) are identified. Disease models (zebrafish, iPSC, bovine) are in place as preclinical platforms for future therapy development ([PMID: 37930228](https://pubmed.ncbi.nlm.nih.gov/37930228/); [PMID: 40885023](https://pubmed.ncbi.nlm.nih.gov/40885023/)).

**Personalized medicine.** Genotype-guided: confirming CACNA1S loss-of-function directs MH-safe anesthesia, genetic counseling, and reproductive options.

---

## 13. Prevention

CMYO18 cannot be prevented at the population level (monogenic, non-environmental). Prevention centers on **genetic approaches and complication avoidance**:

- **Primary prevention (reproductive):** Genetic counseling for at-risk families; carrier testing of relatives; **preimplantation genetic diagnosis (PGD)** and **prenatal diagnosis** once a familial variant is known (ACMG/ACOG frameworks).
- **Secondary prevention:** Cascade genetic testing to identify at-risk relatives; early recognition enables MH-safe anesthetic planning.
- **Tertiary prevention (complication avoidance):** Avoid malignant-hyperthermia triggers (volatile anesthetics, succinylcholine); maintain dantrolene availability; cold/exertion-trigger avoidance; proactive respiratory surveillance and physiotherapy to limit contractures and respiratory decline.
- **Counseling:** Genetic counseling is central (recurrence-risk assessment differs for AD vs AR cases).

No immunization, public-health, or environmental interventions are applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human CACNA1S (Gene ID 779) has orthologs across vertebrates — mouse *Cacna1s*, zebrafish *cacna1s*, bovine *CACNA1S*.
- **Natural bovine disease (comparative model):** A **naturally occurring recessive CACNA1S disorder exists in Holstein cattle** ("early-onset muscle weakness syndrome"), first described in the US in 2022: *"Early-onset muscle weakness (MW) syndrome is a genetic disorder in Holstein cattle, that was first described in the US in 2022 and is caused by a recessively inherited variant in the CACNA1S gene"* ([PMID: 42411118](https://pubmed.ncbi.nlm.nih.gov/42411118/)). Affected calves present with congenital astasia/weakness and non-specific clinical/lab findings, requiring genotyping for diagnosis ([PMID: 39551494](https://pubmed.ncbi.nlm.nih.gov/39551494/)). A first European case has since been reported ([PMID: 42411118](https://pubmed.ncbi.nlm.nih.gov/42411118/)). *Species:* NCBI Taxon 9913 (*Bos taurus*).
- **Comparative biology:** The bovine disease is a true natural recessive CACNA1S loss-of-function myopathy, mirroring the human recessive EC-coupling defect and demonstrating evolutionary conservation of the DHPR's role in muscle. Veterinary relevance: it is a recognized Holstein genetic defect amenable to carrier screening.
- **Transmission:** Not applicable (genetic, non-zoonotic).

---

## 15. Model Organisms

| Model | Type | Key features / recapitulation | Reference |
|---|---|---|---|
| **Zebrafish** *cacna1s* LOF lines (2 variants) | Vertebrate, in vivo | Provide **mild and severe** CACNA1S-related myopathy models; reproduce loss-of-expression/protein-stability mechanism | [PMID: 37930228](https://pubmed.ncbi.nlm.nih.gov/37930228/) |
| **Patient-derived iPSC lines (3)** | Human cellular, in vitro | Derived from patients with **both AD and AR** CACNA1S-CMyo variants; platform for EC-coupling/Ca²⁺-release studies and drug screening | [PMID: 40885023](https://pubmed.ncbi.nlm.nih.gov/40885023/) |
| **Patient myotube cultures** | Human primary, in vitro | Demonstrate **decreased Ca_V1.1 protein and impaired depolarization-induced Ca²⁺ release** — the core functional defect | [PMID: 28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/) |
| **Holstein cattle (natural)** | Mammalian, natural disease | Recessive CACNA1S variant → congenital muscle weakness/astasia; natural comparative model | [PMID: 42411118](https://pubmed.ncbi.nlm.nih.gov/42411118/); [PMID: 39551494](https://pubmed.ncbi.nlm.nih.gov/39551494/) |

**Related triad-apparatus models (mechanistic context, not CMYO18 per se):** RyR1-hypomorphic mouse (RyR1^Q1970fsX16) showing reduced RyR1 protein, fewer calcium release units, and reduced Ca²⁺ transients/strength ([PMID: 30689883](https://pubmed.ncbi.nlm.nih.gov/30689883/)); dynamin-2 centronuclear-myopathy mouse with impaired EC coupling ([PMID: 29071728](https://pubmed.ncbi.nlm.nih.gov/29071728/)). These illuminate how quantitative reduction of triad proteins impairs EC coupling — directly analogous to the Ca_V1.1 reduction in CMYO18.

**Model limitations:** No published conditional/knock-in mouse specifically for human CMYO18 CACNA1S alleles; zebrafish and iPSC models capture loss-of-function physiology but not the full severity spectrum or mammalian muscle architecture. Natural bovine disease is valuable but less experimentally tractable.

---

## Mechanistic Model / Interpretation

CMYO18 is best understood as a **dosage/quantitative triadopathy**: the clinical phenotype tracks the **residual amount of functional Ca_V1.1 at the triad**. This unifies the disparate presentations:

| Residual Ca_V1.1 function | EC-coupling capacity | Clinical phenotype |
|---|---|---|
| Near-zero (biallelic null) | Profound EC-coupling failure | Fetal akinesia → FADS, hydrops, stillbirth |
| Moderately reduced | Partial EC-coupling failure | Perinatal hypotonia, severe axial/generalized weakness, ophthalmoplegia, cores/SR dilatation |
| Mildly reduced | Marginal EC-coupling deficit, stress-sensitive | Childhood/adult exertional rhabdomyolysis, fluctuating hyperCKemia, cold-provoked episodic weakness |

The parallel to the RyR1 hypomorph mouse ([PMID: 30689883](https://pubmed.ncbi.nlm.nih.gov/30689883/)), where ~20–58% residual RyR1 produces graded weakness and loss of calcium release units, strongly supports a **threshold/reserve model**: muscle tolerates partial reduction of triad components until a functional reserve is exceeded. Because Ca_V1.1 and RyR1 are two halves of the same voltage-sensor→Ca²⁺-release machine, CMYO18 and RYR1 core myopathy converge on the same histology (cores, SR dilatation) and the same anesthetic risk network (MHS: RYR1/CACNA1S/STAC3).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [28012042](https://pubmed.ncbi.nlm.nih.gov/28012042/) | *DHPR (CACNA1S) congenital myopathy* | **Founding/landmark paper**; cohort, phenotype, histology, functional mechanism (↓protein, ↓Ca²⁺ release) |
| [37930228](https://pubmed.ncbi.nlm.nih.gov/37930228/) | *Two zebrafish cacna1s LOF variants* | Defines LOF mechanism (↓expression/stability); mild+severe models |
| [40885023](https://pubmed.ncbi.nlm.nih.gov/40885023/) | *Three iPSC lines, CACNA1S CMyo* | Confirms both AD and AR inheritance; human cellular model |
| [38426167](https://pubmed.ncbi.nlm.nih.gov/38426167/) | *DHPR case report (two sisters)* | Neonatal hypotonia, delayed walking, cold-provoked episodic weakness |
| [38111203](https://pubmed.ncbi.nlm.nih.gov/38111203/) | *Biallelic CACNA1S → fetal akinesia* | Severe end: FADS, hydrops, stillbirth; trio-WES |
| [29193480](https://pubmed.ncbi.nlm.nih.gov/29193480/) | *Rhabdomyolysis & hyperCKemia, CACNA1S* | Mild expanded phenotype; type-2-predominant core-like biopsy |
| [34440373](https://pubmed.ncbi.nlm.nih.gov/34440373/) | *Integrated clinical-biological myopathy cohort* | NGS panel + ACMG diagnostic strategy |
| [33060286](https://pubmed.ncbi.nlm.nih.gov/33060286/) | *Fetal akinesia/arthrogryposis genomics* | NGS/ACMG diagnosis in fetal-akinesia cohorts |
| [42189464](https://pubmed.ncbi.nlm.nih.gov/42189464/) | *North American MH genetic-testing approach* | CACNA1S as first-line MHS gene (RYR1/CACNA1S/STAC3) |
| [41300733](https://pubmed.ncbi.nlm.nih.gov/41300733/) | *Genetic testing for MH susceptibility* | MH diagnostics; CACNA1S among causative genes |
| [42411118](https://pubmed.ncbi.nlm.nih.gov/42411118/) / [39551494](https://pubmed.ncbi.nlm.nih.gov/39551494/) | *Holstein CACNA1S muscle weakness* | Natural bovine recessive comparative model |
| [32054689](https://pubmed.ncbi.nlm.nih.gov/32054689/) | *Genetic susceptibility to exertional heat illness* | CACNA1S in EHI/ER spectrum |
| [42887168](https://pubmed.ncbi.nlm.nih.gov/42887168/) | *Pediatric congenital myopathy series* | CACNA1S myopathy is rare (1/12); RYR1 dominant |
| [41023410](https://pubmed.ncbi.nlm.nih.gov/41023410/) | *CACNB1 congenital muscular disorder* | Related DHPR β1-subunit triadopathy (differential) |
| [30689883](https://pubmed.ncbi.nlm.nih.gov/30689883/) | *RyR1 hypomorph mouse* | Threshold/reserve model for triad-protein reduction |

**Important caution on citation integrity:** Finding F006's two quotes from PMID 28012042 were flagged `[mismatch]` during validation (the exact wording may differ slightly from the stored abstract). The *substance* — cohort of 11 patients/7 families, perinatal hypotonia, ophthalmoplegia in 4, reduced protein, impaired depolarization-induced Ca²⁺ release — is consistent with the landmark paper, but the verbatim quotes should be re-verified against the published abstract before being entered into the knowledge base as exact quotations.

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity:** No reliable prevalence/incidence, penetrance, sex-ratio, or population-distribution data; all knowledge is from small cohorts and case reports.
2. **Genotype–phenotype correlation is qualitative:** The dosage/threshold model is well-supported conceptually but not quantified (no systematic correlation of residual Ca_V1.1 function with severity across a large cohort).
3. **No -omics depth:** No large transcriptomic, proteomic, metabolomic, or epigenomic CMYO18 datasets exist; molecular profiling rests on targeted functional assays.
4. **No mammalian genetic model of human alleles:** No knock-in mouse for specific human CMYO18 variants; models are zebrafish, iPSC, and natural bovine.
5. **No therapeutics:** No disease-modifying treatment or interventional trials.
6. **Frequent confusion with HypoPP:** Because CACNA1S is far more often cited for HypoPP (gain-of-abnormal-function/gating-pore) and MHS, literature searches are heavily contaminated by these distinct diseases — a persistent risk for knowledge-base curation.
7. **Citation verification:** Two founding-cohort quotes require re-validation (see above).

---

## Proposed Follow-up Experiments / Actions

1. **Build a quantitative genotype–phenotype map:** Aggregate all published CACNA1S-CMYO18 variants with residual Ca_V1.1 protein/function (where measured) and phenotype severity to formally test the threshold/reserve model.
2. **Generate a conditional knock-in mouse** carrying a representative human CMYO18 allele to study triad ultrastructure, EC-coupling physiology, and candidate therapies in mammalian muscle.
3. **Leverage the iPSC lines for drug screening** ([PMID: 40885023](https://pubmed.ncbi.nlm.nih.gov/40885023/)) — screen for compounds/chaperones that stabilize Ca_V1.1 or enhance residual EC coupling; test proteostasis modulators given the protein-stability mechanism.
4. **Explore gene-replacement/ASO strategies** for recessive null alleles, using zebrafish and bovine natural models as preclinical platforms.
5. **Prospective natural-history registry** to establish prevalence, progression rate, respiratory trajectory, and validated QoL outcomes.
6. **Re-verify the two flagged founding-cohort quotes** against the published PMID 28012042 abstract/full text before KB entry.
7. **Curate a disambiguation note** in the knowledge base firmly separating CMYO18 (LOF, congenital myopathy) from HypoPP (gating-pore) and isolated MHS, all CACNA1S-linked.

---

*Report compiled from 7 confirmed findings and 35 reviewed papers across a 5-iteration autonomous investigation. Disease identifiers independently cross-validated (MONDO:0859514 = OMIM #620246 = DOID:0081350 = GARD:0026730 = UMLS C5830283); causal gene CACNA1S (HGNC:1397, Gene ID 779, 1q32.1; protein Ca_V1.1, UniProt Q13698).*


## Artifacts

- [OpenScientist final report](Congenital_Myopathy_18-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Myopathy_18-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 22 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0081350` (3 mentions) - the report calls it "DOID (Disease Ontology)"; DOID calls it **congenital myopathy 18**
- `GO:0014801` (1 mention) - the report calls it "triad / junctional SR membrane"; GO calls it **longitudinal sarcoplasmic reticulum**
- `UBERON:0002036` (1 mention) - the report calls it "extraocular muscle, contextually"; UBERON calls it **striated muscle tissue**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003325` (1 mention) - the report calls it "Limb-girdle muscle weakness, contextually"; HP calls it **Limb-girdle muscle weakness**
- `GO:0051209` (2 mentions) - the report calls it "release of sequestered Ca²⁺ into cytosol", "release of sequestered calcium ion into cytosol"; GO calls it **release of sequestered calcium ion into cytosol**
- `GO:0010881` (1 mention) - the report calls it "regulation of cardiac muscle contraction by Ca²⁺ — paralog context"; GO calls it **regulation of cardiac muscle contraction by regulation of the release of sequestered calcium ion**
- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle cell / myofiber", "skeletal myofibers"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `CL:0008002` (1 mention) - the report calls it "skeletal muscle myoblast"; CL calls it **skeletal muscle fiber**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0051209` - called "release of sequestered Ca²⁺ into cytosol", "release of sequestered calcium ion into cytosol"
- `CL:0000188` - called "skeletal muscle cell / myofiber", "skeletal myofibers"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `GARD`.