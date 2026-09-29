---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-09T13:29:34.468140'
end_time: '2026-09-09T14:22:16.005079'
duration_seconds: 3161.54
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: MOGS-Congenital Disorder of Glycosylation
  mondo_id: MONDO:0011629
  category: Mendelian
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
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 15
  validator_version: 0.2.1
term_validation:
  total_terms: 45
  verified: 43
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 4
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0011629
    reported_labels:
    - if available
    ontology_label: MOGS-congenital disorder of glycosylation
  - term_id: HP:0001252
    reported_labels:
    - Nearly universal
    ontology_label: Hypotonia
  - term_id: HP:0001188
    reported_labels:
    - Common
    ontology_label: Hand clenching
  - term_id: HP:0002791
    reported_labels:
    - Common (severe cases)
    ontology_label: Hypoventilation
  - term_id: HP:0002720
    reported_labels:
    - Subset
    ontology_label: Decreased circulating IgA concentration
  - term_id: HP:0000505
    reported_labels:
    - Minority
    ontology_label: Visual impairment
  labels_variant: 3
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: MOGS-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: MOGS-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MOGS-Congenital Disorder of Glycosylation
- **MONDO ID:** MONDO:0011629 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MOGS-Congenital Disorder of Glycosylation** covering all of the
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

# MOGS-Congenital Disorder of Glycosylation (MOGS-CDG / CDG-IIb): Comprehensive Disease Characteristics Report

**MONDO:** MONDO:0011629 | **Category:** Mendelian (autosomal recessive inborn error of metabolism)
**Prepared:** Iterations 1–5 — evidence base combines primary literature (human clinical case series and mechanistic studies) with live public-database queries (gnomAD constraint, ClinVar variant spectrum, UniProt protein architecture, ClinicalTrials.gov). MOGS-CDG is ultra-rare (~30 patients reported worldwide as of 2024), so most clinical evidence is from individual patients and small case series rather than aggregated registry-scale data.

**Evidence provenance (database queries performed):** gnomAD (constraint: pLI ≈ 0, LOEUF = 0.84 → LoF-tolerant, recessive) · ClinVar (647 *MOGS* records; ≈27 P/LP vs 153 VUS; overwhelmingly SNVs) · UniProt Q13724 (837-aa type II ER membrane GH63 enzyme; catalytic D583/E807; N-glycosylated at N657) · ClinicalTrials.gov (no MOGS-CDG-specific interventional trials). Evidence types are labelled throughout as human-clinical, in vitro, model-organism, or computational/database.

---

## 1. Disease Information

**Overview.** MOGS-CDG is an ultra-rare autosomal recessive congenital disorder of glycosylation caused by biallelic loss-of-function variants in *MOGS*, which encodes **mannosyl-oligosaccharide glucosidase (glucosidase I / GCS1)**, the first enzyme in the endoplasmic-reticulum (ER) processing/trimming of N-linked oligosaccharides. Loss of glucosidase I activity blocks the initial trimming of the Glc₃Man₉GlcNAc₂ N-glycan precursor, disrupting N-glycan maturation on many glycoproteins. It is classified as a **CDG type II** (a defect of glycan *processing/remodeling*, as opposed to type I assembly defects). The first patient was described by De Praeter et al. in 2000 (PMID 10788335).

**Key identifiers:**
- **OMIM:** #606056 (Congenital disorder of glycosylation, type IIb) — gene *MOGS* OMIM 601336
- **Orphanet:** ORPHA:79328 (MOGS-CDG / CDG-IIb)
- **Mondo:** MONDO:0011629
- **ICD-10:** E77.8 (other disorders of glycoprotein metabolism); **ICD-11:** 5C51.2 (disorders of N-glycosylation)
- **MeSH:** Congenital Disorders of Glycosylation (D018981)
- **Gene HGNC:** MOGS (HGNC:24862); UniProt Q13724 (MOGS_HUMAN)

**Synonyms / alternative names:**
- CDG-IIb / CDG type IIb
- Glucosidase I deficiency; GCS1-CDG
- Mannosyl-oligosaccharide glucosidase deficiency
- Congenital disorder of glycosylation type 2b

