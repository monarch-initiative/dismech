---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T08:49:18.570935'
end_time: '2026-09-25T09:19:11.774159'
duration_seconds: 1793.2
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ulceroglandular Tularemia
  mondo_id: MONDO:0001413
  category: Infectious Disease
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
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
  on_topic: 20
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 27
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 4
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0200042
    reported_labels:
    - Physical manifestation
    ontology_label: Skin ulcer
  - term_id: HP:0001945
    reported_labels:
    - Symptom / sign
    ontology_label: Fever
  - term_id: HP:0002218
    reported_labels:
    - Clinical sign
    ontology_label: Silver-gray hair
  - term_id: UBERON:0002106
    reported_labels:
    - Secondary involvement:** In disseminated/severe disease, spleen
    ontology_label: spleen
  - term_id: NCIT:C255
    reported_labels:
    - Aminoglycoside
    ontology_label: Urinary Anti-Infective Agent
  - term_id: NCIT:C1728
    reported_labels:
    - Ciprofloxacin
    ontology_label: Celecoxib
  - term_id: NCIT:C641
    reported_labels:
    - Doxycycline
    ontology_label: Methimazole
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Ulceroglandular_Tularemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Ulceroglandular_Tularemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ulceroglandular Tularemia
- **MONDO ID:** MONDO:0001413 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Ulceroglandular Tularemia** covering all of the
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

# Ulceroglandular Tularemia: A Comprehensive Disease Characteristics Report

**Disease:** Ulceroglandular Tularemia
**MONDO ID:** MONDO:0001413
**Category:** Infectious Disease (zoonotic, bacterial)
**Causative agent:** *Francisella tularensis* (NCBITaxon:263)
**Evidence base:** Literature-derived (aggregated disease-level resources, systematic reviews, CDC surveillance, and mechanistic studies in cell/mouse models). No individual patient (EHR) data were used.

---

## Summary

**Ulceroglandular tularemia is the most common clinical form of tularemia**, an acute zoonotic infection caused by *Francisella tularensis*, a small, aerobic, Gram-negative, facultative intracellular coccobacillus and one of the most infectious bacterial pathogens known (infectious dose as low as ~10 organisms). The ulceroglandular form arises specifically from **cutaneous inoculation** of the organism — most often through the bite of an infected arthropod (ticks such as *Dermacentor variabilis* and *Amblyomma americanum*, deer flies, and mosquitoes) or through direct handling of infected animals (lagomorphs and rodents). After a 3–6 day incubation period, patients develop an acute febrile illness with a papule that ulcerates at the site of inoculation (skin ulcer, HP:0200042) accompanied by painful regional lymphadenopathy (HP:0002716). This is fundamentally an **infectious, not a genetic, disease**: there are no causal human genes, pathogenic variants, or heritable susceptibility loci, so the "genetic/molecular" content of this report concerns the *bacterial* virulence determinants rather than host germline genetics.

The pathophysiology is driven by the bacterium's ability to survive and replicate inside host phagocytes. The **Francisella Pathogenicity Island (FPI)**, which encodes a **Type VI secretion system (T6SS)**, enables the bacterium to escape the phagosome and replicate freely in the macrophage cytosol, ultimately triggering inflammasome activation and host-cell death. This intracellular lifestyle explains why host defense is predominantly **cell-mediated** (T-cell/IFN-γ dependent): granulocytes cannot kill the organism without opsonizing antibody, and protective immunity emerges as a vigorous T-lymphocyte response 1–2 weeks after infection, with humoral antibody appearing at 2–3 weeks and serving primarily a diagnostic role.

Clinically, ulceroglandular tularemia has a **good prognosis** because the pathogen is well contained by a vigorous local inflammatory reaction, contrasting with the typhoidal syndrome, which has fewer localizing signs, more pneumonia, and higher untreated mortality. Diagnosis relies on serology (microagglutination titer ≥1/160 or a four-fold rise) and PCR of ulcer swabs or lymph-node aspirates; culture is hazardous and requires BSL-3 containment. Treatment with aminoglycosides (streptomycin, gentamicin — first-line), fluoroquinolones (ciprofloxacin), or tetracyclines (doxycycline) yields case-fatality rates below ~1.2%. There is **no licensed vaccine**; prevention rests on exposure avoidance and, after high-risk exposures, post-exposure antibiotic prophylaxis. *F. tularensis* is classified as a **Tier-1 Select Agent / Category A bioterrorism agent** owing to its low infectious dose and aerosol infectivity.

---

## Section 1 — Disease Information

**Overview.** Ulceroglandular tularemia is the cutaneous-inoculation form of tularemia, a zoonosis caused by *Francisella tularensis*. Across a systematic review of 870 cases spanning 1993–2023 in 35 countries, **ulceroglandular disease was the single most common clinical form**, followed by oropharyngeal, glandular, and pneumonic disease — *"The most common clinical forms were ulceroglandular, oropharyngeal, glandular, and pneumonic disease"* ([PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/)). It is defined by the route of infection — cutaneous inoculation producing a local ulcer plus regional lymphadenitis ([PMID: 32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/)).

