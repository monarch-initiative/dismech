---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-09T18:58:50.839337'
end_time: '2026-09-09T19:14:40.968960'
duration_seconds: 950.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 105
  mondo_id: MONDO:0800104
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
citation_count: 10
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 23
  quotes_valid: 23
  relevance_assessed: 12
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 46
  verified: 45
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 7
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_105-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_105-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 105
- **MONDO ID:** MONDO:0800104 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 105** covering all of the
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

# Immunodeficiency 105 (IMD105 / CD45 Deficiency SCID): Comprehensive Disease Characteristics Report

**Disease:** Immunodeficiency 105 · **MONDO:** MONDO:0800104 · **OMIM:** #619924 (phenotype), 151460 (gene) · **Gene:** *PTPRC* (CD45) · **Category:** Mendelian (autosomal recessive)

---

## Summary

**Immunodeficiency 105 (IMD105) is an ultra-rare autosomal recessive severe combined immunodeficiency (SCID) caused by biallelic loss-of-function mutations in *PTPRC*, the gene encoding the leukocyte common antigen CD45.** CD45 is an abundant, hematopoietic-specific, receptor-type transmembrane protein tyrosine phosphatase (UniProt P08575; EC 3.1.3.48) expressed on all nucleated blood cells. Its principal function is to activate the Src-family kinases Lck and Fyn — by dephosphorylating their inhibitory C-terminal tyrosine — which are indispensable for T-cell-receptor (TCR) and B-cell-receptor (BCR) proximal signaling. When CD45 is absent, Lck remains locked in an inhibited conformation, antigen-receptor signaling collapses, and thymic T-cell development arrests. The clinical result is a **T-cell-negative, B-cell-positive, NK-variable (T−B+NK±) SCID** that presents in early infancy (~2 months) with severe, recurrent, opportunistic infections and progressive hypogammaglobulinemia despite normal B-cell numbers.

The disease was defined by only a small number of human patients. The first (Kung et al., 2000) carried a large deletion on one *PTPRC* allele plus an IVS13 splice-site mutation on the other; the second (Tchilian et al., 2001) was homozygous for a 6-bp in-frame deletion removing Glu339/Tyr340 in the first fibronectin type III module of the CD45 extracellular domain, abolishing surface CD45. A *Ptprc*-null mouse faithfully recapitulates the human immunophenotype (T-low, B-normal-to-high) with a two-stage block in thymic T-cell development, providing strong mechanistic corroboration. Importantly, the common *PTPRC* **C77G isoform-altering polymorphism** — associated with autoimmune and infectious-disease susceptibility — is mechanistically and clinically **separate** from the biallelic null mutations that cause IMD105.

Diagnosis begins with universal newborn screening for T-cell receptor excision circles (TRECs); affected infants are T-lymphopenic with low/absent TRECs. Confirmation relies on lymphocyte immunophenotyping (T−B+NK± with the diagnostically distinctive **absence of surface CD45 on all leukocytes**), absent mitogen proliferation, and molecular sequencing of *PTPRC*. The only curative therapy is **allogeneic hematopoietic stem cell transplantation (HSCT)**; untreated disease is fatal in early childhood. Survival is markedly better when disease is detected pre-symptomatically by newborn screening. This report compiles the etiology, phenotype spectrum, molecular mechanism, anatomy, epidemiology, diagnostics, prognosis, treatment, prevention, and model-organism data with supporting ontology terms and primary-literature citations.

---

## Key Findings

### Finding 1 — IMD105 is CD45 deficiency SCID caused by biallelic *PTPRC* mutations

