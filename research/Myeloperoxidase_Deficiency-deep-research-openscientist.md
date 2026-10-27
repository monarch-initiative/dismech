---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-23T19:11:01.247350'
end_time: '2026-09-23T19:38:01.219531'
duration_seconds: 1619.97
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Myeloperoxidase Deficiency
  mondo_id: MONDO:0009694
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Myeloperoxidase_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Myeloperoxidase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myeloperoxidase Deficiency
- **MONDO ID:** MONDO:0009694 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Myeloperoxidase Deficiency** covering all of the
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

# Myeloperoxidase Deficiency: A Comprehensive Disease Characteristics Report

**Disease:** Myeloperoxidase Deficiency
**MONDO ID:** MONDO:0009694 | **OMIM:** #254600 | **Gene:** *MPO* (17q22.1) | **Category:** Mendelian (autosomal recessive)

---

## Summary

Myeloperoxidase (MPO) deficiency is the **most common inherited disorder of neutrophil function**, occurring in roughly **1 in 2,000 to 4,000 individuals** in Western populations, yet it is paradoxically one of the most clinically silent primary immunodeficiencies known ([PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/)). The disorder arises from biallelic loss-of-function missense mutations in the *MPO* gene (e.g., R569W, Y173C, M251T) that cause the misfolded proMPO precursor to be retained in the endoplasmic reticulum via prolonged interaction with the chaperone calnexin, followed by proteasomal degradation. The result is neutrophils and monocytes that contain precursor protein but lack mature, enzymatically active MPO, peroxidase activity, and the capacity to generate chlorinating oxidants ([PMID: 10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/)).

The central biological function lost in MPO deficiency is the enzyme's unique ability to use chloride as a co-substrate with hydrogen peroxide to generate **hypochlorous acid (HOCl)**, a potent antimicrobial oxidant ([PMID: 17592500](https://pubmed.ncbi.nlm.nih.gov/17592500/)). Despite this, most affected individuals never develop clinical disease because the NADPH-oxidase-derived oxidant burst and other non-oxidative microbicidal systems compensate. The dominant clinical exception is **disseminated candidiasis**, which typically emerges only when a "second hit"—most classically **diabetes mellitus**—independently impairs residual antifungal killing ([PMID: 2831185](https://pubmed.ncbi.nlm.nih.gov/2831185/); [PMID: 216438](https://pubmed.ncbi.nlm.nih.gov/216438/)).

This report synthesizes seven confirmed findings across the full disease-characteristics template. The overarching narrative is one of a **biochemistry-versus-clinical paradox**: a complete and readily detectable enzymatic defect that is, in isolation, biologically well-tolerated. Because MPO-derived oxidants also drive inflammatory tissue damage and vascular disease, low-MPO states may even be partially protective against atherosclerotic cardiovascular disease and certain cancers, positioning MPO as a genuine "double-edged sword."

---

## Key Findings

### Finding 1 — MPO deficiency is the most common inherited neutrophil enzyme defect and is usually clinically silent