**Key identifiers.**
- **MONDO:** MONDO:0001413 (ulceroglandular tularemia)
- **MeSH:** Tularemia (D014406)
- **ICD-10:** A21.0 (Ulceroglandular tularaemia); parent A21 (Tularaemia)
- **ICD-11:** 1B94 (Tularaemia)
- **SNOMED CT:** Ulceroglandular tularemia (disorder)
- **OMIM / Orphanet:** Not applicable as a heritable disorder (infectious disease; no OMIM Mendelian entry).

**Synonyms / alternative names.** Ulceroglandular tularaemia (British spelling); "rabbit fever," "deer-fly fever," "Ohara disease," "Francis disease," and "Pahvant Valley plague" are historical synonyms for tularemia broadly, of which the ulceroglandular form is the classic presentation.

**Information source.** The evidence is derived from **aggregated disease-level resources** — systematic reviews, national surveillance (CDC NNDSS), and case series — rather than individual EHR-derived patient records.

---

## Section 2 — Etiology

**Primary cause (infectious).** The disease is caused entirely by infection with *Francisella tularensis*. There is **no genetic (host) etiology**; heritable variants, susceptibility loci, and modifier genes are **not applicable**. Two clinically important subspecies exist: subsp. *tularensis* (**type A**, most virulent, North America) and subsp. *holarctica* (**type B**, milder, Northern Hemisphere including Europe and Asia) ([PMID: 32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/)).