**Data source type:** Individual patients / small international case series (EHR- and research-derived), not population registry aggregates, reflecting the disorder's rarity.

---

## 2. Etiology

**Primary cause (genetic).** Biallelic (homozygous or compound heterozygous) pathogenic variants in *MOGS* (chromosome 2p13.1) causing near-complete loss of glucosidase I enzymatic activity. This is a monogenic Mendelian defect; there are no established environmental or infectious causes.

- De Praeter (2000, PMID 10788335): first patient was a compound heterozygote for missense variants **R486T** and **F652L**; residual enzyme activity <3% of controls; both parents ~50% (obligate carriers) → autosomal recessive.
- Völker (2002, PMID 12145188): glucosidase I activity **<1%** of control in patient fibroblasts with intermediate parental values.

**Genetic risk factors.** The only risk factor is inheritance of two pathogenic *MOGS* alleles. **Consanguinity** raises risk of homozygous forms; reported cases are from diverse populations (European, Chinese, Japanese, Korean, Indian), consistent with private/family-specific variants rather than a common founder allele.

**Environmental risk factors.** None identified — disease is fully determined by genotype (congenital, present at birth).

**Protective factors.** No genetic or environmental protective factors are established. Notably, the glycosylation defect confers an *in vitro* protective phenotype against certain N-glycosylation–dependent enveloped viruses (see Mechanism/Immune), but this is not a clinically established protective factor.

**Gene–environment interactions.** Not applicable in a classical sense; disease expression is genotype-driven. Phenotypic variability among patients with similar genotypes suggests modifier effects (genetic background, residual enzyme activity), but specific modifiers are unidentified.

---

## 3. Phenotypes

MOGS-CDG is a multisystem disorder with prominent **neurological** involvement. Frequencies below are qualitative given the small cohort (~30 patients; Teutonico 2024, PMID 38498292; Post 2023, PMID 36651519; Shimada 2022, PMID 35790351).

| Phenotype | Type | Onset | Frequency | HPO term |
|---|---|---|---|---|
| Muscular hypotonia | Clinical sign | Neonatal/congenital | Nearly universal | HP:0001252 |
| Global developmental delay / intellectual disability | Clinical sign | Infancy | Nearly universal | HP:0001263 / HP:0001249 |
| Seizures / epileptic encephalopathy (often drug-resistant) | Clinical sign | Early infancy | Nearly universal | HP:0001250 / HP:0200134 |
| Feeding difficulties / failure to thrive | Symptom | Neonatal | Common | HP:0011968 / HP:0001508 |
| Hepatomegaly / hepatic dysfunction (elevated transaminases) | Sign/lab | Neonatal–infancy | Common | HP:0002240 / HP:0001392 |
| Dysmorphic facies (long eyelashes, retrognathia, hirsutism, depressed nasal bridge, high palate, blepharophimosis) | Physical | Congenital | Common | HP:0000527, HP:0000278, HP:0001007 |
| Clenched/overlapping fingers, overlapped toes | Physical | Congenital | Common | HP:0001188 |
| Hypoventilation / respiratory insufficiency | Sign | Neonatal | Common (severe cases) | HP:0002791 |
| Generalized edema / abnormal fat distribution | Sign | Neonatal | Reported subset | HP:0007430 |
| Movement disorder (dystonia, hyperkinetic movements) | Sign | Infancy–childhood | Subset (older survivors) | HP:0001332 / HP:0002072 |
| Hypogammaglobulinemia / immunodeficiency | Lab | Infancy | Subset | HP:0002720 |
| Progressive cerebral/cortical–subcortical atrophy, thin corpus callosum, ventricular dilation | Imaging | Infancy | Common | HP:0002059 / HP:0007371 |
| Vision problems | Symptom | Variable | Minority | HP:0000505 |
| Nephromegaly, hypothyroidism, GERD, auditory neuropathy, Hirschsprung disease | Sign | Variable | Rare/individual reports | HP:0000105, HP:0000821, HP:0002020, HP:0002232 |

