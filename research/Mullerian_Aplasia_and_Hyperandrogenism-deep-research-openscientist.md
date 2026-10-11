---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-08T13:33:01.105812'
end_time: '2026-10-08T13:47:51.703156'
duration_seconds: 890.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mullerian Aplasia and Hyperandrogenism
  mondo_id: MONDO:0008019
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
citation_count: 22
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 14
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:9989404
  relevance_assessed: 22
  on_topic: 9
  off_topic: 1
  off_topic_references:
  - PMID:35455528
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 26
  verified: 24
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 2
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0008019
    reported_labels:
    - MONDO
    ontology_label: mullerian aplasia and hyperandrogenism
  - term_id: HP:0000786
    reported_labels:
    - Symptom/sign
    ontology_label: Primary amenorrhea
  - term_id: HP:0000858
    reported_labels:
    - Hyperandrogenism
    ontology_label: Irregular menstruation
  - term_id: HP:0001007
    reported_labels:
    - Physical manifestation
    ontology_label: Hirsutism
  - term_id: HP:0001061
    reported_labels:
    - Physical manifestation
    ontology_label: Acne
  - term_id: HP:0008222
    reported_labels:
    - Decreased ovarian reserve
    ontology_label: Female infertility
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mullerian_Aplasia_and_Hyperandrogenism-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mullerian_Aplasia_and_Hyperandrogenism-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mullerian Aplasia and Hyperandrogenism
- **MONDO ID:** MONDO:0008019 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mullerian Aplasia and Hyperandrogenism** covering all of the
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

# Müllerian Aplasia and Hyperandrogenism (MONDO:0008019 / OMIM #158330): A Comprehensive Disease Characterization Report

## Summary

