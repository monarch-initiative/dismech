---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T08:37:57.318227'
end_time: '2026-08-19T08:55:22.770447'
duration_seconds: 1045.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Intellectual Developmental Disorder, Autosomal Dominant 72
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
citation_count: 11
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 5
  relevance_assessed: 11
  on_topic: 6
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intellectual_Developmental_Disorder_Autosomal_Dominant_72-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intellectual_Developmental_Disorder_Autosomal_Dominant_72-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder, Autosomal Dominant 72
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder, Autosomal Dominant 72** covering all of the
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

# Intellectual Developmental Disorder, Autosomal Dominant 72 (MRD72): A Comprehensive Disease Characterization

**Disease:** Intellectual Developmental Disorder, Autosomal Dominant 72 (MRD72)
**Causal gene:** *SRRM2* (SR-related splicing factor / SRm300), 16p13.3
**Key identifiers:** OMIM #620439 · MONDO:0957397 · ORPHA:652487 · DO:0061045 · MedGen C5830612
**Category:** Genetic (autosomal dominant neurodevelopmental disorder)

> **IMPORTANT DISEASE-IDENTITY NOTE.** "Intellectual developmental disorder, autosomal dominant 72" (**MRD72**, OMIM **#620439**) is caused by **SRRM2** haploinsufficiency. It must **not** be confused with the *ZBTB7A*-related disorder (**MNDLFH**, OMIM 619769 — macrocephaly, neurodevelopmental delay, lymphoid hyperplasia, persistent fetal hemoglobin), a distinct entity. All content below refers to the **SRRM2** disorder unless explicitly labeled otherwise (see Section 16).

---

## Summary

**Intellectual Developmental Disorder, Autosomal Dominant 72 (MRD72) is a rare autosomal dominant neurodevelopmental disorder caused by heterozygous loss-of-function (haploinsufficiency) of *SRRM2***, a gene on chromosome 16p13.3 encoding the SR-related splicing factor SRm300 (SRRM2). Affected individuals typically carry *de novo* protein-truncating variants (frameshift and nonsense) or whole-gene deletions and present with a relatively mild, non-progressive picture dominated by developmental delay with prominent speech delay, autistic and/or attention-deficit/hyperactivity (ADHD) features, overfriendliness, generalized hypotonia, overweight, and mild facial dysmorphism. Intellectual disability, when present, is generally mild and variable.

Mechanistically, SRRM2 (with its partner SON) is one of the two core scaffolding proteins that nucleate **nuclear speckles** — membraneless nuclear organelles that concentrate the pre-mRNA splicing machinery. *SRRM2* is among the most loss-of-function-constrained genes in the human genome (gnomAD pLI = 1.0, LOEUF ≈ 0.18), and complete loss is embryonic-lethal in mouse and *C. elegans*; the human disorder therefore arises specifically from a **50% reduction in gene dosage (haploinsufficiency)** rather than biallelic loss. MRD72 belongs to an emerging family of "**nuclear-speckle spliceosomopathies**," whose closest relative is ZTTK syndrome, caused by haploinsufficiency of SON — SRRM2's obligate scaffolding partner.

**A critical clarification runs through this report.** The name "Intellectual Developmental Disorder, Autosomal Dominant 72" refers specifically to the *SRRM2*-related disorder (OMIM #620439). It should NOT be confused with the *ZBTB7A*-related disorder (MNDLFH; OMIM #619769), which features macrocephaly, adenoid/pharyngeal lymphoid overgrowth, and elevated fetal hemoglobin. Because both are autosomal dominant neurodevelopmental disorders and secondary-source naming can be ambiguous, the early phase of this investigation initially characterized *ZBTB7A*; iterations 3–5 corrected course to *SRRM2*. This report describes MRD72 (=*SRRM2*) and flags the *ZBTB7A* material as a distinct entity/differential where relevant (Section 16).

---

## Section 1 — Disease Information

**What is the disease?** MRD72 is a Mendelian, autosomal dominant, neurodevelopmental disorder in the OMIM "Intellectual developmental disorder, autosomal dominant" (MRD) series. It is defined by heterozygous loss-of-function variation in *SRRM2* and characterized by mild developmental delay with disproportionate speech delay, neurobehavioral features (autism-spectrum and ADHD traits, overfriendliness), hypotonia, a tendency to overweight, and subtle dysmorphism ([PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/)).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (disease) | #620439 |
| OMIM (gene *SRRM2*) | 606032 |
| MONDO | MONDO:0957397 |
| Orphanet | ORPHA:652487 |
| Disease Ontology | DO:0061045 |
| MedGen | C5830612 |
| HGNC (gene) | HGNC:16639 |
| Cytoband | 16p13.3 |

**Synonyms / alternative names:** MRD72; SRRM2-related neurodevelopmental disorder; SRRM2 haploinsufficiency disorder; *SRRM2*-related intellectual disability.

**Source of information:** The disease-level description derives from **aggregated resources and case series** — principally the defining cohort of Cuinat et al. (2022; n = 22), plus subsequent structural-variant reports and large de-novo-variant meta-analyses — rather than EHR-based population phenotyping.

---

## Section 2 — Etiology

**Primary cause (genetic).** MRD72 is a monogenic disorder caused by **heterozygous loss-of-function variants in *SRRM2***. Cuinat et al. identified 22 patients with LoF *SRRM2* variants — 12 frameshift, 8 nonsense, and 2 microdeletions (66 kb and 270 kb) — and "established *SRRM2* as a gene responsible for a rare neurodevelopmental disease" ([PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/)). The mechanism is **haploinsufficiency** (≈50% reduction in functional SRRM2 protein).

> "Here, we report on 22 patients with LoF variants in SRRM2 and provide a description of the phenotype. Molecular analysis identified 12 frameshift variants, 8 nonsense variants, and 2 microdeletions of 66 kb and 270 kb." — Cuinat et al. ([PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/))

**Genetic risk factors.** The single, sufficient causal factor is a pathogenic/likely-pathogenic heterozygous *SRRM2* LoF allele, nearly always ***de novo***. *SRRM2* is "predicted to be highly intolerant to loss of function (LoF) and very conserved through evolution" ([PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/)). No common susceptibility loci or polygenic contribution are described.

**Environmental risk factors / protective factors / gene–environment interactions.** None established. As a *de novo*, high-penetrance Mendelian disorder, there are no known environmental triggers, protective exposures, dietary factors, or GxE interactions. Record as **not applicable / not reported**.

---

## Section 3 — Phenotypes

The core phenotype derives from Cuinat et al. (2022) and the OMIM clinical synopsis for #620439. Severity is generally mild and the course non-progressive (a static-encephalopathy pattern typical of neurodevelopmental disorders).

> "The patients presented with a mild developmental delay, predominant speech delay, autistic or attention-deficit/hyperactivity disorder features, overfriendliness, generalized hypotonia, overweight, and dysmorphic facial features. Intellectual disability was variable and mild when present." — Cuinat et al. ([PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/))

| Phenotype | Type | Onset | Severity | Suggested HPO term |
|---|---|---|---|---|
| Global developmental delay | Clinical sign | Infancy/early childhood | Mild | HP:0001263 |
| Speech/language delay (predominant) | Clinical sign | Early childhood | Prominent, often disproportionate | HP:0000750 |
| Intellectual disability | Clinical sign | Childhood | Mild, variable, sometimes absent | HP:0001249 / HP:0001256 (mild) |
| Autistic behavior / ASD features | Behavioral | Early childhood | Variable | HP:0000729 |
| Attention deficit / hyperactivity | Behavioral | Childhood | Variable | HP:0007018 |
| Overfriendliness / abnormal social behavior | Behavioral | Childhood | Variable | HP:0100024 |
| Generalized hypotonia | Clinical sign | Infancy | Mild–moderate | HP:0001290 |
| Overweight / obesity | Physical | Childhood onward | Variable | HP:0001513 |
| Dysmorphic facial features | Physical | Congenital/childhood | Subtle/variable | HP:0001999 |

**Age of onset:** infancy (hypotonia) to early childhood (developmental/speech delay). **Progression:** stable/non-progressive (developmental, not degenerative). **Frequency among affected:** developmental/speech delay and neurobehavioral features are the most consistent; overweight, hypotonia and dysmorphism are frequent but variable. Precise per-feature percentages are limited by the small cohort (n = 22).

**Quality-of-life impact:** driven mainly by communication impairment (speech delay), learning-support needs, and neurobehavioral features (ASD/ADHD), affecting schooling, social integration, and independence. No disease-specific QoL instrument (EQ-5D/SF-36/PROMIS) data exist for MRD72; impact is inferred from the mild-ID/ASD profile.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *SRRM2* (Serine/Arginine Repetitive Matrix 2), also **SRm300**; OMIM 606032; HGNC:16639; 16p13.3. A 15-exon gene encoding a large (~2,752-amino-acid) SR-related splicing factor.

**Pathogenic variant spectrum.** In the defining cohort (n = 22), variants were **loss-of-function**: 12 frameshift, 8 nonsense, and 2 microdeletions (66 kb, 270 kb) ([PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/)). Whole-gene deletions are independently recurrent: Pagnamenta et al. (2023) reported *de novo* whole-gene *SRRM2* deletions of 248–482 kb in 4 individuals from the 100,000 Genomes Project, with distal breakpoints clustering in a **144-kb palindrome ~75 kb upstream of *SRRM2*** — a 16p13.3 structure predisposing to recurrent complex structural variation ([PMID: 40225164](https://pubmed.ncbi.nlm.nih.gov/40225164/)).

| Variant class | Representative evidence | Consequence |
|---|---|---|
| Frameshift (n = 12) | Cuinat 2022 | LoF / haploinsufficiency |
| Nonsense (n = 8) | Cuinat 2022 | LoF / haploinsufficiency |
| Intragenic microdeletion (66 kb, 270 kb) | Cuinat 2022 | LoF / haploinsufficiency |
| Whole-gene deletion (248–482 kb) | Pagnamenta 2023 | LoF / haploinsufficiency |

- **Variant classification:** pathogenic / likely pathogenic per ACMG/AMP (PVS1 applies to a haploinsufficient gene).
- **Variant type/class:** predominantly protein-truncating (frameshift, nonsense) plus copy-number losses (structural).
- **Allele frequency:** absent/vanishingly rare in gnomAD (private *de novo* alleles). *SRRM2* is extremely LoF-depleted (below).
- **Somatic vs germline:** germline, almost always **de novo**.
- **Functional consequence:** **loss of function (haploinsufficiency)**.

**Constraint metrics.** *SRRM2* is one of the most LoF-intolerant genes in the genome: gnomAD **pLI = 1.0**, observed/expected pLoF ≈ 0.06 (≈7 observed vs ≈111 expected pLoF SNVs), **LOEUF ≈ 0.18**, **RVIS ≈ −4.5** (~15th-most intolerant of ~17,000 genes). **ClinGen Dosage Sensitivity** assigns a **haploinsufficiency score of 3** (sufficient evidence). The Kaplanis/DDD meta-analysis of ~31,000 neurodevelopmental trios identified *SRRM2* as one of **28 genes significantly enriched for de novo variants**, driven by protein-truncating variants. Cuinat et al. note the gene "has not been previously reported in constitutive human disease" ([PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/)).

**Modifier genes / epigenetics.** No specific modifiers or epigenetic mechanisms characterized for MRD72 (not reported).

**Chromosomal abnormalities.** Recurrent 16p13.3 deletions encompassing *SRRM2* arise via non-allelic homologous recombination facilitated by the upstream 144-kb palindrome ([PMID: 40225164](https://pubmed.ncbi.nlm.nih.gov/40225164/)); detectable by chromosomal microarray (CMA).

---

## Section 5 — Environmental Information

No environmental factors, lifestyle factors, or infectious agents are implicated. MRD72 is a fully genetic, *de novo* dominant disorder. **Not applicable.**

---

## Section 6 — Mechanism / Pathophysiology

**Molecular function of SRRM2.** *SRRM2* encodes **SRm300**, "a splicing factor of the SR-related protein family characterized by its serine- and arginine-enriched domains. It promotes interactions between messenger RNA and the spliceosome catalytic machinery" ([PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/)). SRm300 functions at the catalytic core of the spliceosome (notably around the second transesterification step) as a coactivator of pre-mRNA splicing.

**Nuclear speckle scaffolding — the central mechanism.** SRRM2 is the principal antigen of the classic **SC35 (SC-35) monoclonal antibody** and localizes sharply to nuclear speckles: "the main target of SC35 mAb is SRRM2, a spliceosome-associated protein that sharply localizes to NS" ([PMID: 33095160](https://pubmed.ncbi.nlm.nih.gov/33095160/)). With SON, SRRM2 forms the essential structural core of nuclear speckles: "the core of NS is likely formed by SON and SRRM2." Co-depletion of SON and SRRM2 — or SON depletion when SRRM2's intrinsically disordered regions are deleted — causes near-complete dissolution of nuclear speckles ([PMID: 33095160](https://pubmed.ncbi.nlm.nih.gov/33095160/)). Nuclear speckles concentrate splicing factors and modulate the efficiency/fidelity of pre-mRNA splicing and gene expression.

**Causal chain (upstream → downstream):**

```
De novo heterozygous SRRM2 LoF variant (16p13.3)
          │  (truncating / CNV)
          ▼
~50% reduction of SRm300 protein  ── haploinsufficiency
          │
          ▼
Impaired nuclear-speckle scaffolding (with SON) +
reduced splicing-coactivator capacity
          │
          ▼
Perturbed pre-mRNA splicing / gene-expression programs
in developing neurons (dosage-sensitive)
          │
          ▼
Altered neurodevelopment (neuronal differentiation,
synaptic & network maturation)
          │
          ▼
Clinical MRD72: developmental & speech delay, ASD/ADHD
features, hypotonia, overweight, mild dysmorphism
```

**Cellular processes / cell types.** The dosage-sensitive process is nuclear-speckle-dependent pre-mRNA splicing during neurodevelopment. Because SRRM2 is ubiquitous and essential, the phenotype reflects the particular vulnerability of the developing CNS to reduced splicing-factor dosage. Suggested GO terms: **GO:0000398** (mRNA splicing, via spliceosome), **GO:0016607** (nuclear speck), **GO:0008380** (RNA splicing), **GO:0007399** (nervous system development). Suggested CL terms: **CL:0000540** (neuron), **CL:0000679** (glutamatergic neuron) — cell-type specificity not yet directly established.

**Protein dysfunction.** Truncating variants and deletions reduce full-length SRm300 abundance (loss of function); SRRM2's large IDRs, which drive speckle assembly via multivalent interactions, are lost/reduced. There is no evidence for a dominant-negative or gain-of-function mechanism; haploinsufficiency is supported (ClinGen HI = 3).

**Metabolic / immune / other.** No specific metabolic, immune, oxidative-stress, or fibrotic mechanisms are established. MRD72-specific molecular profiling (transcriptomics/proteomics/metabolomics of patient tissue) has not been reported, though blood RNA-seq is an emerging diagnostic modality for splicing disorders generally ([PMID: 40593860](https://pubmed.ncbi.nlm.nih.gov/40593860/)).

---

## Section 7 — Anatomical Structures Affected

- **Primary organ / system:** Central nervous system / brain. Suggested UBERON: **UBERON:0000955** (brain), **UBERON:0001017** (central nervous system).
- **Secondary involvement:** Musculoskeletal (hypotonia; UBERON:0002036 muscle tissue), craniofacial structures (mild dysmorphism), metabolic/adipose (overweight; UBERON:0001013 adipose tissue).
- **Tissue/cell level:** Nervous tissue; neurons are the presumptive vulnerable population (CL:0000540). Specific cortical/subcortical populations unresolved.
- **Subcellular level:** Key compartment is the **nuclear speckle** (GO:0016607) within the **nucleus** (GO:0005634); SRRM2 also associates with the **spliceosomal complex** (GO:0005681).
- **Lateralization:** Bilateral/diffuse CNS involvement; no lateralized pattern reported.

---

## Section 8 — Temporal Development

- **Onset:** Congenital/early-childhood developmental disorder; features apparent in infancy (hypotonia) and early childhood (developmental/speech delay). Pattern is **insidious/developmental**, not acute.
- **Progression:** **Static / non-progressive** (neurodevelopmental, not neurodegenerative). Deficits stable; developmental gains possible with intervention. Duration is **chronic/lifelong**.
- **Disease course:** Stable; no relapsing-remitting/episodic pattern; no spontaneous remission.
- **Critical periods:** Early childhood is the key window for developmental and speech/language intervention.

---

## Section 9 — Inheritance and Population

- **Inheritance pattern:** **Autosomal dominant**. Variants are almost always ***de novo***.
- **Penetrance:** High for the neurodevelopmental phenotype in LoF-variant carriers (consistent with high constraint and de novo occurrence); precise figures not established.
- **Expressivity:** **Variable** (ID mild-when-present or absent; neurobehavioral features and overweight vary).
- **Genetic anticipation / repeat expansion:** Not applicable (no repeat mechanism).
- **Germline mosaicism / founder effects / consanguinity / carrier frequency:** Not established; as a de novo dominant disorder, carrier screening and consanguinity are not relevant. Recurrent deletions are mediated by local 16p13.3 palindrome architecture rather than a founder allele ([PMID: 40225164](https://pubmed.ncbi.nlm.nih.gov/40225164/)).
- **Epidemiology / prevalence:** No formal prevalence exists; rare/ultra-rare. Pagnamenta et al. estimated this condition accounts for approximately **~1 in 1,300 of individuals with otherwise-unexplained intellectual disability** in the cohorts studied ([PMID: 40225164](https://pubmed.ncbi.nlm.nih.gov/40225164/)). *SRRM2*'s status among 28 genome-wide-significant de novo NDD genes in ~31,000 trios (Kaplanis/DDD) indicates a recurrent, individually rare cause of NDD.
- **Population demographics:** No ethnic predilection (de novo mechanism). **Sex ratio** not clearly skewed (autosomal). Age distribution: identified in childhood via diagnostic exome/genome sequencing.

---

## Section 10 — Diagnostics

**Recommended approach.** Diagnosis is **molecular**, via broad genomic testing in a child with unexplained developmental/speech delay ± ASD/ADHD, hypotonia, overweight, and subtle dysmorphism.

| Modality | Utility for MRD72 |
|---|---|
| **Whole-exome sequencing (WES)** | High yield; detects the frameshift/nonsense LoF variants that dominate ([PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/)) |
| **Whole-genome sequencing (WGS)** | High yield; detects SNVs and structural variants/whole-gene deletions ([PMID: 40225164](https://pubmed.ncbi.nlm.nih.gov/40225164/)) |
| **Chromosomal microarray (CMA)** | Detects intragenic and whole-gene *SRRM2* deletions (66–482 kb) |
| **NDD/ID gene panels** | Useful if *SRRM2* is included |
| **Single-gene testing** | Reasonable when phenotype strongly suggests *SRRM2* |
| **RNA-seq (blood transcriptome)** | Emerging adjunct to resolve splicing/expression impact of VUS ([PMID: 40593860](https://pubmed.ncbi.nlm.nih.gov/40593860/)) |

- **Laboratory tests / biomarkers / imaging:** No specific biochemical biomarker; no pathognomonic imaging finding. Brain MRI is typically nonspecific. There is **no** MRD72-specific laboratory abnormality analogous to the elevated fetal hemoglobin of the *distinct* ZBTB7A disorder (Section 16).
- **Clinical criteria:** No standalone diagnostic criteria; diagnosis rests on genotype plus a compatible neurodevelopmental phenotype.
- **Differential diagnosis:** Other nuclear-speckle spliceosomopathies and NDDs — foremost **ZTTK syndrome** (*SON*, OMIM #617140), related SR/SRRM-family disorders (e.g., *SRRM1*), and the phenotypically distinct **ZBTB7A**-related MNDLFH (OMIM #619769). Features favoring *SON*/ZTTK include more severe multisystem involvement (structural brain, skeletal, renal anomalies); MRD72 is comparatively milder.
- **Screening:** Not applicable for asymptomatic population screening; cascade testing is generally unnecessary given de novo origin, but parental testing confirms de novo status for recurrence-risk counseling.

---

## Section 11 — Outcome / Prognosis

- **Survival / mortality:** No evidence of reduced life expectancy; not life-limiting based on available cohorts.
- **Morbidity / function:** Chronic disability relates to learning, communication (speech delay), and neurobehavioral features (ASD/ADHD). ID is mild when present.
- **Disease course / complications:** Stable neurodevelopmental profile; overweight/obesity may carry downstream metabolic risk and warrants monitoring. No specific organ-failure complications described.
- **Recovery potential:** Developmental gains achievable with early intervention; the underlying genetic condition is lifelong.
- **Prognostic factors / biomarkers:** None validated. Given variable expressivity, the presence/absence and degree of ID and ASD features shape functional outcome.

Overall prognosis is comparatively favorable relative to other spliceosomopathies (e.g., ZTTK), consistent with the "mild when present" description of ID ([PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/)).

---

## Section 12 — Treatment

**There is no disease-specific or targeted therapy for MRD72.** Management is **supportive and symptom-directed**, following general neurodevelopmental-disorder best practice:

| Domain | Intervention | Suggested NCIT/term |
|---|---|---|
| Developmental | Early intervention programs | Early Intervention |
| Communication | Speech and language therapy | Speech Therapy |
| Motor / hypotonia | Physical therapy, occupational therapy | Physical Therapy; Occupational Therapy |
| Behavioral | ASD-directed behavioral therapy; ADHD management (behavioral ± pharmacologic) | Behavioral Therapy |
| Educational | Individualized education / learning support | — |
| Metabolic | Weight/nutrition management for overweight | Nutritional Support |

- **Pharmacotherapy:** No gene-directed drug. Standard symptomatic agents (e.g., ADHD medications) may be used per general guidelines; no MRD72-specific pharmacogenomic data.
- **Advanced therapeutics (gene/cell/RNA therapy):** None in development or trials for MRD72. Conceptually, dosage-restorative strategies would be required for a haploinsufficiency mechanism, but none exist.
- **Experimental / clinical trials:** No MRD72-specific registered trials identified.
- **Treatment strategy:** Multidisciplinary, individualized, supportive care plus genetic counseling.

---

## Section 13 — Prevention

- **Primary prevention:** Not applicable — de novo dominant variants cannot be prevented.
- **Secondary prevention:** Early developmental screening enabling early intervention (speech/OT/PT) optimizes functional outcomes.
- **Genetic screening / reproductive options:** For a couple with an affected child, recurrence risk is low (de novo), but **prenatal or preimplantation genetic testing** for the known familial variant is possible; germline mosaicism, though not documented for *SRRM2*, is a theoretical small residual risk.
- **Counseling:** **Genetic counseling** is central — confirming de novo status, communicating low recurrence risk, supporting family planning.
- **Immunization / public health / prophylaxis:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs:** *SRRM2* is highly conserved with stringent 1:1 orthology across human, mouse (**Srrm2**, MGI:1923206), rat, and zebrafish. In *Drosophila*, there is no distinct *SRRM2* ortholog; the fused gene **Srrm234** corresponds to the vertebrate *SRRM2/SRRM3/SRRM4* cluster, which arose by duplication/subfunctionalization of an ancestral *Srrm2/3/4* gene ([PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/) and review context).
- **Natural disease in other species:** No naturally occurring *SRRM2* disorder is catalogued in companion animals or wildlife (not reported in OMIA).
- **Comparative biology:** Essentiality and conservation across metazoans underscore SRRM2's fundamental splicing role; embryonic lethality of complete knockouts (Section 15) is conserved across mouse and *C. elegans*.
- **Zoonotic / transmission:** Not applicable (non-infectious genetic disorder).

---

## Section 15 — Model Organisms

- **Mouse (*Srrm2*, MGI:1923206):** Complete (homozygous) knockout of SRm300/Srrm2 is **early-embryonic lethal**, demonstrating developmental essentiality and explaining why the human disorder is a haploinsufficiency phenotype rather than biallelic loss (reviewed in Cuinat et al. 2022, [PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/)). A dosage-sensitive heterozygous mouse model specific to MRD72 is not yet well characterized.
- ***C. elegans*:** SRm300/*SRRM2* knockout is likewise embryonic-lethal, confirming conserved essentiality.
- ***Drosophila*:** The combined **Srrm234** gene represents the ancestral form of vertebrate *SRRM2/3/4*.
- **Zebrafish:** Reported to modulate cell fate in early development (Carvalho et al. 2024, *Biol Open*), consistent with a broad developmental role.
- **Cross-scaffold model (SON):** As a proxy for the speckle-scaffold mechanism, a **Son+/- haploinsufficiency mouse** "recapitulated clinical symptoms" of ZTTK syndrome — growth retardation, cognitive impairment, skeletal abnormalities, and kidney agenesis, plus hematopoietic abnormalities ([PMID: 38290089](https://pubmed.ncbi.nlm.nih.gov/38290089/)). This shows partial loss of a nuclear-speckle scaffold protein is sufficient to produce a multisystem neurodevelopmental phenotype, strongly supporting the SRRM2 haploinsufficiency model.
- **Model applications / limitations:** Existing models establish essentiality and the speckle-scaffold paradigm but do not yet recapitulate the specific mild MRD72 phenotype; a conditional/dosage-controlled *Srrm2* heterozygous CNS model is the key resource gap.

---

## Section 16 — Critical Clarification: MRD72 (*SRRM2*) vs. the *ZBTB7A* Disorder (MNDLFH)

Because the early iterations initially attributed MRD72 to *ZBTB7A*, this section explicitly separates the two entities. **They are distinct diseases.**

| Feature | **MRD72 (this report)** | **MNDLFH (distinct disorder)** |
|---|---|---|
| Gene | ***SRRM2*** (16p13.3) | *ZBTB7A* (19p13.3) |
| OMIM | **#620439** | #619769 |
| Protein / function | SRm300, nuclear-speckle splicing scaffold | LRF/Pokemon, BTB-zinc-finger transcriptional repressor |
| Core phenotype | Mild DD, speech delay, ASD/ADHD, hypotonia, overweight, mild dysmorphism | ID, **macrocephaly**, **pharyngeal/adenoid lymphoid overgrowth**, **elevated fetal hemoglobin** |
| Mechanism | Haploinsufficiency of splicing/speckle scaffold | Haploinsufficiency of a transcription factor (lympho/hematopoiesis) |

The *ZBTB7A* findings gathered in iterations 1–2 — elevated HbF via γ-globin de-repression ([PMID: 34515416](https://pubmed.ncbi.nlm.nih.gov/34515416/), [PMID: 26816381](https://pubmed.ncbi.nlm.nih.gov/26816381/)); oligodendrocyte differentiation role ([PMID: 22615173](https://pubmed.ncbi.nlm.nih.gov/22615173/)); B-vs-T lineage/Notch regulation ([PMID: 17495164](https://pubmed.ncbi.nlm.nih.gov/17495164/)); overlap with 19p13.3 microdeletion syndrome ([PMID: 25853300](https://pubmed.ncbi.nlm.nih.gov/25853300/), [PMID: 23610052](https://pubmed.ncbi.nlm.nih.gov/23610052/)) — **belong to MNDLFH, not MRD72**, and are retained only to prevent conflation. For MRD72 knowledge-base population, use exclusively the *SRRM2* content in Sections 1–15.

---

## Mechanistic Model / Interpretation

MRD72 is best understood as a **nuclear-speckle spliceosomopathy**. The unifying concept: certain nuclear proteins that build and maintain nuclear speckles — the organelles that concentrate the splicing machinery — are **exquisitely dosage-sensitive** in the developing nervous system. SRRM2 and SON are the two obligate scaffolding subunits of the speckle core ([PMID: 33095160](https://pubmed.ncbi.nlm.nih.gov/33095160/)). Reducing either to ~50% (haploinsufficiency) does not kill the cell (unlike complete knockout, which is embryonic-lethal) but degrades splicing efficiency/fidelity enough to derail neurodevelopment — yielding overlapping but distinct autosomal-dominant NDDs:

```
        Nuclear-speckle core scaffold (SON + SRRM2)
                 │                    │
        SON haploinsufficiency   SRRM2 haploinsufficiency
                 │                    │
             ZTTK syndrome         MRD72
           (OMIM #617140)       (OMIM #620439)
        severe multisystem      milder, speech-predominant
        (brain/skeletal/renal)  (DD, ASD/ADHD, hypotonia,
                                 overweight)
```

The extreme evolutionary constraint on *SRRM2* (pLI = 1.0; LOEUF ≈ 0.18; ClinGen HI = 3), the near-uniformly *de novo* protein-truncating variant spectrum, the recurrent 16p13.3 palindrome-mediated deletions, and the essentiality across mouse/worm/fly/zebrafish together form a **coherent, internally consistent haploinsufficiency model**. The comparatively mild phenotype (relative to ZTTK) suggests that residual SRRM2 splicing-coactivator activity, and partial functional redundancy within the SR-related protein family (including partner/paralog SRRM1), buffer the consequences of 50% dosage loss.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/) | *Loss-of-function variants in SRRM2 cause a neurodevelopmental disorder* | **Defining paper.** Establishes *SRRM2* as causal; 22-patient cohort; variant spectrum; core phenotype; LoF constraint; SRm300 splicing function |
| [33095160](https://pubmed.ncbi.nlm.nih.gov/33095160/) | *SON and SRRM2 are essential for nuclear speckle formation* | Mechanistic basis — SRRM2 is the SC35 antigen and, with SON, the essential speckle scaffold |
| [40225164](https://pubmed.ncbi.nlm.nih.gov/40225164/) | *A Palindrome-Like Structure on 16p13.3…* | Recurrent whole-gene deletions; 16p13.3 palindrome; ~1/1300 prevalence estimate in unexplained ID |
| [38290089](https://pubmed.ncbi.nlm.nih.gov/38290089/) | *Mouse model of ZTTK syndrome reveals indispensable SON functions* | Proof that haploinsufficiency of a speckle-scaffold protein produces a multisystem NDD (paralog support) |
| [40593860](https://pubmed.ncbi.nlm.nih.gov/40593860/) | *Blood transcriptome profiling in a pediatric cohort* | Emerging RNA-seq diagnostics for splicing disorders (adjunct) |
| [34515416](https://pubmed.ncbi.nlm.nih.gov/34515416/), [26816381](https://pubmed.ncbi.nlm.nih.gov/26816381/), [22615173](https://pubmed.ncbi.nlm.nih.gov/22615173/), [17495164](https://pubmed.ncbi.nlm.nih.gov/17495164/), [25853300](https://pubmed.ncbi.nlm.nih.gov/25853300/), [23610052](https://pubmed.ncbi.nlm.nih.gov/23610052/) | *ZBTB7A / 19p13.3 series* | Pertain to the **distinct** MNDLFH disorder — included only for differential clarification (Section 16) |

**Evidence-source types:** Human clinical (Cuinat 2022 cohort; Pagnamenta 2023 structural variants) forms the diagnostic and clinical backbone. In vitro/cell biology (Ilik 2020, [PMID: 33095160](https://pubmed.ncbi.nlm.nih.gov/33095160/)) supplies the speckle-scaffold mechanism. Model-organism data (Son+/- mouse, [PMID: 38290089](https://pubmed.ncbi.nlm.nih.gov/38290089/); lethal Srrm2 knockouts) provide mechanistic and essentiality support. Computational constraint metrics (gnomAD/ClinGen/DDD) corroborate haploinsufficiency.

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** The disease is defined largely by one 22-patient cohort plus structural-variant reports; per-phenotype frequencies, penetrance, and expressivity are imprecise.
2. **No MRD72-specific molecular profiling.** Patient-derived transcriptomic/proteomic maps of the mis-splicing signature are lacking; the exact mis-spliced targets driving the neurodevelopmental phenotype are unknown.
3. **No dedicated animal model.** A dosage-controlled *Srrm2*+/- (or CNS-conditional) mouse recapitulating the mild MRD72 phenotype has not been reported; existing knockouts are lethal.
4. **No natural history / QoL data.** Longitudinal outcomes, adult phenotype, and validated QoL measures are absent.
5. **No targeted therapy.** Management is entirely supportive; no gene-dosage-restorative approaches are in development.
6. **Naming ambiguity.** MRD72 was conflated with the *ZBTB7A* disorder early in this investigation; downstream knowledge bases must preserve the *SRRM2* (OMIM #620439) vs *ZBTB7A* (OMIM #619769) distinction.

---

## Proposed Follow-up Experiments / Actions

1. **Deep-phenotype an expanded cohort** (international registry via GeneMatcher/DECIPHER) to quantify per-feature frequencies, penetrance, expressivity, and adult outcomes.
2. **Patient-derived transcriptomics** (blood + iPSC-derived neurons) to define the SRRM2-haploinsufficiency mis-splicing signature and candidate downstream effectors; leverage RNA-seq diagnostics ([PMID: 40593860](https://pubmed.ncbi.nlm.nih.gov/40593860/)).
3. **Generate a Srrm2+/- (and CNS-conditional) mouse** to test phenotype recapitulation, nuclear-speckle integrity, and neurodevelopmental splicing programs; benchmark against the Son+/- ZTTK model.
4. **Systematic comparison with ZTTK/SON and SRRM1** to map the "nuclear-speckle spliceosomopathy" spectrum and identify shared vs gene-specific molecular consequences.
5. **Functional/CNV validation** of the 16p13.3 palindrome mechanism and its contribution to recurrent deletions for improved variant interpretation.
6. **Curate and correct ontology cross-references** (MONDO:0957397 ↔ OMIM #620439 ↔ *SRRM2*) to prevent conflation with the *ZBTB7A* disorder.

---

*Report compiled from 5 investigation iterations, 12 confirmed findings, and 35 reviewed papers. Primary source: Cuinat et al., Genet Med 2022 ([PMID: 35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/)).*


## Artifacts

- [OpenScientist final report](Intellectual_Developmental_Disorder_Autosomal_Dominant_72-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intellectual_Developmental_Disorder_Autosomal_Dominant_72-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.