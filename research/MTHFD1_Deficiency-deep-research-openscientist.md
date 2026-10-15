---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-04T17:23:32.933556'
end_time: '2026-09-04T18:07:56.178086'
duration_seconds: 2663.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: MTHFD1 Deficiency
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
  path: MTHFD1_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: MTHFD1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MTHFD1 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MTHFD1 Deficiency** covering all of the
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

# MTHFD1 Deficiency — Comprehensive Disease Characteristics Report

**Disease:** MTHFD1 Deficiency (Methylenetetrahydrofolate Dehydrogenase 1 Deficiency)
**Category:** Mendelian (autosomal recessive inborn error of folate metabolism / inborn error of immunity)
**Report type:** Literature-based knowledge synthesis (no primary patient data provided)
**Date:** 2026-09-04

> **Evidence-source note:** Because this is an ultra-rare disorder (<20 molecularly confirmed patients worldwide as of the primary literature reviewed), most clinical statements derive from individual case reports and small case series (human clinical evidence). Mechanistic statements draw on patient-fibroblast studies (in vitro) and mouse models (model organism). Where a claim is inferred rather than demonstrated, this is stated explicitly.

---

## 1. Disease Information

**Overview.** MTHFD1 deficiency is a rare autosomal recessive inborn error of the **cytoplasmic (and nuclear) folate cycle** caused by biallelic loss-of-function variants in *MTHFD1*. The gene encodes a **trifunctional enzyme** carrying three catalytic activities: 5,10-methylenetetrahydrofolate dehydrogenase, 5,10-methenyltetrahydrofolate cyclohydrolase, and 10-formyltetrahydrofolate synthetase. Loss of function disrupts the supply of one-carbon folate coenzymes required for **de novo purine synthesis, de novo thymidylate (dTMP) synthesis, and remethylation of homocysteine to methionine**. Clinically it manifests as a multisystem, folate-responsive disorder combining **megaloblastic anemia, combined/severe combined immunodeficiency, atypical hemolytic-uremic syndrome (aHUS), hyperhomocysteinemia, and neurologic abnormalities** (PMID: 21813566; 25548164; 32414565).

It was first described in 2011 by Watkins et al., who identified it via exome sequencing in a single infant — "the first case of an inborn error of folate metabolism affecting the trifunctional MTHFD1 protein" (PMID: 21813566).

**Key identifiers.**
- **Mondo:** **MONDO:0060611** — "combined immunodeficiency and megaloblastic anemia with or without hyperhomocysteinemia" (acronym **CIMAH**) *(verified via EBI OLS4/MONDO)*
- **OMIM (phenotype):** **#617780** — same name
- **OMIM (gene):** *MTHFD1* **172460**
- **Orphanet:** **ORPHA:658813**
- **UMLS:** C4540434 · **GARD:** 0026001 · **MedGen:** 1615364
- **HGNC:** 7432 · **NCBI Gene:** 4522 · **Ensembl:** ENSG00000100714 · **UniProt:** P11586 · **cytoband:** 14q23.3 *(verified via MyGene.info)*
- **ICD-11:** 4A00.xx (combined immunodeficiencies) / 5C50.x (metabolic disorders) — no dedicated code; **ICD-10:** D81.x (combined immunodeficiencies) / E53.8 as closest approximations
- **MeSH:** no dedicated descriptor; indexed under "Immunologic Deficiency Syndromes," "Anemia, Megaloblastic," and "Folic Acid" metabolism terms

**Synonyms / alternative names.** MTHFD1 deficiency; Methylenetetrahydrofolate dehydrogenase 1 deficiency; **CIMAH** (Combined ImmunodeficiencY and Megaloblastic Anemia with or without Hyperhomocysteinemia); MTHFD1-related folate metabolism disorder. Gene aliases: MTHFC, MTHFD.

**Data source type.** Aggregated disease-level knowledge derived from published individual patient reports and biochemical/model studies — not EHR-derived population data.

---

## 2. Etiology

**Primary cause (genetic).** Biallelic (homozygous or compound heterozygous) pathogenic variants in *MTHFD1* (14q23.3). Reported causal variants include missense, nonsense, and splice-site changes distributed across the dehydrogenase/cyclohydrolase and synthetase domains (see §4). The defect causes markedly reduced MTHFD1 protein and **absent methylenetetrahydrofolate dehydrogenase activity** in patient cells (PMID: 32414565).

