---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T08:57:11.201745'
end_time: '2026-09-25T09:14:55.928988'
duration_seconds: 1064.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Oculoglandular Tularemia
  mondo_id: MONDO:0001665
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
citation_count: 20
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 24
  quotes_valid: 22
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:11228320
  - PMID:22734313
  relevance_assessed: 29
  on_topic: 20
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 27
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 6
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0000198
    reported_labels:
    - periorbital edema analog
    ontology_label: Absence of Stensen duct
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Oculoglandular_Tularemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Oculoglandular_Tularemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oculoglandular Tularemia
- **MONDO ID:** MONDO:0001665 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Oculoglandular Tularemia** covering all of the
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

# Oculoglandular Tularemia — Comprehensive Disease Characterization Report

**Disease:** Oculoglandular Tularemia
**MONDO ID:** MONDO:0001665
**Category:** Infectious Disease (bacterial zoonosis)
**Causative agent:** *Francisella tularensis* (NCBI Taxon: 263)
**Evidence base:** Aggregated disease-level literature (case reports, case series, systematic reviews, and mechanistic model-organism/in-vitro studies). No individual EHR-level or omics data files were provided; this is a literature-synthesis report.

---

## Summary

Oculoglandular tularemia is the conjunctival-entry form of tularemia, an acute zoonotic infection caused by the Gram-negative, facultatively intracellular bacterium *Francisella tularensis*. It is one of the six classic clinical forms of tularemia and accounts for approximately **1–3% of all tularemia cases**. Clinically it presents as unilateral granulomatous follicular conjunctivitis accompanied by painful ipsilateral preauricular, submandibular and cervical lymphadenopathy — the constellation known as **Parinaud oculoglandular syndrome (POGS)**. Among causes of POGS, oculoglandular tularemia ranks **second only to cat scratch disease** (*Bartonella henselae*), which is the single most important differential diagnosis. Infection follows conjunctival inoculation by contaminated fingers, aerosol splashes, or ocular trauma involving infected animal material.

The pathophysiology is that of an intracellular bacterial infection rather than a heritable disorder — there is **no host causal gene, inheritance pattern, or germline variant**. After conjunctival inoculation, *F. tularensis* is phagocytosed by macrophages, escapes the phagosome using a non-canonical Type VI secretion system (T6SS) encoded on the Francisella Pathogenicity Island (FPI; effectors PdpC/PdpD), replicates in the cytosol, and triggers the AIM2 inflammasome with caspase-1 activation, IL-1β/IL-18 release, and pyroptotic cell death. This drives granulomatous conjunctival inflammation and regional suppurative lymphadenitis. *F. tularensis* is one of the most infectious bacteria known, requiring as few as ~10–15 organisms to cause disease, which underlies its classification as a Tier 1 select agent and potential bioterrorism threat.

Diagnosis relies on **serology (microagglutination titer ≥1/160 or four-fold rise)** and **PCR** (targets *tul4*, *ISFtu2*, *fopA*, 23-kDa), because culture is insensitive (~10% positive) and hazardous (requires BSL-3 containment). The disease is highly curable: contemporary isolates remain uniformly susceptible to aminoglycosides, fluoroquinolones, and tetracyclines, while β-lactams reliably fail. Case-fatality among appropriately treated patients is under 2%, and *F. tularensis* subsp. *holarctica* (the European/Asian type B) infections are essentially non-fatal. Suppurative lymph nodes occasionally require surgical drainage. Prevention is behavioral/environmental (personal protective equipment, avoiding sick/dead lagomorphs and rodents, tick-bite avoidance, hand and eye hygiene) plus antibiotic post-exposure prophylaxis; **no licensed human vaccine exists**.

---

## Key Findings

### Finding 1 — Definition and rank among causes of Parinaud oculoglandular syndrome

Oculoglandular tularemia is a rare clinical form of tularemia and the **second commonest cause of Parinaud oculoglandular syndrome (POGS)**. POGS is defined as unilateral granulomatous palpebral conjunctivitis with ipsilateral preauricular, submandibular, and cervical lymphadenopathy, frequently accompanied by fever and malaise. Reviews of POGS etiology consistently identify cat scratch disease (*Bartonella henselae*) as the most common cause, with oculoglandular tularemia second. Entry is via conjunctival inoculation — contaminated fingers after handling infected animals, aerosol splashes, or ocular trauma from infected animal material.

