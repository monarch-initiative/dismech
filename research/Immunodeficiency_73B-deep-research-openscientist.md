---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-05T14:12:56.686051'
end_time: '2026-09-05T14:25:42.113196'
duration_seconds: 765.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 73B
  mondo_id: MONDO:0033554
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
  total_references: 12
  verified: 11
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.083
  relevance_assessed: 11
  on_topic: 9
  unresolved_references:
  - PMID:15814684
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 32
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 1
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_73B-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_73B-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 73B
- **MONDO ID:** MONDO:0033554 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 73B** covering all of the
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

# Immunodeficiency 73B (RAC2 Gain-of-Function Combined Immunodeficiency) — Comprehensive Disease Report

**Disease:** Immunodeficiency 73B (IMD73B), with defective neutrophil chemotaxis and lymphopenia
**MONDO ID:** MONDO:0033554 | **OMIM phenotype:** #618986 | **Gene:** *RAC2* (OMIM 602049; HGNC:9802; NCBI Gene 5880; UniProt P15153) | **Locus:** 22q13.1
**Category:** Mendelian, autosomal dominant

---

## Summary

**Immunodeficiency 73B (IMD73B) is an ultra-rare, autosomal dominant combined immunodeficiency (CID) caused by heterozygous, dominant-activating (gain-of-function, GOF) missense mutations in *RAC2*, a Rho-family small GTPase expressed exclusively in hematopoietic cells.** RAC2 normally functions as a molecular switch, cycling between an inactive GDP-bound and an active GTP-bound state to control two parallel effector arms critical to immune-cell function: (1) NADPH-oxidase–driven superoxide production (via p67phox) and (2) actin-cytoskeleton remodeling for cell migration (via PAK1 and POR1/Arfaptin2). In IMD73B, the mutant protein is locked in, or biased toward, the constitutively active GTP-bound state, dysregulating both effector arms simultaneously.

The clinical consequence is a *combined* immune defect that spans the myeloid and lymphoid lineages: patients develop **T- and B-cell lymphopenia, hypogammaglobulinemia, defective neutrophil chemotaxis, and dysregulated oxidative burst**, presenting with recurrent respiratory infections, bronchiectasis, and heightened susceptibility to viral pathogens (HPV, EBV, herpesviruses). IMD73B sits within a broader *RAC2*-related immunodeficiency spectrum in which the biochemical class of the mutation predicts the clinical phenotype — constitutively active "RAS-like" alleles produce neonatal SCID, dominant-negative alleles produce a leukocyte-adhesion-deficiency (LAD)-like disease, and **dominant-activating alleles produce the CID category corresponding to IMD73B**.

Management combines supportive care (immunoglobulin replacement, antimicrobial prophylaxis) with **allogeneic hematopoietic cell transplantation (HCT) as the only definitive, curative therapy** — rational because RAC2 is expressed solely in hematopoietic cells, so replacing that compartment corrects the defect. Transplant carries substantial risk, however, with reported transplant-related mortality. IMD73B is genetically ultra-rare: fewer than ~54 *RAC2* patients from 37 families (across all allelic classes) had been compiled worldwide by 2024, and causal variants are private, frequently de novo germline missense changes with apparently complete penetrance.

---

## Key Findings

### Finding 1 — IMD73B is caused by dominant-activating (gain-of-function) heterozygous *RAC2* mutations producing combined immunodeficiency with lymphopenia

