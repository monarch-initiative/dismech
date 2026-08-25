---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T08:41:21.164570'
end_time: '2026-08-19T08:58:15.880456'
duration_seconds: 1014.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: DLG4-Related Synaptopathy
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
citation_count: 13
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 8
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: DLG4-Related_Synaptopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: DLG4-Related_Synaptopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DLG4-Related Synaptopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DLG4-Related Synaptopathy** covering all of the
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

# DLG4-Related Synaptopathy (SHINE Syndrome): A Comprehensive Disease Characterization

## Summary

**DLG4-related synaptopathy** (also called **SHINE syndrome**) is a rare, autosomal-dominant neurodevelopmental disorder caused by heterozygous, almost always *de novo*, predominantly loss-of-function variants in **DLG4**, the gene encoding the excitatory postsynaptic scaffold protein **PSD-95** (postsynaptic density protein 95). The disorder was formally defined and named in a landmark 2021 cohort of 53 patients (42 previously unpublished) carrying 45 different DLG4 variants, of which 39 were predicted to lead to loss of protein function [PMID: 33597769]. Its key identifiers are OMIM 618793 (Intellectual developmental disorder, autosomal dominant 62 / IDD62), MONDO:0032919, MedGen/UMLS C5394083, DOID:0061035, and GARD 0025775. The acronym SHINE captures its cardinal features: **S**leep disturbances, **H**ypotonia, **I**ntellectual disability/impairment, **N**eurological disorders, and **E**pilepsy.

Mechanistically, PSD-95 is a membrane-associated guanylate kinase (MAGUK) scaffold that stabilizes and traffics NMDA- and AMPA-type glutamate receptors at the postsynaptic density of excitatory synapses, governing synaptic maturation and plasticity. Loss of one functional DLG4 allele produces PSD-95 haploinsufficiency, disorganizing the glutamatergic postsynaptic density and impairing synaptic maturation and plasticity. The gene is among the most loss-of-function-intolerant genes in the human genome (gnomAD pLI = 1.0; LOEUF = 0.14), providing strong population-genetic support for a haploinsufficiency mechanism. The resulting clinical picture is dominated by early-onset global developmental delay, intellectual disability, autism spectrum disorder (ASD), and attention-deficit/hyperactivity disorder (ADHD), accompanied by hypotonia, sleep disturbance, movement disorders, and epilepsy (present in ~50%, with a distinctive regression-associated ESES/DEE-SWAS subtype in >25% of those with epilepsy).

Diagnosis is molecular, established by clinical whole-exome or whole-genome sequencing; splice-site and deep-intronic variants may require RNA/functional confirmation. There is currently **no disease-modifying therapy**; management is entirely supportive and symptom-directed, including antiseizure medications for epilepsy, developmental and rehabilitative therapies, sleep and behavioral management, and — in at least one reported adolescent case — clozapine for treatment-resistant psychosis. This report integrates 10 confirmed findings and 19 reviewed papers to provide a full disease-knowledge-base characterization across all 15 requested sections.

---

## Key Findings

### Finding 1 — Definition and core identity of the disorder

DLG4-related synaptopathy is a rare autosomal-dominant neurodevelopmental disorder caused by *de novo* variants in DLG4/PSD-95. It was defined by the landmark cohort of Rodríguez-Palmero and colleagues, who reported *"the clinical and genetic features of 53 patients (42 previously unpublished) with DLG4 variants"* and proposed *"we designate this group of disorders as DLG4-related synaptopathy"* [PMID: 33597769]. Of the 45 different DLG4 variants they identified, *"39 were predicted to lead to loss of protein function and the majority occurred de novo"* [PMID: 33597769].

The disorder maps to the following identifiers: **OMIM 618793** (Intellectual developmental disorder, autosomal dominant 62 / IDD62), **MONDO:0032919**, **MedGen/UMLS C5394083**, **DOID:0061035**, and **GARD 0025775**. The causal gene **DLG4** is HGNC:2903, NCBI Gene 1742, UniProt **P78352**, located at chromosome **17p13.1**, and encodes PSD-95.

### Finding 2 — Core clinical phenotype

The predominant clinical features are early-onset global developmental delay, intellectual disability, ASD, and ADHD. The original cohort found that *"the clinical picture was predominated by early onset global developmental delay, intellectual disability, autism spectrum disorder, and attention deficit-hyperactivity disorder, all of which point to a brain disorder"* [PMID: 33597769]. Additional features include hypotonia, sleep disturbance, movement disorders, strabismus, scoliosis, and joint hypermobility. Notably, the study refined an earlier claim: *"Marfanoid habitus, which was previously suggested to be a characteristic feature of DLG4-related phenotypes, was found in only nine individuals"* (9/53), and there was no distinct facial dysmorphism.

