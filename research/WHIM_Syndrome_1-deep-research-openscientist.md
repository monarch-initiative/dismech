---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T19:27:21.818706'
end_time: '2026-09-24T19:55:24.815699'
duration_seconds: 1683.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: WHIM Syndrome 1
  mondo_id: MONDO:8000006
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
citation_count: 29
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 10
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:35588454
  relevance_assessed: 30
  on_topic: 30
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 40
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 7
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:8000006
    reported_labels:
    - MONDO
    ontology_label: WHIM syndrome 1
  - term_id: HP:0001875
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased total neutrophil count
  - term_id: HP:0002718
    reported_labels:
    - Symptom/sign
    ontology_label: Recurrent bacterial infections
  - term_id: HP:0006532
    reported_labels:
    - Sign
    ontology_label: Recurrent pneumonia
  - term_id: HP:0002110
    reported_labels:
    - Physical manifestation
    ontology_label: Bronchiectasis
  - term_id: HP:0200043
    reported_labels:
    - Physical manifestation
    ontology_label: Verrucae
  - term_id: HP:0002664
    reported_labels:
    - Physical manifestation
    ontology_label: Neoplasm
  - term_id: HP:0002720
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased circulating IgA concentration
  - term_id: HP:0001627
    reported_labels:
    - Physical manifestation
    ontology_label: Abnormal heart morphology
  labels_variant: 7
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
  path: WHIM_Syndrome_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: WHIM_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** WHIM Syndrome 1
- **MONDO ID:** MONDO:8000006 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **WHIM Syndrome 1** covering all of the
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

# WHIM Syndrome 1 — Comprehensive Disease Characteristics Report

**Disease:** WHIM Syndrome 1 (Warts, Hypogammaglobulinemia, Infections, Myelokathexis)
**MONDO ID:** MONDO:8000006
**Category:** Mendelian, autosomal dominant combined primary immunodeficiency
**Causal gene:** *CXCR4* (C-X-C chemokine receptor type 4)

---

## Summary

WHIM Syndrome 1 is a rare, autosomal dominant combined primary immunodeficiency and chronic neutropenic disorder caused by heterozygous **gain-of-function truncating mutations in the intracellular C-terminal tail of the chemokine receptor gene *CXCR4*** (most commonly p.R334X). The acronym encodes the four cardinal features — **W**arts, **H**ypogammaglobulinemia, **I**nfections, and **M**yelokathexis. The unifying molecular lesion is loss of the receptor's C-terminal serine/threonine phosphorylation sites, which normally recruit **GRK6 and β-arrestin** to desensitize and internalize the receptor after ligand binding. Truncation uncouples CXCR4 from this "off switch," producing sustained, exaggerated signaling in response to its sole ligand **CXCL12/SDF-1** (increased calcium flux, ERK phosphorylation, and chemotaxis). Because the CXCL12–CXCR4 axis is the master retention signal for mature leukocytes in the bone marrow, hyperactive CXCR4 traps mature neutrophils (and other leukocytes) in the marrow — the hallmark **myelokathexis** — yielding paradoxical peripheral neutropenia and panleukopenia despite a hypercellular marrow.

Clinically, patients present in early childhood with severe congenital neutropenia, recurrent bacterial infections (especially pneumonia), a disproportionate susceptibility to human papillomavirus (HPV)-driven warts and anogenital malignancy, and variable hypogammaglobulinemia with B- and T-lymphopenia. Long-term complications include bronchiectasis and HPV-related cancers. Diagnosis is frequently delayed by a decade or more because myelokathexis requires specialized bone-marrow evaluation and penetrance is incomplete.

The disease has become a landmark example of mechanism-to-medicine translation. Because pathology stems from CXCR4 hyperactivity, CXCR4 antagonism reverses the leukocyte sequestration: the oral small-molecule antagonist **mavorixafor (Xolremdi)** became the **first FDA-approved targeted therapy for WHIM syndrome on 26 April 2024**, following a positive phase 3 trial. Complementary curative strategies exploit the fact that *lowering* CXCR4 gives hematopoietic stem cells a competitive advantage: a patient was spontaneously cured by chromothripsis that deleted the disease allele, and CRISPR-based disease-allele inactivation offers a proof-of-concept genetic cure.

---

## 1. Disease Information

