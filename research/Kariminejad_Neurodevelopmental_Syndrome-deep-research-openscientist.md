---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T08:05:39.092690'
end_time: '2026-09-21T08:24:31.975667'
duration_seconds: 1132.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Kariminejad Neurodevelopmental Syndrome
  mondo_id: MONDO:0975795
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 54
  verified: 51
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0001249
    reported_labels:
    - All (6/6)
    ontology_label: Intellectual disability
  - term_id: HP:0001252
    reported_labels:
    - Frequent
    ontology_label: Hypotonia
  - term_id: HP:0002080
    reported_labels:
    - 1 patient
    ontology_label: Intention tremor
  obsolete_terms:
  - term_id: GO:0017137
    ontology_label: GO_0017137
    replaced_by: GO:0031267
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Kariminejad_Neurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Kariminejad_Neurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kariminejad Neurodevelopmental Syndrome
- **MONDO ID:** MONDO:0975795 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Kariminejad Neurodevelopmental Syndrome** covering all of the
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

# Kariminejad Neurodevelopmental Syndrome (KAREVS) — Comprehensive Disease Characterization

**Disease:** Kariminejad Neurodevelopmental Syndrome (KAREVS)
**MONDO:** MONDO:0975795 · **OMIM:** #620937 · **Gene:** *RBSN* (rabenosyn-5 / ZFYVE20; OMIM \*609511; HGNC:20759)
**Category:** Mendelian, autosomal recessive
**Evidence base:** Predominantly human clinical (2 families, 6 individuals) plus in-vitro/cell-biology and model-organism data on RBSN/rabenosyn-5 function.

> **Note on evidence strength.** KAREVS is an ultra-rare, recently delineated Mendelian disorder described in only two families. Consequently, most clinical statements derive from small aggregated case-level reports (OMIM/primary papers), and many template fields (formal prevalence, survival statistics, QoL instruments, trials) have **no published data**; these are marked *Not available*. Mechanistic claims are supported by direct functional studies of RBSN in patient cells and model organisms.

---

## Summary (Answer to the Research Question)

Kariminejad Neurodevelopmental Syndrome (KAREVS) is an autosomal recessive neurodevelopmental/neuromuscular disorder caused by **biallelic missense variants in the FYVE domain of *RBSN*** (rabenosyn-5), an endosomal Rab4/Rab5 effector. It is characterized by global developmental delay/mild-to-moderate intellectual disability, progressive muscle weakness (myopathy, sometimes with sensorimotor neuropathy or spastic paraplegia), distinctive facial dysmorphism, ophthalmoplegia/ocular anomalies, and variable, nonspecific brain-imaging abnormalities (leukoencephalopathy/delayed myelination). Mechanistically, the FYVE variants abolish binding to phosphatidylinositol-3-phosphate (PI3P), preventing rabenosyn-5 recruitment to early endosomes and thereby **delaying endosomal maturation and impairing endolysosomal degradation while sparing endosomal recycling** — a "separation-of-function" defect. Management is entirely supportive; recurrence risk is 25% and consanguinity is the principal risk factor.

---

## 1. Disease Information