**Severity/progression.** Variable, ranging from **fatal in infancy** (first patient died at 74 days, PMID 10788335) to **survival into adulthood** (oldest reported 19 years, PMID 33058492). Neurological course is generally **progressive** (worsening encephalopathy, brain atrophy) with drug-resistant epilepsy.

**Quality-of-life impact.** Profound: severe neurodevelopmental disability, drug-resistant seizures, feeding/respiratory support needs, and dependence for daily activities. No validated disease-specific QoL instruments exist for this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

- **Causal gene:** *MOGS* (mannosyl-oligosaccharide glucosidase; a.k.a. glucosidase I, GCS1). HGNC:24862; NCBI Gene 7841; OMIM 601336; UniProt Q13724; **Ensembl ENSG00000115275**. Reference transcript **NM_006302**. Located 2p13.1; a compact gene (**chr2:74,461,057–74,465,410, GRCh38**, ~4.35 kb) encoding an **837-aa, ~91.9 kDa type II single-pass ER membrane glycoprotein** of glycoside hydrolase family **CAZy GH63** (EC 3.2.1.106).
- **Population constraint (gnomAD, GRCh38):** MOGS is **loss-of-function tolerant at the heterozygous level** — **pLI ≈ 0** (3.9×10⁻¹⁰), observed/expected LoF **oe_lof = 0.66 (LOEUF = 0.84)**, missense Z = 0.97 (oe_mis = 0.93). This means haploinsufficiency is not disease-causing and healthy carriers are expected — exactly the signature of a **recessive enzymopathy** requiring biallelic loss of function (matches the ~50% carrier enzyme activity in healthy parents; PMID 12145188).

- **Pathogenic variant spectrum** — predominantly **missense**, with some frameshift/duplication:
  - R486T (c.1587G>C) and F652L — original compound heterozygote (PMID 10788335, 12145188)
  - c.1239_1267dup (p.Asp414Leufs*17), c.544G>A (p.Gly182Arg), c.1698C>A (p.Asp566Glu) in Chinese siblings (PMID 30587846)
  - Numerous additional private missense/compound-heterozygous variants across ~30 patients (Shimada 2022 PMID 35790351; Teutonico 2024 PMID 38498292)
- **Variant classification (ACMG/AMP):** Pathogenic/Likely pathogenic when biallelic with functional confirmation (enzyme assay or urine Glc₃Man). Structural modeling has been used to support pathogenicity (PMID 30587846). **ClinVar landscape (Iteration 3 query):** 647 *MOGS* records; of ~300 with classifications — **16 Pathogenic, 9 Likely pathogenic, 2 P/LP (≈27 P/LP), 1 Conflicting, 153 VUS, 114 Likely benign**. The large VUS fraction highlights the diagnostic importance of orthogonal functional confirmation (urine Glc₃Man, enzyme assay, or yeast *CWH41* complementation) to resolve novel variants.
- **Variant type distribution (ClinVar):** Overwhelmingly **single-nucleotide variants (278)** with a minority of small deletions (11), duplications (8), copy-number losses (2), and insertions (1) — i.e., predominantly missense and small frameshift alleles; structural variants are rare (so CMA/karyotype/FISH have little diagnostic role).
- **Variant types/class:** missense (most common), frameshift/duplication, and predicted splice/nonsense in some cases → **loss of function**.
- **Allele frequency:** Individually extremely rare/absent in gnomAD (private variants); no common recurrent allele; carrier frequency very low.
- **Somatic vs germline:** **Germline** only.
- **Functional consequence:** **Loss of function** (near-complete abolition of glucosidase I catalytic activity, <1–3% residual).

- **Modifier genes:** None confirmed. Compensatory upregulation of **endo-α1,2-mannosidase (MANEA)** partially bypasses the block (PMID 12145188) and may modulate phenotype.
- **Epigenetic information:** None reported.
- **Chromosomal abnormalities:** None; point/small variants only.

---

## 5. Environmental Information

