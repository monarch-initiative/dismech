---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T20:50:05.169070'
end_time: '2026-10-14T21:02:54.791696'
duration_seconds: 769.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Tritan Color Vision Deficiency
  mondo_id: MONDO:0008610
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
citation_count: 8
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 14
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 5
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0008610
    reported_labels:
    - MONDO
    ontology_label: blue color blindness
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Tritan_Color_Vision_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Tritan_Color_Vision_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tritan Color Vision Deficiency
- **MONDO ID:** MONDO:0008610 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tritan Color Vision Deficiency** covering all of the
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

# Tritan Color Vision Deficiency (MONDO:0008610): Comprehensive Disease Characteristics Report

## Summary

**Tritan Color Vision Deficiency** (tritan CVD; MONDO:0008610; OMIM 190900) is a rare, congenital, autosomal dominant disorder of the blue-yellow (short-wavelength) axis of color vision. It is caused by heterozygous mutations in **OPN1SW**, the single autosomal gene on chromosome 7q32.1 that encodes the short-wavelength-sensitive (S) cone opsin (HGNC:1012; UniProt P03999). Because OPN1SW — unlike the tandemly arranged X-linked L/M opsin genes (OPN1LW/OPN1MW) — is a solitary autosomal gene, a single pathogenic allele is sufficient to disrupt S-cone function, giving the disorder its autosomal dominant inheritance pattern and roughly equal sex distribution. Pathogenic missense alleles (L56P, G79R, S214P, P264S, R283Q, T190I) are thought to cause S-opsin misfolding/dysfunction, while splice-disrupting variants act through haploinsufficiency, producing a reduced or absent S-cone signal and selective loss of blue-yellow discrimination.

Clinically, tritan CVD is **benign, stationary, and non-degenerative**. Affected individuals have normal visual acuity, a normal fundus, and normal protan/deutan (red-green) color discrimination; the defect is confined to the tritan (blue-yellow) vector and is detected by color-vision psychophysics such as the Farnsworth-Munsell 100-hue, D-15, Mollon-Reffin Minimal test, and computerized tests (Cambridge Colour Test, CAD). Congenital tritan is the **rarest of the congenital color vision deficiencies**, in sharp contrast to acquired tritan defects, which are the most common pattern of acquired color vision loss (seen in glaucoma, diabetic retinopathy, multiple sclerosis, and normal aging owing to the selective vulnerability of the S-cone/short-wavelength pathway). The disorder shows incomplete penetrance and markedly variable expressivity — one allele (T190I) produces an illuminance-dependent phenotype ranging from mild tritanomaly to full tritanopia within a single genotype.

There is **no disease-modifying therapy** for congenital tritan CVD. Management is entirely supportive (education, occupational counseling, color-filter/assistive aids) together with genetic counseling for autosomal dominant inheritance. Because the condition does not affect survival, acuity, or cause ocular complications, the prognosis is excellent. The principal animal model — the *Opn1sw* knockout (Opn1sw^Neo/Neo) mouse — confirms that S-opsin-deficient cones remain viable for at least 1.5 years without degeneration, establishing that S-cones are a theoretically rescuable target. AAV-mediated cone-opsin gene augmentation has restored cone structure and function in related blue cone monochromacy models, providing translational proof-of-concept for a future S-opsin gene therapy, although no tritan-specific clinical trials exist.

---

## 1. Disease Information

**Overview.** Tritan Color Vision Deficiency is an inherited abnormality of the blue-yellow axis of color perception caused by dysfunction of the short-wavelength-sensitive (S) cone photoreceptors. The spectrum ranges from **tritanomaly** (reduced but present S-cone function; anomalous trichromacy on the tritan axis) to **tritanopia** (complete loss of S-cone function; dichromacy). It is sometimes described as "blue-yellow color blindness."

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0008610 |
| OMIM | 190900 (Tritanopia / Colorblindness, tritan) |
| Gene (HGNC) | OPN1SW, HGNC:1012 |
| UniProt | P03999 (OPN1SW / Blue-sensitive opsin) |
| MeSH | Color Vision Defects / Tritanopia |
| ICD-10 | H53.59 (Other color vision deficiencies) |

**Synonyms / alternative names:** Tritanopia, Tritanomaly, Blue-yellow color blindness, Tritan defect, Colorblindness (tritan), S-cone color vision deficiency.