Epilepsy is a major feature. A dedicated epilepsy study noted that *"even though epilepsy is present in 50% of the individuals, it has not been investigated in detail"* and reported that *"encephalopathy related to status epilepticus during slow-wave sleep (ESES)/developmental epileptic encephalopathy with spike-wave activation during sleep (DEE-SWAS) was diagnosed in >25% of the individuals"* [PMID: 38135915]. Focal seizures were the most common type.

**Suggested HPO terms:** Intellectual disability (HP:0001249), Seizure (HP:0001250), Autistic behavior (HP:0000729), Attention deficit hyperactivity disorder (HP:0007018), Muscular hypotonia (HP:0001252), Sleep disturbance (HP:0002360), Strabismus (HP:0000486), Scoliosis (HP:0002650), Joint hypermobility (HP:0001382), Global developmental delay (HP:0001263), Cerebellar vermis atrophy (HP:0006855).

### Finding 3 — Molecular mechanism (PSD-95 scaffolding of glutamate receptors)

PSD-95 scaffolds NMDA and AMPA receptors at the excitatory postsynaptic density; its loss impairs synaptic maturation and plasticity. As summarized in a review, *"postsynaptic density protein-95 (PSD-95) is a major regulator of synaptic maturation by interacting, stabilizing and trafficking N-methyl-d-aspartic acid receptors (NMDARs) and α-amino-3-hydroxy-5-methyl-4-isoxazoleproprionic acid receptors (AMPARs) to the postsynaptic membrane"* [PMID: 29169997]. The original disease paper states that *"postsynaptic density protein-95 (PSD-95), encoded by DLG4, regulates excitatory synaptic function in the brain"* [PMID: 33597769].

At the molecular level, protein-truncating variants and at least one deep-intronic variant act by reducing functional protein. A patient-derived DLG4 V692Wfs*12 transcript illustrates the mechanism: *"the mutant transcript escapes nonsense-mediated decay but results in reduced PSD-95 protein expression"* [PMID: 42565830], demonstrating that even a transcript that evades NMD ultimately yields reduced PSD-95 protein — consistent with haploinsufficiency.

**Suggested GO/CL terms:** postsynaptic density (GO:0014069), dendritic spine (GO:0043197), glutamatergic synapse (GO:0098978), regulation of synaptic plasticity (GO:0048167); glutamatergic neuron (CL:0000679).

### Finding 4 — Extreme loss-of-function intolerance supports haploinsufficiency

DLG4 is among the most constrained genes in the human genome. gnomAD constraint metrics for DLG4 (ENSG00000132535, chr17:7,187,187–7,219,841, GRCh38) show **pLI = 1.0**; observed LoF variants = 7 versus expected 93.8 (**oe_lof = 0.075**, 90% CI 0.042–0.140, i.e. **LOEUF = 0.14**); LoF Z = 7.60; missense Z = 6.06 (oe_mis = 0.55). This extreme depletion of loss-of-function variation in the general population is exactly the population-genetic signature expected for a haploinsufficient, dominant neurodevelopmental gene, and it strongly corroborates the mechanistic model that a single loss-of-function allele is sufficient to cause disease.

### Finding 5 — Model organisms recapitulate cognitive, behavioral, and synaptic-plasticity deficits

Multiple mouse models and patient-derived cellular models support the disease mechanism:

- **PSD-95-null mice** show paradoxically enhanced hippocampal LTP with severely impaired learning: *"in mutant mice lacking PSD-95, the frequency function of NMDA-dependent LTP and LTD is shifted to produce strikingly enhanced LTP at different frequencies of synaptic stimulation"* and *"this frequency shift is accompanied by severely impaired spatial learning"* [PMID: 9853749].
- **PDZ1/2 ligand-binding-deficient PSD-95 knock-in mice** show reduced PSD accumulation of PSD-95/PSD-93/AMPARs, abnormal anxiety, and impaired spatial, working, and remote memory [PMID: 23268962].
- **Dlg4−/− mice** model ASD-relevant behavior: they *"showed increased repetitive behaviors, abnormal communication and social behaviors, impaired motor coordination, and increased stress reactivity and anxiety-related responses"* [PMID: 20952458].
- A **patient-derived Dlg4 V692Wfs*12/+ knock-in mouse** faithfully models the human disorder: *"Dlg4V692Wfs*12/+ mice recapitulate several hallmark features of SHINE syndrome, often in a sex-specific manner"* — including reduced PSD-95, learning/cognitive-flexibility deficits (male-biased), and sleep abnormalities [PMID: 42565830].
- A **patient iPSC line** (AOUMEYi004-A) carrying c.2155A>T p.(Arg719*) was established for in vitro disease modeling [PMID: 42462545].

### Finding 6 — Management is supportive; no disease-modifying therapy

