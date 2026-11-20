---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T00:58:31.140267'
end_time: '2026-11-05T01:29:03.365229'
duration_seconds: 1832.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Heart Defects, Multiple Types, 7
  mondo_id: MONDO:0032913
  category: Mendelian
  causal_genes: FLT4
  omim_id: OMIM:618780
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
citation_count: 24
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 11
  off_topic: 2
  off_topic_references:
  - PMID:27443814
  - PMID:22745786
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 29
  verified: 26
  not_found: 2
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.071
  labels_checked: 12
  labels_matching: 7
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0010316
    reported_labels:
    - Absent pulmonary valve
    ontology_label: Ebstein anomaly of the tricuspid valve
  - term_id: CL:0002138
    reported_labels:
    - relevant to the Milroy branch
    ontology_label: endothelial cell of lymphatic vessel
  labels_variant: 3
  unresolved_terms:
  - HP:0001656
  - HP:0010449
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Heart_Defects_Multiple_Types_7-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Heart_Defects_Multiple_Types_7-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Heart Defects, Multiple Types, 7
- **MONDO ID:** MONDO:0032913 (if available)
- **Causal gene(s):** FLT4
- **OMIM:** OMIM:618780
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Heart Defects, Multiple Types, 7** covering all of the
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

# Congenital Heart Defects, Multiple Types, 7 (CHTD7) — Comprehensive Research Report

**Disease:** Congenital Heart Defects, Multiple Types, 7 (CHTD7)
**MONDO ID:** MONDO:0032913 · **OMIM:** 618780 · **Causal gene:** **FLT4** (VEGFR3)
**Category:** Mendelian (autosomal dominant, incompletely penetrant)

---

## Summary

**Congenital Heart Defects, Multiple Types, 7 (CHTD7; OMIM 618780, MONDO:0032913) is caused by rare, heterozygous, predominantly loss-of-function variants in *FLT4***, the gene encoding the vascular endothelial growth factor receptor 3 (VEGFR3), a receptor tyrosine kinase for VEGF-C and VEGF-D. Despite the serial-number disease name, the causal gene is unambiguously **FLT4** (HGNC:3767; chromosome 5q35.3). The dominant clinical phenotype is **Tetralogy of Fallot (TOF)** and related conotruncal/outflow-tract malformations, although FLT4 variants also produce a broader spectrum that includes some left-sided lesions. The condition is inherited in an autosomal dominant fashion with **incomplete penetrance and variable expressivity**, so that pathogenic alleles are frequently transmitted by parents with no or only subclinical cardiac findings. FLT4 also causes a phenotypically non-overlapping disorder, **Milroy disease** (primary hereditary lymphedema, OMIM 153100), via a different molecular mechanism — the two must not be conflated.

FLT4 is the **second most frequent (after *NOTCH1*) genome-wide-significant gene for nonsyndromic TOF**, and it is **strongly loss-of-function–intolerant** in the general population (gnomAD pLI = 1.0, LOEUF ≈ 0.25), which is the quantitative signature of a **haploinsufficiency** mechanism. Mechanistically, TOF-associated missense variants are distinguished from the lymphedema-causing (Milroy) variants of the same gene: TOF variants cause mutant FLT4 protein to **aggregate in the perinuclear endoplasmic reticulum and activate proteostatic/metabolic stress signalling** in endothelial cells, whereas Milroy-disease variants act by a **dominant-negative** mechanism that prevents the receptor from functioning as a homodimer. These two allelic series therefore cause two distinct human diseases from the same locus.

Clinically, CHTD7 is managed as structural congenital heart disease: the mainstay is **surgical repair of the cardiac lesion** (for TOF, VSD closure plus relief of right-ventricular outflow-tract obstruction). Long-term survival is excellent (~90% survive >30 years after repair), but late sequelae — chiefly **pulmonary regurgitation, right-ventricular volume overload, and atrial/ventricular arrhythmias** — are near-universal and require lifelong specialist follow-up and frequent reinterventions (most commonly pulmonary valve replacement). No FLT4-targeted pharmacotherapy or gene therapy exists; proteostasis modulation is only a preclinical lead. This report consolidates eight confirmed findings across 29 reviewed papers into a full disease-knowledge-base entry spanning etiology, phenotypes, molecular genetics, mechanism, anatomy, temporal course, epidemiology, diagnostics, prognosis, treatment, prevention, cross-species biology, and model organisms.

---

## Key Findings

### Finding 1 — FLT4 (VEGFR3) loss-of-function is a major cause of CHTD7, predominantly Tetralogy of Fallot

