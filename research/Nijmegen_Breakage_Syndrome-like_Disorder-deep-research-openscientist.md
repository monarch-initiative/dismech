---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-31T05:17:41.936023'
end_time: '2026-07-31T05:42:21.545889'
duration_seconds: 1479.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Nijmegen Breakage Syndrome-like Disorder
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Nijmegen_Breakage_Syndrome-like_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Nijmegen_Breakage_Syndrome-like_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nijmegen Breakage Syndrome-like Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Nijmegen Breakage Syndrome-like Disorder** covering all of the
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

# Nijmegen Breakage Syndrome-like Disorder (NBSLD / RAD50 Deficiency): A Comprehensive Disease Characteristics Report

*Disease category: Mendelian (autosomal recessive) · Gene: RAD50 · OMIM #613078 · MONDO:0013415 · Orphanet: NBS-like spectrum*

---

## Summary

**Nijmegen breakage syndrome-like disorder (NBSLD) is an ultra-rare, autosomal-recessive chromosomal-instability syndrome caused by biallelic loss-of-function or hypomorphic variants in *RAD50***, the gene encoding a core structural ATPase subunit of the MRE11–RAD50–NBS1 (MRN) complex. The MRN complex is the primary cellular sensor of DNA double-strand breaks (DSBs); it recruits and activates the ATM kinase, initiating the DNA damage response (DDR). When RAD50 protein is absent or destabilized, cells cannot assemble DNA-damage-induced MRN foci, fail to activate ATM properly, lose cell-cycle checkpoint control, exhibit radioresistant DNA synthesis, and accumulate chromosomal instability. The clinical consequence is a syndrome dominated by congenital **microcephaly**, **pre- and post-natal growth restriction**, a **"bird-like" facial appearance**, and **mild intellectual disability**.