**Information source type:** Information is derived predominantly from **aggregated disease-level resources** (OMIM, Orphanet, HPO) and from small clinical pedigree / psychophysical case studies rather than from large EHR-based individual-patient cohorts. Because the congenital form is rare and benign, it is under-ascertained in the general population; much of the molecular evidence derives from a handful of families and from model organisms.

---

## 2. Etiology

**Disease causal factors.** Congenital tritan CVD is a **Mendelian genetic disorder** caused by heterozygous mutations in the **OPN1SW** gene (chromosome 7q32.1), which encodes the S-cone opsin. There is no infectious or environmental cause for the congenital form. (See Finding F001.)

**Genetic risk factors.** The causal variants are pathogenic alleles of OPN1SW. At least six recognized pathogenic missense substitutions are associated with tritan deficiency:

| Variant | Note |
|---|---|
| L56P | Classic tritan allele |
| G79R | Classic tritan allele; also observed co-segregating in a PDE6C achromatopsia family |
| S214P | Classic tritan allele |
| P264S | Classic tritan allele |
| R283Q | Classic tritan allele |
| T190I | Illuminance-dependent phenotype (mild tritan → tritanope) |

In addition, **splice-disrupting OPN1SW variants** cause tritan deficiency via haploinsufficiency (Finding F002). Because OPN1SW is a single autosomal gene (not part of a head-to-tail tandem array like the X-linked L/M opsins), a single mutant allele is sufficient to produce the phenotype — hence autosomal dominant inheritance.

**Environmental / acquired risk factors.** The *congenital* disorder has no environmental trigger. However, **acquired tritan defects** (phenotypically similar blue-yellow loss) are common and are driven by preferential short-wavelength-pathway vulnerability in glaucoma, primary angle closure, diabetic retinopathy, macular telangiectasia type II, multiple sclerosis, HIV retinopathy, and normal aging (Finding F003). These are distinct in etiology from the Mendelian OPN1SW disorder but important for differential diagnosis.

**Protective factors.** No genetic or environmental protective factors are established for congenital tritan CVD. (Information not available.)

**Gene-environment interactions.** For the T190I allele, **retinal illuminance (an environmental/testing variable) interacts with genotype** to determine severity: the same genotype behaves as mild tritanomaly at higher illuminance but as full tritanopia at low illuminance (Finding F002). This is the clearest documented gene-environment (gene × light-level) interaction for this disorder.

---

## 3. Phenotypes

The defining phenotype is **selective impairment of blue-yellow (tritan-axis) color discrimination** with sparing of all other visual functions (Finding F005).

| Phenotype | Type | Onset | Severity | Progression | Frequency | HPO term |
|---|---|---|---|---|---|---|
| Tritan (blue-yellow) discrimination loss | Clinical sign / lab abnormality | Congenital | Mild (tritanomaly) → severe (tritanopia); variable | Stationary | Defining feature (100%) | HP:0000552 (Tritanomaly) |
| Abnormal color vision | Clinical sign | Congenital | Variable | Stationary | 100% | HP:0000551 / HP:0000496 |
| Normal visual acuity | (Preserved) | — | — | — | Typical | — |
| Normal fundus | (Preserved) | — | — | — | Typical | — |

**Phenotype characteristics.** Onset is congenital; severity is variable (mild tritanomaly to complete tritanopia), including within a single family and even illuminance-dependent for the T190I allele; progression is stable/stationary (non-degenerative). Red-green (protan/deutan) discrimination, visual acuity, and the retinal fundus are normal, which distinguishes tritan CVD from the progressive cone dystrophies that can begin with tritan-like defects.

**Quality of life impact.** Congenital tritan is typically mild and many individuals are undiagnosed. Color vision deficiency broadly causes documented difficulties in daily activities, education, career choice, and emotional well-being (Finding F005), but the tritan subtype is generally less disabling than red-green defects for everyday red-green-coded tasks. Impact is best characterized at the level of "color vision deficiency" generally rather than tritan-specifically.

**Suggested HPO terms:** HP:0000552 (Tritanomaly), HP:0000551 (Abnormality of color vision), HP:0000496 (Abnormality of color vision), and HP:0000496/HP:0000551 for abnormal color vision generally.