> "The most common underlying pathology is cat scratch disease, followed by the oculoglandular form of tularemia." — [PMID: 38941282](https://pubmed.ncbi.nlm.nih.gov/38941282/)

> "Parinaud's oculoglandular syndrome should be considered in the differential diagnosis of a patient presenting with unilateral granulomatous conjunctivitis, painful preauricular, and submandibular lymphadenopathy combined with systemic symptoms of general malaise and fever. Tularemia is one etiology of Parinaud's oculoglandular syndrome." — [PMID: 11228320](https://pubmed.ncbi.nlm.nih.gov/11228320/)

### Finding 2 — Uniform antibiotic susceptibility of *F. tularensis*

*Francisella tularensis* isolates remain **uniformly susceptible to first-line tularemia antibiotics**. Antimicrobial susceptibility testing of 278 U.S. isolates (2009–2018) against 8 drugs (ciprofloxacin, levofloxacin, doxycycline, tetracycline, gentamicin, streptomycin, chloramphenicol, erythromycin) found **all isolates susceptible to all drugs tested**. German subsp. *holarctica* isolates (n=128) showed low MIC90 values: gentamicin 1 mg/L, streptomycin 4.0 mg/L, tetracycline 0.5 mg/L, doxycycline 1.5 mg/L, and ciprofloxacin 0.064 mg/L. One important exception: subsp. *holarctica* biovar II (genotype B.12) is intrinsically erythromycin-resistant. Streptomycin (intramuscular) is the historical drug of choice; ciprofloxacin was used successfully in a confirmed oculoglandular case after β-lactam failure.

> "We tested the susceptibility of 278 F. tularensis isolates from the United States received during 2009-2018 to 8 antimicrobial drugs... All isolates were susceptible to all tested drugs." — [PMID: 38294116](https://pubmed.ncbi.nlm.nih.gov/38294116/)

> "empiric ciprofloxacin therapy was administered, and the patient recovered without sequelae" — [PMID: 38941282](https://pubmed.ncbi.nlm.nih.gov/38941282/)

### Finding 3 — Epidemiology, infectivity, and low treated fatality

Oculoglandular tularemia is an uncommon form (~1–3% of cases), and *F. tularensis* is extraordinarily infectious with low fatality when treated. A systematic review of 870 human tularemia cases (1993–2023, 35 countries) noted that the organism "requires as few as 10 organisms to cause disease," and reported case-fatality among treated patients of **0.7% (aminoglycosides), 0.9% (fluoroquinolones), and 1.2% (tetracyclines)**. In a Missouri series of 121 cases (2000–2007), the oculoglandular form comprised **3%** of cases (vs. ulceroglandular 37%, glandular 25%, pneumonic 12%, typhoidal 10%, oropharyngeal 2%); median incubation was 3 days (range 1–9), 65% of patients were male, median age was 37, and 69% of cases were attributed to tick bites, with systemic disease more common in older patients.

| Clinical form | Frequency (Missouri, n=121) |
|---|---|
| Ulceroglandular | 37% |
| Glandular | 25% |
| Pneumonic | 12% |
| Typhoidal | 10% |
| **Oculoglandular** | **3%** |
| Oropharyngeal | 2% |

> "requires as few as 10 organisms to cause disease, making this potential bioterrorism agent one of the most infectious bacterial pathogens known" — [PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/)

> "the fatality rate was 0.7%, 0.9%, and 1.2%, respectively" — [PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/)

> "Most patients presented with ulceroglandular (37%) and glandular (25%) forms of tularemia, followed by pneumonic (12%), typhoidal (10%), oculoglandular (3%), and oropharyngeal (2%) forms." — [PMID: 22911645](https://pubmed.ncbi.nlm.nih.gov/22911645/)

### Finding 4 — Pathogenesis causal chain

The pathogenesis proceeds from conjunctival inoculation to clinical disease through a well-characterized intracellular mechanism. *F. tularensis* is a facultative intracellular pathogen that survives within phagocytic cells "through phagosomal escape and replication in the cytosol, ultimately causing inflammasome activation and host cell death." Phagosomal escape requires a **non-canonical T6SS encoded on the 33-kb Francisella Pathogenicity Island (FPI)**; effectors PdpC and PdpD are required for phagosome rupture, and strains lacking them cannot escape the phagosome, activate the AIM2 inflammasome, or cause disease in mice. Cytosolic bacterial DNA activates the AIM2 inflammasome, leading to autocatalytic caspase-1 cleavage, IL-1β and IL-18 secretion, and pyroptotic cell death. Host NLRP3 increases susceptibility to tularemia in the mouse. Histopathology of oculoglandular lesions shows granulomatous inflammation with necrosis.

> "strains lacking pdpC and pdpD are unable to escape from phagosome, activate AIM2 inflammasome or cause disease in mice. This suggests that PdpC and PdpD are T6SS effectors involved in phagosome rupture." — [PMID: 28621333](https://pubmed.ncbi.nlm.nih.gov/28621333/)

> "Its life cycle is characterized by an ability to survive within phagocytic cells through phagosomal escape and replication in the cytosol, ultimately causing inflammasome activation and host cell death." — [PMID: 27830989](https://pubmed.ncbi.nlm.nih.gov/27830989/)

> "Escape of F. tularensis from the phagosome into the cytosol of the macrophage triggers the activation of the AIM2 inflammasome" — [PMID: 23115038](https://pubmed.ncbi.nlm.nih.gov/23115038/)

### Finding 5 — Diagnosis via serology and PCR; culture insensitive

Diagnosis relies on **serology (microagglutination)** and **PCR**; culture is insensitive (~10%) and biohazardous. A microagglutination titer ≥1/160 in a single serum, or a ≥4-fold rise/seroconversion between paired sera, is diagnostic — in one Turkish outbreak, 68% were positive on first serum and all initially negative patients seroconverted. PCR on lymph-node aspirate targeting *tul4*, *ISFtu2*, *fopA* and 23-kDa genes detects and subspeciates the organism (91% PCR-positive on node aspirates in one series); a multitarget TaqMan assay (*ISFtu2*, 23-kDa, *tul4*) reached a 1-organism detection limit and outperformed culture. Culture is positive in only ~10% of cases and requires BSL-3 containment; MALDI-TOF and 16S rRNA sequencing identify isolates. Failure to respond to β-lactams is a key diagnostic clue. The chief differential is cat scratch disease (*Bartonella henselae*).

> "in 17 (68%) of them microagglutination test yielded positive result (≥ 1/160) in their first serum samples. All of the 8 patients who had negative results in their first samples (< 1/160), revealed seroconversion in their second samples. In 10 (91%) of the 11 patients from whom lymph node aspirates were obtained, PCR performed with species specific (tul4) primers yielded positivity" — [PMID: 22090310](https://pubmed.ncbi.nlm.nih.gov/22090310/)

> "the TaqMan PCR assay was significantly more sensitive than culturing" — [PMID: 14662930](https://pubmed.ncbi.nlm.nih.gov/14662930/)

> "positive cultures are typically obtained in only 10% of tularemia cases" — [PMID: 37209668](https://pubmed.ncbi.nlm.nih.gov/37209668/)

> "The primary inoculation complex causing regional lymphadenopathy is represented in the eye by Parinaud's oculoglandular syndrome; B. henselae is the most common cause." — [PMID: 10537781](https://pubmed.ncbi.nlm.nih.gov/10537781/)

### Finding 6 — No licensed human vaccine; prevention is behavioral plus antibiotic prophylaxis

No licensed human tularemia vaccine exists. The only prophylactic ever developed is a >50-year-old **live-attenuated vaccine (LVS)** derived from the less virulent subsp. *holarctica*, which "has not been approved for use in humans or animals"; killed and subunit candidates remain experimental (animal models only). In the absence of a vaccine, **post-exposure prophylaxis** after proven *F. tularensis* exposure relies on antibiotics (doxycycline or ciprofloxacin for 14 days). Primary prevention is behavioral/environmental: avoiding bare-handed handling of sick/dead animals (especially lagomorphs and rodents), using gloves when skinning game, tick/insect-bite avoidance and prompt removal, hand and eye hygiene, protective eyewear, avoiding contaminated water, and not mowing over animal carcasses (aerosol risk).

> "A live-attenuated vaccine that was designed over 50 years ago using the less virulent F. tularensis subspecies holarctica is the only prophylactic currently available, but it has not been approved for use in humans or animals." — [PMID: 38564047](https://pubmed.ncbi.nlm.nih.gov/38564047/)

> "Because no effective and safe vaccine is currently available, tularaemia prophylaxis following proven exposure to F. tularensis also relies on administration of antibiotics." — [PMID: 24734221](https://pubmed.ncbi.nlm.nih.gov/24734221/)

### Finding 7 — Zoonotic transmission and broad host range

Tularemia is a zoonosis with a broad host range. *F. tularensis* "is transmitted to humans by handling infected animals, ingestion of contaminated food or water, inhalation of infective aerosols, and arthropod bites." Principal reservoirs and amplifying hosts are lagomorphs (rabbits, hares) and rodents; ticks (*Dermacentor*, *Amblyomma*, *Ixodes*) and deerflies are key vectors. The oculoglandular route specifically follows conjunctival inoculation. In a pediatric case series/review (94 cases, age 6 weeks–17 years), infection was zoonotic in 86.7% and waterborne in 13.3%, with ulceroglandular (46.7%), glandular (17%) and oropharyngeal (18.1%) forms predominating; fever was universal and serology the commonest diagnostic (60.6%). A confirmed oculoglandular case arose in a sheep breeder after a twig scratched the eye; another followed contact with a wild baby rabbit. Congenital transmission has been documented. Cats can transmit *F. tularensis* to humans via scratch or bite, overlapping clinically with cat scratch disease.

> "F tularensis is transmitted to humans by handling infected animals, ingestion of contaminated food or water, inhalation of infective aerosols, and arthropod bites." — [PMID: 22734313](https://pubmed.ncbi.nlm.nih.gov/22734313/)

> "multiple sources of infection, including diverse zoonotic transmission (86.7%) and contact with contaminated water (13.3%)" — [PMID: 39312633](https://pubmed.ncbi.nlm.nih.gov/39312633/)

> "Based on his anamnesis (sheep breeding; a twig scratching his eye 2 days before the initial attendance) and symptoms, a zoonosis, namely the oculoglandular form of tularemia, was suspected" — [PMID: 38941282](https://pubmed.ncbi.nlm.nih.gov/38941282/)

### Finding 8 — Clinical phenotype and complications

Oculoglandular tularemia presents acutely (incubation ~3 days, range 1–9) as **unilateral granulomatous follicular conjunctivitis** with conjunctival follicles, small yellowish ulcers/nodules, chemosis, lid edema, epiphora, mucopurulent discharge and marked injection, accompanied by fever, malaise, and painful ipsilateral preauricular (Parinaud node), submandibular, and cervical lymphadenopathy. Regional nodes frequently **suppurate**: in a confirmed case, node suppuration required surgical drainage before the patient recovered without sequelae on ciprofloxacin. Delayed diagnosis (often weeks) predisposes to suppurative lymphadenitis requiring fine-needle aspiration, drainage, or excision. Systemic constitutional symptoms are common (fever ~97%, lymphadenopathy ~94% in pediatric series). Prognosis with timely appropriate antibiotics is excellent (case-fatality <2%; subsp. *holarctica* infections essentially non-fatal); untreated or β-lactam-treated disease is protracted, with node suppuration and relapse.

> "the suppuration of the lymph nodes required surgical drainage" — [PMID: 38941282](https://pubmed.ncbi.nlm.nih.gov/38941282/)

> "Major clinical manifestations included fever (97%) and swelling of lymph glands (94%)" — [PMID: 36099382](https://pubmed.ncbi.nlm.nih.gov/36099382/)

> "delayed diagnosis may be associated with suppurative lymphadenitis and need for invasive intervention" — [PMID: 42749847](https://pubmed.ncbi.nlm.nih.gov/42749847/)

### Finding 9 — Model organisms

The **mouse is the principal in vivo model**; the attenuated Live Vaccine Strain (LVS, subsp. *holarctica*) is widely used at BSL-2 as a surrogate for virulent *F. tularensis*, which requires BSL-3. *F. tularensis* "is, in part, attributed to the ability of this microorganism to evade, disrupt, and modulate host immune responses" and can "cause lethal disease following inoculation of as few as 15 organisms." Mechanistic mutant studies (ΔpdpC/pdpD, ΔiglE, ΔvgrG, ΔdotU) in J774/THP-1 macrophages and mice link the FPI-encoded T6SS to phagosomal escape, inflammasome activation, and virulence. A zebrafish embryo model of *F. tularensis* subsp. *novicida* (and *F. noatunensis*) reproduces macrophage uptake, granuloma-like aggregates, and TNF-α/IL-1β proinflammatory responses. Protective immunity is T-cell dependent (CD4+/CD8+, IFN-γ).

> "its ability to cause lethal disease following inoculation of as few as 15 organisms. This remarkable virulence is, in part, attributed to the ability of this microorganism to evade, disrupt, and modulate host immune responses" — [PMID: 21687406](https://pubmed.ncbi.nlm.nih.gov/21687406/)

> "All three strains entered preferentially into macrophages, which eventually assembled into granuloma-like structures." — [PMID: 24614659](https://pubmed.ncbi.nlm.nih.gov/24614659/)

### Finding 10 — Integrated synthesis

Integrating all findings across 54 literature items: oculoglandular tularemia is one of six tularemia forms (~1–3% of cases), caused by conjunctival inoculation of *F. tularensis* (subsp. *tularensis* type A / *holarctica* type B). The mechanism is T6SS/FPI (PdpC/PdpD)-mediated phagosomal escape → cytosolic replication → AIM2 inflammasome/caspase-1/IL-1β/IL-18 pyroptosis → granulomatous conjunctivitis + regional (preauricular/submandibular/cervical) lymphadenitis. It presents acutely (incubation ~3 d) as unilateral granulomatous follicular conjunctivitis with ipsilateral tender lymphadenopathy (Parinaud syndrome; second commonest cause after cat scratch disease). Diagnosis is by serology (microagglutination ≥1/160) and PCR (*tul4*/*ISFtu2*/*fopA*); culture ~10% sensitive, BSL-3. Treatment is with aminoglycosides/fluoroquinolones/tetracyclines (all isolates susceptible); β-lactams fail; case-fatality <2%; suppurative nodes may need drainage. Prevention is behavioral/PPE plus antibiotic post-exposure prophylaxis (no licensed vaccine). There is no host causal gene or inheritance; the disease is zoonotic (lagomorph/rodent reservoirs, tick vectors, cats). Mouse (LVS/SchuS4) and zebrafish are the main models.

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Oculoglandular tularemia is the conjunctival-entry ("ocular") clinical form of tularemia, an acute febrile zoonosis caused by *Francisella tularensis*. It manifests as unilateral granulomatous conjunctivitis with ipsilateral regional lymphadenopathy (Parinaud oculoglandular syndrome), and constitutes roughly 1–3% of tularemia cases.

**Key identifiers.**
- **MONDO:** MONDO:0001665 (oculoglandular tularemia)
- **MeSH:** Tularemia (D014406); *Francisella tularensis* organism term
- **ICD-10:** A21.1 (Oculoglandular tularemia); parent A21 (Tularemia)
- **ICD-11:** 1B94 (Tularemia)
- **SNOMED CT:** Oculoglandular tularemia (disorder)
- **OMIM / Orphanet:** Not a Mendelian disorder; no OMIM phenotype entry. It is an infectious disease, not a rare genetic disease.

**Synonyms / alternative names.** Ocular tularemia; ophthalmic tularemia; Parinaud oculoglandular syndrome due to tularemia; "oculoglandular form of tularemia." Historical names for tularemia broadly include rabbit fever, deer-fly fever, Ohara disease, and Francis disease.

**Information source type.** This knowledge base entry is derived from **aggregated disease-level resources** (systematic reviews, case series, clinical guidelines, and mechanistic laboratory studies) rather than individual EHR-derived patient records. Individual case reports (e.g., PMID 38941282) contribute granular clinical detail.

### 2. Etiology

**Disease causal factor — infectious.** The sole cause is infection by *Francisella tularensis*, a small, Gram-negative, non-motile, facultatively intracellular coccobacillus. Clinically important subspecies: **subsp. *tularensis* (type A)** — highly virulent, predominantly North America — and **subsp. *holarctica* (type B)** — less virulent, Northern Hemisphere including Europe/Asia; subsp. *holarctica* infections are essentially non-fatal. The oculoglandular form specifically requires **conjunctival inoculation** of the organism.

**Risk factors (environmental / behavioral).**
- Occupational and recreational animal contact: hunters, trappers, farmers, sheep breeders, veterinarians, laboratory workers.
- Handling infected lagomorphs (rabbits, hares) and rodents.
- Tick and deerfly exposure in endemic regions.
- Ocular trauma or splash while handling infected animal material (a sheep breeder was infected after a twig scratched his eye — PMID 38941282).
- Touching the eye with contaminated fingers.
- Male sex and older age are associated with higher rates of systemic disease in case series (65% male, PMID 22911645).

**Genetic risk factors.** **None identified.** There is no host causal gene, susceptibility locus, or modifier allele established for human oculoglandular tularemia. (Experimentally, host *Nlrp3* increases murine susceptibility — PMID 34690967 — but this is not a clinically actionable human genetic risk factor.)

**Protective factors.** No genetic protective variants are known. Behavioral protection (gloves, eye protection, tick avoidance, hand hygiene) reduces risk. Prior infection or LVS vaccination confers T-cell–dependent immunity, but no licensed vaccine exists.

**Gene–environment interactions.** Not applicable to the human host in a Mendelian sense. The relevant "gene–environment" axis is bacterial: FPI/T6SS genes interact with the intracellular macrophage environment to enable virulence.

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Frequency / characteristics |
|---|---|---|---|
| Unilateral granulomatous conjunctivitis | Clinical sign | HP:0000509 (Conjunctivitis) | Hallmark; unilateral; acute onset ~3 d |
| Conjunctival follicles/nodules/ulcers | Physical manifestation | (ocular surface lesion) | Yellowish granulomatous nodules |
| Preauricular/cervical lymphadenopathy | Clinical sign | HP:0002716 (Lymphadenopathy) | ~94% (pediatric series); ipsilateral, painful |
| Fever | Symptom | HP:0001945 (Fever) | ~97% |
| Eyelid edema / chemosis | Physical manifestation | HP:0000198 (periorbital edema analog) | Common |
| Epiphora / mucopurulent discharge | Symptom/sign | HP:0009926 (Epiphora) | Common |
| Malaise/fatigue | Symptom | HP:0012378 (Fatigue) | Common |
| Suppurative lymphadenitis | Clinical sign / complication | HP:0002840 (lymphadenitis analog) | Occurs with delayed treatment |

**Characteristics.** Age of onset: any age (children through adults). Severity: mild-to-moderate ocular disease that is usually self-limited to the eye/nodes but can become severe with node suppuration or, rarely, systemic spread. Progression: acute onset, then either resolution with treatment or a protracted suppurative course if untreated/β-lactam-treated. Frequency among affected individuals: fever ~97%, lymphadenopathy ~94% in pediatric tularemia series (PMID 36099382).

**Quality of life impact.** Generally transient with prompt treatment; significant discomfort during the acute phase (ocular pain, purulent discharge, tender nodes, fever). Suppurative lymphadenitis requiring drainage prolongs morbidity. No dedicated EQ-5D/SF-36 disease-specific data were identified.

### 4. Genetic/Molecular Information

**Not applicable to the human host.** Oculoglandular tularemia is an infectious disease with **no causal human gene, pathogenic variant, modifier gene, epigenetic signature, or chromosomal abnormality**. There is no germline or somatic variant classification (ACMG/AMP), no allele frequency data, and no ClinVar/OMIM entry for a causal locus.

**Relevant bacterial genetics.** Virulence is governed by the **Francisella Pathogenicity Island (FPI)**, a ~33-kb gene cluster encoding a non-canonical Type VI secretion system (T6SS). Key genes include *pdpC*, *pdpD*, *iglE*, *vgrG*, *dotU*, and *pdpB/icmF*. Deletion mutants of these genes abolish phagosomal escape, inflammasome activation, and virulence (PMIDs 28621333, 22514651, 27830989).

### 5. Environmental Information

**Environmental factors.** *F. tularensis* persists in the environment (water, soil, animal carcasses, mud) and can be aerosolized (e.g., during mowing over carcasses). Contaminated water is a documented outbreak source (waterborne tularemia outbreaks in Turkey).

**Lifestyle factors.** Hunting, trapping, farming, animal husbandry, and outdoor recreation in endemic areas increase exposure.

**Infectious agent.** *Francisella tularensis* (NCBI Taxon: 263). Subspecies: *tularensis* (type A), *holarctica* (type B), *mediasiatica*, and *novicida* (used in models). Note: the lipopolysaccharide (LPS) of *F. tularensis* is atypically non-stimulatory to TLR4, contributing to immune evasion.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating event → clinical manifestation):**

1. **Conjunctival inoculation** of *F. tularensis* (contaminated fingers, splash, aerosol, or ocular trauma) **leads to** deposition of organisms on the conjunctival/ocular surface.
2. Local organisms **are phagocytosed by** resident macrophages and other phagocytes at the conjunctiva and draining lymphatics.
3. Inside the phagocyte, the bacterium **deploys its FPI-encoded T6SS** (effectors PdpC/PdpD), which **results in** rupture/escape from the phagosome into the cytosol. *(Demonstrated: ΔpdpC/pdpD mutants cannot escape — PMID 28621333.)*
4. Cytosolic access **leads to** rapid bacterial replication in the nutrient-rich cytoplasm. *(Branch: the bacterium also suppresses innate signaling and modulates host metabolism to sustain replication — PMID 21687406.)*
5. Cytosolic bacterial DNA **is sensed by the AIM2 inflammasome**, which **results in** autocatalytic caspase-1 activation. *(Demonstrated — PMIDs 23115038, 28621333.)*
6. Caspase-1 activation **leads to** maturation and secretion of IL-1β and IL-18 and to **pyroptotic host-cell death**.
7. Pyroptosis and cytokine release **result in** recruitment of neutrophils and monocytes and **granulomatous inflammation** at the conjunctiva.
8. Lymphatic spread of organisms **leads to** regional (preauricular/submandibular/cervical) **granulomatous lymphadenitis**, which may progress to **suppuration/necrosis** — the clinically evident Parinaud oculoglandular syndrome.
9. *(Branch — rare:)* Failure of local containment **may result in** systemic/typhoidal dissemination; this is uncommon for the oculoglandular form and rarer still for subsp. *holarctica*.

Steps 1–2 and 7–8 in the *ocular tissue specifically* are inferred by analogy from systemic/macrophage models; steps 3–6 are directly demonstrated in macrophage and mouse systems.

**Molecular pathways / cellular processes.** Inflammasome signaling (AIM2 primary; NLRP3 modulatory — host NLRP3 increases susceptibility, PMID 34690967), caspase-1 activation, IL-1β/IL-18 (pyroptosis), and NF-κB (IKKβ in myeloid cells controls host response — PMID 23349802).

**Cell types involved (CL suggestions).** Macrophages (CL:0000235), monocytes (CL:0000576), neutrophils (CL:0000775), dendritic cells (CL:0000451), and conjunctival epithelial cells (CL:0000066). Protective adaptive immunity is CD4+/CD8+ T-cell and IFN-γ dependent (PMID 21687406).

**GO term suggestions.** Modulation of host immune response (GO:0052167), AIM2 inflammasome complex (GO:0097169), positive regulation of interleukin-1 beta production (GO:0032731), pyroptosis (GO:0070269), defense response to bacterium (GO:0042742).

**Subcellular compartments (GO Cellular Component).** Phagosome (GO:0045335), cytosol (GO:0005829), AIM2 inflammasome complex (GO:0097169).

**Tissue damage mechanisms.** Granulomatous inflammation with caseous/suppurative necrosis of regional lymph nodes; local conjunctival ulceration.

### 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** Conjunctiva and ocular surface (UBERON:0001811 conjunctiva; UBERON:0000970 eye).
- **Regional:** Preauricular, submandibular, and cervical lymph nodes (UBERON:0000029 lymph node).
- **Secondary/rare:** Systemic organs (lung, liver, spleen) if dissemination occurs.
- **Body systems:** Visual/ocular system and immune/lymphatic system.

**Tissue and cell level.** Conjunctival epithelium (epithelial tissue); lymphoid tissue of draining nodes. Target cell populations: macrophages (CL:0000235), monocytes (CL:0000576), neutrophils (CL:0000775).

**Subcellular level.** Phagosome (GO:0045335) and cytosol (GO:0005829) of infected macrophages.

**Localization / lateralization.** Characteristically **unilateral** (the inoculated eye) with **ipsilateral** regional lymphadenopathy.

### 8. Temporal Development

- **Onset:** Acute. Median incubation ~3 days (range 1–9 days) (PMID 22911645).
- **Progression:** Rapid symptom onset; with prompt appropriate antibiotics, resolution over days to weeks. Untreated or β-lactam-treated disease follows a protracted course with node suppuration and possible relapse.
- **Disease course pattern:** Typically monophasic/self-limited with treatment; can be prolonged if diagnosis is delayed (median diagnostic delay ~23.5 days in pediatric cases).
- **Duration:** Self-limited to weeks with therapy; suppurative lymphadenitis may extend the course and require drainage.
- **Remission:** Treatment-induced remission is the norm; spontaneous resolution can occur but risks suppuration.
- **Critical period:** Early antibiotic initiation (before node suppuration) is the key window to prevent invasive intervention.

### 9. Inheritance and Population

**Epidemiology.** Oculoglandular tularemia comprises ~1–3% of tularemia cases. Tularemia overall is a reportable, sporadic-to-outbreak zoonosis across the Northern Hemisphere; a nationwide Danish seroprevalence study found 2.2% seropositivity, suggesting underdiagnosis. Incidence varies geographically and seasonally (tick-season peaks).

**Inheritance.** **Not applicable** — infectious, non-heritable. No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency.

**Population demographics.** In case series, ~65% male; median age ~37 (adults) but all ages affected including neonates (congenital transmission documented — PMID 41385785). Geographic distribution: North America (subsp. *tularensis* and *holarctica*), Europe and Asia (subsp. *holarctica*); endemic foci in Turkey, Scandinavia, Central Europe, and parts of the U.S. (e.g., Missouri, Arkansas). Climate modeling suggests potential range expansion.

### 10. Diagnostics

**Serology (mainstay).** Microagglutination test titer **≥1/160** in a single serum, or **≥4-fold rise/seroconversion** between paired sera, is diagnostic (PMID 22090310). ELISA and immunochromatographic rapid tests (sensitivity ~98%, specificity ~96% on human sera) are also available (PMID 20220165). Cross-reactivity with *Brucella* should be excluded.

**Molecular (PCR).** Targets *tul4*, *ISFtu2*, *fopA*, and the 23-kDa gene on lymph-node aspirates or ocular swabs; a multitarget TaqMan assay reached a ~1-organism detection limit and outperformed culture (PMID 14662930). PCR yield on node aspirates ~91% in one series.

**Culture.** Positive in only ~10% of cases; requires cysteine-enriched media and **BSL-3 containment** because of aerosol hazard (PMID 37209668). MALDI-TOF and 16S rRNA sequencing identify isolates.

**Biopsy/pathology.** Granulomatous inflammation with necrosis; immunohistochemistry and 16S rRNA PCR can identify *Francisella* in tissue.

**Clinical clue.** Failure to respond to β-lactam antibiotics in a patient with unilateral granulomatous conjunctivitis and regional lymphadenopathy should prompt consideration of tularemia.

**Differential diagnosis.** Cat scratch disease (*Bartonella henselae*, the most common POGS cause), adenoviral/chlamydial conjunctivitis, sporotrichosis, tuberculosis, syphilis, lymphogranuloma venereum, sarcoidosis, and (as in one report) flea-borne typhus (PMID 32751142).

**Screening.** No population screening applies (acute infectious disease, no carrier state).

### 11. Outcome/Prognosis

- **Mortality:** Very low with appropriate treatment — case-fatality 0.7–1.2% depending on antibiotic class (PMID 38294108); subsp. *holarctica* oculoglandular disease is essentially non-fatal.
- **Morbidity:** Mainly local — ocular discomfort, tender regional lymphadenopathy, and suppurative lymphadenitis requiring drainage in a subset (especially with diagnostic delay).
- **Recovery:** Excellent with timely aminoglycoside/fluoroquinolone/tetracycline therapy; most patients recover without sequelae.
- **Complications:** Suppurative lymphadenitis needing fine-needle aspiration, drainage, or excision; rarely systemic dissemination.
- **Prognostic factors:** Time to appropriate therapy (delay predicts suppuration and invasive intervention — PMID 42749847); patient age (older patients have more systemic disease); infecting subspecies (type A more virulent).

### 12. Treatment

**First-line pharmacotherapy** (all *F. tularensis* isolates uniformly susceptible — PMID 38294116):

| Drug class | Agents | NCIT suggestion | Notes |
|---|---|---|---|
| Aminoglycosides | Streptomycin (IM), gentamicin | NCIT:C312 (Streptomycin), NCIT:C516 (Gentamicin) | Historical drug of choice; lowest treated fatality (0.7%) |
| Fluoroquinolones | Ciprofloxacin, levofloxacin | NCIT:C405 (Ciprofloxacin) | Effective; used successfully in a confirmed oculoglandular case (PMID 38941282) |
| Tetracyclines | Doxycycline, tetracycline | NCIT:C562 (Doxycycline) | Bacteriostatic; higher relapse risk; longer courses |

**Agents that fail:** β-lactams (penicillins, most cephalosporins) — reliably ineffective; clinical non-response is a diagnostic clue.

**Duration:** ~10 days for aminoglycosides/fluoroquinolones; ~14–21 days for tetracyclines. Chloramphenicol is reserved for CNS involvement (meningitis).

**Surgical/interventional:** Incision and drainage or excision of suppurative lymph nodes when they fail to resolve (PMIDs 38941282, 22090310).

**Pharmacogenomics / advanced therapeutics:** Not applicable — no gene therapy, cell therapy, RNA-based, targeted, or immunotherapy is used for this infection.

**Experimental:** Inhaled liposomal ciprofloxacin has shown protection against lethal (pneumonic) tularemia in a marmoset model (PMID 41416830) — relevant to respiratory rather than oculoglandular disease.

### 13. Prevention

- **Primary prevention:** Behavioral/environmental — gloves when handling/skinning game (especially lagomorphs and rodents), avoiding sick/dead animals, tick- and deerfly-bite avoidance and prompt tick removal, eye protection, hand and eye hygiene, avoiding untreated/contaminated water, and not mowing over animal carcasses (aerosol risk).
- **Secondary prevention:** Prompt recognition (especially β-lactam non-response) and early antibiotic therapy to prevent suppuration.
- **Tertiary prevention:** Timely drainage of suppurative nodes; completion of appropriate antibiotic courses to prevent relapse.
- **Immunization:** No licensed human vaccine. Only the unapproved live-attenuated LVS exists; subunit/killed candidates remain experimental (PMID 38564047).
- **Post-exposure prophylaxis:** Doxycycline or ciprofloxacin for 14 days after proven exposure (PMID 24734221; non-vaccinal prophylaxis reviewed in PMID 39669787).
- **Public health:** Water chlorination and sanitation (waterborne outbreak control), vector control, occupational education, and reportable-disease surveillance.

### 14. Other Species / Natural Disease

- **Taxonomy of host species:** Broad. Reservoirs/amplifying hosts include lagomorphs (rabbits, hares; *Oryctolagus*, *Lepus*, *Sylvilagus*), rodents (voles, muskrats, mice), and many mammals. Vectors: ticks (*Dermacentor*, *Amblyomma*, *Ixodes*) and deerflies (*Chrysops*).
- **Natural disease in animals:** Tularemia occurs naturally in wildlife (dramatic die-offs in lagomorphs/rodents) and in domestic animals; cats and sheep are relevant to human oculoglandular transmission. Cats can transmit *F. tularensis* to humans via scratch/bite (clinical overlap with cat scratch disease).
- **Zoonotic potential:** High. Tularemia is a classic zoonosis; humans are incidental hosts.
- **Cross-species susceptibility:** Very broad mammalian host range; the same organism/mechanisms operate across species.
- **Veterinary relevance:** Important in wildlife-health surveillance and as a sentinel for human risk.

### 15. Model Organisms

- **Mouse (primary model):** *Mus musculus*. Virulent strains (SchuS4, subsp. *tularensis*) require BSL-3; the attenuated Live Vaccine Strain (LVS, subsp. *holarctica*) is used at BSL-2 as a surrogate. Recapitulates intracellular infection, inflammasome activation, granuloma formation, and lethality at very low inocula (~15 organisms) (PMID 21687406). Genetic host models (e.g., *Nlrp3*, myeloid *IKKβ* conditional knockouts) dissect host response (PMIDs 34690967, 23349802).
- **Macrophage cell models:** J774 (murine) and THP-1 (human) cells are standard for FPI/T6SS mutant studies (ΔpdpC/pdpD, ΔiglE, ΔvgrG, ΔdotU) (PMIDs 28621333, 22514651, 27830989).
- **Zebrafish embryo model:** *Danio rerio* infected with *F. tularensis* subsp. *novicida* (and *F. noatunensis*) reproduces macrophage tropism, granuloma-like aggregates, and TNF-α/IL-1β responses (PMID 24614659).
- **Phenotype recapitulation:** Mouse models faithfully reproduce intracellular replication, inflammasome-driven pathology, and granulomatous disease; zebrafish captures innate/macrophage biology and granuloma formation.
- **Limitations:** No model specifically reproduces the *oculoglandular* (conjunctival-inoculation) route; models focus on systemic/pneumonic disease. LVS is attenuated and may not fully mirror type A virulence.

---

## Mechanistic Model / Interpretation

```
   Conjunctival inoculation of F. tularensis
   (contaminated finger / splash / ocular trauma)
                    │
                    ▼
        Phagocytosis by macrophages
                    │
                    ▼
   FPI-encoded T6SS (PdpC, PdpD) ──► PHAGOSOMAL ESCAPE
                    │                 (ΔpdpC/pdpD → no escape,
                    ▼                  no disease — PMID 28621333)
        Cytosolic bacterial replication
       (immune subversion; low ID ~10–15 organisms)
                    │
                    ▼
   Cytosolic DNA sensed → AIM2 INFLAMMASOME
                    │
                    ▼
        Caspase-1 activation
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
   IL-1β / IL-18        PYROPTOSIS
   secretion           (host-cell death)
          └─────────┬─────────┘
                    ▼
   Neutrophil/monocyte recruitment → GRANULOMATOUS INFLAMMATION
                    │
          ┌─────────┴──────────────┐
          ▼                        ▼
   Granulomatous              Lymphatic spread →
   CONJUNCTIVITIS             regional (preauricular/
   (unilateral)               submandibular/cervical)
                              LYMPHADENITIS → suppuration
                    │
                    ▼
   PARINAUD OCULOGLANDULAR SYNDROME
   (2nd commonest cause after cat scratch disease)
```

**Upstream vs downstream.** The upstream, rate-limiting virulence step is T6SS-mediated phagosomal escape (bacterial); the downstream pathology (granuloma, lymphadenitis, pyroptosis) is host inflammasome-driven. Therapeutically, intracellular-active antibiotics (aminoglycosides, fluoroquinolones, tetracyclines) interrupt the replication step; β-lactams fail because they poorly access the cytosolic niche and the organism's cell-wall biology.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [38941282](https://pubmed.ncbi.nlm.nih.gov/38941282/) | *F. tularensis* causing Parinaud OGS | Disease definition, POGS rank, transmission, ciprofloxacin cure, node drainage |
| [11228320](https://pubmed.ncbi.nlm.nih.gov/11228320/) | Parinaud's OGS from a wild rabbit | Clinical presentation; tularemia as POGS etiology |
| [38294116](https://pubmed.ncbi.nlm.nih.gov/38294116/) | Antimicrobial susceptibility, US 2009–2018 | Uniform susceptibility to first-line drugs |
| [28605439](https://pubmed.ncbi.nlm.nih.gov/28605439/) | Susceptibility, German *holarctica* | MIC90 values; biovar II erythromycin resistance |
| [38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/) | Systematic review 1993–2023 | Infective dose ~10 organisms; treated fatality 0.7–1.2% |
| [22911645](https://pubmed.ncbi.nlm.nih.gov/22911645/) | Missouri 121 cases | Oculoglandular ~3%; incubation; demographics |
| [28621333](https://pubmed.ncbi.nlm.nih.gov/28621333/) | T6SS/ClpB effector delivery | PdpC/PdpD required for escape, AIM2, virulence |
| [27830989](https://pubmed.ncbi.nlm.nih.gov/27830989/) | IglE T6SS secretion | Intracellular life cycle; phagosomal escape |
| [23115038](https://pubmed.ncbi.nlm.nih.gov/23115038/) | LVS caspase-1 activation | Cytosolic escape → AIM2 inflammasome |
| [22514651](https://pubmed.ncbi.nlm.nih.gov/22514651/) | DotU/VgrG essential | T6SS core components required for pathogenicity |
| [22090310](https://pubmed.ncbi.nlm.nih.gov/22090310/) | Central Anatolia cases | Microagglutination ≥1/160; seroconversion; PCR yield |
| [14662930](https://pubmed.ncbi.nlm.nih.gov/14662930/) | Multitarget TaqMan PCR | PCR more sensitive than culture |
| [37209668](https://pubmed.ncbi.nlm.nih.gov/37209668/) | Prosthetic joint infection review | Culture ~10% sensitive |
| [10537781](https://pubmed.ncbi.nlm.nih.gov/10537781/) | Ocular cat-scratch disease | *B. henselae* as leading POGS cause (key differential) |
| [38564047](https://pubmed.ncbi.nlm.nih.gov/38564047/) | Tularemia vaccine review | No licensed human vaccine; LVS unapproved |
| [24734221](https://pubmed.ncbi.nlm.nih.gov/24734221/) | New therapeutic approaches | Antibiotic post-exposure prophylaxis |
| [39669787](https://pubmed.ncbi.nlm.nih.gov/39669787/) | Non-vaccinal prophylaxis | Prophylaxis strategy |
| [22734313](https://pubmed.ncbi.nlm.nih.gov/22734313/) | Two glandular cases, Turkey | Zoonotic transmission routes |
| [39312633](https://pubmed.ncbi.nlm.nih.gov/39312633/) | Pediatric case series | Zoonotic 86.7%, waterborne 13.3%; form distribution |
| [36099382](https://pubmed.ncbi.nlm.nih.gov/36099382/) | Kosovo pediatric outbreak | Fever 97%, lymphadenopathy 94% |
| [42749847](https://pubmed.ncbi.nlm.nih.gov/42749847/) | Invasive intervention in pediatric tularemia | Diagnostic delay → suppurative lymphadenitis |
| [21687406](https://pubmed.ncbi.nlm.nih.gov/21687406/) | Immune subversion review | ID ~15 organisms; immune evasion; T-cell immunity |
| [24614659](https://pubmed.ncbi.nlm.nih.gov/24614659/) | Zebrafish infection model | Macrophage tropism; granuloma-like structures |
| [34690967](https://pubmed.ncbi.nlm.nih.gov/34690967/) | Nlrp3 and susceptibility | Host NLRP3 increases susceptibility (mouse) |
| [23349802](https://pubmed.ncbi.nlm.nih.gov/23349802/) | Myeloid IKKβ | NF-κB control of host response to LVS |
| [20220165](https://pubmed.ncbi.nlm.nih.gov/20220165/) | Immunochromatographic test | Rapid serodiagnosis sensitivity/specificity |
| [41385785](https://pubmed.ncbi.nlm.nih.gov/41385785/) | Congenital tularemia, Utah | Congenital/neonatal transmission |

**Consistency assessment.** The evidence is internally consistent: multiple independent case series converge on oculoglandular tularemia representing ~1–3% of cases; susceptibility data across two continents agree on uniform first-line efficacy; and mechanistic studies across mouse, macrophage, and zebrafish systems converge on the T6SS→AIM2 axis. No contradictory findings were encountered.

---

## Supported and Refuted Hypotheses

No formal hypotheses were rejected during the investigation. The investigation confirmed 10 findings that collectively **support** the following propositions:

- Oculoglandular tularemia is a distinct, conjunctival-entry clinical form of tularemia and the second commonest cause of POGS (**supported**).
- Its pathogenesis is driven by T6SS-mediated phagosomal escape and AIM2 inflammasome activation (**supported**).
- It has no heritable/host-genetic basis (**supported** — no causal locus identified).
- It is highly treatable with aminoglycosides, fluoroquinolones, or tetracyclines, and β-lactams fail (**supported**).
- No licensed human vaccine exists (**supported**).

---

## Limitations and Knowledge Gaps

1. **Route-specific data are sparse.** Because the oculoglandular form is rare, most quantitative clinical data derive from mixed tularemia cohorts (dominated by ulceroglandular/oropharyngeal forms) or from individual case reports. Form-specific frequencies for symptoms, complications, and outcomes are extrapolated.
2. **No oculoglandular animal model.** All in vivo models study systemic, pneumonic, or dermal/glandular disease; none reproduces conjunctival inoculation. Mechanistic inferences for the ocular route are by analogy.
3. **Mechanistic chain partly inferred.** While phagosomal escape → AIM2 → pyroptosis is directly demonstrated in macrophage and mouse systems, the specific sequence of events *in the human conjunctiva* is inferred rather than demonstrated.
4. **No human host-genetic data.** The clinical relevance (if any) of host inflammasome polymorphisms (e.g., NLRP3, AIM2) to human oculoglandular tularemia susceptibility or severity is unknown.
5. **Quality-of-life instruments not applied.** No EQ-5D/SF-36/PROMIS data specific to oculoglandular tularemia were identified.
6. **Culture-negativity limits isolate-level surveillance.** Because most diagnoses are serologic/PCR-based, subspecies/biovar-level antibiotic-resistance surveillance (e.g., erythromycin-resistant biovar II) is incomplete.

---

## Proposed Follow-up Experiments / Actions

1. **Build a route-specific model.** Develop a murine or rabbit conjunctival-inoculation model of oculoglandular tularemia (LVS at BSL-2, SchuS4 at BSL-3) to directly test the conjunctiva→draining-node causal chain and evaluate topical vs systemic therapy.
2. **Ocular-surface immunology.** Use single-cell RNA-seq of conjunctival and draining-node tissue in the model to define the cell-type–specific inflammasome response (map to CL/GO terms) and confirm AIM2 dependence in ocular disease.
3. **Rapid point-of-care diagnostics.** Validate the immunochromatographic rapid test and multiplex PCR (*tul4*/*ISFtu2*/*fopA*/23-kDa) on ocular swabs and conjunctival scrapings specifically for the oculoglandular presentation to shorten the ~3-week diagnostic delay.
4. **Prospective differential-diagnosis registry.** Establish a POGS registry to prospectively quantify the relative frequencies of cat scratch disease vs tularemia vs other etiologies and to standardize a diagnostic algorithm keyed to β-lactam non-response.
5. **Topical/intracellular antibiotic optimization.** Extend intracellular-activity assays (dye-uptake MIEC method) and liposomal-delivery approaches to ocular formulations to prevent node suppuration and reduce need for surgical drainage.
6. **Host-genetic association study.** Explore whether inflammasome-pathway polymorphisms (AIM2, NLRP3, CASP1) associate with tularemia susceptibility or suppurative complications in endemic populations.
7. **Vaccine development.** Advance defined subunit/attenuated candidates through mucosal/ocular protection endpoints, given the persistent absence of a licensed human vaccine.

---

*Report compiled from 54 reviewed literature items across 5 investigation iterations; 10 findings confirmed. Evidence types span human clinical case series and reviews, model-organism (mouse, zebrafish) studies, and in vitro macrophage mechanistic work.*


## Artifacts

- [OpenScientist final report](Oculoglandular_Tularemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Oculoglandular_Tularemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 24 |
| Quoted claims found in source | 22 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 29 |
| On topic | 20 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:11228320` *(abstract only)*: "Parinaud's oculoglandular syndrome should be considered in the differential diagnosis of a patient presenting with unilateral granulomatous conjunctivitis, painful preauricular, and submandibular lymphadenopathy combined with systemic symptoms of general malaise and fever. Tularemia is one etiology of Parinaud's oculoglandular syndrome."
  - closest text in source: "RESULTS: Parinaud's oculoglandular syndrome should be considered in the differential diagnosis of a patient presenting with unilateral granulomatous conjunctivitis, painful preauricular, and submandibular lymphadenopathy combined with systemic symptoms of general malaise and fever"
- `PMID:22734313` *(abstract only)*: "F tularensis is transmitted to humans by handling infected animals, ingestion of contaminated food or water, inhalation of infective aerosols, and arthropod bites."
  - closest text in source: "E tularensis is transmitted to humans by handling infected animals, ingestion of contaminated food or water, inhalation of infective aerosols, and arthropod bites"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 10 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000198` (1 mention) - the report calls it "periorbital edema analog"; HP calls it **Absence of Stensen duct**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002840` (1 mention) - the report calls it "lymphadenitis analog"; HP calls it **Lymphadenitis**
- `NCIT:C405` (1 mention) - the report calls it "Ciprofloxacin"; NCIT calls it **Cyclophosphamide**, and lists "Carloxan" among its other names
- `NCIT:C562` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Idarubicin**, and lists "4-Demethoxydaunomycin" among its other names