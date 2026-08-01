---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-31T01:30:24.451513'
end_time: '2026-07-31T01:51:51.744522'
duration_seconds: 1287.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Kearns-Sayre syndrome
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
citation_count: 30
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Kearns-Sayre_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Kearns-Sayre_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kearns-Sayre syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Kearns-Sayre syndrome** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Kearns-Sayre Syndrome (KSS): Comprehensive Disease Characteristics Report

**Disease:** Kearns-Sayre syndrome (KSS)
**Ontology identifiers:** MONDO:0009723 · OMIM 530000 · Orphanet ORPHA:480 · MeSH D007625 · ICD-10 H49.81 · ICD-11 8C71 (mitochondrial myopathy) category
**Category:** Mendelian (mitochondrial genome disorder; almost always sporadic/de novo)

---

## Summary

Kearns-Sayre syndrome (KSS) is a rare, multisystem mitochondrial disorder caused by a **single large-scale, heteroplasmic deletion of mitochondrial DNA (mtDNA)** that removes contiguous oxidative-phosphorylation (OXPHOS) subunit genes and transfer-RNA genes. The loss of tRNA genes cripples intramitochondrial protein translation, and the loss of OXPHOS subunits directly disables the respiratory chain, producing a cellular ATP deficit that is most damaging to high-energy-demand post-mitotic tissues — extraocular muscle, cardiac conduction tissue, brain white matter, retina, cochlea, and endocrine organs. KSS is defined clinically by a **triad** — progressive external ophthalmoplegia/ptosis, pigmentary retinopathy, and onset before age 20 — **plus at least one of**: cardiac conduction block, cerebrospinal fluid (CSF) protein >100 mg/dL, or cerebellar ataxia.

KSS sits on the **single large-scale mtDNA deletion syndrome (SLSMDS) spectrum** together with Pearson syndrome (infantile, hematologic) and chronic progressive external ophthalmoplegia (CPEO, milder/later). The same molecular lesion can produce all three phenotypes, and patients can evolve along the Pearson → KSS → CPEO continuum over time. The deletion is nearly always **sporadic (de novo)**, arising in the maternal oocyte or early embryo, with a low empiric recurrence risk of ~4% among offspring of affected women — a critical fact for genetic counseling that distinguishes deletions from maternally inherited mtDNA point mutations.

There is **no cure**; management is supportive, organ-directed, and multidisciplinary. The single most life-saving intervention is **early/prophylactic cardiac pacing**, because progressive atrioventricular conduction block causing sudden cardiac death is the leading cause of mortality. A second high-value, disease-specific intervention is **folinic acid** supplementation, which corrects the cerebral folate deficiency (low CSF 5-methyltetrahydrofolate) that arises from failed ATP-dependent folate transport across the choroid plexus, and can reverse associated white-matter demyelination. Natural history is chronic-progressive: in a large European pediatric-onset cohort, mean onset was 10 years, mean last examination 31 years, and median time from onset to death 11.5 years.

---

## Section 1 — Disease Information