- **Environmental factors:** None causally implicated. Disease is congenital and genotype-determined.
- **Lifestyle factors:** Not applicable (disease presents at/near birth).
- **Infectious agents:** Not a cause. Of note, patients show *reduced* susceptibility to certain enveloped viruses in vitro because viral entry glycoproteins depend on host N-glycosylation (PMID 24716661).

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function variants in *MOGS*** → results in near-complete deficiency (<1–3% residual) of ER glucosidase I. *(Demonstrated: enzyme assays, PMID 10788335, 12145188.)*
2. **Loss of glucosidase I activity** → fails to cleave the distal α1,2-linked glucose from the protein-bound **Glc₃Man₉GlcNAc₂** N-glycan precursor, the first committed step of N-glycan trimming in the ER. *(Demonstrated.)*
3. **Blocked trimming** → leads to accumulation of non-deglucosylated high-mannose N-glycans (**Glc₃Man₇₋₉GlcNAc₂**) on nascent glycoproteins and diversion of the precursor through **endo-α1,2-mannosidase**, releasing the free tetrasaccharide **Glc₃Man**, which is excreted in urine (diagnostic biomarker). *(Demonstrated, PMID 12145188, 36651519, 35137040.)*
4. **Impaired N-glycan maturation** → disrupts the **calnexin/calreticulin glycoprotein quality-control cycle** (which depends on monoglucosylated glycans) and downstream complex/sialylated glycan formation on many secreted and membrane glycoproteins. *(Partly inferred from glycan-processing biology; abnormal serum/IgG N-glycomes demonstrated, PMID 35137040.)*
5. **Aberrant glycoprotein processing** → branches into multiple organ effects:
   - **Neurological branch:** abnormal glycosylation of neuronal ion channels, adhesion molecules, and receptors → **developmental & epileptic encephalopathy, hypotonia, progressive cerebral atrophy, movement disorder**. *(Inferred; clinical correlation strong, PMID 33058492, 33261925, 38498292.)*
   - **Immune branch:** aberrant IgG glycosylation and **shortened immunoglobulin half-life** → **hypogammaglobulinemia**; simultaneously, host-glycan–dependent enveloped viruses (HIV, influenza) show impaired entry/replication → **paradoxical relative viral resistance despite low Ig**. *(Demonstrated in vitro, PMID 24716661.)*
   - **Hepatic branch:** abnormal glycoprotein handling → **hepatomegaly, elevated transaminases, coagulopathy** (glycosylated clotting factors). *(Inferred/clinical.)*
   - **Dysmorphogenesis branch:** disrupted glycosylation during development → **craniofacial dysmorphism, digital anomalies, edema**. *(Inferred.)*
6. **Cumulative multisystem glycoprotein dysfunction** → **progressive neurodegeneration, feeding/respiratory failure, and (in severe cases) death in infancy**; milder residual function permits survival into childhood/adolescence.

**Category detail:**
- **Molecular pathways:** N-linked glycan biosynthesis/processing (KEGG hsa00510); ER glycoprotein quality control / calnexin cycle (Reactome "Calnexin/calreticulin cycle", R-HSA-901042; "Asparagine N-linked glycosylation" R-HSA-446203).
- **Cellular processes:** ER protein processing, glycoprotein folding/quality control, ER-associated degradation modulation; neuronal excitability dysregulation (epilepsy).
- **Protein dysfunction:** Loss of function of glucosidase I. **Protein architecture (UniProt Q13724):** an 837-residue, ~91.9 kDa **type II single-pass ER membrane glycoside hydrolase** of **CAZy family GH63** (EC 3.2.1.106), with a short cytoplasmic tail (1–38), transmembrane signal-anchor (39–59), and a large lumenal catalytic domain (60–837; residues 76–137 required for ER targeting). Catalysis uses a **proton donor at position 583 and proton acceptor at 807**; the enzyme is itself N-glycosylated at Asn657. Pathogenic missense residues (e.g., **R486, F652**; PMID 10788335) map to this lumenal catalytic domain near the active-site machinery, disrupting acid–base catalysis and yielding <1–3% residual activity — loss of function by catalytic-domain disruption rather than aggregation.
- **Metabolic changes:** Accumulation and urinary excretion of free oligosaccharide **Glc₃Man**; hypermannosylated glycopeptides; dyslipidemia and elevated CK reported (PMID 36158009).
- **Immune involvement:** Hypogammaglobulinemia (shortened IgG half-life), reduced T/NK proportions, complement C3/C4 deficiency, elevated IL-6, yet reduced enveloped-virus susceptibility (PMID 24716661, 36158009).
- **Biochemical abnormality:** Enzyme deficiency of glucosidase I (EC 3.2.1.106; CAZy GH63). Catalytic reaction (UniProt Q13724): hydrolysis of the distal α-1,2-glucose from protein-bound Glc3Man9GlcNAc2, releasing β-D-glucose — Reactome R-HSA-4793954 ("Glucosidase I removes glucose from N-glycan").
- **Molecular profiling:** Serum/IgG N-glycomics show non-deglucosylated Glc₃Man₇₋₉GlcNAc₂ glycans and reduced core-fucosylated complex IgG glycans (PMID 35137040); glycomics show compensatory increase in Man₅GlcNAc₂ (PMID 36158009).

