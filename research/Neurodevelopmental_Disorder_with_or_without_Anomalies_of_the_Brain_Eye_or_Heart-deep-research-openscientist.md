---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-18T15:07:59.855827'
end_time: '2026-08-18T15:21:24.311802'
duration_seconds: 804.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with or without Anomalies of the Brain,
    Eye, or Heart
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 12
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_with_or_without_Anomalies_of_the_Brain_Eye_or_Heart-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_with_or_without_Anomalies_of_the_Brain_Eye_or_Heart-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with or without Anomalies of the Brain, Eye, or Heart
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with or without Anomalies of the Brain, Eye, or Heart** covering all of the
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

# Neurodevelopmental Disorder with or without Anomalies of the Brain, Eye, or Heart (NEDBEH): A Comprehensive Disease Characteristics Report

**Disease:** Neurodevelopmental Disorder with or without Anomalies of the Brain, Eye, or Heart (NEDBEH)
**OMIM:** #616975 · **MONDO:** MONDO:0014744 · **Gene:** *RERE* (1p36.23) · **Category:** Mendelian, autosomal dominant

*Evidence base: aggregated human clinical case series plus zebrafish, mouse, and in-vitro functional studies. All content is literature-derived (no primary patient dataset was provided).*

---

## Summary

Neurodevelopmental Disorder with or without Anomalies of the Brain, Eye, or Heart (NEDBEH), also called RERE-related disorder, is an ultra-rare autosomal-dominant Mendelian condition caused by heterozygous pathogenic variants in *RERE* (arginine-glutamic acid dipeptide repeats gene), which encodes the nuclear receptor coregulator Atrophin-2. Most disease-causing variants arise *de novo*. The gene lies within the proximal 1p36 critical region, and the NEDBEH phenotype substantially overlaps that of the far more common 1p36 deletion syndrome (~1 in 5,000 newborns). Affected individuals near-universally show developmental delay, intellectual disability, and/or autism spectrum disorder, accompanied by a variable spectrum of structural anomalies of the brain, eye, heart, kidney, ear, and palate ([PMID: 27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/)).

