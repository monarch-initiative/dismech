---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-11T11:46:52.934210'
end_time: '2026-09-11T12:01:43.963733'
duration_seconds: 891.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Marshall Syndrome
  mondo_id: MONDO:0007949
  category: Genetic
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
citation_count: 20
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 19
  relevance_assessed: 22
  on_topic: 18
  validator_version: 0.2.1
term_validation:
  total_terms: 25
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 7
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0007949
    reported_labels:
    - MONDO
    ontology_label: Marshall syndrome
  - term_id: HP:0011003
    reported_labels:
    - Progressive
    ontology_label: High myopia
  - term_id: HP:0000518
    reported_labels:
    - Progressive
    ontology_label: Cataract
  - term_id: HP:0000501
    reported_labels:
    - Progressive
    ontology_label: Glaucoma
  - term_id: HP:0000407
    reported_labels:
    - Progressive
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0000175
    reported_labels:
    - Stable
    ontology_label: Cleft palate
  - term_id: UBERON:0001796
    reported_labels:
    - anterior chamber region, approximate
    ontology_label: aqueous humor of eyeball
  - term_id: UBERON:0001800
    reported_labels:
    - vitreous humor, approximate
    ontology_label: sensory ganglion
  - term_id: UBERON:0001709
    reported_labels:
    - mid-face region, approximate
    ontology_label: upper jaw region
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Marshall_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Marshall_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Marshall Syndrome
- **MONDO ID:** MONDO:0007949 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Marshall Syndrome** covering all of the
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

# Marshall Syndrome (COL11A1): Comprehensive Disease Characteristics Report

**Disease:** Marshall Syndrome
**MONDO ID:** MONDO:0007949 | **OMIM:** 154780
**Category:** Genetic (autosomal-dominant type XI collagenopathy)
**Report date:** 2026-09-11

---

## Summary

Marshall syndrome (MONDO:0007949; OMIM 154780) is an ultra-rare, autosomal-dominant hereditary connective-tissue disorder — a **type XI collagenopathy** — caused by heterozygous mutations in **COL11A1**, the gene encoding the α1 chain of collagen XI. Its molecular signature is a class of **splicing mutations affecting the 54-base-pair (54-bp) exons in the C-terminal region of the gene** (notably a recurrent intron-50 splice-site hot spot, e.g., c.3816+1G>A), which cause **in-frame exon skipping** and the production of a shortened proα1(XI) chain. Because this mutant chain still co-assembles with normal collagen chains, it exerts a **dominant-negative effect**, disrupting the assembly of heterotypic collagen II/XI fibrils in cartilage, ocular vitreous, and the inner ear. The result is a recognizable multisystem phenotype.

Clinically, Marshall syndrome presents from **infancy** with a cardinal triad: (1) **midfacial hypoplasia** with a flat/depressed nasal bridge, (2) **ocular abnormalities** — high myopia, congenital or juvenile cataract, and vitreoretinal degeneration carrying a lifelong retinal-detachment risk — and (3) **early-onset, progressive, predominantly cochlear sensorineural hearing loss**. Additional features include skeletal abnormalities, short stature, and early-onset osteoarthritis. The disorder overlaps substantially with **Stickler syndrome type 2 (STL2)**, which is allelic (also COL11A1); early severe hearing loss and characteristic facial features are the features most often used to classify a patient as "Marshall" rather than "Stickler." Expressivity is highly variable even within a single family.

There is **no curative or disease-modifying therapy**. Management is **multidisciplinary and symptomatic**, following the closely related Stickler syndrome paradigm: retinal surveillance and prophylaxis (given that this collagenopathy spectrum is the most common inherited cause of childhood retinal detachment), cataract surgery, hearing amplification or cochlear implantation, orthopedic and rheumatologic care, and genetic counseling. A critical practical caveat is **eponym ambiguity**: "Marshall syndrome" also denotes two entirely unrelated conditions — **PFAPA** (Periodic Fever, Aphthous stomatitis, Pharyngitis, Adenitis; the common pediatric autoinflammatory disease) and **acquired cutis laxa type II** (post-inflammatory elastolysis). This report concerns exclusively the genetic COL11A1 ophthalmo-oto-skeletal disorder.

---

## 1. Disease Information

