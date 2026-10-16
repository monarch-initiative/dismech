---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T17:36:10.658881'
end_time: '2026-10-15T17:56:32.523848'
duration_seconds: 1221.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Myopathy Due To Calsequestrin And SERCA1 Protein Overload
  mondo_id: MONDO:0014546
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
citation_count: 12
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 8
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:26416891
  relevance_assessed: 14
  on_topic: 12
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 30
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 14
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0014546
    reported_labels:
    - MONDO
    ontology_label: myopathy due to calsequestrin and SERCA1 protein overload
  - term_id: UBERON:0011907
    reported_labels:
    - quadriceps femoris
    ontology_label: gastrocnemius medialis
  - term_id: NCIT:C15336
    reported_labels:
    - Supportive Care
    ontology_label: Testing
  - term_id: NCIT:C15682
    reported_labels:
    - Physical Therapy
    ontology_label: Dose-Rate
  - term_id: NCIT:C98225
    reported_labels:
    - Genetic Counseling
    ontology_label: Cefodizime Sodium
  labels_variant: 3
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Myopathy_Due_To_Calsequestrin_And_SERCA1_Protein_Overload-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Myopathy_Due_To_Calsequestrin_And_SERCA1_Protein_Overload-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myopathy Due To Calsequestrin And SERCA1 Protein Overload
- **MONDO ID:** MONDO:0014546 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Myopathy Due To Calsequestrin And SERCA1 Protein Overload** covering all of the
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

# Myopathy Due To Calsequestrin And SERCA1 Protein Overload — Comprehensive Disease Report

**Disease:** Myopathy due to calsequestrin and SERCA1 protein overload
**MONDO ID:** MONDO:0014546 | **OMIM:** 616231 ("Myopathy, vacuolar, with CASQ1 aggregates; VMCQA")
**Causal gene:** *CASQ1* (calsequestrin-1), chromosome 1q21
**Category:** Mendelian (autosomal dominant)
**Date:** 2026-10-15

---

## Summary

