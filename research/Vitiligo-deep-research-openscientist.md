---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T06:42:34.155526'
end_time: '2026-07-26T06:57:16.482290'
duration_seconds: 882.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Vitiligo
  mondo_id: MONDO:0008661
  category: Complex
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 47
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Vitiligo-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Vitiligo-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vitiligo
- **MONDO ID:** MONDO:0008661 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Vitiligo** covering all of the
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

# Vitiligo (MONDO:0008661): Comprehensive Disease Characterization Report

**Disease:** Vitiligo — **MONDO:0008661** — Category: Complex (polygenic autoimmune)
**Report type:** Aggregated disease-level synthesis from primary literature and ontology resources (not individual EHR data).
**Date:** 2026-07-26

## Summary

**Vitiligo** is a common, acquired, chronic **autoimmune depigmenting skin disorder** affecting approximately **0.5–2% of the global population**, in which cytotoxic **CD8+ T lymphocytes selectively destroy epidermal melanocytes**, producing well-demarcated, chalk-white macules and patches. It is not a Mendelian disease but a **polygenic/multifactorial (complex) trait**, with more than **50 genome-wide association (GWAS) susceptibility loci** clustered in three functional categories: immune regulation (e.g., HLA, PTPN22, NLRP1), oxidative-stress response, and melanocyte biology/melanogenesis (e.g., TYR). The disease is defined clinically and confirmed with simple tools (Wood's lamp, dermoscopy), and although it is **non-fatal**, it carries a substantial psychosocial and quality-of-life burden and is strongly associated with other autoimmune conditions, particularly thyroid disease.

The prevailing mechanistic model is a **convergence of melanocyte-intrinsic vulnerability and immune effector activity**. Vitiligo melanocytes are hypersensitive to oxidative stress owing to defective stress-response and autophagy pathways. Under stress they release **damage-associated molecular patterns (DAMPs)** — notably HSP70, HMGB1, and IL-15 — which activate innate immunity and prime an adaptive response. Loss of adhesion molecules (DDR1, E-cadherin) promotes melanocyte detachment and antigen exposure. The resulting autoimmune cascade converges on a central, self-amplifying **IFN-γ → CXCL9/CXCL10 → CXCR3 → CD8+ T-cell** effector loop, maintained locally by **tissue-resident memory T cells (TRM)** that explain the characteristic relapse after therapy withdrawal. Critically, this axis is **pharmacologically reversible**: neutralizing CXCL10 or inhibiting STAT1/JAK signaling reverses depigmentation in mouse models and repigments patients in the clinic.

These insights have transformed treatment. **Topical ruxolitinib (a JAK1/2 inhibitor)** is FDA-approved and repigments nonsegmental vitiligo in phase 3 trials; **narrowband UVB (NB-UVB) phototherapy** remains first-line and works by mobilizing melanocyte stem cells while depleting skin memory/resident-memory T cells; and **oral JAK1 inhibitors (povorcitinib, upadacitinib)** and surgical melanocyte grafting extend options for extensive or stable disease. Prognosis is dominated by **anatomical site** (facial lesions repigment best, acral lesions worst) and the availability of a follicular melanocyte reservoir. This report synthesizes 12 confirmed findings drawn from 53 reviewed papers across all 15 requested characterization domains.

---

## 1. Disease Information

**Overview.** Vitiligo is a chronic, acquired autoimmune disorder characterized by the selective and progressive destruction of epidermal melanocytes, resulting in depigmented (white) macules and patches on the skin and, less commonly, mucous membranes and hair (leukotrichia). *"Vitiligo is a chronic autoimmune depigmenting disorder affecting 0.5%-2% of the global population"* ([PMID: 42332186](https://pubmed.ncbi.nlm.nih.gov/42332186/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0008661 |
| OMIM | 193200 (Vitiligo-associated multiple autoimmune disease susceptibility 1, VAMAS1) |
| ICD-11 | EE60 |
| ICD-10 | L80 |
| MeSH | D014820 |
| Orphanet | ORPHA:3435 |

**Synonyms / alternative names.** Acquired leukoderma; vitiligo vulgaris; nonsegmental vitiligo (NSV); segmental vitiligo (SV). Historically "autoimmune vitiligo" was used as a subtype but was formally abandoned by consensus (see Section 5).

**Information source.** The information in this report is derived predominantly from **aggregated disease-level resources** (GWAS meta-analyses, systematic reviews, consensus statements, and randomized clinical trials) supplemented by mechanistic model-organism and in vitro studies, rather than individual patient EHR data.

---

## 2. Etiology

**Primary causes.** Vitiligo is **multifactorial**, arising from an interplay of (1) polygenic genetic predisposition, (2) melanocyte-intrinsic oxidative-stress vulnerability, and (3) environmental/mechanical triggers that precipitate autoimmune melanocyte destruction. The unifying downstream cause of depigmentation is CD8+ T-cell–mediated killing of melanocytes.

**Genetic risk factors.** GWAS have identified **~50 susceptibility loci** ([PMID: 28317533](https://pubmed.ncbi.nlm.nih.gov/28317533/); *"Genomewide association studies have discovered approximately 50 genetic loci contributing to vitiligo risk"*), later refined to **>50 loci** encompassing MHC/HLA-region genes and genes involved in immunity, oxidative stress, and melanogenesis ([PMID: 39890561](https://pubmed.ncbi.nlm.nih.gov/39890561/); *"Genome-wide association studies (GWAS) have identified over 50 susceptibility loci, including key genes within the MHC region and those involved in immunity, oxidative stress, and melanogenesis"*). A well-characterized example is **NLRP1** (innate-immune inflammasome regulator): the susceptible **"GCT" haplotype** (rs2670660, rs6502867, rs12150220) roughly **doubles vitiligo risk** and is accompanied by elevated NLRP1 mRNA ([PMID: 23773036](https://pubmed.ncbi.nlm.nih.gov/23773036/); *"The frequency of susceptible haplotype 'GCT' was significantly higher in patients with GV and increased the risk of vitiligo twofold"*; meta-analysis [PMID: 29152150](https://pubmed.ncbi.nlm.nih.gov/29152150/)).

**Environmental risk factors.** Recognized triggers include cutaneous **oxidative/chemical stress** (phenolic/catechol compounds such as monobenzone), **mechanical trauma / friction** (Koebner phenomenon), **sunburn**, and **emotional/physical stress** (neuroendocrine axis). Family history is a strong risk factor (polygenic burden). Immune-checkpoint inhibitor (ICI) therapy in cancer can precipitate vitiligo-like depigmentation (see Sections 6 and 11).

**Protective factors.** A genetic protective variant has been identified in the **HSP70/HSPA1L** gene: *"the rs2227956 C allele and TC genotype were associated with protection against vitiligo"* ([PMID: 36345598](https://pubmed.ncbi.nlm.nih.gov/36345598/)). No robust dietary/lifestyle protective factor has been established; a folate–autoimmunity review found only weak, low-credibility evidence for any folate association ([PMID: 42396914](https://pubmed.ncbi.nlm.nih.gov/42396914/)).

**Gene–environment interactions.** The central paradigm is that **genetically primed melanocytes** (with defective oxidative-stress handling and reduced adhesion) release DAMPs when exposed to environmental oxidative/chemical stress, converting a subclinical predisposition into overt autoimmune destruction ([PMID: 36154894](https://pubmed.ncbi.nlm.nih.gov/36154894/); [PMID: 35643735](https://pubmed.ncbi.nlm.nih.gov/35643735/)). Neuropeptide Y (NPY), released under stress, synergizes with oxidative stress via NPY2R-mediated NF-κB activation to recruit CD8+ T cells ([PMID: 42031917](https://pubmed.ncbi.nlm.nih.gov/42031917/)).

---

## 3. Phenotypes

**Core phenotype (physical manifestation/clinical sign).** Well-demarcated, chalk-white/depigmented macules and patches from loss of epidermal melanocytes. *"...characterized by the development of white macules resulting from a loss of epidermal melanocytes"* ([PMID: 28685247](https://pubmed.ncbi.nlm.nih.gov/28685247/)).

**Associated phenotypes.**
- **Leukotrichia** (whitening of lesional hair) — found in ~46.5% of NSV patients in one cross-sectional study and considered a marker of poorer prognosis / follicular reservoir depletion ([PMID: 30971534](https://pubmed.ncbi.nlm.nih.gov/30971534/)).
- **Koebner phenomenon** (new lesions at sites of trauma) — an activity sign.
- **Confetti-like depigmentation** and trichrome lesions — signs of active/progressing disease ([PMID: 41703718](https://pubmed.ncbi.nlm.nih.gov/41703718/)).
- **Psychosocial/behavioral impact** — significant impairment of quality of life and neuropsychological burden ([PMID: 42332186](https://pubmed.ncbi.nlm.nih.gov/42332186/); [PMID: 42479635](https://pubmed.ncbi.nlm.nih.gov/42479635/)).

**Characteristics.** Onset: frequently childhood — *"More than 50% of cases begin before 18 years of age"* ([PMID: 42479635](https://pubmed.ncbi.nlm.nih.gov/42479635/)). Severity: variable. Progression: episodic/progressive with periods of stability. Distribution: typically bilateral and symmetric in NSV; unilateral/dermatomal in SV.

**Quality of life.** Measured with the Dermatology Life Quality Index (DLQI); Vellus/leukotrichia scores correlate with DLQI and disease severity ([PMID: 30971534](https://pubmed.ncbi.nlm.nih.gov/30971534/)).

**Suggested HPO terms.** HP:0001010 (Hypopigmentation of the skin); HP:0001053 (Hypopigmented skin patches / vitiligo); HP:0002861 (Vitiligo); HP:0011365 (leukotrichia-related depigmentation of hair).

---

## 4. Genetic / Molecular Information

**Causal / susceptibility genes.** Vitiligo has **no single causal gene**; risk is conferred by **>50 loci** ([PMID: 39890561](https://pubmed.ncbi.nlm.nih.gov/39890561/)). Key implicated genes span:
- **Immune regulation:** HLA (class I and II, MHC region), PTPN22, NLRP1, LPP, IL2RA, CD44, BACH2, TAPBP.
- **Oxidative stress:** HSPA1L (HSP70), and stress-response pathways.
- **Melanogenesis/melanocyte:** TYR (tyrosinase), MC1R, OCA2, TYRP1.

**NLRP1** variants (rs2670660, rs6502867, rs12150220; GCT haplotype ≈ 2× risk) are a robust susceptibility signal shared with other autoimmune diseases including autoimmune thyroid disease ([PMID: 23773036](https://pubmed.ncbi.nlm.nih.gov/23773036/); [PMID: 23374100](https://pubmed.ncbi.nlm.nih.gov/23374100/)).

**Multi-omics / functional link — TAPBP.** Integrative multi-omics (FinnGen GWAS n=466,064; eQTLgen n=31,684; single-cell) identified **TAPBP** (tapasin, antigen-processing) as a top mediator; TAPBP overexpression in melanocytes increased HLA class I, suppressed proliferation, and induced apoptosis, with **STAT2** as upstream regulator linking IFN signaling to antigen presentation ([PMID: 41884389](https://pubmed.ncbi.nlm.nih.gov/41884389/)).

**Variant classification / type.** Vitiligo risk alleles are predominantly **common regulatory/coding SNPs of small individual effect** (susceptibility variants, not ACMG "pathogenic" Mendelian variants). Origin is **germline**; there are no recurrent somatic driver mutations. Functional consequences are largely **regulatory** (altered expression of immune/melanocyte genes) rather than classical loss/gain-of-function.

**Protective allele.** HSPA1L rs2227956 C allele/TC genotype ([PMID: 36345598](https://pubmed.ncbi.nlm.nih.gov/36345598/)).

**Epigenetics.** DNA methylation and histone-modification changes contribute to dysregulated immune and melanocyte gene expression ([PMID: 39890561](https://pubmed.ncbi.nlm.nih.gov/39890561/)).

**Chromosomal abnormalities.** None characteristic — vitiligo is not associated with aneuploidy or recurrent structural rearrangements. **Somatic mosaicism**, however, is proposed to underlie the dermatomal distribution of **segmental vitiligo** ([PMID: 39739902](https://pubmed.ncbi.nlm.nih.gov/39739902/)).

**Suggested HGNC/gene annotations:** HLA-A, PTPN22 (HGNC:9652), NLRP1 (HGNC:14374), TYR (HGNC:12442), TAPBP (HGNC:11566), HSPA1L (HGNC:5234), STAT2, IFNG (HGNC:5438), CXCL10 (HGNC:10637).

---

## 5. Environmental Information

**Environmental / chemical factors.** **Phenolic and catechol chemicals** — most notably **monobenzone (monobenzyl ether of hydroquinone)** — are the best-established chemical triggers; they induce oxidative stress in melanocytes and precipitate CD8+ T-cell-mediated depigmentation, forming the basis of the leading mouse model ([PMID: 42230481](https://pubmed.ncbi.nlm.nih.gov/42230481/); [PMID: 40780471](https://pubmed.ncbi.nlm.nih.gov/40780471/); [PMID: 38542385](https://pubmed.ncbi.nlm.nih.gov/38542385/)). Occupational exposure to phenolic compounds (e.g., in rubber/adhesive industries) is a recognized cause of "occupational/contact vitiligo."

**Lifestyle factors.** Mechanical trauma/friction (Koebner), sunburn, and psychological stress are contributing triggers. No strong causal dietary factor is established.

**Infectious agents.** Vitiligo is **not an infectious disease**; no pathogen causes it. A single case report describes segmental vitiligo temporally following nine-valent HPV vaccination, hypothesized via bystander activation/molecular mimicry, but explicitly noted as **correlation, not proven causation** ([PMID: 40743226](https://pubmed.ncbi.nlm.nih.gov/40743226/)).

**Suggested CHEBI terms:** CHEBI:9613 (monobenzone/hydroquinone monobenzyl ether); CHEBI:16240 (hydrogen peroxide); CHEBI:26523 (reactive oxygen species).

---

## 6. Mechanism / Pathophysiology

Vitiligo pathogenesis integrates a **melanocyte-intrinsic defect**, **innate immune ignition**, and an **adaptive CD8+ T-cell effector loop**.

**Step 1 — Melanocyte-intrinsic oxidative-stress vulnerability.** Vitiligo melanocytes are hypersensitive to oxidative damage due to defective stress-response and autophagy pathways, leading to elevated pro-inflammatory HSP70 ([PMID: 35643735](https://pubmed.ncbi.nlm.nih.gov/35643735/); *"melanocytes are more sensitive to oxidative damage, leading to the increased expression of proinflammatory proteins such as HSP70. The lower expression of epithelial adhesion molecules, such as DDR1 and E-cadherin, facilitates damage to melanocytes and exposure of antigens"*).

**Step 2 — DAMP release ignites immunity.** *"At high oxidative stress levels, damage-associated molecular patterns (DAMPs) are released from keratinocytes or melanocytes in the skin and induce downstream immune responses during vitiligo"* ([PMID: 36154894](https://pubmed.ncbi.nlm.nih.gov/36154894/)). Key DAMPs: **HSP70, HMGB1, IL-15**. Innate immune activation (including the NLRP1 inflammasome) amplifies the adaptive response and licenses autoreactive CD8+ T cells ([PMID: 41169396](https://pubmed.ncbi.nlm.nih.gov/41169396/)).

**Step 3 — Loss of adhesion & antigen exposure.** Reduced DDR1 and E-cadherin facilitate melanocyte detachment (melanocytorrhagy) and antigen presentation ([PMID: 35643735](https://pubmed.ncbi.nlm.nih.gov/35643735/); [PMID: 36947026](https://pubmed.ncbi.nlm.nih.gov/36947026/)).

**Step 4 — The IFN-γ–CXCL9/CXCL10–CXCR3–CD8+ effector loop (central effector pathway).** Lesional skin shows an **IFN-γ-specific gene signature**; melanocyte-antigen-specific CD8+ T cells infiltrate along the basal layer ([PMID: 39739902](https://pubmed.ncbi.nlm.nih.gov/39739902/); *"High levels of melanocyte antigen-specific CD8+ T cells are found in early SV lesional skin infiltrating around melanocytes along the basal layer"*). IFN-γ induces keratinocyte production of the chemokines **CXCL9 and CXCL10**, which recruit and localize **CXCR3+** cytotoxic T cells. Mouse-model dissection shows *"CXCL9 promoted autoreactive T cell global recruitment to the skin but not effector function, whereas CXCL10 was required for effector function and localization within the skin"* ([PMID: 24523323](https://pubmed.ncbi.nlm.nih.gov/24523323/)). Crucially the loop is reversible: *"CXCL10 neutralization in mice with established, widespread depigmentation induces reversal of disease, evidenced by repigmentation"* ([PMID: 24523323](https://pubmed.ncbi.nlm.nih.gov/24523323/)), and STAT1 inhibition with simvastatin *"both prevented and reversed depigmentation in our mouse model of vitiligo, and reduced the number of infiltrating autoreactive CD8(+) T cells in the skin"* ([PMID: 25521459](https://pubmed.ncbi.nlm.nih.gov/25521459/)).

**Step 5 — Disease maintenance by tissue-resident memory T cells (TRM).** *"Tissue resident memory T cells (Trm) form in the skin in vitiligo and persist to maintain disease, as white spots often recur rapidly after discontinuing therapy"* ([PMID: 30423329](https://pubmed.ncbi.nlm.nih.gov/30423329/)). TRM cooperate with recirculating memory T cells, explaining chronicity and relapse.

**Molecular pathways:** JAK/STAT (IFN-γ → JAK1/2 → STAT1), NF-κB (NPY2R-driven; [PMID: 42031917](https://pubmed.ncbi.nlm.nih.gov/42031917/)), IL-15/IL-15R (TRM survival), Wnt (melanocyte regeneration; noncanonical Wnt5a; [PMID: 42230481](https://pubmed.ncbi.nlm.nih.gov/42230481/)), and cAMP/PKA/CREB (melanogenesis; [PMID: 41720011](https://pubmed.ncbi.nlm.nih.gov/41720011/)).

**Causal chain (upstream → downstream):**

```
Genetic predisposition (HLA, NLRP1, oxidative-stress genes)
        │
Melanocyte oxidative-stress vulnerability + environmental trigger (monobenzone, ROS, trauma)
        │
DAMP release (HSP70, HMGB1, IL-15) + adhesion loss (DDR1/E-cadherin)
        │
Innate immune activation (NLRP1 inflammasome, type-1 IFN)
        │
Autoreactive CD8+ T-cell priming → IFN-γ
        │
Keratinocyte CXCL9/CXCL10 ↑  →  CXCR3+ CD8+ T-cell recruitment & effector function
        │
Melanocyte apoptosis → DEPIGMENTED MACULES
        │
Tissue-resident memory T cells (TRM) → chronicity & relapse
```

**Suggested GO / CL terms:** GO:0006979 (response to oxidative stress); GO:0060333 (IFN-γ-mediated signaling pathway); GO:0006955 (immune response); GO:0006915 (apoptotic process); GO:0071356 (cellular response to TNF); CL:0000148 (melanocyte); CL:0000909 (CD8-positive, alpha-beta memory T cell); CL:0000312 (keratinocyte).

---

## 7. Anatomical Structures Affected

- **Primary organ:** Skin (UBERON:0002097) — specifically the **epidermis** (UBERON:0001003) and its **basal layer** (UBERON:0002025).
- **Target cell:** **Epidermal melanocytes** (CL:0000148); follicular melanocyte stem cells in the hair-follicle bulge serve as the regenerative reservoir.
- **Secondary involvement:** Hair follicles (leukotrichia), mucous membranes, and (rarely) the uveal tract/retinal pigment epithelium. Systemic association with the **endocrine (thyroid)** system.
- **Tissue type:** Epithelial (stratified squamous epidermis).
- **Subcellular compartments:** Melanosome (GO:0042470), mitochondria (oxidative stress), endoplasmic reticulum (antigen processing/HSP), nucleus (STAT signaling).
- **Localization / lateralization:** NSV is typically **bilateral and symmetric**, favoring periorificial (face), acral (hands/feet), and extensor surfaces; SV is **unilateral, dermatomal/segmental**. Facial and head/neck sites repigment best; acral sites worst ([PMID: 41840918](https://pubmed.ncbi.nlm.nih.gov/41840918/)).

**Suggested UBERON terms:** UBERON:0002097 (skin), UBERON:0001003 (skin epidermis), UBERON:0002025 (basal layer of epidermis), UBERON:0002073 (hair follicle).

---

## 8. Temporal Development

**Onset.** Frequently **childhood/adolescence**: *"More than 50% of cases begin before 18 years of age"* ([PMID: 42479635](https://pubmed.ncbi.nlm.nih.gov/42479635/)). In a Mexican pediatric cohort mean age at onset was **6.3 ± 3.7 years**, with 85% nonsegmental ([PMID: 42479635](https://pubmed.ncbi.nlm.nih.gov/42479635/)). Onset pattern is typically **insidious/chronic**.

**Progression.** Course is variable — **progressive, episodic, or stable** — with flares (Koebner, confetti lesions) and periods of quiescence. Disease is **chronic and lifelong**; spontaneous repigmentation is uncommon and usually incomplete.

**Patterns.** Repigmentation (treatment-induced) proceeds perifollicularly from the follicular melanocyte reservoir. **Relapse is common** after therapy discontinuation because of persistent TRM ([PMID: 30423329](https://pubmed.ncbi.nlm.nih.gov/30423329/)). **Critical intervention window:** early/active disease responds best to immune suppression, while melanocyte-regeneration strategies matter for repigmentation ([PMID: 36947026](https://pubmed.ncbi.nlm.nih.gov/36947026/)).

---

## 9. Inheritance and Population

**Epidemiology.** Prevalence **~0.5–2%** globally ([PMID: 42332186](https://pubmed.ncbi.nlm.nih.gov/42332186/)), with higher figures (~2%) reported in India ([PMID: 42377206](https://pubmed.ncbi.nlm.nih.gov/42377206/)). A commonly cited general-population estimate is ~0.5% ([PMID: 28685247](https://pubmed.ncbi.nlm.nih.gov/28685247/)).

**Inheritance.** **Multifactorial/polygenic** (complex trait) — not Mendelian. Family clustering reflects cumulative polygenic risk plus shared environment; concordance is incomplete even in monozygotic twins, indicating strong environmental/epigenetic contributions. **Segmental vitiligo** is linked to **somatic mosaicism** ([PMID: 39739902](https://pubmed.ncbi.nlm.nih.gov/39739902/)).

**Autoimmune comorbidity.** Strong association with other autoimmune diseases, especially **thyroid dysfunction**: in the pediatric cohort, 34% of tested patients had thyroid abnormalities (subclinical hypothyroidism 20.4%; thyroid autoantibodies positive in 27.3%) ([PMID: 42479635](https://pubmed.ncbi.nlm.nih.gov/42479635/); *"It has been associated with other autoimmune diseases, particularly thyroid dysfunction"*). Vitiligo also co-occurs with type 1 diabetes ([PMID: 42445886](https://pubmed.ncbi.nlm.nih.gov/42445886/)), alopecia areata, atopic dermatitis, and shares pleiotropic loci with these conditions ([PMID: 41009683](https://pubmed.ncbi.nlm.nih.gov/41009683/); [PMID: 42079583](https://pubmed.ncbi.nlm.nih.gov/42079583/)).

**Subtype distribution.** Segmental vitiligo accounts for **5–27.9%** of patients ([PMID: 39739902](https://pubmed.ncbi.nlm.nih.gov/39739902/)); the remainder are nonsegmental.

**Demographics.** Affects all skin types and ethnicities; more clinically conspicuous (and psychosocially burdensome) in darker skin. No strong sex predilection overall, though ascertainment often skews female.

---

## 10. Diagnostics

**Diagnosis is primarily clinical.** *"tool-free and standardized assessments such as Koebner phenomenon, confetti-like depigmentation, Wood's lamp and dermoscopy provide visible clues associated with active disease"* ([PMID: 41703718](https://pubmed.ncbi.nlm.nih.gov/41703718/)).

**Key modalities.**

| Modality | Role | Evidence |
|---|---|---|
| Wood's lamp (UV-A) | Accentuates depigmentation, especially in fair skin | [PMID: 41703718](https://pubmed.ncbi.nlm.nih.gov/41703718/) |
| Dermoscopy | Activity staging (perifollicular pigment, telangiectasia) | [PMID: 42087462](https://pubmed.ncbi.nlm.nih.gov/42087462/) |
| Reflectance confocal microscopy (RCM) | Non-invasive melanocyte assessment; staging | [PMID: 42087462](https://pubmed.ncbi.nlm.nih.gov/42087462/) |
| Histopathology / IHC | Absent epidermal melanocytes (loss of Melan-A/MITF/tyrosinase); perilesional lymphocytic infiltrate | [PMID: 41703718](https://pubmed.ncbi.nlm.nih.gov/41703718/) |
| Molecular biomarkers | IFN-γ, CXCL9/CXCL10 in blood, blister fluid, tissue | [PMID: 41703718](https://pubmed.ncbi.nlm.nih.gov/41703718/) |

**RCM/dermoscopy staging** shows strong concordance with clinical evaluation: *"Staging results based on RCM and dermoscopy showed strong concordance with clinical evaluation; Kappa values were 0.74 and 0.718"*, with RCM positive percent agreement 94.16% ([PMID: 42087462](https://pubmed.ncbi.nlm.nih.gov/42087462/)).

**Severity scoring:** VASI (Vitiligo Area Scoring Index), F-VASI (facial), T-VASI (total), VES, DLQI ([PMID: 30971534](https://pubmed.ncbi.nlm.nih.gov/30971534/)).

**Genetic testing** is **not routinely indicated** (polygenic, no single causal gene). **Screening:** thyroid function and thyroid autoantibody testing are recommended given the strong comorbidity ([PMID: 42479635](https://pubmed.ncbi.nlm.nih.gov/42479635/)).

**Differential diagnosis:** pityriasis alba, tinea versicolor, post-inflammatory hypopigmentation, nevus depigmentosus, piebaldism, chemical leukoderma, and hypopigmented mycosis fungoides.

---

## 11. Outcome / Prognosis

**Survival/mortality.** Vitiligo is a **non-fatal, chronic** disease with normal life expectancy; morbidity is driven by **psychosocial burden and quality-of-life impairment** ([PMID: 42332186](https://pubmed.ncbi.nlm.nih.gov/42332186/)).

**Prognostic factors.** **Anatomical site is the most consistent predictor of repigmentation**: *"Anatomical site was the most consistent predictor, with facial lesions showing the highest repigmentation rates and acral areas demonstrating poor response"* ([PMID: 41840918](https://pubmed.ncbi.nlm.nih.gov/41840918/)). With povorcitinib, head/neck VASI50 response was **57.3%** vs feet **25.8%** ([PMID: 42440041](https://pubmed.ncbi.nlm.nih.gov/42440041/)). Early clinical improvement predicts better long-term outcome; **leukotrichia** predicts poorer response (follicular reservoir loss; [PMID: 30971534](https://pubmed.ncbi.nlm.nih.gov/30971534/)).

**Prognostic biomarkers.** Exploratory: *"Exploratory biomarker data suggested that Th2 cytokine profiles and reductions in CXCL10 levels may be linked to response"* ([PMID: 41840918](https://pubmed.ncbi.nlm.nih.gov/41840918/)).

**Relapse.** Common after therapy withdrawal due to persistent TRM ([PMID: 30423329](https://pubmed.ncbi.nlm.nih.gov/30423329/)).

**Special context — melanoma.** ICI-induced vitiligo correlates with **favorable melanoma prognosis**: *"Vitiligo, a distinctive cutaneous immune-related adverse event, correlates with favorable prognosis in melanoma patients"* (591 FAERS cases; ipilimumab-pembrolizumab ROR 97.2; [PMID: 42299605](https://pubmed.ncbi.nlm.nih.gov/42299605/)).

---

## 12. Treatment

Treatment targets the **JAK/STAT–IFN-γ effector axis** (immune suppression) and **restores melanocytes** (regeneration). MAXO annotations are suggested where applicable.

### Pharmacotherapy

| Therapy | Class / MoA | Key efficacy | Evidence |
|---|---|---|---|
| **Topical ruxolitinib 1.5% cream** | JAK1/2 inhibitor (FDA-approved) | Week 24 F-VASI75: **29.8%** vs 7.4% vehicle (TRuE-V1); **30.9%** vs 11.4% (TRuE-V2); Week 52 F-VASI75 **50.3%** (continuous) | [PMID: 36260792](https://pubmed.ncbi.nlm.nih.gov/36260792/); [PMID: 40156697](https://pubmed.ncbi.nlm.nih.gov/40156697/) |
| **Oral povorcitinib** | JAK1 inhibitor | Week 24 T-VASI improvement vs placebo (P<.01); Week 52: T-VASI50 **34.0%**, F-VASI50 **61.2%**, F-VASI75 **45.6%** | [PMID: 40518122](https://pubmed.ncbi.nlm.nih.gov/40518122/); [PMID: 42440041](https://pubmed.ncbi.nlm.nih.gov/42440041/) |
| **Oral upadacitinib, ritlecitinib** | JAK1 / JAK3-TEC inhibitors | Promising in trials; upadacitinib used post-grafting | [PMID: 40996476](https://pubmed.ncbi.nlm.nih.gov/40996476/); [PMID: 40832814](https://pubmed.ncbi.nlm.nih.gov/40832814/) |
| Topical corticosteroids / calcineurin inhibitors | Immunosuppression | Mainstay first-line | [PMID: 40996476](https://pubmed.ncbi.nlm.nih.gov/40996476/) |
| Monoclonal antibodies (anifrolumab) | Type-1 IFN receptor | Phase 2/3 pipeline | [PMID: 40417830](https://pubmed.ncbi.nlm.nih.gov/40417830/) |

**Safety of ruxolitinib.** *"No serious treatment-related TEAEs were reported with ruxolitinib cream"* over 104 weeks; most common TEAEs were nasopharyngitis and application-site acne ([PMID: 41125994](https://pubmed.ncbi.nlm.nih.gov/41125994/)). Oral JAK inhibitors require monitoring for infection, hematologic, and cardiovascular risk ([PMID: 40996476](https://pubmed.ncbi.nlm.nih.gov/40996476/)).

### Phototherapy

**NB-UVB** is first-line and dual-acting. It *"promotes the migration of melanocyte stem cells (MelSC) to the epidermis, thus restoring pigmentation in affected individuals"* ([PMID: 42377206](https://pubmed.ncbi.nlm.nih.gov/42377206/)) and depletes pathogenic memory T cells: *"TRM declined in acral (5.95 [3.17-7.41] to 0.65 [0.15-1.15]; pFDR = 0.0039) and non-acral sites (4.12 [2.50-5.57] to 0.69 [0.28-1.19]; pFDR = 0.0039)"* ([PMID: 42415499](https://pubmed.ncbi.nlm.nih.gov/42415499/)). NB-UVB remains a cost-effective first-line therapy ([PMID: 42323047](https://pubmed.ncbi.nlm.nih.gov/42323047/)). 308-nm excimer laser targets localized lesions.

### Combination and surgical

- **JAK inhibitor + NB-UVB** is superior to NB-UVB alone: *"Combination therapy significantly reduced total VASI compared to controls (MD = -4.96, 95% CI [-9.29, -0.63])"* ([PMID: 41454839](https://pubmed.ncbi.nlm.nih.gov/41454839/)).
- **Surgical melanocyte grafting** (non-cultured epidermal cell suspension, NCES) for **stable/segmental** disease, often with adjunctive JAK inhibitor or corticosteroid; best on face/trunk ([PMID: 40832814](https://pubmed.ncbi.nlm.nih.gov/40832814/)).

**Suggested MAXO terms:** MAXO:0000058 (pharmacotherapy); JAK inhibitor therapy (conceptual); MAXO:0000596 (phototherapy); MAXO:0000424 (corticosteroid therapy); MAXO:0000937 (surgical treatment / skin grafting).

---

## 13. Prevention

- **Primary prevention:** Avoid known chemical triggers (phenolic/catechol compounds, e.g., occupational monobenzone exposure) and minimize skin trauma (Koebner) in predisposed individuals. No vaccine or population-level prevention exists.
- **Secondary prevention:** **Thyroid screening** in vitiligo patients for early detection of comorbid autoimmune thyroid disease ([PMID: 42479635](https://pubmed.ncbi.nlm.nih.gov/42479635/)); early treatment of active disease to preserve melanocyte reservoir.
- **Tertiary prevention:** Sun protection of depigmented (melanin-deficient) skin to prevent burns; maintenance therapy and psychological support to prevent relapse and QoL decline.
- **Genetic counseling:** Given polygenic inheritance, counseling addresses modestly elevated familial risk rather than Mendelian recurrence.

---

## 14. Other Species / Natural Disease

- **Naturally occurring vitiligo in horses:** *"Vitiligo is a depigmentation autoimmune disorder characterized by the progressive loss of melanocytes leading to the appearance of patchy depigmentation of the skin. The presence of vitiligo in horses is greater in those with grey coats"* ([PMID: 39199954](https://pubmed.ncbi.nlm.nih.gov/39199954/)). A genomic study in the Pura Raza Español (Andalusian) horse explored its genetic landscape.
- Vitiligo-like depigmentation is also documented in dogs, cats, and other mammals (companion-animal veterinary relevance).
- **Orthologous genes** (IFNG, CXCL10, TYR, MITF) are conserved across mammals, supporting cross-species mechanistic conservation.
- **Taxonomy:** *Homo sapiens* (NCBI:txid9606); *Equus caballus* (NCBI:txid9796); *Mus musculus* (NCBI:txid10090).
- No zoonotic potential (non-infectious).

---

## 15. Model Organisms

| Model | Type | Key features / recapitulation | Evidence |
|---|---|---|---|
| **Monobenzone-induced C57BL/6 mouse** | Chemical/environmental | Oxidative-stress- and CD8+ T-cell-mediated depigmentation; standard therapeutic testbed | [PMID: 42230481](https://pubmed.ncbi.nlm.nih.gov/42230481/); [PMID: 40780471](https://pubmed.ncbi.nlm.nih.gov/40780471/); [PMID: 38542385](https://pubmed.ncbi.nlm.nih.gov/38542385/) |
| **Melanocyte-specific CD8+ T-cell adoptive-transfer mouse** | Genetic/immunologic | IFN-γ signature, skin CXCL10, CXCR3 upregulation; TRM/Tcm maintain disease and relapse | [PMID: 24523323](https://pubmed.ncbi.nlm.nih.gov/24523323/); [PMID: 30423329](https://pubmed.ncbi.nlm.nih.gov/30423329/) |
| **H2O2-induced mouse** | Oxidative stress | NPY/NF-κB-driven CD8+ infiltration | [PMID: 42031917](https://pubmed.ncbi.nlm.nih.gov/42031917/) |
| **Zebrafish; B16F10 & PIG1 cells** | In vitro / lower vertebrate | Melanogenesis (MITF, TYR, cAMP/PKA/CREB) | [PMID: 41720011](https://pubmed.ncbi.nlm.nih.gov/41720011/) |

**Applications:** These models dissect the oxidative-stress→immune cascade, validate the CXCL10/JAK-STAT axis as a therapeutic target, and screen candidate drugs. The adoptive-transfer mouse specifically models TRM-maintained relapse: *"Tissue resident memory T cells (Trm) form in the skin in vitiligo and persist to maintain disease, as white spots often recur rapidly after discontinuing therapy"* ([PMID: 30423329](https://pubmed.ncbi.nlm.nih.gov/30423329/)). **Limitations:** mouse models are typically induced (not spontaneous polygenic), may not fully capture human HLA-restricted antigen specificity, disease chronicity, or the psychosocial dimension. **Resources:** MGI (mouse), ZFIN (zebrafish), Cellosaurus (PIG1, B16F10).

---

## Mechanistic Model / Interpretation

Vitiligo is best understood as a **two-hit convergence disease**: a *genetically encoded melanocyte fragility* (hit 1) meets an *environmental/oxidative trigger* (hit 2), and the collision releases DAMPs that convert local stress into a systemic, self-sustaining autoimmune attack. The 12 confirmed findings assemble into a single, therapeutically actionable pathway:

```
[Genetics: >50 loci] ──► [Melanocyte oxidative fragility + adhesion loss]
        (F002, F008)                     │
                                         ▼
                        [DAMPs: HSP70/HMGB1/IL-15]  (F008)
                                         │
                                         ▼
                        [Innate + type-1 IFN priming] (F008)
                                         │
                                         ▼
        [IFN-γ ─► CXCL9/CXCL10 ─► CXCR3 ─► CD8+ T cell] (F001, F004)
                                         │
                        ┌────────────────┴───────────────┐
                        ▼                                 ▼
             [Melanocyte apoptosis ─► white macules]   [TRM maintenance ─► relapse]
                        (F001, F005)                    (F007, F011)
                                         │
          ┌──────────────────────────────┴───────────────────────────┐
          ▼                                                           ▼
 [Immune blockade: JAK inhibitors, NB-UVB T-cell depletion]   [Melanocyte regeneration:
       (F003, F007, F010)                                        NB-UVB MelSC, grafting] (F007, F010)
                                         │
                                         ▼
                         [Repigmentation — site-dependent] (F011)
```

The **IFN-γ–CXCL10–CXCR3** node is both the mechanistic hub and the clinical fulcrum: every effective modern therapy (topical/oral JAK inhibitors, NB-UVB, combination) suppresses this node, while durable cure is limited by **TRM persistence** — the single best explanation for the field's central clinical frustration (relapse). Prognosis tracks the **follicular melanocyte reservoir**, which is why facial lesions (rich in follicles) outperform acral lesions (sparse follicles), and why leukotrichia is a bad sign.

---

## Evidence Base

| PMID | Contribution | Supports |
|---|---|---|
| [42332186](https://pubmed.ncbi.nlm.nih.gov/42332186/) | Definition, 0.5–2% prevalence | F001 |
| [39739902](https://pubmed.ncbi.nlm.nih.gov/39739902/) | CD8+ T cells in early SV; SV mosaicism/fraction | F001, F005 |
| [28317533](https://pubmed.ncbi.nlm.nih.gov/28317533/), [39890561](https://pubmed.ncbi.nlm.nih.gov/39890561/) | ~50→>50 GWAS loci; immunity/oxidative/melanogenesis | F002 |
| [23773036](https://pubmed.ncbi.nlm.nih.gov/23773036/), [29152150](https://pubmed.ncbi.nlm.nih.gov/29152150/) | NLRP1 GCT haplotype ≈2× risk | F002 |
| [41884389](https://pubmed.ncbi.nlm.nih.gov/41884389/) | STAT2–TAPBP multi-omics axis | F002 |
| [36260792](https://pubmed.ncbi.nlm.nih.gov/36260792/), [40156697](https://pubmed.ncbi.nlm.nih.gov/40156697/), [41125994](https://pubmed.ncbi.nlm.nih.gov/41125994/) | Topical ruxolitinib efficacy & long-term safety | F003 |
| [24523323](https://pubmed.ncbi.nlm.nih.gov/24523323/) | CXCL9 vs CXCL10 roles; reversal by neutralization | F004 |
| [25521459](https://pubmed.ncbi.nlm.nih.gov/25521459/) | Simvastatin/STAT1 prevents & reverses | F004 |
| [22417114](https://pubmed.ncbi.nlm.nih.gov/22417114/), [28685247](https://pubmed.ncbi.nlm.nih.gov/28685247/) | VGICC classification; prevalence/defining lesion | F005 |
| [42479635](https://pubmed.ncbi.nlm.nih.gov/42479635/), [42299605](https://pubmed.ncbi.nlm.nih.gov/42299605/) | Childhood onset, thyroid comorbidity; ICI-vitiligo/melanoma | F006 |
| [42377206](https://pubmed.ncbi.nlm.nih.gov/42377206/), [42415499](https://pubmed.ncbi.nlm.nih.gov/42415499/), [42323047](https://pubmed.ncbi.nlm.nih.gov/42323047/) | NB-UVB MelSC migration + TRM depletion | F007 |
| [36154894](https://pubmed.ncbi.nlm.nih.gov/36154894/), [35643735](https://pubmed.ncbi.nlm.nih.gov/35643735/), [36345598](https://pubmed.ncbi.nlm.nih.gov/36345598/), [36947026](https://pubmed.ncbi.nlm.nih.gov/36947026/) | DAMPs, adhesion loss, HSPA1L protective allele | F008 |
| [30423329](https://pubmed.ncbi.nlm.nih.gov/30423329/), [42230481](https://pubmed.ncbi.nlm.nih.gov/42230481/), [39199954](https://pubmed.ncbi.nlm.nih.gov/39199954/) | Mouse models; TRM; horse natural disease | F009 |
| [40518122](https://pubmed.ncbi.nlm.nih.gov/40518122/), [42440041](https://pubmed.ncbi.nlm.nih.gov/42440041/), [41454839](https://pubmed.ncbi.nlm.nih.gov/41454839/), [40832814](https://pubmed.ncbi.nlm.nih.gov/40832814/) | Oral povorcitinib; JAK+NB-UVB; grafting | F010 |
| [41840918](https://pubmed.ncbi.nlm.nih.gov/41840918/) | Site as key prognostic factor; biomarkers | F011 |
| [41703718](https://pubmed.ncbi.nlm.nih.gov/41703718/), [42087462](https://pubmed.ncbi.nlm.nih.gov/42087462/) | Clinical/RCM diagnostics; IFN-γ/CXCL biomarkers | F012 |

---

## Limitations and Knowledge Gaps

1. **No primary dataset of origin.** This report synthesizes published aggregate/disease-level evidence rather than analyzing a raw patient dataset; effect sizes are quoted from source studies.
2. **TRM eradication remains unsolved.** No approved therapy durably eliminates skin-resident memory T cells; relapse biology (IL-15/IL-15R, TRM survival) is an open target.
3. **Predictive biomarkers are exploratory.** CXCL10/Th2 signatures show promise but lack prospective validation and standardized cutoffs.
4. **Genetic risk is incompletely explained.** >50 loci account for only part of heritability; gene–environment and epigenetic contributions are underquantified; monozygotic-twin discordance is unexplained mechanistically.
5. **Acral disease is refractory.** The follicular-reservoir hypothesis explains but does not solve poor acral repigmentation.
6. **Segmental vitiligo mechanism** (somatic mosaicism vs neuronal) is not definitively resolved.
7. **Model limitations.** Induced mouse models may not capture human HLA-restricted antigen specificity, chronicity, or psychosocial burden.

---

## Proposed Follow-up Experiments / Actions

1. **TRM-targeted therapy trials:** Test IL-15/IL-15Rβ (CD122) blockade or JAK inhibitors specifically for durable, relapse-free maintenance after repigmentation.
2. **Prospective biomarker validation:** Validate serum/skin CXCL10 (and Th2 profiles) as predictive/response biomarkers in a prospective multicenter cohort with standardized thresholds.
3. **Acral-specific regeneration strategies:** Combine melanocyte-stem-cell mobilizers (Wnt/PKA-CREB agonists; [PMID: 41720011](https://pubmed.ncbi.nlm.nih.gov/41720011/)) with immune blockade and grafting for acral lesions.
4. **Genotype-guided precision medicine:** Correlate HLA/NLRP1/TAPBP genotypes with JAK-inhibitor response to enable stratified treatment.
5. **Systematic thyroid & autoimmune screening protocol:** Formalize periodic thyroid function/antibody screening in vitiligo care pathways ([PMID: 42479635](https://pubmed.ncbi.nlm.nih.gov/42479635/)).
6. **Head-to-head and combination RCTs:** Directly compare topical ruxolitinib vs NB-UVB vs their combination, and oral vs topical JAK inhibitors, with QoL endpoints.
7. **Neuro-immune axis exploration:** Investigate NPY2R antagonism and vagus-nerve stimulation ([PMID: 42031917](https://pubmed.ncbi.nlm.nih.gov/42031917/); [PMID: 38542385](https://pubmed.ncbi.nlm.nih.gov/38542385/)) as adjuncts targeting stress-driven flares.

---

*Report compiled from 12 confirmed findings across 53 reviewed papers spanning genetics, immunology, clinical trials, diagnostics, and comparative/model biology. Evidence source types span human clinical (GWAS, RCTs, cohorts), model organism (mouse, horse, zebrafish), and in vitro (melanocyte/keratinocyte) studies.*


## Artifacts

- [OpenScientist final report](Vitiligo-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Vitiligo-deep-research-openscientist_artifacts/final_report.pdf)