**Müllerian Aplasia and Hyperandrogenism** (OMIM #158330; MONDO:0008019) is a rare **Mendelian, autosomal-dominant** disorder caused by **heterozygous loss-of-function (missense) variants in *WNT4*** (1p36.12). In 46,XX women it produces a distinctive dyad: **congenital aplasia of the uterus and upper vagina** (Müllerian agenesis) combined with **clinical and biochemical androgen excess**. It represents the "atypical," hyperandrogenic form of Mayer-Rokitansky-Küster-Hauser (MRKH) syndrome and is, to date, the only MRKH subtype with an established single-gene (Mendelian) cause. The index description was a landmark 2004 report of an 18-year-old 46,XX woman with primary amenorrhea, absent Müllerian derivatives, unilateral renal agenesis, and androgen excess, carrying a heterozygous *WNT4* loss-of-function allele ([PMID: 15317892](https://pubmed.ncbi.nlm.nih.gov/15317892/)).

Mechanistically, WNT4 serves a dual developmental role in the female reproductive tract. During embryogenesis it is required for **formation of the Müllerian (paramesonephric) duct**; in the differentiating ovary it **represses steroidogenic enzyme expression**, thereby suppressing ectopic androgen synthesis. Loss of WNT4 function therefore simultaneously **abolishes Müllerian-duct development** and **de-represses ovarian androgen biosynthesis** (via re-expression of CYP17A1/17α-hydroxylase and HSD3B2/3β-hydroxysteroid dehydrogenase), explaining the coincidence of Müllerian aplasia and hyperandrogenism in a single gene defect. This mechanism is strongly supported by the *Wnt4*-null mouse, in which females lack the Müllerian duct, retain the Wolffian duct, and ectopically activate testosterone biosynthesis — a phenotype the human disorder was described as "remarkably similar to" ([PMID: 9989404](https://pubmed.ncbi.nlm.nih.gov/9989404/); [PMID: 15317892](https://pubmed.ncbi.nlm.nih.gov/15317892/)).

The disorder is **non-lethal**, with the principal burden being **absolute uterine-factor infertility** and substantial **psychosocial impact** (elevated anxiety/depression, impaired sexual function). Management is **symptomatic and multidisciplinary**: non-surgical vaginal dilation (first-line) or surgical neovagina creation, anti-androgen therapy for androgen excess, assisted reproduction (IVF with gestational surrogacy, and increasingly uterine transplantation), and psychological support. It must be carefully distinguished from the dominant disorder's **recessive, embryonic/perinatally lethal counterpart — SERKAL syndrome**, caused by **biallelic (homozygous) *WNT4* mutation**, which features 46,XX female-to-male sex reversal with renal, adrenal, and lung dysgenesis ([PMID: 18179883](https://pubmed.ncbi.nlm.nih.gov/18179883/)).

---

## 1. Disease Information

**Overview.** Müllerian Aplasia and Hyperandrogenism is a congenital disorder of the female reproductive tract in genotypic (46,XX) females, defined by the combination of **Müllerian aplasia** (absence/hypoplasia of the uterus and upper vagina — "uterovaginal aplasia") and **hyperandrogenism** (clinical signs such as hirsutism/acne and/or biochemical elevation of androgens such as testosterone). It is nested within the broader **MRKH / Müllerian agenesis** spectrum but is set apart by androgen excess and by its monogenic *WNT4* etiology. Ovaries are present and typically of normal size on imaging, but are the source of excess androgens; secondary sexual characteristics are otherwise female. Patients characteristically present at adolescence with **primary amenorrhea** and are found to have a 46,XX karyotype.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #158330 ("Müllerian aplasia and hyperandrogenism"; WNT4-related) |
| MONDO | MONDO:0008019 |
| Gene (HGNC) | *WNT4*, HGNC:12783; locus 1p36.12; gene OMIM *603490 |
| Orphanet | Within the MRKH / Müllerian aplasia spectrum (atypical/hyperandrogenic form) |
| ICD-10 | Q51.x (congenital malformations of uterus/cervix); vaginal agenesis Q52.x |
| ICD-11 | LA14 (structural developmental anomalies of female genitalia) |
| MeSH | 46,XX Disorders of Sex Development; Müllerian aplasia / Mullerian ducts |

**Synonyms / alternative names.** Müllerian aplasia and hyperandrogenism; *WNT4* deficiency; atypical MRKH syndrome with hyperandrogenism; MRKH-like syndrome with Müllerian-duct regression and virilization; WNT4 Müllerian aplasia. (Note: the classic, androgen-normal form is "typical MRKH" and is genetically distinct — see §10.)

**Source of information.** The characterization derives predominantly from **aggregated disease-level resources** (OMIM, review articles) and a small number of **individual-patient reports and small cohorts** (the index case and subsequent *WNT4*-mutation-positive adolescents), supplemented by **model-organism** (mouse) and **in-vitro functional** data. There is no large EHR-derived cohort specific to the *WNT4* hyperandrogenic form; EHR-based data exist for the broader Müllerian aplasia category ([PMID: 39391975](https://pubmed.ncbi.nlm.nih.gov/39391975/)).

---

## 2. Etiology

**Primary cause (genetic).** The disorder is caused by **heterozygous loss-of-function missense variants in *WNT4***. The index patient carried p.Glu226Gly (p.E226G) ([PMID: 15317892](https://pubmed.ncbi.nlm.nih.gov/15317892/)); subsequently reported variants include p.Leu12Pro (p.L12P, exon 1; [PMID: 18182450](https://pubmed.ncbi.nlm.nih.gov/18182450/)) and p.Ala233Thr (p.A233T; [PMID: 21377155](https://pubmed.ncbi.nlm.nih.gov/21377155/)). These are **germline**, **dominant-acting** alleles producing a partial loss of WNT4 signalling.

**Genetic risk factors.** The causal variants themselves are the risk determinant; no additional susceptibility loci or validated modifier genes have been established for the hyperandrogenic *WNT4* form. Within the broader MRKH spectrum, *WNT4* is the only gene with mutations definitively linked to an atypical (hyperandrogenic) phenotype: "The only known MRKH-associated mutations are located within the WNT4 gene and lead to an atypical form of MRKH syndrome associated with clinical and biochemical hyperandrogenism" ([PMID: 24641817](https://pubmed.ncbi.nlm.nih.gov/24641817/)).

**Environmental risk factors.** None established as causal for the Mendelian *WNT4* form. For MRKH broadly, no reproducible environmental cause has been identified.

**Protective factors.** No genetic or environmental protective factors have been defined. Mechanistically, retention of one functional *WNT4* allele with sufficient residual signalling may mitigate severity (variable expressivity; see §9), but this is inferred rather than demonstrated.

**Gene–environment interactions.** None documented. The phenotype is driven by the monogenic lesion; environmental modulation of androgen expression has not been characterized in this disorder.

---

## 3. Phenotypes

Phenotypes fall into two cardinal domains — **structural (Müllerian aplasia)** and **endocrine (hyperandrogenism)** — plus extragenital features (chiefly renal).

| Phenotype | Type | HPO suggestion | Onset | Frequency / notes |
|---|---|---|---|---|
| Primary amenorrhea | Symptom/sign | HP:0000786 | Adolescence (presenting) | Near-universal presenting feature |
| Aplasia/hypoplasia of uterus | Physical malformation | HP:0000013 (Hypoplasia of the uterus) | Congenital | Defining; ranges hypoplastic→absent |
| Vaginal aplasia (absent upper vagina) | Physical malformation | HP:0000148 (Vaginal atresia) | Congenital | Defining |
| Hyperandrogenism (clinical) | Clinical sign | HP:0000858 (Hyperandrogenism) | Peripubertal/adult | Defining of this subtype |
| Hirsutism | Physical manifestation | HP:0001007 | Peripubertal/adult | Variable |
| Acne (can be severe) | Physical manifestation | HP:0001061 | Peripubertal | Present in index/variant carriers; acne overall less frequent in MRKH (24.6%) |
| Elevated serum testosterone | Lab abnormality | HP:0030348 (Increased circulating androgen level) | Peripubertal/adult | e.g., 1.8 vs 1.2 nmol/L in a carrier |
| Unilateral renal agenesis | Physical malformation | HP:0000122 / HP:0000104 | Congenital | In index case; renal anomalies ~15.5% in MRKH |
| Follicle depletion / ovarian dysfunction | Lab/structural | HP:0008222 (Decreased ovarian reserve) | Variable | Reported in L12P carrier |

**Characteristics.**
- **Age of onset:** The structural defects are **congenital**; clinical recognition is typically at **adolescence** when primary amenorrhea prompts evaluation. Hyperandrogenic signs emerge peri-/post-pubertally.
- **Severity:** **Variable.** Uterine involvement ranges from hypoplasia to complete absence; androgen excess ranges from biochemical only to clinically overt (severe acne, hirsutism).
- **Progression:** The structural anomaly is **stable (non-progressive)**; androgen-related manifestations are **chronic** and may be modulated by therapy.
- **Frequency among affected:** Müllerian aplasia and androgen excess are the defining, essentially obligate features of this subtype; extragenital (renal) involvement is present in a subset.

**Quality-of-life impact.** The dominant QoL burdens are **infertility-related distress** and **sexual dysfunction** (dyspareunia, impaired arousal/lubrication/orgasm), plus psychological morbidity. A systematic review of MRKH reported that "MRKH could be associated with a higher prevalence of anxiety and depression symptoms and social insecurity compared with women of a similar age without the condition," and found impaired mental-health–related QoL though physical-health–related QoL was not affected ([PMID: 35455528](https://pubmed.ncbi.nlm.nih.gov/35455528/)). An EHR cohort found anxiety/depressive disorders ~2× higher than male referents in Müllerian aplasia ([PMID: 39391975](https://pubmed.ncbi.nlm.nih.gov/39391975/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** ***WNT4*** (Wnt family member 4), HGNC:12783, locus **1p36.12**, gene OMIM *603490. WNT4 is a secreted glycoprotein ligand of the Wnt signalling family.

**Pathogenic variants (germline, heterozygous).**

| Variant (protein) | Exon | Source | Functional consequence |
|---|---|---|---|
| p.E226G | — | Index case, [PMID: 15317892](https://pubmed.ncbi.nlm.nih.gov/15317892/) | Loss-of-function |
| p.L12P | exon 1 | [PMID: 18182450](https://pubmed.ncbi.nlm.nih.gov/18182450/); 1/28 MRKH girls, absent in 100 controls | ↑ expression of HSD3B2 and CYP17A1 (de-repression) |
| p.A233T | — | [PMID: 21377155](https://pubmed.ncbi.nlm.nih.gov/21377155/) | Partial loss of repression; abnormal CYP17A1 re-expression |

- **Variant classification (ACMG/AMP):** The recurrent/characterized missense alleles behave as **pathogenic/likely pathogenic** on the strength of functional assays, segregation, and absence in controls; unselected MRKH screening yields many variants of uncertain significance, and the diagnostic yield of *WNT4* in unselected MRKH is low (~1/28) ([PMID: 18182450](https://pubmed.ncbi.nlm.nih.gov/18182450/)).
- **Variant type/class:** **Missense** (functional loss-of-function), not gross structural.
- **Allele frequency:** Pathogenic alleles are **private/rare**, absent from control panels (e.g., absent in 100 controls for L12P) and population databases.
- **Somatic vs germline:** **Germline.**
- **Functional consequence:** **Loss of function** — reduced WNT4/β-catenin signalling. WNT4 loss downregulates WNT4-dependent inhibition of β-catenin degradation ([PMID: 18179883](https://pubmed.ncbi.nlm.nih.gov/18179883/)), and de-represses ovarian steroidogenic enzymes: "This mutant partially lacks the capability to repress ovarian steroidogenic enzymes, with abnormal expression of 17α-hydroxylase" ([PMID: 21377155](https://pubmed.ncbi.nlm.nih.gov/21377155/)); and the L12P mutation "induces significantly increased expression of the enzymes involved in androgen biosynthesis (3beta-hydroxysteroid dehydrogenase and 17alpha-hydroxylase)" ([PMID: 18182450](https://pubmed.ncbi.nlm.nih.gov/18182450/)).

**Modifier genes.** None validated for this disorder. Pathway partners RSPO1 and FOXL2 are mechanistically related (see §6) but are not established modifiers of the *WNT4* phenotype.

**Epigenetic information.** No disease-specific epigenetic signature has been defined for Müllerian aplasia and hyperandrogenism. (Of pathway interest, DNA methylation via DNMT1 regulates nephron progenitor renewal in kidney development — [PMID: 30518531](https://pubmed.ncbi.nlm.nih.gov/30518531/) — but this is not a documented mechanism in this disorder.)

**Chromosomal abnormalities.** The hyperandrogenic *WNT4* form is a **point-mutation (single-gene)** disorder; it is not caused by aneuploidy or large rearrangements. (By contrast, portions of the broader MRKH spectrum involve copy-number variants, e.g., 16p11.2 and 17q12 — not specific to the *WNT4* subtype.)

---

## 5. Environmental Information

- **Environmental factors:** None established as causal.
- **Lifestyle factors:** None established as causal; weight/obesity may modulate androgenic phenotype expression generally but is not a defined cause here.
- **Infectious agents:** Not applicable — this is a genetic developmental disorder with no infectious etiology.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous loss-of-function missense variant in *WNT4*** (e.g., p.E226G, p.L12P, p.A233T) **reduces** secreted WNT4 ligand activity.
2. Reduced WNT4 **decreases** WNT4-dependent inhibition of β-catenin degradation, which **lowers** canonical Wnt/β-catenin signalling in the developing reproductive tract (demonstrated in vitro — [PMID: 18179883](https://pubmed.ncbi.nlm.nih.gov/18179883/)).
3. **Branch A (structural):** Loss of WNT4 signalling in the paramesonephric mesenchyme **prevents formation of the Müllerian (paramesonephric) duct**, which **results in** uterine and upper-vaginal aplasia (→ primary amenorrhea, absolute uterine-factor infertility). Demonstrated in mouse: "the Mullerian duct is absent while the Wolffian duct continues to develop" ([PMID: 9989404](https://pubmed.ncbi.nlm.nih.gov/9989404/)).
4. **Branch B (endocrine):** Loss of WNT4's repressive action in the differentiating ovary **de-represses ovarian steroidogenic enzymes** — **abnormal re-expression of CYP17A1 (17α-hydroxylase)** and increased **HSD3B2 (3β-hydroxysteroid dehydrogenase)** — which **leads to** ectopic/elevated ovarian androgen (testosterone) biosynthesis (→ hyperandrogenism, hirsutism, acne). Demonstrated functionally in OVCAR3 cells for p.A233T ([PMID: 21377155](https://pubmed.ncbi.nlm.nih.gov/21377155/)) and for p.L12P ([PMID: 18182450](https://pubmed.ncbi.nlm.nih.gov/18182450/)); in mouse, "Wnt-4 in the developing ovary appears to suppress the development of Leydig cells; consequently, Wnt-4-mutant females ectopically activate testosterone biosynthesis" ([PMID: 9989404](https://pubmed.ncbi.nlm.nih.gov/9989404/)).
5. **Branch C (renal, subset):** Because WNT4 is also required in nephrogenesis (Wnt4-null mutants fail to form nephron structures — [PMID: 41358813](https://pubmed.ncbi.nlm.nih.gov/41358813/)), the lesion can **result in** renal anomalies such as unilateral renal agenesis in a subset of patients ([PMID: 15317892](https://pubmed.ncbi.nlm.nih.gov/15317892/)).
6. The convergence of Branches A + B in a 46,XX woman **produces** the clinical syndrome: uterovaginal aplasia with androgen excess.

### Detailed mechanism

**Molecular pathways.** WNT4 acts within the **canonical Wnt/β-catenin pro-ovarian pathway** together with **RSPO1** (R-spondin-1) and **FOXL2**, which collectively promote ovarian fate and antagonize the male (SRY/SOX9) testis-determining program. "The male pathway is opposed by the expression of two signals, WNT4 and R-SPONDIN-1 (RSPO1), that promote the ovarian fate and block testis development. Both of these ligands can activate the canonical Wnt signaling pathway" ([PMID: 18617533](https://pubmed.ncbi.nlm.nih.gov/18617533/)). "Female sex-determining genes RSPO1, Wnt4/β-catenin and Foxl2, are involved in the formation of female genitalia and the maintenance of female ovarian development" ([PMID: 27481580](https://pubmed.ncbi.nlm.nih.gov/27481580/)). Ovarian somatic differentiation is regulated by FOXL2 and the β-catenin pathway activated by Wnt4 and Rspo1 ([PMID: 22251856](https://pubmed.ncbi.nlm.nih.gov/22251856/)). Suggested pathway/GO terms: **Wnt signaling pathway (GO:0016055)**, **canonical Wnt signaling pathway (GO:0060070)**, **female sex differentiation (GO:0046660)**, **Müllerian duct development (GO:0061205)**, **negative regulation of steroid biosynthetic process (GO:0010894)**.

**Cellular processes.** Developmental patterning and lineage specification — **Müllerian duct formation**, **ovarian somatic (pre-granulosa) differentiation**, and **suppression of ectopic steroidogenic (Leydig-like) cell development**. Loss leads to failure of duct morphogenesis (Branch A) and inappropriate steroidogenic gene expression (Branch B).

**Protein dysfunction.** Missense WNT4 variants cause **loss of function** (reduced ligand signalling), not aggregation or classic dominant-negative gain; the heterozygous dominant phenotype reflects **haploinsufficiency/partial loss** sufficient to perturb dosage-sensitive developmental and repressive functions.

**Metabolic/biochemical abnormalities.** The core biochemical defect is **de-repression of steroidogenic enzymes**: **CYP17A1 (17α-hydroxylase/17,20-lyase)** and **HSD3B2 (3β-HSD)**, driving **androgen (testosterone) overproduction** (CHEBI: testosterone CHEBI:17347; androgen CHEBI:50113).

**Immune system / tissue damage.** Not implicated — this is a developmental/endocrine disorder, not inflammatory, fibrotic, or ischemic.

**Molecular profiling.** In-vitro transcriptional assays (OVCAR3, steroidogenic cell models) demonstrate the enzyme de-repression; no large-scale transcriptomic/proteomic/metabolomic atlas exists specific to this disorder.

**Cell types (CL suggestions):** ovarian granulosa cell (CL:0000501), theca/steroid-hormone-secreting cell, Müllerian duct epithelial/mesenchymal cells, nephron progenitor cell (for renal branch).

```
 WNT4 LOF (het missense)
        │  ↓ canonical Wnt/β-catenin signalling
        ├──► Müllerian duct NOT formed ───► uterine + upper-vaginal aplasia ─► primary amenorrhea, UFI
        ├──► loss of ovarian repression ──► CYP17A1↑ / HSD3B2↑ ─► ↑androgens ─► hirsutism, acne, ↑testosterone
        └──► nephron defect (subset) ─────► renal agenesis/anomaly
```

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** Uterus (UBERON:0000995) and upper vagina (UBERON:0000996) — aplastic/hypoplastic. Ovaries (UBERON:0000992) are present but functionally abnormal (androgen over-secreting).
- **Secondary / associated:** Kidney (UBERON:0002113) — unilateral renal agenesis in a subset. Skin/pilosebaceous unit secondarily affected by androgen excess (hirsutism, acne).
- **Body systems:** **Reproductive/genitourinary** (primary) and **endocrine** (androgen axis); **renal/urinary** in a subset.

**Tissue and cell level.** Müllerian-duct–derived **epithelial and mesenchymal** tissue (fails to develop); **ovarian somatic cells** (granulosa/theca-steroidogenic lineage) exhibit aberrant steroidogenesis. Suggested CL terms: granulosa cell (CL:0000501), steroidogenic/theca cell.

**Subcellular level.** **Mitochondria** and **smooth endoplasmic reticulum** (sites of steroidogenesis — CYP17A1 resides in the ER); **nucleus** (transcriptional de-repression of steroidogenic genes); **plasma membrane/extracellular** (WNT4 ligand secretion and receptor signalling). GO cellular-component suggestions: extracellular space (GO:0005615), endoplasmic reticulum membrane (GO:0005789).

**Localization / lateralization.** Uterovaginal aplasia is **midline/bilateral** (a single fused midline structure fails to form). Renal agenesis, when present, is typically **unilateral** ([PMID: 15317892](https://pubmed.ncbi.nlm.nih.gov/15317892/)).

---

## 8. Temporal Development

- **Onset:** Structural anomalies are **congenital**; clinical presentation is at **adolescence** (primary amenorrhea, often ages 14–18). Onset pattern is **insidious/chronic** — the anomaly is present from birth but detected when menarche fails.
- **Progression:** The anatomical defect is **stable and non-progressive**. Hyperandrogenism is **chronic**, variable, and treatment-responsive. There are no formal disease "stages."
- **Course / duration:** **Chronic, lifelong** congenital condition.
- **Patterns:** No spontaneous remission of the structural defect; androgenic features can be controlled (treatment-induced improvement). **Critical periods:** the vulnerable developmental window is **embryonic reproductive-tract morphogenesis** (Müllerian duct and ovarian differentiation); the therapeutic windows are adolescence/adulthood for neovagina creation and fertility interventions.

---

## 9. Inheritance and Population

**Epidemiology.** Precise prevalence of the *WNT4* hyperandrogenic subtype is **not established** (very rare; described in case reports and small cohorts). For context, **MRKH overall affects ~1:4,500 women** ([PMID: 28434104](https://pubmed.ncbi.nlm.nih.gov/28434104/)) and is "the second most common cause of primary amenorrhea, accounting for 10%-15% of cases" ([PMID: 41636313](https://pubmed.ncbi.nlm.nih.gov/41636313/)). Hyperandrogenemia is biochemically common across MRKH cohorts (60.1% in one series) but overt acne (24.6%) and PCOS are relatively infrequent, and *WNT4* mutations account for only the rare atypical, genetically-defined subset ([PMID: 24641817](https://pubmed.ncbi.nlm.nih.gov/24641817/)).

**For genetic etiology.**
- **Inheritance pattern:** **Autosomal dominant** (heterozygous *WNT4* LOF). Contrast with the **autosomal recessive** biallelic-*WNT4* disorder SERKAL ([PMID: 18179883](https://pubmed.ncbi.nlm.nih.gov/18179883/)).
- **Penetrance / expressivity:** **Variable expressivity**; most reported variants arise as rare/private alleles. Penetrance is presumed high for the structural defect in carriers described, but formal estimates are lacking given the small number of families.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects / consanguinity:** Not documented for the dominant form. (Consanguinity is relevant to recessive SERKAL.)
- **Carrier frequency:** Pathogenic alleles are **private/rare**; no meaningful population carrier frequency for the dominant disorder.

**Population demographics.**
- **Affected populations:** Reported across multiple populations; no established ethnic predilection for the *WNT4* subtype.
- **Geographic distribution:** No endemic pattern (Mendelian, globally distributed).
- **Sex ratio:** Affects **46,XX (phenotypic females)** — effectively female-only presentation given the reproductive-tract phenotype.
- **Age distribution:** Diagnosed predominantly in **adolescence/young adulthood**.

---

## 10. Diagnostics

**Clinical tests.**
- **Laboratory:** Karyotype confirming **46,XX**; **serum androgens** (testosterone — elevated, e.g., 1.8 vs control 1.2 nmol/L in a carrier; also free testosterone, androstenedione, DHEAS), gonadotropins (FSH/LH), estradiol, AMH (ovarian reserve); 17-hydroxyprogesterone to screen for CAH. LOINC-codable panels for testosterone and gonadotropins.
- **Biomarkers:** Elevated circulating androgens are the key biochemical discriminator; *WNT4* mutation is the molecular biomarker.
- **Imaging:** **Pelvic ultrasound and MRI** are the mainstay to document uterovaginal aplasia and confirm presence of ovaries (ultrasound and MRI are the main diagnostic techniques — [PMID: 28434104](https://pubmed.ncbi.nlm.nih.gov/28434104/)). Renal imaging to detect associated renal agenesis.
- **Biopsy/pathology:** Not routinely required for diagnosis.

**Genetic testing.** Recommended approach: confirm 46,XX karyotype, then **targeted *WNT4* sequencing** (single-gene) or an MRKH/DSD **gene panel**; **WES/WGS** are useful for atypical/syndromic cases or when panels are negative. Chromosomal microarray can detect CNVs relevant to the broader MRKH spectrum (not the *WNT4* point-mutation form). Yield of *WNT4* in unselected MRKH is low (~1/28), so testing is highest-yield in **hyperandrogenic** MRKH ([PMID: 18182450](https://pubmed.ncbi.nlm.nih.gov/18182450/)).

**Clinical criteria & differential diagnosis.** Diagnosis rests on 46,XX uterovaginal aplasia **plus androgen excess**. Key differentials:

| Condition | Karyotype | Uterus | Gonads | Androgens | *WNT4* | Discriminator |
|---|---|---|---|---|---|---|
| **WNT4 Müllerian aplasia + hyperandrogenism** | 46,XX | Absent/hypoplastic | Ovaries | **High** | Mutated | Androgen excess + *WNT4* |
| Classic (typical) MRKH | 46,XX | Absent | Ovaries | Normal | Negative | Normal androgens |
| CAIS (complete androgen insensitivity) | 46,XY | Absent | Testes | — (resistance) | — | 46,XY, AR mutation, no ovaries |
| MURCS association | 46,XX | Absent | Ovaries | ± | **Not** causal | Skeletal/renal; *WNT4* excluded ([PMID: 24356390](https://pubmed.ncbi.nlm.nih.gov/24356390/)) |
| PCOS / androgen-secreting tumor / CAH | 46,XX | Present | Ovaries/adrenal | High | — | Uterus present; distinct endocrine profile |

A MURCS patient with obesity and hyperandrogenism showed no exonic *WNT4* mutation: "Our finding excludes WNT4 gene as a candidate for MURCS association" ([PMID: 24356390](https://pubmed.ncbi.nlm.nih.gov/24356390/)).

**Screening.** No population newborn screening. **Cascade genetic testing** and genetic counseling are appropriate for families with an identified *WNT4* variant.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** The dominant disorder is **non-lethal** with **normal life expectancy**; it does not directly increase mortality. (This contrasts sharply with recessive SERKAL, which is embryonic/perinatally lethal — [PMID: 18179883](https://pubmed.ncbi.nlm.nih.gov/18179883/).)
- **Morbidity / function:** Principal morbidities are **absolute uterine-factor infertility**, **sexual dysfunction** from vaginal aplasia, **androgen-excess manifestations** (hirsutism, acne), and **psychosocial morbidity**. MRKH systematic review: higher anxiety/depression and social insecurity; impaired sexual function; mental- but not physical-health QoL affected ([PMID: 35455528](https://pubmed.ncbi.nlm.nih.gov/35455528/)).
- **Complications:** Psychological distress; potential complications of neovaginal/surgical interventions; renal sequelae if significant renal anomaly present.
- **Recovery potential:** The structural defect is not reversible, but **functional outcomes are good** with vaginal dilation/vaginoplasty (satisfactory sexual function) and ART; androgen excess is manageable pharmacologically.
- **Prognostic factors:** Degree of uterine/renal involvement, severity of androgen excess, and access to multidisciplinary care and psychological support.

---

## 12. Treatment

Management is **symptomatic, multidisciplinary, and individualized** (NCIT: Supportive Care).

- **Neovagina creation (first-line non-surgical):** **Vaginal dilation** is the recommended initial approach. "Several non-surgical and surgical procedures have been reported for the creation of a functional neovagina; in general, non-surgical treatment should be the first initially pursued" ([PMID: 28434104](https://pubmed.ncbi.nlm.nih.gov/28434104/)). Systematic review: "vaginal dilation is a viable initial treatment option for women with MRKH syndrome" ([PMID: 37994266](https://pubmed.ncbi.nlm.nih.gov/37994266/)). NCIT: dilation therapy.
- **Surgical vaginoplasty:** Reserved for dilation failure/preference — e.g., Vecchietti (including minimally invasive single-port laparoscopic), McIndoe, or bowel vaginoplasty; a modified Vecchietti achieved a ~9 cm neovagina ([PMID: 33461758](https://pubmed.ncbi.nlm.nih.gov/33461758/)). NCIT: vaginoplasty.
- **Pharmacotherapy for hyperandrogenism:** **Anti-androgens** (spironolactone, cyproterone acetate) and combined estrogen–progestin or dermatologic therapy for hirsutism/acne; hormone management as indicated. (Mechanism-directed at androgen excess arising from CYP17A1/HSD3B2 de-repression.) NCIT: anti-androgen therapy.
- **Fertility / ART:** Ovaries are functional, enabling **IVF with gestational surrogacy**; **uterine transplantation** is an emerging option restoring the possibility of gestation ([PMID: 28434104](https://pubmed.ncbi.nlm.nih.gov/28434104/)); psychosocial outcomes of UTx candidacy are being characterized ([PMID: 39388911](https://pubmed.ncbi.nlm.nih.gov/39388911/); [PMID: 39324432](https://pubmed.ncbi.nlm.nih.gov/39324432/)).
- **Psychological support:** Integral — counseling and mental-health support before/after interventions ([PMID: 28434104](https://pubmed.ncbi.nlm.nih.gov/28434104/); [PMID: 39280286](https://pubmed.ncbi.nlm.nih.gov/39280286/)).
- **Advanced / experimental therapeutics:** No gene, cell, RNA, or targeted molecular therapies exist for this disorder; care is anatomic and endocrine.
- **Pharmacogenomics:** None established.

---

## 13. Prevention

- **Primary prevention:** Not possible for this congenital genetic disorder. **Genetic counseling** for families with an identified *WNT4* variant informs reproductive decision-making.
- **Secondary prevention:** **Early recognition** of primary amenorrhea with prompt imaging and endocrine/genetic work-up enables timely intervention and psychological support.
- **Tertiary prevention:** Management of androgen excess, functional restoration (neovagina), fertility planning, and mental-health care to prevent complications and improve QoL.
- **Genetic screening:** Cascade testing and, where a familial variant is known, options including **preimplantation/prenatal genetic testing** can be discussed; carrier/preconception counseling is relevant particularly to distinguish and avoid the recessive SERKAL scenario in consanguineous unions.
- **Immunization / public-health / environmental measures:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *WNT4* is highly conserved; the mouse ortholog **Wnt4** (NCBI Gene 22417) is the principal comparative model. Human *WNT4* NCBI Gene 54361. Species: *Homo sapiens* (NCBI:txid9606), *Mus musculus* (NCBI:txid10090).
- **Natural disease in other species:** No well-characterized spontaneous animal disease catalogued as an exact ortholog of this syndrome; the knowledge base is **engineered model organisms** rather than naturally occurring veterinary disease.
- **Comparative biology:** The **Wnt4-null mouse** closely mirrors the human disorder — "Wnt-4-mutant females are masculinized-the Mullerian duct is absent while the Wolffian duct continues to develop" ([PMID: 9989404](https://pubmed.ncbi.nlm.nih.gov/9989404/)) — evidencing strong **evolutionary conservation** of WNT4's role in Müllerian development and androgen repression.
- **Transmission / zoonosis:** Not applicable (non-infectious, genetic).

---

## 15. Model Organisms

- **Model type:** **Mammalian — mouse (*Mus musculus*)**, principally the **Wnt4 knockout (null)**. In-vitro steroidogenic cell models (e.g., OVCAR3) are used for functional variant assays.
- **Genetic models:** Constitutive **Wnt4 knockout**; pathway-related conditional β-catenin loss/gain-of-function models inform downstream biology (e.g., β-catenin controls nephron segmentation — [PMID: 31685872](https://pubmed.ncbi.nlm.nih.gov/31685872/)).
- **Phenotype recapitulation:** **High.** The female Wnt4-null mouse reproduces the **core human features**: absent Müllerian duct (→ uterovaginal aplasia), retained Wolffian duct, **virilization with ectopic ovarian testosterone synthesis** ([PMID: 9989404](https://pubmed.ncbi.nlm.nih.gov/9989404/)), and **renal/nephron defects** ([PMID: 41358813](https://pubmed.ncbi.nlm.nih.gov/41358813/)). The human disorder was described as "remarkably similar to that of female Wnt4-knockout mice" ([PMID: 15317892](https://pubmed.ncbi.nlm.nih.gov/15317892/)).
- **Limitations:** Homozygous null mice model complete loss (closer to recessive SERKAL severity) whereas the human dominant disorder reflects **partial/heterozygous** loss; species differences in ovarian steroidogenesis regulation and the human-specific psychosocial dimension are not captured.
- **Applications / resources:** Dissecting WNT4 roles in Müllerian morphogenesis, ovarian androgen repression, and nephrogenesis. Resources: **MGI** (Wnt4), IMPC/IMSR.

---

## Mechanistic Model / Interpretation (Synthesis)

The disorder is best understood as the consequence of **partial loss of a single dosage-sensitive developmental signal, WNT4**, whose two independent functions in the female gonad/tract are **simultaneously** disrupted. In normal development WNT4 (acting with RSPO1/β-catenin and FOXL2) does two things that are both lost in patients: (1) it **drives Müllerian-duct formation**, and (2) it **keeps ovarian steroidogenic enzymes switched off**. Removing WNT4 therefore yields the otherwise paradoxical combination of a **missing uterus** and an **androgen-producing ovary** in the same 46,XX individual — a phenotype difficult to explain by any mechanism other than a shared upstream regulator. The convergence of human genetics (recurrent LOF missense alleles), in-vitro enzyme de-repression (CYP17A1/HSD3B2), and a faithful mouse knockout provides a rare, tightly-closed causal loop for a Mendelian reproductive disorder.

The **dosage axis** is central to nosology: **one** defective allele → viable dominant Müllerian aplasia + hyperandrogenism; **two** defective alleles → lethal recessive SERKAL (46,XX sex reversal with renal/adrenal/lung dysgenesis). This gene-dosage spectrum should be emphasized in any knowledge-base entry and in genetic counseling.

```
Dosage spectrum of WNT4 loss
  0 LOF alleles → normal female development
  1 LOF allele  → Müllerian aplasia + hyperandrogenism (OMIM 158330, AD, viable)
  2 LOF alleles → SERKAL syndrome (AR, 46,XX sex reversal, lethal)
```

---

## Evidence Base

| PMID | Role in this report | Evidence type |
|---|---|---|
| [15317892](https://pubmed.ncbi.nlm.nih.gov/15317892/) | Index case defining the disorder; heterozygous *WNT4* LOF; "remarkably similar" to Wnt4-null mouse | Human clinical |
| [18182450](https://pubmed.ncbi.nlm.nih.gov/18182450/) | p.L12P variant; functional de-repression of HSD3B2 + CYP17A1; low yield in unselected MRKH | Human + in vitro |
| [21377155](https://pubmed.ncbi.nlm.nih.gov/21377155/) | p.A233T variant; abnormal CYP17A1 re-expression in OVCAR3; atypical MRKH cohort | Human + in vitro |
| [9989404](https://pubmed.ncbi.nlm.nih.gov/9989404/) | Wnt4-null mouse: Müllerian absence + ectopic testosterone — defines dual mechanism | Model organism |
| [18179883](https://pubmed.ncbi.nlm.nih.gov/18179883/) | Biallelic *WNT4* = SERKAL (AR, lethal); β-catenin degradation link | Human + mechanism |
| [24641817](https://pubmed.ncbi.nlm.nih.gov/24641817/) | WNT4 = only MRKH-associated mutation → atypical hyperandrogenic form; hyperandrogenemia 60.1% | Human clinical |
| [28434104](https://pubmed.ncbi.nlm.nih.gov/28434104/) | MRKH review: ~1:4500; US/MRI diagnosis; management; WNT4 in MRKH-like hyperandrogenism | Review |
| [41636313](https://pubmed.ncbi.nlm.nih.gov/41636313/) | Epidemiology: MRKH ~10–15% of primary amenorrhea; renal anomalies ~15.5% | Human clinical |
| [18617533](https://pubmed.ncbi.nlm.nih.gov/18617533/) | WNT4/RSPO1 canonical Wnt ligands promote ovarian fate, block testis | Model/mechanism |
| [27481580](https://pubmed.ncbi.nlm.nih.gov/27481580/) | RSPO1/Wnt4/β-catenin/Foxl2 in female genitalia & ovarian maintenance | Review |
| [22251856](https://pubmed.ncbi.nlm.nih.gov/22251856/) | Ovarian somatic differentiation via FOXL2 + Wnt4/Rspo1 β-catenin | Review |
| [41358813](https://pubmed.ncbi.nlm.nih.gov/41358813/) | Wnt4-null mutants fail nephron formation (renal branch) | Model organism |
| [35455528](https://pubmed.ncbi.nlm.nih.gov/35455528/) | QoL: anxiety/depression, sexual dysfunction; mental not physical QoL affected | Systematic review |
| [37994266](https://pubmed.ncbi.nlm.nih.gov/37994266/) | Vaginal dilation viable first-line | Systematic review |
| [39391975](https://pubmed.ncbi.nlm.nih.gov/39391975/) | EHR cohort: ~2× anxiety/depression in Müllerian aplasia | Human/EHR |
| [33461758](https://pubmed.ncbi.nlm.nih.gov/33461758/) | Modified Vecchietti vaginoplasty (~9 cm neovagina) | Human clinical |
| [24356390](https://pubmed.ncbi.nlm.nih.gov/24356390/) | *WNT4* excluded in MURCS — differential boundary | Human clinical |
| [31685872](https://pubmed.ncbi.nlm.nih.gov/31685872/) | β-catenin in nephron segmentation (pathway context) | Model organism |

---

## Limitations and Knowledge Gaps

1. **Very small human sample.** The *WNT4* hyperandrogenic subtype rests on a handful of patients/variants (p.E226G, p.L12P, p.A233T). Penetrance, precise prevalence, and genotype–phenotype correlation are not formally quantified.
2. **ACMG classification uncertainty.** Beyond the functionally validated alleles, *WNT4* variants in MRKH are frequently VUS; the low diagnostic yield (~1/28 unselected MRKH) limits clinical actionability outside hyperandrogenic presentations.
3. **Mechanistic resolution.** The CYP17A1/HSD3B2 de-repression is shown in cell lines; the precise ovarian cell type and in-vivo human steroidogenic flux are incompletely defined. No human transcriptomic/proteomic/metabolomic atlas of patient ovarian tissue exists.
4. **Modifiers & epigenetics.** No validated modifier genes or disease-specific epigenetic marks; the basis of variable expressivity is unknown.
5. **Model mismatch.** The mouse null best models the recessive (SERKAL-like) severity; a heterozygous/partial-LOF mouse recapitulating the human dominant syndrome is not well established.
6. **Disorder-specific QoL/outcome data** are largely inferred from the broader MRKH literature rather than the *WNT4* subtype specifically.

---

## Proposed Follow-up Experiments / Actions

1. **Variant registry & functional reclassification.** Assemble all reported *WNT4* alleles in hyperandrogenic MRKH, apply uniform steroidogenic de-repression assays (CYP17A1/HSD3B2 reporter + androgen output), and reclassify under ACMG/AMP with PS3-level functional evidence.
2. **Heterozygous/partial-LOF mouse or organoid models.** Generate *Wnt4* point-knock-in (patient alleles) or hypomorphic alleles, and patient-iPSC-derived ovarian/Müllerian organoids, to model the dominant phenotype and quantify androgen output.
3. **Single-cell transcriptomics** of patient-derived (or model) ovarian somatic cells to pinpoint the de-repressed steroidogenic cell population and map the WNT4→β-catenin→steroidogenic-gene axis.
4. **Targeted gene-panel strategy.** Prospectively test *WNT4* in hyperandrogenic MRKH presentations (enriched yield) and correlate androgen biochemistry with genotype.
5. **Prospective natural-history/QoL cohort** specific to *WNT4*-confirmed patients, capturing androgen trajectories, fertility outcomes (surrogacy/UTx), and validated QoL/psychological measures.
6. **Genetic-counseling protocol** explicitly incorporating the dominant-vs-recessive (SERKAL) dosage distinction, including preconception counseling in consanguineous families.

---

*Evidence source legend: Human clinical (patient reports/cohorts), Model organism (mouse), In vitro (cell-line functional assays), Review (secondary synthesis). All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Mullerian_Aplasia_and_Hyperandrogenism-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mullerian_Aplasia_and_Hyperandrogenism-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 22 |
| On topic | 9 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:9989404` *(abstract only)*: "remarkably similar to"
  - Text part not found as substring: 'remarkably similar to' (note: only abstract available for PMID:9989404, full text may contain this excerpt)

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:35455528` (6 mentions) - The impact of Mayer-Rokitansky-Küster-Hauser Syndrome on Psychology, Quality of Life, and Sexual Life of Patients: A Systematic Review.
  - shared terms: mrkh

Weighed against this report's own most characteristic terms: `wnt4`, `androgen`, `disorder`, `llerian`, `ovarian`, `variant`, `mrkh`, `aplasia`, `hyperandrogenism`, `renal`, `phenotype`, `primary`, `gene`, `clinical`, `hyperandrogenic`, `cyp17a1`, `genetic`, `heterozygous`, `female`, `excess`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008019` (3 mentions) - the report calls it "MONDO"; MONDO calls it **mullerian aplasia and hyperandrogenism**
- `HP:0000786` (1 mention) - the report calls it "Symptom/sign"; HP calls it **Primary amenorrhea**
- `HP:0000858` (1 mention) - the report calls it "Hyperandrogenism"; HP calls it **Irregular menstruation**
- `HP:0001007` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Hirsutism**
- `HP:0001061` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Acne**
- `HP:0008222` (1 mention) - the report calls it "Decreased ovarian reserve"; HP calls it **Female infertility**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0030348` (1 mention) - the report calls it "Increased circulating androgen level"; HP calls it **Increased circulating androgen concentration**, and lists "Increased circulating androgen level" among its other names
- `UBERON:0000995` (1 mention) - the report calls it "Primary:** Uterus"; UBERON calls it **uterus**
- `UBERON:0002113` (1 mention) - the report calls it "Secondary / associated:** Kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names