---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T10:12:36.674624'
end_time: '2026-08-28T10:55:18.738070'
duration_seconds: 2562.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunodeficiency 92
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
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 8
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_92-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_92-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 92
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 92** covering all of the
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

# Immunodeficiency 92 (IMD92): Comprehensive Disease Characteristics Report

**Disease:** Immunodeficiency 92 (IMD92)
**Cause:** Biallelic loss-of-function variants in *REL* (c-Rel deficiency)
**Category:** Mendelian, autosomal recessive
**OMIM:** #619652 | **MONDO:** MONDO:0030498 | **Gene:** *REL* (HGNC:9954, NCBI Gene 5966, MIM \*164910)

---

## Summary

Immunodeficiency 92 (IMD92) is an ultra-rare autosomal recessive **combined immunodeficiency (CID)** caused by **biallelic (homozygous) loss-of-function variants in *REL***, the gene encoding **c-Rel**, one of the five members of the NF-κB transcription-factor family and a core subunit of the canonical NF-κB pathway. c-Rel is selectively expressed in lymphoid and myeloid cells, where it controls the transcriptional programs required for effective adaptive and innate immunity. When c-Rel is absent, patients develop early-childhood susceptibility to a broad spectrum of **viral, bacterial, fungal, and parasitic pathogens**, including intracellular organisms such as *Mycobacterium tuberculosis*, *Salmonella*, *Cryptosporidium*, and cytomegalovirus (CMV), typically accompanied by **hypogammaglobulinemia** and impaired T- and B-cell function.

As of 2026, IMD92 remains **exceedingly rare — only three patients from three consanguineous families have been reported worldwide** (Beaussant-Cohen 2019; Lévy 2021; El-Hamri 2026). Each patient carried a distinct homozygous *REL* null allele: a canonical splice-site variant (c.535+1G>A), an undefined loss-of-function allele, and a frameshift (c.24del, p.Tyr9Ilefs\*2), respectively. Functional studies across these patients converge on a unified mechanism: c-Rel loss simultaneously cripples **myeloid** immunity (abolished IL-12/IL-23 production by conventional type-1 dendritic cells [cDC1s] and monocytes; impaired CD86-dependent antigen presentation) and **lymphoid** immunity (reduced regulatory T cells [Tregs], memory CD4+/CD8+ T cells, NK cells, and memory B cells; defective naive-T-cell IL-2 production; impaired B-cell proliferation and antibody production).

The human phenotype is faithfully recapitulated by the ***Rel*-knockout mouse**, which shows impaired humoral immunity, mitogen-unresponsive B and T lymphocytes, and an IL-2–dependent T-cell proliferation defect — establishing a robust, evolutionarily conserved genotype-phenotype relationship. Management follows general combined-immunodeficiency standards: **immunoglobulin replacement, anti-infective prophylaxis, and allogeneic hematopoietic stem cell transplantation (HSCT)** as the rational curative approach. This report compiles the available evidence across all 15 requested disease-characteristic domains, explicitly flagging the many areas where data do not yet exist for this newly described, ultra-rare disorder.

---

## Key Findings

### Finding 1 — IMD92 is an autosomal recessive combined immunodeficiency caused by biallelic *REL* loss-of-function (c-Rel deficiency)

