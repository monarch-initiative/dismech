---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T21:01:14.513415'
end_time: '2026-08-31T21:29:14.867843'
duration_seconds: 1680.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Developmental and Epileptic Encephalopathy 55
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
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 26
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 3
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Developmental_and_Epileptic_Encephalopathy_55-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Developmental_and_Epileptic_Encephalopathy_55-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental and Epileptic Encephalopathy 55
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental and Epileptic Encephalopathy 55** covering all of the
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

# Developmental and Epileptic Encephalopathy 55 (DEE55 / PIGP Deficiency): A Comprehensive Disease Characteristics Report

## Summary

**Developmental and Epileptic Encephalopathy 55 (DEE55; OMIM #617599)** is an ultra-rare, autosomal-recessive **inherited glycosylphosphatidylinositol (GPI) deficiency (IGD)** caused by biallelic loss-of-function variants in **PIGP** (Phosphatidylinositol Glycan Anchor Biosynthesis, Class P; OMIM \*605938; HGNC:3046; formerly *DSCR5*; located at 21q22.13). PIGP encodes an accessory subunit of the endoplasmic-reticulum **GPI-GlcNAc transferase** complex, the enzyme that catalyzes the committed first step of GPI anchor biosynthesis. When PIGP function is reduced, the cell produces fewer GPI anchors, which in turn lowers the cell-surface expression of the ≥150 human GPI-anchored proteins (GPI-APs) that are essential for normal neuronal development and function. The downstream deficit of these surface proteins produces the disease's cardinal triad: **early-onset refractory seizures, muscular hypotonia, and profound global developmental delay / intellectual disability**, typically accompanied by cerebral and cerebellar atrophy on neuroimaging.

The disease was first defined molecularly in 2017 by Johnstone and colleagues in two compound-heterozygous siblings, and remained described in only ~7 patients as of 2023. Since then the recognized phenotypic spectrum has broadened substantially — from the classic DEE presentation, to **Multiple Congenital Anomalies–Hypotonia–Seizures Syndrome (MCAHS)**, and at the most severe end to **prenatal lethality** (a fetus terminated at 17 weeks gestation). Because complete GPI deficiency is embryonic-lethal, all viable patients carry **hypomorphic (partial-loss-of-function) biallelic variants**. A recurrent frameshift allele, **c.456delA (p.Glu153Asnfs\*34)**, has been observed both in compound-heterozygous and homozygous states across unrelated families and is ultra-rare in population databases (≈9 heterozygous carriers, 0 homozygotes in gnomAD).

There is **no curative or disease-modifying therapy**. Management is symptomatic and multidisciplinary — antiseizure medications for the refractory epilepsy, plus supportive care (feeding-tube nutrition, physical/occupational/speech therapy). Empiric nutritional interventions such as **pyridoxine (vitamin B6)** and the **ketogenic diet** are used in the broader GPI-anchor-disorder group. Prognosis is severe, with profound lifelong disability and substantial mortality (≈18% deceased across the largest IGD cohort). Diagnosis is achieved by whole-exome or whole-genome sequencing — notably, targeted epilepsy gene panels can miss PIGP — supported functionally by flow-cytometric detection of reduced GPI-anchored proteins on blood cells.

---

## Key Findings

### Finding 1 — DEE55 is caused by biallelic PIGP variants and is an autosomal-recessive inherited GPI deficiency

The molecular basis of DEE55 was established by **Johnstone et al. 2017** [PMID: 28334793](https://pubmed.ncbi.nlm.nih.gov/28334793/), who reported two siblings with compound-heterozygous variants in PIGP (NM_153681.2: **c.74T>C, p.Met25Thr** and **c.456delA, p.Glu153AsnFs\*34**). As the authors state: *"Here, we report two siblings with compound heterozygous variants in the gene phosphatidylinositol glycan anchor biosynthesis, class P (PIGP) (NM_153681.2: c.74T > C;p.Met25Thr and c.456delA;p.Glu153AsnFs\*34). PIGP encodes a subunit of the enzyme that catalyzes the first step of GPI anchor biosynthesis."*

Functional work confirmed the loss-of-function mechanism: *"Functional studies with patient cells showed reduced PIGP mRNA levels, and an associated reduction of GPI-anchored cell surface proteins, which was rescued by exogenous expression of wild-type PIGP. This work associates mutations in the PIGP gene with a novel autosomal recessive IGD."* The rescue by wild-type PIGP demonstrates that the surface-protein deficit is a direct consequence of PIGP dysfunction, satisfying a key criterion for causality. The disease is thus an **autosomal-recessive Mendelian disorder** within the family of inherited GPI deficiencies (a subgroup of the congenital disorders of glycosylation).

### Finding 2 — Core clinical phenotype: early-onset refractory seizures, hypotonia, and profound developmental delay

Both index PIGP patients *"presented with early-onset refractory seizures, hypotonia, and profound global developmental delay, reminiscent of other IGD phenotypes"* (Johnstone 2017, [PMID: 28334793](https://pubmed.ncbi.nlm.nih.gov/28334793/)). The frequency and character of these features are well quantified in the largest IGD cohort to date, **Sidpra et al. 2024** ([PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/), n = 83), which reported: *"Core clinical features were developmental delay or intellectual disability (DD/ID, 90%), seizures (83%), hypotonia (72%) and motor symptoms (64%)."* Seizure onset is typically in infancy: *"Median age at seizure onset was 6 months."*

Neuroimaging in the IGD group commonly shows cerebral atrophy (75%), cerebellar atrophy (60%), corpus-callosum anomalies (57%), and a distinctive symmetric restricted diffusion of the central tegmental tracts (60%). The OMIM clinical synopsis for DEE55 specifically (per Vetro et al. 2020, curated in OMIM #617599) describes refractory seizures beginning in the first weeks-to-months of life, profound intellectual disability, absent speech, spastic quadriplegia, dyskinetic movements, cortical visual impairment, and feeding-tube dependence, with MRI showing cerebral atrophy, a thin corpus callosum, and abnormal white-matter signal.

**Suggested HPO terms:** Seizure (HP:0001250); Infantile spasms / early-onset epilepsy (HP:0012469 / HP:0011097); Muscular hypotonia (HP:0001252); Global developmental delay (HP:0001263); Profound intellectual disability (HP:0002187); Absent speech (HP:0001344); Spastic tetraplegia (HP:0002510); Cortical visual impairment (HP:0100704); Cerebral atrophy (HP:0002059); Cerebellar atrophy (HP:0001272); Thin corpus callosum (HP:0033725).

### Finding 3 — Phenotypic spectrum extends to MCAHS and prenatal lethality

**Martín-Grau et al. 2023** ([PMID: 37125481](https://pubmed.ncbi.nlm.nih.gov/37125481/)) expanded the PIGP phenotype beyond classic DEE. They described two compound-heterozygous siblings carrying PIGP **NM_153682.3:c.2T>C (p.?)** and a **136-kb deletion at 21q22.13 (GRCh37 chr21:38,329,939–38,466,066)** removing the entire PIGP gene: *"Both were compound heterozygous of pathogenic variants in PIGP gene: NM_153682.3:c.2 T > C(p.?) and a 136 Kb deletion ... affecting the entire PIGP gene."* One child had dysmorphic features, congenital anomalies, hypotonia, and epileptic encephalopathy; the other was *"a fetus with a severe malformation disorder at 17 weeks of gestation whose pregnancy was interrupted."*

The authors emphasized the rarity of the condition — *"To date, the PIGP gene has only been related to Developmental and Epileptic Encephalopathy 55 (MIM#617599) in just seven patients"* — and proposed a nosological expansion: *"Our results extend the clinical phenotype associated to PIGP gene and propose to include it as a novel cause of Multiple Congenital Anomalies-Hypotonia-Seizures syndrome."* This establishes a **severity continuum** from prenatal-lethal malformation through MCAHS to the classic postnatal DEE presentation, consistent with variable expressivity driven by the residual GPI-biosynthetic activity of each allele combination.

### Finding 4 — Mechanism: PIGP is a subunit of the ER GPI-GlcNAc transferase catalyzing the committed first step of GPI biosynthesis

*"PIGP encodes a subunit of the enzyme that catalyzes the first step of GPI anchor biosynthesis"* (Johnstone 2017, [PMID: 28334793](https://pubmed.ncbi.nlm.nih.gov/28334793/)). This first step — transfer of N-acetylglucosamine (GlcNAc) from UDP-GlcNAc to phosphatidylinositol to form GlcNAc-PI on the cytoplasmic face of the ER — is the committed, rate-defining reaction of the entire pathway. Downstream, the GPI anchor is assembled and transferred to hundreds of proteins: *"At least 150 human proteins are glycosylphosphatidylinositol-anchored proteins (GPI-APs)"* (Kinoshita review, [PMID: 32156170](https://pubmed.ncbi.nlm.nih.gov/32156170/); an updated review, [PMID: 39129667](https://pubmed.ncbi.nlm.nih.gov/39129667/), cites ≥160). GPI attachment is required for the cell-surface expression of these proteins.

A critical mechanistic constraint explains why patients survive at all: *"Patients with IGD have only a partial deficiency because complete GPI deficiency causes embryonic death"* (Murakami & Kinoshita 2015, [PMID: 25803904](https://pubmed.ncbi.nlm.nih.gov/25803904/)). Thus all DEE55 alleles must be **hypomorphic** rather than null on both copies; the degree of residual activity, together with which step of the pathway is impaired, tunes disease severity.

**Suggested GO terms:** GPI anchor biosynthetic process (GO:0006506); N-acetylglucosaminyltransferase activity (GO:0016262/related); attachment of GPI anchor to protein (GO:0016255); endoplasmic reticulum membrane (GO:0005789).

### Finding 5 — PIGP is one of seven components of the GPI-GlcNAc transferase complex

Martín-Grau 2023 ([PMID: 37125481](https://pubmed.ncbi.nlm.nih.gov/37125481/)) situates PIGP within its multi-subunit enzyme: *"the initial stage of their biosynthesis is mediated by PIGA, PIGC, PIGH, PIGP, PIGQ, PIGY, and DMP2 genes, which have been linked to a wide spectrum of phenotypes depending on the gene damaged."* PIGA is the catalytic subunit, while PIGP is an accessory/regulatory subunit (DPM2/DMP2 is shared with the dolichol-phosphate-mannose synthase machinery). Defects in the different subunits produce overlapping yet gene-specific IGD phenotypes; PIGA-, PIGQ-, and PIGY-related disorders overlap clinically with PIGP-related MCAHS. This complex-level view explains the phenotypic convergence of the whole GPI-GnT subgroup on neurodevelopmental epileptic encephalopathy.

### Finding 6 — Recurrent c.456delA allele; ultra-rare in population databases; standard epilepsy panels can miss PIGP

**Krenn et al. 2019** ([PMID: 31139695](https://pubmed.ncbi.nlm.nih.gov/31139695/); *Ann Clin Transl Neurol* 6(5):968–973) described a second, independent family: a 2-year-old girl of unrelated Polish parents who was **homozygous for PIGP c.456delA (p.Glu153Asnfs\*34)** — the very same frameshift allele carried in compound-heterozygous state by the original Johnstone siblings. This makes c.456delA a **recurrent loss-of-function allele** across the small known patient population. The variant is ultra-rare: 6 heterozygotes and no homozygotes in an in-house 16,000-exome database, and 9 heterozygous / 0 homozygous carriers in gnomAD.

Two diagnostic lessons emerge. First, **whole-exome sequencing was required**: a 100-gene epileptic-encephalopathy panel (which included other PIG genes — PIGA, PIGG, PIGN, PIGT — but not PIGP) failed to detect the diagnosis. Second, **flow cytometry of patient lymphocytes showed decreased surface GPI-anchored proteins**, providing functional confirmation. GeneMatcher yielded no additional families at the time, underscoring the disease's extreme rarity.

### Finding 7 — Diagnostic approach: WES/WGS + flow cytometry of GPI-anchored proteins; variable hyperphosphatasia

Diagnosis combines genomic sequencing with a functional cell-surface assay. Murakami & Kinoshita 2015 ([PMID: 25803904](https://pubmed.ncbi.nlm.nih.gov/25803904/)) note that *"Flow cytometric analysis of GPI-APs on granulocytes is also useful for the detection of IGD"* and that *"The presence of hyperphosphatasia is strong evidence of IGD."* Importantly, hyperphosphatasia (elevated tissue-nonspecific alkaline phosphatase, a GPI-anchored protein) is chiefly associated with **late-pathway** defects (e.g., Mabry syndrome / hyperphosphatasia-with-mental-retardation from PIGV/PIGO/PGAP defects) and is **not a consistent feature of PIGP**, an early-pathway defect. Multicolor flow cytometry using markers such as FLAER, CD16, CD24, CD55, CD59 (and the T5 antibody for free GPI) yields gene/complex-specific profiles (Knaus 2019, [PMID: 31353022](https://pubmed.ncbi.nlm.nih.gov/31353022/)): *"Using multicolor flow cytometry, we determined a characteristic profile for GPI transamidase deficiency."* In PIGP cases specifically, diagnosis was made by WES (PMID 28334793, 31139695) and a whole-gene 136-kb deletion was detectable as a copy-number variant on genomic analysis (PMID 37125481).

### Finding 8 — Treatment is symptomatic; pyridoxine and ketogenic diet are reported supportive options

There is no curative therapy. Management is anticonvulsant-based seizure control plus multidisciplinary supportive care. **Boyer, Johnsen & Morava 2022** ([PMID: 35562242](https://pubmed.ncbi.nlm.nih.gov/35562242/)) reviewed nutritional interventions across the >160 congenital disorders of glycosylation, noting that specific therapies exist for very few subtypes: *"Specific nutritional treatment options for certain CDG types include oral supplementation of monosaccharide sugars, manganese, uridine, or pyridoxine."* They explicitly address the GPI-anchor subgroup: *"We review the dietary management in CDG with a focus on two subgroups: N-linked glycosylation defects and GPI-anchor disorders."* Pyridoxine (vitamin B6) and the ketogenic diet are the empiric interventions most often cited for GPI-anchor disorders, though robust efficacy data specific to PIGP are lacking.

### Finding 9 — Severe prognosis, including prenatal lethality and ≈18% mortality across the IGD group

DEE55 carries a severe prognosis. Only ~7 PIGP patients were reported by 2023 ([PMID: 37125481](https://pubmed.ncbi.nlm.nih.gov/37125481/)), and one allele combination produced fetal termination at 17 weeks. Across the largest IGD cohort (Sidpra 2024, [PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/), n = 83), *"Follow-up data were available for all individuals, 15 of whom were deceased at the time of writing"* (≈18% mortality). Morbidity is multisystemic: *"Sixty-one individuals had multisystem involvement including gastrointestinal (66%), cardiac (19%) and renal (14%) anomalies."* The OMIM synopsis notes death in childhood may occur in DEE55 specifically.

### Finding 10 — Authoritative identifiers

| Resource | Identifier |
|---|---|
| Disease (phenotype) | **OMIM #617599** — Developmental and Epileptic Encephalopathy 55 |
| Orphanet | PIGP-related early infantile epileptic encephalopathy (within Orphanet IGD classifications; ORPHA:1934 grouping) |
| Gene | **PIGP** — OMIM \*605938; **HGNC:3046**; NCBI Gene **51227**; Ensembl **ENSG00000185808**; UniProt **P57054** |
| Locus | **21q22.13** (GRCh38 chr21:37,065,364–37,073,071) — within the Down syndrome critical region |
| Former/alias symbols | **DSCR5** (Down syndrome critical region gene 5); DCRC; DSRC |
| MONDO | Align to the MONDO term for developmental and epileptic encephalopathy 55 (map to OMIM:617599) |

---

## Detailed Section-by-Section Report

### 1. Disease Information
DEE55 is a Mendelian, autosomal-recessive developmental and epileptic encephalopathy — a severe neurodevelopmental disorder in which epileptic activity itself is thought to contribute to developmental impairment, superimposed on the direct developmental effect of the underlying metabolic lesion. It belongs to the **inherited GPI deficiencies (IGDs)**, a subclass of the **congenital disorders of glycosylation (CDG)**. Key identifiers are listed in Finding 10. Synonyms include *PIGP-related developmental and epileptic encephalopathy*, *PIGP-CDG*, *early infantile epileptic encephalopathy 55*, and (given the phenotypic expansion) a cause of *Multiple Congenital Anomalies–Hypotonia–Seizures syndrome*. Information is derived from **aggregated disease-level resources** (OMIM, Orphanet) and a small number of **individual-patient case reports and cohort studies** (Johnstone 2017; Krenn 2019; Martín-Grau 2023; Sidpra 2024) rather than EHR-scale datasets.

### 2. Etiology
**Causal factor:** biallelic (homozygous or compound-heterozygous) loss-of-function variants in **PIGP**. **Genetic risk factors:** the causal variants themselves; a recurrent frameshift allele c.456delA (p.Glu153Asnfs\*34) recurs across families. Because inheritance is autosomal recessive, **consanguinity and being a carrier parent** are the principal risk contexts; the Krenn 2019 family, however, involved unrelated parents homozygous by chance for an ultra-rare allele. **Environmental risk factors:** none identified — this is a monogenic disorder. **Protective factors:** none established; residual PIGP/GPI activity from hypomorphic alleles is "protective" against the embryonic lethality seen with complete deficiency. **Gene–environment interactions:** none documented.

### 3. Phenotypes
See Finding 2 for frequencies and HPO suggestions. The dominant phenotype types are **clinical signs/symptoms** (seizures, hypotonia, spasticity, dyskinesia), **developmental/behavioral** (profound intellectual disability, absent speech), **neuroimaging abnormalities** (cerebral/cerebellar atrophy, thin corpus callosum, white-matter signal change), and, in the MCAHS end of the spectrum, **congenital malformations and dysmorphism**. Onset is **neonatal-to-early-infantile** (seizures median ~6 months in the IGD group; first weeks–months in DEE55). Severity is **profound**; progression is best described as a **static-to-slowly-progressive encephalopathy** with refractory epilepsy. Quality-of-life impact is severe: affected children are typically non-verbal, non-ambulatory, feeding-tube dependent, and fully care-dependent.

### 4. Genetic / Molecular Information
**Causal gene:** PIGP (OMIM \*605938). **Reported pathogenic variants:** c.74T>C (p.Met25Thr, missense); c.456delA (p.Glu153Asnfs\*34, frameshift, recurrent LoF); c.2T>C (p.?, start-loss); and a 136-kb whole-gene deletion (structural/CNV). **Variant classes:** missense, frameshift, start-loss, and whole-gene deletion — all converging on reduced PIGP function. **Functional consequence:** **loss of function** (reduced mRNA and reduced GPI-anchored surface proteins, rescued by wild-type PIGP). **Allele frequency:** c.456delA is ultra-rare (≈9 het / 0 hom in gnomAD). **Origin:** germline. **Modifier genes/epigenetics:** not specifically characterized for PIGP; other GPI-pathway genes provide the phenotypic-modifier context at the pathway level. **Chromosomal abnormalities:** the 136-kb 21q22.13 deletion (PMID 37125481) is the notable structural lesion; PIGP lies in the Down syndrome critical region and has multiple pseudogenes (a technical caveat for sequencing/CNV calling).

### 5. Environmental Information
**Not applicable.** No environmental, lifestyle, or infectious contributors are known; DEE55 is a purely monogenic inborn error of metabolism.

### 6. Mechanism / Pathophysiology — Ordered Causal Chain

1. **Biallelic hypomorphic PIGP variants** (missense p.Met25Thr / frameshift p.Glu153Asnfs\*34 / start-loss p.? / 136-kb whole-gene deletion) → **reduced PIGP mRNA/protein** (demonstrated: reduced mRNA in patient cells, PMID 28334793).
2. Reduced PIGP → **impaired GPI-GlcNAc transferase (PIG-A) complex activity** in the ER, since PIGP is an accessory subunit of the seven-component complex (PIGA/PIGC/PIGH/PIGP/PIGQ/PIGY/DPM2) → **decreased synthesis of GlcNAc-PI**, the committed first intermediate of GPI biosynthesis (demonstrated at the pathway level).
3. Reduced GPI-anchor production → **fewer completed GPI anchors in the ER** → **reduced attachment of GPI to nascent proteins** by the transamidase → **lower cell-surface expression of ≥150 GPI-anchored proteins** (demonstrated: reduced surface GPI-APs by flow cytometry, rescued by WT PIGP; PMID 28334793, 31139695).
4. Deficiency of neuronal GPI-anchored proteins (adhesion molecules, receptors, ectoenzymes involved in neuronal migration, axon guidance, and synaptic function) → **disrupted neurodevelopment and neuronal network excitability** (inferred from GPI-AP biology; direct per-protein causation in PIGP not yet demonstrated).
5. This branches to: (a) **epileptogenesis → early-onset refractory seizures**; (b) **impaired brain growth/maturation → developmental delay, intellectual disability, cerebral/cerebellar atrophy, thin corpus callosum**; and (c) at the severe end, **impaired embryonic morphogenesis → congenital anomalies / MCAHS / prenatal lethality** (reflecting near-complete loss approaching the embryonic-lethal threshold).

**Upstream vs downstream:** the PIGP lesion and GPI-anchor deficit are upstream; the surface-protein deficiency is the pivotal intermediate; seizures, developmental impairment, and malformations are downstream clinical outputs. **Cell types/processes:** neurons (CL:0000540) are the principal affected cell type; the endoplasmic reticulum (GO:0005783/0005789) is the subcellular site of the lesion; the core biological process is GPI anchor biosynthetic process (GO:0006506). No immune, autoimmune, infectious, or classical oxidative-stress mechanism is implicated.

### 7. Anatomical Structures Affected
**Primary organ/system:** the **central nervous system** (UBERON:0001017) — cerebral cortex (UBERON:0000956), cerebellum (UBERON:0002037), corpus callosum (UBERON:0002336), and white matter (UBERON:0002316). **Cell level:** **neurons** (CL:0000540). **Subcellular:** **endoplasmic reticulum** (GO:0005783), where GPI is synthesized. **Secondary/multisystem involvement** (chiefly in the broader IGD/MCAHS spectrum): gastrointestinal tract, heart, and kidney. **Lateralization:** brain involvement is **bilateral and symmetric** (e.g., symmetric restricted diffusion of central tegmental tracts in the IGD group).

### 8. Temporal Development
**Onset:** neonatal to early infancy (seizures typically within the first weeks–months; median ~6 months in IGDs). **Onset pattern:** early and progressive within infancy. **Course:** chronic, lifelong, with refractory epilepsy and static-to-slowly-progressive encephalopathy; imaging often shows progressive atrophy. **Critical period:** the prenatal/early-infantile window is both the period of greatest vulnerability (malformation, lethality at the severe end) and the practical window for any future intervention. **Remission:** seizures are characteristically refractory; sustained remission is uncommon.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** effectively complete for biallelic hypomorphic genotypes, with **highly variable expressivity** (prenatal-lethal ↔ MCAHS ↔ classic DEE). **Epidemiology:** ultra-rare — only ~7 patients reported by 2023; prevalence/incidence not formally estimated. **Carrier frequency:** the recurrent c.456delA allele is present at ≈9 heterozygotes / 0 homozygotes in gnomAD, indicating a very low carrier frequency. **Founder effects/geography:** none established; reported families are geographically dispersed (including Polish ancestry in Krenn 2019). **Sex ratio:** no sex bias expected or reported (autosomal). **Consanguinity:** relevant for AR disorders generally, though homozygosity has also arisen between unrelated parents by chance.

### 10. Diagnostics
See Findings 6–7. **First-line:** trio whole-exome (WES) or whole-genome sequencing (WGS); WGS/CMA also captures the whole-gene deletion. **Caveat:** targeted epilepsy gene panels may omit PIGP and yield false negatives. **Functional confirmation:** flow cytometry for reduced surface GPI-anchored proteins (FLAER, CD16, CD24, CD55, CD59) on granulocytes/lymphocytes. **Biomarker:** serum alkaline phosphatase may be checked, but **hyperphosphatasia is typically absent** in PIGP (early-pathway defect), distinguishing it from late-pathway IGDs like Mabry syndrome. **Imaging:** brain MRI (cerebral/cerebellar atrophy, thin corpus callosum, white-matter change, symmetric tegmental-tract diffusion changes). **EEG:** epileptiform/encephalopathic patterns. **Differential diagnosis:** other IGDs (PIGA, PIGQ, PIGY, PIGN, PIGT, PIGO, PIGV, PIGB, PIGL) and other genetic DEEs.

### 11. Outcome / Prognosis
See Finding 9. Severe: profound lifelong disability; substantial mortality (≈18% across IGDs; death in childhood possible in DEE55; prenatal lethality at the severe end). Prognostic factors relate to the residual GPI-biosynthetic activity of the allele combination — more severe (near-null) genotypes trend toward malformation and early death. Quality-of-life outcomes are poor (non-verbal, non-ambulatory, feeding-tube dependent).

### 12. Treatment
See Finding 8. **Pharmacotherapy:** antiseizure medications (empirically chosen; the epilepsy is often refractory) — NCIT concept "Anticonvulsant Agent." **Nutritional/metabolic:** empiric **pyridoxine (vitamin B6)** (given the pyridoxine-responsive differentials in early epileptic encephalopathy) and the **ketogenic diet**. **Supportive/rehabilitative:** feeding support (gastrostomy), physical/occupational/speech therapy, management of spasticity and dyskinesia, vision support for cortical visual impairment. **Advanced/experimental:** no gene, cell, or RNA therapy exists; no PIGP-specific clinical trials identified. Care is coordinated by pediatric neurology and metabolic genetics.

### 13. Prevention
No primary prevention exists for this monogenic disorder. **Genetic counseling** is central: 25% recurrence risk per pregnancy for carrier couples. **Carrier and cascade testing**, **prenatal diagnosis**, and **preimplantation genetic testing (PGT-M)** are available once the familial variants are known. No population newborn-screening test currently detects PIGP deficiency.

### 14. Other Species / Natural Disease
No naturally occurring animal disease specific to PIGP has been catalogued (no OMIA entry noted). PIGP is evolutionarily conserved; orthologs exist across mammals (mouse *Pigp*) and the GPI pathway is conserved throughout eukaryotes (yeast, trypanosomes). The GPI pathway's conservation is illustrated by the trypanosome GPI-biosynthesis literature ([PMID: 19724691](https://pubmed.ncbi.nlm.nih.gov/19724691/)), though that work concerns parasite biology rather than a PIGP-disease model. Neuronal GPI-anchored proteins (e.g., Thy-1, CD24) show developmentally regulated expression in the mouse CNS ([PMID: 10813783](https://pubmed.ncbi.nlm.nih.gov/10813783/); [PMID: 8783272](https://pubmed.ncbi.nlm.nih.gov/8783272/)), supporting the biological plausibility that GPI-anchor deficiency disrupts neurodevelopment — but these are not disease models of PIGP deficiency per se.

### 15. Model Organisms
No published PIGP-specific animal model (knockout/knock-in) recapitulating DEE55 was identified in this investigation. Relevant to interpretation: **complete GPI deficiency is embryonic-lethal in mammals** (Murakami & Kinoshita 2015, PMID 25803904), which constrains constitutive-knockout modeling and argues for **hypomorphic or conditional (e.g., neuron-specific) models** to study the disease. Patient-derived cells (fibroblasts/lymphocytes) with a flow-cytometric GPI-AP readout serve as the principal functional in-vitro system, and wild-type-PIGP rescue in patient cells (PMID 28334793) is the validated cellular assay. Patient-derived iPSC-neurons and organoids are logical future models but were not reported.

---

## Mechanistic Model / Interpretation

```
   Biallelic hypomorphic PIGP variants
   (missense p.Met25Thr / frameshift p.Glu153Asnfs*34 /
    start-loss p.? / 136-kb whole-gene deletion)
                    │  (reduced PIGP mRNA & protein — demonstrated)
                    ▼
   Impaired ER GPI-GlcNAc transferase complex
   (PIGA–PIGC–PIGH–PIGP–PIGQ–PIGY–DPM2)
                    │  ↓ committed 1st step: PI + UDP-GlcNAc → GlcNAc-PI
                    ▼
   Reduced GPI-anchor biosynthesis (partial, never complete —
   complete deficiency = embryonic lethal)
                    │
                    ▼
   ↓ Cell-surface expression of ≥150 GPI-anchored proteins
   (rescued by WT PIGP — demonstrated by flow cytometry)
                    │
        ┌───────────┼─────────────────────────┐
        ▼           ▼                         ▼
  Epileptogenesis   Impaired brain           Impaired embryonic
  → refractory      growth/maturation        morphogenesis
  early-onset       → DD/ID, absent          → congenital anomalies,
  seizures          speech, spasticity,      MCAHS, prenatal
                    cerebral/cerebellar      lethality (severe end)
                    atrophy, thin CC
```

The unifying interpretation is a **dosage/threshold model**: DEE55 severity is set by the residual GPI-biosynthetic output of a patient's specific two-allele combination. Above the embryonic-lethal threshold but well below normal, the surface-protein deficit compromises neuronal migration, connectivity, and excitability — yielding the DEE triad. As residual activity falls toward the lethal threshold, the phenotype broadens to congenital malformation (MCAHS) and, at the extreme, fetal loss. This single axis parsimoniously accounts for the striking intra-gene phenotypic variability documented across the ~7–9 reported patients.

---

## Evidence Base

| PMID | Study | Type | Contribution |
|---|---|---|---|
| [28334793](https://pubmed.ncbi.nlm.nih.gov/28334793/) | Johnstone et al. 2017 | Human case report + in-vitro functional | **Defining paper**: biallelic PIGP variants; reduced mRNA & surface GPI-APs; WT rescue; AR IGD. Supports Findings 1, 2, 4, 6. |
| [31139695](https://pubmed.ncbi.nlm.nih.gov/31139695/) | Krenn et al. 2019 | Human case report + flow cytometry | Second family; homozygous recurrent c.456delA; gnomAD rarity; panel miss; functional confirmation. Supports Finding 6. |
| [37125481](https://pubmed.ncbi.nlm.nih.gov/37125481/) | Martín-Grau et al. 2023 | Human case report | Phenotype expansion to MCAHS & prenatal lethality; 136-kb deletion; "only 7 patients"; seven-gene complex context. Supports Findings 3, 5, 7, 10. |
| [38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/) | Sidpra et al. 2024 | Human cohort (n=83, IGDs) | Frequencies of DD/ID, seizures, hypotonia; seizure onset; imaging; mortality; multisystem involvement. Supports Findings 2, 9. |
| [25803904](https://pubmed.ncbi.nlm.nih.gov/25803904/) | Murakami & Kinoshita 2015 | Review | Partial-deficiency principle (complete = embryonic lethal); flow cytometry & hyperphosphatasia as diagnostics. Supports Findings 4, 7. |
| [32156170](https://pubmed.ncbi.nlm.nih.gov/32156170/) | Kinoshita 2020 | Review | ≥150 human GPI-APs; GPI-AP biology. Supports Finding 4. |
| [39129667](https://pubmed.ncbi.nlm.nih.gov/39129667/) | Kinoshita 2024 | Review | ≥160 GPI-APs; updated biosynthesis mechanism. Supports Finding 4. |
| [31353022](https://pubmed.ncbi.nlm.nih.gov/31353022/) | Knaus et al. 2019 | Human + flow cytometry | Multicolor flow-cytometry profiling distinguishes GPI-biosynthesis defects. Supports Finding 7. |
| [35562242](https://pubmed.ncbi.nlm.nih.gov/35562242/) | Boyer, Johnsen & Morava 2022 | Review | Nutritional therapy in CDG incl. GPI-anchor disorders (pyridoxine, diet). Supports Finding 8. |
| [10813783](https://pubmed.ncbi.nlm.nih.gov/10813783/), [8783272](https://pubmed.ncbi.nlm.nih.gov/8783272/) | Thy-1 / CD24 expression studies | Model organism (mouse) | Developmental expression of neuronal GPI-APs — biological plausibility for neurodevelopmental impact. Contextual support for mechanism. |

**Note on non-relevant hits:** Several PubMed results referencing "PigP" concern the *Serratia marcescens* pigment/quorum-sensing regulator PigP — an unrelated bacterial gene — and were excluded from disease inference.

---

## Limitations and Knowledge Gaps

1. **Extremely small N.** Only ~7–9 molecularly confirmed PIGP patients are described; frequencies, natural history, and genotype–phenotype correlations rest on case reports plus extrapolation from broader IGD cohorts (which are dominated by other PIG genes).
2. **Mechanistic gaps at the protein level.** The chain from GPI-AP deficiency to epileptogenesis is inferred from general GPI-AP biology; **no PIGP-specific study identifies which downstream GPI-anchored proteins mediate the neuronal phenotype**, and there is no PIGP animal model or iPSC-neuron study.
3. **No epidemiology.** Prevalence/incidence and carrier frequency (beyond the single recurrent allele) are not formally established.
4. **Therapeutics are empiric.** Pyridoxine and ketogenic diet are extrapolated from the CDG/GPI-disorder literature; **no PIGP-specific efficacy data or trials** exist.
5. **Ontology alignment.** MONDO/Orphanet mappings should be reconciled to OMIM:617599; the Orphanet grouping cited (ORPHA:1934) is an approximate umbrella for PIGP-related early infantile epileptic encephalopathy and should be verified against the current Orphanet release.
6. **Technical caveat.** PIGP lies in the Down syndrome critical region with multiple pseudogenes, which can complicate sequencing and CNV interpretation.

---

## Proposed Follow-up Experiments / Actions

1. **Aggregate a PIGP patient registry** (via GeneMatcher / Matchmaker Exchange) to reach sufficient N for genotype–phenotype correlation and natural-history mapping.
2. **Quantify residual GPI-biosynthetic activity per allele** in patient cells (flow-cytometric surface GPI-AP levels; free-GPI T5 staining) and correlate with clinical severity to test the threshold/dosage model.
3. **Build disease models:** patient-derived iPSC → cortical neurons/organoids, and neuron-specific conditional *Pigp* hypomorphic/knockout mice (constitutive null is embryonic-lethal), to define the electrophysiological and developmental phenotype.
4. **Identify the pivotal downstream GPI-APs** via surface proteomics on PIGP-deficient neurons to pinpoint the adhesion molecules/receptors driving epileptogenesis and migration defects.
5. **Systematically test empiric therapies** (pyridoxine, ketogenic diet) with standardized seizure and developmental outcomes across the registry.
6. **Standardize diagnostics:** ensure PIGP is included in epilepsy/IGD gene panels (given documented panel misses), pair sequencing with reflex flow cytometry, and include CNV/whole-gene-deletion detection.
7. **Reconcile ontology mappings** (OMIM:617599 ↔ MONDO ↔ Orphanet ↔ ICD-11) for the knowledge-base entry.

---

*Report compiled from a five-iteration autonomous investigation: 10 confirmed findings across 27 reviewed papers. Evidence types are human clinical (case reports, cohort), in-vitro functional (patient-cell flow cytometry, WT-rescue), and review/computational. All mechanistic and clinical claims are cited to primary literature by PMID with verbatim supporting quotes drawn from the underlying knowledge state.*


## Artifacts

- [OpenScientist final report](Developmental_and_Epileptic_Encephalopathy_55-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Developmental_and_Epileptic_Encephalopathy_55-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 3 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 0 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.

23 of 26 terms resolved to a current term; the rest could not be looked up either way.