IMD105 (OMIM #619924; MONDO:0800104) is a severe combined immunodeficiency caused by homozygous or compound-heterozygous loss-of-function mutations in *PTPRC* (CD45; **HGNC:9666**; NCBI Gene 5788) on chromosome **1q31.3**. Inheritance is autosomal recessive. The immunophenotype is **T− B+ NK-variable SCID** with onset of recurrent infections in early infancy. The disorder sits within the OMIM Autosomal Recessive SCID Phenotypic Series (PS601457).

The first CD45-deficient patient (Kung et al., 2000) presented at 2 months with SCID, carrying a large deletion on one allele and an IVS13 donor splice-site point mutation on the other; peripheral T cells were greatly diminished and mitogen-unresponsive, B-cell numbers were normal, but serum immunoglobulins declined with age. The second patient (Tchilian et al., 2001) was homozygous for a 6-bp deletion causing loss of Glu339 and Tyr340 in the first fibronectin type III module of the extracellular domain, which prevented CD45 surface expression.

> "The patient presented at 2 months of age with severe combined immunodeficiency disease." — [PMID: 10700239](https://pubmed.ncbi.nlm.nih.gov/10700239/)
>
> "Thus, CD45 deficiency in humans results in T- and B-lymphocyte dysfunction." — [PMID: 10700239](https://pubmed.ncbi.nlm.nih.gov/10700239/)
>
> "a homozygous 6-bp deletion in the gene encoding CD45 (PTPRC, gene map locus 1q31-32), which results in a loss of glutamic acid 339 and tyrosine 340 in the first fibronectin type III module of the extracellular domain of CD45, is associated with failure of surface expression of CD45 and SCID" — [PMID: 11145714](https://pubmed.ncbi.nlm.nih.gov/11145714/)

### Finding 2 — Mechanism: CD45 activates Src-family kinases (Lck/Fyn) required for antigen-receptor signaling

CD45 is an abundant, hematopoietic-specific transmembrane tyrosine phosphatase on all leukocytes. It dephosphorylates the inhibitory C-terminal tyrosine of Lck (Y505) to relieve autoinhibition and permit the active, open conformation. The phospho-balance at Lck's inhibitory versus activating tyrosines is set jointly by CD45 (activating) and Csk (inhibitory). Loss of CD45 therefore leaves Lck hyperphosphorylated and inactive, abrogating TCR- and BCR-proximal signaling and blocking thymocyte and T-cell development. CD45 additionally has a *negative* role — it can dephosphorylate the TCR itself — and its spatial exclusion from TCR clusters tunes the net signaling outcome (reconstituted-membrane studies).

> "The hematopoietic-specific transmembrane protein tyrosine phosphatase CD45 functions to regulate Src kinases required for T- and B-cell antigen receptor signal transduction." — [PMID: 10700239](https://pubmed.ncbi.nlm.nih.gov/10700239/)
>
> "The balance of phosphorylation at the inhibitory and activating Tyr residues is maintained by a balance between CD45 and Csk" — [PMID: 32794043](https://pubmed.ncbi.nlm.nih.gov/32794043/)
>
> "CD45 is an abundant transmembrane tyrosine phosphatase, expressed on all leukocytes, and is required for efficient lymphocyte signaling." — [PMID: 11145714](https://pubmed.ncbi.nlm.nih.gov/11145714/)

### Finding 3 — CD45-null mouse recapitulates human T−B+ immunophenotype (model organism)

*Ptprc* (Cd45) knockout mice (Byth et al., 1996) completely lack all CD45 isoforms and display an immunophenotype closely matching the human disease: ~5-fold reduction in splenic T cells and ~2-fold increase in B cells versus controls. T-cell development is blocked at two stages — a reduced double-negative→double-positive (DN→DP) transition (~2-fold) and a severely impaired DP→single-positive maturation (~4–5-fold). CD45-null thymocytes are severely impaired in TCR-crosslinking-induced apoptosis (negative selection) yet respond normally to non-TCR signals, and show defective superantigen (SEB)-mediated deletion. CD45 is expressed highest on large, cycling, positively-selected DP thymocytes and enhances positive selection. Mouse *Ptprc* = NCBI Gene 19264, ortholog of human *PTPRC* (NCBI Gene 5788).

> "The spleens from CD45-null mice contain approximately twice the number of B cells and one fifth the number of T cells found in normal controls." — [PMID: 8666928](https://pubmed.ncbi.nlm.nih.gov/8666928/)
>
> "T cell development is significantly inhibited in CD45-null animals at two distinct stages." — [PMID: 8666928](https://pubmed.ncbi.nlm.nih.gov/8666928/)

### Finding 4 — *PTPRC* C77G is a distinct isoform-altering susceptibility polymorphism, NOT a cause of IMD105

The **C77G polymorphism** in *PTPRC* exon 4/exon A disrupts an exonic splicing silencer (ESS1/ARS motif), preventing hnRNP L/K/E2-mediated repression and causing aberrant retention of CD45RA isoforms on activated/memory T cells (Motta-Mena 2011). C77G occurs at low frequency in healthy individuals but is enriched in multiple sclerosis, systemic sclerosis, autoimmune hepatitis, hepatitis C, and HIV-1 cohorts; it enhances TCR signaling and alters cytokine (IL-2/Jak1) responsiveness and adhesion. A second isoform-altering polymorphism, A138G, is associated with Graves' disease. The MS association is inconsistent across populations (no association in an Australian cohort). This is a partial gain/alteration-of-function *susceptibility allele* — mechanistically and clinically **separate** from the biallelic loss-of-function that causes IMD105 SCID. This distinction is essential for correctly curating the disease entry.

> "An enhanced frequency of C77G individuals has been reported in cohorts of patients suffering from multiple sclerosis, systemic sclerosis, autoimmune hepatitis, hepatitis C and human immunodeficiency virus (HIV)-1." — [PMID: 17903220](https://pubmed.ncbi.nlm.nih.gov/17903220/)
>
> "the C77G polymorphism, which correlates with autoimmune disease susceptibility in humans, disrupts exon silencing by preventing the redundant activity of hnRNPs K and E2 to compensate for the weakened function of hnRNP L" — [PMID: 21507955](https://pubmed.ncbi.nlm.nih.gov/21507955/)
>
> "Two polymorphisms (C77G and A138G), which alter CD45 isoform expression, are associated with autoimmune and infectious diseases." — [PMID: 18312479](https://pubmed.ncbi.nlm.nih.gov/18312479/)

### Finding 5 — Diagnostics: TREC newborn screening detects CD45-deficiency SCID; confirmed by flow cytometry and *PTPRC* sequencing

SCID, including CD45 deficiency, is detectable at birth by quantifying T-cell receptor excision circles (TRECs) in dried blood spots; CD45-deficient infants are T-lymphopenic and will have low/absent TRECs. In the Catalonia program (2017–2023), among 420,263 newborns, 105 screened positive (0.02%) using the EnLite Neonatal TREC assay (cut-off 20 copies/µL), yielding an overall SCID incidence of **1:46,753 live births**. Combined TREC/KREC assays additionally flag B-cell lymphopenia. Confirmatory workup: lymphocyte immunophenotyping by flow cytometry (T−/B+/NK-variable; **absent surface CD45 on all leukocytes is diagnostic and distinctive**), mitogen proliferation assays (absent), serum immunoglobulins (hypogammaglobulinemia), and molecular confirmation by *PTPRC* sequencing (single-gene, gene panels, or WES/WGS).

> "Severe combined immunodeficiency (SCID) can be detected at birth through T-cell receptor excision circles (TREC) analysis in dried blood spots." — [PMID: 42079620](https://pubmed.ncbi.nlm.nih.gov/42079620/)
>
> "is associated with failure of surface expression of CD45 and SCID" — [PMID: 11145714](https://pubmed.ncbi.nlm.nih.gov/11145714/)

### Finding 6 — Treatment & prognosis: Allogeneic HSCT is the only curative therapy; early diagnosis markedly improves survival

Allogeneic hematopoietic stem cell transplantation (HSCT/HCT) is the **only curative treatment** for SCID including CD45 deficiency; without immune reconstitution, death occurs in early childhood. Outcome is strongly time-dependent. In a Brazilian cohort, 2-year overall survival was **71.4% for early-diagnosed** (newborn-screened/family history) versus **29.2% for late clinically-diagnosed** SCID (p = 0.053). In a 100-patient single-center HSCT cohort, overall survival was 68% (84% excluding first-month mortality), and NBS-identified cases had superior OS (93%) versus clinically-identified cases (p = 0.04); better outcomes were associated with bone-marrow stem-cell source, matched related donors, and use of conditioning. Supportive care before transplant: protective isolation, antimicrobial/antifungal/anti-*Pneumocystis* prophylaxis, immunoglobulin replacement, avoidance of live vaccines, and use of irradiated/CMV-safe/leukoreduced blood products. Gene therapy is investigational for other SCID subtypes but not established for *PTPRC*.

> "Hematopoietic cell transplantation (HCT) is the only curative treatment currently available in Brazil." — [PMID: 40374985](https://pubmed.ncbi.nlm.nih.gov/40374985/)
>
> "The 2-year overall survival (OS) of the late group was 29.2%, in contrast to the 2-year OS of the early diagnosis group of 71.4%" — [PMID: 40374985](https://pubmed.ncbi.nlm.nih.gov/40374985/)
>
> "SCID cases identified by NBS demonstrated superior OS (93%) compared to cases identified by clinical presentation" — [PMID: 39900265](https://pubmed.ncbi.nlm.nih.gov/39900265/)

### Finding 7 — Clinical phenotype spectrum with HPO terms

Per the OMIM #619924 clinical synopsis and the reported patients: onset in early infancy (~2 months) with recurrent/severe infections. Manifestations include recurrent respiratory infections/pneumonia, severe combined immunodeficiency, T-cell lymphopenia (decreased/absent nonfunctional T cells), normal-to-increased B cells (B+), hypogammaglobulinemia that worsens with age, absent lymphocyte proliferative response to mitogens, dermatitis/eczema, lymphadenopathy, and B-cell lymphoma in one patient. NK cells are normal or low. Severity is severe; the course is rapidly life-threatening without HSCT; expressivity is somewhat variable across the few cases. Typical opportunistic organisms include *Pneumocystis jirovecii*, CMV, and other viral/fungal pathogens.

| Phenotype | HPO term | Frequency/notes |
|---|---|---|
| Severe combined immunodeficiency | HP:0004430 | Defining feature |
| Reduced T-cell count / T lymphopenia | HP:0410354 / HP:0005415 | Core; T− |
| Pneumonia | HP:0002090 | Recurrent |
| Recurrent respiratory infections | HP:0002205 | Frequent |
| Decreased circulating IgG level | HP:0004315 | Progressive with age |
| Decreased circulating IgA level | HP:0002720 | Variable |
| Abnormal T cell proliferation (mitogen-unresponsive) | HP:0031381 | Consistent |
| Eczema / inflammatory skin abnormality | HP:0000964 / HP:0011123 | Reported |
| Lymphadenopathy | HP:0002716 | Reported |
| B-cell lymphoma | HP:0012191 | 1 patient |

> "The population of peripheral blood T lymphocytes was greatly diminished and unresponsive to mitogen stimulation." — [PMID: 10700239](https://pubmed.ncbi.nlm.nih.gov/10700239/)
>
> "Despite normal B-lymphocyte numbers, serum immunoglobulin levels decreased with age." — [PMID: 10700239](https://pubmed.ncbi.nlm.nih.gov/10700239/)

### Finding 8 — Gene/protein annotation: *PTPRC*/CD45 (UniProt P08575) with GO terms

Causal gene *PTPRC* (**HGNC:9666**; NCBI Gene 5788; Ensembl ENSG00000081237; chromosome 1q31.3; OMIM gene 151460). Protein: Receptor-type tyrosine-protein phosphatase C (CD45, leukocyte common antigen), **UniProt P08575**, EC 3.1.3.48. It is a single-pass type I transmembrane protein with a large N-glycosylated extracellular domain (residues 26–577; two fibronectin type-III domains at 391–483 and 484–576), a transmembrane helix (578–598), and a large cytoplasmic region (599–1306) containing two tandem PTP domains — a membrane-proximal, catalytically active D1 (653–912) and a membrane-distal, regulatory/inactive D2 (944–1228). Alternative splicing of exons 4/5/6 (A/B/C) generates the CD45RA, RB, RC, and RO isoforms. Disease-causing variants are germline loss-of-function (large deletion + splice IVS13; homozygous in-frame 6-bp deletion Glu339_Tyr340del) with autosomal recessive inheritance and complete penetrance.

**Suggested GO annotations:**
- **Molecular Function:** transmembrane receptor protein tyrosine phosphatase activity (GO:0005001); protein tyrosine phosphatase activity (GO:0004725); protein tyrosine kinase inhibitor activity (GO:0030292)
- **Biological Process:** T cell receptor signaling pathway (GO:0050852); positive regulation of antigen receptor-mediated signaling pathway (GO:0050857); T cell differentiation (GO:0030217); T cell activation (GO:0042110); B cell receptor signaling pathway (GO:0050853); B cell differentiation (GO:0030183); natural killer cell differentiation (GO:0001779); DN2 thymocyte differentiation (GO:1904155); protein dephosphorylation (GO:0006470)
- **Cellular Component:** external side of plasma membrane (GO:0009897); membrane raft (GO:0045121); plasma membrane (GO:0005886)

> "a loss of glutamic acid 339 and tyrosine 340 in the first fibronectin type III module of the extracellular domain of CD45, is associated with failure of surface expression of CD45" — [PMID: 11145714](https://pubmed.ncbi.nlm.nih.gov/11145714/)

### Finding 9 — Anatomical structures, cell types, and subcellular localization (UBERON / CL / GO-CC)

CD45 is expressed on all nucleated hematopoietic cells (leukocyte common antigen). The primary affected system is the immune/hematolymphoid system (**UBERON:0002405** immune system; **UBERON:0002390** hematopoietic system). Primary organs/tissues: **thymus (UBERON:0002370)** — the site where T-cell development arrests at the DP→SP transition; **bone marrow (UBERON:0002371)** — hematopoietic origin; **spleen (UBERON:0002106)**; **lymph nodes (UBERON:0000029**, clinical lymphadenopathy); **peripheral blood (UBERON:0000178)**. Secondary/complication organs: **lung (UBERON:0002048**; pneumonia) and **skin (UBERON:0002097**; dermatitis).

**Cell types (Cell Ontology):** T cell (CL:0000084), thymocyte (CL:0000893), CD4/CD8 double-positive thymocyte (CL:0000807), mature αβ T cell (CL:0000791), B cell (CL:0000236), natural killer cell (CL:0000623), leukocyte/hematopoietic cell (CL:0000738).

**Subcellular localization (GO-CC):** plasma membrane (GO:0005886), external side of plasma membrane (GO:0009897), membrane raft/microdomain (GO:0045121, GO:0098857) where CD45 regulates raft-associated Src kinases.

> "T cell development is significantly inhibited in CD45-null animals at two distinct stages." — [PMID: 8666928](https://pubmed.ncbi.nlm.nih.gov/8666928/)
>
> "CD45 is an abundant transmembrane tyrosine phosphatase, expressed on all leukocytes" — [PMID: 11145714](https://pubmed.ncbi.nlm.nih.gov/11145714/)

### Finding 10 — Inheritance, epidemiology, and prevention

Inheritance is **autosomal recessive with complete penetrance** for biallelic loss-of-function; heterozygous carriers are clinically unaffected. IMD105 is **ultra-rare** — only ~3 unrelated patients are reported in OMIM — so no disease-specific prevalence/incidence exists; it is a molecularly rare subtype within the broader SCID category (overall SCID incidence ~1:46,753 to ~1:58,000 live births by TREC screening). Consanguinity/homozygosity is a risk context (e.g., the homozygous 6-bp deletion). No sex predilection is expected (autosomal). There is no environmental cause; infections are downstream consequences (opportunistic *Pneumocystis jirovecii*, CMV, other viruses/fungi), not triggers.

**Prevention/management:** (1) secondary prevention via universal newborn TREC screening for presymptomatic detection; (2) genetic counseling for recurrence risk (25% for carrier couples), carrier testing of relatives, and prenatal/preimplantation genetic testing when the familial *PTPRC* variants are known; (3) tertiary prevention of complications pre-HSCT — protective isolation, antimicrobial/anti-*Pneumocystis* prophylaxis, IVIG replacement, only irradiated/CMV-safe/leukoreduced blood products, and strict avoidance of live vaccines (BCG, rotavirus, MMR, VZV, OPV).

> "corresponding to an overall incidence of 1:46,753 live births" — [PMID: 42079620](https://pubmed.ncbi.nlm.nih.gov/42079620/)
>
> "a homozygous 6-bp deletion in the gene encoding CD45" — [PMID: 11145714](https://pubmed.ncbi.nlm.nih.gov/11145714/)

---

## Section-by-Section Report

### 1. Disease Information

IMD105 is an autosomal recessive severe combined immunodeficiency of the T−B+NK-variable type caused by complete deficiency of the leukocyte common antigen CD45 (gene *PTPRC*). It presents in early infancy with life-threatening opportunistic infections. **Key identifiers:** OMIM #619924 (phenotype), OMIM 151460 (gene); MONDO:0800104; part of OMIM Phenotypic Series PS601457 (autosomal recessive SCID). ICD-10 D81.x (combined immunodeficiencies); ICD-11 4A01.0Y (other combined immunodeficiencies). MeSH: Severe Combined Immunodeficiency (D016511); no CD45-specific MeSH descriptor. **Synonyms:** CD45 deficiency; SCID due to CD45 deficiency; leukocyte common antigen deficiency; PTPRC deficiency; T-cell-negative, B-cell-positive SCID due to CD45 deficiency. The information is derived from **aggregated disease-level resources** (OMIM, primary case reports) rather than EHR — the entire literature rests on ~3 individually reported patients plus mouse-model data.

### 2. Etiology

**Causal factor:** purely genetic — biallelic loss-of-function mutations in *PTPRC* (chromosome 1q31.3). **Genetic risk factors:** the only causal factor is inheriting two damaging *PTPRC* alleles; consanguinity increases homozygosity risk. There are **no environmental risk factors** for disease causation. The recurrent opportunistic infections (*Pneumocystis jirovecii*, CMV, other viruses/fungi) are downstream consequences of immune failure, not triggers. **Protective factors:** none genetic beyond simply not carrying biallelic null alleles. **Gene–environment interactions:** not applicable to disease causation; environment determines which opportunistic infections manifest. Note: the *PTPRC* **C77G** and A138G polymorphisms are isoform-altering *susceptibility* alleles for autoimmune/infectious diseases and are **not** part of IMD105 etiology (Finding 4).

### 3. Phenotypes

See Finding 7 table. Phenotype **onset is neonatal-to-early-infancy** (~2 months); **severity is severe**; **progression is progressive and rapidly life-threatening** without HSCT. Laboratory abnormalities (T lymphopenia, absent mitogen response, progressive hypogammaglobulinemia, absent surface CD45) are the most consistent features. Quality-of-life impact is profound: without treatment the disease is uniformly fatal in early childhood; with successful HSCT, survivors may achieve durable immune reconstitution. Behavioral phenotypes are not a feature.

### 4. Genetic / Molecular Information

**Causal gene:** *PTPRC* (HGNC:9666; NCBI Gene 5788; Ensembl ENSG00000081237; OMIM 151460). **Pathogenic variants reported:** (i) large deletion on one allele + IVS13 donor splice-site point mutation (compound heterozygous; Kung 2000); (ii) homozygous in-frame 6-bp deletion p.Glu339_Tyr340del in the first fibronectin type III module (Tchilian 2001). **Variant classes:** structural (large deletion), splice-site, and in-frame indel — all loss-of-function. **Functional consequence:** loss of function → absent or non-functional surface CD45. **Classification:** pathogenic per ACMG (null/LOF in a gene with established LOF mechanism, segregating with recessive disease). **Allele frequency:** the disease alleles are private/ultra-rare (absent from gnomAD at appreciable frequency). **Origin:** germline. **Modifier genes:** none established. **Epigenetics/chromosomal abnormalities:** none specific to IMD105 (though the causal lesions include a submicroscopic deletion detectable in principle by high-resolution methods).

### 5. Environmental Information

No environmental, lifestyle, toxicological, or radiation factors cause IMD105. **Infectious agents** are relevant only as downstream opportunistic complications — *Pneumocystis jirovecii*, cytomegalovirus, and other viral/fungal/opportunistic pathogens typical of SCID. Live vaccine organisms (e.g., BCG, rotavirus, OPV) pose iatrogenic infection risk and must be avoided.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Biallelic loss-of-function *PTPRC* mutation **leads to** absent or non-functional CD45 protein at the leukocyte surface (demonstrated: absent surface CD45; PMID 11145714).
2. Absence of CD45 phosphatase activity **results in** failure to dephosphorylate the inhibitory C-terminal tyrosine (Y505) of the Src-family kinase Lck (and Fyn) (demonstrated biochemically; PMID 32794043).
3. Persistent inhibitory phosphorylation **causes** Lck to remain in its closed, autoinhibited conformation, so active Lck is not generated (mechanistic, in vitro/reconstitution evidence).
4. Loss of active Lck **leads to** failure of TCR/CD3 (and BCR) proximal phosphorylation and ZAP70 activation — i.e., collapse of antigen-receptor signal transduction (PMID 10700239).
5. Failed TCR signaling in the thymus **results in** an arrest of T-cell development at the double-positive → single-positive transition (and reduced DN→DP), impairing both positive and negative selection (demonstrated in mouse; PMID 8666928).
6. Thymic developmental block **leads to** profound peripheral T-cell lymphopenia with non-functional, mitogen-unresponsive T cells (T−) (PMID 10700239).
7. Absent T-cell help, together with intrinsic BCR-signaling impairment, **causes** progressive hypogammaglobulinemia despite normal/increased B-cell numbers (B+) (PMID 10700239).
8. The resulting combined immune failure **leads to** early-infancy recurrent, severe, opportunistic infections and, in one case, lymphoproliferation/B-cell lymphoma — clinical SCID (inferred branch for lymphoma).

**Molecular pathways:** TCR and BCR signaling (Reactome/KEGG "T cell receptor signaling pathway"); the Csk–CD45–Lck regulatory node. **Cellular processes:** thymocyte selection (positive/negative selection), lymphocyte development and activation, TCR-induced apoptosis (defective). **Protein dysfunction:** loss of function of a tandem-domain receptor tyrosine phosphatase; extracellular fibronectin-III lesion abolishes surface expression. **Immune system involvement:** immunodeficiency (not autoimmunity) is the core. **Cell types (CL):** double-positive thymocyte (CL:0000807), T cell (CL:0000084), B cell (CL:0000236), NK cell (CL:0000623). **GO biological processes:** GO:0050852 (TCR signaling), GO:0030217 (T cell differentiation), GO:0006470 (protein dephosphorylation). Upstream = the *PTPRC* lesion and CD45 loss; downstream = defective thymopoiesis, infections, and antibody failure.

### 7. Anatomical Structures Affected

See Finding 9. **Primary organs:** thymus (developmental arrest), bone marrow, spleen, lymph nodes, peripheral blood — the hematolymphoid system. **Secondary/complication organs:** lung (pneumonia) and skin (dermatitis). **Cell/tissue level:** all nucleated hematopoietic cells express CD45; the functional lesion falls hardest on thymocytes and T cells. **Subcellular:** plasma membrane and membrane rafts. Involvement is systemic/bilateral (not lateralized).

### 8. Temporal Development

**Onset:** neonatal-to-early-infancy (recurrent infections from ~2 months). **Onset pattern:** subacute/insidious, becoming acute with severe infection. **Progression:** rapidly progressive and, without immune reconstitution, fatal in early childhood. **Course:** chronic and progressive with acute infectious exacerbations. **Remission:** only treatment-induced, via successful HSCT (durable immune reconstitution). **Critical period:** the neonatal window before infectious/organ complications — pre-symptomatic detection by newborn screening and early transplant define outcome (Finding 6).

### 9. Inheritance and Population

**Inheritance:** autosomal recessive; complete penetrance for biallelic LOF; carriers unaffected. **Expressivity:** somewhat variable across the few cases (e.g., lymphoma in one). **Epidemiology:** ultra-rare — only ~3 unrelated reported families; no disease-specific prevalence. Sits within overall SCID incidence of ~1:46,753–1:58,000 live births by TREC screening. **Consanguinity** is a contributing context (homozygous 6-bp deletion). **No founder effect** established. **Sex ratio** ~1:1 (autosomal). **Carrier frequency** not defined given rarity. No population enrichment documented.

### 10. Diagnostics

**Newborn screening:** TREC assay on dried blood spots (low/absent TRECs in T-lymphopenic infants). **Confirmatory clinical tests:** lymphocyte immunophenotyping by flow cytometry (T−/B+/NK-variable) — **absent surface CD45 on all leukocytes is the disease-specific pointer**; mitogen proliferation assays (absent); serum immunoglobulins (progressive hypogammaglobulinemia). **Genetic testing:** *PTPRC* single-gene sequencing, SCID/IEI gene panels, or WES/WGS; deletion-spanning methods (MLPA/CMA) needed to detect the large-deletion allele. **Differential diagnosis:** other T−B+ SCID (IL2RG/X-linked, JAK3, IL7R deficiency) — distinguished by preserved surface CD45 in those disorders and by the specific gene defect; also RAG1/2, ADA, and reticular dysgenesis for broader SCID. **Screening:** newborn TREC screening; cascade carrier testing in families.

### 11. Outcome / Prognosis

**Untreated:** uniformly fatal in early childhood. **With HSCT:** curative, with survival strongly dependent on timing of diagnosis. Reported 2-year OS: 71.4% (early/NBS-diagnosed) vs 29.2% (late clinically-diagnosed) SCID; single-center OS 68% overall (93% for NBS-identified) (Finding 6). **Complications:** severe opportunistic infections, failure to thrive, and (in one CD45 case) B-cell lymphoma; transplant-related GVHD and graft failure. **Prognostic factors:** age/timing of diagnosis, pre-transplant infection status, donor matching, stem-cell source, and use of conditioning.

### 12. Treatment

**Definitive:** allogeneic HSCT — the only curative therapy (NCIT: Hematopoietic Cell Transplantation, C15431; Allogeneic Bone Marrow Transplantation). **Supportive/bridging:** immunoglobulin replacement (IVIG; NCIT C509), antimicrobial/antifungal/anti-*Pneumocystis* prophylaxis (e.g., trimethoprim-sulfamethoxazole), protective isolation, irradiated/CMV-safe/leukoreduced blood products, avoidance of live vaccines. **Pharmacogenomics:** conditioning agents (e.g., busulfan) are dose-adjusted; not *PTPRC*-specific. **Advanced/experimental:** gene therapy is investigational for other SCID subtypes but **not established for *PTPRC***; antibody-based (anti-CD45-saporin) non-genotoxic conditioning is under study in models (PMID 32387109) but not a *PTPRC* therapy. Treatment strategy is genotype-agnostic beyond confirming diagnosis: proceed rapidly to HSCT with optimal supportive care.

### 13. Prevention

**Primary prevention:** not possible (monogenic); genetic counseling and reproductive options (PGT/prenatal testing) reduce recurrence for known-carrier families (25% recurrence risk). **Secondary prevention:** universal newborn TREC screening for presymptomatic detection — the single most impactful intervention (Findings 5–6). **Tertiary prevention:** anti-infective prophylaxis, IVIG, isolation, safe blood products, and avoidance of live vaccines to prevent complications before HSCT. **Immunization:** live vaccines contraindicated; killed vaccines generally ineffective pre-reconstitution. **Counseling:** genetic counseling and cascade carrier testing.

### 14. Other Species / Natural Disease

**Taxonomy / orthologs:** human *PTPRC* (NCBI Gene 5788); mouse *Ptprc* (NCBI Gene 19264; NCBI Taxon 10090). CD45 is highly conserved across mammals. **Natural disease:** no well-characterized spontaneous CD45-deficiency disease is documented in companion animals in OMIA within this investigation; CD45 biology is conserved and disease models are engineered rather than natural. **Comparative biology:** the mouse knockout closely mirrors the human immunophenotype, supporting strong evolutionary conservation of the CD45→Lck→TCR mechanism (Finding 3). **Zoonotic potential:** none (genetic disorder).

### 15. Model Organisms

**Mouse (*Mus musculus*)** is the principal model: the CD45/*Ptprc*-null knockout (Byth 1996) recapitulates T−B+ immunophenotype with a two-stage thymic block, defective negative selection/superantigen deletion, and CD45's role in enhancing positive selection (Finding 3). **Model types:** germline knockout; transgenic CD45RO-reconstitution lines used to dissect isoform effects. **Phenotype recapitulation:** high for the immunophenotype and developmental block. **Limitations:** mouse strain background and the engineered nature of alleles differ from the human private mutations; species differences in isoform usage; the lymphoma predisposition seen in one human patient is not a defining mouse phenotype. **Resources:** MGI (*Ptprc*), IMPC/IMSR for allele availability. In vitro reconstitution systems (supported lipid bilayers; PMID 25128530) and cell lines elucidate the CD45/Lck/TCR clustering mechanism.

---

## Mechanistic Model / Interpretation

```
 Biallelic PTPRC LOF mutation
   (large del + IVS13 splice; or homozygous 6-bp del, Glu339_Tyr340del)
                │  leads to
                ▼
 Absent / non-functional surface CD45 phosphatase
                │  results in
                ▼
 Failure to dephosphorylate Lck inhibitory Y505  ◄── Csk keeps Y505 phosphorylated
                │  causes                              (CD45 normally counteracts Csk)
                ▼
 Lck locked in closed, autoinhibited conformation  → no active Lck
                │  leads to
                ▼
 Collapse of TCR/CD3 (and BCR) proximal signaling (ZAP70 not activated)
                │  results in
      ┌─────────┴───────────────────────────┐
      ▼ (thymus)                             ▼ (periphery / B lineage)
 T-cell development arrests at DP→SP    Impaired T-cell help + BCR signaling
 (± reduced DN→DP); defective            → progressive hypogammaglobulinemia
 positive & negative selection             despite NORMAL/INCREASED B cells (B+)
      │                                     │
      ▼  leads to                           ▼
 Profound peripheral T-lymphopenia,    Antibody failure
 mitogen-unresponsive T cells (T−)
      └──────────────┬──────────────────────┘
                     ▼  leads to
   Early-infancy severe recurrent opportunistic infections
   (Pneumocystis, CMV, viral/fungal); ± B-cell lymphoma (1 case)
                     ▼  fatal in early childhood without
             ────────────────────────────────
             Allogeneic HSCT  → durable immune reconstitution (cure)
```

CD45 sits at a signaling rheostat: it **activates** Lck by removing the inhibitory phosphate (the dominant net effect in thymocytes) but can also **dephosphorylate the TCR** — a negative role blunted by CD45's spatial exclusion from TCR clusters. In complete deficiency the activating role is lost with no compensation, so the net outcome is a hard block in T-cell development. The mouse knockout, three human patients, and biochemical/reconstitution studies converge on the same causal chain, giving unusually high mechanistic confidence for such an ultra-rare disease.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [10700239](https://pubmed.ncbi.nlm.nih.gov/10700239/) | *Mutations in the tyrosine phosphatase CD45 gene in a child with SCID* | Founding human case; CD45 regulates Src kinases; T−B+ phenotype, progressive hypogammaglobulinemia |
| [11145714](https://pubmed.ncbi.nlm.nih.gov/11145714/) | *A deletion in the gene encoding the CD45 antigen in a patient with SCID* | Second human case; homozygous 6-bp del; absent surface CD45; locus 1q31-32 |
| [8666928](https://pubmed.ncbi.nlm.nih.gov/8666928/) | *CD45-null transgenic mice…* | Mouse knockout recapitulates T−B+ phenotype and two-stage thymic block |
| [32794043](https://pubmed.ncbi.nlm.nih.gov/32794043/) | *The role of competing mechanisms on Lck regulation* | CD45/Csk balance sets Lck activation state |
| [25128530](https://pubmed.ncbi.nlm.nih.gov/25128530/) | *Phosphatase CD45 both positively and negatively regulates TCR phosphorylation* | Dual (activating/inhibitory) CD45 role; spatial exclusion |
| [21507955](https://pubmed.ncbi.nlm.nih.gov/21507955/) | *Disease-associated polymorphism alters CD45 splicing (hnRNPs)* | Mechanism of C77G — distinct from LOF SCID |
| [17903220](https://pubmed.ncbi.nlm.nih.gov/17903220/) | *Altered CD45 isoform expression in C77G carriers…* | C77G = autoimmune/infectious susceptibility, not SCID |
| [18312479](https://pubmed.ncbi.nlm.nih.gov/18312479/) | *PTPRC (CD45) variation and disease association…* | C77G/A138G isoform-altering susceptibility alleles |
| [42079620](https://pubmed.ncbi.nlm.nih.gov/42079620/) | *SCID newborn screening, Catalonia* | TREC screening; incidence 1:46,753 |
| [40374985](https://pubmed.ncbi.nlm.nih.gov/40374985/) | *Newborn screening + early treatment in SCID* | HCT only cure; 71.4% vs 29.2% 2-yr OS by timing |
| [39900265](https://pubmed.ncbi.nlm.nih.gov/39900265/) | *HSCT outcome & NBS impact (single center)* | NBS-identified OS 93% vs clinical |
| [32387109](https://pubmed.ncbi.nlm.nih.gov/32387109/) | *Anti-CD45-saporin conditioning (RAG mice)* | Investigational non-genotoxic conditioning (model, not PTPRC therapy) |

Supporting mechanistic papers on Lck regulation and TCR clustering (PMIDs 28735895, 33225946, 25127865, 30745330, 25658352, 9052865, 9203971) reinforce the CD45→Lck→TCR axis and thymic selection biology.

---

## Limitations and Knowledge Gaps

- **Extreme rarity:** the human disease rests on only ~3 unrelated patients, so phenotype frequencies, expressivity range, and outcome statistics for *PTPRC*-specific SCID are imprecise; most prognosis/screening data are extrapolated from the broader SCID category.
- **No disease-specific epidemiology:** prevalence/incidence, carrier frequency, and any founder effects are unknown.
- **Genotype–phenotype correlation** cannot be established with so few alleles; the single lymphoma case may be incidental or mechanistically linked (uncertain).
- **Therapy:** no *PTPRC*-specific gene/cell therapy exists; HSCT outcome data are not CD45-specific.
- **Ontology mapping** for a few HPO/GO terms should be verified against current ontology releases before database ingestion.
- **Natural animal disease:** no confirmed spontaneous CD45-deficiency disease documented in OMIA within this investigation.

## Proposed Follow-up Experiments / Actions

1. **Query OMIM/ClinVar/HGMD directly** for any additional *PTPRC* SCID cases and variants beyond the three founding families to update the variant table and gnomAD allele-frequency checks.
2. **Curate a differential-diagnosis matrix** for T−B+ SCID (IL2RG, JAK3, IL7R vs PTPRC), emphasizing the flow-cytometry discriminator of absent surface CD45.
3. **Assemble ontology cross-checks** (HPO frequency annotations, GO evidence codes, UBERON/CL IDs) against current ontology versions for database ingestion.
4. **Search GTR/GeneReviews** for CD45-specific transplant management protocols and any conditioning-regimen recommendations.
5. **Monitor ClinicalTrials.gov** for gene-editing/HSCT trials that could extend to *PTPRC* SCID, and track anti-CD45-antibody conditioning translation.
6. **Retrieve MGI/IMPC records** for all *Ptprc* alleles to formalize the model-organism annotation (phenotype recapitulation and limitations).

---

*Report compiled from 10 confirmed findings and 26 reviewed papers across a 5-iteration autonomous investigation. Evidence sources: human clinical case reports, mouse knockout studies, in vitro/biochemical reconstitution, and population screening cohorts.*


## Artifacts

- [OpenScientist final report](Immunodeficiency_105-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_105-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 23 |
| Quoted claims found in source | 23 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 6 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0004315` (1 mention) - the report calls it "Decreased circulating IgG level"; HP calls it **Decreased circulating IgG concentration**, and lists "Decreased circulating IgG level" among its other names
- `HP:0002720` (1 mention) - the report calls it "Decreased circulating IgA level"; HP calls it **Decreased circulating IgA concentration**, and lists "Decreased circulating IgA level" among its other names
- `HP:0031381` (1 mention) - the report calls it "Abnormal T cell proliferation (mitogen-unresponsive)"; HP calls it **Decreased mitogen-induced T-cell proliferation**, and lists "Reduced lymphocyte proliferation to mitogen" among its other names
- `GO:0005001` (1 mention) - the report calls it "Molecular Function:** transmembrane receptor protein tyrosine phosphatase activity"; GO calls it **transmembrane receptor protein tyrosine phosphatase activity**
- `GO:0050852` (2 mentions) - the report calls it "Biological Process:** T cell receptor signaling pathway", "TCR signaling"; GO calls it **T cell receptor signaling pathway**, and lists "TCR signaling pathway" among its other names
- `GO:0009897` (2 mentions) - the report calls it "Cellular Component:** external side of plasma membrane"; GO calls it **external side of plasma membrane**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0050852` - called "Biological Process:** T cell receptor signaling pathway", "TCR signaling"

45 of 46 terms resolved to a current term; the rest could not be looked up either way.