Reuter et al. genome-sequenced 175 adults with TOF and identified **9/175 (5.1%) probands with novel FLT4 variants: seven loss-of-function (including an 8-kb deletion) and two predicted-damaging** [PMID: 30232381](https://pubmed.ncbi.nlm.nih.gov/30232381/). Detection of VEGF-related variants more broadly (19/175, 10.9%) was associated with increased prevalence of **absent pulmonary valve (26.3% vs 3.4%, p<0.0001)** and **right aortic arch (52.6% vs 29.1%, p=0.029)**, linking the VEGF/VEGFR3 axis to specific anatomical sub-phenotypes. A clinically driven reanalysis of exome data from **811 TOF probands** confirmed FLT4 as a major contributor to TOF genetic risk [PMID: 34328347](https://pubmed.ncbi.nlm.nih.gov/34328347/). OMIM entry 618780 ("Congenital heart defects, multiple types, 7") is the formal label for FLT4-associated multiple congenital heart defects.

> *"We identified nine (5.1%) probands with novel FLT4 variants: seven loss-of-function, including an 8-kb deletion, and two predicted damaging."* — [PMID: 30232381](https://pubmed.ncbi.nlm.nih.gov/30232381/)
>
> *"Loss-of-function variants in FLT4 and KDR contribute substantially to the genetic basis of TOF."* — [PMID: 30232381](https://pubmed.ncbi.nlm.nih.gov/30232381/)

### Finding 2 — TOF-associated FLT4 variants act through a proteostatic/ER-aggregation mechanism distinct from Milroy disease

Monaghan et al. showed that **FLT4 TOF variants expressed in primary human endothelial cells cause aggregation of FLT4 protein in the perinuclear endoplasmic reticulum**, activating proteostatic and metabolic signalling, whereas lymphedema (Milroy) variants and wild-type FLT4 do not [PMID: 38713105](https://pubmed.ncbi.nlm.nih.gov/38713105/). Functionally, *flt4* depletion in zebrafish caused **reduced heart size and altered heart looping**, which was rescued by wild-type human *FLT4* mRNA but incompletely or not at all by TOF-variant mRNA; inhibition of proteostatic signalling abrogated the deleterious effects. By contrast, the Milroy-causing variants act by **preventing the receptor from functioning as a homodimer** (a dominant-negative mechanism) [PMID: 33067626](https://pubmed.ncbi.nlm.nih.gov/33067626/). This establishes that the same gene produces two distinct diseases through two distinct allelic mechanisms.

> *"FLT4 variants identified in patients with TOF, when expressed in primary human endothelial cells, cause aggregation of FLT4 protein in the perinuclear endoplasmic reticulum, activating proteostatic and metabolic signalling, whereas lymphoedema-associated FLT4 variants and wild-type (WT) FLT4 do not"* — [PMID: 38713105](https://pubmed.ncbi.nlm.nih.gov/38713105/)
>
> *"we identify a pathogenic mechanism for FLT4 variants predisposing to TOF that is distinct from the known dominant negative mechanism of Milroy-causative variants"* — [PMID: 38713105](https://pubmed.ncbi.nlm.nih.gov/38713105/)

### Finding 3 — Autosomal dominant with incomplete penetrance; excellent surgical prognosis but progressive late sequelae

FLT4 variants cause **isolated left- and right-sided CHD with incomplete penetrance**, transmitted from parents with no or subclinical heart phenotypes [PMID: 39870876](https://pubmed.ncbi.nlm.nih.gov/39870876/); [PMID: 32037394](https://pubmed.ncbi.nlm.nih.gov/32037394/). At the phenotype level, **~90% of TOF patients survive >30 years after repair**; nearly all develop right-ventricular volume overload from pulmonary regurgitation, and atrial tachycardia/fibrillation occurs in **~20–45% by age 45** [PMID: 42258347](https://pubmed.ncbi.nlm.nih.gov/42258347/). Reinterventions — chiefly pulmonary valve replacement — occur in **~41–52%** of long-term cohorts [PMID: 42894905](https://pubmed.ncbi.nlm.nih.gov/42894905/). TOF prevalence is ~3/10,000 live births, representing 5–10% of all CHD [PMID: 36277185](https://pubmed.ncbi.nlm.nih.gov/36277185/).

> *"our study establishes FLT4 splice site variants as a molecular cause of both left and right-sided isolated CHD, with incomplete penetrance"* — [PMID: 39870876](https://pubmed.ncbi.nlm.nih.gov/39870876/)
>
> *"Ninety percent of patients with TOF survive more than 30 years after surgery to close the ventricular septal defect and repair the right ventricular outflow tract."* — [PMID: 42258347](https://pubmed.ncbi.nlm.nih.gov/42258347/)
>
> *"Nearly all adults with repaired TOF develop right ventricular volume overload due to pulmonary regurgitation, and atrial tachycardias and atrial fibrillation occur in approximately 20% to 45% of patients by age 45 years."* — [PMID: 42258347](https://pubmed.ncbi.nlm.nih.gov/42258347/)

### Finding 4 — FLT4 is a genome-wide-significant TOF gene and strongly LoF-intolerant, supporting haploinsufficiency

Page et al. whole-exome-sequenced **829 nonsyndromic TOF patients**; clustering of unique deleterious variants in *NOTCH1* and *FLT4* **surpassed genome-wide significance (P < 5×10⁻⁸)**, with NOTCH1 the most frequent locus followed by FLT4, and together these two genes account for **almost 7% of TOF** [PMID: 30582441](https://pubmed.ncbi.nlm.nih.gov/30582441/). gnomAD constraint metrics for FLT4 (ENSG00000037280, chr5:180,601,506–180,649,624) are **pLI = 1.0, LOEUF (oe_lof_upper) = 0.249, observed/expected LoF = 0.184 (30 observed vs 163.2 expected), LoF Z = 8.85** — indicating strong depletion of LoF variants in the general population and consistent with haploinsufficiency; the gene is also missense-constrained (mis_z = 3.50). A large study of **11,555 CHD probands** found 60 dominant CHD genes accounting for 10.1% of probands with incomplete penetrance [PMID: 40127276](https://pubmed.ncbi.nlm.nih.gov/40127276/).

> *"The clustering of variants in 2 genes, NOTCH1 and FLT4, surpassed thresholds for genome-wide significance"* — [PMID: 30582441](https://pubmed.ncbi.nlm.nih.gov/30582441/)
>
> *"The NOTCH1 locus is the most frequent site of genetic variants predisposing to nonsyndromic TOF, followed by FLT4. Together, variants in these genes are found in almost 7% of TOF patients."* — [PMID: 30582441](https://pubmed.ncbi.nlm.nih.gov/30582441/)
>
> *"Variants in these genes accounted for CHD in 10.1% of probands with similar contributions from de novo and transmitted variants in parent-offspring trios that showed incomplete penetrance."* — [PMID: 40127276](https://pubmed.ncbi.nlm.nih.gov/40127276/)

### Finding 5 — ClinVar variant spectrum: ~50 variants linked to CHTD7, large VUS fraction, SNVs and copy-number losses

ClinVar lists **741 total FLT4 variant records** (181 Pathogenic, 52 Likely pathogenic, 623 Uncertain significance). By condition, **50 FLT4 variants are annotated to "Congenital heart defects, multiple types, 7"**, 17 to Fallot-related terms, and 76 to Milroy disease. By variant type: **639 single-nucleotide variants, 30 deletions, and 12 copy-number losses** — consistent with a loss-of-function spectrum (nonsense/frameshift/splice/SNVs plus intragenic and larger deletions, including the reported 8-kb deletion). The large VUS burden is a key interpretive challenge for the clinical lab.

### Finding 6 — Model organisms: zebrafish *flt4* recapitulates the cardiac branch; the Chy mouse models the lymphatic (Milroy) branch

Zebrafish *flt4* depletion causes reduced heart size and altered looping, rescued by wild-type but not TOF-variant human *FLT4* mRNA [PMID: 38713105](https://pubmed.ncbi.nlm.nih.gov/38713105/) — the most CHTD7-relevant functional model. In mouse, the germline heterozygous Vegfr3-inactivating **Chy** mutant shows limb swelling from hypoplastic cutaneous (not visceral) lymphatics, modeling Milroy disease, and is rescued by VEGF-C gene therapy [PMID: 11592985](https://pubmed.ncbi.nlm.nih.gov/11592985/). Homozygous *Flt4*-null is embryonic lethal with cardiovascular failure (reviewed in [PMID: 33067626](https://pubmed.ncbi.nlm.nih.gov/33067626/)).

> *"the lymphedema (Chy) mice have an inactivating Vegfr3 mutation in their germ line, and swelling of the limbs because of hypoplastic cutaneous, but not visceral, lymphatic vessels"* — [PMID: 11592985](https://pubmed.ncbi.nlm.nih.gov/11592985/)
>
> *"By using virus-mediated VEGF-C gene therapy, we were able to generate functional lymphatic vessels in the lymphedema mice."* — [PMID: 11592985](https://pubmed.ncbi.nlm.nih.gov/11592985/)

### Finding 7 — Environmental risk/protective factors for CHD (general, not FLT4-specific)

Although CHTD7 is a Mendelian disease, incomplete penetrance implies modifier effects. For CHD broadly, **maternal pregestational diabetes is a strong risk factor (adjusted OR 4.04, 95% CI 1.00–16.28)** [PMID: 32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/), as are low maternal education and maternal infections. **Periconceptional folic acid supplementation is modestly protective (OR 0.82, 95% CI 0.68–0.98)** [PMID: 19952004](https://pubmed.ncbi.nlm.nih.gov/19952004/), and diets rich in folate/fruit/vegetables are protective (folate-rich fruit adjOR 0.64, 95% CI 0.47–0.89 [PMID: 32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/); Mediterranean/antioxidant diets protective [PMID: 34392783](https://pubmed.ncbi.nlm.nih.gov/34392783/)). **No FLT4-specific gene–environment interaction has been demonstrated for CHTD7.**

> *"Risk of CHD was associated with low maternal education (OR adjusted for confounders 1.59; 95% confidence interval [CI], 1.02-2.49), pregestational diabetes (OR 4.04; 95% CI 1.00-16.28)"* — [PMID: 32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/)
>
> *"Periconceptional folic acid use revealed an odds ratio (OR) of 0.82 (95% CI 0.68-0.98) for all types of CHD relative to other malformations."* — [PMID: 19952004](https://pubmed.ncbi.nlm.nih.gov/19952004/)

### Finding 8 — Consolidated characterization

Across all findings: FLT4/VEGFR3 LoF is a genome-wide-significant cause of TOF (2nd after NOTCH1, ~7% combined); FLT4 is strongly LoF-intolerant (haploinsufficiency); TOF variants act via perinuclear-ER aggregation/proteostatic stress, distinct from the dominant-negative kinase-dead Milroy variants; inheritance is autosomal dominant with incomplete penetrance and variable expressivity; the variant spectrum is allelically heterogeneous (SNVs + CNVs, large VUS burden); zebrafish models the cardiac branch and the Chy mouse the lymphatic branch; and management is surgical with progressive late pulmonary regurgitation/arrhythmia and no targeted drug or gene therapy.

---

## Section-by-Section Report

### 1. Disease Information

CHTD7 is a Mendelian predisposition to structural congenital heart disease, chiefly **Tetralogy of Fallot** and related conotruncal/right-ventricular-outflow-tract defects, with a minority of left-sided lesions. Key identifiers: **OMIM 618780**, **MONDO:0032913**, causal gene **FLT4** (HGNC:3767; NCBI Gene 2324; Ensembl ENSG00000037280). There is no single dedicated Orphanet/ICD code for the "multiple types 7" serial entry; clinically, cases map to TOF (ICD-11 LA88.0; ICD-10 Q21.3) and other CHD codes, and to MeSH "Tetralogy of Fallot" (D013771) and "Heart Defects, Congenital" (D006330). Synonyms are **not formally recorded** beyond the OMIM designation; in the literature the entity is referred to as "FLT4-associated congenital heart disease" or "FLT4/VEGFR3 TOF." The information is derived predominantly from **aggregated disease-level resources and research cohorts** (exome/genome sequencing studies, ClinVar, gnomAD), not from individual-patient EHR data.

### 2. Etiology

**Causal factor:** genetic — rare, heterozygous, predominantly **loss-of-function** variants in *FLT4* (Findings 1, 4). **Genetic risk:** FLT4 is a genome-wide-significant TOF gene (Finding 4); *NOTCH1* is the leading locus, with other VEGF-pathway genes (e.g., *KDR*/VEGFR2) also contributing [PMID: 30582441](https://pubmed.ncbi.nlm.nih.gov/30582441/), [PMID: 30232381](https://pubmed.ncbi.nlm.nih.gov/30232381/). **Environmental risk (CHD generally, not FLT4-specific):** maternal pregestational diabetes (adjOR 4.04), low maternal education, maternal infection, periconceptional secondhand smoke (associated with septal defects) [PMID: 32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/), [PMID: 27443814](https://pubmed.ncbi.nlm.nih.gov/27443814/). **Protective factors:** periconceptional folic acid (OR 0.82) and folate/antioxidant-rich diets [PMID: 19952004](https://pubmed.ncbi.nlm.nih.gov/19952004/), [PMID: 34392783](https://pubmed.ncbi.nlm.nih.gov/34392783/). **Gene–environment interaction:** plausibly contributes to incomplete penetrance, but **no FLT4-specific GxE interaction has been demonstrated** (Finding 7).

### 3. Phenotypes

The core phenotype is **Tetralogy of Fallot** (HP:0001636), defined by ventricular septal defect (HP:0001629), pulmonary/RVOT stenosis (HP:0001642 / HP:0001656), overriding aorta (HP:0002623), and right ventricular hypertrophy (HP:0001667) [PMID: 36277185](https://pubmed.ncbi.nlm.nih.gov/36277185/). VEGF-pathway variant carriers show enrichment of **absent pulmonary valve** (HP:0010316; 26.3% vs 3.4%, p<0.0001) and **right aortic arch** (HP:0012020; 52.6% vs 29.1%, p=0.029) [PMID: 30232381](https://pubmed.ncbi.nlm.nih.gov/30232381/). The broader FLT4 spectrum includes other right- and left-sided isolated CHD [PMID: 39870876](https://pubmed.ncbi.nlm.nih.gov/39870876/). These are structural/physical manifestations with **congenital (neonatal) onset**, **variable severity**, and **progressive late sequelae** after repair (RV volume overload, arrhythmia). Quality-of-life impact is driven by surgical burden, exercise limitation, reintervention and arrhythmia risk across the lifespan [PMID: 42258347](https://pubmed.ncbi.nlm.nih.gov/42258347/).

| Phenotype | HPO term | Type | Frequency / note |
|---|---|---|---|
| Tetralogy of Fallot | HP:0001636 | Structural | Predominant lesion |
| Ventricular septal defect | HP:0001629 | Structural | Component of TOF |
| Pulmonary valve stenosis | HP:0001642 | Structural | Component of TOF |
| Overriding aorta | HP:0002623 | Structural | Component of TOF |
| Right ventricular hypertrophy | HP:0001667 | Structural | Component of TOF |
| Absent pulmonary valve | HP:0010316 | Structural | Enriched in VEGF-variant carriers (26.3%) |
| Right aortic arch | HP:0012020 | Structural | Enriched in VEGF-variant carriers (52.6%) |
| Pulmonary regurgitation (post-repair) | HP:0010449 | Physiological | Near-universal late |
| Atrial fibrillation / tachyarrhythmia | HP:0005110 / HP:0011675 | Electrophysiological | ~20–45% by age 45 |

### 4. Genetic / Molecular Information

**Causal gene:** FLT4 / VEGFR3 (OMIM *136352). **Variant classes:** nonsense, frameshift, splice-site, missense, and structural deletions (intragenic and larger, including an 8-kb deletion) [PMID: 30232381](https://pubmed.ncbi.nlm.nih.gov/30232381/), [PMID: 39870876](https://pubmed.ncbi.nlm.nih.gov/39870876/). **ClinVar:** 741 FLT4 records total; **50 annotated to CHTD7**, with 181 Pathogenic/52 Likely pathogenic/623 VUS overall; 639 SNVs, 30 deletions, 12 copy-number losses (Finding 5). **Allele frequency:** pathogenic alleles are rare/absent in gnomAD; the gene is strongly LoF-intolerant (pLI=1.0, LOEUF=0.249) (Finding 4). **Origin:** germline; both **de novo and transmitted** alleles contribute [PMID: 40127276](https://pubmed.ncbi.nlm.nih.gov/40127276/). **Functional consequence:** **loss of function / haploinsufficiency** for null alleles; for TOF missense alleles, a **proteostatic gain-of-toxicity via ER aggregation** (distinct from dominant-negative Milroy alleles) (Finding 2). **Modifier genes:** other VEGF-pathway genes (NOTCH1, KDR) co-occur in TOF cohorts; formal modifier mapping for penetrance is lacking. **Epigenetics/large chromosomal abnormalities:** not specifically established for CHTD7 beyond the intragenic/larger deletions noted.

### 5. Environmental Information

No FLT4-specific environmental trigger is established. For CHD generally: environmental factors include maternal pregestational diabetes, maternal infection, and periconceptional secondhand smoke (septal defects) [PMID: 32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/), [PMID: 27443814](https://pubmed.ncbi.nlm.nih.gov/27443814/); lifestyle factors include diet quality (protective Mediterranean/folate-rich patterns) [PMID: 34392783](https://pubmed.ncbi.nlm.nih.gov/34392783/). **Infectious agents:** not applicable as a primary cause.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A rare heterozygous **FLT4 variant** (LoF: nonsense/frameshift/splice/deletion; or damaging missense) arises de novo or is transmitted → **reduces functional VEGFR3 receptor dosage** (haploinsufficiency). *(Demonstrated: gnomAD constraint; cohort LoF enrichment.)*
2. **Branch A (null/LoF alleles):** reduced VEGFR3 → **diminished VEGF-C/VEGF-D → VEGFR3 signalling** through downstream **PI3K/AKT and MEK/ERK** cascades in endothelial cells → impaired endothelial proliferation/migration during cardiac morphogenesis. *(Downstream signalling inferred from VEGFR3 biology: [PMID: 22745786](https://pubmed.ncbi.nlm.nih.gov/22745786/), [PMID: 33067626](https://pubmed.ncbi.nlm.nih.gov/33067626/).)*
3. **Branch B (TOF missense alleles):** mutant receptor **misfolds and aggregates in the perinuclear endoplasmic reticulum** → **activates proteostatic and metabolic stress signalling** → endothelial dysfunction; this is a toxic/ER-stress mechanism additional to simple dosage loss. *(Demonstrated in primary human endothelial cells: [PMID: 38713105](https://pubmed.ncbi.nlm.nih.gov/38713105/).)*
4. Both branches → **perturbed VEGFR3-dependent signalling during cardiac outflow-tract / second-heart-field morphogenesis** → **altered heart size and looping** (shown by zebrafish *flt4* depletion, rescued by WT but not TOF-variant mRNA) → maldevelopment of the right-ventricular outflow tract, pulmonary valve, and great-vessel/arch structures. *(Demonstrated: zebrafish, [PMID: 38713105](https://pubmed.ncbi.nlm.nih.gov/38713105/).)*
5. → **Structural congenital heart defect at birth** (Tetralogy of Fallot; absent pulmonary valve; right aortic arch; other conotruncal/left-sided lesions). *(Demonstrated: human cohorts.)*
6. → After surgical repair, chronic **pulmonary regurgitation → RV volume overload → RV dilation → atrial/ventricular arrhythmia** across adulthood. *(Demonstrated: natural-history cohorts, [PMID: 42258347](https://pubmed.ncbi.nlm.nih.gov/42258347/).)*

**Contrast with Milroy disease (same gene, different mechanism):** Milroy-causing FLT4 missense variants **prevent the receptor from functioning as a homodimer** (dominant-negative), impairing lymphatic rather than cardiac endothelium and producing congenital lymphedema [PMID: 33067626](https://pubmed.ncbi.nlm.nih.gov/33067626/), [PMID: 38201272](https://pubmed.ncbi.nlm.nih.gov/38201272/).

```
 FLT4 variant
   │
   ├─(null/LoF)──► ↓VEGFR3 dosage ─┐
   │                               ├─► ↓VEGF-C/VEGFR3 → PI3K/AKT & MEK/ERK
   ├─(TOF missense)► ER aggregation │     signalling in endothelium
   │                 + proteostatic │
   │                 stress ────────┘
   │                                       │
   │                                       ▼
   │                      perturbed outflow-tract morphogenesis
   │                      (altered heart size/looping — zebrafish)
   │                                       │
   │                                       ▼
   │                        Tetralogy of Fallot / conotruncal CHD
   │                                       │ (surgical repair)
   │                                       ▼
   └───────────► pulmonary regurgitation → RV overload → arrhythmia

 (separate allelic series):
 FLT4 missense (Milroy) ─► dominant-negative, no homodimer ─► lymphedema
```

**Pathways/GO/CL terms:** VEGF/VEGFR3 signalling (KEGG hsa04370; Reactome VEGF signalling); GO:0001525 angiogenesis, GO:0001946 lymphangiogenesis, GO:0003007 heart morphogenesis, GO:0003151 outflow tract morphogenesis, GO:0034976 response to ER stress, GO:0048010 VEGFR signalling pathway. **Cell types (CL):** endothelial cell (CL:0000115), cardiac/endocardial endothelial cell (CL:0010008), lymphatic endothelial cell (CL:0002138 — relevant to the Milroy branch). **Subcellular (GO CC):** endoplasmic reticulum (GO:0005783), plasma-membrane receptor complex.

### 7. Anatomical Structures Affected

**Primary organ:** heart (UBERON:0000948), specifically the **right ventricular outflow tract** (UBERON:0004145), **pulmonary valve** (UBERON:0002146), **interventricular septum** (UBERON:0002094), and **aorta/aortic arch** (UBERON:0000947 / UBERON:0005805). **Body system:** cardiovascular (and, via VEGFR3's canonical role, the lymphovascular system in the allelic Milroy phenotype). **Secondary involvement:** right ventricle (dilation/overload), right atrium (arrhythmia substrate), pulmonary arteries (including MAPCAs in severe TOF variants [PMID: 41957907](https://pubmed.ncbi.nlm.nih.gov/41957907/)). **Tissue/cell level:** vascular/endocardial **endothelium** (CL:0000115), cardiac neural-crest/second-heart-field derivatives of the outflow tract. **Lateralization:** right aortic arch reflects a laterality shift; lesions are structural and typically central/midline.

### 8. Temporal Development

**Onset:** congenital — the structural defect is present at birth and typically detected prenatally or in the neonatal/infant period. **Progression:** the primary lesion is static once formed, but the **post-repair course is progressive**: chronic pulmonary regurgitation leads to RV volume overload and dilation over years to decades, with rising arrhythmia burden by mid-adulthood (atrial tachyarrhythmia/AF ~20–45% by age 45) [PMID: 42258347](https://pubmed.ncbi.nlm.nih.gov/42258347/). **Critical period:** cardiac outflow-tract morphogenesis in early embryogenesis is the window of vulnerability; the intervention window is surgical repair in infancy/early childhood. **Duration:** chronic/lifelong, requiring lifelong ACHD follow-up and periodic reintervention [PMID: 42894905](https://pubmed.ncbi.nlm.nih.gov/42894905/).

### 9. Inheritance and Population

**Inheritance:** autosomal dominant, **incomplete penetrance**, **variable expressivity**; both de novo and transmitted alleles, with transmitting parents often unaffected or subclinically affected [PMID: 39870876](https://pubmed.ncbi.nlm.nih.gov/39870876/), [PMID: 32037394](https://pubmed.ncbi.nlm.nih.gov/32037394/), [PMID: 40127276](https://pubmed.ncbi.nlm.nih.gov/40127276/). **Epidemiology (phenotype-level):** TOF prevalence ~3/10,000 live births, 5–10% of all CHD [PMID: 36277185](https://pubmed.ncbi.nlm.nih.gov/36277185/); FLT4 variants explain ~5% of TOF probands [PMID: 30232381](https://pubmed.ncbi.nlm.nih.gov/30232381/) and, with NOTCH1, ~7% of nonsyndromic TOF [PMID: 30582441](https://pubmed.ncbi.nlm.nih.gov/30582441/). **Penetrance/anticipation/mosaicism/founder/consanguinity:** incomplete penetrance established; no anticipation (not a repeat-expansion disorder); germline mosaicism not specifically quantified; no founder effect described for CHTD7; consanguinity is not a feature of this dominant entity (note: a rare *recessive* FLT4 lymphedema allele exists [PMID: 26091405](https://pubmed.ncbi.nlm.nih.gov/26091405/), separate from CHTD7). **Sex ratio/geography:** no strong sex skew or geographic clustering documented for FLT4-CHD specifically.

### 10. Diagnostics

**Imaging:** transthoracic **echocardiography** is the primary diagnostic; cardiac MRI quantifies RV volumes and pulmonary regurgitation; CT/angiography defines pulmonary arteries/MAPCAs/arch anatomy [PMID: 41957907](https://pubmed.ncbi.nlm.nih.gov/41957907/). **Electrophysiology:** ECG/Holter for arrhythmia surveillance [PMID: 42403553](https://pubmed.ncbi.nlm.nih.gov/42403553/). **Genetic testing:** given locus heterogeneity, **genome or exome sequencing / multigene CHD panels** (including FLT4, NOTCH1, KDR) are the recommended approach; genome sequencing is anticipated to become a first-tier test [PMID: 32037394](https://pubmed.ncbi.nlm.nih.gov/32037394/). Single-gene FLT4 testing and chromosomal microarray/CNV analysis are useful given the deletion/CNV spectrum (Finding 5). RNA-sequencing can resolve splice-site variants of uncertain significance [PMID: 39870876](https://pubmed.ncbi.nlm.nih.gov/39870876/). **Clinical criteria/differential:** TOF is defined anatomically; differential diagnosis includes 22q11.2 deletion (DiGeorge/syndromic TOF), Alagille (JAG1/NOTCH2), and other conotruncal syndromes. The large **VUS burden** (623/741 FLT4 records) complicates interpretation (Finding 5). **Screening:** fetal echocardiography; cascade genetic testing of relatives given AD inheritance.

### 11. Outcome / Prognosis

**Survival:** excellent — **~90% of TOF patients survive >30 years after repair** [PMID: 42258347](https://pubmed.ncbi.nlm.nih.gov/42258347/); contemporary adult cohorts report long-term mortality as low as ~3.6% [PMID: 42894905](https://pubmed.ncbi.nlm.nih.gov/42894905/), though late-presenting/low-resource settings have higher operative mortality (~11.6%) [PMID: 42277928](https://pubmed.ncbi.nlm.nih.gov/42277928/). **Morbidity:** near-universal pulmonary regurgitation → RV volume overload; reintervention (chiefly pulmonary valve replacement) in **~41–52%** [PMID: 42894905](https://pubmed.ncbi.nlm.nih.gov/42894905/); atrial and ventricular arrhythmias are major late morbidities and sudden-death risks [PMID: 42403553](https://pubmed.ncbi.nlm.nih.gov/42403553/). **Prognostic factors:** anatomic subtype (e.g., TOF with MAPCAs/absent pulmonary valve), age at repair, RV size/function, and arrhythmia burden. **Quality-of-life:** reduced by exercise limitation, reinterventions, and arrhythmia; lifelong ACHD follow-up is required.

### 12. Treatment

**Mainstay — surgery (NCIT: Cardiac Surgical Procedure):** complete TOF repair (VSD closure + RVOT relief/transannular patch or homograft), typically in infancy [PMID: 42258347](https://pubmed.ncbi.nlm.nih.gov/42258347/), [PMID: 42894905](https://pubmed.ncbi.nlm.nih.gov/42894905/). Severe anatomy (MAPCAs, ductal-origin PA) is managed with staged unifocalization/ductal stenting then repair [PMID: 41957907](https://pubmed.ncbi.nlm.nih.gov/41957907/). **Late reinterventions:** pulmonary valve replacement — surgical (including minimally invasive left anterior thoracotomy) or transcatheter [PMID: 42875919](https://pubmed.ncbi.nlm.nih.gov/42875919/). **Arrhythmia management:** catheter ablation (including pulsed-field for AF), substrate-guided VT ablation, conduction-system pacing, and selective ICD/subcutaneous/leadless devices [PMID: 42403553](https://pubmed.ncbi.nlm.nih.gov/42403553/). **Advanced/targeted therapy:** **none FLT4-specific exists**; VEGF-C gene therapy rescues the lymphatic phenotype in the Chy mouse [PMID: 11592985](https://pubmed.ncbi.nlm.nih.gov/11592985/) but is not applicable to the cardiac branch, and **proteostasis modulation** is only a preclinical lead from the ER-aggregation mechanism [PMID: 38713105](https://pubmed.ncbi.nlm.nih.gov/38713105/). **Pharmacogenomics:** not established. **Supportive care:** heart-failure and arrhythmia medical therapy, exercise counselling, nutrition support for late-presenting underweight patients [PMID: 42277928](https://pubmed.ncbi.nlm.nih.gov/42277928/).

### 13. Prevention

**Primary prevention** of the Mendelian defect is not possible, but maternal periconceptional **folic acid** (OR 0.82) and folate/antioxidant-rich diets reduce CHD risk generally [PMID: 19952004](https://pubmed.ncbi.nlm.nih.gov/19952004/), [PMID: 34392783](https://pubmed.ncbi.nlm.nih.gov/34392783/), and control of maternal pregestational diabetes addresses a strong modifiable risk factor [PMID: 32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/). **Secondary prevention:** fetal/neonatal echocardiographic screening and cascade genetic testing of first-degree relatives (given AD inheritance with incomplete penetrance). **Tertiary prevention:** lifelong ACHD surveillance to detect and treat progressive pulmonary regurgitation, RV dilation, and arrhythmia before decompensation [PMID: 42894905](https://pubmed.ncbi.nlm.nih.gov/42894905/). **Genetic counselling:** essential — an affected individual has ~50% transmission risk per pregnancy, but penetrance is incomplete so phenotype prediction is limited. Prenatal/preimplantation genetic testing is available for known familial variants.

### 14. Other Species / Natural Disease

**Orthologs:** mouse *Flt4* (NCBI Gene 14257), zebrafish *flt4* (NCBI Gene 30375). VEGFR3 is evolutionarily conserved across vertebrates [PMID: 33067626](https://pubmed.ncbi.nlm.nih.gov/33067626/). **Natural disease:** no well-characterized spontaneous companion-animal FLT4-CHD counterpart is documented (OMIA entries for this specific gene–CHD association are not established); the comparative value is experimental rather than veterinary. **Conservation:** the VEGF-C/VEGFR3 axis and its role in cardiovascular and lymphovascular development are conserved, underpinning the utility of zebrafish and mouse models.

### 15. Model Organisms

**Zebrafish (cardiac branch, most CHTD7-relevant):** *flt4* depletion → reduced heart size and altered looping, rescued by WT human *FLT4* mRNA but not by TOF-variant mRNA; proteostasis inhibition abrogates the defect [PMID: 38713105](https://pubmed.ncbi.nlm.nih.gov/38713105/). Zebrafish also reveal Sox18–VegfC genetic interaction in lymphangiogenesis [PMID: 23520166](https://pubmed.ncbi.nlm.nih.gov/23520166/). **Mouse:** germline heterozygous Vegfr3-inactivating **Chy** mutant models the **lymphatic (Milroy) branch** (hypoplastic cutaneous lymphatics; rescued by VEGF-C gene therapy) [PMID: 11592985](https://pubmed.ncbi.nlm.nih.gov/11592985/); homozygous *Flt4*-null is embryonic lethal with cardiovascular failure [PMID: 33067626](https://pubmed.ncbi.nlm.nih.gov/33067626/). **In vitro:** primary human endothelial cells expressing TOF variants recapitulate the ER-aggregation/proteostatic mechanism [PMID: 38713105](https://pubmed.ncbi.nlm.nih.gov/38713105/). **Limitation:** no mouse model cleanly reproduces the human TOF cardiac phenotype from heterozygous FLT4 loss; the cardiac phenotype is best captured in zebrafish, while the mouse captures the lymphatic allelic series. **Resources:** ZFIN, MGI, IMPC.

---

## Mechanistic Model / Interpretation

CHTD7 is best understood as a **dosage-sensitive endothelial signalling disorder of cardiac outflow-tract development**. Two complementary lines of quantitative evidence anchor a **haploinsufficiency** model: FLT4 is the second genome-wide-significant nonsyndromic-TOF gene after NOTCH1 (cohort-level enrichment of rare deleterious alleles, P < 5×10⁻⁸), and it is among the most loss-of-function-intolerant genes in the human genome (gnomAD pLI = 1.0, LOEUF = 0.249, only 30 of 163 expected LoF alleles observed). Together these establish that a **~50% reduction in VEGFR3 activity is developmentally non-neutral** for the heart.

Layered on top of simple dosage loss is a **variant-class-specific toxic mechanism**: TOF missense alleles cause mutant receptor to aggregate in the perinuclear ER and trigger proteostatic/metabolic stress in endothelial cells — a mechanism demonstrated in primary human endothelial cells and functionally validated in zebrafish, and one that is **mechanistically separable from the dominant-negative, homodimer-blocking missense alleles that cause Milroy lymphedema**. This elegant allelic dichotomy — same gene, two diseases, two mechanisms, two target endothelia (cardiac vs lymphatic) — is the central conceptual insight of this entry and explains why CHTD7 and Milroy disease, though allelic, are phenotypically distinct and rarely co-segregate.

| Feature | CHTD7 (FLT4-TOF) | Milroy disease (allelic) |
|---|---|---|
| Phenotype | Tetralogy of Fallot / conotruncal CHD | Congenital lymphedema |
| Target endothelium | Cardiac/vascular | Lymphatic |
| Dominant variant class | LoF + damaging missense | Missense (kinase-affecting) |
| Mechanism | Haploinsufficiency + ER aggregation/proteostatic stress | Dominant-negative (no homodimer) |
| Best model | Zebrafish *flt4* | Chy mouse |
| Inheritance | AD, incomplete penetrance | AD |

The **incomplete penetrance** that pervades FLT4-CHD (transmission from unaffected/subclinical parents; 10.1% of a 11,555-proband CHD cohort explained by dominant genes with incomplete penetrance) implies the existence of genetic modifiers and/or environmental contributors. While general-CHD environmental factors (maternal diabetes risk; folate protection) are well quantified, **no FLT4-specific gene–environment interaction has yet been demonstrated** — a clear knowledge gap.

---

## Evidence Base

| PMID | Role in this report |
|---|---|
| [30232381](https://pubmed.ncbi.nlm.nih.gov/30232381/) | Core: 5.1% of TOF probands carry FLT4 variants (7 LoF incl. 8-kb deletion); absent pulmonary valve & right arch enrichment |
| [30582441](https://pubmed.ncbi.nlm.nih.gov/30582441/) | Core: FLT4 genome-wide-significant, 2nd after NOTCH1, ~7% of TOF |
| [38713105](https://pubmed.ncbi.nlm.nih.gov/38713105/) | Core: ER-aggregation/proteostatic mechanism; zebrafish rescue; distinct from Milroy |
| [33067626](https://pubmed.ncbi.nlm.nih.gov/33067626/) | VEGFR3 biology; dominant-negative Milroy mechanism; homozygous-null lethality |
| [39870876](https://pubmed.ncbi.nlm.nih.gov/39870876/) | FLT4 splice variants cause left- and right-sided CHD; incomplete penetrance; RNA-seq diagnostics |
| [32037394](https://pubmed.ncbi.nlm.nih.gov/32037394/) | FLT4 transmitted from subclinical parent; genome sequencing as first-tier test |
| [40127276](https://pubmed.ncbi.nlm.nih.gov/40127276/) | 60 dominant CHD genes; 10.1% of 11,555 probands; incomplete penetrance, de novo + transmitted |
| [34328347](https://pubmed.ncbi.nlm.nih.gov/34328347/) | Reanalysis of 811 TOF probands confirms FLT4 as major contributor |
| [42258347](https://pubmed.ncbi.nlm.nih.gov/42258347/) | Prognosis: ~90% >30-yr survival; universal PR/RV overload; AF 20–45% by 45 |
| [42894905](https://pubmed.ncbi.nlm.nih.gov/42894905/) | Long-term adult cohort: reintervention ~41–52%, PVR most common |
| [36277185](https://pubmed.ncbi.nlm.nih.gov/36277185/) | TOF epidemiology (~3/10,000; 5–10% of CHD); nonsyndromic genetics |
| [11592985](https://pubmed.ncbi.nlm.nih.gov/11592985/) | Chy mouse models Milroy branch; VEGF-C gene-therapy rescue |
| [32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/) | CHD risk: maternal diabetes adjOR 4.04; folate-rich diet protective |
| [19952004](https://pubmed.ncbi.nlm.nih.gov/19952004/) | Periconceptional folic acid protective (OR 0.82) |
| [34392783](https://pubmed.ncbi.nlm.nih.gov/34392783/) | Mediterranean/antioxidant diet protective against congenital heart defects |
| [27443814](https://pubmed.ncbi.nlm.nih.gov/27443814/) | Secondhand smoke associated with septal defects |
| [42403553](https://pubmed.ncbi.nlm.nih.gov/42403553/) | Arrhythmia management in adult CHD |
| [42875919](https://pubmed.ncbi.nlm.nih.gov/42875919/) | Minimally invasive pulmonary valve replacement after TOF repair |
| [41957907](https://pubmed.ncbi.nlm.nih.gov/41957907/) | TOF with MAPCAs/ductal-origin PA anatomy and outcomes |
| [42277928](https://pubmed.ncbi.nlm.nih.gov/42277928/) | TOF surgical outcomes in developing-country setting |
| [26091405](https://pubmed.ncbi.nlm.nih.gov/26091405/) | Rare recessive FLT4 lymphedema allele (distinct from CHTD7) |
| [22745786](https://pubmed.ncbi.nlm.nih.gov/22745786/) | VEGFR3 → PI3K/AKT, MEK/ERK downstream signalling |
| [38201272](https://pubmed.ncbi.nlm.nih.gov/38201272/) | Dysregulation of lymphatic endothelial VEGFR3 signalling |
| [23520166](https://pubmed.ncbi.nlm.nih.gov/23520166/) | Sox18–VegfC genetic interaction in zebrafish lymphangiogenesis |

**Evidence types:** human clinical/genetic cohorts (30232381, 30582441, 34328347, 40127276, 39870876, 32037394), in vitro endothelial models (38713105), model organisms (38713105 zebrafish; 11592985 mouse), and epidemiological case-control studies (32092068, 19952004).

---

## Limitations and Knowledge Gaps

- **Serial-number disease label:** CHTD7 lacks dedicated Orphanet/ICD/MeSH codes and recorded synonyms; most clinical literature discusses the TOF phenotype rather than the OMIM entity by name, so phenotype-level and gene-level data had to be bridged.
- **Penetrance not quantified:** incomplete penetrance is firmly established but no numeric penetrance estimate specific to FLT4-CHD is available; modifier genes are unmapped.
- **No FLT4-specific GxE interaction:** environmental risk/protective data (diabetes, folate) are from general-CHD cohorts, not FLT4 carriers.
- **VUS burden:** 623/741 FLT4 ClinVar records are VUS, limiting clinical actionability; functional assays (ER-aggregation readout) are not yet routine.
- **Model gap:** no heterozygous mouse cleanly reproduces the human TOF cardiac phenotype; the mouse captures the lymphatic (Milroy) branch while zebrafish captures the cardiac branch.
- **No targeted therapy:** proteostasis modulation and VEGF-C gene therapy are preclinical/lymphatic-only; no cardiac-directed molecular therapy exists.
- **Epidemiology of the molecular subtype:** prevalence/incidence, sex ratio, and geographic distribution are reported at the TOF phenotype level, not the FLT4-genotype level.

---

## Proposed Follow-up Experiments / Actions

1. **Penetrance estimation:** assemble FLT4-variant pedigrees with genotyped relatives to derive an age-/sex-adjusted penetrance estimate and test for modifier loci (including NOTCH1/KDR second hits).
2. **Functional VUS triage:** develop a scalable ER-aggregation/proteostatic-stress assay in primary human endothelial cells (per [PMID: 38713105](https://pubmed.ncbi.nlm.nih.gov/38713105/)) to reclassify the large FLT4 VUS pool.
3. **Mechanism-anchored therapeutics:** test proteostasis modulators / ER-stress-pathway inhibitors in the zebrafish *flt4*-TOF-variant model to validate the preclinical lead.
4. **Genotype–phenotype mapping:** correlate FLT4 variant class (null vs ER-aggregating missense) with anatomic subtype (absent pulmonary valve, right aortic arch, MAPCAs) and long-term reintervention/arrhythmia outcomes.
5. **Gene–environment interaction:** prospectively test whether maternal diabetes/folate status modifies penetrance specifically in FLT4-variant pregnancies.
6. **Cardiac mouse model:** engineer conditional/endothelial-specific humanized FLT4-TOF-missense knock-in mice to close the model-organism gap for the cardiac phenotype.

---

*Report compiled from 8 confirmed findings across 29 reviewed papers over 5 iterations. Causal gene: **FLT4 (VEGFR3)**. OMIM 618780; MONDO:0032913.*


## Artifacts

- [OpenScientist final report](Congenital_Heart_Defects_Multiple_Types_7-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Heart_Defects_Multiple_Types_7-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 11 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:27443814` (6 mentions) - Associations between maternal periconceptional exposure to secondhand tobacco smoke and major birth defects.
  - shared terms: defect
- `PMID:22745786` (4 mentions) - Vascular endothelial growth factor receptor-3 directly interacts with phosphatidylinositol 3-kinase to regulate lymphangiogenesis.
  - shared terms: primary, genetic

Weighed against this report's own most characteristic terms: `flt4`, `tof`, `variant`, `gene`, `pulmonary`, `defect`, `penetrance`, `chd`, `heart`, `vegfr3`, `cardiac`, `milroy`, `disease`, `incomplete`, `chtd7`, `arrhythmia`, `primary`, `phenotype`, `zebrafish`, `genetic`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0010316` (2 mentions) - the report calls it "Absent pulmonary valve"; HP calls it **Ebstein anomaly of the tricuspid valve**
- `CL:0002138` (1 mention) - the report calls it "relevant to the Milroy branch"; CL calls it **endothelial cell of lymphatic vessel**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001656` (1 mention) - HP does not contain this term
- `HP:0010449` (1 mention), reported as "Pulmonary regurgitation (post-repair)" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001642` (2 mentions) - the report calls it "Pulmonary valve stenosis"; HP calls it **Pulmonic stenosis**, and lists "Pulmonary valve stenosis" among its other names
- `CL:0000115` (2 mentions) - the report calls it "endothelium"; CL calls it **endothelial cell**, and lists "endotheliocyte" among its other names
- `UBERON:0004145` (1 mention) - the report calls it "right ventricular outflow tract"; UBERON calls it **outflow tract**, and lists "heart outflow tract" among its other names