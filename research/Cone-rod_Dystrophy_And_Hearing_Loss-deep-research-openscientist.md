---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-11T11:46:52.965271'
end_time: '2026-09-11T12:16:29.827473'
duration_seconds: 1776.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cone-Rod Dystrophy and Hearing Loss
  mondo_id: MONDO:0014980
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
citation_count: 14
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 26
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 11
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0000548
    reported_labels:
    - Clinical sign
    - Cone-rod dystrophy
    ontology_label: Cone/cone-rod dystrophy
  - term_id: HP:0000407
    reported_labels:
    - Clinical sign / lab (audiometry)
    - Sensorineural hearing impairment
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0000618
    reported_labels:
    - Clinical sign
    ontology_label: Blindness
  labels_variant: 2
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Cone-rod_Dystrophy_And_Hearing_Loss-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cone-rod_Dystrophy_And_Hearing_Loss-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cone-Rod Dystrophy and Hearing Loss
- **MONDO ID:** MONDO:0014980 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Cone-Rod Dystrophy and Hearing Loss** covering all of the
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

# Cone-Rod Dystrophy and Hearing Loss (CRDHL): A Comprehensive Disease Profile

**Disease:** Cone-Rod Dystrophy and Hearing Loss (CRDHL)
**MONDO ID:** MONDO:0014980 · **OMIM:** #617236 · **Category:** Genetic (autosomal recessive ciliopathy)
**Primary gene:** *CEP78* (HGNC:26820) · **Second locus:** *CEP250* (C-Nap1)

*Evidence base: human clinical case series/cohorts, cell-biology (in vitro), and one knockout-mouse model. This is an ultra-rare disorder; several sections rely on a small number of primary reports plus analogy to related deaf-blindness syndromes, which is flagged where used.*

---

## Summary

Cone-Rod Dystrophy and Hearing Loss (CRDHL) is a rare, autosomal recessive **ciliopathy** whose principal molecular cause is **biallelic loss-of-function of *CEP78***, a centriolar distal-end protein that governs centriole length and centrosome homeostasis. First delineated as a distinct Mendelian entity by Namburi et al. in 2016, CRDHL couples a **childhood/adolescent-onset, cone-predominant cone-rod dystrophy** (leading to legal blindness by mid-adulthood) with **bilateral, post-lingual, progressive sensorineural hearing loss (SNHL)**, and — in a subset of male patients — **reduced fertility due to oligoasthenoteratozoospermia**. This triad is mechanistically unified by a defect in the specialized cilia and centriole-derived structures of the body's most centriole-dependent post-mitotic cells: photoreceptor connecting cilia, cochlear hair-cell kinocilia/basal bodies, and sperm flagella.

CRDHL is genetically and clinically distinguishable from **Usher syndrome** (the most common cause of combined deaf-blindness), which is typically rod-first with congenital hearing loss. A second locus, ***CEP250*/C-Nap1**, produces an overlapping but milder CRD+SNHL phenotype and is otherwise classically associated with "atypical Usher syndrome." CRDHL therefore sits within a genetically heterogeneous group of retinal-dystrophy-plus-hearing-loss syndromes whose differential diagnosis includes *ARSG* (Usher type IV), *ABHD12* (PHARC), *TUBB4B*-related syndromic Leber congenital amaurosis, and *CEP250*.

There is **no disease-specific therapy**. Management is supportive and rehabilitative: low-vision aids, hearing aids, and — for severe-to-profound SNHL — **cochlear implantation**, which restores speech perception effectively in analogous post-lingual deaf-blindness syndromes. Diagnosis integrates multimodal ophthalmic phenotyping (full-field ERG showing cone-worse-than-rod loss, OCT, fundus autofluorescence), pure-tone audiometry, and molecular confirmation by retinal-dystrophy gene panels or whole-exome/whole-genome sequencing. This report synthesizes 12 confirmed findings drawn from 35 reviewed papers across human clinical, model organism, and in vitro evidence.

---

## Key Findings

### 1. CEP78 biallelic loss-of-function causes CRDHL, distinct from Usher syndrome (F001)

The founding evidence for CRDHL as a *CEP78*-related disorder comes from **Namburi et al. 2016 (American Journal of Human Genetics)**. Using homozygosity mapping followed by whole-exome sequencing and founder-mutation screening, they identified **two truncating variants in *CEP78*** — c.893-1G>A (a splice-acceptor variant) and c.534delT — in **six individuals of Jewish ancestry** with autosomal recessive cone-rod degeneration and SNHL. The c.893-1G>A variant causes skipping of exon 7 (a 65-bp deletion), producing a frameshift **p.Asp298Valfs*17**. Crucially, immunohistochemistry of human retina showed **intense CEP78 labeling of cone inner segments relative to rods**, providing an anatomical basis for the cone-predominant degeneration.

