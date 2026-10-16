---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T02:38:37.296516'
end_time: '2026-10-15T03:21:52.417936'
duration_seconds: 2595.12
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Familial Hypocalciuric Hypercalcemia 2
  mondo_id: MONDO:0007792
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
citation_count: 27
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 17
  quotes_valid: 17
  relevance_assessed: 27
  on_topic: 19
  validator_version: 0.3.0
term_validation:
  total_terms: 21
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 5
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0007792
    reported_labels:
    - MONDO
    ontology_label: familial hypocalciuric hypercalcemia 2
  - term_id: HP:0003072
    reported_labels:
    - Laboratory abnormality
    ontology_label: Hypercalcemia
  - term_id: HP:0012378
    reported_labels:
    - Symptom
    ontology_label: Fatigue
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Familial_Hypocalciuric_Hypercalcemia_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Familial_Hypocalciuric_Hypercalcemia_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Hypocalciuric Hypercalcemia 2
- **MONDO ID:** MONDO:0007792 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Hypocalciuric Hypercalcemia 2** covering all of the
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

# Familial Hypocalciuric Hypercalcemia Type 2 (FHH2): Comprehensive Disease Characterization

**Disease:** Familial Hypocalciuric Hypercalcemia 2 (FHH2)
**MONDO ID:** MONDO:0007792 · **OMIM:** #145981 · **Category:** Mendelian (autosomal dominant)
**Causal gene:** *GNA11* (Gα11), chromosome 19p13.3

---

## Summary

Familial Hypocalciuric Hypercalcemia type 2 (FHH2) is a rare, autosomal dominant, and generally benign inherited disorder of calcium homeostasis. It is caused by **heterozygous loss-of-function germline mutations in *GNA11***, the gene on chromosome 19p13.3 that encodes **Gα11 (G-protein subunit α-11)** — the heterotrimeric G-protein that couples the **calcium-sensing receptor (CaSR)** to downstream phospholipase C-β (PLCβ) signaling in parathyroid chief cells and renal tubular cells. Because Gα11 is the intracellular relay for the CaSR, loss-of-function variants reduce the potency of extracellular calcium at the receptor, producing a rightward shift (higher EC50) in the calcium concentration–response curve. The physiological consequence is an upward shift in the "set-point" for calcium: the parathyroid glands and kidney behave as though serum calcium were lower than it actually is, so PTH secretion is not suppressed and renal tubular calcium reabsorption persists. Clinically this yields **lifelong mild hypercalcemia, inappropriately normal or high-normal PTH, and relative hypocalciuria** (calcium-to-creatinine clearance ratio, CCCR, typically ≤0.01).

FHH2 is the **rarest of the three recognized FHH subtypes** (FHH1 = *CASR*, ~65% of cases; FHH3 = *AP2S1*; FHH2 = *GNA11*). As of 2026, only approximately eight FHH2 kindreds have been reported worldwide. The condition is usually **asymptomatic with normal life expectancy**, and its principal clinical importance lies in **distinguishing it from primary hyperparathyroidism (PHPT)** so that patients are not subjected to inappropriate and unhelpful parathyroidectomy. When treatment of significant hypercalcemia is warranted, the **calcimimetic cinacalcet** — an allosteric CaSR activator — corrects the biochemical abnormality both in a validated mouse model and in human patients.

*GNA11* behaves as a striking **bidirectional allelic series**: germline **loss-of-function → FHH2** (hypercalcemia); germline **gain-of-function → autosomal dominant hypocalcemia type 2 (ADH2)** (hypocalcemia); and **somatic activating mutations → uveal melanoma** via constitutive MAPK signaling. A newly recognized (2026) manifestation links *GNA11* truncating/deletion variants to **abnormal enamel mineralization**, the first report connecting hypomineralized enamel to a hypercalcemic (rather than hypocalcemic) condition. Perinatally, maternal FHH can cause transient neonatal calcium disturbances in offspring depending on which genotype the newborn inherits.

---

## Section 1 — Disease Information

**Overview.** FHH2 is a Mendelian, autosomal dominant disorder of systemic calcium homeostasis characterized by mild, lifelong, non-progressive hypercalcemia accompanied by inappropriately normal-to-mildly-elevated parathyroid hormone (PTH) and low urinary calcium excretion (relative hypocalciuria). It belongs to the family of familial hypocalciuric hypercalcemia (FHH) syndromes, which together are caused by defects in the CaSR signaling axis.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #145981 (Hypocalciuric hypercalcemia, familial, type II) |
| MONDO | MONDO:0007792 |
| Gene | *GNA11* (HGNC), chromosome 19p13.3 |
| MeSH / ICD | Indexed under Hypercalcemia / Hypercalcemia, familial hypocalciuric (ICD-10 E83.52 family) |
| Orphanet | FHH grouping (ORPHA for familial hypocalciuric hypercalcemia) |

**Synonyms / alternative names:** Familial hypocalciuric hypercalcemia type 2; FHH2; Hypocalciuric hypercalcemia, familial, type II; Familial benign hypercalcemia type 2; GNA11-related FHH.

**Source of information.** The knowledge in this report is derived overwhelmingly from **aggregated disease-level resources** (OMIM, ClinVar, published functional studies) and from **individual case reports / small kindreds** — appropriate given that only ~8 FHH2 families have been described. There is no large EHR-scale cohort specific to FHH2 (unlike FHH1, which has been studied at biobank scale).

---

## Section 2 — Etiology

**Primary cause — genetic (Finding F001).** FHH2 is caused by **heterozygous loss-of-function (inactivating) mutations in *GNA11***, which encodes Gα11, the G-protein that couples the CaSR to intracellular signaling. This is a purely genetic, monogenic Mendelian disorder; there are no established infectious or environmental causes.