**Environmental / exposure risk factors.**
- **Arthropod bites** — ticks (*Dermacentor variabilis*, *Amblyomma americanum*), deer flies, horseflies, and mosquitoes. *"The disease spreads through vectors such as mosquitoes, horseflies, deer flies, and ticks"* ([PMID: 32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/)); the principal US tick vectors are *D. variabilis* and *A. americanum* ([PMID: 40788927](https://pubmed.ncbi.nlm.nih.gov/40788927/)).
- **Handling infected animals / carcasses** — *"The common route of transmission in Central Europe is handling infected animals"* ([PMID: 34990926](https://pubmed.ncbi.nlm.nih.gov/34990926/)).
- **Occupational / recreational** — hunters, trappers, farmers, landscapers, veterinarians, and laboratory workers.
- **Demographic** — highest incidence in children aged 5–9 years and older adult males (bimodal), and markedly elevated among American Indian/Alaska Native persons in the US ([PMID: 39736154](https://pubmed.ncbi.nlm.nih.gov/39736154/)).

**Protective factors.** No genetic protective variants are described (not a host-genetic disease). Environmental protection is behavioral: use of insect repellents, protective clothing, tick checks, and gloves when handling animal carcasses (see Section 13).

**Gene–environment interactions.** Not applicable in the human-host genetic sense. The relevant "gene–environment" axis is the **bacterial** genotype (type A vs type B; FPI integrity) interacting with the route and dose of exposure to determine clinical form and severity.

---

## Section 3 — Phenotypes

The ulceroglandular syndrome is a localized-plus-regional presentation following a 3–6 day incubation.

| Phenotype | Type | HPO term | Frequency / notes |
|---|---|---|---|
| Fever | Symptom / sign | HP:0001945 | Near-universal at onset; acute ([PMID: 3892222](https://pubmed.ncbi.nlm.nih.gov/3892222/)) |
| Skin ulcer at inoculation site | Physical manifestation | HP:0200042 | Defining lesion; papule → ulcer ([PMID: 32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/)) |
| Regional lymphadenopathy (painful) | Clinical sign | HP:0002716 / HP:0002840 | Defining feature; can suppurate/drain ([PMID: 16936340](https://pubmed.ncbi.nlm.nih.gov/16936340/)) |
| Cervical lymphadenopathy (pediatric) | Clinical sign | HP:0002218 | Reported after tick bite in young children ([PMID: 34990926](https://pubmed.ncbi.nlm.nih.gov/34990926/)) |
| Suppurative lymphadenitis | Complication | — | Especially with delayed therapy ([PMID: 16936340](https://pubmed.ncbi.nlm.nih.gov/16936340/)) |
| Secondary skin eruptions (erythema nodosum, Sweet syndrome) | Physical manifestation | HP:0012219 / — | Secondary manifestations in ~15% of tularemia overall; more common in oropharyngeal form ([PMID: 29761532](https://pubmed.ncbi.nlm.nih.gov/29761532/)) |

**Characteristics.**
- **Age of onset:** Any age; the disease is acquired, not congenital. US incidence peaks in children 5–9 and older adults ([PMID: 39736154](https://pubmed.ncbi.nlm.nih.gov/39736154/)).
- **Severity:** Generally mild-to-moderate for the ulceroglandular form (type B predominant in Europe); good prognosis. *"In ulceroglandular tularemia the pathogen appears to be well contained by a vigorous inflammatory reaction. Pneumonia is less common and the patient's prognosis is good"* ([PMID: 3892222](https://pubmed.ncbi.nlm.nih.gov/3892222/)).
- **Progression:** Acute onset; resolving with therapy; lymphadenopathy may persist or suppurate.
- **Quality of life:** Acute febrile illness with painful lymphadenopathy causes short-term functional impairment; suppurative nodes may require drainage. Long-term sequelae are uncommon with timely treatment. (No disease-specific EQ-5D/SF-36 data identified — knowledge gap.)

---

## Section 4 — Genetic / Molecular Information

**Host genetics: not applicable.** Ulceroglandular tularemia is an acquired infection with **no causal human genes, pathogenic germline/somatic variants, modifier genes, epigenetic lesions, or chromosomal abnormalities.** ClinVar/OMIM/HGMD entries do not apply.

**Bacterial molecular determinants (the relevant "molecular information").** Virulence depends on the **Francisella Pathogenicity Island (FPI)**, which encodes a **Type VI secretion system (T6SS)**. *"Required for these processes is the Francisella Pathogenicity Island (FPI), which encodes a Type VI secretion system (T6SS) that is active during intracellular infection"* ([PMID: 27830989](https://pubmed.ncbi.nlm.nih.gov/27830989/)). Key FPI genes include *iglB*, *iglC*, *iglE*, *iglG*, *pdpC*, *dotU*, and *vgrG*. Deletion mutants (ΔiglB, ΔiglE, ΔpdpC) fail to escape the phagosome, do not replicate intracellularly, and are markedly attenuated in the mouse model ([PMID: 27830989](https://pubmed.ncbi.nlm.nih.gov/27830989/); [PMID: 23356941](https://pubmed.ncbi.nlm.nih.gov/23356941/); [PMID: 23403609](https://pubmed.ncbi.nlm.nih.gov/23403609/)). PdpC additionally has a regulatory role over *iglABCD* expression, and its deletion abolishes phagosomal escape and cytopathogenicity ([PMID: 27477000](https://pubmed.ncbi.nlm.nih.gov/27477000/)).

---

## Section 5 — Environmental Information

- **Environmental factors:** The organism persists in the environment (water, soil, animal carcasses) and is maintained in an enzootic cycle. Tularemia is a **Holarctic zoonosis** ([PMID: 31600457](https://pubmed.ncbi.nlm.nih.gov/31600457/)).
- **Lifestyle factors:** Outdoor occupational/recreational activities (hunting, trapping, farming, landscaping) increase exposure. *"Humans can acquire the disease through direct contact of sick animals, consumption of infected animals, drinking or direct contact of contaminated water, and inhalation of bacteria-loaded aerosols"* ([PMID: 32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/)) — the latter routes are more relevant to oropharyngeal/pneumonic forms.
- **Infectious agent (NCBI Taxonomy):** *Francisella tularensis* (NCBITaxon:263). Subspecies: subsp. *tularensis* (type A) and subsp. *holarctica* (type B, NCBITaxon:264). Type B predominates in Europe and causes the ulceroglandular cases reported from Poland and the Czech Republic ([PMID: 34696556](https://pubmed.ncbi.nlm.nih.gov/34696556/); [PMID: 32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/)).

---

## Section 6 — Mechanism / Pathophysiology

### Causal chain (initiating exposure → clinical manifestation)

1. **Cutaneous inoculation** of *F. tularensis* (~10 organisms) via arthropod bite or contact with an infected animal **leads to** local bacterial deposition in the skin and subcutaneous tissue. *"Francisella tularensis is an extremely virulent pathogen capable of initiating infection with as few as 10 organisms inoculated subcutaneously"* ([PMID: 3892222](https://pubmed.ncbi.nlm.nih.gov/3892222/)). *(Demonstrated.)*
2. Local deposition **results in** uptake by resident and recruited **phagocytes** — *"the host responds first with polymorphonuclear leukocytes and then macrophages"* ([PMID: 3892222](https://pubmed.ncbi.nlm.nih.gov/3892222/)). *(Demonstrated.)*
3. Inside the phagocyte, the **FPI-encoded T6SS** mediates **escape from the phagosome** into the cytosol. *"Genes in the FPI are required for F. tularensis to escape from the phagosome and replicate in the cytosol"* ([PMID: 23403609](https://pubmed.ncbi.nlm.nih.gov/23403609/)). *(Demonstrated — FPI mutants fail to escape.)*
4. Cytosolic localization **leads to** rapid **intracellular replication** — *"effective intramacrophage proliferation, which is preceded by phagosomal escape into the cytosol"* ([PMID: 23356941](https://pubmed.ncbi.nlm.nih.gov/23356941/)). *(Demonstrated.)*
5. Intracellular infection **induces** macrophage **PGE2 synthesis** (dampening adaptive immunity) and **inflammasome activation** (IL-1β / LDH release). *(Demonstrated in macrophage models; [PMID: 23403609](https://pubmed.ncbi.nlm.nih.gov/23403609/).)*
6. Inflammasome activation and cytosolic burden **result in** **host-cell death** — *"ultimately causing inflammasome activation and host cell death"* ([PMID: 27830989](https://pubmed.ncbi.nlm.nih.gov/27830989/)) — releasing bacteria to infect neighboring cells and draining to regional lymph nodes. *(Demonstrated.)*
7. Bacterial drainage to regional nodes **leads to** a vigorous local **inflammatory / granulomatous response** — the clinical **skin ulcer + regional lymphadenopathy**, sometimes progressing to **suppurative lymphadenitis**. *(Inferred from clinical–pathological correlation.)*
8. **Branch:** In the ulceroglandular form the pathogen is **well contained** locally → good prognosis. *"In typhoidal disease there are few localizing signs; pneumonia is more common; and the mortality without therapy is much higher, suggesting that the host response is somehow deficient"* ([PMID: 3892222](https://pubmed.ncbi.nlm.nih.gov/3892222/)). *(Inferred from syndrome comparison.)*
9. Adaptive control **requires** a **cell-mediated (T-cell/IFN-γ)** response appearing 1–2 weeks post-infection; humoral antibody at 2–3 weeks is largely diagnostic. *(Demonstrated.)*

### Detail by category

- **Cellular processes (GO):** phagocytosis (GO:0006909); phagosomal escape; intracellular replication; inflammasome/pyroptosis (GO:0070269); inflammatory response (GO:0006954).
- **Immune involvement:** Cell-mediated immunity is dominant. *"Granulocytes are unable to kill the pathogen without opsonizing antibody leaving cellular immunity to play the major role in host defense"* ([PMID: 3892222](https://pubmed.ncbi.nlm.nih.gov/3892222/)). Both natural infection and LVS vaccination drive **multifunctional T-cell responses** ([PMID: 42238599](https://pubmed.ncbi.nlm.nih.gov/42238599/)). In models, perforin/granzyme cytotoxicity and NK-cell activity contribute to protection ([PMID: 22493083](https://pubmed.ncbi.nlm.nih.gov/22493083/)).
- **Protein dysfunction / secretion:** T6SS structural and effector proteins (IglB, IglE, PdpC, VgrG) mediate the secretion required for escape; N-terminal residues of IglE critically control T6SS-mediated secretion ([PMID: 27830989](https://pubmed.ncbi.nlm.nih.gov/27830989/)).
- **Tissue damage mechanisms:** host-cell death (pyroptosis/necrosis), suppuration/abscess formation in lymph nodes, granulomatous inflammation.
- **Cell types (CL):** macrophage (CL:0000235), monocyte-derived macrophage, neutrophil (CL:0000775), T lymphocyte (CL:0000084), NK cell (CL:0000623).

---

## Section 7 — Anatomical Structures Affected

- **Primary organs / sites (UBERON):** skin (UBERON:0002097) at the inoculation site — the ulcer; and **regional lymph nodes** (UBERON:0000029) draining that site (e.g., axillary, inguinal, epitrochlear; cervical in children).
- **Secondary involvement:** In disseminated/severe disease, spleen (UBERON:0002106) and liver (UBERON:0002107) can be affected (demonstrated in mouse models with pathological changes in spleen and liver, [PMID: 27477000](https://pubmed.ncbi.nlm.nih.gov/27477000/)); lungs (UBERON:0002048) in pneumonic progression (less common in ulceroglandular).
- **Body systems:** integumentary and lymphatic/immune systems primarily; reticuloendothelial system secondarily.
- **Tissue / cell level:** epithelial and connective tissue of skin; lymphoid tissue; principal cellular niche is the **macrophage** (CL:0000235).
- **Subcellular level (GO cellular component):** phagosome / *Francisella*-containing phagosome (GO:0045335) and host **cytosol** (GO:0005829) — the replicative compartment.
- **Localization / lateralization:** Unilateral, following the site of the bite/inoculation; lymphadenopathy is typically ipsilateral to the ulcer.

---

## Section 8 — Temporal Development

- **Onset:** Acquired at any age; **incubation 3–6 days** after subcutaneous inoculation ([PMID: 3892222](https://pubmed.ncbi.nlm.nih.gov/3892222/)). Onset is **acute**.
- **Progression / stages:** (i) local papule → ulcer; (ii) regional painful lymphadenopathy; (iii) possible suppuration/drainage of involved nodes, particularly when antibiotics are started late — *"Late initiation antibiotic therapy could not prevent suppuration and draining of the involved lymph nodes"* ([PMID: 16936340](https://pubmed.ncbi.nlm.nih.gov/16936340/)).
- **Immune timeline:** T-cell response detectable at 1–2 weeks; antibody at 2–3 weeks ([PMID: 3892222](https://pubmed.ncbi.nlm.nih.gov/3892222/)).
- **Course / duration:** Self-limiting to resolving with therapy; generally **not** chronic or lifelong. Prognosis good for the ulceroglandular form.
- **Critical intervention window:** Early antibiotic initiation is the key intervention; late therapy cannot always prevent lymph-node suppuration ([PMID: 16936340](https://pubmed.ncbi.nlm.nih.gov/16936340/)).

---

## Section 9 — Inheritance and Population

- **Inheritance:** **Not applicable** — infectious, non-heritable. Penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, and carrier frequency are all not applicable.
- **Epidemiology (US):** Average annual incidence **0.064/100,000 (2011–2022)**, 56% higher than 2001–2010 (0.041). *"During 2011-2022, a total of 47 states reported 2,462 tularemia cases, but four central states (Arkansas, Kansas, Missouri, and Oklahoma) accounted for 50% of all reported cases"* ([PMID: 39736154](https://pubmed.ncbi.nlm.nih.gov/39736154/)). During 2001–2010, *"a total of 1,208 cases were reported (median: 126.5 cases per year; range: 90-154)"* ([PMID: 24280916](https://pubmed.ncbi.nlm.nih.gov/24280916/)). Reported from all US states except Hawaii.
- **Age / sex:** Bimodal — *"Incidence was highest among children aged 5-9 years (0.083 per 100,000 population) and adult males aged 65-84 years (range = 0.133-0.161)"* ([PMID: 39736154](https://pubmed.ncbi.nlm.nih.gov/39736154/)). Male predominance.
- **Race/ethnicity:** *"Incidence among American Indian or Alaska Native persons (0.260) was approximately five times that among White persons (0.057)"* ([PMID: 39736154](https://pubmed.ncbi.nlm.nih.gov/39736154/)).
- **Geographic distribution:** Holarctic (Northern Hemisphere). In Europe, subsp. *holarctica* (type B) predominates; the Czech Republic reports up to ~100 cases/yr (225 and 222 in the 1998–1999 epidemic years) ([PMID: 32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/)). Ulceroglandular is the most common form reported from Poland ([PMID: 34696556](https://pubmed.ncbi.nlm.nih.gov/34696556/)); oropharyngeal predominates in Turkey (water-borne outbreaks).

---

## Section 10 — Diagnostics

- **Serology (mainstay):** microagglutination test (MAT), titer **≥1/160 positive** — *"microagglutination test (MAT) was performed for all patients whose clinical symptoms were consistent with tularemia and MAT titers ≥ 1/160 were considered positive"* ([PMID: 29642835](https://pubmed.ncbi.nlm.nih.gov/29642835/)); some centers use ≥1:640 in outbreak settings ([PMID: 21341160](https://pubmed.ncbi.nlm.nih.gov/21341160/)). A four-fold rise between acute and convalescent sera is confirmatory. Antibody appears at 2–3 weeks.
- **PCR / NAAT:** Positive on **lymph-node aspiration material** and ulcer swabs — *"PCR for F. tularensis was positive in aspiration material of suppurated lymphadenitis of 7 patients"* ([PMID: 16936340](https://pubmed.ncbi.nlm.nih.gov/16936340/)). RD1-primer PCR can subtype to subsp. *holarctica* ([PMID: 21341160](https://pubmed.ncbi.nlm.nih.gov/21341160/)).
- **Direct fluorescent antibody (DFA):** Applicable to lymph aspirates.
- **Culture:** Definitive but **hazardous** — requires **BSL-3** containment; low sensitivity from routine specimens (cultures often negative) ([PMID: 21341160](https://pubmed.ncbi.nlm.nih.gov/21341160/)).
- **Routine labs:** Nonspecific (mild WBC changes, elevated ESR/CRP) ([PMID: 21341160](https://pubmed.ncbi.nlm.nih.gov/21341160/)).
- **Genetic / omics testing:** Not applicable for host diagnosis (no human genetic testing, karyotyping, CMA, or repeat-expansion testing). Pathogen genomics is used for subtyping/epidemiology.
- **Differential diagnosis:** cat-scratch disease, pyogenic bacterial lymphadenitis, plague, cutaneous anthrax, sporotrichosis, atypical mycobacterial infection, syphilitic chancre, and (in the neck) tonsillopharyngitis / neck mass of unknown origin ([PMID: 34696556](https://pubmed.ncbi.nlm.nih.gov/34696556/); [PMID: 21341160](https://pubmed.ncbi.nlm.nih.gov/21341160/)). Diagnosis is often **delayed** because of low prevalence and nonspecific features.

---

## Section 11 — Outcome / Prognosis

- **Prognosis:** **Good** for the ulceroglandular form — the pathogen is well contained by a vigorous inflammatory reaction, pneumonia is less common, and outcomes are favorable ([PMID: 3892222](https://pubmed.ncbi.nlm.nih.gov/3892222/)).
- **Case fatality:** Low with treatment — *"Among patients treated with aminoglycosides (n = 452 [52%]), fluoroquinolones (n = 339 [39%]), or tetracyclines (n = 419 [48%]), the fatality rate was 0.7%, 0.9%, and 1.2%, respectively"* ([PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/)). US surveillance case-fatality is typically <2%.
- **Complications:** Suppurative lymphadenitis with drainage (favored by late therapy) ([PMID: 16936340](https://pubmed.ncbi.nlm.nih.gov/16936340/)); rarely dissemination.
- **Prognostic factors:** **Timeliness of antibiotic initiation** is the key modifiable factor; clinical form (ulceroglandular better than typhoidal/pneumonic) and subspecies (type B milder than type A) shape outcome.

---

## Section 12 — Treatment

| Drug class | Examples | Role | Fatality in review | NCIT |
|---|---|---|---|---|
| Aminoglycosides | Streptomycin, gentamicin | First-line / treatment of choice | 0.7% (n=452) | NCIT:C255 (Aminoglycoside) |
| Fluoroquinolones | Ciprofloxacin | Effective alternative / PEP | 0.9% (n=339) | NCIT:C1728 (Ciprofloxacin) |
| Tetracyclines | Doxycycline | Alternative / PEP | 1.2% (n=419) | NCIT:C641 (Doxycycline) |

- **First-line:** Streptomycin or gentamicin (aminoglycosides) are the treatment of choice ([PMID: 29183485](https://pubmed.ncbi.nlm.nih.gov/29183485/); [PMID: 41026652](https://pubmed.ncbi.nlm.nih.gov/41026652/)). *"Quinolones, tetracyclines, or aminoglycosides are frequently used in the treatment of tularemia"* ([PMID: 32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/)).
- **Timing matters:** Late initiation cannot always prevent lymph-node suppuration and drainage ([PMID: 16936340](https://pubmed.ncbi.nlm.nih.gov/16936340/)).
- **Surgical/interventional:** Incision and drainage or excision of suppurative nodes may be needed as adjunct.
- **Advanced/targeted/gene/cell/RNA therapies:** Not applicable.
- **Pharmacogenomics:** Not applicable (no host-genotype-guided dosing established for this indication).
- **Treatment algorithm:** Empiric aminoglycoside for confirmed/strongly suspected disease; doxycycline or ciprofloxacin for milder disease or when aminoglycosides are contraindicated; drainage for suppurative nodes; CDC 2025 guidance governs both naturally acquired and bioterrorism-response treatment ([PMID: 41026652](https://pubmed.ncbi.nlm.nih.gov/41026652/)).

---

## Section 13 — Prevention

- **Primary prevention:** Avoid arthropod bites (repellents, protective clothing, tick checks) and practice safe handling of animals/carcasses (gloves). Vector-ecology interventions (e.g., prescribed fire affecting tick populations) are studied ([PMID: 40788927](https://pubmed.ncbi.nlm.nih.gov/40788927/)).
- **Immunization:** **No licensed vaccine.** *"No licensed vaccine is available in the prophylaxis of tularemia and this is need of the time and high-priority research area"* ([PMID: 32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/)). The Live Vaccine Strain (LVS) remains investigational ([PMID: 42238599](https://pubmed.ncbi.nlm.nih.gov/42238599/)).
- **Post-exposure prophylaxis (PEP):** **Doxycycline or ciprofloxacin (≈14 days)** — *"Streptomycin, gentamicin, doxycycline or ciprofloxacin are recommended for post-exposure prophylaxis"* ([PMID: 15677845](https://pubmed.ncbi.nlm.nih.gov/15677845/)); CDC 2025 guidance details PEP after high-risk exposures ([PMID: 41026652](https://pubmed.ncbi.nlm.nih.gov/41026652/)).
- **Public-health context:** *F. tularensis* is a **Tier-1 Select Agent / Category A bioterrorism agent** — *"Because F. tularensis has a low infectious inoculum, it is classified as a potential bioterrorism agent that could infect thousands of persons if intentionally released"* ([PMID: 41026652](https://pubmed.ncbi.nlm.nih.gov/41026652/)); tularemia is a **notifiable disease** in the US.
- **Genetic screening / counseling:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy of hosts:** Broad — *"Tularemia is a bacterial disease of humans, wild, and domestic animals"* ([PMID: 32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/)). Natural reservoirs are **lagomorphs** (rabbits, hares) and **rodents**; arthropods (ticks, deer flies, mosquitoes) act as vectors/maintenance hosts. Tularemia is a Holarctic zoonosis ([PMID: 31600457](https://pubmed.ncbi.nlm.nih.gov/31600457/)).
- **Veterinary relevance:** Causes natural disease and die-offs in lagomorphs and rodents ("rabbit fever"); cats and dogs may become infected and transmit to humans.
- **Comparative biology:** Intracellular pathogenesis (FPI/T6SS-dependent macrophage infection) is conserved across mammalian hosts; this conservation underlies the utility of animal models.
- **Zoonotic transmission:** Strongly zoonotic — humans are incidental hosts infected via vector bite, animal contact, ingestion, or inhalation. Human-to-human transmission does not occur.

---

## Section 15 — Model Organisms

- **Principal model — mouse** (*Mus musculus*, NCBITaxon:10090): FPI/T6SS mutants (ΔiglB, ΔiglE, ΔpdpC) show *"incomplete phagosomal escape, and marked attenuation in the mouse model"* ([PMID: 23356941](https://pubmed.ncbi.nlm.nih.gov/23356941/)) and *"showed marked attenuation in the mouse model"* ([PMID: 27830989](https://pubmed.ncbi.nlm.nih.gov/27830989/)). C57BL/6 mice are used to assess FPI-mutant pathology in spleen/liver ([PMID: 27477000](https://pubmed.ncbi.nlm.nih.gov/27477000/)). Mouse **inhalation models** are used to assess vaccine efficacy and identify transcriptional/translational biomarkers ([PMID: 35056485](https://pubmed.ncbi.nlm.nih.gov/35056485/)).
- **In vitro models:** Macrophage cell lines **J774** and **THP-1**, and **human monocyte-derived macrophages (HMDM)** ([PMID: 27477000](https://pubmed.ncbi.nlm.nih.gov/27477000/)); HeLa-FcγRII epithelial model for *F. novicida* ([PMID: 40748985](https://pubmed.ncbi.nlm.nih.gov/40748985/)).
- **Surrogate strains:** *F. tularensis* LVS and *F. novicida* are widely used attenuated surrogates for mechanistic and vaccine studies ([PMID: 22493083](https://pubmed.ncbi.nlm.nih.gov/22493083/)).
- **Phenotype recapitulation:** Mouse models faithfully reproduce intracellular replication, dissemination to spleen/liver, and lethality, and are the standard for vaccine-efficacy testing.
- **Limitations:** Attenuated surrogates (LVS, *F. novicida*) do not fully model virulent type A disease; localized ulceroglandular skin pathology is less emphasized than systemic/pulmonary endpoints in murine work.

---

## Mechanistic Model / Interpretation

```
 Arthropod bite / animal contact  (~10 organisms)
              │  (cutaneous inoculation)
              ▼
   Local deposition in skin ──► phagocyte uptake (macrophage/PMN)
              │
              ▼
   FPI / T6SS  ──►  PHAGOSOMAL ESCAPE  ──►  cytosolic replication
              │                                   │
              ▼                                   ▼
   PGE2 (immune dampening)          Inflammasome (IL-1β) + host-cell death
              │                                   │
              └───────────────┬───────────────────┘
                              ▼
        Drainage to regional lymph node → granulomatous / suppurative
        lymphadenitis  +  skin ULCER at entry site
                              │
             ┌────────────────┴─────────────────┐
             ▼ (ulceroglandular)                ▼ (typhoidal)
   Well contained → GOOD prognosis     Poor containment → pneumonia,
   (T-cell/IFN-γ control at 1–2 wk)    higher untreated mortality
```

The unifying insight is that a **single molecular machine (the FPI-encoded T6SS)** converts *F. tularensis* from an ingested particle into a cytosolic replicating pathogen, and that the **balance between vigorous local cell-mediated immunity and bacterial containment** determines whether disease stays localized (ulceroglandular, good outcome) or disseminates (typhoidal/pneumonic, worse outcome). Because control is cell-mediated and antibody is comparatively unhelpful for killing, both diagnosis (serology at 2–3 weeks) and vaccine development (needing T-cell immunity) are shaped by this biology.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/) | *Systematic Review: Clinical Features, Treatment, Outcomes 1993–2023* | Ulceroglandular = most common form; treatment-specific fatality; low infectious dose |
| [32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/) | *Tularemia: a re-emerging tick-borne disease* | Clinical forms; transmission; antibiotics; no vaccine; zoonosis |
| [3892222](https://pubmed.ncbi.nlm.nih.gov/3892222/) | *Tularemia: 30-year experience, 88 cases* | Incubation 3–6 d; two-syndrome framework; cell-mediated immunity; good prognosis |
| [27830989](https://pubmed.ncbi.nlm.nih.gov/27830989/) | *IglE controls T6SS secretion* | FPI/T6SS → phagosomal escape → cytosolic replication; mouse attenuation |
| [23356941](https://pubmed.ncbi.nlm.nih.gov/23356941/) | *LVS ΔpdpC phenotype* | Intramacrophage proliferation prerequisite; mouse-model attenuation |
| [23403609](https://pubmed.ncbi.nlm.nih.gov/23403609/) | *Francisella mutants failing PGE2 induction* | FPI required for escape/replication; PGE2 immune modulation |
| [27477000](https://pubmed.ncbi.nlm.nih.gov/27477000/) | *ΔpdpC/ΔiglG characterization* | HMDM/mouse models; spleen/liver pathology; PdpC regulation of iglABCD |
| [16936340](https://pubmed.ncbi.nlm.nih.gov/16936340/) | *Tularemia in NW Turkey* | Late therapy → suppuration; PCR of node aspirates |
| [29642835](https://pubmed.ncbi.nlm.nih.gov/29642835/) | *Oropharyngeal tularemia, E. Anatolia* | MAT ≥1/160 diagnostic threshold |
| [39736154](https://pubmed.ncbi.nlm.nih.gov/39736154/) | *Tularemia — US, 2011–2022* | US incidence, geography, age/sex, race disparities |
| [24280916](https://pubmed.ncbi.nlm.nih.gov/24280916/) | *Tularemia — US, 2001–2010* | Earlier surveillance; bimodal age/sex |
| [34990926](https://pubmed.ncbi.nlm.nih.gov/34990926/) | *Cervical lymphadenopathy in children after tick bite* | Pediatric ulceroglandular; animal-handling route in Europe |
| [42238599](https://pubmed.ncbi.nlm.nih.gov/42238599/) | *Tularemia & vaccination T-cell responses* | LVS/natural infection → multifunctional T cells |
| [15677845](https://pubmed.ncbi.nlm.nih.gov/15677845/) / [29183485](https://pubmed.ncbi.nlm.nih.gov/29183485/) | *Bichat guidelines* | First-line aminoglycosides; PEP with doxycycline/ciprofloxacin |
| [41026652](https://pubmed.ncbi.nlm.nih.gov/41026652/) | *CDC 2025 treatment/prophylaxis* | Bioterrorism classification; treatment & PEP recommendations |
| [40788927](https://pubmed.ncbi.nlm.nih.gov/40788927/) | *Prescribed fire & tick vectors* | Principal US tick vectors (*D. variabilis*, *A. americanum*) |
| [22493083](https://pubmed.ncbi.nlm.nih.gov/22493083/) | *Perforin/granzyme protection* | Cytotoxic effector immunity in vaccine protection (model) |
| [35056485](https://pubmed.ncbi.nlm.nih.gov/35056485/) | *Vaccine biomarkers, mouse inhalation* | Mouse inhalation model for vaccine efficacy |
| [29761532](https://pubmed.ncbi.nlm.nih.gov/29761532/) | *Dermatological aspects, 168 cases* | Secondary skin manifestations; form distribution |
| [31600457](https://pubmed.ncbi.nlm.nih.gov/31600457/) | *Ecology of Francisella* | Holarctic zoonosis; reservoir ecology |

---

## Limitations and Knowledge Gaps

1. **Not a genetic disease.** Sections on host causal genes, pathogenic variants, inheritance, penetrance, epigenetics, and genetic testing are **not applicable**; the report reframes "molecular" content around bacterial virulence.
2. **Form-specific data are sparse.** Much clinical data aggregate *all* tularemia; some cited series (Turkey) are oropharyngeal-predominant, so treatment/outcome numbers are partly extrapolated to the ulceroglandular form.
3. **Quality-of-life data absent.** No EQ-5D/SF-36/PROMIS instruments have been applied specifically to ulceroglandular tularemia.
4. **Human mechanistic evidence is indirect.** Core pathogenesis (FPI/T6SS, phagosomal escape) rests on cell-culture and mouse studies; direct human histopathological causal steps are inferred.
5. **Diagnostic thresholds vary** (MAT ≥1/160 vs ≥1:640) across labs/outbreaks.
6. **Vaccine gap.** No licensed vaccine; correlates of protective immunity in humans remain incompletely defined.

---

## Proposed Follow-up Experiments / Actions

1. **Form-stratified outcome analysis** — mine the 870-case systematic-review dataset for ulceroglandular-only fatality, suppuration rate, and time-to-treatment thresholds.
2. **Prospective PROs** — apply EQ-5D/SF-36 in an endemic-region cohort to quantify acute and residual QoL impact of ulceroglandular disease.
3. **Time-to-antibiotic study** — formally test whether treatment within a defined window (e.g., ≤7 days) prevents lymph-node suppuration.
4. **Host-immunogenetics** — although not Mendelian, explore whether host innate-immune polymorphisms (inflammasome, IFN-γ pathway) modulate ulceroglandular severity via candidate-gene/GWAS approaches.
5. **Vaccine correlates** — leverage multifunctional T-cell signatures ([PMID: 42238599](https://pubmed.ncbi.nlm.nih.gov/42238599/)) and mouse-model biomarkers ([PMID: 35056485](https://pubmed.ncbi.nlm.nih.gov/35056485/)) to define human protective correlates for LVS-successor vaccines.
6. **Skin-model development** — an intradermal small-animal model recapitulating the ulcer-plus-node phenotype would fill the gap left by systemic/pulmonary-focused mouse work.

---

*Report compiled from 10 confirmed findings across 5 investigation iterations and 38 reviewed papers. Evidence types: human clinical (case series, systematic reviews, national surveillance), model organism (mouse), and in vitro (macrophage cell lines/HMDM).*


## Artifacts

- [OpenScientist final report](Ulceroglandular_Tularemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Ulceroglandular_Tularemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 12 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0200042` (2 mentions) - the report calls it "Physical manifestation"; HP calls it **Skin ulcer**
- `HP:0001945` (1 mention) - the report calls it "Symptom / sign"; HP calls it **Fever**
- `HP:0002218` (1 mention) - the report calls it "Clinical sign"; HP calls it **Silver-gray hair**
- `UBERON:0002106` (1 mention) - the report calls it "Secondary involvement:** In disseminated/severe disease, spleen"; UBERON calls it **spleen**
- `NCIT:C255` (1 mention) - the report calls it "Aminoglycoside"; NCIT calls it **Urinary Anti-Infective Agent**
- `NCIT:C1728` (1 mention) - the report calls it "Ciprofloxacin"; NCIT calls it **Celecoxib**
- `NCIT:C641` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Methimazole**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000029` (1 mention) - the report calls it "regional lymph nodes"; UBERON calls it **lymph node**