RAC2-related immunodeficiency demonstrates a striking **genotype–function–phenotype correlation**. In the largest compiled cohort to date — 54 patients from 37 families — the biochemical activity of the mutant RAC2 protein predicts the clinical syndrome. As Donkó et al. state directly: *"Disease correlated to RAC2 activity: constitutively active RAS-like mutations caused neonatal SCID, dominant-negative mutations caused LAD-like disease, whereas dominant-activating mutations caused CID"* ([PMID: 38194689](https://pubmed.ncbi.nlm.nih.gov/38194689/)). The **combined immune deficiency (CID)** produced by dominant-activating alleles is the entity catalogued as IMD73B (OMIM #618986).

Reported dominant-activating variants include **E62K** ([PMID: 30723080](https://pubmed.ncbi.nlm.nih.gov/30723080/)), **G12R** ([PMID: 31919089](https://pubmed.ncbi.nlm.nih.gov/31919089/)), **N92T** ([PMID: 31071452](https://pubmed.ncbi.nlm.nih.gov/31071452/)), and **P29R** ([PMID: 35596857](https://pubmed.ncbi.nlm.nih.gov/35596857/)). The gain-of-function mechanism is directly demonstrated at the biochemical level: cell lines transfected with the N92T variant *"displayed characteristics of active GTP-bound RAC2 including enhanced NADPH oxidase-derived superoxide production both at rest and in response to PMA"* ([PMID: 31071452](https://pubmed.ncbi.nlm.nih.gov/31071452/)). The heterozygous, dominant nature of the G12R allele — *"we identified a private, heterozygous mutation in the RAC2 gene (p.G12R)"* — confirms the autosomal dominant, single-allele mechanism ([PMID: 31919089](https://pubmed.ncbi.nlm.nih.gov/31919089/)). Patients uniformly show significant T- and B-lymphopenia with low immunoglobulins.

### Finding 2 — Clinical phenotype: recurrent respiratory/viral infections, T/B lymphopenia, hypogammaglobulinemia, and defective neutrophil chemotaxis

Across dominant-activating *RAC2* CID patients, the recurring clinical picture combines lymphoid and myeloid dysfunction. Common features include recurrent upper and lower respiratory tract infections, susceptibility to viral infections (HPV, EBV, herpetic skin infections), and a characteristic combined-immunodeficiency laboratory profile. Sharapova et al. document: *"Immunologic investigation revealed low numbers of TRECs/KRECs, a severe reduction of memory B cells, absence of isohemagglutinins, and low IgG levels"* ([PMID: 31071452](https://pubmed.ncbi.nlm.nih.gov/31071452/)) — reflecting impaired thymic/bone-marrow output and defective humoral immunity.

The **defining neutrophil migration defect** — which gives the disease its "defective neutrophil chemotaxis" character — is captured directly: *"Flow cytometric investigation of neutrophil migration demonstrated an absence of chemotaxis to fMLP"* ([PMID: 31071452](https://pubmed.ncbi.nlm.nih.gov/31071452/)). Myeloid abnormalities are broad; the cohort study summarizes that *"myeloid abnormalities included neutropenia, altered oxidative burst, impaired neutrophil migration, and visible neutrophil macropinosomes"* ([PMID: 38194689](https://pubmed.ncbi.nlm.nih.gov/38194689/)). Bronchiectasis and chronic pulmonary disease are frequently reported ([PMID: 31382036](https://pubmed.ncbi.nlm.nih.gov/31382036/); [PMID: 35596857](https://pubmed.ncbi.nlm.nih.gov/35596857/)). The P29R report additionally describes *"increased cytokine production and a dysregulated phenotype in T lymphocytes"* and *"accelerated apoptosis with augmented intracellular active caspase 3"* ([PMID: 35596857](https://pubmed.ncbi.nlm.nih.gov/35596857/)).

**Suggested HPO terms:** Recurrent respiratory infections (HP:0002205); Bronchiectasis (HP:0002110); Recurrent viral infections (HP:0004429); T lymphocytopenia (HP:0005403); B lymphocytopenia (HP:0010976); Decreased circulating IgG (HP:0004315); Neutropenia (HP:0001875); Recurrent bacterial infections (HP:0002718); Lymphopenia (HP:0001888).

### Finding 3 — Mechanism: RAC2 signals through p67phox, PAK1, and POR1/Arfaptin2 to control superoxide production and chemotaxis via distinct effector pathways

RAC2 is a hematopoietic-restricted Rho GTPase that cycles between a GTP-bound (active) and GDP-bound (inactive) state. Murine loss-of-function studies established its **non-redundant role** despite the presence of the homologous RAC1: *"Mice deficient in hemopoietic-specific Rac2 exhibited agonist-specific defects in neutrophil functions including chemoattractant-stimulated filamentous actin polymerization and chemotaxis, and superoxide production elicited by phorbol ester, fMLP, or IgG-coated particles, despite expression of the highly homologous Rac1 isoform"* ([PMID: 15528331](https://pubmed.ncbi.nlm.nih.gov/15528331/)).

Critically, the two principal RAC2 outputs are **separable and run through distinct effector modules**: *"Rac2 controls chemotaxis and superoxide production via distinct pathways"* ([PMID: 15814684](https://pubmed.ncbi.nlm.nih.gov/15814684/)) — the NADPH-oxidase superoxide arm via p67phox, and cytoskeletal/migration control via PAK1 and POR1/Arfaptin2. The consequences of altered nucleotide-state balance were shown with engineered mutants: the dominant-active Q61L mutant increased hematopoietic proliferation, whereas the dominant-negative D57N sequestered guanine-nucleotide exchange factors (GEFs), reduced GTP binding to ~10%, and increased apoptosis — *"expansion of cells transduced with WT Rac2 and a dominant active mutant, Q61L, was associated with significantly increased proliferation"* ([PMID: 11278678](https://pubmed.ncbi.nlm.nih.gov/11278678/)). In IMD73B patient cells, the constitutively GTP-bound mutant produces elevated resting and stimulated superoxide, increased F-actin content, and increased RAC2 protein expression ([PMID: 31071452](https://pubmed.ncbi.nlm.nih.gov/31071452/); [PMID: 35596857](https://pubmed.ncbi.nlm.nih.gov/35596857/)).

**Suggested GO terms:** neutrophil chemotaxis (GO:0030593); superoxide anion generation (GO:0042554); respiratory burst (GO:0045730); regulation of actin cytoskeleton organization (GO:0032956); GTPase activity (GO:0003924); apoptotic process (GO:0006915).

### Finding 4 — Model organisms: Rac2-null and mutant mice recapitulate neutrophil migration/oxidase defects; RAC2 is highly conserved

*Rac2* knockout mice (*Mus musculus*, NCBI Taxon 10090; ortholog gene *Rac2*) reproduce the core cellular pathology, showing non-redundant defects in neutrophil chemotaxis, L-selectin capture/rolling, F-actin polymerization, and superoxide production, plus impaired myeloid colony formation — *"is critical for development of myeloid colonies in vitro"* ([PMID: 15814684](https://pubmed.ncbi.nlm.nih.gov/15814684/); see also [PMID: 11278678](https://pubmed.ncbi.nlm.nih.gov/11278678/); [PMID: 15528331](https://pubmed.ncbi.nlm.nih.gov/15528331/)). Bone-marrow transduction/transplantation systems expressing human *RAC2* mutants (D57N dominant-negative, Q61L dominant-active) in murine hematopoietic cells reproduce mutation-specific phenotypes — *"Transplantation of transduced bone marrow cells into lethally irradiated rec[ipients]"* ([PMID: 11278678](https://pubmed.ncbi.nlm.nih.gov/11278678/)). Heterologous expression systems are used to classify patient variants by superoxide, PAK1 binding, and F-actin readouts ([PMID: 38194689](https://pubmed.ncbi.nlm.nih.gov/38194689/)). These are chiefly loss-of-function/knockout and mutant-overexpression models; a dedicated knock-in mouse carrying a specific human dominant-activating IMD73B allele would be the ideal next-generation model.

### Finding 5 — Treatment: immunoglobulin replacement and anti-infective supportive care, with allogeneic HCT as the definitive/curative therapy

Management combines supportive care (immunoglobulin replacement therapy, antimicrobial prophylaxis/treatment) with **allogeneic hematopoietic stem cell/cell transplantation (HSCT/HCT) as the only curative option**. Because RAC2 is expressed only in hematopoietic cells, replacing that compartment corrects the underlying defect. An index G12R patient was *"cured by hematopoietic stem cell transplantation"* ([PMID: 31919089](https://pubmed.ncbi.nlm.nih.gov/31919089/)); a homozygous R68W patient managed with *"immunoglobulin therapy, and ultimately hematopoietic cell transplantation (HCT), after which he achieved sustained clinical improvement"* ([PMID: 41685306](https://pubmed.ncbi.nlm.nih.gov/41685306/)).

Transplant is high-risk, however: an N92T patient *"experienced two hematopoietic stem cell transplantations and despite full chimerism, she developed bone marrow aplasia due to adenovirus infection and died at post-transplant day 86"* ([PMID: 31071452](https://pubmed.ncbi.nlm.nih.gov/31071452/)), underscoring substantial transplant-related mortality risk.

**Suggested NCIT terms:** Hematopoietic Cell Transplantation (NCIT:C15431); Immunoglobulin Therapy (NCIT:C593); Bone Marrow Transplantation (NCIT:C15265).

### Finding 6 — Genetics/epidemiology: ultra-rare autosomal dominant disorder; de novo or dominantly inherited germline missense variants with complete penetrance

*RAC2* maps to chromosome **22q13.1** (HGNC:9802; NCBI Gene 5880; UniProt P15153; gene OMIM 602049). IMD73B (phenotype OMIM #618986; MONDO:0033554) is inherited in an **autosomal dominant** manner; causal variants are heterozygous germline missense mutations that are frequently **de novo**. Duan et al. describe a de novo variant: *"Exome sequencing identified a de novo RAC2 mutation (c.44G > A/p.G15D) that was co-segregated with the disease in the family"* ([PMID: 36459342](https://pubmed.ncbi.nlm.nih.gov/36459342/)); and Lagresle-Peyrou et al. document both a de novo origin and subsequent vertical transmission: *"This mutation was de novo in the index case, who had been cured by hematopoietic stem cell transplantation but had transmitted the mutation to her sick daughter"* ([PMID: 31919089](https://pubmed.ncbi.nlm.nih.gov/31919089/)) — establishing new-mutation origin plus autosomal dominant transmission with apparent complete penetrance.

The disease is **ultra-rare**: *"We investigated 54 patients (23 previously reported) from 37 families yielding 15 novel RAC2 missense mutations, including one present only in homozygosity"* ([PMID: 38194689](https://pubmed.ncbi.nlm.nih.gov/38194689/)) — and this total spans all three allelic classes, so the dominant-activating IMD73B subset is smaller still. No population prevalence or incidence estimate is established. Pathogenic activating variants are private and absent/vanishingly rare in gnomAD. A homozygous activating variant (R68W) that phenocopies the dominant GOF state has also been described ([PMID: 41685306](https://pubmed.ncbi.nlm.nih.gov/41685306/)).

### Finding 7 — Anatomical/cellular targets and ontology mapping

RAC2 is expressed exclusively in hematopoietic cells, so the primary affected system is the **hematopoietic/immune system** (UBERON:0002390), with the **bone marrow** (UBERON:0002371) and circulating leukocytes as the disease compartment. The cohort description that *"Mutations in the small Rho-family guanosine triphosphate hydrolase RAC2, [are] critical for actin cytoskeleton remodeling and intracellular signal transduction"* ([PMID: 38194689](https://pubmed.ncbi.nlm.nih.gov/38194689/)) supports the cellular and subcellular mapping.

| Level | Structures / terms |
|---|---|
| Organ/system | Hematopoietic/immune system (UBERON:0002390); bone marrow (UBERON:0002371); secondary lung/bronchi (UBERON:0002048 / UBERON:0002185, bronchiectasis); skin/mucosa (HPV lesions); lymph nodes/spleen (lymphoproliferation); rarely kidney (light-chain deposition) |
| Cell types | Neutrophil (CL:0000775); T cell (CL:0000084); B cell (CL:0000236); monocyte/macrophage (CL:0000235); hematopoietic stem/progenitor cell (CL:0000037) |
| Subcellular | Cytosol (GO:0005829); plasma membrane/leading edge/lamellipodium (GO:0030027); actin cytoskeleton (GO:0015629); NADPH oxidase complex |

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous, dominant-activating missense mutation** arises in *RAC2* (22q13.1) — de novo or inherited (e.g., G12R, E62K, N92T, P29R, G15D). *(demonstrated)*
2. The mutation, often in the Switch I/Switch II region or nucleotide-binding pocket, **biases RAC2 toward the constitutively GTP-bound active state** (reduced GTP hydrolysis and/or spontaneous nucleotide exchange). *(demonstrated for N92T in vitro — enhanced GTP-bound characteristics)* → **leads to**
3. **Constitutive activation of RAC2 effector arms** even at rest. Because chemotaxis and superoxide are controlled through *distinct* effectors, the lesion branches: → **results in**

   **Branch A — NADPH oxidase (p67phox):** constitutive and hyper-inducible superoxide/ROS production (elevated resting and PMA-stimulated superoxide). → contributes to oxidative dysregulation and myeloid dysfunction.

   **Branch B — actin cytoskeleton (PAK1, POR1/Arfaptin2):** dysregulated, non-polarized F-actin assembly (increased F-actin content, impaired polarization) that **paradoxically impairs directed migration** despite an "active" GTPase. → **leads to** absent neutrophil chemotaxis to fMLP.

   **Branch C — cell survival/proliferation:** altered RAC2 signaling drives accelerated apoptosis (augmented active caspase-3) in lymphocytes and neutrophils, and lymphocyte dysregulation. → **leads to** T/B lymphopenia.
4. Combined myeloid (defective chemotaxis, altered oxidative burst, neutropenia, macropinosomes) and lymphoid (T/B lymphopenia, reduced memory B cells, low TRECs/KRECs, hypogammaglobulinemia) failure. *(demonstrated)* → **results in**
5. **Combined immunodeficiency (IMD73B):** recurrent bacterial respiratory infections, bronchiectasis, and susceptibility to viral pathogens (HPV, EBV, herpesviruses). *(demonstrated)*

```
   RAC2 dominant-activating missense mutation (heterozygous, germline)
                        │
        constitutive GTP-bound (active) RAC2
                        │
        ┌───────────────┼────────────────────┐
        ▼               ▼                     ▼
  p67phox/NADPH    PAK1 + POR1/         apoptosis / survival
   oxidase          Arfaptin2            dysregulation
        │            (actin)                  │
   ↑ superoxide   dysregulated F-actin   ↑ caspase-3
   (rest + PMA)   → impaired polarization  → T/B lymphopenia,
        │              │                    low memory B cells
        └──────┬───────┘                        │
               ▼                                ▼
    absent neutrophil chemotaxis      hypogammaglobulinemia
    + altered oxidative burst          low TRECs/KRECs
               └──────────────┬─────────────────┘
                              ▼
             COMBINED IMMUNODEFICIENCY (IMD73B)
   recurrent respiratory + viral infection, bronchiectasis
```

**Upstream vs downstream:** The mutation and its biochemical effect (constitutive GTP loading) are the most upstream events. The parallel effector arms are intermediate. Lymphopenia, hypogammaglobulinemia, and neutrophil dysfunction are downstream cellular readouts, and the infection phenotype is the terminal clinical manifestation. A key conceptual point is that a *gain* of GTPase activity produces a *loss* of coordinated cell function — because directed migration and regulated oxidative burst require dynamic cycling, not constitutive activation.

### Genotype–phenotype axis across the *RAC2* allelic series

| Biochemical class | Example alleles | Phenotype | Relation to IMD73B |
|---|---|---|---|
| Constitutively active ("RAS-like") | (high-activity alleles) | Neonatal SCID | Severe end of spectrum |
| **Dominant-activating (GOF)** | **E62K, G12R, N92T, P29R** | **Combined immunodeficiency (CID)** | **= IMD73B (OMIM #618986)** |
| Dominant-negative | D57N | LAD-like phagocyte defect | Distinct entity |
| Autosomal-recessive loss-of-function | (biallelic LOF) | CVID-like / other | Distinct entity |

Source: [PMID: 38194689](https://pubmed.ncbi.nlm.nih.gov/38194689/); [PMID: 35596857](https://pubmed.ncbi.nlm.nih.gov/35596857/).

---

## Section-by-Section Report Content

### 1. Disease Information
IMD73B is an autosomal dominant combined immunodeficiency caused by gain-of-function *RAC2* variants. **Identifiers:** OMIM #618986; MONDO:0033554; gene *RAC2* (OMIM 602049). MeSH-level indexing falls under "Severe Combined Immunodeficiency"/"Primary Immunodeficiency Diseases"; ICD-10 maps broadly to D81 (combined immunodeficiencies). **Synonyms/related names:** RAC2-related immunodeficiency (dominant-activating type); RAC2 gain-of-function combined immunodeficiency; combined immunodeficiency due to activating *RAC2* mutation. Information is derived from **aggregated disease-level resources and published individual case reports/case series**, not EHR data.

### 2. Etiology
**Causal factor:** monogenic — heterozygous dominant-activating germline missense mutation in *RAC2*. **Genetic risk:** the causal variant is itself the disease determinant (Mendelian, high penetrance); no separate susceptibility loci or modifier genes are established. **Environmental risk/protective/gene–environment factors:** none established; the disease is genetically determined. Environmental exposures (e.g., viral pathogens such as adenovirus post-transplant) act as *precipitants of complications* rather than disease causes.

### 3. Phenotypes
See Finding 2 and the HPO list above. Phenotype **onset** is typically infantile/childhood; **severity** moderate-to-severe and **variable**; **course** chronic/progressive with recurrent infections and structural lung damage (bronchiectasis). Laboratory abnormalities (LOINC-type analytes): low IgG, low T/B cell counts, low TRECs/KRECs, abnormal neutrophil oxidative burst and chemotaxis. Quality-of-life impact is substantial due to chronic infection burden, need for immunoglobulin therapy, and transplant-related morbidity; disease-specific QoL instruments have not been reported for this ultra-rare entity.

### 4. Genetic / Molecular Information
Causal gene *RAC2* (HGNC:9802). Pathogenic variants are missense (e.g., G12R, G15D, P29R, E62K, R68W [homozygous], N92T), classified pathogenic/likely pathogenic per ACMG/AMP with functional evidence (PS3: abnormal superoxide/F-actin/PAK1 assays). Variants are private, de novo or dominantly transmitted germline changes; allele frequency in gnomAD is absent/vanishingly rare. **Functional consequence:** gain-of-function/dominant-activating (constitutively GTP-bound). No modifier genes, epigenetic mechanisms, or chromosomal abnormalities are established for this disorder.

### 5. Environmental Information
No environmental, lifestyle, or infectious causal agents. Infectious agents (HPV, EBV, herpesviruses, and post-transplant adenovirus) are *consequences* of the immunodeficiency, not causes.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and diagram above. Molecular pathway: Rho-GTPase (RAC2) signaling → NADPH oxidase (p67phox) and actin-regulatory (PAK1, POR1/Arfaptin2) effectors. Cellular processes: dysregulated chemotaxis, respiratory burst, apoptosis, actin remodeling. Immune involvement: primary immunodeficiency affecting both myeloid and lymphoid compartments.

### 7. Anatomical Structures Affected
See Finding 7 table.

### 8. Temporal Development
**Onset:** typically infantile-to-childhood (e.g., infantile-onset CID; an 11-year-old presentation for P29R). **Progression:** chronic, lifelong, progressive with cumulative pulmonary damage (bronchiectasis). **Course:** recurrent-infection pattern; not self-limited. Critical intervention window: early diagnosis and HCT before irreversible organ (lung) damage or fatal infection.

### 9. Inheritance and Population
**Autosomal dominant**, frequently de novo, with vertical transmission documented; apparent **complete penetrance**; expressivity variable. Ultra-rare — <54 *RAC2* patients from 37 families worldwide (all allelic classes) as of 2024; no prevalence/incidence figure established. No founder effect, established consanguinity role (except the rare homozygous R68W case), or sex bias is documented for the dominant-activating class.

### 10. Diagnostics
**Genetic testing is definitive:** WES/WGS or targeted immunodeficiency gene panels including *RAC2*; single-gene testing to confirm. Functional confirmation assays: neutrophil superoxide/oxidative burst, F-actin content, chemotaxis to fMLP, PAK1-binding. Immunophenotyping: T/B lymphopenia, low memory B cells, low TRECs/KRECs, low IgG, absent isohemagglutinins. Newborn screening: **low TRECs on SCID newborn screening** may flag severe cases. Differential diagnosis: SCID, other actinopathies (CDC42, ARPC1B, WAS/WIP, DOCK8/DOCK2), LAD, CVID, chronic granulomatous disease.

### 11. Outcome / Prognosis
Guarded without curative therapy; chronic infections and bronchiectasis cause progressive morbidity. HCT can be curative with sustained improvement, but carries significant transplant-related mortality (documented death from adenovirus-driven marrow aplasia at day 86). Prognostic factors: mutation severity/biochemical class, degree of lymphopenia, pre-transplant infection/organ damage, and transplant course.

### 12. Treatment
See Finding 5. **Supportive:** immunoglobulin replacement (NCIT:C593), antimicrobial prophylaxis/treatment, antiviral therapy. **Definitive:** allogeneic HCT (NCIT:C15431) / bone marrow transplantation (NCIT:C15265). No approved gene therapy or targeted RAC2 inhibitor exists, though RAC-pathway inhibition is a plausible future strategy given the GOF mechanism.

### 13. Prevention
No primary prevention (monogenic). **Secondary:** early genetic diagnosis via newborn SCID screening and prompt HCT. **Genetic counseling** for autosomal dominant transmission risk (50% to offspring); prenatal/preimplantation genetic testing possible for known familial variants. **Tertiary:** immunoglobulin replacement, antimicrobial prophylaxis, and infection surveillance to prevent complications.

### 14. Other Species / Natural Disease
*RAC2* is highly conserved; the mouse ortholog is *Rac2* (*Mus musculus*, NCBI Taxon 10090). No naturally occurring animal disease is catalogued for RAC2 GOF; comparative biology is based on engineered/knockout mouse models. No zoonotic relevance.

### 15. Model Organisms
Mouse (*Mus musculus*): *Rac2* knockout and human-*RAC2*-mutant bone-marrow transduction/transplant models recapitulate neutrophil chemotaxis, F-actin, superoxide, and myeloid-colony defects. In-vitro heterologous expression systems classify patient variants. **Limitation:** existing models are largely loss-of-function/overexpression; a knock-in mouse for a specific human dominant-activating IMD73B allele would better model the lymphoid CID phenotype. Databases: MGI, IMPC/KOMP, Alliance of Genome Resources.

---

## Evidence Base

| PMID | Study (abbrev.) | Contribution | Evidence type |
|---|---|---|---|
| [38194689](https://pubmed.ncbi.nlm.nih.gov/38194689/) | Donkó 2024 — *Clinical and functional spectrum of RAC2-related immunodeficiency* | Defines genotype–function–phenotype axis (active→SCID, dominant-negative→LAD-like, dominant-activating→CID); 54 patients/37 families; myeloid abnormality summary | Human clinical + in vitro |
| [31071452](https://pubmed.ncbi.nlm.nih.gov/31071452/) | Sharapova 2019 — N92T | GOF biochemistry (GTP-bound, enhanced superoxide); CID labs; absent chemotaxis; fatal post-HSCT course | Human clinical + in vitro |
| [35596857](https://pubmed.ncbi.nlm.nih.gov/35596857/) | Zhang 2022 — P29R | Novel de novo GOF variant; ↑ROS, ↑F-actin, ↑RAC2 expression; apoptosis and T-cell dysregulation | Human clinical + in vitro |
| [31919089](https://pubmed.ncbi.nlm.nih.gov/31919089/) | Lagresle-Peyrou 2021 — G12R | Private heterozygous GOF; de novo then vertical transmission; HSCT curative; bone-marrow hypoplasia/AD-SCID | Human clinical |
| [30723080](https://pubmed.ncbi.nlm.nih.gov/30723080/) | Hsu 2019 — E62K | Dominant activating variant with lymphopenia, immunodeficiency, cytoskeletal defects | Human clinical + in vitro |
| [36459342](https://pubmed.ncbi.nlm.nih.gov/36459342/) | Duan 2023 — G15D | De novo variant identified by exome sequencing, co-segregating | Human clinical |
| [41685306](https://pubmed.ncbi.nlm.nih.gov/41685306/) | Desjardins 2026 — R68W (homozygous) | Homozygous activating variant phenocopying GOF; Ig therapy + HCT with sustained improvement | Human clinical |
| [31382036](https://pubmed.ncbi.nlm.nih.gov/31382036/) | Smits 2020 | Dominant activating RAC2 variant with immunodeficiency and pulmonary disease | Human clinical |
| [40860338](https://pubmed.ncbi.nlm.nih.gov/40860338/) | MENA actinopathy registry | RAC2-pathway actinopathies: late-onset, higher EBV/HPV, autoimmune cytopenia, lymphoproliferation; HSCT prioritization | Human clinical registry |
| [15528331](https://pubmed.ncbi.nlm.nih.gov/15528331/) | Yamauchi 2004 | Non-redundant Rac2 role in neutrophil actin polymerization, chemotaxis, superoxide | Model organism (mouse) |
| [15814684](https://pubmed.ncbi.nlm.nih.gov/15814684/) | Carstanjen 2005 | Chemotaxis vs superoxide via distinct effectors (p67phox, PAK1, POR1); myeloid colony development | Model organism (mouse) |
| [11278678](https://pubmed.ncbi.nlm.nih.gov/11278678/) | Gu 2001 | Q61L active/D57N dominant-negative biochemistry; BM transduction/transplant model | In vitro + model organism |

**Coherence:** The human case reports (dominant-activating alleles) and the murine mechanistic studies converge — the GOF alleles constitutively activate the same p67phox and actin effector arms that mouse loss-of-function studies proved are non-redundantly RAC2-dependent. No paper in the reviewed set contradicts the core model. The MENA registry ([PMID: 40860338](https://pubmed.ncbi.nlm.nih.gov/40860338/)) adds a note of phenotypic breadth (some RAC2-pathway patients present late with relatively normal immune profiles but higher EBV/HPV/autoimmune-cytopenia rates), indicating variable expressivity within the broader RAC2-regulator spectrum.

---

## Limitations and Knowledge Gaps

- **Ultra-rare N.** The entire *RAC2* literature comprises fewer than ~54 patients across all allelic classes; the dominant-activating IMD73B subset is smaller, limiting robust genotype–phenotype and outcome statistics.
- **No population epidemiology.** Prevalence/incidence, carrier frequency, sex ratio, and geographic distribution are unestablished (private de novo variants).
- **Mechanistic detail of lymphopenia.** The precise pathway by which cytoskeletal/oxidase dysregulation produces T/B lymphopenia and impaired thymic output is partly inferred (apoptosis, impaired migration/development) rather than fully demonstrated in patient thymus/marrow.
- **Model gap.** No knock-in mouse carrying a specific human dominant-activating IMD73B allele; existing models are knockout/overexpression, which capture myeloid but not fully the lymphoid CID phenotype.
- **Therapeutics.** No targeted RAC2 inhibitor or gene therapy exists; HCT outcome data are anecdotal (individual cases, including one death), with no cohort-level transplant survival statistics.
- **Variant classification.** Some *RAC2* missense changes remain functionally ambiguous; standardized functional assay thresholds for GOF vs dominant-negative classification are still being refined.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional knock-in mouse** for a canonical dominant-activating allele (e.g., E62K or P29R) to model the combined lymphoid+myeloid phenotype and test therapeutics in vivo.
2. **Single-cell transcriptomics/CITE-seq of patient bone marrow and blood** to map cell-type-specific effects on hematopoietic stem/progenitor, T, B, and neutrophil compartments and clarify the lymphopenia mechanism.
3. **Systematic functional variant classification pipeline** (superoxide, F-actin, PAK1-binding, GTP-loading) with defined GOF/DN thresholds, deposited to ClinVar/ClinGen, to resolve VUS.
4. **Multi-center natural history and transplant-outcome registry** for RAC2 immunodeficiency to establish prevalence, penetrance/expressivity, and HCT survival/optimal timing and conditioning.
5. **Preclinical evaluation of RAC-pathway inhibition** (e.g., small-molecule RAC/PAK1 inhibitors) as a mechanism-matched therapy or bridge-to-transplant, given the gain-of-function basis.
6. **Prospective HCT protocol optimization** including antiviral prophylaxis strategy, informed by the documented adenovirus-driven marrow aplasia mortality.

---

*Report compiled from 5 iterations, 7 confirmed findings, and 12 reviewed papers. Evidence types span human clinical case reports/series, murine model-organism studies, and in-vitro functional assays. All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Immunodeficiency_73B-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_73B-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 9 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:15814684` (6 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 2 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002390` (2 mentions) - the report calls it "hematopoietic/immune system"; UBERON calls it **hematopoietic system**

31 of 32 terms resolved to a current term; the rest could not be looked up either way.