IMD92 (OMIM #619652) is defined by **biallelic loss-of-function variants in *REL*** (chromosome 2p16.1), which encodes the NF-κB subunit c-Rel. The gene identifiers are HGNC:9954, NCBI Gene 5966, and MIM \*164910. The index patient carried a homozygous *REL* null mutation abrogating c-Rel protein expression (Beaussant-Cohen 2019, [PMID: 31103457](https://pubmed.ncbi.nlm.nih.gov/31103457/)). The most recently reported patient (2026) carried a homozygous frameshift variant, **NM_001291746.4:REL:c.24del, p.(Tyr9Ilefs\*2)**, with Western blotting confirming severe c-Rel reduction while p65/RelA was preserved (El-Hamri 2026, [PMID: 42117340](https://pubmed.ncbi.nlm.nih.gov/42117340/)). The 2026 report states the disorder is *"immunodeficiency 92 (IMD92), an extremely rare autosomal recessive disorder due to c Rel deficiency that results from pathogenic variants of the REL gene"* and *"identified a novel homozygous frameshift variant (NM_001291746.4) REL:c.24del p.(Tyr9Ilefs\*2)."* Only three patients have been reported worldwide, defining IMD92 as an **ultra-rare Mendelian inborn error of immunity**.

### Finding 2 — Phenotype: broad susceptibility to intracellular/opportunistic pathogens, chronic diarrhea, and possible neuro-developmental features

The index patient presented with a combined immunodeficiency characterized by susceptibility to **intracellular and opportunistic pathogens — *Mycobacterium tuberculosis*, *Salmonella*, *Cryptosporidium*, and CMV** (Beaussant-Cohen 2019, [PMID: 31103457](https://pubmed.ncbi.nlm.nih.gov/31103457/)). The third patient — a 5-year-old Moroccan child from a consanguineous family — was described as *"a 5-year-old Moroccan child with combined immunodeficiency presenting with chronic diarrhea and recurrent opportunistic infections, alongside newly reported features including craniosynostosis, language delay, and epilepsy"* (El-Hamri 2026, [PMID: 42117340](https://pubmed.ncbi.nlm.nih.gov/42117340/)). Whether the neuro-developmental and craniofacial features are core to IMD92 or incidental (e.g., related to consanguinity or a second variant) remains uncertain given the tiny patient number.

### Finding 3 — Mechanism: c-Rel is a canonical NF-κB subunit controlling Treg development, T-cell effector function, and myeloid cytokine output

c-Rel is one of five NF-κB family members and, per El-Hamri 2026, *"c Rel is a key actor of the NF-κB pathway with major implications in the immune response"* ([PMID: 42117340](https://pubmed.ncbi.nlm.nih.gov/42117340/); see also [PMID: 42261849](https://pubmed.ncbi.nlm.nih.gov/42261849/)). NF-κB transcription factors have *"essential functions... in modulating Treg development and function, with some of these mechanistic insights confirmed by recent studies analyzing Treg cells from patients harboring point mutations in the genes encoding NF-κB proteins"* ([PMID: 35672519](https://pubmed.ncbi.nlm.nih.gov/35672519/)). Mouse studies show *Rel*-deficient T cells have *"defects in production of interleukin 3 and granulocyte-macrophage colony-stimulating factor"* ([PMID: 8622948](https://pubmed.ncbi.nlm.nih.gov/8622948/)), and c-Rel drives IL-2/IFN-γ transcription while promoting FOXP3/Treg programs ([PMID: 41410797](https://pubmed.ncbi.nlm.nih.gov/41410797/)).

### Finding 4 — Index patient: homozygous *REL* splice variant c.535+1G>A with detailed combined immunophenotype

Beaussant-Cohen 2019 ([PMID: 31103457](https://pubmed.ncbi.nlm.nih.gov/31103457/); PMC6688935) described a male proband homozygous for a canonical donor splice-site variant **REL NM_002908.3:c.535+1G>A** (chr2:61144153 G/A, GRCh37), **absent from gnomAD and 1000 Genomes**, and heterozygous in unaffected parents and a healthy brother (consistent with autosomal recessive segregation). The mutant transcript uses cryptic splice sites and lacks 54 nucleotides encoding 18 residues within the **Rel homology domain**, abrogating c-Rel protein. The immunophenotype (age 6) is summarized in the table below.

| Parameter | Finding | Reference range |
|---|---|---|
| WBC | Leukocytosis / lymphocytosis / thrombocytosis | — |
| CD4+ / CD8+ T cells | Increased | — |
| Memory CD4+CD45RO+ T cells | Decreased | — |
| PHA proliferation | 47.3% (reduced) | — |
| B cells | B-cell lymphopenia | — |
| B-cell proliferation (CD40L+IL-21) | 6.4% (impaired) | — |
| IgG | 150 mg/dL | 650–1150 |
| IgM | 150 mg/dL | — |
| IgA | Undetectable | — |
| Anti-diphtheria titer | 0.015 IU/mL (non-protective, despite boosters) | — |
| Switched memory B cells | 0.3% | 10.0–30.4% |

The patient was treated with **IVIG plus antibiotic prophylaxis** and evaluated for **HSCT**. The dual role of c-Rel in the immune response underlies this combined immunophenotype (*"c Rel is a key actor of the NF-κB pathway with major implications in the immune response"*, [PMID: 42117340](https://pubmed.ncbi.nlm.nih.gov/42117340/)).

### Finding 5 — Second patient (Lévy 2021, JCI): the myeloid+lymphoid mechanism defined

Lévy et al. 2021 (*J Clin Invest* 131(17):e150143; [PMID: 34623332](https://pubmed.ncbi.nlm.nih.gov/34623332/); Casanova/Puel laboratory) *"studied a child with severe viral, bacterial, fungal, and parasitic diseases, who was homozygous for a loss-of-function mutation of REL, encoding c-Rel, which is selectively expressed in lymphoid and myeloid cells."* This study delineated the dual mechanism:

- **Myeloid defects:** *"Functional deficits of myeloid cells included the abolition of IL-12 and IL-23 production by conventional DC1s (cDC1s) and monocytes, but not cDC2s."* c-Rel was also required for CD86 induction and the antigen-presenting function of conventional dendritic cells.
- **Lymphoid defects:** *"low frequencies of NK, effector memory cells reexpressing CD45RA (Temra) CD8+ T cells, memory CD4+ T cells, including Th1 and Th1\*, Tregs, and memory B cells."* Naive T cells produced reduced IL-2, impairing proliferation/survival, with poor Th1/Th2/Th17 cytokine output by memory CD4+ T cells.

The patient was from Casablanca, Morocco.

### Finding 6 — *Rel*-knockout mice faithfully recapitulate the human IMD92 immune defect

*Rel*-null mice show normal development of all hematopoietic lineages but *"humoral immunity was impaired and mature B and T cells were found to be unresponsive to most mitogenic stimuli"* (Köntgen et al. 1995, *Genes Dev*, [PMID: 7649478](https://pubmed.ncbi.nlm.nih.gov/7649478/)). Critically, *"the ability of exogenous interleukin-2 to restore T cell, but not B cell, proliferation indicates that Rel regulates the expression of different genes in B and T cells."* Gerondakis et al. 1996 independently confirmed that *"mice lacking Rel are defective in mitogenic activation of B and T lymphocytes and display impaired humoral immunity"* ([PMID: 8622948](https://pubmed.ncbi.nlm.nih.gov/8622948/)). These murine phenotypes match the human patients' impaired PHA/T-cell proliferation, hypogammaglobulinemia, and IL-2 deficit, establishing a conserved genotype–phenotype mechanism.

---

## Mechanistic Model / Interpretation

The pathophysiology of IMD92 flows directly from loss of the c-Rel transcription factor in immune cells:

```
   Biallelic REL LOF (c.535+1G>A / c.24del / other null)
                        │
                        ▼
             Absent / severely reduced c-Rel protein
       (Rel homology domain disrupted; p65/RelA preserved)
                        │
        ┌───────────────┴────────────────┐
        ▼                                 ▼
   MYELOID ARM                       LYMPHOID ARM
   • cDC1 + monocyte                 • ↓ naive-T IL-2 → poor
     IL-12/IL-23 abolished             proliferation/survival
   • ↓ CD86 induction →              • ↓ Tregs (FOXP3 program)
     impaired antigen                • ↓ memory CD4+ (Th1/Th1*),
     presentation                      CD8+ Temra, NK cells
        │                             • ↓ memory/switched B cells,
        │                               impaired antibody production
        └───────────────┬────────────────┘
                        ▼
        Defective Th1 / intracellular-pathogen immunity
        + hypogammaglobulinemia + poor vaccine responses
                        │
                        ▼
   Combined immunodeficiency: susceptibility to viral, bacterial,
   fungal, parasitic (M. tuberculosis, Salmonella, Cryptosporidium,
   CMV) infections; chronic diarrhea; early childhood onset
```

**Upstream vs downstream:** The upstream lesion is transcriptional — loss of c-Rel–dependent gene programs. Downstream consequences are the failure of key cytokine axes, most importantly the **IL-12/IL-23 → Th1/IFN-γ axis** (explaining mycobacterial and intracellular-pathogen susceptibility) and the **IL-2 → T-cell expansion axis** — plus impaired humoral immunity. The myeloid defect (antigen-presenting-cell cytokine failure) and the lymphoid defect (intrinsic T/B-cell dysfunction) are additive, producing a broader infection spectrum than a purely lymphoid CID.

**Ontology term suggestions:**
- **Gene/Protein:** *REL* / c-Rel (HGNC:9954, UniProt Q04864)
- **GO biological process:** GO:0038061 (canonical NF-κB signal transduction), GO:0042110 (T cell activation), GO:0050852 (T cell receptor signaling pathway), GO:0045066 (regulatory T cell differentiation), GO:0032609 (IFN-γ production), GO:0032735 (positive regulation of IL-12 production), GO:0032747 (positive regulation of IL-23 production)
- **GO cellular component:** GO:0005634 (nucleus), transcription regulator complex
- **CL cell types:** CL:0000451 (dendritic cell), CL:0002399 (CD141-positive/cDC1), CL:0000576 (monocyte), CL:0000815 (regulatory T cell), CL:0000623 (natural killer cell), CL:0000787 (memory B cell), CL:0000897 (memory CD4+ T cell)
- **UBERON:** UBERON:0002371 (bone marrow), UBERON:0002106 (spleen), UBERON:0002509 (mesenteric lymph node), UBERON:0002405 (immune system), UBERON:0000059 (large intestine — chronic diarrhea)
- **CHEBI (mediators/therapeutics):** interleukin-2, interleukin-12, interleukin-23, interferon-gamma, immunoglobulin G
- **MONDO:** MONDO:0030498

---

## Section-by-Section Report

### 1. Disease Information
IMD92 is an autosomal recessive **combined immunodeficiency** due to c-Rel deficiency. Key identifiers: **OMIM #619652; MONDO:0030498; gene *REL* (MIM \*164910)**. Orphanet, ICD-10/ICD-11, and MeSH do not yet carry a dedicated code for this ultra-rare entity; it falls under the broad category of combined immunodeficiencies (ICD-10 D81; ICD-11 4A01). Synonyms: **c-Rel deficiency; immunodeficiency due to c-Rel deficiency; REL-deficiency combined immunodeficiency.** Information is derived from **individual patient case reports** (three probands) plus aggregated disease-level curation (OMIM) and model-organism data — not from EHR/registry aggregation.

### 2. Etiology
The **sole established cause is genetic**: biallelic (homozygous) loss-of-function variants in *REL*. There are no known environmental, infectious, or acquired causes of the underlying deficiency (infections are consequences, not causes). **Genetic risk factor:** homozygosity for a *REL* null allele; **consanguinity** is a major enabling factor — the index (Kuwaiti) and third (Moroccan) families were consanguineous. No susceptibility loci, modifier genes, or protective alleles have been identified (patient numbers too small). No gene–environment interactions have been characterized. Heterozygous carriers appear healthy (parents/siblings were unaffected carriers), consistent with recessive loss-of-function.

### 3. Phenotypes
| Phenotype | Type | HPO suggestion | Notes / frequency |
|---|---|---|---|
| Recurrent/opportunistic infections | Clinical | HP:0002719 (recurrent infections) | All patients |
| Susceptibility to mycobacteria | Clinical | HP:0032266 (atypical mycobacterial infection) | Index patient |
| CMV / viral disease | Clinical | HP:0011947 | Index + patient 2 |
| Chronic diarrhea | Clinical/GI | HP:0002028 | Patient 3; *Cryptosporidium* in index |
| Decreased IgG (hypogammaglobulinemia) | Lab | HP:0004315 | IgG 150 mg/dL (index) |
| Decreased IgA | Lab | HP:0002850 | Undetectable (index) |
| Poor specific antibody response | Lab | HP:0005387 | Non-protective diphtheria/tetanus titers |
| Decreased switched memory B cells | Lab | HP:0031381 | 0.3% (ref 10–30%) |
| Reduced T-cell proliferation | Lab | abnormal T-cell proliferation | PHA 47.3% |
| Decreased Tregs / NK / memory T cells | Lab | HP:0410358, HP:0040218 | Patient 2 |
| Craniosynostosis | Physical | HP:0001363 | Patient 3 only (uncertain relatedness) |
| Language delay | Behavioral/neuro | HP:0000750 | Patient 3 only |
| Epilepsy | Clinical/neuro | HP:0001250 | Patient 3 only |

**Onset:** early childhood (index evaluated at age 6; patient 3 presented at age 5), likely reflecting a congenital immune defect. **Severity:** severe combined-immunodeficiency phenotype. **Progression:** chronic/lifelong without curative treatment. **Quality of life:** substantial impact — recurrent infections, chronic diarrhea, and lifelong immunoglobulin/prophylaxis requirements; formal QoL instruments have not been applied to this ultra-rare cohort.

### 4. Genetic / Molecular Information
**Causal gene:** *REL* (chr2p16.1; HGNC:9954; NCBI Gene 5966; MIM \*164910; UniProt Q04864). **Reported pathogenic variants:**

| Patient | Variant (nomenclature) | Type | Population frequency | Consequence |
|---|---|---|---|---|
| Index (Beaussant-Cohen 2019) | NM_002908.3:c.535+1G>A | Canonical splice donor | Absent from gnomAD & 1000G | Cryptic splicing; loss of 18 aa in Rel homology domain; no protein |
| Patient 2 (Lévy 2021) | Homozygous *REL* LOF | Loss-of-function | Rare/absent | Abolished c-Rel; loss of function |
| Patient 3 (El-Hamri 2026) | NM_001291746.4:c.24del, p.(Tyr9Ilefs\*2) | Frameshift | Rare/absent | Severe c-Rel reduction; p65/RelA preserved |

All variants are **germline, homozygous, loss-of-function** (ACMG: pathogenic). No somatic or gain-of-function IMD92 alleles exist. Note the mechanistic contrast: *REL* 3′-truncations and amplifications are recurrent oncogenic **gain-of-function** events in lymphoma ([PMID: 34695199](https://pubmed.ncbi.nlm.nih.gov/34695199/)) — the opposite of the loss-of-function that causes IMD92. No modifier genes, epigenetic drivers, or chromosomal abnormalities have been described for IMD92.

### 5. Environmental Information
No environmental toxins, radiation, or occupational exposures contribute to disease causation. **Infectious agents are downstream consequences**, not triggers: *Mycobacterium tuberculosis*, *Salmonella* spp., *Cryptosporidium* spp., cytomegalovirus, and (in patient 2) fungal and parasitic pathogens. Consanguinity (a demographic/social factor) is the principal enabling condition for homozygosity.

### 6. Mechanism / Pathophysiology
**Molecular pathway:** canonical NF-κB signaling (c-Rel–containing dimers). **Cellular processes:** T-cell activation/proliferation, Treg differentiation, dendritic-cell/monocyte cytokine production and antigen presentation, B-cell activation and antibody production. **Protein dysfunction:** loss of function via truncation/splice disruption of the Rel homology domain → absent DNA-binding transcription factor (p65/RelA preserved). **Immune involvement:** combined (myeloid + lymphoid) immunodeficiency. Key downstream axes: **IL-12/IL-23 → Th1/IFN-γ** (abolished in cDC1s/monocytes) and **IL-2 → T-cell expansion** (reduced in naive T cells). Molecular profiling of IMD92 has been limited to targeted immunophenotyping and Western blot; no patient transcriptomic/proteomic/metabolomic datasets are published. See the Mechanistic Model section above for the full causal chain and ontology terms.

### 7. Anatomical Structures Affected
**Primary system:** the immune/hematolymphoid system (UBERON:0002405). **Organs/tissues:** bone marrow (UBERON:0002371), spleen, lymph nodes, and the thymus-derived T-cell compartment; the **gastrointestinal tract** (UBERON:0000059, large intestine) via chronic diarrhea/*Cryptosporidium*. **Cell populations:** cDC1 (CL:0002399), monocytes (CL:0000576), regulatory T cells (CL:0000815), memory CD4+/CD8+ T cells, NK cells (CL:0000623), memory/switched B cells (CL:0000787). **Subcellular:** nucleus (GO:0005634) — the site of c-Rel transcriptional activity. In patient 3, additional structures (cranial sutures — craniosynostosis; CNS — epilepsy/language delay) were reported, though their causal link to *REL* is unconfirmed. Involvement is systemic/bilateral.

### 8. Temporal Development
**Onset:** pediatric/early childhood (ages 5–6 at presentation), likely a congenital immune defect manifesting with first infections. **Onset pattern:** chronic/insidious with recurrent acute infectious episodes. **Progression:** chronic and lifelong without curative HSCT; progressive infectious morbidity. **Critical period:** early diagnosis and definitive treatment (HSCT) before accumulation of infection-related organ damage is the key therapeutic window. No spontaneous remission occurs.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** appears complete in biallelic individuals; carriers unaffected. **Expressivity:** variable — patient 3 exhibited extra neuro-developmental features. **Epidemiology:** ultra-rare — only **3 reported patients worldwide** (as of 2026); prevalence/incidence not calculable. **Founder effects / carrier frequency:** unknown; *REL* LOF alleles are individually private and absent/rare in gnomAD. **Consanguinity** is central (Kuwaiti and Moroccan consanguineous families). **Demographics:** reported patients of Middle Eastern (Kuwaiti) and North African (Moroccan) origin; no established sex bias (numbers too small). **Genetic anticipation and mosaicism:** not applicable/not reported.

### 10. Diagnostics
**Laboratory:** immunoglobulin panel (hypogammaglobulinemia — low IgG/IgM, absent IgA); lymphocyte subset flow cytometry (memory B/T, Treg, NK enumeration); specific antibody titers (post-vaccination diphtheria/tetanus — non-protective); lymphocyte proliferation assays (PHA/mitogen, anti-CD3/CD28, CD40L+IL-21). **Functional immunology:** IL-12/IL-23 production by monocyte-derived/conventional DCs; IL-2 production by naive T cells; c-Rel Western blot (absent protein with preserved p65/RelA is characteristic). **Genetic testing (definitive):** whole-exome or whole-genome sequencing identifying biallelic *REL* LOF, confirmed by Sanger sequencing and family segregation. Inborn-errors-of-immunity/CID gene panels that include *REL* are appropriate. **Differential diagnosis:** other CIDs and NF-κB-pathway inborn errors of immunity — NFKB1 haploinsufficiency/CVID ([PMID: 34473196](https://pubmed.ncbi.nlm.nih.gov/34473196/)), RELA haploinsufficiency/dominant-negative disease ([PMID: 42261849](https://pubmed.ncbi.nlm.nih.gov/42261849/), [PMID: 40876844](https://pubmed.ncbi.nlm.nih.gov/40876844/)), RelB deficiency ([PMID: 42261849](https://pubmed.ncbi.nlm.nih.gov/42261849/)), A20/TNFAIP3 haploinsufficiency ([PMID: 34808442](https://pubmed.ncbi.nlm.nih.gov/34808442/)) — distinguished by inheritance pattern and immunophenotype. **Screening:** not on newborn screening panels; cascade/carrier testing feasible within affected families once the variant is known.

### 11. Outcome / Prognosis
Formal survival statistics do not exist for this 3-patient cohort. By analogy to other combined immunodeficiencies, **untreated IMD92 carries high infection-related morbidity and mortality**; with immunoglobulin replacement and anti-infective prophylaxis, acute risk is reduced, and **allogeneic HSCT offers potential cure**. Complications include recurrent/opportunistic infections, chronic diarrhea with failure to thrive, and (in patient 3) neurological morbidity. **Prognostic factors:** timeliness of diagnosis and access to HSCT; degree of pre-transplant infectious organ damage. No validated prognostic biomarkers exist beyond the immunophenotype.

### 12. Treatment
**Supportive/standard-of-care (from index patient):** **immunoglobulin (IVIG) replacement** plus **antibiotic/anti-infective prophylaxis**. **Curative:** **allogeneic hematopoietic stem cell transplantation (HSCT)** — the rational definitive therapy for a hematopoietic-intrinsic combined immunodeficiency; the index patient was evaluated for HSCT. Directed anti-infective therapy is used for specific pathogens (anti-mycobacterial, antiviral for CMV, etc.). No approved gene therapy, targeted therapy, or IMD92-specific pharmacotherapy exists, and there are no completed clinical trials (given rarity). **NCIT term suggestions:** immunoglobulin therapy (NCIT:C583), hematopoietic stem cell transplantation (NCIT:C15431), antibiotic prophylaxis. Pharmacogenomics is not applicable.

### 13. Prevention
**Primary prevention** of the genetic defect is not possible; **preconception/prenatal genetic counseling** in consanguineous families with a known *REL* variant, plus **carrier/cascade testing and preimplantation or prenatal genetic diagnosis**, can prevent recurrence. **Secondary/tertiary prevention** in affected patients: infection prophylaxis, immunoglobulin replacement, aggressive early treatment of infections, and timely HSCT to prevent cumulative organ damage. **Immunization caveat:** live vaccines are contraindicated in combined immunodeficiency, and responses to inactivated vaccines are poor (documented non-protective titers). Genetic counseling per NSGC/ACMG principles is central.

### 14. Other Species / Natural Disease
**Taxonomy / orthologs:** *REL* is conserved across mammals; the mouse ortholog is *Rel* (NCBI Gene 19696). No naturally occurring IMD92-equivalent disease has been catalogued in companion animals or wildlife (no OMIA entry noted). **Comparative biology:** the *Rel*-knockout mouse (below) demonstrates strong evolutionary conservation of c-Rel's role in lymphocyte activation and humoral immunity. No zoonotic dimension.

### 15. Model Organisms
The principal model is the ***Rel*-knockout mouse** (mammalian germline knockout). It **faithfully recapitulates the human disease**: normal hematopoietic lineage development but impaired humoral immunity and mature B/T cells unresponsive to most mitogens; PMA+ionomycin bypasses the T-cell proliferation block; **exogenous IL-2 restores T- but not B-cell proliferation** (Köntgen 1995, [PMID: 7649478](https://pubmed.ncbi.nlm.nih.gov/7649478/)). *Rel*-/- T cells show normal activation markers (CD25/CD69/CD62L) but impaired cytokine production and fail to proliferate after anti-CD3/anti-CD28, rescued by IL-2 (Gerondakis 1996, [PMID: 8622948](https://pubmed.ncbi.nlm.nih.gov/8622948/)). **Recapitulation:** high for the core immune phenotype (B/T proliferation defect, humoral immunodeficiency, IL-2 dependence). **Limitations:** mouse models do not capture the human-specific infection spectrum, the neuro-developmental features seen in patient 3, or all human myeloid IL-12/IL-23 nuances. **Resources:** MGI (*Rel*); a CRISPR knock-in strategy for conditional human c-Rel expression in mouse T cells has been reported but encountered locus-specific silencing (promoter CpG methylation) challenges ([PMID: 41410797](https://pubmed.ncbi.nlm.nih.gov/41410797/)).

---

## Evidence Base

| PMID | Study | Role in this report |
|---|---|---|
| [31103457](https://pubmed.ncbi.nlm.nih.gov/31103457/) | Beaussant-Cohen 2019 — *Combined immunodeficiency in a patient with c-Rel deficiency* | **First patient**; defines disease, splice variant c.535+1G>A, detailed immunophenotype, IVIG+prophylaxis, HSCT evaluation |
| [34623332](https://pubmed.ncbi.nlm.nih.gov/34623332/) | Lévy 2021 (*JCI*) — *Inherited human c-Rel deficiency disrupts myeloid and lymphoid immunity to multiple infectious agents* | **Second patient**; defines the dual myeloid (IL-12/IL-23, CD86) + lymphoid (Treg, memory T/B, NK, IL-2) mechanism |
| [42117340](https://pubmed.ncbi.nlm.nih.gov/42117340/) | El-Hamri 2026 — *A Novel Biallelic REL Frameshift Variant p.(Tyr9Ilefs\*2) Causing IMD92* | **Third patient**; frameshift variant, profound c-Rel deficiency by Western blot, expanded phenotype (craniosynostosis, epilepsy, language delay); confirms AR inheritance and disease name |
| [7649478](https://pubmed.ncbi.nlm.nih.gov/7649478/) | Köntgen 1995 (*Genes Dev*) — *Rel*-null mice | Mouse model recapitulates impaired humoral immunity, mitogen unresponsiveness, IL-2-dependent T-cell rescue |
| [8622948](https://pubmed.ncbi.nlm.nih.gov/8622948/) | Gerondakis 1996 (*PNAS*) — *Rel*-deficient T cells | Confirms lymphocyte activation/humoral defects; IL-3/GM-CSF and cytokine production deficits |
| [35672519](https://pubmed.ncbi.nlm.nih.gov/35672519/) | Review — *NF-κB in control of regulatory T cell development, identity, and function* | Supports c-Rel/NF-κB role in Treg biology, linked to human NF-κB-mutation patients |
| [42261849](https://pubmed.ncbi.nlm.nih.gov/42261849/) | Review — *Inborn Errors of Immunity in the NF-κB Pathway* | Context: c-Rel within canonical NF-κB; differential diagnosis (RELA, RelB) |
| [41410797](https://pubmed.ncbi.nlm.nih.gov/41410797/) | c-Rel conditional knock-in mouse design | c-Rel drives IL-2/IFN-γ, represses FOXP3; model-engineering resource and caveats |
| [34473196](https://pubmed.ncbi.nlm.nih.gov/34473196/) | NFKB1 variants → AD CVID | Differential diagnosis (contrasting NF-κB inborn error, haploinsufficiency) |
| [34695199](https://pubmed.ncbi.nlm.nih.gov/34695199/) | WGS of adult T-cell leukemia/lymphoma | Contrast: *REL* 3′-truncations are oncogenic gain-of-function (opposite of IMD92 LOF) |

**Evidence source types:** human clinical (3 case reports), model organism (mouse knockouts), and in vitro functional immunology (patient cell assays). All primary mechanistic and clinical claims are anchored to the citation snippets validated during the investigation.

---

## Limitations and Knowledge Gaps

1. **Extreme rarity (n=3).** All clinical conclusions rest on three case reports; prevalence, incidence, penetrance ranges, expressivity, survival, and prognosis cannot be quantified statistically.
2. **Uncertain phenotype boundaries.** Craniosynostosis, epilepsy, and language delay were reported in only one patient (patient 3); it is unclear whether these are core IMD92 features, effects of a second recessive locus, or coincidental consanguinity-related findings.
3. **No natural history or registry data.** Disease course, long-term HSCT outcomes, and quality-of-life metrics are undefined.
4. **No omics depth.** No transcriptomic, proteomic, metabolomic, or single-cell datasets specific to IMD92 patients are published; mechanistic detail derives from targeted assays and mouse models.
5. **No therapeutics evidence base.** Treatment recommendations are extrapolated from general CID management and the index case; no trials, response rates, or adverse-event data exist.
6. **Population genetics unknown.** Carrier frequencies, founder effects, and geographic variant distribution are uncharacterized.

## Proposed Follow-up Experiments / Actions

1. **Establish an international IMD92 patient registry** (via IUIS/inborn-errors-of-immunity networks) to aggregate cases, standardize phenotyping, and capture natural history and HSCT outcomes.
2. **Deep immunophenotyping + single-cell RNA-seq** of patient PBMCs (and, where available, tissue) to resolve cell-type-specific c-Rel-dependent transcriptional programs and validate the IL-12/IL-23 and IL-2 axis defects at single-cell resolution.
3. **Segregation and additional variant analysis in patient 3** to determine whether craniosynostosis/epilepsy/language delay are *REL*-attributable or due to a second locus (trio WGS with functional follow-up).
4. **Functional classification pipeline** for novel *REL* variants (κB-reporter and c-Rel Western blot assays), mirroring the NFKB1 approach ([PMID: 34473196](https://pubmed.ncbi.nlm.nih.gov/34473196/)), to support ACMG variant interpretation and future diagnoses.
5. **Preclinical HSCT / gene-correction studies** in the *Rel*-knockout mouse and patient-derived iPSCs to benchmark curative approaches and inform whether hematopoietic gene therapy is a viable future option.
6. **Curate ontology/database entries** (OMIM cross-links, MONDO:0030498, HPO annotations, potential Orphanet/ICD-11 coding) to improve discoverability and standardized annotation of this ultra-rare disorder.

---

*Report compiled from 6 confirmed findings and 16 reviewed papers across a 5-iteration autonomous investigation. Evidence base: human clinical case reports (n=3), mouse knockout models, and in vitro patient-cell functional studies.*


## Artifacts

- [OpenScientist final report](Immunodeficiency_92-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_92-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.