**Suggested ontology terms:** GO:0006487 (protein N-linked glycosylation), GO:0009311/GO:0006491 (oligosaccharide/N-glycan processing), GO:0004573 (mannosyl-oligosaccharide glucosidase activity), GO:0005788 (ER lumen). Cell types: CL:0000540 (neuron), CL:0000182 (hepatocyte), CL:0000786 (plasma cell). CHEBI: CHEBI:59080-class oligosaccharides; glucose (CHEBI:17234).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Brain/CNS (UBERON:0000955), liver (UBERON:0002107). **Secondary:** immune system (UBERON:0002405), skeletal muscle/neuromuscular (hypotonia), heart (pericardial effusion – PMID 36158009), kidney (nephromegaly), larynx (laryngomalacia/subglottic stenosis).
- **Body systems:** Nervous, hepatic/digestive, immune, respiratory, musculoskeletal.
- **Tissue/cell level:** Neurons and neural tissue (progressive cortical/subcortical atrophy); hepatocytes; plasma cells/B lymphocytes (Ig production); broadly any secretory/membrane-glycoprotein–producing cell.
- **Subcellular level:** **Endoplasmic reticulum** (UBERON n/a; GO:0005783 / GO:0005788 ER lumen) — site of glucosidase I action; secretory pathway broadly affected.
- **Localization / lateralization:** Bilateral, symmetric CNS involvement (diffuse cerebral atrophy). Systemic/generalized rather than focal.

---

## 8. Temporal Development

- **Onset:** **Congenital / neonatal** — hypotonia, dysmorphism, feeding and respiratory problems from birth; seizures in early infancy.
- **Onset pattern:** Subacute-to-chronic with early neonatal symptoms and progressive deterioration.
- **Progression:** Generally **progressive** neurodegeneration (worsening encephalopathy, cortical/subcortical atrophy). Some manifestations evolve (epileptic spasms in infancy ceasing by ~age 7 while tonic seizures persist; emergence of dystonia/hyperkinetic movement disorder — PMID 33058492).
- **Course/duration:** Chronic, lifelong. Severe forms are lethal in infancy (74 days in index case); milder forms survive to adolescence/adulthood.
- **Remission:** No spontaneous remission; seizures are typically drug-resistant. Certain seizure types may abate with age.
- **Critical period:** Neonatal/early-infancy window is critical for diagnosis and supportive intervention.

---

## 9. Inheritance and Population

- **Epidemiology:** Ultra-rare; **~30 patients reported worldwide** as of 2024 (PMID 38498292). Prevalence/incidence not formally estimated (Orphanet: <1/1,000,000); no reliable per-100,000 figures.
- **Inheritance:** **Autosomal recessive** (both parents obligate carriers with ~50% enzyme activity; PMID 10788335, 12145188).
- **Penetrance:** Complete for biallelic loss-of-function genotypes.
- **Expressivity:** **Variable** (lethal infancy → survival to adulthood), even within families.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects:** None documented; variants are private/family-specific.
- **Consanguinity:** Contributes to homozygous cases in consanguineous families.
- **Carrier frequency:** Very low (private variants; largely absent from gnomAD). Consistent with this, gnomAD shows MOGS is LoF-tolerant (pLI ≈ 0, LOEUF = 0.84), so heterozygous carriers are asymptomatic and population-frequent enough to be observed, but biallelic combinations are exceedingly rare.
- **Population demographics:** Reported across European, Chinese, Japanese, Korean, and Indian families; no ethnic predilection or geographic clustering. No clear sex bias (both sexes affected). Age distribution: presents in neonates/infants.

