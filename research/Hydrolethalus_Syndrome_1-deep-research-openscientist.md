---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-28T17:20:51.439826'
end_time: '2026-10-28T17:52:57.303840'
duration_seconds: 1925.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hydrolethalus Syndrome 1
  mondo_id: MONDO:0009365
  category: Mendelian
  causal_genes: HYLS1
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
  on_topic: 6
  validator_version: 0.4.0
term_validation:
  total_terms: 36
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0009365
    reported_labels:
    - MONDO
    ontology_label: hydrolethalus syndrome 1
  - term_id: HP:0002538
    reported_labels:
    - cortical malformation
    ontology_label: Abnormal cerebral cortex morphology
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hydrolethalus_Syndrome_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hydrolethalus_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hydrolethalus Syndrome 1
- **MONDO ID:** MONDO:0009365 (if available)
- **Causal gene(s):** HYLS1
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

Please provide a comprehensive research report on **Hydrolethalus Syndrome 1** covering all of the
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

# Hydrolethalus Syndrome 1 (HYLS1): A Comprehensive Disease Characterization

**Disease:** Hydrolethalus Syndrome 1 (HLS1) · **MONDO:** MONDO:0009365 · **OMIM:** 236680 · **Causal gene:** **HYLS1** (OMIM 610693; HGNC-approved symbol HYLS1; NCBI GeneID 219844; chromosome 11q24.2)

---

## Summary