There is no targeted or curative therapy. Care is symptom-directed: antiseizure medications for epilepsy, developmental/rehabilitative therapies, and management of sleep and behavior. Antiseizure medication response was assessed retrospectively across 35 patients with epilepsy, with variable response and frequent refractoriness in the ESES/DEE-SWAS forms [PMID: 38135915]. For treatment-resistant psychosis, an adolescent with SHINE syndrome and early-onset schizophrenia/catatonia improved markedly on clozapine: *"after failing three antipsychotic drug treatments, the patient was started on clozapine, which resulted in significant improvements in positive and negative symptoms"* [PMID: 37386468]. Experimental PSD-95-directed agents (e.g., nerinetide/Tat-NR2B9c, which disrupt the PSD-95/nNOS interaction) exist but are being developed for stroke and pain, **not** for this disorder [PMID: 40712457].

### Finding 7 — Protein architecture and variant spectrum

PSD-95 (UniProt P78352, 724 aa) is a MAGUK with a characteristic modular architecture: three PDZ domains (PDZ1 aa 65–151, PDZ2 aa 160–246, PDZ3 aa 313–393), an SH3 domain (aa 428–498), and a guanylate kinase-like (GK) domain (aa 534–709), plus an N-terminal disordered region (aa 15–35). Twenty-two experimental PDB structures have been deposited. Pathogenic variants span the entire gene and include nonsense/frameshift (e.g., c.2155A>T p.Arg719*; c.2074_2075 frameshift p.Val692Trpfs*12 in the GK domain), splice-site, a deep-intronic pseudoexon variant (c.2105+235C>T), and six missense variants. *"The six missense variants identified were suggested to lead to structural or functional changes by protein modeling studies"* [PMID: 33597769], and across cohorts *"the majority [are] predicted to be protein-truncating"* [PMID: 37525972].

### Finding 8 — Diagnosis, inheritance, and epidemiology

