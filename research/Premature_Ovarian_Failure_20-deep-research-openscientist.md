---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T20:30:12.342771'
end_time: '2026-10-19T21:01:24.975054'
duration_seconds: 1872.63
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Premature Ovarian Failure 20
  mondo_id: MONDO:0030975
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
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Premature_Ovarian_Failure_20-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Premature_Ovarian_Failure_20-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Premature Ovarian Failure 20
- **MONDO ID:** MONDO:0030975 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Premature Ovarian Failure 20** covering all of the
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

# Premature Ovarian Failure 20 (POF20 / MSH4-related Primary Ovarian Insufficiency): A Comprehensive Disease Characterization

**Disease:** Premature Ovarian Failure 20 (POF20)
**Primary identifiers:** MONDO:0030975 · OMIM:619938 · UMLS:C5677011 · MedGen:1808256 · GARD:0025670
**Causal gene:** MSH4 (HGNC:7327; NCBI Gene 4438; Ensembl ENSG00000057468; UniProt O15457; gene-OMIM *602105; locus 1p31.1)
**Inheritance:** Autosomal recessive (HP:0000007)
**Category:** Mendelian

> **Evidence-source key:** [H] human clinical; [M] model organism; [V] in-vitro/biochemical; [C] computational/database. Primary literature cited as PMIDs.

---

## Summary