Mechanistically, RERE/Atrophin-2 is a widely expressed nuclear receptor coregulator that positively regulates retinoic acid (RA) signaling through the chromatin-associated WHHERE complex (WDR5, HDAC1, HDAC2, RERE) together with the histone methyltransferase EHMT2/G9a, and it also modulates Sonic hedgehog (Shh) signaling. NEDBEH-associated variants behave as hypomorphs in repressing shh signaling, and a genotype–phenotype axis has emerged: loss-of-function (haploinsufficiency) variants cause milder, sometimes-inherited disease with fewer multisystem anomalies, whereas missense variants and in-frame duplications affecting the histidine-rich region (HRR) of the Atrophin-1 domain produce more severe multisystem phenotypes—including a CHARGE-syndrome-like presentation—and appear to act by a gain-of-function or dominant-negative mechanism ([PMID: 29330883](https://pubmed.ncbi.nlm.nih.gov/29330883/); [PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/)).

Diagnosis is molecular—via whole-exome/whole-genome sequencing, multigene neurodevelopmental panels, or chromosomal microarray—with no biochemical biomarker or newborn screening test. Fewer than ~60 individuals have been reported worldwide. There is no disease-specific or curative therapy; management is supportive, multidisciplinary, and increasingly variant-specific, guided by genetic counseling. Animal models (RERE-deficient zebrafish and mice) faithfully recapitulate key features, and Shh pathway inhibition (HPI-1) rescues coloboma in zebrafish—identifying a preclinical therapeutic lead ([PMID: 36576487](https://pubmed.ncbi.nlm.nih.gov/36576487/)).

---

## 1. Disease Information

**Overview.** NEDBEH is a Mendelian neurodevelopmental disorder defined by a near-constant core of developmental delay (DD), intellectual disability (ID), and/or autism spectrum disorder (ASD), plus a variable constellation of congenital anomalies affecting the brain, eye, and heart (as well as kidney, ear, and palate). It was first delineated by Fregeau et al. (2016), who described ten individuals carrying rare, putatively damaging *RERE* variants and noted that the associated defect spectrum overlaps that of proximal 1p36 deletions: *"In this report, we describe ten individuals with intellectual disability, developmental delay, and/or autism spectrum disorder who carry rare and putatively damaging changes in RERE"* ([PMID: 27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/)).

**Key identifiers:**
- **OMIM:** #616975 (Neurodevelopmental disorder with or without anomalies of the brain, eye, or heart)
- **MONDO:** MONDO:0014744
- **Gene:** *RERE*, HGNC:9965, chromosome 1p36.23
- **ICD-11:** neurodevelopmental disorder categories (no NEDBEH-specific code); related monosomy 1p36 is separately coded
- **MeSH:** No dedicated descriptor; indexed under intellectual disability / developmental disabilities

**Synonyms / alternative names:** RERE-related disorder(s); RERE syndrome; NEDBEH.

**Information source.** Knowledge is derived predominantly from aggregated disease-level resources (OMIM, published cohort series) and individual case reports, not from large EHR datasets. The largest assembled series to date comprises 54 individuals ([PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/)).

---

## 2. Etiology

**Primary cause — genetic.** NEDBEH is caused by heterozygous pathogenic variants in *RERE*. In the founding cohort, *"In all cases in which both parental DNA samples were available, these changes were found to be de novo"* ([PMID: 27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/)). *RERE* lies in the proximal 1p36 critical region; large 1p36 deletions encompassing *RERE* cause an overlapping multisystem phenotype.

**Genetic risk factors.** The disease is monogenic: the causal factor is a pathogenic *RERE* variant. Variant class is the principal modifier of risk for multisystem involvement—HRR missense and in-frame HRR duplications confer higher risk of structural eye defects, congenital heart defects, renal anomalies, and sensorineural hearing loss than loss-of-function variants ([PMID: 29330883](https://pubmed.ncbi.nlm.nih.gov/29330883/)).

**Environmental risk / protective factors.** No environmental, lifestyle, occupational, or infectious risk or protective factors have been established for this monogenic disorder. Because RERE is a coregulator of retinoic acid signaling, retinoic-acid biology is mechanistically central, but no dietary or exposure-based modifier has been validated in patients.

**Gene–environment interactions.** None established. The disorder is defined by its genetic etiology; the "environment" of relevance is the developmental/signaling milieu (RA and Shh gradients) rather than external exposures.

---

## 3. Phenotypes

The core phenotype—developmental delay, intellectual disability, and/or autism spectrum disorder—is present across essentially all variant groups: *"Developmental delay, intellectual disability, and/or autism spectrum disorder were prevalent across all groups"* ([PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/)). Recurrent associated features reported by Fregeau et al. included *"hypotonia, seizures, behavioral problems, structural CNS anomalies, ophthalmologic anomalies, congenital heart defects, and genitourinary abnormalities"* ([PMID: 27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/)).

| Phenotype | Type | Approx. frequency | Onset | Suggested HPO term |
|---|---|---|---|---|
| Developmental delay | Neurodevelopmental | Near-universal | Infancy/congenital | HP:0001263 |
| Intellectual disability | Neurodevelopmental | Very frequent | Childhood | HP:0001249 |
| Autism spectrum disorder | Behavioral | Frequent | Childhood | HP:0000717 |
| Hypotonia | Clinical sign | Frequent | Neonatal/infancy | HP:0001252 |
| Seizures | Clinical sign | Common | Childhood | HP:0001250 |
| Structural CNS anomalies | Physical | Common | Congenital | HP:0002011 |
| Ophthalmologic anomalies (coloboma, optic atrophy, refractive error) | Physical | ~1/3 | Congenital | HP:0000478 / HP:0000589 / HP:0000648 |
| Congenital heart defect (e.g., VSD) | Physical | Common (enriched in HRR missense) | Congenital | HP:0001627 / HP:0001629 |
| Renal/genitourinary anomalies | Physical | Variable | Congenital | HP:0000119 |
| Sensorineural hearing loss | Clinical sign | Variable (enriched in HRR missense) | Congenital/childhood | HP:0000407 |
| Cleft palate/lip (orofacial clefting) | Physical | Variable | Congenital | HP:0000175 |
| Chiari type I malformation | Physical | Rare (single case) | Congenital | HP:0002308 |
| Dysmorphic facial features | Physical | Variable | Congenital | HP:0001999 |

**Phenotype characteristics.** Onset is congenital/early-childhood. Severity is variable and stratified by variant class: HRR missense/in-frame duplications produce more severe, multisystem disease, while loss-of-function variants are milder and can even be inherited from a mildly-symptomatic or asymptomatic parent ([PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/)). The neurodevelopmental phenotype is generally **non-progressive/stable**; a Chiari-I case reported progressive spasticity but is exceptional ([PMID: 41669386](https://pubmed.ncbi.nlm.nih.gov/41669386/)).

**Quality of life.** Not formally quantified with EQ-5D/SF-36 in published cohorts. Impact derives from lifelong ID/DD (education, independent living), ASD-related behavioral needs, seizure burden, and the surgical/medical needs of congenital anomalies.

---

## 4. Genetic / Molecular Information

**Causal gene.** *RERE* (arginine-glutamic acid dipeptide repeats; Atrophin-2), HGNC:9965, chromosome **1p36.23**. RERE is *"a widely-expressed nuclear receptor coregulator that positively regulates retinoic acid signaling"* ([PMID: 27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/)).

**Pathogenic variants.**
- **Variant types:** missense (notably within the Atrophin-1 domain / histidine-rich region), in-frame duplications (a recurrent two-amino-acid duplication), and loss-of-function alleles (nonsense, frameshift, splice, whole-gene deletion via 1p36 loss).
- **Classification:** pathogenic / likely pathogenic per ACMG/AMP; the 54-individual cohort also included variants of uncertain significance ([PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/)).
- **Origin:** germline; usually **de novo**, but inherited variants exist—the first inherited variant was reported in a patient and his mildly affected mother ([PMID: 36053530](https://pubmed.ncbi.nlm.nih.gov/36053530/)).
- **Functional consequence:** Two mechanisms. Loss-of-function → **haploinsufficiency**. HRR missense variants are structurally stabilizing: *"HRR missense variants were structurally stabilizing, suggesting a gain-of-function or dominant-negative mechanism"* ([PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/)).

**Genotype–phenotype correlation (central molecular finding).** *"Point mutations affecting the Atrophin-1 domain of RERE are associated with an increased risk of structural eye defects, congenital heart defects, renal anomalies, and sensorineural hearing loss when compared with loss-of-function variants that are likely to lead to haploinsufficiency"*, and *"We have also identified a recurrent two-amino-acid duplication in this region that is associated with the development of a CHARGE syndrome-like phenotype"* ([PMID: 29330883](https://pubmed.ncbi.nlm.nih.gov/29330883/)). The 2026 cohort confirmed that *"Loss-of-function variants are associated with fewer multisystem anomalies than missense variants and are more likely to be inherited from a mildly symptomatic or asymptomatic parent"* ([PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/)).

**Convergent HX/HRR motif biology.** The histidine-rich (HX-repeat) motif is shared across non-homologous genes: disruption of the analogous HX-repeat motif in *ATN1* (Atrophin-1) causes CHEDDA (congenital hypotonia, epilepsy, developmental delay, digit abnormalities), a recognizable non-progressive neurocognitive syndrome distinct from polyglutamine DRPLA. The authors note *"non-homologous human genes containing similar motifs... including RERE, where disruptive variants in this motif have also been linked to a separate condition"*—reinforcing that perturbation of the HX motif itself is pathogenic ([PMID: 30827498](https://pubmed.ncbi.nlm.nih.gov/30827498/)).

**Modifier genes.** In 1p36 deletion syndrome, co-deleted genes modify severity (e.g., *KCNAB2*, *CHD5* for neurodevelopmental prognosis; *PRDM16*, *PRKCZ*, and *RERE* implicated in cardiac complications) ([PMID: 25172301](https://pubmed.ncbi.nlm.nih.gov/25172301/)). For isolated *RERE* variants, variant class (LoF vs HRR missense) is the dominant modifier.

**Epigenetic dimension.** RERE functions within chromatin-modifying complexes (with HDAC1/HDAC2 and the H3K9 methyltransferase EHMT2/G9a), placing NEDBEH among disorders of epigenetic regulation of development ([PMID: 28959017](https://pubmed.ncbi.nlm.nih.gov/28959017/); [PMID: 29300383](https://pubmed.ncbi.nlm.nih.gov/29300383/)).

**Chromosomal abnormalities.** Proximal 1p36 deletions that encompass *RERE* produce an overlapping multisystem phenotype and are detected by chromosomal microarray/FISH ([PMID: 27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/); [PMID: 25172301](https://pubmed.ncbi.nlm.nih.gov/25172301/)).

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributors are established for NEDBEH. It is a monogenic developmental disorder. The mechanistically relevant "chemical" context is endogenous **retinoic acid** (CHEBI:26536) signaling, which RERE coregulates, and **Sonic hedgehog** pathway output—not exogenous exposures. No toxin, radiation, occupational, dietary, or pathogen association has been reported.

---

## 6. Mechanism / Pathophysiology

### Molecular pathways
RERE/Atrophin-2 is a nuclear receptor coregulator of **retinoic acid (RA) signaling**. Vilhais-Neto et al. identified the **WHHERE complex** as required for RA-dependent regulation of embryonic bilateral symmetry: *"we identify a protein complex, containing Wdr5, Hdac1, Hdac2 and Rere (named WHHERE), which regulates RA signaling and controls embryonic symmetry"*, and *"Upon RA treatment, WHHERE and Ehmt2 become enriched at RA target genes to promote RNA polymerase II recruitment"* ([PMID: 28959017](https://pubmed.ncbi.nlm.nih.gov/28959017/)). RERE additionally regulates **Sonic hedgehog (Shh)** signaling; NEDBEH-associated variants *"function as hypomorphs in their ability to repress shh signaling and some exhibit abnormal nuclear localization"* ([PMID: 36576487](https://pubmed.ncbi.nlm.nih.gov/36576487/)).

### Organ-specific causal chains
- **Eye (coloboma / optic atrophy).** *"RERE deficiency causes progressive loss of retinal cells and apoptosis of retinal cells in the ganglion cell layer as early as E17.5"*, producing retinal and optic-nerve atrophy ([PMID: 33742727](https://pubmed.ncbi.nlm.nih.gov/33742727/)). In zebrafish, coloboma arises from optic-fissure closure defects driven by deregulated shh signaling, and *"Inhibiting shh signaling by the protein inhibitor HPI-1 rescues coloboma"* ([PMID: 36576487](https://pubmed.ncbi.nlm.nih.gov/36576487/)).
- **Heart (ventricular septal defect).** *"RERE deficiency leads to decreased expression of GATA4 and the development of ventricular septal defects"* ([PMID: 30061196](https://pubmed.ncbi.nlm.nih.gov/30061196/)).
- **Palate (orofacial clefting).** *"ablation of Rere in cranial neural crest (CNC) cells, mediated by a Wnt1-Cre, leads to delayed elevation of the palatal shelves and cleft palate"* ([PMID: 33772547](https://pubmed.ncbi.nlm.nih.gov/33772547/)).
- **Brain/behavior.** Broadly expressed RERE and its role in RA-dependent neurodevelopment underlie the near-universal DD/ID/ASD; specific structural CNS anomalies and (rarely) Chiari I are reported ([PMID: 27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/); [PMID: 41669386](https://pubmed.ncbi.nlm.nih.gov/41669386/)).

### Upstream → downstream logic
```
RERE pathogenic variant (LoF haploinsufficiency  OR  HRR missense GoF/dominant-negative)
        │
        ▼
Altered RERE coregulator activity within chromatin complexes (WHHERE: WDR5/HDAC1/HDAC2 + EHMT2/G9a)
        │
        ├──► Impaired retinoic-acid target-gene transcription (RNA Pol II recruitment)
        └──► Deregulated Sonic hedgehog signaling (hypomorphic repression)
        │
        ▼  (tissue-specific developmental programs disrupted)
Retinal ganglion cell apoptosis ──► optic/retinal atrophy, coloboma (eye)
Reduced GATA4 ─────────────────────► ventricular septal defect (heart)
Cranial neural crest proliferation defect ──► cleft palate
Disrupted neurodevelopment ────────► DD / ID / ASD, seizures, hypotonia
```

### Cellular processes, GO / CL / cell-type terms
- **Biological processes (GO):** retinoic acid receptor signaling pathway (GO:0048384); smoothened/Shh signaling (GO:0007224); regulation of transcription by RNA polymerase II (GO:0006357); histone modification (GO:0016570); apoptotic process (GO:0006915); neural crest cell development (GO:0014032); heart development (GO:0007507); camera-type eye development (GO:0043010).
- **Cellular component (GO):** nucleus (GO:0005634); nuclear body (GO:0016604) — consistent with abnormal nuclear localization of some variants.
- **Cell types (CL):** retinal ganglion cell (CL:0000740); cranial neural crest cell (CL:0000333); cardiac myocyte / cardiac neural crest derivatives (CL:0000746).

### Metabolic, immune, biochemical
No specific metabolic derangement, enzyme deficiency, or immune/autoimmune involvement is described. The biochemical defect is dysregulated **transcriptional coregulation** (RA/Shh), not a metabolic block.

### Molecular profiling
No large-scale patient transcriptomic/proteomic/metabolomic datasets are published for NEDBEH. Mechanistic evidence is primarily from mouse and zebrafish models and cell-based assays (e.g., GATA4 downregulation; shh-reporter hypomorphism).

---

## 7. Anatomical Structures Affected

- **Organ level.** Primary: **brain/CNS** (UBERON:0000955), **eye** (UBERON:0000970; retina UBERON:0000966; optic nerve UBERON:0000941), **heart** (UBERON:0000948; interventricular septum UBERON:0002094). Secondary/variable: **kidney/genitourinary** (UBERON:0002113), **ear** (inner ear UBERON:0001846), **palate** (UBERON:0001716).
- **Body systems:** nervous, visual, cardiovascular, renal/genitourinary, auditory, craniofacial/skeletal.
- **Tissue/cell level.** Nervous tissue (neurons; retinal ganglion cells CL:0000740), cardiac muscle, and **cranial neural crest**–derived mesenchyme (CL:0000333).
- **Subcellular level.** Nucleus (GO:0005634); some variants show abnormal nuclear localization ([PMID: 36576487](https://pubmed.ncbi.nlm.nih.gov/36576487/)).
- **Localization / lateralization.** Anomalies are generally bilateral/midline (septal, palatal, optic fissure) reflecting disrupted developmental symmetry; RERE's WHHERE role in bilateral symmetry is notable ([PMID: 28959017](https://pubmed.ncbi.nlm.nih.gov/28959017/)).

---

## 8. Temporal Development

- **Onset:** congenital / early infancy. Structural anomalies are present at birth; DD/ID/ASD manifest in infancy–early childhood. Prenatal detection of associated malformations is possible (as in 1p36 deletion, where ventriculomegaly, cardiac defects, and dysmorphism prompt evaluation) ([PMID: 31172545](https://pubmed.ncbi.nlm.nih.gov/31172545/)).
- **Course:** the neurodevelopmental phenotype is generally **stable / non-progressive**, paralleling the "non-progressive neurocognitive syndrome" of the related ATN1/CHEDDA HX-motif disorder ([PMID: 30827498](https://pubmed.ncbi.nlm.nih.gov/30827498/)). Rare progressive features (spasticity with Chiari I) are exceptional ([PMID: 41669386](https://pubmed.ncbi.nlm.nih.gov/41669386/)).
- **Duration:** chronic, lifelong.
- **Critical periods:** embryonic organogenesis (retinal/optic-fissure closure, cardiac septation, palatal-shelf elevation, neurulation)—the windows during which RA/Shh dysregulation produces structural anomalies. This makes prenatal/perinatal windows the theoretical target for any future disease-modifying intervention.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant. Variants are usually **de novo**; inherited transmission from a mildly-affected parent occurs, particularly for loss-of-function alleles ([PMID: 27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/); [PMID: 36053530](https://pubmed.ncbi.nlm.nih.gov/36053530/); [PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/)).
- **Penetrance / expressivity:** highly **variable expressivity**; incomplete penetrance is suggested by mildly-symptomatic/asymptomatic parents carrying LoF variants.
- **Epidemiology:** **ultra-rare**. Fewer than ~60 individuals are reported worldwide (10 in 2016; 23 by the 2022 review; 54 in the 2026 cohort including 30 previously unreported: *"We assembled a cohort of 54 individuals with heterozygous pathogenic, likely pathogenic, and variants of uncertain significance in RERE, including 30 previously unreported cases"*). No formal prevalence/incidence has been established. As an anchor, *"Deletions of chromosome 1p36 affect approximately 1 in 5,000 newborns and are associated with developmental delay, intellectual disability, and defects involving the brain, eye, ear, heart, and kidney"* ([PMID: 27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/); [PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/)).
- **Sex ratio / demographics:** no clear sex skew; cases span both sexes and diverse populations. No founder effect or consanguinity requirement (dominant, usually de novo). EHR studies suggest related rare conditions like 1p36 deletion may be underdiagnosed ([PMID: 39148290](https://pubmed.ncbi.nlm.nih.gov/39148290/)).

---

## 10. Diagnostics

**Diagnosis is molecular.** RERE variants are detected by **whole-exome sequencing (WES)**, **whole-genome sequencing (WGS)**, multigene neurodevelopmental/congenital-anomaly **panels**, or **chromosomal microarray (CMA)** (for 1p36 deletions encompassing *RERE*; FISH/karyotype for larger rearrangements) ([PMID: 27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/); [PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/)).

**No biomarker / no newborn screen.** There is no biochemical or metabolic biomarker and no newborn screening test.

**Supporting clinical work-up (phenotype-driven):** brain MRI (structural CNS anomalies, Chiari I), ophthalmologic exam (coloboma, optic atrophy, refractive error), echocardiography (VSD/other CHD), renal ultrasound, audiologic assessment, and EEG for seizures.

**Differential diagnosis and CHARGE overlap.** In a WES study of 28 CHARGE-suggestive families, 53.6% had *CHD7* variants while *"4 (14.3%) individuals had pathogenic variants in other genes (RERE, KMT2D, EP300, or PUF60)"*, and the authors concluded these *"implicate a shared molecular pathology that disrupts epigenetic regulation of multiple-organ development"* ([PMID: 29300383](https://pubmed.ncbi.nlm.nih.gov/29300383/)). Accordingly, *"Consideration should also be given to screening for RERE variants in individuals who fulfill diagnostic criteria for CHARGE syndrome but do not carry pathogenic variants in CHD7"* ([PMID: 29330883](https://pubmed.ncbi.nlm.nih.gov/29330883/)). Other differentials: 1p36 deletion syndrome, CHEDDA (*ATN1*), and other chromatin-regulator neurodevelopmental syndromes.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival statistics. Life-limiting risk derives mainly from **severe congenital heart defects** when present; the neurodevelopmental core is not itself lethal.
- **Morbidity/disability:** Lifelong intellectual disability/developmental delay and ASD-related functional impairment dominate morbidity, with additional burden from epilepsy, vision/hearing deficits, and the surgical needs of structural anomalies.
- **Disease course:** generally **stable/non-progressive** neurodevelopment; chronic lifelong condition.
- **Prognostic factors:** **variant class is the key prognostic axis**—HRR missense/in-frame duplications predict more severe, multisystem disease; LoF variants predict milder outcomes ([PMID: 29330883](https://pubmed.ncbi.nlm.nih.gov/29330883/); [PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/)). Presence and severity of CHD is the main determinant of early-life risk.
- **QoL measures:** not formally applied in published cohorts.

---

## 12. Treatment

**No disease-specific or curative therapy exists.** Management is supportive, multidisciplinary, and increasingly **variant-specific**: the 2026 cohort's findings *"expand the clinical spectrum of RERE-related disorders, refine genotype-phenotype correlations, and support variant-specific"* management ([PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/)).

| Domain | Intervention | Suggested NCIT |
|---|---|---|
| Developmental | Early-intervention, physical/occupational/speech therapy | Rehabilitation Therapy (NCIT:C15917) |
| Epilepsy | Anti-seizure medications | Anticonvulsant Agent (NCIT:C264) |
| Cardiac | Surgical repair of VSD/CHD | Cardiac Surgery (NCIT:C51648) |
| Orofacial | Cleft palate/lip repair | Cleft Palate Repair procedure |
| Ophthalmologic | Refractive correction, coloboma/optic-atrophy management | Ophthalmologic procedures |
| Audiologic | Hearing amplification/management of SNHL | Hearing Aid (NCIT:C50071) |
| Genitourinary | Management of renal/GU anomalies | Urologic procedures |
| Behavioral/psychiatric | ASD/ADHD supports; symptom-directed pharmacotherapy | Behavioral therapy; stimulants |

**Precedent from 1p36 comorbidity management:** off-label melatonin (insomnia) and methylphenidate (ADHD) were effective without adverse effects in a 1p36 deletion case, illustrating symptom-directed pharmacotherapy relevant to overlapping neurobehavioral features ([PMID: 34831818](https://pubmed.ncbi.nlm.nih.gov/34831818/)).

**Experimental / preclinical lead.** In zebrafish, the Shh inhibitor **HPI-1 rescues coloboma**, nominating Shh-pathway modulation as a candidate therapeutic direction ([PMID: 36576487](https://pubmed.ncbi.nlm.nih.gov/36576487/)). No human clinical trials of targeted therapy exist. No pharmacogenomic guidance is established.

---

## 13. Prevention

- **Primary prevention:** none possible (usually de novo genetic disorder).
- **Secondary prevention / early detection:** phenotype-driven surveillance stratified by variant class—regular ophthalmologic, cardiac, audiologic, renal, and neurodevelopmental evaluation; brain imaging as indicated.
- **Genetic screening / counseling:** **genetic counseling** is central. Recurrence risk is low for confirmed de novo variants (with residual risk from germline mosaicism) but up to 50% for an affected transmitting parent; prenatal/preimplantation testing is feasible once a familial variant is known. Cascade testing of parents clarifies inheritance and recurrence risk ([PMID: 41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/); [PMID: 36053530](https://pubmed.ncbi.nlm.nih.gov/36053530/)).
- **Prenatal considerations:** as with 1p36 deletion, ultrasound findings (ventriculomegaly, cardiac defect, dysmorphism) may prompt CMA/sequencing ([PMID: 31172545](https://pubmed.ncbi.nlm.nih.gov/31172545/)).
- **Immunization / public health / prophylaxis:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *RERE* is highly conserved. Mouse *Rere/Atrophin-2* (*Mus musculus*, NCBI Taxon 10090); zebrafish paralogs *rerea* and *rereb* (*Danio rerio*, NCBI Taxon 7955). The zebrafish *rerea* mutant is named **babyface**.
- **Natural disease in other species:** No spontaneous companion-animal or wildlife NEDBEH-equivalent is catalogued (e.g., no established OMIA entry). Disease knowledge derives from engineered models rather than naturally occurring animal disease.
- **Comparative biology:** RA/Shh developmental roles and the RERE HX-repeat motif are evolutionarily conserved; the convergent human *ATN1* HX-motif disorder (CHEDDA) illustrates conserved motif-level pathogenicity ([PMID: 30827498](https://pubmed.ncbi.nlm.nih.gov/30827498/)).
- **Transmission / zoonosis:** not applicable.

---

## 15. Model Organisms

**Zebrafish (*Danio rerio*).** The *rerea* mutant (**babyface**) *"robustly recapitulates optic fissure closure defects resulting from loss of RERE function, as observed in humans"*; coloboma results from expansion of the proximal optic stalk and reduced ventral retinal fate, and is rescued by the Shh inhibitor HPI-1 ([PMID: 36576487](https://pubmed.ncbi.nlm.nih.gov/36576487/)). This model is powerful for eye phenotypes and for drug-rescue screening.

**Mouse (*Mus musculus*).** RERE-deficient and conditional mice recapitulate multiple organ-specific features:
- Retinal/optic-nerve atrophy via retinal ganglion cell apoptosis from E17.5 ([PMID: 33742727](https://pubmed.ncbi.nlm.nih.gov/33742727/));
- Ventricular septal defects via reduced GATA4 ([PMID: 30061196](https://pubmed.ncbi.nlm.nih.gov/30061196/));
- Cleft palate via cranial-neural-crest-specific ablation (Wnt1-Cre) ([PMID: 33772547](https://pubmed.ncbi.nlm.nih.gov/33772547/)).
- *Wdr5* and *Hdac1* mutant mice phenocopy RA-deficient asymmetric somite formation, validating the WHHERE complex mechanism ([PMID: 28959017](https://pubmed.ncbi.nlm.nih.gov/28959017/)).

**Genetic model types available:** knockout, hypomorphic, and conditional (Cre-lox, e.g., Wnt1-Cre) mouse lines; zebrafish mutants.

**Recapitulation & limitations.** Models faithfully reproduce eye, heart, and palate anomalies and confirm the RA/Shh mechanism. Limitations: the human neurodevelopmental/behavioral phenotype (ID/ASD) is harder to model faithfully; models often assess loss-of-function, whereas HRR missense gain-of-function/dominant-negative biology is less fully modeled in vivo.

**Resources:** MGI (mouse), ZFIN (zebrafish).

---

## Mechanistic Model / Interpretation

NEDBEH is best understood as a **transcriptional-coregulator developmental disorder** with a two-mechanism genetic architecture converging on RA and Shh dysregulation:

```
                    ┌───────────────────────────────────────┐
                    │            RERE variant                 │
                    └───────────────┬─────────────────────────┘
             ┌──────────────────────┴───────────────────────┐
   Loss-of-function (LoF)                        HRR missense / in-frame dup
   → haploinsufficiency                          → structurally stabilizing
   milder, often inherited                       → gain-of-function / dominant-neg
   fewer multisystem anomalies                   more multisystem; CHARGE-like
             └──────────────────────┬───────────────────────┘
                                    ▼
        Abnormal chromatin coregulation (WHHERE: WDR5/HDAC1/HDAC2 + EHMT2/G9a)
                                    ▼
        ┌─────────────► ↓ Retinoic-acid target transcription
        └─────────────► deregulated Sonic hedgehog signaling
                                    ▼
   ┌──────────────┬──────────────┬──────────────┬──────────────┐
  Eye            Heart          Palate         Brain          Ear/Kidney
  RGC apoptosis  ↓GATA4→VSD      CNC defect     DD/ID/ASD,     variable
  coloboma       septation       cleft palate   seizures       anomalies
  (Shh-rescuable)
```

The variant-class axis is clinically actionable: it stratifies surveillance intensity and recurrence-risk counseling. The shared HX/HRR-motif biology across *RERE* and *ATN1* points to a broader class of "HX-motif perturbation" Mendelian syndromes. The Shh-inhibitor rescue in zebrafish is the single most promising translational lead.

---

## Evidence Base

| PMID | Study | Contribution |
|---|---|---|
| [27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/) | Fregeau 2016 (n=10) | Defined the syndrome; de novo RERE variants; RA coregulator; 1p36 overlap |
| [29330883](https://pubmed.ncbi.nlm.nih.gov/29330883/) | Jordan 2018 (n=9) | Core genotype–phenotype correlation; CHARGE-like HRR duplication; RERE testing in CHD7-negative CHARGE |
| [41988794](https://pubmed.ncbi.nlm.nih.gov/41988794/) | Curtis 2026 (n=54) | Largest cohort; LoF vs HRR biology; HRR missense stabilizing (GoF/dominant-neg); variant-specific management |
| [28959017](https://pubmed.ncbi.nlm.nih.gov/28959017/) | Vilhais-Neto 2017 | WHHERE complex; RA-dependent symmetry; Pol II recruitment |
| [36576487](https://pubmed.ncbi.nlm.nih.gov/36576487/) | Zebrafish babyface | Coloboma via shh deregulation; HPI-1 rescue (druggable lead) |
| [33742727](https://pubmed.ncbi.nlm.nih.gov/33742727/) | Mouse eye | RGC apoptosis → retinal/optic atrophy |
| [30061196](https://pubmed.ncbi.nlm.nih.gov/30061196/) | Mouse heart | ↓GATA4 → VSD |
| [33772547](https://pubmed.ncbi.nlm.nih.gov/33772547/) | Mouse palate | Cranial-neural-crest cleft palate mechanism |
| [29300383](https://pubmed.ncbi.nlm.nih.gov/29300383/) | Moccia 2018 | RERE among CHARGE-overlapping chromatin genes; shared epigenetic pathology |
| [30827498](https://pubmed.ncbi.nlm.nih.gov/30827498/) | ATN1/CHEDDA | Convergent HX-motif disorder; non-progressive |
| [36053530](https://pubmed.ncbi.nlm.nih.gov/36053530/) | Case series | First inherited RERE variant; genotype–phenotype |
| [41669386](https://pubmed.ncbi.nlm.nih.gov/41669386/) | Case report | Chiari I; spectrum expansion |
| [25172301](https://pubmed.ncbi.nlm.nih.gov/25172301/) | 1p36 microarray | Modifier genes; RERE and cardiac complications |
| [31172545](https://pubmed.ncbi.nlm.nih.gov/31172545/) | Prenatal 1p36 | Prenatal detection context |
| [39148290](https://pubmed.ncbi.nlm.nih.gov/39148290/) | EHR study | Underdiagnosis of 1p36-related conditions |
| [34831818](https://pubmed.ncbi.nlm.nih.gov/34831818/) | 1p36 psychiatric | Symptom-directed pharmacotherapy precedent |

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity (<60 cases)** limits precise phenotype frequencies, penetrance estimates, and formal prevalence/incidence.
2. **No patient-level omics** (transcriptomics/proteomics/metabolomics) datasets; mechanism rests on model organisms and cell assays.
3. **GoF/dominant-negative mechanism** of HRR missense variants is inferred from structural stabilization; direct in vivo functional proof is incomplete.
4. **Neurodevelopmental phenotype modeling** is weak—models capture structural anomalies better than ID/ASD.
5. **No QoL / natural-history longitudinal data**; survival and life-expectancy figures are unquantified.
6. **Therapeutics** remain entirely supportive; the Shh-inhibitor lead is preclinical (zebrafish, eye only).

---

## Proposed Follow-up Experiments / Actions

1. **International registry & natural-history study** to quantify per-phenotype frequencies, penetrance, and progression by variant class.
2. **Functional validation of HRR missense variants** (knock-in mouse/zebrafish; degron/rescue assays) to confirm gain-of-function/dominant-negative mechanism vs LoF.
3. **Patient-derived iPSC neurons/organoids and cardiac/retinal organoids** for RERE variants to model neurodevelopmental and structural phenotypes and screen RA/Shh modulators.
4. **Preclinical Shh-modulation trials** extending HPI-1 rescue beyond the eye to cardiac/palatal endpoints, defining therapeutic windows.
5. **Chromatin/epigenomic profiling** (CUT&RUN/ChIP-seq for RERE, HDAC1/2, EHMT2; RNA-seq) in variant vs control cells to map dysregulated RA/Shh target genes.
6. **Variant-specific surveillance guideline** formalization and prospective evaluation, with structured genetic-counseling recurrence-risk pathways including germline-mosaicism considerations.


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_with_or_without_Anomalies_of_the_Brain_Eye_or_Heart-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_with_or_without_Anomalies_of_the_Brain_Eye_or_Heart-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.