Hereditary MPO deficiency occurs in **1 in 2,000 to 4,000 individuals** in the general population and has traditionally been regarded as an autosomal recessive trait ([PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/)). Despite this high prevalence, the overwhelming majority of affected individuals are entirely asymptomatic. The explanation is functional redundancy: NADPH-oxidase-derived reactive oxygen species and non-oxidative microbicidal systems (defensins, proteases, lactoferrin) provide sufficient host defense in the absence of MPO-generated HOCl. Clinically significant sequelae are largely restricted to a subset of patients who carry an additional predisposing condition. As the classic review states, *"In the absence of MPO, auxiliary mechanisms protect most MPO-deficient hosts from clinically significant sequelae, except for some persons with diabetes mellitus who suffer severe candidal disease"* ([PMID: 2831185](https://pubmed.ncbi.nlm.nih.gov/2831185/)).

**Evidence quote:** *"Hereditary deficiency of MPO occurs in 1 in 2,000 to 4,000 individuals in the general population and has been generally considered an autosomal recessive trait."* ([PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/))

### Finding 2 — The molecular lesion: MPO missense mutations cause ER retention and defective post-translational maturation

Inherited MPO deficiency results from missense mutations in the *MPO* gene. The best-characterized alleles are **R569W**, **Y173C**, and **M251T**. In the Y173C genotype, the mutant proMPO precursor is retained in the endoplasmic reticulum through prolonged interaction with the chaperone **calnexin** and is ultimately degraded by the **20S proteasome**. Consequently, affected neutrophils contain the precursor protein but lack mature MPO subunits, peroxidase enzymatic activity, and chlorination capacity ([PMID: 10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/)). The R569W mutation is the most frequently encountered allele; most studied patients are **compound heterozygotes** for R569W and demonstrate a spectrum of phenotypes ranging from complete to partial deficiency ([PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/)). These mutations have served as a model system for understanding endoplasmic-reticulum quality control of secretory proteins more broadly ([PMID: 15507769](https://pubmed.ncbi.nlm.nih.gov/15507769/)).

**Evidence quotes:**
- *"In the genotype Y173C, the mutant precursor is retained in the endoplasmic reticulum by virtue of its prolonged interaction with calnexin, and it eventually undergoes degradation in the 20S proteasome."* ([PMID: 10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/))
- *"Most subjects were compound heterozygotes with respect to the R569W mutation and demonstrated a spectrum of phenotypes."* ([PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/))

### Finding 3 — Animal models: MPO contributes to fungicidal defense, but NADPH oxidase is dominant

MPO-knockout (MPO⁻/⁻) mice develop normally but exhibit **severely reduced cytotoxicity** toward *Candida albicans*, *Aspergillus fumigatus*, *Cryptococcus neoformans*, and *Klebsiella pneumoniae*, confirming that the MPO-dependent oxidative system is important for antifungal and antibacterial host defense ([PMID: 15507755](https://pubmed.ncbi.nlm.nih.gov/15507755/)). Head-to-head comparison with NADPH-oxidase-deficient (X-linked chronic granulomatous disease, X-CGD) mice reveals a clear hierarchy: X-CGD mice suffer shorter survival and 10–100× higher fungal tissue burdens than MPO⁻/⁻ mice. Critically, MPO cannot function without NADPH-oxidase-derived hydrogen peroxide, which is its obligate substrate. **However**, at the highest *Candida* inocula, the mortality of MPO⁻/⁻ mice approached that of CGD mice, indicating that MPO becomes rate-limiting under a heavy pathogen load ([PMID: 12521119](https://pubmed.ncbi.nlm.nih.gov/12521119/); [PMID: 16940954](https://pubmed.ncbi.nlm.nih.gov/16940954/)).

**Evidence quotes:**
- *"Both MPO-deficient (MPO-/-) and NADPH-oxidase-deficient (X-linked chronic granulomatous disease [X-CGD]) mice showed increased susceptibility to pulmonary infections with Candida albicans and Aspergillus fumigatus compared with normal mice, and the X-CGD mice exhibited shorter survivals than MPO-/- mice."* ([PMID: 12521119](https://pubmed.ncbi.nlm.nih.gov/12521119/))
- *"MPO is unable to play a role in host defense in the absence of NADPH-oxidase."* ([PMID: 12521119](https://pubmed.ncbi.nlm.nih.gov/12521119/))

### Finding 4 — The core enzymatic reaction: H₂O₂ + Cl⁻ → HOCl, a double-edged sword

MPO is a member of the heme peroxidase-cyclooxygenase superfamily and is abundantly stored in the azurophilic (primary) granules of neutrophils. Its **unique catalytic activity** is the use of chloride as a co-substrate with hydrogen peroxide to generate **hypochlorous acid (HOCl)**, a potent antimicrobial agent ([PMID: 17592500](https://pubmed.ncbi.nlm.nih.gov/17592500/)). This same chemistry is a liability: MPO-derived oxidants contribute to host tissue damage and to the initiation and propagation of acute and chronic vascular inflammatory disease, and circulating MPO levels predict adverse cardiac events. HOCl oxidatively modifies proteins—through amino-acid side-chain modification, backbone fragmentation, and aggregation—driving chronic inflammatory pathology ([PMID: 31867603](https://pubmed.ncbi.nlm.nih.gov/31867603/)). This dual nature is the mechanistic foundation for why loss of MPO can be biologically tolerated and even confer protection in some disease contexts.

**Evidence quotes:**
- *"A unique activity of MPO is its ability to use chloride as a cosubstrate with hydrogen peroxide to generate chlorinating oxidants such as hypochlorous acid, a potent antimicrobial agent."* ([PMID: 17592500](https://pubmed.ncbi.nlm.nih.gov/17592500/))
- *"MPO-derived oxidants contribute to tissue damage and the initiation and propagation of acute and chronic vascular inflammatory disease."* ([PMID: 17592500](https://pubmed.ncbi.nlm.nih.gov/17592500/))

### Finding 5 — Classification and diagnosis: a primary immunodeficiency detected incidentally by hematology analyzers

MPO deficiency is listed among the primary immunodeficiencies that predispose to fungal infection ([PMID: 17551753](https://pubmed.ncbi.nlm.nih.gov/17551753/)). Its high apparent prevalence is itself an artifact of modern laboratory medicine: *"the relatively high prevalence of inherited MPO deficiency was an unanticipated insight provided by the widespread use of automated flow cytometry for the enumeration of leukocytes in clinical specimens"* ([PMID: 10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/)). Automated hematology analyzers use the peroxidase (MPO) channel to perform leukocyte differentials, so MPO-deficient neutrophils are flagged incidentally in otherwise healthy people. Confirmation relies on **cytochemical peroxidase staining** of blood smears—MPO-deficient neutrophils and monocytes are peroxidase-negative while eosinophils remain positive (via eosinophil peroxidase, EPO)—and on direct MPO enzyme-activity assays. A known diagnostic pitfall is that EPO, which is normally expressed in MPO-deficient subjects, can confound leukocyte peroxidase measurements through eosinophil contamination ([PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/)).

**Evidence quotes:**
- *"the relatively high prevalence of inherited MPO deficiency was an unanticipated insight provided by the widespread use of automated flow cytometry for the enumeration of leukocytes in clinical specimens."* ([PMID: 10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/))
- *"Eosinophil peroxidase (EPO) also contributes to the peroxidase activity of blood leukocytes. Because EPO expression is normal in MPO-deficient subjects, eosinophil contamination can significantly contribute to peroxidase activity."* ([PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/))

### Finding 6 — The MPO trade-off: low-expression -463A allele protects the heart but a high-expression genotype raises cancer risk

Distinct from the rare loss-of-function missense mutations that cause hereditary deficiency, a **common functional promoter polymorphism, -463 G>A (rs2333227)**, quantitatively modifies MPO expression: the G allele confers higher expression than the A allele ([PMID: 11479475](https://pubmed.ncbi.nlm.nih.gov/11479475/)). In French-Canadians, the low-expression **AA genotype was associated with markedly decreased coronary artery disease (CAD) risk** (recessive model OR 0.138, 95% CI 0.040–0.474), and carriage of the A allele (AA/AG vs GG) was protective (OR 0.639, 95% CI 0.436–0.937). Conversely, the high-expression **GG genotype hastened hepatocellular carcinoma** in HCV-related cirrhosis (HR 2.8, 95% CI 1.7–4.4; [PMID: 21907168](https://pubmed.ncbi.nlm.nih.gov/21907168/)), and higher MPO activity has been implicated in leukemia and lung cancer through metabolic activation of carcinogens such as benzene ([PMID: 17479404](https://pubmed.ncbi.nlm.nih.gov/17479404/)). These associations extend the biological "double-edged sword" to the population-genetics level, though some studies find no relationship between the promoter polymorphisms and neutrophil MPO release or cardiovascular risk ([PMID: 19877306](https://pubmed.ncbi.nlm.nih.gov/19877306/)), so the effect is modest and not fully reproducible.

**Evidence quotes:**
- *"In a recessive model patients with the AA genotype had a decreased risk of CAD (odds ratio 0.138, 95% confidence interval 0.040-0.474)."* ([PMID: 11479475](https://pubmed.ncbi.nlm.nih.gov/11479475/))
- *"the G allele associated with a higher level of MPO expression than the A allele."* ([PMID: 11479475](https://pubmed.ncbi.nlm.nih.gov/11479475/))
- *"HCC occurrence was increased in patients with either the homozygous GG-MPO genotype (HR=2.8 [1.7-4.4])."* ([PMID: 21907168](https://pubmed.ncbi.nlm.nih.gov/21907168/))

### Finding 7 — The clinical phenotype is unmasked by a second hit: diabetes mellitus converts silent deficiency into candidal susceptibility

The classic clinical scenario for symptomatic MPO deficiency is a **diabetic patient with disseminated or invasive candidiasis**. In a landmark case, an MPO-deficient diabetic patient's granulocytes showed normal phagocytosis but microbicidal activity that was *"almost nil with regard to Candida albicans"*; crucially, *"Fungicidal activity of normal granulocytes was shown to be impaired during the in vitro artificial hyperglycemic condition"*—demonstrating that hyperglycemia independently degrades residual killing ([PMID: 216438](https://pubmed.ncbi.nlm.nih.gov/216438/)). MPO-deficient diabetics have developed *Candida albicans* liver abscess ([PMID: 217268](https://pubmed.ncbi.nlm.nih.gov/217268/); [PMID: 199939](https://pubmed.ncbi.nlm.nih.gov/199939/)). Even in non-diabetics, disseminated pustular candidal dermatitis has occurred, particularly under limited-spectrum antibiotic therapy ([PMID: 9114158](https://pubmed.ncbi.nlm.nih.gov/9114158/)). The unifying principle from Nauseef is that clinically significant disease is limited *"except for some persons with diabetes mellitus who suffer severe candidal disease"* ([PMID: 2831185](https://pubmed.ncbi.nlm.nih.gov/2831185/)).

**Evidence quotes:**
- *"Fungicidal activity of normal granulocytes was shown to be impaired during the in vitro artificial hyperglycemic condition."* ([PMID: 216438](https://pubmed.ncbi.nlm.nih.gov/216438/))
- *"Patients who develop rapidly disseminated fungal dermatitis while they are receiving antimicrobial therapy that is relatively limited in coverage should be evaluated for myeloperoxidase deficiency."* ([PMID: 9114158](https://pubmed.ncbi.nlm.nih.gov/9114158/))

---

## Comprehensive Section-by-Section Report

### 1. Disease Information

Myeloperoxidase deficiency is an inherited disorder in which neutrophils and monocytes lack functional myeloperoxidase, the azurophilic-granule heme enzyme responsible for generating hypochlorous acid during the oxidative burst. It is the most common inherited defect of neutrophils. Two forms exist: **complete (total) deficiency** and **partial deficiency**, reflecting the genotype (homozygous vs. compound heterozygous / heterozygous for hypomorphic alleles).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0009694 |
| OMIM (phenotype) | #254600 |
| OMIM (gene) | *606989 |
| Gene (HGNC) | *MPO*, HGNC:7218 |
| Gene locus | 17q22.1 |
| UniProt (protein) | P05164 (PERM_HUMAN) |
| Orphanet | ORPHA:59181 |
| ICD-10 | D70/D72.0 (functional disorders of neutrophils) |
| MeSH | related to "Peroxidase" / "Leukocyte Disorders" |

**Synonyms / alternative names:** MPO deficiency; myeloperoxidase deficiency; hereditary myeloperoxidase deficiency; leukocyte myeloperoxidase deficiency; total/partial myeloperoxidase deficiency; Peroxidase deficiency.

**Source of information:** The knowledge base for this disorder is derived largely from **aggregated disease-level resources** (OMIM, primary case series, and reviews) combined with individual patient case reports; the high prevalence estimate itself derives from population-scale automated hematology analyzer data ([PMID: 10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/)).

### 2. Etiology

**Causal factors:** The disease is **genetic (Mendelian, autosomal recessive)**, caused by biallelic loss-of-function mutations in *MPO*. It is not infectious or environmental in origin, though environmental/clinical co-factors (see below) determine whether it is expressed clinically.

**Genetic risk factors:** Causal variants include the missense mutations **R569W** (the most common, [PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/)), **Y173C**, and **M251T** ([PMID: 10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/), [PMID: 15507769](https://pubmed.ncbi.nlm.nih.gov/15507769/)). The common promoter polymorphism **-463 G>A (rs2333227)** is a quantitative expression modifier rather than a cause of deficiency ([PMID: 11479475](https://pubmed.ncbi.nlm.nih.gov/11479475/)).

**Environmental/clinical risk factors for symptomatic disease (second hits):** **Diabetes mellitus / hyperglycemia** is the principal unmasking factor, as it independently impairs granulocyte fungicidal activity ([PMID: 216438](https://pubmed.ncbi.nlm.nih.gov/216438/)). Additional triggers include limited-spectrum antimicrobial therapy (allowing fungal overgrowth) ([PMID: 9114158](https://pubmed.ncbi.nlm.nih.gov/9114158/)) and high pathogen inoculum ([PMID: 12521119](https://pubmed.ncbi.nlm.nih.gov/12521119/)).

**Protective factors:** From the host-defense standpoint, an intact **NADPH oxidase** and non-oxidative microbicidal systems are the key compensatory/protective mechanisms ([PMID: 12521119](https://pubmed.ncbi.nlm.nih.gov/12521119/)). From a cardiovascular standpoint, the **low-expression -463A allele** may be protective against CAD ([PMID: 11479475](https://pubmed.ncbi.nlm.nih.gov/11479475/)).

**Gene–environment interaction:** The paradigmatic GxE interaction is **MPO genotype × diabetes mellitus**: neither alone produces disseminated candidiasis, but their combination does ([PMID: 216438](https://pubmed.ncbi.nlm.nih.gov/216438/); [PMID: 217268](https://pubmed.ncbi.nlm.nih.gov/217268/)). A second GxE axis is **MPO-463 genotype × carcinogen exposure** (e.g., benzene, tobacco smoke), where higher MPO activity enhances procarcinogen activation ([PMID: 17479404](https://pubmed.ncbi.nlm.nih.gov/17479404/)).

### 3. Phenotypes

Most individuals are **asymptomatic** (laboratory abnormality only). When present, phenotypes are infectious.

| Phenotype | Type | Onset | Severity | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Peroxidase-negative neutrophils/monocytes | Laboratory abnormality | Congenital | — | ~100% of affected | HP:0011990 (abnormal granulocyte morphology) / lab finding |
| Recurrent/disseminated candidiasis | Clinical sign / infection | Any age (typically adult) | Severe when present | Rare; mainly with diabetes | HP:0002728 (chronic mucocutaneous candidiasis) |
| Candidal (hepatic) abscess | Clinical sign | Adult | Severe | Rare | HP:0100523 (hepatic abscess) |
| Pustular candidal dermatitis | Physical manifestation | Variable | Moderate–severe | Rare | HP:0200037 (pustule) |
| Increased susceptibility to fungal/bacterial infection | Clinical sign | Variable | Mild–severe | Minority | HP:0002719 (recurrent infections) |

**Quality-of-life impact:** For the asymptomatic majority, there is **no measurable QoL impact**; the condition is compatible with normal life. For the rare symptomatic subset, invasive candidiasis carries substantial morbidity and potential mortality. No disease-specific EQ-5D/SF-36 data are available for MPO deficiency.

### 4. Genetic / Molecular Information

**Causal gene:** *MPO* (myeloperoxidase), chromosome **17q22.1**, OMIM gene *606989*; disease OMIM #254600. Protein: myeloperoxidase, UniProt **P05164**, a heme peroxidase-cyclooxygenase superfamily enzyme ([PMID: 17592500](https://pubmed.ncbi.nlm.nih.gov/17592500/)).

**Pathogenic variants:**

| Variant | Type | Consequence | Notes |
|---|---|---|---|
| R569W | Missense | Loss of function; defective maturation | Most common allele; often compound heterozygous ([PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/)) |
| Y173C | Missense | ER retention via calnexin; 20S proteasomal degradation | Model for ER quality control ([PMID: 10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/)) |
| M251T | Missense | Loss of function / defective maturation | ([PMID: 15507769](https://pubmed.ncbi.nlm.nih.gov/15507769/)) |
| -463 G>A (rs2333227) | Promoter SNP | Expression modifier (not causal) | Common quantitative variant ([PMID: 11479475](https://pubmed.ncbi.nlm.nih.gov/11479475/)) |

**Functional consequence:** **Loss of function** — absence of mature MPO subunits, peroxidase activity, and chlorination capacity ([PMID: 10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/)). **Origin:** germline. **Modifier genes:** *CYBB*/NADPH-oxidase components determine the functional consequence of MPO loss (compensatory); the *MPO* -463 promoter genotype modifies expression quantitatively. **Epigenetic / chromosomal abnormalities:** none characteristically associated with the Mendelian form.

### 5. Environmental Information

The disorder is genetically determined; environmental factors act only as **modifiers of clinical expression**. Relevant factors: **hyperglycemia/diabetes** (impairs residual fungicidal activity, [PMID: 216438](https://pubmed.ncbi.nlm.nih.gov/216438/)); **broad- vs. limited-spectrum antibiotic exposure** (fungal overgrowth risk, [PMID: 9114158](https://pubmed.ncbi.nlm.nih.gov/9114158/)); and **carcinogen exposure** interacting with MPO-463 genotype ([PMID: 17479404](https://pubmed.ncbi.nlm.nih.gov/17479404/)). **Infectious agents** are consequences, not causes: chiefly *Candida albicans*, and in models *Aspergillus fumigatus*, *Cryptococcus neoformans*, and *Klebsiella pneumoniae* ([PMID: 15507755](https://pubmed.ncbi.nlm.nih.gov/15507755/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (from genetic lesion to clinical manifestation):**

```
1. Biallelic MPO missense mutation (e.g., R569W, Y173C, M251T)
        │ leads to
2. Misfolded proMPO precursor
        │ leads to (Y173C) prolonged calnexin binding → ER retention
3. Proteasomal (20S) degradation of the precursor
        │ results in
4. Absence of mature, enzymatically active MPO in azurophilic granules
        │ results in
5. Loss of the reaction  H2O2 + Cl-  →  HOCl (hypochlorous acid)
        │ results in
6. Impaired oxidative (HOCl-mediated) microbial killing
        │
        ├── BRANCH A (usual outcome): NADPH oxidase + non-oxidative
        │    systems compensate → CLINICALLY SILENT
        │
        └── BRANCH B (second hit present, e.g., diabetes/hyperglycemia,
             or heavy pathogen inoculum): residual killing overwhelmed
                  │ leads to
             7. Failure to contain Candida albicans
                  │ leads to
             8. Disseminated / invasive candidiasis (e.g., hepatic abscess,
                pustular dermatitis) → CLINICAL DISEASE
```

A parallel, **beneficial branch** stems from step 5: because HOCl also damages host tissue and oxidatively modifies host proteins ([PMID: 31867603](https://pubmed.ncbi.nlm.nih.gov/31867603/)), reduced MPO oxidant output *lowers* vascular inflammatory injury, plausibly underlying the reduced CAD risk seen with the low-expression -463A allele ([PMID: 11479475](https://pubmed.ncbi.nlm.nih.gov/11479475/)).

**Molecular pathways / biochemistry:** The lost reaction is the halide-oxidation cycle of a heme peroxidase (Compound I / Compound II redox intermediates); MPO uniquely oxidizes chloride to HOCl ([PMID: 17592500](https://pubmed.ncbi.nlm.nih.gov/17592500/)). **Cellular processes:** neutrophil respiratory burst, phagolysosomal microbial killing, and inflammation. **Protein dysfunction:** misfolding → ER retention → proteasomal degradation (loss of function) ([PMID: 10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/)). **Immune involvement:** primary immunodeficiency of the innate/phagocytic arm ([PMID: 17551753](https://pubmed.ncbi.nlm.nih.gov/17551753/)). **Tissue-damage mechanism (the flip side):** HOCl-mediated oxidative protein modification, backbone fragmentation, and aggregation in chronic inflammation ([PMID: 31867603](https://pubmed.ncbi.nlm.nih.gov/31867603/)).

**Suggested ontology terms:** GO:0006979 (response to oxidative stress); GO:0042744 (hydrogen peroxide catabolic process); GO:0002446 (neutrophil mediated immunity); GO:0043312 (neutrophil degranulation). Chemicals: CHEBI:24757 (hypochlorous acid); CHEBI:16240 (hydrogen peroxide); CHEBI:17996 (chloride). Cell types: CL:0000775 (neutrophil), CL:0000576 (monocyte). Upstream = mutation/ER retention; downstream = impaired killing and infection.

### 7. Anatomical Structures Affected

- **Primary cells:** neutrophil granulocytes (CL:0000775) and monocytes (CL:0000576); eosinophils are spared (they express eosinophil peroxidase) ([PMID: 217268](https://pubmed.ncbi.nlm.nih.gov/217268/)).
- **Subcellular compartment:** azurophilic (primary) granules — GO:0042582 (azurophil granule); the enzymatic block occurs in the **endoplasmic reticulum** (GO:0005783) ([PMID: 10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/)).
- **Body system:** hematopoietic / innate immune system (UBERON:0002390 hematopoietic system; UBERON:0000178 blood).
- **Secondary organ involvement (only in symptomatic disease):** liver (candidal abscess; UBERON:0002107), skin (pustular candidal dermatitis; UBERON:0002097), and lungs in animal models (UBERON:0002048). Involvement is typically systemic/disseminated rather than lateralized.

### 8. Temporal Development

- **Onset:** the enzymatic defect is **congenital**; the laboratory abnormality is present from birth. Clinical infection, when it occurs, is usually **adult-onset** and tied to acquisition of a second hit (e.g., diabetes).
- **Course:** the underlying deficiency is **chronic and lifelong** but static. Infectious episodes are **episodic/acute**, precipitated by co-factors.
- **Progression:** the enzyme defect itself does not progress. There are no defined disease "stages." **Critical period for intervention:** aggressive antifungal therapy at the onset of disseminated candidiasis; and control of comorbid hyperglycemia as ongoing prophylaxis.

### 9. Inheritance and Population

- **Prevalence:** approximately **1 in 2,000 to 4,000** (≈25–50 per 100,000) for at least partial deficiency in Western populations; complete deficiency is rarer ([PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/)).
- **Inheritance:** **autosomal recessive** with **variable expressivity** ([PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/); [PMID: 199939](https://pubmed.ncbi.nlm.nih.gov/199939/)). Compound heterozygosity (especially involving R569W) is common.
- **Penetrance:** biochemically high (the enzyme defect is consistently detectable), but **clinical penetrance is very low** — most homozygotes/compound heterozygotes are asymptomatic.
- **Expressivity:** variable, from partial to complete enzyme loss and from silent to symptomatic ([PMID: 199939](https://pubmed.ncbi.nlm.nih.gov/199939/)).
- **Sex ratio / geography / founder effects:** no strong sex predilection or well-defined founder effect is established for the classic missense alleles; the -463 promoter allele frequencies vary by population ([PMID: 17479404](https://pubmed.ncbi.nlm.nih.gov/17479404/)).

### 10. Diagnostics

- **Incidental detection:** flagged by **automated hematology analyzers** using the peroxidase (MPO) channel during routine leukocyte differentials ([PMID: 10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/)).
- **Confirmatory tests:** **cytochemical peroxidase staining** of a peripheral blood smear (neutrophils/monocytes peroxidase-negative, eosinophils positive) and **MPO enzyme-activity assays** ([PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/); [PMID: 217268](https://pubmed.ncbi.nlm.nih.gov/217268/)).
- **Diagnostic pitfall:** eosinophil peroxidase (EPO), normally expressed in MPO-deficient subjects, can contribute to measured leukocyte peroxidase and confound results ([PMID: 9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/)).
- **Distinguishing from CGD:** flow-cytometric assays of the oxidative burst (e.g., dihydrorhodamine-123) are normal in MPO deficiency but abnormal in chronic granulomatous disease—an important differential ([PMID: 7813334](https://pubmed.ncbi.nlm.nih.gov/7813334/)).
- **Genetic testing:** *MPO* single-gene sequencing / immunodeficiency gene panels can confirm biallelic variants; useful for family counseling but not required for diagnosis.
- **Differential diagnosis:** chronic granulomatous disease (NADPH-oxidase defect), other neutrophil functional disorders, and secondary/acquired MPO deficiency (e.g., myelodysplasia, certain drugs).

### 11. Outcome / Prognosis

- **Overall prognosis is excellent.** Most individuals have **normal life expectancy** and no increased infection burden.
- **Mortality/morbidity** is confined to the rare symptomatic subset with invasive candidiasis, where outcome depends on prompt antifungal therapy and control of comorbid conditions ([PMID: 2831185](https://pubmed.ncbi.nlm.nih.gov/2831185/); [PMID: 217268](https://pubmed.ncbi.nlm.nih.gov/217268/)).
- **Prognostic factors:** presence of diabetes mellitus/hyperglycemia, completeness of enzyme deficiency, pathogen inoculum, and breadth of antimicrobial coverage ([PMID: 216438](https://pubmed.ncbi.nlm.nih.gov/216438/); [PMID: 12521119](https://pubmed.ncbi.nlm.nih.gov/12521119/)).
- **Potential benefit:** reduced MPO oxidant load may lower atherosclerotic cardiovascular risk ([PMID: 11479475](https://pubmed.ncbi.nlm.nih.gov/11479475/)), an unusual "protective" dimension of an immunodeficiency.

### 12. Treatment

- **No specific therapy** exists or is required for the enzyme deficiency itself.
- **Management is directed at infections and comorbidities:** prompt **antifungal therapy** for candidiasis (e.g., azoles, echinocandins, lipid amphotericin B formulations, which have expanded options for fungal infection in primary immunodeficiencies, [PMID: 17551753](https://pubmed.ncbi.nlm.nih.gov/17551753/)) and **tight glycemic control** in diabetic patients as the single most important preventive measure ([PMID: 216438](https://pubmed.ncbi.nlm.nih.gov/216438/)).
- **Antibiotic stewardship:** avoiding unnecessary limited-spectrum regimens that promote fungal overgrowth ([PMID: 9114158](https://pubmed.ncbi.nlm.nih.gov/9114158/)).
- **Advanced/gene therapy:** none developed or indicated given the benign natural history. **NCIT suggestions:** NCIT:C305 (Amphotericin B), NCIT:C1471 (antifungal agent), NCIT:C1505 (azole antifungal).

### 13. Prevention

- **Primary prevention:** not applicable to the genetic defect; **genetic counseling** for affected families (autosomal recessive recurrence risk) is appropriate.
- **Secondary/tertiary prevention:** the highest-yield intervention is **prevention and control of diabetes/hyperglycemia** to avoid unmasking clinical disease ([PMID: 216438](https://pubmed.ncbi.nlm.nih.gov/216438/)); clinical vigilance for candidal infection in at-risk deficient patients; and judicious antibiotic use ([PMID: 9114158](https://pubmed.ncbi.nlm.nih.gov/9114158/)).
- **Screening:** no population-based newborn screening is indicated because clinical penetrance is very low; incidental analyzer detection effectively serves as opportunistic case-finding.

### 14. Other Species / Natural Disease

- **Model species with MPO orthologs:** *Mus musculus* (mouse *Mpo*), used in knockout studies ([PMID: 15507755](https://pubmed.ncbi.nlm.nih.gov/15507755/)). MPO is evolutionarily conserved within the heme peroxidase-cyclooxygenase superfamily ([PMID: 17592500](https://pubmed.ncbi.nlm.nih.gov/17592500/)).
- **Comparative biology:** the mouse MPO⁻/⁻ phenotype (impaired fungicidal activity, normal development) parallels the human condition, supporting conserved mechanism ([PMID: 12521119](https://pubmed.ncbi.nlm.nih.gov/12521119/)). No prominent naturally occurring companion-animal MPO deficiency disorder is documented in the reviewed literature. Not zoonotic.

### 15. Model Organisms

- **Primary model:** **MPO-knockout (MPO⁻/⁻) mouse** ([PMID: 15507755](https://pubmed.ncbi.nlm.nih.gov/15507755/)).
- **Comparator model:** **X-linked CGD (NADPH-oxidase-deficient) mouse**, and **MPO⁻/⁻ × X-CGD double knockouts**, used to dissect the relative contributions of MPO vs. the oxidase ([PMID: 12521119](https://pubmed.ncbi.nlm.nih.gov/12521119/)).
- **Phenotype recapitulation:** good — MPO⁻/⁻ mice develop normally but show reduced antifungal killing, matching the human "silent-except-under-stress" phenotype; at high inoculum they approach CGD-level mortality, mirroring the human second-hit phenomenon ([PMID: 15507755](https://pubmed.ncbi.nlm.nih.gov/15507755/); [PMID: 16940954](https://pubmed.ncbi.nlm.nih.gov/16940954/)).
- **Limitations:** murine neutrophil biology differs from human; models do not fully capture the diabetes-interaction axis or human population genetics of the -463 polymorphism.
- **In vitro systems:** patient granulocyte functional assays and neutrophil lysate MPO-activity assays have been central to mechanistic work ([PMID: 216438](https://pubmed.ncbi.nlm.nih.gov/216438/); [PMID: 19877306](https://pubmed.ncbi.nlm.nih.gov/19877306/)).

---

## Mechanistic Model / Interpretation

MPO deficiency is best understood as a **conditional, redundancy-buffered immunodeficiency**. The genetic lesion reliably abolishes a specific biochemical capability—HOCl generation—yet the clinical system it feeds into is robust because a parallel, more powerful effector (NADPH oxidase) and non-oxidative killing remain intact. This explains the disease's defining paradox: a 100%-penetrant biochemical defect with near-0% clinical penetrance.

The **"double-edged sword"** framing unifies the seemingly disparate findings:

| Context | MPO/HOCl HIGH | MPO/HOCl LOW (deficiency or -463A) |
|---|---|---|
| Antifungal defense | Effective killing | Impaired (Findings 3, 4) |
| Under a second hit (diabetes, heavy inoculum) | Protected | Susceptible → candidiasis (Finding 7) |
| Vascular inflammation / CAD | Higher risk | Reduced risk (Finding 6) |
| Carcinogen activation (leukemia, HCC) | Higher risk (GG genotype) | Reduced risk (Finding 6) |

The clinical decision node is the **second hit**. Absent one, the deficiency is a laboratory curiosity; present one, it can produce life-threatening invasive fungal disease. Diabetes is the archetype because hyperglycemia independently degrades the residual killing capacity that would otherwise compensate.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [9468285](https://pubmed.ncbi.nlm.nih.gov/9468285/) | *Inheritance & R569W mutation* | Prevalence, AR inheritance, compound heterozygosity, EPO diagnostic pitfall |
| [10482305](https://pubmed.ncbi.nlm.nih.gov/10482305/) | *ER quality control, MPO deficiency* | ER retention/calnexin/proteasome mechanism; incidental analyzer diagnosis |
| [15507769](https://pubmed.ncbi.nlm.nih.gov/15507769/) | *Structural features from MPO deficiency* | Catalog of causal missense mutations |
| [15507755](https://pubmed.ncbi.nlm.nih.gov/15507755/) | *In vivo role of MPO* | MPO-KO fungicidal defect |
| [12521119](https://pubmed.ncbi.nlm.nih.gov/12521119/) | *MPO vs NADPH-oxidase* | Relative contributions; MPO depends on oxidase |
| [16940954](https://pubmed.ncbi.nlm.nih.gov/16940954/) | *MPO in antifungal defense (review)* | High-inoculum equivalence with CGD |
| [17592500](https://pubmed.ncbi.nlm.nih.gov/17592500/) | *MPO: drug target?* | Core HOCl chemistry; tissue-damage duality |
| [31867603](https://pubmed.ncbi.nlm.nih.gov/31867603/) | *HOCl protein modification* | Tissue-damage mechanism |
| [11479475](https://pubmed.ncbi.nlm.nih.gov/11479475/) | *MPO -463 & CAD (French-Canadians)* | Protective low-expression allele |
| [21907168](https://pubmed.ncbi.nlm.nih.gov/21907168/) | *MPO promoter & HCC* | High-expression genotype raises cancer risk |
| [17479404](https://pubmed.ncbi.nlm.nih.gov/17479404/) | *MPO SNPs & leukemia* | Carcinogen-activation trade-off |
| [216438](https://pubmed.ncbi.nlm.nih.gov/216438/) | *Hereditary MPO deficiency (case)* | Hyperglycemia impairs fungicidal activity |
| [217268](https://pubmed.ncbi.nlm.nih.gov/217268/) | *MPO deficiency + diabetes + Candida liver abscess* | Second-hit clinical syndrome |
| [9114158](https://pubmed.ncbi.nlm.nih.gov/9114158/) | *Pustular candidal dermatitis* | Non-diabetic trigger; management advice |
| [2831185](https://pubmed.ncbi.nlm.nih.gov/2831185/) | *MPO deficiency (review)* | Clinical silence except diabetic candidiasis |
| [17551753](https://pubmed.ncbi.nlm.nih.gov/17551753/) | *Fungal infections in PIDs* | Classifies MPO deficiency among PIDs |
| [7813334](https://pubmed.ncbi.nlm.nih.gov/7813334/) | *Flow cytometry for CGD variants* | DHR assay distinguishes MPO deficiency from CGD |
| [19877306](https://pubmed.ncbi.nlm.nih.gov/19877306/) | *MPO promoter SNPs & neutrophil activation* | Challenges reproducibility of -463 CVD link |
| [199939](https://pubmed.ncbi.nlm.nih.gov/199939/) | *Hereditary MPO deficiency (genetics)* | AR transmission, variable expressivity |

**Challenging/qualifying evidence:** [PMID: 19877306](https://pubmed.ncbi.nlm.nih.gov/19877306/) found no relationship between the -129/-463 promoter polymorphisms and neutrophil MPO release or reactive oxygen production, cautioning that the -463/CVD association is modest and inconsistently reproducible. This tempers Finding 6.

---

## Limitations and Knowledge Gaps

1. **No primary dataset was analyzed** — this is a literature-synthesis report; findings rest on published case series, reviews, and mouse models rather than newly generated statistics.
2. **Prevalence uncertainty** — the 1:2,000–4,000 figure is Western/analyzer-derived and may not generalize globally; complete vs. partial deficiency proportions are imprecise.
3. **Clinical penetrance is not precisely quantified** — the fraction of deficient individuals who ever develop candidiasis, and its dependence on diabetes severity, lacks large cohort estimates.
4. **-463 polymorphism associations are inconsistent** — cardiovascular and cancer associations vary across populations and are not robustly reproducible ([PMID: 19877306](https://pubmed.ncbi.nlm.nih.gov/19877306/)).
5. **Genotype–phenotype granularity** — beyond R569W/Y173C/M251T, the full variant spectrum, allele frequencies (gnomAD), and ACMG classifications were not exhaustively enumerated here.
6. **Human GxE quantification** — the diabetes × MPO interaction is well-supported mechanistically but not quantified with modern epidemiology.

---

## Proposed Follow-up Experiments / Actions

1. **Quantify clinical penetrance** via a registry/EHR cohort of MPO-deficient individuals stratified by diabetes status, estimating the absolute and relative risk of invasive candidiasis.
2. **Comprehensive variant curation** — mine ClinVar/gnomAD for the full *MPO* pathogenic variant spectrum, allele frequencies, and ACMG/AMP classifications; report carrier frequencies by ancestry.
3. **Meta-analysis of the -463 G>A polymorphism** across cardiovascular and oncologic endpoints to resolve the reproducibility conflict between [PMID: 11479475](https://pubmed.ncbi.nlm.nih.gov/11479475/) and [PMID: 19877306](https://pubmed.ncbi.nlm.nih.gov/19877306/).
4. **Mechanistic modeling of the second hit** — in vitro MPO-deficient neutrophils under controlled glucose to dissect how hyperglycemia degrades residual (NADPH-oxidase-dependent) *Candida* killing.
5. **Test the cardiovascular-protection hypothesis prospectively** in genetically confirmed complete MPO-deficient individuals (atherosclerosis imaging vs. matched controls).
6. **HPO/ontology annotation package** — formalize the phenotype-frequency table above into HP-term associations for the disease knowledge base, with CL:0000775 (neutrophil), UBERON, and CHEBI:24757 (hypochlorous acid) links.

---

*Report compiled from a 5-iteration autonomous investigation; 7 confirmed findings; 28 papers reviewed. Evidence source types span human clinical case series/reviews, mouse knockout models, and in vitro neutrophil assays.*


## Artifacts

- [OpenScientist final report](Myeloperoxidase_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Myeloperoxidase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 20 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009694` (3 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **myeloperoxidase deficiency**
- `HP:0200037` (1 mention) - the report calls it "pustule"; HP calls it **Skin vesicle**
- `NCIT:C305` (1 mention) - the report calls it "Amphotericin B"; NCIT calls it **Bilirubin**
- `NCIT:C1471` (1 mention) - the report calls it "antifungal agent"; NCIT calls it **Lamivudine**
- `NCIT:C1505` (1 mention) - the report calls it "azole antifungal"; NCIT calls it **Dietary Supplement**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011990` (1 mention) - the report calls it "abnormal granulocyte morphology"; HP calls it **Abnormal neutrophil physiology**
- `CL:0000775` (3 mentions) - the report calls it "neutrophil", "Primary cells:** neutrophil granulocytes"; CL calls it **neutrophil**, and lists "neutrophil leucocyte" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0009694` - called "if available", "MONDO"
- `CL:0000775` - called "neutrophil", "Primary cells:** neutrophil granulocytes"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