---

## 10. Diagnostics

- **First-line clue:** Multisystem neonatal presentation (hypotonia, seizures, dysmorphism, hepatomegaly) with **normal serum transferrin isoelectric focusing** — MOGS-CDG **escapes routine CDG transferrin screening** (PMID 33261925).
- **Key biochemical test:** **Urine oligosaccharide analysis** (MALDI-TOF MS) detecting the pathognomonic free tetrasaccharide **Glc₃Man** — reliable screening/confirmation (PMID 36651519, 35790351, 33261925). Quantitative Glc₃Man assays now available.
- **Enzyme assay:** Glucosidase I activity in fibroblasts/liver markedly reduced (<1–3%) — historical gold standard (PMID 10788335, 12145188).
- **Glycomics:** Serum/IgG N-glycan profiling shows accumulated Glc₃Man₇₋₉GlcNAc₂ and altered IgG glycans (PMID 35137040, 36158009).
- **Genetic testing (definitive):** **Whole-exome sequencing** is the principal diagnostic route in most recent cases (PMID 38498292, 33261925); WGS, targeted CDG gene panels, or single-gene *MOGS* sequencing also applicable. CMA/karyotype/FISH/mtDNA/repeat testing **not** indicated. Confirm biallelic *MOGS* variants + segregation.
- **Imaging:** Brain MRI — cerebral/cortical–subcortical atrophy, thin corpus callosum, ventricular dilation.
- **Supportive labs:** Low immunoglobulins/hypogammaglobulinemia, elevated transaminases, coagulopathy, dyslipidemia, elevated CK, complement C3/C4 deficiency (PMID 36158009).
- **Differential diagnosis:** Other CDG type II subtypes, other early-infantile epileptic/developmental encephalopathies, other inborn errors with hypotonia + hepatopathy + dysmorphism; distinguished by normal transferrin IEF + urine Glc₃Man + *MOGS* genotype. UGGT1-CDG (PMID 40267907) is a related ER quality-control CDG in the differential.
- **Screening:** Not on standard newborn screening panels; cascade carrier testing feasible once a familial variant is known; prenatal/PGT possible for known familial variants.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** Highly variable and often poor. Index patient died at **74 days** (PMID 10788335); severe neonatal forms with hypoventilation/failure to thrive carry high infant mortality. Milder cases survive into childhood/adolescence; **oldest reported 19 years** (PMID 33058492). No formal 5-/10-year survival statistics exist.
- **Morbidity/function:** Severe neurodevelopmental disability, drug-resistant epilepsy, hypotonia, feeding and respiratory dependence, movement disorder in survivors — profound long-term disability.
- **Complications:** Recurrent infections despite paradoxical viral resistance, aspiration/respiratory failure, hepatic dysfunction/coagulopathy, status epilepticus, failure to thrive.
- **Recovery potential:** No cure; management is supportive. Neurological damage is largely irreversible/progressive.
- **Prognostic factors:** Degree of residual enzyme activity, severity of neonatal respiratory/feeding compromise, seizure control. No validated molecular prognostic biomarkers; urinary Glc₃Man is diagnostic rather than prognostic.

---

## 12. Treatment

**No disease-specific or curative therapy exists.** Management is multidisciplinary and supportive.

