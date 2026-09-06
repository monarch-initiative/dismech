---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T21:01:14.175179'
end_time: '2026-08-31T21:53:10.336776'
duration_seconds: 3116.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ORAI1 Deficiency
  mondo_id: ''
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
citation_count: 13
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 13
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 39
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 14
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0001820
    reported_labels:
    - "integument/skin adnexa \u2014 eccrine sweat glands"
    ontology_label: sweat gland
  labels_variant: 5
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
  path: ORAI1_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ORAI1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ORAI1 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ORAI1 Deficiency** covering all of the
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

# ORAI1 Deficiency (CRAC Channelopathy) — Disease Characterization Report

*Autonomous discovery report. Evidence tiers indicated as: [Human clinical], [Model organism], [In vitro], [Computational/inferred]. Primary citations given as PMID.*

---

## Summary / Consensus Answer

**ORAI1 Deficiency** is an ultra-rare, autosomal-recessive primary immunodeficiency caused by **loss-of-function mutations in *ORAI1***, the gene encoding the pore-forming subunit of the plasma-membrane **Ca²⁺ release–activated Ca²⁺ (CRAC) channel**. Loss of ORAI1 abolishes **store-operated Ca²⁺ entry (SOCE)**, crippling the Ca²⁺/calcineurin/NFAT signaling axis. The disease — part of the broader entity **"CRAC channelopathy"** (which also includes STIM1 loss-of-function) — presents as a clinical tetrad: (1) a **severe-combined-immunodeficiency (SCID)-like combined immunodeficiency** with recurrent/severe infections, (2) **autoimmunity/lymphoproliferation**, (3) **non-progressive congenital muscular hypotonia (myopathy)**, and (4) **anhidrotic ectodermal dysplasia** with defective sweating and **dental enamel defects (amelogenesis imperfecta)**. Hematopoietic stem cell transplantation (HSCT) can cure the immunological disease but does not correct the non-hematopoietic (sweat gland, dental, muscle) manifestations.

> **Important nomenclature note:** *ORAI1* is a "two-faced" gene. **Loss-of-function** mutations (the subject of this report) cause the recessive immunodeficiency/CRAC channelopathy described here. **Gain-of-function** mutations in the same gene cause dominant **tubular aggregate myopathy (TAM)** and **Stormorken syndrome** — these are distinct diseases and are NOT "ORAI1 deficiency." They are mentioned only for contrast (PMID: 26469693).

---

## 1. Disease Information