**Genetic risk factors.**
- *Causal:* rare biallelic loss-of-function *MTHFD1* variants (the disease itself).
- *Common susceptibility (distinct entity):* **MTHFD1 R653Q (c.1958G>A, rs2236225)** in the synthetase domain — a low-penetrance hypomorphic variant, homozygous in ~20% of individuals of European ancestry, associated with neural tube defects (NTDs), congenital heart defects (CHDs), and adverse pregnancy outcomes (PMID: 23704330; 26408344). It acts predominantly as a **maternal** risk factor: maternal QQ homozygosity is associated with NTD-affected pregnancy at **OR ~1.5** (original Irish cohort OR 1.52, 95% CI 1.16–1.99, P=0.003, PMID 12384833; independent replication OR 1.49, 95% CI 1.07–2.09, P=0.019, PMID 16552426; meta-analysis of 9 studies / 4,302 cases / 4,238 controls confirming a maternal-allele excess, PMID 24977710). A promoter SNP (rs1076991) further modifies risk in combination with R653Q (PMID 19130090). This is a **modifier/susceptibility allele, not the Mendelian disease**.
- *Consanguinity:* homozygous cases have been reported in consanguineous/founder settings (e.g., Kuwaiti children homozygous for c.517C>T p.Arg173Cys; PMID: 42301236), consistent with AR disease.

**Environmental risk factors.** Maternal/dietary **folate deficiency** can exacerbate one-carbon metabolic insufficiency; in mouse models maternal folate-deficient diet interacts with synthetase deficiency (PMID: 26408344). **Arsenic** (arsenic trioxide) directly targets MTHFD1/SUMO-dependent nuclear dTMP biosynthesis, a teratogenic mechanism converging on the same pathway (PMID: 28265077).

**Protective factors.** **Folate/folinic acid supplementation** is the principal disease-modifying (protective) factor — it partially restores one-carbon flux and improves hematologic and immune outcomes (PMID: 23296427; 42301236). Adequate maternal folate status is protective against the R653Q-associated developmental risks (inferred from GxE data, PMID: 26408344).

**Gene–environment interaction.** Folate availability modulates the phenotype at every level: for the R653Q hypomorph, folate deficiency increases risk of developmental defects; for the Mendelian disease, exogenous reduced folate (folinic acid) partially bypasses the block. Arsenic × folate is a documented toxicant–pathway interaction (PMID: 28265077).

---

## 3. Phenotypes

Onset is typically **neonatal to infantile**; severity and progression are **variable** (from lethal early infancy to milder, treatment-responsive disease). HPO term suggestions and approximate frequencies (from the small published cohort) below.

| Phenotype | Type | Onset / course | Approx. frequency | HPO suggestion |
|---|---|---|---|---|
| Megaloblastic anemia | Lab / hematologic | Infantile; responsive to therapy | Near-universal (hallmark) | HP:0001889 |
| Combined / severe combined immunodeficiency | Clinical / immune | Infantile; progressive if untreated | Very common | HP:0005387 / HP:0004430 |
| Recurrent infections (bacterial, sinopulmonary; opportunistic incl. *Pneumocystis*) | Clinical sign | Infantile | Common | HP:0002719 |
| Lymphopenia (all subsets), poor vaccine response | Lab | Infantile | Common | HP:0001888 |
| Atypical hemolytic-uremic syndrome / thrombotic microangiopathy | Clinical / lab | Infancy–childhood, episodic | Subset (several patients) | HP:0005575 / HP:0001937 |
| Hyperhomocysteinemia | Lab | Congenital-biochemical | Frequent (not universal) | HP:0002160 |
| Hypomethioninemia | Lab | Biochemical | Reported | HP:0500152 (low methionine) |
| Neurologic abnormalities (seizures, developmental delay) | Clinical | Infantile | Subset | HP:0001250 / HP:0001263 |
| Failure to thrive | Clinical | Infantile | Common | HP:0001508 |
| Autoimmune disease (e.g., autoimmune thyroiditis) | Clinical | Childhood | Subset | HP:0002960 |
| Retinopathy | Clinical | Variable | Rare (1 patient) | HP:0000488 |
| Liver fibrosis | Clinical / path | Childhood | Rare | HP:0001395 |
| Severe metabolic acidosis | Lab | Neonatal (severe cases) | Rare (lethal cases) | HP:0002153 |

Evidence: PMID 21813566; 23296427; 25633902; 32414565; 42301236.