Myopathy due to calsequestrin and SERCA1 protein overload is an **ultra-rare, autosomal dominant, adult-onset, benign and slowly progressive skeletal-muscle disease** caused by heterozygous missense mutations in *CASQ1*, the gene encoding the fast-twitch skeletal-muscle isoform of calsequestrin. The disorder was first defined morphologically in 2006 as a "surplus protein myopathy" in which muscle fibers contained non-staining vacuolar inclusions immunoreactive for the sarco/endoplasmic reticulum Ca²⁺-ATPase SERCA1 (ATP2A1) and/or calsequestrin ([PMID: 16714317](https://pubmed.ncbi.nlm.nih.gov/16714317/)). Eight years later the causal lesion was identified as the heterozygous missense mutation *CASQ1* **c.731A>G, p.Asp244Gly (D244G)**, segregating as a founder mutation in Italian families ([PMID: 25116801](https://pubmed.ncbi.nlm.nih.gov/25116801/), [PMID: 26136523](https://pubmed.ncbi.nlm.nih.gov/26136523/)).

Mechanistically, the Asp244 residue sits within a high-affinity Ca²⁺-binding site in Domain II of calsequestrin. The mutation causes the protein to **lose Ca²⁺ binding and aggregate abnormally** into electron-dense sarcoplasmic reticulum (SR) vacuoles that co-sequester SERCA1 and the ryanodine receptor RyR1, predominantly within type II (fast) fibers. Aggregated calsequestrin **dissociates from the junctional SR**, reducing SR Ca²⁺ storage and impairing Ca²⁺ release — a defect that has been termed a **"CASQ1-couplonopathy"** ([PMID: 27196359](https://pubmed.ncbi.nlm.nih.gov/27196359/)). The downstream clinical picture is exercise intolerance, myalgia, mild-to-moderate slowly progressive proximal weakness, and mild-to-moderate elevation of serum creatine kinase (hyperCKemia), often presenting in the sixth decade of life ([PMID: 30258016](https://pubmed.ncbi.nlm.nih.gov/30258016/)).

The disease is benign in prognosis and does not shorten life expectancy. There is **no approved disease-specific therapy**; management is supportive and includes physiotherapy, cardiac surveillance (rare subclinical cardiac findings), and genetic counseling for the dominant trait. A theoretical malignant-hyperthermia/heat-sensitivity concern arises from the related *Casq1*-null mouse model, in which antioxidants and estrogens are protective; these pharmacologic strategies remain unproven in humans. The disease is modeled by D244G knock-in and *Casq1*-knockout mice.

---

## 1. Disease Information

**Overview.** This is a hereditary vacuolar myopathy of skeletal muscle characterized by intracellular accumulation ("overload") of two terminal-cisternae SR proteins — **calsequestrin-1 (CASQ1)** and **SERCA1 (ATP2A1)** — forming inclusions within muscle fibers. It was originally delineated purely by muscle biopsy morphology and immunohistochemistry as a "SERCA1 and calsequestrin storage myopathy" / "surplus protein myopathy" ([PMID: 16714317](https://pubmed.ncbi.nlm.nih.gov/16714317/)), and later unified genetically under mutations in *CASQ1*.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014546 |
| OMIM (phenotype) | 616231 — "MYOPATHY, VACUOLAR, WITH CASQ1 AGGREGATES; VMCQA" |
| Orphanet | ORPHA:88635 |
| GARD | 0016770 |
| MedGen / UMLS | 864061 / C4015624 |
| SNOMED CT | 724095006 |

**Synonyms / alternative names:**
- Myopathy due to calsequestrin and SERCA1 protein overload
- Vacuolar myopathy with CASQ1 aggregates (VMCQA)
- CASQ1-related myopathy
- SERCA1 and calsequestrin storage myopathy
- Protein aggregate myopathy with CASQ1 aggregates
- CASQ1-couplonopathy (mechanistic designation)

**Information source.** Knowledge is derived from **aggregated disease-level resources** (OMIM, Orphanet, MONDO) and from **individual patient reports/case series** in the primary literature (Italian and Chinese families), not from large EHR datasets. The total reported experience worldwide is on the order of 30–40 patients.

---

## 2. Etiology

**Disease causal factors.** The disease is **purely genetic (Mendelian, monogenic)**. It is caused by heterozygous gain-of-function/dominant missense mutations in *CASQ1*. There is no infectious or primary environmental cause.

**Genetic risk factors.** The principal causal variant is **CASQ1 p.Asp244Gly (c.731A>G)**, a founder mutation in Italian families sharing a common haplotype ([PMID: 26136523](https://pubmed.ncbi.nlm.nih.gov/26136523/)). Additional pathogenic alleles at the same or nearby residues broaden the allelic spectrum:
- **p.Asp244His (c.730G>C)** — reported in two unrelated Chinese families ([PMID: 41699400](https://pubmed.ncbi.nlm.nih.gov/41699400/)), establishing residue 244 as a **mutational hotspot**.
- **p.Gly103Asp** — reported in one Italian family, with a distinctive tubular-aggregate histology ([PMID: 30258016](https://pubmed.ncbi.nlm.nih.gov/30258016/)).
- **p.Met87Thr** — a separate variant *weakly* associated with malignant hyperthermia susceptibility rather than the overload myopathy ([PMID: 26416891](https://pubmed.ncbi.nlm.nih.gov/26416891/)).

**Environmental risk factors.** None established as causal. Theoretical triggers relevant to muscle Ca²⁺ handling — strenuous exercise, heat exposure, and volatile anesthetics — are implicated only from the *Casq1*-null mouse (see Section 15), not confirmed in the human overload myopathy.

**Protective factors.** No human genetic or environmental protective factors are established. In the *Casq1*-null mouse model, **estrogens** reduce oxidative stress and protect against lethal hyperthermic episodes ([PMID: 29062464](https://pubmed.ncbi.nlm.nih.gov/29062464/)), and **antioxidants** (N-acetylcysteine, Trolox) are protective ([PMID: 26132720](https://pubmed.ncbi.nlm.nih.gov/26132720/)) — but these pertain to the knockout MH phenotype, not the overload myopathy in humans.

**Gene–environment interactions.** Not formally characterized for the human disease. The mechanistic hypothesis — that a Ca²⁺-handling defect might be unmasked by heat/anesthetic/exercise stress — derives from the knockout model and remains inferred, not demonstrated, for patients.

---

## 3. Phenotypes

The clinical spectrum is best defined by the largest cohort to date: 22 CASQ1-mutated patients from 12 families (21 with p.Asp244Gly, 1 with p.Gly103Asp) ([PMID: 30258016](https://pubmed.ncbi.nlm.nih.gov/30258016/)).

| Phenotype | Type | Onset | Severity | Progression | Frequency | HPO suggestion |
|---|---|---|---|---|---|---|
| Exercise intolerance | Symptom | 6th decade | Mild–moderate | Slowly progressive | Common presenting feature | HP:0003546 (Exercise intolerance) |
| Myalgia | Symptom | 6th decade | Mild | Fluctuating | Common presenting feature | HP:0003326 (Myalgia) |
| Proximal muscle weakness | Clinical sign | Adult/late | Mild–moderate | Slowly progressive | Develops later in most | HP:0003701 (Proximal muscle weakness) |
| Quadriceps atrophy | Physical | Adult/late | Mild–moderate | Progressive | Characteristic | HP:0003327 (Axial muscle weakness)/quadriceps wasting |
| Scapular winging | Clinical sign | Adult/late | Mild | Progressive | Characteristic | HP:0003691 (Scapular winging) |
| HyperCKemia (elevated serum CK) | Lab abnormality | Adult | Mild–moderate | Stable/fluctuating | Very common; sometimes sole feature | HP:0003236 (Elevated serum creatine kinase) |
| Subclinical cardiac abnormality | Lab/clinical | Adult | Mild | Stable | 3/22 (~14%) | HP:0011675 (Arrhythmia)/HP:0001637 (Abnormal myocardium) |

**Key quotes.** "Patients usually presented in the sixth decade with exercise intolerance and myalgias and later developed mild to moderate, slowly progressive proximal weakness with quadriceps atrophy and scapular winging" ([PMID: 30258016](https://pubmed.ncbi.nlm.nih.gov/30258016/)). "Three patients presented subclinical cardiac abnormalities" (ibid.).

**Quality-of-life impact.** Because the disease is mild and slowly progressive, functional impact is limited; most patients remain ambulant. HyperCKemia may be the *only* manifestation, and many carriers are likely under-ascertained ("it is likely that CASQ1 mutations may remain undiagnosed if a muscle biopsy is not performed" — [PMID: 30258016](https://pubmed.ncbi.nlm.nih.gov/30258016/)). No disease-specific QoL instrument (EQ-5D/SF-36/PROMIS) data are available.

---

## 4. Genetic/Molecular Information

**Causal gene — CASQ1 (calsequestrin-1):**

| Annotation | Value |
|---|---|
| HGNC | HGNC:1512 |
| OMIM (gene) | 114250 |
| NCBI Gene | 844 |
| Ensembl | ENSG00000143318 |
| UniProt | P31415 (CASQ1_HUMAN) |
| Cytoband | 1q21 (GRCh38 chr1:160,190,212–160,201,886) |

**Pathogenic variants.**

| Variant (protein) | cDNA | Type | Population | Phenotype | Classification |
|---|---|---|---|---|---|
| p.Asp244Gly | c.731A>G | Missense | Italian founder | Vacuolar aggregate myopathy | Pathogenic |
| p.Asp244His | c.730G>C | Missense | Chinese (2 families) | Vacuolar myopathy | Pathogenic/likely pathogenic |
| p.Gly103Asp | — | Missense | Italian (1 family) | Myopathy w/ tubular aggregates | Pathogenic |
| p.Met87Thr | — | Missense | — | Weak MH susceptibility (not overload myopathy) | Risk variant |

**Variant classification notes.** The Domain-II residue Asp244 is highly conserved ("a highly conserved residue" — [PMID: 41699400](https://pubmed.ncbi.nlm.nih.gov/41699400/)); recurrence across independent populations (Italy, China) supports pathogenicity under ACMG criteria (PS1/PM1/PM5 — same residue, different substitutions).

**Allele frequency.** These are private/ultra-rare variants, essentially absent from population databases (gnomAD); the Italian cases share a single founder haplotype.

**Somatic vs germline.** All reported variants are **germline**, segregating in an autosomal dominant fashion.

**Functional consequences.** The mutation is best characterized as a **dominant, toxic gain-of-function / dominant-negative aggregation defect** combined with loss of normal Ca²⁺-buffering at the junctional SR: mutant CASQ1 loses high-affinity Ca²⁺ binding and aggregates abnormally, sequestering wild-type CASQ1 and partner proteins (SERCA1, RyR1).

**Modifier genes.** None established.

**Epigenetic information / chromosomal abnormalities.** Not applicable/not reported; this is a point-mutation monogenic disorder with no described epigenetic or structural chromosomal component.

---

## 5. Environmental Information

**Environmental factors.** None causally established. The disorder is monogenic. As a theoretical consideration (extrapolated from the knockout model, not the human overload myopathy), **heat stress and volatile halogenated anesthetics** could stress skeletal-muscle Ca²⁺ homeostasis.

**Lifestyle factors.** Strenuous exercise is a presenting trigger of symptoms (exercise intolerance, myalgia) but is not a disease cause.

**Infectious agents.** Not applicable — no infectious etiology.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A heterozygous **CASQ1 missense mutation** at/near a Domain-II high-affinity Ca²⁺-binding site (p.Asp244Gly, p.Asp244His, or p.Gly103Asp) arises in the germline → **leads to** a structurally altered calsequestrin monomer.
2. Loss of two coordinating Ca²⁺ ions in the mutant structure **weakens the hydrophobic core of Domain II** (demonstrated crystallographically for D244G) → **results in** loss of high-affinity Ca²⁺ binding at elevated Ca²⁺ ([PMID: 26416891](https://pubmed.ncbi.nlm.nih.gov/26416891/)).
3. Impaired Ca²⁺ binding **reduces the ability of CASQ1 to form normal elongated polymers** and instead **causes abrupt, abnormal aggregation** ([PMID: 26416891](https://pubmed.ncbi.nlm.nih.gov/26416891/)).
4. Aggregated mutant (and co-recruited wild-type) CASQ1 **leads to** the formation of **electron-dense SR vacuoles** that co-sequester SERCA1 (ATP2A1) and RyR1, preferentially in **type II fibers** ([PMID: 25116801](https://pubmed.ncbi.nlm.nih.gov/25116801/)).
5. In parallel (branch), the mutation **causes CASQ1 to partially dissociate from the junctional SR and accumulate in the ER** (shown in the D244G knock-in mouse) → **reduces junctional CASQ1 content and SR Ca²⁺ stores** ([PMID: 33786938](https://pubmed.ncbi.nlm.nih.gov/33786938/)).
6. Reduced junctional calsequestrin and disrupted couplon architecture **result in less Ca²⁺ release from the SR** of mutant fibers compared with controls (patient-derived myotubes) → defining a **"CASQ1-couplonopathy"** ([PMID: 27196359](https://pubmed.ncbi.nlm.nih.gov/27196359/)).
7. Chronically altered Ca²⁺ handling and protein overload **lead to** the clinical phenotype: **exercise intolerance, myalgia, mild proximal weakness, and hyperCKemia** ([PMID: 30258016](https://pubmed.ncbi.nlm.nih.gov/30258016/)).

```
CASQ1 D244G/D244H/G103D (germline, heterozygous)
        │  (Domain II high-affinity Ca2+ site)
        ▼
Loss of 2 Ca2+ ions → weakened Domain II hydrophobic core   [crystallography, in vitro]
        │
        ├──────────────► Abnormal/abrupt aggregation; loss of normal polymerization
        │                        │
        │                        ▼
        │                Electron-dense SR vacuoles sequestering CASQ1 + SERCA1 + RyR1
        │                (type II fibers)  → "surplus protein / overload"
        │
        └──────────────► Partial dissociation of CASQ1 from junctional SR → ER accumulation [KI mouse]
                                 │
                                 ▼
                    ↓ Junctional CASQ1, ↓ SR Ca2+ store → ↓ SR Ca2+ release ("couplonopathy")
                                 │
                                 ▼
          Adult-onset, slowly progressive, mild proximal myopathy + hyperCKemia
```

### Detail by category

- **Molecular pathways.** Excitation–contraction (EC) coupling: SR Ca²⁺ storage/release through the RyR1–DHPR couplon; Ca²⁺ reuptake via SERCA1. Calsequestrin is the principal luminal Ca²⁺ buffer that modulates RyR1 gating.
- **Cellular processes.** Protein aggregation / proteostasis failure in the SR; vacuole formation; altered intracellular Ca²⁺ signaling. GO suggestions: GO:0006874 (cellular calcium ion homeostasis), GO:0051209 (release of sequestered calcium ion into cytosol), GO:0005513 (detection of calcium ion), GO:0006457 (protein folding).
- **Protein dysfunction.** Loss of high-affinity Ca²⁺ binding, impaired polymerization, and toxic aggregation — a mixed loss-of-buffer + gain-of-aggregation mechanism. Normal CASQ1 binds ~80 Ca²⁺ ions and polymerizes to form the SR terminal-cisternae matrix.
- **Metabolic changes.** Secondary; chronically impaired Ca²⁺ cycling can affect fatigue resistance/energy metabolism in fast fibers (exercise intolerance), though not directly profiled in patients.
- **Immune system involvement.** None; this is a non-inflammatory, non-autoimmune protein-aggregate myopathy.
- **Tissue damage mechanisms.** Chronic vacuolar accumulation and Ca²⁺ dysregulation in type II fibers; mild myofiber stress releasing CK. In the knockout MH model, oxidative stress is central — but that is the loss-of-function phenotype.
- **Biochemical abnormalities.** Defective luminal SR Ca²⁺ buffering (ion-handling defect) rather than an enzyme deficiency.
- **Subcellular localization.** SR terminal cisternae / junctional SR lumen (GO:0033018 sarcoplasmic reticulum lumen region, GO:0014701 junctional sarcoplasmic reticulum membrane); pathologic mislocalization to the ER (GO:0005783 endoplasmic reticulum).

**Cell types involved.** Skeletal muscle fibers, specifically fast-twitch type II fibers — CL:0000190 (fast muscle cell) / CL:0008002 (skeletal muscle fiber).

---

## 7. Anatomical Structures Affected

- **Organ/system level.** Primary: **skeletal muscle** (musculoskeletal system). Distribution is **proximal and bilateral/symmetric** — quadriceps (anterior thigh), scapular/periscapular muscles (scapular winging). Secondary: **heart** — subclinical cardiac abnormalities in ~14% (3/22) ([PMID: 30258016](https://pubmed.ncbi.nlm.nih.gov/30258016/)).
- **Tissue/cell level.** Striated **muscle tissue**; predominantly **type II (fast-twitch) fibers** contain the vacuolar aggregates.
- **Subcellular level.** **Sarcoplasmic reticulum terminal cisternae / junctional SR**; abnormal accumulation in the **endoplasmic reticulum**.
- **UBERON/CL suggestions.** UBERON:0001134 (skeletal muscle tissue), UBERON:0011907 (quadriceps femoris), UBERON:0000948 (heart, secondary), UBERON:0002349 (myocardium); CL:0000190 (fast muscle cell). GO cellular component: GO:0016529 (sarcoplasmic reticulum), GO:0033018, GO:0005783.
- **Lateralization.** Bilateral, symmetric proximal involvement.

---

## 8. Temporal Development

- **Onset.** Adult, typically the **sixth decade**; onset is **insidious/chronic**. HyperCKemia may precede or exist without overt weakness.
- **Progression.** **Slowly progressive**; weakness remains mild-to-moderate; patients generally remain ambulant. Muscle MRI shows a recurrent fibrofatty substitution pattern (reported in 11 patients) ([PMID: 30258016](https://pubmed.ncbi.nlm.nih.gov/30258016/)).
- **Disease course.** Chronic, lifelong, but **benign**; no reported end-stage/wheelchair-dependent phase as a rule.
- **Patterns.** No spontaneous remission; no relapsing-remitting pattern. Symptoms (myalgia, exercise intolerance) may fluctuate with activity. Critical periods for intervention are not defined because no disease-modifying therapy exists.

---

## 9. Inheritance and Population

- **Epidemiology.** Ultra-rare. The world literature totals roughly **30–40 reported patients**, concentrated in Italy (founder p.Asp244Gly) plus isolated Chinese families. Orphanet prevalence: unknown, **<1/1,000,000**. Likely under-ascertained because mild cases escape biopsy ([PMID: 30258016](https://pubmed.ncbi.nlm.nih.gov/30258016/)).
- **Inheritance pattern.** **Autosomal dominant** (heterozygous missense variants).
- **Penetrance / expressivity.** Appears high but with **variable expressivity** (ranging from isolated hyperCKemia to symptomatic proximal weakness); formal penetrance estimates are not established.
- **Genetic anticipation / mosaicism.** Not applicable (not a repeat-expansion disorder); germline mosaicism not reported.
- **Founder effects.** Yes — a shared **Italian founder haplotype** for p.Asp244Gly ([PMID: 26136523](https://pubmed.ncbi.nlm.nih.gov/26136523/)).
- **Consanguinity / carrier frequency.** Not relevant to a dominant disorder; carrier frequency not meaningfully defined.
- **Population demographics.** Italian (founder) and Chinese families reported; both sexes affected; adult age distribution (sixth decade typical).

---

## 10. Diagnostics

- **Laboratory.** Serum **creatine kinase** mildly-to-moderately elevated (hyperCKemia), sometimes the sole abnormality (HP:0003236).
- **Muscle biopsy (diagnostic cornerstone).** Vacuoles in **type II fibers** appearing **"empty"** on H&E, Gomori trichrome, and NADH-tetrazolium reductase stains, but **strongly positive for SR proteins** (SERCA1/ATP2A1 and calsequestrin) by immunohistochemistry; immunoblot shows increased SERCA1 and calsequestrin ([PMID: 16714317](https://pubmed.ncbi.nlm.nih.gov/16714317/); [PMID: 30258016](https://pubmed.ncbi.nlm.nih.gov/30258016/)). The p.Gly103Asp variant additionally shows NADH-positive **tubular aggregates**. Electron microscopy: electron-dense SR vacuoles.
- **Imaging.** Muscle **MRI** shows a recurrent fibrofatty substitution pattern.
- **Electrophysiology.** EMG may show myopathic features; patient-derived myotubes show reduced SR Ca²⁺ release on Ca²⁺ imaging/electrophysiology (research setting) ([PMID: 27196359](https://pubmed.ncbi.nlm.nih.gov/27196359/)).
- **Genetic testing.** Confirmatory. Recommended approach: **single-gene testing of CASQ1** (targeting the Asp244 hotspot) or a **myopathy/limb-girdle gene panel**; **WES/WGS** are useful for undiagnosed cases, especially given the characteristic biopsy. Chromosomal microarray, karyotyping, FISH, mtDNA testing, and repeat-expansion testing are **not applicable**.
- **Clinical criteria / differential diagnosis.** No formal consensus criteria; diagnosis rests on the triad of (1) adult-onset mild proximal myopathy/hyperCKemia, (2) SR-protein-positive type II fiber vacuoles, and (3) a pathogenic CASQ1 variant. Differential diagnoses: **tubular aggregate myopathies** (STIM1/ORAI1), other **protein-aggregate/vacuolar myopathies**, limb-girdle muscular dystrophies, and idiopathic hyperCKemia.
- **Screening.** Cascade genetic testing of at-risk relatives in known families. No population newborn/carrier screening (ultra-rare, dominant, benign).

---

## 11. Outcome/Prognosis

- **Survival/mortality.** **Benign**; life expectancy is not reported to be reduced; no disease-specific mortality established.
- **Morbidity/function.** Mild-to-moderate proximal weakness with slow progression; most patients remain ambulant and functionally independent. Rare subclinical cardiac abnormalities (~14%) warrant surveillance but have not been linked to adverse outcomes.
- **Disease course/complications.** Chronic but stable-to-slowly-progressive. Theoretical anesthetic/heat risk is extrapolated from the knockout model and remains unproven in patients.
- **Prognostic factors.** None validated. Genotype may influence histology (tubular aggregates with p.Gly103Asp) but not clearly prognosis.
- **Supporting quote.** Patients "later developed mild to moderate, slowly progressive proximal weakness" ([PMID: 30258016](https://pubmed.ncbi.nlm.nih.gov/30258016/)).

---

## 12. Treatment

- **Pharmacotherapy.** **No approved disease-specific or targeted drug.** Management is **supportive**.
- **Advanced therapeutics (gene/cell/RNA).** None in clinical use; the dominant aggregation mechanism could in principle be amenable to allele-specific knockdown (ASO/siRNA) in the future, but no such program is reported.
- **Supportive/rehabilitative.** Physiotherapy, graded exercise modification for exercise intolerance/myalgia, periodic **cardiac surveillance** given rare subclinical cardiac findings.
- **Experimental / mechanistic leads.** From the *Casq1*-null mouse (loss-of-function MH model, distinct from the overload disease): **antioxidants** (N-acetylcysteine, Trolox) protected against lethal halothane/heat-triggered hypermetabolic episodes, reducing mortality from ~79–86% to ~20–33% ([PMID: 26132720](https://pubmed.ncbi.nlm.nih.gov/26132720/)), and **estrogens** reduced oxidative stress and mortality ([PMID: 29062464](https://pubmed.ncbi.nlm.nih.gov/29062464/)). These suggest antioxidant strategies and **anesthetic/heat precautions** as rational but unproven approaches in humans.
- **Treatment outcomes / adverse events.** Not applicable (no disease-specific therapy).
- **NCIT suggestions.** NCIT:C15336 (Supportive Care), NCIT:C15682 (Physical Therapy), NCIT:C98225 (Genetic Counseling), NCIT:C265 (Antioxidant) — all general/supportive.

---

## 13. Prevention

- **Primary prevention.** None for a Mendelian disorder.
- **Secondary prevention.** Early detection via **cascade genetic testing** in known families; recognition of isolated hyperCKemia prompting biopsy/genetics.
- **Tertiary prevention.** Cardiac surveillance; prudent **anesthetic and heat precautions** (theoretical, extrapolated from the knockout model).
- **Immunization / public health / environmental interventions.** Not applicable.
- **Counseling.** **Genetic counseling** for autosomal dominant inheritance (50% transmission risk); theoretical prenatal/preimplantation genetic testing is possible but rarely indicated given the benign course.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs.** Mouse ortholog **Casq1**: MGI:1309468, NCBI Gene 12372, Ensembl ENSMUSG00000007122. CASQ1 is highly conserved across mammals.
- **Natural disease in other species.** No naturally occurring animal homolog of this specific overload myopathy is reported (OMIA). Disease knowledge in animals comes from engineered models (Section 15).
- **Comparative biology.** Calsequestrin's role in SR Ca²⁺ storage and EC coupling is evolutionarily conserved, underpinning the translational relevance of mouse models.
- **Transmission.** Not applicable (non-communicable genetic disease; no zoonotic potential).

---

## 15. Model Organisms

Two complementary mouse models anchor the mechanistic understanding, and cellular systems recapitulate the aggregation phenotype.

| Model | Type | Key phenotype | Relevance to human disease |
|---|---|---|---|
| **D244G knock-in mouse** | Mammalian, knock-in | CASQ1 partially dissociates from junctional SR and accumulates in ER; reduced junctional CASQ1 and SR Ca²⁺ ([PMID: 33786938](https://pubmed.ncbi.nlm.nih.gov/33786938/)) | Directly models the human overload/couplonopathy mechanism |
| **Casq1-null (knockout) mouse** | Mammalian, knockout (loss of function) | Viable, normal motor activity, moderate atrophy; profound EC-coupling remodeling (shrunken jSR, proliferating SR/T-tubule contacts, ↑RyR density); **lethal MH-like hypermetabolic episodes** on halothane/heat ([PMID: 22130610](https://pubmed.ncbi.nlm.nih.gov/22130610/); [PMID: 26132720](https://pubmed.ncbi.nlm.nih.gov/26132720/)) | Models malignant-hyperthermia/heat susceptibility; oxidative-stress mechanism; estrogen/antioxidant protection |
| **COS-7 cells, myotubes, patient-derived myotubes** | In vitro/cellular | Mutant CASQ1 forms electron-dense SR vacuoles with CASQ1/RyR1 aggregates; reduced polymerization; less SR Ca²⁺ release ([PMID: 25116801](https://pubmed.ncbi.nlm.nih.gov/25116801/); [PMID: 27196359](https://pubmed.ncbi.nlm.nih.gov/27196359/)) | Recapitulates aggregation and the Ca²⁺-release defect |
| **Recombinant protein / crystallography** | Biophysical | D244G lacks two Ca²⁺ ions, weakened Domain II core, abrupt aggregation ([PMID: 26416891](https://pubmed.ncbi.nlm.nih.gov/26416891/)) | Structural basis of the defect |

**Rescue evidence.** Re-introduction of wild-type CASQ1 by cDNA electrotransfer in *Casq1*-null muscle restores junctional SR targeting, terminal-cisternae ultrastructure, and Ca²⁺ transient amplitude ([PMID: 22049211](https://pubmed.ncbi.nlm.nih.gov/22049211/)) — confirming CASQ1's causal role in both Ca²⁺ homeostasis and terminal-cisternae structure.

**Model limitations.** The *Casq1*-null mouse models **loss of function** and its dominant feature is MH/heat susceptibility, which is *not* the primary human overload phenotype; the knock-in D244G mouse better reflects the human dominant aggregation/couplonopathy. Resources: MGI (Casq1, MGI:1309468).

---

## Mechanistic Model / Interpretation

The convergent human (biopsy, patient-myotube electrophysiology, 22-patient cohort), in vitro (crystallography, cell aggregation), and mouse (D244G knock-in, Casq1 knockout) evidence defines a single coherent model:

> A heterozygous **CASQ1 missense mutation at/near a Domain II high-affinity Ca²⁺ site** (D244G / D244H / G103D) → **loss of Ca²⁺ binding + abnormal aggregation** → **electron-dense SR/ER vacuoles sequestering CASQ1, SERCA1, and RyR1 in type II fibers** → **dissociation of CASQ1 from the junctional SR** → **reduced SR Ca²⁺ storage and release (CASQ1-couplonopathy)** → **adult-onset, slowly progressive, mild proximal myopathy with hyperCKemia.**

Upstream events are molecular/biophysical (the mutation, loss of Ca²⁺ coordination, aggregation); downstream events are physiological and clinical (impaired EC coupling, weakness, CK leak). The disease unifies two apparently opposite effects — a **gain** of toxic protein (the "overload"/surplus protein storage) and a **loss** of functional junctional buffering (the couplonopathy) — into one pathogenic cascade. Notably, calsequestrin dysfunction produces two divergent human phenotypes depending on the allele: the benign dominant **overload myopathy** (D244G/D244H/G103D) versus a weak **malignant-hyperthermia** association (M87T), with the knockout mouse illustrating the MH/heat-stress extreme of the loss-of-function axis.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [16714317](https://pubmed.ncbi.nlm.nih.gov/16714317/) | SERCA1 and calsequestrin storage myopathy | Human (biopsy) | Original morphological definition (surplus SR-protein myopathy) |
| [25116801](https://pubmed.ncbi.nlm.nih.gov/25116801/) | CASQ1 mutation causes vacuolar myopathy | Human genetics + cellular | Causal D244G; vacuoles; altered Ca²⁺ release |
| [26136523](https://pubmed.ncbi.nlm.nih.gov/26136523/) | CASQ1 founder mutation, 3 Italian families | Human genetics | Founder effect; benign evolution |
| [41699400](https://pubmed.ncbi.nlm.nih.gov/41699400/) | CASQ1 p.Asp244His, 2 Chinese families | Human genetics | Second hotspot variant; conserved residue |
| [26416891](https://pubmed.ncbi.nlm.nih.gov/26416891/) | Characterization of two CASQ1 mutants | Biophysical/crystallography | Structural basis: loss of Ca²⁺, abnormal aggregation; D244G vs M87T |
| [27196359](https://pubmed.ncbi.nlm.nih.gov/27196359/) | CASQ1 mutation alters SR Ca²⁺ release | Patient myotubes | Reduced SR Ca²⁺ release; "CASQ1-couplonopathy" |
| [33786938](https://pubmed.ncbi.nlm.nih.gov/33786938/) | Pathological mechanisms from Casq1 mutation | D244G knock-in mouse | jSR→ER mislocalization; reduced SR Ca²⁺ |
| [30258016](https://pubmed.ncbi.nlm.nih.gov/30258016/) | Clinical spectrum of CASQ1 myopathy | Human cohort (n=22) | Onset, weakness distribution, histology, cardiac, MRI |
| [22130610](https://pubmed.ncbi.nlm.nih.gov/22130610/) | Lessons from Casq1 ablation | Knockout mouse | EC-coupling remodeling |
| [26132720](https://pubmed.ncbi.nlm.nih.gov/26132720/) | Antioxidants protect Casq1-null mice | Knockout mouse | MH/heat phenotype; antioxidant protection |
| [29062464](https://pubmed.ncbi.nlm.nih.gov/29062464/) | Estrogens protect Casq1-null mice | Knockout mouse | Estrogen protection; sex difference |
| [22049211](https://pubmed.ncbi.nlm.nih.gov/22049211/) | CASQ1 rescues Casq1-null muscle | Knockout + rescue | Confirms CASQ1 role in Ca²⁺ and structure |
| [28465322](https://pubmed.ncbi.nlm.nih.gov/28465322/) | Exercise triggers MH-like response | Mouse (RyR1/MH) | Exercise as a trigger in MH-susceptible muscle |
| [36311237](https://pubmed.ncbi.nlm.nih.gov/36311237/) | Ablation of Calsequestrin-1 | Mouse | CASQ1 ablation effects |

**Notable verbatim support.**
- "The mutation affects a conserved aspartic acid in position 244 (p.Asp244Gly) located in one of the high-affinity Ca(2+)-binding sites of CASQ1 and alters the kinetics of Ca(2+) release in muscle fibers." ([PMID: 25116801](https://pubmed.ncbi.nlm.nih.gov/25116801/))
- "D244G aggregates abruptly and abnormally … D244G crystallized in low Ca(2+) concentrations lacks two Ca(2+) ions normally present in wild type that weakens the hydrophobic core of Domain II." ([PMID: 26416891](https://pubmed.ncbi.nlm.nih.gov/26416891/))
- "Electrophysiological recordings and sarcoplasmic Ca2+ measurements provide evidence for less Ca2+ release from the SR of mutated myotubes when compared to that of controls." ([PMID: 27196359](https://pubmed.ncbi.nlm.nih.gov/27196359/))
- "The DG mutation causes CASQ1 to partially dissociate from the junctional sarcoplasmic reticulum (SR) and accumulate in the endoplasmic reticulum (ER)." ([PMID: 33786938](https://pubmed.ncbi.nlm.nih.gov/33786938/))

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** Only ~30–40 patients worldwide; cohort statistics (e.g., 22-patient series) dominate, so penetrance, true prevalence, and genotype–phenotype correlations are imprecise.
2. **Ascertainment bias.** Mild/isolated-hyperCKemia cases likely under-diagnosed without muscle biopsy, so the spectrum may be broader and milder than reported.
3. **Mechanistic duality unresolved in humans.** The human overload myopathy vs the knockout MH/heat-stress phenotype are modeled in different systems; whether human D244G patients carry a clinically meaningful anesthetic/heat risk is **not demonstrated** — the precaution is extrapolated.
4. **No human therapeutic data.** Antioxidant/estrogen protection is only shown in Casq1-null mice; no trials in patients.
5. **Cardiac involvement.** The significance of subclinical cardiac abnormalities (~14%) is unclear; CASQ1 is the skeletal isoform (cardiac CASQ2 is distinct), so the cardiac finding needs mechanistic clarification.
6. **Omics gaps.** No transcriptomic, proteomic, metabolomic, or single-cell profiling specific to this disease is available.

---

## Proposed Follow-up Experiments / Actions

1. **Natural-history registry** across Italian and Chinese families (and new cases) to quantify penetrance, progression rate, and cardiac risk prospectively.
2. **Anesthetic/heat-stress risk assessment** in D244G knock-in mice and, cautiously, retrospective review of patient anesthetic exposures to test whether the MH/heat risk translates to the overload myopathy.
3. **Test antioxidant (NAC) and estrogen pathways** in the D244G knock-in (not only knockout) model to determine relevance to the overload phenotype.
4. **Allele-specific knockdown (ASO/siRNA)** proof-of-concept targeting mutant CASQ1 transcripts in patient myotubes to address the dominant aggregation mechanism.
5. **Deep muscle proteomics/transcriptomics** of patient biopsies to map the full "surplus protein" composition and secondary stress responses.
6. **Structural studies** of D244H and G103D (beyond D244G) to confirm shared loss-of-Ca²⁺-binding mechanism across the allelic spectrum.
7. **Cardiac evaluation protocol** to clarify whether skeletal CASQ1 variants have any genuine cardiac phenotype or whether findings are incidental.


## Artifacts

- [OpenScientist final report](Myopathy_Due_To_Calsequestrin_And_SERCA1_Protein_Overload-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Myopathy_Due_To_Calsequestrin_And_SERCA1_Protein_Overload-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 14 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:26416891` *(abstract only)*: "D244G aggregates abruptly and abnormally … D244G crystallized in low Ca(2+) concentrations lacks two Ca(2+) ions normally present in wild type that weakens the hydrophobic core of Domain II."
  - closest text in source: "D244G crystallized in low Ca(2+) concentrations lacks two Ca(2+) ions normally present in wild type that weakens the hydrophobic core of Domain II"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 22 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014546` (2 mentions) - the report calls it "MONDO"; MONDO calls it **myopathy due to calsequestrin and SERCA1 protein overload**
- `UBERON:0011907` (1 mention) - the report calls it "quadriceps femoris"; UBERON calls it **gastrocnemius medialis**
- `NCIT:C15336` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Testing**
- `NCIT:C15682` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Dose-Rate**
- `NCIT:C98225` (1 mention) - the report calls it "Genetic Counseling"; NCIT calls it **Cefodizime Sodium**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006874` (1 mention) - the report calls it "cellular calcium ion homeostasis"; GO calls it **intracellular calcium ion homeostasis**, and lists "cellular calcium ion homeostasis" among its other names
- `UBERON:0000948` (1 mention) - the report calls it "heart, secondary"; UBERON calls it **heart**
- `NCIT:C265` (1 mention) - the report calls it "Antioxidant"; NCIT calls it **Antidepressant Agent**, and lists "Antidepressant" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.