**Overview.** WHIM syndrome is a rare inherited immunodeficiency defined by the tetrad of **W**arts, **H**ypogammaglobulinemia, recurrent bacterial **I**nfections, and **M**yelokathexis (retention/apoptosis of mature neutrophils in the bone marrow). It is classified as an autosomal dominant combined immunodeficiency (CID) with an early-onset hallmark of neutropenia ([PMID: 41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/); [PMID: 29066537](https://pubmed.ncbi.nlm.nih.gov/29066537/)).

**Key identifiers.**
| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:8000006 |
| OMIM | #193670 (WHIM syndrome 1, WHIMS1) |
| Gene | *CXCR4*, OMIM *162643; HGNC:2561 |
| Orphanet | ORPHA:51636 |
| MeSH | WHIM syndrome / Warts, hypogammaglobulinemia, infections, and myelokathexis syndrome |
| ICD-10 | D84.8 (other specified immunodeficiencies) / D70 (neutropenia) |

**Synonyms / alternative names.** Warts–hypogammaglobulinemia–infections–myelokathexis syndrome; WHIMS; WHIMS1; historical "myelokathexis" descriptions (now attributed to CXCR4). "WHIM Syndrome 1" specifically denotes the CXCR4-associated form (the canonical and by far most common genotype).

**Information source.** The knowledge base entry is derived from **aggregated disease-level resources** — international patient cohorts, case series, mechanistic in vitro and mouse studies, and clinical trials — rather than from a single individual EHR.

---

## 2. Etiology

**Primary causal factor — genetic.** WHIM Syndrome 1 is caused by **heterozygous, autosomal dominant, gain-of-function truncating mutations in the *CXCR4* gene**, which encodes a seven-transmembrane G-protein-coupled chemokine receptor. Mutations truncate the intracellular C-terminal tail, removing the serine/threonine residues required for receptor desensitization ([PMID: 31313072](https://pubmed.ncbi.nlm.nih.gov/31313072/); [PMID: 36883568](https://pubmed.ncbi.nlm.nih.gov/36883568/); [PMID: 12692554](https://pubmed.ncbi.nlm.nih.gov/12692554/)).

> "WHIM syndrome is usually caused by autosomal dominant mutations in the G protein-coupled chemokine receptor CXCR4 that impair desensitization, resulting in enhanced and prolonged G protein- and β-arrestin-dependent responses" ([PMID: 31313072](https://pubmed.ncbi.nlm.nih.gov/31313072/)).

**Genetic risk factors.** The disease-causing variants are the risk factors — there are no separate susceptibility loci. The single largest genetic risk factor is inheriting one WHIM *CXCR4* allele; **p.R334X (c.1000C>T)** is the most frequent variant. Additional described variants include p.Ser338X, p.Gly336X, p.Leu317fsX3, and an N-terminal p.D84H variant that expands the spectrum beyond the canonical C-terminal hotspot ([PMID: 36883568](https://pubmed.ncbi.nlm.nih.gov/36883568/); [PMID: 41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/)). Notably, some patients with full clinical WHIM carry a **wild-type CXCR4 gene** yet share the same CXCR4 signaling dysfunction, implying rare non-CXCR4 or upstream/downstream causes (genetic heterogeneity) ([PMID: 21178277](https://pubmed.ncbi.nlm.nih.gov/21178277/)).

**Environmental risk factors.** No environmental exposure causes WHIM. However, **HPV exposure** is the necessary environmental trigger for the wart/malignancy phenotype: the immune defect renders patients unable to control HPV once acquired. Bacterial pathogens drive the infection phenotype but are opportunistic consequences of neutropenia, not causes of the disease.

**Protective factors.** The most striking protective factor is *genetic*: **CXCR4 haploinsufficiency (loss of one functional copy) confers a hematopoietic stem-cell engraftment advantage** and can reverse disease. A WHIM patient was cured when a chromothriptic event deleted the disease allele ([PMID: 25662009](https://pubmed.ncbi.nlm.nih.gov/25662009/)). No dietary or lifestyle protective factors are established.

**Gene–environment interaction.** The genetic lesion (CXCR4 gain-of-function → immune-cell dysfunction) interacts with environmental HPV exposure to produce warts and cancer; mouse studies show WHIM animals are markedly more susceptible to papillomavirus-induced disease specifically because of immune-cell dysfunction, and bone-marrow transplant from wild-type donors normalizes susceptibility ([PMID: 39226327](https://pubmed.ncbi.nlm.nih.gov/39226327/)).

---

## 3. Phenotypes

WHIM is a multisystem immunodeficiency. Frequencies below derive chiefly from an international cohort of 18 patients and a review of 105 published cases ([PMID: 30716504](https://pubmed.ncbi.nlm.nih.gov/30716504/)).

| Phenotype | Type | HPO suggestion | Onset | Frequency | Severity/Course |
|-----------|------|----------------|-------|-----------|-----------------|
| Severe neutropenia | Lab abnormality | HP:0001875 | Congenital/infancy | ~100% (ANC ~195 ± 102 cells/mm³) | Severe, chronic |
| Myelokathexis (marrow neutrophil retention + apoptotic hypersegmented nuclei) | Pathology/lab | HP:0031160 (myelokathexis) | Congenital | Defining feature | Chronic |
| Panleukopenia (lymphopenia, monocytopenia) | Lab abnormality | HP:0001882; HP:0012312 | Childhood | Common; B-lymphopenia and monocytopenia | Chronic |
| Recurrent bacterial infections | Symptom/sign | HP:0002718 | Early childhood (2.2 ± 2.6 yr) | Severe bacterial infection in 78% | Recurrent |
| Recurrent pneumonia | Sign | HP:0006532 | Childhood | 61% | Recurrent → bronchiectasis |
| Bronchiectasis | Physical manifestation | HP:0002110 | Later (progressive) | 27% | Progressive, irreversible |
| Cutaneous/genital warts (HPV) | Physical manifestation | HP:0200043 | Mean age 11 yr | 61% | Refractory, progressive |
| HPV-related malignancy | Physical manifestation | HP:0002664 | Adulthood | 16% | Life-threatening |
| Hypogammaglobulinemia | Lab abnormality | HP:0002720 | Variable | Variable (may be absent) | Variable |
| Congenital cardiac defects | Physical manifestation | HP:0001627 | Congenital | Uncommon | Variable |

**Age of onset.** Clinical features typically manifest at **2.2 ± 2.6 years**, but diagnosis is delayed to a mean of **12.5 ± 10.4 years** ([PMID: 30716504](https://pubmed.ncbi.nlm.nih.gov/30716504/)).

**Severity/progression.** Neutropenia and myelokathexis are stable and lifelong; infections are episodic; bronchiectasis and HPV malignancy are progressive complications. Lymphopenia is selective — **CD8⁺ T-cell lymphopenia is more severe than CD4⁺**, due to sequestration in the thymus and bone marrow ([PMID: 37133343](https://pubmed.ncbi.nlm.nih.gov/37133343/)).

> "Pneumonia recurrence was observed in 61% of patients and was complicated with bronchiectasis in 27%. Skin warts were observed in 61% of patients at a mean age of 11 years, whereas human papilloma virus (HPV)-related malignancies manifested in 16% of patients." ([PMID: 30716504](https://pubmed.ncbi.nlm.nih.gov/30716504/))

**Quality of life impact.** Recurrent infections, chronic wart burden (disfiguring, refractory), IVIG dependence, and progressive lung disease substantially impair daily functioning; formal EQ-5D/SF-36 datasets specific to WHIM are not available. Despite severe neutropenia, the overall clinical course is frequently milder and more manageable than the laboratory picture suggests ([PMID: 36793393](https://pubmed.ncbi.nlm.nih.gov/36793393/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** *CXCR4* (chromosome **2q22.1**; historically mapped by linkage to 2q21). HGNC:2561; OMIM *162643. Encodes a 352-residue GPCR whose sole ligand is CXCL12 (SDF-1).

**Gene discovery.** Hernandez et al. (2003) localized WHIM to chromosome 2q21 and identified **truncating mutations in the cytoplasmic tail domain of *CXCR4*** — the first example of a chemokine receptor causing a human Mendelian disease ([PMID: 12692554](https://pubmed.ncbi.nlm.nih.gov/12692554/)).

> "the identification of truncating mutations in the cytoplasmic tail domain of the gene encoding chemokine receptor 4 (CXCR4)" ([PMID: 12692554](https://pubmed.ncbi.nlm.nih.gov/12692554/))

> "Lymphoblastoid cell lines carrying a 19-residue truncation mutation show significantly greater calcium flux relative to control cell lines in response to the CXCR4 ligand, SDF-1, consistent with dysregulated signaling by the mutant receptor" ([PMID: 12692554](https://pubmed.ncbi.nlm.nih.gov/12692554/))

**Pathogenic variants.**
| Variant | cDNA | Type | Consequence | Notes |
|---------|------|------|-------------|-------|
| p.R334X | c.1000C>T | Nonsense/truncating | Removes ~19 C-terminal residues | Most common WHIM allele |
| p.S338X | — | Nonsense/truncating | C-terminal truncation | Recurrent |
| p.G336X | — | Nonsense/truncating | C-terminal truncation | Recurrent |
| p.Leu317fsX3 | — | Frameshift | Truncation with altered signaling profile | Reduced G-protein signaling despite impaired internalization ([PMID: 36883568](https://pubmed.ncbi.nlm.nih.gov/36883568/)) |
| p.D84H | — | Missense (N-terminal) | Non-canonical activation | Expands genetic spectrum ([PMID: 41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/)) |

- **Classification (ACMG/AMP):** Pathogenic (recurrent truncating variants with established functional gain-of-function mechanism).
- **Variant type:** Predominantly nonsense/frameshift truncations of the C-terminal tail; rarely missense.
- **Allele frequency:** Absent/ultra-rare in gnomAD (consistent with a severe dominant disease).
- **Origin:** **Germline**, inherited autosomal dominant (or de novo). Not somatic in origin (except the acquired *somatic* chromothriptic reversion event that cured one patient).
- **Functional consequence:** **Gain of function** — enhanced and prolonged signaling due to impaired desensitization; not a simple loss of function.

> "All mutations reported in WHIM patients lead to the truncations in the C-terminal domain of CXCR4, R334X being the most frequent. This defect prevents receptor internalization and enhances both calcium mobilization and ERK phosphorylation, resulting in increased chemotaxis in response to the unique ligand CXCL12." ([PMID: 36883568](https://pubmed.ncbi.nlm.nih.gov/36883568/))

**Modifier genes.** No formally validated modifier genes; the marked clinical variability (incomplete penetrance, variable expressivity, WHIM without hypogammaglobulinemia/warts) suggests genetic and stochastic modifiers exist but are not yet mapped.

**Epigenetic information.** No disease-specific DNA-methylation or histone-modification signature has been established for WHIM.

**Chromosomal abnormalities.** Not a cause of WHIM. However, a spontaneous **chromothripsis** event — deleting the *CXCR4^R334X* allele plus 163 neighboring genes from one copy of chromosome 2 in a single HSC — produced a natural cure, an instructive example of a large-scale acquired somatic rearrangement reversing a dominant disease ([PMID: 25662009](https://pubmed.ncbi.nlm.nih.gov/25662009/)).

> "deletion of the disease allele, CXCR4(R334X), as well as 163 other genes from one copy of chromosome 2 occurred in a hematopoietic stem cell (HSC) that repopulated the myeloid but not the lymphoid lineage" ([PMID: 25662009](https://pubmed.ncbi.nlm.nih.gov/25662009/))

---

## 5. Environmental Information

- **Environmental factors:** No toxins, radiation, or occupational exposures cause WHIM.
- **Lifestyle factors:** None established as causal or protective.
- **Infectious agents:** Infections are *consequences* of the immunodeficiency, not causes. The most clinically important pathogen is **human papillomavirus (HPV)**, to which patients are disproportionately susceptible, driving warts and anogenital/cervical/head-and-neck carcinomas ([PMID: 30716504](https://pubmed.ncbi.nlm.nih.gov/30716504/); [PMID: 39226327](https://pubmed.ncbi.nlm.nih.gov/39226327/)). Recurrent encapsulated-bacterial infections (pneumonia, otitis, cellulitis, sepsis) result from neutropenia and hypogammaglobulinemia.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous truncating mutation** in the *CXCR4* C-terminal tail (e.g., p.R334X) **removes the serine/threonine phosphorylation cluster** required for receptor regulation. *(demonstrated)*
2. The truncated receptor **fails to recruit GRK6** (while GRK3 binding is preserved) and shows **delayed β-arrestin2 recruitment**, which **impairs receptor phosphorylation, internalization, and desensitization**. *(demonstrated, in vitro)* ([PMID: 19956569](https://pubmed.ncbi.nlm.nih.gov/19956569/))
3. Impaired desensitization **leads to sustained and exaggerated CXCR4 signaling** in response to CXCL12 — **increased calcium mobilization, prolonged ERK phosphorylation, and enhanced chemotaxis**. *(demonstrated)* ([PMID: 36883568](https://pubmed.ncbi.nlm.nih.gov/36883568/); [PMID: 12692554](https://pubmed.ncbi.nlm.nih.gov/12692554/))
4. At the membrane, the mutant receptor **fails to nanocluster after CXCL12 stimulation**, producing **inadequate β-arrestin1-dependent actin remodeling and defective chemotactic gradient sensing**. *(demonstrated, single-particle tracking)* ([PMID: 35588454](https://pubmed.ncbi.nlm.nih.gov/35588454/))
5. Because CXCL12–CXCR4 is the **master retention signal** keeping leukocytes in the bone-marrow niche, hyperactive CXCR4 **results in failure of mature neutrophils to egress** → they accumulate and undergo apoptotic senescence in the marrow → **myelokathexis**. *(demonstrated)* ([PMID: 29734477](https://pubmed.ncbi.nlm.nih.gov/29734477/); [PMID: 21890643](https://pubmed.ncbi.nlm.nih.gov/21890643/))
6. Retention **leads to peripheral neutropenia and panleukopenia** (lymphocytes and monocytes are also sequestered; ALC > monocyte > neutrophil in responsiveness to CXCR4 blockade). *(demonstrated pharmacologically)* ([PMID: 21890643](https://pubmed.ncbi.nlm.nih.gov/21890643/))

   **Branch A — antibacterial defense:** Neutropenia + hypogammaglobulinemia + impaired B-cell trafficking → **recurrent bacterial infections → pneumonia → bronchiectasis**.

   **Branch B — antiviral/antitumor defense:** Selective **CD8⁺ > CD4⁺ T lymphopenia via sequestration in thymus and bone marrow** ([PMID: 37133343](https://pubmed.ncbi.nlm.nih.gov/37133343/)) + reduced lymphocyte infiltration into infected tissue → **failure to control HPV → refractory warts → HPV-driven malignancy** ([PMID: 39226327](https://pubmed.ncbi.nlm.nih.gov/39226327/)).

7. Overall, CXCR4 hyperactivation **disrupts stromal niches critical for lymphocyte development and survival**, producing the combined immunodeficiency phenotype. *(inferred/demonstrated in models)* ([PMID: 41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/))

### Supporting detail

- **Molecular pathways.** CXCL12→CXCR4→Gαi (inhibits adenylyl cyclase; PI3K/AKT; MAPK/ERK) and β-arrestin scaffolding. The regulatory lesion is at the **GRK/β-arrestin desensitization module** (Reactome: "Signaling by GPCR"; GPCR desensitization). Downstream ERK1/2 activation is prolonged.
- **Cellular processes.** Impaired cell migration/chemotaxis (GO:0006935), defective receptor internalization (GO:0031623 receptor internalization; GO:0002031 GPCR internalization), leukocyte retention, actin cytoskeleton remodeling (GO:0030036), neutrophil apoptosis/senescence.
- **Protein dysfunction.** Truncated GPCR with intact ligand binding and surface expression but **defective regulatory phosphorylation** → gain-of-function signaling. Surface expression and internalization of receptor were shown unaffected in some patients while chemotaxis was enhanced ([PMID: 15026312](https://pubmed.ncbi.nlm.nih.gov/15026312/)).
- **Immune system involvement.** Combined immunodeficiency: neutropenia + B-lymphopenia (reduced memory B cells) + T-cell abnormalities (accumulation of effector memory T cells, restricted TCR repertoire, severe CD8 lymphopenia) + variable hypogammaglobulinemia ([PMID: 15026312](https://pubmed.ncbi.nlm.nih.gov/15026312/); [PMID: 37133343](https://pubmed.ncbi.nlm.nih.gov/37133343/)).
- **Tissue damage.** Chronic pulmonary infection → airway destruction → bronchiectasis; HPV-driven epithelial dysplasia → carcinoma.
- **Biochemical abnormality.** GPCR desensitization defect (receptor regulation, not enzyme deficiency).

> "while both kinases Grk3 and Grk6 bind to WT CXCR4 and are critical to its trafficking to the lysosomes, Grk6 fails to associate with the WHIM-mutant receptor whereas Grk3 associates normally" ([PMID: 19956569](https://pubmed.ncbi.nlm.nih.gov/19956569/))

> "CXCR4R334X, a truncated mutant chemokine receptor linked to WHIM syndrome (warts, hypogammaglobulinemia, infections, myelokathexis), fails to nanocluster after CXCL12 stimulation" ([PMID: 35588454](https://pubmed.ncbi.nlm.nih.gov/35588454/))

**GO term suggestions:** GO:0006935 (chemotaxis), GO:0002031 (GPCR internalization), GO:0007204 (positive regulation of cytosolic calcium), GO:0070098 (chemokine-mediated signaling), GO:0002686 (negative regulation of leukocyte migration).
**CL term suggestions:** CL:0000775 (neutrophil), CL:0000625 (CD8⁺ αβ T cell), CL:0000624 (CD4⁺ αβ T cell), CL:0000236 (B cell), CL:0000576 (monocyte), CL:0000037 (hematopoietic stem cell).
**CHEBI term suggestions:** CHEBI:calcium(2+) ion (second messenger); mavorixafor and plerixafor as CXCR4-antagonist small molecules.

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** Bone marrow (UBERON:0002371) — site of myelokathexis; hematopoietic/immune system (UBERON:0002390 hematopoietic system; UBERON:0002405 immune system).
- **Secondary:** Lung (UBERON:0002048) → recurrent pneumonia and bronchiectasis; skin (UBERON:0002097) and anogenital mucosa → HPV warts and dysplasia; thymus (UBERON:0002370) → T-cell sequestration; occasionally heart (UBERON:0000948) → congenital cardiac defects.
- **Body systems:** Hematologic, immune, respiratory, integumentary; occasionally cardiovascular.

**Tissue and cell level.** Bone-marrow myeloid tissue (accumulated mature neutrophils with hypersegmented, apoptotic nuclei); respiratory epithelium (infection-related damage); squamous epithelium (HPV). Cell populations affected: neutrophils (CL:0000775), CD8⁺ and CD4⁺ T lymphocytes, B lymphocytes, monocytes, and hematopoietic stem/progenitor cells whose egress is impaired.

**Subcellular level.** Plasma-membrane GPCR signaling machinery (GO:0005886 plasma membrane); endocytic/lysosomal trafficking machinery is functionally engaged but the mutant receptor evades normal trafficking to lysosomes (GO:0005764 lysosome); β-arrestin/clathrin endocytic compartment (GO:0005905 clathrin-coated pit).

**Localization / lateralization.** Systemic and bilateral (marrow-wide, systemic leukopenia); warts and infections are distributed per exposure (not lateralized).

---

## 8. Temporal Development

- **Onset:** Congenital/early-childhood. Neutropenia and myelokathexis are present from infancy; clinical symptoms begin ~2 years of age; pattern is **chronic and insidious** ([PMID: 30716504](https://pubmed.ncbi.nlm.nih.gov/30716504/); [PMID: 41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/)).
- **Progression:** Neutropenia is stable and lifelong; infections are episodic/recurrent; **bronchiectasis and HPV malignancy accumulate progressively** with age. Warts typically emerge around age 11; malignancies in adulthood.
- **Course pattern:** Chronic, lifelong; complications progressive. No spontaneous remission except the exceptional chromothriptic reversion ([PMID: 25662009](https://pubmed.ncbi.nlm.nih.gov/25662009/)).
- **Critical periods / windows for intervention:** Early pediatric diagnosis is associated with improved outcomes; newborn screening (low thymic emigrant T cells / TREC assay) can identify some infants, opening an early intervention window ([PMID: 41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/)).

---

## 9. Inheritance and Population

**Epidemiology.** WHIM is ultra-rare. Estimated prevalence is on the order of **~0.23 per million** (Orphanet-class ultra-rare); only ~105 published cases had been reviewed at the time of the cohort analyses ([PMID: 30716504](https://pubmed.ncbi.nlm.nih.gov/30716504/)). Precise incidence figures are unavailable owing to rarity and underdiagnosis.

**Genetic etiology.**
- **Inheritance:** Autosomal dominant ([PMID: 29066537](https://pubmed.ncbi.nlm.nih.gov/29066537/)).
- **Penetrance:** Incomplete/variable — contributes to diagnostic delay ([PMID: 41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/)).
- **Expressivity:** Highly variable, even within families (e.g., a Chinese kindred with four affected members showing heterogeneous phenotypes) ([PMID: 39575248](https://pubmed.ncbi.nlm.nih.gov/39575248/)).
- **Genetic anticipation:** Not a repeat-expansion disorder; anticipation not described.
- **Germline mosaicism / founder effects:** Not established; p.R334X recurs as an independent mutational hotspot rather than a founder allele.
- **Carrier frequency:** Not applicable (dominant); affected individuals are heterozygotes.

**Population demographics.** No strong ethnic predilection; reported worldwide, including the first documented case in a patient of African ancestry ([PMID: 36793393](https://pubmed.ncbi.nlm.nih.gov/36793393/)) and familial Chinese cases ([PMID: 39575248](https://pubmed.ncbi.nlm.nih.gov/39575248/)). Sex ratio approximately equal (autosomal). Age distribution spans infancy to adulthood, with diagnosis often in the second decade.

---

## 10. Diagnostics

**Clinical/laboratory tests.**
- **CBC with differential:** Chronic **severe neutropenia** (ANC ~195 ± 102 cells/mm³ in cohort), lymphopenia, monocytopenia — panleukopenia ([PMID: 30716504](https://pubmed.ncbi.nlm.nih.gov/30716504/)).
- **Immunoglobulins:** Hypogammaglobulinemia (variable; may be normal).
- **Bone-marrow biopsy/aspirate — key diagnostic test:** **Myelokathexis** — hypercellular marrow crowded with mature neutrophils showing hypersegmented, pyknotic (apoptotic) nuclei connected by thin chromatin strands. Detailed BM/peripheral-blood characterization of 30 CXCR4-variant patients confirms morphologic variability and correlates morphology with the CXCR4 internalization defect ([PMID: 40239948](https://pubmed.ncbi.nlm.nih.gov/40239948/)).
- **Lymphocyte immunophenotyping:** Decreased memory B cells, decreased naïve T cells, accumulation of effector-memory T cells, restricted TCR repertoire, and selective severe CD8 lymphopenia ([PMID: 15026312](https://pubmed.ncbi.nlm.nih.gov/15026312/); [PMID: 37133343](https://pubmed.ncbi.nlm.nih.gov/37133343/)).
- **Imaging:** Chest CT for bronchiectasis surveillance.

**Genetic testing (confirmatory).** Sequencing of **CXCR4** — single-gene testing or inclusion in immunodeficiency/neutropenia gene panels; WES/WGS increasingly used. Detection of a heterozygous C-terminal truncating variant (e.g., p.R334X) confirms the diagnosis. Functional assays (impaired CXCL12-induced internalization; enhanced chemotaxis/calcium flux) support pathogenicity in ambiguous cases.

**Clinical criteria / differential diagnosis.** The diagnostic tetrad (WHIM), though hypogammaglobulinemia and/or warts may be absent. WHIM should be **suspected in congenital neutropenia + lymphopenia even without hypogammaglobulinemia or warts** ([PMID: 29066537](https://pubmed.ncbi.nlm.nih.gov/29066537/)). Differentials include:
- **G6PC3 deficiency / severe congenital neutropenia** — can show increased neutrophil CXCR4 expression and myelokathexis-like marrow but is autosomal recessive with multisystem features ([PMID: 20616219](https://pubmed.ncbi.nlm.nih.gov/20616219/)).
- **GATA2 deficiency** — monocytopenia, B/NK lymphopenia, generalized verrucosis, myeloid leukemia risk ([PMID: 24359037](https://pubmed.ncbi.nlm.nih.gov/24359037/)).
- **CXCR2 loss-of-function** — neutropenia + myelokathexis-like morphology ([PMID: 41451234](https://pubmed.ncbi.nlm.nih.gov/41451234/)).
- Other combined immunodeficiencies, epidermodysplasia verruciformis, WILD syndrome.

**Screening.** **Newborn screening TREC assays** (low thymic emigrant T cells) can flag some WHIM infants; cascade genetic testing of first-degree relatives once a proband variant is identified ([PMID: 18535531](https://pubmed.ncbi.nlm.nih.gov/18535531/); [PMID: 41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/)).

---

## 11. Outcome / Prognosis

**Survival/mortality.** With modern supportive care (G-CSF, IVIG) and now CXCR4 antagonists, WHIM is generally manageable and compatible with adult survival; there are no large formal survival curves. Principal threats to life are **invasive HPV-driven malignancy** and **progressive lung disease**.

**Morbidity/function.** Substantial: recurrent infections, IVIG dependence, refractory wart burden, and **bronchiectasis in 27%** with progressive lung-function decline ([PMID: 30716504](https://pubmed.ncbi.nlm.nih.gov/30716504/); [PMID: 18535531](https://pubmed.ncbi.nlm.nih.gov/18535531/)).

**Complications.** Bronchiectasis; anogenital dysplasia and invasive cancer; **HPV-related malignancies in 16%** of patients; chronic humoral immunodeficiency ([PMID: 30716504](https://pubmed.ncbi.nlm.nih.gov/30716504/); [PMID: 29066537](https://pubmed.ncbi.nlm.nih.gov/29066537/)).

**Prognostic factors.** **Early pediatric diagnosis is associated with improved outcomes** ([PMID: 41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/)). Degree of lymphopenia (particularly CD8) and cumulative HPV disease burden predict antiviral/malignancy risk. As a CID with lifetime risk for humoral deficiency, impaired antiviral defense, and malignancy, WHIM warrants **long-term monitoring** ([PMID: 41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/)).

---

## 12. Treatment

### Pharmacotherapy — mechanism-based (CXCR4 antagonists)

Because pathology stems from CXCR4 hyperactivity, **CXCR4 antagonism directly reverses leukocyte sequestration.**

**Mavorixafor (Xolremdi)** — oral small-molecule selective CXCR4 antagonist; **first FDA-approved targeted therapy for WHIM (26 April 2024)**, indicated for patients aged ≥12 years ([PMID: 40223492](https://pubmed.ncbi.nlm.nih.gov/40223492/); [PMID: 40212179](https://pubmed.ncbi.nlm.nih.gov/40212179/)).

> "On April 26th, 2024, Xolremdi (mavorixafor) capsules received its approval from US FDA, is the first targeted treatment specifically for patients aged ≥12 years with WHIM syndrome." ([PMID: 40223492](https://pubmed.ncbi.nlm.nih.gov/40223492/))

**Clinical trial evidence:**

| Trial | Design | Key result | PMID |
|-------|--------|-----------|------|
| Phase 1 plerixafor (low-dose, 6 mo) | n=3, open-label | Durable leukocyte increases; fewer infections; wart improvement with imiquimod; Ig not fully restored; no side effects | [24523241](https://pubmed.ncbi.nlm.nih.gov/24523241/) |
| Phase 1 plerixafor (dose-escalation) | n=3 (R334X) | Dose-dependent correction of panleukopenia (ALC>monocyte>neutrophil) | [21890643](https://pubmed.ncbi.nlm.nih.gov/21890643/) |
| Phase 2 mavorixafor | n=8, open-label | Dose-dependent ANC/ALC rise; infection rate 4.63→2.27/yr; ~75% wart reduction | [32870250](https://pubmed.ncbi.nlm.nih.gov/32870250/) |
| **Phase 3 mavorixafor (pivotal)** | n=31, randomized, double-blind, placebo-controlled, age ≥12 | **TAT-ANC 15.0 vs 2.8 h (P<.001); TAT-ALC 15.8 vs 4.6 h (P<.001); annualized infections 60% lower (1.7 vs 4.2, P=.007)** | [38643510](https://pubmed.ncbi.nlm.nih.gov/38643510/) |

> "mavorixafor least squares (LS) mean TATANC was 15.0 hours and 2.8 hours for placebo (P < .001)" ([PMID: 38643510](https://pubmed.ncbi.nlm.nih.gov/38643510/))

**Plerixafor (Mozobil, AMD3100)** — injectable CXCR4 antagonist (FDA-approved for stem-cell mobilization); used off-label/investigationally in WHIM; provided the first pharmacologic proof that panleukopenia is CXCL12–CXCR4-signaling-dependent ([PMID: 21890643](https://pubmed.ncbi.nlm.nih.gov/21890643/); [PMID: 24523241](https://pubmed.ncbi.nlm.nih.gov/24523241/)).

**Conventional/supportive therapy.** **G-CSF (filgrastim)** to raise neutrophil counts; **IVIG** for hypogammaglobulinemia/passive immunity; **antibiotic prophylaxis**; topical/ablative wart therapy (e.g., imiquimod); HPV vaccination; cancer surveillance. These have limited efficacy, require frequent administration, and carry patient burden — motivating targeted therapy ([PMID: 40212179](https://pubmed.ncbi.nlm.nih.gov/40212179/); [PMID: 36793393](https://pubmed.ncbi.nlm.nih.gov/36793393/)).

### Advanced / curative therapeutics

- **Gene therapy — disease-allele inactivation.** CRISPR/Cas9 inactivation of one *Cxcr4* copy in HSPCs enriches WHIM-allele-inactivated cells in vivo while retaining long-term pluripotency — a proof-of-concept genetic cure exploiting CXCR4 haploinsufficiency's engraftment advantage ([PMID: 36928087](https://pubmed.ncbi.nlm.nih.gov/36928087/)).

> "To our knowledge, this is the first example of gene therapy for an autosomal dominant gain-of-function disease using a disease allele inactivation strategy in place of the less efficient disease allele repair approach" ([PMID: 36928087](https://pubmed.ncbi.nlm.nih.gov/36928087/))

- **Natural cure precedent.** Chromothriptic deletion of the disease allele in an HSC produced a spontaneous, durable cure of a WHIM patient ([PMID: 25662009](https://pubmed.ncbi.nlm.nih.gov/25662009/)).

**NCIT term suggestions:** Mavorixafor (CXCR4-antagonist small molecule), Plerixafor (NCIT:C2411), Granulocyte colony-stimulating factor / Filgrastim (NCIT:C1512), Intravenous immunoglobulin therapy (NCIT:C603), Hematopoietic stem cell gene therapy.

---

## 13. Prevention

- **Primary prevention:** Not preventable (germline dominant). **Genetic counseling** for affected families; prenatal/preimplantation genetic testing possible when the familial variant is known.
- **Secondary prevention (early detection):** Newborn TREC screening flags some infants; cascade genetic testing of relatives; early bone-marrow evaluation in unexplained congenital neutropenia. Early diagnosis improves outcomes ([PMID: 41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/)).
- **Tertiary prevention (complication avoidance):** **HPV vaccination**, dermatologic/gynecologic surveillance for HPV dysplasia/malignancy, antibiotic prophylaxis, IVIG, pulmonary surveillance for bronchiectasis, and CXCR4-antagonist therapy to reduce infection burden ([PMID: 29066537](https://pubmed.ncbi.nlm.nih.gov/29066537/); [PMID: 38643510](https://pubmed.ncbi.nlm.nih.gov/38643510/)).
- **Counseling:** Autosomal dominant recurrence risk (50% to offspring); genetic counseling recommended.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human *CXCR4* (NCBI Gene 7852). Mouse ortholog *Cxcr4* (NCBI Gene 12767) is well conserved; the CXCL12–CXCR4 axis and its role in leukocyte retention are evolutionarily conserved across vertebrates (mouse, zebrafish).
- **Natural disease in other species:** No naturally occurring WHIM-equivalent disease is documented in companion animals or wildlife (OMIA); WHIM in non-human species is experimentally induced, not natural.
- **Comparative biology:** The mechanism (CXCR4 gain-of-function → myelokathexis → neutropenia) is faithfully reproduced in engineered mice, supporting deep evolutionary conservation of the pathway. CXCR4 antagonism corrects analogous neutrophil abnormalities even in a *CXCR2* loss-of-function mouse model, underscoring the conserved CXCR4/CXCR2 balance governing bone-marrow neutrophil release ([PMID: 41451234](https://pubmed.ncbi.nlm.nih.gov/41451234/)).
- **Transmission / zoonosis:** Not applicable (genetic, non-transmissible).

---

## 15. Model Organisms

**Mouse (Mus musculus, NCBI Taxon 10090).** The principal WHIM model is a **knock-in mouse carrying the human-equivalent *Cxcr4* C-terminal truncation (R334X)**.
- **Phenotype recapitulation (strong):** Reproduces peripheral neutropenia, lymphopenia, myelokathexis-like marrow morphology, selective severe CD8 lymphopenia, and heightened HPV (MmuPV1) susceptibility ([PMID: 37133343](https://pubmed.ncbi.nlm.nih.gov/37133343/); [PMID: 39226327](https://pubmed.ncbi.nlm.nih.gov/39226327/); [PMID: 40239948](https://pubmed.ncbi.nlm.nih.gov/40239948/)).
- **Therapeutic validation:** Oral CXCR4 antagonism corrects neutrophil and lymphocyte abnormalities and normalizes leukocyte trafficking in the WHIM mouse ([PMID: 39588369](https://pubmed.ncbi.nlm.nih.gov/39588369/)); bone-marrow transplant from WT donors normalizes papillomavirus susceptibility, localizing the defect to hematopoietic cells ([PMID: 39226327](https://pubmed.ncbi.nlm.nih.gov/39226327/)).
- **Competitive transplant models:** Demonstrated that *Cxcr4* haploinsufficiency confers a strong long-term HSC engraftment advantage — the biological basis for allele-inactivation gene therapy ([PMID: 36928087](https://pubmed.ncbi.nlm.nih.gov/36928087/)).

**Zebrafish (Danio rerio, NCBI Taxon 7955).** Used to model CXCR4-axis immunomodulation; plerixafor reduced sepsis mortality in an LPS zebrafish model, supporting broader CXCR4-antagonist repurposing ([PMID: 38963161](https://pubmed.ncbi.nlm.nih.gov/38963161/)).

**In vitro / cellular models.** Patient lymphoblastoid cell lines and heterologous CXCR4-expression systems established the gain-of-function signaling (calcium flux, ERK, chemotaxis), the GRK6/β-arrestin recruitment defect, and single-particle-tracking membrane-nanoclustering abnormality ([PMID: 12692554](https://pubmed.ncbi.nlm.nih.gov/12692554/); [PMID: 19956569](https://pubmed.ncbi.nlm.nih.gov/19956569/); [PMID: 35588454](https://pubmed.ncbi.nlm.nih.gov/35588454/)).

**Model limitations.** Murine hypogammaglobulinemia and wart phenotypes are less faithful than the neutropenia/myelokathexis phenotype; HPV modeling requires the surrogate MmuPV1.

**Resources:** MGI (*Cxcr4*), IMPC, ZFIN (zebrafish *cxcr4b*).

---

## Mechanistic Model (Synthesis)

```
   CXCR4 C-terminal truncating mutation (e.g., p.R334X, heterozygous, germline)
                              │  removes Ser/Thr phosphorylation cluster
                              ▼
   Failure to recruit GRK6 (GRK3 preserved) + delayed β-arrestin2  [PMID 19956569]
                              │
                              ▼
   Impaired receptor desensitization / internalization
                              │
                              ▼
   Sustained, exaggerated CXCL12→CXCR4 signaling
   (↑Ca²⁺, prolonged pERK, ↑chemotaxis; defective nanoclustering/gradient sensing)
                              │        [PMID 36883568, 12692554, 35588454]
                              ▼
   Failure of mature leukocyte egress from bone marrow  (CXCR4 = master retention signal)
                              │        [PMID 29734477, 21890643]
                              ▼
   MYELOKATHEXIS  →  peripheral NEUTROPENIA + PANLEUKOPENIA
             ┌────────────────────────────┴───────────────────────────┐
             ▼                                                          ▼
  Neutropenia + hypogammaglobulinemia                    Selective CD8>CD4 lymphopenia
   → recurrent bacterial infections                       (thymus/marrow sequestration)
   → pneumonia → BRONCHIECTASIS                            → failure to control HPV
                                                           → refractory WARTS → MALIGNANCY
             └───────────────► reversible by CXCR4 antagonism (mavorixafor) ◄──────────┘
                    curable by CXCR4-allele loss (chromothripsis / CRISPR)
```

---

## Evidence Base

| PMID | Contribution | Evidence type |
|------|-------------|---------------|
| [12692554](https://pubmed.ncbi.nlm.nih.gov/12692554/) | Gene discovery: CXCR4 C-terminal truncations cause WHIM; first chemokine-receptor Mendelian disease; enhanced calcium flux | Human genetics + in vitro |
| [31313072](https://pubmed.ncbi.nlm.nih.gov/31313072/) | Autosomal dominant, impaired desensitization → enhanced G-protein/β-arrestin responses | Review |
| [36883568](https://pubmed.ncbi.nlm.nih.gov/36883568/) | R334X most frequent; prevents internalization; ↑Ca²⁺, ↑ERK, ↑chemotaxis | In vitro |
| [19956569](https://pubmed.ncbi.nlm.nih.gov/19956569/) | GRK6 (not GRK3) recruitment failure; delayed β-arrestin2 → delayed internalization | In vitro |
| [35588454](https://pubmed.ncbi.nlm.nih.gov/35588454/) | R334X fails to nanocluster; impaired gradient sensing/directed migration | In vitro single-particle |
| [15026312](https://pubmed.ncbi.nlm.nih.gov/15026312/) | Enhanced chemotaxis with normal surface expression; lymphocyte phenotype abnormalities | Human |
| [30716504](https://pubmed.ncbi.nlm.nih.gov/30716504/) | 18-patient cohort: infection 78%, pneumonia 61%, bronchiectasis 27%, warts 61%, HPV malignancy 16%; diagnostic delay | Human cohort |
| [37133343](https://pubmed.ncbi.nlm.nih.gov/37133343/) | Selective CD8>CD4 lymphopenia via sequestration in primary immune organs | Human + mouse |
| [21890643](https://pubmed.ncbi.nlm.nih.gov/21890643/) | Plerixafor corrects panleukopenia — pharmacologic proof of sequestration mechanism | Phase 1 |
| [38643510](https://pubmed.ncbi.nlm.nih.gov/38643510/) | Phase 3 mavorixafor: TAT-ANC/ALC and infection endpoints met | Phase 3 RCT |
| [40223492](https://pubmed.ncbi.nlm.nih.gov/40223492/) / [40212179](https://pubmed.ncbi.nlm.nih.gov/40212179/) | FDA approval of mavorixafor, 26 Apr 2024 | Regulatory |
| [25662009](https://pubmed.ncbi.nlm.nih.gov/25662009/) | Chromothriptic spontaneous cure — HSC engraftment advantage from CXCR4 loss | Human case |
| [36928087](https://pubmed.ncbi.nlm.nih.gov/36928087/) | CRISPR disease-allele inactivation gene-therapy proof-of-concept | Mouse/in vitro |
| [39226327](https://pubmed.ncbi.nlm.nih.gov/39226327/) | WHIM mice: HPV susceptibility is immune-cell-dependent; WT BM rescues | Mouse |
| [39588369](https://pubmed.ncbi.nlm.nih.gov/39588369/) | CXCR4 antagonism corrects leukocyte abnormalities in WHIM mouse | Mouse |
| [40239948](https://pubmed.ncbi.nlm.nih.gov/40239948/) | 30-patient BM/PB morphology; genotype–morphology correlation | Human pathology |
| [41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/) | Recent review: newborn screening, expanded genetic spectrum (D84H), niche disruption | Review |

---

## Limitations and Knowledge Gaps

1. **Rarity limits epidemiology.** Precise prevalence/incidence and formal survival statistics are lacking; estimates rest on <150 published cases.
2. **Genetic heterogeneity.** Rare WHIM-phenotype patients carry wild-type *CXCR4* ([PMID: 21178277](https://pubmed.ncbi.nlm.nih.gov/21178277/)); the responsible lesions (upstream regulators, other genes) are not fully mapped. No validated modifier genes explain the marked variable expressivity/incomplete penetrance.
3. **Incomplete Ig/vaccine-response restoration.** CXCR4 antagonists robustly correct cell counts but do not fully restore immunoglobulin levels or specific antibody responses ([PMID: 24523241](https://pubmed.ncbi.nlm.nih.gov/24523241/)), leaving residual humoral risk.
4. **Long-term antagonist data.** Durability, malignancy-prevention efficacy, and pediatric (<12 y) data for mavorixafor remain to be established.
5. **Model gaps.** Mouse models under-represent the humoral/wart phenotype; HPV must be modeled via MmuPV1 surrogate.
6. **Epigenetics/omics.** No disease-specific methylation, transcriptomic, proteomic, or metabolomic signature has been formally defined for WHIM.

---

## Proposed Follow-up Experiments / Actions

1. **Long-term registry** of mavorixafor-treated patients to quantify infection, bronchiectasis progression, HPV malignancy incidence, and survival versus historical G-CSF/IVIG cohorts.
2. **Pediatric and non-CXCR4 (wild-type WHIM) trials** to extend indication and identify alternative causal genes via WGS + functional CXCR4-pathway assays.
3. **Advance CRISPR disease-allele-inactivation gene therapy** ([PMID: 36928087](https://pubmed.ncbi.nlm.nih.gov/36928087/)) toward first-in-human trials, leveraging the HSC engraftment advantage of CXCR4-haploinsufficient cells.
4. **Mechanistic dissection of humoral defect** — why antibody responses remain impaired despite corrected B-cell counts (germinal-center/stromal-niche studies).
5. **Modifier-gene mapping** across large kindreds to explain variable penetrance/expressivity.
6. **Single-cell / spatial transcriptomics of WHIM bone marrow** to characterize the stromal-niche disruption implicated in the combined immunodeficiency ([PMID: 41451822](https://pubmed.ncbi.nlm.nih.gov/41451822/)).
7. **HPV-directed prevention studies** (early vaccination, surveillance protocols) given the 16% malignancy rate.

---

*Report compiled from an autonomous five-iteration literature investigation (32 papers reviewed, 6 confirmed findings). Evidence types are labeled throughout: human clinical/cohort, model organism, in vitro, and regulatory.*


## Artifacts

- [OpenScientist final report](WHIM_Syndrome_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](WHIM_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 30 |
| On topic | 30 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:35588454` *(abstract only)*: "CXCR4R334X, a truncated mutant chemokine receptor linked to WHIM syndrome (warts, hypogammaglobulinemia, infections, myelokathexis), fails to nanocluster after CXCL12 stimulation"
  - closest text in source: "Using single-particle tracking analysis we show that CXCR4R334X, a truncated mutant chemokine receptor linked to WHIM syndrome (warts, hypogammaglobulinemia, infections, myelokathexis), fails to nanoclusterize after CXCL12 stimulation, and alters the lateral mobility and spatial organization of CXCR4 when coexpressed"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 23 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:8000006` (2 mentions) - the report calls it "MONDO"; MONDO calls it **WHIM syndrome 1**
- `HP:0001875` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased total neutrophil count**
- `HP:0002718` (1 mention) - the report calls it "Symptom/sign"; HP calls it **Recurrent bacterial infections**
- `HP:0006532` (1 mention) - the report calls it "Sign"; HP calls it **Recurrent pneumonia**
- `HP:0002110` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Bronchiectasis**
- `HP:0200043` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Verrucae**
- `HP:0002664` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Neoplasm**
- `HP:0002720` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased circulating IgA concentration**
- `HP:0001627` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Abnormal heart morphology**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0002031` (2 mentions) - the report calls it "GPCR internalization"; GO calls it **G protein-coupled receptor internalization**
- `GO:0007204` (1 mention) - the report calls it "positive regulation of cytosolic calcium"; GO calls it **positive regulation of cytosolic calcium ion concentration**
- `GO:0070098` (1 mention) - the report calls it "chemokine-mediated signaling"; GO calls it **chemokine-mediated signaling pathway**
- `CL:0000625` (1 mention) - the report calls it "CD8⁺ αβ T cell"; CL calls it **CD8-positive, alpha-beta T cell**
- `CL:0000624` (1 mention) - the report calls it "CD4⁺ αβ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `UBERON:0002371` (1 mention) - the report calls it "Primary:** Bone marrow"; UBERON calls it **bone marrow**
- `UBERON:0002048` (1 mention) - the report calls it "Secondary:** Lung"; UBERON calls it **lung**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.