**Quality-of-life impact.** Untreated disease is life-threatening (recurrent/opportunistic infection, bone-marrow failure, TMA/renal injury, neurodevelopmental impairment). With early folate/folinic acid therapy, hematologic and immune function can substantially normalize, allowing discontinuation of anti-infective prophylaxis (PMID: 27707659). No formal EQ-5D/SF-36 data exist for this ultra-rare disease.

---

## 4. Genetic / Molecular Information

**Causal gene.** *MTHFD1* (HGNC:7432; OMIM 172460; NCBI Gene 4522; Ensembl ENSG00000100714), chromosome **14q23.3**, encoding the ~101 kDa trifunctional protein C1-THF synthase (UniProt P11586). N-terminal domain: dehydrogenase + cyclohydrolase (NADP-binding); C-terminal domain: 10-formyltetrahydrofolate synthetase.

**Reported pathogenic variants (germline, biallelic).**
- c.517C>T, **p.Arg173Cys** (homozygous; Kuwaiti patients) — PMID: 42301236
- c.517C>T, **p.Arg173Cys** vicinity / **p.R173C** critical NADP-binding arginine + c.727+1G>A splice (first proband) — PMID: 21813566
- c.806C>T, **p.Thr296Ile** + c.1674G>A splice (exon skipping) — PMID: 25633902
- c.146C>T, **p.Ser49Phe** + c.673G>T, **p.Glu225*** (nonsense) — PMID: 25633902
- Compound heterozygous missense + exon-13 deletion (structural) — PMID: 27707659
- Additional deleterious compound-heterozygous variants — PMID: 32414565

**Variant classes:** missense, nonsense, canonical splice-site, and exonic deletions — all consistent with **loss of function** (no dominant-negative/gain-of-function reported). ACMG classification: reported variants are pathogenic/likely pathogenic based on segregation, functional enzymology, and predicted deleteriousness.

**ClinVar landscape (reference transcript NM_005956.4; queried Iteration 4).** 64 **Pathogenic** and 30 **Likely pathogenic** records (vs 629 VUS and 590 Benign among 681 total gene entries). The disease-associated P/LP spectrum is **overwhelmingly loss-of-function/null**: among 64 P/LP records — SNVs 39 (predominantly canonical splice ±1/±2, e.g., c.377+1G>C, c.616-2A>C, c.2280-1G>T, c.1264+1G>A; plus nonsense c.316G>T p.Glu106Ter, c.886G>T p.Glu296Ter), frameshift deletions 10 (e.g., c.2375del p.Gly792fs, c.1755_1756del p.Arg585fs, c.153_154del p.Ile53fs), duplications 2 (c.731dup p.Asp244fs; c.253dup p.Ile85fs), insertion 1 (c.2479_2480insTTGCACA p.Arg827fs), and 12 large copy-number gains/losses (chromosomal, largely incidental). Many P/LP entries are explicitly annotated to the trait "Combined immunodeficiency and megaloblastic anemia." The large VUS pool reflects the gene's tolerance of common missense variation (e.g., R653Q) and complicates novel-missense classification. *(Source: NCBI ClinVar via E-utilities.)*

**Functional consequence.** Loss of function: MTHFD1 protein reduced to **4.8–14.3% of control** (one patient ~44%) with **no detectable dehydrogenase activity** in fibroblasts (PMID: 32414565).

**Allele frequency.** Rare disease alleles are absent/ultra-rare in gnomAD. In contrast, the common non-disease modifier **R653Q (rs2236225; GRCh38 14-64442127-G-A)** is very common — **gnomAD v4 global genome AF 0.386**, with ancestry-specific AF: **Non-Finnish European 0.453 (≈20.5% QQ homozygotes under Hardy-Weinberg)**, Admixed American 0.519, South Asian 0.505, Finnish 0.446, Ashkenazi Jewish 0.436, Middle Eastern 0.432, East Asian 0.221, African/African-American 0.212 *(verified via gnomAD v4 API; consistent with the "~20% of Caucasians homozygous" statement in PMID 23704330)*.

**Somatic vs germline.** Disease variants are **germline**. (Somatic relevance: MTHFD1 is exploited in cancer one-carbon metabolism and is targeted by arsenic trioxide — PMID: 28265077 — but this is not the inherited disease.)

**Modifier genes / epigenetics / chromosomal abnormalities.** No formally established modifier genes beyond folate-pathway context. Downstream **DNA hypomethylation** is expected from reduced methionine/SAM (mechanistically inferred; not systematically profiled in patients). No recurrent chromosomal abnormalities; one causal exon-13 deletion is a small intragenic structural variant (PMID: 27707659).

---

## 5. Environmental Information