- **Pharmacotherapy:** **Anti-seizure medications** for epilepsy (often drug-resistant; combinations frequently required) — NCIT anticonvulsant agents (NCIT:C264). **Immunoglobulin replacement (IVIG)** for symptomatic hypogammaglobulinemia (NCIT:C29099). Nutritional support, management of reflux/hepatic/coagulation issues.
- **Advanced/experimental therapeutics:** No approved gene, cell, RNA, or enzyme-replacement therapy. The α-glucosidase inhibitor **miglustat** (an iminosugar) has been studied in relation to the MOGS glycosylation phenotype and antiviral glycan modification, but **not** as a disease-modifying treatment for MOGS-CDG itself (PMID 33245474). Miglustat NCIT:C61765. A **ClinicalTrials.gov API query (Iteration 3)** for "MOGS-CDG / glucosidase I deficiency / CDG-IIb" returned **no interventional trials specific to MOGS-CDG** (keyword hits were unrelated glucosidase disorders — Pompe/Gaucher ERT and gene-therapy studies), confirming the absence of a disease-specific experimental therapeutic pipeline to date.
- **Surgical/interventional:** Supportive only (e.g., gastrostomy for feeding, respiratory support).
- **Supportive/rehabilitative:** Physical, occupational, and speech therapy; feeding support; respiratory care; developmental/palliative care.
- **Treatment outcomes:** Symptomatic benefit only; seizures frequently refractory. No response-rate data given rarity.
- **Personalized medicine:** Care guided by organ involvement; genetic counseling for families.
- **Pharmacogenomics:** None established.

---

## 13. Prevention

- **Primary prevention:** Not possible (congenital genetic disorder). **Genetic counseling** for at-risk families; carrier screening for relatives; **prenatal diagnosis** and **preimplantation genetic testing (PGT)** available when the familial *MOGS* variants are known.
- **Secondary prevention:** Early recognition via urine oligosaccharide analysis (Glc₃Man) and WES in neonates with encephalopathy/dysmorphism/hepatopathy, enabling timely supportive care.
- **Tertiary prevention:** Aggressive seizure management, IVIG to reduce infections, nutritional/respiratory support to limit complications.
- **Immunization/public health/environmental measures:** Not applicable to disease causation; standard immunizations and infection precautions apply, individualized given the immune phenotype.
- **Counseling:** Autosomal recessive recurrence risk 25% per pregnancy for carrier couples — central genetic counseling message.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *MOGS* is evolutionarily conserved. Orthologs: mouse *Mogs* (NCBI Gene 57377), and the yeast homolog **CWH41/GLS1** in *Saccharomyces cerevisiae* (NCBI Taxon 4932). A prokaryotic MOGS (pMOGS) was recently identified in *Elizabethkingia meningoseptica* (PMID 40674822).
- **Natural disease in animals:** No well-characterized naturally occurring MOGS-CDG equivalent reported in companion animals or wildlife (OMIA has no established entry analogous to human MOGS-CDG). Veterinary relevance limited.
- **Comparative biology:** The N-glycan trimming pathway and glucosidase I function are highly conserved from yeast to humans, making cross-species functional assays informative (see Model Organisms).
- **Transmission:** Not applicable (non-infectious, non-zoonotic).

---

## 15. Model Organisms

- **Yeast (S. cerevisiae):** *CWH41* (MOGS homolog) knockout strains provide a **functional complementation assay** — human *MOGS* and its disease variants can be tested for rescue of the N-glycan profile, allowing pathogenicity assessment of patient mutations (PMID 40674822). Strong tool for variant interpretation.
- **Prokaryotic MOGS:** A bacterial MOGS (pMOGS) characterized as an additional model/reagent for studying MOGS activity (PMID 40674822).
- **Cellular / in vitro models:** Patient-derived **skin fibroblasts** (enzyme kinetics, glycan analysis; PMID 12145188, 10788335); MOGS-null transfected cells used for glycan/antiviral studies (PMID 33245474); overexpression systems for glucosidase-inhibitor and viral-glycoprotein studies (PMID 24716661, 33245474).
- **Mammalian genetic models:** No widely reported viable *Mogs* knockout mouse disease model in the retrieved literature; complete loss is expected to be developmentally severe. This is a **limitation** — no established rodent model recapitulating the human neurological phenotype.
- **Model characteristics/limitations:** Yeast/cellular systems faithfully recapitulate the **biochemical** defect (glycan trimming block) and are excellent for variant functional testing, but do **not** reproduce the multisystem neurological/immunological human phenotype. Applications: variant pathogenicity assays, glycan pathway/compensation studies, and antiviral glycan-modification research.
- **Resources:** SGD (yeast CWH41), MGI (mouse *Mogs*), Cellosaurus (patient fibroblast lines).