Hydrolethalus Syndrome 1 is a rare, autosomal-recessive, perinatally lethal multiple-malformation syndrome caused by **biallelic loss-of-function–type variants in the HYLS1 gene** on chromosome 11q24.2. Despite its serial-number name, the disease belongs squarely to the family of **ciliopathies**: HYLS1 encodes a conserved centriole/basal-body protein, and its dysfunction disrupts the assembly and signaling of the primary cilium during early embryogenesis. The overwhelmingly most common disease allele worldwide is the Finnish founder missense variant **c.632A>G, p.Asp211Gly (D211G; NM_145014.2; rs104894232)**, first linked to the disease by Mee et al. in 2005 ([PMID: 15843405](https://pubmed.ncbi.nlm.nih.gov/15843405/)).

The clinical phenotype is a devastating, recognizable constellation of midline and developmental malformations: hydrocephaly/hydranencephaly with absent midline brain structures, the pathognomonic **occipitoschisis ("keyhole") skull-base defect**, micrognathia, cleft lip/palate, polydactyly of the hands and feet, and defective lobation of the lungs. Affected fetuses are stillborn or die within hours to days of birth; there is no disease-modifying therapy, and management is limited to prenatal diagnosis, genetic counseling, and perinatal palliative care.

Mechanistically, work in *C. elegans*, *Drosophila*, mouse, and mammalian cells converges on a coherent causal chain: the D211G mutation **disrupts the HYLS1–CEP120 interaction**, displacing HYLS1 from the centriole distal end and destabilizing the centriolar microtubule wall; this **loss of centriole integrity impairs ciliary-gate (transition fibre/transition zone) assembly** and intraflagellar transport docking; the resulting **defect in primary-cilium biogenesis and signaling—most critically Hedgehog signaling, modulated via the ciliary lipid kinase PIPKIγ and GPR161/β-arrestin handling—produces the midline, neural, and limb malformations** characteristic of the syndrome. This report documents each link in that chain with primary-literature evidence, and provides the epidemiological, genetic, diagnostic, prognostic, and model-organism detail needed to populate a disease knowledge-base entry.

---

## 1. Disease Information

Hydrolethalus Syndrome 1 is an autosomal-recessive, perinatally lethal fetal malformation disorder. It was originally delineated in the Finnish population, where it is part of the "Finnish disease heritage." The condition is defined by a reproducible pattern of central nervous system (CNS) midline malformations, craniofacial anomalies, polydactyly, and visceral (notably pulmonary) defects.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0009365 |
| OMIM (phenotype) | 236680 (Hydrolethalus syndrome 1) |
| OMIM (gene) | 610693 (HYLS1) |
| Gene (NCBI) | GeneID 219844 |
| Cytogenetic locus | 11q24.2 |
| Orphanet | Hydrolethalus syndrome (rare, lethal) |
| MeSH / ICD | Indexed under congenital malformation syndromes; ICD-10 Q87.8 (other specified congenital malformation syndromes) is typically applied clinically |

**Synonyms / alternative names:** Hydrolethalus syndrome (HLS); HLS1; Salonen-Herva-Norio syndrome.

**Information source type:** The disease-level knowledge is derived from **aggregated disease-level resources** (OMIM, Orphanet, ClinVar, gnomAD) and from **individual/small-series clinical reports and fetal pathology studies**, rather than from large EHR cohorts (the disease is too rare and uniformly lethal for EHR-scale study).

---

## 2. Etiology

**Primary cause — genetic.** HLS1 is a monogenic Mendelian disorder caused by **biallelic pathogenic variants in HYLS1**. There is no infectious or environmental cause. The disease is fully genetically determined once two pathogenic alleles are inherited.

**Genetic risk factors.** The dominant risk factor is **carrier status for the Finnish founder allele D211G (c.632A>G)**. In gnomAD v4 exomes this variant has a global allele frequency of ~5.9×10⁻⁴ but is enriched ~27-fold in Finns (Finnish AF 8.57×10⁻³ vs non-Finnish European 3.19×10⁻⁴; Finding F006). Non-Finnish pathogenic alleles exist — two French fetuses carried the Finnish D211G in trans with novel alleles **c.662G>C, p.Arg221Pro** and **c.613C>T, p.Arg205\*** ([PMID: 34212369](https://pubmed.ncbi.nlm.nih.gov/34212369/)). A large contiguous-gene deletion at 11q23.3–q25 encompassing HYLS1 is also catalogued as pathogenic (Finding F008).

**Environmental risk factors / protective factors / gene–environment interactions.** None established. As a fully penetrant recessive embryonic-lethal disorder, HLS1 has no recognized environmental, lifestyle, dietary, or infectious modifiers, and no protective alleles or behaviors are documented. The only "protective" measure is avoidance of two pathogenic alleles in a conceptus (i.e., reproductive genetics). *Not applicable / not available for this disease.*

---

## 3. Phenotypes

HLS1 presents as a prenatal/neonatal multiple-malformation syndrome. Severity is uniformly **severe (lethal)**; onset is **congenital/prenatal**; the course is non-progressive because death occurs perinatally.

| Phenotype | Type | Frequency / note | Suggested HPO term |
|---|---|---|---|
| Hydrocephaly / hydranencephaly | Physical/structural (CNS) | Core, near-universal | HP:0000238 Hydrocephalus; HP:0007238 Hydranencephaly |
| Absent midline brain structures | Structural (CNS) | Core | HP:0007370 Aplasia/hypoplasia of the corpus callosum |
| Occipitoschisis ("keyhole" skull-base defect) | Structural (cranial) | **Pathognomonic** | HP:0002703 Abnormal skull base morphology (closest) |
| Immature cerebral cortex / abnormal radial glia | Histopathologic (CNS) | Described at fetal autopsy | HP:0002538 (cortical malformation) |
| Hypothalamic hamartoma | Structural (CNS) | Reported key finding | HP:0002902 Hypothalamic hamartoma |
| Micrognathia | Craniofacial | Core | HP:0000347 Micrognathia |
| Cleft lip / cleft palate (midline) | Craniofacial | Common | HP:0000175 Cleft palate; HP:0410030 Cleft lip |
| Polydactyly (hands and feet; pre-/postaxial) | Limb | Core | HP:0100259 Postaxial polydactyly; HP:0001177 Preaxial polydactyly of hand |
| Defective lung lobation | Visceral (respiratory) | Core | HP:0002101 Abnormal lung lobation |
| Abnormal genitalia | Genitourinary | In non-Finnish cases | HP:0000078 Abnormality of the genital system |
| Macrocephaly | Craniofacial | Reported | HP:0000256 Macrocephaly |

**Evidence.** Honkala et al. describe "central nervous system (CNS) malformation such as hydrocephaly and absent midline structures of the brain, micrognathia, defective lobation of the lungs and polydactyly" and note "immature cerebral cortex, abnormalities in radial glial cells and hypothalamic hamartoma are among key findings in the CNS of HLS fetuses" ([PMID: 19400947](https://pubmed.ncbi.nlm.nih.gov/19400947/)). Belengeanu et al. identify occipitoschisis as "the pathognomonic sign of the syndrome" alongside "macrocephaly, midline cleft-lip, cleft palate, polydactyly of both hands and feet" ([PMID: 22029171](https://pubmed.ncbi.nlm.nih.gov/22029171/)). Ghesh et al. expand the spectrum to "pre and postaxial hexadactyly and abnormal genitalia" in non-Finnish fetuses ([PMID: 34212369](https://pubmed.ncbi.nlm.nih.gov/34212369/)). A recent case report describes "open-book cerebral hemispheres, defective lobulation of the lungs (one lobe on the left, two on the right)... and a specific keyhole-shaped defect in the skull base" ([PMID: 39857086](https://pubmed.ncbi.nlm.nih.gov/39857086/)).

**Quality of life.** Not applicable in the conventional sense — the disease is lethal before or shortly after birth. The burden falls on families (pregnancy loss, bereavement) rather than on surviving patients.

---

## 4. Genetic / Molecular Information

**Causal gene.** HYLS1 (HGNC symbol HYLS1; OMIM 610693; GeneID 219844), a 299-amino-acid protein of originally unknown function, located at 11q24.2. Mee et al. mapped HLS to a 1 cM interval on 11q23–25, narrowed by linkage-disequilibrium/haplotype analysis to a 476 kb region between PKNOX2 and DDX25, and identified the causal A>G transition in a novel transcript (FLJ32915), which they named HYLS1 ([PMID: 15843405](https://pubmed.ncbi.nlm.nih.gov/15843405/)).

**Pathogenic variants.**

| Variant (NM_145014.2) | Protein | Type | Classification | Note |
|---|---|---|---|---|
| c.632A>G (rs104894232) | p.Asp211Gly (D211G) | Missense | Pathogenic | Finnish founder allele |
| c.662G>C | p.Arg221Pro | Missense | Reported pathogenic | Non-Finnish (French) |
| c.613C>T | p.Arg205\* | Nonsense | Reported pathogenic | Non-Finnish (French) |
| 11q23.3–q25 deletion | — | Structural/CNV | Pathogenic | Contiguous-gene deletion |

**ClinVar landscape (Finding F008).** A sampled set of ~40 HYLS1 ClinVar records spans the full classification spectrum (~7 Pathogenic, ~13 Likely pathogenic, ~12 VUS, ~7 Likely benign, 1 conflicting). The founder D211G is classified **Pathogenic** (criteria provided, multiple submitters).

**Allele frequency (Finding F006).** gnomAD v4 exomes: D211G global AF 5.88×10⁻⁴ (859/1,461,894); Finnish AF 8.57×10⁻³ (458/53,420); non-Finnish European AF 3.19×10⁻⁴ — a ~26.9-fold Finnish enrichment.

**Origin.** Germline (biallelic, inherited). No somatic contribution.

**Functional consequences.** The D211G missense allele is a **functional loss-of-function with respect to ciliogenesis**. Dammermann et al. demonstrated that "a single amino acid change in human HYLS1 leads to a perinatal lethal disorder... and we show that this mutation impairs HYLS-1 function in ciliogenesis" ([PMID: 19656802](https://pubmed.ncbi.nlm.nih.gov/19656802/)). Mee et al. found altered subcellular localization: wild-type polypeptide was cytoplasmic whereas mutant protein "became localized in distinct nuclear structures" ([PMID: 15843405](https://pubmed.ncbi.nlm.nih.gov/15843405/)).

**Modifier genes / epigenetics.** No validated modifier genes or epigenetic mechanisms are established for HLS1. *Not available.*

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents are implicated in HLS1. The disorder is a pure Mendelian recessive condition. *Not applicable for this disease.*

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic HYLS1 variant (most often D211G)** → produces a HYLS1 protein that **fails to interact normally with CEP120** (demonstrated in mouse; [PMID: 38496445](https://pubmed.ncbi.nlm.nih.gov/38496445/) / [PMID: 40009365](https://pubmed.ncbi.nlm.nih.gov/40009365/)).
2. Loss of the HYLS1–CEP120 interaction → **HYLS1 is displaced from the centriole distal end** → **failure to recruit/stabilize centriole inner-scaffold proteins** → **destabilization of the centriolar microtubule wall and degeneration of the centriole distal end** (demonstrated, mouse).
3. Loss of centriole structural integrity → **impaired assembly of the basal body's distal appendages/transition fibres (TF) and transition zone (TZ)** → **defective ciliary gate** (demonstrated, *C. elegans*; [PMID: 27534274](https://pubmed.ncbi.nlm.nih.gov/27534274/)).
4. Defective ciliary gate → **compromised docking/entry of intraflagellar transport (IFT) particles and impaired gating of membrane and soluble proteins** → **failure of axoneme assembly / primary-cilium biogenesis** (demonstrated, *C. elegans*).
5. In parallel (mammalian branch): HYLS1 is recruited to the ciliary base by **PIPKIγ** and **activates PIPKIγ by relieving its autoinhibitory dimerization**, expediting depletion of centrosomal PI(4)P to **permit axoneme nucleation** (demonstrated, mammalian cells; [PMID: 34162535](https://pubmed.ncbi.nlm.nih.gov/34162535/)).
6. HYLS1 deficiency → **disrupted assembly of the ciliary NPHP module and agonist-induced ciliary exit of β-arrestin** → **impaired removal of ciliary GPR161** → **dysregulated Hedgehog (Hh) signaling** (demonstrated, mammalian cells).
7. Defective primary-cilium–dependent signaling (Hedgehog central; likely Wnt/PCP contributions inferred) during early embryogenesis → **disrupted midline patterning, neural tube/forebrain development, and limb anterior-posterior patterning** → **clinical malformations**: hydrocephaly/hydranencephaly, absent midline brain structures, occipitoschisis, micrognathia, cleft lip/palate, polydactyly, and lung-lobation defects (inferred from cilium/Hedgehog biology linking to the observed phenotype).

```
HYLS1 D211G (biallelic)
      │  disrupts
      ▼
HYLS1–CEP120 interaction lost
      │  displaces HYLS1 from centriole distal end
      ▼
Centriole inner-scaffold destabilized → MT wall degenerates
      │
      ├─► TF/TZ assembly fails → ciliary GATE defective
      │        │ IFT docking + protein gating impaired
      │        ▼
      │   Axoneme/primary cilium fails to form
      │
      └─► (mammal) PIPKIγ not activated → PI(4)P not depleted
               │ NPHP module + β-arrestin exit disrupted
               ▼
          GPR161 not cleared → HEDGEHOG signaling dysregulated
               │  (inferred link to phenotype)
               ▼
   Midline/neural/limb patterning defects → HLS1 malformations → perinatal death
```

### Detail by category

- **Molecular pathways.** Primary-cilium–dependent **Hedgehog signaling** is the best-documented affected pathway (via GPR161/β-arrestin/NPHP module; [PMID: 34162535](https://pubmed.ncbi.nlm.nih.gov/34162535/)). **Phosphoinositide metabolism (PI(4)P via PIPKIγ)** is the proximal lipid-signaling mechanism. Wnt/planar-cell-polarity involvement is plausible for ciliopathies but not directly demonstrated here (inferred).
- **Cellular processes.** Centriole/basal-body biogenesis, ciliogenesis, intraflagellar transport, and ciliary gating. GO suggestions: **GO:0060271 cilium assembly; GO:0098534 centriole assembly; GO:0035869 ciliary transition zone; GO:0036064 ciliary basal body; GO:0042073 intraflagellar transport; GO:0007224 smoothened signaling pathway**.
- **Protein dysfunction.** Loss of function via impaired protein–protein interaction (HYLS1–CEP120) and mislocalization; not aggregation. The centriole inner scaffold is destabilized.
- **Metabolic / biochemical.** Localized phosphoinositide (PI(4)P) remodeling at the centrosome mediated by lipid kinase PIPKIγ (CHEBI: phosphatidylinositol 4-phosphate). No systemic metabolic defect.
- **Immune involvement.** None.
- **Tissue damage mechanism.** Developmental (patterning failure) rather than degenerative/inflammatory injury.
- **Molecular profiling.** Honkala et al. performed molecular/cellular profiling of HLS fetuses, revealing "multiple changes in molecular and cellular level," including abnormal radial glial cells ([PMID: 19400947](https://pubmed.ncbi.nlm.nih.gov/19400947/)). No large transcriptomic/proteomic/metabolomic/single-cell datasets specific to HLS1 are established beyond fetal pathology.

**Cell types involved (CL suggestions):** radial glial cell (CL:0000681), neural progenitor/neuroepithelial cell (CL:0000031), ciliated cell (CL:0000064), spermatozoon/male germ cell (CL:0000019) — HYLS1 is also critical for spermatogenesis/flagella in *Drosophila* ([PMID: 32509774](https://pubmed.ncbi.nlm.nih.gov/32509774/)).

---

## 7. Anatomical Structures Affected

- **Primary organs / systems:** Central nervous system (brain — forebrain midline, cerebral cortex, hypothalamus; UBERON:0000955 brain, UBERON:0001890 forebrain), cranium/skull base (occiput), lungs (UBERON:0002048), limbs/autopod (hands and feet; UBERON:0002398, UBERON:0002387), craniofacial structures (mandible UBERON:0001684; palate UBERON:0001708).
- **Secondary involvement:** Genitourinary (abnormal genitalia; kidney size asymmetry reported in a case).
- **Tissue/cell level:** Neuroepithelium and radial glia (CNS), ciliated epithelia; connective/skeletal tissue (polydactyly, skull defects).
- **Subcellular level (GO Cellular Component):** **centriole (GO:0005814), centrosome (GO:0005813), ciliary basal body (GO:0036064), ciliary transition zone (GO:0035869), cilium (GO:0005929), axoneme (GO:0005930)**. HYLS1 protein localizes to the centriole/basal body; mutant protein mislocalizes to nuclear structures.
- **Localization / lateralization:** Malformations are predominantly **midline and bilateral** (midline brain defects, cleft lip/palate, occipitoschisis), with bilateral polydactyly.

---

## 8. Temporal Development

- **Onset:** **Congenital / prenatal** — malformations arise during embryogenesis and are detectable by first- and second-trimester ultrasound (as early as the 11th week in at-risk families; [PMID: 10210131](https://pubmed.ncbi.nlm.nih.gov/10210131/)).
- **Onset pattern:** Non-applicable in the acute/chronic sense; structural anomalies are present from organogenesis.
- **Progression / course:** The disorder does not "progress" post-natally because it is **perinatally lethal** — stillbirth or death within hours to days of birth. A rare "milder" case survived to seven months ([PMID: 10210131](https://pubmed.ncbi.nlm.nih.gov/10210131/)), attributed to allelic variability.
- **Duration:** Self-limited by lethality; not chronic.
- **Remission:** None. **Critical period:** the embryonic window of cilium-dependent midline/neural/limb patterning — the only "intervention window" is reproductive (preimplantation/prenatal).

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive.
- **Penetrance:** Complete (biallelic pathogenic genotype → disease).
- **Expressivity:** Largely consistent in Finnish D211G homozygotes; allelic variability can yield "milder"/atypical presentations ([PMID: 10210131](https://pubmed.ncbi.nlm.nih.gov/10210131/)).
- **Founder effect:** Strong — the Finnish D211G allele is an archetype of a Finnish-disease-heritage founder mutation (~27-fold enrichment in Finns; Finding F006), identified by Finnish linkage/LD mapping ([PMID: 15843405](https://pubmed.ncbi.nlm.nih.gov/15843405/)).
- **Consanguinity:** Increases recurrence risk for rare alleles outside Finland (standard for AR disorders).
- **Carrier / incidence estimates (derived, Finding F006):** Under Hardy–Weinberg, Finnish carrier frequency ≈ **1.70% (~1 in 59)**; predicted homozygous-affected incidence ≈ **7.3×10⁻⁵ (~1 in 13,600)** — the same order as the classically reported Finnish HLS incidence of ~1 in 20,000 births.
- **Geographic distribution:** Enriched in Finland; rare, sporadic cases reported elsewhere (France, Romania, Norway, non-Finnish families). D211G is concentrated in Finland; novel alleles reported in non-Finnish families.
- **Sex ratio:** No strong sex bias reported; abnormal genitalia noted in some fetuses.
- **Genetic anticipation / germline mosaicism:** Not applicable / not reported.

---

## 10. Diagnostics

- **Prenatal imaging:** Fetal ultrasound is the frontline tool — detects hydrocephaly/hydranencephaly, absent midline structures, polydactyly, and skull defects; diagnosis possible in the first trimester (≈11 weeks) in families with a prior affected fetus ([PMID: 10210131](https://pubmed.ncbi.nlm.nih.gov/10210131/)).
- **Fetal autopsy / pathology:** Confirms the pathognomonic occipitoschisis ("keyhole") skull-base defect, CNS midline defects, immature cortex, abnormal radial glia, hypothalamic hamartoma, defective lung lobation, and polydactyly ([PMID: 19400947](https://pubmed.ncbi.nlm.nih.gov/19400947/), [PMID: 22029171](https://pubmed.ncbi.nlm.nih.gov/22029171/), [PMID: 39857086](https://pubmed.ncbi.nlm.nih.gov/39857086/)).
- **Genetic testing (confirmatory):** Targeted testing for the Finnish D211G allele in Finnish/at-risk families; **single-gene HYLS1 sequencing**, **gene panels** (lethal fetal malformation / ciliopathy panels that include HYLS1), and **WES/WGS** for non-Finnish or atypical cases. Chromosomal microarray detects the 11q deletion. Maternal serum AFP may be elevated with open defects.
- **Biomarkers / lab tests:** No specific circulating biomarker; diagnosis is imaging + molecular.
- **Clinical criteria:** Recognized by the characteristic malformation triad (hydrocephaly/absent midline brain + polydactyly + the keyhole occipital defect) plus molecular confirmation.
- **Differential diagnosis:** Meckel(-Gruber) syndrome (occipital encephalocele, cystic kidneys, polydactyly; [PMID: 17389183](https://pubmed.ncbi.nlm.nih.gov/17389183/)), acrocallosal syndrome (possible allelic/overlapping midline + polydactyly phenotype; [PMID: 10756349](https://pubmed.ncbi.nlm.nih.gov/10756349/)), trisomy 13, Smith-Lemli-Opitz syndrome, Ellis-van Creveld syndrome ([PMID: 23276573](https://pubmed.ncbi.nlm.nih.gov/23276573/)), Joubert syndrome (HYLS1 is also a rare Joubert gene; [PMID: 36580738](https://pubmed.ncbi.nlm.nih.gov/36580738/)), Bardet-Biedl, and oral-facial-digital syndrome. The keyhole/occipitoschisis defect is the most discriminating feature favoring HLS.
- **Screening:** Carrier screening (especially in Finnish populations) and cascade testing of relatives; preimplantation and prenatal testing for at-risk couples.

---

## 11. Outcome / Prognosis

The prognosis is **uniformly fatal**. Affected fetuses are stillborn or die within hours to days after birth; a single atypical "milder" case survived to seven months ([PMID: 10210131](https://pubmed.ncbi.nlm.nih.gov/10210131/)). There is no survival benefit from any intervention. Mortality is 100% and disease-specific. Morbidity/quality-of-life and disability measures are not applicable to surviving patients; the principal measurable burden is reproductive loss and family bereavement. The mouse disease-mutation model dies "shortly after birth," mirroring the human lethality ([PMID: 40009365](https://pubmed.ncbi.nlm.nih.gov/40009365/)). **Prognostic factors:** genotype/allelic severity appears to modulate the rare atypical/"milder" survivors. No prognostic biomarkers exist.

---

## 12. Treatment

**There is no disease-modifying or curative treatment for HLS1.** Because the disorder is a prenatal, uniformly lethal malformation syndrome, care is limited to:

- **Supportive / palliative perinatal care** (NCIT: Palliative Care; comfort care for the neonate and family).
- **Genetic counseling** for recurrence risk and reproductive planning.
- **Pregnancy management**, including the option of termination following prenatal diagnosis per local practice.

No pharmacotherapy, gene therapy, cell therapy, RNA-based therapy, targeted therapy, immunotherapy, surgery, or rehabilitation alters the outcome. No clinical trials target HLS1. Pharmacogenomics and combination/personalized-medicine strategies are not applicable. *Not available for this disease.*

---

## 13. Prevention

Prevention is entirely **reproductive/genetic**, not clinical:

- **Primary prevention:** None for an established pregnancy. Pre-conception **carrier screening** (particularly for the Finnish D211G allele) identifies at-risk couples.
- **Secondary prevention / early detection:** **Prenatal ultrasound** (first-trimester feasible in at-risk families; [PMID: 10210131](https://pubmed.ncbi.nlm.nih.gov/10210131/)) and **prenatal molecular testing** (CVS/amniocentesis).
- **Preimplantation genetic testing (PGT-M):** Available for couples who are known carriers.
- **Genetic counseling:** Central — 25% recurrence risk per pregnancy for carrier couples; cascade testing of relatives.
- **Immunization / behavioral / public-health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

HYLS1 is **evolutionarily conserved** across metazoans. Confirmed orthologs (Finding F008):

| Species | Gene | NCBI GeneID |
|---|---|---|
| Human | HYLS1 | 219844 |
| Mouse (*Mus musculus*) | Hyls1 | 76832 |
| Rat (*Rattus norvegicus*) | Hyls1 | 680262 |
| *Caenorhabditis elegans* | hyls-1 | functional ortholog |
| *Drosophila melanogaster* | HYLS1 ortholog | functional ortholog |

No naturally occurring HLS-equivalent disease is catalogued in companion animals or wildlife (no OMIA entry noted), and the condition has no zoonotic or cross-species transmission relevance. Comparative biology is driven by experimental models rather than spontaneous animal disease. The deep conservation of HYLS1's centriole/cilia function (worm → fly → mouse → human) underpins the translatability of model findings ([PMID: 19656802](https://pubmed.ncbi.nlm.nih.gov/19656802/), [PMID: 27534274](https://pubmed.ncbi.nlm.nih.gov/27534274/), [PMID: 32509774](https://pubmed.ncbi.nlm.nih.gov/32509774/)).

---

## 15. Model Organisms

HLS1 is exceptionally well served by cross-species models, which collectively built the mechanistic chain:

| Model | Type | Key contribution | PMID |
|---|---|---|---|
| **Mouse** (HYLS1 disease-mutation knock-in) | Mammalian, genetic | Dies shortly after birth; recapitulates HLS defects; established CEP120 recruitment and centriole-integrity mechanism | [38496445](https://pubmed.ncbi.nlm.nih.gov/38496445/), [40009365](https://pubmed.ncbi.nlm.nih.gov/40009365/) |
| ***C. elegans*** (hyls-1) | Invertebrate, genetic | Defined HYLS-1 role in centriole structure, transition fibre/zone, ciliary gating, IFT docking | [19656802](https://pubmed.ncbi.nlm.nih.gov/19656802/), [27534274](https://pubmed.ncbi.nlm.nih.gov/27534274/) |
| ***Drosophila*** | Invertebrate, genetic | Confirmed mutation significance; ciliogenesis and spermatogenesis/flagella roles | [15843405](https://pubmed.ncbi.nlm.nih.gov/15843405/), [32509774](https://pubmed.ncbi.nlm.nih.gov/32509774/) |
| **Mammalian cell culture** | In vitro | PIPKIγ activation, PI(4)P depletion, NPHP/β-arrestin/GPR161–Hedgehog axis | [34162535](https://pubmed.ncbi.nlm.nih.gov/34162535/) |

**Phenotype recapitulation:** The mouse disease-mutation model reproduces several human HLS manifestations and dies perinatally, making it the best in vivo surrogate; the worm/fly models recapitulate the cellular ciliogenesis defect but not the organismal malformation pattern. **Limitations:** Invertebrate models cannot reproduce mammalian forebrain/midline morphogenesis; even the mouse may not capture the full human craniofacial/skull-base phenotype (tissue-specific cilia dependence). **Resources:** MGI (mouse Hyls1 76832), RGD (rat Hyls1 680262), WormBase (hyls-1), FlyBase.

---

## Mechanistic Model / Interpretation

The HLS1 literature now supports a **single, coherent, upstream-to-downstream mechanism** in which a point mutation in a centriole protein cascades into a signaling ciliopathy:

**Centriole integrity (CEP120–HYLS1) → ciliary gate (TF/TZ) → primary cilium → Hedgehog signaling → embryonic patterning.**

The two independent molecular branches discovered — (a) the **mouse CEP120/centriole-inner-scaffold** axis ([PMID: 38496445](https://pubmed.ncbi.nlm.nih.gov/38496445/)) and (b) the **mammalian PIPKIγ/PI(4)P/GPR161–Hedgehog** axis ([PMID: 34162535](https://pubmed.ncbi.nlm.nih.gov/34162535/)) — are complementary rather than contradictory: the first explains **why the cilium fails to assemble** (structural), the second explains **why cilium-dependent signaling fails even where cilia form** (functional/signaling). Both terminate in defective Hedgehog-dependent midline, neural, and limb patterning, which is a classic explanation for the HLS malformation triad (absent midline brain structures, polydactyly, craniofacial clefts). The tissue-specificity of centriole/cilia dependence plausibly accounts for the particular organs affected.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [15843405](https://pubmed.ncbi.nlm.nih.gov/15843405/) | *HLS caused by a missense mutation in a novel gene HYLS1* | Gene discovery; D211G; mutant mislocalization; *Drosophila* confirmation |
| [19656802](https://pubmed.ncbi.nlm.nih.gov/19656802/) | *HYLS-1 links core centriole structure to cilia formation* | Establishes ciliopathy; D211G impairs ciliogenesis; centriole anchoring |
| [27534274](https://pubmed.ncbi.nlm.nih.gov/27534274/) | *HYLS-1 regulates formation of the ciliary gate* | TF/TZ formation, ciliary gating, IFT docking |
| [19400947](https://pubmed.ncbi.nlm.nih.gov/19400947/) | *Unraveling the disease pathogenesis behind lethal HLS* | Core phenotype; CNS neuropathology; molecular/cellular profiling |
| [22029171](https://pubmed.ncbi.nlm.nih.gov/22029171/) | *Lethal evolution of a newborn with HLS — Romanian patient* | Occipitoschisis as pathognomonic; craniofacial/limb features |
| [34212369](https://pubmed.ncbi.nlm.nih.gov/34212369/) | *First two non-Finnish HYLS1 variants* | Novel alleles (R221P, R205\*); phenotype expansion |
| [38496445](https://pubmed.ncbi.nlm.nih.gov/38496445/) / [40009365](https://pubmed.ncbi.nlm.nih.gov/40009365/) | *Centriole structural integrity defects in HLS* | Mouse model; CEP120 recruitment; centriole-integrity mechanism |
| [34162535](https://pubmed.ncbi.nlm.nih.gov/34162535/) | *HYLS1 activates the ciliary lipid kinase PIPKIγ* | Lipid-kinase mechanism; GPR161/β-arrestin/Hedgehog |
| [32509774](https://pubmed.ncbi.nlm.nih.gov/32509774/) | *Functional analysis of HYLS1 in ciliogenesis and spermatogenesis* | Conserved function; germ-cell/flagella role |
| [10210131](https://pubmed.ncbi.nlm.nih.gov/10210131/) | *HLS in a non-Finnish family; early prenatal diagnosis* | Allelic variability; first-trimester ultrasound |
| [39857086](https://pubmed.ncbi.nlm.nih.gov/39857086/) | *Hydrolethalus Syndrome: a rare congenital disorder* | Keyhole defect, lung lobation, open-book hemispheres |
| [17389183](https://pubmed.ncbi.nlm.nih.gov/17389183/), [10756349](https://pubmed.ncbi.nlm.nih.gov/10756349/), [23276573](https://pubmed.ncbi.nlm.nih.gov/23276573/), [36580738](https://pubmed.ncbi.nlm.nih.gov/36580738/) | Differential diagnoses | Meckel, acrocallosal, Ellis-van Creveld, Joubert overlap |

**Evidence source mix:** human clinical/fetal-pathology (phenotype, diagnosis, epidemiology), model organism (mechanism: mouse, worm, fly), in vitro (PIPKIγ/Hedgehog), and computational (gnomAD allele-frequency/Hardy-Weinberg epidemiology).

---

## Limitations and Knowledge Gaps

- **Allelic spectrum is narrow.** The great majority of molecular evidence rests on the single Finnish D211G allele; generalizability to rare non-Finnish alleles (R221P, R205\*, CNVs) is only partially characterized.
- **Phenotype–genotype modifiers unknown.** The basis for rare "milder"/atypical survivors and for the HYLS1–Joubert phenotype is not resolved; no validated modifier genes or epigenetic mechanisms exist.
- **No human omics at scale.** There are no large transcriptomic, proteomic, or single-cell datasets specific to HLS1 fetuses; mechanism relies on model systems.
- **Branch integration incomplete.** The precise quantitative contribution of the centriole-integrity branch vs the PIPKIγ/Hedgehog branch to each specific malformation (brain vs limb vs lung) is not experimentally dissected.
- **No therapeutic avenue.** Lethality and prenatal onset mean no treatment pipeline exists.

## Proposed Follow-up Experiments / Actions

1. **Genotype–phenotype catalog:** Compile all reported HYLS1 alleles with precise fetal phenotypes to test whether null vs hypomorphic alleles predict HLS vs Joubert-spectrum outcomes.
2. **Conditional/tissue-specific mouse models:** Use the existing disease-mutation mouse to dissect tissue-specific cilia dependence (forebrain vs limb bud vs lung), clarifying which malformations are Hedgehog-driven.
3. **Single-cell / spatial transcriptomics of model embryos:** Map Hedgehog/GPR161 pathway dysregulation across developing midline, neural tube, and limb bud to connect molecular branches to specific defects.
4. **Structural biology of the HYLS1–CEP120 interface:** Determine how D211G, R221P, and R205\* differentially disrupt CEP120 binding and centriole localization (AlphaFold-guided, then validated).
5. **Carrier-screening and epidemiology refinement:** Validate the Hardy-Weinberg-derived Finnish incidence against registry data and extend gnomAD-based carrier estimates to non-Finnish populations for counseling.
6. **Prenatal diagnostic standardization:** Formalize first-trimester ultrasound + targeted HYLS1 panels (including the 11q deletion) as a diagnostic algorithm for suspected lethal midline ciliopathy.

---

*Report compiled from 8 confirmed findings and 21 reviewed papers over 5 investigation iterations. All mechanistic and clinical claims are attributed to primary literature by PMID; model-organism, in vitro, computational, and human-clinical evidence sources are distinguished throughout.*


## Artifacts

- [OpenScientist final report](Hydrolethalus_Syndrome_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hydrolethalus_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf)

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
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009365` (2 mentions) - the report calls it "MONDO"; MONDO calls it **hydrolethalus syndrome 1**
- `HP:0002538` (1 mention) - the report calls it "cortical malformation"; HP calls it **Abnormal cerebral cortex morphology**