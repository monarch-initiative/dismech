---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T17:54:32.359379'
end_time: '2026-10-30T18:45:28.573562'
duration_seconds: 3056.21
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hyperparathyroidism 1
  mondo_id: MONDO:0007767
  category: Mendelian
  causal_genes: CDC73
  omim_id: OMIM:145000
  synonyms: hyperparathyroidism type 1; hyperparathyroidism, familial primary
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
citation_count: 31
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hyperparathyroidism_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hyperparathyroidism_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hyperparathyroidism 1
- **MONDO ID:** MONDO:0007767 (if available)
- **Causal gene(s):** CDC73
- **OMIM:** OMIM:145000
- **Synonyms:** hyperparathyroidism type 1; hyperparathyroidism, familial primary
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hyperparathyroidism 1** covering all of the
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

# Hyperparathyroidism 1 (MONDO:0007767; OMIM 145000) — Comprehensive Disease Characteristics Report

**Causal gene: _CDC73_ (parafibromin), chromosome 1q31.2.** Hyperparathyroidism 1 is caused by germline loss-of-function mutations of **CDC73** (formerly HRPT2 / C1orf28), the gene encoding the nuclear tumor-suppressor **parafibromin** (HGNC:16783; NCBI Gene 79577; UniProt Q6P1J9; Ensembl ENSG00000134371). Although the disease name is a serial number that does not name its gene, every identifier in this report follows MONDO:0007767 / OMIM 145000 / CDC73. This is the CDC73-related hereditary hyperparathyroidism spectrum, which in its fully expressed form is the **hyperparathyroidism–jaw tumor (HPT-JT) syndrome** and in its limited form is **familial isolated hyperparathyroidism (FIHP)**; both predispose to parathyroid carcinoma. It must not be confused with other primary-hyperparathyroidism loci such as MEN1 (MEN1 gene, 11q13), CASR-related familial hypocalciuric hypercalcemia, CDKN1B (MEN4), RET (MEN2A), or GCM2-related FIHP.

---

## Summary

Hyperparathyroidism 1 is an autosomal dominant hereditary endocrine tumor-predisposition disorder arising from germline inactivating mutations in **CDC73** on chromosome **1q31.2**. CDC73 encodes **parafibromin**, a ubiquitously expressed 531-amino-acid nuclear protein that is a core subunit of the human **PAF1 complex (PAF1C)**, which controls RNA polymerase II transcriptional elongation and associated histone modifications. Parafibromin acts as a tumor suppressor principally by repressing the proliferation genes *CCND1* (cyclin D1) and *MYC* (c-myc), and it also participates in canonical Wnt/β-catenin signaling by binding directly to the C-terminal region of β-catenin. Disease results from **biallelic inactivation** of CDC73 in parathyroid chief cells — a germline "first hit" plus a somatic "second hit," most often loss of heterozygosity (LOH) on chromosome 1q — consistent with Knudson's two-hit model of hereditary cancer ([PMID: 30799315](https://pubmed.ncbi.nlm.nih.gov/30799315/)).

