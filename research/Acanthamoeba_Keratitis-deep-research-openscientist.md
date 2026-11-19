---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-13T19:22:22.515137'
end_time: '2026-11-13T19:38:40.655178'
duration_seconds: 978.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Acanthamoeba Keratitis
  mondo_id: MONDO:0005629
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Acanthamoeba caused keratitis; keratitis, Acanthamoeba
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: a566bb52-3d79-4876-9501-5183ead3bff4
citation_count: 42
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Acanthamoeba_Keratitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Acanthamoeba_Keratitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acanthamoeba Keratitis
- **MONDO ID:** MONDO:0005629 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Acanthamoeba caused keratitis; keratitis, Acanthamoeba
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Acanthamoeba Keratitis** covering all of the
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

# Acanthamoeba Keratitis (MONDO:0005629): A Comprehensive Disease Characteristics Report

**MONDO:** MONDO:0005629 · **Category:** Infectious Disease · **Report date:** 2026-11-14

> **Causal gene — stated up front:** Acanthamoeba keratitis (AK) is **not a genetic/Mendelian disease and has no human causal gene.** It is an **infectious disease** caused by free-living protozoa of the genus ***Acanthamoeba*** (phylum Amoebozoa; predominant genotype **T4**, ~66% of isolates). The template's "Causal gene(s): not recorded / OMIM: not recorded" is therefore correct and expected. Where this report cites "genes," they are **host immune-susceptibility *modifier* genes** (e.g., *CXCL8/IL-8*, *TLR4*, *IL17A*, *CLEC4E*) or **parasite virulence genes/proteins** (e.g., mannose-binding protein, MIP-133) — none is a germline cause of disease.

---

## Summary

Acanthamoeba keratitis is a sight-threatening, painful infection of the cornea caused by free-living *Acanthamoeba* protozoa, with genotype **T4** accounting for roughly two-thirds of clinical and environmental isolates. Because the etiology is infectious rather than Mendelian, there is no OMIM gene entry, no causal variant, and no inheritance pattern; the identifiers that anchor this entry are **MONDO:0005629**, MeSH "Acanthamoeba Keratitis," and **ICD-10 B60.12 / ICD-11 1F56**. Host immune-gene polymorphisms (CXCL8/IL-8, TLR4, Th17-pathway genes) modify disease *severity* but not susceptibility.

AK is overwhelmingly a disease of **contact-lens wearers** (≈85–90% of cases in developed countries), acquired through water exposure, poor lens hygiene, and practices such as rinsing/storing lenses in tap water, "topping-off" solution, and swimming or showering in lenses. The pathogenic cascade runs from parasite adhesion to the corneal epithelium via a **mannose-binding protein (MBP)**, through secretion of a **mannose-induced 133-kDa protease (MIP-133)** and other proteases that drive corneal-cell apoptosis and stromal matrix degradation, to intense innate/adaptive inflammation (the hallmark **ring infiltrate** and **radial keratoneuritis**), and the formation of **drug-resistant double-walled cysts** that make the disease chronic and difficult to cure.

Clinically, AK presents with **severe ocular pain disproportionate to clinical signs**, photophobia, and redness, and is frequently misdiagnosed early as **herpes simplex keratitis** (≈20% of cases), causing diagnostic delay of 3–4 weeks. Diagnosis relies on **in vivo confocal microscopy (IVCM)** and **18S rRNA PCR** (both far more sensitive than culture). Treatment is **prolonged topical cysticidal biguanide therapy** (PHMB or chlorhexidine), increasingly as higher-concentration **PHMB 0.08% monotherapy** (now the first specifically approved AK drug, marketed as Akantior), often with an aromatic diamidine; refractory/advanced cases require therapeutic keratoplasty (needed in ≈30–47% in various cohorts). Prevention is entirely behavioral. AK is rarely fatal (confined to the cornea) but is a major cause of unilateral corneal blindness, and its global incidence is rising with increasing contact-lens use.

---

## Key Findings

### Finding 1 — AK is an infectious, non-genetic corneal disease; contact-lens wear dominates risk