> "loss- and gain-of-function mutations of the GNA11 gene on chromosome 19p13.3, which encodes the G-protein α-11 (Gα11) subunit, lead to FHH type 2 and ADH type 2, respectively" — [PMID: 27647839](https://pubmed.ncbi.nlm.nih.gov/27647839/)

> "Type 1 is due to loss-of-function mutations of the calcium-sensing receptor, a guanine nucleotide-binding protein (G-protein)-coupled receptor that signals through the G-protein subunit α11 (Gα11)" — [PMID: 23802516](https://pubmed.ncbi.nlm.nih.gov/23802516/)

**Genetic risk factors.** The causal variants are the *GNA11* loss-of-function alleles themselves. Because inheritance is autosomal dominant with high penetrance, carrying a single pathogenic allele is effectively the disease-defining risk factor. No separate susceptibility loci or modifier genes have been robustly established for FHH2 (small sample sizes preclude modifier mapping).

**Environmental risk factors.** None established. Family history (a first-degree relative with mild hypercalcemia or an unsuccessful parathyroidectomy) is the key non-laboratory clue. Age and sex do not materially alter risk; the trait is present from birth.

**Protective factors.** No genetic or environmental protective factors are documented. Because FHH2 is benign, "protection" is less relevant than for complication-prone disorders.

**Gene–environment interactions.** The most clinically important interaction is **physiological/pharmacological rather than classic GxE**: concurrent exposure to calcium-mobilizing drugs (e.g., antiresorptive regimens) can unmask or exaggerate hypercalcemia (one patient on alternating denosumab/zoledronic acid for osteonecrosis was subsequently diagnosed with FHH; [PMID: 42822749](https://pubmed.ncbi.nlm.nih.gov/42822749/)). Pregnancy is another state that interacts with the genotype (see Section 8).

---

## Section 3 — Phenotypes

FHH2 is typically an **asymptomatic laboratory diagnosis** (Finding F005). Core phenotypes are biochemical.

| Phenotype | Type | HPO term | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Hypercalcemia | Laboratory abnormality | HP:0003072 | Congenital/lifelong | Mild (often <1 mg/dL above ULN) | ~All affected |
| Inappropriately normal/high PTH | Laboratory abnormality | HP:0003165 (hyperparathyroidism) | Lifelong | Mild | ~All affected |
| Hypocalciuria / low CCCR | Laboratory abnormality | HP:0003355-adjacent | Lifelong | — | Majority (CCCR ≤0.01) |
| Low/normal serum phosphorus | Laboratory abnormality | HP:0002148 (hypophosphatemia) | Lifelong | Mild | Variable |
| Fatigue / asthenia | Symptom | HP:0012378 | Adult | Mild | Minority |
| Polyuria / polydipsia | Symptom | HP:0000103 / HP:0001959 | Adult | Mild | Minority |
| Abnormal enamel mineralization | Clinical sign | HP:0000682 (abnormality of dental enamel) | Childhood | Variable | Newly reported (2 families) |

**Characteristics.** Onset is effectively **congenital/lifelong** but usually detected incidentally in **adulthood** on routine biochemistry. Severity is **mild**, and progression is **stable** (non-progressive). In reported FHH2 kindreds there is **no nephrocalcinosis, no kidney stones, and normal bone mineral density on DXA** ([PMID: 42787214](https://pubmed.ncbi.nlm.nih.gov/42787214/), [PMID: 38920275](https://pubmed.ncbi.nlm.nih.gov/38920275/), [PMID: 42291983](https://pubmed.ncbi.nlm.nih.gov/42291983/)).

> "He had no evidence of kidney stones or nephrocalcinosis and demonstrated normal bone mineral density at dual-energy X-ray absorptiometry." — [PMID: 42787214](https://pubmed.ncbi.nlm.nih.gov/42787214/)

**Newly recognized manifestation — enamel hypomineralization (Finding F005).** A 2026 study reported 10 patients from 2 families in whom **hypomineralized enamel co-segregated with hypercalcemia** due to a *GNA11* complete deletion or a frameshift truncation p.(Ser18Argfs*2) — the first link of abnormal enamel mineralization to a hypercalcemic condition.

> "Abnormal enamel mineralization has been reported in genetic conditions associated with hypocalcemia but never with hypercalcemia." — [PMID: 42670332](https://pubmed.ncbi.nlm.nih.gov/42670332/)

**Quality of life.** Because the disorder is usually asymptomatic and non-progressive, **quality-of-life impact is minimal** in the majority. The principal QoL risk is iatrogenic — unnecessary parathyroid surgery following misdiagnosis as PHPT. A minority with higher calcium (>1 mg/dL above ULN) may experience fatigue, polyuria/polydipsia and warrant treatment ([PMID: 42291983](https://pubmed.ncbi.nlm.nih.gov/42291983/)).

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *GNA11* (G protein subunit alpha 11), chromosome **19p13.3**, encoding **Gα11**; disorder OMIM #145981.

**Pathogenic variants (Findings F002, F006).** FHH2 variants are predominantly **missense** loss-of-function changes, with in-frame deletions, frameshift truncations, and whole-gene deletion also reported. Recurrent and representative FHH2-associated variants include:

| Variant (protein) | cDNA | Type | Note |
|---|---|---|---|
| p.Thr54Met | c.161C>T | Missense | Recurrent; at helical/GTPase domain interface; impairs GDP binding |
| p.Thr347Ala | — | Missense | Loss-of-function, FHH2 |
| p.Leu135Gln | — | Missense | Loss-of-function, FHH2 |
| p.Ile200del | — | In-frame deletion | FHH2 |
| p.Tyr101His | c.301T>C | Missense (homozygous) | Homozygous proband; heterozygous parents |
| p.Ser18Argfs*2 | — | Frameshift truncation | Co-segregated with enamel defect |
| Whole-gene deletion | — | Structural | Co-segregated with enamel defect |
| p.Asp195Gly (mouse D195G) | — | Missense | ENU mouse model of FHH2 |

A 10-year cohort of >1,200 probands tested for calcium disorders identified **37 germline *GNA11* variants**, of which 9 nonsynonymous changes (Thr54Met, Arg60His, Arg60Leu, Gly66Ser, Arg149His, Arg181Gln, Phe220Ser, Val340Met, Phe341Leu) were reported as FHH2- or ADH2-causing ([PMID: 36970776](https://pubmed.ncbi.nlm.nih.gov/36970776/)).

**Variant classification.** Reported disease-causing variants are classified **pathogenic/likely pathogenic** by ACMG/AMP criteria, supported by co-segregation and in vitro functional assays (see below). Many additional rare *GNA11* missense changes remain **VUS** pending functional data.

**Allele frequency.** Pathogenic FHH2 alleles are **extremely rare** in population databases (gnomAD), consistent with the ~8 known kindreds; no common susceptibility allele exists.

**Somatic vs germline origin.** FHH2-causing variants are **germline**. In contrast, **somatic** activating *GNA11* mutations occur in uveal melanoma (distinct disease arm; see Section 6 / Finding F006).

**Functional consequences (Finding F002).** FHH2 variants are **loss-of-function**, reducing CaSR-mediated intracellular calcium signaling. In HEK293 cells expressing CaSR, FHH2 Gα11 variants (Thr54Met, Thr347Ala, Leu135Gln, Ile200del) downregulate IP1 accumulation and intracellular Ca²⁺ responses, producing a **rightward shift (higher EC50 / reduced agonist potency)** in the calcium concentration–response curve.

> "loss-of-function variants in GNA11 lead to reduced agonist potency at CaSR and an FHH phenotype" — [PMID: 38920275](https://pubmed.ncbi.nlm.nih.gov/38920275/)

> "Three-dimensional modeling revealed the Thr54Met mutation to be located at the interface between the Gα11 helical and GTPase domains, and to likely impair GDP binding" — [PMID: 26729423](https://pubmed.ncbi.nlm.nih.gov/26729423/)

**Modifier genes / epigenetics / chromosomal abnormalities.** No validated modifier genes or epigenetic mechanisms are established for FHH2. The only reported structural lesion is a **complete *GNA11* deletion** (haploinsufficiency) associated with the enamel phenotype ([PMID: 42670332](https://pubmed.ncbi.nlm.nih.gov/42670332/)).

---

## Section 5 — Environmental Information

FHH2 is a **monogenic disorder with no established environmental, lifestyle, or infectious etiology**. Non-genetic factors are relevant only insofar as they modify measured calcium:

- **Drugs:** antiresorptive therapy (denosumab/bisphosphonates), thiazides, lithium, and vitamin D can perturb calcium and complicate interpretation; one FHH diagnosis emerged during antiresorptive therapy ([PMID: 42822749](https://pubmed.ncbi.nlm.nih.gov/42822749/)).
- **Lifestyle:** no causal dietary or behavioral factor. Calcium/vitamin D intake does not cause the disease but may transiently affect levels.
- **Infectious agents:** none — not applicable.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous loss-of-function variant in *GNA11*** (e.g., Thr54Met) **results in** a Gα11 protein with impaired guanine-nucleotide handling / reduced coupling capacity (Thr54Met impairs GDP binding at the helical/GTPase interface). *[Demonstrated in vitro and by structural modeling.]*
2. Reduced functional Gα11 **leads to** weaker coupling of the plasma-membrane **CaSR** to its effector **phospholipase C-β (PLCβ)** in parathyroid chief cells (and renal tubular cells). *[Demonstrated: reduced IP1/Ca²⁺ responses in CaSR+Gα11 HEK293 assays.]*
3. Diminished CaSR→Gα11→PLCβ signaling **results in** a **rightward shift (higher EC50)** of the calcium concentration–response curve — the receptor now requires a higher extracellular calcium to achieve the same intracellular signal. *[Demonstrated.]*
4. This **raises the calcium "set-point"**: at a normal serum calcium, the cell senses "too little calcium." *[Inferred from set-point model, consistent with CaSR biology.]*
5. In **parathyroid chief cells**, inadequate CaSR signaling **fails to suppress PTH secretion**, so PTH remains **inappropriately normal/high-normal** for the prevailing calcium. *[Demonstrated clinically and in mouse model.]*
6. In the **kidney (distal tubule / thick ascending limb)**, blunted CaSR signaling **leads to continued tubular calcium reabsorption**, producing **relative hypocalciuria (low CCCR)**. *[Inferred from CaSR renal physiology; consistent with clinical phenotype.]*
7. Steps 5 and 6 together **result in** sustained **mild hypercalcemia with hypocalciuria and non-suppressed PTH** — the defining FHH2 triad. *[Demonstrated clinically.]*

**Branch A (reciprocal, same gene):** A **gain-of-function** *GNA11* variant instead **lowers** the set-point → excessive CaSR signaling → suppressed PTH and renal calcium wasting → **ADH2 (hypocalcemia)**.

**Branch B (somatic/oncogenic):** **Somatic activating** *GNA11* mutations in melanocytes constitutively upregulate **MAPK** signaling → **uveal melanoma**.

### Supporting detail

**Molecular pathways (Finding F007).** CaSR is a **family-C GPCR** on the plasma membrane of parathyroid chief cells, also functionally expressed in kidney, bone and gut. It couples via **Gq/G11 → PLCβ**, generating IP3/DAG and raising intracellular Ca²⁺; it also engages AKT and MAPK. PI-PLC β1/β2/β3/β4 isozymes are expressed in parathyroid chief cells and are candidate CaSR effectors ([PMID: 9723859](https://pubmed.ncbi.nlm.nih.gov/9723859/)).

> "On the cell membrane of the chief cells of the parathyroid glands, the CaR 'senses' the extracellular calcium concentration and, subsequently, alters the release of parathyroid hormone (PTH)." — [PMID: 15697170](https://pubmed.ncbi.nlm.nih.gov/15697170/)

> "Functionally significant mutations in the receptor have been shown to induce diseases of calcium homeostasis owing to changes in the set point for calcium-regulated PTH release as well as alterations in the renal handling of calcium." — [PMID: 15697170](https://pubmed.ncbi.nlm.nih.gov/15697170/)

**Protein dysfunction.** FHH2 is a **loss-of-function** of a signal-transducing G-protein α subunit — a defect in **signal relay**, not receptor or hormone structure. Structural modeling localizes the recurrent Thr54Met to the **helical/GTPase domain interface**, impairing GDP binding ([PMID: 26729423](https://pubmed.ncbi.nlm.nih.gov/26729423/)).

**Biochemical abnormality.** The core defect is **receptor–effector uncoupling** causing set-point elevation — an ion-sensing/second-messenger signaling defect rather than an enzyme deficiency.

**Allelic series (Finding F006).**

> "Familial hypocalciuric hypercalcemia type 2 (FHH2) and autosomal dominant hypocalcemia type 2 (ADH2) are due to loss- and gain-of-function mutations, respectively, of the GNA11 gene that encodes the G protein subunit Gα11, a signaling partner of the calcium-sensing receptor (CaSR)." — [PMID: 36970776](https://pubmed.ncbi.nlm.nih.gov/36970776/)

> "somatic Gα11 mutations mediate uveal melanoma development by constitutively up-regulating MAPK signaling" — [PMID: 26994139](https://pubmed.ncbi.nlm.nih.gov/26994139/)

**Suggested ontology terms.** Biological processes: GO:0007200 (phospholipase C-activating GPCR signaling), GO:0055074 (calcium ion homeostasis), GO:0035556 (intracellular signal transduction). Cellular component: GO:0005886 (plasma membrane), GO:0005834 (heterotrimeric G-protein complex). Cell types: CL:0000446 (parathyroid chief cell); renal tubular epithelial cells. Chemical: CHEBI:29108 (calcium(2+) ion).

```
 GNA11 LOF variant
        |
        v
 Gα11 impaired (↓ GDP binding / coupling)
        |
        v
 CaSR -X-> PLCβ   (weak coupling; higher EC50)
        |
        v
 ↑ calcium set-point  ("senses low Ca at normal Ca")
        |
   -------------------------------
   |                             |
 Parathyroid chief cell        Renal tubule
 PTH NOT suppressed            Ca reabsorption continues
   |                             |
   v                             v
 inappropriate normal/high     relative HYPOCALCIURIA
 PTH                            (low CCCR)
   \___________________________/
                |
                v
     MILD HYPERCALCEMIA (benign, lifelong)
```

---

## Section 7 — Anatomical Structures Affected

**Organ level.**
- **Primary:** Parathyroid glands (UBERON:0001132) — chief cells; Kidney (UBERON:0002113) — renal tubule.
- **Body system:** Endocrine system (calcium/mineral homeostasis); urinary system (renal calcium handling).
- **Newly implicated:** Teeth / dental enamel (UBERON:0001752 enamel) in the enamel-hypomineralization kindreds.
- **Secondary involvement:** Minimal. Unlike PHPT, FHH2 kindreds show **no nephrocalcinosis/stones and normal BMD**, so bone and renal parenchyma are largely spared.

**Tissue / cell level.**
- Parathyroid **chief cells** (CL:0000446) — epithelial endocrine cells.
- Renal **tubular epithelial cells** (thick ascending limb / distal tubule).

**Subcellular level.** Plasma membrane (GO:0005886), where CaSR and the heterotrimeric Gq/G11 complex reside; downstream cytosolic second-messenger machinery (PLCβ, IP3/DAG).

**Localization / lateralization.** Systemic (all parathyroid glands and both kidneys); **bilateral/symmetric** by nature of a germline signaling defect.

---

## Section 8 — Temporal Development

**Onset.** Genetically **congenital** (present from birth); clinically detected incidentally, usually in **adulthood**, on routine biochemistry. Onset pattern is **chronic/insidious**.

**Progression.** **Stable and non-progressive** — lifelong mild hypercalcemia without worsening. There are no defined "stages." Disease duration is **chronic/lifelong**.

**Patterns.** No spontaneous remission (it is constitutive). The only clinically relevant **critical period is the perinatal window** (see below) and any time point at which misdiagnosis could trigger unnecessary surgery.

**Pregnancy / neonatal considerations (Finding F008).** FHH (including FHH2) is one of the main **PTH-dependent causes of gestational hypercalcemia** alongside PHPT. Although maternal FHH is itself benign, maternal hypercalcemia transmitted to a **non-carrier fetus** can suppress the fetal parathyroids and cause **transient neonatal hypocalcemia/tetany**; conversely a neonate who **inherits the inactivating variant** may show transient neonatal hyperparathyroidism/hypercalcemia.

> "PTH-dependent etiologies display increased or inappropriately high PTH levels; primary hyperparathyroidism (PHPT) and familial hypocalciuric hypercalcemia (FHH) are the main contributors." — [PMID: 42707509](https://pubmed.ncbi.nlm.nih.gov/42707509/)

> "Severe cases of neonatal hypocalcemia due to fetal hypoparathyroidism may lead to tetany and even death." — [PMID: 42707509](https://pubmed.ncbi.nlm.nih.gov/42707509/)

Management in pregnancy is largely conservative (hydration; cinacalcet crosses the placenta and is generally avoided) with postpartum and neonatal surveillance ([PMID: 36546344](https://pubmed.ncbi.nlm.nih.gov/36546344/), [PMID: 27957351](https://pubmed.ncbi.nlm.nih.gov/27957351/)).

---

## Section 9 — Inheritance and Population

**Epidemiology (Finding F004).** FHH as a whole is rare, with a classic prevalence estimate of **≥1 in 78,000** (West of Scotland); other sources cite ~1:80,000. **FHH2 is the rarest subtype** (FHH1 ~65% of FHH; FHH3 and FHH2 much less common), with only **~8 reported kindreds** worldwide. Precise FHH2-specific incidence/prevalence figures are not established due to rarity and under-ascertainment.

> "We estimate the prevalence to be 1 in 78,000 at least." — [PMID: 11353947](https://pubmed.ncbi.nlm.nih.gov/11353947/)

**Inheritance pattern.** **Autosomal dominant**, high penetrance. A homozygous case (p.Tyr101His) has been reported with heterozygous, presumably milder, parents ([PMID: 41240382](https://pubmed.ncbi.nlm.nih.gov/41240382/)).

**Penetrance / expressivity.** Penetrance of the biochemical trait is **high (near-complete)**; **expressivity is variable** (degree of hypercalcemia, presence or absence of mild symptoms, the newly described enamel phenotype).

**Anticipation / mosaicism / founder effects / consanguinity.** No genetic anticipation (not a repeat-expansion disorder). No established germline mosaicism or founder effects specific to FHH2. Consanguinity is relevant for the rare homozygous presentation.

**Carrier frequency.** Not applicable in the recessive sense (dominant disorder); pathogenic alleles are vanishingly rare in gnomAD.

**Population demographics.** No ethnic predilection established; reported kindreds span multiple populations (e.g., an Italian kindred, [PMID: 42787214](https://pubmed.ncbi.nlm.nih.gov/42787214/)). **Sex ratio ~1:1** (autosomal). Age distribution: present lifelong, diagnosed across adulthood.

---

## Section 10 — Diagnostics

**Clinical/laboratory tests (Finding F004).** The diagnostic signature is:
- **Serum calcium** — mildly elevated (often <1 mg/dL above ULN);
- **PTH** — inappropriately normal or mildly elevated (non-suppressed);
- **24-h urinary calcium / CCCR** — low; **CCCR ≤0.01 is highly suggestive of FHH**, whereas 0.01–0.02 is equivocal and warrants genetic testing;
- **Serum phosphorus** — low/normal; **magnesium** — often high-normal.

> "a calcium clearance to creatinine clearance ratio (Ca urine 24 h. x serum Cr) / (Cr urine 24 h x serum Ca) ≤ 0.01 is highly suggestive of the diagnosis of FHH" — [PMID: 40198177](https://pubmed.ncbi.nlm.nih.gov/40198177/)

Reported FHH2 cases show CCCR/fractional calcium excretion well below 0.01 (e.g., FECa 0.0039; [PMID: 42291983](https://pubmed.ncbi.nlm.nih.gov/42291983/)).

**Imaging.** Parathyroid imaging (ultrasound, sestamibi) is typically **negative** (no adenoma) and helps argue against PHPT; renal imaging shows **no nephrocalcinosis/stones**; DXA shows **normal BMD**.

**Genetic testing.** Definitive diagnosis is by **sequencing *GNA11***, usually via a **familial hypercalcemia / hyperparathyroidism gene panel** (minimally *CASR*, *GNA11*, *AP2S1*, plus syndromic genes). **Whole-exome sequencing (WES)** has identified FHH2 variants in several reports ([PMID: 42291983](https://pubmed.ncbi.nlm.nih.gov/42291983/)). Single-gene *GNA11* testing is appropriate when the biochemical phenotype strongly suggests FHH but *CASR*/*AP2S1* are negative. Cascade testing of relatives follows a confirmed proband.

**Clinical criteria / differential diagnosis.** The pivotal differential is **primary hyperparathyroidism (PHPT)**; distinguishing them prevents **inappropriate parathyroidectomy**. Other differentials: the other FHH subtypes (FHH1 *CASR*, FHH3 *AP2S1*), **acquired hypocalciuric hypercalcemia (AHH)** due to anti-CaSR autoantibodies ([PMID: 40335290](https://pubmed.ncbi.nlm.nih.gov/40335290/)), vitamin-D-metabolism disorders (*CYP24A1*, *SLC34A1*), and reduced GFR.

> "Measurement of the urinary calcium-to-creatinine ratio clearance (UCCR) may help to distinguish patients with FHH from those with PHPT, as the majority of FHH patients have low urinary calcium excretion (UCCR < 0.01)." — [PMID: 38038882](https://pubmed.ncbi.nlm.nih.gov/38038882/)

Genetic testing is especially advised in patients **<30 years** and those with **equivocal CCCR (0.01–0.02)** ([PMID: 40683368](https://pubmed.ncbi.nlm.nih.gov/40683368/)).

**Screening.** Cascade genetic/biochemical screening of first-degree relatives once a proband variant is identified. No newborn screening exists for FHH2.

---

## Section 11 — Outcome / Prognosis

**Survival / mortality.** FHH2 is **benign** with **normal life expectancy**; there is no disease-specific mortality. Unlike PHPT, it does not drive osteoporosis, nephrolithiasis, or renal failure in reported kindreds.

**Morbidity / function.** Minimal. The chief avoidable morbidity is **iatrogenic** — failed/unnecessary parathyroidectomy and its surgical risks when FHH is mistaken for PHPT ([PMID: 38343604](https://pubmed.ncbi.nlm.nih.gov/38343604/), [PMID: 39818302](https://pubmed.ncbi.nlm.nih.gov/39818302/)).

**Complications.** Rare associations reported across FHH generally (e.g., chondrocalcinosis, pancreatitis) are more firmly linked to FHH1; a large genotype-first analysis of FHH1 did **not** confirm population-level excess pancreatitis/diabetes ([PMID: 42640938](https://pubmed.ncbi.nlm.nih.gov/42640938/)). For FHH2 specifically, no consistent complication beyond mild hypercalcemia and the newly described enamel defect is established.

**Prognostic factors.** The main predictor of whether treatment is needed is **degree of hypercalcemia** (symptomatic or >1 mg/dL above ULN favors intervention). No molecular prognostic biomarkers are validated for FHH2.

---

## Section 12 — Treatment

**General principle.** Most patients need **no treatment** — the priority is **correct diagnosis to avoid unnecessary parathyroidectomy** and reassurance/genetic counseling. Surgery is **not indicated** (hypercalcemia persists after parathyroidectomy because the defect is a systemic set-point shift, not an adenoma).

**Pharmacotherapy — calcimimetics (Finding F003).** For **symptomatic or significant hypercalcemia**, the **calcimimetic cinacalcet** (an allosteric CaSR activator; NCIT:C1876) is effective. It potentiates CaSR signaling, compensating for the weakened Gα11 relay.

> "Cinacalcet (30mg/kg orally) significantly reduced plasma albumin-adjusted calcium and PTH concentrations in Gna11+/195G and Gna11195G/195G mice" — [PMID: 29046478](https://pubmed.ncbi.nlm.nih.gov/29046478/)

> "Cinacalcet and NPS-2143 rectified the Ca(2+) i responses of FHH2- and ADH2-associated Gα11 loss- and gain-of-function mutations, respectively" — [PMID: 26994139](https://pubmed.ncbi.nlm.nih.gov/26994139/)

A human FHH2 patient (GNA11 p.Thr54Met) with calcium >1 mg/dL above ULN was treated with **cinacalcet 30 mg daily**; at three months serum calcium decreased and PTH normalized ([PMID: 42291983](https://pubmed.ncbi.nlm.nih.gov/42291983/)). An earlier case also documented cinacalcet correcting FHH2 hypercalcemia ([PMID: 28833550](https://pubmed.ncbi.nlm.nih.gov/28833550/)).

**Pharmacogenomics.** The therapeutic rationale is itself genotype-driven: the **direction of the *GNA11* variant dictates drug choice** — calcimimetics (cinacalcet) for loss-of-function/FHH2; calcilytics (e.g., NPS-2143, investigational) for gain-of-function/ADH2.

**Advanced / experimental therapeutics.** No gene, cell, or RNA therapies exist or are needed for this benign disorder. No disease-specific clinical trials (NCT) are established for FHH2 beyond general calcimimetic use.

**Surgical.** **Contraindicated/ineffective** — parathyroidectomy does not cure FHH.

**Supportive care.** Hydration during intercurrent illness or pregnancy; avoidance of calcium-perturbing drugs; patient education and genetic counseling.

**Treatment strategy.** (1) Confirm diagnosis (biochemistry + CCCR + *GNA11* genetics); (2) reassure and avoid surgery for the asymptomatic majority; (3) reserve **cinacalcet** for symptomatic/marked hypercalcemia; (4) manage pregnancy conservatively with neonatal surveillance.

**Suggested NCIT terms:** Cinacalcet (NCIT:C1876); Calcimimetic Agent; Parathyroidectomy (NCIT:C51764) — listed as *not recommended*.

---

## Section 13 — Prevention

- **Primary prevention:** Not applicable — germline Mendelian disorder cannot be prevented. **Preimplantation/prenatal genetic options** could theoretically be discussed but are rarely pursued given the benign phenotype.
- **Secondary prevention (early detection):** **Cascade genetic and biochemical screening** of first-degree relatives after a proband is identified prevents misdiagnosis and inappropriate surgery.
- **Tertiary prevention (complication avoidance):** The central tertiary-prevention act is **avoiding needless parathyroidectomy**; perinatal surveillance to prevent/treat transient neonatal calcium disturbances.
- **Genetic counseling:** Autosomal dominant 50% transmission risk; counsel on benign prognosis, pregnancy/neonatal implications, and the value of family screening ([PMID: 40757212](https://pubmed.ncbi.nlm.nih.gov/40757212/)).
- **Immunization / public health / environmental:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy:** Humans (*Homo sapiens*, NCBI:txid9606); experimentally modeled in mouse (*Mus musculus*, NCBI:txid10090).
- **Orthologous gene:** *Gna11* in mouse (NCBI Gene ortholog of human *GNA11*).
- **Natural disease in other species:** No well-characterized naturally occurring *GNA11*-FHH2 equivalent is documented in companion animals or wildlife (OMIA does not list an established FHH2 animal counterpart). Not applicable/limited data.
- **Comparative biology:** The CaSR–Gα11 calcium-sensing axis is **evolutionarily conserved** across mammals, which is why the mouse model faithfully recapitulates the human phenotype (see Section 15).
- **Transmission / zoonosis:** Not applicable (non-infectious genetic disease).

---

## Section 15 — Model Organisms

**Mouse model (Finding F003).** An **ENU-generated *Gna11* D195G mouse** (loss-of-function) is the key disease model. It **recapitulates FHH2** with hypercalcemia, normal/raised PTH, and normal urinary calcium. Both heterozygous (*Gna11⁺/¹⁹⁵ᴳ*) and homozygous (*Gna11¹⁹⁵ᴳ/¹⁹⁵ᴳ*) mice are hypercalcemic, and **cinacalcet (30 mg/kg orally) significantly reduced plasma calcium and PTH**, validating the model pharmacologically ([PMID: 29046478](https://pubmed.ncbi.nlm.nih.gov/29046478/)).

| Model | Type | Phenotype recapitulation | Use |
|---|---|---|---|
| *Gna11* D195G mouse (ENU) | Knock-in / point mutant, mammalian | High — hypercalcemia, non-suppressed PTH, normal urine Ca; cinacalcet-responsive | In vivo validation of FHH2 mechanism and calcimimetic therapy |
| CaSR + Gα11 HEK293 cells | In vitro cellular | Functional readout — IP1/Ca²⁺ signaling | Variant functional classification (EC50 shifts); allosteric drug testing |

**Genetic model types available:** point-mutant/knock-in mouse (above); cellular heterologous expression systems. Dedicated knockout, conditional, and humanized FHH2 lines are limited (reflecting rarity).

**Phenotype recapitulation / limitations.** The mouse captures the **biochemical core** (hypercalcemia, PTH, urine calcium) and **drug response** exceptionally well. Limitations: the newly described **enamel phenotype** and **perinatal transient neonatal calcium dynamics** are not yet modeled, and the model does not address human genotype–phenotype diversity across the ~8 kindreds.

**Resources:** MGI (*Gna11*), standard mouse repositories; HEK293/Cellosaurus for the in vitro system.

---

## Mechanistic Model / Interpretation (Synthesis)

FHH2 is best understood as a **set-point disorder of the CaSR–Gα11–PLCβ signaling module**. The CaSR is the thermostat for serum calcium; Gα11 is the wire connecting that thermostat to the cell's effectors. A heterozygous loss-of-function *GNA11* allele partially cuts the wire: the thermostat still "reads" calcium but transmits a weakened signal, so the body defends an **abnormally high calcium level**. Every clinical feature follows from this single lesion — non-suppressed PTH (parathyroid arm), relative hypocalciuria (renal arm), and mild, stable, lifelong hypercalcemia (the integrated output).

The **elegance of the *GNA11* allelic series** reinforces the model: dialing signaling **down** gives hypercalcemia (FHH2); dialing it **up** germinally gives hypocalcemia (ADH2); dialing it **up** somatically in melanocytes gives uveal melanoma. The therapeutic logic is perfectly complementary — **calcimimetics (cinacalcet)** push signaling back up in FHH2, while **calcilytics (NPS-2143)** push it back down in ADH2, each rectifying the respective defect both in vitro and in vivo. This makes FHH2 a textbook example of **mechanism-matched precision pharmacology**, even though most patients require no treatment at all.

| Feature | FHH2 (GNA11 LOF) | ADH2 (GNA11 GOF) | Uveal melanoma (somatic GNA11) |
|---|---|---|---|
| Variant direction | Loss-of-function | Gain-of-function | Somatic activating |
| Calcium | High (mild) | Low | n/a |
| PTH | Non-suppressed/high-normal | Low/normal | n/a |
| Signaling | ↓ CaSR→PLCβ (↑EC50) | ↑ CaSR signaling | Constitutive MAPK |
| Rectifier | Cinacalcet (calcimimetic) | NPS-2143 (calcilytic) | MAPK-pathway oncology |

---

## Evidence Base

| PMID | Role in this report |
|---|---|
| [27647839](https://pubmed.ncbi.nlm.nih.gov/27647839/) | Establishes *GNA11* locus (19p13.3), Gα11 protein, LOF→FHH2 / GOF→ADH2 (F001) |
| [23802516](https://pubmed.ncbi.nlm.nih.gov/23802516/) | Confirms Gα11 as the CaSR signaling partner (F001) |
| [38920275](https://pubmed.ncbi.nlm.nih.gov/38920275/) | FHH2 variants reduce agonist potency at CaSR; Thr347Ala (F002) |
| [26729423](https://pubmed.ncbi.nlm.nih.gov/26729423/) | Thr54Met at helical/GTPase interface impairs GDP binding (F002) |
| [29046478](https://pubmed.ncbi.nlm.nih.gov/29046478/) | *Gna11* D195G mouse; cinacalcet lowers calcium/PTH (F003) |
| [26994139](https://pubmed.ncbi.nlm.nih.gov/26994139/) | Cinacalcet/NPS-2143 rectify FHH2/ADH2 signaling; somatic→uveal melanoma (F003, F006) |
| [11353947](https://pubmed.ncbi.nlm.nih.gov/11353947/) | FHH prevalence ≥1:78,000 (F004) |
| [40198177](https://pubmed.ncbi.nlm.nih.gov/40198177/) | CCCR ≤0.01 diagnostic threshold (F004) |
| [42670332](https://pubmed.ncbi.nlm.nih.gov/42670332/) | Enamel hypomineralization — novel FHH2/GNA11 manifestation (F005) |
| [42787214](https://pubmed.ncbi.nlm.nih.gov/42787214/) | Benign profile: no stones/nephrocalcinosis, normal BMD (F005) |
| [36970776](https://pubmed.ncbi.nlm.nih.gov/36970776/) | Reciprocal LOF/GOF allelic relationship; 37 GNA11 variants (F006) |
| [15697170](https://pubmed.ncbi.nlm.nih.gov/15697170/) | CaSR in chief cells; set-point mechanism (F007) |
| [9723859](https://pubmed.ncbi.nlm.nih.gov/9723859/) | PI-PLC β isozymes in parathyroid chief cells (F007) |
| [42707509](https://pubmed.ncbi.nlm.nih.gov/42707509/) | FHH as PTH-dependent gestational hypercalcemia; neonatal risk (F008) |
| [42291983](https://pubmed.ncbi.nlm.nih.gov/42291983/) | FHH2 case (Thr54Met), FECa 0.0039, cinacalcet response |
| [41240382](https://pubmed.ncbi.nlm.nih.gov/41240382/) | Homozygous p.Tyr101His FHH2 kindred |
| [28833550](https://pubmed.ncbi.nlm.nih.gov/28833550/) | Cinacalcet corrects FHH2 hypercalcemia (human) |
| [38038882](https://pubmed.ncbi.nlm.nih.gov/38038882/) | UCCR<0.01 distinguishes FHH; hereditary PHPT framework |
| [40683368](https://pubmed.ncbi.nlm.nih.gov/40683368/) | Genetic testing for equivocal CCCR 0.01–0.02; cinacalcet |
| [42640938](https://pubmed.ncbi.nlm.nih.gov/42640938/) | FHH1 genotype-first data (comparative; complication context) |
| [36546344](https://pubmed.ncbi.nlm.nih.gov/36546344/), [27957351](https://pubmed.ncbi.nlm.nih.gov/27957351/) | Pregnancy/neonatal management |

---

## Limitations and Knowledge Gaps

1. **Extreme rarity.** With only ~8 FHH2 kindreds reported, nearly all clinical evidence is from **case reports and small series**; there is **no biobank-scale FHH2 cohort** (in contrast to FHH1, now characterized at UK Biobank scale). Penetrance, expressivity, and complication rates are therefore imprecise.
2. **Novel phenotype unconfirmed at scale.** The enamel-hypomineralization association ([PMID: 42670332](https://pubmed.ncbi.nlm.nih.gov/42670332/)) rests on 2 families and awaits independent replication and mechanistic explanation.
3. **Renal arm inferred.** The precise renal tubular contribution to hypocalciuria in FHH2 is inferred from CaSR physiology rather than directly demonstrated in FHH2 tissue.
4. **Model gaps.** The validated mouse captures biochemistry and drug response but not the enamel or perinatal phenotypes.
5. **Modifiers unknown.** No modifier genes, epigenetic mechanisms, or environmental contributors have been mappable given sample size.
6. **Treatment evidence.** Cinacalcet efficacy is supported but limited to a handful of patients and one mouse model; no randomized data exist specifically for FHH2.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international FHH2 registry** pooling *GNA11*-confirmed kindreds to estimate penetrance, expressivity, complication frequency, and the true prevalence of the enamel phenotype.
2. **Genotype-first biobank screening** (UK Biobank, All of Us) for rare *GNA11* LOF variants to define population prevalence and biochemical range, mirroring the FHH1 approach.
3. **Functionally classify VUS:** systematically run candidate *GNA11* missense variants through the CaSR+Gα11 HEK293 IP1/Ca²⁺ assay to resolve ACMG classification and confirm LOF vs GOF direction.
4. **Model the enamel phenotype:** examine amelogenesis in *Gna11*-deficient mice and characterize CaSR/Gα11 signaling in ameloblasts to test whether enamel hypomineralization is a direct *GNA11* effect.
5. **Prospective cinacalcet evaluation** in symptomatic FHH2 patients (small open-label/n-of-1 framework) with calcium, PTH, and urinary calcium endpoints.
6. **Perinatal surveillance protocol:** define evidence-based neonatal calcium monitoring for infants of FHH2 mothers, stratified by inferred fetal genotype.

---

*Prepared from an autonomous 5-iteration investigation: 8 confirmed findings, 43 papers reviewed. Evidence types span human clinical case reports/kindreds, a validated mouse model, in vitro functional assays, and structural/computational modeling.*


## Artifacts

- [OpenScientist final report](Familial_Hypocalciuric_Hypercalcemia_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Familial_Hypocalciuric_Hypercalcemia_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 27 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 13 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007792` (2 mentions) - the report calls it "MONDO"; MONDO calls it **familial hypocalciuric hypercalcemia 2**
- `HP:0003072` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Hypercalcemia**
- `HP:0012378` (1 mention) - the report calls it "Symptom"; HP calls it **Fatigue**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003165` (1 mention) - the report calls it "hyperparathyroidism"; HP calls it **Elevated circulating parathyroid hormone level**, and lists "Elevated serum parathyroid hormone" among its other names
- `HP:0000682` (1 mention) - the report calls it "abnormality of dental enamel"; HP calls it **Abnormal dental enamel morphology**, and lists "Abnormality of dental enamel" among its other names
- `GO:0007200` (1 mention) - the report calls it "phospholipase C-activating GPCR signaling"; GO calls it **phospholipase C-activating G protein-coupled receptor signaling pathway**, and lists "PLC-activating GPCR signaling pathway" among its other names
- `CL:0000446` (2 mentions) - the report calls it "parathyroid chief cell", "chief cells", "Parathyroid **chief cells"; CL calls it **chief cell of parathyroid gland**, and lists "parathyroid chief cell" among its other names
- `UBERON:0001132` (1 mention) - the report calls it "Primary:** Parathyroid glands"; UBERON calls it **parathyroid gland**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000446` - called "parathyroid chief cell", "chief cells", "Parathyroid **chief cells"