Diagnosis is molecular, established by clinical whole-exome or whole-genome sequencing identifying a heterozygous DLG4 variant; RNA/functional studies resolve splice and deep-intronic variants. In the landmark cohort, most cases were simplex/*de novo*: *"the majority occurred de novo (four with unknown origin)"* [PMID: 33597769]. A deep-intronic variant was *"identified using whole genome sequencing"* [PMID: 37525972], underscoring the value of WGS plus RNA studies when exome sequencing is unrevealing. Brain MRI and EEG (including sleep EEG/video-polygraphy for ESES/DEE-SWAS) are used for phenotyping: *"data on awake and sleep electroencephalography (EEG) and/or video-polygraphy and brain magnetic resonance imaging were collected"* [PMID: 38135915]. The disorder is ultra-rare (~53 patients in the defining 2021 series, with additional case reports since); no population prevalence or incidence has been established, and it is under-ascertained, including late/adolescent diagnoses [PMID: 40444229].

### Finding 9 — Anatomy and temporal course

This is a brain-centered disorder affecting glutamatergic excitatory synapses. PSD-95 is *"an essential scaffolding protein during synaptogenesis and neurodevelopment"* [PMID: 29169997], localizing to the postsynaptic density of excitatory synapses. Primary organ: brain/nervous system; cell type: glutamatergic neurons (CL:0000679); subcellular compartment: postsynaptic density/dendritic spine (GO:0014069, GO:0043197). Some patients show cerebellar vermis atrophy on MRI (HP:0006855, ~33% in the original small series). Onset is early (infancy/early childhood) with global developmental delay; the course is chronic and lifelong and generally non-degenerative, but developmental/verbal-motor regression can occur in those who develop status epilepticus in sleep: *"regression in verbal and/or motor domains was observed in all individuals who su[ffered status epilepticus]"* [PMID: 38135915].

### Finding 10 — Purely genetic etiology; high evolutionary conservation

DLG4-related synaptopathy is monogenic with no established environmental, infectious, lifestyle, or gene-environment contribution; *de novo* germline DLG4 variants arise sporadically, consistent with *"the majority occurred de novo"* [PMID: 33597769]. No protective alleles or modifier genes have been identified. ClinVar (accessed 2026) lists ~445 DLG4 variant records: ~207 pathogenic, ~60 likely pathogenic, and ~316 of uncertain significance. DLG4/PSD-95 is deeply conserved: orthologs include mouse Dlg4 (NCBI Gene 13385, MGI:1277959), rat Dlg4 (NCBI Gene 29495), zebrafish dlg4a/dlg4b, Drosophila dlg1 (discs large), and C. elegans dlg-1; the MAGUK/PDZ–SH3–GK architecture is conserved from invertebrates to humans.

---

## Comprehensive Section-by-Section Report

### 1. Disease Information

**Overview.** DLG4-related synaptopathy (SHINE syndrome) is a rare autosomal-dominant neurodevelopmental "synaptopathy" — a disorder of synaptic structure and function — caused by heterozygous, predominantly *de novo* loss-of-function variants in DLG4 (PSD-95). It presents in infancy/early childhood with global developmental delay and evolves into a lifelong picture of intellectual disability, autism, ADHD, hypotonia, sleep disturbance, movement disorders, and (in ~50%) epilepsy [PMID: 33597769, 38135915].

**Key identifiers.** OMIM **618793** (IDD62); MONDO:**0032919**; MedGen/UMLS **C5394083**; DOID:**0061035**; GARD **0025775**. Gene: DLG4 (HGNC:2903, NCBI Gene 1742, UniProt P78352, 17p13.1). A specific ICD-10/ICD-11 code is not assigned to this ultra-rare entity; it is captured under intellectual disability / developmental disorder categories. MeSH indexing is via DLG4/PSD-95 and intellectual disability terms.

**Synonyms.** SHINE syndrome (Sleep disturbances, Hypotonia, Intellectual disability, Neurological disorders, Epilepsy); Intellectual developmental disorder, autosomal dominant 62 (IDD62); DLG4-related synaptopathy; PSD-95-related neurodevelopmental disorder.

**Information source.** The knowledge base derives from aggregated disease-level resources (OMIM, ClinVar, gnomAD) plus published patient cohorts and case reports — i.e., published individual-patient data aggregated into cohorts, not routine EHR mining.

### 2. Etiology

**Causal factors.** Purely genetic: heterozygous DLG4 variants, most arising *de novo* [PMID: 33597769]. No environmental, infectious, or lifestyle cause is established (Finding 10).

**Genetic risk factors.** The causal variant itself is the sole established risk factor. DLG4 is extremely LoF-intolerant (pLI = 1.0; LOEUF = 0.14), meaning even a single loss-of-function allele confers disease (Finding 4). No susceptibility loci or modifier genes have been established.

**Environmental risk factors / protective factors / gene-environment interactions.** None identified. No protective alleles are known. Because most cases are *de novo*, advanced parental age (a general contributor to *de novo* mutation rates) is a plausible but unproven population-level consideration; this is not disease-specific evidence.

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Frequency/Notes |
|---|---|---|---|---|
| Global developmental delay | Clinical sign | HP:0001263 | Infancy/early childhood | Predominant feature [PMID: 33597769] |
| Intellectual disability | Clinical sign | HP:0001249 | Childhood | Core, variable severity [PMID: 33597769] |
| Autism spectrum disorder | Behavioral | HP:0000729 | Childhood | Predominant [PMID: 33597769] |
| ADHD | Behavioral | HP:0007018 | Childhood | Predominant [PMID: 33597769] |
| Hypotonia | Clinical sign | HP:0001252 | Neonatal/infancy | Common ("H" in SHINE) |
| Sleep disturbance | Symptom | HP:0002360 | Childhood | Common ("S" in SHINE); modeled in mouse [PMID: 42565830] |
| Epilepsy/seizures | Clinical sign | HP:0001250 | Childhood | ~50%; focal most common [PMID: 38135915] |
| ESES/DEE-SWAS | Clinical sign | HP:0002133 | Childhood | >25% of epilepsy patients; regression-associated [PMID: 38135915] |
| Movement disorder | Clinical sign | HP:0100022 | Variable | Reported [PMID: 33597769] |
| Strabismus | Physical | HP:0000486 | Childhood | Reported |
| Scoliosis | Physical | HP:0002650 | Childhood | Reported |
| Joint hypermobility | Physical | HP:0001382 | Childhood | Reported |
| Marfanoid habitus | Physical | HP:0001519 | — | Only 9/53 — NOT characteristic [PMID: 33597769] |
| Cerebellar vermis atrophy | Imaging | HP:0006855 | — | ~33% in small series |

**Severity/progression.** Severity is variable; the disorder is chronic and lifelong and generally non-degenerative. However, verbal/motor **regression** occurs in individuals who develop status epilepticus in sleep (ESES/DEE-SWAS) [PMID: 38135915].

**Quality-of-life impact.** Substantial: intellectual disability, autism, epilepsy, and sleep disturbance collectively impair communication, learning, independence, and family functioning. No disease-specific EQ-5D/SF-36/PROMIS data are available.

### 4. Genetic/Molecular Information

**Causal gene.** DLG4 (HGNC:2903; NCBI Gene 1742; OMIM gene 602887; UniProt P78352; 17p13.1) encoding PSD-95.

**Pathogenic variants.** Variants span the gene and are predominantly protein-truncating (nonsense, frameshift, splice-site), with a minority of missense and at least one deep-intronic pseudoexon variant. Examples: c.2155A>T p.(Arg719*) [PMID: 42462545]; c.2074_2075 frameshift p.(Val692Trpfs*12) in the GK domain [PMID: 42565830]; c.2105+235C>T deep-intronic [PMID: 37525972]. Of 45 variants in the defining cohort, 39 were predicted loss-of-function, and the six missense variants were modeled to disrupt structure/function [PMID: 33597769].

**Variant classification (ClinVar, 2026).** ~445 DLG4 records: ~207 pathogenic, ~60 likely pathogenic, ~316 uncertain significance (Finding 10). Per ACMG/AMP, truncating variants in this LoF-intolerant gene generally meet PVS1.

**Allele frequency.** Pathogenic variants are absent/vanishingly rare in gnomAD, consistent with *de novo* origin and extreme constraint (pLI = 1.0, LOEUF = 0.14).

**Origin.** Germline, predominantly *de novo* [PMID: 33597769]. No somatic disease association.

**Functional consequence.** Loss of function / haploinsufficiency (reduced PSD-95 protein) [PMID: 42565830]; some missense variants may act via structural disruption.

**Modifier genes / epigenetics / chromosomal abnormalities.** None established. DLG4 sits at 17p13.1; larger 17p deletions encompassing DLG4 could plausibly contribute but are not a defined mechanism for this entity.

### 5. Environmental Information

Not applicable. This is a monogenic disorder with no established environmental factors, lifestyle factors, or infectious agents (Finding 10) [PMID: 33597769].

### 6. Mechanism / Pathophysiology

**Molecular pathway.** Glutamatergic synaptic signaling. PSD-95 is the central organizer of the excitatory postsynaptic density (PSD), where it clusters and traffics NMDARs and AMPARs and couples them to downstream signaling (e.g., nNOS, SynGAP, CaMKII) [PMID: 29169997, 20554866].

**Causal chain.**

```
DLG4 LoF variant (de novo, heterozygous)
        │
        ▼
Reduced functional PSD-95 protein (haploinsufficiency)
        │  (transcript may escape NMD but yields less protein — PMID 42565830)
        ▼
Disorganized excitatory postsynaptic density:
  ↓ clustering/trafficking of NMDARs & AMPARs (PMID 23268962)
        │
        ▼
Impaired synaptic maturation & aberrant plasticity
  (altered LTP/LTD; PMID 9853749, 23268962)
        │
        ▼
Disrupted neural circuit development (glutamatergic neurons)
        │
        ▼
Clinical manifestations: developmental delay, ID, ASD/ADHD,
hypotonia, sleep disturbance, epilepsy
```

**Upstream vs downstream.** Upstream: the DLG4 variant and reduced PSD-95. Downstream: receptor mis-clustering, altered synaptic plasticity, circuit dysfunction, and behavior.

**Cellular process.** Synaptogenesis, synaptic maturation, and plasticity in glutamatergic neurons. **Protein dysfunction:** loss of function of a scaffold (not aggregation). **Immune/metabolic involvement:** none established. **Biochemical:** receptor scaffolding defect at the PSD.

**Molecular profiling.** No disease-specific human transcriptomic/proteomic/metabolomic signatures are published; mechanistic evidence derives from mouse models and in vitro biochemistry [PMID: 9853749, 23268962, 20952458, 20554866]. Patient iPSC lines now enable such profiling [PMID: 42462545].

**Suggested GO terms:** GO:0014069 (postsynaptic density), GO:0098978 (glutamatergic synapse), GO:0048167 (regulation of synaptic plasticity), GO:0007416 (synapse assembly), GO:0035249 (synaptic transmission, glutamatergic). **CL:** CL:0000679 (glutamatergic neuron).

### 7. Anatomical Structures Affected

- **Organ level:** Brain / central nervous system (primary). Body system: nervous system. **UBERON:** brain (UBERON:0000955), cerebral cortex (UBERON:0000956), hippocampus (UBERON:0002421), cerebellar vermis (UBERON:0004720; atrophy in a subset, HP:0006855).
- **Tissue/cell level:** Nervous tissue; glutamatergic excitatory neurons (CL:0000679).
- **Subcellular level:** Postsynaptic density (GO:0014069), dendritic spine (GO:0043197), postsynaptic membrane (GO:0045211).
- **Lateralization:** Bilateral (diffuse CNS involvement).

### 8. Temporal Development

- **Onset:** Early — infancy/early childhood, with global developmental delay as the presenting feature; insidious/chronic onset.
- **Progression:** Chronic, lifelong, generally non-degenerative. Epilepsy (including ESES/DEE-SWAS) typically emerges in childhood. **Regression** in verbal/motor domains occurs specifically in those developing status epilepticus in sleep [PMID: 38135915].
- **Critical period:** The ESES/DEE-SWAS window in childhood represents a period of vulnerability (regression) and a potential opportunity for intervention (seizure control). Diagnosis may be delayed to adolescence/adulthood [PMID: 40444229, 42462545].

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant (OMIM 618793), predominantly *de novo*; *"the majority occurred de novo (four with unknown origin)"* [PMID: 33597769].
- **Penetrance/expressivity:** Presumed high penetrance for LoF variants; expressivity is variable (severity ranges; epilepsy in ~50%).
- **Anticipation/mosaicism/founder effects/consanguinity:** Not applicable/not reported (dominant, *de novo*, sporadic). Consanguinity is not relevant. Germline mosaicism is theoretically possible (as for any *de novo* disorder) but not specifically documented.
- **Carrier frequency:** Not applicable (dominant, *de novo*).
- **Epidemiology:** Ultra-rare; ~53 patients in the defining series with subsequent case reports. **No reliable prevalence/incidence estimate exists**; the disorder is under-ascertained.
- **Demographics:** No ethnic predilection established. Mouse models suggest possible sex-biased severity (male-biased cognitive deficits in the knock-in model [PMID: 42565830]), but human sex-ratio data are not established.

### 10. Diagnostics

- **Genetic testing (definitive):** Clinical whole-exome sequencing (WES) or whole-genome sequencing (WGS) identifying a heterozygous DLG4 variant; multi-gene neurodevelopmental/epilepsy/ID panels including DLG4; chromosomal microarray for larger 17p13.1 deletions. RNA/functional studies are required to interpret splice-site and deep-intronic variants (e.g., c.2105+235C>T identified by WGS) [PMID: 37525972, 42462545].
- **Phenotyping studies:** Brain MRI (may show cerebellar vermis atrophy); EEG including **sleep EEG/video-polygraphy** to detect ESES/DEE-SWAS [PMID: 38135915].
- **Biomarkers/laboratory tests:** No specific biochemical biomarker; diagnosis is molecular. No metabolic, proteomic, or metabolomic diagnostic markers.
- **Clinical criteria:** No formal consensus criteria; diagnosis rests on compatible neurodevelopmental phenotype plus a pathogenic DLG4 variant.
- **Differential diagnosis:** Other monogenic synaptopathies and neurodevelopmental disorders (e.g., SHANK-, SYNGAP1-, GRIN-, and other MAGUK/PSD-related disorders); Marfanoid habitus previously led to confusion but is not characteristic [PMID: 33597769].
- **Screening:** No population/newborn screening. Cascade testing is generally unnecessary given the *de novo* nature; parental testing informs recurrence-risk counseling.

### 11. Outcome/Prognosis

- **Survival/mortality:** No evidence of markedly reduced life expectancy; the disorder is non-degenerative. Mortality data are not established (ultra-rare).
- **Morbidity/function:** Substantial lifelong disability from intellectual disability, autism, epilepsy, and behavioral/sleep problems. Many individuals require lifelong support.
- **Disease course/complications:** Epilepsy (including refractory ESES/DEE-SWAS with associated regression), psychiatric complications (including treatment-resistant psychosis/catatonia in at least one adolescent [PMID: 37386468]), and orthopedic issues (scoliosis).
- **Prognostic factors:** Development of status epilepticus in sleep predicts regression [PMID: 38135915]; severity appears to correlate broadly with the degree of PSD-95 loss. No validated prognostic biomarkers.

### 12. Treatment

**No disease-modifying therapy exists.** Management is supportive and multidisciplinary.

| Modality | Details | NCIT suggestion |
|---|---|---|
| Antiseizure medications | Mainstay for epilepsy; ESES/DEE-SWAS forms often refractory; response variable across 35 patients [PMID: 38135915] | NCIT:C264 (Anticonvulsant Agent) |
| Antipsychotic (clozapine) | Effective for treatment-resistant psychosis/catatonia after failing 3 antipsychotics [PMID: 37386468] | NCIT:C371 (Clozapine) |
| Developmental/rehabilitative therapy | Physical, occupational, speech therapy; special education | NCIT:C15351 (Rehabilitation Therapy) |
| Sleep/behavioral management | For sleep disturbance and ASD/ADHD behaviors | — |
| Experimental PSD-95-directed agents | Nerinetide/Tat-NR2B9c, small molecules — developed for stroke/pain, NOT this disorder [PMID: 40712457] | — |

**Pharmacogenomics/gene/cell/RNA/targeted/immuno-therapies:** None established for this indication. Patient iPSC lines [PMID: 42462545] and patient-derived knock-in mice [PMID: 42565830] provide platforms for future therapeutic development.

### 13. Prevention

- **Primary prevention:** Not possible (*de novo* genetic origin).
- **Secondary/tertiary prevention:** Early developmental intervention; sleep-EEG surveillance to detect and treat ESES/DEE-SWAS early (to mitigate regression); management of complications (scoliosis, psychiatric symptoms).
- **Genetic counseling:** Recurrence risk is low for parents of a child with a confirmed *de novo* variant (bounded by the small possibility of parental germline mosaicism); affected individuals who reproduce carry a 50% transmission risk. Prenatal/preimplantation testing is technically possible for a known familial variant.

### 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** DLG4/PSD-95 is deeply conserved. Mouse *Dlg4* (NCBI Gene 13385, MGI:1277959); rat *Dlg4* (NCBI Gene 29495); zebrafish *dlg4a/dlg4b*; Drosophila *dlg1* (discs large); C. elegans *dlg-1*. The MAGUK PDZ–SH3–GK architecture is conserved from invertebrates to humans (Finding 10).
- **Natural disease in other species:** No naturally occurring DLG4 disorder is documented in companion animals or wildlife (OMIA); disease knowledge derives from engineered models.
- **Comparative/evolutionary:** High conservation of the scaffold and its receptor-clustering function underlies the strong translational validity of rodent models.

### 15. Model Organisms

| Model | Type | Key phenotype recapitulation | PMID |
|---|---|---|---|
| PSD-95-null mouse | Mammalian knockout | Enhanced hippocampal LTP; severely impaired spatial learning | [9853749] |
| PDZ1/2 ligand-binding-deficient PSD-95 knock-in | Mammalian knock-in | ↓PSD accumulation of PSD-95/PSD-93/AMPARs; abnormal anxiety; impaired spatial/working/remote memory | [23268962] |
| Dlg4−/− mouse | Mammalian knockout | Increased repetitive behavior; abnormal social/communication behavior; impaired motor coordination; anxiety | [20952458] |
| Dlg4 V692Wfs*12/+ patient-derived knock-in | Mammalian knock-in | Reduced PSD-95; learning/cognitive-flexibility deficits (male-biased); sleep abnormalities — "recapitulate several hallmark features of SHINE syndrome" | [42565830] |
| AOUMEYi004-A iPSC line (c.2155A>T p.Arg719*) | Human iPSC | Pluripotent; three-germ-layer differentiation; platform for neuronal modeling | [42462545] |

**Model strengths:** Rodent models robustly reproduce cognitive, behavioral, synaptic-plasticity, and (in the newest knock-in) sleep phenotypes, with a patient-specific variant. **Limitations:** Species differences in cognition/epilepsy; sex-specific effects require careful design; iPSC models capture cellular but not circuit-level phenotypes. **Resources:** MGI (Dlg4, MGI:1277959), IMPC, Cellosaurus (iPSC line).

---

## Mechanistic Model / Interpretation

DLG4-related synaptopathy is a textbook **haploinsufficiency synaptopathy**. The convergent evidence — extreme population-genetic constraint (pLI = 1.0, LOEUF = 0.14), a predominance of *de novo* protein-truncating variants, direct demonstration of reduced PSD-95 protein from a patient variant, and faithful recapitulation of cognitive/behavioral/sleep phenotypes in a patient-derived knock-in mouse — locks together into a single coherent causal chain: **one lost DLG4 allele → less PSD-95 → a disorganized glutamatergic postsynaptic density → impaired synaptic maturation and aberrant plasticity → abnormal circuit development → the SHINE clinical phenotype.**

Two clinically important nuances emerge. First, the relationship between synaptic plasticity and cognition is not simply "less plasticity = worse learning": PSD-95-null mice show *enhanced* LTP yet *impaired* learning [PMID: 9853749], indicating that PSD-95 sets the correct dynamic range and metaplasticity of synapses, not merely their strength. Second, epilepsy — specifically the ESES/DEE-SWAS subtype — is a modifiable driver of the worst outcomes (regression), making its early detection via sleep EEG a high-yield clinical priority [PMID: 38135915].

```
Population genetics        Molecular biology          Model systems              Clinic
─────────────────────      ─────────────────────      ─────────────────────      ─────────────────────
pLI=1.0, LOEUF=0.14   →    ↓PSD-95 protein       →    KO/KI mice: learning,  →   GDD, ID, ASD/ADHD,
(LoF not tolerated)        disorganized PSD           sleep, behavior deficits    epilepsy, sleep, hypotonia
                           (↓NMDAR/AMPAR clustering)  iPSC platform               (regression if ESES)
```

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [33597769](https://pubmed.ncbi.nlm.nih.gov/33597769/) | *DLG4-related synaptopathy: a new rare brain disorder* | Landmark cohort (n=53); defines disorder, name, core phenotype, *de novo* LoF mechanism, variant spectrum |
| [38135915](https://pubmed.ncbi.nlm.nih.gov/38135915/) | *Developmental epileptic encephalopathy in DLG4-related synaptopathy* | Epilepsy in ~50%; ESES/DEE-SWAS >25%; regression; EEG/MRI diagnostics; ASM response |
| [42565830](https://pubmed.ncbi.nlm.nih.gov/42565830/) | *Patient-derived mouse model reproduces SHINE syndrome* | Reduced PSD-95 protein; knock-in recapitulates hallmark features (sex-specific) |
| [9853749](https://pubmed.ncbi.nlm.nih.gov/9853749/) | *Enhanced LTP and impaired learning in PSD-95 mutant mice* | Synaptic-plasticity/learning link |
| [23268962](https://pubmed.ncbi.nlm.nih.gov/23268962/) | *PDZ1/2 ligand-binding-deficient PSD-95 knockin mice* | Receptor clustering, memory, anxiety deficits |
| [20952458](https://pubmed.ncbi.nlm.nih.gov/20952458/) | *Dlg4 deletion and ASD/Williams-relevant phenotypes* | ASD-relevant behavior in knockout |
| [29169997](https://pubmed.ncbi.nlm.nih.gov/29169997/) | *PSD95: schizophrenia or autism?* | PSD-95 scaffolding function; synaptogenesis role |
| [37386468](https://pubmed.ncbi.nlm.nih.gov/37386468/) | *Clozapine in adolescent with SHINE syndrome* | Treatment of treatment-resistant psychosis |
| [37525972](https://pubmed.ncbi.nlm.nih.gov/37525972/) | *Deep intronic DLG4 variant* | WGS diagnosis; protein-truncating predominance |
| [42462545](https://pubmed.ncbi.nlm.nih.gov/42462545/) | *hiPSC line from DLG4 patient (c.2155A>T p.Arg719*)* | WES diagnosis; iPSC modeling platform |
| [40444229](https://pubmed.ncbi.nlm.nih.gov/40444229/) | *Late-onset diagnosis of SHINE syndrome* | Under-ascertainment; SHINE acronym; AD inheritance |
| [40712457](https://pubmed.ncbi.nlm.nih.gov/40712457/) | *PSD-95/nNOS PPI disruption* | Experimental PSD-95-directed agents (stroke/pain, not this disorder) |
| [20554866](https://pubmed.ncbi.nlm.nih.gov/20554866/) | *NMDAR signaling complexes / lipid rafts* | PSD-95 organizes NMDAR complexes in vivo |

Additional supporting/context papers on PSD-95-interacting partners and MAGUK biology: [PMID: 18248606], [21878521], [37928066], [19467332], [29798891], [26609151].

## Limitations and Knowledge Gaps

- **Epidemiology:** No reliable prevalence or incidence; the entity is ultra-rare and under-ascertained. Sex ratio and age distribution in humans are undefined.
- **Human molecular profiling:** No published patient transcriptomic/proteomic/metabolomic datasets; mechanistic inference relies on rodent and in vitro models.
- **Genotype–phenotype correlation:** Not yet quantified — whether missense/hypomorphic vs truncating variants, or variant location within domains, predicts severity or epilepsy risk remains open.
- **Penetrance/expressivity:** Assumed high penetrance but not formally quantified; drivers of variable expressivity (including the ~50% epilepsy split) are unknown.
- **Therapeutics:** No disease-modifying therapy; supportive-care evidence is limited to retrospective series and single case reports.
- **Missense mechanism:** Whether some missense variants act by dominant-negative rather than simple loss-of-function is not fully resolved.

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** to derive prevalence, natural-history, sex-ratio, and genotype–phenotype data.
2. **Systematic sleep-EEG surveillance study** to define the incidence, timing, and treatment responsiveness of ESES/DEE-SWAS and its link to regression — a directly actionable clinical priority.
3. **Patient-iPSC-derived neuron/organoid profiling** (transcriptomics, proteomics, electrophysiology) to define human cell-autonomous consequences of PSD-95 loss and to build a drug-screening platform [building on PMID: 42462545].
4. **Genotype–phenotype analysis** across the expanding ClinVar/cohort variant set, stratified by variant type and PSD-95 domain, to test whether GK-domain or PDZ-domain variants confer distinct risks.
5. **Preclinical therapeutic testing** in the patient-derived knock-in mouse [PMID: 42565830] — e.g., ASO-mediated upregulation of the wild-type allele, or agents that stabilize the residual PSD, and rigorous evaluation of sex-specific responses.
6. **Prospective ASM comparative-effectiveness study** for the ESES/DEE-SWAS subtype, given its refractoriness and outsized impact on outcomes.

---

*Evidence types: human clinical [33597769, 38135915, 37386468, 40444229, 42462545, 37525972]; model organism [9853749, 23268962, 20952458, 42565830, 20554866]; in vitro / review [29169997, 40712457]; computational/population-genetic [gnomAD constraint, ClinVar].*


## Artifacts

- [OpenScientist final report](DLG4-Related_Synaptopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](DLG4-Related_Synaptopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.