Premature Ovarian Failure 20 (POF20; MONDO:0030975, OMIM 619938) is a rare, Mendelian, **autosomal-recessive** form of primary/premature ovarian insufficiency (POI) caused by **biallelic loss-of-function variants in the meiosis-specific gene *MSH4* (MutS Homolog 4)**, located at chromosome 1p31.1. It was first delineated in 2017 by Carlosama and colleagues, who identified a homozygous donor splice-site variant in a consanguineous Colombian family [PMID: 28541421](https://pubmed.ncbi.nlm.nih.gov/28541421/). Multiple independent biallelic variants have since confirmed the gene–disease relationship across diverse cohorts.

Mechanistically, POF20 is a disease of **failed meiotic recombination**. MSH4 heterodimerizes with MSH5 to form the **MutSγ complex**, which binds and stabilizes Holliday-junction recombination intermediates and licenses the downstream MLH1–MLH3 (MutLγ) resolvase (with EXO1 and RFC-PCNA) to convert double Holliday junctions into crossovers. When MSH4 is lost, crossovers fail to form, homologous chromosomes cannot pair/synapse, meiosis I arrests, and oocytes are eliminated by apoptosis. The resulting depletion of the ovarian follicle pool produces the clinical phenotype: **young-adult-onset secondary amenorrhea, female infertility, and hypergonadotropic hypogonadism** (elevated FSH and LH). Because the meiotic requirement is shared between sexes, the identical biallelic genotype causes **non-obstructive azoospermia (NOA)** in affected male relatives — the male counterpart is annotated as spermatogenic failure (SPGF2).

There is **no disease-modifying or curative therapy**. Management, per the 2024 ESHRE/ASRM/IMS evidence-based POI guideline, centers on **hormone replacement therapy (HRT)** until the average age of natural menopause (~51 years) to prevent the sequelae of premature estrogen deprivation (osteoporosis, cardiovascular disease, adverse cognitive/sexual health, increased all-cause mortality), together with bone-health monitoring and psychological support. Because meiosis is abolished, own-oocyte conception is essentially non-viable; **donor-oocyte (or donor-embryo) IVF** is the principal fertility option.

---

## Key Findings

### Finding 1 — POF20 is caused by biallelic loss-of-function variants in *MSH4* and is inherited autosomal-recessively [H]

POF20 maps unambiguously to the identifier set **OMIM:619938 / MONDO:0030975 / UMLS:C5677011 / GARD:0025670**. The Monarch Initiative records a Causal-Gene-to-Disease association linking **HGNC:7327 (MSH4)** to POF20 with **autosomal recessive inheritance (HP:0000007)**. The disease was first described by Carlosama et al. (2017), who used whole-exome sequencing in a consanguineous Colombian family to identify a **homozygous donor splice-site mutation** causing skipping of exon 17 (p.Ile743_Lys785del). The variant segregated with POI and was absent in 135 fertile controls.

> *"Whole-exome sequencing of members of a Colombian family affected by POI allowed us to identify a novel homozygous donor splice-site mutation in the meiotic gene MSH4 (MutS Homolog 4)."* — [PMID: 28541421](https://pubmed.ncbi.nlm.nih.gov/28541421/)

> *"Our study describes the first MSH4 mutation associated with POI."* — [PMID: 28541421](https://pubmed.ncbi.nlm.nih.gov/28541421/)

Multiple independent biallelic variants have since confirmed the association, including reports from large POI gene-panel and exome cohorts [PMID: 36099812](https://pubmed.ncbi.nlm.nih.gov/36099812/), [PMID: 36793102](https://pubmed.ncbi.nlm.nih.gov/36793102/), [PMID: 36373164](https://pubmed.ncbi.nlm.nih.gov/36373164/), and [PMID: 38175272](https://pubmed.ncbi.nlm.nih.gov/38175272/).

> **Note on causal-gene correction:** Early in this investigation the gene was provisionally listed as MCM8. This was corrected to **MSH4**, which is the gene formally linked to OMIM 619938 / POF20. MCM8 defects cause a distinct POI entity (POF10 / OMIM 612885 — see [PMID: 25873734](https://pubmed.ncbi.nlm.nih.gov/25873734/), [PMID: 32048466](https://pubmed.ncbi.nlm.nih.gov/32048466/)).

### Finding 2 — Mechanism: MSH4 loss disrupts the MutSγ (MSH4–MSH5) complex, abolishing meiotic crossovers [V/H]

MSH4 heterodimerizes with MSH5 to form **MutSγ**, which binds and stabilizes Holliday-junction (HJ) recombination intermediates with the highest affinity among tested substrates (nanomolar K_d) [PMID: 30467025](https://pubmed.ncbi.nlm.nih.gov/30467025/). MutSγ licenses the **MLH1–MLH3 (MutLγ) endonuclease**, acting with EXO1 and RFC-PCNA, to resolve double Holliday junctions into crossovers [PMID: 40319035](https://pubmed.ncbi.nlm.nih.gov/40319035/), [PMID: 32814904](https://pubmed.ncbi.nlm.nih.gov/32814904/). Pathogenic MSH4 variants are typically loss-of-function or disrupt the conserved C-terminal ATPase/Walker-B domain.

> *"MSH4 and MSH5 encode components of the MutSγ complex, which stabilises Holliday junctions during meiotic recombination."* — [PMID: 42386447](https://pubmed.ncbi.nlm.nih.gov/42386447/)

> *"Pathogenic variants are typically loss-of-function and/or disrupt conserved functional domains essential for meiotic recombination, in particular the C-terminal ATPase domain found in both MSH4 and MSH5."* — [PMID: 42386447](https://pubmed.ncbi.nlm.nih.gov/42386447/)

> *"The endonuclease activity of MLH1-MLH3 (MutLγ) is stimulated by MSH4-MSH5 (MutSγ), EXO1, and RFC-PCNA to resolve meiotic recombination intermediates such as double Holliday junctions (HJs) into crossovers."* — [PMID: 40319035](https://pubmed.ncbi.nlm.nih.gov/40319035/)

Loss of crossovers causes failure of homolog pairing/synapsis, meiotic arrest, apoptotic loss of oocytes, and streak/dysgenetic ovaries.

### Finding 3 — *Msh4*-null mice recapitulate POF20; the mechanism is sex-shared (POI in females, azoospermia in males) [M/H]

*Msh4*-knockout mice are sterile in both sexes due to meiotic failure, with defective chromosome pairing/synapsis in prophase I. MSH4 acts in the same genetic pathway as MSH5.

> *"Disruption of the Msh4 gene in mice results in male and female sterility due to meiotic failure."* — [PMID: 10809667](https://pubmed.ncbi.nlm.nih.gov/10809667/)

> *"MSH4 localization on chromosomes during the early stages of meiosis is essential for normal chromosome synapsis in prophase I and that it acts in the same pathway as MSH5."* — [PMID: 10809667](https://pubmed.ncbi.nlm.nih.gov/10809667/)

In humans, the identical biallelic MSH4 defect produces POI in women and **non-obstructive azoospermia (NOA)** in their brothers within the same family, reflecting the shared meiosis-I requirement.

> *"inherited defects in meiosis I may result in common causes for both POI and NOA."* — [PMID: 38175272](https://pubmed.ncbi.nlm.nih.gov/38175272/)

### Finding 4 — MSH4 is loss-of-function-tolerant in heterozygotes, consistent with the recessive mechanism [C]

gnomAD v2 constraint metrics for MSH4 (ENSG00000057468) show it is **not depleted for predicted loss-of-function variants**: pLI ≈ 0 (7.8 × 10⁻³⁴), observed/expected LoF (oe_lof) = 0.93 (90% CI 0.80–1.10; LOEUF ≈ 1.10), obs_lof = 106 vs exp_lof = 113.7, lof_z = 0.61. Heterozygous LoF is therefore well tolerated — exactly what is expected for a gene that causes disease only when **biallelically** inactivated.

ClinVar lists 207 MSH4 records, of which 45 are classified pathogenic and 14 likely pathogenic. Reported pathogenic variant classes include canonical splice-site (exon-17 skipping; p.Ile743_Lys785del), nonsense (c.118C>T, p.Gln40*), frameshift, and missense affecting the conserved C-terminal ATPase/Walker-B domain.

> *"the mutation p.Ile743_Lys785del is predicted to lead to the ablation of the highly conserved Walker B motif of the ATP-binding domain, thus inactivating MSH4."* — [PMID: 28541421](https://pubmed.ncbi.nlm.nih.gov/28541421/)

### Finding 5 — Clinical phenotype: young-adult-onset secondary amenorrhea, infertility, hypergonadotropic hypogonadism [H]

Official HPO/OMIM annotations for OMIM:619938 (all from the index family, frequency 2/2 = 100%) are: **Young adult onset (HP:0011462); Secondary amenorrhea (HP:0000869); Female infertility (HP:0008222); Elevated circulating FSH (HP:0008232); Elevated circulating LH (HP:0011969); Autosomal recessive inheritance (HP:0000007).**

> *"characterized by an early cessation of menses and high FSH levels."* — [PMID: 28541421](https://pubmed.ncbi.nlm.nih.gov/28541421/)

Broader literature indicates affected women predominantly present with secondary amenorrhea (often after initially normal menarche/puberty), with a phenotypic spectrum extending to primary amenorrhea at the severe end and milder **diminished ovarian reserve (DOR)** at the mild end.

> *"Affected individuals predominantly present with secondary amenorrhoea, with emerging evidence for milder phenotypes, including diminished ovarian reserve (DOR)."* — [PMID: 42386447](https://pubmed.ncbi.nlm.nih.gov/42386447/)

### Finding 6 — MSH4 is deeply conserved; functional models span yeast, worm, zebrafish, and mouse [M/C]

MSH4 orthologs exist across eukaryotes: mouse *Msh4* (Gene 55993), rat (295541), zebrafish *msh4* (559917), chicken (424725), dog (612681), cow (616664), chimpanzee (469357), macaque (705294), *S. cerevisiae* MSH4 (850545), *C. elegans* him-14/msh-4 (174157), and *Arabidopsis thaliana* MSH4 (827450). The mouse knockout validates the model.

> *"Disruption of the Msh4 gene in mice results in male and female sterility due to meiotic failure."* — [PMID: 10809667](https://pubmed.ncbi.nlm.nih.gov/10809667/)

### Finding 7 — Prognosis and management: non-progressive lifelong infertility with estrogen-deprivation sequelae; HRT + donor-oocyte IVF [H]

POF20 is not life-threatening but causes irreversible hypergonadotropic hypogonadism. Untreated premature estrogen deficiency increases risks of osteoporosis/fracture, cardiovascular disease, adverse cognitive and sexual-health outcomes, and all-cause mortality.

> *"Premature ovarian insufficiency can result in long-term decrements to all-cause mortality, bone density, cardiovascular health, sexual health, cognitive health, and body mass. Hormone replacement therapy has been demonstrated to reverse these long-term sequalae."* — [PMID: 39448037](https://pubmed.ncbi.nlm.nih.gov/39448037/)

Management follows the 2024 ESHRE/ASRM/IMS evidence-based POI guideline.

> *"The current guideline provides 145 recommendations on symptoms, diagnosis, causation, sequelae and treatment of POI."* — [PMID: 39652037](https://pubmed.ncbi.nlm.nih.gov/39652037/)

### Finding 8 — Investigation complete: comprehensive 15-section characterization with corrected causal gene [C]

The verified identifier set and ontology annotations (below) anchor a complete 15-section characterization. MSH4 aliases **POF20** and **SPGF2** (the male spermatogenic-failure counterpart) were confirmed via mygene.info, and the Monarch Causal-Gene-to-Disease association (MSH4 → POF20, autosomal recessive) was verified.

---

## Mechanistic Model / Interpretation

### Causal chain — from mutation to clinical manifestation

```
1. Biallelic LoF variant in MSH4 (splice / nonsense / frameshift / ATPase-domain missense)
        │  results in
        ▼
2. Absent or non-functional MSH4 protein  →  cannot heterodimerize with MSH5
        │  leads to
        ▼
3. Loss of the MutSγ (MSH4–MSH5) complex  →  Holliday junctions not stabilized   [inferred: biochemistry]
        │  results in
        ▼
4. MLH1–MLH3 (MutLγ) resolvase not licensed  →  double Holliday junctions not resolved   [inferred: biochemistry]
        │  leads to
        ▼
5. Meiotic crossovers fail to form  →  homologous chromosomes do not pair/synapse   [demonstrated: mouse]
        │  results in
        ▼
6. Meiosis-I arrest  →  apoptotic elimination of germ cells / oocytes   [inferred from model/comparative]
        │  leads to
        ▼
7. Depletion of the ovarian follicle pool  →  streak/dysgenetic ovaries
        │  results in
        ▼
8. Hypergonadotropic hypogonadism (loss of estradiol/inhibin feedback → ↑FSH, ↑LH)
        │  manifests as
        ▼
9. CLINICAL: young-adult secondary amenorrhea + female infertility (POF20)

   ── BRANCH (same genotype, male relatives) ──
7b. Spermatogenic meiotic arrest → non-obstructive azoospermia (SPGF2)
```

Steps 3–4 are **inferred from biochemical and model-organism data** (yeast MutSγ binding assays, mouse knockout synapsis defects) rather than demonstrated directly in human ovary. Steps 1, 2, 8, and 9 are established in human patients.

### Upstream vs downstream

| Position | Event | Evidence type |
|----------|-------|---------------|
| **Upstream (initiating)** | Biallelic MSH4 LoF | Human genetics (PMID 28541421) |
| Upstream | MutSγ complex loss | Biochemistry (PMID 30467025) |
| Midstream | Crossover failure, synapsis failure | Mouse model (PMID 10809667) |
| Downstream | Oocyte apoptosis, follicle depletion | Inferred / comparative |
| **Downstream (clinical)** | Hypergonadotropic hypogonadism, amenorrhea, infertility | Human clinical (PMID 28541421) |

### Ontology annotation set

| Category | Terms |
|----------|-------|
| **Disease** | MONDO:0030975; OMIM:619938; UMLS:C5677011; MedGen:1808256; GARD:0025670 |
| **Gene/Protein** | HGNC:7327 (MSH4); NCBI 4438; Ensembl ENSG00000057468; UniProt O15457 |
| **Phenotype (HPO)** | HP:0000869 (secondary amenorrhea); HP:0008222 (female infertility); HP:0008232 (elevated FSH); HP:0011969 (elevated LH); HP:0011462 (young adult onset); HP:0000815 (hypergonadotropic hypogonadism); HP:0008209 (premature ovarian insufficiency); HP:0000786 (amenorrhea); HP:0000007 (AR inheritance) |
| **Biological process (GO)** | GO:0007131 (reciprocal meiotic recombination); GO:0007127 (meiosis I); GO:0006298 (mismatch repair) |
| **Cellular component (GO)** | GO:0000795 (synaptonemal complex); GO:0005713 (recombination nodule); GO:0005634 (nucleus); GO:0000794 (condensed nuclear chromosome) |
| **Molecular function (GO)** | GO:0005524 (ATP binding); GO:0030983 (mismatched DNA binding); GO:0140664 (ATP-dependent DNA damage sensor activity); GO:0003690 (dsDNA binding) |
| **Anatomy (UBERON)** | UBERON:0000992 (ovary) |
| **Cell type (CL)** | CL:0000023 (oocyte); CL:0000020 (spermatogonium) / CL:0000019 (sperm) in males |
| **Treatment (NCIT)** | NCIT:C62002 (HRT); NCIT:C617 (estrogen); NCIT:C713 (progestin); NCIT:C15354 (IVF); NCIT:C92755 (oocyte donation) |

---

## Section-by-Section Report

### 1. Disease Information

POF20 is a rare monogenic form of **primary/premature ovarian insufficiency (POI)** — loss of normal ovarian function before age 40 — defined by its causal gene *MSH4*. Key identifiers: **OMIM 619938, MONDO:0030975, UMLS C5677011, MedGen 1808256, GARD 0025670.** There is no POF20-specific ICD code; it is captured under POI/premature menopause codes (ICD-10 **E28.31**, premature ovarian failure; ICD-11 **5A80.1**) and MeSH *Primary Ovarian Insufficiency* (D016649). **Synonyms/alternative names:** Premature Ovarian Failure 20; MSH4-related POI; ovarian insufficiency due to MSH4 deficiency. The male allelic counterpart is **Spermatogenic Failure 2 (SPGF2)**. Information is derived from **aggregated disease-level resources** (OMIM, Monarch, ClinVar) and a small number of **individual-patient reports/case series** rather than EHR-scale datasets.

### 2. Etiology

**Causal factor:** entirely **genetic** — biallelic (homozygous or compound heterozygous) loss-of-function variants in *MSH4*. **Genetic risk factors:** the only established risk factor is carriage of two pathogenic MSH4 alleles; **consanguinity** substantially raises risk (the index family was consanguineous Colombian; [PMID: 28541421](https://pubmed.ncbi.nlm.nih.gov/28541421/)). Digenic/oligogenic contributions have been reported, including digenic MSH4+MSH5 variants [PMID: 36793102](https://pubmed.ncbi.nlm.nih.gov/36793102/). **Environmental risk factors:** none specific to POF20 — this is a Mendelian disease; general POI environmental contributors (chemotherapy, radiation, smoking) are not causal here. **Protective factors:** none genetic identified; general estrogen-protective lifestyle factors do not modify the underlying meiotic defect. **Gene–environment interactions:** not established; the phenotype is driven by the germline genotype.

### 3. Phenotypes

| Phenotype | HPO term | Type | Onset | Frequency |
|-----------|----------|------|-------|-----------|
| Secondary amenorrhea | HP:0000869 | Clinical sign | Young adult | 2/2 (100%) index family |
| Female infertility | HP:0008222 | Clinical | Young adult | High |
| Elevated circulating FSH | HP:0008232 | Lab abnormality | Young adult | 2/2 (100%) |
| Elevated circulating LH | HP:0011969 | Lab abnormality | Young adult | 2/2 (100%) |
| Hypergonadotropic hypogonadism | HP:0000815 | Lab/clinical | Young adult | High |
| Premature ovarian insufficiency | HP:0008209 | Clinical | <40 y | Defining |
| Young adult onset | HP:0011462 | Modifier | 16–40 y | Typical |

Severity is **variable** (primary amenorrhea → secondary amenorrhea → DOR); the course is **stable/non-progressive** once ovarian reserve is lost. **Quality-of-life impact:** substantial — infertility, estrogen-deficiency symptoms (vasomotor, genitourinary, mood), and long-term bone/cardiovascular/cognitive risks; POI broadly impairs QoL and psychological well-being ([PMID: 40377060](https://pubmed.ncbi.nlm.nih.gov/40377060/)).

### 4. Genetic / Molecular Information

**Causal gene:** *MSH4* (OMIM *602105; HGNC:7327; locus 1p31.1; chr1:75,796,882–75,913,242, GRCh38; NCBI Gene 4438; UniProt O15457). **Variant spectrum:** canonical splice-site (exon-17 skipping, p.Ile743_Lys785del — [PMID: 28541421](https://pubmed.ncbi.nlm.nih.gov/28541421/)); nonsense (c.118C>T, p.Gln40* — [PMID: 38175272](https://pubmed.ncbi.nlm.nih.gov/38175272/)); frameshift; and missense in the conserved C-terminal ATPase/Walker-B domain ([PMID: 42386447](https://pubmed.ncbi.nlm.nih.gov/42386447/)). **Classification:** ClinVar — 45 pathogenic, 14 likely pathogenic of 207 records. **Allele frequency:** pathogenic alleles are rare/absent in gnomAD; MSH4 is LoF-tolerant in heterozygotes (pLI≈0, LOEUF≈1.10). **Origin:** germline. **Functional consequence:** loss of function (recessive). **Modifier genes:** MSH5 (digenic reports); co-occurring meiotic-gene variants may modulate severity. **Epigenetic/chromosomal abnormalities:** none specific to POF20 (though POI generally has epigenetic contributors — [PMID: 40620015](https://pubmed.ncbi.nlm.nih.gov/40620015/)).

### 5. Environmental Information

**Not applicable as a cause** — POF20 is monogenic. No toxins, lifestyle factors, or infectious agents are implicated in its etiology. (Environmental/iatrogenic exposures cause *other* POI subtypes but not MSH4-related disease.)

### 6. Mechanism / Pathophysiology

See the **Mechanistic Model** section above for the ordered causal chain. In brief: MSH4 LoF → loss of MutSγ (MSH4–MSH5) → failure to stabilize Holliday junctions → failure to license MutLγ (MLH1–MLH3)/EXO1/RFC-PCNA → no crossovers → synapsis/pairing failure → meiosis-I arrest → oocyte apoptosis → follicle depletion → hypergonadotropic hypogonadism → amenorrhea/infertility. Key pathway: **meiotic homologous recombination** (not Wnt/MAPK/mTOR). Cellular process: **apoptosis of germ cells** following meiotic arrest. Protein dysfunction: **loss of ATPase-dependent HJ-binding function**. Cell types: oocytes (CL:0000023); subcellular site: synaptonemal complex (GO:0000795). Male branch → spermatocyte arrest → azoospermia.

### 7. Anatomical Structures Affected

**Primary organ:** ovary (UBERON:0000992), typically streak/dysgenetic. **Body system:** endocrine/reproductive (hypothalamic-pituitary-ovarian axis). **Secondary involvement (from estrogen deficiency):** skeleton (osteoporosis), cardiovascular system, CNS (cognition/mood), genitourinary tissues. **Tissue/cell:** germ cells — oocytes (CL:0000023); in males, spermatocytes/spermatogonia. **Subcellular:** nucleus (GO:0005634), synaptonemal complex (GO:0000795), condensed nuclear chromosome (GO:0000794). **Lateralization:** bilateral ovarian involvement.

### 8. Temporal Development

**Onset:** young adult (HP:0011462), typically after apparently normal puberty/menarche; **insidious/chronic** onset of oligo-/amenorrhea. **Progression:** the primary defect is developmental (meiotic failure in fetal/early life depletes the oocyte pool); it presents clinically as **non-progressive, stable** ovarian insufficiency once reserve is exhausted. **Disease course:** chronic, lifelong. **Remission:** none spontaneous; sporadic ovulation is rare. **Critical period:** the meiotic window is prenatal/perinatal — by the time of diagnosis the germ-cell pool is already depleted, limiting fertility-preservation opportunities to early-diagnosed cases.

### 9. Inheritance and Population

**Inheritance:** autosomal recessive (HP:0000007). **Penetrance:** appears high in biallelic carriers but formally incompletely characterized (small case numbers). **Expressivity:** variable (primary amenorrhea ↔ DOR). **Epidemiology:** POI overall affects ~**3.5%** of women ([PMID: 39652037](https://pubmed.ncbi.nlm.nih.gov/39652037/)); MSH4/POF20 is a rare monogenic subset — in targeted-panel/exome POI cohorts, MSH4 accounts for a small percentage of solved cases ([PMID: 36793102](https://pubmed.ncbi.nlm.nih.gov/36793102/), [PMID: 36373164](https://pubmed.ncbi.nlm.nih.gov/36373164/), [PMID: 36099812](https://pubmed.ncbi.nlm.nih.gov/36099812/)). **Consanguinity/founder effects:** homozygous cases enriched in consanguineous families. **Carrier frequency:** low; MSH4 LoF alleles are tolerated in heterozygotes (gnomAD). **Sex:** females present with POI, males with NOA — same genotype, sex-specific manifestation.

### 10. Diagnostics

**Clinical/lab:** elevated FSH (ESHRE 2024: a single FSH >25 IU/L suffices for POI diagnosis), elevated LH, low estradiol, low AMH; pelvic ultrasound shows small ovaries/reduced antral follicle count. **Genetic testing:** POI gene panels or whole-exome sequencing identify biallelic MSH4 variants — the definitive diagnostic for POF20. WES/panel testing is high-yield in familial/consanguineous POI ([PMID: 36099812](https://pubmed.ncbi.nlm.nih.gov/36099812/)). Karyotype and FMR1 premutation testing are performed to exclude common POI causes. **Differential diagnosis:** Turner syndrome, FMR1 premutation, autoimmune oophoritis, other monogenic POI (FOXL2, NOBOX, MCM8/9, MSH5, HFM1, SYCE1, STAG3). **Screening:** cascade genetic testing of at-risk relatives (including male siblings for azoospermia risk).

### 11. Outcome / Prognosis

**Survival:** not directly life-threatening; however untreated POI is associated with **increased all-cause mortality** and cardiovascular/skeletal morbidity ([PMID: 39448037](https://pubmed.ncbi.nlm.nih.gov/39448037/), [PMID: 20938225](https://pubmed.ncbi.nlm.nih.gov/20938225/)). **Morbidity:** infertility, osteoporosis/fracture risk, cardiovascular disease, cognitive and sexual-health effects, vasomotor symptoms. **Recovery:** ovarian function is irreversibly lost; HRT reverses many estrogen-deprivation sequelae but not fertility. **Prognostic factors:** younger age at ART and milder (DOR) phenotype associate with better reproductive prognosis ([PMID: 40936058](https://pubmed.ncbi.nlm.nih.gov/40936058/)).

### 12. Treatment

**No disease-modifying/curative therapy exists.** Management is supportive and hormonal:

| Intervention | NCIT | Purpose |
|--------------|------|---------|
| Hormone replacement therapy (estradiol + progestogen) | NCIT:C62002 | Symptom control; bone/CV/cognitive protection until ~age 51 |
| Estrogen | NCIT:C617 | Core HRT component |
| Progestin | NCIT:C713 | Endometrial protection |
| In vitro fertilization | NCIT:C15354 | Fertility (with donor oocytes) |
| Oocyte donation | NCIT:C92755 | Principal fertility option |

Adjuncts: calcium/vitamin D, DXA bone-density monitoring, psychological support (2024 ESHRE/ASRM/IMS guideline, 145 recommendations — [PMID: 39652037](https://pubmed.ncbi.nlm.nih.gov/39652037/)). Own-oocyte IVF is generally non-viable because meiosis is abolished; **donor-oocyte/donor-embryo IVF** is the mainstay. No gene therapy or pharmacogenomic strategy is currently applicable.

### 13. Prevention

Primary prevention is not possible (germline Mendelian disease). **Secondary/tertiary prevention:** early diagnosis enables timely HRT to prevent osteoporosis and cardiovascular complications, and (if diagnosed before pool exhaustion) consideration of fertility preservation. **Genetic counseling** is central: autosomal-recessive recurrence risk (25% for future siblings of a proband), carrier testing of partners in consanguineous unions, and counseling of male relatives regarding azoospermia risk. **Preimplantation/prenatal genetic testing** is feasible for families with a known biallelic genotype.

### 14. Other Species / Natural Disease

MSH4 is **deeply conserved**. Orthologs: mouse *Msh4* (Gene 55993; taxid 10090), rat (295541), zebrafish *msh4* (559917), chicken (424725), dog (612681), cow (616664), chimpanzee (469357), macaque (705294), *S. cerevisiae* MSH4 (850545; taxid 4932), *C. elegans* him-14/msh-4 (174157; taxid 6239), *Arabidopsis thaliana* MSH4 (827450). The meiotic recombination function is conserved from yeast to mammals. No specific naturally occurring companion-animal disease is catalogued for MSH4, but the shared mechanism makes cross-species meiotic sterility phenotypes directly comparable.

### 15. Model Organisms

| Model | Type | Phenotype recapitulation |
|-------|------|--------------------------|
| **Mouse *Msh4*-null** | Mammalian knockout | Male + female sterility; prophase-I synapsis failure — faithfully recapitulates POF20/SPGF2 ([PMID: 10809667](https://pubmed.ncbi.nlm.nih.gov/10809667/)) |
| ***S. cerevisiae* MSH4** | Yeast | Crossover/recombination defects; biochemistry of MutSγ–HJ binding ([PMID: 30467025](https://pubmed.ncbi.nlm.nih.gov/30467025/)) |
| ***C. elegans* him-14/msh-4** | Invertebrate | Meiotic crossover failure, chromosome missegregation |
| **Zebrafish *msh4*** | Vertebrate | Meiotic model (ortholog available) |

**Model strengths:** the mouse knockout captures the core sterility/meiotic-failure phenotype and the sex-shared mechanism. **Limitations:** rodent ovarian-aging/reserve dynamics differ from humans, and human milder (DOR) phenotypes are harder to model. Resources: MGI, ZFIN, SGD, WormBase.

---

## Evidence Base

| PMID | Title / focus | Role in this report | Evidence type |
|------|---------------|---------------------|---------------|
| [28541421](https://pubmed.ncbi.nlm.nih.gov/28541421/) | *Homozygous donor splice-site mutation in MSH4 causes POI* | **Foundational** — first MSH4–POI link; variant, phenotype, Walker-B ablation | Human clinical/genetic |
| [42386447](https://pubmed.ncbi.nlm.nih.gov/42386447/) | *MSH4 and MSH5 variants in POI: review and case study* | Variant spectrum (LoF/ATPase); phenotype spectrum (2° amenorrhea → DOR) | Review + case |
| [38175272](https://pubmed.ncbi.nlm.nih.gov/38175272/) | *Homozygous nonsense MSH4 variant → POI and NOA* | Sex-shared meiosis-I mechanism; nonsense variant | Human clinical/genetic |
| [10809667](https://pubmed.ncbi.nlm.nih.gov/10809667/) | *Msh4 knockout mouse* | Model organism; synapsis role; same pathway as MSH5 | Mouse model |
| [30467025](https://pubmed.ncbi.nlm.nih.gov/30467025/) | *MutSγ–DNA conformational changes* | MutSγ binds HJs with nanomolar affinity | In vitro biochemistry |
| [40319035](https://pubmed.ncbi.nlm.nih.gov/40319035/) | *EXO1 promotes MLH1-MLH3 endonuclease* | MutSγ licenses MutLγ to resolve dHJs into crossovers | In vitro/biochemistry |
| [32814904](https://pubmed.ncbi.nlm.nih.gov/32814904/) | *Regulation of MLH1-MLH3 endonuclease in meiosis* | Downstream crossover resolution | Review/biochemistry |
| [36099812](https://pubmed.ncbi.nlm.nih.gov/36099812/) | *Genetic landscape of large POI cohort* | Confirms MSH4 causal role; diagnostic yield | Human cohort |
| [36793102](https://pubmed.ncbi.nlm.nih.gov/36793102/) | *NGS of 500 POI patients* | Digenic MSH4+MSH5; compound-het confirmation | Human cohort |
| [36373164](https://pubmed.ncbi.nlm.nih.gov/36373164/) | *Genetic screening in ovarian dysfunction* | MSH4 splice variants; expands spectrum | Human cohort |
| [40936058](https://pubmed.ncbi.nlm.nih.gov/40936058/) | *Genetic variants in DOR/POI & ART outcomes* | Meiotic variants → poor ART; younger age better | Human cohort |
| [39652037](https://pubmed.ncbi.nlm.nih.gov/39652037/) | *2024 ESHRE/ASRM/IMS POI guideline* | Diagnosis (FSH>25) and management framework | Guideline |
| [39448037](https://pubmed.ncbi.nlm.nih.gov/39448037/) | *HRT in radiation-induced POI* | Estrogen-deprivation sequelae; HRT reverses them | Review/clinical |
| [20938225](https://pubmed.ncbi.nlm.nih.gov/20938225/) | *Skeletal effect of natural early menopause* | Bone/mortality risks of early estrogen loss | Review |
| [25873734](https://pubmed.ncbi.nlm.nih.gov/25873734/) | *MCM8 mutations → gonadal failure* | Distinguishes POF10 (MCM8) from POF20 (MSH4) | Human genetic |

**Consistency:** All independent lines of evidence — human genetics (multiple families/cohorts), the mouse knockout, and yeast/worm biochemistry — converge on a single coherent model: MSH4 LoF → MutSγ failure → crossover loss → meiotic arrest → ovarian insufficiency. No contradictory findings were identified.

---

## Limitations and Knowledge Gaps

1. **Small patient numbers.** Core phenotype frequencies (e.g., 100% secondary amenorrhea/elevated FSH) derive from the 2-sibling index family; broader cohorts are needed to establish robust penetrance and expressivity estimates.
2. **No direct human ovarian histology/omics.** The oocyte-apoptosis and follicle-depletion steps are inferred from mouse and comparative data, not demonstrated in human MSH4-deficient ovary. No POF20-specific transcriptomic, proteomic, metabolomic, or single-cell datasets exist.
3. **Penetrance/expressivity.** The genotype–phenotype relationship (why some carriers show primary amenorrhea vs milder DOR) and the role of modifier/digenic alleles (MSH5) are incompletely resolved.
4. **Epidemiology.** No POF20-specific prevalence/incidence figures exist; only the broad POI prevalence (~3.5%) and small panel-based contributions are available.
5. **No disease-modifying therapy or trials.** All treatment evidence is generic POI management; no MSH4-targeted therapeutics or NCT-registered trials specific to POF20.
6. **Epigenetic/environmental modifiers** of the meiotic phenotype are unstudied in this subtype.

---

## Proposed Follow-up Experiments / Actions

1. **Aggregate an international MSH4-POI cohort** (GeneMatcher, large POI consortia) to quantify penetrance, expressivity, genotype–phenotype correlations, and sex-specific outcomes (POI vs NOA).
2. **Functional validation of VUS**: minigene splicing assays and MutSγ complex-formation / HJ-binding assays to reclassify uncertain MSH4 missense variants per ACMG/AMP.
3. **Patient-derived iPSC → germ-cell / ovarian organoid models** to directly observe meiotic arrest and oocyte apoptosis in the human MSH4-deficient context, filling the inferred mechanistic gap.
4. **Single-cell transcriptomics of residual ovarian tissue / model germ cells** to define the apoptotic and granulosa-cell responses downstream of meiotic failure.
5. **Early-diagnosis fertility-preservation protocols**: identify biallelic carriers before pool exhaustion to evaluate oocyte/ovarian-tissue cryopreservation windows.
6. **Structured genetic counseling pathway** including cascade testing of male siblings (azoospermia risk) and partner carrier screening in consanguineous families.
7. **Longitudinal HRT outcome study in genetically defined POF20** to confirm that estrogen-deprivation sequelae are mitigated as in general POI.

---

*Report compiled from a 5-iteration autonomous investigation: 8 confirmed findings, 34 papers reviewed. The causal gene was corrected from MCM8 to MSH4 during the investigation. Evidence integrates human clinical/genetic reports, mouse knockout models, yeast/invertebrate biochemistry, and the 2024 ESHRE/ASRM/IMS POI guideline.*


## Artifacts

- [OpenScientist final report](Premature_Ovarian_Failure_20-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Premature_Ovarian_Failure_20-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 13 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030975` (6 mentions) - the report calls it "if available"; MONDO calls it **premature ovarian failure 20**
- `NCIT:C62002` (2 mentions) - the report calls it "Hormone replacement therapy (estradiol + progestogen)"; NCIT calls it **Amiodarone**
- `NCIT:C713` (2 mentions) - the report calls it "Progestin"; NCIT calls it **Oligonucleotide**
- `NCIT:C92755` (2 mentions) - the report calls it "Oocyte donation"; NCIT calls it **Chorionic Villus Sampling**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0008232` (3 mentions) - the report calls it "Elevated circulating FSH"; HP calls it **Elevated circulating follicle stimulating hormone level**, and lists "Elevated follicle stimulating hormone" among its other names
- `HP:0011969` (3 mentions) - the report calls it "Elevated circulating LH"; HP calls it **Elevated circulating luteinizing hormone level**
- `NCIT:C617` (2 mentions) - the report calls it "Estrogen"; NCIT calls it **Lomustine**, and lists "Belustin" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `UMLS`, `GARD`.