> *"Homozygosity mapping followed by whole-exome sequencing (WES) and founder mutation screening revealed two truncating rare variants (c.893-1G>A and c.534delT) in CEP78, which encodes centrosomal protein 78, in six individuals of Jewish ancestry with CRD and SNHL."* — [PMID: 27588452](https://pubmed.ncbi.nlm.nih.gov/27588452/)

This finding establishes *CEP78* truncating variants as the cause of a **new, non-Usher deaf-blindness syndrome**, distinguished by its **cone-first** (rather than rod-first) retinal degeneration and **post-lingual** (rather than congenital) hearing loss.

### 2. CEP78 is a centriolar distal-end protein controlling centriole length and centrosome homeostasis (F002)

The molecular function of CEP78 places CRDHL firmly among the **ciliopathies**. **Hossain et al. 2017 (Journal of Cell Biology)** showed that CEP78 localizes to **mature centrioles**, directly interacts with **VprBP (viral protein R binding protein)**, and **inhibits the EDD-DYRK2-DDB1 E3 ubiquitin ligase** to regulate centrosome homeostasis.

> *"Here, we show that centrosomal protein of 78 kDa (Cep78) localizes to mature centrioles and directly interacts with viral protein R binding protein (VprBP)."* — [PMID: 28242748](https://pubmed.ncbi.nlm.nih.gov/28242748/)

**Karasu et al. 2022** further demonstrated that the **CEP350-FOP scaffold recruits CEP78 (or OFD1) to the distal end of centrioles**, and that the CEP350-FOP/CEP78 complex **controls centriole microtubule length**:

> *"recruiting the proteins CEP78 and OFD1 to the distal end of centrioles and promoting the assembly of subdistal appendages"* — [PMID: 36315013](https://pubmed.ncbi.nlm.nih.gov/36315013/)

Consistent with this, **Ascari et al. 2020** found that **patient-derived fibroblasts and nasal brushings show elongated primary cilia**, indicating impaired cilia assembly downstream of CEP78 loss:

> *"Elongated primary cilia without clear ultrastructural abnormalities in sperm or nasal brushes suggest impaired cilia assembly."* — [PMID: 31999394](https://pubmed.ncbi.nlm.nih.gov/31999394/)

### 3. The phenotype spectrum includes male infertility; a missense founder allele expands variant type (F003)

**Ascari et al. 2020** identified and functionally characterized the **first *CEP78* missense variant, c.449T>C p.(Leu150Ser)**, across three CRDHL families (biallelic in two Belgian families; compound heterozygous with c.1462-1G>T in a German family). Haplotype analysis demonstrated a **founder effect**, and homology modeling plus patient fibroblasts confirmed **reduced protein stability**. Two affected males had sperm abnormalities causing infertility, expanding the phenotype.

> *"we identified and functionally characterized the first CEP78 missense variant c.449T>C, p.(Leu150Ser) in three CRDHL families"* — [PMID: 31999394](https://pubmed.ncbi.nlm.nih.gov/31999394/)
>
> *"the CEP78 phenotype has been possibly expanded with male infertility"* — [PMID: 31999394](https://pubmed.ncbi.nlm.nih.gov/31999394/)

This finding shows that CRDHL is not confined to null alleles — **destabilizing missense variants** also cause disease — and that the syndrome extends beyond the eye and ear to the **male reproductive tract**.

### 4. CEP250 (C-Nap1) is a second CRDHL/atypical-Usher locus (F004)

**Kubota et al. 2018** reported compound heterozygous null variants **c.361C>T p.R121\*** and **c.562C>T p.R188\*** in ***CEP250***, co-segregating with **mild cone-rod dystrophy and slight SNHL** in a Japanese family (both variants PVS1, pathogenic by ACMG). C-Nap1/CEP250 is expressed in photoreceptor cilia and interacts with other ciliary proteins, including CEP78.

> *"Our data indicate that mutations of CEP250 can cause mild CRD and SNHL in Japanese patients."* — [PMID: 29718797](https://pubmed.ncbi.nlm.nih.gov/29718797/)
>
> *"Mutations of CEP250 cause atypical Usher syndrome which is characterized by early-onset sensorineural hearing loss (SNHL) and a relatively mild retinitis pigmentosa."* — [PMID: 29718797](https://pubmed.ncbi.nlm.nih.gov/29718797/)

*CEP250* thus represents **locus heterogeneity** within the CRDHL phenotype and reinforces the **centriolar-cilium** theme, since CEP250 and CEP78 are physically and functionally interconnected at the centrosome.

### 5. No disease-specific therapy exists; cochlear implantation restores speech perception (F005)

There is **no approved gene or pharmacologic therapy** for *CEP78*- or *CEP250*-related CRDHL. Management is symptomatic and rehabilitative — low-vision aids, hearing aids, **cochlear implantation**, and genetic counseling. The strongest quantitative evidence for the SNHL component comes from the analogous post-lingual syndrome **Usher type IIa**: **Hartel et al. 2017** implanted 8 USH2a adults (mean age 59 at implantation) and found **phoneme scores improved from 41% to 87% (p = 0.02)**, with clear quality-of-life benefit.

> *"The phoneme scores improved significantly from 41 to 87% in patients with USH2a (p = 0.02)"* — [PMID: 28498263](https://pubmed.ncbi.nlm.nih.gov/28498263/)
>
> *"CI increases speech intelligibility and improves quality of life in patients with USH2a."* — [PMID: 28498263](https://pubmed.ncbi.nlm.nih.gov/28498263/)

Because CRDHL hearing loss is likewise **bilateral, post-lingual, and progressive**, cochlear implantation is expected to provide comparable benefit — particularly important given the concurrent progressive visual loss that increases reliance on hearing.

### 6. CRDHL is one of several retinal-dystrophy-plus-hearing-loss syndromes requiring differential diagnosis (F006)

CRDHL must be distinguished from other dual sensory-loss disorders:

| Gene | Syndrome | Distinguishing features | Key reference |
|------|----------|-------------------------|---------------|
| **CEP78** | CRDHL | Cone-first CRD; post-lingual progressive SNHL; ± male infertility | [PMID: 27588452](https://pubmed.ncbi.nlm.nih.gov/27588452/) |
| **CEP250** | Atypical Usher / mild CRD+SNHL | Early-onset SNHL, relatively mild RP | [PMID: 29718797](https://pubmed.ncbi.nlm.nih.gov/29718797/) |
| **ARSG** | Usher type IV | Late-onset RP (pericentral/macular); late progressive SNHL; **no vestibular involvement**; loss of sulfatase activity | [PMID: 39199020](https://pubmed.ncbi.nlm.nih.gov/39199020/) |
| **ABHD12** | PHARC | **Polyneuropathy, ataxia, cataract** in addition to hearing loss + RP | [PMID: 40064796](https://pubmed.ncbi.nlm.nih.gov/40064796/) |
| **TUBB4B** | Syndromic LCA + hearing loss | Early-onset; microtubule (not ciliary) dysfunction | [PMID: 29198720](https://pubmed.ncbi.nlm.nih.gov/29198720/) |

> *"This subtype was assigned as 'USH IV' with a late onset of RP and usually late-onset progressive SNHL without vestibular involvement."* — [PMID: 39199020](https://pubmed.ncbi.nlm.nih.gov/39199020/)
>
> *"PHARC syndrome is an autosomal recessive neurodegenerative disease caused by mutations in the ABHD12 gene and is characterized by five main clinical features: polyneuropathy, hearing loss, ataxia, retinitis pigmentosa, and cataracts."* — [PMID: 40064796](https://pubmed.ncbi.nlm.nih.gov/40064796/)
>
> *"we identified two heterozygous mutations affecting Arg391 in β-tubulin 4B isotype-encoding (TUBB4B)"* — [PMID: 29198720](https://pubmed.ncbi.nlm.nih.gov/29198720/)

### 7. Retinal component: childhood-onset, cone-first, progressive dystrophy → legal blindness by mid-adulthood; hearing loss variably expressed (F007)

The retinal disease of CRDHL follows the natural history of cone-rod dystrophy defined in the **19-year multicenter cohort of Thiadens et al. 2012**: CRD had a **mean age of onset of 12 years (SD 11)**, was AR in 90%, and reached **legal blindness at a mean age of 35 years (SE 1.1)** — significantly earlier than cone-only dystrophy (48 years, P<0.001). Ten years after diagnosis, 51% had bull's-eye maculopathy and 70% had absolute peripheral field defects.

> *"The mean age of legal blindness was 48 (standard error [SE], 3.1) years in CD, and 35 (SE, 1.1; P<0.001) years in CRD."* — [PMID: 22264887](https://pubmed.ncbi.nlm.nih.gov/22264887/)
>
> *"The mean age onset for CD was 16 years (standard deviation, 11), and of CRD 12 years (standard deviation, 11; P = 0.02)."* — [PMID: 22264887](https://pubmed.ncbi.nlm.nih.gov/22264887/)

The hearing-loss component shows **variable expressivity and onset**. **Zhai & Ballios 2024** documented teenage *CEP78* siblings with cone-rod dystrophy and "presumed normal hearing" alongside another patient with "cone-rod dystrophy and early-onset hearing loss":

> *"Both teenagers have a clinical diagnosis of cone-rod dystrophy with presumed normal hearing."* — [PMID: 38780195](https://pubmed.ncbi.nlm.nih.gov/38780195/)

### 8. Diagnosis relies on multimodal ophthalmic + audiologic phenotyping plus panel/exome sequencing (F008)

Diagnosis integrates:
- **Full-field electroretinography** — cone-rod pattern (photopic responses reduced earlier/more than scotopic)
- **Multimodal retinal imaging** — OCT (outer-retinal/ellipsoid-zone and photoreceptor loss), fundus autofluorescence, adaptive optics (reduced cone density)
- **Pure-tone audiometry** — bilateral SNHL
- **Molecular confirmation** — retinal-dystrophy gene panels or whole-exome/whole-genome sequencing

**de Castro-Miró et al. 2016** identified *CEP78* and *CEP250* as new inherited-retinal-dystrophy (IRD) genes via WES:

> *"WES unveiled four new candidates for non-syndromic IRD: SEMA6B, CEP78, CEP250, SCLT1, the two latter previously associated to syndromic disorders."* — [PMID: 28005958](https://pubmed.ncbi.nlm.nih.gov/28005958/)
>
> *"We provide functional data supporting that missense mutations in CEP250 alter cilia formation."* — [PMID: 28005958](https://pubmed.ncbi.nlm.nih.gov/28005958/)

**Zhai & Ballios 2024** showed that retinal-dystrophy panels detect variants (including a splice variant c.1206-2A>C, and a nonsense c.1447C>T p.Arg483\*) that earlier WES had missed:

> *"A retinal dystrophy panel detected a novel homozygous CEP78 pathogenic variant (c.1447C>T, p.Arg483\*)"* — [PMID: 38780195](https://pubmed.ncbi.nlm.nih.gov/38780195/)

### 9. An ultra-rare AR disorder with population-specific CEP78 founder alleles and a role for consanguinity (F009)

CRDHL is **autosomal recessive and ultra-rare** — only several dozen molecularly confirmed cases have been reported worldwide across *CEP78* and *CEP250*. **Founder effects** are documented: the *CEP78* truncating variants c.893-1G>A and c.534delT recurred in Jewish-ancestry individuals identified through homozygosity mapping (consistent with consanguinity/shared haplotypes), and the missense c.449T>C p.(Leu150Ser) allele is a founder allele across Belgian and German families.

> *"Homozygosity mapping followed by whole-exome sequencing (WES) and founder mutation screening revealed two truncating rare variants (c.893-1G>A and c.534delT) in CEP78"* — [PMID: 27588452](https://pubmed.ncbi.nlm.nih.gov/27588452/)
>
> *"Haplotype reconstruction showed a founder effect."* — [PMID: 31999394](https://pubmed.ncbi.nlm.nih.gov/31999394/)

Both sexes are affected for the retinal/auditory phenotype; **reduced fertility affects males specifically**. *CEP250* variants were reported in a non-consanguineous Japanese family.

### 10. Anatomical targets: cone-predominant photoreceptors, cochlear hair cells, and sperm flagella — a shared centriole/cilium defect (F010)

The primary organs affected are the **eye (retina)** and **inner ear (cochlea)**, plus the **male reproductive tract (testis/sperm)**. CEP78 is enriched in **cone inner segments** relative to rods, explaining the cone-predominant degeneration; CEP250/C-Nap1 localizes to **photoreceptor cilia**. The unifying subcellular lesion is at the **centriole/basal body and ciliary axoneme** — the photoreceptor connecting cilium, cochlear hair-cell kinocilium/basal body, and sperm flagellar axoneme all depend on centriolar/ciliary integrity.

> *"Immunohistochemistry studies in the human retina showed intense labeling of cone inner segments compared to rods."* — [PMID: 27588452](https://pubmed.ncbi.nlm.nih.gov/27588452/)
>
> *"C-Nap1 has been reported to be expressed in the photoreceptor cilia"* — [PMID: 29718797](https://pubmed.ncbi.nlm.nih.gov/29718797/)

### 11. Model systems: Cep78-knockout mouse and patient-derived ciliated cells (F011)

- **Mammalian model:** The **Cep78-knockout mouse** (*Mus musculus*; NCBI Taxon:10090) recapitulates the male-infertility component. **Liu et al. 2025**: *"Cep78 knockout causes sterility and oligoasthenoteratozoospermia in male mice."* — [PMID: 39747485](https://pubmed.ncbi.nlm.nih.gov/39747485/)
- **Patient-derived in vitro models:** Dermal fibroblasts and nasal-epithelial brushings from patients show **elongated primary cilia** and reduced CEP78 protein stability ([PMID: 31999394](https://pubmed.ncbi.nlm.nih.gov/31999394/)).
- **Cell-biology models:** HeLa/RPE cultured cells established CEP78's centriolar localization, VprBP interaction, and EDD-DYRK2-DDB1 inhibition ([PMID: 28242748](https://pubmed.ncbi.nlm.nih.gov/28242748/)), and CEP350-FOP-dependent recruitment controlling centriole length ([PMID: 36315013](https://pubmed.ncbi.nlm.nih.gov/36315013/)).
- **Differential-diagnosis models:** *ARSG* has naturally occurring canine and murine neuronal ceroid lipofuscinosis models: *"we identified a homozygous missense variant, p.(Arg99His), previously described in dogs with neuronal ceroid lipofuscinosis"* — [PMID: 39199020](https://pubmed.ncbi.nlm.nih.gov/39199020/).

### 12. Consolidated pathophysiology causal chain (F012)

See the **Mechanistic Model** section below for the integrated causal chain.

---

## Detailed Section-by-Section Report

### Section 1 — Disease Information
CRDHL is a rare autosomal recessive syndrome combining a progressive cone-rod retinal dystrophy with sensorineural hearing loss, and (in males) reduced fertility. **Key identifiers:** MONDO:0014980; OMIM #617236 ("Cone-rod dystrophy and hearing loss 1," CRDHL1, CEP78); OMIM #618358 ("Cone-rod dystrophy and hearing loss 2," CRDHL2, CEP250); it lacks a dedicated ICD-10 code (coded under H35.5 hereditary retinal dystrophy plus H90.x sensorineural hearing loss). **Synonyms:** cone-rod dystrophy with sensorineural hearing loss; CRD-HL; CRDHL; CEP78-related deaf-blindness. Information is derived from **aggregated disease-level resources** (OMIM, published case series/cohorts) rather than EHR.

### Section 2 — Etiology
**Causal factors are purely genetic** (monogenic, autosomal recessive): biallelic *CEP78* loss-of-function/destabilizing variants (primary) or biallelic *CEP250* null variants (second locus). **Genetic risk factors:** the disease requires two pathogenic alleles; documented founder alleles increase risk in specific ancestries. **Environmental risk/protective factors and gene-environment interactions: not applicable** — no environmental, infectious, lifestyle, or protective-allele factors have been reported for this Mendelian disorder.

### Section 3 — Phenotypes
| Phenotype | Type | HPO term | Onset | Progression | Frequency |
|-----------|------|----------|-------|-------------|-----------|
| Cone-rod dystrophy / reduced visual acuity | Clinical sign | HP:0000548 | Childhood/adolescence (mean ~12 y) | Progressive | Obligate (~100%) |
| Photophobia / impaired color vision | Symptom | HP:0000613 / HP:0000551 | Childhood | Progressive | Common (cone-first) |
| Sensorineural hearing loss (bilateral) | Clinical sign / lab (audiometry) | HP:0000407 | Post-lingual, variable | Progressive | Common, variably expressed |
| Legal blindness | Clinical sign | HP:0000618 | ~Mid-adulthood (mean ~35 y) | End-stage | Frequent |
| Male infertility / oligoasthenoteratozoospermia | Lab abnormality | HP:0003251 / HP:0000798 | Adult | Stable | Subset of males |

**Quality-of-life impact:** dual sensory loss severely affects communication, mobility, education, and employment; cochlear implantation and low-vision rehabilitation substantially mitigate the hearing component.

### Section 4 — Genetic/Molecular Information
**Causal genes:** *CEP78* (HGNC:26820; OMIM *617110), *CEP250* (OMIM *611485). **Variant types:** truncating (splice c.893-1G>A → p.Asp298Valfs*17; frameshift c.534delT; nonsense c.1447C>T p.Arg483*), missense (c.449T>C p.Leu150Ser — destabilizing founder allele), and splice (c.1462-1G>T, c.1206-2A>C). **Classification:** pathogenic/likely pathogenic per ACMG (PVS1 for null alleles). **Origin:** germline. **Functional consequence:** loss of function (reduced/absent protein or protein stability). **Allele frequencies:** rare in gnomAD (consistent with ultra-rare recessive disease). **Modifier/epigenetic/chromosomal factors:** none established.

### Section 5 — Environmental Information
**Not applicable.** No environmental toxins, radiation, lifestyle factors, or infectious agents contribute to this monogenic disorder.

### Section 6 — Mechanism / Pathophysiology
Presented as an ordered causal chain in the **Mechanistic Model** section below.

### Section 7 — Anatomical Structures Affected
**Organ level:** eye/retina (UBERON:0000966), inner ear/cochlea (UBERON:0001844), testis (UBERON:0000473). **Body systems:** visual, auditory, reproductive. **Cell level:** retinal cone cells (CL:0000573, primary), retinal rod cells (CL:0000604), cochlear/inner-ear hair cells (CL:0000855), spermatozoa/male germ cells (CL:0000019). **Subcellular:** centriole (GO:0005814), ciliary basal body (GO:0036064), photoreceptor connecting cilium (GO:0032391), sperm flagellum. **Lateralization:** bilateral (both retina and cochlea).

### Section 8 — Temporal Development
**Onset:** retinal disease childhood/adolescence (insidious, chronic); hearing loss post-lingual with variable, often adult, onset. **Progression:** slowly progressive; legal blindness ~mid-adulthood; SNHL progressive. **Course:** chronic, lifelong, progressive; no remission. **Critical period:** early diagnosis enables timely cochlear implantation and low-vision planning before severe dual sensory loss.

### Section 9 — Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** high for the sensory phenotype (variable expressivity of the hearing and fertility components). **Epidemiology:** ultra-rare; prevalence/incidence not formally established (only several dozen confirmed cases worldwide). **Founder effects:** Jewish-ancestry CEP78 truncating alleles; Belgian/German p.Leu150Ser missense allele. **Consanguinity** contributes (homozygosity mapping). **Sex ratio:** retinal/auditory phenotype affects both sexes equally; fertility reduction affects males only.

### Section 10 — Diagnostics
Full-field ERG (cone-rod pattern), OCT, fundus autofluorescence, adaptive optics, pure-tone audiometry, and molecular testing (retinal-dystrophy gene panels, WES, WGS). WES/WGS or panels are needed to detect deep-intronic/splice variants of these ciliary genes. **Differential diagnosis:** Usher syndrome (rod-first, congenital HL), Usher IV/ARSG, PHARC/ABHD12, TUBB4B-LCA, Alström syndrome, Heimler syndrome. **Screening:** carrier/cascade testing in founder populations; no newborn screening exists.

### Section 11 — Outcome/Prognosis
**Survival/mortality:** normal life expectancy — CRDHL is not life-limiting. **Morbidity:** major — progressive dual sensory disability. **Prognosis:** legal blindness by ~mid-adulthood (cone-rod natural history); progressive SNHL. **Recovery:** no spontaneous recovery of vision or hearing; cochlear implantation rehabilitates the auditory component. **Prognostic factors:** allele type (null vs hypomorphic) may influence severity, though genotype-phenotype correlations remain to be established.

### Section 12 — Treatment
**Pharmacotherapy/advanced therapeutics:** none disease-specific (no approved gene/RNA/cell therapy). **Supportive/rehabilitative:** low-vision aids, hearing aids, **cochlear implantation** (NCIT — cochlear implant procedure), genetic counseling. **Experimental:** gene-augmentation and splice-correction approaches are conceptually attractive but not yet in trials for CEP78. **Treatment strategy:** multidisciplinary (ophthalmology, audiology/otology, medical genetics, reproductive medicine).

### Section 13 — Prevention
**Primary prevention:** genetic/carrier screening and counseling in at-risk families and founder populations; prenatal/preimplantation genetic testing where desired. **Secondary prevention:** early molecular diagnosis to enable timely cochlear implantation and low-vision support. **Tertiary prevention:** rehabilitation to preserve function. No vaccine, behavioral, or environmental interventions apply.

### Section 14 — Other Species / Natural Disease
**Model species:** *Mus musculus* (NCBI Taxon:10090) — Cep78-knockout. Orthologs exist across vertebrates (*Cep78*). No naturally occurring companion-animal CEP78-CRDHL is documented; however, the differential-diagnosis gene *ARSG* has naturally occurring **canine** and murine neuronal ceroid lipofuscinosis models. No zoonotic potential (genetic disease).

### Section 15 — Model Organisms
**Mammalian:** Cep78-knockout mouse (recapitulates male infertility/OAT; retinal/auditory phenotyping limited). **Cellular/in vitro:** patient dermal fibroblasts and nasal-epithelial brushings (elongated primary cilia, reduced protein stability); HeLa/RPE cultured cells (centriolar localization, VprBP interaction, CEP350-FOP recruitment). **Limitations:** no validated model of the retinal or cochlear sensory phenotype; retinal organoids and iPSC-derived otic organoids are logical future resources.

---

## Mechanistic Model / Interpretation

CRDHL is best understood as a **centriole/cilium homeostasis disorder** in which loss of CEP78 selectively injures the body's most centriole- and cilium-dependent post-mitotic cells. The following ordered causal chain integrates the confirmed findings; each step is annotated as **demonstrated** or **inferred**.

```
STEP 1 (demonstrated)
  Biallelic CEP78 loss-of-function / destabilizing variants
  (nonsense, frameshift, splice, or missense — e.g. p.Asp298Valfs*17, p.Leu150Ser)
        │  reduce or abolish functional CEP78 protein
        ▼
STEP 2 (demonstrated in vitro)
  Loss of CEP78 at the distal centriole disrupts:
    • the CEP350–FOP–CEP78 centriole-length-control module
    • the EDD–DYRK2–DDB1 ubiquitin-ligase axis (via VprBP)
        │  perturbs centrosome homeostasis
        ▼
STEP 3 (demonstrated in patient cells; extrapolated to specialized cilia = inferred)
  Abnormal centriole/basal-body and ciliary axoneme assembly
  (elongated primary cilia in patient fibroblasts & nasal brushings)
        │
        ├───────────────► STEP 4a (inferred) — RETINA
        │     Defective connecting-cilium transport in cone/rod
        │     photoreceptors → progressive photoreceptor dysfunction
        │     and death, CONE-PREDOMINANT (CEP78 enriched in cone
        │     inner segments)  →  CONE-ROD DYSTROPHY
        │
        ├───────────────► STEP 4b (inferred) — COCHLEA
        │     Kinocilium/basal-body dysfunction in cochlear hair cells
        │     →  BILATERAL PROGRESSIVE SENSORINEURAL HEARING LOSS
        │
        └───────────────► STEP 4c (demonstrated in mouse; human sperm abnormalities)
              Flagellar axoneme/centriole defects in spermatids
              →  OLIGOASTHENOTERATOZOOSPERMIA / MALE SUBFERTILITY

ENDPOINT: Cone-rod dystrophy + progressive bilateral SNHL ± reduced male fertility
```

**Upstream vs downstream.** Steps 1–2 (protein loss → centrosome dysregulation) are upstream and shared across all tissues. Steps 4a–4c are downstream, tissue-specific manifestations of the same lesion. The **cone-predominance** of the retinal phenotype is explained by the higher expression of CEP78 in cone inner segments than in rods — a rare instance where the molecular expression pattern directly predicts the clinical phenotype.

**Supporting quotes:**
> *"deregulation of centrosome homeostasis is a hallmark feature of many human diseases"* — [PMID: 28242748](https://pubmed.ncbi.nlm.nih.gov/28242748/)
>
> *"The CEP350-FOP complex in association with CEP78 or OFD1 controls centriole microtubule length."* — [PMID: 36315013](https://pubmed.ncbi.nlm.nih.gov/36315013/)

**Ontology term suggestions:**

| Category | Term | ID |
|----------|------|-----|
| Disease | Cone-rod dystrophy and hearing loss | MONDO:0014980 |
| Phenotype | Cone-rod dystrophy | HP:0000548 |
| Phenotype | Sensorineural hearing impairment | HP:0000407 |
| Phenotype | Abnormal spermatogenesis / male infertility | HP:0008669 / HP:0003251 |
| Phenotype | Reduced visual acuity / blindness | HP:0007663 / HP:0000618 |
| Biological process (GO) | Centriole elongation | GO:0061511 |
| Biological process (GO) | Cilium assembly | GO:0060271 |
| Biological process (GO) | Centrosome cycle / duplication | GO:0007098 / GO:0051298 |
| Cellular component (GO) | Centriole | GO:0005814 |
| Cellular component (GO) | Ciliary basal body | GO:0036064 |
| Cellular component (GO) | Photoreceptor connecting cilium | GO:0032391 |
| Cell type (CL) | Retinal cone cell | CL:0000573 |
| Cell type (CL) | Retinal rod cell | CL:0000604 |
| Cell type (CL) | Cochlear/inner ear hair cell | CL:0000855 |
| Cell type (CL) | Sperm / male germ cell | CL:0000019 |
| Anatomy (UBERON) | Retina | UBERON:0000966 |
| Anatomy (UBERON) | Cochlea | UBERON:0001844 |
| Anatomy (UBERON) | Testis | UBERON:0000473 |
| Treatment (NCIT) | Cochlear implantation | NCIT (cochlear implant procedure) |

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|------|-----------------|---------------|----------|
| [27588452](https://pubmed.ncbi.nlm.nih.gov/27588452/) | *Bi-allelic Truncating Mutations in CEP78 Cause CRD with SNHL* | Human clinical + IHC | F001, F009, F010, F012 — founding gene discovery; cone-inner-segment expression |
| [28242748](https://pubmed.ncbi.nlm.nih.gov/28242748/) | *Cep78 controls centrosome homeostasis by inhibiting EDD-DYRK2-DDB1* | In vitro cell biology | F002, F012 — CEP78 molecular function |
| [36315013](https://pubmed.ncbi.nlm.nih.gov/36315013/) | *CEP350 coordinates centriole length, stability, maturation* | In vitro cell biology | F002, F012 — CEP350-FOP-CEP78 length control |
| [31999394](https://pubmed.ncbi.nlm.nih.gov/31999394/) | *First missense variant in CEP78 (founder allele)* | Human clinical + functional | F002, F003, F009, F011 — missense allele, founder effect, male infertility, elongated cilia |
| [29718797](https://pubmed.ncbi.nlm.nih.gov/29718797/) | *CEP250 mutations, mild CRD and SNHL (Japanese family)* | Human clinical | F004, F010 — second locus, photoreceptor cilium |
| [28498263](https://pubmed.ncbi.nlm.nih.gov/28498263/) | *Cochlear implantation in USH2a* | Human clinical | F005 — CI benefit for post-lingual SNHL |
| [39199020](https://pubmed.ncbi.nlm.nih.gov/39199020/) | *Usher type IV (ARSG) genetic landscape* | Human clinical | F006, F011 — differential dx; canine model |
| [40064796](https://pubmed.ncbi.nlm.nih.gov/40064796/) | *PHARC neurological spectrum systematic review* | Human clinical | F006 — ABHD12/PHARC differential |
| [29198720](https://pubmed.ncbi.nlm.nih.gov/29198720/) | *TUBB4B causes distinctive sensorineural disease* | Human clinical | F006 — TUBB4B differential |
| [22264887](https://pubmed.ncbi.nlm.nih.gov/22264887/) | *Clinical course of cone and cone-rod dystrophy* | Human clinical cohort | F007 — CRD natural history / prognosis |
| [38780195](https://pubmed.ncbi.nlm.nih.gov/38780195/) | *CEP78-associated syndrome variant spectrum* | Human clinical | F007, F008 — variable expressivity, panel diagnostics |
| [28005958](https://pubmed.ncbi.nlm.nih.gov/28005958/) | *Novel IRD candidate genes by exome sequencing* | Human genomics | F008 — WES discovery of CEP78/CEP250 |
| [39747485](https://pubmed.ncbi.nlm.nih.gov/39747485/) | *Cep78 knockout causes sterility and OAT in male mice* | Mouse model | F003, F011, F012 — infertility recapitulation |

**Note on citation integrity:** Two citation snippets attributed to [PMID: 39747485](https://pubmed.ncbi.nlm.nih.gov/39747485/) were flagged as `mismatch` during verification (the exact wording could not be confirmed against the stored abstract). The mouse-model conclusion is corroborated by the paper's title, *"Cep78 knockout causes sterility and oligoasthenoteratozoospermia in male mice,"* and an associated author correction ([PMID: 40075211](https://pubmed.ncbi.nlm.nih.gov/40075211/)); readers should treat the specific quoted phrasing with caution.

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** CRDHL is ultra-rare (several dozen molecularly confirmed cases). Prevalence and incidence figures are not established; no formal epidemiological registry exists. Penetrance and expressivity estimates are qualitative.
2. **Inferred tissue mechanisms.** The retinal (Step 4a) and cochlear (Step 4b) mechanistic steps are **inferred** by extrapolation from the demonstrated ciliary/centriolar defect in accessible cells (fibroblasts, nasal brushings) and from expression data. Direct demonstration of connecting-cilium or hair-cell kinocilium dysfunction in CEP78-deficient photoreceptors or cochlear cells has not been reported.
3. **Hearing-loss natural history is under-characterized.** Onset, audiometric progression rate, and severity of SNHL in CEP78-CRDHL are variably reported; some patients have "presumed normal hearing" in adolescence, implying delayed onset that may not yet be captured.
4. **Cochlear-implant evidence is indirect.** CI benefit is extrapolated from Usher type IIa and syndromic-deafness cohorts, not from CEP78-CRDHL patients specifically.
5. **No CEP78 retinal/cochlear animal model.** The existing Cep78-knockout mouse recapitulates male infertility but published retinal or auditory phenotyping of this model is limited; a validated model of the sensory phenotype is a gap.
6. **Modifier genes, epigenetics, and gene-environment interactions** are essentially unstudied for this disorder. No protective alleles, environmental risk factors, or infectious triggers apply (this is a monogenic Mendelian disorder).
7. **Verification caveat** on the Cep78-KO mouse quote (see Evidence Base note).

---

## Proposed Follow-up Experiments / Actions

1. **Generate and phenotype a retina/cochlea-focused Cep78 model.** Characterize photoreceptor connecting cilia and cochlear hair-cell kinocilia in Cep78-knockout or conditional/knock-in mice (or in patient-derived retinal organoids and iPSC-derived otic organoids) to convert the inferred Steps 4a/4b into demonstrated mechanisms.
2. **Assemble a CEP78/CEP250 patient registry** with standardized longitudinal ERG, OCT, and pure-tone audiometry to define quantitative natural history (age at legal blindness; audiometric slope; SNHL onset distribution) and penetrance of the fertility phenotype.
3. **Prospectively evaluate cochlear implantation** specifically in CEP78-CRDHL patients, using phoneme/speech-perception scores benchmarked against the Usher CI literature.
4. **Deep structural/functional analysis of the p.Leu150Ser missense allele** and other missense variants to establish genotype-phenotype correlations (null vs. hypomorphic) that may predict severity and residual function — relevant for future variant classification (ACMG/AMP) and therapy eligibility.
5. **Assess gene-augmentation feasibility.** CEP78 is a relatively small centriolar gene; explore AAV-mediated gene replacement or antisense/splice-correction approaches (e.g., for the recurrent c.893-1G>A splice allele) in patient cells and organoids as a proof-of-concept therapeutic strategy.
6. **Screen for CEP78/CEP250 founder alleles** in relevant populations (Jewish-ancestry, Belgian/German cohorts) via carrier screening and cascade testing to inform genetic counseling.

---

## Consensus Answer

Cone-Rod Dystrophy and Hearing Loss (CRDHL; MONDO:0014980, OMIM #617236) is a rare autosomal recessive ciliopathy caused primarily by biallelic loss-of-function of **CEP78**, a distal-centriole protein controlling centriole length and centrosome homeostasis, with an overlapping second locus in **CEP250**. Loss of CEP78 disrupts the specialized cilia and centriole-derived structures of the most centriole-dependent post-mitotic cells, producing childhood-onset cone-predominant cone-rod dystrophy (legal blindness by mid-adulthood), bilateral post-lingual progressive sensorineural hearing loss, and reduced male fertility in some patients — a phenotype distinct from rod-first Usher syndrome. There is no disease-specific therapy; management is supportive (hearing aids/cochlear implantation, low-vision rehabilitation, genetic counseling), with diagnosis by ERG/OCT plus audiometry and panel/exome sequencing.


## Artifacts

- [OpenScientist final report](Cone-rod_Dystrophy_And_Hearing_Loss-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cone-rod_Dystrophy_And_Hearing_Loss-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 16 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000548` (2 mentions) - the report calls it "Clinical sign", "Cone-rod dystrophy"; HP calls it **Cone/cone-rod dystrophy**
- `HP:0000407` (2 mentions) - the report calls it "Clinical sign / lab (audiometry)", "Sensorineural hearing impairment"; HP calls it **Sensorineural hearing impairment**
- `HP:0000618` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Blindness**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000855` (2 mentions) - the report calls it "Cochlear/inner ear hair cell"; CL calls it **sensory hair cell**
- `CL:0000019` (2 mentions) - the report calls it "Sperm / male germ cell"; CL calls it **sperm**, and lists "sperm cell" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000548` - called "Clinical sign", "Cone-rod dystrophy"
- `HP:0000407` - called "Clinical sign / lab (audiometry)", "Sensorineural hearing impairment"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.