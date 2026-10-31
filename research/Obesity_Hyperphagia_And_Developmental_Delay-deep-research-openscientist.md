---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-17T04:54:45.272736'
end_time: '2026-10-17T05:12:10.230218'
duration_seconds: 1044.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Obesity, Hyperphagia, and Developmental Delay
  mondo_id: MONDO:0013483
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 19
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Obesity_Hyperphagia_And_Developmental_Delay-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Obesity_Hyperphagia_And_Developmental_Delay-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Obesity, Hyperphagia, and Developmental Delay
- **MONDO ID:** MONDO:0013483 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Obesity, Hyperphagia, and Developmental Delay** covering all of the
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

# Obesity, Hyperphagia, and Developmental Delay (MONDO:0013483) — Comprehensive Disease Dossier

**MONDO:0013483 · OMIM:613886 · Orphanet:99704 · MeSH:C563938 · UMLS:C3151303 · MedGen:462653**
**Causal gene: NTRK2 (TrkB) · HGNC:8032 · NCBI Gene 4915 · UniProt Q16620 · Ensembl ENSG00000148053 · chr9q21.33**

## Summary

**Obesity, Hyperphagia, and Developmental Delay (MONDO:0013483; OMIM:613886; Orphanet:99704; "OBHD")** is a rare, autosomal-dominant, typically *de novo* Mendelian syndrome caused by **heterozygous loss-of-function variants in *NTRK2* (HGNC:8032)**, the gene encoding **TrkB (tropomyosin receptor kinase B)**, the high-affinity receptor for **brain-derived neurotrophic factor (BDNF)**. BDNF–TrkB signaling is a critical anorexigenic ("satiety brake") node in the hypothalamic leptin–melanocortin pathway, acting *downstream* of the melanocortin-4 receptor (MC4R) in paraventricular (PVH) and dorsomedial (DMH) hypothalamic neurons. When TrkB is disabled, this satiety signal fails, producing insatiable hyperphagia and severe early-onset obesity, while TrkB's broader role in neuronal survival, differentiation, and synaptic plasticity produces global developmental delay, intellectual disability, behavioral abnormalities, hypotonia, impaired nociception, and (in some patients) seizures.

A central discovery of this investigation was a **mid-course correction**: the disease was initially mapped to *SIM1* and the 6q16 Prader–Willi-like syndrome, which is phenotypically very similar. However, the authoritative MONDO/OMIM definition of MONDO:0013483 specifies ***NTRK2*** as the causal gene. The *SIM1* and *NTRK2* disorders are distinct entities that converge on the same hypothalamic circuit — SIM1 builds the PVH and supports MC4R/oxytocin output, while TrkB transduces the satiety signal downstream — explaining their overlapping clinical pictures. This report is organized around *NTRK2*/TrkB as the definitive cause while preserving the SIM1 mechanistic insights as context for the shared circuit and differential diagnosis.

The gene shows a striking **allelic series**: loss-of-function (truncating/structure-disrupting) variants cause the milder obesity–hyperphagia–developmental delay phenotype (this disease), whereas gain-of-function variants in the transmembrane cholesterol-binding motif (recurrent p.Tyr434Cys) cause a *distinct, severe* neurodevelopmental disorder with therapy-refractory epilepsy and blindness. *NTRK2* is extremely intolerant to loss-of-function (gnomAD pLI = 1.00, LOEUF = 0.219), consistent with dominant haploinsufficiency. Diagnosis is molecular (NGS obesity gene panels, whole-exome/genome sequencing, chromosomal microarray), and management is multidisciplinary and supportive; mechanism-based melanocortin-agonist therapy is of uncertain benefit because the TrkB lesion lies downstream of MC4R.

---

## 1. Disease Information

**Overview.** OBHD is a syndromic monogenic obesity disorder defined by the triad of **early-onset severe obesity, hyperphagia (insatiable appetite), and global developmental delay**, with characteristic impairment of short-term memory and language. The MONDO record (EBI OLS) defines it as *"A syndromic disease caused by a variation in the NTRK2 gene, characterized by early-onset severe obesity, hyperphagia, and global developmental delay with specific impairment of short-term memory and language delay."*

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013483 |
| OMIM | 613886 |
| Orphanet | ORPHA:99704 |
| MeSH | C563938 |
| UMLS | C3151303 |
| MedGen | 462653 |
| Causal gene | *NTRK2* / TrkB (HGNC:8032; NCBI Gene 4915; Ensembl ENSG00000148053) |

**Synonyms / alternative names.** OBHD; Obesity-Hyperphagia-Developmental Delay syndrome; Early-onset obesity–hyperphagia–severe developmental delay syndrome; NTRK2-related obesity.