**Overview.** KSS is a mitochondrial cytopathy on the SLSMDS spectrum. It is defined by the **conventional triad plus one major criterion** (Finding F001): (1) progressive external ophthalmoplegia (PEO)/ptosis, (2) pigmentary ("salt-and-pepper") retinopathy, (3) onset before age 20 years — **plus** at least one of cardiac conduction block, CSF protein >100 mg/dL, or cerebellar syndrome. In a European pediatric cohort of 80 SLSMD patients, KSS spectrum disorder was present in 50%, Pearson syndrome in 21%, and CPEO in 29% ([PMID: 34872991](https://pubmed.ncbi.nlm.nih.gov/34872991/)).

> "Kearns-Sayre syndrome according to the conventional triad (onset before 20 years of age, ophthalmoplegia, pigmentary degeneration of the retina) with at least one of three other major manifestations (heart block, CSF protein over 100 mg/dl, cerebellar syndrome)" — [PMID: 8167995](https://pubmed.ncbi.nlm.nih.gov/8167995/)

**Key identifiers:** MONDO:0009723 · OMIM 530000 · Orphanet ORPHA:480 · MeSH D007625 · ICD-10 H49.81 · UMLS C0022541.

**Synonyms / alternative names:** Kearns-Sayre syndrome; Kearns-Sayre-Daroff syndrome; oculocraniosomatic neuromuscular disorder with ragged-red fibers; ophthalmoplegia-plus syndrome; mitochondrial cytopathy, Kearns-Sayre type; chronic progressive external ophthalmoplegia with myopathy (KSS end of spectrum).

**Source of information:** Predominantly **aggregated disease-level resources** (OMIM, Orphanet, HPO) supplemented by clinical case series and multicentre cohorts (e.g., PMID 34872991, PMID 41074779). Because KSS is rare, much of the phenotype-frequency data derives from pooled cohorts rather than population EHR.

---

## Section 2 — Etiology

**Primary cause (genetic).** KSS is caused by a **single large-scale mtDNA deletion** (typically 1.1–10 kb) that removes multiple contiguous genes (Findings F004, F013). It is a primary genetic (not infectious/environmental) disorder of the mitochondrial genome.

**Genetic risk factors.** The lesion is heteroplasmic; **higher blood heteroplasmy correlates with earlier age of onset** ([PMID: 39985363](https://pubmed.ncbi.nlm.nih.gov/39985363/)). Larger deletions correlate with more deleted respiratory-chain complex genes (r=0.516, p=0.012) and more deleted tRNAs (r=0.534, p=0.010); KSS patients had larger deletions and greater tRNA/complex involvement than non-KSS ([PMID: 41074779](https://pubmed.ncbi.nlm.nih.gov/41074779/)). The deletion arises via **direct-repeat misannealing** in the single-stranded major arc during replication (Finding F013).

**Environmental risk factors.** No established environmental cause for the primary deletion. In *late-onset CPEO* (the mild end of the spectrum), acquired mitochondrial toxicity from cigarette use and hepatitis C was noted more often than expected, suggesting acquired mitochondrial stress may modulate the adult phenotype ([PMID: 21156440](https://pubmed.ncbi.nlm.nih.gov/21156440/)) — but this is not causal for KSS itself.

**Protective factors / gene–environment interactions.** No validated genetic protective alleles or dietary protective factors are established. Because pathology is energy-threshold dependent, tissues with lower deletion heteroplasmy are relatively spared. A notable **negative gene–environment interaction**: endurance exercise *worsens* muscle pathology in the mtDNA-deletion mouse model (Findings F007/F012), cautioning against intense exercise.

---

## Section 3 — Phenotypes

KSS is multisystem (Finding F005). Phenotype frequencies from a pediatric SLSMD cohort ([PMID: 34872991](https://pubmed.ncbi.nlm.nih.gov/34872991/)) and a KSS-specific endocrine survey ([PMID: 1424198](https://pubmed.ncbi.nlm.nih.gov/1424198/)):

| Phenotype | Type | Frequency | Onset/Course | Suggested HPO |
|---|---|---|---|---|
| Progressive external ophthalmoplegia / ptosis | Clinical sign (muscle) | Defining (~100% KSS) | Childhood, progressive | HP:0000602, HP:0000508 |
| Pigmentary retinopathy | Physical/ophthalmic sign | 46% | Childhood, progressive | HP:0000580, HP:0007737 |
| Skeletal muscle involvement / exercise intolerance | Symptom (muscle) | 65% | Progressive | HP:0003323, HP:0003546 |
| Cerebellar ataxia | Neurologic sign | 40% | Progressive | HP:0001251 |
| Short stature | Physical/endocrine | 38–42% | Childhood | HP:0004322 |
| Hearing impairment (sensorineural) | Sensory sign | 39% | Progressive | HP:0000407 |
| Cardiac conduction disease (AV block) | Clinical sign (cardiac) | 39% | Progressive, life-threatening | HP:0001678, HP:0011712 |
| Cognitive involvement | Neurologic | 36% | Variable | HP:0001249 |
| Diabetes mellitus | Lab/endocrine | 13–25% | Later childhood/adult | HP:0000819 |
| Gonadal dysfunction / hypogonadism | Endocrine | 20% | Peri/post-puberty | HP:0000135 |
| Renal disease (proximal tubulopathy/Fanconi) | Lab/organ | 19% | Variable | HP:0000114, HP:0008658 |
| Elevated CSF protein (>100 mg/dL) | Lab abnormality | Major criterion | — | HP:0002922 |
| Stroke-like episodes | Neurologic | 9% | Episodic | HP:0002401 |

**Characteristics.** Age of onset is typically **childhood/adolescence (<20 y)**, insidious/chronic. Severity is **variable but overall moderate-to-severe**, and progression is **progressive** across organ systems. Endocrine dysfunction can precede neurological manifestations in ~20% of mitochondrial-disease patients ([PMID: 40382647](https://pubmed.ncbi.nlm.nih.gov/40382647/)).

**Quality of life.** Fatigue increases and quality of life decreases with advancing age ([PMID: 39985363](https://pubmed.ncbi.nlm.nih.gov/39985363/)). Ptosis/ophthalmoplegia impair vision and communication; ataxia and myopathy impair mobility; deafness, diabetes, and cardiac disease add cumulative burden.

---

## Section 4 — Genetic / Molecular Information

**Causal lesion.** Single large-scale deletion of the **mitochondrial genome** (not a nuclear gene). The recurrent **"common deletion" m.8470_13446del4977** (4,977 bp) accounts for only a minority of cases — ~14.3% in a Chinese pediatric cohort, with 23 novel deletions identified in 25 patients ([PMID: 41074779](https://pubmed.ncbi.nlm.nih.gov/41074779/)) (Finding F004).

> "Only 14.3% had the classic 4977 bp deletion, and 23 novel deletions were identified in 25 patients." — [PMID: 41074779](https://pubmed.ncbi.nlm.nih.gov/41074779/)

**Commonly deleted genes.** A recurrent deleted region **involving MT-ND5 (HGNC:7641) occurs in 96%** of SLSMDS participants regardless of phenotype ([PMID: 39985363](https://pubmed.ncbi.nlm.nih.gov/39985363/)). Deletions in the major arc typically remove OXPHOS-subunit genes (e.g., **MT-ND3, MT-ND4, MT-ND4L, MT-ND5** of complex I; **MT-CO3** of complex IV; **MT-ATP6/8**; **MT-CYB** of complex III) plus multiple tRNA genes.

**Variant classification / type.** Structural (large deletion), heteroplasmic; pathogenic per ACMG for mitochondrial-genome disorders when a single large-scale deletion is detected in the appropriate clinical context.

**Origin.** **Germline-mosaic / sporadic (de novo)** — arising in the oocyte or early embryo, not inherited from an affected parent in the vast majority (Finding F008). Not present in population allele-frequency databases (not a polymorphism).

**Functional consequence.** **Loss of function** — loss of tRNA genes impairs mitochondrial translation of all 13 mtDNA-encoded OXPHOS subunits; loss of subunit genes directly disables complexes I, III, IV, and V. Nuclear-encoded **complex II remains normal** ([PMID: 41086592](https://pubmed.ncbi.nlm.nih.gov/41086592/)).

**Genotype–phenotype.** Larger deletions → more deleted MRC complexes (r=0.516, p=0.0123) and more deleted tRNAs (r=0.534, p=0.0103); higher heteroplasmy → earlier onset ([PMID: 41074779](https://pubmed.ncbi.nlm.nih.gov/41074779/), [PMID: 39985363](https://pubmed.ncbi.nlm.nih.gov/39985363/)).

**Molecular origin (Finding F013).** Deletions form in the **major arc** (single-stranded during replication) and are flanked by **direct nucleotide repeats**. The common deletion arises between a first repeat arm at 8470–8482 bp and a second at 13,447–13,459 bp. Spatial proximity in a hairpin-like "contact zone" makes these repeats ~3× more likely to cause deletions ([PMID: 37158879](https://pubmed.ncbi.nlm.nih.gov/37158879/)); breakpoints occur consistently in regions of sequence homology, consistent with slipped-replication/misannealing followed by clonal expansion ([PMID: 29257976](https://pubmed.ncbi.nlm.nih.gov/29257976/)).

> "The direct repeats located within the contact zone, such as the well-known common repeat with a first arm at 8470-8482 bp (base pair) and a second arm at 13,447-13,459 bp, are three times more likely to cause deletions compared to direct repeats located outside of the contact zone." — [PMID: 37158879](https://pubmed.ncbi.nlm.nih.gov/37158879/)

**Modifier genes / epigenetics / chromosomal abnormalities:** No established nuclear modifier genes for the sporadic deletion (nuclear mtDNA-maintenance defects instead cause *multiple* deletions and are Mendelian — a distinct entity). No epigenetic or nuclear chromosomal abnormality is causal.

---

## Section 5 — Environmental Information

KSS has **no established environmental, lifestyle, or infectious cause**; it is a primary mtDNA structural disorder. Relevant modifiers: (a) **intense/endurance exercise** worsens muscle pathology in the mtDNA-deletion mouse model and is a caution in severe disease ([PMID: 39956167](https://pubmed.ncbi.nlm.nih.gov/39956167/)); (b) acquired mitochondrial toxins (tobacco, hepatitis C) associate with adult CPEO but are not causal for KSS ([PMID: 21156440](https://pubmed.ncbi.nlm.nih.gov/21156440/)); (c) **folic acid** (as opposed to folinic acid/5MTHF) can inhibit 5MTHF transport across the blood–CSF barrier and should be avoided ([PMID: 36341171](https://pubmed.ncbi.nlm.nih.gov/36341171/)).

---

## Section 6 — Mechanism / Pathophysiology

**Causal chain.** mtDNA deletion → loss of tRNA + OXPHOS-subunit genes → impaired mitochondrial translation + directly disabled respiratory complexes I/III/IV/V → **electron-transport-chain failure → ATP deficit + increased reactive oxygen species** → energy failure in high-demand post-mitotic tissues → clinical multisystem disease (Findings F004, F006).

**Molecular pathways / biochemical abnormalities.** Oxidative phosphorylation is the central affected pathway (KEGG hsa00190). **Complex IV (cytochrome-c-oxidase) is most frequently impaired**, whereas nuclear-encoded complex II activity remains normal ([PMID: 41086592](https://pubmed.ncbi.nlm.nih.gov/41086592/)). Mitochondrial dysfunction can occur even at deletion heteroplasmy **<10%** ([PMID: 41086592](https://pubmed.ncbi.nlm.nih.gov/41086592/)).

> "Complex IV was most frequently impaired, whereas nuclear-encoded complex II activity remained normal in all samples." — [PMID: 41086592](https://pubmed.ncbi.nlm.nih.gov/41086592/)

**Cellular processes / tissue-damage mechanisms.** Muscle biopsy shows **ragged-red fibers** (subsarcolemmal accumulation of structurally abnormal mitochondria on modified Gomori trichrome), **ragged-blue fibers** (SDH), and **COX-negative fibers** ([PMID: 17541738](https://pubmed.ncbi.nlm.nih.gov/17541738/), [PMID: 38018320](https://pubmed.ncbi.nlm.nih.gov/38018320/)). The CNS shows **spongiform (spongy) degeneration and demyelinating leukoencephalopathy** — distinguishing KSS as a white-matter mitochondrial disorder versus the predominantly grey-matter MELAS/MERRF/Leigh disorders ([PMID: 17541738](https://pubmed.ncbi.nlm.nih.gov/17541738/)).

> "White matter involvement is always seen in Kearns-Sayre syndrome" — [PMID: 17541738](https://pubmed.ncbi.nlm.nih.gov/17541738/)

**Secondary mechanism — cerebral folate deficiency (Finding F003).** ATP failure impairs the ATP-dependent, folate-receptor–mediated transport of 5-methyltetrahydrofolate (5MTHF) across the choroid plexus, producing **low CSF 5MTHF with normal blood folate and a decreased CSF/serum folate ratio** ([PMID: 18058625](https://pubmed.ncbi.nlm.nih.gov/18058625/), [PMID: 16365882](https://pubmed.ncbi.nlm.nih.gov/16365882/)). This contributes to the leukoencephalopathy and is reversible with folinic acid.

> "Failure of ATP production in Kearns-Sayre syndrome ... provides one explanation for the finding of low spinal fluid (CSF) 5-methyltetrahydrofolate (5MTHF) levels in this condition." — [PMID: 18058625](https://pubmed.ncbi.nlm.nih.gov/18058625/)

**Metabolic changes.** Impaired pyruvate oxidation → **lactic acidosis** (elevated blood/CSF lactate; elevated lactate peak on MR spectroscopy). Elevated **CSF protein**.

**Immune involvement:** Not autoimmune; not a primary immune disorder.

**Biomarkers / molecular profiling (Finding F007).** Serum **FGF21** and **GDF15** are elevated. FGF21 was 347 pg/mL in mtDNA-deletion patients vs 66 pg/mL controls (p<0.0001), reproduced in mice (1,163 vs 379 pg/mL, p<0.0001); FGF21 specificity 89.3%, GDF15 sensitivity 76% ([PMID: 27794108](https://pubmed.ncbi.nlm.nih.gov/27794108/)). GDF15 was elevated in all SLSMDS participants ([PMID: 39985363](https://pubmed.ncbi.nlm.nih.gov/39985363/)).

**Suggested GO / CL terms:** GO:0006119 (oxidative phosphorylation), GO:0032543 (mitochondrial translation), GO:0006979 (response to oxidative stress), GO:0006754 (ATP biosynthetic process); cell types CL:0000746 (cardiac muscle cell / conduction), CL:0000187 (muscle cell), CL:0000540 (neuron), CL:0000604 (retinal rod cell), CL:0000209 (auditory hair cell).

---

## Section 7 — Anatomical Structures Affected

- **Primary organs:** extraocular muscles (UBERON:0001601), skeletal muscle (UBERON:0002385), heart conduction system (UBERON:0004146), retina (UBERON:0000966), brain white matter (UBERON:0002316), cerebellum (UBERON:0002037), brainstem (UBERON:0002298), cochlea/inner ear (UBERON:0001846).
- **Secondary/endocrine:** pancreas/islets (UBERON:0000006), pituitary (UBERON:0000007), parathyroid (UBERON:0001132), adrenal cortex (UBERON:0001235), gonads, kidney proximal tubule (UBERON:0004134).
- **Body systems:** nervous, cardiovascular, musculoskeletal, sensory (visual/auditory), endocrine, renal.
- **Neuroimaging localization (Findings F005/F011):** symmetrical T2/FLAIR hyperintensities involving **dorsal brainstem (7/7), cerebellum (6/7), and globus pallidus (6/7)** with elevated lactate on MRS ([PMID: 40637848](https://pubmed.ncbi.nlm.nih.gov/40637848/)). Lesions are typically **bilateral/symmetric**.
- **Subcellular:** **mitochondrion** (GO:0005739), specifically the **mitochondrial inner membrane / respiratory chain** (GO:0005743, GO:0005746).
- **Cellular pathology:** ragged-red/COX-negative myofibers; pigmentary retinal changes at the RPE; spongiform white matter.

---

## Section 8 — Temporal Development

- **Onset:** typically **pediatric, before age 20** (defining criterion), insidious/chronic. Mean onset ~10 years in the European cohort ([PMID: 34872991](https://pubmed.ncbi.nlm.nih.gov/34872991/)); ~9.6 years in a Chinese KSS subgroup vs ~20 years for CPEO ([PMID: 38018320](https://pubmed.ncbi.nlm.nih.gov/38018320/)).
- **Progression:** chronic-**progressive**, with multisystem accrual over years. Median time from onset to death **11.5 years** ([PMID: 34872991](https://pubmed.ncbi.nlm.nih.gov/34872991/)).

> "The average age at disease onset and at last examination was 10 and 31 years, respectively. The median time from disease onset to death was 11.5 years." — [PMID: 34872991](https://pubmed.ncbi.nlm.nih.gov/34872991/)

- **Spectrum evolution:** phenotypes evolve along **Pearson → KSS → CPEO** over time; a prior history of Pearson syndrome predicts poorer survival ([PMID: 39985363](https://pubmed.ncbi.nlm.nih.gov/39985363/)) (Finding F009).
- **Critical intervention windows:** early detection of bifascicular block for prophylactic pacing; early folinic acid before irreversible demyelination.

---

## Section 9 — Inheritance and Population

- **Inheritance:** the single large-scale deletion is **sporadic/de novo**; empiric recurrence risk **~4%** for offspring of affected women ([PMID: 28536827](https://pubmed.ncbi.nlm.nih.gov/28536827/)) (Finding F008). Very low recurrence contrasts with the high/unpredictable recurrence of maternally inherited mtDNA point mutations ([PMID: 27450679](https://pubmed.ncbi.nlm.nih.gov/27450679/)).

> "The majority of mtDNA rearrangements, such as single large-scale deletions, are sporadic, but there is a small risk of recurrence (~4%) among the offspring of affected women." — [PMID: 28536827](https://pubmed.ncbi.nlm.nih.gov/28536827/)

- **Penetrance/expressivity:** heteroplasmy- and tissue-threshold dependent; **variable expressivity**; higher heteroplasmy → earlier/more severe onset.
- **Epidemiology:** KSS is rare. Precise population prevalence/incidence figures were **not robustly established in the reviewed literature** (documented knowledge gap); Orphanet lists KSS as a rare disease. Disease-specific incidence remains uncertain and is generally reported only within combined SLSMDS cohorts.
- **Sex ratio:** approximately equal; gonadal dysfunction affected both sexes equally ([PMID: 1424198](https://pubmed.ncbi.nlm.nih.gov/1424198/)).
- **Consanguinity/founder effects:** not applicable to the sporadic deletion.

---

## Section 10 — Diagnostics

**Definitive molecular diagnosis (Finding F011).** Detection of a **single large-scale mtDNA deletion**, best in **skeletal muscle** (higher heteroplasmy than blood, which frequently tests negative), via **long-range PCR + next-generation sequencing** ([PMID: 41074779](https://pubmed.ncbi.nlm.nih.gov/41074779/)) or **Southern blot** ([PMID: 25539952](https://pubmed.ncbi.nlm.nih.gov/25539952/)).

> "The presence of large-scale mtDNA deletions was an objective diagnostic factor for KSS" — [PMID: 30450853](https://pubmed.ncbi.nlm.nih.gov/30450853/)

**Supporting tests:**
- **Muscle biopsy:** ragged-red, ragged-blue, COX-negative fibers; respiratory-chain enzymology (complex IV most reduced, complex II normal) ([PMID: 41086592](https://pubmed.ncbi.nlm.nih.gov/41086592/)).
- **CSF:** protein >100 mg/dL (major criterion); low 5MTHF; elevated lactate.
- **Blood:** elevated lactate; **FGF21/GDF15** supportive biomarkers ([PMID: 27794108](https://pubmed.ncbi.nlm.nih.gov/27794108/), [PMID: 39985363](https://pubmed.ncbi.nlm.nih.gov/39985363/)).
- **Brain MRI/MRS:** symmetrical dorsal brainstem, cerebellar, globus pallidus T2/FLAIR hyperintensities; lactate peak ([PMID: 40637848](https://pubmed.ncbi.nlm.nih.gov/40637848/)).
- **Cardiac:** ECG/Holter (fascicular/AV block), echocardiography, cardiac MRI (intramural basal inferolateral late-gadolinium enhancement in KSS/CPEO) ([PMID: 26001801](https://pubmed.ncbi.nlm.nih.gov/26001801/)).
- **Ophthalmology:** pigmentary retinopathy, ophthalmoplegia. **Audiometry.** **Endocrine labs** (glucose/HbA1c, GH/IGF-1, PTH, cortisol/ACTH stimulation, thyroid). **Renal tubular function** (Fanconi screen).

**Genetic testing approach:** targeted **mitochondrial DNA testing** (long-range PCR/NGS/Southern blot) on muscle is first-line; blood may be negative. WGS/WES of the nuclear genome is generally not needed unless a mtDNA-maintenance disorder (multiple deletions) is suspected.

**Differential diagnosis:** CPEO and Pearson syndrome (same spectrum), MELAS/MERRF (grey-matter, point mutations), myotonic dystrophy, oculopharyngeal muscular dystrophy, myasthenia gravis, other causes of pigmentary retinopathy.

---

## Section 11 — Outcome / Prognosis

- **Survival:** chronic-progressive; **median onset-to-death 11.5 years** in the pediatric-onset cohort ([PMID: 34872991](https://pubmed.ncbi.nlm.nih.gov/34872991/)).
- **Leading cause of death:** **sudden cardiac death** from progressive conduction block (Finding F002). Prophylactic pacing markedly improves survival.
- **Adverse prognostic factors:** prior **Pearson syndrome** history ([PMID: 39985363](https://pubmed.ncbi.nlm.nih.gov/39985363/)); higher heteroplasmy (earlier onset); profound growth retardation with multisystem dysfunction ([PMID: 40382647](https://pubmed.ncbi.nlm.nih.gov/40382647/)).
- **Morbidity:** cumulative disability from ophthalmoplegia, myopathy, ataxia, deafness, endocrinopathy, and renal disease. Quality of life declines with age ([PMID: 39985363](https://pubmed.ncbi.nlm.nih.gov/39985363/)).
- **Prognostic biomarkers:** GDF15/FGF21 (disease burden); heteroplasmy level.

---

## Section 12 — Treatment

**No disease-modifying cure exists; management is supportive and organ-directed (Finding F012).**

| Intervention | Rationale / evidence | Suggested MAXO |
|---|---|---|
| **Prophylactic permanent pacemaker / ICD** | Life-saving; indicated for bifascicular block or prolonged HV interval ([PMID: 23430846](https://pubmed.ncbi.nlm.nih.gov/23430846/), [PMID: 2707275](https://pubmed.ncbi.nlm.nih.gov/2707275/)) | MAXO:0000133 (implantation) |
| **Folinic acid (or 5MTHF)** 1–3 mg/kg/day | Corrects CSF 5MTHF; reverses demyelination; preferred over folic acid ([PMID: 25539952](https://pubmed.ncbi.nlm.nih.gov/25539952/), [PMID: 36341171](https://pubmed.ncbi.nlm.nih.gov/36341171/)) | MAXO:0000058 (dietary supplementation) |
| **Coenzyme Q10 (ubiquinone)** | Improved corneal endothelial disease in 2 KSS children; with scavengers reduced seizures ([PMID: 27442316](https://pubmed.ncbi.nlm.nih.gov/27442316/), [PMID: 18058625](https://pubmed.ncbi.nlm.nih.gov/18058625/)) | MAXO:0000058 |
| **Insulin / oral agents** for diabetes; **hormone replacement** (GH, thyroid, PTH/calcium, corticosteroids) | Endocrine screening/replacement ([PMID: 1424198](https://pubmed.ncbi.nlm.nih.gov/1424198/), [PMID: 37815532](https://pubmed.ncbi.nlm.nih.gov/37815532/)) | MAXO:0000242 (hormone therapy) |
| **Hearing aids / cochlear implants** | Sensorineural deafness | MAXO:0001028 |
| **Ptosis correction** (crutch glasses, sling surgery) | Visual/functional | MAXO:0000004 (surgical) |
| **Physical/occupational/speech therapy**; dysphagia & nutrition management | Ataxia, myopathy, dysphagia | MAXO:0000506 (rehabilitation) |
| **Avoid intense/endurance exercise** in severe disease | Exercise worsens muscle pathology in mito-miceΔ ([PMID: 39956167](https://pubmed.ncbi.nlm.nih.gov/39956167/)) | — |

> "We report 2 patients with KSS with corneal lesions involving the endothelium, which improved with Coenzyme Q10 (CoQ10)." — [PMID: 27442316](https://pubmed.ncbi.nlm.nih.gov/27442316/)

**Experimental / emerging:** mitochondrial biogenesis inducers (bezafibrate/PGC-1α axis, resveratrol) ([PMID: 24606795](https://pubmed.ncbi.nlm.nih.gov/24606795/)); antioxidant peptides (elamipretide); gene/cell strategies (experimental for mtDNA deletions). **Pharmacogenomics:** avoid mitochondrial-toxic drugs (e.g., aminoglycosides for cochlea, valproate).

---

## Section 13 — Prevention

- **Primary prevention:** none (sporadic de novo deletion; cannot be prevented). **Genetic counseling** for the ~4% recurrence risk in offspring of affected women ([PMID: 28536827](https://pubmed.ncbi.nlm.nih.gov/28536827/)).
- **Secondary prevention (surveillance in diagnosed patients):** **periodic ECG/Holter** for conduction disease (enabling prophylactic pacing); **CSF 5MTHF / folinic acid**; **endocrine screening** (glucose, GH, PTH, cortisol, thyroid); **audiometry**; **renal tubular** monitoring; ophthalmologic surveillance.
- **Tertiary prevention:** prevent complications — pacing before syncope/arrest; treat endocrinopathy before crises; nutritional support.
- **Reproductive options:** prenatal/PGD counseling; heteroplasmy makes prediction difficult, but recurrence risk is low.
- **Behavioral:** avoid intense exercise and mitochondrial toxins; avoid folic acid in favor of folinic acid.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy:** primarily a **human (NCBI:txid9606)** disorder. Naturally occurring KSS-analogous SLSMD disease in companion animals/wildlife is **not established** in the reviewed literature.
- **Orthologous genes:** the deleted mtDNA genes are conserved across mammals (e.g., mouse mt-Nd5, mt-Co3, mt-Cytb).
- **Comparative biology:** mtDNA deletions accumulate with age across species; the deletion mechanism (direct-repeat misannealing in the major arc) is conserved.
- **Zoonotic potential:** none (non-infectious genetic disease).

---

## Section 15 — Model Organisms

- **Primary model — "mito-miceΔ" (Findings F007/F012):** mice accumulating a large-scale ΔmtDNA deletion reproduce **severe multisystem mitochondrial disease**; endurance swimming exacerbated muscle pathology ([PMID: 39956167](https://pubmed.ncbi.nlm.nih.gov/39956167/)). FGF21 elevation was reproduced (1,163 vs 379 pg/mL, p<0.0001) ([PMID: 27794108](https://pubmed.ncbi.nlm.nih.gov/27794108/)).

> "endurance exercise exacerbated muscle pathology in mito-miceΔ" — [PMID: 39956167](https://pubmed.ncbi.nlm.nih.gov/39956167/)

- **Related models:** Polg mutator mice (mtDNA instability, brain deletion hotspots and mood phenotypes; [PMID: 26481320](https://pubmed.ncbi.nlm.nih.gov/26481320/)); TYMP/UPP double-knockout MNGIE mice (mtDNA depletion/leukoencephalopathy; [PMID: 24727567](https://pubmed.ncbi.nlm.nih.gov/24727567/)) — relevant for mtDNA-maintenance pathology though modeling a different (Mendelian) disease.
- **Cellular/in vitro:** patient-derived fibroblasts/myoblasts, cybrids, and iPSC-derived tissues carrying heteroplasmic deletions.
- **Model limitations:** mouse deletion location/heteroplasmy differ from patients; models don't fully capture the human triad (retinopathy, ophthalmoplegia, conduction block, cerebral folate deficiency).

---

## Mechanistic Model / Interpretation

```
        Single large-scale mtDNA deletion (major arc, direct-repeat misannealing)
                                   │  (sporadic, de novo, heteroplasmic)
                                   ▼
        Loss of tRNA genes  +  Loss of OXPHOS-subunit genes (MT-ND5 in 96%)
                                   │
                                   ▼
        Impaired mitochondrial translation  →  Respiratory chain failure
              (Complex IV most affected; Complex II [nuclear] spared)
                                   │
                                   ▼
                 ATP deficit  +  ↑ROS  +  lactic acidosis
                                   │
        ┌──────────────┬──────────┼───────────┬──────────────┬─────────────┐
        ▼              ▼          ▼           ▼              ▼             ▼
  Extraocular/     Cardiac    Brain white   Retina/RPE   Cochlea     Endocrine organs
  skeletal muscle  conduction  matter                                (islet/GH/PTH/adrenal)
  (RRF, COX-neg)   (AV block)  (spongiform,  (pigmentary  (SN deaf-   (DM, short stature,
        │          │           demyelin.)    retinopathy) ness)        hypoPTH, adrenal insuff.)
        ▼          ▼           │ (↓CSF 5MTHF via failed
   PEO/ptosis,  SUDDEN         │  ATP-dependent folate transport)
   myopathy     CARDIAC        ▼
                DEATH ◄──────  Cerebral folate deficiency ──► folinic acid REVERSIBLE
                │
      PROPHYLACTIC PACING = life-saving
```

The unifying principle is a **tissue-specific energy threshold**: organs with the highest oxidative demand and least regenerative capacity (extraocular muscle, cardiac conduction tissue, CNS white matter, retina, cochlea, endocrine secretory cells) cross the ATP-failure threshold first. Two mechanistic branches are therapeutically actionable and disease-specific: (1) the **cardiac conduction branch** (prevented by pacing) and (2) the **cerebral folate branch** (corrected by folinic acid). Most other manifestations are managed by conventional organ-specific replacement/support.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [34872991](https://pubmed.ncbi.nlm.nih.gov/34872991/) | Largest pediatric SLSMD cohort (n=80): spectrum distribution, phenotype frequencies, natural history (onset 10y, death 11.5y from onset) | Human cohort |
| [8167995](https://pubmed.ncbi.nlm.nih.gov/8167995/) | Conventional KSS diagnostic triad + major criteria | Human clinical |
| [23430846](https://pubmed.ncbi.nlm.nih.gov/23430846/) | Conduction-disease progression; early pacing to prevent sudden death | Human clinical |
| [2707275](https://pubmed.ncbi.nlm.nih.gov/2707275/) | Prophylactic pacemaker indication for bifascicular block | Human clinical |
| [18058625](https://pubmed.ncbi.nlm.nih.gov/18058625/) | ATP failure → cerebral folate deficiency; ubiquinone/scavengers reduce seizures | Human clinical |
| [25539952](https://pubmed.ncbi.nlm.nih.gov/25539952/) | Folinic acid normalizes CSF 5MTHF in KSS | Human clinical |
| [16365882](https://pubmed.ncbi.nlm.nih.gov/16365882/) | CFD + leukoencephalopathy reversible with folinic acid | Human case |
| [36341171](https://pubmed.ncbi.nlm.nih.gov/36341171/) | Folic acid inhibits 5MTHF transport; folinic acid preferred | Human clinical |
| [39985363](https://pubmed.ncbi.nlm.nih.gov/39985363/) | MT-ND5 deleted in 96%; heteroplasmy–onset link; GDF15 biomarker; PS predicts poor survival | Human cohort |
| [41074779](https://pubmed.ncbi.nlm.nih.gov/41074779/) | Common deletion only 14.3%; deletion-size genotype-phenotype correlations; long-range PCR/NGS | Human cohort |
| [41086592](https://pubmed.ncbi.nlm.nih.gov/41086592/) | Complex IV most impaired, complex II spared; dysfunction at <10% heteroplasmy | Human/in vitro |
| [17541738](https://pubmed.ncbi.nlm.nih.gov/17541738/) | RRF/COX-negative fibers; white-matter involvement always in KSS | Human pathology |
| [28536827](https://pubmed.ncbi.nlm.nih.gov/28536827/) | ~4% recurrence risk for sporadic deletions | Review/counseling |
| [27450679](https://pubmed.ncbi.nlm.nih.gov/27450679/) | Very low recurrence for single large-scale deletions vs point mutations | Human genetics |
| [27794108](https://pubmed.ncbi.nlm.nih.gov/27794108/) | FGF21/GDF15 biomarkers (human + mouse) | Human + model |
| [39956167](https://pubmed.ncbi.nlm.nih.gov/39956167/) | mito-miceΔ model; endurance exercise worsens myopathy | Model organism |
| [37815532](https://pubmed.ncbi.nlm.nih.gov/37815532/) | Adrenal insufficiency in SLSMDS | Human cohort |
| [1424198](https://pubmed.ncbi.nlm.nih.gov/1424198/) | KSS endocrine prevalences (short stature 38%, gonadal 20%, DM 13%) | Human review |
| [29594260](https://pubmed.ncbi.nlm.nih.gov/29594260/) | DM more common with mtDNA defects (23.3% vs 3.7%) | Human cohort |
| [40382647](https://pubmed.ncbi.nlm.nih.gov/40382647/) | Endocrine dysfunction can precede neurology; severe short stature in KSS/PS | Human cohort |
| [40637848](https://pubmed.ncbi.nlm.nih.gov/40637848/) | Neuroimaging: symmetric brainstem/cerebellar/pallidal lesions + lactate | Human imaging |
| [30450853](https://pubmed.ncbi.nlm.nih.gov/30450853/) | mtDNA deletion as objective KSS diagnostic factor | Human clinical |
| [38018320](https://pubmed.ncbi.nlm.nih.gov/38018320/) | 155-patient cohort; KSS larger deletions/earlier onset than CPEO | Human cohort |
| [26001801](https://pubmed.ncbi.nlm.nih.gov/26001801/) | Cardiac MRI phenotype (basal inferolateral LGE) in KSS/CPEO | Human imaging |
| [37158879](https://pubmed.ncbi.nlm.nih.gov/37158879/) | Common-deletion repeats; contact-zone 3× deletion risk | Computational/genomic |
| [29257976](https://pubmed.ncbi.nlm.nih.gov/29257976/) | Breakpoints at homology repeats; misannealing mechanism | Human genomic |
| [27442316](https://pubmed.ncbi.nlm.nih.gov/27442316/) | CoQ10 improved KSS corneal endothelial disease | Human case |
| [24606795](https://pubmed.ncbi.nlm.nih.gov/24606795/) | Mitochondrial biogenesis pharmacology (experimental) | Review |
| [21156440](https://pubmed.ncbi.nlm.nih.gov/21156440/) | Late-onset CPEO phenotype; acquired mito-toxicity | Human cohort |

---

## Limitations and Knowledge Gaps

1. **Epidemiology gap.** Reliable KSS-specific **prevalence and incidence** figures were not established in the reviewed literature; most numbers derive from small pooled SLSMDS cohorts, not population registries.
2. **Cohort mixing.** Many phenotype frequencies come from combined SLSMDS cohorts (KSS + Pearson + CPEO), so KSS-specific frequencies carry uncertainty.
3. **Rare-disease sample sizes.** Endocrine, renal, and imaging series are small (single digits to tens of patients); wide confidence intervals.
4. **Treatment evidence.** Most therapeutic claims (CoQ10, folinic acid, biogenesis inducers) rest on case reports/small series, not RCTs; the folic-acid caution derives from two cases.
5. **Genotype resolution.** Heteroplasmy varies by tissue and over time, complicating prognosis prediction; blood testing can be falsely negative.
6. **Model-organism translation.** mito-miceΔ replicate severe myopathy but not the full human triad (retinopathy, ophthalmoplegia, conduction block, cerebral folate deficiency).

---

## Proposed Follow-up Experiments / Actions

1. **Population epidemiology study** — establish KSS-specific prevalence/incidence and sex/age distributions using national mitochondrial-disease registries (Orphanet, GBD, MSeqDR).
2. **Prospective natural-history cohort** with serial ECG/Holter, echocardiography, CSF 5MTHF, endocrine panels, and heteroplasmy quantification to define intervention windows and validate GDF15/FGF21 as prognostic biomarkers.
3. **Controlled trial of folinic acid** timing (early vs symptomatic) on white-matter and neurocognitive outcomes.
4. **Registry analysis of prophylactic pacing/ICD** thresholds (HV interval, bifascicular block) to formalize evidence-based pacing guidelines specific to KSS.
5. **Deletion-breakpoint sequencing** across a large KSS cohort to correlate deleted-gene content (tRNA vs OXPHOS load) with organ-specific outcomes.
6. **Preclinical testing** of mitochondrial-targeted therapies (elamipretide, biogenesis inducers, gene/mitochondrial-editing approaches) in mito-miceΔ and patient iPSC-derived cardiomyocytes/retinal organoids.

---

*Report compiled from 13 confirmed findings and 49 reviewed papers over 5 investigation iterations. Evidence types are annotated as human clinical, human cohort, model organism, in vitro, or computational.*


## Artifacts

- [OpenScientist final report](Kearns-Sayre_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Kearns-Sayre_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)