**Overview.** Marshall syndrome is a dominantly inherited connective-tissue disorder characterized by craniofacial and skeletal abnormalities, sensorineural hearing loss, myopia, and cataracts, associated with splicing mutations in *COL11A1* ([PMID: 10889003](https://pubmed.ncbi.nlm.nih.gov/10889003/)). It is best understood as sitting within the **type II/IX/XI collagenopathy spectrum**, which "encompass[es] Stickler syndrome and a spectrum of related connective tissue disorders with diverse and overlapping phenotypes" ([PMID: 41856555](https://pubmed.ncbi.nlm.nih.gov/41856555/)).

**Key identifiers.**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0007949 |
| OMIM | 154780 |
| COL11A1 gene locus (Stickler type 2) | OMIM 120280 |
| Related gene COL11A2 (OSMED/STL3) | OMIM 120290 |

**Synonyms and alternative names.** Marshall syndrome (genetic); it is frequently discussed jointly as "Stickler (Marshall) syndrome" ([PMID: 9235398](https://pubmed.ncbi.nlm.nih.gov/9235398/)) given the overlap with Stickler syndrome type 2. **Important disambiguation** — the eponym is shared by unrelated disorders:
- **PFAPA syndrome** (Periodic Fever, Aphthous stomatitis, Pharyngitis, Adenitis), an autoinflammatory disease ([PMID: 38354003](https://pubmed.ncbi.nlm.nih.gov/38354003/); [PMID: 37751263](https://pubmed.ncbi.nlm.nih.gov/37751263/)).
- **Acquired cutis laxa type II** (post-inflammatory elastolysis) ([PMID: 34929762](https://pubmed.ncbi.nlm.nih.gov/34929762/)).

**Source of information.** Knowledge here is derived predominantly from **aggregated disease-level resources** (OMIM, Orphanet) and from **individual and small-family clinical case reports/series** (e.g., a single 8-member Tunisian family, [PMID: 26367406](https://pubmed.ncbi.nlm.nih.gov/26367406/); a single longitudinal case followed to age 12.5 years, [PMID: 38062645](https://pubmed.ncbi.nlm.nih.gov/38062645/)), not from EHR-scale cohorts. This reflects the ultra-rare status of the disease.

---

## 2. Etiology

**Primary cause — genetic.** Marshall syndrome is a monogenic disorder caused by **heterozygous mutations in COL11A1**. The characteristic mutation class is **splicing mutations of the 54-bp exons in the C-terminal region of the gene**. Genotype–phenotype analysis "revealed an association between the Marshall syndrome phenotype and splicing mutations of 54-bp exons in the C-terminal region of the COL11A1 gene," whereas other COL11A1 mutation types produce overlapping Marshall/Stickler phenotypes ([PMID: 10486316](https://pubmed.ncbi.nlm.nih.gov/10486316/)).

**Genetic risk factors / causal variants.** Recurrent variants include the **intron-50 splice hot spot** (in a cohort of 10 COL11A1 patients, the 4 classified as Marshall syndrome were all heterozygous for a splice-site mutation in intron 50; [PMID: 17236192](https://pubmed.ncbi.nlm.nih.gov/17236192/)), and specific reported variants **c.2702G>A (p.Gly901Glu)**, **IVS50+1G>A**, and **IVS50+1G>C** ([PMID: 25073711](https://pubmed.ncbi.nlm.nih.gov/25073711/)). Most cases are dominant; a **recessive** form exists (see §9).

**Environmental risk factors / protective factors / gene–environment interactions.** As a monogenic dominant-negative collagenopathy, Marshall syndrome has **no established environmental risk factors, protective factors, or gene–environment interactions**. Disease occurrence is determined by the COL11A1 genotype. (No data available.)

---

## 3. Phenotypes

The cardinal triad and its supporting phenotypes are summarized below. Onset is congenital/infantile; ocular, auditory, and articular components are **progressive**; expressivity is **highly variable**.

| Phenotype | Type | Onset | Course | Suggested HPO term |
|-----------|------|-------|--------|--------------------|
| Midfacial hypoplasia / flat nasal bridge | Physical/craniofacial sign | Congenital | Stable structural | HP:0000426 (depressed nasal bridge); HP:0011800 (midface retrusion) |
| High myopia | Ocular sign | Childhood | Progressive | HP:0011003 |
| Cataract (congenital/juvenile) | Ocular sign | Congenital–childhood | Progressive | HP:0000518 |
| Vitreoretinal degeneration / retinal detachment risk | Ocular sign | Childhood onward | Progressive | HP:0000541 (retinal detachment) |
| Glaucoma / goniodysgenesis | Ocular sign | Variable | Progressive | HP:0000501 |
| Lens subluxation / coloboma (rare) | Ocular sign | Variable | Stable/progressive | HP:0001083 (ectopia lentis) |
| Sensorineural hearing loss (cochlear, early, severe) | Auditory sign | Early childhood | Progressive | HP:0000407 |
| Cleft/submucosal cleft palate | Craniofacial sign | Congenital | Stable | HP:0000175 |
| Skeletal abnormalities / short stature | Skeletal sign | Congenital–childhood | Variable | HP:0004322 (short stature) |
| Early-onset arthritis/arthropathy | Musculoskeletal sign | Young adult | Progressive | HP:0003088 (premature osteoarthritis) |

**Supporting evidence.** "Characteristic features of Marshall syndrome include midfacial hypoplasia, high myopia, and sensorineural-hearing deficit" ([PMID: 25073711](https://pubmed.ncbi.nlm.nih.gov/25073711/)). Marshall syndrome is "characterized by craniofacial and skeletal abnormalities, sensorineural hearing loss, myopia, and cataracts" ([PMID: 10889003](https://pubmed.ncbi.nlm.nih.gov/10889003/)), with hearing loss that is "progressive... predominantly cochlear in origin." The Marshall phenotype was distinguished from Stickler "because of early-onset severe hearing loss and characteristic facial features" ([PMID: 17236192](https://pubmed.ncbi.nlm.nih.gov/17236192/)). Additional ocular features — high myopia, glaucoma and goniodysgenesis, congenital cataract, and lens subluxation/coloboma — are documented in [PMID: 9235398](https://pubmed.ncbi.nlm.nih.gov/9235398/). The broader COL11A1/collagenopathy spectrum is "characterized by a distinctive craniofacial appearance, high myopia, vitreoretinal degeneration, hearing loss, and early-onset arthritis" ([PMID: 41715899](https://pubmed.ncbi.nlm.nih.gov/41715899/)).

**Quality-of-life impact.** Per-phenotype QoL instruments (EQ-5D, SF-36) have not been applied to this ultra-rare disease. Qualitatively, the combination of progressive vision loss (with retinal-detachment risk), progressive deafness, and early osteoarthritis imposes substantial lifelong sensory and musculoskeletal disability requiring continuous multidisciplinary support ([PMID: 38062645](https://pubmed.ncbi.nlm.nih.gov/38062645/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** **COL11A1** (HGNC:2186; chromosome 1p21.1), encoding the α1(XI) chain of collagen type XI. OMIM gene entry 120280.

**Pathogenic variants.**
- **Variant classes:** predominantly **splice-site mutations** at the 54-bp C-terminal exons (the Marshall-defining class; [PMID: 10486316](https://pubmed.ncbi.nlm.nih.gov/10486316/)); also **missense** (e.g., c.2702G>A / p.Gly901Glu; c.4526A>G / p.Gln1509Arg reported in STL2, [PMID: 38299479](https://pubmed.ncbi.nlm.nih.gov/38299479/)) and **large exon deletions**.
- **Recurrent variants:** intron-50 splice hot spot (IVS50+1G>A recurrent) ([PMID: 17236192](https://pubmed.ncbi.nlm.nih.gov/17236192/); [PMID: 25073711](https://pubmed.ncbi.nlm.nih.gov/25073711/)).
- **Origin:** germline; most dominant cases arise as inherited or de novo heterozygous variants.
- **Functional consequence:** **dominant-negative**. Splice mutations cause exon skipping that, because of the exon structure of collagen genes, "usually leaves the message in-frame. The mutant protein then exerts a dominant negative effect as it co-assembles with other collagen gene products" ([PMID: 23621912](https://pubmed.ncbi.nlm.nih.gov/23621912/)).
- **Deletion detection:** large intragenic deletions are missed by exon sequencing; "diagnostic screening of COL11A1 should include assays capable of detecting both large and small deletions, in addition to exon sequencing" (MLPA) ([PMID: 23621912](https://pubmed.ncbi.nlm.nih.gov/23621912/)).

**Allele frequency.** Pathogenic COL11A1 variants are absent or ultra-rare in population databases (gnomAD), consistent with the <1 in 1,000,000 disease prevalence. (Specific per-variant frequencies not compiled here.)

**Modifier genes / epigenetics / chromosomal abnormalities.** No established modifier genes or epigenetic mechanisms are described for Marshall syndrome; it is not associated with gross chromosomal abnormalities. (No data available.)

**Ontology suggestions:** gene product collagen XI α1 chain; GO:0005581 (collagen trimer); GO:0030020 (extracellular matrix structural constituent conferring tensile strength).

---

## 5. Environmental Information

Marshall syndrome is a **purely genetic disorder**. There are **no established environmental factors, lifestyle factors, or infectious agents** contributing to its causation or triggering. This distinguishes the genetic COL11A1 disorder from the identically named PFAPA (autoinflammatory) and acquired cutis laxa (post-inflammatory) conditions, whose pathogenesis does involve inflammatory/environmental triggers. (No data available for the genetic disorder.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous COL11A1 splice mutation of a 54-bp C-terminal exon** *leads to* aberrant splicing (**demonstrated**; [PMID: 10486316](https://pubmed.ncbi.nlm.nih.gov/10486316/)).
2. This *results in* **in-frame exon skipping**, because the exon structure of fibrillar collagen genes keeps the reading frame intact (**demonstrated**; [PMID: 23621912](https://pubmed.ncbi.nlm.nih.gov/23621912/)).
3. The message *is translated into* a **stably shortened proα1(XI) chain** that co-assembles with wild-type collagen chains and *exerts* a **dominant-negative effect** (**demonstrated functionally**; [PMID: 23621912](https://pubmed.ncbi.nlm.nih.gov/23621912/)).
4. The defective chain *causes* **failure to nucleate and regulate heterotypic collagen II/XI fibrils**, since "collagen XI is essential for normal formation of cartilage collagen fibrils and the cohesive properties of cartilage" (**demonstrated in the cho/cho mouse**; [PMID: 7859283](https://pubmed.ncbi.nlm.nih.gov/7859283/)).
5. This fibril-assembly failure then **branches** to the three affected tissues:
   - **5a — Skeletal branch:** disrupted growth-plate chondrocyte organization *causes* **midfacial hypoplasia, skeletal dysplasia, short stature** (**demonstrated in mouse and zebrafish models**; [PMID: 7859283](https://pubmed.ncbi.nlm.nih.gov/7859283/); [PMID: 36278545](https://pubmed.ncbi.nlm.nih.gov/36278545/)).
   - **5b — Ocular branch:** abnormal vitreous collagen *causes* **high myopia, vitreoretinal degeneration, and retinal-detachment risk** (**inferred from ocular phenotype and collagenopathy biology**; [PMID: 9235398](https://pubmed.ncbi.nlm.nih.gov/9235398/); [PMID: 21466760](https://pubmed.ncbi.nlm.nih.gov/21466760/)).
   - **5c — Auditory branch:** membranous-labyrinth dysfunction *causes* **progressive cochlear sensorineural hearing loss** — the deficit is "not caused by defective morphogenesis of the osseous labyrinth, but by more direct effects of the COL11A1 mutation on the membranous labyrinth and the central nervous system" (**demonstrated by audiovestibular phenotyping**; [PMID: 10889003](https://pubmed.ncbi.nlm.nih.gov/10889003/)).

### ASCII schematic

```
COL11A1 54-bp exon splice mutation (heterozygous)
        │  (demonstrated: PMID 10486316)
        ▼
In-frame exon skipping → shortened proα1(XI) chain
        │  (demonstrated: PMID 23621912)
        ▼
Co-assembly with WT chains → DOMINANT-NEGATIVE collagen XI
        │  (demonstrated: PMID 23621912)
        ▼
Failed nucleation/regulation of collagen II/XI heterotypic fibrils
        │  (demonstrated cho/cho mouse: PMID 7859283)
        ├───────────────┬────────────────────┐
        ▼               ▼                     ▼
  Cartilage/         Ocular vitreous     Membranous labyrinth
  growth plate       collagen defect     (inner ear)
        │               │                     │
        ▼               ▼                     ▼
  Midface hypoplasia  High myopia,        Progressive cochlear
  skeletal dysplasia, vitreoretinal       sensorineural
  short stature,      degeneration,       hearing loss
  early OA            retinal detachment   (PMID 10889003)
  (PMID 7859283,      (PMID 9235398,
   36278545)          21466760)
```

**Molecular pathways / cellular processes.** The core defect is in **extracellular-matrix (ECM) structural assembly** rather than a signaling cascade; collagen XI acts as a template regulating collagen II fibril diameter. Affected biological processes include collagen fibril organization (GO:0030199), cartilage development (GO:0051216), and skeletal system morphogenesis (GO:0048705). Cell types involved: **chondrocytes** (CL:0000138), **growth-plate chondrocytes**, and inner-ear supporting/sensory cells.

**Protein dysfunction.** Loss/dominant-negative alteration of the **α1(XI) collagen chain**; the shortened chain poisons the heterotrimer. Subcellular compartments: **endoplasmic reticulum** (procollagen folding/secretion; GO:0005788) and **extracellular matrix/collagen trimer** (GO:0005581).

**Molecular profiling / advanced technologies.** No transcriptomic, proteomic, metabolomic, single-cell, or CRISPR-screen datasets specific to Marshall syndrome were identified. Mechanistic evidence derives from mutation analysis and animal models. (No omics data available.)

---

## 7. Anatomical Structures Affected

**Organ level (primary):** craniofacial skeleton (midface, nasal bridge), **eyes** (vitreous, retina, lens, anterior-chamber angle), **inner ear** (membranous labyrinth/cochlea), and **skeleton/joints** (growth plates, epiphyses).

**Body systems:** musculoskeletal, special-sense (ophthalmic and auditory), and craniofacial. Secondary involvement includes retinal detachment (ocular complication) and early osteoarthritis (articular).

**Tissue and cell level:** **cartilage** (connective tissue) — the primary site of collagen XI action; growth-plate and articular **chondrocytes** (CL:0000138). Ocular **vitreous collagen** matrix; **inner-ear membranous labyrinth** epithelium.

**Subcellular level:** endoplasmic reticulum (GO:0005788, procollagen synthesis/folding) and extracellular matrix/collagen trimer (GO:0005581).

**Localization / lateralization:** **bilateral**, largely **symmetric** involvement of paired structures (eyes, ears). UBERON suggestions: UBERON:0002418 (cartilage tissue), UBERON:0001796 (anterior chamber region, approximate), UBERON:0001800 (vitreous humor, approximate), UBERON:0001846 (inner ear), UBERON:0001709 (mid-face region, approximate).

---

## 8. Temporal Development

**Onset:** **Congenital/infantile.** Marshall syndrome is "usually diagnosed in infancy" ([PMID: 38062645](https://pubmed.ncbi.nlm.nih.gov/38062645/)). Craniofacial features are present at birth; ocular and auditory features declare in early childhood. Onset pattern is **chronic/insidious**, not acute.

**Progression:** The disease course is **progressive** for the sensory and articular components. Hearing loss is "progressive... predominantly cochlear" ([PMID: 10889003](https://pubmed.ncbi.nlm.nih.gov/10889003/)); ocular disease (myopia, vitreoretinal degeneration) progresses with retinal-detachment risk across life; arthropathy is early-onset and progressive. Craniofacial structural features are comparatively **stable** after development.

**Disease course pattern / duration:** **Chronic, lifelong** (not self-limited, not relapsing-remitting). A longitudinal report followed one child from birth to age 12.5 years, documenting the chronic multisystem trajectory ([PMID: 38062645](https://pubmed.ncbi.nlm.nih.gov/38062645/)).

**Patterns / critical periods:** No spontaneous remission. **Critical windows for intervention** center on childhood ophthalmologic surveillance (to detect/prevent retinal detachment) and early auditory rehabilitation to support language acquisition.

---

## 9. Inheritance and Population

**Epidemiology.** Prevalence **<1 in 1,000,000** ("Marshall syndrome is an extremely rare genetic disorder usually diagnosed in infancy with a prevalence of <1 in 1 million"; [PMID: 38062645](https://pubmed.ncbi.nlm.nih.gov/38062645/)). Incidence figures are not established given the rarity.

**Inheritance.** Predominantly **autosomal dominant** ([PMID: 10889003](https://pubmed.ncbi.nlm.nih.gov/10889003/)). A recessive form exists: "the first report of autosomal recessive Marshall syndrome was from Saudi Arabia caused by the same mutation (c.2702G>A, p.Gly901Glu)" ([PMID: 25073711](https://pubmed.ncbi.nlm.nih.gov/25073711/)), implicating consanguinity in that setting.

**Penetrance / expressivity.** Penetrance is high; **expressivity is highly variable**, even within one family — "There is a variability of the clinical expression among the affected members of the study's family" (8-member Tunisian family; [PMID: 26367406](https://pubmed.ncbi.nlm.nih.gov/26367406/)).

**Anticipation / mosaicism / founder effects / carrier frequency.** No genetic anticipation (not a repeat-expansion disorder). Germline mosaicism, founder effects, and carrier frequencies are not specifically documented for this ultra-rare disorder. (No data available.)

**Population demographics.** No ethnic predilection is established for the dominant form; the recessive form was reported in a consanguineous Saudi context ([PMID: 25073711](https://pubmed.ncbi.nlm.nih.gov/25073711/)) and additional families have been reported from Tunisia ([PMID: 26367406](https://pubmed.ncbi.nlm.nih.gov/26367406/)). No sex predilection is described. Age distribution: recognized from infancy through adulthood.

---

## 10. Diagnostics

**Diagnostic strategy.** Diagnosis rests on **clinical recognition of the triad plus COL11A1 sequencing**, performed within a **type II/IX/XI collagenopathy multigene panel**. Commercial Stickler panels covering the six collagen genes (COL2A1, COL11A1, COL11A2, COL9A1, COL9A2, COL9A3) had a diagnostic yield of **50%**, higher with a positive family history (OR 2.6) or ocular signs (OR 2.2) ([PMID: 41856555](https://pubmed.ncbi.nlm.nih.gov/41856555/)).

**Genetic testing.**
- **Targeted panel / WES:** trio whole-exome sequencing is effective (e.g., identifying COL11A1 c.4526A>G p.Gln1509Arg) ([PMID: 38299479](https://pubmed.ncbi.nlm.nih.gov/38299479/)).
- **Deletion testing (MLPA):** required because exon sequencing misses large intragenic deletions — "diagnostic screening of COL11A1 should include assays capable of detecting both large and small deletions" ([PMID: 23621912](https://pubmed.ncbi.nlm.nih.gov/23621912/)).
- Karyotyping/CMA/mitochondrial/repeat-expansion testing are **not indicated** (this is a single-gene sequence-level disorder).

**Clinical / functional tests.** Ophthalmologic examination (refraction documenting high myopia, slit-lamp for cataract/lens position, dilated fundoscopy for vitreoretinal degeneration, gonioscopy/tonometry for glaucoma); **audiometry** documenting progressive cochlear SNHL; skeletal radiography showing characteristic Marshall radiological signs ([PMID: 26367406](https://pubmed.ncbi.nlm.nih.gov/26367406/)). Temporal-bone imaging typically shows a normal osseous labyrinth, consistent with a membranous-labyrinth mechanism ([PMID: 10889003](https://pubmed.ncbi.nlm.nih.gov/10889003/)).

**Differential diagnosis.** Stickler syndrome type 1 (COL2A1), Stickler type 2 (COL11A1 — allelic, overlapping), OSMED/Weissenbacher–Zweymüller (COL11A2; midface hypoplasia + deafness + epiphyseal dysplasia; [PMID: 9188673](https://pubmed.ncbi.nlm.nih.gov/9188673/)), autosomal-recessive Stickler (COL9A1/2/3; [PMID: 33570243](https://pubmed.ncbi.nlm.nih.gov/33570243/)), and fibrochondrogenesis (severe recessive COL11A1). A useful discriminator: Stickler type 1 hearing loss is "typically mild and not significantly progressive... less severe than that reported for types II and III... or the closely related Marshall syndrome" ([PMID: 11556853](https://pubmed.ncbi.nlm.nih.gov/11556853/)). **Critically, exclude the unrelated PFAPA and acquired cutis laxa "Marshall syndromes."**

**Screening.** No population newborn screening exists. **Cascade genetic testing** of at-risk relatives after a proband variant is identified is the appropriate approach.

---

## 11. Outcome / Prognosis

**Survival / mortality.** The dominant COL11A1 form is **not typically life-limiting**; life expectancy is essentially normal. (The severe recessive/fibrochondrogenesis end of the COL11A1 spectrum can be perinatally lethal, but that is a distinct severe phenotype; the murine null cho/cho model is neonatally lethal — [PMID: 7859283](https://pubmed.ncbi.nlm.nih.gov/7859283/) — reflecting complete loss of function rather than the human dominant-negative disorder.)

**Morbidity / function.** Substantial **sensory and musculoskeletal morbidity**: progressive vision impairment with retinal-detachment risk, progressive deafness, and early-onset osteoarthritis. These produce lifelong functional disability requiring rehabilitation and assistive devices ([PMID: 38062645](https://pubmed.ncbi.nlm.nih.gov/38062645/); [PMID: 41715899](https://pubmed.ncbi.nlm.nih.gov/41715899/)).

**Complications.** Retinal detachment (major, potentially blinding, partly preventable), cataract, glaucoma, and joint degeneration requiring possible arthroplasty.

**Prognostic factors.** Genotype (54-bp-exon splice mutations correlate with the more severe, early-hearing-loss Marshall phenotype; [PMID: 10486316](https://pubmed.ncbi.nlm.nih.gov/10486316/)) and access to ophthalmologic surveillance/prophylaxis influence the ocular outcome. No molecular prognostic biomarkers beyond genotype are established.

---

## 12. Treatment

**There is no curative or disease-modifying therapy.** No pharmacotherapy, gene therapy, cell therapy, RNA-based therapy, or targeted molecular therapy exists for COL11A1 Marshall syndrome. Care is **symptomatic, organ-specific, and multidisciplinary**, modeled on the closely related Stickler syndrome.

| Domain | Intervention | Evidence/notes | NCIT suggestion |
|--------|-------------|----------------|-----------------|
| Ophthalmic (retina) | Prophylactic retinal interventions (cryotherapy/laser) to reduce retinal-detachment risk; retinal-detachment repair | Stickler is "the most commonly identified inherited cause of retinal detachment in childhood," yet "there is no consensus regarding best practice and no current guidelines on prophylactic interventions" ([PMID: 21466760](https://pubmed.ncbi.nlm.nih.gov/21466760/)) | NCIT laser therapy / cryotherapy |
| Ophthalmic (other) | Refractive correction for high myopia; cataract surgery; glaucoma management | [PMID: 9235398](https://pubmed.ncbi.nlm.nih.gov/9235398/) | NCIT cataract extraction |
| Auditory | Hearing amplification; cochlear implantation for progressive cochlear SNHL | Cochlear origin supports implantation ([PMID: 10889003](https://pubmed.ncbi.nlm.nih.gov/10889003/)) | NCIT cochlear implant / hearing aid |
| Orthopedic/rheumatologic | Management of skeletal dysplasia and early osteoarthritis; joint replacement as needed | Analogous to OSMED, which "may necessitate joint replacements in early adulthood" ([PMID: 9188673](https://pubmed.ncbi.nlm.nih.gov/9188673/)) | NCIT joint arthroplasty |
| Craniofacial | Cleft-palate repair; supportive craniofacial care | [PMID: 9235398](https://pubmed.ncbi.nlm.nih.gov/9235398/) | NCIT surgical repair |
| Supportive | Speech/language therapy, low-vision services, genetic counseling | [PMID: 38062645](https://pubmed.ncbi.nlm.nih.gov/38062645/) | NCIT rehabilitation therapy |

**Experimental therapies / pharmacogenomics / personalized medicine.** None registered specifically for Marshall syndrome. (No data available.)

---

## 13. Prevention

- **Primary prevention:** Not applicable for a monogenic dominant disorder beyond **reproductive genetic counseling**. Options for at-risk families include **prenatal diagnosis** and **preimplantation genetic testing (PGT)** once the familial COL11A1 variant is known.
- **Secondary prevention:** **Ophthalmologic surveillance** for early detection of vitreoretinal degeneration, with **prophylactic retinal interventions** to reduce retinal-detachment/vision-loss risk (though best practice is not standardized; [PMID: 21466760](https://pubmed.ncbi.nlm.nih.gov/21466760/)); early **audiologic monitoring** for timely amplification.
- **Tertiary prevention:** Preventing complications — retinal-detachment repair, joint-preserving orthopedic care, and communication support to mitigate disability.
- **Genetic counseling:** Central to management. Autosomal-dominant recurrence risk is ~50% for an affected parent's offspring; the rare recessive form (consanguineous families) carries a 25% recurrence risk with a known biallelic variant ([PMID: 25073711](https://pubmed.ncbi.nlm.nih.gov/25073711/)).
- **Immunization / public health / prophylactic medication:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologous genes:** *Mus musculus* **Col11a1** (NCBI Taxon 10090) and *Danio rerio* **col11a1a** (NCBI Taxon 7955) are functional orthologs of human COL11A1. Collagen XI's role in cartilage is **evolutionarily conserved** across mammals and teleosts.
- **Natural disease (mouse):** The autosomal-recessive **chondrodysplasia (cho) mouse** carries a Col11a1 frameshift ("Deletion of a cytidine residue about 570 nt downstream of the translation initiation codon in cho alpha 1 (XI) mRNA causes a reading frame shift and introduces a premature stop codon"); homozygous cho/cho mice "die at birth with abnormalities in cartilage of limbs, ribs, mandible, and trachea" ([PMID: 7859283](https://pubmed.ncbi.nlm.nih.gov/7859283/)). This is a naturally arising Col11a1 loss-of-function model.
- **Comparative biology:** In zebrafish, "Col11a1a Regulates Meckel's Cartilage Morphogenesis and Mineralization," confirming a conserved role in craniofacial cartilage ([PMID: 36278545](https://pubmed.ncbi.nlm.nih.gov/36278545/)).
- **Zoonotic / cross-species transmission:** Not applicable (genetic disorder).
- **VBO / OMIA breed data:** No specific companion-animal breed disorder catalogued here. (No data available.)

---

## 15. Model Organisms

| Model | Type | Lesion | Phenotype recapitulation | Reference |
|-------|------|--------|--------------------------|-----------|
| **cho/cho mouse** | Mammalian, genetic (spontaneous) | Col11a1 frameshift → premature stop (null) | Lethal chondrodysplasia; disorganized cartilage collagen fibrils; short limb bones (~½ normal), widened metaphyses; cartilage of limbs, ribs, mandible, trachea affected. Models the **skeletal/cartilage** mechanism; recessive-null, so more severe than human dominant-negative disease | [PMID: 7859283](https://pubmed.ncbi.nlm.nih.gov/7859283/) |
| **Zebrafish col11a1a** | Vertebrate, genetic | col11a1a disruption | Meckel's (craniofacial) cartilage morphogenesis and mineralization defects; models the **craniofacial** branch | [PMID: 36278545](https://pubmed.ncbi.nlm.nih.gov/36278545/) |

**Model applications and limitations.** These models establish collagen XI's essential, conserved role in cartilage fibril assembly and craniofacial cartilage development — the upstream mechanism of Marshall syndrome. **Limitation:** both are effectively loss-of-function/null models, whereas human Marshall syndrome is a **dominant-negative** disorder; the mouse null is neonatally lethal and does not recapitulate the survivable, progressive ocular/auditory human phenotype. Humanized knock-in models carrying specific 54-bp-exon splice variants would better model the human disease and are not yet available. **Resources:** MGI (mouse), ZFIN (zebrafish).

---

## Mechanistic Model / Interpretation

Marshall syndrome is fundamentally a **disorder of extracellular-matrix architecture**. A single class of COL11A1 mutation — splice-site changes at the 54-bp C-terminal exons — produces a shortened but stable α1(XI) chain that acts as a molecular saboteur: by co-assembling into the collagen heterotrimer, it poisons the regulation of collagen II/XI fibril nucleation (**dominant-negative**). Because collagen XI templates fibril diameter in cartilage and related matrices, the downstream consequences cluster in the three tissues most dependent on precisely organized collagen fibrils — **growth-plate cartilage** (midface hypoplasia, skeletal dysplasia, early osteoarthritis), the **ocular vitreous/retina** (high myopia, vitreoretinal degeneration, retinal detachment), and the **membranous labyrinth** (progressive cochlear deafness). The genotype–phenotype logic is elegant: the specific 54-bp-exon splice class predicts the Marshall end of the spectrum (with its hallmark early, severe hearing loss), while other COL11A1 lesions blur into Stickler type 2. The animal models validate the upstream cartilage mechanism but, being nulls, sit at the more severe recessive end — underscoring that dosage and dominant-negative interference, not simple haploinsufficiency, shape the human disease.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [10486316](https://pubmed.ncbi.nlm.nih.gov/10486316/) | Splicing mutations of 54-bp exons cause Marshall syndrome | Defines the Marshall-specific mutation class (genotype–phenotype) |
| [23621912](https://pubmed.ncbi.nlm.nih.gov/23621912/) | COL11A1 deletions / MLPA | Establishes in-frame exon skipping → dominant-negative mechanism; MLPA needed diagnostically |
| [7859283](https://pubmed.ncbi.nlm.nih.gov/7859283/) | Col11a1 essential for skeletal morphogenesis (cho mouse) | Fibril-assembly mechanism; loss-of-function model |
| [10889003](https://pubmed.ncbi.nlm.nih.gov/10889003/) | Audiovestibular phenotype of COL11A1 Marshall | Cardinal phenotype; membranous-labyrinth auditory mechanism |
| [25073711](https://pubmed.ncbi.nlm.nih.gov/25073711/) | Marshall syndrome distinct entity; new findings | Cardinal triad; specific variants; recessive form |
| [17236192](https://pubmed.ncbi.nlm.nih.gov/17236192/) | 10 patients, COL11A1 genotype–phenotype | Intron-50 hot spot; Marshall vs Stickler classification |
| [9235398](https://pubmed.ncbi.nlm.nih.gov/9235398/) | Lens coloboma/dislocation in Stickler (Marshall) | Expanded ocular phenotype |
| [26367406](https://pubmed.ncbi.nlm.nih.gov/26367406/) | Tunisian family, clinical/radiological/genetic | Variable expressivity; radiological signs |
| [38062645](https://pubmed.ncbi.nlm.nih.gov/38062645/) | Growing up with Marshall syndrome | Prevalence <1/1,000,000; infancy onset; lifelong course |
| [21466760](https://pubmed.ncbi.nlm.nih.gov/21466760/) | Prophylactic retinal interventions in Stickler | Retinal-detachment prevention paradigm |
| [41856555](https://pubmed.ncbi.nlm.nih.gov/41856555/) | Type II/IX/XI collagenopathy testing | Diagnostic panel framing and yield |
| [36278545](https://pubmed.ncbi.nlm.nih.gov/36278545/) | Zebrafish col11a1a and Meckel's cartilage | Craniofacial model; conserved mechanism |
| [38299479](https://pubmed.ncbi.nlm.nih.gov/38299479/) | Microphthalmia/cataract in STL2 | Phenotype expansion; WES diagnosis |
| [41715899](https://pubmed.ncbi.nlm.nih.gov/41715899/) | Early ocular presentation, collagenopathy spectrum | Collagenopathy-spectrum phenotype summary |
| [9188673](https://pubmed.ncbi.nlm.nih.gov/9188673/) | OSMED (COL11A2) | Differential diagnosis; hypothesized COL11A1 basis of Marshall |
| [11556853](https://pubmed.ncbi.nlm.nih.gov/11556853/) | Auditory dysfunction in Stickler | Differential (hearing-loss severity across types) |
| [33570243](https://pubmed.ncbi.nlm.nih.gov/33570243/) | Recessive Stickler (COL9A3) | Differential diagnosis |
| [38354003](https://pubmed.ncbi.nlm.nih.gov/38354003/), [37751263](https://pubmed.ncbi.nlm.nih.gov/37751263/) | PFAPA "Marshall syndrome" | Eponym disambiguation |
| [34929762](https://pubmed.ncbi.nlm.nih.gov/34929762/), [35925217](https://pubmed.ncbi.nlm.nih.gov/35925217/), [38924070](https://pubmed.ncbi.nlm.nih.gov/38924070/) | Acquired cutis laxa "Marshall syndrome" | Eponym disambiguation |

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity → thin evidence base.** Nearly all clinical data come from single cases and small families (largest ~8 members). No large cohorts, registries, or natural-history studies exist; frequencies, penetrance, and QoL metrics are qualitative.
2. **Eponym ambiguity** repeatedly contaminates the literature; care must be taken to separate the genetic COL11A1 disorder from PFAPA and acquired cutis laxa.
3. **Marshall vs Stickler type 2 boundary** is not crisp — they are allelic and overlapping; the distinction rests largely on early severe hearing loss and facial features rather than a molecular dichotomy.
4. **No disease-specific omics** (transcriptomics/proteomics/metabolomics/single-cell) data. The molecular mechanism is inferred from mutation analysis and null-allele models, not from human diseased-tissue profiling.
5. **Model mismatch:** available animal models are loss-of-function (null), not dominant-negative; the human ocular/auditory phenotype is not modeled in a survivable animal.
6. **No standardized prophylactic guidelines** for the dominant, preventable ocular complication (retinal detachment).

## Proposed Follow-up Experiments / Actions

1. **Generate a humanized knock-in mouse** carrying a recurrent 54-bp-exon splice variant (e.g., IVS50+1G>A) to model the dominant-negative human disease and its progressive ocular/auditory course.
2. **Establish an international COL11A1 registry** to quantify penetrance, expressivity, genotype–phenotype correlations (54-bp splice vs missense vs deletion), and natural history of hearing/vision loss.
3. **Compile per-variant allele frequencies** from gnomAD/ClinVar and standardize ACMG classification of recurrent COL11A1 variants.
4. **Prospective trials of prophylactic retinal intervention** stratified by collagenopathy subtype to establish evidence-based guidelines and reduce childhood retinal detachment.
5. **Patient-derived iPSC chondrocyte/organoid models** to profile ECM assembly defects (proteomics of collagen fibrils) and screen candidate matrix-stabilizing therapeutics.
6. **Apply disease-specific QoL instruments** (SF-36/PROMIS + disease-specific sensory scales) to characterize the functional burden.

---

*Report compiled from 9 confirmed findings and 25 reviewed publications over a 5-iteration autonomous investigation. All mechanistic and clinical claims are anchored to the cited PMIDs; sections marked "No data available" reflect genuine gaps for this ultra-rare disorder.*


## Artifacts

- [OpenScientist final report](Marshall_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Marshall_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 22 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 18 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007949` (3 mentions) - the report calls it "MONDO"; MONDO calls it **Marshall syndrome**
- `HP:0011003` (1 mention) - the report calls it "Progressive"; HP calls it **High myopia**
- `HP:0000518` (1 mention) - the report calls it "Progressive"; HP calls it **Cataract**
- `HP:0000501` (1 mention) - the report calls it "Progressive"; HP calls it **Glaucoma**
- `HP:0000407` (1 mention) - the report calls it "Progressive"; HP calls it **Sensorineural hearing impairment**
- `HP:0000175` (1 mention) - the report calls it "Stable"; HP calls it **Cleft palate**
- `UBERON:0001796` (1 mention) - the report calls it "anterior chamber region, approximate"; UBERON calls it **aqueous humor of eyeball**
- `UBERON:0001800` (1 mention) - the report calls it "vitreous humor, approximate"; UBERON calls it **sensory ganglion**
- `UBERON:0001709` (1 mention) - the report calls it "mid-face region, approximate"; UBERON calls it **upper jaw region**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005581` (3 mentions) - the report calls it "collagen trimer", "extracellular matrix/collagen trimer"; GO calls it **collagen trimer**
- `UBERON:0001846` (1 mention) - the report calls it "inner ear"; UBERON calls it **internal ear**, and lists "inner ear" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005581` - called "collagen trimer", "extracellular matrix/collagen trimer"