**Data source type.** Information is derived from **aggregated disease-level resources** (OMIM, Orphanet, MONDO, HPO, ClinVar, gnomAD) combined with **individual-patient case reports and a 44-individual genotype–phenotype cohort**. The index case was a single detailed patient report ([PMID: 15494731](https://pubmed.ncbi.nlm.nih.gov/15494731/)); the allelic-series delineation came from an aggregated cohort ([PMID: 39540377](https://pubmed.ncbi.nlm.nih.gov/39540377/)).

---

## 2. Etiology

**Primary cause — genetic.** The disease is caused by **heterozygous loss-of-function variants in *NTRK2***. The index patient carried a *de novo* missense variant **p.Tyr722Cys (Y722C)** that, as the authors state, *"markedly impaired receptor autophosphorylation and signaling to MAP kinase"* ([PMID: 15494731](https://pubmed.ncbi.nlm.nih.gov/15494731/)). The larger cohort established that **truncating variants, or variants that disturb the 3D protein structure leading to loss of function**, produce *"a remarkably milder phenotype of developmental delay, obesity, and hyperphagia"* ([PMID: 39540377](https://pubmed.ncbi.nlm.nih.gov/39540377/)).

**Genetic risk factors.** The causal variants are the risk factors; there are no recognized common susceptibility loci for this specific Mendelian entity. On the ligand side of the same axis, *BDNF* haploinsufficiency (e.g., WAGR 11p14 deletions) causes an overlapping obesity phenotype, confirming the pathway: WAGR patients with *BDNF* deletion *"had significantly higher BMI z scores throughout childhood than did patients with intact BDNF"* ([PMID: 18753648](https://pubmed.ncbi.nlm.nih.gov/18753648/)).

**Environmental risk factors.** As a highly penetrant Mendelian disorder, environmental contribution to *causation* is minimal. However, general obesogenic exposures (hypercaloric diet, sedentary behavior) plausibly modify the *severity* of weight gain. Rodent data show early-life hypercaloric diet alters BDNF/TrkB signaling and feeding behavior, illustrating gene–environment convergence on the same molecular axis ([PMID: 32926590](https://pubmed.ncbi.nlm.nih.gov/32926590/)).

**Protective factors.** No specific genetic protective alleles are established for this disorder. Environmentally, dietary restriction and structured feeding management reduce weight gain but do not correct the underlying hyperphagia driver.

**Gene–environment interactions.** The shared node is BDNF/TrkB tone. Reduced BDNF/TrkB signaling (genetic) and obesogenic diet (environmental) both push the same circuit toward hyperphagia, suggesting additive/synergistic weight gain in affected individuals exposed to obesogenic environments.

---

## 3. Phenotypes

The official HPO disease annotation for **OMIM:613886** (JAX HPO) and the index/cohort reports define the phenotype spectrum below. Frequencies "1/1" reflect the single annotated index proband; the cohort confirms the core triad broadly.

| Phenotype | HPO term | Type | Frequency (annotation) | Onset / notes |
|---|---|---|---|---|
| Obesity | HP:0001513 | Physical/metabolic | 1/1 | Early-onset, severe |
| Hyperphagia / polyphagia | HP:0002591 | Behavioral | 1/1 | Insatiable appetite |
| Severe global developmental delay | HP:0011344 | Neurodevelopmental | 1/1 | Infantile onset |
| Intellectual disability | HP:0001249 | Neurodevelopmental | Core | Variable severity |
| Hypotonia | HP:0001252 | Neuromuscular | 1/1 | Infantile onset |
| Motor stereotypy | HP:0000733 | Behavioral | 1/1 | — |
| Autistic behavior | HP:0000729 | Behavioral | Reported | — |
| Reduced eye contact | HP:0000817 | Behavioral | Reported | — |
| Generalized non-motor (absence) seizure | HP:0002121 | Neurological | 1/1 | — |
| Seizure (general) | HP:0001250 | Neurological | Very rare | — |
| Facial asymmetry | HP:0000324 | Physical | Reported | — |
| Delayed myelination | HP:0012448 | Neuroimaging | Very rare | — |
| Impaired pain sensation | HP:0007328 | Sensory | Index case | Blunted nociception |
| Impaired short-term memory | HP:0009074 | Cognitive | Index case | — |
| Impaired learning | HP:0001328 | Cognitive | Index case | — |
| Language delay | HP:0000750 | Neurodevelopmental | Core | — |

The index report emphasized that *"the associated impairment in memory, learning and nociception seen in the proband reflects the crucial role of TrkB in the human nervous system"* ([PMID: 15494731](https://pubmed.ncbi.nlm.nih.gov/15494731/)). The loss-of-function cohort confirmed *"developmental delay, obesity, and hyperphagia"* as the **core triad**, with cognitive impairment milder than in the gain-of-function group ([PMID: 39540377](https://pubmed.ncbi.nlm.nih.gov/39540377/)).

**Phenotype characteristics.** Onset is **infantile/early childhood** (HP:0003593 infantile onset). Severity ranges from moderate to severe; obesity and hyperphagia are typically severe and progressive if unmanaged, whereas developmental delay is static/non-progressive. **Quality-of-life impact** is substantial: insatiable hyperphagia dominates daily functioning (analogous to other MC4R-pathway hyperphagic diseases, where patients describe "unrelenting hunger"; [PMID: 42821228](https://pubmed.ncbi.nlm.nih.gov/42821228/)), and developmental delay/ID impairs independence, learning, and communication lifelong.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***NTRK2*** (neurotrophic receptor tyrosine kinase 2), encoding **TrkB**. HGNC:8032; chromosome **9q21.33** (GRCh38 chr9:~84.67–85.10 Mb); Ensembl ENSG00000148053; UniProt Q16620.

**Pathogenic variants.**
- **Index variant:** c.2165A>G, **p.Tyr722Cys (Y722C)**, *de novo* heterozygous missense in the tyrosine kinase domain. As reported: *"An 8-year-old male with a complex developmental syndrome and severe obesity was heterozygous for a de novo missense mutation resulting in a Y722C substitution"*; the variant functionally impairs autophosphorylation and MAPK signaling (**loss of function**) ([PMID: 15494731](https://pubmed.ncbi.nlm.nih.gov/15494731/)).
- **LoF group (this disease):** *"The second group had truncating variants or variants that presumably disturb the 3D structure of the protein leading to loss of function"* → obesity/hyperphagia/developmental delay ([PMID: 39540377](https://pubmed.ncbi.nlm.nih.gov/39540377/)).
- **GoF group (distinct disease):** variants in the transmembrane cholesterol-binding motif, recurrent **c.1301A>G p.(Tyr434Cys)** → upregulation of TrkB activity → severe DD/ID, refractory epilepsy, blindness ([PMID: 39540377](https://pubmed.ncbi.nlm.nih.gov/39540377/)).

**Variant classification & burden.** ClinVar (retrieved 2026-10-17): *NTRK2[gene]* returns **978 total variant records**, of which **130 are Pathogenic/Likely pathogenic**, and **49 records annotated to an obesity phenotype**. Classifications follow ACMG/AMP criteria. As the cohort noted, *"Heterozygous pathogenic variants in NTRK2 (HGNC: 8032) have been associated with global developmental delay"* ([PMID: 39540377](https://pubmed.ncbi.nlm.nih.gov/39540377/)).

**Allele frequency.** Pathogenic variants are **ultra-rare/absent in gnomAD**, consistent with *de novo* dominant disease. *NTRK2* is **extremely LoF-constrained**: gnomAD v2 pLI = **1.00**, LOEUF (oe_lof_upper) = **0.219**, observed/expected LoF = 0.138 (13 observed vs 94.5 expected), LoF-Z = 7.11; also missense-constrained (missense-Z = 5.63, oe_mis = 0.60).

**Somatic vs germline.** **Germline** (de novo or, rarely, inherited). Not a somatic/cancer entity in this context.

**Functional consequences.** **Loss of function / haploinsufficiency** for this disease (impaired kinase activity, autophosphorylation, and downstream MAPK/PI3K signaling). The allelic series demonstrates that *gain* of function produces a mechanistically and clinically opposite neurological disorder.

**Modifier genes / epigenetics / chromosomal abnormalities.** No established Mendelian modifier genes specific to *NTRK2* OBHD. Epigenetic regulation of *BDNF*/*NTRK2* (e.g., diet-induced HDAC5 changes in rodents; [PMID: 32926590](https://pubmed.ncbi.nlm.nih.gov/32926590/)) may modulate pathway tone but is not a primary disease mechanism. Large 9q21 deletions encompassing *NTRK2* would be detected by chromosomal microarray (DECIPHER/ClinVar), though point variants predominate in reported cases.

---

## 5. Environmental Information

- **Environmental factors:** No toxicological, radiation, or occupational cause. This is a monogenic disorder.
- **Lifestyle factors:** Diet and physical activity modify the *degree* of obesity but not its genetic cause. Hyperphagia makes dietary control exceptionally difficult.
- **Infectious agents:** Not applicable.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous loss-of-function variant in *NTRK2*** (de novo) **results in** a TrkB receptor with impaired kinase activity (e.g., Y722C abolishes autophosphorylation) — *demonstrated in vitro* ([PMID: 15494731](https://pubmed.ncbi.nlm.nih.gov/15494731/)).
2. Impaired TrkB **leads to** failure of **BDNF→TrkB signal transduction** (reduced MAPK/ERK and PI3K-AKT and PLCγ signaling) in TrkB-expressing neurons — *demonstrated for MAPK; PI3K/PLCγ inferred by homology to canonical TrkB signaling*.
3. In the **hypothalamic PVH and DMH**, loss of TrkB signaling **removes an anorexigenic "satiety brake"** that normally operates **downstream of MC4R** — *demonstrated by mouse circuit genetics* ([PMID: 32265438](https://pubmed.ncbi.nlm.nih.gov/32265438/), [PMID: 30718415](https://pubmed.ncbi.nlm.nih.gov/30718415/)).
4. Absent satiety signaling **results in hyperphagia** (insatiable appetite), which **precedes** weight gain — *demonstrated in Nkx2.1-Ntrk2 mice* ([PMID: 26629410](https://pubmed.ncbi.nlm.nih.gov/26629410/)).
5. Sustained hyperphagia, with **no compensatory increase in energy expenditure**, **leads to** positive energy balance and **severe early-onset obesity**, with secondary **hyperinsulinemia, hyperglycemia, and hyperleptinemia** — *demonstrated in mice* ([PMID: 26629410](https://pubmed.ncbi.nlm.nih.gov/26629410/)).

   **Branch (neurodevelopment):** In parallel, loss of TrkB signaling in **broader CNS neurons** **impairs** neuronal survival, differentiation, and synaptic plasticity, **leading to** global developmental delay, intellectual disability, impaired memory/learning, behavioral abnormalities, hypotonia, and blunted nociception — *inferred from TrkB's established neurobiology and index-patient phenotype* ([PMID: 15494731](https://pubmed.ncbi.nlm.nih.gov/15494731/)).

### Mechanistic detail

- **Molecular pathways.** Canonical TrkB signaling: **MAPK/ERK** (demonstrated defective in Y722C), **PI3K-AKT-mTOR**, and **PLCγ**. These transduce BDNF's anorexigenic and neurotrophic effects. KEGG: *Neurotrophin signaling pathway* (hsa04722); MAPK (hsa04010); PI3K-AKT (hsa04151).
- **Cellular processes.** Synaptic plasticity, neuronal survival/differentiation (neurotrophic support), and hypothalamic satiety neurotransmission. GO: *neurotrophin TRK receptor signaling pathway* (GO:0048011), *positive regulation of synaptic transmission* (GO:0050806), *regulation of eating behavior* (GO:0042755), *energy homeostasis* (GO:0097009).
- **Protein dysfunction.** Loss of receptor tyrosine kinase autophosphorylation and downstream phospho-signaling (loss of function). Gain-of-function variants (distinct disease) increase constitutive activity.
- **Metabolic changes.** Secondary: hyperinsulinemia, hyperglycemia, hyperleptinemia, increased adiposity; reduced locomotor activity and core body temperature contribute in mouse models ([PMID: 26629410](https://pubmed.ncbi.nlm.nih.gov/26629410/)).
- **Immune system.** Not a primary feature.
- **Upstream vs downstream.** **Upstream:** leptin → POMC/α-MSH → **MC4R**. **Node:** BDNF → **TrkB** acts *downstream* of MC4R in PVH/DMH. **Downstream of TrkB defect:** failed satiety → hyperphagia → obesity. This downstream position is therapeutically important (see §12).
- **Cell types & GO/CL terms.** TrkB-expressing hypothalamic neurons in PVH and DMH; broadly, central neurons. CL: *neuron* (CL:0000540), *glutamatergic neuron* (CL:0000679). GO biological processes above.

**Supporting circuit evidence (model organisms):**
- *"selective Ntrk2 deletion within paraventricular hypothalamus (PVH) leads to severe hyperphagic obesity"* ([PMID: 32265438](https://pubmed.ncbi.nlm.nih.gov/32265438/)).
- TrkB neurons in the DMH are *necessary and sufficient to suppress homeostatic feeding* ([PMID: 30718415](https://pubmed.ncbi.nlm.nih.gov/30718415/)).
- Hypothalamic TrkB ablation causes hyperphagia preceding weight gain, with hyperglycemia/hyperinsulinemia/hyperleptinemia ([PMID: 26629410](https://pubmed.ncbi.nlm.nih.gov/26629410/)).
- Human ligand evidence: BDNF-haploinsufficient (WAGR) children *"had significantly higher BMI z scores throughout childhood than did patients with intact BDNF"* ([PMID: 18753648](https://pubmed.ncbi.nlm.nih.gov/18753648/)).

### Shared-circuit context: SIM1 (differential, not causal for MONDO:0013483)

The phenotypically overlapping **6q16 deletion / SIM1 haploinsufficiency Prader–Willi-like syndrome** converges on the same PVH circuit from a different angle: SIM1 builds the PVH and sustains **MC4R and oxytocin** expression. In *Sim1⁺/⁻* mice, *"Oxt mRNA and peptide were decreased by 80% in Sim1(+/-) mice"* and central oxytocin rescues feeding ([PMID: 18451093](https://pubmed.ncbi.nlm.nih.gov/18451093/)); conditional/germline Sim1 loss shows *"a remarkable decrease in hypothalamic oxytocin (Oxt) and PVN melanocortin 4 receptor (Mc4r) mRNA"* ([PMID: 20220015](https://pubmed.ncbi.nlm.nih.gov/20220015/)), and inducible inactivation *"caused increased food and water intake and decreased expression of PVN neuropeptides, especially oxytocin and vasopressin, with no change in energy expenditure"* ([PMID: 24773343](https://pubmed.ncbi.nlm.nih.gov/24773343/)). This explains the clinical mimicry and underscores why *NTRK2* must be distinguished molecularly from SIM1/6q16 disease.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **Brain**, specifically the **hypothalamus** — paraventricular nucleus (UBERON:0001930) and dorsomedial nucleus (UBERON:0002708). Broader CNS involvement underlies developmental delay.
- **Body systems:** **Nervous** (central regulation of appetite and neurodevelopment) and **endocrine/metabolic** (secondary — adipose tissue, pancreatic islets via hyperinsulinemia).
- **Secondary organ involvement:** Adipose tissue expansion (UBERON:0001013); metabolic sequelae in liver/pancreas (insulin resistance).
- **Tissue/cell level:** **Nervous tissue**; **TrkB-expressing hypothalamic neurons** (CL:0000540 neuron). Peripheral adipose BDNF/TrkB axis also modulates feeding, especially in females ([PMID: 28721258](https://pubmed.ncbi.nlm.nih.gov/28721258/)).
- **Subcellular level (GO Cellular Component):** plasma membrane receptor (GO:0005886), **receptor complex** (GO:0043235), postsynaptic membrane (GO:0045211), cytoplasmic kinase signaling.
- **Localization / lateralization:** Bilateral, symmetric CNS involvement (not lateralized).

UBERON suggestions: UBERON:0000955 (brain), UBERON:0001898 (hypothalamus), UBERON:0001930 (paraventricular nucleus), UBERON:0002708 (dorsomedial hypothalamic nucleus).

---

## 8. Temporal Development

- **Onset:** **Infantile/early childhood** (HP:0003593 infantile onset). Obesity and hyperphagia emerge in early life; developmental delay is apparent in infancy (hypotonia, delayed milestones).
- **Onset pattern:** Insidious/chronic.
- **Progression:** Obesity is **progressive** if hyperphagia is unmanaged; developmental delay/ID is **static (non-progressive)**. Seizures, when present, are variable.
- **Disease course:** **Chronic, lifelong.** No spontaneous remission of the genetic defect; weight can be modulated by intensive management.
- **Critical periods:** Early childhood is the key window for feeding-behavior intervention and developmental/early-intervention therapies; hyperphagia precedes measurable weight gain (mouse data; [PMID: 26629410](https://pubmed.ncbi.nlm.nih.gov/26629410/)), supporting early vigilance.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant** (HP:0000006), typically **de novo** heterozygous ([PMID: 15494731](https://pubmed.ncbi.nlm.nih.gov/15494731/); [PMID: 39540377](https://pubmed.ncbi.nlm.nih.gov/39540377/)).
- **Penetrance:** High for the dominant LoF variants reported; precise penetrance estimates are limited by rarity. (Contrast: SIM1 haploinsufficiency shows *incomplete* penetrance — *"only 8 of 13 patients with SIM1 deletion exhibited obesity, in agreement with incomplete penetrance of SIM1 haploinsufficiency"*; [PMID: 25351778](https://pubmed.ncbi.nlm.nih.gov/25351778/).)
- **Expressivity:** Variable (severity of obesity, DD, seizures differs across individuals).
- **Genetic anticipation / mosaicism / founder effects:** Not applicable / not reported (no repeat expansion; ultra-rare de novo variants preclude founder effects).
- **Consanguinity / carrier frequency:** Not relevant for a dominant de novo disorder; carrier frequency effectively zero in gnomAD (pLI = 1.00).
- **Epidemiology:** **Ultra-rare.** Exact prevalence/incidence undefined; only a small number of probands worldwide (one index case plus the LoF subset of a 44-individual *NTRK2* cohort). Orphanet classifies it among rare syndromic obesities.
- **Population demographics:** No ethnic/geographic predilection; de novo origin implies sporadic global occurrence. Sex ratio not established (mouse models suggest females may show a more robust metabolic phenotype — [PMID: 26629410](https://pubmed.ncbi.nlm.nih.gov/26629410/), [PMID: 28721258](https://pubmed.ncbi.nlm.nih.gov/28721258/) — but this is not confirmed in humans).

---

## 10. Diagnostics

**Clinical/laboratory tests.** No specific diagnostic biomarker. Supportive findings: elevated fasting insulin, glucose, and leptin (secondary to obesity). Standard obesity work-up (lipids, HbA1c, thyroid, cortisol) to exclude other causes.

**Genetic testing (definitive).**
- **Recommended approach:** Molecular confirmation of a pathogenic *NTRK2* variant. In a child with **severe early-onset obesity + hyperphagia + developmental delay**, phenotype-driven genetic testing is indicated ([PMID: 42761221](https://pubmed.ncbi.nlm.nih.gov/42761221/)).
- **NGS obesity gene panels** (leptin–melanocortin pathway panels including *NTRK2*, *BDNF*, *MC4R*, *POMC*, *LEPR*, *SIM1*, etc.). The Greek cohort used a 101-gene monogenic-obesity panel ([PMID: 42761221](https://pubmed.ncbi.nlm.nih.gov/42761221/)).
- **Whole-exome (WES)/whole-genome (WGS) sequencing:** high utility for detecting de novo point variants and resolving syndromic presentations.
- **Chromosomal microarray (CMA):** to detect 9q21 deletions involving *NTRK2* and to exclude 6q16 (SIM1) and 15q11-q13 (Prader–Willi) in the differential.
- **Variant interpretation:** ACMG/AMP criteria; many obesity-panel variants are VUS and must be interpreted cautiously ([PMID: 42761221](https://pubmed.ncbi.nlm.nih.gov/42761221/)).

**Imaging.** Brain MRI may show delayed myelination (rare); not diagnostic.

**Clinical criteria & differential diagnosis.** Diagnosis rests on the clinical triad plus molecular confirmation. **Differential diagnosis** includes:
- Prader–Willi syndrome (15q11-q13) and **Prader–Willi-like / SIM1 6q16 deletion** (clinically very similar; distinguished by CMA/molecular testing).
- *MC4R*, *POMC*, *LEPR*, *BDNF* monogenic obesity (leptin–melanocortin pathway).
- *ARNT2*-related syndrome (SIM1 heterodimer partner; [PMID: 34214899](https://pubmed.ncbi.nlm.nih.gov/34214899/)).
- *MRAP2* deficiency.
- Acquired/hypothalamic obesity and ROHHAD.

**Screening.** Cascade testing of at-risk relatives if an inherited (non-de novo) variant is found; prenatal/preimplantation testing possible for known familial variants.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No direct disease-specific mortality data; prognosis is driven by **obesity-related morbidity** (type 2 diabetes, cardiovascular disease, metabolic dysfunction-associated steatotic liver disease) and complications of developmental disability. Life expectancy may be reduced by severe obesity complications if uncontrolled.
- **Morbidity/function:** Substantial lifelong disability from **intellectual disability/developmental delay** and from **refractory hyperphagic obesity**. Quality of life is heavily impacted by insatiable hunger (analogous MC4R-pathway diseases; [PMID: 42821228](https://pubmed.ncbi.nlm.nih.gov/42821228/)).
- **Complications:** Insulin resistance/type 2 diabetes, dyslipidemia, hepatic steatosis, orthopedic and sleep complications of obesity; seizures in a minority; behavioral/psychiatric challenges.
- **Prognostic factors:** Severity of hyperphagia, success of weight management, degree of cognitive impairment, and presence of epilepsy. Developmental delay is static but limits adaptive outcomes.
- **Recovery potential:** The genetic defect is not reversible; weight and metabolic parameters are partially modifiable with intensive management.

---

## 12. Treatment

**General principle — multidisciplinary, supportive.** Management combines **structured dietary/behavioral control of hyperphagia**, **physical activity**, **developmental/early-intervention therapies** (speech, occupational, physical therapy), **anti-seizure medication** where indicated, and management of metabolic complications.

**Pharmacotherapy / mechanism-based therapy — an important caveat.** The MC4R agonist **setmelanotide** (NCIT: Setmelanotide) acts **at MC4R**. Because the *NTRK2*/TrkB lesion lies **downstream of MC4R**, setmelanotide's efficacy in NTRK2-OBHD is **mechanistically uncertain** and unproven. Setmelanotide is effective where downstream MC4R signaling is intact (e.g., POMC/LEPR deficiency, acquired hypothalamic obesity reconceptualized as "α-MSH deficiency"; [PMID: 42114845](https://pubmed.ncbi.nlm.nih.gov/42114845/), [PMID: 42878773](https://pubmed.ncbi.nlm.nih.gov/42878773/), [PMID: 42496807](https://pubmed.ncbi.nlm.nih.gov/42496807/)). In TrkB loss of function, the deficit is at/after the TrkB node, so melanocortin agonism may not restore the missing satiety signal. This should be regarded as experimental for this indication.

**Advanced/experimental therapeutics.** No approved gene therapy, cell therapy, or RNA therapy. A TrkB **agonist** strategy is mechanistically rational for *loss-of-function* variants but unproven clinically; it would be contraindicated for the *gain-of-function* allelic group. No NCT trials specific to NTRK2-OBHD identified.

**Surgical/interventional.** Bariatric/metabolic surgery is considered in hypothalamic/refractory obesity but with heterogeneous response; evidence is limited and individualized ([PMID: 42496807](https://pubmed.ncbi.nlm.nih.gov/42496807/)).

**Supportive & rehabilitative.** Nutritional counseling and tightly structured food environment; developmental and behavioral therapies; management of comorbidities (diabetes, dyslipidemia, sleep apnea).

**Personalized medicine.** Genotype-guided: distinguishing LoF vs GoF *NTRK2* variants is essential because they define opposite disorders with opposite therapeutic logic (TrkB agonism vs. seizure/antagonist management).

NCIT suggestions: Setmelanotide (melanocortin receptor agonist), Behavioral/Dietary Weight Management, Rehabilitation Therapy, Anticonvulsant/Antiepileptic Therapy.

---

## 13. Prevention

- **Primary prevention:** Not possible for a de novo genetic disorder. Genetic counseling for families with an identified variant.
- **Secondary prevention:** Early molecular diagnosis enables **early feeding-behavior management** and metabolic monitoring to limit obesity severity and complications; early developmental intervention optimizes neurodevelopmental outcomes.
- **Tertiary prevention:** Aggressive management of obesity complications (diabetes, cardiovascular, hepatic, sleep), seizure control, and behavioral support.
- **Genetic counseling:** Recurrence risk is low for de novo variants (but germline mosaicism cannot be excluded); prenatal/PGT available for known familial variants.
- **Screening:** Consider *NTRK2* within monogenic-obesity panels for children with severe early-onset obesity, hyperphagia, and neurodevelopmental delay ([PMID: 42761221](https://pubmed.ncbi.nlm.nih.gov/42761221/)).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *Ntrk2* is highly conserved. Mouse *Ntrk2* (*Mus musculus*, NCBI Taxon 10090) and rat ortholog are the principal experimental orthologs; BDNF/TrkB function in energy balance is **evolutionarily conserved** across mammals ([PMID: 38672441](https://pubmed.ncbi.nlm.nih.gov/38672441/)).
- **Natural disease in other species:** No well-characterized spontaneous *NTRK2*-obesity syndrome reported in companion animals (OMIA search did not yield an established natural ortholog disease).
- **Comparative biology:** Mouse models faithfully reproduce the hyperphagia-driven obesity and confirm the hypothalamic BDNF/TrkB circuit, supporting strong cross-species conservation of the mechanism.
- **Transmission/zoonosis:** Not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

**Mouse (*Mus musculus*) is the primary model.**

| Model | Manipulation | Key phenotype | PMID |
|---|---|---|---|
| PVH-specific *Ntrk2* deletion | Conditional KO | Severe hyperphagic obesity; chemogenetic TrkB-PVH neurons bidirectionally control feeding | [32265438](https://pubmed.ncbi.nlm.nih.gov/32265438/) |
| DMH TrkB neuron manipulation | Circuit genetics | TrkB-DMH neurons necessary & sufficient to suppress homeostatic feeding | [30718415](https://pubmed.ncbi.nlm.nih.gov/30718415/) |
| *Nkx2.1-Ntrk2⁻/⁻* (hypothalamic) | Conditional KO | Increased body weight/adiposity; hyperphagia precedes weight gain; hyperglycemia, hyperinsulinemia, hyperleptinemia | [26629410](https://pubmed.ncbi.nlm.nih.gov/26629410/) |
| Adipocyte/neuron-specific BDNF/TrkB CKO | Conditional KO | Feeding/obesity effects, sex-dependent (female-predominant adipose axis) | [28721258](https://pubmed.ncbi.nlm.nih.gov/28721258/) |
| *Sim1⁺/⁻* / conditional *Sim1* (shared circuit) | KO | Hyperphagic obesity; ~80% reduced oxytocin; reduced PVN *Mc4r*/*Oxt*; oxytocin rescues feeding | [18451093](https://pubmed.ncbi.nlm.nih.gov/18451093/), [20220015](https://pubmed.ncbi.nlm.nih.gov/20220015/), [24773343](https://pubmed.ncbi.nlm.nih.gov/24773343/) |
| Patient iPSC line (CUIMCi003-A) | ARNT2 variant (SIM1 partner) | iPSC resource for modeling PVH neurodevelopment | [34214899](https://pubmed.ncbi.nlm.nih.gov/34214899/) |

**Phenotype recapitulation.** Mouse TrkB/Ntrk2 models reproduce the **hyperphagia and obesity** core and localize the effect to hypothalamic PVH/DMH — excellent recapitulation of the metabolic phenotype. **Limitations:** rodent models less fully capture the human **cognitive/developmental delay, memory, language, and nociception** phenotypes; sex-dependence in mice is not clearly mirrored in humans. **Resources:** MGI (*Ntrk2*), IMPC/KOMP for knockout alleles; patient-derived iPSCs for human neuronal modeling.

---

## Mechanistic Model (synthesis)

```
   LEPTIN  ──►  POMC neurons  ──►  α-MSH  ──►  MC4R (PVH)        [upstream, intact]
                                                 │
                                                 ▼
                              BDNF ──► TrkB (NTRK2) in PVH/DMH   ◄── LESION (LoF variant)
                                                 │                      (Y722C: no autophosphorylation;
                                                 │                       truncating → haploinsufficiency)
                              (MAPK/ERK, PI3K-AKT, PLCγ signaling)
                                                 │
                        ┌────────────────────────┴──────────────────────────┐
                        ▼ (metabolic branch)                                 ▼ (neurodevelopmental branch)
          Loss of anorexigenic "satiety brake"                 Loss of neurotrophic support
                        │                                      (survival, differentiation, plasticity)
                        ▼                                                     ▼
            HYPERPHAGIA (precedes weight gain)         Global developmental delay / ID,
                        │                               impaired memory & language,
            No ↑ energy expenditure                     hypotonia, blunted nociception,
                        ▼                               behavioral abnormalities, ± seizures
      SEVERE EARLY-ONSET OBESITY
      (2° hyperinsulinemia, hyperglycemia, hyperleptinemia)
```

**Key point for therapy:** the TrkB defect is **downstream of MC4R**, so MC4R agonists (setmelanotide) may not rescue satiety — unlike in POMC/LEPR deficiency or acquired hypothalamic obesity, where MC4R signaling is intact.

### SIM1 vs NTRK2 — same circuit, distinct genes

| Feature | *NTRK2*/TrkB (MONDO:0013483, this disease) | *SIM1* / 6q16 deletion (Prader–Willi-like, differential) |
|---|---|---|
| Gene / locus | *NTRK2*, 9q21.33 | *SIM1*, 6q16.3 (often contiguous deletion) |
| Molecular role | BDNF receptor; satiety signal downstream of MC4R | bHLH-PAS TF; builds PVH, sustains MC4R/oxytocin |
| Inheritance | AD, de novo; high penetrance | Haploinsufficiency; **incomplete penetrance** (8/13 obese) |
| Core triad | Obesity, hyperphagia, DD | Obesity, hyperphagia, DD, hypotonia (PWS-like) |
| Energy expenditure | Unchanged (hyperphagia-driven) | Unchanged (hyperphagia-driven) |
| Distinguishing test | NGS/CMA at 9q21 | CMA detects 6q16 deletion; oxytocin ↓80% in mice |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [15494731](https://pubmed.ncbi.nlm.nih.gov/15494731/) | *De novo TrkB mutation in severe obesity & developmental delay* | **Index case**; defines NTRK2/TrkB causation; Y722C impairs autophosphorylation/MAPK |
| [39540377](https://pubmed.ncbi.nlm.nih.gov/39540377/) | *Upregulation vs loss of NTRK2 in 44 individuals → 2 disorders* | **Allelic series**; LoF→obesity/hyperphagia/DD vs GoF→epilepsy/blindness |
| [32265438](https://pubmed.ncbi.nlm.nih.gov/32265438/) | *TrkB PVH neurons suppress appetite* | Localizes satiety action to PVH; circuit mechanism |
| [30718415](https://pubmed.ncbi.nlm.nih.gov/30718415/) | *TrkB DMH neurons suppress feeding* | DMH TrkB necessary & sufficient for satiety |
| [26629410](https://pubmed.ncbi.nlm.nih.gov/26629410/) | *Hypothalamic TrkB ablation & energy balance* | Hyperphagia precedes weight gain; metabolic sequelae |
| [18753648](https://pubmed.ncbi.nlm.nih.gov/18753648/) | *BDNF & obesity in WAGR* | Human ligand-side evidence (BDNF haploinsufficiency → ↑BMI) |
| [38672441](https://pubmed.ncbi.nlm.nih.gov/38672441/) | *BDNF/TrkB in energy & glucose balance (review)* | Conserved circuitry; mechanistic synthesis |
| [28721258](https://pubmed.ncbi.nlm.nih.gov/28721258/) | *CNS & adipose BDNF/TrkB axes* | Peripheral axis; sex-dependence |
| [18451093](https://pubmed.ncbi.nlm.nih.gov/18451093/) | *Oxytocin deficiency in Sim1 mice* | Shared-circuit (SIM1) mechanism |
| [20220015](https://pubmed.ncbi.nlm.nih.gov/20220015/) | *Postnatal Sim1 deficiency* | SIM1→↓Mc4r/Oxt; differential context |
| [24773343](https://pubmed.ncbi.nlm.nih.gov/24773343/) | *Inducible Sim1 inactivation* | SIM1 ongoing role; no ΔEE |
| [25351778](https://pubmed.ncbi.nlm.nih.gov/25351778/) | *Incomplete penetrance of 6q16/SIM1* | Differential; penetrance contrast |
| [23778136](https://pubmed.ncbi.nlm.nih.gov/23778136/) | *LoF SIM1 mutations & obesity/PWL* | Differential; SIM1 LOF severity |
| [42761221](https://pubmed.ncbi.nlm.nih.gov/42761221/) | *Leptin-melanocortin variants in Greek cohort* | Diagnostic approach; panel testing; VUS caution |
| [42114845](https://pubmed.ncbi.nlm.nih.gov/42114845/) | *MC4R agonist in ROHHAD* | Setmelanotide context (MC4R-intact disease) |
| [42878773](https://pubmed.ncbi.nlm.nih.gov/42878773/) | *Acquired HO as α-MSH deficiency* | Why MC4R agonism works when signaling is intact |
| [42496807](https://pubmed.ncbi.nlm.nih.gov/42496807/) | *Hypothalamic obesity interventions (review)* | Treatment landscape |
| [42821228](https://pubmed.ncbi.nlm.nih.gov/42821228/) | *Hunger severity in MC4R-pathway diseases* | QoL/hyperphagia burden |
| [34214899](https://pubmed.ncbi.nlm.nih.gov/34214899/) | *iPSC line, ARNT2 variant* | Model resource; SIM1 partner |
| [34571524](https://pubmed.ncbi.nlm.nih.gov/34571524/) | *CMT2Q with NTRK2 variant* | Phenotypic breadth; NTRK2-obesity link noted |

---

## Limitations and Knowledge Gaps

1. **Rarity limits epidemiology.** Prevalence, incidence, sex ratio, and penetrance for *NTRK2*-OBHD are not quantitatively established; the HPO frequencies are anchored largely to the index proband.
2. **Mid-course gene correction.** Early iterations pursued *SIM1*/6q16; the authoritative MONDO definition anchors MONDO:0013483 to *NTRK2*. SIM1 material is retained as shared-circuit/differential context, not as the cause of this entity. Readers should not conflate the two.
3. **Human neurodevelopmental mechanism is partly inferred.** The feeding mechanism is strongly demonstrated in mice; the cognitive/memory/nociception phenotypes are inferred from TrkB's general neurobiology and single-patient observations rather than mechanistic human studies.
4. **Therapeutics unproven.** No controlled trials in *NTRK2*-OBHD. The downstream-of-MC4R position makes setmelanotide's benefit uncertain; TrkB-agonist therapy is conceptual.
5. **Variant interpretation.** Many obesity-panel variants are VUS; functional validation (as done for Y722C) is needed to classify novel *NTRK2* variants and to assign them to the LoF vs GoF axis.
6. **Signaling branches partly inferred.** MAPK defect is demonstrated; PI3K-AKT and PLCγ contributions are inferred from canonical TrkB biology.

---

## Proposed Follow-up Experiments / Actions

1. **Functional variant classification pipeline.** Systematically assay novel *NTRK2* variants (autophosphorylation, MAPK/ERK, PI3K-AKT, PLCγ readouts) to assign LoF vs GoF — critical because the two define opposite disorders and opposite therapeutic logic.
2. **Patient-derived iPSC hypothalamic organoids/neurons.** Model TrkB LoF in human PVH/DMH-like neurons to test satiety-signaling defects and candidate TrkB-agonist rescue in a human system.
3. **Natural-history registry.** Aggregate *NTRK2*-OBHD cases (via GeneMatcher/Orphanet) to define penetrance, sex ratio, progression, seizure frequency, and long-term outcomes.
4. **Therapeutic test of downstream vs upstream logic.** Preclinically compare MC4R agonism (setmelanotide) vs small-molecule TrkB agonists in hypothalamic *Ntrk2*-LoF models to determine whether rescuing *below* the lesion is required.
5. **Deep phenotyping of cognition/nociception.** Standardized neurocognitive and sensory testing across the LoF cohort to characterize the neurodevelopmental branch quantitatively.
6. **Biomarker discovery.** Explore circulating BDNF, leptin, and insulin trajectories as potential monitoring biomarkers in affected children.

---

*Evidence source types are indicated throughout: **human clinical** (index case, cohorts, WAGR), **model organism** (mouse Ntrk2/Sim1 genetics), **in vitro** (luciferase/autophosphorylation assays), and **computational** (gnomAD constraint, ClinVar burden). Ontology suggestions (HPO, GO, CL, UBERON, NCIT, MONDO) are embedded in the relevant sections.*


## Artifacts

- [OpenScientist final report](Obesity_Hyperphagia_And_Developmental_Delay-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Obesity_Hyperphagia_And_Developmental_Delay-deep-research-openscientist_artifacts/final_report.pdf)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 29 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013483` (9 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **obesity, hyperphagia, and developmental delay**
- `HP:0001328` (1 mention) - the report calls it "Impaired learning"; HP calls it **Specific learning disability**
- `UBERON:0001013` (1 mention) - the report calls it "Secondary organ involvement:** Adipose tissue expansion"; UBERON calls it **adipose tissue**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0009074` (1 mention), reported as "Impaired short-term memory" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002591` (1 mention) - the report calls it "Hyperphagia / polyphagia"; HP calls it **Polyphagia**, and lists "Hyperphagia" among its other names
- `HP:0001250` (1 mention) - the report calls it "Seizure (general)"; HP calls it **Seizure**
- `GO:0042755` (1 mention) - the report calls it "regulation of eating behavior"; GO calls it **eating behavior**
- `UBERON:0001930` (2 mentions) - the report calls it "paraventricular nucleus"; UBERON calls it **paraventricular nucleus of hypothalamus**, and lists "paraventricular nucleus" among its other names
- `UBERON:0002708` (2 mentions) - the report calls it "dorsomedial hypothalamic nucleus"; UBERON calls it **posterior periventricular nucleus**, and lists "posterior periventricular hypothalamic nucleus" among its other names
- `GO:0043235` (1 mention) - the report calls it "receptor complex"; GO calls it **signaling receptor complex**, and lists "receptor complex" among its other names
- `HP:0000006` (1 mention) - the report calls it "Autosomal dominant", "Inheritance:** **Autosomal dominant"; HP calls it **Autosomal dominant inheritance**, and lists "Autosomal dominant" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0013483` - called "if available", "MONDO"
- `HP:0000006` - called "Autosomal dominant", "Inheritance:** **Autosomal dominant"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Orphanet`, `UMLS`, `ORPHA`.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.