**Overview.** KAREVS (OMIM #620937) is a rare autosomal recessive developmental disorder featuring global developmental delay (delayed walking by a few years, speech delay), impaired intellectual development, hypotonia and progressive muscle weakness, dysmorphic facial features, and variable nonspecific brain-imaging abnormalities. It was first delineated clinically by Kariminejad et al. (2015) in three Iranian siblings and molecularly resolved (gene = *RBSN*) by Paul et al. (2022) [PMID 26192890; PMID 35652444].

> *"two distinct RBSN missense variants are responsible for a novel Mendelian disorder consisting of progressive muscle weakness, facial dysmorphisms, ophthalmoplegia and intellectual disability."* — Paul et al., 2022 (PMID 35652444)

**Key identifiers.**
- **OMIM:** #620937 (phenotype); \*609511 (*RBSN* gene)
- **MONDO:** MONDO:0975795
- **MedGen:** C5975371
- **Orphanet:** No dedicated ORPHAcode identified as of report date (*Not available*)
- **ICD-10:** No specific code; maps to Q87.8 / F79 (general dysmorphic/ID categories) (*no dedicated code*)
- **ICD-11:** No specific code; would fall under LD2F.1Y / 6A00 classes (*no dedicated code*)
- **MeSH:** No dedicated MeSH heading (*Not available*)

**Synonyms / alternative names.** Kariminejad neurodevelopmental syndrome; **KAREVS**; "Intellectual disability, muscle weakness and characteristic face" (original descriptive title, 3p24.3–p25.3-linked recessive syndrome). Not to be confused with **Kariminejad-Nafissi syndrome** (a distinct skeletal dysplasia).

**Data provenance.** Disease-level aggregated resources (OMIM, MONDO, MedGen) built from **individual patient case reports** (2 families, n=6). No EHR/registry-scale data exist.

---

## 2. Etiology

**Causal factor — genetic (Mendelian, monogenic).** KAREVS is caused by **homozygous missense variants in *RBSN***. No environmental, infectious, or multifactorial etiology is involved.

**Genetic risk factors.**
- Causal variants: **c.547G>A (p.Gly183Arg)** — Iranian family; **c.538C>G (p.Arg180Gly)** — Canadian Cree family (both NM_022340.3, FYVE domain) [PMID 35652444].
- **Consanguinity** is the dominant risk factor: both families are consanguineous and homozygous by descent.
- Being a heterozygous carrier of a pathogenic *RBSN* allele confers risk of affected offspring only when both parents carry it (AR).
- Modifier genes: none identified; phenotypic variability (below) is currently unexplained (*candidate modifiers not studied*).

**Environmental / lifestyle / occupational risk factors.** *Not applicable* — no non-genetic contributors are known or expected for a monogenic recessive disorder.

**Protective factors.** None described. In principle, absence of a second pathogenic allele (heterozygosity) is fully protective (carriers are unaffected) [PMID 26192890].

**Gene–environment interactions.** *None described.*

---

## 3. Phenotypes

All phenotypes derive from n=6 patients; "frequencies" are qualitative/small-count estimates from Kariminejad 2015 (Iranian family, F1) and Paul 2022 / OMIM clinical synopsis (Cree family, F2).

| Phenotype | Type | Onset | Severity/Course | Frequency | HPO |
|---|---|---|---|---|---|
| Intellectual disability (mild–moderate; IQ 42, 53) | Cognitive/behavioral | Childhood | Stable–mild, lifelong | All (6/6) | HP:0001249 |
| Global developmental delay (motor, speech) | Sign | Infancy/early childhood | Walking 18–25 mo | All | HP:0001263 / HP:0000750 / HP:0001270 |
| Progressive muscle weakness / myopathy | Sign | Childhood | **Progressive** | All | HP:0003198 / HP:0001324 |
| Hypotonia | Sign | Early | Variable | Frequent | HP:0001252 |
| Distinctive facies (highly arched eyebrows, downslanting palpebral fissures, prominent nasal bridge/nose, columella below alae nasi, narrow mouth, narrow/high palate, maxillary hypoplasia, small chin) | Physical | Congenital | Stable | All | HP:0002553; HP:0000494; HP:0000426; HP:0000160; HP:0000189; HP:0000347 |
| Ophthalmoplegia / impaired eye abduction; ptosis; amblyopia; hypermetropia | Sign | Childhood | Variable | Subset (≥1 each) | HP:0000602; HP:0000508; HP:0000646; HP:0000540 |
| Dental caries | Sign | Childhood | — | Reported | HP:0000670 |
| Short stature | Growth | Childhood | — | Reported (OMIM) | HP:0004322 |
| Leukoencephalopathy / delayed myelination / white-matter hyperintensities | Lab/imaging | Childhood | Nonspecific | 2/3 F1 | HP:0002352; HP:0012448 |
| Hippocampal atrophy; enlarged ventricles | Imaging | Childhood | — | Single patients | HP:0410170; HP:0002119 |
| Spastic paraplegia | Sign | Childhood | Progressive | 2/3 F2 | HP:0001258 |
| Sensorimotor peripheral neuropathy | Sign | Childhood | — | F2 | HP:0007141 |
| Elevated serum CK; elevated lactate; hyperlipidemia; microcephaly | Lab/physical | Childhood | — | Single patients (F2) | HP:0003236; HP:0002151; HP:0003077; HP:0000252 |
| Intention tremor | Sign | Childhood | — | 1 patient | HP:0002080 |

> *"...mild intellectual disability, progressive muscle weakness, and characteristic facies... highly arched eyebrows, down-slanting palpebral fissures, prominent nasal bridge, prominent nose, columella extending below alae nasi, narrow mouth, narrow palate, and dental caries, and in one of them an inability to abduct the left eye."* — Kariminejad et al., 2015 (PMID 26192890)

**Quality-of-life impact.** No formal QoL instruments (EQ-5D/SF-36/PROMIS) have been applied (*Not available*). Expected functional impact: lifelong intellectual disability limiting independent living, plus progressive weakness/spasticity affecting mobility and self-care.

---

## 4. Genetic / Molecular Information

- **Causal gene:** ***RBSN*** (Rabenosyn, RAB effector; aliases **ZFYVE20**, RBSN5). HGNC:20759; NCBI Gene 64145; Ensembl ENSG00000131381; UniProt **Q9H1K0**; OMIM \*609511; cytoband **3p25.3**.
- **Pathogenic variants (KAREVS):**
  - **c.547G>A, p.Gly183Arg** (homozygous; Iranian F1)
  - **c.538C>G, p.Arg180Gly** (homozygous; Cree F2)
  - Both are **missense**, in the **FYVE domain**, **germline**, homozygous; classified **pathogenic/likely pathogenic** (ACMG: segregation, functional evidence, extreme rarity). p.Arg180Gly is present only **once in gnomAD** (allele frequency <1×10⁻⁵); p.Gly183Arg is absent/ultra-rare [PMID 35652444].
  - **Functional consequence:** selective (separation-of-function) loss of function — loss of PI3P binding → failure of early-endosome localization → impaired endosomal maturation/lysosomal degradation with **preserved recycling** [PMID 35652444].
- **Allelic series (distinct *RBSN* disorders):**
  - **p.Gly425Arg** (ZFYVE20 c.1273G>A): severe multi-organ disorder — intractable seizures, developmental delay, microcephaly, dysostosis, osteopenia, dysmorphism, macrocytosis/megaloblastoid erythropoiesis, transient cobalamin deficiency, hypertriglyceridemia, partial cathepsin D deficiency, 50% reduced transferrin uptake (recycling defect) [PMID 25233840].
  - **Biallelic loss-of-function**: **MFANDO** — Myelofibrosis, Congenital, with Anemia, Neutropenia, Developmental delay, and Ocular abnormalities (OMIM #620939). Caused by homozygous **c.289G>C, p.(Gly97Arg)** (NM_022340.3), which actually disrupts splicing of exon 5 → **absence of intact RBSN** (true loss of function) with larger, clustered EEA1-positive endosomes in patient fibroblasts. Three consanguineous sibs: congenital progressive myelofibrosis (reticulin fibrosis by 4 weeks), anemia, severe congenital neutropenia (filgrastim-refractory), thrombocytopenia, developmental delay, ocular anomalies, dysmorphism; proband died at 20 months with 46,XY complete sex reversal and sensorineural hearing loss; **hematopoietic stem-cell/bone-marrow transplant restored blood counts** in surviving sibs (Magoulas et al., 2018, PMID 29784638). This is the key allelic contrast: **KAREVS lacks hematologic disease** and is caused by hypomorphic FYVE missense alleles, whereas MFANDO is a true-LoF, hematologic/multisystem disorder.

  > *"distinct germline mutations in RBSN cause non-overlapping phenotypes with specific and discrete endolysosomal cellular defects."* — Paul et al., 2022 (PMID 35652444)

- **Somatic vs germline:** germline only; no somatic/cancer association in patients (though complete loss is a tumor-suppressor phenotype in *Drosophila*).
- **Modifier genes / epigenetics:** none identified (*Not available*).
- **Chromosomal abnormalities:** none — disease is a point-mutation (missense) disorder; CMA/karyotype normal.

**Ontology.** Gene product: FYVE-domain Rab effector. GO-MF: phosphatidylinositol-3-phosphate binding **GO:0032266**; Rab GTPase binding **GO:0017137**. CHEBI: phosphatidylinositol 3-phosphate **CHEBI:26034**.

---

## 5. Environmental Information

*Not applicable.* KAREVS is a monogenic recessive disorder with **no** established environmental factors, lifestyle contributors, or infectious agents. No toxin/radiation/occupational exposures are implicated (searches of CTD/PubMed yield no environmental modifiers).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Homozygous FYVE-domain missense variant** (p.Gly183Arg or p.Arg180Gly) in *RBSN* **results in** an amino-acid substitution at a conserved residue of the phosphoinositide-binding FYVE finger. *(Demonstrated — genetics/segregation.)*
2. The altered FYVE domain **abolishes binding to phosphatidylinositol-3-phosphate (PI3P)**. *(Demonstrated — biochemistry.)*
3. Loss of PI3P binding **prevents translocation/recruitment of rabenosyn-5 to early endosomal membranes** (mutant protein fails to co-localize with EEA1). *(Demonstrated — cell imaging in patient fibroblasts.)*
4. Endosome-unassociated rabenosyn-5 **cannot properly scaffold the Rab5–VPS45–SNARE fusion/maturation machinery**, **leading to** delayed **early-to-late endosome maturation** and impaired delivery of cargo to lysosomes. *(Demonstrated — cargo tagged for lysosomal degradation accumulates.)*
5. Critically, the **endosomal recycling arm is spared** (separation-of-function) — the pathway branches here, distinguishing KAREVS from the G425R recycling-defect disorder. *(Demonstrated.)*
6. Impaired endolysosomal degradation **results in** accumulation of undegraded cargo and disturbed membrane/receptor homeostasis in **post-mitotic, trafficking-dependent cells (neurons, myofibers)**. *(Inferred from cellular data → tissue phenotype.)*
7. This **leads to** neuronal/white-matter dysfunction (→ intellectual disability, leukoencephalopathy, delayed myelination) and myofiber dysfunction (→ progressive myopathy; ± neuropathy/spastic paraplegia), plus developmental effects on craniofacial patterning (→ dysmorphism). *(Inferred.)*

### Detail by category
- **Molecular pathways:** Rab5/Rab4 GTPase signaling on early endosomes; PI3-kinase→PI3P phosphoinositide signaling; SNARE-mediated membrane fusion via VPS45 (Sec1/Munc18). Not a classic Wnt/MAPK/mTOR disorder, though endolysosomal trafficking intersects growth-factor-receptor signaling.
- **Cellular processes:** early endosome fusion/maturation; receptor-mediated endocytosis; endosome-to-lysosome (degradative) transport; endosomal recycling (spared). Rabenosyn-5 *"is recruited in a phosphatidylinositol-3-kinase-dependent fashion to early endosomes... complexed to the Sec1-like protein hVPS45"* [PMID 11062261].
- **Protein dysfunction:** selective/partial loss of function — the protein is expressed but mislocalized; a hypomorphic/separation-of-function mechanism (not aggregation or dominant-negative). Complete loss is embryonic-lethal, so disease requires residual function.
- **Metabolic changes:** secondary and variable — elevated lactate and CK in some patients (suggesting mitochondrial/muscle stress); hyperlipidemia in one; the allelic G425R disorder shows cobalamin deficiency/hypertriglyceridemia (trafficking of nutrient receptors).
- **Immune involvement:** none in KAREVS (no hematologic/immune phenotype; contrast RBSN congenital myelofibrosis).
- **Tissue damage mechanisms:** inferred chronic cellular trafficking stress in neurons and myofibers; no fibrosis/ischemia mechanism.
- **Biochemical abnormalities:** loss of PI3P–FYVE interaction; partial cathepsin D processing defect described for the allelic G425R variant.
- **Epigenetic changes / omics profiling:** *Not available* (no transcriptomic/proteomic/metabolomic/single-cell datasets published for KAREVS).

**Cell types (CL):** neuron **CL:0000540**; skeletal muscle fiber **CL:0000188**; fibroblast (model) **CL:0000057**; oligodendrocyte (myelination, inferred) **CL:0000128**.
**Biological process (GO):** endosome to lysosome transport **GO:0008333**; early endosome to late endosome transport **GO:0045022**; endosomal transport **GO:0016197**; regulation of endosome size/maturation; vesicle fusion **GO:0006906**.

---

## 7. Anatomical Structures Affected

- **Organ/system level (primary):** **central nervous system** (brain — cerebral white matter, hippocampus, ventricles) and **skeletal muscle** (neuromuscular system). Secondary/associated: **peripheral nerves** (sensorimotor neuropathy), **eye/extraocular muscles** (ophthalmoplegia, ptosis, refractive error), **craniofacial skeleton** (dysmorphism, maxillary hypoplasia), **skeletal growth** (short stature).
- **Body systems:** nervous (central + peripheral), musculoskeletal, ophthalmologic. **Not** primarily cardiovascular, respiratory, renal, or hematologic (distinguishing from allelic RBSN disorders).
- **Tissue/cell level:** nervous tissue (neurons, myelinating glia), striated muscle tissue (myofibers). Ubiquitously expressed gene, but post-mitotic trafficking-dependent tissues are most vulnerable.
- **Subcellular level:** **early endosome** (primary site of RBSN action) — GO cellular component early endosome **GO:0005769**, early endosome membrane **GO:0031901**; downstream **lysosome GO:0005764**; cytoplasmic vesicle. UniProt localizes rabenosyn-5 to the cytoplasmic face of early endosomes.
- **Localization / UBERON:** brain **UBERON:0000955**; cerebral white matter **UBERON:0002316**; hippocampus **UBERON:0002421**; lateral ventricle **UBERON:0002285**; skeletal muscle **UBERON:0001134**; peripheral nerve **UBERON:0001021**; extraocular muscle **UBERON:0002417**.
- **Lateralization:** generally **bilateral/symmetric** (developmental/systemic); the original ocular finding (impaired abduction) was reported as unilateral (left eye) in one patient.

---

## 8. Temporal Development

- **Onset:** **congenital / early-childhood**, insidious. Motor and speech delay evident in infancy; independent walking delayed to 18–25 months [PMID 26192890].
- **Progression:** **chronic and slowly progressive**, principally the neuromuscular component (*"progressive muscle weakness"*); intellectual disability is relatively static. Spastic paraplegia (Cree family) is progressive.
- **Disease course:** progressive/stable hybrid — cognitive impairment stable, motor/neuromuscular features progressive. No episodic/relapsing pattern.
- **Duration:** lifelong. Survival into adulthood documented (Paul 2022 followed the original Iranian family long-term).
- **Remission:** none (no spontaneous or treatment-induced remission).
- **Critical periods:** early childhood (developmental/rehabilitation window); no proven pharmacologic intervention window.

---

## 9. Inheritance and Population

- **Epidemiology:** **ultra-rare.** Only **6 individuals from 2 families** reported worldwide (3 Iranian sibs; 3 Canadian Cree across 2 generations). Formal **prevalence/incidence not established** (consistent with <1/1,000,000).
- **Inheritance:** **autosomal recessive** (homozygous *RBSN* variants; unaffected consanguineous carrier parents) [PMID 26192890; PMID 35652444].
- **Penetrance:** appears **complete** in homozygotes (all reported homozygotes affected); carriers unaffected.
- **Expressivity:** **variable** — the Cree family expanded the phenotype (spastic paraplegia, neuropathy, ↑CK/↑lactate, microcephaly, hyperlipidemia, enlarged ventricles) beyond the Iranian family.
- **Genetic anticipation:** none (not a repeat-expansion disorder).
- **Germline mosaicism:** none reported.
- **Founder effects:** the two alleles are **family-private** (G183R Iranian; R180G Cree) — plausibly founder alleles within each consanguineous kindred rather than a broad population founder variant.
- **Consanguinity:** **central** — both families consanguineous; homozygosity mapping was the key discovery tool.
- **Carrier frequency:** not defined; RBSN pathogenic alleles are extremely rare in gnomAD (R180G seen once).
- **Population demographics:** reported in **Iranian** and **Canadian Indigenous (Cree)** populations. Sex ratio ~1:1 (both sexes affected). Age distribution: pediatric-through-adult.

---

## 10. Diagnostics

- **Definitive test:** **molecular genetic testing.** In consanguineous families, **homozygosity mapping + whole-exome (WES) or whole-genome (WGS) sequencing** identifies biallelic *RBSN* variants (confirmed by Sanger segregation) [PMID 26192890; PMID 35652444]. Single-gene/**RBSN**-inclusive neurodevelopmental or myopathy gene panels are appropriate when the phenotype is recognized.
  > *"Using exome sequencing, we identified recessively acting germline alleles p.Arg180Gly and p.Gly183Arg."* — Paul et al., 2022 (PMID 35652444)
- **CMA / karyotype / FISH:** expected **normal** (no CNV/structural/aneuploidy cause) — useful mainly to exclude mimics.
- **Mitochondrial DNA / repeat-expansion testing:** not indicated for causation, but mtDNA studies may be considered to exclude mitochondrial disease given elevated lactate/CK in some patients.
- **Supportive clinical tests:**
  - **Electrophysiology (EMG/NCS):** myopathic pattern; sensorimotor neuropathy in some [PMID 26192890].
  - **Muscle biopsy:** nonspecific.
  - **Neuroimaging (MRI):** leukoencephalopathy, delayed myelination, frontal/parietal white-matter hyperintensities, hippocampal atrophy, enlarged ventricles (variable).
  - **Labs:** serum CK and lactate may be elevated in a subset; no specific biomarker.
- **Omics-based diagnostics:** none validated (*Not available*); functional PI3P-binding/endosomal-localization assays are research tools that can support variant interpretation.
- **Clinical criteria:** no formal consensus criteria; diagnosis = compatible phenotype + biallelic pathogenic *RBSN* variants.
- **Differential diagnosis:** other AR syndromic intellectual disability with myopathy and dysmorphism; congenital/metabolic myopathies; mitochondrial encephalomyopathies (↑lactate/CK); hereditary spastic paraplegias with cognitive involvement; and the **distinct RBSN-opathies** — the G425R seizure/microcephaly phenotype (PMID 25233840) and **MFANDO** congenital myelofibrosis with cytopenias (OMIM #620939, PMID 29784638). Distinguishing feature of KAREVS: characteristic facies + progressive myopathy **without** hematologic abnormality, with FYVE-domain *RBSN* genotype.
- **Screening:** no newborn-screening assay. **Carrier and cascade testing** feasible once the family variant is known; **prenatal / preimplantation genetic diagnosis** feasible for at-risk pregnancies.

**NCIT:** Whole Exome Sequencing; Whole Genome Sequencing; Genetic Testing; Magnetic Resonance Imaging; Electromyography.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** No disease-specific mortality data. Reported patients **survived into adulthood**; life-limiting complications not documented in the small cohort (*formal survival statistics Not available*).
- **Morbidity / disability:** Principal morbidity is **lifelong intellectual disability** plus a **progressive neuromuscular disability** (weakness ± spasticity/neuropathy) affecting mobility, and ocular/visual impairment. ICF-level functional limitations in mobility, communication, and self-care are expected.
- **Quality-of-life measures:** none applied (*Not available*).
- **Complications:** progressive weakness/contractures, spasticity, visual impairment; potential feeding/dental issues (narrow palate, caries). No organ failure described.
- **Recovery potential:** none (non-remitting); rehabilitation can improve function but not reverse the underlying deficit.
- **Prognostic factors:** genotype (allelic series predicts severity/organ involvement); presence of spastic paraplegia/neuropathy may portend greater motor disability. No validated prognostic biomarkers.

---

## 12. Treatment

**No disease-modifying or curative therapy exists.** Management is **supportive, multidisciplinary, and symptom-directed** (extrapolated from standard care for AR syndromic ID/myopathy; no KAREVS-specific trials).

- **Pharmacotherapy:** no targeted drug. Symptomatic agents as needed (e.g., antispasticity agents such as **baclofen** for spastic paraplegia; standard management of any seizures). **Pharmacogenomics:** none specific.
- **Advanced therapeutics (gene/cell/RNA/targeted/immunotherapy):** **none available**; entirely theoretical. Gene-replacement/editing is conceptually plausible (recessive LoF) but faces the barrier that complete loss is lethal and CNS delivery is unsolved — no programs exist (*Not available*).
- **Surgical/interventional:** as indicated for complications (e.g., strabismus/ptosis surgery, orthopedic management of contractures).
- **Supportive & rehabilitative (mainstay):** **physical therapy** (weakness, spasticity, contracture prevention), **occupational therapy**, **speech-language therapy**, special education/developmental support, **ophthalmologic correction** (refractive error, amblyopia, ptosis/strabismus), **dental care**, and **nutritional support** as needed.
- **Experimental treatments / trials:** none registered (*Not available*).
- **Treatment outcomes / adverse events:** no cohort data.
- **Treatment strategy:** individualized supportive care coordinated by clinical genetics, neurology, physiatry, ophthalmology, and rehabilitation services.

**NCIT:** Physical Therapy; Occupational Therapy; Speech Therapy; Supportive Care; Rehabilitation Therapy; Baclofen.

---

## 13. Prevention

- **Primary prevention:** **genetic counseling** for consanguineous couples and families with an affected child; **carrier testing** of at-risk relatives; **preconception/prenatal counseling**. Recurrence risk to siblings = **25%**.
- **Secondary prevention (early detection):** **cascade carrier screening** in the extended family; **prenatal diagnosis** or **preimplantation genetic testing (PGT-M)** once the familial *RBSN* variant is known.
- **Tertiary prevention:** early developmental intervention, physiotherapy to prevent contractures, proactive ophthalmologic and dental care to limit complications.
- **Immunization / public-health / environmental / behavioral / prophylaxis measures:** *Not applicable* (no infectious/environmental component). Standard childhood immunizations as per general guidelines.
- **Counseling:** autosomal-recessive genetic counseling is the cornerstone of prevention (NSGC/ACMG frameworks).

**NCIT:** Genetic Counseling; Genetic Carrier Screening; Prenatal Diagnosis.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring KAREVS-equivalent disease is reported in any non-human species (OMIA: none). Human — *Homo sapiens* (NCBI:txid9606).
- **Orthologous genes (NCBI Gene / model):**
  - Mouse *Rbsn* (MGI:1925537; UniProt Q80Y56)
  - *Drosophila* *Rbsn* / CG8506
  - *C. elegans* *rabs-5*
  - *S. cerevisiae* functional homolog **VAC1**
- **Natural disease in animals / veterinary relevance / breeds (VBO):** none known (*Not applicable*).
- **Comparative biology:** the rabenosyn-5–VPS45–Rab5 endosomal-fusion module is **deeply conserved from yeast to humans**, so cellular disease mechanisms translate across species even though the human neurodevelopmental phenotype is not naturally observed elsewhere. *"Rabenosyn-5 is a closer mammalian functional homologue of yeast Vac1p than EEA1."* [PMID 11062261].
- **Transmission / zoonotic potential:** *Not applicable* (genetic, non-transmissible).

---

## 15. Model Organisms

- **Cellular / in vitro (most relevant to KAREVS):** **patient-derived fibroblasts** (p.Gly183Arg) demonstrate the disease mechanism — loss of punctate endosomal localization, failure to co-localize with EEA1, and accumulation of lysosome-targeted cargo [PMID 35652444]. iPSC-derived neurons/myotubes are logical (not yet published) models.
- **Mouse (*Rbsn*, MGI:1925537):** **whole-body knockout is embryonic-lethal** — recapitulates the essential trafficking role but **not** the viable human phenotype; a **knock-in of the human missense (hypomorphic) allele or conditional/tissue-specific model** would be required to model KAREVS. No published KAREVS mouse to date.
- ***Drosophila* (Rbsn/CG8506):** null mutants show defective early-endosome formation, loss of epithelial polarity, and neoplastic overgrowth (Rbsn as tumor suppressor), establishing the Rbsn–Vps45–Rab5–Avalanche fusion module in vivo [PMID 18685079].
- ***C. elegans* (rabs-5 / vps-45):** mutants show endocytic defects with accumulation of aberrantly small endosomes, confirming RABS-5/VPS-45 cooperation downstream of RAB-5 [PMID 17235359].
- **Yeast (*VAC1*):** the functional homolog coordinates Rab/PI3K signaling in VPS45-dependent endosomal docking/fusion [PMID 11062261].
- **Phenotype recapitulation:** model organisms faithfully reproduce the **cellular/endosomal** mechanism but **not** the specific human neurodevelopmental/neuromuscular disease, because null alleles are lethal and human disease arises from residual-function missense alleles. **Model limitation:** need for allele-specific (knock-in) and CNS/muscle-conditional models.
- **Applications:** these models illuminate endosomal fusion/maturation, PI3P–FYVE biology, and Rab5-effector function; allele-specific models would enable therapy testing.
- **Resources:** MGI (mouse), FlyBase (Drosophila), WormBase (C. elegans), SGD (yeast), IMPC/IMSR.

---

## Supported vs. Refuted Hypotheses

**Supported:**
- KAREVS is caused by biallelic FYVE-domain *RBSN* missense variants (AR) — *strongly supported* (segregation in 2 families + functional data) [PMID 26192890; PMID 35652444].
- Mechanism is loss of PI3P binding → endosomal mislocalization → delayed endosomal maturation with spared recycling (separation-of-function) — *supported* (patient-cell biochemistry/imaging) [PMID 35652444].
- Distinct *RBSN* variants cause distinct disorders via distinct endolysosomal defects — *supported* [PMID 35652444; PMID 25233840].

**Refuted / excluded:**
- Environmental, infectious, or chromosomal causation — *excluded* (purely monogenic).
- Hematologic involvement as part of KAREVS — *excluded* in reported families (distinguishes from RBSN congenital myelofibrosis).
- Complete-null mechanism — *refuted* (null is lethal; disease requires hypomorphic alleles).

## Limitations and Future Directions

- **Very small n (6 patients, 2 families):** frequencies, penetrance, expressivity, prognosis, and QoL are provisional. No registry, natural-history study, or trials exist.
- **No omics data** (transcriptomics/proteomics/metabolomics) for patient tissues.
- **Phenotypic variability unexplained** (candidate modifier genes and genotype–phenotype rules need larger cohorts, e.g., via GeneMatcher).
- **Priorities:** identify additional families; generate allele-specific mouse/iPSC-neuron/myotube models; define natural history; explore whether modulating endolysosomal maturation or the PI3P–FYVE interaction is therapeutically tractable.

---

### Key References (PMIDs)
- **26192890** — Kariminejad et al., 2015. Original clinical delineation; 3p24.3–p25.3 mapping (human clinical).
- **35652444** — Paul et al., 2022. *RBSN* gene identification; FYVE variants; separation-of-function mechanism (human clinical + in vitro).
- **25233840** — Stöckler et al., 2014. Distinct *RBSN*/ZFYVE20 p.Gly425Arg disorder (human clinical + in vitro).
- **29784638** — Magoulas et al., 2018 (*Blood*). MFANDO — syndromic congenital myelofibrosis from RBSN loss-of-function p.Gly97Arg splice variant; BMT restores hematology (human clinical + in vitro).
- **11062261** — Nielsen et al., 2000. Rabenosyn-5 as Rab5 effector, FYVE/PI3K recruitment, hVPS45 complex, Vac1p homolog (in vitro).
- **18685079** — Morrison et al., 2008. *Drosophila* Rbsn–Vps45 endosomal-entry module; tumor suppressor (model organism).
- **17235359** — Gengyo-Ando et al., 2007. *C. elegans* VPS-45/RABS-5 in RAB-5-dependent endocytosis (model organism).


## Artifacts

- [OpenScientist final report](Kariminejad_Neurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Kariminejad_Neurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 51 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001249` (1 mention) - the report calls it "All (6/6)"; HP calls it **Intellectual disability**
- `HP:0001252` (1 mention) - the report calls it "Frequent"; HP calls it **Hypotonia**
- `HP:0002080` (1 mention) - the report calls it "1 patient"; HP calls it **Intention tremor**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0017137` (GO_0017137) (1 mention) - replaced by `GO:0031267`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.