- **Overview:** A monogenic (Mendelian) inborn error of immunity in which absent CRAC-channel function eliminates SOCE in immune and non-immune cells. Because SOCE is the dominant Ca²⁺-influx pathway in T lymphocytes, sweat glands, and tooth-forming ameloblasts, the disorder is multisystem.
- **Key identifiers:**
  - **OMIM (phenotype):** Immunodeficiency 9 (IMD9) **#612782** ("combined immunodeficiency with anhidrotic ectodermal dysplasia").
  - **OMIM (gene):** *ORAI1* **#610277**.
  - **Orphanet:** "CRAC channelopathy" / "Immunodeficiency due to a defect in CRAC channel" (Orphanet groups ORAI1 and STIM1 LOF together).
  - **Mondo:** "immunodeficiency 9" / "combined immunodeficiency due to ORAI1 deficiency" (maps to OMIM #612782; a subtype under immunodeficiency-with-ectodermal-dysplasia); umbrella entity "CRAC channelopathy." (Exact MONDO accession should be verified against the current MONDO release; the OMIM #612782 cross-reference is the stable anchor.)
  - **ICD-10:** D81.8 / D81.9 (combined immunodeficiencies, other/unspecified). **ICD-11:** 4A01.1Y (combined immunodeficiencies).
  - **MeSH:** ORAI1 Protein (D000071140); Severe Combined Immunodeficiency (D016511) as related.
  - **HGNC:** *ORAI1* HGNC:25896; **UniProt** Q96D31; **Ensembl** ENSG00000276045 / ENSG00000152580.
- **Synonyms / alternative names:** Immunodeficiency 9; CRAC channelopathy (ORAI1-type); Combined immunodeficiency due to ORAI1 deficiency; ORAI1-CID; "Anhidrotic ectodermal dysplasia with immunodeficiency" (a distinct, ORAI1-specific form — noted by PMID: 29155098 as distinct from NEMO/IKBKG-related EDA-ID); SCID-like disease with SOCE defect. Older literature: "CRAC channel deficiency."
- **Data source type:** Information is **disease-level and individual-patient (case-report/case-series)** derived. Because <20–30 patients are reported worldwide, evidence comes from small kindreds, functional in-vitro studies of patient cells, and mouse models — not from population EHR or registry aggregates.

---

## 2. Etiology

### Disease Causal Factors
- **Primary cause = genetic.** Biallelic (homozygous or compound heterozygous) loss-of-function variants in *ORAI1* that abolish CRAC-channel function and SOCE [Human clinical; PMID: 16582901, 29155098, 26469693].
- No environmental, infectious, or toxic cause initiates the disease; environmental agents act only as **downstream triggers of complications** (opportunistic infections due to the immunodeficiency).

### Risk Factors
- **Genetic:** The causal biallelic *ORAI1* LOF genotype is necessary and sufficient. **Consanguinity** is a major risk factor because homozygous null alleles predominate in reported kindreds (recessive rare disease). Family history of an affected sib or of consanguineous union raises risk.
- **Environmental / demographic:** None established as causal. **Heat exposure** is a hazard (not a cause) because anhidrosis predisposes to hyperthermia/heat intolerance. Sex is not a risk factor (autosomal).

### Protective Factors
- **Genetic:** Heterozygous carriers are clinically unaffected (recessive), although their T cells show partially reduced SOCE — a **gene-dosage effect** — demonstrating that ~50% channel function is protective [In vitro; PMID: 19075015]. Redundant Ca²⁺-entry contributions from paralogs **ORAI2/ORAI3** and **STIM2** may partially buffer some cell types (basis of variable non-immune expressivity) [Model organism/in vitro; PMID: 28294127].
- **Environmental:** Avoidance of heat, infection prophylaxis, and immune reconstitution are protective interventions (see §12–13), not innate protective factors.

### Gene–Environment Interactions
- The genetic immunodeficiency sets susceptibility; **pathogen exposure** determines which infections manifest. Autoimmune flares may be triggered by infection due to loss of regulatory T-cell tolerance. No formal GxE quantitative data exist for this ultra-rare disease.

---

## 3. Phenotypes

Frequencies are qualitative (small n). HPO term suggestions included.

| Phenotype | Type | Onset | Severity / Course | Frequency | HPO |
|---|---|---|---|---|---|
| Recurrent/severe/opportunistic infections (viral, bacterial, fungal; CMV, EBV, Pneumocystis, candidiasis) | Clinical sign | Neonatal–infantile | Severe, life-threatening; often the presenting feature | Nearly all | HP:0002719 (Recurrent infections), HP:0004430 (Severe combined immunodeficiency) |
| Combined immunodeficiency with **normal lymphocyte counts but impaired T-cell function** | Lab abnormality | Congenital | Persistent | ~All | HP:0005387 (T-cell dysfunction), HP:0002090-adjacent |
| Autoimmunity: autoimmune hemolytic anemia, autoimmune thrombocytopenia, lymphoproliferation/HLH | Clinical sign/lab | Infancy–childhood | Variable, can be severe (HLH reported as presenting event) | Common | HP:0001973 (Autoimmune thrombocytopenia), HP:0001890 (Autoimmune hemolytic anemia), HP:0002665 (Lymphadenopathy) |
| **Non-progressive congenital muscular hypotonia / myopathy** | Physical/sign | Congenital/neonatal | Non-progressive, generally mild-moderate | Most | HP:0008947 (Infantile muscular hypotonia), HP:0003198 (Myopathy) |
| **Anhidrosis / hypohidrosis** (defective sweating) → heat intolerance | Physical sign | Congenital | Lifelong, stable | Most | HP:0000970 (Abnormality of the sweat glands), HP:0000966 (Hypohidrosis), HP:0009927 (Anhidrosis) |
| **Amelogenesis imperfecta / dental enamel defects** | Physical sign | With tooth eruption (childhood) | Lifelong, stable | Most | HP:0000705 (Amelogenesis imperfecta), HP:0006297 (Hypoplastic enamel) |
| Ectodermal dysplasia (broader) | Physical | Congenital | Stable | Common | HP:0000968 (Ectodermal dysplasia) |
| Failure to thrive / growth failure (secondary to infection) | Sign | Infancy | Variable | Common | HP:0001508 (Failure to thrive) |
| Splenomegaly/hepatomegaly (lymphoproliferation) | Sign | Childhood | Variable | Subset | HP:0001744 (Splenomegaly) |

- **Quality-of-life impact:** High burden — recurrent hospitalizations for infection; lifelong infection prophylaxis; heat intolerance restricts activity/climate tolerance; dental restoration needs; muscle weakness affects motor milestones. Without immune reconstitution, early mortality is common. No formal EQ-5D/SF-36 data exist (ultra-rare).
- **Evidence:** PMID: 29155098 (subset deficits, enamel, anhidrosis, muscular dysplasia); PMID: 26469693 (tetrad); PMID: 28633876 (HLH as presenting manifestation of profound CID).

---

## 4. Genetic / Molecular Information

- **Causal gene:** ***ORAI1*** (calcium release-activated calcium modulator 1), **12q24.31**, HGNC:25896, OMIM gene #610277, UniProt Q96D31. Encodes a 301-aa tetraspanning (4-transmembrane) plasma-membrane protein; **six ORAI1 subunits assemble into the hexameric CRAC-channel pore** (concatemer functional analysis, PMID: 27806271; *Drosophila* Orai hexamer structure PDB 4HKR). Key pore/structural residues: **E106** (Ca²⁺ selectivity filter, TM1), **R91** (TM1); disease missense mutations (R91W, G98R, L194P) map to transmembrane/pore-proximal regions.
- **Pathogenic variants (all LOF, biallelic; germline):**
  - **c.271C>T, p.Arg91Trp (R91W)** — first reported, homozygous; misfolds/mis-gates channel, abolishes CRAC current. Identified by combined SNP-array linkage + a *Drosophila* RNAi screen; WT ORAI1 re-expression rescued SOCE/I_CRAC in patient T cells, proving causality [PMID: 16582901].
  - **p.Val181SerfsX8 (frameshift), p.Leu194Pro (missense), p.Gly98Arg (missense)** — homozygous; suppress ORAI1 protein expression and SOCE [PMID: 29155098].
  - Additional reported nulls include a nonsense/premature-stop allele (A88Sfs-type) abrogating protein.
  - **Variant classes:** missense (pore/TM), frameshift, nonsense/premature termination → all functionally **loss-of-function** (no/absent channel or non-conducting channel).
  - **ACMG classification:** reported alleles are **Pathogenic/Likely Pathogenic** (functional SOCE assays = strong PS3 evidence; recessive segregation; absent SOCE).
  - **Allele frequency:** Causal alleles are **absent or ultrarare in gnomAD**; *ORAI1* is relatively tolerant to heterozygous LOF but biallelic LOF is nearly private to consanguineous kindreds.
  - **Somatic vs germline:** **Germline** exclusively.
  - **Functional consequence:** **Loss of function** (recessive). Contrast: **gain-of-function** ORAI1 (e.g., p.G98S, p.L138F, p.P245L, p.T184M) → constitutive SOCE → TAM/Stormorken (dominant) — different disease [PMID: 26469693].
- **Modifier genes:** Paralogous **ORAI2, ORAI3** and ER sensors **STIM1, STIM2** contribute to residual/tissue-specific SOCE and likely modify expressivity of non-immune features [PMID: 28294127].
- **Epigenetic information:** No disease-specific methylation/histone signature reported; not implicated.
- **Chromosomal abnormalities:** None — disease is due to point/small variants, not CNVs or aneuploidy.

---

## 5. Environmental Information

- **Environmental factors:** None causal. Pathogen exposure is the principal external factor determining infectious complications.
- **Lifestyle factors:** Not applicable to a Mendelian gene defect; heat/exercise exposure matters clinically due to anhidrosis (risk of hyperthermia).
- **Infectious agents:** Not a cause; opportunistic pathogens (CMV, EBV, Pneumocystis jirovecii, candida, other viruses/bacteria/fungi) act as **downstream complications** of the T-cell defect [PMID: 26469693; 26109647].

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic LOF mutation in *ORAI1*** → loss/non-function of the CRAC-channel pore subunit in the plasma membrane. [Human clinical/in vitro; PMID: 16582901, 29155098]
2. This **results in abolished store-operated Ca²⁺ entry (SOCE)**: after antigen-receptor engagement, PLCγ → IP₃ depletes ER Ca²⁺ → STIM1 oligomerizes and senses depletion → but with no functional ORAI1, **STIM1 cannot open a Ca²⁺ channel**, so sustained cytosolic Ca²⁺ influx fails. [In vitro; PMID: 17572487]
3. Loss of the sustained Ca²⁺ signal **leads to failure of calcineurin-mediated NFAT dephosphorylation** → **NFAT stays cytoplasmic** → **transcription of IL-2 and other cytokine/chemokine genes fails**. [In vitro; PMID: 17572487]
4. In T cells this **results in impaired proliferation, cytokine production, and effector differentiation** despite *normal* lymphocyte numbers → **SCID-like combined immunodeficiency** → recurrent/opportunistic infections. [Human clinical; PMID: 26469693]
5. **Branch (autoimmunity):** SOCE loss **results in strongly reduced invariant NKT and regulatory T (Treg) cells** and altered γδ-T/NK subsets → **breakdown of peripheral tolerance** → autoimmune cytopenias, lymphoproliferation, HLH. [Human clinical; PMID: 29155098, 28633876]
6. **Branch (ectodermal — sweat glands):** In eccrine sweat-gland epithelium, SOCE drives fluid/electrolyte secretion; ORAI1 loss **leads to defective sweat secretion → anhidrosis → heat intolerance**. [Inferred from tissue expression + phenotype; PMID: 26469693]
7. **Branch (ectodermal — teeth):** In **ameloblasts/enamel cells**, CRAC-channel (ORAI1/2/3 + STIM1/2) SOCE supplies the large Ca²⁺ flux needed for enamel mineralization — demonstrated directly in primary enamel cells (thapsigargin-evoked SOCE blocked by the CRAC inhibitor Synta-66), most abundant at the maturation stage; ORAI1 loss **leads to hypomineralized enamel → amelogenesis imperfecta**. [Model/in vitro + human; PMID: 26515404, 28732182, 28352661, 30114531, 29155098]
8. **Branch (muscle):** SOCE is required for skeletal-muscle Ca²⁺ homeostasis and development; when impaired, muscle is prone to early fatigue and myopathy, so ORAI1 loss **leads to a non-progressive congenital myopathy / muscular hypotonia** (a tissue-autonomous defect not corrected by HSCT). [Human clinical + model; PMID: 26469693, 33262706]. *Note the symmetry: GOF STIM1/ORAI1 → constitutive SOCE → tubular aggregate myopathy (PMID: 31666234) — both excess and deficiency of SOCE injure muscle.*

### Category detail
- **Molecular pathways:** Store-operated Ca²⁺ entry / CRAC-channel pathway; **Ca²⁺–calcineurin–NFAT** signaling (Reactome R-HSA-2672351 "Stimuli-sensing / STIM-ORAI"; KEGG "Calcium signaling pathway" hsa04020). Downstream NFAT target-gene transcription.
- **Cellular processes:** T-cell activation, proliferation, cytokine secretion; immune synapse Ca²⁺ signaling; Treg/iNKT development; sweat-gland fluid secretion; ameloblast biomineralization; myocyte Ca²⁺ handling.
- **Protein dysfunction:** Loss of function — misfolded/mis-gated (missense) or absent (frameshift/nonsense) ORAI1 → non-conducting or absent CRAC channel. Not aggregation-related.
- **Metabolic changes:** No primary metabolic defect; secondary effects on Ca²⁺-dependent mitochondrial/energy signaling possible.
- **Immune system involvement:** Central — combined immunodeficiency **plus** autoimmunity (immunodysregulation), a hallmark "immunodeficiency-with-autoimmunity" pattern.
- **Tissue damage mechanisms:** Infection-driven tissue injury; autoimmune destruction of blood cells; HLH-associated inflammation.
- **Biochemical abnormality:** **Ion-channel defect** — loss of Ca²⁺-selective CRAC conductance (the defining biochemical lesion).
- **Molecular profiling:** Patient T cells/fibroblasts show **absent SOCE** on Ca²⁺ imaging and **absent/greatly reduced CRAC current (I_CRAC)** on patch-clamp; reduced ORAI1 protein by Western/flow [PMID: 29155098]. No large transcriptomic/proteomic/metabolomic disease atlases exist (ultra-rare).
- **Functional genomics:** *Orai1* and *Stim1/2* conditional-knockout mice recapitulate SOCE loss and immune defects, confirming causality [Model organism; PMID: 26109647].

### Suggested ontology terms
- **GO (BP):** GO:0002115 (store-operated calcium entry), GO:0070588 (calcium ion transmembrane transport), GO:0033173 (calcineurin-NFAT signaling cascade), GO:0042110 (T cell activation).
- **GO (MF):** GO:0015279 (store-operated calcium channel activity).
- **GO (CC):** GO:0005886 (plasma membrane), GO:0034704 (calcium channel complex).
- **CL:** CL:0000084 (T cell), CL:0000815 (regulatory T cell), CL:0000921 (NKT cell), CL:0002064 (ameloblast/enamel-forming cell), CL:0000188 (skeletal muscle cell).

---

## 7. Anatomical Structures Affected

- **Organ / system level:**
  - **Primary:** Immune system (thymus-derived T-cell compartment, lymphoid tissues) — UBERON:0002405 (immune system); **integument/skin adnexa — eccrine sweat glands** (UBERON:0001820); **teeth/enamel organ** (UBERON:0001091 tooth; UBERON:0007375 enamel); **skeletal muscle** (UBERON:0001134).
  - **Secondary:** Blood (autoimmune cytopenias, UBERON:0000178); spleen/liver/lymph nodes (lymphoproliferation); lungs/GI (site of recurrent infection).
  - **Body systems:** Immune, integumentary, musculoskeletal, hematologic, dental/craniofacial.
- **Tissue / cell level:**
  - Epithelial: sweat-gland secretory epithelium; ameloblasts (enamel epithelium).
  - Immune: T lymphocytes (esp. Treg, iNKT, γδ-T), NK cells.
  - Muscle: skeletal myofibers.
  - **Cell Ontology:** CL:0000084, CL:0000815, CL:0000921, CL:0002064, CL:0000188, CL:0000623 (NK cell).
- **Subcellular level:** **Plasma membrane** (site of the ORAI1/CRAC channel) and **endoplasmic/sarcoplasmic reticulum** (STIM1 sensor). GO-CC: GO:0005886 (plasma membrane), GO:0005783 (endoplasmic reticulum), GO:0034704 (calcium channel complex).
- **Localization / lateralization:** Systemic and **bilateral/symmetric** (generalized anhidrosis, generalized enamel involvement, generalized hypotonia); not focal or lateralized.

---

## 8. Temporal Development

- **Onset:** **Congenital / neonatal–infantile.** Immunodeficiency typically presents in the **first months of life** with severe infection; muscular hypotonia and anhidrosis are congenital; enamel defects become apparent as teeth erupt (childhood). Onset pattern: **early, chronic**, with acute infectious/autoimmune exacerbations.
- **Progression:**
  - **Immunodeficiency:** persistent/lifelong unless corrected by HSCT; punctuated by acute infections and autoimmune flares (HLH can be fulminant, PMID: 28633876).
  - **Muscular hypotonia:** **non-progressive** (static).
  - **Anhidrosis & enamel defects:** **stable/lifelong**, non-progressive.
- **Course pattern:** Chronic lifelong disease with **episodic** infectious/autoimmune crises superimposed.
- **Remission:** No spontaneous remission of the underlying channel defect. **Treatment-induced immune remission** follows successful HSCT (immune compartment), but ectodermal/muscle features persist because they are non-hematopoietic.
- **Critical period:** **Infancy** is the window of highest mortality and the optimal window for definitive immune therapy (early HSCT before severe infection/organ damage).

---

## 9. Inheritance and Population

- **Epidemiology:** **Ultra-rare.** Fewer than ~30 patients with CRAC channelopathy (ORAI1 + STIM1 LOF combined) reported worldwide; ORAI1-LOF kindreds number a handful. Prevalence/incidence too low to estimate reliably (Orphanet: prevalence <1/1,000,000). No SEER/registry rates.
- **Inheritance:** **Autosomal recessive** (biallelic LOF). [PMID: 16582901, 29155098]
- **Penetrance:** **Complete** for the biallelic null genotype (all reported homozygotes affected); heterozygotes **unaffected** clinically though with subclinical partial SOCE reduction (gene-dosage) [PMID: 19075015].
- **Expressivity:** **Variable** across the tetrad — infection/immune severity and degree of muscle/ectodermal involvement differ between kindreds (possible paralog modifiers).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects:** Individual kindreds carry private homozygous alleles, typically in **consanguineous families**; no broad founder allele established.
- **Consanguinity:** **Major** — most reported cases arise from consanguineous unions (hallmark of rare recessive disease).
- **Carrier frequency:** Not established; biallelic pathogenic genotype essentially absent from population databases.
- **Population demographics:** Reported in multiple ethnicities (consanguineous kindreds from various regions); no strong ethnic predilection beyond consanguinity. **Sex ratio ~1:1** (autosomal). Age distribution skews to **infants/young children** given early onset and historically high mortality.

---

## 10. Diagnostics

- **Clinical / laboratory tests:**
  - **Immunophenotyping (flow cytometry):** *Normal* total T/B/NK counts (distinguishes from typical SCID) but **reduced iNKT and Treg cells**, altered γδ-T/NK subsets; poor in-vitro T-cell proliferation to mitogens/antigens [PMID: 29155098]. Immunoglobulins may be normal or with impaired specific antibody responses.
  - **Functional Ca²⁺ assay (diagnostic gold standard for the mechanism):** **Absent SOCE** on single-cell Ca²⁺ imaging of patient T cells/fibroblasts; **absent I_CRAC** by patch-clamp [In vitro; PMID: 29155098, 16582901].
  - **ORAI1 protein expression:** reduced/absent by Western blot/flow.
  - CBC (autoimmune cytopenias), Coombs test (AIHA), ferritin/triglycerides/sIL-2R (HLH work-up).
  - **Sweat testing** (anhidrosis); dental exam (enamel hypoplasia/amelogenesis imperfecta); muscle exam/CK (usually normal-to-mildly abnormal; hypotonia clinical).
- **Biomarkers:** No circulating molecular biomarker; the functional SOCE defect and *ORAI1* genotype are the definitive markers. LOINC codes apply to component tests (lymphocyte subsets, Ig levels).
- **Imaging / electrophysiology:** No pathognomonic imaging. EMG/muscle biopsy may show non-specific/mild myopathic changes; **patch-clamp electrophysiology** (research) demonstrates absent CRAC current.
- **Biopsy/pathology:** Sweat-gland biopsy shows structurally present but non-functional eccrine glands; tooth histology shows hypomineralized enamel.
- **Genetic testing (definitive):**
  - **Single-gene sequencing of *ORAI1***, or (preferred first-line today) **primary-immunodeficiency gene panels** or **whole-exome sequencing (WES)** / **whole-genome sequencing (WGS)** identifying biallelic *ORAI1* LOF variants; confirm recessive segregation in parents [GTR/ClinVar].
  - CMA/karyotype/FISH: **not indicated** (no CNVs). mtDNA/repeat-expansion testing: not applicable.
- **Clinical criteria:** No formal consensus criteria; diagnosis rests on the phenotypic tetrad + demonstration of absent SOCE + biallelic *ORAI1* LOF.
- **Differential diagnosis:** Classical **SCID** (usually low T-cell counts — ORAI1 has normal counts); **STIM1-LOF CRAC channelopathy** (indistinguishable clinically — test STIM1); **NEMO/IKBKG (EDA-ID)** and **NFKBIA** anhidrotic ectodermal dysplasia with immunodeficiency (distinct — PMID: 29155098 notes ORAI1 form is distinct); **ALPS** and other IPEX-like immunodysregulation for the autoimmune component; primary HLH genes (PRF1, UNC13D) when HLH is the presentation (PMID: 28633876).
- **Screening:** No newborn TREC screening detection (T-cell numbers normal, so **ORAI1 deficiency is typically MISSED by TREC-based newborn SCID screening** — an important caveat). Cascade **carrier testing** in consanguineous families and prenatal/preimplantation testing where the familial variant is known.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** Historically **poor without immune reconstitution** — early death from overwhelming infection or fulminant autoimmunity/HLH is common in infancy/early childhood. With **successful HSCT**, immunological prognosis improves substantially.
- **Morbidity / function:** Even after immune cure, patients retain **lifelong anhidrosis (heat intolerance), dental enamel disease, and muscular hypotonia** because these are non-hematopoietic and not corrected by HSCT — a key prognostic point (PMID: 26469693).
- **Complications:** Opportunistic/severe infections; autoimmune hemolytic anemia and thrombocytopenia; lymphoproliferation; **HLH** (can be presenting and life-threatening, PMID: 28633876); dental morbidity; hyperthermia episodes.
- **Recovery potential:** Immune compartment can be reconstituted (curative for infection/autoimmunity) via HSCT; non-immune features are permanent.
- **Prognostic factors:** Age at diagnosis, severity/organ damage from infection before treatment, occurrence of HLH, and success/timing of HSCT. No validated molecular prognostic biomarker beyond genotype.

---

## 12. Treatment

*(No ORAI1-specific approved drug exists; management is that of combined immunodeficiency with immunodysregulation. NCIT terms suggested.)*

- **Definitive / curative:**
  - **Allogeneic hematopoietic stem cell transplantation (HSCT)** — corrects the hematopoietic/immune defect (donor immune cells have wild-type ORAI1). **Does not** correct sweat-gland, dental, or muscle disease. NCIT: C15431 (Hematopoietic Stem Cell Transplantation). [Supported by disease-mechanism logic + CID management standards; PMID: 26469693]
- **Pharmacotherapy / supportive (symptom & complication management):**
  - **Immunoglobulin replacement (IVIG/SCIG)** for antibody insufficiency — NCIT: C578 (Immunoglobulin Therapy).
  - **Antimicrobial prophylaxis** (e.g., trimethoprim-sulfamethoxazole against *Pneumocystis*; antifungal; antiviral) — NCIT: C15843 (Antibiotic Therapy).
  - **Immunosuppression** for autoimmunity/HLH (corticosteroids, and HLH-directed therapy e.g., etoposide-based protocols when HLH occurs) — NCIT: C15370 (Immunosuppressive Therapy).
  - **Blood product/transfusion support** for autoimmune cytopenias.
- **Advanced / experimental:** **Gene therapy / gene correction** of *ORAI1* in autologous HSCs is a conceptual future approach (not clinically available). No approved RNA/targeted/immunotherapy specific to ORAI1 deficiency. (Note: CRAC-channel *inhibitors*, e.g., under development for autoimmune/inflammatory disease, are the opposite pharmacology and are contraindicated conceptually here.)
- **Supportive / rehabilitative:** **Heat-avoidance and cooling strategies** for anhidrosis; **dental restoration/prosthodontics** for enamel defects; **physiotherapy** for hypotonia; nutritional support.
- **Pharmacogenomics:** Not applicable specifically; standard HSCT-conditioning PGx (e.g., thiopurine/TPMT, busulfan monitoring) applies generically.
- **Treatment algorithm:** Early diagnosis → infection/autoimmune stabilization + prophylaxis + IVIG → definitive **HSCT** → lifelong management of non-immune (dental/sweat/muscle) features and heat precautions.

---

## 13. Prevention

- **Primary prevention:** No way to prevent the genetic lesion. **Genetic counseling** for consanguineous couples/known carriers; **carrier screening**, **prenatal diagnosis**, and **preimplantation genetic testing (PGT)** where the familial *ORAI1* variant is known.
- **Secondary prevention (early detection/treatment):** Early clinical suspicion (infant with infections + anhidrosis + hypotonia + enamel defects) → SOCE functional assay + *ORAI1* sequencing → early HSCT. **Caveat:** standard TREC newborn screening does not detect it (normal T-cell counts).
- **Tertiary prevention (complication reduction):** Infection prophylaxis, IVIG, vaccination caution (avoid **live vaccines** in immunodeficient patients), aggressive management of autoimmunity/HLH, heat-precautions, dental care.
- **Immunization:** Killed/inactivated vaccines per immunodeficiency guidelines; **live vaccines contraindicated**.
- **Counseling:** Autosomal-recessive counseling — 25% recurrence risk per pregnancy for carrier couples; cascade testing of relatives.
- **Public-health/environmental:** Not applicable (monogenic disease).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *ORAI1* is conserved across vertebrates. **Mouse *Orai1*** (NCBI Gene ID 109305; MGI:1925542), **rat *Orai1***, **zebrafish**, and a *Drosophila* ortholog (*Orai*) exist — the pathway was in part dissected in *Drosophila* RNAi screens.
- **Natural disease in other species:** A **naturally occurring ORAI1-associated disorder** in companion/wildlife species is **not well documented** in OMIA; the disease knowledge base is dominated by human patients and engineered animal models. (Not applicable / no strong natural-disease entry.)
- **Comparative biology:** SOCE and the STIM–ORAI mechanism are **evolutionarily conserved** from insects to mammals, making cross-species mechanistic inference valid. Mouse SOCE loss reproduces immune phenotypes, supporting conserved mechanism.
- **Zoonotic potential / transmission:** None (genetic, non-communicable).

---

## 15. Model Organisms

- **Mouse (primary model; *Mus musculus*, NCBI Taxon 10090):**
  - **Global *Orai1* knockout:** severe SOCE loss; reported **perinatal lethality/reduced viability and small body size** in some backgrounds, with immune defects — recapitulating the essentiality of CRAC channels. Surviving KO/knock-in models show impaired T-cell function.
  - ***Orai1* R93W knock-in** (mouse equivalent of human R91W) models the human SCID allele.
  - **Conditional/tissue-specific knockouts** (e.g., *Stim1/Stim2* double conditional; muscle-specific *Orai1* KO) dissect cell-type roles — e.g., muscle-specific *Orai1* deletion abolishes muscle SOCE (PMID: 35939054), and *Stim1/Stim2*-deleted macrophages/DCs surprisingly retain many effector functions, showing lineage-specific SOCE dependence (PMID: 26109647).
  - **Model types available:** knockout, knock-in (point mutant), conditional/floxed, tissue-specific — via MGI/IMPC/KOMP.
- **In vitro / cellular models:** **Patient-derived T cells and fibroblasts** (absent SOCE/I_CRAC) are the definitive human cellular models [PMID: 29155098, 16582901]; heterologous ORAI1/STIM1 expression systems (HEK293) and **concatenated tetramer constructs** quantify gene-dosage effects of R91W [PMID: 19075015]. Ameloblast/enamel-cell models illustrate CRAC-dependent mineralization (PMID: 30114531).
- **Invertebrate:** *Drosophila* Orai/Stim genetic screens established the pathway.
- **Phenotype recapitulation:** Mouse and patient-cell models faithfully reproduce the **SOCE/immune defect**; mouse models capture immune and muscle phenotypes well.
- **Model limitations:** Complete global *Orai1* KO can be perinatally lethal in mice (more severe than the human hypomorphic/viable phenotype), and murine ectodermal (sweat/enamel) and autoimmune features may not fully phenocopy the human tetrad; paralog compensation differs between species.
- **Resources:** MGI (*Orai1* MGI:1925542), IMPC/KOMP, IMSR for strain availability; ZFIN (zebrafish), FlyBase (*Drosophila Orai*).

---

## Supported vs Refuted Hypotheses

- **SUPPORTED:** ORAI1 LOF → abolished SOCE → NFAT-signaling failure → combined immunodeficiency (PMID: 16582901, 17572487, 26469693). ✔
- **SUPPORTED:** ORAI1 loss reduces iNKT/Treg cells → autoimmunity/immunodysregulation (PMID: 29155098, 28633876). ✔
- **SUPPORTED:** Multisystem (sweat gland, dental enamel, muscle) involvement reflects SOCE dependence of those tissues (PMID: 26469693, 30114531). ✔
- **SUPPORTED:** Recessive with dosage-dependent channel function (heterozygotes subclinical) (PMID: 19075015). ✔
- **CONTRAST/REFUTED as same disease:** Gain-of-function *ORAI1* is NOT "ORAI1 deficiency"; it causes dominant TAM/Stormorken (PMID: 26469693). ✔ (kept distinct)

## Limitations & Future Directions
- Ultra-rare disease: all clinical claims rest on small case series; no registry-level epidemiology, QoL, or survival statistics exist. Prevalence, penetrance-by-feature, and long-term HSCT outcomes are under-quantified.
- Some branch mechanisms (sweat gland, enamel) are **inferred** from tissue SOCE dependence and mouse data rather than proven in human tissue in vivo.
- Future: prospective natural-history registries; gene-correction/gene-therapy proof-of-concept; therapies for the non-hematopoietic (dental/sweat/muscle) features not addressed by HSCT.

*Evidence key PMIDs: 16582901 (Feske 2006, first ORAI1 SCID mutation), 29155098 (novel recessive ORAI1 mutations, subset deficits), 26469693 (Lacruz & Feske review, disease definition & GOF contrast), 17572487 (SOCE–NFAT axis), 19075015 (heterozygous gene-dosage), 28633876 (HLH presentation), 30114531 (enamel/CRAC), 26109647 (innate-cell SOCE dependence, mouse), 35939054 (muscle-specific Orai1 KO), 29635109 (ion channelopathies of immune system review).*


## Artifacts

- [OpenScientist final report](ORAI1_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ORAI1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 13 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 20 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0001820` (1 mention) - the report calls it "integument/skin adnexa — eccrine sweat glands"; UBERON calls it **sweat gland**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000921` (2 mentions) - the report calls it "NKT cell"; CL calls it **type I NK T cell**, and lists "type I NKT cell" among its other names
- `CL:0002064` (2 mentions) - the report calls it "ameloblast/enamel-forming cell"; CL calls it **pancreatic acinar cell**
- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle cell"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `UBERON:0001134` (1 mention) - the report calls it "skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names
- `CL:0000623` (1 mention) - the report calls it "NK cell"; CL calls it **natural killer cell**, and lists "NK cell" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.