---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-10T20:12:22.871130'
end_time: '2026-08-10T20:26:47.528538'
duration_seconds: 864.66
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Progressive Myoclonic Epilepsy Type 7
  mondo_id: ''
  category: Genetic
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Progressive_Myoclonic_Epilepsy_Type_7-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Progressive_Myoclonic_Epilepsy_Type_7-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Progressive Myoclonic Epilepsy Type 7
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Progressive Myoclonic Epilepsy Type 7** covering all of the
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

# Progressive Myoclonic Epilepsy Type 7 (EPM7 / MEAK): Comprehensive Disease Characteristics Report

**Disease:** Progressive Myoclonic Epilepsy Type 7 (EPM7)
**Clinical eponym/synonym:** Myoclonus Epilepsy and Ataxia due to potassium channel mutation (**MEAK**)
**Key identifiers:** OMIM #616187 · MONDO:0014734 · ORPHA:280620 · Gene: *KCNC1* (Kv3.1)
**Category:** Genetic (autosomal dominant, de novo)

---

## Summary

Progressive Myoclonic Epilepsy Type 7 (EPM7), better known by its clinical descriptor **Myoclonus Epilepsy and Ataxia due to potassium channel mutation (MEAK)**, is a rare, progressive neurodegenerative epilepsy caused almost exclusively by a single **recurrent de novo heterozygous variant in the *KCNC1* gene, c.959G>A (p.Arg320His)**. *KCNC1* encodes **Kv3.1**, a voltage-gated potassium channel subunit that endows fast-spiking neurons with the rapid membrane repolarization needed to sustain high-frequency firing. The R320H substitution sits in the S4 voltage-sensor and acts through a **dominant-negative loss-of-function** mechanism, poisoning heterotetrameric channels and reducing Kv3.1 current well below the 50% expected from simple haploinsufficiency. In the landmark exome study of 84 unrelated patients with previously unexplained progressive myoclonus epilepsy (PME), this one variant explained **13% of cases**, establishing *KCNC1* as a major cause of the disorder ([PMID: 25401298](https://pubmed.ncbi.nlm.nih.gov/25401298/)).

Clinically, MEAK begins in childhood or early adolescence (symptom onset 3–15 years, **median 9.5 years**) with progressively disabling cortical **action myoclonus**, relatively infrequent tonic-clonic seizures, early and prominent **cerebellar ataxia**, and **symmetrical, progressive cerebellar atrophy** on MRI. Roughly half of patients become wheelchair-bound by late adolescence, and mild cognitive decline occurs in about half; unlike some other PMEs, early death is not characteristic. A striking and diagnostically useful feature is **transient clinical improvement with fever**, which has a mechanistic explanation: elevated temperature produces a leftward (hyperpolarizing) shift in Kv3.1 activation that partially rescues channel availability ([PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/)).

The pathophysiology is a channelopathy of **fast-spiking neurons**. Loss of Kv3.1 function impairs high-frequency firing of cortical fast-spiking GABAergic interneurons (producing cortical disinhibition → myoclonus and generalized seizures) and of cerebellar neurons (producing ataxia and tremor), and can induce neuronal cell death; the R320H allele additionally causes a developmental **dendritopathy**, indicating a role beyond firing regulation. Treatment is entirely **symptomatic** — valproate, levetiracetam, clonazepam, perampanel — with strict avoidance of myoclonus-aggravating sodium-channel blockers and related drugs; **no disease-modifying therapy exists**, though Kv3 positive modulators are a rational emerging strategy motivated by cryo-EM structures of the human Kv3.1 gating machinery.

---

## Section 1 — Disease Information

**Overview.** EPM7/MEAK is a monogenic progressive myoclonus epilepsy: a syndrome combining action myoclonus, epileptic seizures, and progressive neurological decline (here dominated by cerebellar ataxia). It is caused by dysfunction of the Kv3.1 voltage-gated potassium channel. It is characterized as *"a highly penetrant and specific form of progressive myoclonus epilepsy with severe ataxia, designated myoclonus epilepsy and ataxia due to potassium channel mutation (MEAK)"* ([PMID: 33735526](https://pubmed.ncbi.nlm.nih.gov/33735526/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #616187 (Epilepsy, progressive myoclonic, 7) |
| MONDO | MONDO:0014734 |
| Orphanet | ORPHA:280620 |
| Gene (HGNC) | *KCNC1* (Kv3.1) |
| Protein (UniProt) | P48547 (KCNC1_HUMAN) |
| Locus | Chromosome 11p15 |

**Synonyms / alternative names.** EPM7; Myoclonus Epilepsy and Ataxia due to potassium channel mutation (MEAK); KCNC1-related progressive myoclonus epilepsy; *KCNC1*-related disorder (MEAK subtype).

**Source of information.** The knowledge base is derived from **aggregated disease-level resources** and **published patient cohorts** (exome-sequencing discovery cohorts and case series), not individual EHR data. Primary evidence sources are human clinical cohorts, in vitro electrophysiology (heterologous expression / patch-clamp), and, more recently, mouse models and cryo-EM structural biology.

---

## Section 2 — Etiology

**Primary cause (genetic).** EPM7/MEAK is caused by a **recurrent de novo heterozygous mutation, c.959G>A (p.Arg320His), in *KCNC1***, which *"was identified as a new major cause for PME"* ([PMID: 25401298](https://pubmed.ncbi.nlm.nih.gov/25401298/)). The variant maps to chromosome 11 and *"encodes for the Kv3.1 protein"* ([PMID: 27629860](https://pubmed.ncbi.nlm.nih.gov/27629860/)). The disorder is essentially always sporadic, arising de novo in the affected individual.

**Genetic risk factors.** The single causal variant (R320H) is the dominant genetic determinant; there are no known susceptibility loci or modifier genes established for MEAK. Because the variant is a recurrent de novo germline change, there is effectively **no population carrier state** and it is absent from population frequency databases (gnomAD).

**Environmental risk factors.** None established. MEAK is a Mendelian channelopathy; environmental exposures are not causal. **Fever/elevated body temperature acts paradoxically as a transient symptom modifier (improvement), not a risk factor** ([PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/)).

**Protective factors.** No genetic protective variants or modifier alleles are described. The best-characterized modifier is a physiological one: **elevated temperature transiently improves symptoms** via a leftward shift in Kv3.1 activation.

**Gene–environment interactions.** The only well-documented gene–environment interaction is **temperature × channel gating**: the R320H dominant-negative deficit is partially offset at higher temperature because wild-type Kv3.1 activation shifts to more hyperpolarized voltages, increasing channel availability ([PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/)).

---

## Section 3 — Phenotypes

Core phenotypes (from the 20-patient R320H cohort, [PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/); mechanism review [PMID: 27629860](https://pubmed.ncbi.nlm.nih.gov/27629860/)):

| Phenotype | Type | Onset | Severity / progression | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Progressive myoclonus (cortical, action myoclonus) | Clinical sign | Childhood/adolescence (3–15 y) | Progressively severe; disabling | Near-universal (defining) | HP:0001336 (Myoclonus); HP:0002123 (Generalized myoclonic seizure) |
| Cerebellar ataxia | Clinical sign | Early in course | Progressive; often leads to loss of ambulation | Highly frequent | HP:0001251 (Ataxia); HP:0002070 (Limb ataxia) |
| Tonic-clonic seizures | Clinical sign | Variable | Relatively infrequent vs myoclonus | Common but rarer than myoclonus | HP:0002069 (Bilateral tonic-clonic seizure) |
| Cerebellar atrophy (MRI) | Physical/imaging manifestation | With disease progression | Symmetrical, progressive | Characteristic imaging hallmark | HP:0001272 (Cerebellar atrophy) |
| Cognitive decline | Behavioral/cognitive | Later | Mild in ~half of patients | ~50% | HP:0001268 (Mental deterioration) |
| Loss of independent ambulation | Functional | Late teens | Severe | ~10/20 wheelchair-bound | HP:0002505 (Loss of ambulation) |
| Photosensitivity (EEG) | Laboratory/electrophysiology | — | — | Frequent | Photoparoxysmal response |
| Transient fever-related improvement | Modifier phenomenon | — | Transient | 6/20 patients | — |

Supporting quotes: *"Symptoms began at between 3 and 15 years of age (median = 9.5), with progressively severe myoclonus and rare tonic-clonic seizures"*; *"Magnetic resonance imaging revealed symmetrical cerebellar atrophy, which appeared progressive"*; *"transient clinical improvement with fever was noted in 6 patients"* ([PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/)).

**Quality-of-life impact.** Progressive action myoclonus and ataxia severely impair mobility, self-care, and independence; approximately half of patients require a wheelchair by late adolescence. Cognitive decline, where present, is generally mild. Early death is not a characteristic feature, so the dominant burden is chronic disability rather than mortality.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *KCNC1* (HGNC:6233; OMIM *176258), encoding the **Kv3.1** voltage-gated potassium channel subunit, which determines high-frequency firing in neurons.

**Pathogenic variant (MEAK-defining).**

| Attribute | Detail |
|---|---|
| cDNA / protein | c.959G>A (p.Arg320His); the recurrent MEAK allele |
| Variant type | Missense |
| Location | S4 voltage-sensor domain |
| Classification | Pathogenic (ACMG) — recurrent de novo, functionally validated |
| Zygosity | Heterozygous |
| Origin | Germline, de novo |
| Population frequency | Absent from population databases (no carrier state) |
| Functional consequence | Dominant-negative loss of function |

*"Functional analysis of the Arg320His mutant channel showed a dominant-negative loss-of-function effect"* ([PMID: 25401298](https://pubmed.ncbi.nlm.nih.gov/25401298/)).

**Broader *KCNC1* allelic series (genotype–phenotype spectrum).** MEAK is one end of a spectrum of *KCNC1*-related neurological disease:

| Variant | Domain | Phenotype | Mechanism |
|---|---|---|---|
| p.Arg320His | S4 | MEAK / PME (EPM7) | Dominant-negative LoF |
| Nonsense / LoF | — | Intellectual disability | Haploinsufficiency |
| p.Cys208Tyr | — | Isolated nonprogressive myoclonus | LoF |
| p.Thr399Met | Pore | ID / epilepsy with nonprogressive ataxia | Complete LoF alone; **dominant-positive/GoF** with WT (∼20 mV hyperpolarizing shift) |
| p.Ala421Val | Pore | Epilepsy (myoclonic/absence/GTC), ataxia, DD | Dominant-negative LoF |
| S6 pore variants | Pore | DD/ID with hypotonia, no epilepsy/ataxia | Gain of Kv3.1 function |

*"either isolated nonprogressive myoclonus (p.Cys208Tyr), intellectual disability (p.Thr399Met), or epilepsy with myoclonic, absence and generalized tonic-clonic seizures, ataxia, and developmental delay (p.Ala421Val, three patients)"* and *"Functional analyses demonstrated no measurable currents for all identified variants and dominant-negative effects for p.Thr399Met and p.Ala421Val predicting neuronal disinhibition as the underlying disease mechanism"* ([PMID: 31353862](https://pubmed.ncbi.nlm.nih.gov/31353862/)). A gain-of-function subgroup with *"a prominent leftward (hyperpolarized) shift in the voltage dependence of activation"* is associated with DD/ID and central hypotonia without epilepsy or ataxia ([PMID: 36419348](https://pubmed.ncbi.nlm.nih.gov/36419348/)). The p.Thr399Met variant illustrates a *"dominant-positive effect"* — complete LoF alone but a ∼20 mV hyperpolarizing shift with slowed deactivation when co-expressed with WT ([PMID: 42347804](https://pubmed.ncbi.nlm.nih.gov/42347804/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** None established for MEAK. The disease is a single-gene channelopathy without a described epigenetic component or large-scale structural/chromosomal etiology.

---

## Section 5 — Environmental Information

**Environmental factors.** None causal. MEAK is a de novo monogenic disorder.

**Lifestyle factors.** No lifestyle behaviors are established as causing or preventing MEAK. As with other myoclonic epilepsies, general seizure-precipitant avoidance (sleep deprivation, photic triggers) is prudent; EEG photosensitivity is present in many patients.

**Infectious agents.** Not applicable — MEAK is genetic, not infectious. Notably, **febrile illness transiently improves symptoms** in a subset of patients (a physiological, not infectious, effect on channel gating) ([PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/)).

---

## Section 6 — Mechanism / Pathophysiology

**Central mechanism.** Kv3.1 is a delayed-rectifier potassium channel with distinctive fast activation/deactivation kinetics tailored for rapid repolarization in **fast-spiking neurons**. The MEAK R320H variant, positioned in the S4 voltage sensor, produces channels that assemble with wild-type subunits but abolish current — a **dominant-negative loss of function** that reduces Kv3.1-mediated repolarization more than haploinsufficiency would.

**Causal chain (upstream → downstream):**

```
KCNC1 c.959G>A (p.Arg320His), de novo, heterozygous   [upstream trigger]
        │
        ▼
Dominant-negative poisoning of Kv3.1 heterotetramers → loss of fast K+ current
        │
        ├──► Fast-spiking GABAergic interneurons fail to sustain high-frequency firing
        │           → cortical DISINHIBITION → cortical (action) myoclonus + generalized seizures
        │
        ├──► Cerebellar neurons impaired → ATAXIA, tremor; progressive cerebellar atrophy
        │
        └──► Developmental DENDRITOPATHY + neuronal cell death   [additional/parallel]
        │
        ▼
Progressive, disabling clinical MEAK phenotype        [downstream manifestation]
```

Supporting statements: *"Loss of Kv3 function disrupts the firing properties of fast-spiking neurons, affects neurotransmitter release and induces cell death"* and *"the most affected neurons include inhibitory GABAergic interneurons and cerebellar neurons. Impairment of the former cells is believed to contribute to myoclonus and seizures, whereas dysfunction of the latter to ataxia and tremor"* ([PMID: 27629860](https://pubmed.ncbi.nlm.nih.gov/27629860/)). The R320H allele additionally *"causes a developmental dendritopathy"*, indicating a role beyond high-frequency firing regulation ([PMID: 33735526](https://pubmed.ncbi.nlm.nih.gov/33735526/)). A 2026 mouse model of the recurrent variant shows **impaired excitability of fast-spiking neurons** ([PMID: 41705663](https://pubmed.ncbi.nlm.nih.gov/41705663/)).

**Structural basis of gating.** Cryo-EM of human Kv3.1a reveals a unique cytoplasmic **T1 tetramerization domain** interacting with the C-terminal axonal-targeting motif and gating machinery; S1/S2-linker–turret interactions strengthen the voltage-sensor–pore interface, and an electrostatic α6(T1)–R449(S6T) contact plus S4/S5-linker residues control the channel's fast gating. *"Malfunction of this process due to genetic variants in the KCNC1 gene causes severe epileptic disorders"* and the structures *"provide insights into gating control and disease mechanisms and may guide strategies for the design of pharmaceutical drugs targeting Kv3 channels"* ([PMID: 35840580](https://pubmed.ncbi.nlm.nih.gov/35840580/)).

**Temperature dependence (fever improvement).** *"At elevated temperatures, there was a robust leftward shift in activation of wild-type K[v3.1]"* — increased channel availability that can partially offset the R320H deficit, explaining transient fever-associated improvement ([PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/)).

**Ontology suggestions.**
- **GO (biological process):** potassium ion transmembrane transport (GO:0071805); regulation of membrane potential (GO:0042391); action potential (GO:0001508); regulation of neuronal action potential (GO:0098908).
- **GO (cellular component):** voltage-gated potassium channel complex (GO:0008076); plasma membrane (GO:0005886); axon (GO:0030424); neuronal dendrite (GO:0030425).
- **CHEBI:** potassium(1+) (CHEBI:29103).
- **CL (cell types):** cerebellar Purkinje cell (CL:0000121); GABAergic interneuron (CL:0000617); fast-spiking basket cell / cortical interneuron.

**Immune, metabolic, and fibrotic mechanisms** are not implicated; MEAK is a primary neuronal channelopathy.

---

## Section 7 — Anatomical Structures Affected

**Organ / body system level.** Primary organ: **brain** (central nervous system). Chiefly affected regions are the **cerebral cortex** (fast-spiking interneurons → myoclonus/seizures) and the **cerebellum** (ataxia and progressive symmetrical atrophy). Body system: **nervous system** (UBERON:0001016). No primary involvement of non-neural organs.

**Tissue / cell level.** Nervous tissue; specifically **fast-spiking GABAergic inhibitory interneurons** of cortex and **cerebellar neurons** (including Purkinje-cell circuitry). *"the most affected neurons include inhibitory GABAergic interneurons and cerebellar neurons"* ([PMID: 27629860](https://pubmed.ncbi.nlm.nih.gov/27629860/)).

**Subcellular level.** The neuronal **plasma membrane** (voltage-gated K+ channel complex), **axon** (Kv3.1 axonal targeting motif), and **dendrites** (developmental dendritopathy, [PMID: 33735526](https://pubmed.ncbi.nlm.nih.gov/33735526/)). GO cellular components: voltage-gated potassium channel complex (GO:0008076); axon (GO:0030424); dendrite (GO:0030425).

**Localization / lateralization.** **Bilateral and symmetrical** — cerebellar atrophy is described as symmetrical and progressive ([PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/)).

**UBERON suggestions:** brain (UBERON:0000955); cerebellum / cerebellar cortex (UBERON:0002037 / UBERON:0002129); cerebral cortex (UBERON:0000956).

---

## Section 8 — Temporal Development

**Onset.** Childhood to early adolescence; symptom onset **3–15 years, median 9.5 years** ([PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/)). Onset is typically insidious, often initially misdiagnosed as idiopathic generalized epilepsy.

**Progression.** **Chronic and progressive.** Myoclonus becomes progressively severe and disabling; ataxia progresses with symmetrical cerebellar atrophy; roughly half of patients lose independent ambulation by late teens. Cognitive decline, when present, is mild. Unlike some PMEs (e.g., Lafora disease), **early death is not characteristic** of MEAK.

**Patterns.** No spontaneous remission. A distinctive feature is **transient, fluctuating improvement during febrile episodes**. The therapeutic critical window and disease-modifying intervention timing remain undefined, though the temperature effect suggests Kv3 augmentation could be beneficial across the disease course.

---

## Section 9 — Inheritance and Population

**Inheritance.** **Autosomal dominant**, arising from a **de novo heterozygous** *KCNC1* variant; *"caused by a recurrent de novo heterozygous mutation (c.959G>A, p.Arg320His) in the KCNC1 gene, which maps to chromosome 11 and encodes for the Kv3.1 protein"* ([PMID: 27629860](https://pubmed.ncbi.nlm.nih.gov/27629860/)). Essentially all cases are sporadic.

**Penetrance / expressivity.** **Highly penetrant** for the R320H allele; the phenotype is relatively **specific and stereotyped** (MEAK) — *"a highly penetrant and specific form of progressive myoclonus epilepsy with severe ataxia"* ([PMID: 33735526](https://pubmed.ncbi.nlm.nih.gov/33735526/)).

**Anticipation / mosaicism / founder effects.** No genetic anticipation (not a repeat-expansion disorder). Recurrence risk to siblings is low but non-zero due to possible parental **gonadal mosaicism**. There is **no founder population** — reported patients span multiple countries and ethnicities.

**Carrier frequency.** Effectively none — the variant is de novo and germline, absent from population frequency databases ([PMID: 25401298](https://pubmed.ncbi.nlm.nih.gov/25401298/); [PMID: 27629860](https://pubmed.ncbi.nlm.nih.gov/27629860/)).

**Epidemiology.** Ultra-rare. No precise prevalence/incidence estimate is established, but the disorder is a **major molecular cause of otherwise-unexplained PME**: R320H accounted for **11/84 (13%)** of exome-discovery cases and **2 additional cases (7%)** in a secondary cohort — *"Eleven unrelated exome-sequenced (13%) and two affected individuals in a secondary cohort (7%) had this mutation"* ([PMID: 25401298](https://pubmed.ncbi.nlm.nih.gov/25401298/)).

**Sex ratio / geographic distribution.** No strong sex predilection reported; no endemic geographic clustering (no founder effect).

---

## Section 10 — Diagnostics

**Diagnostic approach.** Molecular confirmation is definitive. Because the disorder is caused predominantly by a single recurrent variant, **targeted single-gene / gene-panel testing or exome sequencing** for *KCNC1* c.959G>A (p.Arg320His) is the key diagnostic test. Early disease is frequently **misdiagnosed as idiopathic generalized epilepsy** — *"the potential for misdiagnosis as idiopathic generalized epilepsy during the early phase of the disease"* ([PMID: 32972906](https://pubmed.ncbi.nlm.nih.gov/32972906/)).

**Supportive clinical / electrophysiological features.**
- **Giant (high-amplitude) somatosensory evoked potentials (SEPs)** — *"abnormally high amplitude in the sensory evoked potential recording"* ([PMID: 32972906](https://pubmed.ncbi.nlm.nih.gov/32972906/)), reflecting cortical hyperexcitability.
- **Cortical myoclonus** confirmed by polygraphic EEG-EMG (short-duration bursts, agonist–antagonist coactivation).
- **EEG:** generalized spike/polyspike-wave discharges with **photosensitivity**.
- **MRI:** progressive **symmetrical cerebellar atrophy** ([PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/)).

**Differential diagnosis (other PMEs to exclude):** Unverricht-Lundborg disease (EPM1, *CSTB*), Lafora disease (*EPM2A/NHLRC1*), MERRF (mitochondrial *MT-TK*), DRPLA (*ATN1*), sialidosis, and neuronal ceroid lipofuscinoses. Distinguishing features of MEAK: prominent early ataxia with symmetrical cerebellar atrophy, fever-related improvement, absence of dementia/organomegaly, and the specific *KCNC1* genotype.

**Genetic testing utility.** WES/WGS and epilepsy/PME gene panels including *KCNC1* are highly effective; single-variant testing is diagnostic given the recurrent allele. CMA, karyotyping, FISH, mtDNA testing, and repeat-expansion testing are **not applicable** to MEAK (used mainly to exclude mimics). Omics-based diagnostics are not standard.

---

## Section 11 — Outcome / Prognosis

**Survival / mortality.** MEAK is chronically disabling but, unlike Lafora disease or severe EPM1, **early death is not a defining feature**; the 20-case series did not report early death as characteristic ([PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/)). No formal 5-/10-year survival statistics are established.

**Morbidity / function.** The dominant outcome is progressive **motor disability**: severe action myoclonus and ataxia, with ~half of patients wheelchair-bound by late adolescence. Cognitive decline is generally mild. Quality of life is substantially reduced due to impaired mobility and dependence.

**Disease course / complications.** Progressive, lifelong. Complications relate to falls, immobility, and drug-refractory myoclonus. Recovery potential is limited; current therapy controls symptoms partially but does not reverse progression.

**Prognostic factors.** Genotype is the principal determinant — the R320H allele defines the stereotyped MEAK course. Younger onset within the range and rapidly progressive myoclonus/ataxia portend greater disability. No validated molecular prognostic biomarkers exist beyond the causal genotype.

---

## Section 12 — Treatment

**No disease-modifying therapy exists.** Management is **symptomatic anti-myoclonic polytherapy**, frequently requiring 3–4 drugs, plus rehabilitation for ataxia.

**Pharmacotherapy (PME framework, [PMID: 28799509](https://pubmed.ncbi.nlm.nih.gov/28799509/)):**

| Line | Drugs | NCIT suggestion |
|---|---|---|
| Drug of choice | **Valproic acid** (except mitochondrial PME) | NCIT:C935 (Valproic Acid) |
| First add-on | **Levetiracetam**, **Clonazepam** | NCIT:C1698 (Levetiracetam); NCIT:C591 (Clonazepam) |
| Promising alternatives | **Zonisamide**, **Perampanel** | NCIT:C29050 (Zonisamide); NCIT:C74015 (Perampanel) |
| Reserve | Phenobarbital / primidone (resistant myoclonus) | NCIT:C739 (Phenobarbital) |

*"Valproic acid is the drug of choice, except for PMEs due to mitochondrial diseases. Levetiracetam and clonazepam should be considered as the first add-on treatment. Zonisamide and perampanel represent promising alternatives"* ([PMID: 28799509](https://pubmed.ncbi.nlm.nih.gov/28799509/)).

**Drugs to AVOID (aggravate myoclonus/seizures):** carbamazepine, phenytoin, oxcarbazepine, lamotrigine, vigabatrin, gabapentin, pregabalin. *"Avoidance of drugs known to aggravate myoclonus and seizures, such as carbamazepine and phenytoin, is paramount"* ([PMID: 28799509](https://pubmed.ncbi.nlm.nih.gov/28799509/)).

**Supportive / rehabilitative care.** Physical, occupational, and speech therapy for ataxia and functional decline; mobility aids; falls prevention.

**Advanced / experimental therapeutics.** No approved gene, cell, or RNA therapy for MEAK. The mechanistically rational emerging strategy is **Kv3 channel positive modulation** (small-molecule Kv3 openers) to augment residual channel function — motivated by the fever-improvement phenomenon (temperature-induced leftward activation shift, [PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/)) and by cryo-EM structures that *"may guide strategies for the design of pharmaceutical drugs targeting Kv3 channels"* ([PMID: 35840580](https://pubmed.ncbi.nlm.nih.gov/35840580/)).

**Personalized medicine.** Treatment selection is genotype-informed within the *KCNC1* spectrum: LoF/dominant-negative MEAK (R320H) is the target for Kv3 openers, whereas gain-of-function *KCNC1* variants would require the opposite pharmacological direction — underscoring the need for functional variant characterization ([PMID: 35759918](https://pubmed.ncbi.nlm.nih.gov/35759918/)).

---

## Section 13 — Prevention

**Primary prevention.** Not applicable in the classical sense — MEAK arises de novo and cannot be prevented by risk-factor modification. Recurrence risk to future siblings is low (gonadal mosaicism caveat), so **genetic counseling** is the primary preventive tool.

**Secondary prevention / early detection.** Early molecular diagnosis (*KCNC1* testing in childhood-onset myoclonic epilepsy with ataxia and giant SEPs) enables appropriate drug selection and, critically, **avoidance of myoclonus-aggravating drugs**, preventing iatrogenic worsening.

**Genetic screening.** No population carrier screening is warranted (no carrier state). Prenatal/preimplantation testing is generally not applicable given the de novo nature, but is available for recurrence-risk counseling where parental mosaicism is a concern.

**Tertiary prevention.** Rehabilitation and falls-prevention to limit complications of progressive motor disability; optimized polytherapy to control myoclonus.

**Counseling.** Genetic counseling should explain the de novo mechanism, low but non-zero sibling recurrence risk, and the highly penetrant, specific MEAK phenotype.

---

## Section 14 — Other Species / Natural Disease

**Taxonomy / orthologs.** *KCNC1*/Kv3.1 is highly conserved across vertebrates. The mouse ortholog is *Kcnc1* (NCBI Taxon 10090). Conservation of the S4 voltage sensor and pore underpins the validity of cross-species models.

**Natural disease in other species.** No well-characterized naturally occurring *KCNC1*-driven MEAK equivalent is documented in companion animals or wildlife; the disease is defined in humans. (Not applicable / not established in veterinary databases such as OMIA for this specific disorder.)

**Comparative biology.** Evolutionary conservation of Kv3.1's role in fast-spiking neuron repolarization makes rodent models mechanistically faithful. Zoonotic potential and cross-species transmission are **not applicable** (genetic, non-infectious disease).

---

## Section 15 — Model Organisms

**Mouse models.** A **2026 mouse model of the recurrent R320H variant** recapitulates the core cellular defect, showing **impaired excitability of fast-spiking neurons** ([PMID: 41705663](https://pubmed.ncbi.nlm.nih.gov/41705663/)) — directly modeling the disinhibition mechanism. Constitutive *Kcnc1* loss-of-function mice have historically been used to study Kv3.1's role in high-frequency firing, motor coordination, and seizure susceptibility.

**In vitro / heterologous models.** Heterologous expression (e.g., mammalian cell lines / *Xenopus* oocytes) with **whole-cell patch-clamp** is the workhorse for functional classification — demonstrating dominant-negative LoF for R320H ([PMID: 25401298](https://pubmed.ncbi.nlm.nih.gov/25401298/)), no measurable current with dominant-negative effects for pore variants ([PMID: 31353862](https://pubmed.ncbi.nlm.nih.gov/31353862/)), gain-of-function for S6 variants ([PMID: 36419348](https://pubmed.ncbi.nlm.nih.gov/36419348/)), and dominant-positive behavior for p.Thr399Met ([PMID: 42347804](https://pubmed.ncbi.nlm.nih.gov/42347804/)).

**Neuronal / structural models.** A neuronal model demonstrated that R320H causes a **developmental dendritopathy** ([PMID: 33735526](https://pubmed.ncbi.nlm.nih.gov/33735526/)). Cryo-EM of human Kv3.1 provides a structural model of the gating machinery for drug design ([PMID: 35840580](https://pubmed.ncbi.nlm.nih.gov/35840580/)).

**Computational models.** A taxonomy-based multi-task learning SVM predicts gain-/loss-of-function for voltage-gated K+ channel variants, useful for classifying novel *KCNC1* variants where experimental data are lacking ([PMID: 35759918](https://pubmed.ncbi.nlm.nih.gov/35759918/)).

**Phenotype recapitulation / limitations.** The R320H mouse captures the fast-spiking excitability defect central to MEAK; limitations include incomplete modeling of the full progressive human ataxia/cerebellar-atrophy trajectory and human-specific network effects. In vitro systems capture channel biophysics but not circuit-level disinhibition or progression.

---

## Mechanistic Model / Interpretation

MEAK is best understood as a **single-variant channelopathy of fast-spiking neurons** with a clean genotype-to-phenotype logic:

```
                    ┌─────────────────────────────────────────┐
                    │  KCNC1 c.959G>A (p.Arg320His), de novo   │
                    │  S4 voltage sensor · heterozygous        │
                    └───────────────────┬─────────────────────┘
                                        │ dominant-negative
                                        ▼
                    ┌─────────────────────────────────────────┐
                    │  Kv3.1 heterotetramers lose fast K+      │
                    │  current → impaired rapid repolarization │
                    └──────────┬───────────────────┬──────────┘
                               │                   │
              cortical FS      │                   │   cerebellar
              interneurons     ▼                   ▼   neurons
        ┌───────────────────────────┐   ┌───────────────────────────┐
        │ Disinhibition of cortex   │   │ Cerebellar dysfunction +   │
        │ → cortical action         │   │ dendritopathy + cell death │
        │   myoclonus + generalized │   │ → ataxia, tremor,          │
        │   seizures, giant SEPs    │   │   progressive atrophy      │
        └───────────────────────────┘   └───────────────────────────┘
                               │                   │
                               └─────────┬─────────┘
                                         ▼
                    ┌─────────────────────────────────────────┐
                    │  MEAK: childhood-onset (med 9.5 y),      │
                    │  progressive, wheelchair by late teens,  │
                    │  transient fever improvement             │
                    └─────────────────────────────────────────┘
```

The **fever-improvement phenomenon** is the interpretive keystone linking mechanism to therapy: because raising temperature shifts wild-type Kv3.1 activation to more hyperpolarized voltages (increasing channel availability), it partially compensates for the dominant-negative deficit. This is a natural proof-of-concept that **pharmacologically augmenting Kv3 channel function** could be disease-modifying — the leading rational therapeutic hypothesis, now supported structurally by cryo-EM of the human channel.

The wider *KCNC1* allelic series clarifies why MEAK is so stereotyped: the specific biophysical consequence of a variant (dominant-negative LoF vs GoF vs dominant-positive), determined by its structural location (S4 vs pore/S6), maps onto distinct clinical syndromes. This has direct therapeutic implications — Kv3 openers would help LoF/MEAK but could worsen GoF variants — making **functional variant classification a prerequisite for precision therapy**.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report | Evidence type |
|---|---|---|---|
| [25401298](https://pubmed.ncbi.nlm.nih.gov/25401298/) | Recurrent de novo *KCNC1* mutation causes PME | Defines causal variant, 13% of PME, dominant-negative LoF | Human cohort + in vitro |
| [28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/) | MEAK: analysis of 20 cases and Kv3.1 temperature | Clinical syndrome, onset, MRI, fever improvement + biophysics | Human cohort + in vitro |
| [27629860](https://pubmed.ncbi.nlm.nih.gov/27629860/) | MEAK caused by heterozygous *KCNC1* | Mechanism (fast-spiking neurons), AD inheritance, cell types | Review / mechanism |
| [33735526](https://pubmed.ncbi.nlm.nih.gov/33735526/) | *KCNC1* developmental dendritopathy | High penetrance; dendritopathy beyond firing | Neuronal model |
| [31353862](https://pubmed.ncbi.nlm.nih.gov/31353862/) | *KCNC1* new de novo variants expand spectrum | Allelic series, neuronal disinhibition mechanism | Human + in vitro |
| [36419348](https://pubmed.ncbi.nlm.nih.gov/36419348/) | *KCNC1* gain of Kv3.1 function | GoF subgroup (DD/ID, hypotonia) — contrast to MEAK | Human + in vitro |
| [42347804](https://pubmed.ncbi.nlm.nih.gov/42347804/) | Kv3.1 dominant-positive variant (p.Thr399Met) | Dominant-positive mechanism nuance | In vitro |
| [28799509](https://pubmed.ncbi.nlm.nih.gov/28799509/) | Pharmacological treatment of PMEs | Drug hierarchy and drugs to avoid | Clinical review |
| [32972906](https://pubmed.ncbi.nlm.nih.gov/32972906/) | MEAK case report / review | Diagnostic clues (giant SEP), misdiagnosis risk | Case report |
| [35840580](https://pubmed.ncbi.nlm.nih.gov/35840580/) | Cryo-EM of human Kv3.1 | Structural gating machinery; drug-design relevance | Structural biology |
| [41705663](https://pubmed.ncbi.nlm.nih.gov/41705663/) | Mouse model of recurrent variant | Fast-spiking excitability defect in vivo | Mouse model |
| [35759918](https://pubmed.ncbi.nlm.nih.gov/35759918/) | ML prediction of Kv channel variant effects | Functional classification tool for novel variants | Computational |

**Concordance.** The human cohorts, in vitro electrophysiology, the neuronal dendritopathy study, the mouse model, and the cryo-EM structures converge on a single coherent mechanism (Kv3.1 LoF → fast-spiking neuron dysfunction → disinhibition + cerebellar degeneration). No major contradictions were identified; the GoF and dominant-positive studies refine rather than challenge the model by showing that variant biophysics is context- and location-dependent.

---

## Limitations and Knowledge Gaps

1. **Epidemiology is imprecise.** No population prevalence/incidence figures exist for MEAK specifically; the 13% figure reflects the fraction of *unexplained PME*, not general-population frequency.
2. **Natural history quantification is limited.** Progression rate, long-term survival curves, and validated QoL measures (EQ-5D/SF-36) for MEAK are not established.
3. **No disease-modifying therapy validated.** Kv3 positive modulation is mechanistically rational but not yet proven in MEAK clinical trials.
4. **Modifier genetics unexplored.** No modifier genes or epigenetic contributors identified to explain the modest phenotypic variability.
5. **Fever effect not therapeutically translated.** The temperature-gating link is a compelling clue but its safe therapeutic exploitation (channel openers) requires validation.
6. **Model completeness.** Existing mouse and in vitro models capture channel biophysics and fast-spiking defects but incompletely recapitulate the progressive human cerebellar-atrophy trajectory.
7. **No veterinary/natural-disease counterpart** is documented, limiting comparative pathology insight.

---

## Proposed Follow-up Experiments / Actions

1. **Preclinical Kv3 opener trials.** Test small-molecule Kv3 positive modulators in the R320H mouse model ([PMID: 41705663](https://pubmed.ncbi.nlm.nih.gov/41705663/)) for rescue of fast-spiking excitability, myoclonus, and ataxia — leveraging the temperature-gating rationale ([PMID: 28380698](https://pubmed.ncbi.nlm.nih.gov/28380698/)) and cryo-EM structure ([PMID: 35840580](https://pubmed.ncbi.nlm.nih.gov/35840580/)).
2. **Natural-history registry.** Establish a prospective MEAK cohort with standardized myoclonus scales, ataxia scores (e.g., SARA), serial MRI cerebellar volumetry, and QoL instruments to quantify progression and define trial endpoints.
3. **Biomarker development.** Formalize giant SEP amplitude and quantitative EEG/EMG cortical-myoclonus metrics ([PMID: 32972906](https://pubmed.ncbi.nlm.nih.gov/32972906/)) as objective disease-severity/response biomarkers.
4. **Allele-specific therapeutics.** Explore allele-selective silencing/ASO strategies against the dominant-negative R320H transcript to relieve poisoning of wild-type Kv3.1.
5. **Functional variant pipeline.** Apply and extend the ML classifier ([PMID: 35759918](https://pubmed.ncbi.nlm.nih.gov/35759918/)) plus high-throughput patch-clamp to prospectively classify novel *KCNC1* variants (LoF vs GoF), enabling correct therapeutic direction.
6. **iPSC-derived interneuron/cerebellar models** from patients to study the developmental dendritopathy ([PMID: 33735526](https://pubmed.ncbi.nlm.nih.gov/33735526/)) and screen candidate compounds in a human genetic background.
7. **Genotype-guided prescribing guidance.** Codify avoidance of myoclonus-aggravating agents ([PMID: 28799509](https://pubmed.ncbi.nlm.nih.gov/28799509/)) into *KCNC1*-specific management pathways to prevent iatrogenic worsening.

---

*Report compiled from 9 confirmed findings across 5 investigation iterations and 19 reviewed papers. Evidence types span human clinical cohorts, in vitro electrophysiology, neuronal and mouse models, structural biology (cryo-EM), and computational prediction.*


## Artifacts

- [OpenScientist final report](Progressive_Myoclonic_Epilepsy_Type_7-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Progressive_Myoclonic_Epilepsy_Type_7-deep-research-openscientist_artifacts/final_report.pdf)