---

## 4. Genetic / Molecular Information

**Causal gene.** **OPN1SW** (opsin 1, short-wave-sensitive), chromosome **7q32.1**; HGNC:1012; UniProt P03999; OMIM gene/phenotype 190900. Encodes the S-cone opsin, a G-protein-coupled receptor (GPCR) of the visual-pigment family that, with 11-cis-retinal as chromophore, forms the short-wavelength-sensitive photopigment of S-cones (Finding F001).

**Pathogenic variants.**
- **Affected gene:** OPN1SW (HGNC:1012).
- **Variant classification:** The classic missense alleles (L56P, G79R, S214P, P264S, R283Q, T190I) are pathogenic/likely pathogenic for autosomal dominant tritan deficiency per co-segregation and functional data.
- **Variant type/class:** Predominantly **missense** substitutions; also **splice-site** variants acting through haploinsufficiency.
- **Functional consequences:** Missense variants are inferred to cause **S-opsin misfolding / loss of function** (dominant through reduced functional S-opsin), while splice variants cause **haploinsufficiency** (Finding F002). The T190I allele produces a dosage/light-dependent partial loss of function.
- **Allele frequency:** These are rare variants; precise gnomAD frequencies are not well established for the congenital tritan alleles (Information limited).
- **Somatic vs germline:** Germline.

**Modifier genes.** No formal modifier genes are established. Co-occurrence of an OPN1SW G79R allele was proposed to modify the phenotype (complete vs incomplete achromatopsia) in a family also segregating a recessive PDE6C mutation, suggesting OPN1SW status can modulate cone phenotype in trans with other cone-gene lesions (a modifier-like effect; PMID:25605338).

**Epigenetic information.** No disease-specific epigenetic changes are documented for tritan CVD. Cone opsin expression is transcriptionally controlled by nuclear receptors TRβ2 (THRB), RXRγ, RORβ, RORα, and the homeobox factor CRX (Finding F004), but these are developmental regulators, not established epigenetic disease mechanisms.

**Chromosomal abnormalities.** None for the single-gene OPN1SW disorder. Of note, a distinct autosomal dominant cone dystrophy with *early tritanopic* color defect maps to a 16q12 duplication affecting the IRXB/IRX5-IRX6 cluster (PMID:33891002) — this is a separate progressive disease, not OPN1SW tritan CVD.

---

## 5. Environmental Information

