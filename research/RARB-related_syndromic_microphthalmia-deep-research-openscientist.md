---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-31T08:34:21.540109'
end_time: '2026-07-31T08:50:37.925981'
duration_seconds: 976.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: RARB-related syndromic microphthalmia
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
citation_count: 20
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: RARB-related_syndromic_microphthalmia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RARB-related_syndromic_microphthalmia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RARB-related syndromic microphthalmia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RARB-related syndromic microphthalmia** covering all of the
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

# RARB-related Syndromic Microphthalmia (MCOPS12): Comprehensive Disease Characterization Report

*Autonomous literature-based discovery report (5 iterations, 11 confirmed findings, 32 papers reviewed). Evidence is human clinical, in vitro functional, and model-organism as indicated. Primary citations are given as PMIDs. Where information is unavailable for this ultra-rare disorder, this is stated explicitly.*

---

## Summary

**RARB-related syndromic microphthalmia — Syndromic Microphthalmia type 12 (MCOPS12; OMIM #615524; MONDO:0014441)** is a rare Mendelian developmental disorder caused by germline variants in *RARB* (retinoic acid receptor beta), located at chromosome 3p24.2 (HGNC:9865; NCBI Gene 5915; UniProt P10826). The unifying pathomechanism is **dysregulation of retinoic-acid (RA) signaling in either direction** during embryogenesis. Dominant *de novo* gain-of-function (GOF) missense variants — most notably the recurrent p.Arg387Cys and p.Arg387Ser substitutions — increase RA-induced transcriptional activity 2- to 3-fold, whereas biallelic recessive loss-of-function (LOF) variants and dominant truncating/dominant-negative alleles abolish or subvert RARB activity. Both extremes converge on the same tightly dosage-sensitive developmental program governing neural-crest-derived periocular mesenchyme and central nervous system development, explaining how opposite molecular defects produce an overlapping clinical syndrome.

Clinically, MCOPS12 presents congenitally with a **developmental eye malformation** (microphthalmia, anophthalmia, and/or coloboma) that is variably combined with **pulmonary hypoplasia, congenital diaphragmatic hernia, and cardiac defects** — the "PDAC" overlap that originally linked *RARB* to this phenotype. Neonatal survivors uniformly develop **severe global developmental delay with a progressive movement disorder** (spasticity and/or dystonia, with or without chorea), and a majority show Chiari type I malformation and severe feeding difficulties. The phenotype is more variable than initially recognized: some individuals lack cardinal features such as the eye anomaly or motor impairment, indicating incomplete/variable expressivity.

Prognosis is **guarded**: the PDAC-overlap presentation carries substantial neonatal mortality driven by pulmonary hypoplasia and diaphragmatic hernia, and survivors face severe lifelong disability. There is **no disease-modifying therapy**; management is entirely supportive and multidisciplinary. Prevention is limited to genetic counseling, prenatal diagnosis, and preimplantation genetic testing. MCOPS12 is ultra-rare, with roughly 52+ individuals reported in the literature to date.

---

## Key Findings

### F001 — *RARB* variants cause MCOPS12 via bidirectional dysregulation of retinoic-acid signaling

The central molecular finding is that both **dominant gain-of-function** and **recessive/dominant-negative loss-of-function** mechanisms in *RARB* produce the same disease. In the founding study, two siblings with a PDAC-syndrome phenotype (but not their unaffected sibling) were compound heterozygous for a nonsense variant (c.355C>T, p.Arg119\*) and a frameshift variant (c.1201_1202insCT, p.Ile403Serfs\*15), establishing a **recessive loss-of-function** route: *"two PDAC-syndrome-affected siblings, but not their unaffected sibling, were compound heterozygous for nonsense (c.355C>T [p.Arg119\*]) and frameshift (c.1201_1202insCT [p.Ile403Serfs\*15]) mutations in retinoic acid receptor beta (RARB)"* ([PMID: 24075189](https://pubmed.ncbi.nlm.nih.gov/24075189/)). The same work demonstrated a **dominant gain-of-function** route via transfection assays: *"p.Arg387Ser and p.Arg387Cys altered RARB induced a 2- to 3-fold increase in transcriptional activity in response to retinoic acid ligands, suggesting a gain-of-function mechanism."*

A subsequent systematic functional study (25 new individuals; 52 reviewed) resolved the apparent paradox: *"all RARB variants tested in our assays exhibited either a gain-of-function or a loss-of-function activity. Loss-of-function variants disrupted RARB function through a dominant-negative effect"* ([PMID: 37092537](https://pubmed.ncbi.nlm.nih.gov/37092537/)). Thus GOF missense variants over-activate RA target genes, while pathogenic heterozygous LOF variants act through a **dominant-negative** mechanism (mutant receptor poisons the wild-type/heterodimer complex), and biallelic LOF variants act through simple loss of function. The shared consequence is a departure from the narrow window of correct RA-signaling *dosage* required for normal morphogenesis.

### F002 — Clinical spectrum: eye malformation plus a progressive neurodevelopmental/movement disorder

Cardinal features are **microphthalmia/anophthalmia/coloboma**, **pulmonary hypoplasia**, **diaphragmatic hernia**, and **cardiac defects** (the PDAC overlap), plus — in survivors — severe global developmental delay with a progressive motor disorder. In the largest neurodevelopmental case series, *"all subjects who survived the neonatal period (n = 10) displayed severe global developmental delay with progressive motor impairment due to spasticity and/or dystonia (with or without chorea). The majority of subjects also showed Chiari type I malformation and severe feeding difficulties"* ([PMID: 27120018](https://pubmed.ncbi.nlm.nih.gov/27120018/)). Later work broadened the picture, noting that *"disruption of RARB is associated with a more variable phenotype than initially suspected, with the absence in some individuals of cardinal features of MCOPS12, such as developmental eye anomaly or motor impairment"* ([PMID: 37092537](https://pubmed.ncbi.nlm.nih.gov/37092537/)). MCOPS12 is therefore best conceptualized as an **eye–brain developmental syndrome** with variable multi-organ (lung, diaphragm, heart) involvement.

### F003 — Mouse/vertebrate RAR/RXR genetics recapitulate the phenotype and localize RA action to ocular mesenchyme/neural crest

Model-organism genetics provide strong mechanistic corroboration. RAR double-null mutant mice (including *Rarb*) show congenital malformations across nearly every organ system, recapitulating the **fetal vitamin-A-deficiency (VAD) syndrome**, including eye defects and diaphragm malformation — the latter directly paralleling human congenital diaphragmatic hernia ([PMID: 7607068](https://pubmed.ncbi.nlm.nih.gov/7607068/)). Heterodimer-specific analyses showed that *"both RXR alpha:RAR beta and RXR alpha:RAR gamma heterodimers appear to function during the development of the ocular mesenchyme"* ([PMID: 9541199](https://pubmed.ncbi.nlm.nih.gov/9541199/)), localizing RARB function to ocular mesenchyme. Conditional RAR inactivation experiments demonstrated that *"the action of RA during eye morphogenesis is occurring specifically in neural crest-derived periocular mesenchyme"* ([PMID: 18539269](https://pubmed.ncbi.nlm.nih.gov/18539269/)), pinpointing the **neural-crest-derived periocular mesenchyme** as the key responding tissue, with *Pitx2* as a downstream RA-responsive gene. RXRα-null studies further confirmed convergence of RXR and RAR signaling in heart and eye morphogenesis ([PMID: 7923367](https://pubmed.ncbi.nlm.nih.gov/7923367/)), and temporally controlled RA depletion in rat produced specific neural-crest, ocular, and nervous-system defects ([PMID: 9272952](https://pubmed.ncbi.nlm.nih.gov/9272952/)).

### F004 — Variants span the ligand-binding and DNA-binding domains; DBD variants impair nuclear localization

Most reported *RARB* variants affect the **ligand-binding domain (LBD)** — including the recurrent codon-387 substitutions (p.Arg387Cys/Ser). However, a missense variant in the highly conserved **DNA-binding domain (DBD)** was identified in ocular coloboma, and *in vitro* it produced *"lower steady-state protein levels, reduced transcriptional activity, and incomplete nuclear localization of the mutant RARB protein compared with wild-type"* ([PMID: 31816153](https://pubmed.ncbi.nlm.nih.gov/31816153/)). Functional relevance *in vivo* was confirmed in zebrafish, where *"human RARB messenger RNA partially reduced the ocular phenotype caused by morpholino knockdown of rarga gene, a zebrafish homolog of human RARB."* This establishes a second class of LOF mechanism — impaired nuclear import and reduced steady-state protein — distinct from the LBD-based GOF mechanism.

### F005 — Epidemiologic context: microphthalmia/anophthalmia is rare; *RARB* accounts for a small fraction of syndromic cases

Anophthalmia/microphthalmia/coloboma (AMC) are rare congenital eye defects. Reported global prevalence is *"anophthalmia at 0.6-4.2 per 100,000 births and microphthalmia at 2-17 per 100,000 births, with a combined prevalence of up to 30 per 100,000"* ([PMID: 40038803](https://pubmed.ncbi.nlm.nih.gov/40038803/)), and *"15-20% of infant blindness [is] attributed to these anomalies."* Another population-based estimate places anophthalmia/microphthalmia at *"up to 2 per 10,000 live births"* ([PMID: 35716026](https://pubmed.ncbi.nlm.nih.gov/35716026/)). AMC is genetically heterogeneous (*PAX6, SOX2, OTX2, CHD7, STRA6, RARB*, and others); **RARB-related MCOPS12 is an ultra-rare subset**, with only ~52+ individuals reported. No *RARB*-specific prevalence or incidence estimate is established.

### F006 — Inheritance is predominantly autosomal dominant *de novo*, with rare recessive families and dominant truncating variants

Most MCOPS12 cases arise from **heterozygous de novo missense variants** (autosomal dominant, sporadic). A **recessive form** exists: *"RARB bi-allelic loss-of-function variants, inherited from asymptomatic heterozygous carrier parents, have been found in a recessive family with four MCOPS12-affected members"* ([PMID: 37321544](https://pubmed.ncbi.nlm.nih.gov/37321544/)) — importantly, heterozygous carriers of these recessive LOF alleles are **unaffected**, indicating dose/mechanism-dependent penetrance. The same report documented a heterozygous *de novo* nonsense (truncating) variant, providing *"the first detailed evidence for a role of dominant RARB truncating alterations in congenital eye-brain disease, expanding the spectrum of MCOPS12-associated mutations."*

### F007 — Environmental retinoid dysregulation phenocopies RARB disease, reinforcing RA dosage as the shared pathomechanism

Both maternal vitamin-A deficiency and retinoid excess cause overlapping congenital malformations, mirroring the bidirectional (GOF/LOF) genetic mechanism. Gestational exposure to exogenous retinoids produces **retinoic acid embryopathy/fetal retinoid syndrome**: *"Isotretinoin is a retinoid which is derived from Vitamin A. It is indicated for severe cystic acne treatment, but it has been classified as teratogenic. A wide spectrum of birth defects including craniofacial, heart, and nervous system malformations have been described with prenatal exposure to this drug"* ([PMID: 29308367](https://pubmed.ncbi.nlm.nih.gov/29308367/)). A candidate downstream cellular mechanism is neural-crest apoptosis: *"isotretinoin (13-cis retinoic acid), the prodrug of all-trans retinoic acid (ATRA), exaggerates neural crest cell (NCC) apoptosis via upregulation of the pro-apoptotic transcription factor p53"* ([PMID: 28833556](https://pubmed.ncbi.nlm.nih.gov/28833556/)). These environmental phenocopies both confirm the causal role of RA dosage and identify neural-crest cells as the vulnerable population — the same tissue implicated by the mouse conditional-knockout data.

### F008 — No disease-modifying therapy exists; management is supportive, multidisciplinary, and symptom-directed

There is **no curative or disease-modifying treatment**. Management is symptomatic across domains. For the ocular malformation, *"serial socket expansion with progressively larger acrylic conformers"* is the standard approach, achieving *"good outcomes ... in 18 orbits (75%); fair outcomes, in 6 (25%) cases"* ([PMID: 36257503](https://pubmed.ncbi.nlm.nih.gov/36257503/)). Neonatal care addresses congenital diaphragmatic hernia (surgical repair, respiratory support, ECMO in severe cases) and cardiac defects; neurologic care uses antispasticity/antidystonic agents and physical/occupational/speech therapy; gastroenterologic care provides feeding support (e.g., gastrostomy); and Chiari I malformation is monitored with neurosurgical evaluation as needed. Orbital cysts associated with microphthalmos/anophthalmos may aid socket expansion and generally allow good cosmetic outcomes ([PMID: 12812886](https://pubmed.ncbi.nlm.nih.gov/12812886/)).

### F009 — Phenotype spectrum mapped to HPO terms with anatomy (UBERON)

The MCOPS12 phenotype maps onto a defined set of HPO terms with qualitative frequencies (tabulated in Section 3 below). The neuromotor phenotype and its frequency are anchored by [PMID: 27120018](https://pubmed.ncbi.nlm.nih.gov/27120018/) (all 10 survivors with developmental delay; majority Chiari I and feeding difficulties), and the ocular/pulmonary/diaphragmatic/cardiac set by [PMID: 24075189](https://pubmed.ncbi.nlm.nih.gov/24075189/): *"Anophthalmia and/or microphthalmia, pulmonary hypoplasia, diaphragmatic hernia, and cardiac defects are the main features of PDAC syndrome."*

### F010 — Diagnosis relies on molecular confirmation (trio exome/genome) plus imaging; differential includes STRA6 and other AMC genes

Diagnosis is established by identifying a pathogenic *RARB* variant, typically via **whole-exome sequencing**: *"Using whole-exome sequencing, we found that two PDAC-syndrome-affected siblings ..."* ([PMID: 24075189](https://pubmed.ncbi.nlm.nih.gov/24075189/)). Prenatal detectability is meaningful — *"CEAs [congenital eye anomalies] were prenatally diagnosed in 23.5% of cases"* ([PMID: 38528322](https://pubmed.ncbi.nlm.nih.gov/38528322/)). The differential diagnosis for the underlying AMC includes *"chromosomal aberrations and mutations in genes such as PAX6, SOX2, OTX2, and CHD7"* ([PMID: 40038803](https://pubmed.ncbi.nlm.nih.gov/40038803/)), plus Matthew-Wood/PDAC syndrome due to *STRA6* and retinoic acid embryopathy (the environmental phenocopy).

### F011 — Prognosis is guarded; prevention limited to genetic counseling and prenatal testing

Prognosis is guarded. The PDAC-overlap presentation carries neonatal mortality (the explicit distinction of survivors — *"all subjects who survived the neonatal period (n = 10)"* — implies neonatal deaths; [PMID: 27120018](https://pubmed.ncbi.nlm.nih.gov/27120018/)), and survivors have severe lifelong disability. Prevention centers on reproductive options: genetic counseling, prenatal diagnosis, and preimplantation genetic testing. Recurrence risk is low for *de novo* dominant disease (though germline mosaicism cannot be excluded) but **25% for autosomal recessive families**, where counseling relies on carrier detection ([PMID: 37321544](https://pubmed.ncbi.nlm.nih.gov/37321544/)).

---

## Mechanistic Model / Interpretation

MCOPS12 is fundamentally a **retinoic-acid dosage disorder**. RA is a diffusible morphogen whose nuclear receptors (RARα/β/γ heterodimerizing with RXRs) act as ligand-dependent transcription factors. Normal morphogenesis of the eye, diaphragm, heart, and CNS requires RA signaling within a narrow concentration/activity window. *RARB* variants perturb this window from either direction:

```
                         RETINOIC ACID SIGNALING DOSAGE
   TOO LOW  <---------------------- OPTIMAL ----------------------> TOO HIGH
      |                               |                                |
  LOF variants                 Normal development              GOF variants
  - biallelic nonsense/                                        - p.Arg387Cys
    frameshift (recessive)                                     - p.Arg387Ser
  - dominant-negative                                          (2-3x increased
    missense/truncating                                         RA transcriptional
  - DBD variants (impaired                                      activity)
    nuclear localization)                                            |
      |                                                              |
      +---------------------------+----------------------------------+
                                  |
                                  v
              DISRUPTED RA-RESPONSIVE TRANSCRIPTION
        (neural-crest-derived periocular mesenchyme; CNS)
               key RA target gene: Pitx2
                                  |
        +-------------------------+-------------------------+
        v                         v                         v
   EYE MORPHOGENESIS        DIAPHRAGM / LUNG /         CNS DEVELOPMENT
   FAILURE                  HEART DEVELOPMENT          (basal ganglia,
   - microphthalmia         - diaphragmatic hernia      cerebellum,
   - anophthalmia           - pulmonary hypoplasia      hindbrain)
   - coloboma               - cardiac defects          - developmental delay
                                                       - spasticity/dystonia
                                                       - Chiari I malformation
```

**Upstream vs downstream:** The upstream trigger is the germline *RARB* variant altering receptor activity/dosage. The proximate downstream event is dysregulated transcription of RA-responsive genes (e.g., *Pitx2*) in the **neural-crest-derived periocular mesenchyme** (eye) and CNS progenitors. A candidate terminal cellular mechanism — best evidenced in the retinoid-excess phenocopy — is **neural-crest cell apoptosis via p53 upregulation**. The clinical manifestations (ocular, diaphragmatic, pulmonary, cardiac, neurologic) are the downstream morphologic and functional consequences.

**Why opposite mutations cause the same disease:** Because both under- and over-activation move the system out of the tolerated RA-activity window, and because dominant-negative LOF alleles corrupt receptor complexes, the developmental output is disrupted regardless of direction. This is directly paralleled in nature by the overlapping malformation spectra of **fetal vitamin-A deficiency** (too little RA) and **retinoic acid embryopathy** (too much RA).

### Genotype–mechanism–phenotype summary

| Variant class | Example | Molecular mechanism | Inheritance | Evidence |
|---|---|---|---|---|
| LBD missense (GOF) | c.1159C>T p.Arg387Cys; c.1159C>A p.Arg387Ser | 2–3× increased RA transcriptional activity | AD, *de novo* | [PMID: 24075189](https://pubmed.ncbi.nlm.nih.gov/24075189/) |
| Nonsense/frameshift (biallelic LOF) | c.355C>T p.Arg119\*; c.1201_1202insCT p.Ile403Serfs\*15 | Loss of function | AR (carriers unaffected) | [PMID: 24075189](https://pubmed.ncbi.nlm.nih.gov/24075189/); [PMID: 37321544](https://pubmed.ncbi.nlm.nih.gov/37321544/) |
| Dominant-negative (LOF) | various missense/truncating | Poisons WT/heterodimer complex | AD | [PMID: 37092537](https://pubmed.ncbi.nlm.nih.gov/37092537/) |
| Dominant truncating (LOF) | *de novo* nonsense | Truncation; eye–brain disease | AD, *de novo* | [PMID: 37321544](https://pubmed.ncbi.nlm.nih.gov/37321544/) |
| DBD missense (LOF) | conserved DBD residue | ↓ protein, ↓ activity, impaired nuclear localization | (coloboma case) | [PMID: 31816153](https://pubmed.ncbi.nlm.nih.gov/31816153/) |

---

## Detailed Disease Characterization (Template Sections)

### 1. Disease Information
- **Overview:** A syndromic form of microphthalmia in which eye maldevelopment co-occurs with malformations of the diaphragm, lungs, heart, and CNS, plus a progressive neuromotor disorder. Originally recognized within the **PDAC** phenotype (**P**ulmonary hypoplasia/agenesis, **D**iaphragmatic hernia, **A**nophthalmia/microphthalmia, **C**ardiac defects), historically linked to *STRA6*; *RARB* defines a distinct molecular subset ([PMID: 24075189](https://pubmed.ncbi.nlm.nih.gov/24075189/)).
- **Identifiers:** OMIM **#615524** (Microphthalmia, syndromic 12; MCOPS12); MONDO:0014441; gene *RARB* (HGNC:9865; NCBI Gene 5915; OMIM \*180220; Ensembl ENSG00000077092; UniProt P10826; locus 3p24.2). Orphanet: within syndromic microphthalmia/anophthalmia group. ICD-11: LB10.0 (congenital anophthalmos/microphthalmos) with syndromic qualifiers; ICD-10: Q11.0–Q11.2. MeSH: Microphthalmos (D008850).
- **Synonyms:** MCOPS12; Syndromic microphthalmia 12; RARB-related microphthalmia; microphthalmia with diaphragmatic hernia and cardiac defects; RARB-related eye–brain developmental disorder.
- **Information source:** Aggregated disease-level resources (OMIM/Orphanet) plus **individual-patient case series/reviews** (Srour 2013; Srour 2016; Caron 2023, 25 new/52 reviewed; Trieschmann 2023) — not a large registry/EHR dataset.

### 2. Etiology
- **Causal factors:** Germline pathogenic variants in *RARB* (monogenic). Two mechanistic classes: dominant *de novo* GOF missense (recurrent codon 387) and biallelic recessive/dominant-negative/dominant-truncating LOF.
- **Genetic risk factors:** The *RARB* variant is causal, not merely a susceptibility locus. Advanced paternal age is a general (non-specific) contributor to *de novo* dominant variants. No proven modifier genes.
- **Environmental risk factors:** None established as causes of MCOPS12. Gestational retinoid exposure (isotretinoin) and vitamin-A imbalance are biologically relevant phenocopies (Section 5).
- **Protective factors:** None. Heterozygous carriers of a single recessive LOF allele are asymptomatic ([PMID: 37321544](https://pubmed.ncbi.nlm.nih.gov/37321544/)).
- **Gene–environment interactions:** Disease and retinoic-acid embryopathy/fetal VAD converge phenotypically because both perturb RA-signaling dosage ([PMID: 29308367](https://pubmed.ncbi.nlm.nih.gov/29308367/); [PMID: 28833556](https://pubmed.ncbi.nlm.nih.gov/28833556/)). No formal GxE study exists for *RARB*.
- **CHEBI:** all-trans-retinoic acid CHEBI:15367; retinol/vitamin A CHEBI:17336; isotretinoin (13-cis-RA) CHEBI:6067.

### 3. Phenotypes (with suggested HPO terms, onset, severity, progression, frequency)

| Phenotype | HPO | Type | Onset | Severity/Course | Frequency |
|---|---|---|---|---|---|
| Microphthalmia | HP:0000568 | Structural | Congenital | Severe, stable structural | Very frequent/defining |
| Anophthalmia | HP:0000528 | Structural | Congenital | Severe | Subset |
| Coloboma | HP:0000589 | Structural | Congenital | Variable | Subset |
| Optic nerve/retinal anomaly | HP:0000648 / HP:0000479 | Structural | Congenital | Variable | Subset |
| Congenital diaphragmatic hernia | HP:0000776 | Structural | Congenital | Life-threatening | Subset (PDAC) |
| Pulmonary hypoplasia | HP:0002089 | Structural | Congenital | Life-threatening | Subset (PDAC) |
| Congenital heart defect | HP:0001627 | Structural | Congenital | Variable | Subset |
| Global developmental delay | HP:0001263 | Neurodevelopmental | Infancy | Severe | Essentially all survivors |
| Intellectual disability | HP:0001249 | Neurodevelopmental | Childhood | Severe | Essentially all survivors |
| Spasticity | HP:0001257 | Neurological sign | Infancy/childhood | **Progressive** | Majority of survivors |
| Dystonia | HP:0001332 | Neurological sign | Infancy/childhood | **Progressive** | Majority of survivors |
| Chorea | HP:0002072 | Neurological sign | Childhood | Progressive/variable | Subset |
| Chiari type I malformation | HP:0007099 | Structural (CNS) | Congenital | Variable | Majority |
| Severe feeding difficulties | HP:0011968 | Functional | Neonatal/infancy | Severe | Majority |

- **Variable expressivity/reduced penetrance:** some individuals lack cardinal eye or motor features ([PMID: 37092537](https://pubmed.ncbi.nlm.nih.gov/37092537/)).
- **Quality of life:** Severe impact — visual impairment/blindness, motor disability, intellectual disability, feeding dependence. Disease-specific validated QoL instruments (EQ-5D/SF-36/PROMIS) have **not** been reported for this ultra-rare disorder.

### 4. Genetic / Molecular Information
- **Causal gene:** *RARB* (HGNC:9865; OMIM \*180220; 3p24.2); ligand-activated nuclear receptor heterodimerizing with RXR at retinoic-acid response elements (RAREs).
- **Variant types/classification:** recurrent codon-387 missense and specific truncating alleles are **pathogenic**; others likely pathogenic; some ocular-only DBD variants VUS later functionally supported ([PMID: 31816153](https://pubmed.ncbi.nlm.nih.gov/31816153/)). Variant classes: missense (LBD, DBD), nonsense, frameshift.
- **Allele frequency:** pathogenic variants are **absent from gnomAD** (de novo or private familial).
- **Origin:** germline (de novo dominant or inherited recessive/dominant). No somatic role.
- **Functional consequences:** gain-of-function, loss-of-function, and dominant-negative ([PMID: 37092537](https://pubmed.ncbi.nlm.nih.gov/37092537/)); DBD variants additionally impair nuclear localization.
- **Modifier genes/epigenetics:** none confirmed; paralog redundancy (*RARA*, *RARG*) is biologically relevant. No disease-specific methylation/histone signature.
- **Chromosomal abnormalities:** not a feature; chromosomal microarray typically normal.
- **GO:** nuclear receptor activity GO:0004879; retinoic acid receptor activity GO:0003708; RAR signaling pathway GO:0048384; regulation of transcription by RNA Pol II GO:0006357.

### 5. Environmental Information
- **Environmental factors:** Not causal for MCOPS12. Gestational retinoid exposure (isotretinoin/13-cis-RA) causes retinoic-acid embryopathy — craniofacial dysmorphism, cerebellar/vermian hypoplasia, posterior-fossa anomalies, conotruncal cardiac defects, thymic aplasia, ear anomalies ([PMID: 29308367](https://pubmed.ncbi.nlm.nih.gov/29308367/); [PMID: 29843537](https://pubmed.ncbi.nlm.nih.gov/29843537/); [PMID: 34773723](https://pubmed.ncbi.nlm.nih.gov/34773723/)). Maternal vitamin-A deficiency produces overlapping malformations.
- **Lifestyle factors:** Avoidance of teratogenic retinoids and appropriate vitamin-A status in pregnancy are general public-health measures, not specific to RARB disease.
- **Infectious agents:** None — not applicable.

### 6. Mechanism / Pathophysiology
- **Molecular pathway:** Retinoic-acid nuclear-receptor signaling (Reactome "Signaling by Retinoic Acid"; GO:0048384). Suggested GO: cellular response to retinoic acid GO:0071300.
- **Cellular processes:** neural-crest cell patterning/survival; apoptosis via p53 in retinoid-excess phenocopy (GO:0006915) ([PMID: 28833556](https://pubmed.ncbi.nlm.nih.gov/28833556/)).
- **Protein dysfunction:** altered ligand-dependent transactivation (LBD) or impaired DNA binding + reduced steady-state protein + incomplete nuclear import (DBD) ([PMID: 31816153](https://pubmed.ncbi.nlm.nih.gov/31816153/)). No aggregation/misfolding mechanism.
- **Cell types (CL):** neural crest cell CL:0000333; periocular mesenchymal cells; CNS neurons/glia.
- **Causal chain:** *RARB* variant → dysregulated RA-responsive transcription (↑ GOF / ↓ or dominant-negative LOF) → abnormal neural-crest-derived periocular mesenchyme and CNS development → eye/diaphragm/heart/CNS malformation → clinical syndrome.
- **Molecular profiling:** no disease-specific transcriptomic/proteomic/metabolomic signature published for RARB patients; mechanism derives from in vitro reporter assays and animal models.

### 7. Anatomical Structures Affected
- **Primary organs:** eye (UBERON:0000970), diaphragm (UBERON:0001103), lung (UBERON:0002048), heart (UBERON:0000948), brain (UBERON:0000955).
- **Secondary/systems:** nervous (basal ganglia UBERON:0002420; cerebellum UBERON:0002037; cervicomedullary junction — Chiari I), respiratory, cardiovascular, digestive (feeding), musculoskeletal (secondary to spasticity/dystonia).
- **Tissue/cell level:** neural-crest-derived periocular mesenchyme; ocular neuroepithelium; key cell type neural crest cell (CL:0000333).
- **Subcellular:** nucleus (GO:0005634) — site of RARB action; DBD variants cause partial cytoplasmic mislocalization.
- **Laterality:** ocular involvement frequently bilateral but can be unilateral/asymmetric ([PMID: 38528322](https://pubmed.ncbi.nlm.nih.gov/38528322/)).

### 8. Temporal Development
- **Onset:** Congenital structural anomalies; neuromotor features emerge in infancy/early childhood.
- **Onset pattern:** structural defects static/congenital; movement disorder insidious and progressive.
- **Progression:** malformations non-progressive; neuromotor phenotype **progressive** ([PMID: 27120018](https://pubmed.ncbi.nlm.nih.gov/27120018/)); disease chronic and lifelong.
- **Critical period:** first-trimester organogenesis (optic fissure closure ~5th–6th gestational week; diaphragm/heart development) — the RA-sensitive window; malformations are not postnatally correctable.
- **Remission:** none.

### 9. Inheritance and Population
- **Epidemiology:** No *RARB*-specific prevalence. AMC combined prevalence up to ~30/100,000 births ([PMID: 40038803](https://pubmed.ncbi.nlm.nih.gov/40038803/)); A/M up to ~2/10,000 live births ([PMID: 35716026](https://pubmed.ncbi.nlm.nih.gov/35716026/)). MCOPS12 ultra-rare (~52+ reported).
- **Inheritance:** Autosomal dominant (most, de novo missense or truncating) and autosomal recessive (rare biallelic LOF) ([PMID: 24075189](https://pubmed.ncbi.nlm.nih.gov/24075189/); [PMID: 37321544](https://pubmed.ncbi.nlm.nih.gov/37321544/)).
- **Penetrance/expressivity:** high for dominant pathogenic alleles but variable expressivity; single recessive LOF alleles non-penetrant.
- **Anticipation:** none (no repeat expansion). **Mosaicism:** germline mosaicism possible. **Founder effect:** none; codon 387 is a recurrent hotspot, not a founder allele. **Consanguinity:** relevant only to recessive families. **Carrier frequency:** negligible (LOF alleles absent from gnomAD).
- **Demographics:** no sex bias or ethnic predilection established; presentation neonatal/pediatric.

### 10. Diagnostics
- **Molecular (definitive):** trio whole-exome or genome sequencing, or targeted AMC gene panel (RARB, STRA6, PAX6, SOX2, OTX2, CHD7). Original cases solved by WES ([PMID: 24075189](https://pubmed.ncbi.nlm.nih.gov/24075189/)); trio-WES used subsequently ([PMID: 37321544](https://pubmed.ncbi.nlm.nih.gov/37321544/)). Single-gene testing reasonable for classic phenotype + recurrent codon-387 variant.
- **Chromosomal microarray/karyotype:** typically normal; excludes CNV/aneuploidy (e.g., trisomy 13/18 cause A/M — [PMID: 38110175](https://pubmed.ncbi.nlm.nih.gov/38110175/)).
- **Imaging:** ophthalmologic exam + orbital/ocular ultrasound/MRI; brain MRI (Chiari I, posterior fossa, basal ganglia); echocardiography; chest imaging for CDH/lung hypoplasia. Prenatal ultrasound detects microphthalmia/CDH; congenital eye anomalies prenatally diagnosed in ~23.5% ([PMID: 38528322](https://pubmed.ncbi.nlm.nih.gov/38528322/)).
- **Clinical criteria:** no formal consensus criteria; diagnosis is molecular within the syndromic-microphthalmia framework.
- **Differential diagnosis:** STRA6-related Matthew-Wood/PDAC; PAX6/SOX2/OTX2/CHD7 (CHARGE) A/M; retinoic-acid embryopathy (distinguished by maternal exposure history and absence of germline RARB variant).
- **Screening:** not in newborn screening; cascade testing of relatives for known familial variants; carrier testing in recessive families.
- **MAXO:** genetic testing MAXO:0000455; MRI MAXO:0000198.

### 11. Outcome / Prognosis
- **Survival/mortality:** guarded; PDAC-overlap carries neonatal mortality from pulmonary hypoplasia and CDH (survivor-subset framing in [PMID: 27120018](https://pubmed.ncbi.nlm.nih.gov/27120018/)). No disease-specific survival curves.
- **Morbidity/function:** survivors have severe lifelong disability — visual impairment/blindness, severe developmental delay/intellectual disability, progressive spasticity/dystonia with loss of ambulation, feeding dependence.
- **Complications:** respiratory failure/pulmonary hypertension, aspiration/feeding failure, contractures, Chiari I sequelae.
- **Recovery potential:** structural malformations irreversible; supportive care improves function/comfort but not the neurodevelopmental trajectory.
- **Prognostic factors:** presence/severity of pulmonary hypoplasia + CDH (neonatal survival); severity of CNS involvement (long-term disability); GOF vs LOF and variant location may modulate severity ([PMID: 37092537](https://pubmed.ncbi.nlm.nih.gov/37092537/)).

### 12. Treatment (with suggested MAXO terms)
- **No disease-modifying therapy.** Management is supportive/multidisciplinary.
- **Ophthalmic:** serial socket expansion with acrylic conformers and ocular prostheses (~75% good outcomes; [PMID: 36257503](https://pubmed.ncbi.nlm.nih.gov/36257503/)); orbital cyst management ([PMID: 12812886](https://pubmed.ncbi.nlm.nih.gov/12812886/)). *MAXO: therapeutic procedure MAXO:0000004; prosthesis fitting.*
- **Neonatal/surgical:** CDH repair, respiratory support ± ECMO, cardiac defect management. *MAXO: surgical procedure MAXO:0000258.*
- **Neurologic:** antispasticity/antidystonic pharmacotherapy (baclofen, trihexyphenidyl, botulinum toxin for focal dystonia — symptomatic) plus physical/occupational/speech therapy. *MAXO: pharmacotherapy MAXO:0000058; physiotherapy MAXO:0000506.*
- **Gastroenterologic:** feeding support incl. gastrostomy. *MAXO: enteral feeding.*
- **Neurosurgical:** Chiari I monitoring/decompression evaluation.
- **Advanced/experimental:** no gene, cell, RNA, or targeted retinoid therapies established or in trials; no pharmacogenomic guidance; no NCT-registered disease-specific trials identified.

### 13. Prevention
- **Primary prevention:** not possible for *de novo* genetic disease. General: avoid teratogenic retinoids and vitamin-A excess/deficiency in pregnancy (addresses the phenocopy).
- **Secondary/tertiary:** early multidisciplinary intervention and surveillance (vision, feeding, respiratory, neuromotor, Chiari) to limit complications.
- **Reproductive prevention:** genetic counseling; prenatal diagnosis (fetal ultrasound for microphthalmia/CDH; molecular testing when familial variant known); preimplantation genetic testing (PGT-M).
- **Recurrence risk:** low for de novo dominant (germline mosaicism caveat); 25% for autosomal recessive families with informative carrier testing ([PMID: 37321544](https://pubmed.ncbi.nlm.nih.gov/37321544/)).
- **MAXO:** genetic counseling MAXO:0000341; prenatal diagnosis; preimplantation genetic testing.

### 14. Other Species / Natural Disease
- **Taxonomy/orthologs:** mouse *Rarb* (NCBI Gene 218772; Taxon 10090), rat *Rarb* (Taxon 10116), zebrafish *rarb/rarga* homologs (Taxon 7955). RA signaling deeply conserved.
- **Natural disease:** no well-characterized naturally occurring RARB-equivalent Mendelian disease in companion animals/wildlife (OMIA not established) — limited data.
- **Comparative biology:** RAR double-null mice recapitulate fetal VAD malformations across organs ([PMID: 7607068](https://pubmed.ncbi.nlm.nih.gov/7607068/)); mechanism is evolutionarily conserved.
- **Transmission:** non-infectious, non-zoonotic.

### 15. Model Organisms
- **Mouse (Taxon 10090):** RAR double-null mutants show multi-organ malformations recapitulating fetal VAD incl. eye and diaphragm ([PMID: 7607068](https://pubmed.ncbi.nlm.nih.gov/7607068/)); RXRα:RARβ heterodimers function in ocular mesenchyme ([PMID: 9541199](https://pubmed.ncbi.nlm.nih.gov/9541199/)); conditional pan-RAR inactivation in neural-crest-derived periocular mesenchyme alters entire eye morphogenesis with *Pitx2* as key RA target ([PMID: 18539269](https://pubmed.ncbi.nlm.nih.gov/18539269/)). *Recapitulation:* excellent for eye/diaphragm/heart malformation and mechanism; *limitation:* single *Rarb* nulls under-recapitulate the human phenotype due to redundancy, and GOF/dominant-negative alleles are not modeled by simple knockouts.
- **Zebrafish (Taxon 7955):** *rarga* morpholino knockdown causes ocular phenotypes partially rescued by human *RARB* mRNA — validates human-variant pathogenicity ([PMID: 31816153](https://pubmed.ncbi.nlm.nih.gov/31816153/)).
- **In vitro/cellular:** RARE-luciferase reporter assays classify variants as GOF vs LOF and reveal dominant-negative and localization defects ([PMID: 24075189](https://pubmed.ncbi.nlm.nih.gov/24075189/); [PMID: 27120018](https://pubmed.ncbi.nlm.nih.gov/27120018/); [PMID: 37092537](https://pubmed.ncbi.nlm.nih.gov/37092537/); [PMID: 31816153](https://pubmed.ncbi.nlm.nih.gov/31816153/)) — the principal functional model for this disease.
- **Induced (teratogen) models:** gestational retinoid/vitamin-A manipulation in rodents produces overlapping malformations ([PMID: 9272952](https://pubmed.ncbi.nlm.nih.gov/9272952/)).
- **Resources:** MGI (mouse *Rarb*), ZFIN (zebrafish), Alliance of Genome Resources, IMPC/IMSR.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports finding(s) |
|---|---|---|---|
| [24075189](https://pubmed.ncbi.nlm.nih.gov/24075189/) | Recessive and dominant *RARB* mutations in microphthalmia + diaphragmatic hernia | Human clinical + in vitro | F001, F002, F009, F010 |
| [37092537](https://pubmed.ncbi.nlm.nih.gov/37092537/) | Clinical/functional heterogeneity of *RARB* disruption | Human clinical + in vitro | F001, F002 |
| [27120018](https://pubmed.ncbi.nlm.nih.gov/27120018/) | GOF *RARB* mutations cause ID with progressive motor impairment | Human clinical (n=10 survivors) | F002, F009, F011 |
| [37321544](https://pubmed.ncbi.nlm.nih.gov/37321544/) | De novo *RARB* variant with microphthalmia and dystonia | Human clinical | F006, F011 |
| [31816153](https://pubmed.ncbi.nlm.nih.gov/31816153/) | DBD *RARB* variant affects nuclear localization | In vitro + zebrafish | F004 |
| [18539269](https://pubmed.ncbi.nlm.nih.gov/18539269/) | RA signaling in neural crest sufficient to alter eye morphogenesis | Mouse | F003 |
| [9541199](https://pubmed.ncbi.nlm.nih.gov/9541199/) | Mesectoderm a major target of RA (RXRα:RARβ) | Mouse | F003 |
| [7607068](https://pubmed.ncbi.nlm.nih.gov/7607068/) | RAR double mutants — multi-organ malformation | Mouse | F003 |
| [7923367](https://pubmed.ncbi.nlm.nih.gov/7923367/) | RXRα null — heart/eye morphogenesis | Mouse | F003 |
| [9272952](https://pubmed.ncbi.nlm.nih.gov/9272952/) | Temporal RA depletion → NC/ocular/nervous defects | Rat | F003, F007 |
| [40038803](https://pubmed.ncbi.nlm.nih.gov/40038803/) | AMC management review (prevalence, differential) | Review | F005, F010 |
| [35716026](https://pubmed.ncbi.nlm.nih.gov/35716026/) | Exome sequencing in A/M | Human clinical | F005 |
| [38528322](https://pubmed.ncbi.nlm.nih.gov/38528322/) | Prevalence and prenatal diagnosis of congenital eye anomalies | Population | F010 |
| [29308367](https://pubmed.ncbi.nlm.nih.gov/29308367/) | Retinoic acid embryopathy | Review/clinical | F007 |
| [28833556](https://pubmed.ncbi.nlm.nih.gov/28833556/) | Isotretinoin teratogenicity via p53 | Mechanistic | F007 |
| [36257503](https://pubmed.ncbi.nlm.nih.gov/36257503/) | Socket expansion with conformers | Clinical series | F008 |
| [12812886](https://pubmed.ncbi.nlm.nih.gov/12812886/) | Orbital cyst management in microphthalmos/anophthalmos | Clinical series | F008 |

The evidence base is internally consistent: independent human genetics, *in vitro* functional assays, and multiple model organisms all converge on RA-signaling dosage as the shared pathomechanism. The environmental phenocopies (retinoid excess/deficiency) provide orthogonal, causal support for the pathway rather than the gene per se.

### Supported vs Refuted Hypotheses

**Supported:**
- RARB variants cause MCOPS12 via **bidirectional** RA-signaling dysregulation (GOF and LOF/dominant-negative) — *strongly supported* ([PMID: 24075189](https://pubmed.ncbi.nlm.nih.gov/24075189/); [PMID: 27120018](https://pubmed.ncbi.nlm.nih.gov/27120018/); [PMID: 37092537](https://pubmed.ncbi.nlm.nih.gov/37092537/)).
- Disease combines congenital eye/organ malformation with a **progressive** neuromotor disorder — *supported* ([PMID: 27120018](https://pubmed.ncbi.nlm.nih.gov/27120018/)).
- Mechanism localizes to **neural-crest-derived periocular mesenchyme / RA target genes (Pitx2)** — *supported by model organisms* ([PMID: 18539269](https://pubmed.ncbi.nlm.nih.gov/18539269/); [PMID: 9541199](https://pubmed.ncbi.nlm.nih.gov/9541199/); [PMID: 7607068](https://pubmed.ncbi.nlm.nih.gov/7607068/)).
- Variant **domain/mechanism modulates phenotype** (LBD vs DBD; GOF vs LOF) — *supported* ([PMID: 31816153](https://pubmed.ncbi.nlm.nih.gov/31816153/); [PMID: 37092537](https://pubmed.ncbi.nlm.nih.gov/37092537/)).

**Refuted / not supported:**
- That RARB disease is caused by an environmental exposure — *refuted*; it is Mendelian (retinoid embryopathy is a phenocopy).
- That a single heterozygous LOF allele is sufficient for disease — *refuted*; recessive carriers are unaffected ([PMID: 37321544](https://pubmed.ncbi.nlm.nih.gov/37321544/)).
- That the disorder shows anticipation or a founder effect — *not supported* (no evidence).

---

## Limitations and Knowledge Gaps

1. **Ultra-rare disease, small N.** With only ~52+ reported individuals, frequency estimates for individual phenotypes are qualitative, and there are no *RARB*-specific prevalence, incidence, penetrance, or survival statistics.
2. **No disease-specific omics.** No transcriptomic, proteomic, metabolomic, or single-cell datasets specific to RARB MCOPS12 were identified; molecular mechanism relies on model organisms and transactivation assays.
3. **Variable expressivity poorly explained.** Modifier genes and epigenetic factors determining whether cardinal features (eye anomaly, motor impairment) appear are unknown.
4. **Movement disorder mechanism unresolved.** The progressive spasticity/dystonia in survivors is not directly modeled; the link between developmental RA dysregulation and later basal-ganglia/motor pathology is inferred, not demonstrated.
5. **Neonatal mortality not quantified.** The survivor-subset framing implies deaths but no cohort-level mortality rate exists.
6. **No natural animal disease / limited GxE data.** No spontaneous animal model (OMIA) and no formal gene–environment interaction studies for *RARB*.
7. **No validated QoL instruments** have been applied to this disorder.

---

## Proposed Follow-up Experiments / Actions

1. **Assemble a formal MCOPS12 registry** (via GeneMatcher/collaborative networks) to derive quantitative phenotype frequencies, penetrance, genotype–phenotype correlations (GOF vs LOF vs DBD vs truncating), and natural-history/survival data.
2. **Patient-derived iPSC and organoid models** (optic-cup and cerebral organoids) carrying recurrent p.Arg387Cys/Ser GOF and biallelic LOF variants to directly compare transcriptomic responses to RA and identify dysregulated target genes (e.g., *PITX2*).
3. **Single-cell transcriptomics of neural-crest-derived periocular mesenchyme** in mouse *Rarb* GOF knock-in vs conditional-null models to map cell-type-specific dysregulation and test the p53/apoptosis hypothesis.
4. **Knock-in mouse models** of the human GOF codon-387 variant to test whether the progressive movement disorder is recapitulated and to define the developmental window of vulnerability.
5. **Systematic functional classification** of all reported and future *RARB* variants using standardized transactivation and nuclear-localization assays to support ACMG classification and genotype-guided counseling.
6. **Explore pathway-level pharmacologic modulation** — in principle, RAR antagonism for GOF variants and agonism for LOF variants — in cellular/zebrafish models, with the strong caveat that structural malformations are set prenatally, so any therapeutic window is likely developmental/preventive rather than curative, and precise functional stratification would be a prerequisite.

---

### Key References (PMID)
24075189 (Srour 2013, original RARB/PDAC); 27120018 (Srour 2016, GOF + progressive motor impairment); 37092537 (Caron 2023, functional/clinical heterogeneity, n=52); 37321544 (Trieschmann 2023, dominant truncating + recessive review); 31816153 (Kalaskar 2020, DBD variant + zebrafish); 7607068 (Mendelsohn 1994, RAR double-null mice); 9541199 (Mark 1998, ocular mesenchyme); 18539269 (Matt 2008, periocular mesenchyme/Pitx2); 7923367 (RXRα null, heart/eye); 9272952 (temporal RA depletion, rat); 40038803 (Russo 2025, AMC epidemiology); 35716026 (Li 2022, A/M exome); 38528322 (Maillet 2024, prenatal detection); 38110175 (associated anomalies in A/M); 29308367 / 28833556 / 34773723 / 29843537 (retinoic-acid embryopathy); 36257503 / 12812886 (ophthalmic management).

*Report compiled from 11 confirmed findings across 5 investigation iterations and 32 reviewed papers. Evidence types span human clinical genetics, in vitro functional assays, and mouse/rat/zebrafish model organisms. All quoted material is drawn verbatim from cited PubMed abstracts.*


## Artifacts

- [OpenScientist final report](RARB-related_syndromic_microphthalmia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RARB-related_syndromic_microphthalmia-deep-research-openscientist_artifacts/final_report.pdf)