Acanthamoeba keratitis has **no human causal gene**. The etiologic agent is the free-living amoeba *Acanthamoeba* (genotype **T4 predominant**, ~66% of environmental and clinical isolates; [PMID: 34453084](https://pubmed.ncbi.nlm.nih.gov/34453084/): *"the most predominant genotype T4 found in 87 isolates (66.4%)"*). The dominant risk factor is contact-lens wear. In the **UK 2015 prospective national survey**, 124 AK cases gave an overall incidence of **2.35 per million**, with contact-lens wearers accounting for **108/124 (87%)** and an incidence among lens wearers of **26.94 per million** ([PMID: 38097200](https://pubmed.ncbi.nlm.nih.gov/38097200/)). Risk varied sharply by lens type: planned-replacement soft lens wearers had an incidence of **50.65 per million — 7-fold higher** than daily-disposable users (7.24 per million).

A large **Netherlands case-control study** (220 cases / 1020 controls) quantified acquisition risk factors ([PMID: 42393849](https://pubmed.ncbi.nlm.nih.gov/42393849/): *"Identified risk factors were previous eye injury (OR: 16.0, 95%CI: 3.4-76.7), occupational/recreational surface water contact (OR: 9.1, 95%CI: 3.5-23.2), cleaning/rinsing CLs with tap water (OR: 3.3, 95%CI: 1.7-6.4), cigarette smoke exposure (OR: 1.9, 95%CI: 1.1-3.5) and napping in CLs (OR: 1.9, 95%CI: 1.0-3.6)."*). In pediatric **orthokeratology** wearers, inadequate hand hygiene (OR 26.46, 3.29–212.79) and "topping-off" solution (OR 17.40, 2.03–149.34) were the strongest modifiable risks ([PMID: 42442142](https://pubmed.ncbi.nlm.nih.gov/42442142/)).

| Risk factor | Odds ratio (95% CI) | Source |
|---|---|---|
| Previous eye injury | 16.0 (3.4–76.7) | Netherlands [PMID: 42393849] |
| Surface-water contact | 9.1 (3.5–23.2) | Netherlands [PMID: 42393849] |
| Rinsing lenses with tap water | 3.3 (1.7–6.4) | Netherlands [PMID: 42393849] |
| Cigarette smoke exposure | 1.9 (1.1–3.5) | Netherlands [PMID: 42393849] |
| Napping in lenses | 1.9 (1.0–3.6) | Netherlands [PMID: 42393849] |
| Inadequate hand hygiene (ortho-k) | 26.46 (3.29–212.79) | Ortho-k [PMID: 42442142] |
| Topping-off solution (ortho-k) | 17.40 (2.03–149.34) | Ortho-k [PMID: 42442142] |

### Finding 2 — Pathogenesis causal chain: MBP adhesion → MIP-133 protease → cytopathic effect, apoptosis, matrix degradation

The first critical step is **adhesion** of trophozoites to the corneal epithelium via the amoebic **mannose-binding protein (MBP)**. Adhesion triggers secretion of a **contact-dependent metalloproteinase** plus **contact-independent serine proteinases** that kill host cells and degrade the basement membrane and stromal matrix ([PMID: 20427010](https://pubmed.ncbi.nlm.nih.gov/20427010/): *"Acanthamoebae express a major virulence protein, the mannose-binding protein (MBP), which mediates the adhesion of amoebae to the surface of the cornea... the amoebae produce a contact-dependent metalloproteinase and several contact-independent serine proteinases."*).

A mannose-induced **133-kDa protease (MIP-133)** facilitates corneal invasion and **induces apoptosis** via the **cytosolic phospholipase A2α (cPLA2α)** pathway with caspase-3 activation ([PMID: 23132804](https://pubmed.ncbi.nlm.nih.gov/23132804/): *"stimulates trophozoites to secrete a mannose-induced 133 kDa protease (MIP-133), which facilitates corneal invasion and induces apoptosis"*). A purified **33-kDa serine proteinase** shows cytopathic effects on HCE cells, blocked by PMSF, correlating with strain virulence ([PMID: 17170574](https://pubmed.ncbi.nlm.nih.gov/17170574/)). Notably, **cysts induce greater cytotoxicity and pro-inflammatory cytokine release than trophozoites** ([PMID: 31284343](https://pubmed.ncbi.nlm.nih.gov/31284343/): *"A. castellanii induced the expression of IL-1α, IL-6, IL-8, and CXCL1 in HCECs"*).

### Finding 3 — Diagnosis: IVCM and 18S rRNA PCR outperform culture; frequent misdiagnosis as herpes

In a 42-patient study, sensitivities were **nested PCR 96.3%, IVCM 77.78%, one-step PCR 62.96%, culture 37.04%**, with specificity and PPV of 100% for all tests ([PMID: 41588033](https://pubmed.ncbi.nlm.nih.gov/41588033/): *"the sensitivity of IVCM, culture, PCR, and nested PCR was 77.78%, 37.04%, 62.96%, and 96.3%, respectively. The specificity and positive predictive values were 100% for all the tests."*). IVCM reveals **double-walled hyperreflective cysts**; PCR/sequencing targets the **18S rRNA gene**. Diagnostic delay is a defining problem: **herpes simplex keratitis was the initial misdiagnosis in 20.2% (25/124)** of UK cases ([PMID: 38097200](https://pubmed.ncbi.nlm.nih.gov/38097200/): *"Herpes keratitis was initially misdiagnosed in 25 of 124 cases (20.2%)."*). Multiplex PCR can yield **false positives** in patients lacking classic risk factors ([PMID: 42949848](https://pubmed.ncbi.nlm.nih.gov/42949848/)).

| Diagnostic test | Sensitivity | Specificity / PPV |
|---|---|---|
| Nested PCR (18S rRNA) | 96.3% | 100% |
| In vivo confocal microscopy | 77.8% | 100% |
| One-step PCR | 63.0% | 100% |
| Culture (non-nutrient agar) | 37.0% | 100% |

### Finding 4 — Treatment: prolonged biguanide ± diamidine; PHMB 0.08% monotherapy and protocol delivery improve cure

The mainstay is **prolonged combination therapy with topical biguanides (PHMB or chlorhexidine) and aromatic diamidines**, with growing evidence for **PHMB 0.08% monotherapy** ([PMID: 42262140](https://pubmed.ncbi.nlm.nih.gov/42262140/): *"prolonged combination therapy with topical biguanides and aromatic diamidines remains the mainstay of treatment. However, recent evidence supports the use of topical biguanide monotherapy (in higher concentrations) in AK with comparable outcomes to combination treatment."*). An indirect comparison found 12-month clinical resolution of **84.8% for PHMB 0.08%** versus 43.6% for any anti-amoebic, 55.0% for PHMB 0.02%+diamidine, and 40.0% for chlorhexidine ± diamidine ([PMID: 40659372](https://pubmed.ncbi.nlm.nih.gov/40659372/)). **Protocol-based delivery** gave a **1.59-fold higher medical cure rate** vs individualized treatment (95% CI 1.40–1.80, p<0.001) ([PMID: 40204130](https://pubmed.ncbi.nlm.nih.gov/40204130/)).

| Regimen | 12-month clinical resolution rate |
|---|---|
| PHMB 0.08% monotherapy | 84.8% |
| PHMB 0.02% + diamidine | 55.0% |
| Any anti-amoebic treatment | 43.6% |
| Chlorhexidine 0.02% ± diamidine | 40.0% |

### Finding 5 — Clinical phenotype: severe pain out of proportion to signs, ring infiltrate, radial keratoneuritis

Hallmark features are **severe ocular pain disproportionate to clinical findings**, photophobia, and treatment-resistant cysts ([PMID: 42885963](https://pubmed.ncbi.nlm.nih.gov/42885963/): *"characterized by severe pain disproportionate to clinical findings and the presence of cyst forms that confer significant treatment resistance."*). Characteristic signs include a **ring-shaped stromal infiltrate** and **radial keratoneuritis**. **Hypopyon is uncommon in pure AK** and, when present, often signals fungal coinfection with worse prognosis ([PMID: 42685305](https://pubmed.ncbi.nlm.nih.gov/42685305/): *"AK with hypopyon can be a representative sign of fungal coinfection, which has a trend of a worse visual prognosis."*). Most cases are **unilateral**; bilateral disease is rare.

### Finding 6 — Prognosis: ~30–47% require keratoplasty; older age, longer symptom duration, ring infiltrate predict poor outcome

In a 51-eye cohort, **15/51 (29.4%) required therapeutic keratoplasty**; predictors were older age (OR 1.09/yr) and longer symptom duration (OR 1.03/day) ([PMID: 42301488](https://pubmed.ncbi.nlm.nih.gov/42301488/): *"Fifteen eyes (29.4%) required TK... older age at diagnosis (OR 1.09; 95% CI 1.03-1.16; p = 0.005) and longer symptom duration (OR 1.03; 95% CI 1.01-1.05; p = 0.011) were associated with TK."*). In the Netherlands cohort, **treatment failure occurred in 85/179 (47%)** and globe loss in 5% ([PMID: 42393849](https://pubmed.ncbi.nlm.nih.gov/42393849/)). The Danish genotyped cohort confirmed poor-outcome predictors (pre-diagnosis corticosteroids, moderate-severe pain, male sex, older age, ring infiltration, infiltrate >3 mm) while **genotype did not predict outcome** ([PMID: 40387241](https://pubmed.ncbi.nlm.nih.gov/40387241/)).

### Finding 7 — Host immune-gene polymorphisms modify severity

In 105 AK cases (38% with severe inflammatory complications), **CXCL8 (IL-8) SNPs were protective** (rs1126647 OR=0.3, p=0.005), **two TLR4 SNPs increased risk** (both OR=6.9, p=0.01), and **Th17 SNPs** (IL23R, IL1B, IL22) were associated with complications ([PMID: 33755043](https://pubmed.ncbi.nlm.nih.gov/33755043/)). In mouse models, **IL-17A is protective** ([PMID: 25505284](https://pubmed.ncbi.nlm.nih.gov/25505284/): *"corneal Acanthamoeba infection induces IL-17A expression and that IL-17A is critical for host protection against severe AK pathology"*). The C-type lectin receptor **CLEC4E (Mincle)** mediates protective macrophage NF-κB activation ([PMID: 42929688](https://pubmed.ncbi.nlm.nih.gov/42929688/)).

### Finding 8 — Model organisms and vaccine proof-of-concept

The **Chinese hamster** model develops AK via *A. castellanii*-laden lenses; **oral MBP immunization ameliorates disease** with elevated anti-MBP tear IgA ([PMID: 16982837](https://pubmed.ncbi.nlm.nih.gov/16982837/): *"oral immunization with recombinant MBP ameliorates AK in a hamster animal model and that this protection is associated with the presence of elevated levels of anti-MBP immunoglobulin A in the tear fluid..."*). Oral **MIP-133/aPA–cholera toxin** immunization confers additive protection ([PMID: 18055809](https://pubmed.ncbi.nlm.nih.gov/18055809/)). The **mouse corneal model** dissects IL-17A, DECTIN-1, and CLEC4E immunity.

### Finding 9 — Etiologic agent: *Acanthamoeba* spp. with trophozoite and resistant cyst stages

*Acanthamoeba* is ubiquitous in tap water, soil, and pools ([PMID: 39764873](https://pubmed.ncbi.nlm.nih.gov/39764873/): *"Acanthamoeba castellanii is a widespread unicellular eukaryote found in diverse environments, including tap water, soil, and swimming pools."*). The **dormant, double-walled cyst** is highly drug-resistant; encystation involves **global metabolic downregulation** ([PMID: 40738523](https://pubmed.ncbi.nlm.nih.gov/40738523/): *"a global metabolic downregulation during encystation, which is consistent with a state of dormancy. Components of the cyst wall such as cellobiose and lactose accumulated in the final phase."*) and **autophagy** ([PMID: 25896709](https://pubmed.ncbi.nlm.nih.gov/25896709/)). *Acanthamoeba* can act as a **"Trojan horse"** for intracellular bacteria ([PMID: 23444840](https://pubmed.ncbi.nlm.nih.gov/23444840/)).

### Finding 10 — Temporal course: epithelial-stage onset progressing to stromal ring infiltrate

AK begins as **superficial epitheliopathy** progressing to the stroma ([PMID: 35402748](https://pubmed.ncbi.nlm.nih.gov/35402748/)). Early signs can be subtle/atypical, promoting herpes misdiagnosis ([PMID: 34348354](https://pubmed.ncbi.nlm.nih.gov/34348354/)). In the mouse model, temporal transcriptomics showed **peak inflammation at 3 days post-infection**, early innate then adaptive immunity, with DECTIN-1/NF-κB throughout ([PMID: 42872947](https://pubmed.ncbi.nlm.nih.gov/42872947/): *"AK progression was characterized by dynamic changes, with peak inflammatory responses at 3 dpi. Immune infiltration analysis revealed early innate immune activation followed by adaptive immune involvement at later stages."*).

### Finding 11 — Demographics: bimodal age, male predominance, tap-water lens exposure

The CDC multistate study (88 cases/151 controls) found cases more likely aged **<25 (mOR 2.7) or >53 (mOR 2.5)** and **male (mOR 2.6)** ([PMID: 28099282](https://pubmed.ncbi.nlm.nih.gov/28099282/): *"Case patients were more likely to be aged <25 years (unadjusted mOR 2.7, 95% confidence interval 1.3-5.5) or aged >53 years (mOR 2.5, 1.1-5.7), and more likely to be men (mOR 2.6, 1.4-4.8)."*). The Chicago outbreak cohort reported mean age 28±15, 52.5% men, 95% lens wearers ([PMID: 16876498](https://pubmed.ncbi.nlm.nih.gov/16876498/)).

### Finding 12 — *Acanthamoeba* also causes GAE and cross-species disease

Beyond keratitis, *Acanthamoeba* causes **granulomatous amebic encephalitis (GAE)**, a rare, nearly universally fatal CNS infection in immunocompromised hosts ([PMID: 42158383](https://pubmed.ncbi.nlm.nih.gov/42158383/): *"Granulomatous amebic encephalitis (GAE) is a rare but frequently fatal infection of the central nervous system..."*). AK itself is confined to the cornea and rarely fatal. Naturally occurring AK has been documented in **wild birds** ([PMID: 28807756](https://pubmed.ncbi.nlm.nih.gov/28807756/): *"Acanthamoeba infection was detected in wild bird cornea samples with/without keratitis for the first time in the world."*).

### Finding 13 — Rising global incidence; emerging adjunctive therapies

AK has *"evolved from an extraordinarily rare disease to a significant public health concern, with increasing global incidence"* ([PMID: 41111636](https://pubmed.ncbi.nlm.nih.gov/41111636/)). **PHMB 0.08% (Akantior)** is the first approved AK drug (90.9% resolution in a Polish cohort, [PMID: 42961683](https://pubmed.ncbi.nlm.nih.gov/42961683/)). Adjuncts include voriconazole, miltefosine, and **PACK-CXL** ([PMID: 39748383](https://pubmed.ncbi.nlm.nih.gov/39748383/): *"The same-session combination of riboflavin/UV-A and rose bengal/green light PACK-CXL effectively treated a patient with confirmed AK that was resistant to conventional medical therapy"*; [PMID: 42348670](https://pubmed.ncbi.nlm.nih.gov/42348670/)). Refractory T4 cases can still progress to **phthisis bulbi** ([PMID: 41526733](https://pubmed.ncbi.nlm.nih.gov/41526733/)).

---

## Section-by-Section Report

### 1. Disease Information

AK is a sight-threatening, painful corneal infection caused by *Acanthamoeba*. Key identifiers: **MONDO:0005629**; MeSH "Keratitis, Acanthamoeba"; **ICD-10 B60.12**; **ICD-11 1F56**. No OMIM entry (non-genetic). Synonyms: *Acanthamoeba caused keratitis*, *keratitis, Acanthamoeba*, amoebic keratitis. Information is derived from **aggregated disease-level resources** (surveillance surveys, case-control studies, case series), not single-patient EHR.

### 2. Etiology

**Causal factor: infectious** — *Acanthamoeba* spp. (T4 predominant); **no genetic cause**. **Environmental risks**: contact-lens wear (dominant), water exposure of lenses, poor hygiene, topping-off, trauma, hard domestic water, smoke exposure (Findings 1, 11). **Host genetic *modifiers*** (not causes): protective CXCL8/IL-8, risk-increasing TLR4/Th17 (Finding 7). **Protective factors**: daily-disposable lenses, strict hygiene; mucosal IgA and milk proteinase inhibitors reduce cytopathic effect in vitro ([PMID: 18326724](https://pubmed.ncbi.nlm.nih.gov/18326724/)). **Gene–environment interaction**: host immune background tunes the *severity* of inflammation to an environmentally acquired infection.

### 3. Phenotypes

| Phenotype | Type | Frequency/severity | HPO suggestion |
|---|---|---|---|
| Severe pain disproportionate to signs | Symptom | Very frequent; severe | eye pain |
| Photophobia | Symptom | Frequent | HP:0000613 |
| Ring stromal infiltrate | Clinical sign | Common; severity marker | HP:0200136 (keratitis) |
| Radial keratoneuritis | Clinical sign | Characteristic/early | — |
| Reduced visual acuity | Sign | Frequent | HP:0000572 / HP:0000505 |
| Conjunctival hyperemia (redness) | Sign | Frequent | HP:0000532 |
| Epitheliopathy / pseudodendrites | Sign | Early stage | — |

Onset is **adult** (contact-lens wearers, 20–40), bimodal peaks <25 and >53. Progression is **progressive if untreated**. QoL impact is substantial: chronic pain, months-long therapy, vision loss ([PMID: 33151784](https://pubmed.ncbi.nlm.nih.gov/33151784/)).

### 4. Genetic/Molecular Information

**Not applicable as a causal mechanism** — no human causal gene, no pathogenic variants, no chromosomal abnormality, no inheritance. The only relevant human genetics are **severity modifiers** (CXCL8/IL-8 protective; TLR4, IL23R, IL1B, IL22 risk — Finding 7). The pathogen's molecular determinants (MBP, MIP-133, serine proteases, cyst-wall genes) are the functional molecular information (Findings 2, 9).

### 5. Environmental Information

**Environmental agents**: waterborne *Acanthamoeba* (tap water, pools, soil, biofilms). **Lifestyle**: contact-lens wear/hygiene; smoking is associated ([PMID: 42393849](https://pubmed.ncbi.nlm.nih.gov/42393849/)). **Infectious agent**: *Acanthamoeba* spp. (NCBI taxid 5754), T4 predominant; can co-infect with bacteria/fungi.

### 6. Mechanism / Pathophysiology — Causal Chain

```
1. Environmental exposure: Acanthamoeba trophozoites/cysts contact the ocular surface
   (contaminated contact lens, water, or trauma)
        │ leads to
2. ADHESION: amoebic mannose-binding protein (MBP) binds mannosylated corneal
   epithelial glycoproteins (facilitated by lens-related epithelial microtrauma)
        │ triggers
3. PROTEASE SECRETION: MIP-133 (133 kDa), a contact-dependent metalloproteinase,
   and contact-independent serine proteinases (e.g., 33 kDa)
        │ results in (branch)
   ├─4a. HOST-CELL DEATH: MIP-133 → cPLA2α → arachidonic acid → caspase-3 →
   │      apoptosis of corneal epithelial cells; direct cytopathic effect
   └─4b. MATRIX DEGRADATION: proteases digest basement membrane, laminin/fibronectin,
          stromal collagen → amoebic invasion into deep stroma
        │ provokes
5. INFLAMMATION: damaged epithelium + cysts release IL-1α/β, IL-6, IL-8/CXCL8, CXCL1;
   PRRs (DECTIN-1, CLEC4E/Mincle) → SYK/NF-κB (peak ~3 dpi in model);
   neutrophil then CD4+ Th17 (IL-17A protective) infiltration
        │ manifests as
6. CLINICAL DISEASE: radial keratoneuritis (perineural invasion) + ring stromal
   infiltrate, severe pain disproportionate to signs, photophobia, epithelial defects
        │ sustained by
7. CHRONICITY/RESISTANCE: trophozoites encyst (autophagy-dependent) into double-walled,
   dormant, drug-resistant cysts → relapse, prolonged therapy, stromal necrosis
        │ can progress to
8. OUTCOME: scarring, melting/perforation → therapeutic keratoplasty,
   or phthisis bulbi/vision loss in refractory cases
```

**Molecular pathways**: cPLA2α–arachidonic acid–caspase-3 apoptosis; SYK–NF-κB inflammation downstream of DECTIN-1/CLEC4E; HIF-1α amplification. **Cellular processes (GO)**: apoptotic process (GO:0006915), inflammatory response (GO:0006954), autophagy (GO:0006914, parasite), proteolysis (GO:0006508), extracellular matrix disassembly (GO:0022617). **Cell types (CL)**: corneal epithelial cell (CL:0000575), keratocyte (CL:0002363), macrophage (CL:0000235), neutrophil (CL:0000775), Th17 cell (CL:0000899). Upstream events are parasite adhesion/proteolysis; downstream events are host inflammation and tissue destruction.

### 7. Anatomical Structures Affected

**Primary organ**: cornea (UBERON:0000964), eye (UBERON:0000970). **Tissues**: corneal epithelium (UBERON:0001772), corneal stroma (UBERON:0001777), corneal nerves; occasionally sclera. **Cells**: corneal epithelial cells (CL:0000575), keratocytes (CL:0002363). **Subcellular (GO CC)**: plasma membrane, cytosol, extracellular region. **Localization**: central/paracentral cornea; **usually unilateral**. Secondary: anterior chamber inflammation, hypopyon (often signaling coinfection), globe loss in extreme cases.

### 8. Temporal Development

**Onset**: adult, acute-to-subacute. **Stages**: I epithelial/limbitis → II–III stromal (ring infiltrate) → late ring/perforation; most present at stage ≥II. **Duration**: often months (Icelandic 5–24 months; Polish mean 188 days to resolution). **Critical window**: early diagnosis and cysticidal therapy before stromal/ring involvement drives good outcomes (Findings 6, 10).

### 9. Inheritance and Population

**Epidemiology**: 1–2.35 per million general population; ~17–27 per million among lens wearers (UK) with marked geographic variation (higher in hard-water regions; [PMID: 11973250](https://pubmed.ncbi.nlm.nih.gov/11973250/)). **Inheritance: none (infectious)** — penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, carrier frequency are **not applicable**. **Demographics**: predominantly young adult lens wearers (20–40), bimodal peaks <25 and >53, slight male predominance; rising global incidence.

### 10. Diagnostics

**Clinical/lab**: corneal scraping with non-nutrient agar culture (low sensitivity ~37%); **18S rRNA / nested PCR** (up to 96%); **IVCM** (double-walled cysts, ~78%); AS-OCT; histopathology (PAS/calcofluor white). **Parasite genotyping** by 18S rRNA sequencing (T4 predominant). **Clinical criteria**: compatible history + disproportionate pain + characteristic signs + micro/IVCM confirmation. **Differential diagnosis**: herpes simplex keratitis (commonest misdiagnosis), fungal, bacterial. Multiplex PCR false positives require clinical correlation ([PMID: 42949848](https://pubmed.ncbi.nlm.nih.gov/42949848/)). **Screening**: none; prevention is behavioral.

### 11. Outcome/Prognosis

**Rarely fatal**; high morbidity (chronic pain, scarring, vision loss). Keratoplasty in **~29–47%**; globe loss ~5%. **Prognostic factors**: older age, longer symptom duration/diagnostic delay, ring infiltrate, infiltrate >3 mm, pre-diagnosis corticosteroids, male sex; genotype not prognostic. Historical pre-propamidine medical cure was only 19.6% vs much improved modern outcomes ([PMID: 40323557](https://pubmed.ncbi.nlm.nih.gov/40323557/)).

### 12. Treatment

**Pharmacotherapy (NCIT-type intervention terms)**: topical **biguanides** — PHMB/polihexanide 0.02%–0.08%, **chlorhexidine** 0.02%–0.2%; **aromatic diamidines** — propamidine isethionate 0.1%, hexamidine. **PHMB 0.08% (Akantior)** is the first approved AK drug, effective as monotherapy. **Adjuncts**: voriconazole, **miltefosine**, povidone-iodine, antimicrobial peptides, **PACK-CXL** for refractory disease. Corticosteroids used cautiously. **Surgical**: therapeutic/penetrating keratoplasty for refractory/perforating disease. **Strategy**: protocol-based dual-therapy dosing improves cure 1.59-fold ([PMID: 40204130](https://pubmed.ncbi.nlm.nih.gov/40204130/)). Pharmacogenomics: not established.

### 13. Prevention

Entirely **behavioral/primary**: contact-lens hygiene, **avoid water (tap/pool/shower/swim) contact with lenses**, no topping-off, hand hygiene, timely case replacement, prefer daily-disposables, prompt evaluation of ocular discomfort ([PMID: 42442142](https://pubmed.ncbi.nlm.nih.gov/42442142/), [PMID: 28099282](https://pubmed.ncbi.nlm.nih.gov/28099282/)). **Secondary**: early recognition to avoid herpes misdiagnosis/delay. **Public health**: patient/practitioner education; water-management awareness. No human vaccine (animal MBP/MIP-133 immunization is protective — Finding 8).

### 14. Other Species / Natural Disease

**Pathogen taxonomy**: *Acanthamoeba* spp. (NCBI taxid 5754). **Natural disease**: AK in **wild birds** (Eurasian sparrowhawk, *Accipiter nisus*; T4/T5) ([PMID: 28807756](https://pubmed.ncbi.nlm.nih.gov/28807756/)); *Acanthamoeba* also causes GAE/disseminated disease across animals. **No Mendelian animal homolog** (OMIA not applicable). **Transmission**: environmentally acquired; **not zoonotic**.

### 15. Model Organisms

**Chinese hamster (*Cricetulus griseus*)** — contact-lens corneal infection; oral MBP/MIP-133/aPA immunization studies ([PMID: 16982837](https://pubmed.ncbi.nlm.nih.gov/16982837/), [PMID: 18055809](https://pubmed.ncbi.nlm.nih.gov/18055809/)). **Mouse** — corneal intrastromal-injection model; IL-17A ([PMID: 25505284](https://pubmed.ncbi.nlm.nih.gov/25505284/)), DECTIN-1 ([PMID: 42872947](https://pubmed.ncbi.nlm.nih.gov/42872947/)), CLEC4E ([PMID: 42929688](https://pubmed.ncbi.nlm.nih.gov/42929688/)). **In vitro**: HCEC, MDCK monolayers, ex vivo cornea. **Recapitulation**: reproduce corneal infection, protease cytopathology, inflammation, and (hamster) protective mucosal immunity. **Limitations**: corneal anatomy/immunity differ from humans; models do not fully reproduce chronic cyst-driven relapse.

---

## Mechanistic Model / Interpretation

AK is best understood as a **two-phase infectious process**: an initial *parasite-driven cytopathic phase* (adhesion → proteolysis → apoptosis and matrix destruction) followed by a *host inflammatory phase* (PRR-driven NF-κB inflammation, neutrophil and Th17 responses) that produces the ring infiltrate and much of the tissue damage. The **cyst stage** is the linchpin of clinical difficulty: its dormant metabolism and resistant double wall explain treatment failure, prolonged therapy, and relapse. Host genetics tune the *intensity* of phase two but do not determine *whether* infection occurs — that is set by environmental exposure and lens hygiene.

The clinical corollaries all flow from this model: (1) **early diagnosis matters** because intervention during the epithelial phase yields the best outcomes; (2) **cysticidal biguanides** are first-line because they act on the resistant cyst; (3) **corticosteroids before diagnosis worsen outcomes** by suppressing protective immunity while the parasite persists; and (4) **prevention is behavioral** because exposure, not the genome, is modifiable.

---

## Evidence Base

| PMID | Role | Key contribution |
|---|---|---|
| [38097200](https://pubmed.ncbi.nlm.nih.gov/38097200/) | Supports F1, F3 | UK national incidence; lens risk gradient; 20.2% herpes misdiagnosis |
| [42393849](https://pubmed.ncbi.nlm.nih.gov/42393849/) | Supports F1, F6 | Acquisition risk ORs; 47% treatment failure; prognostic factors |
| [34453084](https://pubmed.ncbi.nlm.nih.gov/34453084/) | Supports F1, F9 | T4 genotype predominance (66.4%) |
| [20427010](https://pubmed.ncbi.nlm.nih.gov/20427010/) | Supports F2 | MBP adhesion and protease cascade |
| [23132804](https://pubmed.ncbi.nlm.nih.gov/23132804/) | Supports F2 | MIP-133, cPLA2α apoptosis |
| [31284343](https://pubmed.ncbi.nlm.nih.gov/31284343/) | Supports F2 | Cytokine induction; cysts more cytopathic |
| [41588033](https://pubmed.ncbi.nlm.nih.gov/41588033/) | Supports F3 | Head-to-head diagnostic sensitivities |
| [40659372](https://pubmed.ncbi.nlm.nih.gov/40659372/) | Supports F4 | Comparative clinical resolution rates |
| [42262140](https://pubmed.ncbi.nlm.nih.gov/42262140/) | Supports F4, F13 | Mainstay + monotherapy; emerging therapies |
| [40204130](https://pubmed.ncbi.nlm.nih.gov/40204130/) | Supports F4 | Protocol delivery improves cure 1.59× |
| [42885963](https://pubmed.ncbi.nlm.nih.gov/42885963/) | Supports F5 | Disproportionate pain; cyst resistance |
| [42685305](https://pubmed.ncbi.nlm.nih.gov/42685305/) | Supports F5 | Hypopyon signals fungal coinfection |
| [42301488](https://pubmed.ncbi.nlm.nih.gov/42301488/) | Supports F6 | Keratoplasty rate; TK predictors |
| [40387241](https://pubmed.ncbi.nlm.nih.gov/40387241/) | Supports F6 | Clinical predictors; genotype not prognostic |
| [33755043](https://pubmed.ncbi.nlm.nih.gov/33755043/) | Supports F7 | Host immune-gene SNP modifiers |
| [25505284](https://pubmed.ncbi.nlm.nih.gov/25505284/) | Supports F7, F15 | IL-17A protective (mouse) |
| [42929688](https://pubmed.ncbi.nlm.nih.gov/42929688/) | Supports F7, F15 | CLEC4E/HIF-1α macrophage defense |
| [16982837](https://pubmed.ncbi.nlm.nih.gov/16982837/) | Supports F8 | Hamster model; MBP oral immunization |
| [18055809](https://pubmed.ncbi.nlm.nih.gov/18055809/) | Supports F8 | MIP-133/aPA immunization |
| [39764873](https://pubmed.ncbi.nlm.nih.gov/39764873/) | Supports F9 | Environmental ubiquity |
| [40738523](https://pubmed.ncbi.nlm.nih.gov/40738523/) | Supports F9 | Encystation metabolic dormancy |
| [35402748](https://pubmed.ncbi.nlm.nih.gov/35402748/) | Supports F10 | Epithelial-stage disease |
| [42872947](https://pubmed.ncbi.nlm.nih.gov/42872947/) | Supports F10 | DECTIN-1 temporal immunity (3 dpi peak) |
| [28099282](https://pubmed.ncbi.nlm.nih.gov/28099282/) | Supports F11 | CDC demographics & modifiable risk |
| [16876498](https://pubmed.ncbi.nlm.nih.gov/16876498/) | Supports F11 | Chicago outbreak demographics |
| [42158383](https://pubmed.ncbi.nlm.nih.gov/42158383/) | Supports F12 | GAE (fatal CNS form) |
| [28807756](https://pubmed.ncbi.nlm.nih.gov/28807756/) | Supports F12 | AK in wild birds |
| [41111636](https://pubmed.ncbi.nlm.nih.gov/41111636/) | Supports F13 | Rising global incidence |
| [39748383](https://pubmed.ncbi.nlm.nih.gov/39748383/) | Supports F13 | PACK-CXL for refractory AK |
| [42348670](https://pubmed.ncbi.nlm.nih.gov/42348670/) | Supports F13 | Adjunctive therapies |

---

## Limitations and Knowledge Gaps

1. **Observational evidence base.** Most epidemiology/prognosis data come from case series and case-control studies, susceptible to referral and recall bias; randomized treatment trials remain few (ODAK is a notable exception).
2. **No universally adopted staging or diagnostic guidelines**, contributing to diagnostic delay and heterogeneous outcome reporting.
3. **Cyst biology** — molecular triggers and regulatory networks of encystation/excystation are incompletely defined, limiting rational cysticidal drug design.
4. **Host-genetics modifiers** rest largely on a single ~105-patient study and animal models; need replication in larger, diverse cohorts.
5. **No human vaccine** despite promising animal proof-of-concept; translation barriers unaddressed.
6. **Molecular false positives** (multiplex PCR) and the absence of validated viability assays complicate diagnosis and test-of-cure.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective multicenter registry** with standardized staging, genotyping, and outcome definitions to firm up prognostic models and treatment comparisons.
2. **Randomized trials** comparing PHMB 0.08% monotherapy vs combination regimens and quantifying adjunct value (miltefosine, PACK-CXL) in refractory disease.
3. **Replication of host immune-gene associations** (CXCL8, TLR4, Th17) with functional validation.
4. **Cyst-targeted drug discovery** leveraging encystation metabolomics/autophagy dependence; develop **viability PCR / cyst-viability assays** for test-of-cure.
5. **Diagnostic standardization**: validate AI-assisted IVCM and metagenomic sequencing; define criteria to avoid multiplex-PCR false positives.
6. **Translational vaccine work**: advance MBP/MIP-133 mucosal immunization toward human-relevant platforms; evaluate prophylaxis in high-risk lens wearers.
7. **Public-health intervention trials** on lens-hygiene education and water-avoidance, especially in hard-water regions and pediatric ortho-k populations.


## Artifacts

- [OpenScientist final report](Acanthamoeba_Keratitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Acanthamoeba_Keratitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 42 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 42 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 15 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005629` (5 mentions) - the report calls it "if available"; MONDO calls it **Acanthamoeba keratitis**
- `HP:0000613` (1 mention) - the report calls it "Frequent"; HP calls it **Photophobia**
- `HP:0200136` (1 mention) - the report calls it "keratitis"; HP calls it **Oral-pharyngeal dysphagia**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `HP`, `GO`, `CL`, `UBERON`.