- **Environmental factors:** None cause the congenital disorder. Acquired tritan-type defects arise secondarily to toxic, metabolic, and degenerative retinal/optic-nerve insults (see §2 and §3).
- **Lifestyle factors:** Not applicable to congenital tritan CVD.
- **Infectious agents:** Not applicable to the congenital genetic disorder. (HIV retinopathy can produce acquired cone dysfunction with downregulation of OPN1SW and other cone transcripts, but this is a secondary, acquired phenomenon, not congenital tritan CVD.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A heterozygous **OPN1SW mutation** (missense, e.g., L56P/G79R/S214P/P264S/R283Q/T190I, or a splice-site variant) is inherited in autosomal dominant fashion → **leads to** an abnormal or reduced-quantity S-cone opsin protein.
2. **Missense branch:** The amino-acid substitution **leads to** misfolding / impaired function of the S-opsin GPCR (inferred from GPCR structural biology; direct structural proof for each tritan allele is limited) → **results in** reduced functional short-wavelength photopigment in S-cones.
   **Splice branch:** The splice-disrupting variant **leads to** loss of one functional allele's product (haploinsufficiency) → **results in** reduced S-opsin quantity (Finding F002).
3. Reduced/abnormal S-opsin **results in** a diminished or absent S-cone photoreceptor light response (phototransduction signal) along the short-wavelength pathway.
4. Loss of the S-cone signal **leads to** impaired coding of the blue-yellow (koniocellular/S-cone-opponent) chromatic channel downstream.
5. This **results in** the clinical manifestation: selective loss of blue-yellow (tritan-axis) color discrimination, with preserved acuity, red-green discrimination, and normal fundus (Finding F005).
6. Because S-cones (unlike rods) remain viable without their opsin (demonstrated in the Opn1sw^Neo/Neo mouse, Finding F004), the phenotype is **stationary and non-degenerative** — the chain does not progress to photoreceptor death or vision loss.

For the **T190I allele**, step 2 is partial and **illuminance-modulated**: at higher retinal illuminance enough functional S-opsin signal remains for mild tritanomaly, whereas at low illuminance the signal falls below threshold and the phenotype becomes full tritanopia (Finding F002).

### Mechanistic detail by category

- **Molecular pathways:** Visual phototransduction (GPCR/opsin → transducin → cGMP phosphodiesterase → CNG channel) specifically in the S-cone. The primary lesion is at the receptor (opsin) step. GO: phototransduction (GO:0007602), detection of light stimulus involved in visual perception (GO:0050908).
- **Cellular processes:** Reduced S-cone light response; notably **no apoptosis/degeneration** (cones survive). GO: visual perception (GO:0007601), photoreceptor cell maintenance.
- **Protein dysfunction:** S-opsin misfolding / loss of function (missense) or reduced quantity (haploinsufficiency). GO: photoreceptor outer segment (GO:0001750).
- **Metabolic changes:** None established; the chromophore is 11-cis-retinal (CHEBI:16066).
- **Immune involvement:** None.
- **Tissue damage mechanisms:** None in the congenital disorder (benign, stationary).
- **Biochemical abnormalities:** Defective short-wavelength photopigment function.
- **Molecular profiling:** In the mouse model, elimination of S-opsin mRNA relieves translational competition, **increasing M-opsin expression** in affected cones — a compensatory shift (Finding F004).

**Cell type involved:** S-cone photoreceptor (CL:0000573, retinal cone cell / short-wavelength-sensitive cone). **Biological process GO terms:** GO:0007602 (phototransduction), GO:0007601 (visual perception), GO:0050908 (detection of light stimulus in visual perception).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Eye — specifically the **retina** (UBERON:0000966). Body system: visual/nervous system. No secondary organ involvement.
- **Tissue/cell level:** **Neural retina** (UBERON:0003902); specific target cell population = **S-cone photoreceptors** (CL:0000573, cone retinal photoreceptor cell). Rods, L-cones, and M-cones are spared.
- **Subcellular level:** The **photoreceptor outer segment** (GO:0001750), where opsin-based phototransduction occurs; the S-opsin is a membrane protein of the outer-segment disc membranes. In the mouse model, many S-opsin-null ventral cones **fail to form outer segments** (Finding F004).
- **Localization:** Bilateral and symmetric (both eyes equally, as expected for a germline opsin gene defect). UBERON:0000966 (retina), UBERON:0001782 (retinal photoreceptor layer).
- **Lateralization:** Bilateral, symmetric.

---

## 8. Temporal Development

- **Onset:** Congenital (present from birth), though frequently detected only when color vision is formally tested in later childhood or adulthood. Onset pattern: non-progressive/congenital.
- **Progression:** **Stationary** — stable and non-progressive over life. No disease stages. This is supported both clinically and by the animal model, in which S-opsin-null cones survive ≥1.5 years without degeneration (Finding F004).
- **Disease course:** Chronic lifelong but benign and unchanging.
- **Remission patterns:** Not applicable (stable congenital trait; no remission, no worsening).
- **Critical periods:** Not applicable; because cones remain viable long-term, any hypothetical gene-replacement window would be broad (a favorable feature for future therapy).

---

## 9. Inheritance and Population

**Epidemiology.** Congenital tritan CVD is the **rarest congenital color vision deficiency** (Finding F003). A 2025 systematic review/meta-analysis (1,703,619 participants; 56 studies; 21 countries) estimated the global prevalence of all congenital CVD at **2.59% (95% CI 2.20–3.03%)**, overwhelmingly red-green (deutan/protan); tritan is the smallest subtype. Classic textbook estimates place tritan prevalence on the order of ~1 in 10,000 or lower, but precise congenital tritan prevalence figures are uncertain owing to under-ascertainment.

**Inheritance.** **Autosomal dominant** (OPN1SW is a single autosomal gene on 7q32.1), with:
- **Penetrance:** Incomplete.
- **Expressivity:** Variable — ranging from mild tritanomaly to tritanopia, even illuminance-dependent for T190I (Finding F002).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects / consanguinity:** Not established as relevant; as an autosomal dominant single-gene trait, consanguinity is not a driver.
- **Carrier frequency:** Not well defined (rare alleles).

**Population demographics.**
- **Sex ratio:** Approximately **1:1** (autosomal), in contrast to the strong male predominance of X-linked red-green CVD.
- **Affected populations / geographic distribution:** No strong ethnic or geographic enrichment is established for congenital tritan CVD. (Information limited.)

---

## 10. Diagnostics

**Clinical/psychophysical color-vision tests (primary diagnostic modality).** Diagnosis rests on demonstrating a selective tritan-axis defect (Finding F005):

| Test | Role in tritan diagnosis |
|---|---|
| Farnsworth-Munsell 100-hue | Blue-yellow confusion axis errors |
| Farnsworth D-15 / Lanthony D-15 | Tritan confusion axis crossings |
| Hardy-Rand-Rittler (HRR) plates | Includes tritan plates |
| Mollon-Reffin Minimal test | Sensitive color-discrimination test for tritan axis |
| Cambridge Colour Test (CCT) | Computerized; quantifies tritan vector threshold |
| Colour Assessment and Diagnosis (CAD) | Quantifies tritan vector; high sensitivity/specificity |
| Anomaloscope (Moreland equation) | Tritan/blue-green matching |

**Electrophysiology:** S-cone-specific ERG can demonstrate selective S-cone dysfunction; standard full-field ERG and acuity are otherwise normal, helping distinguish stationary tritan CVD from cone dystrophies.

**Genetic testing:** Single-gene **OPN1SW sequencing** (including splice-site analysis) confirms the molecular diagnosis; WES/WGS or inherited-retinal-disease gene panels including OPN1SW are appropriate in atypical cases. Genetic testing distinguishes benign stationary OPN1SW tritan CVD from progressive cone dystrophies that present with early tritan defects (e.g., the 16q12/IRXB duplication disorder).

**Imaging:** Fundus examination and OCT are **normal** in congenital tritan CVD — a key discriminator from acquired tritan defects and cone dystrophies.

**Differential diagnosis:**
- Acquired tritan defects (glaucoma, primary angle closure, diabetic retinopathy, macular telangiectasia type II, multiple sclerosis, HIV retinopathy, aging) — these have an underlying ocular/systemic cause and often additional findings.
- Autosomal dominant cone dystrophy with early tritanopia (16q12/IRXB duplication) — progressive, with acuity loss.
- Enhanced S-cone syndrome, blue cone monochromacy, achromatopsia — distinguished by ERG, acuity, and genetics.

**Screening:** No population newborn or carrier screening program exists; detection is opportunistic via color-vision testing (e.g., occupational/educational screening).

---

## 11. Outcome / Prognosis

- **Survival/mortality:** Not affected. Congenital tritan CVD does not influence life expectancy or mortality (Finding F006).
- **Morbidity/function:** Minimal; visual acuity and ocular health are preserved. The main impact is on color-dependent tasks and occupational suitability; congenital tritan is generally milder than red-green CVD.
- **Quality of life:** Color vision deficiency broadly affects daily activities, education, career choice, and emotional well-being (Finding F005), but tritan-specific QoL burden is modest and many cases are undiagnosed.
- **Disease course / complications:** None — stationary and non-degenerative; no ocular complications.
- **Prognostic factors/biomarkers:** Not applicable; the condition is stable regardless of genotype (although genotype determines baseline severity, e.g., T190I vs classic alleles).

Overall prognosis is **excellent** (benign, lifelong, stable).

---

## 12. Treatment

**There is no approved disease-modifying therapy** for congenital tritan CVD (Finding F006). Management is:

- **Supportive/rehabilitative:** Patient education, occupational counseling (relevant where color discrimination is safety-critical), and **color-filter/assistive aids** (e.g., tinted lenses, digital color-identification tools). NCIT: supportive care, visual rehabilitation.
- **Genetic counseling:** For autosomal dominant inheritance (50% transmission risk; incomplete penetrance and variable expressivity should be conveyed).
- **Pharmacotherapy / surgery / immunotherapy:** None applicable.
- **Experimental/advanced therapeutics (future):** **AAV-mediated cone-opsin gene augmentation** has achieved robust rescue of cone structure and function in related disorders (blue cone monochromacy mouse models, e.g., C203R/C198R all-cone models), demonstrating that opsin cDNA delivery can restore cone function (Finding F006). Combined with the finding that S-opsin-null cones remain viable for ≥1.5 years (Finding F004), this makes S-cones a theoretically rescuable target. However, **no tritan-specific clinical trials exist**, and given the benign stationary nature of the disease, the clinical imperative for gene therapy is low compared with blinding cone disorders.

**Pharmacogenomics / personalized medicine:** Not applicable currently; any future approach would be genotype-guided (OPN1SW cDNA augmentation).

---

## 13. Prevention

- **Primary prevention:** Not applicable — a germline genetic trait cannot be prevented. Preconception/prenatal **genetic counseling** can inform reproductive decisions.
- **Secondary prevention:** Early detection via color-vision screening (educational/occupational) allows appropriate guidance, but there is no treatment to initiate.
- **Tertiary prevention:** Supportive measures (assistive aids, occupational accommodation) to minimize functional impact.
- **Genetic screening/counseling:** Cascade genetic testing within families and genetic counseling for the autosomal dominant pattern are the main preventive tools. Carrier/newborn screening programs are not established for this benign condition.
- **Immunization/public health/environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologous gene:** The mouse ortholog is **Opn1sw** (NCBI Gene; *Mus musculus*, NCBI:txid10090). S-opsin orthologs exist broadly across vertebrates; cone opsin expression is conserved and transcriptionally regulated by THRB (TRβ2), RXRγ, RORβ, RORα, and CRX (Finding F004).
- **Natural disease in other species:** No well-characterized naturally occurring OPN1SW tritan-equivalent disease is cataloged as a major veterinary entity; S-opsin biology is primarily studied in engineered mouse models rather than spontaneous animal disease (Information limited for OMIA natural-disease entries).
- **Comparative biology:** Mouse S-opsin-null cones survive long-term and show compensatory M-opsin upregulation (Finding F004), illustrating conserved cone-survival mechanisms and translational competition between opsins. S-opsin also contributes to violet-light-dependent refractive development in mice (Opn1sw^−/− mice are more myopic and lack the violet-light hyperopic shift) — a species-specific role not directly part of the human color-vision phenotype.
- **Zoonotic potential:** Not applicable (non-infectious genetic trait).

---

## 15. Model Organisms

**Principal model: the Opn1sw^Neo/Neo (S-opsin knockout) mouse** (Finding F004).

| Feature | Detail |
|---|---|
| Model type | Mammalian genetic knockout (mouse, *Mus musculus*) |
| Construct | Neomycin cassette inserted between exons 3–4 of *Opn1sw* |
| Phenotype recapitulation | Loss of S-cone (S-opsin) function; **stationary, non-degenerative** — models the key human feature that S-cone defect does not kill cones |
| Key findings | Cones remain viable ≥1.5 years (vs rod death by 2.5 months in Rho^−/−); many ventral cones fail to form outer segments; functional cones phototransduce normally and show **increased M-opsin** (compensatory, via relief of translational competition) |
| Limitations | Mice are dichromats with a dorsal-ventral opsin gradient, lack a human-like fovea and trichromatic color vision; models S-opsin *loss* (haploinsufficiency-like) better than dominant missense misfolding |
| Related models | Opn1sw^−/− (refractive/violet-light studies); all-cone BCM gene-therapy models (C203R/C198R) used to demonstrate cone-opsin AAV rescue |
| Databases | MGI, IMPC, IMSR |

Mouse studies underpin two central conclusions: (1) **S-cones survive without their opsin** (stationary phenotype, broad therapeutic window), and (2) **cone-opsin cDNA delivery restores cone function** (proof-of-concept for gene augmentation).

---

## Mechanistic Model / Interpretation

```
            OPN1SW mutation (autosomal dominant, 7q32.1)
                          │
          ┌───────────────┴────────────────┐
   Missense (L56P, G79R,              Splice-site
   S214P, P264S, R283Q, T190I)        variant
          │                                │
   S-opsin misfolding /            Haploinsufficiency
   loss of function                (reduced S-opsin quantity)
          │                                │
          └───────────────┬────────────────┘
                          ▼
         Reduced / absent functional S-cone photopigment
                          ▼
         Diminished S-cone phototransduction signal
                          ▼
     Impaired blue-yellow (S-cone-opponent) chromatic channel
                          ▼
   Selective tritan-axis color discrimination loss
   (acuity, red-green, fundus all NORMAL)
                          ▼
   STATIONARY / BENIGN  ← S-cones remain viable (no degeneration)
                          │
              T190I: severity modulated by retinal illuminance
              (mild tritanomaly at high Td → tritanopia at low Td)
```

**Upstream vs downstream:** The initiating lesion is the OPN1SW mutation (upstream); the most downstream event is the perceptual blue-yellow discrimination deficit. The critical "brake" on the chain is that S-cone survival is independent of S-opsin — so the disease never progresses to cell death, unlike rod opsin loss. **Cell type:** S-cone photoreceptor (CL:0000573). **Process:** phototransduction (GO:0007602) / visual perception (GO:0007601). **Anatomy:** retina (UBERON:0000966), photoreceptor outer segment (GO:0001750). **Chemical:** 11-cis-retinal chromophore (CHEBI:16066).

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [23022137](https://pubmed.ncbi.nlm.nih.gov/23022137/) | *Substitution of isoleucine for threonine at position 190 of S-opsin…* | OPN1SW causal gene; five classic missense alleles; T190I illuminance-dependent phenotype (F001, F002) |
| [32400513](https://pubmed.ncbi.nlm.nih.gov/32400513/) | *Tritan CVD may be associated with an OPN1SW splicing defect and haploinsufficiency* | Splicing/haploinsufficiency mechanism (F002) |
| [42346125](https://pubmed.ncbi.nlm.nih.gov/42346125/) | *Cone Opsins and Inherited Retinal Disease* | Tritan CVD is a cone-opsin gene disorder (F001) |
| [40769301](https://pubmed.ncbi.nlm.nih.gov/40769301/) | *Global Prevalence of Congenital Color Vision Deficiency, 1932–2022* | Global CVD prevalence 2.59%; tritan rarest subtype (F003) |
| [41317340](https://pubmed.ncbi.nlm.nih.gov/41317340/) | *Digital Color Vision Testing… in Multiple Sclerosis* | Tritan most common acquired defect (39.9%) (F003) |
| [21219924](https://pubmed.ncbi.nlm.nih.gov/21219924/) | *A mouse M-opsin monochromat: increased M-opsin when S-opsin knocked out* | Opn1sw KO cones viable ≥1.5 yr; compensatory M-opsin (F004, F006) |
| [30443703](https://pubmed.ncbi.nlm.nih.gov/30443703/) | *The impacts of abnormal color vision on people's life* | QoL/occupational impact of CVD (F005) |
| [15094734](https://pubmed.ncbi.nlm.nih.gov/15094734/) | *Blue cone monochromatism: phenotype/genotype…* | Supports Mollon-Reffin minimal color-discrimination testing (F005) |
| [38060327](https://pubmed.ncbi.nlm.nih.gov/38060327/) | *Structural and functional rescue of cones… C203R* | Cone-opsin AAV augmentation restores cone function (F006) |
| [25605338](https://pubmed.ncbi.nlm.nih.gov/25605338/) | *Congenital Achromatopsia… PDE6C* | OPN1SW G79R tritan allele co-segregating; modifier-like effect |
| [33891002](https://pubmed.ncbi.nlm.nih.gov/33891002/) | *Duplication on 16q12 (IRXB)… AD cone dystrophy with early tritanopia* | Differential diagnosis: distinct progressive tritan disorder |

**Verbatim supporting quotes:**
- F001/F002: *"Five mutations in the S-cone-opsin gene (OPN1SW) that give rise to different single amino-acid substitutions (L56P, G79R, S214P, P264S, R283Q) are known to be associated with tritan color-vision deficiency."* and *"Individuals with the T190I S-opsin mutation behaved as mild tritans at 12.3-92.3Td, but as tritanopes at 1.2-9.2Td…"* (PMID:23022137)
- F002: *"Here we present evidence implicating disrupted RNA splicing as a potential cause of inherited tritan color vision."* (PMID:32400513)
- F003: *"The global prevalence of CVD was estimated at 2.59%"* (PMID:40769301); *"tritan deficiencies being the most common pure type (39.9%)"* (PMID:41317340)
- F004: *"cones of the Opn1sw(Neo/Neo) mouse remain viable for at least 1.5 yrs, even though many ventral cones do not form outer segments"* (PMID:21219924)
- F006: *"gene augmentation targeting cones specifically yielded robust rescue of cone function and structure"* (PMID:38060327)

---

## Limitations and Knowledge Gaps

1. **Small molecular evidence base.** The pathogenic OPN1SW missense alleles derive from a limited number of families; functional/structural proof of misfolding for each specific allele is inferred rather than individually demonstrated.
2. **Imprecise epidemiology.** Congenital tritan prevalence is poorly quantified because the condition is benign and under-ascertained; most CVD prevalence data are dominated by red-green defects.
3. **Penetrance/expressivity not quantified.** Incomplete penetrance and variable expressivity are recognized but lack precise estimates; only T190I has a characterized illuminance-dependence.
4. **No allele frequency data.** gnomAD-level frequencies for the tritan alleles are not well established.
5. **Model limitations.** The mouse is dichromatic and fovealess; it models S-opsin loss (haploinsufficiency-like) more directly than dominant missense misfolding, and cannot reproduce human blue-yellow percepts.
6. **No tritan-specific therapy data.** Gene-therapy evidence is extrapolated from blue cone monochromacy models, not from tritan CVD itself.
7. **Differential-diagnosis overlap.** Acquired tritan defects and progressive tritanopic cone dystrophies (e.g., 16q12/IRXB) phenocopy early findings; genotype + fundus/ERG are needed to separate them.

---

## Proposed Follow-up Experiments / Actions

1. **Functional characterization of each OPN1SW allele** (heterologous expression, spectral tuning, folding/trafficking assays, AlphaFold-guided structural modeling) to convert "inferred misfolding" into demonstrated mechanism and refine ACMG classification.
2. **Population genomics:** query gnomAD/large biobanks for OPN1SW tritan alleles to estimate true allele frequencies, penetrance, and any founder effects.
3. **Deep phenotyping cohort** using standardized tritan-vector quantification (CAD/CCT) plus S-cone ERG and AO imaging to map genotype–severity relationships and test illuminance-dependence beyond T190I.
4. **Knock-in mouse models** carrying human missense alleles (e.g., P264S, T190I) to distinguish misfolding/dominant-negative from haploinsufficiency mechanisms in vivo.
5. **Proof-of-concept S-opsin gene augmentation** in an Opn1sw-deficient model (building on BCM AAV success and demonstrated long-term S-cone viability) to establish whether S-cone function is restorable — primarily of mechanistic interest given the benign clinical course.
6. **Natural-history / QoL study** specifically in congenital tritan individuals to quantify (currently assumed modest) functional and occupational impact separately from red-green CVD.

---

*Evidence source types represented: human clinical/psychophysical and pedigree studies (OPN1SW variants, prevalence, QoL); model-organism (Opn1sw knockout mouse, BCM gene-therapy models); computational/structural (inferred GPCR misfolding). Information explicitly flagged as "not available / not applicable" where the literature does not support a claim for this specific disease.*


## Artifacts

- [OpenScientist final report](Tritan_Color_Vision_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Tritan_Color_Vision_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008610` (3 mentions) - the report calls it "MONDO"; MONDO calls it **blue color blindness**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000496` (3 mentions) - the report calls it "Abnormality of color vision"; HP calls it **Abnormality of eye movement**
- `GO:0050908` (2 mentions) - the report calls it "detection of light stimulus in visual perception"; GO calls it **detection of light stimulus involved in visual perception**
- `GO:0001750` (3 mentions) - the report calls it "photoreceptor outer segment", "Subcellular level:** The **photoreceptor outer segment"; GO calls it **photoreceptor outer segment**
- `UBERON:0003902` (1 mention) - the report calls it "Neural retina", "Tissue/cell level:** **Neural retina"; UBERON calls it **retinal neural layer**, and lists "neural retina" among its other names
- `UBERON:0001782` (1 mention) - the report calls it "retinal photoreceptor layer"; UBERON calls it **pigmented layer of retina**, and lists "retinal pigment layer" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0001750` - called "photoreceptor outer segment", "Subcellular level:** The **photoreceptor outer segment"
- `UBERON:0003902` - called "Neural retina", "Tissue/cell level:** **Neural retina"