- **Environmental factors:** dietary **folate deficiency** aggravates the metabolic block (GxE; PMID: 26408344). **Arsenic** targets the same nuclear dTMP pathway (PMID: 28265077).
- **Lifestyle factors:** maternal folate intake is the key modifiable factor for pathway-related developmental risk. Alcohol (a folate antagonist) and antifolate drugs would be expected to worsen one-carbon insufficiency (inferred).
- **Infectious agents:** none causal. Infections are **consequences** of the immunodeficiency (recurrent bacterial sinopulmonary infections; opportunistic organisms including *Pneumocystis jirovecii*, consistent with a SCID-like state).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function *MTHFD1* variants** reduce MTHFD1 protein to ~5–14% of normal and abolish dehydrogenase activity (**demonstrated**, PMID: 32414565).
2. This **impairs interconversion of one-carbon–substituted tetrahydrofolate coenzymes** (methylene-THF ↔ methenyl-THF ↔ 10-formyl-THF) in the cytosol/nucleus (**demonstrated** enzymology).
3. Reduced supply of **5,10-methylene-THF** and **10-formyl-THF** limits three downstream outputs; the pathway then **branches**:
   - **Branch A — Nuclear de novo thymidylate (dTMP) synthesis falls (~50% reduced flux)** → **uracil is misincorporated into DNA** → futile base-excision-repair cycles and genomic stress (**demonstrated**, PMID: 25548164). → **leads to** ineffective erythropoiesis (**megaloblastic anemia**) and impaired lymphocyte proliferation (**combined/severe combined immunodeficiency**).
   - **Branch B — Homocysteine remethylation to methionine falls (~90% reduced formate→methionine flux)** → **hyperhomocysteinemia and low methionine/SAM** (**demonstrated**, PMID: 25548164). → endothelial injury contributes to **thrombotic microangiopathy / atypical HUS** (**inferred** from homocysteine's known endothelial toxicity) and reduced methylation capacity contributes to **neurologic abnormalities** (**inferred**).
   - **Branch C — De novo purine synthesis is relatively spared** in patient fibroblasts (formate→purine flux unaffected), explaining why purine-dependent phenotypes are less prominent than dTMP-dependent ones (**demonstrated**, PMID: 25548164).
4. The combined hematologic failure, immune failure, and vascular/renal injury → **recurrent/opportunistic infection, bone-marrow failure, renal impairment, failure to thrive, and neurodevelopmental impairment** (**human clinical**, PMID: 23296427; 42301236).
5. **Intervention branch:** exogenous **reduced folate (folinic acid)** replenishes downstream one-carbon pools, partially restoring dTMP/methionine synthesis → **improved hematology and immune reconstitution** (**demonstrated**, PMID: 27707659; 23296427).

### Category detail (checklist)
- **Molecular pathways:** folate/one-carbon metabolism (KEGG hsa00670 one-carbon pool by folate); methionine cycle; de novo purine (IMP) and pyrimidine (dTMP) biosynthesis. **Reactome:** metabolism of folate and pterines.
- **Cellular processes:** DNA replication/repair (uracil misincorporation, BER), cell-cycle arrest in rapidly dividing precursors (erythroid, lymphoid), impaired proliferation. GO suggestions: GO:0006730 (one-carbon metabolic process), GO:0046655 (folic acid metabolic process), GO:0006231 (dTMP biosynthetic process), GO:0009086 (methionine biosynthesis), GO:0006189 (de novo IMP biosynthesis).
- **Protein dysfunction:** loss of function / markedly reduced protein abundance and abolished dehydrogenase activity; MTHFD1 is normally partitioned between cytosol and nucleus (SUMO-dependent nuclear import for dTMP synthesis) (PMID: 25548164; 28265077).
- **Metabolic changes:** ↓ 10-formyl-THF, ↓ methionine/SAM, ↑ homocysteine, ↑ uracil in DNA; elevated methylmalonic acid and selectively decreased methylcobalamin synthesis were noted in the index patient (PMID: 21813566).
- **Immune system involvement:** combined immunodeficiency with lymphopenia across subsets and poor vaccine responses (PMID: 27707659) plus paradoxical **autoimmunity** (thyroiditis, autoimmune disease) — dysregulation of both arms.
- **Tissue damage mechanisms:** endothelial/microvascular injury (TMA/aHUS); ineffective hematopoiesis; possible hepatic fibrosis.
- **Biochemical abnormality:** trifunctional folate enzyme deficiency (EC 1.5.1.5 / EC 3.5.4.9 / EC 6.3.4.3).
- **Epigenetic changes:** reduced SAM → expected global/DNA hypomethylation (**inferred**, not systematically profiled).
- **Molecular profiling / functional genomics:** patient-fibroblast flux studies (PMID: 25548164); MTHFD1 as an arsenic and antifolate metabolic target and a dependency in some cancers (PMID: 28265077).

**Cell types (CL suggestions):** erythroid progenitor (CL:0000038), T cell (CL:0000084), B cell (CL:0000236), hematopoietic stem/progenitor cell (CL:0000037), vascular endothelial cell (CL:0000115).

---

## 7. Anatomical Structures Affected

- **Organ / system level (primary):** hematopoietic/immune system — **bone marrow** (UBERON:0002371), **blood** (UBERON:0000178). **Kidney** (UBERON:0002113) via aHUS/TMA. **Central nervous system / brain** (UBERON:0000955) via neurologic features.
- **Secondary involvement:** **retina/eye** (UBERON:0000970) — retinopathy; **liver** (UBERON:0002107) — fibrosis; **lungs** (recurrent pneumonia); **thyroid** (autoimmune thyroiditis).
- **Tissue/cell level:** erythroid and lymphoid lineages; vascular endothelium (microangiopathy).
- **Subcellular level (GO Cellular Component):** **cytosol** (GO:0005829) and **nucleus** (GO:0005634) — MTHFD1 functions in both compartments; nuclear pool drives de novo dTMP synthesis (PMID: 25548164). Note: MTHFD1 is cytoplasmic/nuclear, distinct from the mitochondrial paralog MTHFD2/MTHFD1L.
- **Localization / lateralization:** systemic and **bilateral** (hematologic, immune, metabolic); renal and retinal involvement generally bilateral.

---

## 8. Temporal Development

- **Onset:** congenital/neonatal to infantile; **subacute-to-chronic** presentation with acute decompensations (infection, TMA, acidosis).
- **Progression:** without treatment, **progressive** with life-threatening bone-marrow failure and infection; severe neonatal cases can be **rapidly fatal** (siblings dead at 9 weeks with megaloblastic anemia, infection, severe acidosis; PMID: 25633902; a 3-year-old died on day 18 of PICU care, PMID: 42301236).
- **Course pattern:** chronic underlying metabolic defect with **episodic** TMA/aHUS crises; largely **treatment-responsive** when folate therapy is started early.
- **Critical period / window of opportunity:** **early molecular diagnosis and prompt folinic/folic acid initiation** is the key intervention window — determines survival and degree of immune reconstitution (PMID: 42301236; 27707659).

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** (biallelic loss-of-function). Both parents obligate heterozygous carriers; unaffected sib carrying neither variant supports segregation (PMID: 21813566).
- **Penetrance / expressivity:** biallelic LOF appears **highly penetrant** but with **variable expressivity** (severity ranges from lethal infancy to milder folate-responsive disease), even within families (PMID: 25633902).
- **Epidemiology:** **ultra-rare** — fewer than ~20 molecularly confirmed patients reported worldwide in the reviewed literature; true prevalence/incidence unknown (no registry estimates). No published incidence per 100,000. (For context, the *R653Q modifier*-associated **neural tube defects** occur in ~1 in 1000 pregnancies in the US/Europe, and maternal periconceptional folic acid reduces NTD occurrence by 50–70% — PMID 22856873; but these are pathway-level, not MTHFD1-deficiency, figures.)
- **Founder / consanguinity:** homozygous cases reported in consanguineous families (e.g., Kuwaiti children, p.Arg173Cys; PMID: 42301236); no established broad founder allele.
- **Carrier frequency:** not established for pathogenic LOF alleles (ultra-rare). By contrast the common **R653Q** modifier reaches ~50% allele frequency in Europeans (PMID: 23704330) — but this is **not** the disease allele.
- **Sex ratio / age distribution:** no sex bias reported; affected individuals are predominantly infants/young children.
- **Geographic distribution:** cases reported from Europe, North America, and the Middle East; no defined endemic region.
- **Variant-frequency geography (R653Q modifier, gnomAD v4):** the common R653Q Q-allele is most frequent in Admixed American (0.519), South Asian (0.505), Non-Finnish European (0.453), Finnish (0.446), Ashkenazi (0.436) and Middle Eastern (0.432) populations, and least frequent in East Asian (0.221) and African/African-American (0.212) populations — potentially relevant to population-specific folate-pathway developmental risk (verified via gnomAD v4).

---

## 10. Diagnostics

**Laboratory / biochemical.**
- **CBC + blood smear:** macrocytic **megaloblastic anemia** (± pancytopenia), hypersegmented neutrophils (LOINC macrocyte/MCV panels).
- **Plasma total homocysteine:** elevated (hyperhomocysteinemia) in many patients; **methionine** low/normal.
- **Methylmalonic acid:** elevated in the index case; **methylcobalamin synthesis** decreased in cultured fibroblasts (PMID: 21813566).
- **Immunology:** lymphopenia across T/B/NK subsets, hypogammaglobulinemia/poor vaccine responses (PMID: 27707659).
- **Renal / hemolysis markers** during aHUS/TMA (schistocytes, ↑LDH, ↑creatinine, thrombocytopenia).
- **Cellular biomarkers (research):** absent MTHFD1 dehydrogenase activity and reduced protein by Western blot in fibroblasts; **elevated uracil in DNA**; abnormal formate-incorporation flux assays (PMID: 32414565; 25548164).

**Genetic testing (definitive).** Diagnosis is confirmed by identifying **biallelic *MTHFD1* variants**. Recommended approach: **whole-exome sequencing (WES)** or a **combined immunodeficiency / inborn-errors-of-metabolism gene panel** including *MTHFD1*; WGS or targeted analysis can detect **intragenic structural variants** (e.g., exon-13 deletion missed by standard SNV calling — requires read-depth/CNV analysis) (PMID: 27707659; 21813566; 23296427). Single-gene sequencing of *MTHFD1* is appropriate when phenotype is characteristic. CMA/karyotype/FISH generally not informative (defect is intragenic). Mitochondrial DNA and repeat-expansion testing: not applicable.

**Clinical criteria / differential diagnosis.** No formal consensus criteria. Consider MTHFD1 deficiency in any infant with **megaloblastic anemia + immunodeficiency + hyperhomocysteinemia and/or aHUS**. Differentials: other inborn errors of folate/cobalamin metabolism (**hereditary folate malabsorption** [SLC46A1], **cblC/MMACHC** and related cobalamin defects, **transcobalamin deficiency**, **DHFR deficiency**, **MTHFR deficiency**), other SCID genotypes, and complement-mediated aHUS. Distinguishing features: MTHFD1 uniquely combines the folate-cycle biochemistry (low methionine, high Hcy, normal purine flux) with combined immunodeficiency (PMID: 32412981).

**Screening.** Not part of standard newborn screening. Cascade carrier testing of relatives once the familial variants are known; prenatal/preimplantation testing feasible for known biallelic variants.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** highly variable and **diagnosis-timing–dependent**. Early-diagnosed, promptly treated patients can achieve immune reconstitution and good outcomes; delayed diagnosis carries high mortality (neonatal deaths and a PICU death reported) (PMID: 25633902; 42301236).
- **Morbidity:** infections, bone-marrow failure, renal injury from TMA/aHUS, neurodevelopmental impairment, and rarely retinopathy/liver fibrosis.
- **Recovery potential:** hematologic and immune parameters are **substantially reversible with folate/folinic acid**; some deficits (e.g., established retinopathy, neurodevelopmental sequelae, renal damage) may be irreversible.
- **Prognostic factors:** timeliness of molecular diagnosis and folate/folinic-acid initiation; severity of presenting phenotype (severe neonatal acidosis portends poor outcome); degree of residual MTHFD1 expression.
- No formal 5-/10-year survival statistics exist (case-level data only).

---

## 12. Treatment

**Core pharmacotherapy (metabolic/precision therapy).**
- **Folinic acid (5-formyltetrahydrofolate / leucovorin)** — preferred reduced folate that bypasses the dihydrofolate reductase step; enables immune reconstitution and hematologic correction (PMID: 27707659). NCIT: **Leucovorin Calcium (C576)** / Folinic acid.
- **Folic acid** — effective in milder/responsive patients; produced significant clinical improvement (PMID: 42301236). NCIT: **Folic Acid (C542)**.
- **Hydroxocobalamin (vitamin B12)** — used to support remethylation; provided partial immune reconstitution with folate in the index case (PMID: 23296427). NCIT: **Hydroxocobalamin (C61805)**.
- **Betaine** — remethylation agent to lower homocysteine (PMID: 25633902). NCIT: **Betaine (C61463)**.
- **Methionine supplementation** — may be considered when hypomethioninemia present (inferred/supportive).

**Supportive / adjunctive care.** Anti-infective prophylaxis and immunoglobulin (IVIG) while immunodeficient; transfusion support for anemia; management of aHUS/TMA (supportive ± eculizumab per complement-mediated protocols, though MTHFD1-related TMA is metabolic in origin); treatment of autoimmune complications. Discontinuation of prophylaxis becomes possible after immune reconstitution on folinic acid (PMID: 27707659).

**Advanced/experimental therapeutics.** No approved gene, cell, or RNA therapies. **Hematopoietic stem-cell transplantation is generally unnecessary** because the immunodeficiency is metabolically correctable — a key contrast with genetic SCIDs (this is an important treatment distinction). No registered disease-specific clinical trials identified.

**Pharmacogenomics.** Not established; genotype-guided care centers on choosing **reduced folate (folinic acid)** to bypass downstream steps.

**Treatment strategy / algorithm.** Suspect → urgent molecular diagnosis → immediate folinic/folic acid ± hydroxocobalamin ± betaine → supportive anti-infective/transfusion care → monitor hematology, homocysteine, and immune reconstitution → taper prophylaxis once reconstituted. **Early treatment is the strongest determinant of survival** (PMID: 42301236).

---

## 13. Prevention

- **Primary prevention:** for the **Mendelian disease**, prevention is via **genetic counseling, carrier testing, and reproductive options** (prenatal/PGT) in at-risk families — not modifiable by lifestyle. For the **common R653Q modifier**, adequate **periconceptional folate** reduces associated NTD/CHD/pregnancy risk (GxE evidence; PMID: 26408344).
- **Secondary prevention:** early recognition and prompt folate/folinic-acid therapy to prevent irreversible organ damage; cascade family screening.
- **Tertiary prevention:** anti-infective prophylaxis, IVIG, homocysteine control (betaine) to prevent vascular/renal complications until reconstitution.
- **Counseling:** autosomal recessive counseling — 25% recurrence risk for carrier couples.
- **Immunization / public health:** live vaccines contraindicated while immunodeficient; general folate fortification is a population-level protective measure for folate-pathway risks.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *MTHFD1* is highly conserved. Mouse ortholog **Mthfd1** (NCBI Gene 108156; taxon *Mus musculus* NCBITaxon:10090). Orthologs exist across vertebrates and yeast (ADE3).
- **Natural disease:** no well-characterized spontaneous *MTHFD1*-deficiency disease reported in companion animals or wildlife (OMIA: none established).
- **Comparative biology:** the trifunctional C1-THF synthase and its one-carbon role are evolutionarily conserved from yeast to human; complete synthetase loss is **embryonic-lethal in mice**, underscoring conserved essentiality (PMID: 23704330).
- **Zoonotic potential:** none (non-infectious genetic disease).

---

## 15. Model Organisms

- **Mouse (primary model).** A **Mthfd1 synthetase-specific hypomorph (Mthfd1S)** was engineered to model the R653Q variant by inactivating 10-formylTHF synthetase activity without disrupting protein expression or the other two activities (PMID: 23704330).
  - **Mthfd1S−/−:** embryonic lethal (~E10.5), developmentally delayed/abnormal — demonstrates essentiality.
  - **Mthfd1S+/−:** reduced plasma/liver 10-formyl-THF, impaired de novo purine synthesis in MEFs, decreased neutrophil counts in pregnancy, increased embryonic developmental defects, and (on a separate cross) **increased congenital heart defects, chiefly ventricular septal defects** (PMID: 23704330; 26408344).
- **Cellular / in vitro models:** patient-derived **fibroblasts** are the workhorse for enzymology and one-carbon flux studies (formate-incorporation assays, uracil-in-DNA measurement, Western blot of MTHFD1) (PMID: 25548164; 32414565). **MEFs** used for purine-synthesis flux.
- **Phenotype recapitulation:** the mouse synthetase model recapitulates **developmental / purine-synthesis** aspects relevant to the *common R653Q variant* (NTD/CHD/pregnancy risk) but is a **partial** model of the human **biallelic Mendelian disease** (it does not reproduce the full megaloblastic-anemia + combined-immunodeficiency + aHUS syndrome). Patient fibroblasts best recapitulate the human dTMP/methionine flux defects.
- **Model limitations:** no reported mouse fully reproducing the human combined-immunodeficiency phenotype; ultra-rare human numbers limit genotype–phenotype modeling.
- **Resources:** MGI (Mthfd1), model described in Rozen-lab publications (PMID: 23704330, 26408344).

---

## Supported and Refuted Hypotheses

**Supported:**
- MTHFD1 deficiency is an AR loss-of-function disorder of the cytoplasmic/nuclear folate cycle (PMID: 21813566; 32414565).
- The hematologic + immune phenotype arises chiefly from **impaired nuclear de novo dTMP synthesis with uracil misincorporation**, with **purines relatively spared** (PMID: 25548164).
- The disorder is **folate/folinic-acid responsive**, and early treatment improves survival/immune reconstitution (PMID: 27707659; 23296427; 42301236).
- The common **R653Q** synthetase variant is a **distinct low-penetrance developmental risk modifier**, not the Mendelian disease (PMID: 23704330; 26408344).

**Refuted / clarified:**
- Not primarily a purine-synthesis disorder at the cellular level (purine flux preserved in patient cells) — refutes the intuitive "SCID via purine block" model as the main mechanism (PMID: 25548164).
- Not a mitochondrial folate defect — MTHFD1 is cytosolic/nuclear (distinct from MTHFD2/MTHFD1L).
- HSCT is generally not required (metabolically correctable), distinguishing it from classical genetic SCID.

---

## Limitations and Future Directions

- **Ultra-rare** (<~20 confirmed patients): frequencies, penetrance, and prognosis are estimated from case-level data; no registry/epidemiologic denominators.
- Mechanistic data on aHUS/neurologic branches remain partly **inferred** (homocysteine-mediated endothelial injury; hypomethylation) rather than directly demonstrated in patients.
- No mouse model of the **biallelic human disease**; no approved advanced therapeutics or trials.
- **Future needs:** a natural-history registry; systematic immunophenotyping and methylome profiling of patients; standardized treatment protocols (folinic acid dosing, betaine, B12); evaluation of newborn-screening biomarkers (homocysteine/methionine + macrocytosis).

### Database provenance (verified during this investigation)
- **Disease/gene identifiers** (MONDO:0060611/CIMAH → OMIM:617780, Orphanet:658813, UMLS:C4540434, GARD:0026001, MedGen:1615364; MTHFD1 HGNC:7432, Ensembl ENSG00000100714, UniProt P11586, 14q23.3) — verified via **EBI OLS4/MONDO** and **MyGene.info**.
- **Common variant R653Q (rs2236225 = GRCh38 14-64442127-G-A)** allele frequencies — verified via **gnomAD v4** (global genome AF 0.386; NFE 0.453 → ~20.5% QQ homozygotes).
- **Pathogenic variant spectrum** (64 P / 30 LP, predominantly splice/frameshift/nonsense; reference NM_005956.4) — verified via **NCBI ClinVar** (E-utilities).
- **Evidence tiers:** human clinical = case reports/series (PMIDs 21813566, 23296427, 25633902, 27707659, 32414565, 42301236); in vitro = patient fibroblast flux/enzymology (25548164, 32414565, 28265077); model organism = Mthfd1 synthetase mouse (23704330, 26408344); genetic-epidemiology = R653Q/NTD association studies (12384833, 16552426, 24977710, 22856873, 19130090).

---

### Key References (PMID)
- 21813566 — First identification of MTHFD1 deficiency (exome).
- 23296427 — SCID from MTHFD1; response to B12+folate.
- 25548164 — Impaired nuclear de novo dTMP biosynthesis mechanism.
- 25633902 — Four new patients; folic/folinic acid treatment review.
- 27707659 — Precision diagnosis (incl. structural variant) and immune reconstitution.
- 32412981 — Review: immunodeficiency in inborn errors of B12/folate.
- 32414565 — Biochemical characterization (protein/activity) in patients.
- 42301236 — Two children (p.Arg173Cys); folate therapy and outcomes.
- 23704330 / 26408344 — Mthfd1 synthetase mouse models (R653Q); purine synthesis, NTD/CHD.
- 28265077 — Arsenic targets MTHFD1/SUMO-dependent nuclear dTMP synthesis.
- 12384833 — R653Q as maternal NTD risk factor (original, OR 1.52).
- 16552426 — Independent replication of maternal NTD risk (OR 1.49).
- 24977710 — Meta-analysis of MTHFD1 G1958A and NTD risk (9 studies).
- 22856873 — Candidate-gene screen confirming MTHFD1 R653Q among top NTD signals; NTD ~1/1000.
- 19130090 — MTHFD1 promoter variant (rs1076991) modifies NTD risk with R653Q.


## Artifacts

- [OpenScientist final report](MTHFD1_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](MTHFD1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.