---

## Key Supported vs. Refuted Hypotheses

**Supported:**
- MOGS-CDG is autosomal recessive, caused by biallelic loss-of-function *MOGS* variants abolishing glucosidase I activity (PMID 10788335, 12145188).
- The disorder escapes transferrin-based CDG screening; urine Glc₃Man is the diagnostic biomarker (PMID 33261925, 36651519).
- Core phenotype = neonatal hypotonia + developmental/epileptic encephalopathy + dysmorphism + hepatic dysfunction, with a paradoxical immune signature (hypogammaglobulinemia + relative viral resistance) (PMID 29235540, 24716661).

**Refuted / not supported:**
- Not detectable by standard serum transferrin IEF (normal pattern) — refutes reliance on transferrin screening.
- No environmental/infectious cause; not associated with chromosomal abnormalities, somatic mutation, founder alleles, or repeat expansion.

## Limitations and Future Directions

- Evidence rests on ~30 individual cases — no registry-scale epidemiology, natural-history, or QoL data; frequencies are qualitative.
- No approved disease-modifying therapy; enzyme/gene/substrate strategies unexplored clinically. Genotype–phenotype correlations and modifiers (e.g., endo-α1,2-mannosidase compensation) merit study.
- A faithful mammalian disease model is lacking; yeast/cellular complementation assays are the current functional standard.
- The therapeutic and antiviral implications of the MOGS glycan phenotype (miglustat, host-glycan–dependent viruses) warrant continued investigation.

---

### Primary References (PMID)
10788335 (De Praeter 2000, first case) · 12145188 (Völker 2002, enzymology/compensation) · 24716661 (Sadat 2014, immune phenotype/viral resistance) · 29235540 (Kim 2018, dysmorphism) · 30587846 (Li 2019, compound het variants) · 33058492 (Lo Barco 2021, oldest patient/movement disorder) · 33245474 (Nunes-Santos 2021, miglustat/glycan) · 33261925 (Anzai 2021, normal transferrin/urine oligosaccharides) · 35137040 (Beimdiek 2022, serum/IgG N-glycomics) · 35790351 (Shimada 2022, clinical/biochemical/genetic characterization) · 36158009 (Abuduxikuer 2022, updated clinical/glycomic) · 36651519 (Post 2023, diagnostic Glc₃Man quantitation) · 38498292 (Teutonico 2024, review, ~30 patients) · 40674822 (Zou 2025, prokaryotic MOGS/yeast complementation) · 41192964 (Shwetabh 2025, DEE case) · 40267907 (Dardas 2025, related UGGT1-CDG).


## Artifacts

- [OpenScientist final report](MOGS-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](MOGS-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 13 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011629` (3 mentions) - the report calls it "if available"; MONDO calls it **MOGS-congenital disorder of glycosylation**
- `HP:0001252` (1 mention) - the report calls it "Nearly universal"; HP calls it **Hypotonia**
- `HP:0001188` (1 mention) - the report calls it "Common"; HP calls it **Hand clenching**
- `HP:0002791` (1 mention) - the report calls it "Common (severe cases)"; HP calls it **Hypoventilation**
- `HP:0002720` (1 mention) - the report calls it "Subset"; HP calls it **Decreased circulating IgA concentration**
- `HP:0000505` (1 mention) - the report calls it "Minority"; HP calls it **Visual impairment**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006491` (1 mention) - the report calls it "oligosaccharide/N-glycan processing"; GO calls it **N-glycan processing**
- `GO:0004573` (1 mention) - the report calls it "mannosyl-oligosaccharide glucosidase activity"; GO calls it **Glc3Man9GlcNAc2 oligosaccharide glucosidase activity**, and lists "mannosyl-oligosaccharide glucosidase activity" among its other names
- `GO:0005788` (2 mentions) - the report calls it "ER lumen"; GO calls it **endoplasmic reticulum lumen**, and lists "ER lumen" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