Clinically, the disorder presents as **primary hyperparathyroidism (PHPT)** with markedly elevated PTH and often severe hypercalcemia, typically in young adults (mean age of presentation ~27–30 years, documented as early as the second decade). The syndromic form adds **ossifying (cemento-ossifying) fibromas of the mandible and maxilla**, **renal lesions** (cysts, hamartomas, Wilms tumor, mixed epithelial and stromal tumor), and **uterine tumors** (leiomyomas and adenofibromas). The feature that most distinguishes this syndrome from all other causes of PHPT is its **uniquely high lifetime risk of parathyroid carcinoma** — on the order of 15–37.5% in HPT-JT operative series, far above the <1% rate in sporadic PHPT. Risk is further stratified by genotype: **"high-impact" mutations that disrupt the parafibromin C-terminal domain confer ~6.6-fold higher carcinoma risk** than low-impact mutations ([PMID: 32590342](https://pubmed.ncbi.nlm.nih.gov/32590342/)).

At the molecular level, loss of nuclear parafibromin (detectable by immunohistochemistry) is both a surrogate marker for CDC73 mutation and a predictor of malignant behavior. Somatic CDC73 mutations are found in up to 80% of sporadic parathyroid carcinomas, and ~30% of parathyroid carcinoma patients carry a germline CDC73 mutation, whereas benign sporadic parathyroid adenomas rarely harbor CDC73 mutations ([PMID: 37531615](https://pubmed.ncbi.nlm.nih.gov/37531615/); [PMID: 16487440](https://pubmed.ncbi.nlm.nih.gov/16487440/)). A Cdc73-knockout mouse recapitulates the syndrome by developing parathyroid and uterine tumors, providing a validated in vivo model ([PMID: 28288139](https://pubmed.ncbi.nlm.nih.gov/28288139/)). The cornerstone of management is **surgery** (en bloc resection when carcinoma is suspected), with lifelong surveillance of mutation carriers and cascade genetic testing of relatives.

---

## Key Findings

### Finding 1 — CDC73/parafibromin is the causal tumor suppressor, acting via a two-hit mechanism

Germline inactivating mutations of CDC73 (formerly HRPT2; encoding the ubiquitously expressed 531-amino-acid nuclear protein parafibromin) cause autosomal dominant HPT-JT, FIHP, and predispose to sporadic parathyroid carcinoma. As stated in [PMID: 30799315](https://pubmed.ncbi.nlm.nih.gov/30799315/): *"Loss of function of the cell division cycle protein 73 homolog (CDC73) gene is responsible for the syndrome. This gene encodes an ubiquitously expressed 531 amino acid protein, parafibromin, that acts as a tumor suppressor."* The somatic second hit is most often LOH at the CDC73 locus: *"Loss of heterozygosity (LOH) of the CDC73 locus in many HPT-JT associated parathyroid tumors from patients with germline mutation is in accordance with Knudson's 'two-hit' model for hereditary cancer."* Loss of parafibromin by IHC serves as a surrogate marker (e.g., ~90% protein reduction documented in a carcinoma despite normal mRNA).

### Finding 2 — Parafibromin functions in the PAF1 complex and regulates Wnt/β-catenin signaling and proliferation genes

Parafibromin is a core component of the human PAF1 complex controlling RNA Pol II transcriptional elongation and histone modifications. It represses *CCND1* (cyclin D1) and *MYC* (c-myc), and binds directly to the C-terminal region of β-catenin/Armadillo to transduce Wnt/Wg signals (Drosophila ortholog Hyrax/hyx). Per [PMID: 29142233](https://pubmed.ncbi.nlm.nih.gov/29142233/): *"CDC73/parafibromin was initially recognized as a tumor suppressor by inhibiting cell proliferation via repression of cyclin D1 and c-myc genes. In recent years, it has also shown oncogenic features by activating the canonical Wnt/β-catenin signal pathway."* And [PMID: 16630820](https://pubmed.ncbi.nlm.nih.gov/16630820/): *"Drosophila Hyrax and its human ortholog, Parafibromin, components of the Polymerase-Associated Factor 1 (PAF1) complex, are required for nuclear transduction of the Wnt/Wg signal and bind directly to the C-terminal region of beta-catenin/Armadillo."* Pathogenic missense mutations cluster in the N-terminal domain (residues 1–111; crystal structure solved to 1.02 Å) and disrupt its hydrophobic core/folding. Parafibromin additionally regulates the translational factor CPEB ([PMID: 20339377](https://pubmed.ncbi.nlm.nih.gov/20339377/)).

### Finding 3 — CDC73 genotype predicts parathyroid carcinoma risk (6.6-fold for high-impact/CTD mutations)

In a cohort of 419 CDC73 germline-mutation carriers, "high-impact" mutations (predicted significant conformational disruption or loss of parafibromin expression) were enriched among parathyroid-cancer cases. Per [PMID: 32590342](https://pubmed.ncbi.nlm.nih.gov/32590342/): *"The Kaplan-Meier analysis showed that high-impact mutations were associated with a 6.6-fold higher risk of parathyroid carcinoma compared to low-impact mutations, despite a similar risk of developing primary hyperparathyroidism between two groups."* Critically, *"Disruption of the C-terminal domain (CTD) of parafibromin is directly involved in predisposition to parathyroid carcinoma, since only the mutations impacting this domain were associated with an increased risk of parathyroid carcinoma."* Operative series report carcinoma in ~20–37.5% of HPT-JT PHPT patients; in one cohort ([PMID: 25444225](https://pubmed.ncbi.nlm.nih.gov/25444225/)): *"37.5% of the patients developed parathyroid carcinoma (median overall survival, 8.9 years; median follow-up, 7.4 years)."*

### Finding 4 — Clinical phenotype spectrum: PHPT with severe hypercalcemia, jaw fibromas, renal and uterine lesions

Core features are PHPT with markedly elevated PTH and severe hypercalcemia, ossifying fibromas of the mandible/maxilla, renal lesions (cysts, hamartomas, Wilms tumor, mixed epithelial/stromal tumor), and uterine tumors. [PMID: 25959515](https://pubmed.ncbi.nlm.nih.gov/25959515/) defines the syndrome as *"characterized by synchronous or metachronous occurrence of primary hyperparathyroidism (PHPT), ossifying fibroma of the maxilla and/or mandible, renal tumor and uterine tumors."* Onset is typically young adult (case-series means 27–30 years; as early as age 13). A 24-case jaw ossifying-fibroma review reported ([PMID: 33505612](https://pubmed.ncbi.nlm.nih.gov/33505612/)): *"The average age was 28.68 years old (age range 10-66), with 12 male and 12 female patients (1:1 M/F ratio). Hyperparathyroidism results from parathyroid adenoma in 16/24 cases (66.666%) and parathyroid carcinome in 5/24 (20.833%)."* Penetrance of PHPT is age-dependent and incomplete — [PMID: 33999366](https://pubmed.ncbi.nlm.nih.gov/33999366/): *"Thirteen carried the deletion, the penetrance was estimated at 50% at 40 years."* PHPT is often uniglandular but multiglandular in ~31% and recurrent in ~20% ([PMID: 25444225](https://pubmed.ncbi.nlm.nih.gov/25444225/)). Bone disease includes osteitis fibrosa cystica, brown tumors, and fractures.

### Finding 5 — CDC73 maps to chromosome 1q31.2

CDC73 is located on chromosome **1q31.2** and contains 17 exons encoding the 531-amino-acid parafibromin (this corrects an earlier internal cytoband typo of "17q11.2"). The somatic second hit is commonly LOH on chromosome 1q. The locus is confirmed across multiple sources including the original mapping paper ([PMID: 16487440](https://pubmed.ncbi.nlm.nih.gov/16487440/)) and the mouse-model study ([PMID: 28288139](https://pubmed.ncbi.nlm.nih.gov/28288139/)).

### Finding 6 — Somatic CDC73 in up to 80% of parathyroid carcinomas; germline in ~30%; benign adenomas rarely affected

Parathyroid carcinoma (PC) accounts for <1% of PHPT and ~0.005% of all cancers. Per [PMID: 37531615](https://pubmed.ncbi.nlm.nih.gov/37531615/): *"PC most commonly occurs as a sporadic disease and somatic CDC73 mutations can be detected in up to 80% of cases. Approximately 30% of patients harbor a germline mutation of the CDC73 gene."* In contrast, sporadic benign adenomas rarely carry CDC73 mutations. The original mapping ([PMID: 16487440](https://pubmed.ncbi.nlm.nih.gov/16487440/)) states: *"The HPT-JT syndrome and FIHP are autosomal dominant disorders that may be caused by abnormalities of the HRPT2 gene, located on chromosome 1q31.2. HRPT2 encodes a 531 amino acid protein, parafibromin, which interacts with human homologues of the yeast Paf1 complex."* Atypical parathyroid adenomas occupy an intermediate position (germline CDC73 in ~4/56; FIHP patients younger, 30±17 vs 55±13 y; [PMID: 34157106](https://pubmed.ncbi.nlm.nih.gov/34157106/)).

### Finding 7 — Cdc73-deleted mice recapitulate HPT-JT

Thakker and colleagues generated conventional and conditional Cdc73-knockout mice that developed parathyroid tumours (atypical adenomas/carcinomas) and uterine neoplasms, phenocopying key features of human HPT-JT ([PMID: 28288139](https://pubmed.ncbi.nlm.nih.gov/28288139/)). The paper confirms: *"HPT-JT is caused by mutations of the cell division cycle 73 (CDC73) gene, located on chromosome 1q31.2 and encodes a 531 amino acid protein, parafibromin."* Mouse ortholog Cdc73 (NCBI Gene 214498). The Drosophila ortholog hyrax/hyx and yeast Cdc73 (PAF1 complex) demonstrate deep evolutionary conservation.

---

## 1. Disease Information

**Overview.** Hyperparathyroidism 1 (CDC73-related hyperparathyroidism) is a Mendelian, autosomal dominant endocrine tumor-predisposition syndrome whose cardinal manifestation is primary hyperparathyroidism due to parathyroid tumors (adenoma, atypical adenoma, or carcinoma) that over-secrete PTH, producing hypercalcemia. The disorder spans a clinical continuum: at one end **familial isolated hyperparathyroidism (FIHP)**, limited to parathyroid disease; at the other, the full **hyperparathyroidism–jaw tumor (HPT-JT) syndrome** with jaw, renal, and uterine lesions. CDC73 germline mutations also underlie a substantial fraction of apparently sporadic parathyroid carcinoma.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0007767 |
| OMIM | 145000 (Hyperparathyroidism 1 / HRPT1) |
| Gene | CDC73 (HGNC:16783; NCBI Gene 79577; Ensembl ENSG00000134371; UniProt Q6P1J9) |
| Orphanet | Hyperparathyroidism–jaw tumor syndrome (ORPHA:99879) |
| MeSH | Hyperparathyroidism, Primary; Jaw Neoplasms |
| ICD-10 | E21.0 (primary hyperparathyroidism) |

**Synonyms.** Hyperparathyroidism type 1; hyperparathyroidism, familial primary; HRPT1; CDC73-related disorders; hyperparathyroidism–jaw tumor syndrome (HPT-JT) when fully expressed; familial isolated hyperparathyroidism (FIHP, in part).

**Nature of evidence.** Information is drawn from **aggregated disease-level resources** (OMIM, Orphanet, GeneReviews-type reviews) and **individual-patient primary literature** — case reports, family studies, and operative/pathology case series — rather than from large EHR cohorts, reflecting the rarity of the disorder.

---

## 2. Etiology

**Disease causal factors.** The primary cause is **genetic**: a heterozygous germline loss-of-function mutation in **CDC73**, inherited in an autosomal dominant manner, followed by somatic inactivation of the remaining wild-type allele in the target tissue (two-hit mechanism). There is no established infectious or primary environmental cause.

**Genetic risk factors.**
- **Causal variants:** germline inactivating CDC73 mutations — nonsense, frameshift, splice-site, and large intragenic deletions predominate; missense and start-loss variants also occur. Examples include p.R76X, p.R91X, p.Q166X nonsense mutations ([PMID: 30361844](https://pubmed.ncbi.nlm.nih.gov/30361844/); [PMID: 27801421](https://pubmed.ncbi.nlm.nih.gov/27801421/)), exon-3 deletion ([PMID: 33999366](https://pubmed.ncbi.nlm.nih.gov/33999366/)), exon 4–10 deletion ([PMID: 28774260](https://pubmed.ncbi.nlm.nih.gov/28774260/)), and a novel exon-2 insertion ([PMID: 37909004](https://pubmed.ncbi.nlm.nih.gov/37909004/)).
- **Genotype as risk modifier:** high-impact / C-terminal-domain-disrupting mutations markedly increase carcinoma risk ([PMID: 32590342](https://pubmed.ncbi.nlm.nih.gov/32590342/)); frameshift indel, splice-site, and stop-gain genotypes carry greatly increased carcinoma risk relative to missense/non-frameshift variants ([PMID: 39775826](https://pubmed.ncbi.nlm.nih.gov/39775826/)).
- **Differential-diagnosis loci** (not CDC73 but overlapping phenotype): MEN1, RET (MEN2A), CASR (FHH), CDKN1B (MEN4), GCM2 ([PMID: 32761341](https://pubmed.ncbi.nlm.nih.gov/32761341/); [PMID: 30536424](https://pubmed.ncbi.nlm.nih.gov/30536424/)).

**Environmental / demographic risk factors.** Age (young-adult onset), family history, and female sex for the uterine component are relevant; no specific toxic, occupational, or infectious exposure is implicated in CDC73-driven disease.

**Protective factors.** No genetic or environmental protective factors are established. Early identification and pre-emptive parathyroidectomy mitigate morbidity but are interventions rather than intrinsic protective factors.

**Gene–environment interactions.** None established. The disease is driven by the germline mutation plus a stochastic somatic second hit; no environmental modifier of penetrance has been robustly identified.

---

## 3. Phenotypes

| Phenotype | Type | HPO term (suggested) | Onset / severity / frequency |
|---|---|---|---|
| Primary hyperparathyroidism | Laboratory/clinical | HP:0008207 | Young-adult onset; severe; near-universal defining feature |
| Hypercalcemia | Laboratory abnormality | HP:0003072 | Often severe (serum Ca frequently >3 mmol/L / >12 mg/dL) |
| Elevated circulating PTH | Laboratory abnormality | HP:0003165 | Markedly elevated, often disproportionate |
| Hypophosphatemia | Laboratory abnormality | HP:0002148 | Common (mean ~1.78 mg/dL in one series) |
| Parathyroid adenoma | Neoplasm | HP:0002897 | Most common parathyroid lesion; often uniglandular (~66.7%) |
| Parathyroid carcinoma | Neoplasm | HP:0006780 | ~15–37.5% of HPT-JT PHPT cases — the signature risk |
| Ossifying/cemento-ossifying jaw fibroma | Physical/neoplasm | HP:0010766 (Jaw neoplasm) | Mean age ~28.7 y; mandible ~66.7%; may precede hypercalcemia in ~21% |
| Nephrolithiasis / nephrocalcinosis | Clinical sign | HP:0000787 / HP:0100634 | Common renal complication |
| Renal cysts / hamartoma / Wilms / mixed epithelial-stromal tumor | Neoplasm/malformation | HP:0000107; HP:0002667 | Variable; renal cysts in multiple series |
| Uterine leiomyoma / adenofibroma | Neoplasm | HP:0000131 (Uterine neoplasm) | Common in affected women; may cause menorrhagia |
| Osteitis fibrosa cystica / brown tumors | Physical manifestation | HP:0002749; HP:0100671 | Severe bone disease; pathological fractures |
| Bone pain, proximal muscle weakness | Symptom | HP:0002653; HP:0003324 | Frequent in symptomatic PHPT |
| Pathological fractures | Clinical sign | HP:0002756 | In severe/prolonged disease |

**Phenotype characteristics.** Onset is typically **young adult** (index-case mean ~27–30 years; as early as age 13). Severity is **variable but often severe**, with markedly elevated calcium/PTH and target-organ damage. Course is **progressive and recurrent** — PHPT recurs in ~20% and is multiglandular in ~31% ([PMID: 25444225](https://pubmed.ncbi.nlm.nih.gov/25444225/)). Penetrance of PHPT is **age-dependent and incomplete** (~50% by age 40; [PMID: 33999366](https://pubmed.ncbi.nlm.nih.gov/33999366/)).

**Quality-of-life impact.** Severe hypercalcemia causes fatigue, cognitive slowing, polyuria, renal colic, bone pain, and fractures; recurrent neck surgery and lifelong surveillance add a chronic-disease burden. Disease-specific QOL-instrument data (EQ-5D/SF-36) for this syndrome are **not available**; impact is inferred from PHPT and parathyroid-carcinoma literature.

---

## 4. Genetic / Molecular Information

**Causal gene.** CDC73 (HGNC:16783; NCBI Gene 79577; UniProt Q6P1J9), chromosome **1q31.2**, 17 exons, encoding **parafibromin**, a 531-amino-acid nuclear tumor suppressor ([PMID: 16487440](https://pubmed.ncbi.nlm.nih.gov/16487440/); [PMID: 30799315](https://pubmed.ncbi.nlm.nih.gov/30799315/)).

**Pathogenic variants.**
- **Classification:** Most reported germline variants are **pathogenic/likely pathogenic** truncating alleles; VUS are encountered ([PMID: 32761341](https://pubmed.ncbi.nlm.nih.gov/32761341/)).
- **Variant types:** nonsense, frameshift indels, splice-site, start-loss (initiator Met), missense, and large multi-exon deletions (exon 3; exons 4–10). 5′UTR insertions can impair parafibromin expression ([PMID: 28774260](https://pubmed.ncbi.nlm.nih.gov/28774260/)).
- **Allele frequency:** germline CDC73 pathogenic variants are rare in gnomAD; the disorder is rare.
- **Somatic vs germline:** both occur. Germline drives the hereditary syndrome; somatic CDC73 mutations (± LOH) provide the second hit and are detectable in **up to 80% of parathyroid carcinomas**, while **~30% of carcinoma patients carry a germline mutation** ([PMID: 37531615](https://pubmed.ncbi.nlm.nih.gov/37531615/)).
- **Functional consequence:** **loss of function** of a tumor suppressor (haploinsufficiency plus somatic second hit → biallelic inactivation). Missense mutations cluster in the N-terminal domain (residues 1–111) and disrupt folding (crystal structure 1.02 Å; [PMID: 29142233](https://pubmed.ncbi.nlm.nih.gov/29142233/)); CTD disruption predisposes to carcinoma ([PMID: 32590342](https://pubmed.ncbi.nlm.nih.gov/32590342/)).

**Genotype–phenotype correlations.** Two correlations are recognized ([PMID: 39775826](https://pubmed.ncbi.nlm.nih.gov/39775826/)): (1) a **start-loss variant of the initiator methionine** correlates specifically with renal **mixed epithelial and stromal tumor**; (2) **frameshift indel, splice-site, and stop-gain** genotypes carry greatly increased parathyroid-carcinoma risk relative to missense/non-frameshift indel variants.

**Modifier genes.** No validated modifier genes; carcinoma risk is driven by the nature/location of the CDC73 variant itself (CTD vs non-CTD).

**Epigenetics / chromosomal abnormalities.** The dominant somatic event is **LOH on chromosome 1q**. Broader genetic/epigenetic alterations in parathyroid carcinoma have been reviewed ([PMID: 35282432](https://pubmed.ncbi.nlm.nih.gov/35282432/)); PI3K/AKT/mTOR and Wnt pathway alterations are emerging co-contributors ([PMID: 42400268](https://pubmed.ncbi.nlm.nih.gov/42400268/)). No recurrent large-scale aneuploidy/translocation signature specific to the syndrome is established.

---

## 5. Environmental Information

No environmental toxin, radiation, pollution, or occupational exposure is established as a cause of CDC73-driven Hyperparathyroidism 1. No lifestyle factor (smoking, diet, alcohol, exercise) is implicated in penetrance. **No infectious agent** is involved. This section is largely **not applicable** — the disease is monogenic/germline-driven.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **germline heterozygous inactivating CDC73 mutation** is inherited (first hit) → **leads to** a tumor-predisposed state in all cells.
2. In a parathyroid chief cell, a **somatic second hit** (most often LOH at 1q, or a second CDC73 point mutation) → **results in** biallelic CDC73 inactivation and near-complete loss of nuclear parafibromin (Knudson two-hit model) ([PMID: 30799315](https://pubmed.ncbi.nlm.nih.gov/30799315/)).
3. Loss of parafibromin → **impairs PAF1-complex function** on RNA Pol II (elongation and histone-modification control) → **de-represses** *CCND1* (cyclin D1) and *MYC* (c-myc) ([PMID: 29142233](https://pubmed.ncbi.nlm.nih.gov/29142233/)). *(Branch: parafibromin also binds β-catenin to transduce Wnt/Wg signaling — [PMID: 16630820](https://pubmed.ncbi.nlm.nih.gov/16630820/) — so its loss dysregulates Wnt/β-catenin target-gene transcription; net oncogenic vs tumor-suppressive effect is context-dependent.)*
4. De-repressed proliferation + loss of growth arrest/apoptosis control → **drives clonal expansion** of chief cells → **produces** a parathyroid adenoma, atypical adenoma, or carcinoma. *(Branch: CTD-disrupting/high-impact mutations → biased toward carcinoma; [PMID: 32590342](https://pubmed.ncbi.nlm.nih.gov/32590342/).)*
5. The expanded tumor **autonomously over-secretes PTH** → **causes** primary hyperparathyroidism.
6. Excess PTH → **increases** osteoclastic bone resorption, renal calcium reabsorption, and 1,25-(OH)₂-vitamin-D-mediated intestinal calcium absorption → **produces hypercalcemia and hypophosphatemia**.
7. Hypercalcemia/high PTH → **cause** downstream sequelae: nephrolithiasis/nephrocalcinosis, osteitis fibrosa cystica with brown tumors and fractures, and neuromuscular/cognitive symptoms.
8. In parallel tissues, biallelic CDC73 loss (inferred, by analogy) **predisposes to** jaw ossifying fibromas, renal cysts/hamartomas/Wilms/mixed epithelial-stromal tumors, and uterine leiomyomas/adenofibromas.

### Molecular and cellular detail

- **Molecular pathways.** Parafibromin is a core subunit of the **PAF1C**, coupling RNA Pol II elongation to histone H2B ubiquitination and H3K4/K36 methylation; it represses *CCND1* and *MYC* and binds the C-terminal region of **β-catenin/Armadillo** to transduce **Wnt/Wg** signals (Drosophila ortholog **Hyrax/hyx**). It also regulates the translational factor **CPEB** ([PMID: 20339377](https://pubmed.ncbi.nlm.nih.gov/20339377/)). Emerging **PI3K/AKT/mTOR** activation contributes to carcinoma ([PMID: 42400268](https://pubmed.ncbi.nlm.nih.gov/42400268/)).
  - Suggested **GO terms:** GO:0006368 (transcription elongation by RNA Pol II), GO:0016055 (Wnt signaling pathway), GO:0008285 (negative regulation of cell population proliferation), GO:0016570 (histone modification).
- **Cellular processes.** Dysregulated cell-cycle entry (cyclin D1), loss of growth arrest/apoptosis, clonal proliferation of parathyroid chief cells.
- **Protein dysfunction.** Loss of function via truncation, deletion, or destabilizing missense mutation (N-terminal folding defects; [PMID: 29142233](https://pubmed.ncbi.nlm.nih.gov/29142233/)); loss of nuclear localization/expression on IHC.
- **Biochemical abnormalities.** Autonomous PTH hypersecretion → hypercalcemia, hypophosphatemia, elevated alkaline phosphatase, elevated 1,25-(OH)₂ vitamin D.
- **Tissue damage mechanisms.** PTH-driven osteoclastic bone resorption (osteitis fibrosa cystica, brown tumors, fractures); hypercalcemia-driven nephrolithiasis/nephrocalcinosis and renal impairment.
- **Cell types involved.** Parathyroid **chief cells** (CL:0000446); osteoclasts (CL:0000092) as effectors of bone resorption.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** **Parathyroid glands** (UBERON:0001132). **Secondary / associated organs:** mandible/maxilla (UBERON:0001684 / UBERON:0002397) for ossifying fibromas; **kidney** (UBERON:0002113) for cysts, hamartomas, Wilms and mixed epithelial-stromal tumors, and stones; **uterus** (UBERON:0000995) for leiomyomas/adenofibromas; **skeleton** (osteitis fibrosa cystica, brown tumors).

**Body systems:** endocrine (parathyroid), skeletal, renal/urinary, reproductive (female).

**Tissue and cell level:** parathyroid glandular **epithelium** (chief cells, CL:0000446); bone (osteoclast-mediated resorption, CL:0000092); renal epithelial/stromal tissue; uterine smooth muscle (leiomyoma).

**Subcellular level:** parafibromin is a **nuclear** protein (GO:0005634) functioning within the **PAF1 complex** (GO:0016593, Cdc73/Paf1 complex). Loss of nuclear parafibromin staining is the diagnostic IHC hallmark.

**Localization / lateralization:** parathyroid tumors are often **uniglandular** but may be **multiglandular** (~31%); renal and uterine involvement can be bilateral/multifocal.

---

## 8. Temporal Development

**Onset.** Typically **young adult** (index-case means ~27–30 years; as early as age 13). Onset pattern is **insidious/chronic**, often discovered via hypercalcemia or a complication (stone, fracture, jaw mass).

**Progression.** **Progressive and recurrent**: PHPT is multiglandular in ~31% and recurs in ~20% ([PMID: 25444225](https://pubmed.ncbi.nlm.nih.gov/25444225/)); carcinoma may arise or recur over years (median OS ~8.9 y in one carcinoma-enriched series). Penetrance is **age-dependent and incomplete** (~50% by age 40; [PMID: 33999366](https://pubmed.ncbi.nlm.nih.gov/33999366/)).

**Patterns.** Remission is **treatment-induced** (surgical cure of PHPT); spontaneous remission does not occur. **Critical window:** early surgical cure before irreversible bone/renal damage or malignant transformation — hence surveillance of carriers from adolescence.

---

## 9. Inheritance and Population

**Epidemiology.** HPT-JT / CDC73-related hyperparathyroidism is **rare** (Orphanet rare disease; precise prevalence not firmly established). Parathyroid carcinoma accounts for <1% of PHPT and ~0.005% of all cancers ([PMID: 37531615](https://pubmed.ncbi.nlm.nih.gov/37531615/)). Overall PHPT incidence has risen sharply (3.5→26.9 per 100,000, 1998–2023), but this is driven by sporadic normocalcemic PHPT, not the hereditary CDC73 form ([PMID: 42541837](https://pubmed.ncbi.nlm.nih.gov/42541837/)).

**Inheritance.** **Autosomal dominant** with incomplete, age-dependent penetrance and **variable expressivity** (FIHP ↔ full HPT-JT ↔ carcinoma). No convincing genetic anticipation. Germline mosaicism and founder effects are not prominently described. Consanguinity is not a driver (dominant disorder).

**Population demographics.** Reported across diverse populations (India, Russia, Portugal, Italy, China). No strong ethnic predilection established. **Sex ratio** for parathyroid disease is roughly balanced (1:1 M/F in a 24-case jaw-fibroma review; [PMID: 33505612](https://pubmed.ncbi.nlm.nih.gov/33505612/)), unlike the female predominance of sporadic PHPT; the uterine component affects women only. Age distribution skews younger than sporadic PHPT.

---

## 10. Diagnostics

**Biochemistry.** Elevated serum **calcium** (often severe, >3 mmol/L), elevated **intact PTH**, **hypophosphatemia**, elevated **alkaline phosphatase**. A non-elevated/low phosphate with hypercalcemia supports parathyroid autonomy ([PMID: 42771820](https://pubmed.ncbi.nlm.nih.gov/42771820/)).

**Imaging / localization.** Neck **ultrasound**, **99mTc-sestamibi** scintigraphy, **4D-CT**, and **[18F]fluorocholine PET/CT** localize lesions and detect metastasis ([PMID: 42400268](https://pubmed.ncbi.nlm.nih.gov/42400268/)). Skeletal survey/DXA assesses bone disease; renal and jaw imaging assess stones/cysts/tumors and ossifying fibromas.

**Pathology / IHC.** **Loss of nuclear parafibromin** by IHC is a surrogate for CDC73 inactivation and flags malignancy risk. Parafibromin-deficient tumors show distinctive morphology — sheet-like growth, eosinophilic cytoplasm with perinuclear clearing, nuclear enlargement with coarse chromatin, arborizing "hemangiopericytoma-like" vasculature, thick capsule, and microcystic change ([PMID: 29324469](https://pubmed.ncbi.nlm.nih.gov/29324469/); [PMID: 36739170](https://pubmed.ncbi.nlm.nih.gov/36739170/)).

**Genetic testing.** **Single-gene CDC73 sequencing of all 17 exons plus deletion/duplication (CNV/MLPA) analysis** is recommended, since large intragenic deletions occur and would be missed by sequencing alone ([PMID: 28774260](https://pubmed.ncbi.nlm.nih.gov/28774260/)). Multigene PHPT panels (CDC73, MEN1, RET, CASR, CDKN1B, GCM2) and NGS are used when the differential is broad ([PMID: 35586626](https://pubmed.ncbi.nlm.nih.gov/35586626/); [PMID: 32761341](https://pubmed.ncbi.nlm.nih.gov/32761341/)). WES is useful in research/undiagnosed settings. **Indications:** age <30–40 y, multigland disease, recurrent/refractory PHPT, atypical adenoma or carcinoma, family history, or syndromic features ([PMID: 39700332](https://pubmed.ncbi.nlm.nih.gov/39700332/)).

**Clinical criteria / differential diagnosis.** Diagnosis integrates biochemical PHPT + syndromic features + CDC73 genotype. Key differentials: MEN1, MEN2A (RET), MEN4 (CDKN1B), FHH (CASR — these patients should *not* undergo parathyroidectomy), GCM2-related FIHP, and IGF-I-related mineral changes in acromegaly ([PMID: 32761341](https://pubmed.ncbi.nlm.nih.gov/32761341/); [PMID: 42771820](https://pubmed.ncbi.nlm.nih.gov/42771820/)).

**Screening.** **Cascade genetic testing** of first-degree relatives; biochemical surveillance (calcium/PTH) and periodic imaging of carriers.

---

## 11. Outcome / Prognosis

**Benign-spectrum disease** has good prognosis with surgical cure, but recurrence (~20%) and multiglandular disease (~31%) necessitate lifelong follow-up.

**Parathyroid carcinoma.** 5-year OS ~60–93% and 10-year ~49–70% across series ([PMID: 32247225](https://pubmed.ncbi.nlm.nih.gov/32247225/); [PMID: 35282432](https://pubmed.ncbi.nlm.nih.gov/35282432/)); recurrence 23–65% mandates lifelong follow-up ([PMID: 42400268](https://pubmed.ncbi.nlm.nih.gov/42400268/)). In an HPT-JT operative cohort where 37.5% developed carcinoma, median OS was 8.9 years ([PMID: 25444225](https://pubmed.ncbi.nlm.nih.gov/25444225/)). **Most deaths result from uncontrollable hypercalcemia rather than tumor bulk** ([PMID: 32247225](https://pubmed.ncbi.nlm.nih.gov/32247225/)).

**Morbidity.** Nephrolithiasis/nephrocalcinosis and renal impairment, osteitis fibrosa cystica with brown tumors and pathological fractures, and complications of recurrent neck surgery.

**Prognostic factors.** Complete initial en bloc resection and postoperative remission predict better outcome; adverse markers include high Ki-67, **loss of parafibromin**, and mTOR activation ([PMID: 42400268](https://pubmed.ncbi.nlm.nih.gov/42400268/)). **High-impact / CTD-disrupting CDC73 genotypes predict carcinoma** (6.6-fold; [PMID: 32590342](https://pubmed.ncbi.nlm.nih.gov/32590342/)).

---

## 12. Treatment

**Surgery (cornerstone).** Parathyroidectomy cures PHPT; for suspected/confirmed **parathyroid carcinoma, en bloc resection with ipsilateral thyroid lobectomy** and clear margins is the gold standard to minimize local recurrence ([PMID: 32247225](https://pubmed.ncbi.nlm.nih.gov/32247225/); [PMID: 42400268](https://pubmed.ncbi.nlm.nih.gov/42400268/)). Intraoperative PTH monitoring aids cure confirmation. (NCIT: parathyroidectomy, NCIT:C51818.)

**Medical management of hypercalcemia.** **Cinacalcet** (calcimimetic / CaSR agonist; NCIT:C65366) lowers calcium and PTH; **bisphosphonates** (e.g., zoledronic acid) and **denosumab** (RANKL mAb) control hypercalcemia and skeletal disease. Sustained access to these agents is critical in advanced carcinoma ([PMID: 40978536](https://pubmed.ncbi.nlm.nih.gov/40978536/)).

**Targeted / systemic therapy for advanced carcinoma.** Conventional chemotherapy and radiotherapy have limited efficacy. The multikinase inhibitor **lenvatinib** produced ~9 months of biochemical/radiological control in a metastatic CDC73-mutant case ([PMID: 40978536](https://pubmed.ncbi.nlm.nih.gov/40978536/)); targeted therapy and immunotherapy are promising but evidence remains weak ([PMID: 42400268](https://pubmed.ncbi.nlm.nih.gov/42400268/)).

**Supportive care.** Management of pathological fractures, hungry bone syndrome post-parathyroidectomy (especially with large adenomas, high alkaline phosphatase, brown tumors; [PMID: 39700332](https://pubmed.ncbi.nlm.nih.gov/39700332/)), hydration, and nutrition.

**Pharmacogenomics / gene therapy / cell therapy.** No established pharmacogenomic guidance, gene therapy, or cell therapy specific to CDC73 disease.

**Treatment strategy / personalized medicine.** Genotype-guided surveillance (CTD/high-impact variants → heightened carcinoma vigilance; [PMID: 32590342](https://pubmed.ncbi.nlm.nih.gov/32590342/)) and multidisciplinary management in centers of excellence ([PMID: 36621911](https://pubmed.ncbi.nlm.nih.gov/36621911/)).

---

## 13. Prevention

- **Primary prevention:** not possible for the inherited mutation; focus is on genetic counseling and reproductive options (prenatal/preimplantation genetic testing) for carriers.
- **Secondary prevention (most important):** **cascade genetic testing** of relatives + lifelong biochemical surveillance (calcium, PTH) and periodic imaging enables **pre-emptive parathyroidectomy** before complications or malignant transformation ([PMID: 28774260](https://pubmed.ncbi.nlm.nih.gov/28774260/)).
- **Tertiary prevention:** complete surgical resection and lifelong follow-up to detect recurrence; management of bone/renal complications.
- **Counseling:** genetic counseling for autosomal dominant inheritance, incomplete penetrance, and variable expressivity.
- **Immunization / public-health / environmental measures:** not applicable (monogenic disorder).

---

## 14. Other Species / Natural Disease

**Taxonomy / orthologs.** CDC73 is deeply conserved. Mouse **Cdc73** (NCBI Gene 214498; *Mus musculus*, NCBI:txid10090); *Drosophila melanogaster* ortholog **hyrax/hyx** (NCBI:txid7227); yeast **Cdc73** PAF1-complex subunit (*Saccharomyces cerevisiae*, NCBI:txid4932). Functional conservation spans transcriptional (PAF1C) and Wnt-signaling roles ([PMID: 16630820](https://pubmed.ncbi.nlm.nih.gov/16630820/); [PMID: 20339377](https://pubmed.ncbi.nlm.nih.gov/20339377/)).

**Natural disease in other species.** No well-characterized naturally occurring CDC73-driven HPT-JT analog is documented in companion animals or wildlife; evidence is primarily from engineered models rather than natural veterinary disease.

**Transmission.** Not applicable — non-infectious, non-zoonotic genetic disorder.

---

## 15. Model Organisms

**Mouse (primary model).** Conventional and conditional **Cdc73-knockout mice** develop **parathyroid tumors (atypical adenomas/carcinomas) and uterine neoplasms**, recapitulating key features of human HPT-JT ([PMID: 28288139](https://pubmed.ncbi.nlm.nih.gov/28288139/)). Model type: mammalian, genetically engineered (knockout, conditional).
- **Phenotype recapitulation:** strong for parathyroid and uterine tumorigenesis.
- **Limitations:** jaw ossifying fibromas and the full renal-lesion spectrum are less completely modeled; penetrance/latency differ from human.

**Invertebrate / yeast models.** *Drosophila* **hyrax** and yeast **Cdc73** elucidated the conserved PAF1-complex transcriptional-elongation function, the Wnt-signaling role, and the CPEB translational link ([PMID: 20339377](https://pubmed.ncbi.nlm.nih.gov/20339377/); [PMID: 16630820](https://pubmed.ncbi.nlm.nih.gov/16630820/)) — valuable for mechanism, not organ-level disease.

**Resources:** MGI (mouse Cdc73), Alliance of Genome Resources, FlyBase (hyx), SGD (yeast CDC73).

---

## Mechanistic Model / Interpretation

```
 Germline CDC73 LOF mutation (1q31.2)  ── "first hit", all cells
                 │
                 ▼
 Somatic 2nd hit in a parathyroid chief cell (LOH at 1q / 2nd mutation)
                 │  (Knudson two-hit)
                 ▼
 Biallelic CDC73 loss → NO nuclear parafibromin (IHC-negative)
                 │
        ┌────────┴─────────────────────────────┐
        ▼                                        ▼
 PAF1C dysfunction on RNA Pol II        Wnt/β-catenin dysregulation
 → de-repress CCND1 (cyclin D1), MYC     (parafibromin binds β-catenin)
        │                                        │
        └───────────────┬────────────────────────┘
                        ▼
       Clonal chief-cell proliferation
       (adenoma → atypical adenoma → CARCINOMA)
          │  CTD/high-impact mutation → ↑↑ carcinoma (6.6×)
                        ▼
       Autonomous PTH hypersecretion
                        ▼
   Hypercalcemia + hypophosphatemia
        ├── bone: osteitis fibrosa cystica, brown tumors, fractures
        ├── kidney: stones, nephrocalcinosis
        └── neuromuscular/cognitive symptoms

 Parallel (biallelic CDC73 loss, inferred): jaw ossifying fibroma,
 renal cysts/hamartoma/Wilms/mixed epithelial-stromal tumor,
 uterine leiomyoma/adenofibroma  → HPT-JT syndrome
```

The unifying principle is a **two-hit tumor-suppressor mechanism** converging on loss of parafibromin, whose transcriptional (PAF1C → CCND1/MYC) and Wnt-signaling functions normally restrain proliferation. The **genotype dictates the malignant ceiling**: C-terminal-domain/high-impact alleles push toward carcinoma. Downstream, a single effector — **PTH excess** — explains the entire hypercalcemic clinical syndrome, while parallel tissue-specific biallelic loss explains the extra-parathyroid tumors.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [30799315](https://pubmed.ncbi.nlm.nih.gov/30799315/) | Novel CDC73 mutation in HPT-JT carcinoma w/o LOH | CDC73/parafibromin (531 aa) tumor suppressor; two-hit/LOH model |
| [29142233](https://pubmed.ncbi.nlm.nih.gov/29142233/) | Crystal structure of CDC73 NTD | Represses cyclin D1/c-myc; Wnt role; NTD folding mutations |
| [16630820](https://pubmed.ncbi.nlm.nih.gov/16630820/) | Parafibromin/Hyrax activates Wnt via β-catenin | PAF1C component; direct β-catenin binding; Drosophila ortholog |
| [20339377](https://pubmed.ncbi.nlm.nih.gov/20339377/) | CPEB is conserved target of HRPT2/CDC73 | Translational control; evolutionary conservation (hyx) |
| [32590342](https://pubmed.ncbi.nlm.nih.gov/32590342/) | CDC73 genotype determines cancer risk | 6.6× carcinoma risk for high-impact/CTD mutations (n=419) |
| [25444225](https://pubmed.ncbi.nlm.nih.gov/25444225/) | HPT-JT operative management | 37.5% carcinoma; recurrence ~20%; multiglandular ~31% |
| [33505612](https://pubmed.ncbi.nlm.nih.gov/33505612/) | Jaw ossifying fibroma in HPT-JT (24 cases) | Mean age 28.7 y; mandible 66.7%; adenoma 66.7%/carcinoma 20.8% |
| [33999366](https://pubmed.ncbi.nlm.nih.gov/33999366/) | Exon-3 deletion family | Penetrance ~50% at 40 y (incomplete, age-dependent) |
| [25959515](https://pubmed.ncbi.nlm.nih.gov/25959515/) | Early-onset severe recurrent PHPT (novel CDC73) | Multi-organ phenotype definition |
| [37531615](https://pubmed.ncbi.nlm.nih.gov/37531615/) | Approach to parathyroid carcinoma | Somatic CDC73 up to 80%; germline ~30% in PC |
| [16487440](https://pubmed.ncbi.nlm.nih.gov/16487440/) | Parafibromin mutations in HPT syndromes | HRPT2/CDC73 at 1q31.2; 531 aa; Paf1 complex |
| [28288139](https://pubmed.ncbi.nlm.nih.gov/28288139/) | Cdc73-KO mice develop parathyroid/uterine tumors | Validated mouse model; 1q31.2 confirmation |
| [29324469](https://pubmed.ncbi.nlm.nih.gov/29324469/) | Parafibromin-deficient tumor morphology | Distinctive histology; IHC triage |
| [36739170](https://pubmed.ncbi.nlm.nih.gov/36739170/) | CDC73 in parathyroid tumors (review) | Parafibromin-deficient tumor spectrum (adenoma/APT/PC) |
| [39775826](https://pubmed.ncbi.nlm.nih.gov/39775826/) | Genotype-phenotype in HPT-JT | Start-loss→MEST; truncating→carcinoma risk |
| [42400268](https://pubmed.ncbi.nlm.nih.gov/42400268/) | PC molecular pathogenesis/management | PI3K/AKT/mTOR + Wnt; imaging; recurrence 23–65% |
| [32247225](https://pubmed.ncbi.nlm.nih.gov/32247225/) | Parathyroid cancer update | 10-yr OS 60–70%; deaths from hypercalcemia |
| [40978536](https://pubmed.ncbi.nlm.nih.gov/40978536/) | Lenvatinib in metastatic PC | Targeted therapy; calcium-lowering agents critical |
| [28774260](https://pubmed.ncbi.nlm.nih.gov/28774260/) | Exon 4–10 deletion family | Need CNV/deletion screening in diagnostics |
| [34157106](https://pubmed.ncbi.nlm.nih.gov/34157106/) | Atypical parathyroid adenoma follow-up | Germline CDC73 in APA; FIHP younger (30±17 vs 55±13 y) |

**Source-type distribution:** human clinical (case reports, family studies, operative/pathology series, reviews) dominate; one validated mouse model ([PMID: 28288139](https://pubmed.ncbi.nlm.nih.gov/28288139/)); in vitro/structural ([PMID: 29142233](https://pubmed.ncbi.nlm.nih.gov/29142233/)); and invertebrate/yeast mechanistic work ([PMID: 16630820](https://pubmed.ncbi.nlm.nih.gov/16630820/); [PMID: 20339377](https://pubmed.ncbi.nlm.nih.gov/20339377/)).

---

## Limitations and Knowledge Gaps

1. **Rarity → small cohorts.** Most clinical evidence is from case reports and modest series; prevalence, incidence, and natural-history parameters are imprecise, and no large EHR/registry dataset for CDC73-specific disease was analyzed.
2. **Penetrance/expressivity estimates** derive from individual families (e.g., ~50% at age 40 in one deletion family) and may not generalize.
3. **Genotype-phenotype correlations**, though increasingly robust for carcinoma risk and the start-loss→MEST link, rest on retrospective, literature-aggregated cohorts.
4. **QOL and disability outcomes** specific to this syndrome are essentially unmeasured (no EQ-5D/SF-36/PROMIS data).
5. **Therapeutics for advanced carcinoma** remain anecdotal (single-case lenvatinib response); no controlled trials.
6. **Mechanistic branch** (Wnt oncogenic vs tumor-suppressive role of parafibromin) is context-dependent and unresolved; extra-parathyroid tumor mechanisms are inferred by analogy rather than directly demonstrated.
7. **Mouse model gaps:** jaw fibromas and the full renal spectrum are incompletely recapitulated.

---

## Proposed Follow-up Experiments / Actions

1. **Build a federated CDC73 variant–phenotype registry** linking germline/somatic variant class (NTD vs CTD, truncating vs missense) to carcinoma incidence, age of onset, and penetrance, to refine risk stratification prospectively.
2. **Prospective surveillance trial in carriers** comparing imaging/biochemical protocols to define optimal screening intervals and the value of pre-emptive parathyroidectomy.
3. **Functional dissection of CTD-specific mechanisms:** structure-function assays of C-terminal-domain mutations to explain why they specifically drive carcinoma (PAF1C integrity, chromatin occupancy, Wnt output).
4. **Conditional, tissue-specific Cdc73 mouse models** (parathyroid-, renal-, jaw-, uterus-specific) to test the inferred biallelic-loss mechanism in extra-parathyroid tissues and improve jaw/renal recapitulation.
5. **Targeted-therapy trials** (mTOR inhibitors, multikinase inhibitors, immunotherapy) in CDC73-mutant parathyroid carcinoma, with parafibromin/Ki-67/mTOR biomarkers as stratifiers.
6. **Standardize parafibromin IHC** as a reflex test for atypical/malignant parathyroid tumors to trigger CDC73 germline testing and cascade screening.
7. **Patient-reported-outcome study** to quantify QOL and disability in CDC73 carriers across the disease continuum.

---

*Report compiled from a 5-iteration autonomous investigation; 7 confirmed findings; 54 papers reviewed. All mechanistic and clinical claims are attributed to the cited primary literature with verified PMIDs. Causal gene: **CDC73** (parafibromin), chromosome 1q31.2.*


## Artifacts

- [OpenScientist final report](Hyperparathyroidism_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hyperparathyroidism_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 28 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 18 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007767` (4 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **hyperparathyroidism 1**
- `HP:0008207` (1 mention) - the report calls it "Laboratory/clinical"; HP calls it **Primary adrenal insufficiency**
- `HP:0003072` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Hypercalcemia**
- `HP:0003165` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Elevated circulating parathyroid hormone level**
- `HP:0002148` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Hypophosphatemia**
- `HP:0002897` (1 mention) - the report calls it "Neoplasm"; HP calls it **Parathyroid adenoma**
- `HP:0006780` (1 mention) - the report calls it "Neoplasm"; HP calls it **Parathyroid carcinoma**
- `HP:0010766` (1 mention) - the report calls it "Jaw neoplasm"; HP calls it **Ectopic calcification**
- `HP:0002756` (1 mention) - the report calls it "Clinical sign"; HP calls it **Pathologic fracture**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016570` (obsolete histone modification) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000131` (1 mention) - the report calls it "Uterine neoplasm"; HP calls it **Uterine leiomyoma**
- `GO:0006368` (1 mention) - the report calls it "transcription elongation by RNA Pol II"; GO calls it **transcription elongation by RNA polymerase II**
- `GO:0016570` (1 mention) - the report calls it "histone modification"; GO calls it **obsolete histone modification**
- `CL:0000446` (2 mentions) - the report calls it "chief cells"; CL calls it **chief cell of parathyroid gland**, and lists "parathyroid chief cell" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0007767` - called "if available", "MONDO"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.