The disorder was first defined molecularly in 2009 (Waltes et al., [PMID: 19409520](https://pubmed.ncbi.nlm.nih.gov/19409520/)) in a single patient who was compound heterozygous for *RAD50* mutations. Crucially, that index patient — unlike patients with classic Nijmegen breakage syndrome (NBS, caused by *NBN*/nibrin mutations) — never had severe infections, had normal immunoglobulin levels, and had not developed lymphoid malignancy by age 23. This distinction (microcephaly and growth failure **without** the severe immunodeficiency/lymphoma of NBS) is the defining feature of the RAD50 phenotype, although subsequent case reports have broadened the spectrum to include bone-marrow failure and B-cell immunodeficiency in some patients.

Because only a handful of unrelated patients have been reported worldwide since 2009, there are no formal prevalence or incidence figures; every reported variant is "private" (family-specific) with no founder mutation. Diagnosis rests on whole-exome sequencing or DNA-repair gene panels combined with **functional confirmation** in patient fibroblasts (radiosensitivity, radioresistant DNA synthesis, absent MRN foci, impaired ATM activation, and rescue by wild-type RAD50). Management is entirely supportive: growth and developmental support, surveillance of blood counts and immune function, strict avoidance of ionizing radiation and dose-reduced genotoxic chemotherapy given the radiosensitivity, and allogeneic hematopoietic stem-cell transplantation (HSCT) reserved for those who develop marrow failure. No curative or disease-specific therapy exists. Heterozygous carriers are relevant to counseling because at least one *RAD50* loss-of-function allele has been classified as a moderate-risk breast-cancer allele.

---

## 1. Disease Information

**Overview.** NBSLD is a Mendelian DNA-repair-deficiency disorder within the family of chromosomal-instability syndromes that also includes ataxia-telangiectasia (A-T, *ATM*), ataxia-telangiectasia-like disorder (ATLD, *MRE11*), and classic Nijmegen breakage syndrome (NBS, *NBN*/nibrin). All four converge on the MRN–ATM DSB-signaling axis. NBSLD specifically denotes the RAD50-deficiency phenotype, which clinically resembles NBS (microcephaly, bird-like face, growth and mental retardation, cellular radiosensitivity) but is caused by mutations in *RAD50* rather than *NBN*.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #613078 (Nijmegen breakage syndrome-like disorder) |
| MONDO | MONDO:0013415 |
| Gene (HGNC) | RAD50, HGNC:9816 |
| NCBI Gene | 10111 |
| UniProt | Q92878 |
| Ensembl / locus | 5q31.1; RefSeq NM_005732 |
| Orphanet | NBS-like spectrum (chromosomal instability syndromes) |

**Synonyms / alternative names.** RAD50 deficiency; NBS-like disorder; NBSLD; Nijmegen breakage syndrome-like disorder due to RAD50 deficiency.

**Information source.** The knowledge base is derived almost entirely from **aggregated disease-level resources and individual published case reports** (a handful of patients worldwide), supplemented by in vitro functional studies of patient-derived cells and model-organism data — not from large EHR cohorts.

---

## 2. Etiology

**Disease causal factors — genetic.** NBSLD is caused by **biallelic (homozygous or compound heterozygous) loss-of-function/hypomorphic variants in *RAD50***. RAD50 is one of three obligate subunits of the MRN complex; when the protein is absent or destabilized, MRN cannot properly sense DSBs or activate ATM. In the index patient, compound heterozygous *RAD50* mutations produced only low levels of unstable RAD50 protein, and the cellular defect was fully rescued by expression of wild-type RAD50, establishing RAD50 as the direct cause ([PMID: 19409520](https://pubmed.ncbi.nlm.nih.gov/19409520/)).

> *"We found that she is compound heterozygous for mutations in the RAD50 gene that give rise to low levels of unstable RAD50 protein. Cells from the patient were characterized by chromosomal instability; radiosensitivity; failure to form DNA damage-induced MRN foci; and impaired radiation-induced activation of and downstream signaling through the ATM protein."* ([PMID: 19409520](https://pubmed.ncbi.nlm.nih.gov/19409520/))

**Genetic risk factors.** The causal variants are the biallelic *RAD50* alleles themselves. No independent modifier or susceptibility loci have been established given the tiny patient population.

**Environmental risk factors.** No environmental cause initiates the disease — it is fully genetic. However, because the defect is in DSB repair, **ionizing radiation and radiomimetic/genotoxic chemicals are dangerous exposures** that exacerbate genomic instability and should be minimized.

**Protective factors.** No genetic or environmental protective factors are established. Conceptually, in DSB-repair-deficient microcephaly models, genetic co-deletion of *TP53* rescues progenitor cell death (see Mechanism), but this is a mechanistic observation, not a clinical protective factor.

**Gene–environment interactions.** The principal clinically relevant interaction is **genotype × ionizing radiation**: RAD50-deficient cells are hypersensitive to radiation, so radiation exposure (diagnostic or therapeutic) produces disproportionate DNA damage and chromosomal instability. This underlies the clinical mandate to avoid radiotherapy and minimize CT imaging.

---

## 3. Phenotypes

The core phenotype is remarkably consistent across reported patients, with variable hematologic/immune involvement. Frequencies are qualitative given the tiny cohort.

| Phenotype | Type | Suggested HPO term | Onset | Frequency (qualitative) |
|---|---|---|---|---|
| Microcephaly (often severe/congenital) | Physical/structural | HP:0000252 (Microcephaly); HP:0011451 (Congenital microcephaly) | Congenital/neonatal | Universal |
| Pre/post-natal growth restriction, short stature | Physical | HP:0001511 (IUGR); HP:0004322 (Short stature) | Prenatal onset | Universal |
| "Bird-like" face (sloping forehead, midface prominence, receding mandible) | Clinical sign | HP:0000271 (Abnormal facial shape); HP:0000347 (Micrognathia) | Congenital | Common |
| Mild intellectual disability / developmental delay | Behavioral/cognitive | HP:0001256 (Intellectual disability, mild) | Childhood | Common |
| Bone-marrow failure | Laboratory/clinical | HP:0005528 (Bone marrow hypocellularity) | Childhood | Variable (subset) |
| B-cell immunodeficiency / lymphopenia | Laboratory | HP:0005479 (B-cell immunodeficiency); HP:0001888 (Lymphopenia) | Childhood | Variable (subset) |
| Café-au-lait macules | Physical | HP:0000957 (Café-au-lait spot) | Childhood | Reported |
| Brachydactyly / skeletal features | Physical | HP:0001156 (Brachydactyly) | Congenital | Reported |
| Cryptorchidism (bilateral) | Physical | HP:0000028 (Cryptorchidism) | Congenital | Reported (male patient) |
| Cellular radiosensitivity / chromosomal instability | Laboratory | HP:0003220 (Chromosomal breakage) | Constitutive | Universal (cellular hallmark) |

**Key distinction from classic NBS.** The index patient *"never had severe infections, had normal immunoglobulin levels, and did not develop lymphoid malignancy up to age 23 years"* ([PMID: 19409520](https://pubmed.ncbi.nlm.nih.gov/19409520/)). This milder immunologic/oncologic profile separates RAD50 deficiency from *NBN*-driven NBS. However, Takagi et al. 2023 reported a girl *"with microcephaly, mental retardation, bird-like face, short stature, bone marrow failure and B-cell immunodeficiency"* ([PMID: 37794136](https://pubmed.ncbi.nlm.nih.gov/37794136/)), showing hematologic/immune involvement is part of the spectrum in some individuals. Sun et al. 2026 described a 6-year-old boy who *"presented with bilateral cryptorchidism, severe microcephaly, growth retardation, multiple café-au-lait macules, brachydactyly, and distinctive craniofacial features, including a sloping forehead, midface prominence, and receding mandible. Mild intellectual impairment was confirmed"* ([PMID: 41655867](https://pubmed.ncbi.nlm.nih.gov/41655867/)).

**Progression and severity.** Microcephaly and growth restriction are congenital and structurally non-progressive; intellectual disability is generally mild and stable. Marrow failure, when present, is progressive and life-threatening.

**Quality-of-life impact.** Microcephaly with mild intellectual disability affects educational attainment and independence; short stature affects psychosocial well-being; marrow failure/immunodeficiency (when present) markedly reduce QoL and survival. No formal EQ-5D/SF-36 data exist for this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene.** *RAD50* (HGNC:9816; NCBI Gene 10111; UniProt Q92878; locus 5q31.1; RefSeq NM_005732). RAD50 encodes a ~1,312-amino-acid SMC-family ATPase with N- and C-terminal Walker A/B ATPase motifs joined by long antiparallel coiled-coils and a central CXXC **zinc-hook** that dimerizes RAD50 and tethers the two ends of a broken DNA molecule.

**Structural role within MRN.** Cryo-EM shows that *"MRN senses DSBs through a tight clamp-like sensing state with closed coiled-coil domains, but auto-inhibited MRE11 nuclease. NBS1 wraps around the MRE11 dimer, with NBS1's ATM recruitment motif sequestered by binding to the regulatory RAD50 S site, necessitating a switch in the NBS1 C helix for ATM activation"* ([PMID: 40968163](https://pubmed.ncbi.nlm.nih.gov/40968163/)). RAD50 thus directly gates ATM activation through its regulatory "S site," explaining why RAD50 loss impairs ATM signaling.

**Reported pathogenic variants in NBSLD (all biallelic, autosomal recessive, private — no founder):**

| Patient / study | Variant(s) (protein) | Type | PMID |
|---|---|---|---|
| Waltes 2009 (index) | Compound het; low unstable RAD50 protein | LOF/hypomorphic | [19409520](https://pubmed.ncbi.nlm.nih.gov/19409520/) |
| Ragamin 2020 | Homozygous c.2524G>A (exon 15) → aberrant splicing/truncation | Splice/LOF | [32212377](https://pubmed.ncbi.nlm.nih.gov/32212377/) |
| Takagi 2023 | p.Arg83His + p.Glu485Ter | Missense + nonsense | [37794136](https://pubmed.ncbi.nlm.nih.gov/37794136/) |
| Sun 2026 (Chinese child) | c.2165_2166insT (p.Lys722Asnfs*6) + c.3752+4_3752+7dup splice | Frameshift + splice | [41655867](https://pubmed.ncbi.nlm.nih.gov/41655867/) |
| Novel case 2026 | p.His1269Argfs*2 + p.Ser844Asn | Frameshift + missense | [41798197](https://pubmed.ncbi.nlm.nih.gov/41798197/) |

> *"compound heterozygosity for two variants in RAD50 (NM_005732.3): a paternally inherited frameshift variant c.2165_2166insT (p.Lys722Asnfs*6) and a maternally inherited splice-site variant c.3752 + 4_3752 + 7dup"* ([PMID: 41655867](https://pubmed.ncbi.nlm.nih.gov/41655867/))

**Variant classification & functional consequence.** All reported variants are pathogenic/likely-pathogenic **loss-of-function or hypomorphic**, producing reduced or unstable RAD50 protein — i.e., a loss-of-function mechanism (not gain-of-function or dominant-negative). Splice variants have been confirmed pathogenic by minigene assays and radioresistant DNA synthesis in patient fibroblasts.

**Somatic vs germline.** All disease-causing variants are germline. (Somatic RAD50/MRN dysregulation is separately implicated in cancer biology but is not the disease mechanism here.)

**Modifier genes.** None formally established for NBSLD. TP53 dosage is a mechanistic modifier of the downstream apoptotic phenotype in model systems.

**Epigenetic information / chromosomal abnormalities.** No specific disease-defining methylation signature or large-scale chromosomal rearrangement; the hallmark is **acquired chromosomal instability** (breaks, radiation-induced aberrations) secondary to defective DSB repair, not a constitutional cytogenetic abnormality.

---

## 5. Environmental Information

- **Environmental factors:** No environmental agent causes NBSLD. Ionizing radiation is a hazard that worsens genomic instability in the radiosensitive cells (relevant to diagnostic imaging and radiotherapy).
- **Lifestyle factors:** None established as causal or protective.
- **Infectious agents:** Not applicable as a cause. Recurrent/severe infections may occur secondary to immunodeficiency in the subset with immune involvement.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

```
Biallelic RAD50 LOF variants
        │  (reduced / unstable RAD50 protein)
        ▼
Destabilized MRE11–RAD50–NBS1 (MRN) complex
        │  (cannot sense DSBs; NBS1 ATM-recruitment switch fails)
        ▼
Failure to form DNA-damage-induced MRN foci
        │
        ▼
Impaired ATM kinase activation & downstream DDR signaling
        │
        ├── Defective G1/S checkpoint
        ├── Radioresistant DNA synthesis (S-phase checkpoint failure)
        ├── G2 accumulation
        └── Chromosomal instability + cellular radiosensitivity
        │
        ▼
Unrepaired DSBs in rapidly proliferating progenitors
        │  (esp. neural progenitor cells)
        ▼
p53 (TP53)-dependent apoptosis of progenitors
        │
        ▼
Depletion of progenitor pool & reduced tissue growth
        │
        ▼
MICROCEPHALY + GROWTH RESTRICTION (± marrow failure)
```

**Molecular pathways & cellular processes.** The central pathway is the **MRN–ATM DNA double-strand-break response / DNA damage checkpoint signaling**. Suggested GO biological-process terms: GO:0006302 (double-strand break repair), GO:0000724 (DSB repair via homologous recombination), GO:0006281 (DNA repair), GO:0031573 (mitotic intra-S DNA damage checkpoint), GO:0007095 (mitotic G2 DNA damage checkpoint), GO:0042769 (DNA damage response, detection of DNA damage), GO:0006977 (DNA-damage-induced cell cycle arrest by p53), GO:0006915 (apoptotic process).

**Protein dysfunction.** RAD50 loss is a loss-of-function of a structural ATPase; the MRN clamp cannot adopt the DSB-sensing state and cannot switch NBS1's C-helix to activate ATM ([PMID: 40968163](https://pubmed.ncbi.nlm.nih.gov/40968163/)). In the index patient, DNA-damage-induced ATM activation was abolished and restored by WT RAD50; Takagi 2023 similarly found *"DNA damage-induced activation of the ATM kinase was markedly decreased, which was restored by the expression of wild-type (WT) RAD50"* ([PMID: 37794136](https://pubmed.ncbi.nlm.nih.gov/37794136/)).

**Downstream apoptotic mechanism (microcephaly).** Evidence from DSB-repair-deficient microcephaly models indicates that unrepaired DSBs in proliferating neural progenitor cells (NPCs) trigger **p53-dependent apoptosis**, depleting the progenitor pool and producing microcephaly:

- In citron-kinase-deficient mice, *"in doubly CitK and Trp53 mutant mice, neural progenitor cell death is dramatically reduced; moreover, clinical and neuroanatomical phenotypes are remarkably improved"* ([PMID: 28199840](https://pubmed.ncbi.nlm.nih.gov/28199840/)).
- Conditional *Ino80* deletion from cortical NPCs *"impairs DNA double-strand break (DSB) repair, triggering p53-dependent apoptosis and microcephaly"* ([PMID: 32737294](https://pubmed.ncbi.nlm.nih.gov/32737294/)).

**In vivo consequences of MRN dysfunction.** Hypomorphic Mre11-complex mouse alleles reveal that *"the DNA repair, rather than DDR signaling functions of the complex, is acutely required in the context of ATM deficiency to suppress genome instability and lymphomagenesis"* ([PMID: 26538284](https://pubmed.ncbi.nlm.nih.gov/26538284/)), establishing genome instability and cancer predisposition as in-vivo consequences of MRN/RAD50 dysfunction.

**Cell types & compartments.** Principally affected cell types: neural progenitor cells (CL:0011020), hematopoietic stem/progenitor cells (CL:0008001), lymphocytes/B cells (CL:0000236). Subcellular compartment: nucleus (GO:0005634); the MRN complex acts at sites of nuclear DNA damage (GO:0035861, site of double-strand break).

**Immune involvement.** Because MRN/ATM signaling participates in V(D)J recombination and class-switch recombination, RAD50 hypofunction can impair lymphocyte development, producing B-cell immunodeficiency and lymphopenia in a subset ([PMID: 37794136](https://pubmed.ncbi.nlm.nih.gov/37794136/)).

**Molecular profiling.** No large-scale transcriptomic/proteomic/metabolomic disease signatures have been published for this ultra-rare disorder; the mechanistic evidence is functional/cell-biological.

---

## 7. Anatomical Structures Affected

- **Primary organs / systems:** Central nervous system — brain, especially cerebral cortex (UBERON:0000955 brain; UBERON:0000956 cerebral cortex) → microcephaly. Whole-body growth (skeletal system, UBERON:0002204) → growth restriction/short stature. Craniofacial skeleton → bird-like facies.
- **Secondary/variable involvement:** Bone marrow / hematopoietic system (UBERON:0002371) → marrow failure; immune system (UBERON:0002405) → B-cell immunodeficiency; reproductive (cryptorchidism); skin (café-au-lait macules).
- **Tissue/cell level:** Proliferating progenitor populations — neural progenitors (CL:0011020) and hematopoietic progenitors (CL:0008001) — are most vulnerable because DSB burden is highest in rapidly dividing cells.
- **Subcellular level:** Nucleus (GO:0005634), specifically chromatin at DSB sites (GO:0035861).
- **Localization / lateralization:** Microcephaly is symmetric/bilateral; craniofacial and growth features are generalized and symmetric.

---

## 8. Temporal Development

- **Onset:** Congenital. Microcephaly and growth restriction are present prenatally (intrauterine growth restriction) and at birth; developmental delay becomes apparent in early childhood.
- **Onset pattern:** Chronic/constitutive (a developmental disorder, not acute).
- **Progression:** Structural/neurodevelopmental features are static/non-progressive. Intellectual disability is stable and mild. When present, **bone-marrow failure is progressive** and may be life-limiting. Cellular radiosensitivity and cancer risk are lifelong.
- **Disease course:** Chronic, lifelong.
- **Critical periods:** Prenatal and early-childhood neurodevelopment (window during which progenitor apoptosis determines brain size). Lifelong vulnerability window for radiation-induced damage and malignancy.

---

## 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (biallelic *RAD50* variants; affected individuals are homozygous or compound heterozygous). Unaffected parents are obligate carriers.
- **Epidemiology:** Ultra-rare. Only a handful of unrelated patients/families reported worldwide since 2009. Sun et al. 2026: *"Merely few cases have been reported worldwide, and its phenotypic spectrum remains incompletely defined"* ([PMID: 41655867](https://pubmed.ncbi.nlm.nih.gov/41655867/)). No reliable prevalence or incidence figures exist.
- **Penetrance / expressivity:** Biallelic LOF appears fully penetrant for microcephaly/growth restriction; expressivity is variable for hematologic/immune features (present in some, absent in others).
- **Founder effects / consanguinity:** No founder mutation; all variants are private. Homozygous cases (e.g., Ragamin 2020's splice variant) imply a role for consanguinity/shared ancestry in some families.
- **Carrier relevance (breast cancer):** In a population-based Northern Finnish study (2,343 breast-cancer cases vs 4,607 controls), heterozygous RAD50 loss-of-function was a **moderate-risk breast-cancer allele**: *"CHEK2 c.1100delC, MCPH1 c.909_921del, and RAD50 c.687delT were moderate-risk alleles"* ([PMID: 40009290](https://pubmed.ncbi.nlm.nih.gov/40009290/)). Carriers warrant counseling about cancer risk even though they do not have NBSLD.
- **Sex ratio:** Both sexes affected; no sex bias expected for an autosomal recessive disorder.

---

## 10. Diagnostics

**Diagnostic approach.** Clinical suspicion is triggered by congenital microcephaly, pre/post-natal growth restriction, bird-like facies, and mild intellectual disability. This prompts **trio-based whole-exome sequencing (WES)** or **DNA-repair gene panels**, which identify the biallelic *RAD50* variants. Splice variants are confirmed by minigene assays ([PMID: 41655867](https://pubmed.ncbi.nlm.nih.gov/41655867/)); variants are Sanger-validated and segregation-tested in parents ([PMID: 41798197](https://pubmed.ncbi.nlm.nih.gov/41798197/)).

**Functional / cellular confirmation (essential given VUS abundance in a private-variant disease).** Patient-derived primary fibroblasts are used to demonstrate:
- reduced/absent RAD50 protein by immunoblot;
- cellular radiosensitivity (colony-survival assays);
- **radioresistant DNA synthesis** — *"Using patient-derived primary fibroblasts, we could show abnormal radioresistant DNA synthesis confirming pathogenicity of the identified variant"* ([PMID: 32212377](https://pubmed.ncbi.nlm.nih.gov/32212377/));
- absent DNA-damage-induced MRN foci;
- impaired ATM activation;
- **rescue by wild-type RAD50 complementation** — *"The defective cellular phenotype was rescued by wild-type RAD50"* ([PMID: 19409520](https://pubmed.ncbi.nlm.nih.gov/19409520/)).

**Laboratory / clinical tests.** Complete blood count (cytopenias/marrow failure), immunoglobulin levels and lymphocyte subsets (immunodeficiency), chromosomal breakage studies (spontaneous and radiation-induced), and brain MRI to characterize microcephaly.

**Clinical criteria / differential diagnosis.** Differential includes classic NBS (*NBN*), ATLD (*MRE11*), ataxia-telangiectasia (*ATM*), LIG4 syndrome, and other microcephalic primordial dwarfism/DSB-repair disorders. Distinguishing features: RAD50 deficiency shows microcephaly + growth failure with generally milder immunodeficiency and (in the index case) no lymphoma, versus prominent immunodeficiency/lymphoma of NBS and the ataxia (without microcephaly) of ATLD.

**Screening.** No newborn or population screening exists (too rare). Cascade carrier testing of relatives and prenatal/preimplantation testing are options once familial variants are known.

---

## 11. Outcome / Prognosis

- **Survival / life expectancy:** Not formally quantified due to rarity. Prognosis is driven by (a) severity of neurodevelopmental impairment, (b) presence of bone-marrow failure/immunodeficiency, and (c) cancer development. Patients without marrow failure or malignancy (e.g., the index patient followed to age 23) can have relatively stable long-term courses.
- **Morbidity:** Mild intellectual disability, short stature, and (variable) immune/hematologic disease. Café-au-lait macules and skeletal features add to the phenotype but are not typically disabling.
- **Complications:** Bone-marrow failure, B-cell immunodeficiency/recurrent infections, and predisposition to malignancy (genome instability). By analogy to MRN-complex dysfunction, lymphomagenesis is a theoretical concern, though the index RAD50 patient had not developed lymphoma by age 23.
- **Prognostic factors:** Presence and severity of marrow failure and immunodeficiency are the key adverse prognostic indicators; radiosensitivity constrains oncologic treatment options.

---

## 12. Treatment

There is **no curative or disease-specific therapy**. Management is supportive and symptom-directed. Suggested MAXO terms in brackets.

- **Supportive / rehabilitative care:** Growth monitoring, developmental and educational support, physical/occupational/speech therapy as indicated [MAXO:0000506 therapeutic intervention]. Surveillance of blood counts and immune function.
- **Endocrine caution:** Recombinant human growth hormone has been tried for short stature, but administering it without prior genetic evaluation is inappropriate — highlighted by a case in which GH was prescribed before the underlying RAD50 diagnosis was recognized ([PMID: 41798197](https://pubmed.ncbi.nlm.nih.gov/41798197/)). Growth-promoting therapy in a genome-instability disorder must weigh theoretical proliferation/cancer risks.
- **Hematopoietic stem-cell transplantation (HSCT):** Reserved for those who develop bone-marrow failure/immunodeficiency. *"Allogeneic hematopoietic stem cell transplantation (HSCT) has been proposed as a potential therapeutic option for DNA damage repair disorders. However, it is not presently required"* in patients without marrow failure ([PMID: 41655867](https://pubmed.ncbi.nlm.nih.gov/41655867/)) [MAXO:0000827 bone marrow transplantation].
- **Radiation / chemotherapy precautions:** Because cells are radiosensitive and chromosomally unstable, **ionizing radiation should be minimized/avoided** (diagnostic and therapeutic), and radiomimetic/genotoxic chemotherapy dose-reduced if malignancy arises — mirroring reduced-intensity protocols established for classic NBS.
- **Pharmacogenomics / targeted / gene / cell / RNA therapies:** None established for NBSLD. Gene-replacement/gene-editing is conceptually attractive (WT-RAD50 rescues the cellular phenotype in vitro) but not clinically available.

---

## 13. Prevention

- **Primary prevention:** Not applicable to disease occurrence (genetic). Genetic counseling for at-risk couples and reproductive options (prenatal diagnosis, preimplantation genetic testing) once familial variants are identified. Avoiding unnecessary ionizing radiation in affected individuals is harm prevention.
- **Secondary prevention:** Cascade testing of relatives; early identification enables surveillance of blood counts/immune function and radiation avoidance before complications arise.
- **Tertiary prevention:** Monitoring for and early management of marrow failure, infections, and malignancy; infection prophylaxis and immunoglobulin support in immunodeficient patients (extrapolated from NBS management).
- **Counseling:** Autosomal-recessive recurrence risk (25% for carrier couples); carrier relatives should be informed of the moderate breast-cancer risk of heterozygous *RAD50* LOF ([PMID: 40009290](https://pubmed.ncbi.nlm.nih.gov/40009290/)).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *RAD50* is deeply conserved. Orthologs: mouse *Rad50* (NCBI Gene 19360), and functional homologs in *S. cerevisiae* (RAD50) and *S. pombe*; the MRN/MRX complex is conserved across eukaryotes.
- **Natural disease in other species:** No well-characterized naturally occurring RAD50-deficiency syndrome is documented in companion animals (OMIA) analogous to human NBSLD; the comparative knowledge base is experimental (engineered models) rather than natural disease.
- **Evolutionary conservation:** The MRN complex and its role in DSB sensing/ATM activation are conserved from yeast to humans, making lower-organism studies informative about mechanism.

---

## 15. Model Organisms

- **Mouse (primary model):** Complete *Rad50* knockout is **embryonic lethal**, so disease modeling relies on **hypomorphic alleles** of the Mre11-complex, which model DSB-repair defects, genome instability, and lymphomagenesis, and reveal ATM-independent repair functions: *"Hypomorphic alleles of MRE11 and NBS1 confer embryonic lethality in ATM-deficient mice, indicating that the complex exerts ATM-independent functions that are essential when ATM is absent"* ([PMID: 26538284](https://pubmed.ncbi.nlm.nih.gov/26538284/)).
- **Related MRN models:** Transgenic mice expressing reduced wild-type MRN or the MRE11-ATLD1 allele exhibit small body size, anemia, bone-marrow failure, extramedullary hematopoiesis, and impaired lymphocyte development — recapitulating hematopoietic aspects of MRN-deficiency disorders ([PMID: 41075274](https://pubmed.ncbi.nlm.nih.gov/41075274/)).
- **Microcephaly models (mechanistic surrogates):** Citron-kinase-deficient ([PMID: 28199840](https://pubmed.ncbi.nlm.nih.gov/28199840/)) and Ino80-deficient ([PMID: 32737294](https://pubmed.ncbi.nlm.nih.gov/32737294/)) mice recapitulate the DSB-repair-failure → p53-apoptosis → microcephaly axis and, importantly, show *TP53* co-deletion rescues progenitor death — supporting the mechanistic model for NBSLD microcephaly.
- **Lower organisms:** *S. cerevisiae* and *S. pombe* (Mre11-Rad50-Nbs1/Xrs2 = MRX/MRN) provide conserved insight into DSB processing and ATM(Tel1) regulation.
- **Model limitations:** No mouse fully recapitulates the specific human RAD50-hypomorph NBSLD phenotype; knockout lethality forces reliance on hypomorphs and related-subunit models, and murine models may not capture the milder human neurocognitive phenotype.

---

## Mechanistic Model / Interpretation

NBSLD is best understood as a **"DSB-sensing failure"** disorder. RAD50 is a structural cornerstone of the MRN clamp that (1) tethers broken DNA ends via its zinc-hook and coiled-coils and (2) gates ATM activation through its regulatory S site controlling NBS1's ATM-recruitment switch. Biallelic hypomorphic RAD50 variants reduce or destabilize the protein, so MRN cannot fold into its DSB-sensing state. The proximal cellular result is loss of DNA-damage-induced MRN foci and blunted ATM activation — directly demonstrated in patient cells and rescued by WT RAD50 in two independent studies ([PMID: 19409520](https://pubmed.ncbi.nlm.nih.gov/19409520/); [PMID: 37794136](https://pubmed.ncbi.nlm.nih.gov/37794136/)).

Downstream, the DDR checkpoint network fails: G1/S checkpoint is defective, DNA synthesis becomes radioresistant, cells accumulate in G2, and chromosomal instability ensues. In the developing organism, the tissues that suffer most are those with the highest proliferative demand — neural and hematopoietic progenitors. Unrepaired DSBs in these progenitors activate **p53-dependent apoptosis**, depleting the progenitor pool. This is the crux linking a housekeeping DNA-repair defect to the tissue-specific clinical picture of **microcephaly and growth restriction**, and it is the same paradigm validated genetically (via *Trp53* rescue) in independent microcephaly models. The variable hematologic/immune involvement reflects the same progenitor-apoptosis mechanism operating in bone marrow plus impaired MRN/ATM-dependent V(D)J and class-switch recombination.

The distinction from classic NBS is instructive: both diseases hit the same MRN–ATM axis, yet *NBN* mutations produce prominent immunodeficiency and lymphoma while *RAD50* mutations produce a comparatively milder immune/oncologic phenotype (at least in the index patient). This likely reflects subunit-specific residual functions and the particular hypomorphic nature of the reported RAD50 alleles.

---

## Evidence Base

| PMID | Study | Contribution |
|---|---|---|
| [19409520](https://pubmed.ncbi.nlm.nih.gov/19409520/) | Waltes 2009 — *Human RAD50 deficiency in a NBS-like disorder* | **Defining paper.** Compound-het RAD50, unstable protein, absent MRN foci, impaired ATM, checkpoint failure, chromosomal instability; rescued by WT RAD50. |
| [32212377](https://pubmed.ncbi.nlm.nih.gov/32212377/) | Ragamin 2020 — *Confirmation of a distinctive phenotype* | Homozygous splice variant; radioresistant DNA synthesis confirms pathogenicity. |
| [37794136](https://pubmed.ncbi.nlm.nih.gov/37794136/) | Takagi 2023 — *Bone marrow failure & immunodeficiency* | Expands phenotype; ATM activation decreased, rescued by WT RAD50. |
| [41655867](https://pubmed.ncbi.nlm.nih.gov/41655867/) | Sun 2026 — *Expanding the mutational spectrum (Chinese child)* | New private biallelic variants; documents rarity; HSCT indication. |
| [41798197](https://pubmed.ncbi.nlm.nih.gov/41798197/) | 2026 case report | Novel variants p.His1269Argfs*2 + p.Ser844Asn; cautionary GH-before-diagnosis narrative. |
| [40968163](https://pubmed.ncbi.nlm.nih.gov/40968163/) | Cryo-EM of MRN | Structural basis of DSB sensing and RAD50-gated ATM activation. |
| [26538284](https://pubmed.ncbi.nlm.nih.gov/26538284/) | Mre11-complex mouse model | In vivo genome instability/lymphomagenesis; ATM-independent MRN repair functions. |
| [28199840](https://pubmed.ncbi.nlm.nih.gov/28199840/) | CitK/Trp53 mice | p53-dependent progenitor apoptosis drives microcephaly; TP53 rescue. |
| [32737294](https://pubmed.ncbi.nlm.nih.gov/32737294/) | Ino80 NPC model | DSB-repair failure → p53 apoptosis → microcephaly. |
| [40009290](https://pubmed.ncbi.nlm.nih.gov/40009290/) | Finnish breast-cancer study | Heterozygous RAD50 LOF is a moderate breast-cancer risk allele (carrier counseling). |
| [41075274](https://pubmed.ncbi.nlm.nih.gov/41075274/) | MRE11-ATLD1 mouse | Low MRN → anemia, marrow failure, impaired lymphocyte development. |

---

## Limitations and Knowledge Gaps

1. **Extreme rarity.** Only a handful of unrelated patients reported worldwide; conclusions rest on case reports and functional assays, not cohorts. No prevalence, incidence, survival, or QoL data exist.
2. **Private-variant genetics.** Every variant is family-specific with no founder allele, complicating variant interpretation and making functional assays essential for diagnosis.
3. **Phenotypic spectrum incompletely defined.** Whether marrow failure/immunodeficiency and cancer risk are core or occasional features is unresolved; longer follow-up is needed to establish lifetime malignancy risk.
4. **No dedicated RAD50-hypomorph mouse** fully models the human disease; knockout lethality forces reliance on related-subunit and general microcephaly models. The p53-apoptosis causal chain is inferred from analogous DSB-repair models, not proven directly in RAD50-deficient neural tissue.
5. **No omics data.** No transcriptomic/proteomic/metabolomic disease signatures exist for NBSLD.
6. **No disease-specific therapy or trials.** Management is extrapolated from NBS and general DNA-repair-disorder practice.

---

## Proposed Follow-up Experiments / Actions

1. **International patient registry / natural-history study** to aggregate scattered cases and define the true phenotypic spectrum, lifetime cancer risk, and survival.
2. **Standardized functional-assay panel** (RAD50 immunoblot, radiosensitivity, radioresistant DNA synthesis, MRN-foci, ATM activation, WT-RAD50 rescue) to classify VUS reproducibly across labs.
3. **RAD50-hypomorph mouse or human iPSC-derived cerebral organoid models** carrying patient variants to directly test the p53-dependent progenitor-apoptosis mechanism and evaluate whether p53/apoptosis modulation preserves progenitor pools.
4. **Prospective hematologic/immune surveillance protocol** to determine who progresses to marrow failure and to define HSCT timing.
5. **Carrier-counseling guidance** integrating the moderate breast-cancer risk of heterozygous RAD50 LOF into family cascade testing.
6. **Careful re-evaluation of growth-hormone use** in genome-instability disorders, given the theoretical proliferation/cancer risk and the reported instance of GH prescribed before genetic diagnosis.

---

*Report compiled from 6 confirmed findings and 31 reviewed papers over 5 investigation iterations. Evidence types span human clinical case reports, in vitro patient-cell functional studies, model-organism genetics, and structural biology.*


## Artifacts

- [OpenScientist final report](Nijmegen_Breakage_Syndrome-like_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Nijmegen_Breakage_Syndrome-like_Disorder-deep-research-openscientist_artifacts/final_report.pdf)